"""Main-reader adjudication of scan027. Original reader returns remain unchanged."""
from common import *
R=load_page(27);T={r:(W/f'readers/027/{r}/reading.tex').read_text() for r in 'ABC'}
CH={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
def a(i):return CH['A'][i]
def b(i):return CH['B'][i]
def c(i):return CH['C'][i]
def ap(i):return f'readers/027/A/crops/{i:02}.jpg'
def bp(i):return f'readers/027/B/crops/{i:02}.jpg'
def cp(s):return 'readers/027/C/crops/'+s+'.jpg'
text=T['A'];replacements=[]
def repl(old,new):
 global text
 assert old in text,old
 text=text.replace(old,new,1);replacements.append((old,new))
quote304=r"\deleted{\unsure{l-2} ``play'' \unsure{no|not} ``s}\unsure{\deleted{''}|''}"
repl(a('304-final-quotes')['reading'],quote304)
repl("313 l9 'shouldn't''",b('313-opening-quotes')['reading'])
raised313=r'\raisebox{1.1ex}[0pt][0pt]{\unsure{\deleted{\unsure{out|at|on|or}}|\unsure{out|at|on|or}}}'
ref313=r'\unsure{\deleted{l-2}|l-2|\deleted{l-7}|l-7}'
repl(a('313-cancelled-cluster')['reading'],r'\deleted{filtering} '+raised313+' '+ref313)
# The terminal point lies beyond the cancellation endpoint; the two lower dashes remain inside.
repl('}- -.} (This certainly','}- -}. (This certainly')
itsmark=r'''\tikz[baseline=(root27its.base)]{\node[inner sep=0pt] (root27its) {its};\draw[line width=.35pt,line cap=round] ([xshift=.01em,yshift=1.65ex]root27its.base west)--++(.05em,-.08ex)--++(-.01em,-.07ex);}'''
repl("l.17 ``its''",'l.17 ``'+itsmark+"''")
repl("317. l.11 'its''",b('317-opening-quotes')['reading'])
repl(r'\deleted{\&}',r'\deleted{\unsure{\&|l}}')
connector=b('326-raised-reference-and-connector')['reading']
repl(a('326-raised-addition-pointer')['reading'],connector)
repl(r"isn't\deleted{''} there!",r"isn't\deleted{\unsure{''|'}} there!")
repl(r"\deleted{wouldn't} should",r"\deleted{would'nt} should")
repl("l12 ``don't'' l-13",r"l12 \unsure{``|'}don't'' l-13")
repl('l.-13 ``semisimplicial.',r"l.-13 \unsure{``|'}semisimplicial\unsure{,|.}")
repl(r"enveloping\unsure{''|'}",r"enveloping\unsure{'|''}")
low5=r'\tikz[baseline=0pt,x=1ex,y=1ex]{\fill (.08,.08) circle (.04);}'
repl('l-5 ``enveloping','l-5'+low5+' ``enveloping')
upperpoints=b('329-upper-points')['reading']
repl(r'\raisebox{1.9ex}[0pt][0pt]{\inserted{l-5',upperpoints+r'\raisebox{1.9ex}[0pt][0pt]{\inserted{l-5')
# Isolated dark point below/right of note, separate from the material circular feature.
lowmargin=r'\fill (3.8,-3.3) circle (.035em);'
repl(r'\end{scope}\end{tikzpicture}}',r'\end{scope}'+lowmargin+r'\end{tikzpicture}}')

D=[]
def add(i,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True):
 D.append(dict(id='027-'+i,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
def pick(r,i,abc,evidence,crops,confidence=None,final=None):
 x=CH[r][i];add(i,x['place'],x['c'],final if final is not None else x['reading'],abc,evidence,crops,confidence or x['confidence'],x.get('kind','other'))
add('top15-retain','Faint opening line reference',r'l.\unsure{15}',r'l.\unsure{15}',[r'l.\unsure{15}',r'l.\unsure{15}','l.15'],
 'The lower curl favors5, but its upper contour is faint and incomplete. Root retains A/B and witness C uncertainty against reader C resolution; the page reference302 is independently still doubtful.',ap(1),'medium','other',False)
add('304-final-state','304, final quoted s',a('304-final-quotes')['c'],quote304,[a('304-final-quotes')['reading'],T['B'].split('304 l-15')[1].split('\n\n')[0],c('02-304-final-quotes')['reading']],
 'The two terminal quote strokes stand above the rising cancellation, but the cancellation continues below and beyond their horizontal position. Root retains cancelled/live state uncertainty rather than treating lack of direct contact as conclusive. Earlier pairs meet the crossing; s is cancelled.',ap(4),'low','deletion state (struck given live or live given struck)')
pick('A','306-old-l',[r'\deleted{l}']*3,'One tall loop and its low foot remain; there is no independent i point and second t. Root resolves l at medium confidence.',ap(6),'medium')
pick('A','312-old-reference',['l-6']*3,'Looped l, a separate short dash and the closed lower bowl and upward return of6 are visible beneath the crossing. Root resolves the reference, retaining the separate lets/lets-apostrophe doubt.',ap(7),'medium')
pick('B','313-opening-quotes',["313 l9 'shouldn't''",b('313-opening-quotes')['reading'],"313 l9 'shouldn't''"],
 'The opener has two adjacent descending legs, joined near the top but distinguishable below. Root follows B on a double opener; the internal apostrophe remains separate.',bp(9),'medium')
add('313-raised-state','313, small raised cluster after cancelled filtering',r'\deleted{filtering \unsure{out|at|on|or}}',r'\deleted{filtering} '+raised313,
 [a('313-cancelled-cluster')['reading'],b('313-raised-cluster')['reading'],c('05-313-raised-fragment')['reading']],
 'The short cluster stands above the old word. Its descending continuation meets the horizontal crossing, but the upper bodies lie clear of it; root keeps B’s state doubt as well as the independent letter alternatives. No caret or new insertion event is invented.',ap(8),'low','deletion state (struck given live or live given struck)')
add('313-reference-state','313, reference before live filtering',r'\unsure{l-2|l-7}',ref313,
 [r'\deleted{\unsure{l-2|l-7}}',r'\unsure{l-2|l-7}',r'\unsure{l-2|l-7}'],
 'Both horizontal crossing runs meet the reference cluster; its low digit favors2 but remains partly buried. Root favors cancellation yet cannot rule out a reference at the end of the cancellation, retaining both digit and state alternatives. The following filtering is clearly live.',ap(8),'low','deletion state (struck given live or live given struck)')
pick('A','315-sentence-overlap',[a('315-sentence-overlap')['reading'],b('315-sentence-overwrite')['reading'],c('06-315-sentence-overwrite')['reading']],
 'The dark old and new middle occupy one place between shared Sent and ce. Root overlays live en on the uncertain old ann/en; neither shared flank is duplicated.',ap(9),'medium')
pick('A','315-old-to',[r'\deleted{to}']*3,'A t stem and cross-stroke followed by a closed right loop survive the diagonal cancellation. Root resolves to without using the following in order to as authority.',ap(10),'medium')
pick('A','315-respect-mark',[a('315-respect-mark')['reading'],'respect.','respect.'],
 'A separate small crooked dark stroke lies below the early letters of respect. Root draws it without assigning a punctuation function; the distinct final period and lowercase concerning are retained.',ap(11),'high')
pick('A','315-certainly-raised',[a('315-certainly-raised')['reading'],b('315-certainly-height')['reading'],c('08-315-certainly-raised')['reading']],
 'Certainly is interlinear above the gap before true, within the abandoned parenthetical attempt. Root preserves its height and overlap.',ap(12),'high')
pick('A','315-as-far-raised',[a('315-as-far-raised')['reading'],b('315-presumably-and-raised-replacement')['reading'],c('09-315-asfar-raised')['reading']],
 'As far as our stands above the presumed presumably, overlapping it horizontally. Root retains the underlying word’s doubt against B’s resolution because the internal joins remain crossed, while preserving the certain interlinear placement.',ap(12),'high')
pick('A','315-no-terminal-marks',[a('315-no-terminal-marks')['reading'],b('315-no-tail')['reading'],c('10-315-cancelled-terminal-strokes')['reading']],
 'Two low short horizontals follow the doubtful No/Now; a longer upper stroke belongs to the cancellation and is not a third dash. The distinct low point beneath N is drawn. Root represents the two lower marks as separate short dashes, against B’s three-dot encoding; terminal point state is decided separately.',ap(13),'medium')
add('315-terminal-point-state','315, after the two low dashes in the abandoned attempt',r'\deleted{\unsure{No|Now}---.}',r'\deleted{\unsure{No|Now}- -}.',
 ['terminal point cancelled','terminal point cancelled','terminal point cancelled'],
 'The final low point stands beyond the rightmost end of the long crossing and its descending return. Root leaves that point live; this is distinct from punctuation lying beneath an ongoing cancellation.',ap(13),'high','deletion state (struck given live or live given struck)')
pick('A','315-before-close-marks',[a('315-before-close-marks')['reading'],"knowledge goes)''...","knowledge goes)''..."],
 'A small low point and a separate short oblique stroke lie between goes and the tall live closing curve. Root retains their geometry independently of the following quote pair and three low continuation marks.',ap(14),'medium')
add('315-its-high-mark','315 l.17, above the dotted i of its','its',itsmark,['its','its','its'],
 'B16 shows a small curved dark mark above-left of the ordinary lower i dot. Root preserves that distinct upper mark once, with the ordinary dot unchanged; no apostrophe function is assigned.',bp(16),'medium','drawing or diagram')
pick('A','315-would-raised',[a('315-would-raised')['reading'],b('315-would-height-caret')['reading'],c('11-315-would-raised')['reading']],
 'Would is above the which/allow gap, with a small two-legged caret below the baseline. Root preserves both height and caret, without expanding the words.',ap(15),'high')
pick('A','315-316-short-mark',[a('315-316-short-mark')['reading'],'omitted','omitted'],
 'A tiny isolated oblique dark mark occurs in the blank near the break in the left rule. Root reproduces its short contour without reading a letter or reference.',ap(28),'medium')
pick('A','316-old-it',[r'\deleted{it}']*3,'Separate i point and short stem, followed by taller t with cross-stroke and foot, remain under the oblique cancellation. Root resolves it at medium confidence.',ap(16),'medium')
pick('B','317-opening-quotes',["317. l.11 'its''",b('317-opening-quotes')['reading'],"317. l.11 'its''"],
 'The opener contains one long curved stroke and a separate short mark to its right, distinct from the lower i dot. Root follows B on a double opener.',bp(19),'medium')
add('317-isnt-retain','317 l-16, opener before isnt',"``isn't''","``isn't''",["``isn't''","``isn't''",r"\unsure{``|'}isn't''"],
 'The existing C crop separates a left high curved stroke from a small hooked second member, with white space between them. Root retains the double opener as witness C and A/B, rejecting a new doubt at this occurrence.',cp('14_317_opener'),'medium','other',False)
add('326-old-sign','326, crossed sign before live ampersand',r'\deleted{\unsure{\&}}',r'\deleted{\unsure{\&|l}}',
 [r'\deleted{\&}',b('326-old-sign')['reading'],r'\deleted{\&}'],
 'The high loop and lower crossed return favor ampersand but do not securely exclude a looped l with its cancellation. Root follows B’s explicit alternatives against A/C resolution; the new lower-right ampersand is independent.',ap(19),'low','misread symbol or index')
add('326-low-point','326, below the crossed old sign','',r'\tikz[baseline=0pt,x=1ex,y=1ex]{\fill (.1,-.32) circle (.035);}',
 [a('326-old-ampersand')['reading'],b('326-low-point')['reading'],'omitted'],
 'A separate low compact point lies below/right of the old sign. Its placement is retained without assigning a word or punctuation role.',ap(19),'medium','drawing or diagram')
add('326-raised-pointer','326, raised reference and descending pointer',a('326-raised-addition-pointer')['c'],connector,
 [a('326-raised-addition-pointer')['reading'],connector,c('15-326-raised-reference')['reading']+' '+c('16-326-connector')['reading']],
 'The added & l-3 is above commutes, with a small high point after3. The long downward stroke ends above the next formula beside a separate small bent tick. Root uses B’s local two-part drawing rather than A’s joined return or C’s formula-anchored layout; it does not attach to a triangular glyph.',ap(20),'high','insertion or placement')
add('327-old-quote-count','327 l-14, crossed quotation after isnt',r"\deleted{\unsure{''}}",r"\deleted{\unsure{''|'}}",
 [r"\deleted{''}",r"\deleted{\unsure{''}}",r"\deleted{''}"],
 'The high group is certainly crossed, but the dense body and interior hole do not settle its original count. Root keeps double/single alternatives, against A/C certainty; the following there! and its final pair are live.',ap(22),'low','misread symbol or index')
pick('B','328-apostrophe',[r"\deleted{wouldn't}",b('328-apostrophe')['reading'],r"\deleted{wouldn't}"],
 'The independent high apostrophe lies after the tall d and before the lower n, with t farther right. Root follows B and preserves would\'nt in this cancelled occurrence. The two live contractions later in the line retain their separately read spellings.',[ap(23),bp(24)],'medium')
add('329-dont-opener','329 l12, opener before dont',"``don't''",r"\unsure{``|'}don't''",["``don't''"]*3,
 'The existing C crop shows a compact upright with attached branches rather than two securely separate bodies. Root retains double/single uncertainty for this occurrence; the internal apostrophe and closing pair remain clear.',cp('18_329_dont_opener'),'low','misread symbol or index')
add('329-semi-opener','329 second l.-13, opener before semisimplicial','``semisimplicial',r"\unsure{``|'}semisimplicial",
 ['``semisimplicial','``semisimplicial',r"\unsure{``|'}semisimplicial"],
 'The high opener has one continuous bent apex with two lower arms. Root retains C reader’s double/single uncertainty, independently of the nearby dont opener.',ap(27),'low','misread symbol or index')
add('329-semi-final','329, low terminal mark after semisimplicial','semisimplicial.',r'semisimplicial\unsure{,|.}',
 ['semisimplicial.','semisimplicial.',r'semisimplicial\unsure{,|.}'],
 'The low mark has a curved short downward body, favoring comma, but the tiny return can also be a hooked period. Root retains C reader’s local comma/period alternatives. No closing quote is supplied.',bp(25),'low','other')
pick('A','329-enveloping',['enveloping']*3,'The initial low e loop is followed by n-v-e, before the clear l-o-p-i-n-g. No initial d ascender occurs. Root confirms enveloping, independently of the earlier developing at320.',[ap(25),cp('20_329_added_word')],'high')
pick('A','329-raised-entry',[a('329-raised-entry')['reading'],b('329-raised-entry')['reading'],c('19-329-added-enveloping')['reading']],
 'The complete l-5 entry is raised above/right of semisimplicial beside the long angled connector. Root preserves its height; the word, low point and clipped closer are separately accounted for.',ap(25),'high')
add('329-clipped-count','329, clipped closer after enveloping',r"\unsure{''}",r"\unsure{'|''}",
 [r"\unsure{''|'}",r"\unsure{''|'}",r"\unsure{'|''}"],
 'Only one high oblique remnant is visible against the cut edge. Root puts the visible single first, with an incompletely preserved double as alternative; no absent second stroke is supplied as certain.',cp('20_329_added_word'),'low','misread symbol or index')
add('329-low-ref-point','329 raised entry, after l-5','l-5','l-5'+low5,['l-5','l-5','l-5.'],
 'A separate low dark point lies after5, below the two high opening strokes and before the first e. Root draws the point at that height without fixing its punctuation function; it is not one of the two higher isolated points.',cp('20_329_added_word'),'medium','drawing or diagram')
add('329-high-points','329, above-left of raised entry','',upperpoints,['omitted',upperpoints,c('21-329-high-points')['reading']],
 'Two distinct small dark points stand above-left of l-5, one higher and slightly to the right. Root preserves them once with no assigned function.',cp('20_329_added_word'),'high','drawing or diagram')
pick('A','329-certa',['certa',r'\unsure{certa|certain}',r'\unsure{certa|certain}'],
 'The visible letters end with certa at the cut edge. Root follows A in printing that readable fragment; possible continuation beyond the image is documented as loss, not included as an alternative reading of visible ink.',[ap(25),cp('21_329_margin_note')],'medium')
pick('A','329-final-p',['p',r'\unsure{p|r}',r'\unsure{p|r}'],
 'The surviving stem extends below the baseline of 1 or2 and begins an upper right bowl. Root follows A on p at medium confidence; no continuation of the clipped word or closing delimiter is reconstructed.',cp('21_329_margin_note'),'medium')
pick('A','329-margin-layout',[a('329-margin-layout')['reading'],b('329-note-layout')['reading'],c('20-329-margin-layout')['reading']],
 'The question mark stands above two slanted lines on the physical right. A large low curve begins beside the writing and returns beneath the second line; root preserves that geometry and the two visible text lines, without a supplied closing curve.',[ap(25),cp('21_329_margin_note')],'high')
add('329-low-margin-point','Below/right of clipped marginal note','',lowmargin,['omitted',b('329-note-layout')['reading'],c('22-329-low-point')['reading']],
 'The separate dark point below-right of the writing is retained once. The nearby faint circular material feature, identified as a hole by all three whole-sheet readers, is not read as manuscript ink or a missing delimiter.',cp('21_329_margin_note'),'high','drawing or diagram')
for i,num,key in [('left-vertical-rule',1,'rule-left'),('right-vertical-rule',2,'rule-right')]:
 pick('A',i,[a(i)['reading'],b(key)['reading'],c('23-left-rule' if num==1 else '24-right-rule')['reading']],
 'The root narrow full-extent crop confirms the rule and both endpoints. '+('A short pale/broken interval occurs just above316, followed by a long resumed lower segment; A’s two-segment drawing is retained. ' if num==1 else 'The nearly continuous slightly irregular right rule passes beside and through long entries. ')+'It remains anchored to the text, not moved into a detached panel.',f'crops/027/0{num}_'+('left' if num==1 else 'right')+'_rule.jpg','high')
# Every explicit old doubt is accounted for; contextual confirmations remain distinct from changes.
cd=doubt_decisions(R['A'],27,'A')
cd[8].update(reading=raised313,resolved=False,evidence='Root A08: raised letter group has uncertain identity and deletion state; lower continuation meets the crossing but upper bodies are clear.')
cd[9].update(reading=ref313,resolved=False,evidence='Root A08: two crossing runs meet the reference, but state and final digit remain uncertain; cancelled l-2 favored.')
cd[16].update(reading=r'\unsure{\&|l}',resolved=False,confidence='low',evidence='Root A19: surviving upper loop and crossed lower return do not exclude a looped l.')
cd[17].update(reading=r"\unsure{''|'}",resolved=False,confidence='low',evidence='Root A22: the dense crossed high group does not settle original quote count.')
cd[18].update(reading=r"\unsure{'|''}",resolved=False,evidence='Root C20: one high remnant visible at the cut edge; a lost second component remains possible.')
for i in [5,6,11,14]:cd[i]['confidence']='medium'
for x in cd:x['decision']=('Resolved/confirmed: ' if x.get('resolved') else 'Retained/revised: ')+x['reading']
doubts=copy.deepcopy(R['A']['remaining_doubts'])
doubts[6].update(reading=raised313,alternatives='out, at, on, or; each may be cancelled or live',reason='Upper bodies are raised above the crossing, while their continuation meets it; both letters and state remain uncertain.')
doubts[7].update(reading=ref313,alternatives='l-2 or l-7, cancelled or live',reason='Both crossing runs meet the narrow reference; lower digit favors2, but upper path and state are not decisive.')
doubts[12].update(reading=r"\unsure{'|''}",alternatives='single closer; double closer with one component lost')
def doubt(place,reading,alts,reason):doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=reason))
doubt('304, final closer after s',r"\unsure{\deleted{''}|''}",'cancelled or live pair','The high pair is clear of direct contact but the cancellation continues below and beyond it.')
doubt('326, old crossed sign',r'\deleted{\unsure{\&|l}}','ampersand or looped l','Dense lower crossing leaves both shapes possible.')
doubt('327 l-14, old quote group',r"\deleted{\unsure{''|'}}",'double or single closer','A dense crossed body does not settle original count.')
doubt('329 l12, opener before dont',r"\unsure{``|'}",'double or single opener','One compact upright has attached branches; stroke count remains uncertain.')
doubt('329 l.-13, opener before semisimplicial',r"\unsure{``|'}",'double or single opener','Joined apex and two arms do not securely decide one returned stroke versus a joined pair.')
doubt('329, final low mark after semisimplicial',r'\unsure{,|.}','comma or period','Short curved downward body favors comma but can be a hooked period.')
# Exact final fragment for the placement row, after independent word/point/quote decisions.
for d in D:
 if d['id']=='027-329-raised-entry':d['final']=r'\raisebox{1.9ex}[0pt][0pt]{\inserted{l-5'+low5+r" ``enveloping\unsure{'|''}}}"
inv=copy.deepcopy(R['A']['inventory'])
for x in inv:
 for old,new in replacements:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
inv[28]['first_words_or_objects']=r"l12 \unsure{``|'}don't''; l-13 makes sense; l.-13 \unsure{``|'}semisimplicial\unsure{,|.}"
inv[32]['first_words_or_objects']=r"Cancelled l-2 play no/not s; final pair \unsure{\deleted{''}|''}"
inv[35]['first_words_or_objects']='filtering cancelled; raised out/at/on/or and l-2/l-7 separately uncertain in identity and state'
inv[38]['first_words_or_objects']='Cancelled first parenthetical attempt and No/Now with two low dashes; final point live'
inv[41]['first_words_or_objects']=r'\deleted{\unsure{\&|l}}'
inv[42]['first_words_or_objects']=r"\deleted{\unsure{''|'}}"
inv[43]['first_words_or_objects']="would'nt"
inv[44]['first_words_or_objects']='raised out/at/on/or; cancellation state uncertain'
inv[50]['first_words_or_objects']=r"l-5, low point, enveloping with \unsure{'|''} at clipped edge"
inv[66]['first_words_or_objects']='descending oblique stroke and separate small bent tick; no contact with formula'
extra=[('drawing','315 l.17 above dotted i','Separate small curved upper mark, in addition to ordinary i dot',1220),('deletion','315, lower word beneath as far as our','presumably, uncertain, within the abandoned parenthesis',1055),('drawing','329, after raised l-5','Low separate point before opener of enveloping',2090),('drawing','329, above-left of raised entry','Two separate high points',2035),('drawing','329, below/right of marginal note','Isolated dark point, separate from material circular feature',2260)]
extra_y={}
for k,p,w,y in extra:
 inv.append(dict(sheet_kind='list',hand='hand or material origin not established' if k=='drawing' else inv[0]['hand'],element='added',kind=k,position=p,first_words_or_objects=w,transcribed='yes'));extra_y[len(inv)-1]=y
ys={0:90,1:90,2:105,3:175,4:300,5:365,6:415,7:480,8:545,9:605,10:680,11:735,12:790,13:900,14:1165,15:1235,16:1355,17:1430,18:1500,19:1560,20:1620,21:1690,22:1760,23:1820,24:1880,25:1950,26:2010,27:2070,28:2135,29:2210,30:2275,31:165,32:305,33:415,34:545,35:680,36:790,37:850,38:1070,39:1355,40:1355,41:1690,42:1820,43:1950,44:655,45:790,46:1030,47:1030,48:1205,49:1645,50:2080,51:430,52:480,53:870,54:920,55:980,56:1040,57:1040,58:1690,59:1820,60:960,61:1130,62:1180,63:1270,64:1315,65:1710,66:1725,67:1635,68:1760,69:1760,70:2070,71:2145,72:2200,73:2180,74:2350}
ys.update(extra_y)
inv=[x for i,x in sorted(enumerate(inv),key=lambda z:(ys[z[0]],z[0]))]
for i,x in enumerate(inv,1):x['element']=f'{i:02}'
notes=copy.deepcopy(R['A']['notes'][:6])
notes[4]='At328 l-12 the old cancelled form is would\'nt, with its apostrophe after d and before n. The live wording is should ``wouldn\'t\'\' = ``shouldn\'t\'\'. The physical position of the old apostrophe is preserved without correcting the spelling.'
notes.append('The exact live qualification at315 is This certainly seems to be so as far as our present knowledge goes. The abandoned attempt includes certainly, presumably (still doubtful), as far as our, and No/Now (doubtful); these are preserved with their cancellations and raised positions. The separate period after respect and lowercase concerning remain as written.')
notes.append('The two long rules, local connectors, underlines, isolated points and raised additions remain related to the main text. The fragment certa and final p at the right edge are readable; the lost continuation is not supplied. The closer after enveloping, several fused quote groups, and parts of the dense313 and315 cancellations remain doubtful. The faint circular edge features were identified as material holes by all three whole-sheet readers and are not transcribed as ink.')
notes.append('No title, date, stated total page count, or own manuscript pagination occurs. The corner26 is retained only as an archive comment. H supplies a description rather than a transcription, so this page has no H collation rows. Isolated correction targets do not supply the definitions or cited surrounding text needed to prove or refute their mathematical content; no substantive mathematical check event is claimed.')
notation=copy.deepcopy(R['A']['notation'])
notation[0]['reading']='$A$ by $A$'
notation[8].update(sign='compact quotation and terminal mark',reading=r"\unsure{``|'}semisimplicial\unsure{,|.}",evidence='Root A27/B25: joined high fork and curved low terminal mark; independent local doubts.')
notation += [dict(sign='apostrophe placement in cancelled contraction',location='328 l-12',reading=r"\deleted{would'nt}",evidence='A23/B24: independent apostrophe after d and before n; live contractions elsewhere separately read.'),dict(sign='readable clipped fragments',location='329 right margin',reading='certa; p',evidence='A25/C21: letters before physical cut; no unseen continuation supplied.'),dict(sign='quote at cut edge',location='329 after enveloping',reading=r"\unsure{'|''}",evidence='C20: one visible high remnant first; double with lost second component remains possible.'),dict(sign='overwritten shared letters',location='315 Sentence',reading=a('315-sentence-overlap')['reading'],evidence='A09: old/new middle overlaps; shared Sent and ce once.'),dict(sign='raised cluster and reference state',location='313 continuation',reading=raised313+' '+ref313,evidence='A08: raised bodies and reference meet the cancellation differently; state remains local and uncertain.'),dict(sign='short dashes versus cancellation tail',location='315 after No/Now',reading='two low short dashes and live final point',evidence='A13: upper long stroke is cancellation; final point beyond its endpoint.'),dict(sign='asymmetric quotations',location='305;313;317;320;329',reading='Single interpret closer and developing opener retained; paired shouldnt/its openers resolved; local compact groups remain doubtful.',evidence='A05/A18/B09/B19/C14/C18/A27: no pattern-based propagation.')] 
viewed=json.loads((W/'records/root_027_viewed.json').read_text())
coverage='All three final full texts, reports, inventories and frozen-crop audits were compared. All21 explicit C uncertainties and page-specific context questions have decisions. Every reader/witness disagreement was adjudicated on a retained crop, including rejected resolutions and root-only geometry/uncertainty decisions. Root reused40 distinct reader crops and made2 narrow full-extent rule crops; re-displays of existing unresolved loci and output recovery do not count as new crops. The inventory has80 elements and19 physical textual/state doubt loci remain (nested uncertainty macros do not imply additional physical loci). All three mathematical glyphs and each component of n-1 were checked independently on ink; no proof or computation was performed. H is description-only. No OCR, outside research or compilation.'
rec=write_record(27,'A','brief_v12.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan027',len(D),'decisions',sum(x['diff_c'] for x in D),'C changes',len(doubts),'doubt loci',len(inv),'inventory',rec['crop_counts'])
