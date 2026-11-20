import json
from pathlib import Path
rows = [
 ('M1327','alternative','(1)','The raised group has a curved opening parenthesis, one thick straight upright 1, and a curved closing parenthesis. The central stroke lacks the bent head and lower return needed for 2.',[600,560,700,620],'high'),
 ('M1328','undecided',r'\unsure{rang} f','The final isolated f has a tall rising stroke, crossing arm and long lower hook, followed by blank paper rather than ini. The preceding proposed word rang is crossed by two dense horizontal strokes; its internal letters cannot all be distinguished.',[570,635,830,720],'low'),
 ('M1329','undecided',r'\unsure{peut}','Between the clear il and following se, a descending p-like stem and a terminal rising stroke survive. The cancellation absorbs the middle joins, so the complete proposed word peut remains unverified.',[635,1055,1020,1165],'low'),
 ('M1330','alternative','convenable','The canceled word ends with two rising strokes and a rounded rightward e return consistent with ble. Its low rounded opening and extended joined middle favor convenable; no final crossed t of commutait is visible.',[1260,1025,1645,1100],'medium'),
 ('M1331','undecided',r'\unsure{certain}','A low opening curve, a central upright, one detached dot and a short final horizontal body survive in this word. The crossing line conceals the intervening letters and exact ending, so certain is retained as uncertain.',[325,1125,575,1210],'low'),
 ('M1332','undecided',r'\unsure{espace}','The word has an initial e-like loop, a separate small s-like remnant and a clear descending p. The following low letter bodies merge into the strike, preventing independent verification of the complete espace ending.',[570,1125,875,1210],'low'),
 ('M1333','undecided',r'\unsure{tel}','Immediately before the following dont is a tall narrow stroke with a low rightward return. The deletion crosses the short preceding and following joins, so three distinct letters t, e and l cannot be established.',[750,1125,875,1210],'low'),
 ('M1334','first','Alors','The inserted word starts with a pointed capital A and crossbar, followed by a tall looped l, compact o, short r shoulder and final s return. The upper-line descender and two cancellation strokes cross it without removing that sequence.',[635,1090,830,1165],'medium'),
 ('M1335','undecided',r'\unsure{tel}','In the inserted line after un, the surviving piece has a descending slant and an adjoining horizontal body. Multiple cancellation lines obscure its top and continuation; the remnant does not establish either the entire proposed tel or an isolated replacement letter.',[1110,1080,1390,1210],'low'),
 ('M1336','first',r'u^{-1}(0)','The baseline u is followed above by a separate minus stroke and upright 1. At baseline the opening parenthesis curves into a small oval 0, and a separate curved closing parenthesis follows; both parentheses are present.',[1430,1240,1630,1335],'high'),
 ('M1337','first',"l'image",'The opening has a tall l with a high adjoining apostrophe flick, followed by a dotted i. The compressed middle runs into a long descending g and a rightward terminal e hook, supporting the complete word.',[995,1325,1225,1410],'medium'),
 ('M1338','alternative','invarie','The underlined word begins with a dotted i, then low n/v forms, a rounded a and r shoulder, a second dotted i and terminal e. Its dotted initial and lack of an opening co loop distinguish invarie from conserve.',[1050,1450,1460,1555],'high'),
 ('M1339','undecided',r'd\unsure{i}','A small closed lower loop with a tall ascender establishes the initial d beneath the insertion arrow. The neighboring short body is overstruck, and no independent i stem or dot can be isolated.',[860,1550,965,1625],'low'),
 ('M1340','first',r'\}','Immediately after E with its lower 1 is a separate right closing brace: its upper inward hook, central outward notch and lower inward return are visible. This is the whole literal brace candidate from the balanced source macro.',[750,1660,820,1755],'high'),
 ('M1341','alternative',r'$\Lambda E$','The canceled group contains two oblique arms meeting in a Λ apex, followed by a separate upright E with top, middle and bottom bars. Both baseline symbols are visible beneath the diagonal and horizontal strikes, excluding E or F alone.',[340,1740,565,1850],'high'),
 ('M1342','first',r'0\leq p\leq n','Below the summation sign are a rounded 0, an angle with lower bar, a narrow p stem with right-hand loop, a second angle with lower dot-like bar, and a final low n. The photo edge crowds the p descender, but those five components remain distinguishable.',[1285,2100,1435,2162],'medium')
]
views = [
 ('page_half',(0,0,1679,2162),.5,1,'Locate assigned body marks on this page.'),
 ('upper',(280,545,1645,760),2,1.4,'Superscript and first crossed rank fragment.'),
 ('draft',(300,980,1645,1270),2,1.5,'Locate every word in the layered canceled draft.'),
 ('lower',(320,1260,1645,2160),1.3,1.35,'Locate inverse, image, invariant word and lower formulas.'),
 ('lambda_index',(550,550,775,635),4,1.2,'Resolve both parentheses and the central digit.'),
 ('rang_fragment',(540,640,825,710),4,1.25,'Check terminal f and obscured preceding word.'),
 ('inserted_draft',(855,1010,1645,1110),2.5,1.2,'Separate upper insertion and its canceled final word.'),
 ('draft_words',(315,1075,990,1255),2.5,1.2,'Separate baseline certain, espace and tel.'),
 ('alors_tel',(640,1090,1630,1160),2,1.2,'Locate inserted Alors and word after un.'),
 ('draft_verb',(635,1060,1020,1135),3,1.15,'Check remnants of peut between il and se.'),
 ('convenable',(1260,1025,1645,1100),3,1.25,'Discriminate the canceled word ending ble from tait.'),
 ('draft_baseline',(320,1130,1645,1210),2,1.15,'Inspect word boundaries throughout canceled baseline.'),
 ('inserted_tel',(1110,1090,1380,1175),4,1.15,'Inspect full surviving inserted tel region.'),
 ('inverse',(1430,1240,1630,1335),4,1.25,'Count u, minus, 1 and parenthesized zero.'),
 ('invarie',(1050,1450,1460,1555),3,1.25,'Distinguish dotted initial and internal letters.'),
 ('deleted_di_brace',(350,1530,820,1760),2.5,1.2,'Inspect lower formula and literal closing brace.'),
 ('deleted_formula',(340,1740,565,1850),4,1.2,'Count both canceled baseline symbols Λ and E.'),
 ('lower_limit',(1180,2075,1665,2162),3,1.2,'Inspect complete lower summation limit at page edge.'),
 ('deleted_di',(575,1540,980,1640),3,1.2,'Separate canceled di from inserted word and arrow.'),
 ('image_word',(1000,1320,1220,1415),3,1.2,'Inspect the whole l’image word.'),
 ('lower_limit_detail',(1285,2100,1435,2162),5,1.15,'Count both inequalities and each lower-limit letter.'),
 ('upper_rank_full',(300,635,830,720),2.5,1.1,'Confirm word boundary and blank space after f.'),
 ('draft_each_words',(325,1125,1120,1210),3,1.1,'Check certain, espace and tel as separate words.'),
 ('certain_detail',(325,1125,575,1210),4,1,'Check hidden middle and exact certain ending.'),
 ('espace_tel_detail',(570,1125,875,1210),4,1,'Separate espace remnants from following tel.'),
 ('alors_detail',(635,1090,830,1165),4,1,'Trace all five letters of inserted Alors.'),
 ('deleted_di_detail',(860,1550,965,1625),5,1,'Discriminate visible d from unverified following i.'),
 ('image_word_raw',(995,1325,1225,1410),5,1,'Check high apostrophe flick, i dot and final g/e.'),
 ('image_context',(540,1305,1240,1425),3,1,'Compare adjacent l’ beginnings on this same line.')
]
report = {
 'scan':67,
 'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan067_c',
 'started_utc':'2026-11-20T04:46:56+00:00',
 'finished_utc':'2026-11-20T04:51:17+00:00',
 'rows':[{'id':i,'scan':67,'decision':d,'reading':r,'what the ink shows':e,'crop':b,'confidence':c} for i,d,r,e,b,c in rows],
 'views':[{'path':'work/crops/scan067_c/'+n+'.png','box':list(b),'scale':s,'contrast':c,'purpose':p} for n,b,s,c,p in views],
 'other_errors':[],
 'patterns':[{'name':'Dense cancellation can leave a recognisable fragment without settling a word','marks':['M1328','M1329','M1331','M1332','M1333','M1335','M1339'],'description':'Several parallel strikes preserve tall ascenders, descenders or dots while covering low joins and endings. M1328 settles only the isolated f; M1339 settles only d. The remaining proposed whole words retain uncertainty.'}],
 'notes':[
  'Assigned M1327–M1342 only. Actual image dimensions are 1679 × 2162. All current-page source mark boundaries were read before evaluating outside errors; no outside error is proposed.',
  'M1340 uses the actual balanced source macro \\unsure{\\}} documented in deliverable/audit/SOURCE_ANOMALIES.md, not the truncated MARKS.tsv representation.',
  'Existing deleted, inserted and underlined layers remain supplied by the unchanged source wrappers. M1334 and M1335 are the inserted line inside the larger deleted passage; no neighboring words are included in their replacements.',
  'M1327 checks three formula components; M1336 checks six; M1340 checks one literal brace; M1341 checks two symbols; M1342 checks five lower-limit components. M1337 includes its apostrophe. Each asserted lexical word is assessed separately in its row.',
  'The whole words rang, peut, certain, espace and the two distinct tel occurrences remain unverified. M1339 leaves its second letter uncertain. No hidden letter or punctuation count is claimed as established for those spans.',
  'A peer check was requested from the coordinator for M1327, M1330 and M1335. This initial report records only my own views and decisions.',
  'The half-size locator is 839 × 1081 pixels after integer rounding. Reported crop boxes always use original source pixels. The elapsed review interval includes reading and annotation, not continuous active image inspection.'
 ]
}
for p in ['work/scan067_c.json','work/scan067_c.initial.json']:
 Path(p).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(Counter(r['decision'] for r in report['rows']))
print('rows',len(report['rows']),'views',len(report['views']))
print('work/scan067_c.json')
