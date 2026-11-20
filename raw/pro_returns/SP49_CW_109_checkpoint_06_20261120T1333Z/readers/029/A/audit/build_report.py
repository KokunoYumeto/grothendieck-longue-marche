from pathlib import Path
import json
root=Path('work/readers/029/A')
m=json.load(open('work/inputs/029/metadata.json'))
frozen=json.load(open(root/'audit/frozen_loci.json'))
by={r['id']:r for r in frozen['open_loci']}
original=Path('work/inputs/029/C.tex').read_text()
s=original
changes=[]
def evidence(crop=None,half=None,bbox=None):
    if crop:
        r=by[crop]
        return {'crop':r['output'],'source':r['source'],'bbox':r['bbox']}
    return {'crop':None,'source':m['half_'+half],'bbox':bbox}
def change(id,place,c,reading,kind,confidence,note,crop=None,half=None,bbox=None,anchor=None,replacement=None):
    global s
    a=c if anchor is None else anchor
    b=reading if replacement is None else replacement
    assert a and s.count(a)==1,(id,a,s.count(a))
    s=s.replace(a,b,1)
    changes.append({'id':id,'place':place,'c':c,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':note,**evidence(crop,half,bbox)})

mark_top=r'''\margin{\begin{tikzpicture}[x=1ex,y=1ex]\draw[gray,line width=.10ex,line cap=round] (.2,0) .. controls (.08,.24) and (.12,.45) .. (.18,.65);\draw[gray!55,line width=.08ex] (.46,.95)--(.60,1.06);\draw[gray!45,line width=.06ex] (.75,1.28)--(.74,1.41);\end{tikzpicture}}'''
barparen=r'''(again\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.08ex,line cap=round] (.10,1.55) .. controls (.52,.70) and (.44,-.05) .. (-.12,-.45);\draw[line width=.08ex,line cap=round] (.43,.05)--(.84,.05);})'''
# The final literal ')' above is only a Python-readable end marker; the visible parenthesis is drawn.
barparen=barparen[:-1]
overlap=r'''in\tikz[baseline=(aold29A.base)]{\node[inner sep=0pt] (aold29A) {\deleted{\unsure{a|o}}};\node[anchor=base west,inner sep=0pt] at (aold29A.base west) {a};}dequacies'''
comdot=r'''\tikz[baseline=(com29A.base)]{\node[inner sep=0pt] (com29A) {commutes};\fill ([xshift=1.35em,yshift=1.65ex]com29A.base west) circle (.055ex);}'''
refdots=r'''\tikz[baseline=(r360A.base)]{\node[inner sep=0pt] (r360A) {l-17};\fill ([xshift=.60em,yshift=2.70ex]r360A.base west) circle (.070ex);\fill ([xshift=.57em,yshift=2.30ex]r360A.base west) circle (.075ex);\fill ([xshift=.46em,yshift=1.65ex]r360A.base west) circle (.060ex);\fill ([xshift=1.25em,yshift=2.05ex]r360A.base west) circle (.045ex);}'''
qdot=r'''\tikz[baseline=(q360A.base)]{\node[inner sep=0pt] (q360A) {``};\fill ([xshift=.14em,yshift=.65ex]q360A.base west) circle (.050ex);}'''
marginpoints=r'''\margin{\begin{tikzpicture}[x=1ex,y=1ex]\fill (0,0) circle (.055ex);\fill (.22,.36) circle (.065ex);\end{tikzpicture}}'''

change('A29-01','upper left before p335',"'",'', 'text not on the page','high','The dark pointed area has an ochre/brown material edge and lies above-left of the entry; the half shows a small damaged/punctured area, not a written quotation stroke.',half='a',bbox=[89,74,121,113],anchor="' p335",replacement='p335')
change('A29-02','right margin below archive number, near p336 level','',mark_top,'omission','medium','A separate short irregular vertical dark trace and two detached paler traces are visible; their origin is unassigned and no continuous line or letter is inferred.',crop='15',anchor="p.336 l.-8 ``skilful''",replacement="p.336 l.-8 ``skilful''\n"+mark_top+'\n% isolated right-margin traces; origin unassigned')
change('A29-03','p341 l.2, after better','better.','better,','misread symbol or index','high','The low mark has a thick upper-right head and a clear taper down-left; it is comma-shaped rather than a round point.',crop='03')
change('A29-04','p341 l7, opening quotation',"'doesn't''",r"\unsure{'|``}doesn't''",'misread symbol or index','low','One curved main stroke has a small crossing spur; a single hook is favoured, but the joined spur does not securely exclude two joined opening strokes.',crop='04',anchor="l7 'doesn't''",replacement=r"l7 \unsure{'|``}doesn't''")
change('A29-05','342, second line reference','l-8','l.-8','omission','high','A separate low dark point is clearly between the l foot and the minus, below the minus baseline.',crop='05',anchor="342 l13 ``didn't'' l-8",replacement="342 l13 ``didn't'' l.-8")
change('A29-06','p.345 l.7, closing parenthesis after again','(again).',barparen,'drawing or diagram','high','The curved closing parenthesis has a short rightward bar joined to its middle/lower portion. No independent following period is visible in the contextual crop; the attached geometry is reproduced.',crop='08')
change('A29-07','p350, short word after also','in',r'\unsure{in|on}','misread word','low','A small closed low body and a separate high point favour a dotted i, but the body also permits an o; the short word is not decided by its context.',crop='09',anchor='also in l.15.',replacement=r'also \unsure{in|on} l.15.')
change('A29-08','p351 l-11, first vowel of inadequacies',r'in\deleted{\unsure{a|o}}adequacies',overlap,'insertion or placement','high','The old oval and the final live a occupy one glyph-space. The cancelled vowel still permits a or o; only the spatial overlap is resolved.',crop='11')
change('A29-09','p353 l.9, opening quotation',"``its''",r"\unsure{``|'}its''",'misread symbol or index','low','Two sides meet to enclose a narrow slot and continue into a downward tail. A joined pair is favoured, but a looped single mark is not excluded.',crop='12',anchor="p353 l.9 ``its''",replacement=r"p353 l.9 \unsure{``|'}its''")
change('A29-10','p356, cancelled Formulae',r'\unsure{Formulae|Formulæ}','Formulae','misread word','medium','The final a has its own round body and right-hand downstroke, followed by a separately formed e; the cancellation crosses above and along their baseline but does not erase that separation.',crop='16')
change('A29-11','p356, second cancelled parenthetic reference',r'\unsure{B|3}','B','misread symbol or index','high','A tall left stem joins two rightward bowls. The stem belongs to the glyph and is distinct from the left parenthesis and cancellation, deciding B rather than 3.',crop='17')
change('A29-12','p357, last symbol of cancelled formula',r'\unsure{s|?}',r'\unsure{?|s}','misread symbol or index','low','A separate low dark point survives under a curved upper form, so a question mark is the first candidate. The crossing still permits an s-like remnant, which is retained.',crop='19')
change('A29-13','p358 l.9, opening quotation before been',"'been wasting my time''",r"\unsure{``|'}been wasting my time''",'misread symbol or index','low','The raised group has two downward tips with an open notch below a joined top; a joined pair is favoured but a hooked single stroke remains possible.',crop='21')
change('A29-14','p358 continuation l-4, opening quotation',"'commutes with''","``commutes with''",'misread symbol or index','medium','A long raised stroke is followed by a distinct smaller raised point at its right, giving two opening marks; neither is part of the initial c.',crop='22',anchor="l-4 'commutes with''",replacement="l-4 ``commutes with''")
change('A29-15','p358 continuation l-4, above first m of commutes','commutes',comdot,'omission','high','A small isolated dark point stands above the first m-region. It is drawn at its observed position without assigning a punctuation or accent function.',crop='22',anchor="l-4 ``commutes with''",replacement='l-4 ``'+comdot+" with''")
change('A29-16','p360, above and beside first l-17 reference','l-17',refdots,'omission','high','Four separate dark points lie around the top of this reference: two stacked above l, one lower beside its loop and one farther right above the 1. They are reproduced separately without being joined or named as punctuation.',crop='25',anchor='p360 l-17',replacement='p360 '+refdots)
change('A29-17','p360, below opening quotation before than/then','``',qdot,'omission','high','A distinct low point lies beneath the two opening quotation strokes. It is preserved geometrically without making a new punctuation reading.',crop='24',anchor=r'``\unsure{than|then} looking',replacement=qdot+r'\unsure{than|then} looking')
change('A29-18','p361 l16, opening quotation',"'didn't''",r"\unsure{'|``}didn't''",'misread symbol or index','low','The raised mark has a main downstroke and a shorter joined oblique arm; it may be a single elaborate hook or two coalesced strokes.',crop='27',anchor="p361 l16 'didn't''",replacement=r"p361 l16 \unsure{'|``}didn't''")
change('A29-19','p362 l.7, opening quotation',"'interpret''",r"\unsure{'|``}interpret''",'misread symbol or index','low','The high group has a tall left arm and short right branch meeting centrally. The merged shape does not securely determine whether one or two quotation strokes were written.',crop='28')
change('A29-20','right margin between p363 and p365 levels','',marginpoints,'omission','high','Two distinct dark points are separated diagonally beside the faint vertical material trace. They are drawn as separate points, with origin and function unassigned.',crop='14',anchor="p363 l-8 ``shouldn't''",replacement="p363 l-8 ``shouldn't''\n"+marginpoints+'\n% two isolated right-margin points; origin unassigned')
change('A29-21','p365 l-19, opening quotation before first isnt',"``isn't''",r"\unsure{``|'}isn't''",'misread symbol or index','low','A joined curved upper group has two low tips, while the i-dot is separately farther right. The group permits a joined pair or a hooked single opener.',crop='29',anchor="l-19 ``isn't''",replacement=r"l-19 \unsure{``|'}isn't''")
change('A29-22','p369 l.4, opening quotation before suggests',"'suggests that one views''",r"\unsure{'|``}suggests that one views''",'misread symbol or index','low','The opener is a connected curved stem with an oblique inner branch. The separate preceding low comma is not counted as a quotation stroke; the opener itself remains one-versus-two uncertain.',crop='31')

# Descriptive comments do not change manuscript content.
s=s.replace('\\margin{\\deleted{\\unsure{end|ed}}}', '% faint lower-right cancellation; lower ink approaches the physical paper edge\n\\margin{\\deleted{\\unsure{end|ed}}}')
s=s.replace('% archive sheet number: 28','% archive sheet number: 28 (upper right)')
s='\\cotefile{109}\n'+s
(root/'reading.tex').write_text(s)

cd=[]
def doubt(place,c,reading,resolved,conf,note,crop=None,half=None,bbox=None):
 cd.append({'place':place,'c':c,'reading':reading,'resolved':resolved,'confidence':conf,'evidence':note,**evidence(crop,half,bbox)})
doubt('p339 l-12 cancelled glyph',r'\deleted{\unsure{\&|l}}',r'\deleted{\unsure{\&|l}}',False,'low','Several loops and a tall stroke survive the crossing. The cancellation is certain; the interior still allows ampersand and l.','02')
doubt('p350 l-10 underline',r'\unsure{\uuline{i}|\uline{i}}',r'\unsure{\uuline{i}|\uline{i}}',False,'low','Several closely touching returned passes lie beneath i. The heavy joins do not securely separate two underlines from retracing of one.','10')
doubt('p351 l-11 cancelled old vowel',r'\deleted{\unsure{a|o}}',r'\deleted{\unsure{a|o}}',False,'low','The old rounded body is buried under the final a. A separate old right-hand tail cannot be distinguished. The spatial overlap, unlike the old letter identity, is certain.','11')
doubt('p356 cancelled first word',r'\unsure{Formulae|Formulæ}','Formulae',True,'medium','A separately formed a with a right-hand stem is followed by e. The ae separation is visible despite the cancellation.','16')
doubt('p356 second cancelled reference',r'\unsure{B|3}','B',True,'high','The left upright and two attached right bowls decide B independently of the preceding (2).','17')
doubt('p357 page reference',r'p\unsure{357}',r'p\unsure{357}',False,'medium','A rightward top remnant and descending end fit 7, but the crossing/faded area removes enough of the figure to retain the doubt. Neighbouring page numbers are not used to supply it.','20')
doubt('p357 raised mark on f',r'f^{\unsure{*|+}}',r'f^{\unsure{*|+}}',False,'low','The raised group has short oblique projections, favouring a star. The cancellation covers the lower joining strokes, so plus remains possible.','19')
doubt('p357 cancelled argument letter',r'\unsure{\beta|g|S}',r'\unsure{\beta|g|S}',False,'low','Upper and lower curved portions plus a downstroke favour beta. The diagonal cancellation supplies/obscures parts of the closures, so g and S are not excluded.','19')
doubt('p357 cancelled argument subscript',r'\unsure{M|m}',r'\unsure{M|m}',False,'low','The low two-humped remnant is separately visible below the argument, but its left stem and case are buried by the crossing.','19')
doubt('p357 cancelled relation',r'\unsure{=|-}',r'\unsure{=|-}',False,'low','A short lower stroke and another roughly parallel segment survive; one may be a cancellation return, leaving either equality or a single dash.','19')
doubt('p357 cancelled final symbol',r'\unsure{s|?}',r'\unsure{?|s}',False,'low','The separate lower point makes question mark the first candidate; the upper curve is too crossed to exclude s.','19')
doubt('p359 page reference',r'p\unsure{359}',r'p\unsure{359}',False,'medium','The upper arc and lower descending remnant favour 9, but the middle is physically faded at the vertical material trace. No sequence-based completion is made.','23')
doubt('p360 l-17 word before looking',r'\unsure{than|then}',r'\unsure{than|then}',False,'low','The small vowel loop can be a cursive a or e; its exit joins the n and does not expose a decisive separate crossbar or tail.','24')
doubt('bottom-right cancelled note',r'\deleted{\unsure{end|ed}}',r'\deleted{\unsure{end|ed}}',False,'low','An e-like beginning, faint middle strokes and a tall final d-like stem remain. A diagonal crossing is visible, but the middle letter is not securely separated; some low ink approaches the physical paper edge.','32')
doubt('p355 l-3 parenthetic star',r'$(*)$',r'$(*)$',True,'high','The half has intersecting central strokes with oblique rays inside round parentheses; no alternative mathematical sign is imposed.',half='b',bbox=[930,207,997,253])
doubt('p341 l.2 underline',r'\uline{got me}',r'\uline{got me}',True,'high','One continuous low rule runs beneath got and me, ending before back; no second independent underline is visible.',half='a',bbox=[640,429,790,490])
doubt('p351 l-11 quotation edges',"``in...adequacies'","``in...adequacies'",True,'high','Two high opening strokes and one terminal high tick are separately visible. The vowel overlap is recorded independently from these quotation edges.',half='a',bbox=[1019,915,1329,1004])
# Replace the span identifier with literal C/output text; all report readings are literal.
cd[-1]['c']=r"``in\deleted{\unsure{a|o}}adequacies'"
cd[-1]['reading']='``'+overlap+"'"
doubt('p353 l.9 joined opening pair in context',"``its''",r"\unsure{``|'}its''",False,'low','The joined narrow slot permits both two coalesced strokes and a looped single mark. The C-context claim of a pair is not treated as controlling the ink.','12')
doubt('p338 qualification and question',r'? ``and even\x27\x27 perhaps.',r'? ``and even\x27\x27 perhaps.',True,'high','The half clearly preserves the question mark, proposed wording and perhaps; crop 01 preserves the isolated terminal point in its actual position.','01')
cd[-1]['c']=cd[-1]['reading']="? ``and even'' perhaps."
doubt('p341 qualification punctuation','is perhaps better.','is perhaps better,',True,'high','The qualification is live; the terminal mark has a descending comma contour.','03')
doubt('p350 reservation about from',r'(``from\x27\x27 can also be used but is less usual.)',r'(``from\x27\x27 can also be used but is less usual.)',True,'high','The complete parenthetic qualification is visible, with paired quotes around from and a final point inside the closing parenthesis.',half='a',bbox=[329,797,1569,923])
cd[-1]['c']=cd[-1]['reading']="(``from'' can also be used but is less usual.)"
doubt('p355 question wording',r'do you mean ``from $(*)$\x27\x27',r'do you mean ``from $(*)$\x27\x27',True,'high','The phrase is visibly do you mean, followed by the quoted from and parenthetic star. There is no supplied final question mark.',half='b',bbox=[640,205,1025,264])
cd[-1]['c']=cd[-1]['reading']="do you mean ``from $(*)$''"
doubt('p356 qualification about copy','(indistinct in my copy)','(indistinct in my copy)',True,'high','The qualification follows the first isnt correction in live ink; both parentheses are visible.',half='b',bbox=[424,266,797,332])
doubt('p356 cancelled complaint and question',r'\deleted{\unsure{Formulae|Formulæ} $(2)$ and $(\unsure{B|3})$ are unreadable. Are they}',r'\deleted{Formulae $(2)$ and $(B)$ are unreadable. Are they}',True,'high','The cancellation continues across the first line and the line beginning are unreadable; the period after unreadable and the following Are they remain readable. Old/new uncertainty of Formulae and B is separately recorded.','18')
doubt('dated divider','Sent 6/2/84','Sent 6/2/84',True,'high','Sent and the date stand above the long wavy separator, between the two p354 entries.',half='a',bbox=[801,1167,1080,1232])

remaining=[]
for d in cd:
 if not d['resolved']:
  remaining.append({'place':d['place'],'reading':d['reading'],'alternatives':d['reading'],'confidence':d['confidence'],'reason':d['evidence']})
for cid in ['A29-04','A29-07','A29-13','A29-18','A29-19','A29-21','A29-22']:
 c=next(x for x in changes if x['id']==cid)
 remaining.append({'place':c['place'],'reading':c['reading'],'alternatives':c['reading'],'confidence':c['confidence'],'reason':c['evidence']})

inv=[]
def item(kind,pos,words,hand='unnamed handwritten correction-list hand'):
 inv.append({'sheet_kind':'list','hand':hand,'element':f'{len(inv)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
entries=[
('upper row 1','p335 l.7. dont; l-16 wouldnt'),
('upper row 2','p.336 l.-8 skilful'),
('upper row 3','p.338 l12 its; l-8 ? and even perhaps.'),
('upper row 4','p.339 l-12 shouldnt'),
('upper row 5','340 l.18 afraid'),
('upper row 6','p341 l.2 and alongside got me back; l7 doesnt; & l.8'),
('upper row 7','342 l13 didnt; l.-8 couldnt'),
('upper row 8','344 l.17 commutes with; l.20 allows us to; l.21 commuting with'),
('upper row 9, continuation of 344','l.23 commutes with; l-9 commute with'),
('upper row 10','p.345 l.5 commutes with; l.7 with (again); l.10 characterises'),
('upper row 11','p.348 l-2 wont'),
('upper rows 12–13','p350 l.14 its; also in/on l.15.; l-10 independent of; from qualification'),
('upper row 14','p351 l12 wasnt; l14 wouldnt; l-11 inadequacies'),
('upper row 15','p.352 l8 didnt'),
('upper row 16','p353 l.9 its; l-17 inadequate'),
('upper row 17','p354 l8 dont'),
('above divider','Sent 6/2/84'),
('first entry below divider','p354 l.-10 didnt; l-11 isnt; l-3 its'),
('lower second entry','p.355 l.-4 which; l-3 do you mean from (*)'),
('lower third entry, two physical lines','p356 l1 isnt (indistinct in my copy); l6 weve got; cancelled complaint; l.-2 weve got'),
('lower fourth entry','p357 l.1 weve got; cancelled formula; l-17 commutes with'),
('lower fifth entry','p358 l.1. didnt; l.4 shouldnt; l8 dont; l.9 been wasting my time'),
('lower continuation below p358','l-4 commutes with'),
('next lower entry','p359 l16 its'),
('next lower entry','p360 l-17 than/then looking ..; l-16 and trying; l-5 didnt'),
('next lower entry','p361 l16 didnt'),
('next lower entry','p362 l.7 interpret'),
('next lower entry','p363 l-8 shouldnt'),
('next lower entry','p365 l.4 its; l-19 isnt; l-17 isnt; l-4 doesnt'),
('next lower entry','p367 l-13, its'),
('third entry from foot','p369 l.4, suggests that one views; l-13 its; l-5 didnt; l-4 dont'),
('second entry from foot','p370 l6 its also l.-3.'),
('last full entry','p371 l14 its; l18 dont; l20 in which I was working; l.21 wasnt')]
for pos,words in entries:item('text',pos,words)
item('deletion','p339 after shouldnt','cancelled ampersand/l')
item('text','nested in p341 l.2','single underline beneath got me')
item('drawing','nested in p345, after again','closing parenthesis with attached short rightward bar')
item('text','nested in p350 l-10','repeated/possibly double underline beneath initial i')
item('deletion','nested in p351 l-11','old a/o under final first a of inadequacies')
item('text','same glyph-space in p351 l-11','live a written over old a/o')
item('drawing','between dated Sent line and lower p354 entry','long wavy horizontal separator')
item('deletion','p356 first physical line, after l6 weve got','Formulae (2) and (B)')
item('deletion','p356 continuation line, before l.-2','are unreadable. Are they')
item('display','p357 between l.1 correction and l-17 correction',r'$(2)\quad f^{\unsure{*|+}}(\unsure{\beta|g|S}_{\unsure{M|m}})\unsure{=|-}\unsure{?|s}$')
item('deletion','same p357 formula','heavy oblique/return cancellation over label and formula')
item('drawing','right margin near p336','short irregular vertical trace and two detached faint traces; origin unassigned','origin and hand unassigned')
item('drawing','p358 continuation, above first m in commutes','isolated dark point; origin/function unassigned','origin and hand unassigned')
item('drawing','p360 first line reference','four separately placed high dark points; no assigned punctuation function','origin and hand unassigned')
item('drawing','p360 before than/then','isolated point below opening quotation pair','origin and hand unassigned')
item('drawing','right margin between p363 and p365','two separate diagonal points; origin/function unassigned','origin and hand unassigned')
item('margin note','bottom right, next to/below end of final line','end/ed, faint and cancelled','hand uncertain, pale handwriting')
item('deletion','nested in bottom-right margin note','diagonal cancellation crossing end/ed','hand uncertain, pale handwriting')
item('margin note','upper-right corner','28, archive sheet number recorded as a comment','unnamed archive-number hand')

notes=[
'English corrections cite pages 335–371. The list contains contractions, its, skilful, characterises, and repeated commute/commutes/commuting with proposals.',
'At p338 l-8 the wording retains a question mark and perhaps; p341 calls the alongside got me back wording perhaps better. The words got me are underlined.',
'At p350 l-10 the note prefers independent of and says from can also be used but is less usual; the initial i bears heavily repeated underline strokes.',
'Sent 6/2/84 is above the long divider. A further p354 entry begins directly below it.',
'At p355 l-3 the writer asks do you mean from (*) without a final written question mark. At p356 the first contraction is qualified by indistinct in my copy.',
'The cancelled p356 passage says Formulae (2) and (B) are unreadable. Are they; the following line has a separately heavily cancelled formula whose small signs remain uncertain. This is not a complete live mathematical assertion.',
'There is a faint cancelled end/ed-like note at the lower right. Its low strokes approach the physical paper edge; no unseen completion is supplied.',
'No title, total page count or authorial page number is visible. The upper-right 28 is treated only as an archive sheet-number comment.'
]
notation=[
{'sign':'(*)','location':'p355 l-3','reading':r'$(*)$','evidence':'The lower half shows a central crossing with diagonal rays within round parentheses.'},
{'sign':'B','location':'p356 cancelled second reference','reading':'B','evidence':'Crop 17 has one left stem and two right bowls; numeral 3 is rejected.'},
{'sign':'raised mark and lowered argument marks','location':'p357 cancelled formula','reading':r'f^{\unsure{*|+}}(\unsure{\beta|g|S}_{\unsure{M|m}})\unsure{=|-}\unsure{?|s}','evidence':'Crop 19 independently inspected each small component; cancellation leaves all listed alternatives open, with final question mark preferred because of its separate low point.'},
{'sign':'single/double opening quotation','location':'p341 l7; p353 l.9; p358 l.9; p361 l16; p362 l.7; p365 l-19; p369 l.4','reading':r'\unsure{\x27|``} or \unsure{``|\x27}, individually marked','evidence':'Each corresponding crop shows a joined form whose stroke count is not securely separable. Decisions were made separately, not copied from recurrence.'},
{'sign':'paired opening quotation','location':'p344 l.20; p345 l.7; lower p354 l-11; p360 l-5; p358 continuation l-4','reading':'``','evidence':'Crops 06, 07, 33, 26 and 22 show two distinct raised elements at each respective location.'},
{'sign':'single opener','location':'p365 l-4','reading':"'",'evidence':'Crop 30 shows one solid curved wedge with a lower toe, without a separate second mark.'},
{'sign':'underlining','location':'p341 l.2; p350 l-10','reading':r'\uline{got me}; \unsure{\uuline{i}|\uline{i}}','evidence':'The upper half decides the single got me span; crop 10 leaves the tightly joined i passes unresolved.'},
{'sign':'overwritten vowel','location':'p351 l-11','reading':overlap,'evidence':'Crop 11 shows old and live vowels in the same glyph-space; old identity remains a/o.'},
{'sign':'rightward bar attached to parenthesis','location':'p345 l.7 after again','reading':barparen,'evidence':'Crop 08 shows a joined transverse stroke, not an isolated period.'},
{'sign':'low reference stop','location':'342 second correction','reading':'l.-8','evidence':'Crop 05 separates the point below the minus and to the right of l.'},
{'sign':'isolated geometric marks','location':'right margin near p336; p358 continuation; p360 reference and quote; right margin at p363/p365','reading':'See exact TikZ readings in changes A29-02, A29-15, A29-16, A29-17 and A29-20.','evidence':'Separate points/traces are preserved without joining them or assigning letters and intentional punctuation.'}
]
notation[3]['reading']=r"l7 \unsure{'|``}doesn't''; p353 l.9 \unsure{``|'}its''; l.9 \unsure{``|'}been wasting my time''; p361 l16 \unsure{'|``}didn't''; p362 l.7 \unsure{'|``}interpret''; l-19 \unsure{``|'}isn't''; p369 l.4, \unsure{'|``}suggests that one views''"
# A code-reference field, rather than descriptive replacement, points to the exact literal code.
notation[-1]['reading']=mark_top+'\n'+comdot+'\n'+refdots+'\n'+qdot+'\n'+marginpoints

report={
'scan':29,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[m[k] for k in ['whole','half_a','half_b']],
'layout':'Single handwritten English correction list occupying almost the full sheet, with page references at the left and corrections across the main area. The date Sent 6/2/84 stands immediately above a long wavy horizontal divider; text continues below from another p354 entry. The p356 complaint wraps to a cancelled second line; the next p357 line carries a heavily cancelled inline formula. One faint cancelled note sits at the lower right near the physical paper edge. The archive 28 is in the upper-right corner. Two thin gray vertical traces at approximately whole-image x=212 and x=1493 have pale flanks and coincide with fading of nearby ink; crops 13/14 support treating them as material/fold or photographic traces rather than secure pen rules, so they are recorded here and not redrawn as ink. The small ochre-edged dark area above-left of p335 is likewise material, not an apostrophe. Distinct isolated dark marginal points/traces are separately reproduced with origin unassigned. No typed text, diagram, title or authorial pagination is seen. The correction-list hand is not identified by name.',
'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'math_checks':[],
'notation':notation,
'abbreviations':[{'form':'p / p.','expansion':'page (tentative list-only expansion)','place':'left references throughout'},{'form':'l / l.','expansion':'line (tentative list-only expansion)','place':'line references throughout'},{'form':'&','expansion':'and (list-only interpretation)','place':'p341 after doesnt; a cancelled ampersand/l remains uncertain at p339'}],
'brief_feedback':'The prescribed whole-once, each-half-once sequence was followed, then 33 unresolved loci were frozen before one crop per locus was made with scripts/crop.py and displayed. No whole or half image was reopened. All source reading was visual; no OCR, recognition, compilation or external research was used. H is description-only, so every h field is null and no H collation row is asserted. Inventory covers every list entry and continuation, the dated line, underline spans, overlapping correction, both cancelled complaint lines, cancelled formula, horizontal rule, distinct isolated marks, faint margin note and archive numeral comment. Material/fold interpretation remains a layout observation rather than an assertion that every gray trace is ink. No mathematically substantive proof or computation was possible from the cancelled fragment without definitions, so math_checks is empty. The added cotefile command is archive metadata, not a manuscript collation change.'}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

crop_decisions={
'01':'Retain the terminal point after perhaps; a distinct low point is visible at a distance from the final s. Do not suppress it as random texture.',
'02':'Retain cancelled ampersand/l uncertainty; cancellation extent certain.',
'03':'Read comma after better.',
'04':'Mark opener single/double uncertain, single first.',
'05':'Read l.-8 with a distinct stop.',
'06':'Confirm double opener before allows.',
'07':'Confirm double opener and closer around with.',
'08':'Draw closing parenthesis with attached bar; no detached final stop.',
'09':'Mark short word in/on uncertain.',
'10':'Retain double/single underline ambiguity.',
'11':'Overlap old a/o and live a in one glyph-space.',
'12':'Mark opener double/single uncertain.',
'13':'Gray vertical trace has material/photographic character; record in layout, not as a definite ink rule.',
'14':'Record gray vertical trace as material/photographic; reproduce two separate dark adjacent points geometrically.',
'15':'Reproduce short dark irregular vertical and detached faint traces, origin unassigned.',
'16':'Resolve Formulae rather than Formulæ.',
'17':'Resolve B rather than 3; confirm preceding (2).',
'18':'Confirm cancelled are unreadable. Are they and its stop.',
'19':'Keep raised mark, argument and index/relation uncertainties; prefer ? over s at end because of separate low point.',
'20':'Retain unsure357; surviving fragment favours 7 but incomplete.',
'21':'Mark been opener double/single uncertain, double first.',
'22':'Read two opening marks; also preserve a separately observed point above the first m-region.',
'23':'Retain unsure359; middle of final digit faded.',
'24':'Retain than/then; preserve point below opener.',
'25':'Preserve four distinct high points around l-17 without assigning punctuation.',
'26':'Confirm double opener before didnt.',
'27':'Mark single/double opener uncertain.',
'28':'Mark single/double opener uncertain.',
'29':'Mark first isnt opener double/single uncertain; i-dot independently identified.',
'30':'Confirm single opener before doesnt.',
'31':'Mark single/double opener uncertain; preceding comma is independent.',
'32':'Retain cancelled end/ed uncertainty; acknowledge physical paper edge.',
'33':'Confirm double opener and closer around isnt; i-dot separately visible.'}
(root/'audit'/'crop_decisions.json').write_text(json.dumps(crop_decisions,ensure_ascii=False,indent=2)+'\n')
(root/'audit'/'visual_log.json').write_text(json.dumps({'whole_views':1,'half_a_views':1,'half_b_views':1,'crop_views':[{**r,'displayed_once':True,'decision':crop_decisions[r['id']]} for r in frozen['open_loci']],'not_used':['OCR','recognition library','PDF extraction','LaTeX compilation','external research','other page images','other reader output']},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(cd),'remaining_doubts':len(remaining),'inventory':len(inv),'crops':len(by),'math_checks':0}))
