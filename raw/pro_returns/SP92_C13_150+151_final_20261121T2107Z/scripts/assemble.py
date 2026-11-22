"""Assemble reviewed records, preserving page order; does not invent readings."""
from pathlib import Path
import csv,json,collections,re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP92_C13_150+151'
ORDER=(ROOT/'page_order.txt').read_text().splitlines()
def write_table(path,cols,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols,delimiter=delimiter,extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def md(x):
    if x is None:return '—'
    return str(x).replace('|','&#124;').replace('\n','<br>')
def table(cols,rows):
    return '| '+' | '.join(cols)+' |\n| '+' | '.join(['---']*len(cols))+' |\n'+''.join('| '+' | '.join(md(x) for x in r)+' |\n' for r in rows)
def fmt_note(x):
    if isinstance(x,list):return '\n\n'.join(fmt_note(y) for y in x)
    if isinstance(x,dict):return '\n'.join(f'- {k}: {v}' for k,v in x.items())
    return str(x or '')
records=[]
for p in ORDER:
    f=ROOT/'records'/f'{p}.json'
    if f.exists():
        d=json.loads(f.read_text())
        if d.get('root_reviewed') and (ROOT/'pages'/f'{p}.tex').exists():records.append(d)
changes=[];collation=[];decisions=[];inventory=[];events=[];coverage=[]
summary=[];consequential=[];doubts=[];abbr=[];hands=[]
for d in records:
    p=d['page'];cs=d.get('changes',[])
    cnt=collections.Counter(c['confidence'] for c in cs)
    summary.append([p,sum(c['against_C'] for c in cs),sum(c['against_H'] for c in cs),cnt['high'],cnt['medium'],cnt['low']])
    for c in cs:
        c=dict(c,page=p)
        changes.append(c)
        evidence=c['evidence']
        if c.get('crop'):evidence+=f" Crop: {c['crop']}; box {tuple(c['box'])}."
        if c.get('against_H'):
            collation.append(dict(folder=d['cote'],their_page=str(int(d['scan'])-1),our_scan=d['scan'],line=c['place'],their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],scan_shows=evidence,kind=c['kind'],marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
        if c.get('consequential'):consequential.append(f"- {p}, {c['place']}: {c['C']} / H: {c['H']} → {c['final']}. {c['evidence']}")
    for a in d.get('decisions',[]):
        a=dict(a)
        a['what the ink shows']=a.get('ink','')
        a['crop']=f"{a['crop']} {tuple(a['box'])}" if a.get('crop') else 'page'
        decisions.append(a)
    inventory.extend(dict(x,scan=p) for x in d.get('inventory',[]))
    events.extend(d.get('check_events',[]))
    coverage.extend(dict(x,page=p,change_ids=', '.join(x.get('change_ids',[]))) for x in d.get('diff_coverage',[]))
    doubts.extend(dict(x,page=p) for x in d.get('doubts',[]))
    abbr.extend(dict(x,page=p) for x in d.get('abbreviations',[]))
    hands.extend(dict(x,page=p) for x in d.get('hand_log',[]))
total=['All reviewed pages']+[sum(r[i] for r in summary) for i in range(1,6)]
root_checks=ROOT/'records/root_mathematical_checks.json'
if root_checks.exists():
    keys=['statement_id','date','who','type','outcome']
    seen={tuple(e.get(k,'') for k in keys) for e in events}
    for event in json.loads(root_checks.read_text()):
        signature=tuple(event.get(k,'') for k in keys)
        if signature not in seen:
            events.append({k:event.get(k,'') for k in keys});seen.add(signature)
head=f'# {PREFIX}: changes against the two witnesses\n\nReviewed pages: {len(records)} of {len(ORDER)}. Counts are places, not changed tokens. A place may differ from both witnesses, so the C and H columns overlap. Confidence columns count each logged place once. Additions of doubt alone and same-reading macro differences are excluded. Resolved C doubt marks are logged with crop evidence, including cases where the first reading is confirmed; these may change certainty rather than the underlying word.\n\n'
head+=table(['Page','Against C','Against H','High','Medium','Low'],summary+[total])
head+='\n## Consequential corrections\n\n'+'\n'.join(consequential)+'\n'
for d in records:
    head+=f"\n## {d['page']}\n\n"
    rows=[]
    for c in d.get('changes',[]):
        ev=c['evidence']
        if c.get('crop'):ev+=f" [{c['crop']}]({c['crop']}), original-pixel box {tuple(c['box'])}."
        rows.append([c['id']+': '+c['place'],c['C'],c['H'],c['final'],ev,c['confidence']])
    head+=table(['Place','Witness C','Witness H','Consolidated reading','What the scan shows','Confidence'],rows)
    head+='\n### Unresolved places\n\n'
    dd=d.get('doubts',[])
    head+=('\n'.join(f"- {x['place']}: `{x['reading']}`. {x.get('reason','')}" for x in dd) if dd else 'None remaining.')+'\n'
    if d.get('audited'):
        head+='\n### Changes after the blind second reading\n\n'
        aa=d.get('audit_changes',[])
        head+=(table(['Box','First reading','Blind second reading','Adjudicated reading','Ink evidence'],[[x['box'],x['first'],x['second'],x['final'],x['evidence']+' Crop: '+x['crop']] for x in aa]) if aa else 'No reading changed after image adjudication.')+'\n'
(ROOT/f'{PREFIX}_changes.md').write_text(head)
write_table(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
decisions.sort(key=lambda x:int(re.search(r'\d+',x['id']).group()))
write_table(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
write_table(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
write_table(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
write_table(ROOT/'diff_coverage.tsv',['page','diff_id','classification','change_ids','reason'],coverage)
notes=f'# {PREFIX}: notes while reading\n\nThese notes concern only the supplied manuscript pages. A summary of a claim is not a proof check. Actual mathematical checks or uses, when performed, are separately recorded in CHECK_EVENTS.tsv.\n'
for d in records:notes+=f"\n## {d['page']}\n\n{fmt_note(d.get('notes'))}\n"
(ROOT/f'{PREFIX}_notes.md').write_text(notes)
dd=f'# {PREFIX}: notation and remaining doubts\n\n'+(ROOT/'notation.md').read_text()+'\n## Remaining doubts\n\n'
dd+=table(['Page','Place','Reading','Alternatives','Confidence','Reason'],[[x['page'],x['place'],x['reading'],x.get('alternatives',''),x['confidence'],x.get('reason','')] for x in doubts])
dd+='\n## Abbreviations (expansions only in this list)\n\n'+table(['Page','Written form','Proposed expansion'],[[x['page'],x.get('form',''),x.get('expansion','')] for x in abbr])
leg=ROOT/'records/legibility.md'
dd+='\n## Legibility and witnesses\n\n'+(leg.read_text() if leg.exists() else 'Reading is in progress; final assessment will be added after the independent audit.')+'\n'
(ROOT/f'{PREFIX}_doubts.md').write_text(dd)
hh=f'# {PREFIX}: handwriting log\n\nEach entry records a habit observed on the cited page; a local observation is not a universal identification rule.\n\n'
hh+=table(['Page','Habit','Places','Scope/consistency','Witness errors'],[[x['page'],x.get('habit',''),x.get('places',''),x.get('scope',''),x.get('witness_errors','')] for x in hands])
(ROOT/f'{PREFIX}_hand_log.md').write_text(hh)
types={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left illegible',6:'Insertion placement',7:'Struck text / state',8:'Abbreviation / spelling normalization',9:'Text not on page',10:'Other'}
counts=collections.Counter()
for c in changes:
    try:k=int(str(c['error_kind']).split()[0])
    except (ValueError,KeyError):k=10
    counts[k]+=1
feedback=f'# {PREFIX}: error-sheet feedback\n\nCounts below concern logged reading places differing from C or H, assigned one primary error-sheet kind per place. They are not token error rates; both witnesses may differ at the same place. No rates from prior runs are used as evidence for a reading.\n\n'
feedback+=table(['Error-sheet kind','Places'],[[types[i],counts[i]] for i in range(1,11)])
extra_feedback=ROOT/'records/recurring_feedback.md'
feedback+='\n## Recurring local observations\n\n'+(extra_feedback.read_text() if extra_feedback.exists() else 'Reading and blind audit are in progress; the final recurring-error assessment will be inserted here.')+'\n'
(ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
combined=[];lastcote=None
for d in records:
    if d['cote']!=lastcote:
        combined.append('\\cotefile{'+str(d['cote'])+'}\n');lastcote=d['cote']
    page_text=(ROOT/'pages'/f"{d['page']}.tex").read_text()
    page_text=re.sub(r'^\\cotefile\{[^}]+\}\s*\n','',page_text,count=1)
    combined.append(page_text.rstrip()+'\n')
(ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(combined))
print(json.dumps({'reviewed_pages':len(records),'changes':len(changes),'against_C':total[1],'against_H':total[2],'decisions':len(decisions),'inventory':len(inventory),'events':len(events),'doubts':len(doubts)}))
