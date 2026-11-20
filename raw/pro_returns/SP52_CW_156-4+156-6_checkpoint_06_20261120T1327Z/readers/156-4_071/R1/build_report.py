from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R1')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_071')
meta=json.loads((packet/'metadata.json').read_text())
whole,ha,hb=meta['images']
crops=json.loads((out/'crop_manifest.json').read_text())
cp={i+1:c['path'] for i,c in enumerate(crops)}
D=[]
def diff(loc,c,h,r,e,n=None,b=None,confidence='high',kind='other',cc=False,ch=True,mh='no',math=False,src=None):
 D.append(dict(id=f'R1-D{len(D)+1:02}',location=loc,c=c,h=h,reading=r,scan_shows=e,confidence=confidence,kind=kind,marked_in_h=mh,change_c=cc,change_h=ch,crop=cp[n] if n else None,bbox=b or (crops[n-1]['bbox'] if n else None),bbox_image=src or whole,math_consequential=math))
diff('upper folio',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}',r'\page{70}',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}','Both digits contain overlaid strokes; the final right loop also has a descending stroke.',1,confidence='low')
diff('opening, au',r'au $=$','au même',r'au $=$','Two separate horizontal strokes stand between au and de.',b=[620,100,810,160],kind='misread symbol or index',src=ha)
diff('opening, ont',r'ont $=$ cosupport','ont même cosupport',r'ont $=$ cosupport','A second pair of horizontal strokes replaces the word même.',b=[270,190,830,265],kind='misread symbol or index',src=ha)
diff('second paragraph',r'\unsure{Donnons nous}',r'Donc \ill{}',r'\unsure{Donnons nous}','After D are several low groups before a separate nous; their reduced middles remain uncertain.',2,confidence='medium',kind='misread word',mh='yes')
diff('left margin opposite Une autre façon',r'\margin{$\unsure{!|\vdots}\qquad\unsure{!|\vdots}$}','',r'% fig:margin-mark-columns','Two uneven columns consist of separated blobs and strokes; the left column is lower and its last point is displaced right.',3,kind='drawing or diagram',cc=True)
diff('implication sentence punctuation',r'de dire que $F,G\ \text{disj.}\Longrightarrow F\prime,G\ \text{disj}$, est ainsi :',r'de dire (que $F, G$ disj. $\Longrightarrow F\prime, G$ disj.) est ainsi :',r'de dire que $F,G\ \text{disj.}\Longrightarrow F\prime,G\ \text{disj}$, est ainsi :','The descending start of que is a letter stroke; the second disj has no detached point, and a low curved comma follows.',4,b=[780,385,1585,590],confidence='medium')
diff('corollary, state and placement of de',r'\inserted{dans $\mathcal F$} de tout',r'\struck{de} \add{dans $\mathfrak{F}$} tout',r'\deleted{de} \inserted{dans $\unsure{F|\mathcal F}$} tout','A rising stroke crosses the baseline de; dans and its F stand together above it.',4,b=[1015,540,1360,680],kind='deletion state (struck given live or live given struck)',cc=True,ch=False)
diff('corollary, capital in raised dans phrase',r'\mathcal F',r'\mathfrak{F}',r'\unsure{F|\mathcal F}','The reduced raised capital has a sloping top bar and curved foot but no securely closed upper loop.',4,b=[1120,535,1195,600],confidence='low',kind='misread symbol or index',cc=True)
diff('corollary, de F after objet G',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The capital has a looped head and returning stem, without Gothic broken strokes.',b=[385,730,450,810],kind='misread symbol or index',src=ha)
diff('corollary, non ... pour',r'\unsure{seult|seulemt}','seulement',r'\unsure{seult|seulemt}','The tall l is followed by a low compressed run and final ascending t; a full ement is not separately legible.',5,b=[1050,688,1300,770],confidence='low',kind='abbreviation expanded or spelling modernised')
diff('corollary, second order sign',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','The rising upper arm meets a bowed lower arm; a second bowed stroke lies below it.',6,b=[975,785,1090,855],kind='misread symbol or index',cc=True,ch=False,math=True)
diff('corollary, phrase before une sous-',r"ce qu'on appelle",r'\ill{} \ill{}',r"ce qu'on appelle",'The low ce, descending qu, following on, and two tall l strokes in appelle are present.',7,b=[270,900,1010,1020],kind='readable ink left as \\ill{}',mh='yes')
diff('corollary, first sous-contrée',r'\unsure{contrée|contrie}','contrée',r'\unsure{contrée|contrie}','A small high tick precedes the final e; the short preceding letter does not settle é versus i.',6,b=[1410,850,1645,950],confidence='medium')
diff('Donc itou',r'\unsure{itou}','itou',r'\unsure{itou}','The t-like stem is multiply worked and there is a high terminal tick; no separate older word is legible.',7,b=[535,1025,700,1100],confidence='medium')
diff('Donc paragraph, F after inclusion',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The F after the open inclusion has a closed upper loop and a long curved stem.',6,b=[1520,945,1625,1035],kind='misread symbol or index')
diff('restatement, toute',r'\deleted{toute}','toute',r'\deleted{toute}','A horizontal stroke crosses all of toute; partie follows live.',b=[1120,0,1540,85],kind='deletion state (struck given live or live given struck)',src=hb)
diff('restatement, de F',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','This F has a loop at the head and a small curved foot.',b=[425,145,505,230],kind='misread symbol or index',src=hb)
diff('restatement, F-support',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The head returns into a loop before its descending stem.',8,b=[1020,1205,1110,1295],kind='misread symbol or index')
diff('restatement, F-saturée capital',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The small capital has a looped top unlike a Gothic F.',8,b=[305,1345,370,1430],kind='misread symbol or index')
diff('restatement, quotation marks',r"``$\mathcal F$-saturée,",r'« $\mathfrak{F}$-saturée »,',r"``$\mathcal F$-\unsure{saturee|saturée},",'Two small upright strokes open the quotation; after the word there is one low comma and no pair of closing strokes.',8,b=[275,1340,720,1430])
diff('restatement, accent of saturée','saturée','saturée',r'\unsure{saturee|saturée}','The last reduced humps have no securely detached accent; a connected high return could carry it.',8,b=[425,1325,635,1425],confidence='low',kind='misread word',cc=True)
diff('restatement, crowded closing marks after leq',r'\unsure{,)|,) ;}',',',r'\unsure{,)|,)\}|,) ;}','A low comma and tall closing curve are followed by a small forked return at the paper edge.',8,b=[1590,1275,1690,1375],confidence='low',cc=True)
diff('page reference',r'cf page $67$','cf p. 67',r'cf \unsure{page|pge} $67$','After p there is a tiny compact mark, then a large descending g loop and an ending stroke; p. alone omits this ink.',13,b=[275,1420,695,1510],confidence='medium',kind='misread word',cc=True)
diff('restatement, est ...',r'\unsure{automatiquemt|automatiquement}','automatiquement',r'\unsure{automatiquemt|automatiquement}','After the q descender the ending is compressed into a low run and rising t.',9,b=[825,1375,1275,1490],confidence='low',kind='abbreviation expanded or spelling modernised')
diff('restatement, cancelled mark before une',r'\deleted{\unsure{f}}','',r'\deleted{\unsure{f}}','A separate tall loop is crossed by a diagonal stroke before une.',9,b=[1290,1360,1370,1480],confidence='low',kind='omission')
diff('inverted folio',r'\mspage{\deleted{\unsure{5\deleted{\unsure{4|3}}5}}}',r'\note{... « 55 » (chiffre surchargé) ...}',r'\mspage{\deleted{5\deleted{\unsure{4|3}}5}}','The surface has two 5 forms; the second overlays an unresolved earlier digit.',10,b=[895,2260,990,2340],confidence='medium',cc=True)
diff('inverted opening, worked Phi',r'\deleted{\unsure{\mathcal F|F}}\Phi',r'\Phi',r'\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}','Several horizontal and oval strokes share the heavy vertical; an earlier complete F is possible but not independently separable.',10,b=[825,2180,930,2265],confidence='low',kind='deletion state (struck given live or live given struck)',cc=True)
diff('inverted opening, un before ens',r'\unsure{un}','un','un','A low u curve runs into one n hump before the next spaced group.',10,b=[710,2180,825,2250],kind='other',cc=True,ch=False)
diff('inverted opening, ens point','ens','ens.','ens','The three-letter group is followed by blank space, with no separate low point.',10,b=[570,2180,710,2250])
diff('inverted opening, de before parties',r'\unsure{de|des}','de','de','The d loop joins one short e stroke; no separate terminal s is visible.',10,b=[475,2180,565,2260],kind='misread word',cc=True,ch=False)
diff('inverted opening, M',r'M',r'\mathcal{M}',r'M','The capital has two ordinary peaked strokes and no added alphabet flourish.',10,b=[95,2165,210,2265],kind='misread symbol or index')
diff('inverted opening, before la condition','satisfaisant la condition','satisfaisant à la condition','satisfaisant la condition','The final satisfaisant stroke is followed directly by la; there is no intervening à group.',10,b=[955,2085,1430,2195],kind='text not on the page')
diff('inverted opening, parenthesis',r'\unsure{(au --)|(ou --)|(en --)}',r'(\ill{})',r'\unsure{(au --)|(ou --)|(en --)}','A small loop and low exit precede a separated dash between clear parentheses.',10,b=[65,2085,315,2180],confidence='low',kind='readable ink left as \\ill{}',mh='yes')
diff('inverted inclusion, terminal punctuation',"d'inclusion,","d'inclusion",r"d'inclusion\unsure{,}",'A small terminal stroke may be a comma; its furthest continuation is incompletely framed in the text crop.',11,b=[20,2025,160,2090],confidence='low',cc=True)
# Bound-variable case is recorded separately at all six occurrences.
for loc,c,h,n,b in [
 ('inverted sont les, subscript',r'A_x',r'A_X',11,[975,1820,1095,1920]),
 ('inverted parenthesis, element',r'x\in M',r'X \in \mathcal{M}',11,[825,1830,925,1920]),
 ('inverted application, source',r'x',r'X',11,[215,1830,285,1920]),
 ('inverted application, target subscript',r'A_x',r'A_X',11,[35,1810,155,1920]),
 ('inverted final argument, first subscript',r'A_x',r'A_X',12,[975,1500,1105,1650]),
 ('inverted union equality, left subscript',r'A_x',r'A_X',12,[225,1565,345,1675])]:
 diff(loc,c,h,c,'The crossed x is low or reduced relative to the adjacent capital; its local placement is retained.',n,b,kind='misread symbol or index')
diff('inverted parenthesis, domain M',r'M',r'\mathcal{M}',r'M','The M consists of two plain peaks; the neighbouring x is compared separately.',11,b=[725,1845,815,1925],kind='misread symbol or index')
diff('inverted application, connecting sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mapsto',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}','The short horizontal has a left upright and a blunt thickened right end, without a securely pointed arrowhead.',11,b=[150,1845,230,1905],confidence='medium',kind='misread symbol or index',math=True)
diff('inverted bijection, M',r'M',r'\mathcal{M}',r'M','The M again has plain peaked strokes.',12,b=[410,1735,530,1835],kind='misread symbol or index')
diff('inverted bijection, ens point',"l'ens","l'ens.","l'ens",'After the last ens stroke there is no detached point before the next line.',12,b=[35,1740,250,1835])
diff('inverted internal deletion',r'\deleted{\unsure{ses|son} \unsure{par|p}}',r'\struck{\ill{}}',r'\deleted{\unsure{ses|son} \unsure{p|par}}','Two crossed groups are present; the second has a clear p descender but its continuation is obscured by the cancelling stroke.',12,b=[985,1630,1295,1740],confidence='low',kind='readable ink left as \\ill{}',cc=True,mh='yes')
diff('inverted final line, argument label',r'\unsure{Dém|Dire|Bien}','Dém.',r'\unsure{Dém}','The initial closed D and a small raised mark favour Dém; the reduced ending remains uncertain and no separate stop follows.',12,b=[1160,1535,1320,1625],confidence='medium',kind='misread word',cc=True)
diff('inverted draft, boundary and cancellation geometry',r'% Cancelled draft, written upside down. The diagonal strokes run across the whole block.',r'\note{la moitié inférieure de la feuille porte, écrit tête-bêche et séparé du haut par un trait, un début de page numéroté « 55 » (chiffre surchargé), barré de longs traits obliques : c\'est le texte donné ici entre les marques de biffure}',r'% fig:inverted-cancelled-draft','An open continuous boundary bends below the last formula; thirteen curved or oblique strokes cross or flank the inverted block.',14,kind='drawing or diagram',cc=True)
# Literal witness quotation repair: preserve the source prime syntax, not merely equivalent notation.
for row in D:
 for field in ('c','h','reading'):
  row[field]=row[field].replace(r'F\prime',"F'")
# One disposition for every C unsure locus, plus the explicit context checks.
CD=[]
def cd(loc,c,r,status,e,n=None,b=None,src=None):
 CD.append(dict(location=loc,c=c,reading=r,status=status,scan_shows=e,crop=cp[n] if n else None,bbox=b or (crops[n-1]['bbox'] if n else None),bbox_image=src or whole))
cd('upper folio, underlying number',r'\unsure{69|79}',r'\unsure{69|79}','retained','The lower left loop and right descending stroke do not uniquely separate the earlier digits.',1)
cd('upper folio, surface number',r'\unsure{70|79}',r'\unsure{70|79}','retained','The closed right loop and surviving descending stroke leave 70/79 open.',1)
cd('Donnons nous',r'\unsure{Donnons nous}',r'\unsure{Donnons nous}','retained','Several medial letters are reduced to low separated humps.',2)
cd('margin, first column',r'\unsure{!|\vdots}',r'% fig:margin-mark-columns','revised','Irregular separate fragments and an offset lower point are reproduced without assigning a punctuation function.',3)
cd('margin, second column',r'\unsure{!|\vdots}',r'% fig:margin-mark-columns','revised','Five separated upper-to-lower fragments are drawn at their higher position.',3)
cd('non ... pour',r'\unsure{seult|seulemt}',r'\unsure{seult|seulemt}','retained','The interval after l is too compressed to decide the contraction.',5)
cd('second order sign',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','The two lower strokes are bowed, unlike the earlier straight leq.',6)
cd('first sous-contrée',r'\unsure{contrée|contrie}',r'\unsure{contrée|contrie}','retained','The short accented-letter position permits both candidates.',6)
cd('Donc itou',r'\unsure{itou}',r'\unsure{itou}','retained','The middle stem is retraced and the end carries a high tick.',7)
cd('restatement, right punctuation',r'\unsure{,)|,) ;}',r'\unsure{,)|,)\}|,) ;}','revised','A forked extra return at the right edge also permits a brace-like closure.',8)
cd('est automatiquemt',r'\unsure{automatiquemt|automatiquement}',r'\unsure{automatiquemt|automatiquement}','retained','The ending is compressed beyond the q descender.',9)
cd('cancelled mark before une',r'\unsure{f}',r'\unsure{f}','retained','The isolated crossed loop is f-like but not fully legible.',9)
cd('inverted folio, surface 55',r'\unsure{5\deleted{\unsure{4|3}}5}',r'5\deleted{\unsure{4|3}}5','resolved','The two surface digits have clear 5 outlines; the internal older digit remains doubtful.',10)
cd('inverted folio, overwritten digit',r'\unsure{4|3}',r'\unsure{4|3}','retained','The shared upper bar and overlapping bowls do not settle the earlier digit.',10)
cd('inverted opening, overwritten capital',r'\deleted{\unsure{\mathcal F|F}}\Phi',r'\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}','revised','The retraced Phi does not securely expose a complete independent earlier F.',10)
cd('inverted un before ens',r'\unsure{un}','un','resolved','The u curve and n hump are visible.',10)
cd('inverted de before parties',r'\unsure{de|des}','de','resolved','Only the joined d and e are visible before the gap.',10)
cd('inverted parenthesis',r'\unsure{(au --)|(ou --)|(en --)}',r'\unsure{(au --)|(ou --)|(en --)}','retained','A low loop-and-exit group is followed by one dash.',10)
cd('inverted application sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}','retained','The right end is blunt rather than securely arrow-shaped.',11)
cd('inverted internal deletion, first group',r'\unsure{ses|son}',r'\unsure{ses|son}','retained','A horizontal cancellation covers the joins between the reduced letters.',12)
cd('inverted internal deletion, second group',r'\unsure{par|p}',r'\unsure{p|par}','revised','The descending p is clearer than any following a or r.',12)
cd('inverted final label',r'\unsure{Dém|Dire|Bien}',r'\unsure{Dém}','revised','The initial form is D-like and the high small mark favours an accent, while the final reduced group stays uncertain.',12)
cd('C_context: both opening repetition signs',r'$=$ ; $=$',r'$=$ ; $=$','resolved','Both positions contain paired horizontal strokes.',b=[270,95,835,265],src=ha)
cd('C_context: straight and bowed order signs',r'\leq ; \unsure{\preceq|\leqslant}',r'\leq ; \preceq','resolved','The first has a straight lower stroke; the second has two bowed lower strokes.',6)
cd('C_context: raised F and Phi subset F',r'\mathcal F, \Phi, \subset',r'\unsure{F|\mathcal F}; \Phi\subset\mathcal F','revised','The raised reduced F lacks a secure head loop; the later Phi, open inclusion and looped family F are clear.',4,b=[1020,535,1630,1040])
cd('C_context: union index i in I',r'\bigcup_{i\in I} A_i',r'\bigcup_{i\in I} A_i','resolved','The lower small i has a point and no descender; I has transverse bars.',12,b=[85,1550,255,1680])
cd('C_context: final A subscript and possible stop',r'A_i',r'A_i','resolved','The raised point belongs to the low i stroke; there is no distinct additional low stop.',12,b=[70,1560,165,1670])
cd('C_context: restatement after struck toute',r'\deleted{toute} partie',r'\deleted{toute} partie','resolved','Only partie is live after the horizontal deletion.',b=[1130,0,1535,85],src=hb)
cd('C_context: inverted Phi muni',r'\Phi, muni',r'\Phi, muni','resolved','No additional e is visible beyond the final short i position.',11,b=[850,2000,1160,2095])
I=[]
def inv(element,kind,pos,words,sheet='text'):
 I.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=words,sheet_kind=sheet,hand='his hand',transcribed='yes'))
inv('upper folio','text','top centre','70/79 over 69/79')
inv('upper overwritten folio layer','deletion','top centre','69/79')
inv('opening paragraph','text','top two lines','Il revient au =')
inv('support paragraph','text','upper third line','Donnons nous un support')
inv('left marginal fragments','drawing','far left of Une autre façon','lower uneven column and offset point')
inv('right marginal fragments','drawing','immediately left of Une autre façon','higher dotted column')
inv('implication paragraph','text','upper fourth and fifth lines','Une autre façon de dire')
inv('corollary paragraph with underlined heading and sous','text','middle upper block','Corollaire Le cosupport')
inv('raised phrase','insertion','above the original de after cosupport','dans F/ℱ')
inv('cancelled de','deletion','baseline beneath raised dans F/ℱ','de')
inv('Donc paragraph','text','below corollary','Donc itou pour toute partie')
inv('restatement paragraph','text','last upright paragraph','En d’autres termes')
inv('cancelled toute','deletion','first line of restatement','toute')
inv('cancelled loop before une','deletion','penultimate upright line','f-like loop')
inv('inverted folio','text','bottom centre in scan; top of inverted draft','55','cancelled_draft')
inv('older inverted folio digit','deletion','second digit of inverted folio','4/3','cancelled_draft')
inv('inverted draft opening','deletion','first two inverted text lines','un ensemble, et Φ','cancelled_draft')
inv('worked opening capital','deletion','inverted first line','possible earlier ℱ/F under Φ; state uncertain','cancelled_draft')
inv('inverted second paragraph','deletion','inverted middle five lines','Alors Φ, muni de la relation','cancelled_draft')
inv('first internally cancelled group','deletion','inverted penultimate line after des','ses/son','cancelled_draft')
inv('second internally cancelled group','deletion','after the preceding internally cancelled group','p/par','cancelled_draft')
inv('inverted last argument line','deletion','beside the long boundary line','Dém A_x est irréductible','cancelled_draft')
inv('continuous boundary','drawing','around side and end of inverted draft','open curve with inward jog below final formula','cancelled_draft')
inv('cancellation strokes','drawing','across and beside inverted draft','thirteen curved or oblique strokes','cancelled_draft')
R=[]
def doubt(loc,r,alts,conf,reason):R.append(dict(location=loc,reading=r,alternatives=alts,confidence=conf,reason=reason))
doubt('upper folio, underlying number',r'\unsure{69|79}',['69','79'],'low','Shared overwritten loops do not separate the older digits.')
doubt('upper folio, surface number',r'\unsure{70|79}',['70','79'],'low','A long trailing stroke survives beside the surface right loop.')
doubt('second paragraph',r'\unsure{Donnons nous}',['Donnons nous'],'medium','The medial groups are reduced to low humps.')
doubt('raised capital in corollary',r'\unsure{F|\mathcal F}',['F',r'\mathcal F'],'low','No securely closed upper loop survives at this small occurrence.')
doubt('non ... pour',r'\unsure{seult|seulemt}',['seult','seulemt'],'low','A compressed run after l does not settle the contraction.')
doubt('first sous-contrée',r'\unsure{contrée|contrie}',['contrée','contrie'],'medium','The short letter before the final e is ambiguous.')
doubt('Donc itou',r'\unsure{itou}',['itou'],'medium','The central stem is retraced; the terminal high tick remains part of this uncertain reading.')
doubt('F-saturée spelling',r'\unsure{saturee|saturée}',['saturee','saturée'],'low','There is no securely separate acute; a connected high return may carry it.')
doubt('closing marks after leq',r'\unsure{,)|,)\}|,) ;}',[',)',r',)\}',',) ;'],'low','The last curve forks at the paper edge.')
doubt('page reference word',r'\unsure{page|pge}',['page','pge'],'medium','The tiny group between p and g does not make a distinct a certain.')
doubt('restatement, automatic ending',r'\unsure{automatiquemt|automatiquement}',['automatiquemt','automatiquement'],'low','The ending after q is reduced to a low run and rising final stroke.')
doubt('cancelled mark before une',r'\unsure{f}',['f'],'low','Only a crossed tall loop is recoverable.')
doubt('inverted earlier digit',r'\unsure{4|3}',['4','3'],'low','The old digit is overlaid by the surface 5.')
doubt('inverted worked Phi',r'\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}',[r'\deleted{\mathcal F}\Phi',r'\deleted{F}\Phi',r'\Phi'],'low','A complete prior F cannot be separated securely from the retracing.')
doubt('inverted parenthesis',r'\unsure{(au --)|(ou --)|(en --)}',['(au --)','(ou --)','(en --)'],'low','The small loop-and-exit group is compressed.')
doubt('inverted inclusion punctuation',r"d'inclusion\unsure{,}",[',','no punctuation'],'low','The rightmost continuation of the textual crop is clipped near original x=20–35, y=2025–2090; no absence is inferred.')
doubt('inverted application sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',[r'\mathrel{\vdash\joinrel\dashv}',r'\mapsto'],'medium','The right terminal is blunt and no clear head can be identified.')
doubt('inverted deletion, first group',r'\unsure{ses|son}',['ses','son'],'low','The cancellation covers the internal joins.')
doubt('inverted deletion, second group',r'\unsure{p|par}',['p','par'],'low','Only p is clear beneath the cancelling line.')
doubt('inverted argument label',r'\unsure{Dém}',['Dém'],'medium','The D is clear but the accented middle and reduced ending remain compressed.')
doubt('marginal columns, function',r'% fig:margin-mark-columns',['exclamation-like marks','incidental ink fragments'],'low','Their literal geometry is drawn; no linguistic function or confident separate authorship is asserted.')
N=[
 dict(sign='two repetition signs',latex=r'=',appearance='two unequal horizontal strokes at each occurrence',location='opening paragraph',alternatives=[]),
 dict(sign='first raised F',latex=r'\unsure{F|\mathcal F}',appearance='sloping upper bar, short middle bar, curved foot, uncertain top loop',location='dans phrase',alternatives=[r'\mathcal F']),
 dict(sign='later family F',latex=r'\mathcal F',appearance='looped head and returning stem',location='de F; Phi subset F; restatement three occurrences',alternatives=[]),
 dict(sign='order signs',latex=r'\leq,\preceq',appearance='first lower stroke straight; second pair of lower strokes bowed',location='corollary',alternatives=[]),
 dict(sign='Phi and inclusion',latex=r'\Phi\subset\mathcal F',appearance='oval across upright, open inclusion, looped F',location='Donc paragraph',alternatives=[]),
 dict(sign='worked Phi',latex=r'\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}',appearance='shared heavy upright with oval and horizontal retracing',location='inverted opening',alternatives=[r'\deleted{F}\Phi',r'\Phi']),
 dict(sign='plain M',latex='M',appearance='two peaks, without extra script flourish',location='three inverted occurrences',alternatives=[]),
 dict(sign='application link',latex=r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',appearance='short horizontal with left upright and blunt right end',location='inverted application',alternatives=[r'\mapsto']),
 dict(sign='small x',latex='x',appearance='low crossed strokes, including reduced subscripts',location='six inverted occurrences',alternatives=[]),
 dict(sign='union and indices',latex=r'\bigcup_{i\in I} A_i',appearance='open union; dotted small i; barred capital I; final low i and its point',location='final inverted formula',alternatives=[]),
]
A=[dict(form='disj.',expansion='disjoints'),dict(form='disj',expansion='disjoints'),dict(form='seult / seulemt',expansion='seulement (uncertain contraction)'),dict(form='cf',expansion='confer'),dict(form='pge',expansion='page (possible abbreviated alternative)'),dict(form='automatiquemt',expansion='automatiquement (possible contraction)'),dict(form='ens',expansion='ensemble'),dict(form='Dém',expansion='Démonstration (uncertain reading)')]
report=dict(reader='R1',cote='156-4',scan='71',brief_version='v07',started_utc='2026-11-20T11:30:22Z',finished_utc=None,image_views=meta['images'],reading_file=str(out/'reading.tex'),differences=D,c_doubts=CD,inventory=I,remaining_doubts=R,notation=N,abbreviations=A,notes=dict(summary='Independent ink reading of the upright notes and the inverted cancelled draft. All supplied C doubt loci and explicit scan-071 context checks have dispositions. H unreadable placeholders are accounted for at Donnons nous, ce qu’on appelle, the lower parenthesis, and the two internally deleted groups.',math_reading_decisions='Only local symbol comparison was used: the straight first inequality was compared with the bowed second sign, and x/i/I sizes and positions were inspected. No theorem, implication, support assertion or bijection claim was proved or mathematically repaired. The application-like context did not justify supplying an arrowhead.',author_checks='The overwritten capital is retained with alternatives that include mere retracing; no independently legible earlier whole glyph is asserted. The low point at final A_i is assigned to i rather than supplied as punctuation. The corollary’s baseline de is visibly cancelled beneath the raised phrase. Paragraph text appears once in the figure for the inverted draft; ordinary deletion state remains encoded with deleted.',title_dates_pagination='No title or date. Upper number remains 70/79 over 69/79. Lower surface number is 55 with an unresolved earlier second digit 4/3. No neighbouring page number was consulted. The reference is read cf page/pge 67.',framing_limits='The rightmost continuation of inclusion punctuation is incompletely framed in crop 11; its uncertainty is retained. Graphic crop 14 reaches the boundary at source x=1680 around y=1805; the line remains open there and no unseen continuation is drawn. The whole-page view established overall extent. Crop 14 was used only for the distinct still-open boundary/cancellation geometry, not to reopen decided textual loci.'),check_events=[],crops=crops,workflow_feedback=['The brief does not state whether a multi-line cancelled block should use normal-order prose plus a separate graphic or text labels within an inverted TikZ group; this reading uses one inverted group to keep text and boundary together.','When a single graphical boundary spans a large block, its one target crop necessarily overlaps already-read text; the geometric-only purpose is logged explicitly.'])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('differences',len(D),'C dispositions',len(CD),'inventory',len(I),'remaining doubts',len(R),'crops',len(crops))
