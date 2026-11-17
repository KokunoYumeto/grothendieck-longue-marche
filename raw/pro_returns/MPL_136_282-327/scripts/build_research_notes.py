#!/usr/bin/env python3
"""Assemble post-freeze notes. Never writes a transcription or page file."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

HEADER = r'''# Research notes: MPL_136_282–327

**Cote 136; scans 282–327, excluding 319; 45 supplied pages. Prepared 17 November 2026.**

## Evidence, attribution, and limits

These notes were written after the 45 individual transcriptions and their combined fragment were frozen at **11:40:51 UTC**; the context archive was opened at **11:40:55 UTC**, as recorded in `progress.log`. The primary transcriber personally read every supplied whole image and both halves in order, then audited every page again; no OCR or delegated transcription was used. Research calculations and contextual comparisons below have not changed the frozen text. A citation such as **136/318:25–27** means cote 136, scan 318, approximately lines 25–27 of its individual TeX file, not the author's manuscript pagination.

The following abbreviations identify the supplied contextual files, which are not reproduced in this deliverable:

| Abbreviation | Exact supplied file | Evidential status |
|---|---|---|
| A | `same_cote_136/MPL_136_047-094_notes.md` | Earlier first-pass notes, expressly unreviewed; source scans not supplied here. |
| B | `same_cote_136/MPL_136_095-141_notes.md` | Earlier first-pass notes, expressly unreviewed; source scans not supplied here. |
| C | `same_cote_136/MPL_136_189-234_notes.md` | Earlier first-pass notes, expressly unreviewed; source scans not supplied here. |
| D | `same_cote_136/MPL_136_235-281_notes.md` | Earlier first-pass notes, expressly unreviewed; source scans not supplied here. |
| H | `hua_project/136.modern.tex` | **Michel Hua's project's AI-produced modernised reading**, credited to that project; neither a diplomatic edition nor human-verified source text. Its page labels are not automatically our scan numbers. |
| R | `notes/RESULTS_STATE.md` | The entire supplied 502-line digest was read; statuses are the originating runs' claims unless a particular review is explicitly recorded. |
| PS VI / VII | `ps_chapters_VI_VII/ps6.tex` / `ps7.tex` | Supplied typed-up *Pursuing Stacks*, cited by section and manuscript page; the relevant passages were read. |

Every numbered research item below gives the current source, a short quotation or literal formula, its kind, the earlier context and relationship, and any relevant R identifier. “No matching entry” means none was found in the supplied digest, not that the subject has never been studied. “Adds” identifies what this packet contributes to the supplied evidence; it is **not a claim of mathematical novelty**. Own calculations are identified explicitly, with assumptions and confidence; complete algebraic arguments are in `records/algebra_checks.md`. The three research dossiers in `records/` preserve the post-freeze comparison work and are subordinate to these integrated notes wherever wording differs.

## Direct answers to the assigned questions

| Question | Answer supported by this packet |
|---|---|
| Is the lecture complex a functorial integral cochain algebra computing cohomology and products, with divided powers on cochains? | The packet supports a functorial **additive** framework and a programme for additional operations; it does not establish that unrestricted statement. The author explicitly separates raw invariants from homotopy invariants (306), additive chains from multiplication (311–312), and ordinary tensor structures from Dold–Puppe equivalence (318). The precise weighted comparison, PD descent, and homotopy-type reconstruction remain the open questions **follow-ups @305**; see N25–N39. |
| What are the de Rham topos and its “faisceautisation”? | Current 302 uses the simplicial presheaf topos, and 314 expects universal abelianization to extend to arbitrary topoi. The strongest supplied lead for the earlier phrase is A, R027–R041, reporting internal PD/exterior resolutions and a tensor-universal acyclicity condition on 080–091; no separately specified de Rham site is identified in this range (N03–N04). |
| What are the universal constructions and the lecture plan? | There is an actual cover, 301, and a locally numbered unit of seventeen pages, 302–318. Its progression is simplex notation and free cocompletion, additive normalization and universal chains, then categories of operations and explicit multiplicative reservations; 320–325 continue with unfinished PD-coalgebra calculations (N01–N13, N22–N24 and the exposition map). This does not determine the full lecture's length or delivery order. |
| Does he name abelian varieties or Chern classes of a Fourier transform among the examples? | Abelian schemes occur on **reused Exposé IX typescript**, not as an identified example of the live PD exposition. The handwritten 326 contains possible characteristic-class notation, and 327 a genuine complex-curve/connection investigation, but neither “Fourier” nor “Chern” is named in the frozen current text and no Fourier-transform Chern-class computation is given (N19–N21, geometry notes). |
| Are “ombre,” “tubulure,” or an application to cote 137 identified? | Neither term nor a cross-reference to cote 137 is located in the current frozen text. The module on 299 is a precise shadow-comparison lead; a reference to **scan 137 of cote 136** in earlier notes is not evidence about **cote 137** (N17–N18). |

## I. The programme, universal constructions, graded modules, and source layers

'''

kind = {
1:'unpursued implication',2:'unpursued implication',3:'reading question',
4:'unproved claim',5:'reading question',6:'unpursued implication',
7:'unpursued implication',8:'unpursued implication',9:'unpursued implication',
10:'unpursued implication',11:'self-flagged',12:'withdrawn in the same text',
13:'self-flagged',14:'unpursued implication',15:'self-flagged',
16:'unpursued implication',17:'reading question',18:'reading question',
19:'reading question',20:'reading question',21:'self-flagged',
22:'unpursued implication',23:'self-flagged',24:'unproved claim'}

def main():
    dossier=(ROOT/'records/context_lecture_research.md').read_text()
    segment=dossier.split('## Proposed research items\n',1)[1].split('\n## Local exposition map',1)[0]
    segment=segment.replace('The manuscript says that representable or simplex-defined invariants are too coarse in structure to be homotopy invariants directly, and proposes adding structure before inverting arrows induced by homotopy equivalences.', 'The manuscript says that representable or simplex-defined invariants are not directly invariant under homotopy equivalence, and proposes adding structure before inverting arrows induced by homotopy equivalences.')
    blocks=re.split(r'(?=^### CL\d\d)',segment,flags=re.M)
    out=[HEADER]
    for block in blocks:
        if not block.strip(): continue
        m=re.match(r'### CL(\d\d) — (.*)\n',block)
        assert m
        n=int(m.group(1))
        block=block[m.end():].strip()
        out.append(f'### N{n:02d} — {m.group(2)}\n\n**Kind:** {kind[n]}.\n\n{block}\n\n')
    extras=ROOT/'records/integrated_notes_additions.md'
    if extras.exists(): out.append(extras.read_text())
    (ROOT/'MPL_136_282-327_notes.md').write_text(''.join(out),encoding='utf-8')
    print('Wrote integrated research notes; no transcription touched.')

if __name__=='__main__': main()
