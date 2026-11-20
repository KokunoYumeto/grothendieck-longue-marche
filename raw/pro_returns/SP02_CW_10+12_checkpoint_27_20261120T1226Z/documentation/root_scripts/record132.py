from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,132);ch=r.change
pa=r'p\rlap{q}as'
diff=r'diff\unsure{\rlap{a}é|é}rence'
cont=r'cont\rlap{a}rainte'
trouv=r'\rlap{f}t\rlap{o}rouver'
arrow=r'\unsure{\rightharpoondown|\rightarrow|-}'
r.edit(r'\unsure{\times|x}',r'\unsure{x|\times}')
r.edit(r'\unsure{\rightarrow|-}',arrow)
r.edit(r'\unsure{autres)}','autres')
r.edit("pas de différence",pa+' de '+diff)
r.edit(r"d'une $\otimes$",r"d'une $\unsure{\otimes|\Omega}$")
r.edit(r'cont\deleted{\unsure{m|n}}rainte',cont)
r.edit(r'\unsure{trouver|frouver}',trouv)
r.edit('besoin):sur',r'besoin)\unsure{;|:}sur')
r.edit(r'\unsure{donc}','donc')
r.edit(r'de $\Delta$).',r'de $\Delta$\unsure{]|)}.')
old=r'$\Delta_{U}$ \inserted{i.e. $A$} non'
new=r'''\begin{tikzpicture}[baseline=(du.base),x=1cm,y=1cm]
\node[inner sep=0] (du) at (0,0) {$\Delta_U$};
\node[anchor=west,inner sep=0] at (.52,0) {non};
\node[anchor=south,inner sep=0] at (.92,.31) {\inserted{i.e. $A$}};
\draw (1.65,.3) .. controls (.8,.05) and (.65,.35) .. (.38,.2) -- (.65,-.4);
\end{tikzpicture}'''
r.edit(old,new)
ch('deleted e in first qu-il',r"qu\deleted{e}'il","qu'il",r"qu\deleted{e}'il",'The small e bowl and bar remain under an x strike between u and the apostrophe.','que','deletion state')
ch('first capital C','C',r'\underline{C}','C','The capital has a single open curve and no separate underline.','C','misread symbol or index','high',False,True,False,True)
ch('clipped first contrainte',r'\unsure{contrainte}','contrainte',r'\unsure{contrainte}','The right edge preserves contrai and the left part of the following n; te starts the next line. The clipped n prevents removing C uncertainty.','contrainteedge; contraintejoin','misread word','medium',False,True)
ch('qutres','qutres','autres','qutres','The first letter has a closed q bowl and a descending right stem with bottom foot.','qutres','misread word')
ch('colon before GxG',':','omitted',':','Two distinct vertically aligned round dots precede the first G.','GxG','omission')
ch('GxG middle glyph',r'\unsure{\times|x}',r'\times',r'\unsure{x|\times}','The crossed diagonals have typewriter serifs and x-height. Literal x is favored, while the multiplication-sign interpretation remains an alternative.','GxG','misread symbol or index','medium',True,True,False,True)
ch('arrow before first k',r'\unsure{\rightarrow|-}',r'\to',arrow,'The blue horizontal stroke ends in one short lower barb; no upper barb is visible. A right lower harpoon is favored, with complete arrow and dash retained as alternatives.','arrowk','misread symbol or index','medium',True,True,False,True)
ch('faint superscript in H2',r'\unsure{*|\prime}','*',r'\unsure{*|\prime}','The pale raised group contains a curved upper mark and lower remnants; it cannot be resolved to a complete star or a prime. The clear star on the previous line is not used to complete this one. C alternatives retained.','H2','misread symbol or index','low',False,True,False,True)
ch('geometrically insertion placement','before nul','after cyclique','before nul','The typewritten insertion lies directly above est nul, before the parenthesized example.','geomet; H2; cancel','insertion or placement','high',False,True,False,True)
ch('missing comma at clipped contraintes','no comma','comma','no comma','The page edge cuts through the final s. No following comma is visible and none is supplied.','contraintesedge','text not on the page')
ch('autres and absent closing parenthesis',r'\unsure{autres)}','autres)','autres','The final s is identifiable at the page edge; the area after it is outside the surviving page. No closing parenthesis is visible.','autresedge','text not on the page','high',True,True)
ch('pas second letter','pas','pas',pa,'The a bowl and rightward baseline foot coexist with a q descender extending below the line. Both unlike letter forms are retained.','pasdiff; pasaq','misread word','high',True,True)
ch('difference accented cell','différence','différence',diff,'The é cell has a closed lower loop and extra right stem, favoring an a/é overlap; plain é remains possible. The weak preceding f still has its upper hook and crossbar.','pasdiff; difffine','misread word','medium',True,True)
ch('typed tensor sign',r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}','A rounded upper contour and x-shaped crossing descend to a flat divided foot. The Omega-like reading is retained as an alternative.','tensor','misread symbol or index','medium',True,True,False,True)
ch('canceled cell after bialgebre',r'\deleted{\unsure{s}}','omitted',r'\deleted{\unsure{s}}','The raised x cancellation and indistinct lower curves are visible above the following comma. The underlying letter is not secure; C qualified s is retained.','bialg; bialgfinal','deletion state','low',False,True)
ch('contrainte overlapping cell',r'cont\deleted{\unsure{m|n}}rainte','contrainte',cont,'The cell has an a lower bowl and right foot together with an r stem and right shoulder. It is an unlike-letter overlap, not a separately canceled m/n followed by r.','contrainte2; contcell','misread word','high',True,True)
ch('trouver first two cells',r'\unsure{trouver|frouver}','trouver',trouv,'The first cell combines a high f hook with the t rightward bottom curl. The second combines an r stem/shoulder with a closed o oval. Both raw overlaps are retained without a typing-order claim.','trouver; troufirst','misread word','high',True,True)
ch('punctuation after besoin)',':','omitted',r'\unsure{;|:}','A dark upper dot stands over a pale lower mark with a descending tail. Semicolon is favored, but the weak lower impression also permits colon.','colon; colonfine; colonactual; colonfull','misread symbol or index','medium',True,True)
ch('handwritten donc',r'\unsure{donc}','donc','donc','The initial looped d and ascender are followed by a small o, extended n and open c. C doubt resolved.','hand1b; doncfine','misread word','medium',True,False)
ch('first non in handwritten note','non commutatif','commutatif','non commutatif','Three small n/o/n strokes stand between Delta-U and commutatif, below the insertion leader. They are separate from the leader and remain live.','handdelta; handnon','omission','high',False,True,False,True)
ch('inserted i.e.A leader','text insertion only','bracketed text','text insertion with curved leader','The i.e. A is above a curved horizontal stroke that turns down between Delta-U and non. The stroke is reproduced with its long upper curve and descending left end.','handdelta; insertrot','drawing or diagram','high',True,True)
ch('tiny interlinear annotation',r'\unsure{vu!|u.!}','omitted',r'\unsure{vu!|u.!}','Two compressed letter-like groups, a point and a long oblique terminal stroke remain visible above the end of commutatif. Enlargement and slight rotation do not settle C alternatives.','tiny; tinyrot','omission','low',False,True)
ch('closing handwritten delimiter',')',') followed by editorial ]',r'\unsure{]|)}','The visible sign has a long nearly straight shaft, angular top and hooked lower return; a square bracket is favored over a rounded parenthesis. Only one delimiter is present before the period.','hand3; endbracket; firstbracket','misread symbol or index','medium',True,True)
for a,b,c,d,e in [
 ('first contrainte','contrainte','','medium','Clipped final n at the right edge; following te is visible.'),
 ('GxG middle sign','x',r'\times','medium','Typed serifed diagonals.'),
 ('hand arrow',r'\rightharpoondown',r'\rightarrow; -','medium','Only lower terminal barb visible.'),
 ('H2 faint superscript','*',"prime",'low','Faint disconnected raised strokes.'),
 ('difference accented cell',r'\rlap{a}é','é','medium','Closed lower loop and extra right stem.'),
 ('typed tensor',r'\otimes',r'\Omega','medium','Crossed round upper contour and flat divided foot.'),
 ('canceled bialgebre ending','s','','low','Underlying curves largely hidden by x cancellation.'),
 ('punctuation after besoin)',';',':','medium','Pale lower mark has a possible comma tail.'),
 ('tiny hand annotation','vu!','u.!','low','Compressed letter-like marks and oblique ending.'),
 ('final hand delimiter',']',')','medium','Straight shaft and hooked return; opening delimiter is rounded.')]:r.doubt(a,b,c,d,e)
r.notation('typed plain capitals','C,U,G,H','10:132 C in opening; U after sss; G after dire, both G in product, G in cohomology, G before cyclique; H in H2')
r.notation('typed lower k','k','10:132 target of product arrow; cohomology argument; canceled algébriquement phrase; extension; characteristic clause')
r.notation('product sign',r'\unsure{x|\times}','10:132 GxG','uncertain')
r.notation('hand arrow',arrow,'10:132 GxG to k','uncertain')
r.notation('raised hand stars',r'first *; second \unsure{*|\prime}','10:132 first target k and H2 argument respectively','uncertain')
r.notation('hand symmetry signs',r'\sigma','10:132 non nul de; bottom existence de')
r.notation('typed tensor',r'\unsure{\otimes|\Omega}','10:132 category example','uncertain')
r.notation('hand note objects',r'\Delta_U, A, U, \Delta','10:132 first Delta with lower U; inserted A; second-line U; final Delta')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:132 '+c) for a,b,c in [('sss','si et seulement si','opening'),('car.','caractéristique','middle'),('n°','numéro','hand note'),('i.e.','id est','hand insertion')]]
r.r['inventory_overrides']={'132-04':dict(first_words_or_objects='uncertain lower-right harpoon / arrow / dash; first hand star'),'132-09':dict(kind='text',first_words_or_objects='a/r unlike-letter overlap inside contrainte'),'132-10':dict(first_words_or_objects='Avec les notations du n° 11, il faudra donc Delta-U non commutatif; U non commutatif; final bracket/parenthesis uncertain'),'132-11':dict(first_words_or_objects='i.e. A above first Delta-U/non with curved leader')}
extras=[('a/q overlap in pas','text','middle, pas de différence','typewriter'),('uncertain a/é overlap in différence','text','middle','typewriter'),('f/t and o/r overlaps in trouver','text','penultimate typed line','typewriter'),('curved insertion leader','drawing','above and after Delta-U in hand note','his hand'),('uncertain semicolon/colon','text','last typed line after besoin)','typewriter')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:132',sheet_kind='typescript',hand=h,element=f'132-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops132.json').read_text())
r.r['inspection_note']='Root alone viewed the whole scan and both halves before C/H, all10 C doubts and all13 C inventory rows. All48 crop recipes were actually viewed, including the initially truncated crops viewed again, the fine unlike-letter cells, every mathematical sign and the slight rotations of both tiny additions. Both halves were reread line by line before finalization. All10 C doubts received explicit decisions. The archival lower-left131 remains solely an archive comment. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record132.json')
