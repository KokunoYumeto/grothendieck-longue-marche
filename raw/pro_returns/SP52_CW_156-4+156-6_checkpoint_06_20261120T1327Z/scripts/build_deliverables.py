"""Rebuild current deliverables from the adjudicator's page decisions, without altering pages."""
from pathlib import Path
import csv,json,re,collections

OUT=Path(__file__).resolve().parents[1]
ID='SP52_CW_156-4+156-6'
def md(s):
    if s is None:return '—'
    if not isinstance(s,str):s=json.dumps(s,ensure_ascii=False)
    return s.replace('|','\\|').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(md(c) for c in row)+' |' for row in rows])+'\n'
def ink_evidence(row,field='scan_shows'):
    """Expose record scope and all cited crops in the actual user-facing logs."""
    value=str(row.get(field,''))
    scope=row.get('scope_note')
    if scope and scope not in value:value+=' Scope: '+scope
    paths=[]
    for item in [row.get('crop')]+list(row.get('supporting_crops') or []):
        if not item:continue
        for path in str(item).split(';'):
            path=path.strip()
            if path and path not in paths:paths.append(path)
    if paths:value+=' ['+'; '.join(paths)+']'
    return value
order=json.loads((OUT/'page_order.json').read_text())
decisions=[]
for m in order:
    p=OUT/'decisions'/f"{m['cote']}_{int(m['our_scan']):03d}.json"
    if p.exists():decisions.append(json.loads(p.read_text()))
changes=['# Consolidated readings and changes\n','Counts are editorial loci, not individual characters or word-error estimates. Confidence counts apply to change rows. The three independent readings and every retained C doubt are documented below.\n']
countrows=[];conseq=[];allconf=collections.Counter();ct=ht=0
for d in decisions:
    rows=d.get('differences',[]);co=collections.Counter(x.get('confidence','medium') for x in rows)
    c=sum(bool(x.get('change_c')) for x in rows);h=sum(bool(x.get('change_h')) for x in rows)
    ct+=c;ht+=h;allconf.update(co)
    countrows.append([d['key'],c,h,co['high'],co['medium'],co['low']])
    for x in rows:
        if x.get('math_consequential'):conseq.append(f"- {d['key']}, {x['location']}: `{x['reading']}` — {x.get('consequence',x['scan_shows'])}")
countrows.append(['TOTAL',ct,ht,allconf['high'],allconf['medium'],allconf['low']])
changes.append(table(['Cote / scan','Against C','Against H','High','Medium','Low'],countrows))
changes+=['## Consequential corrections\n','\n'.join(conseq) if conseq else 'None established so far.','']
collation=[];inventory=[];notes=['# Notes while reading\n','Only these supplied pages were used. A summary of a manuscript assertion is not a proof endorsement. CHECK_EVENTS.tsv identifies the mathematics actually checked or carried as background.\n'];doubts=[];abbrev={};checks=[]
workflow=['# Reading workflow\n','Each page was assigned, in sequence, to three fresh isolated sub-agents with no inherited conversation. Each received its own page images, C and H page excerpts, C’s prior doubts/audit, the conventions, and the notation snapshot. The adjudicator retained their returns and inspected the disputed loci as crops. Original page and half images are not copied into this deliverable. Reader returns, their crop evidence and inspection logs are retained.\n','## Reader brief versions\n','The exact briefs are in briefs/. The first is brief_v01.md; later versions and reasons are recorded in brief_changes.md.\n','## Per-page execution\n']
wfrows=[]
for d in decisions:
    key=d['key'];rows=d.get('differences',[])
    changes+=['## '+key+'\n',table(['Place','C','H','Final','Ink evidence / crop','Confidence','R1 / R2 / R3; adjudication'],[[x['location'],x.get('c'),x.get('h'),x['reading'],ink_evidence(x),x.get('confidence','medium'),x.get('readers','')+('; '+x['decision'] if x.get('decision') else '')] for x in rows]) if rows else 'No reading differences from either witness.\n']
    changes+=['### C doubt decisions\n',table(['Place','C doubt','Final','Status','Evidence'],[[x['location'],x.get('c'),x['reading'],x['status'],ink_evidence(x)] for x in d.get('c_doubts',[])])]
    if d.get('witness_reviews'):
        changes+=['### Witness comments and sweep decisions\n','These reviews are separate from counted differences in the transcribed text.\n',table(['Witness / reference','Draft claim','Decision','Ink evidence'],[[x['reference'],x['claim'],x['decision'],ink_evidence(x,'evidence')] for x in d['witness_reviews']])]
    changes+=['### Reader disagreements and adjudication\n',table(['Place','R1','R2','R3','Decision','Ink evidence'],[[x['location'],x.get('r1'),x.get('r2'),x.get('r3'),x['final'],x['evidence']] for x in d.get('disputes',[])]) if d.get('disputes') else 'No additional reader disagreement beyond the readings recorded in the change table.\n']
    changes+=['### Remaining unresolved places\n',table(['Place','Reading','Alternatives','Confidence','Reason'],[[x['location'],x['reading'],x.get('alternatives',''),x.get('confidence','medium'),x.get('reason','')] for x in d.get('remaining_doubts',[])]) if d.get('remaining_doubts') else 'None.\n']
    for x in rows:
        if x.get('change_h'):collation.append([d['folder'],d['their_page'],d['scan'],x['location'],x.get('h',''),x.get('c',''),x['reading'],ink_evidence(x),x.get('kind','other'),x.get('marked_in_h','no'),x.get('confidence','medium')])
    for x in d.get('inventory',[]):inventory.append([key,x.get('sheet_kind','text'),x.get('hand','his hand'),x['element'],x['kind'],x['position'],x['first_words_or_objects'],x.get('transcribed','yes')])
    for x in d.get('remaining_doubts',[]):doubts.append([key,x['location'],x['reading'],x.get('alternatives',''),x.get('confidence','medium'),x.get('reason','')])
    for x in d.get('abbreviations',[]):abbrev[x['form']]=x['expansion']
    n=d.get('notes',{})
    notes+=['## '+key+'\n']
    sections=[('summary','What the page records'),('math_reading_decisions','Mathematics and reading decisions'),('author_checks','His checks, doubts and slips')]
    if n.get('local_doubts'):sections.append(('local_doubts','Local reading limits'))
    sections.append(('title_dates_pagination','Titles, dates and pagination'))
    for f,title in sections:
        value=n.get(f,'None.')
        if isinstance(value,list):value='\n'.join('- '+(v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)) for v in value) or 'None.'
        notes+=['### '+title+'\n',str(value),'']
    for x in d.get('check_events',[]):checks.append([x['statement_id'],x['date'],x['who'],x['type'],x['outcome']])
    wfrows.append([key,d.get('brief_version',''),d.get('reader_crop_counts',''),d.get('adjudicator_crop_count',0),d.get('workflow_note','')])
changes='\n'.join(changes)+'\n'
(OUT/(ID+'_changes.md')).write_text(changes)
def write_csv(name,headers,rows,delim=','):
    with (OUT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter=delim);w.writerow(headers);w.writerows(rows)
write_csv(ID+'_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation,'\t')
write_csv(ID+'_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory)
write_csv('CHECK_EVENTS.tsv',['statement_id','date','who (model, effort, run)','type','outcome'],checks,'\t')
(OUT/(ID+'_notes.md')).write_text('\n'.join(notes)+'\n')
leg=(OUT/'legibility.md').read_text() if (OUT/'legibility.md').exists() else 'Work in progress; page-specific uncertainties are recorded above.'
(OUT/(ID+'_doubts.md')).write_text((OUT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations (expansions only here)\n\n'+table(['Written form','Probable expansion'],sorted(abbrev.items()))+'\n## Legibility and witnesses\n\n'+leg+'\n')
workflow.append(table(['Cote / scan','Brief','Reader crop counts','Adjudicator crops created','Workflow observations'],wfrows))
if (OUT/'brief_changes.md').exists():workflow.append((OUT/'brief_changes.md').read_text())
workflow.append('\n## Exact initial and final briefs\n\n')
briefs=sorted((OUT/'briefs').glob('brief_v*.md'))
if briefs:
    workflow.append('### Initial brief\n\n'+briefs[0].read_text())
    if len(briefs)>1:workflow.append('### Last-used brief\n\n'+briefs[-1].read_text())
(OUT/(ID+'_workflow.md')).write_text('\n'.join(workflow)+'\n')
parts=[];cote=None
for d in decisions:
    if d['cote']!=cote:
        cote=d['cote'];parts.append('\\cotefile{'+cote+'}\n')
    t=(OUT/'pages'/d['filename']).read_text()
    t=re.sub(r'\\cotefile\{[^}]+\}\s*','',t)
    parts.append(t.rstrip()+'\n')
(OUT/(ID+'_transcription.tex')).write_text('\n'.join(parts))
print(json.dumps({'decided_pages':len(decisions),'changes_C':ct,'changes_H':ht,'confidence':dict(allconf),'remaining_doubts':len(doubts),'inventory_rows':len(inventory),'check_events':len(checks)}))
