#!/usr/bin/env python3
"""Freeze E97's literal witness, exact defect maps and retained attempt history."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
LED=ROOT/"ledger"
def write(name,obj):(LED/name).write_text(json.dumps(obj,indent=2)+"\n")
tex=ROOT/"sections/E_unit_norm_coset.tex"
body=tex.read_text()
assert len(re.findall(r"(?<!\\)\\\[",body))==17
assert len(re.findall(r"(?<!\\)\\\]",body))==17
assert len(re.findall(r"\\tag\{E97\.\d+\}",body))==17
assert not any(ord(c)<32 and c not in "\n\t" for c in body)
for env in ("statement","proof","gathered","array","pmatrix","cases"):
    assert body.count("\\begin{"+env+"}")==body.count("\\end{"+env+"}"),env
cert=json.loads((ROOT/"code/e_unit_norm_coset.json").read_text())
assert cert["status"]=="PASS" and cert["ordinary_unit_defect"]==[0,1]
assert cert["xic1_S_unit_defect"]==1
assert cert["independent_Hensel_valuation_checks"]==12
assert cert["class_coordinate_inverses"]==27
write("e_unit_norm_coset_results.json",[{
 "id":"E.97","status":"Proved",
 "statement":"The actual ordinary-unit defect map E(L1)/N E(L2) to Cl(L2){3}/<q3>=C3^2 sends zeta3 to (0,1). A literal cyclic-algebra norm switch and complete four-orbit divisor evaluate this class. Horizontal norm then gives omega_B(xi*c1)=+1 in the coherent prime73 basis of Cl_S(B2){3}=C3. Consequently xi*c1 is a field norm but not an S-unit norm. The full completed power line has norm preimages exactly for r in3Z3; at r=3z the fiber is the literal included (xi*c1)^z times the actual norm kernel C3 plus Z3^18.",
 "where_proved":"sections/E_unit_norm_coset.tex, E97.1--17 and complete proof; code/e_unit_norm_coset.gp/.py with their actual outputs, complete PARI data and independent rational/Hensel/class checks.",
 "depends_on":["E.64","E.69","E.79","E.84","E.86","E.88","E.91","E_MilneCFT","E_LemmermeyerAmbiguous"],
 "manuscript_passages":["LM section51.16, folios733v--736v, scans172--178, via the exact positional norm maps E46/E88."],
 "depends_on_doubtful_reading":False,
 "notes":"Author fresh two-stage GP/Python rebuild PASS. Only the degree-six lower BNF/genus is rebuilt; no upper BNF is used. The eventual exponent h and old B3 transvection remain unevaluated. Complete failed API/representation attempts and exploratory norm constructions are retained."
}])
write("e_unit_norm_coset_coverage.json",{
 "statement":"E.97",
 "addresses":[{"task":"Part E(c),(d), Item2/Lead3 through the actual positional norm quotient H",
               "status":"Evaluated finite norm obstruction and complete power-line fibers",
               "exact_maps":"The explicit cyclic-algebra matrix switch, Hilbert90 divisor defect, ordinary-to-strongly-ambiguous class quotient, commuting vertical/horizontal field norms, coherent S-class norm z to(0,z), and completed norm image."}],
 "closed_previous_step":"The concrete xi*c1 S-unit norm coset left in E84 is nonzero, with value+1 in the established prime73 basis.",
 "remaining":["The eventual three-unit norm exponent h.","The B3 ordinary transvection W and higher ordinary prime orders.","All positional fibers beyond the evaluated line and systems already proved in E46--E94.","The intrinsic higher-quotient section questions retained in E23."]
})
write("e_unit_norm_coset_source_evidence.json",{
 "statement":"E.97",
 "sources":[
  {"key":"E_LemmermeyerAmbiguous","url":"https://arxiv.org/pdf/1309.1071",
   "opened":"Proposition1 and complete proof, printed pp2--3, opened turn806view1, turn807view0, turn808view1.",
   "usage":"Exact ambiguous/strongly-ambiguous quotient and unit norm defect. The actual inverse map and both kernel directions are proved in E97.",
   "source_precision":"The surjectivity paragraph prints Am_st where Am is required; the stated exact sequence is correct and E97 gives the orbit/Hilbert90 proof directly."},
  {"key":"E_MilneCFT","url":"https://www.jmilne.org/math/CourseNotes/CFT.pdf",
   "opened":"II Proposition1.22 and Corollary1.23, complete proof on printed p67/PDF75, turn808view0; VIII Theorem3.1 and complete proof on printed p234/PDF242, turn809view0.",
   "usage":"The actual norm-one ratio is sigma(v)/v; local norms at all places imply the cyclic field norm. Exact norm-square orientations are proved directly."}
 ],
 "internal_primary_arithmetic":["E64's certified lower fundamental units and residue cubes.","E86's full lower Hilbert genus, actual class-coordinate maps, S-class norm and norm-kernel calculation.","E84's corrected field-norm membership and E86's principal Q1Q2Q3.","E91's ordinary norm surjectivity and exact extension identity."],
 "independent_rational_checks":"Literal degree-six norm identity, all three cyclic-algebra matrix identities, absolute degree-eighteen norm, 12 independent Hensel valuations, 27 inverse class coordinates and nine quotient cosets.",
 "independent_audit":"Root and a_structure have been sent the full proof and portable certificate; no fresh independent full rebuild PASS is asserted at this freeze."
})
dep=ROOT.parent/"research_e86/code/e_stable_lower_genus.gp"
write("e_unit_norm_coset_dependencies.json",{
 "main_rebuild":[{"source":"e_stable_lower_genus.gp","sha256":hashlib.sha256(dep.read_bytes()).hexdigest(),
                  "origin":"E86's certified lower genus; driver searches beside itself first, then the research_e86/code fallback."}],
 "exploratory_inputs":[
  "research_e86/code/e_stable_lower_genus.bin",
  "research_e86/code/e_stable_class_coordinates.bin",
  "research_norm_index/code/cyclotomic_base1_bnf.bin",
  "research_norm_index/code/prime3_field2.bin"],
 "portable_command":"python code/e_unit_norm_coset.py --gp /path/to/gp",
 "retained_main_data":["code/e_unit_norm_coset.bin","code/e_unit_norm_coset_lower.bin"]
})
files=[]
for sub in ("sections","code","ledger"):
    for p in sorted((ROOT/sub).iterdir()):
        if not p.is_file():continue
        if p.name in ("e_unit_norm_coset_manifest.json","e_unit_norm_freeze.out"):continue
        files.append({"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size})
manifest={"status":"frozen_for_parent_and_peer_audit","statement":"E.97",
          "main_rebuild":"PASS, two GP stages and independent Python verification",
          "math_scope":"Exact xi*c1 norm coset and completed power-line fibers; h and the old transvection remain open.",
          "files":files}
write("e_unit_norm_coset_manifest.json",manifest)
print(json.dumps({"status":"PASS","files":len(files),"displays":17,
                  "section_sha256":hashlib.sha256(tex.read_bytes()).hexdigest(),
                  "certificate_sha256":hashlib.sha256((ROOT/"code/e_unit_norm_coset.json").read_bytes()).hexdigest(),
                  "manifest_sha256":hashlib.sha256((LED/"e_unit_norm_coset_manifest.json").read_bytes()).hexdigest()},indent=2))
