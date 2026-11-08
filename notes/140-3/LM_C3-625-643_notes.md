# LM_C3-625-643 — editorial and research notes

## 1. Sources, foliation, and transcription conventions

The transcription covers all 19 supplied image files, `LM_C3-625-643_scan625.jpg` through `LM_C3-625-643_scan643.jpg`. Readings are based on those images, including enlarged and, where useful, rotated crops. No published transcription or external mathematical source was used to supply missing ink. The bibliography records the manuscript identification supplied with the task (Grothendieck, 1981).

The `\scanpage` identifiers follow the filenames. They are one higher than the numbers at the lower left inside the image frames. The upper autograph foliation is recorded separately with `\mspage`; the repeated **623** on scans 639 and 641 is retained. Lower-left handwritten foliation is represented with `\margin`. The printed page number, URL, institutional address, and other footer matter below each black frame are archive metadata and are excluded from the manuscript transcription.

| Scan / filename identifier | Upper autograph foliation | Lower-left foliation |
|---|---|---|
| 625 | 616 | 624 |
| 626 | — | 625 |
| 627 | 617 | 626 |
| 628 | — | 627 |
| 629 | 618 | 628 |
| 630 | — | 629 |
| 631 | 619 | 630 |
| 632 | — | 631 |
| 633 | 620 | 632 |
| 634 | — | 633 |
| 635 | 621 | 634 |
| 636 | — | 635 |
| 637 | 622 | 636 |
| 638 | — | 637 |
| 639 | 623 | 638 |
| 640 | — | 639 |
| 641 | 623 | 640 |
| 642 | — | 641 |
| 643 | 624 | 642 |

The fragment preserves the manuscript's numbering, including the canceled precursor and the repeated display numbers. Scan 636's entire written block is within `\deleted{…}`; its unfinished (39) ends with the visible quotient slash and no supplied denominator. Scan 643 ends in the middle of its proof at `L'image \unsure{de|des}`. Question-shaped superscripts, exclamation-shaped superscripts, stars, primes, hats, and zero/circle marks are kept distinct. The curved group letter is represented by `\mathcal G`, with script `\mathcal M` and `\mathcal N` distinguished from the plainer moduli letters `M` and `U`.

Specific revision cautions accompany the doubt entries. On scan 626, the scope of cancellation around *non triviale* is less certain than the inserted reading *scindée*. On scan 632, the line through *se scinde en* is treated as cancellation in view of the replacement immediately following. The inserted noun over *section* on scan 635 is attached at that word without regularizing agreement. In diagram (38), deleted uncertain arrow glyphs are attached to the canceled edges; those glyphs record the old decoration rather than an additional active morphism. The faint inscription in diagram (37) is retained without assigning an unsupported cancellation state.

The `.tex` file is a fragment, with no preamble or macro definitions. It uses the requested state macros, standard LaTeX mathematical commands, and `tikz-cd`. All diagrams have explicit display contexts and macro-safe matrix separators. For compilation the receiving document must define the state macros and load the usual mathematical and TikZ-CD packages; `\diagram` can be an identity wrapper because the fragment supplies the display context. The complete fragment was compiled with temporary editorial macro definitions, and the rendered diagrams were inspected. The temporary compilation wrapper and PDF are working verification files and are not part of the three-file deliverable.

## 2. Table of doubts

Locations refer to approximate manuscript lines, a named display, or an explicitly located margin, rather than to LaTeX source lines. **High**, **medium**, and **low** describe confidence in the proposed primary reading; none removes the explicit doubt mark in the transcription. Repeated occurrences are listed separately where their ink differs, or grouped where the table expressly identifies the repeated positions. Additional entries record uncertain revision scope, missing arrowheads, and the unsupported *à un* that has deliberately not been inserted on scan 629.

| Scan | Approximate manuscript line or position | Primary reading | Alternatives or qualification | Confidence |
|---|---|---|---|---|
| 625 | Opening formula, (20) | `20` | The second digit is compressed; the written label is not fully clean. | medium |
| 625 | Lines 3–4, insertion after *alors* | `μ_{τ′} normalise L_ρ` | The reference mark points back to the first formula; the two similar small glyphs are treated as editing reference marks, not additional mathematical letters. Exact attachment remains uncertain. | medium |
| 625 | Line 3, deletion before *car* | `ce` | Very short cancelled word; no secure alternative. | low |
| 625 | Line 8, parenthesis | `dans` | Its middle strokes are weak. | medium |
| 625 | Line 9, cancelled term in intersection | `{1}` | Dense cancellation; brackets and numeral are uncertain. | low |
| 625 | Underbrace below (21) | `\mathcal M(-\bar\jmath)` | A prime after `\mathcal M` may be absent or lost among the strokes; it has not been supplied. | medium |
| 625 | Right of (21), deleted formula | `≃\mathcal M_0×μ` | Heavy over-writing obscures both the group adornment and the first relation. | low |
| 625 | Line 16 | `disposition` | The compressed middle letters are not fully separable. | medium |
| 625 | Following product display, deleted term | `Z_{ρ,0}^!×μ` | Several symbols are heavily crossed out. | low |
| 625 | Same display, last factor | `Z_{ρ,0}^?` | Alternative `Z_{ρ,0}^!`; the raised mark is poorly resolved. | low |
| 625 | (22), last horizontal stroke | Stroke without a definite head | A right-pointing arrow may have been intended, but no head is supplied in the diplomatic diagram. | medium |
| 625 | Final extension, about line 24 | `\mathcal N_ρ^{*}` | Alternative `\mathcal N_ρ^{\wedge}`; the superscript has caret-like rather than clearly star-like strokes. | low |
| 626 | (23), lower left group | `\mathcal N_ρ^*` | The upper mark is congested and may contain an overwritten superscript. | medium |
| 626 | (23), deletion before `L_ρ` | `\mathbb Z` | Several vertical strokes are present; identity of the cancelled object is insecure. | low |
| 626 | About line 4, name of preceding extension | `\widetilde\gamma_ρ` | Exact tilde/subscript placement is uncertain. | medium |
| 626 | About line 5, underlined conclusion | `non` retained before the replacement | The long cancellation may include part of *non*. It is not confidently asserted that the entire phrase was cancelled. | low |
| 626 | About line 5, insertion over *triviale* | `scindée` | Independent visual readings favour this word; the cancellation/replacement scope is less secure than the word itself. | medium |
| 626 | About line 6 | `hom` | Abbreviation rather than expanded *homomorphisme*; last stroke is weak. | medium |
| 626 | Remark, about line 10 | `τ′` | Alternative `τ`; the prime is not unambiguous. | medium |
| 626 | About line 12, cancelled subscript | `\mathbb Q` | Deleted part after `Γ` in the subscript of `τ`. | low |
| 626 | About line 13 | `autom.` | The abbreviated word before *int.* is compressed. | medium |
| 626 | About line 16 | `hom` | Same abbreviation shape, less distinct than surrounding prose. | medium |
| 626 | Last line | `y partant` | Initial strokes and spacing permit this reading but are not clear enough for certainty. | medium |
| 626 | Last line, after `α,β` | `associés` | The ending and several middle letters are compressed. | medium |
| 627 | Line 4, cancelled group | `Γ_\mathbb Q^{\prime\prime\prime\sim}` | The cancelled adornments are insecure; the uncancelled display immediately below has its own visible signs. | low |
| 627 | About line 7 | `ou du moins` | Very compressed connective after `\mathcal M(\sqrt3)`. | medium |
| 627 | About line 8, generator | `q` | Alternative `ρ`. The occurrence in `\mathcal M(q)` is clearer than this later letter. | medium |
| 627 | Slanted left note | `Méditer ces` | The small second word is not secure. | medium |
| 627 | Same note | `coïncidences.` | Strongly compressed middle letters; the earlier candidate *cas communs* was not retained after reinspection. | low |
| 627 | Same note | `Attentif.` | Alternative abbreviated `attentiv.`; ending unresolved. | low |
| 627 | About line 10 | `déconner` | The word is forceful and clearly begins *décon-*, but the last strokes are compressed. No euphemistic correction is made. | medium |
| 627 | Just below (25) | `au` | Short preposition before the tilde notation. | medium |
| 627 | About line 17, word in quotation marks | `inévitablement` | Alternative `invariablement`; *inavouablement* was another tentative visual candidate, less convincing on reinspection. | low |
| 627 | Above *points*, about line 17 | `rat./\mathbb Q` | The initial abbreviation could be misread; the `/Q` portion is clearer. | medium |
| 627 | About line 20, cancelled adjective | `privilégiée` | Replacement *envisagée* is clearer; the cancelled word is uncertain. | low |
| 627 | About line 22, deletion before *section* | `quasi-` | Compact deletion obscures middle letters. | medium |
| 627 | About line 24, cancelled base-field subscript | `\mathbb Q` | Small crossing over the subscript of `U_{0,3}`. | low |
| 627 | Penultimate passage, superscript of `\mathcal N_ρ` | `\sim` | Alternative `?`; the shape differs from the clear question marks elsewhere. | medium |
| 628 | About line 14, lifting group | `\mathcal M_μ` | Alternative unadorned `\mathcal M`; a small lower-right blob is visible and has not been erased. | low |
| 628 | About line 15, extension symbol | `\mathcal N_ρ^?` | Alternative starred superscript; the small mark is not fully clear. | medium |
| 628 | (26), lower-right object | `\mathbb E^1` | Alternative `\mathbb E′`; vertical upper-right mark unresolved. | low |
| 628 | (26), small mark under the target | `0` | Alternative open circle `\circ`; it is distinct from the comma at the far right of the diagram. | low |
| 629 | Line 2 | `\mathbb E^1` | Alternative `\mathbb E′`. | low |
| 629 | (27), rightmost object | `\mathbb E^1` | Alternative `\mathbb E′`. | low |
| 629 | (28), second denominator, after *i.e* | `s` with raised `s`, followed by *groupe* | Alternative raised `t`; the abbreviation is not expanded in the transcription. | low |
| 629 | Above `M′_{1,1}`, about line 14 | `rat/Q` | First letters are abbreviated and partly joined to the insertion line. | medium |
| 629 | About line 14, after *s'identifie* | No supplied *à un* | Neither independent reader found ink for *à un* after this occurrence or clearly at the next line's left edge; the grammatical gap is left as written. | medium |
| 629 | Slanted margin, first line | `sous SL(2,Z/2Z)` | Small added words are overwritten; exact cancellation state of the first word is uncertain. | low |
| 629 | Slanted margin, first long word | `privilégiations` | Alternative `rigidifications`; a descender early and a tall stroke later allow either candidate. | low |
| 629 | Slanted margin, quoted repetition | `privilégiations` | Alternative `rigidifications`; not independently resolved by the first occurrence. | low |
| 629 | Slanted margin, order condition | `≤4` | Alternative `4` with a preceding stray/overwritten stroke; the relation is kept doubtful. | low |
| 629 | Slanted margin, end of quoted phrase | `précisées` | Individual middle strokes cannot be separated confidently. | medium |
| 629 | Slanted margin, parenthesis | `ellipt.` | The contracted ending is compressed and overlaps neighbouring ink. | medium |
| 629 | (30), horizontal stroke | Stroke without definite head | No arrowhead is supplied where the enlarged image shows only a short horizontal stroke. | medium |
| 629 | Below (30), cancelled object after *par* | `T` | Several intersecting strokes obscure the cancelled letter. | low |
| 630 | Upper-left note, second line | `maintenant` | Compressed writing; no secure alternative. | medium |
| 630 | Upper-left note, cancelled word after *pt* | `géom.` | A descending stroke survives the cancellation, but the word is not fully recoverable. | low |
| 630 | About line 9 | `élém` | Abbreviation may have an unresolvable terminal point; not expanded. | medium |
| 630 | About line 12, second element of set | `-j` | Alternative `-\bar\jmath`; both the sign and the mark over the letter are heavily overwritten. | low |
| 630 | Left correction beside underlined claim | `erroné` | Alternative `corrigé`; the lack of a clear descender favours *erroné*, while *cf rectification plus bas* is clear. | medium |
| 630 | After *De façon générale*, deletion | `on doit` | The first word is weak, the second has clearer *d/t* strokes. | low |
| 630 | Label of composition arrow, about line 21 | `k` | Alternative Greek `κ`; the ink does not securely distinguish them. | medium |
| 630 | After *ssi*, deletion | `Γ_\mathbb Q` | Crowded cancellation; lower `Q` is more visible than the first letter. | low |
| 630 | Insertion above that deletion | `k` | Alternative `κ`, matching the unresolved arrow label. | medium |
| 630 | Last two lines, restriction and image | `k` in both occurrences | Alternative `κ`; retained as explicit alternatives at both occurrences. | medium |
| 631 | Upper paragraph, line 2, canceled after `\mathcal G_3` | `est` | Short crossed stroke; reading may be only a canceled start. | low |
| 631 | Upper paragraph, line 4, after `que` | canceled `T` | Overwritten character can also be a discarded word-start. | low |
| 631 | Line containing `ext. quadratique de Q` | closing `)` | Curled mark could be another closing delimiter; duplicate closing punctuation is not repaired. | low |
| 631 | First oblique marginal note, denominator in `SL(2,Z)/…` | `\Pi_0` | `\Pi`; the low stroke is difficult to separate from neighboring writing. | medium |
| 631 | End of first marginal note | `canoniquement` | Word is divided `cano- / niquement` in the margin; ending is compressed. | high |
| 631 | After the extension display, `et le … d'obstruction` | `pb` | Compressed abbreviation, possibly with a terminal stroke rather than a clear `b`. | medium |
| 631 | Below lifting triangle, canceled before `n'existe` | `l'on` | Crossed short expression; only part of its letter sequence survives. | low |
| 631 | Second oblique marginal note, opening | `effet` | `fait`; handwriting reduces the middle letters to strokes. | medium |
| 631 | Same marginal opening, before colon | `qu'on` | `puisque`; the surviving word and punctuation do not separate cleanly. | low |
| 631 | Second marginal note, between `\widehat Z^*` and `Z_3^*` | `\supset` | `\twoheadrightarrow`; shape and possible arrowhead remain ambiguous. | low |
| 631 | Second marginal note, after `(Z_3^*)_4 ≃ Z/2Z` | `donc déjà sur` | Word grouping is tentative where the note meets the main writing. | low |
| 631 | End of second marginal note, after `Z_3^*` | `ça ne se remonte pas` | Several letters are abbreviated to strokes; the phrase is a proposed reading, not an inferred completion. | low |
| 632 | Opening line, continuation from scan 631 | `scindée` | Ending somewhat compressed; independent comparison also favors this reading. | high |
| 632 | Lines 6–7, coarse-moduli target | `\mathbb E^1` | `\mathbb E'`; short upper-right stroke. | medium |
| 632 | Left of the first pair of arrows, canceled symbol | `P` | Overwritten shape is only partly preserved. | low |
| 632 | Before the displayed fiber product, canceled formula | `Q=P` | Dense cancellation; the visible `Q`- and `P`-shaped remnants do not securely determine the relation. | low |
| 632 | Fiber-product subscript | `\mathbb E^1` | `\mathbb E'`; same stroke ambiguity as above. | medium |
| 632 | After `P_0=Q_{red}`, canceled sign | `\simeq` | Could be an abandoned relation-sign stroke. | low |
| 633 | Upper-right NB, line 5 | `trivial` | Ending may have a faint final `e`; no grammatical correction has been imposed. | medium |
| 633 | Main paragraph, first coarse-moduli target | `\mathbb E^1` | `\mathbb E'`. | medium |
| 633 | After `G_3`-torseurs `P`, `resp` | terminal `.` | The final point is not cleanly separated from the next stroke. | medium |
| 633 | Main paragraph, `P=T de façon …` | `particulièrement` | Several interior letters are reduced to a continuous wavering line. | medium |
| 633 | Same phrase | `trivial` | `triviale`; final inflection not securely visible. | medium |
| 633 | Second coarse-moduli target, above long interline note | `\mathbb E^1` | `\mathbb E'`. | medium |
| 633 | Same line, before `de m̄ aux` | `correspondent` | End of verb is compressed; primary reading supported by visible stem. | medium |
| 633 | Canceled beginning before `Considérons` | `De là` | The two-word remnant is heavily crossed. | low |
| 634 | First line, third conjugate subgroup | `\dot\sigma_1` | `\bar\sigma_1`; the mark over sigma is elongated. | medium |
| 634 | Main paragraph, canceled word after `et` | `quel` | Possible incomplete or longer word beginning `quel-`. | low |
| 634 | `exercice plaisant et …` | `délectable` | Letter sequence is fairly persuasive, but the compressed middle and ending remain marked. | high |
| 634 | Lower paragraph, `les … de un remontage` | `prises` | `points`; the manuscript's unusual `de un` and `d'l'hom` are retained. | medium |
| 634 | Last line, first group in the kernel position | `\mathcal G_{0,3}^{+\wedge}` | `\widetilde{\mathcal G}_{0,3}^{+\wedge}`; a superposed stroke may be a tilde or a canceled earlier part of the letter. | low |
| 635 | Upper line, canceled group name | `\mathcal N_\rho^{?}` | Dense overtracing; the question-shaped mark is clearer than the letter. | low |
| 635 | Upper small inclusion diagram, edge of index 3 | `\subset` | Overwritten inclusion sign; direction is read from the visible open side, but its precise decoration is uncertain. | medium |
| 635 | `contenant … section` | `la` | `le`; the vowel is compressed and the nearby insertion changes the noun without necessarily changing the article. | low |
| 635 | Above canceled `section` | `sous-groupe` | `sous-groupes`; terminal stroke could be an `s`. | medium |
| 635 | (32), definition marker under first term | `dfn` | `def`; the tiny middle and final strokes are ambiguous. | medium |
| 635 | (32), canceled expression before `Z_\rho` | `\mathcal N_\rho^{?}` | `\mathcal M`; this cancellation is among the weakest mathematical readings in the range. | low |
| 635 | (32), canceled expression above last factor on first equality line | `\operatorname{Ker}\varepsilon_2` | Letter and character remnants are superposed; proposed reading only. | low |
| 635 | (32), last factor on first equality line | `\mathcal M_0^{\prime\prime!}` | `\mathcal M_0^{\prime\prime\prime!}`; two simple prime strokes and an exclamation-shaped mark are clearest. The following line visibly has the different `\mathcal M_0^{0!}`. | medium |
| 635 | Sentence between (32) and (33) | `en dessus` | `au dessus`; first short word reduced to strokes. | medium |
| 635 | (33), canceled relation to `\widetilde\Gamma_Q` | `\ne` | `=`; cancellation line may supply the apparent diagonal. | low |
| 635 | Before (34), `considérons …` | `les` | `le`; short ending not secure. | medium |
| 635 | (34), canceled old name after `\mathcal M'''(-\bar j)` | `\mathcal N_{\rho,0}^{?}` | Remnant identifies rho and lower circle more securely than the overwritten superscript. | low |
| 635 | (34), definition marker | `dfn` | `def`; same minute abbreviation as in (32). | medium |
| 635 | (35), canceled old name to the left of the map | `\mathcal N_{\rho,0}^{?}` | The overwritten superscript remains particularly weak. | low |
| 635 | Last two lines | `en dessus` | `au dessus`. | medium |
| 636 | (36), locally canceled symbol above `\mathcal N_\rho^*` | `\mathcal M'''` | Only portions of the letter and prime strokes remain. | low |
| 636 | (38), identification written below `\mathbb D_\rho` | `\mathbb D_6` | `\mathbb D_\sigma`; handwritten 6 and sigma are hard to distinguish here. | medium |
| 637 | Diagram (37), faint inscription between \(Z_{\rho,0}^{!}\) and \(\mathcal N_\rho^{?}\) | \(\mathcal M'(-\bar j)\times\mu\) | The very faint formula is independent of the darker vertex labels; its state as an abandoned or simply faint inscription is uncertain. It is not marked deleted without visible cancellation. | medium |
| 637 | Same faint diagonal stroke | Down-right arrowhead | The stroke is clear enough to retain, but its terminal decoration cannot securely be distinguished from an unheaded stroke. The diagram carries an uncertain \(\searrow\) decoration. | low |
| 637 | First prose line below (37) | surtout | No secure alternative; the ending is reduced to a stroke. A second reader also favored surtout. | medium |
| 637 | Following line, after “face supérieure” | contenant | concernant; the middle letters run together. | medium |
| 637 | Prose line ending “entre celui-ci et” | \(\mathcal M_0(-\bar j)\) | \(\mathcal M^0(-\bar j)\); the position of the small zero is unusually low here. No normalization from the diagram has been imposed. | low |
| 637 | Parenthesis “d'indice 24 dans …” | Star on \(\mathcal N_\rho\) | The small superscript is compressed; no secure other reading. | medium |
| 637 | Last paragraph, “qui montre … les” | vraiment | mieux; both are possible under the rapid joining strokes. | low |
| 637 | Last paragraph, canceled word before “relations” | groupes | rapports; the deletion hides most individual letters. The loop and descender support only a tentative word. | low |
| 638 | Diagram (38), outer dashed left curve between two \(Z_\rho\) positions | Two arrowheads | A downward hooked arrow is also possible; the upper tip is pointed rather than the clear rounded hooks elsewhere. The doubtful decoration is marked in the diagram. | low |
| 638 | Diagram (38), central object on the dashed horizontal from \(Z_\rho\) | \(\mathcal N_\rho\) | \(\mathcal N_\rho^{*}\); the superscript area is crossed by another stroke. | low |
| 638 | Diagram (38), long dashed curve from the central \(\mathcal N_\rho\) position to the upper \(\mathcal N_\rho^{*}\) | Two arrowheads | The two terminal decorations are small and intersect neighboring material. | low |
| 638 | Diagram (38), canceled diagonal from \(\mathcal M^0(-\bar j)\times\mu\) toward the crossed lower-left vertex | Hooked arrow | Cancellation makes the original source decoration uncertain. A deleted uncertain hooked-arrow mark is retained on this edge. | low |
| 638 | Diagram (38), canceled diagonal from \(\mathcal M'''(-\bar j)\times\mu\) toward the crossed lower-central vertex | Hooked arrow | Same difficulty as the parallel canceled edge. | low |
| 638 | Diagram (38), crossed lower-left vertex | \(L_\rho\) | Heavily overwritten; no secure alternative. A second reader also favored \(L_\rho\). | low |
| 638 | Diagram (38), canceled horizontal edge between crossed vertices | Hooked arrow | Its original terminal decoration is obscured by cancellation. | low |
| 638 | Diagram (38), crossed lower-central vertex | \(\mathbb D_\rho\) | Heavily overwritten; no secure alternative. A second reader also favored a doubled \(D_\rho\). | low |
| 638 | Heading below (38) | a) | The character is very small and could be another item marker. | medium |
| 638 | Diagram (39), upper-right endpoint after \(Z_{\rho,0}^{!}=\) | Superscript \(*!\) on \(\mathcal N_{\rho,0}\) | Both a star-like and exclamation-like stroke appear; their exact grouping is insecure. | low |
| 638 | Before display (40), canceled formula after “sous-groupes” | \(\mathcal M'(-\bar j)\) | Multiple strokes are canceled; no secure other formula. | low |
| 638 | Display (40), canceled fragment beside the second line | \(\mathcal M^0(-\bar j)\times\mu=\) | The extent of the erased fragment is uncertain. The visible candidate has been kept in place. | low |
| 639 | Second line, canceled item before \(Z_\rho,\mathcal M^{!},\operatorname{Ker}\varepsilon_2\) | \(\mathcal M^{!}\) | No secure alternative under the strokes. | low |
| 639 | Start of the line below “d'indice 2” | Deleted dans | It is immediately replaced by an inserted dans; the underlying letter shapes are partly hidden. | medium |
| 639 | Following line before “montrer qu'il l'est” | pour | The initial letter and joining strokes are compressed. | medium |
| 639 | Approximately line 8, canceled fragment before \(x\in\mathcal M\) | \(x\in\) | No secure other reading; this is a false start. | low |
| 639 | Same line, canceled formula after “normalise” | \(\mathcal M_0^{!}\) | Indices partly hidden by cancellation. | low |
| 639 | Display (*), superscript on \([x,u]\) | \(c\) | Small c-like superscript; its function is not inferred. A second reader agreed with the shape. | medium |
| 639 | Display (*), inserted exponent over \(\operatorname{sg}(x)\) | \(\xi_2(u)\) | \(\varepsilon_2(u)\); the descender favors \(\xi\), unlike the clearer \(\varepsilon_2\) later. | medium |
| 639 | Display (*), deleted baseline factor after \(\operatorname{sg}(x)\) | \(\xi_2(u)\) | \(\varepsilon_2(u)\); stronger cancellation than in the inserted exponent. | low |
| 639 | “Cela montre … que”, before Lemme | Deleted qu'on | No secure alternative. | low |
| 639 | Lemma, condition c), inserted exponent | \(\xi_2(u)\) | \(\varepsilon_2(u)\); the same distinction as in (*). | medium |
| 639 | Lemma, condition c), canceled baseline factor | \(\xi_2(u)\) | \(\varepsilon_2(u)\); original placement is clear, individual letters less so. | low |
| 640 | Entirely canceled first line, after “cela montre que” | le | la; the small vowel is crossed by the deleting stroke. | low |
| 640 | Same canceled line, baseline noun | condition | No secure alternative; an insertion above it further obscures the baseline. | low |
| 640 | Same canceled line, inserted words over the noun | premier groupe | A second reader also favored this reading; several middle letters are joined. | medium |
| 640 | End of the canceled first line | est | No secure alternative under the long cancellation. | low |
| 640 | Second half of page, after “distingués dans” | \(\mathcal N_\rho^{*}\) | Overwritten \(N\)-like letter; the star is retained. | medium |
| 640 | Revision above the canceled \(\mathcal M^0(-\bar j)=Z_\rho\cap\mathcal M_0^{\prime\prime!}\), after inserted “voir” | Deleted si les | The short canceled words are difficult to separate from the inserted “les quels des”. | low |
| 641 | Second prose line, under inserted il | Deleted on | donc; only two low humps remain. The horizontal mark also has arrow-like ends, so its cancellation versus editorial-pointer status is uncertain. | low |
| 641 | Same line after opère | Deleted \(Z\) | A Z-like crossed glyph is visible, but no secure other reading or index can be recovered. | low |
| 641 | Display (43), canceled short glyph after alors | \(\tau\) | Possibly a short word such as et or another formula false start; the loop is heavily crossed. | low |
| 641 | Corollaire, “dans …” | \(\mathcal N_\rho^{*}\) | The main letter is overwritten; star and lower \(\rho\) are retained. | medium |
| 642 | Second line | s-groupes | ss-groupes, or a second s written above the first; the abbreviation is highly contracted. | medium |
| 642 | “d'indice 24 dans …” | \(\mathcal N_\rho^{*}\) | Overwritten subscript/superscript area; no secure other group label. | medium |
| 642 | After “Le groupe quotient” | Deleted est un | Only residual short strokes are visible. | low |
| 642 | Next line, canceled short word at left of quotient display | groupe | A large loop and crossed upper strokes remain; the word is only a tentative reading. | low |
| 642 | “normalisateur de \(L_\rho\) dans …” | \(\operatorname{GL}(2,\mathbb Z)\) | The first letter has been rewritten; \(L(2,\mathbb Z)\) is much clearer. | medium |
| 642 | Display (44), denominator | \(\mathcal M^0(-\bar j)\) | \(\mathcal M^0(\bar j)\); there is no securely separate minus before the long upper stroke of \(j\). The rest of the page has clearer minus signs. | low |
| 643 | “Essayons-le …” | ainsi | aussi; the middle strokes are thick and merged. | medium |
| 643 | Diagram (45), first upper-right quotient | Superscript \(*\) on \(\mathcal G\) | \(\wedge\); the superscript is unusually heavy. The lower equivalent quotient and the later canonical map visibly carry hats and are kept separately. | low |
| 643 | Last two manuscript words | L'image de | L'image des; the final flourish may be an s. The sentence remains unfinished exactly here. | medium |

## 3. Abbreviations and compact signs

These expansions are editorial explanations only. Written forms and local variants are listed as encountered; some recur in more than one scan range with a different local qualification. The transcription itself keeps the abbreviations.

| As written | Probable expansion or meaning | Location / qualification |
|---|---|---|
| `\overline{\mathrm m}` | même | 625–630 |
| `produit 1/2 direct` | produit semi-direct | 625–630 |
| `hom` | homomorphisme | 625–630 |
| `i.e`, `i.e.` | id est | 625–630 |
| `NB` | nota bene | 625–630 |
| `autom. int.` | automorphisme intérieur; the first abbreviation is uncertain on scan 626 | 625–630 |
| `pt` | point | 625–630 |
| `rat./Q`, `rat/Q` | rationnel sur `Q`; the inserted forms are not perfectly legible | 625–630 |
| `comp.` | compatible | 625–630 |
| `mod symétrie` | modulo symétrie | 625–630 |
| `ext.` | extension | 625–630 |
| `déf/Q` | défini(e) sur `Q` | 625–630 |
| `sch. mod.` | schéma modulaire | 625–630 |
| `ell.`, `ellipt.` | elliptique(s) | 625–630 |
| `gr.` | groupe | 625–630 |
| `s` with raised `s` or `t`, before *groupe* | probably sous-groupe; exact abbreviation uncertain | 625–630 |
| `isom` | isomorphisme | 625–630 |
| `élém` | élément | 625–630 |
| `cf` | confer / comparer | 625–630 |
| `ssi` | si et seulement si | 625–630 |
| `Cent` | centralisateur | 625–630 |
| `Ker` | noyau | 625–630 |
| `Br` | groupe de Brauer, as named by the notation in the obstruction passage | 625–630 |
| `i.e.` | *id est*, c'est-à-dire | 631–636; high confidence |
| `ext.` | extension | 631–636; high confidence |
| `pb` | problème | 631–636; medium confidence |
| `ab` in `(Γ_Q)_{ab}` | abélianisé / abélianisation | 631–636; high confidence |
| `pt`, `pts` | point, points | 631–636; high confidence |
| `hom` | homomorphisme; in a `G`-hom, an equivariant morphism is intended by the displayed setting | 631–636; high confidence |
| `d'l'hom` | de l'homomorphisme | 631–636; medium confidence |
| `can.` on an arrow | canonique | 631–636; high confidence |
| `can.` with raised `l` | canoniquement | 631–636; medium confidence |
| `NB` | nota bene | 631–636; high confidence |
| `isom.` | isomorphe | 631–636; high confidence |
| `resp.` | respectivement | 631–636; high confidence |
| `mod` | modulo | 631–636; high confidence |
| `sg` | signature / signe | 631–636; high confidence |
| `m̄` | même | 631–636; high confidence |
| `épi` | épimorphisme | 631–636; high confidence |
| `Ker` | noyau (*kernel*) | 631–636; high confidence |
| `dfn` / `def` over or under an equality | définition / par définition | 631–636; medium confidence |
| `red` | réduit | 631–636; high confidence |
| `SL` | groupe spécial linéaire | 631–636; high confidence |
| \(\overline{\mathrm m}\) | même | Scans 640 and 642; the wavy lower stroke with an overbar is kept as a sign. |
| dfn | définition | Scan 639, above the defining equals sign. |
| i.e. | id est / c'est-à-dire | Scan 639. |
| mod | modulo | Scan 639, display (*). |
| can | canonique | Scan 639, arrow defining sg. |
| sg | signe / signature | Scan 639, written as the label of a homomorphism; the exact established terminology requires earlier definitions. |
| s. | Probably suffit | Scan 640, “il faut s. qu'on ait”. No missing conjunction has been supplied in the transcription. |
| s-groupes / ss-groupes | sous-groupes | Scan 642; exact number/position of s strokes is doubtful. |
| hom. | homomorphisme | Scan 643. |
| épi. | épimorphisme | Scan 643, “épi. de degré 4”. |
| corr. | correspondance | Scan 643. |
| \(1\)-\(1\) | One-to-one / biunivoque | Scan 643; written with the intervening dash. |
| \(\pm\) in “c'est ± trivial” | plus ou moins | Scan 639; colloquial shorthand, not a mathematical equality. |

## 4. Legibility and limits

The continuous French prose is generally recoverable after enlargement. Compressed endings, minute superscripts, and words or formulas overwritten by corrections are less secure. The least trustworthy prose is in the slanted notes on scans 627, 629, and 631 and the canceled first sentence on scan 640. The weakest mathematical readings are the dense cancellations in (21) and (32), the small adornments in (34)–(35), the faint inscription in (37), the long dashed and canceled edges in (38), the revised exponent in (*) on scan 639, and the heavy right-hand superscript in (45).

Several differences have been preserved despite the temptation to regularize them: the question-shaped superscript on `\mathcal N_\rho`; the ambiguous coarse-moduli target `\mathbb E^1` versus `\mathbb E'`; the distinction between `\xi_2` and `\varepsilon_2` in scan 639; the unprimed `\tau` at the end of (42); and the unstarred `\mathcal N_\rho` in the final paragraph of scan 641. The parenthesized entry in `\mathcal M(0)` was independently examined and read as a single zero. These choices record the visible forms; they do not assert consistency of the mathematics.

All doubtful material has a proposed reading in place. No mathematical symbol has been replaced by an illegibility placeholder, and no proof or unfinished formula has been completed from context. The low-confidence readings remain unresolved evidence requiring comparison with the scan. The inventory records the represented elements; its `yes` values certify inclusion, not certainty of decipherment.

## 5. Research notes

These English notes concern questions, deferred arguments, and possible investigations suggested by the supplied passage (Grothendieck, 1981). They make no claim that a question remains open in the literature or later in the manuscript, and no claim of novelty. The short quotations identify the author's statements; doubtful quoted words remain identified as doubtful. Items explicitly labeled **own idea** are proposals for further checking, with their confidence and reason stated. They have not been used to change the transcription.

### Scans 625–630

1. **Scan 625, lines 13–19 — unproved claim.** “`μ_{τ′} ne normalise pas Z_{ρ,0}^!`” is the decisive warning against the displayed direct-product decomposition that follows as a rejected possibility. A proof or verification would need the conjugation action on the two factors and an explicit element or character detecting the failure of normality.

2. **Scan 625, (22) and final paragraph — unpursued implication.** “`une quasi-section de multiplicité 2`” identifies the extension by `μ` as the remaining discrepancy between the proposed quasi-section and a genuine section. It would be useful to track precisely which quotient and which finite-index restriction remove that discrepancy; the next scans begin doing this, but the warning on this page should not be lost in a simplified product notation.

3. **Scan 626, opening paragraph — unproved claim.** “`elle est sûrement`” precedes the heavily revised *non triviale / scindée* passage. The exact assertion depends on the cancellation scope; any mathematical commentary should first settle that textual issue, then supply the relevant splitting or nonsplitting argument rather than read the word *sûrement* as a proof.

4. **Scan 626, remark — conjecture.** “`il y a fort à parier que celui-ci est justement ε₂`” proposes a specific quadratic character for the extra component of the action. The calculation sought is explicit: extract the `μ` coordinate after conjugation, compare it with `ε₂`, and check the resulting invariance of the displayed intersection of the two subgroups of `Γ_\mathbb Q^{\sim}`.

5. **Scan 626, final paragraph — unpursued implication.** “`il y aurait lieu de reprendre l'étude de l'extension`” proposes revisiting the preceding construction from the viewpoint of the associated `α,β`. Since their definitions are not supplied in these six scans, this is a cross-reference to be checked against the earlier manuscript, not an invitation to reconstruct them from expected theory.

6. **Scan 627, opening — conjecture.** “`une autre section partielle`” over the displayed kernel of `ε₂ε₃` is proposed, together with the tentative notation `\mathcal M(\sqrt3)` or `\mathcal M(q)`. The three question marks and the adjoining marginal note indicate an unresolved identification; constructing the section and checking its field interpretation are distinct tasks.

7. **Scan 627, middle paragraph — unproved claim.** The passage says that sections correspond to points, with the quoted adverb read tentatively as “`inévitablement`”. The argument would need precise hypotheses and a statement of what is meant by correspondence, by the tilde qualification, and by a partial section over a finite extension; the wording on this page alone does not establish all those implications.

8. **Scan 627, about lines 20–26 — unpursued implication.** The section in b) is compared with the point `1/2`, while the section in c) is compared with `-\bar\jmath`; the passage then stresses that the other group is “`pas ⊂ \mathcal M_0^!`”. This shifts attention from the geometry of a point on `U_{0,3}` to the lifting problem after taking the quotient by `μ`, and provides the transition to the moduli discussion.

9. **Scan 628, middle — conjecture.** “`J'ai donc l'impression ... ne peut se remonter`” states an expectation of a failure to lift the section over the full `Γ_\mathbb Q^{\sim}`. The proposed connection with a nontrivial extension is followed by the question about a curve “`d'invariant 0`” and the author's immediate doubt, “`Alors que semble absurde`”; these are stages of the investigation, not a settled nonexistence claim.

10. **Scan 628, (26), continued on scan 629 — own idea.** Compare the obstruction for a fixed point of `M′_{1,1}` with the set of all points above its coarse-moduli image, keeping the two fibres separate throughout the calculation. **Confidence: high as a useful diagnostic**, because the next page explicitly says that the failure of the first lift “`ne signifie pas`” failure of a lift of its image; this is a proposal for organizing the calculation, not a claim of novelty.

11. **Scan 629, (27)–(30) — unproved claim.** The identifications of the two moduli objects with quotient descriptions lead to the assertion that the datum in (30) “`équivaut à la donnée de (29)`” after forming `T=\widetilde T/μ`. A full check should identify the action of the kernel on `U_{0,3}`, the equivariance conditions, and the equivalences between the indicated torsor groupoids rather than only their object sets.

12. **Scan 629, slanted margin — unpursued implication.** The margin contrasts a construction defined “`pour une courbe ... mod symétrie`” with one defined “`seulement pour une vraie courbe elliptique`”. Its two long technical nouns and the order condition are doubtful readings, so the intended interpretation through finite-level structures should be verified against the ink before it is used as an explanation of the torsor lift.

13. **Scan 630, obstruction paragraph — unproved claim.** “`l'obstruction est, comme il se doit`” identifies the obstruction with an extension by `μ₂` and then with an element of `H²(\mathbb Q,μ₂)≃ {}_2 Br(\mathbb Q)`. The passage states the identification but does not compute the class here; the concrete pullback extension associated with the chosen torsor is the object to calculate.

14. **Scan 630, underlined conclusion and margin — unproved claim.** The underlined assertion “`donc Γ_\mathbb Q→\mathcal G_3 est surjectif`” has the adjoining correction “`[erroné/corrigé], cf rectification plus bas`”. It must be recorded as a revised claim, and the later conclusion on this same page that the image has order 2 must be checked against the proposed argument from connectedness.

15. **Scan 630, final paragraph — own idea.** Compute the image of the torsor homomorphism first, then pull the finite extension back along that actual image, rather than use surjectivity inferred from the two-point image in `U_{0,3}`. **Confidence: high as a verification strategy**, because the handwritten correction and the subsequent order-2 conclusion already isolate the problematic step; the expected obstruction remains to be calculated.

### Scans 631–636

#### R631.1 — Conjecture / expectation: the middle extension is cyclic of order four

**Source:** Scan 631, paragraph before the first extension display and first marginal note. Grothendieck writes, “ça ne peut guère être que `Z/4Z` !”, then adds an argument using the order of the image of `σ=σ_∞`. A full verification would distinguish the two extensions of the displayed order-two group by `μ`, identify the indicated inverse image inside `\widetilde{\mathcal G}_3`, and check the claimed order of the chosen lift. The margin's “canoniquement” also raises the separate issue of which choice makes the identification canonical.

#### R631.2 — Unproved claim: the displayed lifting problem has no solution

**Source:** Scan 631, below the lifting triangle and the lower marginal note. The words “n'existe sûrement pas” concern a lift of the displayed Galois homomorphism through the middle extension. The marginal appeal to abelianization and `Z_3^*` appears to be a compressed justification, but several readings there remain weak; a proof should first reconstruct the precise character and quotient appearing in that note.

#### R631.3 — Own idea: make the pullback extension explicit

**Source:** Scan 631, phrase “image inverse de l'extension” and the lifting triangle. **Confidence: high as a proposed organization of the calculation; no vanishing or nonvanishing conclusion asserted.** One can write the pullback of the displayed extension along the Galois character and formulate the question as whether that pulled-back extension splits. This follows directly from the drawn square and provides a way to separate the group-extension data from the less legible marginal calculation.

#### R632.1 — Unproved claim left for explanation: behavior after adjoining `sqrt(3)`

**Source:** Scan 632, first three lines continuing scan 631's “Il faudrait regarder pourquoi, en termes classiques”. The manuscript says the obstruction is “scindée” after passing to the indicated subgroup corresponding to `Q(sqrt(3))`. The precise extension, action on its kernel, and meaning of this restriction should be reconstructed before giving the requested classical explanation; the field is transcribed without a minus sign.

#### R632.2 — Unpursued implication: compare a chosen point with its coarse image

**Source:** Scan 632, “ne se remonte pas” followed by “son image 0 … doit bien se remonter”. The argument distinguishes failure to lift one chosen rational point of `M_{1,1}'` from the expected existence of a lift of its coarse image. An explicit comparison of the corresponding torsors would clarify how those two statements coexist and which choices of torsor over the same reduced fiber are being varied.

#### R632.3 — Unproved claim: the reduced fiber and its action

**Source:** Scan 632, definition `P_0=Q_{red}` and “can.l isomorphe à Spec Q(-bar j)”. The text identifies the reduced fiber, describes its two points after extending the field, and says the `\mathcal G_3`-action factors through the sign map. A proof would calculate the fiber scheme, separate its reduced part from any multiplicity, and verify the action on those two geometric points.

#### R633.1 — Unproved claim: identify the kernel as a cyclic group of order six

**Source:** Scan 633, NB: “extension centrale”, “isom. à `Z/6Z`”, and “noyau engendré par `ρ`”. The margin compresses both a splitting assertion and a generator assertion. Checking the order of `ρ`, its image in the order-three quotient, and the central order-two subgroup would make the identification precise.

#### R633.2 — Unproved claim: the equivalence between point-lifting and torsor-lifting categories

**Source:** Scan 633, “la catégorie des relèvements … est équivalente à celle des … torseurs”. The statement includes the equivariant map to the underlying scheme, not only the abstract torsor. A detailed construction in both directions should also explain why isomorphism classes are described by conjugacy modulo the indicated kernels, as specified by the interline insertion.

#### R633.3 — Unpursued implication: failure for the preferred splitting does not settle all lifts

**Source:** Scan 633, “On avait choisi un `P=T`” and “mais le torseur `T` ne se remonte pas”. The chosen split image of the order-two group gives one torsor in the fiber, whose failure to lift leaves other torsors to be examined. The transition to considering the image of a general homomorphism is the beginning of that wider classification problem.

#### R634.1 — Unproved claim: a liftable homomorphism must have full image

**Source:** Scan 634, first paragraph: “il faut prendre un épi”. The argument excludes the order-two subgroup and its conjugates before passing to the full group. To make the reduction complete, one should verify that the subgroup list is exhaustive under the prescribed sign character and that nonlifting is unchanged under the stated conjugacies.

#### R634.2 — Conjecture / question explicitly deferred: existence and classification of full-image lifts

**Source:** Scan 634, “s'il existe un tel relèvement” and “comment les obtenir”. Grothendieck calls this an “exercice plaisant et délectable” in class field theory, then says he will not pursue it “pour le moment”. The existence problem and classification of all such lifts should be kept separate; neither is supplied on this page.

#### R634.3 — Unpursued implication: relate homomorphism lifts to sections of the larger extension

**Source:** Scan 634, final paragraph: “il me faudrait en m̄ temps expliciter la relation”. The requested comparison is between choices of lift of the Galois homomorphism and splittings of the displayed extension by the completed group. A precise comparison would need to preserve the relevant equivalence relations, especially conjugacy by the geometric kernel and any distinction between a chosen representative and its class.

#### R635.1 — Unproved claim left for later: normalization by `τ'`

**Source:** Scan 635, “Modulo une vérification que je vais faire plus bas, `τ'` normalise…”. This is explicitly a deferred verification on which the semidirect-product construction in (34) depends. A proof should compute the action on the defining kernel of `ε_2`, then check the intersection with the order-two factor and the stated index four.

#### R635.2 — Unproved claim: compare the two kernel descriptions

**Source:** Scan 635, (32)–(33). The manuscript gives both the pair-of-characters kernel and the kernel of the cyclotomic map followed by reduction modulo 12. Verifying their equality requires identifying the two displayed characters on that quotient; one should first resolve the changes of notation in the canceled right-hand side of (32), rather than silently identify its distinct prime and circle superscripts.

#### R635.3 — Unpursued implication: check the partial section after forming the semidirect product

**Source:** Scan 635, (35) and “c'est une section partielle”. The displayed isomorphism to `\widetilde\Gamma_Q'''` asserts more than the existence of a subgroup: it asserts the behavior of the projection on that subgroup. Once normalization is established, checking its kernel, image, and compatibility with the previously defined partial section would justify this step and the announced isomorphisms on the next page.

#### R636.1 — Own idea: use the canceled index diagram as a consistency check, not as a proved lattice

**Source:** Scan 636, canceled diagram (37). **Confidence: high for the numerical observation; low as evidence of any additional group structure.** The two visible routes from `\mathcal M^0(-\bar j)` to `\mathcal N_\rho^*` have products of indices `2·6·2` and `2·4·3`, both 24. This is a useful check on the transcribed labels, but equal products do not prove the indicated containments or normality, and the whole diagram is canceled.

#### R636.2 — Unproved claim in a canceled draft: the intended finite-quotient isomorphism

**Source:** Scan 636, “induit un isomorphisme d'” and incomplete (39). The canceled draft moves from the finite subgroup `\mathbb D_\rho` to an isomorphism whose target is written only as `\mathcal N_\rho^*/`. Its denominator and precise assertion must be obtained from subsequent reasoning if they are to be discussed mathematically; they cannot be supplied to this transcription.

#### R632.4 — Own idea: test the proposed splitting at a real place

**Source:** Scans 631–632, the cyclic order-four extension and the statement that the obstruction becomes “scindée” over `Q(sqrt(3))`. **Confidence: high in the conditional elementary group calculation, moderate in its applicability here because the full notation and coefficient action precede this extract.** If the extension is literally the constant cyclic extension `C4 → C2` and the prescribed quadratic character is nontrivial on complex conjugation, no homomorphism `C2 → C4` lifts that character: every element of order at most two in `C4` maps to the identity in `C2`. Restriction to the totally real field `Q(sqrt(3))` would preserve this real-place test, so the extension, coefficient action, and meaning of “scindée” should be checked before accepting that interpretation of the assertion. This is a diagnostic to apply to the manuscript's definitions, not a correction of the transcribed field or a conclusion about the intended construction.

### Scans 637–643

#### R637.1 — Scan 637, paragraph after (37)

**Kind: conjecture / stated program.** Grothendieck writes, “Je vais examiner la question d'invariance” and also mentions “la structure des groupes quotients”. The indicated problem is to determine which finite-index intermediate subgroups in the upper part of the diagram are normal in which larger groups, and then identify the resulting quotients. Subsequent pages in this fragment address parts of this program; the diagram itself should not be read as having already settled all normality assertions.

#### R638.1 — Scan 638, right marginal warning to (38)

**Kind: unproved claim at this point.** The warning says the candidate \(\mathcal M'(-\bar j)\mu_{\tau'}\) “n'est pas un sous-groupe”, because \(\mu_{\tau'}\) does not normalize \(\mathcal M'(-\bar j)\). To substantiate this statement independently, one needs the actual conjugation action and an element that leaves the subgroup under that action. Scan 641 returns to precisely this normalization issue through \(\varepsilon_2\).

#### R638.2 — Scan 638, question below (39)

**Kind: conjecture / question.** The explicit question is, “sont ils invariants dans \(Z_\rho\)?” for the four displayed subgroups. This question is answered affirmatively on scan 640, then distinguished from normality in the larger \(\mathcal N_\rho^{*}\) on scan 641. It is useful to keep those two ambient groups separate when reconstructing the argument.

#### R639.1 — Scan 639, upper paragraph

**Kind: unproved claim.** In reducing normalization to the action of \(\rho\), the text uses \(Z_\rho=L_\rho Z_\rho^{!}\) and comments, “c'est ± trivial”. A standalone proof would need the earlier definitions of \(L_\rho\), \(Z_\rho^{!}\), and their multiplication, rather than treating the diagram as a proof of that product description. No such earlier definitions have been reconstructed from this excerpt.

#### R639.2 — Scan 639, display (*)

**Kind: unproved claim recalled from elsewhere.** The introduction “or on sait que” invokes a congruence for \([x,u]\) modulo \(\Pi_0\), expressed using \(\operatorname{sg}(x)\) and an exponent read provisionally as \(\xi_2(u)\). The lemma depends on this relation, so an independent verification must first settle the definitions and the exponent's additive or multiplicative convention. The uncertainty between \(\xi_2\) and \(\varepsilon_2\) is a textual issue as well as a possible mathematical distinction.

#### R639.3 — Scan 639, display (*) and condition c)

**Kind: own idea. Confidence: medium.** Compare the inserted exponents with the final condition \(\varepsilon_2(u)=1\) and with the earlier definitions of these characters before trying to simplify the lemma. The reason for this suggestion is physical: the inserted exponent has a descending \(\xi\)-like stroke, whereas the condition has the clearer \(\varepsilon\)-like form. They could encode related characters with different value conventions, but that interpretation is not established by the visible notation alone.

#### R640.1 — Scan 640, corollaries and intersection argument

**Kind: unpursued implication within this local argument.** The conclusion “les quatre groupes (39) sont distingués dans \(Z_\rho\)” is obtained by combining normalization with subgroup intersections. This suggests documenting exactly which ambient normalizer is available for each intersection, rather than transferring a statement about \(Z_\rho\) to \(\mathcal N_\rho^{*}\) without a new check. The next page shows why the transfer matters: one of the four subgroups fails the stronger condition.

#### R641.1 — Scan 641, displays (42)–(43)

**Kind: own idea. Confidence: medium.** A careful reconstruction could isolate the obstruction to normalization by \(\tau'\) as the nontrivial value of the displayed \(\varepsilon_2\) character, then test it on an explicit element from the earlier presentation. This is suggested by “\(\tau'(x)\in Z_{\rho,0}^{!}\Longleftrightarrow\varepsilon_2(x)=1\)”, not by an externally supplied theorem. The unprimed \(\tau\) at the end of (42) should first be compared with the author’s earlier notation; it should not be silently corrected to \(\tau'\).

#### R641.2 — Scan 641, final corollary

**Kind: unpursued implication.** The assertion that \(\mathcal M'(-\bar j)\) is the sole exceptional subgroup among the four provides a way to organize the lattice by the conjugation action of the extra involution. One can ask whether adjoining \(\mu\) removes the obstruction in each case and how that operation is reflected in the finite quotient. The fragment makes the subgroup assertions but does not yet give a complete action table for that quotient.

#### R642.1 — Scan 642, display (44) and surrounding paragraph

**Kind: unproved identification used locally.** The text calls \(\mathbb D_\rho\) a normalizer in \(\operatorname{GL}(2,\mathbb Z)\), “groupe isomorphe à \(D_6\), et d'ordre 12”. The local injectivity argument uses its intersection with the kernel, but the normalizer identification itself is not derived on this page. A complete independent account would need generators, their action on \(L_\rho\), and the precise convention for \(D_6\).

#### R642.2 — Scans 642–643, page transition

**Kind: conjecture / expectation.** The words “Il serait tentant” lead to the queried isomorphism \(\mathcal N_\rho^{*}/\mathcal M^0(-\bar j)\overset{?}{\simeq}\mathcal G^{\wedge}/\Pi_0\), compatible with the embeddings of \(\mathbb D_\rho\). This is then promoted to a proposition using a concrete composite map on scan 643. The compatibility requirement is part of the proposed identification, not merely an equality of group orders.

#### R643.1 — Scan 643, Proposition, (45)–(46)

**Kind: claim whose proof is unfinished in the supplied pages.** The proposition says that the induced homomorphism “a comme noyau \(\mathcal M^0(-\bar j)\)” and hence gives the quotient isomorphism (46). Its proof starts by writing elements as \(\alpha^{-1}u\) with conditions on \(u(\rho)\), \(\alpha(\rho)\), \(\varepsilon_2(u)\), and \(\varepsilon_3(u)\), but the supplied fragment ends at “L'image de/des”. To check the proof one must obtain the continuation or independently verify both the stated kernel and the image; neither is completed in the transcription.

#### R643.2 — Scan 643, congruence quotient in (45)

**Kind: own idea. Confidence: medium.** Build the finite map in (45) explicitly, starting with the reduction to \(\operatorname{GL}(2,\mathbb Z/4\mathbb Z)\), and compare the images of the subgroup generators from the diagrams. The reason is that (45) provides a concrete proposed route to the quotient rather than merely an abstract isomorphism claim. Such a check could clarify the degree-4 epimorphism and the compatibility with \(\mathbb D_\rho\), but it requires definitions and generators not supplied on these seven pages.

#### R643.3 — Scan 643, hats and the first right-hand superscript in (45)

**Kind: own idea. Confidence: low.** Before interpreting the completion symbols, compare this diagram with the preceding manuscript definitions of \(\mathcal G\), \(\mathcal G^{\wedge}\), and \(\Pi_0^{\wedge}\). The reason is that the top right-hand superscript in (45) is overwritten and star-like, whereas its lower equivalent quotient and the later canonical map visibly have hats. This may be a change of presentation or simply a local rewriting; the scan does not justify choosing one interpretation.

## 6. Coverage and verification

The inventory contains **337 entries** over all **19 scans**, including **26 diagrams**, **83 deletion entries**, **44 insertion entries**, and **28 marginal entries**. Every entry is marked `transcribed=yes`. The state-macro counts and the corresponding inventory kinds were reconciled page by page. The source fragment begins with `\scanpage{625}`, contains every successive scan marker through 643 exactly once, and includes no embedded images or external input files.

The doubt table contains **163 rows**, covering the explicit uncertainty marks and additional state-of-page cautions. Successful compilation checks the LaTeX structure; comparison with the source images remains the basis for the readings.

## Manuscript reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3, archive file pages 293–650; supplied scan files 625–643]. Université de Montpellier archive.
