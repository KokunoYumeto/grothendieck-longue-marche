# LM_P10 — Editorial and research notes

## 1. Scope, pagination, and limits

This is a working diplomatic transcription of the ten supplied images, not a definitive critical edition. The French text has not been translated, mathematically corrected, or completed from another transcription. The research notes below are separate from the transcription: they do not authorize replacing an uncertain reading with a mathematically expected one.

The bibliographic identification supplied with the task is Grothendieck’s *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive, cote 140-2, file described as pages 1–292. That identification has not been independently verified. Only the ten supplied images were used to read the handwriting; no OCR or published transcription was used.

| Scan / filename ending | Printed archive page | Top handwritten number | Lower-left handwritten numeral |
|---|---:|---:|---:|
| 91 / scan091 | 90 | 44 | 90 |
| 92 / scan092 | 91 | — | 91 |
| 93 / scan093 | 92 | 45 | 92 |
| 94 / scan094 | 93 | — | 93 |
| 95 / scan095 | 94 | 46 | 94 |
| 96 / scan096 | 95 | — | 95 |
| 97 / scan097 | 96 | 47 | 96 |
| 98 / scan098 | 97 | — | 97 |
| 99 / scan099 | 98 | 48 | 98 |
| 100 / scan100 | 99 | — | 99 |

The top numbers are represented by `\mspage`; the lower-left numerals by `\margin`, without assuming that the latter were added by the same hand. The printed archive identification, URL, and institutional footer are not part of the manuscript transcription. No manuscript page number has been supplied where none is visible at the top.

### Legibility and editorial limits

The main prose is appreciably easier to read than the small indices and corrections. The least reliable passages are the diagonal marginal material on scan 91, the marginal note on scan 93, the revised lower part of scan 95, the overwritten stabilizer notation on scan 96, the partly clipped bottom caption on scan 96, and the revised formulas and cancellation boundaries on scans 98–100. In those places the transcription intentionally leaves words, alphabets, indices, or correction attachments unresolved.

Repeated `\unsure{\mathcal E}` marks concern the alphabet of the curly extension-group symbol, not a claim that every occurrence is a different group. Repeated κ/k alternatives similarly preserve uncertainty between Greek κ and Latin k/K; the writing does not consistently establish case. These provisional letterforms must not be treated as independent identifications established from the surrounding mathematics.

Parentheses, grammatical fragments, and apparently surprising formulas have not been silently repaired. In particular, the sphere exceptions on scans 91 and 97, the center assertion on scan 98, the changed s/s′ indices on scan 98, and the revised inclusion wording on scan 99 require contextual study rather than editorial correction. The endpoint of the excerpt is not the endpoint of the discussion in the larger manuscript.

The supplied `.tex` file is deliberately a fragment. It uses the requested editorial macros, ordinary mathematical commands, and `tikz-cd`; their definitions and the document preamble belong to the receiving edition. Diagram ampersands use `ampersand replacement=\&` so that the diagrams can occur inside the `\diagram` argument. A temporary wrapper was used to check LaTeX syntax; its styling is not part of this delivery.

## 2. Table of doubts

Approximate manuscript lines are counted from the first body line on each scan, excluding the page numeral and printed footer; a displayed formula or diagram is counted as one body line. Marginal positions are described separately. Because the original baselines and additions are irregular, each location also gives the exact **line within that scan’s LaTeX section**, counting the initial `\scanpage` line as line 1; these are not line numbers in the complete concatenated file. Repeated identical markers on one page are grouped, and “×2” indicates two occurrences on the same LaTeX line.

Confidence describes confidence in the proposed visual reading, not confidence in the mathematical statement. “Low” means that the candidate should not be relied upon without returning to the image; “medium” means that the visible strokes favor it but leave a material ambiguity. For an illegible span, confidence is low in recovery and the word count is only an estimate. An alternative listed here is also provisional, not an emendation.

The fragment contains 149 `\unsure` occurrences and 22 `\illegible` occurrences. These counts include repetitions of the same uncertain notation and cancelled matter; they are not counts of independent textual errors.

| Scan | Approximate manuscript location [section-local TeX line] | Provisional reading / marker | Alternative or reason for doubt | Confidence |
|---|---|---|---|---|
| 91 | ~2; 5 (display) [TeX 5, 9] | `\nu` | The small upper index and the inserted enumeration ending are not fully distinct. | medium |
| 91 | ~2; diagonal lower-left margin, beside 12–18; 18 [TeX 5, 23, 29] | `\illegible{2}` | No reading offered; 2 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 91 | ~3 [TeX 6] | `l_i'` | `l_{i_\alpha}'` | low |
| 91 | ~3 [TeX 6] | `\kappa_{i_\alpha}` | `k_{i_\alpha}` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 91 | ~9 [TeX 15] | `auquel cas` | Initial letters may instead give « en quel cas »; not resolved. | low |
| 91 | ~9 [TeX 15] | `apparemment` | `proprement` | low |
| 91 | ~10 [TeX 16] | `$\simeq$` | Equality/equivalence mark and adjacent correction strokes are difficult to separate. | low |
| 91 | ~10 [TeX 16] | `$(X,\varnothing)(=X)$` | The empty-set reading, punctuation, and correction boundaries are all provisional. | low |
| 91 | ~11; diagonal lower-left margin, beside 12–18; 14 [TeX 17, 23, 25 ×2] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 91 | ~11 [TeX 17] | `au lieu` | The short phrase after the deletion is faint; no secure alternate. | low |
| 91 | ~13 (display); diagonal lower-left margin, beside 12–18 [TeX 20, 22] | `\kappa` | `k` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 91 | ~diagonal lower-left margin, beside 12–18 [TeX 22] | `donc` | Small addition in the diagonal note; no secure alternate. | low |
| 91 | ~diagonal lower-left margin, beside 12–18 [TeX 23] | `l'exclusion des cas` | The note crosses other writing; this word sequence is provisional. | low |
| 91 | ~diagonal lower-left margin, beside 12–18 [TeX 23] | `et alors` | Interference from the diagonal text; no secure alternate. | low |
| 91 | ~14 [TeX 25] | `bien un` | Unresolved phrase in the final paragraph; not completed from syntax. | low |
| 91 | ~15 [TeX 26] | `grain de sel` | Letters and parenthetical attachment are difficult to separate from marginal writing. | low |
| 91 | ~20 [TeX 31] | `E^2_{\mathrm e}` | Final letter, subscript, and exact alphabet unresolved; no secure alternate. | low |
| 92 | ~1 [TeX 3] | `un point` | Possibly « au point »; the continuation from the preceding scan remains uncertain. | low |
| 92 | ~2; 3; 4 [TeX 4, 5, 6] | `\kappa_i` | `k_i` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 92 | ~3 [TeX 5] | `au cas` | Short phrase introducing the exceptional numerical values is faint. | low |
| 92 | ~13 [TeX 16] | `\illegible{3}` | No reading offered; 3 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 92 | ~14 [TeX 17] | `si on y tient!` | The ending and punctuation are crowded at the right edge. | medium |
| 93 | ~2 [TeX 5] | `l'isotopie` | Initial strokes and the presence of l’ are unresolved; no mathematical completion is intended. | low |
| 93 | ~4 [TeX 8] | `du` | `des` | medium |
| 93 | ~5 [TeX 9] | `ms` | Possible abbreviation for mais; a final letter/stroke is uncertain. | medium |
| 93 | ~10; 13; 14 (display); lower-left margin, beside 16–19 [TeX 14, 17, 19 ×2, 23, 24] | `\kappa` | `k` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 93 | ~13 [TeX 17] | `\bar\kappa=\kappa^{-1}` | `\bar k=k^{-1}` The overbar/overwriting is itself not fully clear. | low |
| 93 | ~14 (display) [TeX 19] | `\bar\kappa` | `\bar k` Greek κ versus Latin k/K; case is also uncertain. The overbar/overwriting is itself not fully clear. | medium |
| 93 | ~14 (display) [TeX 19 ×3] | `\zeta` | `\xi` | medium |
| 93 | ~lower-left margin, beside 16–19 [TeX 23] | `Si l'on` | Opening of the diagonal marginal note is poorly separated from other strokes. | low |
| 93 | ~lower-left margin, beside 16–19 [TeX 24] | `rempl.` | Abbreviation and its ending are uncertain. | low |
| 93 | ~lower-left margin, beside 16–19; 20 [TeX 24, 29] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 93 | ~18 [TeX 27] | `non` | Partly obscured by the marginal note; retained as a candidate only. | medium |
| 94 | ~7 (inverse-functor diagram) [TeX 13 ×2] | `étales` | Final plural s is not consistently clear in the two diagram labels. | medium |
| 94 | ~9 [TeX 17] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 94 | ~10 [TeX 18] | `top.` | Crossed-out beginning after « Le »; may be a different fragment of topos. | low |
| 94 | ~11 [TeX 20] | `est celui à` | The connectedness clause may contain different words or a logical sign; no repair supplied. | low |
| 94 | ~14 [TeX 23] | `s.-s.-groupe` | `s.-groupe` | low |
| 94 | ~17 (lower diagram) [TeX 27] | `\widehat\Pi_{e,\Sigma}` | The object is overwritten; the letter, hat, and small indices are not equally secure. | low |
| 95 | ~5; 13; 14 (display); 16 (display) [TeX 8, 20, 22, 26] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 95 | ~8 [TeX 12] | `amalgamée` | The final word after « somme » is faint; no secure competing reading. | medium |
| 95 | ~9 (display) [TeX 14] | `\widehat\times_{\Sigma}` | `\wedge_{\Sigma}` | low |
| 95 | ~10; 14 (display) [TeX 17, 22] | `U` | `X` | low |
| 95 | ~12; 18 (deletion) [TeX 19, 31] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 95 | ~17 (revised passage) [TeX 28] | `\Gamma/\Sigma` | Overwritten ending of the deleted surjectivity clause. | low |
| 95 | ~19 [TeX 32] | `S` | Overwritten numerator in the orbit-set expression. | low |
| 96 | ~1 (display); 9; 10 [TeX 4, 14, 15 ×3] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 96 | ~1 (display) [TeX 4] | `\pi_1` | `\Pi_1` | low |
| 96 | ~1 (display); 3; interlinear addition; 9 [TeX 5, 8, 14] | `\Sigma_{i_0}` | `\Gamma_{i_0}` | low |
| 96 | ~3; interlinear addition [TeX 8] | `s_i` | The chosen-point subscript in the small interlinear addition is uncertain. | low |
| 96 | ~5 [TeX 10] | `un gr.` | Deleted fragment; abbreviation and deletion boundary are uncertain. | low |
| 96 | ~7 [TeX 12] | `dihédral` | `dihedral` The visible h is retained; the spelling is not normalized to diédral. | medium |
| 96 | ~9 [TeX 14] | `\Gamma` | `\Gamma_i` | low |
| 96 | ~10 [TeX 15] | `\Gamma` | A small overwritten mark beside the letter cannot be resolved. | low |
| 96 | ~13 [TeX 19] | `donné` | Final agreement ending is not distinct; not adjusted to the following noun. | low |
| 96 | ~13 [TeX 19] | `condition` | The noun is not securely read; no substitution by an expected mathematical term has been made. | low |
| 96 | ~15 [TeX 23] | `conserve` | Overwritten word, although most letterforms support this reading. | medium |
| 96 | ~17 (revision) [TeX 25] | `l'` | Deleted initial fragment before the interlinear replacement is indistinct. | low |
| 96 | ~18 (display) [TeX 27] | `e` | Small base-object index; the exact letter is not secure. | low |
| 96 | ~18 (display) [TeX 28] | `\kappa_\Gamma` | `k_\Gamma` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 96 | ~bottom margin below 18 [TeX 31, 32] | `s` | `\xi` | low |
| 96 | ~bottom margin below 18 [TeX 31] | `\pi_1(p(s))` | `\pi_1(\varphi p(\xi))` | low |
| 97 | ~2; 16; 17 [TeX 5, 24, 25] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 97 | ~3 [TeX 6] | `condition` | The noun is not securely read; no substitution by an expected mathematical term has been made. | low |
| 97 | ~5 (display); 12 [TeX 10, 19] | `\kappa_i` | `k_i` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 97 | ~5 (display); 6; 7; 8; 13; 14; 15 [TeX 10, 12, 13, 14, 20 ×2, 21, 22] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 97 | ~8 [TeX 14] | `et un` | Beginning of an unresolved clause about inner automorphisms. | low |
| 97 | ~9 [TeX 15] | `\illegible{2}` | No reading offered; 2 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 97 | ~10 [TeX 17] | `S_0` | The second entry of the pair is overwritten. | low |
| 97 | ~16 [TeX 24] | `\S` | A paragraph sign is a candidate; the mark could be a correction remnant. | low |
| 97 | ~17 [TeX 25] | `supposer` | `suppose` | low |
| 98 | ~2 [TeX 4] | `resp.` | Crossed-out fragment between « excepte » and « le cas ». | low |
| 98 | ~4 [TeX 6] | `isom.` | Abbreviation ending and full stop are faint. | medium |
| 98 | ~6 (display) [TeX 9] | `\Sigma` | `\Gamma` | low |
| 98 | ~8; 14 [TeX 12, 21] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 98 | ~11 [TeX 18] | `automs` | Possible plural abbreviation; ending/point not fully clear. | medium |
| 98 | ~13; 16 (display); 18 (display) [TeX 20, 24, 31] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 98 | ~16 (display); 18 (display); 19 (deletion) [TeX 25, 30, 33] | `\kappa_s` | `k_s` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 98 | ~16 (display); 17; 18 (display) [TeX 25, 26, 28, 30, 31] | `\zeta` | `\xi` | medium |
| 98 | ~16 (display) [TeX 26] | `\kappa_{s'}` | `k_{s'}` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 98 | ~17 [TeX 28] | `T` | `\mathbb Z` | low |
| 98 | ~18 (display) [TeX 31] | `\kappa_s` | `\kappa_{s'}` | low |
| 99 | ~1 (deletion); 8; 10 (deletion); 12; 14; 15 (display); 16; 17 (revision); 18; 20 (display) [TeX 4, 13, 16 ×2, 19, 21 ×2, 24, 27, 28, 30, 33 ×2] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 99 | ~2 (deletion) [TeX 5] | `\illegible{2}` | No reading offered; 2 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 99 | ~5 [TeX 9] | `\illegible{1}` | No reading offered; 1 word(s) is an estimate, including unreadable cancelled matter where applicable. | low |
| 99 | ~7; 13 [TeX 11, 20] | `\kappa_s` | `k_s` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 99 | ~8–9 (deleted addition) [TeX 14] | `si` | Initial letters of the small deleted annotation are uncertain. | low |
| 99 | ~10 (deletion) [TeX 16] | `i` | `i_0` | low |
| 99 | ~16 [TeX 27] | `=` | `\ne` | low |
| 99 | ~17 (revision) [TeX 28] | `\subset` | The inserted inclusion mark and its attachment to « n’est » are uncertain. | low |
| 99 | ~19 [TeX 31] | `on` | Faint first word of the sentence introducing the final displayed result. | low |
| 99 | ~19 [TeX 31] | `en` | Faint second word of the sentence introducing the final displayed result. | low |
| 99 | ~20 (display) [TeX 33] | `\equiv` | `=` | low |
| 100 | ~1; 2; 6; 8 [TeX 3, 4 ×2, 8 ×3, 10] | `\mathcal E` | Calligraphic E is provisional; an unstyled E or a ξ-like letterform cannot be excluded. | medium |
| 100 | ~2; 4 [TeX 4, 6] | `\kappa_i` | `k_i` Greek κ versus Latin k/K; case is also uncertain. | medium |
| 100 | ~5; interlinear addition [TeX 7] | `\Sigma` | `\mathcal E` | low |
| 100 | ~8 [TeX 10] | `défin.` | Abbreviated ending and punctuation before mod are not distinct. | low |
| 100 | ~11 (revision) [TeX 14] | `classes de conj.` | Crossed-out wording; only parts of the letters remain distinct. | low |
| 100 | ~13 (revision) [TeX 17] | `sous-` | Overwriting makes the status of the prefix uncertain. | low |
| 100 | ~13 (revision) [TeX 17] | `\Sigma` | `\Gamma` | low |
| 100 | ~18; 19 [TeX 25, 26] | `condition` | The noun is not securely read; no substitution by an expected mathematical term has been made. | low |


### Additional state-of-page and layout doubts

| Scan | Approximate location | Reading or editorial placement | Alternative / unresolved issue | Confidence |
|---|---|---|---|---|
| 91 | ~9–10, parenthesis about the groupoid description | The corrected pair and its surrounding parentheses are retained as doubtful text. | Exact extent of the replacement and number/attachment of closing parentheses are not secure. | low |
| 91 | Diagonal lower-left margin, beside ~12–18 | One marginal block, with readable words and gaps. | It may contain more than one note; the endpoint of the extra-datum remark and beginning of the exclusion remark are not securely separable. | low |
| 91 | ~14–18 | Main prose and the diagonal note are separated provisionally. | Some strokes cross both areas; exact cancellation and insertion boundaries remain uncertain. | low |
| 93 | ~15, before “le système” | “Si” in the baseline and “T=Z, sur” as an addition. | The status of the short opening word and precise attachment of the addition are uncertain. | low |
| 94 | ~1, under the rightmost object | The torsor gloss follows the upper diagram in the fragment. | In the image it is placed directly below the rightmost object, not as an independent new argument. | high |
| 94 | ~10–11 | The topos gloss is treated as an interlinear addition. | The beginning after “Le” and the nearby connectedness clause are heavily revised. | low |
| 94 | ~17, lower diagram | The first link is rendered as a dash. | No arrowhead is securely visible; the direction has not been inferred from the word “morphismes.” | medium |
| 95 | ~17–19, bottom revision | “U connexe” and the coset explanation are treated as the replacement/addition to the surjectivity sentence. | Exact nesting and cancellation extent are difficult to recover from overlapping ink. | low |
| 96 | ~1, 3, 8–10 | Different visible stabilizer forms are not unified. | Overwritten Γ/Σ symbols and i/i₀ subscripts may represent changes of notation. | low |
| 96 | Bottom margin below ~18 | Local-system caption with explicit gaps/alternatives. | The black frame cuts into the lowest strokes; a complete recovery is not claimed. | low |
| 97 | ~2 | The order Γ,e in the subscript is retained. | It has not been changed to match e,Γ elsewhere in the excerpt. | medium |
| 98 | ~18–19 | The second conjugation formula and the cancelled normalizer sentence are kept separately. | The right-hand s/s′ index and whether the final definition of L_s belongs wholly to the cancellation are uncertain. | low |
| 99 | ~17–18 | Deleted “autre que,” an inserted inclusion sign, and the revised stabilizer wording are retained. | The resulting syntax is awkward; the precise revision sequence has not been reconstructed. | low |
| 100 | ~10–13 | “ens. fini d’hom. extérieurs” replaces the crossed baseline; a separate crossed “groupe” is retained in (b). | The extent of the cancelled baseline and the status of “sous-” are not fully secure. | low |
| 100 | ~15–19 | No closing parenthesis has been supplied after the parenthetical description of extended Teichmüller. | A closing stroke may be absent or too faint to distinguish; punctuation is not completed from grammar. | medium |

## 3. Abbreviations encountered

Expansions are explanatory hypotheses for this list only. They are not substituted into the transcription. Entries marked “uncertain” or “deleted” must not be taken as independently secure readings of the abbreviation.

| Form as transcribed | Probable expansion or function | Qualification / occurrence |
|---|---|---|
| `ens.` | ensemble | Scans 91, 95, 100. |
| `i.e.` | id est, that is | Recurrent; kept in the original form. |
| `comp.` | composante | Scans 91, 94, 95. |
| `hom.` | homomorphisme | Recurrent. |
| `mod` | modulo | Scans 92, 100; not expanded in the text. |
| `p.ex.` | par exemple | Scan 92. |
| `rev.` | revêtement / revêtements | Scans 92, 94; number depends on the phrase. |
| `ms` | mais | Uncertain reading, scan 93. |
| `néc.` | nécessairement | Scan 93, in the clause about finiteness of Γ. |
| `s.-s.-groupe` / `s.-groupe` | sous-groupe | Competing readings of the abbreviation, scan 94. |
| `ss-groupes` | sous-groupes | Scan 100; no full stop has been added to this form. |
| `ssi.` | si et seulement si | Scan 95. |
| `gr.` | groupe | Uncertain deleted fragment, scan 96. |
| `pt` | point | In the exceptional sphere pairs, scans 91, 97. |
| `pts` | points | Scan 98, “deux pts.” |
| `autom.` | automorphisme(s) | Scans 97, 100. |
| `automs` | automorphismes | Uncertain abbreviation ending, scan 98. |
| `int` / `int.` | intérieur(s); in `int(g)`, conjugation by g | Formula notation on scan 98; prose abbreviation on scan 97. The exact conjugation convention is not specified here. |
| `ext.` | extérieur(s) | Scan 99; related unabbreviated forms elsewhere. |
| `isom.` | isomorphisme | Uncertain punctuation/ending, scan 98. |
| `Aut` | automorphismes, automorphism group | Scan 98. |
| `Aut ext` / `Autext` | automorphismes extérieurs | Scan 98; the two written spacings are not standardized to a new symbol. |
| `Ker` | kernel / noyau | Scans 97, 99, 100. |
| `Norm` | normalisateur | Scan 99. |
| `Ob` | objets | Bottom caption, scan 96; the surrounding symbols remain uncertain. |
| `conj.` | conjugaison | Uncertain deleted phrase, scan 100. |
| `défin.` | défini / défini à… | Uncertain ending before “mod conjugaison,” scan 100. |
| `resp.` | respectivement | Only a candidate for a deleted fragment, scan 98; this expansion does not establish the reading. |
| `top.` | topos | Only a candidate for a deleted beginning, scan 94. |
| `rempl.` | remplacer / remplacé | Uncertain marginal abbreviation, scan 93. |

## 4. Research notes — separate from the transcription

These notes concern only what is visible or argued in the supplied excerpt (Grothendieck, 1981, scans 91–100). “Unproved claim” means that the supporting proof is not supplied on these pages, not that the claim is false or unproved elsewhere. “Conjecture” is qualified when the source is a question, tentative recollection, or programme rather than a formal conjecture. No claim of novelty or literature coverage is made.

### R01 — Scan 91, ~1–7 — Kind: unproved claim

The presentation is described as “une relation de définition de π,” with conjugated peripheral elements and an ordered product. A proof would need to establish both generation and completeness of the single relation, with the precise choices of the peripheral representatives and their ordering. The uncertain indices in the first three lines prevent using this transcription alone as a definitive statement of those choices.

### R02 — Scan 91, ~8–13 and diagonal margin — Kind: unpursued implication

For “I=∅,” the passage replaces the visible peripheral-homomorphism data by a displayed cohomological identification involving H²(π,Z) and T. It would be useful to formulate exactly how this datum is transported by an outer automorphism and how it compares with the later χ-twisted local systems. The direction and label of the cohomological identification, and the detailed wording of the marginal instruction, should first be checked against the image.

### R03 — Scans 91, ~18–20; 97, ~10–15 — Kind: conjecture (tentative recollection, not a formal conjecture)

The words “Si je me rappelle bien” qualify the statement about not excluding the once-marked sphere on scan 91, whereas scan 97 excludes the sphere with zero or one marked point when asserting injectivity. These need not be contradictory: the two passages may be imposing different requirements on the objects and on their peripheral maps. A useful check is to separate admissibility of an object from injectivity of its lacet homomorphisms, without altering either passage.

### R04 — Scans 92, ~8–20; 93, ~1–2 — Kind: conjecture (research programme / expectation)

The proposed enlargement from homeomorphisms to more general maps “demanderait” an “étude soigneuse.” The missing work includes specifying the permitted ramification, the role of S′⊃f⁻¹(S), and the equivalence relation whose name is only provisionally read as a form of isotopie. The mention of Ladegaillerie is the manuscript’s attribution, not an independently checked description of that thesis.

### R05 — Scan 93, ~8–16 — Kind: unproved claim

The passage says that changing to “l’orientation opposée” leaves the groupoid map in place while inverting the lacet datum, and in the T=Z description replaces l_i by l_i⁻¹. A proof should make the correspondence between local orientation, the chosen T-parameter, and the peripheral maps explicit. It should also account for changes of representatives by conjugation, rather than treating the l_i as canonically chosen elements.

### R06 — Scans 93, ~17–20; 94, ~1–7 — Kind: unproved claim

The mixed groupoids are introduced “par la construction bien connue,” followed by a chain of groupoids and inverse-direction covering functors. The construction is not supplied here in enough detail to identify its objects and arrows solely from these pages. A verification should recover the stated Γ-torsor base category and check the variance of each functor, keeping the groupoids distinct from the later hatted topoi.

### R07 — Scans 94, ~12–18; 95, ~1–9 — Kind: unpursued implication

The reduction to a component and its stabilizer is followed by the warning that the “cas arithmétique” makes that reduction “inopportune.” This suggests separating equivalence of the underlying connected description from retention of the original map to the full Γ. These pages do not identify a particular arithmetic field or Galois group, so no such specialization should be read into the warning.

### R08 — Scan 95, ~7–9 — Kind: unproved claim

The text says that “(X,S,Γ) se récupère” from the component data and displays an induced-space expression whose product symbol is overwritten. A proof should explicitly construct the component copies indexed by cosets, their Γ-action, and the marked subset, and show independence of representatives. The exact notation for the construction must remain open until the overwritten symbol has been securely read.

### R09 — Scan 95, ~16–19 — Kind: unproved claim

The surjectivity discussion is revised to the phrase “U connexe,” together with Γ/Σ≃π₀(U). A verification should identify the image of the mixed fundamental group in Γ with the stabilizer of the chosen component, and then derive the asserted criterion. The deleted transitivity clause should be treated as a revision, not silently reinstated as the final statement.

### R10 — Scan 96, ~2–8 — Kind: unproved claim

The local finite faithful stabilizer is said to be “un groupe cyclique” or the following word provisionally transcribed as dihédral/dihedral. The missing justification is a classification of the relevant finite actions near a marked point, including the orientation-reversing case and the local regularity hypotheses. The insertion “est fini et” matters: the earlier allowance of a Γ that is not necessarily finite should not be replaced by a global finiteness assumption.

### R11 — Scans 96, ~11–18; 97, ~1–9 — Kind: unproved claim

The requirement that an element preserve or reverse orientation according to χ is followed by “Ceci implique” the relative local-system identification and the equivariance of κ_i. A proof should identify the conjugation action on the kernel L_i and compare it with the action of χp_i on T. It should also state exactly which changes of κ_i are absorbed by inner automorphisms, because the concluding clause on scan 97 is not fully legible.

### R12 — Scan 97, ~10–15 — Kind: unproved claim

After the displayed sphere exceptions, the text states that the peripheral maps are “injectifs” and that the mixed local groups can be viewed as “sous-groupes.” A proof should first establish injectivity of each geometric peripheral map and then show how the mixed extension maps inherit it. The statement should be checked against all standing hypotheses in the preceding manuscript, not generalized from the short list of exceptions on this page alone.

### R13 — Scan 97, ~16–20 — Kind: unpursued implication

The author calls it “particulièrement contre-indiqué” to require the point stabilizers all to equal Γ. A useful development would retain the action on the whole marked-point set, rather than replacing it by a family of Γ-fixed punctures. The parenthetical phrase about connectedness is too uncertain to support a stronger conclusion about which reductions are being assumed at this point.

### R14 — Scan 98, ~1–10 — Kind: unproved claim

The centerless-kernel discussion asserts that an extension is determined “à … unique près” by its outer action, with reconstruction as “l’image inverse” of the displayed automorphism extension. A proof needs to specify the equivalence relation on extensions, establish the kernel identification, and explain the sense in which uniqueness is asserted. The source’s cohomological or categorical hypotheses must be checked before applying this outside its intended class of groups.

### R15 — Scans 91, ~1–7; 98, ~1–3 — Kind: own idea

As a scope test for the phrase “le centre de π est réduit à 1,” specialize the earlier presentation formally to g=1 and I=∅: ⟨x,y | [x,y]=1⟩ is Z², whose center is not trivial. This is not an emendation or a claim that the manuscript is mistaken; an earlier hypothesis may exclude that specialization. **Confidence: high in the algebraic test, unresolved in its applicability**, because the omitted preceding pages may impose additional restrictions.

### R16 — Scan 98, ~4–10 — Kind: own idea

A concrete way to check the indicated pullback is to write E_ρ={(a,σ)∈Aut(π)×Σ : [a]=ρ(σ)} for the stated outer action ρ. Under the explicit assumption that π has trivial center, identify the kernel with π through inner automorphisms and then compare an arbitrary extension inducing ρ with this construction. **Confidence: high for this conditional construction**, because it is an explicit group pullback; the source’s uniqueness convention still needs to be specified.

### R17 — Scan 98, ~11–18 — Kind: unproved claim

The inserted assertion “s′ unique !” is important for recovering an actual permutation of the marked-point labels from the action on lacets. Its proof must establish the required distinction between the relevant peripheral morphism classes, with the χ-sign convention and the exceptional cases made explicit. The changed s/s′ index in the second displayed formula is not secure enough to resolve that issue editorially.

### R18 — Scans 98, ~19; 99, ~1–2 — Kind: conjecture (crossed-out question)

The cancelled sequence includes a proposed normalizer conclusion and then “donc sans doute” followed by the question whether the adjusted element belongs to the local mixed group. This is a deleted exploratory step, not an uncancelled conjecture to attribute to the final text. It is worth comparing with the normalizer reconstruction developed immediately afterwards, especially the distinction between moving a puncture and stabilizing it.

### R19 — Scan 99, ~8–20 — Kind: unproved claim

“Peut-on reconstituer” is answered by a normalizer argument culminating in the displayed identification of E_i with Norm_E(L_s). The key unsupported input on these pages is Norm_π(L_s)=L_s, together with the identification of the normalizer’s image with the point stabilizer. A proof must establish both statements for the intended class of peripheral groups and state their exceptions, rather than using them as general properties of arbitrary subgroups.

### R20 — Scan 99, ~14–20 — Kind: own idea

The final group-theoretic step can be isolated as follows: if H⊂N⊂E, p(H)=p(N), and H∩ker(p)=N∩ker(p), then H=N. For n∈N choose h∈H with p(h)=p(n); then h⁻¹n lies in the common kernel intersection and hence in H. **Confidence: high**, because this is a direct conditional argument; it does not establish the source’s separate self-normalizer and image claims.

### R21 — Scans 91, ~1–7; 98, ~1–3; 99, ~14–20 — Kind: own idea

The two-puncture sphere is a useful stress test: the formal presentation g=0, ν=2 gives l₁l₂=1, so the two peripheral subgroup images coincide with the cyclic group they generate. Thus unlabelled normalizer data alone need not distinguish the two marked points in that specialization, even though parameterized lacet maps can retain more information. **Confidence: high for the presentation calculation and moderate for its precise application to this reconstruction**, because the source explicitly singles out this exceptional case and the equivalence conventions need clarification.

### R22 — Scan 100, ~1–19 — Kind: unproved claim

The inverse reconstruction “redonne la structure à lacets,” and the subsequent data are said to be equivalent. Turning this into a theorem requires specifying objects, morphisms, conjugacy identifications, the role of the subgroup Σ⊂Γ, and the compatibility of both sign data. The overwritten choice of acting group in the conjugate formula should be resolved from the manuscript before writing the precise equivalence.

### R23 — Scan 100, ~20–22 — Kind: unpursued implication

The endpoint says that the construction defines π only as a “groupe extérieur,” with the T-lacet qualification inserted above the line. This invites a formulation that distinguishes a genuinely outer action from a chosen action by actual automorphisms, and records the dependence of any lift on choices. These pages do not supply a general strictification result, so such a result should not be inferred from the final sentence.

## 5. Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, supplied scans 91–100; printed archive pages 90–99]. Université de Montpellier.

The title, date, author attribution, and archive designation in this reference are the metadata supplied with the task. The observations and quotations above are grounded in the attached images; no independent bibliographic or literature verification is claimed.
