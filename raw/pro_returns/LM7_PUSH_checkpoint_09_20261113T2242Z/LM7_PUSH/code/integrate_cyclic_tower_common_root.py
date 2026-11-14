#!/usr/bin/env python3
"""Accept D47, D48 and E53, retaining every superseded passage."""
from hashlib import sha256
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    proofs = {'D.47': 'sections/D_cyclic_composite_agent.tex',
              'D.48': 'sections/D_return_tower_agent.tex',
              'E.53': 'sections/E_symplectic_integral_common_root.tex'}
    for ident, name in (('D.47', 'audit_cyclic_composite_root'),
                        ('D.48', 'audit_return_tower_root')):
        audit = json.loads((ROOT / 'code' / (name + '.json')).read_text())
        assert audit['all_passed'] and audit['original_artifacts_unchanged']
        assert digest(ROOT / proofs[ident]) == audit['proof_sha256']
    e53audit = json.loads((ROOT / 'code/bc_symplectic_integral_gl_comparison_audit.json').read_text())
    assert e53audit['status'].startswith('PASS') and e53audit['all_originals_unchanged']
    saved = ROOT / 'research/checkpoint08_cyclic_tower_common_prior_passages.json'
    assert not saved.exists()
    old = {ident + '_audited_source': (ROOT / path).read_text() for ident, path in proofs.items()}
    old['D46_typeset_source'] = (ROOT / 'sections/D_return_prime_agent.tex').read_text()
    old['E48_typeset_source'] = (ROOT / 'sections/E_a6_full_agent.tex').read_text()

    d48 = old['D.48_audited_source']
    anchor = '\\ker(E_n\\to D)=\\ker(J_n\\to\\Gamma)=W_n,\\\n'
    assert d48.count(anchor) == 1
    d48 = d48.replace(anchor, anchor[:-1] + '\\\n')
    anchor = 'The equalities retain the actual maps from \\(\\widehat B\\).'
    assert d48.count(anchor) == 1
    d48 = d48.replace(anchor, 'The quotient equalities are for finite \\(n\\); the kernel\n'
                      'identity also includes \\(n=\\infty\\).\n' + anchor)

    e53 = old['E.53_audited_source']
    anchor = 'by E.52.17, so it is trivial.\n'
    assert e53.count(anchor) == 1
    e53 = e53.replace(anchor, anchor +
        'The full-reduction conclusion also holds for a closed normal\n'
        'subgroup: its quotient is pro-$p$ and topologically perfect;\n'
        'every finite quotient is a perfect finite $p$-group and is\n'
        'therefore trivial.\n')
    e53 += ('\nAn independent complete proof audit and isolated replay reproduce\n'
            'every mathematical JSON entry in 4.551 seconds. A separate\n'
            'symbolic commutator calculation gives the same level-25\n'
            'matrix, and the three conjugate vectors have determinant\n'
            '$3$. All protected originals are unchanged.\n')

    d46 = old['D46_typeset_source']
    anchor = ('The literal programs\n'
              '\\texttt{bc\\_return\\_prime\\_\\allowbreak model.py} and\n'
              '\\texttt{bc\\_return\\_prime\\_\\allowbreak centralizers.py}\n'
              'construct the six-coset maps, retain actual word\n')
    assert d46.count(anchor) == 1
    d46 = d46.replace(anchor,
        'The literal model program is\n'
        '\\texttt{bc\\_return\\_prime\\_model.py}.\n'
        'Its full centralizer companion is\n'
        '\\texttt{bc\\_return\\_prime\\_centralizers.py}.\n'
        'Together they construct the six-coset maps and retain actual word\n')
    e48 = old['E48_typeset_source']
    anchor = ('The complete source-word and quotient certificates are\n'
              'listed in \\texttt{research/DE\\_a6\\_replay.md}.\n')
    assert e48.count(anchor) == 1
    e48 = e48.replace(anchor,
        'The replay guide in the research directory lists the complete\n'
        'source-word and quotient certificates:\n'
        '\\texttt{DE\\_a6\\_replay.md}.\n')

    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    additions = {'D.1': ['D.47'], 'D.2': ['D.48'],
                 'E.2': ['E.53'], 'E.3': ['E.53']}
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("('"):
            continue
        row = ast.literal_eval(stripped.rstrip(','))
        if row[0] not in additions:
            continue
        old[row[0] + '_coverage'] = row
        assert not any(v in row[1].split('; ') for v in additions[row[0]])
        state = row[3]
        if row[0] == 'D.1':
            state += (r' D.47 proves the entire chief-lift theorem for every finite cyclic '
                      r'outer group, retaining the actual nonsplit automorphism extension, '
                      r'all intermediate characters, every prescribed conjugator and the complete ordinary union.')
        elif row[0] == 'D.2':
            state += (r' D.48 retains the same entire old gentle pair through the full integral '
                      r'affine return tower. The actual kernel is $\mathcal O^{6\ell}$, '
                      r'the normalized inverse-limit fibre is an $\mathcal O^\ell$ torsor, '
                      r'and every finite parameter lifts compatibly.')
        else:
            state += (r' E.53 determines the exact uniform common source '
                      r'$G_L\times_{\mathcal J_5}G_R$, including the central sign and abelian kernel. '
                      r'Its full residual correction retains the old small-prime and level-five/seven values '
                      r'through the specified congruence subgroups. The resulting uniform fibre theorem is being completed.')
        lines[i] = ' ' + repr((row[0], row[1] + '; ' + '; '.join(additions[row[0]]), row[2], state)) + ','

    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    for anchor, ids in (
        (r'\InputIfFileExists{sections/D_return_prime_agent.tex}{}{}', ['D.47', 'D.48']),
        (r'\InputIfFileExists{sections/E_symplectic_integral_root.tex}{}{}', ['E.53'])):
        addition = '\n'.join(r'\InputIfFileExists{' + proofs[k] + r'}{}{}' for k in ids)
        assert maintext.count(anchor) == 1 and addition not in maintext
        maintext = maintext.replace(anchor, anchor + '\n' + addition)

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor) == 1
    paragraph = r'''
D.47 removes the split and prime-order restrictions from the cyclic outer chief theorem. The actual lift of an outer generator and all its kernel carries are retained. Exact boundary pushes and twists realize every effective phase, with prime-primary CRT exponents supplying each component while preserving the full character. The intermediate-cover Shapiro maps, powered-root sets, same-map subtraction and normalizer inversion therefore preserve the entire generating fibre for every finite cyclic outer group. The certificate checks all359268 onto genus-one characters for the twelve stated moduli and40 literal word maps with inverses. Its nonsplit Q16 times C3 model checks the complete carries and transport equations. Root's isolated replay takes1.615s, with both JSON outputs byte-identical and every saved array literal; an independent reader checked the whole proof.

D.48 lifts the affine return construction through the actual unramified coefficient ring. The complete kernel is the free lattice $\mathcal O^{6\ell}$, the whole peripheral fibre is its free orbit, and the normalized fibre is the compatible $\mathcal O^\ell$ torsor. All three centralizer projections remain onto, all maps generate, and pure rigidity preserves the actual six-coset source core. The entire old infinite gentle pair, its literal conjugator and its original maximal pro-ell action remain fixed. Every finite parameter lifts to the full tower. Root replayed all four precisions, modulo25,125,49,343, in47.429s; every mathematical JSON field, every NPZ array and every own-location input hash agrees. Both complete proof readings pass. The four normalized counts are5^60,5^90,7^56,7^84. This is the complete specified affine return tower; the arbitrary finite source comparison remains active.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    anchor = '\n## Geometric and germ results\n'
    assert body.count(anchor) == 1
    paragraph = r'''
E.53 determines the exact common quotient of the full signed double-cover source and every integral symplectic level. The canonical pure modular matrix has diagonal entries1 modulo4; it is conjugate by the displayed swap matrix to the actual rank-two symplectic component. This proves the signed quotient $G_m/Q_m=A_{2m}\times_{A_2}Q_{4m}$ with its exact source maps. The uniform maximum common quotient with $G_L$ is precisely $\mathcal J_5$, and the residual kernel is the first five-adic congruence subgroup times all higher-prime SL2 factors and the full additive rank-three factor. Imposing the old D23 kernel leaves that image unchanged. Imposing the level-five and level-seven kernels gives the exact two congruence restrictions and corresponding additive multiples.

The proof includes the normal-subgroup and centre calculation for every SL2(Z_p), the actual x60 commutator giving a nonzero first five-adic layer, and the entire abelian kernel generated by the even exponent vectors(30,0),(0,30). The complete original signed source has x,y of exact order30. Root's first exact-order60 assertion failed; its script and traceback are preserved in code and in research/E53_initial_order_probe_failure.json. The corrected proof uses the verified power relation and the actual exact order. The successful root certificate takes3.779s. An independent complete proof read and isolated replay pass in4.551s, including all102 signed comparisons and a separately computed determinant3 for the three Lie vectors. The audit's first symbolic-expression comparison and its exact simplification are also preserved. The uniform retained-fibre theorem is the next step.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    for prefix in ('1. **D.1--D.2:**', '2. **E.2--E.3:**'):
        begin = body.index(prefix)
        end = body.index('\n', begin)
        old[prefix + '_remaining'] = body[begin:end]
        current = body[begin:end]
        if prefix.startswith('1.'):
            current = current.replace(
                'The next extensions are the complete cyclic nonsplit chief theorem, the integral affine return tower, and the full noncyclic outer union.',
                'D.47 now proves the complete cyclic nonsplit chief theorem, and D.48 proves the full integral affine return tower with compatible fibres. The full noncyclic outer union and general repeated-prime source refinements remain active.')
        else:
            current = current.replace(
                'The uniform simultaneous fibre comparison and the joint A6/$G_L$ comparison are active extensions.',
                'E.53 now determines the uniform signed common quotient and exact residual correction through all congruence levels. The uniform retained-fibre theorem and the full joint A6/$G_L$ comparison are active extensions.')
        body = body[:begin] + current + body[end:]
    body += ('\n\nCheckpoint08 third compilation completed390 pages with two remaining\n'
             'overfull boxes,13.74924pt and10.26797pt, both in certificate-filename\n'
             'paragraphs. The complete attempt is preserved. The two paragraphs\n'
             'are rewritten with explicit sentence boundaries; the next build\n'
             'will verify those changes together with D.47, D.48 and E.53.\n')

    saved.write_text(json.dumps(old, indent=2) + '\n')
    (ROOT / proofs['D.48']).write_text(d48)
    (ROOT / proofs['E.53']).write_text(e53)
    (ROOT / 'sections/D_return_prime_agent.tex').write_text(d46)
    (ROOT / 'sections/E_a6_full_agent.tex').write_text(e48)
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(body)
    acceptance = {'accepted_statements': proofs,
                  'proof_sha256': {k: digest(ROOT / v) for k, v in proofs.items()},
                  'root_complete_proof_read': list(proofs),
                  'independent_complete_proof_read': list(proofs),
                  'root_D48_replay_seconds': 47.429,
                  'preserved_passages': str(saved.relative_to(ROOT)),
                  'remaining_global_tasks': ['D.1', 'D.2', 'E.2', 'E.3']}
    (ROOT / 'research/checkpoint08_cyclic_tower_common_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

120. D47 complete root proof and literal isolated replay PASS; a second
     reader checks every composite phase, nonsplit carry and full fibre.
     D48 complete root proof/code read and all four precision replays PASS
     in47.429s. A second independent proof reader checks every integral
     centralizer, source-core, generation and inverse-limit comparison.

121. E53 exact uniform common-source proof and isolated independent replay
     PASS. The centre/normal-subgroup proof, signed canonical comparison,
     first-layer determinant3 and full abelian kernel are checked. The
     closed full-mod-p case is made explicit. The rejected exact-order60
     probe and the audit's unsimplified symbolic comparison are preserved.
     D47,D48,E53 are integrated with unchanged open task statuses.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
