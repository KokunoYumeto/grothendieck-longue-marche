from pathlib import Path
import csv, difflib
from page_work import ROOT, PREFIX, FIELDS, utc, rebuild

def audit_page(scan, replacements=(), notes='', extra_elements=()):
    path=ROOT/'pages'/f'{PREFIX}_43_scan{scan:03}.tex'
    record=ROOT/'records'/f'scan{scan:03}_audit.txt'
    if record.exists(): raise RuntimeError('Already audited')
    old=path.read_text(encoding='utf-8'); new=old
    for before,after in replacements:
        if before not in new: raise RuntimeError(f'Missing replacement on {scan}: {before!r}')
        new=new.replace(before,after)
    if new!=old: path.write_text(new,encoding='utf-8')
    with (ROOT/f'{PREFIX}_inventory.csv').open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    old_count=sum(int(r['scan'])==scan for r in rows)
    if extra_elements:
        newrows=[]
        for n,(kind,pos,words) in enumerate(extra_elements,old_count+1):
            sheet=next(r['sheet_kind'] for r in rows if int(r['scan'])==scan)
            newrows.append(dict(cote=43,scan=scan,sheet_kind=sheet,element=f'{scan:03}-{n:02}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
        rows+=newrows; rows.sort(key=lambda r:(int(r['scan']),r['element']))
        with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
    diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='first-reading',tofile='audited'))
    record.write_text('Second visual audit by the sole transcription reader, against scan image.\n'+notes+'\n\n'+(diff or 'No textual change after visual comparison.\n'),encoding='utf-8')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'scan {scan:03} audited {utc()}\n')
    rebuild()
    print(f'Audited {scan:03}; changed={old!=new}; new inventory rows={len(extra_elements)}')
