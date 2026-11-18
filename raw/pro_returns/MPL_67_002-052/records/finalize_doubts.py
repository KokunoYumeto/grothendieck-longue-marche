from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from save_page import macro_args

ROOT = Path(__file__).resolve().parents[1]
HEADER = r'''# Notation table

This table records the readings compared against the images before the transcription was frozen. A shared mathematical use did not settle an uncertain glyph: the alternatives remain in the page files. Page references below are scan numbers in cote 67.

| Sign or usage | LaTeX in the transcription | Scans and comparison |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes | Throughout; visible guillemets are retained only where drawn. |
| Surface and marked complex | `$X$, $K$, $S$` | 003–007; inclusions, complements and subscripts remain as written. |
| Cut surface | `$\widetilde X$` | 003–004; overhead wavy stroke. |
| Distinguished boundary | `$\partial'\widetilde X$` | 003–004; prime after the boundary sign. |
| Modified surface | `$X^*$`, `$\widetilde X^*$` | 003–004; the doubtful star/circle on 004 is marked. |
| Collar and curve labels | `$\Gamma_i$`, `$T_i$`, `$\varepsilon_i$` | 003–004; the angular Gamma and crossbar T were compared. |
| Face and component notation | `$f\in F$`, `$g(f)$`, `$\nu(f)$` | 007; overwritten indices remain marked. |
| Connectivity and count letters | `$\lambda$`, `$\mu$`, `$N$` | 007; cancellation of the mu note retained. |
| Tall pi-shaped forms | `\unsure{\Pi\|\pi}` | 007, 011, 013, 026, 048–049; case remains uncertain. Compared with the clear tall Pi forms on 051. The vertical bar here denotes alternatives, not a mathematical operation. |
| Smaller curved pi forms | `$\pi$` | Projection on 006 and the numerical pi in the exponential formulas on 026, 030; checked separately against their ink. |
| Circled numbers and primes | `\textcircled{...}` | 009, 011, 013; ambiguous circled 3-prime/3 on 011 and 7-prime on 013 remain marked. |
| Typewritten numeral with I-shaped serifs | `1` in numerical fields | 008; retained as a numeral where the complete printed number identifies the glyph. |
| Double-struck scalar/group letters | `$\mathbb U$, $\mathbb Z$, $\mathbb C$, $\mathbb R$` | 009 onward; unresolved bold/double-struck R on 004 remains explicit. |
| Compact torus and torsor | `$T$, $\Delta$, $\mathbb U$` | 009, 011–013, 025; the separate letters and superscripts were retained. |
| Projective-group abbreviation | `$\mathrm{GP}(1)_{\mathbb C}$` | 011, 013; GP is the written order. |
| Typewritten underlined scalar letters | `$\underline C$, $\underline R$` | 016–021; the visible underlining is retained. |
| Typewritten multiplicative exponent | `\unsure{\mathrm{x}\|*}+` | 016; x-shaped typewriter glyph retained first, with star as alternative. |
| Marked/bordered moduli letters | `$\widetilde M$, $\widetilde{MB}$` | 016–021; only visible tildes are supplied. |
| Filled surface, right-hand wedge | `$X^{\wedge}$` | 018–020; wedge at upper right. |
| Compactified surface, overhead hat | `$\widehat X$` | 027; hat above the X. |
| Small o-shaped superscript | `$D_i^o$, $\widetilde{MB}^o$` | 017–018; position and shape retained. |
| Radius and multiplier letters | `$r_i$, $\rho_i$, $\lambda_i$, $\ell_i$` | 016–021; endpoints and primes checked separately. |
| Completed radius torsor | `$R_i^{\wedge}$` | 019. |
| Three-bar E | `$\mathbb E^1_{\mathbb C}$` | 027, 030, 045; all three horizontal strokes checked. |
| Exclamation exponent | `$E_a^!$` | 028; vertical stroke and dot visible. |
| Hatted group letters | `$\widehat H$`, or the locally marked alternative | 031–032; overwritten hat/tilde is recorded in place. |
| Orientation cover and involution | `$X^{or}$`, `$\sigma$` | 027–046; the superscript letters and prime on `$X'$` are retained independently. |
| Metric classes and metric space | `$Q_X$, $Q_{X,H}$`, `$R(X)$` | 031–039; Q and R have different visible strokes and remain as written. |
| Positive Hermitian forms | `$\operatorname{Herm}^{*+}(V)$` | 031–038; star-plus and order of superscripts retained. |
| Subgroup signs | `$H^+$`, `$N^-$` | 031–038; plus/minus signs retained, including the minus in the normalizer notation. |
| Circle and scalar field letters | `$C$`, `$\mathbb C$` | 033–038; plain circle-label C kept where written; unresolved C/E on 035 is marked. |
| Script doubled surface | `$\mathcal X$` | 042–044, 051; the flourished X is retained. |
| Half-plane letter | `$\mathbb H$`, `$\overline{\mathbb H}$`, or the local plain H | 043–045; visible doubled stem, bars and later plain H were checked individually. |
| Own page-number strokes | `\mspage{\unsure{1'\|19}}`, `\mspage{\unsure{2'\|21}}` | 045–046; alternatives remain because the small added stroke is ambiguous. Archive foliation stays in comments. |
| Normal propagator and cyclotomic twist | `$N$`, `$\widehat{\mathbb Z}(1)$` | 048; wide hat and parenthesized 1 retained. |
| Flourished Teichmüller T | `$\mathcal T$` | 050–051; compared with the explicit alphabet trial and groupoid/group table on 051. |
| Plain and double-stem T | `$T$`, `\unsure{\mathbb T\|T}`, `\unsure{\mathbb T\|\mathcal T}` | 050–051; the uncertain additional stem remains marked, including the lower sequence on 051. |
| Combined plus/exclamation exponent | `$\mathcal T_{0,4}^{+!}$`, `$T_{g,\nu}^{+!}$` | 050–051; plus and separately dotted exclamation stroke checked. |
| Script/Gothic trials and S | `$\mathfrak S$`, `$\widetilde{\mathfrak S}$`, `\unsure{\mathcal T\|\mathfrak T}` | 051; letter trials are reproduced in TikZ, and the local uncertainty remains explicit. |
| Loop generators | `$\ell_0$, $\ell_1$, $\ell_2$, $\ell_3$, $\ell_\infty$` and primes | 051; the equality has an unprimed left member and primed right member. The first index in the last relation remains uncertain. |

# Doubt records

The line numbers refer to the individual `.tex` page files, so they identify the precise occurrence even when a drawing occupies many source lines. Every `\unsure` and `\illegible` occurrence is indexed below, including nested occurrences. “Medium” means a defensible but unresolved reading after enlargement; “low” identifies particularly compromised ink or an unreadable word. No probability estimate is implied. A blank alternative means that no second reading was supported by the image.

| Cote | Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
'''

ABBREVIATIONS = r'''
# Abbreviations encountered

Expansions in this section are editorial suggestions only. They have not been inserted into the transcription; number and grammatical form depend on the occurrence. A question mark marks an unresolved expansion.

| Written form | Suggested expansion | Scans / remarks |
|---|---|---|
| alg. | algèbre / algébrique | 037, 049 |
| anti. | anti-automorphismes? | 042, cancelled and uncertain |
| antipod. | antipodique | 028 |
| ass. | associé(e) | 032 |
| aut., autom. | automorphisme(s) | 013, 029–046 |
| can. | canonique | 043, 051 |
| car. | caractéristique | 049 |
| cl. | classes | 049, alternative reading to él. |
| coll. | collier(s) | 005 |
| comp. | composante(s), or compact(e) in the compactness passages | 003, 032–046 |
| compl. | complémentaire(s) | 003 |
| conj. | conjugaison / conjugué(e) | 028, 049 |
| conn. | connexe(s) | 005 |
| const., cte. | constante | 005, 032, 043 |
| corr. | correspondant(e) | 033, 037 |
| cpt, cpte, cptes | compact, compacte, compactes | 009–044 |
| cxe | complexe | 011, uncertain reading |
| déf. pos. | défini(e) positif / positive | 030, 032 |
| Dém. | Démonstration | 035 |
| dim. | dimension | 013, 033, 038 |
| él. | élément(s) | 013, 049 |
| ell. | elliptique | 009 |
| ens, ens. | ensemble | 011, 032–044 |
| ét. | étale | 048, uncertain reading |
| évt, évt. | éventuellement | 003, 050 |
| ext. | extérieur(e), extérieur(ement) | 034, 036, 048–049; check the local action/conjugation usage |
| fact. | facteur | 013 |
| géod. | géodésique | 009, 011 |
| géom. | géométrique | 028, 049 |
| gpe, grpe, ss-gpe | groupe, sous-groupe | 009–038 |
| hol. | holomorphe(s) | 027–045 |
| hom. | homomorphisme(s), homothétie? | 011, 048; the 011 reading is uncertain |
| homeo. | homéomorphisme(s) | 005 |
| i.e. | id est | Several handwritten sheets and the letter |
| ind. | indétermination? | 011, uncertain phrase |
| indép. | indépendant | 048, cancelled |
| inv. | invariant(e)(s) | 035, 038, 046 |
| invol. | involution | 031 |
| isom. | isomorphe / isomorphisme | 004, 027–049 |
| m.l. tr. | modulo les translations? | 011; letters themselves remain uncertain |
| mod. | modulo | 029–043 |
| métr. | métrique(s) | 039 |
| NB | nota bene | Throughout |
| néc. | nécessairement | 005, 040, 043, 045 |
| or. | orientation / orienté | 013 and superscripts |
| orth. | orthogonal(e)(s) | 043 |
| p. ex., P.ex. | par exemple | 030, 040 |
| p.r. | par rapport | 042–043 |
| pant. | pants | 020 |
| plgt | plongement | 011, uncertain reading |
| Prop. | Proposition | 037 |
| pts, pts. | points | Throughout |
| rect. | rectiligne? | 004 |
| rectif. | rectifiable | 003, uncertain reading |
| rel. | relatif / relativement | 038 |
| resp. | respectivement | 027–045 |
| rev. | revêtement | 027–046 |
| rg | rang | 009–013 |
| riem. | riemannienne(s) | 036 |
| s. | sous-? | 003, inspect the local phrase |
| sph. | sphérique | 039 |
| ss., Ss. | sous- / sans, according to the written phrase | 011, 013, 045 |
| str. | structure | 032, 038–039 |
| suppl. | supplémentaire(s) | 031 |
| surf. | surface | 045 |
| t.f. | type fini | 049 |
| top. | topologique | 005 |
| tt, tte, ttes | tout, toute, toutes | Throughout handwritten notes |
| unif. | uniformisation | 027 |
| val. | valeurs | 013 |
| Vect. | vectoriel(le) | 013 |
| CNS | condition nécessaire et suffisante | 013, uncertain reading of the abbreviation |
| Réf., Téléph., Expo., Elect. | référence, téléphone, exposition, électrique(s) | 008, printed catalogue |
| Nrs / Frs | nouveaux francs / francs? | 008, uncertain printed abbreviation |
| M., Mr., UNIV. | Monsieur, Mister, University | Printed letter/envelope matter, 010, 013–014 |
| MD | Deligne–Mumford? | 049; the letters are retained in their written order |
| SL, GL, GP | special linear, general linear, groupe projectif | Group labels retained literally |
| OPS | operational mark / restart cue? | 042; no secure expansion proposed |

# Legibility and limits of the reading

The printed letter and most of the uniformization sequence are legible at enlargement. The rapidly written surgery sheets, overwritten equivalence lists, sideways marginal additions, and the working diagrams on the last sheet carry appreciably more uncertainty. Scan 006 combines faint pencil, dark retracing, folds and crossing lines; scans 009, 011 and 013 contain heavily struck or overwritten words; scans 019–020 have dense additions to a typed letter; scans 033–039 combine corrections with long marginal notes. The doubtful sign on scan 040, the set-difference order on scan 045, and the incomplete quotient and indices on scan 051 were preserved from the ink rather than adjusted to a mathematical expectation.

I trust least the short cancelled words whose letter bodies are covered, the small indices inside overwritten formulas, and the case/alphabet of a few broad handwritten letters. Rotating and enlarging these regions improved access but did not resolve every stroke. Remaining uncertainty is recorded locally and in the table above. The reconstructed drawings retain shapes, component positions and labels; line curvature and distances are approximations to freehand strokes. The postal ornament on scan 014 is marked as a crop candidate after its TikZ approximation, as permitted by the task. The scan 051 character-built logos were transcribed by individual printed character positions, with no OCR.

All 46 supplied whole-page images and their two halves were read in the original ordered transcription stream, and all 46 pages received a subsequent root image audit. The final comparison used the images again for recurring pi/Pi, T alphabets, primes, exclamation strokes and overwritten notations. A second audit and the frozen hashes document this work; they do not certify the absence of residual reading errors. The transcription contains the original languages and spellings. This doubts file supplies English apparatus, and the separate research notes may discuss reading questions without changing the frozen page files.
'''

def alternatives(s):
    depth = 0
    for i, c in enumerate(s):
        escaped = i > 0 and s[i-1] == '\\'
        if c == '{' and not escaped: depth += 1
        elif c == '}' and not escaped: depth -= 1
        elif c == '|' and depth == 0 and not escaped:
            return s[:i], s[i+1:]
    return s, ''

def cell(s):
    return s.replace('|', '&#124;').replace('\n', ' ').replace('`', '&#96;')

rows = []
for p in sorted((ROOT/'pages').glob('*.tex')):
    n = int(p.stem[-3:])
    source = p.read_text()
    entries = [(line, 'unsure', arg) for line, arg in macro_args(source, 'unsure')]
    entries += [(line, 'illegible', arg) for line, arg in macro_args(source, 'illegible')]
    for line, kind, arg in sorted(entries, key=lambda x: x[0]):
        if kind == 'illegible':
            reading, alt, confidence = f'illegible: {arg} word(s)', 'No secure reading', 'low'
        else:
            reading, alt = alternatives(arg)
            confidence = 'medium'
            # Editorial low-confidence judgments from the root image audit.
            if (n in {6, 9, 11, 13} and any(x in arg for x in ('illegible', 'm.l.', 'ind.', 'bicentres', 'Z_{', 'TR', 'Fix'))):
                confidence = 'low'
            if n == 51 and (arg == 'm' or any(x in arg for x in ('\\ell_1', '\\mathbb Z\\times'))):
                confidence = 'low'
        rows.append('| 67 | '+f'{n:03d}'+' | TeX line '+str(line)+' | '+cell(reading)+' | '+cell(alt)+' | '+confidence+' |')

(ROOT/'MPL_67_002-052_doubts.md').write_text(HEADER+'\n'.join(rows)+'\n'+ABBREVIATIONS)
print(f'Rebuilt {len(rows)} local doubt records from the current page files.')
