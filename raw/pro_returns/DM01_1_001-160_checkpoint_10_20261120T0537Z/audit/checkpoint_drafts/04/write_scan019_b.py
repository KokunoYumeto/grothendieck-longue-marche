import json
from datetime import datetime,timezone
from pathlib import Path
base='work/scan019_b_views/'
views=[
 {'path':'source/DM01_1_001-160_scans/1_scan019.jpg','box':[0,0,1762,2599],'scale':1,'contrast':1,'purpose':'Locate assigned lower-page marks M0308–M0315 in the whole-page context.'},
]
specs=[
 ('relation_band',[275,1580,1740,1760],2,'Inspect M0308 and its adjacent strict inequalities and sentence.'),
 ('definition_band',[290,1945,1745,2225],2,'Inspect M0309–M0312 together in their line context.'),
 ('bottom_band',[275,2195,1755,2590],2,'Inspect M0313–M0315 together with the inserted fidèle T and closing lines.'),
 ('relation_detail',[395,1665,510,1745],5,'Examine overwritten relation M0308 for a separate equality stroke.'),
 ('abbr_de_detail',[330,1980,1135,2130],3,'Inspect M0309 abbreviation and M0310 cancellation in adjacent lines.'),
 ('fblt_formula_detail',[915,2085,1745,2230],3,'Inspect M0311 abbreviation and M0312 deleted formula with its neighboring strokes.'),
 ('trace_detail',[1525,2290,1762,2420],4,'Inspect the one-letter abbreviation M0313 and crossed T at M0314 at the page edge.'),
 ('uniform_detail',[1100,2490,1515,2590],4,'Inspect compressed abbreviation M0315 and following fermé.'),
 ('de_detail',[330,2050,615,2135],5,'Check surviving loop and terminal strokes under M0310 cancellation.'),
 ('formula_detail',[925,2125,1220,2205],5,'Resolve the components of M0312 and inspect the adjacent crossed cluster.'),
 ('uniform_focus',[1130,2515,1360,2590],6,'Check unresolved middle letters and raised terminal letter of M0315.'),
 ('abbreviations_pair_top',[890,1975,1140,2070],4,'Compare the first s. finie abbreviation with the later instance on this page.'),
 ('relations_compare',[1125,565,1530,650],4,'Compare the page’s clear less-than-or-equal signs with the overwritten M0308.'),
 ('fblt_detail',[1510,2075,1745,2190],4,'Examine the fblt strokes of M0311 separately from the underline.'),
 ('de_compare',[850,2070,1045,2160],4,'Compare uncancelled de strokes in the same line with the uncertain deleted word M0310.'),
]
for name,box,scale,purpose in specs:
 views.append({'path':base+name+'.png','box':box,'scale':scale,'contrast':1,'purpose':purpose})
rows=[
 {'id':'M0308','scan':19,'decision':'undecided','reading':r'\unsure{<|\leq}','what the ink shows':'The relation has a visible leftward angle and a long lower arm, but several heavy diagonal strokes fill the interior and upper half. A separate equality bar cannot be isolated from that overwritten mass; the same page’s clear ≤ signs have a distinct lower dash. The obscured upper layers leave < and ≤ unresolved.','crop':[395,1665,510,1745],'confidence':'low'},
 {'id':'M0309','scan':19,'decision':'first','reading':'s. finie','what the ink shows':'After the deleted finie there is one short hooked letter with a detached raised abbreviation mark, followed by a tall descending f and the low linked strokes and dots of finie. There is no intervening e-m-i sequence or hyphen as in the expanded semi-finie candidate. The same short form recurs at M0313.','crop':[890,1975,1140,2070],'confidence':'high'},
 {'id':'M0310','scan':19,'decision':'undecided','reading':r'\unsure{de}','what the ink shows':'A tall narrow loop at the left survives, followed by a short upright/low joining stroke. The long horizontal deletion merges with the middle and reaches terminal up/down strokes at the right. The surviving beginning could support de or le, but the cancelled bodies do not yet distinguish them securely.','crop':[330,2050,615,2135],'confidence':'low'},
 {'id':'M0311','scan':19,'decision':'first','reading':'fblt','what the ink shows':'Before dense, the abbreviation begins with a long descending f stroke and narrow return, then a compact lower loop beneath a second rising stroke, and a final steep upright/return. These small connected components are compressed but visible above and apart from the underline; they support the abbreviated fblt without expanding it.','crop':[1510,2075,1745,2190],'confidence':'medium'},
 {'id':'M0312','scan':19,'decision':'first','reading':r'A\in\mathcal A^+','what the ink shows':'In the right-hand cancelled formula, the initial capital A retains two sloping sides, followed by an open curved membership sign, then a calligraphic A with a low oval return and upright right stem. A small raised horizontal-and-upright stroke is present above its right side, supporting the superscript plus. The cancellation crosses these letters but leaves their outlines readable.','crop':[925,2125,1220,2205],'confidence':'high'},
 {'id':'M0313','scan':19,'decision':'first','reading':'s. finie','what the ink shows':'The page-edge phrase shows the same single small hooked s with a detached abbreviation stroke as M0309, then a separate tall f, a dot, a low extended joining stroke, and the final dotted/curved strokes of finie. It does not contain the additional letters of semi-finie.','crop':[1525,2290,1762,2420],'confidence':'high'},
 {'id':'M0314','scan':19,'decision':'first','reading':'T','what the ink shows':'At the right edge after finie, a capital T retains a long top bar and descending stem. An angled/curved cancellation crosses its middle, while the top bar and main stem remain distinct.','crop':[1525,2290,1762,2420],'confidence':'high'},
 {'id':'M0315','scan':19,'decision':'undecided','reading':r'\unsure{uniformt}','what the ink shows':'The word before fermé has a large hooked initial group, a low extended joining stroke, an oblique terminal stem and a smaller raised crossed stroke consistent with an abbreviated final t. The middle is compressed into the long joining line, and I cannot independently recover all the letters of uniformt from it.','crop':[1130,2515,1360,2590],'confidence':'low'},
]
data={'scan':19,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan019_b','started_utc':'2026-11-19T23:38:59.036964+00:00','finished_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Repeated abbreviated s. finie','marks':['M0309','M0313'],'description':'Both occurrences have the same one-letter hooked abbreviation with a detached raised mark, a space, and finie. Each lacks the additional e-m-i strokes of the expanded alternative.'}],'notes':['Actual source dimensions: 1762 × 2599; all coordinates use the original image. No OCR or text layer used.','Initial report saved before independent review. M0310 was referred to the coordinator for a second reading of its surviving loop.','Immediately before the right-hand cancelled A∈A⁺ at M0312, another crossed cluster is visible. Its scope and reading were flagged to the coordinator; it is not asserted as an unmarked correction here.','M0308 remains uncertain because overwritten ink merges the possible relation components. M0315 remains uncertain because the compressed middle does not securely distinguish all letters.']}
Path('work/scan019_b.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('work/scan019_b.json')
print({d:sum(r['decision']==d for r in rows) for d in ['first','alternative','other','undecided']})
print(data['finished_utc'])
