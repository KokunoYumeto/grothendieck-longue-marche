"""Apply an explicit main-reader adjudication; never decide a reading automatically.

The manually authored config identifies a completed independent reading as a
base, every replacement/override, inspected crops, disagreements and notes.
"""
from pathlib import Path
import json,copy,argparse,sys,importlib.util
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('config');a=p.parse_args()
c=json.loads(Path(a.config).read_text());n=c['scan'];who=c['base']
if c.get('adjudicated') is not True:raise SystemExit('Explicit completed adjudication required')
reports={}
for l in 'ABC':
    rp=R/'readers'/f'scan{n:03}'/l/'report.json'
    reports[l]=json.loads(rp.read_text())
b=reports[who]
def rel(path):
    path=Path(path)
    return str(path.relative_to(R)) if path.is_absolute() else str(path)
cm={x['id']:rel(x['path']) for x in b.get('crops',[])}
changes=[]
for ix,original in enumerate(b['changes']):
    if ix in c.get('exclude_changes',[]):continue
    row=copy.deepcopy(original);row['final']=row.pop('reading')
    row['crops']=[cm[k] for k in row.pop('crop_ids',[]) if k in cm]
    row['marked_in_H']='yes' if row.get('marked_in_H') in [True,'yes','true'] else 'no'
    row.update(c.get('change_overrides',{}).get(str(ix),{}))
    changes.append(row)
changes+=c.get('extra_changes',[])
seen={rel(p) for p in c['inspected_crops']}
for row in changes:
    if row['against_c'] or row['against_h'] or row.get('readers'):
        if not row.get('crops'):raise SystemExit('Missing decision crop: '+row['place'])
        for cp in row['crops']:
            if cp not in seen:raise SystemExit('Uninspected decision crop: '+cp)
            if not (R/cp).exists():raise SystemExit('Missing crop file: '+cp)
text=(R/'readers'/f'scan{n:03}'/who/'reading.tex').read_text()
for s in c.get('substitutions',[]):
    count=text.count(s['old'])
    if count!=s.get('count',1):raise SystemExit(f'Replacement count {count} instead of expected for '+s['old'])
    text=text.replace(s['old'],s['new'])
unresolved=copy.deepcopy(c.get('unresolved',b.get('unresolved',[])))
unresolved=[u for i,u in enumerate(unresolved) if i not in c.get('exclude_unresolved',[])]
for u in unresolved:
    if isinstance(u.get('alternatives'),list):u['alternatives']='; '.join(u['alternatives'])
inventory=copy.deepcopy(c.get('inventory',reports[c.get('inventory_from',who)]['inventory']))
inventory+=c.get('extra_inventory',[])
for ix,i in enumerate(inventory):
    if c.get('sheet_kind'):i['sheet_kind']=c['sheet_kind']
    if i.get('transcribed') not in [True,'yes','true']:
        raise SystemExit('Inventory element is not fully transcribed: '+str(i))
    i['transcribed']='yes'
    i['element']=f'{n:03}.{ix+1:03} '+str(i.get('element',''))
notation=copy.deepcopy(c.get('notation',b.get('notation',[])))
for ix,v in c.get('notation_overrides',{}).items():notation[int(ix)].update(v)
notation+=c.get('extra_notation',[])
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
events=c.get('check_events',[])
for e in events:
    e.setdefault('date',now);e.setdefault('who','GPT-6 Astra Pro; effort not exposed; root scan%03d adjudication'%n)
for reader,indices in c.get('include_reader_math_checks',{}).items():
    rep=reports[reader]
    for ix in indices:
        event=rep['math_checks'][ix]
        events.append({'statement_id':event['statement_id'],'date':rep.get('end_utc',now),'who':str(rep.get('model','model not exposed'))+'; effort '+str(rep.get('effort','not exposed'))+f'; reader scan{n:03}_{reader}','type':event['type'],'outcome':event.get('place','')+': '+event.get('statement','')+' — '+event['outcome']})
used={cp for row in changes for cp in row.get('crops',[])}
d={'scan':n,'folder':c['folder'],'filename':c['filename'],'brief':c['brief'],'changes':changes,'unresolved':unresolved,'inventory':inventory,'notation':notation,'abbreviations':c.get('abbreviations',b.get('abbreviations',[])),'notes':c['notes'],'check_events':events,'additional_main_crops':sorted(seen-used)}
(R/'pages'/c['filename']).write_text(text)
(R/'decisions'/f'scan{n:03}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
sys.path.insert(0,str(R/'scripts'))
import assemble
assemble.rebuild()
spec=importlib.util.spec_from_file_location('workflow',R/'scripts/workflow.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
with (R/'progress.log').open('a') as f:f.write(f'scan {n:03} done {now}\n')
print('Committed scan %03d at %s'%(n,now))
