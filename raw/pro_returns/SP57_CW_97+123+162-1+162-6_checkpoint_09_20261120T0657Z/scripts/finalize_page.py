"""Apply a main-reader decision specification AFTER all three readings were compared.

The specification is authored by the main reader from viewed crops. This script
only assembles files; it never chooses a reading or recognizes image content.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,copy,re
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out'
spec=json.loads(Path(sys.argv[1]).read_text());stem=spec['stem']
meta=next(x for x in json.loads((OUT/'page_order.json').read_text()) if x['stem']==stem)
reports={r:json.loads((OUT/'readers'/stem/r/'report.json').read_text()) for r in ['R1','R2','R3']}
base=spec['base_reader'];r=reports[base]
t=(OUT/'readers'/stem/base/'reading.tex').read_text()
for edit in spec.get('text_edits',[]):
 old,new=edit['old'],edit['new'];count=t.count(old)
 assert count==edit.get('count',1),(old,count)
 t=t.replace(old,new)
ds=copy.deepcopy(r['differences'])
ds=[d for d in ds if d['id'] not in spec.get('exclude_difference_ids',[])]
for d in ds:
 d['final']=d.pop('reading',d.get('final',''))
 d['readers']='Three complete readings compared; no textual disagreement at this locus beyond any specified qualification.'
 d['marked_in_H']='yes' if '\\ill' in d.get('H','') or '\\uncertain' in d.get('H','') else 'no'
 if d['id'] in spec.get('difference_overrides',{}):d.update(spec['difference_overrides'][d['id']])
ds+=spec.get('additional_differences',[])
for d in ds:
 if not d.get('crop'):raise ValueError('Main-reader evidence crop required at '+d['id'])
 crop=OUT/d['crop']
 assert crop.exists(),crop
record=dict(cote=meta['cote'],scan=int(meta['our_scan']),folder=meta['folder'],their_page=int(meta['their_page']),stem=stem,brief=spec['brief'],differences=ds,c_doubts=spec.get('c_doubts',r['c_doubts']),remaining_doubts=spec['remaining_doubts'],inventory=spec.get('inventory',r['inventory']),notes=spec['notes'],abbreviations=spec.get('abbreviations',r.get('abbreviations',[])),consequential=spec.get('consequential',[]),crop_counts={k:v['crop_count'] for k,v in reports.items()}|{'main_new':spec.get('main_new_crops',0)},s_decisions=spec.get('s_decisions',[]))
dest=OUT/'pages'/(stem+'.tex')
assert not dest.exists(),'Do not overwrite a decided page through this assembler'
dest.write_text(t)
(OUT/'decisions'/(stem+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (OUT/'CHECK_EVENTS.tsv').open('a') as f:
 for event in spec.get('check_events',[]):
  f.write('\t'.join([event['statement_id'],now,event['who'],event['type'],event['outcome']]).replace('\n',' ')+'\n')
with (OUT/'progress.log').open('a') as f:
 f.write('scan '+str(meta['our_scan']).zfill(3)+' done '+now+' cote '+meta['cote']+'; three fresh readers compared; disagreements decided on crops\n')
with (OUT/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:
 f.write('\n## Page '+str(meta['order'])+' — '+meta['cote']+'/'+str(meta['our_scan']).zfill(3)+'\n\nBrief '+spec['brief']+'. Three fresh readers. Crops '+', '.join(k+' '+str(v) for k,v in record['crop_counts'].items())+'.\n\n'+spec.get('workflow_note','No brief change was required by this page.')+'\n')
print(json.dumps({'page':stem,'recorded_loci':len(ds),'remaining_doubts':len(record['remaining_doubts'])}))
