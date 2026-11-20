from pathlib import Path
import csv, re, json, shutil

ROOT=Path('/workspace/scratch/ae626167fbca')
SRC=ROOT/'source/SP47_CW_103_witnesses'
WORK=ROOT/'SP47_CW_103_work'
INPUTS=ROOT/'reader_inputs'
INPUTS.mkdir(exist_ok=True)
rows=list(csv.DictReader((SRC/'page_map.tsv').open(),delimiter='\t'))
hua=(SRC/'hua/transcripts/103/batch-01.fr.tex').read_text()
marks=list(re.finditer(r'^\\page\{(\d+)\}',hua,re.M))
sections={int(m.group(1)):hua[m.start():marks[i+1].start() if i+1<len(marks) else len(hua)] for i,m in enumerate(marks)}
for row in rows:
    scan=int(row['our_scan']); folder=row['folder']; p=INPUTS/f'scan{scan:03}'
    p.mkdir(exist_ok=True)
    shutil.copy2(SRC/row['codex_file'],p/'C.tex')
    h=sections[int(row['their_page'])]
    h=re.split(r'^\\section\*',h,flags=re.M)[0]
    h=h.replace('\\end{document}','')
    (p/'H.tex').write_text(h)
    cbase=SRC/'codex'/folder
    alerts=[]
    for suffix in ['doubts.md','notes.md']:
        text=(cbase/f'{folder}_{suffix}').read_text()
        alerts.append(f'# Witness C {suffix}: rows relevant to scan {scan}\n')
        for line in text.splitlines():
            if not line.startswith('|'):continue
            cell=line.split('|')[1].strip()
            nums=[int(n) for n in re.findall(r'\d+',cell)]
            include=scan in nums or (len(nums)==2 and ('–' in cell or '-' in cell) and nums[0]<=scan<=nums[1])
            if include:alerts.append(line)
    (p/'C_alerts.md').write_text('\n'.join(alerts)+'\n')
    shutil.copy2(cbase/'PREAMBLE.tex',p/'PREAMBLE.tex')
    (p/'source_paths.json').write_text(json.dumps({**row,'whole':str(ROOT/'source/SP47_CW_103_scans'/f'{folder}_103_scan{scan:03}.jpg'),'half_a':str(ROOT/'source/SP47_CW_103_scans'/f'{folder}_103_scan{scan:03}_a.jpg'),'half_b':str(ROOT/'source/SP47_CW_103_scans'/f'{folder}_103_scan{scan:03}_b.jpg')},indent=2))
print(f'Prepared {len(rows)} page-local witness packets. Images stay in source and are never OCRed.')
