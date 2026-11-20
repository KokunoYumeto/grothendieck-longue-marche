# Independent reading audit — scan 007, reader C

## Scope and viewing record

Start recorded at **2026-11-20 11:08:19 UTC**, after reading the reader brief and before reading the packet or any image. Read only the assigned scan 007 packet, supplied notation snapshot, PREAMBLE.tex, brief, and crop helper. Witness H has status `nothing`; there is no H text to collate.

Viewed the whole image once, then supplied half a once and half b once. The original image is 1405 × 1720; both halves are 1405 × 940. Half a has full-scan origin (0, 0), and half b has full-scan origin (0, 780). Made six local crops, then viewed each exactly once. No OCR, internet, other page, other reader, or root decision was consulted. No crop was repeated.

## Line-by-line visual audit

| Locus | Ink reading and audit |
| --- | --- |
| Opening patch, before Soit | Dense black cancellation over a short unidentified item. The enlargement exposes overlapping loops and strokes but no recoverable character sequence. Retain `\deleted{\illegible{1}}`; the uncertainty persists. |
| First line | `Soit a∈ℕ*, b∈ℕ*, c∈ℕ*, q∈ℕ*` followed by `q nombre premier (q≠1)`. Doubled left strokes of N and raised star marks are visible. Commas separate the first four entries. C retained. |
| Second line | `On suppose que` with the three pairwise signs, then `(premiers entre eux deux à deux)`. Each sign has a shallow bowl and a small separate hooked 1 below. C retained. |
| Interlinear insertion at left | `et a^q+b^q=c^q`. All three raised q letters and both equality bars are readable; preserve the interlinear placement as insertion. |
| Next prose line | `On a c>a et c>b car a∈ℕ* et b∈ℕ*`. The two comparisons and both stars are visible. C retained. |
| On pose line | `On pose c=a+b′=b+a′ avec b′∈ℕ* et a′∈ℕ*`. Prime strokes are separate from the bases. C retained. |
| Expansion, first line | `alors a^q+b^q=c^q=(a+b′)^q=Σ C_q^i a^i b′^(q−i) (Newton)` with lower limit i=0 and upper q. Each index and the final parenthesis were read. C retained. |
| Expansion, second line | `=b′^q+Σ C_q^i a^i b′^(q−i)+a^q (car q≥2)` with lower i=1 and upper q−1. Crop 02 shows the main angle and a separate oblique lower comparison stroke; retain `\geqslant`. |
| Numbered display | `donc b^q=Σ C_q^i a^i b′^(q−i)+b′^q (1)`, lower i=1, upper q−1. Crop 03 identifies the small mark left below the sum as the dot of the lower-limit i; no additional independent character is supplied. |
| Factor prose, first physical line | `la puissance de b′ n'étant jamais nulle on peut mettre b′`. The accent in n'étant and both primes are visible. |
| Factor prose, second physical line | `en facteur dans le second membre de (1), donc b′|b^q`. Preserve the comma after (1). |
| Factor prose, third physical line | `(b′ divise b^q)`; both parentheses readable, no terminal full stop. |
| Prime introduction | `Soit p un nombre premier ou p=1 et tel que :`. Two long rising strokes cancel `ou p=1`; retain the readable cancelled words with the deletion macro. |
| Next line | `p|b′ donc p|b. Soit α∈ℕ* et α′∈ℕ* tels que`. The full stop before Soit and the prime of α′ are visible. |
| Divisibility pair 1 | `p^(α′)|b′ et p^(α′+1)∤b′`. Both b primes and the slash across the second divisibility stroke are visible. |
| Divisibility pair 2 | `et p^α|b et p^(α+1)∤b`. C retained. |
| Pale note, first line | `a/α n'exist/n'existe pas si`. Crop 04 retains both original doubts: the first oval and falling tail allow a and α; the tall terminal stroke and short rightward continuation leave the final e question open. Primary readings remain a and n'exist. |
| Pale note, second line | `on avait p=1`. All characters readable. The note's hand remains undetermined. |
| Right-hand prose | `On a α′≤qα car b′|b^q`. The extra lower oblique stroke in ≤, both alpha letters, and b′ are visible. |
| First implication | `(1)⇒p^(qα)|Σ C_q^i a^i b′^(q−i)+b′^q`, lower i=1, upper q−1. Both arrow bars and arrowhead are present. C retained. |
| Second implication | `⇒p^(qα)|b′(Σ C_q^i a^i b′^(q−i−1)+b′^(q−1)) (car q≥2)`. The subtraction strokes, both endpoint parentheses, and comparison stroke were read. |
| Posons line | `posons b′=p^(α′)b″ donc b″` followed by the bowl/1 sign and `p (propriété de α′)`. Double primes, the accent in propriété, and α′ are visible. |
| Final chain, first row | `⇒p^(qα)|p^(α′)b″(Σ C_q^i a^i b′^(q−i−1)+b′^(q−1))`, lower i=1, upper q−1. C retained. |
| Final chain, second row | `⇒p^(qα−α′)|b″(Σ C_q^i a^i b′^(q−i−1)+b′^(q−1)) car qα≥α′`. Crop 05 confirms the crowded indices and the dotted i below the sum. The two minus strokes in q−i−1 remain visible. |
| Final chain, third row | `⇒p^(qα−α′)|Σ C_q^i a^i b′^(q−i−1)+b′^(q−1) car b″` followed by the bowl/1 sign and p. Crop 06 identifies the apparent detached mark above a as the dot of its raised i; the lower sum-limit dot and stem are both present. |
| Lower-left archive numeral | Pencil 6, retained only as `% archive sheet number: 6`. |

## Collation outcome

No reading change from C is proposed. The report has three entries for the three unique original doubtful loci, all retained with `diff_C=false`. The duplicate n'exist uncertainty-table row refers to the same marginal locus. H supplies no full text, so all H fields are null and all `diff_H` values are false.

All written material visible in the supplied images is represented in reading.tex. This page contains text, displays, one interlinear insertion, two cancelled items, a pale marginal note, and the archive number. No independent diagram or drawing was found. Ordinary cancellation strokes are encoded by `\deleted`; no new geometric reconstruction was introduced.

The source has no written title, date, or manuscript pagination. No explicit authorial words of uncertainty were found. The pale note reads, with its two unresolved places, `a/α n'exist/n'existe pas si on avait p=1`.

## Crops and limits

All coordinates below are on the original full scan. Autocontrast, LANCZOS enlargement, and a light unsharp mask were used; rotation was zero throughout.

| Crop | Bounds | Purpose |
| --- | --- | --- |
| 01_top_cancel.png | (22,18)–(180,94) | Complete initial black cancellation, adjoining Soit |
| 02_upper_comparison.png | (929,408)–(1212,515) | Complete upper `(car q≥2)` |
| 03_numbered_sum.png | (271,521)–(958,632) | Complete numbered formula and indices |
| 04_pale_note.png | (1006,961)–(1326,1053) | Complete pale two-line note |
| 05_crowded_sum.png | (395,1487)–(991,1590) | Penultimate row from divisibility stroke through closing parenthesis |
| 06_final_sum.png | (235,1574)–(1184,1673) | Final expression through right-hand p |

Crops 05 and 06 intersect incidental fragments of adjoining lines; their intended formula loci retain their complete ink bounds. Crop 04 includes the whole pale note and incidental tips of darker neighboring writing. No interpretation depends on those clipped neighboring fragments.

No mathematical computation or proof verification was performed. The audit records reading of the written statements, glyphs, and placement only; `check_events` is empty.
