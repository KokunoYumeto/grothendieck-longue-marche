"""Place retained agent programs and computational outputs under code/ for delivery.

Original research paths are preserved. The delivery copy is explicitly indexed
by its original path and SHA256. Source papers, prose drafts, images and caches
are not copied. Run after research writes have stopped, before final packaging.
"""
import csv
import hashlib
import os
import shutil
from pathlib import Path

W = Path(__file__).resolve().parents[1]
DEST = W / 'code' / 'retained_agent_code'
OWNERS = ['agent_F', 'agent_criteria', 'agent_geometric']
SUFFIXES = {'.py', '.cpp', '.c', '.sh', '.csv', '.json', '.jsonl',
            '.log', '.txt', '.stdout', '.so', '.bin'}

def selected(path):
    rel = path.relative_to(W)
    if (not path.is_file() or '__pycache__' in rel.parts
            or 'native' in rel.parts or 'sources' in rel.parts or 'source_checks' in rel.parts):
        return False
    if '_temporary' in path.name:
        return False
    return path.suffix in SUFFIXES or (not path.suffix and 'code' in rel.parts)

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    # Drop only generated delivery copies of raw third-party source-page
    # caches. Original research files and all audit notes remain untouched.
    for owner in OWNERS:
        cache_copy=DEST/owner/'source_checks'
        if cache_copy.exists():shutil.rmtree(cache_copy)
    rows = []
    for owner in OWNERS:
        for source in sorted((W / owner).rglob('*')):
            if not selected(source):
                continue
            rel = source.relative_to(W)
            target = DEST / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            src_hash = digest(source)
            if target.exists() and digest(target) != src_hash:
                target.unlink()
            if not target.exists():
                try:
                    os.link(source, target)
                except OSError:
                    shutil.copy2(source, target)
            assert digest(target) == src_hash
            rows.append([str(rel), str(target.relative_to(W)),
                         source.stat().st_size, src_hash])
    with (DEST / 'CONTENTS.csv').open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['original_path', 'delivery_copy', 'bytes', 'sha256'])
        writer.writerows(rows)
    (DEST / 'README.txt').write_text(
        'These are byte-identical delivery copies of the retained agent programs\n'
        'and computational outputs. Their original research paths remain in the\n'
        'archive so the source references and original invocation paths keep working.\n'
        'Run programs from their original locations using the owner audit instructions.\n'
        'Root programs and their outputs already occupy code/. QA build logs and page\n'
        'renders are additionally retained in qa/. CONTENTS.csv maps every copy.\n'
        'No supplied background files, earlier ZIPs or third-party source PDFs are\n'
        'included in this delivery copy. PROGRAM_INDEX.csv indexes canonical sources.\n')
    print(f'Delivery copies: {len(rows)}; total bytes: {sum(r[2] for r in rows)}')

if __name__ == '__main__':
    main()
