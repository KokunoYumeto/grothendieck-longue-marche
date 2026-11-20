from pathlib import Path
import re,json,datetime
base=Path('/workspace/scratch/94548b74fbe0')
out=base/'out/readers/012/B'
src=(base/'packets/012/C.tex').read_text()
manifest=json.loads((out/'crops/manifest.json').read_text())
idx=json.loads((out/'scripts/C_path_index.json').read_text())
# Every supplied contour was checked by position against the half or its local crop.
# Retaining these source contours avoids idealizing the observed figures.
count=0
def annotate(m):
 global count
 count+=1
 return '%% C contour %02d: retained after visual comparison\n'%count+m.group()
src=re.sub(r'\\path\[fill=black,even odd rule\]',annotate,src)
add=r'''
% B additions. Coordinates remain the original full-scan coordinates.
% The following question marks are editorial uncertainty annotations on the
% adjoining graphic. No alphabetic or mathematical role is supplied for a trace.
% B003 / C doubtful-readings row 3: overlaid zigzags; possible cancellation.
% The underlying oval, fine hatching, broad loops, terminal strokes, and the
% connected lower miniature remain in C contours 34,36,40,42--51.
\node[inner sep=0pt,anchor=west] at (386,584){\unsure{\hspace{0pt}}};
% B004: right-hand group: live graphic primary; whole-group cancellation retained
% as an unresolved alternative to H's categorical editorial description.
\node[inner sep=0pt,anchor=west] at (1629,564){\unsure{\hspace{0pt}}};
% B005: pale upper-oval left rim between the retained dark pieces.
\draw[black!35,line width=0.16pt] (885.5,626) .. controls (882,638) and (878,651) .. (876.5,665);
\node[inner sep=0pt,anchor=east] at (869,646){\unsure{\hspace{0pt}}};
% B006: pale lower and lower-right rim, with the observed interruptions retained.
\draw[black!35,line width=0.16pt] (958,812.6) .. controls (966,817) and (975,820) .. (982,818.4);
\draw[black!30,line width=0.15pt] (985,817.5) .. controls (990,816) and (993,813.8) .. (995.5,811.4);
\draw[black!30,line width=0.15pt] (998,809.5) .. controls (1005,803.8) and (1010,799) .. (1014.2,795.2);
\node[inner sep=0pt,anchor=west] at (1000,818){\unsure{\hspace{0pt}}};
% B007: pale continuation beyond the dark terminal of the upper descending curve.
\draw[black!30,line width=0.18pt] (1600,905) .. controls (1607,910) and (1615,917) .. (1621,922.5);
\draw[black!20,line width=0.13pt] (1605,910.8) -- (1616.3,917.9);
\node[inner sep=0pt,anchor=west] at (1624,920){\unsure{\hspace{0pt}}};
% B008: interrupted last return of the large left overlaid zigzag.
\draw[black!35,line width=0.17pt] (373,758) .. controls (377,755.3) and (380,754) .. (382.5,754.3);
\draw[black!40,line width=0.17pt] (384.1,754.4) .. controls (386,754) and (387.2,755.8) .. (387.8,757.4);
\path[fill=black!70] (386.5,754.6) -- (388.5,756.4) -- (388.5,758) -- (386.7,757.3) -- cycle;
\node[inner sep=0pt,anchor=west] at (393,757){\unsure{\hspace{0pt}}};
% B009--B012: four detached marks near the triangle and its filled point.
\path[fill=black] (216.4,445.8) .. controls (215.5,446.3) and (215.7,449.9) .. (216.8,450.2) .. controls (217.5,449) and (217.5,447) .. (216.4,445.8) -- cycle;
\path[fill=black!50] (272,483.4) ellipse[x radius=1.1,y radius=1.3];
\path[fill=black!25] (443,483.8) ellipse[x radius=1.2,y radius=1.8];
\draw[black!35,line width=0.15pt] (452.8,498.3) -- (453.3,501.2);
\path[fill=black] (453.4,501.2) -- (451.9,503.9) -- (454.4,504.1) -- (455,502.8) -- cycle;
\node[inner sep=0pt,anchor=west] at (222,447){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (278,482){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (449,479){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (460,496){\unsure{\hspace{0pt}}};
% B013--B014: two detached narrow marks in the top gap; hand and origin unsettled.
\draw[black!25,line width=0.14pt] (590,40.5) -- (590.4,44);
\path[fill=black!55] (590.8,45) ellipse[x radius=0.9,y radius=1.7];
\draw[black!30,line width=0.14pt] (609.3,44) -- (609.6,46);
\path[fill=black] (609.6,47.2) ellipse[x radius=0.85,y radius=1.3];
\node[inner sep=0pt,anchor=west] at (617,44){\unsure{\hspace{0pt}}};
% B015: tiny pale detached spot above-left of the lower upright zigzag.
\path[fill=black!20] (426.8,901.1) ellipse[x radius=1.2,y radius=1.1];
\node[inner sep=0pt,anchor=west] at (442,898){\unsure{\hspace{0pt}}};
% B016: detached stroke at the right paper edge, on the level of the fold.
\draw[black,line width=0.42pt] (1656.3,793.6) -- (1663,793.8) -- (1671.4,794.3);
\node[inner sep=0pt,anchor=east] at (1651,790){\unsure{\hspace{0pt}}};
% B017--B019: detached dots within the right-hand graphic field.
\path[fill=black] (1643.2,532.4) ellipse[x radius=1.15,y radius=1.4];
\path[fill=black!60] (1034,823) ellipse[x radius=1,y radius=1.1];
\path[fill=black!60] (1231,860.4) ellipse[x radius=0.9,y radius=1.3];
\node[inner sep=0pt,anchor=west] at (1649,532){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (1039,827){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (1237,863){\unsure{\hspace{0pt}}};
% B020: pale open hook in the lower blank field. Shape only; no character supplied.
\draw[black!22,line width=0.16pt] (401.6,1288.7) .. controls (405,1292) and (409,1298) .. (411,1306)
 .. controls (413.6,1314.4) and (408,1317.2) .. (403,1319.5)
 .. controls (397.5,1323.3) and (391.5,1323.6) .. (386.8,1323.7);
\node[inner sep=0pt,anchor=west] at (418,1310){\unsure{\hspace{0pt}}};
% B021: isolated dark speck visible on half b, full-scan coordinates.
\path[fill=black] (789.3,1430.5) ellipse[x radius=1.8,y radius=2.1];
\node[inner sep=0pt,anchor=west] at (795,1430){\unsure{\hspace{0pt}}};
% B022--B024: pale spot and separate dark pair in lower-right blank field.
\path[fill=black!30] (1454.5,1661) ellipse[x radius=1.3,y radius=1.6];
\path[fill=black] (1529,1705.8) ellipse[x radius=1.2,y radius=1.4];
\path[fill=black] (1524.1,1712.8) .. controls (1522.4,1711.7) and (1522.3,1713.5) .. (1524.1,1714)
 .. controls (1526,1713.2) and (1525.8,1712.1) .. (1524.1,1712.8) -- cycle;
\node[inner sep=0pt,anchor=west] at (1462,1660){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (1536,1709){\unsure{\hspace{0pt}}};
% B025--B026: two separate dark shapes near the right-hand foot of the sheet.
\path[fill=black] (1656,2190.8) -- (1658.8,2190.7) -- (1658,2189.2) -- cycle;
\path[fill=black] (1418,2290) ellipse[x radius=0.9,y radius=1.1];
\node[inner sep=0pt,anchor=east] at (1652,2189){\unsure{\hspace{0pt}}};
\node[inner sep=0pt,anchor=west] at (1424,2290){\unsure{\hspace{0pt}}};
% crop-candidate: scan 12
'''
src=src.replace('\\end{tikzpicture}}',add+'\n\\end{tikzpicture}}')
(out/'reading.tex').write_text(src)

D=[]
def diff(id,location,C,H,reading,evidence,confidence,kind,dC,dH,status=None,crop=None,bbox=None,source=None,**extra):
 obj={'id':id,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dC,'diff_H':dH,'C_doubt_status':status,'readers_crop':crop,'bbox':bbox,'C_source_row':source}
 obj.update(extra);D.append(obj)
c1='crops/c01_upper_right_label.png';c2='crops/c02_marked_left_assembly.png';c3='crops/c03_upper_loop.png';c4='crops/c04_lower_loop.png';c5='crops/c05_right_group.png';c6='crops/c06_triangle_dots.png';c7='crops/c07_top_gap_traces.png';c8='crops/c08_pale_lower_hook.png';c9='crops/c09_lower_paired_spots.png';c10='crops/c10_foot_right_traces.png'
diff('B001','Above upper-right large oval',r'\unsure{OK|Ok}','Four disks marked « OK » (or « ok »), per H rereading note',r'\unsure{OK|Ok}','Closed first oval; tall second upright; upper oblique arm and curved lower return do not settle the case of the second letter. The visible first letter is retained as O.','medium','other',False,False,'retained',c1,[1459,43,1521,97],'CD12.1',qualification='The same primary reading and supported second-letter alternative as C are retained; H’s global case qualification supplies no established local error.')
diff('B002','Between the two miniature ovals under the large left marked oval',r'\unsure{ou}','Variants introduced by « ou »',r'\unsure{ou}','A small left loop has a heavy lower turn, followed by one compressed rising and falling run. ou remains the best lexical candidate; the second-letter stroke is insufficiently distinct for removal of doubt.','medium','other',False,False,'retained',c2,[177,847,214,865],'CD12.2',qualification='No other word is supported. The unassigned graphic-shape alternative is retained in the doubt record.')
diff('B003','Lower-left large oval, overlying broad loops/zigzags and their outer extensions','Doubt table: overlaid zigzags; possible cancellation. C.tex draws these without a local unsure marker.','General drawing description; no separate cancellation statement for this oval','Overlaid zigzags, with possible cancellation of the underlying oval; all strokes retained and the local graphic marked unsure','Fine central hatching coexists with wider diagonal returns that cross several chords and extend beyond the outline at the upper-left and lower-right. Their geometry is readable; their editorial function remains open.','low','other',False,False,'retained',c2,[155,562,390,831],'CD12.3',qualification='This retains the source table’s existing uncertainty; the added local marker is synchronization, not an independent reading correction. B008 records the newly recovered terminal geometry.')
diff('B004','Entire right-hand lower group, including repeated top/left rules, intersecting curves and two ovals','Live paths without cancellation qualification','« Tout le coin inférieur droit, les deux axes en équerre et ce qu’ils renferment ... est biffé »','Live graphic primary, whole-group cancellation retained as an unresolved alternative; existing strokes remain in place','The top is traced twice with a rightward hook on the lower trace. At left there are three closely parallel descending strokes with returns and an open corner gap. The long curves and diagonal cross local shapes; the ink supplies no distinct boundary for a whole-group cancellation target.','low','deletion state (struck given live or live given struck)',True,True,None,c5,[809,348,1649,1178],qualification='Qualified difference: H’s cancelled-state reading remains explicitly available. No chronology or mathematical role is inferred.')
new=[
 ('B005','Upper oval inside right-hand group, pale left rim',[874,624,889,669],c5,'Pale descending rim segment from about (885.5,626) to (876.5,665)','The crop shows a continuous pale narrow curve between darker retained left-rim pieces.','medium','his hand','B.new.01'),
 ('B006','Upper oval inside right-hand group, lower and lower-right rim',[956,793,1018,822],c5,'Interrupted pale bottom/lower-right rim joining the vicinity of retained C contours 41,55,60,61','A faint low arc continues past the two short dark bottom pieces; a pale slant rises toward the retained lower-right fragments. Small interruptions remain.','medium','his hand','B.new.02'),
 ('B007','Upper long descending curve, far-right terminal',[1598,903,1623,925],c5,'Pale oblique terminal extension, including a short parallel residual streak','A light gray continuation extends below-right of the dark angular terminal; the final light endpoint is less definite than the dark stroke.','medium','undetermined hand','B.new.03'),
 ('B008','Large left marked oval, final lower-right return',[372,752,390,761],c2,'Interrupted pale rightward return with a small dark hooked endpoint','The broad lower return continues beyond C’s (373.3,758) endpoint to a pale interrupted segment and dark terminal fleck near (388,757).','medium','his hand','B.new.04'),
 ('B009','Immediately above the small triangle apex',[214,444,220,452],c6,'Detached short upright tick','A narrow dark mark is separated by white space from the longer upper protrusion of the triangle.','high','undetermined hand','B.new.05'),
 ('B010','Between small triangle and its large filled point, above-left of the point',[270,481,275,486],c6,'Small gray round spot','The round gray mark is detached from both triangle and large filled point.','medium','undetermined hand','B.new.06'),
 ('B011','Above-left of the tiny right-hand droplet in the triangle register',[440,480,447,488],c6,'Pale elongated spot','A faint compact vertical oval is visible above-left of the darker droplet. Its role and surface origin are not settled.','low','undetermined hand','B.new.07'),
 ('B012','Right of the triangle and filled point, before upright looping drawing',[450,496,457,507],c6,'Tiny dark droplet with a pale short upper stem','The black lower spot is pointed at its top and has a short pale disconnected/weakly connected continuation upward.','medium','undetermined hand','B.new.08'),
 ('B013','Top gap right of the small alternative oval, left detached mark',[588,39,594,49],c7,'Gray narrow mark with a faint upper trace','The left compact mark has a darker lower center and pale upright continuation. No letter is read.','medium','undetermined hand','B.new.09'),
 ('B014','Top gap right of the small alternative oval, right detached mark',[607,42,613,51],c7,'Dark narrow spot with a short pale upper trace','The right mark has a dark lower oval and a weak vertical top. It remains detached from the left mark.','medium','undetermined hand','B.new.10'),
 ('B015','Above-left of the lower upright zigzag, just below the closing parenthesis',[424,898,430,904],c4,'Tiny pale round spot','A separate pale compact mark lies above-left of the zigzag’s first strong stroke. The neighboring paper grain prevents a confident assignment of origin.','low','undetermined hand','B.new.11'),
 ('B016','Far-right paper edge at fold height',[1655,791,1673,798],c5,'Detached short horizontal stroke reaching the paper edge','The black horizontal mark is separate from the main right-hand curves and meets the dark outside scan boundary at the edge of the paper.','high','undetermined hand','B.new.12'),
 ('B017','Under the right end of the double top rule',[1640,529,1647,537],c5,'Detached dark spot','Compact dark spot below the top rule’s end; local pixel bounds are (1642,531)–(1645,534).','high','undetermined hand','B.new.13'),
 ('B018','Below upper tall oval in the right-hand group',[1031,820,1037,826],c5,'Tiny detached gray-dark spot','A separate point occurs below-right of the pale oval rim; local dark bounds are (1033,822)–(1035,824).','medium','undetermined hand','B.new.14'),
 ('B019','Under lower rising transverse line of the right-hand curves',[1228,857,1234,864],c5,'Tiny detached gray-dark spot','A small vertical spot occurs just below the transverse curve; local dark bounds are (1230,859)–(1232,862).','medium','undetermined hand','B.new.15'),
 ('B020','Lower blank field, left of center',[384,1286,415,1327],c8,'Pale open hook, preserved as a graphical path','A thin open curved trace descends, bends left, and ends in a low leftward return. The crop supplies a path but no secure character or hand attribution.','low','undetermined hand','B.new.16'),
 ('B021','Lower blank field, near center',[786,1427,793,1434],None,'Isolated dark speck','The dark point is fully visible on half b at coordinates (786,327)–(793,334); full-scan offset is +1100 in y.','high','undetermined hand','B.new.17'),
 ('B022','Lower-right blank field, above-left of the paired dark spots',[1452,1658,1458,1665],c9,'Small pale gray spot','A compact gray patch is distinct from the two much darker lower spots; no character is supplied.','low','undetermined hand','B.new.18'),
 ('B023','Lower-right blank field, upper spot of the dark pair',[1526,1703,1532,1709],c9,'Upper separate dark oval spot','Compact dark oval; separated by white paper from the lower-left spot.','high','undetermined hand','B.new.19'),
 ('B024','Lower-right blank field, lower-left spot of the dark pair',[1521,1710,1527,1716],c9,'Lower-left separate dark angular spot','Compact angular spot below-left of B023; no joining stroke appears.','high','undetermined hand','B.new.20'),
 ('B025','Near right edge in the lower foot field',[1654,2187,1661,2193],c10,'Tiny dark wedge-like spot','The compact horizontal triangular shape has local dark bounds (1656,2189)–(1659,2191).','medium','undetermined hand','B.new.21'),
 ('B026','Lower foot field, to the left of the near-edge wedge',[1415,2287,1421,2293],c10,'Tiny dark round spot','The dark point is separate from the archive number and surrounding paper texture; local dark bounds (1417,2289)–(1419,2291).','high','undetermined hand','B.new.22')
]
for id,loc,bbox,crop,reading,evidence,conf,hand,el in new:
 diff(id,loc,'Omitted','Not specified in the drawing description',reading,evidence,conf,'omission',True,True,None,crop,bbox,qualification='Graphical shape retained. Hand, role, and surface origin remain undetermined.' if hand=='undetermined hand' else 'Graphical continuation retained; no semantic or algebraic connection is supplied.',inventory_element=el)
 if id=='B008':D[-1]['C_source_row']='CD12.3'
# H's global prose is assessed as a description, not as invented manuscript prose.
diff('B027','Top row of four large ovals and two miniature alternatives','Detailed TikZ contours and labels','Disks with chords and a triangular or quadrangular hatched region; variants introduced by ou','Four large ovals and two detached small alternatives, with their individual chord systems, cap arc, endpoint forms, hatching and heavy segments','Half a shows the lower cap arc in the first large oval, the second oval’s three uprights and thick crosspiece with local endpoint marks, the third oval’s hatched quadrilateral, the fourth oval’s hatched triangle and short heavy segment, and the two distinct miniature alternatives. These detailed forms are preserved in all original C contours.','high','drawing or diagram',False,True,None,None,[146,22,1633,406],qualification='One aggregate detail-coverage row against H’s generic upper-row description; it does not double-count the label uncertainties or B013/B014’s new detached marks.')
diff('B028','Detached upright looping drawing between upper triangle/point and heavy Y','C contour 27','Not mentioned','Narrow upright looping drawing with tall pointed top, small left loops, larger right loop and low endpoint','Crop c03 shows the complete intertwined contour; no separate secure letters are recovered.','high','omission',False,True,None,c3,[528,412,558,511],qualification='Graphical reading retained; no alphabetic interpretation supplied.')
diff('B029','Lower-left parenthetical pair of miniature ovals','Parenthesis contours 53/58, miniature contours 34/59/63; first ou and doubtful second ou','General reference to variants introduced by ou; this parenthetical pair is not separately described','Opening parenthesis, ou, first miniature oval, doubtful ou, second miniature oval, closing parenthesis; all local radii/wedges preserved','The whole construction is visible on half a; c02 verifies the right miniature’s connection and central filled wedge. The parentheses are asymmetrical and remain actual curved paths.','high','drawing or diagram',False,True,None,c2,[24,757,407,920],qualification='Single coverage row for this passage. B002 and B008 remain separate C-doubt/terminal decisions with no duplicate H passage count.')
diff('B030','Detached lower upright zigzag to the right of the diagonal quadrilateral','C contour 66','Not mentioned','Tall angular looping/zigzag drawing with two small upper return cells, one larger lower triangular cell and a hooked lower endpoint','Crop c04 shows the complete dark form. The faint spot B015 is a separate physical mark.','high','omission',False,True,None,c4,[399,899,444,1020],qualification='Graphical reading retained without supplied letters.')
diff('B031','Central oval of second register, above lower three-spoked triangle','C contour 37','Not individually described','Round outline with intersecting chords and small central hatched wedge, including the lower continuation and crossings','Half a establishes all boundaries, crossing chords, fine hatch, and the lower extensions, retained in C contour 37.','high','drawing or diagram',False,True,None,None,[567,612,786,842],qualification='Coverage difference from H’s prose inventory; no theorem or map is inferred.')

# Inventory: retain C's physical entries, correcting descriptions where source geometry is more specific.
inv=json.loads((base/'packets/012/C_inventory.json').read_text())
for ob in inv:
 ob.pop('cote',None);ob.pop('scan',None)
 ob['hand']='his hand'
 ob['sheet_kind']='text'
# Explicit local properties checked against the image.
updates={
'012.03':'small oval with crossing spokes, dark central point/region and an interrupted right boundary',
'012.05':'oval, three near-upright chords, thick middle crosspiece; open middle end-circles and other local dark/crossed endpoint marks',
'012.08':r'\unsure{OK|Ok}',
'012.13':'detached narrow upright looping graphic; no letters supplied',
'012.15':'four-sided outline with small lower-left gap',
'012.18':'oval with chords, fine central hatching and broad overlaid zigzags; cancellation possible; local graphic marked unsure',
'012.20':'two actual curved parenthesis strokes; opening/closing heights differ',
'012.23':r'\unsure{ou}',
'012.24':'small oval with spokes and central filled wedge, connected above to the marked-oval strokes',
'012.25':'oval with crossing chords, central hatched wedge and lower chord extensions',
'012.27':'detached upright angular looping/zigzag graphic; no letters supplied',
'012.29':'two top horizontal traces (lower one hooked right); three near-parallel descending left traces with returns; open corner gap',
'012.30':'tall oval with crossing chords and faint interrupted lower/left rim; local whole-group cancellation status unresolved',
'012.31':'extended crossing curves with local arrow-like hooks and detached short parallel strokes; whole-group cancellation status unresolved',
'012.32':'low oval/rounded outline with curved chords and extended diagonal; whole-group cancellation status unresolved'
}
for ob in inv:
 if ob['element'] in updates:ob['first_words_or_objects']=updates[ob['element']]
for id,loc,bbox,crop,reading,evidence,conf,hand,el in new:
 inv.append({'sheet_kind':'text','hand':hand,'element':el,'kind':'drawing','position':loc,'first_words_or_objects':reading,'transcribed':'yes','bbox':bbox,'difference_id':id,'role':'unassigned' if hand=='undetermined hand' else 'graphical continuation','source_origin':'unsettled' if hand=='undetermined hand' else 'same drawn contour; precise faded extent qualified','shape_confidence':conf})
inv.append({'sheet_kind':'text','hand':'undetermined hand','element':'B.archive.11','kind':'text','position':'bottom-left corner','first_words_or_objects':'archive numeral 11, recorded only as comment','transcribed':'yes','bbox':[26,2300,74,2334]})

# Every original doubtful-readings row has one source identity, with local subloci.
source_map=[
 {'source_row':'CD12.1','source_heading':'Doubtful readings','source_row_exact':'12 | above upper right oval | OK | Ok | medium | O closes on itself, k/K has an unusually short last branch.','status':'retained','difference_ids':['B001'],'local_subloci':[{'id':'CD12.1.a','location':'first closed oval letter','reading':'O','status':'readable','bbox':[1459,56,1485,94]},{'id':'CD12.1.b','location':'second tall upright and branching return','reading':'K|k','status':'unresolved','bbox':[1487,43,1521,97]}],'crop':c1},
 {'source_row':'CD12.2','source_heading':'Doubtful readings','source_row_exact':'12 | between miniature ovals | ou | — | medium | The second hump is compressed; compare ou beside the top oval.','status':'retained','difference_ids':['B002'],'local_subloci':[{'id':'CD12.2.a','location':'small initial loop','reading':'o-like loop','status':'readable shape','bbox':[177,847,190,865]},{'id':'CD12.2.b','location':'compressed following rise and fall','reading':'u candidate; unassigned graphical run alternative','status':'unresolved','bbox':[187,851,214,864]}],'crop':c2},
 {'source_row':'CD12.3','source_heading':'Doubtful readings','source_row_exact':'12 | lower-left heavily marked oval | overlaid zigzags | possible cancellation of the underlying oval | low | Several strokes extend beyond the boundary. Both the oval with its chords and the overlying pen strokes are drawn in their actual positions. The ink alone does not settle their editorial function.','status':'retained','difference_ids':['B003','B008'],'local_subloci':[{'id':'CD12.3.a','location':'underlying oval and chord network','reading':'all contours retained','status':'readable shape','bbox':[156,574,382,831]},{'id':'CD12.3.b','location':'fine central hatch','reading':'thin oblique hatching retained','status':'readable shape','bbox':[205,624,316,746]},{'id':'CD12.3.c','location':'wide diagonal looping over-strokes','reading':'overlaid zigzags; possible cancellation','status':'unresolved editorial function','bbox':[183,564,390,804]},{'id':'CD12.3.d','location':'last lower-right return and pale terminal','reading':'extended interrupted return, B008','status':'medium-confidence geometry','bbox':[372,752,390,761]},{'id':'CD12.3.e','location':'lower continuation into miniature below','reading':'connected stem/contour retained; no chronology supplied','status':'readable shape','bbox':[296,779,319,839]}],'crop':c2}
]

# Remaining doubts have their own local entries, including uncertain roles.
doubts=[
 {'location':D[0]['location'],'reading':r'\unsure{OK|Ok}','alternatives':['OK','Ok'],'confidence':'medium','reason':D[0]['evidence'],'crop':c1,'C_source_row':'CD12.1','difference_id':'B001'},
 {'location':D[1]['location'],'reading':r'\unsure{ou}','alternatives':['ou','unassigned loop-and-run graphic'],'confidence':'medium','reason':D[1]['evidence'],'crop':c2,'C_source_row':'CD12.2','difference_id':'B002'},
 {'location':D[2]['location'],'reading':'overlaid zigzags; cancellation possible','alternatives':['graphic overlay','cancellation of underlying oval'],'confidence':'low','reason':D[2]['evidence'],'crop':c2,'C_source_row':'CD12.3','difference_id':'B003'},
 {'location':D[3]['location'],'reading':'live drawing primary; cancelled state retained','alternatives':['live drawing','whole-group cancellation'],'confidence':'low','reason':D[3]['evidence'],'crop':c5,'C_source_row':None,'difference_id':'B004'}
]
for ob in D[4:26]:
 # Shape and interpretation uncertainty are kept distinct.
 hand=next((x[7] for x in new if x[0]==ob['id']),None)
 doubts.append({'location':ob['location'],'reading':ob['reading'],'alternatives':['precise faded endpoint remains approximate'] if hand=='his hand' else ['intentional drawn mark','unassigned surface trace'], 'confidence':ob['confidence'],'reason':ob['evidence']+(' Shape is preserved without assigning a hand, role, or origin.' if hand=='undetermined hand' else ' Supported pale geometry is reproduced; very faint endpoint precision remains limited.'),'crop':ob['readers_crop'],'C_source_row':'CD12.3' if ob['id']=='B008' else None,'difference_id':ob['id']})

# Assign all 68 contours to their inspected physical places.
groups={1:('upper-left miniature','half a',['012.03']),2:('first large oval','half a',['012.01']),3:('second large oval','half a',['012.05']),4:('third large oval','half a',['012.07']),5:('fourth large oval','half a',['012.09']),13:('fourth large oval right rim','half a',['012.09']),18:('fourth large oval fine hatching','half a',['012.09']),23:('far-right miniature','half a',['012.11']),24:('third large oval interrupted lower-right rim','half a',['012.07']),25:('right-hand connected top rules, crossing-curve field and lower oval',c5,['012.29','012.31','012.32']),26:('upper stemmed triangle','half a / c05 context',['012.16']),27:('upper isolated looping graphic',c3,['012.13']),28:('small square with lower-left gap','half a / c05 context',['012.15']),29:('heavy three-pronged graphic','half a',['012.14']),30:('small triangle',c6,['012.12']),31:('filled point beside small triangle',c6,['012.12']),32:('left near-parallel frame strokes',c5,['012.29']),33:('upper oval in right-hand field',c5,['012.30']),34:('marked left oval and connected lower-right miniature',c2,['012.18','012.24']),35:('left oval with two dark wedges','half a',['012.17']),36:('detached hatch piece in marked left oval',c2,['012.18']),37:('middle oval with hatched wedge','half a',['012.25']),38:('short upward-right hook in right field',c5,['012.31']),39:('tiny detached piece beside upright right field stroke',c5,['012.31']),40:('small detached fragment in marked left oval',c2,['012.18']),41:('left/lower portion of upper right-field oval',c5,['012.30']),52:('parallel short oblique fragment in right field',c5,['012.31']),53:('opening parenthesis','half a',['012.20']),54:('parallel short oblique fragment in right field',c5,['012.31']),55:('lower-right oval-rim fragment',c5,['012.30']),56:('parallel short oblique fragment in right field',c5,['012.31']),57:('left margin horizontal tick beside parenthesis','half a',['012.20']),58:('closing parenthesis',c2,['012.20']),59:('lower-left miniature','half a',['012.22']),60:('lower oval-rim fragment',c5,['012.30']),61:('second lower oval-rim fragment',c5,['012.30']),62:('parallel short oblique fragment in right field',c5,['012.31']),63:('internal separate diagonal in lower-left miniature','half a',['012.22']),64:('left-end piece of lower rising curve',c5,['012.31']),65:('lower triangle with three interior spokes','half a',['012.28']),66:('lower isolated zigzag',c4,['012.27']),67:('short detached spot beside diagonal',c5,['012.31']),68:('lower quadrilateral with diagonal','half a',['012.26'])}
for n in [6,7,8,9,10,11,12,14,15,16,17,19,20,21,22]:groups[n]=('third large oval fine hatching and disconnected flecks','half a',['012.07'])
for n in range(42,52):groups[n]=('marked left oval fine detached hatching pieces',c2,['012.18'])
for ob in idx:
 loc,on,els=groups[ob['path']]
 ob.update({'location':loc,'inspected_on':on,'inventory_elements':els,'retained':True,'audit':'Source coordinates, open gaps, fills, detached pieces and connections reviewed against the assigned image; no idealized replacement.'})

report={
 'scan':12,'reader':'B','start_utc':'2026-11-20 12:54:32 UTC','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':D,'doubts':doubts,'inventory':inv,
 'notes':[
  {'topic':'Page content','text':'Drawing sheet: four large upper ovals and two small alternatives; a middle register of small triangle and point, two isolated looping graphics at different levels, a heavy three-pronged drawing, quadrilateral and stemmed triangle; lower-left ovals and a parenthetical pair; lower quadrilateral with diagonal and triangle with interior spokes; a large right-hand field of repeated rules, curves and two ovals. Complete paths and all eight lexical labels are retained.'},
  {'topic':'Authorial labels','text':'Four marks read OK (the upper-right case remains OK/Ok). Four small labels read ou, with the between-miniature occurrence qualified. No written sentence, title, date, theorem or explicit authorial question is recovered on this sheet. OK is transcribed literally and is not treated as a proof check.'},
  {'topic':'Page numbering','text':'Bottom-left pencilled 11 is an archive sheet numeral, represented solely by the comment % archive sheet number: 11. No independent manuscript page number is assigned.'},
  {'topic':'H packet boundary','text':'H’s page-11 drawing description and rereading note are collated for scan012. The trailing unnumbered heading Décompositions n-aires (et découpages) d’espaces topologiques is explicitly assigned by H’s own note to feuillet13 and is contextual material outside this scan; it is neither transcribed nor counted as invented text on scan012.'},
  {'topic':'H apparatus','text':'H’s prose drawing description is descriptive apparatus rather than manuscript prose. Its initial three-OK count is superseded by its own rereading note giving four; no count correction is reported. Its clarification that only the horizontal border has a point agrees with the observed top rightward hook and the unarrowed left strokes. Its whole-right-group cancellation assertion remains an available but unresolved state.'},
  {'topic':'Graphic uncertainty encoding','text':'The local unsure markers beside the large left marked oval and the right-hand group apply to cancellation scope. Markers beside added traces qualify their exact faded shape or their unsettled hand, role and surface origin. They add no manuscript words or alphabetic glyphs. Every original path is retained, including the observed crossings and detached pieces.'},
  {'topic':'Faint areas','text':'The pale lower-field hook is retained graphically. The c10 area around the suspected faint upright near (1446,2100) yields paper texture and diffuse shading without a stable stroke or character candidate; no character or extra path is supplied there. The fine repetitive gray page grain elsewhere is not promoted into writing.'},
  {'topic':'Mathematical checking','text':'No mathematical theorem, proof, classification or finite-object computation was tested. The work here establishes visible geometry and labels only; check_events is therefore empty.'},
  {'topic':'Source-path audit','text':'All 68 supplied C contour commands were read and mapped to physical image regions. They are retained after visual comparison, with added pale continuations and detached marks separately identified. No compiler or render was invoked.'}
 ],
 'notation':[
  {'location':'upper and middle labels','written_form':'OK','proposed_LaTeX':'OK','expansion':'okay','status':'Literal abbreviation retained; no expansion in transcription.'},
  {'location':'above upper-right large oval','written_form':'OK/Ok','proposed_LaTeX':r'\unsure{OK|Ok}','status':'Case of second letter remains open.'},
  {'location':'four alternative labels','written_form':'ou','proposed_LaTeX':'ou; between miniature ovals '+r'\unsure{ou}','status':'The joined word is retained at each individual location; fourth occurrence doubtful.'},
  {'location':'isolated upper and lower narrow graphics','written_form':'looped and angular strokes','proposed_LaTeX':'TikZ contours 27 and 66','status':'No text characters supplied.'},
  {'location':'top second oval, middle upright endpoints','written_form':'open small loops','proposed_LaTeX':'actual hollow contour paths in contour 3','status':'Each light center and surrounding rim read locally on half a.'},
  {'location':'lower-right border and crossing curves','written_form':'repeated lines, local hooks, detached short marks','proposed_LaTeX':'TikZ contours 25,32,38,39,52,54,56,62,64,67','status':'Exact visible placements retained without an inferred diagrammatic map.'}
 ],
 'check_events':[], 'crops':manifest,
 'brief_feedback':[
  'The supplied C doubt table contains an uncertain drawing state without a corresponding unsure macro in C.tex. The table row is retained as one doubt and synchronized with a local graphical marker; this is not counted as a new reading difference.',
  'The drawing-heavy source uses 68 contour paths, several spanning more than one inventory element. Explicit path-to-element mapping is provided to avoid treating a multi-element connected path as an omitted object.',
  'A few tiny detached dark shapes and pale traces have stable visible geometry while their hand, purpose and surface origin remain open. Their contours are retained and qualified; no semantic character is forced from them.',
  'Crop c02 deliberately covers the marked oval’s connected lower miniature and the adjacent doubtful ou. It clips unrelated context at the left edge and a small part of the lower quadrilateral at the bottom; none of its target endpoints is clipped. Crop c05 clips unrelated upper-row disks in the top context strip while retaining every endpoint of its target group.'
 ],
 'C_doubt_source_map':source_map,'source_path_audit':idx,
 'workflow':{'view_order':['full scan once','half a once','half b once']+[x['path']+' once' for x in manifest],'image_dimensions':{'full':[1690,2361],'a':[1690,1260],'b':[1690,1261]},'half_offsets':{'a':[0,0],'b':[0,1100]},'crop_count':len(manifest),'no_recrops':True,'pixel_coordinate_check':'PIL intensity components were used only to locate a few already visually identified isolated spots; no OCR or text recognition was used.','structural_checks':None}
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

lines=['# Scan 012 — independent reader B','',
'UTC start: 2026-11-20 12:54:32 UTC. The full scan, half a and half b were each viewed once, in that order. Ten planned local enlargements were made and each viewed once; no recrop, OCR, external source, other page, other reader file, compiler or rendering was used. Half b has the full-scan offset (0,1100), obtained from the actual dimensions 1690×2361 and 1690×1261.','',
'## Page reading audit','',
'| Register / line | Readable ink and graphic form | Unresolved qualification |','|---|---|---|',
'| Top, first large oval | Oval boundary, two crossing oblique chords, a near-upright left chord, thin triangular hatching and a lower cap arc. The small following oval has spokes and a central dark region. The label before it reads ou. | None in the established paths. |',
'| Top, second large oval | OK above; three near-upright chords, thick middle crosspiece, local open endpoint loops, dark side endpoints and crossed/hooked terminations. | Open/filled forms retained from each local rim; no inferred graph identification. |',
'| Top, third large oval | OK above; crossing chords enclose a hatched quadrilateral. Fine separate hatch fragments and the interrupted lower-right outline are retained. | None beyond the exact drawn geometry. |',
'| Top, fourth large oval | The upper label is OK/Ok. Chords, hatched triangle, thick short rightward segment, thin rim and smaller alternative after ou are retained. | B001 / CD12.1: case of second letter. |',
'| Top gap | Two tiny narrow detached marks between the first miniature and the OK oval. | B013–B014: role, hand and origin remain open. |',
'| First free-graph register, left | Small triangle with upper protrusion and side kink; separate substantial filled point. | B009–B012 preserve a detached upper tick and three lesser spots/stems. Their role and origin are open. |',
'| First free-graph register, middle | Narrow looping graphic, then a heavy Y-like three-pronged drawing with dark ends. | No letters supplied for the looping shape; H omits that shape (B028). |',
'| First free-graph register, right | Four-sided outline with a small lower-left gap, then triangle with an upright stem. | Exact open gap and stroke shapes retained. |',
'| Left second register | Small oval with two dark wedges; next a larger oval with fine hatch and broad looping diagonal overlays; OK to its right. | B003 / CD12.3: cancellation function remains open. B008 adds the interrupted terminal beyond the main rightward return. |',
'| Left parenthetical line | Opening curved parenthesis, ou, first miniature, doubtful ou, connected right miniature with spokes and central filled wedge, closing curved parenthesis. | B002 / CD12.2: the compressed second word remains ou with doubt. Parentheses and minis are graphical paths. |',
'| Lower left | Four-sided outline with rising diagonal; isolated angular looping graphic to its right. | The looping graphic remains nonalphabetic transcription (B030). Tiny pale spot B015 has an unsettled origin. |',
'| Middle lower | Oval with crossing chords, hatched central wedge and lower continuations; below it a triangle with three interior spokes. | Exact paths retained; no mathematical assertion added. |',
'| Right large field | Double top trace with rightward hook; three left descending traces with returns and an open corner; two oval outlines, long crossing curves, local hooks, short detached parallel fragments and a small existing spot. | B004: live graphic primary, H’s whole-group cancellation remains possible. B005–B007 recover faded rim/terminal traces. B016–B019 add a side-edge stroke and three detached spots. |',
'| Lower blank field | Pale open hook left of center; isolated dark point near center; pale spot and dark pair lower-right; tiny wedge and point near right foot. | B020–B026 preserve shape only with hand, role and origin unassigned. |',
'| Bottom-left corner | Pencilled archive 11. | Comment only under the governing convention; no manuscript page number inferred. |','',
'## Original C doubtful-readings rows','',
'| Source row | All local subloci mapped | Outcome |','|---|---|---|',
'| CD12.1 — above upper right oval | O loop; second upright and branching return (CD12.1.a–b) | Retained as `\\unsure{OK|Ok}`; B001, crop c01. |',
'| CD12.2 — between miniature ovals | Initial loop; compressed following rise/fall (CD12.2.a–b) | Retained as `\\unsure{ou}`; B002, shared crop c02. |',
'| CD12.3 — lower-left heavily marked oval | Underlying oval/chords; fine hatch; broad loops/cancellation scope; last return; lower connection (CD12.3.a–e) | Editorial state retained, local graphic qualified; B003. New terminal B008 separately mapped. Shared crop c02. |','',
'There are exactly three original source doubt rows. The notation and abbreviation entries are kept in their own categories. No source row is silently split into an extra original doubt; each physical sublocus is explicitly identified in report.json.','',
'## Witness boundary and comparison','',
'H’s drawing description and its rereading note apply to page 11 / our scan012. H’s own rereading note already changes the initial count of three OK marks to four, so there is no independent count correction. The final unnumbered section and note refer explicitly to feuillet13 and are contextual material outside this page; they are excluded from transcription and collation. Descriptive words such as “un triangle” and “deux axes” are H’s apparatus, not manuscript words.','',
'H gives prose coverage rather than the individual contour paths. B027–B031 identify specific graphic coverage differences without counting every retained contour as a separate H error. The new recovered traces have their own local entries. The right-hand cancellation claim is a qualified disagreement: H’s state is retained as an alternative.','',
'## Local decisions and differences','',
'| ID | Place | Reading / result | C / H difference | Evidence |','|---|---|---|---|---|']
for ob in D:
 esc=lambda v:str(v).replace('|',' / ').replace('\n',' ')
 lines.append('| '+ ' | '.join([ob['id'],esc(ob['location']),esc(ob['reading']),('yes' if ob['diff_C'] else 'no')+' / '+('yes' if ob['diff_H'] else 'no'),esc(ob['readers_crop'] or 'Supplied half; full-scan bbox '+str(ob['bbox']))])+' |')
lines+=['','## Source contour audit','','All 68 C contour commands are retained after comparing their physical drawing regions to the assigned images. The complete per-path bounding boxes and inventory mapping are in report.json and scripts/C_path_index.json. The compact list below records every path.','','| C contour | Physical locus | Visual source |','|---|---|---|']
for ob in idx:lines.append(f"| {ob['path']:02d} | {ob['location']} | {ob['inspected_on']} |")
lines+=['','## Limits and checks','','No mathematical theorem or computation was tested; `check_events` is empty. The graphic labels OK are literal authorial labels and supply no independent proof-check evidence. No geometry is regularized and no mathematical repair is proposed.','','The c10 faint area near (1446,2100) gives diffuse shading and paper grain without a stable stroke candidate; no character or invented path is supplied. The lower-field hook and the listed isolated spots have supported visible shapes and remain qualified as to origin.','','Crop c02 retains all endpoints of its marked-oval/miniature/word targets; unrelated left context and the upper edge of the lower quadrilateral are clipped. Crop c05 retains all target-group endpoints; unrelated upper disks appear only as clipped context along its upper edge. No target was recropped.','','Structural source checks will be recorded after the final synchronized read.']
(out/'reading.md').write_text('\n'.join(lines)+'\n')
print('Wrote reading.tex, report.json, reading.md; retained',count,'C contours; added',len(new),'physical trace entries.')
