#!/usr/bin/env python3
"""Print a single page's supplied sources and mechanical navigation aids.

This read-only helper never opens an image, performs OCR, decides a reading,
changes a record, or reads research context.  H extraction uses explicit page
markers only; boundary editorial material remains flagged and uninterpreted.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

from assemble_and_index import group_at, loc, mask_comments
from split_hua import PAGE, END, SECTION

DEFAULT_OUT = Path(__file__).resolve().parents[1]
BASE = DEFAULT_OUT.parent
DEFAULT_WITNESSES = BASE / 'source' / 'SP02_CW_10+12_witnesses'
DEFAULT_SCANS = BASE / 'source' / 'SP02_CW_10+12_scans'
IMAGE_SUFFIXES = {'.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.bmp'}


def doubt_loci(text: str) -> list[dict]:
    clean = mask_comments(text)
    rows = []
    for m in re.finditer(r'\\(?:unsure|illegible)\b', clean):
        argument, end = group_at(clean, m.end())
        line, column = loc(clean, m.start())
        rows.append({'line': line, 'column': column, 'macro': m.group(),
                     'exact_locus': text[m.start():end]})
    return rows


def split_md_row(line: str) -> list[str]:
    return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def scan_matches(cell: str, scan: int) -> bool:
    for m in re.finditer(r'\b(\d{1,3})\s*[-–—]\s*(\d{1,3})\b', cell):
        if int(m.group(1)) <= scan <= int(m.group(2)):
            return True
    return scan in [int(x) for x in re.findall(r'(?<!\d)\d{1,3}(?!\d)', cell)]


def doubt_rows(path: Path, scan: int) -> list[dict]:
    out = []
    heading, headers, scan_col = '', [], None
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if line.startswith('#'):
            heading = line
            headers, scan_col = [], None
        if not line.lstrip().startswith('|'):
            continue
        cells = split_md_row(line)
        matches = [i for i, c in enumerate(cells) if re.fullmatch(r'scan(?:\s*page|\(s\)|s)?|page', c, re.I)]
        if matches:
            headers, scan_col = cells, matches[0]
            continue
        if scan_col is not None and scan_col < len(cells) and scan_matches(cells[scan_col], scan):
            out.append({'source_line': n, 'section': heading, 'headers': headers, 'exact_row': line})
    return out


def hua_span(witness_root: Path, mapped: dict, scratch: Path, key: str) -> dict:
    source = witness_root / mapped['hua_file']
    result = {'status': mapped['hua_has'], 'source_path': str(source.resolve()),
              'their_page': int(mapped['their_page']), 'text': None}
    if mapped['hua_has'] != 'text':
        result['note'] = 'page_map supplies no H text for this page; no text is inferred.'
        return result
    raw = source.read_bytes(); lines = raw.splitlines(keepends=True)
    markers = [(int(m.group(1)), n) for n, line in enumerate(lines) if (m := PAGE.match(line))]
    matches = [j for j, (page, _) in enumerate(markers) if page == int(mapped['their_page'])]
    if len(matches) != 1:
        raise ValueError('Expected exactly one explicit H page marker.')
    j = matches[0]; start = markers[j][1]
    stop = markers[j + 1][1] if j + 1 < len(markers) else len(lines)
    stop = next((n for n in range(start, stop) if END.match(lines[n])), stop)
    exact = b''.join(lines[start:stop])
    fragment_path = scratch / 'hua_pages' / f'{key}.tex'
    existing_matches = fragment_path.exists() and fragment_path.read_bytes() == exact
    sections = [n + 1 for n in range(start, stop) if SECTION.match(lines[n])]
    result.update(text=exact.decode('utf-8'), source_start_line=start + 1, source_end_line=stop,
                  fragment_sha256=hashlib.sha256(exact).hexdigest(),
                  exact_fragment_path=str(fragment_path.resolve()) if existing_matches else None,
                  section_command_lines=sections,
                  boundary_warning='Span is exact marker-to-marker source. Section headings or editorial notes near its end may introduce the following page; no attribution is inferred.')
    return result


def packet(key: str, witnesses=DEFAULT_WITNESSES, scans=DEFAULT_SCANS,
           output=DEFAULT_OUT, scratch=BASE / 'work') -> dict:
    witnesses, scans, output, scratch = map(Path, (witnesses, scans, output, scratch))
    if key.endswith('.tex'):
        key = key[:-4]
    with (witnesses / 'page_map.tsv').open(encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    matches = [r for r in rows if Path(r['codex_file']).stem == key]
    if len(matches) != 1:
        raise ValueError('Supply an exact C page basename from page_map, without a directory.')
    mapped = matches[0]; scan = int(mapped['our_scan'])
    c_path = witnesses / mapped['codex_file']; c_text = c_path.read_text(encoding='utf-8')
    folder = witnesses / 'codex' / mapped['folder']
    inventory_files = list(folder.glob('*_inventory.csv'))
    doubts_files = list(folder.glob('*_doubts.md'))
    if len(inventory_files) != 1 or len(doubts_files) != 1:
        raise ValueError('Expected one C inventory and one C doubts file for the folder.')
    with inventory_files[0].open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        inventory_headers = reader.fieldnames
        inventory = [r for r in reader if int(r['scan']) == scan and str(r.get('cote', mapped['cote'])) == mapped['cote']]
    image_paths = []
    for suffix in ['', '_a', '_b']:
        path = scans / f'{key}{suffix}.jpg'
        image_paths.append({'view': 'whole' if not suffix else suffix[1:], 'path': str(path.resolve()), 'exists': path.is_file()})
    crop_files = []
    short_prefix = f"{mapped['cote']}-{scan:03d}-"
    for search_dir in [scratch / 'crops', scratch / 'reproduced_crops', output / 'evidence']:
        if search_dir.exists():
            for path in search_dir.rglob('*'):
                if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES and (path.name.startswith(short_prefix) or path.name.startswith(key + '__')):
                    crop_files.append(str(path.resolve()))
    record_path = output / 'documentation/page_records' / f'{key}.json'
    recipes = json.loads(record_path.read_text(encoding='utf-8')).get('crops', []) if record_path.exists() else []
    return {'key': key, 'folder': mapped['folder'], 'cote': mapped['cote'], 'our_scan': scan,
            'C': {'path': str(c_path.resolve()), 'text': c_text,
                  'sha256': hashlib.sha256(c_path.read_bytes()).hexdigest()},
            'H': hua_span(witnesses, mapped, scratch, key),
            'inventory': {'path': str(inventory_files[0].resolve()), 'headers': inventory_headers, 'rows': inventory},
            'doubts': {'macro_loci': doubt_loci(c_text), 'witness_doubts_path': str(doubts_files[0].resolve()),
                       'matching_witness_rows': doubt_rows(doubts_files[0], scan),
                       'note': 'Matching witness rows are mechanical selections by their Scan/Page column. Macro loci are exact positions in C, not visual findings.'},
            'images': {'supplied_images': image_paths, 'existing_crop_paths': sorted(set(crop_files)),
                       'recorded_crop_recipes': recipes,
                       'note': 'Paths and recipe metadata only; this helper never opens image bytes.'}}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('page_key')
    ap.add_argument('--witness-root', type=Path, default=DEFAULT_WITNESSES)
    ap.add_argument('--scan-root', type=Path, default=DEFAULT_SCANS)
    ap.add_argument('--output', type=Path, default=DEFAULT_OUT)
    ap.add_argument('--scratch', type=Path, default=BASE / 'work')
    ap.add_argument('--sections', default='images,C,H,inventory,doubts', help='Comma-separated sections: images,C,H,inventory,doubts')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    data = packet(args.page_key, args.witness_root, args.scan_root, args.output, args.scratch)
    selected = args.sections.split(',')
    if set(selected) - {'images', 'C', 'H', 'inventory', 'doubts'}:
        ap.error('Unknown section name.')
    if args.json:
        print(json.dumps({'key': data['key'], **{name: data[name] for name in selected}}, ensure_ascii=False, indent=2))
        return
    for name in selected:
        print(f'\n=== {data["key"]}: {name} ===')
        obj = data[name]
        if name in {'C', 'H'}:
            print(json.dumps({k: v for k, v in obj.items() if k != 'text'}, ensure_ascii=False, indent=2))
            print(obj.get('text') if obj.get('text') is not None else '[No H text supplied.]')
        elif name == 'inventory':
            print(obj['path'])
            buf = io.StringIO(); wr = csv.DictWriter(buf, obj['headers']); wr.writeheader(); wr.writerows(obj['rows'])
            print(buf.getvalue(), end='')
        else:
            print(json.dumps(obj, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
