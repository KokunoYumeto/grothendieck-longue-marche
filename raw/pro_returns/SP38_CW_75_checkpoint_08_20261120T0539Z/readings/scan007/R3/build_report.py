from pathlib import Path
from datetime import datetime,timezone
import json
out=Path('out/readings/scan007/R3')
state=json.loads((out/'work_state.json').read_text())
meta=json.loads(Path('packets/scan007/metadata.json').read_text())
findings=[]
def add(id,place,c,h,final,evidence,confidence,kind,marked_in_H,diff_c,diff_h,bbox,crop='',doubt_action='',math_note=''):
 findings.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked_in_H,diff_c=diff_c,diff_h=diff_h,bbox=bbox,crop=('readings/scan007/R3/'+crop+'.png') if crop else '',doubt_action=doubt_action,s_id='',math_note=math_note))
add('F01','Opening word',r'\uline{connexe}',r'\emph{Contour}',r'\uline{connexe}','Upper half: low connected c-on-n-e-x-e sequence; no tall t or terminal r of Contour. The separate underline is retained.','high','misread word',False,False,True,[274,70,478,126])
add('F02','Opening quoted expression',r"``revient au $=$''",r'« revient au $\equiv$ »',r"``revient au $=$''",'Upper half: two short high ticks at each end, and two horizontal equality strokes, not three.','high','misread symbol or index',False,False,True,[709,64,1098,123])
add('F03','Opening bound after n in N',r'n\geq\unsure{2|?}',r'n\geq2',r'n\geq2','The enlarged bent numeral has a lower returning tail and no separate question-mark dot. The following detached descending stroke is the comma.','high','misread symbol or index',False,True,False,[385,132,681,214],'01_opening_bound','resolve','The later bound does not decide this glyph; this resolution is based on the crop.')
add('F04','After savoir S comma',r'S, ou',r'S, --',r'S, \unsure{ou|--}','Two very reduced horizontal strokes: the first may be a flattened o and the second a compressed u, but closed letter shapes are absent. Retain both word and dash readings.','medium','other',False,True,True,[1364,137,1632,225],'14_savoir_ou','retain')
add('F05','Before choix on third line',r'A au choix',r'A -- \uncertain{choix}',r'A \unsure{au|--} choix','Choix is legible, including the h ascender, i dot and crossed x. The two low preceding strokes allow au or dashes; syntax does not decide them.','medium','other',True,True,True,[285,222,654,302],'15_au_choix','retain')
add('F06','Map name in NB',r'\unsure{\sigma|r}:S\longrightarrow A',r'\sigma:S\to A',r'\unsure{\sigma|r}:S\longrightarrow A','The leading sign has a small dark low hook and flat rightward top. Its loop is not sufficiently closed to exclude r. Colon and rightward arrow are clear.','medium','misread symbol or index',False,False,False,[677,220,1004,299],'02_map_name','retain')
add('F07','First superscript on G and its repetitions',r'G^{\unsure{0|\circ}}',r'G^0',r'G^{\unsure{0|\circ}}','The small elevated rounded loop is nearly circular and slightly open at its top. Its shape does not determine numeral zero versus circle. Mark once, then use the primary reading at subsequent occurrences.','medium','misread symbol or index',False,False,False,[283,305,677,378],'03_group_superscript','retain')
add('F08','End of first paragraph',r'u_{\unsure{\omega|w}}',r'u_\omega',r'u_\omega','The enlarged subscript has two rounded lower lobes with an inward turn at the right; it is omega rather than an angular w.','high','misread symbol or index',False,True,False,[1014,305,1265,382],'04_omega_subscript','resolve')
add('F09','Underline in Se donner sentence',r'\uline{contour connexe}',r'contour \emph{connexe}',r'\uline{contour connexe}','Upper half: one continuous horizontal stroke begins beneath the latter part of contour and extends beneath connexe. Preserve the continuous span over the adjacent words. The distinction is underline scope, not the choice of LaTeX emphasis command.','medium','other',False,False,True,[834,425,1240,499])
add('F10','Item 1 group abbreviation',r'\unsure{gpe|grpe}',r'groupe',r'\unsure{gpe|grpe}','A long descending initial g is followed by a highly compressed bridge and return. There are no separate ou loops; a reduced r cannot be excluded.','medium','abbreviation expanded or spelling modernised',False,False,True,[471,567,1064,659],'05_group_abbreviation','retain')
add('F11','Item 2 canceled word before partie',r'\deleted{\unsure{ens|un}}',r'\struck{\ill{}}',r'\deleted{\unsure{ens|un}}','The cancellation crosses a short initial curved form and several low humps. Ens remains the preferred reading, with un possible; the ink supports candidates rather than a blank.','low','readable ink left as \\ill{}',True,False,True,[578,652,957,737],'06_deleted_word','retain')
add('F12','Item 2 cancellation and following de la forme',r"\deleted{formée d'} de la forme",r'\struck{formée} de $2$ \ill{} de la forme',r"\deleted{formée d'} de la forme",'Upper half: the horizontal cancellation includes formée and the following d apostrophe. The live sequence after it is de la, with forme at the start of the next line; there is no additional live numeral 2 and unreadable word before de la forme.','high','deletion state (struck given live or live given struck)',True,False,True,[1139,655,1515,735])
add('F13','Word générateur',r'générateur',r'\emph{générateur}',r'générateur','The supposed underline returns continuously leftward from the descending initial g. No independent underline is visible beneath the word.','high','other',False,False,True,[1100,728,1635,805],'07_generateur')
add('F14','Parenthesis between items 2 and 3: placement',r'\inserted{(\unsure{donc} partie de card $2$ \unsure{sss|ss} $n\ne2$)}',r'(des parties de card $2$ ssi $n\neq2$)',r'\inserted{(\unsure{donc|des} partie de card $2$ \unsure{sss|ssi|ss} $n\ne2$)}','The smaller writing is fitted between the full-sized item-2 continuation and item 3; both parentheses belong to this compact added sentence. It is an insertion into item 2, not a full-sized continuation. Wording differences are itemized separately below.','high','insertion or placement',False,False,True,[540,745,1382,898],'08_inserted_parenthesis','',r'The stated n\ne2 condition is consistent with the cardinality of the inverse pair; see M01.')
add('F15','First word in inserted parenthesis',r'\unsure{donc}',r'des',r'\unsure{donc|des}','The d ascender is clear but its following low stroke is highly compressed. Donc is favored; des cannot be excluded from the remaining ink.','medium','misread word',False,True,True,[611,788,733,841],'08_inserted_parenthesis','retain')
add('F16','Partie in inserted parenthesis',r'partie',r'parties',r'partie','The terminal e is a small detached rounded trace with no following independent s.','high','misread word',False,False,True,[737,793,918,842],'08_inserted_parenthesis')
add('F17','Shorthand after card 2',r'\unsure{sss|ss}',r'ssi',r'\unsure{sss|ssi|ss}','Three tightly connected movements favor sss; the last could be an undotted i, and merging of the first movements leaves ss possible. No separate terminal-i dot is established.','medium','misread word',False,True,True,[1115,793,1183,846],'08_inserted_parenthesis','retain','The logical meaning is compatible with an iff statement, but that does not choose the written abbreviation.')
add('F18','First bullet opening',r'Du moins si $n\geq3$',r'On suppose si $n\geq3$',r'Du moins si $n\geq3$','Upper half: initial D with short u, followed by the low sequence moins and then si; no letter sequence suppose is present.','high','misread word',False,False,True,[319,934,788,1011])
add('F19','Canceled word after n >= 3',r'\deleted{\unsure{sinon|si on}}',r'\struck{\ill{}}',r'\deleted{\unsure{sinon|si on}}','The long strike crosses a readable initial s, an i dot and compressed following humps. The canceled middle cannot separate sinon from si on.','low','readable ink left as \\ill{}',True,False,True,[806,931,1149,1017],'09_deleted_sinon','retain')
add('F20','Second bullet continuation',r'générale, il faut de plus se donner, en lieu du $2^{\circ}$, un',r'générale, il faut se donner, au lieu de 2°), un',r'générale, il faut de plus se donner, en lieu du $2^{\circ}$, un','Upper half: de plus is present between faut and se donner. The later phrase reads en lieu du; the wrapped reference is 2° followed by comma, not 2° with a closing parenthesis.','high','omission',False,False,True,[308,1017,1620,1184])
add('F21','Item 2 bis abbreviation ens',r'un ens $\Omega$',r'un ens.\ $\Omega$',r'un ens $\Omega$','Lower half: the compressed ens ends in its horizontal tail with no separate following point.','high','other',False,False,True,[717,1183,1023,1252])
add('F22','Item 2 bis elements abbreviation',r'\unsure{élémts|éléts|éléments}',r'éléments',r'\unsure{éléts|élémts|éléments}','The word has tall narrow strokes separated by compressed small forms and a broad terminal return. Éléts best fits the visible short structure; a suppressed m or an extremely compressed full ending cannot be excluded.','medium','abbreviation expanded or spelling modernised',False,True,True,[1023,1171,1526,1256],'10_elements_abbreviation','retain')
add('F23','Horizontal separator below item 2 bis',r'\begin{center}\rule{1cm}{.35pt}\end{center}',r'[no separator]',r'\begin{center}\rule{1cm}{.35pt}\end{center}','Lower half: a single blue horizontal rule separates the list from the closing summaries.','high','omission',False,False,True,[837,1509,946,1554])
add('F24','First closing summary: singular forms',r'Contour orienté (...) $=$ ensemble sur lequel',r'Contours orientés (...) $=$ ensembles sur lesquels',r'Contour orienté (...) $=$ ensemble sur lequel','Lower half: there are no final s strokes after Contour, orienté, ensemble, or lequel. Preserve the singular forms. The parenthetical words are treated in F25.','high','misread word',False,False,True,[332,1570,1544,1777])
add('F25','First closing summary parenthesis',r'(pas \unsure{néc.|néc} connexe)',r'(\uncertain{non} \uncertain{connexes})',r'(pas néc. connexe)','Pas is followed by the shortened néc. A small detached blue point stands immediately after the c, distinguishable from its stroke. Connexe has no final s.','high','misread word',True,True,True,[732,1569,1233,1670],'11_nec_punctuation','resolve')
add('F26','After i.e in closing parenthesis',r'\unsure{avec|ou}',r'\uncertain{avec}',r'\unsure{avec|ou}','The small oval and separated low strokes favor avec, but the middle and ending are too compressed to exclude ou.','medium','misread word',True,False,False,[1031,1685,1143,1744],'12_automorphism_parenthesis','retain')
add('F27','Closing abbreviation autom',r'autom',r'\uncertain{autom.}',r'autom','The sequence has the a loop, tall crossed t and low final letters; no detached full stop follows its final horizontal tail.','high','other',True,False,True,[1181,1672,1381,1749],'12_automorphism_parenthesis')
add('F28','Final variable in closing parenthesis',r'\unsure{$u$|$n$}',r'\ill{}',r'\unsure{$u$|$n$}','The small single letter has a low cup-like portion and final descending exit. It favors u but n remains possible. A dark point beneath it is not securely separable from the letter/ink trace and is not promoted to punctuation.','medium','readable ink left as \\ill{}',True,False,True,[1367,1670,1443,1735],'12_automorphism_parenthesis','retain')
add('F29','Closing i.e punctuation',r'i.e',r'i.e.',r'i.e','The point between i and e is present. The e exits into a long continuous tail; no detached terminal point follows it.','high','other',False,False,True,[938,1687,1017,1749],'12_automorphism_parenthesis')
add('F30','Last summary before equals',r'Contour (pas néc connexe)',r'Contours (non \uncertain{connexes})',r'Contour (pas néc connexe)','Lower half: singular Contour; pas then a separate abbreviated néc, then singular connexe. The second néc has no secure detached terminal point.','high','misread word',True,False,True,[333,1811,1053,1910])
add('F31','Final trace after equals',r'\unsure{\ldots|un}',r'\dots',r'\unsure{\ldots|un}','Two short separated low strokes precede a longer nearly horizontal trace. Ellipsis is preferred, but a highly flattened un is still possible. No further text follows.','low','other',False,False,False,[965,1809,1210,1897],'13_closing_trace','retain')

def inv(element,kind,position,first,hand='his hand'):
 return dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
 inv('Opening paragraph with underlined initial words and NB map','text',[274,64,1645,383],'connexe orienté; n in N; Z/nZ; sigma:S to A; G^0; u_omega'),
 inv('Above-line addition with connector to before torseur','insertion',[844,111,951,193],'tel'),
 inv('Introduction to connected-contour data','text',[309,424,1572,559],'Se donner un contour connexe équivaut : la donnée de'),
 inv('Item 1','text',[471,565,1443,663],'1°) un gpe/grpe cyclique G^0'),
 inv('Item 2 main two-line statement','text',[472,660,1637,808],'2°) une ... partie de G^0 ... de la forme {g,g^-1}'),
 inv('Canceled short word after une','deletion',[702,674,785,710],'ens/un'),
 inv('Canceled construction before live de la','deletion',[1144,667,1364,727],"formée d'"),
 inv('Small interlinear parenthetical addition to item 2','insertion',[614,792,1358,854],'(donc/des partie de card 2 sss/ssi/ss n != 2)'),
 inv('Item 3','text',[496,830,1118,897],'3°) Un torseur S sous G^0'),
 inv('First bullet line','text',[220,934,1650,1017],'Du moins si n >= 3 ... ; pour une description'),
 inv('Canceled word within first bullet','deletion',[878,949,1018,994],'sinon/si on'),
 inv('Second bullet and wrapped 2° reference','text',[215,1020,1625,1184],'générale, il faut de plus se donner, en lieu du 2°, un'),
 inv('Replacement item 2 bis across three lines','text',[332,1182,1623,1450],'2 bis) un ens Omega à deux éléts/élémts/éléments; Omega -> G; i(a)i(b)=1'),
 inv('Short blue separating rule','display',[837,1509,946,1554],'horizontal separator'),
 inv('First concluding summary across two lines','text',[330,1572,1541,1780],'Contour orienté (pas néc. connexe) = ensemble sur lequel Z opère'),
 inv('Second unfinished concluding summary','text',[333,1811,1210,1910],'Contour (pas néc connexe) = .../un'),
 inv('Archive foliation recorded only in a TeX comment','margin note',[47,2257,104,2333],'6','unnamed hand')
]
notation=[
 dict(sign='N, Z',reading=r'\mathbb{N},\mathbb{Z}',ink='Parallel extra strokes give double-stroke number-set capitals. Plain G, S and A have no corresponding doubling. H bold number-field encoding is treated as equivalent.',place='Opening quotient, its repetition, closing Z action'),
 dict(sign='Equality and quotation ticks',reading=r"``revient au $=$''",ink='Two equality bars; paired detached high ticks, not guillemets.',place='Opening line'),
 dict(sign='Map name',reading=r'\unsure{\sigma|r}',ink='Low hook and flat rightward top; closed loop unresolved.',place='NB sigma:S to A'),
 dict(sign='G superscript',reading=r'G^{\unsure{0|\circ}}',ink='Tiny elevated rounded loop, slightly open; subsequent loops use primary 0 after first marked occurrence.',place='First paragraph and items 1–3'),
 dict(sign='omega',reading=r'\omega',ink='Two low rounded lobes with an inward right return.',place='u subscript in first paragraph'),
 dict(sign='Inverse exponent',reading=r'g^{-1}',ink='Short raised horizontal minus followed by a separate slanted one.',place='Item 2 pair'),
 dict(sign='Uppercase Omega',reading=r'\Omega',ink='Tall arch with extended nearly horizontal feet, repeated in map and two-element set.',place='Item 2 bis'),
 dict(sign='Map label',reading=r'\Omega\xrightarrow{i}G',ink='Right arrowhead with dotted i above the shaft; no superscript on G.',place='Item 2 bis'),
 dict(sign='g descender',reading='générateur without underline',ink='The first g returns horizontally to the left at its foot; this continuous letter stroke is not an independent underline.',place='Item 2'),
 dict(sign='sss-like shorthand',reading=r'\unsure{sss|ssi|ss}',ink='Tightly connected small turns, with no secure detached final i dot.',place='Inserted card-2 parenthesis')
]
abbreviations=[
 dict(written='NB',expansion='nota bene'),
 dict(written='i.e. / i.e',expansion='id est'),
 dict(written='gpe / grpe',expansion='groupe; abbreviation form uncertain'),
 dict(written='ens',expansion='ensemble; also a possible reading of canceled ink'),
 dict(written='card',expansion='cardinal'),
 dict(written='sss / ssi / ss',expansion='Logical equivalence shorthand; exact written abbreviation unresolved'),
 dict(written='éléts / élémts',expansion='éléments; exact contraction unresolved'),
 dict(written='gén.',expansion='générateur'),
 dict(written='néc. / néc',expansion='nécessairement'),
 dict(written='autom',expansion='automorphisme')
]
unresolved=[]
for place,reading,alts,conf in [
 ('After savoir S comma','ou','--','medium'),
 ('Before choix','au','--','medium'),
 ('NB map name',r'\sigma','r','medium'),
 ('First G superscript and repetitions','0',r'\circ','medium'),
 ('Item 1 abbreviation','gpe','grpe','medium'),
 ('Item 2 canceled word','ens','un','low'),
 ('Added parenthesis first word','donc','des','medium'),
 ('Added parenthesis shorthand','sss','ssi; ss','medium'),
 ('Canceled word after n >= 3','sinon','si on','low'),
 ('Item 2 bis contraction','éléts','élémts; éléments','medium'),
 ('Closing parenthesis connector','avec','ou','medium'),
 ('Closing parenthesis final variable','u','n','medium'),
 ('After last equals',r'\ldots','un','low')]:
 unresolved.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf))
checks=[dict(statement=r'For a generator g of cyclic order n >= 2, {g,g^{-1}} has cardinality 2 exactly when n != 2.',event_type='symbolic consistency check',reasoning=r'g=g^{-1} is equivalent to g^2=1. Since the order of g is n, this means n divides 2; together with n>=2 it gives n=2. Thus the inverse pair has two distinct elements precisely for n!=2.',outcome='Consistent with the written condition in the added parenthesis. This does not decide its shorthand sss/ssi/ss, nor any uncertain glyph elsewhere.',id='M01'),dict(statement='The proposed two-element Omega formulation retains two elements when n=2.',event_type='boundary-case check',reasoning='For a cyclic group of order 2, its generator is its own inverse. Sending both a and b of a two-element Omega to this generator satisfies i(a)i(b)=1, while the image pair in G has only one element.',outcome='The replacement formulation addresses the order-2 collapse described around the bullets. This is a local consistency check, not a proof of the full contour classification.',id='M02')]
report=dict(scan='007',reader='R3',start_utc=state['start_utc'],end_utc=datetime.now(timezone.utc).isoformat(),images_viewed=meta['images'],reading_file='out/readings/scan007/R3/reading.tex',crop_count=len(state['crops']),findings=findings,inventory=inventory,notation=notation,abbreviations=abbreviations,notes=[
 'Complete handwritten course-manuscript page in his hand, continuing an opening sentence from the preceding page; no other page was inspected. No title or date appears on this sheet.',
 'The page describes connected oriented contours using a cyclic-group torsor, then lists data for a connected contour and revises the second datum by a two-element Omega. Two closing summaries follow a short separator; the last summary stops after a trace read as ellipsis with un possible.',
 'There are three numbered items, a replacement 2 bis item, two bullet marks, two insertions (tel and the small parenthesis), and three cancellations (the short word before partie, formée d\', and sinon/si on). No diagram or pictorial drawing occurs; the separating rule is retained.',
 'The archive pencil 6 is recorded only as a comment, not as manuscript pagination. H page{6} is an editorial archive identifier and is not a collation difference.',
 'No independent authorial doubt word is secure. The opening hook is read as the numeral 2, not an authorial question mark. Parenthetical pas néc./pas néc qualifies connectedness rather than expressing doubt in the reading.',
 'The first opening parenthesis before savoir remains unclosed on the manuscript; no closing parenthesis is supplied.',
 'The two dash-like connectors in the opening are retained with ou/au as primary readings and literal-dash alternatives; grammatical plausibility was not used to erase this uncertainty.',
 'Confidence-only differences against H do not set diff_h. Removal, addition, or alteration of a C doubt marker does set diff_c. Equivalent mathbb/bold number-set macros and standard arrow-length choices are not counted as substantive differences.',
 'S.json contains an empty array, so there were no S rows to confirm or overturn. The packet contains no H_drawings supplement.',
 'All fifteen requested tight crops displayed successfully on their first emission; none was regenerated or reopened. No full page or supplied half was reopened, resized for inspection, or viewed twice. No OCR, web, recognition library, PDF text layer, other reader, or other page was used.',
 'Mathematics was used for the two explicit local checks only. The full asserted classifications and equivariance are transcribed, not independently proved.'
 ],checks=checks,unresolved=unresolved,image_dimensions=state['image_dimensions'],image_check_events=state['image_events'],crop_metadata=state['crops'],s_rows=[],s_disposition='S.json is []; no sweep rows.',validation_events=[])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'findings':len(findings),'inventory':len(inventory),'unresolved':len(unresolved),'crop_count':len(state['crops'])},ensure_ascii=False))
