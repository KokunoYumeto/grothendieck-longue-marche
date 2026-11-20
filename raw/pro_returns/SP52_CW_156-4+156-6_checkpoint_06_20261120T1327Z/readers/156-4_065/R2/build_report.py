from pathlib import Path
from datetime import datetime, timezone
import json

out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R2')
source=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
whole=str(source/'J156-4-08_156-4_scan065.jpg')
a=str(source/'J156-4-08_156-4_scan065_a.jpg')
b=str(source/'J156-4-08_156-4_scan065_b.jpg')
crops=json.loads((out/'crop_manifest.json').read_text())

reading=r'''\scanpage{65}\mspage{64}
Inversement, donnons nous, \deleted{$\unsure{F_i\in|F_i}$} $\unsure{(}\forall i\in I)$ un $F_i\in\mathcal F_i$, quand peut-on dire qu'il existe $F\in\mathcal F$ telle que $\forall i$, $F_i$ soit la $i$ composante de $\deleted{\unsure{\mathcal F}}\unsure{F_0|F}$ ?

Déjà, il le faudrait pour \unsure{le|les} cas où tous les $F_i$ sauf un nb fini sont \deleted{$\varnothing$} vides. On va supposer donc

\uline{$C4$} Si $x,y\in M$ appartiennent à des \unsure{comp|comp.} connexes disjointes de $M$, alors $x$ et $y$ sont compatibles.

\deleted{Cor} \inserted{C'est néc et suffisant pour la \unsure{validité} des}
% The beginning of validité is crowded/retraced; no separate deleted word is securely separable.

\uline{Corollaire 1} L'image de $\mathcal F\to\prod\mathcal F_i$ contient les $(F_i)_{i\in I}$ tels que $F_i=\varnothing$ \deleted{sauf} pour \deleted{\unsure{pres}} que tout $i$.

\inserted{\uline{Cor. 2}} \deleted{donc} $\mathcal F\to\prod\mathcal F_i$ est une bijection dans \unsure{le|les} \deleted{deux} cas où \deleted{suivants} \inserted{$I$ est} \deleted{\unsure{f}} fini.
% Cor. 2 is interlined at the right, underlined and bounded by an angular insertion connector to the next sentence.
% The article after dans is a single retraced cluster; an earlier les is not separately secure.

\deleted{a) $I$ est fini}

\deleted{b) Toute figure est de t.f. -- alors}

\uline{Cor 3} Supposons que les figures \deleted{\unsure{de|des}} $\in\mathcal F$ soient de t.f. \deleted{Alors il} \inserted{(resp. finies)}. Alors il en est de $=$ \deleted{de} pour $\mathcal F_i$, de plus $\mathcal F\text{---}\prod\mathcal F_i$ a comme image l'ens des $(F_i)$ tels que $F_i$ soit $\varnothing$ pour pres que tout $i$.
'''
(out/'reading.tex').write_text(reading,encoding='utf-8')

D=[]
def diff(location,c,h,r,shows,kind='other',confidence='high',marked='no',cc=False,ch=True,crop=None,bbox=None,img=None,math=False):
    if crop is not None:
        cr=crops[crop-1]
        crop_path=cr['path']; bbox=cr['bbox']; img=cr['source']
    else: crop_path=None
    D.append(dict(id=f'R2-D{len(D)+1:03d}',location=location,c=c,h=h,reading=r,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=crop_path,bbox=bbox,bbox_image=img,math_consequential=math))

diff('Opening, donnons nous',r'donnons nous',r'donnons-nous',r'donnons nous','First half: a clear gap separates the two words; no joining hyphen is drawn.','abbreviation expanded or spelling modernised',bbox=[775,145,1250,220],img=a)
diff('Opening, cancelled F_i and membership',r'\deleted{$\unsure{F_i\in|F_i}$}',r'\struck{$F_i \in$}',r'\deleted{$\unsure{F_i\in|F_i}$}','The indexed F is cancelled. The following C-shaped trace meets the cancellation; its status as a membership sign rather than part of a new opening parenthesis remains uncertain.','misread symbol or index','low',crop=1,math=True)
diff('Opening, parenthesis and separator around universal quantifier',r'$\unsure{(}\forall i\in I)$',r'$\forall i \in I$,',r'$\unsure{(}\forall i\in I)$','The closing curved parenthesis after I is clear. No comma occupies its place. An independent opening parenthesis cannot be separated from the preceding crossed trace.','omission','medium',crop=1,math=True)
diff('Opening, first family alphabet',r'F_i\in\mathcal F_i',r'F_i\in\mathfrak{F}_i',r'F_i\in\mathcal F_i','First half: the individual F has a straight top and the family F has a broad bent upper arm and curved stem. The family is calligraphic, not Gothic.','misread symbol or index',bbox=[480,235,701,315],img=a,math=True)
diff('Opening question, wording after first family',r'quand peut-on dire',r'pouvons-nous \uncertain{affirmer}',r'quand peut-on dire','First half: the initial q descends, the next word has the strokes of peut followed by the hyphen and on, and the final word begins with the looped d of dire.','misread word',marked='yes',bbox=[780,245,1505,335],img=a)
diff('Opening, existential family alphabet',r'F\in\mathcal F',r'F\in\mathfrak{F}',r'F\in\mathcal F','The first half and context line in crop 02 distinguish a straight individual F from the bent upper arm of the family letter.','misread symbol or index',crop=2,math=True)
diff('Opening, i composante',r'la $i$ composante',r'la $i$-composante',r'la $i$ composante','First half: the isolated i is followed by open space before composante, with no hyphen.','abbreviation expanded or spelling modernised',bbox=[294,446,830,516],img=a)
diff('Opening, terminal overwritten F and low mark',r'$\deleted{\unsure{\mathcal F}}\unsure{F_0|F}$',r'$F$',r'$\deleted{\unsure{\mathcal F}}\unsure{F_0|F}$','Parallel middle arms and a residual bent upper-left stroke indicate retracing/overwriting. A small loop with a tail sits low to the right; it may be a subscript 0, but a nonindex mark cannot be excluded. H suppresses both difficulties.','misread symbol or index','low',crop=2,math=True)
diff('Déjà paragraph, verb after il le',r'il le faudrait',r'il le faut \uncertain{sûrement}',r'il le faudrait','First half: the long descending f is followed by the joined faudrait strokes; there is no separate sûrement group.','misread word',marked='yes',bbox=[610,515,1145,650],img=a)
diff('Déjà paragraph, pour le(s) cas où',r'pour \unsure{le|les} cas où',r'pour \struck{\ill{}} \ill{}',r'pour \unsure{le|les} cas où','The article is retraced, allowing le or les; cas is separate and où begins the next line. No separately cancelled group occurs here.','readable ink left as \\ill{}','medium',marked='yes',crop=3)
diff('Déjà paragraph, sont',r'sont',r'soient',r'sont','First half: the word ends the second line; its visible strokes give sont, with no separate i or i-dot.','misread word',bbox=[1513,620,1635,702],img=a)
diff('Déjà paragraph, final phrase',r'On va supposer donc',r'Donc on supposera donc',r'On va supposer donc','First half: capital On is followed by the separate va and supposer; no initial Donc or final a on supposer appears.','misread word',bbox=[586,708,1320,789],img=a)
diff('C4, variables and ambient set alphabet',r'x,y\in M;\ M;\ x\text{ et }y',r'X,Y\in\mathcal M;\ \mathcal M;\ X\text{ et }Y',r'x,y\in M;\ M;\ x\text{ et }y','First half: the crosses and y forms have the size and ductus of lower-case variables. M is a single cursive capital, not a separately stylized calligraphic alphabet. The same forms recur in the final sentence.','misread symbol or index',bbox=[288,845,1569,1142],img=a,math=True)
diff('C4, word after appartiennent à',r'\unsure{des|deux}',r'deux',r'des','The word has a d loop, an e turn and an un-crossed terminal downstroke. The cancelled deux on this same page has a separate crossed x; no such x appears here.','misread word','medium',cc=True,crop=4,math=True)
diff('C4, comp abbreviation punctuation',r'comp.',r'comp.',r'\unsure{comp|comp.}','The terminal small loop is attached to the p-like down-and-up stroke. A detached abbreviation point is not visible; the attached loop could nevertheless include a point.','other','medium',cc=True,crop=5)
diff('Interlinear note, néc abbreviation',r'\unsure{néc|néc.}',r'nécessaire',r'néc','The short word has three letter groups and an accent-like mark above the middle. Its final c is followed by space, not a point.','abbreviation expanded or spelling modernised',cc=True,crop=6)
diff('Interlinear note, crowded validité and alleged cancelled prefix',r'\deleted{\unsure{déd|val}} \unsure{validité|déduction}',r'\ill{}',r'\unsure{validité}','The crowded lower line contains a looped first group followed by i/d/i/t/é-like strokes and then des. I see one word, best read validité; I cannot separate a cancelled word and a second complete live validité. The low horizontal stroke can be a joining/retracing stroke.','deletion state (struck given live or live given struck)','low',marked='yes',cc=True,crop=6)
diff('Interlinear note, after des',r'des',r'des \ill{}',r'des','The short note ends with des. There is no further word or cancellation to its right.','text not on the page',marked='yes',crop=6)
diff('Interlinear note, insertion state relative to cancelled Cor',r'\deleted{Cor} \inserted{C\text{’}est \ldots des}',r'C\text{’}est \ldots des \ill{}\par\struck{Cor}',r'\deleted{Cor} \inserted{C\text{’}est néc et suffisant pour la \unsure{validité} des}','The cancelled Cor is at the left below the new two-line note; the note is interlined between C4 and Corollaire 1. The reading records it as inserted wording replacing the abandoned Cor lead-in.','insertion or placement',bbox=[295,1110,1475,1255],img=a)
diff('Corollaire 1, family alphabets in map',r'\mathcal F\to\prod\mathcal F_i',r'\mathfrak F\to\prod\mathfrak F_i',r'\mathcal F\to\prod\mathcal F_i','Second half: both family letters have the same bent/looped upper arm seen in the opening, with i at the product family. The arrow has a visible right head.','misread symbol or index',bbox=[1070,145,1380,235],img=b,math=True)
diff('Corollaire 1, sauf deletion state',r'\deleted{sauf}',r'sauf',r'\deleted{sauf}','Second half: a dark horizontal stroke traverses sauf, including its initial and terminal portions. It is cancelled, not live.','deletion state (struck given live or live given struck)',bbox=[1498,248,1633,317],img=b,math=True)
diff('Corollaire 1, cancelled group before que',r'\deleted{\unsure{pres}}que',r'\struck{\ill{}}',r'\deleted{\unsure{pres}} que','A crossed p-like descent and small following groups occupy the position before a separate clear que. Pres remains a best but uncertain reading. A visible gap precedes que, retained in the transcription.','readable ink left as \\ill{}','low',marked='yes',cc=True,crop=8)
diff('Corollaire 1, ending after cancelled pres',r'que tout $i$.',r'un nb fini d\text{’}$i$.',r'que tout $i$.','The q has a deep descending loop, followed by ue, then the separated strokes of tout and i with a final point. Neither nb nor fini nor d’ is written here.','misread word',crop=8,math=True)
diff('Corollaire 2, heading insertion and connector',r'\inserted{\uline{Cor. 2}}',r'\emph{Cor. 2}',r'\inserted{\uline{Cor. 2}}','Cor. 2 is interlined on the right, above the cancelled donc, with its own underline and an angular border/connector leading down-left to the sentence. H notes the frame editorially but does not mark the heading as inserted.','insertion or placement',crop=9)
diff('Corollaire 2, cancelled donc case and reading',r'\deleted{\unsure{donc}}',r'\struck{Donc}',r'\deleted{donc}','The old word below the label starts with a looped lower-case d ascender. The following o/n/c trace is crossed.','misread word','medium',cc=True,crop=9)
diff('Corollaire 2, family alphabets in map',r'\mathcal F\to\prod\mathcal F_i',r'\mathfrak F\to\prod\mathfrak F_i',r'\mathcal F\to\prod\mathcal F_i','The two bent-upper-arm family forms are visible in the right-hand map, along with a right-headed arrow.','misread symbol or index',crop=9,math=True)
diff('Corollaire 2, article after dans and correction state',r'\deleted{les} le',r'les',r'\unsure{le|les}','A single short retraced group follows dans. Its loop and dark terminal stroke allow le or les; I cannot securely distinguish a separately legible deleted les and live le.','deletion state (struck given live or live given struck)','low',cc=True,crop=9)
diff('Corollaire 2, I est insertion',r'\inserted{$I$ est}',r'$I$ est',r'\inserted{$I$ est}','I est is written above the crossed suivants, at the beginning of the next physical line.','insertion or placement',crop=9,math=True)
diff('Corollaire 2, cancelled initial before fini',r'\deleted{\unsure{f}}',r'',r'\deleted{\unsure{f}}','A short crossed stem with rightward bars lies between the abandoned suivants line and the taller live f of fini. It is plausibly an abandoned f; the heavy crossing prevents certainty.','omission','low',crop=9)
diff('Corollaire 2, placement of cancelled suivants',r'\deleted{suivants} \inserted{$I$ est} \deleted{\unsure{f}} fini.',r'$I$ est fini \struck{suivants :}',r'\deleted{suivants} \inserted{$I$ est} \deleted{\unsure{f}} fini.','The cancelled suivants is under the inserted I est and precedes the live fini in the correction sequence. It does not follow the completed I est fini as H’s running text suggests.','insertion or placement',crop=9)
diff('Corollaire 2, colon after cancelled suivants',r'\deleted{suivants}',r'\struck{suivants :}',r'\deleted{suivants}','No two-dot colon follows the cancelled word. The nearby strokes belong to the abandoned initial before fini.','text not on the page',crop=9)
diff('Corollaire 2, full stop after live fini',r'fini.',r'fini',r'fini.','A small full stop lies to the right of the live fini at the end of its line.','omission',crop=9)
diff('Cancelled case a, introduced semicolon in H',r'\deleted{a) $I$ est fini}',r'\struck{a) $I$ est fini ;}',r'\deleted{a) $I$ est fini}','The cancelled a line ends after fini; no semicolon is drawn before the separate b line.','text not on the page',crop=10)
diff('Cancelled case b, Toute capitalization',r'\deleted{b) Toute figure est de t.f. \unsure{--} alors}',r'\struck{b) toute figure est de t.f. \ill{} alors}',r'\deleted{b) Toute figure est de t.f. -- alors}','The initial T of Toute has a distinct broad top and stem. It is a capital, even though the word is crossed.','abbreviation expanded or spelling modernised',crop=10)
diff('Cancelled case b, dash before alors',r'\unsure{--}',r'\ill{}',r'--','A short horizontal bar below the long cancellation line lies between t.f. and alors. Its endpoints are independent of the cancellation.','readable ink left as \\ill{}',marked='yes',cc=True,crop=10)
diff('Corollaire 3, cancelled group after figures',r'\deleted{\unsure{de}}',r'\struck{\ill{}}',r'\deleted{\unsure{de|des}}','The first loop and small ascender support d, followed by a heavily crossed e-like tail. The far-right downturn may belong to s or to the cancellation, so de/des remains open.','readable ink left as \\ill{}','low',marked='yes',cc=True,crop=11)
diff('Corollaire 3, family after membership',r'\in\mathcal F',r'\in\mathfrak F',r'\in\mathcal F','The family has a looped upper arm and curved stem; the membership sign has its separate interior bar.','misread symbol or index',crop=13,math=True)
diff('Corollaire 3, resp. finies insertion and order',r'\deleted{Alors il} \inserted{(resp. finies)}',r'(resp. finies) \struck{\ill{}}',r'\deleted{Alors il} \inserted{(resp. finies)}','The parenthesis is interlined immediately above the crossed Alors il. It is an addition at that position, not ordinary baseline text preceding an unidentified later deletion.','insertion or placement',marked='yes',crop=12)
diff('Corollaire 3, readable cancelled Alors il',r'\deleted{Alors il}',r'\struck{\ill{}}',r'\deleted{Alors il}','The crossed baseline text has the capital A, joined lors, then a dotted i and tall l; the cancellation does not erase their identities.','readable ink left as \\ill{}',marked='yes',crop=12)
diff('Corollaire 3, sign after en est de',r'$\unsure{=|\text{même}}$',r'même',r'$=$','Two separate horizontal strokes are drawn, the lower with a small left hook. No letters spelling même occur. The equality-shaped repetition abbreviation is preserved literally.','abbreviation expanded or spelling modernised',cc=True,crop=13)
diff('Corollaire 3, deleted de after repetition sign',r'\deleted{\unsure{de}}',r'',r'\deleted{de}','The small cancelled cluster has a visible d loop/ascender followed by an e loop at the right. It precedes pour.','omission','medium',cc=True,crop=13)
diff('Corollaire 3, family after pour',r'\mathcal F_i',r'\mathfrak F_i',r'\mathcal F_i','Second half: the upper arm bends to the left and the stem curves; the small right-hand i is dotted and descends only to index height.','misread symbol or index',bbox=[1105,915,1210,1002],img=b,math=True)
diff('Corollaire 3, final map alphabets and separator',r'\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i',r'\mathfrak F\to\prod\mathfrak F_i',r'\mathcal F\text{---}\prod\mathcal F_i','The family letters have looped upper arms. Between the first family and product is a horizontal stroke with one short downward terminal turn, not a visible two-armed arrowhead. The two earlier maps have unmistakable heads; none is supplied here.','misread symbol or index','high',cc=True,crop=14,math=True)
diff('Corollaire 3, ens abbreviation punctuation',r"l'ens",r"l'ens.",r"l'ens",'The s-shaped terminal tail is followed by a gap and des. No abbreviation point intervenes.','abbreviation expanded or spelling modernised',crop=15)
diff('Corollaire 3, pres que spacing',r'pres que',r'presque',r'pres que','A word-sized gap separates the pres group from the descending q. No accent is visible over pres.','abbreviation expanded or spelling modernised',crop=15)

CD=[]
def cd(location,c,r,status,shows,crop=None,bbox=None,img=None):
 if crop:
  cr=crops[crop-1]; cp=cr['path']; bbox=cr['bbox']; img=cr['source']
 else: cp=None
 CD.append(dict(location=location,c=c,reading=r,status=status,scan_shows=shows,crop=cp,bbox=bbox,bbox_image=img))
cd('Opening, cancelled membership',r'\unsure{F_i\in|F_i}',r'\unsure{F_i\in|F_i}','retained','The indexed F is crossed; the following C-shaped trace intersects the cancellation and possible parenthesis.',1)
cd('Opening, opening parenthesis',r'\unsure{(}',r'\unsure{(}','retained','The closing parenthesis is clear, but the opening curved trace cannot be independently separated from the old membership sign.',1)
cd('Question, underlying terminal letter',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','Bent upper-left residual stroke and parallel middle arms support an overwritten family F; mere retracing remains possible.',2)
cd('Question, low mark beside terminal F',r'\unsure{F_0|F}',r'\unsure{F_0|F}','retained','Small low loop with a tail is visible; subscript zero versus a nonindex mark is unresolved.',2)
cd('Déjà, article before cas',r'\unsure{le|les}',r'\unsure{le|les}','retained','The l loop and following strokes are retraced; the terminal group permits both endings.',3)
cd('C4, des/deux',r'\unsure{des|deux}',r'des','resolved','Terminal downstroke has no independent x crossing, unlike cancelled deux in the Cor 2 revision.',4)
cd('Interlinear note, néc punctuation',r'\unsure{néc|néc.}',r'néc','resolved','Final c is followed by space, with no detached point.',6)
cd('Interlinear note, alleged cancelled prefix',r'\deleted{\unsure{déd|val}}',r'\unsure{validité}','revised','No complete second word is separable. The crowded initial group belongs to the best reading validité; cancellation of that group is not securely established.',6)
cd('Interlinear note, validité/déduction',r'\unsure{validité|déduction}',r'\unsure{validité}','revised','The live right-hand groups fit dité and include a t-like ascender. The first group is crowded; déduction is not supported by a visible -ction ending.',6)
cd('Corollaire 1, cancelled pres',r'\deleted{\unsure{pres}}',r'\deleted{\unsure{pres}}','retained','A p-like descent and three small groups remain under crossing; the word is still partly obscured.',8)
cd('Corollaire 2, cancelled donc',r'\deleted{\unsure{donc}}',r'\deleted{donc}','resolved','Lower-case d ascender and following horizontal letter groups remain visible beneath the strike.',9)
cd('Corollaire 2, cancelled initial before fini',r'\deleted{\unsure{f}}',r'\deleted{\unsure{f}}','retained','Short stem and rightward bars are partially merged with the strike through suivants.',9)
cd('Cancelled b, dash before alors',r'\unsure{--}',r'--','resolved','A separate short horizontal bar sits below the cancellation line.',10)
cd('Corollaire 3, cancelled word after figures',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de|des}}','revised','d-like ascender and e-like tail survive; right terminal downturn can also allow s.',11)
cd('Corollaire 3, equality-shaped repetition sign',r'\unsure{=|\text{même}}',r'=','resolved','Two strokes, with no written letters, decide the literal graphic form.',13)
cd('Corollaire 3, cancelled word before pour',r'\deleted{\unsure{de}}',r'\deleted{de}','resolved','The d loop/ascender and right e loop remain distinct enough to read.',13)
cd('Corollaire 3, final separator',r'\unsure{\text{---}|\longrightarrow}',r'\text{---}','resolved','Horizontal stroke ends in a small downward turn; no actual arrowhead is visible.',14)
cd('C context, individual/family alphabet and i indices',r'F_i,\mathcal F_i,\forall i,(F_i)_{i\in I}',r'F_i,\mathcal F_i,\forall i,(F_i)_{i\in I}','resolved','Straight individual F and bent family F are distinct throughout. All relevant low indices have the i form. Quantifier has crossed V-like form.',bbox=[476,236,709,319],img=a)
cd('C context, C4 variables and M',r'x,y\in M',r'x,y\in M','resolved','Crossed x, descending y and ordinary cursive M are visible; no distinct calligraphic M construction is drawn.',bbox=[684,850,929,932],img=a)
cd('C context, empty signs and first two map arrows',r'\varnothing,\to',r'\varnothing,\to','resolved','Empty signs are slashed ovals; the first two maps each have a separate right-pointing head.',bbox=[1074,150,1634,317],img=b)
cd('C context, final pres que spacing',r'pres que|presque',r'pres que','resolved','The gap before q is at least comparable to adjacent word gaps, and pres has no accent.',15)

INV=[]
def inv(element,kind,pos,first):
 INV.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='manuscript leaf',hand='his hand',transcribed='yes'))
inv('Pagination','page number','top centre','64')
inv('Opening question','text block','upper quarter, four manuscript lines','Inversement, donnons nous')
inv('Opening cancellation','deletion','first line, right of donnons nous',r'F_i\in (uncertain extent)')
inv('Terminal overwritten symbol','deletion / overwriting','opening question, fourth line',r'\mathcal F overwritten by F with low mark')
inv('Introductory paragraph','text block','below opening question, three lines','Déjà, il le faudrait')
inv('Old empty sign','deletion','introductory paragraph, immediately before vides',r'\varnothing')
inv('C4 heading','underlined heading','left, middle upper area','C4')
inv('C4 statement','text block','three manuscript lines following heading',r'Si x,y\in M')
inv('Abandoned Cor heading','deletion','left of the interlinear note, below C4','Cor')
inv('Necessity/sufficiency note','insertion','two small lines between C4 and Corollaire 1',"C'est néc et suffisant")
inv('Crowded word in note','retraced text','second line of inserted note','validité (initial group uncertain)')
inv('Corollaire 1 heading','underlined heading','below inserted note','Corollaire 1')
inv('Corollaire 1 statement','text block','three lines around inserted Cor. 2 label',"L'image de")
inv('Corollaire 1 sauf','deletion','right end of second statement line','sauf')
inv('Corollaire 1 pres','deletion','third statement line, after pour','pres (uncertain)')
inv('Corollaire 2 heading and angular connector','insertion','interlined right of Corollaire 1 ending; connector bends down-left to sentence','Cor. 2')
inv('Corollaire 2 old lead-in','deletion','directly under inserted Cor. 2 label','donc')
inv('Corollaire 2 statement','text block','map to right of label, continues at left on next lines',r'\mathcal F\to\prod\mathcal F_i est une bijection')
inv('Corollaire 2 article correction','retraced text','after dans','le / les; earlier state unresolved')
inv('Corollaire 2 deux','deletion','after article and before cas où','deux')
inv('Corollaire 2 suivants','deletion','next line, below inserted I est','suivants')
inv('Corollaire 2 I est','insertion','above crossed suivants',r'I est')
inv('Corollaire 2 abandoned initial','deletion','before live fini','f (uncertain)')
inv('Cancelled case a','deletion / text block','first line below Corollaire 2 correction',r'a) I est fini')
inv('Cancelled case b','deletion / text block','second line below Corollaire 2 correction','b) Toute figure est de t.f. -- alors')
inv('Corollaire 3 heading','underlined heading','lower quarter, at left','Cor 3')
inv('Corollaire 3 statement','text block','last five manuscript lines','Supposons que les figures')
inv('Corollaire 3 old preposition','deletion','right end of first Cor 3 line','de / des')
inv('Corollaire 3 abandoned sentence start','deletion','after de t.f. on second Cor 3 line','Alors il')
inv('Corollaire 3 finite parenthesis','insertion','above cancelled Alors il','(resp. finies)')
inv('Corollaire 3 deleted de','deletion','third Cor 3 line, after equality-shaped repetition sign','de')

remaining=[
 dict(location='Opening, cancelled symbol',reading=r'\deleted{$\unsure{F_i\in|F_i}$}',alternatives=[r'F_i\in',r'F_i'],confidence='low',reason='Cancellation joins the possible membership trace and possible parenthesis.'),
 dict(location='Opening, left parenthesis',reading=r'\unsure{(}',alternatives=['opening parenthesis','no distinct opening parenthesis'],confidence='low',reason='Only a shared curved trace survives before the quantifier; the right parenthesis is clear.'),
 dict(location='Question, old terminal letter',reading=r'\deleted{\unsure{\mathcal F}}',alternatives=[r'overwritten \mathcal F',r'retraced plain F'],confidence='low',reason='Bent residual stroke suggests family letter but overlapping arms conceal the older construction.'),
 dict(location='Question, subscript after F',reading=r'\unsure{F_0|F}',alternatives=[r'F_0',r'F with nonindex low mark'],confidence='low',reason='Low closed loop has a tail and could be punctuation/retracing.'),
 dict(location='Déjà, article',reading=r'\unsure{le|les}',alternatives=['le','les'],confidence='medium',reason='Terminal cluster retraced; no stable final s can be isolated.'),
 dict(location='C4, comp punctuation',reading=r'\unsure{comp|comp.}',alternatives=['comp','comp.'],confidence='medium',reason='The terminal loop is attached; it may include an abbreviation point, but no detached point is visible.'),
 dict(location='Interlinear note, validité and its state',reading=r'\unsure{validité}',alternatives=['one retraced word validité','partially cancelled initial group val followed by dité'],confidence='low',reason='One word fits the surviving letter groups; the low horizontal stroke may be either joining/retracing or cancellation.'),
 dict(location='Corollaire 1, cancelled pres',reading=r'\deleted{\unsure{pres}}',alternatives=['pres','unresolved crossed group beginning with p'],confidence='low',reason='Several cancellation strokes obscure the small interior letters.'),
 dict(location='Corollaire 2, article after dans',reading=r'\unsure{le|les}',alternatives=['le','les','les overwritten as le'],confidence='low',reason='Single heavily retraced cluster does not securely distinguish old and new states.'),
 dict(location='Corollaire 2, cancelled initial before fini',reading=r'\deleted{\unsure{f}}',alternatives=['f','unresolved abandoned stem-and-bars'],confidence='low',reason='Old initial intersects crossing from suivants.'),
 dict(location='Corollaire 3, cancelled word after figures',reading=r'\deleted{\unsure{de|des}}',alternatives=['de','des'],confidence='low',reason='Right terminal downturn may be a letter s or part of the cancellation.')
]

notation=[
 dict(sign='Individual F and indexed F',latex=r'F,F_i',appearance='Straight upper arm and approximately upright main stem; small i at lower right.',location='Opening and all corollaries',alternatives=[]),
 dict(sign='Family F',latex=r'\mathcal F,\mathcal F_i',appearance='Upper arm bends or loops at left, with curved stem; no Gothic construction.',location='Opening and three corollaries',alternatives=[]),
 dict(sign='Universal quantifier',latex=r'\forall',appearance='V-like two oblique strokes crossed by a horizontal bar.',location='Opening first and third lines',alternatives=[]),
 dict(sign='Membership',latex=r'\in',appearance='Open curved form with short inner bar, sometimes compressed to an angular form.',location='Opening, C4, Cor 3',alternatives=[]),
 dict(sign='Index-set capital',latex='I',appearance='Capital stem with upper and lower crossbars; lower bar may slant.',location='Opening, Cor 1 family index, Cor 2 cases',alternatives=[]),
 dict(sign='C4 variables and ambient set',latex='x,y,M',appearance='Crossed x, forked/descending y, ordinary cursive capital M.',location='C4',alternatives=[]),
 dict(sign='Empty set',latex=r'\varnothing',appearance='Small oval crossed by a slanted long stroke.',location='Introductory cancellation, Cor 1 and final Cor 3 clause',alternatives=[r'\emptyset is treated as an equivalent encoding of this handwritten sign']),
 dict(sign='Two headed maps',latex=r'\to',appearance='Horizontal shaft with an unambiguous right-pointing head.',location='Cor 1 and Cor 2',alternatives=[]),
 dict(sign='Repetition abbreviation',latex='=',appearance='Two separated horizontal strokes; lower has a curled left start.',location='Cor 3, en est de =',alternatives=['Semantic expansion même is not transcribed']),
 dict(sign='Final map separator',latex=r'\text{---}',appearance='Horizontal stroke with short downward terminal turn, no visible arrowhead.',location='Cor 3 final map',alternatives=[])
]
abbreviations=[
 dict(form='nb',expansion='nombre'),dict(form='comp',expansion='composantes'),dict(form='néc',expansion='nécessaire'),dict(form='Cor',expansion='Corollaire'),dict(form='Cor.',expansion='Corollaire'),dict(form='t.f.',expansion='type fini'),dict(form='resp.',expansion='respectivement'),dict(form='ens',expansion='ensemble'),dict(form='=',expansion='même (repetition abbreviation, preserved as a sign)')
]
notes=dict(
 summary='Manuscript page 64 asks when prescribed component figures come from one figure, adds condition C4, and records three corollaries with substantial cancellations and interlinear revisions. There are no mathematical diagrams, standalone drawings, detached margin notes, typed additions, title, date, or archive number visible on this sheet. The angular line around Cor. 2 is an insertion connector, represented by the insertion macro and documented in the inventory rather than treated as an independent figure.',
 math_reading_decisions='No mathematical proposition was proved or tested. The analogous form of the three family maps prompted scrutiny of the final separator, but its visible one-stroke form was transcribed as a dash; no arrowhead was supplied from mathematical expectation. The two strokes after en est de were recorded literally as =, not expanded to même. Family alphabets and indices were read from each occurrence. The comparison used to decide des versus deux was a comparison of letter strokes within this page, not mathematical reasoning.',
 author_checks='The inserted author wording says C\u2019est néc et suffisant pour la validité des (validité remains uncertain in its first group). There is no visible author check mark or explicit verification instruction. This transcription does not claim that C4 or any corollary has been verified.',
 title_dates_pagination='Only the handwritten page number 64 appears at top centre. The reading retains scanpage{65} and mspage{64}; no cote marker was added because this C fragment had none. No title or date is on the page.',
 witness_encoding='Equivalent state macro names (struck/deleted, uncertain/unsure) and emph/uline for the same underline were not counted solely for syntax. The emptyset/varnothing rendering choice was likewise treated as the same handwritten slashed-oval sign. Family alphabet differences were counted because the brief explicitly requires alphabet fidelity.'
)

report=dict(reader='R2',cote='156-4',scan='065',brief_version='v01',started_utc='2026-11-20T08:57:53Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),image_views=[whole,a,b],reading_file=str(out/'reading.tex'),differences=D,c_doubts=CD,inventory=INV,remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,notes=notes,check_events=[],crops=crops,workflow_feedback=['The mandated one-crop rule worked for this page. Connected correction clusters (especially Cor. 2) need to be treated as one open place so the insertion connector and its destination remain visible.','The brief does not explicitly say whether editorial insertion borders count as drawings; I treated the Cor. 2 border as insertion markup, documented its geometry, and did not add an independent diagram.'])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

observations=[
 'Cancelled F_i is clear; following C-shaped trace and possible opening parenthesis remain inseparable. Closing parenthesis is clear.',
 'Parallel middle bars and residual bent upper-left stroke support an overwritten family F; small low loop retains F_0/F doubt.',
 'Article before cas remains le/les; cas and following où are live, with no cancelled extra group.',
 'Word after à is best des; terminal mark lacks the crossed x visible in cancelled deux elsewhere on this same page.',
 'connexes disjointes is legible. After comp the terminal loop is attached; period remains uncertain. Lower-case x and y and final compatibles point are visible.',
 'néc has no detached final point. Lower line best one crowded validité, with no separate deleted word securely distinguishable. Note ends des.',
 'Corollaire 1 is underlined including digit. No additional parenthesis or punctuation follows the digit.',
 'Cancelled group best pres remains uncertain. Clear separate que tout i. follows; no un nb fini d’i.',
 'Cor. 2 is inserted with underline and angular connector. Cancelled donc is lower-case. Article after dans is retraced le/les; no securely separable old/new full words. Deux and suivants crossed, I est above suivants, short abandoned f before live fini; final point visible.',
 'Both lettered cases are fully crossed. Toute begins capital T. Short independent dash before alors lies below long strike.',
 'Cancelled word after figures supports de/des; far-right tail hidden by crossing. Live Alors il en below is legible.',
 'Inserted (resp. finies) stands above clearly cancelled Alors il; no need to leave latter unread.',
 'Two bars decide literal =. Following cancelled de has recognizable d and e. Soient has i-dot and t endpoint.',
 'Final separator is a plain horizontal stroke with downturned end, no visible arrowhead. Product and family index i are clear.',
 'No dot follows ens. Final pres que has a clear gap, no accent. Final i and full stop are visible.'
]
with (out/'inspection_log.md').open('a',encoding='utf-8') as f:
 f.write('\n## Tight-crop inspection sequence\n\nEvery crop below was selected independently after the half views and viewed exactly once. No crop was regenerated or used for a second inspection. All bboxes refer to the whole original JPG. Each crop was autocontrasted (cutoff 0), resized by PIL LANCZOS to 2400 px wide, and sharpened with ImageEnhance.Sharpness factor 1.25. All rotations were 0 degrees. PNG format was already generated before the parent suggested JPEG for future crops.\n\n')
 for i,(cr,obs) in enumerate(zip(crops,observations),4):
  f.write(f'{i}. `{cr["path"]}`\n\n   Source: `{cr["source"]}`; original bbox `{cr["bbox"]}`; scale {cr["scale"]:.9f}; rotation {cr["rotation"]}°.\n\n   Reason: {cr["reason"]}\n\n   Visible evidence: {obs}\n\n')
 f.write('## Completion\n\nAll manuscript lines were compared against both witnesses. No OCR, text-recognition tool, browsing, other scans, or other reader files were used. No mathematical verification was performed; report check_events is intentionally empty. No view was repeated.\n')
print(json.dumps({'reading_file':str(out/'reading.tex'),'report_file':str(out/'report.json'),'differences':len(D),'c_doubts':len(CD),'inventory':len(INV),'remaining_doubts':len(remaining),'crops':len(crops)},indent=2))
