from pathlib import Path
import json,re
from datetime import datetime,timezone
B=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_068/R1')
PACK=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_068')
S='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan068.jpg'
A=S.replace('.jpg','_a.jpg'); Z=S.replace('.jpg','_b.jpg')
crops=json.loads((B/'crop_manifest.json').read_text())
cm={Path(x['path']).stem:x for x in crops}
D=[]
def diff(loc,c,h,r,e,conf='high',kind='other',marked='no',cc=False,ch=True,crop=None,bbox=None,source=None,math=False):
    row={'id':f'R1-D{len(D)+1:03d}','location':loc,'c':c,'h':h,'reading':r,'scan_shows':e,'confidence':conf,'kind':kind,'marked_in_h':marked,'change_c':cc,'change_h':ch,'crop':cm[crop]['path'] if crop else None,'bbox':bbox or (cm[crop]['bbox'] if crop else None),'bbox_image':source or (S if crop else A),'math_consequential':math}
    D.append(row); return row['id']
# Upper paragraph and cancelled opening.
diff('Cancelled opening, after de',r'\unsure{``c|``C|``6}',r'\ill{}',r'\unsure{``c|``C|``6}','Two tiny raised opening ticks precede a low inward curl. The strike obscures its upper outline, so c/C/6 remain possible.','low','readable ink left as \\ill{}','yes',crop='01_cancelled_opening')
diff('Toute partie de: family letter',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','Long bent top and a rounded lower return; no Gothic angular construction.',kind='misread symbol or index',bbox=[915,125,993,199])
diff('Parenthesis after first family letter: resp',r'resp',r'resp.',r'resp','No detached stop follows the abbreviated group before M.',kind='text not on the page',bbox=[1045,125,1335,203])
diff('Parenthesis: M',r'M',r'\mathcal{M}',r'M','The capital has two plain peaks and no separate script flourish.',kind='misread symbol or index',bbox=[1233,122,1328,195])
diff('First paragraph: minimale',r'\unsure{minimale}',r'minimale',r'\unsure{minimale}','The first minims include a thick overwritten-looking knot; the rest supports minimale but does not resolve every medial stroke.','medium',crop='02_minimale')
diff('Parenthesis: celles/telles',r'\unsure{celles|telles}',r'celles',r'\unsure{telles|celles}','The initial glyph rises to the height of both l stems and has a short upper transverse return. This favours t, but its rounded bowl also allows c.','medium','misread word',cc=True,crop='03_parenthesis')
diff('After la contenant closing parenthesis',r'la contenant),',r'la contenant),',r'la contenant)','The right parenthesis ends in one connected descending curve. The clear space to its right contains no separate comma.',kind='text not on the page',cc=True,crop='03_parenthesis',bbox=[1245,280,1625,375])
diff('Cancelled phrase following qui',r'\deleted{s\'appelle \unsure{du|de}}',r'\struck{s\'appelle le}',r'\deleted{s\'appelle \unsure{du|de}}','The last word starts with a small oval joined to a tall d ascender; the end lies under the strike and can be u or e. It is not a secure l.','low','misread word',crop='04_cancelled_sappelle')
diff('After L’application, before cosup',r'\unsure{.}',r'',r'.','A small detached low point is separated from both application and the c of the operator.','high','omission',cc=True,crop='05_operator',bbox=[765,830,835,895])
diff('Cosupport operator in L’application sentence',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'cosupp',r'\operatorname{cosup}','The ending has one descending p stroke; there is no second separated downstroke of the kind visible in the neighbouring full cosupport.','high','misread word',cc=True,crop='05_operator',bbox=[795,817,1010,915])
diff('Verb following cosup: accent',r'définit',r'définit',r'\unsure{definit|définit}','No detached acute stroke over the e can be securely separated before the tall f; the i mark farther right is distinct. The accent is therefore not silently restored.','medium','abbreviation expanded or spelling modernised',cc=True,crop='05_operator',bbox=[1050,790,1325,910])
diff('bijection: raised letter and certainty',r'\unsure{bij\inserted{e}ction}',r'bijection',r'\unsure{bij\inserted{e}ction}','A rounded e-like glyph sits distinctly above the j-to-c join. The long j return is clear; the compressed i/e structure remains doubtful.','medium','insertion or placement',crop='06_bijection',bbox=[335,930,650,1060])
diff('l’ens des parties: abbreviation point',r"l'ens",r"l'ens.",r"l'ens",'The final low sweep of ens is followed by clear space and des; there is no separate full stop.',kind='text not on the page',crop='06_bijection',bbox=[820,930,1018,1017])
diff('des parties saturées: final ending',r'\unsure{saturées|saturée}',r'saturées',r'\unsure{saturées|saturée}','An upper short accent is visible, but the terminal baseline sweep does not securely separate a final s.','medium',crop='07_saturees')
diff('Before elles: sur',r'\unsure{sur}',r'sur',r'sur','Three small separated traces give the initial s curve, shallow u and terminal r return.','high','other',cc=True,ch=False,crop='08_sur_elles',bbox=[330,1073,505,1128])
diff('After sur: elles and repetition mark',r'elles \unsure{=|mêmes}',r'\ill{}',r'elles $=$','Two long parallel strokes stand in a separate word space after elles, followed by a comma. There is no written sequence mêmes.','high','readable ink left as \\ill{}','yes',cc=True,crop='08_sur_elles',bbox=[535,1038,875,1127])
# Second paragraph.
diff('l’ens des supports: abbreviation point',r"l'ens",r"l'ens.",r"l'ens",'No distinct point follows ens before des.',kind='text not on the page',bbox=[1200,101,1440,184],source=Z)
diff('supports virtuels: underline extent',r'\uline{supports} \uline{virtuels}',r'\emph{supports virtuels}',r'\uline{supports} \uline{virtuels}','Two separate underlines end below their respective words, with a substantial unlined gap between. This records stroke extent, not merely a different emphasis macro.',bbox=[310,232,925,337],source=Z)
diff('Raised M zero: alphabet',r'\inserted{$M_0$}',r'\add{$\mathcal{M}_0$}',r'\inserted{$M_0$}','The added M has two plain peaks followed by a low round zero.',kind='misread symbol or index',crop='09_M0_leader',bbox=[213,1422,320,1500])
reading=(B/'reading.tex').read_text()
fig=re.search(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}',reading,re.S).group(0)
diff('Raised M zero: distinct connecting arm',r'',r'',fig,'A separate slightly curved diagonal rises from below-left of de to the right of the raised M zero. It has no arrowhead. The local TikZ group reproduces it and includes de M, once.','high','drawing or diagram',cc=True,crop='09_M0_leader',bbox=[210,1415,615,1525])
diff('de M immediately after raised M zero',r'M',r'\mathcal{M}',r'M','The baseline capital consists of two plain peaks, matching the locally visible added M.',kind='misread symbol or index',crop='09_M0_leader',bbox=[485,1435,600,1520])
diff('After first de M: où/ou',r'\unsure{où|ou}',r'ou',r'où','A detached short diagonal sits above the second vowel; it is not the following deletion stroke. The visible spelling is retained despite the connective expected by the sentence.','high','misread word',cc=True,crop='10_ou_F0_cancelled',bbox=[645,1432,737,1503])
diff('Cancelled de before family zero',r'\deleted{\unsure{de}}',r'\struck{de}',r'\deleted{\unsure{de}}','The ascender and low body are heavily filled by cancellation. de remains the best reading, with its final letter obscured.','low',crop='10_ou_F0_cancelled',bbox=[755,1434,854,1497])
diff('Family zero after cancelled de',r'\mathcal F_0',r'\mathfrak{F}_0',r'\mathcal F_0','The capital has a bent top and a curved lower stem, followed by a distinct low oval zero.',kind='misread symbol or index',crop='10_ou_F0_cancelled',bbox=[910,1397,1018,1498])
diff('Final M in family-zero de M',r'M',r'\mathcal{M}',r'M','The last capital is a plain two-peaked M and is followed by a full stop. No readable F replaces it.',kind='misread symbol or index',crop='10_ou_F0_cancelled',bbox=[1136,1380,1256,1486])
diff('H editorial correction of family-zero de M',r'',r'\note{« $\mathfrak{F}_0$ de $\mathcal{M}$ » : lire « de $\mathfrak{F}$ » ; la lettre finale est surchargée}',r'','The note is editorial, not manuscript text. The crop leaves the visible M in place; it does not establish the asserted replacement by F or a distinct overwritten F.','high','text not on the page','yes',crop='10_ou_F0_cancelled',bbox=[1136,1380,1256,1486])
diff('Cancelled On définit at line end',r'\deleted{On \unsure{définit}}',r'\struck{\ill{}}',r'\deleted{On \unsure{définit}}','The opening O/n and the d loop, f descender and terminal t survive multiple strikes. Medial strokes and accent remain obscured.','medium','readable ink left as \\ill{}','yes',crop='10_ou_F0_cancelled',bbox=[1315,1380,1668,1508])
diff('Cancelled L’application: preposition before cosupport',r'\deleted{L\'application du cosupport de}',r'\struck{L\'application de cosupport d}',r'\deleted{L\'application de cosupport \unsure{d|de}}','After application the d loop exits in a short low e-like stroke; no separate u cup is visible. The whole line has one long cancellation.',kind='misread word',cc=True,ch=False,crop='11_cancelled_application',bbox=[305,1521,1210,1615])
diff('Cancelled L’application: final d/de',r'de',r'd',r'\unsure{d|de}','The terminal small oval and tall right stem give d. A possible e cannot be separated from the long cancellation stroke to its right.','low','other',cc=True,crop='11_cancelled_application',bbox=[1255,1512,1357,1575])
diff('Paragraph placement around cancelled attempts',r'\deleted{On \unsure{définit}} \deleted{L\'application du cosupport de} On',r'\struck{\ill{}}\par\struck{L\'application de cosupport d}\par On',r'\deleted{On \unsure{définit}} \deleted{L\'application de cosupport \unsure{d|de}} On','The cancelled second attempt occupies one manuscript baseline; the replacement On begins immediately on the next close baseline. No additional paragraph gap separates these attempts.','medium','insertion or placement',crop='12_desidentifie',bbox=[315,1515,1355,1665])
diff('Live verb before Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\ill{}',r'\unsure{désidentifie}','One connected word-sized group begins d-é/s-like strokes, has another d loop internally, and ends in a tall f and dotted i. No gap or length supports two complete words délibérément identifie. The compressed medial sequence remains uncertain.','medium','readable ink left as \\ill{}','yes',cc=True,crop='12_desidentifie',bbox=[501,1570,855,1665])
diff('Preposition following second Sigma',r'de',r'à',r'de','A low oval joins a tall loop and horizontal exit; this is the same d-plus-e structure as nearby de, without a detached accent.','high','misread word',crop='12_desidentifie',bbox=[1045,1575,1133,1635])
diff('Cancelled glyph after Sigma de',r'\deleted{$\unsure{\mathcal F}$}',r'\struck{\ill{}}',r'\deleted{$\unsure{\mathcal F_2|\mathcal F_0|\mathcal F|\mathscr P}$}','Crossing oblique strokes cover an upright with a broad upper portion. At its lower right is a small 2-like or looped component. It may be an index, a terminal flourish or cancellation debris; omitting it without doubt is unsafe.','low','misread symbol or index','yes',cc=True,crop='12_desidentifie',bbox=[1167,1558,1264,1646],math=True)
diff('After cancelled glyph: ses deux',r'ses deux',r'un \ill{}',r'ses deux','The first group starts with an angular s and two low returns; the following d loop, low eu sweep and separate x give deux.','high','misread word','yes',crop='12_desidentifie',bbox=[1280,1555,1568,1627])
diff('Before parenthesis: réalisations',r'\unsure{réalisations}',r'\ill{}',r'\unsure{réalisations}','The r/é opening, tall l, dotted i and t/ion ending are visible; several low medial strokes remain compressed.','medium','readable ink left as \\ill{}','yes',crop='13_realisations_P1',bbox=[322,1653,628,1747])
diff('comme partie(s)',r'\unsure{partie|parties}',r'partie',r'\unsure{partie|parties}','The final low dark stroke follows the dotted i but does not separate e from a possible added s.','medium',crop='13_realisations_P1',bbox=[987,1642,1182,1737])
diff('First power-set-style capital',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\mathfrak{P}',r'\unsure{P|\mathscr P|\mathcal P}','The first sign has a straight upright, broad angular upper bowl and no certain lower flourish. Plain P is allowed; a Gothic construction or characteristic Weierstrass curl is not established.','medium','misread symbol or index',cc=True,crop='13_realisations_P1',bbox=[1272,1625,1336,1719])
diff('Argument of first P',r'M',r'\mathcal{M}',r'M','Two plain angular peaks lie inside the parentheses; no separate script alphabet is indicated.',kind='misread symbol or index',crop='13_realisations_P1',bbox=[1317,1625,1410,1718])
diff('Second power-set-style capital',r'\mathscr P',r'\mathfrak{P}',r'\mathscr P','The upright has a broad angular bowl and a long looped lower return to the left, supporting a script P locally.',kind='misread symbol or index',crop='14_P2_sigma_display',bbox=[328,1740,433,1840])
diff('Argument of second P',r'\mathcal F',r'\mathfrak{F}',r'\unsure{\mathcal F|F}','The small F has two separated cross-strokes and a stem; its compressed top does not securely separate plain from calligraphic form.','medium','misread symbol or index',cc=True,crop='14_P2_sigma_display',bbox=[440,1742,536,1825])
diff('After pour sigma in Sigma: comma',r'\sigma\in\Sigma',r'\sigma \in \Sigma,',r'\sigma\in\Sigma','No separate comma follows the final Sigma in the available right-hand clear space.',kind='text not on the page',crop='14_P2_sigma_display',bbox=[1255,1720,1460,1810])
diff('Displayed M sigma: alphabet',r'M_\sigma',r'\mathcal{M}_\sigma',r'M_\sigma','The capital is a plain two-peaked M; the small subscript has a loop and rightward tail.',kind='misread symbol or index',crop='14_P2_sigma_display',bbox=[530,1815,648,1900])
diff('Displayed ambient M: alphabet',r'M',r'\mathcal{M}',r'M','The second M has the same plain peaked form.',kind='misread symbol or index',crop='14_P2_sigma_display',bbox=[705,1810,791,1890])
diff('Display separator following ambient M',r'M\qquad',r'\mathcal{M}, \qquad',r'M,\qquad','A distinct comma descends immediately after M before the second inclusion.',kind='omission',cc=True,ch=False,crop='14_P2_sigma_display',bbox=[768,1823,823,1900])
diff('Displayed family sigma: alphabet',r'\mathcal F_\sigma',r'\mathfrak{F}_\sigma',r'\mathcal F_\sigma','The F has a bent/looped upper bar and a low looped sigma; it is not written with Gothic broken strokes.',kind='misread symbol or index',crop='14_P2_sigma_display',bbox=[876,1793,991,1900])
diff('Rightmost displayed family letter',r'\mathcal F',r'\mathfrak{F}',r'\unsure{\mathcal F|F}','The upper bar lies close to the descender of pour above. The surviving simple stem/crossbar permits calligraphic or plain F locally.','medium','misread symbol or index',cc=True,crop='14_P2_sigma_display',bbox=[1030,1790,1117,1895])
diff('End of displayed inclusions: full stop',r'\mathcal F',r'\mathfrak{F} .',r'\unsure{\mathcal F|F}','There is no detached terminal stop after the rightmost F in the clear space to its right.',kind='text not on the page',crop='14_P2_sigma_display',bbox=[1045,1795,1195,1905])
# Bottom paragraph.
diff('Revised anti compound: lettering and deletion state',r'anti\deleted{\unsure{isomorph|homéo}}\unsure{involution|bijection|dualité}',r'anti\ill{}',r'anti\unsure{\deleted{invo}lution|involution|bijection|dualité}','After anti there is one dense word-sized group, with an overwritten or struck central run and a tall loop plus a tion-like ending. The ink does not recover an independent complete deleted isomorph/homéo followed by a second whole live word. A possibly cancelled invo prefix within the single best-reading involution is shown as an alternative state; the word and state both need adjudication.','low','deletion state (struck given live or live given struck)','yes',cc=True,crop='15_anti_compound',bbox=[945,1960,1458,2060],math=True)
diff('Intersection sentence: M',r'M',r'\mathcal{M}',r'M','The capital before ou de has two plain peaks, with a comma following.',kind='misread symbol or index',bbox=[845,1100,960,1187],source=Z)
diff('Intersection sentence: family letter',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','A long upper bar and curved descending return form the family F before the closing parenthesis.',kind='misread symbol or index',bbox=[1180,1082,1263,1173],source=Z)
# C-doubt dispositions. Every unsure macro in C, plus every context-table row, is covered explicitly.
checks={}
def ck(key,loc,c,r,status,e,crop=None,bbox=None,source=None):
    checks[key]={'location':loc,'c':c,'reading':r,'status':status,'scan_shows':e,'crop':cm[crop]['path'] if crop else None,'bbox':bbox or (cm[crop]['bbox'] if crop else None),'bbox_image':source or (S if crop else A)}
ck('opening','Cancelled opening after de',r'\unsure{``c|``C|``6}',r'\unsure{``c|``C|``6}','retained','Opening raised ticks and inward lower curl survive; the upper outline is crossed.','01_cancelled_opening')
ck('minimale','First paragraph: minimale',r'\unsure{minimale}',r'\unsure{minimale}','retained','The medial minims include a dark knot; the ending is clear.','02_minimale')
ck('celles','Parenthetical initial word',r'\unsure{celles|telles}',r'\unsure{telles|celles}','revised','The tall initial stem and small upper return favour t; c remains possible.','03_parenthesis')
ck('du','Cancelled phrase after qui',r'\unsure{du|de}',r'\unsure{du|de}','retained','A d loop and ascender are visible, but the last low stroke is crossed.','04_cancelled_sappelle')
ck('point','Before operator after L’application',r'\unsure{.}',r'.','resolved','A detached low point is secure.','05_operator',bbox=[765,830,835,895])
ck('cosup','Upper cosupport operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','Only one descending p is written.','05_operator',bbox=[795,817,1010,915])
ck('bij','bijection',r'\unsure{bij\inserted{e}ction}',r'\unsure{bij\inserted{e}ction}','retained','Raised e-like letter is secure as placement; compressed i/e structure is not fully separated.','06_bijection')
ck('saturees','des parties saturées',r'\unsure{saturées|saturée}',r'\unsure{saturées|saturée}','retained','Terminal sweep does not securely separate s.','07_saturees')
ck('sur','Before elles',r'\unsure{sur}',r'sur','resolved','Three small glyph traces give sur.','08_sur_elles',bbox=[330,1073,505,1128])
ck('equals','After elles',r'\unsure{=|mêmes}',r'$=$','resolved','Two separate parallel bars are written; no letters of mêmes are present.','08_sur_elles',bbox=[710,1038,835,1100])
ck('ou','Between de M and cancelled de',r'\unsure{où|ou}',r'où','resolved','Separate diagonal over second vowel supports the accent.','10_ou_F0_cancelled',bbox=[645,1432,737,1503])
ck('cancelde','Before family zero',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','Crossing mass obscures the low ending of the small word.','10_ou_F0_cancelled',bbox=[755,1434,854,1497])
ck('definit','Cancelled On définit',r'\deleted{On \unsure{définit}}',r'\deleted{On \unsure{définit}}','retained','O, d, f descender and terminal t survive; medial ink and accent are struck.','10_ou_F0_cancelled',bbox=[1315,1380,1668,1508])
ck('verb','Live verb before Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\unsure{désidentifie}','revised','One long word-sized group, not two words, begins with d and contains another d before the f/i ending.','12_desidentifie',bbox=[501,1570,855,1665])
ck('crossF','Cancelled glyph after Sigma de',r'\deleted{$\unsure{\mathcal F}$}',r'\deleted{$\unsure{\mathcal F_2|\mathcal F_0|\mathcal F|\mathscr P}$}','revised','A lower-right loop/2-like component must be retained as an index-or-flourish uncertainty.','12_desidentifie',bbox=[1167,1558,1264,1646])
ck('realisations','Before comme',r'\unsure{réalisations}',r'\unsure{réalisations}','retained','Tall l and t/ion ending remain visible; middle low strokes remain compressed.','13_realisations_P1',bbox=[322,1653,628,1747])
ck('partie','comme partie(s)',r'\unsure{partie|parties}',r'\unsure{partie|parties}','retained','The dark final low stroke does not separate a final s.','13_realisations_P1',bbox=[987,1642,1182,1737])
ck('P1','First power-set letter',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\unsure{P|\mathscr P|\mathcal P}','revised','Straight upright and angular bowl permit plain P; no secure Weierstrass form is visible.','13_realisations_P1',bbox=[1272,1625,1336,1719])
ck('anti_deleted','Revised anti compound: alleged deleted word',r'\deleted{\unsure{isomorph|homéo}}',r'\unsure{\deleted{invo}lution|involution|bijection|dualité}','revised','There is one overworked word-sized group. A separate full deleted word is not recovered; the possible cancellation is kept within the same word candidate.','15_anti_compound',bbox=[1090,1960,1458,2060])
ck('anti_live','Revised anti compound: surviving word',r'\unsure{involution|bijection|dualité}',r'\unsure{\deleted{invo}lution|involution|bijection|dualité}','revised','The best candidate has a tall loop and a tion-like ending, but overwork obscures the middle and its state.','15_anti_compound',bbox=[1090,1960,1458,2060])
ck('sigma','On désigne and displayed subscripts',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma','resolved','Capital Sigmas have angular horizontal arms; the lower sigma and both subscripts have a small loop and rightward tail, distinct from zero.',bbox=[525,619,1437,801],source=Z)
ck('Pboth','Two power-set letters',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\unsure{P|\mathscr P|\mathcal P}(M),\quad\mathscr P(\unsure{\mathcal F|F})','revised','The first P is upright/angular without a certain lower flourish; the second has a clear leftward loop at its foot. The two local forms receive separate certainty dispositions.','13_realisations_P1',bbox=[1272,1625,1410,1719])
checks['Pboth']['additional_evidence']={'crop':cm['14_P2_sigma_display']['path'],'bbox':[328,1740,433,1840],'bbox_image':S}
ck('InfSup','Bottom paragraph: Inf and Sup',r'\mathrm{Inf},\mathrm{Sup}',r'\mathrm{Inf},\mathrm{Sup}','resolved','Inf has a barred capital I and a long descending f; Sup begins with a full capital S. No change is needed.',bbox=[345,1040,900,1248],source=Z)
ck('ens','l’ens des parties, l’ens des supports, d’ens. ordonnés',r'ens; ens; ens.',r'ens; ens; ens.','resolved','Both l’ens groups end without a detached point; d’ens. has a separate visible full stop.','06_bijection',bbox=[820,930,1018,1017])
checks['ens']['additional_evidence']=[{'source':Z,'bbox':[1200,101,1440,184]},{'crop':cm['15_anti_compound']['path'],'source':S,'bbox':[350,2055,520,2130]}]
ck('pointop','Point and operator together',r'\unsure{.}\ \unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'.\ \operatorname{cosup}','resolved','The low detached point and the single p descender are each visible.','05_operator',bbox=[765,817,1010,915])
ck('F0M','After inserted M zero: family zero de M',r'M_0\text{ de }M,\quad\mathcal F_0\text{ de }M',r'M_0\text{ de }M,\quad\mathcal F_0\text{ de }M','resolved','Both final M forms have two clear peaks. The last is followed by a point; the visible M is not replaced by F.','10_ou_F0_cancelled',bbox=[910,1380,1256,1498])
C_D=[]
for n,key in enumerate(['opening','minimale','celles','du','point','cosup','bij','saturees','sur','equals','ou','cancelde','definit','verb','crossF','realisations','partie','P1','anti_deleted','anti_live'],1):
    row=dict(checks[key]); row['origin']='C.tex'; row['source_check']=f'C-UNSURE-{n:02d}'; C_D.append(row)
contextkeys=['sigma','Pboth','InfSup','ens','cosup','opening','minimale','celles','du','bij','saturees','sur','equals','cancelde','definit','verb','crossF','realisations','Pboth','anti_deleted','anti_live','pointop','ou','partie','F0M','equals']
for n,key in enumerate(contextkeys,1):
    row=dict(checks[key]); row['origin']='C_context.md'; row['source_check']=f'C-CONTEXT-ROW-{n:02d}'; C_D.append(row)
# Every physical unit, including graphic leader and uncertain correction state.
I=[]
def inv(element,kind,pos,words): I.append({'element':element,'kind':kind,'position':pos,'first_words_or_objects':words,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('Manuscript page number','text','top centre, y 25–90','67')
inv('Cancelled opening sentence','deletion','upper line, y 80–125','On a une notion de …')
inv('First prose paragraph','text','upper half, y 135–1210','Toute partie de …')
inv('Cancelled s’appelle phrase','deletion','inside first paragraph, y 400–448',"s'appelle du/de")
inv('Raised letter in bijection','insertion','above j-to-c junction, x 430–463, y 946–990','e-like letter')
inv('Second prose paragraph','text','middle-lower page, y 1210–1810','On désigne par Σ …')
inv('Added M zero','insertion','left of de M, x 220–315, y 1430–1490',r'M_0')
inv('Curved oblique insertion leader, R1-F1','drawing','left of de, x 294–339, y 1445–1516','non-arrow diagonal from below-left toward raised M zero')
inv('Cancelled small de','deletion','before family zero, x 770–845, y 1440–1490','de')
inv('Cancelled sentence beginning On','deletion','right end of line, x 1325–1650, y 1400–1495','On définit')
inv('Cancelled cosupport application sentence','deletion','full line, x 323–1340, y 1520–1608',"L'application de cosupport d/de")
inv('Cancelled mathematical glyph','deletion','after second Σ de, x 1180–1250, y 1570–1640','F with lower-right index/flourish uncertainty')
inv('Paired inclusions','display','lower middle, x 535–1100, y 1810–1895',r'M_\sigma\subset M,\quad\mathcal F_\sigma\subset\mathcal F')
inv('Final prose paragraph','text','bottom, y 1905–2340','Dans Σ …')
inv('Cancelled pour','deletion','after Dans Σ, x 792–926, y 1928–1960','pour')
inv('Overworked anti compound','deletion','inside last paragraph, x 1100–1440, y 1970–2050','one word with uncertain partial cancellation/overwriting state')
# Remaining doubts are local, with no implied theorem verification.
R=[]
def doubt(loc,r,alts,conf,reason):R.append({'location':loc,'reading':r,'alternatives':alts,'confidence':conf,'reason':reason})
doubt('Cancelled opening final glyph',r'``c',[r'``C',r'``6'],'low','The strike removes the upper distinguishing outline; only a lower curl remains.')
doubt('minimale',r'minimale',[],'medium','Dark joined minims are not individually separable.')
doubt('Parenthetical telles/celles',r'telles',['celles'],'medium','Tall initial stem favours t, but rounded entry also permits c.')
doubt('Cancelled s’appelle du/de',r'du',['de'],'low','The ending lies under the cancellation stroke.')
doubt('Accent of upper definit',r'definit',['définit'],'medium','No separate acute stroke over e is secure in the framed crop.')
doubt('bijection and raised e',r'bij\inserted{e}ction',[],'medium','The added e-like form is visible; the compressed i/e structure around the j join is not fully distinct.')
doubt('Plural ending of upper saturées',r'saturées',['saturée'],'medium','The final horizontal sweep can hide or constitute a final s.')
doubt('Cancelled de before family zero',r'de',[],'low','Heavy crossing ink obscures the final low character.')
doubt('Cancelled On définit',r'définit',[],'medium','The medial and accent strokes are partly obliterated by several horizontal strikes.')
doubt('End of cancelled L’application sentence',r'd',['de'],'low','The possible e is merged with the long deletion line.')
doubt('Live verb before Sigma',r'désidentifie',[],'medium','One word is present, but the small medial sequence is compressed.')
doubt('Cancelled glyph following Sigma de',r'\mathcal F_2',[r'\mathcal F_0',r'\mathcal F',r'\mathscr P'],'low','The lower-right 2-like component may be an index, a flourish or cancellation debris; upper form is crossed.')
doubt('réalisations',r'réalisations',[],'medium','Several medial low strokes do not separate clearly.')
doubt('comme partie(s)',r'partie',['parties'],'medium','The black final stroke can include an s.')
doubt('First P alphabet',r'P',[r'\mathscr P',r'\mathcal P'],'medium','Straight upright and angular bowl are secure, but alphabet identity is not.')
doubt('F argument of second P',r'\mathcal F',[r'F'],'medium','The small top and middle bars lack a decisive local flourish.')
doubt('Final F in inclusion display',r'\mathcal F',[r'F'],'medium','Close approach of the upper text’s descender obscures the top-bar form.')
doubt('Single revised anti compound',r'anti\deleted{invo}lution',[r'antiinvolution',r'antibijection',r'antidualité'],'low','The group is heavily overwritten; neither the exact middle letters nor a distinct cancelled substrate is securely recoverable. The alternatives express a possibly cancelled prefix inside one word, not two asserted complete words.')
N=[
{'sign':'Family F','latex':r'\mathcal F','appearance':'Bent or looped top and curved stem in the large clear occurrences; two compressed occurrences retain local plain-F alternatives.','location':'upper paragraph; family zero; display; bottom paragraph','alternatives':[r'F at P argument and final displayed occurrence only']},
{'sign':'Ambient M','latex':r'M','appearance':'Two plain peaks with a long initial approach; no separate script alphabet.','location':'all M occurrences, including inserted M zero','alternatives':[]},
{'sign':'Sigma and small sigma','latex':r'\Sigma,\sigma','appearance':'Angular upper/lower arms for capital; loop with a rightward tail for lowercase and subscripts.','location':'definition, pour sigma, inclusions, bottom paragraph','alternatives':[]},
{'sign':'Zero index','latex':r'_0','appearance':'Low closed oval distinct from the sigma loop with tail.','location':'raised M zero and family zero','alternatives':[]},
{'sign':'First P','latex':r'\unsure{P|\mathscr P|\mathcal P}','appearance':'Straight upright and broad angular bowl without secure lower flourish.','location':'first parenthesized power-set expression','alternatives':[r'\mathscr P',r'\mathcal P']},
{'sign':'Second P','latex':r'\mathscr P','appearance':'Broad bowl and a leftward lower loop.','location':'second parenthesized power-set expression','alternatives':[]},
{'sign':'Cosupport operator','latex':r'\operatorname{cosup}','appearance':'One descending p stroke; a separate low point stands before the operator.','location':'L’application sentence','alternatives':[]},
{'sign':'Literal repetition mark','latex':r'=','appearance':'Two separate approximately parallel horizontal strokes.','location':'after elles','alternatives':[]},
{'sign':'Inf and Sup','latex':r'\mathrm{Inf},\mathrm{Sup}','appearance':'Capital initial letters; f in Inf has a long low return.','location':'last two manuscript lines','alternatives':[]},
{'sign':'Curved insertion arm','latex':r'\figure{...} (R1-F1)','appearance':'Oblique slightly curved stroke rising from below-left of de, with no arrowhead.','location':'raised M zero','alternatives':[]}
]
report={
'reader':'R1','cote':'156-4','scan':'068','brief_version':'v04','started_utc':'2026-11-20T10:18:56Z','finished_utc':datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
'image_views':[S,A,Z],'reading_file':str(B/'reading.tex'),'differences':D,'c_doubts':C_D,'inventory':I,'remaining_doubts':R,'notation':N,
'abbreviations':[{'form':'resp','expansion':'respectivement'},{'form':'ens','expansion':'ensemble'},{'form':'ens.','expansion':'ensembles (in d’ens. ordonnés)'},{'form':'cosup','expansion':'cosupport'},{'form':'Inf','expansion':'infimum / infima'},{'form':'Sup','expansion':'supremum / suprema'}],
'notes':{
'summary':'One handwritten page with manuscript number 67, three prose blocks, one paired inclusion display, seven ordinary cancelled passages/words, a raised letter in bijection, and a raised M zero with a distinct curved leader. The dense anti compound has an uncertain cancellation/overwriting state. All words, small signs and graphic states included in the fragment were inspected on the full-resolution halves and, where open, in own crops.',
'math_reading_decisions':'No mathematical proof was undertaken. Graphic comparison, not an assumed cosupport theorem, decided the single-p operator, literal equals mark, sigma-versus-zero forms and inclusion directions. Mathematical context identified the anti compound as consequential but did not settle its ink. The apparent family-zero de M wording is preserved. Two compressed F forms retain local alphabet doubts rather than inheriting the clearer nearby forms.',
'author_checks':'The manuscript itself contains several cancelled starts and a heavily revised compound. No explicit author verification mark or independent proof check is added. The small lower-right component of the cancelled symbol after Sigma de is retained as an index/flourish uncertainty. The anti compound is treated as one word-sized group; no complete deleted substrate is asserted outside its uncertainty alternatives.',
'	title_dates_pagination'.strip():'Manuscript page number 67 is visible at the top. No title, date, separate archive corner number, stamp or typed text is visible. The final parenthesis and sentence remain open at the bottom edge; no closing text is supplied.'
},
'check_events':[],'crops':crops,
'workflow_feedback':['The packet’s full-resolution halves have 1681 pixels across. Enlarging a long crowded line to 2500 pixels still leaves the cancelled lower-right component and anti compound ambiguous; the one-crop rule is respected and these remain unresolved. Crop 06 includes the full raised e target but clips the extreme bottom of the j loop by a few pixels; no absence or complete tail-shape claim is based on that crop. The half-a view supplied the complete loop.','The report schema has no dedicated correction-overwriting state separate from deletion; the anti compound is explicitly described as an uncertain state and its alternatives remain within one word-sized group.'],
'structural_checks':{'compiler_invoked':False,'ocr_used':False,'outside_research_used':False,'delegation_used':False,'whole_views':1,'half_a_views':1,'half_b_views':1,'own_crop_views':15,'all_crops_viewed_once':True}
}
def clean_strings(value):
    if isinstance(value,str): return value.replace("\\'","'")
    if isinstance(value,list): return [clean_strings(x) for x in value]
    if isinstance(value,dict): return {k:clean_strings(v) for k,v in value.items()}
    return value
report=clean_strings(report)
# Scope the preposition-only difference to the actual disputed word.
for row in report['differences']:
    if row['location']=='Cancelled L’application: preposition before cosupport':
        row.update(c='du',h='de',reading='de')
    if row['location']=='Paragraph placement around cancelled attempts':
        row['change_c']=True
        row['scan_shows']+=' The lexical changes contained in this complete placement snippet are separately itemized; C already has the retained paragraph placement.'
(B/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Inspection log is ordered by actual successful tool displays. The three source images were never re-displayed.
lines=['# R1 inspection log — 156-4 scan 068','', 'Start recorded: 2026-11-20T10:18:56Z.','', 'The packet metadata, C.tex, H.tex, CONVENTIONS.md, PREAMBLE.tex, C_context.md, brief_v04.md and the supplied notation snapshot were read before the image sequence. No other reader files or pages were opened.','', '## View order','',f'1. Whole: {S} — once, untransformed; layout and all blocks inventoried.',f'2. Half a: {A} — once, untransformed; upper lines compared word by word with both witnesses.',f'3. Half b: {Z} — once, untransformed; lower lines, display and corrections compared with both witnesses.','']
evidence={
'01_cancelled_opening':'Opening ticks and c/C/6 curl remain unresolved; page number 67 clear.',
'02_minimale':'Medial minims remain compressed; retain minimale doubt.',
'03_parenthesis':'Tall initial favours telles but celles remains possible. No separate comma after closing parenthesis.',
'04_cancelled_sappelle':'d loop excludes a confident le; terminal u/e remains under strike.',
'05_operator':'Low point and single-p cosup are clear. No separate acute over e of definit is secure.',
'06_bijection':'Raised e-like glyph above j-to-c join; retain lettering uncertainty. No stop after ens. Framing limitation: the extreme lower edge of the j loop is clipped by a few pixels; the raised-letter target is complete and the complete j was already visible in half a.',
'07_saturees':'Final s cannot be separated from low sweep; preserve plural/singular alternatives.',
'08_sur_elles':'sur is legible; literal double-bar equals and following comma are clear.',
'09_M0_leader':'Plain M zero raised at left; separate curved oblique leader has no arrowhead. Rendered in R1-F1.',
'10_ou_F0_cancelled':'Detached accent in où; cancelled de uncertain; family zero de plain M retained; cancelled On définit partly legible.',
'11_cancelled_application':'de before cosupport; terminal d/de not fully separable from strike.',
'12_desidentifie':'One word-sized désidentifie candidate; de and ses deux clear; cancelled glyph has uncertain lower-right loop/2-like part.',
'13_realisations_P1':'réalisations and partie(s) remain doubtful; first P can be plain/script/calligraphic; M plain.',
'14_P2_sigma_display':'Second P has lower loop; sigma and inclusion signs clear; comma after M visible; no added comma after Sigma or stop after final F. Two small F alphabets uncertain.',
'15_anti_compound':'One densely overwritten word-sized group after anti; possible cancellation of part of the best-reading involution remains uncertain. No independently recoverable complete deleted word.'}
for n,c in enumerate(crops,4):
 name=Path(c['path']).stem
 lines.extend([f"{n}. {c['path']}",f"   Source: {c['source']}",f"   Original bbox: {c['bbox']}; scale: {c['scale']:.8f}; rotation: {c['rotation']} degrees.",f"   Transformations: {'; '.join(c['transformations'])}.",f"   Visible evidence: {evidence[name]}"])
lines.extend(['','## Final checks','','No OCR, text recognition, web research, LaTeX compiler, other-reader inspection or delegation was used. All 15 own crops were displayed once in five batches of three; none was truncated. No decided place was recropped. Crop source coordinates are in the whole image; non-crop differences identify half a or half b explicitly. Structural checks only were performed on the fragment and JSON. No mathematical assertion was proved, so check_events is empty.'])
(B/'inspection_log.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'differences':len(D),'c_doubts':len(C_D),'inventory':len(I),'remaining_doubts':len(R),'crops':len(crops)},ensure_ascii=False))
