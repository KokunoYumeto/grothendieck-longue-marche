"""Commit each blind submission once, then compare its exact tokens."""
from datetime import datetime, timezone
import csv, io, json, sys
from build_reports import ROOT
from integrity import atomic_write, compare_bytes, digest, verify_first, verify_second, verify_views

verify_first()
for n in map(int,sys.argv[1:]):
    stem=f'147_scan{n:03d}'
    verify_views(n)
    first_bytes=(ROOT/'second'/f'{stem}_first.tsv').read_bytes()
    second_path=ROOT/'second'/f'{stem}_second.tsv'
    second_bytes=second_path.read_bytes()
    commitment=ROOT/'second'/f'{stem}_second_SHA256.tsv'
    if commitment.exists():
        verify_second(n)
    else:
        buffer=io.StringIO(newline='')
        writer=csv.DictWriter(buffer,['path','sha256'],delimiter='\t');writer.writeheader()
        writer.writerow({'path':str(second_path.relative_to(ROOT)),'sha256':digest(second_bytes)})
        atomic_write(commitment,buffer.getvalue().encode(),exclusive=True)
        stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        with (ROOT/'progress.log').open('a') as f:
            f.write(f'blind second reading committed {stamp}: {stem}; SHA-256 {digest(second_bytes)}\n')
    # Compare the exact immutable bytes whose digest was just committed.
    out=compare_bytes(n,first_bytes,second_bytes)
    target=ROOT/'second'/f'{stem}_comparison.json'
    if target.exists():
        if json.loads(target.read_text())!=out:
            raise SystemExit(f'Refusing to replace stale or altered comparison: {target}')
    else:
        atomic_write(target,(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode(),exclusive=True)
    print(json.dumps({k:out[k] for k in ('scan','boxes','differences')},ensure_ascii=False))
