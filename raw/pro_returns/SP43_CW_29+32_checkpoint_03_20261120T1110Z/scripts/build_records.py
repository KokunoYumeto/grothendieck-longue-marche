"""Build public records from adjudicated page JSON; never infer an ink reading."""
from pathlib import Path
import csv,json,hashlib,re
from datetime import datetime,timezone

OUT=Path(__file__).resolve().parents[1]
STEM='SP43_CW_29+32'

def esc(v):
    if v is None: return '—'
    if isinstance(v,(dict,list)): v=json.dumps(v,ensure_ascii=False)
    return str(v).replace('|','&#124;').replace('\n','<br>')

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(esc(v) for v in row)+' |' for row in rows])+'\n'

def doubt_reason(x):
    reason=x.get('evidence') or x.get('reason') or x.get('note') or x.get('limitation') or ''
    source=x.get('source','')
    return reason+('; ' if reason and source else '')+source

def records():
    return sorted([json.loads(p.read_text()) for p in (OUT/'decisions').glob('*.json')],key=lambda x:x['order'])

def main():
    pages=records()
    combined='\n\n'.join((OUT/'pages'/p['filename']).read_text().rstrip() for p in pages)+'\n'
    (OUT/(STEM+'_transcription.tex')).write_text(combined)
    changes=['# Consolidated changes and decisions','',
             'The scans supplied with the task are the primary evidence. C and H are independent draft witnesses. Counts are local decision places, not edit distances or error rates. A place may contain adjacent changes belonging to one correction. Pure macro-syntax differences are excluded. H has no text for cote 29 scans 134 and 136; these pages are compared with C alone.','',
             '## Counts','']
    counts=[]
    totals=[0,0,0,0,0]
    for p in pages:
        ds=p['differences']
        vals=[sum(bool(d.get('diff_C')) for d in ds),sum(bool(d.get('diff_H')) for d in ds)]
        vals += [sum(d.get('confidence')==c and (d.get('diff_C') or d.get('diff_H')) for d in ds) for c in ['high','medium','low']]
        counts.append([p['scan']]+vals)
        totals=[a+b for a,b in zip(totals,vals)]
    changes.append(table(['Cote/scan','Against C','Against H','High confidence places','Medium','Low'],counts+[['TOTAL']+totals]))
    confidence_rows=[]
    confidence_totals=[0]*6
    for page in pages:
        values=[sum(bool(d.get('diff_'+witness)) and d.get('confidence')==level for d in page['differences']) for witness in ['C','H'] for level in ['high','medium','low']]
        confidence_rows.append([page['scan']]+values)
        confidence_totals=[a+b for a,b in zip(confidence_totals,values)]
    changes+=['### Confidence by witness','',table(['Cote/scan','C high','C medium','C low','H high','H medium','H low'],confidence_rows+[['TOTAL']+confidence_totals])]
    changes+=['## Consequential corrections','']
    consequential=[f"- {p['scan']}, {d['place']}: {d.get('consequence',d['reading'])}" for p in pages for d in p['differences'] if d.get('mathematical') and (d.get('diff_C') or d.get('diff_H'))]
    changes.extend(consequential or ['None recorded so far.'])
    coll=[]
    inv=[]
    doubts=[(OUT/'notation.md').read_text(),'\n# Doubts and retained slips\n']
    notes=['# Notes while reading','',
           'Source scope: only the supplied scans and draft witnesses. A statement attributed to a page is reported as that page’s statement; this is not certification of its mathematical truth. Actual mathematical check events, where performed, are separately recorded in CHECK_EVENTS.tsv. Scan references identify the archival evidence; no external literature was consulted.','']
    workflow=['# Reading workflow','',
              'Each page was assigned in archive order to three new independent agents, with that page’s source images, the two witness excerpts (H absent where recorded), C’s prior questions, the conventions, the current brief, and the notation table snapshot. Inputs were intended to be page-local; the prior-note scope errors on 29/102 and 29/113 are disclosed in the page notes and input_scope_incidents.md. Readers were instructed not to inspect one another’s work. The main reader waited for all final returns, compared them, and adjudicated differing places on saved or newly made crops; the preliminary-return exception on 29/039 is disclosed below. Candidate readings remain in readers/; only pages/ is the consolidated transcription.','',
              '## Page runs and crop counts','']
    runrows=[]
    events=json.loads((OUT/'additional_check_events.json').read_text()) if (OUT/'additional_check_events.json').exists() else []
    for p in pages:
        scan=p['scan']
        changes += [f'\n## {scan}\n',table(['Place','C','H','Consolidated reading','Scan evidence and crop','Confidence','Three reader readings'],[[d['place'],d.get('C'),d.get('H'),d['reading'],d['evidence']+'; '+d.get('source',''),d['confidence'],d.get('readers',{})] for d in p['differences']])]
        if p.get('c_doubts'):
            changes+=['### Disposition of C’s doubt marks\n',table(['Place','C','Final','Status','Evidence'],[[d['place'],d['C'],d['reading'],d['status'],d['evidence']+'; '+d.get('source','')] for d in p['c_doubts']])]
        changes+=['### Still unresolved\n']
        u=p.get('unresolved',[])
        changes += [table(['Place','Reading / alternatives','Confidence','Reason'],[[x.get('place',''),x.get('reading',x.get('C','')),x.get('confidence','medium'),doubt_reason(x)] for x in u]) if u else 'None.\n']
        for d in p['differences']:
            if d.get('diff_H'):
                coll.append([p['folder'],p['their_page'],p['our_scan'],d['place'],d.get('H',''),d.get('C',''),d['reading'],d['evidence']+'; '+d.get('source',''),d['kind'],d.get('marked_in_H','no'),d['confidence']])
        inv.extend(p['inventory'])
        doubts += [f'\n## {scan}\n']
        doubts += [table(['Place','Reading / alternatives','Confidence','Ink and contextual distinction'],[[x.get('place',''),x.get('reading',x.get('C','')),x.get('confidence','medium'),doubt_reason(x)] for x in u]) if u else 'No unresolved reading recorded.\n']
        if p.get('slips'): doubts += ['### Slips retained as written\n']+[f'- {x}' for x in p['slips']]
        notes += [f'## {scan}\n',p.get('notes',''), '']
        counts_by_reader=[]
        for rid in ['r1','r2','r3']:
            rp=OUT/'readers'/p['stem']/rid/'report.json'
            if rp.exists():
                rr=json.loads(rp.read_text())
                counts_by_reader.append(len(rr.get('crops',[])))
            else: counts_by_reader.append('missing')
        runrows.append([scan,p.get('brief',''),*counts_by_reader,len(p.get('main_crops',[])),p.get('agents',{})])
        events.extend(p.get('checks',[]))
    doubts += ['\n# Abbreviations\n', 'Abbreviations are preserved in the transcription. Expansions below are explanatory only.\n']
    abbr=[]
    for p in pages:
        abbr.extend(p.get('abbreviations',[]))
    doubts+= [table(['Form','Possible expansion','Evidence'],[[a['form'],a['expansion'],a['evidence']] for a in abbr]) if abbr else 'None recorded so far.']
    doubts+=['\n# Legibility and witness comparison\n', 'The pages include faint typescript, overtyping, handwritten mathematics, crowded corrections and clipped edges. Surviving low or medium confidence places are listed by scan above. The differences tables provide local evidence for comparing the drafts; counts are not estimates of either witness’s error rate.']
    if (OUT/'legibility_observations.md').exists(): doubts.append((OUT/'legibility_observations.md').read_text())
    workflow += [table(['Cote/scan','Brief','R1 crops','R2 crops','R3 crops','Main-reader new crops','Agent runs'],runrows)]
    workflow += ['## Brief history\n',(OUT/'briefs/history.md').read_text() if (OUT/'briefs/history.md').exists() else 'v01 first used on cote 29 scan 036.\n']
    briefs=sorted((OUT/'briefs').glob('brief_v*.md'))
    if briefs:
        workflow+=['## First brief (verbatim)\n',briefs[0].read_text(),'## Last brief (verbatim)\n',briefs[-1].read_text()]
    if (OUT/'workflow_observations.md').exists(): workflow+=['## Observations\n',(OUT/'workflow_observations.md').read_text()]
    for suffix,data in [('changes.md',changes),('doubts.md',doubts),('notes.md',notes),('workflow.md',workflow)]:
        (OUT/(STEM+'_'+suffix)).write_text('\n'.join(data)+'\n')
    with (OUT/(STEM+'_collation.tsv')).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
    with (OUT/(STEM+'_inventory.csv')).open('w',newline='') as f:
        fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(inv)
    with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        fields=['statement_id','date','who','type','outcome'];w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(events)
    print(json.dumps({'decided_pages':len(pages),'C_changes':totals[0],'H_changes':totals[1],'inventory_elements':len(inv),'check_events':len(events)},ensure_ascii=False))

if __name__=='__main__':main()
