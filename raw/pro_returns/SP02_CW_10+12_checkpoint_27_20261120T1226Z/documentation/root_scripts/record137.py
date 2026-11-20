from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,137);ch=r.change
mp=r'\handwritten{\unsure{\mathrel{\vert\! -\!\vert}|\mapsto}}'
fi=r'\unsure{\rlap{m}fini|fini|mini}'
so=r's\unsure{\rlap{u}o|o}\rlap{n}ulevée'
en=r'en\rlap{f}visagëe'
r.edit(r'\handwritten{\mapsto}',mp)
r.edit(r'\unsure{fini|mini}',fi)
r.edit(r'=(M\otimes_{k}M)',r'=(M\rlap{\(M\)}\otimes_{k}M)')
r.edit(r'\unsure{soulevée|sonlevée}',so)
r.edit(r'\unsure{envisagëe|envisagée|enfisagëe|enfisagée}',en)
ins=r'''\begin{tikzpicture}[baseline=-.5ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.4) {\inserted{et sa duale est cocomplète,}};
\draw (.04,-.22) .. controls (.07,.18) and (.55,.22) .. (1,.2) -- (3,.2) .. controls (3.5,.2) and (3.5,-.05) .. (4.1,-.05) -- (6.1,-.05) .. controls (6.45,-.05) and (6.55,.15) .. (6.5,.25) -- (6.35,.25) -- (6.35,.45);
\end{tikzpicture}'''
r.edit(r'$k$\inserted{et sa duale est cocomplète,}','$k$,'+ins)
for loc,word,crop in [('heading','Corollaire','heading'),('corollary last word of line2','isomorphisme','isomend'),('quotient argument','surjective','surjective'),('last paragraph condition','pourvu que','pourvu')]:
 ch(loc,r'\uline{'+word+'}',r'\emph{'+word+'}',r'\uline{'+word+'}','A single continuous horizontal rule runs below this entire word or phrase. It is not italic type. The surrounding type is upright.',crop,'other')
ch('gap in induced homomorphism',r'(A\otimes_k A)\quad M\otimes_k M',r'(A\otimes_k A)\to M\otimes_k M',r'(A\otimes_k A)\quad M\otimes_k M','The wide gap after the closing parenthesis is blank. No shaft, arrowhead or erased arrow is visible. H supplies an arrow not present in the scanned area.','mapsource; blank; maptarget','text not on the page','high',False,True,False,True)
ch('canceled cell after target tensor',r'\deleted{\unsure{,|x}}','omitted',r'\deleted{\unsure{,|x}}','A full cancel x covers a dark lower mass with a faint hooked tail. The possible underlying comma cannot be separated securely from the strike; C doubt is retained.','cancelcomm; cancelcommfine','omission','medium',False,True)
ch('punctuation after isomorphisme',r'\uline{isomorphisme} Alors',r'\emph{isomorphisme}. Alors',r'\uline{isomorphisme} Alors','The final e and underline reach the right paper edge. No full stop is visible before that edge; none is supplied. This does not claim what might have lain outside the captured edge.','isomend','text not on the page','high',False,True)
ch('map sign between u and u.e',r'\handwritten{\mapsto}',r'\mapsto',mp,'A horizontal blue shaft has a clear left vertical bar. The right end is a narrow upright triangular lump with a downward stroke; two right-facing arrowhead arms are not separable. The visible impression is a shaft between two short vertical bars; a poorly resolved mapsto remains possible.','umap; umapfine','misread symbol or index','medium',True,True,False,True)
ch('rank letter above line',r'\inserted{n}','omitted',r'\inserted{n}','A typed n sits above the space between rang and de. Its shoulder and two feet are clear; no leader or cancellation is attached.','rankn','omission','high',False,True,False,True)
ch('fini first cell',r'\unsure{fini|mini}','fini',fi,'The tall hooked f and its crossbar are visible together with lower vertical/curved strokes. An m/f overprint is favored, but the underlying m is not fully separable. The following dotted i, n and dotted i are clear. C uncertainty is refined rather than removed.','fini; finifine','misread word','medium',True,True)
ch('extra M under tensor in NB',r'(M\otimes_k M)',r'(M\otimes_k M)',r'(M\rlap{\(M\)}\otimes_k M)','Between the first and last M, the tensor cell carries another full-height M impression: its two upper serifs and right stem stand above/behind the smaller O/x tensor construction. Both impressions are retained without assigning a typing chronology.','NBformula; NBmiddle; NBmiddlefine','misread symbol or index','high',True,True,False,True)
ch('soulevée overprinted cells',r'\unsure{soulevée|sonlevée}','soulevée',so,'The third cell has both an upper n shoulder and a lower u bowl. The second closed o has an extra left top bar and right foot resembling a u overprint, which remains qualified. The l, e, v, acute e and final e are clear. The C alternatives alone do not preserve these overlapping impressions.','soulevee; souleveefine','misread word','medium',True,True)
ch('envisagée overprint and accent',r'\unsure{envisagëe|envisagée|enfisagëe|enfisagée}','envisagée',en,'The third cell contains both the hooked ascender/crossbar of f and the two oblique legs and foot of v. Above the penultimate e are two separate upright dot-like strokes, not an acute diagonal. The raw overlap and diaeresis are retained; C doubt is resolved.','envisagee; envisageefine','misread word','high',True,True)
ch('comma after finite over k','$k$ followed immediately by insertion','$k$, followed by insertion','$k$, followed by insertion','A black low comma with descending tail is present after k, beside the blue start of the insertion leader. C omits that typed comma.','kfini; insertdual','omission','high',True,False)
ch('leader of dual cocompleteness insertion','inserted words only','added words only','inserted words with curved leader','The typed insertion stands above the line. A blue curve starts after k, passes under its first words, descends gently over the following base line and curls up at the right into a short bent end. Text and leader are reproduced together in TikZ.','insertdual; cocomplete','drawing or diagram','high',True,True)
ch('canceled a before apostrophe',r"l\deleted{a}'algèbre","l'algèbre",r"l\deleted{a}'algèbre",'The a bowl and right stem remain under the typed x between l and the apostrophe. H omits this canceled letter. The passing blue insertion leader is separate.','ladelete','deletion state','high',False,True)
r.doubt('canceled cell after target tensor',',','x','medium','Underlying low comma-like mass cannot be isolated from cancellation.')
r.doubt('map sign u to u.e',r'\mathrel{\vert\! -\!\vert}',r'\mapsto','medium','Right endpoint is a compact upright triangular lump with a descending stroke.')
r.doubt('fini first cell',r'\rlap{m}fini','fini; mini','medium','f clear; lower strokes favor m/f overlap but m is incompletely exposed.')
r.doubt('second cell of soulevée',r'\rlap{u}o','o','medium','Closed o with extra upper-left bar and lower-right foot; adjacent n/u overlap is clear.')
r.notation('typed tensor construction',r'\otimes: O with an x overstrike','10:137 initial map; induced source and target; rank tensors; NB all four tensor positions; barred-M product; barred-e tensor x; tensor-categories')
r.notation('hand arrows and base coproduct',r'\longrightarrow; \Delta_A; qualified mapsto','10:137 initial M map; induced source subscript (A,Delta_A); u map with qualified right endpoint','uncertain')
r.notation('rank equality and inequality',r'n^2; n=n^2; n(n-1)=0; n\ne0; n=1','10:137 proof; raised 2s; minus and both equality bars; hand diagonal slash through final equality')
r.notation('hand bars',r'\bar M six times; \bar e twice','10:137 quotient paragraph; horizontal strokes above each M/e individually enlarged')
r.notation('math alphabets and subscripts','M,A,B,n,k,e,x; (A,Delta_A); (A tensor_k A)','10:137 every displayed/inline occurrence; plain capitals, lowered k/A, raised 2; no hidden underline under letters')
r.notation('unlike typewriter overlaps',r'possible m/f; M/tensor; possible u/o and clear n/u; f/v','10:137 fini; NB middle; soulevée; envisagëe','uncertain')
r.r['abbreviations']=[dict(abbreviation='NB',expansion='nota bene',attestations='10:137 quotient identity'),dict(abbreviation='i.e.',expansion='id est',attestations='10:137 rank argument and last paragraph')]
r.r['inventory_overrides']={'137-12':dict(hand='typewriter',first_words_or_objects='et sa duale est cocomplète, typed interlinear insertion with hand leader')}
extras=[('four underlines','text','heading; isomorphisme; surjective; pourvu que','typewriter'),('possible m/f overprint in fini','text','rank paragraph','typewriter'),('M under tensor in NB','text','quotient identity','typewriter'),('u/o possible and n/u clear overlaps','text','soulevée','typewriter'),('f/v overlap and diaeresis','text','envisagëe','typewriter'),('curved insertion leader','drawing','beneath et sa duale est cocomplète','his hand')]
for i,(s,t,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:137',sheet_kind='typescript',hand=h,element=f'137-R{i:03d}',kind=t,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path('work/'+p).read_text()) for p in ['crops137.json','crops137_extra.json']],[])
r.r['inspection_note']='Root alone viewed whole137 and both actual supplied halves before C/H, all4 C doubts and all13 inventory rows. All56 crop recipes (49 whole-source and7 supplied-a) were actually viewed; ranktensor,n2,equalnsquare,nn1 from a truncated output were re-viewed and only then counted. All mathematical letters, tensor signs, indices, equalities, inequality, arrows, bars, all cancel/insertion regions and C doubts were enlarged. There is no slanted verbal note; the horizontal interlinear insertion and its curved leader were read upright. Both actual supplied halves were reread line by line before finalization. Each C doubt has an explicit decision. H section/note after this page concerns following unselected pages138–139 and is outside this page boundary, not a supposed omission in this page. Archive136 is retained only as a comment. Context remains sealed; no OCR, parallel transcription, audit or mathematical checking occurred.'
r.save('work/record137.json')
