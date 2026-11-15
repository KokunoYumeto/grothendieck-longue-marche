#!/usr/bin/env python3
"""Index doubt macros without interpreting or modifying manuscript readings.

The parser skips TeX comments and escaped control symbols, balances ordinary
brace groups, and extracts every nested \\unsure{...} / \\illegible{...}.
Raw contents are exact source slices, including any internal whitespace.
Containing macros are the nearest enclosing brace arguments whose owner is
unambiguous from a directly preceding control word. Optional arguments and
second/subsequent required arguments are not assigned speculative owners.
"""
from __future__ import annotations

import argparse
import bisect
import json
import re
from pathlib import Path


TARGETS = {'unsure', 'illegible'}


def extract(source: str, *, filename: str, scan: int) -> list[dict]:
    line_starts = [0] + [m.end() for m in re.finditer('\n', source)]

    def line_number(offset: int) -> int:
        return bisect.bisect_right(line_starts, offset)

    stack = []
    pending_command = None
    records = []
    errors = []
    i = 0
    while i < len(source):
        character = source[i]
        if character == '%':
            end = source.find('\n', i)
            i = len(source) if end < 0 else end
            continue
        if character == '\\':
            command_start = i
            i += 1
            if i == len(source):
                pending_command = None
                break
            if source[i].isascii() and (source[i].isalpha() or source[i] == '@'):
                start = i
                while i < len(source) and source[i].isascii() and (
                    source[i].isalpha() or source[i] == '@'
                ):
                    i += 1
                name = source[start:i]
                if name == 'verb':
                    # A literal \\verb body must not produce false occurrences.
                    if i < len(source) and source[i] == '*':
                        i += 1
                    if i < len(source):
                        delimiter = source[i]
                        end = source.find(delimiter, i + 1)
                        if end < 0:
                            errors.append(f'unclosed verb delimiter at line {line_number(i)}')
                            i = len(source)
                        else:
                            i = end + 1
                    pending_command = None
                else:
                    pending_command = (name, command_start)
                continue
            # Escaped braces, percent signs, and \\\\ have no grouping role.
            i += 1
            pending_command = None
            continue
        if character.isspace():
            i += 1
            continue
        if character == '{':
            owner = pending_command
            ancestors = [group['owner'][0] for group in stack if group['owner']]
            stack.append({'opening': i, 'owner': owner, 'ancestors': ancestors})
            pending_command = None
            i += 1
            continue
        if character == '}':
            if not stack:
                errors.append(f'unmatched closing brace at line {line_number(i)}')
            else:
                group = stack.pop()
                owner = group['owner']
                if owner and owner[0] in TARGETS:
                    name, command_start = owner
                    ancestors = group['ancestors']
                    records.append({
                        'file': filename,
                        'scan': scan,
                        'source_line': line_number(command_start),
                        'source_end_line': line_number(i),
                        'macro': '\\' + name,
                        'raw_contents': source[group['opening'] + 1:i],
                        'containing_macro': '\\' + ancestors[-1] if ancestors else None,
                        'enclosing_macros': ['\\' + name for name in ancestors],
                        'source_offset': command_start,
                        'argument_start_offset': group['opening'] + 1,
                        'argument_end_offset': i,
                    })
            pending_command = None
            i += 1
            continue
        pending_command = None
        i += 1
    errors.extend(f'unclosed brace at line {line_number(group["opening"])}' for group in stack)
    if errors:
        raise ValueError(filename + ': ' + '; '.join(errors))
    records.sort(key=lambda item: item['source_offset'])
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    occurrences = []
    pages = sorted((root / 'pages').glob('MPL_136_095-141_136_scan*.tex'))
    for path in pages:
        match = re.fullmatch(r'MPL_136_095-141_136_scan(\d+)\.tex', path.name)
        if not match:
            continue
        source = path.read_text(encoding='utf-8')
        occurrences.extend(extract(source, filename=path.relative_to(root).as_posix(),
                                   scan=int(match.group(1))))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(occurrences, ensure_ascii=False, indent=2) + '\n',
                           encoding='utf-8')
    counts = {name: sum(item['macro'] == '\\' + name for item in occurrences)
              for name in sorted(TARGETS)}
    print(json.dumps({'pages_parsed': len(pages), 'occurrences': len(occurrences),
                      'counts': counts, 'output': str(args.output.resolve())}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
