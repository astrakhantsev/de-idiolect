#!/usr/bin/env python3
"""Offline test suite for the v0.8 controller (prereg-v08.md). NO model calls.
Covers: all 16 (La,Lb) composition cells incl. mirrors, terminal conditions in §4
order, reviewRequired serialization, the full E1 bar (incl. the false-escalation
boundary) + E1b + E1c, mechanical validators (§9-F5), strict output schemas,
surface-similarity flag (§5), retrieval tie-break (§9-F7), the sampling-pool rule
(§9-F3/B1: all 11 docs, no reserved split), call-completion bookkeeping (round-3 F2),
and the decompose/containment result classification on fixture files."""
import json, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import smoke

# ---------- fixtures ----------
def lv(k=0, c=0, u=0, downgrades=(), pre=None):
    dec = k + c
    if dec < 2: agg = "abstain"
    elif k >= 2 and c == 0: agg = "covers"
    elif c >= 2 or k / dec <= 0.3: agg = "fails"
    else: agg = "mixed"
    return {"n": k + c + u, "k": k, "c": c, "u": u,
            "pre_decided": pre if pre is not None else dec,
            "agg": agg, "quote_downgrades": list(downgrades)}

def dres(L, monotone=True, starved=False, collapsed=False, c_L1=0, status="ok"):
    if status != "ok": return {"status": status}
    return {"status": "ok",
            "levels": {"L0": lv(2), "L1": (lv(0, c_L1, 2) if c_L1 else lv(2)), "L2": lv(2)},
            "L": L, "monotone": monotone, "starved": starved, "collapsed": collapsed}

def ctx(A, B, mutual=False, flag=False, sym=None, dc=None, ct=None,
        configfail=None, floor=None):
    return {"configfail": configfail, "floor_fail": floor,
            "dirs": {"a2b": A, "b2a": B}, "symcheck": sym, "mutual": mutual,
            "decompose": dc, "containment": ct, "flag": flag}

PAIR = {"pair_id": "PX", "term_a": "alpha stone", "term_b": "beta gravel",
        "expected": "exactMatch"}

def key10():
    mk = lambda i, a, b, exp, br=None: dict(
        pair_id=f"P{i:02d}", term_a=a, term_b=b, expected=exp,
        **({"broader_side": br} if br else {}))
    return [mk(1, "t1a", "t1b", "exactMatch"), mk(2, "t2a", "t2b", "exactMatch"),
            mk(3, "t3a", "t3b", "broadnarrow", "a"), mk(4, "t4a", "t4b", "broadnarrow", "b"),
            mk(5, "t5a", "t5b", "relatedMatch"), mk(6, "t6a", "t6b", "relatedMatch"),
            mk(7, "jingle one", "jingle one", "noMatchDespiteSimilarity"),
            mk(8, "jingle two", "jingle two", "noMatchDespiteSimilarity"),
            mk(9, "t9a", "t9b", "noMatch"), mk(10, "t10a", "t10b", "noMatch")]

def A_(rel, broader=None): return smoke._v(rel, "asserted", broader=broader)
def RR(reason="r"): return smoke._v(None, "review_required", reason)
def IE(reason="r"): return smoke._v(None, "insufficient_evidence", reason)
def CF(reason="r"): return smoke._v(None, "config_fail", reason)

PATH_P_CELLS = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (0, 0), (0, -1), (-1, 0), (-1, -1)]

# ---------- composition table (§5) ----------
class TestCompositionTable(unittest.TestCase):
    def test_totality_all_16_cells(self):
        for La in (-1, 0, 1, 2):
            for Lb in (-1, 0, 1, 2):
                v = smoke.compose_pair(PAIR, ctx(dres(La), dres(Lb)))
                self.assertIn(v["status"],
                              ("asserted", "review_required", "insufficient_evidence"),
                              f"cell ({La},{Lb}) fell through")

    def test_exact(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(2)))
        self.assertEqual((v["proposed_relation"], v["status"]), ("exactMatch", "asserted"))

    def test_detail_divergence_both_orientations(self):
        for La, Lb in ((2, 1), (1, 2)):
            v = smoke.compose_pair(PAIR, ctx(dres(La), dres(Lb)))
            self.assertEqual(v["status"], "review_required")
            self.assertEqual(v["reason"], "detail-divergence")

    def test_row3_confirmed_broadnarrow(self):
        for Lb in (0, -1):
            v = smoke.compose_pair(PAIR, ctx(dres(2), dres(Lb, c_L1=2),
                                             sym={"status": "ok", "confirms": True}))
            self.assertEqual(v["proposed_relation"], "broadnarrow")
            self.assertEqual(v["broader_side"], "a")

    def test_row3_mirror(self):
        for La in (0, -1):
            v = smoke.compose_pair(PAIR, ctx(dres(La, c_L1=2), dres(2),
                                             sym={"status": "ok", "confirms": True}))
            self.assertEqual(v["proposed_relation"], "broadnarrow")
            self.assertEqual(v["broader_side"], "b")

    def test_row4_unconfirmed(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(0, c_L1=2),
                                         sym={"status": "ok", "confirms": False}))
        self.assertEqual((v["status"], v["reason"]),
                         ("review_required", "asymmetry-unconfirmed"))

    def test_row5_no_deep_c(self):
        # incl. the c>=2-only-at-L2 case: deep-c is pinned to L1 (§0.5)
        A, B = dres(2), dres(0)
        B["levels"]["L2"] = lv(0, 3)
        v = smoke.compose_pair(PAIR, ctx(A, B))
        self.assertEqual((v["status"], v["reason"]),
                         ("review_required", "unexplained-asymmetry"))

    def test_row3_symcheck_missing_or_bad_is_iE(self):
        for sym in (None, {"status": "missing"}, {"status": "unparseable"},
                    {"status": "refused"}):
            v = smoke.compose_pair(PAIR, ctx(dres(2), dres(0, c_L1=2), sym=sym))
            self.assertEqual(v["status"], "insufficient_evidence")
            self.assertTrue(v["reason"].startswith("symcheck-"))

    def test_pathP_no_mutual(self):
        for La, Lb in PATH_P_CELLS:
            v = smoke.compose_pair(PAIR, ctx(dres(La), dres(Lb), mutual=False))
            self.assertEqual((v["proposed_relation"], v["status"]), ("noMatch", "asserted"))
            v = smoke.compose_pair(PAIR, ctx(dres(La), dres(Lb), mutual=False, flag=True))
            self.assertEqual(v["proposed_relation"], "noMatchDespiteSimilarity")

    def test_pathP_decompose_routes(self):
        base = lambda **kw: ctx(dres(1), dres(1), mutual=True, **kw)
        self.assertEqual(smoke.compose_pair(PAIR, base(dc=None))["status"],
                         "insufficient_evidence")
        self.assertEqual(smoke.compose_pair(PAIR, base(dc={"status": "fail", "detail": "quote-validation"}))["status"],
                         "insufficient_evidence")
        v = smoke.compose_pair(PAIR, base(dc={"status": "abstain"}))
        self.assertEqual(v["proposed_relation"], "noMatch")  # ABSTAIN is semantic, not failure
        v = smoke.compose_pair(PAIR, base(dc={"status": "abstain"}, flag=True))
        self.assertEqual(v["proposed_relation"], "noMatchDespiteSimilarity")

    def test_pathP_containment_routes(self):
        base = lambda **kw: ctx(dres(1), dres(1), mutual=True,
                                dc={"status": "ok", "core": "x"}, **kw)
        self.assertEqual(smoke.compose_pair(PAIR, base(ct=None))["status"],
                         "insufficient_evidence")
        self.assertEqual(smoke.compose_pair(PAIR, base(ct={"status": "fail", "detail": "quote-validation"}))["status"],
                         "insufficient_evidence")
        cases = {"t1_within_t2": ("broadnarrow", "b"), "t2_within_t1": ("broadnarrow", "a"),
                 "partial_overlap": ("relatedMatch", None)}
        for rel, (want, br) in cases.items():
            v = smoke.compose_pair(PAIR, base(ct={"status": "ok", "relation": rel}))
            self.assertEqual(v["proposed_relation"], want)
            if br: self.assertEqual(v["broader_side"], br)
        v = smoke.compose_pair(PAIR, base(ct={"status": "ok", "relation": "no_relation"}))
        self.assertEqual(v["proposed_relation"], "noMatch")
        v = smoke.compose_pair(PAIR, base(ct={"status": "ok", "relation": "no_relation"}, flag=True))
        self.assertEqual(v["proposed_relation"], "noMatchDespiteSimilarity")
        v = smoke.compose_pair(PAIR, base(ct={"status": "ok", "relation": "unclear"}))
        self.assertEqual((v["status"], v["reason"]),
                         ("review_required", "containment-unclear"))

# ---------- terminals (§4, in order) ----------
class TestTerminals(unittest.TestCase):
    def test_configfail_first(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(2), configfail="polarity-inversion:a:x",
                                         floor="sample<4"))
        self.assertEqual(v["status"], "config_fail")

    def test_floor_before_verify(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2, status="missing"), dres(2),
                                         floor="sample<4:a:x:n=2"))
        self.assertEqual((v["status"], v["reason"]),
                         ("insufficient_evidence", "sample<4:a:x:n=2"))

    def test_verify_failures(self):
        for st in ("missing", "unparseable", "refused"):
            v = smoke.compose_pair(PAIR, ctx(dres(2, status=st), dres(2)))
            self.assertEqual((v["status"], v["reason"]),
                             ("insufficient_evidence", f"verify-a2b-{st}"))

    def test_quote_collapse_either_direction(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(-1, starved=True, collapsed=True)))
        self.assertEqual((v["status"], v["reason"]),
                         ("insufficient_evidence", "quote-collapse-b2a"))

    def test_non_monotone_either_direction(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2, monotone=False), dres(2)))
        self.assertEqual((v["status"], v["reason"]),
                         ("insufficient_evidence", "non-monotone-a2b"))

    def test_both_starved(self):
        v = smoke.compose_pair(PAIR, ctx(dres(-1, starved=True), dres(-1, starved=True)))
        self.assertEqual((v["status"], v["reason"]),
                         ("insufficient_evidence", "both-directions-starved"))

    def test_one_starved_not_terminal(self):
        # (2,-1) with b2a starved (no deep-c possible) -> row 5 reviewRequired, NOT terminal
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(-1, starved=True)))
        self.assertEqual((v["status"], v["reason"]),
                         ("review_required", "unexplained-asymmetry"))

# ---------- serialization (§3) ----------
class TestSerialization(unittest.TestCase):
    def test_review_required_serialization(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(1)))
        self.assertIsNone(v["proposed_relation"])
        self.assertEqual(v["status"], "review_required")
        self.assertTrue(v["reason"])

    def test_asserted_serialization(self):
        v = smoke.compose_pair(PAIR, ctx(dres(2), dres(2)))
        self.assertEqual(v["proposed_relation"], "exactMatch")
        self.assertEqual(v["status"], "asserted")

    def test_display_names(self):
        self.assertEqual(smoke.display(RR("x")), "reviewRequired(x)")
        self.assertEqual(smoke.display(IE("y")), "insufficientEvidence(y)")
        self.assertEqual(smoke.display(CF("z")), "configFail(z)")
        self.assertEqual(smoke.display(A_("broadnarrow", "a")), "broadnarrow(a)")

# ---------- endpoints (§6) ----------
class TestE1Bar(unittest.TestCase):
    def base_correct(self):
        K = key10()
        v = {"P01": A_("exactMatch"), "P02": A_("exactMatch"),
             "P03": A_("broadnarrow", "a"), "P04": A_("broadnarrow", "b"),
             "P05": A_("relatedMatch"), "P06": A_("relatedMatch"),
             "P07": A_("noMatchDespiteSimilarity"), "P08": A_("noMatchDespiteSimilarity"),
             "P09": A_("noMatch"), "P10": A_("noMatch")}
        return K, v

    def test_perfect_passes(self):
        K, v = self.base_correct()
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 10); self.assertTrue(s["E1_PASS"])
        self.assertEqual(s["E1c_graded"], 10.0)
        self.assertEqual(s["E1b_detection"], {"tp": 6, "fn": 0, "tn": 4, "fp": 0, "abstain": 0})

    def test_one_false_escalation_passes(self):
        K, v = self.base_correct()
        v["P08"] = A_("noMatch")      # jingle miss, not a promotion
        v["P09"] = RR("x")            # false escalation #1
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 8)
        self.assertEqual(s["false_escalations"], ["P09"])
        self.assertTrue(s["E1_PASS"])

    def test_two_false_escalations_fail(self):
        K, v = self.base_correct()
        v["P09"] = RR("x"); v["P10"] = RR("y")
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 8)          # still >= 7 correct
        self.assertEqual(len(s["false_escalations"]), 2)
        self.assertFalse(s["E1_PASS"])               # killed by the escalation cap alone

    def test_promotion_fails(self):
        K, v = self.base_correct()
        v["P09"] = A_("relatedMatch")
        s = smoke.score(K, v)
        self.assertEqual(s["promotions"], ["P09"])
        self.assertFalse(s["E1_PASS"])

    def test_jingle_zero_fails(self):
        K, v = self.base_correct()
        v["P07"] = A_("noMatch"); v["P08"] = A_("noMatch")
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 8)
        self.assertEqual(s["jingle_specific"], 0)
        self.assertFalse(s["E1_PASS"])

    def test_below_seven_fails(self):
        K, v = self.base_correct()
        for pid in ("P01", "P02", "P05", "P06"): v[pid] = IE("x")
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 6)
        self.assertFalse(s["E1_PASS"])

    def test_broadnarrow_needs_planted_side(self):
        K, v = self.base_correct()
        v["P03"] = A_("broadnarrow", "b")  # wrong side
        s = smoke.score(K, v)
        self.assertEqual(s["n_correct"], 9)
        self.assertFalse(s["per_pair"]["P03"]["correct"])
        # wrong-side broadnarrow on a planted match pair is not a promotion
        self.assertEqual(s["promotions"], [])

    def test_review_required_never_correct(self):
        K, v = self.base_correct()
        v["P01"] = RR("detail-divergence")
        s = smoke.score(K, v)
        self.assertFalse(s["per_pair"]["P01"]["correct"])

    def test_e1c_grades(self):
        K, v = self.base_correct()
        v["P01"] = IE("x")                  # 0.4
        v["P05"] = RR("x")                  # 0.7 (match-class pair)
        v["P09"] = RR("x")                  # 0.2 (no-match pair)
        v["P10"] = CF("x")                  # 0.0
        s = smoke.score(K, v)
        self.assertAlmostEqual(s["E1c_graded"], 6 * 1.0 + 0.4 + 0.7 + 0.2 + 0.0)

    def test_e1b_abstain_and_positive_classes(self):
        K, v = self.base_correct()
        v["P01"] = IE("x"); v["P02"] = CF("x")   # abstain x2
        v["P09"] = RR("x")                        # positive on planted no-match -> fp
        s = smoke.score(K, v)
        d = s["E1b_detection"]
        self.assertEqual(d["abstain"], 2)
        self.assertEqual(d["fp"], 1)
        self.assertEqual(d["tp"], 4)
        self.assertEqual(d["tn"], 3)

# ---------- mechanical validators (§9-F5) ----------
class TestValidators(unittest.TestCase):
    def test_sentence_count(self):
        self.assertEqual(smoke.sentence_count("One sentence."), 1)
        self.assertEqual(smoke.sentence_count("No terminator at all"), 1)
        self.assertEqual(smoke.sentence_count("First one. Second one. Third."), 3)
        self.assertEqual(smoke.sentence_count("Uses e.g. lowercase after dot. Fine."), 2)

    def good_ladder(self):
        return {"L0": "A procedure that checks one thing for a purpose.",
                "L1": "A procedure that checks one thing for a purpose. "
                      "It works by comparing two runs of the same item. "
                      "The comparison is done by hand.",
                "L2": ("A procedure that checks one thing for a purpose. "
                       "It works by comparing two runs of the same item, done by hand. "
                       "The output is a binary flag per item, read as pass or fail. "
                       "It applies whenever an item is suspected of instability, "
                       "before any score is published, and it requires both runs "
                       "to be complete and to use exactly the same configuration.")}

    def test_ladder_mech_pass(self):
        self.assertEqual(smoke.ladder_mech_issues(self.good_ladder()), [])

    def test_ladder_mech_failures(self):
        bad = dict(self.good_ladder()); bad["L0"] = "Two sentences here. Second one."
        self.assertTrue(any("L0-not-1-sentence" in i for i in smoke.ladder_mech_issues(bad)))
        bad = dict(self.good_ladder()); bad["L0"] = "word " * 46
        self.assertTrue(any("L0-over-45" in i or "L0-not-1-sentence" in i
                            for i in smoke.ladder_mech_issues(bad)))
        bad = dict(self.good_ladder()); bad["L1"] = "One sentence only."
        self.assertTrue(any("L1-sentences" in i for i in smoke.ladder_mech_issues(bad)))
        bad = dict(self.good_ladder()); bad["L2"] = "Too short. Really just a few words here."
        self.assertTrue(any("L2-words" in i for i in smoke.ladder_mech_issues(bad)))
        self.assertEqual(smoke.ladder_mech_issues("not a dict"), ["not-a-json-object"])
        self.assertTrue(smoke.ladder_mech_issues({"L0": "x."}))

    def test_checklist_mech(self):
        ok = "\n".join(f"- commitment line {i}" for i in range(5))
        self.assertEqual(smoke.checklist_mech_issues(ok), [])
        self.assertTrue(smoke.checklist_mech_issues("- one\n- two\n- three"))
        self.assertTrue(smoke.checklist_mech_issues("\n".join(f"- l{i}" for i in range(8))))
        self.assertTrue(smoke.checklist_mech_issues("- " + "word " * 41 + "\n- a\n- b\n- c"))

    def test_matrix_schema(self):
        row = lambda i: {"excerpt": i, "L0": "instantiates",
                         "L1": {"verdict": "instantiates", "quote": "q"},
                         "L2": {"verdict": "insufficient", "quote": ""}}
        good = [row(1), row(2), row(3)]
        self.assertIsNotNone(smoke.validate_matrix_rows(good, 3))
        self.assertIsNone(smoke.validate_matrix_rows(good, 4))            # wrong count
        self.assertIsNone(smoke.validate_matrix_rows([row(1), row(1), row(3)], 3))  # dup id
        self.assertIsNone(smoke.validate_matrix_rows([row(1), row(2), row(9)], 3))  # out of range
        bad = [row(1), row(2), dict(row(3))]; del bad[2]["L2"]
        self.assertIsNone(smoke.validate_matrix_rows(bad, 3))             # missing level
        bad = [row(1), row(2), dict(row(3))]
        bad[2]["L1"] = {"verdict": "maybe", "quote": ""}
        self.assertIsNone(smoke.validate_matrix_rows(bad, 3))             # unknown enum
        self.assertIsNone(smoke.validate_matrix_rows("nope", 3))

    def test_flat_schema(self):
        rows = [{"item": 1, "verdict": "ok"}, {"item": 2, "verdict": "inverted"}]
        self.assertIsNotNone(smoke.validate_flat_rows(rows, 2, id_key="item",
                                                      enum={"ok", "inverted"}, extra=()))
        self.assertIsNone(smoke.validate_flat_rows(rows, 3, id_key="item",
                                                   enum={"ok", "inverted"}, extra=()))
        self.assertIsNone(smoke.validate_flat_rows([{"item": 1, "verdict": "meh"}], 1,
                                                   id_key="item", enum={"ok", "inverted"}, extra=()))

    def test_containment_schema(self):
        good = {"relation": "no_relation", "quote_1": "a", "quote_2": "b", "justification": "c"}
        self.assertIsNotNone(smoke.validate_containment(good))
        self.assertIsNone(smoke.validate_containment({"relation": "within"}))
        self.assertIsNone(smoke.validate_containment(None))
        # round-3 F3: ALL FOUR keys required; a missing key is malformed
        self.assertIsNone(smoke.validate_containment({"relation": "unclear"}))
        for drop in ("quote_1", "quote_2", "justification"):
            bad = dict(good); del bad[drop]
            self.assertIsNone(smoke.validate_containment(bad), f"missing {drop} must be malformed")
        unclear = {"relation": "unclear", "quote_1": "", "quote_2": "", "justification": "j"}
        self.assertIsNotNone(smoke.validate_containment(unclear))

    def test_conformance_schema(self):
        # round-3 F4: reason required; NONEMPTY for nonconformant
        ok = [{"item": 1, "verdict": "conformant", "reason": ""},
              {"item": 2, "verdict": "nonconformant", "reason": "condition 3: drops mechanism"}]
        self.assertIsNotNone(smoke.validate_conformance_rows(ok, 2))
        self.assertIsNone(smoke.validate_conformance_rows(ok, 3))  # wrong count
        self.assertIsNone(smoke.validate_conformance_rows(
            [{"item": 1, "verdict": "nonconformant", "reason": ""}], 1))     # bare nonconformant
        self.assertIsNone(smoke.validate_conformance_rows(
            [{"item": 1, "verdict": "nonconformant"}], 1))                   # reason key missing
        self.assertIsNone(smoke.validate_conformance_rows(
            [{"item": 1, "verdict": "maybe", "reason": "x"}], 1))            # bad enum
        self.assertIsNotNone(smoke.validate_conformance_rows(
            [{"item": 1, "verdict": "conformant", "reason": "note"}], 1))    # note on conformant ok

    def test_quote_matcher_semantics(self):
        # round-3 F1 disposition: folding admits case/typography/whitespace, never words
        texts = ["The “Alpha” run — was checked twice.", "Beta text here two.",
                 "Gamma text here three."]
        rows = {1: {"verdict": "instantiates", "quote": 'the "alpha" run - was checked'},
                2: {"verdict": "instantiates", "quote": "beta   text here"},
                3: {"verdict": "insufficient", "quote": ""}}
        v = smoke.level_verdict(rows, texts, quote_required=True)
        self.assertEqual((v["k"], v["quote_downgrades"]), (2, []))  # folded variants accepted
        rows[1]["quote"] = "the alpha run was checked once"          # altered word
        v = smoke.level_verdict(rows, texts, quote_required=True)
        self.assertEqual(v["quote_downgrades"], [1])

    def test_level_verdict_rules(self):
        texts = ["alpha text one", "beta text two", "gamma text three", "delta four"]
        rows = {1: {"verdict": "instantiates", "quote": "alpha text"},
                2: {"verdict": "instantiates", "quote": "beta text"},
                3: {"verdict": "insufficient", "quote": ""},
                4: {"verdict": "insufficient", "quote": ""}}
        v = smoke.level_verdict(rows, texts, quote_required=True)
        self.assertEqual((v["k"], v["c"], v["agg"]), (2, 0, "covers"))
        rows2 = dict(rows); rows2[2] = {"verdict": "instantiates", "quote": "NOT PRESENT"}
        v = smoke.level_verdict(rows2, texts, quote_required=True)
        self.assertEqual((v["k"], v["agg"], v["quote_downgrades"]), (1, "abstain", [2]))
        rows3 = {1: {"verdict": "contradicts", "quote": "alpha text"},
                 2: {"verdict": "contradicts", "quote": "beta text"},
                 3: {"verdict": "instantiates", "quote": "gamma text"},
                 4: {"verdict": "insufficient", "quote": ""}}
        v = smoke.level_verdict(rows3, texts, quote_required=True)
        self.assertEqual(v["agg"], "fails")  # c >= 2
        rows4 = {1: {"verdict": "instantiates", "quote": "alpha text"},
                 2: {"verdict": "contradicts", "quote": "beta text"},
                 3: {"verdict": "instantiates", "quote": "gamma text"},
                 4: {"verdict": "instantiates", "quote": "delta four"}}
        v = smoke.level_verdict(rows4, texts, quote_required=True)
        self.assertEqual(v["agg"], "mixed")  # k3 c1: ratio 0.75, c < 2

    def test_matrix_direction_monotone_and_collapse(self):
        texts = ["alpha text one", "beta text two", "gamma text three"]
        mk = lambda spec: {i + 1: {"L0": {"verdict": spec[0][i], "quote": ""},
                                   "L1": {"verdict": spec[1][i], "quote": texts[i][:5]},
                                   "L2": {"verdict": spec[2][i], "quote": texts[i][:5]}}
                           for i in range(3)}
        I, C, U = "instantiates", "contradicts", "insufficient"
        d = smoke.matrix_direction(mk(([I, I, I], [I, I, I], [I, I, I])), texts)
        self.assertEqual((d["L"], d["monotone"], d["starved"]), (2, True, False))
        # L0 fails, L2 covers -> non-monotone
        d = smoke.matrix_direction(mk(([C, C, U], [I, I, I], [I, I, I])), texts)
        self.assertEqual((d["L"], d["monotone"]), (2, False))
        # decided L1/L2 verdicts with invalid quotes collapse to starvation
        bad = mk(([U, U, U], [I, I, U], [I, I, U]))
        for i in bad:
            for lvl in ("L1", "L2"):
                if bad[i][lvl]["verdict"] == I: bad[i][lvl]["quote"] = "ZZZ"
        d = smoke.matrix_direction(bad, texts)
        self.assertEqual((d["L"], d["starved"], d["collapsed"]), (-1, True, True))
        # plain starvation without downgrades is not collapse
        d = smoke.matrix_direction(mk(([U, U, U], [U, U, U], [U, U, U])), texts)
        self.assertEqual((d["starved"], d["collapsed"]), (True, False))

    def test_row3_candidate(self):
        agg = {"PX": {"a2b": dres(2), "b2a": dres(0, c_L1=2)}}
        self.assertEqual(smoke._row3_candidate("PX", agg, None), ("b2a", "a"))
        agg = {"PX": {"a2b": dres(0, c_L1=2), "b2a": dres(2)}}
        self.assertEqual(smoke._row3_candidate("PX", agg, None), ("a2b", "b"))
        agg = {"PX": {"a2b": dres(2), "b2a": dres(0)}}  # no deep-c
        self.assertIsNone(smoke._row3_candidate("PX", agg, None))
        agg = {"PX": {"a2b": dres(2), "b2a": dres(1, c_L1=2)}}  # Lb=1 not row 3
        self.assertIsNone(smoke._row3_candidate("PX", agg, None))

# ---------- surface-similarity flag (§5 exact) ----------
class TestSimFlag(unittest.TestCase):
    def test_identical_and_case(self):
        self.assertTrue(smoke.sim_flag("echo test", "Echo Test"))
        self.assertTrue(smoke.sim_flag("a—b", "a-b"))  # dash folding via norm

    def test_trigram_overlap(self):
        self.assertTrue(smoke.sim_flag("salt run", "salt runs"))
        self.assertFalse(smoke.sim_flag("groove lock", "trajectory template carryover"))

    def test_short_string_rule(self):
        self.assertTrue(smoke.sim_flag("ab", "ab"))    # clause (i)
        self.assertFalse(smoke.sim_flag("ab", "ba"))   # clause (ii) blocked when S < 3 chars

# ---------- retrieval tie-break (§9-F7) ----------
class TestRank(unittest.TestCase):
    def test_tie_break_lower_doc_index(self):
        self.assertEqual(smoke.rank_top3([0.5, 0.9, 0.9, 0.1]), [1, 2, 0])
        self.assertEqual(smoke.rank_top3([0.9, 0.9, 0.9, 0.9]), [0, 1, 2])

# ---------- sampling pool (§9-F3, B1: all 11 docs, first-6 prefix) ----------
class TestSamplePool(unittest.TestCase):
    def test_sample_asserts_pool_bound(self):
        entry = {"pool": [{"doc": "12", "idx": 0, "text": "x"}]}
        with self.assertRaises(AssertionError):
            smoke.sample_of(entry)

    def test_sample_first_six_prefix(self):
        entry = {"pool": [{"doc": f"{i:02d}", "idx": i, "text": "x"} for i in range(1, 12)]}
        s = smoke.sample_of(entry)
        self.assertEqual(len(s), 6)
        self.assertEqual([e["doc"] for e in s], ["01", "02", "03", "04", "05", "06"])
        thin = {"pool": [{"doc": "01", "idx": 0, "text": "x"}] * 3}
        self.assertEqual(len(smoke.sample_of(thin)), 3)  # floor handled by §4, not padding

# ---------- review-layer separation (v09-review F6: scoring never reads dispositions) ----------
class TestReviewSeparation(unittest.TestCase):
    def test_scoring_never_reads_review_state(self):
        src = (Path(__file__).resolve().parent / "smoke.py").read_text()
        for needle in ("decisions.jsonl", "tau-setting"):
            self.assertNotIn(needle, src,
                             f"smoke.py must never reference {needle} — the review layer is operational only")

# ---------- call-completion bookkeeping (round-3 F2) ----------
class TestCallBookkeeping(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.out = self.d / "out.json"; self.mf = self.d / "manifest.json"

    def write(self, out_text=None, manifest_lines=None):
        if out_text is not None: self.out.write_text(out_text)
        if manifest_lines is not None: self.mf.write_text("\n".join(manifest_lines) + "\n")

    def test_never_attempted(self):
        self.assertFalse(smoke.call_attempted(self.mf))
        self.assertFalse(smoke.call_completed(self.out, self.mf))

    def test_interrupted_no_clean_exit(self):
        self.write(out_text="partial", manifest_lines=["kind: claude"])
        self.assertTrue(smoke.call_attempted(self.mf))
        self.assertFalse(smoke.call_completed(self.out, self.mf))

    def test_completed_hash_match(self):
        import hashlib
        self.write(out_text="payload")
        h = hashlib.sha256(b"payload").hexdigest()
        self.write(manifest_lines=["kind: claude", f"out_sha256: {h}", "exit: 0"])
        self.assertTrue(smoke.call_completed(self.out, self.mf))

    def test_completed_hash_mismatch(self):
        self.write(out_text="tampered or truncated",
                   manifest_lines=["kind: claude", "out_sha256: " + "0" * 64, "exit: 0"])
        self.assertFalse(smoke.call_completed(self.out, self.mf))

# ---------- decompose / containment result classification on fixture files ----------
class TestStageResults(unittest.TestCase):
    def setUp(self):
        self._runs = smoke.RUNS
        smoke.RUNS = Path(tempfile.mkdtemp())
        (smoke.RUNS / "decompose").mkdir(parents=True)
        (smoke.RUNS / "containment").mkdir(parents=True)
        self.pair = {"pair_id": "P99", "term_a": "alpha stone", "term_b": "beta gravel"}
        self.exc = {"a": {"alpha stone": {"pool": [
                        {"doc": "01", "idx": 0, "text": "We ran the alpha stone check on every batch yesterday."}] * 4}},
                    "b": {"beta gravel": {"pool": [
                        {"doc": "01", "idx": 0, "text": "The beta gravel procedure was applied to each queue."}] * 4}}}
        self.terms = {"a": ["alpha stone"], "b": ["beta gravel"]}

    def tearDown(self):
        smoke.RUNS = self._runs

    def dwrite(self, text):
        (smoke.RUNS / "decompose/out-P99.json").write_text(text)

    def cwrite(self, text):
        (smoke.RUNS / "containment/out-P99.json").write_text(text)

    def test_decompose_abstain_literal(self):
        self.dwrite("ABSTAIN")
        self.assertEqual(smoke.decompose_result("P99", self.pair, self.exc, self.terms),
                         {"status": "abstain"})
        self.dwrite("```\nABSTAIN\n```")
        self.assertEqual(smoke.decompose_result("P99", self.pair, self.exc, self.terms)["status"],
                         "abstain")

    def test_decompose_missing_and_unparseable(self):
        self.assertEqual(smoke.decompose_result("P99", self.pair, self.exc, self.terms),
                         {"status": "fail", "detail": "missing"})
        self.dwrite("I think there might be a shared core, roughly speaking.")
        self.assertEqual(smoke.decompose_result("P99", self.pair, self.exc, self.terms)["status"],
                         "fail")

    def test_decompose_quotes(self):
        good = {"core": "checking every unit of work",
                "quote_1": "check on every batch", "quote_2": "applied to each queue"}
        self.dwrite(json.dumps(good))
        self.assertEqual(smoke.decompose_result("P99", self.pair, self.exc, self.terms)["status"],
                         "ok")
        bad = dict(good, quote_1="not actually present anywhere")
        self.dwrite(json.dumps(bad))
        r = smoke.decompose_result("P99", self.pair, self.exc, self.terms)
        self.assertEqual((r["status"], r["detail"]), ("fail", "quote-validation"))

    def test_containment_quote_rules(self):
        good = {"relation": "partial_overlap", "quote_1": "check on every batch",
                "quote_2": "applied to each queue", "justification": "j"}
        self.cwrite(json.dumps(good))
        self.assertEqual(smoke.containment_result("P99", self.pair, self.exc, self.terms),
                         {"status": "ok", "relation": "partial_overlap"})
        bad = dict(good, quote_2="fabricated words")
        self.cwrite(json.dumps(bad))
        r = smoke.containment_result("P99", self.pair, self.exc, self.terms)
        self.assertEqual((r["status"], r["detail"]), ("fail", "quote-validation"))
        # unclear is quote-exempt (§9-F5)
        unclear = {"relation": "unclear", "quote_1": "", "quote_2": "", "justification": "j"}
        self.cwrite(json.dumps(unclear))
        self.assertEqual(smoke.containment_result("P99", self.pair, self.exc, self.terms),
                         {"status": "ok", "relation": "unclear"})

if __name__ == "__main__":
    unittest.main(verbosity=1)
