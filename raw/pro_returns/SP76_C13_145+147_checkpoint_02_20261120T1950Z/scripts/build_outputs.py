from pathlib import Path
import csv, json
from collections import Counter

W=Path(__file__).resolve().parents[1]
PREFIX='SP76_C13_145+147'
ORDER=(W/'page_order.txt').read_text().splitlines()
reports=[]
for page in ORDER:
    p=W/'reports'/f'{page}.json'
    if p.exists():
        r=json.loads(p.read_text())
        if r.get('adjudicated'): reports.append(r)

def tsv(name, fields, rows, delimiter='\t'):
    with (W/name).open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore')
        wr.writeheader(); wr.writerows(rows)

def cell(x):
    if isinstance(x,(dict,list)): x=json.dumps(x,ensure_ascii=False)
    return str(x if x is not None else '').replace('|','\\|').replace('\n','<br>')

def table(fields,rows):
    s='| '+' | '.join(fields)+' |\n| '+' | '.join('---' for _ in fields)+' |\n'
    return s+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)+'\n'

counts=[]; allchanges=[]; consequence=[]; collation=[]; decisions=[]; inventory=[]; checks=[]
for r in reports:
    cc=r['changes']; hist=Counter(x['confidence'] for x in cc)
    counts.append([r['page'],sum(bool(x.get('against_C')) for x in cc),sum(bool(x.get('against_H')) for x in cc),len(cc),hist['high'],hist['medium'],hist['low']])
    for x in cc:
        allchanges.append((r,x))
        if x.get('consequential'): consequence.append(f"- {r['page']}, {x['place']}: `{x['final']}` — {x['evidence']}")
        if x.get('against_H'):
            collation.append(dict(folder=r['cote'],their_page=int(r['scan'])-1,our_scan=f"{int(r['scan']):03d}",line=x['place'],their_reading=x['H'],codex_reading=x['C'],final_reading=x['final'],scan_shows=x['evidence']+(' ['+x.get('crop','')+' '+str(x.get('box',''))+']' if x.get('crop') else ''),kind=x['kind'],marked_in_H=x.get('marked_in_H','no'),confidence=x['confidence']))
    for d in r.get('decisions',[]):
        d=dict(d)
        if d.get('box'): d['crop']=d.get('crop','')+' '+str(d['box'])
        decisions.append(d)
    inventory+=r.get('inventory',[]); checks+=r.get('check_events',[])
total=['TOTAL']+[sum(row[i] for row in counts) for i in range(1,7)]
change_text='# Changes and scan evidence\n\nCounts are decision places, not individual character edits. Against C/H counts substantive differences of reading or placement; certainty alone is excluded from those two counts. Rows additionally includes cropped resolutions of C doubts even when their selected reading is unchanged. Added doubt alone is listed in the doubts file. Pure macro differences and H editorial notes are excluded. Confidence qualifies the reading at that place.\n\n'
change_text+=table(['Page','Against C','Against H','Rows','High','Medium','Low'],counts+[total])
witness_confidence=[]
for r in reports:
    for witness in ['C','H']:
        h=Counter(x['confidence'] for x in r['changes'] if x.get('against_'+witness))
        witness_confidence.append([r['page'],witness,h['high'],h['medium'],h['low'],sum(h.values())])
for witness in ['C','H']:
    hs=[row for row in witness_confidence if row[1]==witness]
    witness_confidence.append(['TOTAL',witness]+[sum(row[i] for row in hs) for i in range(2,6)])
change_text+='## Confidence by witness\n\n'+table(['Page','Witness','High','Medium','Low','Total'],witness_confidence)
change_text+='## Consequential corrections\n\n'+ ('\n'.join(consequence) if consequence else 'None recorded yet.')+'\n\n'
for r in reports:
    change_text+='## '+r['page']+'\n\n'
    change_text+=table(['Place','Witness C','Witness H','Final reading','What the scan shows; crop and original box','Confidence'],[[x['place'],'`'+x['C']+'`','`'+x['H']+'`','`'+x['final']+'`',x['evidence']+(' — `'+x['crop']+'`, '+str(x.get('box')) if x.get('crop') else ' — full-resolution half'),x['confidence']] for x in r['changes']])
    if r.get('additional_crop_checks'):
        change_text+='### Additional cropped inspections (reading unchanged)\n\nThese inspections are documented without adding substantive change rows or error counts.\n\n'
        change_text+=table(['Place','Reading retained','Ink evidence; crop and original box','Confidence'],[[x['place'],x['reading'],x['evidence']+' — `'+x['crop']+'`, '+str(x['box']),x['confidence']] for x in r['additional_crop_checks']])
    change_text+='### Unresolved places\n\n'
    change_text+=table(['Place','Reading','Alternatives','Confidence','Reason'],[[d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')] for d in r.get('doubts',[])]) if r.get('doubts') else 'No unresolved reading is recorded.\n\n'
    if r.get('audited'):
        a=r['audit']
        change_text+='### Independent image-only second reading\n\n'
        change_text+=f"Reader {a['reader']}; {a['boxes']} boxes read, {a['differences']} token-level differences adjudicated, {a['changed']} places changed. The second reading was written before comparison. Every mismatch below was inspected on its second-pass crop, including notational or scope differences that do not change the ink reading.\n\n"
        change_text+=table(['Box','First reading','Independent second reading','Final decision','Changed','Ink evidence and crop','Confidence'],[[d['box'],d['first_reading'],d['second_reading'],d['final_reading'],d['changed'],d['evidence']+' — '+d['crop'],d['confidence']] for d in a['adjudications']])
(W/f'{PREFIX}_changes.md').write_text(change_text)
tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
decisions.sort(key=lambda d:int(d['id'][1:]))
tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
tsv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
notation=[]; abbr=[]; doubts=[]; habits=[]
for r in reports:
    notation += [[n['form'],n['meaning_or_use'],n.get('places',r['page'])] for n in r.get('notation',[])]
    abbr += [[a['form'],a['expansion'],a.get('places',r['page'])] for a in r.get('abbreviations',[])]
    doubts += [[r['page'],d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')] for d in r.get('doubts',[])]
    habits += [[h['habit'],h.get('places',r['page']),h.get('scope',''),h.get('witness_errors','')] for h in r.get('hand_habits',[])]
def consolidate_forms(rows):
    grouped={}
    for form,meaning,places in rows:
        entry=grouped.setdefault(form,{'meanings':[],'places':[]})
        if meaning not in entry['meanings']: entry['meanings'].append(meaning)
        if places not in entry['places']: entry['places'].append(places)
    return [[form,' '.join(v['meanings']),'; '.join(v['places'])] for form,v in grouped.items()]
notation=consolidate_forms(notation)
abbr=consolidate_forms(abbr)
notetext='# Notation table\n\n'+table(['Form','Meaning or use','Places'],notation)
(W/'notation.md').write_text(notetext)
doubttext=notetext+'## Remaining doubts\n\n'+table(['Page','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'## Abbreviations\n\nExpansions are editorial suggestions for this list only.\n\n'+table(['Written form','Suggested expansion','Places'],abbr)
legibility=W/'reports/legibility.md'
doubttext+='## Legibility and witness comparison\n\n'+(legibility.read_text() if legibility.exists() else 'Assessment in progress; retain the individual doubts above.')+'\n'
(W/f'{PREFIX}_doubts.md').write_text(doubttext)
(W/f'{PREFIX}_hand_log.md').write_text('# Hand and notation log\n\nObservations are local unless their scope explicitly says otherwise. Similar shapes elsewhere must still be checked against the ink.\n\n'+table(['Habit','Places','Observed scope','Witness errors'],habits))
notes='# Notes while reading\n\nThese notes describe the supplied leaves only. A summary of a manuscript claim is not verification of that claim. CHECK_EVENTS.tsv records only the check types actually performed; no outside literature was researched.\n\n'
for r in reports:
    note=r.get('notes','')
    if isinstance(note,list): note='\n\n'.join(str(x) for x in note)
    if r.get('pagination_attribution'): note=str(note)+'\n\n'+r['pagination_attribution']
    notes+='## '+r['page']+'\n\n'+str(note)+'\n\n'
(W/f'{PREFIX}_notes.md').write_text(notes)
kind_counts=Counter(x['kind'] for _,x in allchanges if x.get('against_C') or x.get('against_H'))
error_sheet=[('Symbols and indices','misread symbol or index'),('Words','misread word'),('Omissions','omission'),('Drawings and diagrams','drawing or diagram'),('Readable ink left as illegible','readable ink left as \\ill{}'),('Insertions put in the wrong place','insertion or placement'),('Struck text','deletion state'),('Abbreviations expanded, spelling modernised','abbreviation expanded or spelling modernised'),('Text that is not on the page','text not on the page'),('Other','other')]
feedback_rows=[]
for title,kind in error_sheet:
    rows=[x for _,x in allchanges if x['kind']==kind]
    feedback_rows.append([title,sum(bool(x.get('against_C')) for x in rows),sum(bool(x.get('against_H')) for x in rows),sum(bool(x.get('against_C') or x.get('against_H')) for x in rows)])
feedback='# Error-sheet feedback\n\nCounts below are recorded decision places, with one primary classification per row; they are not rates per token. A place may exhibit several visual hazards even though it is counted once.\n\n'+table(['Error-sheet kind','Against C','Against H','Distinct decision places'],feedback_rows)
feedback+='\nCropped resolutions of an unchanged C reading: '+str(sum(bool(x.get('certainty_resolution_C')) for _,x in allchanges))+'. These are reading decisions, excluded from substantive error counts above.\n\n'
feedback+='## Additional recurring observations\n\nSee the hand log for observed letterforms and notation, including the scope of each observation. No unobserved cross-cote habit is assumed.\n'
feedback_extra=W/'reports/feedback_observations.md'
if feedback_extra.exists(): feedback+='\n'+feedback_extra.read_text().strip()+'\n'
(W/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
combined=[]; prev=None
for r in reports:
    if r['cote']!=prev: combined.append('\\cotefile{'+str(r['cote'])+'}\n');prev=r['cote']
    combined.append((W/'pages'/f"{r['page']}.tex").read_text().rstrip()+'\n')
(W/f'{PREFIX}_transcription.tex').write_text('\n'.join(combined))
print(json.dumps({'committed_pages':len(reports),'change_rows':len(allchanges),'collation_rows':len(collation),'mark_decisions':len(decisions),'inventory_elements':len(inventory),'remaining_doubts':len(doubts)},ensure_ascii=False))
