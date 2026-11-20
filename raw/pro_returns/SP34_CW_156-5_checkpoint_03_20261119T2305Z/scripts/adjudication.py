"""Record explicit main-reader decisions. Does not select readings automatically."""
from pathlib import Path
import json, datetime, re
O=Path(__file__).resolve().parents[1]

def reports(n):
    return [json.loads((O/f'readers/R{i}/scan{n:03}.json').read_text()) for i in (1,2,3)]

def differences(d):
    return d.get('differences',d.get('differences_and_reviews',[]))

def reading(x):
    return x.get('reading',x.get('proposed_reading',x.get('proposed','')))

def checks(rr):
    out=[]
    for i,d in enumerate(rr,1):
        for e in d.get('checks',d.get('mathematical_checks',d.get('check_events',[]))):
            e=dict(e)
            e.setdefault('date',d.get('end_utc',datetime.datetime.now(datetime.timezone.utc).date().isoformat()))
            e.setdefault('who',f'GPT-6 Astra Pro; R{i}; inherited effort not separately exposed; SP34 second pass')
            if isinstance(e['who'],dict) or 'GPT-' not in str(e['who']):
                e['who']=f'GPT-6 Astra Pro; R{i}; inherited effort not separately exposed; SP34 second pass'
            if e.get('refined_statement_id') and e['refined_statement_id'] not in e.get('outcome',''):
                e['outcome']+=' Refined statement: '+e['refined_statement_id']+'.'
            out.append(e)
    return out

def row(n,i,x,reader_readings,crop,**overrides):
    y={'id':f'{n:03}-{i:02}','place':x['place'],'C':x.get('C',''),'H':x.get('H',''),
       'readers':reader_readings,'final':reading(x),'ink':x.get('ink',''),
       'crop':f'Main enlargement {crop}; recipes in documentation/crops.jsonl.',
       'confidence':x.get('confidence','medium'),'kind':x.get('kind','other'),
       'against_C':x.get('against_C',False),'against_H':x.get('against_H',False),
       'marked_in_H':'yes' if x.get('marked_in_H') in (True,'yes') else 'no'}
    y.update(overrides)
    if y['kind']=='deletion state':y['kind']='deletion state (struck given live or live given struck)'
    if y['kind'] in ('C doubt review','notation review','C slip review'):
        y.setdefault('review_type',y['kind']);y['kind']='other'
    if y['kind']=='readable ink left as \\ill{}':y['kind']='readable ink left as `\\ill{}`'
    if '\\unsure' in y['C'] and not y.get('review_type'):y['review_type']='C doubt reviewed'
    return y

def unsure_occurrences(t):
    """Read balanced macro arguments, preserving mathematical bars as written."""
    result=[];pos=0
    while True:
        a=t.find('\\unsure{',pos)
        if a<0:break
        b=a+8;depth=1;j=b
        while j<len(t) and depth:
            if t[j] in '{}':
                k=j-1
                while k>=0 and t[k]=='\\':k-=1
                if (j-1-k)%2==0:depth+=1 if t[j]=='{' else -1
            j+=1
        if depth:raise ValueError('unbalanced unsure argument')
        result.append((a,t[b:j-1]));pos=b
    return result

def doubt_alternatives(arg):
    """Split only top-level alternative bars, preserving nested marked text."""
    if arg.startswith('|'):
        return [arg]
    parts=[];depth=0;start=0
    for i,c in enumerate(arg):
        if c in '{}':
            k=i-1
            while k>=0 and arg[k]=='\\':k-=1
            if (i-1-k)%2==0:depth+=1 if c=='{' else -1
        elif c=='|' and depth==0:
            parts.append(arg[start:i]);start=i+1
    parts.append(arg[start:]);return parts

def make_doubts(t,rows):
    out=[]
    for a,arg in unsure_occurrences(t):
        full='\\unsure{'+arg+'}'
        matches=[r for r in rows if full in r['final']]
        r=matches[0] if len(matches)==1 else None
        # A generic source location is exact and does not manufacture a semantic match.
        context=t[max(0,a-65):a].splitlines()[-1] if t[max(0,a-65):a].splitlines() else ''
        parts=doubt_alternatives(arg)
        out.append({'place':r['place'] if r else 'LaTeX line '+str(t.count('\n',0,a)+1)+'; '+context,
                    'reading':parts[0],'alternatives':' | '.join(parts[1:]),
                    'confidence':r['confidence'] if r else 'low',
                    'reason':r['ink'] if r else 'Retained uncertainty; see the corresponding locus and independent reader reports.'})
    return out

def save(n,t,rows,inventory,notes,rr,notation=None,abbreviations=None,overview='',extra_checks=None):
    folder='J156-5-04' if n<=33 else 'J156-5-05' if n<=41 else 'J156-5-06'
    fn=f'{folder}_156-5_scan{n:03}.tex'
    if (O/'decisions'/f'scan{n:03}.json').exists():raise RuntimeError('Page already finalized; explicit revision required')
    ds=make_doubts(t,rows)
    d={'scan':n,'folder':folder,'filename':fn,'manuscript':str(n-1),'overview':overview,
       'rows':rows,'inventory':inventory,'doubts':ds,
       'unresolved':[x['place']+': '+x['reading'] for x in ds],
       'notes':notes,'checks':checks(rr)+(extra_checks or []),
       'notation':notation or [],'abbreviations':abbreviations or {}}
    (O/'pages'/fn).write_text(t.rstrip()+'\n')
    (O/'decisions'/f'scan{n:03}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    # Assemble required records before recording completion and allowing the next page.
    import build_records
    build_records.main()
    now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
    with (O/'progress.log').open('a') as f:f.write(f'scan {n:03} done {now}\n')
    p=O/'documentation/run.json';s=json.loads(p.read_text());s['completed_scans'].append(n);p.write_text(json.dumps(s,indent=2)+'\n')
