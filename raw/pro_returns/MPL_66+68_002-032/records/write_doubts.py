"""Build the doubt register from the exact macros, with root-reader judgments.
No OCR or contextual reading enters this report. Historical pre-context generator.
The final Markdown also incorporates abbreviation-list QA recorded afterwards.
Re-run only before context.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'records/doubt_occurrences.json').read_text())
header=r'''# Recurring notation

| Ink / use | LaTeX reading | Cross-page evidence and caution |
|---|---|---|
| Position set and successor relation | `C`, `R`, `R(x)` | 68/002–013, 024–032. C is open; G usually has an inward stroke. Local uncertain C/G readings remain marked. |
| Terminal positions and finite-height layers | `C_0`, `C_{-1}`, `C_i`, `C_\infty` | 68/002–003; the zero, minus-one, and infinity indices are distinct. No uniform finite bound is supplied by an infinity subscript. |
| Player set and initiative | `J`, `j`, `j'`, `i(x)`, later `\alpha(x)` | 68/002 versus 024 onward. The change from i to alpha is in the manuscript. Primes were checked individually, not supplied by symmetry. |
| Winning sets | `G_0(j)`, `G(j)` | Throughout both game drafts. G and C, and 0 and omitted subscripts, are not silently interchanged. |
| Complement notation | `\overline C(j)`, `\bar C(j)`, `\overline G(j)`, `\complement G(j)` | 68/003–013 versus 024–032. The underlying domain of the bar-C complement changes between drafts; this is not a font error. |
| Strategies and restrictions | `\Sigma`, `\Sigma'`, `\Sigma_0`, `\Sigma_y` | Throughout the game drafts. Sigma has angled strokes, unlike the separate right-angle capital below. |
| Arbitrary subset of winning positions | `\Gamma` | 68/006–009. The repeated sign has a left vertical stem and a horizontal top to the right; comparison across these pages supports Gamma, rather than a script T. |
| Reachability comparison | `\unsure{\succ|\geq}` | 68/007–009. Distinct from the ordinary numerical/well-order `\leq` on the same leaves; faint lower strokes keep the exact sign uncertain. |
| Power sets and nonempty finite subsets | `\mathcal P`, `\mathcal P^*`, `\mathcal P_f` | 68/002, 017, 019, 021–025; calligraphic open P, not an ordinary P or Greek rho. |
| Empty set / a written zero | `\varnothing`, `0` | Slashed oval retained as empty set. Literal `R(x)\ne0` in 004 is not normalized to empty-set notation. |
| Disjoint union | `\coprod` | The perpendicular bars in 002 and the later decompositions are retained. |
| Indexed finite sets | `E_i`, `F_j`, `V_i` | 68/015–017. E/F/V and indices were compared across the scratch sheets; anomalous `F_i` with j in the interval remains marked, not repaired. |
| Group algebra / function notation | `\mathbb R[G]^+`, `\mathbb R(G)^+`, `C(G)^+` | 68/019–022. Parentheses and brackets fluctuate in the ink and are not globally regularized. |
| Permutation group | `\unsure{\mathfrak S_G}` | 68/019; the intended alphabet is not fully secure, so the whole Gothic reading stays marked. |
| Rearrangement pairing and ordinary pairing | `|f,g|`, `\langle f,g\rangle` | 68/019–021. These are different notations on the page; the first is not silently replaced by the second. |
| Convolution and group action | `\ast`, juxtaposition | 68/015–022. Stars in products are not primes; missing product signs are not supplied. |
| Reflection / inverse image under inversion | `\check A`, `\check f`, `\check g` | 68/017, 020–022. V-shaped accents were compared with the wavy accents on lifted elements; one check/tilde ambiguity in 017 remains explicit. |
| Lifted group and elements | `\tilde G`, `\tilde g`, `\tilde h` | 68/017. Written untilded G in two quantified expressions is retained even where a tilde may be mathematically expected. |
| Level-set families | `E_\alpha(f)`, `E_\ast(f)` | 68/019–022. Alpha and star have different forms. |
| Translations and two-torsion | `\varepsilon_s`, `{}_2G`, `i(u)` | 68/017, 020–022. Epsilon is not a Latin e; the 2 is a left subscript in the exact sequence and kernel condition. |
| Families of subsets / cones | `\mathcal A`, `\mathcal B`, `C(\tilde g)` | 68/017. The B in the condition on the second factor is retained, not changed to A. |
| Majorization relation | `\prec`, `\sim` | 68/019–022. This `\prec` is not the faint reachability sign in the earlier game draft. The order-to-preorder correction is represented as a deletion and insertion. |
| Recurrent adjective in the convolution notes | `\unsure{pritorisé|priorisé}` (and plural) | Six full-word occurrences in 020–022 were compared before the freeze. The first reading is a low-confidence attempt at the visible pri- plus tall middle stroke, not a normalized French spelling. `privilégié` is another possible reading; inserted `pri` remains abbreviated. |
| Selected initial position and eventual value | `\varepsilon(x)`, `\unsure{\xi|\zeta}` | 68/027–029. Epsilon is distinct from the capital E of the set E(x); the overwritten E/epsilon occurrence in 028 is explicitly unresolved. |
| Current-player classification | `G^*`, `P^*`, `N^*` | 68/031. Stars are literal; no exclamation-mark exponent is identified in the supplied pages. |
| Initiative extension and opposite player | `\hat\alpha`, `\bar\alpha`, `\overline{\hat\alpha}` | 68/031–032. A hat is not supplied on the final G formula of 032 where the ink has alpha without one. |
| Double quotation marks | two backticks and two apostrophes | Used consistently for the manuscript's double quotation marks, including the cancelled Schubert/Bruhat prose. |
| Underlining and page interventions | `\uline`, `\uuline`, `\deleted`, `\inserted`, `\margin` | Underlines, cancellations, interlinear additions, and independent marginal notes are kept distinct. The typed table border on 018 is not treated as an underline. |

# Doubt register

All readings below come from the frozen page files. The table lists every `\unsure` occurrence, including repeated signs and cancelled words; there are no `\illegible` omissions. “Line” is the exact one-based line in the named page file, a reproducible locator rather than an assertion that TeX line wrapping matches the handwriting; the broad vertical position is approximate and follows the transcription's reading order on rotated sheets.

Confidence concerns the **first tentative reading**: medium means identifiable strokes with an unresolved letter, sign, ending, or overwritten region; low means a substantially obscured or compressed reading, especially in cancelled scratch work. No doubtful occurrence has been promoted to high confidence merely because its mathematics is plausible. “No distinct alternative” means that the visible attempt itself remains uncertain, not that the passage was securely read.

| File | Scan | Approximate position / line | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|---|
'''
low_scan={7,15,16}
low_lines={2:{20,24,54},3:{14},4:{5,9,16,18,25,28,32},5:{3,6,24,28,29},6:{9,14,16,18,19,21,23},8:{3,6,7},9:{3,9,15,17},10:{3},11:{9,11},13:{20,44,54},17:{31,38,42,48,58,60,65},19:{6,30},20:{12,26,28,39,40,42},21:{2,3,34,57},22:{2,15,17,21,31,35,60},25:{26},26:{23},27:{2,14},28:{21,35},29:{10},31:{12},32:{2,19}}
def esc(s):
 return s.replace('|','&#124;').replace('\n',' ')
def code(s):return '`'+esc(s)+'`'
rows=[]
for q in d['occurrences']:
 n=q['scan']; line=q['tex_line']; lines=len((R/'pages'/q['page_filename']).read_text().splitlines())
 ratio=line/max(lines,1); pos='upper' if ratio<.34 else ('middle' if ratio<.68 else 'lower')
 conf='low' if n in low_scan or line in low_lines.get(n,set()) else 'medium'
 alts=[code(a) for a in q['alternatives']]
 if 'pritorisé' in q['reading']:alts.append(code('privilégiés' if q['reading'].endswith('s') else 'privilégié'))
 rows.append(f"| {q['page_filename']} | {n:03d} | {pos}; line {line} | {code(q['reading'])} | {'; '.join(alts) if alts else 'No distinct alternative'} | {conf} |")
footer=r'''

# Abbreviations encountered

Expansions in this section are editorial suggestions only. The abbreviations, their punctuation, and truncated words remain as written in the transcription.

| Written form | Likely expansion or interpretation | Examples / caution |
|---|---|---|
| `NB`, `N.B.` | nota bene | Repeated marginal and interlinear notes; punctuation varies. |
| `i.e.` | id est, “that is” | Throughout; the first occurrence in 002 is itself uncertain. |
| `ens`, `ens.` | ensemble | 024, 032 and elsewhere. |
| `conf.` | configurations | 024. |
| `Prop`, `Prop.`, `prop.` | proposition | 004, 008, 019, 026–028; several headings are cancelled. |
| `Th`, `Th.`, `Thm` | théorème | 004, 010, 013; the small final m in 004 is uncertain. |
| `Dém`, `Dém.` | démonstration | Game proofs and 020. |
| `Def` | définition | 020; no accent is supplied in the page file. |
| `Cor` | corollaire | 020; the fully written cancelled Corollaire in 029 is not an abbreviation. |
| `hyp`, `hyp.` | hypothèse | 004–006, 008, 021. |
| `comp.` | compatible | 003–013, 025, 029; context distinguishes it from composition. |
| `strat.` | stratégie | Cancelled draft, 007. |
| `gagn.` | gagnante | 027. The cancelled `ga` in 005 is only a truncated beginning. |
| `pb.` | problème | 005. |
| `pos.` | position | 005. |
| `rec.`, `réc.` | récurrence | 005, 008, 012; the accent is not standardized. |
| `cqfd`, `cqfd.` | ce qu'il fallait démontrer | 005, 027. |
| `cq` | possibly a shortened cqfd | 028; uncertain truncated mark, not expanded in the transcription. |
| `tt`, `tt.`, `tte` | tout / tous / toute, according to use | 006, 009, 021, 028–029; in 021 and 028 a universal-quantifier reading is kept first where its stroke is closer to the ink. |
| `sss`, `ssi` | si et seulement si | 015, 019–022; the final s/i is sometimes ambiguous. |
| `t.q.` | tel que | 020. |
| `resp.` | respectivement | 031. |
| `gr` | groupe | 017. |
| `hom.` | homomorphisme | 017. |
| `tot`, `tot.` | totalement | 017, 019–022. |
| `ord.`, `ord` | ordonné / ordonnés | 020–022. |
| `croiss.` | croissante | 002. |
| `sym.` | symétrique / symétriques | 021. |
| `inv.` | invariant / invariante | 021. |
| `équ.`, `équiv.`, uncertain `eq` | équivalence / équivalent | 020–021; meaning depends on the surrounding sentence. |
| `Impl.` | implication | 003, uncertain. |
| `pri` | beginning of the unresolved adjective in 020–022 | Inserted over cancelled “bon” in 022; not expanded from an assumed technical term. |
| `id` | idem | Oblique marginal comparison in 022. |
| `OK`, `O.K.` | agreement / completion mark | Retained literally. |
| `éch.` | échelon | Typed administrative table, 018. |
| `Enseign.` | enseignement | Typed heading “Discipline d'Enseign.”, 018. |
| Personal initials, including `A.`, `B.`, `Ch.`, `J.`, `M.` | Initials only; no name expansion attempted | Typed personnel table, 018. |

# Legibility and limits

The principal game-theory prose is usually legible, but fine indices, priming, brief insertions, and words traversed by cancellation strokes remain less secure than the main text. The first draft (002–013) is particularly crowded around the repairs of the local strategy proof, and the wholly cancelled leaf 007 should be read with its cancellation state always in view. The second draft (024–032) is clearer overall, although E versus epsilon, overwritten starting indices, and the final hats and subscripts still need the explicit doubts recorded above.

The least trustworthy passages are the dense arithmetic/convolution scratch work in 015–017 and the recurrent adjective in 020–022. Their numeric arrays, signs, small deleted expressions, and drawings have been included, but low-confidence marks are substantive cautions, not assurances of decipherment. The cancelled Schubert/Bruhat prose in the opposite orientation on 016 and the oppositely oriented group-family axioms on 017 have their own reading order indicated in TeX comments. The diagrams and freehand marks are encoded as arrays or TikZ; their geometry is an approximation of the visible arrangement, while the labels retain the textual doubts.

The typed personnel sheet 018 is much clearer than the handwriting; its names, dates, numbers, and institutional headings are transcribed as printed, including the open parenthesis in the last-promotion entry for GRIMAUD. The sparse 014 has only a section heading. Neither a printed date on reused paper nor an archive corner number has been converted into an authorial date or authorial page number.

All 30 supplied whole-page images and their two supplied halves were inspected by the same reader, with a complete second page-by-page reading before the freeze and a final comparison of recurring notation. No OCR, manuscript-reading subagent, or contextual text was used to supply readings. A separate mechanical parser extracted the doubts and checked syntax/bookkeeping; that check does not establish palaeographic accuracy. No `\illegible` macro was necessary: an uncertain visible attempt was retained wherever the ink could support one, including attempts that may ultimately prove wrong.

Scope: the supplied images are cote 68, scans 002–022 and 024–032, 30 pages in all. Scan 023 is omitted as blank in the input; cote 66 scans 002–005 were not supplied because the task says another run transcribed them. No replacement text has been invented for those absent images. The later “34 pages” phrase in the instructions does not change this image inventory.
'''
(R/'MPL_66+68_002-032_doubts.md').write_text(header+'\n'.join(rows)+'\n'+footer)
print(f"Wrote {len(rows)} doubt rows; root-reader confidence judgments applied.")
