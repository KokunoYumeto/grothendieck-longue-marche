#!/usr/bin/env python3
"""Extract exact H page-marker spans; never decide manuscript readings.

Only explicit \\page{N} markers define the raw spans.  Material between a
page's body and the following marker (section headings, editorial notes) may
refer forward.  Such spans are flagged rather than assigned by inference.
The first 12 source lines before each marker are also made available as
*boundary context*, not as part of the page.  Source bytes are not modified.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

PAGE = re.compile(rb'^\\page\{([0-9]+)\}[^\S\r\n]*(?:%[^\r\n]*)?\r?\n?$')
END = re.compile(rb'^\\end\{document\}')
SECTION = re.compile(rb'^\\(?:sub)*section\*?\{')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split(source: Path, dest: Path) -> dict:
    source = source.resolve()
    dest = dest.resolve()
    if source == dest or source in dest.parents:
        raise ValueError('Destination must not be inside the witness source tree.')
    rows = list(csv.DictReader((source / 'page_map.tsv').open(encoding='utf-8'), delimiter='\t'))
    dest.mkdir(parents=True, exist_ok=True)
    parsed = {}
    for name in dict.fromkeys(r['hua_file'] for r in rows):
        raw = (source / name).read_bytes()
        lines = raw.splitlines(keepends=True)
        markers = []
        for i, line in enumerate(lines):
            m = PAGE.match(line)
            if m:
                markers.append((int(m.group(1)), i))
        if len({p for p, _ in markers}) != len(markers):
            raise ValueError(f'Duplicate page marker in {name}')
        page_spans = {}
        for j, (page, start) in enumerate(markers):
            stop = markers[j + 1][1] if j + 1 < len(markers) else len(lines)
            stop = next((i for i in range(start, stop) if END.match(lines[i])), stop)
            page_spans[page] = (start, stop)
        parsed[name] = (raw, lines, page_spans)

    manifest = []
    for r in rows:
        key = f"{r['folder']}_{r['cote']}_scan{int(r['our_scan']):03d}"
        raw, lines, spans = parsed[r['hua_file']]
        m = dict(r)
        m.update(key=key, source_sha256=digest(raw), fragment='', fragment_sha256='',
                 source_start_line='', source_end_line='', boundary_context='',
                 section_lines='', warning='')
        page = int(r['their_page'])
        if r['hua_has'] == 'text':
            if page not in spans:
                raise ValueError(f"H text promised but page marker absent: {key} (H {page})")
            start, stop = spans[page]
            fragment = b''.join(lines[start:stop])
            target = dest / f'{key}.tex'
            target.write_bytes(fragment)
            numbered = ''.join(f'{i+1:5d}\t{line.decode("utf-8")}' for i, line in enumerate(lines[start:stop], start))
            (dest / f'{key}.lines.txt').write_text(numbered, encoding='utf-8')
            context_start = max(0, start - 12)
            context = b''.join(lines[context_start:start])
            context_target = dest / f'{key}.before.tex'
            context_target.write_bytes(context)
            sections = [i + 1 for i in range(start, stop) if SECTION.match(lines[i])]
            warning = ('Contains section commands; inspect boundary material, which may introduce the next page.'
                       if sections else '')
            m.update(fragment=target.name, fragment_sha256=digest(fragment),
                     source_start_line=start + 1, source_end_line=stop,
                     boundary_context=context_target.name, section_lines=','.join(map(str, sections)), warning=warning)
            meta = {**m, 'boundary_context_source_start_line': context_start + 1,
                    'boundary_context_source_end_line': start,
                    'extraction_rule': 'Exact bytes from explicit page marker to immediately before next page marker or end-document; editorial boundary material is not attributed by this script.'}
            (dest / f'{key}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        else:
            m['warning'] = 'No H text according to page_map; no text fragment generated and no collation rows should be fabricated.'
        manifest.append(m)
    fields = list(manifest[0])
    with (dest / 'INDEX.tsv').open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fields, delimiter='\t')
        wr.writeheader()
        wr.writerows(manifest)
    report = {'pages': len(rows), 'hua_has': dict(Counter(r['hua_has'] for r in rows)),
              'fragments': sum(bool(r['fragment']) for r in manifest),
              'destination': str(dest), 'index': str(dest / 'INDEX.tsv'),
              'warning': 'Mechanical extraction only. No image inspection, reading decision, or verification is performed.'}
    (dest / 'EXTRACTION_REPORT.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--witness-root', required=True, type=Path)
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    print(json.dumps(split(args.witness_root, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
