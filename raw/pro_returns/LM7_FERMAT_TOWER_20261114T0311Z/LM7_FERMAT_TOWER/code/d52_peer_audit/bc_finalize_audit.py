#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
frozen=ROOT/"D52_EXPERIMENTS"
manifest=json.loads((frozen/"ledger/d_finite_invariant_repair_manifest.json").read_text())
checks=[]
for row in manifest["files"]+manifest["retained_attempts"]+[manifest["runtime_input"],manifest["historical_input_not_read_by_final_programs"]]:
    path=frozen/row["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest()==row["sha256"],row["path"]
    checks.append(row["path"])
cert=json.loads((HERE/"bc_peripheral_parameter_check.json").read_text())
assert cert["status"]=="PASS"
assert cert["peripheral_pair_space_rank"]==120
assert cert["actual_derivation_image_rank"]==18
assert cert["actual_homology_derivation_image_rank"]==18
assert cert["pair_to_derivation_kernel_dimension"]==102
result={
    "status":"PASS",
    "scope":"Full D52 written proof/program audit, with an independently executed exact pair-to-derivation kernel computation. Root owns the complete fresh three-program rebuild.",
    "clarification":"The120-dimensional space is the conjugator-pair parameter space. Its actual derivation image has dimension18 and kernel W^r x W^s of dimension102. Author and root have agreed the wording clarification; frozen theorem files were not altered by this auditor.",
    "frozen_section_sha256":manifest["files"][0]["sha256"],
    "verified_manifest_files":checks,
    "runtime_input_sha256":manifest["runtime_input"]["sha256"],
    "parameter_certificate":cert,
    "owned_files":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.iterdir()) if p.is_file() and p.name not in {"audit.json","bc_finalize_audit.out"}}
}
(HERE/"audit.json").write_text(json.dumps(result,indent=2)+"\n")
other=ROOT/"bc_e96_audit"
old=json.loads((other/"audit.json").read_text())
old["full_text_review"]={
    "status":"PASS",
    "path":"research_e96/sections/E_zero_free_elliptic_obstruction.tex",
    "sha256_at_review":hashlib.sha256((ROOT/"research_e96/sections/E_zero_free_elliptic_obstruction.tex").read_bytes()).hexdigest(),
    "notes":"Full theorem/proof, marking, both global directions, rational-prime equivariance and all modulo-three inertia rays check. Two missing TeX backslashes in E96.9 reported to root."
}
old["files"]={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(other.iterdir()) if p.is_file() and p.name!="audit.json"}
(other/"audit.json").write_text(json.dumps(old,indent=2)+"\n")
print("PASS: all",len(checks),"D52 frozen manifest entries, exact18/102 parameter maps and full focused proof audit.")
print("PASS: E96 full-text review appended to the independent algebra/lattice audit.")
