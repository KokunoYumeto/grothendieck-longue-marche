from pathlib import Path
import json,hashlib,sys
OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/022/A')
end_utc=sys.argv[1]
tex=(OUT/'reading.tex').read_text()
g=json.loads((OUT/'graphical_audit.json').read_text())
s=json.loads((OUT/'source_audit.json').read_text())
r=json.loads((OUT/'report.json').read_text())
v=json.loads((OUT/'structural_validation.json').read_text())
# Complete selected final-Sigma group, including both independently qualified points.
lookup={x['id']:x for x in g['groups']}
a=lookup['A022-S17']['source_start_byte_utf8'];b=lookup['A022-M06-below-beta-point']['source_end_byte_utf8']
composite={'id':'A022-complete-last-Sigma','children':['A022-S17','A022-M05-sigma-inner-point','A022-M06-below-beta-point'],'observed_bbox':[1194,1928,1298,2054],'origin':[0,0],'coordinate_map':'all children share original full-scan coordinates; nested marker pictures have the documented base-west origins and cancelling scope translations','owns':'complete final Sigma head, body, roof, plus, beta, inner point and below-right point once; union and its limit remain outside','source_start_byte_utf8':a,'source_end_byte_utf8':b,'complete_source_excerpt':tex.encode()[a:b].decode(),'source_quality':'manual selected graphical group; no rendered or metric validation'}
g['complete_composites']=[composite]
g['component_count_convention']='Each listed draw command contains one continuous path; each fill command contains one point-shaped fill. Paths can share endpoints or cross within a complete group. Command counts are kept separate from physical glyph/cluster counts and from font-rendered label strokes.'
for group in g['groups']:
 owned=[p for p in s['all_literal_paths'] if p['owner']==group['id']]
 group['own_literal_draw_commands']=sum(p['command_kind']=='draw' for p in owned)
 group['own_literal_fill_commands']=sum(p['command_kind']=='fill' for p in owned)
s['complete_graphical_composites']=[composite]
s['component_count_convention']=g['component_count_convention']
s['final_source_sha256']=hashlib.sha256(tex.encode()).hexdigest()
s['validation_result_file']='structural_validation.json'
s['resolved_concrete_source_defects']=['Exact C source-line bounds corrected at the small annotations, Comme passage, inverse display, Soit line and precise clause.','S12 head/body source path now shares the declared upper vertex, matching its connected-arm source classification.','Actual H quoted scopes preserve their original line wraps and apostrophe, with local marker flags confined to the two ill placeholders.']
r['end_utc']=end_utc
r['status']='final immutable independent reader return; root adjudication pending'
r['source_validation']={'file':'structural_validation.json','passed':v['passed'],'check_count':len(v['checks']),'source_sha256':v['source_sha256'],'scope':'required structural source, selected-reading coverage and ownership checks only; no optional broad validation after completion'}
r['complete_graphical_composite_file']='graphical_audit.json'
r['provenance']['final_immutable_status']='All files under out/readers/022/A are frozen after final_immutable.json is written. Root alone adjudicates and commits.'
r['provenance']['source_audit_repairs']=s['resolved_concrete_source_defects']
p=json.loads((OUT/'progress.json').read_text())
p.update(status='final immutable',end_utc=end_utc,next_step='none; independent return complete, root adjudication pending',return_complete=True,final_main_files=['reading.tex','report.json','reading.md'],structural_validation_passed=v['passed'])
view=json.loads((OUT/'viewing_audit.json').read_text());view['end_utc']=end_utc;view['final_status']='all 18 delivered views completed once; no unseen failed delivery; no recrop'
for name,obj in [('graphical_audit.json',g),('source_audit.json',s),('report.json',r),('progress.json',p),('viewing_audit.json',view)]:
 (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for path in sorted(OUT.rglob('*')):
 if path.is_file() and path.name!='final_immutable.json':
  data=path.read_bytes();manifest.append({'path':str(path.relative_to(OUT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
final={'scan':22,'reader':'A','start_utc':r['start_utc'],'end_utc':end_utc,'status':'FINAL IMMUTABLE','mutations_after_this_file':'none authorized in this independent return','main_files':['reading.tex','report.json','reading.md'],'manifest_excludes':'final_immutable.json itself to avoid circular hashing','files':manifest,'counts':r['count_proposal'],'validation':r['source_validation']}
(OUT/'final_immutable.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
main={x['path']:x['sha256'] for x in manifest if x['path'] in final['main_files']}
print(json.dumps({'end_utc':end_utc,'status':'FINAL IMMUTABLE','main_sha256':main,'manifest_sha256':hashlib.sha256((OUT/'final_immutable.json').read_bytes()).hexdigest(),'manifest_files':len(manifest),'counts':{'difference_rows':len(r['differences']),'C_physical':r['count_proposal']['C']['physical_cluster_count'],'H_physical':r['count_proposal']['H']['physical_cluster_count'],'C_source_doubts':7,'resolved':1,'retained':6,'remaining_doubt_records':len(r['doubts']),'inventory':len(r['inventory']),'graphics':39,'Sigma_groups':17,'draw_commands':98,'fill_commands':2,'crops':15,'views':18},'source_validation_passed':v['passed']},ensure_ascii=False))
