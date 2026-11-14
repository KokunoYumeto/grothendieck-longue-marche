"""Freeze the proved E93 calculation and its actual source evidence."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/'research_e93'
BASE=ROOT/'LM7_FERMAT_TOWER'
ledger=HERE/'ledger';ledger.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
certificate=json.loads((HERE/'code/e_global_central_localization.json').read_text())
assert certificate['status']=='PASS'
for row in certificate['inputs'].values():
    assert sha(BASE/'code'/row['name'])==row['sha256'],row['name']

rows=[{
 'id':'E.93','status':'Proved',
 'statement':'The entire global central localization map for the intrinsic cubic class-two quotient has image Z3^25 plus C3^9 plus C9^5, kernel the restricted prime-exponent module outside {2,3}, and cokernel Z3^21. Its literal marked restriction, continuous section and every fibre are evaluated. The actual joint coefficient map kills every ramified Tate-line cocycle and has precisely the horizontal rho image, with full restricted-prime and finite-Smith kernel. These maps act on every actual nonempty global class-two section fibre with no further stabilizer quotient.',
 'where_proved':'sections/E_global_central_localization.tex, E93.1--15 and full proof; code/e_global_central_localization.py/.out/.json, including every basis transport, integral quotient and inverse matrix.',
 'depends_on':['E.36','E.37','E.74','E.75','E.85','E.90'],
 'manuscript_passages':['LM section51.12, folios717--718, scans136--138; section51.15, folios725--727, scans156--160; section51.16, folio734v, scan174; actual central and quotient maps as in E.37,E.85.'],
 'depends_on_doubtful_reading':False,
 'notes':'The actual marking constants b and alpha are retained symbolically, with alpha a unit. The primitive Tate vector is transported from exterior to Hall coordinates. Its horizontal free coordinates have exact common three-divisibility and are not replaced by a primitive horizontal basis vector. The numerical joint origin for each global abelian input and higher nonabelian lifts remain active.'
}]
(ledger/'e_global_central_localization_results.json').write_text(json.dumps(rows,indent=2)+'\n')
evidence=[]
for key,name,passages in [
 ('E37_internal','E_intrinsic_class2.tex','E37.20 and its full proof of the actual global residue map, primitive integral Tate line, uniformly convergent Kummer splitting, and evaluation of the unramified summand; full section-fibre comparison.'),
 ('E74_internal','E_wild_local_layers.tex','Actual local-to-global marked quotient and the vanishing local invariant group.'),
 ('E75_internal','E_wild_relation_module.tex','Actual local coefficient cohomology, saturated rank22 relative kernel, complete matrix inverse.'),
 ('E85_internal','E_compatible_joint_fibre.tex','E85.10--18 and full coefficient/fibre proof: F2, exact image lattice, complete target geometric conjugacy, rho section, all Smith and relative inverse coordinates.'),
 ('E90_internal','E_relative_multiples.tex','Actual marked Kummer basis (kappa3,kappa4), b and alpha, complete restricted prime topology and literal global-to-local logarithmic formula.')
]:
 p=BASE/'sections'/name
 evidence.append({'key':key,'verified':True,'path':str(p.relative_to(ROOT)),'sha256':sha(p),'passages':passages,'scope':'Actual integrated proof and specified maps read. The new central restriction and joint-kernel assertions are proved in E93.'})
evidence.append({'key':'E93_executed_certificate','verified':True,'path':'research_e93/code/e_global_central_localization.json','sha256':sha(HERE/'code/e_global_central_localization.json'),'checks':'All five inputs hash-verified; full exterior/Hall arithmetic intertwiners, primitive relative quotient and inverse, horizontal Smith maps, literal joint zero Tate vector and rho kernel, symbolic marking inverse, 1134 finite-precision localization identities, 1458 full coordinate round trips.','scope':'Finite computations accompany the complete integral proof; no numerical value is assigned to b or alpha.'})
(ledger/'e_global_central_localization_source_evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
coverage={
 'statement':'E.93','tasks':['E.c','E.d','E.follow-up-4'],
 'state':'Exact central localization and every central variation fibre over the already evaluated global class-two image.',
 'remaining':'Evaluate the particular joint origin for every global abelian input; evaluate higher wild/nonabelian lifts and the remaining positional norm exponents, phases and other-primary comparisons.'
}
(ledger/'e_global_central_localization_coverage_notes.json').write_text(json.dumps(coverage,indent=2)+'\n')
report='''# E.93: exact global central localization

The actual restriction of global central cocycles is
`(z,a) -> (z+b*L(a)*[w], alpha*L(a)*w)`, where `L(a)` is the convergent logarithmic prime sum and the genuine marked Kummer constants remain symbolic. Its entire image is `Z3^25 + C3^9 + C9^5`, its kernel is the restricted prime-exponent module outside `{2,3}`, and its cokernel is `Z3^21`.

The proof gives continuous additive sections, all kernel coordinates, and an explicit rank21 quotient map with an integral inverse. The exterior-to-Hall signed permutation is checked against both actual arithmetic operators before using the primitive Tate vector. The horizontal class retains its exact Smith coordinates and three-divisibility.

The genuine joint coefficient map sends the Tate vector to zero. Thus every ramified central Kummer cocycle has literally zero joint image. The global composite has only the horizontal rho coordinate, with full kernel `restricted primes outside3 + Z3^23 + C3^9 + C9^5`. All finite cyclic coordinates and all inverse free coordinates are retained. Vanishing of the actual source and target abelian invariant groups transfers these maps to every nonempty global section fibre without a further stabilizer quotient.

The independent program completed with all matrix identities, 1134 finite-precision localization checks and 1458 full coordinate inverses passing. The text proves the full integral assertions, including continuity and the exact choice-of-origin translation. No numerical joint origin is asserted for an arbitrary global abelian input. E.23 remains active at those particular origins and at higher nonabelian layers.

## Retained files and rerun

Run `python code/e_global_central_localization.py --source-code ../LM7_FERMAT_TOWER/code` from `research_e93`, or run the same program without arguments from the final common `code/` directory. SymPy is required. The certificate records every input hash. This freeze has not yet been assigned an independent peer audit.
'''
(ledger/'e_global_central_localization_report.md').write_text(report)
files=[]
for folder in ['sections','code','ledger']:
 for p in sorted((HERE/folder).iterdir()):
  if p.is_file() and p.name not in ['e_global_central_localization_manifest.json','e_global_central_freeze.out']:
   files.append({'path':str(p.relative_to(HERE)),'sha256':sha(p),'bytes':p.stat().st_size})
manifest={'statement':'E.93','status':'frozen for independent audit','files':files,'input_files':certificate['inputs'],'self_exclusions':['ledger/e_global_central_localization_manifest.json','code/e_global_central_freeze.out']}
(ledger/'e_global_central_localization_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'statement':'E.93','status':'PASS','files':len(files),'TeX_sha256':sha(HERE/'sections/E_global_central_localization.tex'),'program_sha256':sha(HERE/'code/e_global_central_localization.py'),'certificate_sha256':sha(HERE/'code/e_global_central_localization.json')},indent=2))
