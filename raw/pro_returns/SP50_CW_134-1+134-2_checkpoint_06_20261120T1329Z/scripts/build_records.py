"""Render the accumulated main-reader decisions into the requested deliverables."""
import csv,json,re
from pathlib import Path

O=Path(__file__).resolve().parents[1]
P='SP50_CW_134-1+134-2'
order=json.loads((O/'page_order.json').read_text())
decisions=[]
for page in order:
    key=f"{page['cote']}_scan{int(page['our_scan']):03d}"
    path=O/'decisions'/(key+'.json')
    if path.exists():decisions.append((page,json.loads(path.read_text())))

def cell(x):
    if x is None:return '—'
    if isinstance(x,(list,dict)):x=json.dumps(x,ensure_ascii=False)
    return str(x).replace('&','&amp;').replace('|','&#124;').replace('<','&lt;').replace('>','&gt;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)

counts=[];totc=toth=0;conf={'high':0,'medium':0,'low':0};consequential=[]
wconf={w:{k:0 for k in conf} for w in ['c','h']}
for p,d in decisions:
    changes=d.get('changes',[])
    actual=[x for x in changes if x.get('against_c') or x.get('against_h')]
    nc=sum(bool(x.get('against_c')) for x in actual);nh=sum(bool(x.get('against_h')) for x in actual)
    cs={k:sum(x.get('confidence')==k for x in actual) for k in conf}
    by_witness={w:{k:sum(bool(x.get('against_'+w)) and x.get('confidence')==k for x in actual) for k in conf} for w in ['c','h']}
    counts.append([p['cote'],p['our_scan'],nc,*[by_witness['c'][k] for k in conf],nh,*[by_witness['h'][k] for k in conf]])
    totc+=nc;toth+=nh
    for k in conf:conf[k]+=cs[k]
    for w in wconf:
        for k in conf:wconf[w][k]+=by_witness[w][k]
    for x in actual:
        if x.get('math_consequential'):consequential.append(f"- {p['cote']} scan {p['our_scan']}, {x['location']}: {x.get('consequence',x['final'])}")
changes_text=f'# {P} — Consolidated changes\n\nCounts are distinct adjudicated places, not edit distance or word error rates. A place can differ from both witnesses and is counted once for each witness. Confidence is counted separately against C and against H. Pure macro syntax is excluded. Removing or adding a genuine doubt mark counts as a change of reading status; retained doubts are recorded separately. H has no transcription for scan 002 and generates no H collation rows.\n\n'
changes_text+=table(['Cote','Scan','C total','C high','C medium','C low','H total','H high','H medium','H low'],counts+[['TOTAL','',totc,*[wconf['c'][k] for k in conf],toth,*[wconf['h'][k] for k in conf]]])
changes_text+='\n## Consequential corrections\n\n'+('\n'.join(consequential) if consequential else 'None recorded so far.')+'\n'
coll=[];invent=[];doubts=[];abbrev={};slips=[];notes=f'# {P} — Notes while reading\n\nThese notes concern only the supplied pages. Authorial claims are reported as claims. Transcription is not mathematical verification; check events below distinguish actual checks from statements carried as background.\n'
events=[]
math_events=O/'math_work/events.json'
if math_events.exists():
    for x in json.loads(math_events.read_text()):
        events.append([x['statement_id'],x['date'],x['who'],x['type'],x['outcome']])
for p,d in decisions:
    title=f"{p['cote']} — scan {int(p['our_scan']):03d} (H page {p['their_page']})"
    changes_text+='\n## '+title+'\n\n'
    actual=[];review=[]
    for x in d.get('changes',[]):
        ev=x.get('evidence','')
        if x.get('crop'):ev+=' Evidence: '+str(x['crop'])+'.'
        readings=x.get('readers',{})
        if readings:ev+=' Three readings: '+'; '.join(str(k)+' = '+str(v) for k,v in readings.items())+'.'
        if x.get('decision'):ev+=' Main decision: '+x['decision']
        row=[x['location'],x.get('c',''),x.get('h',''),x['final'],ev,x['confidence']]
        (actual if x.get('against_c') or x.get('against_h') else review).append(row)
        if x.get('against_h') and p['hua_has']=='text':
            kind=x.get('kind','other').replace(chr(92)*2+'ill{}',chr(92)+'ill{}')
            coll.append([p['folder'],p['their_page'],p['our_scan'],x['location'],x.get('h',''),x.get('c',''),x['final'],ev,kind,x.get('marked_in_H','no'),x['confidence']])
    headers=['Place','C','H','Final','What the scan shows and adjudication','Confidence']
    changes_text+=(table(headers,actual) if actual else 'No differences from the available witnesses.\n')
    if review:changes_text+='\n### Doubt and disagreement review without a changed reading\n\n'+table(headers,review)
    changes_text+='\n### Still unresolved\n\n'
    page_d=d.get('doubts',[])
    changes_text+=(table(['Place','Reading','Alternatives','Confidence','Reason'],[[x['location'],x['reading'],x.get('alternatives',''),x['confidence'],x.get('reason','')] for x in page_d]) if page_d else 'None.\n')
    for x in page_d:doubts.append([p['cote']+' / '+p['our_scan'],x['location'],x['reading'],x.get('alternatives',''),x['confidence'],x.get('reason','')])
    for x in d.get('inventory',[]):
        invent.append([p['our_scan'],x['sheet_kind'],x['hand'],x['element'],x['kind'],x['position'],x['first_words_or_objects'],x.get('transcribed','yes')])
    for x in d.get('abbreviations',[]):abbrev.setdefault(x['abbreviation'],set()).add(x['proposed_expansion'])
    for x in d.get('slips',[]):slips.append([p['cote']+' / '+p['our_scan'],x['location'],x['written'],x.get('apparent_intention',''),x.get('reason','')])
    notes+='\n## '+title+'\n\n'+d.get('notes','')+'\n'
    for x in d.get('checks',[]):
        events.append([x['statement_id'],x.get('date',d.get('decided_utc','')),x.get('who','GPT-6 Astra Pro; effort not exposed; main adjudication'),x['type'],x['outcome']])
    key=f"{p['cote']}_scan{int(p['our_scan']):03d}"
    for reader in ['r1','r2','r3']:
        rf=O/'readers'/key/reader/'report.json'
        if not rf.exists():continue
        rr=json.loads(rf.read_text())
        for i,x in enumerate(rr.get('checks',[])):
            override=d.get('reader_check_decisions',{}).get(reader+':'+str(i),{})
            if override.get('exclude'):continue
            who=str(rr.get('model','model not exposed'))+'; effort '+str(rr.get('effort','not exposed'))+'; '+key+'/'+reader
            sid=override.get('statement_id',x.get('statement_id',key+'.'+reader+'.check'+str(i+1)))
            events.append([sid,rr.get('finished_utc',d.get('decided_utc','')),who,override.get('type',x['type']),override.get('outcome',x['outcome'])])

(O/(P+'_changes.md')).write_text(changes_text)
with (O/(P+'_collation.tsv')).open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
with (O/(P+'_inventory.csv')).open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(invent)
(O/(P+'_notes.md')).write_text(notes)
dt=(O/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Cote / scan','Place','Reading','Alternatives','Confidence','Evidence / reason'],doubts)
dt+='\n## Abbreviations\n\nExpansions here are editorial aids only; the transcription preserves the abbreviation.\n\n'+table(['Abbreviation','Proposed expansion'],[[k,'; '.join(sorted(v))] for k,v in sorted(abbrev.items())])
dt+='\n## Apparent slips retained\n\n'+(table(['Cote / scan','Place','Written','Possible intention','Reason'],slips) if slips else 'No additional slip recorded so far.\n')
lp=O/'legibility.md'
dt+='\n## Legibility and witness comparison\n\n'+(lp.read_text() if lp.exists() else 'Work in progress. Legibility and witness comparison will be assessed after all pages have been read.\n')
(O/(P+'_doubts.md')).write_text(dt)
with (O/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome']);w.writerows(events)
texts=[]
for p,d in decisions:
    f=O/'pages'/Path(p['codex_file']).name
    if f.exists():texts.append(f.read_text().rstrip()+'\n')
(O/(P+'_transcription.tex')).write_text('\n'.join(texts))
(O/'summary_counts.json').write_text(json.dumps({'pages':len(decisions),'against_c':totc,'against_h':toth,'confidence_union':conf,'confidence_against_c':wconf['c'],'confidence_against_h':wconf['h'],'inventory_elements':len(invent),'remaining_doubts':len(doubts),'check_events':len(events)},indent=2)+'\n')
print(json.dumps({'pages':len(decisions),'C':totc,'H':toth,'doubts':len(doubts),'inventory':len(invent)}))
