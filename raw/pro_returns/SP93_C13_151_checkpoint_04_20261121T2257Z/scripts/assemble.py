"""Assemble the edition from page reports approved by the main reader.

This script never infers manuscript readings. All readings and evidence are
supplied by the human-visible image-reading reports and main-reader review.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import hashlib
import json

ROOT = Path('/workspace/scratch/d12e26a9cd50')
OUT = ROOT / 'SP93_C13_151_work'
PREFIX = 'SP93_C13_151'

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def table(path, fields, rows, delimiter='\t'):
    with path.open('w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=delimiter, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

def md(value):
    if value is None:
        return '— (no H for this scan)'
    return str(value).replace('|', '&#124;').replace('\n', '<br>')

def as_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return '\n\n'.join(as_text(v) for v in value)
    return json.dumps(value, ensure_ascii=False)

def evidence(row):
    s = row.get('evidence', '')
    coords = row.get('pixel_box', row.get('box'))
    if row.get('crop'):
        s += f" Crop: `{row['crop']}`; original box {coords}."
    elif coords:
        s += f" Native-half observation; original box {coords}."
    return s

def assemble():
    reports = [json.loads(p.read_text()) for p in sorted((OUT / 'reviews').glob('151_scan[0-9][0-9][0-9].json'))]
    counts = Counter()
    change_lines = ['# SP93_C13_151 — changes against the two draft witnesses', '',
        'Each row concerns a reading or a diplomatic state, not macro syntax. The scan is the authority. '
        'Confidence describes the reading of the visible ink, not the mathematical truth of the statement.', '',
        '| Scan | Rows | Against C | Against H | High | Medium | Low |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for r in reports:
        c = r['changes']
        conf = Counter(x['confidence'] for x in c)
        a = sum(bool(x.get('differs_C')) for x in c)
        b = sum(bool(x.get('differs_H')) for x in c)
        counts.update(rows=len(c), C=a, H=b, **conf)
        change_lines.append(f"| {r['scan']} | {len(c)} | {a} | {b} | {conf['high']} | {conf['medium']} | {conf['low']} |")
    change_lines += [f"| **Total** | **{counts['rows']}** | **{counts['C']}** | **{counts['H']}** | **{counts['high']}** | **{counts['medium']}** | **{counts['low']}** |", '',
        '## Consequential mathematical corrections', '']
    consequential = [(r['scan'], c) for r in reports for c in r['changes'] if c.get('consequential')]
    change_lines += [f"- Scan {s}, {c['place']}: {c['consequential']}" for s, c in consequential] or ['None recorded in the pages completed so far.']
    collation, inventory, decisions, checks, coverage = [], [], [], [], []
    notes = ['# SP93_C13_151 — notes while reading', '',
        'These notes describe only the supplied sheets. No external literature was researched. '
        'Descriptions of a manuscript claim are not assertions that it has been proved. '
        'CHECK_EVENTS.tsv separately records the reasoning actually performed.', '']
    doubts = ['# SP93_C13_151 — notation, doubts and abbreviations', '', '## Notation table', '',
        '| Notation | LaTeX representation | Ink evidence | Scope |', '|---|---|---|---|']
    notations, abbreviations, hands = [], [], []
    for r in reports:
        scan = str(r['scan']).zfill(3)
        change_lines += ['', f'## Scan {scan}', '', '| ID / place | Witness C | Witness H | Consolidated reading | What the scan shows | Confidence |', '|---|---|---|---|---|---|']
        for c in r['changes']:
            change_lines.append('| ' + ' | '.join(md(x) for x in [f"{c['id']} — {c['place']}", c.get('C'), c.get('H'), c['final'], evidence(c), c['confidence']]) + ' |')
            if c.get('differs_H'):
                collation.append(dict(folder='151', their_page=int(scan)-1, our_scan=int(scan), line=c['place'],
                    their_reading=c.get('H', ''), codex_reading=c.get('C', ''), final_reading=c['final'], scan_shows=evidence(c),
                    kind=c['kind'], marked_in_H=c.get('marked_in_H', 'unknown'), confidence=c['confidence']))
        change_lines += ['', '### Still unresolved', '']
        change_lines += [f"- {d['place']}: `{d['reading']}` — {d.get('reason', '')}" for d in r.get('doubts', [])] or ['None recorded.']
        if r.get('second_adjudications'):
            change_lines += ['', '### Blind second reading: adjudications', '',
                'The first reading was written before the blind reading and is preserved unchanged in `second/`. '
                'This table records every token-level disagreement, including equivalent notation. '
                'The main changes table above counts final departures from the witnesses, not repeated decisions on the same place.', '',
                '| Box | First reading | Blind second reading | Final decision | Evidence / crop | Changed |',
                '|---|---|---|---|---|---|']
            for a in r['second_adjudications']:
                change_lines.append('| ' + ' | '.join(md(x) for x in [a['box'],a['first'],a['second'],a['final'],evidence(a),a['changed']]) + ' |')
        for x in r['inventory']:
            inventory.append(dict(scan=scan, sheet_kind=r['sheet_kind'], hand=x.get('hand', r['hand']), **{k:v for k,v in x.items() if k!='hand'}))
        for d in r['decisions']:
            decisions.append(dict(id=d['id'], cote='151', scan=int(scan), decision=d['decision'], reading=d['reading'],
                **{'what the ink shows':d.get('ink','')}, crop=f"{d.get('crop','page')}; {d.get('box','page')}", confidence=d['confidence']))
        notes += [f'## Scan {scan}', '', as_text(r.get('notes', '')), '']
        checks += r.get('check_events', [])
        notations += [(scan,x) for x in r.get('notation', [])]
        abbreviations += [(scan,x) for x in r.get('abbreviations', [])]
        hands += [(scan,x) for x in r.get('hand_log', [])]
        for c in r.get('difference_coverage', []):
            coverage.append(dict(scan=scan, **c))
    for scan, n in notations:
        doubts.append('| ' + ' | '.join(md(x) for x in [n.get('notation',''), n.get('representation',''), n.get('evidence',''), f"Scan {scan}: {n.get('scope','')}"]) + ' |')
    consistency = OUT/'reviews/notation_consistency.md'
    if consistency.exists():
        doubts += ['', '## Cross-page consistency review', '', consistency.read_text()]
    doubts += ['', '## Remaining doubts', '', '| Scan | Place | Reading | Alternatives | Confidence | Reason |', '|---|---|---|---|---|---|']
    for r in reports:
        for d in r.get('doubts', []):
            doubts.append('| ' + ' | '.join(md(x) for x in [r['scan'], d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')]) + ' |')
    doubts += ['', '## Abbreviations (expansions are editorial and occur only here)', '', '| Scan | Written form | Suggested expansion | Place |', '|---|---|---|---|']
    for scan, a in abbreviations:
        doubts.append('| ' + ' | '.join(md(x) for x in [scan,a.get('written',''),a.get('expansion',''),a.get('place','')]) + ' |')
    legibility = OUT/'reviews/legibility.md'
    doubts += ['', '## Legibility and comparison of the witnesses', '', legibility.read_text() if legibility.exists() else 'Assessment is in progress; see the page-specific unresolved readings above.']
    hand_lines = ['# SP93_C13_151 — hand log', '', '| Scan | Habit | Places | Consistency on inspected pages | Witness misreadings |', '|---|---|---|---|---|']
    for scan,h in hands:
        hand_lines.append('| ' + ' | '.join(md(x) for x in [scan,h.get('habit',''),h.get('places',''),h.get('consistency',''),h.get('witness_errors','')]) + ' |')
    feedback_counts = Counter(c['kind'] for r in reports for c in r['changes'])
    feedback = ['# SP93_C13_151 — error-sheet feedback', '', 'Counts concern distinct logged places; a place is assigned its principal kind. Macro-only differences are excluded.', '',
        '| Error-sheet kind | Logged places |', '|---|---:|']
    mapping = [('Symbols and indices',['misread symbol or index']),('Words',['misread word']),('Omissions',['omission']),
        ('Drawings and diagrams',['drawing or diagram']),('Readable ink left as illegible',['readable ink left as \\ill{}']),
        ('Insertions and placement',['insertion or placement']),('Struck text',['deletion state']),
        ('Abbreviations expanded or spelling modernised',['abbreviation expanded or spelling modernised']),
        ('Text not on the page',['text not on the page']),('Other',['other'])]
    for label, cats in mapping:
        feedback.append(f"| {label} | {sum(feedback_counts[c] for c in cats)} |")
    extra = OUT/'reviews/feedback_extra.md'
    feedback += ['', '## Recurring observations', '', extra.read_text() if extra.exists() else 'See the hand log for the page-by-page observations; synthesis is in progress.']
    for name, lines in [('changes',change_lines),('notes',notes),('doubts',doubts),('hand_log',hand_lines),('sheet_feedback',feedback)]:
        (OUT/f'{PREFIX}_{name}.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    table(OUT/f'{PREFIX}_collation.tsv', ['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    table(OUT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    table(OUT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],sorted(decisions,key=lambda d:int(d['id'][1:])))
    table(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    table(OUT/f'{PREFIX}_difference_coverage.tsv',['scan','id','disposition','changes_ids','explanation'],coverage)
    combined = ('\\cotefile{151}\n\n' if reports else '')+'\n\n'.join((OUT/'pages'/f"151_scan{str(r['scan']).zfill(3)}.tex").read_text().rstrip() for r in reports)+'\n'
    (OUT/f'{PREFIX}_transcription.tex').write_text(combined,encoding='utf8')
    print(json.dumps({'pages':len(reports),'changes':dict(counts),'decisions':len(decisions),'collation':len(collation),'inventory':len(inventory)},ensure_ascii=False))

def commit(scan, preserve_first=False):
    scan = f'{int(scan):03d}'
    report_path = OUT/'reports'/f'151_scan{scan}.json'
    report = json.loads(report_path.read_text())
    if not report.get('root_reviewed'):
        raise ValueError('Root must explicitly set root_reviewed after examining the images.')
    existing = (OUT/'reviews'/report_path.name).exists()
    (OUT/'reviews'/report_path.name).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (OUT/'pages'/f'151_scan{scan}.tex').write_text((OUT/'reports'/f'151_scan{scan}.tex').read_text())
    boxes = report.get('second_boxes',[])
    if not preserve_first:
        table(OUT/'second'/f'151_scan{scan}_boxes.tsv',['box','kind','x0','y0','x1','y1'],boxes)
        table(OUT/'second'/f'151_scan{scan}_first.tsv',['box','reading'],boxes)
    assemble()
    if not existing:
        crops = report.get('crop_count',len(set(c.get('crop') for c in report['changes']+report['decisions'] if c.get('crop') and c['crop']!='page')))
        with (OUT/'progress.log').open('a') as f:
            f.write(f"scan {scan} done {stamp()} cote 151: {report['lines_read']} lines read, {crops} places cropped, {len(report['changes'])} rows\n")

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--commit'); p.add_argument('--preserve-first',action='store_true')
    a = p.parse_args()
    if a.commit: commit(a.commit,a.preserve_first)
    else: assemble()
