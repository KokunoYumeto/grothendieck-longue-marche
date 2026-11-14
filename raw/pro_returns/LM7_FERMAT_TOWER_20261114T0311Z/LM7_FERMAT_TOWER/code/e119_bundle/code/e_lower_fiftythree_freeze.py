#!/usr/bin/env python3
"""Freeze E119's proof, exact certificates, actual failures and preview."""
from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]
L=ROOT/'ledger';L.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(L/name).write_text(json.dumps(obj,indent=2)+'\n')
proof=ROOT/'sections/E_lower_fiftythree.tex'
data=json.loads((ROOT/'code/e_lower_fiftythree.json').read_text())
replay=json.loads((ROOT/'code/e_lower_fiftythree_replay.json').read_text())
layout=json.loads((ROOT/'code/e_lower_fiftythree_layout.json').read_text())
amend=json.loads((L/'e_lower_fiftythree_rational_export_amendment.json').read_text())
assert amend['status']=='PASS' and amend['all_other_JSON_fields_identical']
assert amend['new_main_sha256']==sha(ROOT/'code/e_lower_fiftythree.py')
assert amend['new_JSON_sha256']==sha(ROOT/'code/e_lower_fiftythree.json')
assert amend['unchanged_proof_sha256']==sha(proof)
assert amend['fresh_checker_replay']['stdout_byte_identical']
assert amend['fresh_checker_replay']['JSON_byte_identical']
for item in amend['unchanged_arithmetic_files']:
    assert sha(ROOT/item['path'])==item['sha256']
assert data['status']==replay['status']=='PASS'
assert layout['status']=='LAYOUT_PASS' and layout['pages']==9
assert layout['section_sha256']==sha(proof)
assert (ROOT/'code/e_lower_fiftythree.out').read_bytes()==(ROOT/'code/e_lower_fiftythree.json').read_bytes()
assert replay['excluded_fields']==replay['excluded_binary_components']==[]
assert all(x['byte_identical'] for x in replay['text_outputs'].values())
assert all(x['complete_decoded_GEN_identical'] for x in replay['binary_objects'].values())
tex=proof.read_text()
assert [int(x) for x in re.findall(r'\\tag\{E119\.(\d+)\}',tex)]==list(range(1,29))
assert len(re.findall(r'(?m)^\\\[$',tex))==len(re.findall(r'(?m)^\\\]$',tex))
assert not any(ord(c)<32 and c not in '\n\t' for c in tex)
assert '^{,' not in tex
GP_NAMES=['e53_horizontal_base','e53_genus_kummer','e53_six_character_witness',
 'e53_horizontal_norm_matrix','e53_genus_transition','e53_local_genus_maps',
 'e53_positional_horizontal_norm','e53_positional_genus_transition']
DEPS=['e116_small_inert_units','e116_prime_columns']

save('e_lower_fiftythree_results.json',[{
 'id':'E.119','status':'Proved',
 'statement':'For the actual first positional53 field L1=Q(beta1), beta1^3=53*zeta3, and B1=L1(zeta9), the full S-class groups are C3^2; the ordinary three-class groups are C9+C3 and C9+C3^2. The literal S-Hilbert field, horizontal ideal norm/extension, complete completed S-unit bases, both unit norm images and their full fibres are evaluated. At B2/B1 and L2/L1 the actual six/two local characters and complete idelic genus presentations give exactly the sigma-coinvariants C9+C3^3 and C9+C3, with every Smith forward/inverse map, surjective norm, projected extension and capitulation bound. Exact S-unit norm indices are 3^5 times the actual B capitulation order and 3 times the actual L capitulation order. The full upper class groups remain in explicit exact sequences with kernel (sigma-1)A2.',
 'where_proved':'sections/E_lower_fiftythree.tex, E119.1--28 and complete proof; code/e_lower_fiftythree.py with eight owned GP stages, two literal E116 dependency stages, all full outputs and complete PARI objects.',
 'depends_on':['E.46','E.114','E.116','E_MilneCFT','E_LemmermeyerAmbiguous','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379; Part E(c),(d), Item2/Lead3 via the actual H quotient and root-cubing Kummer--Shapiro map.'],
 'depends_on_doubtful_reading':False,
 'notes':'Default flag0 fully certifies the cyclotomic and positional lower fields. Successful flag1 on the degree9 c-fixed field proves only a natural class-presentation upper quotient; exact ideal relations prove its zero S-class quotient. The full B1 S-class group follows from actual quadratic norm/extension and cgc=g^-1. Independent principal-divisor index and residue-unit saturation prove the full ordinary B1 class/unit conclusions. The timed-out upper BNF certification is not used. All upper coinvariant statements retain the exact quotient kernel and no higher stability is assigned.'
}])
save('e_lower_fiftythree_coverage.json',{
 'statement':'E.119',
 'addresses':[{'task':'Part E(c),(d), Item2 and Lead3 through the actual H quotient',
   'scope':'A complete finite transition in the unresolved lower j=1 positional factor for first classes on the kappa(53) line.',
   'exact_maps':['Literal beta1=beta2^3 and Ld subset Bd map, with root-cubing pushforward equal to field norm under E46.',
    'Actual outside-S ideals, local Artin characters, ideal Frobenius norm square and full S-Hilbert Kummer field.',
    'Horizontal norm I to C3^2 and transfer C3^2 to I, with the order27 semidirect group and prime163/7 sign calibration.',
    'Complete S-unit matrices, continuous inverse coset representatives, actual torsion carries and full free/torsion kernels.',
    'Idelic quotient to the maximal abelian-over-base subfield of the upper S-Hilbert field; totally ramified decomposition sections identify its restriction kernel with A2/(sigma-1)A2.',
    'Exact rational ambient formulas that restrict to integral Smith maps on the restriction-kernel lattice, with full inverse, norm and projected extension on every finite coordinate.',
    'Outside-S element/ideal Hilbert90 identifies actual capitulation with H1 of S-units; the full Herbrand quotient gives the remaining unit-norm index.']}],
 'closed_steps':['Full B1 and L1 ordinary/S class groups, literal S-Hilbert field and horizontal class maps.',
  'Complete B1 S-units with independent ordinary three-saturation and principal S-divisor lattice.',
  'Every horizontal norm image/fibre, including torsion and actual inverse maps.',
  'All next local characters and both complete finite genus/coinvariant presentations.',
  'Exact next norm kernels, projected extension maps and necessary actual capitulation lines.'],
 'remaining':['The full A(B2), A(L2) and kernels (sigma-1)A2 require their actual normalizer actions and transfer maps.',
  'Actual capitulation inside the two displayed lines remains to be evaluated; the exact unit norm indices retain those actual orders.',
  'Higher lower positional53 transitions, their compatible inverse systems and the j=2 factor are not assigned values here.',
  'Intrinsic metabelian or marked sections still map to H through their established actual quotient; no surjectivity is inferred from these H norm coordinates.']
})
save('e_lower_fiftythree_source_evidence.json',{
 'statement':'E.119',
 'sources':[
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'opened_passages':['III Theorem3.1 and complete cup-product Res/Cor proof, lines6262--6297: turn1026view0/turn1027view0, freshly turn1038view3. The invariant/corestriction identity is used in that proved orientation.',
    'V Proposition3.3, including its full ideal-norm/Frobenius proof, lines9131--9168: turn1026view1 and freshly turn1032view0.',
    'V Theorem3.6 and Example3.9, the class-field correspondence and modulus-one Hilbert class field: turn1027view4 and turn1032view0, both exact passages freshly turn1038view1.',
    'V Proposition5.2 and its full local-to-global idele proof, with reciprocity Theorem5.3 and existence Theorem5.5: turn1027view1, turn1032view1 and freshly turn1038view0. Root independently reopened the precise numbering at turn1035--1037. V5.4 is the Hilbert-symbol product-formula example, not an existence theorem.',
    'VII Proposition3.1 and its complete lattice/Herbrand proof, lines12803--12908: turn1026view3/turn1027view2--3, freshly turn1032view2 and turn1038view2.',
    'VIII Theorem3.1 and complete cyclic Hasse norm proof, lines14305--14331: turn1026view4.'],
   'usage':'Actual local norm/inclusion and transfer maps, the precise ideal/Frobenius norm square, S-Hilbert idelic quotients, S-unit Herbrand indices and cyclic field-norm sufficiency.',
   'precision':'The printed III Lemma3.2 says its proof is to be added; no complete printed proof of that lemma is claimed. In Tate degree minus2, H^(-2)(G,Z)=G^ab: restriction is group transfer, and corestriction is induced by subgroup inclusion. In degree0 for the multiplicative field module, the maps are field inclusion and norm. Cupping with the fundamental class in the proved III3.1 Res/Cor square therefore gives inclusion--transfer and norm--restriction for local reciprocity. The product of local maps in V5.2 gives the actual global ideal maps. The outside-S Hilbert90 capkernel and every finite idele presentation are proved explicitly in E119.'},
  {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
   'opened_passages':['Theorem1, Proposition1 and its complete ideal/Hilbert90 construction: turn1023view1/turn1026view6 and freshly turn1030view1.',
    'The full remaining invariant-ideal and unit Herbrand reduction through the end of the proof, lines201--339: turn1027view5--6 and turn1032view3.'],
   'usage':'The exact element/ideal cohomology maps; E119.16 proves the needed outside-S capkernel isomorphism and both inverse constructions directly.'},
  {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html',
   'opened_passages':['Official bnfcertify contract, flags0/1 and factored principal generator representation: turn1026view5 and turn1030view2/turn1032view4.',
    'Official PARI2.19.0 doc/usersch3.tex lines20401--20433, and src/basemath/buch3.c class-generation phase already opened and retained with E116.'],
   'usage':'Flag1 certifies only the natural class-presentation upper quotient. Full ideal identities and the independent residue determinant supply the separate exact class/unit conclusions. Full flag0 is used only where it returned1.'}
 ],
 'author_review':'Complete proof and every owned source read; exact copied-source ten-stage reconstruction and full decoded-object comparison passed before the narrow rational-export correction. All arithmetic sources, outputs and BIN objects remain byte unchanged. A new separate copied checker-only replay of the corrected exact JSON export passed, with no excluded field.',
 'peer_status':'D completed full proof/all-ten-GP-source/checker and independent exact map review. The peer identified the ambient-export denominator3 truncation, also present in the author export; both exact in-memory tests were correct. Corrected peer export/refreeze is pending this amended author manifest.',
 'root_status':'Root reports full proof/source review and complete source-only ten-stage replay PASS. Its original reconstruction is preserved. A separate root check of the corrected rational exports is pending this amended manifest.',
 'serialization_amendment':'ledger/e_lower_fiftythree_rational_export_amendment.json; the complete original frozen tree is preserved in audit/pre_rational_export/full_tree.'
})
save('e_lower_fiftythree_dependencies.json',{
 'portable_full_rebuild':'python code/e_lower_fiftythree.py --gp /absolute/path/to/gp',
 'workspace_full_rebuild':'python research_e119/code/e_lower_fiftythree.py --gp /workspace/scratch/e34c61ec5a35/research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck':'python code/e_lower_fiftythree.py',
 'fresh_copy_comparison':'python code/e_lower_fiftythree_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path',
 'layout':'python code/e_lower_fiftythree_layout.py',
 'freeze':'python code/e_lower_fiftythree_freeze.py',
 'required_sources':['code/e_lower_fiftythree.py']+['code/'+n+'.gp' for n in GP_NAMES]+['inputs/'+n+'.gp' for n in DEPS],
 'precomputed_binary_inputs_required_for_full_rebuild':[],
 'expected_text_outputs':['code/e_lower_fiftythree.out','code/e_lower_fiftythree.json']+['code/'+n+'.out' for n in GP_NAMES]+['inputs/'+n+'.out' for n in DEPS],
 'expected_complete_binary_outputs':sorted(replay['binary_objects']),
 'successful_structured_records':data['successful_GP_record_counts'],
 'Python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'serialization_rule':'Each ten-stage mathematical reconstruction uses initially empty temporary directories, avoiding writebin append semantics. Complete deserialized PARI objects are compared; raw serialization bytes may differ and no component is excluded. Ambient rational forward matrices use canonical exact rational strings, decoded entrywise with Rational; every integer matrix export asserts integrality and exact decode equality.',
 'post_amendment_recheck':'python code/e_lower_fiftythree.py (all unchanged GP records); a copied checker-only replay is retained in audit/rational_export_replay/fresh. No BNF certification was repeated for this export amendment.',
 'old_BNF_status':'The superseded seventeen sessions24024 and40565 were stopped with exit130 in E101 and were not restarted. E119 retains one actual180-second B1 flag1 timeout; no expensive equivalent certification is repeated.'
})
save('e_lower_fiftythree_computation_status.json',{
 'statement':'E.119','status':'PASS',
 'final_owned_full_rebuild_session':55404,'final_owned_full_rebuild_exit':0,
 'fresh_copy_replay':'audit/author_replay_final/replay.json',
 'fresh_copy_text_outputs':len(replay['text_outputs']),
 'fresh_copy_complete_PARI_objects':len(replay['binary_objects']),
 'excluded_fields':[],'excluded_binary_components':[],
 'rational_export_amendment':amend,
 'finite_checks':{'horizontal_group_products':data['horizontal_group_products_checked'],
  'norm_M_inverses':data['norm_to_M']['inverse_checks'],
  'norm_M_kernel_coordinates':data['norm_to_M']['kernel_coordinate_checks'],
  'norm_L_inverses':data['norm_to_L1']['inverse_checks'],
  'B_coinvariant_Smith_roundtrips':data['B2_genus']['exact_Smith_roundtrips'],
  'L_coinvariant_Smith_roundtrips':data['L2_genus']['exact_Smith_roundtrips'],
  'norm_transfer_compositions':data['norm_transfer_composition_checks']},
 'failed_and_superseded_attempts':[
  {'directory':'code/history/horizontal_flag1_timeout','actual_exit':124,'timeout_seconds':180,
   'status':'No certification return before the timeout. Actual stdout contains only the stack warning. No class-number or unit-completeness assertion is drawn from it.'},
  {'directory':'code/history/genus_sign_failure','status':'The first radical product was minus53; the literal sign was corrected and the positive product is independently checked.'},
  {'directory':'code/history/genus_tame_localpower_failure','status':'A fractional local-power input caused a GP type error. Replaced by exact finite residue-cube calculations, with independent mod53^2 verification.'},
  {'directory':'code/history/genus_residue_type_failure','status':'Finite-field lift was not an integer; replaced by explicit residue enumeration at degree-one primes.'},
  {'directory':'code/history/genus_rank_shape_failure','status':'A GP Mat row-shape error was corrected to the actual matrix.'},
  {'directory':'code/history/genus_principal_precision_failure','status':'Expanded principal generators exceeded the available precision. The final proof uses literal factored generators with exact ideal checks.'},
  {'directory':'code/history/genus_expanded_ideal_overflow','status':'Expanding those factored generators overflowed the stack. The final check factors the full ideals and cancels every prime valuation, with proven rational factor primes.'},
  {'directory':'code/history/local_genus_quote_failure','status':'GP output string quoting failed; corrected structured output retained.'},
  {'directory':'code/history/initial_stack_guard','actual_exit':1,'status':'Initial strict output guard rejected the exact benign new-maximum-stack warning. Corrected narrowly; no mathematical output was changed.'},
  {'directory':'code/history/genus_before_prime_certification','status':'Successful earlier source/output retained before adding explicit rational-prime proofs and original ideal HNF columns.'},
  {'directory':'code/history/before_fixed_field_ideal_relations','status':'Successful earlier source/output retained before adding every literal R-prime relation and class-generator power relation.'},
  {'directory':'audit/author_replay','actual_exit':1,'status':'All twelve text outputs and all twelve full decoded objects already matched, but the comparison guard rejected the exact allocatemem warning. Original wrapper, actual stdout and full fresh outputs retained. Final replay from another empty tree accepts only that literal warning.'},
  {'directory':'code/history/initial_matrix_columns','actual_exit':1,'status':'TeX default matrix-column limit caused the first preview failure. Replaced locally by an explicit fifteen-column array.'},
  {'directory':'code/history/initial_delimiter_and_overfull','actual_exit':1,'status':'Retained TeX control-character/missing-backslash failure and long-line layout. Exact amendment source/output records the literal corrections; mathematical coefficients unchanged.'}
  ,{'directory':'code/history/before_reciprocity_citation_correction','status':'Retained proof and clean preview before correcting the existence-theorem number from V5.4 to V5.5 and spelling out the actual Tate degree-minus-two Res/Cor maps. No mathematical matrix or arithmetic source/output changed.'}
 ],
 'layout':layout,
 'visual_scope':'Author viewed the full nine-page contact sheet and enlarged pages1,4,5,7,8. The final automated PDF text checks and LaTeX log contain no overfull, undefined-reference or undefined-citation warning.'
})
(L/'e_lower_fiftythree_refs.bib').write_text('% verified: E119 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_PARICertifiedUnits. Exact primary passages, proof scope and certification limits are in e_lower_fiftythree_source_evidence.json. No duplicate bibliography keys.\n')
(L/'e_lower_fiftythree_report.md').write_text('''# E.119 — Actual next positional maps at 53

## Evaluated fields and complete lower groups

The positional field is L1=Q(beta1), beta1^3=53*zeta3, and B1=L1(zeta9)=Q(zeta9,cuberoot53). The actual S set consists of primes over3 and53. The theorem proves the full S-class groups A(B1)=C3² and A(L1)=C3². Their full ordinary three-class groups are C9+C3² and C9+C3 respectively.

The class-generation bound for the degree-nine c-fixed field is certified with PARI flag1. Every S-prime relation and the sole class-generator cube are independently checked as complete ideals. This proves its zero S-class quotient. Actual quadratic norm/extension then gives c=-1 on A(B1), and the field relation cgc=g^-1 forces g=1. The exact idele genus quotient therefore equals the entire A(B1).

Three literal pi_j in Q(zeta9) have product53. Their independent prime valuations, the exact wild Hensel valuation13>12 and all tame cube residues prove that adjoining their cube roots gives the entire S-Hilbert field of B1. Arithmetic primes over163 and7 calibrate the horizontal norm and Artin signs. The order27 group and its actual transfer give N(e0,e1)=(0,e0+2e1) and j(a,b)=(a,a), including both compositions and the full capitulation kernel.

## Complete unit maps with inverse coordinates

Fifteen literal elements in the retained eighteen-dimensional tensor basis form the full completed B1 S-unit group C9+Z3^14. The nine ordinary columns have residue-character determinant minus17, so they are three-saturated independently of any upper BNF completeness. The actual norm to M=Q(zeta3,cuberoot53), whose S-class group is zero by E116, has exact index9 by the outside-S Hilbert90 map and S-unit Herbrand quotient. Its valuation image proves the full principal S-divisor lattice: the three wild valuations are congruent modulo3 and the tame valuations are arbitrary.

This divisor lattice has index9. Combined with A(B1) of order9 it proves that the ordinary three-class group has order81. Actual power relations for three ideal generators of orders9,3,3, their genus images and all S-prime relation columns prove the displayed exact group without using the timed-out upper certification.

The theorem prints both complete horizontal norm matrices. It gives continuous inverse coset representatives, all free kernel coordinates, and the actual torsion C3 generated by xi^3. The norm to M has kernel C3+Z3^8; the norm to L1 is onto with kernel C3+Z3^10. The digit section C3 to C9 has its literal carry in xi^3; no homomorphic splitting is asserted.

## The actual next quotient and its remaining kernel

At B2/B1 all six S-primes are totally ramified. The complete local character matrix has rank2: the three wild rows coincide and the three tame rows coincide. On ordinary units its rank is1. Each sign is fixed by the actual arithmetic local Artin norm square, the norm uniformizer beta1+1 at3 and beta1 at53, and the same global zeta3.

The exact idelic presentation retains local generators, ordinary ideal generators, their full principal powers and all S-prime corrections. Its Smith form is Gamma_B=C9+C3^4. The actual restriction to B2 has kernel Q_B=C9+C3^3. A totally ramified decomposition subgroup in the upper S-Hilbert field splits restriction, so this kernel is exactly A(B2)/(sigma-1)A(B2). The full Smith matrices and inverses identify every coordinate, not only the group order.

The direct positional calculation gives Gamma_L=C9+C3² and Q_L=C9+C3. Its two local characters vanish on every complete lower S-unit. Both norms Q_B,Q_L to their lower C3² groups are onto. Their kernels are C3³ and C3. The projected extension maps are (a,b) to (6a+3b,0,0,0) and (a,b) to (6a,0). Both norm/transfer compositions are verified on every finite class.

The exact projection kernels (sigma-1)A(B2) and (sigma-1)A(L2) remain displayed. Actual capitulation embeds in the diagonal C3 for B and the second-coordinate C3 for L. Outside-S Hilbert90 and Herbrand give exact completed S-unit norm indices 3^5 times the actual B capitulation order and3 times the actual L order. Field-norm indices are9 and1; their quotients by actual S-unit norms have orders3^3 times the B order and3 times the L order. These formulas retain the concrete uncomputed maps and do not assign the full upper groups their coinvariant values.

## Reproduction, failures and scope

Run `python code/e_lower_fiftythree.py --gp /absolute/path/to/gp`. It reconstructs the two literal E116 dependency stages and all eight owned stages in empty temporary directories, then checks the complete finite matrices, maps and inverse coordinates. No precomputed BIN object is required. Expected outputs and source lists are in e_lower_fiftythree_dependencies.json.

The separate source-only author replay compares all twelve complete text outputs and all twelve decoded PARI objects, with no omitted field or component. It retains both raw serialization hashes and exact GEN equality. The first comparison guard rejected a benign allocatemem warning after all arithmetic comparisons had passed; its entire source and output are retained, and a second empty-tree replay passes the narrowed guard.

All actual failed or superseded programs and outputs are retained. In particular the180-second upper flag1 timeout supplies no proof of a class number or unit basis. Expanded-principal precision/stack failures are replaced by exact factored-ideal checks with proven factor primes. The complete failed preview sources and literal TeX correction record are preserved.

The final standalone proof is nine pages. The full contact sheet and enlarged formula pages were actually viewed; the automated final preview has no overfull or unresolved-reference warning. The proof and PDF remain byte unchanged through the certificate amendment. Root reports complete proof/source review and full source-only ten-stage replay PASS; D reports full proof/source and independent map review.

## Exact rational-export amendment

The two ambient forward matrices are KU*K^-1. Their restrictions to the displayed kernel lattices are integral, but their ambient last rows contain twelve denominator-three entries (eight for B2 and four for L2). Each of those rows is a modulus-one Smith coordinate. The old JSON integer conversion truncated these twelve ambient entries; the exact in-memory maps, all finite quotient coordinates, proof, GP arithmetic and inverse tests were correct.

The complete original frozen tree, including its manifest, actual sources and outputs, is preserved under audit/pre_rational_export/full_tree. The amended forward matrices are arrays of canonical rational strings and are decoded entrywise with exact Rational equality. Every integer-matrix export now asserts denominator one and exact decoded equality. Both full ambient inverse compositions are checked. The entire corrected JSON differs from its predecessor only in the two forward fields; all other fields are identical.

A new isolated checker-only replay uses the unchanged GP outputs and sources and reproduces the complete corrected stdout and JSON byte for byte. Every arithmetic GP source/output and BIN hash is unchanged; no BNF certification was repeated. The original full ten-stage author and root replays remain retained with their precise pre-amendment scope. The amendment's complete field/entry list is in e_lower_fiftythree_rational_export_amendment.json.

The next arithmetic task is the actual normalizer action on A(B2) and A(L2), the projection kernels and actual capitulation. Their further tower compatibility and the remaining lower j=2 factor are still required for the unrestricted positional53 norm system. Every transfer back to H uses E46's root-evaluation Kummer--Shapiro map and literal root-cubing norm. The intrinsic-to-H lifting map remains the established further quotient.
''')
exclude={'ledger/e_lower_fiftythree_manifest.json','code/e_lower_fiftythree_freeze.out'}
files={}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in exclude:continue
    files[rel]={'sha256':sha(p),'bytes':p.stat().st_size}
save('e_lower_fiftythree_manifest.json',{'statement':'E.119','status':'FROZEN_AUTHOR_PASS',
 'files':files,'excluded_own_stdout':'code/e_lower_fiftythree_freeze.out',
 'mathematical_rebuild':'python code/e_lower_fiftythree.py --gp /absolute/path/to/gp',
 'complete_copy_replay':'python code/e_lower_fiftythree_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path'})
print(json.dumps({'statement':'E.119','status':'FROZEN_AUTHOR_PASS','files':len(files),
 'proof_sha256':sha(proof),'main_sha256':sha(ROOT/'code/e_lower_fiftythree.py'),
 'JSON_sha256':sha(ROOT/'code/e_lower_fiftythree.json'),
 'manifest_sha256':sha(L/'e_lower_fiftythree_manifest.json'),
 'standalone_pages':layout['pages'],'complete_text_replays':len(replay['text_outputs']),
 'complete_PARI_object_replays':len(replay['binary_objects'])},indent=2))
