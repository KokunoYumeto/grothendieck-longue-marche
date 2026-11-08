# LM_C3-378-396 — transcription notes

## Scope, numbering, and editorial conventions

This package transcribes the 19 supplied images in filename order, scans 378–396. The scan number is the number in the filename, not the smaller archival numeral printed below the image: scan 378 carries archival page 377, and scan 396 carries archival page 395. Visible original manuscript foliation is retained separately with `\mspage`; the lower handwritten archival numerals are retained as marginal numerals. The printed institutional footers are also transcribed, following an explicit LaTeX comment that distinguishes them from the autograph.

Readings are based only on the supplied images. No external transcription or mathematically reconstructed text has been substituted. Crossed passages, insertions, repeated equation numbers, asymmetric delimiters, apparent missing factors, and inconsistent decorations remain as read. The broad double-loop group glyph is represented with a locally uncertain calligraphic G/C reading; a continuous upper stroke is not automatically treated as a separate tilde. A flat/natural decoration and several zero/omega suffixes remain locally uncertain.

The `.tex` file is a fragment with no preamble or macro definitions. Its host document must supply the requested editorial macros and the standard mathematical and `tikz-cd` facilities. In particular, `\deleted`, `\inserted`, and `\margin` must accept mathematical expressions and display or multi-paragraph content; a text-only strikeout box is insufficient. The diagrams use `ampersand replacement=\&` so that their cell separators survive capture by `\diagram{…}`. Structural checks covered page order, balanced groups, environments and math delimiters, permitted editorial commands, and inventory coverage. The fragment was not compiled to PDF: the available TeX installation lacked its formats and packages.

## Table of doubts

Locations are approximate manuscript lines or named displays. The local macro in the transcription identifies the exact affected span. High confidence still records a reading or visible discrepancy worth checking; medium and low indicate progressively less secure letterforms. A doubt marker preserves the best available reading rather than suppressing the text.

| Scan | Approximate line / location | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 378 | Display (29), first line | `\xi`, `\eta` | Both cursive letters are strongly abbreviated; letterforms, not their expected algebraic roles, guide the readings. | medium |
| 378 | Proposition, lines 1–3 | « morphisme de schémas »; « caractérisé » | First word and compressed endings faint; no stronger alternative. | high |
| 378 | End of proof, target of λ | `\mu_2` | `\mathcal{E}_2`; the target is considerably less clear here than the earlier μ₂. | low |
| 378 | End of proof | « cqfd » | Compressed four-letter closing mark. | medium |
| 378 | Remark, after « de plus » | deleted « tout » | Ink partly obliterated by cancellation. | low |
| 378 | Remark, after « impose » | deleted « une » | May be a longer crossed word; remaining loops insufficient. | low |
| 378 | Remark, « normalisation » | deleted « supplémentaire », inserted « correspondante » | The deletion is heavily crossed, and the insertion's ending is a short stroke. | low |
| 378 | Remark, after « mais » | « sauf erreur » | The large descender supports final f of « sauf »; the following compressed undulations support « erreur ». | medium |
| 378 | Remark, « qui ici est… » | « nécessairement » | Final stroke compressed. | medium |
| 378 | Bottom paragraph, before « correspondant » | deleted « tout » | Bare remnants of a crossed short word. | low |
| 378 | Bottom right, after ellipsis | deleted « Err. » | Could be a nonverbal pen cancellation; retained as a doubtful literal reading. | low |
| 378 | Diagonal lower-left margin | « sur »; `S\mathcal G_{ρ,σ}`; `ε^i ε'^j` | The diagonal lines overlap main text; the exponent letters are faint. | low |
| 378 | Diagonal lower-left margin, before the sign powers | « par » | A rightward mapsto-like mark; its long upright and rightward horizontal stroke could be a formula sign rather than a word. | low |
| 379 | Upper manuscript foliation | 490 | Overwritten first digit; retain the visible final “90” without inferring recto/verso numbering. | low |
| 379 | First paragraph, reference after « prop. p. » | 478′ | 470′; final digit is compressed. | medium |
| 379 | First paragraph, after parenthesis | « peu importe » | « peu important » / « peu importera »; final short strokes cannot be securely separated. | low |
| 379 | Left oblique marginal note | « Par la suite » | « Pour la suite ». | medium |
| 379 | Left oblique marginal note | « officialisation »; « structures » | The tall double stem and following compressed letters support the first word, but its middle and the plural ending remain uncertain. | medium |
| 379 | Display (2), source symbol | calligraphic G with hat | calligraphic C; the broad upper looping stroke appears to be part of the glyph, not a separate tilde. | low |
| 379 | Display (2), matrix group on right | Gl | Sl; two letters are overwritten, and a separate underlying correction cannot be securely isolated. | low |
| 379 | Last line | « élémts » | « éléments »; possible abbreviation. | low |
| 380 | Top line, quotient by signs | `{±1}` | The braces, unlike the sign and numeral, are not securely separable at the right edge. | low |
| 380 | Middle, quotient of M by Π | calligraphic A | calligraphic H; the elaborate capital is overdrawn. | low |
| 380 | Middle, repeated T group | T with two hats | T with one retraced hat; two small roofs are visible, but their status is uncertain. | low |
| 380 | Middle, after the quotient identification | « par ch = d'une extension de » | Possibly an abbreviated statement involving change of base; the text remains locally marked and is not expanded to restore a sentence. | low |
| 380 | Tuple (3), component letters | f₀, f₁, f∞ | g₀, g₁, g∞; main tuple is overdrawn, while the explanatory condition to its right visibly has g letters. | low |
| 380 | Tuple (3), group after membership sign | Π̂₀,₃ | Overdrawn base symbol. | medium |
| 380 | Formula (4), conjugator | f with index dotted u(i) | g; component letter is overdrawn. | medium |
| 380 | Formula (5), first component of second tuple | deleted u | Two horizontal strokes cross the small symbol; no replacement is securely visible there. | low |
| 380 | Formula (5), final component | f′∞u′(f∞) | Right edge clips the closing marks. | medium |
| 380 | Last paragraph | « dégonflage! » | Compact parenthetical word, retained as read. | medium |
| 381 | Between (6) and (7) | « donc on a » | The middle words are pale dots and short strokes. | low |
| 381 | Formula (8), right-hand group | M̃₀,₃ without S | This is the visible notation, despite the surrounding discussion of the larger S-group. It has not been corrected. | high |
| 381 | Above « la propriété » | inserted « via » | Three small connected strokes; attachment is indicated by the rising line before « la ». | low |
| 381 | Before fᵢ₊₁, fᵢ₊₂ | deleted « formes » | « formules »; several letters are hidden by the cancellation. | low |
| 381 | Insertion below (11) | opening square bracket, closing parenthesis | The asymmetric delimiters are visible and retained. | high |
| 381 | Final prose line | « retrouve » | « retrouvera »; the ending is a short horizontal stroke. | low |
| 381 | Last display, second term | f with index (i+2)+1 | g; the initial letter is overwritten. | low |
| 382 | Opening tuple | opening parenthesis before u | An upright curved stroke touches u and cannot be securely separated from its first stroke. | low |
| 382 | Opening tuple, third component | f₁ | h; the looped descender usual elsewhere is absent here. | low |
| 382 | First parenthetical sentence | « qu'il le vérifie » | « qu'il les vérifie »; the final tiny stroke after the pronoun is unclear. | medium |
| 382 | Diagram (13) | arrows in first and third positions, headless connectors in second and fourth | Some connectors have definite tips, whereas the final two short dark strokes do not resolve into arrowheads. The displayed strokes have been distinguished rather than supplying the expected exact-sequence arrows. | medium |
| 382 | Diagram (14), right vertical connector | downward arrow accompanied by a parallel plain stroke | Could be an identity/equality notation or a double arrow; the two visible strokes are reproduced without inserting an equals label. | low |
| 382 | Below (14), after « l'image » | « d'envers » | « d'inverse »; the middle letters are contracted to small strokes. | low |
| 382 | Below (14), between the M groups | inclusion sign | Membership sign; this short heavily retraced sign is uncertain. | low |
| 383 | Opening, and all group superscripts | `M_{0,3}^{!\sim}` | The first sign is read as an exclamation mark followed by a tilde, not an ordinary prime. | medium |
| 383 | Lines 2–3 | `p. 407 ff` | The doubled terminal stroke after the page reference may be a different abbreviation. | medium |
| 383 | (16), explanatory condition | `im. récipr.` | Very compressed cursive; the group and set expressions are clearer than the intervening abbreviation. | low |
| 383 | Left margin beside (16) | `à (u,f) on associe (fu,f) en mettant fu ... sous la forme u_{α,β}` | The products `fu` and their relation to inner automorphisms have not been expanded or repaired. | medium |
| 383 | (17), underbrace | `h^ν` | The base could be a cursive `l`; there is no confidently visible subscript. | low |
| 383 | After (17) | deleted `sans aucune`; `ambiguité` or `univoquement` | The deletion is heavy; the surviving word’s initial letters and its tall medial stroke remain doubtful. | low |
| 383 | Following line | `et m̄ par la seule connaissance`, then deleted `de l'image` | Reinspection supports this connected phrase, but the compressed initial cluster and the long final noun still receive a local doubt mark. | low |
| 383 | Before (19) | `u_{ξ,η}` or `u_{α,β}`; deleted `ou u_ξ`; deleted `l'autom`; `ou simplement` | The small subscript is overwritten and the words above it are crossed out. | low |
| 383 | (16), group in the explanatory arrow | Hatted script `G` or `C` | The looping glyph remains locally uncertain; no detached tilde is introduced. | low |
| 384 | After (20) | `on aura` | Possibly `on a`; compressed final strokes. | medium |
| 384 | (22) | `(u_{α,β},f)` | No third subscript `f` is visible here, although the preceding prose has `u_{α,β,f}`. The displayed formula has not been harmonized. | high |
| 384 | (23), far right | Terminal prime on `SL(2,Zhat)` | The right edge clips the closing portion of the expression. | low |
| 384 | (23), fourth coordinate | Small upward annotation `ε` beneath `ε_2(μ)` | The letter and small arrow are overwritten; the uncertainty is explicit. | low |
| 384 | Prose below (23) | `&` after the three underlined letters | A small symbol is present; its reading as an ampersand is tentative. | low |
| 384 | Same paragraph | Quotation marks around `accent` | The prime and punctuation are hard to separate. | medium |
| 384 | Cancelled prose before ambient product | `définis d'éléments de` | Crossed-out word boundaries are uncertain. | low |
| 384 | Ambient product | Superscript `′±1` on the first `GL` factor | Overwriting makes the status and placement of `±1` uncertain; no corrected group has been substituted. | low |
| 384 | Inserted warning above (24) | `pas dans SL(2,Zhat)' !` | Initial group letter may be `GL`; the first, unprimed `SL` is clearer. | medium |
| 384 | Deleted line above (24) | `par modulo passage à` | Crossed-out cursive; alternatives cannot be responsibly chosen. | low |
| 385 | Opening group | Deleted `S_0` before `M` | Overwritten capital and small lower character; the visible `M[0]` is retained. | low |
| 385 | First paragraph | `définissant` | The terminal letters are compressed strokes; no expansion of an assumed abbreviation has been made without a doubt mark. | medium |
| 385 | Before the cocycle calculation | `pour me rassurer` | The faint word has the visible sequence of humps and final stroke compatible with this reading. | medium |
| 385 | Before (25) | `à un des deux signes près` | The middle noun is very compressed. | low |
| 385 | (25), first `u′` | Tiny subscript `∞` or `ω` | A small looped character beneath the `u′` is visibly present; its identity is not resolved. It has not been silently dropped. | low |
| 385 | Paragraph after (25) | Inserted `élémts` above deleted `images` | The abbreviation's internal vowels and accent are uncertain. | medium |
| 385 | Parenthesis after (26) | `item` or `idem` | A short cross-stroke appears to belong to a `t`; the alternative is retained. | low |
| 385 | Before (27) | Deleted `Π`, then hatted script `G` or `C` | The deletion is heavily inked. The double-loop surviving group glyph has a definite detached hat, but its alphabet remains uncertain; the upper wave is treated as part of the glyph. | low |
| 385 | Prose before (28) | Double or single primes on the three indicated `α,β` occurrences | The ink makes some paired prime strokes merge into one dot. The uncertainty is local; (28) has clearer double primes. | low |
| 386 | Opening ambient product | Deleted `Γ(GL(2,Zhat) × SL(2,Zhat) ×` | The left symbol is overwritten; the unfinished terminal multiplication sign is retained without supplying absent factors. | medium |
| 386 | Inserted ambient product | `E^{*}` or `E′`, with a heavy/double-stroked `E` | The character's alphabet and the superscript are uncertain; the other factors and `μ_2` are more legible. | low |
| 386 | After the reference to (28) | `sera valable` | The first word is faint and partly retraced. | medium |
| 386 | Between `ou` and `de III` | Inserted `m̄` or `=` | A small two-stroke sign with a placement mark is present; its exact reading is unresolved. | low |
| 386 | (29), membership conditions | `α,α′ ∈ T_ρ` and `β,β′ ∈ N′_σ` | These appear to be Greek letters, even though the main formulas also use Latin `a,b`; no contextual correction has been made. | medium |
| 386 | After (29), cancelled below `le produit` | `calculé à` | The final short mark could be a different letter or punctuation. | low |
| 386 | Below (30) | Deleted `u`, then `α,β,α′,β′` | The isolated first character is heavily overwritten. | low |
| 386 | Same paragraph, next line | Deleted `α,β,u,a` | Several crossed letters and punctuation overlap; this is only a tentative symbolic reading. | low |
| 386 | End of displayed calculation | Deleted `OK` | The cancellation almost obscures the two-character mark. | low |
| 386 | Below displayed calculation | Deleted `u′(β)β′` | Recognizable initial and tall letters survive the cancellation, but primes and parentheses are less clear. | low |
| 386 | Bottom right | Check mark or slash | An isolated diagonal mark is preserved as a marginal mark. | low |
| 387 | (31), third coordinate | `μ=1` | The letter before `=1` is darkened by overwriting. | medium |
| 387 | (31), both conditions | Deleted `{±1}` replaced by `G_m` after `Γ` | The old braces and inner signs are partly obscured by the added group symbols. Both visible states are represented rather than choosing only the final one. | low |
| 387 | Immediately below (31) | `Γ` or `S` before `G_{ρ,σ}`, superscript `∘` or `0` | The narrow dark prefix is overwritten, and the small circular superscript is ambiguous. | low |
| 387 | Square-bracketed remark | Deleted `μ_2` beneath added `G_m` | The overlaid forms have tall descenders; the reading of the cancelled symbol is tentative. | low |
| 387 | Parenthesis about multiplication | Deleted `sur les` / `sur le`; deleted `en α,β`, then inserted `en α β` | Two rejected phrases and the surviving phrase are stacked closely. | low |
| 387 | Middle, special subgroup | `ss-groupe` | The abbreviation is compressed; no expansion is introduced into the transcription. | medium |
| 387 | Quoted description of the special subgroup | `de nature triviale` or `d'action triviale` | The middle word has a clear tall `t` but its surrounding small strokes are ambiguous. Both readings are kept. | low |
| 387 | Bottom boxed insertion | `Σ_0`, followed by a small point | The subscript is a small round character. The box is retained as a boxed insertion. | medium |
| 387 | Immediately after the boxed insertion | Deleted `engendré` | A horizontal stroke crosses the word; the final letters are faint. | medium |
| 388 | 2 | hom. | hom without a visible full stop | medium |
| 388 | 11, before “groupe” | opening quotation mark | a correction stroke rather than quotation mark | low |
| 388 | equation (32), first component | deleted f, before int(f) | overwritten first component whose punctuation cannot be separated securely | low |
| 388 | equation (32), second component | f without exponent | there is no visibly legible −1; the adjacent triple has f inverse | high |
| 388 | 17, after sur Π̂ | deleted étant | est or a longer overwritten form | low |
| 388 | 19, subscript to underlined Aut | loc | lac | low |
| 388 | equation (33), first component | deleted α= followed by l_0^n | overwritten initial letter or equality sign | low |
| 389 | 1 | aura | a; the ending is reduced to a stroke | medium |
| 389 | unnumbered upper formula, cancelled expression | f' inverse · f inverse · (f u_{α',β'} f inverse) | the central indices and final parenthesis are overwritten | low |
| 389 | unnumbered upper formula, replacement | u_{α',β'} | first index's prime is weak | medium |
| 389 | upper formula, underbrace label | f double-prime inverse | count of prime strokes insecure | medium |
| 389 | 3 | i.e. | ici | low |
| 389 | 5, before the resulting triple | pour | par | low |
| 389 | 5, cancelled symbol before triple | g''= | g'' without equality sign | low |
| 389 | 10 | correspondante | corresponding final word ending is cursive and faint | medium |
| 389 | after equation (35), reference | 489' | overwritten third digit, possibly 488' | medium |
| 389 | before equation (36) | en définissant le | on définira l'; the article is involved in the following revision | low |
| 389 | equation (36), deleted left coordinate | (α,β,μ,ε) | (α,β); strongly overwritten | low |
| 389 | margin below (36) | à, with a left-pointing arrow below | inversion notation rather than the word à | medium |
| 390 | equation (37), denominator | Σ with a tilde | the upper decoration is overwritten | medium |
| 390 | equation (37), deleted material after denominator | (Ẑ) | nearly cancelled parenthesized argument | low |
| 390 | below (37) | ss-groupe “impuissant” | abbreviation and quotation marks run into the page edge | medium |
| 390 | annotation below (38) | SG(Ẑ) | hat and last parenthesis are at the cropped manuscript edge | medium |
| 390 | prose after (38) | ambiguïtés de signes | ambiguités de signe; diaeresis and final s insecure | medium |
| 390 | before (39) | hom | hom. with a faint or absent full stop | medium |
| 390 | target of (39) | S_0 M with deleted superscript !~ | S M; the apparent subscript and superscript are heavily revised | low |
| 390 | first coordinate of (39) | α = ε_0(λ) | minus before λ may be merged into its first stroke; equality sign is crowded | low |
| 390 | second coordinate of (39) | β = ε_0(−λ) | equality sign is crowded into β | medium |
| 390 | final line | S_0 M_{ρ,σ}^{!~} | S M_{ρ,σ}^{!~}; small loop after S may be an overtraced letter, not 0 | low |
| 391 | (40), cancelled product and right margin | j | i; the long descending stem favours j | medium |
| 391 | left margin beside cancelled calculation | No. | Non. | low |
| 391 | cancelled U tuple, underlined second coordinate | a | ρ; heavy retracing obscures the bowl and descender | low |
| 391 | cancelled U tuple, underlined third coordinate | b | β | low |
| 391 | cancelled U tuple, character before f | ε | a cancellation mark rather than a separate coordinate | low |
| 391 | prose before (41), superscript on S M | star | a revision mark rather than retained superscript | low |
| 391 | (41), deleted left-hand group | S M with star | exact prior decoration is overwritten | low |
| 391 | prose after (41) | mono i | homo i; the first loop favours m | medium |
| 391 | after (42) | d'inclusions | d'inclusion | medium |
| 391 | bottom-right diagram, deleted target after B'_0 | 𝒢_{ρ,σ} with star | exact subscript partly erased | low |
| 391 | bottom-right diagram, character beside right brace | i' | a remnant of the cancelled adjacent group rather than a separate label | low |
| 391 | bottom-right diagram, deleted shared target | 𝒢_{ρ,σ} with star | M_{ρ,σ}; strongly overwritten | low |
| 391 | bottom-right diagram, third source object | N'_σ | N''_σ; apparent extra prime is continuous with the descender of ρ in the preceding row | medium |
| 392 | first displayed subgroup, deleted subscript to i | B | the cancelled strokes do not securely establish another letter | low |
| 392 | after est invariant par, crossed group notation | ΓT_ρ, ΓT_σ i_T | the two group symbols and last subscript are substantially overwritten | low |
| 392 | above crossed group notation | inserted les | may belong to the abandoned phrase rather than the surviving list | medium |
| 392 | under first brace in the central calculation | cancelled λ before x(λ) | cancelled x; a compact overwritten cluster | low |
| 392 | under second brace in the central calculation, last delimiter | square bracket after i_G(x(λ) inverse | opening delimiter is round; the visibly square ending is retained | high |
| 392 | diagonal left margin, first line | On voit de suite | middle verb is rapidly written | medium |
| 392 | before the L_0 morphism, deleted object | G_a | L_0; the ink is heavily crossed | low |
| 392 | L_0 morphism target after equality | S-tilde 𝒢 with star | the long descending stem is G, even though a later target uses M | high |
| 392 | after sur le deuxième via | π_B | i_B; top shape resembles π but is overtraced | medium |
| 392 | next morphism target, under M | cancelled 0 | an overwritten index rather than a distinct zero | low |
| 392 | next morphism target, superscript | flat sign | star, natural sign, or a revision mark; heavily retraced | low |
| 392 | final displayed conjugation, first argument | f overwritten by x | correction direction and old letter are not fully secure | low |
| 392 | penultimate prose line | peut sauter sur le facteur | peut sauter sous le facteur; verb and preposition are cursive | medium |
| 393 | Top, second dimension total | `4` | Overwritten digit; the final shape is 4, but an earlier stroke remains. | medium |
| 393 | Top, after `i(L_0)` | `fournit` | `fournir`; the final strokes are faint. No missing grammatical subject has been supplied. | medium |
| 393 | Top, before `notés` | deleted `ce` | The short word is heavily overwritten; its precise letters remain insecure. | low |
| 393 | Diagram (43), middle vertical arrow | hook arrow; `can.` | The arrow has a hooked top and a dark head; the small adjacent annotation is overwritten. | low |
| 393 | Diagram (43), lower right object | `M_{rho,sigma}` | A tilde is not securely visible; `M` with a tilde remains an alternative. | low |
| 393 | Below diagram (43) | `représentables` | The long word's central letters are very cursive; independent rereading supports this over an earlier tentative `exprimables`. | medium |
| 393 | Below diagram (43) | deleted `par les`; inserted `comme` | Possibly only `par`; the following short strokes are heavily cancelled. | low |
| 393 | Equation (44), first left member | `S` with tilde | Several strokes overlap the initial S. | low |
| 393 | Equation (44), first right member | deleted `T_0` | Only the top bar and lower strokes survive. | low |
| 393 | Equation (44), second left member | deleted extra tilde | The small overwritten mark cannot be distinguished from a different superscript. | low |
| 393 | Equation (44), second right member | deleted flat/natural decoration; deleted `S` before `G` | Both deletions are dense. | low |
| 393 | Final paragraph, decorations of `G^*(0)` | flat sign | The added small signs are darker than the surrounding ink and partly overwritten; flat and natural remain alternatives. | low |
| 394 | Opening paragraph | `hom.` | The final stop is not distinct. | medium |
| 394 | (45), deleted prefix of source | `S_0` | Both the S and the lower small mark are cancelled. | low |
| 394 | (45), decomposition beneath target | deleted `B'_0`; `T_0` | The replacement T may carry a hat; the earlier letter is densely struck out. | low |
| 394 | Paragraph after (45) | `resp.t` | A detached raised stroke follows `resp.`; possibly an abbreviated ending. | low |
| 394 | Remark, group in prose | `(0)` | The handwritten 0 is looped; the following diagram has a more distinct 0. | medium |
| 394 | (46), left lower group | flat/natural decoration after star | Same overwritten small sign as on scan 393. | low |
| 394 | Unnumbered lower diagram, cancelled first object | calligraphic `G` | Calligraphic `C`; the glyph is heavily cancelled. | low |
| 394 | Unnumbered lower diagram, middle object | double-loop `G` with hat | Calligraphic `C`; the upper wavy loop is continuous with the glyph, not a secure separate tilde. | low |
| 394 | Beneath middle object | vertical isomorphism sign | A small curved vertical mark rather than an equality. | medium |
| 394 | (47), right-hand first factor | `M_{0,3}^{!~}` | No `(0)` is securely visible; none has been supplied. | medium |
| 395 | (48), normalized factor | `(0)` | `(omega)`; the small loop is open and doubled. | medium |
| 395 | (48), last factor | double-loop calligraphic `G` | Calligraphic `C`. No separate hat is visible here, although one is clear in the next displayed map. | low |
| 395 | Unnumbered map, source | double-loop calligraphic `G` with hat | Calligraphic `C` with hat. | low |
| 395 | (49), extreme right | `Sigma` | Partly against the black frame at the image edge. | medium |
| 396 | Sentence introducing (1) | `du produit semi-direct` | Independent rereading supports the singular wording; the compressed endings were checked against the scan. | high |
| 396 | (1), both superscripts after the star | flat sign | Independent visual reading favors a flat sign, with a natural sign still possible; the mark has one long stem and a rounded lower loop. | low |
| 396 | (1), both parenthesized suffixes | `omega` | `0`; the visible lower shape is open and double-lobed, unlike the clearer oval zeros in (44) on scan 393. | medium |
| 396 | (2), second inclusion subscript | deleted `rho`, inserted `rho` | The earlier upper glyph could be `B`; the lower replacement is more clearly rho. | low |
| 396 | (2), third inclusion | `i_sigma` | `i'_sigma`; the sloping stroke above the i could be its dot or an additional prime. | medium |
| 396 | Conditions below (2) | `N'_sigma` | The N is heavily retraced. | medium |
| 396 | (3), vertical identification mark | vertical isomorphism sign | Small curved stroke and a separate vertical stroke. | medium |
| 396 | (3), lower left group | deleted `M`, then calligraphic `G` | The initial letter has been retraced over an M-like form; the surviving long descender supports G. | low |
| 396 | (3), lower group superscript | flat sign after star | The same small retraced decoration as in (1). | low |
| 396 | Unnumbered formula below (3), argument of `i_G` | `f` | `phi`; the written loop differs from the final f on the same line. | low |

## Abbreviations and compact notations encountered

Expansions below are editorial suggestions only. Abbreviations remain unexpanded in the transcription.

| Written form | Tentative expansion / meaning |
|---|---|
| dfn. | définition |
| mod | modulo |
| resp. | respectivement |
| i.e. | id est |
| `\overline{\mathrm m}` (m̄) | même |
| cqfd | ce qu'il fallait démontrer |
| Rmq | remarque |
| hom. | homomorphisme |
| car. | caractéristique |
| can. | canonique |
| tjrs | toujours |
| cf | confer / comparez / voir |
| p. ex. | par exemple |
| prop. | proposition |
| p. | page |
| cor. | corollaire |
| ff. | et les pages suivantes |
| dét | déterminant |
| ch (doubtful) | changement, possibly change of base; the full phrase is uncertain |
| l'ens. | l'ensemble |
| hom | homomorphisme; no terminal dot visible in scan 381 |
| `ff` | following pages, if the reading is correct |
| `im. récipr.` | image réciproque, if the reading is correct |
| `dfn` | définition |
| `Norm` | normalisateur |
| `autom` | automorphisme |
| `NB` | nota bene |
| `loc. cit.` | loco citato, at the place cited |
| `int` | automorphisme intérieur / conjugaison intérieure |
| `élémts` | éléments, if this reading of the overwritten abbreviation is right |
| `item` / `idem` | also / the same; the actual written form is doubtful |
| `OK` | okay, accepted/check successful |
| `de =` | de même; the written equals sign has not been expanded |
| `ss-groupe` | sous-groupe, if this is the intended abbreviation |
| `Γ` | notation for sections, not expanded in the transcription |
| Aut | automorphismes |
| loc / lac (uncertain subscript) | local / lacets, respectively; no secure expansion |
| ½ direct | semi-direct |
| etc | et cetera |
| autom. | automorphismes |
| int. | intérieurs |
| mono | monomorphisme |
| O.K. | okay / accord |
| `dim` | dimension |
| `suppl.` | supplémentaires |
| resp.ᵗ (uncertain) | respectivement |

## Legibility and limits

The numbered formulas are generally more legible than the fast, pale French prose. The least reliable material is the normalization remark and diagonal margin on scan 378; the ornate quotient-group glyphs and abbreviated middle phrase on scan 380; the prose after (17) on scan 383; the overlapping revisions below (23) on scan 384; the revised scalar conditions on scan 387; the abandoned calculation and inclusion diagram on scan 391; and the overwritten group decorations in (44) on scan 393. Faint primes, zero/omega suffixes, and arrowheads close to the frame deserve particular caution. Scan 395 is comparatively clear, but its notation has not been harmonized with adjacent pages. All pages have been reread against their transcription and inventoried; this is not a claim that every uncertain glyph has been resolved.

## Research notes

These notes are in English and are separate from the diplomatic transcription. They identify proof obligations, implications, and possible investigations visible in this extract. An “unproved claim” means that a complete proof is not supplied at the cited location; it may rely on earlier sections or be addressed later. The notes do not certify novelty, and the rest of the manuscript and the external literature have not been checked. Own ideas are explicitly labelled and carry confidence and a reason. No securely readable explicit conjecture formula has been added merely to populate a category.

1. **Scan 378, proposition and proof; kind: unproved claim.** The manuscript says that the morphism is « caractérisé par les formules (29), mod un morphisme » to μ₂. The proof identifies the ambiguity through the intersections of centralizers and a determinant condition; a full verification over the intended base would need the precise hypotheses ensuring those centralizer identifications, especially in characteristic 2 (Grothendieck, 1981, scan 378).

2. **Scan 378, normalization remark; kind: unproved claim.** After the normalization `Θ(1,1,1,1)=1`, the text cautiously says « sauf erreur » before asserting that λ is an « hom. de schémas en groupes » and singles out an ambiguity involving ε. The useful question is which hypotheses make normalization force the asserted multiplicativity and which remaining component characters survive; the cautious phrase itself is a medium-confidence reading of the faint handwriting (Grothendieck, 1981, scan 378).

3. **Scan 378, diagonal margin; kind: unpursued implication.** The note contrasts working with `S\mathcal G_{ρ,σ}` and the larger starred group and records an ambiguity involving two sign powers. A careful comparison of the character groups of the two domains would clarify this distinction; this note records the visible claim without certifying its hardest exponent readings (Grothendieck, 1981, scan 378).

4. **Scan 379, first paragraph; kind: unproved claim.** Grothendieck says that one could make the construction « aussi sans cette condition supplémentaire », referring to `Tr σ=0` and replacing the starred group by its unstarred variant. A proof would have to identify precisely which later uses of the trace-zero condition can be removed and how the group law and its action change (Grothendieck, 1981, scan 379).

5. **Scan 379, first paragraph; kind: unproved claim.** The sentence « Nous pouvons au besoin supposer ρ,σ normalisés » leads to `Tr(ρ+σ)=1`. One should verify the existence and permissible base changes of this normalization under the general conditions cited on earlier manuscript pages; those conditions are not supplied in this package (Grothendieck, 1981, scan 379).

6. **Scan 379, display (2); kind: unpursued implication.** The specific matrices provide a concrete test case for the canonical map into the determinant-±1 subgroup modulo signs. Computing their images and relations over finite quotients could test compatibility of the later constructions, but the transcription does not replace the ambiguous source-group glyph or overwritten target letters by a presumed standard identification (Grothendieck, 1981, scan 379).

7. **Scan 380, opening paragraph; kind: unproved claim.** The promised variant is to map canonically into the product and to make « ledit morphisme multiplicatif ». Establishing this requires specifying the compatible group law, including its action on the extra component; the opening paragraph itself is a construction goal, not yet its proof (Grothendieck, 1981, scan 380).

8. **Scan 380, middle and tuple (3); kind: unproved claim.** The text describes an « extension … par Ẑ³ » through choices of conjugators for the three inertia elements. A proof should identify the kernel with the three appropriate procyclic centralizers and verify surjectivity under the stated conditions; ambiguous group glyphs in the passage should first be checked against their definitions on earlier manuscript pages (Grothendieck, 1981, scan 380).

9. **Scan 380, formula (5) and final line; kind: unpursued implication.** The formula is explicitly given « en nous bornant … au cas » in which the induced permutations are trivial. Extending it to general permutations requires tracking the relabeling of the three conjugator components; the formula must not simply be copied unchanged to that setting (Grothendieck, 1981, scan 380).

10. **Scan 381, formulas (6)–(7); kind: unproved claim.** The statement « On a un hom surjectif » identifies the kernel with three inertia factors and writes it as Ẑ³. A full verification would need the earlier definitions of each Lᵢ and the conditions ensuring that all required conjugators exist, as well as the claimed procyclic centralizer identifications (Grothendieck, 1981, scan 381).

11. **Scan 381, formulas (9)–(11) and final display; kind: unpursued implication.** Exterior commutation with ρ yields the recurrence for successive conjugators, and the final underbrace identifies the three-term product with 1. This suggests a useful explicit consistency check: derive the cocycle identity and show that the recurrence returns the original conjugator after three steps under exactly the stated hypotheses, without replacing the manuscript's surprising subgroup notation in (8) (Grothendieck, 1981, scan 381).

12. **Scan 382, opening paragraph and (12); kind: unproved claim.** The manuscript says that the quadruples satisfying the cyclic condition « forment un sous-groupe » and that this subgroup identifies with the displayed pairs. To verify the claim, one should prove closure under the multiplication already given, then show that the recurrence reconstructs the other two conjugators from the first without adding further restrictions (Grothendieck, 1981, scan 382).

13. **Scan 382, diagrams (13)–(15); kind: unproved claim.** The three-factor extension is said to be « déduite, par l'hom diagonal » from the « plus fine » extension with one Ẑ factor. A full account would formulate and verify the relevant extension construction, including its action on the kernel, and check that diagram (14) realizes that construction rather than merely a compatible morphism of extensions (Grothendieck, 1981, scan 382).

14. **Scan 382, (15); kind: own idea.** Compare the three-factor extension after quotienting its kernel by the diagonal Ẑ with the finer extension, to isolate precisely which two residual conjugator freedoms are removed by cyclic compatibility. Confidence: medium; the displayed diagonal map motivates the comparison, but its exact cohomological interpretation depends on the group action and on definitions outside these scans (Grothendieck, 1981, scan 382).

15. **Scan 383, (16)–(18); kind: unproved claim.** The text says that the earlier calculations “permettent d'autre part d'expliciter les couples” and identifies the `f=1` case with the normalizer of `L_0`. Verification would require returning to the cited §46, checking both directions of the coordinate parametrization, and establishing that the stated relation gives precisely that normalizer, not merely a subgroup mapping to it (Grothendieck, 1981, scan 383).

16. **Scan 383, after (17); kind: unproved claim.** The assertion that `μ` is determined by `α` is stated here without a proof on this sheet. A proof would need the precise previously defined maps and the uniqueness statement for the multiplier; the doubtful intervening prose is not used to supply that proof (Grothendieck, 1981, scan 383).

17. **Scan 383, (18); kind: own idea.** Check the coordinate description of the normalizer first on finite quotients of the profinite groups. **Confidence: medium as a proposed consistency check**, since finite calculations can expose sign or convention errors, but they would not on their own establish the full profinite assertion or a new result (Grothendieck, 1981, scan 383).

18. **Scan 384, (23)–(24); kind: unpursued implication.** The author emphasizes that the relation is imposed “dans SL(2,Zhat)” and “pas dans ...′ !” (the latter group letter is doubtful). This invites a separate check of the difference between an equality of lifts and equality after a central sign quotient; the text's declared independence of sign choices should be verified under exactly the stated conventions (Grothendieck, 1981, scan 384).

19. **Scan 384, (21)–(23); kind: own idea.** Track the conjugating parameter `f` through both displayed coordinate maps before using their composition. **Confidence: high as an editorial consistency check**, because the preceding prose includes `u_{α,β,f}` while (22) visibly appears to omit the third subscript; this observation does not authorize an emendation or establish which notation was intended (Grothendieck, 1981, scan 384).

20. **Scan 385, opening through (28); kind: unproved claim.** The author says that the restriction is a homomorphism and immediately writes “Je vais la revérifier.” This sheet begins the verification using a cocycle relation and compatibility with matrix images; completion requires checking the multiplication law in the target as well as the displayed coordinate identities (Grothendieck, 1981, scan 385).

21. **Scan 385, (27); kind: unproved claim.** The displayed compatibility is followed by the incomplete reference “cf ...”. The relation should be traced to the exact previously constructed homomorphism and its equivariance, because the reference is not supplied on this page (Grothendieck, 1981, scan 385).

22. **Scan 385, (25)–(28); kind: own idea.** Keep a separate table of left/right composition conventions and of the chosen matrix lifts when checking these formulas. **Confidence: high as a verification method**, since the page simultaneously uses primed cocycle coordinates, conjugation, and representatives defined only up to sign; this is a proposed check, not a correction of the manuscript (Grothendieck, 1981, scan 385).

23. **Scan 386, prose before (29); kind: unproved claim.** The author says the verification will be valid “sur une base quelconque” under the general hypotheses cited as V or III. The displayed algebra establishes the coordinate identity, but the extension to that generality also requires verifying that the chosen factorization and multiplication descriptions are available over the stated base (Grothendieck, 1981, scan 386).

24. **Scan 386, after (30); kind: unproved claim.** The calculation is written out for the `α` coordinate, followed by “et de = pour la deuxième relation 30”. The omitted parallel calculation for the `β` coordinate is a specific check to perform with the normalizer factor and its conventions; the note does not supply or alter manuscript text (Grothendieck, 1981, scan 386).

25. **Scan 386, (29)–(30); kind: own idea.** Separate the elementary conjugation identity from the existence and uniqueness of the preceding coordinate factorizations. **Confidence: high as a proof-audit method**, because the handwritten computation directly verifies only the former, while the latter is imported from earlier definitions. This is not a novelty claim (Grothendieck, 1981, scan 386).

26. **Scan 387, (31) and the bracketed remark; kind: unproved claim.** The text says these systems “forment un sous-groupe” and sketches why scalar multiplication preserves the relevant data. The claim should be checked against the exact distinction between the ordinary group, its special subgroup, and the overwritten `G_m` versus `μ_2` conditions; no choice among uncertain glyphs is used as a premise here (Grothendieck, 1981, scan 387).

27. **Scan 387, lower half; kind: unpursued implication.** The author identifies working with representatives “à signes près” with working in a quotient by the subgroup displayed as `Σ_0 ≃ Z/2Z × Z/2Z`. A useful follow-up is to track which subsequent constructions factor through this quotient and which require actual lifts, especially because the earlier relation was explicitly imposed in an unprimed matrix group (Grothendieck, 1981, scans 384, 387).

28. **Scan 387, (31) and scalar subgroup; kind: own idea.** Compare the full scalar subgroup and the two-torsion subgroup before and after base change, keeping the group-scheme statement separate from its points over `Zhat`. **Confidence: medium as a proposed investigation**, since the visible revision from sign conditions to `G_m` makes that distinction relevant, but these pages alone do not establish every base-change property or an equivalence of the corresponding quotient functors (Grothendieck, 1981, scan 387).

29. **Scan 388, equation (31), unproved claim.** The assertion “ils forment un … groupe isomorphe” precedes a “structure de produit ½ direct.” On these lines the group law and the compatibility of the displayed embedding with the asserted semidirect product are not fully checked; a proof should specify the conjugation convention and verify the action on the normal factor (Grothendieck, 1981, scan 388).

30. **Scan 388, equation (32), own idea. Confidence: medium.** Before interpreting the embedding, compare its visible pair (int(f),f) with the preceding pair (int(f inverse),f) and with the displayed triple (1,1,f inverse). This is a local convention or correction question, not a reason to change the transcription; checking the coordinate multiplication on the next scan may identify which inversions are intended (Grothendieck, 1981, scan 388).

31. **Scan 388, equation (33), unpursued implication.** The “sous-groupe invariant” Ẑ is written in triple coordinates with all three coordinates equal to l_0^n. It would be useful to compute its conjugation action directly from the upcoming multiplication formula, distinguishing normality from centrality; the present lines explicitly assert invariance, not centrality (Grothendieck, 1981, scan 388).

32. **Scan 389, equations (34)–(36), unpursued implication.** The coordinate multiplication is followed by a semidirect-product definition and an explicit warning, “Attention au passage de f à f inverse !” The warning makes the order convention a substantive part of the construction; comparing the homomorphism against both coordinate multiplication and the action through Θ would test whether the same convention is used throughout (Grothendieck, 1981, scan 389).

33. **Scan 389, equation (34), own idea. Confidence: medium.** Use the identity and pure normal-factor elements as minimal checks of the inversion in (36), then verify the displayed product on two general triples. This is a proposed consistency check, grounded in the explicit coordinate law, and does not assert that the manuscript contains an error (Grothendieck, 1981, scan 389).

34. **Scan 390, equations (37)–(38), unpursued implication.** The text says that quotienting “exprime les trois ambiguïtés de signes,” associated with α, β, and f. A useful structural check would identify the kernel of the coordinate-to-group map and establish that the displayed three order-two factors account for precisely those ambiguities (Grothendieck, 1981, scan 390).

35. **Scan 390, equation (39), unproved claim stated for subsequent verification.** “c'est un hom. de groupes” and “un ss-groupe distingué” are asserted for the additive-group map, followed by “Pour vérifier ceci.” A proof must establish the homomorphism law, injectivity if subgroup identification is intended, and invariance under the indicated semidirect product; the verification begins on the following pages (Grothendieck, 1981, scan 390).

36. **Scan 390, equation (38), own idea. Confidence: medium.** Examine how the sign-quotient description behaves under base change where 2 is not invertible. The reason for proposing this check is the explicit use of three sign factors in a construction introduced over a general base S; no claim about the result or its novelty is made here (Grothendieck, 1981, scan 390).

37. **Scan 391, equations (40)–(42), unproved claim announced here.** “on va voir que l'image du mono i … est m̄ distinguée dans ce groupe plus grand” enlarges the normality claim to the ambient semidirect product. The proposed factor-by-factor proof needs to keep track of the action through B'_0, and to establish invariance under all four displayed inclusion morphisms; the next scan carries out these checks (Grothendieck, 1981, scan 391).

38. **Scan 391, cancelled middle calculation, own idea. Confidence: low.** Compare the abandoned direct conjugation calculation with the subsequent argument using the four inclusions. Its retained expression U_0 f i(λ) f inverse U_0 inverse may help diagnose the coordinate conventions, but the cancelled and overwritten tuple is too uncertain to support an independent algebraic conclusion (Grothendieck, 1981, scan 391).

39. **Scan 392, upper invariance argument, unproved claim within the calculation.** “Pour les deux premiers, c'est trivial — avec action triviale sur L_0” disposes of the two torus-type inclusions without a separate calculation. A complete verification would identify their action on L_0 from the previously defined action, rather than deriving it from the displayed B'_0 calculation alone (Grothendieck, 1981, scan 392).

40. **Scan 392, central and final calculations, unpursued implication.** The displayed B'_0 equivariance and the statement that i(λ) acts trivially on G together distinguish the two mechanisms proving normality: equivariance under B'_0 and commutation with the G factor. The diagonal note, “commute à G, donc est invariant par G,” makes the second mechanism explicit; it need not imply centrality in the whole ambient group (Grothendieck, 1981, scan 392).

41. **Scan 392, own idea. Confidence: medium.** Abstract the argument for a group acting on another group through inner automorphisms: a compatible anti-diagonal embedding may centralize the normal factor and remain stable under the acting factor. The reason to explore this is the explicit product i_B(λ)i_G(λ inverse); the requisite compatibility, order convention, and possible kernel would need to be stated and checked before any general claim (Grothendieck, 1981, scan 392).

42. **Scan 393, opening remark — unproved claim.** Grothendieck calls the larger group a “groupe plat” and records relative dimensions 10 and 7, then 9 and 6 after the additive quotient. A verification should separate the dimension counts from flatness and establish the properties of the quotient over the base actually in use; the arithmetic alone is not a flatness proof (Grothendieck, 1981, scan 393).

43. **Scan 393, below (43), (44) — unproved claim.** The phrase “Le passage au quotient ne fait pas de difficultés” precedes explicit descriptions as semidirect products. The exact subgroup decorations need palaeographic confirmation before proving that the chosen complements descend and yield the displayed products (Grothendieck, 1981, scan 393).

44. **Scan 394, (45) and following paragraph — unpursued implication.** The “hom. canonique” takes values in a quotient by the product of three order-two factors. Its construction invites a precise study of how much information is lost to the three sign choices, keeping that issue separate from any further kernel of the comparison homomorphism (Grothendieck, 1981, scan 394).

45. **Scan 394, remark and (46) — unpursued implication.** The phrase “essentiellement, à l'aide de l'hom.” locates the construction in a normalizer of `L_0`, identified with the subgroup of “autom. normalisés.” One can ask how the comparison changes when the normalization is transported by an inner automorphism, and whether the displayed quotient removes all resulting ambiguity; this is a question suggested by the displayed construction, not a claim that these pages prove it (Grothendieck, 1981, scan 394).

46. **Scan 394, (47) — own idea. Confidence: low.** Before using (47) to derive an explicit product law, compare its first right-hand factor with the normalized subgroup in (46); the image does not securely show a normalization suffix in (47). This is first an editorial and structural consistency check, not a proposed correction to the transcription or an assertion that the written equality is false (Grothendieck, 1981, scan 394).

47. **Scan 395, (48)–(49) — unproved claim.** The announced map “prolonge l'hom (45)” from the distinguished subgroup “d'indice 6.” Beyond the displayed semidirect decomposition, a full verification should check equivariance between its factors and the corresponding action in the target quotient; specifying homomorphisms on the two factors is not by itself enough (Grothendieck, 1981, scan 395).

48. **Scan 395, concluding sentence — own idea. Confidence: medium.** Once the asserted extension is verified, compare its kernel and image on the subgroup of index six with its action on the six cosets. This is a finite preliminary calculation suggested by the explicit index, without any assertion here that it yields faithfulness or determines the full arithmetic image (Grothendieck, 1981, scan 395).

49. **Scan 396, (1)–(3) — unpursued implication.** The construction gives a “homomorphisme de groupes” whose value on the displayed four-factor expression is `x.f`. This makes the kernel accessible in the chosen coordinates, but a description of that kernel as a group must still account for the semidirect action and the relations among the factors rather than treating the coordinates as independent commuting variables (Grothendieck, 1981, scan 396).

50. **Scan 396, final paragraph — unproved claim.** The assertion that the composite “sera bien trivial” on the displayed `i(lambda)` leads to the descended homomorphism. Substitution suggests the cancellation `lambda lambda^{-1}`; a full scheme-level statement should check this identity functorially and invoke the quotient property in the intended category (Grothendieck, 1981, scan 396).

51. **Scan 396, (2) and final paragraph — own idea. Confidence: medium.** After fixing the exact group decorations from the preceding section, test whether the copy of G displayed in the semidirect product supplies a section of the descended map, and then describe its kernel explicitly. The reason for trying this is the formula `Theta(...i_G(f))=x.f`; neither a splitting of every earlier comparison map nor any new result is asserted here (Grothendieck, 1981, scan 396).

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3, scans 378–396; supplied image files]. Université de Montpellier.

The bibliographic identification and date follow the supplied task sheet. Page citations above refer to the filename scan numbering. The archive imprint reproduced on the supplied images is [grothendieck.umontpellier.fr](https://grothendieck.umontpellier.fr).

## Inventory coverage

The accompanying CSV contains one row per inventoried element, including the printed archive footer on each image. An insertion or deletion within a larger text block or display receives its own row where separately identified. All rows have `transcribed = yes`; uncertain readings remain marked in the transcription and doubt table.

| Scan | Inventoried elements |
|---|---|
| 378 | 30 |
| 379 | 17 |
| 380 | 18 |
| 381 | 24 |
| 382 | 17 |
| 383 | 19 |
| 384 | 23 |
| 385 | 21 |
| 386 | 26 |
| 387 | 28 |
| 388 | 19 |
| 389 | 21 |
| 390 | 15 |
| 391 | 27 |
| 392 | 28 |
| 393 | 18 |
| 394 | 22 |
| 395 | 9 |
| 396 | 25 |

Total: **407 elements** across **19 scan pages**; **23 `tikz-cd` diagrams**.
