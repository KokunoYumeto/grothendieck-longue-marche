"""Assemble the human-readable collation records from individually reviewed pages.

This script performs no image recognition and makes no reading decisions.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, json

WORK=Path(__file__).resolve().parents[1]
BASE=WORK.parent
PREFIX='SP94_C13_151'

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(value):
    if value is None: return ''
    return str(value).replace('\n',' / ').replace('|',r'\|')
def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+
                     ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])+'\n'
def write_tsv(path, fields, rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def write_csv(path, fields, rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def crop_evidence(r):
    crop=r.get('crop','')
    box=r.get('box',[])
    return (r.get('evidence','')+' '+(f'Crop: {crop}; original box {tuple(box)}.' if crop and crop!='page' else 'Page/halves; unresolved.' if crop=='page' else '')).strip()

def compile_all():
    state=json.loads((WORK/'run_state.json').read_text())
    order=state['order']
    done=set(state['completed'])
    reports=[json.loads((WORK/'reports'/(p+'.json')).read_text()) for p in order if p in done]
    (WORK/(PREFIX+'_transcription.tex')).write_text('\\cotefile{151}\n\n'+'\n\n'.join((WORK/'pages'/(p+'.tex')).read_text().rstrip() for p in order if p in done)+'\n')

    counts=[];total=Counter();conseq=[]
    for r in reports:
        cc=Counter()
        for row in r['changes']:
            if not (row.get('diff_c') or row.get('diff_h')): continue
            cc['C']+=bool(row.get('diff_c'));cc['H']+=bool(row.get('diff_h'))
            if row.get('diff_c'): cc['C_'+row['confidence']]+=1
            if row.get('diff_h'): cc['H_'+row['confidence']]+=1
            cc[row['confidence']]+=1;cc['rows']+=1
            if row.get('consequential'):conseq.append(f"- Scan {r['scan']:03d}, {row['place']}: {row['consequential']}")
        counts.append([f"{r['scan']:03d}",cc['C'],cc['C_high'],cc['C_medium'],cc['C_low'],cc['H'],cc['H_high'],cc['H_medium'],cc['H_low'],cc['rows']]);total.update(cc)
    counts.append(['Total',total['C'],total['C_high'],total['C_medium'],total['C_low'],total['H'],total['H_high'],total['H_medium'],total['H_low'],total['rows']])
    changes=['# Consolidated reading: changes and decisions','',
        'Counts are recorded places, not changed tokens. One place may differ from both witnesses. Pure macro syntax is excluded. Retained doubts and certainty-only decisions are identified separately; they do not count as textual corrections unless the ink reading or its state changes. Where alternatives remain open, a counted disagreement concerns the primary printed reading and is not a claim that the competing reading has been ruled out. In the collation TSV, their_page follows the supplied convention: H page n corresponds to scan n+1.','',
        table(['Scan','Against C','C high','C medium','C low','Against H','H high','H medium','H low','Places'],counts),
        '## Consequential corrections','', '\n'.join(conseq) if conseq else 'None recorded yet.','']
    coll=[];decisions={};inventory=[];doubts=[];notes=['# Notes while reading','',
        'The source images are the authority. Mathematical comments are limited to these leaves. A page summary is not a proof check; CHECK_EVENTS.tsv states what was actually checked or merely carried as background.','']
    checks=[];habits=[];abbrevs={};feedback=Counter();feedback_places={}
    for r in reports:
        n=r['scan'];p=r['page']
        changes.extend([f'## Scan {n:03d}','',table(['Place','Witness C','Witness H','Consolidated reading','Visible evidence and crop','Confidence'],[
            [x['place'],x.get('c',''),x.get('h',''),x.get('final',''),crop_evidence(x),x['confidence']] for x in r['changes'] if x.get('diff_c') or x.get('diff_h')]),'### Still unresolved',''])
        ds=r.get('doubts',[])
        changes.append('\n'.join('- '+x['place']+': '+x['reading']+' — '+x.get('reason','') for x in ds) if ds else 'None recorded.')
        changes.append('')
        if r.get('second_changes'):
            changes.extend(['### Changes after the independent second reading', '',
                'These rows document revisions of the first consolidated reading. Final disagreements with C and H are counted in the main table above; this audit history is not counted a second time.', '',
                table(['Place / box','First consolidated reading','Independent second reading','Final adjudication','Visible evidence and crop','Confidence'], [
                    [x['place'],x['first'],x['second'],x['final'],crop_evidence(x),x['confidence']]
                    for x in r['second_changes']]), ''])
        for x in r['changes']:
            if x.get('diff_h'):
                coll.append(dict(folder='151',their_page=n-1,our_scan=n,line=x['place'],their_reading=x.get('h',''),codex_reading=x.get('c',''),final_reading=x.get('final',''),scan_shows=crop_evidence(x),kind=x['kind'],marked_in_H='yes' if x.get('marked_h') else 'no',confidence=x['confidence']))
            if x.get('diff_c') or x.get('diff_h'):
                cat=int(x.get('error_category',10));feedback[cat]+=1;feedback_places.setdefault(cat,[]).append(f"{n:03d}/{x['id']}")
        for x in r.get('decisions',[]):
            decisions[x['id']]=dict(id=x['id'],cote='151',scan=n,decision=x['decision'],reading=x['reading'],**{'what the ink shows':x['evidence']},crop=(x.get('crop','page')+' '+str(tuple(x.get('box',[])))) if x.get('crop','page')!='page' else 'page',confidence=x['confidence'])
        for x in r.get('inventory',[]):inventory.append(dict(scan=n,**x))
        for x in ds:doubts.append([f'{n:03d}',x['place'],x['reading'],x.get('alternatives',''),x['confidence'],x.get('reason','')])
        notes.extend([f'## Scan {n:03d}','']+r.get('notes',[])+[''])
        for x in r.get('checks',[]):checks.append(dict(statement_id=x['statement_id'],date=x.get('date',r.get('reviewed_utc',now())),who=x.get('who','GPT-6 Astra Pro; run SP94_C13_151; '+r.get('reader','reader')+' / main reader (effort not exposed)'),type=x['type'],outcome=x['outcome']))
        for x in r.get('hand',[]):habits.append([f'{n:03d}',x['habit'],x['evidence'],x.get('every_occurrence','not established'),x.get('misread_places','')])
        for x in r.get('abbreviations',[]):
            k=x['form'];abbrevs.setdefault(k,{'expansion':x['expansion'],'pages':[]})['pages'].append(f'{n:03d}')

    (WORK/(PREFIX+'_changes.md')).write_text('\n'.join(changes))
    write_tsv(WORK/(PREFIX+'_collation.tsv'),['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    with (BASE/'source/SP94_C13_151_texts/MARKS.tsv').open() as f:markorder=[r['id'] for r in csv.DictReader(f,delimiter='\t')]
    write_tsv(WORK/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],[decisions[k] for k in markorder if k in decisions])
    write_csv(WORK/(PREFIX+'_inventory.csv'),['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory)
    (WORK/(PREFIX+'_notes.md')).write_text('\n'.join(notes))
    write_tsv(WORK/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    legibility=(WORK/'legibility_note.md').read_text() if (WORK/'legibility_note.md').exists() else 'First reading in progress. The report will distinguish clear main-line ink from crowded insertions and cancellation layers.'
    (WORK/(PREFIX+'_doubts.md')).write_text('# Notation and remaining doubts\n\n'+(WORK/'notation.md').read_text()+'\n\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions are explanatory and are not inserted into the transcription.\n\n'+table(['Written form','Possible expansion','Scans'],[[k,v['expansion'],', '.join(v['pages'])] for k,v in sorted(abbrevs.items())])+'\n## Legibility and witnesses\n\n'+legibility+'\n')
    (WORK/(PREFIX+'_hand_log.md')).write_text('# Hand log\n\nEach observation is bounded by its cited pages; "not established" means it has not been shown to hold universally.\n\n'+table(['Scan','Habit','Visible evidence','Every occurrence?','Witness misreadings'],habits))
    labels={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left illegible',6:'Insertion placement',7:'Struck text',8:'Abbreviations / spelling',9:'Text not on the page',10:'Other'}
    feedback_note=(WORK/'feedback_note.md').read_text() if (WORK/'feedback_note.md').exists() else 'Recurring observations are collected in the hand log; final feedback awaits completion of the independent second reading.'
    (WORK/(PREFIX+'_sheet_feedback.md')).write_text('# Error-sheet feedback\n\nOne principal category per substantive recorded place; categories are not rates of error per token.\n\n'+table(['Category','Places','Locations'],[[labels[k],feedback[k],', '.join(feedback_places.get(k,[]))] for k in labels])+'\n## Additional patterns and qualifications\n\n'+feedback_note+'\n')
    return dict(pages=len(reports),changes_C=total['C'],changes_H=total['H'],rows=total['rows'],marks=len(decisions),inventory=len(inventory),doubts=len(doubts))

if __name__=='__main__': print(json.dumps(compile_all(),indent=2))
