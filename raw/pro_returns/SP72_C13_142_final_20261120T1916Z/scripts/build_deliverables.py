"""Rebuild the scholarly apparatus from the main reader's decided reports.

This performs no text recognition or manuscript reading. All inputs are visual
decisions recorded by the readers and adjudicated by the main reader.
"""
from pathlib import Path
import csv, json, html, collections

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parent
PREFIX='SP72_C13_142'
reports=[]
for p in sorted((OUT/'documentation/decided').glob('scan*.json')):
    reports.append(json.loads(p.read_text()))
crop_manifest={m['file']:m for m in (json.loads(s) for s in (OUT/'crops/crop_manifest.jsonl').read_text().splitlines())}
ERROR_CATEGORIES=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']

def crop_evidence(c):
    path=c.get('crop')
    if path and path!='page':
        m=crop_manifest.get(path,{})
        return f"Crop: {path}; crop box in original pixels {m.get('box',c.get('evidence_crop_box',c.get('box','')))}; rotation {m.get('rotation',0)} degrees; place box {c.get('box','')}."
    return f"Page/half view; place box in original pixels {c.get('box','')}."

def text(v):
    if isinstance(v,str): return v
    if isinstance(v,list): return '\n'.join(text(x) for x in v)
    if isinstance(v,dict): return '; '.join(f'{k}: {text(x)}' for k,x in v.items())
    return str(v)

def cell(v):
    return text(v).replace('|','\\|').replace('\n','<br>')

def code(v):
    return '<code>'+html.escape(text(v)).replace('|','&#124;').replace('\n','<br>')+'</code>'

def table(headers, rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)

def write_tsv(name,headers,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',extrasaction='ignore')
        w.writeheader()
        for r in rows:w.writerow({k:text(r.get(k,'')) for k in headers})

all_changes=[dict(c,scan=r['scan']) for r in reports for c in r.get('changes',[]) if c.get('c_changed') or c.get('h_changed')]
summary=[]
for r in reports:
    cc=[c for c in all_changes if c['scan']==r['scan']]
    summary.append([f"{r['scan']:03}",sum(bool(c.get('c_changed')) for c in cc),sum(bool(c.get('h_changed')) for c in cc),*[sum(c.get('confidence')==conf for c in cc) for conf in ['high','medium','low']]])
summary.append(['Total',sum(x[1] for x in summary),sum(x[2] for x in summary),sum(x[3] for x in summary),sum(x[4] for x in summary),sum(x[5] for x in summary)])
md='# Consolidated changes — SP72_C13_142\n\nCounts refer to substantive reading places, not tokens. A place can differ from both witnesses. Macro syntax alone and certainty alone are excluded. The confidence counts count each recorded place once. Archive scan numbers run from 077 through 100; H page numbers are one less.\n\n'
md+=table(['Scan','Changes against C','Changes against H','High','Medium','Low'],summary)
md+='\n## Consequential corrections\n\n'
conseq=[c for c in all_changes if c.get('consequential')]
md+=''.join(f"- Scan {c['scan']:03}, {c['place']}: {code(c['final'])}. {cell(c.get('math_note') or c['scan_shows'])}\n" for c in conseq) or 'None identified so far.\n'
for r in reports:
    md+=f"\n## Scan {r['scan']:03}\n\n"
    rows=[]
    for c in r.get('changes',[]):
        if not(c.get('c_changed') or c.get('h_changed')):continue
        evidence=c['scan_shows']
        evidence+=' '+crop_evidence(c)
        if c.get('main_review'): evidence+=' Main review: '+c['main_review']
        rows.append([cell(c.get('id','')+' — '+c['place']),code(c.get('c','')),code(c.get('h','')),code(c['final']),cell(evidence),c['confidence']])
    md+=table(['Place','Witness C','Witness H','Final reading','What the scan shows','Confidence'],rows)
    md+='\n### Remaining doubts\n\n'
    doubts=r.get('doubts',[])
    md+=''.join(f"- {d['place']}: {code(d['reading'])}; {cell(d.get('reason',''))} ({d['confidence']}).\n" for d in doubts) or 'None.\n'
(OUT/f'{PREFIX}_changes.md').write_text(md)

collation=[]
for c in all_changes:
    if not c.get('h_changed'):continue
    collation.append(dict(folder='142',their_page=c['scan']-1,our_scan=c['scan'],line=c['place'],their_reading=c.get('h',''),codex_reading=c.get('c',''),final_reading=c['final'],scan_shows=c['scan_shows']+' '+crop_evidence(c),kind=c['kind'],marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
write_tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)

decisions={}
for r in reports:
    for d in r.get('decisions',[]):
        d=dict(d)
        d['what the ink shows']=d.get('what_the_ink_shows',d.get('what the ink shows',''))
        decisions[d['id']]=d
with (ROOT/'source/SP72_C13_142_texts/MARKS.tsv').open() as f:
    marks=list(csv.DictReader(f,delimiter='\t'))
write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],[decisions[m['id']] for m in marks if m['id'] in decisions])

inventory=[i for r in reports for i in r.get('inventory',[])]
with (OUT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore')
    w.writeheader()
    for row in inventory:w.writerow(row)

notation=[]
canonical_notation=OUT/'documentation/notation_final.json'
if canonical_notation.exists():
    for n in json.loads(canonical_notation.read_text()):
        notation.append([code(n.get('sign','')),code(n.get('reading','')),cell(n.get('pages','')),cell(n.get('evidence',''))])
else:
    for r in reports:
        for n in r.get('notation',[]):
            row=[code(n.get('sign','')),code(n.get('reading','')),cell(n.get('pages',r['scan'])),cell(n.get('evidence',''))]
            if row not in notation:notation.append(row)
notation_md='# Notation table — SP72_C13_142\n\n'+table(['Written sign / form','Transcription / interpretation','Scans','Evidence and limits'],notation)
(OUT/'notation.md').write_text(notation_md)
doubts_md=notation_md+'\n## Remaining doubts\n\n'
doubts_md+=table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],[[f"{r['scan']:03}",cell(d['place']),code(d['reading']),code(d.get('alternatives','')),d['confidence'],cell(d.get('reason',''))] for r in reports for d in r.get('doubts',[])])
doubts_md+='\n## Certainty-only decisions\n\nThese records resolve, narrow or retain uncertainty without adding a substantive witness difference. Some retain an explicit alternative or an unknown illegible-word count; they are also listed among the remaining doubts when unresolved.\n\n'
doubts_md+=table(['Scan','Place','Reading','Confidence','Reason'],[[f"{r['scan']:03}",cell(d['place']),code(d['reading']),d['confidence'],cell(d.get('reason',''))] for r in reports for d in r.get('certainty_decisions',[])])
live_mark_ids={m['id'] for m in marks}
extra_decisions=[(r,d) for r in reports for d in r.get('decisions',[]) if d['id'] not in live_mark_ids]
doubts_md+='\n## Supplementary decisions\n\nThese records include C doubts in cancelled text, which are outside the supplied live-text MARKS.tsv, and newly identified uncertain places. They are kept separate from the 175 ordered live-mark rows in decisions.tsv. An absent-reading label records removal of unsupported text and is not inserted into the manuscript.\n\n'
doubts_md+=table(['Scan','Id / place','Decision','Reading','What the ink shows','Evidence','Confidence'],[[f"{r['scan']:03}",cell(d['id']),cell(d['decision']),code(d['reading']),cell(d.get('what_the_ink_shows',d.get('what the ink shows',''))),cell(d.get('crop','')),d['confidence']] for r,d in extra_decisions])
doubts_md+='\n## Abbreviations\n\nExpansions are explanatory and are not substituted into the transcription.\n\n'
abbr=collections.defaultdict(lambda: {'expansion':set(),'scans':set()})
for r in reports:
    for a in r.get('abbreviations',[]):
        abbr[a['form']]['expansion'].add(a['expansion'])
        abbr[a['form']]['scans'].add(r['scan'])
doubts_md+=table(['Form','Proposed expansion','Scans'],[[code(k),cell('; '.join(sorted(v['expansion']))),', '.join(f'{n:03}' for n in sorted(v['scans']))] for k,v in sorted(abbr.items())])
assessment=OUT/'documentation/legibility_assessment.md'
doubts_md+='\n## Legibility and comparison of witnesses\n\n'+(assessment.read_text() if assessment.exists() else 'Assessment in progress; all surviving uncertainties are retained in the page text and the table above.\n')
(OUT/f'{PREFIX}_doubts.md').write_text(doubts_md)

notes='# Reading notes — SP72_C13_142\n\nThese notes distinguish what the manuscript states from mathematical checks actually performed. No outside source has been consulted. Scan numbers identify the supplied archive images; authorial and later page numbers are reported separately. The supplied error sheet names the paper watermark EXTRA STRONG; watermark impressions and bleed-through are excluded from the manuscript text.\n'
for r in reports:
    page_notes=r.get('notes','')
    if isinstance(page_notes,list):page_notes='\n\n'.join(text(n) for n in page_notes)
    notes+=f"\n## Scan {r['scan']:03}\n\n"+text(page_notes)+'\n'
    math=[c for c in r.get('changes',[]) if c.get('math_note')]
    if math:
        notes+='\n### Mathematics and reading decisions\n\n'+''.join(f"- {c['place']}: C {code(c.get('c',''))}; H {code(c.get('h',''))}; ink {code(c['final'])}. {c['math_note']}\n" for c in math)
    if r.get('audit_note'):notes+='\n### Second reading\n\n'+text(r['audit_note'])+'\n'
(OUT/f'{PREFIX}_notes.md').write_text(notes)
events=[e for r in reports for e in r.get('check_events',[])]
write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)

hand='# Hand log — SP72_C13_142\n\nA habit is a visual aid, not authority to regularize a clearly different written form. Scope statements below distinguish a verified recurrence from an observation at a single place.\n\n'
hand+=table(['Habit / notation','Pages','Scope across occurrences','Witness misreadings'],[[cell(h['habit']),cell(h.get('pages',r['scan'])),cell(h.get('scope','')),cell(h.get('witness_errors',''))] for r in reports for h in r.get('hand_log',[])])
(OUT/f'{PREFIX}_hand_log.md').write_text(hand)

cats=collections.Counter(c.get('category','Other') for c in all_changes)
assert not set(cats)-set(ERROR_CATEGORIES), 'Noncanonical error-sheet category: '+str(set(cats)-set(ERROR_CATEGORIES))
feedback='# Error-sheet feedback — SP72_C13_142\n\nThe unit is a recorded substantive place that differs from at least one witness, counted once under its primary cause. These are observed corrections or retained disagreements, not an estimated error rate over all manuscript tokens. Certainty-only decisions are excluded; they appear in the doubts file, with the listed C marks also recorded in decisions.tsv.\n\n'
feedback+=table(['Error-sheet category','Places'],[[cell(k),cats[k]] for k in ERROR_CATEGORIES])
feedback+='\nThe complete [category and location index](documentation/error_category_index.tsv) lists every counted comparison place with its scan, identifier, witness flags and confidence. The changes log supplies the readings and image evidence for each identifier.\n'
category_rows=[dict(category=c.get('category','Other'),scan=f"{c['scan']:03}",comparison_id=c['id'],place=c['place'],changes_against_C='yes' if c.get('c_changed') else 'no',changes_against_H='yes' if c.get('h_changed') else 'no',confidence=c['confidence']) for c in all_changes]
write_tsv('documentation/error_category_index.tsv',['category','scan','comparison_id','place','changes_against_C','changes_against_H','confidence'],category_rows)
feedback+='\n## Further recurrent difficulties\n\n'+text([r.get('feedback_extra','') for r in reports if r.get('feedback_extra')])+'\n'
feedback_final=OUT/'documentation/feedback_additions.md'
if feedback_final.exists():feedback+='\n'+feedback_final.read_text()+'\n'
(OUT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)

combined='\\cotefile{142}\n\n'+'\n\n'.join((OUT/'pages'/f"142_scan{r['scan']:03}.tex").read_text().rstrip() for r in reports)+'\n'
(OUT/f'{PREFIX}_transcription.tex').write_text(combined)
print(json.dumps({'pages':len(reports),'changes':len(all_changes),'against_C':sum(bool(c.get('c_changed')) for c in all_changes),'against_H':len(collation),'marks_decided':sum(m['id'] in decisions for m in marks),'supplementary_decisions':len(decisions)-sum(m['id'] in decisions for m in marks),'inventory_elements':len(inventory),'check_events':len(events)},indent=2))
