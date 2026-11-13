#!/usr/bin/env python3
"""Arrange already rendered, unreviewed pages for actual human/model inspection.

This does not select additional PDF pages, render PDFs, inspect images, or change
review status. It checks the existing image evidence and writes small overview
grids plus a page/hash index. The default is sixteen 550px-wide page images.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from verify_pdf import sha256, image_pixel_sha256, review_is_attributed


def arrange(directory, output=None, width=550, columns=4, rows_per_sheet=4):
    directory = Path(directory)
    destination = Path(output) if output else directory / 'pending_review'
    with (directory / 'VISUAL_REVIEW.tsv').open(newline='') as handle:
        inventory = list(csv.DictReader(handle, delimiter='\t'))
    pending = [row for row in inventory if not review_is_attributed(row)]
    destination.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype('DejaVuSans.ttf', 20)
    heading_font = ImageFont.truetype('DejaVuSans.ttf', 24)
    page_height = max((round(int(row['image_height']) * width / int(row['image_width']))
                       for row in pending), default=0)
    gap, label_height, heading_height = 14, 34, 42
    batch_size = columns * rows_per_sheet
    sheets = []
    for offset in range(0, len(pending), batch_size):
        group = pending[offset:offset + batch_size]
        used_rows = (len(group) + columns - 1) // columns
        canvas = Image.new('RGB',
                           (gap + columns * (width + gap),
                            heading_height + used_rows * (page_height + label_height + gap)),
                           '#dddddd')
        draw = ImageDraw.Draw(canvas)
        number = len(sheets) + 1
        draw.text((gap, 8), f'{directory.name} | pending review {number}',
                  font=heading_font, fill='black')
        pages = []
        for index, row in enumerate(group):
            image_path = directory / row['full_page_image']
            if (sha256(image_path) != row['png_sha256'] or
                    image_pixel_sha256(image_path) != row['rendered_pixel_sha256']):
                raise ValueError(f"Page {row['page']}: existing image evidence has changed.")
            x = gap + (index % columns) * (width + gap)
            y = heading_height + (index // columns) * (page_height + label_height + gap)
            draw.text((x, y + 3), f"Page {row['page']}", font=font, fill='black')
            with Image.open(image_path) as source:
                height = round(source.height * width / source.width)
                thumbnail = source.convert('RGB').resize((width, height), Image.Resampling.LANCZOS)
                canvas.paste(thumbnail, (x, y + label_height))
            pages.append({'page': int(row['page']), 'pdf_sha256': row['pdf_sha256'],
                          'pixel_sha256': row['rendered_pixel_sha256'],
                          'png_sha256': row['png_sha256'], 'full_page_image': row['full_page_image'],
                          'reasons': row['reasons']})
        filename = f'pending_{number:03d}.png'
        canvas.save(destination / filename)
        sheets.append({'image': filename, 'pages': pages})
    result = {'book': directory.name, 'selected_pages': len(inventory),
              'pending_pages': len(pending), 'page_thumbnail_width': width,
              'columns': columns, 'rows_per_sheet': rows_per_sheet, 'sheets': sheets,
              'review_status_changed': False, 'inspection_claimed': False,
              'policy': 'Only arrange existing unreviewed images after validating stored PNG and pixel hashes.'}
    (destination / 'PENDING_REVIEW_INDEX.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory')
    parser.add_argument('--output')
    parser.add_argument('--width', type=int, default=550)
    parser.add_argument('--columns', type=int, default=4)
    parser.add_argument('--rows', type=int, default=4)
    args = parser.parse_args()
    if min(args.width, args.columns, args.rows) < 1:
        parser.error('Grid dimensions must be positive.')
    result = arrange(args.directory, args.output, args.width, args.columns, args.rows)
    print(json.dumps({key: result[key] for key in
                      ('book', 'selected_pages', 'pending_pages', 'review_status_changed', 'inspection_claimed')}))


if __name__ == '__main__':
    main()
