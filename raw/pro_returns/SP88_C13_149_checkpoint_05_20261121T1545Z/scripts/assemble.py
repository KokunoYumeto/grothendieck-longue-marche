from pathlib import Path
import csv,json,re,collections,datetime,hashlib
ROOT=Path(__file__).resolve().parents[1]; ACCEPTED=ROOT/'review/accepted'
SCANS=[103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129]
def esc(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(esc(c) for c in row)+' |\n' for row in rows)
def write_tsv(name,headers,rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(headers);w.writerows(rows)
def cropstr(r):
    p=r.get('crop','page');b=r.get('bbox',[])
    return p+((' '+str(tuple(b))) if p!='page' and b else '')
def main():
    data=[json.loads(p.read_text()) for p in ACCEPTED.glob('*.json')];data.sort(key=lambda d:d['scan'])
    changes=[(d,r) for d in data for r in d['changes'] if r.get('vs_C') or r.get('vs_H')]
    counts=[]
    for d in data:
        rows=[r for r in d['changes'] if r.get('vs_C') or r.get('vs_H')]
        counts.append([d['scan'],len(rows),sum(bool(r.get('vs_C')) for r in rows),sum(bool(r.get('vs_H')) for r in rows),*[sum(r['confidence']==c for r in rows) for c in ['high','medium','low']]])
    if counts:counts.append(['TOTAL',*[sum(r[i] for r in counts) for i in range(1,7)]])
    log='# SP88_C13_149 — changes against the two draft witnesses\n\n'
    log+=f'Adjudicated pages: {len(data)} of {len(SCANS)}. Counts are distinct logged places; a place can differ from both witnesses. Macro-only rendering differences and new doubt without a changed base reading are excluded.\n\n'
    log+=table(['Scan','Places','Against C','Against H','High','Medium','Low'],counts)
    log+='\n## Consequential corrections\n\n'
    significant=[f"- Scan {d['scan']}, {r['place']}: `{r['C']}` (C), `{r['H']}` (H) → `{r['final']}`. {r.get('consequence',r['evidence'])}" for d,r in changes if r.get('consequential')]
    log+='\n'.join(significant) if significant else 'No correction designated consequential yet.'
    coll=[];decisions=[];inventory=[];doubts=[];notes=[];checks=[];hands=[];notations=[];abbreviations=[]
    for d in data:
        n=d['scan'];log+=f'\n\n## Scan {n}\n\n'
        log+=table(['Place','Witness C','Witness H','Consolidated reading','What the scan shows; image evidence','Confidence'],[[r['place'],r['C'],r['H'],r['final'],r['evidence']+' — '+cropstr(r)+((' — Audit: '+r['audit']) if r.get('audit') else ''),r['confidence']] for r in d['changes'] if r.get('vs_C') or r.get('vs_H')])
        log+='\nUnresolved: '+('; '.join(f"{r['place']}: {r['reading']}" for r in d.get('doubts',[])) or 'none recorded')+'.\n'
        uncertain_comparisons=[r for r in d['changes'] if not (r.get('vs_C') or r.get('vs_H'))]
        if uncertain_comparisons:
            log+='\n### Unresolved comparisons and certainty changes\n\n'
            log+='These records preserve the witnesses and the inspected ink without declaring either witness wrong. They are excluded from the correction counts above.\n\n'
            log+=table(['Place','Witness C','Witness H','Current reading','Ink evidence','Confidence'],[[r['place'],r['C'],r['H'],r['final'],r['evidence']+' — '+cropstr(r),r['confidence']] for r in uncertain_comparisons])
        resolved=[r for r in d['decisions'] if r['decision']!='undecided']
        if resolved:
            log+='\n### Resolved supplied doubt marks\n\n'
            log+='These decisions document the deciding strokes even where the first reading of C was confirmed. Confirmation or removal of a doubt alone does not add a witness-error count.\n\n'
            log+=table(['Mark','Decision','Reading','Deciding ink and crop','Confidence'],[[r['id'],r['decision'],r['reading'],r['evidence']+' — '+cropstr(r),r['confidence']] for r in resolved])
        if d.get('audit_changes'):
            log+='\n### Changes after the independent second reading\n\n'
            log+='These rows preserve both frozen readings and the adjudicated result. They are not additional witness-error counts when the same place is already listed above.\n\n'
            log+=table(['Box / place','Frozen first reading','Independent second reading','Adjudicated reading','Ink evidence','Confidence'],[[r.get('box',r.get('place','')),r['first'],r['second'],r['final'],r['evidence']+' — '+cropstr(r),r['confidence']] for r in d['audit_changes']])
        for r in d['changes']:
            if r.get('vs_H'):coll.append(['149',n-1,n,r['place'],r['H'],r['C'],r['final'],r['evidence']+' — '+cropstr(r),r['kind'],'yes' if r.get('H_marked') else 'no',r['confidence']])
        for r in d['decisions']:decisions.append([r['id'],'149',n,r['decision'],r['reading'],r['evidence'],cropstr(r),r['confidence']])
        for r in d['inventory']:inventory.append([n,*[r[k] for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']]])
        for r in d.get('doubts',[]):doubts.append([n,r['place'],r['reading'],r.get('alternatives',''),r['confidence']])
        notes.append(f"## Scan {n}\n\n"+'\n\n'.join(d.get('notes',[])))
        for r in d.get('checks',[]):checks.append([r['statement_id'],r.get('date',datetime.datetime.now(datetime.timezone.utc).date().isoformat()),r.get('who','GPT-6 Astra Pro; effort not exposed by runtime; SP88_C13_149 / '+d['reader']),r['type'],r['outcome']])
        for r in d.get('hand_observations',[]):hands.append([n,r['habit'],r['places'],r['holds'],r['witness_errors']])
        for r in d.get('notation',[]):notations.append([r['written'],r['meaning_or_use'],f'Scan {n}: '+r.get('places',str(n))])
        for r in d.get('abbreviations',[]):abbreviations.append([n,r['written'],r['expansion']])
    (ROOT/'SP88_C13_149_changes.md').write_text(log+'\n')
    write_tsv('SP88_C13_149_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    decisions.sort(key=lambda r:int(r[0][1:]))
    write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    with (ROOT/'SP88_C13_149_inventory.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(inventory)
    synthesis=ROOT/'review/notation_synthesis.md'
    doubt_text='# Notation table\n\n'
    if synthesis.exists():
        doubt_text+=synthesis.read_text().rstrip()+'\n\n## Page-local notation observations\n\n'
    doubt_text+='Only visually inspected occurrences are evidence; a recorded local shape is not authority for uninspected occurrences. Double quotation marks are set as two backticks and two apostrophes; genuine guillemets are retained.\n\n'+table(['Written form','Meaning or use','Verified places'],notations)
    doubt_text+='\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)
    doubt_text+='\n## Abbreviations\n\nExpansions in this table are explanatory only and are not supplied in the transcription.\n\n'+table(['Scan','Written','Proposed expansion'],abbreviations)
    note=ROOT/'review/legibility_note.txt'
    doubt_text+='\n## Legibility and reliability\n\n'+(note.read_text() if note.exists() else 'The page-local reports retain uncertain letters and cancellation layers explicitly. A final comparative assessment follows completion of all first and independent second readings.')+'\n'
    (ROOT/'SP88_C13_149_doubts.md').write_text(doubt_text)
    (ROOT/'SP88_C13_149_notes.md').write_text('# Notes while reading\n\nPage summaries report the manuscript’s claims; they do not certify those claims. Mathematical checks actually performed are identified separately in CHECK_EVENTS.tsv. No external text was researched.\n\nThe supplied reading instructions identify the paper watermark as “EXTRA STRONG”; it is not manuscript text and is not transcribed. Faint reverse-side traces are distinguished from foreground writing.\n\n'+'\n\n'.join(notes)+'\n')
    write_tsv('CHECK_EVENTS.tsv',['statement id','date','who (model, effort, run)','type','outcome'],checks)
    (ROOT/'SP88_C13_149_hand_log.md').write_text('# Hand log\n\nThe supplied prior log was consulted as a warning, not as evidence for the present pages. Its cote-149 observations concern scans 003–004; the observations below are from the current 25 scans.\n\n'+table(['Scan','Habit','Places','Range and exceptions','Witness errors'],hands))
    categories=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    feedback='# Feedback on the recurrent-error sheet\n\nCounts below are logged adjudicated places, not a statistical estimate of the error rate in the manuscript. A place belongs to its principal category and is counted once. Counts distinguish corrections of C from disagreements with either draft.\n\n'
    feedback+=table(['Error-sheet category','Places differing from either witness','Places differing from C','Places differing from H'],[[c,sum(r.get('error_category','Other')==c for d,r in changes),sum(r.get('error_category','Other')==c and bool(r.get('vs_C')) for d,r in changes),sum(r.get('error_category','Other')==c and bool(r.get('vs_H')) for d,r in changes)] for c in categories])
    feedback+='\n## Page-local details\n\n'+table(['Scan','Place','Category','Observation'],[[d['scan'],r['place'],r.get('error_category','Other'),r['evidence']] for d,r in changes])
    extra=ROOT/'review/feedback_extra.txt'
    if extra.exists():feedback+='\n## Recurring issues requiring added emphasis\n\n'+extra.read_text()+'\n'
    (ROOT/'SP88_C13_149_sheet_feedback.md').write_text(feedback)
    combined='\\cotefile{149}\n\n'+'\n\n'.join((ROOT/'pages'/f'149_scan{d["scan"]:03d}.tex').read_text().rstrip() for d in data)+'\n'
    (ROOT/'SP88_C13_149_transcription.tex').write_text(combined)
    print(json.dumps({'accepted':len(data),'changes':len(changes),'vs_C':sum(bool(r.get('vs_C')) for d,r in changes),'vs_H':len(coll),'mark_decisions':len(decisions),'remaining_doubts':len(doubts),'checks':len(checks)}))
if __name__=='__main__':main()
