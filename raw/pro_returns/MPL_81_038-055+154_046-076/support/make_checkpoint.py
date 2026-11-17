from pathlib import Path
from datetime import datetime, timezone
import argparse,zipfile
root=Path('/workspace/scratch/89f8415d3ab0')
prefix='MPL_81_038-055+154_046-076'
p=argparse.ArgumentParser();p.add_argument('number',type=int);args=p.parse_args()
path=root/f'{prefix}_checkpoint_{args.number:02d}.zip'
if path.exists():raise SystemExit('Refusing to overwrite a checkpoint.')
with (root/'deliver/progress.log').open('a') as f:f.write(f'checkpoint {args.number:02d} packaged '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for base in ('deliver','support'):
        for f in sorted((root/base).rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts:
                arc=f.relative_to(root/'deliver') if base=='deliver' else f.relative_to(root)
                z.write(f,str(arc))
print(str(path));print(path.stat().st_size)
