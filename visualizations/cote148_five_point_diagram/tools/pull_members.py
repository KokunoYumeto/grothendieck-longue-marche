"""Pull selected original members out of an unzipped portable checkpoint (CHECKPOINT_RESUME.json + chunks/*.tar.xz).
Only blobs with codec 'original' are written; each member is checked against its sha256. Read-only on the source.
usage: python -I -B pull_members.py CHECKPOINT_DIR DEST_DIR REGEX"""
import hashlib, json, lzma, pathlib, re, sys, tarfile
src, dest, pat = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), re.compile(sys.argv[3])
rec = json.loads((src / 'CHECKPOINT_RESUME.json').read_text(encoding='utf-8'))
want = {}
for name, d in rec['members'].items():
    if pat.search(name):
        want.setdefault(d['blob'], []).append((name, d))
todo = set(want)
print('members wanted', sum(len(v) for v in want.values()), 'blobs', len(todo))
ok = bad = skipped = 0
for chunk in rec['chunks']:
    if not todo: break
    if not set(chunk['blobs']) & todo: continue
    with lzma.open(src / chunk['name'], 'rb') as dec, tarfile.open(fileobj=dec, mode='r|') as tar:
        for item in tar:
            if item.name not in todo: continue
            data = tar.extractfile(item).read(); todo.discard(item.name)
            if rec['blobs'][item.name]['codec'] != 'original':
                skipped += len(want[item.name]); continue
            for name, d in want[item.name]:
                if hashlib.sha256(data).hexdigest() != d['sha256']: bad += 1; print('SHA MISMATCH', name); continue
                p = dest / pathlib.PurePosixPath(name)
                if '..' in p.parts: raise ValueError(name)
                p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data); ok += 1
            if not todo: break
print('written', ok, 'bad', bad, 'skipped (non-original codec)', skipped, 'missing blobs', len(todo))
