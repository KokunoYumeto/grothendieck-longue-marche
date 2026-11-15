# Notation table

The following decisions were made from the scans before the context archive was opened. A common typesetting form records a common visible sign; it does not assert that its mathematical meaning is constant throughout the manuscript. The root reader compared the signs during the sequential reading and the complete second visual audit, then checked the cross-page command concordance and the remaining differing readings. Local uncertainty is retained when the ink does not decide.

| Visible sign or practice | LaTeX used | Scans and cautions |
|---|---|---|
| Single raised slant after a letter or numeral | `'`, occasionally `\prime` inside a doubt marker | Throughout; especially 127, 132, 137, 140, 151–154, 157–159, 161–163, 169, 172, 174–176. Primes are not exclamation marks. |
| Raised star | `^*` | 151, 157, 160; distinguish the duality stars from primes. |
| Final punctuation after the counting inequality | `\unsure{?\|!}` | 131; the punctuation remains uncertain. No exclamation-mark exponent has been identified in these fifty scans. |
| Small crossed/angled strip label | `\unsure{\lambda\|1}` | 127; lambda is the ink-first reading after the second inspection, not an inferred count. |
| Looped sigma with a projecting upper stroke | `\sigma`, with written indices or primes | 127, 131, 133, 135–140, 146, 153–154, 157. Local faint or overwritten occurrences remain marked. |
| Consecutive indexed signs versus unordered-looking pairs | `\sigma_i\sigma_j` versus `(\sigma_i,\sigma_j)` | Especially 135–140, 146, 157. A product was not substituted for a written parenthesized pair, or conversely. |
| Long descending Greek sign with a small upper curl | `\unsure{\zeta\|\xi}` and corresponding barred form | 132; the same unresolved distinction is retained across its sequence and circle occurrences. The separate cancelled trial sign is an uncertain xi. |
| Looped alpha/beta; rho in position-relative labels | `\alpha`, `\beta`, `\rho` | 131–133, 137, 151, 157–159, 162–163, 169, 176. The ambiguous `\beta_f\|P_f` on 137 stays local. |
| Gamma versus delta in faint pencil | `\unsure{\gamma\|\delta}` | 158. It is not silently made identical with the delta used on 154 or 160. |
| Large phi form | `\varphi` | 132, 136, 160; the occurrence on 136 is cancelled. |
| Lowercase and uppercase orientation signs | `\omega`, `\bar\omega`, `\Omega`, `\Omega'` | 133 onward. Bars, capitals and primes remain distinct. The local capital-Omega expressions on 133 were not normalized to lowercase. |
| Two-lobed epsilon form | `\varepsilon` | 136, 154, 171. The faint 136 occurrence and the first 171 definition are uncertain. |
| Angular descending multiplicity sign | `\nu`; `\unsure{\nu_a\|\ell_a}`, `\unsure{\nu_s\|\ell_s}` | 154 versus 171. A fresh comparison confirmed the more distinct nu on 154; the hurried 171 form remains unresolved consistently in prose and both sums. |
| Tilde with fork-shaped raised sign | `\widetilde X^{\swarrow\!\searrow}` | 135–136; two descending legs are visible. The TeX `\!` here is only negative spacing, not a transcribed exclamation mark. |
| Tilde on the triangular symbol and on its index | `\widetilde{\Delta}_{\widetilde{\unsure{S\|s}}}` | 132; case of the index remains uncertain. |
| Tilde versus directional stroke above an indexed set | `\unsure{\widetilde{I\setminus\{i_0\}}\|\overrightarrow{I\setminus\{i_0\}}}` | 132; no arrowhead was supplied on mathematical grounds. |
| Check accent and star on X | `\check X`, `X^*` | 158 and 151/160 respectively; the two decorations are preserved separately. |
| Uppercase X versus calligraphic form | `\unsure{X\|\mathcal X}` | Cancelled heading on 160. |
| Prime and overstroke on K | `\unsure{\widetilde K'\|K'}`, `\unsure{K\|K'}` | 171; repeated references do not resolve the local overwritten stroke. |
| Closure bars and inclusion-like sign in the face equation | `\unsure{\overline F}`, `\unsure{\subset\|\in}` | 171; retained at each affected occurrence. |
| Delta and relation beside a boundary band | `\unsure{\Delta=0\|\Delta\simeq0}` | 176; several strokes overlap the coloured band, so the relation is not secure. |
| Plain connecting stroke, pointed arrow, dashed/dotted route | TikZ/TikZ-CD `dash`, direction and dash-style options as observed | All drawings and diagrams; arrowless joins stay arrowless. Geometric strokes are not converted into implication symbols. |
| Double quotation marks | Two backticks and two apostrophes | 133, 135, 151, 154, 158, 160. No guillemets have been supplied in place of these marks. |
| Raised abbreviation ending | `\textsuperscript{t}`, `m\textsuperscript{me}` | 138 and 160; expansions occur only below. |
| Low marginal consecutive numerals | `\margin{\mspage{n}}` | All fifty sheets show 126–175, corresponding to scans 127–176. This records visible pagination without establishing who supplied it. |

## Abbreviations

Expansions below are editorial proposals, not additions to the transcription. A dot, absence of a dot, superscript, or spelling variation in the page files follows the local reading.

| Written form | Proposed expansion or meaning | Location / qualification |
|---|---|---|
| p.r.; position r.; pos. | position relative; position | 133–160. |
| p.r. au | par rapport au | 135; distinct from the preceding technical abbreviation. |
| p.r. s.o. | position relative; suffix unresolved | 137; no confident expansion of `s.o.` is offered. |
| l.p.r. | likely ligne/lieu des positions relatives | 157 drawing label; low confidence, the first letter is not securely expanded. |
| ps. droites; ps. dr. | pseudo-droites | 153. |
| stble; stbles; semi-stble; semi-stbles; instble | stable(s); semi-stable(s); instable | 142, 151, 153–154, 160; uncertain endings stay marked in the text. |
| ens; l'ens. | ensemble; l'ensemble | 133, 154. |
| elt.; élém.; élémts | élément; éléments | 133, 135. |
| op. | opération | 135. |
| dim | dimension | 135, 154. |
| ori. | orientation | 136. |
| gén; gén. | générisation | 151, 176; the actual final label on 176 has an ink-first `épéc` doubt and is not expanded in the transcription. |
| spéc | spécialisation | 176. |
| changᵗ | changement | 138; entire abbreviation remains uncertain. |
| bisect. ang. | bissecteurs angulaires | 135 margin; proposed expansion. |
| fus | fuseau(x) | 135 margin; reading and number uncertain. |
| ds | possibly droites | 135 brace label; low confidence. |
| arcs sort. | arcs sortants | 151. |
| somm. | sommets | Cancelled text, 151. |
| vois. | voisinage | 151. |
| corresp.; correspond. | correspondance; correspond/correspondant, according to phrase | 151, 153, 158. |
| comp. connexe | composante connexe | 153. |
| syst. | système | 153. |
| canon. | canonique | 153–154. |
| tt | tout | 153. |
| mᵐᵉ | même | 160; handwritten superscript ending is retained. |
| pt; pts | point; points | 160, 171. |
| dis. | disons | 160. |
| cf. | confer / compare | 160. |
| int; int. | intérieur | 171. |
| rev. | revêtement | 171; proposed reading and expansion. |
| 1-compl. | 1-complexe | Cancelled line, 171; uncertain. |
| gr. | graphe, possibly groupe | Cancelled phrase, 171; low confidence. |
| nb | nombre | 171. |
| indép. | indépendant | 171. |
| fluo | fluorescent | 166; uncertain. |
| i.e. | id est | 133 onward. |
| resp. | respectivement | 158. |
| NB | nota bene | 133, 153–154. |
| DDNAME | data definition name | Reused computer output, e.g. 127, 145, 157, 166. |
| RECORDS-NB / RECORD-NB; BYTES-NB | number of records; number of bytes | Printed headings; local differences preserved. |
| STD. | standard | Printed forms, e.g. 127, 145, 157. |
| SYSMSG; SYSIN; SYSOUT | system messages; system input; system output | Reused listings, not mathematical notation. |
| PGM; EXEC; DD; DSN | program; execute; data definition; data-set name | Reused JCL and job logs. |
| MSGLEVEL; MSGCLASS | message level; message class | Reused JCL, e.g. 153–154, 164. |
| FCB; UCS | forms control buffer; universal character set | Printed listing headings; contextual technical expansions only. |
| SRB; VIO; TCPU; ELAPS | service request block; virtual input/output; CPU time; elapsed | Printed accounting tables, especially 169; exact units and uncertain column readings are not inferred. |
| C.U.; C.C.U / T.C.U | accounting-unit headings; expansion not established here | Printed tables, 150, 169. |
| GRAPH. | graphiques | Printed plotting form, 142. |
| CFT; JES2; MVS/SP | software/system identifiers | Printed listings. They are kept as identifiers; no expansion is needed to read the manuscript. |

## Legibility and limits

The package alternates relatively readable black-ink prose with faint pencil, coloured overtracing, heavy cancellations and computer output showing through reused paper. The strongest prose is still compressed and contains genuine unfinished clauses, surprising numbering and local corrections. The least secure prose is the marginal NB on scan 153, parts of the cancelled passage on 151, several phrases of the cancelled draft on 160, and the compressed conditions on 171. The word after “droites” on 158 and the caption beginning `Canali|Canaux` on 166 are particularly doubtful; they should not support an argument without renewed inspection.

The least secure printing is on 141, 162, 166 and 168. In particular, `\illegible{45}` on 162 is a rough estimate for faint printed words that could not be individually segmented at enlargement, not a recovered forty-five-word passage. Other unreadable-word counts are estimates too. The numerical fields under the coloured strokes on 169 are retained with explicit alternatives, including the differing printed totals; agreement with another listing has not been used to repair them. Printed dates in August 1982 are dates of computer output, not automatically dates of the manuscript inscriptions.

TikZ preserves visible curve systems, directions, approximate relative positions, colours, hatching, pencil construction lines and labels. Its coordinates are manually estimated from the images and are not geometric measurements or a proof of topological equivalence. Dense overwritten labels on 132, 137, 140–141, 146, 169, 172 and 174 are weaker than the clean labels beside them. Printing has been reflected or rotated for visual reading where necessary; no OCR was used.

The table below includes every uncertainty-macro occurrence, including repetitions and the complete contents of large uncertain printed blocks. “Approximate location” is the line in the corresponding page's TeX source, with an occurrence number for repeated markers on that line; it is a navigation aid, not a claim about manuscript lineation. The accompanying `records/doubts_extracted.csv` retains surrounding source snippets. Confidence means confidence in the proposed reading: **medium** is plausible but insecure; **low** is substantially unresolved, has competing readings, belongs to especially weak ink, or covers a long obscured block. No reading explicitly marked uncertain is rated high. These conservative labels do not certify unmarked text as error-free.

# Doubts by occurrence

