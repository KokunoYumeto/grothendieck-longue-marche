# Existing editions of three Montpellier documents: checked against the scans

12 November 2026, 17:40 WEST. Checked and written by Claude Opus 5.5 (effort max).

The question for each document: is the outside edition complete and faithful to the archive's document, or must we transcribe it ourselves? The answers below come from the scans and the texts. A text that normalizes, paraphrases, silently corrects or skips is counted as not faithful, with examples.

## Method

- Archive scans: `15_pursuing_stacks_a_la_poursuite_des_champs_first_ep\134-1.pdf` … `134-8.pdf`, `13_autour_desquisse_dun_programme\119.pdf`, `04_elements_de_geometrie_algebrique_ega\24.pdf` and `25.pdf`. Site page n is PDF page n+1; both are given below as "site n (PDF n+1)".
- Each compared page was rendered from the embedded scan image at its native resolution (about 1700 × 2400 px), split into halves, and read in full; handwriting was zoomed and, where written sideways, rotated. The images are in `existing_editions_check_work\`.
- Tesseract OCR (English model) of every page was used only to map the documents and to locate the matching passage in the outside text (the Pursuing Stacks LaTeX by its `\pspage` markers and by grep). Every difference reported below was read on the scan image, not taken from the OCR.
- Scripts, OCR text and downloaded files were kept in the session's temporary folder, outside Documents. One helper script was written by mistake into `pursuing_stacks_expert_20261110\src\` and deleted within a minute; that folder again holds only its original files.
- Classes used: **wording** (a different word, including typos the edition introduces), **formula**, **omission**, **addition**, **silent correction** (a typo, misspelling or grammatical slip of the original corrected without notice), **normalization** (spelling, accents, hyphenation, punctuation, notation, layout), **handwritten annotation** (included without marking, altered, or missing).

## Sources looked at

| Source | What it is | Read? |
|---|---|---|
| arXiv 2111.01000 v2, LaTeX source, local `pursuing_stacks_expert_20261110\src\` (ps.tex, ps1–ps7.tex, preface.tex, prefacescriv.tex, LICENSE) | Pursuing Stacks, ed. M. Carmona with U. Buchholtz (2021), on the 2015 "scrivener" edition | Yes |
| https://arxiv.org/abs/2111.01000 | abstract page: v1 1 Nov 2021, v2 21 Nov 2021, ix+514 pp., CC0 1.0 | Yes |
| https://smf.emath.fr/publications/la-poursuite-des-champs-volume-i and its free sample https://smf.emath.fr/sites/default/files/2022-06/DM20-version-def__sample.pdf (12 pp.) | SMF edition, vol. I | Page and sample only |
| https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/PursuingStacksOrig.pdf (630 pp., 2024) | Circle scan of the typescript | Typescript p. 24 only |
| https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf (44 pp., 2008) | Circle's French Esquisse | Yes |
| https://csg.igrothendieck.org/wp-content/uploads/2026/08/G94d.pdf (50 pp.) | CSG transcription, "Draft, August 2026" | Yes |
| GGA 1 (Schneps–Lochak, CUP 1997), printed book | French text + English translation | Not read (not freely available) |
| https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseEng.pdf | Circle's English Esquisse | Not checked |
| https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/pubtexts.php | Circle bibliography, EGA V items | Yes |
| Circle `EGA/EGAV1-2.ps` (6 pp.), `EGAV5.ps` (61 pp.), `EGAV6.ps` (24 pp.), `EGAVaiello.pdf` (112 pp.), `EGAVcontents.pdf` (2 pp.), `EGA/EGA5.pdf` (171-page scan) | Blass & Blass translations (TeX, 2004), contents note, scan of the prenotes | Yes (scan: p. 95 only) |
| https://jcreinhold.github.io/ega/v/00-front-matter.html, `01-ch5-01-singular-supersingular-sets.html`, `03-ch5-05-hyperplane-sections-part-1.html` | web edition of EGA V | Yes (these three pages) |
| https://csg.igrothendieck.org/wp-content/uploads/2025/08/U90d.pdf (11 pp.) | CSG "Réflexions sur le plan des EGA", draft Aug 2025 | Yes |
| https://csg.igrothendieck.org/transcriptions/ | CSG list of transcriptions | Yes |
| CSG L49d, "Lettre à J. Dieudonné, 29.09.1965", https://csg.igrothendieck.org/wp-content/uploads/2024/09/L49d.pdf | listed transcription | Link returns "page not found"; not checked |
| `SECTIONS_STATE.md` (passages on 119, 134, 24, 25) and `MANIFEST.json` (archive titles and notes) | our earlier survey | Yes |

---

## 1. Pursuing Stacks (cotes 134-1 to 134-8)

### Outside editions

- **arXiv 2111.01000** (read): A. Grothendieck, *Pursuing Stacks*, "an extended version by Mateo Carmona with the collaboration of Ulrik Buchholtz" (copyright page in ps.tex) of the 2015 edition by an anonymous "scrivener" (https://github.com/thescrivener/PursuingStacks). v1 1 Nov 2021, v2 21 Nov 2021, ix+514 pp. Licence CC0 1.0 (arXiv and the LICENSE file). The scrivener's preface (prefacescriv.tex, kept in the source but not compiled) says the edition was made from the djvu scan on Maltsiniotis's page, and states its corrections: "some 'which's to 'that's", "many 'it's's to 'its's", "every 'standart' to 'standard'", "and so on".
- **SMF edition** (not read; page and free sample only): *Pursuing Stacks (À la poursuite des champs)*, vol. I, ed. G. Maltsiniotis, Documents Mathématiques 20 (2022), cxxi+446 pp., ISBN 978-2-85629-958-6, print only, 75 €. Volume I holds the first four chapters, §§1–91 and 95–98; volume II is announced with "les trois derniers chapitres, sections 92–94 et 99–140, les lettres à Breen" and Grothendieck's correspondence around the book. The sample's contents list shows that it reproduces Grothendieck's own front matter ("Réflexions Mathématiques", "Pursuing Stacks", "The Modelizing Story", "Table of contents of The Modelizing Story") and adds a preface with a section "Le travail d'édition de Pursuing Stacks" (p. xi), section summaries, a glossary and four indexes. Its chapter titles (I The take-off, II Test categories, III Homotopy structures, IV Asphericity structures) agree with the typescript's contents list where I checked it (II and IV). Which copy it was made from, and whether Grothendieck's handwritten annotations were collated, is not stated on the pages that are freely available: not checked.

### Coverage

The archive's Pursuing Stacks folders hold 895 site pages. In the arXiv edition:

| Archive part | In the arXiv edition? |
|---|---|
| 134-2 sites 14–36: chapter I, the letter to Quillen | Yes, with page references L.1, L.1′ … L.12. On the page checked (site 17) the edition's "2" is the number written by hand in the corner, "2)", not the "3" at the head of the page. |
| 134-2 sites 37–77: appendix, the three letters to Breen (5.2 and 17.2.1975 in French, 17–19.7.1975 in English, as in the typescript) | Yes, without page references. |
| 134-2 sites 78–81: "Notes to chapter I and Appendix" (typescript pp. 62–65) | Yes, turned into footnotes. |
| 134-3 to 134-8: typescript pp. 1–593 (§§14–140) | Yes, complete. Page markers run without gap except for pp. 279, 289 and 370, whose text is present (checked). |
| 134-1 (6 pp.): folder "Lettres Breen 75, 76", a blank page, and a 4-page handwritten letter beginning "Cher Deligne" | No. |
| 134-2 sites 3–12: Grothendieck's provisional table of contents (typed, with handwritten additions; sites 8 and 10 entirely handwritten) | No; the edition generates its own contents from the section titles. |
| 134-2 site 13: handwritten dedication ("À ceux qui furent mes élèves … et à mon frère, Dodek Shapiro …") | No. |
| 134-2 site 115 and sites 128–143: R. Brown's informal English translation of the 17–19 July 1975 letter, with his cover note | Only indirectly: the edition prints the typescript's corrected version of this translation, not Brown's document or note. |
| 134-2 sites 117–120: Brown's "COMMENTS", with references (the commented bibliography) | No. |
| 134-2 sites 122–126: Brown's translation of the 17.2.1975 letter | No (the edition prints the letter in French, with a margin reference to a published translation). |
| 134-2 sites 145–183: handwritten letter copies in French, including the 17/19 July 1975 letter to Breen ("Cher Larry, Tout d'abord félicitations …") | No. |
| 134-8 sites 42–86: about 40 pages of handwritten notes on computer-listing paper (some headed "SGA 7 Exposé IX", "SGA 7 Exposé XIII"), with versos | No. |
| Duplicates: 134-2 sites 83, 85, 87, 89, 92–114 (second copies of the appendix opening, notes pp. 64–65, the letter to Quillen) | Not compared with the first copy. |
| Not Pursuing Stacks: versos from *Récoltes et Semailles* (134-2 sites 84, 86, 88, 90; 134-4 site 83), the kimchi text and listings in 134-8 | Not applicable. |

The Montpellier scan of p. 556 (134-8 site 2) covers the page's first paragraph with a white box. The edition prints a paragraph there ("I suspect that potentially, in every single instance anew, the act of giving birth …"), taken from another copy. It cannot be checked against the Montpellier scan.

Part titles: the edition calls the parts II "Test categories and test functors", III "Homotopy structures and contractibility structures", V "Abelianization I", VII "Abelianization II". The typescript's contents list has, for example, "V Homology and cohomology (abelianization of homotopy types)" (handwritten, 134-2 site 9) and "VII Linearization of homotopy types" (site 12). The edition starts part V at §87 (p. 291), the SMF puts §§95–98 in chapter IV and §§92–94 with the last three chapters, and the archive's folders split at p. 320.

### Fidelity: pages compared

Eleven typescript pages from 134-2 to 134-8 were compared word for word and formula by formula. For 134-1 there is nothing to compare against.

| # | Archive page | Typescript page | arXiv source |
|---|---|---|---|
| 1 | 134-2 site 17 (PDF 18) | chapter I, letter to Quillen; edition's p. 2 (L.2) | ps1.tex l. 103–165 |
| 2 | 134-2 site 44 (PDF 45) | appendix p. 29, letter of 5.2.1975 (French) | ps1.tex l. 1209–1216 (§App.3) |
| 3 | 134-3 site 24 (PDF 25) | p. 24 | ps2.tex l. 1114 ff. |
| 4 | 134-3 site 81 (PDF 82) | p. 81 | ps2.tex l. 4217 ff. |
| 5 | 134-4 site 44 (PDF 45) | p. 132 | ps3.tex l. 2231 ff. |
| 6 | 134-4 site 82 (PDF 83) | p. 170 | ps3.tex l. 4210 ff. |
| 7 | 134-5 site 29 (PDF 30) | p. 216 | ps4.tex l. 1368 ff. |
| 8 | 134-6 site 1 (PDF 2) | p. 320 | ps5.tex l. 1368 ff. |
| 9 | 134-6 site 18 (PDF 19) | p. 337 | ps5.tex l. 2285 ff. |
| 10 | 134-7 site 64 (PDF 65) | p. 506 | ps6.tex l. 3129 ff. |
| 11 | 134-8 site 2 (PDF 3) | p. 556 | ps7.tex l. 49 ff. |
| 12 | 134-1 sites 3–6 (PDF 4–7) | handwritten letter "Cher Deligne" | none (omission of the whole document) |

Differences per page (typescript → edition):

1. **L.2.** Wording: handwritten "as" (replacing struck "for") → "to" in "inadequate to a sweeping foundational set-up"; "composition" → "compoisition" (typo introduced). Formula: handwritten margin note "id_a = k_1^i(a)" → `d_a=\cst k_1^i(a)`. Silent correction: "unadequate" → "inadequate". Normalization: "too bad !" → "too bad!", roman s, t, k. Handwritten, included unmarked: "(or rather, homotopy)", "as", "etc", the subscript ℓ on *, the "notation" note (rendered as a `\marginpar`).
2. **App. p. 29.** Wording: "dans le langage" → "dans la langage" (typo introduced). Omission: the closing quotation mark after "pour 0≤i≤n". Normalization: "dim. n" → "dimension n"; "disparaitre" → "disparaître"; "chaines" → "chaînes". Silent corrections: "stablilise" → "stabilise"; "interpéter" → "interpréter". Handwritten: a deletion not applied ("pouvoir" is struck and replaced by "espérer"; the edition prints "pour espérer pouvoir conclure"); "de plus", "espérer", "équivalente à", "général" included unmarked.
3. **p. 24.** Addition: "for such topology" → "for such a topology". Omission: "a still coarser" → "a coarser". Silent corrections: "caracterizing", "developped". Handwritten: the margin note "this condition just mean that the fibers are 'aspheric' … 'contractible' (in Čech sense)" becomes the footnote "this condition is equivalent to the fibers being ``aspheric'' (i.e. weakly contractible)", a rewriting that changes the mathematics. Included unmarked: "many", "section 23" (for struck "page 19 ff"), "direct" (for struck "inverse"), "arbitrary", "sheaves", "Hot-".
4. **p. 81.** Wording: "attractive in this condition" → "in the condition"; "whereas" → "wheres" and, in a footnote, "In fact" → "If fact" (typos introduced). Silent corrections: "respresented", "strenghtening", "dont". Normalization: the parentheses around "(and nothing on either factor … in (5))" are dropped; "implies (vii) i.e." → "implies (vii), i.e.,". Handwritten: three margin notes ("27.3. But this is true for any equivalence of categories …", "The 'plus' is unnecessary visibly …", "In fact, it is the condition that j_A … should be model preserving …") become ordinary footnotes, the first with its date; interlinear insertions ("induce auto", "of (Hot)", "nothing on", "in (5)", "and local test categories", "the first") included unmarked. The struck items (i) and (ii) are left out correctly.
5. **p. 132.** Wording: "loc. cit." → "loc. sit."; "homotopy structures definable" → "homotopy structure definable". Formula: "W_h ⊂ W" → `W_{h_W}\subset W`. Silent correction: "was'nt". Normalization: commas added ("compatible, i.e.,", "W-aspheric, i.e.,"). Handwritten: the margin note "11.4. By which we mean that I→e is 'universally in W' …" becomes a dated footnote; about nine interlinear insertions ("moreover", "definitely", "many", "strictly", "i.e. is", "mathematical", "natural", "take for W a homotopism structure on M,", "itself") included unmarked.
6. **p. 170.** Wording: "nor is it implied by it" → "nor is it implies by it". Handwritten insertion missing: "(ii) The product of two W-aspheric objects [in Â] is again W-aspheric": "in Â" is not printed. Handwritten, included unmarked: "the" (twice), "and map a→G", the heading "A) Total asphericity", "and moreover A is W-aspheric", "(i)". The call "(*)" written after "totally W-aspheric" has no counterpart at that place in the edition; not traced further.
7. **p. 216.** Omission: "restricted to be an object b in B" → "restricted to be object b in B". Formula: Grothendieck's handwritten correction "the projection BxC → B" is printed "the projection $B\times C\to C$", which contradicts the sentence it illustrates. Formula: the bottom vertex of the triangle diagram, "Hot(W)", is printed `\Cat`. Silent corrections: "it's image" → "its image"; the doubled "in the the functor" removed. Handwritten, included unmarked: "(A_b)_{b∈I}", "between", "W-", the bar over i*, "λ̄_i ≃".
8. **p. 320.** Wording: "a considerably clearer understanding … than now" → "a considerably clear understanding … than now"; "but belongs to" → "but belong to"; "situations where" → "situations when". Silent corrections: "undispensable", "developping", "it's twin brothers", "sacro-saint" → "sacrosanct", "Independance". Normalization: underlined "Hom(A°,M)" → `\bHom(A\op,M)`. Handwritten, included unmarked: "part of", "handy criterion for", "one or the other of", "one", "(strict)".
9. **p. 337.** Omission: "There is the problem of course" → "There is problem of course". Silent corrections: "then it seemed" → "than it seemed"; handwritten "and for whom now" → "and for which now". Normalization: "non ordered", "non trivial" (three times), "so called" hyphenated; "A°" → A^op; "L." → L_•; commas added after "Therefore", "Thus" (twice), "(non-ordered simplices)" and "boundary maps)", and one removed. Handwritten, included unmarked: "but only", "cases".
10. **p. 506.** Silent corrections: "Adam's" → "Adams'"; "analyzor" → "analyzer"; "it's tensor powers" → "its"; handwritten "a Ω-structure" → "an Ω-structure". Normalization: "i.th" → `$i$\textsuperscript{th}`; commas added ("possibly, too,", "119),", "Thus,"). Handwritten: the insertion "(prompted by the reflections from the day before, cf. section 119)" and seven others ("(n≥−1)", "extra", "(n+1)", "where", "(F,G) ↦ F∘G", "Ω_n over k_0", "yield a Ω-structure") included unmarked; the margin instructions "à la ligne" and "id" are not reproduced.
11. **p. 556.** First paragraph masked in the Montpellier scan (see Coverage). Wording: "– even as discovering them again" → "-- and as discovering them again"; "out of a mist" → "out of the mist". Silent corrections: "affraid", "was'nt", "arpegios". Normalization: commas added ("Rather surprisingly,", "way, maybe"). Handwritten: "(and the atmosphere relaxed and friendly)" printed without its parentheses; "Rather", "start", "special" included unmarked.

Counts over the eleven pages: wording 14 (6 of them typos the edition introduces), formula 4, omission 4, addition 1, silent correction 25, normalization 29 counted (notation macros not counted one by one), handwritten annotations included without marking about 65, altered 3 (pages 3, 9, 11), missing or not applied 4 (pages 2, 6, 7, 10).

The three most serious:

- p. 216 (134-5 site 29): the scan has "the projection BxC → B" (the B written by hand over the typed letter); the edition has "the projection $B\times C\to C$".
- p. 24 (134-3 site 24): margin note "fibers are 'aspheric' … 'contractible' (in Čech sense)"; edition footnote "the fibers being ``aspheric'' (i.e. weakly contractible)".
- p. 216 (same page): diagram vertex "Hot(W)"; edition `\Cat`.

### Handwritten annotations

Grothendieck's handwritten corrections and insertions are merged into the running text without any mark. His deletions are applied, with an exception on page 2 of the sample above. His margin notes become ordinary footnotes, keeping the date when he wrote one ("27.3.", "11.4."), and nothing marks them as handwritten or as later than the typed text. Some are missed (p. 170, p. 216) and one is rewritten (p. 24). His instructions to the typist ("à la ligne", "id") are dropped. The editors' own comments are marked (red brackets, `\scrcomment`). The annotations on the Montpellier copy are those of the copy the edition used: on p. 24 the Circle scan shows the same handwriting in the same places. The annotations in this edition are therefore present but unmarked, and not reliable.

### Verdict: (c) not faithful, so we transcribe anew

The arXiv text is complete for the typescript's pp. 1–593 and the appendix. But it normalizes by declared policy, corrects silently, adds and drops words, changes formulas, and merges or rewrites Grothendieck's handwritten layer without marking it. The 18 wording or formula changes on 11 pages are enough to rule it out as our text. It also lacks 134-1, the provisional contents, the dedication, Brown's documents, the French original of the third letter and the handwritten notes of 134-8. Since it is complete and CC0, its LaTeX can serve as a draft for a page-by-page collation against the scans. The p. 556 paragraph must come from another copy, such as the Circle scan (not checked there).

---

## 2. Esquisse d'un programme (in cote 119)

### Where it is in 119.pdf

- **Copy 1:** site 2 (PDF 3) is the sommaire; sites 3–59 (PDF 4–60) hold the typescript pp. 1–57 (typescript page n = site n+2). The (*)-footnotes are at the foot of the page, and the notes (1)–(7) come at the end (pp. 52–57).
- **Copy 2:** site 78 (PDF 79) is the sommaire and sites 79–135 (PDF 80–136) hold pp. 1–57. On p. 1 the title and author are struck through by hand. This copy was checked only for the sommaire and two OCR readings, which agree with copy 1.
- The rest of 119 is not the Esquisse: Comptes rendus offprints of 1971 (sites 61–76), an activity report for 1.10–15.12.1984 (sites 137–139), teaching texts, handwritten notes (about sites 144–160), course notes "Fonctions holomorphes" from 1973–74 (sites 162 ff.).

### Outside editions

- **Circle, EsquisseFr.pdf** (read). Typeset, 44 pp., PDF dated 2008. Its running heads carry pages 5–48, the GGA 1 page numbers, so it reproduces the GGA French text. The typescript page numbers 1–57 are printed in the margin. No licence stated.
- **CSG G94d** (read). "Transcription by M. Carmona et al., CSG, Grothendieck Institute. Draft, August 2026", 50 pp.; "© 2026 Grothendieck Institute, All rights reserved". It states: "derived from an unpublished scan provided by the Montpellier archive with the reference 'Cote n°119'", and notes the GGA publication.
- **GGA 1** printed text and the English translations (EsquisseEng.pdf, GGA): not read.

### Coverage

Both texts contain the whole Esquisse: the sommaire, §§1–10, every (*)-footnote and the notes (1)–(7). An OCR alignment found all 57 pages in both. Missing are only the features of the archive copies: the handwritten numbers in the N.B., and copy 2 with its annotations.

### Fidelity: pages compared

Eleven pages were compared word by word with both texts. The "page" column gives the typescript page.

| Archive | Typescript | Circle PDF | G94d PDF | Differences: Circle | Differences: G94d |
|---|---|---|---|---|---|
| site 2 (PDF 3) | sommaire | 1 | 4 (and 5) | wording: "4. Polyèdres réguliers et corps finis" → "sur les corps finis"; normalization: '"jeu de Légo-Teichmüller",' → 'jeu de "Lego-Teichmüller"'; silent corrections: "bidimensionelle" → "bidimensionnelle", "astéristiques" → "astérisques"; handwritten "1" and "7" of the N.B. typed without mark | the same, plus wording: "Théories différentiables" → "différentielles"; normalization: "Épilogue"; the N.B. moved to a footnote on p. 1; page numbers added |
| site 3 (PDF 4) | p. 1, with footnote apparatus | 3 | 5–6 | wording: "par A. Grothendieck" → "par Alexandre Grothendieck"; "plus en plus illusoires pour moi les perspectives" → "illusoire" | the same, plus omission: "développer des travaux" → "développer es travaux"; "1. —" |
| site 9 (PDF 10) | p. 7, footnote (*) | 7–8 | 10–11 | none found | normalization: underline → italics |
| site 19 (PDF 20) | p. 17, footnote (*) | 14–15 | 18–19 | none found beyond typography | normalization: "ℓ-adiques", dashes |
| site 25 (PDF 26) | p. 23, footnotes (*) and (**) | 19–20 | 22–23 | wording: "arguments de spécialisation standards" → "standard" | footnote marker "(**)" → "(*)" |
| site 30 (PDF 31) | p. 28 | 22–23 | 26–27 | none found | wording/normalization: "la thèse de Yves" → "d'Yves"; "ambiguité" → "ambiguïté" |
| site 42 (PDF 43) | p. 40, footnote (*) | 31–32 | 35–36 | omission: the full stop after "Weierstrass (*)" | none found |
| site 47 (PDF 48) | p. 45 | 34–35 | 39–40 | none found | normalization: "IHES" → "IHÉS", "A plusieurs" → "À" |
| site 53 (PDF 54) | p. 51, footnote (*) | 39 | 44–45 | none found | normalization: "..." → "…" |
| site 56 (PDF 57) | p. 54, note (4) | 41–42 | 46–47 | none found | normalization: "A l'heure" → "À" |
| site 58 (PDF 59) | p. 56, note (7) with diagram | 42–43 | 48–49 | wording: "système" → "sytème" (typo introduced); "carrés de droite" → "carrés de droites"; silent correction: the second "X_{i,j} → X_i" → "Xij → Xj"; normalization: X_{i,j}, X_{i,j,k} → Xij, Xijk | silent correction: the same X_j; normalization: indices; diagram correct |

Counts over the eleven pages:

- Circle: wording 6, omission 1, silent correction 3, normalization 2 (plus layout), handwritten included unmarked 1.
- G94d: wording 5, omission 1, silent correction 3, normalization 10, footnote marker changed 1, handwritten included unmarked 1.

Formulas agree apart from the silent correction on p. 56 and the indices. The hexagonal diagram of note (7) is right in both.

The three most serious:

- Sommaire, both texts: "Polyèdres réguliers et corps finis" (both archive copies) became "Polyèdres réguliers sur les corps finis".
- p. 1, both texts: "rend de plus en plus illusoires pour moi les perspectives" became "illusoire".
- p. 56, note (7), both texts: the typescript's "X_{i,j} → X_i (qui sont des fibrations propres" is silently corrected to "Xij → Xj".

### Version and footnotes

Both texts follow this typescript, or a copy with the same pagination. The Circle's marginal page numbers 1–57 fall at the archive copy's page breaks, and the footnote apparatus is the same: (*), (**), and the notes (1)–(7) "rajoutées ultérieurement". The Circle keeps the typescript's markers and numbering exactly. G94d keeps the notes (1)–(7) but turns the "(**)" of p. 23 into "(*)". Where G94d differs from the typescript it mostly agrees with the GGA-based Circle text ("illusoire", "sur les corps finis", "Alexandre"). It was therefore set from the GGA text and checked against the scan only in part.

### Handwritten annotations

Copy 1 has few: the numbers in the N.B. are handwritten, and both texts type them without mark. Copy 2 has a struck title on p. 1, and its other annotations were not checked. Neither outside text records annotations.

### Verdict: (c) not faithful, so we transcribe anew

Both texts are complete. Both change Grothendieck's wording in a few places, silently correct a formula, and normalize: the Circle text less, G94d more. Under the rule above they are not faithful. The differences are sparse: six of the eleven pages show none in the Circle text. A new transcription can therefore be made quickly by collating either text against copy 1, then recording copy 2's annotations.

---

## 3. EGA V (cotes 24 and 25)

### What each cote is

- **Cote 24 (76 site pages).** Archive title: "[EGA V, traduction en anglais] : copies de tapuscrit annoté (s.d.), notes manuscrites (s.d.)". The archive's note says Piotr Blass translated EGA V in 1987 from Grothendieck's notes. The pages show:
  - site 1: title page "EGA V based on notes of Alexandre Grothendieck / Stage 0 – translation by Piotr Blass";
  - site 2: "Summary";
  - site 3: contents §§1–16;
  - sites 4–74: an English typescript, pp. 4–74, of IV 20 "Hyperplane sections and conic projections", from §1 into §11 (Grassmannians), with typed translator queries ("[illegible ask Grothendieck]*") and some handwritten notes ("* Ask AG");
  - site 75: a handwritten note in French;
  - site 76: the last page of a typed CV and publications list (paragraph on "Survivre"), unrelated to EGA V.
- **Cote 25 (184 site pages).** Archive title: "Nouveau EGA V : copies de tapuscrits annotés (s.d.)", with a letter to Dieudonné (1965). Grothendieck's French prenotes, typed, with many handwritten corrections:
  - sites 2–95: IV 20 "Sections hyperplanes et projections coniques" ("Etat 0"; contents with "Commentaires", then §§1–15);
  - sites 98–133 and 137–138: IV 21 "Faisceaux inversibles et diviseurs relatifs sur les fibrés projectifs et multiprojectifs; systèmes linéaires" (§§1–4);
  - sites 134–135: the letter "Cher Dieudonné, Merci de ta lettre du 24 et pour la table des matières des par. 16–19 …";
  - sites 140–156: IV 16 "Un nouveau n° : Ensemble singulier et supersingulier d'une fonction, et critères différentiels", headed "nouveau EGA V" by hand;
  - sites 158–184: IV 17.15 "Formes lisses …" and 17.16 "Formes quadratiques lisses", with "Remords" pages (sites 166–172).
- The Circle's 171-page scan `EGA/EGA5.pdf` (freely downloadable) is a copy of the same document as cote 25. Its p. 95 is cote 25 site 140, with the same handwriting, and its page order is that of `EGAVcontents.pdf`.

### Outside texts and what they correspond to

| Text | Who, when | Corresponds to | Transcription or translation | Completeness |
|---|---|---|---|---|
| Circle `EGAV1-2.ps`, `EGAV5.ps`, `EGAV6.ps` | P. Blass and J. Blass, TeX 2004; the Circle warns they are not proofread and have many typos; no licence stated | cote 25 (IV 16 + 17.15–16; IV 20; IV 21). `EGAV5` is a revised version of Blass's 1987 typescript in cote 24. | English translation, renumbered EGA V §1, §2.15–16, §5, §6 | All the mathematical sections of cote 25; the letter to Dieudonné is not translated (no trace in the four files) |
| Circle `EGAVaiello.pdf` | 112 pp., 2004 | the same, in one file | English translation | as above |
| jcreinhold web edition, EGA V pages | J. C. Reinhold, current site; licence not stated on the pages read (GitHub repository not checked) | the Blass translations: "The Blass & Blass translation is the canonical source", "Source PDFs (digital-LaTeX, not scans)" | English re-edit of a translation: "polished into idiomatic English", French residue retired, phrasing modernized | the four fragments V.1, V.2.15–16, V.5, V.6 |
| CSG U90d "Réflexions sur le plan des EGA" | Carmona et al., draft Aug 2025, "© 2024 Grothendieck Institute, All rights reserved" | another document: a typed plan of EGA V–XII; source given as "an unpublished scan", no cote. OCR found it neither in cotes 24–25 nor in 21, 23, 26. | French transcription | not compared (not one of these cotes) |
| CSG L49d "Lettre à J. Dieudonné, 29.09.1965" | Carmona et al. | possibly the letter in cote 25, not established | not checked: link dead | not checked |

### Fidelity: pages compared

1. **Cote 24 site 4 (PDF 5), typescript p. 4, against Circle `EGAV5` p. 4 and jcreinhold §V.5.1.**
   - Circle: typos introduced ("threfore", "invertiblel", "invertile", "deifnes"); formula typos "of p" and "(p: p → S" for P; addition "invertible quotient module L_P"; omission "(locally direct summands or factors)" → "(locally direct factors)"; underlined letters lost.
   - jcreinhold rewords further ("or also the transpose homomorphism" → "or equivalently the transposed homomorphism"; "which is therefore determined" → "determined") and adds "P∨ = P(E∨)".
2. **Cote 24 site 18 (PDF 19), p. 18, against `EGAV5` p. 11.** Wording: "X is separable over k" → "separate"; "should be" → "shuld" (typo). Formula: "Z_i" → "Ziη". Addition: "and we are reduced". The typed query "[PB incomprehensible].*" is moved to a footnote. Commas added.
3. **Cote 24 site 37 (PDF 38), p. 37, against `EGAV5` pp. 21–22.** Omission: "start from a closed subset" → "start a closed subset". Typo: "dimension fo". Addition: "then for ξ ∈ P^v − Z we have coproof of T_ξ ≤ n", not in the typescript. The illegible gap "(S_k) [illegible ask Grothendieck]* S_{k−1}" is silently filled as "(Sk) we have that Gξ is (Sk−1)". The handwritten "* Ask AG" is not reproduced.
4. **Cote 25 site 2 (PDF 3): IV 20 contents and "Commentaires", against Blass "Summary" and contents (`EGAV5` pp. 2–3, cote 24 sites 2–3).**
   - "Commentaires" → "Summary", placed before the contents.
   - "esquisse détaillée" → "detailed summary".
   - "Je n'ai pas encore rédigé le n° 16" → "I have not even written section 16".
   - "sans doute les actuels nos 11, 12, 14, 15" → "without a doubt".
   - The heading "IV 20 … (Etat 0)" is dropped.
   - The handwritten "nouveau EGA V" is not reproduced.
5. **Cote 25 site 4 (PDF 5), top half (§20.1, to "accouplement naturel"), against Blass §1 (cote 24 p. 4, `EGAV5` p. 4).**
   - The handwritten corrections "coniques" (for "linéaires") and "et" are followed.
   - "20.1" → "Section 1".
   - EGA's capital "Module" → "module".
   - "(loc facteurs directs)" → "(locally direct summands or factors)" (cote 24) or "(locally direct factors)" (Circle).
   - "un module quotient inversible L_P" → "an invertible quotient L_P" (cote 24).
   - Ě, P̌ → E^v, P^v.
6. **Cote 25 site 140 (PDF 141), first page of IV 16, against `EGAV1-2` p. 2 and jcreinhold §V.1.**
   - Renumbering: "Ce n° sera utilisé au par. 20 …, mais sa place naturelle me semble bien au par. 16" → "used in V 5 (former IV 20) …, but its natural place seems to me to be here".
   - Addition: "singular zero (or root)".
   - Formula: "m_x" → "m_X"; "point ξ de X à valeurs dans k′" → "with values in k"; "x′ de X_{k′}" → "x′ of X′_k"; "φ_{k′}" → "φ′_k".
   - "Remarques 2" → "Remark 2".
   - The passage Grothendieck struck out is left out without notice.
   - jcreinhold adds "Sym²" and an editorial introduction, and quotes the translators' renumbered sentence as "Grothendieck remarks at its head: 'This section will be used in §V.5 (formerly EGA IV §20) …'".

Counts over the six pages:

- Blass texts against the French (pages 4–6): renumbering 4, wording or meaning changes 4, formula 4, addition 2, omission 2 (one of them the heading "IV 20 … (Etat 0)"), normalization 3, the handwritten header "nouveau EGA V" not reproduced 2.
- Circle TeX against the Blass typescript (pages 1–3): typos and formula typos introduced 8, formula 1 ("Ziη"), wording 1, addition 3, omission 2, illegible gap silently filled 1, handwritten note missing 1.

The three most serious:

- "Je n'ai pas encore rédigé le n° 16" became "I have not even written section 16".
- "point ξ de X à valeurs dans k′" became "point ξ of X with values in k".
- In the Circle TeX, the gap "[illegible ask Grothendieck]*" is replaced by "we have that Gξ is".

### Handwritten annotations

The translators follow Grothendieck's corrections and leave out his struck passages without notice. Some margin remarks appear as translator-marked footnotes ("Marginal remark … [Tr.]" in `EGAV5`); the jcreinhold edition sets them as marked italic inserts. None of the texts transcribes them.

### Has anyone transcribed "Nouveau EGA V" (cote 25)?

No. Nothing in the Circle, the jcreinhold edition, the CSG list of transcriptions or two web searches on the French section titles is a French transcription of cote 25. What exists is a scan of the same document (Circle `EGA5.pdf`), its contents note, English translations (Blass & Blass 2004) and an English re-edit of those (jcreinhold). The only CSG items near it are U90d, a different document, and L49d, a 1965 letter to Dieudonné whose link is dead.

### Verdict: (c) not faithful, so we transcribe anew

For cote 25 there is no transcription at all. The outside texts are translations into English that renumber Grothendieck's sections and change his references, add glosses, contain mistranslations and formula changes, and skip the letter to Dieudonné. All 184 pages of cote 25 (IV 16, IV 17.15–17.16, IV 20, IV 21, the letter, the "Remords" pages) need a French transcription from the scans. The Circle scan `EGA5.pdf` can serve as a second witness. Cote 24, Blass's 1987 English typescript, is not reproduced faithfully by the Circle TeX either (introduced typos, additions, a silently filled gap), so it too would need its own transcription if we want it as a document.

---

## Summary

None of the three outside editions can be used as our text.

- The arXiv *Pursuing Stacks* (Carmona–Buchholtz 2021, CC0) is complete for the typescript's 593 pages and the appendix. It normalizes by declared policy, corrects silently, and has 18 wording or formula changes on the 11 pages compared, including errors such as "B×C → C" for Grothendieck's handwritten "B×C → B" and "(Cat)" for "Hot(W)". It merges his handwritten layer without marking it and sometimes misses or rewrites it. It lacks 134-1, the provisional contents, the dedication, Brown's documents, the French letter originals and the handwritten notes of 134-8.
- The two Esquisse texts, the Circle's GGA-based PDF and CSG G94d, both follow the cote 119 typescript with its footnote numbering. They have only sparse departures, such as "illusoire", "sur les corps finis" and a silently corrected X_j, plus normalization that is heavier in G94d. They are not faithful in the strict sense but make good collation drafts.
- For EGA V, cote 24 is Piotr Blass's 1987 English translation typescript of IV 20 §§1–11, and cote 25 is Grothendieck's French "Nouveau EGA V" prenotes (IV 16, 17.15–16, 20, 21 and a letter to Dieudonné). All outside texts (Blass & Blass 2004 at the Circle, the jcreinhold web edition) are English translations, and nobody has transcribed cote 25.

All three verdicts are therefore (c), and the work differs in size. Pursuing Stacks and the Esquisse can be done by collating the existing texts against the scans, plus the missing archive items. The 184 pages of cote 25 need a transcription from the scans.

## Not checked

- The SMF edition's text and its editorial principles (preface p. xi).
- GGA 1 and the English Esquisse texts.
- The Maltsiniotis djvu.
- The Circle Pursuing Stacks scan beyond p. 24, including whether it shows the paragraph masked on p. 556.
- Copy 2 of the Esquisse beyond its sommaire.
- The jcreinhold pages other than the three listed, and its GitHub licence.
- CSG L49d (dead link).
- Which archive document U90d transcribes.
- The 134-2 duplicate copies.
- Typescript pages not listed above.
