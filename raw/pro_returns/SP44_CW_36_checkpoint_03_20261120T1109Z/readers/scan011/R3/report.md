# Scan 011 — independent reader R3

Start (UTC): 2026-11-20T09:14:10Z  
End (UTC): 2026-11-20T09:23:08Z

## Scope and visual record

I read the assigned brief v02, the exact `PREAMBLE.tex`, packet, both witness files, and the frozen page-local notation table. I accessed only scan 011 and my R3 crop/output directory. No OCR, text-recognition service, web source, published transcription, other page, or other reader was used.

The actual image sequence was whole once for layout, half a once, half b once, then eight distinct tight enlargements, each viewed once. The whole page is 1684 × 2152 pixels; the two supplied overlapping halves are each 1684 × 1156. I did not reopen or enlarge a full half. All crops used the supplied helper with reader R3, autocontrast, LANCZOS to 2400 pixels wide, and modest UnsharpMask(1,110,3); no rotation was required. Exact filenames, source bounding boxes and operation timestamps are in `result.json` → `crops`.

| Crop | Whole-image bounding box |
|---|---|
| `crops/scan011/R3/first_coefficient.jpg` | `[775, 202, 1010, 342]` |
| `crops/scan011/R3/first_cohomology.jpg` | `[540, 558, 875, 706]` |
| `crops/scan011/R3/section_subscripts.jpg` | `[1070, 640, 1608, 772]` |
| `crops/scan011/R3/correspondence_coefficient.jpg` | `[560, 985, 995, 1122]` |
| `crops/scan011/R3/nulle_right_edge.jpg` | `[1490, 1270, 1670, 1415]` |
| `crops/scan011/R3/codimension_relation.jpg` | `[1145, 1270, 1400, 1410]` |
| `crops/scan011/R3/final_cohomology.jpg` | `[585, 1480, 895, 1613]` |
| `crops/scan011/R3/final_overtyping.jpg` | `[1410, 1780, 1630, 1970]` |

## Complete coverage

Each row below records an actual pass against both C and H, including ordinary words, punctuation and apparently agreed glyphs. D01–D05 are the five displays; L01–L21 are physical prose lines, not editorial paragraph numbers.

| Line/block | Source span | Check |
|---|---|---|
| L01 | localisation étale … homomorphisme | All words, accent, comma; page starts mid-sentence. |
| D01 | a′ ↦ Z(a′) … F_Y, | All symbols and ink layers checked; coefficient unresolved. |
| L02 | et par suite … pour les | encore noté par Z; ordinary H^1; empty second argument. |
| L03 | drux membres. | Literal r, full stop. |
| L04 | Nous allons appliquer … relative C | Indented paragraph; où, Y′, C. |
| L05 | sur S, m′=2, x′ … cohomologie | Both primes, equality, commas. |
| D02 | x′ ∈ H²(C, Z_(χ|ℓ)(1)) | Pen 2 and membership; single underlined Z; crossed subscript. |
| L06 | défini par un diviseur … t_o | No final e on défini; both section occurrences and où checked; o|0 retained. |
| L07 | sont deux sections … connexes | S., Supposant C à fibres géométriques connexes. |
| L08 | on voit donc … aussi bien | x′, primitif., opening (NB. |
| L09 | n’importe quel diviseur … pour Z | degré relatif nul.); closing parenthesis present. |
| L10 | la classe de cohomologie | No terminal punctuation. |
| D03 | Z ∈ H^(2n)(Y x_S C, Z_χ(n)) | Capital Z, 2n, baseline x and lowered S, coefficient and parentheses. |
| L11 | associée à un cycle … notera | accents, x_S product, codimension n, comma and apostrophe. |
| L12 | aussi Z. (NB pour que … définie | Capital Science is on next line; opening NB retained. |
| L13 | en l’état actuel … restrictives | Science, il faut; all words and accents. |
| L14 | genre S de type fini … nulle | Both S, comma, excellent, characteristic word; final e clipped. |
| L15 | ou le dycle Z … fibre par fibre | dycle, double typewriter quotes, i.e., handwritten ≤, no secure stop/closure. |
| L16 | Sous ces conditions, x … cohomologie | Normal line spacing and unindented start; no added paragraph. |
| D04 | x ∈ H^(2n)(Y, Z_χ(n)) | All degree, coefficient, twist, membership and parentheses. |
| L17 | associée au cycle algébrique | Both accents and no terminal punctuation. |
| D05 | z = Z(t_1) − Z(t_o) | Lowercase z, uppercase Z, indices and subtraction; round subscript follows first uncertainty. |
| L18 | sur Y. (NB on suppose … qu’on | Opening NB, écrites, sens, comma and apostrophe. |
| L19 | travaille avec des classes … - ce | Single underline beneath classes; façon; qu’elles; single hyphen. |
| L20 | dernier cas supposant … que[overtyping] S | Inner parenthesis closes after Science; accent and two cancelled cells uncertain. |
| L21 | est de type fini sur un corps. | Full stop; no outer closing parenthesis. |
| numbers/margins | 2 top right; 10 bottom left | No diagram, drawing, independent marginal prose, or caret-led insertion; incidental edge traces not assigned authorial content. |

## Collation and principal decisions

`result.json` contains the complete 27-row collation (7 rows against C; 17 against H; 20 C-doubt or C-audit rows). Each row preserves C and H readings, the reading adopted here, specific ink observations, evidence and crop/region box. It also contains the full 30-entry inventory, notation additions, abbreviations and unresolved list. No separate handwriting-wrapper omission in H is counted as a reading error.

The first coefficient remains an explicit six-candidate alphabet/typeface doubt. My nearest literal candidate is an ordinary E with overlapping strokes; I do not claim that C’s candidate set is wrong. A clean F cannot be obtained simply by comparison with the target.

The three underlined integer coefficients have ordinary single Z forms and separate lower rules. Their subscripts repeat a mechanical crossed shape with an upper hook, long diagonal and lower foot. I retain `χ|ℓ` on the first occurrence and χ thereafter; I do not assign these subscripts to handwriting. The H² exponent 2 and membership signs are separate filled pen forms. H and R themselves are ordinary serifed capitals.

The lowered round section label is visibly the same short o-shaped glyph as prose o. I therefore retain `o|0` at the first occurrence, then use o consistently at the remaining two occurrences. This records literal uncertainty rather than asserting a different mathematical section. The source’s typed product is baseline x with lowered S; quotes around relatif are typewriter double marks.

The ordinary prose preserves **drux**, **défini**, and **dycle**. The final e of **nulle** remains clipped. The nearly vertical mark above the final live e and the two subsequent machine-overstruck character cells remain `què|qué|que` and deleted `ax|xx`. The single underline under classes and the single typed hyphen before ce are retained. No period after fibre par fibre or missing outer NB parenthesis is supplied. I retain only a source newline before Sous because there is no blank line or indentation; intended paragraphing there remains a medium-confidence issue.

The handwriting inventory distinguishes the typed letters from their pen-filled signs or underline rules. The mechanism of the Z underlines is not asserted. No caret-led insertion, independent marginal prose note, diagram, or drawing occurs. Page 2 is at top right; archive 10 is recorded only in a comment. Irregular edge traces are not promoted to authorial notation.

## Mathematical reading and performed check

The page states that the correspondence map on direct images induces a map on H¹(S, ). It specializes Y′ to a relative curve C with m′=2 and takes x′ to be the degree-2, twist-1 class of a difference of sections. With geometrically connected fibres it calls x′ primitive, and permits any relative divisor of relative degree zero. It then uses a codimension-n correspondence cycle Z on Y x_S C and identifies the resulting degree-2n, twist-n class x with the cycle z=Z(t₁)−Z(tₒ), subject to the recorded uncertainties in the literal coefficient and section glyphs.

The page itself qualifies the construction: “pour que cette classe de cohomologie soit vraiment définie en l’état actuel de la Science, il faut faire des hypothèses restrictives”, and later “on suppose que les intersections écrites ont un sens”. These reservations remain in the transcription. The fibrewise codimension sign visibly points **≤ n**; its direction is not changed by a mathematical expectation. The exact status of the listed hypotheses, cycle class construction, intersection product and general primitivity claim was not proved by this reading.

One actual mathematical check was performed, classified **computation or formal certificate** with **no formal certificate**: conditionally, if each given section meets a geometric fibre as one reduced degree-one point, the degree of their difference is 1−1=0. This is only a local arithmetic check. It does not add unstated smoothness/properness hypotheses, establish the author’s meaning of primitive, or prove any construction on the page. The assumptions and limits are recorded in the sole `check_events` entry.

## Remaining doubts and brief feedback

The unresolved list contains the first coefficient capital, χ/ℓ literal subscript, o/0 section subscript, clipped nulle, final live accent, deleted two-character string, and paragraph interpretation before Sous. Each visual doubt received the single indicated enlargement; the paragraph issue was settled only provisionally from the half’s layout. No candidate was supplied solely by the mathematics.

The v02 brief is workable. A future clarification could specify treatment of literal typewriter o used as a possible substitute for zero, and whether an unindented start at normal line spacing is to count as a new paragraph without additional layout evidence. The exact permitted check-event type and the exception for merely missing handwriting wrappers were followed.
