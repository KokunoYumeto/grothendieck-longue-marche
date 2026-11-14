#!/usr/bin/env python3
"""Seal the independent full mathematical J-centralizer audit."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'work/part_c/review_actual_gt0_negative_transposition_centralizer.json'
REPORT = OUT.with_suffix('.txt')
AUTHOR = ROOT/'work/part_d_attack/actual_gt0_negative_transposition_centralizer_result.json'

def bind(p):
    p = ROOT/p if isinstance(p,str) else p
    raw = p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),
            'sha256':sha256(raw).hexdigest(),'lines':len(raw.decode().splitlines())}

def binary_bind(p):
    raw = p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

assert not OUT.exists(), 'Never overwrite a sealed independent audit.'
assert bind(AUTHOR)['sha256'] == 'c14bd3c196a0620c2cd2c3cae97b20a875d7881c0532b3488f09f69a6925fda6'
author = json.loads(AUTHOR.read_text())
checked = []
for row in author['files']+author['dependencies']:
    actual = bind(row['path'])
    assert actual == {k:row[k] for k in actual}
    checked.append(actual)
assert checked[0]['sha256'] == 'f752c55462f13ad58779bcb01791b18c7bd4db1c5645e09f3316f19042d99385'
assert checked[0]['lines'] == 283
source = author['primary_source_read_scope'][0]
for key in ['pdf','text']:
    p = ROOT/source[key]['path']
    actual = binary_bind(p)
    assert all(actual[k] == source[key][k] for k in actual)

full_reads = [
    ('work/part_d_attack/actual_gt0_negative_transposition_centralizer.txt',283),
    ('work/part_d_attack/actual_gt0_negative_transposition_centralizer_result.json',89),
    ('work/part_c/d74.tex',646),
    ('work/part_c/d37.tex',312),
    ('work/part_a/pure_involution_first_symmetry.tex',219),
    ('work/part_d_attack/tau_original_cusp_followup.txt',276),
]
read_bindings = []
for path,lines in full_reads:
    actual = bind(path)
    assert actual['lines'] == lines
    read_bindings.append({**actual,'read_in_full':True})

images = []
for page,digest in [
    (9,'040a1038267e77a4c5921544060c7a7d703686351ed8f59f747bb17a29be331c'),
    (10,'45c5da34535700aef59a767018da0ad542957ade6e2e2684a1076eb2a9ef560b')]:
    actual = binary_bind(ROOT/f'work/part_c/j_centralizer_peer_review/haran-{page:02d}.png')
    assert actual['sha256'] == digest
    images.append({'printed_page':page,**actual,'actually_viewed':True,
        'observation':'The real-projectivity definition, Proposition2.2 and its proof are legible.'})
previous_qa_path = ROOT/'work/part_c/render_review_619.json'
previous_qa = json.loads(previous_qa_path.read_text())
assert bind(previous_qa_path)['sha256'] == 'e1ee62c58e81aa0f0a64cfdf279287c05370e4ec9e539548bf576c11bd93d528'
for row in previous_qa['frozen_source_and_review_bindings_unchanged']:
    actual = binary_bind(ROOT/row['path'])
    assert actual == row

result = {
    'status':'PASS','reviewer':'/root/c89_review_and_general_c',
    'sealed_at_utc':datetime.now(timezone.utc).isoformat(),
    'proof':checked[0],'author_metadata':bind(AUTHOR),'report':bind(REPORT),
    'corrections_requested':[],'mathematical_issues_found':[],
    'complete_read_bindings':read_bindings,
    'author_dependency_bindings_verified':checked[1:],
    'D75_read_scope':'Hash verification as an author-listed dependency; no new full reread claimed.',
    'mathematical_checks':[
        'Actual psi and J automorphisms from the original unique h; generator identities and full multiplier.',
        'Chosen original z reflection, its square, full dihedral normalizer and both continuous inverse coordinates.',
        'Regular mod-two module, high cohomology dimension1 and one full global F-section class.',
        'Both parity-orbit coset maps with explicit inverse formulas, plus the original z-coset inverse.',
        'Complete transported v-action retaining the exchanged x/y cusp pair and its stabilizers.',
        'Actual augmentation split, continuous Hom coefficient sequence and literal subgroup restriction.',
        'Equivariant evaluation pairing and original completed surface-pair perfect duality.',
        'Positive-column cyclic coordinates, perfect dual quotients and transposed d2 maps.',
        'Shifted relative groups, finite high u-periodicity and the exact three-rank half-dimension calculation.',
        'Vanishing high D_x term, rather than an assertion of invertible u on nonzero low D_x groups.',
        'Full finite-coefficient Brown hypotheses and finite dense-image surjectivity.',
        'Exact coefficient conjugation transport, bar prism and the duplicated restriction (15).',
        'Finite permutation self-duality, distinct fixed singleton basis classes and C-invariance of restriction.',
        'Full trivial original fixed subgroup and exact normalizer maps before and after that conclusion.',
        'Haran Proposition2.2 hypotheses, closed involution set and weak finite lifting scope.',
        'Unique actual g, full abelian equation a+b=-1 and original character chi(g)=1.',
        'Both centralizer product coordinates, closed Z_p x Z_p contradiction and normalizer exponent.',
        'All full nu transporter formulas, continuous parity/half-exponent maps and inverse chi.',
    ],
    'new_coset_inverse_formulas':{
        'coordinates':'Write e=f v^epsilon with f in F and epsilon=u(e).',
        'even_x_orbit':'f D_x -> f L_x',
        'odd_y_orbit':'f v D_x -> f b L_y',
        'z_orbit':'e D_z -> (e v^{-u(e)}) L_z',
        'inverse_topology':'Continuous forward bijections from compact profinite coset spaces onto Hausdorff parity orbits; all composites verified.',
        'literal_possible_b':'b=a_z^{-1}h',
    },
    'primary_checks':{
        'brown':bind(ROOT/'work/part_c/j_centralizer_peer_review/primary_brown_check.json'),
        'haran_pdf':binary_bind(ROOT/source['pdf']['path']),
        'haran_text':bind(source['text']['path']),
        'haran_read_scope':'Definition of real projectivity, Proposition2.2 and full proof on printed pages9-10.',
        'haran_actual_view_groups':[[9,10]],'haran_images':images,
        'haran_render_exit_code':0,
        'haran_render_notice':'Type3 glyph bounding-box warnings were emitted; both pages were actually viewed and are clear. No exact warning count is asserted.',
    },
    'accepted_conclusions':[
        'C_F(J)=1 for the original actual negative transposition.',
        'The specified E_J is real projective in the stated weak finite embedding-problem sense.',
        'Unique original g with [g,v]=z and full abelian sum a+b=-1.',
        'C_F(g)=N_F(<g>)=<g>, identified with full Zhat by the split original character.',
        'Every transporter v->z^nu v is the unique displayed parity formula, with continuous inverse chi.',
    ],
    'retained_scope':[
        'No point of the original D74.40 solution set T is constructed.',
        'No local pro-p coboundary replaces the original unique h.',
        'No full-unit assertion for a-b.',
        'No generation by x,Y or g,J(g), and no original-extension free-product recognition.',
        'No new numbered claim assigned.',
    ],
    'executable_replay':'No new executable producer exists for this cohomological proof; none is claimed or substituted.',
    'plain_text_proof_compilation_or_pdf_review_claimed':False,
    'all_author_and_prior_frozen_sources_unchanged':True,
    'previous_final619_record':bind(previous_qa_path),
    'previous_frozen_bindings_reverified_count':len(previous_qa['frozen_source_and_review_bindings_unchanged']),
    'review_sealer':bind(Path(__file__).resolve()),
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','report':bind(REPORT),'metadata':bind(OUT),
    'author_proof':checked[0],'author_metadata':bind(AUTHOR)},indent=2))
