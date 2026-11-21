#!/usr/bin/env python3
"""Independent scan029 second reading, authored only from its fixed crops."""

import csv
import json
import os
import tempfile
from pathlib import Path


BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan029')
OUT = BASE / 'second'

READINGS = [
    ('B029-01', r'\margin{\(M_{\unsure{0|8},5}\)}'),
    ('B029-02', r'\margin{\mspage{28}}'),
]

JOURNAL = {
    'page': '148_scan029',
    'role': 'independent blind second reader',
    'input_image': '/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan029/scan.jpg',
    'input_boxes': '/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan029/boxes.tsv',
    'box_count': 2,
    'all_boxes_successfully_viewed': True,
    'whole_page_viewed': False,
    'crop_helper_invocations': 1,
    'no_other_page_or_reading_consulted': True,
    'no_ocr_or_recognition_libraries': True,
    'no_external_research_or_tex_compilation': True,
    'boxes': [
        {
            'box': 'B029-01',
            'evidence': str(BASE / 'crops/second/148_scan029/B029-01.jxl'),
            'successful_views': [
                str(DISPLAY / 'B029-01.jpg'),
                str(DISPLAY / 'B029-01-nearest.png'),
            ],
            'rotation_degrees': 0,
            'observation': (
                'Capital M followed by two lower indices separated by a comma. '
                'The first index is uncertain between 0 and 8: its upper turn '
                'and lower loop were checked with a nearest-neighbor '
                'magnification of the saved native crop. The final digit is '
                'read as 5, with its separated top stroke retained as part '
                'of the digit rather than assumed to be an overbar. No '
                'mathematical expectation used to resolve the first index.'
            ),
        },
        {
            'box': 'B029-02',
            'evidence': str(BASE / 'crops/second/148_scan029/B029-02.jxl'),
            'successful_views': [str(DISPLAY / 'B029-02.jpg')],
            'rotation_degrees': 0,
            'observation': 'Marginal handwritten page number read 28.',
        },
    ],
}


def atomic_write(path, callback):
    fd, temporary = tempfile.mkstemp(
        prefix='.' + path.stem + '.', suffix='.tmp', dir=path.parent
    )
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            callback(stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def write_tsv(stream):
    writer = csv.writer(stream, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['box', 'reading'])
    writer.writerows(READINGS)


def write_journal(stream):
    json.dump(JOURNAL, stream, ensure_ascii=False, indent=2)
    stream.write('\n')


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    tsv = OUT / '148_scan029_second.tsv'
    journal = OUT / '148_scan029_blind_journal.json'
    atomic_write(tsv, write_tsv)
    atomic_write(journal, write_journal)
    print(json.dumps({
        'tsv': str(tsv),
        'journal': str(journal),
        'boxes': len(READINGS),
        'tsv_bytes': tsv.stat().st_size,
        'journal_bytes': journal.stat().st_size,
    }))
