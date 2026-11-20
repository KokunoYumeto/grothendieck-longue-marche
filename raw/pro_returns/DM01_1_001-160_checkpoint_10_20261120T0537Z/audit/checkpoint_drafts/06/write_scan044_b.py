from pathlib import Path
from datetime import datetime, timezone
import json, shutil
root=Path('/workspace/scratch/18ee30ea2ccf')
now=datetime.now(timezone.utc).isoformat()
rows=[
 {'id':'M0907','scan':44,'decision':'first','reading':r'$\overline E$ est ainsi','what the ink shows':'One baseline E has a separate short bar above it, with no superscript letter. After it, the cancellation still leaves the tall t of est and two dotted i positions in ainsi.','crop':[290,525,570,585],'confidence':'medium'},
 {'id':'M0908','scan':44,'decision':'first','reading':'loi de groupe','what the ink shows':'The first word has an upright l and a distinct i dot. After the small de group, the descending loop of g and the later p descender remain below the strike through groupe.','crop':[925,572,1325,646],'confidence':'medium'},
 {'id':'M0909','scan':44,'decision':'undecided','reading':r'\unsure{elle est|est}','what the ink shows':'Between i.e and additive there is one low undulating group with a short upright near its right end. Separate tall l strokes for elle cannot be distinguished; est alone remains a concrete competitor.','crop':[675,817,1215,890],'confidence':'low'},
 {'id':'M0910','scan':44,'decision':'undecided','reading':r"c'est de plus une isométrie (\unsure{au point de vue de l'application}",'what the ink shows':'The opening retains the dotted/apostrophe strokes of c’est, the p descender in plus, and the tall t and dotted i of isométrie. The parenthesis and point group survive, but the rest of the parenthetical and the following line’s long final word have bodies merged with the cancellation; application versus identification is not resolved.','crop':[280,900,1665,1052],'confidence':'low'},
 {'id':'M0911','scan':44,'decision':'undecided','reading':r"\unsure{de l'espace|d'espace} de Banach",'what the ink shows':'Before espace, a hooked raised stroke and a separate apostrophe-like dot are visible; a distinct second tall l is not recoverable, so d’espace competes with de l’espace. The following de and Banach retain the high B and terminal ch.','crop':[650,977,1155,1045],'confidence':'low'},
 {'id':'M0912','scan':44,'decision':'first','reading':'possède','what the ink shows':'In the rotated margin, the word after the barred E has an initial p stroke, compressed central turns, and a taller d before the final e. The accent area is faint and crossed by nearby ink, but the sequence supports possède.','crop':[115,1110,385,1450],'confidence':'medium'},
 {'id':'M0913','scan':44,'decision':'first','reading':'structure','what the ink shows':'The next margin line has an initial s turn, a rising t stroke, and a low connected middle followed by another upright t and the open final e. These strokes are legible enough for structure despite the diagonal neighboring lines.','crop':[30,970,420,1560],'confidence':'medium'},
 {'id':'M0914','scan':44,'decision':'undecided','reading':r'\illegible{4}','what the ink shows':'The end of the margin note has sparse short strokes near the final E and long crossing lines. At enlarged and rotated views they do not separate into a dependable four-word continuation.','crop':[30,970,420,1560],'confidence':'low'},
 {'id':'M0915','scan':44,'decision':'undecided','reading':r'E=\unsure{\overline E|E}','what the ink shows':'There are exactly two baseline E letters, separated by two equality bars; no superscript letter or numeral is visible. Two cancellation strokes intersect the top of the right E, preventing an independent overbar from being distinguished.','crop':[725,1115,842,1175],'confidence':'low'},
 {'id':'M0916','scan':44,'decision':'undecided','reading':r'\illegible{4}','what the ink shows':'After the equality, a curved opening stroke, several low loops and a later upright survive; a further right-hand group has a descending stem and isolated humps. The horizontal cancellations merge these bodies too extensively for a dependable wording.','crop':[850,1110,1665,1188],'confidence':'low'}
]
views=[]
def view(name,box,scale,purpose,contrast=1,rotation=None,post_crop=None):
    d={'path':name,'box':box,'scale':scale,'contrast':contrast,'purpose':purpose}
    if rotation is not None:d['rotation_degrees']=rotation
    if post_crop is not None:d['post_rotation_scaled_crop']=post_crop
    views.append(d)
view('source/DM01_1_001-160_scans/1_scan044.jpg',[0,0,1696,2147],1,'Locate every assigned mark and margin note.')
p='work/scan044_b_views/'
view(p+'m0907_m0909.png',[270,495,1670,895],2,'Read M0907–M0909 with adjacent prose.')
view(p+'m0910_m0911.png',[280,885,1675,1060],2,'Locate the two-line cancelled isometry sentence.')
view(p+'m0915_m0916.png',[310,1070,1665,1215],2,'Locate cancelled equality and following prose.')
view(p+'margin.png',[25,950,600,1585],2,'Locate all three margin marks before rotation.')
view(p+'m0907_detail.png',[290,525,570,585],4,'Check barred E, t and dotted i strokes under cancellation.')
view(p+'m0908_detail.png',[925,572,1325,646],3,'Check loi and g/p descenders of groupe.')
view(p+'m0909_detail.png',[675,817,1215,890],3,'Distinguish one low word from elle est.')
view(p+'m0910_line1.png',[598,900,1665,994],3,'Inspect word groups in first cancelled line.')
view(p+'m0910_line2.png',[280,974,1260,1052],3,'Inspect final word and de l’espace de Banach sequence.')
view(p+'m0915_detail.png',[715,1100,1060,1178],4,'Count baseline E letters and examine bar overlap.')
view(p+'m0916_right.png',[1120,1105,1665,1188],3,'Inspect separate right-hand cancelled group.')
view(p+'margin_rot45.png',[25,950,535,1585],2,'Align the slanted note for reading.',rotation=-45)
view(p+'margin_detail_rot45.png',[30,970,420,1560],3,'Follow possède, structure and note ending.',contrast=1.25,rotation=-45)
view(p+'m0915_m0916_left_context.png',[300,1110,1070,1180],3,'Separate cancelled formula from neighboring prose.')
view(p+'m0912_m0914_rot45.png',[115,1110,385,1450],4,'Inspect margin letter bodies and overlapping cancellation.',rotation=-45)
view(p+'margin_lower_lines.png',[30,970,420,1560],3,'Isolate lower margin lines after rotation.',contrast=1.25,rotation=-45,post_crop=[0,970,1550,1495])
view(p+'m0910_tail.png',[1290,912,1665,994],4,'Check parenthetical point and following compressed words.')
view(p+'m0911_detail.png',[650,977,1155,1045],4,'Compare de l’espace against d’espace.')
view(p+'m0915_bar.png',[725,1115,842,1175],6,'Check if right E has a separate overbar.')
report={'scan':44,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan044_b','started_utc':'2026-11-20T02:27:40.470392+00:00','finished_utc':now,'source_dimensions':[1696,2147],'rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Cancellation across letter bodies','marks':['M0907','M0908','M0910','M0911','M0915','M0916'],'description':'Horizontal cancellation often leaves dots, ascenders and descenders outside the crossed baseline; in M0915 it occupies exactly the height needed to identify a bar over the right E.'}],'notes':['All ten assigned IDs were personally inspected in source order; source dimensions were measured with Pillow. No other page image or OCR was used.','M0909 and M0910 have concrete competing word readings for selective peer review; M0911 has a concrete de l’espace versus d’espace distinction. Unresolved cancellation in M0914–M0916 is retained.','Primary elapsed interval includes annotation and coordination time, not continuous active visual reading. Initial report preserved before any targeted revision.']}
out=root/'work/scan044_b.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
shutil.copyfile(out,root/'work/scan044_b.initial.json')
print(out)
print('finished_utc',now)
print('rows',len(rows),'views',len(views))
print('counts', {x:sum(r['decision']==x for r in rows) for x in ['first','alternative','other','undecided']})
