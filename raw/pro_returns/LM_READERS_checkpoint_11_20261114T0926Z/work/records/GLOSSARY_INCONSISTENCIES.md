# Glossary inconsistencies and retained variation

## Sources and scope

This audit uses `en/glossary/GLOSSARY_LM.csv`, `en/glossary/entries_LM.txt`, `en/glossary/terms_LM.txt`, the French and English package texts, and the supplied translation checks and waivers. Source locations below give the archive cote and scan; they do not give a reader PDF page, because pagination differs by form.

The attached `entries_LM.txt` has **116 entries**. The attached `terms_LM.txt` has **117 entries**: it additionally supplies **automorphisme à lacets**, including homomorphism and isomorphism, as a term to translate by **loop automorphism**, **loop homomorphism**, and **loop isomorphism**. Earlier narrative records describe this as an addition to both tables, but the attached French matching table does not contain it. This audit includes the extra term from the supplied prompt/check table. The source tables are retained as received.

The complete concordance covers **116 packages, 1,588 aligned scan blocks, and 10,800 paragraph–term pairs**. Every corresponding scan has the same number of nonempty paragraphs after comments are removed; no scan-level fallback was needed. The audit includes both running text and the words extracted from simple mathematical text boxes. The supplied checks separately report **245 of 245 translation units passing**, with their recorded fixes and waivers (`en/checks/CHECKS.json`, `FIXES.jsonl`, `WAIVERS.jsonl`). Their PASS result is evidence of the earlier checks, not evidence that each possible synonym is editorially interchangeable.

`GLOSSARY_CONCORDANCE.tsv` gives every detected paragraph–term pair, its French wording, English candidates and both contexts. `data/glossary_concordance.json` gives counts and source references. `scripts/glossary_audit.py` regenerates both from the attached packages. The concordance matches the supplied regular expressions with longest-match suppression in French. It is a retrieval aid, not a word-alignment oracle: an English word in the same paragraph can translate a different French word. In particular, co-occurrence of “center” and “centralizer” does not show that *centre* has been translated “centralizer.” Adjacent deletion/insertion contents can also merge when markup is removed; such extracted strings are not silently corrected.

The tables below distinguish genuine lexical alternatives from inflection, the different French terms grouped in one glossary entry, and wording required by the boundaries of the manuscript’s marks. The inventory covers all supplied glossary terms; it is not a claim to have constructed a new bilingual dictionary of every ordinary word in the manuscript.

## Recorded unmarked correction

| Source ID | Place | English source | English edition | Reason |
|---|---|---|---|---|
| EN-GLOSS-140-2-296-001 | 140-2, scan 296; `en/packages/LM_P030_en.tex`, line 96 | structure with loops | loop structure | The French has the unmarked abbreviation “str. à lacets.” The supplied glossary prescribes “loop structure.” This isolated alternative is outside all doubt, deletion and insertion marks. |

The exact replacement and its occurrence assertion are in `data/glossary_edits.json`. It is an English translation correction, not a new French reading; no French manuscript variant is fabricated for it. The English master and both English forms must apply the same recorded replacement. No notation, uncertainty alternative or annotation boundary is changed by this edit.

## Confirmed alternative renderings, with dispositions

| French term or family | English renderings occurring in the supplied translation | Source examples | Disposition and reason |
|---|---|---|---|
| groupe à lacets | group with loops; group of loops; group-with-loops in a compound | 140-2:284; 140-4:180 | Keep the two alternatives in `\unsure{group with loops\|group of loops}`: they correspond to “groupe à lacets\|groupe lacets.” Keep the adjectival compound “group-with-loops structures.” No “loop group” is substituted. |
| structure à lacets / str. à lacets | loop structure; structure with loops | 140-2:296 | Correct the single unmarked “structure with loops” as above; the underlying French abbreviation is unchanged. |
| relation / équation / formule des lacets | loop relation; loop equation; loop formula; equation of the loops | 140-3:289 | The first three follow three distinct French nouns. At scan 289 the text has separate doubts on “des” and “lacets”: “equation `\unsure{of the}` `\unsure{loops}`” preserves their scope. Retain it. |
| lacet | loop; shoelace | 140-2:436 | “Lacets de souliers” occurs in a figurative phrase and is correctly “shoelaces.” The supplied waiver explicitly records this ordinary sense. |
| automorphisme / homomorphisme à lacets | loop automorphism / homomorphism; automorphism / homomorphism with loops | 140-2:305, 306, 319, 345, 364 | The “with loops” exceptions preserve an insertion containing only “à lacets.” Moving “loop” before the noun would move words outside that insertion. These are the five supplied glossary waivers. |
| homomorphisme extérieur, with isomorphism/automorphism variants | outer homomorphism; homomorphism that is outer; homomorphisms that are outer; outer L-automorphism | 140-2:90; 140-3:47; 140-4:187–188 | Postposed forms keep a doubt or underline on the noun intact. The L-prefix is manuscript terminology. At 140-2:512, “outer” is deleted and “of extensions” inserted; preserve those two acts instead of manufacturing a smooth diplomatic phrase. |
| extérieurement | by outer automorphisms; as outer actions; up to inner automorphisms; up to conjugacy; as an outer group | 140-2:110, 379, 416; 140-3:76, 133, 170, 229–242 | Retain contextual phrasing. Commuting in the outer automorphism group can be expressed as commuting up to inner automorphisms; the object being described determines whether an action, an automorphism or an outer group is named. No reading is newly decided. |
| extérieur / extérieurement, in a marked alternative | outer; outer with superscript “ly” | 140-2:191 | Retain the supplied doubtful alternative `\unsure{outer\|outer\textsuperscript{ly}}`. This is an exceptional departure from the glossary’s instruction against “outerly,” corresponding to `extérieur\|extérieurem` with a raised ending in French. Normalizing it would rewrite a marked alternative; it is explicitly disclosed here. |
| prédiscrétification | prediscretification; pre-discretification | 140-2:489 | The hyphenated form is `\inserted{pre-}discretification`; the prefix itself is an insertion. Retain that boundary and hyphen. Ordinary unmarked instances use “prediscretification.” |
| bouchage / boucher | plugging; plug; plugged; pluggings; Boucher | 140-1 and later cotes; see concordance | Verb and noun inflection is normal. “R. Boucher” is a signature on a reused sheet, already identified in the glossary; it is a proper name, not an inconsistent translation of plugging. |
| forage / forer | drilling; drill; drillings | See concordance under “forage de trous” | Retain ordinary noun/verb and number distinctions. |
| enveloppe schématique / adhérence schématique | schematic envelope; schematic closure | See concordance under this entry | These translate two distinct French expressions that the source glossary groups in one row. Do not collapse them. |
| module d’orientation(s) | orientation module; module of orientations | 140-4:188 | Keep “module of orientations,” corresponding to the manuscript’s plural “d’orientations.” The grammatical variant expresses the same object and is not a misspelling or mistranslation. |
| structure d’extension | extension structure; structure of extension | 140-3:580 | The source has `\inserted{On a une structure}` followed by “d’extension.” English `\inserted{We have a structure}` followed by “of extension” preserves the insertion boundary. Retain. |
| sous-groupe | subgroup; sub-group with marked prefix or noun | 140-2:100; 140-3:605; 140-4:16, 101 | The hyphen arises from `\inserted{sub-}group`, or from “sub-” preceding deleted “groups” and inserted “Z”-modules. It records word formation and manuscript revision; it is not an unmarked spelling inconsistency. |
| sous-groupe ouvert / fermé / invariant | open / closed / invariant subgroup; subgroup followed by a marked adjective | 140-2:87, 323, 371, 521; 140-4:24 | Retain postposed adjectives when their mark boundaries require this. The attached waivers document several of these cases. |
| suite exacte | exact sequence; exact cohomology sequence; sequences that are exact; sequences followed by deleted “exact” | 140-2:125, 129, 559; 140-4:104 | Mathematical modifiers and split annotation scope account for these alternatives. At 140-4:128, the extracted phrase “exact exact” includes the manuscript’s deletion/insertion history; it is not an independently duplicated English word. |
| commutant | commutant; commuting; commute / commutes | 140-2:374, 485; 140-4:111 | The noun naming a centralizer is “commutant”; the present participle is “commuting.” This distinction is explicitly accepted in the original check refinement. Do not convert the participle to the noun. |
| conjugaison / conj. | conjugation; conjugacy in class compounds; conjecture when “conj.” abbreviates that word | See concordance and the source term-table comments | Ordinary syntax and the two possible expansions of the abbreviation explain the variation. “Conjugacy class” remains the established term for “classe de conjugaison.” |
| produit semi-direct | semidirect product; “semi-” deleted before “direct product” | 140-3:409 | The second is `\deleted{semi-}direct product`; it records the author’s change to a direct product. The deletion is not normalized into an unmarked “semidirect.” |
| opérer / opération | operate / operation; act / acting in one marked diagram label | 140-1:19 | The source diagram has `\unsure{opèrent\|opérant}`; English has `\unsure{act\|acting}`. This localized glossary departure remains marked and is disclosed. Ordinary unmarked “opérer” is kept as “operate”; “agir” remains “act.” |
| schéma en groupes | group scheme; schemes in Groups; scheme in groups; scheme of groups | 140-4:17, 51, 150 | Scan 17 distinguishes the manuscript’s capitalized “Groupes.” Scan 51 inserts “en groupes” after “schéma”; scan 150 has nested deletion/insertion of “groupes” and “Z-modules.” Preserve capitalization and annotation scope. |
| relèvement | lifting; lift in a marked abbreviation; lift / lifts / lifted when verbal | 140-3:78; see concordance | Verb forms are grammatical differences. At scan 78 the noun is the retained doubtful “lift” with a raised abbreviation ending. No uncertain expansion is silently rewritten. |
| revêtement | covering; cover- at a scan break | 140-4:137–138 | The truncated stem continues across the source scan break. It is not an alternative technical term “cover.” |
| genre / bord / carte / champ / chemin | genus or kind; boundary or edge; map (contextually card/chart); stack or field; path or “way” in idioms | See ordinary-sense entries and 140-2:560 | The glossary itself allows ordinary senses. “En chemin” and “chemin faisant” are idioms, not paths in a space. Only attested forms in the inventory/concordance count as occurrences; allowed forms in the table are not assertions that every one occurs. |
| hom, isom, autom | morphism or homomorphism; isomorphism; automorphism; endomorphism | `en/checks/FAITHFULNESS_REVIEW_PILOT_20261112.md`; concordance | “Hom” between spaces, schemes, topoi or sheaves of sets is a morphism; a group homomorphism remains a homomorphism. The category, not uniform English spelling, decides the expansion. |
| m-bar shorthand (même) | same; even; itself; likewise; and likewise | Supplied check inventory; 140-3:454–458, 497–501 | These are contextually distinct grammatical uses of “même.” The attached unit checks count 476 standalone shorthand formulas; their pattern is narrower than the earlier glossary’s count of 479 written occurrences. Neither count licenses replacing m-bar inside a larger formula. |
| tt / tte / ts / tjrs | every; all; any; each; whole; always | Concordance | These are ordinary contextual expansions of French abbreviations, not changes to the manuscript. French forms retain the abbreviations. |
| i.e. / cf. / resp. | i.e.; that is; cf.; resp.; respectively | Concordance | Retain grammatical expansions of the source abbreviations. No mathematical assertion is changed. |

The two disclosed departures inside doubtful readings are retained rather than being presented as newly deciphered text. They remain reachable through their scan links. The report does not declare the English terminology universally normalized at the cost of those marks.

## Notation and orthography that must not be standardized

The supplied glossary and typesetting discussion lists proposed future normalization of Sl/Gl, doubled Gamma, arrows, operator names, equation-number forms, and script capitals/exponents. Those proposals are **not applied** here. The task requires the manuscript notation, and uncertain alternatives such as natural/sharp remain unchanged. A matching English operator name inside mathematical notation is not treated as an untranslated prose word. For example, `Centre` inside a formula remains the source’s notation; it is not changed to `Center` by a prose spelling check.

No unmarked “loop group,” “outerly,” “no doubt,” “doubtless,” or “without doubt” was substituted for the glossary’s chosen technical or epistemic wording. The source’s one marked superscript “outerly” exception is stated above. “Sans doute” is observed as “probably”; “sauf erreur” as “unless I am mistaken.” The ordinary prose spellings “center,” “fiber” and “neighborhood” remain American English. Occurrences of their French forms in source comments or mathematical labels are not counted as English prose inconsistencies.

## Complete supplied-term inventory

The following inventory contains every one of the 117 supplied term decisions. Counts are detected French occurrences after longest-match suppression, not a claim to count every abbreviated manuscript spelling. “Candidate forms” are literal English regex matches in the aligned paragraphs, with duplicate inflection retained for audit. Full source references and contexts are in the concordance. Spurious concatenations caused by removing deletion/insertion markup are excluded from this display but retained in the machine-readable evidence. The broad abbreviation entry has many grammatical expansions; all are recorded in the JSON and TSV.

| French glossary entry | Detected French occurrences | Observed English candidate forms |
|---|---:|---|
| groupe à lacets | 120 | group with loops; groups with loops; group of loops |
| structure à lacets | 59 | loop structure; loop structures; structure with loops (corrected) |
| relation des lacets | 55 | loop relation; loop equation; loop formula; equation of the loops |
| lacet | 113 | loops; loop; shoelaces (ordinary sense) |
| sous-groupe à lacets | 10 | loop subgroups; loop subgroup |
| action extérieure | 136 | outer action; outer operation; outer actions; outer operations; outer faithful action; outer admissible action |
| groupe extérieur | 41 | outer group; outer groups; outer profinite group |
| homomorphisme extérieur | 117 | outer automorphisms; outer automorphism; outer homomorphism; outer homomorphisms; outer loop automorphisms; outer isomorphism; outer isomorphisms; outer loop automorphism; outer outer homomorphism |
| extérieurement | 34 | by outer automorphisms; as outer actions; up to inner automorphisms; up to conjugacy; as an outer group |
| arithmétiquement extérieur | 9 | arithmetically outer |
| anabélien | 93 | anabelian; anabelianity |
| discrétification | 68 | discretification; discretifications |
| prédiscrétification | 46 | prediscretifications; prediscretification; pre-discretification |
| quasi-discrétification | 10 | quasi-discretification; quasi-discretifications |
| arithmétisation | 52 | arithmetization; arithmetizations; arithmetized; arithmetizability |
| rigidification | 28 | rigidification; rigidifications; rigidified; rigidifying |
| bouchage de trous | 52 | plugging; plug; boucher; plugged; pluggings |
| forage de trous | 18 | drilling; drill; drillings |
| trou | 46 | holes; hole |
| topos multigaloisien | 53 | multi-galois |
| multiplicité modulaire | 13 | modular multiplicities; modular multiplicity |
| multiplicité | 22 | multiplicity; multiplicities |
| topos modulaire | 9 | modular topos; modular teichmüller topos; modular multiplicity or topos |
| groupe de Teichmüller | 49 | teichmüller group; teichmüller groups; teichmüller subgroup; teichmüller subgroups; subgroups of Teichmüller (regex prefix) |
| tour, groupoïde de Teichmüller | 8 | teichmüller space; teichmüller spaces; teichmüller tower |
| Galois-Teichmüller | 6 | Galois-Teichmüller (regex matches the prefix) |
| groupe cartographique | 12 | cartographic |
| carte | 21 | map; maps |
| drapeau | 3 | flags; flag |
| germe | 139 | germ; germs |
| tour de Fermat | 21 | tower; towers |
| approximation de Lie | 9 | lie approximations; lie approximation |
| enveloppe schématique | 14 | schematic closure; schematic envelope; schematic envelopes; schematic closures |
| épinglage | 26 | pinning; pinnings; pin |
| L-groupe, L-structure | 17 | l-group; l-structure; l-groups; l-structures; lt-group |
| Gr-catégorie, Gr-champ | 5 | gr-category; gr-categories; gr-stack |
| multiplicateur | 49 | multiplier; multipliers |
| relèvement admissible | 36 | admissible; admissibility; admissibly |
| relèvement | 142 | lifting; liftings; lift; lifted; lifts |
| section | 464 | section; sections; quasi-section |
| scindage | 240 | splittings; splitting; split; splits; splittable |
| unipotent régulier | 33 | regular; regularity |
| anti-involution | 33 | anti-involution; anti-involutions |
| antipodisme | 9 | antipodism |
| condition liminaire | 9 | preliminary condition |
| module d'orientation | 15 | orientation module; orientation modules; module of orientation |
| structure d'extension | 38 | extension structure; extension structures; structure of extension |
| isotopique | 47 | isotopic; isotopy; isotopically; isotopies |
| topossique | 7 | topossic |
| proétale | 7 | pro-étale |
| congruentiel | 13 | congruential |
| cyclotomique | 8 | cyclotomic |
| générateurs involutifs | 11 | involutive |
| sous-groupe | 638 | subgroup; subgroups |
| sous-groupe invariant | 34 | invariant subgroup; invariant subgroups; invariant closed subgroup; invariant commutator subgroup; invariant ◇ -subgroup; invariant\|inscribed subgroups |
| sous-groupe distingué | 23 | normal subgroup; normal subgroups |
| sous-groupe ouvert, d'indice fini | 114 | open subgroup; closed subgroup; open subgroups; subgroup of finite index; subgroups of finite index; closed subgroups; closed characteristic subgroup; open image subgroup |
| groupe profini | 145 | profinite |
| compactifié profini, complété profini | 7 | completion; compactification; completions |
| groupe fondamental, groupoïde fondamental | 71 | fundamental group; fundamental groups |
| extension | 471 | extension; extensions |
| suite exacte | 219 | exact sequence; exact sequences; exact exact sequence |
| image inverse | 156 | inverse image; inverse images |
| noyau | 176 | kernel; kernels |
| commutant | 62 | commuting; commutant; commute; commutes; commutation |
| centralisateur, normalisateur, stabilisateur | 139 | normalizer; stabilizer; centralizer; stabilizers; centralizers; normalizers |
| centre | 89 | center; central; centers |
| conjugaison | 151 | conjugacy; conjugation; conjugate; conjecture; conjugating; conjugates; conjectural; conjecturally |
| classe de conjugaison | 56 | conjugacy class; conjugacy classes |
| conjugué | 161 | conjugate; conjugates; conjugation; conjugating |
| produit semi-direct | 23 | semidirect; semi-direct |
| somme amalgamée | 12 | amalgamated sum |
| opérer, opération | 571 | operates; operation; operating; operations; operate; operators; operated |
| action | 321 | action; actions |
| action effective | 18 | actual action; actual actions |
| fidèle, fidèlement | 125 | faithful; faithfully; faithfulness |
| librement, transitif | 48 | transitive; freely; transitively |
| torseur | 220 | torsor; torsors |
| tordu, tordre | 22 | twisted; twist; twisting |
| schéma en groupes | 99 | group scheme; group schemes; group subschemes; scheme in groups; scheme of groups; schemes in groups |
| groupe de Galois | 21 | galois group; galois groups; galois-poincaré group |
| caractère cyclotomique | 17 | cyclotomic character |
| revêtement | 267 | covering; coverings; cover |
| point base | 27 | base point; base; base points |
| points à l'infini | 10 | points at infinity; point at infinity; infinity |
| voisinage | 38 | neighborhood; neighborhoods |
| surface, genre, bord | 169 | surface; surfaces; type; genus; boundary; kind; boundaries; bounded; types |
| orientation | 203 | oriented; orientation; orientable; orientations |
| courbe elliptique, courbe algébrique | 130 | curves; curve |
| rigidification de Jacobi d'échelon n | 12 | level |
| classe de chemins | 36 | paths; path |
| homéomorphisme | 54 | homeomorphism; homeomorphic; homeomorphisms; homeomorphically |
| topos | 132 | topos; topoi |
| topos classifiant, topos étale | 30 | discrete topos; induced topos; classifying topos; étale topoi; étale topos; classifying topoi |
| morphisme de topos | 19 | morphisms of topoi; morphism of multi-galois topoi; morphism of topoi; morphisms of multi-galois topoi; morphism of galois topoi; morphism of multi-galois\|multi-galois topoi; morphisms of étale topoi |
| foncteur fibre | 13 | fiber functor; fiber functors |
| catégorie fibrée, champ, gerbe | 35 | gerbe; fibered; stack; field; gerbes |
| équivalence de catégories | 28 | equivalence of categories; equivalences of categories |
| pleinement fidèle | 16 | fully faithful; full faithfulness |
| transport de structure | 15 | transport of structure; transport of structures |
| passage au quotient | 55 | passage to the quotient; passes to the quotient; passing to the quotient; passage to the additive quotient; passage to the coarse quotient |
| bordélique | 19 | messy |
| draconien | 13 | draconian |
| dévissage | 7 | dévissage |
| yoga | 6 | yoga |
| sauf erreur | 37 | unless i am mistaken |
| sans doute | 40 | probably |
| cqfd | 22 | q.e.d |
| N.B., Rmq | 396 | n.b.; remark; number; numbers; remarks |
| hom, isom, autom | 1667 | homomorphism; isomorphism; automorphisms; automorphism; homomorphisms; morphism; isomorphisms; isomorphic; morphisms; endomorphism; morphic |
| ssi | 63 | iff |
| tt, tte, ts, tjrs | 229 | every; always; all; any; each; everywhere; whole; everything |
| pt, élt, mb | 297 | point; points; elements; element; sides; side |
| néc., gén., loc., can., alg., géom., top. | 1530 | necessarily, general(ly), local(ly), canonical(ly), algebraic(ally), geometric(ally), topological(ly), arithmetic(ally), set, category, hypothesis, definition, proof, proposition, corollary, example, dimension, commutative(ly), universal, essential(ly), equivalent, inverse, invariant, inner, outer, extension, and contextual expansions (all forms in concordance) |
| m̄ (même) | 0 | same; even; itself; likewise (supplied check inventory, 476 standalone formulas) |
| i.e., cf., resp. | 1601 | i.e.; cf.; resp.; that is; respectively |
| automorphisme à lacets | 20 | loop automorphisms; loop automorphism; automorphism/homomorphism with loops (marked scope) |


## Audit outputs and reproduction

- `scripts/glossary_audit.py`: parses the source tables, aligns the 1,588 scan blocks and their paragraphs, and writes the full concordance and summary.
- `scripts/write_glossary_report.py`: writes this report from the reviewed decisions and concordance.
- `data/glossary_edits.json`: one exact English replacement with source ID, source line, old and new text, reason, evidence and expected match count.
- `GLOSSARY_CONCORDANCE.tsv`: 10,800 paragraph–term records with paired contexts and relative source locations.
- `data/glossary_concordance.json`: all 117 entries, counts and references.

Run the two scripts in that order after making the three source ZIPs available under the build script’s input tree. The scripts do not alter the supplied French or English packages. Application of the recorded replacement belongs to the annotated-master build, so the English forms derive from the same decision.
