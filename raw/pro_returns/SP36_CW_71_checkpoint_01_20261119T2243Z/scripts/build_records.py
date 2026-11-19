from pathlib import Path
import csv, json, collections, hashlib, re

OUT=Path(__file__).resolve().parents[1]
def esc(x):
    if x is None:return '—'
    return str(x).replace('|','&#124;').replace('\n','<br>')
def code(x):return '—' if x is None else '`'+esc(x)+'`'
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(esc(x) for x in r)+' |' for r in rows])+'\n'
def write_csv(name,fields,rows,delimiter=','):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)

decisions=[json.loads(p.read_text()) for p in sorted((OUT/'decisions').glob('scan*.json'))]
changes=['# SP36_CW_71 — Consolidated decisions','\nCounts are local reading decisions, not word-error rates. Syntax-only differences are excluded. A retained C doubt is documented but is not counted as a change against C. H pages with no transcription have no collation rows. Confidence describes the final reading, including a precisely preserved uncertainty.\n','## Counts\n']
countrows=[]; totals=collections.Counter(); consequential=[]; coll=[]; inv=[]; notes=['# SP36_CW_71 — Notes while reading','\nThese notes report the supplied pages only. A mathematical correction discussed here never replaces the manuscript reading. See CHECK_EVENTS.tsv for the actual level of checking.\n']; doubts=[]; abbreviations={}; checks=[]; notation=[]
for d in decisions:
    fs=d['findings']; co=collections.Counter()
    for f in fs:
        co['C']+=int(f.get('diff_c',False)); co['H']+=int(f.get('diff_h',False))
        if f.get('diff_c') or f.get('diff_h'):co[f['confidence']]+=1
        if f.get('diff_c'):co['C_'+f['confidence']]+=1
        if f.get('diff_h'):co['H_'+f['confidence']]+=1
        if f.get('consequential'):consequential.append(f"- Scan {d['scan']:03d}, {f['place']}: {code(f['reading'])}. {f.get('consequence','See the page decision and notes.')} ({f['id']})")
        if f.get('diff_h') and d['hua_has']=='text':
            coll.append(dict(folder=d['folder'],their_page=d['their_page'],our_scan=d['scan'],line=f['place'],their_reading=f.get('h',''),codex_reading=f.get('c',''),final_reading=f['reading'],scan_shows=f['evidence'],kind=f['kind'],marked_in_H='yes' if f.get('marked_in_H') else 'no',confidence=f['confidence']))
    countrows.append([f"{d['scan']:03d}",co['C'],co['C_high'],co['C_medium'],co['C_low'],co['H'],co['H_high'],co['H_medium'],co['H_low']]);totals.update(co)
    inv.extend(d['inventory'])
    for q in d.get('doubts',[]):doubts.append([f"{d['scan']:03d}",q['place'],code(q['reading']),code(q.get('alternatives','')),q['confidence'],q.get('reason','')])
    for a in d.get('abbreviations',[]):abbreviations.setdefault(a['written'],{'expansion':a['expansion'],'scans':[]})['scans'].append(d['scan'])
    for n in d.get('notation',[]):notation.append([n['sign'],code(n['tex']),f"{d['scan']:03d}: {n['place']}",n['ink'],n.get('alternatives','')])
    notes.append(f"## Scan {d['scan']:03d}\n")
    for i,n in enumerate(d.get('notes',[]),1):
        if isinstance(n,str): notes.append(f"**N{d['scan']:03d}-{i:02d}.** {n}\n")
        else:notes.append(f"**{n['id']}.** {n['text']}\n")
    checks.extend(d.get('checks',[]))
countrows.append(['Total',totals['C'],totals['C_high'],totals['C_medium'],totals['C_low'],totals['H'],totals['H_high'],totals['H_medium'],totals['H_low']])
changes.append(table(['Scan','Against C','C high','C medium','C low','Against H','H high','H medium','H low'],countrows))
changes.append('## Consequential readings\n\n'+('\n'.join(consequential) or 'None recorded yet.')+'\n')
for d in decisions:
    changes.append(f"## Scan {d['scan']:03d} — {d['folder']} / H page {d['their_page']} ({d['hua_has']})\n")
    rows=[]
    for f in d['findings']:
        readers=f.get('readers',{})
        rr='; '.join(r+': '+code(readers.get(r,'not separately proposed; see complete reading')) for r in ['R1','R2','R3'])
        crop=f.get('crop')
        if isinstance(crop,str):crop=crop.replace(str(OUT)+'/', '')
        evidence=f['evidence']+((' Crop: '+str(crop)) if crop else '')
        tags=[]
        if f.get('c_doubt'):tags.append('C doubt')
        if f.get('s_id'):tags.append('S: '+str(f['s_id']))
        rows.append([f['id']+'; '+f['place']+(' ('+', '.join(tags)+')' if tags else ''),code(f.get('c')),code(f.get('h')),code(f['reading']),rr,evidence,f['confidence']])
    changes.append(table(['Place / decision','C','H','Final','Three independent readings','What the scan shows / decision','Confidence'],rows))
    changes.append('### Remaining doubts\n')
    ds=d.get('doubts',[])
    changes.append('\n'.join('- '+q['place']+': '+code(q['reading'])+'; '+q.get('reason','') for q in ds)+'\n' if ds else 'None.\n')
    if d.get('sweep'):changes.append('### Witness S\n\n'+d['sweep']+'\n')
(OUT/'SP36_CW_71_changes.md').write_text('\n'.join(changes))
write_csv('SP36_CW_71_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll,'\t')
write_csv('SP36_CW_71_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv)
(OUT/'SP36_CW_71_notes.md').write_text('\n'.join(notes))
known_check_ids={c['statement_id'] for c in checks}
for p in sorted((OUT/'adjudication').glob('scan*_main_check.json')):
    event=json.loads(p.read_text())
    if event['statement_id'] not in known_check_ids:
        checks.append(event);known_check_ids.add(event['statement_id'])
write_csv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks,'\t')
notation_text='# Notation table\n\nEntries are observations of the ink, not instructions to normalize a differing manuscript sign.\n\n'+table(['Sign / usage','LaTeX','Scan / place','Written form','Alternatives'],notation)
(OUT/'notation.md').write_text(notation_text)
leg=(OUT/'legibility.md').read_text() if (OUT/'legibility.md').exists() else 'The reading is in progress. Final comparative assessment will be written after all pages are decided.'
(OUT/'SP36_CW_71_doubts.md').write_text(notation_text+'\n# Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Ink / reason'],doubts)+'\n# Abbreviations\n\nExpansions below are conjectural glosses only and are never supplied in the transcription.\n\n'+table(['Written','Possible expansion','Scans'],[[k,v['expansion'],', '.join(map(str,sorted(set(v['scans']))))] for k,v in sorted(abbreviations.items())])+'\n# Legibility and witness comparison\n\n'+leg+'\n')
pages=[]
for d in decisions:
    p=OUT/'pages'/d['filename']
    if p.exists():pages.append(re.sub(r'\\cotefile\{71\}\s*','',p.read_text()))
(OUT/'SP36_CW_71_transcription.tex').write_text('\\cotefile{71}\n'+ '\n\n'.join(pages))
print(json.dumps({'decided_pages':len(decisions),'scans':[d['scan'] for d in decisions],'changes_C':totals['C'],'changes_H':totals['H'],'inventory_elements':len(inv),'check_events':len(checks),'unresolved':len(doubts)},indent=2))
