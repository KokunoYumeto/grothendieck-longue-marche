#!/usr/bin/env python3
"""Format a literal uncertainty extraction for root review; assign no judgments."""
import argparse
import json
from collections import defaultdict
from pathlib import Path


def format_review(source: Path, output: Path) -> dict:
    data = json.loads(source.read_text())
    grouped = defaultdict(list)
    for item in data['occurrences']:
        grouped[(item['cote'], item['scan'], item['source_file'])].append(item)
    lines = ['LITERAL UNCERTAINTY REVIEW',
             'Source: ' + source.name,
             'Quoted strings use JSON escaping; readings and alternatives are unchanged.',
             'No confidence or interpretation is assigned.', '']
    for page in data['source_files']:
        key = (page['cote'], page['scan'], page['source_file'])
        items = grouped[key]
        lines.extend([f"COTE {page['cote']} | SCAN {page['scan']:03d} | {len(items)} occurrences",
                      'TeX file: ' + page['source_file']])
        for item in items:
            element = item.get('element')
            position = element['position'] if element else None
            lines.append(f"{item['page_ordinal']:03d} | {item['macro']} | TeXline {item['source_line']} | position "
                         + json.dumps(position, ensure_ascii=False))
            lines.append('  reading: ' + json.dumps(item['reading'], ensure_ascii=False))
            lines.append('  alternatives: ' + json.dumps(item['alternatives'], ensure_ascii=False))
        lines.append('')
    if data.get('errors'):
        lines.extend(['PARSER ERRORS', json.dumps(data['errors'], ensure_ascii=False, indent=2), ''])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(lines), encoding='utf-8')
    return {'output': str(output.resolve()), 'source_files': len(data['source_files']),
            'occurrences': len(data['occurrences']), 'parser_errors': len(data.get('errors', []))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_json', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(format_review(args.source_json, args.output), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
