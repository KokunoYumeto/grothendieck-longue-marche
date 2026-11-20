# Scan 008 — independent C-reader audit

Started **2026-11-20 11:21:15 UTC**, before reading the brief and packet. This reader is the independently assigned **C-reader**, not witness C. H contains no text: all report rows have `H=null` and `diff_H=false`.

## Visual coverage and method

The whole image was viewed **once**, half a **once**, and half b **once**, in that order. Every visible text line and written feature was compared with C. Ten tight crops were then made once, enlarged to 2,800 pixels across with LANCZOS, autocontrast and mild sharpening, and viewed once each. Every target was already upright; rotation is zero. No whole half was enlarged. No crop was remade. No OCR, internet, other page, other reader file, or delegation was used.

Whole dimensions: 1404 × 1721; half a: 1404 × 940; half b: 1404 × 941. Crops use original full-scan coordinates. Evidence using the supplied halves is expressly labelled with that half's own coordinate origin. An exact pixel comparison to nominal crops failed; the half-specific boxes are consequently left as half coordinates rather than silently converted.

## Line-by-line audit

| Location | Reading audit | Evidence and remaining doubt |
| --- | --- | --- |
| Top line | `Supposons que qα−α′≠0 alors` | Each word, prime, subtraction and nonzero sign read on half a. No terminal punctuation supplied. |
| First expansion | `(1)⇒p∣Σ C_q^i a^i b′^(q−i−1)+b′^(q−1)` | Half a: sum lower `i=1`, upper `q−1`; dotted raised i; lower q on C; prime on both b terms. |
| Second implication | `⇒p∣q a^(q−1) car p∣b′ et pour i≠q−1 q−i−1 [cancelled ≠0]>0` | Half a and crop 01. The cancelled sign retains two bars and crossing; its zero is rounded. C retained. |
| `or` line | `or p∣b′ et b′∣b^q donc b′ bowl-1 a donc p bowl-1 a` | Every relation and lower 1 checked on half a. |
| Isolated cancelled line | `donc si p≠1` / `donc si p≠q` | Crop 02: **retained doubt**. The narrow final upright favours 1, but crossings obscure its upper and right outline. |
| Next implication | `(1)⇒p∣q donc [p=1 ou] p=q (si qα−α′≠0)` | Half a: deleted `p=1 ou` followed by live `p=q`; complete round parenthesis. |
| `Donc si` line | `Donc si p≠q p premier`, inserted `ou p=1`, `et p∣b′ alors α′=qα` | Half a: insertion sits beneath `p premier`, with a small attachment mark. |
| Cancelled parenthesis | `(on l'impose sans risque si p=1)` | Half a: all words readable; two physical lines and **two distinct oblique strikes** retained with explicit paths. |
| First existential line | `Donc ∃b₀∈ℕ* et ∃γ∈ℕ tel que b′=q^γ b₀^q` | Half a: doubled N, raised star, lower zeros, gamma and exponents checked. Right margin `q∤b₀` retained. |
| Above fold | `de plus b₀∣b et si b=b₀b″ alors b₀ bowl-1 b″ ?` | Half a: both double-prime groups and final question mark read. |
| First line below fold | `De même ∃a₀∈ℕ* et ∃ζ∈ℕ tel que a′=q^ζ a₀^q` | Crop 03: **ζ/δ doubt retained** at first occurrence; same leading candidate used for recurrences. |
| Following line | `avec a₀∣a et si a=a₀a″ alors a₀ bowl-1 a″ ?` | Half b: lower zeros, both double-prime groups and question mark read. |
| Coprimality chain | `or a bowl-1 b ⇒ a′_[cancelled 0?] bowl-1 b′ ⇒ ζ×γ=0 (et aussi a₀ bowl-1 b₀)` | Half b and crop 04. The small black patch is **still a doubtful 0**; no alternative mathematical glyph is established. |
| Assumption line | `Je suppose désormais que ζ=0 donc a′=a₀^q` | Half b: acute on `désormais`; first-candidate ζ recurrence retained without a repeated doubt macro. |
| `Donc` formula | `c=b+a₀^q=a+q^γb₀^q` | Half b: all terms and exponents read. No algebraic check performed. |
| Numerical example | `pour q=2 on a, a₀=b₀=1, γ=1, b=4, a=3, c=5` | Half b: commas and every numeral read; top, left, bottom frame sides present, right open. C's checked three-sided drawing retained. |
| Ruled hypothesis | `Je fais l'hypothése suivante si q premier et 1≤i<q alors q∣C_q^i` | Half b and crop 09: acute accent established independently; both long rules preserved. |
| Lower condition | `alors Si q≥3 et qα−α′≥2 [alors?] on a` | Half b and crop 05: comparison strokes retained. **Cancelled alors remains doubtful**. |
| Pale addition | `p=q, a′=γ` / `p=q, α′=γ` | Crop 05: **a/α doubt retained**. Two separate curved strokes follow q; an extra lower comma-shaped candidate is preserved with unresolved role and hand. |
| First lower implication | `(1)⇒[p²?/p?] q²∣q a^(q−1) [ou p=1]` | Crop 06: **cancelled p²/p doubt retained**. Crop 07: the latter cancelled words are readable, with a lower returning stroke explicitly drawn. |
| Second lower implication | `⇒q∣a^(q−1) [ou p=1⇒p=1]` | Crop 07: words, equalities and implication read. The long cancellation rises rightward. Pale `absurde car q∤a` is placed above its cancelled continuation. |
| Faint interline traces | Residual curved strokes and points above the right end of the lower implications | Crop 07: no secure character, word, or cancellation target. A small gray drawing preserves the traces without such reconstruction. |
| Final line | `Donc γ=0 ou γ=[cancelled q]` with `qα−1` raised above/right, followed by `(sous réserve que l'hypothése est vraie)` | Crop 08: the actual C cancelled-q doubt is **resolved**. The q loop and descender, raised qα−1, and repeated diagonal returns are visible. Crop 10: acute in the final `hypothése` separately established. No chronology or algebraic completion asserted. |
| Lower-right note | `C'est peut-être interessant car ici 2 est mis à part dans l'ensemble des nombres premiers` | Half b: exact spelling retained; no acute over the first e of `interessant`. Return arrow points back to this note. A detached point at the lower arrow start is retained. |
| Lower-left archive number | `7` | Half b; recorded only as `% archive sheet number: 7`. |

## Actual C doubt accounting

The source classification received from the root identifies **seven** actual `Doubtful readings` rows. The earlier six entries are notation; the last `interessant` and `hypothése` entries are retained spellings, not doubt rows.

| Original locus | Report row | Decision |
| --- | --- | --- |
| First isolated struck line | 008-C-01 | Retained `p≠1 / p≠q` |
| Second existential line | 008-C-02 | Retained `ζ / δ` |
| Before second bowl in `or a…` | 008-C-03 | Retained cancelled candidate `0` |
| Above last two implications | 008-C-04 | Retained cancelled candidate `alors` |
| After `(1)⇒` in lower left | 008-C-05 | Retained cancelled `p² / p` |
| End of final line | 008-C-06 | Resolved lower cancelled `q` and uncrossed raised `qα−1`; no algebraic interpretation |
| Lower line, pale addition | 008-C-07 | Retained `a / α` |

**Six retained; one resolved.** The report has 15 rows, including nine `diff_C=true` rows. Those consist of the resolved actual C doubt, an extra detached comma-shaped mark, omitted faint residual traces, the lower insertion's placement, and physical details of cancellation/arrow drawings. No primary lexical or mathematical-symbol candidate in C has been silently replaced. The mathematical check-event list is empty: no arithmetic or proof verification was performed.

## Crop record

| File | Full-scan box `(x0,y0,x1,y1)` | Target |
| --- | --- | --- |
| 01_top_cancelled_neq0.png | (1114,198,1389,280) | Cancelled nonzero before `>0` |
| 02_struck_donc_si.png | (94,375,483,455) | Whole isolated cancelled line |
| 03_zeta_forms.png | (548,879,1167,981) | Initial ζ/δ and raised recurrence |
| 04_cancelled_subscript.png | (449,1044,723,1139) | Small cancelled subscript |
| 05_lower_alors_and_pale.png | (545,1378,1005,1467) | Cancelled alors, pale a/α, two curved marks |
| 06_cancelled_p_power.png | (98,1446,551,1540) | Cancelled p²/p |
| 07_lower_cancellations.png | (452,1452,837,1589) | Lower cancellations, pale insertion, residual traces |
| 08_final_cancelled_q.png | (518,1576,733,1699) | Final lower q, raised entry and returning strikes |
| 09_first_hypothese.png | (226,1324,613,1403) | First acute in hypothése |
| 10_final_hypothese.png | (1019,1585,1345,1686) | Final acute, closing parenthesis and arrow-start point |

The full target height and endpoint space are retained in these crops. Neighbouring line fragments sometimes enter a crop edge, but no target letter, descender or cancellation stroke identified for that crop is clipped. The complete right return arrow was settled from half b; crop 10 contains only its lower starting point and was not used to infer the unseen remainder.

## Source consistency check

The current TeX and report decisions were read together. Braces, dollar delimiters, paired TikZ environments, crop filenames, C-doubt mappings, and H-null fields passed structural checks. A control-character typo was repaired. A pdfLaTeX compile was attempted, but the environment lacks pdflatex.fmt; no render check is claimed. This technical check adds no mathematical check-event.

Finished **2026-11-20 11:34:58 UTC**.
