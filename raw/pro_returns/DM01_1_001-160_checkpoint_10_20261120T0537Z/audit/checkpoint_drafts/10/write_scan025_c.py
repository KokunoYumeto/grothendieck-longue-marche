import json
from pathlib import Path
rows=[
('M0484','first','De plus','A capital D retains its upright and rounded bowl; after the flattened e, the p descends below the strike and the l rises above the connected low us strokes.',[430,1640,685,1712],'medium'),
('M0485','undecided',r'Ainsi, pour que la \unsure{mesure soit}','The initial A, small nsi strokes and comma are visible, followed by the descending p, q and short la group. Several crossing lines merge the bodies of the final two words, so their full sequence remains uncertain.',[710,1598,1710,1697],'low'),
('M0486','first','Ainsi en définitive','Ainsi has a distinct capital A and compact trailing strokes, followed by a separated low en group. The last word preserves the tall d, deep returning f stroke and raised terminal t connection despite its compressed middle.',[530,1705,1135,1800],'medium'),
('M0487','first','comme','The inserted word begins with an open c curve, then a small o and connected low humps, ending in a long rising-and-returning e stroke before the separate underlined c.',[1115,1676,1365,1750],'medium'),
('M0488','first',r'\underline b','The canceled symbol has a tall sloping stem joined to a closed lower bowl, with a separate short underline below; the crossing line cuts the bowl without removing its outline.',[1390,1685,1510,1800],'medium'),
('M0489','undecided',r'\unsure{de}','A left upward hook and a terminal raised hook remain above a broad horizontal cancellation. The intervening body is merged with that line, preventing a secure distinction of the proposed d and e.',[1485,1725,1655,1790],'low'),
('M0490','undecided',r'\unsure{compte} dans un','The first word retains its open c and an upright near its end, but the central letters are buried in the strike. The following d loop and ascender, separated ans traces and two low connected humps of un remain legible.',[380,1810,1125,1885],'low'),
('M0491','undecided',r'\unsure{\mu|\rho}','The measure symbol is reduced to a tiny upright opening hook followed by a nearly flat right stroke. It shows neither a secure closed rho bowl nor a separately identifiable second mu shoulder.',[745,1855,880,1930],'low'),
('M0492','undecided',r'i\in\unsure{\mathcal C|\mathcal E}','After i and the two-bar membership sign, the final character is one tall left-bowed curve with a lower hook, separate middle bar and detached upper-right oblique mark. It differs from the two-legged Omega later on this line, but the C/E distinction remains unresolved.',[915,2125,1110,2220],'low'),
('M0493','first','i','Within the first braces, a separate dot stands above a short stem with a hooked base; it is not the undotted tall t seen in nearby words.',[775,2360,848,2430],'medium'),
('M0494','first','i','The second braced index also has a detached dot above its short stem. The heavily closed lower hook could resemble another letter by itself, but its dotted upper structure supports i.',[963,2370,1026,2440],'medium'),
('M0495','first','qui sont des','Above and around the cancellation, the first group preserves its loop, long low connection and separate i dot; the next has a curved s and an end t hook. The final des remains at the right with a raised loop and short terminal sweep.',[1300,2320,1715,2418],'medium'),
('M0496','first','facteurs','The initial f is crossed by the vertical paragraph cancellation, but the following connected act strokes retain a raised crossed t. The low rounded eurs sequence runs into the closing parenthesis.',[400,2425,742,2510],'medium'),
('M0497','alternative','sont','The word has a separated s curve, a low o/n connection and a sharply raised terminal t. There is no separate i dot or extra e body in the clear space before that terminal, unlike the distinctly dotted soit higher on this page.',[758,2435,934,2502],'medium')
]
views=[
('source/DM01_1_001-160_scans/1_scan025.jpg',[0,0,1764,2596],1,'Locate assigned lower-page marks.'),
('cancel_band',[315,1550,1710,1905],2,'Locate canceled phrases and insertion.'),
('general_band',[370,2110,1735,2585],2,'Read final lines and formula context.'),
('de_plus',[430,1640,685,1712],4,'Check surviving De plus strokes.'),
('ainsi_pour',[710,1598,1710,1695],3,'Trace canceled sentence word groups.'),
('ainsi_definitive',[530,1705,1135,1800],3,'Check d, f and terminal of definitive.'),
('insertion',[1115,1676,1655,1810],3,'Read comme, underlined b and de.'),
('compte_mesure',[380,1810,1125,1940],3,'Separate crossed phrase from measure line.'),
('index_membership',[915,2125,1110,2220],4,'Distinguish final membership letter.'),
('formula_indices',[635,2320,1040,2437],4,'Inspect both braced indices and dots.'),
('facteurs_soient',[400,2425,943,2510],3,'Read facteurs and sont/soient shapes.'),
('qui_sont',[1285,2300,1710,2415],3,'Inspect crossed qui sont des.'),
('measure_glyph',[745,1855,880,1930],6,'Test mu shoulder versus rho bowl.'),
('insertion_de',[1485,1725,1655,1790],5,'Inspect de above heavy cancellation.'),
('mesure_soit_cancelled',[1280,1610,1710,1697],4,'Test final canceled word bodies.'),
('comparison_letters',[1275,2140,1645,2410],3,'Compare local Omega and phrase strokes.'),
('soient_detail',[758,2435,934,2502],6,'Test missing i dot and e body.'),
('soit_comparison',[1125,1856,1245,1916],5,'Compare clearly dotted local soit.'),
('de_left_context',[1180,1708,1665,1812],3,'Verify insertion location and canceled de.'),
('qui_deleted_detail',[1300,2320,1715,2418],4,'Check i dot, t hook and final des.')
]
report={
'scan':25,
'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan025_c',
'started_utc':'2026-11-20T00:26:25Z',
'finished_utc':'2026-11-20T00:29:49Z',
'rows':[dict(zip(['id','decision','reading','what the ink shows','crop','confidence'],r),scan=25) for r in rows],
'views':[{'path':p if p.startswith('source/') else f'work/views/scan025_c/{p}.png','box':b,'scale':s,'contrast':1,'purpose':purpose} for p,b,s,purpose in views],
'other_errors':[],
'patterns':[{'name':'Dotted braced i with curled base','marks':['M0493','M0494'],'description':'Both tiny braced indices preserve a detached dot above a short stem, although their lower hooks are broad or closed.'}],
'notes':['Only M0484–M0497 assigned and submitted. All observations came from the scan; no OCR or Hua comparison used.','M0492 was sent for a concrete independent C/E versus Omega check before submission; this initial report does not wait for that check.','Primary elapsed interval includes documentation and report preparation; it is not a claim of uninterrupted active viewing.']}
p=Path('work/scan025_c.json');p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(p)
from collections import Counter
print(dict(Counter(r['decision'] for r in report['rows'])))
