# scan015 — independent reader R3 audit

## Scope and sequence

I read only the assigned scan015 packet, the supplied notation table, the exact PREAMBLE and H convention file, and the crop utility’s source. I did not consult another reader, another page image, another page transcription, a consolidated decision, OCR, a text-recognition service, a PDF text layer, the web, or an external edition. No subreader was spawned. All writes are under `out/readers/scan015/R3`.

The first recorded clock anchor was 2026-11-20 12:48:35 UTC, after the textual conventions had been read and before the first image view. The image pass was strictly whole image once for layout, half_a once, half_b once, then one enhanced crop per listed open locus. The two supplied halves overlap naturally; neither half was re-emitted or enlarged as a whole. Every logged image was emitted through `tools.view_image` and the image output helper.

| Order | Role | Image | UTC view timestamp |
|---:|---|---|---|
| 1 | whole | `J156-6-02_156-6_scan015.jpg` | 2026-11-20 12:48:42 UTC |
| 2 | half_a | `J156-6-02_156-6_scan015_a.jpg` | 2026-11-20 12:48:49 UTC |
| 3 | half_b | `J156-6-02_156-6_scan015_b.jpg` | 2026-11-20 12:50:11 UTC |
| 4 | crop | `01_opening_family_F.jpg` | 2026-11-20 12:51:57 UTC |
| 5 | crop | `02_definit_and_cancelled_capital.jpg` | 2026-11-20 12:51:57 UTC |
| 6 | crop | `03_first_live_M.jpg` | 2026-11-20 12:51:57 UTC |
| 7 | crop | `04_family_order_indices.jpg` | 2026-11-20 12:51:57 UTC |
| 8 | crop | `05_reference_after_L.jpg` | 2026-11-20 12:52:27 UTC |
| 9 | crop | `06_star_label.jpg` | 2026-11-20 12:52:27 UTC |
| 10 | crop | `07_powerset_P.jpg` | 2026-11-20 12:52:27 UTC |
| 11 | crop | `08_cancelled_X_first_map.jpg` | 2026-11-20 12:52:27 UTC |
| 12 | crop | `09_deployment_operator.jpg` | 2026-11-20 12:52:27 UTC |
| 13 | crop | `10_insertion_and_definie.jpg` | 2026-11-20 12:53:06 UTC |
| 14 | crop | `11_double_star_label.jpg` | 2026-11-20 12:53:06 UTC |
| 15 | crop | `12_cancelled_X_second_map.jpg` | 2026-11-20 12:53:06 UTC |
| 16 | crop | `13_s_interprete.jpg` | 2026-11-20 12:53:06 UTC |

All permitted image inspections ended at 12:53:06 UTC. The complete `reading.tex` was persisted at 12:54:53 UTC, and the main reader was informed immediately afterward that the full draft was available while the report was being completed. No image was viewed after that draft.

## Open loci after the halves and the single crop pass

The halves settled the ordinary prose, formula structure, arrow directions and hooks, relation signs, tildes, separators, most punctuation, centered order indices, the locations of every repeated family letter, the three visible frame strokes, and the lateral displacement of the annotation brace. Tight coordinates for uncropped witness differences are in `report.json`. The remaining issues were the first-occurrence alphabet choices; definit and its following canceled symbol; the detached cap under the second induced relation; the reference’s last digit; two potentially surcharged star labels; the two map-input interventions; the deployment operator; the raised insertion and neighboring accent; and the final s’interprète accent.

Each of the following 13 loci received one crop and one view. Every crop uses the original 1681 × 2360 whole-page JPEG as source. All rotations are 0 degrees. The utility applied: crop → autocontrast → UnsharpMask(radius=1.2, percent=120, threshold=3) → LANCZOS enlargement to width 2800 → JPEG quality 95. The `.json` sidecars preserve the source, original-pixel box, transform, width and creation time. Existing evidence was not overwritten or recompressed.

| Crop | Original box (left, top, right, bottom) | Output pixels | Reason and result |
|---|---|---|---|
| `01_opening_family_F.jpg` | [1138, 63, 1254, 160] | 2800 × 2341 | First family F: cap, cross-arm and returning foot are clear; printed mathcal/fraktur alphabet remains uncertain. |
| `02_definit_and_cancelled_capital.jpg` | [1286, 511, 1644, 625] | 2800 × 892 | definit has no independent acute. The crossed character has two uprights and a trough, supporting M; exact M alphabet remains open. |
| `03_first_live_M.jpg` | [759, 631, 950, 715] | 2800 × 1231 | First live M provides the two-peak/rounded-trough form. Mathcal versus ordinary handwritten M remains an alphabet choice, not a changed letter identity. |
| `04_family_order_indices.jpg` | [418, 846, 603, 951] | 2800 × 1589 | The first family index has a connected small upper loop; the second has a detached cap. Family F versus barred f remains open for the second. |
| `05_reference_after_L.jpg` | [418, 1038, 604, 1132] | 2800 × 1415 | The final reference digit has an upper bar and open downward turn: literal (1.25), without cross-page correction. |
| `06_star_label.jpg` | [295, 1150, 386, 1232] | 2800 × 2523 | The (*) label has heavy crossing/retraced star strokes; no independently readable previous token is established. H’s surcharge note is credited; no speculative old label is inserted. |
| `07_powerset_P.jpg` | [749, 1139, 864, 1250] | 2800 × 2703 | Angular bowl and left-returning hook establish ornamental P. Mathcal/script/fraktur alternatives remain. |
| `08_cancelled_X_first_map.jpg` | [1086, 1139, 1167, 1225] | 2800 × 2973 | Two oblique limbs make a readable X beneath live F. The uncertainty on X is removed; H’s explicit note is credited. |
| `09_deployment_operator.jpg` | [1335, 1125, 1575, 1249] | 2800 × 1447 | Literal Dep: descending p loop, no acute on e, no final l. C’s Def alternative and H’s Dépl are rejected. |
| `10_insertion_and_definie.jpg` | [252, 1225, 681, 1349] | 2800 × 809 | Raised word reads alors. The long curve is its insertion leader; no separate acute over the following e is visible, so definie is unaccented. |
| `11_double_star_label.jpg` | [248, 1545, 389, 1645] | 2800 × 1986 | The (**) label contains two connected angular star marks. No separate prior label is recoverable; no invented deletion is added. |
| `12_cancelled_X_second_map.jpg` | [1048, 1528, 1134, 1628] | 2800 × 3256 | Live F is clear; only one additional long diagonal is separable. F versus F replacing canceled X remains a cancellation-state doubt. |
| `13_s_interprete.jpg` | [267, 2149, 636, 2251] | 2800 × 774 | The final accent is crowded by tall t and preceding-line ink. Grave versus circumflex remains unresolved; no new crop or repeat view was made. |

Actual crop count: **13**. Total actual image views: **16** (1 whole + 2 halves + 13 crops). Re-crops: **0**. Repeat image views: **0**. Rotation: **0 degrees for every crop**.

## Line-by-line comparison against both C and H

1. **Header:** the manuscript number is 14. C’s mspage and H’s page/note agree on its content. No separate archive sheet number was observed.

2. **Opening two prose lines:** “En résumé, en termes de …, c’est de la donnée de deux relations d’ordre.” H omits the visible de after c’est. The first family F retains the notation-table alphabet doubt. Both relations and d’ordre have separate single underlines; H’s emphasis macro is credited as equivalent and is not a difference by itself.

3. **(1.30) main row:** both witnesses correctly give ≤, ≪ and F≤G ⇒ F≪G. I checked the comma, implication direction, both ordinary F and G operands and the absence of equality bars on the double-chevron sign. The drawn enclosure has three visible edges with two small left gaps and no visible right vertical; both boxed witnesses add geometric closure.

4. **(1.30) annotation:** the words are “rel. d’ordre dans” followed by the family F. The annotation is beneath the row and under a brace whose left end lies right of the first relation sign. H’s prose note correctly records a brace below the signs, so it receives credit. Its formula nevertheless supplies parentheses not visible in the manuscript. The annotation’s family F has its own alphabet row and coordinates.

5. **“que je vais partir.”:** both witnesses agree; period preserved.

6. **“En termes de celles-ci, on definit” and cancellation:** the actual hyphen and comma agree. The first crop resolves the verb to unaccented definit. The canceled following symbol is M, not the family F alternative offered by C; the M alphabet is marked at this first occurrence. H correctly recognizes a cancellation.

7. **M ⊂ family F:** inclusion is open on the right, without an equality bar. Both individual letters have local alphabet rows. The cursive M has two peaks and a rounded trough; family F has a broad detached cap and crossing arm.

8. **“par (1.20), avec les relations … induites”:** number, comma and all words agree after resolving H’s explicit uncertainty on avec. Both M indices sit directly under their respective order signs. Each index gets its own occurrence row; C differs in M alphabet, H in placement.

9. **“par …, puis”:** the two family-letter indices are centered below the signs. First is the recurring family F. The second has a detached upper stroke and retains C’s family-F/barred-f alternative. Commas and puis are preserved.

10. **L ⊂ M:** both witnesses identify L and inclusion; M’s alphabet differs from C and has a separate row.

11. **“par (1.25). L’application”:** reference is read literally as (1.25), resolving C’s 6/5 doubt in favor of 5. The following period and apostrophe agree. No other page was consulted to correct the number.

12. **(*) left-hand map:** family F, hooked right arrow, ornamental P and parenthesized M were all checked. The family letter, P alphabet and M alphabet are separate collation loci. The arrow has a visible hook and right arrowhead, as in both witnesses. The thick star label was cropped once; no readable predecessor was recovered.

13. **(*) element map and final operator:** X is visibly canceled/overwritten by ordinary F at one position. C’s uncertainty on X is removed; H’s separate correct note is credited. The maps-to initial vertical bar, right arrow, tilde F, equality and parenthesized ordinary F agree. The literal operator is Dep, with no acute or final l; H’s Dépl and C’s Def alternative do not match the strokes.

14. **“est alors definie par”:** est and par agree. The raised insertion is alors, as C reads, rather than H’s donc. Its curved leader passes above the next word; no independent acute belongs to definie. The insertion is preserved with inserted markup.

15. **(1.31):** tilde F = {X∈M | X≤F}. Label, tilde, braces, ordinary operands, membership, single vertical separator and ≤ agree. M’s local alphabet differs from C and has its own row.

16. **“et”:** connecting word agrees, with no added punctuation.

17. **(**) left-hand map:** the two-star label was cropped once; the two angular star marks are retained without an invented earlier value. Family F, darkened hooked arrow and Fig(M) are read. H’s family alphabet and C’s M alphabet differ; the hook and direction agree with both.

18. **(**) right-hand map:** the initial F is legible but an extra long diagonal creates a real state uncertainty. Unlike the first map, a full separate X cannot be isolated. The reading therefore gives F versus deleted X plus F, rather than asserting a deletion and merely doubting its letter. The maps-to bar/arrow and Fig_M(F) otherwise agree. M in this Fig subscript is a distinct reported occurrence, at lower right rather than directly beneath.

19. **“par (1.4) :” and canceled number:** two small points form the colon omitted by H. The crossed (1.32) is level with the following Fig formula, below the par line. Both witnesses know it is canceled; H’s placement after the prose reference differs.

20. **Fig formula:** Fig_M(F) = {tilde X | X∈tilde F} ⊂ P(M). All ordinary letters, wave marks, separator, braces, membership, equality and inclusion were compared against both witnesses. The left subscript M, right ornamental P and its M argument have separate alphabet rows.

21. **“avec” and the subordinate definition:** tilde X = {Y∈M | Y≤X}, followed by a point. Word, wave, ordinary variables, membership, separator, inequality and terminal point agree. C and H merely line-wrap this material differently; no difference is invented for that. M’s alphabet is separately reported.

22. **Concluding paragraph, first two lines:** “Ainsi, … est interprété comme un ens. de parties dans … via (*), et ≤”. All prose and the literal ens. abbreviation agree. The family F and M each have an occurrence row. The star reference is retained; no additional old token is inferred from its retracing.

23. **Concluding paragraph, last line:** C’s s’interprète/s’interprête doubt remains after one crop. H gives the grave without a doubt. “simplement par l’inclusion” agrees, including apostrophe.

24. **Final (1.32):** F≤G ⇔ tilde F ⊂ tilde G. All symbols and the label agree with both witnesses. The final G has the local curved body and basal return; both wave marks are tildes. No terminal punctuation was added.

## Completeness and honest limits

The report contains 38 substantive difference loci, 11 individual C doubt dispositions, 29 inventory elements, 6 unresolved loci, and an empty S-row list because the supplied S.json is empty. Every difference has original-source coordinates; enhanced evidence is linked only where that locus was still open after the halves. The alphabet collation covers eight family-F occurrences, thirteen M occurrences including the canceled one, and two power-set P occurrences. No row was added solely for emphasis versus underline syntax, label syntax, prose line wrapping, or H’s explicit correct note about the first canceled X.

The six residual questions are: exact family-F alphabet; exact M alphabet; the second induced-order index as family F or barred f; exact power-set P alphabet; live/replacement state at the second map’s input; and the accent in s’interprète. The complete reading marks these in place. No physically unreadable word was replaced by a fabricated reading or by a gap. No formula symbol uses illegible markup.

The author gives no explicit doubt, verification request, question or reservation on this page. Accordingly author_doubts is empty. The check-events list records only the supplied category “carried as background without fault found”, with the exact limitation “read as the author’s assertion; no mathematical verification performed”. Visual collation is not reported as a proof check.

The frame approaches the scanned right sheet edge, so only the absence of a visible right vertical is asserted; unseen closure is not invented. The drawing is reproduced using standard TikZ inside the supplied figure macro, with (1.30) as a text node in the same drawing. The other displays use standard display delimiters and tag* labels.

Structural verification checked UTF-8 JSON parsing, required fields, literal confidence values, difference coordinates inside the source image, existence of linked evidence, all inventory flags, unique view count, matching braces, eight display-delimiter pairs, even dollar count, environment pairing, and allowed macro usage. No new macros were defined. No LaTeX engine, format build, OCR, or compilation was attempted. These checks do not certify visual typesetting, and no such certification is claimed.
