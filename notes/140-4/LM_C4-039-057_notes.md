# LM_C4-039-057: transcription notes

## 1. Source, scope, and conventions

This package transcribes the 19 supplied scan images, numbered 39–57, in their supplied order. The title, date, and archival identification below come from the accompanying task prompt. The supplied scans, rather than a published transcription or an algebraically reconstructed text, are the source of the readings (Grothendieck, 1981). No external edition or literature was used to resolve the handwriting.

The LaTeX file is a fragment without a preamble. It uses the requested editorial macros, ordinary LaTeX mathematics, and `tikz-cd`. Original top running numbers are recorded with `\mspage`; the secondary numbers at the bottom left and the printed archive footers are preserved separately with `\margin`. Thus scan 39 and its visible footer number 38 remain distinct. Page order follows the scan filenames. Marginal notes remain separate from the main text, and insertions are placed at their interpreted insertion points.

The ornate underlined C/G-like group letter and the circular O/Φ/D-like ring-scheme letter remain uncertain. The individual readings retain this uncertainty; differing alternatives do not assert that the manuscript uses different mathematical objects. In particular, the upper wiggle attached to the C/G-like letter has not been silently treated as a separate tilde. The detached tilde over Z is retained. The ζ/ξ parameter is also left explicitly uncertain where its shape does not settle the reading.

Literal changes of sign, missing factors, unusual expressions, abandoned definitions, and visibly unfinished lines are preserved. Apparent discrepancies are discussed only in the research notes. The end of scan 57 is transcribed to the final visible line; it is not completed from a continuation outside this package.

## 2. Table of doubts

Locations are approximate manuscript locations, using displayed equation numbers and paragraph or marginal positions where possible. Repeated instances of a doubtful letter may be grouped here. The exhaustive marker index in section 6 provides an additional exact line reference into the delivered LaTeX fragment for every `\unsure` and `\illegible` marker. Confidence describes the proposed reading, not the mathematical truth of the sentence.

| Scan | Approximate line / location | Proposed reading | Alternatives / unresolved detail | Confidence |
|---|---|---|---|---|
| 39 | upper; (25) | `\beta` | \beta_0 | medium |
| 39 | unnumbered display after (25) | `dfn` | df | medium |
| 39 | (26), (26bis), (27), (28) | `\zeta` | \xi | medium |
| 39 | (26), deleted symbol | `\beta` | unresolved overwritten symbol | low |
| 39 | (27a) | `localem.` | localement | medium |
| 39 | parenthesis below (27) | `pour)` | \nu_3) | low |
| 39 | parenthesis below (27) | `apparemment` | none established | medium |
| 40 | (29); final paragraph | `\zeta` | \xi | medium |
| 40 | before (30) | `opérations` | none established | medium |
| 40 | deleted before pour le second | `car. 2` | none established | low |
| 41 | old formula label beside (31) | `(24)` | (31) | low |
| 41 | (31), coefficients and underbrace | `minus; zeta` | plus; xi | low |
| 41 | (32), overwritten operators | `id; minus; plus` | 1; equals; minus | low |
| 41 | reference in Remarque, deletion | `§ 6` | unresolved cancelled reference | low |
| 41 | line after n’est pas lisse | `ça coince` | se corse | medium |
| 41 | before modifier | `Ça` | Ce | medium |
| 41 | before groupe Z | `encore un` | none established | low |
| 41 | lower paragraph | `normalisateur` | normaliseur | medium |
| 41 | superscripts of L_0 and M_rho,sigma | `sharp` | unresolved superscript | low |
| 41 | cancelled word before § suivant | `suite` | none established | medium |
| 41 | last line | `suppose` | none established | medium |
| 41 | left marginal first sentence | `provenir du` | none established | medium |
| 41 | left marginal conclusion | `est bien épi...` | soit bien épi... | medium |
| 41 | marginal formula, deleted id | `id` | none established | low |
| 41 | before groupe Z | `m’interdisant` | n’utilisant | medium |
| 41 | lower paragraph | `apparaîtra` | apparaît | medium |
| 41 | insertion after apparaîtra | `à la fois` | de façon; the independent rereading more strongly supports à la fois | high |
| 42 | first line, cancelled first noun | `sphère` | schéma | low |
| 42 | group glyph throughout | `underlined ornate C` | underlined ornate G | low |
| 42 | before (34), cancelled reference | `[7]` | (7) | medium |
| 42 | before (35), cancelled final word | `intro` | none established | low |
| 42 | (35), after aligned formulas | `alpha` | ampersand | low |
| 42 | (35)–(36) | `zeta` | xi | medium |
| 42 | last display, overwritten symbols | `mu` | unresolved cancelled symbols | low |
| 43 | top display | `u` | overwritten u | medium |
| 43 | upper display deletion | `σ²` | heavily crossed exponent | low |
| 43 | lower-middle | `vaseux` | word middle strokes compressed | medium |
| 43 | lower-middle deletion | `hom` | heavily overwritten word | low |
| 43 | lower-middle | `implicitement` | unclosed parenthesis and rapid ending | medium |
| 43 | above libre engendré | `heuristique` | initial strokes overwritten | medium |
| 43 | lower deletion | `démontrer` | ending covered by strike | low |
| 43 | throughout | `C⁺ / G⁺` | ornate alphabet and possible tilde uncertain | low |
| 43 | formula u(λ1) | `ζ` | ξ; long descending loop parameter, not resolved by later pages | medium |
| 44 | throughout | `ornate C / G` | alphabet and decorations uncertain | low |
| 44 | (40) | `G♯` | G♮; superscript too compressed to distinguish | low |
| 44 | (43) deletion | `λ` | overwritten letter before i | low |
| 45 | top deletion | `note que u définit un hom au d’indice de 3 C` | several strokes obscured by cancellation | low |
| 45 | top cancelled display | `SL(2,Z)` | first letters and digit compressed | medium |
| 45 | (44) correction | `ρ` | heavy overwritten initial glyph | low |
| 45 | (45) | `ζρ / u(ρ)` | overwritten parameter above earlier u; parentheses remain | low |
| 45 | (45) | `η / η_0` | small subscript is not distinct | medium |
| 45 | (46) deletion | `ρ′(λ′_0)` | heavy scribble; formula best reading only | low |
| 45 | after vérifier | `que / plus` | short heavily crossed word | low |
| 45 | above (48) | `que` | tiny cancelled word | low |
| 45 | before vérifier (49) | `cela` | crossed text partly visible | medium |
| 45 | after η_0σ | `pui` | word incomplete/cancelled | low |
| 45 | bottom | `car maintenant; là où ils ont un sens` | extremely cursive final clause | medium |
| 45 | throughout | `ornate C / G; ζ / ξ` | symbol family uncertain | low |
| 46 | top deleted formula | `u(ρ)=` | heavily cancelled; exact u and parentheses uncertain | low |
| 46 | middle deleted right side | `id_M` | heavy scribble before 0_M | low |
| 46 | lower-middle deletion | `au` | isolated short crossed word | low |
| 46 | lower-middle diagram | `subscript 0 on C⁺` | 0 or overwritten 4; group alphabet C/G uncertain | low |
| 46 | lower formula deletion | `λ_0` | overwritten glyph before μλ_0 | low |
| 46 | bottom overwritten factor | `ζ / ξ` | vertical overwritten factor after ω^{ν_2} | low |
| 46 | throughout | `ζ / ξ; C / G` | alphabet uncertainty retained | low |
| 47 | top foliation | `671` | overwritten final digits | low |
| 47 | all occurrences of long descending parameter | `ζ` | ξ | medium |
| 47 | upper formula after μ−1=2ν | `deleted +1` | deleted =1 | low |
| 47 | ν=2ν′−ν2 and exponent in next line | `minus` | plus, overwritten | low |
| 47 | upper third, middle factor | `(ωl0)^(−ν2)` | (ωl0^(−ν2)); parenthesis placement ambiguous | low |
| 47 | soit enfin | `deleted ζ0=` | ξ0= | low |
| 47 | middle parenthesis | `deleted pour u=u_C0` | pour u_C0 | low |
| 47 | all ornate group glyphs | `C` | G | low |
| 47 | Reste à vérifier (42) | `commutativité` | ending overwritten | medium |
| 47 | after pair of actions | `ce signifie aussi que` | ce signifie [short doubtful word] que | medium |
| 47 | cancelled words before sont égaux | `two physically unreadable words` | no secure reading at enlarged inspection | low |
| 47 | (51) cancelled arrow | `ν, {±1}²S0` | ε, μ²S0 | low |
| 47 | (51) d’où μ= | `4ν′+2+ν2` | 4ν′+2ν2+1; literal addition stroke retained first | low |
| 47 | (51) small upper-right diagram | `Gm↪Ga` | the small upward decoration is not completely clear | medium |
| 48 | 1, deleted word | `foncteurs` | — | medium |
| 48 | (52), (53) | `\underline C^{+}` | \underline G^{+} | low |
| 48 | 10, after mono. | `?` | isolated closing/overwritten mark | low |
| 48 | 12 | `groupe` | groupes | medium |
| 48 | 17, deleted phrase above (54) | `ce n’est pas` | — | low |
| 48 | left margin, first words | `cavalier` | — | medium |
| 48 | left margin, formula | `−` | + | low |
| 48 | left margin, after n’est pas épi | `où il` | — | low |
| 48 | left margin, penultimate line | `canular` | — | low |
| 48 | (55), deleted symbol | `\alpha_0` | — | low |
| 49 | (57), last argument | `u` | underlined u | medium |
| 49 | (57), interline relation | `simeq` | vertical equality | medium |
| 49 | left margin | `saute` | — | medium |
| 49 | (58) | `bold V` | double-struck V | medium |
| 49 | before (59) | `one illegible cancelled word` | comme (attempted, not securely legible) | low |
| 49 | (59), kernel object | `deleted M; inserted P` | a single overwritten P | low |
| 49 | (60), alpha_0 equation | `a_1 at three overwritten coefficients` | b_1 at the last occurrence | medium |
| 49 | (61), first b_1/b_0 sign | `−` | + | low |
| 49 | below (61), deleted opening | `On` | — | medium |
| 49 | below (61), cancelled line | `on fera a_1; one unreadable word` | c_1 in place of a_1 | low |
| 49 | bottom, Remarque | `deleted un; inserted un` | an earlier overwritten short word | low |
| 50 | 2, deleted symbol | `epsilon_3` | epsilon_2 | low |
| 50 | upper paragraph, after (62) | `ampersand` | an isolated overwritten mark | low |
| 50 | cancelled paragraph, after définition de | `Z` | — | low |
| 50 | first (63), before tuple | `Gamma` | mu | low |
| 50 | first (63), ambient factors | `third factor G_a` | overwritten factor | medium |
| 50 | first (63), after 4nu prime | `−` | + | low |
| 50 | first (63), coefficient after 2 | `nu_2` | — | medium |
| 50 | first (63), operator initial entry | `1` | overwritten symbol | medium |
| 50 | first (63), deleted coefficient c | `2nu prime−nu_2+nu_3` | — | low |
| 50 | left margin, heading | `en exprimant mu s’écrivent` | exigeant; nu; individual words remain doubtful | low |
| 50 | left margin, after pair of congruences | `square bracket` | a tall connecting brace | low |
| 50 | left margin, first equality | `1−2nu_2` | 1+2nu_2 | medium |
| 50 | left margin, after first equality | `avec` | — | medium |
| 50 | cancelled prose before second (63) | `et on va en fait` | et on a en fait | medium |
| 50 | second (63), deleted a) term | `+nu_3` | — | medium |
| 50 | second (63), deleted parenthesis | `4nu prime−2nu_2+1` | plus before 2nu_2 | medium |
| 50 | second (63), c) | `lacets` | lacet | medium |
| 50 | second (63), last symbol | `underlined lambda_1` | lambda_1 without underline | medium |
| 51 | heading deletion | `Z tilde rho,sigma; révisés; two unreadable words; O_N` | cancelled earlier title; exact central words unavailable | low |
| 51 | ring symbol throughout | `calligraphic O_N` | Phi_N; circular letter with internal vertical stroke | medium |
| 51 | above sur Z | `en groupes, O_N` | en groupes O_N without comma | medium |
| 51 | sur Z after insertion | `sur Z` | opening curved mark may resemble parenthesis but links inserted phrase; no definite matching closing parenthesis | medium |
| 51 | (65), first nontrivial term | `bold E^1` | blackboard E^1; stylized double upright E | high |
| 51 | after Rappelons la, deleted | `défi` | unfinished début of définition | medium |
| 51 | Je dis qu’il y a | `sur` | dans; retraced word could be correction | medium |
| 51 | after est, deleted | `locale` | localement; visible letters end le, no certain ment | medium |
| 51 | before n+N[lambda], deleted | `k` | x; heavily retraced single symbol | low |
| 51 | (67)b, deleted after iff | `xi` | n; compact overwritten symbol | low |
| 52 | (68), first factor | `n` | overwritten n; no stable distinct previous glyph recoverable | medium |
| 52 | (68), last product | `lambda lambda prime` | lambda lambda; the last stroke is attached or overlapping, and no N is visible before the product | medium |
| 52 | deleted word before compatible | `biad` | unfinished beginning of biadditif; lower crossing obscures middle letters | low |
| 52 | deleted phrase after Autre façon de | `la con` | le en; visibly crossed fragment, not a secure complete word | low |
| 52 | deleted ring scheme before A | `O_N` | Phi_N; circular glyph with inner upright | medium |
| 52 | cancelled glyph before Z-algèbre | `Z` | z; compact double-stroked cancellation | low |
| 52 | deleted fragment before associative | `com` | un; two rounded shoulders under strike line | low |
| 52 | insertion above associative | `unifère` | unitaire; ending is compressed | medium |
| 52 | deleted word under munie d’un idéal | `principal` | possibly truncated principal; final letter crossing unclear | medium |
| 52 | deleted phrase above l’idéal NA | `un idéal` | first word is heavily covered by cancellation | low |
| 52 | (69), first term and quotient denominator | `deleted NA, overwritten J` | N in denominator; exact earlier compound obscured | medium |
| 52 | cancelled quotient expression | `(A)_S dot underlined NB` | S0; NA; final retraced symbol xi followed by arrow, or p | low |
| 52 | inserted product phrase | `A_S0 dot underlined J produit` | no unambiguous opening parenthesis visible; the trailing parenthesis after semi-direct retained | medium |
| 52 | (70), first kernel glyph | `underlined J` | top is connected to descending right stroke: no detached tilde discerned at high zoom | high |
| 53 | 5 | `de` | deleted word may be a heavily retraced de rather than a deletion | medium |
| 53 | 7 | `hom.` | hom without final point; the final stroke is compressed | medium |
| 53 | 9, below groupes | `anneaux` | struck-through word, initial and medial strokes partly obscured | low |
| 53 | 13 | `(B_S0)*` | (B_S0)′; the superscript is a short single mark | medium |
| 53 | 14 | `passage` | the middle letters are compressed | medium |
| 53 | 14 | `s-groupe` | s.-groupe; dot not clearly visible | medium |
| 53 | (73), first line | `subset` | subseteq; lower stroke is ambiguous | medium |
| 53 | (74) | `blackboard-bold O_N*` | blackboard-bold D_N*; the oval has an interior vertical stroke | low |
| 54 | top centre | `canceled manuscript number 674` | heavily overwritten three-digit mark | medium |
| 54 | (75), before Z | `deleted G_a` | overwritten symbol; its subscript may differ | low |
| 54 | 4 | `hom. canonique (en partie` | hom without point; incomplete final phrase | medium |
| 54 | 5–8; (76) | `O_N; O_N*; O_1*; O*` | D-shaped double-stroke glyph | low |
| 54 | 11 | `les` | the word is retraced heavily | medium |
| 54 | 12–13 | `questions ... plus générales` | question; généralement; final strokes are compressed | medium |
| 54 | 15 | `hom.` | hom without point | medium |
| 54 | below (76) | `deleted φ` | several canceled strokes; symbol identity insecure | low |
| 54 | 20, left | `deleted φ λ` | two canceled signs may have been part of a discarded word/formula | low |
| 54 | 20 | `ssgt.` | syst.; handwritten abbreviation unresolved | low |
| 54 | before (77) | `+` | small isolated crossed stroke, attachment unclear | low |
| 54 | last two lines | `sans` | s-s (possible compressed abbreviation) | medium |
| 55 | 3 | `est dim. relative 1` | est de dim. relative 1; abbreviation is crossed through | medium |
| 55 | 6–8 | `du groupe; parfait` | du/des and groupe/groupes endings are compressed; parfait is rapid | medium |
| 55 | 7; (78)–(81) | `O_N*, O_12*` | D-shaped double-stroke glyph; an O/Φ/D ambiguity persists across these pages. | low |
| 55 | three canceled lines before (79) | `et on trouve une section ensembliste; le/la [one word] de/du groupe/noyau sur de l’extension β` | Middle line and final canceled symbol remain low-confidence after two independent enlarged readings. | low |
| 55 | below (79) | `ν2 ν3` | first subscript can look like 3 | medium |
| 55 | above définies | `des morphismes` | insertion attachment is curved over définies; no explicit cancellation of définies is visible | medium |
| 55 | right of (80) | `ici` | small canceled word | low |
| 55 | under (81) | `(+1)↦(0)` | canceled draft of the following assignment; first parenthesized expression obscured | low |
| 56 | top-left | `que` | The tiny word appears canceled; its stroke also partly follows the letter shapes. | medium |
| 56 | inserted ε-formulas | `(−1)^ν2 and (−1)^ν3` | The 1s are retraced; retained as unsure symbols rather than invented clean corrections. | medium |
| 56 | (83) and general-section prose | `O_12*` | D-like or Φ-like double-stroke oval; the first occurrence appears underlined. | low |
| 56 | (84), final summand | `12[deleted λ0, inserted ν0]` | Numeral 12 and the bracket variable are overwritten. λ0 remains clear in the condition below. | low |
| 56 | canceled line before power calculation | `On raisonne par/plus mod 4` | The first two words after On are compressed and crossed through; mod is also uncertain. | low |
| 56 | number (85) | `85` | The number is overwritten, possibly on an earlier 84. | medium |
| 56 | (85), first line | `−6; canceled −8ν2²)` | The minus/coefficient is overwritten; the old closing parenthesis and quadratic tail are struck through. | medium |
| 56 | (85), canceled second line | `(−8)ν2²` | A closing parenthesis after −8 is hard to separate from the digit’s stroke. | medium |
| 56 | (85), canceled third line | `1−2ν2+4[ν2−2ν2²+ν3(1` | The first sign and first ν2 inside the bracket are overwritten; the line is visibly unfinished. | low |
| 56 | last canceled sentence and equation | `On pourrait prendre; (85′) μ0′=1+4ν3−6ν2` | The ending of pourrait and the prime on the equation number are uncertain. | medium |
| 57 | first line | `Si on a` | a is reduced to a short ink spot; the double parenthesis before and after (84), (85) is visible. | medium |
| 57 | initial display | `deleted λ0, inserted ν0, or simply overwritten ν0` | The variable is heavily retraced, and the state of revision cannot be established confidently. | low |
| 57 | line after initial display | `en s’intéressant aux congruences` | The long verb is rapidly written; its internal letters and ending are compressed. | medium |
| 57 | (86) | `ν3−ν2−3ν2ν3+3ν0` | The sign before 3 is heavily overwritten and could be +; the digit 3 itself is clear. | low |
| 57 | before (87) | `et par/pour congruence/congruences mod 6` | Preposition and singular/plural ending are compressed. | medium |
| 57 | below (87) | `le non souligné μ; une replaced by la; correspondante` | Insertion μ and replacement la are above the baseline; the final ending of correspondante is uncertain. | medium |
| 57 | right of first two-row equality | `two prime/quote-like marks` | Their attachment is uncertain; retained after the first row rather than interpreted as new notation. | low |
| 57 | proposition insertion | `le schéma en groupe lisse` | Possible plural groupes; short ending is compressed. | medium |
| 57 | proposition, first listed variable | `ν2` | The first glyph is overwritten and can resemble ξ2. | medium |
| 57 | proposition, after ν3 | `canceled ξ3/ε3 et` | The canceled symbols and short word remain difficult despite 4× inspection. | low |
| 57 | proposition, after ν″ | `canceled μ3/ν3` | The first letter is obscured by deletion strokes. | low |
| 57 | proposition, after Gm | `inserted star, =O1*⊂O1` | A separate star is visible above Gm; whether it is intended as its exponent is uncertain. | low |
| 57 | proposition, final verb | `définies` | The final letters are rapidly drawn. | medium |
| 57 | (88), first row | `image can.; l’hom de Groupes; O_N* → O_1*` | The g descender supports full image rather than im.; its internal letters remain compressed. Arrowhead is not clearly distinguishable from the end of the connecting stroke; N is retained literally. | medium |
| 57 | (88), second left-hand side | `canceled l’image and (ε2/ξ2), replaced by (−1)^ν2` | The lower parenthesized symbol and beginning of the canceled word overlap several strokes. | low |
| 57 | (89), left margin | `superseded left brace` | An extra partly retraced/struck curved stroke accompanies the new brace; exact revision state is uncertain. | low |
| 57 | (89), first row | `canceled μ0; ν0/λ0 in bracket` | The erased symbol and bracket variable are heavily overwritten. | low |
| 57 | (89), last row | `opening square bracket` | The opening bracket is retraced and partly resembles a brace. | medium |
| 57 | throughout | `O_12*, O_1*, O_N*` | The closed oval with internal stroke admits O/Φ/D readings; no mathematical convention has been used to settle it. | low |

## 3. Abbreviations met

Expansions are editorial suggestions confined to this list. They do not replace the written forms in the transcription. Different written variants are retained as separate entries.

| Written form | Suggested expansion / sense | Scans |
|---|---|---|
| `$\overline{\mathrm m}$` | même | 41, 42, 44, 46 |
| `\overline{\mathrm m}` | même | 49 |
| `can.` | canonique | 57 |
| `car.` | caractéristique | 40, 41, 48, 49 |
| `cedex` | courrier d’entreprise à distribution exceptionnelle (postal abbreviation in the printed footer) | 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 |
| `cf` | confer / compare | 39 |
| `cf` | confer | 45, 47 |
| `cf` | confer / comparer | 48 |
| `CNRS` | Centre national de la recherche scientifique (printed archive footer) | 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 |
| `dfn` | définition (uncertain reading) | 39 |
| `dfn` | définition | 49 |
| `dim` | dimension | 49 |
| `gr` | groupes | 48 |
| `hom` | homomorphisme | 43, 44, 45, 46, 49, 57 |
| `hom` | homomorphismes | 56 |
| `hom.` | homomorphisme | 41, 53, 54 |
| `i.e` | id est | 50 |
| `i.e.` | id est | 39, 40, 43, 44, 45, 47, 50, 54, 56 |
| `Id / id` | identité | 40 |
| `inv.` | inversible | 53 |
| `localem.` | localement (uncertain abbreviation) | 39 |
| `mod` | modulo | 50, 56, 57 |
| `mono.` | monomorphisme | 48 |
| `mono.` | monomorphisme (or monomorphique) | 54 |
| `NB` | nota bene | 41, 56 |
| `OK.` | okay | 47 |
| `s-groupe` | sous-groupe | 53 |
| `Spec` | spectre | 47 |
| `ssgt.` | sous-groupe (uncertain reading; alternative syst. = système) | 54 |
| `syst.` | système | 54 |
| `t.f.` | type fini | 52 |
| `tte` | toute | 40 |
| `UMR` | unité mixte de recherche (printed archive footer) | 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 |
| `épi` | épimorphisme | 48 |
| `épi` | épimorphisme (or épimorphique) | 54 |
| `épi...` | épimorphisme (uncertain reading) | 41 |

## 4. Legibility and limits

The larger matrices, many numbered identities, and most of the sustained prose are more legible than the revisions. The least secure material is the overwritten signs in the early parameter systems; the diagonal notes and compressed prose on scan 41; the cancelled opening and overwritten exponents on scan 42; the abandoned presentation on scan 45; the cancelled proposal on scan 50; the three cancelled lines on scan 55; and parts of the rewritten arithmetic on scans 56–57. The ornamental group and ring letters remain uncertain throughout. Enlarged crops and, for slanted marginalia, rotated views were used to inspect these passages. Recoverable ink is transcribed with a proposed reading and a doubt mark; `\illegible` is reserved for prose whose letters could not be recovered. Neither the inventory nor a confidence label should be read as a guarantee that every proposed reading is correct.

## 5. Research notes — separate from the transcription

These notes record questions or obligations visible at the point where they arise, even when a subsequent page begins to address them. Quotations reproduce the proposed reading and inherit its uncertainty marks where applicable. The notes do not settle uncertain manuscript readings. Items labelled **own idea** are suggestions for checking or further work, with confidence and reasons; they are not claims of established results or novelty. Cross-references to sections outside the supplied scans have not been verified.

### Scan 39

**R01 — unpursued implication; (27)–(28).**

Manuscript wording: “localement de la forme” (Grothendieck, 1981, scan 39).

The locality of the two displayed expressions deserves separate attention: replacing local choices of alpha_0 and beta_0 by global parameters may introduce gluing or torsor data. These pages should be checked for the topology intended by “localement” before identifying sectionwise images with sheaf images.

**R02 — own idea; unnumbered display after (25).**

The middle product in the displayed computation of eta appears without the inverse on sigma(beta_0) that occurs in the definition of eta_0. Compare the same computation elsewhere in the manuscript; the transcription retains the visible absence rather than resolving it algebraically. (Source location: Grothendieck, 1981, scan 39.)

**Confidence:** medium. **Reason:** The omission is visible in the scan, but it may reflect a cramped or omitted exponent rather than a deliberate mathematical assertion.


### Scan 40

**R03 — unpursued implication; after (30).**

Manuscript wording: “en car. 3 pour le premier” (Grothendieck, 1981, scan 40).

The matrices expose different integral obstructions: the determinant of id-rho is 3, while id-sigma is singular over every base. A useful further calculation is the kernel and cokernel of each map over the integers and after base change, keeping distinct the notions of an epimorphism of sheaves and a surjection on sections.

**R04 — conjecture; final paragraph.**

Manuscript wording: “groupe (si possible...)” (Grothendieck, 1981, scan 40).

The parenthetical “si possible...” explicitly leaves the existence of a group structure on the proposed systems open at this point. Later formulas in this packet should be checked as a possible answer, particularly their dependence on characteristics 2 and 3.


### Scan 41

**R05 — conjecture; Remarque after (32).**

Manuscript wording: “semble bien lisse” (Grothendieck, 1981, scan 41).

Grothendieck tentatively expects the finer parameter scheme to be smooth, while expressing reservations about the earlier scheme in characteristics 2 and 3. The marginal note qualifies the optimism through the epimorphism property of a displayed linear map; the exact connective wording remains doubtful.

**R06 — own idea; left marginal map.**

Compute the Smith normal form of the block map (1-rho, -(1-sigma)) over the integers before asserting relative smoothness of its kernel. The matrices on scan 40 suggest a residual characteristic-3 obstruction, consistent with the final marginal qualification. (Source location: Grothendieck, 1981, scan 41.)

**Confidence:** high. **Reason:** This is an explicit finite matrix calculation proposed as a check, not an assertion about the unresolved scheme presentation.

**R07 — unproved claim; last paragraph.**

Manuscript wording: “On fera une présentation dans ce sens” (Grothendieck, 1981, scan 41).

A revised presentation using a normalizer is deferred to the next section, yet the construction is already taken as available here. Verify the exact ambient groups and the two marked versions of L_0 before using this identification elsewhere.


### Scan 42

**R08 — unproved claim; after (33).**

Manuscript wording: “il faut quand m̄ vérifier” (Grothendieck, 1981, scan 42).

The automorphism assertion is explicitly recognized as requiring verification, with preservation of the displayed commutator relation singled out. The following scans undertake this check; the note records the obligation at the point where it is first stated.

**R09 — own idea; (33), (35), last display.**

Track the plus signs in the nu_3 lambda_1 term and in mu=4nuprime+2nu_2+1 against the overwritten signs on scan 41 and the later parameter identities. They may reveal a change of convention or an unreconciled correction; no algebraic normalization has been applied to these displays. (Source location: Grothendieck, 1981, scan 42.)

**Confidence:** medium. **Reason:** The plus signs here are visually clear, whereas the earlier signs are overwritten; identifying their intended relation requires evidence beyond this page.


### Scan 43

**R10 — unproved claim; lower half.**

Manuscript wording: “Tous ces calculs sont un peu vaseux, logiquement” (Grothendieck, 1981, scan 43).

The author explicitly identifies a logical dependence: calculations use the existence of the homomorphism they are intended to construct. His proposed repair uses the intrinsic contracted-product description (39); a proof must establish the universal property and verify its compatibility conditions before using the resulting map.

**R11 — unpursued implication; lower half, (39).**

Manuscript wording: “Une façon de les rendre rigoureux serait” (Grothendieck, 1981, scan 43).

The proposed construction suggests separating existence of a morphism from its computation on generators. One can ask which parts of this argument remain valid under arbitrary base change and which require properties of the displayed subgroup or its presentation.


### Scan 44

**R12 — unproved claim; (41)–(42).**

Manuscript wording: “satisfaisant les deux conditions suivantes” (Grothendieck, 1981, scan 44).

The two conditions specify agreement on the common subgroup and compatibility with its action. A complete proof of the asserted construction should show necessity and sufficiency of both conditions for the contracted product in (39), including its sheaf or group-scheme interpretation.

**R13 — unproved claim; bottom.**

Manuscript wording: “Il faut donc d’abord vérifier que (33) définit bien un hom” (Grothendieck, 1981, scan 44).

This identifies the remaining existence check before applying the compatibility conditions. The subsequent generator-and-relation calculations must be tracked separately from the preceding conditional computations to avoid circularity.


### Scan 45

**R14 — unproved claim; (44)–(49).**

Manuscript wording: “les vérifications essentielles sont (47) et (49)” (Grothendieck, 1981, scan 45).

The author reduces the construction to the equalities for the powers of the transformed generators and for the transformed distinguished element. A proof should explicitly check that these equalities imply every relation in the displayed presentation, including the commutator relation.

**R15 — unproved claim; bottom.**

Manuscript wording: “une fois (47) prouvé, les calculs précédents ... sont justifiés” (Grothendieck, 1981, scan 45).

The text asserts that proving the generator power relations retrospectively legitimizes the earlier calculations. This is worth checking against the precise intermediate group used in (48), so that no relation of the final quotient was used before it was established.


### Scan 46

**R16 — unproved claim; middle, following (50).**

Manuscript wording: “dont la vérification est triviale” (Grothendieck, 1981, scan 46).

The assertion reduces the generator relations to two norm-type identities on the module. The explicit proof should substitute the displayed coboundary expressions for the parameters and check the additional ν_3λ_1 term using the stated operator identities.

**R17 — own idea; lower half.**

The expressions ζ+ρ(ζ)+ρ²(ζ) and η_0+σ(η_0) invite a systematic reading through norm operators for cyclic actions. A small chain-complex calculation might organize the presentation checks and isolate what remains valid over bases with torsion; this is a suggested reformulation, not a claim of novelty. (Source location: Grothendieck, 1981, scan 46.)

**Confidence:** medium. **Reason:** The displayed identities have exactly the form of cyclic norm annihilation, but the precise integral module and base conditions require confirmation.


### Scan 47

**R18 — unproved claim; Reste à vérifier (42).**

Manuscript wording: “qui est également évident” (Grothendieck, 1981, scan 47).

The author reduces equivariance to equality of the old and modified actions on M and calls this evident. A formal verification would need the displayed generator changes and the action of their correcting factors on M.

**Confidence:** medium. **Reason:** The asserted equality is readable, while the preceding cancelled formulation is not.

**R19 — unpursued implication; Ainsi, le groupe.**

Manuscript wording: “du moins, en tant que schéma sur S0=Spec Z” (Grothendieck, 1981, scan 47).

The qualification explicitly distinguishes constructing the underlying scheme from further group-theoretic structure. The displayed parameter maps invite a later check of their compatibility with composition; this note records only the boundary stated on this page.

**Confidence:** high. **Reason:** The qualification and parameter diagrams are explicit.

**R20 — own idea; (51).**

One could compare the fibres of the parameter maps in small characteristics with the integral presentation on the preceding pages. This is only a proposed check: the overwritten formula for μ must first be resolved from the manuscript, without replacing it by a mathematically expected expression. (Source location: Grothendieck, 1981, scan 47.)

**Confidence:** low. **Reason:** Small-characteristic behaviour may depend on the overwritten signs and integer coefficients.


### Scan 48

**R21 — unproved claim; middle, after (53).**

Manuscript wording: “« des calculs déjà faits trente six fois »” (Grothendieck, 1981, scan 48).

The group-homomorphism assertion for (53) is deferred to repeated calculations, and uniqueness is attributed to “densité schématique.” A proof would need an explicit composition law and hypotheses ensuring that equality on the indicated open locus determines the morphisms on the integral scheme; the exceptional characteristics cannot simply be discarded.

**R22 — unproved claim; left lower margin, beside (54).**

Manuscript wording: “« n’est pas un épi »; « car. 3 »” (Grothendieck, 1981, scan 48).

The marginal qualification retracts or limits the apparent surjectivity in (54), linking the issue to the map from M × M to M. Its exact wording is partly doubtful, but it directs attention to characteristic 3 and “cf plus bas”; the scheme-theoretic image and cokernel require checking.

**R23 — own idea; (55)–(56).**

Compare the integral equations for the displayed subgroup and the kernel of multiplication by 4 on the additive group, retaining the printed plus sign in (55) during the textual audit. A separate algebraic calculation could distinguish an actual characteristic-2 phenomenon from a subsequently revised sign or definition, without emending the transcription. (Source location: Grothendieck, 1981, scan 48.)

**Confidence:** medium. **Reason:** The explicit constraint 4ν′ = 0 and the displayed target _4 G_a identify the characteristic-2 locus, but the passage contains revisions and uncertain group notation.


### Scan 49

**R24 — unproved claim; upper left margin; (58)–(59).**

Manuscript wording: “« sa dimension relative … de 2 à 3 ! »” (Grothendieck, 1981, scan 49).

The marginal correction records a dimension jump in characteristic 3, while the main text continues to describe a rank-two module and an exact sequence. The comparison between the kernel scheme, its generic vector-group description, and base change to characteristic 3 therefore needs an explicit argument, including the qualification “en car. ≠ 3.”

**R25 — own idea; (61)–(62).**

Compute the Smith normal form of the integer matrix in (61), using (62)’s relation c₀+c₁=3a₁ as an independent check; the expected elementary divisors are 1 and 3. This could isolate the characteristic-3 cokernel and show precisely why the kernel after reduction is larger than the reduction of a rank-two integral kernel. (Source location: Grothendieck, 1981, scan 49.)

**Confidence:** high. **Reason:** The displayed sum of the two output coordinates is 3a₁, and the other coordinate contains a coefficient 1; the suggestion depends on resolving the overwritten sign in (61), which remains marked in the transcription.


### Scan 50

**R26 — unproved claim; upper half, congruence calculation.**

Manuscript wording: “« et elle est automatiquement satisfaite »” (Grothendieck, 1981, scan 50).

The image condition modulo 3 is said to be automatic for the profinite element considered in the preceding remark. The displayed calculation reduces it to μ ≡ 1−2ν₃ (3); checking the claim in its intended functorial setting requires specifying how the profinite element determines the discrete sign ν₃, without assuming that the same statement holds over arbitrary bases.

**R27 — conjecture; lower half, cancelled proposal.**

Manuscript wording: “« j’ai envie de modifier la définition »” (Grothendieck, 1981, scan 50).

The cancelled proposal introduces ν″ and a strengthened relation 2ν′−ν₂=3ν″−ν₃, then replaces the lacet coefficient by 3ν″. This is an authorial plan for a revised definition, not a settled assertion on this page; its effect on exceptional-characteristic fibers and the recovery of the original construction would need proof.

**R28 — own idea; left lower margin.**

Study the two congruence parameters simultaneously through the maps modulo 4 and modulo 6, keeping the common parity condition explicit. The resulting integral construction may distinguish compatible lifts from merely equal scalar values, a distinction that becomes essential when 2 or 3 is not invertible. (Source location: Grothendieck, 1981, scan 50.)

**Confidence:** high. **Reason:** Both congruences and their lifted forms μ=1−2ν₂+4ν′ and μ=1−2ν₃+6ν″ are visible in the margin, although parts of the marginal heading are doubtful.


### Scan 51

**R29 — unproved claim; introductory paragraph and (63).**

Manuscript wording: “On va introduire une construction auxiliaire” (Grothendieck, 1981, scan 51).

The author introduces a group scheme encoding the parameters mu, nu prime, nu double prime and the two discrete parameters. The simultaneous equations in (63) belong to the definition; no elimination of one relation is licensed by this page.

**Confidence:** high. **Reason:** Explicit future wording followed by a displayed system.

**R30 — unproved claim; paragraph following (66).**

Manuscript wording: “une structure d’Anneaux unique” (Grothendieck, 1981, scan 51).

The author asserts uniqueness of a ring structure with the specified addition and forthcoming multiplication. This page gives the additive construction and calculation rules; multiplication and its verification continue on the next scan.

**Confidence:** high. **Reason:** The claim precedes the unfinished calculation-rule discussion at the page break.

**R31 — own idea; (63), (66)–(67).**

Manuscript wording: “2ν′−ν₂=3ν″−ν₃” (Grothendieck, 1981, scan 51).

Compare the auxiliary formal extension with its map to the additive group, especially over bases with 2- or 3-torsion. Keeping the equality between the two half-parameters separate may retain data lost by multiplying it by 2. This is an interpretive question, not a correction to the written relations or to (67)b.

**Confidence:** medium. **Reason:** The first equality for mu is twice the displayed half-parameter equality, while the construction retains formal N[lambda] notation.


### Scan 52

**R32 — unproved claim; paragraph immediately after (68).**

Manuscript wording: “on vérifie que c’est” (Grothendieck, 1981, scan 52).

Compatibility with (67)b, biadditivity, commutativity, associativity and the stated unit are asserted without the calculations being written here. The final lambda product in (68) is uncertain, and no extra N is visible before it; the transcription therefore preserves the visible expression rather than repairing it.

**Confidence:** high. **Reason:** The prose explicitly lists properties to verify; the displayed multiplication is the only local formula offered.

**R33 — unpursued implication; generalization after (68) and diagrams (69)–(70).**

Manuscript wording: “Soit plus généralement” (Grothendieck, 1981, scan 52).

The revisions replace a principal ideal NA by a two-sided ideal J free of finite type over Z. This suggests a general construction of an algebra object from the extension 0→J→A→B→0. Its functoriality with respect to maps of pairs (A,J), and its behaviour when base change introduces torsion, are not developed on this page.

**Confidence:** medium. **Reason:** The crossed principal-ideal wording and added bilatère/finite-type conditions make the widening of scope visible; later pages must be checked before classifying the question as globally unpursued.

**R34 — own idea; (68) compared with previous (67)b.**

Manuscript wording: “N[nλ′+n′λ+λλ′]” (Grothendieck, 1981, scan 52).

Check the multiplication against the map represented in (67)b by n+N[lambda]↦n+Nlambda. Literal multiplication of the scalar images produces an N-squared cross term, whereas the visible (68) has only the outer N. This may reflect an omitted factor or a convention not supplied locally; it must remain an audit question, not an emendation.

**Confidence:** medium. **Reason:** The comparison is an elementary symbolic calculation, but the last handwritten factor and the intended formal-bracket convention remain uncertain.


### Scan 53

**R35 — unproved claim; (72)–(73).**

Manuscript wording: “on trouve une suite exacte” (Grothendieck, 1981, scan 53).

The passage from the exact sequence of ring schemes (71) to the exact sequence of unit groups (72) is stated without a local lifting argument here. A proof would have to specify the topology in which the rightmost map is surjective and verify the scheme-theoretic identification of its kernel with the invertible elements of 1+J.

**R36 — unpursued implication; (73).**

Manuscript wording: “λ+λ′+λλ′=0” (Grothendieck, 1981, scan 53).

The displayed inverse-pair equation gives a concrete model for the kernel and suggests an explicit representability check. Its relation to the ring multiplication and its behaviour under base change can be tested directly from the preceding construction, without presuming that J is nilpotent.


### Scan 54

**R37 — unpursued implication; lines 9–15.**

Manuscript wording: “ni examiner les limites projectives” (Grothendieck, 1981, scan 54).

Grothendieck explicitly postpones the structure of the projective systems and their projective limits, including the corresponding construction for a general A. The transition maps, the topology for taking the limit, and representability of the resulting object are therefore points to check beyond these pages.

**R38 — unproved claim; (76), following text.**

Manuscript wording: “n’est ni épi, ni mono” (Grothendieck, 1981, scan 54).

The canonical map to G_m is asserted to fail in general to be both an epimorphism and a monomorphism. A proof or counterexample analysis must make the chosen sheaf topology explicit, and separate the functor-of-points kernel from any failure of local surjectivity.

**R39 — unproved claim; (77).**

Manuscript wording: “en tant que schéma (sans structure de groupe)” (Grothendieck, 1981, scan 54).

The kernel is identified as a scheme with the N-torsion of G_a, while the parenthesis deliberately withholds identification of the group laws. Checking the coordinate map and computing the induced multiplication would clarify exactly what survives as a group-scheme statement.


### Scan 55

**R40 — unproved claim; lines 1–4.**

Manuscript wording: “non plat si N≠1” (Grothendieck, 1981, scan 55).

The N-torsion additive scheme is said to vanish after inverting N and to have G_a fibres at primes dividing N, hence to be nonflat for N≠1. The coordinate-ring verification is not supplied here; it would also need the previously stated range of N and the precise base S_0.

**R41 — unpursued implication; lines 5–8.**

Manuscript wording: “une maladresse de sortir du groupe” (Grothendieck, 1981, scan 55).

Grothendieck reconsiders replacing the constructed unit group by G_m and elects to retain the N-dependent group. The comment suggests that the residue and kernel data are part of the intended structure; “parfait en son genre” should not be read as an assertion that the group is perfect in the algebraic sense.

**R42 — own idea; (79)–(81).**

Clarify the nature of μ before comparing these character maps in characteristic 2: the constant group of two signs and the group scheme of square roots of unity have different fibres there. The displayed conversion to {0,1}_S0 makes this a useful notation audit, rather than an identification to assume. (Source location: Grothendieck, 1981, scan 55.)

**Confidence:** high. **Reason:** The page explicitly passes from the unit group of a finite ring to a constant two-element scheme, while μ itself is not redefined on this page.


### Scan 56

**R43 — own idea; (82)–(83).**

Audit the off-diagonal entries in table (82) against (83). With ε2 as the column label and ε3 as the row label, the visible table gives +5 at (ν2,ν3)=(1,0), whereas the visible formula (−5)^ν2(+5)^ν3 gives −5; the opposite off-diagonal is reversed too. Both readings have been retained without correction. (Source location: Grothendieck, 1981, scan 56.)

**Confidence:** high. **Reason:** The diagonal heading labels, off-diagonal signs, exponents, and mod 4/mod 6 congruences are individually visible in enlarged inspection.

**R44 — unproved claim; below (82), before (83).**

Manuscript wording: “une section ensembliste de (79)” (Grothendieck, 1981, scan 56).

The proposed section is explicitly only a section of underlying sets/schemes, not asserted to respect the group law. Verifying it requires reconciling its residue characters with the preceding table and checking the intended functorial interpretation of the idempotent sign coordinates.

**R45 — own idea; (83)–(85).**

Compute the multiplication defect of the chosen representatives μ0 to describe the extension in (79) by an explicit cocycle. The canceled simpler representative μ0′ differs from the final expression by a multiple of 12, suggesting a change of kernel coordinate rather than a new residue choice. (Source location: Grothendieck, 1981, scan 56.)

**Confidence:** medium. **Reason:** The page supplies a set-theoretic section and an explicit correction coordinate, but neither a group-law calculation nor a claim that the section is multiplicative appears here.

**R46 — unpursued implication; margin NB; power calculations.**

Manuscript wording: “ν2=ν2²” (Grothendieck, 1981, scan 56).

The idempotence remark makes the polynomial expansions meaningful for locally varying sign coordinates. A later verification should retain the distinction between a binary constant-scheme section and an arbitrary element of the base ring, especially on disconnected bases.


### Scan 57

**R47 — own idea; initial display; (86)–(87); equality before proposition; (89).**

Check the mixed-term coefficients before using these displayed formulas in a reconstructed proof. The initial expression and (89) give a −24ν2ν3 term, whereas the visible 3ν2ν3 and 2ν2ν3 terms in (86)–(87) yield different coefficients after multiplication by 4 and 6; the following two-row equality uses −6ν2ν3 on both sides. The overwritten sign in (86) is separately uncertain, and no coefficient has been corrected in the transcription. (Source location: Grothendieck, 1981, scan 57.)

**Confidence:** high. **Reason:** The coefficients 3, 2, 4, 6, and the final 12(ν0−2ν2ν3) are visible; the observation is a direct comparison of the printed algebra, not a proposed emendation.

**R48 — unpursued implication; paragraph below (87).**

Manuscript wording: “le souligné dans μ désigne la section” (Grothendieck, 1981, scan 57).

The author explicitly distinguishes a section of the constructed unit group from its image in G_m by underlining. A functor-of-points account should preserve this distinction, since earlier pages note that the map to G_m is not generally a monomorphism; replacing all underlined sections by scalar units can lose information.

**R49 — unproved claim; insertion before proposition.**

Manuscript wording: “le schéma en groupe lisse” (Grothendieck, 1981, scan 57).

The proposition refers to the constructed O_12* as smooth. A proof should identify its components and coordinate charts over the stated base, rather than infer smoothness only from its scalar image or from the two residue characters.

**R50 — unproved claim; (88)–(89), last line.**

Manuscript wording: “une section ν0 bien déterminée” (Grothendieck, 1981, scan 57).

The final normal form asserts uniqueness of the additive correction coordinate ν0. Verification must use the constructed ring scheme, where 12[ν0] is a structural coordinate, rather than cancel 12 in an arbitrary base ring; existence must also respect the sign-coordinate conditions and the displayed unit condition.

**R51 — own idea; proposition; (88)–(89).**

Test the normal form on bases with 2- or 3-torsion and on disconnected bases carrying nonconstant idempotent sign sections. Such examples can distinguish uniqueness in the constructed ring scheme from uniqueness of its image in G_m, and can expose any accidental cancellation of 12. (Source location: Grothendieck, 1981, scan 57.)

**Confidence:** high. **Reason:** The text separately records the underlined section, two constant sign coordinates, and a unique additive coordinate, while the modulus 12 is not assumed invertible on this page.

## 6. Exhaustive uncertainty-marker index

The line column refers to the plain-text line number in `LM_C4-039-057_transcription.tex`, not a newly imposed manuscript lineation. Each row corresponds to one explicit editorial marker; nested markers therefore have separate entries. This index supplements the approximate source locations and confidence judgments in section 2.

| Scan | Fragment line | Marker | Exact contents / estimated unreadable words |
|---|---|---|---|
| 39 | 12 | `unsure` | `\beta\|\beta_0` |
| 39 | 18 | `unsure` | `\mathrm{dfn}` |
| 39 | 27 | `unsure` | `\zeta\|\xi` |
| 39 | 27 | `unsure` | `\beta` |
| 39 | 31 | `unsure` | `\zeta\|\xi` |
| 39 | 33 | `unsure` | `\zeta\|\xi` |
| 39 | 42 | `unsure` | `\zeta\|\xi` |
| 39 | 42 | `unsure` | `localem.` |
| 39 | 51 | `unsure` | `pour\|$\nu_3$` |
| 39 | 51 | `unsure` | `apparemment` |
| 39 | 59 | `unsure` | `\zeta\|\xi` |
| 39 | 62 | `unsure` | `\zeta\|\xi` |
| 40 | 76 | `unsure` | `\zeta\|\xi` |
| 40 | 78 | `unsure` | `\zeta\|\xi` |
| 40 | 86 | `unsure` | `opérations` |
| 40 | 107 | `unsure` | `car. 2` |
| 40 | 110 | `unsure` | `\zeta\|\xi` |
| 41 | 121 | `unsure` | `(24)` |
| 41 | 131 | `unsure` | `\nu` |
| 41 | 131 | `unsure` | `-\|+` |
| 41 | 132 | `unsure` | `-\|+` |
| 41 | 132 | `unsure` | `\zeta\|\xi` |
| 41 | 143 | `unsure` | `\mathrm{id}\|1` |
| 41 | 144 | `unsure` | `-\|=` |
| 41 | 145 | `unsure` | `-\|+` |
| 41 | 145 | `unsure` | `+\|-` |
| 41 | 148 | `unsure` | `provenir du` |
| 41 | 153 | `unsure` | `\mathrm{id}` |
| 41 | 155 | `unsure` | `est` |
| 41 | 155 | `unsure` | `épi` |
| 41 | 158 | `unsure` | `\S\ 6` |
| 41 | 159 | `unsure` | `ça coince\|se corse` |
| 41 | 162 | `unsure` | `\zeta\|\xi` |
| 41 | 163 | `unsure` | `Ça` |
| 41 | 165 | `unsure` | `m'interdisant\|n'utilisant` |
| 41 | 166 | `unsure` | `encore un` |
| 41 | 167 | `unsure` | `\zeta\|\xi` |
| 41 | 168 | `unsure` | `apparaîtra\|apparaît` |
| 41 | 168 | `unsure` | `à la fois\|de façon` |
| 41 | 169 | `unsure` | `normalisateur\|normaliseur` |
| 41 | 169 | `unsure` | `\sharp` |
| 41 | 170 | `unsure` | `\sharp` |
| 41 | 171 | `unsure` | `suite` |
| 41 | 172 | `unsure` | `suppose` |
| 42 | 181 | `unsure` | `sphère\|schéma` |
| 42 | 184 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 42 | 195 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 42 | 197 | `unsure` | `[7]` |
| 42 | 211 | `unsure` | `\zeta\|\xi` |
| 42 | 211 | `unsure` | `intro` |
| 42 | 215 | `unsure` | `\zeta\|\xi` |
| 42 | 218 | `unsure` | `\alpha\|\&` |
| 42 | 223 | `unsure` | `\zeta\|\xi` |
| 42 | 228 | `unsure` | `\mu` |
| 42 | 228 | `unsure` | `\mu` |
| 43 | 243 | `unsure` | `u` |
| 43 | 254 | `unsure` | `\sigma^2` |
| 43 | 263 | `unsure` | `\zeta\|\xi` |
| 43 | 264 | `unsure` | `\zeta\|\xi` |
| 43 | 265 | `unsure` | `\zeta\|\xi` |
| 43 | 275 | `unsure` | `vaseux` |
| 43 | 276 | `unsure` | `hom` |
| 43 | 276 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 43 | 277 | `unsure` | `implicitement` |
| 43 | 278 | `unsure` | `heuristique` |
| 43 | 281 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 43 | 282 | `unsure` | `démontrer` |
| 43 | 285 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 43 | 286 | `unsure` | `C^{+}_{S_0}\|G^{+}_{S_0}` |
| 43 | 290 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 43 | 291 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 44 | 300 | `unsure` | `G^{\sharp}\|G^{\natural}` |
| 44 | 304 | `unsure` | `C_{S_0}\|G_{S_0}` |
| 44 | 304 | `unsure` | `C\|G` |
| 44 | 304 | `unsure` | `G^{\sharp}\|G^{\natural}` |
| 44 | 308 | `unsure` | `C\|G` |
| 44 | 308 | `unsure` | `G^{\sharp}(S_0)\|G^{\natural}(S_0)` |
| 44 | 317 | `unsure` | `C^+_{S_0}\|G^+_{S_0}` |
| 44 | 317 | `unsure` | `C\|G` |
| 44 | 328 | `unsure` | `C^+_{S_0}\|G^+_{S_0}` |
| 44 | 330 | `unsure` | `C\|G` |
| 44 | 333 | `unsure` | `\underline C\|\underline G` |
| 44 | 336 | `unsure` | `\lambda` |
| 44 | 342 | `unsure` | `\underline C^+\|\underline G^+` |
| 44 | 348 | `unsure` | `C\|G` |
| 44 | 350 | `unsure` | `C^+_{S_0}\|G^+_{S_0}` |
| 44 | 355 | `unsure` | `C_{S_0}\|G_{S_0}` |
| 44 | 357 | `unsure` | `C\|G` |
| 45 | 363 | `unsure` | `note que` |
| 45 | 363 | `unsure` | `au` |
| 45 | 363 | `unsure` | `d'indice` |
| 45 | 364 | `unsure` | `C\|G` |
| 45 | 365 | `unsure` | `de` |
| 45 | 365 | `unsure` | `C^+\|G^+` |
| 45 | 368 | `unsure` | `C_0^+\|G_0^+` |
| 45 | 369 | `unsure` | `\simeq` |
| 45 | 370 | `unsure` | `\operatorname{SL}(2,\mathbb Z)` |
| 45 | 376 | `unsure` | `C^+\|G^+` |
| 45 | 381 | `unsure` | `\rho` |
| 45 | 389 | `unsure` | `\zeta\rho\|u(\rho)` |
| 45 | 391 | `unsure` | `\zeta\|\xi` |
| 45 | 392 | `unsure` | `\eta\|\eta_0` |
| 45 | 401 | `unsure` | `\rho'(\lambda'_0)` |
| 45 | 404 | `unsure` | `que\|plus` |
| 45 | 408 | `unsure` | `que` |
| 45 | 414 | `unsure` | `C_0^+\|G_0^+` |
| 45 | 414 | `unsure` | `C_0\|G_0` |
| 45 | 420 | `unsure` | `C_0\|G_0` |
| 45 | 422 | `unsure` | `cela` |
| 45 | 428 | `unsure` | `pui` |
| 45 | 431 | `unsure` | `C\|G` |
| 45 | 433 | `unsure` | `car maintenant` |
| 45 | 433 | `unsure` | `là où ils ont un sens` |
| 45 | 434 | `unsure` | `C\|G` |
| 46 | 444 | `unsure` | `u(\rho)=` |
| 46 | 445 | `unsure` | `\zeta\|\xi` |
| 46 | 445 | `unsure` | `\zeta\|\xi` |
| 46 | 445 | `unsure` | `\zeta\|\xi` |
| 46 | 446 | `unsure` | `\zeta\|\xi` |
| 46 | 446 | `unsure` | `\zeta\|\xi` |
| 46 | 446 | `unsure` | `\zeta\|\xi` |
| 46 | 453 | `unsure` | `\zeta\|\xi` |
| 46 | 453 | `unsure` | `\zeta\|\xi` |
| 46 | 453 | `unsure` | `\zeta\|\xi` |
| 46 | 458 | `unsure` | `\zeta\|\xi` |
| 46 | 458 | `unsure` | `\zeta\|\xi` |
| 46 | 458 | `unsure` | `\zeta\|\xi` |
| 46 | 465 | `unsure` | `\mathrm{id}_{\underline M}` |
| 46 | 468 | `unsure` | `au` |
| 46 | 470 | `unsure` | `C_0^+\|G_0^+` |
| 46 | 472 | `unsure` | `C_0^+\|G_0^+` |
| 46 | 472 | `unsure` | `\underline C_0^+(S_0)\|\underline G_0^+(S_0)` |
| 46 | 477 | `unsure` | `C_0\|G_0` |
| 46 | 480 | `unsure` | `C_0\|G_0` |
| 46 | 480 | `unsure` | `\lambda_0` |
| 46 | 481 | `unsure` | `C_0\|G_0` |
| 46 | 486 | `unsure` | `C_0\|G_0` |
| 46 | 487 | `unsure` | `C_0\|G_0` |
| 46 | 487 | `unsure` | `C_0\|G_0` |
| 46 | 488 | `unsure` | `\zeta\|\xi` |
| 46 | 488 | `unsure` | `\zeta\|\xi` |
| 46 | 489 | `unsure` | `\zeta\|\xi` |
| 46 | 490 | `unsure` | `\zeta\|\xi` |
| 47 | 497 | `unsure` | `671` |
| 47 | 503 | `unsure` | `\zeta\|\xi` |
| 47 | 505 | `unsure` | `+1\|=1` |
| 47 | 506 | `unsure` | `\zeta\|\xi` |
| 47 | 507 | `unsure` | `-\|+` |
| 47 | 508 | `unsure` | `\zeta\|\xi` |
| 47 | 510 | `unsure` | `(\omega l_0)^{(-\nu_2)}\|(\omega l_0^{(-\nu_2)})` |
| 47 | 511 | `unsure` | `-\|+` |
| 47 | 513 | `unsure` | `\zeta\|\xi` |
| 47 | 517 | `unsure` | `\zeta\|\xi` |
| 47 | 517 | `unsure` | `\zeta\|\xi` |
| 47 | 520 | `unsure` | `\zeta\|\xi` |
| 47 | 521 | `unsure` | `\zeta_0=\|\xi_0=` |
| 47 | 522 | `unsure` | `\zeta\|\xi` |
| 47 | 522 | `unsure` | `\lambda_1(\nu)\|\lambda_1^{(\nu)}` |
| 47 | 526 | `unsure` | `\zeta\|\xi` |
| 47 | 531 | `unsure` | `pour $u=u_{\unsure{C_0\|G_0}}$\|pour $u_{\unsure{C_0\|G_0}}$` |
| 47 | 531 | `unsure` | `C_0\|G_0` |
| 47 | 531 | `unsure` | `C_0\|G_0` |
| 47 | 532 | `unsure` | `C_0\|G_0` |
| 47 | 534 | `unsure` | `C_0\|G_0` |
| 47 | 536 | `unsure` | `\zeta\|\xi` |
| 47 | 537 | `unsure` | `\zeta\|\xi` |
| 47 | 538 | `unsure` | `\zeta\|\xi` |
| 47 | 543 | `unsure` | `signifie` |
| 47 | 544 | `unsure` | `commutativité` |
| 47 | 548 | `unsure` | `ce signifie` |
| 47 | 551 | `illegible` | `2` |
| 47 | 563 | `unsure` | `\nu\|\varepsilon` |
| 47 | 563 | `unsure` | `\{\pm1\}_{S_0}^{2}\|\mu_{S_0}^{2}` |
| 47 | 569 | `unsure` | `4\nu'+2+\nu_2\|4\nu'+2\nu_2+1` |
| 48 | 588 | `unsure` | `foncteurs` |
| 48 | 592 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 48 | 600 | `unsure` | `\underline C^{+}\|\underline G^{+}` |
| 48 | 604 | `unsure` | `?` |
| 48 | 604 | `unsure` | `groupe\|groupes` |
| 48 | 604 | `unsure` | `ce n'est pas` |
| 48 | 611 | `unsure` | `cavalier` |
| 48 | 618 | `unsure` | `-\|+` |
| 48 | 620 | `unsure` | `où il` |
| 48 | 620 | `unsure` | `canular` |
| 48 | 629 | `unsure` | `\alpha_0` |
| 49 | 653 | `unsure` | `u\|\underline u` |
| 49 | 654 | `unsure` | `\simeq\|\Vert` |
| 49 | 659 | `unsure` | `saute` |
| 49 | 662 | `unsure` | `\mathbf V\|\mathbb V` |
| 49 | 664 | `illegible` | `1` |
| 49 | 668 | `unsure` | `M` |
| 49 | 676 | `unsure` | `a_1` |
| 49 | 677 | `unsure` | `a_1` |
| 49 | 677 | `unsure` | `a_1\|b_1` |
| 49 | 687 | `unsure` | `-\|+` |
| 49 | 691 | `unsure` | `On` |
| 49 | 692 | `unsure` | `on fera` |
| 49 | 692 | `unsure` | `a_1\|c_1` |
| 49 | 692 | `illegible` | `1` |
| 49 | 699 | `unsure` | `un` |
| 50 | 708 | `unsure` | `\varepsilon_3\|\varepsilon_2` |
| 50 | 716 | `unsure` | `\&` |
| 50 | 731 | `unsure` | `Z` |
| 50 | 735 | `unsure` | `\Gamma\|\mu` |
| 50 | 736 | `unsure` | `\mathbf G_{\mathrm a}` |
| 50 | 738 | `unsure` | `-\|+` |
| 50 | 738 | `unsure` | `\nu_2` |
| 50 | 739 | `unsure` | `1` |
| 50 | 740 | `unsure` | `2\nu'-\nu_2+\nu_3` |
| 50 | 745 | `unsure` | `exprimant\|exigeant` |
| 50 | 745 | `unsure` | `\mu\|\nu` |
| 50 | 745 | `unsure` | `s'écrivent` |
| 50 | 751 | `unsure` | `\left[\vphantom{\begin{matrix}\mu\\\mu\end{matrix}}\right.` |
| 50 | 756 | `unsure` | `-\|+` |
| 50 | 756 | `unsure` | `avec` |
| 50 | 765 | `unsure` | `va\|a` |
| 50 | 776 | `unsure` | `\nu_3` |
| 50 | 777 | `unsure` | `-\|+` |
| 50 | 780 | `unsure` | `lacets\|lacet` |
| 50 | 781 | `unsure` | `\underline{\lambda_1}\|\lambda_1` |
| 51 | 792 | `unsure` | `\widetilde Z_{\rho,\sigma}` |
| 51 | 792 | `unsure` | `révisés` |
| 51 | 792 | `illegible` | `2` |
| 51 | 792 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 792 | `unsure` | `\mathcal O_N^{*}\|\Phi_N^{*}` |
| 51 | 808 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 810 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 821 | `unsure` | `\mathbf E^{1}\|\mathbb E^{1}` |
| 51 | 821 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 825 | `unsure` | `défi` |
| 51 | 828 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 831 | `unsure` | `sur\|dans` |
| 51 | 831 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 835 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 51 | 836 | `unsure` | `k\|x` |
| 51 | 843 | `unsure` | `\xi\|n` |
| 52 | 855 | `unsure` | `n` |
| 52 | 856 | `unsure` | `\lambda'\|\lambda` |
| 52 | 858 | `unsure` | `biad` |
| 52 | 861 | `unsure` | `la\|le` |
| 52 | 861 | `unsure` | `con\|en` |
| 52 | 863 | `unsure` | `\mathcal O_N\|\Phi_N` |
| 52 | 864 | `unsure` | `\mathbb Z\|z` |
| 52 | 865 | `unsure` | `com` |
| 52 | 865 | `unsure` | `unifère\|unitaire` |
| 52 | 866 | `unsure` | `principal` |
| 52 | 869 | `unsure` | `un` |
| 52 | 875 | `unsure` | `NA` |
| 52 | 875 | `unsure` | `NA\|N` |
| 52 | 881 | `unsure` | `S\|S_0` |
| 52 | 881 | `unsure` | `NB\|NA` |
| 52 | 881 | `unsure` | `\xi\to\|p` |
| 53 | 902 | `unsure` | `de` |
| 53 | 909 | `unsure` | `hom.` |
| 53 | 909 | `unsure` | `anneaux` |
| 53 | 917 | `unsure` | `*\|'` |
| 53 | 917 | `unsure` | `passage` |
| 53 | 917 | `unsure` | `s-groupe` |
| 53 | 921 | `unsure` | `\subset\|\subseteq` |
| 53 | 931 | `unsure` | `\mathbb O_N^*\|\mathbb D_N^*` |
| 54 | 940 | `unsure` | `674` |
| 54 | 946 | `unsure` | `\mathbf G_a` |
| 54 | 949 | `unsure` | `hom.` |
| 54 | 949 | `unsure` | `en partie` |
| 54 | 951 | `unsure` | `\mathbb O_N\|\mathbb D_N` |
| 54 | 951 | `unsure` | `\mathbb O_N^*\|\mathbb D_N^*` |
| 54 | 953 | `unsure` | `les` |
| 54 | 953 | `unsure` | `questions` |
| 54 | 953 | `unsure` | `générales\|généralement` |
| 54 | 953 | `unsure` | `hom.` |
| 54 | 957 | `unsure` | `\mathbb O_N^*\|\mathbb D_N^*` |
| 54 | 957 | `unsure` | `\mathbb O_1^*\|\mathbb D_1^*` |
| 54 | 957 | `unsure` | `\mathbb O^*\|\mathbb D^*` |
| 54 | 960 | `unsure` | `\varphi` |
| 54 | 963 | `unsure` | `\varphi` |
| 54 | 963 | `unsure` | `\lambda` |
| 54 | 963 | `unsure` | `ssgt.\|syst.` |
| 54 | 964 | `unsure` | `$+$` |
| 54 | 969 | `unsure` | `sans` |
| 55 | 977 | `unsure` | `dim.\|de dim.` |
| 55 | 979 | `unsure` | `du` |
| 55 | 979 | `unsure` | `groupe` |
| 55 | 979 | `unsure` | `\mathbb O_N^*\|\mathbb D_N^*` |
| 55 | 979 | `unsure` | `parfait` |
| 55 | 985 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 55 | 995 | `unsure` | `le\|la` |
| 55 | 995 | `illegible` | `1` |
| 55 | 995 | `unsure` | `de\|du` |
| 55 | 995 | `unsure` | `groupe\|noyau` |
| 55 | 995 | `unsure` | `sur` |
| 55 | 995 | `unsure` | `\beta` |
| 55 | 999 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 55 | 1003 | `unsure` | `2\|3` |
| 55 | 1003 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 55 | 1004 | `unsure` | `ici` |
| 55 | 1008 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 55 | 1015 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 55 | 1016 | `unsure` | `(+1)\mapsto(0)` |
| 56 | 1025 | `unsure` | `que` |
| 56 | 1029 | `unsure` | `1` |
| 56 | 1029 | `unsure` | `1` |
| 56 | 1043 | `unsure` | `\underline{\mathbb O}_{12}^*\|\underline{\mathbb D}_{12}^*` |
| 56 | 1053 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 56 | 1056 | `unsure` | `12` |
| 56 | 1056 | `unsure` | `\deleted{\lambda_0}\inserted{\nu_0}\|\nu_0` |
| 56 | 1066 | `unsure` | `raisonne` |
| 56 | 1066 | `unsure` | `par\|plus` |
| 56 | 1066 | `unsure` | `mod` |
| 56 | 1084 | `unsure` | `85` |
| 56 | 1086 | `unsure` | `-6` |
| 56 | 1086 | `unsure` | `-8` |
| 56 | 1087 | `unsure` | `(-8)` |
| 56 | 1088 | `unsure` | `-` |
| 56 | 1088 | `unsure` | `\nu_2` |
| 56 | 1093 | `unsure` | `pourrait` |
| 56 | 1095 | `unsure` | `85'\|85` |
| 57 | 1104 | `unsure` | `a` |
| 57 | 1106 | `unsure` | `\deleted{\lambda_0}\inserted{\nu_0}\|\nu_0` |
| 57 | 1109 | `unsure` | `s'intéressant` |
| 57 | 1112 | `unsure` | `-\|+` |
| 57 | 1114 | `unsure` | `par\|pour` |
| 57 | 1114 | `unsure` | `congruence\|congruences` |
| 57 | 1119 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 57 | 1119 | `unsure` | `une` |
| 57 | 1119 | `unsure` | `correspondante\|correspondant` |
| 57 | 1119 | `unsure` | `\mathbb O_1^*\|\mathbb D_1^*` |
| 57 | 1122 | `unsure` | `''` |
| 57 | 1129 | `unsure` | `groupe\|groupes` |
| 57 | 1129 | `unsure` | `\mathbb O_{12}^*\|\mathbb D_{12}^*` |
| 57 | 1129 | `unsure` | `\nu_2\|\xi_2` |
| 57 | 1129 | `unsure` | `,` |
| 57 | 1129 | `unsure` | `\xi_3\|\varepsilon_3` |
| 57 | 1129 | `unsure` | `et` |
| 57 | 1129 | `unsure` | `\mathbb O_1\|\mathbb D_1` |
| 57 | 1129 | `unsure` | `\mu_3\|\nu_3` |
| 57 | 1129 | `unsure` | `*` |
| 57 | 1129 | `unsure` | `\mathbb O_1^*\|\mathbb D_1^*` |
| 57 | 1129 | `unsure` | `\mathbb O_1\|\mathbb D_1` |
| 57 | 1129 | `unsure` | `définies` |
| 57 | 1133 | `unsure` | `image` |
| 57 | 1133 | `unsure` | `\mathbb O_1^*\|\mathbb D_1^*` |
| 57 | 1134 | `unsure` | `\mathbb O_N^*\|\mathbb D_N^*` |
| 57 | 1134 | `unsure` | `\longrightarrow\|\mathrel{-}` |
| 57 | 1134 | `unsure` | `\mathbb O_1^*\|\mathbb D_1^*` |
| 57 | 1137 | `unsure` | `l'image` |
| 57 | 1138 | `unsure` | `\varepsilon_2\|\xi_2` |
| 57 | 1139 | `unsure` | `image` |
| 57 | 1146 | `unsure` | `\Bigg\{` |
| 57 | 1148 | `unsure` | `\mu_0` |
| 57 | 1148 | `unsure` | `\nu_0\|\lambda_0` |
| 57 | 1150 | `unsure` | `[` |
| 57 | 1153 | `unsure` | `\mathbb O_1\|\mathbb D_1` |

## 7. Page coverage and reference

The fragment contains 19 scan markers, in uninterrupted order from 39 through 57. The CSV contains 497 inventoried elements; all entries are marked `yes`. The checks performed on the assembled source include brace balance, paired environments and math delimiters, the requested scan sequence, and the absence of a preamble or embedded scan images. A full TeX compilation was not completed because the available TeX executables lacked their format files; this package supplies the requested source fragment, not a rendered edition.

| Scan | Visible footer counter | Inventoried elements |
|---|---|---|
| 39 | 38 | 23 |
| 40 | 39 | 19 |
| 41 | 40 | 16 |
| 42 | 41 | 25 |
| 43 | 42 | 26 |
| 44 | 43 | 21 |
| 45 | 44 | 34 |
| 46 | 45 | 26 |
| 47 | 46 | 32 |
| 48 | 47 | 21 |
| 49 | 48 | 28 |
| 50 | 49 | 43 |
| 51 | 50 | 29 |
| 52 | 51 | 35 |
| 53 | 52 | 15 |
| 54 | 53 | 18 |
| 55 | 54 | 22 |
| 56 | 55 | 29 |
| 57 | 56 | 35 |

### Primary-source reference (APA style)

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished handwritten manuscript; supplied scans 39–57 of Montpellier archive file, cote 140-4, pages 650bis–787]. Université de Montpellier. [Archive address printed on the scans](https://grothendieck.umontpellier.fr).

Bibliographic identification follows the supplied task prompt and the printed scan footer. Scan citations in these notes use the supplied filenames, not the footer counters.
