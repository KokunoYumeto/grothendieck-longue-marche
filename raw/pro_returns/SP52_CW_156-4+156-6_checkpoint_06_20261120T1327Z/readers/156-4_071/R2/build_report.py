from pathlib import Path
import json,datetime,re
base=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R2')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_071')
metadata=json.loads((packet/'metadata.json').read_text())
manifest=json.loads((base/'crop_manifest.json').read_text())
tex=(base/'reading.tex').read_text()
whole=metadata['images'][0]; upper=metadata['images'][1]; lower=metadata['images'][2]

def fig(name):
 start=tex.index('% '+name)
 end=tex.find('\n\n',start)
 return tex[start:end]

F_MARGIN=fig('R2-margin-marks')
F_COR=fig('R2-corollary-correction')
F_ITOU=fig('R2-itou-mark')
F_PUNCT=fig('R2-right-punctuation')
F_DRAFT=fig('R2-cancelled-draft')

def evidence(n=None,bbox=None,source=None):
 if n:
  m=manifest[n-1]
  return dict(crop=m['path'],bbox=m['bbox'],bbox_image=m['source'],source=m['source'])
 return dict(crop=None,bbox=bbox,bbox_image=source,source=source)

dif=[]
def d(id,location,c,h,reading,scan,kind='other',cc=False,ch=False,confidence='high',marked='no',n=None,bbox=None,source=None,math=False):
 dif.append(dict(id=id,location=location,c=c,h=h,reading=reading,scan_shows=scan,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,math_consequential=math,**evidence(n,bbox,source)))

d('R2-01','Running folio, top centre',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}',r'\page{70}',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}','A crossed/looped left digit and overlaid right oval plus descending old stroke do not securely separate 70 from 79 or the predecessor.','other',False,True,'low','yes',1)
d('R2-02','Opening, au =',r'au $=$',r'au même',r'au $=$','Two separate horizontal strokes occupy the word position.','abbreviation expanded or spelling modernised',False,True,n=None,bbox=[625,106,815,158],source=upper)
d('R2-03','Opening, ont =',r'ont $=$',r'ont même',r'ont $=$','The same position after ont contains two horizontal strokes, not letters.','abbreviation expanded or spelling modernised',False,True,bbox=[269,187,510,255],source=upper)
d('R2-04','Third line, beginning',r'\unsure{Donnons nous}',r'Donc \ill{}',r'\unsure{Donnons nous}','The initial D is followed by several reduced humps; a separate nous-like group follows. The fast middle remains uncertain.','readable ink left as \\ill{}',False,True,'medium','yes',2)
d('R2-05','Left margin beside Une autre façon',r'\margin{$\unsure{!|\vdots}\qquad\unsure{!|\vdots}$}','',F_MARGIN,'The two groups have different segmented bodies and different vertical positions; the first low point is displaced right.','drawing or diagram',True,True,'high','no',4)
d('R2-06','Condition, immediately before que',r'dire que',r'dire (que',r'dire que','There is no separate opening parenthesis before que; the descending stroke belongs to q.','text not on the page',False,True,n=3)
d('R2-07','Condition, final disj and following punctuation',r"F',G\ \text{disj}$,",r"F', G$ disj.)",r"F',G\ \text{disj}$,",'The second disj has no separate stop; the following short curved mark matches a comma.','other',False,True,n=3)
d('R2-08','Corollary, de below the raised addition',r'Le cosupport \inserted{dans $\mathcal F$} de tout objet $G$',r'Le cosupport \struck{de} \add{dans $\mathfrak{F}$} tout objet $G$',r'Le cosupport \deleted{de}\inserted{dans $\mathcal F$} tout objet $G$','The long rising line crosses the de group below dans F; I record de as cancelled.','deletion state (struck given live or live given struck)',True,False,'medium','no',5)
d('R2-09','Corollary, long stroke under dans F',r'\inserted{dans $\mathcal F$}',r'\add{dans $\mathfrak{F}$}',F_COR,'The rising stroke extends well beyond de and curves upward beneath the right end of the raised phrase.','drawing or diagram',True,True,n=5)
d('R2-10','Six live family-F occurrences: raised dans F; de F after G; Phi inclusion; partie de F; F-support; F-saturée',r'\mathcal F; \mathcal F; \Phi\subset\mathcal F; \mathcal F; \mathcal F\text{-support}; \mathcal F\text{-saturée}',r'\mathfrak{F}; \mathfrak{F}; \Phi\subset\mathfrak{F}; \mathfrak{F}; \mathfrak{F}\text{-support}; \mathfrak{F}\text{-saturée}',r'\mathcal F; \mathcal F; \Phi\subset\mathcal F; \mathcal F; \mathcal F\text{-support}; \mathcal F\text{-saturee}','The live family letters have a long returned top, slender stem and hooked foot; none is an angular blackletter F. Accent is separately collated.','misread symbol or index',False,True,'high','no',None,[274,540,1640,1420],whole)
d('R2-11','Corollary, non ... pour',r'\unsure{seult|seulemt}',r'seulement',r'\unsure{seult|seulemt}','After seu the tall l is followed by a compressed low run and a high terminal t; a full seulement is not established.','abbreviation expanded or spelling modernised',False,True,'low','no',6)
d('R2-12','Corollary, second order sign',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','The lower two arms bow downward, unlike the preceding straight leq.','misread symbol or index',True,False,'high','no',6,math=True)
d('R2-13','Corollary, after c\'est donc',r"ce qu'on appelle",r'\ill{} \ill{}',r"ce qu'on appelle",'The separate ce, long-descending qu and two tall l strokes of appelle are visible.','readable ink left as \\ill{}',False,True,'high','yes',None,[276,901,986,1008],upper)
d('R2-14','Corollary, first sous-contrée',r'\uline{sous}-\unsure{contrée|contrie}',r'\emph{sous}-contrée',r'\uline{sous}-\unsure{contrée|contrie}','Only sous is underlined. The short medial letter before final e and its high tick remain reduced.','misread word',False,True,'medium','no',7)
d('R2-15','Donc, worked following word',r'\unsure{itou}',r'itou',r'\unsure{itou|itout}','An i, a heavily retraced t-like middle and ou-like ending are visible; the detached high final stroke could belong to a terminal t.','misread word',True,True,'low','no',8)
d('R2-16','Donc, detached high final mark',r'\unsure{itou}',r'itou',F_ITOU,'A short two-leg stroke sits above the final right edge of the word, with a visible gap below it.','drawing or diagram',True,True,'high','no',8)
d('R2-17','Restatement, toute before partie',r'\deleted{toute} partie',r'toute partie',r'\deleted{toute} partie','A horizontal stroke runs through toute; partie immediately follows and stays live.','deletion state (struck given live or live given struck)',False,True,bbox=[1125,0,1540,93],source=lower)
d('R2-18','Restatement, quotation marks around the F-saturée phrase',r'``$\mathcal F$-saturée,',r'« $\mathfrak{F}$-saturée »,',r'``$\mathcal F$-\unsure{saturee|saturée},','Two short upright quotation strokes open the phrase; a single comma follows the word, with no closing pair. Alphabet and accent are separately collated.','other',False,True,n=9)
d('R2-19','Restatement, accent in saturée',r'saturée',r'saturée',r'\unsure{saturee|saturée}','The final connected humps do not show a securely separate acute stroke.','misread word',True,True,'medium','no',9)
d('R2-20','Restatement, punctuation immediately after leq',r'\unsure{,)|,) ;}',r',',F_PUNCT,'A low comma precedes a large closing curve; a triangular loop and short right arm are attached near the sheet edge. A semicolon is not secure.','drawing or diagram',True,True,'low','no',10)
d('R2-21','Restatement, page reference',r'cf page $67$)',r'cf p. 67)',r'cf page $67$)','After cf there is a p stem, a small internal loop and a descended loop, rather than a stopped p alone.','abbreviation expanded or spelling modernised',False,True,'medium','no',11)
d('R2-22','Restatement, automatically',r'\unsure{automatiquemt|automatiquement}',r'automatiquement',r'\unsure{automatiquemt|automatiquement}','The middle is compressed and the terminal run ends high; the full ment letters cannot be individually separated.','abbreviation expanded or spelling modernised',False,True,'low','no',11)
d('R2-23','Restatement, cancelled loop before une',r'\deleted{\unsure{f}}une',r'une',r'\deleted{\unsure{f}}une','One tall looped group is crossed by a descending oblique stroke immediately before une.','omission',False,True,'medium','no',11)
d('R2-24','Inverted draft folio',r'\mspage{\deleted{\unsure{5\deleted{\unsure{4|3}}5}}}',r'\note{la moitié inférieure de la feuille porte, écrit tête-bêche et séparé du haut par un trait, un début de page numéroté « 55 » (chiffre surchargé), barré de longs traits obliques : c\'est le texte donné ici entre les marques de biffure}',r'\mspage{\deleted{5\deleted{\unsure{4|3}}5}}','Both surface 5 forms have upper bars and lower bowls; the older second digit remains crowded and may be 4 or 3. H records the folio editorially, not as a diplomatic folio.','other',True,True,'medium','yes',12)
d('R2-25','Inverted cancelled draft, enclosure, orientation and cancellation strokes',r'% Cancelled draft, written upside down. The diagonal strokes run across the whole block.',r'\note{la moitié inférieure de la feuille porte, écrit tête-bêche et séparé du haut par un trait, un début de page numéroté « 55 » (chiffre surchargé), barré de longs traits obliques : c\'est le texte donné ici entre les marques de biffure}',F_DRAFT,'An irregular upper/right boundary, several crossing diagonals and additional right-side curves surround/cross the inverted writing.','drawing or diagram',True,True,'high','yes',None,[24,1465,1677,2338],whole)
d('R2-26','Inverted first line, worked capital after et',r'\deleted{\unsure{\mathcal F|F}}\Phi',r'\Phi',r'\unsure{\Phi|\deleted{\mathcal F}\Phi|\deleted{F}\Phi}','A dense central stem crosses a retraced oval and extra bars; the final Phi is plausible, but a complete distinct older F is not independently recoverable.','deletion state (struck given live or live given struck)',True,True,'low','no',14)
d('R2-27','Inverted first line, un after the worked capital',r'\unsure{un}',r'un',r'\unsure{un}','A small loop and extended low wave support un, but the compressed joins do not fully settle it.','misread word',False,True,'medium','no',13)
d('R2-28','Inverted draft, first ens and later l\'ens',r'ens; l\'ens',r'ens.; l\'ens.',r'ens; l\'ens','Neither occurrence has a separate point after the low terminal run.','other',False,True,'high','no',None,[80,1710,1445,2275],whole)
d('R2-29','Inverted opening, before parties',r'\unsure{de|des}',r'de',r'de','The group contains a looped d and e exit; no additional s is visible before parties.','misread word',True,False,'high','no',13)
d('R2-30','Inverted draft, three M occurrences: parties de M; x in M; bijection de M',r'M; M; M',r'\mathcal{M}; \mathcal{M}; \mathcal{M}',r'M; M; M','Each M consists of two ordinary peaks; there is no separate calligraphic flourish.','misread symbol or index',False,True,'high','no',None,[70,1710,1450,2275],whole)
d('R2-31','Inverted second line, satisfaisant la',r'satisfaisant la condition',r'satisfaisant à la condition',r'satisfaisant la condition','Only la lies between the end of satisfaisant and condition; no separate à is present.','text not on the page',False,True,n=13)
d('R2-32','Inverted second line, parenthetical abbreviation',r'\unsure{(au --)|(ou --)|(en --)}',r'(\ill{})',r'\unsure{(au --)|(ou --)|(en --)}','A small looped vowel group and a distinct short dash stand between the parentheses.','readable ink left as \\ill{}',False,True,'low','yes',15)
d('R2-33','Inverted Alors line, punctuation after inclusion',r"d'inclusion,",r"d'inclusion",r"d'inclusion\unsure{,}",'A faint detached hooked trace follows the ending near the original left edge; a comma remains only tentative.','other',True,True,'low','no',16)
d('R2-34','Inverted draft, six x occurrences in A_x, domain and application',r"A_x; (x\in M); x\mathrel{\vdash\joinrel\dashv}A_x; A_x; A_x",r"A_X; (X\in\mathcal{M}); X\mapsto A_X; A_X; A_X",r"A_x; (x\in M); x\mathrel{\vdash\joinrel\dashv}A_x; A_x; A_x",'The x crossings are reduced relative to A and M; the terminal indices sit below the capital baseline. Arrow and M are separately collated.','misread symbol or index',False,True,'high','no',None,[25,1470,1420,1960],whole)
d('R2-35','Inverted application, sign after x',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}','The horizontal ends in a small upright at each end; the right end does not have converging arrowhead arms.','misread symbol or index',True,True,'high','no',17,math=True)
d('R2-36','Inverted penultimate line, two internal deletions after des',r'\deleted{\unsure{ses|son} \unsure{par|p}}',r'\struck{\ill{}}',r'\deleted{\unsure{ses|son}} \deleted{\unsure{p|par}}','Two word-sized groups have separate horizontal strike strokes: the first has low s/e/s-like joins; the second clearly has p but its following letters are masked.','readable ink left as \\ill{}',True,True,'low','yes',18)
d('R2-37','Inverted final line, first word',r'\unsure{Dém|Dire|Bien}',r'Dém.',r'\unsure{Dém|Dire}','The first letter has a D-like outer curve and lower return, followed by a high short mark and low humps; no second B bowl is visible. The absent period is separately collated.','misread word',True,True,'medium','no',19)
d('R2-38','Inverted final line, stop after first word',r'\unsure{Dém|Dire|Bien} $A_x$',r'Dém. $A_X$',r'\unsure{Dém|Dire} $A_x$','There is no separate stop between the low terminal hump and A. Letter readings are separately collated.','text not on the page',False,True,n=19)

cd=[]
def doubt(location,c,reading,status,scan,n=None,bbox=None,source=None):
 cd.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=scan,**evidence(n,bbox,source)))

doubt('Running folio, predecessor',r'\deleted{\unsure{69|79}}',r'\deleted{\unsure{69|79}}','retained','A low loop below the left crossing and an older right descender are present, but layering does not settle the number.',1)
doubt('Running folio, surface',r'\unsure{70|79}',r'\unsure{70|79}','retained','The visible right loop has a lower return and an overlapping long descender.',1)
doubt('Opening repetition signs, both occurrences',r'$=$; $=$',r'$=$; $=$','resolved','Both positions have two horizontal strokes; the second has a short connected return at its left.',None,[270,103,810,260],upper)
doubt('Third line',r'\unsure{Donnons nous}',r'\unsure{Donnons nous}','retained','The D is clear, but the reduced middle humps leave the phrase tentative.',2)
doubt('Leftmost marginal group',r'\unsure{!|\vdots}',F_MARGIN,'revised','Its segmented body and right-shifted low point are drawn literally; identity remains unassigned.',4)
doubt('Second marginal group',r'\unsure{!|\vdots}',F_MARGIN,'revised','It is a column of several separated dots/strokes, higher than the left group.',4)
doubt('Corollary abbreviation',r'\unsure{seult|seulemt}',r'\unsure{seult|seulemt}','retained','The low run between l and final t does not separately show all expanded letters.',6)
doubt('Corollary order signs',r'\leq; \unsure{\preceq|\leqslant}',r'\leq; \preceq','resolved','The first has straight arms, the second two clearly curved lower arms.',6)
doubt('Raised family F and later Phi inclusion',r'\mathcal F; \Phi\subset\mathcal F',r'\mathcal F; \Phi\subset\mathcal F','resolved','Returned F top/foot and upright-crossed oval Phi are locally visible; inclusion is open.',None,[1010,539,1635,1068],upper)
doubt('First sous-contrée',r'\unsure{contrée|contrie}',r'\unsure{contrée|contrie}','retained','The high tick is distinct but the tiny medial letter remains equivocal.',7)
doubt('Donc itou',r'\unsure{itou}',r'\unsure{itou|itout}','revised','One densely retraced t-like centre and a detached high final tick remain; the tick is also drawn.',8)
doubt('Restatement, struck toute',r'\deleted{toute} partie',r'\deleted{toute} partie','resolved','A straight horizontal cancellation crosses toute; there is no extra live toute.',None,[1125,0,1540,93],lower)
doubt('Restatement, punctuation after leq',r'\unsure{,)|,) ;}',F_PUNCT,'revised','The comma, long closing curve, upper-right loop and edge-running arm are drawn; their linguistic segmentation remains uncertain.',10)
doubt('Restatement, automatically',r'\unsure{automatiquemt|automatiquement}',r'\unsure{automatiquemt|automatiquement}','retained','The contracted/fused ending does not decide between the two readings.',11)
doubt('Restatement, cancelled f-like group',r'\deleted{\unsure{f}}',r'\deleted{\unsure{f}}','retained','One looped vertical group is crossed; there is no separate complete extra word.',11)
doubt('Inverted folio, surface 55',r'\unsure{5\deleted{\unsure{4|3}}5}',r'5\deleted{\unsure{4|3}}5','revised','Both surface 5s have distinct upper bars and lower bowls.',12)
doubt('Inverted folio, older second digit',r'\deleted{\unsure{4|3}}',r'\deleted{\unsure{4|3}}','retained','Overlapping upper and medial strokes do not separate a prior 4 from 3.',12)
doubt('Inverted first-line overwritten capital',r'\deleted{\unsure{\mathcal F|F}}\Phi',r'\unsure{\Phi|\deleted{\mathcal F}\Phi|\deleted{F}\Phi}','revised','The Phi-like central loop is evident, but a distinct complete older F cannot be isolated.',14)
doubt('Inverted first-line un',r'\unsure{un}',r'\unsure{un}','retained','A small initial loop and low joined run support, but do not fully settle, un.',13)
doubt('Inverted first-line de/des',r'\unsure{de|des}',r'de','resolved','The final exit is an e-like stroke, with no additional s group.',13)
doubt('Inverted parenthetical phrase',r'\unsure{(au --)|(ou --)|(en --)}',r'\unsure{(au --)|(ou --)|(en --)}','retained','The small looped vowel group is followed by a separate dash.',15)
doubt('Inverted Alors Phi, muni',r'\Phi, muni',r'\Phi, muni','resolved','The run ends at the i position; there is no separate terminal e.',16)
doubt('Inverted application sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mathrel{\vdash\joinrel\dashv}','resolved','Two short terminal uprights bound the horizontal; there is no pointed right head.',17)
doubt('Inverted internal deletion, first group',r'\unsure{ses|son}',r'\unsure{ses|son}','retained','The strike crosses the low joins; both the ses-like and son-like readings remain possible.',18)
doubt('Inverted internal deletion, second group',r'\unsure{par|p}',r'\unsure{p|par}','revised','The p stem and shoulder are distinct; any following ar is masked by the strike.',18)
doubt('Inverted final-line first word',r'\unsure{Dém|Dire|Bien}',r'\unsure{Dém|Dire}','revised','One D-like outline is visible; the raised mark and following humps do not distinguish Dém from Dire.',19)
doubt('Inverted final union index',r'\bigcup_{i\in I} A_i',r'\bigcup_{i\in I} A_i','resolved','The first subscript is dotted with no descender; I has horizontal bars.',20)
doubt('Inverted last A subscript and possible stop',r'A_i',r'A_i','resolved','The right short lowered stroke has one high dot; there is no separate terminal low stop.',20)

inv=[]
def invitem(element,kind,position,words,sheet='text'):
 inv.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind=sheet,hand='his hand',transcribed='yes'))
invitem('Running folio','text','top centre','70 / 79 over 69 / 79')
invitem('Older running folio','deletion','top centre, under surface digits','69 / 79')
invitem('Opening paragraph','text','upper block, first two lines','Il revient au =')
invitem('Support line','text','upper block, third line','Donnons nous un support')
invitem('Implication restatement','text','upper block, next two lines','Une autre façon de dire')
invitem('Two marginal mark groups','drawing','left of Une autre façon','segmented columns with separated low dots')
invitem('Corollary heading','text','left at corollary start','Corollaire, singly underlined')
invitem('Corollary body','text','middle upper block','Le cosupport ... sous-contrée')
invitem('Raised phrase','insertion','above de after cosupport','dans F')
invitem('Crossed de','deletion','below raised phrase','de')
invitem('Long rising correction stroke','drawing','under dans F, through de','rising curved oblique stroke')
invitem('Donc paragraph','text','after corollary','Donc itou / itout pour toute partie')
invitem('Detached high terminal mark','drawing','above final edge of itou','two short joined legs')
invitem('Restatement paragraph','text','last live paragraph','En d\'autres termes')
invitem('Crossed toute','deletion','restatement first line','toute')
invitem('Crowded terminal punctuation','drawing','right edge after leq','comma, closing curve, upper loop and right arm')
invitem('Cancelled single looped group','deletion','before une in final live line','f-like form')
invitem('Inverted draft folio','text','bottom centre in page orientation','55 over earlier second digit 4 / 3','cancelled_draft')
invitem('Older second draft-folio digit','deletion','inside second digit of 55','4 / 3','cancelled_draft')
invitem('Draft opening paragraph','deletion','bottom strip, first two lines when rotated','un ensemble, et ... condition précédente','cancelled_draft')
invitem('Worked first capital','deletion','after et in draft opening; layer state uncertain','Phi-like retraced capital, possible earlier F','cancelled_draft')
invitem('Draft assertion paragraph','deletion','inverted draft, next five lines','Alors Phi, muni ... objets irréductibles de Phi','cancelled_draft')
invitem('First internal cancelled group','deletion','draft assertion, after des','ses / son','cancelled_draft')
invitem('Second internal cancelled group','deletion','same line before objets','p / par','cancelled_draft')
invitem('Draft final line','deletion','upper boundary of inverted block','Dém / Dire A_x est irréductible, car si ...','cancelled_draft')
invitem('Draft enclosure and cancellation strokes','drawing','whole bottom strip','irregular top/right boundary, oblique rules and right-side curves','cancelled_draft')

remaining=[
 dict(location='Running folio and predecessor',reading=r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}',alternatives=['69 or 79 beneath','70 or 79 at surface'],confidence='low',reason='Overlaid digit strokes cannot be cleanly assigned to layers.'),
 dict(location='Third line',reading=r'\unsure{Donnons nous}',alternatives=['Donnons nous; reduced medial letters not fully deciphered'],confidence='medium',reason='Several letter groups collapse into low humps.'),
 dict(location='Corollary abbreviation',reading=r'\unsure{seult|seulemt}',alternatives=['seult','seulemt'],confidence='low',reason='No separate full medial e/m sequence is established.'),
 dict(location='First sous-contrée',reading=r'\unsure{contrée|contrie}',alternatives=['contrée','contrie'],confidence='medium',reason='Tiny medial letter plus high tick.'),
 dict(location='Donc, worked word and high mark',reading=r'\unsure{itou|itout}',alternatives=['itou with a detached unexplained stroke','itout with a displaced final t stroke'],confidence='low',reason='The terminal high stroke is detached and its function is unknown; it is drawn in R2-itou-mark.'),
 dict(location='F-saturée label',reading=r'\unsure{saturee|saturée}',alternatives=['saturee','saturée'],confidence='medium',reason='No secure detached acute is visible above the final humps.'),
 dict(location='Restatement punctuation after leq',reading='Doubt-marked TikZ punctuation in R2-right-punctuation',alternatives=[',) plus a worked loop/arm',',) ; with overlapping strokes'],confidence='low',reason='The right loop and arm run into the sheet edge; their linguistic division is unclear.'),
 dict(location='Final live automatically',reading=r'\unsure{automatiquemt|automatiquement}',alternatives=['automatiquemt','automatiquement'],confidence='low',reason='Compressed ending.'),
 dict(location='Cancelled loop before une',reading=r'\deleted{\unsure{f}}',alternatives=['f-like single letter; exact form uncertain'],confidence='low',reason='A cancellation stroke crosses the loop and stem.'),
 dict(location='Inverted folio older digit',reading=r'5\deleted{\unsure{4|3}}5',alternatives=['4','3'],confidence='low',reason='Dense overlapping upper digit strokes.'),
 dict(location='Inverted first-line capital',reading=r'\unsure{\Phi|\deleted{\mathcal F}\Phi|\deleted{F}\Phi}',alternatives=['one retraced Phi','Phi over calligraphic F','Phi over plain F'],confidence='low',reason='The common central stem and bars do not isolate a complete older glyph.'),
 dict(location='Inverted un after capital',reading=r'\unsure{un}',alternatives=['un; lettering incompletely resolved'],confidence='medium',reason='Compressed loop and low joined run.'),
 dict(location='Inverted parenthetical phrase',reading=r'\unsure{(au --)|(ou --)|(en --)}',alternatives=['(au --)','(ou --)','(en --)'],confidence='low',reason='Vowel loops are reduced.'),
 dict(location='Inverted inclusion punctuation',reading=r"d'inclusion\unsure{,}",alternatives=['comma','incidental/edge trace'],confidence='low',reason='Faint detached hook near the original left edge.'),
 dict(location='Inverted first internal deletion',reading=r'\deleted{\unsure{ses|son}}',alternatives=['ses','son'],confidence='low',reason='Horizontal strike covers the medial joins.'),
 dict(location='Inverted second internal deletion',reading=r'\deleted{\unsure{p|par}}',alternatives=['p','par'],confidence='low',reason='Only the p stem and shoulder are clear.'),
 dict(location='Inverted final-line first word',reading=r'\unsure{Dém|Dire}',alternatives=['Dém','Dire'],confidence='medium',reason='High short mark and low humps do not identify the middle unequivocally.'),
]
notation=[
 dict(sign='repetition sign',latex=r'=',appearance='Two horizontal strokes, second pair with a short left return.',location='Opening, twice',alternatives=[]),
 dict(sign='family of figures',latex=r'\mathcal F',appearance='Returned long top, slender stem, hooked foot.',location='Six live occurrences',alternatives=[]),
 dict(sign='individual objects',latex=r'F,F\prime,G',appearance='Plain capitals; one raised prime on second F.',location='Opening and implication; G in corollary',alternatives=[]),
 dict(sign='two order signs',latex=r'\leq;\preceq',appearance='First straight; second lower arms curved.',location='Corollary',alternatives=[]),
 dict(sign='Phi and inclusion',latex=r'\Phi\subset\mathcal F',appearance='Oval crossed by central upright, open inclusion.',location='Donc paragraph',alternatives=[]),
 dict(sign='worked Phi',latex=r'\unsure{\Phi|\deleted{\mathcal F}\Phi|\deleted{F}\Phi}',appearance='Retraced oval, vertical and extra bars.',location='Inverted opening',alternatives=['single retraced Phi','Phi over calligraphic F','Phi over plain F']),
 dict(sign='ambient set',latex='M',appearance='Plain two-peaked capital.',location='Three inverted occurrences',alternatives=[]),
 dict(sign='capped horizontal',latex=r'\mathrel{\vdash\joinrel\dashv}',appearance='Horizontal with small terminal upright at each end, no pointed head.',location='Inverted application',alternatives=[]),
 dict(sign='subscripts and union',latex=r'A_x;\bigcup_{i\in I}A_i',appearance='Reduced crossing x; dotted short i; barred capital I.',location='Inverted argument',alternatives=[]),
]
abbr=[dict(form='disj.; disj',expansion='disjoints (local point present only at first occurrence)'),dict(form='seult / seulemt',expansion='seulement'),dict(form='cf',expansion='confer'),dict(form='automatiquemt',expansion='automatiquement'),dict(form='ens; l\'ens',expansion='ensemble; l\'ensemble'),dict(form='Dém',expansion='démonstration (uncertain reading)'),dict(form='au -- / ou -- / en --',expansion='not securely established; left unexpanded')]

notes=dict(summary='One live handwritten argument occupies the upper page; an inverted, heavily cancelled draft fills the bottom strip. The complete reading includes raised text, local deletions, overwritten folios and drawn marks.',math_reading_decisions='Comparison of the two order signs and of the application terminal strokes prompted local inspection. Curvature and terminal uprights, not the expected mathematics, decided those forms. The i/I and x/X distinctions were read from size, dots and placement. No theorem or implication was proved or corrected.',author_checks='No mathematical validation performed; check_events is empty. The apparent loss of de under a cancellation stroke and the unclosed quotation are preserved rather than repaired. marked_in_h means H explicitly flags doubt, unreadability or an editorial issue; ordinary insertion/deletion markup alone is not treated as a doubt flag.',title_dates_pagination='No title or date. Top folio remains 70/79 over 69/79 from this page alone. The inverted surface folio is 55 with an uncertain older second digit 4/3. No adjacent folios were consulted.')

report=dict(reader='R2',cote='156-4',scan='71',brief_version='v07',started_utc='2026-11-20T11:30:32.566200Z',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),image_views=metadata['images'],reading_file=str(base/'reading.tex'),differences=dif,c_doubts=cd,inventory=inv,remaining_doubts=remaining,notation=notation,abbreviations=abbr,notes=notes,check_events=[],crops=manifest,workflow_feedback=['For a crowded punctuation group whose graphic parts are clearer than their character identities, the brief gives no preferred inline encoding. I preserved the complete group as doubt-marked TikZ in its paragraph.'],structural_checks={})

outcomes=[
'Overwritten top digits remain unresolved; no adjacent-page inference used.',
'Donnons nous remains tentative; terminal support stop is visible.',
'No opening parenthesis before que; second disj has no stop and is followed by a comma. Crop lower boundary clips the extreme bottom of j, but that descender was visible in the supplied half and is not used to infer punctuation absence.',
'Both segmented marginal groups drawn literally at their different heights.',
'de is crossed by a long rising stroke; full raised phrase dans F preserved, including stroke geometry.',
'seult/seulemt remains open; second order resolves to the curved preceq.',
'Only sous underlined; contrée/contrie retained.',
'Retraced central word and detached high tick kept; itou/itout left open.',
'Double opening strokes and no closing quote; accent in saturee/saturée uncertain.',
'Whole terminal punctuation reaches actual sheet edge; comma, closing curve and attached loop/arm drawn rather than normalized.',
'cf page 67 read; automatically abbreviation and cancelled f-like group retained as uncertain.',
'Surface 55 resolved; older second digit remains 4/3.',
'un remains tentative; de rather than des; no periods after ens; plain M; satisfaisant la without added à.',
'Worked Phi may be a single retraced glyph or overwrite; no confident distinct earlier F asserted.',
'Parenthetical vowel group plus dash preserved as au/ou/en alternatives.',
'muni has no separate e; faint final inclusion hook retains comma doubt; C1 on baseline.',
'Lowercase x forms and capped horizontal sign read; no arrowhead observed.',
'Two separately struck groups identified; ses/son and p/par remain unresolved.',
'D-like initial permits Dém or Dire; no separate stop before A; Bien excluded.',
'Union subscript i in I and final A_i resolved; no separate terminal low stop.'
]
with (base/'inspection_log.txt').open('a',encoding='utf-8') as log:
 for k,(m,result) in enumerate(zip(manifest,outcomes),4):
  log.write(f'{k:02d} Viewed crop exactly once: {m["path"]}; source={m["source"]}; original bbox={m["bbox"]}; scale={m["scale"]}; rotation={m["rotation"]}. Evidence: {result}\n')
 log.write('All twenty crop images were fully delivered by view_image in batches of at most three. No OCR, second half view, re-crop, outside research, other-reader inspection or LaTeX compilation.\n')

# Structural checks only: do not compile or perform mathematical validation.
without_comments='\n'.join(line.split('%')[0] for line in tex.splitlines())
balance=0
for i,ch in enumerate(without_comments):
 if ch=='{' and (i==0 or without_comments[i-1]!='\\'): balance+=1
 if ch=='}' and (i==0 or without_comments[i-1]!='\\'): balance-=1
 if balance<0: raise AssertionError('negative brace depth')
assert balance==0
beg=re.findall(r'\\begin\{([^}]+)\}',without_comments)
end=re.findall(r'\\end\{([^}]+)\}',without_comments)
assert sorted(beg)==sorted(end)
assert without_comments.count('$')%2==0
assert r'\scanpage{71}' in tex and r'\mspage' in tex
assert r'\illegible' not in tex
assert len(dif)==len(set(x['id'] for x in dif))
assert all(type(x['change_c']) is bool and type(x['change_h']) is bool and type(x['math_consequential']) is bool for x in dif)
assert all(Path(m['path']).is_file() for m in manifest)
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed_kinds for x in dif)
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in inv)
report['structural_checks']=dict(braces_balanced=True,environment_counts_balanced=True,math_dollars_even=True,scanpage_and_mspage_retained=True,no_math_illegible=True,all_crop_paths_exist=True,json_booleans_correct=True,unique_difference_ids=True,compilation_run=False,mathematical_validation_run=False)
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (base/'inspection_log.txt').open('a',encoding='utf-8') as log:
 log.write('Structural checks passed: brace depth, environment counts, even math delimiters, scan/folio macros, no illegible math, unique difference IDs, JSON boolean types, inventory/kind enums and all crop paths. No compilation.\n')
 log.write('Finished UTC: '+report['finished_utc']+'\n')
print(json.dumps(dict(differences=len(dif),c_doubts=len(cd),inventory=len(inv),remaining_doubts=len(remaining),crops=len(manifest),reading_file=report['reading_file'],report_file=str(base/'report.json')),indent=2))
