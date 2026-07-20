#!/usr/bin/env python3
"""Append the amendment-A1 d02 record (PubMed take-first, no skips) and freeze the manifest."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).parent
RECORDS = HERE / "records" / "corpus_records.jsonl"

d02 = {
    "id": "d02",
    "set": "owner",
    "field": "value of information analysis",
    "source_id": "PMID:37345680",
    "title": "Value-of-Information Analysis for External Validation of Risk Prediction Models.",
    "abstract": "Background: A previously developed risk prediction model needs to be validated before being used in a new population. The finite size of the validation sample entails that there is uncertainty around model performance. We apply value-of-information (VoI) methodology to quantify the consequence of uncertainty in terms of net benefit (NB). Methods: We define the expected value of perfect information (EVPI) for model validation as the expected loss in NB due to not confidently knowing which of the alternative decisions confers the highest NB. We propose bootstrap-based and asymptotic methods for EVPI computations and conduct simulation studies to compare their performance. In a case study, we use the non-US subsets of a clinical trial as the development sample for predicting mortality after myocardial infarction and calculate the validation EVPI for the US subsample. Results: The computation methods generated similar EVPI values in simulation studies. EVPI generally declined with larger samples. In the case study, at the prespecified threshold of 0.02, the best decision with current information would be to use the model, with an incremental NB of 0.0020 over treating all. At this threshold, the EVPI was 0.0005 (relative EVPI = 25%). When scaled to the annual number of heart attacks in the US, the expected NB loss due to uncertainty was equal to 400 true positives or 19,600 false positives, indicating the value of further model validation. Conclusion: VoI methods can be applied to the NB calculated during external validation of clinical prediction models. While uncertainty does not directly affect the clinical implications of NB findings, validation EVPI provides an objective perspective to the need for further validation and can be reported alongside NB in external validation studies.",
    "url": "https://pubmed.ncbi.nlm.nih.gov/37345680/",
    "rationale": "addresses when information of a given quality is worth acquiring or acting on (Amendment A1: PubMed substitution for unreachable frozen sources; first relevant result in source order, no skips)",
}

lines = [json.loads(l) for l in RECORDS.read_text().splitlines() if l.strip()]
assert not any(r["id"] == "d02" for r in lines), "d02 already present"
lines.append(d02)
lines.sort(key=lambda r: r["id"])
assert len(lines) == 18, f"expected 18, got {len(lines)}"
owners = [r["id"] for r in lines if r["set"] == "owner"]
assert len(owners) == 3, f"owners: {owners}"

RECORDS.write_text("\n".join(json.dumps(r) for r in lines) + "\n")

freeze = {
    "frozen_at": "pre-generation (no D/N/F queries exist yet)",
    "file_sha256": hashlib.sha256(RECORDS.read_bytes()).hexdigest(),
    "per_record": {r["id"]: hashlib.sha256(json.dumps(r).encode()).hexdigest()[:16] for r in lines},
    "owner_ids": owners,
    "n_docs": len(lines),
}
(HERE / "records" / "FROZEN.json").write_text(json.dumps(freeze, indent=2))
print(f"18 records frozen; owners={owners}; file sha256={freeze['file_sha256'][:16]}...")
