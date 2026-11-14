#!/usr/bin/env python3
"""Record the executed E.118 arithmetic and actual page review."""
from pathlib import Path
import hashlib
import json
import shutil

root=Path(__file__).resolve().parents[1]
work=root.parent
ledger=root/'ledger';ledger.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda name,data:(ledger/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
proof=root/'sections/E_quartic_five_numerical.tex'
assert sha(proof)=='142d07c7f19d79b5044ae37208f226031595c97b1060c023bf9da3b734f1a0f2'
certificate=json.loads((root/'code/e_quartic_five_numerical_verify.json').read_text())
assert certificate['status']=='PASS'
layout=json.loads((root/'qa/layout.json').read_text())
assert layout['proof_sha256']==sha(proof) and layout['pages']==4 and not layout['problems']
assert layout['PDF_sha256']=='f422a870c64e8ae086ff68c654070e935530e9c0d3d0cd074f741b78974ed9cf'
for row in layout['page_images']:
    assert sha(root/row['path'])==row['sha256']
old=json.loads((root/'qa/history/scalar_extension_typing/layout.json').read_text())
assert [x['sha256'] for x in layout['page_images'][1:3]]==[x['sha256'] for x in old['page_images'][1:3]]
write('e_quartic_five_numerical_visual.json',{
 'statement':'E.118','status':'PASS','proof_sha256':sha(proof),
 'PDF_sha256':layout['PDF_sha256'],'pages':4,'page_images':layout['page_images'],
 'actual_review':'Root individually viewed all four images of the immediately preceding build. After the peer typing correction, root individually viewed the changed pages1 and4 again; pages2 and3 are byte-identical to the images already viewed.',
 'findings':'All final pages are legible with no overlap, clipping or overfull display. The explicit tensor map and its inverse fit on page1; the actual rational correcting-cochain argument is legible on page4.',
 'history':'The initial missing display delimiters, the initial overwide E118.12 display, and the peer scalar-extension typing correction are retained with their actual outputs and exact changes.'})
write('e_quartic_five_numerical_results.json',[{
 'id':'E.118','statement':'An explicit global five-Kummer cocycle for the actual plus-quartic has finite arithmetic image E_+[5] semidirect Gamma of order800. At p3121 its exact local order is5 and its chosen residual Frobenius is(3,1). Over the toric input kappa5(3121) times the sum of the four A-cusp directions, the entire integral compact class-two slice is5 Z5^3, of index125; every nonempty fibre is the E115 central torsor. The separately specified tensor-extension map and actual rational cochain inverse give the whole rational compact slice.',
 'status':'Proved','where_proved':'sections/E_quartic_five_numerical.tex, E118.1--12 and full proof; code/e_quartic_five_numerical.gp and code/e_quartic_five_numerical_verify.py',
 'depends_on':['E.108','E.112','E.115'],
 'manuscript_passages':'Section51.16; folios733v--736v; scans172--178; equations371--379; PartE(c),(d), follow-up4',
 'depends_on_doubtful_reading':False,
 'notes':'Both algebraic units, their characters, division-field inclusions, corestriction and cochain ambiguity are explicit. The final arithmetic reconstruction uses no external certificate input. No integral Frobenius matrix modulo25 is assigned: the actual point count proves the exact denominator through det(F-1). The historical discovery uses the retained E112 certificate. Higher intrinsic targets remain in E23.'}])
deps=[]
for rel in ['research_e108/sections/E_quartic_peripheral_slice.tex','research_e112/sections/E_quartic_five_cohomology.tex','research_e115/sections/E_quartic_mixed_five.tex']:
    p=work/rel;deps.append({'path':rel,'sha256':sha(p),'bytes':p.stat().st_size})
historical=work/'research_e112/code/quartic_five_character_fields.bin'
(root/'inputs').mkdir(exist_ok=True)
shutil.copy2(historical,root/'inputs/quartic_five_character_fields.bin')
write('e_quartic_five_numerical_dependencies.json',{
 'statement':'E.118','proof_dependencies':deps,
 'exact_transfers':['E108 actual toric input and all55 peripheral tests','E112 actual division-field point maps and integral H1 reduction isomorphism','E115 actual mixed localizer, scalar divisibility test, rational correction inverse and all central fibres'],
 'standalone_arithmetic_inputs':[],
 'historical_discovery_input':{'original_path':str(historical.relative_to(work)),'retained_path':'inputs/quartic_five_character_fields.bin','sha256':sha(historical),'bytes':historical.stat().st_size},
 'historical_command':'From the original workspace root: GP -q -f research_e118/code/kummer_unit_explore.gp. The unchanged source expects research_e112/code/quartic_five_character_fields.bin and writes research_e118/code/kummer_unit_explore.bin.',
 'complete_portable_rebuild':'python code/e_quartic_five_numerical_verify.py --gp /absolute/path/to/gp'})
write('e_quartic_five_numerical_coverage.json',{
 'statement':'E.118','tasks':['E.c','E.d','E.follow-up-4'],
 'exact_result':'One actual nonzero global compact Kummer class, its finite order800 image and exact numerical prime3121; the entire integral and rational compact slices over the specified toric input, with all nonempty fibres through E115.',
 'maps':['E118.6 division-field inclusions and coordinate inverses','E118.10 Kummer character coordinates','E118.11 literal corestriction and coboundary ambiguity','E118.12 exact residue-field Frobenius and boundary denominator','Actual E115 class-two lift and fibre maps','Explicit (5R^3) tensor_R Q5 isomorphism and inverse, followed by the independent rational cochain inverse'],
 'remaining':'Original E23 higher intrinsic and marked preimages, other coefficient cases and the remaining full arithmetic sources remain active.'})
write('e_quartic_five_numerical_source_evidence.json',[
 {'source':'PARI/GP official elliptic-curve documentation, ellweilpairing',
  'url':'https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html',
  'opened':True,'web_open_refs':['turn1015view0','turn1015view1'],
  'local_document':'research_e52/vendor/pari-2.19.0/doc/usersch3.tex, lines33218--33229',
  'read_scope':'Definition of the finite-field Weil pairing and its Miller-function convention. Root read the exact local documentation and opened the official web documentation. The independent Python Miller line calculation reproduces190 with the alternating sign.',
  'proof_use':'Software convention corroboration. The proof retains the explicit torsion points and unit residues; no new external arithmetic theorem is inferred from the software manual.'},
 {'source':'Previously checked E108, E112 and E115 proof dependencies',
  'opened':True,'read_scope':'Root previously read their complete proofs and retained their actual arithmetic/source audits. E118 uses the exact maps listed in its dependency ledger.',
  'scope_limit':'No fresh opening of those external originals is claimed here.'}])
(ledger/'e_quartic_five_numerical_refs.bib').write_text('% E118 uses the already registered E108/E112/E115 mathematical sources.\n% The separately recorded official PARI documentation specifies the checked software convention.\n')
programs=[]
for name in ['kummer_unit_explore.gp','e_quartic_five_numerical.gp','e_quartic_five_numerical_verify.py','build_standalone.py','correct_scalar_extension.py']:
    p=root/'code'/name;o=p.with_suffix('.out');assert o.is_file() and o.stat().st_size
    programs.append({'program':str(p.relative_to(root)),'source_sha256':sha(p),'stdout':str(o.relative_to(root)),'stdout_sha256':sha(o),'exit_code':0})
write('e_quartic_five_numerical_computation.json',{
 'status':'PASS','executed_programs':programs,
 'certificate_sha256':sha(root/'code/e_quartic_five_numerical_verify.json'),
 'actual_finite_checks':{'exact_unit_and_inverse_polynomial_identities':True,'division_field_degree':32,'distinct_field_embeddings':32,'residual_products':1024,'invariant_tensor_generator_identities':3,'primality_trial_limit':55,'point_count':3200,'distinct_five_torsion_points':25,'independent_Miller_pairing':190,'unit_residues':[1362,1576],'fifth_residues':[2163,2119],'Frobenius_cocycle':[3,1]},
 'preserved_failures':['code/history/initial_display_delimiters: actual exit1, empty stdout, complete stderr and compiler output','qa/history/initial_equation_width: successful initial compile with an overfull display, corrected by a line break'],
 'proof_scope':'The finite certificates verify the displayed arithmetic data. The descent, full arithmetic image, local denominator, exact integral/rational slices and all fibres are proved in the text using the specified maps.'})
(ledger/'e_quartic_five_numerical_report.md').write_text('''# E.118: an explicit mixed obstruction at3121

The two displayed algebraic units u and u^c define an actual E_+[5]-valued global cocycle after3 times corestriction from the full degree32 division field. Its finite arithmetic image has order800. The field is L(u^(1/5),(u^c)^(1/5)); the exact unit characters prove that the translation kernel is C5^2. The proof writes the coset formula and the full change-of-representatives coboundary.

At the specified degree-one place above3121, the residue basis has Weil pairing190, the two fifth-power residues have exponents3 and4, and the cocycle is(3,1). Independent enumeration gives3200 elliptic points, with full five-primary group C5^2. Thus F-1=5D with D invertible over Z5, and the actual boundary of every integral generator has exact order5. This uses the determinant and does not assign an uncomputed higher Frobenius matrix.

The toric input kappa5(3121) times the four A-cusp directions passes all peripheral tests. Its full compact slice is5 Z5^3, of index125; the complete fibres are those of E115 through their actual coefficient maps. The proof specifies the tensor-extension isomorphism and its inverse separately from the literal coefficient map. Every rational compact input lifts by the actual E115 correction at one prime, which has a finite denominator and finite support.

The final GP program reconstructs every arithmetic datum without any input certificate. The Python verifier independently checks the exact rational unit identities, all residual group products, the full point count, all25 torsion points and the Weil pairing by Miller lines. The original search source, stdout, binary result and its exact E112 input are retained. The complete portable command is in the dependency ledger.

Root viewed all four standalone pages. After the independent peer requested the exact tensor-map typing, root viewed the two changed pages again and verified byte identity of the other two. The preserved earlier versions record the initial TeX delimiter failure and the repaired display width. The final mathematical audit and fresh independent replay are recorded separately before freezing.

This is a completed explicit slice of the original class-two question. Original E23 continues to retain its higher intrinsic, marked and remaining coefficient/source tasks.
''')
print(json.dumps({'status':'PASS','statement':'E.118','proof_sha256':sha(proof),'PDF_sha256':layout['PDF_sha256'],'records_written':sorted(p.name for p in ledger.iterdir())},indent=2))
