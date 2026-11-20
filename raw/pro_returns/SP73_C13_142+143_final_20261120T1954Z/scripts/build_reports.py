from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP73_C13_142+143'
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(x):
    if isinstance(x,(list,tuple)): x='; '.join(str(v) for v in x)
    return str(x if x is not None else '— (no H text)').replace('|', '\\|').replace('\n', '<br>')
def prose(x):
    if isinstance(x,list):
        return '\n\n'.join(prose(v) for v in x)
    if isinstance(x,dict):
        if 'note' in x:
            return ('**'+str(x['place'])+'.** ' if x.get('place') else '')+str(x['note'])
        return '\n\n'.join(str(k)+': '+prose(v) for k,v in x.items())
    return str(x or '')
def crop_reference(mark):
    value=mark.get('crop','page')
    box=mark.get('box')
    if isinstance(value,dict):
        box=value.get('box',box)
        value=value.get('path','page')
    if value!='page' and box and '[' not in str(value):
        return str(value)+' '+str(box)
    return str(value)
def evidence_text(change):
    text=change['ink']
    if change.get('crop'):
        text+=f" Evidence: {change['crop']}; original box {change.get('box')}."
    else:
        text+=f" Evidence: original page/half; box {change.get('box')} (no additional crop)."
    seen={(change.get('crop'),tuple(change.get('box') or []))}
    for extra in change.get('additional_crops',[])+change.get('evidence_crops',[]):
        key=(extra.get('crop'),tuple(extra.get('box') or []))
        if key in seen: continue
        seen.add(key)
        text+=f" Additional evidence: {extra['crop']}; original box {extra.get('box')}."
    return text
def collation_kind(value):
    if value.startswith('deletion state'):
        return 'deletion state (struck given live or live given struck)'
    if value.startswith('readable ink left as'):
        return 'readable ink left as \\ill{}'
    return value
def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(md(c) for c in row)+' |' for row in rows])+'\n'
def write_tsv(path, fields, rows, delimiter='\t'):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore'); w.writeheader(); w.writerows(rows)

records=[]
for p in sorted((ROOT/'state').glob('*_accepted.json')):
    records.append(json.loads(p.read_text()))
changes=[dict(c,page=r['page']) for r in records for c in r.get('changes',[]) if c.get('differs_c') or c.get('differs_h')]
counts=Counter(c.get('confidence','low') for c in changes)
summary=[]
for r in records:
    cs=[c for c in changes if c['page']==r['page']]
    co=Counter(c['confidence'] for c in cs)
    summary.append([r['page'],sum(bool(c.get('differs_c')) for c in cs),sum(bool(c.get('differs_h')) for c in cs),len(cs),co['high'],co['medium'],co['low']])
summary.append(['TOTAL',sum(bool(c.get('differs_c')) for c in changes),sum(bool(c.get('differs_h')) for c in changes),len(changes),counts['high'],counts['medium'],counts['low']])
out=['# Changes against witnesses C and H','',
     'The scans are authoritative. Rows count substantive local differences, not macro syntax or certainty alone. One location can differ from both witnesses, so the two witness totals overlap. Confidence describes the retained reading. All pixel boxes use the original scan coordinates.','',
     'H’s separate drawing files were not supplied. Figure comparisons use its positive local code, explicit claims and named label readings. Silence about a detail in a general figure description is not counted as an omission from the unavailable drawing. Documentary corrections to earlier comparison flags are preserved in the work records.','',
     table(['Page','Against C','Against H','Distinct places','High','Medium','Low'],summary),
     '## Consequential corrections','']
for c in changes:
    if c.get('consequential'):
        out.append(f"- {c['page']}, {c['place']}: {md(c['final'])}. {md(c.get('mathematical_effect',c.get('ink','')))}")
out+=['','## Page records','']
for r in records:
    out += [f"### {r['page']}",'']
    rows=[]
    for c in [c for c in changes if c['page']==r['page']]:
        evidence=evidence_text(c)
        rows.append([c.get('id',''),c['place'],c['c'],c['h'],c['final'],evidence,c['confidence']])
    out.append(table(['ID','Place','C','H','Consolidated','What the scan shows','Confidence'],rows) if rows else 'No substantive difference from the available witnesses.\n')
    out+=['**Still unresolved**','']
    doubts=r.get('remaining_doubts',[])
    out += [f"- {d['place']}: {md(d['reading'])}; alternatives: {md(d.get('alternatives',''))}. {d.get('reason','')} ({d['confidence']})." for d in doubts] or ['None.']
    out+=['']
(ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(out),encoding='utf-8')

coll=[]
for c in changes:
    if not c.get('differs_h'): continue
    cote,scan=c['page'].split('_scan')
    h=c.get('h','') or ''
    marked=c.get('marked_in_H',any(s in h for s in ['\\ill','\\unsure','\\unclear','\\uncertain','[?]']))
    coll.append(dict(folder=cote,their_page=int(scan)-1,our_scan=int(scan),line=c['place'],their_reading=h,codex_reading=c['c'],final_reading=c['final'],scan_shows=evidence_text(c),kind=collation_kind(c['kind']),marked_in_H='yes' if marked else 'no',confidence=c['confidence']))
write_tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)

marks=[]
for r in records:
    for m in r.get('marks',[]):
        marks.append({'id':m['id'],'cote':m.get('cote',r['page'].split('_')[0]),'scan':m.get('scan',int(r['page'].split('scan')[1])),'decision':m['decision'],'reading':m['reading'],'what the ink shows':m['ink'],'crop':crop_reference(m),'confidence':m['confidence']})
marks.sort(key=lambda m:int(m['id'][1:]))
write_tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],marks)

inventory=[]
for r in records:
    for e in r.get('inventory',[]):
        inventory.append(dict(e,scan=r['page']))
write_tsv(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')

notes=['# Notes while reading','',
       'These notes describe the manuscript and the actual reading decisions. A summary of a manuscript assertion is not a proof of that assertion. No material outside the supplied pages was researched. The separate CHECK_EVENTS.tsv records the mathematical work actually performed, with its assumptions and limits.','']
notes_override_path=ROOT/'state/notes_consolidated.json'
notes_override=json.loads(notes_override_path.read_text()) if notes_override_path.exists() else None
if notes_override is not None and set(notes_override) != {r['page'] for r in records}:
    raise SystemExit('Consolidated notes must cover every accepted page exactly once.')
events=[]
notes_cote=None
for r in records:
    cote=r['page'].split('_')[0]
    if cote != notes_cote:
        notes += [f'## Cote {cote}','',
                  'The supplied error sheet names the paper watermark “EXTRA STRONG”. It is excluded wherever it appears and is never treated as a source word or doubt mark. This identification is attributed to the supplied sheet, not to an independent watermark study.','']
        notes_cote=cote
    notes += [f"### {r['page']}",'']
    if notes_override is not None:
        notes += [prose(notes_override[r['page']]),'']
    else:
        notes += [prose(r.get('notes','')),'']
        if r.get('main_notes'): notes += [prose(r['main_notes']),'']
        if r.get('audit_notes'): notes += ['#### Second reading','',prose(r['audit_notes']),'']
    for ev in r.get('check_events',[]):
        ev=dict(ev)
        ev['date']=ev.get('date',r.get('accepted_at','').split(' ')[0])
        ev['who']=ev.get('who',f"GPT-6 Astra Pro; effort not exposed; {r.get('reader','reader')}; SP73_C13_142+143 second-pass run")
        events.append(ev)
(ROOT/f'{PREFIX}_notes.md').write_text('\n'.join(notes),encoding='utf-8')
write_tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','place','statement'],events)

notations=[]; abbreviations=[]; hand=[]; doubts=[]
for r in records:
    for n in r.get('notation',[]):
        notations.append([n.get('sign',''),n.get('appearance',''),n.get('meaning',''),n.get('pages',r['page']),n.get('confidence','')])
    for a in r.get('abbreviations',[]): abbreviations.append([a.get('form',''),a.get('expansion',''),r['page']])
    for h in r.get('hand_log',[]): hand.append([h.get('habit',''),h.get('pages',r['page']),h.get('universality',''),h.get('misread_places','')])
    for d in r.get('remaining_doubts',[]): doubts.append([r['page'],d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
abbreviation_pages={}
for form, expansion, page in abbreviations:
    key=(form,expansion)
    abbreviation_pages.setdefault(key,[])
    if page not in abbreviation_pages[key]: abbreviation_pages[key].append(page)
abbreviations=[[form,expansion,pages] for (form,expansion),pages in abbreviation_pages.items()]
notation_override=ROOT/'state/notation_consolidated.md'
notation=notation_override.read_text() if notation_override.exists() else '# Notation table\n\n'+table(['Sign','Appearance in the hand','Meaning on these pages','Pages','Confidence'],notations)
(ROOT/'state/notation.md').write_text(notation,encoding='utf-8')
doubt_text=[notation,'','## Remaining doubts','',table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts),'','## Abbreviations','',
            'Expansions are editorial suggestions confined to this list; the transcription preserves the abbreviation. Identical form-and-expansion pairs are grouped, with their pages listed. Different local meanings and punctuation remain separate.','',table(['Written form','Suggested expansion','Pages'],abbreviations),'','## Disposition of the original doubt marks','',
            f'{len(marks)} source marks have a recorded decision. '+', '.join(f"{k}: {v}" for k,v in sorted(Counter(m['decision'] for m in marks).items()))+'. Certainty-only resolutions are recorded in decisions.tsv and are excluded from substantive change counts.','',
            table(['Mark','Page','Decision','Reading retained','Confidence'],[[m['id'],str(m['cote'])+'_scan'+str(m['scan']).zfill(3),m['decision'],m['reading'],m['confidence']] for m in marks if m['decision']!='undecided']),'',
            '## Legibility and witnesses','']
legibility=ROOT/'state/legibility.md'
doubt_text.append(legibility.read_text() if legibility.exists() else 'The review is in progress. Crowded insertions, cancellations, and handwritten indices require the most caution. Both witnesses are treated as unverified readings of the same scans.')
(ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(doubt_text),encoding='utf-8')
(ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand and notation log\n\nEach entry is limited to the stated occurrences; similarity of shapes does not authorize silently correcting a clear manuscript slip.\n\n'+table(['Habit','Pages','Does it hold at every occurrence?','Witness misreadings'],hand),encoding='utf-8')

categories={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left as illegible',6:'Insertion placement',7:'Struck text / deletion state',8:'Abbreviations expanded or spelling modernised',9:'Text not on the page',10:'Other'}
cat=Counter(int(c.get('error_category',10)) for c in changes)
feedback=['# Feedback on the error sheet','',
          'Counts refer to distinct substantive disagreement locations recorded in the changes log, each assigned one primary error-sheet category. They are not counts of every word or symbol on the pages and do not establish an error rate. Locations can differ from C, H, or both. Certainty-only decisions are counted separately in decisions.tsv.','',
          table(['Category','Recorded places','Against C','Against H'],[[f'{k}. {v}',cat[k],sum(bool(c.get('differs_c')) for c in changes if int(c.get('error_category',10))==k),sum(bool(c.get('differs_h')) for c in changes if int(c.get('error_category',10))==k)] for k,v in categories.items()]),'','## Locations by category','']
for k,v in categories.items():
    feedback += [f'### {k}. {v}','']
    feedback += [f"- {c['id']}, {c['page']}, {c['place']}: {md(c['final'])}." for c in changes if int(c.get('error_category',10))==k] or ['None recorded.']
    feedback+=['']
feedback+=['## Additional recurring phenomena','']
extra=ROOT/'state/additional_feedback.md'
feedback.append(extra.read_text() if extra.exists() else 'No additional category has yet been established; see the hand log for local letter and notation habits.')
(ROOT/f'{PREFIX}_sheet_feedback.md').write_text('\n'.join(feedback),encoding='utf-8')

combined=[]
last_cote=None
for r in records:
    cote=r['page'].split('_')[0]
    tex=(ROOT/'pages'/f"{r['page']}.tex").read_text()
    if cote!=last_cote and '\\cotefile' not in tex: combined.append('\\cotefile{'+cote+'}\n')
    combined.append(tex.rstrip()+'\n'); last_cote=cote
(ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(combined),encoding='utf-8')
print(json.dumps({'pages':len(records),'changes':len(changes),'against_C':sum(bool(c.get('differs_c')) for c in changes),'against_H':len(coll),'decisions':len(marks),'inventory':len(inventory),'check_events':len(events),'remaining_doubts':len(doubts)},ensure_ascii=False))
