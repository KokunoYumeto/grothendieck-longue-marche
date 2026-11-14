#!/usr/bin/env python3
"""Freeze E111's actual arithmetic, complete proof and portable outputs."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/'ledger'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(LEDGER/name).write_text(json.dumps(obj,indent=2)+'\n')
proof=ROOT/'sections/E_nonunit_seventeen.tex'
code=ROOT/'code/e_nonunit_seventeen.py'
summary=ROOT/'code/e_nonunit_seventeen.json'
d=json.loads(summary.read_text())
assert d['status']=='PASS'
assert summary.read_bytes()==(ROOT/'code/e_nonunit_seventeen.out').read_bytes()
assert d['actual_GP_record_count']==13
assert d['all_character_inverse_checks']==54
assert d['all_S_unit_character_normalizations']==4374
assert d['adjacent_prime_chain_checks']==1164
assert d['integral_toric_inverse_checks']==50000
tex=proof.read_text()
assert [int(x) for x in re.findall(r'\\tag\{E111\.(\d+)\}',tex)]==list(range(1,26))
assert len(re.findall(r'(?m)^\\\[$',tex))==len(re.findall(r'(?m)^\\\]$',tex))==25
assert not any(ord(c)<32 and c not in '\n\t' for c in tex)
for name,h in d['source_hashes'].items():assert sha(ROOT/'code'/name)==h

save('e_nonunit_seventeen_results.json',[{
 'id':'E.111','status':'Proved',
 'statement':'For every j>=2 and m>=0, the three-primary S-class group of Q(zeta_(3^j),(17*zeta_(3^j))^(1/3^m)), S above3,17, is zero. Every adjacent S-unit norm quotient is the explicitly evaluated four-place sum-zero C3^3 with actual character inverse matrices. Every compatible outside-S divisor lifts coherently; the entire factor is a split product of the restricted divisor module at primes with v3(ord_p17)=j and a countably infinite compact product of Z3. Combining these exact positional factors with E110 evaluates the complete global H section set for every nonzero first class r*kappa3(17): its second toric support is precisely {3,17} and the primes with v3(ord_p17)<=v3(r)+1, and every fiber has the displayed actual inverse coordinates. E47 supplies r=0.',
 'where_proved':'sections/E_nonunit_seventeen.tex, E111.1--25 and complete proof; code/e_nonunit_seventeen.py and e_nonunit_seventeen_base.gp with their complete outputs and retained five-component PARI object.',
 'depends_on':['E.38','E.46','E.47','E.107','E.110','E_MilneCFT','E_LemmermeyerAmbiguous','E_KatoUniversalNorms'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379, via the actual positional norms and scaled toric maps.'],
 'depends_on_doubtful_reading':False,
 'notes':'The additional S-class induction uses the actual four totally ramified places, two calibrated Hilbert-character matrices, the exact local norm/corestriction square, and the S-unit/ideal Hilbert90 sequences. Compactness is used only for unit fibers. The complete H fibers use actual initial S-valuations and explicit pure-factor compensation; no separate uncomputed ordinary-class exponent is assumed. The intrinsic metabelian and marked image remains the further lifting problem through E38.'
}])
save('e_nonunit_seventeen_coverage.json',{
 'statement':'E.111',
 'addresses':[{'task':'Part E(c),(d), Item2/Lead3 through the actual H quotient',
  'status':'Complete entire first-coordinate Z3*kappa3(17) line in H, using E47 at zero and E110 at unit multiples',
  'exact_maps':['Actual cofinal polynomial factorization and root-cubing norm maps.',
   'Local Kummer corestriction with literal radicand norms and no degree multiplier.',
   'Actual S-class capitulation/Hilbert90 map and field-norm-to-S-unit-norm comparison.',
   'Completed principal outside-S divisor map, compact-fiber coherent lifting and restricted product splitting.',
   'Finite S-unit character direct limit under actual transposed norm matrices, with its product coordinate inverse.',
   'Initial-field S-valuations and their residue-degree rational norm.',
   'Two pure valuation corrections that make the total norm exactly the cube of every displayed toric input.',
   'Kummer-Shapiro inverse and arithmetic H automorphism for the unit part of r.']}],
 'closed_previous_steps':['Every nonunit multiple of kappa17 left by E110 is evaluated completely in H.',
  'All additional positional S-class obstructions vanish by proof at every height.',
  'All their outside-S inverse divisor systems and their compact fibers are evaluated.',
  'The toric second-coordinate image has no remaining compatibility or phase condition beyond the displayed support.'],
 'remaining':['The full intrinsic metabelian/marked-depth image above these H sections remains an exact quotient-lifting problem in E23.',
  'First classes outside the already evaluated families are separate. The new general inert-prime tail is reserved for E114 and is not asserted in E111.',
  'Individual higher ordinary class groups and the separate finite-level projection images of each added coherent S-unit group are not numerically enumerated; the full H normal form requires only its proved compact product maps and actual initial valuations.']
})
save('e_nonunit_seventeen_source_evidence.json',{
 'statement':'E.111',
 'sources':[
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'opened_passages':['VII Proposition3.1, printed pp208--209, statement and full logarithmic/permutation-lattice proof: turn963view0--1 and turn967view0.',
    'III Section2 formulas29,30 and complete invariant/corestriction proof: turn963view3.',
    'III Theorem3.1 and its proved Res/Cor cup-product compatibility: turn963view4.',
    'VIII Theorem3.1, entire cyclic Hasse norm proof: turn963view2.'],
   'usage':'The four-place S-unit Herbrand quotient27, exact common-root Kummer norm square and cyclic field-norm zero criterion.',
   'precision':'III Lemma3.2 is not described as having a printed complete proof; the actual argument uses the proved cup-product and invariant compatibilities.'},
  {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
   'opened_passages':['Theorem1 and Proposition1 with its actual ideal/Hilbert90 proof: turn948view1; full ideal/Herbrand proof already opened and read for E110.'],
   'usage':'Cyclotomic base three-class vanishing. The new S-class exact sequence is proved directly in E111.21--25, with its actual divisor map.'},
  {'key':'E_KatoUniversalNorms','url':'https://ems.press/content/book-chapter-files/27477',
   'opened_passages':['Coherent-norm definition and Theorem1.1(2): turn948view2.',
    'Unconditional rank and cohomological comparison in Section3.2: turn967view1.',
    'Corollary5.2 and the full concluding proof Sections5.4--5.5: turn967view2--3.',
    'Proposition4.2 and complete Sections4.3--4.6 were already read for E69/E110.'],
   'usage':'Unbounded actual projections of coherent three-unit systems into the added factors, each of which has one place over3. The exact restriction map to the literal positional chain is stated.'}
 ],
 'internal_inputs':['E46 actual Kummer-Shapiro and total norm cube condition.',
  'E107 actual complex phase and recursive coherent unit coordinates.',
  'E110 complete pure divisor splitting, compact unit inverse and two-prime rational norm.'],
 'actual_computation':'PASS: the small certified degree-six K2 basis, complete local residue/unit divisions and all polynomial/coordinate checks are retained. No larger BNF is used.',
 'peer_status':'Full draft sent to a_structure; independent E111 audit pending at author freeze.',
 'root_status':'Root has received the complete proof and PASS outputs; independent E111 audit pending at author freeze.'
})
save('e_nonunit_seventeen_dependencies.json',{
 'portable_full_rebuild':'python code/e_nonunit_seventeen.py --gp /absolute/path/to/gp',
 'existing_workspace_command':'python research_e111/code/e_nonunit_seventeen.py --gp research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck':'python code/e_nonunit_seventeen.py',
 'Python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'actual_binary':'code/e_nonunit_seventeen_base.bin',
 'complete_binary_contents':'[certified K2 BNF, xi, seven actual S-unit columns, actual3 primes, actual17 primes]',
 'required_rebuild_sources':['code/e_nonunit_seventeen.py','code/e_nonunit_seventeen_base.gp'],
 'reference_input':'inputs/e111_complex_prime_classes.out retains the E107 phase table used in the proof; the new main certificate is self-contained and does not read that file.',
 'history':'All exploratory sources and actual outputs are in code/history. The two inline Python attempts were materialized verbatim from their actual tool invocations, with their actual stdout. The old character inverse uses its original workspace-relative evidence path; the final main source is portable.',
 'old_BNF_status':'Original superseded sessions24024 and40565 were stopped with actual exit130 and retained in E101. Neither was restarted. Only the new small degree6 K2 certification ran.'
})
save('e_nonunit_seventeen_computation_status.json',{
 'statement':'E.111','status':'PASS','actual_final_exit_code':0,
 'main':'code/e_nonunit_seventeen.py','stdout':'code/e_nonunit_seventeen.out','JSON':'code/e_nonunit_seventeen.json',
 'GP':'code/e_nonunit_seventeen_base.gp','GP_stdout':'code/e_nonunit_seventeen_base_gp.out',
 'certification':'bnfcertify default flag0, return value1',
 'actual_GP_records':13,'all_character_inverse_checks':54,'all_S_unit_normalizations':4374,
 'exact_polynomial_norms':10,'positional_factorizations':12,'ramification_rank_rows':63,
 'rational_primes':194,'actual_degree_one_prime_transitions':1164,'complete_toric_inverse_checks':50000,
 'failed_mathematical_runs':[],
 'corrected_initial_comparison':'The apparent conflict with old B1 was resolved before making a claim: B1=K2(cuberoot17) has a split3-prime and Herbrand quotient9, while the new radicand17*xi has four totally ramified places and quotient27. The proof retains the exact fields/place modules.',
 'scope':'The program verifies actual finite arithmetic and identities. All-level S-class vanishing, completed inverse-system surjectivity and the complete section maps are mathematical proofs, not extrapolations from a finite table.'
})
(LEDGER/'e_nonunit_seventeen_refs.bib').write_text('% verified: E111 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_KatoUniversalNorms; exact freshly opened proof passages are recorded in e_nonunit_seventeen_source_evidence.json. No duplicate bibliography keys.\n')
(LEDGER/'e_nonunit_seventeen_report.md').write_text('''# E.111 — The complete nonzero seventeen line in H

Every nonzero first coordinate r*kappa3(17) is now evaluated in the actual H quotient. If r=3^k*u with u a three-adic unit, the second toric image consists exactly of arbitrary coefficients at3 and17 together with restricted coefficients at primes p for which v3(ord_p17)<=k+1. There is no additional global phase equation on this full image. E47 covers the zero first coordinate.

## All added arithmetic factors

At cofinal positional height n=m+k+1 the actual etale algebra splits into the pure F_m, the former complex L_m, and K_j((17*zeta_(3^j))^(1/3^m)) for2<=j<=k+1. The polynomial and the root-cubing inclusions are displayed, so every factor has its genuine norm transition.

Each added factor has one three-prime and three seventeen-primes, all totally ramified vertically. The small certified field Q(zeta9) supplies seven explicit S-unit columns. Their four cubic characters have image the complete sum-zero C3^3, with explicit three-prime-generator inverse matrices. At j>=3 the actual radicand norm to Q(zeta9) becomes zeta9 modulo cubes, whose second evaluated matrix has the same full image. The corestriction projection formula retains the exact characters at every vertical level, without multiplying by the local degree.

The completed S-class groups are zero at every height. The proof uses the actual capitulation/Hilbert90 isomorphism, the S-unit Herbrand quotient27, the Hasse norm kernel and the exact invariant-divisor sequence. It proves the entire adjacent S-unit norm cokernel C3^3, rather than only a necessary local condition. The old K2(cuberoot17) comparison is explicitly resolved by its split three-prime and Herbrand quotient9.

## Exact full factors and section inverse

Every compatible outside-S divisor lifts coherently by compactness of its completed S-unit fibers. The surviving prime chains are exactly the unique degree-one branches at P_j. Thus the full factor is U_j times the restricted divisor module R(P_j), with actual product splitting and its exact choice-change map. U_j is an infinite countable product of Z3; finite S-unit characters and transposed actual norms specify its coordinate map and inverse. Kato's one-three-place theorem supplies unbounded actual finite-level projections.

For each chosen U_j element, the two rational S-norm exponents are read from its initial K_j coordinate: the normalized three valuation and the sum of seventeen valuations weighted by2*3^(j-2). The added outside-prime generators contribute their equally explicit initial valuations. These values need no separate universal-unit projection membership computation: the pure factor absorbs them.

For any requested second toric input, choose arbitrary b,z,B,k_F,k_L and arbitrary y_j in every added compact U_j. Set t_j=3*r|P_j, read n_j3,n_j17 from the exact norm, and put

    e=3*B17-2*b-sum n_j17,
    C=3*B3-3*z+sum ell_p*r_p-sum n_j3-B.

The pure element s_F(B,C,e,3*r|P0), the exact complex E107 element and all added y_j*s_j(t_j) have total rational norm exactly the cube of the target. Reading the independent factor coordinates gives the stated inverse. Every nonempty fiber is Z3^3 times the pure compact unit product, the old complex base-zero unit product, and the added U_j products. The unit part u of the first class is transported by the exact arithmetic H automorphism (a,v(T))->(u*a,v(T^u)).

The example p19 explicitly produces toric pair (3*kappa17,kappa19), with the two actual pure S-valuation corrections. E110's first kappa17 image excludes that second coordinate, and the displayed positional maps prove this comparison.

## Rebuild and remaining scope

    python code/e_nonunit_seventeen.py --gp /absolute/path/to/gp

The complete output includes13 certified GP records,54 inverse character maps,4374 S-unit normalizations,10 exact norms,12 positional factorizations,194 primes and1164 actual root-chain transitions, and50000 complete raw/scaled toric inverses. The full five-component PARI object is retained. No upper BNF was run or restarted.

The result is complete for the full seventeen line in H. The image of the intrinsic metabelian and marked section sets is still governed by their actual quotient kernels; no intrinsic lift is inferred. Other first-coordinate classes and the separately reserved general inert-prime tail are outside this theorem.
''')
manifest={'statement':'E.111','files':[]}
excluded={'ledger/e_nonunit_seventeen_manifest.json','code/e_nonunit_seventeen_freeze.out'}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in excluded:continue
    manifest['files'].append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
save('e_nonunit_seventeen_manifest.json',manifest)
print(json.dumps({'statement':'E.111','status':'AUTHOR_FREEZE_PASS','file_count':len(manifest['files']),
 'section_sha256':sha(proof),'program_sha256':sha(code),
 'GP_sha256':sha(ROOT/'code/e_nonunit_seventeen_base.gp'),'JSON_sha256':sha(summary),
 'manifest_sha256':sha(LEDGER/'e_nonunit_seventeen_manifest.json'),
 'complete_scope':'The entire nonzero first-coordinate kappa17 line in H, with all toric images and fibers.'},indent=2))
