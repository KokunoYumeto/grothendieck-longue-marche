#!/usr/bin/env python3
"""Integrate two fully read, peer-reviewed and independently replayed results."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_distribution_orbifold_prior_passages.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'This one-shot integration has already run.'
    paths = {
        'E66': 'research/root_E66_distribution_replay/replay.json',
        'E67': 'research/root_E67_replay/replay.json',
    }
    replay = {k: json.loads((ROOT / v).read_text()) for k, v in paths.items()}
    assert replay['E66']['status'] == 'PASS_ISOLATED_E66_DISTRIBUTION_OVERLAP'
    assert replay['E66']['all_288_actual_common_words_replayed']
    assert replay['E66']['protected_files_unchanged'] == 76
    assert replay['E67']['status'] == 'PASS_COMPLETE_ISOLATED_E67_REPLAY'
    assert replay['E67']['regenerated_six_JSON_provenance_hashes_verified']
    e66 = json.loads((ROOT / 'research/E66_authoritative_manifest.json').read_text())
    e67 = json.loads((ROOT / 'research/E67_authoritative_manifest.json').read_text())
    for name, expected in e66['sha256'].items():
        assert digest(ROOT / name) == expected, name
    for name, expected in {**e67['files'], **e67['inputs']}.items():
        assert digest(ROOT / name) == expected, name
    proofs = {
        'sections/E_distribution_overlap_agent.tex': '87f7c44d63c0a4b90136c1827f0c1366c5053f794e42e81d2d12eb74efab981f',
        'sections/E_orbifold_CM_agent.tex': '4ea79ced2b396eb1327b5ea5ad315a660da6d13f508a020f907fcb14d3ff6155',
    }
    for name, expected in proofs.items():
        assert digest(ROOT / name) == expected, name
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_cm_character_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor + '\n' +
        r'\InputIfFileExists{sections/E_distribution_overlap_agent.tex}{}{}' + '\n' +
        r'\subsection{The original orbifold signs and the complete finite norm fibres}' + '\n' +
        r'\InputIfFileExists{sections/E_orbifold_CM_agent.tex}{}{}')
    lines = new[names[1]].splitlines()
    final = 'Arbitrary finite pentagon sources remain unresolved.'
    additions = (
        ' E.66 proves the actual index-two common source of all five '
        'distribution maps and the E.62 correction group, with both '
        'explicit binary characters. All 96 final E.62 values have exactly '
        'three compatible coefficient tuples; all 288 same-word witnesses '
        'are independently replayed. Its cyclic-three source comparisons '
        'retain the complete based and induced maps and prove their direct '
        'products with the E.62 two-group through their odd abelianizations. '
        'E.67 proves the positive original Mordell orbifold sign, the exact '
        'four Gaussian frame values, and the entire twelve-evaluation '
        'N-prime correction image F3^9. Both the E.1 and E.17 origin lists '
        'are evaluated separately, each with four complete finite norm '
        'values and actual correction words. The specified order-1944 '
        'two-factor source map is generating. The full-GT discrepancy '
        'character remains unevaluated. ' + final)
    hits = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(final)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.66; E.67', row[2],
                                  row[3][:-len(final)].rstrip() + additions)) + ','
            hits += 1
    assert hits == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    body = new[names[2]]
    start = body.index('1. **E.3:**')
    end = body.index('\n', start)
    old['prior_current_E3_paragraph'] = body[start:end]
    current = (
        '1. **E.3:** The full profinite GT CM image remains undecided. '
        'E.65 identifies the exact remaining quantity as the image of '
        'the continuous quadratic character Delta restricted to full GT. '
        'Its whole gentle-group extension, arbitrary-multiplier invariance, '
        'Galois vanishing and nonzero E.58 value are proved, with the '
        'explicit multiplier-matching and cubing comparison to the specified '
        'G6 matrix fibre. E.64 gives both actual CM braid inclusions and '
        'the separately defined orbifold discrepancy characters. E.67 '
        'proves the positive original Mordell sign and computes the entire '
        'twelve-evaluation finite norm fibre for both separately evaluated '
        'origin lists. E.66 retains all 96 E.62 final values under five '
        'simultaneous distribution equations, with an exact index-two '
        'common source and all 288 same-word witnesses. Their common '
        'intersection is being certified. E.60 retains the full preceding '
        'boundary and congruence family through 3.A6. The 2.A6 target has '
        'a completely replayed perfect kernel and the specified solvable '
        'quotient of order 96. Its signed source has exact relative kernel '
        'dimension 125 and an identified candidate common quotient whose '
        'remaining source factorization is being checked. Preservation of '
        'the E.59/E.62 binary values requires its actual common-source '
        'comparison. Direct discrepancy and further central-cover tests '
        'continue. No completed finite family is asserted cofinal.')
    body = body[:start] + current + body[end:]
    body += '''

## Five distribution maps on the full E.62 correction source

E.66 uses the actual E.17 representatives retained in E.62. Their origin words are named explicitly; the initial E.1-only citation was corrected and its prior draft preserved. The induced degree-5223 source retains every cyclic coordinate for n=2,3,4,6,12 together with the actual E.62 source. The derived image is computed before restriction to the five coordinate-zero blocks. Its exact common image in C times J has order356241767399424 and index two. The common characters are the zero-based E.62 mask175728 and the lower-left entry divided by two in the signed modulo-four matrix of the n=3 coordinate. Every basis product and every common strong generator is checked under these actual maps.

Each of the96 final E.62 values admits exactly three coefficient tuples satisfying all five distribution equations and the retained multiplicative coefficient identities. The c3 values are0,2,4; the even c2 value is fixed by the actual origin. All288 successful memberships are converted to literal words in N_B-prime and replayed in all5223 points, retaining the precise correction coordinate. The separate cyclic-three source has abelianization C3 in both its three-coordinate and full induced versions. Goursat applied to the specified maps proves its full direct product with the E.62 two-group; no extra equation on an unevaluated conjugate coordinate is imposed.

Root and geometry read the full E.66 proof and all three programs. Root's fresh isolated replay passed in20.301921seconds, with all four complete certificates and every mathematical JSON/NPZ value identical; all76 protected originals are unchanged. The288 actual common words all replayed. The source does not claim generation in the additional distribution refinement or assign the full-GT character.

## Original orbifold signs and complete finite norm fibres

E.67 retains the literal affine quotients V semidirect C6 and V semidirect C4, of orders54 and36, with V=F3 squared. Their based Ferrari generators and exact deck maps identify the quotient kernels. In the Mordell factor, the exact deck-zero z-frame forces the positive-line scalar to be one. Consequently the remaining sign is precisely the specified discrepancy sign. The Gaussian frame equation B e1=e1-v gives the four complete determinant-one values and the explicit parity v2 squared.

All twelve actual substitutions of the same word are retained. Evaluating all4656 original N_B commutators and every97-generator normal conjugation gives the exact correction image F3^9, the product of the displayed rank-three Mordell and rank-six Gaussian spaces. Literal pivot words and both inclusions in the printed formula are checked. Every original N_B sixth power is killed by the full exponent argument, proving equality with the K6 image. The nine framed Mordell targets retain their three-element frame ambiguity; each actual origin coset meets them in exactly one. All four Gaussian targets are attained. Both the E.1 and E.17 origin families are independently evaluated, with96 literal corrections in each family and no transfer of their vectors. The resulting exact word fibres are cosets of the specified full evaluation kernel. Generation is proved for the actual order1944 two-factor source by the product of its two explicit automorphisms.

Root and arithmetic read the complete E.67 proof and all four program sources. Root's isolated replay passed in285.135576seconds. Every mathematical JSON field and all exported NPZ arrays agree, including every literal generator and both origin arrays. The variable elapsed-time provenance hashes are checked against the actual regenerated bytes; no mathematical field is omitted. All20 protected original files remain unchanged. The separate four-page TeX build has zero overfull boxes and no undefined citations, with all four pages individually inspected; the integrated paper retains its own build and visual gate. The earlier fixed-word failures and initial six-evaluation attempt remain preserved.
'''
    new[names[2]] = body
    new[names[3]] += '''

163. The 2.A6 target's five complete derived chains pass a fresh complete
     replay, with3091439 final relations and indices1,2,6,96,96.
     Independent DAG substitutions and the specified S_L map give exact
     quotient orders96,48,16,1,1. The terminal group is perfect and is
     the entire kernel of this quotient. Profinite peer read of the full
     target proof and five programs passes. The initial incorrect kernel
     docstring and the failed registration-ID lookup are separately
     preserved with their exact fixes. Source integration awaits its
     final common-quotient proof.

164. E66 root isolated replay PASS20.301921seconds: four complete
     certificates, all mathematical JSON/NPZ values and288 same-word
     witnesses agree, with76 original files unchanged. Root and geometry
     full proof/program reads pass. The E17 origin correction is explicit.

165. E67 root isolated replay PASS285.135576seconds: all four programs,
     mathematical JSON values and every exported NPZ array agree. Both
     actual origin lists and all correction words are retained. Regenerated
     timing-dependent provenance hashes are separately checked. Root and
     arithmetic full proof/program reads pass;20 originals are unchanged.

166. Exact binary-overlap probes are retained under
     e_a6_double_binary_overlap_probe_root and e_a6_double_E62_word_probe_root.
     The stable ternary six-space acts trivially on the old binary six-space;
     its commutator rank is0, while the new central binary pairing has rank3.
     Of125 named old-J-identity N words, only11 have E62 values in its
     N-prime image. None of the six chosen module lifts has such a value;
     all15 pair commutators do. Thus these particular literal N words cannot
     be substituted for unspecified deep N-prime preimages. The full binary
     comparison remains active; no whole-fibre inference uses this probe.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    result = {'statements': ['E.66', 'E.67'],
              'full_root_proof_and_program_reads': True,
              'independent_peer_proof_reads': True,
              'root_replay_records': paths,
              'proof_sha256': proofs,
              'preserved_prior_passages': str(SAVED.relative_to(ROOT)),
              'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_distribution_orbifold_acceptance.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
