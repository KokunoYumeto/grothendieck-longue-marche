from pathlib import Path
import json,re
p=Path('out/readers/021/C'); tex=(p/'reading.tex').read_text(); report=json.loads((p/'report.json').read_text()); man=json.loads((p/'crop_manifest.json').read_text()); gs=json.loads((p/'graphical_groups.json').read_text())
report['differences'][0]['C']="\\unsure{l'on a|on a}"
# Source-only structure review; no TeX engine is invoked.
body='\n'.join(x.split('%',1)[0] for x in tex.splitlines())
stack=[]; errors=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',body):
 typ,name=m.groups()
 if typ=='begin':stack.append(name)
 elif not stack or stack[-1]!=name: errors.append({'environment_mismatch':name,'offset':m.start()})
 else:stack.pop()
level=0
for i,ch in enumerate(body):
 if ch not in '{}':continue
 slashes=0;j=i-1
 while j>=0 and body[j]=='\\':slashes+=1;j-=1
 if slashes%2:continue
 level += 1 if ch=='{' else -1
 if level<0:errors.append({'negative_brace_level':i})
if stack:errors.append({'unclosed_environments':stack})
if level:errors.append({'final_brace_level':level})
if body.count('$')%2:errors.append({'odd_math_dollar_count':body.count('$')})
for c in man['crops']:
 if not (p/c['path']).exists():errors.append({'missing_crop':c['path']})
actual_ids=[x['source_row_id'] for x in report['actual_C_outcome_map']]
if actual_ids != [f'C021-R{i:02d}' for i in range(1,16)]:errors.append({'source_identity_error':actual_ids})
if any(x['transcribed']!='yes' for x in report['inventory']): errors.append({'inventory_untranscribed':True})
struct={'kind':'source-only structural review','checks':['balanced unescaped braces','nested begin/end environments','even inline math delimiter count','all crop paths exist','15 canonical source-row identities in original order','inventory material selected in complete TeX'],'result':'passed' if not errors else 'issues','issues':errors,'not_claimed':['compilation','render validation','metric validation','mathematical proof check']}
report['structural_review']=struct
report['counts']={'actual_C_rows':15,'actual_C_local_parts':15,'resolved_C_rows':7,'retained_C_rows':8,'crops_generated':22,'crops_successfully_viewed':22,'failed_unseen_image_deliveries':0,'image_retries':0,'difference_audit_rows':len(report['differences']),'diff_C_parent_flags':sum(x['diff_C'] for x in report['differences']),'diff_H_parent_flags':sum(x['diff_H'] for x in report['differences']),'count_scope':'Administrative counts of the selected records only; child graphical rows retain explicit parent-count references.'}
report['provenance']['boundary_limits']=['crop01 clips the neighbouring que descender; complete que attachment is included in the separately planned i.e target crop02. The opening l’on/on target is complete.','crop10 clips surrounding formula/next-line context; the cancelled word and live signifie target are complete. Their neighbours have their own complete formula crops11 and22.','crop13 reaches the original physical lower paper edge. The lower brace and some low descenders survive only to that edge; no further brace arm is supplied.','Other crops can cut unrelated contextual ink at their outer edges; no deciding target endpoint was knowingly clipped.']
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
views=[{'order':1,'path':'source/SP40_CW_81_scans/J81-03_81_scan021.jpg','kind':'whole layout','status':'success','view_count':1},{'order':2,'path':'source/SP40_CW_81_scans/J81-03_81_scan021_a.jpg','kind':'upper half line-by-line','status':'success','view_count':1},{'order':3,'path':'source/SP40_CW_81_scans/J81-03_81_scan021_b.jpg','kind':'lower half line-by-line','status':'success','view_count':1}]
for n,c in enumerate(man['crops'],4):views.append({'order':n,'path':c['path'],'kind':'one tight local target','bbox':c['bbox'],'status':'success','view_count':1,'rotation':0})
imageaudit={'scan':'021','reader':'C','views':views,'whole_views':1,'half_a_views':1,'half_b_views':1,'local_crop_views':22,'failed_unseen_deliveries':[],'retries':[],'same_target_recrops':[],'source_dimensions':man['original_size'],'half_dimensions':man['half_sizes'],'coordinate_processing':report['provenance']['coordinate_processing'],'processing_order':'packet reads; whole; a; b; dimension inspection; generate crop01-17; each viewed once in numerical order; generate five remaining independently open head/formula targets crop18-22; each viewed once in numerical order','boundary_limits':report['provenance']['boundary_limits']}
(p/'image_audit.json').write_text(json.dumps(imageaudit,ensure_ascii=False,indent=2)+'\n')
choices=[
{'location':'opening','exact_selection':"Soit alpha0 in K1, je dis que l'on a|on a; no colon",'evidence':'half a and crop01'},
{'location':'first formula','exact_selection':r'\widehat Sigma_alpha0 has no +; \widehat Sigma_i has +; right Sigmas have no roofs; i.e has no final point','evidence':'crops18,19,02'},
{'location':'parenthesis','exact_selection':r'(ce qui ach[è|é|e]vera la [demonstration|démonstration], car on aura; no close supplied','evidence':'crop03'},
{'location':'upper U and condition','exact_selection':r'U=X\setminus union_{alpha in K} roofed Sigma_alpha+; K=K1 union {i}; deleted Sigma_alpha; comme dans le lemme.','evidence':'half a,crops04,20'},
{'location':'Or line','exact_selection':'Or qualified comme on a; no colon and no added word','evidence':'crop05'},
{'location':'central inclusion','exact_selection':r'E_i subset U_{J,i}=X\setminus cup-with-cross-run_{alpha in K0} roofed Sigma_alpha+','evidence':'crop06'},
{'location':'second inclusion','exact_selection':r'cela implique que; E_i subset X\setminus roofed Sigma_alpha0+ = Sigma_[alpha0|alpha]-','evidence':'half a,crop07'},
{'location':'margin','exact_selection':'G05 owns j.e./i.e. cluster, top Sigma_i+ ou Sigma_i-, E_i, qualified Sigma_i alpha/i,alpha, E_alpha, Sigma_alpha0+, both sideways Sigma_i-/Sigma_i+, central sign and two braces','evidence':'crop08'},
{'location':'next argument','exact_selection':r"d'autre part alpha0 in K1 signifie; Sigma_alpha0+ not subset Sigma_i+",'evidence':'crops09,11'},
{'location':'conclusion','exact_selection':r'ce qui deleted[impli|impl.] signifie aussi que Sigma_i+ cap Sigma_alpha+ = empty, cqfd.','evidence':'crops10,22'},
{'location':'corollary heading','exact_selection':'Corollaire du lemme underlined; Pour une classe; no heading punctuation','evidence':'half b'},
{'location':'first corollary line','exact_selection':'V de Pi_I^[circle|zero], son expression','evidence':'half b,crop12'},
{'location':'corollary expression','exact_selection':r'V=X\setminus union_{alpha in K} roofed Sigma_alpha+; no added endpoint punctuation','evidence':'crop21'},
{'location':'corollary prose','exact_selection':'du lemme pr[é|ê]cédent est unique (single underline) -- on a','evidence':'crop17'},
{'location':'bottom K set','exact_selection':'bar V cap E_alpha != empty i.e. deleted V/live E_alpha cap dot V != empty; enclosing set braces present','evidence':'crop13'},
{'location':'last condition','exact_selection':r'Sigma_alpha+ est l’unique comp. de X\setminus Sigma_alpha contenue dans X\setminus V; no final point','evidence':'crop13'},
{'location':'archive','exact_selection':'20, comment only; no manuscript page marker or cotefile command','evidence':'half b'}]
sourceaudit={'scan':'021','reader':'C','complete_transcription_file':'reading.tex','actual_C_rows':report['actual_C_outcome_map'],'graphical_groups':gs,'source_choices_including_report_silent':choices,'macro_syntax_policy':'No new macro definitions. Standard math/TikZ/tikz-cd and the supplied PREAMBLE macros only. Macro conversions alone are not counted.','source_structure_review':struct,'original_C_note_and_slip_handling':{'C_notes_empty':True,'raw_slip_middle_index':'The C slip table describes Sigma_alpha- while C.tex and actual doubt row15 retain alpha0|alpha. This is kept as source provenance, with no extra C source row.','notation_rows':'Notation rows are not counted as actual C doubts.','other_sheet_context':'Shared notation other-page records were context only.'},'group_ownership_policy':'Each group gives its complete exact source excerpt, words, mathematical labels, marks, origin, baseline and crop. Point-only groups own no neighbouring word. Nested exact excerpts overlap their parent source by design; visible components are drawn once.','H_apparatus':report['provenance']['H_apparatus_classification'],'S_coverage':report['S_coverage'],'processing':report['provenance'],'check_events':[],'administrative_operations':'JSON parsing, source-offset searches, structural delimiter checks, diff creation and record counts; no mathematical result is claimed.'}
(p/'source_audit.json').write_text(json.dumps(sourceaudit,ensure_ascii=False,indent=2)+'\n')
md='''# Scan021 — reader C

The author writes the two empty intersections beginning with \\(\\widehat\\Sigma_{\\alpha_0}\\cap\\widehat\\Sigma_i^+=\\varnothing\\), gives \\(K=K_1\\cup\\{i\\}\\), and ends the proof with \\(\\Sigma_i^+\\cap\\Sigma_\\alpha^+=\\varnothing\\) and “cqfd.” The underlined corollary calls \\(V=X\\setminus\\bigcup_{\\alpha\\in K}\\widehat\\Sigma_\\alpha^+\\) unique and writes its final complement as \\(X\\setminus\\Sigma_\\alpha\\). These are the manuscript's assertions; no proof check was performed.

## Line-by-line reading audit

| Position | Selected reading and local qualification |
| --- | --- |
'''
for x in choices:md+='| '+x['location']+' | '+x['exact_selection'].replace('|',' / ')+' — '+x['evidence']+' |\n'
md+='''
## Original C doubt rows

The original source table has fifteen rows, each retained under its original order and identity. All have a local crop. Seven are resolved and eight retained.

| Canonical row | Local outcome | Reading |
| --- | --- | --- |
'''
for x in report['actual_C_outcome_map']:md+='| '+x['source_row_id']+' | '+x['status']+' | '+x['local_parts'][0]['reading'].replace('|',' / ')+' |\n'
md+='''
## Marks and limits

The literal groups preserve the upper cancelled Sigma, the two cancelled-word crossing runs, the overlaid V/E correction, the two marginal braces and transverse labels, the lower looped brace, the central union cross-stroke, the corollary union retrace, and the individual short Sigma head runs. The first repeated head-role ambiguity carries its printed qualifier; later local alternatives remain in the report. Six detached shape groups retain explicit uncertainty about their role, hand and surface origin.

The first roofed Sigma has no written plus. The first “i.e” has no final point. Both live occurrences of “signifie” are selected with their short final e. The opening l’on/on, the retraced comme, marginal lead-in and central sign, third marginal index, cancelled impli/impl., Pi ring, and terminal alpha0/alpha remain qualified. The additional accent and K-head/state qualifications are explicit in the complete source.

S's quoted examples have no matching formula on this sheet. The bar over V and the six existing roofs are already present in C and H. The separate Sigma head runs keep their local role qualification.

## Processing record

Whole, half a, half b and 22 distinct local crops were successfully viewed once each. No image delivery failed or required a retry. The initial combined text output was truncated; complete bounded packet reads followed before the images. No OCR, research, mathematical check, compilation or rendering was performed. Detailed coordinates, exact source group boundaries and the physical-edge limits are in the structured audits.
'''
(p/'reading.md').write_text(md)
(p/'assembly_status.json').write_text(json.dumps({'phase':'complete source, report and audits; final UTC sealing pending','checkpoint_pause':False,'structural_review':struct},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'structural_review':struct,'counts':report['counts']},ensure_ascii=False))
