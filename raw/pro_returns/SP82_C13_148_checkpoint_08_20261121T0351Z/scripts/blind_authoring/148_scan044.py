#!/usr/bin/env python3
"""Independent visual transcription of the twenty authorized scan044 boxes.

The only source inputs are scan.jpg and boxes.tsv in the blind input directory.
Readings were completed after visually inspecting every native crop with
view_image.  No OCR, outside transcription, comparison, or TeX compilation was
used.  This script preserves those readings and performs only self-validation.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

from PIL import Image


WORKSPACE = Path('/workspace/scratch/8132fe1cca43')
INPUT = WORKSPACE / 'work/blind_inputs/148_scan044'
PROJECT = WORKSPACE / 'work/SP82_C13_148'
CROPS = PROJECT / 'crops/second/148_scan044'
DISPLAY = WORKSPACE / 'work/blind_display/148_scan044'
OUTPUT = PROJECT / 'second'


# These twenty readings were all completed before the first TSV was saved.
READINGS = {
    'S44-author1': r'''1''',
    'S44-title': r'''\uline{Groupoïdes de Teichmüller}.''',
    'S44-circled1': r'''\textcircled{1}''',
    'S44-first-formula': r'''\(\mathcal{T}_{\mathrm{top}}^{+} \sim \mathcal{T}_{\mathrm{top}}\)''',
    'S44-first-descriptor': r'''(\uline{groupoïde de Teichmüller} \uuline{orienté} \uline{topologique})''',
    'S44-objects': r'''\uline{Objets} : surfaces \uline{à bord} compactes orientées
\margin{\(\mathcal{T}\),}''',
    'S44-fleches': r'''\uline{flèches} : classes d'isotopie d'iso (conservant l'orientation)''',
    'S44-upper-note': r'''\margin{Finalement, tant
qu'on ne travaille pas
au point de vue arith-
métique, il semble que
c'est le gr. \(\mathcal{T}^{\pm}\) qui est
le plus utilisé; \deleted{\unsure{tout|tant}}
c'est lui qui \unsure{mérite}
donc ici la \unsure{notation}
\unsure{la|le} plus simple
\(\mathcal{T}\), et le gr. \unsure{non|or.}
orienté doit s'appeler
\(\mathcal{T}^{+}\).}''',
    'S44-upper-deletion': r'''\deleted{\unsure{tout|tant}}''',
    'S44-nect': r'''(ne conservant pas \(\mathrm{néc}^{t}\). l'orientation)''',
    'S44-one-object': r'''Soit \([\pm 1]\) le groupoïde ayant un seul objet (par
exemple \(e = \unsure{\varnothing|\phi}\)) et comme groupe d'autom \(\pm 1\). On a''',
    'S44-signature': r'''\diagram{\begin{tikzcd}
\mathcal{T}_{\mathrm{top}}^{\pm} \arrow[r, "\chi"] & [\pm 1]
\end{tikzcd}}''',
    'S44-fibre': r'''dont la \uline{fibre} \deleted{est} (ou noyau) est \(\mathcal{T}_{\mathrm{top}}^{+} = \mathcal{T}_{\mathrm{top}}\).''',
    'S44-deleted-est': r'''\deleted{est}''',
    'S44-lower-note': r'''\margin{\unsure{connexité|connexe},
si on se borne
à des surfaces
connexes!
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (0,1.2) -- (0,0.12) .. controls (0,0) and (-0.10,0) .. (-0.55,0.15);
\end{tikzpicture}}}''',
    'S44-complex-formula': r'''\(S_{*}\mathcal{T}\unsure{D|\mathcal{D}}_{\mathrm{top}}^{+} \sim S_{*}\mathcal{T}\unsure{D|\mathcal{D}}_{\mathrm{top}}\),''',
    'S44-final-descriptor': r'''``\uline{groupoïde de Teichmüller} \inserted{\uline{orienté}} \uline{spécial dévissé topologique}'' ''',
    'S44-oriente': r'''\inserted{\uline{orienté}}''',
    'S44-devisse': r'''\uline{dévissé}''',
    'S44-folio43': r'''\margin{43}''',
}

READINGS = {box: reading.rstrip() for box, reading in READINGS.items()}


# Every listed proxy is a transformation of the entire corresponding crop.
# All were successfully displayed with view_image; no output was truncated.
PROXIES = {
    'S44-title': [('S44-title-2x.png', '2x whole-crop enlargement')],
    'S44-first-formula': [('S44-first-formula-2x.png', '2x whole-crop enlargement')],
    'S44-first-descriptor': [('S44-first-descriptor-2x.png', '2x whole-crop enlargement')],
    'S44-objects': [('S44-objects-2x.png', '2x whole-crop enlargement')],
    'S44-fleches': [('S44-fleches-2x.png', '2x whole-crop enlargement')],
    'S44-upper-note': [
        ('S44-upper-note-rot30-2x.png', 'whole crop rotated 30 degrees clockwise, expanded white canvas, then enlarged 2x'),
        ('S44-upper-note-rot33-contrast1p8-2x.png', 'whole crop contrast factor 1.8, rotated 33 degrees clockwise, expanded white canvas, then enlarged 2x'),
    ],
    'S44-upper-deletion': [('S44-upper-deletion-rot30-2x.png', 'whole crop rotated 30 degrees clockwise, expanded white canvas, then enlarged 2x')],
    'S44-nect': [('S44-nect-2x.png', '2x whole-crop enlargement')],
    'S44-one-object': [('S44-one-object-2x.png', '2x whole-crop enlargement')],
    'S44-signature': [('S44-signature-2x.png', '2x whole-crop enlargement')],
    'S44-fibre': [('S44-fibre-2x.png', '2x whole-crop enlargement')],
    'S44-deleted-est': [('S44-deleted-est-2x.png', '2x whole-crop enlargement')],
    'S44-lower-note': [('S44-lower-note-rot30-3x.png', 'whole crop rotated 30 degrees clockwise, expanded white canvas, then enlarged 3x')],
    'S44-complex-formula': [('S44-complex-formula-2x.png', '2x whole-crop enlargement')],
    'S44-final-descriptor': [('S44-final-descriptor-2x.png', '2x whole-crop enlargement')],
    'S44-oriente': [('S44-oriente-2x.png', '2x whole-crop enlargement')],
    'S44-devisse': [('S44-devisse-2x.png', '2x whole-crop enlargement')],
    'S44-folio43': [('S44-folio43-2x.png', '2x whole-crop enlargement')],
}

EXCLUSIONS = {
    'S44-author1': 'No adjacent text excluded.',
    'S44-title': 'No adjacent text excluded. The final full stop is outside the underline.',
    'S44-circled1': 'No adjacent text excluded. The enclosing oval is represented by textcircled.',
    'S44-first-formula': 'Tiny clipped strokes at the bottom edge belonging to the following line are excluded.',
    'S44-first-descriptor': 'Clipped fragments along the upper edge from the preceding formula are excluded.',
    'S44-objects': 'Clipped fragments from the preceding and following main lines, and incomplete diagonal margin-note letters, are excluded. The complete isolated diagonal marginal T and comma at the right are retained explicitly as margin text.',
    'S44-fleches': 'The overlapping objects line at the upper edge and incomplete diagonal margin-note fragments at upper right are excluded.',
    'S44-upper-note': 'Horizontal main-text fragments entering from the left and bottom edges are excluded. The dark page-edge stripe at right is not writing and is excluded. The diagonal marginal note, its formulas, and its cancellation are retained.',
    'S44-upper-deletion': 'Surrounding clipped unstruck words from adjacent note lines are excluded; only the complete struck word is foreground in this box.',
    'S44-nect': 'No adjacent words excluded.',
    'S44-one-object': 'A clipped stroke at the bottom edge from the following diagram is excluded.',
    'S44-signature': 'A small clipped stroke at the upper edge from the preceding line is excluded.',
    'S44-fibre': 'The partial formula entering along the upper edge from the preceding diagram is excluded.',
    'S44-deleted-est': 'No adjacent words excluded; the entire struck word is retained.',
    'S44-lower-note': 'A partial main-text letter at right and the isolated clipped stroke at the bottom edge are excluded. The long descending hooked stroke beside surfaces, ending toward connexes, is retained as a TikZ drawing.',
    'S44-complex-formula': 'The partial inserted word at the lower edge and other clipped strokes from the descriptor below are excluded; the complete formula and its trailing comma are retained.',
    'S44-final-descriptor': 'Clipped formula fragments along the upper edge are excluded. The inserted underlined word and its placement mark are encoded by inserted.',
    'S44-oriente': 'The clipped underlying letters from spécial and other neighboring main-line fragments are excluded. The curved insertion mark is encoded by inserted.',
    'S44-devisse': 'Only the complete word and its visible underline are foreground; neighboring clipped strokes are excluded.',
    'S44-folio43': 'A small isolated speck at the upper edge is treated as background; the handwritten folio is retained.',
}

UNCERTAINTIES = {
    'S44-first-descriptor': [
        'A long pale underline spans the descriptor; a shorter darker underline under orienté gives that word two visible underline strokes. Encoded with uuline for orienté.'
    ],
    'S44-upper-note': [
        'The crossed word has candidate readings tout and tant; cancellation is retained.',
        'mérite and notation remain marked unsure rather than resolved by sentence meaning.',
        'The short word preceding plus simple may be la or le.',
        'The short word after the last gr. is uncertain; non and or. are retained as candidates without grammatical or mathematical repair.'
    ],
    'S44-upper-deletion': ['The struck word may read tout or tant.'],
    'S44-nect': ['The abbreviated word is preserved as néc with a superscript t and following full stop; it is not expanded.'],
    'S44-one-object': ['The slashed oval after e = may represent varnothing or phi; both symbol candidates are retained.'],
    'S44-lower-note': ['The first word is uncertain: connexité or connexe. The drawing is represented schematically with its downward and leftward hooked direction retained.'],
    'S44-complex-formula': ['The D-shaped capitals could be ordinary D or calligraphic D; both candidates are retained at both positions.'],
}


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_name = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', newline='',
                                         dir=path.parent, prefix=path.name + '.',
                                         suffix='.tmp', delete=False) as handle:
            tmp_name = handle.name
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    finally:
        if tmp_name and os.path.exists(tmp_name):
            os.unlink(tmp_name)


def brace_balance(text: str) -> bool:
    depth = 0
    for i, char in enumerate(text):
        if char not in '{}':
            continue
        # A brace escaped by an odd number of backslashes is a literal glyph.
        backslashes = 0
        j = i - 1
        while j >= 0 and text[j] == '\\':
            backslashes += 1
            j -= 1
        if backslashes % 2:
            continue
        depth += 1 if char == '{' else -1
        if depth < 0:
            return False
    return depth == 0


def main() -> None:
    with (INPUT / 'boxes.tsv').open(encoding='utf-8', newline='') as handle:
        boxes = list(csv.DictReader(handle, delimiter='\t'))
    order = [row['box'] for row in boxes]
    assert len(boxes) == 20
    assert len(set(order)) == 20
    assert list(READINGS) == order, 'Own readings must cover the twenty fixed boxes in order.'
    assert all(READINGS.values())
    for box, reading in READINGS.items():
        assert brace_balance(reading), box
        assert reading.count(r'\(') == reading.count(r'\)'), box
        assert '\x00' not in reading and '\r' not in reading, box

    CROPS.mkdir(parents=True, exist_ok=True)
    entries = []
    with Image.open(INPUT / 'scan.jpg') as source:
        for row in boxes:
            box = row['box']
            rect = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
            crop_path = CROPS / (box + '.png')
            if not crop_path.exists():
                source.crop(rect).save(crop_path)
            with Image.open(crop_path) as crop:
                assert crop.size == (rect[2] - rect[0], rect[3] - rect[1]), box
            successful_views = [{
                'path': str(crop_path),
                'tool': 'view_image',
                'result': 'success; complete image displayed and visually inspected',
                'transform': 'none; native fixed rectangle',
            }]
            for filename, transform in PROXIES.get(box, []):
                proxy_path = DISPLAY / filename
                assert proxy_path.exists(), proxy_path
                successful_views.append({
                    'path': str(proxy_path),
                    'tool': 'view_image',
                    'result': 'success; complete image displayed and visually inspected',
                    'transform': transform,
                    'transform_source': str(crop_path),
                    'subrectangle_used': False,
                })
            entries.append({
                'box': box,
                'fixed_rectangle': list(rect),
                'native_crop': str(crop_path),
                'successful_views': successful_views,
                'excluded_background': EXCLUSIONS[box],
                'uncertainties': UNCERTAINTIES.get(box, []),
            })

    buffer = io.StringIO(newline='')
    writer = csv.writer(buffer, delimiter='\t', quoting=csv.QUOTE_MINIMAL,
                        lineterminator='\n')
    writer.writerow(['box', 'reading'])
    writer.writerows((box, READINGS[box]) for box in order)
    tsv = buffer.getvalue()
    parsed = list(csv.DictReader(io.StringIO(tsv, newline=''), delimiter='\t'))
    assert [row['box'] for row in parsed] == order
    assert [row['reading'] for row in parsed] == [READINGS[box] for box in order]

    journal = {
        'scan_id': '148_scan044',
        'method': 'strictly independent blind visual transcription',
        'authorized_inputs': [str(INPUT / 'scan.jpg'), str(INPUT / 'boxes.tsv')],
        'source_sha256': {
            name: hashlib.sha256((INPUT / name).read_bytes()).hexdigest()
            for name in ('scan.jpg', 'boxes.tsv')
        },
        'all_twenty_readings_completed_before_first_tsv_save': True,
        'all_native_crops_successfully_viewed': True,
        'truncated_image_outputs_counted_as_views': False,
        'ocr_used': False,
        'research_used': False,
        'other_readings_or_witnesses_accessed': False,
        'comparison_or_adjudication_performed': False,
        'tex_compiled': False,
        'subrectangle_transformations_used': False,
        'verification_scope': 'Own output order, coverage, TSV round trip, balanced braces and inline math delimiters, and native crop dimensions only.',
        'typographic_note': 'Prose double quotations use two backticks and two apostrophes. Double quotes inside tikz-cd are label syntax, not typographic quotation marks.',
        'repeat_views': [
            str(CROPS / 'S44-lower-note.jxl'),
            str(DISPLAY / 'S44-upper-note-rot30-2x.png'),
        ],
        'boxes': entries,
        'completed_utc': datetime.now(timezone.utc).isoformat(),
    }

    output_tsv = OUTPUT / '148_scan044_second.tsv'
    output_journal = OUTPUT / '148_scan044_blind_journal.json'
    atomic_write(output_tsv, tsv)
    atomic_write(output_journal, json.dumps(journal, ensure_ascii=False, indent=2) + '\n')

    # Read back only this agent's own newly saved outputs.
    with output_tsv.open(encoding='utf-8', newline='') as handle:
        saved = list(csv.DictReader(handle, delimiter='\t'))
    assert saved == parsed
    saved_journal = json.loads(output_journal.read_text(encoding='utf-8'))
    assert [entry['box'] for entry in saved_journal['boxes']] == order
    assert all(entry['successful_views'] for entry in saved_journal['boxes'])
    print(json.dumps({
        'rows': len(saved),
        'native_views': len(entries),
        'unique_proxy_views': sum(len(PROXIES.get(box, [])) for box in order),
        'tsv': str(output_tsv),
        'journal': str(output_journal),
        'checks': 'own output coverage, order, quoted multiline TSV round trip, braces, math delimiters, and crop dimensions passed',
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
