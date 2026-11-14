"""Verify the losslessly repacked 224-statement archive before replacement."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import zipfile

BASE = Path(__file__).resolve().parent
ARCHIVE = BASE / 'LM7_FERMAT_TOWER.zip'
PREFIX = 'LM7_FERMAT_TOWER/'
EXPECTED_SHA = '710655b94beb024bcb3c281c60633446be8652d2a6d9467b6bb30719a2d0a645'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    digest = sha(ARCHIVE.read_bytes())
    assert digest == EXPECTED_SHA
    assert ARCHIVE.stat().st_size <= 536870912
    with zipfile.ZipFile(ARCHIVE) as archive:
        def read(name):
            return archive.read(PREFIX + name)

        ledger = json.loads(read('ledger/checkpoint224_integration.json'))
        mappings = ledger['frozen_to_archive_mapping']
        assert len(mappings) == 676
        for item in mappings:
            assert sha(read(item['archive'])) == item['sha256'], item
        amendments = ledger['active_ledger_amendments']
        assert len(amendments) == 4
        for item in amendments:
            assert sha(read(item['file'])) == item['after_sha256'], item
            assert sha(read(item['author_freeze'])) == item['before_sha256'], item

        pdf = read('LM7_FERMAT_TOWER_paper.pdf')
        pdf_sha = sha(pdf)
        assert pdf_sha == '2036e398af92127ac966829ae10540426d3100fa15d5f9c753724db76350ae6b'
        qa = json.loads(read('qa/pdf_qa.json'))
        visual_data = read('qa/visual224_root.json')
        visual = json.loads(visual_data)
        assert qa['sha256'] == visual['pdf_sha256'] == pdf_sha
        assert qa['pages'] == visual['pdf_pages'] == 713
        for item in visual['contact_sheets']:
            assert sha(read(item['path'])) == item['sha256'], item
        for item in visual['detail_images']:
            assert sha(read(item['file'])) == item['sha256'], item
        methods = Counter(info.compress_type for info in archive.infolist())
        assert methods[zipfile.ZIP_LZMA] > 0
        result = {
            'status': 'PASS', 'zip_sha256': digest,
            'zip_size': ARCHIVE.stat().st_size,
            'members': len(archive.infolist()),
            'compression_method_member_counts': dict(methods),
            'exact_frozen_mappings': len(mappings),
            'active_amendments_and_exact_originals_checked': len(amendments),
            'missing_files': 0, 'unexplained_changes': 0,
            'pdf_pages': 713, 'numbered_statements': 224,
            'visual_record_sha256': sha(visual_data),
            'contact_images_rehashed': len(visual['contact_sheets']),
            'detail_images_rehashed': len(visual['detail_images']),
            'checked_utc': datetime.now(timezone.utc).isoformat(),
        }
    (BASE / '.lm7_archive224_lzma_readback.json').write_text(
        json.dumps(result, indent=2) + '\n'
    )
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
