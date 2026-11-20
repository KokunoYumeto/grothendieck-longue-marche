from pathlib import Path
import json
from datetime import datetime, timezone
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan003/reader_C')
source=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan003.jpg')
s=Path('/workspace/scratch/7178efd1cfac/reader_inputs/scan003/C.tex').read_text()
changes=[
(r'{\unsure{\mathbb F|F}}_1 \arrow[l',r'\mathbb F_1 \arrow[l'),
(r'{\unsure{f|F}}_1 \arrow[r',r'f_1 \arrow[r'),
(r'\mu^{\unsure{4|1}}_1',r'\mu^4_1'),
(r'&l\\',r'&\ell\\'),
(r'\texttt{MATHEMATIQUES\unsure{.}\hspace{8em}5}',r'\texttt{MATHEMATIQUES.\hspace{8em}5}'),
(r'I_A\,\unsure{\circ|:}\,',r'I_A\,\circ\,'),
(r'\unsure{\mathord{-}\,\mathord{-}|\cdots}\,\unsure{\times|<}\,\Delta_{n_{\unsure{n|r}}}',r'\mathord{-}\,\mathord{-}\,\unsure{\times|<}\,\Delta_{n_n}'),
(r'\mathrm{Ob}\,\Delta_{\unsure{kn\'|n\,n\'}}',r'\mathrm{Ob}\,\Delta_{\unsure{kn\'|n\,n\'|n\'}}'),
(r'\deleted{\unsure{\mathrm{Ob}\,\Delta_n|\mathrm{O}\Delta_n}}',r'\deleted{\mathrm{Ob}\,\Delta_n}'),
(r'{\unsure{\mathbb F|F}}\mathrm{l}(\Delta_n)',r'{\unsure{\mathbb F|F}}\mathrm{l}^{\unsure{\prime}}(\Delta_n)'),
(r'\times\mathrm{Fl}\,\Delta_{n\'\'})',r'\times\mathbb F\mathrm{l}\,\Delta_{n\'\'})'),
]
# Apostrophes in raw strings above are escaped only for Python syntax.
for old,new in changes:
 old=old.replace("\\'", "'");new=new.replace("\\'", "'")
 if old not in s: raise SystemExit('Missing replacement: '+old)
 s=s.replace(old,new,1)
# Filled right ends, hollow left ends of the two upper ovals.
s=s.replace(r'\draw (1095,68) circle[radius=4] (1181,70) circle[radius=4];',r'\draw (1095,68) circle[radius=4];\fill (1181,70) circle[radius=4];')
s=s.replace(r'\draw (1342,63) circle[radius=4] (1490,72) circle[radius=4];',r'\draw (1342,63) circle[radius=4];\fill (1490,72) circle[radius=4];')
# Add only small visible marks missing from otherwise checked C drawings.
s=s.replace(r'\draw[->] (459,1067)--(503,1060);',r'''\draw[->] (459,1067)--(503,1060);
% Small contour returns; their semantic status as arrows is not asserted.
\draw (267,1049)..controls(275,1048)and(283,1033)..(291,1024)
 (291,1024)..controls(280,1032)and(271,1040)..(267,1049)
 (294,1021)--(292,1031)
 (340,998)--(349,1001)--(350,1006)
 (598,1019)--(596,1028)--(603,1024);''')
s=s.replace(r'\draw (1326,876)',r'\fill (1315,870) circle[radius=1.3];'+'\n'+r'\draw (1326,876)',1)
s=s.replace(r'(2041,735)--(2047,752) (2153,730)--(2153,756) (2163,735)--(2162,746);',r'''(2041,735)--(2047,752) (2153,730)--(2153,756) (2163,735)--(2162,746);
\fill (1738,730) circle[radius=1.1];''')
s=s.replace(r'{} \& \& \& \&'+ '\n'+r'\end{tikzcd}}',r'\bullet \& \& \& \&'+ '\n'+r'\end{tikzcd}}',1)
s=s.replace(r'\arrow[from=1-1,to=2-1,dash,shift left=.22ex]',r'''\arrow[from=1-1,to=4-1,shift left=.22ex]
\arrow[from=1-1,to=2-1,dash,shift left=.22ex]''',1)
s=s.replace(r'\draw (1010,1405)--(1147,1397)--(1272,1394)--(1404,1382)--(1496,1375);',r'''\draw (1010,1405)--(1137,1398)
 (1148,1397)--(1272,1394)--(1404,1382)--(1496,1375);
\fill (1019,1398) circle[radius=1.5];
\draw (1122,1383)--(1118,1387)
 (1008,1417)--(1017,1413);
\draw (1278,1392) circle[radius=3];''')
s=s.replace('% Lower edge cuts through the last line.',r'''% Lower edge cuts through the last line. No missing subscript is supplied.
% Detached thin rule below the right end of the last formula; function uncertain.
\figure{\begin{tikzpicture}[line width=.4pt]
\draw (0,0)--(2.7,.12);
\end{tikzpicture}}''')
(root/'reading.tex').write_text(s)
manifest=json.loads((root/'crop_manifest.json').read_text())
for m in manifest:m['viewed']=True
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
issues=[]
def add(id,loc,c,h,reading,evidence,confidence,bbox,dc,dh,kind='misread symbol or index',crop='',unresolved=False,marked='no'):
 issues.append(dict(id=id,location=loc,C=c,H=h,reading=reading,evidence=evidence,confidence=confidence,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=marked,crop=('crops/'+crop+'.png') if crop else '',bbox=bbox,unresolved=unresolved))
add('01_tick','Upper left, before F row','check mark','omitted','check mark','The large rising stroke has a short downstroke at its left, forming a separate check mark; it is not an F stroke.','high',[40,70,230,211],False,True,'omission')
add('02_first_F','First object of upper diagram',r'\unsure{F|\mathbb F}_0',r'F_0',r'\unsure{F|\mathbb F}_0','C doubt retained. Two short bars and a disconnected lower upright/drop remain. The interrupted stem does not establish whether one or two full verticals were intended.','low',[158,130,214,204],False,True,crop='01_upper_F_row',unresolved=True)
add('03_upper_F1','Second object of upper diagram',r'\unsure{\mathbb F|F}_1',r'F_1',r'\mathbb F_1','C doubt resolved. Two distinct vertical strokes enclose white space above the middle arm; both join at the lower stem.','high',[307,125,373,203],True,True,crop='01_upper_F_row')
add('04_upper_F2','Third object and final dot of upper diagram',r'\mathbb F_2.',r'F_2',r'\mathbb F_2.','The F has two separated uprights; a separate round stop follows the 2. C agrees; H loses both the doubled stem and final dot.','high',[447,121,519,201],False,True,crop='01_upper_F_row')
add('05_labels','Upper s/t labels and second sigma label','s1 above t1; s2 above t2; sigma1, sigma2','same','same','Contextual C doubt resolved: all four left arrowheads point left; s labels lie above their upper shafts and t labels below their lower shafts. Numerals 1 and 2 are independently visible. Sigma2 has the same loop-and-topbar family as sigma1.','high',[211,106,449,256],False,False,'other',crop='01_upper_F_row')
add('06_sigma_F0','First object of sigma row',r'\mathbb F_0',r'F_0',r'\mathbb F_0','Two clear vertical strokes meet under the middle bar. C agrees; the doubled stem is not inferred from other objects.','high',[166,324,224,391],False,True,crop='02_sigma_row')
add('07_sigma_tip','First sigma shaft terminal',r'\unsure{\cdot|>}',r'\longrightarrow',r'\unsure{\cdot|>}', 'C doubt retained. A short downward peg is attached to the shaft near its right end. There is no complete, independently resolved right-pointing chevron. The diplomatic alternatives preserve uncertainty about the head, not about the shaft.','low',[228,350,298,381],False,True,crop='02_sigma_row',unresolved=True)
add('08_lower_f','Middle object of sigma row',r'\unsure{f|F}_1',r'F_1',r'f_1','C doubt resolved: the top is a rounded hook turning right and the single upright crosses one short bar; it is the lower-case f form, unlike the flat two-arm final F.','high',[303,320,362,393],True,True,crop='02_sigma_row')
add('09_mu4','First mu superscript',r'\mu_1^{\unsure{4|1}}',r'\mu_1^1',r'\mu_1^4','C doubt resolved to the visible live 4: a diagonal and crossing horizontal enclose a small triangular counter; the right upright continues below the crossbar. The strokes may be retraced, but no separately recoverable earlier numeral is asserted.','high',[187,438,259,541],True,True,crop='03_mu_row')
add('10_other_mu','Second and third mu groups',r'\mu_1^2,\mu_2^2','same','same','Contextual C doubt resolved: both superscripts are curved-top 2s ending in a horizontal baseline; lower indices are 1 and 2. Long mu descenders are visible on all three.','high',[276,438,440,533],False,False,'other',crop='03_mu_row')
add('11_ell','Vertical a/l/r group',r'a,l,r',r'a,\ell,r',r'a,\ell,r','C contextual doubt resolved: the middle letter has a narrow ascender loop and a curled right foot; the three letters occupy separate levels. a and r agree with both witnesses.','high',[192,593,249,762],True,False)
add('12_address','Sideways typewritten label','MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES plus doubtful stop; 5','address omitted','MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES.; 5','All named words are directly readable after clockwise rotation. Capitals are unaccented; ALEX ends in a round full stop. The isolated 5 belongs to the same typed label and is not a manuscript folio.','high',[806,492,982,1238],False,True,'omission',crop='05_typed_label')
add('13_label_stop','Terminal mark after MATHEMATIQUES',r'\unsure{.}','omitted','.','C doubt resolved to a stop, with medium confidence: a distinct small round dark point lies just after the lower right of S at its baseline. Its size is smaller than the ALEX stop, but its location and separation are punctuation-like.','medium',[939,951,972,988],True,True,'misread symbol or index',crop='05_typed_label')
add('14_map_circle','Map separator after I_A',r'\unsure{\circ|:}',r'\cdot\text{ inside subscript}',r'\circ','C doubt resolved: one closed oval with a white centre is visible; there are not two separated dots.','high',[604,833,632,870],True,True,crop='04_map')
add('15_map_letter','First S-like letter of map',r'\unsure{S|s|\delta}',r'S\text{ inside subscript}',r'\unsure{S|s|\delta}','C doubt retained. A closed high loop leads into a long descending diagonal and an open lower turn. The target S is wider and unlooped. Shape and case of the first letter remain uncertain.','low',[627,807,663,872],False,True,crop='04_map',unresolved=True)
add('16_map_placement','Baseline and subscript of map',r'I_A\circ S\longrightarrow S',r'I_{A\cdot S}\longrightarrow S',r'I_A\circ\unsure{S|s|\delta}\longrightarrow S','Only A is lowered below the foot of I. The circle and narrow following letter stand higher, beside I; H places an entire group into the subscript. I has long top and bottom serifs.','high',[520,800,780,905],False,True,'insertion or placement',crop='04_map')
add('17_small_oval','Small upper oval and descending arrow','both ends hollow','right marked end only','left hollow; right filled; partial extra top arc; down arrow','The left endpoint is an open ring. The right endpoint is solid at this scale and joins a retraced short upper cap. H has neither the left ring nor the extra cap; C has the cap but leaves the right point hollow.','high',[1088,37,1218,118],True,True,'drawing or diagram')
add('18_big_oval','Larger upper oval','both ends hollow','both ends filled','left hollow, right filled, descending arrow','Left endpoint has a clear white hole; right endpoint is filled. The down arrow is separate to the right and is present in both witnesses.','high',[1332,22,1568,119],True,True,'drawing or diagram')
add('19_hatching','Disc and two adjacent hatched lenses','disc: 4 upper/3 lower strokes; lenses: 3 left/7 right strokes','disc: 3 upper/2 lower; lenses: 3 left/3 right','retain the checked C hatching','Separate diagonals can be counted, including seven short obliques in the right lens and three below the disc diameter. They are drawn strokes, not filling texture.','high',[1078,119,1544,235],False,True,'drawing or diagram')
add('20_four_points','Four-point segment','loop over second point','four ordinary filled points','four points with the small loop over the second','The second point is circled by a short upper arch in addition to its dark junction; H regularizes it to an ordinary dot.','high',[730,275,1080,319],False,True,'drawing or diagram')
add('21_single_lens','Long upper middle lens with upward arrow','left endpoint hollow, right filled','both endpoints filled','retain C','The left endpoint is an open circle, while the right is black where the rising arrow begins. Both arcs and the upward head are secure.','high',[722,331,1127,458],False,True,'drawing or diagram')
add('22_sphere_arcs','Oval with internal arcs','upper domed arc, middle line, two lower arcs','flat internal almond only','retain C internal arc inventory','Inside the vertical oval, the upper arc rises well above the middle line; two separate lower curves are also visible. H drawing suppresses the middle straight line and flattens/reduces these paths.','high',[1230,225,1365,368],False,True,'drawing or diagram')
add('23_curved_arrow','Curved arrow to right of oval','left/down arrowhead','plain arc','left/down arrowhead','The left end bends to a pointed down-left head. The right end has no head. H actual drawing is an undirected arc.','high',[1412,242,1526,314],False,True,'drawing or diagram')
add('24_two_strips','Two-cell vertical and horizontal strips','gaps, short returns, middle peg','closed regular rectangles','retain checked C details','Vertical strip: a small gap between upper-left side and top, plus a short peg at the middle rule. Horizontal strip: a gap and inward/upward return at the lower right of the left cell. H closes and straightens these details.','high',[1676,216,2029,385],False,True,'drawing or diagram')
add('25_three_strips','Vertical and horizontal three-cell strips','retraced boundaries and projecting returns','regular rectangles; horizontal strip made heavy','retain checked C geometry','Repeated boundary paths are separated in places rather than one uniform thick outline. The second internal vertical of the horizontal strip projects below its bottom edge and turns left. C explicitly preserves these paths.','high',[1243,455,1809,740],False,True,'drawing or diagram')
add('26_square','Curved two-by-two block','gap and inward return; doubled vertical','regular closed smoothed block','retain C; add small detached dot at upper-left','Top-left side begins separately from the top; the first middle-horizontal stroke stops with an inward/upward return; the interior vertical is repeated. A tiny detached dark point precedes the upper-left top stroke.','high',[1308,846,1560,1039],True,True,'drawing or diagram')
add('27_axis','Marked horizontal line at right','four graduation marks and separate slanted initial stroke','one initial upright and four marks','retain C; add small detached dot above its left portion','Four transverse marks are present. At the left, the long downward upright and a separate higher slanted short stroke coexist; the first interval is retraced below. A tiny detached dark point appears beside the high slant.','high',[1700,703,2178,874],True,True,'drawing or diagram')
add('28_product_dashes','Long right product continuation',r'\unsure{-\,-|\cdots}',r'\cdots',r'\mathord{-}\,\mathord{-}','C doubt resolved as visible horizontal marks: the first continuation stroke extends rightwards from the preceding multiplication cross; one further separate dash follows. No three separate round ellipsis dots are resolved.','high',[1974,927,2082,972],True,True,crop='06_long_product')
add('29_product_cross','Sign before last triangle',r'\unsure{\times|<}',r'\times',r'\unsure{\times|<}','C doubt retained. Two slants form an open-right angle, with a very short extra spur at the crossing. The upper/lower arms do not fully settle a cross versus an angle.','low',[2083,925,2121,966],False,True,crop='06_long_product',unresolved=True)
add('30_nested_n','Final nested index of long product',r'\unsure{n|r}',r'n',r'n','C doubt resolved: the small final character has an upright followed by an arch that descends again and turns slightly up at its end; this is an n rather than a single r shoulder.','medium',[2190,935,2226,980],True,False,crop='06_long_product')
add('31_joined_lenses','Two joined lenses at middle left','axis arrow and second lower arc; upper contour marks absent','two plain axial lenses','C geometry plus small contour returns/loop on upper arcs','The right lens has two lower curves and a right-pointing triangle on its axis. Additional small returns interrupt both upper arcs, and a narrow loop follows the upper-left rising outline. These marks are traced without asserting that every return is an arrow.','high',[254,984,653,1128],True,True,'drawing or diagram',crop='12_joined_lenses')
add('32_chain_endpoints','Four horizontal right arrows and left downward branch','initial and final dots, downward endpoint blank','only far-right terminal dot','initial and far-right dots; small dot below downward arrow','A separate small dark diamond is visible below the downward arrowhead; the horizontal branch starts in a black point. H lacks the initial and lower dots; C lacks only the lower dot. Four rightward heads are secure.','high',[1215,1156,1696,1323],True,True,'drawing or diagram')
add('33_products_positions','Three separate products on page','separate source blocks','combined into one display','retain separate blocks','The long product lies at right middle; the unfinished product lies farther down at left; the doubled-triangle product lies near the lower right. H combines distant formulas in one display.','high',[341,908,2232,1387],False,True,'insertion or placement')
add('34_grid','Lower-left rectangular diagram','4 columns by 3 rows, internal Downarrows and hatching, plain vertical boundaries','3 by 3 plain grid; no internal arrows/hatching','4 by 3 with C details plus visible long downward left-edge head','Five vertical boundaries delimit four columns; four horizontal levels delimit three rows. Every horizontal row has four right arrows. Twelve cell marks have paired descending shafts; hatching lies in the first column. The heavily retraced left boundary has a downward termination.','high',[676,1319,985,1570],True,True,'drawing or diagram',crop='10_grid')
add('35_four_lobes','Four linked lower cells','three paths per cell plus internal down strokes; continuous first axial segment; some tiny marks absent','four cells with internal almond; interior short arrows omitted','retain C paths/down strokes; add first-axis gap, dot, small open ring and contour returns','The first straight internal line stops short of the first joint. A dot lies inside the first upper-left corner and a small open ring sits beside the central dark joint. Twelve short interior vertical/hooked strokes are visible. The first two top contours have tiny returns/gaps.','high',[997,1333,1509,1491],True,True,'drawing or diagram',crop='11_four_lobes')
add('36_double_triangles','Product above foot formulas','both triangles traced with doubled left edges',r'\Delta_n\times\Delta_{n\'}','retain C double-edge triangles and n, n-prime','Contextual C doubt resolved: each triangle has two distinct adjoining left diagonals, while the product higher at left uses single diagonals. The second index has one detached prime. No uncertain alphabet name is assigned to the traced outline.','high',[1541,1294,1793,1384],False,True)
add('37_bottom_F0','Initial symbol of first foot equality',r'\mathbb F_0',r'F_0',r'\mathbb F_0','Two uprights enclose white space in F; 0 is a separate small oval below. C agrees.','high',[1408,1458,1459,1531],False,True,crop='07_first_equality')
add('38_bottom_index','First foot equality Delta subscript',r'\unsure{kn\'|n\,n\'}',r'n\'',r'\unsure{kn\'|n\,n\'|n\'}','C doubt retained and widened. A tall narrow leading stroke/loop precedes a larger n-shaped arch and a detached prime. The leading strokes could form k, a cramped first n, or a retraced start of n. H single n-prime does not account for them securely enough to resolve the locus.','low',[1631,1460,1690,1519],True,True,crop='07_first_equality',unresolved=True)
add('39_deleted_first','First cancelled group in F1 equality',r'\deleted{\unsure{Ob\,\Delta_n|O\Delta_n}}',r'\struck{\ill{}}',r'\deleted{Ob\,\Delta_n}','C doubt resolved with medium confidence: an initial closed O, a taller b stroke, a small triangular outline and a low n survive beneath ascending cancellation strokes. H leaves the group wholly unreadable.','medium',[1522,1531,1648,1605],True,True,'readable ink left as \\ill{}',crop='08_second_equality',marked='yes')
add('40_deleted_second','Underlying group overwritten by live Fl',r'\deleted{\unsure{Ob}}',r'part of \struck{\ill{}}',r'\deleted{\unsure{Ob}}','C doubt retained: a lower closed loop and rightward return survive below the live horizontal F bars, consistent with Ob, but their overlap does not independently settle both old letters.','low',[1643,1522,1714,1600],False,True,'deletion state',crop='08_second_equality',unresolved=True,marked='yes')
add('41_live_Fl','Live Fl after cancellation',r'\unsure{\mathbb F|F}l',r'Fl',r'\unsure{\mathbb F|F}l','C doubt retained. Two uprights are visible, but one shares the outline of the overwritten group. The live top and middle arms are secure, as is the following tall looped l.','medium',[1643,1516,1731,1601],False,True,crop='08_second_equality',unresolved=True)
add('42_prime_after_l','Small detached stroke after live l and before opening parenthesis','omitted','omitted',r'l^{\unsure{\prime}}(','A separate short oblique dark stroke lies at upper-letter height between the looped l and the opening parenthesis. It looks prime-like; intentional punctuation cannot be distinguished from an isolated pen mark. Included as an in-place doubt, not silently removed.','low',[1718,1523,1735,1545],True,True,'omission',crop='08_second_equality',unresolved=True)
add('43_bottom_relation','Beginning of clipped final line',r'F\mathrel{\unsure{-|=}}',r'F_2=',r'F\mathrel{\unsure{-|=}}','C doubt retained: one horizontal bar and the upper part of F are visible. No left subscript is recoverable. A second equality bar could be beyond the clipped/lost lower portion, but none is supplied as certain.','low',[1398,1610,1525,1664],False,True,crop='09_clipped_equality',unresolved=True)
add('44_last_Fls','Both Fl groups on final line',r'\mathbb F l\ (\Delta_n)\times Fl',r'Fl(\Delta_n)\times Fl',r'\mathbb F l\ (\Delta_n)\times\mathbb F l','Both capital Fs show two distinguishable verticals, including the second F before the final Delta. This resolves the contextual alphabet issue; C already doubles the first but not the second.','high',[1540,1581,1968,1655],True,True,crop='09_clipped_equality')
add('45_final_argument','Right end of final formula',r'\Delta_{n\'\'})',r'(\Delta_{n\'})',r'\Delta_{n\'\'})','Contextual C doubt resolved as visible ink: two separate raised strokes follow n and a closing parenthesis follows them. There is no opening parenthesis between this Fl and Delta. These visible asymmetries are preserved without correction.','high',[1958,1572,2091,1645],False,True,crop='09_clipped_equality')
add('46_bottom_rule','Thin line below final formula at right','omitted','omitted','separate rising thin rule, traced','A distinct thin oblique line begins below the last formula and runs to the right edge. Its function is not established; it is represented as a separate graphic line rather than silently treating it as formula punctuation or underlining.','high',[2000,1629,2355,1661],True,True,'omission')
# Apostrophes escaped solely for Python literals are normalized in the report.
for q in issues:
 for k in ['C','H','reading']:
  q[k]=q[k].replace("\\'", "'")
inventory=[]
def inv(element,kind,box,first,sheet='text',hand='his hand'):
 inventory.append({'element':element,'kind':kind,'position':f'whole-image bbox {box}','first_words_or_objects':first,'sheet_kind':sheet,'hand':hand,'transcribed':'yes'})
inv('Upper small oval and its arrow','drawing',[1088,37,1218,118],'two-ended oval; partial upper cap; down arrow')
inv('Upper larger oval and its arrow','drawing',[1332,22,1568,119],'hollow left end, solid right end; down arrow')
inv('Large check mark','drawing',[40,70,230,211],'check mark',hand='unattributed hand; heavy check mark')
inv('Top capped interval and downward arrow','drawing',[715,77,969,151],'interval with short end caps; downward arrow')
inv('Upper F diagram','diagram',[158,106,519,256],'F0; doubled F1, F2; two left arrows for each pair')
inv('Hatched bisected disc','drawing',[1078,119,1222,235],'horizontal diameter; four upper and three lower hatches')
inv('Two joined hatched lenses','drawing',[1283,119,1544,212],'three vertex marks; three left and seven right hatches')
inv('Three-point segment','drawing',[732,164,969,193],'three filled points on segment')
inv('Vertical two-cell strip','drawing',[1676,216,1781,385],'two stacked cells, gap, middle peg')
inv('Horizontal two-cell strip','drawing',[1861,225,2029,338],'two adjacent cells; lower gap/return')
inv('Oval with internal arcs','drawing',[1230,225,1365,368],'oval, upper inner dome, line, lower arcs')
inv('Separate curved arrow','drawing',[1412,242,1526,314],'arc ending down-left')
inv('Four-point segment','drawing',[730,275,1080,319],'four points; second has small extra loop')
inv('Sigma diagram','diagram',[166,307,529,395],'doubled F0, f1, F2; sigma labels')
inv('Long lens and ascending arrow','drawing',[722,331,1127,458],'hollow left endpoint, filled right endpoint, up arrow')
inv('Mu row','display',[187,438,440,541],'mu with lower/upper 1/4, 1/2, 2/2')
inv('Vertical three-cell strip','drawing',[1243,455,1371,740],'three stacked cells, repeated edges')
inv('Horizontal three-cell strip','drawing',[1492,455,1809,583],'three adjacent cells, projecting second division')
inv('Sideways typed address label','text',[806,492,982,1238],'MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES.; 5','reused_typed','unattributed typist')
inv('Vertical letter list','display',[192,593,249,762],'a; looped ell; r')
inv('Marked right-hand interval','drawing',[1700,703,2178,874],'long left upright, extra slanted stroke, four ticks, small dot')
inv('Map at left centre','display',[520,800,780,905],'I_A circle S-like letter to S')
inv('Curved two-by-two block','drawing',[1308,846,1560,1039],'four cells, open return, repeated division, small dot')
inv('Long product','display',[1773,906,2228,1000],'Delta_n1 times Delta_n2; two horizontal marks; last nested n')
inv('Joined middle-left lenses','drawing',[254,984,653,1128],'two joined lenses; axis arrow; two lower curves at right')
inv('Tiny capped interval','drawing',[1850,1078,1958,1119],'short horizontal line with end caps')
inv('Four right arrows and downward branch','diagram',[1215,1156,1696,1323],'four right steps; left down arrow; endpoint dots')
inv('Unfinished left product','display',[341,1251,539,1326],'Delta_n1 times bare Delta')
inv('Doubled-triangle product','display',[1541,1294,1793,1384],'double-left-edge triangle_n times triangle_n-prime')
inv('Four-by-three grid','diagram',[676,1319,985,1570],'four columns, three rows, right arrows, down double shafts, first-column hatching')
inv('Four linked lobed cells','drawing',[997,1333,1509,1491],'four linked cells with internal arcs and short down marks')
inv('First foot equality','display',[1400,1445,1700,1528],'doubled F0 = Ob Delta with doubtful compound subscript')
inv('Second foot equality','display',[1400,1505,2040,1610],'F1 = cancelled groups then live Fl with doubtful prime (Delta_n) times Ob Delta_n-prime')
inv('First cancellation','deletion',[1522,1531,1648,1605],'Ob Delta_n struck through')
inv('Second overwritten cancellation','deletion',[1643,1522,1714,1600],'doubtful Ob under live Fl')
inv('Final clipped formula','display',[1390,1582,2090,1683],'F; one bar; doubled Fl(Delta_n) times doubled Fl Delta_n-double-prime)')
inv('Archive numeral','text',[60,1588,108,1657],'2; retained only as archive comment',hand='unattributed archival hand')
inv('Detached lower rule','drawing',[2000,1629,2355,1661],'thin oblique rule toward right edge')
# Stable sorting by physical upper extent, retaining order for equal heights.
inventory.sort(key=lambda a:int(a['position'].split('[')[1].split(',')[1]))
notes=[
'One landscape sheet, 2371 by 1691 pixels. The halves are left and right crops; all reported boxes use the whole-image coordinates.',
'The foreground consists principally of handwritten diagrams, cell sketches and formulas, with one sideways typewritten address label. The whole, a, b, then twelve single decision crops were each viewed once.',
'No further genuinely readable type was established beyond the address label. Pale grey formula-like remnants and paper/label boundaries are visible; they do not establish an additional continuous typed text block. Nothing has been reconstructed from H’s editorial show-through assertion.',
'The page records F-object/arrows data, sigma arrows and three mu expressions, several Delta products, and tentative formulas involving Ob and Fl. No proposition or proof is stated in a form checked in this run.',
'No explicit verbal author doubt, title or date is present. The isolated typed 5 is on the address label. No manuscript folio is identified; the lower-left 2 is retained as an archive comment.',
'The final line is clipped through its lower portion. The reading retains one visible relation bar, no supplied F subscript, two terminal prime strokes and a closing parenthesis without an invented matching opener.',
'The first mu exponent is read from its visible crossed, triangular form as 4. Possible earlier writing underneath is not claimed as a readable cancelled 1.',
'Small extra contour returns, isolated dark points next to drawings, and a thin bottom-right rule have been preserved without assigning them a mathematical role.',
'The H_drawing.tex file was checked as the actual second graphic witness. Its editorial description was not counted again where the actual drawing supplied the object.',
'No new mathematical proof check was performed; diagram counts and symbol distinctions are observations of ink rather than proof verification.'
]
notation=[
{'sign':'F / doubled F / f','evidence':'Upper first F remains interrupted; upper next two, sigma-row first, foot F0, and both final Fl capitals have visibly paired stems. Sigma-row middle has a curved hook and one crossbar, read f. Live Fl over erasure remains F-alphabet doubtful.'},
{'sign':'mu, superscripts and subscripts','evidence':'Long left descender on all three. First upper glyph has a triangular counter and crossbar, read 4; the next two are curved-top 2. Lower indices read 1, 1, 2.'},
{'sign':'circle and narrow S-like glyph','evidence':'Separator is one closed oval, resolved circle. Adjacent high-loop glyph remains S|s|delta; case cannot be settled from the narrow form.'},
{'sign':'triangles','evidence':'The lower-right product has an additional left diagonal on each triangle, traced directly. Separate higher products have single outlines. No abstract alphabet identification is inferred.'},
{'sign':'Ob / Fl','evidence':'O closed loop and b with tall ascending stroke; l is tall looped. First deleted Ob Delta_n partly survives crossing slashes. A second overwritten Ob remains uncertain.'},
{'sign':'typed capitals','evidence':'MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES.; 5 are unaccented typewriter capitals/numeral. ALEX stop is large; MATHEMATIQUES stop is smaller but detached at baseline.'},
{'sign':'prime marks','evidence':'One prime after n in the lower product and second equality; two distinct raised marks after n in the final argument. An additional detached stroke after the live l in F1 is retained as an uncertain prime.'},
{'sign':'sigma1 endpoint','evidence':'The shaft ends with a tiny downward peg. The dot/head alternative is retained; a complete chevron is not resolved.'}
]
report={'scan':3,'reader':'C','model':'GPT-6 Astra Pro','effort':'inherited/not exposed','started_utc':'2026-11-20T09:19:12.976193+00:00','finished_utc':datetime.now(timezone.utc).isoformat(),'views':[str(source),str(source).replace('.jpg','_a.jpg'),str(source).replace('.jpg','_b.jpg')]+[m['path'] for m in manifest],'issues':issues,'inventory':inventory,'notes':notes,'notation':notation,'checks':[],'crop_count':len(manifest),'brief_feedback':'The bounded whole/halves/crop workflow was sufficient. One clarification would help: how to encode an unmistakable small shaft-end peg whose semantic dot-versus-arrow reading is unsettled; this report keeps C’s explicit alternative while describing the actual peg. No additional crops were made for differences already settled by the halves.'}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
log='''# Scan 003 — independent reader C

Model: GPT-6 Astra Pro. Effort: inherited/not exposed. Whole source: 2371 × 1691 pixels.

## Source-view register

1. Whole image viewed once for the full landscape layout, all foreground blocks, label, marks, drawing groups and clipped lower edge.
2. Half a viewed once. Checked the upper-left F row, both sigma shafts, all mu indices, a/ell/r, map, typed label, left-side lenses, partial product and grid.
3. Half b viewed once. Checked upper ovals/hatching, sphere/arc, strips, marked line, four-cell square, right product, arrow chain, doubled triangles and all foot formulas.
4. Decision crops 01–12 viewed once each, in numerical order. Exact source boxes, rotation and LANCZOS enlargement are in crop_manifest.json. No OCR, recognition, web, other scan or other reader file was used.

## Element-by-element checked register

- **Upper F row:** all three objects, 0/1/2, four left arrowheads, s/t baselines and terminal dot compared to C and H. C’s first F doubt retained; second and third doubled stems confirmed. Both witnesses agree on arrow direction/labels. H lacks the doubled alphabet and terminal dot.
- **Sigma row:** doubled F0, curved lowercase f1, plain F2 and sigma1/sigma2 checked. First terminal peg remains ambiguous; second rightward end accepted. C f/F doubt resolved to f.
- **Mu row:** all three letters, descenders, superscripts and subscripts checked. First superscript has the visible crossed 4 form; following upper 2s and lower 1/2 agree with both witnesses.
- **a / ell / r:** three distinct vertical levels; looped middle ell. No extra text or punctuation. C’s l is represented as ell; H uses ell.
- **Top drawing groups:** capped interval/down arrow and three-dot line agree. Small oval has an extra upper cap, open left and solid right ends. Larger oval likewise has open left/solid right ends. Disc and paired-lens hatching counted. H’s actual file, not only its prose, loses several marks.
- **Four-point segment and long lens:** counted four points, checked extra loop over point two, open/filled lens endpoints and upward arrow. C retains those distinctions; H simplifies them.
- **Oval with inner paths and nearby curved arrow:** upper domed inner arc, straight middle line and lower retraced arcs checked separately. The nearby curve has a left/down head. H actual drawing omits that head.
- **Two- and three-cell strips:** checked cell counts, open endpoints, inward returns, middle peg, multiple retraced paths and projecting vertical on three-cell horizontal strip. C’s geometry reused after comparison.
- **Typed address:** clockwise crop reads MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES.; and the separate 5. Every word/capital and both stop locations checked. No accent inserted. Small final stop accepted with medium confidence. H omits the label.
- **Other possible type:** no additional genuinely readable type established beyond the address. Pale formula-like remnants do not yield a continuous typed text block. They were not reconstructed from H’s editorial comment and were not assigned invented word counts.
- **Map:** I has two serifs, A alone is lowered. Single hollow separator resolved as circle. High-loop first S-like glyph remains S/s/delta. Rightward arrow and final S agree with both witnesses; H’s enlarged subscript does not match vertical placement.
- **Right marked line and two-by-two block:** ticks, doubled/extra strokes, gaps, inward returns and two small detached dark points checked. C geometry retained with the two tiny points added.
- **Long right product:** both first triangles and nested 1/2, two visible horizontal continuation marks, final cross/angle and nested final n inspected. Dashes and final n resolved; cross/angle remains. No ellipsis dots invented.
- **Joined lenses at left:** both contours and axes, extra lower curve on right, rightward axial arrow and small upper-outline loop/returns checked. Upper marks traced without imposing a directional interpretation.
- **Tiny interval:** horizontal stroke and two end caps agree with C and H drawing.
- **Four-step right chain with downward branch:** all heads point as recorded. Initial/final black points checked. A small separate point below the down head was omitted by both and has been added.
- **Unfinished product:** Delta indexed n1, multiplication cross and bare second Delta agree with both; no missing factor supplied.
- **Grid:** five vertical boundaries and four horizontal levels give four columns by three rows. All sixteen rightward row arrows and twelve paired downward cell marks checked, along with first-column hatching and left-edge downward termination. H actual drawing has only three columns and omits internal arrows/hatching. C retained and left-edge head added.
- **Four linked cells:** each upper contour, axis, two lower outlines, short internal down/hooked strokes, joints and gaps checked. C is substantially accurate. Added the first-axis gap, tiny first-cell point, central open ring and small contour returns; H lacks all the interior short strokes.
- **Lower-right product:** both triangles have distinct doubled left diagonals, indices n and n-prime. C tracing retained. H’s plain Delta loses the doubled edges.
- **First foot equality:** doubled F0, equals, Ob, triangle and crowded index checked. Index remains kn-prime / n n-prime, now also allowing a retraced single n-prime. No mathematical normalization.
- **Second foot equality:** F1, equals, first struck Ob Delta_n, second overwritten Ob-like group, live Fl, parentheses, Delta_n, multiplication, Ob and Delta_n-prime checked. First deleted reading resolved with medium confidence; second and live-F alphabet doubt retained. A detached prime-like stroke after l, omitted by both, is included as doubtful.
- **Final clipped line:** no F subscript supplied; one bar remains with minus/equality doubt. Both Fl capitals have paired stems. The final n has two prime strokes; closing parenthesis present, matching opening absent. Visible asymmetry retained.
- **Lower marks:** separate thin rightward rising rule traced. Lower-left 2 is an archive annotation, retained only as a comment, not a manuscript folio. No date, title or author’s verbal uncertainty appears.

## C doubts: explicit disposition

Resolved: upper second F doubled; sigma middle f; first mu exponent 4; other mu labels/indices; looped ell; typed small terminal stop; single map circle; visible two horizontal continuation marks; final nested n; first deleted Ob Delta_n; doubled lower triangles; two final primes; missing final opening parenthesis; alphabet of both final Fl capitals.

Retained: first upper F/F-double; sigma1 peg dot/head; first map S/s/delta; final product cross/angle; first foot subscript (with single retraced n-prime added as an alternative); second overwritten Ob; alphabet of live Fl over erasure; final one-bar minus/equality. New doubt: detached prime-like mark after live l in F1.

## Verification limits

No proof or background theorem check was performed. Counts and glyph observations are diplomatic checks of ink. All detailed disagreements have a crop or a whole-image bounding box in report.json. No additional image was opened after the twelve designated crop views.
'''
(root/'read_log.md').write_text(log)
print(json.dumps({'issues':len(issues),'crops':len(manifest),'inventory':len(inventory),'files':['reading.tex','report.json','read_log.md','crop_manifest.json']},ensure_ascii=False))
