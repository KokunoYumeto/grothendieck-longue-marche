#!/usr/bin/env python3
"""Integrate D42 after three proof readings and the isolated exact replay."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent

def main():
    audit = json.loads((ROOT/'code/audit_coprime_even_root.json').read_text())
    assert audit['all_passed'] and audit['entire_JSON_byte_identical']
    assert audit['original_artifacts_unchanged']
    section = ROOT/'sections/D_even_base_agent.tex'
    assert sha256(section.read_bytes()).hexdigest() == '715596a4a61e3d0d66021eb99ac966d543dc041903c8855b02fb00fb1bf851c7'
    saved = ROOT/'research/checkpoint07_even_base_prior_passages.json'
    assert not saved.exists()
    old = {}
    program = ROOT/'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("('"):
            continue
        row = ast.literal_eval(stripped.rstrip(','))
        if row[0] == 'D.1':
            old['D.1'] = row
            assert 'D.42' not in row[1]
            previous = ('Over every odd finite base, all pairing-compatible multiplier-one abelian lifts '
                        'extend through the full relative pro-$p$ cover for every coprime prime. '
                        'Their complete literal fibres and all-source factorization are proved. '
                        'This retains all D.37 shadows for every $p\\ne5$; the further mixed-prime finite extensions remain to be covered.')
            replacement = (r'Over every finite base, all pairing-compatible multiplier-one abelian lifts extend through the full relative pro-$p$ cover for every coprime prime. '
                           r'The prescribed boundary maps give the exact primitive neck reduction of a closed free-action surface; its invariant integral Lagrangian proves the finite-field form comparison. '
                           r'The complete literal fibres and all-source factorization are retained. Every D.37 parameter lifts through each characteristic relative-two stage and then its full relative pro-$p$ cover for odd $p\ne5$, retaining the exact maximal pro-five quotient $P_n$. '
                           r'Kernels at primes dividing the base order and the remaining nonabelian chief steps still require their full-source comparison.')
            assert previous in row[3]
            state = row[3].replace(previous, replacement)
            lines[i] = ' '+repr((row[0], row[1]+'; D.42', row[2], state))+','
    assert 'D.1' in old
    mainpath = ROOT/'LM7_PUSH_paper.tex'
    text = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/D_relative_prop_agent.tex}{}{}'
    assert text.count(anchor) == 1
    assert 'sections/D_even_base_agent.tex' not in text
    text = text.replace(anchor, anchor+'\n'+r'\InputIfFileExists{sections/D_even_base_agent.tex}{}{}')
    report = ROOT/'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor) == 1
    paragraph = r'''
D.42 proves the multiplier-one coprime relative-cover theorem over every finite base, including even-order bases. The prescribed boundary maps identify each actual circle by $[d,t]\mapsto[\alpha(d)h_i,t]$. Gluing the original cover to the oppositely oriented twisted cover gives a closed surface with a free deck action. Its primitive neck lattice has the exact equivariant reduction $I^\perp/I=C\oplus-C^\alpha$. Barge--Marché's Theorem 1, reopened in the primary author PDF, gives a primitive invariant integral Lagrangian. Its reduction and the explicit semisimple multiplicity-form cancellation give the required finite-field isometry; averaging and integral corrections then recover every precision. All D.41 source and literal-fibre maps transfer with the stated coprimality hypothesis. The resulting characteristic two-then-$p$ family retains every D.37 parameter and the exact maximal pro-five quotient $P_n$. Three independent proof readings passed, including the primary theorem and every gluing, lattice, and cancellation comparison. The isolated Q8 certificate replay passes in 0.368 seconds, byte-identically: at primes three and five the actual module has two distinct form orbits, and all eight prescribed boundary maps lift through $3^6$ or $5^6$ with five nonzero corrections each. The computation checks those covers; the general theorem follows from the proved comparison maps.
'''
    body = body.replace(anchor, '\n'+paragraph.strip()+'\n'+anchor)
    begin = body.index('1. **D.1--D.2:**')
    end = body.index('\n2. **E.2--E.3:**', begin)
    old['remaining_D_paragraph'] = body[begin:end]
    body = body[:end] + (' D.42 now proves the same multiplier-one full relative pro-$p$ lift over arbitrary finite bases with coprime order, through the actual matched-boundary double. Its characteristic two-then-$p$ application retains the specified $P_n$ shadow. The active extensions concern compatibility through infinite coprime bases, primes dividing the current base order, and nonabelian chief factors with nontrivial odd outer action.') + body[end:]
    bib = ROOT/'LM7_PUSH_references.bib'
    refs = bib.read_text()
    assert 'ABargeMarche2024' not in refs
    refs += r'''

@article{ABargeMarche2024,
 author={Barge, Jean and March{\'e}, Julien},
 title={The intersection form on the homology of a surface acted on by a finite group},
 journal={Mathematische Annalen}, volume={389}, year={2024}, pages={1255--1266},
 doi={10.1007/s00208-023-02688-6},
 url={https://webusers.imj-prg.fr/~julien.marche/papiers/Symplectic_Chevalley_Weil.pdf},
 note={verified: opened the ten-page primary author version, Theorem 1 on p.1, which explicitly states the primitive invariant integral Lagrangian. The published preview has rational Theorem 1 and its integral formulation in Remark 1; publication metadata are printed there. The free action and the exact integral reduction required here are proved in D.42. The DOI resolver was unavailable.}
}
'''
    saved.write_text(json.dumps(old, indent=2)+'\n')
    program.write_text('\n'.join(lines)+'\n')
    mainpath.write_text(text)
    report.write_text(body)
    bib.write_text(refs)
    with (ROOT/'research/root_searches_02.md').open('a') as log:
        log.write('''

103. D42 passes three complete independent proof readings. Root reopened
     Barge--Marché's primary author PDF (turn471view0): Theorem1 gives
     the integral primitive invariant Lagrangian on p1. The proof checks
     the actual alpha-twisted free-action double, the Mayer--Vietoris neck
     lattice including its integral index, its orthogonal quotient, and
     finite-field Witt cancellation on identical semisimple modules.
     Root's isolated Q8 replay is byte-identical in0.368s, with all eight
     boundary maps through729 and15625 and original inputs unchanged.
     D42 is integrated. The exact characteristic two-then-p quotient
     maps retain P_n; compatibility as the intermediate stage varies
     is the next explicit comparison under investigation.

104. The first checkpoint07 build, incorporating D40 andD41, completes
     with zero overfull boxes and no undefined citations or references.
     Its exact inputs and logs are preserved in checkpoint07_first_complete.
     D42 and the current E50 continuation postdate that preserved build.
     E50's four source certificates independently replay in dependency
     order with all mathematical JSON records and NPZ arrays identical.
     The replay verifies every declared input hash against its own files.
     The initial replay-driver input discovery failed before any certificate
     executed because it treated an overlong text literal as a filename.
     The failed driver/output remain preserved; the correction accepts
     only explicit bounded filename literals. The target replay is ongoing.
''')
    print(json.dumps({'integrated':['D.42'],
                      'preserved_passages':str(saved.relative_to(ROOT)),
                      'new_verified_reference':'ABargeMarche2024',
                      'unresolved_tasks':['D.1','D.2','E.2','E.3']},indent=2))

if __name__ == '__main__':
    main()
