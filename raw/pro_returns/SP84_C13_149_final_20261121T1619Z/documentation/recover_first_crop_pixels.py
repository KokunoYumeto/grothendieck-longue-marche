#!/usr/bin/env python3
"""Verify five recovered first-crop rectangles against every saved RGB pixel.

Default execution is read-only. --record writes the evidence note/JSON once and
appends only verified missing rows to first_crop_coordinates.tsv. No scan, crop,
page, review, adjudication, or frozen independent return is modified.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps, __version__ as pillow_version

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
DOCUMENTATION = EDITION / 'documentation'
CASES = [
    ('005', '19', (465, 865, 1130, 1005), True),
    ('010', '14', (1172, 2080, 1631, 2189), True),
    ('010', '15', (272, 2184, 741, 2289), True),
    ('010', '16', (925, 2242, 1265, 2345), True),
    ('018', '10', (280, 1411, 624, 1525), False),
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_case(scan: str, number: str, box: tuple[int, ...], sharpen: bool) -> dict:
    source_path = ROOT / f'source/SP84_C13_149_scans/149_scan{scan}.jpg'
    crop_path = EDITION / f'crops/149_scan{scan}_c{number}.png'
    source = Image.open(source_path).convert('RGB')
    saved = Image.open(crop_path).convert('RGB')
    reproduced = ImageOps.autocontrast(source.crop(box), cutoff=0.5)
    output_size = (2600, round(reproduced.height * 2600 / reproduced.width))
    reproduced = reproduced.resize(output_size, Image.Resampling.LANCZOS)
    if sharpen:
        reproduced = reproduced.filter(
            ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3)
        )
    if reproduced.size != saved.size:
        raise AssertionError(f'{crop_path.name}: dimensions differ')
    difference = ImageChops.difference(reproduced, saved)
    # Count differences in each of the three channels, independently of a bbox.
    histogram = difference.histogram()
    mismatched_channels = sum(
        sum(histogram[offset + 1:offset + 256]) for offset in (0, 256, 512)
    )
    maximum_difference = max(hi for lo, hi in difference.getextrema())
    assert difference.getbbox() is None, crop_path.name
    assert mismatched_channels == 0, crop_path.name
    assert maximum_difference == 0, crop_path.name
    saved_pixel_sha = sha256(saved.tobytes())
    reproduced_pixel_sha = sha256(reproduced.tobytes())
    assert saved_pixel_sha == reproduced_pixel_sha, crop_path.name
    return {
        'crop': str(crop_path.relative_to(EDITION)),
        'source': str(source_path.relative_to(ROOT)),
        'box_xyxy_original_pixels': list(box),
        'source_size': list(source.size),
        'source_rectangle_size': [box[2] - box[0], box[3] - box[1]],
        'saved_size': list(saved.size),
        'reproduced_size': list(reproduced.size),
        'pipeline': {
            'source_mode': 'RGB',
            'crop_coordinates': 'Pillow crop: left/top inclusive, right/bottom exclusive',
            'autocontrast': {'cutoff': 0.5, 'phase': 'before resize'},
            'resize': {'width': 2600, 'height': 'round(crop_height*2600/crop_width)',
                       'resample': 'PIL.Image.Resampling.LANCZOS'},
            'post_resize_unsharp_mask': (
                {'radius': 1.5, 'percent': 120, 'threshold': 3} if sharpen else None
            ),
            'rotation_degrees': 0,
        },
        'source_file_sha256': sha256(source_path.read_bytes()),
        'saved_crop_file_sha256': sha256(crop_path.read_bytes()),
        'saved_rgb_pixels_sha256': saved_pixel_sha,
        'reproduced_rgb_pixels_sha256': reproduced_pixel_sha,
        'rgb_channel_values_compared': saved.width * saved.height * 3,
        'mismatched_rgb_channel_values': mismatched_channels,
        'maximum_channel_difference': maximum_difference,
        'difference_bbox': None,
        'pixel_exact': True,
    }


def make_note(evidence: dict) -> str:
    lines = [
        '# Exact first-crop coordinate recovery by pixel reproduction',
        '',
        f"Verified {evidence['verified_utc']} using Pillow {pillow_version}.",
        '',
        '## Result',
        '',
        'All five requested rectangles are recovered and verified against every RGB '
        'channel value of their existing saved crops. The acceptance criterion is '
        'zero differing channel values and identical full RGB pixel hashes. Template '
        'correlation alone was not accepted as coordinate provenance.',
        '',
        '| Saved crop | Original rectangle (x0, y0, x1, y1) | Saved pixels | Sharpening | Differing channel values |',
        '|---|---|---|---|---|',
    ]
    for item in evidence['cases']:
        box = tuple(item['box_xyxy_original_pixels'])
        size = ' × '.join(str(v) for v in item['saved_size'])
        sharpen = 'UnsharpMask 1.5 / 120 / 3' if item['pipeline']['post_resize_unsharp_mask'] else 'None'
        lines.append(f"| {item['crop']} | {box} | {size} | {sharpen} | 0 |")
    lines += [
        '',
        'Coordinates use the original JPEG pixel grid. Left/top are inclusive; '
        'right/bottom are exclusive, as in Pillow `Image.crop`.',
        '',
        '## Discovery and verification',
        '',
        'The existing metadata supplied a candidate for scan018 c10. Applying '
        'autocontrast with cutoff 0.5 before the resize reproduced that saved crop '
        'exactly. The earlier test without this contrast step had failed.',
        '',
        'For the other four, a pixel-only scale search compared each saved crop with '
        'its original scan using FFT normalized cross-correlation. Both were '
        'downsampled by about three for initial location/scale discovery. The search '
        'was then refined on the original pixel grid, considering integer rectangle '
        'widths/heights whose rounded 2600-pixel-wide output matched the saved '
        'dimensions. No handwriting was read, no OCR was performed, and no proposed '
        'source text was used as a template.',
        '',
        'The best integer rectangles initially reproduced almost all pixels with '
        'autocontrast 0.5 and LANCZOS, but sparse edge differences remained. A parameter '
        'search on an interior pixel tile identified UnsharpMask radius 1.5, percent '
        '120, threshold 3. That candidate filter was then applied to each entire '
        'reproduced image. All four complete RGB arrays became identical to their '
        'saved targets. The tile search was only a way to discover parameters; '
        'acceptance required the complete-image checks.',
        '',
        'The established reproducing pipeline is:',
        '',
        '1. Open the original JPEG and convert to RGB.',
        '2. Crop the exact integer rectangle in the table.',
        '3. Apply `ImageOps.autocontrast(..., cutoff=0.5)`.',
        '4. Resize to `(2600, round(height*2600/width))` with LANCZOS.',
        '5. For scan005 c19 and scan010 c14/c15/c16 only, apply '
        '`ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3)`.',
        '6. Compare every output RGB channel value with the existing PNG.',
        '',
        'No rotation, resampling of the source scan beforehand, additional contrast '
        'enhancement, or source-image edit is needed. This records an exactly '
        'reproducing pipeline; it does not claim that the historical shell command '
        'itself was recovered or that all conceivable processing pipelines are unique.',
        '',
        '## Reproduction',
        '',
        'Run from the workspace root:',
        '',
        '```sh',
        'python3 edition/documentation/recover_first_crop_pixels.py',
        '```',
        '',
        'The default invocation is read-only. It checks output dimensions, the '
        '`ImageChops` difference bounding box, the count of nonzero values in each '
        'difference channel, the maximum channel difference, and full RGB pixel '
        'hashes. It fails immediately if any target differs. `--record` is the '
        'explicit one-time evidence/coordinate-table write mode.',
        '',
        '## Hash evidence',
        '',
        f"Verification-script SHA-256: `{evidence['verification_script_sha256']}`.",
        '',
        'The machine-readable companion `coordinate_recovery_reader_c.json` records '
        'source-file, saved-PNG-file, saved-RGB-pixel, and reproduced-RGB-pixel SHA-256 '
        'hashes, dimensions, parameters, and zero-difference counts for all five cases.',
        '',
    ]
    for item in evidence['cases']:
        lines += [
            f"### {item['crop']}", '',
            f"- Source SHA-256: `{item['source_file_sha256']}`",
            f"- Saved PNG SHA-256: `{item['saved_crop_file_sha256']}`",
            f"- Saved and reproduced RGB SHA-256: `{item['saved_rgb_pixels_sha256']}`",
            f"- RGB channel values compared: {item['rgb_channel_values_compared']:,}; differing values: 0; maximum difference: 0.",
            '',
        ]
    lines += [
        '## Mutation scope', '',
        'Only the five proven rows are appended to `first_crop_coordinates.tsv`. '
        'The existing rows are preserved byte-for-byte. This evidence note, its '
        'JSON companion, and the verification script are separate new documentation. '
        'No original scan, saved crop, page, review JSON, frozen TSV, or adjudication '
        'file was modified.',
        '',
    ]
    return '\n'.join(lines)


def record(evidence: dict) -> None:
    json_path = DOCUMENTATION / 'coordinate_recovery_reader_c.json'
    note_path = DOCUMENTATION / 'coordinate_recovery_reader_c.md'
    if json_path.exists() or note_path.exists():
        raise FileExistsError('Evidence already exists; default read-only verification remains available.')
    table = DOCUMENTATION / 'first_crop_coordinates.tsv'
    with table.open('r+', newline='') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        before = stream.read()
        reader = csv.DictReader(io.StringIO(before), delimiter='\t')
        fields = ['crop', 'x0', 'y0', 'x1', 'y1', 'coordinate_provenance']
        if reader.fieldnames != fields:
            raise AssertionError('Unexpected coordinate-table columns')
        existing = {row['crop']: row for row in reader}
        additions = []
        for item in evidence['cases']:
            box = item['box_xyxy_original_pixels']
            old = existing.get(item['crop'])
            if old:
                if [int(old[k]) for k in fields[1:5]] != box:
                    raise AssertionError(f"Conflicting existing coordinates: {item['crop']}")
                continue
            additions.append({
                'crop': item['crop'],
                **dict(zip(fields[1:5], box)),
                'coordinate_provenance': (
                    'documentation/coordinate_recovery_reader_c.json; '
                    'exact complete RGB pixel reproduction with '
                    'documentation/recover_first_crop_pixels.py; '
                    'documentation/coordinate_recovery_reader_c.md'
                ),
            })
        if len(additions) != 5:
            raise AssertionError(f'Expected exactly five missing rows, found {len(additions)}')
        evidence['coordinate_table_sha256_before_append'] = sha256(before.encode())
        buffer = io.StringIO(newline='')
        writer = csv.DictWriter(buffer, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writerows(additions)
        suffix = ('' if before.endswith('\n') else '\n') + buffer.getvalue()
        evidence['coordinate_table_sha256_after_append'] = sha256((before + suffix).encode())
        evidence['appended_row_count'] = len(additions)
        with json_path.open('x') as out:
            json.dump(evidence, out, ensure_ascii=False, indent=2)
            out.write('\n')
        with note_path.open('x') as out:
            out.write(make_note(evidence))
        stream.seek(0, os.SEEK_END)
        stream.write(suffix)
        stream.flush()
        os.fsync(stream.fileno())
        stream.seek(0)
        after = stream.read()
        assert after == before + suffix, 'The coordinate table did not change by append only'
        fcntl.flock(stream, fcntl.LOCK_UN)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', action='store_true', help='Create new evidence and append five proven rows')
    args = parser.parse_args()
    cases = [verify_case(*case) for case in CASES]
    evidence = {
        'verified_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'reader': 'reader_c',
        'pillow_version': pillow_version,
        'verification_script': 'documentation/recover_first_crop_pixels.py',
        'verification_script_sha256': sha256(Path(__file__).read_bytes()),
        'acceptance': 'Every reproduced RGB channel value equals the existing saved PNG',
        'cases': cases,
    }
    if args.record:
        record(evidence)
    for case in cases:
        print(case['crop'], case['box_xyxy_original_pixels'], 'EXACT',
              case['rgb_channel_values_compared'], 'channel values; zero differences')
    if args.record:
        print('Appended exactly five verified rows; prior coordinate-table bytes preserved.')


if __name__ == '__main__':
    main()
