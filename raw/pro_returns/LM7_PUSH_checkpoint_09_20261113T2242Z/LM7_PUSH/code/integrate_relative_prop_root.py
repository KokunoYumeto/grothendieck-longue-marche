#!/usr/bin/env python3
"""Integrate the audited D40 and D41 proofs, preserving the previous scope text."""
from pathlib import Path
import ast
import json

ROOT=Path(__file__).resolve().parent.parent

def main():
    for name in ('audit_coprime_intersection_root','audit_relative_prop_root'):
        d=json.loads((ROOT/'code'/f'{name}.json').read_text())
        assert d['all_passed'] and d['entire_JSON_byte_identical']
        assert d['original_artifacts_unchanged']
    saved=ROOT/'research/checkpoint07_relative_prop_prior_passages.json'
    assert not saved.exists()
    old={}
    program=ROOT/'code/assemble_register.py'
    lines=program.read_text().splitlines()
    for i,line in enumerate(lines):
        stripped=line.strip()
        if not stripped.startswith("('"):
            continue
        row=ast.literal_eval(stripped.rstrip(','))
        if row[0]=='D.1':
            old['D.1']=row
            assert 'D.40' not in row[1]
            state=(row[3]+r' Over every odd finite base, all pairing-compatible multiplier-one abelian lifts extend through the full relative pro-$p$ cover for every coprime prime. Their complete literal fibres and all-source factorization are proved. This retains all D.37 shadows for every $p\ne5$; the further mixed-prime finite extensions remain to be covered.')
            lines[i]=' '+repr((row[0],row[1]+'; D.40; D.41',row[2],state))+','
    assert 'D.1' in old
    mainpath=ROOT/'LM7_PUSH_paper.tex';text=mainpath.read_text()
    anchor=r'\InputIfFileExists{sections/D_frattini_agent.tex}{}{}'
    assert text.count(anchor)==1
    text=text.replace(anchor,anchor+'\n'+
        r'\InputIfFileExists{sections/D_intersection_agent.tex}{}{}'+'\n'+
        r'\InputIfFileExists{sections/D_relative_prop_agent.tex}{}{}')
    report=ROOT/'research/report_body.md';body=report.read_text()
    anchor='\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor)==1
    paragraphs=r'''
D.40 constructs pairing-compatible automorphisms through every universal abelian coprime cover of an odd finite base. The actual compact cover homology has zero deck invariants. Broto--Møller--Oliver Lemma A.1(b), checked in the primary author PDF, supplies the finite-field equivariant isometry, including characteristic two. The explicit averaged Hensel correction uses no division by two and gives the integral similitude. It retains the entire group-ring intersection pairing, every intermediate-cover transfer and restriction, and the unique invariant quadratic refinement modulo two. Four actual covers and sixteen similitudes through moduli 64 and 729 passed isolated root replay in 0.643 seconds, with byte-identical JSON and unchanged inputs.

D.41 determines the exact homology image and the full literal fibre of the relative pro-$p$ peripheral automorphisms above an odd finite base. The image consists precisely of the prescribed boundary permutations, all compact-to-boundary homomorphisms, and compact symplectic maps. Actual Hurwitz, handle and bounding-pair maps supply these blocks. Compactness and the pro-$p$ kernel then give a complement conjugator that retains the entire prescribed integral homology map. The primitive-boundary Magnus centralizer recovers each peripheral generator from its power, with its base conjugator unchanged. Every generating source map factors through an automorphism of the same relative cover. The complete fibre is the displayed quotient of $R\times\mathcal Y_{\alpha,h}$ by $R^D$, with its full ordinary centralizer union. Root and geometry independently checked the entire proof. The corrected finite certificate uses exactly eight elementary transvections for $\mathrm{Sp}_4(\mathbf F_2)$ and two for $\mathrm{Sp}_2(\mathbf F_3)$, and verifies the literal free-word maps and inverses. Root replay passes in 0.279 seconds with byte-identical JSON. The earlier all-vector certificate remains preserved under its explicit superseded names.
'''
    body=body.replace(anchor,'\n'+paragraphs.strip()+'\n'+anchor)
    marker='1. **D.1--D.2:**'
    start=body.index(marker);end=body.index('\n2. **E.2--E.3:**',start)
    old['remaining_D_paragraph']=body[start:end]
    body=body[:start]+body[start:end]+(
        ' D.40 and D.41 now control the full relative pro-$p$ cover over every odd finite base, including all pairing-compatible integral homology maps and every generating source lift. For D.37 this gives every coprime-prime relative cover with the same characteristic five-group quotient. The next comparison concerns actual even bases and successive extensions with kernels involving more than one prime; the extra symmetry equations for D.2 also remain to be imposed on these fibres.')+body[end:]
    body+='\n\nCheckpoint 06 has been saved and is retained unchanged under `history/LM7_PUSH_checkpoint_06.zip`. Its archive contains 3987 files (409074505 bytes), all CRC checked, with SHA-256 `6ea5d7a87a572b9eeabc7b7aabf2d374e3173f6163173619bcb1384dd5996ce5`. The active investigation continues beyond its verified 331-page snapshot.\n'
    bib=ROOT/'LM7_PUSH_references.bib';refs=bib.read_text()
    assert 'ACoprimeBMO2012' not in refs
    refs+=r'''

@article{ACoprimeBMO2012,
 author={Broto, Carles and M{\o}ller, Jesper M. and Oliver, Bob},
 title={Equivalences between fusion systems of finite groups of Lie type},
 journal={Journal of the American Mathematical Society},
 volume={25}, number={1}, year={2012}, pages={1--20},
 doi={10.1090/S0894-0347-2011-00713-3},
 url={https://www.math.univ-paris13.fr/~bobol/bmo1-jams.pdf},
 note={verified: opened the primary author PDF, Lemma A.1(b) and its complete proof on printed pp.15--17, including the characteristic-two argument. Publisher issue metadata confirms the journal, volume, pages and DOI. The exact zero-invariant and coprimality hypotheses are checked in D.40.}
}
'''
    saved.write_text(json.dumps(old,indent=2)+'\n')
    program.write_text('\n'.join(lines)+'\n');mainpath.write_text(text)
    report.write_text(body);bib.write_text(refs)
    with (ROOT/'research/root_searches_02.md').open('a') as out:
        out.write('''

100. D40 and D41 pass root full-proof review and isolated program replay.
     D40 reproduces its entire JSON byte for byte in 0.643s over the four
     actual covers, with all sixteen finite-field and integral corrections.
     D41's initial finite gate used all vector transvections; root required
     the exact elementary list in the proof. The original artifacts are
     preserved as a_relative_prop_all_vectors_superseded.*, and the new
     eight-generator/two-generator runs give orders 720 and 24. The root
     isolated replay is byte-identical in 0.279s. The proof also retains the
     explicit four-factor diagonal SL2 identity. Both statements are now
     integrated; all four full-source tasks remain unresolved.

101. Checkpoint06 is frozen, CRC-verified and saved under a new identity.
     It contains 3987 files and 409074505 bytes; SHA256 is
     6ea5d7a87a572b9eeabc7b7aabf2d374e3173f6163173619bcb1384dd5996ce5.
     The five earlier archives are unchanged. The local transfer helper
     failed before a service write because its Codex auth file was absent;
     the runtime-authenticated prepared upload then transferred the exact
     workspace bytes and finalized its returned opaque session. The
     preserved metadata and history copy identify the same saved archive.

102. For the even-base intersection problem, root searched Barge--Marche
     and opened the primary author PDF at
     https://webusers.imj-prg.fr/~julien.marche/papiers/Symplectic_Chevalley_Weil.pdf
     (turn459view0, ten pages). Its Theorem1 directly gives a primitive
     integral invariant Lagrangian for a free finite-group surface action.
     The manuscript's rational Witt comparison and the field hypothesis
     in Section2 were also read. The publisher URL failed. D42 is reserved
     for the ongoing actual boundary-gluing and finite-field cancellation
     argument; no even-base extension has yet been registered as proved.
''')
    print(json.dumps({'integrated':['D.40','D.41'],
        'preserved_passages':str(saved.relative_to(ROOT)),
        'new_verified_reference':'ACoprimeBMO2012',
        'unresolved_tasks':['D.1','D.2','E.2','E.3']},indent=2))

if __name__=='__main__':
    main()
