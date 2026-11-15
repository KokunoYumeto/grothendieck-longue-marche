"""Reconcile the descriptive metadata from the personally audited page files.

No scan reading, OCR, mathematical correction or context access is performed.
Run before freezing only. Page files are read, never changed by this script.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
assert 'transcription frozen' not in (ROOT / 'progress.log').read_text()
PAGES = sorted((ROOT / 'pages').glob('*.tex'))
INV = ROOT / 'MPL_136_235-281_inventory.csv'
rows = list(csv.DictReader(INV.open()))
headers = list(rows[0])
groups = defaultdict(list)
for row in rows:
    groups[int(row['scan'])].append(row)

def new_row(n, kind, pos, words):
    return dict(cote='136', scan=str(n), sheet_kind=groups[n][0]['sheet_kind'],
                element='', kind=kind, position=pos,
                first_words_or_objects=words, transcribed='yes')

# Position the six individually inspected audit additions beside their source elements.
for n, targets in [(239, {'oval around double-underlined Iso si':'239.04'}),
                   (244, {'outline around heading':'244.01', 'circle around T':'244.05',
                          'outline around automorphism note':'244.06', 'circle around M plus':'244.07',
                          'oval around boxed functor':'244.15'})]:
    additions = [r for r in groups[n] if r['first_words_or_objects'] in targets]
    groups[n] = [r for r in groups[n] if r not in additions]
    for r in additions:
        anchor = targets[r['first_words_or_objects']]
        j = next(i for i,x in enumerate(groups[n]) if x['element']==anchor)
        groups[n].insert(j+1, r)

for r in groups[254]:
    r['first_words_or_objects'] = r['first_words_or_objects'].replace('18 Juin','16 Juin').replace('Diffusions dégénérées','Diffusions réfléchies').replace('M/Neg0','M/Neg∞ (0 alternative)')
for r in groups[271]:
    if r['element']=='271.03': r['first_words_or_objects']='ψσ←~id_C; σ exact; κ exact'
for r in groups[279]:
    if r['element']=='279.01': r['kind']='diagram'
    if r['element']=='279.14': r['first_words_or_objects']='Hom_M(s,τ^NN⊗s)≃N₀ (N alternative) ??'
j = next(i for i,r in enumerate(groups[279]) if r['element']=='279.13')
groups[279].insert(j+1,new_row(279,'deletion','lower, Hom subscript','N₀ overwritten before M'))

# Header/page-number marks are inventory elements even on reused typed sheets.
for p in PAGES:
    n=int(p.stem[-3:]); s=p.read_text()
    own=re.findall(r'\\mspage\{([^}]+)\}',s)
    for num in own:
        exists=any(r['first_words_or_objects'].strip() in [num,f'- {num} -'] for r in groups[n])
        if not exists:
            groups[n].insert(0,new_row(n,'margin note','header centre',f'- {num} -'))
    if r'\margin{IX}' in s and not any(r['first_words_or_objects'].strip()=='IX' for r in groups[n]):
        groups[n].insert(1,new_row(n,'margin note','header right','IX'))
    # Printed top markers originally inventoried after body text are moved to the top.
    top=[r for r in groups[n] if r['position'].startswith('header') or
         (r['first_words_or_objects']=='IX' and 'top' in r['position']) or
         r['position']=='top above page number']
    groups[n]=top+[r for r in groups[n] if r not in top]

ordered=[]
for n in sorted(groups):
    for i,r in enumerate(groups[n],1):
        r['element']=f'{n}.{i:02d}'
        ordered.append(r)
with INV.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=headers); w.writeheader(); w.writerows(ordered)

notation = r'''# Notation table

This is the single notation table for the package. The quotation-mark convention was entered before the first page; the fuller table was consolidated at the start of the second reading, rather than being maintained fully during the first pass. Recurring signs were compared during the personal audit and the final reconciliation, before any context content was opened; local unresolved differences remain marked in the transcription.

| Sign or alphabet | LaTeX representation | Evidence and cautions |
|---|---|---|
| Double quotation marks | two backticks and two apostrophes | Printed and handwritten double quotes use the same encoding; guillemets are not substituted. |
| Roman capitals and lower-case letters | `A,B,C,K,M,N,P,Q,R,S,T,X,Y,Z`; `i,j,k,n,p,q,s,t,u` | Case follows each occurrence; in particular the coalgebra `s` on scans 279–281 is not silently changed to `S`. |
| Hatted algebra A | `\widehat A`, `\hat A` | Both commands denote a hat, with width chosen to fit its scope; the additional raised wedge on scan 235 is separately doubtful. |
| Star, cochain dot, divided-power index | `*`, `\bullet`, `^{(i)}` | These are distinct marks; parentheses are not supplied around an ordinary power. |
| Calligraphic category letters | `\mathcal M`, `\mathcal N` | Calligraphic categories are kept distinct from their ordinary module letters `M,N`; uncertain overwritten letters are marked. |
| Other script/underlined letters | `\mathcal`, `\mathfrak`, `\underline`, `\uline` as locally written | Underlining in the reused print is retained, including underlined modules and rings. |
| Doubled integers, rationals, fields, multiplicative group | `\mathbb Z`, `\mathbb Q`, `\mathbb F`, `\mathbb C`, `\mathbb G` | Doubled glyphs were reconciled; the boxed lower symbol on scan 281 remains doubtful. Ordinary isolated `Z` is not automatically an integer ring. |
| Greek capitals | `\Delta`, `\Gamma`, `\Sigma`, `\Phi`, `\Psi`, `\Pi` | Exterior powers use `\bigwedge`, not capital Delta; the Pi/K reading on scan 239 remains explicit. |
| Greek lower-case letters | `\alpha`, `\beta`, `\gamma`, `\delta`, `\eta`, `\kappa`, `\lambda`, `\mu`, `\pi`, `\rho`, `\sigma`, `\tau`, `\varphi`, `\psi` | Letter identities follow visible strokes; the right-adjoint rho and later varphi notation are not unified merely by their roles. |
| Xi and zeta | `\xi`, `\zeta` | Cancelled calculations on scans 249 and 251 and coefficients on 259/279 were rechecked; residual ambiguity is marked. |
| Sigma versus tau | `\sigma`, `\tau` | Scan 279 writes sigma in the truncation definition and tau in the theorem; this discrepancy is retained. |
| Kappa versus ordinary k | `\kappa`, `k` | Adjoint/evaluation kappa is retained on 252, 263, 269 and 271; coefficient rings use ordinary k. |
| Zero versus O | `0`, `\underline O` | The underlined local-ring letter on scan 238 remains O/0 doubtful; it is clearer on 242. |
| Exclamation exponent | `^!` | Personally checked on printed scans 272 and 274; not encoded as a prime. |
| Prime and dual sign | `'`, `^\vee` | Base-change/object primes and the dual signs on 281 remain distinct. |
| Natural/sharp and b/flat | `\natural`, `\sharp`, `b`, `\flat` within explicit doubts | The reused Raynaud print does not always distinguish these small signs clearly. |
| Translation and truncation indices | `T^i`, `[-i]`, lower/upper indices on `\tau,\sigma,\varphi,\rho` | Signs and bracket directions are retained individually, including apparently inconsistent indices. |
| PD coefficient algebras | `k\{T\}`, `k\{\{T\}\}`, doubtful `\langle T\rangle` | Single braces, double braces and angle-bracket alternatives are not equated. |
| Arrows and plain strokes | `\longrightarrow`, `\longleftarrow`, `\xrightarrow`, `\xleftarrow`; TikZ `nohead` | A line without a visible head is retained as such or marked dash/arrow doubtful; the unit on 271 points left. |
| Parallel maps and tables | `\diagram{\begin{tikzcd}...}` / `\diagram{\begin{array}...}` | All objects and written labels are represented; no missing target is supplied from the mathematics. |
| Underlining and deletion | `\uline`, `\uuline`, `\deleted` | Nested cancellations are retained inside the larger cancelled blocks. |
| Added writing and marginal writing | `\inserted`, `\margin` | Insertions follow the visible relation to the main text; separate margin notes remain separate. |
| Abbreviations | literal forms in the transcription | Proposed expansions appear only in the list below. |

# Readings in doubt

Each row records one occurrence of a doubt macro in the final, pre-context page files, including doubts inside other doubtful or cancelled material. Line numbers refer to the individual page file and are approximate locators in the image, not manuscript line counts. “Medium” means a plausible visible reading remains uncertain; “low” is used for competing readings, difficult cancellations, and longer uncertain phrases. These labels are editorial judgements, not calibrated probabilities. A dash in the alternatives column means that no second reading is proposed, not that the first is certain.

| File | Scan | Approximate line | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|---|
'''

def escaped(s,i):
    n=0; i-=1
    while i>=0 and s[i]=='\\': n+=1; i-=1
    return n%2==1

def argument(s,start):
    assert s[start]=='{'
    level=1; j=start+1
    while j<len(s):
        if not escaped(s,j):
            if s[j]=='{': level+=1
            elif s[j]=='}':
                level-=1
                if not level: return s[start+1:j],j+1
        j+=1
    raise ValueError('Unclosed macro')

def alternatives(s):
    level=0
    for i,c in enumerate(s):
        if escaped(s,i): continue
        if c=='{': level+=1
        elif c=='}': level-=1
        elif c=='|' and level==0: return s[:i],s[i+1:]
    return s,''

def md(s):
    return s.replace('\n',' ').replace('|',r'\|').replace('`','&#96;').strip()

out=[notation]
count=0
for p in PAGES:
    s=p.read_text(); n=int(p.stem[-3:])
    for m in re.finditer(r'\\(unsure|illegible)\{',s):
        body,end=argument(s,m.end()-1)
        rd,alt=alternatives(body)
        if m.group(1)=='illegible': rd=f'physically unreadable: estimated {body} word(s)'; alt=''; confidence='low'
        else: confidence='low' if alt or n in [247,249,251,253,279,281] or len(body.split())>3 else 'medium'
        line=s.count('\n',0,m.start())+1
        out.append(f'| `{p.name}` | {n} | {line} | `{md(rd)}` | '+(f'`{md(alt)}`' if alt else '—')+f' | {confidence} |\n')
        count+=1

out.append(r'''
# Abbreviations encountered

These are proposed expansions, provided only here. A form may be abbreviated differently in separate places, and doubtful expansions do not resolve doubtful ink.

| Written form | Proposed expansion or explanation | Scans / caution |
|---|---|---|
| `ab.` | abélienne / abélien | 275; `.ab` on abelian-part notation is retained mathematically as written. |
| `adj.` | adjoint | 246, 271. |
| `alg.` | algèbre | 247, 251. |
| `autom.` | automorphisme | 244. |
| `bij.` | bijectif / bijective | 257. |
| `can.` | canonique | 257. |
| `Cat.` | catégorie | 275; reading itself is marked. |
| `cf.` | confer / comparez | Reused typed pages. |
| `comm.`, `commut.` | commutatif / commutative | 244, 247; the latter is cancelled. |
| `copuiss.` | copuissances | 281; abbreviated phrase is doubtful. |
| `déf.` | défini / définition | 237; the short inserted phrase is doubtful. |
| `ens` | ensembles | 257; reading is doubtful, no full stop supplied. |
| `Ex`, `p.ex.`, `p. ex.` | exemple; par exemple | 239, 263, 265. |
| `Exp.` | exposé | In typed mathematical references. |
| `ext.` | extension | 259. |
| `g.`, `dr.`; `à g` | gauche, droite | 244, 246, 275. |
| `gr.`, `grad`, `gr.d` | gradué / graduée; graded | 247, 279; the last abbreviated subscript is not expanded in the transcription. |
| `hom`, `homom.` | homomorphisme | 259, 267, 269. |
| `homog` | homogène | 259, inserted parenthesis. |
| `hyp.` | hypothèse | 235. |
| `i.e.`, `i.e` | id est | Throughout; punctuation follows the individual occurrence. |
| `isom`, `iso`, `Iso` | isomorphisme | Throughout the handwritten calculations. |
| `loc.`, `loc.cit.`, `loc. cit.` | localisation; loco citato | The functor label on 250 and the references on 270 have different senses. |
| `NB`, `N.B.` | nota bene | Throughout the handwritten pages. |
| `négl.`, `négl` | négligeable | 256–259. |
| `p.` | page | Bibliographic references. |
| `par.` | paragraphe | 236, 238. |
| `p.f.` | présentation finie | 257, cancelled and replaced by `t.f.`; expansion is probable. |
| `pl. fid.`, `pl. fidèle` | pleinement fidèle | 244–279. |
| `pr. div.`, `puiss. div.`, `pd`, `p.d.` | puissances divisées / divided powers | 235, 247, 251 and the PD calculations; `pr. div.` itself is doubtful. |
| `prés. finie` | présentation finie | 265. |
| `quelc.` | quelconques | 246; reading is doubtful. |
| `resp.` | respectivement | 274. |
| `respect` | respectant | 281; uncertain abbreviated phrase, not silently expanded. |
| `ss.-module` | sous-module | 246. |
| `syst.` | système | 275. |
| `t.f.` | type fini | 256–257. |
| `t.q.` | tel que | 259. |
| `Th.`, `th.` | théorème | 279; 272 reference. |
| `Mod`, `Hom`, `End`, `Ker`, `Im`, `Imess`, `Ext`, `NS`, `Spec`, `Gal` | modules; homomorphisms; endomorphisms; kernel; image; essential image; extensions; Néron–Severi; spectrum; Galois group | Conventional mathematical labels, retained literally and with their written capitalisation. |
| `EXTPAN`, `EXT` | catégorie d'extensions panachées; catégorie d'extensions | 278; distinct from `Ext` groups. |
| `GAGA` | Géométrie algébrique et géométrie analytique | 242, typed reference. |
| `EGA`, `SGA` | Éléments de géométrie algébrique; Séminaire de géométrie algébrique | Reused typed pages, not expansions supplied in their text. |
| `U.E.R.` | Unité d'enseignement et de recherche | 245. |
| `U.S.T.L.` | Université des sciences et techniques du Languedoc | 258; the full name is also printed on the sheet. |
| `Pr`, `M.`, `Mr`, `n°` | Professeur; Monsieur; Monsieur; numéro | Reused administrative sheets. |
| `AMC/MD` | Administrative initials / routing code | 258; not expanded because the names are not supplied. |
| `P.R.`, `A.`, `R.`, `E.` before personal names | Personal initials | Reused letters/notices; no unattested full names supplied. |

# Legibility and limits

Every supplied whole-page image and both supplied halves was personally viewed in the first reading, and every page was personally read again against its transcription before the freeze. Rotations, crops and enlargements were used for inverted writing and difficult strokes; no OCR was used, and no context text or published mathematical text was used to supply a reading. The context ZIP's directory names had been listed before the prompt was read; its contents remained unextracted and unread until the recorded freeze and opening time.

The reused print is mostly clear, with local damage, faint type, overwritten signs and show-through. Scan 254 is especially faint; its mirrored seminar notice was checked on that scan's own ink. The handwritten notes vary considerably: the cancelled calculations on 247, 249, 251 and 253, the overlapping Hom computations on 279, and the inverted cancelled block on 281 are the least secure parts. Arrowheads, coefficients, letter endings, and overwritten subscript/prime marks are the main remaining risks. The small natural/sharp and b/flat signs in the printed mathematical pages remain explicitly uncertain.

The TikZ drawings are hand-coded approximations of visible strokes, shapes and signatures. They preserve labels and relationships, but do not claim pixel-level facsimile fidelity. The fragment has been checked mechanically for its declared structure; the supplied environment has no usable LaTeX class/package tree, so no successful typesetting run is claimed. The doubt table includes the unresolved readings rather than treating a plausible mathematical reconstruction as a verified reading.
''')
(ROOT/'MPL_136_235-281_doubts.md').write_text(''.join(out))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'metadata reconciliation {now}: inventory regrouped in page order, duplicate IDs removed by renumbering, audit corrections and missing heading entries incorporated; doubt register rebuilt from every final in-place doubt macro ({count} occurrences), abbreviations and legibility note completed.\n')
print(f'Inventory: {len(ordered)} rows; doubt occurrences: {count}')
