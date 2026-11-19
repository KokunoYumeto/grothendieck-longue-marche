import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{\times|*}',r'\times'),
(r'\unsure{èquiv|équiv}','èquiv'),
(r'\unsure{èquivalent|équivalent}','èquivalent'),
(r'dim\unsure{,|.}','dim,'),
(r'\unsure{prèschémas|préschémas}','prèschémas'),
]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('upper-left marks','drawn oblique broken lines and curve','omitted','drawn oblique broken lines and curve','topmarks6x: two sets of nearly parallel broken sloping marks and a pale U-shaped return to their right, separate from the words.','high',False,True,'drawing or diagram')
a('item 25 lower circle mark',r'\unsure{\times|*}','omitted',r'\times','circle25x13: four diagonal arms are distinct; lower pair overlaps the circle, without an extra asterisk ray.','medium',True,True,'drawing or diagram')
a('item circles','circled 25 and 28','parenthesized 25 and 28','circled 25 and 28','whole, top half and circle25x13: pen loops surround the numerals, with a small upper-right gap at 25.','high',False,True,'drawing or diagram')
a('item 25 first abbreviated adjective',r'\unsure{èquiv|équiv}','équiv.','èquiv','equiv1x18: accent descends toward the right; final v exit has no separate abbreviation point.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 25 parenthetical abbreviation','pb','Pb','pb','pb13x: p has a long descender below the b body; its upper bowl is lowercase-sized.','high',False,True,'abbreviation expanded or spelling modernised')
a('item 25 parenthetical article','du','des','du','pb13x: d loop and joined u bowl ending in a long exit; no e plus s sequence.','high',False,True,'misread word')
a('item 25 quoted noun','carré',r'\uncertain{courbes}','carré','pb13x: open c, closed a, two short r shoulders and final e; raised acute over the ending; no b ascender.','high',False,True,'misread word','yes')
a('item 25 quotation marks',"``pb du carré''",'« Pb des courbes »',"``pb du carré''",'pb13x: two short raised strokes at either end, not angled guillemets.','high',False,True,'misread symbol or index')
a('item 25 second equivalence abbreviation','alb.','alg.','alb.','alb13x: the third letter has a tall ascender and closed lower bowl, unlike a g descender.','high',False,True,'misread word',cons='The second question concerns the written alb. equivalence; H substitutes alg.')
a('item 25 after alb.','èquiv.','équiv.','èquiv.','alb13x: first accent leans down toward the right above the initial e.','medium',False,True,'abbreviation expanded or spelling modernised')
a('item 25 full adjective',r'\unsure{èquivalent|équivalent}','équivalent','èquivalent','equivalent13x: long thin downward-right extension follows the dark upper accent mark; retained as a grave.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 25 final equivalence noun',r'\unsure{équivalence|èquivalence}','équivalence',r'\unsure{équivalence|èquivalence}','equivalence12x: the short nearly vertical accent above the first e has no secure diagonal direction.','low',False,True)
a('item 25 margin bracket','curved bracket and separate lower vertical stroke','omitted','curved bracket and separate lower vertical stroke','bracket12x: long parenthesis-like curve ends before the last line; a separate near-vertical stroke continues below it. The margin note was read at9x rotated −39 degrees.','high',False,True,'drawing or diagram')
a('item 26 adjective',r'\unsure{relative|reletive}','relative',r'\unsure{relative|reletive}','relative16x: low loop after l and before the tall t may be an open a or e; letter form does not securely settle it.','low',False,True)
a('item 26 end punctuation','no period','period','no period','twentysix5x: closing parenthesis reaches the image edge; no following period is visible and none is supplied.','high',False,True,'text not on the page')
a('item 27 initial accent',r'\unsure{Adèles|Adéles}','Adèles',r'\unsure{Adèles|Adéles}','adeles17x: accent is a short near-vertical bent mark; acute/grave direction remains uncertain.','low',False,True)
a('item 27 after dim',r'\unsure{,|.}','.',',','dim17x: mark has a curved tail descending below the writing line.','high',True,True,'misread symbol or index')
a('item 27 final punctuation',',','.',',','locales15x: long oblique tail descends leftward from the upper point.','high',False,True,'misread symbol or index')
a('item 28 prefix accent',r'\unsure{prèschémas|préschémas}','préschémas','prèschémas','preschemas13x: first accent runs from upper left toward lower right; the second accent remains in its separate position over the later e.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 28 final punctuation',',','.',',','end14x: bent descending stroke to the right of the closing parenthesis, with a faint trailing tip.','medium',False,True,'misread symbol or index')
I=[dict(kind=k,position=p,text=t) for k,p,t in [
('drawing','upper left corner','two oblique broken lines and pale curved return'),
('drawing','left of item 25','circle around 25 with cross overlapping its lower border'),
('text','item 25 first question',"Le produit de deux cycles alg. èquiv à 0 est-il rat. équiv. à 0 ? (``pb du carré'')."),
('text','item 25 second question',"Un 0-cycle qui est alb. èquiv. à 0 est-il rationnellement èquivalent à 0 ?"),
('text','item 25 final sentence',"Question de l’équivalence|èquivalence rationnelle des 0-cycles sur une surface."),
('margin note','left of item 25, slanted','faux, cf Mumford...'),
('drawing','between margin and item 25 continuation','long curved bracket then separate lower vertical line'),
('text','item 26','Théorie de Rosenlicht relative|reletive (sur base quelconque)'),
('text','item 27','Adèles|Adéles des schémas de dim, quelconque. Jacobiennes locales,'),
('drawing','left of item 28','circle around 28'),
('text','item 28',"Construction d’une théorie abstraite des motifs sur prèschémas de type fini sur blackboard Z (construction catégorique générale),"),
]]
commit(66,5,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole then both halves personally viewed before witnesses. All crops from crop66_005.py, including rotated margin, and adaptive categorique/motifs personally viewed. Every agreed word, abbreviation, zero, punctuation and the two parallel diagonals of blackboard Z checked. Bottom half is blank except archive numeral 4, retained only as comment. No watermark visible. No deleted passage. Not a second audit or a mathematical check.'))
