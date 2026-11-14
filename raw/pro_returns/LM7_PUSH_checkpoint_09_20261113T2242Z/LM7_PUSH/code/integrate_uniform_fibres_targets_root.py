#!/usr/bin/env python3
"""Integrate the completely audited E55 and E56, preserving prior passages."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    proofs = {
        'E.55': 'sections/E_symplectic_integral_fibres_root.tex',
        'E.56': 'sections/E_symplectic_integral_targets_agent.tex',
    }
    expected = {
        'E.55': 'c3ec7c81b43f89d79e02b7f45537b431272050eb14ac5b81dcd3ab40410af907',
        'E.56': '08d8419c27ea7eaacbe33f8f0eb3ca6ed9eb04462fe28bbd2f7160699e026e3e',
    }
    for ident, path in proofs.items():
        assert digest(ROOT / path) == expected[ident], ident
    replay = json.loads((ROOT / 'code/audit_integral_targets_root.json').read_text())
    assert replay['all_passed'] and replay['all_mathematical_JSON_equal']
    assert replay['original_artifacts_unchanged']
    assert replay['proof_sha256'] == expected['E.56']
    audit = (ROOT / 'research/BC_integral_fibres_audit.md').read_text()
    assert '**PASS**' in audit and expected['E.55'] in audit

    saved = ROOT / 'research/checkpoint08_uniform_fibres_targets_prior_passages.json'
    assert not saved.exists()
    old = {ident + '_audited_source': (ROOT / path).read_text()
           for ident, path in proofs.items()}

    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] not in ('E.2', 'E.3'):
            continue
        old[row[0] + '_coverage'] = row
        assert 'E.55' not in row[1].split('; ')
        state = row[3].replace(
            'The resulting uniform fibre theorem is being completed.',
            'E.55 now retains the complete 432-point multiplier-one family and every '
            'prescribed full boundary fibre through all these congruence levels with '
            'one profinite word and the same actual Galois value. Its maximum common '
            'source quotients and both full word fibres are explicit. E.56 proves '
            'the exact integral four- and five-strand targets and their entire '
            'products with the preceding targets, including every congruence kernel. '
            'The full A6 comparison is under independent replay; compatibility at '
            'an arbitrary finite source remains unresolved.')
        assert state != row[3]
        lines[i] = ' ' + repr((row[0], row[1] + '; E.55; E.56', row[2], state)) + ','

    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/E_symplectic_integral_common_root.tex}{}{}'
    addition = '\n'.join(r'\InputIfFileExists{' + path + r'}{}{}'
                         for path in proofs.values())
    assert maintext.count(anchor) == 1 and addition not in maintext
    maintext = maintext.replace(anchor, anchor + '\n' + addition)

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\n## Geometric and germ results\n'
    assert body.count(anchor) == 1
    paragraph = r'''
E.55 retains the full 432-point multiplier-one family, every prescribed complete two-adic class-two and three-adic class-three boundary correction, and every full relative pro-p boundary identity through the entire symplectic congruence system prime to six. One actual profinite commutator word has the same signed and uniform symplectic values as the same Galois word, whose cyclotomic character equals one globally. The exact common quotient at m is $A_{2m}\times_{A_{2g}}G_g$, with $g=\gcd(m,35)$; the full inverse-limit quotient and all correction and word fibres are given by their literal homomorphism kernels. The generation proof uses the same Galois precomposition, the exact residual kernel, and the retained finite-source quotient. Root and an independent reader checked the entire proof, including compactness and every source comparison; this deduction requires no new finite experiment.

E.56 proves the exact target groups over every Z/m prime to six and over the full product of the p-adic rings for p at least five. Three transvections generate the specified vector stabilizer, with its explicit Heisenberg kernel; the fourth generates Sp4. Literal elementary elimination proves these assertions over every local ring and CRT parameter words prove their full products. The transpose and braid-mirror maps identify the saved right action exactly. The proof of perfectness, the projective simplicity argument, and every solvable congruence kernel determine the complete joint target products with the old signed, small-prime and Hurwitz targets. Two independent full proof readings pass. Root's isolated replay takes 3.082 seconds and reproduces every mathematical JSON value, all 12,096 saved permutation entries, all 3,024 nonzero field vectors and 112 literal matrix factorizations over seven prime-power and mixed moduli. Every protected original remains unchanged.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    prefix = '2. **E.2--E.3:**'
    begin = body.index(prefix)
    end = body.index('\n', begin)
    old['E_remaining'] = body[begin:end]
    current = body[begin:end].replace(
        'The uniform retained-fibre theorem and the full joint A6/$G_L$ comparison are active extensions.',
        'E.55 proves the full uniform retained-fibre theorem, and E.56 proves every integral target and the full products with the preceding targets. The complete joint A6/$G_L$ certificates are replaying independently; the simultaneous A6 and uniform comparison and arbitrary finite sources remain active.')
    assert current != body[begin:end]
    body = body[:begin] + current + body[end:]
    body += ('\n\nCheckpoint 08 fourth compilation completes 405 pages with zero overfull boxes, '
             'no undefined references or citations, and verified active-source input hashes. '
             'Its exact build is preserved under build/checkpoint08_fourth_complete. '
             'The next build incorporates the newly accepted E.55 and E.56.\n')

    saved.write_text(json.dumps(old, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(body)
    acceptance = {
        'accepted_statements': proofs,
        'proof_sha256': expected,
        'complete_root_proof_reads': list(proofs),
        'complete_independent_proof_reads': list(proofs),
        'E56_isolated_replay_seconds': replay['seconds'],
        'E55_new_computation': 'Deduction from accepted E51-E53; no new experiment required.',
        'preserved_passages': str(saved.relative_to(ROOT)),
        'remaining_global_tasks': ['D.1', 'D.2', 'E.2', 'E.3'],
    }
    (ROOT / 'research/checkpoint08_uniform_fibres_targets_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

122. Root opened Steinberg's original Yale notes at the University of Utah,
     https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf.
     Section 7 Theorem 10 and Corollary 2(b), including the finite-field
     exceptions, prove the exact universal SL2(F5) to PSL2(F5) central cover
     used in E54. The F5 rank-one case satisfies every displayed restriction.
     The actual PSL2(F5) to A5 permutation identification is retained separately.
     PDF pages at indices84,88,89 were opened as screenshots after the text read.

123. Primary research for general outer-character detectors found Turaev's
     Sections of fiber bundles over surfaces, arXiv:0904.2692v1 (2009).
     Root opened its full PDF and read Theorems1.1,1.2 and Sections2.1--2.4.
     The relative statement assumes positive genus and a q-free boundary
     family; it does not supply the genus-zero chief step. The arXiv PDF
     open for0804.1489 failed with DisabledError. Publisher copies were
     located but not yet opened. The active proof route derives the exact
     all-genus finite group-algebra count and finite scalar covers directly,
     retaining proper subgroup images for an explicit Mobius inversion.
     No general chief theorem is registered from this active route yet.

124. E55 complete root and independent proof reads PASS. The exact CRT
     common source, inverse-limit residual correction, one actual Galois
     word, generation and both complete word fibres are all checked.
     E56 complete root and two independent proof reads PASS; root's isolated
     exact replay PASS in3.082s, with every mathematical JSON value equal
     and every original unchanged. E55 and E56 are integrated, retaining
     all four unresolved global task statuses.

125. The first E54 root chain driver stopped before running a saved chain:
     it chose a preparation log instead of the complete _order.out record.
     The exact driver, traceback and isolated directory are preserved in
     E54_root_chain_initial_log_failure.json. The corrected driver accepts
     only a final PASS record with every exact chain field and checks all
     available complete records for equality. Its new full replay is active.
     The separate E54 quotient replay proceeds independently and protects
     all417 frozen source artifacts.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
