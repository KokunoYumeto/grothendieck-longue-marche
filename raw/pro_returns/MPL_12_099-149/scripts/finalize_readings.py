#!/usr/bin/env python3
"""Apply the root reader's final, image-checked notation decisions before freeze."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
P = 'MPL_12_099-149'
log = ROOT / 'progress.log'
assert 'transcription frozen ' not in log.read_text()

def patch(n, old, new):
    p = ROOT / 'pages' / f'{P}_12_scan{n:03d}.tex'
    t = p.read_text()
    assert old in t, (n, old)
    p.write_text(t.replace(old, new))

patch(108, r'\ell', 'l')
for n in (111, 114):
    patch(n, r'\operatorname{Spec}\mathbb Z',
          r'\unsure{\operatorname{Sp}|\operatorname{Spec}}\mathbb Z')

path = ROOT / f'{P}_doubts.md'
old = path.read_text()
register = old.split('## Doubt register\n', 1)[1].split('## Abbreviations\n', 1)[0]
replacements = {
    '| top spectral-sequence exponent | pq / rs | Faint small pair; alternative retained | low |': '| top spectral-sequence exponent | rs | pq; enlarged during audit | medium |',
    '| replacement paragraph | ms | Abbreviation for mêmes apparently visible | medium |': '| replacement paragraph | = | Literal equality/ditto sign; first-pass ms withdrawn | high |',
    '| C1 result wording | même | Written as a very abbreviated equality-like form | medium |': '| C1 result wording | = | Literal equality/ditto sign; not the written word même | high |',
    '| C2 level bound | Inf(i,n) / Inf(2i,n) | First argument overwritten; no mathematical normalization | low |': '| C2 level bound | Inf(2i,n) | Inf(i,n); enlarged during audit, no mathematical normalization | medium |',
    '| theorem derived image | R^i_! f_!(F) | the extra subscript exclamation under R is visibly present | medium |': '| theorem derived image | R^i_! f_*(F) | f_! remains an alternative; the lower ! under R is distinct | low |',
    '| repeated coefficient Q alphabet | bold Q_l | plain Q_l; heavily retraced Q, not securely a cancellation | medium |': '| repeated coefficient Q alphabet | double-stroke Q_l | plain or retraced Q_l; not securely a cancellation | low |',
    '| affine adjective | exclt | excellent abbreviation ending uncertain | medium |': '| affine adjective | noeth. | exclt; enlarged during audit, ending compressed | medium |',
    '| top total degree | α | *; overwritten superscript | low |': '| top total degree | * | α; overwritten superscript | medium |',
    '| NB line opening | en gr. | short faded abbreviation | low |': '| NB line opening | gr. fini | en gr.; enlarged during audit | low |',
    '| characteristic-zero parenthesis | néronique | unusual criterion label; low-resolution join at first syllable | low |': '| characteristic-zero parenthesis | critique | néronique; word remains unresolved after enlargement | low |',
    '| parenthesis about finite sums | ou qui revient au = | ce qui revient au =; small insertion | low |': '| parenthesis about finite sums | ce qui revient au = | ou qui revient au =; small insertion | medium |',
    '| final words | c à qui | ce qui; faint separated strokes | low |': '| final words | ce qui | c à qui; faint separated strokes | medium |',
    '| M superscript | * | natural/sharp-like doubled strokes | low |': '| M superscript | sharp-like mark | * or natural; enlargement favours doubled parallel strokes | medium |',
    '| h, M superscripts at opening | * | natural/sharp-like retracing | low |': '| h, M superscripts at opening | sharp-like mark | * or natural; compared with scan 145 | medium |',
}
for a,b in replacements.items():
    assert a in register, a
    register = register.replace(a,b)
register += '\n| 12 | 111 | left definition note, spectrum abbreviation | Sp | Spec; compressed terminal strokes | medium |\n'
register += '| 12 | 114 | proof, base spectrum abbreviation | Sp | Spec; compressed terminal strokes | medium |\n'
register += '| 12 | 111 | bottom-left eff! | eff! | A separate dot is visible after enlargement; retained as punctuation-like mark rather than silently changed to raised t | high |\n'

notation = r'''# Doubts and notation record

## Notation table

This table was maintained during the single-reader transcription and consolidated against the images before the freeze. A difference retained below reflects a visible difference or an explicitly unresolved form, not a choice supplied by the mathematical argument. The first alternative in every `\unsure` is the reading favoured by the ink.

| Visible form | LaTeX | Scans / audit decision |
|---|---|---|
| Double quotation marks | two backticks followed by two apostrophes | All actual double quotes use the same LaTeX convention; no guillemets supplied. |
| Ordinary capital and lower-case variables | `H,X,Y,F,E,P,Q,R,S,T,U,V,i,j,k,l,p,q,r,n` | Ordinary letters are not promoted to script or double-stroke alphabets from mathematical expectation. |
| Prime-index letter | `l` | The same looped handwritten lower-case l is used throughout; the three earlier `\ell` spellings on 108 were aligned to `l` after comparison with 111. |
| Single versus double-stroke coefficient letters | `Q,Z` versus `\mathbb Q,\mathbb Z` | Explicit double strokes are retained on 111–116 and 141; heavily retraced forms on 125,129,149 carry ordinary-Q alternatives. Generic field Q and k on 145 are not normalized to one another. |
| Projective-space letter | `P^2` or `\mathbb P` as visible | Plain P in 101; the doubled letter in 111 is distinguished. |
| Script category letters | `\mathcal V,\mathcal C,\mathcal M` | 144–149: V is script V, not Greek nu. The cancelled script-like F on 125 remains doubtful. |
| Weight subset | `\Phi` | 111 onward: capital loop and tall stem, distinct from plain P. |
| Level parameter | `\nu`, with `\unsure{\nu&#124;\gamma}` where needed | 112–113 compared directly; two overwritten forms on 112 retain gamma as alternative. |
| Group-to-motive functor | `\unsure{\varphi&#124;\Phi}` | 141–142: capital/lower-case distinction is not secure. |
| Functor equivalence letters | `\varphi,\psi` | 146: distinguished from the source's V and target M. |
| Cech/cover indexing | `\sigma`, with local `s` alternatives | 107; no inferred replacement of the written index. |
| Projectors | `\pi,\pi',\varpi,\varpi'` | 145,147: broad omega-like varpi with a horizontal head is distinct from pi. |
| Lower shriek on H | `H^i_!` | 099,104–109: the dotted lower mark is not a prime. The overwritten sign in 099 item 3 remains `\unsure{*&#124;!}`. |
| Shriek, star and prime on direct images | `i_!,f_*,R^i_!f`, local `\unsure` | 111–137: placement under R and/or f is preserved; 113 keeps `R^i_!f_{\unsure{*&#124;!}}` rather than normalizing it. |
| Total-degree mark | `\unsure{*}`, or `\unsure{\alpha&#124;*}` / reverse | 105–108,115,137: tiny stars and alpha-like marks are not inferred from spectral-sequence convention. |
| Genuine exclamation after eff | `eff!` | 111 bottom-left warning: enlarged image shows a separate dot. |
| Raised abbreviation ending | `eff$^{t}$`, `str$^{t}$`, `\mathrm{ess}^{t}` | 112 onward; cramped forms on 112 retain `t&#124;!`. These forms are not globally converted to exclamation marks. |
| Tilde and primes | `\widetilde T,T',\widetilde T'` | 101: each visibly written prime is retained, including surprising ones. |
| Check on a dual | `\check F` | 111–113: distinct from hats on compactifications. |
| Compactification hats | `\widehat X,\widehat V,\widehat h` | 113,131; the faint first hat on h and the Y-hat on 135 remain doubtful. |
| Doubtful derived-functor decoration | `\unsure{\widehat R&#124;R^\uparrow}` | 116: no confident standard derived notation supplied. |
| Doubled derived R | `\unsure{\mathbb R&#124;\mathbf R}` | 133: the doubled vertical is visible, its typographic alphabet uncertain. |
| Closure bar | `\overline{x},\overline{f(X)},\overline{U-V}` | 116,125,133: distinguished from hats, tildes and underlines. |
| Dense source-category superscript | `^{\unsure{\circ&#124;*}}` | 144: circle remains first reading; no supplied interpretation in transcription. |
| Completion superscript | `^{\unsure{\sharp&#124;*&#124;\natural}}` | 145–146: enlarged doubled strokes favour sharp; explicitly distinguished from the small mark on V in 144. |
| Underlining | `\uline`, `\uuline`, standard math `\underline` | Single and double strokes retained; live semi-simple at foot of 146 is underlined, not cancelled. |
| Plain connectors | `\mathbin{-}`, `\arrow[...,no head]`, `\arrow[...,dash]` | 101,105,125,127,140,142,144–149: no arrowhead added where a shaft alone is visible. |
| Unheaded hook | `\arrow[...,hook,no head]` | 116: hook retained without inventing a terminal head. |
| Spectral-sequence abutment | `\Longleftarrow` | Left-facing double arrows on 105,107–108,114,137. The assignment in 107 also points left, as written. |
| Reversed triangle edge | `X\longrightarrow U`, label i | 135: kept even though adjacent prose gives i:U→X. |
| Literal ditto signs | `De \(=\)`, `de \(=\) nature`, `\mathbin{-}` | 107,109,141,147,149: no expansion to même or repeated words. |
| Spectrum abbreviation | `\operatorname{Sp}`, local `Sp&#124;Spec` | 105,127 use Sp; 111 and 114 retain an uncertain short form; 142 has the longer visible Spec. |
| Operator abbreviations | `\operatorname{Im},\operatorname{Ker},\operatorname{Inf},\operatorname{Fl}` | Capitalization and spelling retained; Fl replaces a cancelled Hom in 144. |
| Fractional shorthand | `\frac12` | Before simple/simplicité: 113,115,140; not expanded in transcription. |
| Exterior and tensor powers | `\bigwedge`, `\otimes`, `\overset{n}{...}` | 116,149; faint degree n is marked where uncertain. |
| Two tensor symbols | `\boxtimes`, `\otimes` | 149: cancelled otimes replaced by boxtimes for V, while M uses otimes. |
| Circled item labels | `\textcircled{A}`, `\textcircled{1}`, etc. | Item labels, not author page numbers. |
| Blank table cells and ruled voids | empty array cells, `\times`, `\diagup` | 104–118: empty cells are not supplied with ellipses; drawn crosses and dividers are retained. |
| Literal surprising indices and bounds | e.g. `\operatorname{inj}_2u\operatorname{pr}_2` | 148 and numerical tables: no correction from expected mathematics. |

## Doubt register

Locations are approximate manuscript positions. Audit observations are retained alongside the corresponding rows; the readings below have been reconciled to the final pre-context text. Confidence concerns the visual reading, not the truth of the mathematical assertion.

'''
abbreviations = old.split('## Abbreviations\n',1)[1].split('## Legibility and limits',1)[0]
abbreviations = abbreviations.replace('- `ms`: probably mêmes (107), uncertain.', '- `ms`: a first-pass conjecture withdrawn on checking the equals/ditto signs; not expanded in the transcription.')
abbreviations = abbreviations.replace('- `en gr.`: en groupes (reading uncertain in scan 141).', '- `gr. fini`: groupe fini; the reading is uncertain in scan 141, with `en gr.` retained as an alternative.')
abbreviations += '\n- `noeth.`: noethérien / noethérienne (133; contracted reading uncertain).\n'

legibility = '''## Legibility and limits

The 36 retained scan pages were read by the same reader in order, from each whole image and its two supplied halves, then audited a second time against those images. No OCR was used. The covers and the printed offprint cover on scan 119 are substantially clearer than the fast manuscript prose; its small publisher emblem is a TikZ approximation and is explicitly marked as a crop candidate. Scans 120 and 122 are reused typed sheets: reversed show-through from the other face was distinguished from writing on the photographed face, and no extra text was invented from that bleed-through.

The weakest passages are the densely cancelled marginal block and multiple revisions on 111; cancellations and overlapping formulas on 108,113,120,125,131; the last NB on 141; the unresolved criterion word on 142; and the interleaved cancelled and inserted proof on 147. The exact scope of a cancelling bracket on 147 is especially uncertain. The small terminal marks on category symbols in 144–146, some coefficient alphabets, and the cramped primes and arrowheads on 140 are explicitly marked rather than resolved by expectation. Numerical weight/level tables were checked cell by cell, but their overwritten individual digits remain less secure than the broad organization of those tables.

`\\illegible{n}` is confined to estimated counts of physically obscured words after enlargement; uncertain mathematical symbols have a proposed `\\unsure` reading instead. Existing unmatched parentheses, abbreviated words, grammatical irregularities, surprising inequalities and arrow directions are retained. The inventory records the elements that were transcribed; it is a coverage record, not a claim that every difficult reading is correct. All research comparisons were deferred until after the transcription freeze, and any later reading questions belong exclusively in the separate notes.
'''
text = notation + register + '\n## Abbreviations\n' + abbreviations + '\n' + legibility
# Markdown tables need contiguous rows, unlike the incremental working register.
text = re.sub(r'(\|[^\n]*\|)\n\s*\n(?=\|)', r'\1\n', text)
path.write_text(text)

inv = ROOT / f'{P}_inventory.csv'
with inv.open(newline='') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['scan'] == '147' and row['element'] == '147.24':
        row['first_words_or_objects'] = 'P′+P″, Q′+Q″; P′, Q′; doubtful π label'
with inv.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
    f.write(f'notation comparison completed {now}\n')
    f.write('Final pre-context notation review: lower ! versus primes/stars, raised abbreviation endings, l, coefficient alphabets, category superscripts, phi/nu, hats/checks/tildes/bars, quotes, connectors, ditto signs and abbreviated Sp compared against images. Doubt register reconciled; legibility note completed.\n')
print('Final image-checked notation decisions saved; context remains unopened.')
