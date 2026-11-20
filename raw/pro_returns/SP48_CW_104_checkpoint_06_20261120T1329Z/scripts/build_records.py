"""Build deliverables from page decisions; never infers manuscript readings."""
from pathlib import Path
from collections import Counter
import json, csv, io, re

OUT=Path(__file__).resolve().parents[1]
PREFIX='SP48_CW_104'
def esc(value):
    return str(value).replace('|','&#124;').replace('\n','<br>')
def code(value):
    return '<code>'+esc(value).replace('&','&amp;').replace('<br>','</code><br><code>').replace('&#124;','&#124;')+'</code>'
def cell(value):
    return str(value).replace('\t',' ').replace('\n',' ')

def build():
    decisions=[json.loads(p.read_text()) for p in sorted((OUT/'records').glob('scan*/decision.json'))]
    totals=Counter(); counts=[]; consequences=[]
    for d in decisions:
        count=Counter()
        for x in d.get('issues',[]):
            if x.get('diff_C'): count['C']+=1; count['C_'+x['confidence']]+=1
            if x.get('diff_H'): count['H']+=1; count['H_'+x['confidence']]+=1
            if x.get('diff_C') or x.get('diff_H'): count[x['confidence']]+=1
            if x.get('consequential'): consequences.append(f"- Scan {d['scan']:03d}, {x['location']}: {x['consequential']}")
        totals.update(count); counts.append((d['scan'],count))
    changes=[f'# {PREFIX}: changes and adjudications','',
      'A place is counted once against each witness it differs from. Confidence counts are unique changed places, so their sum need not equal C + H. Removing or refining an in-place doubt counts as a change against C; equivalent macro syntax does not. Each reader is identified A, B, or C; witness C is always labelled “witness C”. All observations refer to the supplied scans, without outside research.','',
      '| Scan | C total | C high | C medium | C low | H total | H high | H medium | H low | Unique high | Unique medium | Unique low |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    changes += [f"| {n:03d} | {c['C']} | {c['C_high']} | {c['C_medium']} | {c['C_low']} | {c['H']} | {c['H_high']} | {c['H_medium']} | {c['H_low']} | {c['high']} | {c['medium']} | {c['low']} |" for n,c in counts]
    changes += [f"| **Total** | **{totals['C']}** | {totals['C_high']} | {totals['C_medium']} | {totals['C_low']} | **{totals['H']}** | {totals['H_high']} | {totals['H_medium']} | {totals['H_low']} | **{totals['high']}** | **{totals['medium']}** | **{totals['low']}** |",'', '## Consequential corrections','']
    changes += consequences or ['None yet recorded.']
    collation=[]; inventory=[]; remaining=[]; notes=[f'# {PREFIX}: notes while reading','',
      'These notes concern only the supplied pages. A statement being transcribed is not thereby proved. Actual checks and limited background uses are identified in CHECK_EVENTS.tsv.','']
    for d in decisions:
        n=d['scan']; folder=d['folder']
        changes += ['',f'## Scan {n:03d} — H page {n-1}','',
          '| Place | Witness C | Witness H | Consolidated reading | Ink and adjudication | Confidence |',
          '|---|---|---|---|---|---|']
        for x in d.get('issues',[]):
            if not (x.get('diff_C') or x.get('diff_H')): continue
            evidence=x['evidence']
            if x.get('crop'): evidence+=' Crop: `'+x['crop']+'`.'
            if x.get('readers'): evidence+=' Readers: '+'; '.join(f"{k}: {v}" for k,v in x['readers'].items())+'.'
            changes.append('| '+' | '.join(esc(x.get(k,'')) for k in ['location','C','H','final'])+' | '+esc(evidence)+' | '+x['confidence']+' |')
            if x.get('diff_H'):
                collation.append([folder,n-1,n,x['location'],x['H'],x['C'],x['final'],evidence,x['kind'],x.get('marked_in_H','no'),x['confidence']])
        others=[x for x in d.get('issues',[]) if not (x.get('diff_C') or x.get('diff_H'))]
        if others:
            changes += ['','### Retained C doubts and unchanged adjudications','',
              '| Place | Retained reading | Readers and scan evidence | Confidence |','|---|---|---|---|']
            for x in others:
                e=x['evidence']
                if x.get('crop'): e+=' Crop: `'+x['crop']+'`.'
                if x.get('readers'): e+=' Readers: '+'; '.join(f'{k}: {v}' for k,v in x['readers'].items())+'.'
                changes.append('| '+' | '.join(map(esc,[x['location'],x['final'],e,x['confidence']]))+' |')
        doubts=d.get('remaining',[])
        changes += ['','### Still unresolved','']
        if doubts:
            changes += [f"- {r['location']}: {r['reading']}; alternatives: {r.get('alternatives','none separately identified')}. {r.get('reason','')}" for r in doubts]
            remaining += [[n,r['location'],r['reading'],r.get('alternatives',''),r['confidence'],r.get('reason','')] for r in doubts]
        else: changes += ['None.']
        for inv in d.get('inventory',[]):
            inventory.append([n]+[inv.get(k,'') for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']])
        notes += [f'## Scan {n:03d}','']
        for para in d.get('notes',[]): notes += [para,'']
    (OUT/f'{PREFIX}_changes.md').write_text('\n'.join(changes)+'\n')
    with (OUT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t'); w.writerow('folder their_page our_scan line their_reading codex_reading final_reading scan_shows kind marked_in_H confidence'.split()); w.writerows([[cell(v) for v in row] for row in collation])
    with (OUT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow('scan sheet_kind hand element kind position first_words_or_objects transcribed'.split());w.writerows(inventory)
    (OUT/f'{PREFIX}_notes.md').write_text('\n'.join(notes)+'\n')
    doubts=[(OUT/'notation.md').read_text(), '\n## Remaining doubts\n',
      '| Scan | Place | Reading | Alternatives | Confidence | Reason |','|---|---|---|---|---|---|']
    doubts += ['| '+' | '.join(map(esc,row))+' |' for row in remaining]
    if not remaining: doubts += ['No decided page currently carries an unresolved doubt.']
    for extra in ['abbreviations.md','legibility.md']:
        p=OUT/extra
        if p.exists(): doubts += ['',p.read_text()]
    (OUT/f'{PREFIX}_doubts.md').write_text('\n'.join(doubts)+'\n')
    checks=[]
    for d in decisions:
        checks.extend(d.get('checks',[]))
    with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
        for c in checks: w.writerow([cell(c.get(k,'')) for k in ['statement_id','date','who','type','outcome']])
    pages=sorted((OUT/'pages').glob('*.tex'))
    (OUT/f'{PREFIX}_transcription.tex').write_text('\n\n'.join(p.read_text().rstrip() for p in pages)+'\n')
    versions=sorted((OUT/'briefs').glob('brief_v*.md'))
    wf=[f'# {PREFIX}: workflow record','',
      'For every completed scan listed below, three fresh subagents were assigned in numerical page order. They received only that page’s packet, image paths, conventions and the running notation snapshot. Reader outputs were kept in separate directories. The main reader compared all three returns and viewed decision crops before recording each completed page. Source archives were unpacked once; no OCR, PDF text layer or external research was used.','',
      '## Brief revision history','']
    ev=OUT/'workflow_events.md'
    if ev.exists(): wf += [ev.read_text()]
    wf += ['','## Crop counts','', '| Scan | Reader A | Reader B | Reader C | Main reader new crops |','|---|---:|---:|---:|---:|']
    for d in decisions:
        counts=d.get('crop_counts',{})
        wf.append('| '+' | '.join(str(x) for x in [d['scan'],counts.get('A',0),counts.get('B',0),counts.get('C',0),counts.get('main',0)])+' |')
    if versions:
        wf+=['','## First brief','',versions[0].read_text(),'','## Last brief','',versions[-1].read_text()]
    p=OUT/'workflow_assessment.md'
    if p.exists():wf+=['','## Assessment','',p.read_text()]
    (OUT/f'{PREFIX}_workflow.md').write_text('\n'.join(wf)+'\n')
    return {'pages':len(decisions),'changes_C':totals['C'],'changes_H':totals['H'],'remaining_doubts':len(remaining),'inventory':len(inventory)}

if __name__=='__main__': print(json.dumps(build(),ensure_ascii=False))
