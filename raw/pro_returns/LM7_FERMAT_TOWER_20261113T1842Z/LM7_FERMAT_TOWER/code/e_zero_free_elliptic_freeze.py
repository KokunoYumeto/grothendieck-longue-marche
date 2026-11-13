#!/usr/bin/env python3
"""Record the actually executed E96 computation, proof and exact scope."""
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
LEDGER=BASE/'ledger'
CODE=BASE/'code'
PREFIX='e_zero_free_elliptic'
dump=lambda p,x:p.write_text(json.dumps(x,indent=2)+'\n')
result=json.loads((CODE/'e_global_zero_free_elliptic.json').read_text())
assert result['status']=='PASS'
assert result['exact_matrix_comparisons']==72 and result['finite_inertia_cases']==59049
section=BASE/'sections/E_zero_free_elliptic_obstruction.tex'
assert section.exists() and '^{44}quad' not in section.read_text()
summary=(
 'On the full global cubic b=0 slice, the actual intrinsic pro-three class-two '
 'obstruction is evaluated by an explicit integral 44-coordinate polynomial '
 'numerator N and correction -N/(3(q-1)). The exact global image retains every '
 'local divisibility and restricted-convergence exponent. The image on all '
 'modulo-three good-prime inertia residues is exactly one rational cusp ray '
 'on each finite elliptic stratum, attained by actual rational tangential '
 'sections. Every nonempty class-two fibre is the already evaluated full '
 'central cohomology torsor.'
)
dump(LEDGER/(PREFIX+'_results.json'),[{
 'id':'E.96','status':'Proved','statement':summary,
 'where_proved':'sections/E_zero_free_elliptic_obstruction.tex, E96.1--20 and full proof; code/e_global_zero_free_elliptic.py/.out/.json, including the exact primitive quotient, all polynomial rows, finite inertia classification and actual norm-seven witnesses.',
 'depends_on':['E.36','E.37','E.92','E.93','E.95'],
 'manuscript_passages':['section51.16; folios733v--736v; scans172--178; formulas371--379; Part E(c),(d), follow-up4'],
 'depends_on_doubtful_reading':False,
 'notes':'The phase-zero formula uses the full actual E95 marking transport. The slice has zero free compact elliptic coordinate; the finite elliptic carry is retained. Q subtracts the pivot multiple of w before deleting that coordinate. Actual arithmetic Kummer values remain in the fixed source marking. Formal finite matrix samples are not asserted to be new Frobenius evaluations. The nonzero free elliptic slice, higher geometric quotients, quartic curve and full profinite classification remain active.'
}])
dump(LEDGER/(PREFIX+'_coverage_notes.json'),{
 'statement':'E.96','tasks':['E.c','E.d','E.follow-up-4'],
 'state':summary,
 'remaining':'Evaluate the free proper-elliptic Frobenius coordinate and all higher nonabelian images, actual joint origins, other-primary and mixed sources, the quartic curve and the retained norm-phase questions.'
})
dump(LEDGER/(PREFIX+'_source_evidence.json'),{
 'statement':'E.96',
 'internal_inputs':[
  {'statement':'E.37','scope':'Entire statement and proof reread, including the integral quotient M/Z3w, peripheral sign, actual local extension equation, continuous localization, restricted convergence and full central fibres.'},
  {'statement':'E.92','scope':'Actual compact projection, global Kummer coordinates, finite elliptic carry and the fixed-column cochain identity.'},
  {'statement':'E.95','scope':'Entire working path derivation and complete exact program read; the actual marked scalar basis change, lifted free-group automorphism, eight framed-point cochains and proper projections are used. Exact input hash retained.'},
  {'statement':'E.93','scope':'Exact action of central localization on every nonempty class-two fibre.'}
 ],
 'new_external_theorem_used':False,
 'root_execution':{'status':'PASS','formal_full_inverse_comparisons':72,'finite_inertia_cases':59049,'actual_norm7_counterexample_nonintegral_coordinates':36,'actual_rational_cusp_witnesses':['A0','B0']},
 'peer_audit':'B/C read the complete E37 proof, E95 path derivation, exact coefficient program and the complete E96 proof. Its separate symbolic certificate verifies the universal identities and actual quotient lattice. Two missing TeX backslashes reported by the peer were corrected before this freeze. Final peer files are retained separately.'
})
report='''# E96: global zero-free-elliptic slice

The full actual b=0 slice of H1(Q,V) is parametrized by the finite elliptic
residue epsilon and the complete toric Kummer class beta, with E92's finite
carry. E95's actual framed-path cochains allow the local correction in E37
to be written as -N/[3(q-1)], with N an explicit integral44-column. The
elliptic Frobenius scalar cancels through the proved mixed-wedge identity.
The criterion retains the exact exponent v3(q-1)+1 and the additional m
in the restricted-convergence condition. For toric valuations of finite
support it is a finite list of explicit congruences.

The primitive quotient is the actual map Q(m)=(m-m_p w)_(i!=p), with an
integral section. In particular its first row retains the -9 pivot term.
The determinant-nine comparison with M0 is not discarded.

The first mixed congruences have an exact global image: modulo-three
inertia lies on the O, A0 or B0 cusp ray according to epsilon=0,1,2.
Every finite family of rational-prime residues on that ray is attained
by an actual rational tangential section twisted by a rational Kummer
class. Conjugate K-primes inherit the exact same rational valuation and
the actual cusp permutation. The pure toric kappa(7)eA0 class fails;
the actual A0 and B0 norm-seven tangent twists have zero correction.

The executed program exports all44 polynomial rows (569 terms), the full
quotient and section, every rational coefficient and input hash. It
compares72 complete corrections to the original rational44x44 inverse,
enumerates59049 finite inertia/pivot cases, and verifies the marked
norm-seven witnesses. The additional matrix samples are algebraic
identities; they do not assign arbitrary values to arithmetic Frobenii.

The peer independently checked80 universal mixed-wedge identities,
eight universal numerator identities,352 coefficient-integrality
checks and eight actual norm-seven quotient equations. It then read
the entire proof and checked the global image, marking, finite carry,
both criterion directions and rational-prime attainment.

This is an evaluated slice of the requested section problem. The
nonzero free proper-elliptic coordinate, particular joint origins,
higher geometric quotients, quartic case and other-primary or mixed
comparisons remain active. No item of E23 is closed by this refinement.
'''
(LEDGER/(PREFIX+'_report.md')).write_text(report)
(LEDGER/(PREFIX+'_refs.bib')).write_text('% E96 uses the actual internal comparisons E37, E92, E93 and E95; no new external bibliography key.\n')
members=[]
for folder in ['sections','code','inputs','ledger']:
 for p in sorted((BASE/folder).glob('*')):
  if not p.is_file() or p.name==PREFIX+'_manifest.json' or p.name==PREFIX+'_freeze.out':continue
  members.append({'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
dump(LEDGER/(PREFIX+'_manifest.json'),{
 'status':'frozen_for_integration_and_peer_hash_check','statement':'E.96',
 'files':members,'exclusions':['The manifest itself and the actual freeze stdout, which is written after this manifest.'],
 'source_input_hashes':result['input_sha256'],
 'scope':'Exact b=0 global slice and its exact mod3 inertia image. No full E23 completion is claimed.'})
print('PASS E96 proof, actual computation, exact scope, source evidence and full manifest recorded.')
print('Statements:1; exact numerator rows:44; terms:569; full inverse comparisons:72; finite inertia cases:59049.')
print('Proof SHA256:',hashlib.sha256(section.read_bytes()).hexdigest())
