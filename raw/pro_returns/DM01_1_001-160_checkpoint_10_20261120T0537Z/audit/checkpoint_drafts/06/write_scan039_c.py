import json
from pathlib import Path
rows=[
 {'id':'M0807','scan':39,'decision':'undecided','reading':r'E_{\unsure{n}}','what the ink shows':'The capital E has an upright and three rightward bars. Its low following index is overrun by zigzag cancellation, so the n cannot be isolated securely.','crop':[1135,1450,1230,1600],'confidence':'low'},
 {'id':'M0808','scan':39,'decision':'undecided','reading':r'\unsure{{}^2}','what the ink shows':'A compact raised residue remains after the final norm, with a short descending/slanted return. The thick cancellation also crosses the preceding index and conceals the upper curve and foot needed to identify 2.','crop':[1135,1450,1230,1600],'confidence':'low'},
 {'id':'M0809','scan':39,'decision':'undecided','reading':r'\illegible{1}','what the ink shows':'Two heavy horizontal swipes and rising diagonals cover the word body; a curved left return and one central ascender survive, but no complete letter sequence can be separated.','crop':[1415,1550,1610,1615],'confidence':'low'},
 {'id':'M0810','scan':39,'decision':'undecided','reading':r'\unsure{en conc}lut','what the ink shows':'The ending l-u-t survives as an upright, a broad lower return and a terminal cross-stem. The preceding en conc bodies are fused into the thick horizontal strike.','crop':[510,1885,837,1942],'confidence':'low'},
 {'id':'M0811','scan':39,'decision':'first','reading':'En posant','what the ink shows':'The initial E has a detached upper stroke, followed by the low connected n; the next word begins with a descending p and retains compact rounded and horizontal strokes through osant before the large deletion loop.','crop':[490,2295,680,2385],'confidence':'medium'},
 {'id':'M0812','scan':39,'decision':'undecided','reading':r'\unsure{\left(\sum\rho_n(u)^p\right)^{1/p}}=\unsure{\|u\|_p}','what the ink shows':'One sum-shaped glyph, one baseline rho and a following u remain at left, and the two equals strokes remain separate. Large looping cancellation masks the grouping and raised powers, and crosses parts of the right norm and its index.','crop':[650,2300,1280,2460],'confidence':'low','candidates':[r'\left(\sum\rho_n(u)^p\right)^{1/p}=\|u\|_p']},
 {'id':'M0813','scan':39,'decision':'undecided','reading':r'Les \unsure{deux théorèmes}','what the ink shows':'The initial tall L and small connected es traces remain, followed by a d ascender and a separate tall stem at the third word. The long deletion line swallows the middle bodies needed to establish deux théorèmes.','crop':[390,2445,835,2525],'confidence':'low'},
 {'id':'M0814','scan':39,'decision':'undecided','reading':r'\illegible{1}','what the ink shows':'A tall T-like upright and short hooked fragments extend above and below two crossing strokes. The following letter bodies are merged into the cancellation and cannot be segmented.','crop':[820,2445,1010,2535],'confidence':'low'},
 {'id':'M0815','scan':39,'decision':'alternative','reading':'ky-Fan','what the ink shows':'The first letter has a straight ascender and a small rounded shoulder at its foot, the minuscule k form. The following y descends well below it; F has two separate rightward arms.','crop':[836,2510,982,2568],'confidence':'medium','candidates':['Ky-Fan','ky-Fan']},
 {'id':'M0816','scan':39,'decision':'first','reading':'m+n+1','what the ink shows':'The final separator before the separate upright 1 has a compact horizontal body and a short downward projection, supporting a small plus. The m and compressed n occupy the same subscript baseline; there is no raised exponent here.','crop':[1060,2465,1230,2514],'confidence':'medium','candidates':['m+n+1','m+n-1']},
 {'id':'M0817','scan':39,'decision':'first','reading':'m+n+1','what the ink shows':'Before the upright 1, the broader horizontal arm has a short descending middle stroke, comparable to the small plus in the right-hand indices. The preceding n is a separate low arch after the first plus.','crop':[1060,2514,1230,2560],'confidence':'medium','candidates':['m+n+1','m+n-1']},
 {'id':'M0818','scan':39,'decision':'first','reading':'<','what the ink shows':'Two arms meet at a leftward point. There is blank paper immediately below them, with no separate lower equality bar; the distant horizontal line is the surrounding box.','crop':[1310,2510,1395,2565],'confidence':'high','candidates':['<',r'\leq']}
]
views=[{'path':'source/DM01_1_001-160_scans/1_scan039.jpg','box':[0,0,1768,2602],'scale':1,'contrast':1,'purpose':'Locate assigned lower-page marks.'}]
items=[
 ('807_809',(340,1420,1730,1640),2,1,'Locate crossed infimum index, raised numeral and deleted word.'),
 ('810',(370,1840,1140,1950),3,1,'Inspect deleted en conclut and insertion context.'),
 ('811_814',(380,2285,1320,2530),2,1,'Inspect deleted En posant, formula and following phrase.'),
 ('815_818',(820,2445,1680,2580),3,1,'Inspect name case, both subscripts and lower relation.'),
 ('807_808_detail',(1135,1450,1230,1600),6,1,'Separate the crossed E index and raised numeral residue.'),
 ('809_detail',(1415,1550,1610,1615),5,1,'Inspect remaining letter strokes under dense cancellation.'),
 ('811_detail',(490,2295,680,2385),4,1,'Resolve initial E, n, p and the following compressed sequence.'),
 ('812_detail',(650,2300,1280,2460),3,1,'Count surviving baseline glyphs separately from masked powers.'),
 ('813_814_detail',(390,2445,1010,2535),3,1,'Inspect first word and the crossed following word bodies.'),
 ('816_817_detail',(1060,2465,1230,2560),6,1,'Check each final sign before 1 for a vertical projection.'),
 ('815_detail',(836,2510,982,2568),5,1.3,'Distinguish the low k shoulder and y descent.'),
 ('810_detail',(510,1885,837,1942),4,1.3,'Check the surviving lut ending against obscured preceding bodies.'),
 ('816_818_compare',(1040,2450,1660,2580),4,1,'Compare small plus strokes with adjacent right-hand indices and inspect <.')]
for name,box,scale,contrast,purpose in items:
 views.append({'path':f'work/scan039_c_views/{name}.png','box':list(box),'scale':scale,'contrast':contrast,'purpose':purpose})
report={'scan':39,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan039_c','started_utc':'2026-11-20T01:46:24.781869+00:00','finished_utc':'2026-11-20T01:49:32Z','rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Compact small plus with downward stem','marks':['M0816','M0817'],'description':'Both final subscript signs have a short horizontal body with a lower projection; the neighboring right-hand index plus signs on this page provide a visible local comparison.'}],'notes':'Actual source dimensions are 1768 x 2602. Personally inspected every assigned mark without OCR. M0816/M0817 were sent to root for targeted independent sign checks; this records my own initial reading. M0812 retains uncertain grouping and powers because deletion merges those distinctions, while the equals sign is secure. No unmarked correction established.'}
p=Path('work/scan039_c.json'); p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(str(p)); print({k:sum(r['decision']==k for r in rows) for k in ['first','alternative','other','undecided']})
