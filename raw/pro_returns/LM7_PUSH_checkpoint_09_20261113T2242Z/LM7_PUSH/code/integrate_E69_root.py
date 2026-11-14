#!/usr/bin/env python3
"""Integrate E69 after complete root replay and independent proof review."""
from pathlib import Path
from hashlib import sha256
import ast
import json
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_gaussian_central_prior_passages.json'


def main():
    assert not SAVED.exists(), 'This integration has already run.'
    manifest_path = ROOT / 'research/E69_authoritative_manifest.json'
    assert sha256(manifest_path.read_bytes()).hexdigest() == '89fefb9a80be5e2d75266db03ddb58c39a19861d1908d03d5c2b6f72a6030fc1'
    manifest = json.loads(manifest_path.read_text())
    for name, expected in {**manifest['files'], **manifest['inputs']}.items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    proof = 'sections/E_gaussian_central_agent.tex'
    proof_hash = sha256((ROOT / proof).read_bytes()).hexdigest()
    assert proof_hash == '649129f4d94d3f1e8e6d0df3fcf325a9db8706a6827a566f43cf32303575cae3'
    replay_dir = ROOT / 'research/root_E69_replay'
    replay = json.loads((replay_dir / 'replay.json').read_text())
    assert replay['status'] == 'PASS_COMPLETE_ISOLATED_E69_REPLAY'
    assert replay['protected_originals_unchanged'] == 34
    assert len(replay['results']) == 4
    assert all(row['status'] == 'PASS' and row['all_mathematical_JSON_fields_identical']
               for row in replay['results'])
    array_checks = []
    for stem in ['bc_gaussian_heisenberg_source', 'bc_gaussian_heisenberg_joint']:
        original = np.load(ROOT / 'code' / (stem + '.npz'))
        rerun = np.load(replay_dir / 'code' / (stem + '.npz'))
        assert set(original.files) == set(rerun.files)
        for name in original.files:
            a, b = original[name], rerun[name]
            assert a.dtype == b.dtype and a.shape == b.shape and np.array_equal(a, b), name
            array_checks.append({'archive': stem, 'array': name,
                                 'dtype': str(a.dtype), 'shape': list(a.shape)})
    peer = ROOT / 'research/A_E69_independent_review.md'
    peer_text = peer.read_text()
    assert 'Result: PASS.' in peer_text and proof_hash in peer_text
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_distribution_orbifold_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor + '\n' +
        r'\InputIfFileExists{sections/E_gaussian_central_agent.tex}{}{}')
    ending = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.69 retains the first Gaussian central layer with its actual '
        'six substitutions. Its complete correction image is the product '
        'of the Mordell rank-three space and three Heisenberg groups of '
        'order27, of total order3^12. The exact E.67 projection is its '
        'abelianization; E.68 therefore proves the common E.66 source '
        'is the full product of order189321481108517289984. Each of the '
        '1152 retained combinations has three Gaussian framed lifts, '
        'and all3456 actual common N-prime words are replayed. The full '
        'word fibres retain the specified common kernel. ' + ending)
    lines = new[names[1]].splitlines()
    hits = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(ending)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.69', row[2],
                                  row[3][:-len(ending)].rstrip() + addition)) + ','
            hits += 1
    assert hits == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    anchor = ('E.68 proves that their actual common N_B-prime image is the full '
              'product and supplies all1152 simultaneous word witnesses.')
    assert new[names[2]].count(anchor) == 1
    new[names[2]] = new[names[2]].replace(anchor, anchor +
        ' E.69 retains the first Gaussian central layer and gives all3456 '
        'common framed lifts, with the same E.66 values and exact kernel-coset fibres.')
    new[names[2]] += '''

## The Gaussian central layer and its full common finite fibres

E.69 constructs the actual order108 Gaussian triangle quotient H3 semidirect C4 directly from the based free-by-cyclic presentation. Here H3 is the order27 exponent-three Heisenberg group. It retains x fourth power as the inverse primitive commutator, y squared and z fourth power as the identity, and all six ordered substitutions. Exhausting the729 deck-zero frame pairs gives four automorphisms, the literal conjugations by the first four powers of x, and36 framed pairs. The complete six-evaluation correction image retains precisely12 of those pairs, three over each old Gaussian action.

The same97 N_B words are evaluated in all twelve Mordell and Gaussian maps. All4656 pairwise commutators, every original normal conjugation and every bracket give exactly the product of the rank-three Mordell space with three copies of H3, of order3^12. Literal row-operation words are retained by the exact class-two formula log(a b [a,b])=log(a)+log(b). The new three-dimensional derived center is exactly the kernel of the actual E.67 projection. Thus that particular projection is the abelianization map. All N_B sixth powers vanish, proving equality of the K6 and N_B-prime images.

The actual common image with E.66 is Z times this Heisenberg product. A common quotient with the finite three-group would have a cyclic order-three quotient, factoring through the displayed E.67 abelianization; E.68 excludes it through the same source maps. Its order is189321481108517289984. Six old-kernel words give the horizontal Gaussian basis, and their three paired commutators give the entire new center. Their old values are independently checked to be the identity on all5223 old induced points. Each of E.68's1152 words then has exactly three prescribed Gaussian framed lifts. All3456 actual common words are replayed through35076 DAG ancestors, retaining their old coordinates and the complete common-kernel coset fibre. This theorem makes precisely the stated finite source and word-fibre claims.

Root and arithmetic read the whole proof and all four mathematical programs. Root's isolated replay passes in12.548128seconds; every mathematical JSON field and NPZ array agrees, all34 protected originals are unchanged, and every omitted input provenance hash is validated against its exact file bytes. Integration also compares every NPZ dtype and shape. All three standalone pages were viewed, with zero overfull boxes and zero warnings. The initial exploratory model and environment-specific failed build records remain preserved.
'''
    new[names[3]] += '''

172. E69 complete root and arithmetic proof/program reads PASS. Root
     isolated replay PASS12.548128seconds: all four mathematical outputs,
     every array value, shape and dtype, and all3456 actual common words
     agree;34 protected originals remain unchanged. The Gaussian central
     quotient has correction image M times Heis3 cubed and its actual
     E67 projection is precisely its abelianization. The same-map Goursat
     argument gives the full E66 product, with all three central lifts
     over each old combination and exact word-kernel fibres. E3 remains
     open. Entries170--171 are reserved for the complete E63 integration.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    acceptance = {
        'statement': 'E.69', 'full_root_and_peer_reads': True,
        'peer_review': str(peer.relative_to(ROOT)),
        'peer_review_sha256': sha256(peer.read_bytes()).hexdigest(),
        'isolated_root_replay': 'research/root_E69_replay/replay.json',
        'proof_sha256': proof_hash, 'array_shape_dtype_checks': array_checks,
        'preserved_prior_passages': str(SAVED.relative_to(ROOT)),
        'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_gaussian_central_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    print(json.dumps(acceptance, indent=2), flush=True)


if __name__ == '__main__':
    main()
