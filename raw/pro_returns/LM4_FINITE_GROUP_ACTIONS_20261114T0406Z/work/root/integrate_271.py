#!/usr/bin/env python3
"""Register the fully reviewed F32 proof and accepted exact continuations."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[2]
proof = 'work/part_a/f_nonproduct_first_character_one_images.tex'
proof_hash = 'b91fd2611f1d9bd5cde096c6307004dca0fc740463971c164aa0fe52a146af13'
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
gate = json.loads((ROOT/'work/root/final_new_claim_acceptance_271.json').read_text())
assert gate['status'] == 'PASS_ROOT_AND_PEER' and gate['proof_sha256'] == proof_hash
baseline = ROOT/'work/root/prior_270_snapshot/paper.pdf'
assert sha256(baseline.read_bytes()).hexdigest() == '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
for name in ['initial_fixed_region_continuation_acceptance.json',
             'negative_transposition_continuation_acceptance.json',
             'marked_v4_continuation_acceptance.json']:
    assert json.loads((ROOT/'work/root'/name).read_text())['status'] == 'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS'
f7 = ROOT/'work/part_a/f_centralizer_audit.tex'
f7_hash = sha256(f7.read_bytes()).hexdigest()
changes = []

def once(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new, 1)

def edit(name, operation):
    p = ROOT/name
    old = p.read_bytes()
    new = operation(old.decode()).encode()
    assert new != old, name
    p.write_bytes(new)
    changes.append({'path': name, 'old_sha256': sha256(old).hexdigest(),
                    'new_sha256': sha256(new).hexdigest()})

def assembly(s):
    s = once(s, " 'work/part_a/f_full_product_one_affine_images.tex']",
             " 'work/part_a/f_full_product_one_affine_images.tex',\n 'work/part_a/f_nonproduct_first_character_one_images.tex']")
    return once(s, " 'work/part_a/f_full_product_one_affine_images_results.json']",
                " 'work/part_a/f_full_product_one_affine_images_results.json',\n 'work/part_a/f_nonproduct_first_character_one_images_results.json']")
edit('work/root/assemble.py', assembly)
edit('work/root/pdf_qa.py', lambda s: once(s, "'F.30.', 'F.31.'", "'F.30.', 'F.31.', 'F.32.'"))

f_old = ('The remaining affine target has chi(P0)!=1; full marginal equality and the original interaction comparison remain unresolved.')
f_new = ('F32 proves every finite affine marginal image on the exact remaining locus chi(Y1)=1 and h=chi(P0)!=1. '
         'The actual boundary projection N=I-delta D/(h-1), its inverse coordinate maps and the original X1 evaluation give a five-dimensional invariant core and one-dimensional quotient. '
         'Source zero forces equal h in a common core; the exact Frobenius fixed field contains h and k1 and excludes t. '
         'Eight direct eigenrows, four determinant cases and all three simple-type comparisons give the summed restriction injection, the exact principal tuple kernel and rank6m+1. '
         'The actual coefficient and based sign maps retain every original finite field and both signs. '
         'The remaining affine character case has chi(Y1)!=1 and chi(P0)!=1; full marginal equality and the original interaction comparison remain unresolved.')
c_old = ('The initial common fixed region, compatible edge/cycle stages and controlled infinite composition remain to be constructed.')
c_new = ('The accepted initial-region continuation constructs a common fixed region over every prescribed compact quotient subpolyhedron for each actual compact based family. '
         'Finite supported extension products have explicit inverse and based formulas; pointed lifting and constant tracks retain every original sheet and deck label. '
         'The actual compact evaluation families prove the original circle extension, and both carrier and inverse-modulus bounds preserve common C0 tails. '
         'Compatible finite nested-core stages follow. Control of the accumulated correction size from the original tail envelope, the edge/cycle construction and the infinite composition remain unresolved.')
d_new = (' The accepted negative-transposition continuation proves C_F(J)=1 for the original J=alpha Inn(h)theta. '
         'The exact two-orbit/three-cusp coefficient maps, dual transgressions, half-rank restriction and finite permutation coefficients give the full equality. '
         'Its unique g with [g,v]=z has a+b=-1, full centralizer and normalizer <g>, and every transporter to z^nu v is exactly z^((nu-epsilon)/2)g^epsilon. '
         'The accepted marked V4 continuation gives the actual map C2 coproduct V4 to G and its positive restriction eta on C2 coproduct Zhat, with both inverse coproduct coordinate maps. '
         'It proves eta_F(z)=z, determinant a-b, both beta equivariance equations and exact reflection-choice transport. '
         'The full unit a-b, the image of eta, the two original cusp alignments and nonemptiness of the original T remain unresolved.')

def report(s):
    old = ('rows=[(label, current_270[label][0], current_270[label][1])\n'
           '      if label in current_270 else (label, references, state)')
    new = 'current_271 = dict(current_270)\n'
    new += "for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_271[_key]\n"
    new += '    assert _state.count(' + repr(f_old) + ') == 1\n'
    new += "    current_271[_key] = (_refs.replace('F.31', 'F.32'), _state.replace(" + repr(f_old) + ', ' + repr(f_new) + ', 1))\n'
    new += "for _key in ['Item 5', 'C.b']:\n    _refs, _state = current_271[_key]\n"
    new += '    assert _state.count(' + repr(c_old) + ') == 1\n'
    new += '    current_271[_key] = (_refs, _state.replace(' + repr(c_old) + ', ' + repr(c_new) + ', 1))\n'
    new += "_refs, _state = current_271['D.b']\ncurrent_271['D.b'] = (_refs, _state + " + repr(d_new) + ')\n'
    new += ('rows=[(label, current_271[label][0], current_271[label][1])\n'
            '      if label in current_271 else (label, references, state)')
    s = once(s, old, new)
    anchor = "add_report('work/root/research_update_270.md')"
    addition = "\nadd_report('work/root/research_update_271.md')"
    addition += "\nadd_report('work/part_a/f_nonproduct_first_character_one_images_report.txt',title='Actual affine marginal images with first character one and nontrivial boundary')"
    addition += "\nadd_report('work/part_c/compact_family_initial_fixed_region_report.txt',title='Actual common lifted fixed regions and compatible finite stages')"
    addition += "\nadd_report('work/part_d_attack/actual_gt0_negative_transposition_centralizer.txt',title='The actual negative transposition and all original cusp transporters')"
    addition += "\nadd_report('work/part_d_attack/actual_marked_v4_cusp_endomorphism.txt',title='The actual marked V4 extension and exact cusp endomorphism')"
    return once(s, anchor, anchor + addition)
edit('work/root/make_report.py', report)

def package(s):
    s = once(s, 'checkpoint_270_extra_paths.json', 'checkpoint_271_extra_paths.json')
    start = s.index('f31_manifest=ROOT/')
    end = s.index('for name in sorted(inputs):', start)
    block = s[start:end].replace('f31_', 'f32_').replace('F31', 'F32').replace(
        'f_full_product_one_affine_images', 'f_nonproduct_first_character_one_images')
    s = s[:end] + block + s[end:]
    start = s.index('for entry in f31_routes:')
    end = s.index('required = json.loads', start)
    block = s[start:end].replace('f31_', 'f32_').replace('F31', 'F32')
    return s[:end] + block + s[end:]
edit('work/root/package_deliverable.py', package)
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
assert sha256(f7.read_bytes()).hexdigest() == f7_hash
record = {'status': 'REGISTERED_REVIEWED_F32_AND_ACCEPTED_CONTINUATIONS',
          'new_claims': ['F.32'], 'proof_sha256': proof_hash,
          'earlier_f7_proof_unchanged': True, 'f7_sha256': f7_hash,
          'changes': changes, 'preserved_619_page_pdf': str(baseline.relative_to(ROOT))}
(ROOT/'work/root/integration_271_source_changes.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'changed_files': len(changes), 'new_claims': ['F.32']}, indent=2))
