"""Maintain the reader's manually entered transcription decisions; no OCR."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT.parent/'input'/'SP56_CW_63_witnesses'
MAP={int(r['our_scan']):r for r in csv.DictReader((INPUT/'page_map.tsv').open(),delimiter='\t')}
PREFIX='SP56_CW_63'

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(s): return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n|'+ '|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(md(x) for x in row)+' |\n' for row in rows)+'\n'

def save(scan, *, replacements=(), text=None, **record):
    path=ROOT/'pages'/Path(MAP[scan]['codex_file']).name
    old=(INPUT/MAP[scan]['codex_file']).read_text() if not path.exists() else path.read_text()
    text=old if text is None else text
    for before,after in replacements:
        if before not in text: raise ValueError(f'{scan}: missing replacement {before!r}')
        text=text.replace(before,after)
    text=text.rstrip()+'\n'
    path.write_text(text)
    record.update(scan=scan,folder=MAP[scan]['folder'],filename=path.name,hua_has=MAP[scan]['hua_has'],done=utc())
    (ROOT/'records'/f'{scan:03}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    rebuild()
    with (ROOT/'progress.log').open('a') as f: f.write(f'scan {scan:03} done {record["done"]}\n')
    print(f'scan {scan:03} written; {len(record.get("changes",[]))} textual change rows')

def rebuild():
    rs=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('*.json'))]
    (ROOT/f'{PREFIX}_transcription.tex').write_bytes(b'\\cotefile{63}\n'+b''.join((ROOT/'pages'/r['filename']).read_bytes() for r in rs))
    counts=[]; allch=[]
    for r in rs:
        ch=r.get('changes',[]);allch.extend((r['scan'],c) for c in ch)
        counts.append([r['scan'],sum('C' in c.get('against','C') for c in ch),sum('H' in c.get('against','C') for c in ch),*[sum(c['confidence']==q for c in ch) for q in ['high','medium','low']]])
    total=['All']+[sum(x[i] for x in counts) for i in range(1,6)]
    s='# Consolidation changes\n\nCounts concern reading changes only; certainty-only decisions are in the doubts file. H descriptions are editorial summaries, not transcriptions, and generate no collation rows. A place differing from both witnesses is one change row but contributes to both witness counts. Crops use original whole-image pixel coordinates.\n\n'
    s+=table(['Scan','Against C','Against H','High','Medium','Low'],counts+[total])
    s+='## Consequential corrections\n\n'
    consequential=[f'- Scan {scan}, {c["place"]}: {c["consequential"]}' for scan,c in allch if c.get('consequential')]
    s+='\n'.join(consequential) if consequential else 'No consequential correction recorded at this stage.'
    s+='\n\n'
    coll=[]
    for r in rs:
        s+=f'## Scan {r["scan"]:03}\n\n'
        ch=r.get('changes',[])
        if ch:s+=table(['Place','C','H','Final reading','What the scan shows / crop','Confidence'],[[c['place'],c['c'],c.get('h','No source transcription ('+r['hua_has']+').'),c['final'],c['evidence'],c['confidence']] for c in ch])
        else:s+='No reading change against C. H has no source transcription on this page.\n\n' if r['hua_has']!='text' else 'No reading change against either witness.\n\n'
        if r.get('reviews'):
            s+='### Crop decisions and retained readings\n\n'+table(['Place','Witness readings','Decision / visible evidence','Confidence'],[[x['place'],x['witness'],x['decision'],x['confidence']] for x in r['reviews']])
        s+='### Unresolved\n\n'+ ('\n'.join('- '+d['place']+': '+d['reading']+'; '+d['reason'] for d in r.get('doubts',[])) or 'None.')+'\n\n'
        for c in ch:
            if 'H' in c.get('against','C'):
                coll.append([r['folder'],MAP[r['scan']]['their_page'],r['scan'],c['place'],c['h'],c['c'],c['final'],c['evidence'],c.get('hkind',c['kind']),c.get('marked_in_H','no'),c['confidence']])
    (ROOT/f'{PREFIX}_changes.md').write_text(s)
    with (ROOT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
    inv=[]
    for r in rs:
        for i,e in enumerate(r.get('inventory',[]),1):
            inv.append([r['scan'],r.get('sheet_kind','typescript'),e.get('hand','typewriter'),e.get('element',f'{r["scan"]:03}-{i:02}'),e['kind'],e['position'],e['text'],'yes'])
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(inv)
    s='# Notation table\n\nReadings are local to these images; a typeface or hand change is not silently regularised.\n\n'
    s+=table(['Scan(s)','Sign / usage','Reading','Evidence / limits'],[[r['scan'],n['sign'],n['reading'],n['evidence']] for r in rs for n in r.get('notation',[])])
    s+='## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],[[r['scan'],d['place'],d['reading'],d.get('alternatives','none recoverable'),d['confidence'],d['reason']] for r in rs for d in r.get('doubts',[])])
    s+='## Decisions on witness C doubt marks\n\n'+table(['Scan','Place','C reading','Decision','Evidence'],[[r['scan'],d['place'],d['c'],d['final'],d['reason']] for r in rs for d in r.get('certainty',[])])
    s+='## Abbreviations (expanded here only)\n\n'+table(['Scan','As written','Probable expansion / use'],[[r['scan'],a[0],a[1]] for r in rs for a in r.get('abbreviations',[])])
    s+='## Legibility and witness coverage\n\n'+ '\n\n'.join(f'**Scan {r["scan"]}.** '+r.get('legibility','') for r in rs)+'\n'
    (ROOT/f'{PREFIX}_doubts.md').write_text(s)
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes describe only the supplied pages. A description of what a page claims is not a proof check. Actual mathematical checks are separately recorded in CHECK_EVENTS.tsv.\n\n'+''.join(f'## Scan {r["scan"]:03}\n\n'+r.get('notes','')+'\n\n' for r in rs))
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand and notation log\n\nNo attribution of an annotation to Grothendieck is made merely because the sheet is in his archive. These typescripts and printed pages can have other readers’ or proofreaders’ marks.\n\n'+table(['Pages','Habit / notation','Scope / exceptions','Witness misreading'],[[r['scan'],h['habit'],h['scope'],h['error']] for r in rs for h in r.get('hands',[])]))
    kinds=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded or spelling modernised','Text that is not on the page','Other']
    s='# Feedback on the error sheet\n\nCounts are textual change places against C, assigned one primary category each. Certainty-only resolutions are excluded. H differences are counted separately in the collation file. Retained source slips are not witness errors.\n\n'
    s+=table(['Error-sheet kind','Places','Scan and place'],[[k,sum(c.get('category')==k and 'C' in c.get('against','C') for _,c in allch),'; '.join(f'{n}: {c["place"]}' for n,c in allch if c.get('category')==k and 'C' in c.get('against','C'))] for k in kinds])
    s+='## Additional recurring issues\n\n'+ '\n'.join('- '+x for r in rs for x in r.get('feedback',[]))+'\n'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(s)
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
        for r in rs:
            for x in r.get('checks',[]):w.writerow([x['id'],x.get('date',r['done']),x.get('who','ChatGPT GPT-6 Astra Pro; effort not exposed; SP56_CW_63 second pass'),x['type'],x['outcome']])
    (ROOT/f'{PREFIX}_audit.md').write_text('# Second reading\n\nAll image reading and all reading decisions in both passes were made by the same primary reader. A separate helper supplied only the syntax/inventory validator.\n\n'+''.join(f'## Scan {r["scan"]:03}\n\n'+r.get('audit','Pending second reading.')+'\n\n' for r in rs))

def audit(scan, note, replacements=(), changes=(), certainty=(), doubts=None):
    p=ROOT/'records'/f'{scan:03}.json';r=json.loads(p.read_text())
    f=ROOT/'pages'/r['filename'];s=f.read_text()
    for before,after in replacements:
        if before not in s:raise ValueError(f'{scan}: missing audit replacement {before!r}')
        s=s.replace(before,after)
    f.write_text(s);r['audit']=note+'\n\nCompleted '+utc();r.setdefault('changes',[]).extend(changes);r.setdefault('certainty',[]).extend(certainty)
    if doubts is not None:r['doubts']=doubts
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');rebuild()
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {utc()}\n')
    print(f'scan {scan:03} audited')

if __name__=='__main__':rebuild()
