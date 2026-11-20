from pathlib import Path
import json, datetime
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_068/R3')
whole='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan068.jpg'
ha=whole.replace('.jpg','_a.jpg'); hb=whole.replace('.jpg','_b.jpg')
manifest=json.loads((out/'crop_manifest.json').read_text())
by_number={i+1:c for i,c in enumerate(manifest)}
diffs=[]
def D(location,c,h,reading,shows,confidence='high',kind='other',marked=False,cc=False,ch=True,crop=None,bbox=None,half=None,math=False):
    if crop:
        cr=by_number[crop]; path=cr['path']; source=cr['source']; box=bbox or cr['bbox']
    else:
        path=None; source=half or whole; box=bbox
    diffs.append(dict(id='R3-D%02d'%(len(diffs)+1),location=location,c=c,h=h,reading=reading,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h='yes' if marked else 'no',change_c=cc,change_h=ch,crop=path,bbox=box,bbox_image=source,source=source,math_consequential=math))
D('Cancelled opening line, after de',r'\deleted{On a une notion de \unsure{``c|``C|``6}}',r'\struck{On a une notion de \ill{}}',r'\deleted{On a une notion de \unsure{``c|``C|``6}}','A paired high quote-like mark precedes a small inward-curled lower loop under the cancelling stroke. The terminal glyph is not securely distinguished among c, C and 6.','low','readable ink left as \\ill{}',True,crop=1)
D('First live line, family symbol',r'$\mathcal F$',r'$\mathfrak{F}$',r'$\mathcal F$','The F has a long cap and a curved, lower-looped stem; no Gothic broken construction.',kind='misread symbol or index',bbox=[915,125,1000,195],half=ha)
D('First live line, abbreviation resp',r'(resp $M$)',r'(resp. $\mathcal{M}$)',r'(resp $M$)','No detached point separates the ending of resp from M.',kind='abbreviation expanded or spelling modernised',bbox=[1040,125,1345,197],half=ha)
D('First live line, M in parenthesis',r'$M$',r'$\mathcal{M}$',r'$M$','Two plain peaked uprights form M, without a distinct calligraphic flourish.',kind='misread symbol or index',bbox=[1235,125,1345,197],half=ha)
D('Upper paragraph, adjective before parenthesis',r'\unsure{minimale}','minimale',r'\unsure{minimale}','The ending -male is visible; the initial mini strokes coalesce and contain a worked crossing. The full adjective is plausible but not letter-for-letter secure.','medium','misread word',crop=2)
D('Upper paragraph, first word after parmi',r'\unsure{celles|telles}','celles',r'\unsure{celles|telles}','The first tall hooked stroke is unusual for c; no separate decisive t-crossing can be isolated. Two subsequent tall loops and the ending are clear.','medium','misread word',crop=3)
D('Upper paragraph, cancelled phrase after qui',r"\deleted{s'appelle \unsure{du|de}}",r"\struck{s'appelle le}",r"\deleted{s'appelle \unsure{du|de}}",'The final word begins with a small lower loop attached to a tall d-like stem. The cancelling line masks the following vowel; le is not supported.','medium','misread word',crop=4)
D('Upper paragraph, immediately before operator',r"L'application \unsure{.}",r"L'application cosupp",r"L'application .",'A separate low ink point is visible before the operator, with clear white space on both sides.','high','omission',cc=True,crop=5)
D('Upper paragraph, operator after L’application',r'$\unsure{\operatorname{cosup}|\operatorname{cosupp}}$','cosupp',r'$\operatorname{cosup}$','After cosu there is one downstroke and return for p. There is no independently visible second p descender.','high','misread symbol or index',cc=True,crop=5)
D('Upper paragraph, bijection',r'\unsure{bij\inserted{e}ction}','bijection',r'\unsure{bij\inserted{e}ction}','The small e is raised above the join between the long j and the following c. The oblique joining stroke is continuous with the j exit, so no separate insertion arm is asserted here. The compressed full spelling remains uncertain.','medium','insertion or placement',crop=6)
D('Upper paragraph, l’ens des parties',"l'ens", "l'ens.","l'ens",'The wavy ens group ends without a detached point before des.',kind='abbreviation expanded or spelling modernised',crop=7)
D('Upper paragraph, last saturées before sur',r'\unsure{saturées|saturée}','saturées',r'\unsure{saturées|saturée}','The accented stem is visible, but the terminal low sweep does not separate a final plural s from the e-ending.','medium','misread word',crop=7)
D('Upper paragraph, line beginning sur elles',r'\unsure{sur}','sur',r'\unsure{sur}','Three short disconnected traces occupy the position of sur; they fit that reading, but the reduced forms do not settle it completely.','medium','misread word',crop=8)
D('Upper paragraph, after sur',r'elles \unsure{=|mêmes}',r'\ill{}',r'elles $=$','The word elles is followed by two separate near-parallel horizontal bars and then a comma. No letters of mêmes are present.','high','readable ink left as \\ill{}',True,cc=True,crop=8,math=True)
D('Second paragraph, l’ens des supports',"l'ens", "l'ens.","l'ens",'There is no detached abbreviation point between the wavy ens and des.',kind='abbreviation expanded or spelling modernised',bbox=[1205,115,1550,165],half=hb)
D('Second paragraph, raised M0 alphabet',r'\inserted{$M_0$}',r'\add{$\mathcal{M}_0$}',r'\inserted{$M_0$}','The raised symbol has the same two plain M peaks, followed by a round low 0.','high','misread symbol or index',crop=9)
D('Second paragraph, M0 insertion arm',r'\inserted{$M_0$}',r'\add{$\mathcal{M}_0$}',r'Figure R3-M0-insertion in reading.tex: \draw[line width=0.45pt] (0.98,0.50) .. controls (1.00,0.30) and (0.60,-0.05) .. (0.57,-0.27);','A distinct curved oblique stroke descends from beside the raised M0 toward the place before de. It has no visible arrowhead. The word group and the arm are transcribed together once.','high','drawing or diagram',cc=True,crop=9)
D('Second paragraph, first de M after inserted M0',r'de $M$',r'de $\mathcal{M}$',r'de $M$','The capital consists of plain peaked strokes, without a separate script alphabet.','high','misread symbol or index',crop=9)
D('Second paragraph, short word before cancelled de',r'\unsure{où|ou}','ou',r'\unsure{où|ou}','A separate short oblique mark lies over the second vowel; its status as a grave accent remains uncertain. The accent is not supplied from syntax.','medium','misread word',crop=9)
D('Second paragraph, cancelled de before F0',r'\deleted{\unsure{de}}',r'\struck{de}',r'\deleted{\unsure{de}}','The d-like stem survives over a dense cancelling stroke; the rest of the small group is obscured.','low','misread word',crop=9)
D('Second paragraph, F0 alphabet',r'$\mathcal F_0$',r'$\mathfrak{F}_0$',r'$\mathcal F_0$','Long upper and middle arms with a curved stem and a small separate round subscript; no Gothic letterform.','high','misread symbol or index',crop=9)
D('Second paragraph, M after F0',r'$\mathcal F_0$ de $M$',r'$\mathfrak{F}_0$ de $\mathcal{M}$',r'$\mathcal F_0$ de $M$','The final letter has two clear M peaks and a separate period. No readable F is substituted. H’s editorial suggestion to read de F is not adopted.','high','misread symbol or index',crop=9)
D('Second paragraph, cancelled line-end On définit',r'\deleted{On \unsure{définit}}',r'\struck{\ill{}}',r'\deleted{On \unsure{définit}}','The initial On and a following looped d, long f and high final t are visible through several horizontal cancelling strokes. Medial letters are obscured.','medium','readable ink left as \\ill{}',True,crop=10)
D('Second paragraph, cancelled phrase first preposition',r"\deleted{L'application du cosupport de}",r"\struck{L'application de cosupport d}",r"\deleted{L'application de cosupport \unsure{de|d}}",'The short word after application has a d-loop followed by a low e-like exit. The u-return required by du is not independently present.','medium','misread word',cc=True,ch=False,crop=11)
D('Second paragraph, cancelled phrase terminal word',r'cosupport de',r'cosupport d',r'cosupport \unsure{de|d}','The final tall d-like stroke and low loop survive, but the horizontal cancellation merges with the possible e-exit.','low','misread word',cc=True,crop=11)
D('Second paragraph, live verb before Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\ill{}',r'\unsure{désidentifie}','There is one elongated word-sized group beginning with a looped d and an accented small letter, ending with a tall f and short dotted ending. No independent délibérément group or space is visible. The compressed middle leaves désidentifie uncertain.','low','readable ink left as \\ill{}',True,cc=True,crop=12,math=True)
D('Second paragraph, preposition after Sigma',r'$\Sigma$ de',r'$\Sigma$ à',r'$\Sigma$ de','A lower loop, tall upper loop and low right exit form de. There is no isolated accented a.','high','misread word',crop=13,math=True)
D('Second paragraph, deleted symbol after Sigma de',r'\deleted{$\unsure{\mathcal F}$}',r'\struck{\ill{}}',r'\deleted{$\unsure{\mathcal F}$}','One tall stem and transverse strokes are crossed obliquely. The F reading remains uncertain; a low right curl cannot securely be separated as a subscript.','low','readable ink left as \\ill{}',True,crop=13)
D('Second paragraph, ses deux réalisations',r'ses deux \unsure{réalisations}',r'un \ill{}',r'ses deux \unsure{réalisations}','A small s-like opening and low sweep precede a d-loop and the separated terminal x of deux. The following word has the tall and dotted groups of réalisations, but its compressed medial letters remain uncertain.','medium','readable ink left as \\ill{}',True,crop=14)
D('Second paragraph, comme partie(s)',r'\unsure{partie|parties}','partie',r'\unsure{partie|parties}','The final dark horizontal exit may combine e with s; a separate s cannot be secured or excluded.','medium','misread word',crop=14)
D('Second paragraph, first power-set letter',r'$\unsure{\mathscr P|\mathcal P|\wp}(M)$',r'$\mathfrak{P}(\mathcal{M})$',r'$\unsure{\mathscr P|\mathcal P|\wp}(M)$','Tall upright with a broad angular bowl and extended top cap. The specific script/calligraphic encoding remains uncertain; the shape is not securely Gothic.','medium','misread symbol or index',crop=15)
D('Second paragraph, M within first power-set parentheses',r'$M$',r'$\mathcal{M}$',r'$M$','The enclosed letter has two M peaks. A horizontal stroke crosses the left part, but no separately readable prior capital can be isolated.','medium','misread symbol or index',crop=15)
D('Second paragraph, second power-set letter',r'$\mathscr P(\mathcal F)$',r'$\mathfrak{P}(\mathfrak{F})$',r'$\mathscr P(\mathcal F)$','The second P has a broad angular bowl and a pronounced lower-left curl. The same uncertain alphabet is represented by the first candidate after its first-page occurrence. Crop 16 reaches the bottom of the upright; no absence claim about a further terminal stroke is made.','medium','misread symbol or index',crop=16)
D('Second paragraph, family symbol inside second power-set parentheses',r'$\mathcal F$',r'$\mathfrak{F}$',r'$\mathcal F$','A broad long cap, middle arm and curved stem are visible inside the two closing parentheses.','high','misread symbol or index',crop=16)
D('Second paragraph, after pour sigma in Sigma',r'pour $\sigma\in\Sigma$',r'pour $\sigma \in \Sigma$,',r'pour $\sigma\in\Sigma$','The final Sigma ends without a separate comma before the display. The half includes clear space beyond it.','high','text not on the page',bbox=[1060,620,1510,715],half=hb)
D('Display, both M capitals',r'M_\sigma\subset M',r'\mathcal{M}_\sigma \subset \mathcal{M}',r'M_\sigma\subset M','Both M letters have plain paired peaks. The first has a low looped sigma; the inclusion opens to the right.','high','misread symbol or index',bbox=[525,715,815,800],half=hb)
D('Display, both family capitals',r'\mathcal F_\sigma\subset\mathcal F',r'\mathfrak{F}_\sigma \subset \mathfrak{F}',r'\mathcal F_\sigma\subset\mathcal F','Both F letters have the long cap and middle arm. The first has a low looped sigma, and the inclusion opens to the right.','high','misread symbol or index',bbox=[875,690,1145,800],half=hb)
D('Display, terminal punctuation',r'\mathcal F_\sigma\subset\mathcal F',r'\mathfrak{F}_\sigma \subset \mathfrak{F} .',r'\mathcal F_\sigma\subset\mathcal F','No detached period follows the rightmost F. The visible area to its right is blank.','high','text not on the page',bbox=[1040,690,1260,810],half=hb)
D('Bottom paragraph, worked compound after anti',r'anti\deleted{\unsure{isomorph|homéo}}\unsure{involution|bijection|dualité}',r'anti\ill{}',r'Figure R3-worked-anti in reading.tex: anti\unsure{involution|bijection|dualité} with the overstrike drawn on the same suffix','There is one worked suffix-sized span, with crossing baseline strokes, an initial loop, a tall central loop, a descending middle trace and tall strokes toward the ending. An older complete isomorph or homéo cannot be isolated independently of the surviving word. One uncertain suffix is retained and the visible overstrike is drawn, without a second sequential word.','low','deletion state (struck given live or live given struck)',True,cc=True,crop=17,math=True)
D('Bottom paragraph, M in intersection description',r'de $M$',r'de $\mathcal{M}$',r'de $M$','A plain two-peak M occurs after parties de, followed by a comma.','high','misread symbol or index',bbox=[845,1100,975,1175],half=hb)
D('Bottom paragraph, family symbol in intersection description',r'ou de $\mathcal F$',r'ou de $\mathfrak{F}$',r'ou de $\mathcal F$','The F has a long cap and curved middle/stem, followed by the closing parenthesis.','high','misread symbol or index',bbox=[1175,1080,1295,1165],half=hb)

# Every row of this packet's C_context doubt table is explicitly disposed of.
c_doubts=[]
def CD(row,location,c,reading,status,shows,crop=None,bbox=None,half=None):
    if crop:
        cr=by_number[crop]; path=cr['path']; source=cr['source']; box=bbox or cr['bbox']
    else:
        path=None; source=half or whole; box=bbox
    c_doubts.append(dict(id='R3-C%02d'%row,context_row=row,location=location,c=c,reading=reading,status=status,scan_shows=shows,crop=path,bbox=box,bbox_image=source,source=source))
CD(1,'On désigne, pour sigma, display and bottom occurrences',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma','resolved','Capital Sigma is angular, with long arms and diagonal joining strokes. The low sigma after pour and both display subscripts has a small loop and right exit, unlike the separate round zero in M0/F0.',bbox=[520,105,1460,1000],half=hb)
CD(2,'First power-set letter and recurring second letter',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\unsure{\mathscr P|\mathcal P|\wp}','retained','The first bowl is angular and its upright tall. Script and calligraphic encoding are not securely distinguished. The second has an additional lower-left curl.',crop=15)
CD(3,'Bottom Inf and Sup',r'\mathrm{Inf},\mathrm{Sup}',r'\mathrm{Inf},\mathrm{Sup}','resolved','Inf starts with a barred capital I and ends in a long descending f; Sup begins with a distinct capital S. They are not read as all-lowercase operators.',bbox=[340,1030,540,1240],half=hb)
CD(4,'Both l’ens and final d’ens.',r'ens; ens; ens.',r'ens; ens; ens.','resolved','Neither upper l’ens nor l’ens des supports has a detached terminal point. In d’ens. ordonnés a distinct point follows ens. Local punctuation is preserved.',crop=7)
CD(5,'Operator after L’application',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','Only one p descender and return is visible at this occurrence. This is a local spelling decision, not normalization from other occurrences.',crop=5)
CD(6,'Cancelled opening line, after de',r'\unsure{``c|``C|``6}',r'\unsure{``c|``C|``6}','retained','Quote-like high strokes and a small inward-curling lower loop survive; the cancellation prevents a secure c/C/6 distinction.',crop=1)
CD(7,'Upper minimale',r'\unsure{minimale}',r'\unsure{minimale}','retained','The inner mini strokes run together and include a crossing; the ending is clearer.',crop=2)
CD(8,'Parenthesis, celles/telles',r'\unsure{celles|telles}',r'\unsure{celles|telles}','retained','The initial hooked tall stroke remains ambiguous; two following tall l-loops are secure.',crop=3)
CD(9,'Cancelled word after s’appelle',r'\unsure{du|de}',r'\unsure{du|de}','retained','The initial lower loop and tall stem are d-like; the cancellation masks the vowel.',crop=4)
CD(10,'Bijection with raised e',r'\unsure{bij\inserted{e}ction}',r'\unsure{bij\inserted{e}ction}','retained','A raised e is secure. The long diagonal is continuous with the j exit, not a separately established arm; the compressed full spelling remains uncertain.',crop=6)
CD(11,'Saturées before sur',r'\unsure{saturées|saturée}',r'\unsure{saturées|saturée}','retained','A straight low finish does not separate final e from possible es.',crop=7)
CD(12,'Sur before elles',r'\unsure{sur}',r'\unsure{sur}','retained','The word comprises three short disconnected traces. Sur is the best reading without a secure complete spelling.',crop=8)
CD(13,'Two bars after elles',r'\unsure{=|mêmes}',r'$=$','resolved','Two near-parallel bars occupy the word space; there is no written mêmes.',crop=8)
CD(14,'Cancelled de before F0',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','A d-like stem is visible above the dense deletion. The e is not independently clear.',crop=9)
CD(15,'Cancelled On définit',r'\deleted{On \unsure{définit}}',r'\deleted{On \unsure{définit}}','retained','Initial On, looped d, long f and high terminal t survive; the middle is crossed repeatedly.',crop=10)
CD(16,'Live verb before Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\unsure{désidentifie}','revised','One word-sized group begins with d and an accented small letter and ends with f and a dotted ending. The proposed two-word expansion lacks a separate group; identifie alone omits the clear initial d. The remaining middle is still uncertain.',crop=12)
CD(17,'Cancelled family sign after Sigma de',r'\deleted{$\unsure{\mathcal F}$}',r'\deleted{$\unsure{\mathcal F}$}','retained','The crossed stem and transverse traces suggest F but do not decide the letter. The lower-right curl is not independently recoverable as an index.',crop=13)
CD(18,'Réalisations',r'\unsure{réalisations}',r'\unsure{réalisations}','retained','The tall and dotted groups fit réalisations, but multiple medial letters are reduced to small traces. Two low ink spots beneath the middle are recorded as unassigned spots, not promoted to punctuation.',crop=14)
CD(19,'Both power-set letters, occurrence-specific check',r'\unsure{\mathscr P|\mathcal P|\wp};\mathscr P',r'\unsure{\mathscr P|\mathcal P|\wp};\mathscr P','retained','The first P is tall and angular; the second has a pronounced lower-left curl. The second crop reaches the terminal upright at its bottom boundary, so no claim that further terminal ink is absent is made. The first occurrence carries the recurring alphabet doubt.',crop=16)
CD(20,'Worked anti suffix, alleged older word',r'\deleted{\unsure{isomorph|homéo}}',r'Figure R3-worked-anti: one overstruck suffix; no separate recovered older word','revised','Crossing strokes cannot be assigned to a complete independent isomorph or homéo. Rendering a separate deleted word followed by a complete live word would overstate the recoverable lettering. The overstrike is drawn on one suffix.',crop=17)
CD(21,'Worked anti suffix, surviving reading',r'\unsure{involution|bijection|dualité}',r'\unsure{involution|bijection|dualité}','retained','Tall loops and an -ion-like ending favour involution as the first candidate, but overlapping traces prevent a secure live spelling. No mathematical expectation decides it.',crop=17)
CD(22,'Point and p count before/within operator',r'\unsure{.} $\unsure{\operatorname{cosup}|\operatorname{cosupp}}$',r'. $\operatorname{cosup}$','resolved','There is a separate low point and one p descender. Their local ink is visible independently of the witnesses.',crop=5)
CD(23,'Où/ou after de M',r'\unsure{où|ou}',r'\unsure{où|ou}','retained','A detached short oblique stroke above the second vowel permits an accent, but its status remains uncertain.',crop=9)
CD(24,'Comme partie(s)',r'\unsure{partie|parties}',r'\unsure{partie|parties}','retained','The terminal dark sweep may represent e or es; no separate s can be isolated.',crop=14)
CD(25,'M0 de M, then F0 de M',r'M_0\text{ de }M,\;\mathcal F_0\text{ de }M',r'M_0\text{ de }M,\;\mathcal F_0\text{ de }M','resolved','The final capital has two plain M peaks and a period. The different F appearing in the display does not authorize correction of this M. H’s editorial emendation is not ink evidence.',crop=9)
CD(26,'Repeated check of elles =',r'elles \unsure{=|mêmes}',r'elles $=$','resolved','The two bars are literal drawn bars, followed by a comma; no letters of mêmes are transcribed.',crop=8)

inventory=[]
def I(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
I('Page number','text','top centre','67')
I('Cancelled initial sentence','deletion','top line beneath page number','On a une notion de ``c/C/6')
I('First prose paragraph','text','upper two-thirds through d’inclusion','Toute partie de F (resp M)')
I('Cancelled s’appelle phrase','deletion','upper paragraph after qui',"s'appelle du/de")
I('Raised e in bijection','insertion','upper paragraph, above j/c join','e')
I('Literal repetition/equality mark','text','upper paragraph after elles','=')
I('Second prose paragraph','text','middle through pour sigma in Sigma','On désigne par Sigma')
I('Underlined supports','text','middle second paragraph','supports — separate underline')
I('Underlined virtuels','text','middle second paragraph','virtuels — separate underline')
I('Raised M0','insertion','left edge of line beginning de M','M0')
I('M0 curved insertion arm','drawing','between raised M0 and de M','curved descending oblique stroke without arrowhead; Figure R3-M0-insertion')
I('Cancelled de','deletion','before F0','de')
I('Cancelled On définit','deletion','right line end after F0 de M.','On définit')
I('Cancelled L’application line','deletion','middle line immediately above live On désidentifie',"L'application de cosupport de/d")
I('Cancelled family letter','deletion','after live Sigma de','F uncertain, crossed obliquely')
I('M_sigma and F_sigma display','display','below second paragraph',r'M_\sigma\subset M,\quad\mathcal F_\sigma\subset\mathcal F')
I('Final prose paragraph','text','bottom, continuing beyond page','Dans Sigma, pour [cancelled] la notion de cosupport')
I('Cancelled pour','deletion','bottom paragraph first line after Sigma','pour')
I('Worked anti suffix overstrike','deletion','bottom paragraph after anti','one worked suffix; older full word unrecoverable')
I('Worked suffix graphic reconstruction','drawing','same anti suffix','overstrike, initial loop and descending trace; Figure R3-worked-anti')

remaining=[
 dict(location='Opening cancelled terminal glyph',reading=r'\unsure{``c|``C|``6}',alternatives=['``C','``6'],confidence='low',reason='Only a small inward-curled loop survives under the strike.'),
 dict(location='minimale',reading=r'\unsure{minimale}',alternatives=[],confidence='medium',reason='Compressed and worked initial mini strokes.'),
 dict(location='celles/telles',reading=r'\unsure{celles|telles}',alternatives=['telles'],confidence='medium',reason='Tall hooked initial without a decisive separate crossbar.'),
 dict(location='Cancelled s’appelle du/de',reading=r'\unsure{du|de}',alternatives=['de'],confidence='medium',reason='Cancellation masks the vowel after d.'),
 dict(location='bijection',reading=r'\unsure{bij\inserted{e}ction}',alternatives=[],confidence='medium',reason='Raised e is clear; the remaining compressed spelling is less secure.'),
 dict(location='saturées/saturée before sur',reading=r'\unsure{saturées|saturée}',alternatives=['saturée'],confidence='medium',reason='The terminal sweep does not separate e from es.'),
 dict(location='sur elles',reading=r'\unsure{sur}',alternatives=[],confidence='medium',reason='Three reduced disconnected traces.'),
 dict(location='où/ou before cancelled de',reading=r'\unsure{où|ou}',alternatives=['ou'],confidence='medium',reason='Small detached high stroke may be an accent.'),
 dict(location='Cancelled de before F0',reading=r'\deleted{\unsure{de}}',alternatives=[],confidence='low',reason='Dense strike leaves only the d-like stem clear.'),
 dict(location='Cancelled On définit',reading=r'\deleted{On \unsure{définit}}',alternatives=[],confidence='medium',reason='Medial letters concealed by repeated horizontal strokes.'),
 dict(location='Cancelled L’application final word',reading=r'\unsure{de|d}',alternatives=['d'],confidence='low',reason='Possible e-exit merges with the cancelling line.'),
 dict(location='Verb before Sigma',reading=r'\unsure{désidentifie}',alternatives=[],confidence='low',reason='One group and its d-/f-ending are clear; medial letters and accent shape remain compressed.'),
 dict(location='Cancelled symbol after Sigma de',reading=r'\deleted{$\unsure{\mathcal F}$}',alternatives=[],confidence='low',reason='Oblique crossings prevent a secure letter or index decomposition.'),
 dict(location='réalisations',reading=r'\unsure{réalisations}',alternatives=[],confidence='medium',reason='Short medial traces remain underdetermined.'),
 dict(location='comme partie(s)',reading=r'\unsure{partie|parties}',alternatives=['parties'],confidence='medium',reason='Dark terminal horizontal exit may combine e and s.'),
 dict(location='Power-set alphabet at first and second occurrences',reading=r'\unsure{\mathscr P|\mathcal P|\wp}',alternatives=[r'\mathcal P',r'\wp'],confidence='medium',reason='Tall angular bowl does not uniquely select a typographical script alphabet; second P has a lower-left curl and a framing limitation at the terminal upright.'),
 dict(location='Worked anti suffix, lettering and state',reading=r'anti\unsure{involution|bijection|dualité} with drawn overstrike',alternatives=['bijection','dualité','An older isomorph/homéo is possible but cannot be isolated as a complete independent word.'],confidence='low',reason='One worked span; baseline crossing and descender overlap the possible live letters. This is the highest-priority adjudication locus.')
]
notation=[
 dict(sign='Family F',latex=r'\mathcal F',appearance='Long cap, middle arm and curved stem; lower loop especially visible in the first occurrence.',location='First line; F0; power-set argument; display; final paragraph',alternatives=[]),
 dict(sign='Ambient M',latex='M',appearance='Two plain peaked uprights.',location='First parenthesis; M0 line; power-set argument; display; final paragraph',alternatives=[]),
 dict(sign='Capital Sigma',latex=r'\Sigma',appearance='Long angular arms connected by diagonal stroke.',location='On désigne; désidentifie; pour; twice in final paragraph',alternatives=[]),
 dict(sign='Lower sigma',latex=r'\sigma',appearance='Low loop and rightward exit.',location='After pour and both display subscripts',alternatives=[]),
 dict(sign='Zero subscript',latex='0',appearance='Small separate round loop.',location='Raised M0 and F0',alternatives=[]),
 dict(sign='Power-set P',latex=r'\unsure{\mathscr P|\mathcal P|\wp}',appearance='Tall upright, wide angular bowl; second occurrence has a pronounced left lower curl.',location='First and second power-set expressions',alternatives=[r'\mathcal P',r'\wp']),
 dict(sign='Local cosup spelling',latex=r'\operatorname{cosup}',appearance='Single clear p downstroke and return.',location='L’application . cosup',alternatives=[]),
 dict(sign='Two-bar mark',latex='=',appearance='Two near-parallel independent bars.',location='After elles',alternatives=[]),
 dict(sign='Inf and Sup',latex=r'\mathrm{Inf},\mathrm{Sup}',appearance='Barred capital I with long f descender; capital S in Sup.',location='Final paragraph',alternatives=[]),
 dict(sign='Subset signs',latex=r'\subset',appearance='Curved signs open to the right.',location='Both display inclusions',alternatives=[]),
 dict(sign='Insertion arm',latex='Figure R3-M0-insertion',appearance='Curved oblique line from beside raised M0 to the place before de; no arrowhead.',location='M0 line',alternatives=[]),
 dict(sign='Worked-word strokes',latex='Figure R3-worked-anti',appearance='Crossing baseline, initial loop and descending mid-word trace occupying the same suffix span.',location='anti compound',alternatives=[])
]
report=dict(reader='R3',cote='156-4',scan='068',brief_version='v04',started_utc='2026-11-20T10:19:08Z',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),image_views=[whole,ha,hb],reading_file=str(out/'reading.tex'),differences=diffs,c_doubts=c_doubts,inventory=inventory,remaining_doubts=remaining,notation=notation,abbreviations=[dict(form='resp',expansion='respectivement'),dict(form='ens',expansion='ensemble'),dict(form='ens.',expansion='ensembles (contextual plural in d’ens. ordonnés)'),dict(form='cosup',expansion='cosupport')],notes=dict(summary='Page 67 is a wholly handwritten prose page about saturated parts and virtual supports. It contains one display, two separately underlined words, several cancellations, a raised e, a raised M0 with a distinct curved insertion arm, and one heavily worked anti suffix. All text has been included; no diagram or marginal sentence is present. Seventeen independent crops were inspected.',math_reading_decisions='No proof or mathematical validation was performed. The subject matter prompted scrutiny of the operator’s p count, the sigma/zero distinction, the final M after F0, and the anti suffix. These decisions rest on local ink. In particular, the later display F_sigma subset F does not license changing the earlier F0 de M. No expected order-theoretic property was used to select the anti suffix.',author_checks='The printed fragment ends mid-parenthesis after « partie saturée ». H’s suggestion to read F in « F0 de M » is editorial and unsupported by the two visible M peaks. The first power-set argument M has a crossing horizontal stroke but no readable independent prior symbol. Two low spots below réalisations have no secure linguistic attachment. Crop 16 reaches the lower upright of the second P at its boundary; this framing limitation is recorded and no absence claim is made. The worked anti suffix is reconstructed graphically on one word span rather than decomposed into two supposedly recovered full words.',title_dates_pagination='Manuscript page number 67 at top centre; scan marker 68 retained. No title or date. « supports » and « virtuels » have separate underlines. No archive sheet number or stamp is visible.'),check_events=[],crops=manifest,workflow_feedback=['The brief does not specify a standard inline encoding for one overwritten word whose older state cannot be separated. This reader uses one uncertain suffix with the visible crossing strokes reproduced in a local TikZ figure and flags the locus for adjudication.','A crop intended to include a long lower curl may still reach the last upright at its boundary. Crop 16 has this framing limitation; it was not recropped and did not settle the remaining alphabet uncertainty.'])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Actual view order: three originals, then crops 01 through 17, each once in batches of at most three.
evidence=[
'Opening loop remains c/C/6; quote-like marks present; whole opening line crossed.',
'Compressed mini group remains uncertain; ending of minimale is clearer.',
'Initial tall hook leaves celles/telles unresolved.',
'Cancelled terminal word begins with d; du/de vowel obscured.',
'Separate low point; only one p descender in cosup.',
'Raised e visible; diagonal continuous with j exit, not established as separate leader.',
'No point after ens; terminal plural s of saturées not separable.',
'Sur reduced; elles followed by two literal bars and comma.',
'M0 raised; separate curved arm without arrowhead; accent-like stroke over ou; cancelled de; final M clear.',
'On and d/f/t framework of définit survive repeated crossing.',
'Cancelled phrase first preposition read de; final de/d remains uncertain.',
'One long word-sized group before Sigma; désidentifie retained uncertain; no independent délibérément group.',
'De after Sigma clear; crossed F uncertain; ses deux visible.',
'Réalisations and partie(s) remain uncertain; two low spots unassigned.',
'First P broad angular bowl; enclosed M has two peaks with crossing horizontal stroke.',
'Second P lower-left curl visible; bottom upright reaches crop boundary, so full terminal form not settled. Family argument visible.',
'One worked anti suffix; overlapping strokes prevent secure older/live word decomposition.']
with (out/'inspection_log.md').open('a') as f:
    for idx,(cr,ev) in enumerate(zip(manifest,evidence),4):
        f.write(f'\n{idx}. Viewed `{cr["path"]}` once. Source `{cr["source"]}`; original bbox `{cr["bbox"]}`; scale `{cr["scale"]:.8f}`; rotation 0°. Transformations: autocontrast, LANCZOS enlargement, unsharp mask radius 1/110%/threshold 3, JPEG quality 94. Evidence: {ev}\n')
    f.write('\nAll seventeen crop images were returned visibly; none was tool-output-truncated. Crop 16 has the stated framing limitation. No image was re-viewed or recropped. Structural checking only followed; no LaTeX compiler or mathematical proof check was run.\n')
print(json.dumps({'differences':len(diffs),'c_context_dispositions':len(c_doubts),'inventory':len(inventory),'remaining_doubts':len(remaining),'crops':len(manifest)},ensure_ascii=False))
