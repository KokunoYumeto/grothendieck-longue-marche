"""Pre-context editorial housekeeping, after the root's visual comparison.

This is not an OCR or reading program. It records root-approved notation
choices, expands already-recorded inventory groups, and builds the register.
Do not run after the transcription has been frozen.
"""
from pathlib import Path
import csv
import re
from workflow import ROOT, PREFIX, log, now, combine, macro_arguments

assert 'transcription frozen ' not in (ROOT/'progress.log').read_text()

for n, old, new in [
    (46, r'\mathbf{Q}', r'\mathbb Q'),
    (47, r'\mathbf Z', r'\mathbb Z'),
    (51, r'\mathbf P', r'\mathbb P'),
]:
    p=ROOT/'pages'/f'{PREFIX}_138_scan{n:03}.tex'
    p.write_text(p.read_text().replace(old,new))

# The root compared the open-loop symmetric-group glyph on 060, 061 and
# 080--087. Its alphabet remains uncertain; use the same alternatives.
for p in sorted((ROOT/'pages').glob('*.tex')):
    s=p.read_text()
    s=s.replace(r'\unsure{\mathfrak S|\mathcal S}', 'SYMMETRICGLYPH')
    s=s.replace(r'\unsure{\mathfrak S}', 'SYMMETRICGLYPH')
    s=s.replace(r'\unsure{\mathfrak S_3}', r'SYMMETRICGLYPH_3')
    s=s.replace(r'\mathfrak S', 'SYMMETRICGLYPH')
    s=s.replace('SYMMETRICGLYPH', r'\unsure{\mathfrak S|\mathcal S}')
    p.write_text(s)

ip=ROOT/(PREFIX+'_inventory.csv')
rows=list(csv.DictReader(ip.open()))
fields=list(rows[0])
expanded=[]
for row in rows:
    n=int(row['scan']); e=row['element']; words=row['first_words_or_objects']
    replacements=None
    if n==47 and e=='047-16':
        replacements=[('deletion','-1(1)'),('deletion','i(n); crossed connecting stroke')]
    elif n==66 and e=='066-04':
        replacements=[('margin note','-g prime; ici'),('deletion','-g prime'),('deletion','ici')]
    elif n==66 and e=='066-29':
        replacements=[('deletion','sum'),('deletion','si'),('deletion','ou')]
    elif n==68 and e=='068-23':
        replacements=[('deletion','On ne peut être plus précis'),('deletion','de'),
                      ('insertion','les p-sous-'),('deletion','extensions'),
                      ('deletion',"toute hypothèse; On déduit même que l’extension est"),
                      ('deletion','abélienne finie')]
    elif n==71 and e=='071-08':
        replacements=[('deletion','compatible'),('insertion','de omega dans')]
    elif n==80 and e=='080-12':
        replacements=[('deletion','le'),('deletion','le rang')]
    elif n==82 and e=='082-06':
        replacements=[('deletion','Changeons'),('deletion','le')]
    if replacements:
        for kind, text in replacements:
            x=dict(row);x['kind']=kind;x['first_words_or_objects']=text;expanded.append(x)
    else:
        expanded.append(row)

def add_before(n, predicate, kind, position, text):
    idx=next(i for i,r in enumerate(expanded) if int(r['scan'])==n and predicate(r))
    x=dict(expanded[idx]);x.update(kind=kind,position=position,first_words_or_objects=text)
    expanded.insert(idx,x)

add_before(64,lambda r:r['kind']=='deletion','margin note','right edge of diagram','cancelled pi_1 plus')

# Move audit-added elements next to the block to which the ink belongs.
for n, position_prefix, anchor in [
    (49,'upper expansion coefficient','049-04'),
    (83,'above Gal argument','083-04'),
]:
    extra=[r for r in expanded if int(r['scan'])==n and r['position'].startswith(position_prefix)]
    expanded=[r for r in expanded if r not in extra]
    idx=next(i for i,r in enumerate(expanded) if int(r['scan'])==n and r['element']==anchor)+1
    expanded[idx:idx]=extra

expanded.sort(key=lambda r:int(r['scan'])) # stable within-page reading order
counts={}
for r in expanded:
    n=int(r['scan']);counts[n]=counts.get(n,0)+1;r['element']=f'{n:03}-{counts[n]:02}'
with ip.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(expanded)

notation=r'''# Notation table

This table was completed by comparing recurring signs against the scans before the context ZIP was opened. It records graphic readings, not identifications imported from later texts. Alternatives remain in the transcription wherever the ink does not decide; a repeated doubtful alphabet is marked at every occurrence.

| Manuscript sign | LaTeX rendering | Evidence / cautions |
|---|---|---|
| Double-stroked number-system letters | `\mathbb Q`, `\mathbb Z`, `\mathbb N`, `\mathbb C`, `\mathbb P` | Compared on 046–047, 051, 068, 071, 075, 078 and 080–089; hats, bars and powers are separate marks. |
| Double-stroked dihedral D | `\mathbb D` | Clear on 047; `\unsure{\mathbb D\|D}` on 062 retains the less decisive strokes there. |
| Curved S for the permutation group | `\unsure{\mathfrak S\|\mathcal S}` | Same open-loop shape on 060–061 and 080–087; the letter S is clear, but the exact typographical alphabet remains uncertain. |
| Rectangular capital Gamma | `\Gamma`, `\widetilde\Gamma` | 081–083 and 089; also the Galois-group Gamma on 084–087. |
| Curved script T with a loop across the top | `\mathcal T`, `\widetilde{\mathcal T}` | 084–087; checked against the rectangular Gamma on 081–083. No inference of an identification between these letters is inserted. |
| Exclamation-mark exponent | `^!`, `^{!0}` | 086–087: the upright stroke and separate lower dot are retained as an exclamation mark, never a prime. |
| Primes and double primes | `'`, `''` | Coordinates on 049–055, maps and objects on 058–061, flags on 077; distinct from the late exclamation marks. |
| Circle / zero in superscripts | `^\circ`, `^0` | Circle forms in groupoid kernels and 081 are recorded as circles; zero forms in 086 are retained as zeros. These shapes do not by themselves justify identifying all the groups. |
| C and a possible script C | `C_n`, `\unsure{C_n\|\mathcal C_n}` | The later looped occurrence on 046 remains doubtful. |
| Upper- and lower-case pi | `\Pi`, `\pi` | Capital Pi in early covering groups and 074–075; lower-case pi for the profinite groups on 080–089. The drawing labels on 064 and 077–078 are lower-case pi. |
| Script J / plain J | `\mathcal J`; one `\unsure{\mathcal J\|J}` | 072–075; retained separately from plain I and from the puncture set S. |
| T / L for the rank-one module | `\unsure{T\|L}`, plain `L`, plain `T` | 089 contains visibly different or ambiguous forms; they have not been silently unified. |
| Lowercase ell / e / 1 in transported groupoid elements | The alternatives at the relevant formulas | 058–059; subscripts and inverses were checked separately. |
| Lambda, mu, nu; rho and its indices | `\lambda`, `\mu`, `\nu`, `\rho` | 047–055, 064, 066–068, 080–089. The 0/1 ambiguity in rho on 064 remains marked. |
| Set empty sign, wedge and multiplication signs | `\varnothing`, `\wedge`, `\times` | 062, 071–075; the ambiguous wedge/cross on 062 is explicitly retained. |
| Hat over Spec | `\widehat{\operatorname{Spec}}` or marked alternative | Accent-like mark on 047; visible corresponding mark on 051. No correction to affine Spec is made. |
| Exterior-square symbol and Pi with lower wedge | `\bigwedge^2`, `\Pi_\wedge` | 074–075; the crowded 074 insertion is much less secure than 075 and remains marked. |
| Semidirect notation | `\underset{1/2}{\mathord{.}}`, words `produit $\tfrac12$ direct`, or the written dot | 047, 068, 084, 087; no uniform modern semidirect-product symbol is substituted. |
| Arrow, dash, inclusion and isomorphism | `\longrightarrow`, `-`, `\subset`, `\simeq`, etc., with local alternatives | Actual heads and strokes govern the encoding. The plain/dotted dashes on 060, 081, 085–087 remain dashes or explicitly doubtful. |
| E plus/minus, D double indices, S single indices | `E^\pm`, `D_{ij}`, `S_i` | 064, 077–078; each diagram was checked individually, rather than copied by inferred symmetry. |
| Underlining and double underlining | `\uline{...}`, `\uuline{...}` | Includes “Hyp” on 089 and the double underline on 062. Formula underlines use mathematical positioning where necessary. |
| Double quotation marks | two backticks followed by two apostrophes | Actual quotes on 070, 072, 082. A standalone pair of upper ticks used as a ditto mark on 086/089 is retained separately. |
| Added archive numbers | `% archive foliation: n` | Pencil foliation is not treated as the author's pagination. No confident author page number has been supplied via `\mspage`. |

'''

abbreviations=r'''# Abbreviations

The expansions below are editorial suggestions only; none replaces the abbreviated text in the transcription. Periods and their absence are preserved in the page files.

| Form met | Suggested expansion / sense | Scans or setting |
|---|---|---|
| `ramfctn` | ramification; compressed spelling itself is uncertain | 046–047 |
| `rev.`, `revêt`, `pro-` | revêtement(s), with the written pro-prefix | 046, 082 |
| `pts`, `pt`, `pt⁽ˢ⁾` | point(s) | 047, 068 |
| `resp.` | respectivement | 075 |
| `gr.`, `ss-groupe`, `ss` | groupe; sous-groupe; sous | 062, 068, 073, 086 |
| `autom.`, `Aut` | automorphisme(s); automorphism group | 057 onward |
| `hom`, `hom.`, `Hom`, `Homext` | homomorphisme; morphism set; exterior homomorphism classes | 058 onward |
| `iso`, `iso.`, `isom`, `isom.` | isomorphisme / isomorphe, according to the local sentence | 058–061, 074–075, 080–089 |
| `il f. et s.`, `il f et s.`, `il f. et il s.` | il faut et [il] suffit | 058–061 |
| `comp.`, `conn.` | composante(s); connexe(s) | 058, 061, 071–072 |
| `NB` | nota bene | 061, 080 |
| `Obs` | observation | 066 |
| `ens`, `ens.` | ensemble | 062, 066, 071 |
| `tt`, `tte`, `ts` | tout / toute / tous; the endings are uncertain on 062 | 062, 073 |
| `tjrs` | toujours | 066 (alternative), 075 |
| `pb` | problème | 073 |
| `ds` | dans | 068, 089 |
| `alg.`, `car.` | algébrique; caractéristique | 068, 081, 083 |
| `gén.`, `génᵗ` | généra[lement] on 068; générateurs on 085 | 068, 085 |
| `tlt` | totalement | 068 |
| `dim` | dimension | 068 |
| `quo.`, `inv.` | quotient; invariant | 074 |
| `can.`, `can` | canonique(s) | 084, 087 |
| `ext.` | extérieur(s) / extérieure, depending on the local construction | 074, 082 |
| `décomp.` | décomposition (reading uncertain) | 071 |
| `envisag.` | envisagées (reading uncertain) | 082 |
| `pro.` | profini, in the cancelled phrase | 089 |
| `syst.` | systèmes | 068 |
| `quelc.` | quelconque | 066 |
| `OPS` | on peut supposer | 066, 083 |
| `i.e.`, `i. e.` | id est / c'est-à-dire | Throughout the mathematical notes |
| `de \bar m`, `au =`, `le =` | de même / au même / le même, where the ink uses a sign | 058, 062, 071–072 |
| `trans.`, `tr`, `gr.` in cancellations | No expansion confidently established from the remaining ink | 068, 084 |
| `M.`, `MM.`, `Mr`, `MR` | Monsieur, Messieurs, Mister; typographic form kept | Reused letters and forms |
| `Cl.` | clair | 072 |
| `Techn.`, `Univ.` | technique, université | Reused administrative sheets |
| `N°` | numéro | Reused administrative forms |

# Legibility

All 42 supplied whole-page images and both corresponding halves were inspected manually, in scan order, without OCR. Each page was then read against its image again in a separate audit. Typed sheets are generally clear; the most difficult material is the interleaving of local corrections and large diagonal cancellations on 068, the oblique and crowded insertion on 074, and the small overstruck flag coordinates on 077. Other sensitive places include the pale calculations on 049–055, the right edge of the E-plus condition on 077, the lower paragraph of 058, the top module letters on 089, and short superscripts/subscripts throughout.

The table does not assign statistical probabilities. **High** means a strongly favoured reading with a small residual graphic doubt; **medium** means a plausible reading or two graphic alternatives; **low** marks a particularly weak or obstructed reading. A readable mathematical expression can still be erroneous or unfinished in the manuscript; apparent contradictions have not been repaired. No `\illegible` token was needed: in each difficult passage at least a tentative reading was supplied with `\unsure`, including the weakest ones. That is not a claim that those readings are reliable.

The drawings are manual TikZ reconstructions of the visible strokes and labels, not geometric normalizations. The manuscript's incomplete lines, unclosed prose parentheses, isolated labels and corrected formulas are retained. Static LaTeX structure and TikZ endpoints were checked; a full rendered compilation was unavailable because the installed TeX executable has no usable LaTeX/package tree. The technical report records that limitation.
'''

def cell(s):
    return s.replace('\n',' ').replace('|',r'\|')

def confidence(n,line,arg):
    if n==74 and line>=23 and line<=34: return 'low'
    if n==68 and line>=34: return 'low'
    if n==77 and (line>=66 and line<=70): return 'low'
    if n in (54,55) and ('deleted' in arg or 'vphantom' in arg): return 'low'
    if n==89 and (line<=10 or 'widehat F' in arg): return 'low'
    if n==65 or n==76: return 'low' if n==65 else 'medium'
    if 'ramfctn' in arg or arg in ('Ricouard','2'): return 'high'
    return 'medium'

doubts=['# Doubts\n\nApproximate line numbers refer to the per-page TeX source. A single marked reading has no positively identified alternative. Confidence concerns the ink, not mathematical plausibility. The first reading is the preferred graphic reading.\n\n| Cote | Scan | Approx. line / place | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n']
for p in sorted((ROOT/'pages').glob('*.tex')):
    n=int(re.search(r'scan(\d+)',p.name)[1]);s=p.read_text()
    for line,arg in macro_arguments(s,'unsure'):
        first,*alts=arg.split('|')
        alt=' / '.join(alts) if alts else '—'
        doubts.append(f'| 138 | {n:03} | TeX line {line} | `{cell(first)}` | `{cell(alt)}` | {confidence(n,line,arg)} |\n')
    for line,arg in macro_arguments(s,'illegible'):
        doubts.append(f'| 138 | {n:03} | TeX line {line} | Physically unreadable: {arg} word(s) | — | low |\n')
(ROOT/(PREFIX+'_doubts.md')).write_text(notation+''.join(doubts)+'\n'+abbreviations)
combine()
log('Cross-page notation review completed before context: number-system alphabets; Gamma versus script T; exclamation exponents versus primes; S and J alphabets; circles, bars, indices, arrows/dashes and quotation marks '+now())
log(f'Inventory regrouped into {len(expanded)} individually indexed rows; all transcribed=yes; doubt register regenerated from final per-page sources '+now())
print(f'{len(expanded)} inventory rows; {len(doubts)-1} doubt rows; combined transcription written')
