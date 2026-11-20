# Scan 007 — independent reader B

## Scope and viewing record

Start: **2026-11-20 11:08:02 UTC**, recorded before reading the brief and packet. I read the full v06 brief; metadata, C, the empty H file, C doubts, C notes, C inventory, notation snapshot, and PREAMBLE. H has status `nothing`; there are no H collation differences.

I viewed the full source **once**, supplied half **a once**, and supplied half **b once**, in that order. I made **three** tight enlarged crops and viewed **each once**. I read the page line by line against C. I used no other reader, other page image, OCR, recognition output, or internet source. No algebraic/proof check was performed; `check_events` is empty.

The original measures 1405×1720. Each half measures 1405×940. Half a has origin (0,0); half b has origin (0,780), giving 160 pixels of overlap. Coordinates below refer to the full original image.

## Line-by-line audit

| Locus | Reading and visual audit |
| --- | --- |
| Top-left patch, y≈24–64 | A dense overwritten black unit before **Soit**. Internal loops remain unreadable in crop 01. Retained `\deleted{\illegible{1}}`; original C doubt remains open. |
| Top line, y≈28–89 | **Soit** followed by `a∈ℕ*, b∈ℕ*, c∈ℕ*, q∈ℕ*`; at right **q nombre premier (q≠1)**. Commas, raised stars, doubled N strokes, inequality cross-stroke, and closing parenthesis read. Agrees with C. |
| Second main line, y≈94–167 | **On suppose que** followed by the three pairs `a`/`b`, `a`/`c`, `b`/`c`, each with the shallow bowl and small hooked 1 underneath. The explanation is **(premiers entre eux deux à deux)**, physically wrapped within its parentheses. Agrees with C. |
| Interlinear left insertion, y≈152–204 | **et a^q+b^q=c^q**. The three powers q and both equality strokes are visible; retained as the insertion belonging to the hypotheses. |
| Next main line, y≈190–237 | **On a c>a et c>b car a∈ℕ* et b∈ℕ***. Both greater-than signs are plain > here. Agrees with C. |
| Definition line, y≈262–332 | **On pose c=a+b′=b+a′ avec b′∈ℕ* et a′∈ℕ***. Single raised primes on the two new variables; both equalities and both stars read. Agrees with C. |
| First expansion row, y≈325–421 | **alors a^q+b^q=c^q=(a+b′)^q=Σ C_q^i a^i b′^{q−i} (Newton)**. Sum bounds are lower `i=0`, upper `q`. Both parentheses around the binomial and the Newton label are visible. Agrees with C. |
| Second expansion row, y≈416–524 | **=b′^q+Σ C_q^i a^i b′^{q−i}+a^q (car q≥2)**. Sum bounds lower `i=1`, upper `q−1`; an extra lower stroke accompanies the > in ≥. Agrees with C. |
| Numbered row, y≈533–625 | **donc b^q=Σ C_q^i a^i b′^{q−i}+b′^q (1)**. Same bounds `i=1` to `q−1`; label (1) has both curved delimiters. Agrees with C. |
| Prose line 1, y≈632–695 | **la puissance de b′ n’étant jamais nulle on peut mettre b′**. The apostrophe and accent in n’étant are retained; both b primes read. Agrees with C. |
| Prose line 2, y≈691–766 | **en facteur dans le second membre de (1), donc b′\|b^q**. Comma after (1), single upright divisibility mark, and q power read. Agrees with C. |
| Prose line 3, y≈773–840 | **(b′ divise b^q)**. Parentheses enclose the whole explanation. Agrees with C. |
| Soit p line, y≈824–917 | **Soit p un nombre premier**, cancelled **ou p=1**, **et tel que :**. The cancellation has a dark rising diagonal and a thinner nearly parallel lower stroke. C already marks the correct words as deleted; the two visible strokes are reproduced explicitly in TikZ. This is the one added physical-detail difference, B007-D04. |
| Next line, y≈917–982 | **p\|b′ donc p\|b. Soit α∈ℕ* et α′∈ℕ* tels que**. Dot after b; separate prime on the second alpha; both N stars read. Agrees with C. |
| First divisibility-pair row, y≈985–1065 | **p^{α′}\|b′ et p^{α′+1}∤b′**. Separate prime on α and both b’s. The right relation consists of a slashed upright. Agrees with C. |
| Pale note, y≈972–1046 | **a/α n’exist/n’existe pas si on avait p=1**. Crop 02 contains the whole note. First sign has a small loop and a down-right tail; a/alpha remains open. The final curved return of the word after it does not isolate a separate e; both original candidates remain. `pas si on avait p=1` is readable. Hand attribution remains undetermined. |
| Second divisibility-pair row, y≈1067–1141 | **et p^α\|b et p^{α+1}∤b**. Unprimed b in both positions; plus 1 is raised with alpha. Agrees with C. |
| Right-side statement, y≈1049–1125 | **On a α′≤qα car b′\|b^q**. Prime on the left alpha; lower stroke in ≤; b prime and raised q at the right. Agrees with C. |
| First implication row, y≈1156–1259 | **(1)⇒p^{qα}\|Σ C_q^i a^i b′^{q−i}+b′^q**. Bounds `i=1` to `q−1`; p exponent qα; no surrounding parenthesis on this sum. Agrees with C. |
| Second implication row, y≈1231–1350 | **⇒p^{qα}\|b′(Σ C_q^i a^i b′^{q−i−1}+b′^{q−1}) (car q≥2)**. Both minus signs in the summand exponent and the closing parenthesis read. Agrees with C. |
| Posons line, y≈1323–1424 | **posons b′=p^{α′}b″ donc b″** bowl-with-1 **p (propriété de α′)**. Double primes on both b’s; prime on both alphas; acute accents in propriété. Agrees with C. |
| Third implication row, y≈1413–1519 | **⇒p^{qα}\|p^{α′}b″(Σ C_q^i a^i b′^{q−i−1}+b′^{q−1})**. Distinct p factors and both primes; bounds and end parenthesis read in half b. Agrees with C. |
| Penultimate implication row, y≈1503–1590 | **⇒p^{qα−α′}\|b″(Σ C_q^i a^i b′^{q−i−1}+b′^{q−1}) car qα≥α′**. Crop 03 settles the crowded central sum bounds and exponents: upper q−1, lower i=1, summand q−i−1, terminal q−1. The right car explanation was read in half b. Agrees with C. |
| Last implication row, y≈1583–1665 | **⇒p^{qα−α′}\|Σ C_q^i a^i b′^{q−i−1}+b′^{q−1} car b″** bowl-with-1 **p**. Crop 03 shows the final summation bounds and both minus signs in q−i−1. The absence of surrounding parentheses here follows the ink. The right explanation was read in half b. Agrees with C. |
| Bottom-left corner, y≈1657–1698 | Pale archive numeral **6**; preserved only as `% archive sheet number: 6`. No title or date read. |

## Crop record

| Crop | Full-scan box | Purpose and result |
| --- | --- | --- |
| `crops/01_initial_deletion.png` | (24,15)–(174,88) | Whole blacked-out unit plus **Soit**; original unreadability retained. Width 2400, rotation 0. |
| `crops/02_pale_note.png` | (998,964)–(1325,1052) | Both adjoining original C doubts with the complete two-line note; both doubts retained. Width 3100, rotation 0. |
| `crops/03_final_two_sums.png` | (232,1496)–(960,1661) | Crowded final-two-row bounds, primes, and exponents; C readings retained after visual settlement. Width 3300, rotation 0. |

Each crop used the supplied PIL LANCZOS/autocontrast/sharpening helper and was viewed. Crop 03 includes clipped fragments of the preceding row above its target and the beginning of the final **car** at the right. Both target sum rows are retained completely. The full preceding row and right-side **car** explanations were read on half b. There was no recropping.

## Differences and remaining doubt

The wording, formulas, punctuation, insertion, and deletion state agree with C. One physical detail is newly explicit: the two nearly parallel rising cancellation strokes over **ou p=1** (B007-D04). The semantic `\deleted` macro is retained; its generic horizontal rule is suppressed locally, and the actual pair is drawn in TikZ.

All three original C uncertainty loci are recorded: the unreadable initial cancellation, `a|α`, and `n’exist|n’existe`. The repeated n’exist row in C_doubts is the same physical locus and has one decision, B007-D03. None has been promoted to certainty. `report.json` sets these three rows to `C_doubt_status=retained` and `diff_C=false`; the paired-stroke detail has `diff_C=true`. All H fields are null with `diff_H=false`.
