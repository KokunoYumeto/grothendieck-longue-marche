"""Render final37 PDF pages selected from actual headings; no visual approval.

Checkpoint37 source. Run only after the final build and fresh metrics have
completed. This helper never builds a PDF or changes the paper/register.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import re

import fitz


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def statement_pages(texts, label):
    pattern = re.compile(r'(?m)^\s*' + re.escape(label) + r'\.\s*\[')
    return [i + 1 for i, text in enumerate(texts) if pattern.search(text)]


def boundary_page(texts, start, part, first_label):
    part_pattern = re.compile(r'(?m)^\s*Part\s+' + part + r'\.\s+')
    first_pattern = re.compile(r'(?m)^\s*' + re.escape(first_label) + r'\.\s*\[')
    hits = [i + 1 for i in range(start - 1, len(texts))
            if part_pattern.search(texts[i]) or first_pattern.search(texts[i])]
    require(bool(hits), 'No following actual Part ' + part + ' / ' + first_label)
    return hits[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    pdf_path = root / 'LM4_SUCCESSOR_paper.pdf'
    metrics_path = root / 'records/checkpoint37_metrics.json'
    metrics_raw = metrics_path.read_bytes()
    metrics = json.loads(metrics_raw)
    pdf_bytes = pdf_path.read_bytes()
    pdf_sha = sha(pdf_bytes)
    require(pdf_sha == metrics['pdf_sha256'], 'Final PDF does not match fresh37 metrics')

    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    require(len(doc) == metrics['pages'], 'Final page count differs from37 metrics')
    texts = [page.get_text() for page in doc]
    labels = [f'A.{n}' for n in range(126, 131)] + [f'B.{n}' for n in range(174, 175)]
    headings = {}
    for label in labels:
        hits = statement_pages(texts, label)
        require(len(hits) == 1, 'Expected one actual statement heading for ' + label + ': ' + repr(hits))
        headings[label] = hits[0]
    require(list(headings.values()) == sorted(headings.values()),
            'New statement headings are not in their actual paper order')

    a_start = headings['A.126']
    a_end = boundary_page(texts, a_start, 'B', 'B.1')
    b_start = headings['B.174']
    b_end = boundary_page(texts, b_start, 'C', 'C.1')
    require(a_start <= headings['A.130'] <= a_end < b_start <= headings['B.174'] <= b_end,
            'Actual new-section intervals are inconsistent')
    # Inclusive final boundary pages conservatively retain a shared-page tail.
    intervals = {'A126_through_A130': [a_start, a_end],
                 'B174_complete': [b_start, b_end]}
    required = sorted(set(range(a_start, a_end + 1)) | set(range(b_start, b_end + 1)))
    reference_hits = [i + 1 for i, text in enumerate(texts)
                      if re.search(r'(?m)^\s*References\s*$', text)]
    require(bool(reference_hits), 'No actual References heading in final PDF')
    reference_start = reference_hits[-1]
    require(reference_start > b_end, 'References start precedes the completed new mathematics')
    # A.121 has a newly repaired whole-group cancellation. Select its entire
    # actual interval, including the shared A.122 boundary, for fresh review.
    editorial_headings = {}
    for label in ('A.121', 'A.122'):
        hits = statement_pages(texts, label)
        require(len(hits) == 1, 'Expected one correction-boundary heading for '+label)
        editorial_headings[label] = hits[0]
    legacy_start, legacy_end = editorial_headings['A.121'], editorial_headings['A.122']
    require(legacy_start <= legacy_end < a_start, 'Corrected A.121 interval is inconsistent')
    editorial_intervals = {'A121_complete_algebraic_correction': [legacy_start, legacy_end]}
    editorial_pages = list(range(legacy_start, legacy_end + 1))
    required_individual = sorted(set(required) | set(editorial_pages))
    front = list(range(1, min(7, len(doc)) + 1))
    boundaries = [a_start - 1, a_end + 1, b_start - 1, b_end + 1]
    references = list(range(reference_start, len(doc) + 1))
    pages = sorted({n for n in front + required_individual + boundaries + references + [len(doc)]
                    if 1 <= n <= len(doc)})

    out = root / 'records/pdf_qa/checkpoint37_final'
    require(not out.exists() or not any(out.iterdir()),
            'Preserve the existing37 render directory before a new final render')
    out.mkdir(parents=True, exist_ok=True)
    for n in pages:
        doc[n - 1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(
            out / f'page-{n:03d}.png')

    contact_names = []
    width, height = 330, 490
    for start in range(0, len(pages), 9):
        block = pages[start:start + 9]
        canvas = fitz.open()
        page = canvas.new_page(width=3 * width, height=math.ceil(len(block) / 3) * height)
        page.draw_rect(page.rect, color=None, fill=(0.85, 0.85, 0.85))
        for k, n in enumerate(block):
            x, y = (k % 3) * width, (k // 3) * height
            page.insert_text((x + 10, y + 15), f'Page {n}', fontsize=10, color=(0, 0, 0))
            page.insert_image(fitz.Rect(x + 6, y + 24, x + width - 6, y + height - 6),
                              filename=str(out / f'page-{n:03d}.png'), keep_proportion=True)
        name = f'contact-{start // 9 + 1:02d}.png'
        page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).save(out / name)
        contact_names.append(name)
        canvas.close()

    manifest = {
        'recorded_at': datetime.now(timezone.utc).isoformat(),
        'pdf': 'LM4_SUCCESSOR_paper.pdf', 'pdf_sha256': pdf_sha,
        'metrics_sha256': sha(metrics_raw), 'page_count': len(doc), 'dpi': 144,
        'actual_statement_heading_pages': headings,
        'required_new_mathematical_intervals_inclusive': intervals,
        'required_new_mathematical_pages': required,
        'editorial_statement_heading_pages': editorial_headings,
        'required_editorial_intervals_inclusive': editorial_intervals,
        'required_editorial_pages': editorial_pages,
        'required_individual_pages': required_individual,
        'front_matter_pages': front, 'references_start_page': reference_start,
        'rendered_pages': pages, 'contact_sheets': len(contact_names),
        'contact_files': contact_names, 'contact_page_capacity': 9,
        'scope': 'Final combined PDF only. Entire corrected A121 proof, actual A126-A130 and B174 intervals, inclusive boundary pages, front1-7, all References pages, and final document page.',
        'visual_approval': False,
        'approval_scope': 'Rendering is not visual inspection or approval. Every required page still needs individual review.',
    }
    (out / 'render_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    doc.close()
    print(json.dumps({'rendered_pages': len(pages), 'required_new_mathematical_pages': len(required),
                      'contact_sheets': len(contact_names), 'intervals': intervals,
                      'editorial_intervals': editorial_intervals, 'required_individual_pages': required_individual,
                      'pdf_sha256': pdf_sha, 'visual_approval': False}, indent=2))


if __name__ == '__main__':
    main()
