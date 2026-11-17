#!/usr/bin/env python3
"""Read-only structural inspection of tikz-cd row/column arrow destinations.

No handwriting or mathematical interpretation is attempted. An omitted or
empty target is reported for visual review; explicit {} nodes are permitted.
Ragged matrix rows are legal and are not errors by themselves.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Cell:
    text: str
    offset: int


def comments_to_spaces(text: str) -> str:
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == '\\':
            i += 2
        elif text[i] == '%':
            end = text.find('\n', i)
            if end < 0:
                end = len(text)
            chars[i:end] = ' ' * (end - i)
            i = end
        else:
            i += 1
    return ''.join(chars)


def group_end(text: str, start: int, opening: str, closing: str) -> int:
    depth = 1
    braces = 0
    i = start + 1
    while i < len(text):
        char = text[i]
        if char == '\\':
            i += 2
            continue
        if opening != '{':
            if char == '{':
                braces += 1
            elif char == '}':
                braces -= 1
        if braces == 0:
            if char == opening:
                depth += 1
            elif char == closing:
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError(f'unclosed {opening}{closing} group at offset {start}')


def skip_space(text: str, start: int) -> int:
    while start < len(text) and text[start].isspace():
        start += 1
    return start


def cells(body: str, offset: int) -> list[list[Cell]]:
    """Split only top-level matrix separators, respecting nested environments."""
    i = skip_space(body, 0)
    if i < len(body) and body[i] == '[':
        i = group_end(body, i, '[', ']')
    start = i
    rows: list[list[Cell]] = []
    row: list[Cell] = []
    brace_depth = 0
    environments: list[str] = []
    while i < len(body):
        char = body[i]
        if char == '\\':
            if body.startswith('\\\\', i):
                if brace_depth == 0 and not environments:
                    row.append(Cell(body[start:i], offset + start))
                    rows.append(row)
                    row = []
                    i = skip_space(body, i + 2)
                    if i < len(body) and body[i] == '*':
                        i = skip_space(body, i + 1)
                    if i < len(body) and body[i] == '[':
                        i = group_end(body, i, '[', ']')
                    start = i
                else:
                    i += 2
                continue
            command = re.match(r'\\([A-Za-z@]+)', body[i:])
            if not command:
                i += 2
                continue
            name = command.group(1)
            end = i + len(command.group(0))
            argument = skip_space(body, end)
            if name in ('begin', 'end') and argument < len(body) and body[argument] == '{':
                arg_end = group_end(body, argument, '{', '}')
                environment = body[argument + 1:arg_end - 1]
                if name == 'begin':
                    environments.append(environment)
                elif not environments or environments.pop() != environment:
                    raise ValueError(f'unbalanced nested environment {environment}')
                i = arg_end
                continue
            if name in ('arrow', 'ar') and argument < len(body) and body[argument] == '[':
                i = group_end(body, argument, '[', ']')
                continue
            i = end
            continue
        if char == '{':
            brace_depth += 1
        elif char == '}':
            brace_depth -= 1
            if brace_depth < 0:
                raise ValueError('unmatched closing brace in matrix')
        elif char == '&' and brace_depth == 0 and not environments:
            row.append(Cell(body[start:i], offset + start))
            start = i + 1
        i += 1
    if brace_depth or environments:
        raise ValueError('unclosed brace or nested environment in matrix')
    row.append(Cell(body[start:], offset + start))
    if any(cell.text.strip() for cell in row) or not rows:
        rows.append(row)
    return rows


def arrows(cell: Cell):
    text = cell.text
    cursor = 0
    pattern = re.compile(r'\\(?:arrow|ar)\b')
    while match := pattern.search(text, cursor):
        opening = skip_space(text, match.end())
        if opening >= len(text) or text[opening] != '[':
            yield match.start(), match.end(), None, ''
            cursor = match.end()
            continue
        end = group_end(text, opening, '[', ']')
        options = text[opening + 1:end - 1]
        direction = options.split(',', 1)[0].strip()
        yield match.start(), end, direction, options
        cursor = end


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    total_diagrams = total_arrows = findings = explicit_empty_targets = 0
    diagrams = re.compile(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}', re.S)
    for path in sorted((args.root / 'pages').glob('*.tex')):
        source = path.read_text(encoding='utf-8')
        clean = comments_to_spaces(source)
        for number, match in enumerate(diagrams.finditer(clean), 1):
            total_diagrams += 1
            diagram_line = source.count('\n', 0, match.start()) + 1
            label = f'{path.name}: diagram {number} (line {diagram_line})'
            try:
                grid = cells(match.group(1), match.start(1))
            except ValueError as exc:
                print(f'REVIEW {label}: {exc}')
                findings += 1
                continue
            for row_index, row in enumerate(grid):
                for col_index, cell in enumerate(row):
                    try:
                        cell_arrows = list(arrows(cell))
                    except ValueError as exc:
                        print(f'REVIEW {label}, r{row_index+1}c{col_index+1}: {exc}')
                        findings += 1
                        continue
                    for start, end, direction, options in cell_arrows:
                        total_arrows += 1
                        line = source.count('\n', 0, cell.offset + start) + 1
                        arrow_label = f'{path.name}:{line}: diagram {number}, r{row_index+1}c{col_index+1}, arrow[{direction}]'
                        if not direction or not re.fullmatch('[udlr]+', direction):
                            print(f'REVIEW {arrow_label}: no recognized relative direction; inspect options {options!r}.')
                            findings += 1
                            continue
                        if ('u' in direction and 'd' in direction) or ('l' in direction and 'r' in direction):
                            print(f'REVIEW {arrow_label}: conflicting direction letters.')
                            findings += 1
                        target_row = row_index + direction.count('d') - direction.count('u')
                        target_col = col_index + direction.count('r') - direction.count('l')
                        target_label = f'r{target_row+1}c{target_col+1}'
                        if target_row < 0 or target_row >= len(grid) or target_col < 0 or target_col >= len(grid[target_row]):
                            print(f'REVIEW {arrow_label}: target {target_label} is outside its row; row widths {[len(r) for r in grid]}.')
                            findings += 1
                            continue
                        target = grid[target_row][target_col]
                        target_text = target.text
                        for a, b, _, _ in reversed(list(arrows(target))):
                            target_text = target_text[:a] + target_text[b:]
                        if not target_text.strip():
                            print(f'REVIEW {arrow_label}: target {target_label} is blank (no object or explicit {{}} node).')
                            findings += 1
                        elif target_text.strip() == '{}':
                            explicit_empty_targets += 1
    print(f'Inspected {total_diagrams} diagrams and {total_arrows} arrows; {findings} coordinate findings; {explicit_empty_targets} permitted explicit-empty targets.')
    print('No page fragments modified. Source coordinates do not establish fidelity to the scans.')
    return 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
