"""Append reviewer-authored page observations to an independent, hash-bound ledger.

This helper never generates an observation or modifies VISUAL_REVIEW.tsv.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
STEMS = {
    'LM_FR_texte_de_lecture': 'fr_reading',
    'LM_EN_corrected_apparatus': 'en_app',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(book, notes):
    directory = ROOT / 'work/verification' / book
    index_path = directory / 'release578_pending/PENDING_REVIEW_INDEX.json'
    index = json.loads(index_path.read_text())
    rows = {str(p['page']): dict(p, contact_sheet=s['image'])
            for s in index['sheets'] for p in s['pages']}
    stem = STEMS[book]
    output = ROOT / 'work/data' / (stem + '_release578_typeset_observations.json')
    evidence = output.with_name(stem + '_release578_typeset_review_evidence.json')
    old = json.loads(output.read_text()) if output.exists() else {}
    if evidence.exists():
        prior = json.loads(evidence.read_text())
        assert prior['index_sha256'] == digest(index_path), 'Review queue changed.'
    pdf_hash = digest(ROOT / 'work/build' / (book + '.pdf'))
    for key, observation in notes.items():
        key = str(key)
        assert key in rows and isinstance(observation, str) and observation.strip()
        assert rows[key]['pdf_sha256'] == pdf_hash, 'Current PDF changed.'
        assert digest(directory / rows[key]['full_page_image']) == rows[key]['png_sha256']
        old[key] = observation
    output.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n')
    evidence.write_text(json.dumps(dict(
        reader=book, pdf_sha256=pdf_hash, reviewer='typeset',
        basis='Actual inspection of 2x2 contact sheets with each source page rendered at900px; additional native observations are recorded separately.',
        index=index_path.relative_to(ROOT).as_posix(), index_sha256=digest(index_path),
        observations_generated_by_script=False, reviewed_pages=len(old),
        pages=[rows[key] for key in sorted(old, key=int)]
    ), ensure_ascii=False, indent=2) + '\n')
    print(f'{book}: {len(old)}/{len(rows)} actual page observations recorded')
