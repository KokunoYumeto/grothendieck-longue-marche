from pathlib import Path
import re, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from save_page import rebuild_doubts

ROOT = Path(__file__).resolve().parents[1]
target = ROOT / 'MPL_12_051-098_doubts.md'
rebuild_doubts()
current = target.read_text(encoding='utf-8')
body = current.split('# Doubts by page',1)[1].split('# Abbreviations',1)[0]
rows=[]
for line in body.splitlines():
    m=re.match(r'\| 12 \| (\d+) \| TeX line (\d+) \|',line)
    if m:
        scan, source_line=map(int,m.groups())
        # Editorial confidence judgments from the primary reader's two visual passes.
        if (scan in {52,58,61} or (scan==55 and source_line>=8) or
            (scan==59 and source_line>=10) or (scan==51 and 20<=source_line<=22) or
            (scan==72 and source_line>=9) or (scan==94 and source_line>=32)):
            line=line.removesuffix(' medium |')+' low |' if line.endswith(' medium |') else line
    rows.append(line)
body='\n'.join(rows).replace('| Cote | Scan |', '| File | Scan |').replace('| 12 |', '| 12.pdf |')
heading=r'''# Notation table

This table records the primary reader's visual decisions before the context archive was opened. The second pass covered every whole page and both supplied halves; the package concordances were then checked for inconsistent representations. Differences retained below correspond to visible differences or explicit unresolved alternatives, not mathematical normalization. The concordance files in `records/` are literal indexes, not independent readings.

| Visible sign / usage | LaTeX transcription | Visual reservations / scans |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | The same convention throughout; no replacement by guillemets. |
| Underlining; double underlining | `\uline{…}`; `\uuline{…}` | Extent follows the ink; e.g. extended double underline at 082. |
| Exclamation point, prime, star | `!`, `'`, `*` | Kept distinct. The compact-support signs on H and R are `!`; prime marks on X, M, A, and forms remain primes. |
| Compact-support cohomology | `H^i_!`, and the visibly different position `H!` when applicable | 051, 058, 067, 092–094; do not supply a missing `!` to the later h on 092. |
| Curled Tate-like symbol | `\unsure{\xi\|\zeta}` | 051, 054, 058: same unresolved family; no choice supplied from meaning. The deleted marks on 067 remain bracket/`\xi` alternatives. |
| Category M and its variants | `M`, `M^+`, `M_i`, `M_\ell` | Ordinary capital, with each sign/index preserved; no script category substituted. |
| Category D, degree classes | `D`, `D_i`, `D^b` | 051–060; distinguish superscript b from a prime. |
| Heavy/double-stroked coefficient letters | `\mathbf Q`, `\mathbf Z`, `\mathbf F`, `\mathbf N` | Consistent transcription of handwritten coefficient alphabets; subscripts and overbars retained. |
| Multiplicative group letter | `\mathbf G_m` | 079, 084. |
| Derived R | `\mathbf R` | 060, 062 and first RΓ on 067; second R!Γ on 067 remains `\unsure{R\|\mathbf{R}}_!\Gamma_X` where the weight of the stroke is uncertain. |
| Hyper-Ext / hypercohomology capitals | `\mathbb E\mathrm{xt}`, `\mathbb H`, with explicit alternatives to plain capitals | 062–063; not silently harmonized with ordinary `\mathrm{Ext}^1`. |
| Correspondence/enveloping-algebra script | `\unsure{\mathcal U^i\|\mathcal W^i}` and corresponding indexed variants | 056–057; the repeated uncertain form is kept consistently unresolved. |
| Lie algebra g | `\mathfrak g` or `\unsure{\mathfrak g_\ell\|g_\ell}` | 057, 059, 071: Gothic appearance checked against the actual occurrence. |
| Sheaf Hom, structure sheaf | `\mathcal Hom`, `\mathcal O` | 084, 086, 094; script H/O distinguished from plain cohomology H. |
| Script category A | `\mathcal A` | 090, handwritten correction in the categorical setup. |
| Greek Γ | `\Gamma` | 060, 062, 064, 067, 086, 089; not substituted for a script T. |
| T for Tate constructions | `T_\ell`, `T_{\mathrm{motif}}`, `T_{\mathrm{mot}}`, `T_{\unsure{\bullet\|\ell}}` | 074–075 and later; the written motif/mot abbreviation difference and dot/subscript doubt are retained. |
| Weight rho, fundamental-group pi | `\rho`, `\pi` | 051, 054, 073, 086–094 and 055–080; rho is not a Roman p. |
| Ell and numeral one | `\ell`, `1` | Coefficients, torsion and indices checked separately; doubtful digits remain marked. |
| Other Greek lower-case letters | `\alpha`, `\beta`, `\delta`, `\eta`, `\lambda`, `\nu`, `\sigma` | As located in the concordance; unresolved i/alpha and eta remain in `\unsure`. |
| Greek Phi and chi | `\Phi`, `\chi` | Φ of forms at 086–089 is distinct from the underlined Euler class χ at 092. |
| Typed phi and handwritten phi | `\phi` (072), `\varphi` (091) | Deliberate shape distinction between the typescript and handwritten formal-series variable. |
| Greek upper-case letters | `\Sigma`, `\Lambda` | Σ notation 053–054; Λ logarithmic-derivative map 091–092. |
| Bars, hats, checks | `\bar{…}`, `\widehat{…}`, `\check{…}` | Geometric base extension, profinite Z and dual coefficients remain separate; uncertain bar placement is marked. |
| Plain dash versus arrow | `\mathbin{-}` / `\arrow[…,dash]` versus `\longrightarrow` / `\arrow[…]` | Especially 063, 076, 079, 093; no arrowhead added by mathematical inference. |
| Isomorphism/equality and vertical equality | `\simeq`, `=`, `\Vert` | The vertical equality on 071 is drawn with `\Vert`; uncertain isomorphism signs remain marked. |
| Inequalities, bounds, signs | `\le`, `\ge`, `<`, `>`, `+`, `-` | Kept as visible, including the weight +1 on 074, Q(ρ) on 087 and positive exponent in the product on 091. |
| Roman operators and labels | `\mathrm{Ob}`, `\mathrm{cl}`, `\mathrm{Gr}`, `\mathrm{Spec}`, `\mathrm{End}`, `\mathrm{Hom}` | Typeset labels, not expansions of prose abbreviations. |
| Label in comparison diagram | `(b)` on 077; `\unsure{(D)\|(b)}` on 079 | The later letter is not forced to agree with the clear earlier label. |
| ct / lct and written-out qualification | `ct`, `\unsure{ct\|et}`, `\unsure{lct\|ct}`, `\unsure{localement tordu\|constant tordu}` | 073–074, 093, 095: preserve the observed abbreviated forms; expansion is only in the list below. |
| Author number versus archive foliation | `\mspage{…}` versus `% archive foliation: …` | Author numbers 13–18 occur at 053, 056, 060, 074, 086, 090; archive pencil numbers never become author numbers. |

'''
tail=r'''# Abbreviations

Expansions below are editorial and tentative; none has been inserted into the transcription. A terminal period sometimes belongs to the sentence rather than the abbreviation, and that ambiguity is left in the source. Ordinary sentence-final words from the mechanical abbreviation concordance are not included here.

| Written form | Tentative expansion (only here) | Representative scans |
|---|---|---|
| Ob | objets | 051–055 |
| cl | classe | 051, 053, 092–094 |
| Gr / gr | gradué / gradué associé | 051, 058 |
| dim | dimension | throughout |
| liss | lisse | 051 |
| conn. | connexe | 051 |
| gén. | général / générale | 051 |
| i.e. | id est | 052 onward |
| alg. / Alg. | algébrique; in “alg. clos”, algébriquement | 052, 054, 056, 064–065, 086, 091 |
| faisc. | faisceau(x) | 053 |
| isom. | isomorphe(s) / isomorphisme | 053 |
| filtr. | filtration | 053 |
| val. abs. | valeur(s) absolue(s) | 053 |
| N.B. / NB. | nota bene | 054, 057, 062, 065, 071, 075, 087 |
| pr. | probably preuve in the marginal “pr. du th.”; propre in support contexts | 054, 067 |
| th. / thm | théorème | 054, 067 |
| ds | dans | 056 |
| ss / ½ simple (reading uncertain) | semi-simple | 056, 086 |
| cat | catégorie | 059, 060 |
| ab | abélienne | 059, 060 |
| h. | homologique? the cancelled context remains uncertain | 059 |
| qu. cpt / qu. sép. | quasi-compact / quasi-séparé | 060 |
| g. | gauche, in “Dérivé g.” | 062 |
| n° / N° | numéro | 062, 093 |
| t. f. / tf | type fini | 063, 074 |
| M. | motifs? in a heavily revised passage | 064 |
| ess. | essentiellement | 067 |
| duals. | dualisants? retained abbreviated | 067 |
| géo. / géom. | géométriquement | 071, 078 |
| Conj. | conjecture | 071 |
| ct / lct | constant / localement constant, subject to the marked readings | 073, 074, 093, 095 |
| hom | homomorphisme | several pages |
| can | canonique | 065, 071 |
| p.ex. | par exemple | 075, 076, 084 |
| V.A. / VA | variété abélienne | 074, 076 |
| tjrs | toujours | 076 |
| tt | tout | 089 |
| cst | constant | 090 |
| ssi | si et seulement si | 087 |
| pts / pt | points / point | 053, 074, 082 |
| nbs | nombres | 088 |
| aut° | automorphisme | 091 |
| fix | fixe | 076–079 |
| top. | topologique | 077 |
| corr. | correspondances | 078 |
| coh. | cohomologie | 079 |
| triv. | triviale | 079 |
| surj. | surjectif / surjective | 079 |
| équiv. | équivalent | 079 |
| car. | caractéristique; in “pol. car.”, caractéristique | 079, 090–092 |
| cour. | courbe | 084 |
| C. Artin | first initial of the named Artin; not expanded from outside evidence | 084 |
| int. | intérieur | 087 |
| proj. | projectif | 090 |
| irréd. | irréductible | 090 |
| coeff. | coefficient(s) | 090 |
| pol. / pol. car. | polynôme(s) / polynôme caractéristique | 091 |
| irr. (alternative only) | irréductibles | 091 |
| séparé alg. (reading uncertain) | séparablement algébrique? no expansion chosen | 091 |
| connaiss. | connaissance | 092 |
| fonct. rat. | fonction(s) rationnelle(s) | 093 |
| mod. | modulo | 093–094 |
| Frob | Frobenius | 054, 094 |
| var. | variable | 096 |

# Legibility and limits

The uncancelled main text is usually readable at the supplied half-page resolution, but the handwriting often reduces word endings to a short stroke. Every image was read directly by the primary reader, in page order, with no OCR and no delegated image reading; every page then received a second visual audit before the context was opened. A doubt marker records a proposed reading, not a guarantee that the alternatives exhaust what the ink could mean.

I trust least the overwritten first-page expansions (051), the completely cancelled drafts (052 and 058), the heavy cancellations at the foot of 055 and 059, the inverted small typescript fragment on 061, the cancelled typescript details on 072, and the tiny slanted margin on 079. Dense exponents and line intersections on 054, 058, 073, 084 and 093 deserve renewed checking against the originals; the low-confidence rows flag the most obstructed passages. The shapes of the early Tate-like symbol, the script U/W, the doubled hyper-Ext capitals, and several abbreviated words remain deliberately unresolved.

The prose spellings, unfinished parentheses, incomplete sentences, numerical weights and signs have not been repaired. Mathematical surprise does not establish a reading error. Drawings and enclosures are TikZ approximations of the observed strokes, not facsimiles; arrows, labels and local relations were checked visually. Archive foliation, paper damage and verso show-through were distinguished from the author's marks. The cover at 096 has no written page count. The source fragments have structural checks, but no successful TeX compilation is claimed: the available executable lacked its document-class/package installation.
'''
target.write_text(heading+'# Doubts by page'+body+'\n\n'+tail,encoding='utf-8')
print('Doubts register rebuilt from audited fragments; notation, confidence and abbreviation sections finalized.')
