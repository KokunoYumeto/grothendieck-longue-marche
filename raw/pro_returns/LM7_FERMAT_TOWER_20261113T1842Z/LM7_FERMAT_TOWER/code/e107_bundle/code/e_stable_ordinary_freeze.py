#!/usr/bin/env python3
"""Retain the all-level proof, finite certificate, maps and source record."""
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

proof=ROOT/"sections/E_stable_ordinary_phase.tex"
program=ROOT/"code/e_stable_ordinary_phase.py"
summary=ROOT/"code/e_stable_ordinary_phase.json"
d=json.loads(summary.read_text())
assert d["status"]=="PASS" and d["eventual_exponent_h"]==1
assert d["rank4_image_count"]==81
assert d["global_reciprocity_hyperplane_count"]==243
assert d["all_new_unit_character_vectors_with_sums_1_2"]==81
assert d["all_residue_character_products"]==82944
assert d["complete_mod9_cube_inputs"]==59049
assert d["accepted_mod9_cube_inputs"]==19683
assert d["fixed_toric_fiber_inverse_tests"]==59049
assert d["toric_inverse_coordinate_convention"]["raw_beta_exponent"]=="b=3*B17/2"
assert d["toric_inverse_coordinate_convention"]["raw_seventeen_norm_exponent"]=="2*b=3*B17"
assert summary.read_bytes()==(ROOT/"code/e_stable_ordinary_phase.out").read_bytes()
for name,digest in d["inputs"].items():
    assert sha(ROOT/"inputs"/name)==digest
tex=proof.read_text()
assert [int(n) for n in re.findall(r"\\tag\{E107\.(\d+)\}",tex)]==list(range(1,25))
assert len(re.findall(r"(?m)^\\\[$",tex))==len(re.findall(r"(?m)^\\\]$",tex))==24
assert not any(ord(c)<32 and c not in "\n\t" for c in tex)

save("e_stable_ordinary_results.json",[{
 "id":"E.107","status":"Proved",
 "statement":(
 "The actual E101 ordinary unit eta and E106 horizontal ordinary-unit norm "
 "surjection supply the fifth local character, with exact triple sums(1,2). "
 "The cyclic-nine Artin norm/inclusion square preserves the characters under "
 "every later inclusion. Thus the six-character image is the full reciprocity "
 "hyperplane at every B step from level3. All ordinary B class norms fromB3 "
 "and L class norms fromL2 are isomorphisms, with the specified norm/extension "
 "matrices and principal S-lattice; every distinguished original three-prime "
 "class has order3. The actual eventual coherent three-unit exponent is h=1. "
 "A coherent tuple of base lambda^3 normalizes the entire complex divisor "
 "phase to -sum ell_p*t_p/3, with exact forward/inverse maps and choice "
 "ambiguity. For first class kappa17 and pure positional component1, the "
 "complete scaled toric image and every fiber are evaluated."),
 "where_proved":(
 "sections/E_stable_ordinary_phase.tex, E107.1--24 and complete proof; "
 "code/e_stable_ordinary_phase.py/.out/.json and the retained immutable "
 "E106/E88 input certificates."),
 "depends_on":["E.46","E.69","E.72","E.86","E.88","E.91","E.101","E.106",
               "E_MilneCFT","E_LemmermeyerAmbiguous"],
 "manuscript_passages":[
 "LM section51.16, folios733v--736v, scans172--178, through the actual positional norm maps and scaled toric comparison E46/E69/E72/E88."],
 "depends_on_doubtful_reading":False,
 "notes":(
 "The fifth vector is obtained from an ACTUAL ordinary unit norm preimage; "
 "its coordinate normalization is performed through E106's actual image "
 "inverse. The all-level proof uses the norm square and induction, not "
 "extrapolation from finite computations. Compatible lambda^3 lifts are "
 "proved by compact finite intersection with the actual norm maps. The "
 "restricted divisor module is explicitly prodiscrete and is not declared "
 "compact. The complex factor and its H fibers are complete in the stated "
 "pure-component1 locus; no full intrinsic lift or separate pure-factor "
 "norm evaluation is inferred.")
}])
save("e_stable_ordinary_coverage.json",{
 "statement":"E.107",
 "addresses":[{
  "task":"Part E(c),(d), Item2/Lead3 through the actual H positional quotient",
  "status":"Complete all-level ordinary-class stability, coherent exponent, complex phase and specified toric fibers",
  "exact_maps":(
   "Cyclic-nine local Artin norm/inclusion square; split-prime product norms "
   "with both triple sums; ordinary Hilbert class-field norm and extension "
   "maps; named prime norms; coherent lambda^3 tuple and compact inverse "
   "fiber; restricted divisor map; exact phase correction and Kummer-Shapiro "
   "total-norm cube condition.")}],
 "closed_previous_steps":[
  "E69's eventual coherent exponent h is exactly1.",
  "All later ordinary B and original L distinguished-prime orders are evaluated.",
  "All later ordinary class norm/extension maps and principal S-divisor lattices stabilize in actual coordinates.",
  "E88's formerly unevaluated phase modulo3^h is fully evaluated and admits the stated exact linear normalization.",
  "Every toric fiber in the complete complex positional factor with pure component1 is explicitly the evaluated coherent kernel."],
 "remaining":[
  "The separate pure-field positional norm factor for the kappa17 line, and its combination with the complex factor in the whole H section set.",
  "The remaining intrinsic/metabelian and marked-depth lifting/classification questions recorded in E23.",
  "No numerical fundamental-unit bases for every individual higher coherent image I_d are asserted; the explicit recursive maps and free product coordinates are those already proved in E69."]})
save("e_stable_ordinary_source_evidence.json",{
 "statement":"E.107",
 "sources":[
  {
   "key":"E_MilneCFT",
   "url":"https://www.jmilne.org/math/CourseNotes/CFT.pdf",
   "freshly_opened":[
    "III Theorem3.1 and the complete restriction/corestriction cup-product proof, turn886view0, lines6217--6297.",
    "V Proposition3.3 and full ideal-norm/Frobenius proof, turn886view2; Theorem3.6 and Example3.9, turn887view0.",
    "VII Proposition3.1 and its full unit-Herbrand lattice proof, turn888view0--1, lines12803--12908.",
    "VIII Theorem3.1 and full cyclic Hasse norm proof, turn886view1.",
    "VIII Theorem7.4 and complete proof through line16289, turn887view1--2."],
   "usage":(
    "Exact local norm/inclusion square, complete field-norm character kernel, "
    "actual ideal norm surjectivity via the Hilbert class field, ordinary-unit "
    "Herbrand quotient and norm-fiber exactness."),
   "source_precision":(
    "The local square follows from III Theorem3.1's proved Res/Cor "
    "compatibility. III Lemma3.2 itself prints 'Proof. To be added'; no "
    "complete printed proof of that lemma is claimed.")
  },
  {
   "key":"E_LemmermeyerAmbiguous",
   "url":"https://arxiv.org/pdf/1309.1071",
   "freshly_opened":[
    "Theorem1 and Proposition1 with the full ideal Hilbert90 proof, turn884view1.",
    "Complete invariant-ideal and unit-Herbrand derivation through the end of section3, turn885view2 and turn886view3."],
   "usage":(
    "The ambiguous class order using the unit FIELD-norm index; the actual "
    "strongly ambiguous divisor quotient giving the extra ordinary-unit defect."),
   "source_precision":(
    "The Proposition1 surjectivity paragraph has the already recorded "
    "Am_st/Am typographical slip. The tower proof uses its explicit "
    "orbitwise ideal Hilbert90 map. The unit Herbrand assertion is separately "
    "supported by Milne's full proved VII Proposition3.1 above.")
  }],
 "internal_exact_inputs":[
  "E101's actual ordinary eta with norm zeta*epsilon and residue eta^96=zeta.",
  "E106's COMPLETE rank4 arithmetic character map and exact surjection N_B3/L3 on ordinary units.",
  "E91's full trivial vertical B class action and exact original class-group type.",
  "E69's recursive coherent-unit kernel coordinates; E72's prime-order/norm-valuation equality.",
  "E88's complete actual divisor sequence, retained degree-six class map and phase modulo3."],
 "author_certificate":"PASS, with all finite outputs retained and no omitted fields.",
 "independent_audit":"Complete proof and source were sent to root and a_structure; no unreceived audit result is asserted at author freeze."})
save("e_stable_ordinary_dependencies.json",{
 "portable_rebuild":"python code/e_stable_ordinary_phase.py",
 "Python_dependencies":["sympy"],
 "working_directory":"Any; all input routing is relative to the source.",
 "immutable_inputs":[{"path":"inputs/"+n,"sha256":h} for n,h in sorted(d["inputs"].items())],
 "input_regeneration":[
  "E106's full certified prime and finite class-map certificate.",
  "E88's full degree-six prime-class/divisor program and complete79-prime output."],
 "new_GP_or_BNF_computation":False,
 "old_BNF_status":"The superseded original sessions24024/40565 were already stopped with actual exit130; E101 retains all statuses and output. No duplicate job was started."})
save("e_stable_ordinary_computation_status.json",{
 "statement":"E.107","status":"PASS","actual_exit_code":0,
 "source":"code/e_stable_ordinary_phase.py",
 "actual_stdout":"code/e_stable_ordinary_phase.out",
 "complete_JSON":"code/e_stable_ordinary_phase.json",
 "rank4_vectors":81,"all_fifth_vectors":81,
 "reciprocity_hyperplane_vectors":243,
 "residue_unit_products":82944,
 "stable_B_classes":243,
 "phase_prime_basis_size":79,
 "phase_forward_inverse_tests":257,
 "complete_mod9_cube_inputs":59049,
 "accepted_mod9_cube_inputs":19683,
 "fixed_toric_fiber_inverse_tests":59049,
 "proof_vs_computation":"All-level persistence, ordinary class stability, coherent compatibility and phase normalization are proved algebraically. Finite computations certify the stated finite maps and arithmetic calibrations; they are not a numerical extrapolation."})
save("e_stable_ordinary_toric_test_amendment.json",{
 "statement":"E.107",
 "requested_by":"root full-proof/program audit",
 "correction":(
  "The original finite inverse test used b=B17/2, the divided beta parameter, "
  "whereas the displayed theorem uses the raw beta exponent b=3*B17/2. "
  "The test now checks that literal raw exponent and both equalities "
  "2*b/3=B17 and 2*b=3*B17. The theorem's proof and maps did not change."),
 "original_frozen_material":"ledger/e107_original_author_freeze/",
 "original_program_sha256":sha(LEDGER/"e107_original_author_freeze/e_stable_ordinary_phase.py"),
 "corrected_program_sha256":sha(program),
 "original_summary_sha256":sha(LEDGER/"e107_original_author_freeze/e_stable_ordinary_phase.json"),
 "corrected_summary_sha256":sha(summary),
 "proof_sha256_unchanged":sha(proof),
 "fresh_corrected_execution":"PASS; complete actual stdout and JSON retained."
})
(LEDGER/"e_stable_ordinary_refs.bib").write_text(
 "% verified: E107 reuses E_MilneCFT and E_LemmermeyerAmbiguous; all exact freshly opened passages are recorded in its source-evidence ledger. No duplicate entries.\n")
(LEDGER/"e_stable_ordinary_report.md").write_text("""# E.107 — The exact stable exponent and complex positional fibers

The eventual coherent three-unit exponent is h=1. The proof does
not extrapolate a stable finite class number: it constructs the
missing fifth local character and proves that this character
persists under every later inclusion.

## The fifth actual character

E106 evaluates the complete six-character image on ordinary B2
units. It has dimension4 and both three-prime sums vanish.
The actual ordinary unit eta from E101 has residue eta^96=zeta,
so its arithmetic tame character at17 is2 and global reciprocity
gives character1 at3. E106's horizontal ordinary-unit norm is
onto; an actual preimage v in B3 therefore has triple sums(1,2).
This is the fifth independent direction. The cyclic-nine Artin
norm square proves exact equality of the character on every
included unit at consecutive stages. Global reciprocity bounds
the image by the five-dimensional hyperplane, so the image is
exactly that hyperplane at all stages fromB3.

## All-level ordinary classes and principal divisors

The complete local field-norm index is3^5. Since E91 proves the
vertical action on the entire B class group is trivial, the
ambiguous formula fixes every later class number at243.
Ordinary class norms are onto by the actual Hilbert-class-field
intersection/Frobenius map, hence are isomorphisms. The six named
prime classes, the full principal S-lattice and all horizontal
norm/extension matrices are transported by those exact maps.
Each original L prime above3 consequently has order3.

Thus the B groups are C9^2+C3 from level3, the L groups C9+C3
from level2, with actual vertical maps N=I and j=3I in the
specified coordinates. The horizontal ordinary unit norms stay
onto. The ordinary vertical unit norm quotients are C3^6 overB
and C3^3 overL in the stated ranges, with the complete local
plus ideal-divisor tests given in the theorem.

## Coherent tuple and phase

The exact finite prime order makes every finite norm image in
the base three-units equal lambda^(3Z3). Compact finite
intersection with the actual adjacent norm maps supplies a
coherent tuple e with e0=lambda^3. Conversely every coherent
tuple lies in each finite image. This proves h=1 in both
directions and gives the explicit decomposition into e^z and
the exact kernel of the base projection.

For the E88 restricted divisor kernel K, the remaining phase
can now be normalized exactly to

    Theta_*(t) = -sum_p ell_p*t_p / 3.

The numerator is integral by the first class congruence.
Starting from any actual splitting s, multiply by
e^((Theta_*-Theta)/3). This is a continuous coherent map,
preserves outside divisors and the seventeen valuation, and
has the required phase. Splittings with the same phase differ
by precisely a continuous homomorphism K to the base-zero
coherent three-unit kernel.

## Complete fixed-pair fibers in the complex H component

For first class kappa17 and pure positional component1, the
second toric class may have arbitrary coefficients B17,B3
at17,3 and restricted coefficients r_p at the eligible complex
primes, subject exactly to sum c_p*r_p=0 mod3. Its entire
fiber is the evaluated compact kernel
product over d>=0 of Z3^(2*3^d).
The theorem gives the actual product map and inverse:

    x = beta^(3B17/2) e^(B3+sum ell_p*r_p/3) k s_*(3r).

The separate pure-field positional factor and the intrinsic
lifting questions are not inferred from this quotient result.

## Reproduction

    python code/e_stable_ordinary_phase.py

The source uses only SymPy and the three retained immutable
E106/E88 inputs. Every output is retained, with full finite
coordinate inverses. It exhausts all81 fifth-vector possibilities,
82,944 residue character products, the79-prime phase basis,
59,049 cube inputs and59,049 fixed-pair inverse checks.
No new BNF computation is used.
""")

manifest={"statement":"E.107","files":[]}
excluded={"ledger/e_stable_ordinary_manifest.json","code/e_stable_ordinary_freeze.out"}
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    rel=path.relative_to(ROOT).as_posix()
    if rel in excluded:
        continue
    manifest["files"].append({"path":rel,"bytes":path.stat().st_size,"sha256":sha(path)})
save("e_stable_ordinary_manifest.json",manifest)
print(json.dumps({
 "statement":"E.107","status":"AUTHOR_FREEZE_PASS",
 "file_count":len(manifest["files"]),
 "section_sha256":sha(proof),"program_sha256":sha(program),
 "summary_sha256":sha(summary),
 "manifest_sha256":sha(LEDGER/"e_stable_ordinary_manifest.json"),
 "eventual_h":1,
 "complete_complex_phase":"-sum ell_p*t_p/3 on the actual divisor kernel",
 "fixed_toric_fiber":"product_d>=0 Z3^(2*3^d)"
},indent=2))
