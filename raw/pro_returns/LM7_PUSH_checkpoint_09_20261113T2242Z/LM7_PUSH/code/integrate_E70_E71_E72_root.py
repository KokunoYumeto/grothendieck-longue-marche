#!/usr/bin/env python3
"""One-shot integration of the three fully replayed next source results."""
from pathlib import Path
from hashlib import sha256
import ast
import json
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_gaussian_matrix_surface_prior_passages.json'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'This integration has already run.'
    m70 = ROOT / 'research/E70_authoritative_manifest.json'
    m71 = ROOT / 'research/E71_authoritative_manifest.json'
    assert digest(m70) == 'cd413df44192e77e296acc9b0c830b9d93f1a5bd9298520d32eb4755b32498dd'
    assert digest(m71) == '6c913e1b5e5aae2bb2688fcddc131ef229527ade36b6af7c8867bc1589c68eff'
    a70, a71 = json.loads(m70.read_text()), json.loads(m71.read_text())
    for name, h in {**a70['files'], **a70['inputs'], **a71['sha256']}.items():
        assert digest(ROOT / name) == h, name
    r70 = json.loads((ROOT / 'research/root_E70_replay/replay.json').read_text())
    r71 = json.loads((ROOT / 'research/root_E71_replay/replay.json').read_text())
    r72 = json.loads((ROOT / 'research/root_E72_replay/replay.json').read_text())
    assert r70['status'] == 'PASS_COMPLETE_ISOLATED_E70_REPLAY'
    assert r71['status'] == 'PASS_ISOLATED_COMPLETE_E71_FULL_K6_FPRIME_MATRIX_FIBRES'
    assert r72['status'] == 'PASS_COMPLETE_ISOLATED_E72_ROOT_REPLAY'
    assert r70['protected_originals_unchanged'] == 70
    assert r71['all_18432_literal_source_words_replayed']
    assert r71['entire_K6_intersect_Fprime_domain_retained']
    assert len(r71['complete_certificates_exact_and_replayed']) == 6
    for name, h in r72['protected_sha256'].items():
        assert digest(ROOT / name) == h, name
    proof_hashes = {
        'sections/E_gaussian_pro3_agent.tex': '8f17c8f80e1e1b8cef70bd186a3f5ef8901ffc0c9dd0eaa13674ad89447038de',
        'sections/E_kn_matrix_agent.tex': a71['sha256']['sections/E_kn_matrix_agent.tex'],
        'sections/E_wajnryb_homology_agent.tex': '781213236c19c551250b4cfb8fecacb2e7192434af2990c0845fd2ae2dab022c'}
    for name, h in proof_hashes.items():
        assert digest(ROOT / name) == h
    array_counts = {}
    for label, stems in [('E70', a70['replay_order']), ('E71', a71['mathematical_stage_stems'])]:
        count = 0
        for stem in stems:
            p = ROOT / 'code' / (stem + '.npz')
            if not p.exists():
                continue
            q = ROOT / 'research' / ('root_' + label + '_replay') / 'code' / p.name
            a, b = np.load(p), np.load(q)
            assert a.files == b.files
            for name in a.files:
                assert a[name].dtype == b[name].dtype
                assert a[name].shape == b[name].shape
                assert np.array_equal(a[name], b[name]), (label, stem, name)
                count += 1
        array_counts[label] = count
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_gaussian_central_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    inputs = '\n'.join(r'\InputIfFileExists{' + name + '}{}{}' for name in proof_hashes)
    new[names[0]] = new[names[0]].replace(anchor, anchor + '\n' + inputs)
    ending = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.70 computes the entire Gaussian pro-three six-coordinate image '
        'as the specified fibre product of two free-group triples over '
        'their class-two quotient. Its abelianization has rank12, including '
        'all six weight-three characters. The complete same-source finite '
        'Frattini comparison proves its full product with E.66 and the '
        'unchanged finite Mordell image. All3456 E.69 finite combinations '
        'have compatible full Gaussian norm lifts. E.71 evaluates both '
        'matrix distribution equations on all34 literal GL2(F3)/SL2(F3) '
        'epikernels over the entire K6-intersect-F-prime domain. Its exact '
        'integral lattice adds95 sixth powers, and its enlargement over '
        'N-prime is the actual C4 quotient c2/6 modulo4. Every one of '
        'the1152 E.68 values admits all16 coefficient lifts modulo24, '
        'with unique finite values and18432 actual full-source words. '
        'E.72 supplies integral block-conjugation morphisms proving that '
        'the five genus-three homology evaluations have exactly the kernel '
        'of the three retained genus-two evaluations. Their same-Galois '
        'source families retain all displayed Wajnryb relations and full '
        'matrix generation. ' + ending)
    lines = new[names[1]].splitlines()
    hits = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(ending)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.70; E.71; E.72', row[2],
                                  row[3][:-len(ending)].rstrip() + addition)) + ','
            hits += 1
    assert hits == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    anchor = ('E.69 retains the first Gaussian central layer and gives all3456 '
              'common framed lifts, with the same E.66 values and exact kernel-coset fibres.')
    assert new[names[2]].count(anchor) == 1
    new[names[2]] = new[names[2]].replace(anchor, anchor +
        ' E.70 retains all these values through the entire Gaussian pro-three '
        'group. E.71 exhausts the two matrix-distribution equations over the '
        'whole K6-intersect-F-prime domain, with18432 actual words. E.72 '
        'identifies the exact genus-three homology source through its retained '
        'genus-two block maps.')
    new[names[2]] += f'''

## The complete Gaussian pro-three source

E.70 keeps the actual free-by-C4 quartic triangle. Its six-coordinate image on both N_B-prime and the whole F-prime is the fibre product of two copies of P cubed over their class-two quotients, through the displayed integral A and B maps. The upper inclusion uses exact covariance polynomials over Z[1/2] on the normal source commutator. The reverse inclusion isolates three independent gamma3(P) kernels using the literal x fourth and z fourth powers and commutators with N_B-prime. The source membership follows from the normality of N_B-prime in F; the fourth powers themselves are used in F.

The split fibre products have abelianization Z3^12. All six additional weight-three coordinates are retained in a faithful2187-element characteristic detector. Its four explicit upper-unitriangular matrix maps, order-four deck action and every literal source word are checked. The complete7869-point common N image is derived before the retained projection. All six complete Schreier presentations give the exact products with E.66 and the finite Mordell image. The full12-character map then proves the entire pro-three product by Frattini and Goursat. Coprime complement conjugacy and the two exact fixed-centralizer surjections give compatible full frames for all3456 E.69 finite combinations, with complete common-kernel word fibres.

Root read the complete proof and all four mathematical programs; profinite independently read the proof and integral-map program. Root isolated replay PASS{r70['seconds']}seconds protects70 originals, compares every mathematical output and every array value, shape and dtype, and repeats all six full Schreier calculations and independent replays. All twelve generated certificate inputs/binaries are byte-identical. All five standalone pages were viewed, with zero overfull boxes and undefined warnings. The source before its two display repairs is preserved.

## The complete matrix-distribution fibres on the whole word domain

E.71 evaluates the positive cyclic-cover equations for n=2 and3 in all18 GL2(F3) and16 SL2(F3) epikernels, using the literal left-right action on each matrix group. It retains both coefficient maps modulo24 and every E.68 value. The actual source has11691 points; its correction projection has7501. The domain is exactly K6 intersect F-prime. The integral97-generator exponent matrix has image index12 and Smith factors2,6. An explicit unimodular basis, with its integer inverse verified in both orders, gives95 kernel words whose sixth powers adjoin the whole profinite quotient6ker(e).

The entire finite correction image has order2^105·3^17. Its N_B-prime intermediate has index four, and the quotient is precisely c2/6 modulo4. The old image stays E.68's order2^42·3^13 group, with kernel2^63·3^4. A complete prescribed-base certificate proves that the70 simultaneous matrix/coefficient targets have trivial stabilizer in that kernel. Exhausting all13824 old candidates recovers exactly the1152 retained old values. Every one admits all16 coefficient lifts modulo24, giving18432 unique finite values. All actual word preimages are replayed on the full source, with exact free exponents zero and N-abelian exponents zero modulo six. The N_B-prime intermediate has exactly4608 values and is retained separately.

Root and geometry read the complete proof, all nine mathematical programs and the unchanged-engine fixed-base wrapper. Root's complete isolated replay PASS{r71['seconds']}seconds repeats all six exact presentations, all18432 word checks and every mathematical output; all{r71['protected_originals_unchanged']} protected originals remain unchanged. Every input provenance hash is verified against its actual original or regenerated bytes. Integration also checks every NPZ shape and dtype. The failed preliminary elementary-abelian guess is preserved; the complete quotient multiplication and the c2 map prove the actual cyclic answer.

## The exact genus-three homology comparison

E.72 constructs the literal integral Wajnryb chain transvections and D=T_(e1+e3), verifies the remaining relation through d3=T_(e1+e3+e5), and retains the exact genus-two and genus-four comparisons. Two unimodular symplectic bases identify all five genus-three evaluation pairs with the three old genus-two pairs. The two added scalar blocks are read from the action of the same old matrices on their stable first line. This proves equality of the actual common kernels over every integer modulus and on their profinite limits. Induction retains all six original B/F coset words; the prior eight-evaluation source therefore maps onto this complete homology source.

The same-Galois source families retain the entire corrected matrix target, with its Wajnryb relations and generation, through these explicit arrows. Root read the full proof and program. Its isolated replay PASS{r72['seconds']}seconds compares every integral identity, all90 induced transition coordinates, every mathematical array and all fixed input hashes;16 originals are unchanged. The nonlinear free-surface action and further finite surface-cover tests are separate subsequent calculations.

The integration preserves every prior main-document, coverage and report passage in checkpoint09_gaussian_matrix_surface_prior_passages.json. It also puts the three previously reserved search-ledger entries170--172 into numerical order and removes their fulfilled reservation note; those earlier exact passages remain in that preservation file.
'''
    ledger = new[names[3]]
    start172 = ledger.index('\n172. E69 complete root')
    start170 = ledger.index('\n170. E63 full source', start172)
    block172 = ledger[start172:start170]
    reservation = ' Entries170--171 are reserved for the complete E63 integration.'
    assert reservation in block172
    block172 = block172.replace(reservation, '')
    ledger = ledger[:start172] + ledger[start170:].rstrip() + '\n\n' + block172.strip() + '\n'
    ledger += f'''

173. E70 complete root proof/four-program and independent profinite proof
     reads PASS. Root isolated replay PASS{r70['seconds']}seconds: all70
     protected originals unchanged, every mathematical field and array
     exact, all six complete Schreier inputs/binaries byte-identical and
     independently replayed. The complete Gaussian pro-three source,
     all12 abelian characters, full E66/Mordell product and compatible
     lifts of every3456 E69 frame are proved through their actual maps.

174. E71 complete root and geometry proof/nine-program reads PASS.
     Root complete isolated replay PASS{r71['seconds']}seconds; all six
     complete certificates and18432 full-source words agree, with
     {r71['protected_originals_unchanged']} originals protected. The actual
     full K6-intersect-F-prime domain is obtained through6ker(e), retaining
     its index12 exponent image. The extra quotient is C4 via c2/6 mod4.
     All1152 retained values admit all16 coefficient lifts; the finite
     simultaneous stabilizer is trivial and full word fibres are given.

175. E72 full root proof/program read and isolated replay
     PASS{r72['seconds']}seconds, with16 originals unchanged. The two
     explicit integral basis maps identify every genus-three homology
     evaluation with the three retained genus-two evaluations, including
     their exact scalar characters and all90 induced transition maps.
     Thus this homology enlargement has the stated old source kernel.
     The nonlinear Wajnryb source is retained as a separate next route.
'''
    new[names[3]] = ledger
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    acceptance = {'statements': ['E.70', 'E.71', 'E.72'],
                  'full_root_proof_and_program_reads': True,
                  'root_isolated_replay_seconds': {k: r['seconds'] for k, r in
                                                  [('E70', r70), ('E71', r71), ('E72', r72)]},
                  'proof_sha256': proof_hashes, 'array_dtype_shape_counts': array_counts,
                  'preserved_prior_passages': str(SAVED.relative_to(ROOT)), 'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_gaussian_matrix_surface_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    print(json.dumps(acceptance, indent=2), flush=True)


if __name__ == '__main__':
    main()
