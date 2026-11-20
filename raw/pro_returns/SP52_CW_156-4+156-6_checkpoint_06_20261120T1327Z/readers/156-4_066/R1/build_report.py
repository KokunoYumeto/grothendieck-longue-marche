from pathlib import Path
import json
from datetime import datetime,timezone
R=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R1')
W='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg'
A=W[:-4]+'_a.jpg'; B=W[:-4]+'_b.jpg'
crops=json.loads((R/'crop_manifest.json').read_text())
D=[]
def add(loc,c,h,reading,shows,kind='other',conf='high',mh='no',cc=False,ch=True,cr=None,box=None,src=A,mc=False):
    if cr is not None:
        crop=crops[cr-1]; path=crop['path']; box=crop['bbox']; src=crop['source']
    else: path=None
    D.append(dict(id=f'R1-066-D{len(D)+1:02}',location=loc,c=c,h=h,reading=reading,scan_shows=shows,confidence=conf,kind=kind,marked_in_h=mh,change_c=cc,change_h=ch,crop=path,bbox=box,bbox_image=src,math_consequential=mc))
add('Opening, after résulte','du','de','du','The second small letter after the d has the low joined u form.','misread word',box=[699,75,805,152])
add('Opening deletion, C of C4',r'\deleted{\uline{C}4 et}',r'\struck{C4 et}',r'\deleted{\uline{C}4 et}','A short separate underline lies under the cancelled C; the longer cancellation passes through C4 et.','omission',box=[804,73,1021,150])
add('Lemma, parenthetical reminder',r'\inserted{(resp. \unsure{fini|finie})}','(resp. fini)',r'\inserted{(resp. fini)}','The entire parenthesis stands above the t. f. line; it is an insertion.','insertion or placement',cr=1)
add('Lemma, final letters of fini',r'\unsure{fini|finie}','fini','fini','The last short body stroke has a separate i dot; no further e body intervenes before the parenthesis.','other',cc=True,ch=False,cr=1)
add('Lemma, after the raised reminder','Il','il','il','The initial short body has a detached dot, followed by the tall l.','other',cc=True,ch=False,cr=1)
add('Lemma, necessity and sufficiency abbreviation','f et s','faut et il suffit','f et s','Only f, the joined et, and s are written; there are no full words or terminal points.','abbreviation expanded or spelling modernised',cr=2)
add('Lemma b), initial word','Tous','tous','Tous','The initial T is a tall capital with a long top arm.','other',box=[369,386,502,453])
add('Lemma b), after un',r'\unsure{nb}','nb','nb','A low n-shaped entry is followed by the short upright and return of b.','other',cc=True,ch=False,cr=3)
add('Lemma b), verb before the empty set','sont','soient','sont','The surviving forms are s followed by the joined ont; there is no separate i or i dot.','misread word',cr=3)
add('Notations heading','Notations',r'\emph{Notations}','Notations','There is no underline below this heading.','other',box=[303,539,559,629])
add('Notations, NB clause','Si','si','Si','The first letter is a large looped S, followed by the short dotted i.','other',box=[1075,531,1144,596])
add('Notations, immediately after pi_0(G)',r'\deleted{\unsure{)|?}}',r'\ill{}',r'\deleted{\unsure{)}}','One cancelled curved group is present before the comma. A closing parenthesis is the best reading, but the crossing loop prevents certainty; no independent question-mark body is identifiable.','deletion state (struck given live or live given struck)',conf='medium',mh='yes',cc=True,cr=4)
add('Notations, after transitivité)',')', '),', ')','The closing parenthesis ends the line; no following comma is visible.','text not on the page',box=[1318,626,1432,721])
add('Notations, ambient object',r'\pi_0(M)',r'\pi_0(\mathcal M)',r'\pi_0(M)','The M is a plain peaked capital with its normal entry and exit strokes.','misread symbol or index',box=[284,772,512,865])
add('Notations, cancelled first exponent',r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}',r'\note{signe biffé}',r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}','Three upper small shapes are crossed. The first two remain too entangled to separate cat from act; the last tall t-like stroke is clear.','readable ink left as \\ill{}',conf='low',mh='yes',cr=5)
add('Notations, first live exponent',r'\pi_0^{!}',r'\pi_0^{\cdot}',r'\pi_0^{!}','The live exponent has a distinct upright and a separate lower dot.','misread symbol or index',mh='yes',cr=5,mc=True)
add('Notations, first family argument',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The family sign has a looped upper arm and curved lower foot, not Gothic strokes.','misread symbol or index',cr=5)
add('Notations, low point inside first family parenthesis','','',r'\unsure{.}','A discrete low short ink stroke stands between the left parenthesis and the family sign. It may be incidental ink; it is marked as a doubtful literal point rather than silently suppressed.','omission',conf='low',cc=True,cr=5)
add('Notations, Attention',r'\unsure{Attention}','Attention',r'\unsure{Attention}','The A, tall t strokes and comma are visible, but the central and final letters collapse into connected runs.','other',conf='medium',cr=6)
add('Notations, second exponent',r'\unsure{d|!}',r'\cdot',r'\unsure{d|!}','The upper component has a closed lower-left loop against a heavy upright, favouring d. A distinct lower round point survives, so an overwritten ! remains possible.','misread symbol or index',conf='medium',mh='yes',cr=7,mc=True)
add('Notations, second family argument',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The upper arm loops and the foot bends, as independently visible at this occurrence.','misread symbol or index',cr=7)
add('Notations, comparison object after n\'est pas',r'\pi_0(F,\leq)',r'\pi_0(\mathfrak F,\leq)',r'\pi_0(F,\leq)','This F has plain top and middle arms, without the looped family form.','misread symbol or index',box=[753,850,1050,943],mc=True)
add('Notations, article before Sup',r'\unsure{du|des}','des',r'\unsure{du|des}','The d is distinct. Its joined continuation favours u but is too compressed to exclude es.','other',conf='medium',cr=8)
add('Notations, Sup',r'\unsure{Sup}','Sup','Sup','The capital S, low u run and descending p are identifiable.','other',cc=True,ch=False,cr=8)
add('Notations, quotation extent and quotation marks',r'``en tenant compte \unsure{du|des} \unsure{Sup}\'\'',r'\ill{} en tenant compte des « Sup »',r'``en tenant compte \unsure{du|des} Sup\'\'','Two small opening strokes precede en; the two closing strokes follow Sup. The quote covers the whole phrase and there are no guillemets around Sup alone.','misread symbol or index',mh='yes',cr=8)
add('Notations, after the quoted phrase',r"Sup''. Si",r'« Sup ».) Si',r"Sup''. Si",'A point follows the closing quotation strokes, then Si. No closing parenthesis is present here or at the end of the tuple sentence.','text not on the page',cr=8)
add('Notations, C at the start of the tuple',r'\unsure{\mathcal C|\mathscr C|C}',r'\mathcal C',r'\unsure{\mathcal C|\mathscr C|C}','The capital has a rounded outer curve and an inward top return; the exact calligraphic/script/plain alphabet remains undecided.','other',conf='medium',cr=9)
add('Notations, family in the tuple',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The family F has the curved slanting stem and upper arm at this occurrence.','misread symbol or index',cr=9)
add('Notations, third relation in the tuple',r'\deleted{\unsure{\leq|\prec}}\unsure{\preceq|\leqslant}',r'\ldots',r'\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}','There is one heavily worked relation-sized group, with an ascending arm and several bowed returns. I cannot extract a separately legible predecessor or settle whether the entire relation is cancelled.','deletion state (struck given live or live given struck)',conf='low',mh='yes',cc=True,cr=10,mc=True)
add('Notations, clause following tuple','on pose aussi','on peut aussi écrire','on pose aussi','The visible sequence is on, a p-led short word, and aussi; no separate écrire group is present.','misread word',cr=11)
add('Notations, gloss below C',r'\margin{\unsure{Contrée|Contrie}}',r'\note{« contrée »}',r'\unsure{Contrée|Contrie}','The gloss is below the initial C and connected to it. The raised mark before the final vowel is too short to settle é versus i.','insertion or placement',conf='medium',mh='yes',cr=9)
add('Notations, gloss below third relation',r'\margin{qui ne sert \deleted{\unsure{pourtant}} \unsure{à} rien ici}',r'\note{« \ill{} vues ici »}',r'qui ne sert \unsure{pourtant|pour\deleted{tant}|\deleted{pourtant}} \unsure{à|:} rien ici','The first line reads qui ne sert; the last line reads rien ici. The intervening word and two-stroke mark require the separate state doubts recorded below.','readable ink left as \\ill{}',conf='medium',mh='yes',cc=True,cr=10)
add('Notations, pourtant in the right gloss',r'\deleted{\unsure{pourtant}}',r'\ill{}',r'\unsure{pourtant|pour\deleted{tant}|\deleted{pourtant}}','There is one word-sized group. Its initial pour remains unobstructed; strong horizontal strokes cross the latter portion and may be cancellation or long t crossbars.','deletion state (struck given live or live given struck)',conf='low',mh='yes',cc=True,cr=10)
add('Notations, mark after pourtant',r'\unsure{à}',r'\ill{}',r'\unsure{à|:}','Only two short vertically separated marks survive; à is plausible, but a colon-like reading cannot be excluded from the strokes.','other',conf='low',mh='yes',cc=True,cr=10)
add('Notations, two gloss pointers','','',r'\figure{\begin{tikzpicture}...\end{tikzpicture}}','A slanting bare stroke links C to its gloss; the relation has an upright pointer with a curved cap. Both are reproduced in TikZ.','drawing or diagram',cc=True,cr=10)
add('Axiome heading, underline state','Axiome renforcé',r'\emph{Axiome \uncertain{renforcé}}','Axiome renforcé','There is no underline beneath this heading.','other',mh='yes',box=[414,203,1067,311],src=B)
add('Axiome heading, final word','renforcé',r'\uncertain{renforcé}','renforcé','The word shows the long descending f, the following run and a separate rising accent at the end.','other',mh='yes',box=[752,199,1067,313],src=B)
add('C4 bis, underline',r'\uuline{C4 bis}',r'\emph{C4 bis}',r'\uuline{C4 bis}','Two separate underlining strokes meet and cross beneath the label.','other',box=[268,364,514,477],src=B)
add('C4 bis, product family',r'\prod\mathcal F_i',r'\prod\mathfrak F_i',r'\prod\mathcal F_i','The indexed family has the slanted head and curved foot; its i is short and dotted.','misread symbol or index',box=[1224,296,1413,408],src=B)
add('C4 bis, cancelled right edge',r'\deleted{\unsure{\exists F|\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\exists\mathcal F}','Two distinct groups survive the diagonal strikes: a three-bar existential sign and a loop-headed family F. The aborted fragment is not regularized to exists F.','readable ink left as \\ill{}',conf='medium',mh='yes',cc=True,cr=12)
add('C4 bis, family after the live membership',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The live family letter has an oblique top and curved lower end.','misread symbol or index',box=[471,479,555,568],src=B)
add('C4 bis, restricted ambient set',r'M_i',r'\mathcal M_i',r'M_i','The M is the same plain peaked capital, with a small dotted i.','misread symbol or index',cr=13)
add('C4 bis, overwritten result F_i',r'\deleted{\unsure{\mathcal F}}F_i',r'F_i',r'\unsure{F_i|\deleted{\mathcal F}F_i}','One F-sized group contains several stems and bars. A plain final F_i is visible. A former family F is possible but cannot be separated confidently from retracing.','deletion state (struck given live or live given struck)',conf='low',cc=True,cr=13)
add('C4 bis, terminal relation',r'i\unsure{\vdash|\in}I',r'i\in I',r'i\vdash I','The relation is an upright with one rightward crossbar. It has no rounded left bowl or separate lower arm of the nearby membership sign.','misread symbol or index',cc=True,cr=14,mc=True)
add('C4 bis, final punctuation','.','.',r'\unsure{.|,}','The final little mark is a short bent descending stroke rather than a round dot; its period/comma value remains uncertain.','other',conf='medium',cc=True,cr=14)
add('Lower heading, Contrée',r'\unsure{Contrée|Contrie}','Contrée',r'\unsure{Contrée|Contrie}','The compressed middle and short raised mark do not definitively distinguish the accented e from a dotted i.','other',conf='medium',cr=15)
add('Lower heading, résiduelle',r'\unsure{résiduelle|réssiduelle}','résiduelle','résiduelle','After the initial accented run there is one s-shaped curve followed by the dotted i, not two s bodies.','other',cc=True,ch=False,cr=15)
add('Lower heading, final noun','cosupport','complément','cosupport','The word has co followed by the support form, with the pair of descending p strokes.','misread word',box=[1364,652,1636,771],src=B)
add('Lower heading, separate underlines',r'\uline{Support} \uline{et} \uline{cosupport}',r'\emph{Support et complément}',r'\uline{Support} \uline{et} \uline{cosupport}','There are three strokes: one below Support, a short one below et, and a long one below cosupport.','other',box=[1000,647,1638,773],src=B)
add('Bottom paragraph, initial cancelled family',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}','A parenthesized indexed letter and a later family F are visible through the cancellation. The first letter favours F, but the strokes do not safely exclude H or expose all of the intervening relation.','readable ink left as \\ill{}',conf='low',mh='yes',cr=16)
add('Bottom paragraph, family after Phi subset',r'\Phi\subset\mathcal F',r'\Phi\subset\mathfrak F',r'\Phi\subset\mathcal F','The inclusion is open and the following family letter has a slanted head and curved stem.','misread symbol or index',box=[900,789,1141,884],src=B)
add('Bottom paragraph, H_i insertion position',r'figures \inserted{$H_i$}',r'\Phi\subset\mathfrak F\add{$H_i$} un ens. de figures',r'figures \inserted{$H_i$}','The added H_i lies above the end of figures; the long oblique connector reaches the position at the end of that word.','insertion or placement',cr=16)
add('Bottom paragraph, oblique insertion connector','','',r'\figure{\begin{tikzpicture}...\end{tikzpicture}}','A long oblique curved stroke accompanies H_i and reaches the end of figures. Its relative placement is reproduced in TikZ.','drawing or diagram',cc=True,cr=16)
add('Bottom paragraph, cancelled expression after Pour',r'\deleted{\unsure{Cosupp.} $\Phi$}',r'\struck{Compl.\ $\Phi$}',r'\deleted{Cosupp. $\Phi$}','The deletion contains the initial Co, a compressed su run, and two descending p bodies followed by a point and Phi.','misread word',cc=True,cr=17)
add('Bottom paragraph, disjointe ending',r'\unsure{disjointe|disjoint}','disjointe',r'\unsure{disjointe|disjoint}','A short return follows the crossed final t, favouring e, but it can also be the t exit stroke.','other',conf='medium',cr=18)
add('Bottom paragraph, necessity and sufficiency abbreviation','il f et s.','il faut et il suffit','il f et s.','Only il, f, et, s and a final separate point are present.','abbreviation expanded or spelling modernised',cr=18)
add('Bottom paragraph, final parenthesis','(à cause de C3)','(cf. conséquence de C3)','(à cause de C3)','The short accented à is followed by cause de. There is no cf. or conséquence word.','misread word',box=[313,1180,991,1253],src=B)
add('Bottom paragraph, final deleted word',r'\deleted{\unsure{Posons|Poser}}',r'\struck{Posons}',r'\deleted{Posons}','The crossed word shows P, the os group, a following o loop, then the n run and final s turn.','other',cc=True,ch=False,cr=19)

CD=[]
def doubt(loc,c,read,status,shows,cr=None,box=None,src=A):
    if cr:
        x=crops[cr-1]; path=x['path']; box=x['bbox']; src=x['source']
    else:path=None
    CD.append(dict(location=loc,c=c,reading=read,status=status,scan_shows=shows,crop=path,bbox=box,bbox_image=src))
doubt('Lemma insertion',r'\unsure{fini|finie}','fini','resolved','The final dotted i precedes the closing parenthesis without a further e.',1)
doubt('Lemma b), nb',r'\unsure{nb}','nb','resolved','The short n entry and following b return are distinct.',3)
doubt('Notations, cancelled sign after pi_0(G)',r'\deleted{\unsure{)|?}}',r'\deleted{\unsure{)}}','revised','Best closing parenthesis remains doubtful; no independent question-mark form can be recovered.',4)
doubt('Notations, cancelled exponent',r'\unsure{\mathrm{cat}|\mathrm{act}}',r'\unsure{\mathrm{cat}|\mathrm{act}}','retained','Crossing strokes prevent the first two small letters from being ordered with certainty.',5)
doubt('Notations, Attention',r'\unsure{Attention}',r'\unsure{Attention}','retained','The initial and t strokes are clear; the remaining letter runs stay compressed.',6)
doubt('Notations, second exponent',r'\unsure{d|!}',r'\unsure{d|!}','retained','A closed d-like loop and heavy upright sit above a separate lower round point.',7)
doubt('Notations, article before Sup',r'\unsure{du|des}',r'\unsure{du|des}','retained','Joined final strokes favour u but do not exclude es.',8)
doubt('Notations, Sup',r'\unsure{Sup}','Sup','resolved','S, u run and descending p are distinguishable.',8)
doubt('Notations, C alphabet',r'\unsure{\mathcal C|\mathscr C|C}',r'\unsure{\mathcal C|\mathscr C|C}','retained','The inward curl is real but does not decide a formal alphabet.',9)
doubt('Notations, supposed earlier third relation',r'\deleted{\unsure{\leq|\prec}}',r'\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}','revised','Only one worked cluster is visible; no distinct predecessor can be extracted safely.',10)
doubt('Notations, final third relation',r'\unsure{\preceq|\leqslant}',r'\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}','revised','The bowed returns support these forms, while cancellation state is unresolved.',10)
doubt('Notations, gloss below C',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','Short raised stroke above compressed ending does not settle é/i.',9)
doubt('Notations, pourtant cancellation',r'\deleted{\unsure{pourtant}}',r'\unsure{pourtant|pour\deleted{tant}|\deleted{pourtant}}','revised','The first part is unobstructed; only the latter part has crossing strokes, potentially t bars.',10)
doubt('Notations, à in right gloss',r'\unsure{à}',r'\unsure{à|:}','revised','Two separate short strokes have no clear a bowl and permit a colon-like reading.',10)
doubt('C4 bis, right-hand deletion',r'\deleted{\unsure{\exists F|\mathcal F}}',r'\deleted{\exists\mathcal F}','resolved','Two distinct glyphs survive: an existential sign and a loop-headed family F.',12)
doubt('C4 bis, prior sign beneath F_i',r'\deleted{\unsure{\mathcal F}}F_i',r'\unsure{F_i|\deleted{\mathcal F}F_i}','revised','One retraced F-sized group; prior family F remains possible but is not separately legible.',13)
doubt('C4 bis, relation before I',r'\unsure{\vdash|\in}',r'\vdash','resolved','One upright and one right bar, with no left bowl.',14)
doubt('Lower heading, Contrée',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','Compressed final vowel and short raised stroke remain ambiguous.',15)
doubt('Lower heading, résiduelle',r'\unsure{résiduelle|réssiduelle}','résiduelle','resolved','One s body precedes the dotted i.',15)
doubt('Bottom paragraph, first deletion',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}','retained','The cancellation obscures the first indexed letter and intervening relation.',16)
doubt('Bottom paragraph, Cosupp.',r'\unsure{Cosupp.}','Cosupp.','resolved','The two descending p bodies and final point are visible.',17)
doubt('Bottom paragraph, disjointe',r'\unsure{disjointe|disjoint}',r'\unsure{disjointe|disjoint}','retained','The terminal short return may be e or the exit of t.',18)
doubt('Last line, deleted Posons',r'\unsure{Posons|Poser}','Posons','resolved','The later o loop, n run and final s turn are visible under the cancellation.',19)
doubt('Notations, unclosed Attention parenthesis','No closing parenthesis visible','No closing parenthesis supplied','resolved','The phrase ends with quotation strokes and a point, then Si; the tuple sentence ends with a point alone.',8)

inv=[]
def item(el,kind,pos,words): inv.append(dict(element=el,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
item('E01','text','top centre','65')
item('E02','text','top opening line','Ceci résulte du')
item('E03','deletion','within opening line','underlined C, then 4 et')
item('E04','text','upper block, three manuscript lines','underlined Lemme; Pour que F')
item('E05','insertion','above end of lemma first line','(resp. fini)')
item('E06','text','central upper block','Notations pi_0(F)')
item('E07','deletion','after pi_0(G)','uncertain closing parenthesis')
item('E08','deletion','above first family pi_0','cat/act')
item('E09','display','last line of Notations block','C=(cal F, leq, worked relation), on pose aussi pi_0(C)')
item('E10','deletion','third slot of tuple','possible cancellation or overwriting of the relation; state alternatives are explicit')
item('E11','margin note','below initial C in tuple','Contrée/Contrie; rendered in the annotated TikZ group')
item('E12','margin note','below third tuple relation','qui ne sert ... rien ici; rendered in the annotated TikZ group')
item('E13','deletion','middle line of right gloss','pourtant, possible partial or whole cancellation')
item('E14','drawing','between C and left gloss','sloping connector without an arrowhead')
item('E15','drawing','between third relation and right gloss','vertical pointer with curved cap')
item('E16','text','middle lower heading','Axiome renforcé')
item('E17','text','two-line axiom under heading','double-underlined C4 bis; Pour tout')
item('E18','deletion','end of C4 bis first line','exists cal F')
item('E19','deletion','result of restriction equation','possible former cal F beneath final F_i; correction-state alternatives explicit')
item('E20','text','lower left heading','underlined Contrée/Contrie résiduelle')
item('E21','text','lower right heading','separately underlined Support, et, cosupport')
item('E22','text','bottom paragraph','Soit ... Phi subset cal F ... Posons')
item('E23','deletion','after first Soit in bottom paragraph','(F_i) in cal F / (H_i) in cal F')
item('E24','insertion','above end of figures','H_i')
item('E25','drawing','beside inserted H_i and end of figures','long oblique curved insertion connector')
item('E26','deletion','after figures sentence','On posera')
item('E27','deletion','after Pour','Cosupp. Phi')
item('E28','deletion','last line, before live Posons','Posons')

rem=[
 dict(location='Notations, after pi_0(G)',reading=r'\deleted{\unsure{)}}',alternatives=['closing parenthesis','unrecoverable cancelled curved sign'],confidence='medium',reason='The cancellation loop crosses the curved body.'),
 dict(location='Notations, cancelled exponent',reading=r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}',alternatives=['cat','act'],confidence='low',reason='The first two small shapes are obscured by cancellation.'),
 dict(location='Notations, low mark before first family F',reading=r'\unsure{.}',alternatives=['literal low point','incidental ink'],confidence='low',reason='A separate stroke is visible but its textual function is unknown.'),
 dict(location='Notations, Attention',reading=r'\unsure{Attention}',alternatives=['Attention'],confidence='medium',reason='Several middle and final letters are reduced to joined runs.'),
 dict(location='Notations, second exponent',reading=r'\unsure{d|!}',alternatives=['d','!','d written over !'],confidence='medium',reason='The upper loop favours d, while a detached lower round point remains.'),
 dict(location='Notations, article before Sup',reading=r'\unsure{du|des}',alternatives=['du','des'],confidence='medium',reason='The joined ending does not expose enough separate letters.'),
 dict(location='Notations, C alphabet, both occurrences',reading=r'\unsure{\mathcal C|\mathscr C|C}',alternatives=[r'\mathcal C',r'\mathscr C','C'],confidence='medium',reason='Different degrees of inward curl occur; these do not decide a formal alphabet.'),
 dict(location='Notations, tuple third relation',reading=r'\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}',alternatives=[r'\preceq',r'\leqslant',r'\deleted{\preceq}',r'\deleted{\leqslant}'],confidence='low',reason='One heavily worked cluster does not expose separate earlier and later signs or clear cancellation state.'),
 dict(location='Notations, left gloss',reading=r'\unsure{Contrée|Contrie}',alternatives=['Contrée','Contrie'],confidence='medium',reason='The short raised mark and reduced vowel body do not settle the ending.'),
 dict(location='Notations, right gloss, pourtant',reading=r'\unsure{pourtant|pour\deleted{tant}|\deleted{pourtant}}',alternatives=['pourtant',r'pour\deleted{tant}',r'\deleted{pourtant}'],confidence='low',reason='Crossing strokes cover the latter part and may be t bars or a partial/whole cancellation.'),
 dict(location='Notations, right gloss, à',reading=r'\unsure{à|:}',alternatives=['à',':'],confidence='low',reason='Only two separate short marks are visible; no secure a bowl.'),
 dict(location='C4 bis, result F_i correction',reading=r'\unsure{F_i|\deleted{\mathcal F}F_i}',alternatives=[r'F_i',r'\deleted{\mathcal F}F_i'],confidence='low',reason='Final plain F_i is visible; the possible underlying family F is inseparable from retracing.'),
 dict(location='C4 bis, final punctuation',reading=r'\unsure{.|,}',alternatives=['.',','],confidence='medium',reason='The mark is a bent descending stroke rather than an unambiguous dot.'),
 dict(location='Lower heading, first word',reading=r'\unsure{Contrée|Contrie}',alternatives=['Contrée','Contrie'],confidence='medium',reason='Compressed ending and short raised mark.'),
 dict(location='Bottom paragraph, first deletion',reading=r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',alternatives=[r'(F_i)\in\mathcal F',r'(H_i)\in\mathcal F'],confidence='low',reason='The overstriking obscures the indexed first letter and membership region.'),
 dict(location='Bottom paragraph, disjointe',reading=r'\unsure{disjointe|disjoint}',alternatives=['disjointe','disjoint'],confidence='medium',reason='The final short return may be an e or the exit stroke of t.'),
]
notation=[
 dict(sign='individual figure F',latex='F, F_i',appearance='plain upper and middle arms; small dotted i',location='lemma, component map, comparison argument, C4 bis and bottom paragraph',alternatives=[]),
 dict(sign='family F',latex=r'\mathcal F,\mathcal F_i',appearance='looped or sloping upper arm and curved foot',location='Notations family arguments, tuple, product and bottom set of figures',alternatives=[]),
 dict(sign='ambient set M',latex='M,M_i',appearance='plain peaked capital with normal entry and exit strokes',location='pi_0(M), restriction equation',alternatives=[]),
 dict(sign='component index',latex=r'\pi_0',appearance='low small oval, lower than the pi body',location='Notations',alternatives=[]),
 dict(sign='first live superscript',latex='!',appearance='separate short upright and lower point beneath cancelled cat/act',location='first pi_0 of family',alternatives=[]),
 dict(sign='second superscript',latex=r'\unsure{d|!}',appearance='closed lower-left loop at a heavy upright; separate lower round point',location='Attention clause',alternatives=['d','!','d over !']),
 dict(sign='contrée capital',latex=r'\unsure{\mathcal C|\mathscr C|C}',appearance='rounded outer curve with inward return, larger in the final occurrence',location='tuple and pi_0(C)',alternatives=[r'\mathscr C','C']),
 dict(sign='third tuple relation',latex=r'\unsure{\preceq|\leqslant|\deleted{\preceq}|\deleted{\leqslant}}',appearance='ascending arm and several bowed lower returns, heavily worked',location='third tuple slot',alternatives=[r'\leqslant','possible cancellation']),
 dict(sign='terminal axiom relation',latex=r'\vdash',appearance='straight upright with one rightward crossbar',location='C4 bis, i vdash I',alternatives=[]),
 dict(sign='empty set',latex=r'\varnothing',appearance='oval traversed by long diagonal slash',location='lemma b)',alternatives=[]),
 dict(sign='inserted indexed H',latex='H_i',appearance='two straight uprights and crossbar, small dotted i',location='above figures in bottom paragraph',alternatives=[]),
 dict(sign='capital Phi',latex=r'\Phi',appearance='broad oval traversed by a vertical and lower bar',location='bottom set and cancelled Cosupp expression',alternatives=[])
]
abr=[dict(form=a,expansion=b) for a,b in [('cor.','corollaire'),('t. f.','type fini'),('resp.','respectivement'),('f et s','faut et suffit'),('f et s.','faut et suffit'),('nb','nombre'),('NB','nota bene'),('ens.','ensemble'),('Cosupp.','cosupport')]]
evidence=[
'Raised parenthesis is wholly inserted. Final dotted i resolves fini. Following dotted initial and tall l read il.',
'Long descending f, compressed et, and separate s; no full words and no terminal punctuation.',
'nb resolved from two small bodies. fini sont and slashed oval are visible; no i inside sont.',
'One cancelled curved sign before a comma. Closing parenthesis is best but remains unsure; no distinct question-mark form.',
'First exponent is definite ! below cancelled cat/act. Family F is looped. A separate low stroke inside the parenthesis is marked as a doubtful point.',
'Attention retained as unsure: initial A, t strokes and comma are visible, but central/final letter runs stay compressed.',
'Upper component strongly d-like, with closed lower-left loop and heavy upright; separate lower circle/point keeps d versus overwritten ! open.',
'Double quotation strokes enclose the whole phrase. du/des retained; Sup resolved. Point and Si follow without closing parenthesis.',
'First C has inward curl but alphabet remains open. Lower Contrée/Contrie remains doubtful. The connector is a plain slanted stroke.',
'One worked comparison cluster, not separately legible predecessor plus replacement. Right gloss reads qui ne sert / pourtant [state doubtful] à/: / rien ici. Curved-cap upward pointer visible.',
'on pose aussi is confirmed; no separate écrire. Final C has a longer inward return and is taken as the same locally ambiguous capital.',
'Two cancelled groups resolve to existential sign followed by loop-headed family F; not one isolated family sign.',
'Plain final F_i visible in one multiply retraced cluster. Possible former family F not separable with confidence. M_i plain.',
'Terminal relation resolves to vdash from its upright and right bar. The final mark remains period/comma doubtful.',
'Contrée/Contrie remains open. résiduelle resolves to one s before the dotted i. Continuous underline covers both heading words.',
'Cancelled parenthesized indexed family remains doubtful. H_i and its long oblique connector place insertion after figures. Separate On posera is cancelled.',
'Cosupp. resolves: two descending p bodies and following point; Phi is clear. Entire expression is cancelled.',
'disjointe/disjoint remains open because final return may be e or t exit. The later f et s. abbreviation is explicit.',
'Cancelled Posons resolves: os, later o loop, n run and terminal s visible; live replacement Posons has no following point.'
]
finish=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
report=dict(reader='R1',cote='156-4',scan=66,brief_version='v02',started_utc='2026-11-20T09:23:41Z',finished_utc=finish,image_views=[W,A,B],reading_file=str(R/'reading.tex'),differences=D,c_doubts=CD,inventory=inv,remaining_doubts=rem,notation=notation,abbreviations=abr,notes=dict(summary='One handwritten subject-notes page with a lemma, a Notations discussion and two connected glosses, strengthened axiom C4 bis, and the beginning of a section on the residual contrée, support and cosupport. Every manuscript block and cancellation has been represented. The worked tuple relation and correction states are deliberately left open where the ink does not separate them.',math_reading_decisions='The expected membership at the end of C4 bis made the straight relation worth targeted inspection; its visible upright and single right bar decide vdash, which is retained without mathematical repair. Distinguishing an individual plain F from the looped family F also mattered at pi_0(F,leq). No theorem, equivalence or axiom was proved or refuted. Exponent and tuple-relation readings were not inferred from the expected mathematics.',author_checks='No outside-page research or mathematical validation. Cancelled exists cal F is copied as an aborted fragment. The multiply worked tuple relation and F_i are each treated as one physical cluster, with explicit alternatives for correction/cancellation state rather than invented separate complete undertexts.',title_dates_pagination='Manuscript page 65 at top centre; assigned scan 66. Internal headings: Lemme; Notations; Axiome renforcé; C4 bis; Contrée/Contrie résiduelle; Support et cosupport. No date, separate title sheet or page count is visible.'),check_events=[],crops=[{k:v for k,v in c.items() if k!='transformations'} for c in crops],workflow_feedback=['The supplied C_context.md includes a scan-70 entry; it was not investigated or used for this page.','For marginal/interlinear glosses attached by drawn pointers, the brief does not explicitly prescribe whether to prefer margin macros or labels inside the required TikZ reproduction. I render the tuple and both glosses together in TikZ, once, to preserve their positions and connectors.','Several tight crops retain same-formula or same-line context rather than an entire adjacent manuscript line; no crop was remade or viewed twice.'],inspection_log=str(R/'inspection_log.md'))
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (R/'inspection_log.md').open('a') as f:
    for i,(c,e) in enumerate(zip(crops,evidence),start=4):
        f.write(f"{i}. Viewed once: {c['path']}\n   Source: {c['source']}\n   Original bbox: {c['bbox']}; scale: {c['scale']:.8f}; rotation: 0°.\n   Transformations: {', '.join(c['transformations'])}.\n   Evidence and decision: {e}\n\n")
    f.write('## Completion\n\nAll 3 required source views and all 19 crop views were completed once. No half was redisplayed or enlarged as a whole. No decided locus was recropped. The full reading, witness differences, 24 C doubt decisions, inventory, notation and remaining doubts were written. The TikZ reproductions use the observed pointer shapes and insertion placement; they are not mathematical diagrams. No mathematical proof check was performed.\n\nFinished: '+finish+'\n')
print(json.dumps(dict(differences=len(D),c_doubts=len(CD),inventory=len(inv),remaining_doubts=len(rem),crops=len(crops),finished_utc=finish)))
