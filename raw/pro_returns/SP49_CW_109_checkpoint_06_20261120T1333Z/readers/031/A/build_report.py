from pathlib import Path
import json, difflib, re
ROOT=Path('/workspace/scratch/6d55c8c3e5a7')
OUT=ROOT/'work/readers/031/A'
META=json.loads((ROOT/'work/inputs/031/metadata.json').read_text())
C=(ROOT/'work/inputs/031/C.tex').read_text()
text=C
frozen=json.loads((OUT/'unresolved_frozen.json').read_text())['loci']
loci={r['id']:r for r in frozen}
changes=[]
def change(id,place,c,reading,kind,evidence,crop=None,source=None,bbox=None,confidence='high'):
 global text
 assert text.count(c)==1,(id,text.count(c),c)
 text=text.replace(c,reading)
 if crop:
  q=loci[crop]; source=q['source']; bbox=q['bbox']; crop=str(OUT/q['crop'])
 changes.append({'id':id,'place':place,'c':c,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,'crop':crop,'source':source,'bbox':bbox})

raised_its=r"""\tikz[baseline=(old407A.base)]{\node[inner sep=0pt] (old407A) {\deleted{\unsure{the|its}}};\node[anchor=base west,inner sep=0pt] at ([xshift=1.1em,yshift=1.5ex]old407A.base west) {\inserted{its}};}"""
over_as=r"""\tikz[baseline=(oldi407A.base)]{\node[inner sep=0pt] (oldi407A) {\deleted{\unsure{i}}};\node[anchor=base west,inner sep=0pt] at (oldi407A.base west) {a};}s"""
pp_insert=r"""\tikz[baseline=0pt,x=1ex,y=1ex]{\path[use as bounding box] (-.2,-.2) rectangle (.7,1.2);\draw[line width=.35pt,line cap=round] (.05,.9)--(-.15,-1.4)--(-.05,-.8)--(.55,-1.25);\node[anchor=base,inner sep=0pt] at (.25,2.2) {\inserted{a p.p of}};}"""
up_ditto=r"""\tikz[baseline=(ditto408A.base)]{\node[inner sep=0pt] (ditto408A) {''};\node[anchor=base,inner sep=0pt] at ([xshift=-.2em,yshift=1.6ex]ditto408A.base) {$\uparrow$};} \quad ''"""
identical_point=r"""\tikz[baseline=(ident408A.base)]{\node[inner sep=0pt] (ident408A) {``identical''};\fill ([xshift=3.8em,yshift=.5ex]ident408A.base east) circle (.045ex);}"""
over_its=r"""``i\tikz[baseline=(olds409A.base)]{\node[inner sep=0pt] (olds409A) {\deleted{\unsure{s}}};\node[anchor=base west,inner sep=0pt] at (olds409A.base west) {t};}s''"""
over_do=r"""\tikz[baseline=(oldt412A.base)]{\node[inner sep=0pt] (oldt412A) {\deleted{\unsure{t}}};\node[anchor=base west,inner sep=0pt] at (oldt412A.base west) {d};}o"""
p416point=r"""\tikz[baseline=(p416A.base)]{\node[inner sep=0pt] (p416A) {p 416};\fill ([xshift=.45em,yshift=.95ex]p416A.base east) circle (.045ex);}"""
margin420=r"""\margin{\tikz[x=1ex,y=1ex]{\fill (0,0)--(.06,.07)--(.13,.01)--(.07,-.035)--cycle;\fill (.26,.42) ellipse (.05 and .065);}}"""
in422=r"""\tikz[baseline=0pt,x=1ex,y=1ex]{\path[use as bounding box] (0,0) rectangle (.65,1.1);\draw[line width=.35pt,line cap=round] (.25,1.3)--(.25,-.8)--(.48,-.65);\node[anchor=base,inner sep=0pt] at (0,2.0) {\inserted{in}};}"""

change('A031-01','402, reference before hatted A',r"""l \unsure{$\downarrow$6|16}""",r"""l $\downarrow$6""",'misread symbol or index','The long sloping shaft ends in two short upward-returning strokes at the foot, forming a down-arrow head; the separate following 6 is closed.','02')
change('A031-02','403 l.4, cancelled word',r"""\deleted{\unsure{own}}""",r"""\deleted{own}""",'misread word','A left oval, two central troughs and the final n shoulder survive the cancellation. The opening and closing quotes stand outside the old word.','03',confidence='medium')
change('A031-03','404, third line reference',r"""l.-5 ``analogue''""",r"""l.\unsure{+|-}5 ``analogue''""",'misread symbol or index','The point after l is separate. The following horizontal sign has a distinct short pendant stroke near its middle; a plus is favoured, but a retraced or accidentally thickened dash remains possible.','04',confidence='medium')
change('A031-04','405 l-9, opening quotation',r"""l-9 ``didn't''""",r"""l-9 \unsure{``|`}didn't''""",'misread symbol or index','The high opener is one fused curved body with two rightward arms. Its physical count is not securely one versus two; the closer has two separate strokes.','05',confidence='medium')
change('A031-05','407 l-15, raised replacement its',r"""\deleted{\unsure{the|its}} \inserted{its}""",raised_its,'insertion or placement','The live its is above and somewhat to the right of the crossed word, rather than on its baseline. The old word remains the/its uncertain because the cancellation crosses its middle.','07')
change('A031-06','407 continuation, corrected as',r"""\deleted{\unsure{i}}as""",over_as,'insertion or placement','The surviving old upright and dot occupy the same initial-glyph space as the live a; s is shared only once. The older i remains uncertain.','08')
change('A031-07','407 continuation, a p.p of',r"""\inserted{a p.p of}""",pp_insert,'insertion or placement','The added words stand above the gap between as and relier. A long local connector descends through the gap and turns at its foot; the code preserves that geometry and the raised words. There is one point between the two p letters and no second final abbreviation point.','08')
change('A031-08','407 continuation, relier opening quotation',r"""`relier''""",r"""``relier''""",'misread symbol or index','The opening group below the raised second p has two pointed legs, distinct from the descender of that p. Two closing strokes also remain visible.','08',confidence='medium')
change('A031-09','408, first line reference',r"""408 l.3 below""",r"""408 l3 below""",'text not on the page','The complete gap between the l foot and numeral 3 is visible and contains no independent stop.','09')
change('A031-10','408 l3, punctuation after copy',r"""last e missing in copy.""",r"""last e missing in copy,""",'misread symbol or index','The low mark has a vertical upper body and a bent descending tail to the left, rather than an isolated round stop.','10')
change('A031-11','408 l.4, pointer above first ditto',r"""\unsure{$\uparrow$|`} '' \quad ''""",up_ditto,'insertion or placement','There is an upward-pointing head on a short shaft, raised above and slightly left of the first ditto pair. Both ditto groups contain two strokes; the second pair joins at the top.','11')
change('A031-12','408 l.4, isolated point right of identical',r"""``identical''""",identical_point,'omission','A small isolated dark point stands well to the right of identical, approximately at mid-letter height. It is reproduced geometrically without assigning a punctuation function or origin.',source=META['half_a'],bbox=[935,980,971,1020])
change('A031-13','409 l-1, under-writing in its',r"""l-1 ``its''""",'l-1 '+over_its,'deletion state (struck given live or live given struck)','The existing crop for this word separates an s-like upper-left loop and lower-right loop beneath the live t stem and its long crossbar. I preserve an uncertain overwritten s in the same space, rather than silently dropping the extra loops. This body detail was recognized within the one already prescribed crop; no extra crop or second viewing was made.','13',confidence='medium')
change('A031-14','410, first cancelled reference and quotation',r"""\deleted{l.\unsure{2} ``its''}""",r"""\deleted{l.2} ``\deleted{its''}""",'deletion state (struck given live or live given struck)','The old numeral has a visible curved top, descending diagonal and returned foot, reading 2. The paired opening quotation strokes sit above the cancellation paths; the words and the terminal quote group meet the returning crossing.','14',confidence='medium')
change('A031-15','410 l2, high mark after being',r"""\unsure{`|''}\ldots{}""",r"""\unsure{''|`}\ldots{}""",'misread symbol or index','Two pendant ends favour a fused double closer, but a single branched stroke remains possible. The three low dots are independently distinct and are unchanged.','16',confidence='medium')
change('A031-16','410 l2, second cancelled quoted word',r"""\deleted{``\unsure{its}''}""",r"""``\deleted{\unsure{its}}\unsure{\deleted{''}|''}""",'deletion state (struck given live or live given struck)','The opening pair is clear above-left of the cancellation envelope. The closer meets the terminal diagonal unevenly, so its deletion state remains uncertain. The old word still reads only tentative its from the surviving uprights and low s curve.','17',confidence='medium')
change('A031-17','410 l17, opening quotation',r"""l 17 `shouldn't''""",r"""l 17 ``shouldn't''""",'misread symbol or index','One long high opening stroke and one separate short high stroke are visible before s, with blank area around both.','18')
change('A031-18','411 l19, punctuation after copy',r"""e lost off end of line in copy .""",r"""e lost off end of line in copy \unsure{,|.}""",'misread symbol or index','The terminal low mark has a short left-to-right head turning downward at the right. A comma is favoured, but a dragged stop cannot be excluded.','20',confidence='medium')
change('A031-19','411 l-4 & -3, punctuation after p.407',r"""c.f comment on p.407.""",r"""c.f comment on p.407,""",'misread symbol or index','The terminal mark has a rounded high head followed by a separate-looking lower-left continuation, reading a comma. The internal stop after p remains unchanged.','21',confidence='medium')
change('A031-20','412 l.9, opening quotation of first formulary',r"""p 412 l.9. ``formulary''""",r"""p 412 l.9. \unsure{``|`}formulary''""",'misread symbol or index','The opener has a tall left stroke and shorter rising right arm joined at the foot. It may be a joined pair or one hooked stroke.','22',confidence='medium')
change('A031-21','412 l.12, corrected initial of do',r"""\deleted{\unsure{t}}do""",over_do,'insertion or placement','The older bar/stem and the live d occupy one letter-space; only one o follows. The old t remains tentative because its strokes merge into the new d.','23')
change('A031-22','413 l-2, closing quotation of wont',r"""``won't''""",r"""``won't\unsure{''|'}""",'misread symbol or index','After the t and beyond the pale vertical material trace, the closer is a tall stroke joined to a short rightward arm. A pair with a joined second member and a single hooked closer remain possible.','24',confidence='medium')
change('A031-23','416, raised isolated point after page number',r"""p 416 l-1.""",p416point+' l-1.','omission','A separate dark round point stands above the numeral baseline to the right of 416 and left of the material trace. It is retained at its observed height without converting it to a baseline stop.','25')
change('A031-24','417 l1, cancelled false start before (84)',r"""\deleted{\unsure{l 1}}(84)""",r"""\deleted{l 1}(84)""",'misread word','A tall looped l and a second short straight upright with a returned foot survive the two cancellation lines; they read l 1.','26',confidence='medium')
change('A031-25','419 l.6, opening quotation of make sense',r"""l.6 `make sense''""",r"""l.6 \unsure{`|``}make sense''""",'misread symbol or index','The high opener is a single joined fork with a long left portion and short rising arm. One mark is favoured, while a fused pair remains possible.','27',confidence='medium')
change('A031-26','419, final dont opening quotation',r"""\quad `don't''""",r"""\quad ``don't''""",'misread symbol or index','Two distinct high strokes are separated by a visible pale gap before d.','28')
change('A031-27','420, right margin at level of usual',r"""p 420 l.10 ``made up of'' is more usual.""",r"""p 420 l.10 ``made up of'' is more usual."""+margin420,'omission','Two small dark marks stand diagonally, the upper one to the right of the lower one, just left of the pale vertical material trace. They are drawn separately with origin and function unassigned.','29')
change('A031-28','422, raised in and connector after again',r"""again \inserted{in} l.14.""",'again '+in422+' l.14.','insertion or placement','The word in is above the gap after again, over a long vertical connector with a hooked lower end. The connector reaches below the writing line. The final formulary quotation is a joined pair and remains unchanged.','30')
change('A031-29','425 l.11, opening quotation of its',r"""l.11 `its''""",r"""l.11 \unsure{``|`}its''""",'misread symbol or index','The opening group has two descending legs meeting at a pointed top, favouring a joined pair; a single forked stroke remains possible. Its separate i-dot is not included in the quotation.','32',confidence='medium')

text='\\cotefile{109}\n'+text
text=text.replace('% archive sheet number: 30','% Two near-vertical material creases and faint right-margin circular paper features are not transcribed as ink.\n% archive sheet number: 30')
(OUT/'reading.tex').write_text(text)

c_doubts=[]
def doubt(place,c,reading,resolved,evidence,crop=None,source=None,bbox=None,confidence='high',category='literal C uncertainty'):
 if crop:
  q=loci[crop];source=q['source'];bbox=q['bbox'];crop=str(OUT/q['crop'])
 c_doubts.append({'place':place,'c':c,'reading':reading,'resolved':resolved,'confidence':confidence,'evidence':evidence,'crop':crop,'source':source,'bbox':bbox,'category':category})
doubt('402 hatted-A reference',r"""\unsure{$\downarrow$6|16}""",r"""$\downarrow$6""",True,'The two short strokes at the foot form a down-arrow head on the long diagonal shaft.','02')
doubt('403 l.4 old word',r"""\deleted{\unsure{own}}""",r"""\deleted{own}""",True,'The oval o, two w troughs and final n shoulder can be followed separately despite cancellation.','03',confidence='medium')
doubt('407 l-15 old word',r"""\deleted{\unsure{the|its}}""",r"""\deleted{\unsure{the|its}}""",False,'A tall first stem and looped middle favour the, but the crossing hides the joins required to reject its. Live raised its does not settle the buried letters.','07',confidence='low')
doubt('407 initial under as',r"""\deleted{\unsure{i}}as""",over_as,False,'A separate dot and old upright remain under the a. The precise old body remains uncertain; only the overlapping placement is corrected.','08',confidence='medium')
doubt('408 l.4 high mark',r"""\unsure{$\uparrow$|`}""",r"""$\uparrow$""",True,'A pointed top with two oblique arms and a lower shaft is distinct from the two ditto strokes beneath it.','11')
doubt('410 first cancelled numeral',r"""\unsure{2}""",'2',True,'The top bend, descending diagonal and returned bottom remain legible as 2.','14',confidence='medium')
doubt('410 high mark after being',r"""\unsure{`|''}""",r"""\unsure{''|`}""",False,'The fused high body has two pendant ends, making a pair the first candidate; the single branched-stroke alternative remains.','16',confidence='medium')
doubt('410 second cancelled its',r"""\unsure{its}""",r"""\unsure{its}""",False,'The cancellation passes through the upper joins and leaves only partial uprights and a low right curve. The earlier readable its is not used to resolve this occurrence.','17',confidence='low')
doubt('412 l.12 old initial',r"""\deleted{\unsure{t}}do""",over_do,False,'A bar and upright compatible with t overlap d; the shared o is clear.','23',confidence='low')
doubt('417 false start',r"""\deleted{\unsure{l 1}}""",r"""\deleted{l 1}""",True,'The tall loop and second straight short upright can be separated from the diagonal cancelling strokes.','26',confidence='medium')
doubt('423 first page-reference glyph',r"""\unsure{p|l}""",r"""\unsure{p|l}""",False,'The long descender has a small rightward thickening near its top but no recoverable open bowl. The tiny separated upper component does not securely decide p versus l.','31',confidence='low')

def context(place,c,reading,evidence,crop=None,source=None,bbox=None,confidence='high'):
 doubt(place,c,reading,True,evidence,crop,source,bbox,confidence,'C_context confirmation')
context('402, hatted A and both lowered letters',r"""$\hat{A}_{ab}$""",r"""$\hat{A}_{ab}$""",'The roof sits over the ordinary A alone. The lowered a is closed, followed by a b with upright and right bowl.',source=META['half_a'],bbox=[741,116,859,211])
context('407 l-15, insertion its',r"""\inserted{its}""",r"""\inserted{its}""",'The raised word reads its. Its physical height is preserved in the changed local TikZ layout.','07')
context('407 continuation, insertion a p.p of',r"""\inserted{a p.p of}""",r"""\inserted{a p.p of}""",'Raised letters and the connecting stroke identify an insertion between as and relier; the abbreviation has only its medial point.','08')
context('422 after again, insertion in',r"""\inserted{in}""",r"""\inserted{in}""",'Raised in has a separate i-dot and two low strokes, above the vertical connector pointing to the gap.','30')
context('411 reference abbreviation',r"""c.f""",r"""c.f""",'There is a point between c and f but none after f before comment. The generic C_context list does not license adding the absent final stop.',source=META['half_b'],bbox=[777,249,1029,301])
context('408 l.4, two ditto groups',r"""'' \quad ''""",r"""'' \quad ''""",'Both positions contain two strokes; the second pair joins at the top. The up-arrow is a distinct raised object.','11')
context('411 negative line references',r"""l-4 \& -3""",r"""l-4 \& -3""",'The joining sign is a loop with a crossing stroke between the two negative references.',source=META['half_b'],bbox=[251,240,506,304])
context('413 formula reference',r"""$(75)e$""",r"""$(75)e$""",'The e follows the closing parenthesis on the same writing baseline, not above it.',source=META['half_b'],bbox=[660,432,900,505])
context('417 formula reference',r"""$(84)e$""",r"""$(84)e$""",'This e also occupies the baseline independently of the earlier occurrence.',source=META['half_b'],bbox=[252,682,476,759])
context('402 missing-index comment',r"""(the ab is missing.)""",r"""(the ab is missing.)""",'Both letters ab are written in the comment; a low point precedes the closing parenthesis.',source=META['half_a'],bbox=[876,139,1300,216])
context('407 l3 missing-letter note',r"""``categorie\uline{s}'' the s is missing on my copy.""",r"""``categorie\uline{s}'' the s is missing on my copy.""",'Final s is present in the example and singly underlined; the prose explicitly says it is missing on the copy.',source=META['half_a'],bbox=[337,712,1089,784])
context('408 l3 missing-letter note',r"""``see'' - last e missing in copy.""",r"""``see'' - last e missing in copy,""",'The note specifies last e. Only its terminal punctuation is revised after the dedicated crop.','10')
context('411 l19 missing-letter note',r"""e lost off end of line in copy .""",r"""e lost off end of line in copy \unsure{,|.}""",'The visible wording says e lost off end of line, without a further corrected position. Its terminal mark is locally uncertain.','20')
context('407 parenthetical qualification',r"""(however I feel it should be not ``around'' but perhaps ``on and around'')""",r"""(however I feel it should be not ``around'' but perhaps ``on and around'')""",'The words however, I feel and perhaps are all present; the final parenthesis is visible and no extra final stop is supplied.',source=META['half_a'],bbox=[257,577,1453,708])
context('407 proposed translation qualification',r"""suggests a translation as ``binding''""",r"""suggests a translation as ``binding''""",'The prose says suggests a translation as; it is not silently recast as a categorical equivalence.',source=META['half_a'],bbox=[528,833,1307,910])

remaining=[
('404 third line reference',r"""l.\unsure{+|-}5""",'+ versus -','medium','A short pendant stroke interrupts the horizontal sign.'),
('405 l-9 opener',r"""\unsure{``|`}didn\'t''""",'double versus single opener','medium','The opening group is fused into a curved two-arm body.'),
('407 old word before old French origin',r"""\deleted{\unsure{the|its}}""",'the versus its','low','The cancellation hides decisive middle joins.'),
('407 older initial under a',r"""\deleted{\unsure{i}}""",'tentative i','medium','Dot is separate but the old body merges with a.'),
('409 l-1 under-writing',r"""\deleted{\unsure{s}}""",'tentative overwritten s','medium','Two old loops are visible, but the live t obscures their central join.'),
('410 after being',r"""\unsure{\'\'|`}\ldots{}""",'double closer versus single raised stroke','medium','The two pendant ends share a dense upper join.'),
('410 second cancelled word',r"""\deleted{\unsure{its}}""",'tentative its','low','Multiple cancellation strokes obscure the letter sequence.'),
('410 second cancelled closer',r"""\unsure{\deleted{''}|''}""",'deleted versus live closing pair','medium','The terminal diagonal crosses the first component unevenly and passes beside the other.'),
('411 terminal mark after copy',r"""\unsure{,|.}""",'comma versus period','medium','A low wedge turns downward but could be a dragged stop.'),
('412 l.9 first formulary opener',r"""\unsure{``|`}formulary''""",'double versus single opener','medium','Tall and short arms share one lower turn.'),
('412 old initial of do',r"""\deleted{\unsure{t}}""",'tentative t','low','The top bar and upright overlap the new d.'),
('413 l-2 wont closer',r"""won't\unsure{''|'}""",'double versus single closer','medium','The upright meets a horizontal rightward arm.'),
('419 l.6 make sense opener',r"""\unsure{`|``}make sense''""",'single versus double opener','medium','One high fork remains physically joined.'),
('423 page-reference initial',r"""\unsure{p|l}""",'p versus l','low','The long shaft has only a tiny rightward thickening, not a recoverable bowl.'),
('425 l.11 its opener',r"""\unsure{``|`}its''""",'double versus single opener','medium','Two legs meet at the high point; the independent i-dot is excluded.')]
remaining=[{'place':p,'reading':r.replace("\\'","'"),'alternatives':a,'confidence':cf,'reason':why} for p,r,a,cf,why in remaining]

inventory=[]
def inv(id,kind,pos,first,hand='his hand',transcribed='yes'):
 inventory.append({'sheet_kind':'list','hand':hand,'element':id,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':transcribed})
rows=[
('01','text','Top line, first entry','p.402 l.3 analogue'),('02','text','Top line, middle entry','l 7 commutes with'),('03','text','Top line, right entry',"l 14 don't"),
('04','text','Second line, left entry',"l.17 didn't"),('05','text','Second line, middle/right entry','l down-arrow6; hatted A with low ab; missing-index comment'),
('06','text','Third line, first entry','p 403 l.2 analogue'),('07','text','Third line, second entry','l.4 its own'),('07a','deletion','Within 403 l.4 quotation','own'),
('08','text','Third line, third entry','l.8 its'),('09','text','Third line, last entry','l 16 analogue'),
('10','text','404 first entry',"l 11 wouldn't"),('11','text','404 middle entry',"l-12 haven't"),('12','text','404 right entry','l. plus/minus5 analogue'),
('13','text','405 left entry','l.11 commutes with'),('14','text','405 right entry',"l-9 didn't"),
('15','text','407, five-line prose paragraph','The word formulaire is not English; formulary; magic spells; however; perhaps on and around'),
('16','text','407, first entry below paragraph','l 3 categories; the s is missing on my copy'),('16a','text','Nested in categories','Single underline beneath final s'),
('17','text','407, right entry on same line','l-15 its'),
('18','text','407, two-line entry below categories','l-15 relying is not used in this sense; old French origin; suggests a translation as binding'),
('18a','deletion','407 before old French origin','the/its'),('18b','insertion','407 above crossed old word','its'),
('18c','deletion','407 continuation, under live initial of as','tentative i under a'),('18d','insertion','407 raised above as/relier gap','a p.p of'),('18e','drawing','407 as/relier gap','Long insertion connector with bent lower branch'),
('19','text','408 first entry','l3 below diagram - see - last e missing in copy'),('20','text','408 second entry','l.4, two ditto groups, identical'),
('20a','drawing','408 second entry, above first ditto','Up-arrow'),('20b','drawing','408 second entry, right of identical','Isolated dark point'),
('21','text','409 first entry','p 409. l 12 its'),('22','text','409 second entry',"l-12 doesn't"),('23','text','409 third entry',"l-3 don't feel that I have understood"),
('24','text','409 next line, first entry',"l-2 hasn't"),('25','text','409 next line, second entry','l-1 its'),('25a','deletion','409 l-1, beneath t','Tentative s-shaped under-writing'),
('26','text','410, cancelled first entry','l.2 its'),('26a','deletion','410 first cancelled entry, reference','l.2'),('26b','deletion','410 first cancelled entry, quoted text and closer','its and closing quotation'),
('27','text','410 live l2 entry','it before being; high quote group and three dots'),('27a','text','Nested in live 410 l2 entry','Single underline under before'),
('28','deletion','410, second cancelled quoted group','Tentative its; closer deletion state uncertain; opener live'),
('29','text','410 l17 entry',"shouldn't"),('30','text','410 next line, l19 entry',"shouldn't"),('31','text','410 next line, l-8 entry','commuting with again in l-7'),
('32','text','411 first entry','l 19 accurately; e lost off end of line in copy'),('33','text','411 second entry','l-4 & -3 formulary; c.f comment on p.407'),
('34','text','412 first entry','l.9. formulary again in l12'),('35','text','412 second entry, continued on next line','l.12 do replace forgetting by to get'),('35a','deletion','412 initial of do','Tentative t overwritten by d; one shared o'),('36','text','412 final entry','l.-14 formulary'),
('37','text','413 first entry','l 6 formulary'),('38','text','413 formula-reference entry','In (75)e commutes with'),('39','text','413 next line, first entry','l-9 with small'),('40','text','413 next line, second entry','l-7 commuting with'),('41','text','413 next line, third entry',"l-2 won't"),
('42','text','415 entry','l.-10 formula'),('43','text','416 entry','l-1. formulary'),('43a','drawing','416, after page reference at raised height','Isolated dark point'),
('44','text','417 first entry','In (84)e commutes with'),('45','text','417 second entry continuing to next line',"l 1 after cancelled l1 (84) formulary doesn't"),('45a','deletion','417 after, before second (84)','l 1'),
('46','text','419 first entry','l.6 make sense'),('47','text','419 second entry',"l.8 doesn't"),('48','text','419 third quoted item without own reference',"don't"),
('49','text','420 entry','l.10 made up of is more usual'),('49a','drawing','420 level, far right margin','Two separated diagonal dark points'),
('50','text','421 entry','l 7 interpret'),('51','text','422 entry','l 13 formulary again in l.14'),('51a','insertion','422, above gap after again','in'),('51b','drawing','422 gap after again','Vertical insertion connector with hooked foot'),
('52','text','423 entry','l-4 above diagram 105 its'),('53','text','425 final entry','l.11 its also in l-7')]
for row in rows: inv(*row)
inv('54','margin note','Lower right corner','Archive sheet number 30, preserved as comment','another unnamed hand (archive pencil)')

notation=[
{'sign':r"""$\downarrow$6""",'location':'402 reference before hatted A','reading':r"""$\downarrow$6""",'evidence':'Crop02: two arms return upward from the foot of the sloping shaft, followed by separate 6.'},
{'sign':r"""$\hat{A}_{ab}$""",'location':'402 second line','reading':r"""$\hat{A}_{ab}$""",'evidence':'Half a: single ordinary A; separate two-stroke roof; lowered closed a and stemmed b.'},
{'sign':r"""\unsure{+|-}""",'location':'404 third reference','reading':r"""l.\unsure{+|-}5""",'evidence':'Crop04: a separate low stop after l, then horizontal sign with a short central pendant stroke.'},
{'sign':r"""\uline{s}; \uline{before}""",'location':'407 categories; 410 live l2','reading':r"""categorie\uline{s}; \uline{before}""",'evidence':'Crop06 and crop15 show one rule in each location; before has a thick retraced band, not two separated rules.'},
{'sign':r"""$\uparrow$; '' \quad ''""",'location':'408 l.4','reading':up_ditto,'evidence':'Crop11: upward head and shaft above the first of two independently paired ditto groups.'},
{'sign':r"""\&""",'location':'411 line-reference pair','reading':r"""l-4 \& -3""",'evidence':'Half b: looped joining sign with a cross-stroke.'},
{'sign':'(75)e; (84)e','location':'413 and 417, separately','reading':r"""$(75)e$; $(84)e$""",'evidence':'Half b: both e glyphs follow closing parentheses on the writing baseline.'},
{'sign':'quotation groups','location':'All quotations; changed local groups itemized in changes','reading':'Paired strokes remain paired where separable; single or fused groups are locally marked without propagating certainty.','evidence':'Crops01,03,06,12,13,18,19,28,30 resolve local pairs; crops05,16,22,24,27,32 leave local count doubts.'},
{'sign':'overlapping old/new initials','location':'407 as; 409 its; 412 do','reading':over_as+'; '+over_its+'; '+over_do,'evidence':'Crops08,13,23: each old/new body occupies one physical glyph space; shared adjacent letters are printed once.'},
{'sign':'isolated dark marks','location':'408 right of identical; 416 after page number; 420 right margin','reading':identical_point+'; '+p416point+'; '+margin420,'evidence':'Half a and crops25/29 preserve separate geometry, with no assigned punctuation function or origin.'},
{'sign':'three continuation points','location':'410 after being','reading':r"""\ldots{}""",'evidence':'Crop16: three separate low dark marks.'},
{'sign':'material vertical traces','location':'Approximately x211–235 and x1485–1508 through the page','reading':'Material creases, not transcribed as ink rules.','evidence':'Whole and halves show dark upper portions fading to pale strips. Crops33/34 show thin dark nuclei with broad light/dark material edges; lower contextual portions of crops24/25/29 show the same surface trace.'}
]

report={'scan':31,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed','viewed':[META['whole'],META['half_a'],META['half_b']],
'layout':'One handwritten sheet containing a dense English correction list for typescript page references 402 through 425. Twenty distinct page references are visible. The main writing is in one consistent hand, with a narrow left reference area and prose extending across most of the page; p407 has a five-line prose paragraph and a later two-line etymological note. There are no standalone displays or mathematical diagrams. Raised additions occur at p407 (its; a p.p of) and p422 (in); local cancellations/over-writing occur at p403, p407, p409, p410, p412 and p417. Two near-vertical material crease traces run from approximately (211,95) to (235,2332) and (1485,95) to (1508,2321), dark above and much paler below. Their appearance in crops33/34 and lower contextual crops supports material traces rather than ink rules, so they are not redrawn. Faint circular right-margin paper features near whole y155 and y2255 likewise are not treated as text. Separate dark marks at 408,416,420 are retained geometrically. Archive pencil 30 is in the lower right and appears only as a comment.',
'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
'notes':[
'The sheet lists wording corrections for twenty typescript page references: 402,403,404,405,407,408,409,410,411,412,413,415,416,417,419,420,421,422,423,425. The handwritten archive corner number is 30.',
'At p407 the writer says formulaire is not English, gives formulary = a collection of formulae, invokes a list of magic spells, and calls formulary an excellent word to use. The parenthetical qualification retains however, I feel and perhaps in suggesting on and around.',
'At p407 l-15 the writer says relying is not used in this sense. The raised a p.p of belongs before relier, and the note says its old French origin suggests a translation as binding; this is a qualified proposal.',
'Missing-copy notes concern ab at 402, final s in categories at 407, the last e of see at 408, and an e lost off the end of the line at 411. The last note supplies no more precise replacement position.',
'The quoted wording at 409 l-3 is dont feel that I have understood (with its apostrophe in the transcription). Its presence as a quoted correction is preserved without recasting it as a separate assertion about the writers comprehension.',
'At 412 l.12 the instruction is do replace forgetting by to get. References (75)e at 413 and (84)e at 417 retain e on the baseline.',
'Inventory coverage: each distinct correction entry, the p407 prose block, nested deletions/over-writings, raised insertions, insertion connectors, underline spans, isolated dark-mark groups and the archive annotation receive rows. There are no standalone display or diagram elements to inventory.'
],
'math_checks':[],
'notation':notation,
'abbreviations':[
{'form':'p.; p','expansion':'page (tentative interpretation only)','place':'Page references throughout'},
{'form':'l.; l','expansion':'line (tentative interpretation only)','place':'Line references throughout'},
{'form':'c.f','expansion':'compare / confer (tentative interpretation only)','place':'411 l-4 & -3'},
{'form':'p.p','expansion':'past participle (tentative interpretation only)','place':'407 raised a p.p of'}],
'brief_feedback':'The assigned whole and halves were each viewed exactly once. Thirty-four unresolved loci were frozen before any crop generation; each resulting crop was displayed singly once. No other page image or reader output was inspected; no OCR, PDF extraction, outside lookup, compilation or mathematical proof was performed. Crop13, prescribed for the last quote group of its, also exposed s-like under-writing in the included word body; that detail is reported rather than silently omitted, without making another crop. The two narrow material-trace crops are taller than ordinary word crops because their unresolved question was local line texture; their extent was judged only from the required whole/half views. H status is desc, so no H comparison rows are manufactured. Static checks and an exact C diff are saved separately; they are not counted as mathematical checks.',
'counts':{'changes':len(changes),'c_doubts':len(c_doubts),'literal_c_uncertainties':11,'literal_c_uncertainties_resolved':5,'literal_c_uncertainties_retained_or_revised':6,'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':len(frozen),'math_checks':0}}
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

crop_outcomes={
'01':'Two separate closing components and two openers confirm C analogue quotation.',
'02':'Resolve down-arrow6; hat and low ab independently legible.',
'03':'Resolve cancelled own; retain outer paired quotation.',
'04':'Keep dot after l; revise sign to plus/minus uncertainty because of pendant middle stroke.',
'05':'Opening quote count remains double/single uncertain.',
'06':'Two opening and two closing strokes; one underline under s. C confirmed.',
'07':'Old the/its remains uncertain; live its is raised and offset right.',
'08':'Old i under a remains uncertain; overlap retained. Raised a p.p of and connector reproduced. Relier opener resolved as paired.',
'09':'No independent stop between l and3; remove C period.',
'10':'Final copy mark reads comma from descending bent tail.',
'11':'Resolve upward arrow and raised position over first ditto. Both ditto groups paired.',
'12':'Two distinct opening strokes before dont confirm C.',
'13':'Closing pair confirmed. Existing crop additionally exposes tentative old s beneath t in its; report overlap.',
'14':'Resolve old2. Opener remains above cancellation; quoted word and terminal group cancelled.',
'15':'One thick, locally retraced underline under before; C single underline confirmed.',
'16':'Fused double closer favoured but single raised mark remains; three low dots clear.',
'17':'Old its retained uncertain. Opening pair live; closing deletion state uncertain.',
'18':'Two opening strokes (long and short) before shouldnt; replace C single opener.',
'19':'Long curved opener plus separate short partner confirms C double opener.',
'20':'Comma/period doubt for final copy mark.',
'21':'Comma after p.407; internal abbreviation point unchanged.',
'22':'Fused V-like opener remains double/single uncertain.',
'23':'Tentative old t and live d overlap; shared o once.',
'24':'Closer after wont remains double/single uncertain. Pale vertical trace is distinct from the quote.',
'25':'Separate raised point after416 retained geometrically; stop after l-1 distinct.',
'26':'Resolve cancelled l1 from looped l and short upright1.',
'27':'Single opener favoured but fused double retained as alternative.',
'28':'Two distinct opening strokes before dont; replace C single opener.',
'29':'Two separate diagonal dark marks retained with no origin/function assignment.',
'30':'Final formulary quote is joined pair. Raised in and long hooked connector preserved.',
'31':'p/l uncertainty retained for first reference glyph.',
'32':'Double/single opening quote doubt; i-dot independent; closer paired.',
'33':'Local dark/light material edge supports crease interpretation; do not redraw as ink rule.',
'34':'Local irregular dark nuclei and pale edge support material crease; do not redraw as ink rule.'}
(OUT/'crop_decisions.json').write_text(json.dumps([dict(q,decision=crop_outcomes[q['id']],displayed_once=True) for q in frozen],ensure_ascii=False,indent=2)+'\n')
with (OUT/'views.jsonl').open('a') as f:
 for i,q in enumerate(frozen,4):
  f.write(json.dumps({'order':i,'path':str(OUT/q['crop']),'stage':'single crop view','observed_once':True})+'\n')
(OUT/'literal_diff.patch').write_text(''.join(difflib.unified_diff(C.splitlines(True),text.splitlines(True),fromfile='C.tex',tofile='reading.tex')))
print(json.dumps(report['counts']))
