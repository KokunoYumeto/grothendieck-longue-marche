"""Final pre-context notation reconciliation, based only on the scanned ink.

Run once by the sole visual reader. This is a work record, not a normalizer.
"""
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
log = root / 'progress.log'
assert 'transcription frozen' not in log.read_text(), 'The transcription is frozen.'

p = root / 'pages/MPL_136_002-046_136_scan007.tex'
s = p.read_text()
assert s.count('X_*') == 8, s.count('X_*')
p.write_text(s.replace('X_*', r'\mathcal X_*'))

p = root / 'pages/MPL_136_002-046_136_scan026.tex'
s = p.read_text()
assert r'\mathbf Z' in s and r'\mathbf N' in s
p.write_text(s.replace(r'\mathbf Z', r'\mathbb Z').replace(r'\mathbf N', r'\mathbb N'))

p = root / 'pages/MPL_136_002-046_136_scan035.tex'
s = p.read_text()
assert r'\unsure{v_p|\nu_p}' in s
s = s.replace(r'\unsure{v_p|\nu_p}', r'\unsure{\nu_p|v_p}')
s = s.replace(r'\unsure{v_p(n!)|\nu_p(n!)}', r'\unsure{\nu_p(n!)|v_p(n!)}')
p.write_text(s)

p = root / 'MPL_136_002-046_doubts.md'
s = p.read_text()
start = s.index('This table is maintained')
end = s.index('## Doubt register')
table = r'''This table was maintained from the first page and expanded during the final, pre-context comparison. It records visible conventions, not a license to regularize ambiguous ink. The same recurring form has one preferred encoding; local ambiguity remains marked. The second audit and the final comparison are chronological work records: where an earlier doubt row gives a different reading, the later audit/reconciliation row supersedes it, and the page file contains the final reading.

| Manuscript form | LaTeX | Reading rule and comparison |
|---|---|---|
| DR; DRS; DRpd | `\mathrm{DR}`, `\mathrm{DRS}`, `\mathrm{DRpd}` in formulas | Keep each suffix and the visible spacing; no expansion. |
| Single / double cohomological dot | `\bullet` / `\bullet\bullet` | Preserve single and bigraded notation, including the author's changes. |
| Star; prime; exclamation | `*`, `'`, `^!` | Read each stroke individually. The reindexing mark on 010 and `Lie'` on typed 036 are primes; the unclear stars/primes on 037/041 remain marked. No clear exclamation-mark exponent has been established in this package; prose exclamation marks and factorials are distinct. |
| Script semi-simplicial object | `\mathcal X_*`, `\mathcal X_\bullet` | Looping X on 007 compared with 009–018; 007 corrected before freezing. Plain topological `X`, coordinates `X_i`, and `S_*(X)` retain their own forms. |
| Script graded-module letters / categories | `\mathcal M`, `\mathcal N`, `\mathcal M_N` | Distinguish from plain modules `M,N` and thresholds `N`. Heavily retraced N on 037 is separately encoded `\mathbf N` and not interpreted as the natural numbers. |
| Double-stroke number letters | `\mathbb Z`, `\mathbb Q`, `\mathbb R`, `\mathbb C`, `\mathbb N`, `\mathbb F_p` | The inserted double-stroke Z and N on 026 have been reconciled with the other pages. |
| Capital Greek auxiliary modules | `\Phi`, `\Psi` | Keep the two letters distinct in 008–009 and 017; exterior powers use `\bigwedge`, not capital lambda as a name. |
| Truncation / shadow / right-adjoint letters | `\tau_N`, `\omega_N`, `\pi_N`, `\varphi_N`, `\varphi_{0N}` | No interchange of functors. Looped phi on 027 is compared with 037/041; two compressed 027 occurrences keep rho as a marked alternative. |
| Coefficient families | `\xi_i`, `\xi_s`, `\eta_s` | Xi is the preferred reading across 024 and 027–034/045; the first two cramped signs on 024 retain zeta as an alternative. Eta on 043 is distinct. |
| Carry variables | `\rho_\alpha`, `\sigma_\alpha` | Rho in the cancelled digit calculation on 033 is not changed to the adjoint's phi. |
| Valuation sign | `\unsure{\nu_p|v_p}` | The hooked right stroke on 035 and 043 supports a common preferred nu; Latin v remains an explicit alternative. This final comparison supersedes 035's earlier v-first audit entry. |
| Unit coefficients and prime | `\nu_r`, `\nu'_r` | Distinct role from the valuation; the same hooked letter is retained on 043–045, with its actual subscript and prime. |
| Divided-power monomial / p-typical generator | `T^{(n)}`, `T_r`, `T^{(p^r)}` | Parenthesized powers, ordinary powers, and subscripts are not interchangeable. |
| Factorial after a power | `p^r!`, `p^{r+1}!` | Preserve the written grouping, without adding parentheses from mathematical expectation. |
| Binomial coefficients | `c_{ij}`, `c_{\ell,k}`, etc. | Preserve the displayed order and repeated indices, even in the anomalous coefficients on 028 and 032. |
| Isomorphism and comparison marks | `\simeq`, `\sim`, arrow labels, `\subset` | Arrowheads, hooks, dashes, and inclusion directions are local visual readings. The right-pointing diagonal-inclusion arrow on 008 is retained. |
| Equality-like shorthand in prose | `$=$` | The two short strokes, probably shorthand for *même*, remain a sign on 007, 011, 014, 016, 017; they are not expanded in the transcription. |
| Double quotation marks | two backticks and two apostrophes | Use guillemets only if drawn. Ditto signs within calculations, including 033, are separate marks. |
| Underline / double underline | `\uline{...}` / `\uuline{...}` | Visible emphasis is preserved, including the double underline of `La` on 017 and the restored underline of `égaux` on 024. |
| Bars, hats, tildes, natural sign | `\overline`, `\hat`, `\tilde`, `\natural` where present | Do not supply a decoration from the object's usual name. The ambiguous shorthand `\overline m` on 021 remains marked; typed `A^\natural` on 036 is distinct. |
| Typed script and underlined letters | `\mathcal E`, `\uline{E}`, `\uline{R}`, `\uline{O}`, `\uline{F}` | Keep calligraphic E, ordinary E, and the underlined sheaf letters distinct on 036, 038, 046. These are reused printed leaves, not a single notation system with the handwritten argument. |
| Fractional abbreviation | `$\frac12$` followed by `simpl.`, `simplicial`, etc. | Preserve the fraction and the actual ending; do not replace it by “semi-”. |
| Unknown symbol in mathematics | `\unsure{best reading}` | No formula/diagram symbol is represented by `\illegible`. |

'''
s = s[:start] + table + s[end:]
s += r'''

## Final notation-comparison additions

| File | Scan | Approximate line / position | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|---|
| 136 | 007 | lower half, eight occurrences | `\mathcal X_*` | Visible looped X agrees with 009–018; replaces plain X in the earlier reading. Topological X and coordinates are unchanged. | high |
| 136 | 024 | coefficient definition | `\xi_i` | Zeta remains a local alternative for the first two compressed signs; repeated family checked against 027–034. | medium |
| 136 | 026 | inserted quantified line | `\mathbb Z`, `\mathbb N` | Double-stroke number letters checked against the ink; replaces bold encoding. | high |
| 136 | 027 | first two adjoint formulas | `\varphi_N`, `\varphi_{0N}` | Rho remains an alternative at these two compressed occurrences; the loop and descending stroke are compared with 037/041. | medium |
| 136 | 035, 043 | valuation formulas | `\nu_p` | Latin v remains possible. Common preferred reading follows the hooked right stroke on both leaves, not the expected notation for a valuation. Supersedes 035's earlier v-first entry. | medium |

## Abbreviations encountered

The expansions below are editorial aids only. They have not been inserted into the transcription; punctuation and endings vary in the manuscript.

| Written abbreviation / shorthand | Probable expansion or meaning |
|---|---|
| alg.; algéb. | algébrique / algèbre, according to syntax |
| anti comm.; anticomm. | anticommutatif / anticommutative |
| ass.; unit.; altern. | associatif; unitaire; alterné |
| aug.; augm. | augmentation / augmenté |
| can.; canoniq. | canonique / canoniquement |
| car. | caractéristique |
| cat.; s-cat. | catégorie; sous-catégorie |
| cf. | confer, “compare” |
| chif | chiffre(s), specifically the sum of base-p digits in 035 |
| coeff | coefficient(s) |
| coh.; cohom. | cohomologie / cohomologique |
| comm.; com. | commutatif |
| comp. | compatible(s) |
| cond.; condts | condition(s) |
| cqfd | ce qu'il fallait démontrer |
| Dém | démonstration |
| dfn | définition (typed mathematical notation) |
| diff. | différentiel / différentielle |
| DR; DRS; DRpd | De Rham; De Rham–Sullivan; De Rham à puissances divisées |
| ens.; Ens | ensemble(s) |
| esp.; top. | espace(s); topologique(s) |
| ext. | extérieur |
| faisc. | faisceau(x) |
| fonct. | fonctoriel / fonctoriellement |
| gr. | groupe / gradué, according to syntax |
| hom. | homotopie / homomorphisme, according to syntax |
| i.e. | id est |
| IHES | Institut des Hautes Études Scientifiques |
| isom.; iso. | isomorphisme / isomorphe |
| mb. | membre |
| mod. | module / modulo, according to syntax |
| mult. | multiplicatif / multiplicative |
| nb; nbs | nombre; nombres |
| néc. | nécessairement |
| op.; op. coh. | opération(s); opérations cohomologiques |
| OPS | on peut supposer |
| p.d.; pd; puiss. div. | puissances divisées |
| p.ex. | par exemple |
| Pb | problème |
| prop.; Prop | proposition |
| pt | point |
| q. iso.; qu-isom | quasi-isomorphe / quasi-isomorphisme |
| rés. | résolution |
| resp. | respectivement |
| Rmq | remarque |
| simpl.; simplt | simplicial / simplement, according to syntax |
| t.f. | type fini |
| th.; ths; Thm | théorème; théorèmes |
| tjrs | toujours |
| ttes | toutes |
| two parallel strokes `=` within prose | probably même; left as a sign in the transcription |
| U.S.T.L. | Université des Sciences et Techniques du Languedoc, as in the reused administrative material |
| S.N.C.F. | Société Nationale des Chemins de fer Français |

## Legibility and limits

Most main text is recoverable, but the fast running hand frequently reduces word endings, accents and linking words to a stroke. The least secure passages are the densely cancelled introductory clauses on 003–007, the tiny insertion about categories of sheaves on 016, retraced indices and coefficients in 027–034, the cancelled and rotated Cayley-graph material on 037, and the right-edge formulas on 041/043. The reused typed sheets are easier to read, although their print is faint and some accents, names and isolated digits remain doubtful.

All 44 whole pages and their supplied halves were viewed by the same reader in sequence, then every page received a second image-based audit. Enlarged crops and rotations were used for difficult writing; no OCR was used. This procedure reduces omissions and inconsistent signs, but it does not make the difficult readings certain. In particular, a structurally valid TeX fragment and an inventory marked “yes” attest to the recorded transcription process, not to a guarantee that every faint stroke has been identified correctly. Local doubt marks and this register are part of the deliverable, and the manuscript's mathematical anomalies were left in place.
'''
p.write_text(s)
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
    f.write(f'notation reconciliation completed {now}; sole visual reader; 007 script X, 026 double-stroke number letters, 035/043 common nu-first valuation alternative; recurring alphabets, stars/primes, coefficients, quotation marks and prose shorthand compared; context still sealed\n')
print(now)
