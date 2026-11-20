"""Build delivery tables from main-reader decisions, without altering transcription."""
from pathlib import Path
import csv,json,collections,re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP40_CW_81'
def esc(x):
    if x is None:return '—'
    if isinstance(x,(dict,list)):x=json.dumps(x,ensure_ascii=False)
    return str(x).replace('|','\\|').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(esc(x) for x in row)+' |\n' for row in rows)
def write_csv(name,fields,rows,delimiter=','):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
decisions=[(r,d) for r in records for d in r['decisions']]
changes=['# SP40_CW_81 — consolidated reading decisions\n',
    'Every reading rests on the supplied scan. Three independent proposed readings are retained under `readers/`; main-reader decisions are retained under `records/`. Rows resolving or retaining a C doubt are included even when the final reading has no textual change. Counts refer to decision loci, not changed tokens; macro syntax alone is excluded. H has no collation rows on scans with no transcribed text.\n',
    '## Counts\n']
countrows=[];tot=collections.Counter()
for r in records:
    cs=collections.Counter()
    for d in r['decisions']:
        cs['C']+=bool(d.get('diff_C'));cs['H']+=bool(d.get('diff_H'))
        for witness in ('C','H'):
            if d.get('diff_'+witness):cs[witness+'_'+d['confidence']]+=1
        if d.get('diff_C') or d.get('diff_H'):cs[d['confidence']]+=1
    tot.update(cs);countrows.append([f"{r['scan']:03d}",cs['C'],cs['C_high'],cs['C_medium'],cs['C_low'],cs['H'],cs['H_high'],cs['H_medium'],cs['H_low'],len(r.get('doubts',[]))])
countrows.append(['Total',tot['C'],tot['C_high'],tot['C_medium'],tot['C_low'],tot['H'],tot['H_high'],tot['H_medium'],tot['H_low'],sum(len(r.get('doubts',[])) for r in records)])
changes.append(table(['Scan','Against C','C high','C medium','C low','Against H','H high','H medium','H low','Remaining doubt loci'],countrows))
changes.append('\n## Consequential corrections\n')
con=[f"- Scan {r['scan']:03d}, {d['location']}: {d['mathematical_consequence']}" for r,d in decisions if d.get('mathematical_consequence') and (d.get('diff_C') or d.get('diff_H'))]
changes.append('\n'.join(con) if con else 'None recorded on the pages decided so far.')
collation=[];inventory=[];doubts=[];notes=['# SP40_CW_81 — notes while reading\n\nThese notes report only the supplied pages. Reading and collating a mathematical statement does not certify its proof. Actual checks are distinguished in CHECK_EVENTS.tsv.\n'];events=[]
for r in records:
    n=r['scan'];changes.append(f'\n## Scan {n:03d}\n')
    dr=[]
    for d in r['decisions']:
        readers=d.get('readers',{})
        readertext='; '.join(f'{k}: {v}' for k,v in readers.items()) if isinstance(readers,dict) else str(readers)
        evidence=d.get('evidence','')
        if d.get('qualification'):evidence+=' '+d['qualification']
        if d.get('crop'):evidence+=' Image: '+str(d['crop'])+'.'
        if d.get('C_doubt_status'):evidence+=' C doubt: '+d['C_doubt_status']+'.'
        if d.get('S_id'):evidence+=' Witness S '+d['S_id']+': '+d.get('S_status','reviewed')+'.'
        if d.get('diff_C') or d.get('diff_H') or d.get('C_doubt_status') or d.get('S_id') or d.get('log_decision'):
            dr.append([d['id'],d['location'],d.get('C'),d.get('H'),d['final'],readertext,evidence,d['confidence']])
        if d.get('diff_H') and r['hua_has']=='text':
            collation.append({'folder':r['folder'],'their_page':r['their_page'],'our_scan':n,'line':d['location'],'their_reading':d.get('H',''),'codex_reading':d.get('C',''),'final_reading':d['final'],'scan_shows':evidence,'kind':d['kind'],'marked_in_H':d.get('marked_in_H','no'),'confidence':d['confidence']})
    changes.append(table(['ID','Place','Witness C','Witness H','Final','Three readings','What the scan shows / decision','Confidence'],dr) if dr else 'No reading differences found.\n')
    changes.append('\n### Still unresolved\n')
    rd=r.get('doubts',[])
    changes.append(table(['Place','Reading','Alternatives','Confidence','Reason'],[[d['location'],d['reading'],d.get('alternatives','—'),d['confidence'],d.get('reason','')] for d in rd]) if rd else 'None.\n')
    for d in rd:doubts.append([f'{n:03d}',d['location'],d['reading'],d.get('alternatives','—'),d['confidence'],d.get('reason','')])
    for i in r.get('inventory',[]):inventory.append({'scan':n,**i})
    notes.append(f'\n## Scan {n:03d}\n\n'+r.get('notes','')+'\n')
    for e in r.get('check_events',[]):events.append(e)
(ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(changes)+'\n')
write_csv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation,'\t')
write_csv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory)
write_csv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events,'\t')
(ROOT/f'{PREFIX}_notes.md').write_text('\n'.join(notes))
abbr=[]
for r in records:
    for a in r.get('abbreviations',[]):abbr.append([r['scan'],a['form'],a['expansion']])
leg=(ROOT/'legibility_note.md').read_text() if (ROOT/'legibility_note.md').exists() else 'Assessment in progress; the record currently covers only the scans listed above.'
notation=(ROOT/'notation.md').read_text()
# Escape alternative separators for Markdown tables, retaining raw reader notation separately.
notation=re.sub(r'(?<!`)`([^`\n]+)`(?!`)',lambda m:'`'+re.sub(r'(?<!\\)\|',r'\\|',m.group(1))+'`',notation)
notation=re.sub(r'\|\n(?:[ \t]*\n)+(?=\|)', '|\n', notation)
(ROOT/f'{PREFIX}_doubts.md').write_text(notation+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions appear only in this list.\n\n'+table(['Scan','As written','Probable expansion'],abbr)+'\n## Legibility and witnesses\n\n'+leg+'\n')
(ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join((ROOT/'pages'/r['filename']).read_text().rstrip()+'\n' for r in records))
workflow=['# SP40_CW_81 — reading workflow\n',
    'Scans are processed in the page-map order. Each scan has three fresh readers (A, B, C-reader), started without conversation history and restricted to that scan, its two witnesses, conventions, and the current notation snapshot. C-reader is a role name; witness C is the prior Codex transcription. Each reader views the whole image once and each supplied half once, then crops unresolved loci. The main reader compares returns and views crops for adjudication. No OCR or external research is used. Root retains returns and adjudication crops. Reader directories preserve the independent page proposals, evidence, and crop metadata.\n',
    '## Model and effort\n\nMain reader and subreaders: GPT-6 Astra Pro / inherited model configuration. The runtime does not expose a separately verifiable numerical reasoning-effort setting; none is invented in this record.\n',
    '## Per-page record\n']
wrows=[]
for r in records:
    counts={}
    for role in ['A','B','C']:
        path=ROOT/'readers'/f"{r['scan']:03d}"/role/'report.json'
        if path.exists():counts[role]=len(json.loads(path.read_text()).get('crops',[]))
    rootc=len(list((ROOT/'crops'/f"{r['scan']:03d}").glob('*.png')))
    wrows.append([r['scan'],r.get('brief_version','v01'),counts.get('A','?'),counts.get('B','?'),counts.get('C','?'),rootc,r.get('workflow_note','')])
workflow.append(table(['Scan','Brief','A crops','B crops','C-reader crops','Main new crops','Observations'],wrows))
workflow.append('\n## Brief versions\n')
for p in sorted((ROOT/'briefs').glob('brief*.md')):workflow.append(f'\n### {p.name}\n\n'+p.read_text())
if (ROOT/'workflow_assessment.md').exists():workflow.append('\n## Assessment\n\n'+(ROOT/'workflow_assessment.md').read_text())
(ROOT/f'{PREFIX}_workflow.md').write_text('\n'.join(workflow)+'\n')
print(json.dumps({'decided_scans':[r['scan'] for r in records],'C_loci':tot['C'],'H_loci':tot['H'],'inventory_rows':len(inventory),'doubt_loci':len(doubts)},ensure_ascii=False))
