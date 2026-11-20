# Scan 028 — independent reader C

- **Identity:** model inherited; effort not exposed. This reader label C is distinct from historical witness C.
- **UTC start:** 2026-11-20T09:27:55Z.
- **UTC end:** 2026-11-20T09:36:57Z.
- **Overall confidence:** medium. The principal running text is legible; nine local readings/statuses remain qualified.
- **Inputs:** only the page-specific C/H witnesses, prior questions, supplied notation snapshot, PREAMBLE, brief, the prescribed crop helper, and the three permitted source images.

## Viewing sequence and layout

I opened `J75-04_75_scan028.jpg` **once**, then `_a.jpg` **once**, then `_b.jpg` **once**, in that order, using `view_image`. The whole image is 1686 × 2357 pixels. The halves are 1686 × 1258 and 1686 × 1259; the second starts at full-image y = 1098. Neither half was reopened or enlarged. I then made and viewed exactly one crop for each of twelve unresolved places; the parenthetical insertion and neighbouring cancellation share one crop, as do adjacent heading abbreviations and the adjacent initial-filtration issues.

The sheet contains handwritten sections b) and c), one small rightward map with a label above its arrow, four mathematical displays, a bracketed example, two raised insertions with leaders, several cancellations/overwrites, a slanted right-margin cluster, two underlined headings, a short separator, and two offset closing strokes with a small detached mark. Archive number 27 is at lower left. The remaining lower field is blank apart from incidental specks. There is no typescript, letterhead, dateline, signature, or additional manuscript page number.

## Physical-line coverage and inventory

All coordinates below refer to the full image. Every line was read against both witnesses, including their agreements. The listed insertions, deletions, leaders, and strokes are separate inventory elements in `review.json`.

| Line / vertical range | Reading event and visible content | Confidence |
|---|---|---|
| L01, y 82–177 | b) and “Contexte des familles finies de modules”; checked every word, the f and dotted i strokes in finies, and final modules. | high |
| L02, y 190–294 | quadratiques, colon, two-stroke equals-like sign, formule with comma, avec, the second two-stroke sign, and the edge-clipped final word. Crop 01 preserves the physical edge. | medium |
| L03, y 278–337 | Raised parenthesis “(surjection si on veut)”; separate long return connector enters after application. Both text and leader are inventoried. | medium |
| L04, y 340–426 | c), overwritten source I/J, map arrow directed right with p above, destination I, application, d’ens, cancellation before finis, and final comma. | medium |
| L05, y 465–573 | Full odd-fibre definition, raised minus, i ∈ I, divider, capital Card, p with exponent −1 and parenthesized dotted i, impair, closing brace and stop. Independently read the crossed phrase at the right. | medium |
| L06, y 578–723 | Opening bracket, p. ex, J, ens avec relation d’équivalence; no extra un/muni d’une. Raised script R and its descending insertion mark attach at the word ending; following comma retained. | high except insertion-edge crowding |
| L07, y 730–818 | et I = J/R, closing bracket and stop; looped script R; overwritten initial of Alors. | medium |
| L08, y 852–978 | Three omega glyphs, J and I⁻ indices, wave over one straight bar, small wedge, larger wedge with i ∈ I underneath, and the heavily inked last J/index. The tiny nested index remains 2 or i, in that order. | medium; tiny index low |
| L09, y 986–1068 | Slanted broken cluster at the right; one rotated crop gave no defensible word. Retained one illegible unit and uncertainty about its status as writing. | low |
| L10, y 1086–1188 | Compatibilités with final s and underline confined to that word; entre les; isom without a point; can. with a point; a) b) c). | medium–high |
| L11, y 1250–1260 | One short, slightly uneven separator stroke. | high |
| L12, y 1330–1410 | Cas d’extensions; apostrophe, spelling and final s checked; continuous underline spans the heading. | high |
| L13, y 1432–1533 | Braced zero, equals, first E with a qualified underlying zero/loop, its separate subscript 0, inclusions without lower bars, E₁, E₂, **two** continuation marks, inclusion, E_d = E. | medium |
| L14, y 1561–1670 | Qualified crossed On, then Définir un isom. canonique; D, é, f, abbreviation point and final word checked. | high for live text; low for deletion |
| L15, y 1696–1839 | ω_E, wave-over-bar sign, large wedge with 1 ≤ i ≤ d below, final omega and two E arguments with i and i−1 indices. The putative slash overlaps the second E’s left limb and stays qualified. | medium |
| L16, y 1901–1940 | Longer upper stroke rising slightly rightward; shorter lower stroke starting farther right; small detached dash below the upper stroke’s left end. All represented in TikZ. | high |
| L17, y 2273–2320 | Archive 27, in another unnamed hand, retained as the archive-number comment. | high |

The source-to-target map is encoded in `tikzcd`; the two independent separator/closing drawings are encoded in `tikzpicture`. Insertion leader destinations are encoded by the exact placement of the `inserted` macro. The inventory has 25 separate elements, all marked transcribed.

## Collation and C doubts

The complete witness strings, evidence, flags, and bounding boxes are in `review.json`. This table identifies every locus without duplicating the long witness passages.

| Locus | Decision / witness difference |
|---|---|
| 028C01 | Resolve C’s finies doubt from the f and dotted i strokes; H agrees. |
| 028C02 | Retain C’s full/truncated demonstration alternatives. The terminal trace reaches the page edge; H’s unqualified word and terminal point exceed the secure reading. |
| 028C03 | Resolve the underlying barred I beneath live J; H omits the overwrite. |
| 028C04 | Resolve si on veut; preserve insertion after application from the return line. H’s parenthesis is uncertain and lacks that insertion state. |
| 028C05 | Preserve d’ens without the point supplied by H. |
| 028C06 | Retain cancelled C/f alternatives before finis; H omits this form. |
| 028C07 | Preserve capital Card from the separate tall initial semicircle; H prints lowercase. |
| 028C08 | Retain qualified struck Je dis que from J, d and q remnants; H leaves the deleted phrase unread. |
| 028C09 | Preserve p. ex with a point after p only; H adds a point after ex. |
| 028C10 | Preserve J ens avec relation. H adds un and substitutes muni d’une, also punctuating ens. |
| 028C11 | Preserve the raised R as an insertion at the end of d’équivalence; H makes it ordinary running text. |
| 028C12 | Retain the qualified underlying O-like loop in Alors; H omits it. |
| 028C13 | Resolve C’s omega/w alternative to omega from the paired rounded lobes; H agrees. |
| 028C14 | Reorder C’s tiny-index alternatives to **2\|i** on the visible rounded head and hooked foot. H prints i but explicitly qualifies it in its ink-blot note. |
| 028C15 | Retain C’s illegible marginal unit; H has no corresponding item. |
| 028C16 | Preserve plural Compatibilités; H has the singular ending. |
| 028C17 | Preserve the underline under Compatibilités alone; H italicizes the complete line. |
| 028C18 | Resolve C’s heading alternatives to isom, with no detached point; H adds one. |
| 028C19 | Resolve C’s can./cas. alternatives to can. from the short n return and detached point; H agrees. |
| 028C20 | Preserve the short separator omitted by H. |
| 028C21 | Preserve the full underline under Cas d’extensions; H’s heading macro omits it. |
| 028C22 | Resolve C’s interior 0/dot alternative to zero; preserve the outer braces against H’s parentheses. |
| 028C23 | Retain the qualified overwritten zero/loop in the first E; H omits it. |
| 028C24 | Replace both witnesses’ three-dot command with the two observed continuation marks, without a comma. |
| 028C25 | Retain qualified cancelled On; H leaves this word unread. |
| 028C26 | Resolve C’s lower isom. doubt; the detached point is visible. H agrees. |
| 028C27 | Retain C’s slash/no-separate-slash alternative. H gives an unqualified quotient stroke. |
| 028C28 | Add the small detached initial dash to C’s two closing strokes; H omits the entire drawing. |

All **17** C doubt locations are accounted for: eight resolved, eight retained unchanged, and one retained with its two candidates reordered (028C14). The nine remaining qualified loci are **02, 06, 08, 12, 14, 15, 23, 25, 27**. No additional long passage was found. H’s equivalent page-number wrapper and purely equivalent macro spellings are excluded from collation. An H note is treated as an uncertainty statement only at the ink-blotted final middle index; insertion/deletion descriptions alone are not uncertainty marks.

## Crops

Each was generated by the prescribed helper with autocontrast, LANCZOS enlargement and UnsharpMask(1.0, 130, 3), then viewed once. The exact machine manifest is `crops.tsv`; crop files are in `/workspace/scratch/888e3fda13a9/crops/scan028/C/`.

| File | Full-image box (x0, y0, x1, y1) | Output width | Rotation |
| 01_b_ending.png | 1345, 180, 1686, 280 | 2800 | 0.0° |
| 02_map_source.png | 449, 328, 559, 415 | 2800 | 0.0° |
| 03_parenthesis_finis.png | 794, 265, 1476, 432 | 3000 | 0.0° |
| 04_card.png | 670, 469, 921, 549 | 2600 | 0.0° |
| 05_struck_phrase.png | 1298, 458, 1647, 578 | 2800 | 0.0° |
| 06_alors_overwrite.png | 956, 719, 1108, 823 | 2800 | 0.0° |
| 07_middle_index.png | 1026, 843, 1315, 985 | 2800 | 0.0° |
| 08_slanted_trace.png | 1508, 969, 1686, 1091 | 2600 | 28.0° |
| 09_heading_abbreviations.png | 1058, 1085, 1382, 1185 | 2800 | 0.0° |
| 10_filtration_initial.png | 528, 1420, 757, 1533 | 2800 | 0.0° |
| 11_struck_before_definir.png | 343, 1549, 517, 1660 | 2800 | 0.0° |
| 12_final_quotient.png | 715, 1685, 1106, 1839 | 2800 | 0.0° |

## Mathematics, notation, and abbreviations

**No mathematical proof or calculation occurred.** `check_events` is empty. I parsed the formulas to inspect their glyphs and attachment: minus on I; exponent −1 on p; J and I⁻ below their respective omegas; i ∈ I below the middle large wedge; and 1 ≤ i ≤ d below the final large wedge. Both ≤ signs have visible lower strokes. These are visual reading events. The wedge’s i was not used to decide the ink-blotted nested index, and the expected meaning of an extension formula was not used to decide the overlapped slash.

Proposed notation entries record this page’s omega forms, the local 2/i index doubt, exactly two continuation marks, the overlapped slash, the looped script R, and capital Card. Abbreviation records preserve ens (both occurrences), Card, p. ex, heading isom, can., and lower isom. The possible démonstrati. form is listed only as a surviving local alternative. No abbreviation is expanded in the page transcription.

## Verification and workflow

Static checks passed for balanced braces, four paired display-math delimiters, paired inline-math delimiters, and properly nested TikZ/TikZ-CD environments. The schema has 28 complete locus records, 25 inventory elements, twelve unique manifest entries, and every referenced crop present. The final page has eight explicit unsure locations and one illegible marginal unit, matching the nine unresolved review loci. No TeX compiler was invoked.

No OCR, text-recognition library, research, other page, other reader, consolidated decision, or TeX compilation was used. No decided place was cropped again. **Workflow problem/improvement: none.**
