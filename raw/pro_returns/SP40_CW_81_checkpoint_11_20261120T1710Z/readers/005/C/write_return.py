from pathlib import Path
import json
from datetime import datetime, timezone
out=Path('/workspace/scratch/94548b74fbe0/out/readers/005/C')
tex=r'''\scanpage{5}
% Small raised hook with a detached dark dot above the B of NB;
% its reading as a question mark remains uncertain (full scan x225--234, y61--81).
\(\overset{\hspace{0.55em}\unsure{?}}{\text{\uline{NB}}}\)\quad Si $\sigma$ est un
% Detached dot below the middle of automorphisme (full scan x853--859, y168--175);
% retained without an assigned textual function.
\(\underset{\unsure{\cdot}}{\text{automorphisme}}\) du corps des complexes, et si $f$ est ``spécial'', alors $f^\sigma$ est égalmt spécial -- donc $\operatorname{Aut}(\mathbb C)$ opere sur l'ens des $f$ spèciaux. Mais il opère par l'intermédiaire de $\operatorname{Aut}(\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}})$, car si $f=P/Q$ spécial, les coeff. de $P,Q$ sont des \uline{nbs algébriques}. Il revient au $=$ de dire que les zéros de $P,Q$ sont des nbs algébriques, i.e. le diviseur de $f$ est
% Tiny paired dark traces to the right of the last line, slightly above its baseline;
% full scan x858--872, y1258--1267. Their function is uncertain.
\margin{\(\unsure{\cdot\,\cdot|-}\)}

% Isolated lower marks: first dark short rule with a much fainter upper trace;
% then a separate pale shallow arch; then the second dark short rule.
% The first two remain uncertain in function. The arch is a shape candidate.
\[
 \unsure{-|=}\hspace{0.8em}\unsure{\frown|-}\hspace{6em}-
\]
% archive sheet number: 4
'''
(out/'reading.tex').write_text(tex)
D=[]
def add(id, location, C, H, reading, evidence, confidence, kind, diff_C, diff_H, status=None, crop=None, bbox=None, consequence=None):
    d={'id':id,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':diff_C,'diff_H':diff_H,'C_doubt_status':status,'readers_crop':crop,'bbox':{'coordinate_space':'original full scan','xyxy':bbox} if bbox else None}
    if consequence is not None:d['mathematical_consequence']=consequence
    D.append(d)
add('005-C-01','Above the B of NB, line 1',r'\uline{NB}',r'\emph{NB}',r'\overset{\hspace{0.55em}\unsure{?}}{\text{\uline{NB}}}',
    'A pale short hooked stroke lies above a separate dark short dot, both above the right part of NB. A question-mark shape is a candidate; textual intention and authorship of this tiny trace remain uncertain. The single underline below NB is clear.',
    'low','omission',True,True,crop='01_nb_sigma.png',bbox=[217,57,242,86])
add('005-C-02','Line 1, automorphisme',r'\unsure{automorphisme}','automorphisme','automorphisme',
    'The opening oval a, shallow u, tall t, intervening low connections, descending p, tall h, dotted i and final sme strokes are visible. Enlargement supports the full word.',
    'high','other',True,False,'resolved','02_automorphisme.png',[680,86,1134,171])
add('005-C-03','Detached dot below automorphisme, between lines 1 and 2','[absent]','[absent]',r'\underset{\unsure{\cdot}}{\text{automorphisme}}',
    'One small round dark point is visible below the middle of the long word, around (855,172). No attached shaft or neighbouring punctuation fixes its function. The transcription preserves it as an uncertain detached dot, without assigning it to a word.',
    'low','omission',True,True,crop='02_automorphisme.png',bbox=[851,166,862,177])
add('005-C-04','Line 3, after f superscript sigma est',r'\unsure{égalmt|également}','également','égalmt',
    'The acute-accented opening, deep g loop, small a, high l, low contracted continuation and final crossed t-like ending are visible. The ending is contracted; I read mt at the ordinary word level. The supplied expansion également is not written out letter by letter.',
    'medium','abbreviation expanded or spelling modernised',True,True,'resolved','03_superscript_egalmt.png',[1033,280,1184,364])
add('005-C-05','Line 4, immediately after Aut(C)',r'\unsure{opere|opère}','opère','opere',
    'After the detached o and descending p, the low continuous ere strokes have no detached accent above them in the enlarged local field. The second occurrence on line 6 has its own separate descending accent stroke.',
    'high','abbreviation expanded or spelling modernised',True,True,'resolved','04_aut_c_opere.png',[916,375,1040,454])
add('005-C-06','Line 5, l’ens',"l'ens","l'ens.", "l'ens",
    'The last s ends in its downward hook. The blank gap before des contains no period. The period following spèciaux later on the line is a separate visible mark.',
    'high','other',False,True,crop=None,bbox=[150,481,314,548])
add('005-C-07','Line 5, spèciaux',r'\unsure{spèciaux|spéciaux}','spéciaux','spèciaux',
    'The detached accent above the e descends from upper left to lower right. The ending carries a two-legged x-like finish, followed by its own period.',
    'high','abbreviation expanded or spelling modernised',True,True,'resolved','05_speciaux.png',[548,479,753,558])
add('005-C-08','Line 7, barred Q inside Aut',r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}',r'\overline{\mathbb{Q}}',r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}',
    'The bar is distinct. The upper bowl has one visible perimeter. Extra strokes crowd the lower left and crossed tail, but they do not settle whether a deliberately doubled alphabet was intended. Both supplied candidates remain. H’s alphabet is retained among the alternatives, so this row records C-doubt retention rather than a settled H error.',
    'medium','other',False,False,'retained','06_barred_q.png',[302,691,348,765])
add('005-C-09','Line 9, revient',r'\unsure{revient}','revient','revient',
    'The first connected group has low r/e/v-like turns and a detached i dot; the continuation ends in the writer’s crossed t-shaped finish. The whole local sequence supports revient.',
    'medium','other',True,False,'resolved','08_revient_au_equals.png',[786,923,939,966])
add('005-C-10','Line 9, au = de',r'au $=$ de','au même de',r'au $=$ de',
    'Two separate nearly horizontal strokes stand between au and de. Their right ends align; the lower one is darker and slightly curved. The visible token is the equals sign.',
    'high','misread symbol or index',False,True,crop='08_revient_au_equals.png',bbox=[1043,923,1105,956])
add('005-C-11','Right of final line, slightly above est baseline','[absent]','[absent]',r'\margin{\(\unsure{\cdot\,\cdot|-}\)}',
    'Two tiny neighbouring dark points lie in a pale horizontal trace, around (863,1263) and (868,1263). A paired-dot reading is strongest; a very short fragmented rule remains possible. No function is assigned.',
    'low','omission',True,True,crop='09_detached_mark.png',bbox=[855,1256,876,1270])
add('005-C-12','First of the isolated lower dark marks',r'\unsure{-|=}','[absent]',r'\unsure{-|=}',
    'A dark, short, uneven horizontal trace is clear near (375,1427). A much fainter trace sits above it near y1415. The faint upper trace has broken rather than continuous ink, so the candidate equals sign remains unresolved.',
    'low','omission',False,True,'retained','10_lower_left_marks.png',[354,1405,398,1440])
add('005-C-13','Pale trace just right of the first lower dark mark','[absent]','[absent]',r'\unsure{\frown|-}',
    'A separate pale, shallow arch-like trace lies around x427–447, y1419–1427. Its central part rises slightly above the ends. The transcription gives shape candidates only; its status as intentional writing remains uncertain.',
    'low','omission',True,True,crop='10_lower_left_marks.png',bbox=[423,1414,452,1434])
add('005-C-14','Second lower dark mark, to the right',r'-','[absent]',r'-',
    'The supplied lower half shows one short dark nearly horizontal rule near (921,1425), with no separate upper mate visible locally.',
    'high','omission',False,True,crop=None,bbox=[905,1417,938,1437])

inventory=[
{'sheet_kind':'text','hand':'his hand','element':'005.C.01','kind':'text','position':'Twelve physical lines in the upper and middle part of the sheet','first_words_or_objects':'NB Si σ est un automorphisme ... de f est','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.02','kind':'text','position':'Line 1, below NB','first_words_or_objects':'Single underline beneath NB','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.03','kind':'drawing','position':'Above the B in NB; hand attribution uncertain for the trace','first_words_or_objects':'Small pale hook plus detached dark dot; uncertain question-mark candidate','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.04','kind':'drawing','position':'Below automorphisme; hand attribution uncertain for the isolated point','first_words_or_objects':'Detached dark dot','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.05','kind':'text','position':'Line 9, beneath nbs algébriques','first_words_or_objects':'Single underline beneath nbs algébriques','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.06','kind':'margin note','position':'Right of final line, slightly above its baseline; hand attribution uncertain for the marks','first_words_or_objects':'Two tiny points / short fragmented rule','transcribed':'yes'},
{'sheet_kind':'text','hand':'his hand','element':'005.C.07','kind':'display','position':'Below the unfinished prose','first_words_or_objects':'First dark rule with faint upper trace; separate pale arch; second dark rule','transcribed':'yes'},
{'sheet_kind':'text','hand':'another unnamed hand','element':'005.C.08','kind':'text','position':'Bottom left archive numeral','first_words_or_objects':'4, recorded only in archive-sheet comment','transcribed':'yes'}
]

doubts=[
{'location':'Above NB','reading':'?','alternatives':['uninterpreted hook and detached dot'],'confidence':'low','reason':'The shape is visible, but its textual intention and its hand are not established.','crop':'01_nb_sigma.png'},
{'location':'Below automorphisme','reading':r'\cdot','alternatives':['unassigned nontextual point'],'confidence':'low','reason':'Isolated dark point without an attached stroke; retained without semantic assignment.','crop':'02_automorphisme.png'},
{'location':'Aut of barred Q, line 7','reading':r'\overline{\mathrm Q}','alternatives':[r'\overline{\mathbb Q}'],'confidence':'medium','reason':'Extra lower-left and tail strokes leave alphabet choice unresolved.','crop':'06_barred_q.png'},
{'location':'Right of final line','reading':r'\cdot\,\cdot','alternatives':['-'],'confidence':'low','reason':'Tiny separate dark points lie within a faint horizontal trace; function uncertain.','crop':'09_detached_mark.png'},
{'location':'First lower dark mark','reading':'-','alternatives':['='],'confidence':'low','reason':'The much fainter upper trace remains too broken to settle its membership in the sign.','crop':'10_lower_left_marks.png'},
{'location':'Pale trace right of first lower mark','reading':r'\frown','alternatives':['-'],'confidence':'low','reason':'A shallow pale arch is visible; intentional writing and symbol function remain uncertain.','crop':'10_lower_left_marks.png'}
]
notation=[
{'location':'Lines 1 and 3','sign':'small open arched sigma, raised above f at its second occurrence','latex':r'\sigma, f^\sigma'},
{'location':'Line 3 around spécial','sign':'Two short quotation ticks on each side','latex':"``spécial''"},
{'location':'Line 4, Aut(C)','sign':'Capital C with a separate inner left stroke forming a narrow doubled left side','latex':r'\operatorname{Aut}(\mathbb C)'},
{'location':'Line 3, contracted ending','sign':'égalmt, ending on the ordinary word level','latex':'égalmt'},
{'location':'Line 5','sign':'ens without terminal period','latex':'ens'},
{'location':'Line 7','sign':'Separate bar above uncertain alphabet Q','latex':r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}'},
{'location':'Line 7, quotient','sign':'Plain capitals P and Q separated by an oblique slash','latex':r'f=P/Q'},
{'location':'Line 8','sign':'coeff. with visible terminal point','latex':'coeff.'},
{'location':'Line 9','sign':'Two horizontal strokes in running prose','latex':r'au $=$ de'},
{'location':'Lines 9 and 11','sign':'nbs abbreviation','latex':'nbs'},
{'location':'Line 11','sign':'i.e. with its small points','latex':'i.e.'}
]

report={'scan':5,'reader':'C','start_utc':'2026-11-20 10:05:21 UTC','end_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
'image_view_record':{'whole_scan_view_count':1,'half_a_view_count':1,'half_b_view_count':1,'whole_dimensions':[1231,1678],'half_dimensions':[1231,919],'half_a_full_origin':[0,0],'half_b_full_origin':[0,759],'half_b_offset_basis':'Full height 1678 minus lower-half height 919 = 759; matching overlap inspected visually.','crop_count':10,'each_crop_viewed_once':True,'workflow':'Whole scan once for layout; each supplied half once; one enlargement per remaining locus, with adjoining targets sharing crops. No recropping, OCR, external research, other-page images, other-reader files, or delegation.'},
'differences':D,'doubts':doubts,'inventory':inventory,
'notes':[
'One handwritten NB paragraph occupies twelve physical lines. It discusses σ, f^σ, Aut(C), Aut of barred Q, coefficients and zeros of P,Q, and ends at de f est. The unfinished phrase is preserved.',
'No written date, title, or manuscript page number was found. The archive numeral 4 is in the bottom-left corner and appears only as the required comment.',
'No securely read authorial word of uncertainty occurs. The small hook and dot above NB have the uncertain shape candidate ?, without an assertion that Grothendieck placed a doubt sign there.',
'The expanded word également in H is collated against the visible contracted ending égalmt; first opere remains unaccented, while the later opère carries its own grave accent. The plural spèciaux has a downward-to-right accent.',
'Both single underlines are retained: NB and nbs algébriques. H’s emphasis macros carry the same word spans and are treated as emphasis-macro correspondence, not as an independent collation difference.',
'H’s note about the unfinished sentence is editorial apparatus. It supplies no extra manuscript words and is not collated as text not on the page. Its omission of the isolated dark marks is reported separately.',
'C_doubts.txt includes notation/abbreviation and comparison rows. Only the seven actual uncertainty loci in C.tex receive C_doubt_status. In particular au = de is a comparison row, not an invented C doubt.',
'The crop at sont on line 8 supports the live word and its crossed terminal t shape. No distinct cancellation stroke or recoverable replacement was identified there.',
'The isolated tiny marks are preserved conservatively as uncertain marks. Their visibility is reported separately from the unresolved questions of writing intention and hand attribution.',
'Mathematical reading was used only to keep track of the written symbols and quotient. No mathematical repair was made. No proof or calculation was performed.'
],
'notation':notation,'check_events':[],
'crops':json.loads((out/'crop_manifest.json').read_text()),
'brief_feedback':[
'The convention for very small isolated traces whose status as intentional writing is unresolved could be more explicit. I preserved their visible shapes with unsure candidates, stated the uncertainty of intention, and did not call them secure authorial punctuation.',
'No separate requirement in the brief specifies spatial markup for a dot beneath a prose word or an uncertain mark above NB; standard overset/underset preserve those relations in this return.'
]}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
md='''# Scan 005 — independent reader C

## Viewing attestation

Recorded start: 2026-11-20 10:05:21 UTC. I opened the whole image once, half a once, and half b once. I visually read all twelve manuscript lines, their marks, the lower isolated traces, the margins, and the archive numeral. I then viewed each of ten tight enlarged crops once. I did not recrop any locus. No OCR, external source, other page, other reader’s file, or delegation was used.

The full image is 1231 × 1678 pixels. Each half is 1231 × 919. Half b begins at full-image y = 759, obtained from 1678 − 919 and checked against the overlap. All boxes in the report and crop manifest use original full-image coordinates.

## Line-by-line visual audit

| Physical line / place | Reading checked against the ink | Outcome |
| --- | --- | --- |
| 1, y≈60–172 | Underlined NB; Si σ est un automorphisme | Main words readable. The word automorphisme is resolved. A small raised hook-plus-dot above NB remains an uncertain question-mark candidate. A tiny detached point beneath the middle of automorphisme is preserved without assigned function. |
| 2, y≈185–244 | du corps des complexes, et si | All words read; comma after complexes retained. |
| 3, y≈269–360 | f est “spécial”, alors f^σ est égalmt | Both pairs of quotation ticks, acute accent, comma and raised σ checked. Contracted ending read égalmt, with its final crossed t-like stroke at ordinary word level. |
| 4, y≈377–453 | spécial — donc Aut(C) opere sur | The first spécial has its acute accent. The C has a doubled left construction. No accent is visible over the first opere. |
| 5, y≈476–569 | l’ens des f spèciaux. Mais il | No dot follows ens. The plural has a descending-to-right accent, hence spèciaux; its period is distinct. Mais il is readable. |
| 6, y≈589–673 | opère par l’intermédiaire de | Second opère has a separate grave stroke. Apostrophe and the accent in intermédiaire checked. |
| 7, y≈689–793 | Aut(barred Q), car si f = P/Q spécial, | The bar is clear; the Q alphabet remains unresolved. Parentheses, both commas, the two equality strokes, slash, plain P/Q, and final spécial checked. |
| 8, y≈797–905 | les coeff. de P, Q sont des | The period of coeff. and comma after P are visible. Enlarged sont supports live writing with a crossed t-like ending; no separate cancellation was read. |
| 9, y≈918–1028 | underlined nbs algébriques. Il revient au = de | Single underline span, acute accent and final point checked. Revient resolved. Two written horizontal strokes between au and de are retained as =. |
| 10, y≈1035–1154 | dire que les zéros de P, Q sont | Words and acute accent read; comma after P retained. |
| 11, y≈1137–1259 | des nbs algébriques, i.e. le diviseur | Comma, abbreviation points, accent and complete diviseur read. |
| 12, y≈1253–1341 | de f est | The last three words are readable, with no final punctuation supplied. The long connecting stroke into f is preserved through the ordinary text reading; no added arrow or relation is assigned. |
| Right of line 12, x≈858–872, y≈1263 | Two tiny dark points in a pale horizontal trace | Unresolved paired-dot / fragmented-rule shape retained in the margin. Its function is unassigned. |
| Lower left dark mark, x≈359–389, y≈1410–1433 | Short dark rule with a much fainter upper trace | C’s − / = doubt retained. The upper trace remains too broken to settle its role. |
| Immediately right, x≈427–447, y≈1419–1427 | Pale shallow arch-like trace | Added as uncertain shape candidates, with no assertion of intentional writing. |
| Lower right dark mark, x≈911–931, y≈1424 | Short horizontal dark rule | Read as −; H omits it. |
| Bottom left, x≈66–85, y≈1618–1656 | Archive numeral 4 | Recorded only in the archive-sheet comment. |

## Collation outcome

The principal definite readings are **automorphisme**, **égalmt**, **opere** at its first occurrence, **spèciaux**, **revient**, **l’ens** without a dot, and **au = de**. The seven actual C uncertainty loci are all recorded: five resolved and two retained. The retained C doubts concern the barred Q alphabet and the first lower mark. H’s macro-only emphasis correspondence and editorial sentence-end note are not counted as manuscript-text differences.

Several small traces omitted by both witnesses are separately retained with low confidence in their textual status: the hook and dot above NB, the detached point below automorphisme, the paired tiny points beside the last line, and the pale arch near the first lower rule. Their shape evidence and precise locations are in report.json; none is promoted to a secure authorial instruction or mathematical symbol.

## Mathematics and completeness

I followed the symbols and the written quotient while reading. I made no mathematical repair, proof, or calculation; check_events is empty. The complete proposed page is in reading.tex. Every reported added mark is represented there, and all crop references point to the ten existing PNGs listed in crop_manifest.json.
'''
(out/'reading.md').write_text(md)
print(json.dumps({'written':['reading.tex','report.json','reading.md'],'differences':len(D),'actual_C_doubt_rows':sum(d['C_doubt_status'] is not None for d in D),'resolved_C_doubts':sum(d['C_doubt_status']=='resolved' for d in D),'retained_C_doubts':sum(d['C_doubt_status']=='retained' for d in D),'end_utc':report['end_utc']},ensure_ascii=False))
