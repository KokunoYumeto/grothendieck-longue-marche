#!/usr/bin/env python3
"""Freeze E114's actual uniform tail proof and all executed evidence."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/'ledger';LEDGER.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(LEDGER/name).write_text(json.dumps(obj,indent=2)+'\n')
proof=ROOT/'sections/E_inert_prime_tail.tex'
code=ROOT/'code/e_inert_tail.py'
summary=ROOT/'code/e_inert_tail.json'
d=json.loads(summary.read_text())
assert d['status']=='PASS'
assert summary.read_bytes()==(ROOT/'code/e_inert_tail.out').read_bytes()
assert d['all_small_augmentation_ideal_cases']=={'1':2,'3':18,'9':13122}
assert len(d['larger_exact_inverse_cases'])==140
assert d['all_actual_character_inverse_checks']==21195
assert d['actual_cyclotomic_ramification_tests']==888
assert d['literal_Q3_cube_Hensel_checks']==426
assert len(d['actual_surviving_prime_chains'])==63
assert d['actual_surviving_prime_transition_checks']==252
assert len(d['actual_orbit_GP_records'])==5
assert d['inputs']['e114_cyclo9_base.bin']==sha(ROOT/'inputs/e114_cyclo9_base.bin')
tex=proof.read_text()
assert [int(x) for x in re.findall(r'\\tag\{E114\.(\d+)\}',tex)]==list(range(1,16))
assert len(re.findall(r'(?m)^\\\[$',tex))==len(re.findall(r'(?m)^\\\]$',tex))==15
assert '^{,' not in tex
assert not any(ord(c)<32 and c not in '\n\t' for c in tex)
layout=json.loads((ROOT/'code/e_inert_tail_layout.json').read_text())
assert layout['status']=='LAYOUT_PASS' and layout['section_sha256']==sha(proof)

save('e_inert_tail_results.json',[{
 'id':'E.114','status':'Proved',
 'statement':'For every inert prime ell and every j>=s=v3(ell+1), all three-primary S-class groups of K_j((ell*zeta_(3^j))^(1/3^m)), S above3 and ell, vanish at every m. The exact cyclic S-unit norm quotient for length r<=j is (Z/3^r)^(3^(s-1)), with literal local residue matrices and inverse maps. A uniform augmentation-ideal inverse evaluates the cubic characters. Each completed tail factor is a split product of the restricted divisor module at primes with v3(ord_p ell)=j and an infinite compact product of Z3. Actual Kummer-Shapiro maps split these evaluated tails off every corresponding global H section fiber, retaining precisely the unevaluated lower norm coupling.',
 'where_proved':'sections/E_inert_prime_tail.tex, E114.1--15 and complete proof; code/e_inert_tail.py and e_inert_tail_orbit.gp with all actual outputs and complete retained PARI object.',
 'depends_on':['E.38','E.46','E.47','E.110','E.111','E_MilneCFT','E_LemmermeyerAmbiguous','E_KatoUniversalNorms'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379, through the actual positional norms and scaled toric map.'],
 'depends_on_doubtful_reading':False,
 'notes':'The full prime orbit has t=3^(s-1) columns. Reciprocity puts its ell-radicand symbol in the augmentation ideal, and the root-of-unity part is a nonzero scalar. The displayed finite geometric series supplies the exact inverse at every t. The S-class vanishing and all-level compact-fiber sufficiency are proved, not extrapolated from the finite certificate. Lower factors j<s and the pure factor remain in the explicit norm condition unless evaluated by earlier statements. Intrinsic lifts through the actual E38 quotient are not inferred.'
}])
save('e_inert_tail_coverage.json',{
 'statement':'E.114',
 'addresses':[{'task':'Part E(c),(d), Item2/Lead3 through the actual H quotient',
 'status':'Complete uniform inert-prime positional tail; exact split comparison to the full first-coordinate fiber',
 'exact_maps':['Literal beta_(m+1,j)^3=beta_(m,j) fields and ideal norms.',
  'Actual Galois orbit of a completed principal prime generator and its circulant character matrix.',
  'The two literal radicand norms and the common-root cup/corestriction square, with local invariant unchanged.',
  'Finite geometric-series inverse in F3[C_(3^(s-1))] and lifted inverses over Z/3^r.',
  'Capitulation-to-Hilbert90 and invariant S-class-to-unit-norm-defect isomorphisms.',
  'Completed principal outside-S divisor map, compact-fiber coherent lift and actual restricted product splitting.',
  'Character-basis compact product coordinates under actual transposed norm maps.',
  'Initial S-valuations, residue-degree rational norm, total-norm cube condition and divided-divisor projection.',
  'Arithmetic unit-part automorphism Phi_u and exact inverse.']}],
 'closed_steps':['All S-class obstructions and all cyclic S-unit norm membership tests in the tail j>=s.',
  'All completed tail divisor systems and their compact fibers.',
  'Infinitely many independent actual global H directions, with their exact S-prime toric corrections.'],
 'remaining':['The pure factor and lower factors j<s, except those settled by prior prime-specific statements, remain in N_<s and its displayed norm coupling.',
  'The next lower-factor work is reserved for E116; this theorem does not declare the full inert-prime first line evaluated.',
  'The image from intrinsic metabelian or marked section sets is still the further lift through the actual E38 quotient kernel.',
  'Separate projection images of the coherent compact unit factor at a fixed finite height are not assigned an uncomputed finite index.']
})
save('e_inert_tail_source_evidence.json',{
 'statement':'E.114',
 'sources':[
 {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
  'opened_passages':['VII Proposition3.1 with its complete lattice proof, printed208--209: turn992view2--3 and turn993view1; the final identity through line12908 was already read in E111 and reopened in turn985view3.',
   'III Section2 formulas29,30 and proved invariant/corestriction comparison: turn985view5.',
   'III Theorem3.1 proved cup-product Res/Cor compatibility, read for E111 as turn963view4 and used with the actual radicand norms.',
   'VIII Theorem3.1 and complete cyclic Hasse norm proof: turn992view4.',
   'VIII Theorem7.4, complete Chebotarev proof through printed260: turn992view0--1 and turn993view0.'],
  'usage':'Exact n^t S-unit Herbrand quotient; the actual local norm/corestriction square; cyclic norm sufficiency; infinitely many independent permitted rational prime chains.',
  'precision':'III Lemma3.2 is not described as possessing a printed proof. The norm square uses the proved cup-product compatibility and local invariant identities.'},
 {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
  'opened_passages':['Theorem1 and Proposition1 with its ideal/Hilbert90 maps: turn984view2 and turn985view1. The full proof was also read for E110/E111.'],
  'usage':'The cyclotomic base three-class induction and the explicit comparison maps used in the S-class proof. The outside-S variant is proved in E111.21--25 and applied with t+1 totally ramified places.'},
 {'key':'E_KatoUniversalNorms','url':'https://ems.press/content/book-chapter-files/27477',
  'opened_passages':['Coherent-norm definition and Theorem1.1(2): turn984view1.',
   'Complete Sections5.4--5.5 proof: turn992view5--6 and turn993view2.',
   'Section3.2 and Proposition4.2 with its proof were already read for E69/E110/E111.'],
  'usage':'Unbounded actual projection ranks of coherent three-units into the literal one-three-place tail chains; the restriction map and its domain are displayed.'}
 ],
 'actual_input':{'path':'inputs/e114_cyclo9_base.bin','sha256':d['inputs']['e114_cyclo9_base.bin'],
  'origin':'E111 certified five-component [BNF,xi,seven S-unit columns,three-primes,seventeen-primes] object.',
  'certification':'The original E111 bnfcertify used default flag0 and returned1. E114 reads that full object and starts no new BNF.'},
 'peer_status':'Complete E111 was independently audited PASS by A; E114 full draft and PASS evidence supplied for its separate audit.',
 'root_status':'Root received the complete E114 result and paths; independent E114 proof/rebuild audit pending at author freeze.'
})
save('e_inert_tail_dependencies.json',{
 'portable_full_rebuild':'python code/e_inert_tail.py --gp /absolute/path/to/gp',
 'workspace_full_rebuild':'python research_e114/code/e_inert_tail.py --gp research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck':'python code/e_inert_tail.py',
 'required_inputs':['code/e_inert_tail.py','code/e_inert_tail_orbit.gp','inputs/e114_cyclo9_base.bin'],
 'Python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'actual_output_binary':'code/e_inert_tail_orbit.bin',
 'complete_binary_contents':'[complete E111 five-component input, three actual orbit elements, full seven-by-three S-unit matrix, three signs]',
 'serialization_rule':'Compare every deserialized PARI component if raw serialization bytes differ; exclude no component.',
 'layout_command':'python code/e_inert_tail_layout.py',
 'layout_dependencies':['Pillow','pdftoppm','paper LuaLaTeX type1 runtime'],
 'old_BNF_status':'The two original superseded sessions24024 and40565 were stopped with exit130 and are preserved in E101; neither was restarted.',
 'history':'The initial complete PASS with a SymPy deprecation warning and the subsequent complete PASS before prime-chain additions have their actual sources, stdout and JSON retained. The stock pdflatex-format failure retains its actual source/stdout/log; the final layout uses the established paper runtime.'
})
save('e_inert_tail_computation_status.json',{
 'statement':'E.114','status':'PASS','actual_final_exit_code':0,
 'main':'code/e_inert_tail.py','stdout':'code/e_inert_tail.out','JSON':'code/e_inert_tail.json',
 'GP':'code/e_inert_tail_orbit.gp','GP_stdout':'code/e_inert_tail_orbit.out',
 'actual_GP_record_count':5,'all_small_ring_inverses':13142,'larger_exact_ring_inverses':140,
 'all_actual_character_inverse_checks':21195,'actual_quadratic_factorizations':7,
 'actual_quadratic_factors':53,'actual_cyclotomic_ramification_tests':888,
 'literal_Q3_cube_Hensel_checks':426,'surviving_rational_prime_chains':63,'actual_prime_chain_steps':252,
 'failed_mathematical_runs':[],
 'retained_presentation_failure':'The first layout run exited1 because the stock pdflatex format was unavailable. Its exact source/stdout/TeX log are retained. The existing paper LuaLaTeX runtime was then used.',
 'layout':layout,
 'scope':'The program proves each finite arithmetic assertion it checks. The uniform class induction, all-level norm maps, compact-fiber lifting and global section comparison are proved in the theorem, not inferred from numerical sampling.'
})
(LEDGER/'e_inert_tail_refs.bib').write_text('% verified: E114 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_KatoUniversalNorms. Exact opened theorem/proof passages are in e_inert_tail_source_evidence.json. No duplicate bibliography keys.\n')
(LEDGER/'e_inert_tail_report.md').write_text('''# E.114 — A uniform evaluated tail for every inert first prime

For an inert rational prime ell, write s=v3(ell+1) and t=3^(s-1). Every positional factor K_j((ell*zeta_(3^j))^(1/3^m)) with j>=s has one three-prime and t ell-primes, all totally ramified in each vertical cubic step. Its three-primary S-class group is zero at every height.

## The actual inverse that proves the uniform result

Choose one completed principal ell-prime generator in K_s and take its genuine Galois orbit under xi_s -> xi_s^4. Its ell-radicand cubic Hilbert matrix is multiplication by a in F3[C_t]. When s>=2, ell is a cube in Q3, so reciprocity puts a in the augmentation ideal. When s=1 the generator is ell and the alternating pairing gives a=0. The xi_s radicand contributes the nonzero scalar c=(ell^2-1)/3^s modulo3.

The inverse is the finite geometric series c^-1 sum_(d=0)^(t-1)(-c^-1*a)^d. At higher cyclotomic bases the actual radicand norm kills the ell term modulo cubes and the matrix is cI. The local invariant/corestriction formula carries these exact characters to every vertical height without multiplying by the local degree.

The S-unit Herbrand quotient is3^t. The actual ideal/Hilbert90 sequences identify its capitulation term and the field-norm versus unit-norm defect. The full character image then forces the invariant upper three-class group to vanish, proving the all-level class result. For every cyclic distance r<=j the complete norm quotient is (Z/3^r)^t. The displayed tame finite-field matrix and its lifted inverse give actual membership and inverse coordinates. The completed kernel has literal torsion mu_(3^r) and the stated free rank.

## Completed factors and global sections

The unique surviving outside-S prime chain exists exactly at P_j(ell), where v3(ord_p ell)=j, and has degree one. Every compatible divisor lifts by compactness of its completed S-unit fibers. Choosing coherent principal generators gives a convergent restricted-product splitting. The compact kernel is an infinite countable product of Z3 with the actual finite-character/transpose-norm coordinate map; Kato's one-three-place theorem supplies unbounded actual projections.

The rational norm is retained as the two initial S-valuations, with ell-prime weights2*3^(j-s). These values are used in the exact Kummer-Shapiro comparison. Every full first-coordinate fiber splits into the evaluated restricted tail divisors and the displayed kernel consisting of lower norm systems together with tail units and their total-norm cube equation. Choosing tail divisors three times arbitrary restricted coordinates and setting all remaining components to one supplies actual global H sections. Their toric coordinates include the literal three/ell corrections of the chosen generators. An explicit Chebotarev class proves infinitely many independent such directions for every tail j.

The lower positional factors j<s and the pure factor remain exactly in N_<s unless previous statements have evaluated them. E116 is reserved for the next lower-factor calculation. The intrinsic metabelian and marked image remains the actual quotient-lifting problem; no intrinsic lift follows from the H section construction alone.

## Exact certificate and rebuild

    python code/e_inert_tail.py --gp /absolute/path/to/gp

The five GP records read the certified E111 object and prove the exact orbit pi1, xi^6*pi3, pi2. The full four-component output object is retained. The Python certificate checks all13142 augmentation-ideal inverses for t=1,3,9;140 additional exact cases for t=27,81;21195 inverse character coordinates for actual cubic, ninth and twenty-seventh matrices; seven actual cyclotomic factorizations with53 prime factors;888 local degree tests;426 literal Q3 Hensel checks; and63 actual rational prime chains with252 root-cubing transitions.

Every executed source and its actual output is retained, including the harmless initial SymPy warning and the stock-format layout failure. No larger BNF calculation ran. The final standalone proof uses the paper's actual typography and is checked separately from the mathematical certificate.
''')
excluded={'ledger/e_inert_tail_manifest.json','code/e_inert_tail_freeze.out'}
manifest={'statement':'E.114','files':[]}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in excluded:continue
    manifest['files'].append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
save('e_inert_tail_manifest.json',manifest)
print(json.dumps({'statement':'E.114','status':'AUTHOR_FREEZE_PASS','file_count':len(manifest['files']),
 'section_sha256':sha(proof),'program_sha256':sha(code),
 'GP_sha256':sha(ROOT/'code/e_inert_tail_orbit.gp'),'JSON_sha256':sha(summary),
 'manifest_sha256':sha(LEDGER/'e_inert_tail_manifest.json')},indent=2))
