#!/usr/bin/env python3
"""Prepare the next exact logical-tree ZIP writer without modifying224."""
from pathlib import Path
import hashlib,json

A=Path(__file__).resolve().parent
source=A.parent/'LM7_FERMAT_TOWER/code/package.py'
t=source.read_text();before=hashlib.sha256(source.read_bytes()).hexdigest()
def replace(a,b):
    global t
    assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
replace('import zipfile\n','import zipfile\nfrom materialize_archive_images import plan_image_aliases\n')
replace("'.pdf', '.png', '.jpg', '.aux', '.log'}),","'.pdf', '.png', '.jpg', '.aux', '.log', '.txt'}),")
replace("('inputs', {'.json', '.out', '.bin'}),","('inputs', {'.json', '.out', '.bin', '.txt'}),")
needle='    # Record the exact completed checks; the resulting archive is then read back.\n'
block='''    # Exact duplicate QA raster images have explicit logical-path aliases.
    # Every mathematical record and every current main-PDF image remains an
    # ordinary member. The local tree retains all original files throughout.
    image_plan = plan_image_aliases(
        {str(p.relative_to(BASE)): p.read_bytes() for p in files}, len(results))
    aliases = {r['path']: r['storage_path'] for r in image_plan['aliases']}
    alias_path = BASE / 'ledger/archive_image_aliases.json'
    alias_path.write_text(json.dumps(image_plan, indent=2) + '\\n')
    files = sorted(set(files + [alias_path]))
'''
replace(needle,block+needle)
replace("        'Large binary and JSON records use lossless ZIP LZMA; all paths and bytes are retained.',",
'''        'Large binary and JSON records use lossless ZIP LZMA.',
        f'Byte-identical duplicate QA image paths represented by exact verified aliases: {len(aliases)}',
        'All logical paths and original bytes are retained; the supplied materializer restores image aliases.', ''')
replace("'manifest_scope': 'Every archived file except this manifest itself.',",
        "'manifest_scope': 'Every logical file except this manifest itself. storage_path names the exact byte-identical ZIP member; the image-alias materializer restores every original image path.',")
replace("'compression': 'Standard ZIP: LZMA for binary/JSON records of at least 1000000 bytes; deflate for other members. See code/ARCHIVE_README.md.',",
''' 'compression': 'Standard ZIP: LZMA for binary/JSON records of at least 1000000 bytes; deflate for other members. Duplicate historical QA image bytes are stored once with explicit lossless path aliases. See code/ARCHIVE_README.md.',
        'image_alias_count': len(aliases),
        'logical_file_count': len(payload),
        'ordinary_member_count_including_manifest': len(payload) - len(aliases) + 1,''')
replace("'files': [{'path': name, 'bytes': len(data), 'sha256': sha(data)}",
        "'files': [{'path': name, 'storage_path': aliases.get(name, name), 'bytes': len(data), 'sha256': sha(data)}")
replace("    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:\n        for name, data in sorted(payload.items()):",
'''    physical = {name: data for name, data in payload.items() if name not in aliases}
    assert all(payload[name] == physical[target] for name, target in aliases.items())
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(physical.items()):''')
replace("        assert set(z.namelist()) == {PREFIX + '/' + name for name in payload}",
        "        assert set(z.namelist()) == {PREFIX + '/' + name for name in physical}")
replace("            assert z.read(PREFIX + '/' + name) == data, name",
        "            assert z.read(PREFIX + '/' + aliases.get(name, name)) == data, name")
replace("            assert sha(z.read(PREFIX + '/' + item['path'])) == item['sha256']",
        "            recovered = z.read(PREFIX + '/' + item['storage_path'])\n            assert len(recovered) == item['bytes'] and sha(recovered) == item['sha256']")
replace("'sha256': archive_digest, 'members': len(payload)}, indent=2))",
        "'sha256': archive_digest, 'members': len(physical),\n                      'logical_files_including_manifest': len(payload), 'image_aliases': len(aliases)}, indent=2))")
compile(t,str(A/'package226.py'),'exec')
(A/'package226.py').write_text(t)
print(json.dumps({'status':'PREPARED','source_sha256':before,
                  'prepared_package_sha256':hashlib.sha256(t.encode()).hexdigest(),
                  'current_tree_modified':False,'archive_rebuild_executed':False},indent=2))
