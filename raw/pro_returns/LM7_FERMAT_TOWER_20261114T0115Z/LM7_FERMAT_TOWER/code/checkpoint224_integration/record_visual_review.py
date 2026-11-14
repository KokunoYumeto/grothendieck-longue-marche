"""Record the root assistant's completed image inspection, with exact hashes.

Images were actually opened through view_image. This program verifies their
identity and extent; it does not infer or perform the visual inspection.
"""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[2]
PDF_SHA = '2036e398af92127ac966829ae10540426d3100fa15d5f9c753724db76350ae6b'
VIEWED_DETAIL_PAGES = [
    1, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 56,
    233, 234, 235, 236, 237, 238, 239, 240, 241,
    254, 255, 256, 257, 258, 259, 260, 261, 262,
    695, 696, 697, 698, 699, 700, 701, 702, 703, 713,
]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert digest(BASE / 'LM7_FERMAT_TOWER_paper.pdf') == PDF_SHA
    qa = json.loads((BASE / 'qa/pdf_qa.json').read_text())
    detail = json.loads((BASE / 'qa/detail224_manifest.json').read_text())
    assert qa['sha256'] == detail['pdf_sha256'] == PDF_SHA
    assert qa['pages'] == detail['pages_in_pdf'] == 713
    expected_contacts = [
        f'qa/contact_{first:03d}_{min(first + 15, 713):03d}.jpg'
        for first in range(1, 714, 16)
    ]
    assert qa['contact_sheets'] == expected_contacts
    assert detail['rendered_pages'] == VIEWED_DETAIL_PAGES
    assert [x['page'] for x in detail['details']] == VIEWED_DETAIL_PAGES
    contacts = []
    for first, name in zip(range(1, 714, 16), expected_contacts):
        contacts.append({
            'first_page': first, 'last_page': min(first + 15, 713),
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
        'pdf_sha256': PDF_SHA, 'pdf_pages': 713,
        'reviewer': 'root assistant',
        'all_contact_sheets_actually_viewed': True,
        'contact_sheets': contacts,
        'detail_pages_actually_viewed': VIEWED_DETAIL_PAGES,
        'detail_images': detail['details'],
        'inspection_findings': (
            'All 45 overview sheets and all 41 specified 110-dpi detail pages '
            'were actually opened and visually inspected. No clipped formula '
            'or table, overlap, unintended blank page, or displaced equation '
            'label was observed.'
        ),
        'scope': (
            'Full-document layout overview; complete amended D13, D19 and E23 '
            'statements; complete new D64 and E121 proofs, with adjoining '
            'boundaries; title page and final bibliography page. Detailed '
            'proof, source and arithmetic-replay audits are separate records.'
        ),
        'truncated_tool_result_handling': (
            'The earlier truncated return containing contact sheets 481-496, '
            '497-512 and 513-528 was not counted. All three were reopened '
            'successfully and actually inspected in subsequent calls.'
        ),
    }
    (BASE / 'qa/visual224_root.json').write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + '\n'
    )
    (BASE / 'qa/visual_review.md').write_text(
        '# Actual visual review of the assembled 224-statement paper\n\n'
        f'PDF SHA256: `{PDF_SHA}`. Pages: 713.\n\n'
        'All 45 contact sheets, covering pages 1-713, were actually opened '
        'and inspected by the root assistant. All 41 detail images in '
        'visual224_root.json were separately opened at 110 dpi: pages 1, '
        '42-47, 51-56, 233-241, 254-262, 695-703 and 713. This covers the '
        'complete amended D13, D19 and E23 statements, the entire newly '
        'integrated D64 and E121 proofs with their boundaries, the title '
        'page and the final bibliography page.\n\n'
        'No clipping, overlap, broken table, unintended blank page, or '
        'displaced equation label was observed. The automatic renderer '
        'separately checked all 224 statement headings and page borders. '
        'The detailed proof and arithmetic-replay audits remain separate '
        'from this layout review.\n\n'
        'The earlier truncated tool return was not used as visual evidence; '
        'all three affected contact sheets were reopened and inspected. The '
        'previous checkpoint review is preserved under '
        'qa/history/checkpoint222_before224.\n'
    )
    for name in ['root_assemble224.err', 'root_build224.err', 'root_qa224.err']:
        source = BASE.parent / name
        assert source.exists() and source.stat().st_size == 0
        shutil.copy2(source, Path(__file__).parent / name)
    print(json.dumps({
        'status': record['status'], 'pdf_sha256': PDF_SHA,
        'pages': 713, 'overview_sheets_actually_viewed': len(contacts),
        'detail_pages_actually_viewed': len(VIEWED_DETAIL_PAGES),
        'visual_record_sha256': digest(BASE / 'qa/visual224_root.json'),
        'review_markdown_sha256': digest(BASE / 'qa/visual_review.md'),
    }, indent=2))


if __name__ == '__main__':
    main()
