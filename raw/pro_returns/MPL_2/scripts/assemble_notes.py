#!/usr/bin/env python3
"""Assemble research-only deliverable. Never reads images or changes any TEX file."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent.parent
REC=ROOT/'records'

def items(name, pattern):
    text=(REC/name).read_text()
    matches=list(re.finditer(pattern,text,re.M))
    out={}
    for k,m in enumerate(matches):
        end=matches[k+1].start() if k+1<len(matches) else len(text)
        piece=text[m.start():end]
        # Research appendices and bibliographies remain in evidence files, not in a note.
        piece=re.split(r'^## (?:Calculation|Primary references|Primary-source references|Primary literature|References used|Evidence|Bibliography|Sources|Verification|Supplement|Context search|Appendix|Standing questions)',piece,flags=re.M)[0]
        piece=re.sub(r'^#{2,4} ', '### ', piece, count=1)
        out[m.group(1)]=piece.strip()
    return out

A=items('research_primary.md',r'^## (A\d\d)\b')
CC=items('research_chern_curves.md',r'^### (CC\d\d)\b')
L=items('research_lambda.md',r'^### (L\d\d)\b')
S=items('research_supports.md',r'^### (S\d\d)\b')
R=items('research_bridge.md',r'^### (R\d\d)\b')

support_kinds={
    'S01':'reading question / own idea',
    'S02':'unproved claim / own idea',
    'S03':'own idea — conditional proof',
    'S04':'unproved claim — construction condition',
    'S05':'reading question / own idea',
    'S06':'reading question',
    'S07':'unpursued implication',
    'S08':'own idea',
    'S09':'self-flagged',
    'S10':'self-flagged / reading question',
    'S11':'self-flagged / own idea',
    'S12':'unpursued implication',
    'S13':'own idea',
    'S14':'unproved claim',
    'S15':'own idea — conditional strengthening',
    'S16':'withdrawn in the same text / own idea',
    'S17':'unpursued implication',
    'S18':'unproved claim on a cancelled reused sheet',
    'S19':'reading question',
    'S20':'unpursued implication / own idea',
    'S21':'reading question — title',
}
for key,piece in S.items():
    heading,body=piece.split('\n',1)
    heading=heading.replace(' — ', ' — Cote 2, scans ',1)
    body=re.sub(r'\bAppendix ([A-C])',r'Appendix \1 of `records/research_supports.md`',body)
    S[key]=heading+'\n\n**Kind:** '+support_kinds[key]+'.\n'+body
for key,piece in L.items():
    piece=piece.replace("Appendix B's $n=3$ example", "The $n=3$ example in appendix B of `records/research_lambda.md`")
    piece=re.sub(r'\bAppendix ([A-F])',r'Appendix \1 of `records/research_lambda.md`',piece)
    piece=piece.replace('**Kind:** own verification','**Kind:** own idea — verification')
    L[key]=piece

intro=r'''# MPL_2 — Research notes

## Scope, evidence and status

These notes concern **cote 2, scans 002–045, excluding the three omitted blank scans 006, 027 and 031**. The primary reader completed the transcription and the second visual reading of all 41 retained sheets, recorded the 42 SHA-256 hashes, and froze the transcription at **2026-11-16 20:56:22 UTC**, before opening the context. Research calculations, literature comparisons and alternative interpretations below have not changed any frozen transcription file.

The supplied context contains only `README.md` and `notes/RESULTS_STATE.md`. The README places this cote in Book I, I.X, intersections/Chern classes/Riemann–Roch, at package 246, rank 25, and asks the standing questions; it supplies no neighboring transcript. The register has **zero matching open, settled, intake, returned-package or planning entries** from the user's own project. Its unrelated LM4/LM7 referee list does not establish anything about this cote. The three relevant rows are **Hua, findings register** imports explicitly described as AI-produced, with intake status “new to us: our package for this cote is waiting”; the comparisons here do not promote them to reviewed results.

Each individual note states its scan and kind; own ideas carry confidence and the reason for it. Brief quotations refer to the frozen transcription: a reading marked doubtful there remains provisional here, even when only its readable portion is quoted. “No context match” means no relevant counterpart in the two supplied files, not absence from the archive or literature. Per-note searches were actually run and are retained in `records/context_search_primary.md`, `records/context_search_chern_curves.md`, `records/context_search_lambda.md`, `records/context_search_supports.md`, `records/context_search_standing.md` and `records/context_search_bridge.md`; matching words alone were not treated as mathematical agreement.

The register contains **80 individual substantive notes**, followed by **10 entries for explicitly unverified steps** and **9 title/pagination entries**. Longer independent calculations are retained in the accompanying research records so that the individual notes remain short. Line locators refer approximately to the frozen page fragment or the position on the scan, not to a new editorial line numbering of the manuscript.

### Assessment of the three imported findings

| Supplied register ID | Supplied source scans | What this package adds or changes | Status retained |
|---|---|---|---|
| **2-chern-ring-gamma-comparison** | 021, 022, 029, 030 | The factorial comparison needs its positive-degree scope, the sign discrepancy between 021 and 022 recorded, and the modified product on the return map's target on 030. The explicit λ-homomorphism definition and the shorter relation list on 029 require separate treatment. | Unreviewed imported lead; conditional calculations and primary-literature comparisons below, no claim of novelty. |
| **2-chern-ring-not-injective-pn** | 022 | The sheet answers its own question “Non,” specifies a single chosen geometric generator, and shows how adding `nL−1` changes the universal ring. The exact small case and homogeneous torsion calculation make the example testable. | Unreviewed imported lead; the dependence on the chosen geometric family is essential. |
| **2-trivial-total-chern-class** | 010, 012, 014 | The register describes the cancelled hypersurface setup; the live elliptic point-difference example is verified integrally. Rank zero, the zero/unit convention and the distinction between a sufficient factorial bound and minimal dimension are recorded separately. | Unreviewed imported lead; attribution and hypotheses refined, with a conditional verification of its stated Cartier-divisor version. |

## 1. Curves, the preliminary class group and integral structure
'''

sections=[intro]

def add(ids, source):
    for key in ids:
        if key not in source: raise KeyError(key)
        sections.append(source[key])

add(['A01','A02','A03','A04','A05','A06','A07','A21'],A)
sections.append('## 2. Torsion and trivial total Chern classes')
add([f'CC{i:02d}' for i in range(1,10)],CC)
sections.append('## 3. Equivariant modules and symmetric tensor powers')
add([f'A{i:02d}' for i in range(8,14)],A)
sections.append('## 4. Universal Chern rings and the gamma filtration')
add([f'L{i:02d}' for i in range(1,17)],L)
add(['R01'],R)
sections.append('## 5. Supports, relative perfectness and covariant characters')
add([f'S{i:02d}' for i in range(1,22)],S)
sections.append('## 6. Riemann–Roch for fibrations, curves and surfaces')
add([f'CC{i:02d}' for i in range(10,21)],CC)
sections.append('## 7. Reused algebra leaves and their unresolved readings')
add([f'A{i:02d}' for i in range(14,19)]+['A22'],A)
sections.append('## 8. Internal structure and chronological layers')
add(['A19','A20'],A)
standing=(REC/'research_standing.md').read_text()
standing=standing.split('\n',1)[1].strip()
standing=standing.replace('## Manuscript steps explicitly marked as unverified','## 9. Standing question: steps explicitly marked as unverified')
standing=standing.replace('## Title sheets and page-count statements','## 10. Standing question: title sheets and page-count statements')
sections.append(standing)
sections.append((REC/'references_final.md').read_text().strip())
text='\n\n'.join(sections)+'\n'

# Editorial prose spacing only; source fragments are never touched.
text=text.replace('Cote2','Cote 2')
text=re.sub(r'\b(scans?|on|from|into|in|through)(\d{3})\b',r'\1 \2',text)
text=re.sub(r'\b(Scan|while|cite|rewrite|before|after)(\d{3})\b',r'\1 \2',text)
text=re.sub(r'(Cote 2, )scans (\d{3}) —',r'\1scan \2 —',text)
text=re.sub(r'\b(formula|equation)\((\d+)\)',r'\1 (\2)',text)
text=text.replace('class of1','class of 1').replace('by1_i','by 1_i')
text=text.replace('eigenvaluesζ','eigenvalues ζ').replace('andζ','and ζ')
text=text.replace('Likewise,036','Likewise, 036')
text=text.replace('Atiyah(1966,§2,Proposition2.2)','Atiyah (1966, §2, Proposition 2.2)')
text=text.replace('Atiyah\'s symmetric-group construction(1966,§1)',"Atiyah's symmetric-group construction (1966, §1)")
text=text.replace('Pedrini and Weibel(1994,AppendixA,p.404)','Pedrini and Weibel (1994, Appendix A, p. 404)')
text=text.replace('(Borel & Serre,1958,§§7–9)','(Borel & Serre, 1958, §§7–9)')
text=text.replace('(Serre,1977,§§7.1–7.3)','(Serre, 1977, §§7.1–7.3)')
text=text.replace('Serre(1958,§§4–5)','Serre (1958, §§4–5)')
text=text.replace('The Stacks Project Authors,2026,Tag0AFV','The Stacks Project Authors, n.d., Tag 0AFV')
text=text.replace('The Stacks Project Authors,2026,Tags00GH,0307,090P','The Stacks Project Authors, n.d., Tags 00GH, 0307, 090P')
text=re.sub(r'\b(Tags?)(?=[0-9])',r'\1 ',text)
text=text.replace('equation(17)','equation (17)').replace('formula(14)','formula (14)').replace('formula(2)','formula (2)')
text=text.replace('before(17)','before (17)').replace('conditions(1)','conditions (1)')
text=text.replace('factors2 and4','factors 2 and 4').replace('inclusion1','inclusion 1')
text=text.replace('lifts1_i','lifts 1_i').replace('characterχ','character χ')
text=text.replace('elliptic2-torsion','elliptic 2-torsion').replace('initial1','initial 1')
text=text.replace('when2-torsion','when 2-torsion').replace('n°234','n° 234')
text=text.replace('page−12−','page −12−').replace('sequence−9−','sequence −9−')
text=text.replace('package246/rank25','package 246/rank 25').replace('cote2','cote 2')
text=text.replace('derivation A below','appendix A of `records/research_chern_curves.md`')
text=text.replace('derivation A','appendix A of `records/research_chern_curves.md`')
text=text.replace('derivation B','appendix B of `records/research_chern_curves.md`')
text=text.replace('The title and pagination inventory below','The title and pagination inventory in section 10')
text=text.replace('Stacks Project, Tags','The Stacks Project Authors, n.d., Tags')
text=text.replace('Stacks Project, Tag','The Stacks Project Authors, n.d., Tag')
text=text.replace('The Stacks Project The Stacks Project Authors','The Stacks Project Authors')
text=re.sub(r'(?<![/\w`])RESULTS_STATE\.md(?!`)',r'`notes/RESULTS_STATE.md`',text)
text=text.replace('`context_search_primary.md`','`records/context_search_primary.md`')
text=re.sub(r'\n{3,}', '\n\n', text)
assert not re.search(r'@@[A-Z_]+@@',text), 'Unresolved assembly placeholder'
assert (len(A),len(CC),len(L),len(S),len(R))==(22,20,16,21,1)
(ROOT/'MPL_2_notes.md').write_text(text)
print(f'Assembled {len(A)+len(CC)+len(L)+len(S)+len(R)} substantive notes, standing questions, title/pagination index, and final bibliography.')
