# LM_C1-020-037 — Editorial apparatus and research notes

## 1. Source, numbering, and editorial scope

The transcription is based on the 18 supplied JPEG images, whose filenames run from `LM_C1-020-037_scan020.jpg` to `LM_C1-020-037_scan037.jpg`. The task identifies them as Alexander Grothendieck’s *La Longue Marche à travers la théorie de Galois*, brouillon, Montpellier cote 140-1 (catalogued as 1981). The filename number is the `\scanpage` number: the archival folio visible on each image is one lower. The supplied catalogue year does not establish the date of every reused sheet or every mathematical addition.

The circled `7` on scan 20 is retained with `\mspage{7}`. The pencil folios 19–36 are retained with `\margin`, because their attribution and function are not certain. The modern Montpellier URL and address footer are archival apparatus and are excluded. The fragment begins with `\scanpage{20}` and contains no preamble or macro definitions. Standard mathematical LaTeX, TikZ, and tikz-cd are used together with the editorial macros specified in the task; a temporary wrapper defining those macros was used for compilation and visual checking and is not part of the deliverable.

### Whole-sheet exceptions explicitly permitted by the task

| Scan | Visible archival folio | Treatment |
|---|---|---|
| 22 | 21 | `% blank`; the marginal numeral is retained. |
| 24 | 23 | `% not manuscript`: the unrelated printed *Plurielles* film leaflet, with a diagonal stroke; its folio is retained. |
| 26 | 25 | `% not manuscript`: an unrelated printed research-sector classification sheet, headed by printed page number “− 4 −”; its folio is retained. |
| 28 | 27 | `% not manuscript`: the inverted printed thesis-defence notice concerning Yoon Suk-Im’s *Algèbres de Rees*; its folio is retained. |
| 37 | 36 | `% not manuscript`: the inverted, unfilled university thesis-defence form, “ANNEXE II”; its folio is retained. |

These sheets were inspected in full, including rotation where needed. The exception is not applied to mixed sheets: the postal label on scan 27 and the separate sideways billet on scan 34 are transcribed. The latter’s date and uncertain signature belong to that billet, not automatically to the mathematical writing.

Writing sectors with different orientations are read locally upright and retained in scan order. Large cancellation strokes are represented by encompassing `\deleted` groups; smaller cancellations inside them remain separately marked. The exact chronology of overlapping pen strokes is not asserted. Diagrams retain visible node and arrow data, including unfinished expressions, a literal question-mark node, apparent unmatched punctuation, and unexpected signs or inequalities. Layout spacing and label offsets prevent accidental typesetting collisions; they do not supply mathematical relations.

The large Teichmüller glyph is rendered as `\mathcal T` where that is the best reading, but its precise alphabet is not always secure. Doubled D-stems on scans 27 and 29 are rendered `\mathbb D`, whereas thinner forms on scan 31 are rendered ordinary D; this is a visual distinction, not an assertion that the author intended different groups. No published transcription was consulted. External literature cited in §5 was consulted only for a separately labelled research comparison and was not used to settle the French or mathematical readings.

## 2. Table of doubts

Positions refer to the supplied scan, except where a rotated writing sector is identified. Confidence concerns the reading, not the validity of its mathematics. A high-confidence entry can record a surprising but clear mark, such as the lower bar in `n≤6`; low confidence means that the proposed reading remains tentative. “No secure alternative” does not make the proposed reading certain. Repeated occurrences can be grouped here; §2.2 provides a locator for every explicit doubt marker in the final LaTeX.

### 2.1 Contextual register

| Scan | Approximate manuscript line or position | Reading | Alternatives or limitation | Confidence |
|---|---|---|---|---|
| 20 | Main group diagram, repeated glyph | `\mathcal T_{11}` | The handwriting resembles a large tau; the choice of calligraphic T is not fully determined by the pen form. | medium |
| 20 | Symmetric-group glyph in the two right-hand formulas | `\mathfrak S_3` | Script/calligraphic S is another possible alphabet. | medium |
| 20 | Upper-left main sequence, first character | `1` | Small dark mark; could be an unfinished endpoint stroke. | low |
| 20 | Above T_11, overwritten expression | `\Pi_{0,3}^{D}` | Several ink strokes overlap; only the Pi-like form and superscript are tentatively recoverable. | low |
| 20 | Above T_11, slanting underlined words | `identifié à` | Final strokes and attachment overlap the neighboring formula. | medium |
| 20 | Above T_11, small inserted product | `S\mathcal T_{11}\times_{\Pi_{0,3}^{D}}\mathbb Z/12\mathbb Z` | The product connector, subscript attachment, and final modulus are crowded. | low |
| 20 | Below rho_0, above sigma_0 | `\Pi_{0,3}` | Could be an attached subscript rather than a separate scribble. | low |
| 20 | rho tilde maps to 2, deleted glyph | `4` | Heavily overwritten numeral or letter before the final 2. | low |
| 20 | Upper-centre-right annotation | `pour T_11 identifié à` | First word may be `avec`; the ending of `identifié` is abbreviated. | low |
| 20 | Right-hand question, opening | `A-t-on bien` | The A is overwritten and the second word is highly cursive. | medium |
| 20 | Tiny label above Z-to-S T_11 line | `1 - omega bar = omega^2` | A mapsto head is not securely visible; plain dash is the primary reading, mapsto the alternative. | medium |
| 20 | D'3-to-D3 horizontal arrow | `cart` | `can`; the final pen stroke does not securely separate the two labels. | low |
| 20 | Immediately before PM_11 | `\mathcal T_{11}` (deleted) | Could instead be a crossed-out `que` or another abbreviated symbol. | low |
| 20 | Parenthesis below tangent | `PU_{0,3}` | The P is overwritten; the letters U and indices are clearer. | medium |
| 21 | Upper-left parameter array and conjugation equation | `g_i` | `q_i`; the descending loop changes form between occurrences. | medium |
| 21 | Three vertical membership signs, upper-left box | rotated `\in` | These are upward-facing membership signs; the smallest third one overlaps the subscript. | medium |
| 21 | Upper horizontal sequence | `\pi_1(\operatorname{Aut}(X)` | Only one right parenthesis is visible; the apparent unmatched parenthesis is retained, not supplied from expected syntax. | medium |
| 21 | Centre term in upper-left group diagram | `\mathfrak Z\pi` | `\mathfrak z\pi`; the initial glyph has a 3-like form. | low |
| 21 | Middle automorphism column | `\operatorname{Aut}^{+}_{!}(\widetilde X)` | Exclamation-mark subscript clear; the exact placement relative to Aut is cramped. | medium |
| 21 | Two-row extension, top-left term | `\widetilde F` | `\widehat F`; the accent is overwritten. | low |
| 21 | Two-row extension, bottom-left term | deleted `E`, inserted `F` | Several former strokes are superposed; the underlying letter may not be E. | low |
| 21 | Beside G | `\mathfrak S_n\ast\mathbb T^n` | Dot rather than star; no semidirect-product sign has been supplied. | low |
| 21 | Cancelled sentence below extension | `Op. ext. de pi_0 sur F` | Initial abbreviation has an overwritten first letter. | medium |
| 21 | Below pi_1-to-F arrow | `central` | Ending and precise attachment are abbreviated. | medium |
| 21 | Beside curved arrow to centre(F) | `compatible avec pi_0` | First letters intersect a diagonal cancellation. | medium |
| 21 | Lower-right sentence | `extérieurement` | Final syllables are reduced to a long cursive stroke. | medium |
| 21 | Both occurrences of centre(F) | `\mathfrak Z(F)` | `\mathfrak z(F)`; handwriting does not securely settle case/alphabet. | low |
| 21 | Lower-right crossed-out line | `compatible avec l’op. ext.` | The first word is extensively crossed; the remaining words are clearer. | low |
| 21 | Penultimate lower sequence, F | `F` | Lower serif or additional stroke is overwritten; no subscript has been inferred. | medium |
| 21 | Penultimate lower sequence, next-to-last term | `\pi_0` | `\pi_\infty`; the index has an extra loop. | low |
| 21 | Bottom sequence, initial two terms | deleted `1`, deleted `\pi_1` | Both are overwritten, particularly the second term. | low |
| 21 | Below penultimate-sequence pi_0 | Short diagonal slash | Retained beneath the node; it may be an unfinished connector, but no target or arrowhead is supplied. | medium |
| 21 | Large lower-left curved arrows | Arrow paths retained | Their exact textual attachment is less secure than the separate node labels. | low |
| 23 | First line, deleted adjective | `satisfaisant` | `strictement`; the long descender and first few strokes survive, but the middle is struck through. | low |
| 23 | After “Alors” | deleted `H^1` | The overwritten mathematical fragment is not fully recoverable. | low |
| 23 | Parenthesis about characteristic 2 | inserted `pt gén.` | `si gén.`; deletion below appears to read `résiduelle`. The relationship of these short strokes to the deleted word is crowded. | low |
| 23 | Diagonal margin heading | `Dém` | The acute accent and final m support Dém in three independent readings; the initial D has a number-like curl. | high |
| 23 | First marginal cohomology term | `H^1(S_3,H^0(U_03,G_m)` | The outer closing parenthesis is not securely visible and has not been silently supplied. | medium |
| 23 | Final nonzero term in second marginal sequence | `h_1(V(J))` | `h^1(V(J))`; the operator and the small stroke beside h are unclear. | low |
| 23 | Opening of “dis que si” | `Je` | The presumed opening word overlaps the diagonal margin; “dis que si” itself is clear. | low |
| 23 | Overwritten scheme name in definition | deleted `U_{0,3}`, inserted `Sigma_J` | The final Sigma_J is clearer than its cancelled predecessor. | low |
| 23 | At right edge after P(V_J) | `i.e.` | Only a dot and short cursive strokes are clearly resolved. | low |
| 23 | “fibré principal” | `principal` | Several medial and final letters are reduced to strokes. | medium |
| 23 | P Sigma definition | `\check V(\mathcal O_{\Sigma_J}(1))^*` | Sigma_J is written directly below O, inside the parentheses; attachment to O rather than to the outer V is supported by independent close readings. | medium |
| 23 | Generator cohomology arguments | `Sigma_J^*`, `S_J` | Replacements overlap cancelled U_03/S_3-like characters and a correction arrow. | medium |
| 23 | “Je vais d’abord ...” | `trouver` | The word is abbreviated by long connected strokes. | medium |
| 23 | Tensor-bundle comparison | `\mathcal T^{\otimes3}(\omega)` | `\mathcal J^{\otimes3}(\omega)`; the long descending loop does not settle the letter. | low |
| 23 | Slanting insertion below O(6) | `sur Sigma bar tout entier` | The final two words are compressed; no grammatical correction to “toute entière” is made. | low |
| 23 | Deleted parenthetical clause | `ne s’annule que` | The horizontal strike starts after the retained `(qui`; the rising line above qui is treated as an insertion connector. No closing parenthesis is securely visible. | low |
| 23 | Insertion above deleted clause | `est, inversible` | Comma and the final ending of inversible are uncertain. | low |
| 23 | Before Gamma display | deleted `prenant` | Could be `prend`; the ending is struck out. | low |
| 23 | Product section, first two triangular symbols | `\varphi` | `\Delta`; these two symbols have a long descending stem, unlike the clear final Delta in the NB. | medium |
| 23 | Deleted term after product symbol equals | `sum_{i in J}` | The index and crossed summation sign are overwritten. | low |
| 23 | “groupe structural” | `structural` | `structurel`; final letters are compressed. | medium |
| 23 | After “groupe structural” | deleted `de` | Small overwritten word. | low |
| 23 | Lower Sigma_J and P Sigma_J superscripts | `*` | `\wedge`; only two or three strokes are visible. | low |
| 23 | Before invariant algebra | deleted `Sym` | Struck through and retraced. | low |
| 23 | Two generators inside O(...) | `gamma_2`, `gamma_3` | `varphi_2`, `varphi_3`; both letters are overwritten. | low |
| 23 | Gamma_3 product, first sign | minus | plus; the visible horizontal stroke supports minus, and no correction from expected invariant theory is made. | medium |
| 25 | First crossed line, initial word | `Si` | The initial letter and following short stroke are traversed by the cancellation. | medium |
| 25 | First crossed line, after 2 | `inversible` | Several medial letters are hidden by the strike, though the final tall loop and ending survive. | medium |
| 25 | First crossed line, after on | `aura donc` | The two groups of reduced cursive strokes are not securely resolved. | low |
| 25 | Crossed invariant-algebra display | `W_J` | `V_J`; the letter has two visible troughs, favouring W. No surrounding parentheses are securely visible. | low |
| 25 | Same display, group index | `J` | `3`; the small group index is crossed by the long cancellation. | low |
| 25 | Same display, final expression | `O[` | The expression stops after the opening square bracket; no missing generators or closing bracket are supplied. | high |
| 25 | Short crossed line below display | `Remarque` | The first two letters and a final tall stroke are visible, but most of the word is struck through. The final stroke may be t, which weakens the proposed complete reading; no firm alternative is resolved. | low |
| 25 | After first en | deleted `les` | The thick horizontal stroke obscures the final letters. | medium |
| 25 | First vanishing point | `P_omega` | `P_m`; the subscript is a shallow two-lobed form with no clear dot. | low |
| 25 | After O(n)* and before sur | deleted `pour` | A p-like initial descender and rounded terminal stroke support this very tentative reading; mathematical notation cannot be excluded. | low |
| 25 | First Sigma_J superscript | `*` | Wedge; this mark is more wedge-like than the distinct star on O(n)*. | low |
| 25 | Deleted words after Sigma_J | `en degré <` | The words are struck through; the final less-than sign is clearer. | medium |
| 25 | Bound on n | `n <= 6` | The separate lower bar is visible. The weak inequality is retained even though it raises a question when compared with the preceding degree-six construction. | high |
| 25 | After ce qui | `prouve` | The middle and ending are reduced to separated cursive strokes. | medium |
| 25 | Last line before mixte | `H^1` | The H is retraced and the superscript is cramped. | medium |
| 27 | Upper-right square, lower-left node | `M_{11}(\widetilde{2}^{\sim})` | `M_{11}(2^{\sim})`; two separate small strokes around 2 may be retracing rather than two marks | low |
| 27 | Upper-right square, lower-right equality | `M_{11}(2)` | The small argument resembles an n-shaped numeral; no different argument secure | medium |
| 27 | Short cancelled map below square | `x` | Beginning is heavily overwritten; no alternative secure | low |
| 27 | Same cancelled map, target | `x^2\wedge\omega_0` | The operator between the power and the last symbol may be a lambda-like mark; entire target is doubtful | low |
| 27 | Display below the cancelled map | `H^1(TU_{03},\mathbb D_3;\mu_2)` | Initial superscript is poorly separated from H | medium |
| 27 | Middle-left diagram, first diagonal label, deleted | `\mathcal D/\Pi_{0,3}` | The prefix and fraction stroke are overwritten | low |
| 27 | Middle-left diagram, after upper-right `M_{11}(2)` | `-` | Prime | low |
| 27 | Middle-right diagram, two downward labels | `gerbe` | Last letters run together; no alternative secure | medium |
| 27 | Bottom-left diagram, crossed label near upper diagonal | `{1,\omega}` | Deleted strokes overlap the D-label | low |
| 27 | Bottom-left diagram, right downward label | `2-gerbe`, with `gerbe` underlined | Initial mark may be another short prefix; the reading as the numeral 2 is uncertain | low |
| 27 | Bottom-left diagram, left downward label | `2-gerbe` | Same doubtful initial mark as the other downward label | low |
| 27 | Bottom-left diagram, two group names | `Sl(2,\mathbb Z)` | Capitalization of l/L is not securely distinguishable | medium |
| 29 | Cancelled top graph, label on its top incoming arrow | `''` | `1`; two short upright strokes | low |
| 29 | Cancelled top graph, left upper object | `\widetilde\varepsilon` | `\widetilde E` | low |
| 29 | Cancelled top graph, first fibre product | `\mathbb Z/12\mathbb Z` | Middle strokes can also resemble n; numeral 12 is the best reading | medium |
| 29 | Cancelled top graph, subscript of second fibre product | `\mathbb Z/2\mathbb Z` | Slash and numeral overlap; not silently supplied from the preceding product | medium |
| 29 | Cancelled top graph, final object after equality | `\varepsilon` | `E` | medium |
| 29 | Cancelled top graph, lower-left D-object | `\widetilde{\mathbb D}_3^{*}` | `\widetilde{\mathbb D}'_3`; overwritten superscript may be a sharp-like mark | low |
| 29 | Cancelled top graph, long horizontal line from the upper Z | An unheaded line | A worn arrowhead cannot be excluded; the ink does not securely support one | low |
| 29 | Central graph, upper-left object | `\mathbb Z_{(\omega/2)}` | The 2 could instead label the downward arrow; the parenthesis/fraction arrangement is difficult | low |
| 29 | Central graph, first lifted Pi-node | Superscript `\circ` | Small filled mark, possibly 0 | low |
| 29 | Central graph, faint overwritten object after that node | `\widetilde\Pi_{0,3}` | Subscript is very faint beneath the horizontal stroke | low |
| 29 | Central graph, second lifted Pi-node | Superscript prime | Small grey stroke might be another annotation | low |
| 29 | Central graph, beneath `\mathbb D''_3` | `12` | `10`; pale earlier annotation | low |
| 29 | Left of the final Z in the central graph | `fond` | `bon`; short crowded word | low |
| 29 | Central graph, between Z/12Z and Z/6Z | Bidirectional horizontal arrow, label 2 | Two oppositely directed heads appear on separated stretches of the line; no algebraic interpretation is imposed | medium |
| 29 | Lower two-row sequence, downward Z-map | A second `4` below the clear 4 | May be a repeated pen stroke rather than a separate annotation | low |
| 29 | Bottom row, group at the right of the literal `?` | `Sl(2,\mathbb Z)` | First letters have been retraced | medium |
| 30 | Top line, cancelled mark after `V_J` | `\simeq` | Could be a failed initial symbol rather than a completed relation | low |
| 30 | Top-line insertion | `\Gamma(X,\uline{\mathcal O}(1))` | Opening parenthesis merges with the Gamma-like letter; the underline on O is visible | low |
| 30 | Top line | `engendré` | Final letters compressed | medium |
| 30 | Cancelled expression starting next line | `\Pi(e_i-e_j)` | `P(e_i-e_j)`; initial letter is crossed and retraced | low |
| 30 | Upper prose, first word | `comment` | Several medial letters are only strokes | medium |
| 30 | Upper prose | `sections` | Final letters compressed | medium |
| 30 | Upper prose | `sont` | Short word represented by a low connected stroke | low |
| 30 | Upper prose, following line | `permutées` | Several retraced letters; no secure alternative | low |
| 30 | Cancelled display left of `e_i-e_j=` | `\mathcal O(6)` | `\mathcal O(1)` | low |
| 30 | Isolated symbol below that display | `\xi_i.` | Subscript and final point not fully separated | low |
| 30 | Upper-right calculation, fibre notation | `\uline{\mathcal O}_x(1)` | Subscript a | low |
| 30 | Below the same fibre notation | Vertically oriented `\in` | Shape resembles a small upsilon/psi because of orientation | medium |
| 30 | Middle-left extension, subscript of lifted Pi | `03` | Small compressed loop; no comma confidently visible | low |
| 30 | Same extension, superscript of unlifted Pi | `\sharp` | `\ast`; superscript is overdrawn | low |
| 30 | Middle-right evaluation, underlined point | `Q_n` | `Q_k`; the Q-like glyph is highly cursive | low |
| 30 | Crossed expression beneath that evaluation | `e_i-e_j` | Middle strokes are obscured by cancellation | low |
| 30 | Expression above the small numerical array | `e_i-e_j(Q_k` | The Q-like symbol is cancelled; no closing parenthesis is securely visible and none was added | low |
| 30 | Lower, rotated, first sentence: deletion | `surface` | Most of the first half is concealed by the cancellation | low |
| 30 | Lower, rotated, above first sentence | `cellulation` | `cellulaire`; placed after the deleted noun and before “combinatoire” | low |
| 30 | Lower, rotated, beginning of second line | `donne` | Medial letters reduced to strokes | medium |
| 30 | Lower, rotated, after “lieu” | `à` | Colon | low |
| 30 | Lower, rotated, first paragraph and question | `opérateurs` | `opérations`; the ending is uncertain | low |
| 30 | Lower, rotated, before first displayed relation | `satisfaisant` | Final inflection is only a short stroke | medium |
| 30 | Lower, rotated, orientation question | `quels` | `quelles` | low |
| 30 | Lower, rotated, orientation question | `correspondants` | `correspondantes` | low |
| 30 | Lower, rotated, two occurrences before representatives | `provient` | Final t/n/t strokes are compressed | medium |
| 30 | Lower, rotated, repeated involution subscript | `m` | `n`; every occurrence is marked, and the choice was not derived from an expected presentation | low |
| 30 | Lower, rotated, before “la classe” | `donc` | Final letters reduced to a wavering line | medium |
| 30 | Lower, rotated, before “t on a donc” | Deleted `E` | A heavily retraced initial E may not be an intentional deletion | low |
| 30 | Lower, rotated, last parenthesis | `plaisant` | Ending almost entirely a horizontal stroke | low |
| 30 | Lower, rotated, transverse right marginal note, first term | `\widetilde Q_m` | `\widetilde R_m`; initial glyph and subscript both uncertain | low |
| 30 | Same marginal note, second term | `\widetilde Q_j` | `\widetilde R_j` | low |
| 30 | Transverse note, cancelled initial symbol on second line | `\xi` | No alternative secure | low |
| 30 | Transverse note, second line | `\gamma_h\ i\gamma_h` | Gamma-like glyphs and their subscripts are not securely identified | low |
| 30 | Transverse difference calculation | `=` | A separate equality sign is not securely resolved from the short strokes | low |
| 30 | Same calculation, last subscript | `j` | `n` | low |
| 31 | Top cancelled sequence, lower target | `D''_3` | Initial part of D is heavily overwritten | low |
| 31 | Upper kernel equality, after the right `\Pi_0` | Raised point | Prime | low |
| 31 | Main graph, lifted D subscript | `3` | `0` | low |
| 31 | Above the middle exact sequence, cancelled symbol before Z | `\widetilde\Pi` | Mark above Pi is crowded by cancellation | low |
| 31 | Middle sequence, cancelled lower branch | `D_3` | Stem and subscript are crossed through | low |
| 31 | Bottom display between Pi-prime and Pi | `\subset` | Leftward arrow | low |
| 31 | Bottom-left cancelled product, first factor | `\widetilde\Pi` | Tilde and letter partially overwritten | low |
| 31 | Same cancelled product, final factor | `\mathbb Z/4` | `\mathbb Z/4\mathbb Z`; no separate terminal Z is securely resolved | low |
| 32 | 1, over « construction » | inserted « ne » | abbreviated correction, attachment uncertain | low |
| 32 | 1 | « peut se continuer indéfiniment » | compressed word endings | medium |
| 32 | 2–3 | « on pose alors σa_n = ρa_0 » | final index on a may be n rather than 0 | medium |
| 32 | 4 | « se prolonge indéfiniment » | compressed final letters | medium |
| 32 | 5, deleted parenthesis | « soit que l'on ... a un cycle fini » with « donc » added | wording heavily obscured by cancellation | low |
| 32 | 6 | « ou un cycle infini » | finite/infinite cycle wording | low |
| 32 | 6 | « On ne définit pas ρâ alors » | a rather than â; entire clause compressed | low |
| 32 | upper left marginal bracket | « notion de connexité définie dans un sens restreint » | individual words uncertain | low |
| 32 | 7 | « prolongé », replacing « défini » | annotation is compressed and overlaps the cancellation | low |
| 32 | 7–8 | « sur tt A et que = pour l'orientation inverse » | « tt » or quantifier; the short sign after « que » uncertain | low |
| 32 | 9 | « propriétés combinatoires » | word ending compressed | medium |
| 32 | 10 | « autom. » | « action » | low |
| 32 | 10–11 | bar S and hat S; subset sign | equality sign in the latter position | low |
| 32 | 12 | « compactifier partiellement X en X̂ » | Final letters remain faint; « compléter ponctuellement » is less well supported by the enlarged strokes. | medium |
| 32 | 13–14 | « ajoutant les pts ... (ainsi que : K°) » | K° and inserted Π₀,₃ reading uncertain | low |
| 32 | 14–16 | « l'image inverse Â′ ... contient A′ et ... st. ∀ par ρ et σ » | short stability notation uncertain | low |
| 32 | 16–17, cancellation and insertion | « mais n’est pas néc. égal à A′ »; inserted « A tt entier » | « ce n’est pas »; « avec »; inserted « A est entier ». The longer reading « A est engendré par A′ » is not supported and is not in the transcription. | low |
| 32 | lower left circled note | « st. liberté de l'action en passant de A′ : Â′ ? » | question and relation sign uncertain | low |
| 32 | 18–20 | « satisfaisant ... doivent ... s’identifier » | « s’identifient »; the short word tentatively read « doivent » is not secure, so it does not settle the following ending. | medium |
| 32 | 21 | « ens. quelc. » | final abbreviated word uncertain | medium |
| 32 | 23 | « On retrouve A′ comme l'ens des él. » | « retrouve » compressed | medium |
| 33 | top diagram, downward arrow to Z/qZ | « nul sur Π̃₀, can sur Zω̄ » | short words and placement of bar uncertain | medium |
| 33 | top right, deleted formula | β ∈ (Z/qZ)* | initial letter heavily crossed | low |
| 33 | middle diagram, bottom horizontal arrow | q | tiny superscript-like label could be two strokes rather than q | low |
| 33 | deleted heading above class formula | « L'extension est [one unreadable word] : » | heavy cancellation makes final word unrecoverable | low |
| 33 | extension-class formulas | ζ, ζ′ | ξ, ξ′ | low |
| 33 | first class formula | Ext¹ with deleted Z subscript | power/subscript interwoven with correction | low |
| 33 | pullback formula | cl(Π̃₀(q)) followed by prime | cl(Π̃₀ q); final small stroke possibly punctuation | medium |
| 33 | bottom right and final left formula | δ* | δ′ | medium |
| 34 | top deleted line | « 4) SL̃(2,Z) ≃ T₁,₁ SL Π » | heavily overwritten group symbols; initial number uncertain | low |
| 34 | top identity, fibre-product subscript | Z/6Z | first Z overwritten | medium |
| 34 | below top identity, small cancelled symbol | α | scribble has no certain recovery | low |
| 34 | inverted network, branch from top edge | Π → D₃″ → Z/ | final quotient label unfinished; double stroke on D uncertain | low |
| 34 | inverted network, separate right-hand label | Π₀ × 7 | Π₀ × 1 | low |
| 34 | inverted lower square | underlined « cart » | « can » | medium |
| 34 | sideways reused-paper note, signature | R. Boucher | surname uncertain | low |
| 35 | numeric specialization, crossed symbols | p; p′+ | overwritten remnants | low |
| 35 | below circled −α | cancelled φ | partly overwritten symbol | low |
| 35 | prose beside residue map | « revêt » plus cancelled « ement » | abbreviation or cancelled ending unclear | low |
| 35 | prose, last two lines | « multisection canonique de O_U(4)* » | « multiplication »; numeral 1; earlier deleted O(1) notation uncertain | medium |
| 35 | left inclusion diagram, lower label | μ₆-revᵗ | superscript or overwritten end of « revêt » | low |
| 35 | left inclusion diagram, isolated mark | + | small ink stroke not certainly a plus | low |
| 35 | central diagram, bottom horizontal arrow | equality label | short bar may be part of retraced arrow | low |
| 35 | lower left cancelled formula | Π̃₀,₃ᴰ Z/4Z → | symbols heavily crossed; no recovery of a connecting operation | low |
| 35 | generator definitions near foot | ρ̃♯ and σ̃♯ | primed generators, or another superscript | low |
| 35 | last presentation, underbrace | ω′⁻¹ = ω | ω̃⁻¹ = ∞; annotation heavily overwritten | low |
| 35 | last presentation, cancelled clause | ω ∈ Z | fully overdrawn initial relation sign | low |
| 36 | above first Z | ω′ = ω⁻¹ | ω′ = ω̄′; superscript placement favours inverse | medium |
| 36 | after presentation above SΠ₀,₃ᴰ | cancelled ω | cancelled ∞ or further central-symbol annotation | low |
| 36 | upper-right NB, first factor | dotted ω̄⁴ | ω̄⁴ with stray dot above the bar | low |
| 36 | upper-right NB, central factor | ω⁻¹ | overwritten omega may have additional decoration | medium |
| 36 | after final ω′ in NB | cancelled ω | no certain recovery of overdrawn symbol | low |
| 35 | very pale marks immediately right of residue rows | Γ / √, ξ₀′ / ξ₀, t′r / t′h | may be verso show-through or erased pencil; not attributed to the front-page argument | low |

### 2.2 Locator index of explicit uncertainty marks

This index is exhaustive for `\unsure` and `\illegible` in the delivered fragment. “LaTeX line” identifies the physical line of that file, not a reconstructed manuscript line; use the scan and contextual register above for the manuscript location. Contents are recorded literally, so a vertical bar separates proposed readings as specified in the task. The single `\illegible{1}` concerns a deleted prose word on scan 33, not a mathematical symbol.

| Scan | LaTeX line | Macro | Literal contents |
|---|---|---|---|
| 20 | 15 | `\unsure` | `\Pi_{0,3}^{D}` |
| 20 | 16 | `\unsure` | `identifié à` |
| 20 | 17 | `\unsure` | `S\mathcal T_{11}\times_{\Pi_{0,3}^{D}}\mathbb Z/12\mathbb Z` |
| 20 | 23 | `\unsure` | `\Pi_{0,3}` |
| 20 | 28 | `\unsure` | `1` |
| 20 | 29 | `\unsure` | `-\|\mapsto` |
| 20 | 30 | `\unsure` | `4` |
| 20 | 36 | `\unsure` | `cart\|can` |
| 20 | 46 | `\unsure` | `pour` |
| 20 | 46 | `\unsure` | `identifié à` |
| 20 | 49 | `\unsure` | `A-t-on` |
| 20 | 49 | `\unsure` | `bien` |
| 20 | 54 | `\unsure` | `\mathcal T_{11}` |
| 20 | 58 | `\unsure` | `PU_{0,3}` |
| 21 | 72 | `\unsure` | `g_i\|q_i` |
| 21 | 80 | `\unsure` | `g_i\|q_i` |
| 21 | 80 | `\unsure` | `g_i\|q_i` |
| 21 | 91 | `\unsure` | `\mathfrak Z\pi\|\mathfrak z\pi` |
| 21 | 124 | `\unsure` | `\widetilde F\|\widehat F` |
| 21 | 125 | `\unsure` | `E` |
| 21 | 126 | `\unsure` | `\ast\|\cdot` |
| 21 | 130 | `\unsure` | `Op.` |
| 21 | 133 | `\unsure` | `compatible` |
| 21 | 134 | `\unsure` | `\mathfrak Z(F)\|\mathfrak z(F)` |
| 21 | 136 | `\unsure` | `central` |
| 21 | 138 | `\unsure` | `extérieurement` |
| 21 | 139 | `\unsure` | `\mathfrak Z(F)\|\mathfrak z(F)` |
| 21 | 145 | `\unsure` | `compatible` |
| 21 | 157 | `\unsure` | `F` |
| 21 | 157 | `\unsure` | `\pi_0\|\pi_\infty` |
| 21 | 161 | `\unsure` | `1` |
| 21 | 161 | `\unsure` | `\pi_1` |
| 23 | 172 | `\unsure` | `satisfaisant\|strictement` |
| 23 | 174 | `\unsure` | `H^1` |
| 23 | 178 | `\unsure` | `résiduelle` |
| 23 | 178 | `\unsure` | `pt gén.\|si gén.` |
| 23 | 180 | `\unsure` | `Dém` |
| 23 | 187 | `\unsure` | `h_1(V(J))\|h^1(V(J))` |
| 23 | 190 | `\unsure` | `Je` |
| 23 | 191 | `\unsure` | `U_{0,3}` |
| 23 | 191 | `\unsure` | `i.e.` |
| 23 | 195 | `\unsure` | `principal` |
| 23 | 200 | `\unsure` | `U_{0,3}` |
| 23 | 201 | `\unsure` | `\mathfrak S_3` |
| 23 | 203 | `\unsure` | `trouver` |
| 23 | 206 | `\unsure` | `\mathcal T^{\otimes3}(\omega)\|\mathcal J^{\otimes3}(\omega)` |
| 23 | 209 | `\unsure` | `tout entier` |
| 23 | 210 | `\unsure` | `ne s'annule que` |
| 23 | 211 | `\unsure` | `est` |
| 23 | 211 | `\unsure` | `inversible` |
| 23 | 212 | `\unsure` | `prenant` |
| 23 | 219 | `\unsure` | `\varphi\|\Delta` |
| 23 | 220 | `\unsure` | `\varphi\|\Delta` |
| 23 | 221 | `\unsure` | `\sum_{i\in J}` |
| 23 | 226 | `\unsure` | `U_J` |
| 23 | 226 | `\unsure` | `*\|\wedge` |
| 23 | 226 | `\unsure` | `structural\|structurel` |
| 23 | 227 | `\unsure` | `de` |
| 23 | 228 | `\unsure` | `*\|\wedge` |
| 23 | 232 | `\unsure` | `\operatorname{Sym}` |
| 23 | 234 | `\unsure` | `\gamma_2\|\varphi_2` |
| 23 | 234 | `\unsure` | `\gamma_3\|\varphi_3` |
| 23 | 240 | `\unsure` | `-\|+` |
| 25 | 253 | `\unsure` | `Si` |
| 25 | 253 | `\unsure` | `inversible` |
| 25 | 253 | `\unsure` | `aura` |
| 25 | 253 | `\unsure` | `donc` |
| 25 | 255 | `\unsure` | `W_J\|V_J` |
| 25 | 255 | `\unsure` | `J\|3` |
| 25 | 257 | `\unsure` | `Remarque` |
| 25 | 259 | `\unsure` | `les` |
| 25 | 259 | `\unsure` | `\omega\|m` |
| 25 | 261 | `\unsure` | `pour` |
| 25 | 262 | `\unsure` | `*\|\wedge` |
| 25 | 262 | `\unsure` | `en degré` |
| 25 | 266 | `\unsure` | `prouve` |
| 25 | 267 | `\unsure` | `H^1` |
| 27 | 292 | `\unsure` | `\widetilde{2}^{\sim}\|2^{\sim}` |
| 27 | 294 | `\unsure` | `2` |
| 27 | 299 | `\unsure` | `x` |
| 27 | 299 | `\unsure` | `x^2\wedge\omega_0` |
| 27 | 302 | `\unsure` | `H^1` |
| 27 | 307 | `\unsure` | `\mathcal D/\Pi_{0,3}` |
| 27 | 308 | `\unsure` | `-\|'` |
| 27 | 316 | `\unsure` | `\mathrm{gerbe}` |
| 27 | 317 | `\unsure` | `\mathrm{gerbe}` |
| 27 | 328 | `\unsure` | `\{1,\omega\}` |
| 27 | 329 | `\unsure` | `2\text{-}\uline{\mathrm{gerbe}}` |
| 27 | 330 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 27 | 331 | `\unsure` | `2\text{-}\mathrm{gerbe}` |
| 27 | 334 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 29 | 346 | `\unsure` | `''\|1` |
| 29 | 349 | `\unsure` | `\widetilde\varepsilon\|\widetilde E` |
| 29 | 352 | `\unsure` | `12` |
| 29 | 353 | `\unsure` | `2` |
| 29 | 357 | `\unsure` | `\varepsilon\|E` |
| 29 | 363 | `\unsure` | `\widetilde{\mathbb D}_3^{*}\|\widetilde{\mathbb D}'_3` |
| 29 | 376 | `\unsure` | `\mathbb Z_{(\omega/2)}` |
| 29 | 377 | `\unsure` | `\circ` |
| 29 | 378 | `\unsure` | `\widetilde\Pi_{0,3}` |
| 29 | 382 | `\unsure` | `'` |
| 29 | 394 | `\unsure` | `12\|10` |
| 29 | 403 | `\unsure` | `fond\|bon` |
| 29 | 407 | `\unsure` | `4` |
| 29 | 433 | `\unsure` | `\mathrm{Sl}(2,\mathbb Z)` |
| 30 | 442 | `\unsure` | `\simeq` |
| 30 | 442 | `\unsure` | `\Gamma(X,\uline{\mathcal O}(1))` |
| 30 | 443 | `\unsure` | `engendré` |
| 30 | 445 | `\unsure` | `\Pi(e_i-e_j)\|P(e_i-e_j)` |
| 30 | 446 | `\unsure` | `comment` |
| 30 | 446 | `\unsure` | `sections` |
| 30 | 446 | `\unsure` | `sont` |
| 30 | 447 | `\unsure` | `permutées` |
| 30 | 466 | `\unsure` | `\mathcal O(6)\|\mathcal O(1)` |
| 30 | 470 | `\unsure` | `\xi_i` |
| 30 | 474 | `\unsure` | `\uline{\mathcal O}_x(1)\|\uline{\mathcal O}_a(1)` |
| 30 | 474 | `\unsure` | `\in` |
| 30 | 481 | `\unsure` | `03` |
| 30 | 482 | `\unsure` | `\sharp\|\ast` |
| 30 | 487 | `\unsure` | `Q_n\|Q_k` |
| 30 | 488 | `\unsure` | `e_i-e_j` |
| 30 | 494 | `\unsure` | `Q_k` |
| 30 | 510 | `\unsure` | `surface` |
| 30 | 511 | `\unsure` | `cellulation\|cellulaire` |
| 30 | 512 | `\unsure` | `donne` |
| 30 | 512 | `\unsure` | `à\|:` |
| 30 | 512 | `\unsure` | `opérateurs\|opérations` |
| 30 | 513 | `\unsure` | `satisfaisant` |
| 30 | 518 | `\unsure` | `quels\|quelles` |
| 30 | 519 | `\unsure` | `opérateurs\|opérations` |
| 30 | 519 | `\unsure` | `correspondants\|correspondantes` |
| 30 | 521 | `\unsure` | `provient` |
| 30 | 522 | `\unsure` | `provient` |
| 30 | 522 | `\unsure` | `m\|n` |
| 30 | 524 | `\unsure` | `m\|n` |
| 30 | 525 | `\unsure` | `m\|n` |
| 30 | 526 | `\unsure` | `m\|n` |
| 30 | 526 | `\unsure` | `m\|n` |
| 30 | 527 | `\unsure` | `m\|n` |
| 30 | 528 | `\unsure` | `m\|n` |
| 30 | 530 | `\unsure` | `donc` |
| 30 | 530 | `\unsure` | `m\|n` |
| 30 | 533 | `\unsure` | `E` |
| 30 | 535 | `\unsure` | `m\|n` |
| 30 | 536 | `\unsure` | `m\|n` |
| 30 | 537 | `\unsure` | `m\|n` |
| 30 | 537 | `\unsure` | `m\|n` |
| 30 | 538 | `\unsure` | `m\|n` |
| 30 | 550 | `\unsure` | `plaisant` |
| 30 | 556 | `\unsure` | `\widetilde Q_m\|\widetilde R_m` |
| 30 | 557 | `\unsure` | `\widetilde Q_j\|\widetilde R_j` |
| 30 | 560 | `\unsure` | `\xi` |
| 30 | 560 | `\unsure` | `\gamma_h\ i\gamma_h` |
| 30 | 563 | `\unsure` | `=` |
| 30 | 563 | `\unsure` | `j\|n` |
| 31 | 577 | `\unsure` | `D''_3` |
| 31 | 582 | `\unsure` | `.` |
| 31 | 588 | `\unsure` | `3\|0` |
| 31 | 603 | `\unsure` | `\widetilde\Pi` |
| 31 | 612 | `\unsure` | `D_3` |
| 31 | 632 | `\unsure` | `\subset\|\leftarrow` |
| 31 | 635 | `\unsure` | `\widetilde\Pi` |
| 31 | 635 | `\unsure` | `\mathbb Z/4\|\mathbb Z/4\mathbb Z` |
| 32 | 647 | `\unsure` | `ne` |
| 32 | 647 | `\unsure` | `peut` |
| 32 | 647 | `\unsure` | `indéfiniment` |
| 32 | 648 | `\unsure` | `pose` |
| 32 | 651 | `\unsure` | `indéfiniment` |
| 32 | 653 | `\unsure` | `soit que` |
| 32 | 653 | `\unsure` | `l'on` |
| 32 | 653 | `\unsure` | `donc` |
| 32 | 653 | `\unsure` | `a un cycle fini` |
| 32 | 653 | `\unsure` | `ou un` |
| 32 | 654 | `\unsure` | `infini` |
| 32 | 654 | `\unsure` | `définit` |
| 32 | 654 | `\unsure` | `\widehat a\|a` |
| 32 | 654 | `\unsure` | `alors` |
| 32 | 657 | `\unsure` | `notion de connexité` |
| 32 | 657 | `\unsure` | `définie dans un` |
| 32 | 657 | `\unsure` | `sens restreint` |
| 32 | 662 | `\unsure` | `défini` |
| 32 | 662 | `\unsure` | `prolongé` |
| 32 | 662 | `\unsure` | `tt` |
| 32 | 663 | `\unsure` | `$=$` |
| 32 | 663 | `\unsure` | `inverse` |
| 32 | 664 | `\unsure` | `combinatoires` |
| 32 | 665 | `\unsure` | `autom.` |
| 32 | 665 | `\unsure` | `\overline S` |
| 32 | 666 | `\unsure` | `\subset\|=` |
| 32 | 667 | `\unsure` | `compactifier` |
| 32 | 667 | `\unsure` | `partiellement` |
| 32 | 667 | `\unsure` | `$\overline X$` |
| 32 | 668 | `\unsure` | `ajoutant` |
| 32 | 669 | `\unsure` | `K^\circ` |
| 32 | 669 | `\unsure` | `$\simeq\Pi_{0,3}$` |
| 32 | 670 | `\unsure` | `contient $A'$ et` |
| 32 | 671 | `\unsure` | `st.` |
| 32 | 671 | `\unsure` | `$\forall$` |
| 32 | 672 | `\unsure` | `n'est pas\|ce n'est pas` |
| 32 | 672 | `\unsure` | `à\|avec` |
| 32 | 673 | `\unsure` | `tt entier\|est entier` |
| 32 | 676 | `\unsure` | `st. liberté de l'action` |
| 32 | 676 | `\unsure` | `en passant de` |
| 32 | 685 | `\unsure` | `satisfaisant` |
| 32 | 686 | `\unsure` | `doivent` |
| 32 | 687 | `\unsure` | `s'identifier\|s'identifient` |
| 32 | 687 | `\unsure` | `triples` |
| 32 | 688 | `\unsure` | `quelc.` |
| 32 | 690 | `\unsure` | `retrouve` |
| 33 | 698 | `\unsure` | `nul sur ` |
| 33 | 698 | `\unsure` | `can sur ` |
| 33 | 703 | `\unsure` | `\beta` |
| 33 | 708 | `\unsure` | `q` |
| 33 | 717 | `\unsure` | `L'extension est` |
| 33 | 717 | `\illegible` | `1` |
| 33 | 719 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 719 | `\unsure` | `\zeta\|\xi` |
| 33 | 721 | `\unsure` | `1` |
| 33 | 721 | `\unsure` | `\mathbb Z` |
| 33 | 725 | `\unsure` | `=` |
| 33 | 726 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 728 | `\unsure` | `(q)\|q` |
| 33 | 728 | `\unsure` | `\zeta\|\xi` |
| 33 | 729 | `\unsure` | `'` |
| 33 | 732 | `\unsure` | `\zeta\|\xi` |
| 33 | 739 | `\unsure` | `\zeta'\|\xi'` |
| 33 | 741 | `\unsure` | `*\|' ` |
| 33 | 742 | `\unsure` | `*\|'` |
| 34 | 748 | `\unsure` | `4)` |
| 34 | 748 | `\unsure` | `\widetilde{\mathrm{SL}}` |
| 34 | 749 | `\unsure` | `\mathcal T_{1,1}` |
| 34 | 749 | `\unsure` | `\mathrm{SL}` |
| 34 | 749 | `\unsure` | `\Pi` |
| 34 | 758 | `\unsure` | `\mathbb Z/6\mathbb Z` |
| 34 | 762 | `\unsure` | `\alpha` |
| 34 | 770 | `\unsure` | `\Pi` |
| 34 | 773 | `\unsure` | `\mathbb Z/` |
| 34 | 776 | `\unsure` | `7\|1` |
| 34 | 779 | `\unsure` | `cart` |
| 34 | 790 | `\unsure` | `Boucher` |
| 35 | 801 | `\unsure` | `p` |
| 35 | 804 | `\unsure` | `p'+` |
| 35 | 825 | `\unsure` | `\varphi` |
| 35 | 827 | `\unsure` | `\Gamma\|\sqrt{\phantom{x}}` |
| 35 | 827 | `\unsure` | `\xi_0\prime\|\xi_0` |
| 35 | 827 | `\unsure` | `t\prime r\|t\prime h` |
| 35 | 830 | `\unsure` | `revêt` |
| 35 | 830 | `\unsure` | `ement` |
| 35 | 832 | `\unsure` | `multisection\|multiplication` |
| 35 | 833 | `\unsure` | `\mathcal O(1)` |
| 35 | 833 | `\unsure` | `4\|1` |
| 35 | 839 | `\unsure` | `(1)` |
| 35 | 841 | `\unsure` | `\mathrm{rev}^{\mathrm t}` |
| 35 | 841 | `\unsure` | `+` |
| 35 | 844 | `\unsure` | `\longrightarrow` |
| 35 | 849 | `\unsure` | `=` |
| 35 | 860 | `\unsure` | `\widetilde\Pi_{0,3}^D` |
| 35 | 860 | `\unsure` | `\mathbb Z/4\mathbb Z` |
| 35 | 863 | `\unsure` | `\sharp\|'` |
| 35 | 864 | `\unsure` | `\sharp` |
| 35 | 864 | `\unsure` | `\sharp` |
| 35 | 865 | `\unsure` | `\sharp\|'` |
| 35 | 872 | `\unsure` | `\omega'^{-1}\|\widetilde\omega^{-1}` |
| 35 | 872 | `\unsure` | `\omega\|\infty` |
| 35 | 873 | `\unsure` | `\omega\in\mathbb Z` |
| 36 | 880 | `\unsure` | `\omega\|\infty` |
| 36 | 881 | `\unsure` | `\omega^{-1}\|\overline\omega'` |
| 36 | 886 | `\unsure` | `\dot{\overline\omega}\|\overline\omega` |
| 36 | 886 | `\unsure` | `\omega^{-1}` |
| 36 | 887 | `\unsure` | `\omega` |

## 3. Abbreviations met

Expansions in this table are editorial suggestions only. They have not been substituted into the diplomatic transcription. Mathematical initials whose verbal expansion is not supplied securely are left unexplained.

| Form as written | Tentative expansion or meaning | Scan(s) |
|---|---|---|
| `can` | canonique | 20, 29, 33 |
| `cart`, `Cart` | cartésien / cartésienne; some readings remain doubtful | 20, 27, 34 |
| `Aut` | automorphismes | 21 |
| `SAut` | Probably a group of automorphismes fixing boundary data; the initial S is not securely expanded | 21 |
| `Op.`, `op.` | opération / opère, depending on the note | 21 |
| `ext.` | extérieure / extérieurement | 21 |
| `Pic` | groupe de Picard | 23 |
| `car.` | caractéristique | 23 |
| `pt gén.` (uncertain) | point générique | 23 |
| `Dém` | démonstration | 23 |
| `i.e.` | id est, « c’est-à-dire »; one occurrence is uncertain | 23, 30, 32 |
| `NB` | nota bene | 23, 36 |
| `Sym` | algèbre / puissance symétrique, according to the exponent | 23, 25 |
| `cl` | classe | 25, 33 |
| `MR` | Monsieur; printed postal-label abbreviation | 27 |
| `ALEX.` | Alexander / Alexandre; abbreviated given name on the postal label | 27 |
| `gal` | galoisien / galoisienne | 27 |
| `mod` | modulo | 30, 35 |
| `int` | intérieur; conjugation notation | 30 |
| `Sl`, `SL` | Special linear group notation; differences in case are preserved, not silently standardized | 27, 29, 34 |
| `PM`, `PU`, `TU` | No secure verbal expansion supplied by these pages; retained as mathematical notation | 20, 27, 35 |
| `tt` (uncertain) | tout | 32 |
| `autom.` | automorphisme | 32 |
| `pts` | points | 32 |
| `st.` (uncertain) | stable / stabilité, depending on context | 32 |
| `néc.` | nécessairement | 32 |
| `ens.`, `ens` | ensemble | 32 |
| `ss pt fixe` | sans point fixe | 32 |
| `quelc.` | quelconque | 32 |
| `él.` | éléments | 32 |
| `hom. can.` | homomorphisme canonique | 33 |
| `pr` | projection | 33 |
| `Ext` | Extension-functor notation | 33 |
| `M.` | Monsieur; in the separate reused-paper billet | 34 |
| `revêt`, `revᵗ` (uncertain) | revêtement | 35 |

## 4. Legibility and limits

The main objects in the group diagrams are generally more legible than their small labels, overwritten decorations, and surrounding prose. The least secure continuous passage is the faint text on scan 32, especially its parenthesis, marginal notes, and overlapping corrections. Scan 30 is also difficult because it combines two writing orientations, compressed French, and transverse marginal calculations. Small annotations above scan 20’s first diagram, the cancelled prose on scan 21, the diagonal and corrected passages on scan 23, and the cancelled opening of scan 25 require particular editorial caution.

The manuscript’s apparent quotient in scan 23’s NB, its minus-first candidate for the γ₃ factor, the distinction between a stemmed φ-like symbol and the final Δ, and scan 25’s weak inequality `n≤6` are preserved rather than made consistent with expected mathematics. The extremely pale marks beside scan 35’s residue rows are retained as uncertain marginal marks and may instead be verso show-through. The supplied resolution and overwritten ink do not permit a definitive edition: the transcription is complete in coverage, but the marked readings and the attribution or scope of some strokes remain open. Every scan was inventoried and compared with its transcription; all inventory rows are marked `yes`, meaning represented, not certain.

## 5. Research notes — English, separate from the transcription

These items identify questions for subsequent checking against the surrounding manuscript and the literature. They do not establish novelty, complete the author’s proofs, or alter the transcription. All scan-specific quotations and claims refer to the supplied primary images (Grothendieck, 1981, indicated scan); the year is the task’s catalogue designation. “Unproved claim” means that a complete proof is not given on these supplied pages, even where a sketch or calculation is present. Items labelled “own idea” are editorial proposals with their confidence and reason stated.

1. **Scan 20, right upper-middle; conjecture (explicit question).** The explicit question “A-t-on [bien]” followed by `S T_11 ≃ S Pi^D_03 ??` asks whether two central-extension objects agree. Any investigation must first settle precisely which projections and identifications the crowded upper diagram assigns to these symbols; the double question mark is not a proof or assertion.

2. **Scan 20, right middle and lower; conjecture (expectation).** “il semblerait plutôt, pourtant” introduces a tentative comparison `PM_11 ≃ (T*U_03, S_3)`, followed by a proposed fundamental-group identification. The annotation “fibré tangent (et non PU_03 !!)” makes the distinction between the indicated tangent object and the P-object worth checking, without changing either symbol in the transcription.

3. **Scan 20, main diagram; unproved claim.** Several regions are labelled “cart”/“Cart” and several arrows “can”. A verification would require definitions of the displayed group homomorphisms and a direct universal-property or explicit fibre-product check; no such proof is written on this page.

4. **Scan 20, generators above main diagram; own idea.** A presentation-level comparison using the written pairs for rho and sigma may expose whether the candidate group identification depends on a choice of central generator or on a sign convention. **Confidence: medium**, because the displayed generator images and cyclic quotients give a concrete test, but some relevant subscripts and the small fibre-product formula remain uncertain. This is a proposed check, not an established consequence or a claim of novelty.

5. **Scan 21, upper parameter box and equation; unpursued implication.** The written equation `u(l_i)=g_i l_{sigma(i)}g_i^{-1}` suggests that the automorphism and permutation data are accompanied by chosen conjugators, rather than merely their existence. An investigation can compare the group of such triples with the stated extension by pi, keeping track of the ambiguity in the chosen conjugators; the page gives diagrams but no explanatory derivation.

6. **Scan 21, upper and middle sequences; unproved claim.** The diagram links `SAut^+(X)`, `Aut^+(X)`, boundary automorphisms, and a term identified with `S T`; the boundary group is compared with the underlined product `S_n·T^n`. A proof would need the definitions of the topological automorphism groups, the exact boundary condition represented by S and the exclamation-mark subscript, and the relevant lifting or restriction properties.

7. **Scan 21, middle repeated sequence; unproved claim.** The annotation “0 ou Z” beneath `pi_1 Aut^+(X)` asserts a restricted pair of possibilities without giving hypotheses or a proof here. Those possibilities should be checked against the class of surfaces intended on surrounding pages, including any exceptional surfaces.

8. **Scan 21, lower-right prose; unproved claim.** “pi_0(G)=pi_0 opère extérieurement sur F / donc opère sur [centre](F)” records passage from an outer action to an action on the centre. A direct verification would show why changing an automorphism representative by an inner automorphism leaves its restriction to the centre unchanged; whether all the displayed groups are discrete or topological must remain explicit.

9. **Scan 21, lower-left boundary map; own idea.** The map `pi_1(G)→F`, the centre target, and the component-group action can be checked together using path lifting in the depicted group extension. **Confidence: medium**, because the page explicitly places these objects together, but the construction of the extension and some arrow attachments are not fully legible. This proposes a verification of the diagram, not a completed proof.

10. **Scan 23, top lemma; unproved claim (proof sketch).** The lemma states `H^1(U_03,S_3;G_m) ≃ Z/6Z` for a regular integral scheme with `Pic(S)=0` and the stated condition on the characteristic of its generic point. The page supplies a construction and marginal cohomology sequences, but a complete verification would have to establish both generation and exact order, with all base-scheme and action hypotheses fixed.

11. **Scan 23, parenthesis below lemma; unproved claim.** The phrase “est 2, on trouve Z/3Z” records a characteristic-2 variant, although its short subject is partly overwritten. This deserves a separate argument rather than an automatic reduction of the characteristic-not-2 case, particularly because the relevant finite group schemes and equivariant line-bundle data can change with characteristic.

12. **Scan 23, diagonal margin; unpursued implication.** “on utilise suite exacte” introduces mixed-cohomology and global-unit sequences, with an inner H^1 term explicitly braced to 0. These sequences may furnish an alternative algebraic proof of the same line-bundle order, but the small terminal operator before V(J) and the exact equivariant module structure first need to be resolved.

13. **Scan 23, middle bundle definition; unproved claim (proof sketch).** The statement “est un générateur” identifies the indicated principal bundle with a generator of an H^1 group. A proof must connect the tautological construction on P(V_J) with the equivariant structure and explain why no additional classes arise from the base under the written Picard-group hypothesis.

14. **Scan 23, lower middle; unproved claim (proof sketch).** “le groupe structural ... est réduit à mu_6” follows the construction of a degree-six section. To verify this step one must check that the section is invariant and nowhere zero on the indicated open subset, then formulate exactly the induced reduction of structure group, including in residue characteristics dividing 6.

15. **Scan 23, NB at bottom; conjecture (explicit uncertainty).** “Sauf erreur” introduces the displayed invariant-algebra formula, definitions of gamma_2 and gamma_3, and `Delta=gamma_2^3`. The author's qualification should remain attached to these formulas; the overwritten generators, apparent quotient, and uncertain first sign of gamma_3 warrant independent examination rather than editorial normalization.

16. **Scan 23, product and NB; own idea.** Expand the candidate polynomials separately for the literal minus reading and the alternate plus reading in gamma_3, and compare their relations with the written degree-six product. Keep the stemmed phi-like symbol distinct from the final Delta until their relationship is justified by the manuscript. **Confidence: medium**, because this is a concrete algebraic check, while the readings and intended normalizations remain uncertain; no identity or novelty is asserted.

17. **Scan 23, lemma hypotheses; own idea.** Test the construction over bases with residue characteristic 3 while retaining the written generic-characteristic condition, since only 2 is explicitly singled out in the statement. **Confidence: medium**, because the proposed order and reduction both involve 6, but the page does not spell out all relevant base-change hypotheses. This is a proposed special-case check, not a counterexample or correction.

18. **Scan 25, main paragraph; unproved claim (proof sketch).** The argument begins “Comme gamma_2 s’annule” at the indicated P-point and similarly places gamma_3 at the Q_i, then infers absence of invariant sections in the written degree range. A complete proof would require the definitions of these loci, precise vanishing multiplicities, and an account of why every relevant invariant section is controlled by the indicated generators.

19. **Scan 25, final three lines; unproved claim (proof sketch).** “l’ordre de cl(O(1)) ... est bien 6” and “un générateur du H^1 mixte” state exact order and generation. The page sketches the order argument but does not independently establish that the entire mixed H^1 group is cyclic; this should be related carefully to the lemma and marginal sequences on scan 23.

20. **Scan 25, bound on n compared with scan 23; own idea.** Compare the literal weak inequality `n <= 6` with the earlier construction involving O(6), while distinguishing arbitrary invariant sections, sections of the punctured line bundle, and the direction of dualization. **Confidence: high that the scope needs checking**, because the lower bar is visibly present and both pages single out degree six; this is an editorially separate question, not a correction of the inequality or a claim that the argument is false.

21. **Scan 25, crossed opening; unpursued implication.** The cancelled phrase beginning “[Si] 2 [inversible]” appears to impose a stronger base condition than a statement merely about generic characteristic. The reason for abandoning this route could be investigated against the surviving argument, but the unclear remainder of the cancelled sentence must not be treated as an established theorem.

22. **Scan 27, upper-right square — conjecture.** The identification `PM_{11}(2^{\sim}) \overset{?}{\simeq} PU_{0,3}` carries a literal question mark. The precise level/tangent decorations must be read and defined before testing whether this is an isomorphism of spaces, stacks, or torsors; the square alone does not settle that category. The nearby cohomological notation may be relevant, but its initial `H^1` is itself a doubtful reading (Grothendieck, 1981, scan 27).

23. **Scan 27, upper-right square — unproved claim.** The square is labelled “cart”. A proof would require explicit definitions of all four objects and maps and a comparison with their fibre product, including whatever ineffective action is suggested by the pair `(U_{0,3},\{1,\omega\})`. The manuscript supplies a diagram rather than a proof on this sheet (Grothendieck, 1981, scan 27).

24. **Scan 27, lower quotient diagrams — unproved claim.** Several arrows are labelled “gal”, with groups `D'_3`, `D_3`, and `{1,\omega}`, while other arrows carry the tentative reading “gerbe”. Verifying these descriptions requires specifying the actions and stabilizers, and determining when a displayed map is an effective covering and when it retains an ineffective kernel. No assertion about these kernels should be imported merely from the familiar names of the groups (Grothendieck, 1981, scan 27).

25. **Scan 29, middle network — unproved claim.** The diagram compares successive D-groups and cyclic groups `Z/12Z`, `Z/6Z`, `Z/4Z`, and `Z/2Z`, with labels “2”, “3”, and “12”. A proof would need presentations or explicit homomorphisms sufficient to check the kernels, all indicated composites, and the compatibility of the central Z-maps. The handwritten leftward head between two cyclic groups is particularly worth checking against the surrounding development (Grothendieck, 1981, scan 29).

26. **Scan 29, bottom exact sequence — conjecture.** The middle group in `1 — Z → ? → Sl(2,Z) — 1` is left as a literal “?”. Its position below the extension with quotient `Pi^D_{0,3} × Z/4Z` suggests an identification problem for a pulled-back extension, but that interpretation remains to be verified from the missing definitions and maps (Grothendieck, 1981, scan 29).

27. **Scan 29, bottom comparison — own idea. Confidence: medium; reason: the sheet visibly compares extensions with a common infinite cyclic kernel.** After fixing the relevant actions and identifying whether the kernels are central, compute the extension classes and their restrictions along the displayed map from `Sl(2,Z)`. This could determine the group represented by “?” and distinguish a pushout on the kernel from a restriction on the quotient; it is a proposed calculation, not a claimed result or novelty.

28. **Scan 30, upper prose — conjecture.** The line beginning “comment ces sections sont elles” appears to ask how the sections `e_i-e_j` are “permutées entre elles”, with the latter word explicitly doubtful. A useful next step is to identify the acting group and calculate its action on the individual differences, retaining any signs, rather than considering only the span indicated by the tentative top-line identification of `V_J` (Grothendieck, 1981, scan 30).

29. **Scan 30, upper-right calculation — unproved claim.** The displayed relation `\lambda^6=\prod_{i,j}\xi_{ij}(x)` gives a root construction but does not define its index set or global gluing on this page. Establishing a global torsor or line-bundle interpretation would require identifying the sheaf containing each factor, the multiplicities, and the locus on which the product is invertible. These are questions prompted by the display, not corrections to it (Grothendieck, 1981, scan 30).

30. **Scan 30, lower rotated prose — conjecture.** The explicit question begins “Si on prend l’orientation inverse” and asks for the corresponding barred operators. It is followed on the same page by the candidate formulas `\bar\rho'_s=\bar\rho_s^{-1}` and `\bar\rho'_f=\mathrm{int}(\sigma)\bar\rho_f^{-1}`. The calculation should be checked against the definitions of the representatives in `A^L_+`, `A^L_-`, and the involution whose subscript is doubtful (Grothendieck, 1981, scan 30).

31. **Scan 30, final operator identities — own idea. Confidence: high as a conditional algebraic check; reason: it follows formally from the displayed transformation if sigma is an involution fixed by it.** Under that explicit hypothesis, applying the proposed orientation-reversal transformation twice should recover both original operators. Checking this directly is a small consistency test, but it cannot establish that the geometric orientation change is represented by these formulas or that the hypothesis on sigma holds in the author’s conventions.

32. **Scan 31, lower two-row diagram — unpursued implication.** The two rows have the same displayed kernel `Pi_0`, and the middle and right vertical maps are drawn as inclusions. It is worth checking whether `Pi'` is the inverse image of `D'_3` under the map `Pi × Z/4Z → D_3 × Z/4Z`; the picture suggests this comparison but does not explicitly label that square cartesian. A proof must identify the maps and verify equality of the resulting subgroup, not merely compare the printed kernels (Grothendieck, 1981, scan 31).

33. **Scan 31, middle and bottom diagrams — own idea. Confidence: medium; reason: the same decoration `(4)` recurs together with a new `Z/4Z` quotient.** Determine whether the construction denoted `\widetilde\Pi(4)` is a pushout of the infinite cyclic kernel, a pullback, or another modification. Computing one explicit presentation and following the distinguished generator of Z through the two diagrams would separate these possibilities without assuming that `(4)` means a level-four congruence subgroup.

34. **Scan 32, opening cases — unproved claim.** The clauses beginning « La construction ... » distinguish termination, expressed through `σa_n ∉ A′`, from indefinite continuation. A proof would need the preceding definition of the iterative construction, in particular what determines the sequence and why the displayed closing assignment to `ρa_0` has the required properties; the reading of the opening negation remains uncertain.

35. **Scan 32, middle — unproved claim.** The passage « Alors ρ sur A est un ... » appears to claim that the extension is an automorphism, and then defines a quotient and the part corresponding to finite orbits. To justify it one must check both bijectivity and the compatibility of the extension with the previous partial permutation; the manuscript wording is too compressed to substitute a reconstructed proof for it.

36. **Scan 32, final paragraph — unproved claim.** The asserted identification of quadruples `(A,σ,A′,ρ)` with triples `(A,σ,ρ)` includes the conditions « σ d'ordre 2 ss pt fixe » and `A′ ∪ σA′ = A`, while recovering `A′` from finite `ρ`-orbits. The exact axioms referred to in this fragment are not stated here, so any proof requires them and must show that the recovery procedure is inverse to forgetting `A′`.

37. **Scan 32, final paragraph — own idea; confidence: medium.** On the tentative reading of `A′` as the set of finite `ρ`-orbits, finite and infinite test examples of pairs of permutations `(σ,ρ)` could determine which direction of the asserted equivalence uses `A′ ∪ σA′ = A`. This is a proposed diagnostic, not an established conclusion or a claim of novelty; the reason for moderate confidence is the explicit final displayed condition despite uncertainty in the preceding prose.

38. **Scan 33, top and central diagrams — unproved claim.** The simultaneous diagrams of `Π̃₀(q)` assert compatibility between an extension by `Z`, the quotient to `Z/qZ`, and the product `Z/pZ × Z/qZ`. A proof must specify the maps on generators, including the chosen `α`, and verify the displayed squares; the sheet itself largely consists of the diagrams.

39. **Scan 33, lower formulas — unproved claim.** The equations `δ_p*(η_p) = q′η_μ` and `δ_q*(η_q) = p′η_μ` supply the arithmetic of the pullback of the extension classes. A verification must determine the definitions of `p′`, `q′`, and `μ` and the normalizations of the generator classes from the surrounding manuscript, rather than assume them from conventional notation.

40. **Scan 33, cancelled formula — own idea; confidence: medium.** The cancellation of the expression lacking `α`, followed by `δ_p*(αη_p) = q′αη_μ`, suggests checking dependence on the identification of the cyclic quotient before comparing extensions. This is an editorial diagnostic prompted by the visible correction, not an assertion that the manuscript has proved a general classification result.

41. **Scan 34, top identity — unproved claim.** The chained identifications beginning `ST₁₁ ≃ SL̃(2,Z)` and the presentation `ρ³ = σ²` are asserted alongside a fibre product over `Z/6Z`. To prove that the indicated isomorphisms respect the extensions, one would need explicit maps on the displayed generators and the identification of the central generator marked `ω`.

42. **Scan 34, inverted lower square — conjecture.** A visible question mark labels the upward arrow from `Π̃` to `Π̃(4)`, next to a word tentatively read as « cart ». The question may concern the map or the Cartesian nature of the square; the sheet does not specify which, so the research issue is to determine the intended square and test its universal property.

43. **Scan 34, source-sheet note — own idea; confidence: high as a source-critical caution.** The distinct sideways billet reads « 27-11-81 », « M. Grothendieck », and « A remplir d'urgence ». It should be kept separate from the mathematical author's assertions; its date alone does not determine when the mathematical additions were written, and the signature is not read securely.

44. **Scan 35, top numeric specialization — conjecture.** The explicit parenthesis « (α = −1 ?) » leaves a sign choice open at the point where `p=6`, `q=4`, and `μ=12` are substituted. The displayed residue maps and later circled `α′` offer evidence to investigate the intended convention, but they should not be used to erase the written question.

45. **Scan 35, prose to the right of the residue map — unproved claim.** The map from `Π₀,₃ᴰ` to `Z/6Z` is said to be « défini directement par l'action » on a principal covering associated with a canonical multisection, the latter noun read with some doubt. A proof would need the construction of this covering, its equivariance for the displayed symmetry group, and a direct computation of the residues of `ρ` and `σ`.

46. **Scan 35, lower extension diagram — unproved claim.** The diagram identifies a group written `Π̃₀,₃ᴰ(4)` with `π₁(PU₀,₃, S₃ × μ₄)` and relates the lower group to a fibre product over `Z/2Z`. Verification requires checking that the two vertical maps preserve the distinguished central subgroups and the group action on the total space.

47. **Scan 35, final presentation — unproved claim.** The final relation `ρ̃³ = σ̃²` is followed by an isomorphism to the displayed lifted Teichmüller group. The preceding generators carry an uncertain extra superscript and an annotation involving `ω′`; a proof must first fix these distinctions and then show that the presentation has neither additional relations nor a larger central kernel.

48. **Scan 35, top and final formulas — own idea; confidence: medium.** Computing the residue maps on the two displayed generators and comparing the image of their common central power could test the sign convention without using an external presentation. This is a proposed consistency check, not a correction of the manuscript; the reason for moderate confidence is that the residues are legible, whereas the decorated lifted generators are not.

49. **Scan 36, main comparison diagram — unproved claim.** The displayed maps on generators, including `ρ ↦ ρω̄²`, `σ ↦ σω̄³`, and `ω² ↦ ω̄⁴ = ω′`, are asserted to fit the three rows of extensions. A proof should check the relations in the explicitly written presentation of `SΠ₀,₃ᴰ(4)` and the compatibility of the chosen central generators; the sheet supplies formulas rather than a written verification.

50. **Scan 36, upper-right presentation and main diagram — own idea; confidence: medium.** Substituting the displayed generator images directly into the relation `ρ³ = σ² = ω̄⁻⁴` provides a possible test of the comparison maps and the inverse convention relating `ω` and `ω′`. This is an editorial consistency test, not a correction or a claim that all identifications follow from it; moderate confidence reflects legible exponents in the presentation but overwritten notation in NB.

51. **Scan 36, inverted foot annotation — unproved claim.** The group `SΠ₀,₃ᴰ(4)` is annotated as `π₁(U₀,₃, S₃ × μ₄)` over a map to `Π₀,₃ᴰ`. The visible base symbol has no P in this foot annotation, whereas the preceding sheet writes P in a related identification; establishing the intended objects would require the author's definitions, and the difference has been preserved.

52. **Scans 23, 25, 27, and 35–36, equivariant classes and cyclic quotients — own idea; confidence: medium.** Compare the manuscript’s degree-six class and its quotients of orders 4, 6, and 12 with Fulton and Olsson’s (2010, Theorem 1.1) identification of $\operatorname{Pic}(\mathcal M_{1,1,S})$ with $\mathbb Z/12\mathbb Z\times\operatorname{Pic}(\mathbb A^1_S)$ when $S$ is reduced or is a $\mathbb Z[1/2]$-scheme. Their Lemma 2.2, in the section where 6 is invertible, places the compatible characters at the order-4 and order-6 stabilizers in a common order-12 subgroup. A comparison would require actual morphisms of the relevant quotient stacks and an identification of the manuscript’s bundle with a specified power or dual of the Hodge bundle; shared orders alone do not identify them. Confidence is medium because the explicit orders and bundle trivializations give a concrete comparison to test, while the required identifications and base hypotheses are not established in these sheets.

## References

Fulton, W., & Olsson, M. (2010). The Picard group of $\mathcal M_{1,1}$. *Algebra & Number Theory, 4*(1), 87–104. [https://doi.org/10.2140/ant.2010.4.87](https://doi.org/10.2140/ant.2010.4.87)

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois: Brouillon* [Handwritten manuscript draft, cote 140-1; supplied scans 20–37]. Université de Montpellier. (Identification and catalogue year supplied with the task.)
