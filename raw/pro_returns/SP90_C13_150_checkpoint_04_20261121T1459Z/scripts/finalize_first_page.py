"""Commit an explicitly adjudicated page's cumulative records and next assignment.

The editor must first inspect the evidence and write editor/150_scanNNN.json
and pages/150_scanNNN.tex. This helper does not choose readings.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser()
    p.add_argument('scan',type=int)
    p.add_argument('--next-scan',type=int)
    p.add_argument('--reader')
    a=p.parse_args()
    stem=f'150_scan{a.scan:03}'
    meta=ROOT/'editor'/f'{stem}.json'
    page=ROOT/'pages'/f'{stem}.tex'
    if not meta.exists() or not page.exists():raise RuntimeError('Adjudicated metadata and page required')
    d=json.loads(meta.read_text())
    if not d.get('editor_review'):raise RuntimeError('Explicit editor review required')
    log=ROOT/'progress.log'
    if f'scan {a.scan:03} done ' in log.read_text():raise RuntimeError('Already logged done')
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    d['reviewed_at']=stamp
    meta.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    proc=subprocess.run([sys.executable,str(ROOT/'scripts/build_records.py')],capture_output=True,text=True,check=True)
    report=json.loads(proc.stdout)
    if report['missing_marks']:raise RuntimeError('Source marks missing: '+str(report['missing_marks']))
    check=subprocess.run([sys.executable,str(ROOT/'scripts/check_edition.py')],capture_output=True,text=True)
    if check.returncode:raise RuntimeError(check.stdout+check.stderr)
    crop_files=len([x for x in (ROOT/'crops').glob(f'{stem}_*.jpg') if '_audit_' not in x.name])
    crops=d.get('crop_place_count',crop_files)
    rows=sum(bool(x.get('change_C') or x.get('change_H')) for x in d['changes'])
    with log.open('a') as f:f.write(f'scan {a.scan:03} done {stamp} cote 150: {d["line_count"]} lines read, {crops} places cropped, {rows} rows\n')
    if a.next_scan is not None:
        if not a.reader:raise RuntimeError('Reader required for next assignment')
        nxt=f'150_scan{a.next_scan:03}'
        packet=ROOT.parent/'reader_packets'/nxt
        if not packet.is_dir():raise RuntimeError('Next packet missing')
        if f'scan {a.next_scan:03} assigned ' in log.read_text():raise RuntimeError('Next scan already assigned')
        shutil.copyfile(ROOT/'reference/notation.md',packet/'notation_at_assignment.md')
        snapshots=ROOT/'reference/notation_snapshots';snapshots.mkdir(exist_ok=True)
        shutil.copyfile(ROOT/'reference/notation.md',snapshots/f'{nxt}.md')
        with log.open('a') as f:f.write(f'scan {a.next_scan:03} assigned {stamp}: {a.reader}; first reading\n')
    print(json.dumps({'scan':a.scan,'utc':stamp,'cropped_places':crops,'crop_images':crop_files,'rows':rows,'cumulative':report,'next_scan':a.next_scan,'reader':a.reader},indent=2))

if __name__=='__main__':main()
