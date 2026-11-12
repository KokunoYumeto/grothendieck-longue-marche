# Sample check of the first pass MPL_1_002-050 (cote 1, scans 3–50)

Eight pages were checked against the scans: an early and a late page from each of the four parallel streams of
GPT-6 Astra (ChatGPT Pro mode). Every line of the first-pass transcription was compared with the page halves from
`MPL_1_002-050_scans.zip`; disputed places were cropped and enlarged from the archive's own page images in `1.pdf`.
The ink decided. Line numbers ("l.") count manuscript lines from the top of the page and are approximate.

Scoring rule: the error rates count discrepancies of high and medium confidence. Low-confidence discrepancies
(mostly small marks: bars, arcs, strokes) are listed in the same table and counted separately. Words are estimated
from the checked transcription: prose words, struck text included, plus one word per formula and one more per
relation sign or comma in it. On scan 024, a struck block of about 82 words (lower half, crossed out with long
diagonal strokes) could not be read better than the first pass did; it is left out of the score.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 004 | l. 5, "donc pour … y∈C''" | `pour \(\forall y\in C''\)` | `pour ~~tout~~ y∈C''`: a word struck with three strokes, no ∀ | DI | no | medium |
| 004 | l. 12, "hermitien pour … x∈C" | `pour tout \(x\in C\)` | `pour ~~tout~~ x∈C` (solid bar through *tout*) | DI | no | high |
| 004 | l. 19, "Pour … a∈Γ₁" | `Pour tout \(a\in\Gamma_1\)` | `Pour ~~tout~~ a∈Γ₁` (solid bar) | DI | no | high |
| 004 | l. 21 | `T_a x=ax` | `T_a(x) = ax` | OM | no | high |
| 004 | l. 22, "donc pour … a∈Γ₁" | `pour \(\forall a\in\Gamma_1\)` | `pour ~~tout~~ a∈Γ₁` (struck as on l. 5) | DI | no | medium |
| 012 | P′₃ | `semi-continue` | `semi continue` (no hyphen) | OT | no | medium |
| 012 | line after the struck block | `\unsure{une suite bornée\|des suites bornées}` | `… bornées` (plural; the two words before it not settled) | MW | yes, alternative right | medium |
| 012 | same line | `\unsure{converge\|convergent}` | `convergent` | MW | yes, alternative right | medium |
| 012 | last line | `L^1(\unsure{K\|k})` | small `k` | MS | yes, alternative right | low |
| 012 | Définition 1 | insertion `I=]0,ω[ (0<ω≤+∞)` placed only after `Soit ~~M …~~` | the insertion sits under the struck `M un espace mesuré (mesure m)`, and an arc runs to it from `sur ~~M~~` | PL | no | low |
| 012 | left margin | — | pencil stroke from the margin note to "Définition 1" | OM | no | low |
| 012 | P₂ | — | short vertical stroke under the display | OM | no | low |
| 015 | l. 1 | `\deleted{d'où} i.e.` | `i.e.` is written above the struck `d'où`: an insertion | DI | no | high |
| 015 | l. 1 | — | small star-like mark and stroke above "compact" | OM | no | low |
| 015 | l. 2 (struck) | `\unsure{compact} \unsure{fblt} compact` | two words, about `qu'il est`, then `fblt compact` | MW | yes | medium |
| 015 | l. 3 | `\sigma(L^{\unsure{1\|\infty}}(K),…)` | overwritten L with a clear `∞`: `σ(L^∞(K), L^∞(K))` | MS | yes, alternative right | medium |
| 015 | "En vertu de P₁" | `\deleted{\unsure{spectralement}}` | `spectralement` is not struck; the line above it is the guide line of the insertion | DI | yes (the word, not the deletion) | medium |
| 015 | same line | `équimesurable` | `équivalente` | MW | no | medium |
| 015 | same line | insertion `i et tout g∈L^∞(K)` placed after *spectralement* | its guide line starts right after `g`, before *spectralement* | PL | no | low |
| 015 | margin note 1 | — | brace joining the note to lines 3–5 | OM | no | low |
| 015 | margin note 2 | — | vertical line with arrowheads beside the note | OM | no | low |
| 015 | "L_i∈L¹(K), …" | — | an "&"-like blot before the struck words | OM | no | low |
| 024 | margin note 2 | `\unsure{Définition de} W(A)` | first word begins with R (`R…tion de`) | MW | yes | medium |
| 024 | last lines | `\inserted{(Si E est un projecteur …}` | ordinary continuation under the struck block, enclosed by a long line | OT | no | low |
| 027 | l. 1 (struck) | `\unsure{Corollaire} $A\unsure{\in\underline b}$` | `~~[word] A [word] [word]~~`: two words after A, not "∈ b" | MW | yes | medium |
| 027 | insertion above C | `=\unsure{C_0(A)}` | `= C_0(M)` | MS | yes | medium |
| 027 | display after "on trouve" | `\unsure{E\mathrm{\ comm.\ }A}` | last letter looks like H or M | MS | yes | low |
| 027 | "(N° 1, formule (4))" | `\unsure{d'où} dans (5),` | `d'où donc dans (5,`: *donc* missing | OM | no | medium |
| 027 | same | — | stroke under `d'où` (underline or strike) | DI | no | low |
| 027 | same | `(5),` | `(5,` | OT | no | low |
| 027 | same | `le \unsure{deuxième} membre.` | `le […] mb.`: abbreviation expanded | OT | no | medium |
| 027 | Corollaire 4 | `A\longmapsto\varphi_{\|A\|}^-(t)` | `A — φ…`: plain dash, no bar, no head | MS | no | medium |
| 035 | "Astuce" note | `on \unsure{plonge} un` | `on vt. […] un`: token *vt.* missing | OM | no (next word unsure) | medium |
| 035 | after Prop. 1 | `\unsure{second membre}, il suffit` | `second mb.`: abbreviation expanded | OT | yes | medium |
| 035 | same | — | a short token after `mb.` | OM | no | low |
| 035 | same | `il suffit` | `Il suffit` | OT | no | low |
| 035 | Prop. 2 | — | small `φ` written above the first `φ_{\|A\|}` | OM | no | low |
| 035 | Prop. 2, line 2 | `\unsure{que}` | the word before `φ_{AA*}` looks struck | DI | yes | low |
| 039 | ll. 5–6, insertions | `\unsure{l'on range les} \unsure{finies} \unsure{en gardant même} \unsure{du point de vue du rang} n+1` | about `le rang est bien […] y a même / à partir [..] rang n+1` | MW | yes | medium |
| 039 | same | — | the insertions are in a rounder, different-looking hand; not noted | OT | no | low |
| 039 | l. 6 | `à $\lambda_n(u)$` | `à λ₁(u), ——— λₙ(u)` | OM | no | medium |
| 039 | "Si h est … positif" | `hermitien positif` | `~~hermitien~~ positif` | DI | no | medium |
| 039 | display after "On a aussi" | `\inf_{E_n}\sup_{x\in E_n}` | `Inf_{F_n} Sup_{x∈F_n}` (two symbols) | MS ×2 | no | medium |
| 039 | same, end of line | `\uline{d'où}` | `, d'où` with a low line through or under it | DI | no | low |
| 039 | same | — | a raised token after `d'où` (like "?:i 2") | OM | no | medium |
| 039 | boxed formula after "en prenant h=\|u\|" | `\inf_{E_n}` | `Inf_{F_n}` | MS | no | medium |
| 039 | left margin, "où … parcourt" | — | a margin mark (like "ℓs") | OM | no | low |
| 039 | struck line before Ky-Fan | `\unsure{Les deux théorèmes} \illegible{1}` | `~~Le[s] de R… T…~~` | MW | yes | low |
| 049 | l. 1 | `défini par (5).` | `(3).` | MS | no | medium |
| 049 | l. 1 and ll. 5–9 | — | two vertical margin bars | OM | no | low |
| 049 | l. 3 | `est donc un espace` | one word beginning with d before `un` | OT | no | low |
| 049 | "(formule (2))" | `(2)` | a single curved stroke, not clearly 2 | MS | no | low |
| 049 | "résulte en effet" | `\unsure{résulte} en effet` | an interlinear line, with a first word (qui?) before *résulte*, above the struck `qui résulte aussitôt de` | OM | partly | low |
| 049 | end of l. 6 | — | a short token after `orthonormale` | OM | no | low |
| 049 | start of the "montrons" line | — | a double-struck word, unless it is in `\illegible{2}` | OM | no | low |

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004 | 1, early | 2.5 | 218 | 0 | 0 | 1 | 0 | 4 | 0 | 5 | 2.29 | 5 | 0 |
| 012 | 1, late | 4.5 | 262 | 2 | 0 | 0 | 0 | 0 | 1 | 3 | 1.15 | 1 | 4 |
| 015 | 2, early | 1.4 | 148 | 2 | 1 | 0 | 0 | 2 | 0 | 5 | 3.38 | 2 | 5 |
| 024 | 2, late | 5.3 | 152 (+82 not scored) | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.66 | 0 | 1 |
| 027 | 3, early | 2.5 | 141 | 1 | 2 | 1 | 0 | 0 | 1 | 5 | 3.55 | 3 | 3 |
| 035 | 3, late | 7.3 | 205 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0.98 | 1 | 4 |
| 039 | 4, early | 2.0 | 213 | 1 | 3 | 2 | 0 | 1 | 0 | 7 | 3.29 | 6 | 4 |
| 049 | 4, late | 1.5 | 187 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0.53 | 1 | 6 |
| **All** | | | **1526** | **7** | **7** | **5** | **0** | **7** | **3** | **29** | **1.90** | **19** | **27** |

Minutes on page: the gap between this page's "done" line in `progress.log` and the previous page of the same stream.

Overall: 1.90 errors per 100 words (one in 53 words); 1.25 unmarked errors per 100 words (one in 80); misread
words and symbols alone, 0.92 per 100 words (one in 109). Ten of the 29 errors carry a doubt mark: the same third
that the prompt reported for earlier work. Most unmarked errors are of four sorts: struck words given as live text
(four struck *tout*, two of them rendered as ∀; *hermitien*), wrong letters in subscripts and equation numbers
(E_n for F_n three times on scan 039, (5) for (3)), expanded abbreviations (*mb.* → *membre*), and short tokens left
out (*donc*, *vt.*, a pair of parentheses, `λ₁(u), ———`).

## Early versus late, per stream

| Stream | Early page | Errors / 100 words (unmarked) | Late page | Errors / 100 words (unmarked) |
|---|---|---|---|---|
| 1 (003–013) | 004, 2.5 min | 2.29 (2.29) | 012, 4.5 min | 1.15 (0.38) |
| 2 (014–025) | 015, 1.4 min | 3.38 (1.35) | 024, 5.3 min | 0.66 (0) |
| 3 (026–036) | 027, 2.5 min | 3.55 (2.13) | 035, 7.3 min | 0.98 (0.49) |
| 4 (038–050) | 039, 2.0 min | 3.29 (2.82) | 049, 1.5 min | 0.53 (0.53) |
| All | 720 words | 3.06 (2.22) | 806 words | 0.87 (0.37) |

In every stream the late page is better than the early one. The early pages are each stream's second page, finished
within five and a half minutes of the start, in 1.4–2.5 minutes each; three of the four late pages took 4.5–7.3
minutes.
Accuracy did not decline over the run. The errors cluster on the pages that were done fastest. Page difficulty is a
possible confound: 049, the one fast late page, is mostly prose and is clean.

## Doubt-mark calibration

The eight first-pass pages carry 226 `\unsure` marks (32 of them with an alternative) and 14 `\illegible` marks
(27 words).

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 58 | 84 % |
| First reading wrong, an alternative right | 4 | 6 % |
| Wrong both ways | 7 | 10 % |
| Not decidable from the scan | 157 | — |

- Of the 13 decided marks with an alternative, 9 had the first reading right and 4 the alternative right; none was
  wrong both ways. All 7 wrong-both-ways marks are single readings: 015 *compact* (two other words), 024
  *Définition de* (begins with R), 027 *∈ b* (two words) and *C₀(A)* (C₀(M)), 035 *second membre* (mb.), 039
  *finies* and *du point de vue du rang* (second-hand insertion).
- Of the 157 undecidable marks, 93 sit in struck text; the other 64 are in margin notes, pencil notes and the
  hardest words.
- Marks are over-cautious on readable text (*fblt*, *puisque*, *t+0*, *équicontinu* were all right) and absent at
  most real errors: 19 of the 29 errors carry no mark.

## Completeness

Nothing larger than a token or a mark is missing. Every text block, display, boxed formula, margin note, insertion
and deletion block on the eight pages is present, and in the order of the page. The omissions are short: one word
(*donc*, 027), one abbreviation (*vt.*, 035), one pair of parentheses (004), one list start `λ₁(u), ———` (039), one
raised token (039). Among the low-confidence items, small non-verbal marks are left out: margin bars (049), an arc
that joins an insertion to its place (012), a brace and arrowed lines beside margin notes (015), a pencil link stroke
and a short vertical stroke (012). The struck passages were transcribed in full with doubt marks; they could not be
checked word by word.

## Verdict

1. Good enough as a first pass for a second pass to correct: nothing larger than a token is missing, and the error rate is 1.9 per 100 words (0.9 for misread words and symbols).
2. Two thirds of the errors carry no doubt mark, and they are the kind that changes a diplomatic text: struck words given as live text, wrong subscripts, a wrong equation number, expanded abbreviations; the second pass has to re-read every line against the scan, not only the marked places.
3. The sample points to speed, not the parallel streams: the fast early pages have 3.1 errors per 100 words against 0.9 on the late pages, with no decline over the run; larger packages are safe if the minutes per page do not shrink.
