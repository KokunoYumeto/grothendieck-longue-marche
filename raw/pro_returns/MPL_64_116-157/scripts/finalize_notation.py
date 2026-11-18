#!/usr/bin/env python3
"""Record the principal transcriber's pre-context notation audit and index doubts.
Run once before the transcription is frozen; never modifies page fragments.
"""
from pathlib import Path
from datetime import datetime,timezone
import re
r=Path(__file__).resolve().parent.parent
p=r/'MPL_64_116-157_doubts.md'
t=p.read_text()
head=r'''# Notation table

This table records decisions from the manuscript images alone, before the context archive was opened. The principal transcriber inspected every whole page and both halves in one stream, then performed a second visual audit; the comparison below checks recurrent alphabets, exponents, arrows and abbreviations across that reading. The table is not a mathematical normalization: visible differences and unresolved readings remain in place.

| Handwritten sign or practice | LaTeX representation | Locations and visual distinction |
|---|---|---|
| Root letters with subscripts | `\zeta_i`, `\zeta_\lambda`, `\zeta_\mu` | 116–126; distinguished from coordinate `z`, the involutions `\sigma_i`, and `\xi`. The scalar on 147 remains `\unsure{\zeta\|\xi}`. |
| Involutions | `\sigma_i` | 116–121; long upper stroke and curled lower part. |
| Index set | `\unsure{J\|I}` where unresolved | 117–118; the descending/leftward foot favors J, but the ambiguity is not erased. |
| Ordinary and dual bundles | `F`, `\check F`, `\underline V`, `\underline{\mathcal O}` | 118–121; checks, tensor exponents and underlines kept at their individual occurrences. |
| Tangent and orientation objects | `t_E`, `\underline t`, `\underline\omega`, `\check{\underline t}` | 118–121; the small check above the domain on 120 remains doubtful. |
| Ornate sheaf or group letters | `\mathcal O`, `\mathcal F`, `\mathcal H` | 118–121, 143–145; the F alphabet on 118 is explicitly uncertain. |
| Teichmüller/group symbol | `\mathcal T` | 140, 150; the visibly looped script T is kept distinct from a Greek Gamma. |
| Domain letter | `\mathcal D`, with the written `+` where present | 136–152; the theorem product on 149 has `\unsure{*\|+}` because the ink is filled and multi-stroked. |
| Universal-family letter | `\unsure{\mathcal X\|\mathfrak X}` | 145–152; the same ornate crossed letter is recorded consistently with its alphabet ambiguity at each occurrence. |
| Permutation-group letter | `\unsure{\mathcal S\|\mathfrak S}` | 154; cancelled top diagram remains uncertain. |
| Lattice and fundamental-group letters | `H`, `\Pi` | 131–145; the doubtful forms on 131, 135 and 136 are not silently assimilated to H. |
| Matrix groups | `\mathrm{Gl}`, `\mathrm{Sl}` | 132–152; cursive lowercase l retained. The opening Gl/Sl ambiguity on 140 is explicit. |
| Number fields and residue fields | `\mathbb R`, `\mathbb C`, `\mathbb Q`, `\mathbb Z`, `\mathbb F_p` | As read at each occurrence; `\mathbb Z_p[t]` on 155 is retained as written. |
| Affine-line-like symbol | `\mathbb E^1_{\mathbb Z}` | 154–156; written E is retained without changing it to A. |
| Circle group | `\mathbb U` or ordinary `U` according to the strokes | 133; the manuscript uses both graphic forms. |
| Local ideals | `\mathfrak m`, `\mathfrak r(C)` | 155; the overwritten first r/m in the regularity argument is marked. |
| Quadratic-extension variable | `S` | 154–156; capital checked against nearby T and the explicit substitution `T=S-\alpha` on 155. |
| Prime versus exclamation exponent | prime; `^!` | Primes in bases/coordinates are retained; the mark on `L` at 132 remains `\unsure{\prime\|!}`. The terminal exponent of `M_{1,2}^!` on 152 is an exclamation. |
| Other small exponents | tensor powers, squares, inverse, `\vee` | 118–121, 154–157; the small dual mark on 118 and the first T/T² on 157 remain doubtful. |
| Conjugation and negative signs | `\bar`, `\overline`, visible `-` | 132, 137–139; overwritten bars and cancelled conventions are transcribed without choosing an expected analytic convention. |
| Ordinary and map arrows | `\to`, `\longrightarrow`, `\mapsto`, TikZ-cd arrows | Direction and head checked individually. The final mapping on 123 is a barred shaft without a head; the two t mappings on 146 retain a headless-shaft/mapsto alternative, distinct from the clear tau arrow. |
| Headless end of cancelled diagram | TikZ-cd `dash` | 154, last segment before 1; no arrowhead supplied. |
| Explicit equality used as a word | `$=$` | 133, 135 and 154; not expanded to *même*. |
| Double quotation strokes | two backticks and two apostrophes | Consistent LaTeX quotation throughout; no typographic English curly quotes substituted. |
| Underlining | `\uline`, `\uuline` | Single/double strokes distinguished, including *antilinéaire* on 132 and partial underlining of *rigidi* on 151. |
| Parenthesized equation numbers | `\tag{n}` or written inline number | Repetitions and doubtful numbers retained, including 27 and 19/18. |
| Authorial versus archival numbering | `\mspage` versus `% archive foliation:` | Pencil corner foliation is only a comment. Uncertain count on 129 is transcribed as cover text, not silently promoted to authorial pagination. |
| Deletion, insertion and marginalia | `\deleted`, `\inserted`, `\margin` | An insertion's attachment and a deletion's boundaries were checked separately from the reading of its words. |
| Unfinished writing | literal unfinished formula or phrase | 123, 144, 156–157; no completion, closing punctuation or missing polynomial variable supplied. |

'''
t=head+t[t.index('# Doubt register'):]
# Replace obsolete initial readings by the final visual decisions; detailed audit rows remain.
t=t.replace('| 64 | 133 | 2° upper third | au même | Connective compressed into strokes | medium |','| 64 | 133 | 2° upper third | au $=$ | Two horizontal strokes; earlier expanded tentative reading removed in visual audit | high |')
t=t.replace('| 64 | 138 | before on voit | envis. | Abbreviation compressed; could be earlier formula reference | low |','| 64 | 138 | after Torelli | mod iso | Final visual reading; earlier envis. reading rejected against the ink | medium |')
t=t.replace('| 64 | 139 | margin final sentence | où il | Connector overlaps underlined formula | medium |','| 64 | 139 | margin final sentence | auquel il / où il | Connector overlaps underlined formula | low |')
t=t.replace('| 64 | 140 | before Corollaire 2 | centraux-piles | Compound word is compressed; possible broader theorem reference | low |','| 64 | 140 | before Corollaire 2 | marteaux-pilons | Final enlarged visual reading; supersedes initial tentative reading | medium |')
t=t.replace('la base phi remplacée par lambda phi','la base phi multipliée / remplacée par lambda phi')
t=t.replace('Fraktur X also possible; subsequent occurrences use same choice','Fraktur X also possible; every recurring occurrence retains the explicit alphabet alternative')
t+='''\n| 64 | 146 | first displayed t mapping and final t mapping | barred shaft without definite arrowhead | mapsto; the separate tau mapping has a clearer head | low |\n| 64 | 154 | definition of B | S | Capital S checked against 155–156 before freezing | high |\n'''
t+=r'''
# Abbreviations encountered

Expansions in this section are editorial hypotheses only; none has been substituted into the transcription. Punctuation varies in the manuscript and is retained there.

| Written form | Probable expansion or meaning | Qualification |
|---|---|---|
| `i.e.`, `i.e` | *id est* | Latin explanatory abbreviation. |
| `p.r. à`, `p.r. au` | *par rapport à*, *par rapport au* | Relative dependence or comparison. |
| `p.ex.` | *par exemple* | Example. |
| `cf.` | *confer*, compare | Cross-reference. |
| `NB`, `NB.` | *nota bene* | Note heading. |
| `prop.` | *proposition* | 117. |
| `inv.` | *inverse* or *invariance*, according to phrase | 121, 123; expansion is contextual, not imposed in the text. |
| `div.` | *divisé* | 116, in an arithmetic expression. |
| `expr.` | *expression* | 116. |
| `ens.`, `ens` | *ensemble* | 116, 136, 138. |
| `esp.` | *espace* | Cancelled and uncertain at 134. |
| `str.` | *structure* | 132, 145. |
| `endom` | *endomorphisme* | 131. |
| `compl.` | *complexe* | 137. |
| `rigidif.` | *rigidification* | 136. |
| `corr.` | *correspondance* | 136, 145. |
| `biuniv.` | *biunivoque* | 136. |
| `iso.`, `iso`, `isom.` | *isomorphisme*, *isomorphe* | Grammatical expansion depends on occurrence. |
| `autom.` | *automorphisme* | 144, 150. |
| `ext.` | *extension* | 150, 153, 155. |
| `rev.` | *revêtement* | 155. |
| `gén.`, `gén`, `gén` with raised t | *générique*, *génériquement* | 133, 155–156; raised letter preserved as a superscript where visible. |
| `car.`, `car` | *caractéristique* | 155–156. |
| `coeff.` | *coefficient(s)* | 155. |
| `mult.` | *multiplication* | 123. |
| `hom` | *homomorphisme* | 140. |
| `pb` | *problème* | 149, 151–152. |
| `pt`, `pts` | *point*, *points* | 136, 152, 154–155. |
| `nb`, `nbs` | *nombre*, *nombres* | 138–139, 154–155. |
| `ssi` | *si et seulement si* | 155–156. |
| `qque` | *quelque* | 156. |
| `codim` | *codimension* | 154. |
| `mod` | *modulo* | Quotients, isomorphism classes and congruences; never expanded in the text. |
| `VA` | *variétés abéliennes* | Uncertain reading in the dense margin on 132; expansion also tentative. |
| `rg`, `corg` | *rang*, *corang* | Mathematical operator notation on 133–134. |
| `df` | *définition* | Superscript attached to an equality on 154. |
| `ab`, `an`, `lac` | *abélianisé*, *analytique*, *lacets* | Mathematical indices on 139–140, 150; `lac` is not silently read as `loc`. |
| `Sl`, `Gl` | special/general linear group notation | Letter case is a visual decision, not an expansion in the transcription. |
| `MM.`, `M.`, `M` | *Messieurs*, *Monsieur* | Printed correspondence. |
| `Tel.`, `Télex` | telephone, telex | Printed institutional heading on 157. |
| `h.` | *heure(s)* | Printed examination time on 157. |
| `U.S.T.L.` | Université des Sciences et Techniques du Languedoc | Institutional initialism spelled out in the same printed letter. |
| `MD/gs`, `A.`, `C.`, `Cl.`, `E.`, `JP.`, `Ph.`, `R.` | office or personal initials | Not expanded without evidence. |

# Legibility and limits

The larger mathematical displays and the printed notices are generally clearer than the prose. The least secure material is the small oblique marginalia on 116, 132 and 139, the overwritten signs on 125–126 and 138–139, the cancelled sentence on 149, the crowded lower revisions on 152, and the cancelled diagram and compressed last lines on 154. Scan 155 has difficult margin connectors and an unresolved phrase after *génériquement*; the reused sheet 157 contains unfinished, overwritten calculations whose incompleteness has been kept.

The transcription is a visual reading, not a reconstructed critical text. The many `\unsure` marks are substantive limits on confidence; they must not be treated as verified readings merely because the underlying mathematics is familiar. All supplied whole images and halves were inspected directly, with additional enlarged or rotated crops when useful; no OCR was used. Printed reverse-side notices, cover titles and pencil counts are included, while archive foliation is distinguished from authorial numbering. This output does not claim that a further human palaeographic review could find no remaining error.

# Complete uncertainty concordance

The following index is generated from the final pre-context page files. Locations are source-TeX line numbers, added for precise retrieval; the preceding register gives physical positions and the stronger individual assessments. Confidence is conservatively recorded as low in this exhaustive index wherever the particular occurrence has not been assigned a more specific assessment above; this is not a second reading or a change to the text. Every literal alternative remains in its original order.

| Cote | Scan | TeX line | In-place reading or alternatives | Confidence |
|---|---|---|---|---|
'''
count=0
for page in sorted((r/'pages').glob('*.tex')):
 s=page.read_text();scan=page.stem[-3:]
 for m in re.finditer(r'\\unsure\{',s):
  i=m.end();start=i;depth=1
  while i<len(s) and depth:
   if s[i]=='\\' and i+1<len(s) and s[i+1] in '{}':i+=2;continue
   if s[i]=='{':depth+=1
   elif s[i]=='}':depth-=1
   i+=1
  assert depth==0,(page,m.start())
  value=s[start:i-1].replace('\n',' ').replace('|','&#124;').replace('`','&#96;')
  line=s.count('\n',0,m.start())+1
  t+=f'| 64 | {scan} | {line} | `{value}` | low; see assessed register |\n';count+=1
p.write_text(t)
with (r/'progress.log').open('a') as h:h.write('notation audit complete '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+f'; recurring alphabets, primes/exclamation marks, arrows, bars, quote convention, abbreviations and uncertainty concordance compared before context; {count} in-place uncertainty occurrences indexed.\n')
print(f'Notation table and {count} uncertainty entries written.')
