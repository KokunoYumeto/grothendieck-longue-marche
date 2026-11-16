from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root = Path(__file__).resolve().parents[1]
out = root.parent / 'deliverables'
out.mkdir(exist_ok=True)
number = int(sys.argv[1])
name = f'MPL_15_139-194_checkpoint_{number:02d}.zip'
path = out / name
if path.exists():
    raise FileExistsError(path)
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root / 'progress.log').open('a', encoding='utf-8') as f:
    f.write(f'checkpoint {number:02d} assembled {stamp}\n')
with ZipFile(path, 'x', compression=ZIP_DEFLATED) as z:
    for file in sorted(root.rglob('*')):
        if file.is_file() and '__pycache__' not in file.parts:
            z.write(file, file.relative_to(root))
print(path)
