import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,43);ch=r.change
r.edit(r'\unsure{fausse|faux}',r'\unsure{tasser}')
r.edit(r'\mathbb{S}',r'\unsure{\mathbb{S}|S}',count=2)
r.edit(r'\unsure{p\'_*|q\'_*}'.replace('\\\'','\''),r'\unsure{q\'_*|p\'_*}'.replace('\\\'','\''))
r.edit(r'\unsure{*|\times}','*')
r.edit('se factorise à',r'se \unsure{factorise|favtorise} à')
r.edit(r'Corollaire 11\handwritten{.}2',r'Corollaire 11\handwritten{\unsure{.|/}}2')
ch('manuscript number','11','omitted','11','Two tall separate pen strokes.','number','omission')
for p,crop in [('section heading','top'),('11.0 heading','top'),('lemma heading and opening','lemma'),('lemma assertion and cases a-c','lemma'),('corollary','corollary')]:
 ch(p,'underlined, short dash where present','bold heading or no underline; long dash','underlined, short dash where present','Continuous rules beneath the corresponding lines; short typed hyphens in numbered headings.',''+crop,'other')
ch('algebra notation at definition',r'\unsure{\mathcal{A}|a}',r'\mathcal{A}',r'\unsure{\mathcal{A}|a}','Low rounded bowl with returning upper curl resembles a; distinction from calligraphic A remains unresolved.','top','misread symbol or index','medium')
for p,crop in [('tensor base S','S1'),('Y-prime product S-prime','S2')]:
 ch(p,r'\mathbb{S}','S',r'\unsure{\mathbb{S}|S}','Doubled contours and a heavy central stroke are visible; retracing versus intended alphabet cannot be separated from this ink.',''+crop,'misread symbol or index','medium',True,True)
ch('upper right marginal instruction',r'\unsure{fausse|faux} Formule',r'\uncertain{fausse} formule',r'\unsure{tasser} Formule','Upright crop shows a single crossed initial t, a, two pointed s strokes, then a small e and rising terminal r; second word begins with a large looped F. The first word remains marked doubtful.','margin-word','misread word','medium',True,True,True,True)
ch('marginal enclosures','two TikZ ellipses','circles described in note','two TikZ ellipses','Broad open pen loops enclose each marginal note.','lemma; margin-formula','drawing or diagram')
ch('lower right marginal formula',r'f_*(\underline{O}_X)',r'f_*(\mathcal{O}_X)',r'f_*(\underline{O}_X)','Round upright O with a separate underline beneath it, then subscript X.','margin-formula','misread symbol or index')
for p,crop in [('small hook below lemma title','lemma'),('curved stroke under tensor base','lemma'),('curved stroke under f-star in c','lemma'),('angular mark above d-un','proof2')]:
 ch(p,'TikZ mark','omitted','TikZ mark','The pen mark is separate from the adjacent letters and is represented by its visible geometry.',crop,'drawing or diagram')
ch('end of Spec expression',r'X\unsure{)}','X),',r'X\unsure{)}','Closing curved stroke is clipped into the black right edge; no comma is visible.','right-edge','other','low')
ch('factorise', 'factorise','factorise',r'\unsure{factorise|favtorise}','Third letter has a dark lower bowl and overlapping right stroke, allowing c or v; no lexical correction imposed.','factorise','misread word','medium',True,True)
ch('cancelled sur',r'\deleted{sur}',r'\struck{\ill{}}',r'\deleted{sur}','Typed s-u-r remain visible beneath the horizontal cancellation.','proof2','readable ink left as \\ill{}','high',False,True,True)
ch('punctuation before Ou','semicolon','.','semicolon','Two dark components at different heights, the lower one extending down; a handwritten O precedes the typed u.','punct','misread symbol or index','medium')
ch('cancelled display operator',r'\deleted{\unsure{p\prime_*|q\prime_*}}',r'\struck{\ill{}}',r'\deleted{\unsure{q\prime_*|p\prime_*}}','A typed round bowl with right descender and bottom serif favours q. Prime and star are obscured by diagonal hatching; the whole operator remains doubtful.','cancelled','readable ink left as \\ill{}','low',True,True,True)
ch('third g-prime exponent',r'\unsure{*|\times}','*','*','Three intersecting strokes give six rays, including a short leftward middle ray; not just two crossing diagonals.','star','other','high',True,False)
ch('added definition of p-prime','ou','où','ou','The rounded o and u have no accent above them.','proof2','abbreviation expanded or spelling modernised')
ch('corollary number separator','handwritten dot','. ',r'\unsure{.|/}','Heavy low dot is connected to a long rising diagonal stroke. A dot correction or slash-shaped separator cannot be distinguished.','corollary','misread symbol or index','medium',True,True)
for p,rd,alt,co in [('algebra notation',r'\mathcal{A}','a','medium'),('two retraced S letters',r'\mathbb{S}','S','medium'),('marginal instruction','tasser','','medium'),('clipped parenthesis',')','','low'),('factorise','factorise','favtorise','medium'),('cancelled operator',r'q\prime_*',r'p\prime_*','low'),('corollary number separator','.','/','medium')]:r.doubt(p,rd,alt,co)
r.r['crops']=json.loads(Path('work/crops043.json').read_text())
for n,b,s in [('cancelled',[583,1438,743,1498],6),('star',[1141,1428,1206,1493],6),('S1',[677,389,732,433],5),('S2',[308,803,347,853],5),('right-edge',[1581,753,1666,798],5),('punct',[1008,1217,1094,1273],5),('factorise',[720,1091,901,1138],5)]:r.crop(n,b,scale=s)
r.notation('retraced capital S',r'\mathbb{S} | S','10/043 tensor base and base change','ambiguous')
r.notation('asterisk exponent','*','10/043 third g-prime exponent: six rays','read')
r.r['inspection_note']='Whole page then both halves read, all prose and displayed indices checked; all C doubts enlarged, all marginal and cancelled ink inspected, upper margin note rotated upright. C inventory matched, including small pen marks. Agreed p:G and X-préschémas retained as printed. No mathematics repaired.'
r.save('work/record043.json')
