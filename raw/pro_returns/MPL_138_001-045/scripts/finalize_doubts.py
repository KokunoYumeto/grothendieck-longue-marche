#!/usr/bin/env python3
"""Consolidate the root reader's pre-context notation and doubt records.

This reads transcribed text only; it performs no image recognition.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

notation = r"""# Notation and doubts

## Recurring notation

This table records the visual comparison completed before the transcription freeze and before opening the context archive. The font choices are typographic representations of the visible letter forms; explicit alternatives remain where the handwriting does not decide them. A difference in the author's visible writing is retained at its own occurrence.

| Visible form / use | LaTeX representation | Scans | Reading notes |
|---|---|---|---|
| Looped capital with long descending stroke | `\mathcal G` | 005–015 | Compared with the outlined capital and the open plain capital; overwritten occurrences carry doubt marks. |
| Double-contour capital G | `\mathbb G` | 005–014 | Especially clear in 005 (2); the quotient letter at 006, last display, remains `G` with `\mathbb G` as alternative. |
| Open plain G, finite covering group | `G` | 006–014 | Read at 007 (16) and 008 (18); kept plain where the contour is single. |
| Rounded, outlined permutation-group letter | `\unsure{\mathfrak S_3\|\mathbb G_3}` and corresponding indices | 016–017, 027–044 | The shape has both S-like and G-like features; repeated occurrences retain the same explicit alphabet doubt. |
| Cross-shaped, curved X | `\mathcal X` | 005–015 | Straight crossed X is retained as `X`; the covering accent is `\widetilde{\mathcal X}`. |
| Rounded two-loop extension letter | `\mathcal E` | 006–042 | Prime, double prime and tilde are transcribed at their own occurrences. |
| Angular top bar with stem at left | `\Gamma` | throughout mathematical sheets | Compared with centered-stem `T` in 028–042; no script-T replacement is supplied from the mathematics. |
| Centered-stem module letter | `T`, `T_\infty` | 020, 023, 028–042 | Plain T as seen; hats and twists retained individually. |
| Dot with small 1/2 below | `\mathbin{\underset{\scriptscriptstyle1/2}{.}}` | 005, 006, 009, 015, 027–028, 036–042 | Cross-checked with especially clear occurrences on 015 and 027; earlier provisional product readings were corrected before freeze. |
| Plain multiplication/joining dot | `\cdot` or literal `.` with spacing | 016, 019–020, 023, 026 | No small 1/2 is supplied where it is absent from the ink. |
| Tall double vertical group letter | `\Pi_n`, `\Pi_{n\mathbb Q}` | 025–027 | The smaller point-group `\pi_n` is an insertion at 027 (8); scheme and point letter forms are recorded separately as written. |
| Root-of-unity letter, doubled left stem | `\mu_n` | 015–042 | The point-letter top cross-stroke at 027 remains `\unsure{\bar\mu_n\|\mu_n}`; it is not silently propagated to all occurrences. |
| Left-pointing arrow over roots-of-unity letter | `\overleftarrow{\mu}_\infty` | 026, 028 | Read directly from the accent; separate inverse-limit arrows are also retained. |
| Curled centralizer Z | `\unsure{\mathcal Z\|Z}` | 012–013 | Straight Z is retained in the succeeding displays; the lowercase center letter is `z`. |
| Hats on integers; bars on fields | `\widehat{\mathbb Z}`, `\bar k`, `\overline{\mathbb Q}` | throughout | A faint bar in the final field quotient of 036 remains explicitly doubtful. |
| Negative j and conjugate j | `-j`, `-\bar j` | 019, 031, 038 | Signs and bars retained; crossed earlier bars on 038 remain within deletion markup. |
| Pair of nonreal points and its short index | `\alpha`, `\bar\alpha`, `\unsure{\alpha_*\|\alpha_2}` | 031–034 | Compared across the pair definitions, projection and lower labels; retraced indices remain doubtful. |
| Revised real-point labels | `\alpha'(i)` above deleted beta labels | 035 | The final index in (33) is written `2` and retained. |
| Set label with overwritten final argument | `\unsure{\alpha(\infty)\|\alpha(I)}` | 036 | Both the marginal set label and inserted sets retain the ambiguity. |
| Short upper strokes | prime `'`, double prime `''`, star `*` as written | throughout | Checked individually; no exclamation-mark exponent was securely identified in these pages. The literal `!` arrow label at 005 (6) is preserved. |
| Unheaded connecting strokes | `no head` in tikz-cd; `\mathbin{-}` in inline expressions | 005–042 | Arrowheads are supplied only at visible heads. Ambiguous arrow/dash at 011 remains in `\unsure`. |
| Vertical inclusion strokes | `\cup`, `\bigcup`, spatially placed | 007, 019 and related displays | Their orientation is retained rather than rotated into a horizontal conventional formula. |
| Two-stem abbreviation | `tt`, occasionally `\unsure{\mathrm{tt}\|\forall}` | 007, 012–015, 017 | Compared with clear underlined `tt` on 007; the uncertain instance on 012 has `tt` first. |
| Source double quotation marks | two backticks and two apostrophes | manuscript prose | Literal printed guillemets are kept on the printed sheet where visible. |
| Underlining and double underlining | `\uline`, `\uuline` | throughout | The pair of vertical emphasis strokes beside the final note on 039 is drawn in TikZ. |
| Incomplete brackets, missing factors, revised numbering | same visible signs and numbering | 019, 022, 030, 032, 035 | No completion or mathematical repair has been inserted. |
| Circled section labels | `\textcircled{...}` | 005–014 | These are section labels. No author's page number was securely identified; later archive foliation is recorded only in comments. |
| Tables, diagrams and drawings | arrays, tikz-cd, TikZ | throughout | Drawing positions are approximate; the two photographs on 002 and complex sketches on 044 have crop-candidate comments. |

## Doubts

Positions refer approximately to the manuscript page. The reading column gives the first ink reading; alternatives and reasons are editorial. Rows at high confidence preserve unusual visible writing or record a resolved visual question. The exact inline-marker index below supplements this position table, including repeated occurrences of the same uncertain glyph.

| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
"""

rows = (ROOT/'records/doubts_rows.md').read_text()
replacements = {
    '| 138 | 005 | (7), product sign | ltimes | sign written below dot, construction of glyph uncertain | medium |':
    '| 138 | 005 | (7), product sign | dot with small 1/2 underneath | checked directly against 005 and the clearer repeated form on 015 | high |',
    '| 138 | 006 | last display number | 14 | 12 | low |':
    '| 138 | 006 | last display number | 12 | 14 | low |',
    '| 138 | 012 | uniqueness sentence | forall | tt | low |':
    '| 138 | 012 | uniqueness sentence | tt | ∀; two-stem form compared with scan 007 | low |',
    '| 138 | 020 | before indép. | Z | large cursive initial letter; reading reflects visible zigzag | medium |':
    '| 138 | 020 | before indép. | Z | Q; large cursive initial letter, with a zigzag in the first reading | medium |',
    '| 138 | 025 | lower left note | alpha_i | alpha(i) | low |':
    '| 138 | 025 | lower left note | alpha(i) | alpha_i | low |',
    '| 138 | 025 | last two lines | un donne rev. principal | on donne rev. principal; line partly at sheet edge | low |':
    '| 138 | 025 | last two lines | un; donne | on; trouve; line partly at sheet edge | low |',
    '| 138 | 041 | diagram annotation | alpha_1 | small subscript under alpha; identity marks placed under alpha only | medium |':
    '| 138 | 041 | diagram annotation | alpha_1 | small subscript under alpha; identity marks under both aligned upper nodes reproduced | medium |',
    '| 138 | 044 | margin final lines | ce qui combinatoire / entraîne; on le voit de suite le rev. abélien universel | lowest insertion physically clipped; du monoèdre par 2 is only a provisional ink reading | low |':
    '| 138 | 044 | margin final lines | ce qui entraîne; on le voit de suite le rev. abélien universel | combinatoire as alternative to entraîne; lowest insertion physically clipped, with du monoèdre par 2 and a faint final dash only a provisional reading | low |',
}
for old,new in replacements.items():
    assert old in rows, old
    rows = rows.replace(old,new)

additional = r"""| 138 | 006 | last quotient letter | `G` | `\mathbb G`; partly overwritten contour | low |
| 138 | 009 | (23), third variant | `\mathcal G_1` | `\mathcal G'_1`; small mark at upper right | low |
| 138 | 011 | upper paragraph | trivialt | compressed final abbreviation, underlined in the ink | medium |
| 138 | 011 | final situation | arrow between X prime and X | unheaded dash; head is faint | low |
| 138 | 012 | uniqueness sentence | s'égaliser | s'égaler | low |
| 138 | 013 | definition mark at (30) | dfn | def; letters are compressed | low |
| 138 | 037 | after donc à | pointer | prendre; the small joined strokes favour pointer at enlarged inspection | medium |
| 138 | 038 | opening word | Rappelons | Rappel; trailing strokes are faint | medium |
| 138 | 039 | final marginal emphasis | two vertical strokes | positions approximate; no horizontal double underline transcribed | high |
| 138 | 044 | clipped final insertion | du monoèdre par 2 followed by faint dash | words and mathematical continuation remain very low confidence; no continuation supplied | low |
"""
all_rows = [x for x in (rows+additional).splitlines() if x.strip()]
all_rows.sort(key=lambda x:int(x.split('|')[2].strip()))

abbreviations = r"""

## Abbreviations

The following expansions are editorial suggestions, restricted to this list. The original abbreviations, punctuation and grammatical forms remain in the transcription; the expansion depends on the immediate occurrence.

| Form met | Suggested expansion | Confidence / qualification |
|---|---|---|
| alg. | algébrique | high |
| aut.; autom. | automorphisme(s) | high |
| aut. ext.; Autext | automorphismes extérieurs | high |
| aut. int; int | automorphisme intérieur; conjugaison intérieure | high |
| can.; can- | canonique(s); first part of canonique across a sheet break | high |
| car. | caractéristique | high |
| ch. | chaque | high |
| Ch 2. | chapitre 2 | low; faint reference on 005 |
| comm. | commutatif / commutativité | medium |
| d'ext | d'extension | high |
| dfn / def | définition | low; compressed notation at 013 |
| dim | dimension | high |
| ds | dans | high |
| él.; élts; élém. | élément(s) | medium; cancelled last abbreviation on 032 is uncertain |
| ens. | ensemble | high |
| ext. | extension | high |
| gén. | généralement / général | medium; depends on occurrence |
| géom | géométrique(s) | high |
| grpe | groupe | high |
| hom. | homomorphisme | high |
| hyp. | hypothèse | high |
| i.e. | id est | high |
| indép. | indépendant(s) | high |
| inv. | invariant(s) | high |
| iso.; isom | isomorphisme | high |
| lim. proj. | limite projective | high |
| mod. | modulo | high |
| NB | nota bene | high |
| op. | opération / opérant | medium; depends on occurrence |
| pb | problème | high |
| prés. | présentation | high |
| pt; pts | point(s) | high |
| quots | quotients | medium |
| rat | rationnel(s) | high |
| resp. | respectivement | high |
| rev. | revêtement | high |
| s-grpe; ss-grpe; ss-groupe | sous-groupe | high |
| sép. | séparable / séparablement | high |
| ss-ext. | sous-extension | high |
| ssi | si et seulement si | high |
| surj | surjectif | high |
| syst. fond. | système fondamental | high |
| top. | topologique | medium; cancelled occurrence on 007 |
| trivialt | trivialement | medium; compressed final letters |
| tt | tout / tous | medium; number depends on the occurrence; faint forms explicitly doubtful |

## Legibility and limits of confidence

All 44 full-page images and their 88 overlapping halves were inspected personally in one stream, without OCR; each page then received a separate second visual audit. The printed and typed sheets are usually clearer than the handwritten mathematical leaves. Fine letter endings, crowded indices, heavily cancelled formulas and the exact typographic alphabet of rounded group letters remain the principal sources of uncertainty. An unmarked reading still represents a visual reading, not a guarantee of editorial infallibility.

The least secure prose lies in cancelled passages and marginal writing at 007, 012, 017, 025, 036 and 044. The bottom of the insertion at 044 is physically clipped, and its provisional words must be checked against a fuller image before being quoted as secure text. The pair labels and overwritten coordinates at 031–038 deserve particular caution; the repeated S/G alternatives deliberately retain a font ambiguity. The two-word `\illegible{2}` at 036 is confined to cancelled prose; no mathematical symbol or diagram was replaced by an illegibility placeholder.

The table on 002, printed matter on 003, notice on 043 and cancelled reused letter on 045 were transcribed along with the mathematical leaves. Archive foliation is commented rather than promoted to an author's page number. TikZ reproductions preserve visible labels and main geometry, while photographic details on 002 and crowded sketches on 044 are approximations explicitly marked as crop candidates. Drawings, cancellation strokes and spacing cannot be regarded as facsimile reproductions.

## Exact inline doubt-marker index

This mechanical index is generated from the completed page files, not from image recognition. Its line numbers refer to the individual `.tex` file and are supplied only to locate every marker precisely; manuscript positions and confidence assessments are given in the table above and in the recurring-notation table. Each value below is the literal macro argument, including its first reading and any alternative; `|` is displayed as `\|` solely to keep the Markdown table valid.

| Cote | Scan | TeX line | Marker | Literal argument |
|---|---|---|---|---|
"""

def macro_arguments(text):
    for m in re.finditer(r'\\(unsure|illegible)\{',text):
        start=m.end(); pos=start; level=1
        while level:
            c=text[pos]
            slash=0; j=pos-1
            while j>=0 and text[j]=='\\': slash+=1; j-=1
            if slash%2==0:
                if c=='{': level+=1
                elif c=='}': level-=1
            pos+=1
        yield m.group(1),text.count('\n',0,m.start())+1,text[start:pos-1]

index=[]
for path in sorted((ROOT/'pages').glob('*.tex')):
    scan=int(re.search(r'scan(\d+)',path.name).group(1))
    for name,line,arg in macro_arguments(path.read_text()):
        arg=arg.replace('\n',' ').replace('|',r'\|').replace('`','&#96;')
        index.append(f'| 138 | {scan:03d} | {line} | `{name}` | `{arg}` |')

(ROOT/'MPL_138_001-045_doubts.md').write_text(notation+'\n'.join(all_rows)+'\n'+abbreviations+'\n'.join(index)+'\n')
print(f'Wrote {len(all_rows)} positioned doubt rows and {len(index)} exact inline marker entries.')
