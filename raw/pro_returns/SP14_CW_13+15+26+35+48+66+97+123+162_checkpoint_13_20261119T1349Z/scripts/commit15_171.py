import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[];L=[]
def change(p,a,b,ink,conf='medium',kind='other',consequential=None):
 R.append((a,b));d=dict(place=p,c=a,h='absent',final=b,ink=ink,confidence=conf,kind=kind,against_c=True,against_h=False,marked_in_H='not applicable')
 if consequential:d['consequential']=consequential
 L.append(d)
def keep(p,c,ink,conf='low'):
 L.append(dict(place=p,c=c,h='absent',final=c+' retained',ink=ink,confidence=conf,kind='other',against_c=False,against_h=False,marked_in_H='not applicable'))
change('heading manuscript number',r'\mspage{20}',r'\mspage{(20)}','head: a clear opening and closing parenthesis enclose 20 beside the title. The number is not the pencil archive170.','high','omission')
change('1 first lattice symbol',r'\unsure{I|\Gamma|\mathbb{P}|L|\Pi}',r'\unsure{\mathbb{I}|\Gamma|\mathbb{P}|L|\Pi}','firstletter: two displaced top and bottom bars and a doubled main stem are visible. Apply the specified rule for an overtyped mathematical letter to the primary I reading. A short upper right descending stroke prevents identification of the underlying letter with confidence.','low','misread symbol or index','Primary lattice letter marked double-struck; underlying I/Gamma/P/L/Pi still unresolved.')
keep('3 parenthetical word before le groupe simple','unsure oar/par','oar, third: the first letter has a closed bowl and a small upper-left serif but no secure descending p stem below the neighbouring a/r baseline. The page does not settle whether this is o or a defective p; no grammatical completion.')
change('heading Tribu numeral provenance',r'\handwritten{59}',r'\unsure{\handwritten{59}|59}','n59, head, order1, dim5: the 5 and 9 have narrow descending forms, but closely similar forms recur in baseline numbers elsewhere. Manual versus machine origin is not secure from this reproduction. Numerical reading 59 is clear.','low')
change('1 quotient divisor provenance',r'\handwritten{/3}',r'\handwritten{/}\unsure{\handwritten{3}|3}','first, F3, sp3: slash is an oblique added stroke; 3 has two uneven lobes but resembles baseline 3 later. Keep C hand as primary for the raised/added numeral with explicit origin doubt; subsequent same numeral follows that primary locally.','low')
change('1 dimension numeral provenance','dimension 5.','dimension \\unsure{5|\\handwritten{5}}.','dim5, order1, n59: 5 has a short cap, separate upper stem and descending lower curve. These match other page figures closely enough that manual origin cannot be asserted; value 5 is secure.','low')
change('2 first order numeral provenance',"(d'ordre 25 920)","(d'ordre \\unsure{25 920|\\handwritten{25 920}})",'order1, order2: two 2 figures, descending 5 and 9, and closed 0 are clear. Similar repeated outlines do not securely distinguish type impressions from hand lettering. First occurrence marks the provenance doubt; later repeated order retains primary.','low')
change('F heading E subscript provenance',r'E_{\handwritten{7}}',r'E_{\unsure{\handwritten{7}|7}}','F: separate lowered 7 with a flat top and descending diagonal; origin uncertain against the similar baseline7 in the order. Value and subscript position secure.','low')
# Only first occurrence of the repeating F_2 receives this provenance doubt.
from work import W,row
text=(W/row(15,171)['codex_file']).read_text()
for a,b in R:
 assert a in text,a
 text=text.replace(a,b)
a=r'F_{\handwritten{2}}';b=r'F_{\unsure{\handwritten{2}|2}}';assert a in text;text=text.replace(a,b,1)
L.append(dict(place='F first coefficient-field subscript provenance',c=a,h='absent',final=b,ink='F, baseline2, sect2, ZZ: lowered2 is clear, but its top hook and wavy foot resemble the baseline2 impressions. Hand/machine origin remains uncertain at first occurrence; repeated subscripts keep C primary.',confidence='low',kind='other',against_c=True,against_h=False,marked_in_H='not applicable'))
for p,a,b,ink in [
 ('F dimension6 provenance',r'\handwritten{6}',r'\unsure{\handwritten{6}|6}','F: open upper hook and lower closed loop give6; origin not secure.'),
 ('F order exponent9 provenance',r'\handwritten{9}',r'\unsure{\handwritten{9}|9}','seq: small raised loop with descending stroke gives9; same origin uncertainty as the baseline9.'),
 ('F order exponent4 provenance',r'\handwritten{4}',r'\unsure{\handwritten{4}|4}','seq: raised open angular4 is clear, but the original hand versus machine impression is not secure.'),
 ('last paragraph E subscript8 provenance',r'\handwritten{8}',r'\unsure{\handwritten{8}|8}','end: lowered two-loop8 is clear; provenance remains uncertain.')]:
 assert a in text;text=text.replace(a,b)
 L.append(dict(place=p,c=a,h='absent',final=b,ink=ink,confidence='low',kind='other',against_c=True,against_h=False,marked_in_H='not applicable'))
a='\\[\n1\\handwritten';b='\\[\n\\text{(s)}\\qquad 1\\handwritten';assert a in text;text=text.replace(a,b).replace('\n\\tag*{(s)}','')
L.append(dict(place='exact-sequence label placement',c='tag (s) at display right',h='absent',final='(s) before the sequence at left',ink='seq: (s) stands separately at the left margin, on the same baseline as the sequence.',confidence='high',kind='insertion or placement',against_c=True,against_h=False,marked_in_H='not applicable'))
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','header left','SYSTÈMES de RACINES (20)')
i('text','header right','Tribu n raised o 59','typewriter and unnamed hand; numeral provenance uncertain')
i('text','opening continuation','de signe +1.')
i('text','exercise1','On pose E=...; bil. sym. non dégénérée; distinct roots')
i('insertion','exercise1 formula','slash3 and lowered3; hand origin of numeral uncertain','unnamed hand; numerals uncertain')
i('drawing','under F in exercise1','two separate horizontal underlines','unnamed hand')
i('text','exercise2','On note O(E); norm spinorielle; groupe simple; unique Omega')
i('insertion','exercise2 first equality','braces and plus-minus around1','unnamed hand')
i('insertion','exercise2 spinor map','right arrow, braces and plus-minus','unnamed hand')
i('insertion','exercise2 SO exponents','three raised plus signs','unnamed hand')
i('insertion','exercise2 subgroup','Omega','unnamed hand')
i('text','exercise3','Tout élément de Aut(R); quotient; isomorphisme; image W and W+')
i('insertion','exercise3 images','Omega and two raised plus signs','unnamed hand')
i('text','parenthetical conclusion','Ainsi W(R) est extension... oar/par ...25 920')
i('text','sectionF heading','F) Groupe de Weyl W de E7','typewriter; subscript provenance uncertain')
i('text','sectionF first paragraph','Soient Q le réseau radiciel; P celui des poids; forme alternée')
i('insertion','sectionF lattice relations','two subset signs and quotient slash','unnamed hand')
i('text','sectionF numerals','F2, dim(E)=6, Sp(3,F2)','typewriter and unnamed hand; numeral provenance uncertain')
i('insertion','sectionF homomorphism','right arrow W to Sp(E)','unnamed hand')
i('text','before sequence','Montrer que la suite')
i('display','middle-lower sequence','(s) 1 -> (1,-1) -> W -> Sp(3,F2) ->1','typewriter and unnamed hand')
i('text','after sequence','est exacte; order2^9.3^4.5.7; cf. Alg. IX','typewriter; raised numerals provenance uncertain')
i('text','penultimate paragraph','Montrer que le sous-groupe W+... ne contient pas -1')
i('insertion','penultimate paragraph W exponent','raised plus','unnamed hand')
i('text','last paragraph','Donner une seconde démonstration; W(E8); Sp(3,F2) -> underlined O(7,F2)','typewriter and unnamed hand; numeral provenance uncertain')
i('insertion','last isomorphism','right arrow','unnamed hand')
i('drawing','last O','single short horizontal underline','unnamed hand')
commit(15,171,dict(text=text,changes=L,inventory=I,sheet_kind='typescript',hand='typewriter and unnamed hand',observations='Whole image then both halves viewed before C. H absent. Every line and formula checked in head/first/second/third/F/seq/end enlargements; every letter candidate and provenance issue enlarged further. First lattice glyph identity and oar/par remain doubtful. Numerous narrow descending numerals resemble each other; their values are secure but ambiguous hand-versus-machine origin is marked in place instead of inferred from shape alone. Plain Z single diagonal and F single stem retained; F3 double underline and final O single underline confirmed. Pair (x y) has blank without comma; first pair(x,y) has comma. All signs and indices read literally, no mathematical validation claimed. Title has grave accent. Archive170 comment only; no watermark seen. Context unopened.'))
