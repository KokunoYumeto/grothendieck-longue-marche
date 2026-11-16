#!/usr/bin/env python3
"""Execute all superseded PNG restorations with the original PDF absent."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
fixture = root.parent / 'checkpoint17_pdf_png_restoration/archive_fixture'
fixture.mkdir(exist_ok=False)
manifest = json.loads((root / 'qa/reconstruction_manifest.json').read_text())
selected = {name: row for name, row in manifest['images'].items()
            if name.startswith('qa/superseded_checkpoint17_build1/')}
assert len(selected) == 51
dependencies = {'qa/reconstruction_manifest.json', 'code/restore_qa_png.py',
                'code/restore_pdf_delta.py'}
for row in selected.values():
    recipe_name = row['pdf_restore_recipe']
    recipe = json.loads((root / recipe_name).read_text())
    dependencies.update((recipe_name, recipe['base_path'], recipe['payload_path']))
for name in dependencies:
    target = fixture / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / name, target)
rows = []
for name, row in selected.items():
    assert not (fixture / row['pdf_path']).exists()
    target = fixture.parent / 'restored_pngs' / Path(name).name
    subprocess.run([sys.executable, str(fixture / 'code/restore_qa_png.py'),
                    str(fixture / 'qa/reconstruction_manifest.json'), name,
                    str(target)], check=True, capture_output=True, text=True)
    restored, original = target.read_bytes(), (root / name).read_bytes()
    assert restored == original
    rows.append({'path': name, 'bytes': len(restored),
                 'sha256': hashlib.sha256(restored).hexdigest(),
                 'original_pdf_absent': True, 'entire_png_bytes_equal': True})
result = {'status': 'PASS', 'restored_pngs': len(rows),
          'method': 'Actual standalone PNG decoder processes in a fixture without the old PDF; the exact PDF is decoded from its verified delta in memory.',
          'literal_dependencies': sorted(dependencies), 'rows': rows,
          'no_zip_created': True}
(root / 'notes/checkpoint17_pdf_png_restoration.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
