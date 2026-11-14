#!/usr/bin/env python3
"""Integrate four completed proof/certificate packages, preserving prior passages."""
from hashlib import sha256
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    for name in ('audit_cyclic_outer_root','audit_return_prime_root',
                 'audit_a6_full_chains_root','audit_a6_full_quotients_root'):
        data = json.loads((ROOT/'code'/(name+'.json')).read_text())
        assert data['all_passed'] and data['original_artifacts_unchanged']
    proofs = {'D.45':'sections/D_cyclic_outer_agent.tex',
              'D.46':'sections/D_return_prime_agent.tex',
              'E.48':'sections/E_a6_full_agent.tex',
              'E.52':'sections/E_symplectic_integral_root.tex'}
    assert digest(ROOT/proofs['D.45']) == '5ddc6a60dc7aa6b689bf9e3207d7a28228cc8feb48ab86a2e773a168f308e887'
    assert digest(ROOT/proofs['E.48']) == 'ba5894a39eaafa5727b7fbc83cf9d4ef9225d60d717ce98c09317ad2569a3583'
    d46audit = json.loads((ROOT/'code/audit_return_prime_root.json').read_text())
    assert digest(ROOT/proofs['D.46']) == d46audit['proof_sha256']
    for name in ('bc_symplectic_integral_audit','bc_symplectic_integral_residual_audit',
                 'bc_symplectic_integral_source_comparison'):
        data = json.loads((ROOT/'code'/(name+'.json')).read_text())
        assert str(data['status']).startswith('PASS'),name

    saved = ROOT/'research/checkpoint08_cyclic_return_a6_integral_prior_passages.json'
    assert not saved.exists()
    old = {}
    e52 = ROOT/proofs['E.52']
    old['E52_before_final_audit_text'] = e52.read_text()
    text = e52.read_text().replace(
        'the first three are independent, their indicated',
        'the first three are independent, their indicated')
    text = text.replace(
        'The first three are independent, their indicated\nthree-column minor has determinant $-1/3$, and',
        'The first three are independent, their minor in columns\n$0,2,3$ (numbered from zero) has determinant $-1/3$, and')
    anchor = 'maps and the radical products.\n'
    assert text.count(anchor)==1
    text = text.replace(anchor,anchor+
        'The second independent audit replays the complete residual\n'
        'certificate and checks all five $K_2$ Schreier generators\n'
        'under each of $s,r,x,y$, retaining the row-action convention.\n'
        'A further literal comparison reconstructs the induced $s,r$\n'
        'permutations at five and seven: all 29952 and 115200\n'
        'entries, respectively, agree with the frozen uncompressed\n'
        'sources. The coset sections agree, so the intervening\n'
        'conjugating gauge is the identity.\n')

    program = ROOT/'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i,line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("('"):
            continue
        row = ast.literal_eval(stripped.rstrip(','))
        additions = {'D.1':['D.45'],'D.2':['D.46'],
                     'E.2':['E.48','E.52'],'E.3':['E.48','E.52']}
        if row[0] not in additions:
            continue
        old[row[0]] = row
        assert not any(value in row[1].split('; ') for value in additions[row[0]])
        state = row[3]
        if row[0]=='D.1':
            state += (r' D.45 retains the full prescribed peripheral fibre across every actual '
                      r'$\mathrm{PSL}_2(32)$ chief extension over an arbitrary finite base, '
                      r'with the split cyclic-prime outer theorem and the exact old $P_n$ action.')
        elif row[0]=='D.2':
            state += (r' D.46 adds a strict return-prime quotient over that entire old source: '
                      r'its exact joint source is $\Gamma\times_D E$, every peripheral map generates '
                      r'and descends to an automorphism, and the full normalized fibre has '
                      r'$\ell^{\ell\operatorname{ord}_p(\ell)}$ elements.')
        else:
            state += (r' E.48 now retains all864 old points through the full $A_6$ Ferrari source, '
                      r'including its complete ternary and binary solvable layers, exact positive '
                      r'Kummer label, all centralizer choices and actual joint-source generation. '
                      r'E.52 identifies the full integral symplectic source at every modulus prime to6 '
                      r'and its common inverse-limit lower-central residual; its simultaneous '
                      r'peripheral comparison with the remaining sources is the next step.')
        lines[i] = ' '+repr((row[0],row[1]+'; '+'; '.join(additions[row[0]]),row[2],state))+','
    assert all(key in old for key in ('D.1','D.2','E.2','E.3'))

    mainpath = ROOT/'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    for anchor, addition in (
        (r'\InputIfFileExists{sections/D_modular_coprime_agent.tex}{}{}',
         '\n'.join(r'\InputIfFileExists{'+proofs[k]+r'}{}{}' for k in ('D.45','D.46'))),
        (r'\InputIfFileExists{sections/E_integral_class_three_agent.tex}{}{}',
         r'\InputIfFileExists{sections/E_a6_full_agent.tex}{}{}'),
        (r'\InputIfFileExists{sections/E_symplectic_five_p7_agent.tex}{}{}',
         r'\InputIfFileExists{sections/E_symplectic_integral_root.tex}{}{}')):
        assert maintext.count(anchor)==1 and addition not in maintext
        maintext = maintext.replace(anchor,anchor+'\n'+addition)

    report = ROOT/'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor)==1
    paragraph = r'''
D.45 proves the full multiplier-one chief lift for a nonabelian simple group whose actual automorphism extension is split with prime cyclic outer group. The positive boundary pushes and Hurwitz squares have literal inverse source words; they remove every independent effective field phase while preserving the prescribed surface character and surjectivity. The signed Shapiro formula, all intermediate embeddings, all powered-root intersections, the subtraction of the very same maps factoring through the finite base, and subgroup-poset inversion give the exact number of generating maps for every prescribed base conjugator. No restriction is imposed on the finite base. The concrete group is $\mathrm{PSL}_2(32)$; its simplicity and its full $S\rtimes C_5$ automorphism group are proved through the actual projective action. White's author manuscript, Section3 before Lemma3.1 and Lemma3.2, was opened and the precise field automorphism checked. Root's isolated replay of both programs takes8.075s; both JSON files are byte-identical and every saved array agrees. Root and an independent reader checked the complete proof. The preceding uint8 packing failure and its exact correction remain preserved.

D.46 proves a strict first return-prime lift while retaining the complete old infinite gentle pair. For distinct $\ell,p\ge5$, its six-coset affine kernel has dimension $6\ell a$, $a=\operatorname{ord}_p(\ell)$, and is a simple nontrivial module. The complete ordinary conjugator union has $\ell^{6\ell a}$ maps, all generating, in one free kernel orbit; the exact normalized fibre has $\ell^{\ell a}$ maps. The three full centralizer projections are proved onto. A separate pure-source rigidity argument proves preservation of the actual induced kernel, so every counted source map is a genuine automorphism of the same finite quotient. The old relative kernel maps onto the entire new module, proving the actual common source $\Gamma\times_D E$ and retaining the literal old conjugator and maximal pro-$\ell$ quotient. Both prime-pair cases, $(5,7)$ and $(7,5)$, pass root's four-program isolated replay in26.956s; every mathematical JSON record, every saved array and every own-location input hash agrees. A second complete proof reading checks the centralizer union, source-core preservation and joint fibre. This establishes the displayed return quotient and does not assert cofinality of the whole return completion.
'''
    body = body.replace(anchor,'\n'+paragraph.strip()+'\n'+anchor)
    anchor = '\nE.49 gives the complete five-strand symplectic test at three.'
    assert body.count(anchor)==1
    paragraph = r'''
E.48 now completes the full inner/free $A_6$ Ferrari source. Its actual source order is $2^{218}3^{84}5^{62}7^6 11^3 13^2$. The full derived comparison gives ordinary abelian exponent120, then a nine-dimensional ternary layer and a six-dimensional binary layer above a perfect normal subgroup; the maximum solvable quotient has order108839116800. Every one of the864 old points survives. Per old point, the complete solvable fibre has18 norm solutions and exactly16 generating solutions. All powered-root, ordinary centralizer, generation and source-word choices are retained. Its remaining quotient coordinate equals the positive $\kappa_2$ coordinate of the same actual Galois word; the complete24 labels and all fibre directions are checked literally. The actual image of the correcting subgroup $\gamma_5N$ is the whole required $N'$ image, so the correction retains the full $D_{23}$ value. Both the exact joint source and the four-strand target $T_{23}\times_{C_2}T_6$ are generated after correction.

Root's full $A_6$ audit compiles and replays all eleven complete stabilizer chains in680.367s, with all strong-word and Schreier relations checked. Its further22 quotient, module and Python fibre programs pass in870.501s, including the entire binary module, all 6668 old-kernel relations, complete source fibres, correction words and Kummer labels. The authoritative267-file package remains unchanged. A second reader checked the entire proof. The new simultaneous $G_L/A_6$ comparison is a separate calculation: E.48 does not use the equality of a scalar Kummer label as a substitute for that joint map.
'''
    body = body.replace(anchor,'\n'+paragraph.strip()+'\n'+anchor)
    anchor = '\n## Geometric and germ results\n'
    assert body.count(anchor)==1
    paragraph = r'''
E.52 proves a single integral description of the eight-pair symplectic source through every modulus $m>1$ prime to6 and the full product $R=\prod_{p\ge5}\mathbf Z_p$. All4656 N matrices have an explicit common $\mathrm{SL}_2$ component and a five-dimensional additive component over $\mathbf Z[1/6]$. The five K2 Schreier words have the same decomposition. A basis minor $2^{13}3^2$ and the exact Smith lattice prove generation at every prime power. Two literal sign characters detect the whole quotient $A_2$ at every modulus. Four actual conjugates of $[x,y]$ give the complete three-dimensional additive derived image; the conjugation differences have Smith invariants1,1,4, proving stability under every lower-central step. The exact source order is $24m^5|\mathrm{SL}_2(\mathbf Z/m)|$, its pure abelianization is $(\mathbf Z/2m)^2$ with the ordinary exponent coordinates, and its quotient by the derived image is the actual $A_{2m}$.

The compactness argument uses the closed fibres of the displayed source maps simultaneously in the lower-central index and the congruence modulus. It proves $\rho_R(R_{\rm nil})=\mathrm{SL}_2(R)\times R^3$, with every individual word fibre retained as an exact kernel coset. The integral probe and residual programs run in4.643s and11.403s; independent audits reconstruct the matrices, replay the entire residual certificate, check all20 conjugates of the K2 basis, and verify every lattice and action convention. An additional exact comparison reconstructs both full induced source permutations at five and seven: all29952 and115200 entries agree, with identity gauge between the same coset sections. Root and a second reader checked the whole integral closure proof. The uniform common-source and simultaneous peripheral-fibre comparison is the next step; E.52 does not register that pending comparison as proved.
'''
    body = body.replace(anchor,'\n'+paragraph.strip()+'\n'+anchor)
    begin = body.index('1. **D.1--D.2:**')
    end = body.index('\n2. **E.2--E.3:**',begin)
    old['remaining_D_paragraph'] = body[begin:end]
    current = body[begin:end].replace(
        'The active extensions concern primes dividing the current base order and nonabelian chief factors with nontrivial odd outer action.',
        r'D.45 now supplies the full split cyclic-prime outer chief theorem, including $\mathrm{PSL}_2(32)$ over arbitrary finite bases. D.46 proves the full finite affine return fibre above the entire old coprime lift, with the exact common source and every old normalized conjugator retained. The next extensions are the complete cyclic nonsplit chief theorem, the integral affine return tower, and the full noncyclic outer union.')
    body = body[:begin]+current+body[end:]
    begin = body.index('2. **E.2--E.3:**')
    end = body.index('\n',begin)
    old['remaining_E_paragraph'] = body[begin:end]
    current = body[begin:end]
    current = current.replace('All24 fibres remain nonempty through E.47.','All24 fibres remain nonempty through the accepted refinements E.47--E.51.')
    current = current.replace(
        'The full inner/free A6 source has additional three-primary layers in its successive derived quotients; their actions and exact comparison with all old parameters remain active work.',
        'E.48 now resolves the complete ternary and binary layers of the full inner/free A6 source, retaining all864 old points with exact generation and correction preimages.')
    current = current.replace(
        'E.49 proves the full prime-three five-strand symplectic comparison; its prime-five source and common-quotient comparison are now active.',
        'E.49 proves the full prime-three five-strand symplectic comparison.')
    current = current.replace(
        'The full inner/free A6 source is undergoing root quotient-and-fibre replay; the uniform integral symplectic source and the joint A6/$G_L$ comparison are active extensions.',
        r'E.52 now proves the complete integral congruence source, its actual $A_{2m}$ quotient and its full inverse-limit lower-central residual. The uniform simultaneous fibre comparison and the joint A6/$G_L$ comparison are active extensions.')
    body = body[:begin]+current+body[end:]

    bib = ROOT/'LM7_PUSH_references.bib'
    bibtext = bib.read_text()
    assert 'ACyclicOuterWhite2011' not in bibtext
    bibtext += r'''

@misc{ACyclicOuterWhite2011,
  author = {White, Donald L.},
  title = {Character Degrees of Extensions of {PSL}$_2(q)$},
  year = {2011},
  howpublished = {Author manuscript, July 25, 2011},
  url = {https://www.math.kent.edu/~white/papers/autpsl2.pdf},
  note = {verified: author PDF opened; Section 3 before Lemma 3.1 and Lemma 3.2 identify the actual field automorphism and full automorphism group. D.45 gives the direct proof and maps for PSL2(32).}
}
'''
    replaymd = ROOT/'research/DE_a6_replay.md'
    old['DE_a6_replay_before_filename_correction'] = replaymd.read_text()
    replaytext = replaymd.read_text().replace(
        '`de_a6_a5_common_source_order.bin/.out`',
        '`de_a6_a5_common_source.bin` and `de_a6_a5_common_source_order.out`')
    assert replaytext != replaymd.read_text()

    saved.write_text(json.dumps(old,indent=2)+'\n')
    e52.write_text(text)
    program.write_text('\n'.join(lines)+'\n')
    mainpath.write_text(maintext)
    report.write_text(body)
    bib.write_text(bibtext)
    replaymd.write_text(replaytext)
    acceptance = {'accepted_statements':proofs,'proof_sha256':{k:digest(ROOT/v) for k,v in proofs.items()},
                  'root_complete_proof_read':list(proofs),'independent_complete_proof_read':list(proofs),
                  'primary_opened':'https://www.math.kent.edu/~white/papers/autpsl2.pdf, Section3 before Lemma3.1 and Lemma3.2',
                  'preserved_passages':str(saved.relative_to(ROOT)),
                  'remaining_global_tasks':['D.1','D.2','E.2','E.3']}
    (ROOT/'research/checkpoint08_cyclic_return_a6_integral_acceptance.json').write_text(json.dumps(acceptance,indent=2)+'\n')
    with (ROOT/'research/root_searches_02.md').open('a') as log:
        log.write('''

117. D45 is fully read by root; White's exact author PDF Section3 and
     Lemma3.2 are opened. Both isolated programs reproduce all JSON bytes
     and all arrays in8.075s. D46 is fully read and its two model/centralizer
     cases reproduce every mathematical output and literal array in26.956s.
     Both complete finite-base and return-source proofs also pass a second reader.

118. E48 root validation completes all11 full stabilizer chains in680.367s
     and all22 remaining quotient/module/fibre steps in870.501s. All267
     authoritative source artifacts remain unchanged. The complete proof
     and the exact common-source generation are accepted; a replay-guide
     filename typo is corrected with the original passage preserved.

119. E52 identifies the exact integral source at every modulus prime to6,
     including parity detection, SL2 times rank5 N image, rank3 F-derived
     image, the actual A_(2m) quotient and full lower-central inverse-limit
     residual. Independent audits reproduce the complete residual certificate,
     all20 K2 conjugation comparisons and both uncompressed p5/p7 source maps.
     The whole closure proof passes a second reader. The uniform simultaneous
     fibre/common-source comparison remains an active next step.
''')
    print(json.dumps(acceptance,indent=2))


if __name__ == '__main__':
    main()
