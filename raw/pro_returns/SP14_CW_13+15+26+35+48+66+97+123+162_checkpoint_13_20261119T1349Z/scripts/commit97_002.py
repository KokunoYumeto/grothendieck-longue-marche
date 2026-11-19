import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[(r'\unsure{papier}','papier'),(r'J-P. \uline{Serre}.',r'J-P Se\uline{rr}e.')]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no'):
 L.append(dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh))
a('printed letterhead','COLLÈGE / DE / FRANCE / rule / CHAIRE / D’ALGÈBRE ET GÉOMÉTRIE','described in editorial note, not transcribed','COLLÈGE / DE / FRANCE / rule / CHAIRE / D’ALGÈBRE ET GÉOMÉTRIE','header2x: all six printed lines are distinct, with a separate short horizontal rule between FRANCE and CHAIRE; grave on COLLÈGE, apostrophe and accents in the chair title.','high',False,True,'omission')
a('first paragraph quotation marks',"``Notice''",'« Notice »',"``Notice''",'line2x7: two separate upright raised strokes on each side of Notice; no inward angles.','high',False,True,'misread symbol or index')
a('first paragraph last phrase','même chose',r'\uncertain{même chose}','même chose','same18x and line4x12: m shoulders, compressed e, second m and e with flattened circumflex; chose has tall h, rounded o, compact s and e.','medium',False,True,'other','yes')
a('second paragraph initial noun','Notice','notice','Notice','line5x7: initial letter has two tall strokes and a connecting diagonal, the same capital N shape as the quoted Notice above.','high',False,True,'abbreviation expanded or spelling modernised')
a('second paragraph after un',r'\unsure{papier}','papier','papier','papier20x: two separate long p descenders, low a, dotted i, compressed e and final r shoulder/exit.','medium',True,False)
a('second paragraph after justement',r'\unsure{le fibré|les fibrés}','les fibrés',r'\unsure{le fibré|les fibrés}','fibres18x and line7x7: short article ends after a low hump; fibré ends in a broad compressed stroke below the acute. Neither final s can be separated securely; primary singular follows visible shorter forms, but plural remains possible.','low',False,True,'misread word')
a('group notation',r'\mathrm{SL}_{2}',r'\mathrm{Sl}_2',r'\mathrm{SL}_{2}','sl2x24: the second letter has a tall straight stem, equal in height to S, and a distinct horizontal foot; 2 is lower and smaller.','high',False,True,'misread symbol or index')
a('last adjective before joli',r'\unsure{très}','très',r'\unsure{très}','tres24x: t cross is separate from a nearly horizontal upper accent; remaining letters form a compressed shoulder and downward terminal curl. The e/s division is too merged to remove C’s doubt.','medium',False,True)
a('signature after initial P','J-P.','J-P.','J-P','signature16x: blank space between the tall P and the S; no separate abbreviation point is visible.','high',True,True,'text not on the page')
a('signature underline',r'\uline{Serre}','Serre',r'Se\uline{rr}e','signature16x and signame7x: a short separate red horizontal stroke lies beneath the middle two r strokes, starting near the e exit and stopping before the final e; it does not span the name.','high',True,True,'insertion or placement')
a('signature final point','.','absent','.','signature16x and signame7x: a separate low red oval point follows the final e, with clear white spacing.','high',False,True,'omission')
I=[
 dict(kind='text',position='upper left, printed letterhead',text='COLLÈGE / DE / FRANCE / CHAIRE / D’ALGÈBRE ET GÉOMÉTRIE',hand='print'),
 dict(kind='drawing',position='between FRANCE and CHAIRE',text='short horizontal printed rule',hand='print'),
 dict(kind='text',position='upper right, date formula',text='Paris, le',hand='print'),
 dict(kind='text',position='upper right, date',text='4 Nov. 66',hand='Jean-Pierre Serre'),
 dict(kind='text',position='salutation',text='Cher Grothendieck,',hand='Jean-Pierre Serre'),
 dict(kind='text',position='first paragraph',text='Je n’ai pas regardé ton pb. Mais je suis tombé sur une Notice...',hand='Jean-Pierre Serre'),
 dict(kind='text',position='second paragraph',text='La Notice renvoie à un papier de Milnor...',hand='Jean-Pierre Serre'),
 dict(kind='text',position='closing',text='Bien à toi',hand='Jean-Pierre Serre'),
 dict(kind='text',position='bottom right signature',text='J-P Serre.',hand='Jean-Pierre Serre'),
 dict(kind='drawing',position='beneath middle of surname',text='short underline below rr',hand='Jean-Pierre Serre'),
]
commit(97,2,dict(replace=R,changes=L,inventory=I,sheet_kind='letter',hand='Jean-Pierre Serre',observations='Whole then both supplied halves personally viewed before C/H. All 17 non-header crops from crop97_002.py personally viewed; oversized original header output was truncated and was not read, replaced by header2x; adaptive signame7x read. Date, salutation, both full paragraphs, all punctuation, hyphens, accents, closing and signature read in enlarged ink. Printed and red handwritten portions distinguished. Archive numeral 1 retained only as comment. No readable watermark or additional annotation established. H’s following section heading belongs to scan5 outside this page and is not treated as text on scan2. Not a second audit or mathematical check.'))
with open('out/notation.tsv','a') as f:
 f.write('Serre capital L\t97/2, SL2\tStraight capital-height stem and short horizontal foot, no cursive loop; numeral lower\t\\mathrm{SL}_{2}\tnone\n')
 f.write('Serre partial underline\t97/2 signature\tShort separate horizontal stroke beneath middle rr, not full surname\tSe\\uline{rr}e\tnone\n')
