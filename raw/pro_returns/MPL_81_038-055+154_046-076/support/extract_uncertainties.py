#!/usr/bin/env python3
"""Extract diplomatic doubt macros without interpreting or changing readings.

JSON is written to stdout. Page files are read only. The parser follows literal
TeX grouping and escapes, skips comments and verbatim material, and visits nested
macros. It does not expand TeX commands or assign confidence.
"""
from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from pathlib import Path

DEFAULT_PAGES = Path('/workspace/scratch/89f8415d3ab0/deliver/pages')
FILE_RE = re.compile(r'_(?P<cote>\d+)_scan(?P<scan>\d+)\.tex$')
ELEMENT_RE = re.compile(r'%\s*E:\s*([^|]+)\|([^|]+)\|(.*)$')
CONTROL_LETTERS = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@')
VERBATIM_ENVIRONMENTS = {'verbatim', 'verbatim*', 'Verbatim', 'BVerbatim', 'LVerbatim'}


def control_end(source: str, position: int) -> int:
    """Return the end of a control word or a single escaped control symbol."""
    j = position + 1
    if j == len(source):
        return j
    if source[j] not in CONTROL_LETTERS:
        return j + 1
    while j < len(source) and source[j] in CONTROL_LETTERS:
        j += 1
    return j


def skip_space_comments(source: str, position: int) -> int:
    while position < len(source):
        if source[position].isspace():
            position += 1
        elif source[position] == '%':
            end = source.find('\n', position)
            position = len(source) if end == -1 else end + 1
        else:
            break
    return position


def skip_verb(source: str, word_end: int) -> int:
    """Skip the literal argument of a known \\verb or \\verb* command."""
    start = word_end + (word_end < len(source) and source[word_end] == '*')
    if start >= len(source) or source[start] in '\r\n':
        return start
    delimiter = source[start]
    end = source.find(delimiter, start + 1)
    newline = source.find('\n', start + 1)
    if end == -1 or (newline != -1 and newline < end):
        return len(source) if newline == -1 else newline
    return end + 1


def skip_verbatim_environment(source: str, word_end: int) -> int | None:
    opening = skip_space_comments(source, word_end)
    if opening >= len(source) or source[opening] != '{':
        return None
    closing = source.find('}', opening + 1)
    if closing == -1:
        return None
    name = source[opening + 1:closing]
    if name not in VERBATIM_ENVIRONMENTS:
        return None
    end_token = '\\end{' + name + '}'
    end = source.find(end_token, closing + 1)
    return len(source) if end == -1 else end + len(end_token)


def group_end(source: str, opening: int) -> tuple[int, bool]:
    """Return the closing-brace index, or EOF and False for an unclosed group."""
    assert source[opening] == '{'
    depth = 1
    i = opening + 1
    while i < len(source):
        char = source[i]
        if char == '%':
            end = source.find('\n', i)
            i = len(source) if end == -1 else end + 1
            continue
        if char == '\\':
            end = control_end(source, i)
            word = source[i + 1:end]
            if word == 'verb':
                i = skip_verb(source, end)
                continue
            if word == 'begin':
                skipped = skip_verbatim_environment(source, end)
                if skipped is not None:
                    i = skipped
                    continue
            i = end
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                return i, True
        i += 1
    return len(source), False


def split_top_level_pipes(argument: str) -> list[str]:
    """Split only unescaped | outside nested braces, comments, and verbatim.

No whitespace is stripped. Literal top-level pipes are delimiters by the user's
macro convention; this function does not infer mathematical meaning for them.
"""
    segments = []
    start = depth = i = 0
    while i < len(argument):
        char = argument[i]
        if char == '%':
            end = argument.find('\n', i)
            i = len(argument) if end == -1 else end + 1
            continue
        if char == '\\':
            end = control_end(argument, i)
            word = argument[i + 1:end]
            if word == 'verb':
                i = skip_verb(argument, end)
                continue
            if word == 'begin':
                skipped = skip_verbatim_environment(argument, end)
                if skipped is not None:
                    i = skipped
                    continue
            i = end
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
        elif char == '|' and depth == 0:
            segments.append(argument[start:i])
            start = i + 1
        i += 1
    segments.append(argument[start:])
    return segments


def extract_source(source: str, *, cote: str, scan: int, source_file: str,
                   ordinal_start: int = 1) -> tuple[list[dict], list[dict]]:
    """Extract one in-memory source, permitting verification on synthetic text."""
    newlines = [-1] + [m.start() for m in re.finditer('\n', source)]

    def location(position: int) -> tuple[int, int]:
        line = bisect.bisect_left(newlines, position)
        return line, position - newlines[line - 1]

    records: list[dict] = []
    errors: list[dict] = []
    current_element = None
    i = 0
    while i < len(source):
        char = source[i]
        if char == '%':
            end = source.find('\n', i)
            if end == -1:
                end = len(source)
            line, column = location(i)
            prefix = source[newlines[line - 1] + 1:i]
            marker = ELEMENT_RE.fullmatch(source[i:end].rstrip('\r')) if not prefix.strip() else None
            if marker:
                current_element = {
                    'source_line': line,
                    'kind': marker[1].strip(),
                    'position': marker[2].strip(),
                    'first_words_or_objects': marker[3],
                    'raw_marker': source[i:end],
                }
            i = end
            continue
        if char != '\\':
            i += 1
            continue
        end = control_end(source, i)
        word = source[i + 1:end]
        if word == 'verb':
            i = skip_verb(source, end)
            continue
        if word == 'begin':
            skipped = skip_verbatim_environment(source, end)
            if skipped is not None:
                i = skipped
                continue
        if word in {'unsure', 'illegible'}:
            line, column = location(i)
            opening = skip_space_comments(source, end)
            if opening == len(source) or source[opening] != '{':
                errors.append({'source_file': source_file, 'source_line': line,
                               'source_column': column, 'macro': word,
                               'error': 'macro has no literal braced argument'})
            else:
                closing, closed = group_end(source, opening)
                raw = source[opening + 1:closing]
                segments = split_top_level_pipes(raw)
                records.append({
                    'cote': cote,
                    'scan': scan,
                    'source_file': source_file,
                    'source_line': line,
                    'source_column': column,
                    'ordinal': ordinal_start + len(records),
                    'page_ordinal': len(records) + 1,
                    'macro': word,
                    'element': current_element,
                    'raw_argument': raw,
                    'reading': segments[0],
                    'alternatives': segments[1:],
                    'closed': closed,
                })
                if not closed:
                    errors.append({'source_file': source_file, 'source_line': line,
                                   'source_column': column, 'macro': word,
                                   'error': 'unclosed argument; raw_argument extends to EOF'})
        # Do not skip a parsed argument: nested uncertainty macros must be visited.
        i = end
    return records, errors


def extract_directory(pages_dir: Path) -> dict:
    records: list[dict] = []
    errors: list[dict] = []
    file_list = []
    paths = list(pages_dir.glob('*.tex'))
    if not paths:
        errors.append({'error': 'no .tex page files found', 'directory': str(pages_dir)})
    parsed_paths = []
    for path in paths:
        match = FILE_RE.search(path.name)
        if not match:
            errors.append({'source_file': path.name, 'error': 'filename has no cote/scan suffix'})
            continue
        parsed_paths.append((int(match['cote']), int(match['scan']), path))
    for cote_number, scan, path in sorted(parsed_paths):
        source_file = 'pages/' + path.name
        try:
            source = path.read_bytes().decode('utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append({'source_file': source_file, 'error': str(exc)})
            continue
        found, failures = extract_source(source, cote=str(cote_number), scan=scan,
                                         source_file=source_file,
                                         ordinal_start=len(records) + 1)
        records.extend(found)
        errors.extend(failures)
        file_list.append({'cote': str(cote_number), 'scan': scan,
                          'source_file': source_file, 'occurrences': len(found)})
    return {
        'schema_version': 1,
        'scope': 'Literal uncertainty macros; no reading judgment, confidence assignment, or TeX expansion.',
        'source_directory': str(pages_dir.resolve()),
        'source_files': file_list,
        'occurrence_count': len(records),
        'occurrences': records,
        'errors': errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages_dir', nargs='?', type=Path, default=DEFAULT_PAGES)
    parser.add_argument('--compact', action='store_true', help='emit compact JSON')
    args = parser.parse_args()
    result = extract_directory(args.pages_dir)
    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
