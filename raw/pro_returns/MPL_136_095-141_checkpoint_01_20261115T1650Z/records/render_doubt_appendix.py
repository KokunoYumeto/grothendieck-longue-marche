#!/usr/bin/env python3
"""Render a mechanical doubt index as Markdown, without editorial judgment."""
import argparse
import json
import re
from pathlib import Path


def main():
    base = Path(__file__).resolve().parent.parent.parent / 'technical_checks'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=base / 'doubt_occurrences.json')
    parser.add_argument('--output', type=Path, default=base / 'doubt_occurrences_appendix.md')
    args = parser.parse_args()
    records = json.loads(args.input.read_text(encoding='utf-8'))
    output = [
        '# Mechanical appendix: every doubt-marker occurrence\n',
        'This appendix reproduces the raw arguments of the indexed `\\unsure` and '
        '`\\illegible` macros. Source lines refer to the page LaTeX files, not to '
        'manuscript lines. Nested occurrences appear separately. No reading, '
        'alternative, confidence, or legibility judgment is added here.\n',
        f'Occurrences indexed: **{len(records)}**.\n',
    ]
    for index, item in enumerate(records, 1):
        output.append(f'## {index:04d} — Scan {item["scan"]:03d}, source line {item["source_line"]}\n')
        output.append(f'File: `{item["file"]}`. Macro: `{item["macro"]}`.\n')
        if item.get('containing_macro'):
            output.append(f'Nearest identifiable enclosing macro: `{item["containing_macro"]}`.\n')
        body = item['raw_contents']
        fence = '`' * max(3, 1 + max((len(m.group()) for m in re.finditer(r'`+', body)), default=0))
        output.append(fence + 'tex\n' + body + ('' if body.endswith('\n') else '\n') + fence + '\n')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(output), encoding='utf-8')
    print(json.dumps({'occurrences': len(records), 'output': str(args.output.resolve())}))


if __name__ == '__main__':
    main()
