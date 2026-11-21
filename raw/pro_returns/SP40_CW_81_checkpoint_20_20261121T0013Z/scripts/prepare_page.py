"""Rebuild a one-page reader packet from the original attached witness tree.

This is text extraction from supplied transcriptions, never OCR of manuscript ink.
Run only for the next page after the preceding page's commit is logged.
"""
from pathlib import Path
import csv, json, re, shutil, sys

OUT = Path(__file__).resolve().parents[1]
BASE = OUT.parent
WIT = BASE / 'source/SP40_CW_81_witnesses'
SCANS = [2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
n = int(sys.argv[1])
assert n in SCANS
if SCANS.index(n):
    previous = SCANS[SCANS.index(n)-1]
    assert f'scan {previous:03d} done ' in (OUT/'progress.log').read_text(), 'Previous page is not committed'
rows = list(csv.DictReader((WIT/'page_map.tsv').open(), delimiter='\t'))
row = next(r for r in rows if int(r['our_scan']) == n)
p = BASE/'packets'/f'{n:03d}'
p.mkdir(parents=True, exist_ok=True)
shutil.copyfile(WIT/row['codex_file'], p/'C.tex')
htext = ''
if row['hua_file'] and row['hua_has'] != 'nothing':
    whole = (WIT/row['hua_file']).read_text()
    matches = list(re.finditer(r'\\page\{(\d+)\}', whole))
    for i, m in enumerate(matches):
        if int(m.group(1)) == int(row['their_page']):
            htext = whole[m.start():matches[i+1].start() if i+1 < len(matches) else len(whole)].rstrip()+'\n'
            break
(p/'H.tex').write_text(htext)
(p/'metadata.json').write_text(json.dumps(row, ensure_ascii=False, indent=2)+'\n')
if 15 <= n <= 22:
    sweep = BASE/'source/SP40_CW_81_sweep3/readings/cote81_CORRECTIONS.tsv'
    sweep_row = next(r for r in csv.DictReader(sweep.open(), delimiter='\t') if r['id'] == 'SA01-K81-06')
    scope = 'The row spans scans015–022 and its recorded author explicitly viewed no scan. It supplies witness proposals only. Its examples concern Sigma/U closure bars; do not invent an example or a current C/H omission on scan018. The separately qualified possible bar over corrected E_i must be decided locally from ink and retains its actual C doubt identity.' if n == 18 else 'The row spans scans015–022 and its recorded author explicitly viewed no scan. It supplies witness proposals only. Match each example to this page locally; do not infer an unobserved bar or a current C/H omission from the broad scan range.'
    (p/'S_rows.json').write_text(json.dumps({'source':str(sweep.relative_to(BASE)), 'rows':[sweep_row], 'scope_note':scope}, ensure_ascii=False, indent=2)+'\n')
folder = WIT/'codex'/row['folder']
for suffix, dest in [('doubts.md','C_doubts.txt'), ('notes.md','C_notes.txt')]:
    original = folder/(row['folder']+'_'+suffix)
    lines = original.read_text().splitlines()
    selected = []
    section = None
    emitted_section = None
    table_heading = []
    for line in lines:
        if line.startswith('#'):
            section = line
            table_heading = []
        if re.match(r'^\|\s*Scan\s*\|', line, re.I):
            table_heading = [line]
        elif table_heading and re.match(r'^\|[ :|\-]+\|?$', line):
            table_heading.append(line)
        target = (re.match(r'^\|\s*'+str(n)+r'\s*\|', line)
                  or re.match(r'^(?:-\s*)?\*\*Scan '+str(n)+r'[. :*]', line))
        if target:
            if section != emitted_section:
                if selected:selected.append('')
                if section:selected.append(section)
                selected.extend(table_heading)
                emitted_section = section
            selected.append(line)
    (p/dest).write_text('\n'.join(selected)+'\n')
inv = list(csv.DictReader((folder/(row['folder']+'_inventory.csv')).open()))
selected_inv = [r for r in inv if str(r.get('scan',r.get('scanpage',''))) == str(n)]
(p/'C_inventory.json').write_text(json.dumps(selected_inv, ensure_ascii=False, indent=2)+'\n')
shutil.copyfile(OUT/'notation.md', p/'notation.md')
shutil.copyfile(OUT/'notation.md', OUT/'briefs'/f'notation_scan{n:03d}.md')
for role in 'ABC':
    (OUT/'readers'/f'{n:03d}'/role).mkdir(parents=True, exist_ok=True)
print(json.dumps({'scan':n,'packet':str(p),'folder':row['folder'],'hua_has':row['hua_has']}))
