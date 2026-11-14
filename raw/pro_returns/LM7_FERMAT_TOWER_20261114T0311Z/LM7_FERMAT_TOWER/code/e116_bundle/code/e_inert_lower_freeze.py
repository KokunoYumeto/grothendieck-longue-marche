#!/usr/bin/env python3
"""Freeze E116 with literal successful and unsuccessful execution evidence."""
from pathlib import Path
import hashlib,json,re,shutil
ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/'ledger';LEDGER.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(LEDGER/name).write_text(json.dumps(obj,indent=2)+'\n')
proof=ROOT/'sections/E_inert_lower_factors.tex'
d=json.loads((ROOT/'code/e_inert_lower_factors.json').read_text())
assert d['status']=='PASS'
assert (ROOT/'code/e_inert_lower_factors.json').read_bytes()==(ROOT/'code/e_inert_lower_factors.out').read_bytes()
assert d['newton_valuation_checks']==145 and d['compatible_pure_prime_chains']==108
assert d['raw_scaled_toric_inverse_checks']==700
assert d['first_lower53']['full_norm_fibre_inverse_checks']==6561
assert d['first_lower53']['class_congruence_checks']==81
assert d['pure53_power_class_checks']==81
assert len(d['actual_nonzero_zeta_columns'])==29
assert sum(x['checks'] for x in d['literal_pure_unit_norm_maps'])==486
tex=proof.read_text()
assert [int(x) for x in re.findall(r'\\tag\{E116\.(\d+)\}',tex)]==list(range(1,25))
assert len(re.findall(r'(?m)^\\\[$',tex))==len(re.findall(r'(?m)^\\\]$',tex))==24
assert not any(ord(c)<32 and c not in '\n\t' for c in tex)
assert '^{,' not in tex
layout=json.loads((ROOT/'code/e_inert_lower_layout.json').read_text())
assert layout['status']=='LAYOUT_PASS' and layout['section_sha256']==sha(proof)
peer=ROOT.parent/'a_e116_focus'
if peer.exists():
    for ext in ('md','json'):shutil.copy2(peer/f'audit.{ext}',LEDGER/f'e_inert_lower_peer_audit.{ext}')

save('e_inert_lower_results.json',[{
 'id':'E.116','status':'Proved',
 'statement':'For every inert rational prime ell congruent2 or5 modulo9, all pure and complex radical-tower three-class groups vanish; pure ordinary-unit norms are onto with explicitly presented free kernels. Literal coherent principal prime generators and unit norm matrices evaluate the entire pure completed norm factor, and E114/E46 then give every global H fibre for nonzero first classes on the kappa(ell) line, including the exact scaled total-norm inverse. At53 the complete first pure S-unit norm image and every fibre, the exact ordinary class group C3², zero pure S-class group, and complex S-class group C3 with sigma=1,c=-1 are evaluated. The complex field-unit norm test has one congruence and the actual S-unit norm test has two, with a literal nonzero defect witness.',
 'where_proved':'sections/E_inert_lower_factors.tex, E116.1--24 and complete proof. code/e_inert_lower_factors.py plus its five GP stages, four retained Python component verifiers, all actual outputs and complete PARI objects.',
 'depends_on':['E.38','E.46','E.55','E.110','E.111','E.114','E_MilneCFT','E_LemmermeyerAmbiguous','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379; Part E(c),(d) through the actual H quotient and positional norm map.'],
 'depends_on_doubtful_reading':False,
 'notes':'The full default-flag0 certification at degree9 timed out and is not used. The completed flag1 certification supplies only the natural class presentation upper quotient. Exact S-prime relations, Hilbert90 with the conjugation sign, quadratic norms and an independent lower bound prove the actual class group. A separate determinant-minus-four residue matrix proves three-saturation of the four units. All higher lower53 factors remain explicit residual norm systems; no intrinsic metabelian lift is inferred from an H class.'
}])
save('e_inert_lower_coverage.json',{
 'statement':'E.116',
 'addresses':[{'task':'Part E(c),(d), Item2/Lead3 through the actual H quotient',
  'status':'Complete first-line H fibres for inert ell with v3(ell+1)=1; exact first lower53 transition',
  'exact_maps':['Cubic and quadratic field norms, with Nj=3 or2 on the actual ideal lattices.',
   'Complex conjugation fixed-part maps j and N/2 on completed pure units.',
   'Ordinary norm Smith matrices, right inverses and free kernel coordinates at every pure height.',
   'Actual coherent principal prime chains, restricted product splitting and initial rational norm.',
   'Kummer-Shapiro and E55 cocycle comparison in both directions, with the raw norm equal to the scaled toric cube.',
   'Outside-S ideal Hilbert90 capkernel and invariant-class norm-defect maps, including nu(cD)=cnu(D)^-1.',
   'Flag1 natural class upper quotient and literal ideal relation columns, followed by an independent exact class lower bound.',
   'Every first53 S-unit norm fibre and the complete Smith inverse, ordinary-unit residue saturation and exact complex obstruction class.']}],
 'closed_steps':['All pure norm factors at s=1 and hence all H first-line fibres after E114.',
   'The exact degree-nine pure53 class, S-unit basis and first norm image/fibres.',
   'The exact degree-eighteen complex53 S-class group and its actual sigma/c actions.',
   'Both directions of the complex first53 field-norm versus S-unit norm tests.'],
 'remaining':['Higher pure53 transitions and the lower complex positional factors j<3 are not evaluated here.',
   'For arbitrary inert primes with s>1, E114 evaluates j>=s; the lower factors require their actual class/unit norm calculations.',
   'The exact intrinsic metabelian/marked-to-H quotient remains a further lifting problem; this statement does not claim every H class lifts.',
   'No value of an uncomputed upper ordinary complex class group is inferred from its evaluated S-class group.']
})
save('e_inert_lower_source_evidence.json',{
 'statement':'E.116',
 'sources':[
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'opened_passages':['VII Proposition3.1 and complete lattice proof, printed208--209: turn1005view0--1 through line12908.',
     'III Theorem3.1 and the proved cup-product Res/Cor compatibility: turn1004view5.',
     'VIII Theorem3.1 and complete cyclic Hasse norm proof: turn1004view4.',
     'III invariant/corestriction identity(30), through its proof, was retained in turn1003view1 and earlier E114 source reads.'],
   'usage':'Exact ordinary/S-unit Herbrand quotients, actual local Artin norm square, cyclic field-norm sufficiency and exact completion comparisons.',
   'precision':'III Lemma3.2 is not claimed to have a printed proof; the norm square follows from the explicitly proved preceding cup-product compatibility.'},
  {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
   'opened_passages':['Theorem1, Proposition1 and its full ideal/Hilbert90 construction: turn1002view1.',
     'The complete remaining ideal-index and Herbrand proof, printed3--5: turn1004view0--1.'],
   'usage':'Both ambiguous and strongly ambiguous class formulae. The exact outside-S Hilbert90 map and its conjugation sign are proved afresh in E116.19--21.'},
  {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html',
   'opened_local_primary':['Official PARI2.19.0 doc/usersch3.tex, bnfcertify at lines20401--20433.',
     'Official source src/basemath/buch3.c, bnfcertify0 class-generation phase at lines1167--1210.'],
   'retained_excerpts':['inputs/pari_bnfcertify_documentation.txt','inputs/pari_bnfcertify_class_phase.txt'],
   'usage':'Default flag0 certifies the complete BNF; flag1 certifies the natural class upper quotient only. The separate actual residue determinant supplies the three-saturation of the units.'}
 ],
 'computation_domains':['Twelve certified degree3/6 lower fields and two default-flag0 certified degree9 examples at2 and5.',
    'A degree9 candidate at53, used only for literal verified element/ideal identities, followed by successful flag1 class bound.',
    'Actual finite residue fields at13,61 and53, and three-adic arithmetic at the three labeled completions.'],
 'peer_status':'A complete proof read with independent focused PASS on E116.19--21, the completion maps, conjugation twist and full complex S-class deduction is copied to e_inert_lower_peer_audit.md/.json. No peer GP replay is claimed.',
 'root_status':'Full source and completed computations supplied to root; independent final root proof/rebuild audit pending at author freeze.'
})
save('e_inert_lower_dependencies.json',{
 'portable_full_rebuild':'python code/e_inert_lower_factors.py --gp /absolute/path/to/gp',
 'workspace_full_rebuild':'python research_e116/code/e_inert_lower_factors.py --gp research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck':'python code/e_inert_lower_factors.py',
 'required_sources':['code/e_inert_lower_factors.py','code/e_small_inert_units.gp','code/e53_prime_columns.gp',
    'code/e53_pure9_norm_witness.gp','code/e53_pure9_class_upper.gp','code/e53_exact_maps.gp',
    'code/e53_first_norm_explore.py','code/e53_s_norm_explore.py','code/e53_unit_saturation.py','code/e53_complete_transition.py'],
 'required_precomputed_binary_inputs':[],
 'Python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'retained_actual_binary_outputs':['code/e_small_inert_units.bin','code/e53_prime_columns.bin',
    'code/e53_pure9_candidate.bin','code/e53_pure9_norm_witness.bin','code/e53_pure9_class_upper.bin','code/e53_exact_maps.bin'],
 'serialization_rule':'The full rebuild uses a clean temporary directory, avoiding PARI writebin append semantics. Compare all deserialized PARI components if raw serialization differs; no component is excluded.',
 'layout_command':'python code/e_inert_lower_layout.py',
 'layout_dependencies':['Pillow','pdftoppm','paper LuaLaTeX type1 runtime'],
 'old_BNF_status':'The old superseded sessions24024 and40565 were stopped with exit130 in E101. They were not restarted. No degree18 upper BNF is launched here.'
})
save('e_inert_lower_computation_status.json',{
 'statement':'E.116','status':'PASS','actual_final_full_rebuild_exit':0,'full_rebuild_session':26875,
 'main':'code/e_inert_lower_factors.py','stdout':'code/e_inert_lower_factors.out','JSON':'code/e_inert_lower_factors.json',
 'successful_GP_stages':d['successful_GP_structured_record_counts'],
 'finite_counts':{'Newton':145,'nonzero_zeta_columns':29,'compatible_prime_chains':108,
  'small_pure_norm_inverse':486,'raw_scaled_toric_inverse':700,'pure53_class_congruences':81,
  'pure53_norm_fibre_inverse':6561,'pure53_unit_power_classes':81},
 'failed_or_superseded_attempts':[
  {'source':'code/e53_pure9_cert.gp','stdout':'code/e53_pure9_cert.out','session':88140,'outer_timeout_seconds':180,'actual_exit':124,
   'status':'Stopped before default-flag0 certification returned. Its candidate class number is not used as proof. No equivalent full certification was repeated.'},
  {'stdout':'code/history/initial_binary_path_failure.out','actual_exit':127,
   'status':'The first executable-relative-path was one directory too high; corrected path is in the portable driver.'},
  {'source':'code/history/parse_1/e_small_inert_units.gp','stdout':'code/history/parse_1/e_small_inert_units.out','actual_GP_exit':0,
   'status':'GP parse error despite exit0; no PASS or arithmetic output accepted.'},
  {'source':'code/history/norm_witness_mod_sign/e53_pure9_norm_witness.gp','stdout':'code/history/norm_witness_mod_sign/e53_pure9_norm_witness.out',
   'status':'Element/ideal checks passed, but a Mod-valued sign was not valid JSON. The print was corrected to lift(sign), with literal norms unchanged.'},
  {'source':'code/history/appended_binary_read_failure/e53_exact_maps.gp','stdout':'code/history/appended_binary_read_failure/e53_exact_maps.out','actual_GP_exit':0,
   'status':'A previous repeated writebin appended objects, so read returned two objects and the component access failed. Both original appended BIN files are preserved. The successful pipeline rebuilds in a clean directory and retains one complete object per file.'},
  {'directory':'code/history/before_full_complex_S_class',
   'status':'Complete initial finite verifier source/stdout/JSON retained before adding the proved full complex S-class action and actual quadratic/cubic maps.'},
  {'directory':'code/history/initial_layout','status':'Initial complete PDF had five overfull lines. Exact proof/source/stdout/JSON/log/PDF retained; formulas were reflowed without changing the arithmetic.'}
 ],
 'layout':layout,
 'scope':'Finite verified arithmetic supplies the displayed identities and exact certified bounds. All-level class induction, Hilbert90/C2 transfers, compact/restricted inverse systems and global H maps are proved in the theorem.'
})
(LEDGER/'e_inert_lower_refs.bib').write_text('% verified: E116 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_PARICertifiedUnits. Exact newly opened proof passages and the official PARI flag1 source phase are recorded in e_inert_lower_source_evidence.json. No duplicate bibliography keys.\n')
(LEDGER/'e_inert_lower_report.md').write_text('''# E.116 — Complete s=1 norm coordinates and the first lower53 transition

## The uniform completed family

For every inert rational prime ell congruent2 or5 modulo9, the pure tower Q(ell^(1/3^m)) has one prime over3 and one overell at every height. In the complex tower obtained by adjoining zeta3, these two places are totally ramified in every adjacent cubic. The included zeta3 has a nonzero tame norm character atell, while reciprocity leaves only one independent ordinary-unit character. Both ambiguous-class formulae therefore give zero three-primary class groups at every height and the exact ordinary-unit norm quotient C3. Complex conjugation acts by inversion on that quotient.

The actual quadratic maps j and N satisfy Nj=2 and jN=1+c. Taking the c-fixed part gives surjective ordinary-unit norms in the pure tower. Fundamental-unit norm Smith matrices supply the literal recursive coordinates z_(m+1)=R_m z_m+K_m t_m, with t_m in Z3^(3^m), and their coordinate inverse. This evaluates the entire coherent ordinary-unit group as the displayed compact product.

Completed principal generators of the surviving prime chains can be corrected recursively by these surjective ordinary-unit norms. Their initial values are exactly3,ell,p. The pure completed multiplicative norm system is the unit product times two S-valuations times the restricted prime module for primes with the three-primary order of ell modulo p equal1. All infinite products converge uniformly in each multiplication quotient because the exponents are restricted.

E114 evaluates all the remaining positional factors for s=1. The theorem gives the exact total-norm cube formula and its inverse for every nonzero first class on the kappa(ell) line. In particular the two pure S-valuations compensate the actual initial norms of all complex unit and divisor factors. The comparison to E55 is the actual cocycle map through E46, evaluation on the specified arithmetic generators and its inverse; it is not a comparison of abstract product ranks. The intrinsic-to-H projection remains the actual further quotient map and is not asserted to be onto.

## The complete first lower transition at53

Let F=Q(cuberoot53), L=Q(ninthroot53), M=F(zeta3), E=L(zeta3). The lower fields have fully certified class number1. The cubic E/M splits at one of the three3-primes and is cyclotomic at the other two; it is totally ramified at53. Actual local Artin calculations on the seven lower S-unit columns give one character row, the sum of the three3-valuations modulo3. All ordinary-unit columns have zero character.

The outside-S element/ideal Hilbert90 maps give zero S-capitulation kernel from M and S-unit Herbrand quotient9. Thus the true S-unit norm cokernel is C3². Its quotient detected by the field norm has order3. The remaining norm defect is the invariant upper S-class group, with the essential conjugation twist nu(cD)=cnu(D)^-1.

A completed PARI flag1 certification supplies a natural upper presentation C3² for Cl(L). Actual verified ideal identities show that the S-prime columns span this presentation. Consequently Cl_S(L)=0 before the exact ordinary class number is known. Quadratic norm/extension then makes the c-fixed part of Cl_S(E){3} zero. The Hilbert90 twist shows that the natural S-unit norm quotient is entirely c-plus, and the explicit inverse N/2 identifies it with the pure S-unit norm quotient. This proves its index9 independently of an exact class-number assertion.

Eight literal S-units have the displayed four-by-eight norm matrix, whose image also has index9. They therefore generate the full norm image, with both lower3-valuations divisible3. Their exact upper S-divisors span an index9 lattice, while the norm criterion forces every principal S-divisor to lie in that lattice. This gives an independent class lower bound9. Together with flag1 it proves Cl(L)=C3² and the exact prime coordinates.

The four ordinary units are certified three-saturated by four residue maps at13 and61: the character determinant is minus4. Thus the unit index issue left open by flag1 is resolved independently. All eight completed S-units form a basis, and the theorem gives each norm fibre and its explicit inverse in four free Z3 coordinates. The ordinary pure unit norm is onto as well.

The complex S-class group is also fully determined. Its c-fixed part is zero, hence c=-1. The literal relation c sigma c=sigma^-1 forces sigma=1 on this three-group, so its evaluated invariant group C3 is the whole group. The complex field norm criterion is v0+v1+v2=0 modulo3; the true S-unit norm criterion is v0=0 and v1+v2=0 modulo3. The ratio of the actual generators of Q0 and Q1 supplies the nonzero field-norm/S-unit-norm defect. Its quadratic norm is exactly pA/pB.

## Reproduction and scope

Run `python code/e_inert_lower_factors.py --gp /absolute/path/to/gp`. It rebuilds all five successful arithmetic stages in a clean temporary directory, then executes the four component verifiers and every combined coordinate check. The complete PARI objects are retained; if serialized bytes differ, compare every deserialized component. No degree18 BNF is used.

The failed180-second default-flag0 degree9 certification is retained with its actual exit124 and is not used. The successful flag1 return certifies only the upper class presentation. The exact class lower bound, all ideal identities, norm matrices and the separate unit saturation determinant supply the missing conclusions. Prior print/parse/path/append and layout failures retain their actual sources and outputs.

At53 this theorem evaluates the first lower pure/complex transition. It does not assign these groups to later lower layers or claim the remaining intrinsic metabelian section classification is complete. The next work is the actual lower-factor norm/class calculation for arbitrary inert primes with s>1.
''')
exclude={'ledger/e_inert_lower_manifest.json','code/e_inert_lower_freeze.out'}
files={}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in exclude:continue
    files[rel]={'sha256':sha(p),'bytes':p.stat().st_size}
save('e_inert_lower_manifest.json',{'statement':'E.116','status':'FROZEN_AUTHOR_PASS',
    'files':files,'excluded_own_stdout':'code/e_inert_lower_freeze.out',
    'mathematical_rebuild':'python code/e_inert_lower_factors.py --gp /absolute/path/to/gp'})
print(json.dumps({'statement':'E.116','status':'FROZEN_AUTHOR_PASS','files':len(files),
 'proof_sha256':sha(proof),'main_sha256':sha(ROOT/'code/e_inert_lower_factors.py'),
 'JSON_sha256':sha(ROOT/'code/e_inert_lower_factors.json'),
 'manifest_sha256':sha(LEDGER/'e_inert_lower_manifest.json')},indent=2))
