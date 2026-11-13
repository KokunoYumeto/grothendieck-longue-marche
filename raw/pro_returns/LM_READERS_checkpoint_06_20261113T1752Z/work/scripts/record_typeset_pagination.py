"""Record only manually supplied, actually viewed pagination observations."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = {
    'LM_FR_texte_de_lecture': 'work/data/pagination_final_FR_reading_observations.json',
    'LM_EN_corrected_apparatus': 'work/data/pagination_final_EN_apparatus_observations.json',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def record(book, group, entries):
    """entries: (queue index, observation, tag page, display pages, image indices, status)."""
    queue_path = ROOT / 'work/data/pagination_final_queues' / (book + '.json')
    queue = json.loads(queue_path.read_text())
    assert sha(ROOT / 'work/build' / (book + '.pdf')) == queue['pdf_sha256']
    target = ROOT / OUTPUTS[book]
    rows = json.loads(target.read_text()) if target.exists() else []
    by_id = {row['id']: row for row in rows}
    assert len(by_id) == len(rows)
    for index, observation, tag_page, display_pages, image_indices, status in entries:
        item = queue[group][index]
        assert observation.strip() and isinstance(tag_page, int) and display_pages
        images = []
        for image_index in image_indices:
            evidence = item['images'][image_index]
            assert sha(ROOT / evidence['path']) == evidence['sha256']
            images.append({'path': evidence['path'], 'sha256': evidence['sha256']})
        assert images
        assert status in {'RESOLVED_ON_FINAL_PDF', 'CLEARED_ON_FINAL_PDF', 'DETACHMENT_REMAINS'}
        by_id[item['id']] = {
            'id': item['id'], 'status': status, 'pdf_sha256': queue['pdf_sha256'],
            'reviewer': 'typeset', 'observation': observation, 'tag_page': tag_page,
            'display_pages': display_pages, 'images': images,
        }
    target.write_text(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2) + '\n')
    print(book, len(by_id), 'manual observations recorded')
