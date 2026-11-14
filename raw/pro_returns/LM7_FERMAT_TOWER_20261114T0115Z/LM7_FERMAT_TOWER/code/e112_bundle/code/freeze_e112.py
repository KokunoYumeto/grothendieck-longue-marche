"""Record the proved E112 scope, actual executions, source reads and file hashes."""
from pathlib import Path
import hashlib
import json
import fitz

root=Path(__file__).resolve().parents[1]
ledger=root/'ledger'
ledger.mkdir(exist_ok=True)
proof=root/'sections'/'E_quartic_five_cohomology.tex'
assert hashlib.sha256(proof.read_bytes()).hexdigest()=='3b9c685b92d973c3e6ced92bf1d79c9e0cc1a84488ed9878aca84b09a30d10a4'
certificate=json.loads((root/'code'/'e_quartic_five_cohomology.json').read_text())
assert certificate['status']=='PASS'
assert (root/'code'/'e_quartic_five_cohomology.out').read_bytes()==(root/'code'/'e_quartic_five_cohomology.json').read_bytes()
assert len(certificate['certified_character_subfields'])==12
build=json.loads((root/'qa'/'build_status.json').read_text())
assert build['status']=='PASS' and build['proof_sha256']==hashlib.sha256(proof.read_bytes()).hexdigest()
def save(name,data):
    (ledger/name).write_text(json.dumps(data,indent=2)+'\n')
statement=('For the actual five-adic quartic CM lattices V, Vchi2, V(1), '
           'V(1)chi2 and U_CM, all finite H2 over G_Q,{2,5} vanish, '
           'finite H1 is cyclic of order5^n, and integral H1 is Z5. '
           'Twelve fully certified degree8 character fields, actual torsion-point '
           'field inclusions, and explicit ideal extension/norm inverses prove '
           'vanishing of both degree32 division fields\' five-primary class groups. '
           'The actual decomposition groups kill the finite Brauer-coefficient '
           'invariants. Unrestricted H1 of each twisted Tate module is Z5; '
           'H1(U_CM) is Z5 plus the restricted Z5 coefficient module over '
           'primes3 mod4, with exact tame-inertia projections and cocycle sections. '
           'Every nonempty central quartic fibre at5 has evaluated module '
           'Z5^66 plus six all-prime, three split-prime and three inert-prime '
           'restricted modules, with all original coefficient maps retained.')
save('e_quartic_five_cohomology_results.json',[{
    'id':'E.112','status':'Proved','statement':statement,
    'where_proved':'sections/E_quartic_five_cohomology.tex, E112.1--18 and full proof; '
                   'code/e_quartic_five_cohomology.py/.out/.json and '
                   'quartic_five_character_fields.gp/.out/.bin.',
    'depends_on':['E.103','E.105','E.108','E_MilneADT','E_JannsenContinuous','E_PARICertifiedUnits'],
    'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178; '
                          'Part E(c),(d), E follow-up4.'],
    'depends_on_doubtful_reading':False,
    'notes':'The original E23 mixed obstruction and other coefficient primes '
            'remain active. No full degree32 class number is asserted. '
            'The binary serialization is retained as actual PARI output; '
            'independent replay equality is recorded after deserialization.'}])
save('e_quartic_five_cohomology_dependencies.json',{
    'statement':'E.112','internal':['E.103','E.105','E.108'],
    'external':['E_MilneADT','E_JannsenContinuous','E_PARICertifiedUnits'],
    'input_sources':['code/quartic_five_character_fields.gp','code/quartic_five_character_fields.out'],
    'original_tasks_still_open':['D.13','D.19','E.23','D.a original-source verification']})
save('e_quartic_five_cohomology_coverage.json',{
    'statement':'E.112','tasks':['E.c','E.d','E.followup4'],
    'state':'All three previously retained quartic CM central cohomology types '
            'are evaluated at5 with exact inverse maps. The full mixed image '
            'and other coefficient primes remain in the original E23 task.',
    'does_not_close_original_task':True})
save('e_quartic_five_cohomology_computation_status.json',{
    'main_command':'python3 research_e112/code/e_quartic_five_cohomology.py --gp research_e52/vendor/pari-2.19.0/gp',
    'actual_main_exit_code':0,'actual_full_GP_exit_code':0,
    'certified_fields':12,'certification_flag':0,
    'fourier_inverse_checks':1536,'norm_extension_checks':576,
    'actual_residual_Galois_group_order':32,'finite_inert_projector_checks':1584,
    'complete_stdout_equals_JSON':True,
    'historical_attempts':[
        {'path':'code/history/whole_field_certification_interrupted',
         'actual_exit_code':130,'status':'Interrupted; full degree32 certification was not obtained.'},
        {'path':'code/history/reserved_I_parser_failure','actual_exit_code':0,
         'status':'Rejected immediately: reserved-variable parser failure, zero certified fields.'},
        {'path':'code/history/reserved_theta_parser_failure','actual_exit_code':1,
         'status':'Rejected: reserved-variable parser failure; final count guard stopped execution.'},
        {'path':'code/read_primary_sources.py','actual_exit_code':1,
         'status':'Public author-PDF retrieval returned HTTP406. Its actual traceback is retained. '
                  'The original PDF was read through the already working web reader.'}],
    'standalone_build':build})
save('e_quartic_five_cohomology_source_evidence.json',[
    {'key':'E_MilneADT','url':'https://www.jmilne.org/math/Books/ADTnot.pdf',
     'verified':True,'opened':True,
     'fresh_root_scope':['II.2.1 and its proof, II.2.2(a): Kummer/Brauer maps',
                         'II.2.9 and complete proof, printed170--172: Galois--etale comparison',
                         'II.0.1(f) and proof: localization sequence',
                         'I.4.15 and proof: finite-S finiteness',
                         'I.5.1 and complete number-field proof, including Lemmas5.3 and5.4'],
     'prior_and_peer_scope':'II.1.7(b) purity and its exact local maps, already verified '
                            'for E108; independently reopened in the complete E112 peer audit.',
     'web_refs':['turn972view0','turn974view0','turn974view1','turn974view2',
                 'turn983view0','turn983view1','turn983view2','turn983view3','turn994view4'],
     'local_download':'Attempted public fetch returned HTTP406; no downloaded copy or '
                      'successful local extraction is claimed.'},
    {'key':'E_JannsenContinuous','url':'https://epub.uni-regensburg.de/26684/1/jannsen12.pdf',
     'verified':True,'opened':True,
     'scope':'Proposition1.6 and Theorem2.2 as already read in the E108 source evidence '
             'and freshly reopened by the independent E112 reviewer. The proof above '
             'also constructs the compatible cocycles and their inverse coordinates.',
     'prior_evidence':'research_e108/ledger/e_quartic_peripheral_source_evidence.json'},
    {'key':'E_PARICertifiedUnits',
     'url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html',
     'verified':True,'opened':True,
     'scope':'Original bnfcertify specification, default flag0 and complete certification '
             'meaning; exact returned value1 required for all12 structures.',
     'web_refs':['turn972view2','turn974view3']}])
(ledger/'e_quartic_five_cohomology_refs.bib').write_text(
    '% E112 reuses verified keys E_MilneADT, E_JannsenContinuous and E_PARICertifiedUnits.\n'
    '% Exact original passages and actual read scopes are in its source-evidence ledger.\n')
(ledger/'e_quartic_five_cohomology_report.md').write_text('''# E.112: complete five-primary quartic central cohomology

The actual fields Q(E_+[5]) and Q((y^2=x^3+4x)[5]) are described by two fourth radicals over Q(i). Explicit torsion points prove both field inclusions. The two residual Tate characters are 2^r and 2^(-s); the pure symmetric-square coefficient U(-1) therefore uses the character r+s and the exact cyclic subfield Q(i,5^(1/4)).

Six degree-eight subfields in each family were fully certified with default bnfcertify flag0. Their class numbers are 1,1,2,2,1,2. Ideal extension and norm compose to multiplication by four and the four-term group norm. Their inverse maps, followed by the sixteen integral character idempotents, prove that both degree32 division fields have trivial five-primary class group. The full class numbers of those fields are not assigned values.

The actual decompositions of2 and5 in the relevant cyclic subfields have full relative decomposition group of order4. These groups kill the required residual coefficient invariants in the finite Brauer exact sequence. Restriction/corestriction of degree32, Kummer, the original Galois--etale comparison, and the exact coefficient sequences prove H2=0 at every exponent for V, Vchi2, V(1), V(1)chi2 and U. Euler characteristic and the explicit transition maps give cyclic H1 of order5^n and a chosen continuous generator with its inverse scalar coordinates.

For unrestricted cohomology, the four Tate-module types have no tame-inertia coordinates outside{2,5}. U has one integral fixed line at each prime3 mod4. Its exact Frobenius projector and inverse row are written in E112.17; localization supplies bounded cocycles with exactly one such residue. The uniformly convergent restricted sum and subtraction of those cocycles give inverse global maps. Substitution into E108 evaluates the whole central fibre as Z5^66 plus six all-prime, three split-prime and three inert-prime restricted modules. The rational-five statement follows by the actual bounded-denominator cochain comparison.

The actual full arithmetic run exited0 and retained all twelve structures. The supplementary exact program checks1536 Fourier inverses,576 norm compositions, the32-element residual group and1584 finite inert Frobenius projections, in addition to five polynomial matrix identities. The all-level and unrestricted assertions use the complete written proof.

The initial degree32 class-number certification was interrupted; it supplies no class-number assertion. Two parser attempts were rejected after inspecting their actual outputs, including a misleading zero-field completion marker. All attempted sources, outputs and statuses remain attached. The later successful field count is exactly12. A direct source-download attempt returned HTTP406; the original Milne PDF was successfully read through the web reader already in use.

The earlier investigation of Kings's determinant result and Bars's CM cohomology results did not supply the fixed-twist finite H2 vanishing needed here. Their read scopes are recorded in the research history; neither is an input to this proof. The proof uses the certified character fields and exact cohomology maps above.

This result evaluates the retained named CM cohomology factors at5. The unrestricted quartic mixed obstruction, other geometric primes and the full original E23 classification remain active. D13, D19 and the missing-original-source part of D.a also retain their original status.
''')
qa=root/'qa'
document=fitz.open(qa/'E112_check.pdf')
images=[]
for index,page in enumerate(document):
    image=page.get_pixmap(dpi=110,alpha=False)
    path=qa/('E112_page_'+str(index+1)+'.jpg')
    image.save(path)
    images.append({'page':index+1,'path':str(path.relative_to(root)),
                   'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
save('e_quartic_five_cohomology_render.json',{
    'pdf_sha256':build['pdf_sha256'],'pages':len(document),'images':images,
    'all_pages_rendered':True,'visual_review_claimed':False})
paths=[]
for directory in ['code','sections','ledger']:
    paths.extend(p for p in (root/directory).rglob('*') if p.is_file()
                 and p.name not in ['e_quartic_five_cohomology_manifest.json','freeze_e112.out']
                 and '__pycache__' not in p.parts)
manifest={'statement':'E.112','status':'author frozen',
          'section':'sections/E_quartic_five_cohomology.tex',
          'files':[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,
                    'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(paths)],
          'excluded_directories':['sources','qa'],
          'scope':'Actual mathematical sources, outputs, complete binary certificates, '
                  'historical failed attempts and metadata. Render images are recorded '
                  'by the separate render manifest; independent audits are attached later.'}
save('e_quartic_five_cohomology_manifest.json',manifest)
print(json.dumps({'status':'PASS','frozen_files':len(paths),'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
                  'manifest_sha256':hashlib.sha256((ledger/'e_quartic_five_cohomology_manifest.json').read_bytes()).hexdigest(),
                  'rendered_standalone_pages':len(document)},indent=2))
