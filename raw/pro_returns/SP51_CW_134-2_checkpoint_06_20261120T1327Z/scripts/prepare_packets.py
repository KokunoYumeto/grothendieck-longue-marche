from pathlib import Path
import csv, re, json, shutil
from datetime import datetime, timezone

BASE=Path('/workspace/scratch/8db4dde48936')
OUT=BASE/'result'
W=BASE/'source/SP51_CW_134-2_witnesses'
S=BASE/'source/SP51_CW_134-2_scans'
for d in ['pages','records','briefs','crops','scripts']:
    (OUT/d).mkdir(parents=True,exist_ok=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if not (OUT/'progress.log').exists():
    (OUT/'progress.log').write_text(now+'\nSecond pass begun; 16 scans, 170–185; independent fresh readers A/B/C for every scan.\n',encoding='utf-8')
    (OUT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n',encoding='utf-8')
    (OUT/'notation.md').write_text('# Working notation table\n\nNo entries yet. Build readings from scan 170 onward; every entry remains subject to the next page’s ink.\n',encoding='utf-8')
shutil.copyfile(W/'codex/H134-05/PREAMBLE.tex', OUT/'PREAMBLE.tex')
for row in csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'):
    n=row['our_scan']; folder=row['folder']; dest=BASE/'packets'/n
    dest.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(W/row['codex_file'],dest/'C.tex')
    h=(W/row['hua_file']).read_text()
    m=re.search(r'\\page\{'+row['their_page']+r'\}(.*?)(?=\\page\{|\\end\{document\})',h,re.S)
    if not m: raise RuntimeError(n)
    (dest/'H.tex').write_text(m.group(1).strip()+'\n')
    doubts=(W/f'codex/{folder}/{folder}_doubts.md').read_text()
    lines=[l for l in doubts.splitlines() if re.match(r'\|\s*'+n+r'\s*\|',l)]
    notes=(W/f'codex/{folder}/{folder}_notes.md').read_text()
    notes_lines=[]
    for l in notes.splitlines():
        if not l.startswith('|'): continue
        cell=l.split('|')[1].strip()
        include=False
        for token in re.findall(r'\d+(?:[–-]\d+)?',cell):
            ends=re.split('[–-]',token)
            low=int(ends[0]);high=int(ends[-1])
            if low<=int(n)<=high:include=True
        if include:notes_lines.append(l)
    (dest/'C_questions.md').write_text('# Earlier questions for this scan\n\n'+ '\n'.join(lines)+'\n\n# Earlier notes\n\n'+'\n'.join(notes_lines)+'\n')
    row['image_whole']=str(S/f'{folder}_134-2_scan{n}.jpg')
    row['image_a']=str(S/f'{folder}_134-2_scan{n}_a.jpg')
    row['image_b']=str(S/f'{folder}_134-2_scan{n}_b.jpg')
    (dest/'metadata.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
print('Initialized',now,'and extracted exactly 16 page-specific witness packets.')
