#!/usr/bin/env python3
"""Queue generated apparatus/doubt headings with no following body line.

This is an all-page candidate inventory, not a visual-clearance claim.
"""
from pathlib import Path
import argparse
import json
import re
import unicodedata
import fitz
from audit_equation_pagination import BOOKS, ignored, lines, normalize, page_scans, render_pair, sha

ROOT = Path(__file__).resolve().parents[2]
HEADINGS = {
    'Apparat du scan': 'apparatus',
    'Apparatus for this scan': 'apparatus',
    'Doutes conservés dans les passages biffés.': 'retained_doubts',
    'Uncertainty retained from cancelled passages.': 'retained_doubts',
}


def canonical(text):
    return normalize(unicodedata.normalize('NFKC', text)).casefold()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='work/data/generated_heading_candidates_revision512.json')
    parser.add_argument('--proof-dir', default='work/visual_repair_proofs/generated_headings_revision512')
    args = parser.parse_args()
    files, candidates = [], []
    titles = {canonical(title): (title, kind) for title, kind in HEADINGS.items()}
    directory = ROOT / args.proof_dir
    directory.mkdir(parents=True, exist_ok=True)
    for book in BOOKS:
        pdf = ROOT / 'work/build' / (book + '.pdf')
        before = sha(pdf)
        found = 0
        heading_count = 0
        with fitz.open(pdf) as doc:
            scans = page_scans(book, doc)
            for page in doc:
                body = [line for line in lines(page) if not ignored(line, page)]
                for line in body:
                    match = titles.get(canonical(line['text']))
                    if not match and re.fullmatch(r'scans\s*\d+\s*[–—-]\s*\d+', unicodedata.normalize('NFKC',line['text']).strip(),re.I):
                        match = (line['text'],'scan_range')
                    if not match:
                        continue
                    heading_count += 1
                    below = [other for other in body if other is not line and other['bbox'][1] >= line['bbox'][3] - 1]
                    if below or page.number + 1 >= len(doc):
                        continue
                    title, kind = match
                    row = {'id': f'HEADING-{book}-p{page.number + 1:04d}-{kind}',
                           'reader': book, 'pdf_sha256': before, 'page': page.number + 1,
                           'adjacent_page': page.number + 2, 'heading_kind': kind, 'heading': title,
                           'tag': title, 'bbox': line['bbox'], 'direction': 'number_before_next_page_display',
                           'scan_context': scans.get(page.number + 1, []),
                           'adjacent_scan_context': scans.get(page.number + 2, []),
                           'next_page_text': doc[page.number + 1].get_text()[:3000],
                           'status': 'PENDING_MASTER_PIXEL_IDENTITY' if 'master' in book else 'PENDING_ACTUAL_VISUAL_REVIEW'}
                    if 'master' not in book:
                        render_pair(row, directory)
                        row['native_pair_image'] = Path(row['native_pair_image']).relative_to(ROOT).as_posix()
                    candidates.append(row)
                    found += 1
                # A separator can detach one step earlier than its heading.
                # Qualify the graphic by the generated rule's exact left edge
                # and the actual macro width (.26 for apparatus, .2 for
                # retained doubts), plus the next page's opening title.
                if page.number + 1 < len(doc) and not page.rotation:
                    next_page = doc[page.number + 1]
                    next_body = [item for item in lines(next_page) if not ignored(item, next_page)]
                    next_title = titles.get(canonical(next_body[0]['text'])) if next_body else None
                    if next_title:
                        margin = 25 * 72 / 25.4
                        title, kind = next_title
                        rule_fraction = .26 if kind == 'apparatus' else .2
                        rule_width = (page.rect.width - 2 * margin) * rule_fraction
                        for drawing in page.get_drawings():
                            rect = drawing['rect']
                            if not (abs(rect.x0 - margin) < 2 and abs(rect.width - rule_width) < 2
                                    and rect.height <= 1.5 and rect.y0 >= page.rect.height * .47
                                    and rect.y1 < page.rect.height - 62):
                                continue
                            if any(item['bbox'][1] >= rect.y1 - 1 for item in body):
                                continue
                            row = {'id': f'HEADING-{book}-p{page.number + 1:04d}-rule-only-{kind}',
                                   'reader': book, 'pdf_sha256': before, 'page': page.number + 1,
                                   'adjacent_page': page.number + 2, 'heading_kind': kind + '_rule_only',
                                   'heading': title, 'tag': 'rule before ' + title, 'bbox': list(rect),
                                   'direction': 'number_before_next_page_display',
                                   'next_page_heading_bbox': next_body[0]['bbox'],
                                   'rule_width_pt': rect.width, 'rule_stroke_width_pt': drawing.get('width'),
                                   'expected_rule_fraction': rule_fraction, 'expected_rule_width_pt': rule_width,
                                   'scan_context': scans.get(page.number + 1, []),
                                   'adjacent_scan_context': scans.get(page.number + 2, []),
                                   'next_page_text': next_page.get_text()[:3000],
                                   'status': 'PENDING_MASTER_PIXEL_IDENTITY' if 'master' in book else 'PENDING_ACTUAL_VISUAL_REVIEW'}
                            if 'master' not in book:
                                render_pair(row, directory)
                                row['native_pair_image'] = Path(row['native_pair_image']).relative_to(ROOT).as_posix()
                            candidates.append(row)
                            found += 1
            pages = len(doc)
        after = sha(pdf)
        if after != before:
            raise RuntimeError('PDF changed during generated-heading audit: ' + book)
        files.append({'reader': book, 'sha256': before, 'sha256_after': after, 'pages': pages,
                      'stable_during_audit': True, 'generated_heading_count': heading_count,
                      'candidate_count': found})
        print(book, heading_count, 'headings;', found, 'end-of-page candidates', flush=True)
    result = {'status': 'CANDIDATES_REQUIRE_ACTUAL_REVIEW',
              'scope': 'Every page of all seven current publication PDFs. Exact generated apparatus/retained-doubt headings and generated Scans first–last range headings are tested for absence of a following body line, excluding footers, marginal source markers and isolated daggers. Generated thin separator rules at the body left edge are tested for separation from the next-page opening heading, using the actual macro widths: .26 of textwidth for apparatus and .2 for retained doubts.',
              'files': files, 'candidates': candidates,
              'primary_candidate_count': sum('master' not in r['reader'] for r in candidates),
              'master_candidate_count': sum('master' in r['reader'] for r in candidates),
              'observations_generated_by_script': False}
    (ROOT / args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'primary_candidates': result['primary_candidate_count'],
                      'master_candidates': result['master_candidate_count'], 'output': args.output}))


if __name__ == '__main__':
    main()
