from pathlib import Path
import csv, json, os, re

ROOT=Path('/workspace/scratch/b12af914b284')
OUT=ROOT/'edition/reader_returns'
index=json.loads((ROOT/'edition/scripts/150_scan060_crop_index.json').read_text())
boxes=index['crops']
def cp(n): return f'crops/150_scan060_{n}.png'

# The doubtful cancelled s is overprinted at the head of p, not set as a
# spatially separate preceding letter. Its identity remains a proposal.
first_glyph=r'\mathord{\rlap{$\deleted{\unsure{s}}$}p}_1'
tex=r'''\scanpage{60}
On voit alors que
\[
x\prec y\text{ et }y\prec z\quad\Longrightarrow\quad x\prec z
\]
car soient $u,v\in\Sigma_{\unsure{<|*}}(1)$ tels que
\[
FIRST_GLYPH u=x,\quad\uline{b}u=\underbrace{y,\quad p_1}v=y,\quad\uline{b}v=z
\]
% In the first glyph the possible cancelled s overlaps the head of p;
% the earlier letter is unresolved. The short brace is spatial: it lies
% beneath the first y toward the following p_1, not beneath both complete equalities.
on a donc
\[
\unsure{\uline{b}}u=p_1v
\]
% This b and its underline are heavily overdrawn. No earlier character is assigned.
donc par le carré cartésien de (38), \deleted{$\exists\unsure{w|u}$}
\[
\exists\mid\ d\in\Sigma^{\unsure{<|*}}(2),\quad\text{avec}\quad\uline{b'}(d)=v,\quad p_2(d)=u
\]
soit
\[
w=\uline{s'}(d)\in\Sigma^{\unsure{<|*}}(1)
\]
on a
\[
\begin{aligned}
p_1(w)&=p_1(\uline{s'}(d))\overset{(38)}{=}p_1p_2(d)=p_1(u)=x\\
\uline{b}(w)&=\uline{b}(\uline{s'}(d))=\uline{b}(\uline{b'}(d))=\uline{b}(v)=z
\end{aligned}
\]
donc
\figure{\begin{tikzpicture}[baseline=(x.base)]
\node (x) at (0,0) {$w:x$};
\node at (2,0) {$z$};
\draw (1.15,.28) .. controls (1.15,.08) and (1.08,.03) .. (.85,0);
\draw[->] (.85,0) .. controls (1.03,-.03) and (1.2,-.18) .. (1.45,-.28);
\end{tikzpicture}}.
De plus, on a
\[
x\not\prec x\qquad\left(\text{car }\operatorname{Im}(\Sigma_1\overset{(p_1;\uline{b})}{\relbar\joinrel\relbar}\Sigma\times\Sigma)\cap\text{diag}=\varnothing\right)
\]
% The final = empty-set and the end of the parenthesis continue below at the right.
donc la relation $x\prec y$ est la relation
d'inégalité stricte associée à une relation
d'ordre sur $\Sigma$. On récupère $\Sigma^{\unsure{<|*}}(1)$ comme
le graphe de la relation d'ordre stricte,
$\Sigma^{<}(2)$ comme les drapeaux $x\prec y\prec z$ de
longueur $2$ dans \illegible{1} $\Sigma$, et les applications
% A separate small curved upright is raised in the gap after dans, before Sigma;
% its value is unassigned. It is preserved above as an unread fragment.
% Pale lower-left foliation, apparently another hand; no top authorial number is visible.
\margin{59}
'''.replace('FIRST_GLYPH',first_glyph)

changes=[]
def ch(place,C,H,final,aC,aH,kind,category,marked,conf,evidence,crop,consequence=''):
    changes.append({'id':f'060-{len(changes)+1:02d}','place':place,'C':C,'H':H,'final':final,
      'against_C':aC,'against_H':aH,'kind':kind,'error_category':category,'marked_in_H':marked,
      'confidence':conf,'evidence':evidence,'crop':cp(crop),'box':boxes[crop],
      'mathematical_consequence':consequence})
ch('line 3, membership expression',r'\unsure{\Sigma_{<}(1)|\Sigma^{<}(1)}',r'\Sigma^{*}(1)',r'\Sigma_{\unsure{<|*}}(1)',False,True,
   'misread symbol or index','Symbols and indices',False,'low',
   'The small sign is lowered beside the lower-right corner of Sigma, with its bottom below the Sigma baseline. The first C placement is retained. The dark sign itself has overlapping short arms: < is the leading proposal, and * remains open. The comparison with H records the lowered placement and the leading local candidate, not a resolved rejection of the open shape.', 'p01_membership')
ch('line 4, reworked head of the first p_1',r'\deleted{\unsure{s}}p_1',r'p_1',first_glyph,True,True,
   'insertion or placement','Struck text',False,'low',
   'A long p-like descending stem and lowered 1 are visible. Looped, crossing strokes occupy the head of that p; a possible cancelled s remains doubtful. The strokes overlap the p head instead of forming a separate character at its left. The final overlay preserves that location; H leaves the reworking unrecorded.', 'p02_firstrow')
ch('line 4, span of the lower brace',r'\underbrace{\uline{b}u=y,\quad p_1v=y}',r'\underline b u=y,\quad p_1v=y; note: une accolade réunit les deux égalités',r'\uline{b}u=\underbrace{y,\quad p_1}v=y',True,False,
   'drawing or diagram','Drawings and diagrams',False,'high',
   'The short brace is centred below the gap/comma between the two middle equalities. Its left end lies beneath the first y toward its right side, and its right end reaches toward the following p_1. It does not extend beneath the full width of both equalities. The TeX brace represents its local span without assigning additional algebraic scope.', 'p02_firstrow')
ch('line 7, cancelled variable after the existence sign',r'\deleted{$\unsure{\exists u}$}',r'\struck{$\exists w$}',r'\deleted{$\exists\unsure{w|u}$}',True,False,
   'misread symbol or index','Symbols and indices',False,'low',
   'The cancelled sign has the three horizontal levels and upright of an existence sign. The following variable has two low lobes above the crossing stroke, favouring w. Because the strike hides part of the joins, u remains an explicit alternative. The comparison follows the preferred w candidate, not a claim that the alternative has been excluded.', 'p04_cancel_exists')
ch('line 8, mark after the existence sign',r'\unsure{\exists!|\exists\mid}',r'\exists!',r'\exists\mid',True,True,
   'misread symbol or index','Symbols and indices',False,'high',
   'A single continuous upright follows the existence sign. It reaches down without a separately visible lower dot. The written vertical-bar alternative is retained without adding a dot.', 'p05_existence',
   'The literal sequence is an existence sign followed by an upright. No interpretation of that upright as a uniqueness assertion has been supplied.')
ch('line 8, Sigma with parameter 2',r'\Sigma^{<}(2)',r'\Sigma^{*}(2)',r'\Sigma^{\unsure{<|*}}(2)',False,True,
   'misread symbol or index','Symbols and indices',False,'low',
   'The raised compact mark joins the opening parenthesis. An angular < is the leading local reading, but the short overlapping arms also leave * open. The H comparison records the leading proposal only.', 'p05_existence')
ch('line 9, Sigma with parameter 1',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{\unsure{<|*}}(1)',False,True,
   'misread symbol or index','Symbols and indices',False,'low',
   'The small raised sign is joined to the opening parenthesis. Its upper angled arm and thick meeting point favour <, while the compact additional projection prevents excluding *. Both alternatives remain in the text.', 'p06_w')
ch('line 13, drawn mark between x and z',r'\figure{\begin{tikzpicture}[baseline=(x.base)] ... \draw[->] ... \end{tikzpicture}}',r'w : x\prec z .',r'\figure{curved upper arm to a left junction; lower curved arm ending in a rightward arrowhead, between w:x and z}.',False,True,
   'drawing or diagram','Drawings and diagrams',False,'high',
   'The upper curve descends leftward to a junction. The lower arm curves down and right from that junction and ends in a separate two-stroke arrowhead below the z baseline. The final keeps C’s actual TikZ paths rather than replacing this drawn head by a plain relation glyph.', 'p09_drawn_mark')
ch('lines 15–16, source of the Im map',r'\Sigma_1',r'\Sigma^{*}(1)',r'\Sigma_1',False,True,
   'misread symbol or index','Symbols and indices',False,'high',
   'A plain Sigma is followed by a short lowered upright 1. There is no raised star or parenthesised argument in this local source expression.', 'p10_Im_whole')
ch('lines 15–16, punctuation in the map label',r'(p_1;\uline{b})',r'(p_1,\underline b)',r'(p_1;\uline{b})',False,True,
   'misread symbol or index','Symbols and indices',False,'high',
   'Between p_1 and the underlined b, a distinct upper point stands above a lower comma-shaped stroke. The source label uses a semicolon.', 'p10_Im_whole')
ch('lines 15–16, horizontal shaft within Im',r'\unsure{-|\longrightarrow}',r'\xrightarrow{(p_1,\underline b)}',r'\overset{(p_1;\uline{b})}{\relbar\joinrel\relbar}',False,True,
   'drawing or diagram','Drawings and diagrams',False,'high',
   'The horizontal shaft has a slightly thick right endpoint but no separately drawn upper or lower arrowhead arm. It is retained as an extended unheaded rule, the first C alternative.', 'p10_Im_whole')
ch('line 18, after associée',r'associée à une relation',r'associée : une relation',r'associée à une relation',False,True,
   'misread word','Words',False,'high',
   'The short mark after associée has a small horizontal/curved a body and a detached upper grave stroke. The two levels have different shapes, supporting the accented letter à.', 'p11_associee')
ch('line 19, Sigma after On récupère',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{\unsure{<|*}}(1)',False,True,
   'misread symbol or index','Symbols and indices',False,'low',
   'The raised sign has an angular upper arm and thick join into the opening parenthesis. < is retained first, while the compact lower projection leaves * open. This is an explicitly unresolved comparison.', 'p12_recupere')
ch('line 21, Sigma before comme les drapeaux',r'\Sigma^{<}(2)',r'\Sigma^{*}(2)',r'\Sigma^{<}(2)',False,True,
   'misread symbol or index','Symbols and indices',False,'high',
   'The raised sign shows two arms meeting at a left point, with the lower arm joining the opening parenthesis. Its angular shape is locally separable from that parenthesis.', 'p13_drapeaux')
ch('line 22, gap after dans',r'dans $\Sigma$',r'dans $\Sigma$',r'dans \illegible{1} $\Sigma$',True,True,
   'omission','Omissions',False,'medium',
   'A separate small curved upright stands high in the blank interval after dans and before Sigma. It is visible independently of both neighbouring words. It is retained as an unassigned fragment; no letter, punctuation function or attachment is selected.', 'p14_length')
ch('bottom left, pale foliation',r'\mspage{59}',r'(not recorded)',r'\margin{59}',False,True,
   'omission','Omissions',False,'high',
   'The lower-left grey writing reads 59: a double-curved 5 and a looped 9 with a descending curved tail. It is apart from the dark main writing and is represented as marginal foliation.', 'p15_foliation')

# Exact surrounding source for the figure is retained in the C/H fields as
# available source text, while the final contains the complete chosen drawing.
csource=(ROOT/'input/SP91_C13_150_texts/pages/150_scan060.tex').read_text()
hsource=(ROOT/'input/SP91_C13_150_texts/hua/hua_150_scan060.tex').read_text()
figure_c=re.search(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}',csource,re.S).group(0)
for row in changes:
    if row['place']=='line 13, drawn mark between x and z':
        row['C']=figure_c
        row['H']=r'w : x\prec z .'
        row['final']=figure_c+'.'
    if row['place']=='line 4, span of the lower brace':
        row['H']=r'\underline b u=y,\quad p_1v=y'

D=[
 {'id':'M0599','decision':'first','reading':r'\Sigma_{\unsure{<|*}}(1)',
  'evidence':'The mark is clearly lowered beside Sigma’s bottom right, retaining the first C placement. Its thick local < / * shape is a separate unresolved doubt, made explicit in the final.',
  'crop':cp('p01_membership'),'box':boxes['p01_membership'],'confidence':'medium'},
 {'id':'M0600','decision':'alternative','reading':r'\exists\mid',
  'evidence':'One continuous upright follows the existence sign, with no independently visible exclamation dot. The second C alternative records the written form.',
  'crop':cp('p05_existence'),'box':boxes['p05_existence'],'confidence':'high'},
 {'id':'M0601','decision':'first','reading':r'\relbar\joinrel\relbar',
  'evidence':'The shaft is a horizontal line whose endpoint thickens slightly without separate arrowhead arms. The first C alternative is represented as an extended unheaded rule.',
  'crop':cp('p10_Im_whole'),'box':boxes['p10_Im_whole'],'confidence':'high'},
]

inventory=[]
def inv(kind,pos,words,hand='his hand'):
    inventory.append({'element':f'E{len(inventory)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':words,'sheet_kind':'text','hand':hand,'transcribed':'yes'})
inv('text','line 1','On voit alors que')
inv('display','line 2',r'x\prec y et y\prec z \Longrightarrow x\prec z')
inv('text','line 3',r'car soient u,v\in\Sigma_{\unsure{<|*}}(1) tels que')
inv('display','line 4',r'p_1u=x, \uline b u=y, p_1v=y, \uline b v=z')
inv('deletion','overlapping the head of the first p_1 in line 4',r'possible cancelled s, retained with doubt over the reworked p head; earlier letter not established')
inv('drawing','beneath the middle gap in line 4',r'short lower brace from the first y toward the following p_1; spatial span preserved')
inv('text','line 5','on a donc')
inv('display','line 6',r'\unsure{\uline b}u=p_1v; b and underline densely overdrawn; no earlier letter assigned')
inv('text','line 7',r'donc par le carré cartésien de (38),')
inv('deletion','right end of line 7',r'\exists\unsure{w|u}; heavy strike crosses the sign and the two-lobed variable')
inv('display','line 8',r'\exists\mid d\in\Sigma^{\unsure{<|*}}(2), avec \uline{b\prime}(d)=v, p_2(d)=u')
inv('display','line 9, with soit at the far left',r'soit w=\uline{s\prime}(d)\in\Sigma^{\unsure{<|*}}(1)')
inv('text','line 10','on a')
inv('display','line 11',r'p_1(w)=p_1(\uline{s\prime}(d))=(38) p_1p_2(d)=p_1(u)=x')
inv('insertion','above an equality in line 11',r'(38), a parenthesised reference written above the equality after p_1(s\prime(d))')
inv('display','line 12',r'\uline b(w)=\uline b(\uline{s\prime}(d))=\uline b(\uline{b\prime}(d))=\uline b(v)=z; composition retained literally')
inv('diagram','line 13',r'donc w:x [upper curve meeting a lower curved arm with a rightward arrowhead] z .')
inv('text','line 14','De plus, on a')
inv('display','line 15 with a short lower-right continuation on line 16',r'x\not\prec x (car Im(\Sigma_1 [unheaded shaft labelled (p_1;\uline b)] \Sigma\times\Sigma)\cap diag=\varnothing)')
inv('text','lines 17–22',r'donc la relation x\prec y est la relation ... longueur 2 dans Sigma, et les applications')
inv('text','line 22, raised in the gap after dans',r'\illegible{1}; separate small curved upright, unassigned')
inv('text','bottom left, outside the body','59; pale grey foliation, no dark top authorial number is visible','apparently another hand, pale grey writing')

doubts=[
 {'place':'line 3, lowered mark next to Sigma','reading':r'\Sigma_{\unsure{<|*}}(1)','alternatives':r'< or *; lowered placement is secure','confidence':'low','reason':'The compact dark arms overlap. The lowered position settles the placement part of M0599, while the local shape remains open.'},
 {'place':'line 4, reworked head of first p_1','reading':first_glyph,'alternatives':'possible cancelled s over a p head; earlier character unassigned','confidence':'low','reason':'The descending p-like stem and lowered 1 are visible, but the head contains multiple loops and crossing strokes. The s proposal is retained without certainty and at the overlap position.'},
 {'place':'line 6, overdrawn underlined b','reading':r'\unsure{\uline b}u=p_1v','alternatives':'b is the retained letter; previous form, if any, unassigned','confidence':'low','reason':'A tall stem and lower rounded body support b, but repeated internal crossings and dense parallel underline strokes obscure the earlier ductus. C and H agree on b; this new uncertainty is not a textual comparison correction.'},
 {'place':'line 7, cancelled variable','reading':r'\deleted{\exists\unsure{w|u}}','alternatives':'w first, u second','confidence':'low','reason':'Two low lobes favour w, but the horizontal strike crosses their joins.'},
 {'place':'line 8, raised Sigma mark','reading':r'\Sigma^{\unsure{<|*}}(2)','alternatives':r'C: <; H: *','confidence':'low','reason':'The raised mark is compact and joins the opening parenthesis; the short arms do not securely exclude either local candidate.'},
 {'place':'line 9, raised Sigma mark','reading':r'\Sigma^{\unsure{<|*}}(1)','alternatives':r'C: <; H: *','confidence':'low','reason':'The thick junction and joining parenthesis leave a small projection whose status cannot be resolved.'},
 {'place':'line 19, raised Sigma mark after On récupère','reading':r'\Sigma^{\unsure{<|*}}(1)','alternatives':r'C: <; H: *','confidence':'low','reason':'An angled arm is visible, but the compact joining strokes leave the alternative star reading open.'},
 {'place':'line 22, after dans','reading':r'\illegible{1}','alternatives':'unassigned raised curved upright; no punctuation reading selected','confidence':'low','reason':'The independent stroke is visible, but it has no securely identifiable letter or role on this page.'},
]

notes=[
 {'id':'150-060-N01','text':'No authorial page number is visible at the top; a pale lower-left foliation reads 59. The line count includes the short lower-right continuation of the Im parenthesis as its own physical row. The manuscript opens On voit alors que, followed by an implication involving x, y and z. It then chooses u and v in a Sigma expression with a visibly lowered local mark. The first p_1 has reworked strokes over its head, and a short brace lies beneath the gap between the two middle equalities. These local marks are retained without assigning an earlier letter from the expected formula.'},
 {'id':'150-060-N02','text':'The author invokes the carré cartésien de (38), writes a cancelled existence expression with a doubtful two-lobed variable, and continues with an existence sign followed by one uninterrupted upright. The upright is transcribed literally; no uniqueness meaning is supplied. The author then writes w=s′(d) and two equality chains. The second chain includes b(s′(d))=b(b′(d)) as written. Neither the referenced square nor the validity of these chains has been independently checked in this page reading.'},
 {'id':'150-060-N03','text':'The conclusion w:x ... z uses a drawn two-arm curved mark whose lower arm ends in an arrowhead. The manuscript next gives x not-prec x and an Im expression with source Sigma_1, label (p_1; underlined b), a visibly unheaded shaft, a crossed product sign and intersection with diag followed by the empty-set sign. The final equality and outer parenthesis continue below at the right. These are descriptions of the source display, without a separate proof of its claim.'},
 {'id':'150-060-N04','text':'The final paragraph describes the relation in the author’s words as the relation d’inégalité stricte associée à une relation d’ordre sur Sigma. It says that Sigma(1) is recovered as the graph and Sigma(2) as the drapeaux x-prec-y-prec-z of length 2, then ends with et les applications. Local raised marks remain doubtful where the ink is compact. A separate curved upright after dans is recorded as an unassigned fragment. No mathematical theorem has been checked during this transcription.'},
]
notation=[
 {'form':r'\prec','meaning':'The author’s written relation sign in the displayed implication and later prose.','evidence':'Curved left-pointing two-arm marks between x,y,z.','places':'lines 2, 15, 17, 21'},
 {'form':r'\Sigma_{\unsure{<|*}}(1)','meaning':'The lowered-mark Sigma expression in the author’s choice of u,v.','evidence':'The small mark lies below/right of Sigma, rather than above it; its arms remain compact.','places':'line 3'},
 {'form':r'\Sigma^{\unsure{<|*}}(2),\Sigma^{\unsure{<|*}}(1),\Sigma^{<}(2)','meaning':'Local raised marks on the Sigma expressions.','evidence':'Compact joins with parentheses in lines 8, 9 and 19; a separable two-arm angle in line 21.','places':'lines 8, 9, 19, 21'},
 {'form':r'p_1,p_2','meaning':'Labels used in the author’s equalities and map label.','evidence':'Small lowered upright 1 and curved 2 next to p; repeated across the formulas.','places':'lines 4, 6, 8, 11, 15'},
 {'form':r'\uline b,\uline{b\prime},\uline{s\prime}','meaning':'Underlined letter labels in the source’s formulas.','evidence':'Independent horizontal strokes beneath the letters, with primes above/right where present; one b is densely overdrawn.','places':'lines 4, 6, 8–9, 11–12, 15'},
 {'form':r'\exists\mid','meaning':'The literal existence sign followed by an uninterrupted upright; meaning of the upright not assigned.','evidence':'No separate exclamation dot is visible.','places':'line 8, M0600'},
 {'form':r'\Sigma_1\overset{(p_1;\uline b)}{\relbar\joinrel\relbar}\Sigma\times\Sigma','meaning':'The map-like expression inside the author’s Im display.','evidence':'Lowered 1, semicolon in the label, unheaded horizontal shaft and crossing strokes in the product sign.','places':'lines 15–16'},
 {'form':r'(38)','meaning':'The manuscript’s written internal reference.','evidence':'Parenthesised 3 and 8 in prose and above the first equality chain.','places':'lines 7 and 11'},
]
abbreviations=[
 {'written':'Im','expansion':'image','places':'line 15; mathematical short form retained'},
 {'written':'diag','expansion':'diagonale','places':'line 15; short form retained'},
]
hand_log=[
 {'habit':'Overwriting is locally dense at a p head and at a separate underlined b.','places':'lines 4 and 6','scope':'both reworked clusters inspected separately','witness_errors':'C’s possible cancelled s is spatially relocated to the p head; H omits the reworking there. The earlier form beneath b is not assigned.'},
 {'habit':'A short brace may sit only under the middle gap of a longer displayed row.','places':'line 4','scope':'the single brace on this page','witness_errors':'C’s full-width underbrace is shortened to the visible span. H records its presence in a note.'},
 {'habit':'Two low lobes survive above a cancellation stroke.','places':'cancelled variable at line 7','scope':'this single struck variable','witness_errors':'The leading proposal w follows the visible lobes; C’s u remains open as the second candidate.'},
 {'habit':'The mark after the existence sign is a continuous upright.','places':'line 8','scope':'this occurrence only','witness_errors':'H’s exclamation dot is not visible; C’s written vertical-bar alternative is chosen.'},
 {'habit':'Small marks join the opening parenthesis following Sigma.','places':'lines 8, 9, 19, 21','scope':'each local occurrence inspected; three remain open','witness_errors':'Low-confidence < / * comparisons are recorded separately; line 21 has a clearer two-arm angle.'},
 {'habit':'The lower arm of the drawn conclusion has a separate arrowhead.','places':'line 13','scope':'this one drawing','witness_errors':'H’s plain prec glyph does not retain the lower head.'},
 {'habit':'A small lowered 1 can sit close to Sigma’s lower edge.','places':'line 15','scope':'the Im source expression','witness_errors':'H replaces the visible Sigma_1 by Sigma*(1).'},
 {'habit':'A compressed à has a short horizontal body beneath its grave stroke.','places':'line 18','scope':'the inspected associée à occurrence','witness_errors':'H reads a colon.'},
 {'habit':'A separate curved upright is raised between two otherwise complete words/symbols.','places':'line 22, after dans','scope':'this isolated fragment','witness_errors':'Both witnesses omit it; its identity remains unassigned.'},
]

audit=[]
def au(kind,b,reading):
    audit.append({'box':f'B{len(audit)+1:02d}','kind':kind,'x0':b[0],'y0':b[1],'x1':b[2],'y1':b[3],'reading':reading})
au('doubtful formula',[580,284,889,359],r'u,v\in\Sigma_{\unsure{<|*}}(1)')
au('struck passage',[604,391,1454,523],first_glyph+r'u=x,\quad\uline b u=\underbrace{y,\quad p_1}v=y,\quad\uline b v=z')
au('doubtful formula',[630,602,887,704],r'\unsure{\uline b}u=p_1v')
au('struck passage',[1190,721,1525,820],r'(38),\quad\deleted{\exists\unsure{w|u}}')
au('doubtful formula',[502,827,1535,950],r'\exists\mid d\in\Sigma^{\unsure{<|*}}(2),\quad avec\quad\uline{b\prime}(d)=v,\quad p_2(d)=u')
au('doubtful formula',[750,975,1252,1067],r'w=\uline{s\prime}(d)\in\Sigma^{\unsure{<|*}}(1)')
au('handwritten number',[503,1164,1314,1274],r'p_1(w)=p_1(\uline{s\prime}(d))\overset{(38)}{=}p_1p_2(d)=p_1(u)=x')
au('doubtful formula',[503,1279,1423,1362],r'\uline b(w)=\uline b(\uline{s\prime}(d))=\uline b(\uline{b\prime}(d))=\uline b(v)=z')
au('lexical disagreement',[270,1393,1210,1489],'donc '+figure_c+'.')
au('doubtful formula',[1020,1557,1675,1706],r'(car\ \operatorname{Im}(\Sigma_1\overset{(p_1;\uline b)}{\relbar\joinrel\relbar}\Sigma\times\Sigma)\cap diag=\varnothing)')
au('lexical disagreement',[812,1797,1598,1900],r'associée à une relation')
au('doubtful formula',[842,1910,1670,2022],r'On récupère \Sigma^{\unsure{<|*}}(1) comme')
au('handwritten number',[274,2154,449,2232],r'\Sigma^{<}(2)')
au('medium-confidence departure',[277,2229,1518,2341],r'longueur 2 dans \illegible{1} \Sigma, et les applications')
au('handwritten number',[24,2294,87,2343],r'59')

purpose={
'p01_membership':'Whole membership expression and M0599; lowered sign and handwritten 1.',
'p02_firstrow':'Whole first equality row, reworked/cancelled initial glyph, two p_1 indices and short local brace.',
'p03_bu':'Entire separate bu=p_1v display; heavily overdrawn b and underline.',
'p04_cancel_exists':'Reference (38) and the whole cancelled existence expression, including uncertain terminal w/u.',
'p05_existence':'Entire existence formula, M0600, local Sigma mark, both written 2 indices and the primed b label.',
'p06_w':'Whole w=s′(d) membership expression and local Sigma mark/1.',
'p07_calc1':'Whole first equality chain, including the raised (38) and every p index.',
'p08_calc2':'Whole second equality chain, inspected literally without an inferred mathematical correction.',
'p09_drawn_mark':'Complete donc w:x-to-z drawing, lower arrowhead and final period.',
'p10_Im_whole':'Whole nonrelation/Im parenthesis, M0601, Sigma_1, semicolon label, product and lower-right continuation.',
'p11_associee':'associée à une relation versus H colon.',
'p12_recupere':'On récupère Sigma(1) comme, local superscript and handwritten 1.',
'p13_drapeaux':'Sigma(2), local raised angle and following drapeaux expression.',
'p14_length':'Final line with written length 2 and previously unrecorded raised curved stroke after dans.',
'p15_foliation':'Pale bottom-left 59, omitted by H.',
}
with (ROOT/'edition/packets/150_scan060/diffs.tsv').open(newline='',encoding='utf-8') as f:
    diffs=len(list(csv.DictReader(f,delimiter='\t')))
result={'scan':'060','reader':'reader_b','line_count':22,'changes':changes,'decisions':D,
 'inventory':inventory,'doubts':doubts,'notes':notes,'check_events':[],
 'notation':notation,'abbreviations':abbreviations,'hand_log':hand_log,'audit_boxes':audit,
 'crops':[{'file':cp(n),'box':b,'purpose':purpose[n]} for n,b in boxes.items()],
 'unresolved':[
  'Shape of the lowered Sigma sign in line 3: < remains first, * open; placement itself is secure.',
  'Possible cancelled s over the first p_1 head; overlapping reworking is visible, earlier letter unproved.',
  'Dense overdrawn b and underline in the next display; no earlier letter assigned.',
  'Cancelled variable after exists: w preferred, u remains open.',
  'Compact raised Sigma forms in lines 8, 9 and 19: < / * remain open locally.',
  'Raised curved upright after dans in line 22: visible fragment unassigned.',
 ],
 'coverage':{'whole_image_viewed':True,'halves_viewed':['top','bottom'],'all_tokens_read':True,
  'all_C_insertions_deletions_checked':True,'differences_considered':diffs,
  'macro_only_differences_ignored':'H’s editorial no-number/suite note is not copied as manuscript text. Equivalent uline/underline commands, math spacing, display packaging, Im font and empty-set font are not counted as reading differences. H’s note records the brace and literal second chain; only C’s visible brace span is changed. The raw diff’s long TikZ stretch is collated as one graphic disagreement, not as source words. Existing C/H symbol disagreements with open alternatives have explicit low-confidence comparison rows using the leading final candidate; the newly doubtful b shared by C/H appears only in doubts. The bottom 59 is represented as marginal foliation, with hand attribution qualified.'}}

# Validate all deliverable content before publishing either final-named return.
required={'scan','reader','line_count','changes','decisions','inventory','doubts','notes','check_events','notation','abbreviations','hand_log','audit_boxes','crops','unresolved','coverage'}
assert required <= result.keys()
assert {d['id'] for d in D}=={'M0599','M0600','M0601'}
assert all(i['transcribed']=='yes' for i in inventory)
assert all(type(c['against_C']) is bool and type(c['against_H']) is bool for c in changes)
assert len({c['id'] for c in changes})==len(changes)
assert len({a['box'] for a in audit})==len(audit)
for c in result['crops']:
    assert (ROOT/'edition'/c['file']).is_file(), c['file']
for a in audit:
    assert 0<=a['x0']<a['x1']<=1685 and 0<=a['y0']<a['y1']<=2358, a
assert r'\margin{59}' in tex and r'\mspage{' not in tex
assert not result['check_events']
# A literal-body brace check, ignoring escaped delimiter braces.
body=re.sub(r'\\[{}]', '', tex)
level=0
for c in body:
    if c=='{': level+=1
    elif c=='}': level-=1
    assert level>=0
assert level==0
OUT.mkdir(parents=True,exist_ok=True)
for suffix,content in [('tex',tex),('json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')]:
    p=OUT/f'150_scan060.{suffix}'
    t=p.with_name(p.name+'.tmp')
    t.write_text(content,encoding='utf-8')
for suffix in ['tex','json']:
    p=OUT/f'150_scan060.{suffix}'
    os.replace(p.with_name(p.name+'.tmp'),p)
print(json.dumps({'scan':'060','changes':len(changes),'decisions':len(D),'inventory':len(inventory),'doubts':len(doubts),'audit_boxes':len(audit),'crops':len(boxes),'packet_differences':diffs,'validated':True}))
