#!/usr/bin/env python3
"""Integrate the twice-read D43 proof and preserve the D42 alignment repair."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    section = ROOT / 'sections/D_inverse_base_agent.tex'
    assert sha256(section.read_bytes()).hexdigest() == 'fb7213549a4ca52ca2e2875914fbb13f04c5568f0a93cbccc2a422ef8261c60c'
    saved = ROOT / 'research/checkpoint07_inverse_base_prior_passages.json'
    assert not saved.exists()
    old = {}
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("('"):
            continue
        row = ast.literal_eval(stripped.rstrip(','))
        if row[0] == 'D.1':
            old['D.1'] = row
            assert 'D.43' not in row[1]
            previous = (r'Every D.37 parameter lifts through each characteristic relative-two stage and then its full relative pro-$p$ cover for odd $p\ne5$, retaining the exact maximal pro-five quotient $P_n$. ')
            replacement = (r'Over every actual pro-prime-to-$p$ quotient, the entire peripheral automorphism fibre is the nonempty compact inverse limit of the finite-base fibres, through proved descent maps. '
                           r'Every D.37 parameter therefore lifts compatibly to the single actual quotient $\widehat F/O^p(O^2(K_n))$ for odd $p\ne5$, retaining a chosen full relative pro-two lift and the exact maximal pro-five quotient $P_n$. ')
            assert previous in row[3]
            lines[i] = ' ' + repr((row[0], row[1] + '; D.43', row[2], row[3].replace(previous, replacement))) + ','
    assert 'D.1' in old

    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    text = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/D_even_base_agent.tex}{}{}'
    assert text.count(anchor) == 1
    assert 'sections/D_inverse_base_agent.tex' not in text
    text = text.replace(anchor, anchor + '\n' + r'\InputIfFileExists{sections/D_inverse_base_agent.tex}{}{}')

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor) == 1
    paragraph = r'''
D.43 proves the complete relative pro-$p$ lift over an actual infinite pro-prime-to-$p$ base. The equality $\bigcap_j O^p(K_j)=O^p(K)$ is proved through every actual finite quotient of the source. At two finite-base stages, the transition kernel is exactly the pro-$p$ residual of the inverse image of the lower base kernel; every upper automorphism therefore descends. This supplies an actual inverse system of the complete compact peripheral fibres. Compactness gives one compatible automorphism without an assumption that the fibre transitions are surjective, and nested closed conjugator sets retain the three prescribed projections exactly. The all-source factorization uses Hopficity of the two-generated whole quotient, with no finite-generation assumption on the relative kernel. Applied to D.37, the single quotient $\widehat F/O^p(O^2(K_n))$ retains a chosen full relative pro-two lift, every two-primary stage and its relative $p$-central stages, and exactly $P_n$ as its maximal pro-five quotient. Two independent complete proof readings passed. The theorem settles the compatibility step left within D.42; the full D.1 and D.2 source comparisons remain under investigation.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    begin = body.index('1. **D.1--D.2:**')
    end = body.index('\n2. **E.2--E.3:**', begin)
    old['remaining_D_paragraph'] = body[begin:end]
    current = body[begin:end]
    previous = ('The next comparison concerns actual even bases and successive extensions with kernels involving more than one prime; '
                'the extra symmetry equations for D.2 also remain to be imposed on these fibres.')
    replacement = ('D.42 supplies the actual even-base comparison, and D.43 supplies the compatible infinite coprime-base lift. '
                   'The extra symmetry equations for D.2 remain to be imposed through their actual braid-source maps.')
    assert previous in current
    current = current.replace(previous, replacement)
    previous = ('The active extensions concern compatibility through infinite coprime bases, primes dividing the current base order, '
                'and nonabelian chief factors with nontrivial odd outer action.')
    replacement = (r'D.43 identifies the entire infinite-base fibre with the compact inverse limit through exact descent maps and gives '
                   r'$\widehat F/O^p(O^2(K_n))$ with the specified maximal pro-five quotient. '
                   r'The active extensions concern the gentle normalization on the actual $C_2*C_3$ source, '
                   r'primes dividing the current base order, and nonabelian chief factors with nontrivial odd outer action.')
    assert previous in current
    body = body[:begin] + current.replace(previous, replacement) + body[end:]

    even = ROOT / 'sections/D_even_base_agent.tex'
    even_text = even.read_text()
    assert sha256(even.read_bytes()).hexdigest() == '715596a4a61e3d0d66021eb99ac966d543dc041903c8855b02fb00fb1bf851c7'
    start = even_text.index('\\[\n \\begin{split}\n R_2&=')
    finish = even_text.index('\\tag{D.42.17}', start)
    old['D.42.17_alignment'] = even_text[start:finish]
    updated = old['D.42.17_alignment'].replace(r'\begin{split}', r'\begin{aligned}').replace(r'\end{split}', r'\end{aligned}')
    assert updated != old['D.42.17_alignment']
    even_text = even_text[:start] + updated + even_text[finish:]

    saved.write_text(json.dumps(old, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(text)
    report.write_text(body)
    even.write_text(even_text)
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

107. D43 passes root and geometry independent complete proof readings.
     Both audit the residual equality through actual finite source maps,
     the exact characteristic transition kernels and automorphism descent,
     the compact inverse fibre without surjectivity of its transitions,
     and the nested exact-conjugator sets. Whole-quotient Hopficity proves
     all-source factorization without finite generation of the kernel.
     The two-then-p application retains precisely the original P_n quotient.
     D43 is integrated; the four outstanding task rows remain open.

108. The second checkpoint07 build fails during LuaLaTeX pass1 in
     D.42.17: split was used for two aligned equation pairs. The complete
     attempt and its source snapshot are preserved as checkpoint07_second_failure.
     No new PDF was produced. The repair changes only that environment
     to aligned; the exact prior source passage is separately preserved.
''')
    print(json.dumps({'integrated': ['D.43'],
                      'proof_readers': ['root', 'geometry'],
                      'preserved_passages': str(saved.relative_to(ROOT)),
                      'typography_repair': 'D.42.17 split to aligned',
                      'unresolved_tasks': ['D.1', 'D.2', 'E.2', 'E.3']}, indent=2))


if __name__ == '__main__':
    main()
