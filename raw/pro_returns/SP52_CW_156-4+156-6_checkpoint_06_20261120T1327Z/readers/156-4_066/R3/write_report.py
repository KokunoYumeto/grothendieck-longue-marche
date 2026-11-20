from pathlib import Path
import json
from datetime import datetime, timezone
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R3')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg'
a=source.replace('.jpg','_a.jpg'); b=source.replace('.jpg','_b.jpg')
crops=json.loads((out/'crop_manifest.json').read_text())
reading=(out/'reading.tex').read_text()
figure=reading[reading.index('\\figure{'):reading.index('\n\nAxiome')]
diffs=[]
def d(location,c,h,r,e,confidence='high',kind='other',marked='no',cc=False,ch=True,crop=None,bbox=None,img=None,math=False):
    cm=crops[crop-1] if crop else None
    diffs.append(dict(id=f'R3-D{len(diffs)+1:02}',location=location,c=c,h=h,reading=r,scan_shows=e,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=cm['path'] if cm else None,bbox=bbox if bbox else cm['bbox'],bbox_image=img if img else source if cm else a,math_consequential=math))
d('Opening sentence, before the cancellation','du','de','du','The second letter is a joined low u, after the looped d.',kind='misread word',bbox=[703,80,804,145])
d('Opening sentence, cancelled C4 et',r'\deleted{\uline{C}4 et}',r'\struck{C4 et}',r'\deleted{\uline{C}4 et}','A short independent underline lies beneath the cancelled C; the longer strike crosses C4 et.',kind='omission',bbox=[800,70,1030,150])
d('Lemma, raised parenthesis placement',r'\inserted{(resp. \unsure{fini|finie})}','(resp. fini)',r'\inserted{(resp. fini)}','The whole parenthesis is on the raised line above t. f.; the long stroke beneath is continuous with the following l.',kind='insertion or placement',cc=False,crop=1)
d('Lemma, final word in raised parenthesis',r'\unsure{fini|finie}','fini','fini','The final small i and its point precede the closing parenthesis; there is no separate e return.',kind='other',cc=True,ch=False,crop=1)
d('Lemma, beginning of il f et s','Il','il','il','A detached point belongs to the small i before the tall looped l.',kind='other',cc=True,ch=False,crop=1)
d('Lemma, abbreviation','f et s','il faut et il suffit','f et s','The line contains a long descending f, et and a small s, with no written expansion.',kind='abbreviation expanded or spelling modernised',bbox=[240,285,461,391])
d('Lemma b), Tous','Tous','tous','Tous','The initial T has a high stem and broad cap.',kind='other',bbox=[357,382,494,452])
d('Lemma b), after un',r'\unsure{nb}','nb','nb','A low n is followed by the tall, compressed b; no point follows.',kind='other',cc=True,ch=False,crop=2)
d('Lemma b), last verb','sont','soient','sont','The word has the s and compressed ont strokes, without a separate dotted i.',kind='misread word',crop=2)
d('Notations heading','Notations',r'\emph{Notations}','Notations','There is no underline beneath Notations.',kind='other',bbox=[297,548,551,624])
d('Notations, after NB','Si','si','Si','The initial S is large and retraced, with a separate small dotted i.',kind='other',bbox=[1080,537,1148,589])
d('Notations, immediately after pi zero of G',r'\deleted{\unsure{)|?}}',r'\ill{}',r'\deleted{\unsure{)|?}}','There is one looped, crossed group before the following comma. The crossing is clear; the original sign is not.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',crop=3)
d('Notations, after transitivité)','transitivité)','transitivité),','transitivité)','The closing parenthesis has no following comma; the next item starts on the following line.',kind='text not on the page',bbox=[1235,620,1430,719])
d('Notations, argument M',r'\pi_0(M)',r'\pi_0(\mathcal{M})',r'\pi_0(M)','M has its ordinary two peaked strokes, not a separately curled alphabet.',kind='misread symbol or index',bbox=[290,778,507,847])
d('Notations, first superscript and its vertical arrangement',r'\pi_0^{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}!}',r'\pi_0^{\cdot}',r'\pi_0^{\substack{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}\\!}}','A cancelled three-letter group stands above a surviving upright and detached point. The visible ! is below the deleted letters, not merely a point.',confidence='medium',kind='insertion or placement',marked='yes',cc=True,crop=4,math=True)
d('Notations, first family argument',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The top arm curls into a loop and the stem has a hooked foot; it is a cursive family F.',kind='misread symbol or index',crop=4)
d('Notations, Attention certainty',r'\unsure{Attention}','Attention',r'\unsure{Attention}','The A and tall t strokes survive, but the compressed middle and ending do not justify removing the doubt.',confidence='medium',kind='other',crop=5)
d('Notations, second superscript',r'\pi_0^{\unsure{d|!}}',r'\pi_0^{\cdot}',r'\pi_0^{\unsure{d|!}}','The upper sign has a loop attached to a thick upright, and a detached low mark remains. This is more than a point, but d versus a modified ! remains open.',confidence='low',kind='misread symbol or index',marked='yes',crop=5,math=True)
d('Notations, second family argument',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The argument has a looped top and curved foot, matching the family form locally.',kind='misread symbol or index',crop=5)
d('Notations, argument before comma-leq',r'\pi_0(F,\leq)',r'\pi_0(\mathfrak{F}, \leq)',r'\pi_0(F,\leq)','The F has straight upper and middle arms and no curled top loop.',kind='misread symbol or index',crop=6,math=True)
d('Notations, quotation scope and opening mark',"``en tenant compte "+r'\unsure{du|des} '+r'\unsure{Sup}'+"''",r'\ill{} en tenant compte des « Sup »',"``en tenant compte du Sup''",'Two small opening strokes precede en; the two closing strokes follow Sup. The whole phrase is quoted.',kind='readable ink left as \\ill{}',marked='yes',crop=6)
d('Notations, article before Sup',r'\unsure{du|des}','des','du','The low joined final stroke is a u; there is no separate s after it.',kind='misread word',cc=True,crop=6)
d('Notations, Sup certainty',r'\unsure{Sup}','Sup','Sup','The tall S, reduced u and descending p are distinguishable.',kind='other',cc=True,ch=False,crop=6)
d('Notations, after the quotation',"Sup''. Si",'Sup ».) Si',"Sup''. Si",'A period follows the closing quotes, then Si. No closing parenthesis is present there or at the end of the tuple sentence.',kind='text not on the page',crop=6)
d('Notations, C at the left of the tuple',r'\unsure{\mathcal C|\mathscr C|C}',r'\mathcal{C}',r'\mathcal C','The upper terminal turns distinctly inward, supporting the cursive C. The final C in pi zero has the same conspicuous return.',kind='other',cc=True,ch=False,crop=8)
d('Notations, family in the tuple',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The first argument is the looped family F, not a Gothic letter.',kind='misread symbol or index',crop=7)
d('Notations, third tuple relation and cancellation state',r'\deleted{\unsure{\leq|\prec}}\unsure{\preceq|\leqslant}',r'\ldots',r'\unsure{\preceq|\leqslant|\deleted{\preceq}}','All strokes occupy one symbol-sized group: an upper arm and several bowed lower retracings. A separate old complete sign and a second live complete sign cannot be isolated. Cancellation itself remains an alternative.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',cc=True,crop=7,math=True)
d('Notations, note attached to C',r'\margin{\unsure{Contrée|Contrie}}','contrée',r'\unsure{Contrée|Contrie}','The word stands below C and has a short raised mark before its last e. That mark does not securely distinguish an acute from an i point. TikZ restores its subline placement.',confidence='medium',kind='insertion or placement',cc=True,crop=8)
d('Notations, note attached to the third relation',r'\margin{qui ne sert \deleted{\unsure{pourtant}} \unsure{à} rien ici}',r'\ill{} vues ici',r'qui ne sert\\\deleted{\unsure{pourtant}} \unsure{à}\\rien ici','Three lines read qui ne sert / a partly crossed word beginning p followed by a small raised mark / rien ici. The final line is not vues ici; pourtant and à remain uncertain.',confidence='medium',kind='readable ink left as \\ill{}',marked='yes',cc=True,crop=9)
d('Notations, two note connectors','', '',figure,'A short slanting line joins the C region to its lower gloss. A vertical line and curved cap point from the second lower note to the relation. They are reproduced, without inventing straight arrowheads.',kind='drawing or diagram',cc=True,crop=9,bbox=[213,1083,815,1290])
d('Notations, final clause','on pose aussi','on peut aussi écrire','on pose aussi','After on, the p descender and compressed ose are followed directly by aussi. No écrire group is present.',kind='misread word',bbox=[824,1055,1321,1155])
d('Axiome renforcé, underline state','Axiome renforcé',r'\emph{Axiome \uncertain{renforcé}}','Axiome renforcé','The heading is live and has no underline.',kind='other',bbox=[424,208,1062,311],img=b)
d('Axiome renforcé, final word certainty','renforcé',r'\uncertain{renforcé}','renforcé','The extended f and ending cé with its separate raised acute are visible.',kind='other',marked='yes',bbox=[750,207,1061,311],img=b)
d('C4 bis, double underline',r'\uuline{C4 bis}',r'\emph{C4 bis}',r'\uuline{C4 bis}','Two underline strokes run beneath the label, partly meeting at the centre.',kind='other',bbox=[267,355,512,475],img=b)
d('C4 bis, family in the product',r'\prod\mathcal F_i',r'\prod \mathfrak{F}_i',r'\prod\mathcal F_i','The factor has the cursive family-F stem and hooked lower stroke, with a small dotted i.',kind='misread symbol or index',crop=10)
d('C4 bis, cancelled expression after the product',r'\deleted{\unsure{\exists F|\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\unsure{\exists F|\exists\mathcal F}}','Two distinct vertical groups remain under the slanting strikes: a quantifier-shaped left group and an F-shaped right group. The alphabet of the right group remains doubtful.',confidence='low',kind='readable ink left as \\ill{}',marked='yes',cc=True,crop=10,math=True)
d('C4 bis, family after the live membership',r'\exists F\in\mathcal F',r'\exists\, F \in \mathfrak{F}',r'\exists F\in\mathcal F','The final F has the broad slanted top and curved foot of the family form.',kind='misread symbol or index',bbox=[280,474,558,573],img=b)
d('C4 bis, ambient M in the restriction',r'F\mid M_i',r'F|\mathcal{M}_i',r'F\mid M_i','The restriction bar is separate; M has ordinary peaked strokes, with a small dotted i.',kind='misread symbol or index',crop=11)
d('C4 bis, overwritten F before subscript i',r'\deleted{\unsure{\mathcal F}}F_i','F_i',r'\deleted{\unsure{\mathcal F}}F_i','Several parallel lower stems remain beneath the dark final F. This is one overwritten letter; the underlayer is only tentatively family F.',confidence='low',kind='omission',crop=11)
d('C4 bis, relation between i and I',r'i\unsure{\vdash|\in}I',r'i \in I',r'i\vdash I','The visible mark has a straight upright with one rightward crossbar. Unlike the nearby rounded membership signs, it has no visible upper or lower curved arms.',kind='misread symbol or index',cc=True,crop=11,math=True)
d('C4 bis, terminal punctuation','I.','I.','I,','The final small mark is a curved descending stroke rather than a compact point.',kind='other',cc=True,crop=11)
d('Lower heading, first word certainty',r'\unsure{Contrée|Contrie}','Contrée',r'\unsure{Contrée|Contrie}','A small raised mark is visible, but the local letter group remains compatible with an i point or the acute in é.',confidence='medium',kind='other',crop=12)
d('Lower heading, résiduelle',r'\unsure{résiduelle|réssiduelle}','résiduelle','résiduelle','There is one s-shaped group between the accented e and dotted i, followed by duelle.',kind='other',cc=True,ch=False,crop=12)
d('Lower heading, cosupport and underline segmentation',r'\uline{Support} \uline{et} \uline{cosupport}',r'\emph{Support et complément}',r'\uline{Support} \uline{et} \uline{cosupport}','The right word has co followed by two descending p strokes and the ending ort. Support, et and cosupport have separate underline strokes.',kind='misread word',crop=12,math=True)
d('Bottom, initial cancelled family',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}','A parenthesised indexed letter, intervening marks and a final family-F shape remain under heavy diagonal crossing. F versus H and the intervening expression remain tentative.',confidence='low',kind='readable ink left as \\ill{}',marked='yes',crop=13,math=True)
d('Bottom, family after Phi subset',r'\Phi\subset\mathcal F',r'\Phi \subset \mathfrak{F}',r'\Phi\subset\mathcal F','Phi has an oval across its upright; the inclusion is open; the following family F has a bent top and foot.',kind='misread symbol or index',bbox=[905,790,1152,867],img=b)
d('Bottom, inserted H_i placement',r'figures \inserted{$H_i$}',r'\Phi \subset \mathfrak{F} \add{$H_i$} un ens. de figures',r'figures\inserted{$H_i$}','H_i stands above the end of figures. Its sloping insertion guide meets the line between figures and its point, not after the family F.',kind='insertion or placement',crop=13)
d('Bottom, deleted Cosupp. Phi',r'\deleted{\unsure{Cosupp.} $\Phi$}',r'\struck{Compl.\ $\Phi$}',r'\deleted{Cosupp. $\Phi$}','Under the cancellation are Co, a compressed su and two long p descenders, followed by a separate point and Phi.',kind='misread word',cc=True,crop=14,math=True)
d('Bottom, disjointe ending',r'\unsure{disjointe|disjoint}','disjointe',r'\unsure{disjointe|disjoint}','A short descending return follows the crossed t, but it does not securely distinguish a final e from the t terminal.',confidence='medium',kind='other',crop=15)
d('Bottom, abbreviation f et s.','f et s.','il faut et il suffit','f et s.','A long descending f and the two small written groups et s. are present; the expanded words are absent.',kind='abbreviation expanded or spelling modernised',crop=15)
d('Bottom, parenthesis referring to C3','(à cause de C3)','(cf. conséquence de C3)','(à cause de C3)','The opening has a small a with grave, then the compact cause and de groups. There is no cf. or conséquence.',kind='misread word',crop=16)
d('Bottom, final cancelled word',r'\deleted{\unsure{Posons|Poser}}',r'\struck{Posons}',r'\deleted{Posons}','P, the two rounded o groups and the final ns wave remain below the strike. The following live word is a separate Posons.',kind='other',cc=True,ch=False,crop=16)

cd=[]
def doubt(location,c,r,status,e,crop=None,bbox=None,img=None):
    cm=crops[crop-1] if crop else None
    cd.append(dict(location=location,c=c,reading=r,status=status,scan_shows=e,crop=cm['path'] if cm else None,bbox=bbox if bbox else cm['bbox'],bbox_image=img if img else source if cm else a))
doubt('Lemma, raised parenthesis',r'\unsure{fini|finie}','fini','resolved','The final i and point are followed by the parenthesis, with no extra e.',1)
doubt('Lemma b)',r'\unsure{nb}','nb','resolved','The low n and tall compact b are visible.',2)
doubt('Notations, after pi zero of G',r'\deleted{\unsure{)|?}}',r'\deleted{\unsure{)|?}}','retained','The crossed loop does not reveal its original form.',3)
doubt('Notations, cancelled upper letters',r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}',r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}','retained','The final t is clearer than the two lower looped letters under the strike.',4)
doubt('Notations, surviving first superscript',r'\pi_0^{!}',r'\pi_0^{!}','resolved','A detached point lies below the separate upright; deleted letters stand above both.',4)
doubt('Notations, parenthetical opening',r'\unsure{Attention}',r'\unsure{Attention}','retained','A and tall t strokes are visible; the remaining word is compressed.',5)
doubt('Notations, second superscript',r'\unsure{d|!}',r'\unsure{d|!}','retained','A loop joins a tall dark stem and a low separate mark remains.',5)
doubt('Notations, article in the quote',r'\unsure{du|des}','du','resolved','The ending has one joined u stroke and no separate s.',6)
doubt('Notations, quoted noun',r'\unsure{Sup}','Sup','resolved','The capital S and descending p bracket the reduced u.',6)
doubt('Notations, quotation strokes',"`` ... ''","``en tenant compte du Sup''",'resolved','Two tiny opening strokes stand before en and two closing strokes after Sup.',6)
doubt('Notations, C alphabet',r'\unsure{\mathcal C|\mathscr C|C}',r'\mathcal C','resolved','The upper terminal has a distinct inward curl; the terminal C was also checked in the upper half.',8)
doubt('Notations, alleged struck underlying comparison',r'\deleted{\unsure{\leq|\prec}}',r'\unsure{\preceq|\leqslant|\deleted{\preceq}}','revised','Only one retraced symbol-sized group is separable; no independent underlying complete sign is established.',7)
doubt('Notations, final third comparison',r'\unsure{\preceq|\leqslant}',r'\unsure{\preceq|\leqslant|\deleted{\preceq}}','revised','Bowed lower strokes support preceq but dense retracing leaves both the sign and cancellation state open.',7)
doubt('Note below C',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','The raised short mark might be an acute or an i point.',8)
doubt('Note below relation, crossed word',r'\deleted{\unsure{pourtant}}',r'\deleted{\unsure{pourtant}}','retained','Initial p and a tall medial stem survive; the last part is crossed.',9)
doubt('Note below relation, following mark',r'\unsure{à}',r'\unsure{à}','retained','The mark is reduced to a low dark point and a short raised oblique stroke; the a body is not secure.',9)
doubt('C4 bis, deleted right-hand expression',r'\deleted{\unsure{\exists F|\mathcal F}}',r'\deleted{\unsure{\exists F|\exists\mathcal F}}','revised','Two groups are visible, so the alternate reading also retains the quantifier; the alphabet of F remains open.',10)
doubt('C4 bis, underlying letter before i',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','The heavy final F overlies parallel stems; the underlayer cannot be read independently.',11)
doubt('C4 bis, relation before I',r'\unsure{\vdash|\in}',r'\vdash','resolved','The mark has one upright and one rightward bar, with no visible curved arms.',11)
doubt('Lower heading, first word',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','The raised mark still does not decide between the two written spellings.',12)
doubt('Lower heading, second word',r'\unsure{résiduelle|réssiduelle}','résiduelle','resolved','Only one s-shaped group occurs between e and i.',12)
doubt('Bottom, first deletion',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}','retained','Heavy diagonal strokes obscure the indexed initial and the middle; the final family F is more visible.',13)
doubt('Bottom, cancelled abbreviation',r'\unsure{Cosupp.}','Cosupp.','resolved','Co, two p descenders, and the point survive the crossing.',14)
doubt('Bottom, ending after soit',r'\unsure{disjointe|disjoint}',r'\unsure{disjointe|disjoint}','retained','The last small return may be e or the t terminal.',15)
doubt('Bottom, last cancellation',r'\unsure{Posons|Poser}','Posons','resolved','The two o groups and final ns wave survive.',16)
doubt('Notations, plain F and G forms',r'\pi_0(F),\pi_0(G)',r'\pi_0(F),\pi_0(G)','resolved','The straight-armed F and open G with downward foot were checked in the upper half and arrow crop.',3)
doubt('Notations and C4 bis, family alphabet',r'\mathcal F,\mathcal F_i',r'\mathcal F,\mathcal F_i','resolved','Curled top and foot occur in the notation argument and product.',10)
doubt('C4 bis and bottom, indices, restriction and Phi',r'F_i,\;F\mid M_i,\;\Phi',r'F_i,\;F\mid M_i,\;\Phi','resolved','The i marks are dotted without j descenders; the restriction is a separate vertical; Phi is an oval across an upright.',bbox=[285,315,1655,930],img=b)
doubt('Lemma and bottom, abbreviations','f et s; f et s.','f et s; f et s.','resolved','The abbreviated letters, including the lower occurrence point, are written rather than the expanded phrase.',15)
doubt('Notations, closing parenthesis for Attention paragraph','opening parenthesis with no visible closer','opening parenthesis retained without a closing parenthesis','retained','No closing stroke follows the quote period or the final tuple sentence.',bbox=[915,738,1583,1157])

inventory=[]
def inv(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('I01','text','top centre','65')
inv('I02','text','top line','Ceci résulte du ... cor. 1 et du')
inv('I03','deletion','top line, between du and cor. 1',r'\uline{C}4 et')
inv('I04','text','upper left, lemma heading','Lemme, underlined')
inv('I05','text','upper three text lines','Pour que F soit de t. f. ...')
inv('I06','insertion','raised above t. f., upper right','(resp. fini)')
inv('I07','text','upper-middle block, Notations and NB lines',r'Notations \pi_0(F) (NB Si F\leq G ...')
inv('I08','deletion','end of the arrow formula, before its comma',r'\unsure{)|?}')
inv('I09','deletion','above the first surviving ! exponent',r'\unsure{\mathrm{cat}|\mathrm{act}}')
inv('I10','text','middle, three lines beginning Attention','(Attention, le ... en tenant compte du Sup. Si')
inv('I11','text','middle, tuple and final prose clause',r'\mathcal C=(\mathcal F,\leq,...) , on pose aussi ...')
inv('I12','deletion','third slot of tuple; cancellation uncertain',r'\unsure{\preceq|\leqslant|\deleted{\preceq}}')
inv('I13','margin note','below left C in tuple',r'\unsure{Contrée|Contrie}')
inv('I14','drawing','between left C and its lower note','short slanted connector without arrowhead')
inv('I15','margin note','below third tuple relation, three lines','qui ne sert / pourtant à / rien ici')
inv('I16','deletion','second line of the lower relation note',r'\unsure{pourtant}')
inv('I17','drawing','between third relation and lower note','vertical pointer with curved cap')
inv('I18','text','below tuple annotations','Axiome renforcé, not underlined')
inv('I19','text','left of C4 statement','C4 bis, double underlined')
inv('I20','text','two lines of C4 bis','Pour tout ... telle que ... pour i ... I,')
inv('I21','deletion','right end of first C4 line',r'\unsure{\exists F|\exists\mathcal F}')
inv('I22','deletion','beneath the overwritten final F in restriction equality',r'\unsure{\mathcal F}')
inv('I23','text','lower heading, left','Contrée résiduelle, underlined')
inv('I24','text','lower heading, right','Support et cosupport, three underline strokes')
inv('I25','text','bottom paragraph','Soit ... Posons')
inv('I26','deletion','bottom paragraph, immediately after first Soit',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}')
inv('I27','insertion','above end of figures, with sloping insertion guide',r'H_i')
inv('I28','deletion','after figures and its insertion','On posera')
inv('I29','deletion','between Pour and que',r'Cosupp. \Phi')
inv('I30','deletion','bottom line, before live Posons','Posons')

remaining=[
 dict(location='After pi zero of G',reading=r'\deleted{\unsure{)|?}}',alternatives=[')', '?'],confidence='low',reason='Crossed loop; the initial sign is not separable.'),
 dict(location='First deleted exponent',reading=r'\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}',alternatives=['cat','act'],confidence='low',reason='The strike masks the order of the first two small looped letters.'),
 dict(location='Attention',reading=r'\unsure{Attention}',alternatives=[],confidence='medium',reason='The beginning and tall strokes are clear but the middle is reduced to a low line.'),
 dict(location='Second superscript',reading=r'\unsure{d|!}',alternatives=['d','!'],confidence='low',reason='Upper loop plus upright and low detached mark; overwrite history is unsettled.'),
 dict(location='Third relation in tuple',reading=r'\unsure{\preceq|\leqslant|\deleted{\preceq}}',alternatives=[r'\preceq',r'\leqslant',r'\deleted{\preceq}'],confidence='low',reason='One dense retraced group; neither a separate under-sign nor cancellation state is securely recoverable.'),
 dict(location='Note below C',reading=r'\unsure{Contrée|Contrie}',alternatives=['Contrée','Contrie'],confidence='medium',reason='Raised small mark can be acute or i point.'),
 dict(location='Crossed word in note below relation',reading=r'\deleted{\unsure{pourtant}}',alternatives=[],confidence='low',reason='Initial p and later tall stem survive, but the ending lies under crossing.'),
 dict(location='Mark after crossed word in relation note',reading=r'\unsure{à}',alternatives=[],confidence='low',reason='A low point and raised stroke do not securely show the body of a.'),
 dict(location='C4 bis cancelled right-hand expression',reading=r'\deleted{\unsure{\exists F|\exists\mathcal F}}',alternatives=[r'\exists F',r'\exists\mathcal F'],confidence='low',reason='Two groups are visible; the second glyph alphabet remains unclear under crossing.'),
 dict(location='C4 bis overwritten F underlayer',reading=r'\deleted{\unsure{\mathcal F}}F_i',alternatives=[],confidence='low',reason='Parallel stems survive but the underlying letter cannot be independently traced.'),
 dict(location='Lower heading first word',reading=r'\unsure{Contrée|Contrie}',alternatives=['Contrée','Contrie'],confidence='medium',reason='Same local accent-versus-point problem as the lower note.'),
 dict(location='Bottom initial cancelled family',reading=r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',alternatives=[r'(F_i)\in\mathcal F',r'(H_i)\in\mathcal F'],confidence='low',reason='The initial indexed letter and middle expression are largely covered by diagonal crossing.'),
 dict(location='Bottom disjointe ending',reading=r'\unsure{disjointe|disjoint}',alternatives=['disjointe','disjoint'],confidence='medium',reason='The small final return may be a reduced e or part of the t.'),
]
notation=[
 dict(sign='individual figure',latex=r'F,F_i,G',appearance='Straight F upper and middle arms; open G with low turned foot.',location='lemma, arrows and restriction',alternatives=[]),
 dict(sign='family',latex=r'\mathcal F,\mathcal F_i',appearance='Looped or slanted upper arm and bent lower foot.',location='Notations, C4 product and bottom subset',alternatives=[]),
 dict(sign='ambient set',latex='M,M_i',appearance='Plain paired peaked strokes with a lower hooked start.',location='pi zero of M and restriction',alternatives=[]),
 dict(sign='contrée symbol',latex=r'\mathcal C',appearance='Large open circular body with the top turning inward.',location='tuple and terminal pi zero',alternatives=[]),
 dict(sign='first superscript',latex='!',appearance='Separate upright and lower point, beneath cancelled letters.',location='first family pi zero',alternatives=[]),
 dict(sign='second superscript',latex=r'\unsure{d|!}',appearance='Loop at the side of a thick upright with a low detached mark.',location='Attention phrase',alternatives=['d','!']),
 dict(sign='third tuple relation',latex=r'\unsure{\preceq|\leqslant|\deleted{\preceq}}',appearance='Single group with one rising upper arm and several bowed retracings.',location='third tuple slot',alternatives=[r'\preceq',r'\leqslant',r'\deleted{\preceq}']),
 dict(sign='terminal C4 relation',latex=r'\vdash',appearance='Straight upright and one bar extending right; no visible curved arms.',location='C4 bis, between i and I',alternatives=[]),
 dict(sign='empty set',latex=r'\varnothing',appearance='Small oval crossed by a long rising slash.',location='lemma ending',alternatives=[]),
 dict(sign='subset and Phi',latex=r'\Phi\subset\mathcal F',appearance='Oval across upright, open inclusion curve, cursive family F.',location='bottom paragraph',alternatives=[]),
 dict(sign='indices',latex='i',appearance='Small short lower stroke with detached dot, without a j descender.',location='all indexed formulae',alternatives=[]),
]
abbreviations=[dict(form=x,expansion=y) for x,y in [('cor.','corollaire'),('t. f.','type fini'),('resp.','respectivement'),('f et s','faut et suffit'),('f et s.','faut et suffit'),('nb','nombre'),('NB','nota bene'),('ens.','ensemble'),('Cosupp.','cosupport')]]
evidence=[
'01: Entire raised (resp. fini) inspected; final i, no additional e. Following main-line il has a visible point. The long stroke beneath the insertion joins the l flourish.',
'02: nb is n plus tall reduced b; the last verb has no separate i point and reads sont. Slashed empty-set oval and final point are visible.',
'03: Arrow has a full right head. One crossed looped sign precedes the comma after pi zero of G; its original identity remains unsure.',
'04: Cancelled cat/act is vertically above a clear !. Family F has a looped upper arm. The deleted letters remain unsure.',
'05: Attention remains tentative in its compressed middle. Second exponent has a d-like loop on an upright and a separate low mark; d/! retained.',
'06: du and Sup resolved; two opening and two closing quote strokes bracket the whole phrase. A period is followed by Si without a closing parenthesis.',
'07: Third relation is one heavily retraced symbol-sized group; sign and cancellation state retained locally, without asserting two separately readable complete symbols.',
'08: C has a clear inward top return. Contrée/Contrie and its straight subline pointer inspected; accent/point remains open.',
'09: Three-line note reads qui ne sert / crossed tentative pourtant plus tentative à / rien ici. Vertical pointer has a curved cap. No rotation needed.',
'10: Product family F and both indices inspected. Cancellation contains two vertical groups, best quantifier plus F, with F alphabet left open.',
'11: Restriction uses plain M. Final F is overdrawn, underlayer unsure. Relation before I visibly upright plus single right bar; read literal turnstile. Terminal mark descends like a comma.',
'12: One s group in résiduelle; Contrée/Contrie retained. The right heading reads cosupport and shows separate underlines for Support, et and cosupport.',
'13: Initial deleted family remains tentative. H_i is above the end of figures; diagonal insertion guide meets the line before its punctuation.',
'14: Deleted Cosupp. Phi resolved through two p descenders and separate abbreviation point. On posera remains a separate cancelled phrase.',
'15: disjointe/disjoint remains open at the t terminal; written f et s. is visibly abbreviated.',
'16: Parenthesis reads à cause de C3. Cancelled Posons is recoverable and separate from the following live Posons.'
]
finished=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
report=dict(reader='R3',cote='156-4',scan='66',brief_version='v02',started_utc='2026-11-20T09:24:15Z',finished_utc=finished,image_views=[source,a,b],reading_file=str(out/'reading.tex'),differences=diffs,c_doubts=cd,inventory=inventory,remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,notes=dict(summary='Complete independent reading of the one assigned handwritten page. All main lines, annotations, insertions and cancellations were checked against both drafts using the prescribed three image views and sixteen own open-place crops. No other reader, scan, OCR or outside source was used.',math_reading_decisions='No theorem was proved or independently validated. The mismatch between the membership expected from the phrase and the visible upright-plus-bar in i [relation] I triggered close inspection; literal ink gives a turnstile. The overloaded tuple sign triggered a separation of symbol shape from cancellation state; it remains one uncertain retraced group. The superscripts were read from loops, uprights and detached points without selecting a meaning from the mathematics.',author_checks='The page names cor. 1, a lemma, a reinforced C4 bis, and C3. These are authorial references/assertions only, not recorded as proofs checked in this run.',title_dates_pagination='Manuscript page number 65 appears at top centre; scan number is 66. Internal headings are Lemme, Notations, Axiome renforcé, C4 bis, and Contrée/Contrie résiduelle, Support et cosupport. No date, separate title sheet, or archive pencil number is visible. The Attention parenthesis has no visible closing parenthesis.'),check_events=[],crops=crops,workflow_feedback=['The brief permits ordinary insertion macros to represent ordinary strokes but requires distinct connectors in TikZ. This page has both: the simple H_i insertion guide is treated as ordinary insertion, while the two note pointers are drawn explicitly. A clearer rule for this boundary would improve consistency.','The one-crop limit preserves independent judgement, but retraced mathematical signs can leave cancellation history undecidable; the report therefore records one group with local state alternatives rather than multiplying unread symbols.'])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
log=(out/'inspection_log.md').read_text().replace('Pending one inspection.','Viewed once in the sequence recorded below.')
log+='\n## Crop views in exact order\n\n'
for k,m in enumerate(crops,4):
    log+=f"{k}. {m['path']} — one view. {evidence[k-4]}\n"
log+='\nNo full page or half was displayed a second time. No decided place was recropped; no rotations were necessary. No OCR, text-recognition or outside research was run.\n'
log+=f'\nFinished UTC: {finished}\n'
(out/'inspection_log.md').write_text(log)
print(json.dumps(dict(differences=len(diffs),c_doubts=len(cd),inventory=len(inventory),remaining_doubts=len(remaining),crops=len(crops),finished_utc=finished),indent=2))
