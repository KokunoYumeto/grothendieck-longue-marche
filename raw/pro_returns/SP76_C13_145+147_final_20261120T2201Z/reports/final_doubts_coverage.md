# Final doubts coverage register

Reviewed 2026-11-20 21:59:21 UTC. All 24 page reports are adjudicated and independently audited, through 147_scan023.

## Result and authority

The authoritative page files contain **147 active uncertainty occurrences: 145 `\unsure` and 2 `\illegible`**. They map to **145 remaining-doubts entries** in the current page reports. Every occurrence is mapped below, every doubts entry is used, and no resolved C-mark decision is contradicted by the current page text. No transcription reading was changed in this review.

The source of each occurrence is `work/pages/<page>.tex`. The destination is the `doubts` array of `work/reports/<page>.json`. U01, U02, etc. number active uncertainty macros in page order. D01, D02, etc. number the JSON doubts array from one (D01 means `doubts[0]`). TeX line numbers refer to the current authoritative page files after the wrapper repairs.

Balanced macro arguments were inspected, with TeX comments excluded. Matches use the complete uncertainty argument or a complete preferred candidate together with its recorded alternatives. They do not use generic-word substring matches. 134 occurrence mappings have the same complete macro in the doubt reading; 13 are represented by separate preferred-reading/alternative fields. Whitespace and duplicated presentation escapes in legacy metadata do not create a different reading. Repeated short readings were assigned by their place and page order.

Two grouped entries explain the two-row difference: 145_scan028 D01 covers its upper and lower canceled notation, and 145_scan036 D05 covers the two S-alphabet occurrences in the same chain. On 147_scan023 the two `\illegible{1}` occurrences have separate entries: D06 for the upper clipped fragment and D07 for the lower fragment within `\deleted`.

All 72 marked decisions were checked against the page text after whitespace normalization: 39 resolved choices and 33 undecided choices. Every recorded decision reading occurs in the current page. No resolved mark identifier remains in a doubts-place label. All 35 change rows flagged `certainty_resolution_C` have their final reading in the corresponding page text; three of those also carry a substantive against-C flag, so only 32 are counted as resolutions of an unchanged C reading.

This is a static text and metadata review. No images or blind-reading tables were read, no OCR or external research was used, and no TeX compilation or mathematical verification was performed. The earlier `work/reports/doubts_register_review.md` is retained as a historical first-pass snapshot (120 occurrences / 118 entries); it is not the current coverage register.

## Per-page coverage

| Page | Active occurrences | Doubt entries | Unmapped occurrences | Unused entries |
| --- | --- | --- | --- | --- |
| 145_scan028 | 5 | 4 | 0 | 0 |
| 145_scan029 | 7 | 7 | 0 | 0 |
| 145_scan030 | 14 | 14 | 0 | 0 |
| 145_scan031 | 4 | 4 | 0 | 0 |
| 145_scan033 | 9 | 9 | 0 | 0 |
| 145_scan034 | 10 | 10 | 0 | 0 |
| 145_scan035 | 14 | 14 | 0 | 0 |
| 145_scan036 | 11 | 10 | 0 | 0 |
| 145_scan037 | 1 | 1 | 0 | 0 |
| 145_scan038 | 4 | 4 | 0 | 0 |
| 147_scan003 | 8 | 8 | 0 | 0 |
| 147_scan004 | 3 | 3 | 0 | 0 |
| 147_scan007 | 4 | 4 | 0 | 0 |
| 147_scan008 | 5 | 5 | 0 | 0 |
| 147_scan009 | 1 | 1 | 0 | 0 |
| 147_scan010 | 4 | 4 | 0 | 0 |
| 147_scan014 | 1 | 1 | 0 | 0 |
| 147_scan016 | 7 | 7 | 0 | 0 |
| 147_scan017 | 8 | 8 | 0 | 0 |
| 147_scan018 | 5 | 5 | 0 | 0 |
| 147_scan019 | 7 | 7 | 0 | 0 |
| 147_scan021 | 4 | 4 | 0 | 0 |
| 147_scan022 | 4 | 4 | 0 | 0 |
| 147_scan023 | 7 | 7 | 0 | 0 |
| TOTAL | 147 | 145 | 0 | 0 |

## Complete occurrence-to-doubt mapping

### 145_scan028

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{(\overline P)\|(\mathcal E)}` | D01 — L8 canceled covering notation | low | same macro |
| U02 | 2 | `\unsure{\mathcal E\|\xi}` | D01 — L8 canceled covering notation | low | same macro |
| U03 | 8 | `\unsure{conj.}` | D02 — L14 struck conj. | low | same macro |
| U04 | 10 | `\unsure{\Gamma\|F}` | D03 — L16 struck initial character | low | same macro |
| U05 | 12 | `\unsure{en\|ou}` | D04 — L19 connector before sigma_1 | low | same macro |

### 145_scan029

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 11 | `\unsure{relèvements\|relèvement}` | D01 — First paragraph final relèvement(s) | medium | preferred + alternatives |
| U02 | 13 | `\unsure{Il\|Je}` | D02 — Second paragraph initial pronoun | medium | preferred + alternatives |
| U03 | 13 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D03 — M0880: alphabet of S in Gamma | medium | preferred + alternatives |
| U04 | 16 | `\unsure{\rho'\|\dot\rho'}` | D04 — Struck first generator, not in MARKS.tsv | low | preferred + alternatives |
| U05 | 16 | `\unsure{\tau\|\deleted{\tau}}` | D07 — Tau after rho in generator definition | medium | same macro |
| U06 | 16 | `\unsure{\tau}` | D05 — Struck symbol before first decorated sigma, not in MARKS.tsv | low | preferred candidate |
| U07 | 27 | `\unsure{{\rho'}^{\deleted{-1}2}\|\dot\rho^{-2}}` | D06 — Struck product relation rho/exponent, not in MARKS.tsv | low | preferred + alternatives |

### 145_scan030

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D01 — opening symmetric-group letter | low | same macro |
| U02 | 2 | `\unsure{élts\|éléments}` | D02 — opening first compressed elements word | low | same macro |
| U03 | 2 | `\unsure{élts\|éléments}` | D03 — opening second compressed elements word | low | same macro |
| U04 | 4 | `\unsure{\dot\rho\|\rho}` | D04 — overworked generator rho | low | same macro |
| U05 | 20 | `\unsure{0\|\infty}` | D12 — Second system, first commutation, left sigma subscript | low | same macro |
| U06 | 33 | `\unsure{éléments\|élémts}` | D13 — Lower left note, elements word | medium | same macro |
| U07 | 38 | `\unsure{l_\infty=}` | D05 — canceled right-margin l_infinity starter | low | same macro |
| U08 | 43 | `\unsure{Or\|On\|Ceci}` | D06 — canceled lower-right starter | low | same macro |
| U09 | 43 | `\unsure{conjuguent\|engendrent}` | D07 — M0881 lower-right verb | low | same macro |
| U10 | 43 | `\unsure{un\|le}` | D14 — Lower right note, before ss-groupe | low | same macro |
| U11 | 45 | `\unsure{Peut-on}` | D08 — canceled bottom Peut-on | low | same macro |
| U12 | 45 | `\unsure{et pas plus}` | D09 — canceled bottom et pas plus | low | same macro |
| U13 | 45 | `\unsure{dernier\|derniers}` | D10 — bottom dernier ending | medium | same macro |
| U14 | 45 | `\unsure{groupe\|groupes}` | D11 — bottom groupe ending | medium | same macro |

### 145_scan031

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 14 | `\unsure{\deleted{i.e.}\|i.e.}` | D01 — Right annotation, state of i.e. | low | same macro |
| U02 | 18 | `\unsure{s}` | D02 — Line-end canceled starter | low | same macro |
| U03 | 18 | `\unsure{:\|;}` | D04 — Between duplicated en words | low | same macro |
| U04 | 18 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D03 — Final quotient alphabet, M0885 | medium | same macro |

### 145_scan033

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{15\|13}` | D01 — Author number | medium | preferred + alternatives |
| U02 | 7 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D02 — M0887 alphabet of S in (1) | medium | preferred + alternatives |
| U03 | 11 | `\unsure{0}` | D03 — Underlying subscript of first g in (2) | low | same macro |
| U04 | 11 | `\unsure{\infty\|0}` | D04 — M0888 final g subscript in (2) | medium | preferred + alternatives |
| U05 | 11 | `\unsure{\infty\|0}` | D05 — M0890 final sigma argument in (2) | medium | preferred + alternatives |
| U06 | 23 | `\unsure{\mathrm{lac}\|\mathrm{loc}}` | D09 — Formula (4), Aut subscript | medium | same macro |
| U07 | 37 | `\unsure{(4)\|(p)}` | D06 — M0892 marginal reference | low | preferred + alternatives |
| U08 | 40 | `\unsure{)}` | D07 — M0894 outer close of tuple (8) | low | preferred candidate |
| U09 | 42 | `\unsure{,}` | D08 — Final punctuation after calcul | low | preferred candidate |

### 145_scan034

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{satisfaisante\|satisfaisant}` | D07 — Opening, ending of satisfaisante | medium | same macro |
| U02 | 2 | `\unsure{seules\|formelles}` | D08 — Inserted word before données | low | same macro |
| U03 | 2 | `\unsure{sauf}` | D01 — Opening, canceled sauf | low | same macro |
| U04 | 6 | `\unsure{\operatorname{int}}` | D02 — (9), canceled int | low | same macro |
| U05 | 6 | `\unsure{\sigma0\|\sigma(0)}` | D03 — M0895, first lower l index in (9) | low | same macro |
| U06 | 6 | `\unsure{\sigma(\infty)}` | D04 — M0896, final exponent subscript in (9) | low | same macro |
| U07 | 12 | `\unsure{:\|.}` | D09 — Operation paragraph, punctuation after canceled et | low | same macro |
| U08 | 14 | `\unsure{\deleted{u}\inserted{\tilde u^{-1}}\|\tilde u^{-1}}` | D05 — (10), correction of inverse factor | medium | same macro |
| U09 | 18 | `\unsure{terme\|\deleted{2ième}\|\deleted{2ème}}` | D06 — Final paragraph, terme or canceled ordinal | medium | same macro |
| U10 | 18 | `\unsure{p.r.\|p.v.}` | D10 — Final paragraph, abbreviation p.r. | medium | same macro |

### 145_scan035

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 4 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D01 — M0898; opening ornate S | low | same macro |
| U02 | 4 | `\unsure{\subset\|\in\|\leftarrow}` | D02 — opening relation before double-hatted Gamma | low | same macro |
| U03 | 4 | `\unsure{\mathrm{lac}\|\mathrm{loc}}` | D09 — opening Autext subscript | low | same macro |
| U04 | 4 | `\unsure{,\|.}` | D10 — opening formula terminal punctuation | low | same macro |
| U05 | 8 | `\unsure{\vcenter{\hbox{\tikz[x=0.7em,y=0.7em,baseline=0pt]{\draw[line width=0.45pt] (0.12,0.92)--(0.05,0.72)--(0.19,0.48)--(0.22,0.16); \draw[line width=0.45pt] (0.08,0.72)--(0.35,0.86) (0.13,0.53)--(0.36,0.67) (0.20,0.22)--(0.08,0.10); \draw[line width=0.65pt] (0.32,0.27)--(0.46,0.22)--(0.44,-0.06);}}}}` | D03 — canceled ink immediately before live rho | low | same macro |
| U06 | 8 | `\unsure{\tau}` | D04 — canceled sign after rho, not separately in MARKS | low | same macro |
| U07 | 8 | `\unsure{extérieurs\|secteurs}` | D05 — struck extérieurs, not separately in MARKS | low | same macro |
| U08 | 8 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D06 — M0902; ornate S in Gamma_P* definition | low | same macro |
| U09 | 8 | `\unsure{idem}` | D07 — M0904; word before pour 1,infinity | low | same macro |
| U10 | 12 | `\unsure{rem.te\|remonte}` | D11 — live verb below equation (11) | low | same macro |
| U11 | 20 | `\unsure{On\|\deleted{On}}` | D12 — state of On at final paragraph opening | low | same macro |
| U12 | 20 | `\unsure{est\|$\to$}` | D13 — final paragraph predicate | low | same macro |
| U13 | 20 | `\unsure{ss-\|sous-}` | D14 — final short form | low | same macro |
| U14 | 20 | `\unsure{.}` | D08 — final paragraph stop | low | same macro |

### 145_scan036

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{se définit}` | D01 — Opening cancelled definition | medium | same macro |
| U02 | 2 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D02 — M0906, first S_3 | medium | same macro |
| U03 | 6 | `\unsure{2}` | D09 — Canceled terminal after on trouve que les | low | same macro |
| U04 | 6 | `\unsure{abstrayant\|oubliant}` | D03 — M0907, parenthesis after (p,sigma) | low | same macro |
| U05 | 6 | `\unsure{\mathbb Z}` | D04 — Overwritten group factor | medium | same macro |
| U06 | 6 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D05 — M0908 and M0909, S_3 twice in chain | medium | same macro |
| U07 | 6 | `\unsure{\mathfrak S_3\|\mathcal S_3}` | D05 — M0908 and M0909, S_3 twice in chain | medium | same macro |
| U08 | 6 | `\unsure{ou\|en}` | D06 — Cancelled word before double-hatted pi | low | same macro |
| U09 | 6 | `\unsure{=\|\hat{=}\|\overset{\cdot}{=}}` | D10 — First equality after rectificateurs | low | same macro |
| U10 | 8 | `\unsure{:\|à}` | D07 — Sign after quitte | medium | same macro |
| U11 | 8 | `\unsure{ou}` | D08 — M0912, word after sigma_i and dash | medium | same macro |

### 145_scan037

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 12 | `\unsure{\sigma\|\tau}` | D01 — M0913, second coordinate of tilde-u tuple | low | same macro |

### 145_scan038

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{g_0\|\rho}` | D01 — L1 canceled symbol | low | same macro |
| U02 | 4 | `\unsure{\mathfrak S_3^+\|\mathcal S_3^+}` | D02 — L3 ornate S alphabet, M0914 | low | same macro |
| U03 | 16 | `\unsure{On remarque d'abord\|On pourrait}` | D03 — L10 first canceled line | low | same macro |
| U04 | 18 | `\unsure{exprimons\|exprimer}` | D04 — L11 canceled initial word | low | same macro |

### 147_scan003

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 8 | `\unsure{Le\|La}` | D01 — entry4 article | low | same macro |
| U02 | 11 | `\unsure{g,\nu\|g}` | D02 — M0918; item7 whole subscript | low | same macro |
| U03 | 13 | `\unsure{MDT\|MOT}` | D04 — entry9 acronym | low | same macro |
| U04 | 14 | `\unsure{MDT\|MPT}` | D05 — entry10 acronym | low | same macro |
| U05 | 15 | `\unsure{des\|du}` | D06 — entry11 article | low | same macro |
| U06 | 15 | `\unsure{groupoïde\|groupoïdes}` | D07 — entry11 noun ending | low | same macro |
| U07 | 15 | `\unsure{fondamental\|fondamentaux}` | D08 — entry11 adjective ending | low | same macro |
| U08 | 16 | `\unsure{leur\|leurs}` | D03 — entry12 possessive ending | low | same macro |

### 147_scan004

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 7 | `\unsure{courbe}` | D01 — Cancelled word after un plus struck e | medium | same macro |
| U02 | 11 | `\unsure{un\|\deleted{un}}` | D03 — Condition b: un after à, before next-line la courbe | medium | same macro |
| U03 | 13 | `\unsure{contenu\|courbe}` | D02 — Cancelled word after I est | low | same macro |

### 147_scan007

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 10 | `\unsure{\text{avec}\|\text{et}}` | D01 — L9 canceled word in (5)b | low | same macro |
| U02 | 10 | `\unsure{\phi\|\varnothing}` | D02 — L9 sign after the equality in (5)b | medium | same macro |
| U03 | 15 | `\unsure{sous-schém.s\|sous-schémas}` | D03 — L14 word before inserted fermés | medium | same macro |
| U04 | 20 | `\unsure{schém.s\|schémas}` | D04 — L19 word before relatifs | medium | same macro |

### 147_scan008

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 3 | `\unsure{\phi\|\varnothing}` | D01 — margin: empty-set glyph | medium | same macro |
| U02 | 4 | `\unsure{Y\|X}` | D02 — first tuple: single overworked glyph | low | same macro |
| U03 | 4 | `\unsure{dévisant\|divisant}` | D03 — struck word after système | low | same macro |
| U04 | 8 | `\unsure{X\|S}` | D04 — Soit X | low | same macro |
| U05 | 8 | `\unsure{\widetilde A,}` | D05 — canceled entry after d'où Y | low | same macro |

### 147_scan009

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 13 | `\unsure{--\|ou}` | D01 — Parenthesis after arcs, before arêtes | low | same macro |

### 147_scan010

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 3 | `\unsure{sc.\|ie.}` | D01 — Raised abbreviation after doubles, M0932 | medium | same macro |
| U02 | 3 | `\unsure{tt\|tte}` | D03 — L14 abbreviated word before arc | medium | same macro |
| U03 | 5 | `\unsure{à}` | D02 — L17 first word of the cancellation | low | same macro |
| U04 | 5 | `\unsure{compo-\|comp.-}` | D04 — Final divided or abbreviated word | medium | same macro |

### 147_scan014

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 19 | `\unsure{,\|.}` | D01 — Heading, punctuation after closing quote of stables | medium | same macro |

### 147_scan016

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 3 | `\unsure{\to\|-}` | D07 — Opening tuple, map from S to N | medium | same macro |
| U02 | 7 | `\unsure{1\|0}` | D01 — initial sum display: index of h | medium | same macro |
| U03 | 9 | `\unsure{+1\|et}` | D02 — canceled group after first h_1=1 | low | same macro |
| U04 | 11 | `\unsure{.}` | D03 — terminal punctuation of stability insertion | low | same macro |
| U05 | 11 | `\unsure{ou}` | D04 — end of canceled graph description | medium | same macro |
| U06 | 11 | `\unsure{1\|0}` | D05 — M0937: h_1 value following nuls | medium | same macro |
| U07 | 11 | `\unsure{comme}` | D06 — canceled word after the later Mais | medium | same macro |

### 147_scan017

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{poids\|points}` | D01 — poids/points | low | same macro |
| U02 | 2 | `\unsure{le}` | D02 — small struck word after donc | low | same macro |
| U03 | 4 | `\unsure{-}` | D03 — hyphen in first MD prefix | low | same macro |
| U04 | 4 | `\unsure{-}` | D04 — hyphen in second MD prefix | low | same macro |
| U05 | 4 | `\unsure{standart\|stable}` | D07 — Canceled adjective after courbe | low | same macro |
| U06 | 4 | `\unsure{-\|.}` | D08 — Terminal mark of abbreviated suppl | medium | same macro |
| U07 | 4 | `\unsure{X\|C}` | D05 — sur C/X | low | same macro |
| U08 | 6 | ```\unsure{``types'' des}``` | D06 — final struck phrase | low | same macro |

### 147_scan018

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 3 | `\unsure{\mathcal S\|S}` | D01 — After sur, M0940 | low | same macro |
| U02 | 5 | `\unsure{\underline G\|\underline S}` | D02 — Initial tuple cancellation | low | same macro |
| U03 | 7 | `\unsure{isomorphes\|isomorphe}` | D03 — loc. isomorphes | medium | same macro |
| U04 | 7 | `\unsure{Le}` | D04 — Cancelled Le | low | same macro |
| U05 | 11 | `\unsure{qui est le}` | D05 — Cancelled qui est le | medium | same macro |

### 147_scan019

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{tt\|$\forall$}` | D01 — short form before alpha in S | medium | same macro |
| U02 | 2 | `\unsure{6\|0}` | D02 — first connectedness digit | medium | same macro |
| U03 | 2 | `\unsure{sur}` | D03 — M0941 after Y_alpha | medium | same macro |
| U04 | 4 | `\unsure{\widehat I_\alpha\|\widehat I}` | D04 — attachment of alpha to raised hatted I in canceled notation | medium | same macro |
| U05 | 4 | `\unsure{deux\|de}` | D05 — canceled word replaced by un | medium | same macro |
| U06 | 4 | `\unsure{\alpha\|\nu}` | D06 — canceled index after the later g | medium | same macro |
| U07 | 14 | `\unsure{catégorie\|catég.}` | D07 — Canceled category word beside (19) | low | same macro |

### 147_scan021

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{correspondante\|correspondants}` | D04 — Opening word, final e/s | medium | same macro |
| U02 | 2 | `\unsure{qui\|que}` | D01 — Opening, canceled word after correspondante | low | same macro |
| U03 | 5 | `\unsure{G}` | D02 — M0942, first M subscript in (23) | low | same macro |
| U04 | 13 | `\unsure{le\|les\|la}` | D03 — Final paragraph, article before groupoïde | medium | same macro |

### 147_scan022

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 4 | `\unsure{\mathfrak S_J\|\mathfrak G_J\|\mathcal G_J}` | D01 — NB, first ornamental group symbol (M0943) | medium | same macro |
| U02 | 4 | `\unsure{\mathfrak S_\nu\|\mathfrak G_\nu\|\mathcal G_\nu}` | D02 — NB, second ornamental group symbol (M0944) | medium | same macro |
| U03 | 4 | `\unsure{des\|de}` | D03 — NB, first de/des after barred-m shorthand | medium | same macro |
| U04 | 8 | `\unsure{la\|le}` | D04 — Final article before continuation on next leaf | medium | same macro |

### 147_scan023

| Occurrence | TeX line | Complete uncertainty macro | Doubt entry and place | Confidence | Match |
| --- | --- | --- | --- | --- | --- |
| U01 | 2 | `\unsure{ainsi q.}` | D01 — Canceled phrase after dim 1 | low | same macro |
| U02 | 2 | `\unsure{autismes\|conditions}` | D02 — Inserted parenthesis, contracted word | low | same macro |
| U03 | 2 | `\unsure{\phi\|\varnothing}` | D03 — Condition on I, loop-and-stem sign | medium | same macro |
| U04 | 6 | `\unsure{\mathcal S=}` | D04 — Canceled base formula before un trait | low | same macro |
| U05 | 6 | `\unsure{des\|de}` | D05 — Word after invariance | medium | same macro |
| U06 | 9 | `\illegible{1}` | D06 — M0947, upper clipped right-edge fragment | low | same macro |
| U07 | 9 | `\illegible{1}` | D07 — Lower clipped right-edge fragment and its state | low | same macro |

## Metadata reconciliation performed with this review

- 147_scan017: the canceled-adjective inventory excerpt now preserves `\unsure{standart\|stable}`.
- 147_scan019: canceled-index and canceled-category inventory excerpts now preserve `\unsure{\alpha\|\nu}` and `\unsure{catégorie\|catég.}`.
- 147_scan021: the general note now includes all three retained article readings `le\|les\|la`.
- 147_scan022: two place labels now identify the barred-m shorthand rather than an equals sign. The existing NB inventory entry now explicitly includes `Il en est donc de $\bar m$ \unsure{des\|de}`. Its notation, abbreviation, audit reading, and final page reading already agreed on barred m and were not altered.
- 147_scan023: the current `autismes\|conditions` parenthesis, barred-m shorthand, five unsure readings, and two separate clipped-fragment entries are coherent. No metadata edit was needed here.

The mapping is based on the current JSON reports. Final regeneration of derived inventories, notes, and doubts from these reviewed reports is handled by the parent workflow; this review did not execute the output builder.
