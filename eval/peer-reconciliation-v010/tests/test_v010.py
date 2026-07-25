#!/usr/bin/env python3
"""Offline test suite for the v0.10 workspace. NO model calls; pure stdlib; deterministic.
Covers: the H1/H2 regeneration state machine (split budget, mixed-class transitions, max-3
generations, feedback-prompt content), conformance batching by generation index, the shared
parser grammar (every classification branch), the three serializers (4/5/6 excerpts,
first-document labeling, terminal-newline rule, baseline-A doc block), the scorer
(counterpart-identity adapter, directional mapping, two-direction combination table,
coverage numerator, §5 decision table + P=1.00 guardrail, sealed-hash custody), the
answer-blind load_pairs guard, make_pairs_manifest answer-blindness, and (via subprocess)
the gate-fidelity proof."""
import json, sys, os, hashlib, tempfile, subprocess, unittest
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WS))
sys.path.insert(0, str(WS / "scripts"))
import smoke_v010 as smoke
import serializers as ser
import parser_adjudicator as pa
import scorer_v010 as sc
import assemble as asm
import baseline_a, baseline_b
import attest, spend
import verify_gate_fidelity as vgf


# ----------------------------------------------------------------------------
# round-8: the spend log is per-H namespaced; unit tests stamp a fixed test H.
HT = "H-test-fixed-namespace"


class TestGateFidelity(unittest.TestCase):
    def test_verifier_passes(self):
        r = subprocess.run([sys.executable, str(WS / "scripts/verify_gate_fidelity.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("GATE-FIDELITY OK", r.stdout)


# ----------------------------------------------------------------------------
class TestConformanceRunner(unittest.TestCase):
    def test_conformance_runner_passes(self):
        r = subprocess.run([sys.executable, str(WS / "conformance_runner.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("0 failed", r.stdout)


class TestRegenStateMachine(unittest.TestCase):
    """H2 split budget (total cap 2, semantic sub-cap 1) + H1 feedback prompts."""
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._orig = smoke.RUNS
        smoke.RUNS = Path(self.tmp)
        for d in ("checklists", "definitions", "manifests"):
            (smoke.RUNS / d).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        smoke.RUNS = self._orig

    def _art(self, kind="lad"):
        a = smoke._new_artifact(kind, "a", "widget alpha", cli="claude", model="opus")
        # base prompt must exist for H1 write_regen_prompt to embed it
        smoke.base_prompt_path(kind, "a", "widget alpha").write_text("BASE PROMPT BODY\nEXCERPTS:\n1. foo")
        return a

    def _fail(self, a, gate):
        rows = []
        smoke._route_fail(None, a, gate, f"{gate}-detail-measured-value", rows)
        return rows

    def test_mechanical_budget_two_then_configfail(self):
        a = self._art()
        self.assertEqual((a["total_regens"], a["semantic_regens"]), (0, 0))
        self._fail(a, "mechanical")
        self.assertEqual((a["total_regens"], a["semantic_regens"], a["state"]), (1, 0, "pending_regen"))
        self._fail(a, "mechanical")
        self.assertEqual((a["total_regens"], a["state"]), (2, "pending_regen"))
        self._fail(a, "mechanical")
        self.assertEqual((a["total_regens"], a["state"]), (2, "configFail"))
        self.assertEqual(a["failed_gate"], "mechanical")

    def test_semantic_subcap_one(self):
        a = self._art()
        self._fail(a, "semantic")
        self.assertEqual((a["total_regens"], a["semantic_regens"], a["state"]), (1, 1, "pending_regen"))
        self._fail(a, "semantic")  # sem sub-cap hit even though total<2
        self.assertEqual((a["total_regens"], a["semantic_regens"], a["state"]), (1, 1, "configFail"))

    def test_mixed_semantic_then_mechanical_then_mechanical(self):
        a = self._art()
        self._fail(a, "semantic")    # total1 sem1
        self._fail(a, "mechanical")  # total2 sem1 (allowed: non-semantic)
        self.assertEqual((a["total_regens"], a["semantic_regens"], a["state"]), (2, 1, "pending_regen"))
        self._fail(a, "mechanical")  # total==2 -> configFail
        self.assertEqual(a["state"], "configFail")

    def test_mixed_mechanical_then_semantic_then_semantic(self):
        a = self._art()
        self._fail(a, "mechanical")  # total1 sem0
        self._fail(a, "semantic")    # total2 sem1
        self.assertEqual((a["total_regens"], a["semantic_regens"], a["state"]), (2, 1, "pending_regen"))
        self._fail(a, "semantic")    # total==2 -> configFail
        self.assertEqual(a["state"], "configFail")

    def test_leak_shares_total_budget(self):
        a = self._art()
        self._fail(a, "leak"); self._fail(a, "leak")
        self.assertEqual((a["total_regens"], a["state"]), (2, "pending_regen"))
        self._fail(a, "leak")
        self.assertEqual(a["state"], "configFail")

    def test_max_three_generations(self):
        a = self._art()
        gens_seen = [a["total_regens"]]  # g0
        for _ in range(2):
            self._fail(a, "mechanical"); gens_seen.append(a["total_regens"])
        # g0, g1, g2 = three generation indices before configFail
        self.assertEqual(gens_seen, [0, 1, 2])
        self._fail(a, "mechanical")
        self.assertEqual(a["state"], "configFail")

    def test_h1_feedback_prompt_written_with_gate_and_measure_and_cap(self):
        a = self._art()
        self._fail(a, "mechanical")
        pf = smoke.gen_prompt_path("lad", "a", "widget alpha", 1)
        self.assertTrue(pf.exists())
        body = pf.read_text()
        self.assertIn("mechanical", body)                       # failing gate identity
        self.assertIn("mechanical-detail-measured-value", body)  # measured value + cap detail
        self.assertIn("60-160 words", body)                     # cap in words (H1 _GATE_CAP)
        self.assertIn("BASE PROMPT BODY", body)                 # original task embedded
        # g0 uses the base (blind) prompt path, g>=1 the feedback path
        self.assertEqual(smoke.gen_prompt_path("lad", "a", "widget alpha", 0),
                         smoke.base_prompt_path("lad", "a", "widget alpha"))
        self.assertNotEqual(pf, smoke.base_prompt_path("lad", "a", "widget alpha"))

    def test_generate_malformed_consumes_total_not_semantic(self):
        a = self._art()
        self._fail(a, "generate")
        self.assertEqual((a["total_regens"], a["semantic_regens"]), (1, 0))


# ----------------------------------------------------------------------------
class TestConformanceBatchingByGenIndex(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._orig = smoke.RUNS
        smoke.RUNS = Path(self.tmp)
        for d in ("definitions", "checklists", "conformance", "manifests"):
            (smoke.RUNS / d).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        smoke.RUNS = self._orig

    def _ready_ladder(self, side, term, g):
        smoke.canon_path("chk", side, term, "txt").write_text("- commitment one\n- commitment two")
        smoke.canon_path("lad", side, term, "json").write_text(json.dumps(
            {"L0": "x.", "L1": "x y.", "L2": " ".join(["w"] * 70) + "."}))
        return {"kind": "lad", "side": side, "term": term, "total_regens": g,
                "semantic_regens": 0, "state": "awaiting_semantic", "log": [], "cli": "claude", "model": "opus"}

    def test_only_lowest_pending_index_staged_at_a_time(self):
        # round-5 anti-stranding: with terms at g0 AND g1 present, only the LOWEST index's
        # batch is staged (the g1 entrant waits so late entrants can coalesce before g1 opens).
        st = {"artifacts": {}, "conf_batches": {}, "polarity": {}, "polarity_side_fail": []}
        st["artifacts"]["lad:a:widget alpha"] = self._ready_ladder("a", "widget alpha", 0)
        st["artifacts"]["lad:a:widget beta"] = self._ready_ladder("a", "widget beta", 0)
        st["artifacts"]["lad:a:widget gamma"] = self._ready_ladder("a", "widget gamma", 1)  # later index waits
        smoke.gate_save(st)
        smoke.prompts_conformance([])
        st2 = smoke.gate_load()
        self.assertIn("a-g0", st2["conf_batches"])
        self.assertNotIn("a-g1", st2["conf_batches"])   # NOT staged while g0 is pending
        m0 = json.load(open(smoke.RUNS / "conformance/batch-a-g0.json"))
        self.assertEqual(m0["terms"], ["widget alpha", "widget beta"])  # term order
        self.assertEqual(m0["gen_index"], 0)


# ----------------------------------------------------------------------------
class TestParser(unittest.TestCase):
    A = pa.RELATION_ENUM_A
    B = pa.RELATION_ENUM_B

    def cls(self, text, enum=None):
        return pa.parse_adjudication(text, enum or self.A)["classification"]

    def test_well_formed_positive(self):
        t = ("match: yes\nmatched_term: gadget alpha prime\n"
             "relation: exact\nevidence: some verbatim span")
        r = pa.parse_adjudication(t, self.A)
        self.assertEqual(r["classification"], pa.POSITIVE)
        self.assertEqual(r["fields"]["matched_term"], "gadget alpha prime")
        self.assertEqual(r["fields"]["relation"], "exact")

    def test_well_formed_negative(self):
        t = "match: no\nmatched_term: none\nrelation: n/a\nevidence: none"
        self.assertEqual(self.cls(t), pa.NEGATIVE)

    def test_case_insensitive_keys_and_values(self):
        t = "MATCH: YES\nMatched_Term: gadget alpha prime\nRELATION: Exact\nEvidence: v"
        self.assertEqual(self.cls(t), pa.POSITIVE)

    def test_whitespace_tolerated(self):
        t = "  match :   no  \n matched_term :  none \n relation : n/a \n evidence : none "
        self.assertEqual(self.cls(t), pa.NEGATIVE)

    def test_extra_prose_ignored(self):
        t = ("Here is my analysis blah blah.\nmatch: yes\nmatched_term: gadget alpha prime\n"
             "relation: partial-overlap\nevidence: span\nThanks!")
        self.assertEqual(self.cls(t), pa.POSITIVE)

    def test_code_fence_ignored(self):
        t = "```\nmatch: no\nmatched_term: none\nrelation: n/a\nevidence: none\n```"
        self.assertEqual(self.cls(t), pa.NEGATIVE)

    def test_duplicate_field_malformed(self):
        t = "match: no\nmatch: yes\nmatched_term: none\nrelation: n/a\nevidence: none"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_missing_field_malformed(self):
        t = "match: no\nmatched_term: none\nrelation: n/a"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_invalid_match_enum(self):
        t = "match: maybe\nmatched_term: none\nrelation: n/a\nevidence: none"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_invalid_relation_enum(self):
        t = "match: yes\nmatched_term: x\nrelation: superMatch\nevidence: y"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_negative_cross_field_violation(self):
        # match=no but matched_term not none
        t = "match: no\nmatched_term: gadget alpha prime\nrelation: n/a\nevidence: none"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_positive_cross_field_violation_relation_na(self):
        t = "match: yes\nmatched_term: x\nrelation: n/a\nevidence: y"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_positive_cross_field_violation_empty_evidence(self):
        t = "match: yes\nmatched_term: x\nrelation: exact\nevidence: none"
        self.assertEqual(self.cls(t), pa.MALFORMED)

    def test_wrapper_quotes_stripped(self):
        t = 'match: yes\nmatched_term: "gadget alpha prime"\nrelation: exact\nevidence: "a span"'
        r = pa.parse_adjudication(t, self.A)
        self.assertEqual(r["fields"]["matched_term"], "gadget alpha prime")
        self.assertEqual(r["fields"]["evidence"], "a span")

    def test_arm_b_relation_enum(self):
        t = "match: yes\nmatched_term: x\nrelation: A-broader\nevidence: y"
        self.assertEqual(self.cls(t, self.B), pa.POSITIVE)
        # A-broader is NOT valid in arm A
        self.assertEqual(self.cls(t, self.A), pa.MALFORMED)


# ----------------------------------------------------------------------------
class TestSerializers(unittest.TestCase):
    def test_a_excerpts_4_5_6(self):
        for k in (4, 5, 6):
            out = ser.serialize_a_excerpts([f"ex{i}" for i in range(k)])
            lines = out.split("\n")
            self.assertEqual(len(lines), k)
            self.assertEqual(lines[0], "1. ex0")
            self.assertEqual(lines[-1], f"{k}. ex{k-1}")
            self.assertFalse(out.endswith("\n"))  # terminal-newline rule: none

    def test_a_excerpts_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            ser.serialize_a_excerpts(["x", "y", "z"])  # 3 < 4
        with self.assertRaises(ValueError):
            ser.serialize_a_excerpts([f"e{i}" for i in range(7)])  # 7 > 6

    def test_b_corpus_first_document_labeling_and_no_terminal_newline(self):
        docs = [("b/01", "alpha body"), ("b/02", "beta body")]
        out = ser.serialize_b_corpus(docs)
        self.assertTrue(out.startswith("=== DOCUMENT b/01 ==="))  # FIRST doc is labeled
        self.assertIn("=== DOCUMENT b/02 ===", out)
        self.assertIn("alpha body\n\n=== DOCUMENT b/02 ===", out)  # "\n\n" join
        self.assertFalse(out.endswith("\n"))

    def test_b_corpus_rstrips_doc_text(self):
        out = ser.serialize_b_corpus([("b/01", "body   \n\n")])
        self.assertEqual(out, "=== DOCUMENT b/01 ===\nbody")

    def test_baseline_a_docs_block(self):
        out = ser.serialize_baseline_a_docs([("b/07", "d7"), ("b/03", "d3"), ("b/09", "d9")])
        self.assertTrue(out.startswith("--- RANK 1 (document b/07) ---"))
        self.assertIn("--- RANK 2 (document b/03) ---", out)
        self.assertIn("--- RANK 3 (document b/09) ---", out)
        self.assertFalse(out.endswith("\n"))

    def test_concat_docs_text_excludes_headers(self):
        out = ser.concat_docs_text([("b/01", "alpha"), ("b/02", "beta")])
        self.assertEqual(out, "alpha\n\nbeta")


# ----------------------------------------------------------------------------
KEY = {  # synthetic toy key shape (mirrors scorer.verify_and_load_key output)
    "P01": {"term_a": "widget alpha", "term_b": "gadget alpha prime", "expected": "exactMatch", "broader_side": None},
    "P03": {"term_a": "widget gamma", "term_b": "gadget gamma small", "expected": "broadnarrow", "broader_side": "a"},
    "P05": {"term_a": "widget epsilon", "term_b": "gadget epsilon var", "expected": "relatedMatch", "broader_side": None},
    "P07": {"term_a": "toy echo slot", "term_b": "toy echo slot", "expected": "noMatchDespiteSimilarity", "broader_side": None},
    "P09": {"term_a": "widget theta", "term_b": "gadget kappa index", "expected": "noMatch", "broader_side": None},
}


class TestAdapterAndCombination(unittest.TestCase):
    def test_adapter_partner_passes(self):
        rec = {"final": "positive", "matched_term": "gadget alpha prime", "relation": "exact"}
        self.assertEqual(sc._adapt_direction(rec, "gadget alpha prime"), ("positive", "exact"))

    def test_adapter_non_partner_becomes_na(self):
        rec = {"final": "positive", "matched_term": "some other term", "relation": "exact"}
        self.assertEqual(sc._adapt_direction(rec, "gadget alpha prime"), ("NA",))

    def test_adapter_folds_case_and_quotes(self):
        rec = {"final": "positive", "matched_term": "GADGET Alpha  Prime", "relation": "exact"}
        self.assertEqual(sc._adapt_direction(rec, "gadget alpha prime")[0], "positive")

    def test_negative_and_no_assertion_passthrough(self):
        self.assertEqual(sc._adapt_direction({"final": "negative"}, "x"), ("negative",))
        self.assertEqual(sc._adapt_direction({"final": "no-assertion"}, "x"), ("NA",))

    def test_relation_mapping_directional(self):
        self.assertEqual(sc._map_relation("exact", "A", "a2b"), ("exactMatch", None))
        self.assertEqual(sc._map_relation("term-broader", "A", "a2b"), ("broadnarrow", "a"))
        self.assertEqual(sc._map_relation("corpus-broader", "A", "a2b"), ("broadnarrow", "b"))
        self.assertEqual(sc._map_relation("term-broader", "A", "b2a"), ("broadnarrow", "b"))
        self.assertEqual(sc._map_relation("corpus-broader", "A", "b2a"), ("broadnarrow", "a"))
        self.assertEqual(sc._map_relation("A-broader", "B", "a2b"), ("broadnarrow", "a"))
        self.assertEqual(sc._map_relation("B-broader", "B", "a2b"), ("broadnarrow", "b"))
        self.assertEqual(sc._map_relation("partial-overlap", "B", "a2b"), ("relatedMatch", None))

    def test_combination_both_exact(self):
        kp = KEY["P01"]
        v = sc._combine_two(("positive", ("exactMatch", None)), ("positive", ("exactMatch", None)), kp)
        self.assertEqual((v["proposed_relation"], v["status"]), ("exactMatch", "asserted"))

    def test_combination_both_broadnarrow_same_side(self):
        kp = KEY["P03"]
        v = sc._combine_two(("positive", ("broadnarrow", "a")), ("positive", ("broadnarrow", "a")), kp)
        self.assertEqual((v["proposed_relation"], v["broader_side"]), ("broadnarrow", "a"))

    def test_combination_broadnarrow_different_sides_related(self):
        kp = KEY["P03"]
        v = sc._combine_two(("positive", ("broadnarrow", "a")), ("positive", ("broadnarrow", "b")), kp)
        self.assertEqual(v["proposed_relation"], "relatedMatch")

    def test_combination_positive_negative_is_negative(self):
        kp = KEY["P09"]
        v = sc._combine_two(("positive", ("exactMatch", None)), ("negative",), kp)
        self.assertEqual((v["proposed_relation"], v["status"]), ("noMatch", "asserted"))

    def test_combination_positive_na_is_no_assertion(self):
        kp = KEY["P01"]
        v = sc._combine_two(("positive", ("exactMatch", None)), ("NA",), kp)
        self.assertEqual(v["status"], "no_assertion")

    def test_combination_negative_na_is_negative(self):
        kp = KEY["P09"]
        v = sc._combine_two(("negative",), ("NA",), kp)
        self.assertEqual(v["proposed_relation"], "noMatch")

    def test_combination_na_na_no_assertion(self):
        v = sc._combine_two(("NA",), ("NA",), KEY["P01"])
        self.assertEqual(v["status"], "no_assertion")

    def test_negative_jingle_maps_to_nmds(self):
        # P07 jingle: term_a == term_b -> sim_flag fires -> noMatchDespiteSimilarity
        v = sc._neg_verdict(KEY["P07"])
        self.assertEqual(v["proposed_relation"], "noMatchDespiteSimilarity")
        v9 = sc._neg_verdict(KEY["P09"])
        self.assertEqual(v9["proposed_relation"], "noMatch")


class TestScoreArmAndDecision(unittest.TestCase):
    def _perfect_tool_verdicts(self, key):
        # every pair correct
        out = {}
        for pid, kp in key.items():
            out[pid] = {"proposed_relation": kp["expected"], "status": "asserted",
                        "broader_side": kp.get("broader_side")}
        return out

    def full_key(self):
        return sc.verify_and_load_key(WS / "toy-key/key", WS / "toy-key/recorded-hashes.txt")

    def test_perfect_arm_is_fixed(self):
        key = self.full_key()
        v = self._perfect_tool_verdicts(key)
        s = sc.score_arm(key, v)
        self.assertEqual(s["S"], 10)
        self.assertEqual(s["P"], 1.0)
        self.assertEqual(s["C"], 1.0)
        self.assertEqual(s["jingle_specific"], 2)
        self.assertEqual(sc.decision_label(s)[0], "fixed")

    def test_promotion_breaks_precision(self):
        key = self.full_key()
        v = self._perfect_tool_verdicts(key)
        v["P09"] = {"proposed_relation": "exactMatch", "status": "asserted", "broader_side": None}  # promote a no-match
        s = sc.score_arm(key, v)
        self.assertLess(s["P"], 1.0)
        self.assertEqual(sc.decision_label(s)[0], "second miss (reported)")

    def test_all_abstain_precision_na_second_miss(self):
        key = self.full_key()
        v = {pid: {"proposed_relation": None, "status": "no_assertion", "broader_side": None} for pid in key}
        s = sc.score_arm(key, v)
        self.assertIsNone(s["P"])
        self.assertEqual(s["C"], 0.0)
        self.assertEqual(sc.decision_label(s)[0], "second miss (reported)")

    def test_coverage_counts_negatives_not_abstains(self):
        key = self.full_key()
        v = {}
        for pid, kp in key.items():
            if kp["expected"] in ("noMatch", "noMatchDespiteSimilarity"):
                v[pid] = {"proposed_relation": kp["expected"], "status": "asserted", "broader_side": None}
            else:
                v[pid] = {"proposed_relation": None, "status": "insufficient_evidence", "broader_side": None}
        s = sc.score_arm(key, v)
        self.assertEqual(s["C"], 0.4)  # 4 no-match pairs decided, 6 abstain

    def test_seven_correct_with_c_0_7_is_fixed_shortfall(self):
        key = self.full_key()
        v = self._perfect_tool_verdicts(key)
        # make 3 match pairs abstain: S=7, C=0.7 (7 decided), jingle=2, P=1.0
        for pid in ("P01", "P02", "P03"):
            v[pid] = {"proposed_relation": None, "status": "insufficient_evidence", "broader_side": None}
        s = sc.score_arm(key, v)
        self.assertEqual(s["S"], 7)
        self.assertEqual(s["C"], 0.7)
        self.assertEqual(s["P"], 1.0)
        label, why = sc.decision_label(s)
        self.assertEqual(label, "fixed")
        self.assertIn("shortfall", why)

    def test_jingle_zero_is_second_miss(self):
        key = self.full_key()
        v = self._perfect_tool_verdicts(key)
        # mistype both jingles as noMatch (still no promotion, still covered) -> jingle=0, S=8
        v["P07"] = {"proposed_relation": "noMatch", "status": "asserted", "broader_side": None}
        v["P08"] = {"proposed_relation": "noMatch", "status": "asserted", "broader_side": None}
        s = sc.score_arm(key, v)
        self.assertEqual(s["jingle_specific"], 0)
        self.assertGreaterEqual(s["S"], 7)
        self.assertEqual(sc.decision_label(s)[0], "second miss (reported)")


class TestSealedHashCustody(unittest.TestCase):
    def test_correct_hashes_load(self):
        key = sc.verify_and_load_key(WS / "toy-key/key", WS / "toy-key/recorded-hashes.txt")
        self.assertEqual(len(key), 10)
        self.assertEqual(key["P03"]["expected"], "broadnarrow")
        self.assertEqual(key["P03"]["broader_side"], "a")

    def test_wrong_hash_aborts(self):
        tmp = tempfile.mkdtemp()
        Path(tmp, "recorded.txt").write_text(
            "0000000000000000000000000000000000000000000000000000000000000000  key/answer_key.json\n"
            "0000000000000000000000000000000000000000000000000000000000000000  key/concepts.json\n")
        with self.assertRaises(SystemExit):
            sc.verify_and_load_key(WS / "toy-key/key", Path(tmp, "recorded.txt"))

    def test_missing_recorded_hash_aborts(self):
        tmp = tempfile.mkdtemp()
        Path(tmp, "recorded.txt").write_text("")  # no recorded hashes at all
        with self.assertRaises(SystemExit):
            sc.verify_and_load_key(WS / "toy-key/key", Path(tmp, "recorded.txt"))


class TestAnswerBlindness(unittest.TestCase):
    def test_load_pairs_rejects_answer_fields(self):
        tmp = tempfile.mkdtemp()
        bad = Path(tmp, "pairs.json")
        bad.write_text(json.dumps({"pairs": [
            {"pair_id": "P01", "term_a": "x", "term_b": "y", "expected": "exactMatch"}]}))
        orig = smoke.PAIRS_MANIFEST
        smoke.PAIRS_MANIFEST = bad
        try:
            with self.assertRaises(SystemExit):
                smoke.load_pairs()
        finally:
            smoke.PAIRS_MANIFEST = orig

    def test_pairs_json_carries_no_answer_fields(self):
        pairs = json.load(open(WS / "toy-key/pairs.json"))["pairs"]
        for p in pairs:
            self.assertEqual(set(p), {"pair_id", "term_a", "term_b"})

    def test_make_pairs_manifest_discards_answers(self):
        tmp = tempfile.mkdtemp()
        out = Path(tmp, "pairs.json")
        subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                        str(WS / "toy-key/key"), str(out)], check=True, capture_output=True)
        pairs = json.load(open(out))["pairs"]
        for p in pairs:  # check KEYS (substring match would false-positive: "score" ⊃ "core")
            self.assertEqual(set(p), {"pair_id", "term_a", "term_b"})


class TestBaselineVerdictsEndToEnd(unittest.TestCase):
    def full_key(self):
        return sc.verify_and_load_key(WS / "toy-key/key", WS / "toy-key/recorded-hashes.txt")

    def test_baseline_a_partner_exact_both_dirs(self):
        key = self.full_key()
        recs = {
            "a:widget alpha": {"final": "positive", "matched_term": "gadget alpha prime", "relation": "exact"},
            "b:gadget alpha prime": {"final": "positive", "matched_term": "widget alpha", "relation": "exact"},
        }
        v = sc.baseline_a_verdicts(key, recs)
        self.assertEqual(v["P01"]["proposed_relation"], "exactMatch")

    def test_baseline_a_non_partner_positive_excluded(self):
        key = self.full_key()
        # A-term says it matches the WRONG b-term -> adapter NA; b-term abstains -> NA/NA -> no_assertion
        recs = {"a:widget alpha": {"final": "positive", "matched_term": "gadget zeta var", "relation": "exact"}}
        v = sc.baseline_a_verdicts(key, recs)
        self.assertEqual(v["P01"]["status"], "no_assertion")

    def test_baseline_b_partner_broadnarrow(self):
        key = self.full_key()
        recs = {"P03": {"final": "positive", "matched_term": "gadget gamma small", "relation": "A-broader"}}
        v = sc.baseline_b_verdicts(key, recs)
        self.assertEqual((v["P03"]["proposed_relation"], v["P03"]["broader_side"]), ("broadnarrow", "a"))

    def test_baseline_b_negative_jingle(self):
        key = self.full_key()
        recs = {"P07": {"final": "negative"}}
        v = sc.baseline_b_verdicts(key, recs)
        self.assertEqual(v["P07"]["proposed_relation"], "noMatchDespiteSimilarity")


class TestBugFixes(unittest.TestCase):
    """BUG-1 single-document grounding + BUG-2 single-pass substitution (fixture-audit fixes)."""
    DOCS = [("b/01", "alpha beta"), ("b/02", "gamma delta")]

    def test_grounding_distinct_docs_ok(self):
        # matched_term in doc1, evidence within doc2 -> each individually grounded -> True
        for gr in (baseline_a._ground, baseline_b._ground):
            self.assertTrue(gr({"matched_term": "alpha", "evidence": "gamma delta"}, self.DOCS))

    def test_grounding_boundary_spanning_rejected(self):
        # "beta gamma" spans the b/01|b/02 boundary; in NO single doc -> False
        for gr in (baseline_a._ground, baseline_b._ground):
            self.assertFalse(gr({"matched_term": "alpha", "evidence": "beta gamma"}, self.DOCS))

    def test_grounding_boundary_spanning_singleword_docs_rejected(self):
        docs = [("b/01", "alpha"), ("b/02", "beta")]
        self.assertFalse(baseline_a._ground({"matched_term": "alpha", "evidence": "alpha beta"}, docs))

    def test_grounding_both_in_one_doc_ok(self):
        self.assertTrue(baseline_b._ground({"matched_term": "alpha", "evidence": "alpha beta"}, self.DOCS))

    def test_grounding_absent_field_rejected(self):
        self.assertFalse(baseline_a._ground({"matched_term": "alpha", "evidence": "not present anywhere"}, self.DOCS))

    def test_single_pass_substitution_preserves_placeholder_in_excerpt(self):
        out = asm.assemble_baseline_b("coin inj",
                                      ["contains {B_CORPUS} literally", "ex one", "ex two", "ex three"],
                                      [("b/01", "doc one body"), ("b/02", "doc two body")])
        # the literal token from the excerpt must survive verbatim (NOT re-substituted)
        self.assertIn("1. contains {B_CORPUS} literally", out)
        # and the real corpus is still inserted exactly once (at the {B_CORPUS} placeholder)
        self.assertEqual(out.count("=== DOCUMENT b/01 ==="), 1)
        self.assertEqual(out.count("=== DOCUMENT b/02 ==="), 1)

    def test_single_pass_substitution_baseline_a_doc_placeholder(self):
        out = asm.assemble_baseline_a("alpha coin",
                                      [("b/07", "body containing {TERM} inside it"), ("b/03", "d two"), ("b/09", "d three")])
        self.assertIn("body containing {TERM} inside it", out)
        self.assertIn('TERM: "alpha coin"', out)

    def test_single_pass_normal_inputs_unchanged(self):
        # single-pass must produce identical bytes to the plain template fill for benign inputs
        docs = [(f"b/{i:02d}", f"doc {i} body") for i in range(1, 12)]
        out = asm.assemble_baseline_b("widget alpha", ["e0", "e1", "e2", "e3", "e4"], docs)
        self.assertIn('COMMUNITY A TERM: "widget alpha"', out)
        self.assertTrue(out.endswith("\n"))
        self.assertEqual(out.count("{B_CORPUS}"), 0)  # placeholder consumed


class TestReviewFixes(unittest.TestCase):
    """Adversarial-review fixes: opaque-id blindness, whitelist/symlink, spend lock,
    H self-check, fidelity global-mutation catch, mixed-wrapper quotes, opaque join."""
    CANON = ["exactMatch", "exactMatch", "broadnarrow", "broadnarrow", "relatedMatch",
             "relatedMatch", "noMatchDespiteSimilarity", "noMatchDespiteSimilarity", "noMatch", "noMatch"]

    def _make_pairs(self, key_dir, out):
        subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"), str(key_dir), str(out)],
                       check=True, capture_output=True)

    # ---- P0: opaque randomized shuffled ids, no class-recoverable ordering ----
    def test_opaque_ids_and_shuffle_blindness(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"
        self._make_pairs(WS / "toy-key/key", out)
        pairs = json.load(open(out))["pairs"]
        # opaque ids: 16-hex, none positional like P0x
        for p in pairs:
            self.assertRegex(p["pair_id"], r"^[0-9a-f]{16}$")
            self.assertNotRegex(p["pair_id"], r"^P\d")
        # order = sorted-by-id (deterministic, key-independent)
        self.assertEqual([p["pair_id"] for p in pairs], sorted(p["pair_id"] for p in pairs))
        # class sequence along the manifest order is NOT the canonical class order (shuffled)
        ak = {(p["term_a"], p["term_b"]): p["expected"]
              for p in json.load(open(WS / "toy-key/key/answer_key.json"))["pairs"]}
        seq = [ak[(p["term_a"], p["term_b"])] for p in pairs]
        self.assertNotEqual(seq, self.CANON)
        # determinism: rebuild -> identical bytes
        out2 = tmp / "pairs2.json"; self._make_pairs(WS / "toy-key/key", out2)
        self.assertEqual(out.read_bytes(), out2.read_bytes())

    def test_make_pairs_stdout_is_only_hash(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"), str(WS / "toy-key/key"), str(out)],
                           check=True, capture_output=True, text=True)
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        self.assertEqual(len(lines), 1)
        self.assertRegex(lines[0], r"^pairs_sha256: [0-9a-f]{64}$")
        self.assertEqual(lines[0].split()[1], hashlib.sha256(out.read_bytes()).hexdigest())

    # ---- P1: load_pairs symlink + strict whitelist ----
    def _with_manifest(self, path):
        orig = smoke.PAIRS_MANIFEST
        smoke.PAIRS_MANIFEST = Path(path)
        self.addCleanup(lambda: setattr(smoke, "PAIRS_MANIFEST", orig))

    def test_load_pairs_rejects_symlink(self):
        tmp = Path(tempfile.mkdtemp())
        real = tmp / "real.json"
        real.write_text(json.dumps({"count": 1, "pairs": [{"pair_id": "x", "term_a": "a", "term_b": "b"}]}))
        link = tmp / "pairs.json"; os.symlink(real, link)
        self._with_manifest(link)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_rejects_path_under_key_dir(self):
        tmp = Path(tempfile.mkdtemp()); (tmp / "key").mkdir()
        f = tmp / "key" / "pairs.json"
        f.write_text(json.dumps({"count": 1, "pairs": [{"pair_id": "x", "term_a": "a", "term_b": "b"}]}))
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_rejects_extra_top_level_field(self):
        tmp = Path(tempfile.mkdtemp()); f = tmp / "pairs.json"
        f.write_text(json.dumps({"count": 1, "pairs": [{"pair_id": "x", "term_a": "a", "term_b": "b"}], "note": "x"}))
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_rejects_extra_record_field(self):
        tmp = Path(tempfile.mkdtemp()); f = tmp / "pairs.json"
        f.write_text(json.dumps({"count": 1, "pairs": [{"pair_id": "x", "term_a": "a", "term_b": "b", "expected": "exactMatch"}]}))
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_rejects_count_mismatch(self):
        tmp = Path(tempfile.mkdtemp()); f = tmp / "pairs.json"
        f.write_text(json.dumps({"count": 2, "pairs": [{"pair_id": "x", "term_a": "a", "term_b": "b"}]}))
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_accepts_valid(self):
        self._with_manifest(WS / "toy-key/pairs.json")
        pairs = smoke.load_pairs()
        self.assertEqual(len(pairs), 10)

    # ---- P2: slug collision / empty slug ----
    def test_load_pairs_rejects_slug_collision(self):
        tmp = Path(tempfile.mkdtemp()); f = tmp / "pairs.json"
        f.write_text(json.dumps({"count": 2, "pairs": [
            {"pair_id": "1", "term_a": "Foo Bar", "term_b": "x"},
            {"pair_id": "2", "term_a": "foo!bar", "term_b": "y"}]}))  # both slug -> 'foo-bar'
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    def test_load_pairs_rejects_empty_slug(self):
        tmp = Path(tempfile.mkdtemp()); f = tmp / "pairs.json"
        f.write_text(json.dumps({"count": 1, "pairs": [{"pair_id": "1", "term_a": "字字", "term_b": "y"}]}))
        self._with_manifest(f)
        with self.assertRaises(SystemExit):
            smoke.load_pairs()

    # ---- spend-state lock enforcement (atomic-claim model) ----
    def _ready_log(self, tmp):
        """a log in the state the driver leaves right before the scorer: structure:read + one
        scoring-attempt."""
        log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)
        return log

    def test_claim_one_shot(self):
        tmp = Path(tempfile.mkdtemp()); log = self._ready_log(tmp)
        spend.claim_authorized_read(log, HT)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log, HT)  # a second claim is refused (already spent)

    def test_scoring_attempt_capped_at_two(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)
        spend.append_event(log, "state:scoring-attempt", HT)  # 2nd OK
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt", HT)  # 3rd refused

    def test_spend_accidental_blocks_everything(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "spend:accidental-access-during-gen", HT)
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt", HT)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)

    def test_scorer_gate_refuses_after_claim(self):
        tmp = Path(tempfile.mkdtemp()); log = self._ready_log(tmp)
        spend.assert_scoring_allowed(log, HT)          # allowed (structure:read + attempt, no claim)
        spend.claim_authorized_read(log, HT)           # claim (key now spent)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)      # a second scorer run is refused (claim present)

    # ---- P1: H self-consistency ----
    def test_H_self_check_catches_tamper(self):
        tmp = Path(tempfile.mkdtemp()); hf = tmp / "H.json"
        man = {"v010_files": {"a.py": "deadbeef"}, "x": 1}
        good = attest.hashlib.sha256(attest._canonical(man)).hexdigest()
        hf.write_text(json.dumps({"H": good, "manifest_of_manifests": man}))
        self.assertEqual(attest.load_and_verify_H(hf)["H"], good)   # consistent -> loads
        man["v010_files"]["a.py"] = "cafebabe"                      # tamper per-file hash, keep old H
        hf.write_text(json.dumps({"H": good, "manifest_of_manifests": man}))
        with self.assertRaises(SystemExit):
            attest.load_and_verify_H(hf)

    # ---- P1: fidelity proof catches a mutated module global ----
    def test_fidelity_catches_mutated_global(self):
        tmp = Path(tempfile.mkdtemp())
        ref = tmp / "ref.py"; new = tmp / "new.py"
        ref.write_text((WS / ".." / "peer-reconciliation-test3" / "smoke.py").read_text())
        # the real v0.10 controller, but with ONE carried gate-dependency global mutated
        # (function text unchanged) — the extended proof must catch it.
        mutated = (WS / "smoke_v010.py").read_text().replace(
            'VERDICT_ENUM = {"instantiates", "contradicts", "insufficient"}',
            'VERDICT_ENUM = {"instantiates", "contradicts", "insufficient", "SNUCK_IN"}')
        self.assertIn("SNUCK_IN", mutated)   # guard: the replace actually fired
        new.write_text(mutated)
        errors, _ = vgf.compare_modules(new, ref)
        self.assertTrue(any("global DRIFTED" in e and "VERDICT_ENUM" in e for e in errors), errors)

    def test_fidelity_clean_copy_passes(self):
        tmp = Path(tempfile.mkdtemp())
        ref = tmp / "ref.py"; new = tmp / "new.py"
        ref.write_text((WS / ".." / "peer-reconciliation-test3" / "smoke.py").read_text())
        new.write_text((WS / "smoke_v010.py").read_text())
        errors, _ = vgf.compare_modules(new, ref)
        self.assertEqual(errors, [])

    # ---- P2: mixed-wrapper quotes not stripped ----
    def test_mixed_wrapper_quotes_not_stripped(self):
        r1 = pa.parse_adjudication('match: yes\nmatched_term: "x”\nrelation: exact\nevidence: y', pa.RELATION_ENUM_A)
        self.assertEqual(r1["fields"]["matched_term"], '"x”')     # ASCII open + curly close: kept
        r2 = pa.parse_adjudication('match: yes\nmatched_term: “x"\nrelation: exact\nevidence: y', pa.RELATION_ENUM_A)
        self.assertEqual(r2["fields"]["matched_term"], '“x"')     # curly open + ASCII close: kept
        r3 = pa.parse_adjudication('match: yes\nmatched_term: “x”\nrelation: exact\nevidence: y', pa.RELATION_ENUM_A)
        self.assertEqual(r3["fields"]["matched_term"], "x")       # matched curly pair: stripped

    # ---- P0/scorer: opaque term-pair join ----
    def test_scorer_opaque_join(self):
        sealed = sc.verify_and_load_key(WS / "toy-key/key", WS / "toy-key/recorded-hashes.txt")
        key_opaque = sc._join_opaque(sealed, WS / "toy-key/pairs.json")
        # keys are the opaque ids from pairs.json (not P01-P10), expected resolved via term pair
        opaque_ids = {p["pair_id"] for p in json.load(open(WS / "toy-key/pairs.json"))["pairs"]}
        self.assertEqual(set(key_opaque), opaque_ids)
        for oid, kp in key_opaque.items():
            self.assertRegex(oid, r"^[0-9a-f]{16}$")
            self.assertIn(kp["expected"], ("exactMatch", "broadnarrow", "relatedMatch",
                                           "noMatch", "noMatchDespiteSimilarity"))


class TestRev9Closures(unittest.TestCase):
    """rev-9 cross-check closures: typed structure-read in the one spend log; projector hash
    gate; pairs.json §3.6 schema fixture kind."""
    # ---- 1: typed structure-read + scorer gate semantics ----
    def test_second_structure_read_refused(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        with self.assertRaises(SystemExit):
            spend.append_event(log, "structure:read", HT)

    def test_scorer_passes_with_one_structure_read(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)
        spend.assert_scoring_allowed(log, HT)   # must NOT raise (one structure-read + attempt, no claim)

    def test_scorer_refuses_zero_structure_reads(self):   # round-5: the >1-only bug fix
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "state:scoring-attempt", HT)  # attempt but NO structure:read
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log, HT)              # claim also requires exactly one

    def test_scorer_refuses_untyped_entry(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        # an untyped entry IN the current-H namespace must trip the untyped-entry refusal
        log.write_text(json.dumps({"event": "bogus:thing", "run_H": HT, "utc": "x"}) + "\n")
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)

    def test_scorer_refuses_answer_read_entry(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)
        spend.claim_authorized_read(log, HT)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)

    def test_one_pre_read_failure_then_relaunch(self):    # round-5: bounded relaunch path
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)  # attempt 1 (scorer fails pre-read, no claim)
        spend.append_event(log, "state:scoring-attempt", HT)  # attempt 2 (the ONE relaunch)
        spend.claim_authorized_read(log, HT)                  # relaunch reaches the claim -> OK
        spend.complete_authorized_read(log, HT)
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt", HT)  # a 3rd attempt is refused

    def test_crash_after_claim_refuses_second_invocation(self):  # round-5: post-read crash
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)
        spend.claim_authorized_read(log, HT)                  # claim, then "crash" (no complete)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT)             # second invocation refused (spent)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log, HT)              # cannot re-claim

    # ---- 2: projector hash gate + the (driver-logged) per-H structure:read custody entry ----
    def test_projector_emits_pairs_and_driver_logs_structure_read(self):
        # round-8: the projector no longer writes the spend log (it runs at phase 0.5 before H
        # exists). It emits pairs.json on a valid hash; the DRIVER logs the per-H structure:read
        # after build-H. Here we exercise both halves.
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"; log = tmp / "spend.jsonl"
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            str(WS / "toy-key/key"), str(out),
                            "--recorded-hashes", str(WS / "toy-key/recorded-hashes.txt")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(out.exists())
        self.assertFalse(log.exists())     # the projector itself touched no spend log
        # the driver's post-build-H custody entry (one-shot, per-H)
        self.assertFalse(spend.projector_completed(log, HT))
        spend.append_event(log, "structure:read", HT)
        self.assertTrue(spend.projector_completed(log, HT))
        self.assertEqual([e["event"] for e in spend.read_events(log)], ["structure:read"])

    def test_projector_aborts_on_hash_mismatch_nothing_read(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"
        bad = tmp / "bad-recorded.txt"
        bad.write_text("0000000000000000000000000000000000000000000000000000000000000000  key/concepts.json\n"
                       "0000000000000000000000000000000000000000000000000000000000000000  key/answer_key.json\n")
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            str(WS / "toy-key/key"), str(out),
                            "--recorded-hashes", str(bad)],
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ABORT (nothing read)", r.stdout + r.stderr)
        self.assertFalse(out.exists())               # nothing written

    # ---- 3: pairs_manifest schema fixture kind is exercised ----
    def test_pairs_manifest_fixtures_present_and_pass(self):
        import make_pairs_manifest as mpm
        fx = list((WS / "fixtures").glob("pairs_manifest_*.json"))
        self.assertGreaterEqual(len(fx), 3)
        for f in fx:
            obj = json.load(open(f))
            got = mpm.build_payload([tuple(tp) for tp in obj["term_pairs"]])
            self.assertEqual(got, obj["expect"])
            for r in got["pairs"]:
                self.assertRegex(r["pair_id"], r"^[0-9a-f]{16}$")
                self.assertEqual(set(r), {"pair_id", "term_a", "term_b"})


class TestRound5(unittest.TestCase):
    """round-5: conformance-batching anti-stranding + strengthened attestation."""

    # ---- item 4: batching coalesces a late entrant (no stranding) ----
    def _write_conf_out(self, runs, bid, r, rows):
        out = runs / f"conformance/out-{bid}-r{r}.json"; out.write_text(json.dumps(rows))
        mf = runs / f"manifests/conf-{bid}-r{r}.json"
        mf.write_text(f"exit: 0\nout_sha256: {hashlib.sha256(out.read_bytes()).hexdigest()}\n")

    def test_batching_coalesces_late_entrant(self):
        tmp = Path(tempfile.mkdtemp()); orig = smoke.RUNS; smoke.RUNS = tmp
        try:
            for d in ("definitions", "checklists", "conformance", "manifests"):
                (tmp / d).mkdir(parents=True, exist_ok=True)
            def ready(term, g, sem):
                smoke.canon_path("chk", "a", term, "txt").write_text("- c1\n- c2")
                smoke.canon_path("lad", "a", term, "json").write_text(
                    json.dumps({"L0": "x.", "L1": "x y.", "L2": " ".join(["w"] * 70) + "."}))
                smoke.base_prompt_path("lad", "a", term).write_text("BASE\nEXCERPTS:\n1. foo")  # for H1 regen
                return {"kind": "lad", "side": "a", "term": term, "total_regens": g,
                        "semantic_regens": sem, "state": "awaiting_semantic", "log": [],
                        "cli": "claude", "model": "opus"}
            st = {"artifacts": {}, "conf_batches": {}, "polarity": {}, "polarity_side_fail": []}
            st["artifacts"]["lad:a:xterm"] = ready("xterm", 1, 0)  # mechanical g0-fail -> g1
            st["artifacts"]["lad:a:yterm"] = ready("yterm", 0, 0)  # will semantic-fail at g0
            smoke.gate_save(st)
            # iter1: lowest pending index g0 -> stage a-g0 with [yterm] ONLY (xterm at g1 waits)
            smoke.prompts_conformance([])
            st1 = smoke.gate_load()
            self.assertIn("a-g0", st1["conf_batches"]); self.assertNotIn("a-g1", st1["conf_batches"])
            self.assertEqual(json.load(open(tmp / "conformance/batch-a-g0.json"))["terms"], ["yterm"])
            # yterm judged nonconformant -> regenerates to g1
            self._write_conf_out(tmp, "a-g0", 0, [{"item": 1, "verdict": "nonconformant", "reason": "dropped mechanism"}])
            smoke.gate_conformance([])
            st2 = smoke.gate_load(); y = st2["artifacts"]["lad:a:yterm"]
            self.assertEqual((y["total_regens"], y["state"]), (1, "pending_regen"))
            y["state"] = "awaiting_semantic"; smoke.gate_save(st2)   # simulate g1 mech+leak pass
            # iter2: a-g0 resolved -> lowest index now g1 -> ONE batch with BOTH entrants coalesced
            smoke.prompts_conformance([])
            self.assertEqual(sorted(json.load(open(tmp / "conformance/batch-a-g1.json"))["terms"]),
                             ["xterm", "yterm"])
            self._write_conf_out(tmp, "a-g1", 0, [{"item": 1, "verdict": "conformant", "reason": ""},
                                                  {"item": 2, "verdict": "conformant", "reason": ""}])
            smoke.gate_conformance([])
            smoke.assert_resolved([])   # must NOT sys.exit — nothing stranded
            st3 = smoke.gate_load()
            self.assertEqual(st3["artifacts"]["lad:a:xterm"]["state"], "passed")
            self.assertEqual(st3["artifacts"]["lad:a:yterm"]["state"], "passed")
        finally:
            smoke.RUNS = orig

    # ---- item 3: strengthened attestation ----
    def _min_man(self, base):
        return {"v010_files": attest._inventory(attest.INVENTORY_GLOBS, base),
                "runtime_answer_blind_files": {},
                "inherited_recorded": {"corpora": {}, "bge_snapshot_tree_sha256": "x",
                                       "sealed_key_recorded_hashes_BOUND_NOT_REHASHED": {"k": "v"}}}

    def test_verify_files_fails_on_missing_runtime(self):
        base = Path(tempfile.mkdtemp()); (base / "x.py").write_text("z")
        man = self._min_man(base); man["runtime_answer_blind_files"] = {"pairs.json": "d" * 64}
        self.assertTrue(any("runtime file drift/MISSING: pairs.json" in e
                            for e in attest._verify_files_errs(man, base)))

    def test_verify_files_fails_on_extra_runtime(self):
        base = Path(tempfile.mkdtemp()); (base / "pairs.json").write_text("{}")
        self.assertTrue(any("on disk NOT in H: pairs.json" in e
                            for e in attest._verify_files_errs(self._min_man(base), base)))

    def test_verify_files_fails_on_missing_corpus(self):
        base = Path(tempfile.mkdtemp())
        man = self._min_man(base); man["inherited_recorded"]["corpora"] = {"corpora/a/01.md": "c" * 64}
        self.assertTrue(any("corpus MISSING" in e for e in attest._verify_files_errs(man, base)))

    def test_recorded_artifacts_match_frozen_record(self):
        errs = attest.verify_recorded_artifacts(attest.RECORDED_MANIFEST, WS)
        self.assertEqual(errs, [], errs)   # 7 prompts + split + gen_leakcheck + run_isolated

    def test_recorded_artifacts_detect_drift(self):
        tmp = Path(tempfile.mkdtemp()); bogus = tmp / "rec.txt"
        bogus.write_text("0000000000000000000000000000000000000000000000000000000000000000  run_isolated.sh\n")
        self.assertTrue(attest.verify_recorded_artifacts(bogus, WS))  # non-empty errs

    def test_bge_tree_hash_deterministic_and_change_detecting(self):
        d = Path(tempfile.mkdtemp()); (d / "sub").mkdir()
        (d / "a.bin").write_text("alpha"); (d / "sub" / "b.bin").write_text("beta")
        h1 = attest.bge_tree_hash(d); h2 = attest.bge_tree_hash(d)
        self.assertEqual(h1, h2)
        man_ok = {"inherited_recorded": {"bge_snapshot_tree_sha256": h1}}
        self.assertEqual(attest.check_bge(man_ok, d), [])
        (d / "a.bin").write_text("ALPHA")                 # mutate a file
        self.assertTrue(attest.check_bge(man_ok, d))      # now mismatches -> errs
        self.assertTrue(attest.check_bge({"inherited_recorded": {"bge_snapshot_tree_sha256": "z"}}, d))


class TestRound6(unittest.TestCase):
    """round-6: executable setup (splitter path + leak checks), alias pinning at the boundary,
    spend/driver terminal+resume closure, H/attestation freeze-package completeness."""

    # ---- finding 1: confirmatory setup constructs a valid, leak-checked draw ----
    def _gen_blocks(self, terms):
        blocks = []
        for i in range(1, 12):
            t1, t2 = terms[(i - 1) % len(terms)], terms[i % len(terms)]
            blocks.append(f"<<<DOC {i}>>>\n# Report {i}\nThe {t1} and {t2} runs completed with logged results.")
        return "\n".join(blocks) + "\n"

    def test_setup_corpus_attempt_valid_and_leak_detected(self):
        import setup_confirmatory as sc
        kd = Path(tempfile.mkdtemp()) / "conf"; (kd / "key").mkdir(parents=True)
        (kd / "key" / "concepts.json").write_text((WS / "toy-key/key/concepts.json").read_text())
        subprocess.run([sys.executable, str(WS / "harness/validate_key.py"), str(kd / "key/concepts.json")],
                       check=True, capture_output=True)
        subprocess.run([sys.executable, str(WS / "harness/gen_leakcheck.py"), str(kd)],
                       check=True, capture_output=True)
        ak = json.load(open(kd / "key/answer_key.json"))
        a_terms = [p["term_a"] for p in ak["pairs"]]; b_terms = [p["term_b"] for p in ak["pairs"]]
        (kd / "runs").mkdir(parents=True, exist_ok=True)
        (kd / "runs/gen-a.out").write_text(self._gen_blocks(a_terms))
        (kd / "runs/gen-b.out").write_text(self._gen_blocks(b_terms))
        sc.copy_splitter(kd)
        # valid draw: 11 docs per side UNDER the key dir + all frozen leak checks pass
        self.assertTrue(sc._corpus_attempt_ok(kd, "a", kd / "runs/gen-a.out"))
        self.assertTrue(sc._corpus_attempt_ok(kd, "b", kd / "runs/gen-b.out"))
        self.assertEqual(len(list((kd / "corpora/a").glob("[0-9][0-9].md"))), 11)
        self.assertEqual(len(list((kd / "corpora/b").glob("[0-9][0-9].md"))), 11)
        # NEGATIVE: a b-term leaked into an a-doc fails cross-a -> attempt rejected
        bad = self._gen_blocks(a_terms).replace("logged results.",
                                                f"logged results. Also {b_terms[3]} appeared.", 1)
        (kd / "runs/gen-a-bad.out").write_text(bad)
        self.assertFalse(sc._corpus_attempt_ok(kd, "a", kd / "runs/gen-a-bad.out"))

    def test_split_writes_under_key_dir_not_harness(self):
        import setup_confirmatory as sc
        kd = Path(tempfile.mkdtemp()) / "conf"; (kd / "runs").mkdir(parents=True)
        (kd / "runs/gen-a.out").write_text(self._gen_blocks(["alpha term", "beta term"]))
        splitter = sc.copy_splitter(kd)
        self.assertEqual(sc._sha(splitter), sc.SPLIT_RECORDED)   # hash-verified copy
        subprocess.run([sys.executable, str(splitter), "a", str(kd / "runs/gen-a.out")], check=True, capture_output=True)
        self.assertEqual(len(list((kd / "corpora/a").glob("[0-9][0-9].md"))), 11)  # under KEY dir

    # ---- finding 2: alias pinning at the boundary ----
    def test_pin_model_translate(self):
        import pin_model as pm
        self.assertEqual(pm.translate("claude", "opus"), "claude-opus-4-8")
        self.assertEqual(pm.translate("claude", "sonnet"), "claude-sonnet-5")
        self.assertEqual(pm.translate("claude", "claude-opus-4-8"), "claude-opus-4-8")   # pinned pass-through
        self.assertEqual(pm.translate("codex", "gpt-5.6-terra"), "gpt-5.6-terra")
        for bad in [("claude", "haiku"), ("claude", "gpt-4o"), ("codex", "gpt-5"), ("weird", "x")]:
            with self.assertRaises(ValueError):
                pm.translate(*bad)

    def test_every_staged_claude_model_is_pinnable(self):
        import re, pin_model as pm
        models = set()
        for s in ("smoke_v010.py", "v010.py", "baseline_a.py", "baseline_b.py", "setup_confirmatory.py"):
            models |= set(re.findall(r'"claude",\s*"([^"]+)"', (WS / s).read_text()))
        self.assertTrue(models)  # found staged claude models
        for m in models:                      # every effective model post-translation is pinned
            self.assertIn(pm.translate("claude", m), pm.CLAUDE_PINNED)
        self.assertIn("pin_model.py", (WS / "run_calls.sh").read_text())  # boundary actually translates

    # ---- finding 3: spend/driver terminal + resume closure ----
    def test_fault_after_requires_prior_claim(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
        with self.assertRaises(SystemExit):   # no claim -> a "post-read" fault is refused
            spend.append_event(log, "spend:fault-after-authorized-read", HT)
        spend.append_event(log, "structure:read", HT); spend.append_event(log, "state:scoring-attempt", HT)
        spend.claim_authorized_read(log, HT)
        spend.append_event(log, "spend:fault-after-authorized-read", HT)  # post-claim fault OK (spent)

    def test_projector_completed_helper(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
        self.assertFalse(spend.projector_completed(log, HT))
        spend.append_event(log, "structure:read", HT)
        self.assertTrue(spend.projector_completed(log, HT))   # restart would SKIP the projector

    def test_terminal_markers_always_appendable(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
        for ev in ("state:setup-exhaustion", "state:confirmatory-phase-fail",
                   "state:terminated-during-gen-or-attest2-mismatch"):
            spend.append_event(log, ev, HT)   # documentation markers, no gate

    def test_driver_wires_both_classifier_and_terminal_events(self):
        drv = (WS / "run_v010.sh").read_text()
        self.assertIn("classify_failure first", drv)   # first attempt classified
        self.assertIn("classify_failure final", drv)   # AND the relaunch classified (same classifier)
        for ev in ("spend:fault-after-authorized-read", "state:setup-exhaustion",
                   "state:confirmatory-phase-fail", "state:terminated-during-gen-or-attest2-mismatch"):
            self.assertIn(ev, drv)
        self.assertIn("projector_completed", drv)       # resume skip wired

    # ---- finding 4: H/attestation freeze-package completeness ----
    def _build_H(self, out, extra=()):
        return subprocess.run([sys.executable, str(WS / "attest.py"), "build-H",
                               "--recorded-manifest", str(WS / "toy-key/recorded-hashes.txt"),
                               "--out", str(out), *extra], capture_output=True, text=True)

    def test_build_H_refuses_without_prereg(self):
        # PREREG.md is absent in the normal (pre-freeze) workspace -> build-H must refuse
        if (WS / "PREREG.md").exists():
            self.skipTest("PREREG.md present (post-freeze)")
        r = self._build_H(Path(tempfile.mkdtemp()) / "H.json")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("PREREG.md", r.stdout + r.stderr)

    def test_build_H_determinism_with_dummy_freeze_package(self):
        created = []
        for p, txt in ((WS / "PREREG.md", "DUMMY PREREG for test\n"),
                       (WS / "recorded-cli.json", '{"claude": "x", "codex": "y"}\n')):
            if not p.exists():
                p.write_text(txt); created.append(p)
        self.addCleanup(lambda: [p.unlink() for p in created if p.exists()])
        sp = Path(tempfile.mkdtemp())
        r1 = self._build_H(sp / "H1.json"); self.assertEqual(r1.returncode, 0, r1.stdout + r1.stderr)
        r2 = self._build_H(sp / "H2.json"); self.assertEqual(r2.returncode, 0)
        m1 = json.load(open(sp / "H1.json")); m2 = json.load(open(sp / "H2.json"))
        self.assertEqual(m1["H"], m2["H"])   # deterministic
        self.assertIn("prereg_sha256", m1["manifest_of_manifests"])
        self.assertIn("recorded_cli_sha256", m1["manifest_of_manifests"])

    def test_build_H_runtime_refuses_without_corpora(self):
        created = []
        for p, txt in ((WS / "PREREG.md", "DUMMY\n"), (WS / "recorded-cli.json", "{}\n")):
            if not p.exists():
                p.write_text(txt); created.append(p)
        self.addCleanup(lambda: [p.unlink() for p in created if p.exists()])
        r = self._build_H(Path(tempfile.mkdtemp()) / "H.json", extra=("--runtime",))
        self.assertNotEqual(r.returncode, 0)   # --runtime requires corpora/pairs/key (absent)
        self.assertIn("corpora", r.stdout + r.stderr)


class TestRound7(unittest.TestCase):
    """round-7: scoring-relaunch/attempt-cap, restart/terminal routing, output-manifest binding,
    exact inventories, aggregate-only output, conformance drain, corpus attempt hygiene."""

    # ---- finding 1: attempt cap + no-third-attempt-reaches-scorer (shell-level) ----
    def test_third_attempt_refused_before_scorer(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
        spend.append_event(log, "structure:read", HT)
        spend.append_event(log, "state:scoring-attempt", HT)   # attempt 1 (pre-read fail, no claim)
        spend.append_event(log, "state:scoring-attempt", HT)   # attempt 2 (pre-read fail, no claim)
        # mimic the driver's run_attempt marker guard on RESTART: the 3rd marker append is refused
        # with an EXPLICIT `|| exit` BEFORE the "scorer" would run.
        script = (f'set -euo pipefail\n'
                  f'python3 "{WS}/attest.py" spend-log --event state:scoring-attempt --H "{HT}" --out "{log}" '
                  f'|| {{ echo REFUSED-BEFORE-SCORER; exit 7; }}\n'
                  f'echo SCORER-LAUNCHED\n')
        r = subprocess.run(["bash", "-c", script], capture_output=True, text=True)
        self.assertEqual(r.returncode, 7)
        self.assertIn("REFUSED-BEFORE-SCORER", r.stdout)
        self.assertNotIn("SCORER-LAUNCHED", r.stdout)

    def test_scoring_gates_reject_terminal_state(self):
        # round-8: only genuine within-H blockers refuse scoring. The eligible-outcome markers
        # (abort-before-gen / setup-exhaustion) are documentation and do NOT block a same-H resume.
        for term in ("state:terminated-during-gen-or-attest2-mismatch", "spend:fault-after-authorized-read",
                     "state:confirmatory-phase-fail"):
            tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
            spend.append_event(log, "structure:read", HT); spend.append_event(log, "state:scoring-attempt", HT)
            if term == "spend:fault-after-authorized-read":
                spend.claim_authorized_read(log, HT)  # fault needs a prior claim; but claim then blocks anyway
            spend.append_event(log, term, HT)
            with self.assertRaises(SystemExit):
                spend.assert_scoring_allowed(log, HT)

    def test_eligible_outcome_markers_do_not_block_same_H_resume(self):
        # round-8 recovery: abort-before-gen / setup-exhaustion leave the key eligible — a later
        # same-H resume that reaches a clean pre-claim state must NOT be refused by them.
        for term in ("state:abort-before-gen", "state:setup-exhaustion"):
            tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
            spend.append_event(log, term, HT)                       # earlier instance documented
            spend.append_event(log, "structure:read", HT); spend.append_event(log, "state:scoring-attempt", HT)
            spend.assert_scoring_allowed(log, HT)                   # must NOT raise

    def test_old_H_terminal_does_not_block_new_H(self):
        # round-8 per-H namespacing: a terminal under one H must not block scoring under a NEW H.
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"
        oldH = "H-old-revision"
        spend.append_event(log, "state:terminated-during-gen-or-attest2-mismatch", oldH)
        spend.append_event(log, "structure:read", HT); spend.append_event(log, "state:scoring-attempt", HT)
        spend.assert_scoring_allowed(log, HT)                       # new-H run is not blocked by old-H terminal

    def test_custody_ledger_blocks_scoring_cross_run(self):
        # round-8: the durable custody ledger blocks scoring EVERYWHERE once spent/forfeited,
        # even under a fresh H whose per-H spend log is otherwise clean.
        tmp = Path(tempfile.mkdtemp()); log = tmp / "s.jsonl"; ledger = tmp / "custody.jsonl"
        spend.append_event(log, "structure:read", HT); spend.append_event(log, "state:scoring-attempt", HT)
        spend.assert_scoring_allowed(log, HT, custody_ledger=ledger)   # eligible -> OK
        spend.record_custody(ledger, "forfeited-unspent", "H-prev", "attest2-mismatch")
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log, HT, custody_ledger=ledger)
        with self.assertRaises(SystemExit):                            # monotone: cannot un-forfeit
            spend.record_custody(ledger, "eligible", HT, "x")

    # ---- finding 2: per-key idempotence + routing ----
    def test_build_key_skips_completed_key(self):
        import setup_confirmatory as sc
        kid = "test-skip-key"; kd = sc.BASE / f"runs/confirmatory/{kid}"; (kd).mkdir(parents=True, exist_ok=True)
        self.addCleanup(lambda: __import__("shutil").rmtree(kd, ignore_errors=True))
        # round-8: a completed key's skip is TYPED — the receipt embeds accepted-corpora hashes
        # + leakcheck_pass, and the resume re-hashes those corpora before skipping.
        (kd / "corpora/a").mkdir(parents=True, exist_ok=True)
        (kd / "corpora/a/01.md").write_text("hello corpus")
        ch = hashlib.sha256((kd / "corpora/a/01.md").read_bytes()).hexdigest()
        (kd / "setup-key.done").write_text(json.dumps({"key_id": kid, "H": "HX", "complete": True,
            "leakcheck_pass": True, "accepted_corpora_sha256": {"corpora/a/01.md": ch}}))
        args = type("A", (), {"H_value": "HX", "dry_run": False})()
        rec, ok = sc.build_key(kid, args)
        self.assertTrue(ok)
        self.assertFalse((kd / "key/concepts.json").exists())  # NOT regenerated
        # a corrupted accepted corpus HALTS the skip (does not silently reuse)
        (kd / "corpora/a/01.md").write_text("TAMPERED")
        with self.assertRaises(SystemExit):
            sc.build_key(kid, args)
        (kd / "corpora/a/01.md").write_text("hello corpus")     # restore for the different-H check
        args2 = type("A", (), {"H_value": "DIFFERENT", "dry_run": False})()
        with self.assertRaises(SystemExit):                    # different H -> refuse overwrite
            sc.build_key(kid, args2)

    def test_driver_routes_and_resumes(self):
        drv = (WS / "run_v010.sh").read_text()
        # round-8/9: PRE-confirmatory failures (projector/probe) are RESUMABLE — no forfeit.
        self.assertRegex(drv, r"PROJECTOR failed.*resumable")
        self.assertRegex(drv, r"PROBE failed.*resumable")
        # round-9 finding 3: a POST-confirmatory attestation-1 mismatch HALTS + demands classification
        # (re-freeze + two NEW draws, or retirement) — it is NOT silently resumable.
        self.assertRegex(drv, r"ATTESTATION-1 MISMATCH")
        self.assertIn("re-freeze + two NEW draws", drv)
        # NO EXIT-trap auto-forfeit; infra faults during generation are resumable, not terminal.
        self.assertNotIn("trap on_exit EXIT", drv)
        self.assertNotIn("GEN_STARTED", drv)
        # round-9 finding 1: H is IMMUTABLE on restart (verify, never rebuild) + a cross-H
        # generation-started guard HALTs an in-place different-H run.
        self.assertIn("verify-files --H runs/H.json", drv)
        self.assertIn("generation-started", drv)
        self.assertRegex(drv, r"DIFFERENT H")
        # round-9 finding 2: persistence failures are HARD HALTS (no 2>/dev/null || true suppression).
        self.assertNotIn("2>/dev/null || true", drv)
        # round-9 finding 7: the projector receipt is verified before registering structure:read.
        self.assertIn("--verify-receipt runs/pairs-receipt.json", drv)
        # forfeiture is EXPLICIT + only at the two genuine terminals, mirrored into the custody ledger.
        self.assertIn("forfeit_custody attest2-mismatch", drv)
        self.assertIn("state:terminated-during-gen-or-attest2-mismatch", drv)
        self.assertIn("spend:fault-after-authorized-read", drv)
        # every spend-log / custody call carries the per-H namespace.
        self.assertIn('--H "$H"', drv)
        # resume: TYPED phase receipts (phase_check) + per-conf-key skip.
        for p in ("phase_check probe", "phase_check attest1", "phase_check generation",
                  'phase_check "draw-$ck"'):
            self.assertIn(p, drv)

    # ---- finding 3: output-manifest binds the scorer's inputs ----
    def _make_scored_workspace(self):
        base = Path(tempfile.mkdtemp())
        for d in ("runs/v010", "runs/baseline_a", "runs/baseline_b"):
            (base / d).mkdir(parents=True)
        ak = json.load(open(WS / "toy-key/key/answer_key.json"))["pairs"]
        (WS / "toy-key/pairs.json")  # ensure exists
        pairs = json.load(open(WS / "toy-key/pairs.json"))["pairs"]
        by_tp = {(p["term_a"], p["term_b"]): p for p in ak}
        tau1 = {pp["pair_id"]: {"proposed_relation": by_tp[(pp["term_a"], pp["term_b"])]["expected"],
                                "status": "asserted",
                                "broader_side": by_tp[(pp["term_a"], pp["term_b"])].get("broader_side")}
                for pp in pairs}
        (base / "runs/v010/verdicts.json").write_text(json.dumps({"primary": "tau1", "tau1": tau1}))
        (base / "runs/baseline_a/records.json").write_text(json.dumps(
            {f"a:{pp['term_a']}": {"final": "negative"} for pp in pairs} |
            {f"b:{pp['term_b']}": {"final": "negative"} for pp in pairs}))
        (base / "runs/baseline_b/records.json").write_text(json.dumps(
            {pp["pair_id"]: {"final": "no-assertion"} for pp in pairs}))
        # round-9 finding 4: the deterministic derived records are REQUIRED unconditionally.
        for rel in ("runs/v010/review-context.json", "runs/v010/agg.json",
                    "runs/v010/route-union.json", "runs/v010/retrieval.json"):
            (base / rel).write_text("{}")
        return base

    def _attest2(self, base, om, bound_om=None):
        # round-9 finding 4: a minimal attestation-2 receipt binding output_manifest_sha256.
        H = json.load(open(base / "H.json"))["H"]
        a2 = base / (Path(om).name + ".attest2.json")
        b = Path(bound_om or om)
        a2.write_text(json.dumps({"H": H, "point": 2,
                                  "output_manifest_sha256": hashlib.sha256(b.read_bytes()).hexdigest()}))
        return a2

    def _scorer(self, base, om, spendlog, extra=(), bound_om=None):
        # round-8/9: `score` subcommand + a per-invocation custody ledger (fresh => eligible) +
        # the attestation-2 receipt binding the output-manifest hash.
        a2 = self._attest2(base, om, bound_om)
        return subprocess.run([sys.executable, str(WS / "scorer_v010.py"), "score",
                               "--key-dir", str(WS / "toy-key/key"),
                               "--recorded-hashes", str(WS / "toy-key/recorded-hashes.txt"),
                               "--pairs", str(WS / "toy-key/pairs.json"),
                               "--H", str(base / "H.json"), "--spend-log", str(spendlog),
                               "--custody-ledger", str(spendlog) + ".custody",
                               "--output-manifest", str(om), "--attest2-receipt", str(a2),
                               "--run-root", str(base),
                               "--tool-verdicts", str(base / "runs/v010/verdicts.json"),
                               "--baseline-a", str(base / "runs/baseline_a/records.json"),
                               "--baseline-b", str(base / "runs/baseline_b/records.json"),
                               "--out", str(base / "scores.json"), *extra], capture_output=True, text=True)

    def _H_json(self, base):
        # a minimal self-consistent H.json bound to the toy recorded-hashes
        man = {"recorded_manifest_sha256": hashlib.sha256((WS / "toy-key/recorded-hashes.txt").read_bytes()).hexdigest()}
        import attest as at
        h = hashlib.sha256(at._canonical(man)).hexdigest()
        (base / "H.json").write_text(json.dumps({"H": h, "manifest_of_manifests": man}))
        return h

    def test_scorer_verifies_inputs_against_output_manifest_before_claim(self):
        import attest as at
        base = self._make_scored_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        # normal run succeeds + writes aggregate-only scores.json
        r = self._scorer(base, base / "om.json", sp)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # TAMPER a baseline input after the manifest -> scorer refuses PRE-CLAIM (no claim appended)
        (base / "runs/baseline_a/records.json").write_text('{"tampered": true}')
        sp2 = base / "spend2.jsonl"
        spend.append_event(sp2, "structure:read", H); spend.append_event(sp2, "state:scoring-attempt", H)
        r2 = self._scorer(base, base / "om.json", sp2)
        self.assertNotEqual(r2.returncode, 0)
        self.assertNotIn("authorized-read-claimed", (sp2).read_text())  # never claimed the key

    def test_scorer_refuses_missing_verdicts_before_claim(self):
        import attest as at
        base = self._make_scored_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)
        (base / "runs/v010/verdicts.json").unlink()
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        r = self._scorer(base, base / "om.json", sp)
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("authorized-read-claimed", sp.read_text())

    def test_scorer_refuses_manifest_swapped_after_attest2(self):
        # round-9 finding 4: a manifest swapped between attestation-2 and the claim is caught by the
        # output_manifest_sha256 bound in the attestation-2 receipt.
        import attest as at
        base = self._make_scored_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)
        (base / "om2.json").write_text((base / "om.json").read_text() + "\n")   # different bytes, same set
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        # attest-2 receipt binds om.json, but the scorer is handed the swapped om2.json
        r = self._scorer(base, base / "om2.json", sp, bound_om=base / "om.json")
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("authorized-read-claimed", sp.read_text())

    # ---- finding 4: exact inventories ----
    def test_impl_inventory_diff_detects_extra_and_missing(self):
        import attest as at
        req = at.required_inventory(WS / "REQUIRED-INVENTORY.txt")
        extra, miss = at.impl_inventory_diff(req, WS)
        self.assertEqual((extra, miss), ([], []))                 # workspace matches canonical
        extra2, miss2 = at.impl_inventory_diff(req - {"pin_model.py"}, WS)
        self.assertIn("pin_model.py", extra2)                     # a file present but not required = extra
        extra3, miss3 = at.impl_inventory_diff(req | {"ghost.py"}, WS)
        self.assertIn("ghost.py", miss3)                          # a required file absent = missing

    def test_corpora_exact_rejects_extra_and_missing(self):
        import attest as at
        base = Path(tempfile.mkdtemp())
        for s in ("a", "b"):
            (base / f"corpora/{s}").mkdir(parents=True)
            for i in range(1, 12):
                (base / f"corpora/{s}/{i:02d}.md").write_text("x")
        (base / "key").mkdir()
        (base / "key/concepts.json").write_text("{}"); (base / "key/answer_key.json").write_text("{}")
        self.assertEqual(at.corpora_exact_errs(base), {"extra": [], "missing": [], "key_extra": []})
        (base / "corpora/a/12.md").write_text("x")               # extra numbered doc
        self.assertIn("corpora/a/12.md", at.corpora_exact_errs(base)["extra"])
        (base / "corpora/a/notes.md").write_text("x")            # round-9: NONNUMERIC extra .md caught
        self.assertIn("corpora/a/notes.md", at.corpora_exact_errs(base)["extra"])
        (base / "corpora/b/05.md").unlink()                       # missing
        self.assertIn("corpora/b/05.md", at.corpora_exact_errs(base)["missing"])
        (base / "key/rogue.txt").write_text("x")                  # round-9: unexpected key-dir file caught
        self.assertIn("key/rogue.txt", at.corpora_exact_errs(base)["key_extra"])

    # ---- finding 5: aggregate-only scoring output ----
    def test_scores_json_is_aggregate_only(self):
        import attest as at
        base = self._make_scored_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        r = self._scorer(base, base / "om.json", sp); self.assertEqual(r.returncode, 0, r.stderr)
        blob = (base / "scores.json").read_text()
        for banned in ("per_pair", "expected", '"promotions"', '"false_escalations"'):
            self.assertNotIn(banned, blob)
        d = json.load(open(base / "scores.json"))["tool_arm"]
        self.assertIn("promotions_count", d); self.assertIn("fp", d["detection"])
        # round-8 finding 5: the per-pair diagnostics are EMBARGOED (written during the single read,
        # hash-bound into scores.json), NOT released. scores.json stays aggregate-only.
        sj = json.load(open(base / "scores.json"))
        self.assertIn("embargo_sha256", sj)
        emb = WS / "runs/scoring/.embargo/per-pair.json"
        self.addCleanup(lambda: __import__("shutil").rmtree(WS / "runs/scoring", ignore_errors=True))
        self.assertTrue(emb.exists())                                  # embargoed (not released)
        self.assertEqual(hashlib.sha256(emb.read_bytes()).hexdigest(), sj["embargo_sha256"])

    def test_per_pair_export_only_after_real_addendum_commit(self):
        import attest as at, subprocess as sub
        base = self._make_scored_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        r = self._scorer(base, base / "om.json", sp); self.assertEqual(r.returncode, 0, r.stderr)
        emb = WS / "runs/scoring/.embargo/per-pair.json"
        self.addCleanup(lambda: __import__("shutil").rmtree(WS / "runs/scoring", ignore_errors=True))
        self.assertTrue(emb.exists())
        def export(commit, repo, out):
            return sub.run([sys.executable, str(WS / "scorer_v010.py"), "export-embargo",
                            "--embargo", str(emb), "--repo", str(repo), "--commit", commit,
                            "--out", str(out)], capture_output=True, text=True)
        # (a) a fabricated / non-existent commit is REFUSED (no release without a real addendum).
        r1 = export("deadbeefcafe", WS, base / "rel.json")
        self.assertNotEqual(r1.returncode, 0)
        self.assertFalse((base / "rel.json").exists())
        # (b) a REAL addendum commit carrying the E5.1 marker releases the embargoed per-pair file.
        repo = Path(tempfile.mkdtemp())
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
               "GIT_COMMITTER_EMAIL": "t@t"}
        sub.run(["git", "-C", str(repo), "init", "-q"], check=True, env=env)
        (repo / "EXPERIMENT-LOG.md").write_text("# log\nE5.1 post-commit per-pair addendum\n")
        sub.run(["git", "-C", str(repo), "add", "EXPERIMENT-LOG.md"], check=True, env=env)
        sub.run(["git", "-C", str(repo), "commit", "-qm", "addendum"], check=True, env=env)
        sha = sub.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        r2 = export(sha, repo, base / "rel.json")
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertTrue((base / "rel.json").exists())
        self.assertIn("per_pair", (base / "rel.json").read_text())

    # ---- finding 6: conformance drain e2e (through the actual gate loop, scripted outputs) ----
    def test_conformance_drain_no_stranding_e2e(self):
        tmp = Path(tempfile.mkdtemp()); orig = smoke.RUNS; smoke.RUNS = tmp
        orig_leak = smoke.leak_ok; smoke.leak_ok = lambda f: (True, "")  # leak gate not under test here
        try:
            for d in ("definitions", "checklists", "conformance", "manifests"):
                (tmp / d).mkdir(parents=True, exist_ok=True)
            term = "widget alpha"; A = aid_(term)
            L0 = "One sentence genus here."                        # 1 sentence, 4 words
            L1 = "One sentence genus here. Then the mechanism does concrete work."  # 2 sentences
            L2_ok = L1 + " Measured as " + " ".join(["w"] * 60)    # 60-160 words, > L1
            L2_short = L1 + " Too short."                          # < 60 words -> L2-count mech fail
            smoke.canon_path("chk", "a", term, "txt").write_text("- mech commitment\n- another")
            smoke.canon_path("lad", "a", term, "json").write_text(json.dumps({"L0": L0, "L1": L1, "L2": L2_ok}))
            smoke.base_prompt_path("lad", "a", term).write_text("BASE\nEXCERPTS:\n1. foo")
            smoke.gate_save({"artifacts": {A: {"kind": "lad", "side": "a", "term": term, "total_regens": 0,
                             "semantic_regens": 0, "state": "awaiting_semantic", "log": [],
                             "cli": "claude", "model": "opus"}},
                             "conf_batches": {}, "polarity": {}, "polarity_side_fail": []})

            def exec_ladder(g, ok):   # write the scripted g-th ladder output + a clean manifest
                out = smoke.gen_path("lad", "a", term, g, "json")
                out.write_text(json.dumps({"L0": L0, "L1": L1, "L2": L2_ok if ok else L2_short}))
                smoke.manifest_for("lad", "a", term, g).write_text(
                    f"exit: 0\nout_sha256: {hashlib.sha256(out.read_bytes()).hexdigest()}\n")
            def exec_open_conf(verdict):   # execute the single OPEN conformance batch
                open_bids = [b for b, v in smoke.gate_load()["conf_batches"].items() if not v["resolved"]]
                bid = open_bids[0]
                n = len(json.load(open(tmp / f"conformance/batch-{bid}.json"))["terms"])
                out = tmp / f"conformance/out-{bid}-r0.json"
                out.write_text(json.dumps([{"item": i + 1, "verdict": verdict,
                    "reason": "" if verdict == "conformant" else "dropped mechanism"} for i in range(n)]))
                (tmp / f"manifests/conf-{bid}-r0.json").write_text(
                    f"exit: 0\nout_sha256: {hashlib.sha256(out.read_bytes()).hexdigest()}\n")
                _run_smoke("gate-conformance", tmp)

            # DRIVER-LOOP mimic (the run_v010 phase-6 drain loop): drain ladder regens to
            # quiescence, stage ONE conformance batch, gate it; repeat. Scripted path:
            # g0 conform -> nonconformant (semantic fail -> g1) ; g1 ladder MECH-fails -> g2 ;
            # g2 ladder ok -> conformance -> conformant.
            verdicts = iter(["nonconformant", "conformant"])
            for _ in range(6):   # bounded
                regen = tmp / "definitions/regen-calls.tsv"
                while regen.exists() and regen.read_text().strip():
                    g = smoke.gate_load()["artifacts"][A]["total_regens"]
                    exec_ladder(g, ok=(g != 1))       # g1 mechanically FAILS; g2 ok
                    _run_smoke("gate-ladders", tmp)
                _run_smoke("prompts-conformance", tmp)
                if not (tmp / "conformance/calls.tsv").read_text().strip():
                    break
                exec_open_conf(next(verdicts))
            smoke.assert_resolved([])   # must NOT halt — the late g2 entrant was NOT stranded
            self.assertEqual(smoke.gate_load()["artifacts"][A]["state"], "passed")
        finally:
            smoke.RUNS = orig; smoke.leak_ok = orig_leak

    # ---- finding 7: corpus attempt hygiene ----
    def _synth_key(self):
        import setup_confirmatory as sc
        kd = Path(tempfile.mkdtemp()) / "conf"; (kd / "key").mkdir(parents=True)
        (kd / "key/concepts.json").write_text((WS / "toy-key/key/concepts.json").read_text())
        subprocess.run([sys.executable, str(WS / "harness/validate_key.py"), str(kd / "key/concepts.json")], check=True, capture_output=True)
        subprocess.run([sys.executable, str(WS / "harness/gen_leakcheck.py"), str(kd)], check=True, capture_output=True)
        return kd

    def _gen(self, terms, start=1, count=11):
        return "\n".join(f"<<<DOC {i}>>>\n# R{i}\nThe {terms[(i-1) % len(terms)]} run logged results."
                         for i in range(start, start + count)) + "\n"

    def test_corpus_misnumbered_rejected(self):
        import setup_confirmatory as sc
        kd = self._synth_key(); a = [p["term_a"] for p in json.load(open(kd / "key/answer_key.json"))["pairs"]]
        (kd / "runs").mkdir(exist_ok=True)
        (kd / "runs/gen-a.out").write_text(self._gen(a, start=0, count=11))   # DOC 0..10 -> 00..10.md
        self.assertFalse(sc._corpus_attempt_ok(kd, "a", kd / "runs/gen-a.out"))
        self.assertFalse((kd / "corpora/a").exists())   # nothing promoted

    def test_corpus_retry_after_extra_file_is_clean(self):
        import setup_confirmatory as sc
        kd = self._synth_key(); a = [p["term_a"] for p in json.load(open(kd / "key/answer_key.json"))["pairs"]]
        (kd / "runs").mkdir(exist_ok=True)
        (kd / "runs/gen-a-bad.out").write_text(self._gen(a, start=1, count=12))   # 01..12 (extra 12)
        self.assertFalse(sc._corpus_attempt_ok(kd, "a", kd / "runs/gen-a-bad.out"))  # rejected (temp discarded)
        (kd / "runs/gen-a.out").write_text(self._gen(a, start=1, count=11))       # valid retry
        self.assertTrue(sc._corpus_attempt_ok(kd, "a", kd / "runs/gen-a.out"))
        names = sorted(p.name for p in (kd / "corpora/a").glob("*.md"))
        self.assertEqual(names, [f"{i:02d}.md" for i in range(1, 12)])            # exactly 01..11, no stale 12


class TestRound8(unittest.TestCase):
    """round-8: per-H recovery/custody, typed phase receipts, exact output-manifest set-equality,
    confirmatory typed-receipt attestation, and finding-6 pre-claim input binding."""

    # ---- finding 3: typed phase receipts (attest.py phase-receipt / phase-verify) ----
    def _H_json(self, base):
        man = {"recorded_manifest_sha256": hashlib.sha256((WS / "toy-key/recorded-hashes.txt").read_bytes()).hexdigest()}
        import attest as at
        h = hashlib.sha256(at._canonical(man)).hexdigest()
        (base / "H.json").write_text(json.dumps({"H": h, "manifest_of_manifests": man}))
        return h

    def _pv(self, phase, H, receipt, extra=()):
        return subprocess.run([sys.executable, str(WS / "attest.py"), "phase-verify",
                               "--phase", phase, "--H", str(H), "--receipt", str(receipt), *extra],
                              capture_output=True, text=True)

    def test_phase_receipt_roundtrip_and_stale_and_missing(self):
        base = Path(tempfile.mkdtemp()); self._H_json(base)
        Hj = base / "H.json"
        out = base / "artifact.json"; out.write_text('{"ok": true}')
        rec = base / "phase.done"
        r = subprocess.run([sys.executable, str(WS / "attest.py"), "phase-receipt", "--phase", "gen",
                            "--H", str(Hj), "--require", str(out), "--assert", "gate_pass=true",
                            "--out", str(rec)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # complete: outputs re-hash + semantics hold -> exit 0 (skip)
        self.assertEqual(self._pv("gen", Hj, rec, ("--assert", "gate_pass=true")).returncode, 0)
        # missing receipt -> exit 2 (run the phase)
        self.assertEqual(self._pv("gen", Hj, base / "nope.done").returncode, 2)
        # a wrong semantic assertion -> HALT (exit 1)
        self.assertEqual(self._pv("gen", Hj, rec, ("--assert", "gate_pass=false")).returncode, 1)
        # DAMAGED required output -> HALT (exit 1)
        out.write_text('{"ok": false, "tampered": 1}')
        self.assertEqual(self._pv("gen", Hj, rec).returncode, 1)

    def test_phase_receipt_refuses_when_required_output_absent(self):
        base = Path(tempfile.mkdtemp()); self._H_json(base)
        r = subprocess.run([sys.executable, str(WS / "attest.py"), "phase-receipt", "--phase", "gen",
                            "--H", str(base / "H.json"), "--require", str(base / "ghost.json"),
                            "--out", str(base / "phase.done")], capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse((base / "phase.done").exists())

    # ---- finding 4: exact step-7 output manifest — set equality (missing AND extra) ----
    def _staged_workspace(self):
        """A synthetic runs/ dir with ONE completed staged call (out + manifest) + the derived
        scorer inputs, so step7_expected has both a staged output and derived records."""
        base = Path(tempfile.mkdtemp())
        (base / "runs/v010/verify").mkdir(parents=True)
        (base / "runs/v010/manifests").mkdir(parents=True)
        (base / "runs/baseline_a").mkdir(parents=True); (base / "runs/baseline_b").mkdir(parents=True)
        out = base / "runs/v010/verify/out-0.json"; out.write_text('{"v": 1}')
        man = base / "runs/v010/manifests/verify-0.json"
        man.write_text(f"exit: 0\nout_sha256: {hashlib.sha256(out.read_bytes()).hexdigest()}\n")
        (base / "runs/v010/verify/calls.tsv").write_text(
            f"vfy\topus\tp.md\t{out}\t{man}\n")
        (base / "runs/v010/verdicts.json").write_text("{}")
        (base / "runs/baseline_a/records.json").write_text("{}")
        (base / "runs/baseline_b/records.json").write_text("{}")
        for rel in ("runs/v010/review-context.json", "runs/v010/agg.json",
                    "runs/v010/route-union.json", "runs/v010/retrieval.json"):
            (base / rel).write_text("{}")   # round-9: derived records required unconditionally
        return base

    def test_completed_output_drift_refused(self):
        import attest as at
        base = self._staged_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)              # clean build OK
        # MODIFY a completed staged output (manifest out_sha256 now stale) -> build + attest-2 refuse
        (base / "runs/v010/verify/out-0.json").write_text('{"v": 999}')
        with self.assertRaises(SystemExit):
            at.build_output_manifest_at(H, base / "om2.json", base)
        self.assertTrue(any("drift" in e for e in at._verify_output_manifest_errs(base / "om.json", H, base)))

    def test_output_manifest_exact_set_equality(self):
        import attest as at
        base = self._staged_workspace(); H = self._H_json(base)
        files = at.build_output_manifest_at(H, base / "om.json", base)
        self.assertIn("runs/v010/verify/out-0.json", files)          # the completed staged output
        self.assertIn("runs/v010/manifests/verify-0.json", files)    # its isolation manifest
        self.assertIn("runs/v010/verdicts.json", files)              # a derived scorer input
        # (a) a MISSING expected output is rejected at verify (set-equality both directions)
        errs = at._verify_output_manifest_errs(base / "om.json", H, base)
        self.assertEqual(errs, [])
        (base / "runs/v010/verify/out-0.json").unlink()
        errs2 = at._verify_output_manifest_errs(base / "om.json", H, base)
        self.assertTrue(any("out-0.json" in e for e in errs2), errs2)

    def test_output_manifest_rejects_missing_completed_output_at_build(self):
        import attest as at
        base = self._staged_workspace(); H = self._H_json(base)
        # delete a COMPLETED staged output before building -> build must REFUSE (not silently omit)
        (base / "runs/v010/verify/out-0.json").unlink()
        with self.assertRaises(SystemExit):
            at.build_output_manifest_at(H, base / "om.json", base)

    def test_output_manifest_rejects_extra_unlisted_output(self):
        import attest as at
        base = self._staged_workspace(); H = self._H_json(base)
        at.build_output_manifest_at(H, base / "om.json", base)      # baseline manifest
        # now add an UNLISTED output matching OUTPUT_GLOBS -> a fresh build must REFUSE (extra)
        (base / "runs/v010/verify/out-9.json").write_text('{"rogue": 1}')
        with self.assertRaises(SystemExit):
            at.build_output_manifest_at(H, base / "om2.json", base)

    # ---- finding 3: confirmatory typed-receipt verification (attest-1) ----
    def test_confirmatory_receipt_verification(self):
        import attest as at
        base = Path(tempfile.mkdtemp())
        cd = base / "conf-key-1"; (cd / "runs").mkdir(parents=True); (cd / "corpora/a").mkdir(parents=True)
        (cd / "corpora/a/01.md").write_text("corpus one")
        ch = hashlib.sha256((cd / "corpora/a/01.md").read_bytes()).hexdigest()
        H = "H-conf-test"
        (cd / "runs/confirmatory-result.json").write_text(json.dumps(
            {"H": H, "gate_pass": True, "numerator": 0, "corpora_sha256": {"corpora/a/01.md": ch}}))
        self.assertEqual(at._verify_confirmatory_receipt(cd, H), [])              # valid
        self.assertTrue(at._verify_confirmatory_receipt(cd, "OTHER-H"))          # H mismatch
        (cd / "runs/confirmatory-result.json").write_text(json.dumps(
            {"H": H, "gate_pass": False, "corpora_sha256": {"corpora/a/01.md": ch}}))
        self.assertTrue(at._verify_confirmatory_receipt(cd, H))                  # gate_pass false
        (cd / "corpora/a/01.md").write_text("TAMPERED")
        self.assertTrue(at._verify_confirmatory_receipt(cd, H))                  # corpus drift
        __import__("shutil").rmtree(cd / "runs")
        self.assertTrue(at._verify_confirmatory_receipt(cd, H))                  # receipt missing

    # ---- finding 6: deterministic pre-claim input binding (attest-side) ----
    def _binding_base(self):
        base = Path(tempfile.mkdtemp()); (base / "key").mkdir()
        (base / "key/concepts.json").write_text("{}"); (base / "key/answer_key.json").write_text("{}")
        cli = base / "recorded-cli.json"; cli.write_text('{"claude": "1", "codex": "2"}')
        probe = base / "probe.json"; probe.write_text('{"resolved": {}}')
        man = {"recorded_cli_sha256": hashlib.sha256(cli.read_bytes()).hexdigest()}
        return base, man, cli, probe

    def test_input_binding_key_existence_and_schema_and_hash(self):
        import attest as at
        base, man, cli, probe = self._binding_base()
        self.assertEqual(at.input_binding_errs(man, cli, probe, 1, base), [])     # all good
        # (a) missing sealed key file
        (base / "key/answer_key.json").unlink()
        self.assertTrue(any("answer_key.json" in e for e in at.input_binding_errs(man, cli, probe, 1, base)))
        (base / "key/answer_key.json").write_text("{}")
        # (b) wrong CLI schema (extra key)
        cli.write_text('{"claude": "1", "codex": "2", "gemini": "3"}')
        errs = at.input_binding_errs(man, cli, probe, 1, base)
        self.assertTrue(any("schema" in e for e in errs))
        # (c) --recorded-cli hash != bound in H (schema restored, but H binds old hash)
        cli.write_text('{"claude": "9", "codex": "9"}')
        self.assertTrue(any("hash != value bound in H" in e for e in at.input_binding_errs(man, cli, probe, 1, base)))

    def test_input_binding_probe_log_identity_point2(self):
        import attest as at
        base, man, cli, probe = self._binding_base()
        # point 2 requires the SAME probe-log bytes recorded at attestation-1
        self.assertTrue(any("probe-log" in e for e in at.input_binding_errs(man, cli, probe, 2, base)))
        (base / "runs").mkdir()
        (base / "runs/attestation-point-1.json").write_text(json.dumps(
            {"probe_log_sha256": hashlib.sha256(probe.read_bytes()).hexdigest()}))
        self.assertEqual(at.input_binding_errs(man, cli, probe, 2, base), [])      # identical -> OK
        probe.write_text('{"resolved": {"opus": ["x"]}}')                          # different bytes
        self.assertTrue(any("probe-log" in e for e in at.input_binding_errs(man, cli, probe, 2, base)))

    # ---- finding 6 (scorer-side): pre-claim key-file existence ----
    def test_scorer_refuses_absent_key_before_claim(self):
        base = Path(tempfile.mkdtemp())
        for d in ("runs/v010", "runs/baseline_a", "runs/baseline_b"):
            (base / d).mkdir(parents=True)
        man = {"recorded_manifest_sha256": hashlib.sha256((WS / "toy-key/recorded-hashes.txt").read_bytes()).hexdigest()}
        import attest as at
        H = hashlib.sha256(at._canonical(man)).hexdigest()
        (base / "H.json").write_text(json.dumps({"H": H, "manifest_of_manifests": man}))
        (base / "runs/v010/verdicts.json").write_text(json.dumps({"primary": "tau1", "tau1": {}}))
        (base / "runs/baseline_a/records.json").write_text("{}")
        (base / "runs/baseline_b/records.json").write_text("{}")
        for rel in ("runs/v010/review-context.json", "runs/v010/agg.json",
                    "runs/v010/route-union.json", "runs/v010/retrieval.json"):
            (base / rel).write_text("{}")
        at.build_output_manifest_at(H, base / "om.json", base)
        a2 = base / "attest2.json"
        a2.write_text(json.dumps({"H": H, "point": 2,
            "output_manifest_sha256": hashlib.sha256((base / "om.json").read_bytes()).hexdigest()}))
        sp = base / "spend.jsonl"
        spend.append_event(sp, "structure:read", H); spend.append_event(sp, "state:scoring-attempt", H)
        empty_key = base / "emptykey"; empty_key.mkdir()   # no concepts.json / answer_key.json
        r = subprocess.run([sys.executable, str(WS / "scorer_v010.py"), "score",
                            "--key-dir", str(empty_key),
                            "--recorded-hashes", str(WS / "toy-key/recorded-hashes.txt"),
                            "--pairs", str(WS / "toy-key/pairs.json"), "--H", str(base / "H.json"),
                            "--spend-log", str(sp), "--custody-ledger", str(base / "c.jsonl"),
                            "--output-manifest", str(base / "om.json"), "--attest2-receipt", str(a2),
                            "--tool-verdicts", str(base / "runs/v010/verdicts.json"),
                            "--out", str(base / "scores.json")], capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("authorized-read-claimed", sp.read_text())   # refused BEFORE the claim


class TestRound9(unittest.TestCase):
    """round-9: atomic custody claim (crash-window + concurrent-different-H), idempotent custody,
    recovery-aware availability, generation-started marker, setup attempt reuse, projector receipt."""
    H9 = "H-round9-fixed"

    def _ready(self, tmp):
        log = tmp / "sp.jsonl"; led = tmp / "cust.jsonl"
        spend.append_event(log, "structure:read", self.H9)
        spend.append_event(log, "state:scoring-attempt", self.H9)
        return log, led

    # ---- finding 2: ONE fail-closed atomic claim ----
    def test_atomic_claim_writes_both_then_refuses_second(self):
        tmp = Path(tempfile.mkdtemp()); log, led = self._ready(tmp)
        spend.atomic_claim(log, led, self.H9)
        self.assertEqual(spend.custody_state(led), "spent")            # ledger spent
        self.assertIn("authorized-read-claimed", log.read_text())      # per-H claim
        with self.assertRaises(SystemExit):                            # crash-after-claim: no second read
            spend.atomic_claim(log, led, self.H9)

    def test_atomic_claim_recovery_after_ledger_before_claim(self):
        # crash AFTER the ledger write, BEFORE the claim: ledger spent (this H), no claim yet.
        tmp = Path(tempfile.mkdtemp()); log, led = self._ready(tmp)
        spend.record_custody(led, "spent", self.H9, "crash-window")
        spend.atomic_claim(log, led, self.H9)                          # idempotent recovery: appends the missing claim
        self.assertEqual(log.read_text().count("authorized-read-claimed"), 1)
        self.assertEqual(len(spend.read_events(led)), 1)               # ledger NOT double-appended
        with self.assertRaises(SystemExit):
            spend.atomic_claim(log, led, self.H9)                      # a re-run (key now read) is refused

    def test_atomic_claim_concurrent_different_H_refused(self):
        tmp = Path(tempfile.mkdtemp()); log, led = self._ready(tmp)
        spend.record_custody(led, "spent", "H-other-run", "another instance already read")
        with self.assertRaises(SystemExit):
            spend.atomic_claim(log, led, self.H9)
        self.assertNotIn("authorized-read-claimed", log.read_text())   # never claimed

    def test_record_custody_idempotent_and_monotone(self):
        tmp = Path(tempfile.mkdtemp()); led = tmp / "c.jsonl"
        spend.record_custody(led, "spent", self.H9, "a")
        self.assertIsNone(spend.record_custody(led, "spent", self.H9, "b"))   # same-H dup = no-op
        self.assertEqual(len(spend.read_events(led)), 1)
        with self.assertRaises(SystemExit):
            spend.record_custody(led, "forfeited-unspent", self.H9, "c")      # conflicting state refused
        with self.assertRaises(SystemExit):
            spend.record_custody(led, "spent", "H-other", "d")               # different-H dup refused

    def test_assert_key_available_recovery_aware(self):
        tmp = Path(tempfile.mkdtemp()); led = tmp / "c.jsonl"
        spend.record_custody(led, "spent", self.H9, "x")
        spend.assert_key_available(led, self.H9)                              # same H -> recovery OK
        with self.assertRaises(SystemExit):
            spend.assert_key_available(led, "H-other")                       # different H -> refused
        with self.assertRaises(SystemExit):
            spend.assert_key_available(led)                                  # no run_H -> strict refuse

    def test_generation_started_event_appendable(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "sp.jsonl"
        spend.append_event(log, "state:generation-started", self.H9)
        self.assertEqual([e["event"] for e in spend.read_events(log)], ["state:generation-started"])

    # ---- finding 5: setup attempt durability — a completed attempt is REUSED, never re-issued ----
    def test_setup_completed_attempt_reused_on_restart(self):
        import setup_confirmatory as sc
        tmp = Path(tempfile.mkdtemp()); (tmp / "manifests").mkdir()
        out = tmp / "call.out"; manifest = tmp / "manifests/site.json"
        snap_out, snap_man, att_rcpt = sc._attempt_paths(manifest, 0)
        snap_out.write_text("completed output")
        snap_man.write_text("exit: 0\n")
        att_rcpt.write_text(json.dumps({"site": "s", "attempt": 0, "path": str(out),
                                        "sha256": sc._sha(snap_out), "rc": 0}))
        calls = {"n": 0}
        orig = sc._isolated
        sc._isolated = lambda *a, **k: calls.__setitem__("n", calls["n"] + 1) or 0
        try:
            receipt = {"outputs": []}
            ok = sc._call_with_retry("s", "claude", "m", tmp / "p.md", out, manifest,
                                     lambda: True, receipt, dry=False)
        finally:
            sc._isolated = orig
        self.assertTrue(ok)
        self.assertEqual(calls["n"], 0)                       # the model call was NOT re-issued
        self.assertEqual(out.read_text(), "completed output") # canonical output restored from snapshot

    # ---- finding 7: projector receipt bound to pairs.json; tamper refused ----
    def test_projector_receipt_tamper_refused(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"; rc = tmp / "receipt.json"
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            str(WS / "toy-key/key"), str(out), "--emit-receipt", str(rc)],
                           check=True, capture_output=True, text=True)
        v = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            "--verify-receipt", str(rc), "--pairs", str(out)], capture_output=True, text=True)
        self.assertEqual(v.returncode, 0, v.stdout + v.stderr)           # matches
        out.write_text(out.read_text() + "\n ")                          # TAMPER pairs.json
        v2 = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                             "--verify-receipt", str(rc), "--pairs", str(out)], capture_output=True, text=True)
        self.assertNotEqual(v2.returncode, 0)
        self.assertIn("REFUSE", v2.stdout + v2.stderr)


def aid_(term):
    return f"lad:a:{term}"

def _run_smoke(cmd, runs):
    import smoke_v010 as s
    old = s.RUNS; s.RUNS = runs
    try:
        {"gate-ladders": s.gate_ladders, "prompts-conformance": s.prompts_conformance,
         "gate-conformance": s.gate_conformance}[cmd]([])
    finally:
        s.RUNS = old


if __name__ == "__main__":
    unittest.main(verbosity=2)
