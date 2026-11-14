#!/usr/bin/env python3
"""One-shot integration of the completely replayed E68 common source."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_joint_distribution_orbifold_prior_passages.json'


def main():
    assert not SAVED.exists(), 'This integration has already run.'
    manifest_path = ROOT / 'research/E68_authoritative_manifest.json'
    assert sha256(manifest_path.read_bytes()).hexdigest() == '3c87a264cf516c617e1df00b3bf60e0f47ce61ea52a8e857c5fc9d081cb45d2a'
    manifest = json.loads(manifest_path.read_text())
    for name, expected in manifest['sha256'].items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    proof = 'sections/E_distribution_orbifold_agent.tex'
    proof_hash = sha256((ROOT / proof).read_bytes()).hexdigest()
    assert proof_hash == '64f01ce27a8156b223f4a40735ac0833b94bc792817334049f5be6ddfcbfb309'
    replay = json.loads((ROOT / 'research/root_E68_replay/replay.json').read_text())
    assert replay['status'] == 'PASS_ISOLATED_E68_COMMON_SOURCE'
    assert replay['all_1152_actual_common_words_replayed']
    assert replay['protected_files_unchanged'] == 88
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_orbifold_CM_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor + '\n' +
        r'\InputIfFileExists{sections/E_distribution_orbifold_agent.tex}{}{}')
    final = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.68 computes the actual common N-prime image of E.66 and '
        'E.67 as their full direct product, of order '
        '7011906707722862592. All 1152 combinations over the separately '
        'evaluated E.17 origins have literal common N-prime witnesses. '
        'Every retained E.62 final value, each of its three distribution '
        'tuples and all four orbifold norm values coexist. The whole word '
        'fibre is the displayed coset of the actual common kernel. ' + final)
    lines = new[names[1]].splitlines()
    hits = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(final)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.68', row[2],
                                  row[3][:-len(final)].rstrip() + addition)) + ','
            hits += 1
    assert hits == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    phrase = 'Their common intersection is being certified.'
    assert new[names[2]].count(phrase) == 1
    new[names[2]] = new[names[2]].replace(phrase,
        'E.68 proves that their actual common N_B-prime image is the full '
        'product and supplies all1152 simultaneous word witnesses.')
    new[names[2]] += '''

## The exact simultaneous distribution and orbifold source

E.68 computes the image of the same N_B-prime under the E.66 and E.67 maps. It begins with the actual common degree5331 source, compares every one of the97 literal N_B words, and replays them in both factors. Only after computing the full derived image does it project to the five distribution coordinate-zero blocks. The resulting degree4957 image has order7011906707722862592, exactly the product356241767399424 times3^9. Both projections are onto through their retained word maps, so this order equality proves the full direct product. The calculation retains the possible three-primary overlap until this complete comparison removes it.

Each E17 origin is independently reevaluated in the twelve orbifold maps. The complete finite lists have four E.62 correction coordinates, three distribution coefficient tuples for each, and four orbifold norm targets. All48 combinations per origin,1152 in total, have actual preimages in N_B-prime. The witness program substitutes the projected transversal words through the full derived-source DAG and replays24363 ancestors on all5331 points. Every resulting word attains its exact Ferrari correction, all five distribution values and all twelve orbifold values. The entire word fibre is the specified coset of the common kernel. Generation of an enlarged distribution source and a full-GT realization remain outside this finite statement.

Root and geometry read the whole proof and both mathematical programs. Root's isolated replay passes in23.535915seconds: both mathematical JSON/NPZ outputs, all four complete certificates and all1152 words agree; all88 protected files are unchanged. The first replay stopped because the witness retained the byte hash of a parent JSON containing elapsed time. Its driver, output, diagnosis, prior manifest and an unrun alternative are preserved. The accepted driver verifies both recorded parent hashes against their actual bytes and excludes only that single timing-dependent provenance value from mathematical equality; every fixed hash and every mathematical field remains exact.
'''
    new[names[3]] += '''

167. E68 full root and geometry proof/program reads PASS. Root isolated
     replay PASS23.535915seconds: all four complete certificates, all
     mathematical JSON/NPZ values and1152 literal common words agree;
     all88 originals remain unchanged. The exact common quotient is
     trivial, giving the full E66-by-E67 product on the same N_B-prime.
     The actual E17 origin maps and full kernel-coset fibres are retained.

168. Root and profinite prove the exact joint2.A6/3.A6 target over the
     actual old signed-A6 target. The triple relative kernel maps onto
     ASL2(F3), with kernel3^105; the affine abelianization has order3.
     It has no nontrivial two-group quotient, while the double relative
     kernel is elementary abelian2^151. Goursat gives the full fibre
     product, order2^5573^2715^1177^8 11^3 13^2. The specified solvable
     quotient remains order20736, with a perfect kernel proved by its
     two- and three-primary abelianization bounds. Actual T23, uniform
     and Hurwitz arrows are retained. New target fragment tagsE63.36--38
     and the exact order certificate pass peer read.

169. Additional primary-source scope check: Nakamura--Tsunogai,
     Harmonic equations in the Grothendieck--Teichmuller group,
     RIMS Kokyuroku1267(2002),197--208, opened at
     https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1267-18.pdf.
     Theorems1--2 and their corollary explicitly concern the Galois image;
     the opening discussion leaves their full-GT subgroup comparison
     undecided. Section5 records the full-GT cyclic Kummer cocycles and
     a further hypothesis for comparison with the accessory cocycle.
     These formulas are retained as source comparisons, not used as a
     full-GT vanishing theorem. Chinburg's ICTS January2024 slides,
     https://www.icts.res.in/sites/default/files/seminar%20doc%20files/Ted%20Chinburg%2004.01.2024.pdf,
     slides20--23 were opened as well: the modular-family representation
     extension carries explicit subgroup-stabilization and linear-lift
     conditions. It does not assign the remaining character here.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    result = {'statement': 'E.68', 'full_root_and_peer_reads': True,
              'isolated_root_replay': 'research/root_E68_replay/replay.json',
              'proof_sha256': proof_hash,
              'preserved_prior_passages': str(SAVED.relative_to(ROOT)),
              'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_joint_distribution_orbifold_acceptance.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
