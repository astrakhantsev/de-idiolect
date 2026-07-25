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
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")
        return log

    def test_claim_one_shot(self):
        tmp = Path(tempfile.mkdtemp()); log = self._ready_log(tmp)
        spend.claim_authorized_read(log)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log)  # a second claim is refused (already spent)

    def test_scoring_attempt_capped_at_two(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")
        spend.append_event(log, "state:scoring-attempt")  # 2nd OK
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt")  # 3rd refused

    def test_spend_accidental_blocks_everything(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "spend:accidental-access-during-gen")
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt")
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)

    def test_scorer_gate_refuses_after_claim(self):
        tmp = Path(tempfile.mkdtemp()); log = self._ready_log(tmp)
        spend.assert_scoring_allowed(log)          # allowed (structure:read + attempt, no claim)
        spend.claim_authorized_read(log)           # claim (key now spent)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)      # a second scorer run is refused (claim present)

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
        ref.write_text((WS / "_reference/smoke_v09_frozen.py").read_text())
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
        ref.write_text((WS / "_reference/smoke_v09_frozen.py").read_text())
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
        spend.append_event(log, "structure:read")
        with self.assertRaises(SystemExit):
            spend.append_event(log, "structure:read")

    def test_scorer_passes_with_one_structure_read(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")
        spend.assert_scoring_allowed(log)   # must NOT raise (one structure-read + attempt, no claim)

    def test_scorer_refuses_zero_structure_reads(self):   # round-5: the >1-only bug fix
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "state:scoring-attempt")  # attempt but NO structure:read
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log)              # claim also requires exactly one

    def test_scorer_refuses_untyped_entry(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        log.write_text(json.dumps({"event": "bogus:thing", "utc": "x"}) + "\n")
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)

    def test_scorer_refuses_answer_read_entry(self):
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")
        spend.claim_authorized_read(log)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)

    def test_one_pre_read_failure_then_relaunch(self):    # round-5: bounded relaunch path
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")  # attempt 1 (scorer fails pre-read, no claim)
        spend.append_event(log, "state:scoring-attempt")  # attempt 2 (the ONE relaunch)
        spend.claim_authorized_read(log)                  # relaunch reaches the claim -> OK
        spend.complete_authorized_read(log)
        with self.assertRaises(SystemExit):
            spend.append_event(log, "state:scoring-attempt")  # a 3rd attempt is refused

    def test_crash_after_claim_refuses_second_invocation(self):  # round-5: post-read crash
        tmp = Path(tempfile.mkdtemp()); log = tmp / "spend.jsonl"
        spend.append_event(log, "structure:read")
        spend.append_event(log, "state:scoring-attempt")
        spend.claim_authorized_read(log)                  # claim, then "crash" (no complete)
        with self.assertRaises(SystemExit):
            spend.assert_scoring_allowed(log)             # second invocation refused (spent)
        with self.assertRaises(SystemExit):
            spend.claim_authorized_read(log)              # cannot re-claim

    # ---- 2: projector hash gate ----
    def test_projector_registers_structure_read_on_valid_hash(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"; log = tmp / "spend.jsonl"
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            str(WS / "toy-key/key"), str(out),
                            "--recorded-hashes", str(WS / "toy-key/recorded-hashes.txt"),
                            "--spend-log", str(log)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(out.exists())
        events = [e["event"] for e in spend.read_events(log)]
        self.assertEqual(events, ["structure:read"])

    def test_projector_aborts_on_hash_mismatch_nothing_read(self):
        tmp = Path(tempfile.mkdtemp()); out = tmp / "pairs.json"; log = tmp / "spend.jsonl"
        bad = tmp / "bad-recorded.txt"
        bad.write_text("0000000000000000000000000000000000000000000000000000000000000000  key/concepts.json\n"
                       "0000000000000000000000000000000000000000000000000000000000000000  key/answer_key.json\n")
        r = subprocess.run([sys.executable, str(WS / "make_pairs_manifest.py"),
                            str(WS / "toy-key/key"), str(out),
                            "--recorded-hashes", str(bad), "--spend-log", str(log)],
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ABORT (nothing read)", r.stdout + r.stderr)
        self.assertFalse(out.exists())               # nothing written
        self.assertEqual(spend.read_events(log), [])  # structure:read NOT registered (gate before it)

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
