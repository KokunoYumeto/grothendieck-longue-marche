import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\handwritten{\mspage{33}}',r'\mspage{\handwritten{- 33 -}}'),(r'connex\unsure{e},','connex'),(r'défini\unsure{es}','défini'),(r'ens\unsure{em}ble','ens% right edge clips the rest of this line; no em survives\nble'),('2) Lorsque',r'\handwritten{2)} Lorsque'),(r'\unsure{\mathbb{R}|R}',r'R'),('voisina-ge',r'voisina\handwritten{-}ge'),(r'vois\unsure{i}na-ge',r'vois\unsure{i}na\handwritten{-}ge')]
L=[]
def a(p,c,f,s,v='high',C=True,k='other',q=None):
 d=dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable')
 if q:d['consequential']=q
 L.append(d)
a('page header','handwritten 33','handwritten - 33 -','header: two blue horizontal strokes flank the handwritten numeral.','high',k='omission')
a('right edge after non connex','connex unsure e,','connex','connexe: the image ends immediately after the complete x; neither e nor comma has a surviving stroke. Supplying either would complete absent ink.','high',k='text not on the page')
a('right edge after défini','défini unsure es','défini','definies: the complete i is followed by the cut edge; no e or s is visible.','high',k='text not on the page')
a('right edge ensemble split','ens unsure em ble','ens then ble; no em','ensemble: the terminal s is complete at the cut edge and the next line begins ble. The letters em have no surviving ink.','high',k='text not on the page')
a('right edge variété','variét unsure é','variét unsure é retained','variete: a small blue segment survives at the edge after t, but its body and accent cannot be read securely.','low',False)
a('section ordinal','2) unmarked','handwritten 2)','section2number: the curved 2 and long parenthesis are continuous pen strokes, unlike the adjacent type impressions.')
a('symbol before (z_k)','unsure frak I/script I/script J','same local alphabet alternatives retained','imaginary and symbol_formula: top-left curl and broad curled foot join a straight right stem; this alone does not settle I/J or the typographic alphabet.','low',False,k='misread symbol or index')
a('real field letter','unsure mathbb R/R','R','Rfield: a single stem supports one loop and oblique leg; no separate parallel upright appears.','medium',k='misread symbol or index')
a('right edge g(x)','g(x unsure closing parenthesis','same uncertainty retained','closing: a short blue curved fragment touches the right boundary below x; it is consistent with the bottom of a closing parenthesis, but most of the stroke is lost.','low',False)
a('right edge voisinage','vois unsure i na-ge','same i uncertainty retained','voisinage: the edge retains small upper/lower blue pieces after s, without a complete stem.','low',False)
a('first internal voisinage hyphen','voisina-ge; hyphen unmarked','voisina-handwritten hyphen-ge','hyphen and proof: a slanting continuous pen dash lies between a and g, inside the line.')
a('second internal voisinage hyphen','vois unsure i na-ge; hyphen unmarked','vois unsure i na-handwritten hyphen-ge','na_hyphen: the narrow rising pen dash between a and g differs from the neighbouring type impressions.')
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 33 -','unnamed hand')
i('text','opening continuation','l’amplitude de z … theta prime bounds … non connex … défini … H et H prime')
i('text','two function definitions','par -2pi/3 < theta < -pi/3 et pi/3 < theta < 2pi/3 … f(z) … g(z)')
i('text','squares and holomorphy','(f(z))^2=z … (g(z))^2=z … chap.I, section2, th.1 …')
i('text','end of first paragraph','Mais dans H … theta prime=2pi+theta … et dans H theta prime=theta … f(z)=-g(z)')
i('text','section 2 opening','2) Lorsque K=C … ens [edge] ble … f(x)=g(x) … variét unsure é')
i('text','real linear subspace','linéaire réelle V … script/frak I/J(z_k)=beta_k … 1<=k<=p … a in U intersection V')
i('text','derivative proof','les dérivées partielles de h … h(x) … f(x)=g(x) … voisina-ge')
i('text','one-variable condition','Si K=R ou K=C, et p=1 … g(x unsure closing parenthesis … voisinage compact … infini')
i('text','final paragraph','En effet … b in U … points distincts (z_n) … h(z_n)=0 … h(x)=0 … précédemment')
commit(15,64,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally viewed before C. All mathematical bands, right-edge C doubts, hand additions, and alphabet questions enlarged. The two occurrences of H after Mais dans and et dans are both unprimed: Hfirst confirms absence of prime rather than repairing the argument. K and M are ordinary type, C is handwritten plain; d’après has enough surviving left s curves to retain its final s. No H coverage, no cancellations or marginal notes; archive 63 comment only. Context unopened.'))
