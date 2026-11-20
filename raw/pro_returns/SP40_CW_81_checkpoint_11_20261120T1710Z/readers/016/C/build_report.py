from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/016/C'
D=[]
def row(id,location,C,H,reading,evidence,confidence='medium',kind='other',diff_C=False,diff_H=False,status=None,crop=None,bbox=None,source=None,group=None):
    d=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,readers_crop=crop,bbox=bbox)
    if source:d['C_source_doubt_row']=source
    if group:d['physical_group']=group
    D.append(d)
row('D01','Opening union, second Sigma subscript',r'\Sigma_{\deleted{\unsure{2}}1}^+',r'\Sigma_1^+',r'\Sigma_{\deleted{\unsure{2}}1}^+','The heavy live 1 has an additional hooked shoulder. The predecessor candidate 2 remains obscured by the heavy upright and foot; its full earlier contour cannot be recovered. H has the live index only.','low','omission',False,True,'retained','c01_subscript.png',[840,114,926,158],'01')
row('D02','Opening verb cluster before un ouvert',r'\deleted{\unsure{sera|sont}} est','serait',r'\deleted{\unsure{sera|sont}} est','The compact overwriting has a live e loop, following low connecting strokes and a tall terminal t-like stroke. The predecessor is still compatible with sera or sont. The crop does not show the separate continuation required for H’s serait. The whole overwritten cluster receives one H difference.','medium','misread word',False,True,'retained','c02_old_verb.png',[973,96,1082,139],'02')
row('D03','Far right of opening first line',r'\unsure{connexe}','connexe','connexe','The initial c/o and connected n/n/e/x/e run can be followed to the terminal downturned stroke. The separate line below is recorded as G03.','high','other',True,False,'resolved','c03_right_insertions.png',[1460,113,1665,149],'03')
row('D04a','Opening right insertion, stroke after X',r'X\unsure{/|\setminus}E_{\unsure{2}}',r'X\setminus E_2',r'X/E_{\unsure{2}}','The intervening stroke is near upright and leans from lower left toward upper right. The slash candidate is selected from that direction; no set-theoretic inference was used.','medium','misread symbol or index',True,True,'resolved','c03_right_insertions.png',[1593,173,1646,218],'04','opening-right-insertion')
row('D04b','Opening right insertion, final subscript at clipped edge',r'E_{\unsure{2}}',r'E_2',r'E_{\unsure{2}}','The low curved tail supports 2, but its continuation reaches the right image edge. The original local qualification remains. H has the same primary digit, so no additional H difference is counted.','low','other',False,False,'retained','c03_right_insertions.png',[1646,188,1685,222],'04','opening-right-insertion')
row('D05','Opening third line, struck writing after donc',r"\deleted{\unsure{c'est}}",r'\struck{\ill{}}',r"\deleted{\unsure{c'est}}",'A short isolated raised stroke and terminal t survive above the strike, with a small initial curve and low dark central remnants. c’est remains a qualified reading. H’s one struck ill placeholder is counted once.','low',r'readable ink left as \ill{}',False,True,'retained','c04_egale_cluster.png',[424,283,586,328],'05')
row('D06','Opening conclusion abbreviation on its own physical line',r'\unsure{cqfd|qfd}','cqfd',r'\unsure{cqfd|qfd}','An open initial curve joins the long descending stem. The crop preserves the entire q and f descenders but does not settle whether that first curve supplies a separate c or the open bowl of q.','medium','other',False,False,'retained','c06_cqfd.png',[243,376,400,526],'06')
row('D07a','First partition, first Sigma',r'\deleted{\unsure{E}}\Sigma_1^+',r'\Sigma_1^+',r'\deleted{\unsure{E}}\Sigma_1^+','A thinner near-upright crosses the dark angular Sigma. Its independent middle arm is not clearly isolated; E remains qualified.','low','omission',False,True,'retained','c07_first_sigma.png',[644,607,706,667],'07','row07-first-partition')
row('D07b','Five-term partition, central Sigma12',r'\deleted{\unsure{E}}\Sigma_{12}',r'\Sigma_{12}',r'\deleted{E}\Sigma_{12}','A separate near-vertical and a short horizontal middle arm survive within the angular replacement, in addition to the upper and lower arms. These local strokes support E.','high','omission',True,True,'resolved','c08_centre_sigma.png',[1004,887,1129,950],'07','row07-centre')
row('D07c','Car paragraph, first expression under closure bar',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}',r'\overline{\Sigma_{12}}',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}','Retraced upper/lower rules are visible, but the earlier upright is largely covered. E remains a low-confidence predecessor candidate, read from this local form rather than from the central correction.','low','omission',False,True,'retained','c11_bottom_predecessors.png',[1030,2018,1159,2104],'07','row07-lower-Sigma')
row('D07d','Car paragraph, E1 after intersection sign',r'\deleted{\unsure{\Sigma}}E_1',r'E_1',r'\deleted{\unsure{\Sigma}}E_1','The upper diagonal within the live E and an angular middle return support the earlier Sigma candidate; the lower diagonal is crowded and remains uncertain.','low','omission',False,True,'retained','c11_bottom_predecessors.png',[1221,2032,1300,2100],'07','row07-lower-E')
row('D08','Initial D of Dans',r'\deleted{\unsure{O}}Dans','Dans',r'\deleted{\unsure{O}}Dans','Several overlapping rounded and upright runs survive inside the dark D. O remains the supported predecessor candidate without a fully separable contour.','low','omission',False,True,'retained','c09_dans.png',[274,1210,384,1300],'08')
row('D09','Raised insertion above cancelled alors, second word',r'\unsure{conclurait}','considérant','conclurait','The visible run has co, short connected middle strokes, a tall narrow loop at l, then the low urai run and terminal t. No separate d loop is visible at the position required by considérant.','high','misread word',True,True,'resolved','c12_lower_insertion.png',[467,2120,790,2169],'09','lower-insertion')
row('D10a','Opening third line, sign after egale/egal',r'\unsure{à|:}','à',':','Two separate small points are stacked vertically. Neither point provides a connected a bowl; the two-point punctuation form is retained as a colon, without changing the surrounding assertion.','high','misread symbol or index',True,True,'resolved','c04_egale_cluster.png',[815,298,840,332],'10','opening-sign')
row('D10b','Opening third line, connective before final inclusion',r"\unsure{donc|d'où}",'donc','donc','A looped d is followed by a continuous low run with a small hump and downturned c ending. No detached apostrophe or raised accent is visible.','medium','other',True,False,'resolved','c05_donc.png',[1110,303,1215,339],'10','opening-connective')
row('D11','Raised insertion above cancelled alors, first word',r'\unsure{en|on}','en',r'\unsure{en|on}','The first letter is a shallow open trough; the following n-like run is clearer. en stays primary, with on retained. The preceding line’s on does not settle this glyph.','medium','other',False,False,'retained','c12_lower_insertion.png',[322,2140,400,2169],'11','lower-insertion')
row('D12a-old','Final long overbar, first amended join: predecessor',r'\deleted{\unsure{\amalg}}',r'\sqcup',r'\deleted{\amalg}','Two uprights and a straight foot extending to the left survive together with a round lower curve. The square-join predecessor glyph is resolved. The final-state question is D12a-live. One H count covers this physical join cluster.','high','misread symbol or index',True,True,'resolved','c13_lower_joins.png',[755,2252,794,2290],'12','first-bottom-join')
row('D12a-live','Final long overbar, first amended join: final form',r'\unsure{\cup|\amalg}',r'\sqcup',r'\unsure{\cup|\amalg}','A rounded lower bowl extends below the square foot. The bowl supports cup as primary, while the superposed square form leaves the intended final sign unresolved. The H overlap is already included in D12a-old.','low','other',False,False,'retained','c13_lower_joins.png',[755,2252,794,2290],'12','first-bottom-join')
row('D12b-old','Final long overbar, second amended join: predecessor',r'\deleted{\unsure{\amalg}}',r'\sqcup',r'\deleted{\amalg}','The local left and right uprights meet a straight extended foot, beneath the darker rounded return. The square-join predecessor glyph is resolved independently here. D12b-live retains the final-form question.','high','misread symbol or index',True,True,'resolved','c13_lower_joins.png',[875,2252,917,2293],'12','second-bottom-join')
row('D12b-live','Final long overbar, second amended join: final form',r'\cup in C.tex; source doubtful-readings row 12 includes both joins',r'\sqcup',r'\unsure{\cup|\amalg}','The heavy round lower return supports cup, while both upright/foot strokes remain. The source doubt row already includes the two joins; carrying that qualification into this formerly unmarked C.tex occurrence is retention of the source doubt, not an additional physical correction.','low','other',False,False,'retained','c13_lower_joins.png',[875,2252,917,2293],'12','second-bottom-join')
row('D13','Foot right, closing bracket candidate',r'\unsure{\big]}',None,'Closing-bracket candidate ]; the local unsure encloses the two visible return paths G10.','The upper and lower short returns are visible; the joining upright is outside the white-sheet area or merges with the image boundary. The bracket candidate remains qualified. H ends the formula without the closing bracket. Only the surviving returns are drawn in reading.tex.','low','omission',False,True,'retained','c14_right_bracket.png',[1630,2215,1685,2334],'13','right-bracket')
# H supplies full text, so a local absence is represented by a descriptive string, not page-level H=null.
D[-1]['H']='no closing bracket after final formula'
row('N01a','Opening third line, accent over the e of egale/egal','é','é',r'\unsure{é|ê}','The raised mark has an angular top with a short returning leg. An acute is the primary candidate; a small circumflex remains supported by the visible two-part angle. This is a new local qualification, not a new H primary reading.','low','other',True,False,None,'c04_egale_cluster.png',[644,283,667,300],group='opening-egale')
row('N01b','Opening third line, endpoint of egale/egal','égale','égal',r'\unsure{é|ê}gal\unsure{e|}','After the tall l, a low rightward return ends with a downturned kink. An e ending remains primary, with an absent separate e as the explicit alternative. H’s égal survives as an alternative, so this H difference is qualified.','medium','misread word',True,True,None,'c04_egale_cluster.png',[730,280,778,331],group='opening-egale')
row('N02','Definition label above equals',r'\text{def}',r'\mathrm{déf}',r'\text{def}','Half a shows the d/e/f run and the f ascender. No separate accent is present above the e.','high','misread word',False,True,None,None,{'image':'J81-02_81_scan016_a.jpg','origin':'top-left of half a = full scan (0,0)','xyxy':[792,1025,874,1105]})
row('N03','End of Sigma12 definition','no terminal period','period after Sigma_2^-','no terminal period','The white space after the second negative Sigma is clear on half a; no endpoint dot is visible.','high','text not on the page',False,True,None,None,{'image':'J81-02_81_scan016_a.jpg','origin':'top-left of half a = full scan (0,0)','xyxy':[1060,1038,1224,1141]})
row('N04','Right edge after sont ouverts','no comma after ouverts','comma after ouverts','no comma after ouverts','The final downturned s reaches the edge-side gap; no separate comma is visible within the supplied sheet. The narrow visible margin limits any assertion about material outside the image.','medium','text not on the page',False,True,None,'c10_ouverts.png',[1604,1223,1685,1311])
row('G01','Guide beneath la comp. conn.','insertion wording without explicit guide path','insertion wording without explicit guide path','Inserted wording retained; bent path G01','A shallow descending curve starts left of la, runs beneath the raised phrase and turns down at its right endpoint before Sigma2. The actual guide is added once.','high','drawing or diagram',True,True,None,'c03_right_insertions.png',[1165,174,1402,238])
row('G02','Guide beneath the right insertion de X/E2','insertion wording without explicit guide path','insertion wording without explicit guide path','Inserted wording retained; bowed path G02','The pale curve begins below/left of de, rises into a broad arch, then continues to the clipped right edge. The separate lower curved mark is the following comma, preserved once as punctuation.','medium','drawing or diagram',True,True,None,'c03_right_insertions.png',[1527,218,1685,250])
row('G03','Short separate rule beneath the final part of connexe','no separate rule','no separate rule','Locally qualified graphical rule G03','A detached near-horizontal rule begins around x1526 beneath the latter part of connexe and reaches the right edge. Its underline/guide role, hand and surface origin remain unresolved; the actual line is drawn with unsure, without assigning it to the whole word.','medium','omission',True,True,None,'c03_right_insertions.png',[1520,145,1685,165])
row('G04','Point above/right of the central overwritten Sigma12','no point','no point','Locally qualified point graphic G04','The crop shows a small isolated gray-dark spot above/right of the central correction, separated from the brace. The contour is preserved without a character or a mathematical role. Hand and surface origin remain open.','medium','omission',True,True,None,'c08_centre_sigma.png',[1135,837,1145,849])
row('G05','Point below/right of avec','no point','no point','Locally qualified point graphic G05','A discrete dark point lies below/right of avec, with no joining stroke. Its position is preserved; role, hand and surface origin remain unresolved.','high','omission',True,True,None,'c18_point_below_avec.png',[426,1123,436,1135])
row('G06','Right blank margin adjacent to the third closure row','no points','no points','Locally qualified two-point graphic G06','Two separate dark compact spots lie on a short rising diagonal. Their two contours are preserved as a single local cluster, with no supplied punctuation or mathematical role. Hand and surface origin remain unresolved.','high','omission',True,True,None,'c17_detached_points.png',[1616,1724,1631,1743])
row('G07','Point above second nonempty-intersection formula','no point','no point','Locally qualified point graphic G07','One small dark wedge-like point is detached above the gap between the second closure term and E2. It is independent of the que descender and the closure bar. Role, hand and surface origin remain unresolved.','high','omission',True,True,None,'c19_point_above_second_closure.png',[923,1889,934,1901])
row('G08','Strike through cancelled alors and its expression','generic deleted annotation','generic struck annotation','Same deleted wording, actual curved cancellation path G08','The strike begins below alors at the left, rises toward the first Sigma and then runs through the expression to the right. The source retains the deleted annotation invisibly for dimensions and draws this one observed cancellation path. No second generic visible strike is added.','high','drawing or diagram',True,True,None,'c12_lower_insertion.png',[300,2170,1053,2217])
row('G09','Underbrace below the first component closure in final equality','ordinary underbrace','descriptive underbrace note','Same label; observed brace with a small return and taller right hook','The right end makes a short upturned return, dips locally and rises again in a taller hook. The one explicit path G09 contains that geometry and the existing subset Sigma2+ cup E2 label. No text correction is counted for the label.','high','drawing or diagram',True,True,None,'c15_lower_annotation.png',[1128,2293,1230,2319])
row('G10','Visible geometry of right-bracket candidate','complete closing-bracket glyph under unsure','no closing bracket','Qualified graphic with two visible returns only','The two drawn paths reproduce the visible upper and lower returns, including the upper-left spur. No unseen vertical connection is supplied. D13 carries the single H omission count for this physical bracket cluster.','medium','drawing or diagram',True,False,None,'c14_right_bracket.png',[1630,2215,1685,2334],group='right-bracket')
row('BR01','Upper brace of five-term partition','standard overbrace','descriptive upper-brace note','Explicit upper brace path BR01, same Sigma2^- label','The upper brace has a broad shallow left part, a raised central cusp and a short downturned right end at x1063, over the Sigma body and before its lowered 12. The conventional full-term brace spans farther. Its source-coordinate path preserves this endpoint, with unchanged label.','high','drawing or diagram',True,True,None,'c08_centre_sigma.png',[656,843,1069,885])
row('BR02','Lower brace of five-term partition','standard underbrace beginning with phantom central term','descriptive lower-brace note','Explicit lower brace path BR02, same Sigma1^- label','The visible left end starts around x1085 beneath the lowered 12 area, rather than the left edge of the central Sigma body included by the conventional underbrace. The brace dips, turns at its central cusp and ends beneath the final term. No algebraic regrouping is inferred from these physical endpoints.','high','drawing or diagram',True,True,None,'c08_centre_sigma.png',[1082,953,1470,990])

source_map=[
 {'row':'01','source_place':'first line, subscript','local_ids':['D01']},
 {'row':'02','source_place':'same line, old word','local_ids':['D02']},
 {'row':'03','source_place':'far right line 1','local_ids':['D03']},
 {'row':'04','source_place':'first insertion at right boundary','local_ids':['D04a','D04b']},
 {'row':'05','source_place':'after donc','local_ids':['D05']},
 {'row':'06','source_place':'after inclusion','local_ids':['D06']},
 {'row':'07','source_place':'first partition, brace display and lower argument','local_ids':['D07a','D07b','D07c','D07d']},
 {'row':'08','source_place':'before Dans','local_ids':['D08']},
 {'row':'09','source_place':'above alors','local_ids':['D09']},
 {'row':'10','source_place':'after égale and before last inclusion of opening','local_ids':['D10a','D10b']},
 {'row':'11','source_place':'above struck alors','local_ids':['D11']},
 {'row':'12','source_place':'under long final bar','local_ids':['D12a-old','D12a-live','D12b-old','D12b-live']},
 {'row':'13','source_place':'foot, right edge','local_ids':['D13']}
]
for s in source_map:
    s['statuses']={d['id']:d['C_doubt_status'] for d in D if d['id'] in s['local_ids']}

# Preserve the packet inventory identities, but use the final wording and allowed hand names.
inv=json.loads((root/'packets/016/C_inventory.json').read_text())
for i in inv:
    i.pop('cote',None);i.pop('scan',None);i['hand']='his hand';i['transcribed']='yes'
    i['provenance']='C_inventory.json '+i['element']+'; independently inspected for this reading'
changes={
 '016.05':r'de X/E_{\unsure{2}}; bowed guide G02',
 '016.07':r'\unsure{cqfd|qfd}',
 '016.10':r'qualified earlier E beneath first Sigma',
 '016.12':r'five-term partition; explicit brace paths BR01/BR02 and the same labels',
 '016.13':r'resolved earlier E beneath central Sigma12',
 '016.17':r'qualified O beneath D of Dans',
 '016.24':r'qualified E beneath Sigma12',
 '016.25':r'qualified Sigma beneath E1',
 '016.26':r'alors Sigma12 amalg E2 amalg Sigma2; one explicit curved strike G08',
 '016.27':r'\unsure{en|on} conclurait',
 '016.29':r'resolved square-join predecessor, final cup/amalg qualified at first join',
 '016.30':r'resolved square-join predecessor, final cup/amalg qualified at second join',
 '016.31':r'subset Sigma2+ cup E2 below explicit brace path G09'
}
for i in inv:
    if i['element'] in changes:i['first_words_or_objects']=changes[i['element']]
def add_inv(element,kind,position,first,hand='his hand'):
    inv.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
add_inv('016.C.G01','drawing','opening, below raised la comp. conn.','G01 bent insertion guide')
add_inv('016.C.G02','drawing','opening, below right-edge insertion','G02 bowed insertion guide')
add_inv('016.C.G03','drawing','opening right edge, beneath latter part of connexe','qualified detached short rule G03','undetermined hand')
add_inv('016.C.G04','drawing','above/right of central Sigma12 correction','qualified detached point G04','undetermined hand')
add_inv('016.C.G05','drawing','below/right of avec','qualified detached point G05','undetermined hand')
add_inv('016.C.G06','drawing','right blank margin adjacent to third closure row','qualified two-point cluster G06','undetermined hand')
add_inv('016.C.G07','drawing','above second nonempty-intersection formula','qualified detached point G07','undetermined hand')
add_inv('016.C.G08','drawing','through cancelled alors expression','curved rising strike G08; one path, one physical cancellation')
add_inv('016.C.G09','drawing','below first component closure in final equality','brace G09 with short return and taller right hook')
add_inv('016.C.G10','drawing','foot right, clipped by sheet edge','qualified closing-bracket returns G10; two paths; no invented upright')
add_inv('016.C.archive','text','lower-left corner','archive numeral 15, recorded only in the archive-number comment','undetermined hand')

# Inventory follows the supported page positions; attached graphical components stay local.
_order=['016.01', '016.02', '016.03', '016.C.G03', '016.04', '016.C.G01', '016.05', '016.C.G02', '016.06', '016.07', '016.08', '016.09', '016.10', '016.11', '016.C.G04', '016.12', '016.13', '016.14', '016.15', '016.C.G05', '016.16', '016.17', '016.18', '016.19', '016.20', '016.C.G06', '016.21', '016.C.G07', '016.22', '016.23', '016.24', '016.25', '016.27', '016.26', '016.C.G08', '016.28', '016.29', '016.30', '016.C.G10', '016.C.G09', '016.32', '016.31', '016.C.archive']
inv.sort(key=lambda i:_order.index(i['element']))

notation=[
 {'location':'opening, first union and remaining formulas','sign':'Sigma signs with plus and minus','latex':r'\Sigma_i^+,\Sigma_i^-','evidence':'Raised crossing strokes for plus; short horizontal bars for minus; subscript 1 uprights and hooked 2 forms individually inspected.'},
 {'location':'two partitions, central display, deleted lower expression','sign':'square join','latex':r'\amalg','evidence':'Two uprights on a horizontal foot extending beyond them; H sqcup is treated as its macro convention at the ordinary unamended occurrences, with no separate glyph-reading correction.'},
 {'location':'opening main line versus right raised insertion','sign':'two locally read separating strokes','latex':r'X\setminus E_2; X/E_{\unsure{2}}','evidence':'Main-line stroke descends right; right inserted stroke is nearly upright with an upper-right lean. No mathematical identification was used to choose them.'},
 {'location':'definition label','sign':'unaccented abbreviation','latex':r'\overset{\text{def}}{=}','evidence':'Small d/e/f above the two equality strokes, no independent accent above e.'},
 {'location':'three closure rows and final arguments','sign':'closure bars and inclusion relations','latex':r'\overline{\Sigma};\subsetneq;\subset','evidence':'Flat upper rules; outer rows have a crossed lower stroke beneath the inclusion curve; middle-row inclusions remain single curves.'},
 {'location':'nonempty statements and lower prose','sign':'empty-set sign','latex':r'\varnothing','evidence':'Small loop crossed by a long oblique slash.'},
 {'location':'opening third line','sign':'two-point punctuation','latex':':','evidence':'Two separate vertically stacked points after the egale/egal word.'},
 {'location':'opening and final prose','sign':'abbreviations','latex':r'comp. conn.; \unsure{cqfd|qfd}; p.\,ex.','evidence':'Points after comp and conn; no point following the cqfd/qfd cluster; separate points after p and ex.'}
]

report=dict(
 scan=16,reader='C',start_utc='2026-11-20 16:05:45 UTC',end_utc='2026-11-20 16:22:37 UTC',
 full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 image_delivery=dict(full={'file':'J81-02_81_scan016.jpg','count':1,'delivered':True,'size':[1685,2362]},
                     halves=[{'file':'J81-02_81_scan016_a.jpg','count':1,'delivered':True,'size':[1685,1261],'full_scan_origin':[0,0]},
                             {'file':'J81-02_81_scan016_b.jpg','count':1,'delivered':True,'size':[1685,1261],'full_scan_origin':[0,1101]}],
                     crop_files_viewed_once=19,failed_or_dropped_image_deliveries=0,
                     reading_order='UTC clock, mandatory brief, supplied witnesses/conventions/metadata, whole image, half a, half b, planned crops 01–17 one at a time, two additional new-locus crops 18–19 one at a time. No source image was reopened.'),
 differences=D,
 doubts=[],inventory=inv,
 notes=[
  {'topic':'page content','text':'The page continues an argument about two decompositions of X, records their five-term intersection partition and a definition of Sigma12, and writes three closure relations followed by two nonempty-intersection assertions. The final prose and bracketed equality are transcribed as the page writes them.'},
  {'topic':'author’s own uncertainty','text':'No explicit authorial question mark or verbal statement of doubt was observed. The unsure qualifications in reading.tex are this reader’s apparatus; they do not supply words to the manuscript.'},
  {'topic':'title/date/page counts','text':'No title, date or authorial page number is visible. The lower-left archive numeral is 15 and is retained only in a comment. The supplied metadata maps scan 16 to H page 15.'},
  {'topic':'mathematics-led reading decisions','text':'No topological theorem, algebraic computation, inferred correspondence or intended conclusion was used to repair or choose the transcription. check_events is empty. The signs, bars, terms, indices and two bracket returns were assessed from their ink.'},
  {'topic':'witness apparatus','text':'H’s explanatory brace notes describe the two central braces and the lower annotation; they are treated as apparatus, with their manuscript labels collated. They supply no additional prose to be transcribed. H uses sqcup for the ordinary square joins; that macro convention alone is not counted as a reading difference. The amended bottom joins are each collated locally.'},
  {'topic':'C source tables','text':'C_notes.txt contains one blank newline. Only the 13 actual Doubtful readings rows in C_doubts.txt are counted as source doubt rows; notation and abbreviation rows supply context only. The compound rows 04, 07, 10 and 12 are expanded into explicit local status entries.'},
  {'topic':'source boundaries','text':'The top-right insertion, the opening-right rule, the final bracket and the lower underbrace label reach original image boundaries. All crops include the complete available source extent; missing material beyond those original boundaries is not supplied. Crop 17 is a tight margin-only crop; its neighbouring text position was established in the one half-b view.'},
  {'topic':'graphical placement','text':'Every newly retained path is named in reading.tex and in the differences/inventory. Fixed local origins, base-west anchors, zero node padding and x/y units are declared. The source-coordinate rectangles describe the path placement; they do not assert exact font extents. No compilation or rendered layout validation was performed.'},
  {'topic':'central brace representation','text':'BR01 and BR02 redraw the visible central brace runs with their existing Sigma2-minus and Sigma1-minus labels. G04 is the separate point beside them. The brace path changes and the point are recorded separately; no physical stroke is drawn twice.'}
 ],notation=notation,check_events=[],crops=json.loads((out/'crop_manifest.json').read_text()),
 C_doubt_source_map=source_map,
 brief_feedback=[
  'The final bracket’s upright coincides with the dark image boundary. A standard full bracket glyph would supply an unseen run, so the return keeps a bracket candidate qualified and draws only the two visible returns.',
  'A tight crop of isolated margin points cannot contain a neighbouring text line without a large blank span. Crop 17 preserves the local marks; its relative line position comes from the already viewed half b.',
  'The brief specifies source-coordinate origins for nested uncertain graphics but no typographic scale. Each selected origin and scale is declared explicitly; no exact rendered text alignment is claimed.'
 ],
 validation={'method':'source-only structural and consistency checks; completed by validate.py','compiled':False,'rendered':False,'external_sources':False,'ocr_used':False,'delegated':False},
 paths={'reading':'reading.tex','report':'report.json','audit':'reading.md','crop_manifest':'crop_manifest.json','validation':'validation.json','scripts':['make_crops.py','add_remaining_crops.py','build_report.py','validate.py']}
)
for d in D:
    if d['C_doubt_status']=='retained' or d['id'] in ['N01a','N01b','G03','G04','G05','G06','G07','G10']:
        alts={
          'D01':['unrecovered predecessor shape; 2 remains primary'],
          'D02':['sont'], 'D04b':['unrecovered right-edge continuation'], 'D05':['unrecovered struck word'],
          'D06':['qfd'],'D07a':['unrecovered predecessor'],'D07c':['unrecovered predecessor'],'D07d':['unrecovered predecessor'],
          'D08':['unrecovered predecessor'],'D11':['on'],'D12a-live':[r'\amalg'],'D12b-live':[r'\amalg'],
          'D13':['return strokes with unestablished complete bracket'], 'N01a':['ê'], 'N01b':['absent separate final e'],
          'G03':['underline or guide role unestablished'], 'G04':['unestablished character, hand, role and surface origin'],
          'G05':['unestablished character, hand, role and surface origin'], 'G06':['unestablished character, hand, role and surface origin'],
          'G07':['unestablished character, hand, role and surface origin'], 'G10':['unseen upright not supplied']
        }.get(d['id'],[])
        report['doubts'].append({'id':d['id'],'location':d['location'],'reading':d['reading'],'alternatives':alts,'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'source_row':d.get('C_source_doubt_row')})
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

md=r'''# Scan 016 — independent reader C

Start recorded: **2026-11-20 16:05:45 UTC**, before the brief, packet and image reads. H page 15 is the supplied witness for this scan. No other page or reader was inspected.

## Image delivery and scope

The whole image was delivered and viewed once, then half a once, then half b once. Dimensions: whole 1685 × 2362; each half 1685 × 1261. Half a has source origin (0,0); half b has origin (0,1101). Nineteen tight crops were delivered and viewed once each. There were no dropped image outputs, retried views or recrops. All coordinates below and in the report are full-scan coordinates unless the half image is explicitly named.

The half images supplied the continuous visual reading. The crops address still-open local forms, small marks and edge limits. The right and bottom cut-offs noted below are limits of the original source, not a subsequent enlargement. Crop 17 contains the isolated margin marks without text; the half-b view established their position alongside the third closure row.

## Line-by-line audit

| Physical line or element | Reading audit |
| --- | --- |
| Opening line, “et par suite” through “connexe” | Words, Sigma signs, raised minus/plus and union read directly. The overwritten second index stays `deleted unsure 2` before live 1 (D01). The overwritten verb stays `deleted unsure sera/sont` followed by live est (D02); H’s serait changes the cluster. connexe is resolved (D03). A separate rule beneath its latter part is locally qualified and drawn as G03; its role is unassigned. |
| Opening second line, “de X donc de … contenant …” | Main-line `X\setminus E_2` read from the descending stroke. Raised “la comp. conn.” and its two abbreviation points are retained. Guide G01 is drawn. The second inserted phrase reads “de X/E” with slash resolved and the edge subscript 2 still qualified (D04a/b); guide G02 is drawn. The separate lower curved mark is retained once as the comma following this insertion. |
| Opening third line | The struck c’est candidate remains qualified (D05). The following word is `unsure é/ê` + `gal` + `unsure e/blank` (N01a/b). The next two stacked points are read as a colon (D10a). Sigma2-minus, comma, the final connective donc (resolved D10b), inclusion, and comma are read. No expected wording was supplied to replace the colon. |
| Opening final abbreviation | `cqfd/qfd` remains qualified (D06); full q/f descenders were inside crop 06. No terminal point is visible. |
| “L’intersection des deux partitions” | All words and the apostrophe read on half a; no inserted punctuation. |
| First partition | X, equality, Sigma1-plus, square join, E1, square join, Sigma1-minus read. Earlier E under the first Sigma remains qualified (D07a). |
| Second partition | X, equality, Sigma2-plus, square join, E2, square join, Sigma2-minus read. No predecessor is supplied here. |
| “de X est” | Retained as read; the two preceding equalities remain on successive display rows. |
| Five-term partition | X equals Sigma1-plus, square join, E1, square join, corrected Sigma12, square join, E2, square join, Sigma2-plus. The central earlier E is resolved from its own middle arm and upright (D07b). Upper Sigma2-minus and lower Sigma1-minus labels read. Explicit brace runs BR01/BR02 preserve the observed endpoints; the lower brace begins beneath the 12 region. A separate point G04 is qualified. |
| “avec” and definition | avec read. Isolated point G05 lies below/right and is preserved without assigning it a textual role. Definition reads Sigma12, unaccented def above equality, Sigma1-minus intersection Sigma2-minus. H’s accent and endpoint period have no corresponding visible marks (N02/N03). |
| “Dans cette partition … sont ouverts” | Initial overwritten O remains qualified (D08). Commas after partition and between the three Sigma terms read. No comma is visible after ouverts at the narrow right edge (N04). |
| “E1, E2 sont fermés, et on a” | Commas, accent on fermés, and final words read on half b. |
| First closure row | Sigma1-plus, proper-inclusion sign with crossed lower line, barred Sigma1-plus, inclusion, Sigma1-plus union E1. All bars, pluses and indices retained. |
| Middle closure row | Barred Sigma12 included in barred Sigma1-minus intersection barred Sigma2-minus, then included in the parenthesized unions, then included in Sigma12 union E1 union E2. Both parentheses and the two closure bars before the middle intersection read. |
| Third closure row | Sigma2-plus, proper-inclusion sign, barred Sigma2-plus, inclusion, Sigma2-plus union E2. Two compact detached spots in the far right margin are drawn under local qualification as G06; no mathematical role is assigned. |
| “Notons aussi que” | All words read; the descender of que is separate from the later point G07. |
| Two nonempty-intersection statements | Each Sigma12 is barred. First intersection E1 and second intersection E2; both unequal slashed-loop empty-set signs read. Comma separates the two statements. The small point above the second formula is drawn as G07. |
| “Car si on avait p. ex. …, on” | Abbreviation points, corrected barred Sigma12, intersection and corrected E1, equality, empty-set loop and comma read. Earlier E under Sigma and earlier Sigma under E remain separately qualified (D07c/d). |
| Raised insertion and cancellation | First inserted word remains en/on (D11); second word resolves as conclurait (D09), with its own tall l loop and terminal t. Cancelled “alors Sigma12 square-join E2 square-join Sigma2” remains deleted. G08 draws the single rising, then nearly horizontal strike, without a second generic visible cancellation. |
| Live continuation | Barred Sigma1-minus intersection E1 equals empty set, comma, retained. |
| Final bracketed equality | Opening bracket and car, barred Sigma1-minus, equality, long closure bar, Sigma2-plus, the two amended joins, E2 and Sigma12, equality, barred Sigma2-plus, union E2, union barred Sigma12, inclusion, Sigma1-minus union barred Sigma12. Both square-join predecessor glyphs resolve; each final cup/square-join form stays locally qualified (D12a/b). |
| Annotation beneath first component closure | Existing subset Sigma2-plus union E2 label read. G09 draws the underbrace with its short return and taller right hook. The lowest subscript extents meet the original bottom edge. |
| Final closing bracket area | Upper and lower returns are visible at the right boundary. Complete-bracket reading remains qualified (D13). G10 draws the two returns only, including the small upper spur; it does not add an unseen upright. |
| “ce qui n’est pas.” | Whole visible footer and final point read in crop 16. The lower descenders meet the original page edge; wording is still readable. |
| Lower-left archive numeral | 15 is retained only as `% archive sheet number: 15`; attribution remains undetermined hand. No authorial page number, title or date was added. |

## C source-doubt map

The thirteen actual source rows are counted once each. The notation and abbreviation tables are not counted as additional doubts.

'''
for s in source_map:
    bits=', '.join(f"{i}: {s['statuses'][i]}" for i in s['local_ids'])
    md+=f"- **Row {s['row']} — {s['source_place']}**: {bits}.\n"
md+=r'''

The added accent and final-e qualifications (N01a/b) are separate from those original thirteen rows. The original row 12 already describes both final joins as ambiguous even though C.tex marks only the first final cup; the second local qualification preserves that table doubt.

## Graphics and source origins

All literal paths occur in reading.tex. Each nested unsure graphic has an explicit local rectangle, baseline, base-west zero-padding anchor and declared units. Those declarations preserve the selected path origin; font extents have not been measured or rendered.

| Component | Full-scan origin or locus | Source representation |
| --- | --- | --- |
| G01 | Origin (1165,145) | One bent insertion guide; text occurs once in its node. |
| G02 | Origin (1522,176) | One bowed insertion guide; the ordinary following comma represents the separate lower curved mark once. |
| G03 | Word frame origin (1460,100), inner graphic anchored (1526,151) | One locally qualified detached rule. |
| BR01/BR02 | Common display origin (500,800) | One upper-brace path and one lower-brace path, with original labels. |
| G04 | Inner anchor (1137,839) | One qualified filled spot near (1139,842). |
| G05 | Frame origin (257,1034), inner anchor (428,1126) | One qualified point below/right of avec. |
| G06 | Origin (1618,1726) | Two separate filled point contours, qualified together; hand/role/origin unresolved. |
| G07 | Display origin (320,1890), inner anchor (926,1892) | One qualified wedge-like point above the second formula. |
| G08 | Origin (286,2104) | One curved strike over an invisible dimensional deleted copy; no generic duplicate strike. |
| G09 | Origin (1090,2228) | One connected brace path including both right-end turns and its existing label. |
| G10 | Origin (1630,2215) | Two return paths only; bracket candidate locally qualified. |

## Verification limits

No OCR, external source, other page, other reader, delegation, installation, compilation or rendering was used. No mathematical computation or theorem check was performed; `check_events` is empty. The page’s mathematical assertions remain attributed to the page.

Source-only checks inspect brace/environment balance, allowed macro names, source-doubt coverage, crop references and agreement between the final TeX, report and this audit. The generated validate.py and validation.json record those checks. The crop manifest records all nineteen boxes and purposes, including original-edge limits.
'''
(out/'reading.md').write_text(md)
print(json.dumps({'differences':len(D),'source_doubt_rows':len(source_map),'source_doubt_local_entries':sum(len(s['local_ids']) for s in source_map),'doubts':len(report['doubts']),'inventory':len(inv),'crops':len(report['crops'])}))
