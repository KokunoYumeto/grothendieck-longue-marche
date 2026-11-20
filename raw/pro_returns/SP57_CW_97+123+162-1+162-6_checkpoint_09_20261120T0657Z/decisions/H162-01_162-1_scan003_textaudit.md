# H162-01_162-1_scan003: page 14 text-only audit

Read: all three complete saved readings and reports, this page's C/H/question packet, text crop manifests, and root preview. No images, OCR, web, other-page content or root image observations were read. No ink choice is made here. No source, reader or root file was changed. The partial root spec was not audited as if complete.

## 1. Integrity and counts

Every nonempty C and H field in all 291 report differences is an exact substring of the current packet. All difference IDs are unique within each report. Counts below are raw arrays/Boolean sums, not deduplicated event totals.


| Reader | Differences | C checks | Inventory | Remaining doubts | C changed | H changed | marked H | Crops |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | 100 | 58 | 86 | 27 | 43 | 93 | 33 | 28 |
| R2 | 90 | 61 | 113 | 35 | 37 | 84 | 33 | 36 |
| R3 | 101 | 49 | 101 | 30 | 45 | 95 | 36 | 30 |


C has 48 unsure wrappers and one illegible wrapper; all three readers cover all 49 loci. R1's 58 and R2's 61 C-check rows add 9 and 12 question-packet/non-doubt checks. R3 records those non-doubt checks in notes/notation, so its count of 49 is not an omission. All inventory rows say transcribed=yes.

Crop manifest lengths, distinct report crop references and declared counts agree at 28/36/30; every referenced path exists. This checks metadata, not the claimed view history. Saved texts have 25/33/29 unsure wrappers and one illegible wrapper each. The remaining-doubt counts differ because R1 also lists the Artin point's relation, R2 also lists the contour near-contact, and R3 locally wraps its third-shaft uncertainty.

**Live update caught:** R2 changed its date during this audit to 10.5.66 / 10.3.66 / 10.I.66. The saved text, R2-018, CQ-013, remaining doubts, inventory and notes now agree. The table below uses that current reading.

## 2. Report/flag issues

- **R3-D060:** H is literally cohomologie but marked_in_H=true. That local word is unmarked. Set false for the narrow word, or expand to the actual full H title containing its two illegible spans.
- **R2-008:** evidence itself calls H périodes unmarked, but the true flag comes from neighboring uncertain Griffiths in the broad quotation. Narrow H to périodes and use false.
- **R2-009:** the same unrelated Griffiths marker is carried onto absent terminal punctuation. An empty H field and false accurately describe this local omission.
- **R2-086:** Article(s) is flagged from neighboring uncertain Grünberg. Use literal H Article and false.
- **R3-D062:** the extra-67 event is marked from the unread glyph before 67. For a separate extra-digits event use literal H 67 and false, as R1-D062 does. A combined BG/67 event may have true.
- **R2-061 / R3-D087:** broad H quotations contain illegible words, but the absent brace and baseline L have no local H marker. A separate brace/L omission should use empty H and false; if kept as a combined full-subject event, state that scope. These are scope warnings, not failed substring checks.
- **R2 inventory 44:** “Additional hatching of Ferrand photocopies,” transcribed=yes, is not backed by an explicit hatch command in the saved text. R2 has nested deletion only. R1/R3 draw the hatches; the preview retains R1's run.
- R3 inventory 46 groups “Notes sur R.R. ?” as cancelled. Its own reading and D077 clearly leave the external question live. Do not propagate the coarse inventory label as cancellation of the question.
- R1 alone lacks terminal clearpage. R2/R3 and the preview have it.
- No other word-choice contradiction between a reader's text and its report was found. Scoped reading fragments without a deletion wrapper should be interpreted in their full-row context, not promoted to live text automatically.


### Exact implicated H strings

| Scope | Literal H |
| --- | --- |
| R3-D060 narrow | `cohomologie` |
| R3-D060 full | `Hartshorne \ill\\ncohomologie \ill` |
| R2-008/009 broad | `\struck{\uncertain{Griffiths} périodes}` |
| R2-086 broad | `Article \uncertain{Grünberg}` |
| R3-D062 broad | `Notes sur \ill\ 67` |
| Serre broad | `Lettre : Serre \add{sur} \ill\ fonctionnelles, suite, début de monodromie \ill` |


## 3. Complete lexical variation table, mapped to R1 IDs

Every cell below is the actual saved local reading, including candidate order, wrappers and math delimiters. Table pipe escapes are Markdown only. Empty H is an omission. Exp numeral mode and Amsterdam spacing differ only in TeX formatting, not interpreted digits or number of closing curves. R1 IDs give the baseline apparatus locus; merged rows must retain the full feature scope.


| Locus | R1 ID | C literal | H literal | R1 | R2 | R3 |
| --- | --- | --- | --- | --- | --- | --- |
| suite | D001 | `\unsure{suite}` | `\emph{(suite)}` | `suite` | `\unsure{suite}` | `suite` |
| BG lower letter | D003 | `\unsure{$B_G$\|$B_g$}` | `\ill\ 67` | `$B_G$` | `\unsure{$B_G$\|$B_g$}` | `\unsure{$B_G$\|$B_g$}` |
| Quillen separator | D053 | `Quillen :` | `Quillen sur` | `Quillen \unsure{:\|.} sur` | `Quillen : sur` | `Quillen : sur` |
| Date | D012/D056 | `\unsure{10.3.66\|10.5.66}` | `10.I.66` | `10.\unsure{I\|1}.66` | `\unsure{10.5.66\|10.3.66\|10.I.66}` | `\unsure{10.5.66\|10.3.66}` |
| Deviations points | D059 | `\ldots` | `Quillen, \emph{Derivations} \ill` | `\ldots` | `\unsure{....\|\ldots}` | `\unsure{....\|...}` |
| Shih title | D065 | `Rapport à Bourbaki calcul différentiel` | `R. Wood à Bourbaki, calcul différentiel` | `R. Wood à Bourbaki calcul différentiel` | `R. Wood à Bourbaki calcul différentiel` | `Rapport à Bourbaki calcul différentiel` |
| 3 underline | D066 | `\uline{3}` | `3 articles` | `\uline{3}` | `\unsure{\uline{3}\|3}` | `\uline{3}` |
| fibrés | D016 | `\unsure{fibrés\|fibrés,}` | `fibrés` | `fibrés` | `fibrés` | `\unsure{fibrés}` |
| Hatched initial | D017 | `\unsure{N\|M}` | `\ill` | `\unsure{N\|M}` | `\unsure{N\|M}` | `\unsure{M\|N}` |
| PTTM spacing | D018 | `\unsure{PTTM\|PTT M}` | `\ill` | `PTTM` | `\unsure{PTTM\|PTT M}` | `PTTM` |
| Mme | D020 | `\unsure{Mme\|Mne}` | `Mme` | `Mme` | `\unsure{Mme\|Mne}` | `Mme` |
| Mme surname | D021 | `\unsure{Mathieu\|Mathies}` | `Hakim` | `Hakim` | `\unsure{Mathieu\|Mathies}` | `Hakim` |
| schémas accent | D072 | `deux schémas,` | `deux séminaires,` | `deux schémas,` | `deux schémas,` | `deux sch\unsure{é\|e}mas,` |
| Exp numeral mode | D023 | `$\unsure{7\|\mathrm I}$` | `exp.~7` | `$7$` | `7` | `$7$` |
| par.factoriel | D025 | `\unsure{parafactoriel\|par.factoriel}` | `\ill` | `par.factoriel` | `\unsure{par.factoriel\|parafactoriel}` | `\unsure{par.factoriel\|parafactoriel}` |
| Preposition | D026 | `\unsure{en\|de}` | `de dimension 2` | `en` | `\unsure{de\|en}` | `en` |
| foncteur | D027 | `\unsure{foncteur}` | `\ill` | `\unsure{foncteur}` | `foncteur` | `foncteur` |
| Added abbreviation | D082/D083 | `(dim. coh.)` | ∅ | `(dim. coh.)` | `(dim. \unsure{ch.\|coh.})` | `(dim. \unsure{coh.\|ch.})` |
| Amsterdam spacing | D029/D085 | `\unsure{?\,)\|?} )` | `?)` | `?\,) )` | `?\,)\,)` | `?\,) )` |
| équ. | D030 | `\unsure{équ.}` | `\ill` | `équ.` | `\unsure{équ.}` | `équ.` |
| fonction(s) | D031 | `\unsure{fonction\|fonctions}` | ∅ | `fonction` | `\unsure{fonction\|fonctions}` | `fonction` |
| Serre exponent | D036 | `\unsure{n-i\|n-1\|n-\nu}` | `Notes Serre sur \ill` | `\unsure{n-\nu\|n-i\|n-1}` | `\unsure{n-i\|n-1\|n-\nu}` | `\unsure{n-i\|n-1\|n-\nu}` |
| Calcul opening/P | D037 | `\unsure{(\mathrm{P}^{n}\|\mathrm{CP}^{n}}` | `Calcul \ill` | `\unsure{(\mathrm{P}^{n}\|\mathrm{CP}^{n}}` | `(\mathrm{P}^{n}` | `(\mathrm{P}^{n}` |
| Calcul inner bar/letter | D038 | `\unsure{\overline{\mathrm L}\|\mathrm L^{-}\|\overline{\mathrm C}}` | `Calcul \ill` | `\unsure{\mathrm L^{-}\|\overline{\mathrm L}}` | `\unsure{\mathrm L^{-}\|\overline{\mathrm L}\|\overline{\mathrm C}}` | `\unsure{\mathrm L^{-}\|\overline{\mathrm L}}` |
| Photocopies case | D039 | `\unsure{photocopies\|Photocopies}` | `Manuscrits ?` | `\unsure{Photocopies\|photocopies}` | `\unsure{photocopies\|Photocopies}` | `\unsure{photocopies\|Photocopies}` |
| Chev. point | D094 | `Chev.` | `Chevalley` | `Chev\unsure{.}` | `Chev.` | `Chev\unsure{.}` |
| Determinant order | D042 | `\unsure{bidéterminants\|holodéterminants}` | `Notes \ill` | `\unsure{holodéterminants\|bidéterminants}` | `\unsure{bidéterminants\|holodéterminants}` | `\unsure{bidéterminants\|holodéterminants}` |
| Gabriel | D044 | `\unsure{Gabriel}` | `Gabriel` | `\unsure{Gabriel}` | `Gabriel` | `\unsure{Gabriel}` |
| Terjanian | D045 | `\unsure{Terjanian\|Terzanian}` | `\ill` | `\unsure{Terjanian\|Terzanian}` | `Terjanian` | `Terjanian` |
| Final C index | D047 | `\unsure{$C_i$\|$C_1$}` | `\ill` | `$C_i$` | `\unsure{$C_i$\|$C_1$}` | `\unsure{$C_i$\|$C_1$}` |


## 4. Graphic and placement variations

These comparisons use saved commands, not visual measurements. Minor coordinate differences can be schematic. The table records presence, uncertainty, count, contact, extent and association differences relevant to the apparatus; it does not choose their visual accuracy.


| Locus | R1 map | R1 | R2 | R3 |
| --- | --- | --- | --- | --- |
| Third Griffiths shaft | D050 | Definite third path (957,46)--(951,77) | Definite third path (960,81)--(966,49) | Local unsure wrapper around third path |
| Point below Griffiths | D050; add R3-D050 | Absent | Absent | \fill (1176,83) circle[radius=1.4]; |
| Artin low point | D055 | Literal fill at (938,265) | Local unsure wrapper around oval fill | Literal fill at (939,265) |
| Date arc | D057 | Ends (1252,247) | Ends (1269,246) | Right hook continues to (1270,290) |
| Upper contour junction | D061 | Shared branch at (888,249) | Separate paths start (600,132)/(901,346) | Separate paths start (600,133)/(897,347) |
| Left label hatches | D067 | 6 separate slants | 5 separate slants | 6 separate slants |
| PTTM hatches | D067 | 5 separate slants | 4 separate slants | 6 separate slants |
| Early Bertin/Mme diagonal | D073 | Separate leg end (236,983) and wave start (272,848) | Low contour and broad wave separate | Explicit join (232,980)--(276,852) |
| Ferrand extra hatching | D076 | 11 slant segments | No explicit hatch command | Dense connected zigzag |
| Added papers layout | D082 | One unrotated node (635,1287) | Two nodes (632,1286)/(1056,1268) | One rotate=3 node (638,1295) |
| Serre brace low endpoint | D088 | (863,1510) | (866,1491) | (862,1505) |
| Right note second line | D089 | elliptiques (1375,1515) | elliptiques (1431,1522) | elliptiques (1380,1524) |
| Gabriel mesh | D044/D100; add R3-D099 | Absent | Absent | 8-vertex zigzag starts (707,1953) |
| Right thin diagonal | D100 | Ends (1374,1698), separate spur | Continues to (1447,1840) | Continues to (1424,1843) |
| First broad lower downstroke | D100 | Starts (564,1697) | Starts kleimanrow.base west=(553,1733) | Starts (564,1719) |
| Far-right outer return | D100 | Starts (1045,1670); ends (1597,2080) | Starts (1047,1676); ends (1597,2044) | Starts (1405,1658); ends (1598,2047) |
| Page termination | assembly | No clearpage | clearpage | clearpage |


Root preview already contains the detached Griffiths point, unsure Artin point, longer date hook, shared upper endpoint (909,360), six PTTM strokes with hooked lower terminals, faint early Bertin/Mme diagonal, Ferrand hatches, split raised-papers nodes, Gabriel mesh, extended lower-right diagonal, first broad downstroke from (555,1670), separate Rapport stroke/outer return, and clearpage. Thus none of those known inventory omissions remains in the inspected preview. R3's tentative third-shaft status and R2's hatch counts/underline doubt still belong in the reader-variance apparatus if root chooses definite/different graphics.

## 5. Full report-union coverage map

All 100 R1, 90 R2 and 101 R3 IDs occur exactly once in this map. Numeric ranges omit R1/R3's D prefix. Grouping is coverage, not a requirement to retain duplicate event rows.


| Feature group | R1 | R2 | R3 |
| --- | --- | --- | --- |
| Heading | 001,002,048 | 001,002 | 001,002,048 |
| Stationery/Giraud/Klose/Algèbre | 003,004,049,062–064 | 003–006,028 | 003,004,049,062–064 |
| Griffiths/shafts/points | 005,006,050 | 007–009 | 005,006,050 |
| SGA | 007,051 | 010,011 | 007,051 |
| Chern | 052 | 012 | 052 |
| Quillen/Adams | 008,053 | 013 | 008,053 |
| Artin/date/cross/point/arc | 009–012,054–057 | 014–019 | 009–012,054,055 |
| Goodman/Deviations/Hartshorne/contours | 013–015,058–061 | 020–027 | 013–015,056–061 |
| Shih/Schwarzenberger | 016,065,066 | 029–031 | 016,065,066 |
| Hatched labels/Atiyah | 017,018,067–069 | 032–036 | 017,018,067,068 |
| Bertin/Mme/seminar/Exp | 019–023,070–073 | 037–044 | 019–023,069–071 |
| Ferrand/Dieudonné | 024–026,074–078 | 045–050 | 024–026,072–076 |
| Circled R.R./Picard | 027,079–081 | 051–053 | 027,077,078 |
| Added papers/adic entry | 028,082–084 | 054–058 | 028,079–083 |
| Hirzebruch/Serre subjects | 029–033,085–088 | 059–066 | 029–033,084–087 |
| Right note/RR | 034,089,090 | 067–069 | 034,088,089 |
| Serre/Calcul formulas | 035–038 | 070–072 | 035–038,090,091 |
| Rapport/Kleiman/EGA V | 039,091–093 | 073–076 | 039,092–094 |
| Chev./Agison/Problèmes | 040–042,094–096 | 077–080 | 040–042,095–097 |
| Verdier/Gabriel/mesh | 043,044,097,098 | 081–084 | 043,044,098,099 |
| Final recipient/title/index | 045–047,099 | 085–088 | 045–047,100 |
| Lower cancellation paths | 100 | 089 | 101 |
| H editorial list joins | note 6, no ID | 090 | no separate ID |


## 6. Loci that can fall between imported R1 rows

1. **Full Serre formula ending:** R1-D035/036 cover base/exponent, but the explicit =0 scope is supplied by R3-D090 and R2-070.
2. **Full Calcul extent:** R1-D037/038 isolate two doubtful groups. R3-D091 covers K, raised n, both openings and both closing parentheses. Keep its whole-formula scope.
3. **Local source casing:** R2-006 explicitly distinguishes C/source lettre from H Lettre in Klose's row. R2-067 distinguishes C/source Lettre from H lowercase lettre in the right note. These belong with R1-D004/D063 and D034/D089 respectively.
4. **Picard le:** R1-D080 / R2-052 isolate this H omission; R3's foncteur and underline rows alone do not.
5. **Inserted papers:** preserve both names, parenthetical abbreviation, live state and raised association. Hartshorne alone does not cover H's misplaced et Godement and deleted Papiers.
6. **Serre baseline L:** a brace-only graphic row does not cover the missing L; retain R1-D087 / R2-063 / R3-D087's symbol scope along with singular fonctionnelle, following fonction(s), no inserted sur, début and terminal points.
7. **H-only details equal to C:** preserve stationery, deleted Deligne, XII versus XIV, all Roman cap/base rules, Chern opening/final point, no internal added commas, singular lettre/Papier/Note, initial Thèse/Congrès, source op./Exp/dim/Chev., RR without points, Problèmes deletion, Verdier full-body deletion, mon exemplaire personnel and Greenberg.
8. **Editorial joins:** R2-090 records H's repeated em dashes and semicolons. R1 note 6 treats them as linearizing layout rather than source punctuation. A single explicit scope decision covers this report variance; silently omitting it does not. Literal H — and ; both occur.
9. **Editorial H note:** reports correctly distinguish the chronological note and explanatory RR addition from manuscript text. This audit makes no historical inference from H's note.
10. **Graphics:** Griffiths point (R3-D050) and Gabriel mesh (R3-D099) need independent scope beyond bare R1. Root preview has both.

### Exact whole-formula witnesses

C:


    Notes Serre sur ${\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-i|n-1|n-\nu}}=0$


    Calcul $K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}(\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}))$


H:

    Notes Serre sur \ill

    Calcul \ill


## 7. Preview conclusion

The inspected root preview includes =0 and both Calcul closing parentheses; it matches all announced root textual choices, including 5/I/1/3, R. Wood, Mme Hakim, Exp 7, par.factoriel en, local fibrés/foncteur/sché-e doubts, M|N, ch.|coh., n-nu-first exponent, P rather than CP, L-minus/overline-L, definite Terjanian and C_i/C_1.

No unresolved text-only blocker was found in that preview. This is not certification of ink or an audit of the partial final spec. All individual-reader alternatives and the report-union coverage are above.


## 8. Final merged-spec audit follow-up

No remaining concrete text-only blocker was found in the regenerated complete spec.

- All 105 merged differences have literal C/H fields where nonempty, consistent local marked_in_H values and permitted kind values.
- The replacement's old text equals the complete R1 base; its new text equals the preview exactly.
- The substantive lexical and uncertainty alternatives in the 30-row table are represented in merged reader fields. The two harmless TeX variants (math-mode 7 and spacing between the same two Amsterdam closing curves) retain identical source content.
- Physical presence/count alternatives are recorded, including third shaft, detached points, six/five/four hatch counts, Ferrand hatch omission, contour junction, right-note placement, brace endpoints and Gabriel mesh.
- All 32 remaining-doubt records correspond to the preview's 31 unsure wrappers and one illegible wrapper. C-question witness strings are literal and decisions match final content.
- All three follow-up findings are corrected: D067 now states that R2 both draws and inventories five/four hatches; CQ-039's definite outer-parenthesis/P decision is marked resolved; the R.R. inventory explicitly has mixed state, cancelled words and a live following question.
- D050 records R3's shorter-shaft uncertainty; D088/D089 record coordinate alternatives; workflow says nine existing R2 crops.
- Inventory captions no longer contradict final live/cancelled states. Serre =0 and the complete Calcul closing delimiters remain intact.

Text and metadata only were inspected. No ink decision was made.
