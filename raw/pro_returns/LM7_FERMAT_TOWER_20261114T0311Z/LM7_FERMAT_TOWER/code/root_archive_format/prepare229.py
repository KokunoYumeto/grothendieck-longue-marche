#!/usr/bin/env python3
"""Prepare the next lossless ZIP writer without changing the current deliverable."""
from pathlib import Path
import hashlib,json

R=Path(__file__).resolve().parent
p=(R/'package226.py').read_text()
def replace(old,new):
    global p
    assert p.count(old)==1,old[:100]
    p=p.replace(old,new)
replace('from materialize_archive_images import plan_image_aliases',
        'from materialize_archive_images import plan_image_aliases\nfrom materialize_archive_files import plan_binary_aliases')
replace('''    # Exact duplicate QA raster images have explicit logical-path aliases.
    # Every mathematical record and every current main-PDF image remains an
    # ordinary member. The local tree retains all original files throughout.
    image_plan = plan_image_aliases(
        {str(p.relative_to(BASE)): p.read_bytes() for p in files}, len(results))
    aliases = {r['path']: r['storage_path'] for r in image_plan['aliases']}
    alias_path = BASE / 'ledger/archive_image_aliases.json'
    alias_path.write_text(json.dumps(image_plan, indent=2) + '\\n')
    files = sorted(set(files + [alias_path]))''',
'''    # Only complete byte-identical binary data and historical QA images are
    # aliased. All text sources, outputs, JSON and current page images remain
    # ordinary members; every original logical byte string is retained.
    provisional = {str(p.relative_to(BASE)): p.read_bytes() for p in files}
    image_plan = plan_image_aliases(provisional, len(results))
    image_plan['scope'] = 'Only complete byte-identical historical QA raster images; current main-PDF page images remain ordinary members.'
    binary_plan = plan_binary_aliases(provisional)
    del provisional
    all_alias_rows = image_plan['aliases'] + binary_plan['aliases']
    aliases = {r['path']: r['storage_path'] for r in all_alias_rows}
    assert len(aliases) == len(all_alias_rows)
    assert not any(target in aliases for target in aliases.values())
    alias_paths = []
    for kind, plan in [('image', image_plan), ('binary', binary_plan)]:
        alias_path = BASE / ('ledger/archive_' + kind + '_aliases.json')
        alias_path.write_text(json.dumps(plan, indent=2) + '\\n')
        alias_paths.append(alias_path)
    files = sorted(set(files + alias_paths))''')
replace("        'Large binary and JSON records use lossless ZIP LZMA.',", "        'Standard ZIP deflate, BZIP2 and LZMA are used with complete byte preservation.',")
replace("        f'Byte-identical duplicate QA image paths represented by exact verified aliases: {len(aliases)}',",
        "        f'Byte-identical duplicate QA image paths represented by verified aliases: {len(image_plan[\"aliases\"])}',\n        f'Byte-identical duplicate binary data paths represented by verified aliases: {len(binary_plan[\"aliases\"])}',")
replace("        'All logical paths and original bytes are retained; the supplied materializer restores image aliases.', ",
        "        'All original logical paths and bytes are retained; materialize_archive_files.py restores both exact alias types.',")
replace("'manifest_scope': 'Every logical file except this manifest itself. storage_path names the exact byte-identical ZIP member; the image-alias materializer restores every original image path.',",
        "'manifest_scope': 'Every logical file except this manifest itself. storage_path names its exact byte-identical ZIP member. materialize_archive_files.py restores every original duplicate binary-data and historical-image path.',")
replace("'compression': 'Standard ZIP: LZMA for binary/JSON records of at least 1000000 bytes; deflate for other members. Duplicate historical QA image bytes are stored once with explicit lossless path aliases. See code/ARCHIVE_README.md.',",
        "'compression': 'Standard ZIP with deflate, BZIP2 and LZMA. The retained whole-byte codec benchmark supplies choices for identical known records; new large binary/text records use LZMA. Exact duplicate binary data and historical QA images have explicit path aliases. All original bytes are retained; see code/ARCHIVE_README.md.',")
replace("        'image_alias_count': len(aliases),",
        "        'image_alias_count': len(image_plan['aliases']),\n        'binary_alias_count': len(binary_plan['aliases']),")
replace("    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:",
'''    benchmark = json.loads((CODE / 'root_archive_format/compression229_benchmark.json').read_text())
    assert benchmark['status'] == 'PASS'
    codecs = {}
    for row in benchmark['members']:
        method = {'existing': row['original_method'], 'bzip2': zipfile.ZIP_BZIP2,
                  'lzma': zipfile.ZIP_LZMA}[row['best']]
        assert row['complete_roundtrip_byte_identity']
        assert method in {zipfile.ZIP_DEFLATED, zipfile.ZIP_BZIP2, zipfile.ZIP_LZMA}
        if row['sha256'] in codecs: assert codecs[row['sha256']] == method
        codecs[row['sha256']] = method
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:''')
replace("""            codec = (zipfile.ZIP_LZMA
                     if Path(name).suffix in {'.bin', '.json'} and len(data) >= 1000000
                     else zipfile.ZIP_DEFLATED)""",
"""            codec = codecs.get(sha(data), zipfile.ZIP_LZMA
                     if Path(name).suffix in {'.bin','.json','.out','.tex','.md','.txt','.csv','.log'} and len(data) >= 65536
                     else zipfile.ZIP_DEFLATED)""")
replace("'logical_files_including_manifest': len(payload), 'image_aliases': len(aliases)",
        "'logical_files_including_manifest': len(payload), 'image_aliases': len(image_plan['aliases']), 'binary_aliases': len(binary_plan['aliases'])")
compile(p,'package229.py','exec')
(R/'package229.py').write_text(p)

q=(R/'materialize_archive_images.py').read_text()
q=q.replace('Only raster QA images are eligible. All code, mathematical inputs, outputs,\ncertificates and current main-PDF page images remain ordinary ZIP members.',
            'Only raster QA images are handled by this compatibility utility. The\ncompanion materialize_archive_files.py also restores exact binary-data aliases.\nCurrent main-PDF page images remain ordinary ZIP members.')
q=q.replace('Only byte-identical duplicate QA raster images; all mathematical records and current main-PDF page images are ordinary files.',
            'Only byte-identical duplicate QA raster images; current main-PDF page images are ordinary files.')
(R/'materialize_archive_images229.py').write_text(q)

readme='''# Extracting and verifying the complete archive

This is a standard ZIP using deflate, BZIP2 and LZMA. Python 3 extracts all
three methods with its standard library:

```sh
python -m zipfile -e LM7_FERMAT_TOWER.zip extracted
python extracted/LM7_FERMAT_TOWER/code/materialize_archive_files.py
```

The second command restores every original duplicate binary-data and
historical-image path. It copies exact original bytes from a verified ZIP
member, checks the original byte count and SHA-256, and refuses to overwrite
a different file or follow a symlink. It does no numerical conversion,
binary reserialization, image resampling or re-encoding. Running it again
verifies the same files. The optional `--verify-only` mode only checks an
already restored tree.

All source programs, text transcripts, JSON records, documents and current
paper page images are ordinary ZIP members. Complete byte-identical copies
of `.bin`, `.npz` and `.npy` certificates/inputs and historical QA images
are stored once, with every original logical path recorded in
`ledger/archive_binary_aliases.json` and `ledger/archive_image_aliases.json`.
Different binary serializations remain different complete byte strings.
The compatibility utility `materialize_archive_images.py` restores only
the image aliases; the command above restores both kinds.

`LM7_FERMAT_TOWER_manifest.json` describes every original logical file.
Its `storage_path` names the ordinary ZIP member carrying that exact file's
bytes. It equals `path` for every file except an explicitly listed duplicate.
The packaging program checks all physical CRCs and reconstructs every
logical file through this map, comparing its whole original byte string,
byte count and SHA-256. The local author and review trees remain unchanged.

The binary layout was independently exercised on all 296 binary records
in the preceding checked archive. All 93 duplicate paths were physically
restored and all 296 complete files were compared with their original
bytes. Both restoration and a second verification-only execution passed;
escaping paths, symlinks and nonmatching existing targets were rejected.
The retained records are `code/root_archive_format/binary_roundtrip229.json`
and the complete verifier source and actual outputs. The preceding image
round trip likewise restored all 237 duplicate paths among 999 images.

The whole-byte codec benchmark and exact archive read-back records are
retained. Earlier packaging versions remain in the recorded history.
No research source, execution output, mathematical certificate or original
logical file is removed by this storage representation.
'''
(R/'ARCHIVE_README229.md').write_text(readme)
print(json.dumps({'status':'PASS','prepared_files':[
    {'path':n,'sha256':hashlib.sha256((R/n).read_bytes()).hexdigest()}
    for n in ['package229.py','materialize_archive_images229.py','ARCHIVE_README229.md']],
    'current_deliverable_modified':False},indent=2))
