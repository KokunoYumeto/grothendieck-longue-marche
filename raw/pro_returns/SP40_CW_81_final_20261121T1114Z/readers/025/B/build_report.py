from pathlib import Path
import json,datetime,re,hashlib
D=Path('out/readers/025/B');tex=(D/'reading.tex').read_text();sm=json.loads((D/'source_map.json').read_text());gs={g['id']:g for g in sm['groups']};crops=json.loads((D/'crop_manifest.json').read_text())
C=(Path('packets/025/C.tex')).read_text();H=(Path('packets/025/H.tex')).read_text();dt=(Path('packets/025/C_doubts.txt')).read_text()
rows=[];inside=False
for line in dt.splitlines():
 if line=='## Doubtful readings':inside=True;continue
 if inside and line.startswith('## '):break
 if inside and line.startswith('| 25 |'):rows.append(line)
assert len(rows)==8
for g in sm['groups']:
 if g['id']=='B025-S01':g['local_hand_scopes']=[{'components':'Sigma body, predecessor candidate, minus, index','hand':'his hand'},{'components':'detached upper run','hand':'his hand in head/retrace candidate; undetermined hand in independent-run candidate'}]
 elif g['id'] in ['B025-S04','B025-S05','B025-S06','B025-S07']:g['local_hand_scopes']=[{'components':'Sigma body, raised sign and index','hand':'his hand'},{'components':'detached upper run','hand':'his hand in head/retrace candidate; undetermined hand in independent-run candidate'}]
 elif g['id']=='B025-S02':g['local_hand_scopes']=[{'components':'hatted Sigma, alpha and plus','hand':'his hand'},{'components':'two small intervening traces','hand':'undetermined hand'}]
 elif g['id']=='B025-G09':g['local_hand_scopes']=[{'components':'que and its descender','hand':'his hand'},{'components':'point right of q','hand':'undetermined hand'}]
 else:g['local_hand_scopes']=[{'components':g['ownership'],'hand':g['hand']}]
 if g['id'] in ['B025-M01','B025-M02']:
  g['parent_placement']={'parent_units':'x=0.01em, y=-0.01em','parent_original_origin':[0,1100],'node_anchor':'base west','inner_sep':'0pt','outer_sep':'0pt','parent_baseline_xy':[g['bbox'][0],g['base_y']-1100],'inner_baseline_xy':[0,g['base_y']-g['bbox'][1]],'inner_units':'x=0.01em, y=-0.01em'}
 if g['id'] in ['B025-S01','B025-S06','B025-S07']:
  g['complete_qualified_candidates']=[{'complete_symbol_state':a,'upper_run_role':role,'hand_scope':'main glyph his hand; independent upper-run candidate retains undetermined hand'} for a in g['alternatives'] for role in ['head/retrace','independent upper run']]
sm['text_spans']=[]
def textspan(id,needle,loc):
 a=tex.index(needle);b=a+len(needle);sm['text_spans'].append({'id':id,'location':loc,'literal_source':needle,'char_offsets':[a,b],'byte_offsets_utf8':[len(tex[:a].encode()),len(tex[:b].encode())]})
textspan('B025-T01',r'\deleted{Soit en effet} Si on a','opening crossed and live wording')
textspan('B025-T02',r'\deleted{et si} alors','opening cancelled connective and live alors')
textspan('B025-T03',r'\text{mut\textsuperscript{t}. disjoints}','abbreviation and following adjective; no final period')
textspan('B025-T04',r'\unsure{determinés|déterminés|determines}','word after sont, complete alternatives')
textspan('B025-T05',r'$ i.e. $','dotted connective between signed Sigmas')
textspan('B025-T06','% archive sheet number: 24','archive numeral recorded as comment')
(D/'source_map.json').write_text(json.dumps(sm,ensure_ascii=False,indent=2)+'\n')
report={'scan':25,'reader':'B','start_utc':'2026-11-21T05:40:21Z','end_utc':None,'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,'differences':[],'doubts':[],'inventory':[],'notes':{},'notation':[],'check_events':[],'crops':crops,'brief_feedback':[]}
def diff(id,loc,c,h,reading,evidence,confidence='medium',kind='other',dc=False,dh=False,cs=None,crop=None,bbox=None,parent=None,source=None,scope=None,markedH=False):
 d={'id':id,'location':loc,'C':c,'H':h,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':cs,'readers_crop':crop,'bbox':bbox,'physical_parent':parent or id,'source_group':source,'scope':scope,'marked_in_H':markedH}
 if source:
  g=gs[source];d['reader_source_quote']=g['proposal'];d['reader_source_qualification']=g['qualification'];d['reader_source_offsets']=g['byte_offsets_utf8'];d['reader_source_map']='source_map.json';d['reader_literal_source_id']=source
 report['differences'].append(d);return d
R=[]
R.append(diff('B025-R01','opening Sigma, predecessor',r'\deleted{\unsure{E|I}}\Sigma_i^-',r'\Sigma_{i}^{-}',gs['B025-S01']['proposal'],'A thin upright survives inside the angular live glyph, with overlapping horizontal ends. E and I remain possible. The full proposed group also preserves its separate upper run and one short undotted index; those added local qualifications are recorded separately.','low','omission',False,True,'retained','01_opening_sigma.png',[830,119,924,194],'P01','B025-S01','Original C row 1 covers the predecessor only.'))
R.append(diff('B025-R02','relation after opening barred U',r'\deleted{\unsure{=}}\cap',r'\cap',gs['B025-G02']['proposal'],'Two horizontal traces run under the arch, the lower one interrupted at its left. Equals remains the predecessor candidate; their allocation to predecessor versus retrace is not decided.','low','omission',False,True,'retained','02_opening_cap_E.png',[1100,151,1147,185],'P02','B025-G02','Original C row 2 covers the old relation; the E index has its own row.'))
R.append(diff('B025-R03','opening E index',r'E_{\unsure{i|j}}',r'E_i',gs['B025-G02']['proposal'],'A separate upper point and a short lower hooked stroke remain visible. The lower return does not settle i versus j.','medium','other',False,False,'retained','02_opening_cap_E.png',[1203,152,1222,189],'P03','B025-G02','Original C row 3 only.'))
R.append(diff('B025-R04','large union after X setminus',r'\mathop{\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\deleted{\bigcap}\bigcup}}\limits_{\alpha\in K}',r'\bigcup_{\alpha\in K}',gs['B025-G04']['proposal'],'The high transverse run, upper-left curved return and doubled round bowl are all present. Their complete states remain a union with high cross or union over an earlier intersection. H explicitly describes a disjoint-union sign in its note; that description is included in this collation.','medium','other',False,False,'retained','05_union_hat.png',[838,269,931,395],'P04','B025-G04','Original C row 4 is one operator/state locus.'))
R.append(diff('B025-R05','far right after pi-zero expression',r'\deleted{\unsure{\text{les}|K}}',r'\struck{tel},',gs['B025-G05']['proposal'],'A tall initial upright, upper loop, lower returning stroke and transverse cancellation remain. Les is primary; K and H’s tel remain possible complete readings. No separate terminal comma is visible before the paper edge.','low','misread word',False,True,'retained','06_condition_edge.png',[1597,342,1673,399],'P05','B025-G05','Original C row 5; H tel remains an alternative, so this is a qualified difference.'))
R.append(diff('B025-R06','cluster immediately left of fresh les',r'\deleted{\unsure{U\Sigma|\bigcup\Sigma|U}}','et les',gs['B025-G06']['proposal'],'A large bowl encloses an angular two-diagonal shape at its right, with a lower hooked return. The original complete U-Sigma/union-Sigma/U alternatives remain. A separate local live/cancelled-state qualification is retained; the following les is firm and stays outside the cluster.','low','misread symbol or index',False,True,'retained','07_lower_condition.png',[1103,439,1163,513],'P06','B025-G06','Original C row 6 covers the whole cluster.'))
R.append(diff('B025-R07','before disjoints',r'\unsure{mut\textsuperscript{t}.|mut.}',r'mut\supplied{uellemen}t disjoints.',r'mut\textsuperscript{t}.','A separate raised t-shaped stem with short right arm stands above a distinct point after the contracted baseline mut. The raised t and abbreviation stop are visible. H’s supplied letters are editorial expansion; they are not alleged extra manuscript ink.','high','abbreviation expanded or spelling modernised',True,True,'resolved','07_lower_condition.png',[1380,423,1501,479],'P07',None,'Original C row 7. Resolved reading is exactly mut with raised t and stop.'))
R.append(diff('B025-R08','after sont',r'\unsure{determinés|déterminés|determines}','déterminés',r'\unsure{determinés|déterminés|determines}','No separate acute is clear over the first e. Near the ending, a short slant lies below the complete descender of que from the preceding line and near the final-letter head. The full word alternatives remain together, with determinés first.','low','misread word',False,True,'retained','09_determines.png',[480,682,780,762],'P08',None,'Original C row 8 jointly covers both accent positions; H déterminés survives as an alternative.'))
for i,d in enumerate(R,1):d['C_source_row_id']=f'C025-R{i:02d}';d['C_source_row_literal']=rows[i-1]
report['original_C_doubts']=[{'id':f'C025-R{i+1:02d}','literal_source_row':row,'mapped_difference':R[i]['id'],'status':R[i]['C_doubt_status'],'scope':R[i]['scope']} for i,row in enumerate(rows)]
diff('B025-D09','opening cancelled connective',r'\deleted{et si}',r'\struck{ainsi}',r'\deleted{et si}','The first group has a looped e and tall crossed t; the second has an s-like curve and separate i-point under the descending crossing. The following alors is live.','high','misread word',False,True,crop='03_cancelled_etsi.png',bbox=[1404,143,1541,197],parent='P09')
diff('B025-D10','reduced continuation after alors','on a','on a',gs['B025-G03']['proposal'],'The continuation is reduced to a small filled first mark, a longer low arch and a short final arch. On a is the supported primary, with unassigned marks retained; all three shapes are drawn once.','low','other',True,False,crop='04_reduced_ona.png',bbox=[296,283,439,304],parent='P10',source='B025-G03',scope='New whole-phrase qualification, not a supplied expansion.')
diff('B025-D11','first Sigma index',r'\Sigma_i^-',r'\Sigma_i^-',gs['B025-S01']['proposal'],'Only one short oblique low stroke is visible at the index; it has no isolated upper point. The proposed complete glyph retains i and prime candidates. This does not alter the independently retained E/I predecessor doubt.','medium','other',True,False,crop='01_opening_sigma.png',bbox=[897,153,911,172],parent='P01',source='B025-S01',scope='New index qualification; subsequent two signed prose indices keep their own local recurrence records.')
diff('B025-D12','cancelled-cluster state before les',r'\deleted{\unsure{U\Sigma|\bigcup\Sigma|U}}','et',gs['B025-G06']['proposal'],'The angular form and bowl overlap; an independent cancellation stroke cannot be assigned securely. The complete live U-Sigma state is retained alongside the three original deleted-state candidates.','low','deletion state (struck given live or live given struck)',True,False,crop='07_lower_condition.png',bbox=[1103,439,1163,513],parent='P06',source='B025-G06',scope='New state uncertainty; H physical difference is counted under R06.')
diff('B025-D13','end of lower condition','disjoints','disjoints.','disjoints','The adjective reaches the physical right edge. No independent terminal full stop is visible after its final strokes.','medium','text not on the page',False,True,crop='07_lower_condition.png',bbox=[1515,424,1680,505],parent='P13')
diff('B025-D14','end of final set',r'\Sigma_\alpha^-',r'\Sigma_{\alpha}^{-}\}',gs['B025-S08']['proposal'],'The last signed alpha-indexed Sigma is followed by blank paper. No closing curly brace is drawn; the last alpha itself remains the written index.','high','text not on the page',False,True,crop='12_final_set.png',bbox=[1166,899,1340,1038],parent='P14',source='B025-S08',scope='C slips table context, not a ninth original doubt.')
for id,gid,loc,ev,parent in [
('B025-GD01','B025-S01','first overwritten Sigma geometry','The detached heavy top run, thin upper diagonal, heavy main diagonal/foot and inner predecessor upright remain distinct components.','P01'),
('B025-GD02','B025-G02','overwritten relation and opening E geometry','The two old horizontal traces, broad arch, detached curved E top arm, E upright/middle/foot and both index components are retained once.','P02'),
('B025-GD04','B025-G04','large union geometry','The upper-left curved return, high transverse run, two bowl runs and short right retrace are drawn literally; an ordinary cup plus one dash omits these local runs.','P04'),
('B025-GD05','B025-G05','right-edge cancelled cluster geometry','The looped upper strokes, tall upright, lower return and transverse stroke are reproduced together without a generic second strike.','P05'),
('B025-GD06','B025-G06','cluster before les geometry','Both bowl and inner angular form, including the descending terminal hook, occur once under the complete local state qualification.','P06'),
('B025-GD07','B025-G07','K replacement and bent guide','The raised K-setminus-braced-i is above the crossed K. A long curved stroke enters from lower left, crosses the K region and finishes with a hooked upper-right end; all parts are preserved.','P15'),
('B025-GD08','B025-S04','disjointness Sigma upper run','A short upper horizontal is separated from the angular body by white space; alpha and plus remain in the same group.','P16'),
('B025-GD09','B025-S05','prose Sigma upper run','The upper horizontal is detached above the separate upper diagonal; alpha and plus remain in the group.','P17'),
('B025-GD10','B025-S06','signed plus Sigma in prose','The long upper slant is detached, the lower foot has a downturned end, and the index is one short stroke without a separate dot; the local i/prime and head-role alternatives remain.','P18'),
('B025-GD11','B025-S07','signed minus Sigma in prose','The upper slant is detached, the body has a curled lower ending, and the index is one short stroke without a separate dot; the sentence point remains outside.','P19')]:
 g=gs[gid]
 diff(id,loc,'Ordinary symbol/state macro at the same locus','Ordinary symbol/state macro or cited apparatus at the same locus',g['proposal'],ev,'medium','drawing or diagram',True,True,crop=g['crop'],bbox=g['bbox'],parent=parent,source=gid,scope='Literal geometry addition; shared physical parents prevent duplicate correction counts.')
diff('B025-D20','between hatted Sigma plus and alpha',r'\widehat{\Sigma}_\alpha^+',r'\widehat{\Sigma}_{\alpha}^{+}',gs['B025-S02']['proposal'],'One pale short stroke and one dark small wedge lie in the gap between the plus and alpha. Both are drawn locally; attachment, role, hand and surface origin remain unresolved.','medium','omission',True,True,crop='05_union_hat.png',bbox=[1039,306,1053,321],parent='P20',source='B025-S02',scope='Local mark qualification does not qualify the firm roof, plus or alpha.')
diff('B025-D21','beside final que descender','que','que',gs['B025-G09']['proposal'],'A separate small triangular dark point lies to the right of q’s long descender, well below the live word baseline. Its presence is clear; role, hand, attachment and surface origin remain open.','medium','omission',True,True,crop='15_que_adjacent_point.png',bbox=[1090,836,1101,848],parent='P21',source='B025-G09',scope='Complete word-bearing group owns que and the point; Je dis is outside.')
for id,gid,loc,ev,parent in [('B025-D22','B025-M01','faint lower-left-middle trace','A pale curved run bends down and left into a foot, with a pale middle continuation and separated short left foot. No character is supplied.','P22'),('B025-D23','B025-M02','isolated lower-right points','Two dark filled spots stand diagonally apart on otherwise blank paper. No colon or other character is supplied.','P23')]:
 g=gs[gid];diff(id,loc,'Absent','Absent','Qualified literal graphical group '+gid,ev,'medium','omission',True,True,crop=g['crop'],bbox=g['bbox'],parent=parent,source=gid,scope='Shape retained; role, hand and surface origin undetermined.')
# Full source proposals and their qualifications are carried without mixing witness wording.
for g in sm['groups']:
 if g['qualification'] or g['alternatives']:
  report['doubts'].append({'location':g['id']+': '+g['ownership'],'reading':g['proposal'] or 'literal graphical group '+g['id'],'alternatives':g['alternatives'],'confidence':'low' if g['id'] in ['B025-S01','B025-G02','B025-G03','B025-G05','B025-G06'] else 'medium','reason':g['qualification'] or 'The recurring local alternatives remain recorded while the first occurrence carries the printed qualifier.','crop':g['crop'],'source_group':g['id'],'literal_source_offsets':g['byte_offsets_utf8'],'local_hand_scopes':g['local_hand_scopes']})
report['doubts'].append({'location':'after sont','reading':r'\unsure{determinés|déterminés|determines}','alternatives':['determinés','déterminés','determines'],'confidence':'low','reason':'Complete first/final accent alternatives retained together under original C025-R08.','crop':'09_determines.png','source_span':'B025-T04'})
# Inventory is ordered by page position, with whole regions and local components interleaved.
def inv(element,kind,pos,first,y,hand='his hand',source=None,extra=None):
 o={'sheet_kind':'text','hand':hand,'element':element,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes','source_group':source,'order_y':y}
 if extra:o.update(extra)
 report['inventory'].append(o)
inv('B025-I01','deletion','top line','Soit en effet',80)
inv('B025-I02','text','opening live line and reduced continuation','Si on a U_s ... alors on a',140)
for gid in ['B025-S01','B025-G02']:inv(gid,'text','opening formula',gs[gid]['proposal'],gs[gid]['bbox'][1],source=gid,extra={'local_hand_scopes':gs[gid]['local_hand_scopes']})
inv('B025-I03','deletion','inside first Sigma','E/I predecessor',145,source='B025-S01')
inv('B025-I04','deletion','beneath first cap','equals predecessor candidate',165,source='B025-G02')
inv('B025-I05','deletion','opening right','et si',166)
inv('B025-G03','text','left continuation above display',gs['B025-G03']['proposal'],283,source='B025-G03')
inv('B025-I06','display','first display and its right conditions','U_s=X setminus union; i in K subset I; component and disjointness conditions',285)
for gid in ['B025-G04','B025-S02','B025-S03','B025-G05','B025-G06','B025-S04']:
 kind='deletion' if gid in ['B025-G05','B025-G06'] else 'display'
 inv(gid,kind,'first display local group',gs[gid]['proposal'],gs[gid]['bbox'][1],source=gid,extra={'local_hand_scopes':gs[gid]['local_hand_scopes']})
inv('B025-I07','drawing','between hatted plus and alpha','two small traces',309,'undetermined hand','B025-S02')
inv('B025-I08','text','last condition','les Sigma-alpha-plus mut with raised t and stop disjoints',450)
inv('B025-I09','insertion','above crossed K','K setminus braced i',488,source='B025-G07')
inv('B025-I10','text','paragraph beginning Il faut voir','Il faut voir que ... Je dis que',573)
inv('B025-I11','deletion','after first que','K',560,source='B025-G07')
inv('B025-G07','drawing','K correction','complete raised replacement, cancelled K and long bent guide',481,source='B025-G07')
for gid in ['B025-S05','B025-S06','B025-S07','B025-G09']:
 inv(gid,'text','lower prose local group',gs[gid]['proposal'],gs[gid]['bbox'][1],source=gid,extra={'local_hand_scopes':gs[gid]['local_hand_scopes']})
inv('B025-I12','drawing','right of final q descender','small triangular point',841,'undetermined hand','B025-G09')
inv('B025-I13','display','last inked formula','K setminus braced i = left brace alpha in I | E_alpha subset Sigma_alpha^-',925)
for gid in ['B025-G08','B025-S08']:inv(gid,'display','last equation local group',gs[gid]['proposal'],gs[gid]['bbox'][1],source=gid)
for gid in ['B025-M01','B025-M02']:inv(gid,'drawing','lower-sheet isolated trace',gs[gid]['ownership'],gs[gid]['bbox'][1],'undetermined hand',gid)
inv('B025-I14','text','lower-left archive number','24; archive comment only',2310,'undetermined hand',extra={'archive_only':True})
report['inventory'].sort(key=lambda x:x['order_y'])
report['notes']={'page_content':'The sheet writes the opening U_s inclusion and barred-U nonemptiness expression, a U_s equality with an indexed large union and hatted positive Sigma, then a component condition and disjointness wording. It says “Il faut voir que” K setminus braced i and the Sigma-alpha-plus family are determined in terms of i and Sigma-i-plus, followed by “i.e.” Sigma-i-minus. The final written equality ends with E_alpha subset Sigma_alpha-minus and has no closing set brace. These are attributed manuscript expressions, not proof checks.','author_uncertainty_exact_words':['Il faut voir que'],'title_date_page_counts':'No title or date. Archive sheet number 24 at lower left; no manuscript page-number macro supplied.','mathematics_led_reading_decisions':'None. The final alpha, all signed forms and the unclosed brace are retained from their ink. No mathematical repair, inference, identity check or conditional theorem was performed.','C_notes':'C_notes.txt is empty.','H_scope':'H page24 corresponds to scan25 and has full text. H note apparatus is read with its body: repassé Sigma, malformed exponent, and disjoint-union description inform the witness collation; the note itself is not manuscript prose. H supplied expansion letters are editorial.','notation_context':'The six notation-table rows and two Slips kept as written rows are contextual entries, preserved separately from the eight actual Doubtful readings rows.'}
report['notation']=[{'location':'opening and lower signed prose Sigmas','sign':'short one-part undotted index','latex':r'\unsure{i|\prime} first occurrence; i primary thereafter','local_occurrences':['B025-S01','B025-S06','B025-S07'],'note':'Each literal short stroke is drawn once; each local i/prime alternative remains in source_map.'},{'location':'first Sigma and S04-S07','sign':'detached upper run','latex':'literal complete Sigma groups','local_occurrences':['B025-S01','B025-S04','B025-S05','B025-S06','B025-S07'],'note':'Head/retrace or independent-run role unresolved. S02, S03 and S08 have locally observed joins.'},{'location':'right condition','sign':'low ring after pi','latex':r'\pi_0','note':'Two-legged pi with a low oval, as seen in crop06; no new doubt.'},{'location':'lower condition','sign':'contracted mut, raised t, stop','latex':r'mut\textsuperscript{t}.','note':'Original C025-R07 resolves; no expansion inserted.'},{'location':'between signed prose terms','sign':'dotted connective','latex':'i.e.','note':'Both separator and terminal point visible in crop11.'},{'location':'raised correction and final equality','sign':'setminus slash and braced dotted i','latex':r'K\setminus\{i\}','note':'All three occurrences read locally, with the raised occurrence literal in G07.'},{'location':'last equation','sign':'unclosed outer set','latex':r'\bigl\{\alpha\in I\mid E_\alpha\subset\Sigma_\alpha^-','note':'The open endpoint is a slips-table entry, not an extra C doubt.'}]
report['source_geometry']={'file':'source_map.json','groups':len(sm['groups']),'selected_bodies':'Literal source excerpts and UTF-8 offsets are supplied for every selected group; each adjoining word boundary is explicit.','metric_validation':'No rendering, compilation, curve-extrema calculation, pixel differencing, OCR or automatic recognition. All paths are manual visual approximations. Source coordinate translations are administrative declarations.'}
report['provenance']={'inputs':['out/briefs/brief_v23_scan025.md','packets/025/C.tex','packets/025/H.tex','packets/025/C_doubts.txt','packets/025/C_notes.txt','packets/025/C_inventory.json','packets/025/metadata.json','packets/025/notation.md','source/SP40_CW_81_witnesses/codex/J81-03/PREAMBLE.tex','source/SP40_CW_81_witnesses/codex/J81-03/PROMPT.md','source/SP40_CW_81_scans/J81-03_81_scan025.jpg','source/SP40_CW_81_scans/J81-03_81_scan025_a.jpg','source/SP40_CW_81_scans/J81-03_81_scan025_b.jpg'],'independence':'No other pages, readers, root records or external sources inspected; no delegation.','start_order':'UTC recorded after brief read and before packet/image reading.','image_dimensions':{'whole':[1685,2361],'a':[1685,1260],'b':[1685,1261]},'half_origins':{'a':[0,0],'b':[0,1100]},'view_audit':'view_audit.json','view_count':18,'failed_unseen_deliveries':[],'crop_sequence_note':'Fourteen initial unresolved-target crops, each once. A fifteenth first crop subsequently addressed the small point beside the final que descender recalled from the full half reading; no target was re-viewed or re-cropped. The word que was context for its point, not reopened for lexical reconsideration.','text_output_note':'The first combined packet read was text-output truncated; missing portions of the notation snapshot and source prompt were subsequently read in bounded chunks. No image was dropped or retried.','counting':'Original C table rows: exactly8. Their source identities survive all local geometry/state additions. Differences carry physical_parent identifiers for deduplication; repeated rows within a parent do not create extra physical correction counts. All literal component additions remain individually traceable.','explicitly_not_done':['OCR','internet','research','compilation','rendering','installation','mathematical repair','proof inference']}
report['brief_feedback']=['The brief filename is v23 but its last printed revision heading is v22 after scan023; I followed the complete supplied contents.','The conventions allow literal graphical preservation without assigning a character, but provide no separate macro for surface-origin uncertainty; I used local unsure wrappers and exact role/hand scope in source_map/report.','Manual graphical groups are source-only approximations and are not claimed as metric or rendered validation.']
report['C_context_tables']={'notation_table':dt.split('## Doubtful readings')[0].strip(),'slips_kept_as_written':dt.split('## Slips kept as written')[1].strip() if '## Slips kept as written' in dt else ''}
literal_witnesses={
'B025-S01':(r'\deleted{\unsure{E|I}}\Sigma_i^-',r'\Sigma_{i}^{-}'),
'B025-G02':(r'\deleted{\unsure{=}}\cap E_{\unsure{i|j}}',r'\cap E_{i}'),
'B025-G04':(r'\mathop{\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\deleted{\bigcap}\bigcup}}\limits_{\alpha\in K}',r'\bigcup_{\alpha\in K}'),
'B025-G05':(r'\deleted{\unsure{\text{les}|K}}',r'\struck{tel},'),
'B025-G06':(r'\deleted{\unsure{U\Sigma|\bigcup\Sigma|U}}','et'),
'B025-G07':(r'\deleted{K}\inserted{K\setminus\{i\}}',r'\struck{$K$} $K\smallsetminus\{i\}$'),
'B025-S04':(r'\Sigma_\alpha^+',r'\Sigma_{\alpha}^{+}'),
'B025-S05':(r'\Sigma_\alpha^+',r'\Sigma_{\alpha}^{+}'),
'B025-S06':(r'\Sigma_i^+',r'\Sigma_{i}^{+}'),
'B025-S07':(r'\Sigma_i^-',r'\Sigma_{i}^{-}')}
for d in report['differences']:
 gid=d.get('source_group')
 if gid:
  d['reader_semantic_annotation']=gs[gid]['proposal']
  d['reader_source_quote']=gs[gid]['literal_source']
  d['reader_complete_alternatives']=gs[gid].get('complete_qualified_candidates',gs[gid]['alternatives'])
 if d['id'].startswith('B025-GD'):
  d['C'],d['H']=literal_witnesses[gid]
 if gid=='B025-G04':d['H_apparatus_quote']='la réunion est écrite avec le signe de réunion\ndisjointe'
# Honest source-only structural audit.
lines=[]
for line in tex.splitlines():
 out='';i=0
 while i<len(line):
  if line[i]=='%' and (i==0 or line[i-1]!='\\'):break
  out+=line[i];i+=1
 lines.append(out)
s='\n'.join(lines);stack=[];brace_error=None
for i,ch in enumerate(s):
 if ch in '{}':
  bs=0;j=i-1
  while j>=0 and s[j]=='\\':bs+=1;j-=1
  if bs%2:continue
  if ch=='{':stack.append(i)
  elif not stack:brace_error=('closing',i);break
  else:stack.pop()
envstack=[];enverror=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
 typ,n=m.groups()
 if typ=='begin':envstack.append(n)
 elif not envstack or envstack[-1]!=n:enverror.append([n,m.start()])
 else:envstack.pop()
inside_math=False;blank_in_math=[]
for n,line in enumerate(tex.splitlines(),1):
 if r'\[' in line:inside_math=True
 if inside_math and not line.strip():blank_in_math.append(n)
 if r'\]' in line:inside_math=False
checks={'brace_balance':not stack and brace_error is None,'unclosed_braces':len(stack),'brace_error':brace_error,'environment_balance':not envstack and not enverror,'environment_errors':enverror,'display_open_count':s.count(r'\['),'display_close_count':s.count(r'\]'),'dollar_count':len(re.findall(r'(?<!\\)\$',s)),'blank_physical_lines_inside_displays':blank_in_math,'crop_files_exist':all((D/c['path']).exists() for c in crops),'all_crops_viewed_once':all(c['viewed'] for c in crops),'original_C_doubt_rows':len(rows),'original_C_resolved':sum(d['C_doubt_status']=='resolved' for d in R),'original_C_retained':sum(d['C_doubt_status']=='retained' for d in R),'source_offset_match':all(tex[g['char_offsets'][0]:g['char_offsets'][1]]==g['literal_source'] for g in sm['groups']),'reading_sha256':hashlib.sha256(tex.encode()).hexdigest(),'rendering_performed':False,'mathematical_checks_performed':False}
report['final_source_audit']=checks
report['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,indent=2))
