#!/usr/bin/env python3
"""Freeze E106 with complete literal inputs, outputs, and proof record."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/"ledger"
LEDGER.mkdir(exist_ok=True)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,value):
    (LEDGER/name).write_text(json.dumps(value,indent=2)+"\n")

proof=ROOT/"sections/E_next_ordinary_classes.tex"
code=ROOT/"code/e_next_unit_characters.py"
summary=ROOT/"code/e_next_unit_characters.json"
data=json.loads(summary.read_text())
assert data["status"]=="PASS"
assert data["finite_input_count"]==19683
assert data["image_rank"]==4 and data["finite_image_count"]==81
assert data["each_finite_fiber_count"]==243
assert data["B3_entire_class_group"]==[9,9,3]
assert data["L3_entire_class_group"]==[9,3]
assert data["E91_transvection_W_order"]==1
assert data["horizontal_ordinary_unit_norm_index"]==1
assert data["original_q3_order"]==3
assert (ROOT/"code/e_next_unit_characters.out").read_bytes()==summary.read_bytes()
gpout=(ROOT/"code/e_next_prime_maps.out").read_text()
assert '"type":"completion","status":"PASS"' in gpout
assert "***   at top-level" not in gpout and "***   user error" not in gpout
tex=proof.read_text()
assert len(re.findall(r"(?m)^\\\[$",tex))==len(re.findall(r"(?m)^\\\]$",tex))==20
assert not any(ord(c)<32 and c not in "\n\t" for c in tex)
assert [int(n) for n in re.findall(r"\\tag\{E106\.(\d+)\}",tex)]==list(range(1,21))
for name,digest in data["inputs"].items():
    assert sha(ROOT/"inputs"/name)==digest

result={
 "id":"E.106","status":"Proved",
 "statement":(
 "The actual local norm/inclusion square divides the E76 ninth-character map "
 "on the COMPLETE E101 ordinary-unit norm lattice by three. Its six arithmetic "
 "cubic characters have rank4. Hence the entire ordinary three-class group "
 "Cl(B3){3} is C9^2+C3, the E91 transvection W is zero, the existing ninth-genus "
 "field is the full Hilbert three-class field, and Cl(L3){3}=C9+C3 with the "
 "distinguished prime above3 of order3. All adjacent/horizontal ideal norm and "
 "extension maps, the six actual S-prime classes, the full principal S-divisor "
 "lattice and its inverse are evaluated. The actual horizontal ordinary unit "
 "norm B3 to L3 is onto. The vertical ordinary norm quotients are C3^5 over B2 "
 "and C3^3 over L2, with completed norm kernels C3+Z3^54 and C3+Z3^18."),
 "where_proved":(
 "sections/E_next_ordinary_classes.tex, E106.1--20 and full proof; "
 "code/e_next_unit_characters.py and e_next_prime_maps.gp with complete actual "
 "stdout, JSON, finite row/column maps and inverses, and all literal inputs."),
 "depends_on":["E.64","E.69","E.72","E.76","E.86","E.88","E.91","E.94","E.101",
               "E_MilneCFT","E_LemmermeyerAmbiguous"],
 "manuscript_passages":[
 "LM section51.16, folios733v--736v, scans172--178, through the actual positional norm maps E46/E69/E72/E88."],
 "depends_on_doubtful_reading":False,
 "notes":(
 "The source lattice is the complete ordinary norm image. Every ninth-character "
 "product entry is divisible by3, with the arithmetic mu3 inclusion into mu9 "
 "explicitly fixed. The owned GP step recertifies the retained degree18 B1 field "
 "and computes literal prime7/73 ray Frobenii; it computes no BNF in B2, B3, L2, "
 "or L3. The finite projection exponent a3 is1. The eventual all-level h and later "
 "ordinary prime orders are not evaluated here. Independent audits are separate.")
}
save("e_next_ordinary_results.json",[result])
save("e_next_ordinary_coverage.json",{
 "statement":"E.106",
 "addresses":[{
   "task":"Part E(c),(d), Item2/Lead3 through the actual positional norm quotient H",
   "status":"Complete third ordinary class projection and all stated adjacent/horizontal norm maps",
   "exact_maps":(
    "Local Artin norm/inclusion square with exponent3; complete E101 norm-lattice "
    "inclusion P; six-character matrix D and both finite inverses; actual genus "
    "restriction; ray restriction and prime7/73 Frobenii; ideal norm/extension "
    "matrices; principal-divisor inverse; strongly ambiguous divisor quotient "
    "and completion.")}],
 "closed_previous_steps":[
   "E91's B3 transvection W is zero.",
   "The original L3 prime above3 has order3, so the E69 finite projection a3 is1.",
   "All ideal norm/extension maps in the square B3,B2,L3,L2 are evaluated.",
   "The full principal S-divisor lattice at B3 and ordinary-unit norm defects at this step are evaluated."],
 "remaining":[
   "The eventual coherent three-unit exponent h of E69.",
   "Later ordinary distinguished-prime orders and any later vertical transvection on the original L tower.",
   "The remaining intrinsic/metabelian section classification recorded in E23."]})
save("e_next_ordinary_source_evidence.json",{
 "statement":"E.106",
 "sources":[
  {
   "key":"E_MilneCFT",
   "url":"https://www.jmilne.org/math/CourseNotes/CFT.pdf",
   "opened":(
    "III Theorem3.1 and its complete proved restriction/corestriction cup-product "
    "compatibility, III section4 Hilbert-symbol definition/Theorem4.4/proof and "
    "Remark4.5 freshly read in turn851view0, turn853view0 and turn853view1. "
    "VIII Theorem3.1 and full proof freshly read in turn856view0. The exact "
    "ideal-norm/Frobenius square V Proposition3.3 and Hilbert-class-field "
    "correspondence V Theorem3.6/Example3.9 were opened in prior E91/E101 audits."),
   "usage":"Actual local norm/inclusion square and exponent3, cyclic Hasse norm theorem, Hilbert90, and ideal-norm/Artin coordinate maps.",
   "source_precision":(
    "III Lemma3.2 prints 'Proof. To be added'. The square is derived from the "
    "proved Tate cup-product Res/Cor compatibility immediately before it; no "
    "complete printed proof of the lemma is claimed.")
  },
  {
   "key":"E_LemmermeyerAmbiguous",
   "url":"https://arxiv.org/pdf/1309.1071",
   "opened":"Theorem1, Proposition1 and complete ideal/Herbrand derivation through section3, freshly read in turn851view1, turn852view0 and turn853view2.",
   "usage":"Ambiguous class order with ordinary-unit FIELD-norm index, strongly ambiguous divisor/ordinary-unit quotient, and unramified capitulation formula with actual ideal maps.",
   "source_precision":(
    "The article invokes the unit Herbrand quotient as Theorem2 with references. "
    "No separate printed proof of that auxiliary theorem is claimed. The "
    "Proposition1 surjectivity paragraph's Am_st/Am slip is bypassed by the "
    "explicit orbitwise Hilbert90 construction.")
  },
  {
   "key":"E_PARICertifiedUnits",
   "url":"https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify",
   "opened":"The exact default-flag0 certification semantics were opened in prior E76/E101 source audits.",
   "usage":"The fresh owned GP step calls bnfcertify(B) with default flag0 and verifies return1 on the retained B1 data."
  }],
 "internal_arithmetic":[
  "E76's literal B1 unit basis, six ninth-character rows, full ray Smith transforms and actual ray restriction.",
  "E94's exact arithmetic row weights (5,5,5,8,5,4).",
  "E101's COMPLETE ordinary-unit norm lattice, compared by exact unimodular matrices and literal unit polynomial equality.",
  "E91's proved trivial vertical ordinary B action, full genus Artin quotient and prime columns.",
  "E86's actual horizontal norm maps, coherent prime73 S-basis and original ideal-class bases."],
 "author_execution":"The full owned --gp rebuild exited0, reran the certified B1 prime calculation, and verified every finite map. Complete Python stdout equals the complete JSON.",
 "independent_audit":"The complete proof and code were sent to root and a_structure. No unreceived audit result is asserted at this author freeze."})
save("e_next_ordinary_dependencies.json",{
 "portable_rebuild":"python code/e_next_unit_characters.py --gp /absolute/path/to/gp",
 "retained_output_check":"python code/e_next_unit_characters.py",
 "PARI_version":"2.19.0","Python_dependencies":["sympy"],
 "working_directory":"Any; final routing is relative to the owned source.",
 "input_files":[{"path":"inputs/"+name,"sha256":digest} for name,digest in sorted(data["inputs"].items())],
 "input_regeneration":[
   "The complete E76 field/local/genus/ninth-genus/ninth-transfer/export pipeline regenerates the certified B1 BNF, both retained ray BIN objects and e106_e76_export.out.",
   "The full E101 five-stage pipeline regenerates e106_e101_coordinates.out.",
   "The full E94 six-stage pipeline regenerates e106_e94_comparison.json."],
 "full_binary_inputs_retained":True,
 "upper_radical_BNF_computation":False,"uncertified_discovery_BNF_input":False,
 "new_binary_output":False,
 "GP_stdout_guard":"Retain stack-allocation notices; reject top-level/user errors and require the exact completion marker."})
save("e_next_ordinary_computation_status.json",{
 "statement":"E.106",
 "author_full_rebuild":{
  "exit_code":0,"status":"PASS",
  "command":"python research_e106/code/e_next_unit_characters.py --gp research_e52/vendor/pari-2.19.0/gp > research_e106/code/e_next_unit_characters.out 2>&1",
  "actual_GP_output":"code/e_next_prime_maps.out",
  "actual_Python_output":"code/e_next_unit_characters.out",
  "finite_character_inputs":19683,"image_vectors":81,"preimages_per_image":243,
  "all_upper_class_coordinates":243,"all_lower_class_coordinates":81,
  "actual_prime_Frobenii":[7,73]},
 "initial_calculation":{
  "source":"code/history/initial_e_next_unit_characters.py",
  "stdout":"code/history/initial_e_next_unit_characters.out",
  "JSON":"code/history/initial_e_next_unit_characters.json",
  "status":"PASS; this initial calculation established rank4 before the complete map certificate."},
 "initial_GP_driver":{
  "source":"code/history/e106_initial_prime_driver.py",
  "retained_arithmetic_stream":"code/history/e106_initial_prime_driver_arithmetic.out",
  "provenance":(
   "The exploratory wrapper invoked the same GP source and printed its exit "
   "code and final1500 characters. The complete arithmetic stream is retained "
   "here from the successful rebuild; it is identified as the GP arithmetic "
   "stream, not invented as the wrapper's complete terminal stdout.")},
 "previous_long_BNF_jobs":{
  "status":"Both superseded jobs were interrupted on 2026-11-13 at16:42:07 UTC with actual exit130.",
  "session_ids":[24024,40565],"no_duplicates_started":True,
  "complete_status_and_actual_outputs":"E101 code/e101_history/superseded_bnf and ledger/e_unit_norm_complete_computation_status.json.",
  "conclusion":"No uncompleted BNF output or failed search is used as arithmetic evidence."}})
(LEDGER/"e_next_ordinary_refs.bib").write_text(
 "% verified: E106 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_PARICertifiedUnits; exact opened passages are in its source-evidence ledger. No duplicate entries.\n")
(LEDGER/"e_next_ordinary_report.md").write_text("""# E.106 — Complete third ordinary classes and actual norm maps

The actual ninth-symbol norm square evaluates the next six cubic local
characters on the COMPLETE ordinary-unit norm image from E.101. The
literal inclusion of Galois groups multiplies the exponent by three:
chi9(Nu) = 3 chi3(u) mod9. Each column of the full norm lattice has
the required divisibility. After the arithmetic row weights, the
resulting map has rank4. The certificate includes both finite
row/column changes and inverses, all19,683 source residues, all81
images and all243 preimages of each image.

## Class groups and exact maps

The proved trivial vertical class action lets the ambiguous formula
compute the entire ordinary three-class group: Cl(B3){3}=C9^2+C3.
The actual ninth-genus Artin quotient is an isomorphism, so E.91's
transvection vanishes. Its prime columns are now full class
coordinates. The six S-primes generate an order81 subgroup; the
exact integral kernel, index81, is given with its rational inverse.

The three primes above3 each have order3 and their product is
principal. Their horizontal norms prove that the original L3
prime above3 has order3. Thus Cl(L3){3}=C9+C3 and the finite
E.69 exponent a3 is1. Every vertical/horizontal ideal norm and
extension matrix in the square B3,B2,L3,L2 is evaluated.

The horizontal extension matrix is fixed by actual primes: the
fresh certified B1 ray calculation gives prime7 class (6,0,1)
and specified prime73 class (1,8,2). The actual h-trace and
coherent quotient J/P remove the possible lift ambiguity.
Every class is checked against jN, Nj and the actual h-trace.

## Ordinary-unit norms

The horizontal capitulation kernel is exactly the original order3
prime class. The unramified ideal/Herbrand map then proves that the
ordinary unit norm B3 to L3 is onto.

For B3/B2 the ordinary field-unit norm index is81. The further
choice-independent Hilbert90 divisor obstruction is the actual
quotient A9/R3=C3, extracted by the first coordinate modulo3.
This gives the complete two-step norm test, total ordinary norm
quotient C3^5, and completed norm-one kernel C3+Z3^54.
The L3/L2 quotient is C3^3, with kernel C3+Z3^18.
Every nonempty completed fiber is a coset of the actual kernel.

## Reproduction and scope

From this directory run:

    python code/e_next_unit_characters.py --gp /absolute/path/to/gp

The final program uses relative paths, copies the complete PARI
inputs to a fresh temporary directory, calls bnfcertify with
default flag0 and checks return1, and computes both prime Frobenii.
It then verifies the complete matrix/class certificate. No upper
radical BNF is used. The superseded original jobs have actual
exit130; their complete source/output remains in E101.

The theorem closes the third finite projection and its transvection.
It does not assign the eventual coherent exponent h or later
ordinary prime orders. The norm systems map to H through
E46/E69/E72/E88; no full intrinsic section lift is inferred.
""")
(ROOT/"code/history/README.md").write_text("""# Retained E106 exploratory work

The initial rank calculation and its actual stdout/JSON preceded
the full transformations and class maps. Its original workspace
path routing is retained literally.

The initial prime-wrapper source is retained. It ran the owned GP
calculation and printed the exit code and a truncated tail.
The arithmetic.out file is explicitly the complete actual GP
stream retained from the successful rebuild, rather than an
invented complete wrapper terminal transcript. The final portable
driver retains and checks the full GP stream directly.
""")

manifest={"statement":"E.106","files":[]}
excluded={"ledger/e_next_ordinary_manifest.json","code/e_next_ordinary_freeze.out"}
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    rel=path.relative_to(ROOT).as_posix()
    if rel in excluded:
        continue
    manifest["files"].append({"path":rel,"bytes":path.stat().st_size,"sha256":sha(path)})
save("e_next_ordinary_manifest.json",manifest)
print(json.dumps({
 "statement":"E.106","status":"AUTHOR_FREEZE_PASS",
 "file_count":len(manifest["files"]),
 "section_sha256":sha(proof),"program_sha256":sha(code),
 "GP_source_sha256":sha(ROOT/"code/e_next_prime_maps.gp"),
 "summary_sha256":sha(summary),
 "manifest_sha256":sha(LEDGER/"e_next_ordinary_manifest.json"),
 "complete_ordinary_groups":{"B3":[9,9,3],"L3":[9,3]},
 "finite_projection_exponent_a3":1,"eventual_h":"unevaluated"
},indent=2))
