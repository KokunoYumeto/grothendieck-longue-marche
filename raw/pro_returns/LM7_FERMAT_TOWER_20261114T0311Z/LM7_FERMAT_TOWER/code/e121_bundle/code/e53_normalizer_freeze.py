#!/usr/bin/env python3
"""Freeze E121's complete proof, exact arithmetic outputs and replay scope."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'ledger';LEDGER.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    (LEDGER/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
proof=ROOT/'sections/E_fiftythree_normalizer.tex'
data=json.loads((ROOT/'code/e53_normalizer_module.json').read_text())
replay=json.loads((ROOT/'code/e53_normalizer_replay.json').read_text())
layout=json.loads((ROOT/'code/e53_normalizer_layout.json').read_text())
inputs=json.loads((ROOT/'inputs/manifest.json').read_text())
amendment=json.loads((ROOT/'audit/e121_final_typing.json').read_text())
assert amendment['status']=='PASS' and amendment['after_proof_sha256']==sha(proof)
for rel,digest in amendment['unchanged_mathematical_files'].items():
    assert sha(ROOT/rel)==digest,rel
assert data['status']==replay['status']=='PASS'
assert layout['status']=='LAYOUT_PASS' and layout['section_sha256']==sha(proof)
assert replay['excluded_fields']==replay['excluded_binary_components']==[]
for row in inputs['files']:
    assert sha(ROOT/row['path'])==row['sha256'],row['path']
for rel,d in replay['text_outputs'].items():
    assert d['byte_identical'] and sha(ROOT/rel)==d['sha256']
for rel,d in replay['binary_objects'].items():
    assert d['complete_decoded_GEN_identical'] and sha(ROOT/rel)==d['author_sha256']
assert len(re.findall(r'\\begin\{statement\}\{E\.121\}',proof.read_text()))==1
assert not [ord(c) for c in proof.read_text() if ord(c)<32 and c not in '\n\t\r']

save('e_fiftythree_normalizer_results.json',[{
 'id':'E.121','status':'Proved',
 'statement':'For the actual positional fields beta1^3=53*zeta3, beta2^3=beta1, Li=Q(betai), Bi=Li(zeta9), the entire three-primary S-class groups at S={3,53} are A(B2)=C9+C3^3 and A(L2)=C9^2. The actual vertical action is identity on A(B2) and the matrix [[1,3],[0,1]] on A(L2). All vertical/horizontal ideal norms and extensions, full capitulation groups, the cyclic-nine and simultaneous normalizer quotients, the literal normal-closure Artin character and all three completed S-unit norm defect types and kernel types are evaluated.',
 'where_proved':'sections/E_fiftythree_normalizer.tex, E121.1--20 and complete proof; code/e53_normalizer_module.py, five actual GP stages, exact full outputs and complete decoded PARI objects.',
 'depends_on':['E.46','E.38','E.114','E.116','E.119','E_MilneCFT','E_LemmermeyerAmbiguous','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379; Part E(c),(d), Item2/Lead3 through the actual H quotient and root-cubing Kummer--Shapiro morphism.'],
 'depends_on_doubtful_reading':False,
 'notes':'The full upper class conclusions follow from exact normalizer actions, the actual trace identity, an explicit nilpotence bound, and the positive horizontal connecting class. No upper BNF completeness assumption is used. The three unit norm subgroups have their actual Hilbert90 divisor comparison, not an invented upper fundamental-unit matrix. All assertions concern this actual transition; later positional levels and the full intrinsic section set retain their separate comparison kernels.'
}])
save('e_fiftythree_normalizer_coverage.json',{
 'statement':'E.121',
 'addresses':[{'task':'Part E(c),(d), Item2 and Lead3 through the actual H quotient',
 'scope':'Closes both full projection kernels and all actual class/capitulation maps left in E119 at the next lower positional53 transition.',
 'exact_maps':['Literal beta2 cubing to beta1 and the inclusions Li into Bi; E46 identifies the corresponding root pushforward with field norm.',
 'Actual automorphisms g,h with hgh^-1=g^4; full ideal/principal corrections transport their action to the E119 Smith bases.',
 'Actual ideal norm and extension on all four finite groups; all squares, trace identities, inverse coordinates and basis ambiguity are checked.',
 'Positive connecting class [sigma0,h0] maps to [3e0]; its injection through the unramified S-split class-field sequence determines the entire A(L2).',
 'Literal compositum C=B2*conjugate(B2), fixed subgroups, intersection B1, and the exact Artin character of C/B2.',
 'Element-to-ideal Hilbert90 map Nx to pr3[D_x] identifies each actual S-unit norm defect, including its inverse and completed topology.']}],
 'closed_steps':['Full A(B2) and its zero (sigma-1) kernel.',
 'Full A(L2), its nonzero kernel <3u>, exact sigma action and all vertical/horizontal class maps.',
 'Actual three capitulation groups; all S-unit norm indices/types and completed norm-kernel free/torsion types.',
 'Exact cyclic-nine genus quotient, g/h actions and their joint quotient; literal unramified compositum character.'],
 'remaining':['The subsequent lower positional53 transitions and their compatible inverse limit are not assigned the values of this transition.',
 'The remaining lower positional factors for general inert primes, and their complete norm-coherent unit/divisor systems, still require their actual arithmetic.',
 'The explicit finite unit norm-defect maps here do not provide an uncomputed six-row upper fundamental-unit basis; the defining subgroup is the exact norm image with the stated Hilbert90 inverse.',
 'Intrinsic metabelian and marked sections map to H through the established actual quotient; no lifting surjectivity is inferred from these H norm coordinates.']})

save('e_fiftythree_normalizer_source_evidence.json',{
 'statement':'E.121',
 'read_scope':'Exact primary passages were opened and read in this conversation; E119 retains the earlier retrieval record. This ledger distinguishes the proved cup-product argument from the adjacent lemma whose printed proof is omitted.',
 'sources':[{
  'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
  'opened_passages':['Version4.03 III Theorem3.1 and its complete cup-product Res/Cor proof.',
   'V Proposition3.3 and its ideal-norm/Frobenius proof; Theorem3.6 and Example3.9 (trivial-modulus Hilbert class field).',
   'V Proposition5.2 with complete local-to-global proof; Theorems5.3 and5.5. Example5.4 is the Hilbert-symbol product formula, not the existence theorem.',
   'VII Proposition3.1 with the complete unit-lattice Herbrand calculation; VIII Theorem3.1 with its complete cyclic Hasse-norm proof.'],
  'explicit_transfer':'Tate degree minus two is the abelianization of the Galois group. Its cohomological restriction is group transfer and its corestriction is induced inclusion. In degree zero for the multiplicative field module the maps are field inclusion and norm. Cupping with the fundamental class in the proved III3.1 square gives inclusion--transfer and norm--restriction for local reciprocity. V5.2 then multiplies the actual local maps into the global idelic map, and V3.3 identifies the actual ideal Frobenius square.',
  'omitted_proof_caution':'Adjacent III Lemma3.2 prints Proof. To be added. Its omitted proof is not claimed as read or used as an independently proved source.',
  'usage':'The exact idelic genus subgroup, decomposition splitting, class norm/extension, unramified S-split exact sequence, unit Herbrand quotient and field-norm condition are stated with their literal maps in the proof.'},
 {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
  'opened_passages':['Theorem1, Proposition1, and the full ideal/Hilbert90 and unit-Herbrand proof.'],
  'usage':'E121.20 supplies the actual outside-S element/divisor construction and both inverse directions. The finite class group is projected canonically to its three-primary subgroup; the omitted prime-to-three invariant quotient vanishes by jN=3.'},
 {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html',
  'opened_passages':['Official nfgaloisapply contract, including transformed-ideal comparison through ideal HNF (retrieval turn1056view0 and local PARI2.19.0 doc/usersch3.tex).',
   'E119 retains the official bnfcertify flag0/flag1 documentation and complete class-generation/saturation proof scope.'],
  'usage':'Only the immutable fully justified lower E119 objects are inputs. Every new ideal image, principal correction, contraction, residue degree and local character is checked exactly. E121 makes no new upper BNF class-number or unit-completeness claim.'}],
 'author_review':'Complete proof and owned programs read; five-stage fresh copied-source/input replay passed with all seven text outputs byte-identical and all seven complete decoded PARI objects identical, no exclusions.',
 'root_status_at_freeze':'Root reports a complete proof/source audit and full original 128-file five-stage replay PASS. Its independently written finite-map program, without author code/output imports, checks all full groups/maps/squares, trace identities, basis shears, positive connecting class, defect quotients and compositum subgroups. The two final proof-only precision changes were specifically requested and checked by root; the complete mathematical sources and outputs are unchanged.',
 'peer_status_at_freeze':'d_galois reports a complete proof/source read and independent finite/ideal executions PASS, including all nine lower classes and all nine norm lifts for the exact j_L rule. The peer will validate this refreshed manifest before its final audit freeze. No separate a_structure full E121 review is claimed.',
 'final_proof_only_amendment':amendment})

names=['e53_order_nine_genus','e53_normalizer_actions','e53_horizontal_upper_norm','e53_horizontal_upper_extension','e53_cyclic_nine_comparison']
save('e_fiftythree_normalizer_dependencies.json',{
 'portable_full_rebuild':'python code/e53_normalizer_module.py --gp /absolute/path/to/gp',
 'workspace_full_rebuild':'python research_e119_continuation/code/e53_normalizer_module.py --gp /workspace/scratch/e34c61ec5a35/research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck':'python code/e53_normalizer_module.py',
 'fresh_copy_comparison':'python code/e53_normalizer_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path',
 'layout':'python code/e53_normalizer_layout.py',
 'freeze':'python code/e53_normalizer_freeze.py',
 'required_sources':['code/e53_normalizer_module.py']+['code/'+n+'.gp' for n in names],
 'immutable_lower_inputs':['inputs/e119_e53_genus_transition.bin','inputs/e119_e53_positional_genus_transition.bin','inputs/e119_e53_horizontal_base.bin'],
 'lower_input_provenance':'Exact hashes and their corrected E119 manifest hash are in inputs/manifest.json. E119 provides the complete ten-stage source-only upstream reconstruction. The three copied lower GP sources and outputs document the input-producing stages; those sources retain their E119 dependencies and are not represented as a standalone lower reconstruction.',
 'upstream_full_rebuild':'In the retained E119 bundle: python code/e_lower_fiftythree.py --gp /absolute/path/to/gp',
 'expected_text_outputs':['code/e53_normalizer_module.out','code/e53_normalizer_module.json']+['code/'+n+'.out' for n in names],
 'expected_complete_binary_outputs':sorted(replay['binary_objects']),
 'Python_dependencies':['sympy'],'PARI_version_used':'2.19.0',
 'serialization_rule':'Every declared integer matrix is checked integral and decoded exactly. Ambient rational forward matrices use canonical rational strings with exact Rational decoding and both inverse compositions. Seven complete decoded PARI objects are compared by ===; raw binary headers may differ and no component is excluded.',
 'scope':'The five stages reconstruct the entire new arithmetic from immutable certified lower inputs. No upper BNF and no repeated lower class-group certification is required.'})

save('e_fiftythree_normalizer_computation_status.json',{
 'statement':'E.121','status':'PASS','final_five_stage_session':18343,'final_five_stage_exit':0,
 'fresh_copy_replay_session':72637,'fresh_copy_replay_exit':0,
 'fresh_copy_replay':'audit/author_replay/replay.json',
 'fresh_copy_text_outputs':len(replay['text_outputs']),
 'fresh_copy_complete_PARI_objects':len(replay['binary_objects']),
 'excluded_fields':[],'excluded_binary_components':[],
 'finite_checks':data['finite_checks'],
 'retained_attempts':[{
  'directory':'code/history/cyclic_restriction_row_shape','status':'Actual failed assertion caused by a GP column-versus-row representation. Original source and output retained; corrected exact row is checked in the final certificate.'},
 {'directory':'code/history/normalizer_submatrix_assignment','status':'Actual GP parser failure on submatrix assignment; original source/output retained.'},
 {'directory':'code/history/normalizer_prime_ordering','status':'Actual failed relation-preservation check from conflating the analytic wild-prime labels with raw PARI ordering. Final source transports the literal retained prime permutation before every character/ideal map.'},
 {'directory':'code/history/normalizer_interrupted_after_g','status':'Actual g output retained. Session44421 became unavailable before an exit code or h result was returned; no completion or final PASS is attributed to it.'},
 {'directory':'code/history/before_portable_inputs','status':'All five actual executed GP sources and outputs before the path-only switch to immutable local inputs are retained.'},
 {'directory':'code/history/first_finite_only_checker','status':'The initial finite-only checker exited0 before the full-module proof. Its source had been updated before a history copy, and its original stdout was overwritten. The reconstructed earlier source and a new actual isolated replay are retained with explicit provenance; that replay is not called recovered original stdout.'},
 {'directory':'code/history/initial_paragraph_layout','status':'Actual first LuaTeX preview failure, Improper prevdepth at a paragraph heading. Complete failed proof/source/output retained. Replacing heading macros by emph is the only correction; the final seven-page rendering is clean.'}],
 'layout':layout,
 'visual_scope':'The author actually opened and reviewed all seven original page images at the retained 100-dpi full-page scale. After the two proof-only additions, pages1--4 are byte-identical; every changed final page5--7 was opened and reviewed individually. All formulas, tags, tables, page boundaries and references are legible with no clipping or overlap. Final log has no overfull box.',
 'final_proof_only_amendment':amendment,
 'expensive_BNF_status':'No upper BNF was run in this continuation. The two superseded original seventeen jobs were stopped with exit130 in E101 and were not restarted. E119 retains its actual timeout/failure scope; none supplies an upper class-group conclusion here.'})

(LEDGER/'e_fiftythree_normalizer_refs.bib').write_text('% verified: E121 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_PARICertifiedUnits. Exact proof scope and actual norm/transfer derivation are in e_fiftythree_normalizer_source_evidence.json. No duplicate bibliography keys.\n')
(LEDGER/'e_fiftythree_normalizer_report.md').write_text('''# E.121 — Entire upper positional class groups at 53

## What is now evaluated

The actual fields are beta1^3=53*zeta3, beta2^3=beta1, Li=Q(betai) and Bi=Li(zeta9), with S all places over3 and53. The full groups are A(B2)=C9+C3^3 and A(L2)=C9^2. This replaces the explicit projection kernels left in E119 by their proved values: zero for B2 and the order-three subgroup <3u> for L2. The L2 vertical action is [[1,3],[0,1]].

Every norm and extension is the actual ideal map. The theorem supplies the full vertical and horizontal matrices, their precise source/target bases, all composition squares and trace identities, and every capitulation kernel. The ambiguity in the second L2 basis vector is exactly a to a+3ku; each displayed map is unchanged with that transported basis. The projected horizontal norm in E119 has index three, while the full horizontal norm is the injection of the h-coinvariants into A(L2) supplied by the unramified S-split class-field sequence.

## Why the full B2 projection kernel vanishes

The retained ideal calculations evaluate the actual g and h actions on the sigma-coinvariants. Write T=g-1, s=g^3-1 and M=sA on the full unknown finite three-group A. The computed quotient action gives T^2 A contained in M. The lower g-action is identity, and actual ideal extension composed with norm is the trace 3+3s+s^2. Thus T times that trace vanishes, and M is contained in (3,T)M. For 3^e A=0, g^9=1 gives T^9 in3 Z3[g], so (3,T)^(9e) annihilates A. Iteration proves M=0. This uses the finite group itself, not an assumption that its coinvariants determine it.

## Why the full L2 group has two order-nine generators

The actual extension B2/L2 is unramified and split at every place of S. Its class-field sequence embeds (A(B2))_h=C9+C3 into A(L2), with quotient C3. The literal positive tame inertia lift sigma0 and horizontal lift h0 have commutator class3e0 in the E119 coordinates. Consequently the remaining vertical difference subgroup is <3u>, where u is the ideal norm of e0, of order nine. The vertical trace and the lower exponent-three group imply exponent at most nine; the quotient modulo3 has dimension two and the total order is81. These actual maps force A(L2)=C9^2. The power relation 3a=N_h(e1) is fixed by the horizontal norm/extension identity, removing the remaining coordinate ambiguity.

## Cyclic-nine and normal-closure comparisons

Over F=Q(zeta9), four literal local Artin characters and the complete certified F S-unit basis give Gamma_F=C9^2+C3^2. Its restriction kernel, with all forward and inverse Smith maps, is the actual g-coinvariant quotient C9+C3^2. The g,h ideal maps and principal corrections retain every prime label and the arithmetic reciprocity sign.

The actual compositum is C=B2*conjugate(B2)=Q(53^(1/9),zeta27), and the intersection is B1. The two fixed subgroups are computed in the literal order162 normal-closure group. The extension C/B2 is unramified and S-split, and its exact Artin character is x0+x1+2x2+x3 modulo3. This gives an explicit comparison without assigning an action of complex conjugation on a field that it does not preserve.

## Actual unit norm images and complete kernel types

For each cyclic extension E/D, an S-unit u=Nx determines an outside-S divisor D_x with div(x)=(tau-1)D_x. The exact boundary sends u to the canonical three-primary class of D_x modulo extended base classes. Hilbert90 and the invariant-divisor comparison prove both directions. On prime-to-three classes the omitted invariant quotient vanishes by the actual identity jN=3. Thus the actual field-norm/S-unit-norm defects are C3^4, C3, C3 for B2/B1, L2/L1 and B2/L2. Combining the evaluated local field-norm indices gives total unit quotients C3^6, C3, C3.

Completion is by powers of three on finitely generated S-units. The actual root-of-unity norms are cubing vertically and xi to zeta horizontally. They give kernel torsion C3 in all three cases; the free kernel ranks are18,6,22. The exact norm subgroup is defined by the literal map and its ideal boundary. No uncomputed upper fundamental-unit matrix is substituted for that subgroup.

The final proof-only clarification spells out two actual maps. For every lower class b, choose any actual a with N_L(a)=b and put j_L(b)=3a. Its independence follows from ker N_L=3A(L2) and 9A(L2)=0; no inverse of the noninjective norm is invoked. For each completed unit-norm kernel K, choose a Z3-basis of K/mu3 and actual lifts k_i. The map (z,(a_i)) to z times the product of k_i^a_i is a continuous isomorphism; its inverse reads quotient coordinates and divides to recover z. The proof states the GL_r(Z3) basis change and the exact root-of-unity lift ambiguity.

## Reproduction and evidence

Run `python code/e53_normalizer_module.py --gp /absolute/path/to/gp` from the bundle. The five owned GP stages read only the three immutable certified lower E119 objects; the input manifest gives their hashes and complete upstream provenance. The complete lower reconstruction remains available in E119. Every new ideal identity, principal factor, residue degree, local character and relation-lattice map is checked exactly.

The separate source/input-only author replay reproduces all seven complete text outputs byte for byte and compares all seven full decoded PARI objects with exact equality, excluding no component. Raw serialized binary headers differ, and both byte hashes plus the exact object comparison are retained. Ambient rational Smith maps use canonical rational strings with exact decoder checks; integer exports assert integrality before conversion.

All actual failed, interrupted and superseded attempts are retained with their scope. One early finite-only stdout was overwritten before a history copy; the retained reconstructed source and fresh replay are explicitly identified as a replay, not recovered original output. No upper BNF certification is used. The complete original128-file freeze is preserved under audit/pre_final_typing/full_tree. The literal two-change proof diff and amendment record are audit/e121_final_typing.diff and audit/e121_final_typing.json. All mathematical code, complete outputs and PARI objects are hash-identical. The final proof is seven pages; pages1--4 equal the previously reviewed images and all changed final pages5--7 were individually viewed after rendering. The final log has no overfull box. Root's full original arithmetic replay and independent peer finite/ideal checks have passed; the final manifest validation is the only remaining peer bookkeeping step.

The result closes the complete next lower positional53 transition. Subsequent levels, compatible inverse norm systems and the unrestricted intrinsic section set remain the next arithmetic work. Transfer to H uses E46's actual Kummer--Shapiro root-evaluation and root-cubing norm, and intrinsic section classes reach H through the established exact quotient maps.
''')

exclude={'ledger/e_fiftythree_normalizer_manifest.json','code/e53_normalizer_freeze.out'}
files={}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in exclude:continue
    files[rel]={'sha256':sha(p),'bytes':p.stat().st_size}
save('e_fiftythree_normalizer_manifest.json',{
 'statement':'E.121','status':'FROZEN_AUTHOR_PASS','files':files,
 'excluded_own_stdout':'code/e53_normalizer_freeze.out',
 'mathematical_rebuild':'python code/e53_normalizer_module.py --gp /absolute/path/to/gp',
 'complete_copy_replay':'python code/e53_normalizer_replay.py --gp /absolute/path/to/gp --destination /new/empty/audit/path'})
print(json.dumps({'statement':'E.121','status':'FROZEN_AUTHOR_PASS','files':len(files),
 'proof_sha256':sha(proof),'main_sha256':sha(ROOT/'code/e53_normalizer_module.py'),
 'JSON_sha256':sha(ROOT/'code/e53_normalizer_module.json'),
 'manifest_sha256':sha(LEDGER/'e_fiftythree_normalizer_manifest.json'),
 'standalone_pages':layout['pages'],'complete_text_replays':len(replay['text_outputs']),
 'complete_PARI_object_replays':len(replay['binary_objects'])},indent=2))
