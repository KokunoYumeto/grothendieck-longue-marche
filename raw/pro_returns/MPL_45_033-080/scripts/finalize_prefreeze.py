from pathlib import Path
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
assert 'transcription frozen ' not in (ROOT / 'progress.log').read_text()

notation = r'''# Doubts and notation — MPL_45_033-080

## Package notation table

The table records visual distinctions, not mathematical corrections. The same reader compared recurring forms during the second audit and the final comparison before freezing; individual unresolved occurrences remain marked in place. A difference that is visible in the ink has not been regularized merely because the mathematical role is similar.

| Recurring ink | LaTeX treatment | Compared occurrences / caution |
|---|---|---|
| Capital triangular delta; lower-case delta | `\Delta`, `\delta` | Typed rays on 033 and coproduct on 069; case retained. |
| Ordinary Latin capitals and lower-case letters | Ordinary math letters | E/F, G/H, x/X, u/v, k/K remain distinct; 064, 068, 076, 078, 079 have local doubts. |
| Doubled Z, R, C, K, Q | `\mathbb` | Compared 038, 045, 047, 053, 055, 057, 064, 066, 068, 070, 076–079; changed earlier inconsistent bold/plain rendering to the doubled alphabet. Plain typed N in 071 is retained. |
| Overwritten G in G_m | Ordinary G or `\mathbf G`, marked | The retraced G on 064 and the less emphatic G on 079 do not justify a uniform confident alphabet; local doubt retained. |
| Tall Gothic g, h, u | `\mathfrak` | 038, 040, 042; distinguished from capitals G, H. The last normalizer label on 042 remains script L versus Gothic b. |
| Script F, A, B, U in sheaf typescript | `\mathcal` | 046/048, including supplied handwritten script letters; the script block letter on 052 is U/A uncertain. |
| Script quotient-space letters C, D, C′ | `\mathcal C`, `\mathcal D` | 049; no replacement by modern notation. |
| Gamma versus H | `\Gamma`, `H`, with `\unsure` where overwritten | 045–059; repeated heavily retraced H-like objects on 047 remain doubtful. |
| Phi versus phi / varphi | `\Phi`, `\phi`, `\varphi` | Capital form symbols on 050–060; map labels on 045/048; visibly oval-with-stroke empty-set notation on 046/049 retained as phi. |
| Rho, epsilon, xi | `\rho`, `\epsilon` or `\varepsilon`, `\xi` | Twisting class rho on 045–059 differs from xi; the small printed permutation sign on 067/069 is consistently `\unsure{\rho\|\varepsilon}`. |
| Rank epsilon | `\epsilon` | 070, 076, 077; distinguished from the capital E of forms. |
| Corner action pointing one way or the other | `\lrcorner`, `\llcorner` | 035–036 and 067–069 compared: the two visibly opposite corner orientations on 067 are preserved. |
| Star product, dual star, graded dual star | `*`, `^*`, `^{*\mathrm{gr}}` | Position retained; the absent dual star at the first membership in 069 is not supplied. |
| Transpose t | `{}^{\mathrm t}` | 067; not read as a prime or exclamation. |
| Prime, double prime, and exclamation | `'`, `''`, `!` | Each visible prime checked separately, especially 045–060 and 066–079; no secure exclamation-mark exponent was identified in this package. The exclamations on 068 are punctuation. |
| Round orthogonal exponent | `^{\mathrm o}`, `^{\mathrm{oo}}` | 050–056; neither zero nor a perpendicular sign is substituted. |
| Bar, hat, and check | `\bar`, `\hat`, `\check` | Barred xi and N on 051/053; barred E on 070; hats on completions in 079; checks in 068. A missing check is not supplied. |
| Sigma with raised or lowered 2 | `\Sigma^2`, `\Sigma_2`, locally doubtful | 068; the disputed third object is raised 2 first after comparison, without changing the surrounding sequence. |
| F with raised or lowered filtration index | `F^2`, `F_1`, etc., with doubts | 076–079; the raised F/Gamma on 076, repeated 1-like denominator on 077, and k-like subscript on 078 remain visibly different. |
| Arrows, plain shafts, inclusions | `\arrow`, `dash` / `no head`, `\subset` | 042, 045–059, 062–079; arrowheads checked independently of expected exactness. Two-ended strokes retained only where two tips are visible. |
| Wavy relation or arrow | `\sim`, `\rightsquigarrow` | 066 and 068; ambiguous 066 relation marked rather than replaced by a straight arrow. |
| Vertical paired strokes | `equal` or phantom label with `\Vert` / `\wr` doubt | 079; no added shaft under the Pic expression. |
| Single / double underlining | `\uline`, `\uuline`; `\underline` within mathematics | Underlined words and mathematical symbols distinguished; double underlining on 055 and 078 retained. |
| Straight double quotation marks | Two backticks and two apostrophes | One convention throughout; guillemets would be used only for drawn guillemets. |
| Circled labels and words | `\textcircled`, or an oval in TikZ | 047, 049, 051, 053, 055, 059, 076, 078; circles are not silently reduced to parentheses. |
| Boxes, braces, curved insertion pointers | TikZ, tikz-cd, or array braces | The geometry is an approximation to the visible drawing; no missing mathematical objects are supplied to complete a shape. |
| Double square interval brackets | `\lbrack\!\lbrack` and `\rbrack\!\rbrack` | 067, 069, 071; printed endpoints retained even where inconsistent. |
| Aff and hyperalgebra U | `\operatorname{Aff}_A(G)`, `U_A(G)` | 034–036; original notation retained. |
| Underlined Aut / Isom / O | `\underline` on the written symbol | 038–059 and 039/041; not replaced by a different alphabet or a modern functor notation. |
| Tangent abbreviation tg | `\operatorname{tg}` | 033; not modernized to tan. |
| Superscript o / os in numbered references | `n$^{\mathrm{o}}$`, `n$^{\mathrm{os}}$` or visible n° | Case and punctuation retained. The faint pencilled 3 on 071 is an insertion, not a blank. |
| Blank typescript formula or reference slots | `\quad` / spacing | 039, 041, 069; no absent relation, operation, or reference number supplied. |
| Main pagination versus isolated pencil numerals | `\mspage` versus `\margin` | Printed pagination and its dashes retained; isolated pencil numbers are not attributed to the author. |
| Broken words and unfinished expressions | Partial text/formula retained | Bru--- on 051; incomplete algebra on 066/070/079; no added closing argument or inferred continuation. |

## Doubt table

Approximate lines refer to written/typed lines in the natural reading orientation, not LaTeX source lines. Repeated doubtful forms may share a row; every occurrence remains marked in the page files. Audit additions below record the final preferred reading, not a mathematical emendation.

| File | Scan | Approximate line / position | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|---|
'''

dp = ROOT / 'MPL_45_033-080_doubts.md'
rows = [x for x in dp.read_text().splitlines() if x.startswith('| 45 |')]
out = []
for line in rows:
    line = line.replace('diverses; groupe unitaire; voisines; même; ne sont pas', 'diverses; groupe unitaire; opposées; même; ne sont pas')
    line = line.replace('condition est vérifiée (deleted); dernière condition; est-elle toujours', 'condition est vérifiée (deleted); dernière condition; est-elle tjrs vérifiée')
    line = line.replace('à priori leur différence pour une certaine classe ... valable', 'à priori leur différence par une certaine classe ... nulle')
    line = line.replace('donné par; l’image d’un élément connu', 'donné par; l’image [inserted can] d’un élément connu')
    line = line.replace('G pour G0=GL(2); donc W1=W0 comme', 'G pour G0=GP(2) (GL alternative); donc W1=W0 comme')
    line = line.replace('Σ2\\|Σ²', 'Σ²\\|Σ₂')
    if '| 071 | 20 |' in line:
        line = '| 45 | 071 | 20, Proposition 5 reference | § 5, n° [inserted doubtful 3], prop.8 | Faint pencil 3 visible at enlargement; first pass incorrectly treated the slot as blank | medium |'
    if '| 076 | 18 |' in line:
        line = '| 45 | 076 | 18 | F^2(A) | Gamma^2(A); very small lower bar of the initial letter | medium |'
    if '| 078 | e formula |' in line:
        line = '| 45 | 078 | e formula | F_k(K); K*/k*2 | First subscript k or 1, with k first after enlargement; lower-case denominator differs from K numerator | low |'
    if '| 079 | above F prime(A) |' in line:
        line = '| 45 | 079 | above F prime(A) | paired vertical strokes | Vertical equality or isomorphism sign; no separate shaft visible | low |'
    # Escape alternatives even inside Markdown code spans.
    line = re.sub(r'`([^`]+)`', lambda m: '`' + re.sub(r'(?<!\\)\|', r'\\|', m[1]) + '`', line)
    out.append(line)
out.append('| 45 | 079 | cancelled H^1(K,G_m) | G_m | Bold/retraced G_m; the alphabet is not certain | low |')

abbreviations = r'''

## Abbreviations encountered

Expansions in this section are interpretive aids only; they have not been inserted into the transcription. An unresolved abbreviation is explicitly identified as such. Variants with and without a final point are retained in the page files.

| Written abbreviation / notation | Probable expansion or use | Examples / caveat |
|---|---|---|
| N.B. | nota bene | 033, 049, 053, 055, 057, 062, 070, 076 |
| i.e., ie | id est | 039–041, 047–055, 076–078; some handwritten examples doubtful |
| resp. | respectivement | Reused typescripts 039, 050–060, 071 |
| cf. | confer / compare | 058; also references without point |
| cqfd | ce qu’il fallait démontrer | 039 |
| ssi | si et seulement si | 051, 057; cancelled occurrence retained |
| il f. et s. | il faut et il suffit | 049 |
| Th., Th | théorème | 053, 078 |
| prop. | proposition | 033, 036, 039, 041, 046, 052, 056, 069, 071 |
| cor. | corollaire | 056 |
| Dém | démonstration | 053, cancelled |
| chap. | chapitre | 069 |
| n°, nᵒ, nᵒˢ | numéro, numéros | Original upper/lower case retained |
| éd. | édition | 069 |
| p. ex. | par exemple | 055 |
| tjrs | toujours | 049, 057; preserved as abbreviation |
| tt, tt., tte, ttes | tout, toute, toutes, according to the occurrence | Reduced forms in 042, 051, 059; no expansion in the transcription |
| ens | ensemble | 045–059 |
| élémts | éléments | 057, doubtful ending |
| gr | groupe | 049 and nearby handwritten notes |
| ss-groupe, ss-groupes | sous-groupe, sous-groupes | 049, 051 |
| s. simple | semi-simple, probably | 045; abbreviation itself remains doubtful |
| comm. | commutatif | 034 |
| noeth. | noethérien | 039 |
| alg. / alg | algébrique / algébriquement, by syntax | 078 |
| car., car | caractéristique | 077–078; also other handwritten notes |
| rés, rés. | résiduelle | 076, 078 |
| val. discrète | valuation discrète | 079 |
| non div de 0 | non diviseur de zéro | 076 |
| hom | homomorphisme | 076 |
| isom., isom | isomorphisme / isomorphe | 045–059, 070; inflection not expanded |
| aut., aut | automorphisme | 051, 057 |
| ext. | extérieur | 047 |
| rel. | relatif / relatives | 057, depending on syntax |
| géomᵗ | géométriquement | 049 |
| trivialt | trivialement | 057 |
| égalemt | également | 078, doubtful |
| équival. | équivalentes | 053 |
| max. | maximal | 053 |
| interméd. | intermédiaire | 045, doubtful insertion |
| loc. | localement / local, depending on syntax | 038 |
| immers. | immersion | 038, possible abbreviated reading |
| m. infi. | Unresolved; infi. may abbreviate infinitésimal | 038; do not use as a secure technical phrase |
| Tch | Possibly Tchevalley / Chevalley | 053 footline; unresolved abbreviation |
| Bru--- | Possibly an interrupted proper name beginning Bru | 051; not silently completed to Bruhat |
| D. | Unresolved | 053, unfinished final line |
| qu. | Unresolved; perhaps quadratique(s) | 042; the surrounding phrase is doubtful |
| coh. / coh, | cohomologie | 037; punctuation doubtful |
| inv. | invariant | 070 |
| nb | nombre | 078 |
| dim., codim | dimension, codimension | 050–056, 066 |
| d’aug. | d’augmentation, probably | 066; alternative dim. remains in place |
| sym., symm | symétrique(s) | 061, 066, 068 |
| bil., bilin. | bilinéaire | 068 |
| quadr., quad | quadratique | 068 |
| hyp., hyp | hyperbolique | 062 |
| unim., unimod | unimodulaire | 062 |
| orth | orthogonal, probably | 062; uncertain short label |
| prod. | produit | 064, 068 |
| Aff | fonctions affines / algebra of regular functions in the manuscript’s notation | 034–036; not renamed in the text |
| Aut, ad / Ad, Ext | automorphismes, action/groupe adjoint, automorphismes extérieurs | 038–059; case and underlining retained |
| Lie | algèbre de Lie | 038–042 |
| Isom | isomorphismes | 053; retained even where the displayed target suggests a question |
| Spéc / Spec | spectre; some compound labels uncertain | 062 |
| Bil, Alt, Quad | formes bilinéaires, alternées, quadratiques | 062, 066, 068 |
| Sym, Mod | symétrique; module(s) | 062, 068 |
| Sp | Possibly spécial, in the compound Sp Mod unimod | 062; unresolved expansion |
| dét | déterminant | 064 |
| Im, Ker | image, noyau | 045–059, 068 |
| Cl, Br, Pic | Clifford, Brauer, Picard | 053, 076–079 |
| tg | tangente | 033 |

## Legibility and limits

The reused typescripts are generally much clearer than the handwritten pages, but several have damaged or empty formula slots, faint inserted letters, or overwritten characters. Their apparent mathematical inconsistencies, blank slots, index order, absent primes, repeated equality signs, and unfinished references have been preserved. The diagrams are encoded as editable TikZ/tikz-cd; exact pen geometry and the layering of heavy cancellations can only be approximated.

The least secure readings are the diagonal marginal names and cancelled words on 038; the overwritten group letters and marginal qualifications on 045–059; the compressed difference-class paragraph on 057; the field qualification at the right of 059; the erased or retraced formulas on 062–070; and the superscripts, alphabets, and cancelled cohomology calculations on 079. The five estimated cancelled words on 055 and two on 038 marked `\illegible` remained physically unreadable after enlargement. Doubt marks are substantive: an elegant mathematical interpretation must not be treated as confirmation of these readings. The second audit reduced omissions and inconsistencies but is not a claim of error-free decipherment.
'''
dp.write_text(notation + '\n'.join(out) + abbreviations)

ip = ROOT / 'MPL_45_033-080_inventory.csv'
with ip.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    items = list(reader)

extra = {
    '049.27': [('drawing', 'around bottom question', 'rectangular frame around Question')],
    '049.29': [('drawing', 'above bottom question line', 'oval around dernière')],
    '051.05': [('drawing', 'left margin question', 'frame around Il semble')],
    '051.14': [('drawing', 'right of opening paragraph', 'oval around fibres des quotients')],
    '053.16': [('deletion', 'proof diagram diagonal down-left', 'cancelled implication i to iii'), ('deletion', 'proof diagram vertical down', 'cancelled implication i prime to i double prime, triv'), ('deletion', 'proof diagram diagonal up-right', 'cancelled implication i double prime to ii')],
    '055.11': [('drawing', 'above Pic(S)=0 example', 'oval around p. ex. S local')],
    '057.05': [('insertion', 'over image in middle paragraph', 'can')],
    '059.08': [('drawing', 'above middle table', 'oval around d’un = G')],
    '062.04': [('deletion', 'upper middle diagram', 'whole Spéc Bil hyp–Spéc Bil unimod draft')],
    '062.05': [('deletion', 'upper right diagram', 'whole Alt–Spéc Alt draft')],
    '062.07': [('deletion', 'upper right coefficient system', 'cancelled system beginning (ax-by)^2')],
    '066.27': [('deletion', 'right sideways drawing label', 'ad')],
    '071.06': [('insertion', 'Proposition 5, § 5 reference', 'faint pencil 3 after n°')],
    '077.04': [('diagram', 'under upper quotient formulas', 'curved arrow from F_3 denominator to subgroup annotation')],
    '078.03': [('drawing', 'above title', 'oval around de corps')],
    '078.21': [('diagram', 'left of third Hasse line', 'curved pointer to F_2(K)/F_3(K)')],
    '079.21': [('diagram', 'above lower-left paragraph', 'curved arrow from V to valuation-ring descriptor')],
}
rebuilt = []
for r in items:
    if r['element'] == '047.20':
        continue
    if r['element'] == '062.06':
        r['kind'] = 'deletion'
    if r['element'] == '055.22':
        r['first_words_or_objects'] = 'Dans ce cas on aura = ξ=e'
    if r['element'] == '066.20':
        r['first_words_or_objects'] = 'f ~ Q, uncertain wavy relation'
    if r['element'] == '068.01':
        r['first_words_or_objects'] = '0-Σ²(Ě)→Sym²(E)→Σ²/Σ₂(Ě)→Sym²(E)'
    rebuilt.append(r)
    add = list(extra.get(r['element'], []))
    if r['element'] == '047.17':
        add.append(('drawing', 'lower left margin', 'oval around Exemple'))
    for kind, pos, first in add:
        q = dict(r)
        q.update(kind=kind, position=pos, first_words_or_objects=first, transcribed='yes')
        rebuilt.append(q)
counts = {}
for r in rebuilt:
    n = r['scan']
    counts[n] = counts.get(n, 0) + 1
    r['element'] = f'{int(n):03}.{counts[n]:02}'
with ip.open('w', newline='') as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    w.writerows(rebuilt)

pages = sorted((ROOT / 'pages').glob('*.tex'))
assert len(pages) == 39
combined = ROOT / 'MPL_45_033-080_transcription.tex'
combined.write_text('\n'.join(p.read_text().rstrip() for p in pages) + '\n')
with (ROOT / 'progress.log').open('a') as f:
    f.write('pre-freeze reconciliation ' + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC') + ': notation table completed; abbreviations and legibility note added; inventory drawing/insertion/cancellation subelements reconciled and IDs resequenced within each scan; ' + str(len(rebuilt)) + ' inventory rows, all yes; combined fragment assembled from 39 page files.\n')
print({'pages': len(pages), 'inventory_rows': len(rebuilt), 'combined_bytes': combined.stat().st_size})
