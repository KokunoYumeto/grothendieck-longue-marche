from pathlib import Path
from datetime import datetime, timezone
import collections, csv, hashlib, json, re

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'result'
csv.field_size_limit(16*1024*1024)
ORDER=(OUT/'page_order.txt').read_text().splitlines()

def read_tsv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def args(s, names=('unsure',)):
    result=[]
    pattern=re.compile(r'\\('+'|'.join(map(re.escape,names))+r')\s*\{')
    for m in pattern.finditer(s):
        start=m.end(); pos=start; depth=1
        while pos<len(s) and depth:
            ch=s[pos]
            slashes=0;j=pos-1
            while j>=0 and s[j]=='\\':slashes+=1;j-=1
            if not slashes%2:
                if ch=='{':depth+=1
                elif ch=='}':depth-=1
            pos+=1
        if depth==0:result.append({'macro':m[1],'start':m.start(),'end':pos,'arg':s[start:pos-1]})
    return result

def first_alt(s):
    depth=0
    for i,ch in enumerate(s):
        slashes=0;j=i-1
        while j>=0 and s[j]=='\\':slashes+=1;j-=1
        if slashes%2:continue
        if ch=='{':depth+=1
        elif ch=='}':depth-=1
        elif ch=='|' and depth==0:return s[:i]
    return s

def without_certainty(s):
    for _ in range(20):
        matches=args(s,('unsure','uncertain'))
        if not matches:return s
        # Process only outermost matches to avoid applying stale nested offsets.
        outer=[]
        for m in matches:
            if not any(a['start']<=m['start']<a['end'] for a in outer):outer.append(m)
        for m in reversed(outer):s=s[:m['start']]+first_alt(m['arg'])+s[m['end']:]
    return s

def ws(s):return re.sub(r'\s+',' ',s).strip()
def norm(s):return ws(without_certainty(s))

def plain_macros(s):
    s=without_certainty(s)
    for _ in range(20):
        matches=args(s,('text','textrm','mathrm','mbox'))
        if not matches:break
        outer=[]
        for m in matches:
            if not any(a['start']<=m['start']<a['end'] for a in outer):outer.append(m)
        for m in reversed(outer):s=s[:m['start']]+m['arg']+s[m['end']:]
    s=s.replace('\\(','').replace('\\)','').replace('$','')
    return ws(s)

records={p:json.loads((OUT/'records'/f'{p}.json').read_text()) for p in ORDER}
diagnostics={'generated_utc':datetime.now(timezone.utc).isoformat(),'scope':'Read-only static metadata audit; no image or manuscript reading judgments.','snapshots':{},'counts':{},'schema_issues':[],'exact_flags':[],'certainty_flags':[],'macro_candidates':[],'potential_doubt_mapping_gaps':[],'potential_stale_doubts':[],'unmapped_check_events':[],'missing_crop_files':[],'missing_review_registration':[],'missing_final_spans':[],'aggregate_mismatches':[]}
ids=[];markids=[];all_noteids=set();all_changes=[]
for page,r in records.items():
    for n in r.get('notes',[]):
        if isinstance(n,dict):all_noteids.add(n.get('id'))
for page,r in records.items():
    page_path=OUT/'pages'/f'{page}.tex'
    page_text=page_path.read_text()
    diagnostics['snapshots'][page]={'record_sha256':hashlib.sha256((OUT/'records'/f'{page}.json').read_bytes()).hexdigest(),'page_sha256':hashlib.sha256(page_path.read_bytes()).hexdigest(),'audited':bool(r.get('audit'))}
    required=['page','reader','lines_read','changes','decisions','doubts','inventory','notes','check_events','notation','abbreviations','second_boxes']
    for key in required:
        if key not in r:diagnostics['schema_issues'].append({'page':page,'missing':key})
    for c in r['changes']:
        ids.append(c['id']);all_changes.append((page,c))
        needed=['id','place','c','h','final','diff_c','diff_h','kind','error_kind','evidence','crop','box','confidence','marked_in_h','consequential']
        for key in needed:
            if key not in c:diagnostics['schema_issues'].append({'id':c['id'],'missing':key})
        for witness in ('c','h'):
            if not c.get('diff_'+witness):continue
            info={k:c[k] for k in ('id','place','c','h','final','diff_c','diff_h','kind','evidence','confidence')}
            info.update({'page':page,'audited':bool(r.get('audit')),'witness':witness.upper()})
            if ws(c['final'])==ws(c[witness]):diagnostics['exact_flags'].append(info)
            elif norm(c['final'])==norm(c[witness]):diagnostics['certainty_flags'].append(info)
            elif plain_macros(c['final'])==plain_macros(c[witness]):diagnostics['macro_candidates'].append(info)
        final=ws(c['final'])
        if r.get('audit') and len(final)<350 and '\\figure' not in final and '\\diagram' not in final and final not in ws(page_text):
            diagnostics['missing_final_spans'].append({'page':page,'id':c['id'],'place':c['place'],'final':c['final'],'flags':[c['diff_c'],c['diff_h']]})
    for d in r['decisions']:markids.append(d['id'])
    registered=set(r.get('main_reader_crops',[]))
    for group in ('changes','decisions','implicit_decisions'):
        for obj in r.get(group,[]):
            p=obj.get('crop')
            if p and p!='page':
                if not (OUT/p).is_file():diagnostics['missing_crop_files'].append({'page':page,'group':group,'id':obj.get('id'), 'crop':p})
                mandatory=bool(obj.get('diff_c') or obj.get('diff_h') or obj.get('decision') in ('first','alternative','other'))
                if mandatory and p not in registered:diagnostics['missing_review_registration'].append({'page':page,'group':group,'id':obj.get('id'),'crop':p})
    for e in r.get('check_events',[]):
        if e.get('statement_id') not in all_noteids:diagnostics['unmapped_check_events'].append({'page':page,**e})
    doubt_text='\n'.join(str(d.get('reading',''))+'\n'+str(d.get('alternatives',''))+'\n'+str(d.get('place',''))+'\n'+str(d.get('reason','')) for d in r.get('doubts',[]))
    for m in args(page_text,('unsure','illegible')):
        if len(m['arg'])>1000:continue
        if ws(m['arg']) not in ws(doubt_text):
            diagnostics['potential_doubt_mapping_gaps'].append({'page':page,'audited':bool(r.get('audit')),'macro':m['macro'],'argument':m['arg'],'context':page_text[max(0,m['start']-55):min(len(page_text),m['end']+55)]})
    for i,d in enumerate(r.get('doubts',[]),1):
        target=d.get('reading','')
        if 1<len(target)<200 and not ws(target) in ws(page_text):
            diagnostics['potential_stale_doubts'].append({'page':page,'audited':bool(r.get('audit')),'index':i,**d})

for name,sequence in [('change ids',ids),('decision ids',markids)]:
    for key,n in collections.Counter(sequence).items():
        if n>1:diagnostics['schema_issues'].append({'duplicate':name,'id':key,'count':n})

dec=read_tsv(OUT/'decisions.tsv')
recdec={d['id']:(page,d) for page,r in records.items() for d in r['decisions']}
for d in dec:
    if d['id'] not in recdec:diagnostics['aggregate_mismatches'].append({'table':'decisions','id':d['id'],'problem':'not in records'})
    else:
        page,x=recdec[d['id']]
        for k in ('decision','reading','confidence'):
            if d[k]!=x[k]:diagnostics['aggregate_mismatches'].append({'table':'decisions','id':d['id'],'field':k,'aggregate':d[k],'record':x[k]})
coll=read_tsv(OUT/'SP83_C13_148+149_collation.tsv')
collmap=collections.defaultdict(list)
for c in coll:collmap[(c['folder']+'_scan'+c['our_scan'].zfill(3),c['line'])].append(c)
for page,c in all_changes:
    if c.get('diff_h'):
        matches=collmap.get((page,c['place']),[])
        if not matches:diagnostics['aggregate_mismatches'].append({'table':'collation','id':c['id'],'problem':'missing H row'})
        elif not any(x['final_reading']==c['final'] for x in matches):diagnostics['aggregate_mismatches'].append({'table':'collation','id':c['id'],'field':'final','aggregate':[x['final_reading'] for x in matches],'record':c['final']})

diagnostics['counts']={'pages':len(records),'audited':sum(bool(r.get('audit')) for r in records.values()),'changes_total':len(all_changes),'material_places':sum(bool(c['diff_c'] or c['diff_h']) for p,c in all_changes),'against_c':sum(bool(c['diff_c']) for p,c in all_changes),'against_h':sum(bool(c['diff_h']) for p,c in all_changes),'record_decisions':len(markids),'aggregate_decisions':len(dec),'aggregate_h_rows':len(coll),'record_doubts':sum(len(r['doubts']) for r in records.values()),'inventory_elements':sum(len(r['inventory']) for r in records.values())}
target=OUT/'qa'/'reader_b_static_diagnostics.json'
target.write_text(json.dumps(diagnostics,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(target),'counts':diagnostics['counts'],'candidate_counts':{k:len(v) for k,v in diagnostics.items() if isinstance(v,list)}},indent=2))
