#!/usr/bin/env python3
"""Retain E101 proof, exact sources, actual exploratory output, and metadata."""
from __future__ import annotations
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parent.parent
WORK=ROOT.parent
LEDGER=ROOT/"ledger";LEDGER.mkdir(exist_ok=True)
def save(name,obj):
    (LEDGER/name).write_text(json.dumps(obj,indent=2)+"\n")
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

status=json.loads((WORK/"research_h_after_e97/computation_status.json").read_text())
status["observed_UTC"]="2026-11-13 16:42:07"
status["no_duplicate_BNF_started"]=True
status["distinct_discovery_field"]={
    "session_id":66170,
    "source":"research_h_after_e97/unit_kummer_bnf.gp",
    "stdout":"research_h_after_e97/unit_kummer_bnf.out",
    "binary":"research_h_after_e97/unit_kummer_bnf.bin",
    "command":"timeout 60s research_e52/vendor/pari-2.19.0/gp -q research_h_after_e97/unit_kummer_bnf.gp > research_h_after_e97/unit_kummer_bnf.out 2>&1",
    "actual_exit_code":124,
    "status":"BNF initialization completed and data saved; subsequent certification timed out",
    "class_group_output_used_as_evidence":False,
    "use":"Candidate generators supplied a literal reversed norm, which the final certificate independently verifies without reading this binary."}
for row in status["jobs"]:
    row["last_poll_UTC"]="2026-11-13 16:39:54"
    row["last_poll_new_output"]="none"
    row["status"]="superseded run terminated by explicit interrupt"
    row["termination_exit_code"]=130
    row["termination_new_output"]=""
    row["termination_observed_UTC"]="2026-11-13 16:42:07"
    start=datetime.fromisoformat(row["started_UTC"])
    stop=datetime.fromisoformat("2026-11-13 16:42:07")
    row["elapsed_seconds_at_termination"]=(stop-start).total_seconds()
    row["stdout_sha256"]=digest(WORK/row["stdout"])
    row["reason"]=("The requested class/discriminant/ramification data are now proved by E86. "
        "The reduced input differs only by beta to minus beta. Neither unfinished run had "
        "exported an upper BNF; the original script did not request an upper unit basis. "
        "Completed lower computations and all actual stdout are preserved. No missing "
        "certification result or class-group value is inferred.")
(WORK/"research_h_after_e97/computation_status.json").write_text(json.dumps(status,indent=2)+"\n")
save("e_unit_norm_complete_computation_status.json",status)

inputs=ROOT/"inputs";inputs.mkdir(exist_ok=True)
for name in ("e_stable_lower_genus","e_basechange_field","e_basechange_local_norms"):
    source=WORK/"LM7_FERMAT_TOWER/code"/(name+".gp")
    shutil.copyfile(source,inputs/source.name)
history=ROOT/"code/e101_history";history.mkdir(exist_ok=True)
for source in (WORK/"research_h_after_e97").iterdir():
    if source.is_file():shutil.copyfile(source,history/source.name)
old=history/"superseded_bnf";old.mkdir(exist_ok=True)
for name in ("first_layers.gp","first_layers.out","layer2_reduced.gp","layer2_reduced.out"):
    shutil.copyfile(WORK/"research_prime17"/name,old/name)
(history/"README.md").write_text("""# Actual exploratory work preceding E.101

Every source and actual output in this directory is retained, including
representation errors, bounded searches with no hit, and timed-out certification.
The final portable proof is in the two e_unit_norm_*.gp files one directory up.

`unit_kummer_bnf.bin` is discovery data. Its BNF initialization completed and
was saved, but the certification command timed out after sixty seconds (exit124).
No theorem uses its displayed class group or the completeness of its units.
The literal reversed norm extracted with those candidate generators is checked
independently by rational polynomial identities in the final certificate.

`ordinary_unit_preimage.out` records 160 weighted ideal reductions without a
generator hit. The target ideal is proved principal by the exact class map and
the full ambiguous-class order27. This unsuccessful bounded search gives no
nonprincipality or non-norm conclusion.

Both original radical-upper BNF jobs were explicitly interrupted after their
requested arithmetic outputs had been superseded by proved class-field maps.
Their actual outputs and the successful lower-field results are preserved in
`superseded_bnf/`; the status JSON records exit130, not a completed certification.

Historical sources retain their actual workspace input paths. The final
five-stage driver has its own complete portable input routing and does not read
either unfinished upper BNF, the discovery BNF, or a historical failed output.
""")

result={
"id":"E.101","status":"Proved",
"statement":"The ordinary-unit divisor defect of e1*e2 in L2/L1 is (0,2) in the established genus coordinates. Together with E97 this evaluates the complete ordinary L-unit norm image a=b=c mod3 and complete L S-unit norm image with the additional c1 exponent divisible by3. The actual horizontal norm evaluates the remaining B1 field-norm-kernel scalar, yielding all six S-unit congruences and all four ordinary-unit congruences, exact quotient maps and image inverses. Every nonempty completed fiber has the actual norm-one kernel, of type C3 plus Z3^6 over L or C3 plus Z3^18 over B.",
"where_proved":"sections/E_first_unit_norms.tex, E101.1--24 and complete proof; code/e_unit_norm_scalar.gp, e_unit_norm_coordinates.gp and e_unit_norm_complete.py with all actual outputs and full PARI data.",
"depends_on":["E.64","E.76","E.79","E.86","E.88","E.91","E.97","E_MilneCFT","E_LemmermeyerAmbiguous"],
"manuscript_passages":["LM section51.16, folios733v--736v, scans172--178, through the actual positional norm comparison E46/E88."],
"depends_on_doubtful_reading":False,
"notes":"The independently verified literal reversed norm replaces reliance on the uncertified discovery BNF. The complete first-layer norm images are evaluated; a bounded extraction of a numerical generator of the proved principal correction ideal had no hit. The eventual exponent h, the B3 transvection, and compatibility beyond the stated first maps remain separate. Author five-stage rebuild and independent rational/matrix verification are retained; peer/root audit statuses are recorded separately."}
save("e_unit_norm_complete_results.json",[result])
save("e_unit_norm_complete_coverage.json",{
"statement":"E.101","addresses":[{"task":"Part E(c),(d), Item2/Lead3 through the actual norm quotient H","status":"Complete first ordinary/S-unit norm images over L1 and B1 with exact image/fiber maps","exact_maps":"Literal cyclic-algebra eigenline, divisor defect, actual lower genus Artin map, horizontal field norm and integral projection inverse, local-character kernel, scalar defect, Smith coordinates and completion."}],
"closed_previous_step":"The unevaluated scalar on the epsilon=e1*e2 horizontal direction is2; all first-step B1 S-unit and ordinary-unit norm memberships are consequently computed.",
"remaining":["The eventual coherent three-unit exponent h.","The B3 ordinary transvection W and later distinguished prime orders.","A literal numerical generator d for the proved principal correction ideal in E101.19; existence and its exact norm consequences are proved.","Higher compatible positional norm systems beyond the maps already evaluated in E46--E101.","The remaining intrinsic higher-quotient section questions in E23."]})
save("e_unit_norm_complete_source_evidence.json",{
"statement":"E.101",
"sources":[
 {"key":"E_LemmermeyerAmbiguous","url":"https://arxiv.org/pdf/1309.1071","opened":"Theorem1, Proposition1, and the full printed derivation through the end of section3; freshly opened turn839view0, turn840view0, turn841view0 and turn841view1.","usage":"The whole ambiguous ideal-class group has order27; therefore the fixed correction ideal with zero three-primary coordinates is actually principal. Proposition1 gives the exact divisor/ordinary-unit defect.","source_precision":"The proof invokes the unit Herbrand quotient as Theorem2, with references; no claim is made that the article separately proves that auxiliary theorem. Proposition1's surjectivity paragraph has the printed Am_st/Am slip already recorded in E97."},
 {"key":"E_MilneCFT","url":"https://www.jmilne.org/math/CourseNotes/CFT.pdf","opened":"V Proposition3.3 with its entire norm/Frobenius proof, Theorem3.6 and Example3.9 freshly opened turn841view2--4. E97's opened II1.22--23 and VIII3.1 supply Hilbert90 and cyclic Hasse norm theorem.","usage":"The actual Artin coordinate of an upper prime is the coordinate of its norm, with the relative residue-degree factor; the Hilbert class-field map and exact norm criterion have the stated orientations."}],
"internal_arithmetic":["E64's certified lower unit basis and seventeen residues.","E76/E79's certified B1 basis and full six local norm characters.","E86's actual Hilbert genus, ordinary/S-class maps and norm defect exactness.","E97's literal zeta norm witness and (0,1) defect."],
"new_exact_certificate":"Literal reversed norm of beta1, three cyclic-algebra identities, relative/absolute eigenline and norm identities, full ideal HNF identity, complete three-prime contraction/Artin calculation, both Smith transforms and inverses, and 59049 field-norm kernel vectors.",
"discovery_only":"The auxiliary unit-radical BNF was saved before its certification timeout; no class group or complete unit basis from it is used in any proof.",
"independent_audit":"Full draft and final code were sent to root and a_structure; no unreceived independent audit is claimed at this author freeze."})
save("e_unit_norm_complete_dependencies.json",{
"portable_rebuild":"python code/e_unit_norm_complete.py --gp /absolute/path/to/gp",
"PARI_version":"2.19.0","Python_dependencies":["sympy"],
"dependency_sources":[{"path":"inputs/"+name+".gp","sha256":digest(inputs/(name+".gp"))} for name,_ in [("e_stable_lower_genus",0),("e_basechange_field",0),("e_basechange_local_norms",0)]],
"upper_radical_BNF_computation":False,"uncertified_discovery_BNF_input":False,
"binary_retention":"The full rebuild retains both owned BIN certificates and the complete lower genus, certified B1 BNF, and local-character BIN inputs."})
(LEDGER/"e_unit_norm_complete_refs.bib").write_text("% E101 reuses the verified existing entries E_MilneCFT and E_LemmermeyerAmbiguous; no duplicate entries.\n")

proof=(ROOT/"sections/E_first_unit_norms.tex").read_text()
assert proof.count(r"\[")==proof.count(r"\]")==24
assert not any(ord(ch)<32 and ch not in "\n\t" for ch in proof)
summary=json.loads((ROOT/"code/e_unit_norm_complete.json").read_text())
assert summary["status"]=="PASS" and summary["complete_field_norm_kernel_vectors"]==59049
assert "Traceback" not in (ROOT/"code/e_unit_norm_complete_rebuild.out").read_text()
manifest={"statement":"E.101","files":[]}
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():continue
    rel=path.relative_to(ROOT).as_posix()
    if rel in {"ledger/e_unit_norm_complete_manifest.json","code/e_unit_norm_freeze.out"}:continue
    manifest["files"].append({"path":rel,"bytes":path.stat().st_size,"sha256":digest(path)})
save("e_unit_norm_complete_manifest.json",manifest)
print(json.dumps({"statement":"E.101","status":"AUTHOR_FREEZE_PASS","file_count":len(manifest["files"]),
                  "section_sha256":digest(ROOT/"sections/E_first_unit_norms.tex"),
                  "program_sha256":digest(ROOT/"code/e_unit_norm_complete.py"),
                  "summary_sha256":digest(ROOT/"code/e_unit_norm_complete.json"),
                  "old_BNF_exit_codes":[130,130]},indent=2))
