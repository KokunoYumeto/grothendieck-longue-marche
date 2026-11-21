# Mechanical notation concordance — scans 054–079 (24 supplied pages)

**Scope:** the 24 current TeX files in `pages/` (054,056–068,070–079), plus `notation.md`, `workflow/notation_review_queue.md`, and the existing `reviewed/` metadata. Scans 055/069 are outside this supplied set. The extension to 079 and the cross-page review use page text and review metadata only. No images, witnesses, frozen first/second readings, external research or compilation were used for this review. No page, reviewed JSON, frozen reading or generated deliverable was changed by the initial concordance review. Later documentary repairs refresh the references and local-variant index below from existing page text and audit metadata; they make no new image reading. The current reviewed records mark the independent box-reading audits complete for all 24 supplied pages. The original cross-page findings and historical hashes, together with the later dated root source resolutions, remain in `workflow/notation_crosspage_review.json`.

**References:** `066:9` means line 9 of `pages/147_scan066.tex`. Counts include canceled text and alternative candidates; they count literal TeX tokens, not distinct handwritten glyphs. This concordance cannot settle ink.

## Documentation flags

The current text shows no unmarked live P/E/Z alphabet change, no phi-to-emptyset replacement, and no prime-to-bang normalization. The seven documentation flags from the earlier 054–078 concordance are now covered by the current `notation.md`; they remain indexed here as local variants or explicit doubts, not transcription corrections:

| Reference | Existing form | Current documentation / caution |
| --- | --- | --- |
| 066:9–11 | `Codim 0`, `codim 1`, `codim 2` | The notation table now records 066’s mixed case explicitly. |
| 064:14 | `\mathbf Z` in a canceled doubtful trial | Sole bold P/E/Z token. Not a live inconsistency; do not normalize the canceled candidate. |
| 066:30 | Roman-IV / triple-prime / double-prime alternatives on I | Explicitly documented as an unresolved prime-count/Roman-numeral choice. |
| 075:2 | Epsilon / membership alternatives | Explicitly documented as a local Greek-letter/sign doubt. |
| 077:10 | Exclamation / natural / canceled-exclamation alternatives on Gamma | Explicitly documented local exception to 057’s definite Gamma-bang habit. |
| 063:38 | `ca.` | The notation table now includes this shorter form beside 064’s `car`/`car.`. |
| 067:7 | Main-text `sss`, inserted `ssi` | The distinct written endings are explicitly documented. |

```tex
064:14  \deleted{\unsure{$\simeq\mathbf Z$}}
066:30  \unsure{I^{\mathrm{IV}}|I'''|I''}(2)
075:2   \inserted{transposition des deux} \unsure{$\varepsilon$|$\in$} $c_i,c_{i+1}$
077:10  \Gamma^{\unsure{!|\natural|\deleted{!}}}_{\underline G}
063:38  (en ca. $\neq2$)
```

## Completed source checks

Root has personally checked all three remaining decoration contrasts. The dated resolutions and historical findings are preserved in `workflow/notation_crosspage_review.json`. These checks confirmed local differences; no page text was regularized.

| ID | Source finding | Crops personally checked by root, relative to `crops/` |
| --- | --- | --- |
| NCR-01 | The serifed I at060:26 has no detached roof. The earlier targets at060:6–9 and058:5 have roofs. Preserve the bare I in(75). | `147_scan060_second_B07.png`, `147_scan060_second_B02.png`, `147_scan058_second_B03.png`, `147_scan058_second_B04.png` |
| NCR-02 | Both NB M factors at060:14 have roofs without bang stems/dots; both factors at060:8 have distinct bangs. The notation entry is scoped to actual bang-bearing occurrences. | `147_scan060_second_B03.png`, `147_scan060_second_B02.png` |
| NCR-03 | At077:4–7 the M-factor I has a roof, the upper T-factor I is bare, and the lower T-factor nu is bare. Both earlier072 nu indices have roofs. | `147_scan077_second_B02.png`, `147_scan072_second_B14.png` |

## Alphabets

| Form | Occurrences by scan |
| --- | --- |
| `\mathbb P` | 061×2, 062×2, 066×5, 070×1, 071×5, 072×2 |
| `\mathbb E` | 063×2, 064×5, 065×1, 071×1 |
| `\mathbb Z` | 060×3, 061×3, 063×3, 064×5, 065×4, 066×2, 068×1, 070×4, 071×6, 072×6 |
| `\mathbb N` | 068×1 |
| `\mathbb G` | 071×1 |
| `\mathbf Z` | 064×1 |
| `\mathcal T` | 077×3 |
| `\mathfrak S` | 057×1, 058×4, 059×12, 060×12, 062×7, 063×4, 066×2, 068×2, 070×1, 071×8 |
| `\mathfrak P` | 066×2 |

All three ornate-X slots in **062:3** retain paired calligraphic/fraktur alternatives: two with `^!_{0,4}` and one with `_{0,4}`. Each alphabet occurs three times as a candidate, matching the notation table. The separate `\unsure{U|\mathbb P}` in **062:28** does not resolve X.

```tex
061:23  \widehat M^!_{0,4}\simeq\mathbb P^1_{\mathbb Z}
065:8   [U]=[\mathbb E^1]-[S_0]-[S_1]+[a_2]+[a_3]
068:4   \nu\in\mathbb N
071:6   \mathbb G_m^{1}\wedge_{\pm1}J'
071:18  M_{D_0}\simeq\mathbb E^1_{\mathbb Z}\setminus\{\text{section }2\}
077:5   \prod_\alpha\mathcal T^+_{g_\alpha,I_\alpha}
077:7   \prod_\alpha\mathcal T^{!+}_{g_\alpha,\nu_\alpha}
077:9   \mathcal T^{!+}_{g,\nu}
```

The outer class brackets on 063–065 remain separate from E; no judgment about their drawn strokes is made. The five E tokens on064 comprise four live glyphs and the canceled doubtful `\mathbb E` candidate at **064:16** in the current page text.

Scan079 adds no `\mathbb`, `\mathcal` or `\mathfrak` token, so the alphabet occurrence table is unchanged by its inclusion.

## Codim and de/des

All table-header occurrences, excluding prose and TikZ coordinate names:

| Page:line | Forms |
| --- | --- |
| 061:13 | `Codim $0$`; `Codim $1$` |
| 062:9–10 | `codim $0$`; `codim $1$` |
| 063:21–22 | `\text{codim }0`; `\text{codim }1` |
| 066:9–11 | `\text{Codim }0`; `\text{codim }1`; `\text{codim }2` |
| 070:16 | `\text{codim }0`; `\text{codim }1`; `\text{codim }2` |

The queued headings are `\uline{Cas \unsure{de|des}}` at **061:6,063:16,066:3**. **070:3** is definite `\uline{Cas de}`. Separate prose `\unsure{des|de} dim. modulaires` at **060:32** retains the opposite candidate order.

## Phi and D subscripts

Four phi tokens: **066:32** once, **073:8** once, **074:13** twice in canceled doubtful text. No `\varphi`, `\emptyset` or Unicode empty-set sign occurs.

```tex
066:32  I'\cap I''=\phi
073:8   M^\infty_{g_\alpha,\widehat\nu_\alpha}\ne\phi
074:13  \deleted{\unsure{\text{on a }I_1\ne\phi\text{ (et card }I_2\ne\phi\text{)}}}
```

| D family | All locations | Match to existing table |
| --- | --- | --- |
| Pointed-loop TikZ | Five tokens on 070:22,23,25,26 | All five snippets identical; graphical definition preserved. |
| `D_{\bullet-\bullet}` | Five tokens on 070:22,23,25 | Segment definition preserved. |
| Ordinary `D_0` | Five tokens on 071:16,18,21,24 | Local oval exception preserved. |
| `D_0\bar\varepsilon` | One doubtful marginal label on 071:15 | Trailing candidate remains separately doubtful. |
| `D_1` | Two tokens on 072:7,10; second deleted | Explicit numeral 1 preserved. |

No D-subscript token occurs on 073–079; no `D_\circ` substitute occurs. Scan079 adds no phi or alternative empty-set token. Exact shared 070 loop:

```tex
D_{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.2ex,line width=.3pt]\draw (0,0)..controls(-.35,.25)and(-.9,.3)..(-.95,0)..controls(-.9,-.3)and(-.35,-.25)..(0,0);\fill(0,0)circle(.6pt);\end{tikzpicture}}
071:15  \margin{$(\unsure{\widehat M_{D_0\bar\varepsilon}})$}
```

## Greek letters and Pi

| Command | Literal occurrence index |
| --- | --- |
| `\delta` | 056×6, 058×1 |
| `\mu` | 056×6, 057×5, 059×9 |
| `\nu` | 054×5, 056×5, 057×5, 059×1, 061×2, 062×1, 068×2, 072×2, 073×8, 075×2, 076×2, 077×2 |
| `\alpha` | 056×24, 057×25, 058×14, 059×23, 060×8, 072×7, 073×7, 077×9 |
| `\beta` | 072×1 |
| `\zeta` | 065×22 |
| `\varepsilon` | 071×8, 075×1 |

Current-page recount includes the `\delta_1` candidate at **058:7** and counts eight alpha tokens on060 after the canceled product at **060:8** was narrowed to its surviving alpha-zero/comma fragment. These are metadata updates to the earlier concordance, not new source readings.

Mu occurs only on 056,057,059. Live tilde-order forms coexist with the explicitly retained **059:17** slip `(\alpha_i,\widehat\mu_i)` and `\alpha=S`. The un-zeroed insertion `\widetilde\mu_\alpha` at **059:14** remains beside alpha-zero forms. These are already explained; no normalization is warranted.

```tex
056:5   3(g_\alpha-1)+\nu_\alpha+\widetilde\mu_\alpha
057:11  \widehat\nu_\alpha
057:13  \unsure{g_{\alpha_0}|g_\alpha}=1
057:17  \widehat I_{\alpha_0}=I_{\alpha_0}+\widetilde A_{\alpha_0}
059:17  (\alpha_i,\widehat\mu_i)
068:3   M^\infty_{0,I} ... \widehat M_{0,I}
072:8   \unsure{J_1|j_1}=2^{\unsure{\alpha}}3^{\unsure{\beta}}
```

Pi forms: **060:32**, one `\Pi_1`; **076:7,30**, three `\Pi`; **077:4,10,12,14**, six `\Pi`; **079:4,6**, three `\Pi` (one canceled doubtful glyph and two live groupoid expressions). **077:2,4,12** has six `\pi_1`; no lowercase pi occurs elsewhere in this set. Different contexts are not treated as interchangeable. Scan079 adds none of the Greek-letter commands in the preceding table.

## Primes, bangs and G underlines

- **071:2,4:** three `\widetilde A'_0` tokens; no tilde-A bang.
- **071:2:** the inline `\unsure{J':|J^!}` retains prime-plus-colon versus raised-bang uncertainty. The detached low point is definite, but clean J primes elsewhere do not resolve its local grouping.
- Definite Gamma bangs: **057:8–9,059:5–7,070:26,28–29,071:12,078:24–25,31,36**. Bare Gamma remains separately. No `\Gamma'` occurs.
- **066:30** retains the I Roman-IV/prime-count choice; **070:3** has a canceled doubtful M-bang; **070:26** has `\widehat M^{\unsure{!}}_{G_0}`. These are not settled by the Gamma habit.
- **077:10** retains the three-way exponent/state doubt; all three 077 Teichmüller capitals are script T with their local plus/bang-plus exponents.
- **078:38** retains a qualified bang in the third margin. The retraced raised mark does not separate a clean stem and detached dot. The first G underline and the absence of the second underline remain separately established.
- **079:2,14** adds three Gamma tokens, all inside canceled, doubtful expressions. Their written candidates have bangs; they do not add three independently definite Gamma-bang readings. The final tuple at **079:2** has two bare Gamma-index G bodies in its doubtful candidate, already explained in the reviewed record.
- **079:2–6** introduces starred M germs. The first opening M has a hat and star; the second roof is crossed and uncertain. The independent inserted hat at **079:3** remains distinct from its doubtful G underline. Both M bodies in **079:6**, display (100), are bare; each raised sign remains `\unsure{*|\leftarrow}`. The star/left-arrow alternatives do not supply a roof over either M. These are documented local forms, not reasons to supply a missing hat.
- **079:4** has a prose asterisk after `fondamentaux`; **079:8** has the written page reference `768'`. Neither is substituted for an M exponent or treated as an inferred footnote.

Already explained G variations:

```tex
056:3,16   \underline G
056:5,14   \delta(G)
057:15     \widehat M_G
058:3      \Gamma_{\underline G} ... \widehat M_G
076:26     \Gamma_{\underline G}=\operatorname{Aut}\underline G
077:4      \alpha\in S(\underline G)
077:10     (\Pi M_{\underline G},\Gamma_G)
077:12     ...\Gamma_{\underline G}) ...\Gamma_{\underline G})\relbar\joinrel\relbar\Gamma_G
078:31     (\widehat M_{\underline G},\Gamma^!_{\underline G,\underline G'})
078:36     (M_{\underline G},\Gamma^!_{G,G'})
078:38     \Gamma^{\unsure{!}}_{\underline G,G'}
079:2      \unsure{(\widehat M_{\underline G},\Gamma^!_{G,G'})}
079:3      \widehat M_{\unsure{\underline G|G}}
079:4      M_{G'}
```

Literal underlined-G totals: **056×3,058×4,076×7,077×12,078×32,079×27**; 078 has 17 unprimed/15 primed. Counts include canceled material and alternative candidates. Graphical G at **076:7–12** is excluded. Bare M/G subscripts on 057–060,072–073 and indexed G-zero/G-one on 070–072 must not be regularized from later notation. The local absent bars and doubtful bar on079 are explicitly explained in `notation.md` and `reviewed/147_scan079.json`.

## Reduced à, operators, maps and names

```tex
063:14  resp\textsuperscript{t} :
066:32  points à l'infini ... pts à l'infini
067:8   correspond \unsure{à|:} celle
071:16  \inserted{(pt. $P_0$)}\unsure{:|;|à} la trajectoire
072:3   correspond à la section à l'infini, et $P_1$ à la section $2$
077:14  relativement à deux sortes de
079:23  donnant lieu \unsure{à|:} des morphismes de groupoïdes
```

The 077 context joins the comparison without deciding earlier punctuation; the reduced mark on079 also remains explicitly doubtful. Operator doubts remain at **064:21** (`+`/set-minus), **065:30** (between zeta 2/zeta 3), **074:25** (first canceled cardinality comparison, `\geq|>`), **074:82** (between 2/ell), **075:45,65** (index signs). **075:44** is plain `c_{i-1}`; its repeated minus has not been regularized.

**065:18** has `\unsure{\longrightarrow}`: the recorded blind audit qualifies its rounded endpoint. **070:29** retains `z\longmapsto z^{-1}`; **071:21** uses plain `\longrightarrow` twice; **077:12** retains the unheaded bar before Gamma. The 078 hooks remain drawing instructions. **079:16–18**, diagram (101), has a headless upper connection, a downward arrow and a lower rightward arrow; the existing reviewed metadata explicitly distinguishes them. **079:8** has `\underset{\longrightarrow}{\lim}`, a rightward limit marker rather than a diagram edge. No new visual-head comparison was made in this review.

**076:3** has `Teichmuller`; **077:9** has `Teichmüller`; no 078–079 occurrence. This local accent variation is already explained.

## Short-form index

Word boundaries exclude TikZ units and coordinate names. Alternatives and canceled text are included; no expansion is inferred.

| Written form | Page:line occurrences |
| --- | --- |
| `top` | 054:3 |
| `top.` | 054:3 |
| `homéom.` | 054:3, 054:7 |
| `isom.` | 068:8, 075:2 |
| `iso` | 057:4, 057:13, 072:3, 072:10 |
| `nb` | 054:7, 065:12, 066:32 |
| `dim` | 056:16, 057:5, 058:7, 058:9, 058:15, 058:16, 059:18, 060:3, 060:22, 061:4, 073:6 |
| `dim.` | 057:5, 058:7, 058:16, 060:32 |
| `can.` | 057:13 |
| `trivialt` | 060:27, 071:16 |
| `comp.` | 068:6 |
| `standart` | 068:3 |
| `ca.` | 063:38 |
| `car` | 064:23 |
| `car.` | 064:23 |
| `ell.` | 064:14 |
| `gr.` | 064:14 |
| `autom` | 072:8, 078:25 |
| `hom.` | 078:25, candidate within `\unsure{la flèche\|l'hom.}` |
| `automs` | 064:14, within `\unsure{automs\|autos}` |
| `autos` | 064:14, alternative to automs |
| `pt` | 057:4, 062:21, 068:8, 071:2 |
| `pt.` | 071:16 |
| `pts` | 061:19, 064:14, 066:32, 067:2, 068:6, 070:29, 071:2, 071:16, 075:2 |
| `ens` | 071:2, 076:7 |
| `ens.` | 061:19, 078:3 |
| `def` | 066:33 |
| `déf` | 063:36 |
| `déf.` | 078:24 |
| `sss` | 066:32, 067:7 |
| `ssi` | 067:7 |
| `DPS` | 073:10 |
| `OPS` | 074:15, 074:25 |
| `resp` | 063:14, 073:45, 073:48 |
| `resp.` | 079:2, in canceled text |
| `revêtts` | 079:8 |
| `équiv` | 079:20 |
| `n°` | 079:8 |
| `p.` | 079:8 |
| `quelc.` | 061:19, 074:15 |
| `évt.` | 072:12 |
| `géom.` | 072:16 |
| `éch.` | 074:25 |
| `ég.` | 056:21 |
| `él` | 075:2 |
| `élts` | 071:2, 075:2 |
| `elmts` | 066:35, within `\unsure{elmts\|elts}` |
| `elts` | 066:35, alternative to elmts |
| `mult.` | 059:20 |
| `prop.` | 068:8 |
| `icos.` | 066:35, 067:2 |
| `mod` | 054:3, 058:9, 058:16, 059:18, 075:2 |
| `i.e.` | 056:22, 056:24, 057:5, 058:7, 058:9, 058:22, 058:31, 058:36, 059:14, 059:17, 060:32, 066:32, 066:35, 067:7, 072:12, 074:25 |

Additional raised/doubtful forms: **054:7** `isom\unsure{.}`; **062:21** `p\textsuperscript{ts}`; **063:14** `resp\textsuperscript{t}`; **076:7** `\unsure{canoniq\textsuperscript{t}}`. Prose repetition signs remain literal `$=$` at 062,065,071,072,074,075,078.

Scan079’s reviewed abbreviation entries explicitly preserve `resp.`, `revêtts`, undotted `équiv`, `n°`, and `p.`; their expansions are not inserted into the page. At **079:8**, the two separate groups `\unsure{ou} ou` remain across the source line break. This written repetition is already documented and is not collapsed. The same line retains `multi-plicités`: the blind audit identifies a separate hyphen after multi at the physical line end.

## Scan079 coverage references

All source descriptions in this section are carried from the current page and its existing reviewed record; no new image reading was made.

| Page-text locations | Covered feature | Existing crop references, relative to `crops/` |
| --- | --- | --- |
| 079:2–3 | Opening starred pair, canceled roof state, whole crossed l’infini/l’âme and de la réunion/sur le germe alternatives, canceled formulas, and inserted independent hat with uncertain G bar | `147_scan079_second_B01.png`, `147_scan079_second_B02.png`, `147_scan079_second_B03.png`; canceled tuple detail `147_scan079_place18.png` |
| 079:4,6 | Qualified Ils sont donc prefix, local bare G-prime, prose asterisk, canceled Pi, and both bare M bodies in (100) with both raised signs star/left-arrow uncertain | `147_scan079_second_B04.png`, `147_scan079_second_B05.png`, `147_scan079_second_B06.png` |
| 079:2,8 | `resp.`, rightward limit, repeated ou, `revêtts`, visible `multi-plicités` hyphen, and the written `[5], n°5, p. 768'` reference | `147_scan079_place02.png`, `147_scan079_second_B07.png`, `147_scan079_second_B08.png` |
| 079:12–21 | Diagram objects, separately doubtful canceled groups, headless upper shaft, two headed arrows, undotted équiv and detached closing curve | `147_scan079_second_B09.png` |
| 079:23–24 | Reduced à/colon doubt and separate pencil foliation | `147_scan079_second_B10.png`, `147_scan079_second_B11.png` |

**Coverage complete:** mechanical concordance for all 24 supplied pages. **Source checks NCR-01–03 are complete.** Root confirmed the local source variations listed above; no page text changed in that final notation check.
