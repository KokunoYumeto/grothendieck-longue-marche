#!/usr/bin/env python3
"""Integrate the fully audited E62 common matrix-cover fibres once."""
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_GL23_prior_passages.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'One-shot E62 integration already performed.'
    replay = json.loads((ROOT / 'research/root_E62_replay/result.json').read_text())
    assert replay['status'] == 'PASS_ISOLATED_COMPLETE_E62_REPLAY'
    assert replay['all_mathematical_outputs_identical'] and replay['protected_original_files_unchanged']
    assert replay['complete_generation_certificate_count'] == 960
    assert len(replay['complete_certificates_replayed']) == 1011
    manifest_path = ROOT / 'research/E62_authoritative_manifest.json'
    assert sha(manifest_path) == replay['manifest_sha256'] == '70a8877f919281244be269ccc02e3bb7d5814151c885cdf152fa590081e9efc5'
    manifest = json.loads(manifest_path.read_text())
    for name, record in manifest['files'].items():
        assert sha(ROOT / name) == record['sha256'], name
    proof = ROOT / 'sections/E_gl23_ferrari_agent.tex'
    assert sha(proof) == '7d7cc35227480fa84c0a7ca0f1879564b6b5bd4926005d29a9ac5ca8825029aa'
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_genus_one_sewing_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor+'\n'+
        r'\InputIfFileExists{sections/E_gl23_ferrari_agent.tex}{}{}')
    lines = new[names[1]].splitlines()
    count = 0
    final = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.62 retains all 18 literal GL2(F3) epikernels and their actual '
        'common source and target with E.59. The full K6 correction groups '
        'have orders 2^21 and 2^24; their central derived groups have orders '
        '2^3 and 2^6. Every specified G6 fibre has 16 GL gentle values and '
        '32 common gentle values, with four final pentagon/braid values in '
        'each test. The four common final values map two-to-one onto only '
        'two of the four GL-only final values and onto both E.59 final '
        'values. All 24 CM pairs survive. All source and target generation '
        'claims, the complete G6 fibre product and the actual N-prime words '
        'are proved; root replay passes all 1011 complete certificates, '
        'including 960 generation certificates. '+final)
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] != 'E.3':
            continue
        assert row[2] == 'OPEN: full GT image' and row[3].endswith(final)
        old['prior_E3_coverage_row'] = row
        lines[i] = ' '+repr((row[0], row[1]+'; E.62', row[2],
                             row[3][:-len(final)].rstrip()+addition))+','
        count += 1
    assert count == 1
    new[names[1]] = '\n'.join(lines)+'\n'
    body = new[names[2]]
    start = body.index('1. **E.3:**')
    end = body.index('\n', start)
    old['prior_current_E3_paragraph'] = body[start:end]
    current = (
        '1. **E.3:** The full profinite GT CM image remains undecided. '
        'E.58 constructs an actual full gentle pair with positive extra '
        'CM bits (1,0). E.17--E.57 retain their specified finite, boundary '
        'and uniform congruence families. E.59 and E.62 exhaust the '
        'complete SL2(F3), GL2(F3), and common correction groups over '
        'all 24 specified E.17 G6 points. The common group has 2^24 '
        'corrections per point, 32 gentle values and four final '
        'pentagon/braid values. All 24 CM pairs, including 12 extra '
        'pairs, survive with full actual source and target generation. '
        'The common projection removes two of the four GL-only final '
        'values; it preserves both SL-only final values. E.61 proves '
        'the signed modulus-twelve genus-one sewing identity for every '
        'normalized multiplier-one gentle pair. The central-three A6 '
        'source has passed full isolated root replay and its exact '
        'closed correction bridge is under final target review. The '
        'new central-double A6 source has a completed, independently '
        'replayed 128-dimensional binary kernel; its residual and fibre '
        'calculations are active. The geometric route now retains an '
        'explicit full profinite Mordell B3 inclusion and the actual '
        'difference between its induced and orbifold actions. The two '
        'positive CM characters are being compared at their specified '
        'finite maps. Compatibility through every finite pentagon '
        'quotient, or a complete exclusion of all extra CM fibres, '
        'remains to be proved.')
    body = body[:start]+current+body[end:]
    body += '''

## The complete GL2(F3) fibres and their actual common SL2(F3) source

E.62 is integrated after complete root and independent peer proof/program reads and a full isolated replay. The literal matrix enumeration has48 elements,864 ordered generating pairs,48 actual automorphisms and18 epimorphism kernels. The determinant-one inclusion, restriction of all automorphisms and four-line projective action are actual saved maps. The Ferrari free image has order2^23 times3^3, its Nielsen image has order2^16 times3^7, and the full target has order2^39 times3^10. The free coordinates are retained jointly; no independence of the18 factors is assumed.

The GL source has order2^29 times3^6 and faithful degree2808. Its actual common block source with E.59 has order2^41 times3^6, and their common target has order2^63 times3^12. The source block kernels have orders2^12 over GL and2^15 over SL. These nontrivial kernels disprove exactly the two proposed factorizations of the specified source maps, by the graph-of-a-homomorphism comparison. The corresponding target projections have kernels2^24 times3^2 and2^34 times3^8. No conclusion about arbitrary homomorphisms between the underlying groups is substituted for these actual quotient-map statements.

The whole K6 correction groups are the actual N_B-derived images, of orders2^21 and2^24. Their derived subgroups are central elementary abelian of dimensions3 and6, and their quotient dimensions are18. Every coordinate-prefix subgroup has a complete Schreier certificate. All97 original sixth powers belong to the correction group, and each coordinate generator has a retained literal N_B-prime word, with its exact embedding into F. The ordered class-two product retains every basis square and commutator term. The source cycles are imposed first on the18-dimensional quotient and then on all remaining central coordinates. This exhausts the full correction fibres.

For each of the24 specified G6 points, the GL-only fibre has16 gentle values and four final pentagon/braid values. The common fibre has32 gentle values and four simultaneous final values. Among those32 common gentle values, the GL pentagon passes on eight and the SL pentagon on16; their intersection has four. Both literal full twists are fixed throughout the gentle fibres. The common final values project two-to-one onto exactly two of the four GL-only final values and two-to-one onto both E.59 final values. Every positive CM matrix pair, including all12 extra pairs, remains represented.

All768 common gentle source points,96 common final target points, and96 GL-only final target points have full generation certificates. The actual quotient to Q retains N_B as its exact preimage. The subdirect comparison of the N_B images with the abelian G6 image contains the entire new N_B-derived correction group and proves generation in the full common source with G6 itself. Thus every count and generation assertion concerns the same literal word in all components.

The isolated root replay completed in651.328seconds. Every mathematical JSON field, every NPZ array and every complete chain output agrees with the frozen originals. All1011 complete certificates were replayed, including all960 generation certificates and all40 coordinate certificates; all4183 protected files remain unchanged. The earlier incorrect old-output filename, initial TeX overflow, and manifest self-stdout hash failure remain preserved. The final five-page standalone TeX build and visual checks are also retained. This integration saves the entire previous active passages and edited files in research/checkpoint09_GL23_prior_passages.json. The report continues to mark E.3 Open.
'''
    new[names[2]] = body
    new[names[3]] += '''

153. E62 full isolated root replay PASS,651.328seconds. All1011 complete
     certificates, including960 generation and40 coordinate certificates,
     were replayed. Every mathematical JSON field and NPZ array agrees,
     and all4183 protected files are unchanged. Root's complete proof
     and all-new-program reads and the independent profinite_images
     review pass. The actual common source, full class-two fibres,
     complete G6 comparison and strict4-to2 GL final projection are
     integrated. E3 remains the sole Open task.
'''
    SAVED.write_text(json.dumps(old, indent=2)+'\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    result = {'statements': ['E.62'], 'root_complete_proof_and_new_programs_read': True,
              'independent_profinite_images_proof_and_code_read': True,
              'root_isolated_replay_seconds': replay['seconds'],
              'complete_certificates_replayed': 1011, 'generation_certificates_replayed': 960,
              'protected_original_files_unchanged': len(manifest['files']),
              'proof_sha256': sha(proof), 'manifest_sha256': sha(manifest_path),
              'preserved_previous_files_and_passages': str(SAVED.relative_to(ROOT)),
              'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_GL23_acceptance.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
