# LM_P038 — Notes accompanying the diplomatic transcription

## 1. Source, scope, and numbering

The transcription covers the ten supplied manuscript images `LM_P038_scan371.jpg` through `LM_P038_scan380.jpg`. It was made from those images, with enlargement and independent checks of difficult passages; no published transcription or external mathematical account was used to supply words, symbols, or missing arguments. Source metadata and date are those supplied in `LM_P038_prompt.md`.

Three numbering systems are distinguished. `\scanpage` uses the scan identifiers requested in the prompt. `\mspage` records the upper author folio numbers. The lower-left handwritten numbers are retained with `\margin`, without assuming that they are in the author's hand; the printed archive footer and institutional credit outside the manuscript frame are not transcribed.

| Scan identifier | Upper manuscript folio | Lower-left handwritten number |
|---|---|---|
| 371 | 188 | 370 |
| 372 | — | 371 |
| 373 | 189 | 372 |
| 374 | — | 373 |
| 375 | 190 | 374 |
| 376 | — | 375 |
| 377 | 191 | 376 |
| 378 | — | 377 |
| 379 | 192 | 378 |
| 380 | — | 379 |

The LaTeX file is a UTF-8 fragment without a preamble or macro definitions. It uses the requested editorial macros and standard mathematical LaTeX. The recurring small surface-group glyph is rendered as lower-case `\pi`, after comparison with the clear `\pi_1` on scan 371; the Galois-group glyph is rendered as `\Gamma`. The calligraphic group letters are rendered `\mathcal G` and `\mathcal T`. Single hats, double hats, visible superscripts, and discrepancies between successive formulas have not been harmonized. Descriptions inside `\figure{[... ]}` record circles and connecting marks, rather than adding text to the manuscript.

## 2. Table of doubts

Line references are approximate visual locations, not LaTeX source lines. Each reader counted principal handwritten rows, including formula rows; formula numbers, quoted anchors, and positions are therefore the more reliable locators. **High**, **medium**, and **low** describe confidence in the reading, never confidence in the truth of a mathematical claim. Cancelled material is not treated as an assertion surviving in the active text.

| Scan | Approximate line / position | Reading in the transcription | Alternatives / unresolved feature | Confidence |
|---|---|---|---|---|
| 371 | l. 1, opening parenthesis | `définitif` | `définitifs`; ending is compressed, and a second reading sees a possible final plural stroke. | medium |
| 371 | ll. 2–3, interlinear formula | `M_{g,\nu+1\,\mathbb C}` | Retracing obscures the punctuation and possible parentheses around `\nu+1`. | low |
| 371 | l. 4, base point | `\alpha` | `a` is also graphically possible. | medium |
| 371 | l. 5 | `crans` | Final strokes are very abbreviated. | medium |
| 371 | (9), middle factor | `\widehat{\mathcal T(\pi_{g,\nu})}^{+}` | The wide hat's scope is uncertain: it may attach to `\mathcal T` alone. | medium |
| 371 | after (9), before `induisant` | deleted `en` | Short, overwritten deletion; could be another short word. | low |
| 371 | before (10) | `ss-groupe` | The doubled abbreviation stroke is uncertain; `s-groupe` possible. `fermé` sits below the line and is treated as an insertion. | medium |
| 371 | (10), parenthesis | `mais pas \widehat{\mathcal G}_{g,\nu} !` | The single hat is visible and is retained even though the surrounding inclusions may invite a different mathematical reading. | high |
| 371 | after (10), `La donnée` | deleted `de`, inserted `d'un tel` | The addition is clear; the exact deletion/attachment of the preceding `de` is less secure. | low |
| 371 | lower-left marginal NB | `comme provenant des éléments` | The note is small, diagonal, and overlaps the main display's number. | low |
| 371 | same marginal NB, before first `\widehat{\mathcal T}` | one deleted illegible item | Could be a stray or overwritten mathematical character; no completion supplied. | low |
| 372 | opening notation and (14)–(15) | deleted arguments `(\pi_0)`; new subscripts `\pi_0` | Several arguments are densely cancelled; their former contents are only partly recoverable. | low |
| 372 | left-hand side of (15) | `\widehat{\widehat{\mathcal T}}(\pi_0)` | Two hats are visible. The marginal proposed single-hat symbol and question are preserved separately. | high |
| 372 | left margin beside (15) | `\widehat{\mathcal T}` followed by `?` | The highly looped marginal letter is less secure than the main-text `\mathcal T`. The oblique linking arrow has a small head at each end. | medium |
| 372 | after (15) | `procédant` | The ending is abbreviated. | medium |
| 372 | paragraph before (16), after the isomorphism | `défini` | `définie` is also possible; grammatical agreement has not been used to decide. | low |
| 372 | (16), (17), (18), cancelled parenthesized arguments | `(\pi)` | Dense deletion obscures the original argument and any subscript. | low |
| 372 | under `N_\alpha` in (17) | vertical equality with `M_\alpha/\pi` | The two short vertical strokes are rendered `\Vert`; they appear to express an equality written vertically. | medium |
| 372 | right margin beside (17) | `\widehat{\widehat{\mathcal T}}` followed by `?` | Letter is highly looped; the main display has a single hat inside an oval. | medium |
| 372 | line before (19) | deleted `\tau_\alpha dont` | `\tau_\alpha` is relatively clear; the following short word is much less secure. | low |
| 373 | 2 | arithmétisation | Accent and compressed ending are not individually secure. | medium |
| 373 | 5, formula (20) | Isomext | The joined `ext` can resemble `cat`; semantic expansion has not been substituted. | medium |
| 373 | 6, after P(pi) | l'ens | Could be a different very compressed `en…` abbreviation; no terminal period is visible. | medium |
| 373 | 6, insertion above line | orientées | Final letters are abbreviated-looking strokes. | medium |
| 373 | 8, formula (21) | Isomext | Same joined-letter ambiguity as (20); unlike (20), no separate underline is visible. | medium |
| 373 | 13 | autom. | `auto…` abbreviation, ending compressed. | medium |
| 373 | 16, inserted rewrite | deleted word before alpha | Word is struck through and not recoverable. | low |
| 373 | 17, crossed-out line | trivi | Beginning of the last word is visible, but its ending and punctuation are not. | low |
| 373 | 18, beginning and parenthesis | ne; vu la notat. ([illegible] … | The first `ne` is disputed between readers; the lead-in could be `d'où`; an inner opening parenthesis is visible, but its shorthand and terminal delimiters are not securely readable. | low |
| 373 | 18–19 | G-hat subscript a in parenthesis, without plus | No plus is visible here, although a plus occurs in (23); retained without correction. | medium |
| 373 | Lower-left marginal note | mais. Attention | Punctuation between the words is uncertain; it could be a comma. | low |
| 373 | 22, foot of text | Ou encore / d'où encore | The initial character is retraced; `encore` is more legible than its lead-in. | low |
| 374 | 3, (25) | N_a = M_a/pi | The first relation is compressed to an extremely short mark; equality is probable. | medium |
| 374 | 9 | revient | The word is very compressed; its final stroke is secure but its internal letters are not. | medium |
| 374 | 9 | isom. | Final mark could be a short dash instead of a period. | medium |
| 374 | Left of (27) | deleted Gamma_a followed by an isomorphism/equivalence sign | A crossed-out false start; the relation is difficult to disentangle from the deletion stroke. | low |
| 374 | 11 | changé | Letters `ch…gé` discernible; middle is reduced to a line. | medium |
| 374 | 11 | autom. | Abbreviation after `par`; no article `un` has been supplied. | medium |
| 374 | 12 | d'alpha / alpha | Faint loop above alpha could be the remains of `d'`; alpha itself is clear. | low |
| 374 | 14, deleted false start | arith / ext | The tall final strokes favour a beginning `arith`; cancellation obscures the beginning. | low |
| 374 | Beneath a_(g,nu), origin pair | arithm. “canonique” | The abbreviation is contracted; the bracket attaches the annotation to a_(g,nu), not to the whole following paragraph. | medium |
| 374 | 17, deleted passage | correspondants | Ending obscured by deletion line. | medium |
| 374 | 19, deleted passage | ds / dans | Only a compact `d…s` is secure. | low |
| 374 | 18, replacement insertion | autom; ext | Terminal punctuation is not visible; no period has been added. | medium |
| 374 | 20, inserted displayed material | T-hat_(g,nu), without plus | No plus is visible; retained despite the plus in (24)–(26). | medium |
| 374 | 20, argument of pi_1 | Q / Q-bar | The field symbol is overwritten; a bar cannot be confirmed or excluded. | low |
| 374 | 20–22, parenthesis | calculé par rapport | `calculé` and especially the beginning of `rapport` are abbreviated-looking strokes. | medium |
| 374 | Bottom-left margin | injectif | Initial strokes are faint; `bijectif` is a less likely alternative. | medium |
| 375 | 2 | la = chose / barred-m shorthand | Two nearly horizontal strokes are visible; an extremely flattened m below a bar cannot be distinguished from an equals sign. Neither reading has been expanded to `même`. | low |
| 375 | 4, initial base M | Q-bar followed by an added Q | The original field symbol is retraced and a smaller Q is written above/right; the exact cancellation or replacement relation is uncertain. Both visible layers are retained under doubt. | low |
| 375 | 5 | considère | Final syllable is very compressed. | medium |
| 375 | 6, before (28) | M_(g,nu,Q), without tilde | The stroke immediately above belongs to the descending f of `famille`; no distinct tilde is visible here, although the display has a tilde. | medium |
| 375 | 9, parenthesis | donc | The word has an initial d-like stroke and a compressed ending; `aussi` is less likely. | medium |
| 375 | 14 | autom | The abbreviated ending is not fully resolved; no period has been supplied. | medium |
| 375 | 19–20, end of page | permet / pourrait; en; effet; servir | The final verbal phrase is particularly compressed. It has been marked at each doubtful word and has not been repaired to improve its syntax. | low |
| 376 | 1 | `relative` | The interior letters after the initial stroke are compressed; no secure alternative. | medium |
| 376 | 1 | `permettant` | Ending is a short continuous stroke. | medium |
| 376 | 3, 6, 13 | `lacets` | `lacet`; plural ending is not separately distinguishable in these three occurrences. | medium |
| 376 | 6 | `arithmétisés` | The final participial ending and accent are not sharply resolved. | medium |
| 376 | 8, underlined | `homomorphismes` | `isomorphismes`; the initial group of strokes is difficult, so the mathematical expectation has not been used to choose silently. | low |
| 376 | 10 | `marquée` | Compressed beginning and final ending; the descender supports the middle of the reading. | medium |
| 376 | 15 | `conjecturalement` | Several medial syllables are reduced to a continuous wave. | medium |
| 376 | 15 | `admettant` | Initial letters are overwritten; `en admettant` is a possible segmentation, but the extra word is not securely visible. | low |
| 376 | 19 | `correspondant` | Last line is close to the lower border; ending is compressed. | medium |
| 377 | 2 | `il` | Heavily retraced small word immediately before the deletion. | medium |
| 377 | 2, deletion | `donne` | `donné`; the deletion obscures the ending and any accent. | low |
| 377 | 2–3 | `de \illegible{1} canonique` | A small trace after `de` is not readable; `façon` would give a possible phrase, but has not been inserted as a confident reading. | low |
| 377 | 4, insertion above `torseur` | `\Gamma_{\mathbb Q}` | `\Gamma_0`; subscript is small and rounded. | medium |
| 377 | 5 | `\overline{\mathbb Q}\hookrightarrow\mathbb C` | `\subset`; the left hook is visible, but the right end of the horizontal stroke does not give an unequivocal arrowhead. | medium |
| 377 | 5–6 | `en corr.` | The short word preceding `corr.` is faint. | medium |
| 377 | 7 | `orientées` | Accent and final ending are weak. | medium |
| 377 | 7 | `donnant` | Final letters are a compressed terminal stroke. | medium |
| 377 | 16, deletion | `de` in `l'image de (29) est` | The small word is crossed through. | medium |
| 377 | 17 | `bijective` | Last letters are compressed at the right edge. | medium |
| 377 | Below (30) | Superscript `\rightleftarrows` on `P_a` | `\leftrightarrow`; two opposed arrowlike strokes, supported by the clearer recurrence in scan 378, but not identified with certainty. | low |
| 377 | Below (30) | `(pas orientées)` | `(non orientées)`; lower strokes partly meet the black frame. | low |
| 377 | Below (30), far right | Closing `)` after `sur a` | Visible curved terminal stroke; its opening partner and exact scope are unclear. | low |
| 378 | 1 | `provient` | Ending is a single short stroke. | medium |
| 378 | 3 | `centralisateur` | Medial letters and last syllable are compressed. | medium |
| 378 | 6 | `discrétification` | Accent and some medial letters are uncertain. No initial `pré-` is supplied: the word visibly begins directly with the `discrétification`-like sequence. | medium |
| 378 | 6 | Superscript `\rightleftarrows` on `\alpha` | `\leftrightarrow`; upper stroke appears to point right and lower stroke left. | medium |
| 378 | 10 | `\overline{\mathbb Q}_1` | `\overline{\mathbb Q}`; a short vertical stroke at the lower right could be a subscript 1 or part of the handwritten letter. | low |
| 378 | Below final paragraph, around y=1135 | Deleted `30` | Heavily crossed numeral-like mark; could be an unreadable pen trial or a different numeral. | low |
| 379 | Upper-right heading | `a)` | Initial character is a filled, dot-like mark; possibly a bullet followed by `)`. | low |
| 379 | Upper-right heading | `ss-groupes` | `s-groupes`; the compressed abbreviation is heavily retraced. | medium |
| 379 | 2 | `le` | Short loop between `par` and `contexte` is faint. | medium |
| 379 | 3, deletion | `puissent` | Verb is struck through; several middle strokes are obscured. | medium |
| 379 | 3 | `formuler` | `formulent`; final strokes do not resolve the ending, and the deletion before the word must not silently dictate its grammar. | low |
| 379 | 3 | `de` before `façon` | Very compressed connective. | medium |
| 379 | 4 | `soient` | Ending is largely a continuous stroke. | medium |
| 379 | 5 | `caractériser` | Internal letters and ending are compressed. | medium |
| 379 | 6, deletion after `N_{g,ν}` | One illegible word | Crossed out almost completely; no dependable reading. | low |
| 379 | 7 | `lacets` | Final letters in “groupe à lacets” are reduced to short strokes. | medium |
| 379 | 11 | `paramétrée` | Final letters are not independently distinct. | medium |
| 379 | Insertion above 12 | `\widetilde M_{g,\nu\overline{\mathbb Q}}` | The tilde is clear; the crowded field subscript and exact placement of its overbar are less secure. | medium |
| 380 | Above 4, within circle | `hum-` | Interlinear annotation has a clear initial tall stroke and trailing dash, but its middle letters are compressed. | low |
| 380 | 5 | `de` before `relèvements continus` | `des`; the final small stroke is not distinct. | medium |
| 380 | 8, after `Weil` | Deleted `)` | The closing parenthesis is retraced with a cancellation squiggle; the extended parenthesis closes after `simples` on line 10. | medium |
| 380 | 11, deletion | `ainsi dégagées` | The stroke crosses the beginning and middle; the intended deletion boundary across the rest of `dégagées` is uncertain. | medium |
| 380 | 11 | `devraient` | Inflectional ending is a long stroke. | medium |
| 380 | 12, deletion beneath `stables` | `invariantes` | Several letters are lost in the strike-through and the inserted replacement. | low |
| 380 | 14 | `ces` | `un`; the short word consists of a shallow curved stroke and a hook. | low |
| 380 | 14 | `germes` | `germe`; final plurality is not securely separable from the trailing stroke. | medium |
| 380 | 15 | `pourraient` | `pourrait`; the final inflection is compressed. | medium |
| 380 | 16, before `façon` | `de` | Heavily retraced word. No independent crossing stroke can be distinguished confidently, so the reading is not treated as a deletion. | low |
| 380 | 18, between `et` and `qu'il` | `\overline{\mathrm m}` | Two short strokes, the lower slightly wavy; interpreted as the supplied abbreviation for “même”, with explicit doubt. | medium |
| 380 | Insertion above 18 | `classes` in `(classes de π-conj.)` | The first word is compressed; `de π-conj.` is appreciably clearer. The bent insertion line points before `de tels`. | medium |

## 3. Abbreviations met

The expansions below are interpretive aids only. None has been substituted into the transcription. Terminal periods are retained or omitted in the fragment according to the visible reading; uncertain endings remain marked there.

| As written | Tentative expansion or meaning |
|---|---|
| `can.` | canonique / canoniquement, according to context |
| `isom.` | isomorphisme(s) / isomorphe(s), according to context |
| `iso.` | isomorphisme(s) |
| `iso` | isomorphisme; no secure terminal point in the cited occurrence |
| `isom` | isomorphisme; no secure terminal point in the cited occurrences |
| `ss-groupe`, `ss-groupes` (uncertain; `s-groupe(s)` possible) | sous-groupe(s) |
| `hom.` | homomorphisme |
| `hom` | homomorphisme; no visible terminal point in scan 379 |
| `i.e.` | id est |
| `NB` | nota bene |
| `cple` | couple |
| `mod` | modulo |
| `ens`, `ens.` | ensemble |
| `lac` (mathematical subscript) | lacets |
| `Isom` | isomorphismes; notation for the corresponding set or object |
| `Isomext` (joined letters uncertain) | isomorphismes extérieurs |
| `autom.`, `autom` | automorphismes |
| `notat.` | notation |
| `trivi` (cancelled, ending unclear) | probably the beginning of trivialement |
| `int.` | intérieur |
| `arithm.` (uncertain annotation) | arithmétisation, in the label attached to the marked origin |
| `ds` (uncertain, cancelled) | dans |
| `ext` (scan 374, no secure period) | extension |
| `ext.` (attached to a group or fundamental group) | extérieur |
| `l'ext.` (scan 380) | l'extension |
| `rev.` | revêtement(s) |
| `corr.` | correspondance |
| `π-conj.` | conjugaison par π; the phrase “classes de π-conj.” is read provisionally |
| `\overline{\mathrm m}` (uncertain in scan 380) | même |
| `=` / `\overline{\mathrm m}` (unresolved sign in scan 375) | equality-like shorthand or abbreviated même; no verbal expansion is made in the transcription |
| `Gal` | groupe de Galois, in the mathematical notation |
| `Spec` | spectre, in the mathematical notation |

## 4. Legibility and limits of confidence

The continuous prose is generally more recoverable than the dense revisions, although many word endings are reduced to short strokes. The clearest material is the main sequence of quotient constructions and the involution formulas; the least trustworthy material is the lower-left NB on scan 371, the cancelled arguments and hat corrections on scan 372, the overlapping revisions before (23) on scan 373, the interleaved cancellation and replacement at the foot of scan 374, and the field corrections and final phrase on scan 375. The opening rewrite and the addition against the lower frame on scan 377, the orientation-forgetting superscripts, and the last five lines of scan 380 also remain significantly uncertain.

Potentially misleading details have been left visible: the double-hat left term questioned in (15), the single-hat right term questioned in (17), the absent plus in some later occurrences, the provisional `\overline{\mathbb Q}_1`, and the awkward phrase containing “de servir.” The possible `ne` before “dépend pas” on scan 373 is disputed between readers and is included only as an explicitly doubtful reading. “Heuristiquement” on scan 379 is retained, and the underlined “peut être” on scan 380 has no supplied hyphen. The last page ends with “de tels”; no continuation or sentence-ending punctuation has been inferred. These uncertainty marks should remain attached to the text in any subsequent use.

## 5. Research notes — English; separate from the transcription

These are manuscript-based research prompts, not a literature survey or an assessment of present-day theorem status. All quotations and attributions refer to the supplied pages of Grothendieck (1981), with scan locators on each item. The categories distinguish his conjectures or expectations, assertions for which these pages supply no proof, implications not pursued here, and explicitly labelled ideas suggested by this reading. A withdrawn claim remains identified as withdrawn. Own ideas carry a confidence level and its reason; none is presented as established or as new. These notes have not been used to repair the transcription.

1. **Scan 371, paragraph after (9) — conjecture / expressed expectation.** Grothendieck writes “on présume injectivement” about the homomorphism into the group carrying a double hat. A proof would have to identify the kernel of this particular arithmetic action, including the base-point and inner-automorphism conventions; the displayed filtration by itself does not establish injectivity (Grothendieck, 1981, scan 371).

2. **Scan 371, (10)–(12) — unproved claim.** The assertions “est normal” and “équivaut à celle d'un” introduce passage between the groups denoted \(M_{g,\nu}\) and \(N_{g,\nu}\), and identify two quotients. A proof would need the relevant inner subgroup, its containment, the induced quotient map, and normality; these pages state the resulting relationships without supplying those checks (Grothendieck, 1981, scan 371).

3. **Scan 371, (13) and final two lines — conjecture / expressed expectation.** The surjection \(\Gamma_{\mathbb Q}\to\Gamma_{g,\nu}\) is followed by “on présume qu'il est bijectif,” and the text relates this expectation to canonical isomorphisms among the \(\Gamma_{g,\nu}\). The specific kernel and the sense in which these identifications are canonical are natural objects of further study; the expectation must not be reported here as an established identification (Grothendieck, 1981, scan 371).

4. **Scan 371, marginal NB; scan 372, (19) — unproved claim.** A “canonique” element is said to have order two; (19) explicitly includes both \(\tau_\alpha^2=1\) and \(\tau_\alpha\ne1\). One should check independence from the representatives used in the negative/positive quotient construction and separately verify nontriviality (Grothendieck, 1981, scans 371–372).

5. **Scan 372, paragraph after (15) — unproved claim.** After transport by an isomorphism \(\pi_0\simeq\pi_{g,\nu}\), the text says “le résultat n'en dépend pas.” Establishing this requires comparing two transporting isomorphisms and proving that the relevant change of marking preserves each of the subgroups being defined, with the precise positive/full-group convention used on the page (Grothendieck, 1981, scan 372).

6. **Scan 372, (16)–(19) — unpursued implication.** The passage from a pre-discretification \(\alpha\) to \(M_\alpha,N_\alpha,\Gamma_\alpha,\tau_\alpha\) suggests a compatibility problem under isomorphisms of profinite groups carrying the relevant peripheral data. It would be useful to write down the transport maps, their dependence on representatives, and their action on the distinguished involution; the present formulas alone do not give that complete functorial statement (Grothendieck, 1981, scan 372).

7. **Scan 372, questioned terms in (15) and (17) — own idea. Confidence: medium.** Make an explicit diagram of the single-hat and double-hat groups, their maps to outer automorphism groups, and the relevant quotient kernels before interpreting the arithmetic statements. The reason is palaeographic and structural: the manuscript itself circles these terms and proposes altered hats with question marks, so treating all hats as settled risks attributing a false assertion to the text. This is a proposed checking method, not a claim of novelty or a correction to the transcription (Grothendieck, 1981, scan 372).

8. **Scan 373, approximately lines 9–11, (21)–(22); kind: unproved claim.** The text says that Gamma acts “librement … sur P(pi)” and identifies A(pi) with its orbit set. A proof would need to track the normal subgroup used in (21), justify the induced action, and check that equality of orbit classes is precisely the equivalence relation used in (20) (Grothendieck, 1981, scan 373).

9. **Scan 373, approximately lines 18–21, (23); kind: unproved claim.** The asserted subgroup “dépend pas de alpha” and is said to be “le noyau de l'opération” of M_a on P_a. The heavily revised passage deserves comparison with the unrevised definitions: independence requires showing that a change of representative preserves the same subgroup, while the kernel assertion requires comparing all point stabilizers (Grothendieck, 1981, scan 373).

10. **Scan 373, lower-left margin; kind: unpursued implication.** The marginal correction explicitly warns that the starred group “dépend de alpha,” and likewise says that tau_alpha depends on alpha. This distinguishes the subgroup identified in (23) from the auxiliary starred stabilizer and the involution associated with a chosen prediscretification; later uses should retain that dependence rather than silently replacing alpha by a (Grothendieck, 1981, scan 373).

11. **Scan 374, approximately lines 6–12, (26)–(27); kind: unproved claim.** Gamma_a “s'identifie au commutant” of the right Gamma_(g,nu) action, and the choice of alpha supplies an isomorphism that is altered by an inner automorphism when alpha changes. One should check the transitivity of the M_a action, its asserted kernel, and the left/right action convention before identifying this quotient with the full commutant (Grothendieck, 1981, scan 374).

12. **Scan 374, approximately lines 13–16; kind: unproved claim.** The category is asserted to be “un groupoïde connexe” with “une origine fixée.” This requires specifying its arrows and showing that every arithmetized group under discussion is isomorphic to the stated origin in that particular category; abstract isomorphism of the underlying profinite groups alone does not state all the needed compatibility (Grothendieck, 1981, scan 374).

13. **Scan 374, interlinear replacement at the foot and bottom-left margin; kind: unproved claim.** The automorphism group is identified with N_(g,nu), described as an extension, and compared with a fundamental group of the moduli space; a marginal qualification reads provisionally “si … injectif !”. The field symbol and the qualification remain palaeographically uncertain, so the exact hypothesis and whether a plus belongs on the geometric kernel should be checked before treating the comparison as a theorem (Grothendieck, 1981, scan 374).

14. **Scan 374, canceled passage at the foot; kind: unproved claim (withdrawn in the manuscript).** The deleted text says that the profinite groups coming from discrete groups are “can. isom.” in the category. Its cancellation matters: it records a formulation tried and then discarded here, and supplies no authorization to restore a canonical identification in the active text (Grothendieck, 1981, scan 374).

15. **Scan 374, (27); kind: own idea. Confidence: high as a diagnostic, not as a claim of novelty.** Fix one element of the right torsor P_a and compute the identification of its equivariant automorphisms explicitly, then change the chosen element by right multiplication. This elementary check should make the inner-conjugacy change and any opposite-group convention visible; the reason for suggesting it is the explicit “à droite” insertion on the preceding page (Grothendieck, 1981, scan 374).

16. **Scan 375, approximately lines 1–7, (28); kind: unproved claim.** Giving an object is said to be the same thing, “à isom unique près” (the abbreviation before `chose` is uncertain), as giving a universal cover, or a torsor under N_(g,nu). A proof needs the precise category of universal covers or pro-objects and its arrows, together with the correspondence between its isomorphisms and the torsor action; the uniqueness qualification should not be inferred merely from existence of a cover (Grothendieck, 1981, scan 375).

17. **Scan 375, approximately lines 5–10, (28); kind: unproved claim.** The pulled-back family is called “la” algebraic curve whose exterior fundamental group is the specified group with loops. One would need to check the effect of pulling back to the universal cover of the moduli object, the comparison with the fundamental group of the total space invoked in the parenthesis, and preservation of the peripheral data meant by the loops (Grothendieck, 1981, scan 375).

18. **Scan 375, approximately lines 11–19; kind: unpursued implication.** Passing to groups that are “pas extérieurs” replaces the automorphism group N by M and replaces the moduli-space universal cover by one of the universal family. The page thereby suggests that remembering inner data should correspond geometrically to this change of total space; the relevant forgetful functor and its effect on the stated groupoids deserve an explicit construction (Grothendieck, 1981, scan 375).

19. **Scan 375, (28); kind: own idea. Confidence: medium, because the excerpt does not specify the full geometric category.** Compare the construction first for a finite étale cover of the moduli object, then pass to the inverse system that is intended by the universal cover. This could expose which parts of the “curve” language are literal statements about schemes and which require pro-objects, without altering the author's wording or assuming a later resolution (Grothendieck, 1981, scan 375).

20. **Scan 376, lines 1–4 — unpursued implication.** The continuation distinguishes “un vrai groupe à lacets” from “un groupe ext.” A worthwhile further question is exactly which reference covering or choice removes the inner-automorphism ambiguity, and how changing that choice acts on the resulting group with its additional structure. This would require tracing the reference object referred to as (28) and its functoriality, rather than adding a base point not written here (Grothendieck, 1981, scan 376).

21. **Scan 376, lines 5–12 — unproved claim.** The statement “On trouve encore un groupoïde connexe” is accompanied by identification of the automorphism group with \(\Gamma_{g,\nu}\). The local argument would need a precise transport-of-structure construction, an account of the allowed arithmetically exterior morphisms, and a computation of the stabilizer of the marked origin. The first word of the underlined morphism phrase is uncertain in the transcription, so its exact formulation should be settled before evaluating that claim (Grothendieck, 1981, scan 376).

22. **Scan 376, lines 12–14 — unproved claim.** The completed groups are said to be “can. isom. entre eux.” To assess the asserted canonicity, one needs to specify which arithmetization and comparison morphisms are held fixed and whether any inner-automorphism ambiguity survives. No construction of those particular canonical comparisons is supplied on this page (Grothendieck, 1981, scan 376).

23. **Scan 376, lines 14–19 — conjecture.** The qualifier read as “conjecturalement” accompanies the hypothesis that \(\Gamma_{\mathbb Q}\to\Gamma_{g,\nu}\) is an isomorphism and the proposed equivalence with the category of universal coverings of \(\operatorname{Spec}\mathbb Q\), or of algebraic closures of \(\mathbb Q\). The formal equivalence of suitable connected groupoids once their automorphism groups are identified should be distinguished from the substantive assertion that this particular displayed map is an isomorphism (Grothendieck, 1981, scan 376).

24. **Scan 377, lines 1–7 — unproved claim.** A group with arithmetization is assigned an algebraic closure, and the torsor of field isomorphisms is put in “corr. 1-1” with oriented prediscretifications giving the arithmetization. A proof needs equivariance for the inserted Galois-group action and a clear account of the identification of field isomorphisms with the indicated embeddings into \(\mathbb C\). The conditional context of the preceding page should remain explicit when this construction is evaluated (Grothendieck, 1981, scan 377).

25. **Scan 377, lines 8–14 and (29) — unproved claim.** “Tout \(\alpha\) définit un élément” is followed by the nontrivial involution conditions and by \(\tau_\alpha=\tau_{-\alpha}\). To verify this construction one would need a representative of the oriented prediscretification, independence from its allowed changes, and an explanation of why the resulting element is nonidentity. The invariance under changing the orientation is stated, but its construction is not repeated in these lines (Grothendieck, 1981, scan 377).

26. **Scan 377, lines 15–19 and (30) — unproved claim.** The opening “S'il est vrai que” makes the bijection from \(P_a/\{\pm1\}\) to the elements of order two conditional on the displayed isomorphism of Galois groups. Its proof must establish both that every such involution is obtained and that the only ambiguity in its preimage is the orientation change. The following page identifies two group-theoretic facts intended to provide these two steps (Grothendieck, 1981, scan 377).

27. **Scan 378, lines 1–4 — unproved claim.** The manuscript calls it a “fait connu” that the involutions of \(\Gamma_{\mathbb Q}\) are the conjugates of \(\tau\) and that its centralizer is \(\{1,\tau\}\). No proof is given here; a complete verification would need both the conjugacy assertion and the centralizer computation, for example through a precise analysis of the fixed fields involved. The page's designation as known should not be mistaken for a proof supplied in these scans (Grothendieck, 1981, scan 378).

28. **Scan 378, lines 5–11 — unpursued implication.** The datum of a nonoriented discrétification is said to “revient à la donnée” of a “valuation archimédienne”; the earlier word “topologie” is cancelled. The precise equivalence relation on such valuations or absolute values should be investigated, especially in comparison with the explicitly retained quotient “mod conjugaison complexe.” This terminological distinction matters for the claim that the displayed field-isomorphism datum captures exactly the proposed structure (Grothendieck, 1981, scan 378).

29. **Scans 377–378, (30) and opening of scan 378 — own idea. Confidence: high for the conditional formal calculation; reason: it reduces to an orbit–stabilizer calculation once the torsor and action conventions are fixed.** A useful verification strategy is to choose an origin in the torsor and write the proposed map as \(g\langle\tau\rangle\mapsto g\tau g^{-1}\). Conjugacy of the involutions would give surjectivity, while the assertion \(C_G(\tau)=\langle\tau\rangle\) would identify each fiber and give injectivity. This is a proposed way to organize the verification, not a claim that the manuscript has already justified every required identification (Grothendieck, 1981, scans 377–378).

30. **Scan 378, lines 1–11 — own idea. Confidence: medium; reason: the conjugacy and centralizer assertions here are formulated for the particular base field \(\mathbb Q\), whereas the torsor calculation itself is formal.** Test the construction after replacing the base field by a more general number field, keeping track separately of real and complex embeddings. Such a comparison could clarify exactly which part of the proposed interpretation by archimedean valuations uses the special base field and which part follows solely from the groupoid and torsor construction. No generalization is asserted here (Grothendieck, 1981, scan 378).

31. **Scan 379, lines 1–6 — conjecture / expectation.** Grothendieck writes “On aimerait dégager des propriétés” and asks for a formulation “purement algébrique”; the following hope appears to be that sufficiently strong conditions could characterize the groups `N_{g,ν}`. The last verb is marked uncertain in the transcription, and this is an aspiration rather than an asserted characterization. The page supplies neither a complete list of conditions nor a sufficiency argument (Grothendieck, 1981, scan 379).

32. **Scan 379, lines 7–13 — unproved claim.** The interpretation of an arithmetized group with loops is expressly qualified by “heuristiquement”: it is related to a choice of algebraic closure and, when the group is “donné extérieurement”, a family over a universal cover of the moduli space. A proof would need to make the objects and their equivalences precise and show that these data can be recovered in both directions. The uncertainty in the inserted notation for the cover should be resolved before relying on its exact base field (Grothendieck, 1981, scan 379).

33. **Scan 379, lines 14–20 and display (1) — unproved claim.** The phrase “doit revenir à se donner un moyen de relèvement” connects specializing the universal family to a single algebraic curve with lifting the surjection `N_a → Γ_a`. The page gives its kernel but no precise class of permitted lifts or proof of this correspondence; the next scan itself begins to restrict which lifts should qualify. Continuity, equivalence under changes of marking, and the field of definition are matters requiring explicit treatment (Grothendieck, 1981, scan 379).

34. **Scan 380, lines 1–4 and adjacent annotations — conjecture / question.** The opening assertion “revient à la donnée d'une courbe algébrique” identifies a lift over an open subgroup `Γ'` with a curve over the finite extension `K'` determined by that subgroup. A large marginal “?” and a circle around `l'ext.` together with a reading tentatively transcribed `hum-` register visible reservation; the page does not say exactly which aspect is in doubt. Both the asserted correspondence and this reservation should be preserved when comparing the passage with later developments (Grothendieck, 1981, scan 380).

35. **Scan 380, lines 5–10 — conjecture / expectation.** Grothendieck excludes arbitrary continuous lifts and calls for “propriétés particulières”, including properties “du genre ‘Weil’”. His underlined “peut être” qualifies the hope that even deep requirements could follow from “propriétés beaucoup plus simples”. Neither these simpler conditions nor their proposed consequences are specified or proved here (Grothendieck, 1981, scan 380).

36. **Scan 380, lines 10–13 — conjecture / expectation.** The properties “devraient” be “stables” under passage to a smaller open subgroup, with `stables` inserted over a deleted word. This is a proposed compatibility requirement, not a demonstrated characterization. An eventual definition should distinguish preservation under restriction from recovery of a property from a restricted subgroup (Grothendieck, 1981, scan 380).

37. **Scan 380, lines 14–17 — conjecture / expectation.** A further hoped-for property is the possibility to “se remonter” to the group written with a double hat over the calligraphic G, and to do so in an equally “admissible” manner. The admissibility is expressly left “en un sens à préciser”; the text gives no definition or argument that such secondary lifts exist. The uncertain singular/plural forms in the transcription do not resolve what exact collection of germs is intended (Grothendieck, 1981, scan 380).

38. **Scan 380, line 18 and insertion — conjecture / expectation.** The phrase “qu'il y aurait ‘beaucoup’” is supplemented by an insertion read as “(classes de π-conj.)”. This suggests an abundance question formulated modulo conjugation, but the sentence is incomplete at the end of the supplied scan. No quantitative meaning of “beaucoup” or conclusion from the next page is supplied here (Grothendieck, 1981, scan 380).

39. **Scan 380, lines 1–4 — own idea (confidence: medium).** Investigate whether the circled field-of-definition statement conceals a distinction between descent data and actual descent to the fixed field `K'`, or between a field of moduli and a field of definition. The reason for this suggestion is the very local question mark at `l'ext.`; the annotation itself does not establish that this was Grothendieck's intended objection. A useful first check would compare two equivalent markings with nontrivial automorphisms of the same curve (Grothendieck, 1981, scan 380).

40. **Scans 379–380, display (1) and scan 380 lines 14–18 — own idea (confidence: medium).** Pull back the automorphism-to-outer-automorphism map along a proposed lift and ask whether the resulting extension splits after restriction to a smaller open subgroup. This would separate the first lifting problem from the additional lifting problem visible on scan 380 and make the role of conjugacy explicit. The idea is a proposed organizational test, not a claim that the manuscript's undefined admissibility conditions are equivalent to splitting (Grothendieck, 1981, scans 379–380).

## 6. Primary-source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2; supplied scans 371–380 of the archive file described as “pages 1–292”]. Université de Montpellier. https://grothendieck.umontpellier.fr

Bibliographic identification follows the supplied task metadata. The source of each reading is the attached image, rather than a separately consulted edition or web transcription.
