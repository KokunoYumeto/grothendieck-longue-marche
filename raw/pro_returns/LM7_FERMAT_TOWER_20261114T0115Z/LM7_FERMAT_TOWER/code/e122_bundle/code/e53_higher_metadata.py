"""Record E122's exact mathematical, execution, source and scope metadata."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];L=R/'ledger';L.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):(L/name).write_text(json.dumps(data,indent=2)+'\n')
result=[{'id':'E.122','status':'Proved',
 'statement':'For beta_d^(3^d)=53*zeta3, B_d=Q(zeta9,beta_d) and S over3,53, every vertical three-primary S-class action is trivial. All actual norms A(B_(d+1))->A(B_d) are isomorphisms from d=2 onward, and the full groups and inverse limit are C9+C3^3 through those norms. Every stable ideal extension is3 times that actual inverse. Three explicit additional S-unit characters, obtained from22 literal verified cube roots, kill the first remaining norm kernel. The complete first embedded S-unit norm image is the displayed six-row congruence lattice of index729, with an actual preimage map. Every later unit-norm cokernel is C3^9 and completed kernel is mu3 plus Z3 of rank2*3^(d+1), with the exact Hilbert90/class maps retained.',
 'where_proved':'sections/E_fiftythree_higher_action.tex, complete proof and E122.1--25; three exact GP stages, independent rational relative-ring verifier, finite-map certificate and full fresh replay.',
 'depends_on':['E.46','E.119','E.121','E_MilneCFT','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, through the actual positional root-cubing and Kummer--Shapiro maps of E46. Part E(c),(d), Item2 and Lead3.'],
 'depends_on_doubtful_reading':False,
 'notes':'The proof uses all-level Eisenstein/decomposition/normalizer maps and an exact kernel recursion; stability is not extrapolated from finite data. The literal roots are checked independently of their discovery. No upper BNF or upper unit-basis completeness assertion enters the theorem. Higher embedded norm subgroups retain the exact character plus Hilbert90 map; unrestricted intrinsic section lifting and other positional factors remain separate tasks.'}]
save('e_fiftythree_higher_results.json',result)
save('e_fiftythree_higher_coverage.json',{
 'statement':'E.122','addresses':[{'task':'Part E(c),(d), Item2 and Lead3 through the actual H quotient',
 'scope':'Evaluates the entire B_d positional53 S-class tower and all its finite unit-norm defect types; gives the complete first embedded norm subgroup and literal preimage.',
 'exact_maps':['beta_(d+1)^3=beta_d and actual ideal norms/extensions','Six actual local Artin maps with positive radical calibration','Class-field decomposition injection and norm-kernel recursion K_d=j_dK_(d-1)','Stable norm coordinates n_d:A_d->A_2 and their inverses','Twenty-two literal cube and relative norm identities in the degree54 relative ring','Six-row full first norm congruence map, quotient right inverse and actual preimage products','Actual outside-S Hilbert90 divisor map to A_(d+1)/j_dA_d and completed norm-kernel product coordinates']}],
 'closed_steps':['All higher B_d projection kernels, vertical actions and actual norms/extensions.','Full A_d and inverse-limit module, including the horizontal H action.','The embedded first N(U2) lattice and its actual preimage map.','All later finite unit norm-defect types, roots-of-unity norm kernel and free ranks.'],
 'remaining':['Complete norm-coherent unit/divisor fibres require the compatible positional inverse-system construction; no uncomputed coherence is replaced by the list of one-step quotients.','Other lower positional factors, including the separate L_d comparison and general inert primes, require their actual maps.','The intrinsic metabelian/marked section sets map to H by established quotient maps; this statement does not assert a lifting surjectivity.']})
save('e_fiftythree_higher_dependencies.json',{
 'portable_full_rebuild':'python code/e53_higher_maps.py --gp /absolute/path/to/gp',
 'fresh_copy_comparison':'python code/e53_higher_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path',
 'finite_recheck':'python code/e53_higher_maps.py',
 'independent_relative_ring':'python code/e53_literal_unit_ring.py',
 'layout':'python code/e53_higher_layout.py','freeze':'python code/e53_higher_freeze.py',
 'required_sources':['code/e53_higher_maps.py','code/e53_literal_unit_ring.py','code/e53_higher_local.gp','code/e53_higher_genus.gp','code/e53_upper_witness_verify.gp'],
 'required_inputs':['inputs/e119_e53_genus_transition.bin','inputs/e119_e53_genus_transition.out','inputs/e121_normalizer_module.json','inputs/e122_literal_unit_witnesses.json','inputs/e122_literal_unit_witnesses.txt'],
 'input_provenance':'The lower input-producing sources and complete upstream rebuild are in the frozen E119/E121 bundles. The two new witness files are literal rational coefficients whose complete identities are reverified; they are not asserted as an upper fundamental-unit basis. Discovery sources and actual outputs are all retained.',
 'upstream_rebuild':'E119: python code/e_lower_fiftythree.py --gp /absolute/path/to/gp; E121: python code/e53_normalizer_module.py --gp /absolute/path/to/gp',
 'expected_text_outputs':['code/e53_higher_local.out','code/e53_higher_genus.out','code/e53_upper_witness_verify.out','code/e53_literal_unit_ring.out','code/e53_literal_unit_ring.json','code/e53_higher_maps.out','code/e53_higher_maps.json'],
 'expected_complete_binary_outputs':['code/e53_higher_local.bin','code/e53_higher_genus.bin','code/e53_upper_witness_verify.bin'],
 'python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'serialization':'Integer exports assert integrality. Rational matrices use exact strings and decode equality. Complete PARI GEN objects are compared by ===, with no component exclusions; raw serialization headers may differ.',
 'optional_discovery_reconstruction':'The candidate/root-search GP programs retain their actual inputs, outputs and checkpoint stream. They are not required for the minimal theorem replay, which checks every literal witness directly.'})
save('e_fiftythree_higher_source_evidence.json',{
 'statement':'E.122','read_scope':'Exact primary passages were opened and read in this conversation and in the retained E119/E121 work. The final certificate uses their explicit maps; no omitted source proof is represented as read.',
 'sources':[{'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
 'opened_passages':['III2.4 logarithm/exponential range and proof; III3.1 complete cup-product Res/Cor proof; III3.4 local norm-index theorem.','V3.3 complete ideal-norm/Frobenius square; V3.6 and Example3.9 Hilbert class field.','V5.2 complete product-of-local-reciprocity proof; Theorems5.3 and5.5; Example5.4 product formula.','VII3.1 full S-unit lattice/Herbrand argument and VIII3.1 complete cyclic Hasse-norm proof, retained through E119/E121.'],
 'actual_transfer':'Tate degree minus two is Galois abelianization; its restriction/corestriction give transfer/inclusion. The proved fundamental-class cup-product square identifies field inclusion with transfer and field norm with restriction in reciprocity. The product of these actual local maps gives the global idelic map. The proof then spells out the six decomposition injections and both class-field inclusions.',
 'precision':'Adjacent III Lemma3.2 prints Proof. To be added. Its omitted proof is not claimed as read; the argument uses the complete III3.1 cup-product proof.',
 'usage':'All-level norm surjectivity, local/global character maps, norm-kernel identification, logarithmic U^16 containment and the exact field-unit norm condition.'},
 {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html',
 'opened_passages':['Official idealstar/ideallog contracts and exact residue-unit inverse.','Official nfeltispower contract and rnfequation literal root maps, opened at turn1096view0--2 and local PARI2.19.0 doc/usersch3.tex.','Official BNF scope: uncertified candidate data supply only literal elements; E119 retains all required lower certification and saturation proof.'],
 'usage':'Final verification uses only literal polynomial arithmetic, actual ideal support in the smaller field, certified lower data and exact finite residue arithmetic. No upper BNF output is used as a class or unit-completeness theorem.'}],
 'author_review':'Complete proof and all owned mathematical sources read. Full fresh three-GP plus independent relative-ring/finite-map replay passes with all complete text bytes and all three complete decoded GEN objects identical, no exclusions.',
 'root_status':'Root read the complete preliminary all-level proof, all final literal witness sources, and independently replayed the frozen minimal subset. All complete subset outputs and Python JSON are byte-identical, no exclusions. The strengthened final proof is supplied for its final review; no unreceived final proof audit is claimed.',
 'peer_status':'No separate full E122 peer audit is claimed at this freeze.'})
history={'statement':'E.122','active_long_jobs':[],
 'prior_long_BNF_jobs':'The old17 jobs were stopped and retained in E101; no duplicate upper BNF was launched here.',
 'executions':[
 {'program':'e53_higher_local.gp','session_id':86063,'exit':0,'result':'Complete local degree9 norm subgroups; only stack warning.'},
 {'program':'e53_higher_genus.gp','session_id':69069,'exit':0,'result':'Exact cyclic-nine genus and reduction maps.'},
 {'program':'e53_upper_unit_candidates.gp','session_id':36739,'exit':0,'result':'Ten literal degree18 S-unit candidates, all divisors verified. Uncertified BNF class data unused.'},
 {'program':'e53_upper_unit_characters.gp','exit':0,'result':'All30 candidate conjugates add no character beyond rank2. This negative discovery result is retained.'},
 {'program':'history/initial_residue_denominator/e53_upper_residue_search.py','exit':1,'stdout':'history/initial_residue_denominator/e53_upper_residue_search.out','stderr':'history/initial_residue_denominator/e53_upper_residue_search.err','result':'Stopped at a prime dividing a power-basis denominator; no mathematical result inferred.'},
 {'program':'e53_upper_residue_search.py','exit':0,'result':'1161 actual finite embeddings, rank23; denominator primes explicitly skipped. Nullspace is only nominated root-test data.'},
 {'program':'e53_upper_exact_roots.gp','session_id':80325,'exit':0,'result':'All22 nominated products have literal verified cube roots. The binary output is an append-only stream of22 complete checkpoints.'},
 {'program':'history/initial_root_character_stream/e53_upper_root_characters.gp','exit':0,'stdout':'history/initial_root_character_stream/e53_upper_root_characters.out','stderr':'history/initial_root_character_stream/e53_upper_root_characters.err','result':'GP reported nonexistent component while reading the checkpoint stream as one object. Empty stdout and actual error retained; exit0 is not recorded as success.'},
 {'program':'e53_upper_root_characters.gp','exit':0,'result':'Correctly decodes the final checkpoint, exact rank5 local characters.'},
 {'program':'e53_upper_witness_export.gp','session_id':49077,'exit':0,'result':'Complete relative coefficients and lower norm coordinates; full index729 lattice.'},
 {'program':'e53_upper_witness_verify.gp','exit':0,'result':'Minimal fresh literal verification; no upper NF/BNF input.'},
 {'program':'e53_literal_unit_ring.py','exit':0,'result':'Independent exact rational field arithmetic, all22 cubes/norms, determinant−4 and norm lattice inverse.'},
 {'program':'e53_higher_replay.py','session_id':5162,'exit':0,'result':'All7 complete text outputs byte-identical, all3 full decoded PARI objects identical.'},
 {'program':'audit/initial_layout/code/e53_higher_layout.py','session_id':80805,'exit':1,'result':'Initial TeX matrix exceeded default ten-column limit; actual error/source/log retained.'},
 {'program':'e53_higher_layout.py','session_id':64292,'exit':0,'result':'Eight pages, no overfull boxes; all eight page images actually opened and reviewed.'},
 {'program':'history/initial_freeze_count/e53_higher_freeze.py','exit':1,'result':'The first metadata guard counted a TeX line-break optional argument as a display opener. Its actual source/stdout/error are retained; the guard was narrowed to full delimiter lines. No mathematical source or result changed.'}],
 'empty_stdout_records':'The two failed programs have genuinely empty stdout and nonempty retained stderr. These bytes are preserved, not replaced by invented output. The initial layout likewise records its actual error stream.',
 'arithmetic_subset_frozen':'ledger/e122_witness_subset_manifest.json'}
save('e_fiftythree_higher_computation_status.json',history)
layout=json.loads((R/'code/e53_higher_layout.json').read_text())
save('e_fiftythree_higher_visual_review.json',{'status':'PASS','reviewer':'bc_fermat','scope':'Every one of the eight final page images was individually opened at110dpi; formulas, matrices, endings and references are unclipped and legible. Automated layout reports no overfull boxes.','pages':8,'section_sha256':layout['section_sha256'],'PDF_sha256':layout['PDF_sha256']})
(L/'e_fiftythree_higher_refs.bib').write_text('% Reuses verified existing primary keys E_MilneCFT and E_PARICertifiedUnits.\n% No duplicate bibliography entries are introduced.\n')
report='''# E.122 — stable positional53 class tower

The entire B_d three-primary S-class tower is now evaluated. Every norm from level two onward is an actual isomorphism, identifying every group and the inverse limit with C9 ⊕ C3³. Under these literal norm coordinates, every vertical extension is multiplication by three and the horizontal action is the previously evaluated matrix H.

## Why the all-level conclusion follows

The proof first establishes the six actual totally ramified prime chains by Eisenstein equations. The class-field decomposition injections and the order-nine normalizer give vertical triviality on the entire class group. The exact norm-kernel recurrence is K_d = j_d K_(d−1), with the complete restriction diagram and lift ambiguity retained.

The missing initial kernel is then killed by actual units. Twenty-two products of forty-five literal S-units have exact cube roots. All roots and relative norms are checked twice: once in PARI's relative polynomial ring, once by an independently written rational ring implementation. Lower columns8,10 and roots8,14,20 give five local characters with determinant−4 on the first five rows. This fills the product-formula hyperplane, proving K2=0. The already proved recurrence propagates this exact vanishing to every later level.

## Embedded unit norm and inverse

The first norm image is exactly the six-row congruence lattice in E122.23. Its index is729. The nine selected root norms and six included lower cubes give a literal preimage basis with determinant94770 = 3⁶·130 and an exact rational inverse over Z3. All signs, the first root-of-unity coordinate, both lattice inclusions, a quotient right inverse and the preimage ambiguity are explicit.

At every later step the field-unit norm index is3⁵ and the exact Hilbert90 defect is A2/3A2 = C3⁴. The complete unit norm quotient is therefore C3⁹, since included cubes are norms. The literal torsion kernel is μ3; the completed free kernel rank is2·3^(d+1). Its basis/lift product isomorphism and inverse are stated. The higher embedded subgroup remains the actual local-character plus Hilbert90 map, not an uncomputed numerical unit basis.

## Verification and discovery records

The complete theorem replay needs only three GP sources, two Python sources, the certified lower E119 object and literal witness coefficients. It does not need an upper BNF or a root search. The full author fresh-copy replay compares every complete stdout/JSON byte and all three complete decoded PARI objects, with no exclusions. Root separately replayed the frozen minimal witness subset with identical complete outputs.

Discovery is retained separately: the smaller-field candidate lattice gave only rank two; finite-prime residue tests gave rank23 and nominated22 products; each product was then proved a cube by an exact identity. The denominator-prime failure, the checkpoint-stream decoding failure, and the initial TeX failure retain their actual source/output/error. No unsuccessful or finite search is used as a nonexistence argument.

## Remaining original scope

This theorem closes the B_d class projection kernels and evaluates its finite unit-norm defects. The compatible positional norm-coherent unit/divisor fibres, separate lower factors and the intrinsic lifting maps still require their exact further constructions. The full original E.23 is not marked complete by this one factor.

## Portable commands

```text
python code/e53_higher_maps.py --gp /absolute/path/to/gp
python code/e53_higher_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path
python code/e53_higher_layout.py
```

The standalone proof has eight pages. All eight final page images were actually opened and checked; the final layout has no overfull boxes.
'''
(L/'e_fiftythree_higher_report.md').write_text(report)
print(json.dumps({'status':'PASS','metadata_files':[p.name for p in sorted(L.glob('e_fiftythree_higher_*'))],
                  'proof_sha256':sha(R/'sections/E_fiftythree_higher_action.tex')},indent=2))
