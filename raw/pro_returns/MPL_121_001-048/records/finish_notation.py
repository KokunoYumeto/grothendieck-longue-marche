from pathlib import Path
import json
from save_page import ROOT,PREFIX,refresh,utc
header=r'''# Diplomatic transcription: notation and doubts

## Notation table — checked before freezing

The table records the glyphs read in this package and their LaTeX representations. The same root reader transcribed and audited all 43 pages from the images, without OCR or access to the context ZIP. Recurrence was checked across the pages; unresolved differences remain marked at their actual occurrences. A clearer neighbouring formula has not been used to supply a stroke absent from another occurrence.

| Ink / usage | LaTeX representation | Scans and comparison outcome |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | Throughout; no typographic double quotation marks substituted. |
| Single / double underline | `\uline{…}`, `\uuline{…}` | Throughout. The short descending stroke of handwritten g in *singulier* on 026–027 has not been treated as a separate underline. |
| Cancellation / insertion / independent margin | `\deleted{…}`, `\inserted{…}`, `\margin{…}` | Throughout; surviving cancelled letters retained, including inside diagrams. |
| Circled words, labels and objects | `\textcircled`, TikZ ellipse/circle | 011, 017, 041, 043; circles checked separately from ordinary parentheses. |
| Square enclosure | `\boxed`, TikZ straight enclosure | 043; retained alongside circled objects. |
| Ordinary set family F | `F`, with subscripts as drawn | 004–024; cancelled earlier initials separately marked. |
| Closed-member family | `F_0` | 006–010, 019; the 0 is a subscript. |
| Family restricted to a subset | `F_A`, `F_U`, `F_B` | 019–024; not replaced by sheaf notation. |
| Partition and its associated family | `\mathcal P`, `F_{\mathcal P}` | 011–022; looped P read consistently, with the uncertain alphabet recorded in the page doubts. |
| Script function algebra | `\mathcal A_F`, `\mathcal A_{(F_{\mathcal P})}` | 004–005, 011. |
| Double-stroked integer and real letters | `\mathbb Z`, `\mathbb R`, `\mathbb N` | 004, 022, 024, 043; ordinary Z in diagrams remains ordinary Z. |
| Triangular capital / lower-case coefficient letter | `\Lambda`, `\lambda` | 004–005, 011, 039; overwritten K/Λ retained as uncertain. |
| Characteristic-function letter | `\varphi_A` | 004–005; distinct visible forms of φ, Φ, π checked individually rather than inferred by role. |
| Upright algebra abbreviation | `\operatorname{Et}(X,\Lambda)` | 004–005; letters preserved. |
| Power-set letter | `\mathfrak P(X)` | 006–007, 015, 019; looped double-stroke P, medium confidence. |
| Interior circle / closure bar | `A^\circ`, `\overline A` | 005–024, 031–037; every bar and circle checked against its occurrence. |
| Dotted boundary letter | `\dot A`, `\dot Y` | 005–006, 009, 015, 018; explicit dot retained. |
| Boundary written with b | `bA`, `bF_i` | 006, 031–032; the literal b remains where written. |
| Complement sign | `\complement` | 005–009, 015, 018; unresolved grouping on 005 remains marked. |
| Greek condition labels | `\alpha`, `\beta`, `\gamma`, `\delta`, `\gamma'` | 007–009, 019; prime on γ′ checked. |
| Implication and inclusion signs | `\Rightarrow`, `\Longrightarrow`, `\Leftarrow`, `\subset`, `\supset`, `\leq`, `\geq` | Throughout. Literal d)/f) references on 012–013 and 018 are retained; the direction is read independently of the claimed proof. |
| Incidence order | `<`, uncertain `<`/`\le`, `\Longleftrightarrow` | 012–014, 031–034; uncertain first sign on 012 remains marked. |
| Finite family Phi | `\Phi`, `\Phi'` | 006, 015–018; prime positions retained. |
| Refinement-set letter | `\unsure{\mathcal E|\mathcal D}` | 016; both occurrences carry the same uncertainty. |
| Regularity family and subscripts | `F_r`, `Y_{\mathrm{reg}}`, `Y_{\mathrm{sing}}` | 017–018. |
| Regularity condition label | circled `\unsure{B|S}`; `\unsure{S|B}` | 017–018. Recomparison retains the two-lobed overwritten glyph on 017 and open S-like glyph on 018; their intended identification remains unresolved. |
| Ring over Y in regularity proof | `\mathring Y_{\mathrm{sing}}` | 018; retained in addition to the separately dotted Y. |
| Sheaf of subset germs | `\underline{\mathcal P}_X` | 020. |
| Generated sheaf / family of sections | `\underline F`, `\overline F`, `\overline{\overline F}` | 020, 023–024; underlines and one/two overbars counted separately. |
| Alternative sheaf notation | `\Phi_F`, `\Gamma(X,\Phi_F)` | 021; the change of notation is literal. |
| Compactified-real example | `\widehat{\mathbb R}`, `\unsure{\mathbb P^1(\mathbb R)|S^1}` as entered locally | 022; the precise displayed uncertain alternatives are retained in the page. |
| Local finiteness / terminal index | literal `loc$^t$`, `X_{\unsure{n+2|n+1}}` | 023; the last digit has a curled 2-like stroke, without correction to an expected index. |
| Uniform dimension axiom | `(e_n)`, `\underline F`-dim | 024. |
| Mobility order | `\nu`, `\nu(x)`, `\nu_0` | 026–028; Greek ν compared with dimension indices n on 047. |
| Open mobility loci / complementary filtration | `\operatorname{Mob}^i(X)`, `F_i(X)`, `Y_i` | 027–028; literal uncertain `F_{3|2}` retained. |
| Pointed normal space | `(N,a)`, `(N_{i|\xi},a)` | 026–028; the literal uncertain a/N wording and y/x in Proposition C remain marked. |
| Script diagram of spaces | `\mathcal X=(X_i)_{i\in I}` | 030, 034, 039; plain X remains plain. |
| Primes on local charts | `X'`, `Y'`, `Z'` | 015–018, 030, 036–037; no prime converted to an exclamation mark. |
| Vertical isomorphism-like mark | `\unsure{\wr|2}` | 030; all four marks compared, with arrowhead/headless differences retained. |
| Filtration / entrance / closed leaf | `F_i`, `bF_i`, `\overline F_{i,\alpha}` | 031–037; *entrantes* and its uncertain endings preserved. |
| Sets of leaves | `\Phi_i`, `\Phi'_i` | 034, 037; margin on 037 visibly writes `\overline F'_i`, retained alongside body `\Phi'_i`. |
| Sheaf letters on a gluing diagram | `\mathcal F`, `\mathcal G`, `\mathcal X` | 039, 043; script style maintained. |
| Primes on gluing maps | `i'`, `p'` | 039; the unprimed p in the pushout diagram is retained as written. |
| Exceptional functor mark | `q_!`, `q^!`, `\alpha_!`, `\alpha^!` | 039; clear exclamation marks kept separate from primes. The two cramped `i^{*|!}` occurrences remain uncertain. |
| Upper / lower stars | `p^*`, `p_*`, `i^*`, `i'_*`, `p'_*` | 039; position of each star checked. |
| Stratum-index letters | `\Sigma`, `I`, `J`, `X_{I,J}`, `\alpha_{I,J/I',J'}` | 039. |
| Dualizing-complex mark | `K^\bullet_{X,\Lambda}` | 039; round raised dot retained. |
| Manifolds with boundary | `V_i^\circ` | 041, 043–047; the superscript circles have not been removed on semantic grounds. |
| Infinity-like superscript | `\unsure{\infty|\circ}` | 042; the two-loop ink remains the first reading despite neighbouring circles elsewhere. |
| Boundary operator and iterates | `\partial`, `\partial_j`, `\partial_{j,h}`, `\partial_{j>h>\ell>m}` | 039, 041–047; comma/order signs and missing base letters retained as locally written. |
| Dotted boundary / bullet | `\dot\partial`, `\partial^\bullet` | 041; unresolved placements explicitly marked. |
| Relative boundary | `\partial_{i/j}`, `\partial_{0/(j)}`, `\partial^{\unsure{\mathrm{pr}|\mathrm{rel}}}` | 041, 047; forms retained separately, without forcing a common notation. |
| Short index letters | `h`, `k`, `\ell` with local alternatives | 041, 047; the h/k switches are explicitly uncertain. |
| Facet / leaf letters | `\Phi_i`, `\Psi_i`, `F_i` | 041, 043; Φ and Ψ shapes checked at each occurrence. |
| Projection letters and decorations | `\pi`, `\pi'`, `\bar\pi`, `\partial\pi` | 043; the circled `\pi_{2,1,2|1}` retains first reading 2, beside the literal `\partial\pi_{2,1,1}`. |
| Prime and circle order | `V^{\circ\prime}`, `V^{\prime\circ}`, `U'`, `U''` | 044–045; order and multiplicity retained. Literal `\partial U` in item6 of044 has not received added primes. |
| Upper / lower-case u | `U_i`, `u_i` and marked alternatives | 045; drawing labels checked separately from the top diagrams. |
| Roman section labels | I, II, III | 045 drawings; retained as written. |
| Short heading on faint sheet | `\unsure{\Phi D|\Phi B}` | 046; one contour after Φ favours D, but remains uncertain. |
| Dimensions below objects | `\underset{n_i-r}{…}` | 047; `n_{j|i}-2` retained where the source appears to switch index. |
| Ordinary arrow / headless stroke | TikZ-CD `\arrow`, `dash`, `no head` | Throughout; headless strokes on 030 and 043 remain headless. |
| Hook at source / curl at terminal end | TikZ-CD `hook`; `-{Hooks[harpoon]}` | 044–047. Both endpoints checked; terminal curls have been reproduced at the terminal end. |
| Product-square crosses | phantom `\times` | 047; each visible cross retained in its diagram cell. |
| Flat bracket / pointed brace | `\underbracket`, `\underbrace` | 041, 047; the flat and pointed shapes were compared and are represented separately. |
| Missing terminal circle | no added `^\circ` | 047 lower grid, last objects of rows3–4; absence retained despite circles in other rows. |

'''
# Check the exact real-compactification line before using the general description above.
header=header.replace('`\\widehat{\\mathbb R}`, `\\unsure{\\mathbb P^1(\\mathbb R)|S^1}` as entered locally','`\\widehat{\\mathbb R}` and a marked P¹(R)/S¹ reading')
(ROOT/'records/doubts_header.md').write_text(header)
tail=r'''## Abbreviations

Expansions are reading aids in this list only; none replace abbreviations in the transcription. Punctuation and superscript endings are kept as drawn in each page file. A proposed expansion of an uncertain abbreviation remains uncertain.

| Manuscript form | Proposed expansion | Scans / qualification |
|---|---|---|
| ens, ens. | ensemble(s) | 004 onward |
| nb, nb. | nombre | 004 onward; 039 uncertain pa./nb. |
| pr | pour / par | 004, 009 and elsewhere; depends on phrase |
| alg., alg | algèbre; algébrique in category lists | 004, 031 |
| an. | analytique | 031 |
| lin. | linéaire | 031 |
| i.e. | id est | Throughout |
| p.ex., p. ex. | par exemple | 021, 023, 027, 030, 033 |
| inv. | inversion | 004, uncertain abbreviation and expansion |
| prem. | premier | 005 |
| loc, loc., loc$^t$ | local / localement | 005 onward |
| top., top | topologie / topologique | 008 onward |
| élts, él. | éléments | 007–009, 039 |
| int. | intersection | 007, 009 |
| syst., sys | système | 009, 027 |
| fond. | fondamental | 009 |
| comp., comp | composante(s) | 010 onward |
| conn., conn | connexe(s) | 019 and elsewhere |
| rel. | relativement / relatif | 007, 010, 017, 019 |
| pt, pt., p$^t$, pts, p$^{ts}$ | point(s) | Throughout; the written form is preserved |
| tt, tte, ttes | tout, toute, toutes | Throughout; expansions do not repair agreement |
| ssi | si et seulement si | Throughout |
| suff., s. | suffisant / suffisante | 008, 032 |
| Néc | nécessité | 011 |
| corres. | correspondance | 011, uncertain |
| corr. | correspondant(e) | 031 |
| Prop., prop., Prop | proposition | 015 onward |
| Cor., Cor | corollaire | 016 onward |
| dém. | démonstration | 016–017 |
| sup., Sup | supremum / bornes supérieures | 016–018 |
| th. | théorème | 014 |
| admiss. | admissible | 014; title reading uncertain |
| gén., général$^t$ | général / généralement | 021–024 |
| QPS | quitte à supposer | 018, expansion tentative |
| resp. | respectivement | 018 |
| cqfd. | ce qu'il fallait démontrer | 019 |
| ss-espaces | sous-espaces | 026 |
| sing. | singulier | 026 |
| homéom | homéomorphisme | 026 |
| comm. | commutatif | 030 |
| gross. | grossière | 035, cancelled/inserted context |
| hyp. | hypothèse | 037 |
| 1re | première | 037 |
| max. | maximaux | 039 |
| can | canonique | 039 |
| préd. | prédécesseur | 041 |
| isom. | isomorphisme | 044 |
| cart | cartésien | 044 |
| v. à b. | variété(s) à bord | 046 |
| id. / idem | idem | 046, uncertain |
| gr-poïde(s) | groupoïde(s) | 043, low-confidence abbreviation |
| mod, mod. | modéré | 002 diagram labels |
| épi | épimorphisme / épimorphique | 002 diagram labels |
| cont | continu | 002 diagram label |
| Ob, Fl | objets, flèches | 002; Fl uncertain |
| NB, Ex | nota bene, exemple | Throughout |

## Legibility and limits

The printed institutional cover (001) is clear. The prose pages are usually readable, but cancellations, short insertions, compressed endings and rewritten quantifiers are materially less secure than the main line. The fast lower proof on011, marginal proof on016, overlapping regularity rewrite on018, and cancellations on023,027,035 have especially fragile readings. `\illegible` is used only for physically obliterated words after attempted readings, never as a substitute for a mathematical symbol.

The faint diagrams on002 and densely written diagrams on039 and041–047 carry many more uncertain labels than the main prose. The bottom of043 is the least secure extended passage: several cancelled groupoid words, the torsor expression and its parenthetical labels remain low-confidence attempted readings. On046 the faint underlying shapes have been approximated in TikZ; their outlines and the uncertain short heading should not be treated as high-confidence palaeographic evidence. All drawings are geometric reproductions, with unavoidable loss of the exact pen trajectory, rather than embedded source images. The long grids on047 preserve the visible objects, arrows and omissions, but the doubtful indices and relative-boundary superscript remain explicitly unresolved.

The independent-looking second reading here was performed by the same reader, as requested, and therefore cannot rule out that reader's systematic errors. The syntax check verifies parsing with a documented wrapper; it provides no additional evidence for a handwritten reading. No context material or mathematical expectation was used to upgrade a reading. The frozen transcription preserves even surprising formulas and visibly inconsistent notation; the later research notes are separate.
'''
(ROOT/'records/doubts_tail.md').write_text(tail)
# Synchronize the root-approved purely syntactic scan002 revision.
p=ROOT/'records/scan002.json';d=json.loads(p.read_text());d['text']=(ROOT/'pages'/f'{PREFIX}_121_scan002.tex').read_text();d['syntax_revision']={'utc':utc(),'note':'Root inserted empty groups before six literal vertical-bar TikZ cells to prevent option parsing; no visible symbol changed.'};p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
refresh()
with (ROOT/'progress.log').open('a') as f:f.write('notation cross-check completed '+utc()+'; root compared recurring alphabets, exponents, primes/exclamation marks, boundaries, indices, quotes, brackets and arrow endpoints against the page audits and targeted images; unresolved differences remain explicitly marked.\n')
print('Notation table and abbreviation/legibility sections completed; page002 record synchronized.')
