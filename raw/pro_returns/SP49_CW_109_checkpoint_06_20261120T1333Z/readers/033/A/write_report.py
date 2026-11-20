from pathlib import Path
import json,difflib,re
O=Path('work/readers/033/A')
C=Path('work/inputs/033/C.tex').read_text()
F=json.loads((O/'frozen_loci.json').read_text())
L={x['id']:x for x in F['loci']}
A=F['viewed_once'][1]; B=F['viewed_once'][2]
changes=[]; decisions=[]; notes=[]; remaining=[]; notation=[]
reading=C

def change(id,place,c,r,kind,crop=None,box=None,src=A,conf='high',evidence='',replace=True):
    global reading
    if replace:
        assert c in reading,(id,c)
        reading=reading.replace(c,r,1)
    loc=L[crop] if crop else None
    changes.append(dict(id=id,place=place,c=c,h=None,reading=r,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=conf,evidence=evidence,crop=loc['crop'] if loc else None,source=loc['source'] if loc else src,bbox=loc['bbox'] if loc else box))

def decision(place,c,r,resolved,crop=None,box=None,src=A,conf='high',evidence=''):
    loc=L[crop] if crop else None
    decisions.append(dict(place=place,c=c,reading=r,resolved=resolved,confidence=conf,evidence=evidence,crop=loc['crop'] if loc else None,source=loc['source'] if loc else src,bbox=loc['bbox'] if loc else box))

def rem(place,r,alts,reason,conf='low'):
    remaining.append(dict(place=place,reading=r,alternatives=alts,confidence=conf,reason=reason))

def nt(sign,loc,r,evidence):
    notation.append(dict(sign=sign,location=loc,reading=r,evidence=evidence))

# All marks below are tied to the text they physically accompany.
l468=r'''\tikz[baseline=(l468A.base)]{\node[inner sep=0pt] (l468A) {l-4};\fill[overlay] ([xshift=-4.9em,yshift=-.1ex]l468A.base west) circle (.045ex);}'''
change('left-point-468','left margin between p468 and p469',r'l-4 ``doesn\'t\'\''.replace('\\\'','\''),l468+" ``doesn't''",'drawing or diagram',box=[53,147,81,178],evidence='One separate compact dark point at approximately (67,167), left of the column rule; no punctuation function assigned.')

# The small high point just right of the first reference is independent of the numeral.
ref471=r'''\tikz[baseline=(ref471A.base)]{\node[inner sep=0pt] (ref471A) {l.-14};\fill[overlay,black!65] ([xshift=.42em,yshift=1.35ex]ref471A.base east) circle (.04ex);}'''
change('ref471-point','471 first reference, small raised point after 14','471 l.-14','471 '+ref471,'drawing or diagram',crop='02',evidence='The low full stop between l and minus is real and retained. A separate small dark point stands high to the right of 14; it is not a second stop in the reference.')
decision('471 first line reference, newly inspected punctuation','l.-14','l.-14',True,crop='02',evidence='Crop02 separates the low dot from the foot of l and from the following horizontal minus. No change to C reference.')

this471=r'''\tikz[baseline=(this471A.base)]{\node[inner sep=0pt] (this471A) {This};\fill[overlay] ([xshift=1.25em,yshift=3.0ex]this471A.base east) circle (.04ex);}'''
change('point-above-471','blank above the 471 prose, near x922,y299','This sentence',this471+' sentence','drawing or diagram',box=[903,283,940,311],evidence='Half a shows a compact isolated dark point above the sentence; it is separate from the line reference and from all letters below.')

very=r'''\tikz[baseline=(badly471A.base)]{\node[inner sep=0pt] (badly471A) {badly};\node[overlay,anchor=south west,inner sep=0pt] at ([xshift=-.75em,yshift=.6ex]badly471A.north west) {\inserted{very}};\draw[overlay,line width=.4pt,line cap=round] ([xshift=-.48em,yshift=-.35ex]badly471A.base west) -- ([xshift=-.30em,yshift=.32ex]badly471A.base west) -- ([xshift=-.03em,yshift=-.15ex]badly471A.base west);}'''
change('very-height','471 reads very badly',r'\inserted{very} badly',very,'insertion or placement',box=[1131,284,1369,387],evidence='Very is above the baseline between reads and badly, with a lower angular insertion mark. The replacement places both at that gap rather than on the running-text baseline.')
negatives=r'''\tikz[baseline=(and471A.base)]{\node[inner sep=0pt] (and471A) {\&};\node[overlay,anchor=south west,inner sep=0pt] at ([xshift=-.18em,yshift=1.0ex]and471A.north west) {\inserted{(too many negatives)}};}'''
change('negative-note-height','471 raised parenthetical after badly',r'\inserted{(too many negatives)} \&',negatives,'insertion or placement',box=[1353,268,1634,385],evidence='The parenthetical is written wholly above the end of badly and the following ampersand/isnt area; parentheses and words are all live.')
change('say-colon','471 after I think you want to say',r'\unsure{:|.}',':','misread symbol or index',crop='03',evidence='Two separately formed dark bodies stand vertically, an upper hooked mark and a lower triangular point.')
decision('471 after say',r'\unsure{:|.}',':',True,crop='03',evidence='The two vertically separated bodies decide a colon, not a lone period.')

false_start=r'''``\deleted{I wouldn't expect} \tikz[baseline=(much471A.base)]{\node[inner sep=0pt] (much471A) {\deleted{much}};\node[overlay,anchor=south west,inner sep=0pt] at ([xshift=-.30em,yshift=.25ex]much471A.north west) {\inserted{too}};\draw[overlay,line width=.4pt,line cap=round] ([xshift=-.28em,yshift=-.55ex]much471A.base west) -- ([xshift=-.12em,yshift=.12ex]much471A.base west) ([xshift=-.25em,yshift=-.43ex]much471A.base west) -- ([xshift=.18em,yshift=-.49ex]much471A.base west) -- ([xshift=.26em,yshift=-.31ex]much471A.base west);}'''
change('false-start-scope','471 cancelled opening proposal',r'''\deleted{``I wouldn't expect \inserted{too} much}''',false_start,'deletion state (struck given live or live given struck)',crop='04',evidence='Both opening quotation strokes are above/left of the first cancellation. The raised too is above the crossing and remains live, with an angular cue below; the baseline words I wouldnt expect and much are crossed. No closing quotation is supplied.')
change('pi-bar','471 group object formula',r'\unsure{\bar{\pi}|\pi}_{1}',r'\bar{\pi}_{1}','misread symbol or index',crop='05',evidence='The pi has a long roof, two legs and lowered 1; a separate short horizontal stroke stands above its right side. The visible upper stroke is preserved as a bar.')
decision('471 group object, upper stroke on pi',r'\unsure{\bar{\pi}|\pi}_{1}',r'\bar{\pi}_{1}',True,crop='05',evidence='A distinct short horizontal upper stroke is visible above the pi roof. This is a graphical reading; no interpretation of barred pi is imposed.')
aken=r'''mist\tikz[baseline=(ook471A.base)]{\node[inner sep=0pt] (ook471A) {\deleted{ook}};\node[overlay,anchor=south west,inner sep=0pt] at ([xshift=-.15em,yshift=.18ex]ook471A.north west) {\inserted{aken}};}'''
change('mistaken-placement','471 N.B. correction in mistook',r'mist\deleted{ook}\inserted{aken}',aken,'insertion or placement',crop='06',evidence='Two old rounded bodies and the final k survive the crossing. Aken is readable above these old letters, starting over the first old o, so it is placed above the cancelled portion.')
decision('471 C context: mistook replaced by mistaken',r'mist\deleted{ook}\inserted{aken}',aken,True,crop='06',evidence='The old ook and upper aken are both visible. The lexical reading agrees with C; only their height/overlap is changed.')

for old,new,cf,ev in [
    (r'\unsure{so}','so','high','Separate surviving s turns and a closed o at the left edge are readable despite the crossing.'),
    (r'\unsure{if}','if','high','A short first upright with a high small stroke precedes a distinct tall looped f, including its descender.')]:
    change('cancel-'+new,'471 cancelled request, '+new,old,new,'misread word',crop='07',conf=cf,evidence=ev)
for word,cf,ev in [
    ('so','high','The two first letter bodies survive at the left edge and decide so.'),
    ('please','low','The long p descender and l ascender survive, but repeated crossings cover several middle letters.'),
    ('check','low','Initial lower curve and tall h loop survive; the middle and ending strokes are partly buried.'),
    ('if','high','The short i body and following tall f with low loop are separately visible.'),
    ('my','low','The lower returning y loop is visible; the preceding short shoulders are heavily crossed.'),
    ('guess|view','low','The middle group is almost continuously covered; surviving low turns do not decide guess versus view.'),
    ('is','low','Only a short pair of bodies and a possible high mark survive securely.'),
    ('correct','medium','Initial low cups and terminal t/exit are visible, but several intervening joins are covered.')]:
    old='\\unsure{'+word+'}'
    resolved=word in ('so','if')
    new=word if resolved else old
    decision('471 cancelled request, word '+word,old,new,resolved,crop='07',conf=cf,evidence=ev)
    if not resolved: rem('471 cancelled request, '+word,new,word,ev,cf)

decision('468 l-15, second letter before the very least',r'\unsure{at|an}',r'\unsure{at|an}',False,crop='01',conf='medium',evidence='The first a is readable. The second short descending-and-returning body has no secure high crossbar or shoulder; at and an remain possible.')
rem('468 l-15',r'\unsure{at|an}','at | an','The local second-letter strokes do not decide a crossed t versus compressed n. No grammatical correction is made.','medium')

decision('472 worth interest closing quote, newly inspected edge',"``worth interest''","``worth interest''",True,crop='08',evidence='The closing group has two descending legs joined by an oblique return. The complete right edge is visible; C double quote is retained.')

old474=r'''\tikz[baseline=(old474A.base)]{\node[inner sep=0pt] (old474A) {\deleted{\unsure{p|i}}};\node[anchor=base west,inner sep=0pt] at (old474A.base west) {i};}ts'''
change('old474-overlap','474 l-6 initial corrected letter',r'\deleted{\unsure{p|i}}its',old474,'insertion or placement',crop='09',conf='high',evidence='Old small loop/descending traces and the live i occupy the same glyph space. Shared ts is printed once. The old p/i identity remains uncertain.')
decision('474 l-6 old initial',r'\unsure{p|i}',r'\unsure{p|i}',False,crop='09',conf='low',evidence='A small loop and low descender favor p, but overlapping/crossing strokes leave i possible. The old and new strokes are physically superposed.')
rem('474 l-6 old initial',r'\unsure{p|i}','p | i','The old stem/loop is crossed by the live initial and cannot be separated securely.')
change('quote474-close','474 l-6 close after corrected its',old474+"''",old474+r"\unsure{'|''}",'misread symbol or index',crop='09',conf='low',evidence='One independent short raised closer is clear. A neighboring longer component descends from the preceding line near the repetition parenthesis; its contribution to a second closer is unresolved. The crop does not show the full upper origin, so absence is not asserted.')
rem('474 l-6 closing quotation',r"\unsure{'|''}","single ' | double ''",'One independent stroke is visible; a nearby descending component may belong to the line above. Full upper origin is outside crop09, so both counts remain.')
change('commute-dots','474 l-5 continuation points',r'commute .... with',r'commute \unsure{.....|....} with','misread symbol or index',crop='10',conf='medium',evidence='Four compact low groups follow a short oblique group at the e exit. Five discrete groups are favored; the first may instead be the final e exit, so four remains possible.')
rem('474 l-5 after commute',r'\unsure{.....|....}','five low groups | four points plus the e exit','The leftmost short oblique group is close to the e terminal; its status is unresolved.','medium')
decision('474 l-5 quotation opener, newly inspected edge','``commute','``commute',True,crop='10',evidence='Two separate raised oblique opening strokes are visible; the fused appearance in the half resolves to a pair.')
change('diagram-label','475 primed diagram reference',r'\unsure{117|17|H|11}',r'\unsure{117|17|H}','misread symbol or index',crop='11',conf='medium',evidence='The last body has a distinct long oblique top and descending right stem, excluding a simple final 1. Two close preceding vertical bodies remain compatible with 11, a retraced 1, or the left part of H.')
decision('475 primed diagram reference',r'\unsure{117|17|H|11}',r'\unsure{117|17|H}',False,crop='11',conf='medium',evidence='11 is rejected because the last body has a clear oblique top plus a descending right shaft. 117,17,H remain; the separate high prime is certain.')
rem('475 diagram label',r'\unsure{117|17|H}','117 | 17 | H','The close initial verticals may be two numerals, a retraced numeral, or the left component of H.','medium')
decision('475 commutes with closing quotation, newly inspected edge',"commutes with''","commutes with''",True,crop='12',evidence='The high connected mark has two pendant legs and a bridging return. The complete right blank edge supports two strokes.')

change('poss','476 cancelled false start',r'\unsure{Poss.|For}','Poss.','misread word',crop='13',evidence='A tall closed P loop, low rounded o and two successive s turns survive; a distinct terminal point follows. This decides Poss. rather than For.')
decision('476 cancelled false start',r'\unsure{Poss.|For}','Poss.',True,crop='13',evidence='The capital has a closed P bowl and the lower sequence has o plus two s turns; the period is separately visible. Cancellation of the false start is certain.')
slight=r'''\tikz[baseline=(possible476A.base)]{\node[inner sep=0pt] (possible476A) {possible};\node[overlay,anchor=south west,inner sep=0pt] at ([xshift=-.55em,yshift=.35ex]possible476A.north west) {\inserted{slight}};\draw[overlay,line width=.4pt,line cap=round] ([xshift=-.25em,yshift=.35ex]possible476A.base west) -- ([xshift=-.50em,yshift=-.75ex]possible476A.base west) ([xshift=-.48em,yshift=-.65ex]possible476A.base west) -- ([xshift=-.30em,yshift=-.85ex]possible476A.base west);}'''
change('slight-height','476 slight possible ambiguity',r'\inserted{slight} possible',slight,'insertion or placement',crop='13',evidence='Slight is above the gap after the dash and before possible; the angular cue descends below the line there. The surrounding words are not underlined.')
decision('476 after we, cancelled letter',r'\unsure{a|e}',r'\unsure{a|e}',False,crop='14',conf='low',evidence='A small rounded body and short right exit are crossed by two diagonal passes. The interior is compatible with either a or e.')
rem('476 after we',r'\unsure{a|e}','a | e','Cancellation covers the small letter interior; both closed/partly open forms remain.')
change('it476-close','476 unattached pronoun it, closing quotation',"``it'.","``it''.",'misread symbol or index',crop='15',evidence='The compact high closer has two upward tips and two downward legs joined through the middle; the period below/right is independent. Both closing strokes are retained.')
decision('476 l-14 C context, cancelled its and live its/its distinction',r'''``\deleted{its} it's'' to be replaced by ``its'' ''',r'''``\deleted{its} it's'' to be replaced by ``its'' ''',True,crop='16',evidence='The cancellation exposes a dotted initial, crossed tall t and s loop. The following live form has an independent apostrophe before s; the replacement form on the half has none.')

# Clear detached left-margin point beside the 476 continuation.
unattached=r'''\tikz[baseline=(unattached476A.base)]{\node[inner sep=0pt] (unattached476A) {``unattached};\fill[overlay] ([xshift=-3.0em,yshift=-1.7ex]unattached476A.base west) circle (.035ex);}'''
change('left-point-476','left margin below unattached pronoun line','``unattached pronoun',unattached+' pronoun','drawing or diagram',src=B,box=[100,281,126,306],evidence='Half b shows one compact dark point around (113,293), well left of the text and before the l-14 row. No punctuation role is assigned.')
ref479=r'''\tikz[baseline=(ref479A.base)]{\node[inner sep=0pt] (ref479A) {l 2};\fill[overlay] ([xshift=.22em,yshift=-.75ex]ref479A.base east) circle (.045ex);}'''
change('point-479','479 l2, low point after reference','p 479 l 2','p 479 '+ref479,'drawing or diagram',crop='17',evidence='One isolated dark point lies below/right of the 2, under the blank before the opener; it is neither part of the numeral nor a high quote.')

ref481=r'''\tikz[baseline=(ref481A.base)]{\node[inner sep=0pt] (ref481A) {l 8};\fill[overlay,black!65] ([xshift=.12em,yshift=.95ex]ref481A.base west) circle (.035ex);\fill[overlay] ([xshift=-.48em,yshift=2.15ex]ref481A.base east) circle (.035ex);}'''
change('points-481-ref8','481 l8, two detached small points',"l 8 `didn't''",ref481+" `didn't''",'drawing or diagram',crop='18',evidence='The crop shows a small point just to the upper right of l and a second above the upper bowl of 8. Both are detached from the glyphs; origin is unassigned.')
change('didnt-opener','481 l8 opening quotation',ref481+" `didn't''",ref481+r" \unsure{`|``}didn't''",'misread symbol or index',crop='18',conf='medium',evidence='One dark upright opener is clear. A narrow, much paler parallel trace stands to its right; its ink/material status is unresolved, so a second stroke remains possible.')
rem('481 l8 opener',r'\unsure{`|``}','single ` | double ``','The right parallel trace is substantially paler than the secure left opener.','medium')
i481=r'''d\tikz[baseline=(i481A.base)]{\node[inner sep=0pt] (i481A) {\i};\draw[overlay,line width=.4pt,line cap=round] ([xshift=.03em,yshift=-.05ex]i481A.base west) -- ([xshift=.29em,yshift=-.05ex]i481A.base west);}dn't'''
change('low-i-mark481','481 l8 didnt, first i and its low mark',"didn't",i481,'drawing or diagram',crop='18',conf='medium',evidence='The first i has a short upright body and a separate low short horizontal mark at its foot; no secure high dot is visible there. The observed low geometry is preserved without labeling it an underline.')
change('yet-opener','481 l10 yet opening quotation',"l 10 `yet",r'l 10 \unsure{``|`}yet','misread symbol or index',crop='20',conf='medium',evidence='The opener is a compact forked group with two upper tips and a shared dark middle. Double is favored, but a single thick/returned stroke remains possible.')
rem('481 l10 yet opener',r'\unsure{``|`}','double `` | single `','The connected black group does not securely separate the number of pen strokes.','medium')
decision('481 l9 wasnt opener, newly inspected quotation',"``wasn't''","``wasn't''",True,crop='19',evidence='The opener has two narrow legs joined low in a U-like return. The apostrophe and final pair are separately visible; C is retained.')
decision('481 first factorial expression and following closer',r'''$(136)!$'' ''',r'''$(136)!$'' ''',True,crop='21',evidence='A tall exclamation stem and independent low point stand after the closing parenthesis. The adjacent high group has two pendant quote legs.')
change('doesnt481-close','481 l12 closing quotation after doesnt',"l 12, `doesn't''",r"l 12, `doesn't\unsure{''|'|}",'misread symbol or index',crop='22',conf='low',evidence='The opener is one separate high stroke, and the comma after 12 is clear. At the closing edge the long upper components can also be descenders from suggest above. Their entire upper origin is not included, so no absence is asserted; double, single or no independent closer is left explicit.')
rem('481 l12 closing quotation',r"\unsure{''|'|}","double '' | single ' | no independent closer",'Upper components at the edge may come from suggest on the preceding line; crop22 does not include their complete origin. The empty third TeX alternative denotes no independent closer.')

# Anchored long manuscript rules, with the left lower fading segment retained.
rule_code=r'''\tikz[remember picture,overlay]{
  \coordinate (scan033Abottom) at (0,0);
  \draw[line width=.3pt] ([xshift=3.40em,yshift=.65ex]scan033Atop) -- ([xshift=3.39em,yshift=2.4ex]scan033Abottom);
  \draw[black!35,line width=.25pt] ([xshift=3.39em,yshift=2.4ex]scan033Abottom) -- ([xshift=3.42em,yshift=-1.6ex]scan033Abottom);
  \draw[line width=.3pt] ([xshift=.91\linewidth,yshift=.55ex]scan033Atop) -- ([xshift=.911\linewidth,yshift=-1.7ex]scan033Abottom);
}'''
change('long-rules','left page-reference divider and near-right rule','',rule_code,'drawing or diagram',replace=False,box=[190,84,1489,2352],src=F['viewed_once'][0],evidence='The whole and both halves show two continuous thin rules from near the first row to below the last. The left rule fades at the foot; the right rule crosses long prose lines. They are anchored beside/through the text, not moved to a separate picture.')
reading=reading.replace('\\scanpage{33}',r'''\cotefile{109}
\scanpage{33}
\noindent\tikz[remember picture,overlay]{\coordinate (scan033Atop) at (0,0);}''',1)
reading=reading.replace('% archive sheet number: 32',rule_code+'\n% archive sheet number: 32')
reading=reading.replace(r"l 12, `doesn't\unsure{''|'|}",r"% In the following uncertainty, the final empty alternative means no independent closing quotation stroke."+'\n'+r"l 12, `doesn't\unsure{''|'|}")

# Explicit decisions on every page-specific context entry, separate occurrences kept separate.
for loc,tex,box in [
('469 l.4, first three-sign group',r'$\substack{\ast\,\ast\\ \ast}$',[404,181,476,239]),
('469 l.5, second three-sign group',r'$\substack{\ast\,\ast\\ \ast}$',[823,182,877,239]),
('471 first complex symbol',r'$X_{\ast}$',[465,502,541,563]),
('471 formula argument',r'$X_{\ast}$',[363,633,441,694]),
('471 ambient notation',r'$U(k)$',[549,622,680,690]),
('471 submersion label',r'$(H)$',[1337,624,1440,693]),
('474 l.3 repetition count',r'$(\times 2)$',[412,933,510,1007]),
]:
    decision(loc+' (C context)',tex,tex,True,box=box,evidence='The supplied half shows the stated configuration/letters at this occurrence; no competing stroke changes the literal C reading.')
    nt(tex,loc,tex,'Independently read from half a; this is an ink decision, not a theorem check.')
decision('482 l15 repetition count (C context)',r'$(\times 2)$',r'$(\times 2)$',True,src=B,box=[717,1113,804,1180],evidence='Crossed diagonals followed by 2, inside two round delimiters; independently read from half b.')
nt(r'$(\times 2)$','482 l15',r'$(\times 2)$','Half b, separate from the count at474.')
decision('475 high prime (C context)',"'","'",True,crop='11',evidence='One high oblique stroke stands after the ambiguous reference body and before its closing parenthesis.')
nt("'",'475 diagram label',"'",'Crop11: one separate high oblique prime inside the parentheses.')
decision('481 terminal factorial136! (C context)',r'$136!$',r'$136!$',True,src=B,box=[1395,982,1548,1050],evidence='Half b shows 136 followed by a tall separate exclamation stem and its low point, then the enclosing sentence parenthesis.')
nt(r'$(136)!$; $136!$','481 punctuation remark',r'$(136)!$; $136!$','Crop21 and half b independently preserve the two different parenthesis placements.')
decision('469 l.5 quasi-isomorphy (C context)','quasi-isomorphy','quasi-isomorphy',True,box=[899,181,1239,267],evidence='The last letter has a long descending y loop. It is not expanded to the morphism form used later.')
decision('481 upto (C context)','upto','upto',True,src=B,box=[1111,927,1224,994],evidence='The four letters are joined in one continuous word; no space is supplied.')
nt(r'\bar{\pi}_{1}','471 group object',r'\bar{\pi}_{1}','Crop05: separate short upper bar, pi roof with two legs and independently lowered1.')
nt(r'\&','471;480',r'\&','Both occurrences show the crossed/looped ampersand form; they are not an expanded word.')
nt('raised insertions','471 very; (too many negatives); too; aken;476 slight','very; (too many negatives); too; aken; slight','Each is placed at its independently visible height. The raised too remains live above the cancelled baseline wording.')
nt('quotation counts','474 l-6;476 it;481 l8,l10,l12',r"\unsure{'|''}; ``it''; \unsure{`|``}; \unsure{``|`}; \unsure{''|'|}",'The local quote-edge decisions are independent; nearby descenders are not automatically counted as quotation strokes.')

# Every actual list entry/text block, with nested corrections and drawings inventoried separately.
inv=[]
def elem(kind,pos,words,hand='another unnamed hand'):
    inv.append(dict(sheet_kind='list',hand=hand,element=f'{len(inv)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
entries=[
('468 first row left','p 468 l 12 ``its\'\''),('468 first row middle','l 15 ``won\'t\'\''),('468 first row right','l-15 at/an the very least'),('468 second row','l-4 doesn\'t'),
('469 first entry','p 469 l.4 after three crossed signs don\'t'),('469 second entry','l.5 after three crossed signs quasi-isomorphy'),('470 entry','p 470 l-12 its'),
('471 first short entry','471 l.-14 its'),('471 l-9 prose introduction','l-9 wouldn\'t This sentence reads very badly'),
('471 rejected opening','I wouldn\'t expect too much'),('471 proposed paragraph','The least I would expect from a complex X_*'),('471 N.B. paragraph','N.B. I may have mistook / aken'),('471 heavily cancelled request','so please check if my guess/view is correct'),
('472 first entry','p.472 l.10 worthy of interest or worth interest'),('472 second row first entry','l 12 satisfy the'),('472 second row second entry','l-5 doesn\'t .'),
('474 first row first entry','p 474 l.3 its (times2). also l4.'),('474 first row middle entry','l-9 its'),('474 first row last entry','l-8 doesn\'t'),('474 second row first entry','l-6 corrected its; doesn\'t'),('474 second row final entry','l-5 commute points with'),
('475 entry','475 l4 after diagram (ambiguous reference prime) commutes with'),
('476 introduction','p.476 cancelled Poss. l.4 slight possible ambiguity'),('476 continuation','I think you mean the only condition, it seems, to impose'),('476 continuation next line','i.e that we cancelled a/e need to impose'),('476 final prose line','unattached pronoun it'),('476 l-14 comment','good crop of cancelled its, it\'s to be replaced by its in this locality'),('476 final short entry','l-2 isn\'t'),
('477 first entry','p477 l8 analogue'),('477 second entry','l-7 apparent'),('478 first entry','p478 l13 quasi-isomorphism'),('478 second entry','l15 its'),('478 third entry','l-15 its'),('478 second row','l-5 quasi-isomorphism'),
('479 first entry','p479 l2 don\'t'),('479 second entry','l-3 developing'),('480 first entry','p480 l13 its & l.14.'),('480 second entry','l-17 isn\'t'),('480 third entry','l-15 can\'t'),('480 second row first entry','l-12 its we\'ve got'),('480 second row middle entry','l-7 developing'),('480 second row right entry','l-4 won\'t'),('480 third row','l-2 doesn\'t'),
('481 first entry','p481 l6 hadn\'t'),('481 second entry','l8 didn\'t'),('481 third entry','l9 wasn\'t'),('481 l10 original wording','yet... (136). reads badly'),('481 proposed revision','I suggest finished, yet I\'d only got upto formula (136).'),('481 parenthetical comment','I\'d almost suggest (136)! but some might think it was factorial136!'),('481 final row first entry','l12, doesn\'t'),('481 final row second entry','l.13 from starting'),('481 final row third entry','l-12 isn\'t'),('482 first entry','p.482 l.2 its'),('482 second entry','l15 ones (times2).')]
for p,w in entries: elem('text',p,w)
for p,w in [
('above 471 reads/badly','very with angular cue'),('above end of 471 badly and following ampersand','(too many negatives)'),('above cancelled 471 expect/much gap','live too with lower angular cue'),('above cancelled ook in471 N.B.','aken'),('above 476 possible','slight with lower angular cue')]:elem('insertion',p,w)
for p,w in [
('471 rejected opening, quotation strokes live','I wouldn\'t expect and much'),('471 N.B. old ending','ook'),('471 request beneath N.B.','entire so ... correct, period live'),('474 l-6 initial glyph space','old p/i overwritten by live i'),('476 before l.4','Poss.'),('476 after live we','a/e'),('476 l-14 old contraction','its')]:elem('deletion',p,w)
for p,w in [
('vertical beside page references','long thin left rule; pale lower segment'),('near right edge, through some long text lines','long thin right rule'),('left margin at468/469','one isolated dark point'),('high just right of471 l.-14','one small detached dark point'),('blank above471 This sentence','one isolated dark point'),('left margin below476 unattached line','one compact dark point'),('479 l2 below-right of reference','one isolated dark point'),('481 l8 reference','two detached small points'),('481 first i in didn\'t','low short horizontal mark with dotless letter body')]:elem('drawing',p,w)
elem('margin note','lower right archive corner','32, recorded as an archive-sheet comment','another unnamed hand (archive pencil)')

notes=[
'Handwritten English corrections cover references p468 through p482; the archive corner number is32, not a manuscript text-page heading.',
'At471 the writer calls the sentence very bad, adds (too many negatives), and says it is not without ambiguity. A cancelled false start is followed by a proposal concerning a smooth complex X_* satisfying the Kan condition, a group object G=bar(pi)_1(X_*) in U(k), and a submersion(H). This is phrased as what the writer would expect, not as a proved theorem.',
'The N.B. says the writer may have mistaken the intended sense; a following request for checking is cancelled. Deletion extent is certain even though six words remain lexically doubtful.',
'At476 the writer qualifies possible ambiguity or incoherence as slight and attributes it to lack of commas; the suggested comma placement is followed by a comment about an unattached pronoun. The unmatched outer quotation after unattached is retained.',
'At481 the suggested wording ends finished, yet Id only got upto formula(136). The following parenthetical hesitates over an exclamation mark because some might read factorial136!. No mathematical assertion in471 is proved here.',
'Quasi-isomorphy at469 ends in y. Quasi-isomorphism at478 is separately retained. Upto at481 is one written word. The repetition counts at474 and482 are both times2.',
'There is no diagram drawn on this page;475 merely refers to a diagram with a primed label. The two long thin rules and distinct dark points are reproduced geometrically. Pale circular impressions at upper and lower right are treated as material features, not as ink diagrams.'
]
report=dict(scan=33,reader='A',model='GPT-6 Astra Pro',effort='not exposed',viewed=F['viewed_once'],layout=F['layout'],changes=changes,c_doubts=decisions,remaining_doubts=remaining,inventory=inv,notes=notes,math_checks=[],notation=notation,abbreviations=[dict(form='p / p.',expansion='page',place='page references468–482'),dict(form='l / l.',expansion='line',place='line references throughout'),dict(form='N.B.',expansion='nota bene',place='471 qualification'),dict(form='i.e',expansion='id est',place='476 paraphrase'),dict(form='Poss.',expansion='possibly or possible, tentative only',place='476 cancelled false start')],brief_feedback='Whole and supplied halves each viewed exactly once. Twenty-two local loci were frozen before generating one crop each with the required script; all22 generated crops were displayed once. The continuously overcancelled request was treated as one visual locus because common crossing strokes cover its entire single line; its eight lexical decisions are reported individually. H has desc status, so no H collation rows were manufactured. Crop09 and crop22 do not include the complete upper origin of adjacent descending components; quote counts therefore remain uncertain, with no absence asserted. Full inventory covers54 text entries/blocks plus every nested insertion/deletion, drawn rule/point group and the archive comment. No OCR, external research, compilation, other page images, other reader outputs or theorem checks were used.')
(O/'reading.tex').write_text(reading)
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(O/'literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),reading.splitlines(True),fromfile='C.tex',tofile='A/reading.tex')))
summary={'crops_generated':len(L),'crops_viewed':len(L),'change_places':len(changes),'doubt_decisions':len(decisions),'explicit_C_uncertainty_decisions':15,'remaining_doubts':len(remaining),'inventory_elements':len(inv),'text_inventory_elements':len(entries),'math_checks':0}
(O/'counts.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
