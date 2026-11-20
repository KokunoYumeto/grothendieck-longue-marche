#!/usr/bin/env python3
"""Apply a main-reader decision specification; never decide or recognize readings."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,copy,re
p=argparse.ArgumentParser();p.add_argument('page');a=p.parse_args()
out=Path(__file__).resolve().parent.parent; page=a.page
cfg=json.loads((out/'adjudication'/page/'decision.json').read_text())
reports={r:json.loads((out/'readers'/page/r/'report.json').read_text()) for r in ['R1','R2','R3']}
base=cfg.get('base_reader','R1'); report=copy.deepcopy(reports[base])
text=(out/'readers'/page/base/'reading.tex').read_text()
for change in cfg.get('replacements',[]):
    old,new=change['old'],change['new'];expected=change.get('count',1)
    if text.count(old)!=expected:raise SystemExit(f'Replacement count mismatch for {old!r}: {text.count(old)} != {expected}')
    text=text.replace(old,new)
order=json.loads((out/'records/page_order.json').read_text());m=next(r for r in order if r['page']==page)
first=next(r for r in order if r['cote']==m['cote'])['page']==page
if first and not re.search(r'\\cotefile\{'+str(m['cote'])+r'\}',text):text='\\cotefile{'+str(m['cote'])+'}\n'+text
rec={k:m[k] for k in ['page','folder','cote','our_scan','their_page','hua_has']}
rec['changes']=[]
for x in cfg.get('changes',[]):
    if 'source' in x:
        r,i=x['source'];entry=copy.deepcopy(reports[r]['changes'][i]);entry['final']=entry.pop('reading')
    else:entry={}
    for k,v in x.items():
        if k not in ['source','reader_sources']:entry[k]=v
    if 'reader_sources' in x:
        entry['reader_readings']={r:reports[r]['changes'][i]['reading'] for r,i in x['reader_sources'].items()}
    if set(entry.get('reader_readings',{}))!={'R1','R2','R3'}:raise SystemExit('Every adjudicated row requires all three readings: '+str(entry.get('place')))
    if not entry.get('evidence'):raise SystemExit('Missing main-reader crop evidence: '+str(entry.get('place')))
    entry['adjudicator']='root';rec['changes'].append(entry)
for key in ['c_doubts','remaining_doubts','inventory','notes','notation','abbreviations','check_events','prior_flags']:
    rec[key]=copy.deepcopy(cfg.get(key,report.get(key,[] if key!='notes' else {})))
for edit in cfg.get('inventory_edits',[]):
    index=edit['index'];rec['inventory'][index].update({k:v for k,v in edit.items() if k!='index'})
rec['inventory']+=cfg.get('inventory_add',[])
for i,element in enumerate(rec['inventory'],1):element['element']=str(m['cote'])+'-'+str(m['our_scan']).zfill(3)+'-'+str(i).zfill(3)
rec['notes'].update(cfg.get('notes_update',{}))
if cfg.get('background_summary_event',True):
    rec['check_events'].append({'statement_id':page+':summary','date':datetime.now(timezone.utc).date().isoformat(),'who':'GPT-6 Astra Pro; effort not exposed; root adjudication','type':'carried as background without fault found','outcome':cfg.get('summary_event_outcome','The reading note attributes the statements to this page. This event records their use as source content; it claims no proof verification beyond the separately specified mathematical events.')})
rec['rejected_difference_rows']=cfg.get('rejected_difference_rows',[])
rec['reader_only_decisions']=cfg.get('reader_only_decisions',[])
rec['adjudicated_crops']=cfg.get('adjudicated_crops',[])
rec['completed_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record=out/'records'/(page+'.json')
if record.exists():raise SystemExit('Page already recorded; refusing to overwrite completion without explicit correction workflow.')
(out/'pages'/(page+'.tex')).write_text(text)
record.write_text(json.dumps(rec,ensure_ascii=False,indent=2))
with (out/'progress.log').open('a') as f:f.write('cote '+str(m['cote'])+' scan '+str(m['our_scan']).zfill(3)+' done '+rec['completed_utc']+'\n')
print(json.dumps({'page':page,'changes':len(rec['changes']),'remaining_doubts':len(rec['remaining_doubts']),'inventory':len(rec['inventory'])}))
