from pathlib import Path
import csv,json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition')
readings=[]
observations={}
def add(box,reading,notes):
    readings.append((box,reading))
    observations[box]=notes
add('B01',r'\[(2)\quad\left\{\begin{aligned}\sigma_0^2&=\sigma_1^2=\sigma_\infty^2=1\\ \sigma_0\sigma_1&=\deleted{\unsure{l_0\rho}}\inserted{\rho l_0}\quad\unsure{\dot{\sigma}_1|\sigma_1}\sigma_\infty=\deleted{\unsure{l_1\rho}}\inserted{\rho l_1}\quad\sigma_\infty\sigma_0=\deleted{l_\infty\rho}\inserted{\rho l_\infty}\end{aligned}\right.\]',[
'Left brace groups two rows beside handwritten (2).',
'First replacement rho l0 is below its cancellation; second and third replacements are above.',
'Underlying first two cancelled products are obscured by hatching and remain whole-product doubtful.',
'A small isolated dark point above the first sigma of the middle lower relation is preserved as an overdot-versus-incidental-ink alternative.'
])
add('B02',r'\margin{NB Comme $\sigma_1=\rho\sigma_0\rho^{-1}\ldots$, les $\leftarrow$ relations s\textquoteright écrivent aussi \deleted{\[\unsure{l_0=(\sigma_0\rho)\sigma_0(\rho\sigma_0\rho^{-1})}\\\unsure{l_1=\sigma_1\rho^2\sigma_1}\qquad\unsure{l_0=\rho^{-1}\sigma_0}\\\unsure{l_\infty=(\sigma_0\rho)^2\sigma_\infty}\]} \[l_0=\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}\quad\deleted{\unsure{On a}}\quad=\rho^{-1}[\sigma_0,\rho]\] On a \deleted{\[\unsure{\sigma_0(l_0)=l_1}\\\unsure{\sigma_0(l_1)=l_\infty}\\\unsure{\sigma_0(l_\infty)=l_1^{-1}l_0^{-1}}\]} \[\sigma_0(l_0)=l_\infty^{-1}l_1^{-1}\\\sigma_0(l_1)=l_\infty\\\sigma_0(l_\infty)=l_1\]}',[
'Complete tall upper-right margin note. Left-pointing arrow is beside relations; a tall vertical rule separates the lower note from the main text.',
'First cancellation block is densely crosshatched; every proposed complete formula there remains explicitly doubtful, including the short right-hand l0 formula and exposed exponents.',
'The short struck prose below the first live l0 equation is provisionally On a, not certain.',
'Three subsequent struck action formulas retain whole-formula doubts because strike strokes cross letter bodies and indices.',
'Last three action formulas are live and legible. No terminal punctuation is supplied.',
'Incidental main-text remnants at the extreme left are not continuations of the marginal note.'
])
add('B03',r'où $\rho$, au dessus de $\dot\rho$, est défini par \unsure{le} chemin trivial \unsure{de|en} \unsure{$P:P$|$P$ à $P$}. On a donc',[
'The second rho has a separate overdot; the first is undotted.',
'Two separate marks between the capital P forms can be a literal colon or an extremely compressed accented a; both local readings are retained.',
'The short word after trivial is locally uncertain de/en; the far-right continuation le on the upper line is clipped and qualified.',
'No punctuation is visible after donc.'
])
add('B04',r'\[\left\{\begin{aligned}\rho\sigma_0\rho^{-1}&=\sigma_1\\\rho\sigma_1\rho^{-1}&=\sigma_\infty\\\rho\sigma_\infty\rho^{-1}&=\sigma_0\end{aligned}\right.\qquad\text{i.e}\qquad\left\{\begin{aligned}\rho\sigma_0&=\sigma_1\rho\\\rho\sigma_1&=\sigma_\infty\rho\\\rho\sigma_\infty&=\sigma_0\rho\end{aligned}\right.\]',[
'Two live three-row displays with separate left braces; all six indices and all three inverse exponents inspected.',
'No equation number or terminal punctuation occurs inside this crop. The i.e separator has no visible final stop.',
'Small isolated specks by a few letters are not confidently over-dots; letter sequences themselves are read undotted.'
])
add('B05',r"\deleted{On ne voit pas apparaître d'expression de $\rho$ en fonction des \unsure{.} $\sigma_0$, $\sigma_1$, $\sigma_\infty$ seuls — on voit \unsure{par} contre (utilisant le fait que $l_0$, $l_1$, $l_\infty$}",[
'Opening of the broadly cancelled central paragraph; long oblique cancellation strokes cross its continuation.',
'The word par is clipped at the lower-left border and retained provisionally.',
'A separate point after des and before sigma0 is retained as a doubtful punctuation mark; no closing parenthesis is supplied at the end of this crop.'
])
add('B06',r"\deleted{avec la relation fondamentale (1) est une présentation de $\pi$, que $\deleted{\rho}\inserted{(\sigma_0\sigma_1)^3\ \text{\unsure{(p.ex)}}}$ peut s'exprimer en fonction des $l_i$, \unsure{puisque en vertu}}",[
'Continuation of broad cancellation. The rho after que has an additional local strike and a formula written above it.',
'The inserted product has indices 0 and 1, a closing parenthesis and superscript 3; the following small parenthetical is provisionally p.ex and remains doubtful.',
'The words after the li comma are crossed by several oblique strokes; the proposed puisque en vertu remains a whole-phrase uncertainty.',
'The group letter after de has the curved right leg of pi. Source grammar and incomplete parenthesis are not repaired.'
])
add('B07',r'\deleted{$\rho=l_0l_1l_\infty$}\qquad\deleted{\unsure{des rel.} $\sigma_i^2=1$, il faudra que $\rho$ soit}',[
'An additional horizontally cancelled rho=l0l1linfinity is above the continuing prose; it is separately represented.',
'The beginning des rel. is intersected by cancellation strokes and remains doubtful.',
'The sigma has subscript i with its dot and exponent 2; no separate overdot is read. The source sentence continues beyond this box.'
])
add('B08',r'\deleted{produit de termes $\sigma_i$ \uline{\unsure{par|pas} deux consécutifs} \unsure{distincts}, or $\sigma_0\sigma_1\sigma_0=$\quad et $\sigma$}',[
'Continuation and end of the cancelled paragraph. The phrase beginning par/pas and ending consécutifs has a low horizontal underline.',
'Distincts is crossed horizontally and remains locally doubtful.',
'The equation is genuinely unfinished after the equals sign. A detached et sigma sits above and to its right; it is retained without supplying an index or further equation.',
'No closing parenthesis or completion is added.'
])
add('B09',r'\[\left\{\begin{aligned}\dot\sigma_{\unsure{1|0}}^2&=\dot\sigma_1^2=\dot\sigma_\infty^2=1\\\dot\sigma_0\dot\sigma_1&=\dot\sigma_1\dot\sigma_\infty=\dot\sigma_\infty\dot\sigma_0=\dot\rho\\\dot\rho^3&=1\end{aligned}\right.\qquad\text{est une présentation de }\mathfrak{S}_3,\]',[
'Three live rows share a left brace; every displayed sigma and rho has a separate overdot.',
'The first subscript of the top row is a narrow upright mark, favoring 1 over a fully looped 0; local 1|0 doubt is retained. The following subscript is read 1.',
'The second row has the successive products 01, 1-infinity and infinity-0, followed by dotted rho. The third exponent is 3.',
'The group symbol is a large looped capital S with subscript 3; its following comma is retained.',
'An oblique note overlaps the lower-left region and is separately transcribed in B10; it is not part of the equations.'
])
add('B10',r'\margin{\unsure{Comme} \illegible{1} \unsure{être} \unsure{un|une} \unsure{des} \unsure{\uline{pas exigée}}}',[
'Original prescribed crop rotated -35 degrees once; no replacement crop made.',
'The small oblique note overlaps the main dotted-rho-cubed-equals-one display, whose strokes cross the first note line. That main formula is incidental here and is transcribed completely in B09.',
'The note is only partially recoverable: provisional Comme, être, un/une, des and pas exigée; one intervening word is physically obscured/clipped and counted provisionally as one.',
'The low short strokes around the final words may be underlining; this state is included within the local uncertainty rather than asserted.',
'Clipped incidental text at the bottom is not completed.'
])
add('B11',r'que le système des relations (1)(2) et \unsure{outre|entre}',[
'The complete supplied horizontal strip was read. The relation numbers are round-parenthesized 1 and 2 with no written separator.',
'The terminal short word has uncertain initial vowels and remains outre/entre; the preceding et is read literally.',
'Incidental oblique note strokes touch the top and lower-left edge. No terminal stop is supplied.'
])
add('B12',r'\[\rho^3=1\]',[
'Live isolated equation: undotted rho, exponent 3, equals sign and 1.',
'The rho descender touches the bottom crop boundary; no punctuation is visible.'
])
add('B13',r"\unsure{est} une présentation de l'image inverse de $\mathfrak{S}_3$ dans $\mathcal E$ (ou dans $\widehat{\mathcal E}$, du pt de vue profini).",[
'Two complete main-text lines. Oblique marginal writing overlaps the opening est, which remains locally qualified.',
'The first group glyph is a looped capital S with subscript 3, matching its visible form in B09 without altering its index.',
'The two E-shaped group glyphs are curved; only the second carries a clear caret hat.',
'The abbreviation pt, closing parenthesis and final stop are preserved.',
'Footer 17 also occurs incidentally at the right edge and is separately transcribed in B15.'
])
add('B14',r"\margin{C'est faux, \unsure{Comme|comme} on voit en faisant dans ces relations $\rho=1$, on \unsure{a} \unsure{pas|plus|puis} $\unsure{\rho\sigma_0\rho^{-1}=\sigma_1}$ (?)}",[
'Original prescribed crop rotated -45 degrees once; no replacement crop made.',
'Target oblique marginal note begins C\'est faux, and continues with en faisant dans ces relations rho=1.',
'The beginning of Comme/comme has a prominent initial curve; capitalization remains locally qualified.',
'The last prose words after on and the following conjugation formula are overlapped by incidental main-text strokes. The short a and pas/plus/puis readings remain provisional, and the complete final formula is qualified.',
'A question mark enclosed in two curves is preserved after the final formula.',
'Faint slanting main-text fragments at the right and bottom, including a large E, belong to the main paragraph; they are not added to the marginal note.'
])
add('B15',r'\mspage{17}',[
'Handwritten footer 17, with the 7 crossed horizontally. No terminal punctuation or cancellation.'
])
def save():
    out=base/'second/145_scan018_second.tsv'
    with out.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['box','reading']);w.writerows(readings)
    mp=base/'second/145_scan018_second_manifest.json'
    manifest=json.loads(mp.read_text(encoding='utf-8'))
    for item in manifest:
        if item['box'] in observations:
            item['observations']=observations[item['box']]
            item['inspected']=True
        else:
            item['inspected']=False
    mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Saved {len(readings)} independent readings.')
if __name__=='__main__': save()
