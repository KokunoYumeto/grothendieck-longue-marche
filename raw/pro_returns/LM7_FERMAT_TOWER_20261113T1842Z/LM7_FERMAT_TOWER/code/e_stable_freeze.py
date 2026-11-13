#!/usr/bin/env python3
"""Write E.86 provenance and freeze the proof and exact certificates."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'ledger';LEDGER.mkdir(exist_ok=True)
code=ROOT/'code';proof=ROOT/'sections/E_stable_sclass_towers.tex'
text=proof.read_text()
assert len(re.findall(r'^\\\[$',text,re.M))==28
assert len(re.findall(r'^\\\]$',text,re.M))==28
assert not any(ord(c)<32 and c not in '\n\t\r' for c in text)
assert not re.search(r'(?<!\\)\b(?:quad|qquad)\b',text)
assert r'^{,' not in text
cert=json.loads((code/'e_stable_sclass_towers.json').read_text())
assert cert['status']=='PASS'
def save(n,obj):(LEDGER/n).write_text(json.dumps(obj,indent=2)+'\n')
save('e_stable_sclass_results.json',[{
 'id':'E.86',
 'statement':'At every level Cl_S(B_d){3}=C3 and Cl_S(L_d){3}=C3^2, in actual coherent prime73 and prime7 bases; all adjacent norms are identity and all extensions zero. Horizontal norm is the second-coordinate inclusion, with explicit Artin quotient. Cl(B2){3}=C9+C3^2 and Cl(L2){3}=C9+C3 have complete genus restriction, inverse Smith, ordinary norm and extension maps. All27 prior candidate ideals are principal; the full B2 principal S-divisor lattice has index27. Every cyclic B cubic/ninth-degree S-unit defect is C3, with quotient C_(3^r)^5+C3. Every original adjacent cubic defect is C3^2, with quotient C3^3. Literal Hilbert90 maps, completed fibers, ranks and roots-of-unity kernels are proved.',
 'status':'Proved',
 'where_proved':'sections/E_stable_sclass_towers.tex, E86.1--E86.28 and full proof; code/e_stable_sclass_towers.py, three owned GP stages, ten arithmetic dependencies, all actual outputs and three retained BIN certificates.',
 'depends_on':['E.57','E.69','E.72','E.76','E.79','E.81','E.84','E_MilneCFT','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178; actual positional/norm maps E.46,E.69,E.72,E76.11.'],
 'depends_on_doubtful_reading':False,
 'notes':'All-level proof uses actual order9/order3 automorphisms and the cyclic-module endomorphism ring, not finite extrapolation. Complete13-stage author rebuild session56177 exited0. Primary Milne VII3.1 full proof freshly reopened/read. Original eventual h and the particular xi*c1 norm coset remain uncomputed. A checked the all-level induction; full draft/certificate audit requested.'}])
save('e_stable_sclass_coverage.json',{
 'statement':'E.86','scope':'All-level S-class and cyclic norm evaluation inside E(c),E(d),Lead3.',
 'completed':[
  'Entire B S-class tower, coherent generator, every norm/extension matrix and cyclic annihilator.',
  'Entire L S-class tower, coherent prime7/prime73 basis and horizontal Artin/norm sequence.',
  'Complete ordinary three-class groups B2,L2; exact genus restrictions, inverses and four ideal maps.',
  'All27 E81 principal ideals, delta=w=0 and full index27 B2 principal S-divisor lattice.',
  'All cyclic cubic/ninth-degree B unit defects and adjacent L defects with actual Hilbert90 maps.',
  'Every horizontal unit norm congruence, completed exact sequence and finite fiber rank/torsion.'],
 'remaining':[
  'Evaluate original higher ordinary prime orders and eventual3-unit exponent h.',
  'Evaluate the particular xi*c1 unit-norm coset in its now computed obstruction group.',
  'Complete remaining intrinsic metabelian/marked-depth section comparison kernels.'],
 'combined_original_tasks_complete':False})
save('e_stable_sclass_source_evidence.json',{
 'statement':'E.86','primary_sources':[
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'passage':'VII Proposition3.1, printed208--209/PDF216--217, including Lemmas3.2,3.4,3.5 and full lattice proof.',
   'read':'Freshly opened/read 2026-11-13: turn750view0,turn752view0,turn752view1,turn752view2.',
   'use':'Herbrand quotients n^5,3,1/3 for the exact local degrees. Actual Hilbert90/capitulation maps are proved in E86.'},
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'passage':'II1.22; III3.1,3.4; V5.2; VIII3.1.',
   'read':'Exact statements/full printed proofs read during E64,E65,E76,E79; used through their proved maps. III Lemma3.2 has no separate printed proof: E79 proves the compatibility from III3.1.',
   'use':'Local norm kernels, genus field maximality, actual prime Frobenius norm maps.'},
  {'key':'E_PARICertifiedUnits','url':'https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.19.0/users.pdf',
   'local_source':'research_e52/vendor/pari-2.19.0/doc/usersch3.tex',
   'passage':'bnfcertify,bnfisprincipal,bnrinit,bnrisprincipal,nfmodpr,nfmodprlift,nfgaloisapply.',
   'read':'Official source manual entries read before use. Full rebuild calls bnfcertify with default flag0 and receives return1.',
   'use':'Certified B1 and L1 inputs only; no B2/L2 BNF. Actual ideals/residue fields/ray maps/Smith inverses.'}],
 'new_proof':'Actual normalizer commutator forces the cyclic-module action trivial. The ordinary B2 norm polynomial annihilates the actual six-prime subgroup. Explicit class-field inclusions and computed degrees identify both full Hilbert three-class fields.',
 'independent_audit':'A checked all-level induction and preceding ordinary strengthening; full draft/certificate review requested. Root audit follows freeze.'})
save('e_stable_sclass_computation_status.json',{
 'author_complete_rebuild':{'session_id':56177,'exit_code':0,'stages':13,
  'command':'python research_e86/code/e_stable_sclass_towers.py --gp research_e52/vendor/pari-2.19.0/gp > research_e86/code/e_stable_sclass_towers.out 2>&1',
  'output':'code/e_stable_sclass_towers.out'},
 'original_BNF_jobs':[
  {'session_id':24024,'command':'research_e52/vendor/pari-2.19.0/gp -q research_prime17/first_layers.gp',
   'created_UTC':'2026-11-13 05:59:47.616539','last_poll_UTC':'2026-11-13 13:03:59','status':'still running, no new output','duplicated':False},
  {'session_id':40565,'command':'research_e52/vendor/pari-2.19.0/gp -q research_prime17/layer2_reduced.gp',
   'created_UTC':'2026-11-13 06:54:11.574697','last_poll_UTC':'2026-11-13 13:03:59','status':'still running, no new output','duplicated':False}],
 'retained_attempts':[
  {'source':'code/e_stable_class_maps_vector_attempt.gp','output':'code/e_stable_class_maps_vector_attempt.out',
   'outcome':'PARI type error from appending a second object to an existing BIN. Fresh driver uses an empty temporary directory and writes once. Historical output retained; later fresh inputs are not claimed to reproduce that appended state.'},
  {'source':'code/e_stable_class_maps_inspect.gp','output':'code/e_stable_class_maps_inspect.out',
   'outcome':'Actual type diagnostic found the appended outer vector.'},
  {'source':'code/e_stable_class_maps_seven_attempt.gp','output':'code/e_stable_class_maps_seven_attempt.out',
   'outcome':'Expected three primes with beta1=6, but the actual field has one degree3 prime; the other two have beta1=3,5. No class conclusion used the failed count.'},
  {'source':'code/e_stable_class_maps_inspect_seven.gp','output':'code/e_stable_class_maps_inspect_seven.out',
   'outcome':'Exact residue diagnostic found prime4 and class(0,2,0).'},
  {'source':'code/e_stable_class_maps_column_attempt.gp','output':'code/e_stable_class_maps_column_attempt.out',
   'outcome':'PARI concatenated columns vertically; explicit Mat([col1,col2]) fixed the coordinate export.'}]})
(LEDGER/'e_stable_sclass_refs.bib').write_text(
 '% Existing keys only; no duplicate entries.\n'
 '% verified: E_MilneCFT VII Proposition3.1 and full proof freshly read.\n'
 '% verified: E_PARICertifiedUnits official PARI2.19.0 entries read.\n')
(LEDGER/'e_stable_sclass_report.md').write_text("""# E.86: complete S-class towers

## Results and exact maps

Every three-primary S-class group of B_d is C3, and every such group of L_d is C3². Actual adjacent norms are identities in coherent prime73/prime7 bases, and actual ideal extensions are zero. Literal order9/order3 field automorphisms prove the result at every level.

The first ordinary groups are C9×C3² for B2 and C9×C3 for L2. Their genus restriction rows are (1,2,1,1) and (2,2,2), with complete inverse Smith maps. Three upper prime73 generators and two lower prime generators determine four ordinary norm/extension matrices. E86.25 explicitly transports the earlier beta2=3 prime at7 to the coherent beta2=-1 prime.

All27 E81 candidate ideals are principal; delta=w=0; the full principal S-divisor lattice has index27. Both genus fields equal the respective Hilbert three-class fields.

For B_{d+r}/B_d, r=1,2, the field-norm-to-S-unit defect is C3 and the total quotient C_(3^r)^5×C3. For the adjacent L tower these groups are C3² and C3³. The actual map solves div(x)=(sigma-1)D outside S and takes the displayed S-class coordinates. The proof gives both choice changes, the kernel, surjectivity and primary projection.

Every horizontal S-unit norm is given by one explicit valuation congruence. Completion preserves the exact maps and finite quotients. Each nonempty finite norm fiber has the exact free rank and literal root-of-unity torsion in E86.16.

The original ordinary prime-class exponent h remains retained, and no value of the particular xi*c1 coset is inferred from the order of its ambient defect group.

## Reproduction and checks

Run from the workspace root:

    python research_e86/code/e_stable_sclass_towers.py --gp research_e52/vendor/pari-2.19.0/gp

In the flat final code directory the same driver locates its dependency GP sources beside itself. It reconstructs thirteen stages in an empty temporary directory, retaining every output and three owned BIN data certificates. It certifies BNF only for B1 and L1, and does not duplicate either original L2 job.

Author run56177 exited0. Python verifies40 literal cubic norms, three complete Smith inverse systems,60 retained Frobenius coordinate records,33 integral-basis residue maps,216 kernel/inverse round trips,729 S-divisor residues, all27 principal candidates, four ordinary norm/extension maps and72 coherent prime-chain checks. GP checks192 upper and82 lower actual prime Frobenii.

Five development sources/outputs retain the appended-BIN diagnostic, the exact one-prime correction at7, and the PARI column export error. No failed search is used to infer nonprincipality or a norm obstruction.

The original BNF sessions24024 and40565 were still running without new output at2026-11-13 13:03:59 UTC. Exact commands and creation times are in the computation ledger. The present proof evaluates the three-class data independently of those jobs.
""")
manifest={}
for folder in ['sections','code']:
 for p in sorted((ROOT/folder).glob('*')):
  if p.is_file() and p.name!='e_stable_freeze.out':
   manifest[str(p.relative_to(ROOT))]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
save('e_stable_sclass_manifest.json',{'statement':'E.86','status':'author-frozen','files':manifest,
 'rebuild':'python code/e_stable_sclass_towers.py --gp PATH_TO_OFFICIAL_PARI_GP',
 'retained_data':['code/e_stable_lower_genus.bin','code/e_stable_class_coordinates.bin','code/e_stable_class_maps.bin']})
print('PASS: E86 displays, complete certificate, metadata and manifest.')
for p in [proof,code/'e_stable_sclass_towers.py',code/'e_stable_sclass_towers.json']:
 print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
