"""Build the public doubt table from the final, pre-context page files.

The JSONL is a historical reading journal, including superseded first-pass
readings. This table deliberately takes the readings from the current TeX.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
PREFIX='MPL_68_033-056+162-1+162-6'

def marks(s):
    for m in re.finditer(r'\\(unsure|illegible)\{',s):
        level=1; i=m.end(); start=i
        while level:
            if s[i]=='{' and (i==0 or s[i-1]!='\\'): level+=1
            elif s[i]=='}' and (i==0 or s[i-1]!='\\'): level-=1
            i+=1
        yield m.start(),m.group(1),s[start:i-1]

def split_alternatives(s):
    level=0
    for i,c in enumerate(s):
        if c=='{' and (i==0 or s[i-1]!='\\'): level+=1
        if c=='}' and (i==0 or s[i-1]!='\\'): level-=1
        if c=='|' and level==0: return s[:i],s[i+1:]
    return s,''

def esc(s): return s.replace('|',r'\|').replace('\n',' ')
out=[(ROOT/'notation.md').read_text(),
'''## Doubts in the frozen transcription

All entries concern **68.pdf**. “L” is the line number in the named individual page's `.tex` file; it is a precise locator within that file, not a claim about the manuscript's physical line numbering. The short context is taken from that same line, whose place on the sheet can also be found in the inventory. The first reading and the alternative are copied from the final pre-context transcription; a blank alternative means that no second reading was sufficiently supported by the ink.

Confidence is deliberately conservative: **medium** means a supported but uncertain reading, and **low** means obscured, overwritten, clipped or especially ambiguous ink. Clear but mathematically surprising readings are discussed separately below. Historical first-pass guesses in `doubts_rows.jsonl` and the page-writing records are superseded where the audit changed them; they are not additional readings proposed by this final table.

| File | Scan | Approximate line / anchor | Reading | Alternative | Confidence |
|---|---:|---|---|---|---|
''']
total=0
for p in sorted((ROOT/'pages').glob('*.tex')):
    s=p.read_text(); scan=int(re.search(r'scan(\d+)',p.name)[1])
    for pos,kind,body in marks(s):
        total+=1; lineno=s.count('\n',0,pos)+1
        line=s.splitlines()[lineno-1]
        near=line[max(0,pos-(s.rfind('\n',0,pos)+1)-45):][:110]
        reading,alternative=split_alternatives(body)
        if kind=='illegible':
            reading=f'Unreadable ink: estimated {body} word(s)'
            alternative='No supported reading after repeated enlargement'
        low=(kind=='illegible' or r'\deleted' in line or scan in {43,53,55,56}
             or (scan==36 and any(x in body for x in ['introduction','indéterminées','voir']))
             or (scan==41 and body=='0|1')
             or (scan==54 and any(x in body for x in ['(-1)','ell'])))
        conf='low' if low else 'medium'
        out.append(f'| 68.pdf | {scan:03} | L{lineno}: `{esc(near)}` | `{esc(reading)}` | {"`"+esc(alternative)+"`" if alternative else "—"} | {conf} |\n')

out.append('''
## Additional local cautions and clear discrepancies

| File / scan / place | Reading retained | Confidence and reason |
|---|---|---|
| 68.pdf / 036 / second marginal NB | `exp 1=0` | High as a reading: the word is exp, not log; the mathematical issue belongs in the research notes. |
| 68.pdf / 037–044 / group letters | ordinary `G` with separately read bars | Medium: reinforcement alone does not securely distinguish ordinary, bold or blackboard-bold G. No mathematical convention was used to add missing bars. |
| 68.pdf / 041 / coefficient display | `c_{ij}=1/(i+j)!` in a ditto-style layout | High for the visible coefficient; no minus sign or additional 1 was supplied. |
| 68.pdf / 041 / ambient operator space | `U=End_K(M)` | High for the visible letter M; no replacement by Hom(M,N). |
| 68.pdf / 041 / operator alphabet | `Theta`, `Theta'` | Medium: large crossed circular forms could be lowercase theta; the same convention is used throughout. |
| 68.pdf / 043 / vertical semilinearity connector | downward arrow | Medium: shaft and direction are supported, terminal stroke faint. |
| 68.pdf / 044 / final E identity | plus sign between the E terms | High: a cross is visible; composition is not substituted. |
| 68.pdf / 046 / first corollary | `opérateur diff` | High after enlargement: the longer word is opérateur, not autom. The earlier record was corrected before freezing. |
| 68.pdf / 050 / proof under a) | `varphi_V: Omega(W) -> Omega'(W)` | High for W and the right arrow; the subscript/object mismatch is retained. |
| 68.pdf / 050 / bottom Stokes expression | `Omega(V,W)` | High: the order differs from earlier Omega(W,V). |
| 68.pdf / 052 / last cancellation | `deleted{illegible{1}}` | Low: dense hatching conceals the word. A trial reading “Vérifier” could not be supported and is not transcribed. |
| 68.pdf / 053 / last imperative revision | `deleted{illegible{2}}` | Low: attempted readings involving toi / un / toi-même / autant were not sufficiently visible. |
| 68.pdf / 054 / bottom square | one secure downward arrow at right | Medium: reinforced corners are not all arrowheads; the other strokes are reproduced without invented heads. |
| 68.pdf / 054 / product sign exponent | q first, ? as alternative | Low: closed head and descending stem favour q; this is not reliable evidence of an authorial question mark. |
| 68.pdf / 055 / faint upper-right marks | marginal unreadable ink, estimated one word | Low: erased or transferred lettering is possible; no manuscript page number can be recovered. |
| 68.pdf / 056 / lower-left determinant object | `Delta(V_1)` | High for the two-stroke V; the expected W is not substituted. |
| 68.pdf / 056 / vertical isomorphisms | headless connectors | High for absence of definite heads; the right connector has a curved foot. |

## Abbreviations encountered

Expansions in this table are interpretive aids only. They have **not** been substituted into the transcription; periods, raised endings, shorthand equality signs and doubtful endings remain as written.

| Written form(s) | Probable expansion / meaning |
|---|---|
| `resp.`, `Resp`, `Resp.` | respectivement |
| `i.e.`, `i.e` | id est / c'est-à-dire |
| `ens`, `ens.` | ensemble / ensembles |
| `il f et s.`, `il f. et s.` | il faut et suffit |
| `Th`, `Th.`, `th.` | théorème; in a theory heading, possibly théorie |
| `Prop`, `prop.` | proposition |
| `Cor`, `Cor.` | corollaire |
| `Dém` | démonstration |
| `NB` | nota bene |
| `car.`, `car` | caractéristique |
| `alg.`, `alg`, `Alg` | algèbre / algèbres |
| `ass.`, `assoc.` | associative / associatif |
| `comm.` | commutative / commutatif; in the Picard-category definition, commutativité |
| `unif.` | unifère |
| `él.` | élément / éléments |
| `nilp.`, doubtful `nilp.t` | nilpotent / nilpotente |
| `inv.` | inversible / inversibles |
| `str`, `str.` | structure |
| `app.`, `appl.` | application |
| `can.` / raised `can` ending | canonique / canoniquement, according to syntax |
| `cf.`, `cf` | confer / compare |
| `Ex.` | exemple |
| `hom.`, `hom`, `Hom` | homomorphisme; Hom also names the morphism set or functor |
| `gr`, `gr.`, `grpe`, `ssgrpe` | groupe / sous-groupe |
| `bij.`, `bij`, `bijectif` | bijection / bijective; the full word is retained where written |
| `inj`, `surj` | injective, surjective |
| `isom.`, `isom`, `iso`, doubtful `is. à` | isomorphisme / isomorphe à |
| `nb`, `nbre` | nombre |
| `cqfd.` | ce qu'il fallait démontrer |
| `cond.`, raised `condts` | condition / conditions |
| `néc.`, `n et s.`, `suff.` | nécessaire, nécessaire et suffisante, suffisante |
| `mult.` | multiplicatif |
| `endom`, `autom`, `autom.` | endomorphisme, automorphisme |
| `univ.`, doubtful raised `univ` ending | universellement |
| `réc`, `réc.` | récurrence |
| `déf`, `Défin` | définition |
| `Op.`, `op.` | opération or opérateur, depending on the phrase |
| `d'habt` / `d'hab` | d'habitude |
| `tt`, `tte` | tout / toute |
| `proj.`, `t.f.` | projectif, type fini |
| `lin.` | linéaire; this final abbreviation on 043 is uncertain |
| `loc` | localement |
| `diff` | différentiel |
| `p. ex.` | par exemple |
| `noeth` | noethérien |
| `ssi` | si et seulement si |
| `st` | sont, in the doubtful cancelled NB on 045 |
| `cat.` | catégorie |
| `card.`, `card`, `Card` | cardinal |
| `dim` | dimension |
| `p. es` / `p. esp.` | pour espaces, uncertain compressed heading on 050 |
| `ori.`, `condt` | orientation, condition, in the cancelled paragraph on 052 |
| `circ.` | circulaire |
| `pr`, `gén` | pour, général / générale |
| `sg` | signe, as the notation for the sign map |
| `funct.` | fonctoriel |
| `rg` | rang |
| `suppl.` | supplémentaire / supplémentaires |
| `de =`, `au =` | de même, au même; the equals sign is the actual transcription |

## Legibility and limits

The included material comprises 21 scans from cote 68; the supplied archive contains no pages to transcribe from 162-1 or 162-6. All whole images and both supplied halves were inspected directly in sequence, with a second full reading and additional enlarged or rotated inspection of difficult areas; no OCR or parallel readers were used. The typed pages 051, 053 and 055 were read separately, so one copy was not used to silently supply another copy's clipped or overwritten text.

Most continuous mathematical text is readable, but rapidly written endings, reinforced capitals, nearly erased marginal writing and cancellations are less secure. The least trusted areas are the oblique margin and overwritten algebra letters on 036, the evaluation symbol on 037, the compressed final word on 038, the retraced digits on 041, the final word and coefficient-ring letter on 043, several cancellations and inserted qualifications on 045, the overwritten orientation formulas on 050–054, and the central object and cancelled labels on 056. The three `illegible` locations are explicitly word estimates; none replaces a mathematical symbol or formula.

The TikZ reproductions encode visible strokes, directions and labels, with relative placement rather than photographic geometry. Neither the transcription nor its typography claims to recover ink hidden under solid cancellation. Mathematical inconsistencies have been retained; later context comparisons are confined to the research notes.
''')
(ROOT/f'{PREFIX}_doubts.md').write_text(''.join(out))
print('Wrote',total,'final doubt-macro occurrences.')
