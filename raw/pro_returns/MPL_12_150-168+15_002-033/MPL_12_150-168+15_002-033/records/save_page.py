from pathlib import Path
from datetime import datetime, timezone
import csv, json
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_12_150-168+15_002-033'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(cote, scan, tex, elements, doubts=(), notes='', sheet_kind='text', notation=()):
    dest=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03}.tex'
    if dest.exists(): raise RuntimeError('Page already exists; revise explicitly.')
    dest.write_text(tex.strip()+'\n')
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,pos,words) in enumerate(elements,1):
            w.writerow([cote,scan,sheet_kind,f'{cote}.{scan:03}.{i:02}',kind,pos,words,'yes'])
    record={'cote':cote,'scan':scan,'doubts':list(doubts),'notation':list(notation)}
    with (ROOT/'records/readings.jsonl').open('a') as f: f.write(json.dumps(record,ensure_ascii=False)+'\n')
    if notes:
        with (ROOT/'records/precontext_observations.md').open('a') as f: f.write(f'\n## Cote {cote}, scan {scan}\n\n{notes}\n')
    render_doubts()
    with (ROOT/'progress.log').open('a') as f: f.write(f'{cote} scan {scan:03} done {utc()}\n')
    print(dest.name, len(tex), 'characters;',len(elements),'inventory elements;',utc())
def render_doubts():
    records=[json.loads(s) for s in (ROOT/'records/readings.jsonl').read_text().splitlines()]
    lines=['# Notation table','', '| Sign or usage | LaTeX | First observed / qualification |','|---|---|---|']
    for r in records:
        for sign,latex,qualification in r['notation']:
            lines.append('| '+ ' | '.join(str(x).replace('|','&#124;') for x in [sign,latex,f"{r['cote']}, scan {r['scan']}: {qualification}"] )+' |')
    lines += ['','# Doubt register','', 'This register is supplemented by every in-place `\\unsure` or `\\illegible` in the page files. Approximate lines refer to visual reading order, including displays.','', '| Cote | Scan | Approximate line / position | Reading | Alternative(s) | Confidence | Comment |','|---|---|---|---|---|---|---|']
    for r in records:
        for d in r['doubts']:
            vals=[r['cote'],r['scan'],*d]
            lines.append('| '+' | '.join(str(x).replace('|','&#124;').replace('\n',' ') for x in vals)+' |')
    lines += ['','# Abbreviations','', 'The expansions below are editorial hypotheses, not expansions made in the transcription.','', '| Abbreviation | Probable expansion |','|---|---|','| cat. | catégorie |','| f. et s. | faut et suffit |','| comp. conn. | composantes connexes |','| alg. clos. | algébriquement clos |','','# Legibility and reliability','', 'Work in progress. The handwriting contains heavily compressed words, retraced mathematical signs, and occasional crowded interlinear additions. Doubt marks are retained wherever the ink does not decide a reading. No OCR is used; no contextual material has been read.']
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(lines)+'\n')
