#!/usr/bin/env python3
"""Write the exact E123 scope, provenance, replay and visual-review records."""
from pathlib import Path
import hashlib, json

R=Path(__file__).resolve().parents[1]
L=R/'ledger'; L.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,obj):
    (L/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

proof='sections/E_fiftythree_positional_stable.tex'
replay=json.loads((R/'code/e53_positional_replay.json').read_text())
finite=json.loads((R/'code/e53_positional_maps.json').read_text())
layout=json.loads((R/'code/e53_positional_layout.json').read_text())
assert replay['status']==finite['status']=='PASS'
assert replay['excluded_fields']==[] and layout['overfull']==[]
assert layout['section_sha256']==sha(R/proof)

put('e_fiftythree_positional_results.json',[{
 'id':'E.123','status':'Proved',
 'statement':'For beta_d^(3^d)=53*zeta3, L_d=Q(beta_d), B_d=L_d(zeta9), and S over3,53, every actual vertical three-primary S-class norm on L_d is an isomorphism from d=2, all classes are C9^2 and all extensions are3 times that inverse. The horizontal maps are the displayed complete matrices. All later vertical S-unit norm quotients are C3^3 and horizontal quotients C3, with actual Hilbert90 maps and completed kernels. The entire coherent divisor image of this positional factor is the kernel of a surjective restricted-support class map to C9^2, with literal prime basis31,103, an unconditional ideal-presentation certificate, explicit coordinates and inverse. Compact-fibre compatibility gives the complete factor as its coherent unit kernel times that divisor module, with literal total norm and a closed family of actual H-section classes.',
 'where_proved':proof+', complete proof and E123.1--26; eight final replayed mathematical stages including the no-input nf-only nine-ideal verifier.',
 'depends_on':['E.46','E.119','E.121','E.122','E_MilneCFT','E_KatoUniversalNorms','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, through E46 actual positional root-cubing/Kummer--Shapiro maps; Part E(c),(d), Item2 and Lead3.'],
 'depends_on_doubtful_reading':False,
 'notes':'The all-level statement uses actual horizontal class-field coinvariants and norm-surjectivity maps, not extrapolation. No upper-field BNF class-group or unit-basis assumption is used. The universal three-valuation functional, the other positional factors and further intrinsic lifting remain the explicit maps in E123.12/26; no complete E23 claim is made. The all-prime algorithm projects to the three-primary subgroup using m=1 mod9 and full ideal equalities.'
}])

put('e_fiftythree_positional_coverage.json',{
 'statement':'E.123',
 'addresses':[{'task':'Part E(c),(d), Item2 and Lead3 through the established actual H quotient',
  'scope':'The entire j=1 positional53 factor: stable actual S-class norms, all later one-step unit quotients, full coherent divisor image, product coordinates and an actual closed section family.',
  'exact_maps':['Horizontal class-field inclusion and coinvariant norm sequence E123.14--15',
   'Actual stable norms m_d and extensions3*m_d inverse E123.2',
   'Complete horizontal norm/extension matrices and positive Artin map E123.3',
   'Literal horizontal norm of v20, positive characters(2,1), local cup-product corestriction E123.17--19',
   'Both directions of the outside-S Hilbert90 defect map E123.20--21',
   'Literal prime31/103 ideals, principal corrections, complete relation and inverse matrices E123.22--24',
   'Uniform finite-node orbit norm weights and exact restricted class map',
   'Compact-fibre coherent lift and convergent basis product with inverse E123.9--11',
   'Actual rational total norm, factor map, cube condition and scaled toric projection E123.12--13/26'] }],
 'closed_steps':['All higher L_d three-primary S-class groups, vertical actions, actual norms and extensions.',
  'All later vertical/horizontal finite S-unit norm-defect types and completed kernel maps.',
  'The complete coherent divisor image, with an actual finite prime basis and exact topology.',
  'The full positional factor expressed by actual coherent lifts and its literal rational norm.',
  'A closed restricted-support family of actual H-section classes and its inverse.'],
 'remaining':['The universal valuation functional nu3 on the coherent unit kernel is retained as an actual map; its numerical image and phase are not assigned by one-step norm data.',
  'Other positional factors on general first-coordinate lines remain in the explicit total-norm equation E123.26.',
  'The actual quotient maps from intrinsic metabelian/marked groups to H are retained; this theorem proves no additional intrinsic lifting surjectivity.']
})

put('e_fiftythree_positional_dependencies.json',{
 'portable_full_replay':'In a fresh copy: python code/e53_positional_replay.py --gp /absolute/path/to/gp --label fresh_audit',
 'standalone_no_input':'In an empty directory: /absolute/path/to/gp -q -f /absolute/path/to/code/e53_positional_ideals.gp',
 'standalone_literal_norm':'In an empty directory: /absolute/path/to/gp -q -f /absolute/path/to/code/e53_positional_verify.gp',
 'finite_recheck':'python code/e53_positional_maps.py',
 'independent_literal_ring':'python code/e53_positional_unit.py',
 'layout':'python code/e53_positional_layout.py',
 'freeze':'python code/e53_positional_freeze.py',
 'mathematical_sources':list(replay['source_hashes']),
 'required_inputs':['inputs/e122_literal_unit_witnesses.json','inputs/e122_literal_unit_ring.json',
  'inputs/e121_normalizer_module.json','inputs/e119_positional_genus_transition.bin','inputs/e122_L2_candidate_bnf.bin'],
 'input_scope':{'e119_positional_genus_transition.bin':'Fully certified lower-field unit/ideal data and exact local Artin/Smith maps from frozen E119.',
  'e122_L2_candidate_bnf.bin':'Uncertified discovery object used only to propose exact principal-ideal witnesses. No mathematical class or unit assertion is read from it. The separate no-input verifier reconstructs and checks every used ideal identity.',
  'e122_literal_unit_witnesses.json':'Literal coefficients of v20; full cube and relative norm checked independently.',
  'e121_normalizer_module.json':'Actual finite class maps and proved order81 lower bound.'},
 'expected_text_outputs':[str(Path('code')/(Path(n).stem+'.out')) for n in replay['source_hashes']],
 'expected_JSON':['code/e53_positional_unit.json','code/e53_positional_maps.json'],
 'expected_binary':['code/e53_positional_genus_pivots.bin','code/e53_positional_presentation.bin'],
 'python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'serialization':'Exact rational-string matrices with decode equality; integer conversion asserts integrality. Entire decoded PARI objects compared with ===; no component exclusions. The retained append-container amendment proves [B,B] -> B with inverse B -> [B,B].',
 'replay_precaution':'Use a fresh copy or the replay driver. PARI writebin appends when a producing GP stage is run repeatedly in the same directory; all reference-container history is preserved.',
 'expensive_search':'No BNF reconstruction or certification is run by the final eight-stage replay.'
})

put('e_fiftythree_positional_source_evidence.json',{
 'statement':'E.123',
 'sources':[{
  'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
  'edition':'v4.03',
  'opened_passages':['III3.1 complete fundamental-class cup-product restriction/corestriction proof, retained through E119--E122.',
   'V3.3 complete ideal-norm/Frobenius square proof; V3.6 and Example3.9 Hilbert class field.',
   'V5.2 product of local reciprocity maps and proof; V5.4 is the Hilbert-symbol product-formula example, while existence is V5.5.',
   'VII3.1 S-unit lattice/Herbrand proof; VIII3.1 complete cyclic Hasse-norm proof; VIII7.4 Chebotarev proof retained in E119--E122.'],
  'fresh_retrievals':['turn1117view4: V3.3 proof','turn1117view5: VIII3.1 proof','turn1116view5: Example3.9'],
  'actual_transfer':'Tate cohomology degree minus two identifies the group with Galois abelianization. Its restriction/corestriction maps are transfer/inclusion. The proved fundamental-class cup-product compatibility identifies field inclusion with transfer and field norm with restriction. Product of these local maps gives the global Artin map; the theorem spells out the horizontal coinvariant sequence and the Frobenius norm-surjectivity construction.',
  'omitted_proof_precision':'III Lemma3.2 literally says Proof. To be added. No reading of an absent proof is claimed; the complete III3.1 cup-product proof supplies the compatibility used.'},
  {'key':'E_KatoUniversalNorms','url':'https://ems.press/content/book-chapter-files/27477',
   'opened_passages':['Definition of the coherent norm image on printed page551 and Theorem1.1(2), page552.',
    'Sections2.2--2.3, Proposition4.2, proof Sections4.4--4.6 and Sections5.1--5.2, read in the retained E69/E110 source work and reopened in this continuation.'],
   'fresh_retrievals':['turn1128view0','turn1128view1'],
   'actual_transfer':'Apply the one-place theorem to F=L_d and F(mu_3-infinity,53^(1/3-infinity)); restrict the actual norm-compatible family to the cofinal positional fields L_e. Its image in the d-th S-unit group contains the finite-index coherent three-unit image of rank3^d. Only that proved rank consequence is used; no index is assigned.'},
  {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/dochtml/html/General_number_fields.html',
   'opened_passages':['Official nf/BNF distinction and exact bnfcertify flag0/flag1 scope.',
    'nfinit with supplied integral basis and prime list; nfcertify empty-list unconditional integral-basis certificate; exact ideal HNF and ideal arithmetic contracts.'],
   'fresh_retrievals':['turn1132view0','turn1133view0','turn1133view1','turn1134view0'],
   'actual_transfer':'The final independent no-input verifier performs only nf arithmetic. The saved BNF object proposes seven upper ideal equalities, all reconstructed and checked independently; the proved order81 plus independently witnessed pivot basis supplies the class-group conclusion.'}],
 'author_scope':'Complete proof and all eight final mathematical sources read; fresh complete copied-source replay and actual eight-page visual review passed.',
 'root_scope_at_freeze':'Root read the draft class-field, Hilbert90, local-character, ideal-presentation and section arguments and requested the uniform finite-node branch clarification, now included. No unreceived final whole-proof or replay audit is claimed.',
 'peer_scope_at_freeze':'No separate full E123 peer review has yet been claimed.'
})

put('e_fiftythree_positional_computation_status.json',{
 'statement':'E.123','final_status':'PASS','replay':'code/e53_positional_replay.json',
 'whole_text_and_JSON_identity':True,'complete_GEN_identity':[4,13],'excluded_fields':[],
 'counts':{'complete_literal_ideal_equalities':9,'upper_presentation_equalities':7,
  'Smith_roundtrips':finite['Smith_roundtrips'],'finite_branch_primes':finite['finite_branch_primes_checked'],
  'eligible_prime_records':len(finite['eligible_prime_records']),
  'divisor_inverse_tests':finite['divisor_coordinate_inverse_tests'],
  'scaled_toric_inverse_tests':finite['raw_scaled_toric_inverse_tests']},
 'actual_attempts':[{'path':'code/e53_positional_pivots.gp','status':'Stopped','exit_code':124,'seconds':180,
   'actual_outputs':['code/e53_positional_pivots.out','code/e53_positional_pivots.err'],
   'scope':'Saved candidate loaded; bnfcertify(B,1) did not return. No class or unit conclusion follows.'},
  {'path':'code/history/initial_input_inspection','status':'Retained actual failure','reason':'list/dictionary inspection mismatch; no mathematics changed.'},
  {'path':'code/history/initial_gp_verify','status':'Retained actual failure','reason':'Initial GP API error; exact corrected standalone norm verification retained.'},
  {'path':'code/history/first_finite_checker','status':'Retained actual failure','reason':'Expected JSON instead of the actual standalone PASS lines; mathematical checks rerun.'},
  {'path':'audit/author_replay','status':'Retained actual failure','reason':'All eight mathematical stages passed; complete binary comparison exceeded its initial 8MB stack.'},
  {'path':'audit/author_replay_final','status':'Retained actual failure','reason':'All eight mathematical stages passed; reference writebin file had two identical records. Exact whole-record verification and actual projection/inverse are retained.'},
  {'path':'audit/binary_reference_amendment','status':'Proved container amendment','reason':'Both complete old13-component records equal the fresh object. Original bytes preserved; no numerical field changed.'},
  {'path':'code/history/primary_projection_initial','status':'Retained actual failure','reason':'Text-match assertion failed before the theorem write; exact emitted stderr and old source retained.'}],
 'active_expensive_BNF_jobs':[],'active_final_replay_jobs':[],
 'all_level_scope':'All infinite-level conclusions are proved using exact field, class, norm, character and compactness maps. The finite certificates are not substituted for those proofs.'
})

visual={'status':'PASS','statement':'E.123','pages':8,
 'section_sha256':sha(R/proof),'PDF_sha256':sha(R/'qa/e123_standalone.pdf'),
 'images':[{'page':i,'file':f'qa/page-{i}.png','sha256':sha(R/f'qa/page-{i}.png'),'actually_viewed':True} for i in range(1,9)],
 'scope':'All eight actual page images viewed. Pages6--8 rereviewed after the exact three-primary projection paragraph amendment; pages1--5 unchanged from the reviewed version.',
 'automated_overfull':layout['overfull'],'clipped_or_overlapping_content':False}
for i in range(1,6):
    assert (R/f'qa/page-{i}.png').read_bytes()==(R/f'audit/pre_primary_projection/qa/page-{i}.png').read_bytes()
put('e_fiftythree_positional_visual_review.json',visual)

(L/'e_fiftythree_positional_refs.bib').write_text(
 '% Reuses existing keys E_MilneCFT, E_KatoUniversalNorms and E_PARICertifiedUnits.\n'
 '% verified: exact source passages and proof scope are in e_fiftythree_positional_source_evidence.json.\n'
 '% No duplicate bibliography entries are introduced.\n')

report=r'''# E.123 — the positional 53 factor

The actual fields are `L_d=Q(beta_d)`, `beta_d^(3^d)=53*zeta3`, and `B_d=L_d(zeta9)`. For every `d>=2`, the three-primary S-class norm on `L_(d+1)/L_d` is an isomorphism onto `C9^2`; extension is three times that actual inverse. The horizontal class-field coinvariant sequence supplies the order81 at every level, and the ramified vertical extension is disjoint from the S-Hilbert class field. The proof retains the resulting Frobenius norm map, the horizontal matrices and the positive Artin character.

The literal horizontal norm of E122's root20 has absolute norm `27/53^2` and positive characters `(2,1)` at `(3,53)`. Its included character persists by the actual local cup-product corestriction square. This evaluates all later vertical S-unit norm quotients as `C3^3`, horizontal quotients as `C3`, and both completed kernels through the explicit Hilbert–90 divisor map. The local equality `L_2,w=B_2,v=Q_3(mu27)` is retained separately from the literal global roots of unity.

The complete coherent divisor image is the kernel of the restricted-support class map to `C9^2`. The actual surviving degree-one primes at31 and103 form a basis. Their lower idele columns, full principal corrections, upper HNF ideals and seven complete upper ideal relations are retained. The independent no-input GP verifier reconstructs both fields and verifies all nine lower/upper identities using only nf arithmetic. The candidate upper BNF is used only to propose witnesses. The proved order81 and independently witnessed prime basis certify the entire three-primary S-class subgroup. For other primes, the terminating coordinate search also enumerates `m=1 mod9`; it thereby kills the prime-to-three part while leaving the required coordinate unchanged.

The nonfixed-branch argument is uniform on every finite node: after refining a ball away from the affine fixed point, the distance valuation is constant, and the three-part of the orbit length is `3^max(0,m-s-t)`. Deep norm weights therefore force every such coherent mass to vanish. Compact fibres of the completed principal-divisor map give compatible all-level lifts without assuming that the unit norm maps are onto. Literal convergent products and division give the product decomposition and its inverse. The coherent unit kernel is a countable product of `Z3` through the stated character construction; its rational norm is retained as the actual two valuation maps.

The factor is inserted into E46 by its actual Kummer–Shapiro map. Cubing a chosen coherent divisor lift and setting the other factors to one gives a closed family of H-section classes, with the displayed scaled toric map and inverse outside-S divisor divided by three. The subgroup is `3D`; no replacement by `D intersect 3R` is made. The universal three-valuation image/phase, other positional factors and further intrinsic lifting remain explicit outstanding maps.

## Executed verification

The fresh eight-stage copied-source replay passes with complete stdout/stderr and both JSON files byte-identical. The generated standalone source is byte-identical. Both entire decoded PARI objects are identical, of4 and13 components, with no exclusions. Raw binary serialization differs and is not used as mathematical equality. The earlier reference file with two appended identical records is preserved; the exact map `[B,B] -> B` and inverse `B -> [B,B]` were checked on both complete records.

The certificate checks81 Smith roundtrips,194 prime-branch cases,52 eligible prime records,6561 divisor inverses and6561 scaled toric inverses. All eight rendered pages were actually viewed; no overfull, clipped or overlapping content remains.

## Replay

In a fresh copy, run:

```
python code/e53_positional_replay.py --gp /absolute/path/to/gp --label fresh_audit
```

The two independent no-input checks may be run from an empty directory:

```
/absolute/path/to/gp -q -f /absolute/path/to/code/e53_positional_ideals.gp
/absolute/path/to/gp -q -f /absolute/path/to/code/e53_positional_verify.gp
```

The final replay performs no BNF reconstruction or certification. All stopped/failed attempts and their actual outputs are retained in `code/history` and `audit`, including the180-second flag-one timeout. No inference is made from that timeout.

## Review scope

The author read the complete proof and all final sources and completed the fresh replay and visual review. Root has read the main draft arguments and requested the uniform finite-node clarification, now supplied. A final root whole-proof/replay audit and a separate peer audit are not represented as already received.
'''
(L/'e_fiftythree_positional_report.md').write_text(report)

print(json.dumps({'status':'PASS','statement':'E.123','proof_sha256':sha(R/proof),
 'metadata_files':sorted(p.name for p in L.iterdir() if p.is_file()),
 'whole_replay':'PASS','visual_pages_actually_viewed':8},indent=2))
