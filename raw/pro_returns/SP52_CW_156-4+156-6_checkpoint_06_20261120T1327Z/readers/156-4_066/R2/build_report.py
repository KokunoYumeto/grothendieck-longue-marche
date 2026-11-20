from pathlib import Path
from datetime import datetime, timezone
import json
p=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R2')
root='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/'
w=root+'J156-4-09_156-4_scan066.jpg'; a=w.replace('.jpg','_a.jpg'); b=w.replace('.jpg','_b.jpg')
crops=json.loads((p/'crops_manifest.json').read_text())
D=[]
def diff(loc,c,h,r,shows,kind='other',confidence='high',n=None,bbox=None,img=None,mc=False,cc=False,ch=True,mh='no'):
 z=crops[n-1] if n else None
 D.append(dict(id=f'R2-D{len(D)+1:02}',location=loc,c=c,h=h,reading=r,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=mh,change_c=cc,change_h=ch,crop=z['path'] if z else None,bbox=z['bbox'] if z else bbox,bbox_image=z['source'] if z else img,source=z['source'] if z else img,math_consequential=mc))
diff('Opening, résulte du',r'du',r'de',r'du','The second letter after d is a low joined u.', 'misread word',bbox=[710,91,795,133],img=a)
diff('Opening cancellation, underline under C',r'\deleted{\uline{C}4 et}',r'\struck{C4 et}',r'\deleted{\uline{C}4 et}','A separate short underline survives below C, beneath the long cancellation.',bbox=[802,75,1022,147],img=a)
diff('Lemma, raised parenthesis',r'\inserted{(resp. \unsure{fini|finie})}',r'(resp. fini)',r'\inserted{(resp. fini)}','The whole parenthesis is raised; the final i has a separate short stroke and dot, with no additional e before the closing parenthesis.','insertion or placement',n=1,cc=True)
diff('Lemma, il',r'Il',r'il',r'il','A separate dot accompanies the short initial i; the tall stem belongs to l.','other',n=1,cc=True,ch=False)
diff('Lemma, abbreviation',r'f et s',r'il faut et il suffit',r'f et s','One long f and one short s are written around et; the expanded words are absent.','abbreviation expanded or spelling modernised',bbox=[240,290,467,389],img=a)
diff('Lemma b), capital Tous',r'Tous',r'tous',r'Tous','The initial T is a tall capital with a separate top bar.','other',bbox=[375,390,489,455],img=a)
diff('Lemma b), nb',r'\unsure{nb}',r'nb',r'nb','The low n is followed by the ascending stem and lower turn of b; no point follows.','other',n=2,cc=True,ch=False)
diff('Lemma b), sont',r'sont',r'soient',r'sont','Only the short s group and low joined ont group occur, without the dotted i seen in soient on the line above.','misread word',n=2)
diff('Notations heading, underline state',r'Notations',r'\emph{Notations}',r'Notations','There is no underline below this heading.',bbox=[297,541,572,630],img=a)
diff('Notations, NB Si',r'NB Si',r'NB si',r'NB Si','The S is a large, heavily retraced capital; the i is short and dotted.','other',bbox=[944,531,1150,602],img=a)
diff('Notations, mark after pi-zero(G)',r'\deleted{\unsure{)|?}}',r'\ill{}',r'\deleted{\unsure{)}}','A curved mark is crossed by diagonal strokes. A cancelled closing parenthesis remains the best reading; no separate question-mark point is discernible.','readable ink left as \\ill{}','low',n=3,cc=True,mh='yes')
diff('Notations, punctuation after transitivité)',r'transitivité)',r'transitivité),',r'transitivité)','The closing parenthesis is visible at the right; there is no following comma before the next line.','text not on the page',bbox=[988,621,1420,729],img=a)
diff('Notations, ambient M',r'\pi_0(M)',r'\pi_0(\mathcal{M})',r'\pi_0(M)','M is a simple peaked capital with no calligraphic loop.','misread symbol or index',bbox=[280,777,514,853],img=a)
diff('Notations, first family and superscript',r'\pi_0^{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}!}(\mathcal F)',r'\pi_0^{\cdot}(\mathfrak{F})',r'\pi_0^{\deleted{\unsure{\mathrm{cat}|\mathrm{act}}}!}(\unsure{.}\mathcal F)','A live upright and separate point make !; a crossed three-letter group sits above it. F has the looped top and curved foot of the family alphabet, not Gothic. A further isolated low point appears just inside the left parenthesis.','misread symbol or index','medium',n=4,mc=True,cc=True,mh='yes')
diff('Notations, Attention certainty',r'\unsure{Attention}',r'Attention',r'\unsure{Attention}','The initial A and tall t strokes are clear; the middle and ending compress into short waves, so full lettering remains uncertain.','other','medium',n=5)
diff('Notations, second pi-zero family and superscript',r'\pi_0^{\unsure{d|!}}(\mathcal F)',r'\pi_0^{\cdot}(\mathfrak{F})',r'\pi_0^{\unsure{\underset{\circ}{d}|!}}(\mathcal F)','The upper component is d-shaped, with a closed left loop against an upright. A detached small hollow ring lies beneath it. The family F is looped, not Gothic. The exponent is preserved as a compound uncertain appearance.','misread symbol or index','low',n=5,mc=True,cc=True,mh='yes')
diff('Notations, pi-zero(F,leq)',r'\pi_0(F,\leq)',r'\pi_0(\mathfrak{F},\leq)',r'\pi_0(F,\leq)','The F has a straight stem and two straight rightward arms, unlike the looped family letters.','misread symbol or index',n=6,mc=True)
diff('Notations, quotation punctuation',r'``en tenant compte \unsure{du|des} \unsure{Sup}''',r'\ill{} en tenant compte des « Sup »',r'``en tenant compte \unsure{du|des} Sup''','Double quotation strokes surround the entire phrase. No guillemets surround Sup. The opening strokes are visible in the upper half, and the closing pair and period in crop 06.','other',n=6,cc=True,mh='yes')
diff('Notations, du/des',r'\unsure{du|des}',r'des',r'\unsure{du|des}','The word begins with a loop and ascender of d, followed by a low joined ending; du is preferred, but the compressed ending does not exclude des.','misread word','medium',n=6)
diff('Notations, Sup certainty',r'\unsure{Sup}',r'Sup',r'Sup','S is tall, u is low, and p has a distinct downstroke and return.','other',n=6,cc=True,ch=False)
diff('Notations, outer parenthesis after quotation',r"Sup''. Si",r'Sup ».) Si',r"Sup''. Si",'The closing quotation pair and separate full stop are followed by Si. No closing parenthesis for Attention is written here or after pi-zero(C).','text not on the page',n=6)
diff('Notations, C alphabet certainty',r'\unsure{\mathcal C|\mathscr C|C}',r'\mathcal C',r'\unsure{\mathcal C|\mathscr C|C}','The top returns inward in a broad curl. Calligraphic C is preferred; the manuscript does not decisively separate the font alternatives.','misread symbol or index','medium',n=7)
diff('Notations tuple, family alphabet',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The family letter has a sloping top and curved stem/foot, with no Gothic structure.','misread symbol or index',n=7)
diff('Notations tuple, third relation and overwrite',r'\deleted{\unsure{\leq|\prec}}\unsure{\preceq|\leqslant}',r'\ldots',r'\deleted{\unsure{\leq|\prec}}\unsure{\preceq|\leqslant}','One heavily overwritten group contains a curved upper comparison and several lower returns. The old and final forms cannot be separated securely; they are not two spatially separate signs.','misread symbol or index','low',n=8,mc=True,mh='yes')
diff('Below tuple, Contrée gloss certainty',r'\margin{\unsure{Contrée|Contrie}}',r'contrée',r'\unsure{Contrée|Contrie}','A small separate raised mark precedes the last e. It may be an acute accent or the dot of a reduced i.','other','medium',n=7)
diff('Below tuple, right gloss',r'\margin{qui ne sert \deleted{\unsure{pourtant}} \unsure{à} rien ici}',r'\ill{} vues ici',r'qui ne sert \deleted{\unsure{pourtant}} \unsure{à} rien ici','Three lines read qui ne sert / [crossed word] [tiny marked letter] / rien ici. The p and tall t of the crossed word are visible; pourtant and à remain uncertain.','readable ink left as \\ill{}','medium',n=8,mh='yes')
diff('Below tuple, two drawn pointers',r'\margin{...}\margin{...}',r'\note{...}',r'\figure{\begin{tikzpicture}...\end{tikzpicture}}','A short slanted plain stroke connects the left C to its gloss. A vertical stroke with a curved cap connects the third relation to the right gloss; both are reproduced.','drawing or diagram',n=8,cc=True)
diff('Notations, closing clause',r'on pose aussi',r'on peut aussi écrire',r'on pose aussi','After on, the next group begins with a descending p and has the compressed ose ending. There is no separate écrire group.','misread word',bbox=[821,1065,1568,1155],img=a)
diff('Axiome renforcé, lettering and underline state',r'Axiome renforcé',r'\emph{Axiome \uncertain{renforcé}}',r'Axiome renforcé','The heading is live and has no underline. The tall f and final raised accent are visible.','other',bbox=[415,206,1065,315],img=b,mh='yes')
diff('C4 bis, double underline',r'\uuline{C4 bis}',r'\emph{C4 bis}',r'\uuline{C4 bis}','Two low strokes cross and converge beneath C4 bis.','other',bbox=[268,370,516,476],img=b)
diff('C4 bis, product family alphabet',r'\prod\mathcal F_i',r'\prod\mathfrak F_i',r'\prod\mathcal F_i','The letter after the product has a bent upper arm and curved lower stem.','misread symbol or index',bbox=[1195,298,1402,417],img=b)
diff('C4 bis, cancelled right group',r'\deleted{\unsure{\exists F|\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\exists\unsure{\mathcal F|F}}','Two distinct vertical groups survive cancellation. The left has three leftward bars of exists; the right has an upper loop and curved foot, favouring a family F over plain F.','misread symbol or index','medium',n=9,cc=True,mh='yes')
diff('C4 bis, family after exists F in',r'\mathcal F',r'\mathfrak F',r'\mathcal F','The family letter has an oblique upper bar and curved foot.','misread symbol or index',bbox=[285,474,559,572],img=b)
diff('C4 bis, ambient restriction M_i',r'F\mid M_i',r'F|\mathcal M_i',r'F\mid M_i','The restriction stroke is vertical and M is a simple peaked capital.','misread symbol or index',bbox=[1020,444,1206,524],img=b)
diff('C4 bis, overwritten final F_i',r'\deleted{\unsure{\mathcal F}}F_i',r'F_i',r'\deleted{\unsure{\mathcal F|F}}F_i','The live F has retraced parallel stem and middle bars. An underlying family F is possible, but plain F retracing also remains possible; the old glyph occupies the same place.','deletion state (struck given live or live given struck)','low',n=10,cc=True)
diff('C4 bis, final relation',r'i\unsure{\vdash|\in}I',r'i\in I',r'i\vdash I','The mark consists of one tall vertical and one short rightward tick. It has no upper/lower arms like the membership signs earlier on this page.','misread symbol or index',n=11,cc=True,mc=True)
diff('Lower heading, Contrée certainty',r'\unsure{Contrée|Contrie}',r'Contrée',r'\unsure{Contrée|Contrie}','After tr a short curved letter and a tiny raised mark precede final e. Accent versus dotted i remains unsettled.','other','medium',n=12)
diff('Lower heading, résiduelle certainty',r'\unsure{résiduelle|réssiduelle}',r'résiduelle',r'résiduelle','There is one s-shaped curve between the accented first group and dotted i, followed by d and the two l loops.','other',n=12,cc=True,ch=False)
diff('Lower heading, Support et cosupport',r'\uline{Support} \uline{et} \uline{cosupport}',r'\emph{Support et complément}',r'\uline{Support} \uline{et} \uline{cosupport}','The last word has initial co and two long p descenders. Support, et, and cosupport have separate underline strokes.','misread word',bbox=[993,650,1634,771],img=b)
diff('Bottom, cancelled family',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}',r'\struck{\ill{}}',r'\deleted{\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}}','A left parenthesis, a stemmed indexed letter, a comparison/membership-like group, and a final family letter survive dense zigzag cancellation. F_i is preferred, but H_i remains possible.','readable ink left as \\ill{}','low',n=13,mh='yes')
diff('Bottom, live Phi subset family alphabet',r'\Phi\subset\mathcal F',r'\Phi\subset\mathfrak F',r'\Phi\subset\mathcal F','The live family letter is looped and curved, not Gothic. Phi has an oval across its vertical.','misread symbol or index',bbox=[905,792,1137,862],img=b)
diff('Bottom, H_i insertion placement and connector',r'figures \inserted{$H_i$}',r'\Phi\subset\mathfrak F \add{$H_i$} un ens. de figures',r'figures\inserted{$H_i$}.','H_i is raised over the end of figures. A long slanted connector reaches the place just before the period after figures; the mark is reproduced in TikZ.','insertion or placement',n=13,cc=True)
diff('Bottom, cancelled Cosupp.',r'\deleted{\unsure{Cosupp.} $\Phi$}',r'\struck{Compl.\ $\Phi$}',r'\deleted{Cosupp. $\Phi$}','The cancelled word has initial Co, low su, and two long p descenders followed by a separate point.','misread word',n=14,cc=True)
diff('Bottom, disjointe certainty',r'\unsure{disjointe|disjoint}',r'disjointe',r'\unsure{disjointe|disjoint}','The terminal t continues rightward into a short downward hook. It can contain the final e, but the e is not independently formed.','other','medium',n=15)
diff('Bottom, f et s. abbreviation',r'il f et s.',r'il faut et il suffit',r'il f et s.','The manuscript has a long f, et, and a short s with a separate point.','abbreviation expanded or spelling modernised',bbox=[866,1031,1180,1132],img=b)
diff('Bottom, strates certainty',r'strates',r'strates',r'\unsure{strates}','The apparent a is reduced to a tiny separate mark between the r group and the next tall t. The word is likely strates, but full lettering is not secure.','other','medium',n=16,cc=True,ch=True)
diff('Bottom, parenthetical reason',r'(à cause de C3)',r'(cf. conséquence de C3)',r'(à cause de C3)','The first small marked letter is à; the following group reads cause. No cf. or conséquence group occurs.','misread word',bbox=[321,1180,992,1240],img=b)
diff('Bottom, cancelled Posons',r'\deleted{\unsure{Posons|Poser}}',r'\struck{Posons}',r'\deleted{Posons}','P is followed by the os curves, a small o loop, and the low ns ending; the strike does not conceal a final r.','other',n=16,cc=True,ch=False)

CD=[]
def doubt(loc,c,r,status,shows,n=None,bbox=None,img=None):
 z=crops[n-1] if n else None
 CD.append(dict(location=loc,c=c,reading=r,status=status,scan_shows=shows,crop=z['path'] if z else None,bbox=z['bbox'] if z else bbox,bbox_image=z['source'] if z else img,source=z['source'] if z else img))
doubt('Notations, small zero and plain F/G',r'\pi_0(F),\pi_0(G)',r'\pi_0(F),\pi_0(G)','resolved','Small low ovals are subscripts; F has straight arms and G has the downturned lower return.',3)
doubt('Notations and C4 bis, family alphabet',r'\mathcal F,\mathcal F_i',r'\mathcal F,\mathcal F_i','resolved','Looped or bent upper stroke and curved lower stem recur locally.',4)
doubt('Notations, C alphabet',r'\unsure{\mathcal C|\mathscr C|C}',r'\unsure{\mathcal C|\mathscr C|C}','retained','Broad inward curl favours calligraphic C, without decisively separating font alternatives.',7)
doubt('Notations, both upper marks',r'\pi_0^{!};\pi_0^{\unsure{d|!}}',r'\pi_0^{!};\pi_0^{\unsure{\underset{\circ}{d}|!}}','revised','The first ! is clear. The second has a d-shaped upper component with a detached hollow ring beneath.',5)
doubt('Notations, quotation strokes',r"``en tenant compte du Sup''",r"``en tenant compte \unsure{du|des} Sup''",'resolved','The closing two strokes are distinct; the upper half supplies the opening double strokes.',6)
doubt('C4 bis and bottom, i/restriction/Phi',r'F_i;F\mid M_i;\Phi',r'F_i;F\mid M_i;\Phi','resolved','The i letters are dotted with short stems; the restriction is a vertical bar; Phi has an oval crossing its stem.',bbox=[905,790,1139,863],img=b)
doubt('Lemma and bottom, f et s',r'f et s;f et s.',r'f et s;f et s.','resolved','Both have an isolated descending f and short s; the bottom has a point after s.',bbox=[866,1031,1180,1132],img=b)
doubt('Tuple, final comparison',r'\unsure{\preceq|\leqslant}',r'\unsure{\preceq|\leqslant}','retained','Several curved returns overlap beneath a curved upper comparison.',8)
doubt('Lemma, raised fini/finie',r'\unsure{fini|finie}',r'fini','resolved','The ending is a short i stroke and separate dot, followed by the parenthesis; no e is visible.',1)
doubt('Lemma b), nb',r'\unsure{nb}',r'nb','resolved','Low n and ascending b are distinguishable.',2)
doubt('Notations, cancelled mark after pi-zero(G)',r'\unsure{)|?}',r'\unsure{)}','revised','Crossed curved stroke supports a parenthesis; a question mark point is not visible.',3)
doubt('Notations, deleted upper letters',r'\unsure{\mathrm{cat}|\mathrm{act}}',r'\unsure{\mathrm{cat}|\mathrm{act}}','retained','The last t is distinguishable; cancellation prevents a secure order for the first two small forms.',4)
doubt('Notations, Attention',r'\unsure{Attention}',r'\unsure{Attention}','retained','A and tall t strokes survive clearly, but the other letters are compressed.',5)
doubt('Notations, second exponent',r'\unsure{d|!}',r'\unsure{\underset{\circ}{d}|!}','revised','Loop against an upright makes a d-like top; a detached ring must also be represented.',5)
doubt('Notations, Sup',r'\unsure{Sup}',r'Sup','resolved','Tall S, low u and descending p are distinguishable.',6)
doubt('Tuple, initial C',r'\unsure{\mathcal C|\mathscr C|C}',r'\unsure{\mathcal C|\mathscr C|C}','retained','Font classification is not fully decided by the broad curl.',7)
doubt('Tuple, overwritten older relation',r'\unsure{\leq|\prec}',r'\unsure{\leq|\prec}','retained','Old and newer strokes share one footprint; no clean original outline remains.',8)
doubt('Below tuple, Contrée/Contrie',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','Tiny raised mark is not decisively an accent or an i dot.',7)
doubt('Below tuple, cancelled pourtant',r'\deleted{\unsure{pourtant}}',r'\deleted{\unsure{pourtant}}','retained','Initial p, low middle and t stem survive, but the final section is crossed.',8)
doubt('Below tuple, à',r'\unsure{à}',r'\unsure{à}','retained','Two tiny separated strokes occupy the expected word position; the lower body is not securely letter-shaped.',8)
doubt('C4 bis, cancelled right group',r'\unsure{\exists F|\mathcal F}',r'\exists\unsure{\mathcal F|F}','revised','There are two glyph-sized groups, left exists and right a looped F-like capital.',9)
doubt('C4 bis, old glyph under F_i',r'\unsure{\mathcal F}',r'\unsure{\mathcal F|F}','revised','Multiple parallel stems and arms prove retracing but not the old alphabet.',10)
doubt('C4 bis, relation before I',r'\unsure{\vdash|\in}',r'\vdash','resolved','One vertical plus one rightward tick, without the bowl or extra arms of membership.',11)
doubt('Bottom, cancelled family',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}','retained','Parenthesis, indexed capital, middle relation and final family survive under dense cancellation; first capital remains uncertain.',13)
doubt('Bottom, cancelled Cosupp.',r'\unsure{Cosupp.}',r'Cosupp.','resolved','Two p descenders and the final point distinguish this from Compl.',14)
doubt('Bottom, cancelled final word',r'\unsure{Posons|Poser}',r'Posons','resolved','Small o loop and low ns ending remain beneath the horizontal strike.',16)
doubt('Notations quotation, article',r'\unsure{du|des}',r'\unsure{du|des}','retained','Joined low ending is compatible with du and does not exclude compressed des.',6)
doubt('Lower heading, résiduelle',r'\unsure{résiduelle|réssiduelle}',r'résiduelle','resolved','One s-shaped curve appears before dotted i, not two.',12)
doubt('Bottom, disjointe/disjoint',r'\unsure{disjointe|disjoint}',r'\unsure{disjointe|disjoint}','retained','A short terminal downward hook may include e but is not independent of the t.',15)
doubt('Tuple, repeated comparison doubt in C context',r'\unsure{\preceq|\leqslant}',r'\unsure{\preceq|\leqslant}','retained','Same single overwritten locus as above; not inspected twice.',8)
doubt('Lower heading, Contrée/Contrie',r'\unsure{Contrée|Contrie}',r'\unsure{Contrée|Contrie}','retained','Raised mark near the compressed vowel remains ambiguous.',12)
doubt('Notations, missing closing Attention parenthesis',r'(Attention ... Si ... \pi_0(\mathcal C).',r'(\unsure{Attention} ... Si ... \pi_0(\mathcal C).','resolved','No final closing parenthesis follows the quotation period or the final formula period.',bbox=[1290,1038,1571,1140],img=a)

INV=[]
def inv(e,k,pos,first): INV.append(dict(element=e,kind=k,position=pos,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('Manuscript page number','text','top centre','65')
inv('Opening sentence','text','top line','Ceci résulte du')
inv('Cancelled opening reference','deletion','top line after du',r'\uline{C}4 et')
inv('Lemma heading and statement','text','upper page, lines 2–4','Lemme Pour que F')
inv('Raised alternative','insertion','above t. f.',r'(resp. fini)')
inv('Notations paragraph','text','middle upper page','Notations pi-zero(F)')
inv('Cancelled premature parenthesis','deletion','after pi-zero(G)',r'\unsure{)}')
inv('Cancelled exponent letters','deletion','above first pi-zero family',r'\unsure{cat|act}')
inv('Tuple overwrite','deletion','third tuple slot',r'\unsure{\leq|\prec}')
inv('Left tuple gloss','margin note','below tuple C',r'\unsure{Contrée|Contrie}')
inv('Right tuple gloss','margin note','below third tuple slot','qui ne sert ... rien ici')
inv('Cancelled gloss word','deletion','second line of right gloss',r'\unsure{pourtant}')
inv('Tuple pointers','drawing','below C and third relation','slanted stroke; vertical stem with curved cap')
inv('Strengthened axiom heading','text','middle page','Axiome renforcé')
inv('C4 bis statement','text','below strengthened axiom heading','C4 bis Pour tout')
inv('Cancelled axiom group','deletion','right of product',r'\exists\unsure{\mathcal F|F}')
inv('Overwritten axiom F','deletion','right member of restriction equation',r'\unsure{\mathcal F|F}')
inv('Lower section heading','text','above bottom paragraph','Contrée résiduelle Support et cosupport')
inv('Bottom paragraph','text','bottom of page','Soit ... Phi subset family')
inv('Cancelled family','deletion','after Soit',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}')
inv('Raised H_i','insertion','above end of figures',r'H_i')
inv('H_i connector','drawing','beside figures and raised H_i','long slanted connecting stroke')
inv('Cancelled On posera','deletion','after figures.','On posera')
inv('Cancelled Cosupp. Phi','deletion','after Pour',r'Cosupp. \Phi')
inv('Cancelled Posons','deletion','last line','Posons')

RD=[
('Notations, crossed parenthesis',r'\unsure{)}',['cancelled closing parenthesis','indeterminate crossed curved mark'],'low','Cancellation hides part of the curve.'),
('Notations, deleted exponent',r'\unsure{\mathrm{cat}|\mathrm{act}}',[r'\mathrm{cat}',r'\mathrm{act}'],'low','Crossed small letters cannot be securely ordered.'),
('Notations, isolated low point',r'\unsure{.}',['literal point','incidental ink mark'],'low','A detached low point is visible inside the parenthesis; its intended status is unclear.'),
('Notations, Attention',r'\unsure{Attention}',['Attention'],'medium','Compressed intermediate letters.'),
('Notations, second exponent',r'\unsure{\underset{\circ}{d}|!}',[r'\underset{\circ}{d}',r'!','d written over the stem of !, retaining the lower point'],'low','A d-shaped top and detached ring are visible; the correction history is unclear.'),
('Quotation, article',r'\unsure{du|des}',['du','des'],'medium','Low joined ending admits either reading.'),
('Tuple C alphabet',r'\unsure{\mathcal C|\mathscr C|C}',[r'\mathcal C',r'\mathscr C','C'],'medium','Broad curl does not fully identify the mathematical font.'),
('Tuple old relation',r'\deleted{\unsure{\leq|\prec}}',[r'\leq',r'\prec'],'low','Old strokes cannot be separated from retracing.'),
('Tuple final relation',r'\unsure{\preceq|\leqslant}',[r'\preceq',r'\leqslant'],'low','Several bowed returns are superimposed.'),
('Below tuple, Contrée',r'\unsure{Contrée|Contrie}',['Contrée','Contrie'],'medium','Accent versus i dot remains unsettled.'),
('Below tuple, crossed word',r'\deleted{\unsure{pourtant}}',['pourtant'],'low','Final portion is obscured by cancellation.'),
('Below tuple, short marked letter',r'\unsure{à}',['à'],'low','Only two small strokes survive clearly.'),
('C4 bis, cancelled right letter',r'\exists\unsure{\mathcal F|F}',[r'\exists\mathcal F',r'\exists F'],'medium','The final capital is looped but crossed heavily.'),
('C4 bis, old F glyph',r'\deleted{\unsure{\mathcal F|F}}F_i',[r'\mathcal F','F','retracing without a changed glyph'],'low','Several parallel stems and arms overlap in one place.'),
('Lower heading, Contrée',r'\unsure{Contrée|Contrie}',['Contrée','Contrie'],'medium','Tiny raised mark and compressed vowel.'),
('Bottom, cancelled family',r'\unsure{(F_i)\in\mathcal F|(H_i)\in\mathcal F}',[r'(F_i)\in\mathcal F',r'(H_i)\in\mathcal F'],'low','Dense zigzag strike obscures the indexed capital and middle group.'),
('Bottom, disjointe',r'\unsure{disjointe|disjoint}',['disjointe','disjoint'],'medium','Terminal hook may contain e or only finish t.'),
('Bottom, strates',r'\unsure{strates}',['strates'],'medium','The a is reduced to a tiny point-like mark.'),
]
remaining=[dict(location=x[0],reading=x[1],alternatives=x[2],confidence=x[3],reason=x[4]) for x in RD]
notation=[
 dict(sign='individual figure',latex='F, F_i',appearance='Straight upper and middle arms with plain stem.',location='Lemma; plain F in pi-zero(F,leq); C4 bis and bottom',alternatives=[]),
 dict(sign='family',latex=r'\mathcal F,\mathcal F_i',appearance='Bent or looped upper arm and curved stem/foot.',location='Notations; C4 bis; bottom',alternatives=[]),
 dict(sign='ambient set',latex='M, M_i',appearance='Simple peaked capital.',location='pi-zero(M); restriction equation',alternatives=[]),
 dict(sign='first family exponent',latex='!',appearance='Separate upright and detached lower point.',location='First pi-zero family',alternatives=[]),
 dict(sign='second family exponent',latex=r'\unsure{\underset{\circ}{d}|!}',appearance='D-shaped upper component with separate hollow ring immediately below.',location='Attention parenthesis',alternatives=[r'!','overwritten !']),
 dict(sign='contrée symbol',latex=r'\unsure{\mathcal C|\mathscr C|C}',appearance='Broad C with inward-returning upper curl.',location='Tuple and final pi-zero(C)',alternatives=[r'\mathscr C','C']),
 dict(sign='third tuple comparison',latex=r'\unsure{\preceq|\leqslant}',appearance='Curved upper angle and multiple bowed lower returns, overwritten.',location='Tuple third slot',alternatives=[r'\leqslant']),
 dict(sign='literal final relation',latex=r'\vdash',appearance='Vertical stroke and short rightward tick; no membership bowl.',location='C4 bis i vdash I',alternatives=[]),
 dict(sign='empty set',latex=r'\varnothing',appearance='Small oval crossed by long diagonal.',location='Lemma end',alternatives=[]),
 dict(sign='Phi',latex=r'\Phi',appearance='Oval through upright with upper and lower bar.',location='Bottom',alternatives=[]),
 dict(sign='map arrow',latex=r'\longrightarrow',appearance='Horizontal shaft with full right arrowhead.',location='Notations pi-zero(F) to pi-zero(G)',alternatives=[]),
]
abbreviations=[dict(form=k,expansion=v) for k,v in [('cor.','corollaire'),('t. f.','type fini'),('resp.','respectivement'),('f et s','faut et suffit'),('f et s.','faut et suffit'),('nb','nombre'),('NB','nota bene'),('ens.','ensemble'),('Cosupp.','cosupport')]]
evidence=[
'Raised parenthesis reads (resp. fini), without final e. The following initial is dotted il.',
'nb is distinguishable; the last verb is sont, with no dotted i. Empty set has a diagonal slash.',
'The extra curved mark after the formula is cancelled. Best reading is ), retained uncertain.',
'Crossed cat/act remains doubtful; live ! is clear. Family F is looped. An isolated low point inside the left parenthesis is preserved uncertain.',
'Attention remains compressed. The second exponent has a d-shaped top and separate hollow ring, so a simple d loses visible material.',
'du is preferred over des, but the ending remains compressed. Sup and closing double quotation strokes with a separate period are clear; no closing parenthesis.',
'The C has an inward upper curl; its alphabet remains uncertain. The gloss Contrée/Contrie has a tiny raised mark. The slanted connector is separate.',
'One heavily overwritten comparison group remains uncertain. The note reads qui ne sert, cancelled probably pourtant, uncertain à, then rien ici. Vertical pointer and curved cap are distinct.',
'Two cancelled glyph-sized groups: exists at left and a looped F-like capital at right.',
'Final F_i has multiple superimposed stems/arms. Old family F versus plain F retracing cannot be settled.',
'The relation is visibly a turnstile shape: one vertical and one rightward tick. Transcribed literally as vdash.',
'Contrée/Contrie remains uncertain. Résiduelle contains one s-shaped curve before dotted i, not a doubled s.',
'Cancelled parenthesized indexed family remains uncertain. H_i is raised above figures, with a long slanted connector to the insertion place near its period.',
'Cancelled Cosupp. is legible: two p descenders and a point. Phi is clear.',
'Disjointe/disjoint remains uncertain because the last hook may be e or only the t ending.',
'Cancelled Posons can be read. The surrounding line reveals that the a of strates is a tiny point-like mark, so that word is retained uncertain.'
]
for z,ev in zip(crops,evidence): z['visible_evidence']=ev
report=dict(reader='R2',cote='156-4',scan='66',brief_version='v02',started_utc=(p/'started_utc.txt').read_text().strip(),finished_utc=datetime.now(timezone.utc).isoformat(),image_views=[w,a,b],reading_file=str(p/'reading.tex'),differences=D,c_doubts=CD,inventory=INV,remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,notes=dict(summary='The page continues a lemma, introduces component notation and a reinforced axiom, then begins the section on residual contrées, support and cosupport. All live text, cancellations, raised material and two sets of connectors are included.',math_reading_decisions='No theorem was proved or re-proved. The possible semantic difference between a dot, ! and d prompted close inspection of the exponents, but visible strokes control the result. Likewise, membership would be natural before I, but the ink is a turnstile shape and is transcribed literally. The tuple comparison remains uncertain rather than being repaired from expected mathematics.',author_checks='No explicit proof-check mark or verification by the author is claimed. C3 and cor. 1 are references only. No outside page or source was used.',title_dates_pagination='Manuscript page 65 at top centre; scan 66. Headings Axiome renforcé and Contrée résiduelle / Support / et / cosupport. No date visible.'),check_events=[],crops=crops,workflow_feedback=['The supplied C_context contains a scan 70 row. It was treated as outside-page draft context and not investigated; no scan 70 image or file was opened.','The instruction to include one surrounding line can make separately planned tight crops overlap. Crop coordinates and all transformations are recorded so the extent is explicit.','The prescribed macros have no direct inline mechanism for below-line connecting strokes. Two small TikZ figures preserve the pointers and the H_i connector without describing away the marks.'])
(p/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
with (p/'inspection_log.md').open('a') as f:
 for i,(z,ev) in enumerate(zip(crops,evidence),4):
  f.write(f'{i}. {z["path"]}\n   - Source: {z["source"]}; bbox {z["bbox"]}; scale {z["scale"]:.8f}; rotation {z["rotation"]} degrees.\n   - Transformations: {z["transforms"]}.\n   - Viewed once. Evidence: {ev}\n')
 f.write('\nNo whole-page or half image was viewed a second time. No OCR, outside source, other page or other reader file was used. All crops were generated before their single view; no decided locus was recropped.\n')
(p/'inventory.json').write_text(json.dumps(INV,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(D),c_doubts=len(CD),remaining_doubts=len(remaining),inventory=len(INV),crops=len(crops))))
