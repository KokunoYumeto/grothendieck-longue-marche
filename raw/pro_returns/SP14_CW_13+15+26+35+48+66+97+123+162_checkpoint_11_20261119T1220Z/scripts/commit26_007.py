import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\uline{\unsure{Recommandation} importante}',r'Re\uline{commandation importante}'),(r'``\unsure{fid|fid.} \unsure{plt|plt.} \unsure{qu.|qu} \unsure{cpct|cpt}\'\'',r'``fid plt qu. cpct\'\''),(r'\unsure{détachées}',r'détachées'),(r'\unsure{\leftarrow|=}',r'\unsure{=|\leftarrow}')]
# Apostrophes are literal quotation marks, not escaped LaTeX commands.
R[1]=(R[1][0].replace("\\'","'"),R[1][1].replace("\\'","'"))
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no'):
 L.append(dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh))
a('heading word',r'\unsure{Recommandation}','Recommandation','Recommandation','heading_upright: the compressed successive c-o-m-m-a-n-d-a-t-i-o-n strokes are present; the terminal n has no additional s.','medium',True,False)
a('heading underline','whole heading underlined','heading without underline',r'Re\uline{commandation importante}','heading_upright: the horizontal line begins under the first c, after the initial R and e, and continues under importante.','high',True,True,'insertion or placement')
a('first quoted abbreviation',r'\unsure{fid|fid.}','fid.','fid','quote_upright: f-i-d is followed by white space; the terminal dark spot belongs to the upturned end of d, not a detached period.','medium',True,True,'misread word')
a('second quoted abbreviation',r'\unsure{plt|plt.}','plt','plt','quote_upright: the tall p descender and the l/t strokes are visible; the spot at the end is joined to t.','medium',True,False)
a('third quoted abbreviation',r'\unsure{qu.|qu}','qu.','qu.','quote_upright/cpct: a separate round dot follows the flat u.','high',True,False)
a('fourth quoted abbreviation',r'\unsure{cpct|cpt}','cpt','cpct','cpct: after the first c and the long p descender there is another separate low curved c before the tall terminal t.','medium',True,True,'misread word')
a('between qu. and cpct','space','hyphen','space','cpct: white gap after the separate period; no horizontal joining dash.','high',False,True,'text not on the page')
a('quotation marks','two raised strokes at each end','guillemets','two raised strokes at each end','quote_upright: each pair consists of short raised strokes, also around couvrant; no angled guillemet is drawn.',k='misread symbol or index')
a('lower title noun','Relation','Relations','Relation','bottomwords_upright: after the n there is no further letter; the line continues with d’équivalence.',k='misread word')
a('lower title final word',r'\unsure{détachées}','détachées','détachées','bottomwords_upright: initial looped d, accented e, long t, a, c-h and the final é-e-s sequence can be followed.','medium',True,False)
a('lower punctuation',r'\unsure{??|!?}','!?',r'\unsure{??|!?}','punct: the first dark sign bends at its top and turns right at the bottom above a separate dot; the top hook is too slight to exclude a bent exclamation mark. The second sign is plainly a question mark.','low',False,True,'misread symbol or index')
a('cancelled object left of diagram',r'\deleted{\unsure{X|S}}','note: crossed illegible sign',r'\deleted{\unsure{X|S}}','old: intersecting diagonal strokes support X but a curved upper/lower remnant also permits S; dense crossing prevents resolution. The visible crossed object is included in the diagram.','low',False,True,'drawing or diagram')
a('cancelled connector left of R0',r'\deleted{\unsure{\leftarrow|=}}','omitted',r'\deleted{\unsure{=|\leftarrow}}','old: two short parallel horizontal remnants survive at the right of the cancellation; no separate intact arrowhead survives, so = is primary while a damaged left arrow remains possible.','low',True,True,'omission')
a('overwritten superscript at R0',r'\deleted{\unsure{o}}i','i',r'\deleted{\unsure{o}}i','super0: a small loop remains under the thick rewritten body and a distinct dot stands above; old o remains uncertain and the live dotted i is retained.','low',False,True,'omission')
a('upper arrowhead','left-pointing arrow','note: only lower arrowhead legible','left-pointing arrow','arrows: the upper shaft ends at the left in a continuous curved turn with a lower oblique arm; the lower shaft has a separate complete left-pointing head.','high',False,True,'drawing or diagram')
a('encircling oval','TikZ oval','described in note','TikZ oval','formula: a pale single oval surrounds the two parenthesized objects and crosses the cancelled left symbol. It is drawn, not replaced by prose.',k='drawing or diagram')
a('watermark','VELIN EXTRA P.J','omitted','VELIN EXTRA P.J','watermark_readable: after rotation and reflection the faint outlined capitals VELIN EXTRA and P.J are visible on this sheet. The dark manuscript strokes cross them but do not supply any of their letters.','medium',False,True,'omission')
I=[dict(kind=k,position=p,text=t,hand=h) for k,p,t,h in [
 ('text','upper heading','Recommandation importante','his hand'),
 ('drawing','under heading','underline begins under first c, ends under importante','his hand'),
 ('text','recommendation','Partout où c’est possible, remplacer "fid plt qu. cpct" par "couvrant".','his hand'),
 ('drawing','between two text blocks','long horizontal rule','his hand'),
 ('text','lower title','(pré)-Relation d’équivalence en pièces détachées ??/!?','his hand'),
 ('diagram','lower right','(R0^i) receives two arrows from (R1^{ij}); cancelled left object and connector','his hand'),
 ('deletion','left edge of diagram','X/S and =/left arrow','his hand'),
 ('deletion','superscript of R0','old o, doubtful, under i','his hand'),
 ('insertion','superscript of R0','live dotted i over old loop','his hand'),
 ('drawing','around diagram','oval crossing cancelled left symbol','his hand'),
 ('marginnote','vertical through sheet','VELIN EXTRA P.J','paper watermark')]]
commit(26,7,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole then both supplied halves viewed before C/H. Every word and punctuation mark inspected; heading, both text lines, all C doubts and all mathematical components enlarged. Sloping prose rotated upright. Watermark read on this sheet after rotation, reflection and contrast adjustment, not inferred from a neighbour. All crop26_007.py crops viewed, including tight cpct and watermark_readable. Plain handwritten R; i has a separate dot, j descends; no doubled mathematical alphabet inferred from retracing. Archive6 remains a comment. Context unopened.'))
