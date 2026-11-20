"""Assemble the decided pages and their audit records without altering readings."""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,collections
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP51_CW_134-2'

def md(value):
    if isinstance(value,(list,dict)):value=json.dumps(value,ensure_ascii=False)
    return str(value if value is not None else '').replace('|','\\|').replace('\n','<br>')

def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(md(x) for x in r)+' |\n' for r in rows)

decisions=[]
for f in sorted((ROOT/'records').glob('scan*/decision.json')):
    d=json.loads(f.read_text());d['_file']=str(f.relative_to(ROOT));decisions.append(d)
pages=[];counts=[];witness_confidence=[];allcoll=[];allinv=[];events=[];consequential=[]
changes=['# Consolidated changes and witness collation\n\nCounts are distinct recorded places, not words or error-rate estimates. A place can differ from both witnesses. Confidence describes the final ink reading. Macro-equivalent renderings are excluded. Retained doubts and syntax-only adjustments are recorded separately.\n']
notes=['# Notes while reading\n\nThese notes describe only the supplied pages. No external text was consulted. A source statement reported here is not thereby proved; the check-event ledger distinguishes content carried as background from actual local checks.\n']
inventory_cols=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
coll_cols=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
doubts_rows=[];abbr={};workflow=[]
for d in decisions:
    n=d['scan']; f=ROOT/'pages'/d['filename'];pages.append(f.read_text().rstrip()+'\n')
    diffs=d.get('differences',[])
    cnt=collections.Counter(x['confidence'] for x in diffs)
    for witness in ['C','H']:
        wc=collections.Counter(x['confidence'] for x in diffs if x.get('differs_'+witness))
        witness_confidence.append([n,witness,sum(wc.values()),wc['high'],wc['medium'],wc['low']])
    counts.append([n,sum(bool(x.get('differs_C')) for x in diffs),sum(bool(x.get('differs_H')) for x in diffs),cnt['high'],cnt['medium'],cnt['low'],len(d.get('unresolved',[]))])
    changes.append(f'\n## Scan {n} — manuscript page {n-145}\n\n')
    changes.append(table(['Place','Witness C','Witness H','Consolidated reading','Ink evidence / crop','Confidence'],[[x['place'],x['C'],x['H'],x['final'],x['evidence']+((' Crop: `'+x['crop']+'`.') if x.get('crop') else ' Half: '+x.get('half','as identified in reader reports')+'.'),x['confidence']] for x in diffs]) if diffs else 'No substantive differences from either witness.\n')
    comparisons=d.get('reader_comparisons',[])
    if comparisons:
        changes.append('\n### Three-reader decisions\n\n'+table(['Place','Reader A','Reader B','Reader C','Final decision and ink'],[[x['place'],x['A'],x['B'],x['C'],x['decision']] for x in comparisons]))
    if d.get('doubt_review'):
        changes.append('\n### Witness C doubt review\n\n'+table(['Place','Earlier doubt','Decision','Grounds'],[[x['place'],x['earlier'],x['decision'],x['evidence']] for x in d['doubt_review']]))
    changes.append('\n### Still unresolved\n\n')
    if d.get('unresolved'):
        changes.append(table(['Place','Reading','Alternatives','Confidence','Reason'],[[x['place'],x['reading'],x.get('alternatives',''),x['confidence'],x['reason']] for x in d['unresolved']]))
    else:changes.append('None.\n')
    for x in diffs:
        if x.get('differs_H'):
            allcoll.append(dict(zip(coll_cols,[d['folder'],n-1,n,x['place'],x['H'],x['C'],x['final'],x['evidence']+(' Crop: '+x['crop'] if x.get('crop') else ''),x.get('kind','other'),x.get('marked_in_H','no'),x['confidence']])))
        if x.get('consequential'):consequential.append(f'- Scan {n}, {x["place"]}: {x["consequential"]}\n')
    for x in d.get('inventory',[]):allinv.append({'scan':n,**{k:x.get(k,'') for k in inventory_cols[1:]}})
    for x in d.get('unresolved',[]):doubts_rows.append([n,x['place'],x['reading'],x.get('alternatives',''),x['confidence'],x['reason']])
    for x in d.get('abbreviations',[]):
        if isinstance(x,dict):abbr.setdefault(x.get('written',x.get('form','')),x.get('expansion',x.get('meaning','')))
    notes.append(f'\n## Scan {n} — manuscript page {n-145}\n\n'+d.get('notes','')+'\n')
    if d.get('note_statements'):
        notes.append('\nCheck-event references: '+ '; '.join('**'+x['id']+'** ('+x['place']+')' for x in d['note_statements'])+'. These entries carry source statements as background and do not claim proofs.\n')
    events+=d.get('check_events',[])
    main_ledger=ROOT/f'records/scan{n}/main_viewed_crops.txt'
    main_views=main_ledger.read_text().splitlines() if main_ledger.exists() else []
    main_reused=sum('/main/' not in p for p in main_views)
    workflow.append([n,d.get('brief',''),*[d.get('crop_counts',{}).get(r,0) for r in ['A','B','C','main']],main_reused,len(main_views),d.get('workflow_note','')])
total=[sum(x[i] for x in counts) for i in range(1,7)]
changes.insert(1,'\n## Counts\n\n'+table(['Scan','Against C','Against H','High','Medium','Low','Unresolved places'],counts+[['TOTAL',*total]])+'\n## Consequential corrections\n\n'+(''.join(consequential) if consequential else 'No consequential correction recorded in the pages decided so far.\n'))
confidence_totals=[]
for witness in ['C','H']:
    selected=[row for row in witness_confidence if row[1]==witness]
    confidence_totals.append(['TOTAL',witness,*[sum(row[i] for row in selected) for i in range(2,6)]])
changes.insert(2,'\n### Confidence by witness\n\nThe High/Medium/Low columns in the preceding table count distinct recorded places. This table separates each witness’s differences.\n\n'+table(['Scan','Witness','Total','High','Medium','Low'],witness_confidence+confidence_totals))
(ROOT/f'{PREFIX}_transcription.tex').write_text(''.join(pages))
(ROOT/f'{PREFIX}_changes.md').write_text(''.join(changes))
(ROOT/f'{PREFIX}_notes.md').write_text(''.join(notes))
for name,cols,rows,delim in [(f'{PREFIX}_inventory.csv',inventory_cols,allinv,','),(f'{PREFIX}_collation.tsv',coll_cols,allcoll,'\t')]:
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols,delimiter=delim);w.writeheader();w.writerows(rows)
event_cols=['statement_id','date','who','type','outcome']
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_cols,delimiter='\t');w.writeheader()
    for e in events:w.writerow({k:e.get(k,'') for k in event_cols})
doubt='# Doubts, notation and abbreviations\n\n'+(ROOT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Grounds'],doubts_rows)+'\n## Abbreviations\n\nExpansions are interpretative and appear only here.\n\n'+table(['Written form','Possible expansion'],sorted(abbr.items()))
if (ROOT/'records/notation_review_final.md').exists():
    doubt=doubt.replace('\n## Remaining doubts\n', '\n'+(ROOT/'records/notation_review_final.md').read_text()+'\n## Remaining doubts\n',1)
if (ROOT/'records/legibility.md').exists():doubt+='\n## Legibility and witnesses\n\n'+(ROOT/'records/legibility.md').read_text()
(ROOT/f'{PREFIX}_doubts.md').write_text(doubt)
workflow_text='# Workflow record\n\nEach scan was assigned, in order, to three fresh agents with `fork_turns="none"`. Each agent read the whole page once and the two supplied halves once, then made targeted crops where needed. The main reader retained their written returns and adjudication crops. No OCR, PDF text layer, external edition or web research was used. Original sources remain outside this deliverable. Saved crops document specific decisions.\n\nMain new crops count saved main-reader images; reused crops are existing reader images successfully inspected by main. Failed displays are described in each workflow observation and are not counted as successful inspections.\n\n## Per-page records\n\n'+table(['Scan','Brief','Reader A crops','Reader B crops','Reader C crops','Main new crops','Main reused crops','Main successful crop inspections','Workflow observation'],workflow)
if (ROOT/'records/brief_changes.md').exists():workflow_text+='\n## Brief changes and lessons\n\n'+(ROOT/'records/brief_changes.md').read_text()
if (ROOT/'records/C_question_coverage.tsv').exists():workflow_text+='\n## Earlier-question coverage\n\n`records/C_question_coverage.tsv` maps every supplied C question row to its completed disposition and decision-record fields. Repeated questions and the broader structural questions grouped in the early reviews remain individually indexed. This is a text-only cross-reference to the completed readings; it adds no image inspection, mathematical check, or witness-change count.\n'
if (ROOT/'records/environment_recovery_20261120.md').exists():workflow_text+='\n## Environment recovery\n\n'+(ROOT/'records/environment_recovery_20261120.md').read_text()
if (ROOT/'records/final_review.md').exists():workflow_text+='\n## Final review and validation\n\n'+(ROOT/'records/final_review.md').read_text()
briefs=sorted((ROOT/'briefs').glob('brief_*.md'))
if briefs:
    workflow_text+='\n## First brief\n\n'+briefs[0].read_text()
    workflow_text+='\n## Last-used brief\n\n'+briefs[-1].read_text()
(ROOT/f'{PREFIX}_workflow.md').write_text(workflow_text)
print(json.dumps({'decided_pages':len(decisions),'C_changes':total[0],'H_changes':total[1],'unresolved':total[5],'inventory_rows':len(allinv),'check_events':len(events)}))
