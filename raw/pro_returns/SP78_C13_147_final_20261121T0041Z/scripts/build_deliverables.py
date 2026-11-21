#!/usr/bin/env python3
"""Assemble the reviewed, source-grounded page records without changing page text."""
from pathlib import Path
import csv, json, collections, re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP78_C13_147'

def read_reports():
    return [json.loads(p.read_text()) for p in sorted((ROOT/'reviewed').glob('*.json'))]

def clean(x):
    return str(x).replace('\t',' ').replace('\r',' ').replace('\n',' ')

def cell(x):
    return clean(x).replace('|','\\|')

def md_table(headers, rows):
    out = ['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']
    out.extend('| '+' | '.join(cell(v) for v in row)+' |' for row in rows)
    return '\n'.join(out)+'\n'

def write_tsv(name, fields, rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        w.writeheader()
        for r in rows: w.writerow({k:clean(r.get(k,'')) for k in fields})

def evidence(c):
    loc = c.get('crop','')
    box = c.get('box',[])
    return c.get('evidence','')+(f' Crop: `{loc}`; original box {tuple(box)}.' if loc else '')

def main():
    (ROOT/'reviewed').mkdir(exist_ok=True)
    reports=read_reports()
    all_changes=[c for r in reports for c in r.get('changes',[])]
    counts=[]
    for r in reports:
        cs=r.get('changes',[]); confid=collections.Counter(c.get('confidence','') for c in cs)
        counts.append([f"{r['scan']:03}",len(cs),sum(bool(c.get('against_C')) for c in cs),sum(bool(c.get('against_H')) for c in cs),confid['high'],confid['medium'],confid['low']])
    counts.append(['TOTAL']+[sum(x[i] for x in counts) for i in range(1,7)])
    changes=[f'# {PREFIX}: changes against the two witnesses\n',
      'Only substantive readings are counted. A row may differ from both witnesses and then contributes to both witness totals. Macro wrappers alone and certainty-only refinements are excluded, including reordering or narrowing pre-existing candidates while the reading remains unresolved. Resolutions of indexed doubts are separately recorded in `decisions.tsv`.\n',
      md_table(['Scan','Rows','Against C','Against H','High','Medium','Low'],counts),
      '## Consequential corrections\n']
    consequences=[f"- Scan {r['scan']:03}, {c['place']}: `{c['C']}` / `{c['H']}` → `{c['final']}`. {c.get('evidence','')}" for r in reports for c in r.get('changes',[]) if c.get('consequential')]
    changes.append('\n'.join(consequences) if consequences else 'No consequential correction has yet been approved.')
    collation=[]; decisions=[]; inventory=[]; notes=[]; checks=[]; doubts=[]; hands=[]; abbreviations=[]
    for r in reports:
        n=r['scan'];cs=r.get('changes',[])
        changes.append(f'\n## Scan {n:03}\n')
        changes.append(md_table(['Place','C','H','Consolidated reading','What the scan shows','Confidence'],[[c['place'],c['C'],c['H'],c['final'],evidence(c),c['confidence']] for c in cs]))
        changes.append('### Unresolved places\n')
        unresolved=r.get('unresolved',[])
        changes.append('\n'.join('- '+x for x in unresolved) if unresolved else 'No unresolved place recorded.')
        if r.get('audit_complete'):
            changes.append('### Independent second reading\n')
            changes.append(r.get('audit_summary','The independent reading and adjudication are recorded in second/.'))
            if r.get('audit_changes'):
                changes.append(md_table(['Box / place','First reading','Independent reading','Final reading','Decision and evidence'],[
                    [a.get('box',''),a.get('first',''),a.get('second',''),a.get('final',''),a.get('evidence','')]
                    for a in r['audit_changes']]))
            else:
                changes.append('No transcription change was required by the independent comparison. See the box-level adjudications in second/.')
        for c in cs:
            if c.get('against_H'):
                collation.append(dict(folder=147,their_page=n-1,our_scan=n,line=c['place'],their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],scan_shows=evidence(c),kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
        for d in r.get('decisions',[]):
            decisions.append({**d,'what the ink shows':d.get('ink',d.get('what the ink shows',''))})
        inventory.extend(r.get('inventory',[]))
        notes.append(f'## Scan {n:03}\n')
        for i,note in enumerate(r.get('notes',[]),1):
            notes.append(f'**147-{n:03}-N{i}.** {note}\n')
        review_note=r.get('root_review_notes',r.get('root_review_note',''))
        if review_note: notes.append('**Main-reader review.** '+review_note+'\n')
        if r.get('witness_comparison'):notes.append('**Witness comparison.** '+r['witness_comparison']+'\n')
        checks.extend(r.get('check_events',[]))
        for d in r.get('doubts',[]):doubts.append([f'{n:03}',d.get('place',''),d.get('reading',''),d.get('alternatives',''),d.get('confidence',''),d.get('reason','')])
        for h in r.get('hand_log',[]):hands.append([h.get('habit',''),', '.join(str(p) for p in h.get('pages',[n])),h.get('all_occurrences',''),h.get('witness_misreadings','')])
        abbreviations.extend(r.get('abbreviations',[]))
    (ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(changes)+'\n')
    write_tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],sorted(decisions,key=lambda d:int(re.sub(r'\D','',d['id']))))
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');w.writeheader();w.writerows(inventory)
    (ROOT/f'{PREFIX}_notes.md').write_text(f'# {PREFIX}: notes while reading\n\nThe statements below describe these manuscript pages. They are not attributed to external publications. A reading or summary does not constitute a proof check; actual uses, checks and background status are recorded in CHECK_EVENTS.tsv.\n\n'+'\n'.join(notes))
    write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    notation=(ROOT/'notation.md').read_text()
    seen=set();abrows=[]
    for a in abbreviations:
        t=(a.get('written',''),a.get('expansion',''))
        if t not in seen:abrows.append(t);seen.add(t)
    legibility=(ROOT/'legibility.txt').read_text() if (ROOT/'legibility.txt').exists() else 'The reading is in progress. Remaining doubts are retained explicitly; no claim of complete verification is made before the second readings.'
    (ROOT/f'{PREFIX}_doubts.md').write_text(f'# {PREFIX}: notation and doubts\n\n'+notation+'\n## Remaining doubts\n\n'+md_table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions here are explanatory only; they do not replace the manuscript forms in the transcription.\n\n'+md_table(['Written','Possible expansion'],abrows)+'\n## Legibility and witnesses\n\n'+legibility+'\n')
    (ROOT/f'{PREFIX}_hand_log.md').write_text(f'# {PREFIX}: hand log\n\nObservations are restricted to the pages listed. A local resemblance is not assumed to be an invariant of the writer’s hand.\n\n'+md_table(['Habit or notation','Scans','Scope / all occurrences','Witness errors'],hands))
    categories=['symbols and indices','words','omissions','drawings and diagrams','readable ink left as illegible','insertions put in wrong place','struck text','abbreviations expanded spelling modernised','text not on page','other']
    catrows=[]
    for cat in categories:
        places=[f"{r['scan']:03}: {c['place']}" for r in reports for c in r.get('changes',[]) if c.get('error_sheet_kind','other')==cat]
        catrows.append([cat,len(places),'; '.join(places)])
    extra=(ROOT/'feedback_extra.md').read_text() if (ROOT/'feedback_extra.md').exists() else 'No additional recurring class has yet been established.'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(f'# {PREFIX}: feedback on the error sheet\n\nCounts are of logged substantive places classified by their primary error-sheet category, not of all occurrences of a glyph. A place differing from both witnesses is counted once.\n\n'+md_table(['Kind','Places','Locations'],catrows)+'\n## Additional recurring errors\n\n'+extra+'\n')
    pages=sorted((ROOT/'pages').glob('147_scan*.tex'))
    if pages:(ROOT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{147}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n')
    print(json.dumps({'approved_pages':len(reports),'page_files':len(pages),'changes':len(all_changes),'collation':len(collation),'mark_decisions':len(decisions),'inventory_elements':len(inventory)},ensure_ascii=False))

if __name__=='__main__':main()
