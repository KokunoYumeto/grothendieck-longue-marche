"""Freeze the completely proved and independently audited E98 result."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent;ROOT=STAGE.parent;LEDGER=STAGE/'ledger'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
def save(name,data):
    (LEDGER/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
section=STAGE/'sections/E_split7_complete.tex'
assert sha(section)=='0e182d511154b61cad06cbc41c95a1cf0011f5780a72da5312f6c42f413701f9'
root=read(ROOT/'root_e98_audit/comparison.json')
peer=read(ROOT/'bc_e98_full_audit/audit.json')
assert root['status']=='PASS' and peer['status'].startswith('PASS')
assert all(x['byte_equal'] for x in root['complete_byte_comparisons'])
assert root['comparison_exclusions']==[]
final=read(HERE/'e_global_split7_normal_forms.json')
assert final['status']=='PASS' and final['relative_image_size']==73
assert final['negative_layer_ranks'][3]['comparison_fibre_negative_rank']==504
programs=['e_global_split7_explore','e_global_split7_residues','e_global_split7_central','e_global_split7_normal_forms']
for name in programs:
    assert read(HERE/(name+'.json'))['status']=='PASS'
    assert (HERE/(name+'.out')).stat().st_size
summary=('The complete global section spaces unramified outside{3,7} for the actual cubic geometric pro-three group, its intrinsic metabelian quotient and its class-two quotient. '
 'The full class-two abelian image is the union of nine cusp rays modulo9 with the exact horizontal criterion r(U-k_D) in(T-I)V+Z3 e_D. '
 'All nine quotient maps have C3^5+C9^2, with explicit Smith inverses. The universal inertia lattice is9W. '
 'Every fixed-abelian fibre is Z3^25+C3^9+C9^5, and every fixed-inertia fibre is Z3^31+C3^(9+t)+C9^5, with t3 on3W and0 otherwise. '
 'All full and metabelian ramified classes have literal cusp packet coordinates(D,r,b,[g]), with r nonzero, b in{0,1,2}, and[g] in H^J\H. '
 'Explicit anti-fixed Hall/Chen coordinates evaluate the latter quotient in every degree. The actual full→metabelian map is onto on ramified classes with every fibre(R^J\R), R=N'', and exact product ranks beginning504 in degree4. '
 'An explicit global class-two section with inertia9(eA0+eB0) has no metabelian or full lift.')
save('e_split7_complete_results.json',[{'id':'E.98','status':'Proved','statement':summary,
 'where_proved':'sections/E_split7_complete.tex, E98.1–E98.31 and complete proof; all four executed e_global_split7 programs and full certificates.',
 'depends_on':['E.34','E.37','E.40','E.41','E.49','E.56','E.61','E.66','E.71','E.78','E.87','E.95','E_WingbergRiemann'],
 'manuscript_passages':['Section51.16, folios733v–736v, scans172–178, formulas371–379; Part E(c),(d) and follow-up4.'],
 'depends_on_doubtful_reading':False,
 'notes':['Complete source/proof and all four program sources independently reviewed by B, with no correction requested.',
          'Root fresh copied-source/input reconstruction reproduces every complete JSON and stdout byte for byte; no exclusions.',
          'Peer independently reran the complete central and normal-form programs with byte-identical results, and separately checked all73 ray witnesses and exact set equality.',
          'The actual arithmetic action, all root/path choices, every geometric gauge and all infinite-product inverse maps are retained.',
          'The initial interrupted generic central-stage calculation and all its actual progress output are preserved with exact provenance. The final reduced-domain central proof uses a full44-by44 inverse and explicit fixed-eigenspace basis.',
          'This evaluates the full stated{3,7} ramification locus. Unrestricted ramification, the remaining wild/global higher and mixed targets, and the quartic retain their E23 scope.'],
 'independent_audit':{'status':'PASS','root_full_four_stage_rebuild':'root_e98_audit/comparison.json',
                     'peer_full_proof':'bc_e98_full_audit/audit.md','initial_independent_source_and_witness_audit':'bc_e98_audit/audit.md'},
 'computation':{'program_order':programs,'relative_residues':73,'first_digits_tested':6561,
                'second_digits_per_admissible_first':6561,'local_quotients':9,'central_inverse_round_trips':40,
                'negative_rank_rows':14,'degree4_fibre_rank':504}}])
save('e_split7_complete_coverage_notes.json',{'statement':'E.98','tasks':['E.c','E.d','E.follow-up-4'],
 'completed':summary,'remaining':['Unrestricted coupled global ramification.','Other-primary or mixed sources and the quartic curve.','The remaining wild higher-stage and arithmetic norm targets in E23.']})
save('e_split7_complete_source_evidence.json',{
 'status':'verified complete proof with exact comparison maps',
 'primary_source':{'key':'E_WingbergRiemann','url':'https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Riemann-kpi1.pdf',
   'root_open_refs':['turn824view0','turn825view1','turn825view2'],
   'peer_open_refs':['turn813view0','turn814view0','turn815view0'],
   'checked':'Continuous bundle and Lemma1.1, printed4–5; Theorem2.4 and full proof, printed13–15; K(pi,1) criterion and infinite-set clause. Root read the full displayed theorem proof; peer separately checked the remark after Proposition2.1.',
   'application':'S contains the places over3; the cyclotomic tower makes both7-adic unramified completions nontrivial. Actual inertia inclusions give the kernel maps; the two independent marked Frobenii give the free quotient basis and actual reverse map.'},
 'internal_exact_maps':['E56 actual split-prime arithmetic presentation and its reverse generator map.',
   'E95 actual cusp cochains and full marking transport.',
   'E61/E66 full local classification for every nonzero exponent and metabelian zero-abelian-inertia exclusion.',
   'E41.13–15 completed Fox derivative, Koszul filtration equality, actual integral Chen basis and topology.',
   'E98 explicit P,Q,S primitive quotient, full inverse differential, nine lattice maps and central Smith inverses.',
   'E98 actual fixed-element lift h0(h0^-1Jh0)^(1/2), fibre map[k]→[kg0], and anti recursion u(uJu)^(-1/2).'],
 'scope_limits':['No numerical arithmetic G3 boundary value is inferred.','The unrestricted global E23 locus remains active.']})
(LEDGER/'e_split7_complete_refs.bib').write_text('% E.98 reuses the verified E_WingbergRiemann and the exact internal E.41/E.56/E.61/E.66 comparisons.\n')
report='''# E.98: complete split-seven source

## Exact result and maps

The actual arithmetic source is (D7 *_3 D7') semidirect C2, with both specified Frobenii and inertias. The actual inertia-bundle and quotient maps are proved inverse. Normalizing the value at complex conjugation leaves the exact pair equation u T(a) u^-1=a^7 modulo H^J.

The complete class-two abelian locus is the nine cusp lines modulo9W, with the exact additional horizontal criterion r(U-k_D) in(T-I)V+Z3e_D. Every one of the nine local lattice quotients is C3^5+C9^2, with full transformations and inverse maps. The relative set has73 residues. Its universal horizontal-admissibility lattice is exactly9W.

The primitive determinant-line quotient gives the44-by44 differential with Smith1^14,3^18,9^12. Its literal inverse gives every central inertia correction. The central fixed-gauge quotient has Smith1^7,3^9,9^5 and free rank24; the tame determinant line adds one free coordinate. Thus every fixed-abelian fibre is Z3^25 x C3^9 x C9^5. Every fixed-relative fibre is Z3^31 x C3^(9+t) x C9^5, where t=3 on3W and0 otherwise. The full geometric gauge retains the actual handle-action correction.

For the full and metabelian groups every nontrivial inertia has an actual cusp packet(D,r,b,[g]), where r is a nonzero three-adic integer, b is0,1,2 and[g] is the left fixed-group coset. The anti-fixed word g^-1J(g) has explicit inverse[x^-1/2]. Ordered Hall/Chen recursion u(uJ(u))^-1/2 computes every layer and every nonlinear carry. The exact full→metabelian map sends[g] to[gbar]; every fibre is(R^J\R), R=N'', with actual map[k] to[kg0]. Its complete product-coordinate ranks are the differences of the evaluated full and Chen negative ranks, beginning504 in degree4. The zero-inertia locus is the complete E41 locus.

The literal global inertia9(eA0+eB0) has an integral class-two correction but is outside all nine exact cusp lines. The actual local restriction and geometric quotient maps exclude every metabelian or full lift.

## Executed evidence

Run e_global_split7_explore.py, e_global_split7_residues.py, e_global_split7_central.py and e_global_split7_normal_forms.py in that order. Supply --source-code /absolute/path/to/archive/code to the first, third and fourth when using a copied staging directory. The second reads the adjacent first certificate. Dependencies are Python3, SymPy and NumPy; the exact local-Smith and row-kernel helpers are included.

All6561 first digits and all6561 second digits for each admissible first digit are exhausted. All73 actual witnesses are checked against the full rational inverse. All9 lattice Smith maps, all primitive wedge witnesses and every displayed inverse are retained. Forty central coordinate/conjugator round trips, the full nonlifting tame relation and fourteen exact character rows pass. Root rebuilt all four programs using copied immutable inputs: all eight complete JSON/stdout files are byte-identical, with no exclusions. The peer read the full675-line proof and all four programs, independently rebuilt both final programs byte for byte, and separately checked the73-element ray equality and all2190 original congruences.

The historical interrupted normal-form source/output is preserved in code/history at author staging, with its exact exit130/progress provenance. The final central program uses the explicit21-column fixed eigenspace and the complete44-by44 inverse to prove the rank, with every change-of-basis inverse checked. No final result is attributed to the interrupted attempt.

## Requested work still active

This result computes the complete stated{3,7} ramification locus. It does not end the unrestricted global, higher wild, quartic or other-primary and mixed-source requests. Those remain in E23 with their own actual maps and unfinished calculations.
'''
(LEDGER/'e_split7_complete_report.md').write_text(report)
all_files=[]
for folder in ['sections','ledger','code']:
    for p in sorted((STAGE/folder).rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts:continue
        if p.name in ['e_split7_complete_manifest.json','e_global_split7_freeze.out']:continue
        all_files.append({'path':str(p.relative_to(STAGE)),'sha256':sha(p),'bytes':p.stat().st_size})
save('e_split7_complete_manifest.json',{'statement':'E.98','status':'frozen after complete root and peer audit',
 'section_sha256':sha(section),'run_order':[n+'.py' for n in programs],
 'complete_root_comparison':'root_e98_audit/comparison.json','peer_full_review':'bc_e98_full_audit/audit.md',
 'files':all_files,'runtime_inputs':root['unchanged_input_hashes']})
print('PASS E98 frozen: complete proof, all4 exact programs, every output and both independent audits.',flush=True)
