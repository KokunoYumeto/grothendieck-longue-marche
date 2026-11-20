import json
from datetime import datetime,timezone
root='work/scan025_b_views/'
rows=[
('M0470','first','est','A low horizontal e/s group ends in a separate angular rising t; the cancellation lies above these surviving strokes.',[1510,580,1610,635],'medium'),
('M0471','first','induit','The struck word retains an initial i and dot, a small looped d ascender near its middle, and the upright hooked final t. The intervening low bodies merge with the deletion line.',[1010,650,1205,715],'medium'),
('M0472','first','facteur','The cancelled word preserves the tall initial f, the raised middle t and the low terminal hooked group. The same page’s clear facteur has the corresponding f–t spacing, although cancellation conceals most small counters here.',[1285,715,1465,775],'medium'),
('M0473','undecided',r'\unsure{nombre}','The raised insertion has a long downstroke ending in a small shoulder, then a dot and detached terminal bar. Its o/m/b bodies cannot be separated securely from the horizontal ink above, so the full word versus a contraction remains unsettled.',[1280,675,1435,735],'low'),
('M0474','first','alors','Above the deleted line, a small initial oval is followed by a tall l and a rounded terminal r/s sweep. The insertion arrow remains separate beneath the letters.',[570,940,690,988],'high'),
('M0475','first','cet','After the cancelled E est, the initial open c and low e connection survive, followed by a prominent crossed angular t. The long cancellation merges with the lower letter bodies.',[850,982,995,1045],'medium'),
('M0476','first','algèbre','The compressed word retains its initial rising a/l stroke, the closed descending g loop, an accent above, and a second raised b stroke before the trailing re line.',[1525,940,1695,1015],'medium'),
('M0477','first','auto-adjointe','The insertion shows the separated short auto group, then an a loop, a tall d, a downward j turn and a long terminal ointe connection ending in a pointed t. Its curved insertion line runs below rather than through those letters.',[165,1050,495,1115],'medium'),
('M0478','first','on sait que','Despite the strike-through, the initial o/n loop, the a loop and dotted i of sait, its tall crossed t, and the long q descender of que remain in sequence.',[270,1190,685,1280],'medium'),
('M0479','first','qui se réduit nécessairement','The phrase starts with a descending q and separated i-dot, followed by the short se group. The next compact group retains a dotted middle stroke, and the final long nécessairement group ends in the writer’s angular t; the small interior letters are compressed.',[850,1380,1535,1480],'medium'),
('M0480','undecided',r'\unsure{\mu|\rho}','The measure glyph is a shallow open left curl leading into a long right stroke. There is no secure descending stem or closed rho bowl, so the supplied mu/rho choice is not established; a nu-like reading also remains possible.',[1445,1480,1550,1540],'low'),
('M0481','undecided',r'\illegible{2}','The deleted segment preserves an initial A-like slant with a dot/dash group, then a tall l-like upright and a low right curl. The heavy stroke removes the word bodies, so even the possible Ainsi le recovery is not secure.',[1275,1515,1640,1580],'low'),
('M0482','first','de type I pur','The deleted phrase retains the low de group, the tall t and lower return in type, an isolated upright I with a foot, and the tall p followed by a low ur connection. Several cancellation strokes cross the small bodies but leave those spaced components visible.',[1140,1552,1660,1640],'medium'),
('M0483','first','Ainsi on a','The initial tall triangular A, the later dotted i stroke, a small rounded on group and the terminal short a-like upturn survive along the cancellation. The low n/s connections are partly covered.',[330,1590,710,1650],'medium'),
]
views=[
('source/DM01_1_001-160_scans/1_scan025.jpg',[0,0,1764,2596],1,1,'Locate the fourteen assigned marks.'),
(root+'upper_band.png',[210,550,1730,860],2,1,'M0470–M0473 in line context.'),
(root+'middle_band.png',[170,920,1730,1285],2,1,'M0474–M0478 insertions and cancellations.'),
(root+'lower_band.png',[230,1370,1730,1695],2,1,'M0479–M0483 phrase and deleted lines.'),
(root+'est_detail.png',[1430,555,1630,650],4,1,'M0470 terminal t and low bodies.'),
(root+'induit_detail.png',[900,630,1210,725],4,1,'M0471 dotted i, d ascender and final t.'),
(root+'facteur_nombre_detail.png',[1190,670,1650,800],4,1,'M0472–M0473 overlapping replacement.'),
(root+'alors_cet_detail.png',[530,935,1010,1050],3,1,'M0474–M0475 separate insertion and cancelled word.'),
(root+'algebre_detail.png',[1500,925,1715,1025],4,1,'M0476 g loop, accent and raised b.'),
(root+'auto_adjointe_detail.png',[155,1035,510,1130],4,1,'M0477 middle d/j and terminal t.'),
(root+'on_sait_que_detail.png',[260,1180,700,1290],4,1,'M0478 surviving dots, t and q descender.'),
(root+'qui_phrase_detail.png',[830,1378,1735,1492],3,1,'M0479 word-group order.'),
(root+'measure_deleted_detail.png',[1265,1470,1738,1590],4,1,'M0480–M0481 glyph and cancelled words.'),
(root+'type_pur_detail.png',[1140,1552,1660,1640],4,1,'M0482 surviving word and numeral stems.'),
(root+'ainsi_on_a_detail.png',[300,1565,735,1655],4,1,'M0483 initial A, dot and final groups.'),
(root+'nombre_tight.png',[1280,675,1435,735],6,1,'M0473 full word versus contraction.'),
(root+'phrase_right.png',[1430,1365,1755,1485],4,1,'M0479 boundary and far-right ink.'),
(root+'phrase_middle.png',[840,1385,1540,1480],4,1,'M0479 four compressed word groups.'),
(root+'measure_tight.png',[1445,1480,1550,1540],6,1,'M0480 left bowl and absent secure stem.'),
(root+'deleted_two_words.png',[1275,1515,1640,1580],5,1.5,'M0481 possible partial word recovery.'),
(root+'type_pur_context.png',[1135,1510,1685,1665],3,1,'Separate M0481 and M0482 cancellation strokes.'),
(root+'facteur_comparison.png',[1180,275,1430,355],4,1,'Same-page clear facteur for M0472.'),
(root+'facteur_deleted_tight.png',[1285,715,1465,775],6,1,'M0472 surviving f and middle t.'),
(root+'ainsi_comparison.png',[330,1590,710,1650],5,1,'M0483 and possible M0481 initial comparison.'),
]
report={
'scan':25,
'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan025_b',
'started_utc':'2026-11-20T00:26:21.674083+00:00',
'finished_utc':datetime.now(timezone.utc).isoformat(),
'rows':[dict(zip(['id','decision','reading','what the ink shows','crop','confidence'],r),scan=25) for r in rows],
'views':[dict(zip(['path','box','scale','contrast','purpose'],v)) for v in views],
'other_errors':[],
'patterns':[{'name':'Low compressed groups with distinctive high or low strokes','marks':['M0470','M0471','M0475','M0478'],'description':'This page compresses e/s and connecting bodies into long low strokes; the surviving angular t, dotted i, d loop and q descender provide the specific word evidence.'}],
'notes':['All fourteen assigned IDs were individually inspected; no OCR or text recognition was used. The actual primary interval includes image generation and annotation, not a claim of continuous active reading.','M0473, M0480 and M0481 remain uncertain. Concrete peer concerns were sent before saving; this initial report does not await their outcome.','M0479 was checked as four word groups. The far-right group beyond x1605 was not confidently deciphered, so no unmarked correction is asserted.']
}
with open('work/scan025_b.json','w') as f:json.dump(report,f,ensure_ascii=False,indent=2)
print(report['finished_utc'])
print({k:sum(r['decision']==k for r in report['rows']) for k in ['first','alternative','other','undecided']})
