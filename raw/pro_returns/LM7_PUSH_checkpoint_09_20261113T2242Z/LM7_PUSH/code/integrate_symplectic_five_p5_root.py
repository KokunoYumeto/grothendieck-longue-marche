#!/usr/bin/env python3
"""Integrate E50's fully replayed source and joint-target comparison."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent

def main():
    for stem in ('audit_symplectic_five_p5_root', 'audit_symplectic_five_p5_target_root'):
        audit = json.loads((ROOT/'code'/(stem+'.json')).read_text())
        assert audit['all_passed'] and audit['original_artifacts_unchanged']
        assert all(a['literally_equal'] for s in audit['steps'] for a in s['NPZ_arrays'])
    section = ROOT/'sections/E_symplectic_five_p5_agent.tex'
    assert sha256(section.read_bytes()).hexdigest() == '26266637344abb2d82a7cf38708b072fd27463b44d4f417d922da6978b2a6c29'
    saved = ROOT/'research/checkpoint07_symplectic_p5_prior_passages.json'
    assert not saved.exists()
    old = {}
    program = ROOT/'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("('"):
            continue
        row = ast.literal_eval(stripped.rstrip(','))
        if row[0] in ('E.2', 'E.3'):
            old[row[0]] = row
            assert 'E.50' not in row[1]
            state = row[3]
            if row[0] == 'E.2':
                state = state.replace('through E.49.', 'through E.49 and E.50.')
            state += (r' The prime-five five-strand test retains all 432 multiplier-one points and every prescribed full boundary fibre. '
                      r'Its actual source of order $9000000$ has common quotient $J=A_{10}\times_{A_2}Q_{20}$ of order $72000$ with $G_L$, retaining all three signed modular bits. '
                      r'The exact residual correction in the old kernels reaches $(\mathbf Z/5)^3$, and one word gives generating maps on the full common sources and joint braid targets.')
            lines[i] = ' '+repr((row[0], row[1]+'; E.50', row[2], state))+','
    assert set(old) == {'E.2', 'E.3'}
    mainpath = ROOT/'LM7_PUSH_paper.tex'
    text = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/E_symplectic_five_root.tex}{}{}'
    assert text.count(anchor) == 1
    text = text.replace(anchor, anchor+'\n'+r'\InputIfFileExists{sections/E_symplectic_five_p5_agent.tex}{}{}')
    report = ROOT/'research/report_body.md'
    body = report.read_text()
    previous = 'The prime-five symplectic source is a separate active calculation, with its new solvable layers retained.'
    assert body.count(previous) == 1
    old['E49_closing_sentence'] = previous
    body = body.replace(previous, 'E.50 below now completes the prime-five symplectic source and its actual joint comparisons.')
    anchor = '\n## Geometric and germ results\n'
    assert body.count(anchor) == 1
    paragraph = r'''
E.50 completes the prime-five symplectic five-strand comparison. Its literal eight-evaluation, six-coset source has order 9,000,000; the actual third pentagon coordinate identifies its lower-central H residual with $C_5=\mathrm{SL}_2(\mathbf F_5)\times(\mathbf Z/5)^3$ and its N image with $\mathrm{SL}_2(\mathbf F_5)\times(\mathbf Z/5)^5$. The exact common quotient with $G_L$ is $J=A_{10}\times_{A_2}Q_{20}$ of order 72,000. Both maps to $A_2$ are checked on every value and generator edge. All 25,965 lifted Schreier relations retain the full three-coordinate binary kernel of $Q_{20}$ over the projective base; the old kernel rank stays 44. This proves the signed quotient map, including the scalar sign. The earlier one-bit attempt is preserved with the literal failed comparison and its explanation.

The closed lower-central residual of H maps onto $C_5$, kills every retained finite nilpotent boundary factor, and has image exactly $(\mathbf Z/5)^3$ after intersecting the old $G_L$ and $D_{23}$ kernels. One correction therefore retains every full two-adic and three-adic class-three fibre, all full pro-$p$ boundary factors away from two and three, and the old Ferrari/Hurwitz comparisons while matching the same actual Galois word in the new source. That Galois element has cyclotomic character one in the entire profinite unit group. The original and corrected joint sources are exactly $(G_{\rm old}\times_S G_L)\times_JG_{5,\mathrm{sp}}$. The proof explicitly checks surjectivity on H although the new source itself does not retain B/H. It proves generation directly on the actual source maps.

The joint four-strand target is $(T_{23}\times_{S_L}T_L)\times T_{5,\mathrm{sp}}^{(4)}\times A_{96}$, where the new factor has order 15,000. A complete 73,496-relator target replay gives the exact $T_L\times T_{5,\mathrm{sp}}^{(4)}$ image, and three literal derived words generate the entire new factor. The five-strand joint target is $\mathrm{Sp}_4(\mathbf F_5)\times A_{96}$. All corrected braid maps are onto and retain the stated pentagon, twist, and periodic identities. Independent proof readings cover both the source and the added target argument. Root isolated replay takes 242.635 seconds for the four source programs and 204.890 seconds for the two target programs; every mathematical JSON record and every NPZ array agrees literally, all own-location input hashes are verified, and the original artifacts are unchanged. All 24 CM fibres remain represented in the specified multiplier-one family. The full-source cofinality questions are still open.
'''
    body = body.replace(anchor, '\n'+paragraph.strip()+'\n'+anchor)
    begin = body.index('2. **E.2--E.3:**')
    end = body.index('\n', begin)
    old['remaining_E_paragraph'] = body[begin:end]
    body = body[:end] + (' E.50 now retains the entire multiplier-one boundary family through the prime-five symplectic source with exact common quotient $J$ and full joint-target generation. The next actual comparisons are the remaining order-64 layer in the full inner/free A6 source and the prime-seven symplectic source; neither is registered here as a completed theorem.') + body[end:]
    saved.write_text(json.dumps(old, indent=2)+'\n')
    program.write_text('\n'.join(lines)+'\n')
    mainpath.write_text(text)
    report.write_text(body)
    with (ROOT/'research/root_searches_02.md').open('a') as log:
        log.write('''

105. The previously inaccessible Gonzalez thesis is now opened in the
     supervisor-hosted primary PDF (turn463view0), Definition2.6.10 and
     Remark2.6.13 on printedpp90--91. The displayed pro-l comparison
     concerns the group with the pentagon retained. Marin's author PDF
     (turn468view0) and published primary text (turn480view0), Section3.3
     on printedp773, were opened and give the same equations and arrow.
     Fresse's cited primary book, Theorem11.1.7 and Chapter12, is also
     opened (turn470view0 and turn471view2). Its operadic comparison has
     the full pentagon in its source and target. The explicit projection
     of a profinite pair to its pro-l pair retains that equation, so its
     leading metabelian output lies in the proved D3 line. No lift of the
     extra peripheral or gentle directions is inferred from that arrow,
     and its displayed surjectivity is not used as an additional theorem.

106. E50 passes both complete isolated replays: source242.635s and
     target204.890s. Every mathematical JSON record and every NPZ array
     is literally equal; each input hash is checked against its own
     original or replay location. Two readers check the exact signed
     common quotient and residual correction, and the added target proof
     has a second full reading. The new H-image and its generation are
     proved explicitly without finite-kernel invariance. The full common
     quotient has order72000 and kernel125; both three-bit signs and all
     25965 source/73496 target relations are retained. E50 is integrated.
     The full A6 order64 solvable layer and prime-seven source remain
     active computations, outside this accepted statement register.
''')
    print(json.dumps({'integrated':['E.50'],
                      'preserved_passages':str(saved.relative_to(ROOT)),
                      'source_replay_seconds':242.635,
                      'target_replay_seconds':204.890,
                      'unresolved_tasks':['D.1','D.2','E.2','E.3']},indent=2))

if __name__ == '__main__':
    main()
