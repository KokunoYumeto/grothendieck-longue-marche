import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\unsure{pr|pour}','pr'),(r'\unsure{la|le}',r'\unsure{la|le|th}'),('Schéma de Hilbert','Schémas de Hilbert'),(r'\unsure{Appendice|Appendix}','Appendice'),(r'\mathrm B}\arrow[ddr]\arrow[ddrrrr]',r'\mathrm B}\arrow[ddr]\arrow[ddrrrr,thick]'),(r'\mathrm C}\arrow[ddl]\arrow[ddrr]',r'\mathrm C}\arrow[ddl,dashed]\arrow[ddrr,thick]'),(r'\mathrm D}\arrow[dr]',r'\mathrm D}\arrow[dr,thick]'),(r'execute before arrows={',r'''execute before arrows={
\draw[thin] ([xshift=-5em,yshift=-2em]\tikzcdmatrixname-3-4.west) -- ++(0,.12em);'''),('% Paper watermark, sideways.',r'''% Detached ink traces below and to the left of the appendix; no character assigned.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,.22)--(.07,.25)--(.11,.23);\fill (.15,.42) circle (.012);
\draw (1.20,0)--(1.19,.10)--(1.22,.14);
\end{tikzpicture}}
% Paper watermark, sideways.''')]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no'):
 L.append(dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh))
a('upper-left cancelled word',r'\unsure{Pbs|Plan|Pl.}','gribouillis',r'\deleted{\unsure{Pbs|Plan|Pl.}}','corner: an upper loop and long P stem survive, with two small crossed bodies to the right; the diagonal hatching prevents a secure ending.','low',False,True,'omission')
for line in [1,2]:a(f'line {line}, before les',r'\unsure{pr|pour}','pour','pr',f'line{line}: one long descending p joins directly to a short nearly horizontal r; there are no separate o and u bodies.','medium',True,True,'abbreviation expanded or spelling modernised')
a('line 2, name',r'\unsure{Matsusaka}','Matsusaka',r'\unsure{Matsusaka}','name/line2: M, the small a spot, a high t stroke and final k-a are visible, but the very flat central s/u/s strokes are compressed. The named reading remains explicitly uncertain.','medium',False,True,'misread word')
for line in [2,3]:a(f'line {line}, abbreviation','Th','Th.','Th',f'line{line}: no detached dot follows h; the gap before de is clean.',k='text not on the page')
a('line 3, cancelled word',r'\unsure{la|le}','th',r'\unsure{la|le|th}','old3: a heavily retraced tall first loop and a zigzag second body survive; neither the last vowel nor a possible t-h sequence can be established. th is retained as an additional alternative, not silently substituted.','low',True,True,'misread word')
a('line 3, quotation marks','double raised strokes','guillemets','double raised strokes','line3: two short upright marks stand at both ends of courbe générique.',k='misread symbol or index')
a('line 4, first word','Schéma','Schémas','Schémas','lines45: a separate small curved terminal s follows the dark a body before the gap to de.','high',True,False)
a('line 4, old wording',r'\unsure{sur propre|propre}',r'\ill{}',r'\deleted{\unsure{sur propre|propre}}','old4: an initial curled group may read sur, followed by a long p descender and r-o-p-r-e remnants under a horizontal cancellation. The exact initial group remains doubtful.','low',False,True,'readable ink left as \\ill{}',mh='yes')
a('line 5, quotation marks','double raised strokes','guillemets','double raised strokes','lines45: small paired vertical strokes enclose diviseur Θ.',k='misread symbol or index')
a('diagram C to H shaft','continuous','continuous','broken/dashed shaft','CtoH: the short arrow descends separately to H with several clear white gaps in its shaft; the neighbouring uninterrupted longer line is a page cancellation.','high',True,True,'drawing or diagram')
a('diagram arrow weights','all shafts same weight','note identifies B–G, C–G, D–F as thicker','B–G, C–G and D–F thicker','diagram: these three arrows have visibly broader dark strokes and heads than B–H, E–F, F–G, H–I and G–I.','high',True,False,'drawing or diagram')
a('diagram vertical placement','F above H/G','F on same row as H/G; note says three rows','F above H/G, I below','diagram: F is centred near y1195, H/G near y1330, I near y1520; the top row is near y1030. The drawing therefore has four levels.','high',False,True,'insertion or placement')
a('detached left mark','omitted','omitted','tiny vertical stroke left of H/I gap','strayleft: a distinct short black upright trace stands by itself near x233,y1425. Reproduced as a stroke without assigning a numeral.','medium',True,True,'omission')
a('below appendix, left traces','omitted','omitted','small dash, dot and curved upright trace','straybottom: isolated dark traces near x355 and x520 are reproduced as unlabelled ink marks.','medium',True,True,'omission')
a('appendix heading',r'\unsure{Appendice|Appendix}','Appendice','Appendice','appendix: after the dotted i there are low curved c/e strokes and no pair of crossed diagonals for x.','medium',True,False)
a('appendix letter',r'\mathcal L','L',r'\mathcal L','appendix: a tall looped ascender continues through a large lower loop to a long rightward foot, distinctly cursive against the upright diagram capitals.','medium',False,True,'misread symbol or index')
a('watermark','VELIN EXTRA P.J','omitted','VELIN EXTRA P.J','watermark_readable: a 90-degree rotation without reflection makes the outlined capitals upright; VELIN EXTRA and P.J are individually visible across the sheet. The earlier trial with reflection was upside down.','medium',False,True,'omission')
I=[]
def i(k,p,t,h='his hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('marginnote','upper left','cancelled Pbs/Plan/Pl.')
i('deletion','upper left','dense hatching through the short word')
for p,t in [('line1','Th. de finitude pr les schémas de Hilbert'),('lines2–3','Th de Matsusaka pr les automorphismes d’une variété polarisée'),('line4','Th de la [old la/le/th] "courbe générique" [pour Picard]'),('line5','Schémas de Hilbert d’une courbe [old sur propre/propre] sur S.'),('line6','Picard des courbes sur S ["diviseur Θ" etc ?]'),('line7','Picard d’un schéma propre non projectif sur k'),('lines8–9','Picard d’un S-schéma projectif à fibres réductibles [p.ex. cas d’une courbe sur S]')]:i('text',p,t)
i('deletion','third item','old la/le/th, independently cancelled')
i('deletion','fourth item','old sur propre/propre, horizontal cancellation')
i('deletion','first five text lines','five short diagonal strokes across two groups of items')
i('deletion','whole sheet','four long thin diagonal cancellation strokes')
i('diagram','lower half','A wavy arrow toward B; B to H/G; C broken arrow to H and thick arrow to G; D to F/J; E to F; F to G; H/G to I; K isolated')
i('drawing','across diagram','four long cancellation strokes retained separately from arrows')
i('drawing','left of lower diagram','short isolated vertical ink mark')
i('drawing','under diagram','long horizontal rule')
i('text','below rule','cursive L; Appendice : Pbs ouverts.')
i('drawing','lower left below appendix','two small ink traces and detached dot')
i('marginnote','vertical through page','VELIN EXTRA P.J','paper watermark')
commit(26,8,dict(replace=R,changes=L,inventory=I,sheet_kind='cancelled_draft',hand='his hand',observations='Whole then both supplied halves viewed before C/H; every agreed word, accent, abbreviation, capital, bracket and diagram edge read. All C doubts and disagreements enlarged. C superseded words remain uncertain where hatching hides letters. The whole-page cancellation is already explicitly stated in H, so absence of H struck macros alone is not counted as a substantive difference. Plain upright diagram capitals and cursive L distinguished. Every crop in crop26_008.py viewed; watermark orientation corrected by a final unreflected 90-degree rotation. Archive7 is a comment only. Context unopened.'))
