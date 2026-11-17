"""Exercise both nested containers against actual checkpoint23, without a ZIP write.

An in-memory archive-interface adapter replaces the historical/preview PDF
entries by one standard TAR. This checks the production logical reader's
two-container path behavior on real bytes. No new ZIP is made or saved.
The compression round trip and native tar restoration were checked by
measure_checkpoint24_pdf_bundle.py; actual ZIP CRCs will be checked after
the one scheduled checkpoint24 capture.
"""
from pathlib import Path
from datetime import datetime, timezone
from unittest.mock import patch
import csv
import hashlib
import io
import json
import zipfile
import checkpoint_archive_io as reader
from checkpoint_standard_tar import build_standard_tar

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_23.zip'
prefix = reader.PREFIX
with zipfile.ZipFile(archive) as actual:
    entries = actual.infolist()
    pdfs = [i for i in entries if i.filename.endswith('.pdf') and i.filename != prefix + 'LM4_SUCCESSOR_paper.pdf']
    pdf_names = {i.filename for i in pdfs}
    files = [(i.filename[len(prefix):], actual.read(i)) for i in pdfs]
    bundle, metrics = build_standard_tar(files)
    physical = [i for i in entries if i.filename not in pdf_names]
    physical.append(zipfile.ZipInfo(reader.DOCUMENT_BUNDLE))
    manifest_name = prefix + 'records/checkpoint_23_contents_sha256.tsv'
    rows = list(csv.DictReader(io.StringIO(actual.read(manifest_name).decode()), delimiter='\t'))
    expected = {prefix + r['path']: r for r in rows}

    class ArchiveInterface:
        def infolist(self):
            return physical

        def read(self, name):
            return bundle if name == reader.DOCUMENT_BUNDLE else actual.read(name)

        def close(self):
            pass

    with patch.object(reader.zipfile, 'ZipFile', return_value=ArchiveInterface()):
        with reader.CheckpointReader('interface-only-no-created-archive') as logical:
            assert set(logical.names()) == set(expected) | {manifest_name}
            assert set(logical.document_members) == pdf_names
            assert prefix + 'LM4_SUCCESSOR_paper.pdf' in logical.direct
            assert reader.IMAGE_BUNDLE in logical.direct
            assert reader.DOCUMENT_BUNDLE in logical.direct
            checked = set(pdf_names)
            checked.update(prefix + name for name in ['LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.tex', 'LM4_SUCCESSOR_results.csv'])
            checked.add(next(n for n,m in logical.members.items() if m.isfile()))
            checked.add(next(n for n,m in logical.members.items() if m.islnk()))
            for name in checked:
                data = logical.read(name)
                row = expected[name]
                assert len(data) == int(row['bytes']), name
                assert hashlib.sha256(data).hexdigest() == row['sha256'], name
            assert logical.read(manifest_name) == actual.read(manifest_name)
            logical_count = len(logical.names())

out = {
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'input_archive': archive.name,
    'archive_interface_only_no_new_zip': True,
    'logical_paths_preserved': logical_count,
    'historical_preview_pdf_paths': len(pdf_names),
    'all_reencoded_pdf_bytes': 'PASS',
    'main_pdf_and_current_sources_direct': 'PASS',
    'existing_image_regular_and_hardlink_reads': 'PASS',
    'both_container_logical_namespace': 'PASS',
    'original_manifest_unchanged': 'PASS',
    'bundle_metrics': metrics,
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'reader_sha256': hashlib.sha256((root/'code/checkpoint_archive_io.py').read_bytes()).hexdigest(),
    'limit': 'This preflight exercises the new reader and real TAR bytes. Actual checkpoint24 ZIP CRC and full retention checks remain required after scheduled capture.',
}
(root / 'records/checkpoint24_container_compatibility.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
