import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,46);ch=r.change
r.edit(r'sur $S$ tel que',r'sur $S$\handwritten{,} tel que')
r.edit(r'\unsure{X}',r'X')
r.edit(r'\unsure{\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}',r'\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})')
r.edit(r'\mathbb{S}',r'\unsure{\mathbb{S}|S}',2)
def picture(text,path):
 return r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=(n.base)]\node (n) at (0,0) {'+text+r'};\draw '+path+r';\end{tikzpicture}'
r.edit(r"\handwritten{Notons qu'}",r'\handwritten{'+picture("Notons qu'",r'(-1.15,-.15)--(-1.05,.28)--(-.95,-.02)')+'}')
end=r'\operatorname{End}_{\mathcal{O}_{\unsure{\mathbb{S}|S}}}(\unsure{\mathbb{W}|W}(\mathcal{E}))'
r.edit(r'\inserted{\handwritten{'+end+'}}',r'\inserted{\handwritten{'+picture('$'+end+'$',r'(-1.45,-.22)--(-.65,-.22) .. controls (-.4,-.22) and (-.35,-.45) .. (0,-.45) .. controls (.3,-.45) and (.35,-.25) .. (.65,-.25)--(1.5,-.25)')+'}}')
r.edit(r'\handwritten{et seulement si}',r'\handwritten{'+picture('et seulement si',r'(-1.25,-.75) .. controls (-1.5,-.2) and (-1,-.3) .. (1.3,-.28)--(1.3,-.02)')+'}')
r.edit(r'\handwritten{alors}',r'\handwritten{'+picture('alors',r'(-.6,-.25) .. controls (-.6,.05) and (-.25,.2) .. (-.1,.55) .. controls (-.05,.12) and (.6,.3) .. (.6,-.2)')+'}')
r.edit(r'\inserted{\handwritten{\mathcal{E}\longrightarrow}}',r'\inserted{\handwritten{'+picture(r'$\mathcal{E}\longrightarrow$',r'(-.7,.15) .. controls (-.95,-.4) and (-.45,-.35) .. (-.15,-.35)--(.75,-.2)--(.75,.1)')+r'\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--(0,-.38);\end{tikzpicture}}}')
r.edit(r'\handwritten{plat et}',r'\handwritten{'+picture('plat et',r'(-.6,-.75) .. controls (-1,-.15) and (-.2,-.25) .. (.65,-.18) .. controls (.9,-.1) and (.9,0) .. (.9,.1)')+'}')
ch('manuscript number','14','omitted','14','Tall initial 1 and sharply angled 4 at upper left.','number','omission')
ch('opening comma after S','omitted',',',r'\handwritten{,}','A pale curved descending comma between typed S and tel.','comma','omission','high',True,False)
ch('first A alphabet',r'\unsure{\mathcal{A}|a}',r'\mathcal{A}',r'\unsure{\mathcal{A}|a}','Rounded bowl and upper retracing do not distinguish a formal calligraphic capital from lowercase a.','opening','misread symbol or index','medium')
ch('End base S',r'\mathbb{S}','S',r'\unsure{\mathbb{S}|S}','The S has two dark lower curves, compatible with double stroke or retracing.','opening','misread symbol or index','medium',True,True)
ch('End W alphabet',r'\unsure{\mathbb{W}|W}',r'\mathbb{W}',r'\unsure{\mathbb{W}|W}','Several close parallel strokes form the left part of W; dark reinforcement prevents certain alphabet attribution.','W','misread symbol or index','medium')
ch('cancelled Hom formula',r'\unsure{\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})}',r'\ill{}',r'\mathcal{H}om_{\mathcal{O}_S}(\mathcal{E},\mathcal{E})','Hom, a round subscript O with S below, opening and closing parentheses and two curled E forms survive the diagonal hatching.','deletedHom','readable ink left as \\ill{}','medium',True,True,True)
ch('first square old X',r'\deleted{\unsure{X}}','omitted',r'\deleted{X}','Serifed crossing diagonals of typed X remain beneath the heavier handwritten V.','X','omission','high',True,True)
for place,crop in [('first square','diagram1'),('first triangle','diagram2'),('CM1 square','CM1'),('CM2 triangle','CM2')]:
 ch(place+' closing text','oval and long leftward pointer','plain est commutatif.','oval and long leftward pointer','A closed pencil loop surrounds the typed phrase and a curved stroke points left beneath the diagram.',crop,'drawing or diagram')
for place,crop in [('first triangle','diagram2'),('CM2 triangle','CM2')]:
 ch(place+' isomorphism label',r'\sim',r'\simeq',r'\sim','Single undulating mark beside the rising left arrow, without a separate lower bar.',crop,'misread symbol or index')
ch('axioms introduction alors',r'\inserted{alors}','omitted',r'\inserted{alors}','Five letters written below revient, with joining enclosure directed to its following gap.','axioms','omission')
ch('rho target base S',r'\mathbb{S}','S',r'\unsure{\mathbb{S}|S}','S has a heavily doubled lower bowl, which may be a retrace.','axioms','misread symbol or index','medium',True,True)
ch('left margin enclosure','TikZ enclosure','unenclosed formula','TikZ enclosure','Closed irregular loop surrounds E arrow A(G) tensor E.','margin','drawing or diagram')
ch('deleted reference',r'\unsure{(Exp. I)}',r'\ill{}',r'\unsure{(Exp. I)}','Opening curve and final serifed I are distinct; the central letters are partly covered by close diagonal hatching.','reference','readable ink left as \\ill{}','low',False,True,True)
ch('replacement reference abbreviation',r'\unsure{compar|comparer}','comparer',r'\unsure{compar|comparer}','The word ends in short connected strokes; compar is visible but a full er ending cannot be separately established.','reference','abbreviation expanded or spelling modernised','medium')
ch('replacement reference number',r'\unsure{4|9}.2','4.2',r'\unsure{4|9}.2','First digit has a hooked upper loop and long right descender; its open/closed junction remains ambiguous.','reference','misread symbol or index','medium')
for place,word,crop in [('heading','11.6.','opening'),('definition','opération','opening'),('lemma','Lemme','bottom')]:
 ch(place+' underline',r'\uline{'+word+'}','bold or italic '+word,r'\uline{'+word+'}','Separate pen line beneath the letters; the word itself is typed.',crop,'other')
for i,(place,shape,crop) in enumerate([
 ('Notons qu’','pale caret before replacement','opening'),('End formula','shallow lower brace with central dip','opening'),('et seulement si','lower bracket with left hook to insertion gap','opening'),('alors','inverted enclosure directed to gap above','axioms'),('inserted E arrow','lower U-shaped enclosure and downward anchor','axioms'),('plat et','lower curved bracket extending to gap before tel','bottom')],46):
 ch(place+' insertion marks','omitted','omitted','TikZ '+shape,'Visible '+shape+'.',crop,'drawing or diagram','high',True,True)
 r.r['inventory_extra'].append(dict(scan='10:046',sheet_kind='typescript',hand='his hand',element=f'046-{i:02d}',kind='drawing',position=place,first_words_or_objects=shape,transcribed='yes'))
for p,rd,alt,co in [('first A',r'\mathcal{A}','a','medium'),('End base S',r'\mathbb{S}','S','medium'),('W alphabet',r'\mathbb{W}','W','medium'),('rho target base S',r'\mathbb{S}','S','medium'),('cancelled reference','(Exp. I)','','low'),('replacement abbreviation','compar','comparer','medium'),('reference digit','4','9','medium')]:r.doubt(p,rd,alt,co)
r.r['crops']=json.loads(Path('work/crops046.json').read_text())
for n,b in [('comma',[1259,67,1310,112]),('W',[666,195,748,248]),('deletedHom',[753,191,1000,274]),('X',[462,689,493,723])]:r.crop(n,b,scale=5)
r.r['inventory_extra'].append(dict(scan='10:046',sheet_kind='typescript',hand='his hand',element='046-52',kind='insertion',position='opening after sur S',first_words_or_objects='comma',transcribed='yes'))
r.r['inspection_note']='Root viewed whole then both halves, read every line and all four diagrams, enlarged each C doubt, every H difference, all arrows and labels, margin and struck passages. Retained both Soient G, CM1 A(theta), upper-left A tensor A tensor A and lower-right A from visible ink. Inventory checked including insertion marks. No mathematical validation performed.'
r.notation('triangle isomorphism mark',r'\sim','10/046 first and CM2 triangles: one wave without lower bar')
r.save('work/record046.json')
