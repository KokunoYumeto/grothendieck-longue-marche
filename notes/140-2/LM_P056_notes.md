# LM_P056 — Transcription notes

## 1. Source, scope, and reading conventions

The accompanying LaTeX fragment transcribes the ten supplied images `LM_P056_scan551.jpg` through `LM_P056_scan560.jpg` in that order. The bibliographic identification comes from the supplied task prompt and the archive footers: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive, cote 140-2. All quotations and source-based observations below refer to these supplied images (Grothendieck, 1981); no published transcription, later manuscript pages, or secondary literature was used to fill a reading.

The scan labels required by the prompt are the filename numbers. The archive footer numbers differ from them by one. The small upper manuscript numbers are recorded separately with `\mspage`; the lower archive numbers are not substituted for them.

| Supplied scan | Visible archive footer | Upper manuscript page number |
|---|---|---|
| 551 | 550 | 281, last digit overwritten and uncertain |
| 552 | 551 | Not visible |
| 553 | 552 | 280bis / 281bis, uncertain overwritten digit |
| 554 | 553 | Not visible |
| 555 | 554 | 282 |
| 556 | 555 | Not visible |
| 557 | 556 | 283 |
| 558 | 557 | Not visible |
| 559 | 558 | 284 |
| 560 | 559 | Not visible |

This order places (33)–(37) before (31)–(32). It has been preserved. The opening and closing sentence fragments, the unclosed parenthesis on scan 553, and apparent numerical or indexing inconsistencies have not been completed or corrected. Ordinary line-end word divisions are joined where they merely divide a word across handwritten lines; paragraph and page divisions remain identifiable.

`\unsure{...}` marks a proposed reading, not an emendation; alternatives separated by `|` remain alternatives. `\illegible{n}` gives an estimated number of unreadable words, or an approximate single unit where the obscured matter is a symbol or numeral. Deletions and insertions can be nested when an above-line addition was itself cancelled. Curved insertion leaders have not automatically been treated as emphatic underlining. A headless stroke in a diagram remains headless where no arrowhead is securely visible. The heavily revised diagram (46) is described in brackets within `\diagram{...}`.

The ornamental symmetric-group letter is rendered as `\mathfrak{S}`. The group names `Sl` and `Gl` retain the apparent handwritten lowercase second letter. In the arithmetic quotient of (44), (46), (47), and (49), the symbol has two close left stems and an upper bar, with no right descending stem: it is Gamma-shaped. It is rendered `\unsure{\Gamma_{\mathbb Q}}` because its exact doubled-stroke alphabet remains uncertain; it is not silently rendered as Pi. The doubled E in the last paragraph is retained, rather than replaced with A. These typographical decisions concern the ink, not a modernization of the mathematics.

The `.tex` file is a fragment, with no preamble, document environment, or macro definitions, as requested. Its caller must define the supplied editorial macros and load the standard mathematics and `tikz-cd` support it uses. Syntax was checked in a temporary wrapper; that wrapper and its intermediate output are not part of this archive.

## 2. Table of doubts

Locations are approximate handwritten line numbers or nearby display numbers, not source-code line numbers. **High** means the reading is comparatively secure but retains a specific small doubt; **medium** means plausible letters or endings remain unresolved; **low** means significant ambiguity, overwriting, or cancellation. Confidence concerns the reading of the image, not the mathematical truth of the statement. Repeated instances of one doubt can be grouped in a row.

| Scan | Approximate line / location | Reading retained | Alternatives or unresolved detail | Confidence |
|---|---|---|---|---|
| 551 | Upper page number | `281` | Last digit is overwritten; its earlier state cannot be recovered securely. | medium |
| 551 | 2, (33), above equality | `df` | Possibly a longer abbreviation for definition; final stroke not resolved. | low |
| 551 | 5 | `invarie` | `inverse` is a possible visual reading, although the first reading fits the visible letter order better. | medium |
| 551 | 5 | `induise` | `induit`; final letter is abbreviated to a stroke. | medium |
| 551 | 6 | `sa` | Very compressed connecting word after `chacun`; retained with doubt. | medium |
| 551 | 8, after `d'ordre 2,` | Deleted `)` | Crossed curved mark, probably a cancelled closing parenthesis. | low |
| 551 | 11, before `une application` | Deleted `que` | Strike-through obscures the short word. | low |
| 551 | Final line | Full stop after `(i∈I)` | A small mark may instead be a comma; the sentence continues on the next scan. | low |
| 551 | 19, after (35) | Deleted `qui`; deleted `compatible` | Both readings are partly obscured by cancellation. | low |
| 552 | 1, opening continuation | `isomorphes` | Several medial and final strokes are compressed; no specific alternative is justified. | high |
| 552 | 2, deletion before `par des isom.` | deleted `mais` | One cancelled word remains only partly visible. | low |
| 552 | 3, immediately before `sont` | `$\overline{\mathrm m}$` | The upper heavy stroke could be a cancellation rather than the bar of the abbreviation. | low |
| 552 | 3, deletion after `sont` | deleted `pas` | `par`; initial descender and cancellation obscure the ending. | low |
| 552 | 3, blot above/before `déduits` | one illegible deleted word | The overwritten letters cannot be separated. | low |
| 552 | 4, deletion after `canoniques` | deleted `égales` | A different word ending in `-ales` cannot be ruled out. | medium |
| 552 | displayed (37), old number | illegible deleted number; replacement `37` | Earlier numeral is overwritten. | low |
| 552 | correction adjoining (37) | `la transposition (non à l'identité)` | The short line under `transposition` is emphasis; the longer line under the parenthesis is taken as an insertion leader, not additional underlining. | high |
| 552 | 9, cancelled parenthesis | `ne forment pas un` | Cross-line cancellation and interleaving with the replacement obscure the endings. | medium |
| 552 | 11, cancelled parenthesis | `syst.` | First compressed strokes could represent a longer abbreviation. | medium |
| 552 | 15, first moduli expression | first subscript `0` in `$M_{0,4}^{!}$` | The first subscript has an overwritten stroke. The exclamation mark is clearly separate. | medium |
| 552 | 15, `la clef de la ...` | `compréhension` | Medial letters and terminal stroke are compressed. | medium |
| 552 | 17, proposition heading line | `s-groupe` | `ss-groupe`; the abbreviated prefix is compressed. | medium |
| 552 | 18–19, four indices/arguments | deleted `4`, replaced by `I` | Several corrections superpose a numeral-like old stroke and a capital I; identifying the old reading as 4 is tentative. | medium |
| 552 | 20, following `est triviale` | `&` | `Si`; the two-loop sign and small separate mark are not secure. | low |
| 552 | left margin, second line | `termes` | End of the word is compressed. | medium |
| 552 | left margin, `ens.` and `card.` | periods after the abbreviations | Whether the tiny strokes are actual punctuation is uncertain. | low |
| 552 | left margin, final moduli expression | last subscript `n` | A short bar-like handwritten index, with no secure alternative. | low |
| 553 | upper manuscript page number | `280bis` | `281bis`; the final digit has been overwritten. | low |
| 553 | 1, opening deletion | deleted `de` | The first letter is overtraced. | medium |
| 553 | 1, following `des` | `s-groupes` | `ss-groupes`; compressed prefix. | medium |
| 553 | 3, before `de` | `celle` | `celles`; terminal stroke is ambiguous. | medium |
| 553 | 5, group notation after `$\Gamma'_2=$` | `Sl` | `SL`; the second letter is looped and appears lowercase, but handwriting does not settle the typographic distinction. | medium |
| 553 | 7, subgroup `$\mathfrak S_1\times\mathfrak S_3$` | first subscript `1` | Heavy retracing obscures a possible earlier subscript. | high |
| 553 | 8, open parenthesis after `élément` | `correspond.` | `correspondant`, or an abbreviated ending without a full stop. | low |
| 553 | 10, word deleted after dash | deleted `qui` | Cancellation obscures the final stroke. | medium |
| 553 | 10, following `les trois` | `suivants` | `suivant`; final plural stroke is weak. | medium |
| 553 | 11, before `aux trois éléments` | `correspondts` | `correspondants`; the expected medial syllable is not separately visible, so the abbreviation has not been expanded. | low |
| 553 | 12, before `$\ne2$` | `car.` | `car` without punctuation; the abbreviation ending is weak. | medium |
| 553 | 13, before `fixes` | `p` with raised `t` | `pt` on the baseline; a plural `s` is not securely visible. | medium |
| 553 | 14, `l'opération ... de` | `naïve` | `naive`; the word is readable, but the precise accent/dot pattern is not secure. | high |
| 553 | 18, after `gymnastique` | `schématique` | The opening and medial compressed strokes prevent a wholly secure spelling. | medium |
| 553 | 18, first parenthetical word | `indépendante` | `indépendts`; the handwritten ending may be abbreviated. | low |
| 553 | 18, following that word | `directement` | `strictement`; first letters are overtraced and compressed. | low |
| 553 | 21, cancelled word replaced by `actions de` | deleted `représentations` | Several medial letters are covered by the horizontal cancellation. | medium |
| 554 | 8, parenthetical modifier to `isomorphe` | `non can.` with raised `t` | First word could be a more compressed abbreviation; the reading `non` is tentative. | low |
| 554 | 10, `et en ... que tel` | `tt` | Full `tant` compressed to similar strokes. | medium |
| 554 | 11, verb following `$V(I)$` | `opérant` | The final strokes do not securely distinguish all letters of the ending. | medium |
| 554 | 13, immediately before crossed-out word | `de` | `d'`; the preposition may not have been adjusted when `espace` was replaced by `plan`. | low |
| 554 | 13, cancelled word under inserted `plan` | deleted `espace` | Middle strokes are hidden by the cancellation. | medium |
| 554 | 15, verb following `$\mathfrak S_I$` | `s'interprétant` | `s'interprète`; ending is overtraced. | low |
| 554 | 16, underlined abbreviation | `tte` | Precise placement of final `e` is uncertain; no expansion has been supplied. | medium |
| 554 | 17, cancelled mark between `il` and `y a` | deleted `n'` | One illegible deleted short word. | low |
| 554 | 22, deletion after `que` | deleted `les` | One illegible short word beginning with a looped ascender. | low |
| 554 | 22, last word on page | `une` | `un`; terminal stroke is weak. | medium |
| 555 | 1 | `provenant` | The middle and final letters are compressed; no secure alternative. | medium |
| 555 | 5 | `standard` | A plausible reading of the large initial and compressed middle; no secure alternative. | medium |
| 555 | 12 | `ens.` | The abbreviation is legible; its final stop may be absent. | medium |
| 555 | 13 and 23 | `autom.` | The abbreviation is legible; a final stop is not equally clear at both occurrences. | medium |
| 555 | 17, above-line insertion | `(pour i∈{0,1,∞})` | Placement before `la transposition` follows the small above-line addition; no competing substantive reading. | high |
| 555 | 23 | `ses opérations` | `ces opérations`. | medium |
| 555 | 23, after `int` | `σ₁` | `σᵢ`; the short subscript lacks a distinctive numeral foot. Display (39) itself is clearer and reads `σ₁`. | medium |
| 556 | 1, (40), both factors | `σ₁`, `σ₁⁻¹` | `σᵢ`, `σᵢ⁻¹`; short vertical subscripts. The transcription does not silently settle them by the preceding argument. | medium |
| 556 | 2 | `prop. 4` | The reference after `prop.` is not fully secure; no alternative reference can be read confidently. | low |
| 556 | 3 | `équivaut` | Compressed central and final letters. | medium |
| 556 | 5 | `schém.` | The ending and stop are abbreviated/compressed; possibly a fully written `schéma`. | medium |
| 556 | 5 | `ens` | A short, undotted abbreviation; `un` is a less likely graphic alternative. | medium |
| 556 | 6, before `sᵢ` | `\deleted{\illegible{1}}` | One overwritten symbol or short word inside the parenthesis cannot be recovered. | low |
| 556 | 6 | `mutuellement` | Possibly the abbreviated `mutuellemt`; the terminal strokes are compressed. | medium |
| 556 | 7 | deleted `transposition` | The descender and several letter shapes survive, but the strike obscures much of the word. | medium |
| 556 | 7, replacement above deletion | inserted `involution` | The replacement is above the crossed-out word; several middle letters remain compressed. | medium |
| 556 | 10 | `autom.` | Final stop uncertain. | medium |
| 556 | 12 | `s_{i₁}=0`, `s_{i₂}=∞` | `s₁=0`, `s₂=∞`; an apparent small `i` and the numerical subscript can be difficult to separate. | low |
| 556 | 13 | `s_{i₂},s_{i₃}` | `s₂,s₃`; the same compact subscript ambiguity. These are not silently replaced with indices 3 and 4. | low |
| 556 | 14, before `u défini` | `\deleted{\illegible{1}}` | One small cancelled word or symbol. | low |
| 556 | 15 | `u(z)=λ/z` | The denominator has a capital-like form: `Z` is retained as an alternative. | medium |
| 556 | 17 | prose `pour échanger s₂,s₃` | The subsequent equations visibly use `λ/s₃=s₄`, `λ/s₄=s₃`. The apparent inconsistency is retained. | high |
| 556 | 19, second triple | `(s₁,s₂,s₄)` | The second subscript could be `1`. | medium |
| 556 | 19 | `sont` | `soient`; the internal strokes and dot are not secure. | medium |
| 557 | (41), second condition | a closing `)` immediately after `n≥2` | The mark is overworked and may have been cancelled when the condition was extended; its status is uncertain. A later closing parenthesis is also visible. | low |
| 557 | after (41) | `donne` | `donnent`; the ending is a short stroke. | medium |
| 557 | after (41) | `isom.` | The stop after the abbreviation is unclear. | medium |
| 557 | (42), left of upper `π₁` | `\deleted{\illegible{1}}` | An overwritten sign, perhaps a grouping brace; no confident recovery. | low |
| 557 | (42), second condition | closing `)` immediately after `n≥2` | As in (41), cancellation of the early closing mark is uncertain. | low |
| 557 | (42), condition for `n=2` | `grain de sel` | The handwriting appears to contain this phrase after the sign for *même*, but the small letters are not fully resolved. | medium |
| 557 | left margin beside connectedness statement | `Kronecker` | Compressed name; no alternative name is supplied from historical expectations. | medium |
| 557 | same margin | `de l'équation cyclotomique` | `des équations cyclotomiques`; endings are faint and the lines slope steeply. | medium |
| 557 | (43), left internal vertical arrow | label `∼` | The curved mark also resembles `2`; it is flagged rather than silently regularized. | medium |
| 557 | (43), both middle objects | deleted `[n]` | The upper cancellation is particularly dense; the lower bracket shape is clearer. | medium |
| 557 | after (43), first prose line | `réconstruire` | `reconstruire`; a small stroke over the first part may be an accent. | medium |
| 557 | after (43), third prose line | `connait` | `connaît`; no secure circumflex is visible. | medium |
| 557 | before Proposition | `\deleted{\illegible{2}}`, followed by inserted `comme` | Approximately two cancelled words; the replacement stands above the strike. | low |
| 557 | final two lines | `\deleted{\illegible{5}}` | Approximately five crossed-out words between `suites exactes` and `d'homotopie`; not reconstructed from the argument. | low |
| 558 | Top annotation above first nontrivial object of (44) | `\widehat{\mathcal T}_{1,1}^{+}` | The script initial and its superscript are compressed; the plus is visible but the exact script letter is less secure. | medium |
| 558 | Crossed-out line immediately below (45) | `d'où [one unread word] fait que la suite` | Initial connector uncertain; the little word after it cannot be recovered safely through the strike. | low |
| 558 | Next line, “On a … compatibilité essentielle” | `la` | Dense retracing; could include a cancelled preceding word. | low |
| 558 | (46), struck formula displaced by the arithmetic Galois-group symbol | `\Gamma_n=\mathrm{Gl}(2,\mathbb Z_n)` | The cancelled left symbol and right subscript are poorly recoverable; the closing delimiter is obscured. | low |
| 559 | Annotation to the left member of (48) | `= [deleted illegible symbol] N_{1,1}'` | The preceding cancelled abbreviation/identification is overwritten rather than safely readable. | low |
| 559 | Cancelled display above (49) | `(49) \pi_1(M_{1,1}')\simeq\widehat{\mathcal T}_{1,1}^{+\,\prime}\simeq` | Number and the Teichmüller-group superscript are crossed; keep the uncertainty rather than reconstruct from the live diagram. | low |
| 559 | Annotation above geometric term in live (49) | `\widehat{\mathcal T}_{1,1}^{+\,\prime}` | The script initial and superscript plus/prime arrangement remain compressed. | medium |
| 559 | (50), quotient below left object | `\widehat\Pi_{0,3}/\{\ell_1^2,\ell_\infty^3\}` | Opening brace is retraced, and the first generator's subscript is cramped. | medium |
| 559 | (51), first exponent in quotient | `2` | A short hooked stroke; clearer in (50), but (51) is marked independently. | medium |

## 3. Abbreviations encountered

Expansions are supplied only here. Stops, accents, superscripts, and abbreviated endings are retained or marked doubtful in the transcription itself; forms separated by a slash below collect occurrences with different visible punctuation.

| Form as written | Probable expansion or function | Scans |
|---|---|---|
| `df` (uncertain, over `=`) | définition / par définition | 551 |
| `$\overline{\mathrm m}$` | même; the first occurrence on 552 is doubtful | 552, 556–557 |
| `$\overline{\mathrm m}$s` | mêmes | 553 |
| `isom.` / `isom` | isomorphisme(s) | 551–552, 555, 557, 559–560 |
| `isom can` | isomorphisme canonique | 552 |
| `syst.` | système | 552 |
| `s-groupe`, `s-groupes`, `ss-groupe` | sous-groupe(s); some prefixes doubtful | 552–553 |
| `NB` | nota bene | 552, 556 |
| `tt` | tout in `pour tt ens.`; possibly tant in `en tt que tel` | 552, 554 |
| `ens.` / `ens` | ensemble(s) | 552, 554–556 |
| `card.` | cardinal | 552 |
| `correspond.` | correspondant, tentative | 553 |
| `correspondts` | correspondants, tentative | 553 |
| `ell.` | elliptique | 553 |
| `géom` | géométrique, qualifying a curve; géométriquement in `géom connexe` | 553, 557 |
| `géom.` | géométrie | 553 |
| `car.` | caractéristique | 553 |
| `p` with raised `t` | point(s); exact ending doubtful | 553 |
| `dim` | dimension | 553–554 |
| `hom` | homomorphisme | 554, 560 |
| `can.` with raised `t` | canoniquement, tentative exact abbreviation | 554 |
| `i.e.` | id est | 554–556 |
| `autom.` | automorphisme(s) | 554–556, 560 |
| `tte` | toute | 554 |
| `int` | intérieur; notation for an inner automorphism | 555, 559 |
| `prop.` | proposition | 556 |
| `schém.` | schéma | 556 |
| `él.` | éléments | 556 |
| `Dém` | démonstration | 556 |
| `OPS` | on peut supposer | 556 |
| `mutuellemt` (possible reading) | mutuellement | 556 |
| `th.` | théorème | 557 |
| `Spec` | spectre | 557 |
| `ext.` | extérieurs | 558 |
| `surj` | surjectif / surjective | 558 |
| `det` | déterminant | 558 |
| `an` in superscript | analytique | 560 |
| `val.` | valeurs | 560 |
| `Sl`, `Gl` | Author's group-name forms, conventionally special/general linear groups | 553, 558–559 |

## 4. Legibility and limitations

The main prose and many displayed formulas are readable, but this is fast, compressed handwriting with retraced letters, tiny indices, and substantial cancellations. The least secure prose includes the beginning and diagonal margin of scan 552, the parenthetical wording after “gymnastique” on 553, abbreviated endings on 554–556, and the sloping Kronecker note on 557. Small punctuation, accents, and the distinction between the subscript `1` and `i` remain especially vulnerable.

The greatest mathematical transcription risks are the corrected `4`/`I` indices on 552, the section indices in the proof on 556, the small conditions beside (41)–(42), and the overwritten diagram labels on 558–559. Dense cancellations are left unreadable rather than reconstructed from the argument. The last paragraph of 560 contains an uncertain exponent or prime on the doubled E and heavily retraced words. Its sentence continues beyond the supplied excerpt.

Three conspicuous readings have deliberately been left unchanged: “d'indice 3” on 551; “qui fixe les trois premiers éléments” on 553; and the prose indices `s₂,s₃` beside equations using `s₃,s₄` on 556. Mathematical plausibility has not been used to replace those visible readings. The notes below discuss their implications separately.

## 5. Research notes — English

These are reading notes and proposed checks, not a literature review or claims of novelty. “Unproved claim” means a statement or step not justified in detail at the cited location; it does not assert that the entire manuscript lacks a proof. Where the supplied pages themselves return to an earlier question, that is identified. The required label “conjecture” also covers an author's explicitly recorded question or expectation, with that distinction stated. Own ideas are marked as such and include confidence and reasons. Uncertain source readings remain uncertain when quoted here.

### Scans 551–554

- **Scan 551, approximately lines 3–9, (33) — unproved claim.** The text identifies the elements attached to partitions with the “permutations paires d'ordre 2” and says that they and the identity form `V(I)`. A proof within this four-element setting would list the three unordered partitions into pairs, compute the products of their associated permutations, and check compatibility with relabelling; these checks would justify the displayed bijection without adding anything to its transcription (Grothendieck, 1981, scan 551).
- **Scan 551, approximately lines 12–20, (34)–(36) — unproved claim.** “Cette bijection étant compatible avec le transport des structures” is used to identify the induced symmetric-group isomorphism with the displayed composite. A complete verification would check the action of a permutation fixing `i` on the partition determined by `{i,j}`, then verify the stated composite on every `j` (Grothendieck, 1981, scan 551).
- **Scan 551, last two lines — own idea (high confidence; reason: the manuscript explicitly has a four-element indexing set and the stabilizers in (36)).** The phrase “d'indice 3” deserves a textual and mathematical check against the surrounding manuscript. For the ordinary symmetric group on four elements, a stabilizer of one element has index four by the orbit–stabilizer calculation; the transcription therefore preserves `3` while the notes flag the discrepancy rather than silently repairing it (Grothendieck, 1981, scan 551).

1. **Scan 552, upper third, approximately lines 5–13 — unproved claim.** The comparison maps are said to form a “syst. transitif d'isom.” after the correction replacing the identity on the two common elements by “la transposition”. A proof should track the maps through the common three-element partition set and verify the cocycle identity for three omitted indices, including the precise bijection on their common elements (Grothendieck, 1981, scan 552).

2. **Scan 552, proposition, approximately lines 17–22 — unproved claim.** The proposition states that the action of the subgroup consisting of the identity and even involutions “est triviale” on the indicated four-point moduli object, hence factors through the symmetric group of the partition set. Proving this in the indicated moduli setting requires an automorphism implementing each double transposition and a check that the construction is compatible with families, rather than only a calculation on individual geometric points. The corollary and coordinate proof on supplied scan 556 return to this statement (Grothendieck, 1981, scans 552, 556).

3. **Scan 552, corollary, final three lines — unpursued implication.** The assertion that each point-stabilizer action “est déduite de celle de” the quotient group suggests that choosing different distinguished points should lead to compatibly identified effective actions. It is useful to distinguish the canonical identification through the partition set from an identification obtained by simply matching the common labels, because the preceding correction shows those bijections need not coincide (Grothendieck, 1981, scan 552).

4. **Scan 553, final paragraph, approximately lines 17–23 — conjecture (explicit question and tentative expectation).** Grothendieck asks “comment passer d'une de ces” actions to the other and adds “On a envie de penser que ce sont les” abbreviated *mêmes*. This should be treated as a request to identify the two actions with the relevant labeling conventions, not as an already proved assertion of literal equality; the exact parenthetical characterization of the question is partly uncertain in the transcription. The explicit comparison in (38)–(40), on supplied scans 555–556, returns to this question (Grothendieck, 1981, scans 553, 555–556).

5. **Scan 553, approximately lines 7–16 — own idea.** The two indicated copies of the three-letter symmetric group could be compared explicitly on the three partitions into pairs, keeping the chosen bijections of their label sets visible throughout. **Confidence: high as a check to perform**, because the text specifies both subgroup embeddings and the finite partition set, so every action can be enumerated without importing additional moduli conventions.

6. **Scan 553, approximately line 16 — own idea.** The visible phrase “qui fixe les trois premiers éléments” deserves an independent mathematical audit against its immediate subgroup notation: pointwise fixation of three labels would be incompatible with a nontrivial three-letter symmetric group acting on those labels, whereas setwise preservation would be a different statement. **Confidence: high in the need for this audit**, because the phrase and the displayed embedding are readable; the observation does not authorize changing `fixe` or the numeral in the transcription.

7. **Scan 554, after (32), approximately lines 7–12 — unproved claim.** The map on the three partitions “est surjectif” and its kernel is described as a two-dimensional vector space over the two-element field; its action makes the original four-element set a torsor. A direct proof would enumerate the kernel permutations and check that each nonidentity element is fixed-point-free, which is the additional condition needed for simple transitivity (Grothendieck, 1981, scan 554).

8. **Scan 554, approximately lines 12–19 — unproved claim.** The text asserts that the four-element set has “1 et 1 seule structure de plan affine” over the two-element field and that every permutation is affine. A proof should specify the intrinsic affine structure, explain in what sense uniqueness is literal on the fixed underlying set, and verify that the group of translations is exactly the subgroup already defined (Grothendieck, 1981, scan 554).

9. **Scan 554, final four lines — unpursued implication.** The phrase “ce qui suggère d'interpréter” the three-element partition set as the nonzero translation vectors points to a canonical equivalence between a partition into pairs and the translation whose orbits are those pairs. This should be checked for equivariance under all permutations of the four-element set, so that the resulting interpretation also accounts for the asserted automorphism group. The explicit bijection (33) is on supplied scan 551, earlier in the supplied file order (Grothendieck, 1981, scans 551, 554).

10. **Scan 554, approximately lines 12–19 — own idea.** One way to test the affine-structure assertion is to define the ternary operation on three distinct labels by taking the fourth label, and to prescribe the value on repeated labels as suggested by the expression `x+y+z` in characteristic two. **Confidence: medium**, because the proposed construction is intrinsic and fits the four-point model, but the heap/affine identities and their compatibility with the manuscript's translation subgroup still require explicit checking.

### Scans 555–557

#### 555-R1 — Specified conjugacy of the two symmetric-group actions

**Scan/location:** 555, displays (38)–(39) and corollary, continuing into (40) on scan 556. **Kind:** unpursued implication. The phrase “via l'autom.” and the explicit permutation `1↦4, 2↦3, 3↦2` make the choice of identification of the two actions part of the statement, rather than merely an abstract identification of groups. It would be useful to track this particular relabelling when comparing subsequent basepoint choices or named inertia elements, because an unspecified identification with the same abstract symmetric group can hide that information (Grothendieck, 1981, scans 555–556).

#### 555-R2 — Removing the inner twist at the level of the comparison map

**Scan/location:** 555, corollary; 556, (40). **Kind:** own idea. With the left-action convention suggested by (40), test the modified map `ψ(x)=σ₁⁻¹·φ(x)` to see whether the comparison becomes strictly equivariant for the same labelled group. **Confidence:** high for this algebraic test, because substituting (40) cancels the two adjacent factors `σ₁⁻¹σ₁`; the handwritten `1/i` ambiguity and the precise action convention must first be settled from the manuscript (Grothendieck, 1981, scans 555–556).

#### 556-R1 — The earlier proposition and its reformulation

**Scan/location:** 556, lines approximately 2–11. **Kind:** unproved claim. Grothendieck writes “Il faut quand” followed by the sign for *même* and “démontrer la prop.”, then says that the statement “équivaut” to the four-section corollary. The corollary receives a coordinate argument on this page, but the exact earlier reference and the two directions of the claimed equivalence should be traced explicitly; the handwritten reference after `prop.` is uncertain (Grothendieck, 1981, scan 556).

#### 556-R2 — The normalization and uniqueness steps

**Scan/location:** 556, “évidemment unique” and proof beginning “OPS”, approximately lines 10–15. **Kind:** unproved claim. The proof compresses the passage to the normalized projective line into “OPS” and does not spell out the uniqueness argument. A complete verification over an arbitrary base would need to justify the local normalization and show that the locally constructed automorphisms agree on overlaps, using the effect on three disjoint sections; this is a request to supply the omitted details of the argument actually written here (Grothendieck, 1981, scan 556).

#### 556-R3 — The weakened disjointness condition

**Scan/location:** 556, final NB, approximately lines 18–21. **Kind:** unpursued implication. The observation “pas la peine que” the last two sections be mutually disjoint suggests studying the same formula on the locus where those two sections can coincide, while the two indicated triples remain disjoint. The page does not describe the resulting fixed locus or its behaviour over bases of different characteristics; the uncertain middle index of the second triple should be resolved before giving a formal moduli interpretation (Grothendieck, 1981, scan 556).

#### 556-R4 — A coordinate-free check through the projective matrix

**Scan/location:** 556, formula `u(z)=λ/z` and `λ=s₃s₄`. **Kind:** own idea. Test the construction with the matrix `[[0,ab],[1,0]]` for invertible sections `a,b`: its square is `ab` times the identity and its determinant is `−ab`, which gives a direct calculation to examine over a general base, including the allowed coincidence `a=b`. **Confidence:** high for the proposed matrix calculation, because these identities are formal; the application to the global relative curve still requires the normalization and gluing details noted above (Grothendieck, 1981, scan 556).

#### 557-R1 — Quotient presentations and the exceptional level two clause

**Scan/location:** 557, (41)–(42). **Kind:** unproved claim. “On part de” introduces the two quotient presentations, with the explicit replacement of `M₁,₁[2]` by its primed version when `n=2`. A detailed verification should identify the represented objects and their automorphisms, and explain precisely why the level two replacement is necessary before applying the fundamental-group construction; this page states those identifications without supplying that moduli argument (Grothendieck, 1981, scan 557).

#### 557-R2 — Connectedness, geometric connectedness, and the cyclotomic margin note

**Scan/location:** 557, prose between (42) and (43), with left marginal note. **Kind:** unproved claim. The manuscript uses “est connexe” while allowing “s'il n'est pas géom connexe” and links the point to cyclotomic irreducibility in the margin. To make that justification explicit, one would need to describe the geometric components of the level space, their arithmetic permutation, and the connection with the cited cyclotomic equation; the attribution and singular/plural wording of the margin remain transcription doubts (Grothendieck, 1981, scan 557).

#### 557-R3 — Recovering the extension by pullback

**Scan/location:** 557, (43) and following proposition. **Kind:** unproved claim. The phrase “par image inverse” is followed by the assertion that the unprimed fundamental group is an “extension centrale” of the primed one by `{±1}`. A complete argument should identify the upper middle group with the pullback of the lower extension along `Γₙ→Γₙ′`, and then verify the kernel and its centrality; the diagram records the structure of this argument but the verification is not written out (Grothendieck, 1981, scan 557).

#### 557-R4 — The extension class as a further invariant

**Scan/location:** 557, final proposition. **Kind:** own idea. Once the central extension is established, one could ask whether its class can be read from the finite-level pullback description, and whether restrictions to suitably specified subgroups split. **Confidence:** medium, because the page gives a concrete central extension and compatible finite quotients, but basepoint conventions, the relevant category of extensions, and any splitting behaviour have not been checked here (Grothendieck, 1981, scan 557).

### Scans 558–560

#### 558-R1 — Unpursued implication; scan 558, margin beside (45)

Grothendieck warns, “Attention ne pas confondre” the completion of `Sl(2,Z)` with `Sl(2,Z-hat)`. Together with the downward surjection in (47), this marks a distinction whose kernel and information loss deserve separate study; these pages do not describe that kernel. The precise location of the completion sign is therefore mathematically consequential as well as a transcription issue (Grothendieck, 1981, scan 558).

#### 558-R2 — Unproved claim; scan 558, introduction to (46)

The phrase “compatibilité essentielle … la commutativité” asserts compatibility of the arithmetic fundamental-group sequence with the level-n matrix-group sequence. A full verification would need the definitions of the level structures, transition maps, and determinant character, with the chosen identifications tracked; the diagram itself does not provide those checks. The statement may depend on arguments on earlier pages (Grothendieck, 1981, scan 558).

#### 558-R3 — Own idea; scan 558, determinant and cyclotomic-character square in (46)

One possible proof route is to formulate the level-n monodromy on torsion and use a pairing to relate its determinant to the displayed cyclotomic character. **Confidence: medium**: the labels `det` and “caractère cyclotomique” motivate this route, but the exact pairing conventions and the manuscript's definition of the moduli objects must be checked before this becomes an argument. This idea is not used to repair any symbol in the transcription (Grothendieck, 1981, scan 558).

#### 558-R4 — Unproved claim; scan 558, (47) and following line

“Passant à la limite sur n” produces (47), and he explicitly adds “diagramme sur lequel nous allons revenir.” The passage invites verification that the finite-level maps are compatible and that the inverse-limit sequence has the asserted exactness and surjectivity. That later return is outside the present set of pages (Grothendieck, 1981, scan 558).

#### 559-R1 — Unproved claim; scan 559, (48)–(49)

Grothendieck says that one obtains the extension isomorphism “de façon entièrement conceptuelle.” A proof written out from these pages would have to verify that the moduli identification and the inner automorphism `int(σ₁)` used in (48) induce the particular comparison of geometric kernels and arithmetic quotients in (49). The reference to the preceding section should be checked before treating the abbreviated argument as a gap in the manuscript as a whole (Grothendieck, 1981, scan 559).

#### 559-R2 — Unpursued implication; scan 559, (50)–(51)

The completed isomorphism “est associé à un isom” of discrete groups in (51), where two displayed relations are imposed. This suggests studying which choices of generators and orientation determine that discrete isomorphism and how much of it remains detectable after completion. The next scan explicitly asks for its formula, so the present note concerns the relation between the two levels rather than claiming the question is overlooked (Grothendieck, 1981, scan 559).

#### 560-R1 — Conjecture (author's request for an explicit construction); scan 560, approximately lines 4–9

“Il faudrait quand même expliciter l'hom (51)” identifies an unfinished task: compute formulas for a homomorphism so far defined conceptually. He explicitly states that it is defined only “modulo autom. intérieurs, a priori,” so any concrete answer must declare the choices that resolve that ambiguity. This is a request and expectation, not a conjectural truth statement in the usual sense (Grothendieck, 1981, scan 560).

#### 560-R2 — Conjecture (author's expectation about difficulty); scan 560, approximately lines 12–14

The computation is called “un calcul-clef,” with the insertion “sûrement instructif,” and he expects that it “ne devrait pas présenter de difficulté particulière.” This is his stated assessment; no calculation on this page establishes its feasibility or resolves the inner-automorphism ambiguity. It is worth checking where, if anywhere, he later carries it out (Grothendieck, 1981, scan 560).

#### 560-R3 — Own idea; scan 560, requested formula for (51)

A candidate computation could choose explicit order-two and order-three matrices modulo the central signs, then compare their geometric monodromies with the two generators in (51). **Confidence: medium**: the exponents visible in the quotient suggest this construction, but the exact loops, multiplication order, and action convention are not fixed on these pages. A bare abstract presentation is insufficient to identify Grothendieck's geometrically defined map (Grothendieck, 1981, scan 560).

#### 560-R4 — Unproved claim; scan 560, final paragraph

The author recalls “après avoir affirmé qu'il est” followed by the displayed affine-line-like identification, and “qu'il y a deux sections marquées.” The precise definition of the “schéma modulaire ‘grossier’” and its base must be recovered from earlier pages before one can justify this assertion, including its integral formulation. The exponent on the E is itself marked uncertain in the transcription and should not be used as secure evidence for a particular modern notation (Grothendieck, 1981, scan 560).

#### 560-R5 — Own idea; scan 560, final paragraph on the two marked sections

Check the behavior of those two sections in the fibers of characteristics 2 and 3, and distinguish the coarse moduli statement from stabilizer information carried by the preceding multiplicities. **Confidence: medium**: the integral base and the two special sections make these fibers a natural test, but the page ends mid-sentence and provides neither their coordinates nor a claim that they remain distinct in every fiber. This is a proposed check, not an asserted defect or a novelty claim (Grothendieck, 1981, scan 560).

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, supplied scans 551–560; archive cote 140-2, “pages 1–292” file, as identified in the task prompt]. Université de Montpellier archive.

The year, work title, and archive cote are taken from the supplied prompt; the institution is also printed in the supplied archive footers. No claim about subsequent publication, later treatment, or priority is made in these notes.
