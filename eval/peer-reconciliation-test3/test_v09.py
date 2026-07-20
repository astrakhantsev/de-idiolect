#!/usr/bin/env python3
"""Offline tests for the v0.9 resample controller (prereg-v09.md). NO model calls.
Covers: per-τ covers boundaries, promotion algebra (base required; SILENCE rule R10 —
c>=1 stops extension; mixed/fails stop; consecutive extension; τ0 never promotes),
the row-3 promotion-base rule (R4), union-route closure (R3), τ0 regression against
the raw v0.8 aggregation, τ-mutual mapping, primary-point pin, and the review-layer
separation guard for the v0.9 controller."""
import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import smoke
import v09

def lv(k=0, c=0, u=0):
    return {"n": k + c + u, "k": k, "c": c, "u": u, "pre_decided": k + c,
            "agg": "", "quote_downgrades": []}

def raw(l0, l1, l2, collapsed=False):
    """Raw direction dict as smoke.matrix_direction emits (L/monotone recomputed by tau_dir)."""
    levels = {"L0": l0, "L1": l1, "L2": l2}
    def agg(x):
        dec = x["k"] + x["c"]
        if dec < 2: return "abstain"
        if x["k"] >= 2 and x["c"] == 0: return "covers"
        if x["c"] >= 2 or x["k"] / dec <= 0.3: return "fails"
        return "mixed"
    order = ("L0", "L1", "L2")
    L = max((i for i, l in enumerate(order) if agg(levels[l]) == "covers"), default=-1)
    return {"status": "ok", "levels": levels, "L": L,
            "monotone": not any(agg(levels[l]) == "fails" for i, l in enumerate(order) if i < L),
            "starved": all(levels[l]["k"] + levels[l]["c"] < 2 for l in order),
            "collapsed": collapsed}

class TestTauCovers(unittest.TestCase):
    def test_boundaries(self):
        self.assertTrue(v09.tau_covers(2, 0, "tau0"))
        self.assertFalse(v09.tau_covers(2, 1, "tau0"))
        self.assertFalse(v09.tau_covers(2, 1, "tau1"))
        self.assertTrue(v09.tau_covers(2, 1, "tau2"))   # one dissent tolerated at tau2 only
        self.assertFalse(v09.tau_covers(1, 1, "tau2"))  # k floor holds
        self.assertFalse(v09.tau_covers(1, 0, "tau2"))
        # k2c2 must be fails, never covers, at every point
        for tau in v09.TAUS:
            self.assertFalse(v09.tau_covers(2, 2, tau))

class TestPromotion(unittest.TestCase):
    def test_tau0_never_promotes(self):
        d = v09.tau_dir(raw(lv(3), lv(3), lv(0, 0, 4)), "tau0")
        self.assertEqual((d["base_L"], d["L"], d["promoted"]), (1, 1, False))

    def test_silent_extension(self):
        d = v09.tau_dir(raw(lv(3), lv(3), lv(0, 0, 4)), "tau1")
        self.assertEqual((d["base_L"], d["L"], d["promoted"]), (1, 2, True))
        # extension through TWO silent levels from an L0 base
        d = v09.tau_dir(raw(lv(3), lv(0, 0, 4), lv(0, 0, 4)), "tau1")
        self.assertEqual((d["base_L"], d["L"]), (0, 2))
        # k1c0 above base is silent (k+c<2, c=0) -> extends
        d = v09.tau_dir(raw(lv(3), lv(3), lv(1, 0, 3)), "tau1")
        self.assertEqual(d["L"], 2)

    def test_silence_rule_blocks_contradiction(self):
        # R10: a single valid contradiction above the base is abstain but NOT silent
        d = v09.tau_dir(raw(lv(3), lv(3), lv(0, 1, 3)), "tau1")
        self.assertEqual((d["base_L"], d["L"], d["promoted"]), (1, 1, False))

    def test_mixed_and_fails_stop_extension(self):
        d = v09.tau_dir(raw(lv(3), lv(2, 1, 1), lv(0, 0, 4)), "tau1")  # L1 mixed
        self.assertEqual((d["base_L"], d["L"]), (0, 0))
        d = v09.tau_dir(raw(lv(3), lv(0, 3), lv(0, 0, 4)), "tau1")     # L1 fails
        self.assertEqual((d["base_L"], d["L"]), (0, 0))

    def test_no_promotion_without_base(self):
        d = v09.tau_dir(raw(lv(0, 0, 4), lv(0, 0, 4), lv(0, 0, 4)), "tau1")
        self.assertEqual((d["base_L"], d["L"], d["starved"]), (-1, -1, True))

    def test_tau0_regression_matches_raw(self):
        for spec in ((lv(3), lv(3), lv(3)), (lv(3), lv(2, 1, 1), lv(0, 0, 4)),
                     (lv(0, 3), lv(3), lv(3)), (lv(0, 0, 4), lv(0, 0, 4), lv(0, 0, 4))):
            r = raw(*spec)
            d = v09.tau_dir(r, "tau0")
            self.assertEqual(d["L"], r["L"], f"tau0 must reproduce raw L for {spec}")

class TestBaseRule(unittest.TestCase):
    def test_genus_only_promotion_cannot_assert_row3(self):
        dirs = {"a2b": v09.tau_dir(raw(lv(3), lv(0, 0, 4), lv(0, 0, 4)), "tau1"),  # base L0 -> L†2
                "b2a": v09.tau_dir(raw(lv(3), lv(0, 4), lv(0, 4)), "tau1")}
        cand = v09.row3_candidate(dirs)
        self.assertEqual(cand, ("b2a", "a"))
        v = smoke._v("broadnarrow", "asserted", broader="a")
        out = v09.apply_base_rule(v, dirs, cand)
        self.assertEqual((out["status"], out["reason"]),
                         ("review_required", "promotion-base-genus-only"))

    def test_mechanism_base_promotion_asserts(self):
        dirs = {"a2b": v09.tau_dir(raw(lv(3), lv(3), lv(0, 0, 4)), "tau1"),  # base L1 -> L†2
                "b2a": v09.tau_dir(raw(lv(3), lv(0, 4), lv(0, 4)), "tau1")}
        cand = v09.row3_candidate(dirs)
        v = smoke._v("broadnarrow", "asserted", broader="a")
        self.assertEqual(v09.apply_base_rule(v, dirs, cand), v)

    def test_unpromoted_assertion_untouched(self):
        dirs = {"a2b": v09.tau_dir(raw(lv(3), lv(3), lv(3)), "tau1"),
                "b2a": v09.tau_dir(raw(lv(3), lv(0, 4), lv(0, 4)), "tau1")}
        v = smoke._v("broadnarrow", "asserted", broader="a")
        self.assertEqual(v09.apply_base_rule(v, dirs, v09.row3_candidate(dirs)), v)

    def test_pathP_containment_broadnarrow_untouched(self):
        """Round-2 F1 regression: a PATH-P broadnarrow (containment-derived) with a
        promoted genus-only base is NOT the row-3 rule's business — no candidate, no veto."""
        dirs = {"a2b": v09.tau_dir(raw(lv(3), lv(0, 0, 4), lv(0, 0, 4)), "tau1")}
        dirs["a2b"]["L"] = 1  # promoted only to L†=1 (silent L1); L2 not silent in this fixture
        dirs["b2a"] = v09.tau_dir(raw(lv(3), lv(1, 0, 3), lv(0, 1, 3)), "tau1")
        self.assertIsNone(v09.row3_candidate(dirs))
        v = smoke._v("broadnarrow", "asserted", broader="a")
        self.assertEqual(v09.apply_base_rule(v, dirs, None), v)

class TestGating(unittest.TestCase):
    def test_authorization_reads_primary_only(self):
        results = {"primary": "tau1",
                   "tau0": {"E1_PASS": False}, "tau1": {"E1_PASS": False},
                   "tau2": {"E1_PASS": True}}
        self.assertFalse(v09.authorized(results))  # τ2-only pass never fires TEST
        results["tau1"]["E1_PASS"] = True
        self.assertTrue(v09.authorized(results))

class TestDecideGrammar(unittest.TestCase):
    def test_broadnarrow_requires_side(self):
        import review_pairs
        self.assertEqual(review_pairs.parse_override("override:broadnarrow(a)"),
                         ("broadnarrow", "a"))
        self.assertEqual(review_pairs.parse_override("override:broadnarrow(b)"),
                         ("broadnarrow", "b"))
        with self.assertRaises(SystemExit):
            review_pairs.parse_override("override:broadnarrow")
        with self.assertRaises(SystemExit):
            review_pairs.parse_override("override:kindaMatch")
        self.assertEqual(review_pairs.parse_override("override:relatedMatch"),
                         ("relatedMatch", None))

class TestRouting(unittest.TestCase):
    def p04_like(self):
        # a2b: L0 covers, deep-c at L1 -> raw L=0; b2a: base L1 with silent L2
        return {"a2b": raw(lv(6), lv(0, 4, 2), lv(0, 4, 2)),
                "b2a": raw(lv(3), lv(2, 0, 4), lv(0, 0, 6))}

    def test_union_covers_route_change_across_tau(self):
        agg = {"PX": self.p04_like()}
        retr = {"PX": {"L2": {"mutual": True}, "L0L1": {"mutual": True}}}
        sym, dec = v09.route_unions(agg, retr)
        # tau0: (0,1) path P with mutual -> decompose required
        self.assertIn("PX", dec)
        # tau1/tau2: b2a promotes to 2 -> row 3 with deep-c in a2b -> symcheck required
        self.assertIn(("PX", "a2b"), sym)

    def test_pathP_and_row3_predicates(self):
        td0 = {d: v09.tau_dir(x, "tau0") for d, x in self.p04_like().items()}
        td1 = {d: v09.tau_dir(x, "tau1") for d, x in self.p04_like().items()}
        self.assertTrue(v09.pathP(td0))
        self.assertIsNone(v09.row3_candidate(td0))
        self.assertFalse(v09.pathP(td1))
        self.assertEqual(v09.row3_candidate(td1), ("a2b", "b"))

    def test_tau_mutual_mapping(self):
        entry = {"L2": {"mutual": False}, "L0L1": {"mutual": True}}
        self.assertFalse(v09.tau_mutual(entry, "tau0"))
        self.assertTrue(v09.tau_mutual(entry, "tau1"))
        self.assertTrue(v09.tau_mutual(entry, "tau2"))

class TestGovernance(unittest.TestCase):
    def test_primary_is_tau1(self):
        self.assertEqual(v09.PRIMARY, "tau1")

    def test_v09_scoring_never_reads_review_state(self):
        src = (Path(__file__).resolve().parent / "v09.py").read_text()
        for needle in ("decisions.jsonl", "tau-setting"):
            self.assertNotIn(needle, src)

if __name__ == "__main__":
    unittest.main(verbosity=1)
