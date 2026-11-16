"""Package all authored work, excluding attached duplicates and third-party full source copies."""
from pathlib import Path
import csv,hashlib,zipfile,argparse
p=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('number',type=int);o=a.parse_args();name=f'LM4_SUCCESSOR_checkpoint_{o.number:02d}.zip';out=p.parent/name
assert not out.exists(),'Never overwrite a checkpoint'
excluded=[];included=[]
for f in sorted(p.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(p);r=str(rel);why=None
 if r.startswith('work_CE/') and f.parent==p/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif r.startswith('work_DE/') and f.name.endswith('_source.txt'):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif f.name in ['CE_check.pdf','DE_review.pdf']:why='Transient component preview superseded by the combined clean paper; source and logs retained.'
 elif 'work_CE/sources/' in r and f.suffix.lower()=='.pdf':why='Third-party full source copy; authoritative links, bibliography and reading records retained.'
 elif '__pycache__' in f.parts or f.suffix in ['.aux','.toc','.blg','.bbl']:why='Regenerable TeX/Python auxiliary; source, output PDF, build logs and recipes retained.'
 if why:excluded.append((r,why))
 else:included.append(f)
manifest=p/'records'/f'checkpoint_{o.number:02d}_exclusions.csv'
with manifest.open('w') as h:
 w=csv.writer(h);w.writerow(['path','reason']);w.writerows(excluded)
included=[f for f in included if f!=manifest]+[manifest]
sha=p/'records'/f'checkpoint_{o.number:02d}_contents_sha256.tsv'
sha.write_text('sha256\tbytes\tpath\n'+''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}\t{f.stat().st_size}\t{f.relative_to(p)}\n' for f in included))
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in included+[sha]:z.write(f,Path('LM4_SUCCESSOR')/f.relative_to(p))
print(out);print('files',len(included)+1,'bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
