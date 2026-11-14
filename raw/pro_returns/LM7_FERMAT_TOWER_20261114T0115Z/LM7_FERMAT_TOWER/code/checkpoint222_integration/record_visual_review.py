"""Record the root assistant's completed image inspection, with exact hashes.

The image inspection took place through view_image. This program verifies the
identity and extent of the inspected material; it does not perform or infer a
visual review. The earlier truncated image return was not used as evidence.
"""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[2]
PDF_SHA = '25c6993393973d27e66edd6f38706b2fc29af03e01385a73ae712dcaabe54860'
VIEWED_DETAIL_PAGES = [
    1, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55,
    227, 228, 229, 230, 231, 232, 233, 234,
    247, 248, 249, 250, 251, 252, 253, 254, 255,
    678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 699,
]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert digest(BASE / 'LM7_FERMAT_TOWER_paper.pdf') == PDF_SHA
    qa = json.loads((BASE / 'qa/pdf_qa.json').read_text())
    detail = json.loads((BASE / 'qa/detail222_manifest.json').read_text())
    assert qa['sha256'] == detail['pdf_sha256'] == PDF_SHA
    assert qa['pages'] == detail['pages_in_pdf'] == 699
    expected_contacts = [
        f'qa/contact_{first:03d}_{min(first + 15, 699):03d}.jpg'
        for first in range(1, 700, 16)
    ]
    assert qa['contact_sheets'] == expected_contacts
    assert detail['rendered_pages'] == VIEWED_DETAIL_PAGES
    assert [x['page'] for x in detail['details']] == VIEWED_DETAIL_PAGES
    contacts = []
    for first, name in zip(range(1, 700, 16), expected_contacts):
        contacts.append({
            'first_page': first, 'last_page': min(first + 15, 699),
            'path': name, 'sha256': digest(BASE / name),
            'actually_viewed': True,
        })
    for item in detail['details']:
        p = BASE / item['file']
        assert digest(p) == item['sha256']
        assert p.stat().st_size == item['bytes']
        assert item['exit_code'] == 0 and item['dpi'] == 110
    record = {
        'status': 'PASS_VISUAL_LAYOUT',
        'pdf_sha256': PDF_SHA, 'pdf_pages': 699,
        'reviewer': 'root assistant',
        'all_contact_sheets_actually_viewed': True,
        'contact_sheets': contacts,
        'detail_pages_actually_viewed': VIEWED_DETAIL_PAGES,
        'detail_images': detail['details'],
        'inspection_findings': (
            'All 44 overview sheets and all 42 specified 110-dpi detail pages '
            'were actually opened and visually inspected. No clipped formula '
            'or table, overlap, unintended blank page, or displaced equation '
            'label was observed.'
        ),
        'scope': (
            'Full-document layout overview; complete amended D13, D19 and E23 '
            'statements; complete new D63 and E119 proofs, with adjoining '
            'boundaries; title page and final bibliography page. Detailed '
            'proof, source and arithmetic-replay audits are separate records.'
        ),
        'truncated_tool_result_handling': (
            'The earlier truncated return containing the first four contact '
            'sheets was not counted. All four were reopened successfully and '
            'actually inspected in subsequent calls.'
        ),
    }
    (BASE / 'qa/visual222_root.json').write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + '\n'
    )
    (BASE / 'qa/visual_review.md').write_text(
        '# Actual visual review of the assembled 222-statement paper\n\n'
        f'PDF SHA256: `{PDF_SHA}`. Pages: 699.\n\n'
        'All 44 contact sheets, covering pages 1-699, were actually opened '
        'and inspected by the root assistant. All 42 detail images in '
        'visual222_root.json were separately opened at 110 dpi: pages 1, '
        '42-47, 51-55, 227-234, 247-255, 678-689 and 699. This covers the '
        'complete amended D13, D19 and E23 statements, the entire newly '
        'integrated D63 and E119 proofs with their boundaries, the title '
        'page and the final bibliography page.\n\n'
        'No clipping, overlap, broken table, unintended blank page, or '
        'displaced equation label was observed. The automatic renderer '
        'separately checked all 222 statement headings and page borders. '
        'The detailed proof and arithmetic-replay audits remain separate '
        'from this layout review.\n\n'
        'The earlier truncated tool return was not used as visual evidence; '
        'all four affected contact sheets were reopened and inspected. The '
        'previous checkpoint review is preserved under '
        'qa/history/checkpoint220_before222.\n'
    )
    # Preserve the actual outer stderr streams, including their true emptiness.
    for name in ['root_assemble222.err', 'root_build222.err', 'root_qa222.err']:
        source = BASE.parent / name
        assert source.exists() and source.stat().st_size == 0
        shutil.copy2(source, Path(__file__).parent / name)
    print(json.dumps({
        'status': record['status'], 'pdf_sha256': PDF_SHA,
        'pages': 699, 'overview_sheets_actually_viewed': len(contacts),
        'detail_pages_actually_viewed': len(VIEWED_DETAIL_PAGES),
        'visual_record_sha256': digest(BASE / 'qa/visual222_root.json'),
        'review_markdown_sha256': digest(BASE / 'qa/visual_review.md'),
    }, indent=2))


if __name__ == '__main__':
    main()
