"""Record explicitly supplied observations of native images viewed by root.

This helper verifies and copies evidence metadata; it does not inspect images.
"""
import hashlib
import json
from pathlib import Path


def record(book, rows, target_name):
    queue = json.loads(Path('work/data/final_native_closure_queues', book + '.json').read_text())
    path = Path('work/data', target_name)
    output = json.loads(path.read_text()) if path.exists() else []
    for ident, pages, note in rows:
        spec = next(x for x in queue['items'] if x['id'] == ident)
        assert ident not in {x['id'] for x in output}
        assert len(note.strip()) >= 40
        images = [e for e in queue['evidence_candidates']
                  if e.get('finding_id') == ident and e['page'] in pages
                  and e['scale'] >= spec['minimum_native_scale']]
        assert images
        for image in images:
            assert hashlib.sha256(Path(image['path']).read_bytes()).hexdigest() == image['sha256']
        output.append(dict(id=ident, reader=book, pdf_sha256=queue['pdf_sha256'],
                           status='RESOLVED', reviewer='assistant/root', observation=note,
                           images=[{k: im[k] for k in ('path', 'sha256')} for im in images]))
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(book, 'actual native observations:', len(output))
