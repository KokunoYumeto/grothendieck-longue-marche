"""Consolidate the current root-reader marks; old readings remain in records only."""
from pathlib import Path
import json,re
from collections import Counter
ROOT=Path(__file__).resolve().parent.parent

def arg(s,i):
 while s[i].isspace():i+=1
 assert s[i]=='{'
 start=i+1;level=1;i+=1
 while i<len(s):
  if s[i]=='\\':i+=2;continue
  if s[i]=='{':level+=1
  if s[i]=='}':
   level-=1
   if level==0:return s[start:i],i+1
  i+=1
 raise ValueError('unbalanced argument')

def code(s):
 s=s.replace('\n',' ').replace('|',r'\|')
 fence='`'*(max([len(x) for x in re.findall(r'`+',s)]+[0])+1)
 return fence+' '+s+' '+fence

def words(s):
 return set(re.findall(r'[A-Za-zÀ-ÿ]{3,}',s.lower()))-{'unsure','deleted','inserted','uline','operatorname','mathrm','mathcal','mathbb','frac','text'}

records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
header=r'''# Notation and doubts — MPL 57, scans 271–315

## Package notation table

This is the final pre-context notation register. The primary reader compared the recurring forms during the second visual reading and revisited the differing C/Q/Z alphabets before the freeze; local differences that the ink does not resolve remain marked in the transcription. Upright `\operatorname{Pic}` and `\mathrm{Pic}` render the same alphabet; their choice does not distinguish two manuscript objects.

| Visible convention | LaTeX rendering | Scans / decision |
|---|---|---|
| Ordinary Latin capitals and lower-case letters | `X,Y,S,A,B,C,D,F,G,L,M,N,V,W`; `x,y,s,t,p,n,u,v` | Case retained, including `F_0` with `B_0` alternative on 289. |
| Typewritten mathematical letters | Ordinary math letters; printed indices retained | 271, 273, 295–296, 299, 301, 303, 307, 312; missing typewritten arrows/signs on 307 are not supplied. |
| Doubled field/ring capitals | `\mathbb C`, `\mathbb Q`, `\mathbb Z` | 272, 281, 285, 289, 291–292 compared together; Q on 281 remains `\unsure{\mathbb Q\|\mathbf Q}`. The forms agree with 296, 300, 302. |
| Script L, O, D, P, R | `\mathcal L`, `\mathcal O`, `\mathcal D`, `\mathcal P`, `\mathcal R` | 271, 272 onward, 302, 304; local alternatives for R/P and L/F retained. |
| Gothic M | `\mathfrak M` | 291, distinct from ordinary M in the final covariant formula and on 292; first occurrence marks the alphabet uncertainty. |
| Gothic g versus script T | `\unsure{\mathfrak g\|\mathcal T}` | 294, 297; the same preferred letter is used, with visible underlining on 294 only. |
| Gothic X versus script X | `\unsure{\mathfrak X\|\mathcal X}` | 300; retained as an unresolved alphabet distinction. |
| Greek letters | `\alpha,\beta,\gamma,\lambda,\mu,\nu,\rho,\sigma,\tau,\varphi,\Phi,\xi,\Gamma,\Lambda,\Omega` | Original case kept; gamma/sigma and Gamma/sigma ambiguities marked locally in 297, 304. |
| One / two underline strokes | `\uline{...}`, `\uuline{...}` | Both math and words; nested legacy underline encodings were converted without changing the stroke count. The two O underlines on 285 remain doubtful. |
| Pic / Nér / NS / Hom | Upright names, with one or two underlines as drawn | 275–290; no global replacement of single by double underlining. |
| Accented Nér and Néron in formulas | `\operatorname{N\acute{e}r}`, `\mathrm{N\acute{e}ron}` | Encoding preserves the written accent and avoids a dropped glyph in pdfLaTeX. French prose accents remain UTF-8. |
| Overwritten Pol → Nér | `\deleted{...}\inserted{...}` | 275–280; untouched instances of Pol remain unchanged. |
| Prime, double prime, plus | `'`, `''` or `\prime\prime`, `+` | 275–281; prime strokes were checked independently of word-ending exclamation-like abbreviation strokes. No mathematical exclamation exponent is inferred. |
| Zero / tau / positive part | `^0`, `^\tau`, `^+` | Kept distinct throughout; crossed superscripts retain deletion and doubt markers. |
| Two loops / infinity | `\unsure{00\|\infty}` | 294 and 311; the separate-loop reading leads in both. |
| Action invariants / coinvariants | `A^\Gamma`, `A_\Gamma`, `t_{A'}`, `(t_A)'` | 284–288, 297; exponent/subscript and position of the prime are not normalized. |
| Left torsion prefix | `{}_nM`, `{}_pM`, `{}_{p^n}M`, `{}_2A'` | 285, 291–292, 313; not rewritten as a right subscript. |
| Tate-type functors | `T_p` and `T^p` | 291–292; lower and upper p remain distinct. |
| Hats and checks | `\widehat A`, `\widehat X`, `\widehat Y`, `\check V` | 272, 294, 297; doubtful letters under the marks are not harmonized from meaning. |
| Structure sheaf and differential underlining | `\uline{\mathcal O}`, `\uline{\Omega}` where drawn | 287–288, 294, 302, 304, 315; plain and underlined occurrences remain locally distinct. |
| Quotient styles | `\mathbb Z/2\mathbb Z`, `\mathbb Z/2`, `\mathbb Z_2` | 285, 300, 302; the shortened quotient/subscript forms are not expanded. |
| Products / tensor products | `\times`, `\otimes`, `\prod_{Y/S}` | Products on 287 and the relative product on 283–284 retained; no substitution of direct-sum notation. |
| Limits | `\varprojlim`, `\varinjlim`, with written indices | 291–292, 296; direction is read from the source arrows. |
| Inequalities and inclusions | `\leq,\geq,\subset,\not\subset,\ne` | 289–292, 296, 313; the third hypothesis on 289 was rechecked as an equality, while its subscript remains doubtful. |
| Plain line versus arrow | `\mathbin{\unsure{-\|\to}}`, or `\arrow[...,dash]` | 272, 289, 297, 300, 309; doubtful heads are not supplied confidently. |
| Isomorphism signs | `\simeq`, `\overset{\sim}{\longrightarrow}` | Kept separate from equality and bare arrows. |
| Equals-like shorthand | `=`, `\overline{=}`, with local `\unsure` | 280, 285, 286, 309, 310, 313; never expanded to the word “même” in the transcription. |
| Double quotation marks | Two backticks and two apostrophes | French and English quoted phrases; two ditto marks on 313 remain unexpanded. |
| Guillemets | `«` and `»` | The angular pair at the end of 288 is retained. |
| Printed running numbers | `\margin{...}` | 271, 273, 312; the damaged first digit in 312 remains doubtful. |
| Printed page numbers and lower pencil foliation | `\mspage{...}` | Printed surrounding dashes are literal text; the lower foliation is retained separately, even where the printed sequence is out of order. |
| Cancellations, insertions and marginal matter | `\deleted`, `\inserted`, `\margin` | Includes overwritten symbols and partial words; crossed passages are not silently discarded. |
| Diagrams / non-diagram line work | `\diagram{\begin{tikzcd}...}` / `\figure{\begin{tikzpicture}...}` | Objects and labels are transcribed; hand-drawn line shapes are approximations of their visible relative geometry. |

## Current doubts

Every `\unsure` and `\illegible` occurrence in the final page files is indexed below, in scan order. “Line” gives the approximate location through the numbered line of the page fragment, plus a nearby manuscript phrase when available; long manuscript paragraphs can occupy one LaTeX line. Confidence concerns the proposed reading, not the mathematical plausibility: **medium** means a plausible ink reading with a residual ambiguity, **low** means substantial ambiguity or overwritten/faint ink; no uncertainty has been upgraded merely because the mathematics fits.

The older candidate readings in `records/` document the working history. Where they differ, this table and the frozen page fragment give the final pre-context reading; a dash in the alternatives column means that no second positive reading is proposed, not that the first is certain.

| File / cote | Scan | Line approximately | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|---|
'''
rows=[];counts=Counter()
low_scans={272,275,276,277,279,280,284,286,287,289,290,291,292,294,297,298,300,302,304,306,307,309,310,313,314}
for d in records:
 t=d['tex'];scan=d['scan']
 for m in re.finditer(r'\\(unsure|illegible)\s*\{',t):
  body,end=arg(t,m.end()-1);kind=m.group(1);line=t.count('\n',0,m.start())+1;counts[kind]+=1
  if kind=='illegible':
   reading='Physically unreadable: estimated '+body+' word(s)';alternative='No positive reading retained';confidence='low'
  else:
   # The first separator in these marks separates the two reading candidates.
   parts=body.split('|',1);reading=parts[0];alternative=parts[1] if len(parts)>1 else '—'
   confidence='low' if scan in low_scans else 'medium'
  token=words(reading)
  candidates=[]
  for j,x in enumerate(d['doubts']):
   w=words(str(x.get('reading','')));score=len(token&w)/max(1,len(token))
   if token and score>=.7:candidates.append((score,j,x))
  loc='LaTeX line '+str(line)
  if candidates:
   x=max(candidates,key=lambda x:(x[0],x[1]))[2]
   loc+='; '+x['line']
   if kind=='unsure' and x.get('confidence') in ('medium','low'):confidence=x['confidence']
  rows.append('| 57.pdf / 57 | '+str(scan)+' | '+loc.replace('|',r'\|')+' | '+code(reading)+' | '+code(alternative)+' | '+confidence+' |')

abbrevs=[
('i.e. / ie.','id est; that is'),('n° / N° / n^circ','numéro'),('ord','ordre'),('resp.','respectivement'),('N.B.','nota bene'),('O.K. / OK','okay; affirmative check'),('C.Q.F.D.','ce qu’il fallait démontrer'),('cf.','confer; compare'),('th.','théorème'),('prop.','proposition'),('cor.','corollaire'),('chap. / Chap.','chapitre'),('App.','appendice'),('éd.','édition'),('p.','page when bibliographic; the mathematical p is not expanded'),('ex. / p. ex. / p.ex','exemple / par exemple'),('exer.','exercice'),('loc.','localement'),('fid. / fid','fidèlement'),('plat / plt.','plat / plate, as abbreviated in context'),('qu. cpt / q. cpt / qu. cpts','quasi-compact / quasi-compacts'),('tte / tt / ttes','toute / tout / toutes'),('tjrs','toujours'),('qcq','quelconque'),('ens','ensemble'),('éléme / élémt','élément(s); ending retained as written'),('changt','changement'),('f. et s.','faut et suffit'),('ssi / sss','si et seulement si; the doubled-s form is kept'),('ss-','sous-'),('pt / pts','point / points'),('nb','nombre'),('inv.','inversible'),('rel. / rel!','relativement; the final shorthand stroke is not a mathematical exponent'),('abs','absolument; cancelled reading remains doubtful'),('alg. / algt.','algébriquement or algébrique according to the phrase'),('Alg.','algèbre in bibliographic references; final abbreviation on 272 is uncertain'),('géom. / géom^t / géo','géométrique / géométriquement; géo on 277 remains uncertain'),('Géom.','géométrie'),('gén.','général / généralement'),('car. / car / caract.','caractéristique'),('rés.','résiduelle(s)'),('noeth.','noethérien'),('prés.','présentation'),('proj.','projectif'),('lin.','linéairement'),('équiv.','équivalence / équivalent'),('équivalts','équivalents'),('isom / isom.','isomorphisme'),('Hom','homomorphismes; upright mathematical operator'),('Pic / Pic.','Picard'),('Nér / N.S. / NS','Néron / Néron–Severi, with the written name changes preserved'),('comp.','composantes'),('ext.','extension'),('can.','canonique'),('univ. / univ^t','universellement'),('indép.','indépendantes'),('hyp.','hypothèse'),('d’acc.','d’accord; uncertain abbreviation on 290'),('mor!','morphisme; ending on 272 uncertain'),('ensemblist!','ensemblistement'),('trivial!','trivialement'),('diffelles / diffélles','différentielles; quoted abbreviation on 303'),('anots','probably anneaux noethériens; the expansion remains uncertain and the spelling is not repaired'),('géné','générique; cancelled, uncertain shortened word on 290'),('Min. / Dim.','possibly minimum / dimension; first reading Min. on 309 remains doubtful'),('no.','uncertain short cancelled abbreviation on 279; no reliable expansion')]
footer='\n\n## Abbreviations met\n\nExpansions below are explanatory proposals only. They are not inserted into the transcription, and an uncertain abbreviation does not gain certainty through this list.\n\n| Written abbreviation | Probable expansion or qualification |\n|---|---|\n'
for a,b in abbrevs:footer+='| '+code(a)+' | '+b+' |\n'
footer+='''
## Legibility and limits of confidence

The clean typed pages are generally the most secure, although missing typewriter signs, overtyping, damaged digits and original word spacing require care (especially 307 and the running number on 312). The handwritten definitions and larger displays are more legible than the compressed connecting prose; quotations, accents, index positions and the ends of abbreviated words remain significant sources of uncertainty.

The least secure passages are the heavily cancelled opening of 279, the crossed final clause on 284, parts of 286–287, the pale gluing discussion on 298–302, the cancelled projective-family draft on 306, and especially the slanting left note on 309 and the boxed/marginal comments on 310. The final two lines of the left note on 309 should be treated as a provisional sequence of ink readings, not as a reliable mathematical sentence. The opaque cancelled word on 315 and the other numbered unreadable spans were retained only after enlarged visual inspection; word counts are estimates, and no mathematical symbol has been replaced by an illegibility count.

The main reader viewed every supplied whole image and both halves, completed a second page-by-page visual audit, and then compared recurring notation across the package before freezing. No OCR or context-derived correction was used. The TikZ line work preserves the visible structure and labels but is not a metric facsimile: long insertion strokes and cancellation enclosures have approximate shapes, and their association is also carried by the insertion/deletion macros and inventory positions.

The frozen transcription is an auditable reading with explicit uncertainty, not a claim that every ambiguous letter has been solved. Mechanical compilation confirms that the fragments can be processed with the documented macro wrapper; it cannot establish a manuscript reading.
'''
text=header+'\n'.join(rows)+footer
(ROOT/'MPL_57_271-315_doubts.md').write_text(text)
print({'rows':len(rows),'marks':dict(counts),'abbreviations':len(abbrevs),'bytes':len(text.encode())})
