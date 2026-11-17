#!/usr/bin/env python3
"""Map validation PDF pages to scans and render a mechanical figure-page sample.

Reads the compiled PDF and validation logs only, not page sources or scan images.
Selection uses vector-path geometry, without OCR or interpretation of content.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


def prepare(pdf: Path, stdout: Path, output: Path, max_full_pages: int, dpi: int,
            *, all_pages: bool = False, contact_sheets: int | None = None) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    matches = re.findall(r'^VALIDATION COTE (\d+) SCAN (\d+) PDFPAGE (\d+)$',
                         stdout.read_text(), re.MULTILINE)
    starts = [tuple(map(int, match)) for match in matches]
    if not starts or [x[2] for x in starts] != sorted({x[2] for x in starts}):
        raise ValueError('Missing or non-monotone scan/page markers in the compilation stdout.')
    doc = fitz.open(pdf)
    metadata_path = pdf.parent / 'wrapper_report.json'
    metadata = json.loads(metadata_path.read_text()) if metadata_path.is_file() else {}
    filenames = {(x['cote'], x['scan']): x['filename'] for x in metadata.get('sources', [])}
    mapping = []
    page_to_scan = {}
    for i, (cote, scan, first) in enumerate(starts):
        last = starts[i + 1][2] - 1 if i + 1 < len(starts) else len(doc)
        entry = {'cote': cote, 'scan': scan, 'pdf_first': first, 'pdf_last': last,
                 'pdf_pages': last - first + 1,
                 'source_filename': filenames.get((cote, scan), '')}
        mapping.append(entry)
        for number in range(first, last + 1):
            page_to_scan[number] = (cote, scan)
    if set(page_to_scan) != set(range(1, len(doc) + 1)):
        raise ValueError('Scan mapping does not cover every PDF page exactly once.')
    metrics = []
    for index, page in enumerate(doc):
        number = index + 1
        cote, scan = page_to_scan[number]
        drawings = page.get_drawings()
        significant = [d for d in drawings if d['rect'].width >= 20 and d['rect'].height >= 10]
        curves = sum(sum(item[0] == 'c' for item in d['items']) for d in significant)
        area = sum(min(d['rect'].get_area(), 80000) for d in significant)
        metric = {'pdf_page': number, 'cote': cote, 'scan': scan,
                  'drawing_paths': len(drawings), 'significant_paths': len(significant),
                  'curves': curves, 'significant_area': round(area, 1),
                  'score': round(1000 * len(significant) + 50 * curves + area / 100, 3)}
        metrics.append(metric)
    candidates = [m for m in metrics if m['significant_paths']]
    selected = metrics if all_pages else sorted(
        sorted(candidates, key=lambda m: (-m['score'], m['pdf_page']))[:max_full_pages],
        key=lambda m: m['pdf_page'])
    contact_candidates = metrics if all_pages else candidates
    full_paths = {}
    for entry in selected:
        page = doc[entry['pdf_page'] - 1]
        name = f"cote{entry['cote']}_scan{entry['scan']:03d}_pdf{entry['pdf_page']:03d}.png"
        path = output / name
        page.get_pixmap(dpi=dpi, alpha=False).save(path)
        full_paths[entry['pdf_page']] = path
    try:
        font = ImageFont.truetype('DejaVuSans.ttf', 18)
    except OSError:
        font = ImageFont.load_default()
    contacts = []
    thumb_width = 500
    tile_width = 524
    tile_height = 392
    batch_size = max(1, math.ceil(len(contact_candidates) / contact_sheets)) if contact_sheets else 12
    for offset in range(0, len(contact_candidates), batch_size):
        batch = contact_candidates[offset:offset + batch_size]
        rows = math.ceil(len(batch) / 3)
        sheet = Image.new('RGB', (3 * tile_width, rows * tile_height), '#eceff2')
        draw = ImageDraw.Draw(sheet)
        for index, entry in enumerate(batch):
            page = doc[entry['pdf_page'] - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(0.8, 0.8), alpha=False)
            thumb = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
            thumb.thumbnail((thumb_width, 354), Image.Resampling.LANCZOS)
            x = (index % 3) * tile_width + 12
            y = (index // 3) * tile_height + 12
            label = f"Cote {entry['cote']} / scan {entry['scan']:03d} / PDF {entry['pdf_page']:03d}"
            draw.text((x, y), label, font=font, fill='#16202b')
            sheet.paste(thumb, (x, y + 26))
        prefix = 'all_pages_contact' if all_pages else 'figure_pages_contact'
        path = output / f'{prefix}_{offset // batch_size + 1:02d}.png'
        sheet.save(path)
        contacts.append(str(path))
    for entry in mapping:
        entry['selected_full_pages'] = ' '.join(str(p) for p in full_paths
                                                if entry['pdf_first'] <= p <= entry['pdf_last'])
        entry['thumbnail_pages'] = ' '.join(str(m['pdf_page']) for m in contact_candidates
                                            if entry['pdf_first'] <= m['pdf_page'] <= entry['pdf_last'])
    with (output / 'scan_pdf_mapping.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(mapping[0]))
        writer.writeheader()
        writer.writerows(mapping)
    with (output / 'pdf_page_geometry.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(metrics[0]))
        writer.writeheader()
        writer.writerows(metrics)
    result = {
        'pdf': str(pdf.resolve()), 'pdf_pages': len(doc), 'source_scans': len(mapping),
        'selection_method': ('All PDF pages rendered in order; no content selection or interpretation.' if all_pages else
                             'Vector paths with bounding box at least 20 pt wide and 10 pt high; full-page sample ranked by path count, curve count, and bounded area. No content interpretation.'),
        'candidate_pdf_pages': [m['pdf_page'] for m in candidates],
        'contact_pdf_pages': [m['pdf_page'] for m in contact_candidates],
        'full_page_renders': [{'cote': m['cote'], 'scan': m['scan'], 'pdf_page': m['pdf_page'],
                               'path': str(full_paths[m['pdf_page']])} for m in selected],
        'full_page_dpi': dpi, 'contact_sheets': contacts, 'scan_mapping': mapping,
        'source_pages_read': False, 'source_pages_modified': False,
    }
    (output / 'render_manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    doc.close()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('stdout', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--max-full-pages', type=int, default=12)
    parser.add_argument('--dpi', type=int, default=150)
    parser.add_argument('--all-pages', action='store_true', help='Render every PDF page and include every page in contact sheets.')
    parser.add_argument('--contact-sheets', type=int, help='Distribute contact thumbnails over this many sheets.')
    args = parser.parse_args()
    if args.contact_sheets is not None and args.contact_sheets < 1:
        parser.error('--contact-sheets must be positive')
    result = prepare(args.pdf, args.stdout, args.output, args.max_full_pages, args.dpi,
                     all_pages=args.all_pages, contact_sheets=args.contact_sheets)
    print(json.dumps({k: v for k, v in result.items() if k != 'scan_mapping'}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
