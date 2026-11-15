#!/usr/bin/env python3
"""Extract raw, explicitly braced doubt-macro arguments into separate JSON.

This module performs no file reading on import. The CLI reads page fragments
only when explicitly invoked. It never writes a transcription, doubts Markdown,
notation table, inventory, per-scan record, or progress log.

The lexer recognizes literal ASCII control words with ordinary TeX backslash,
brace, whitespace, and percent-comment syntax. It performs no macro expansion,
catcode changes, or interpretation of verbatim-like environments. The extracted
argument is a raw source slice, not an interpretation of its contents.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAGES = ROOT / 'pages'
DEFAULT_OUTPUT = ROOT / 'records' / 'doubts_extracted.json'
SCHEMA = 'diplomatic-doubts-raw-v1'
TARGETS = frozenset(('unsure', 'illegible'))


class Locations:
    """Exact locations in an unmodified, UTF-8-decoded source string."""

    def __init__(self, text: str):
        self.text = text
        self.line_starts = [0] + [match.end() for match in re.finditer(r'\r\n|\r|\n', text)]
        self.byte_offsets = [0]
        for char in text:
            self.byte_offsets.append(self.byte_offsets[-1] + len(char.encode('utf-8')))

    def point(self, offset: int) -> dict[str, int]:
        line_index = bisect_right(self.line_starts, offset) - 1
        return {
            'line': line_index + 1,
            'column': offset - self.line_starts[line_index] + 1,
            'character_offset': offset,
            'utf8_byte_offset': self.byte_offsets[offset],
        }

    def span(self, start: int, end: int) -> dict[str, dict[str, int]]:
        return {'start': self.point(start), 'end': self.point(end)}


def _ascii_letter(char: str) -> bool:
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'


def _control_token(text: str, start: int) -> tuple[str, int, bool]:
    """Return token name, exclusive end, and whether it is a control word."""
    assert text[start] == '\\'
    cursor = start + 1
    if cursor == len(text):
        return '', cursor, False
    if _ascii_letter(text[cursor]):
        end = cursor + 1
        while end < len(text) and _ascii_letter(text[end]):
            end += 1
        return text[cursor:end], end, True
    # A backslash plus a nonletter is one control symbol. This consumes escaped
    # braces, escaped percent, and a doubled backslash before later tokens.
    end = cursor + 1
    if text[cursor] == '\r' and end < len(text) and text[end] == '\n':
        end += 1
    return text[cursor:end], end, False


def _comment_end(text: str, start: int) -> int:
    cursor = start
    while cursor < len(text) and text[cursor] not in '\r\n':
        cursor += 1
    if cursor == len(text):
        return cursor
    if text[cursor] == '\r' and cursor + 1 < len(text) and text[cursor + 1] == '\n':
        return cursor + 2
    return cursor + 1


def _skip_space_and_comments(text: str, start: int) -> int:
    cursor = start
    while cursor < len(text):
        if text[cursor].isspace():
            cursor += 1
        elif text[cursor] == '%':
            cursor = _comment_end(text, cursor)
        else:
            break
    return cursor


def _group_end(text: str, opening: int) -> tuple[int | None, int]:
    """Find a structural closing brace, ignoring escaped/commented braces."""
    assert text[opening] == '{'
    depth, cursor = 1, opening + 1
    while cursor < len(text):
        char = text[cursor]
        if char == '\\':
            _, cursor, _ = _control_token(text, cursor)
        elif char == '%':
            cursor = _comment_end(text, cursor)
        elif char == '{':
            depth += 1
            cursor += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                return cursor, 0
            cursor += 1
        else:
            cursor += 1
    return None, depth


def scan_from_filename(path: str | Path) -> int | None:
    match = re.search(r'(?:^|_)scan(\d+)\.tex$', Path(path).name)
    return int(match.group(1)) if match else None


def extract_text(text: str, *, file: str, scan: int | None = None) -> dict[str, Any]:
    """Extract from a supplied string; this function performs no file access."""
    locations = Locations(text)
    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    cursor = 0
    while cursor < len(text):
        if text[cursor] == '%':
            cursor = _comment_end(text, cursor)
            continue
        if text[cursor] != '\\':
            cursor += 1
            continue
        start = cursor
        name, token_end, is_word = _control_token(text, cursor)
        cursor = token_end
        if not is_word or name not in TARGETS:
            continue

        argument_start = _skip_space_and_comments(text, token_end)
        occurrence_id = f'{file}#character-{start}'
        record: dict[str, Any] = {
            'occurrence_id': occurrence_id,
            'occurrence_in_file': len(records) + 1,
            'file': file,
            'scan': scan,
            'macro': name,
            'location': locations.point(start),
            'macro_token_span': locations.span(start, token_end),
            'between_name_and_argument': text[token_end:argument_start],
            'argument_opening_brace': None,
            'argument_closing_brace': None,
            'argument_content_span': None,
            'raw_argument': None,
        }
        error_code = None
        if argument_start == len(text) or text[argument_start] != '{':
            record['status'] = 'missing_braced_argument'
            record['occurrence_span'] = locations.span(start, token_end)
            record['expected_argument_at'] = locations.point(argument_start)
            record['next_character'] = text[argument_start:argument_start + 1] or None
            error_code = 'missing_braced_argument'
            message = f'Expected a braced argument after \\{name}.'
        else:
            record['argument_opening_brace'] = locations.point(argument_start)
            closing, remaining_depth = _group_end(text, argument_start)
            available_end = len(text) if closing is None else closing
            record['argument_content_span'] = locations.span(argument_start + 1, available_end)
            record['raw_argument'] = text[argument_start + 1:available_end]
            if closing is None:
                record['status'] = 'unclosed_argument'
                record['occurrence_span'] = locations.span(start, len(text))
                record['unclosed_group_depth'] = remaining_depth
                error_code = 'unclosed_argument'
                message = f'Argument of \\{name} reaches end of file with {remaining_depth} group(s) unclosed.'
            else:
                record['status'] = 'complete'
                record['argument_closing_brace'] = locations.point(closing)
                record['occurrence_span'] = locations.span(start, closing + 1)
        records.append(record)
        if error_code:
            errors.append({
                'code': error_code,
                'occurrence_id': occurrence_id,
                'file': file,
                'scan': scan,
                'macro': name,
                'location': locations.point(start),
                'message': message,
            })
        # Deliberately continue at the end of the control word, not at the end
        # of its argument. Nested target macros are therefore visited in their
        # own lexical order, including inside a malformed outer argument.

    return {'records': records, 'errors': errors}


def extract_files(paths: list[Path]) -> dict[str, Any]:
    """Read the explicitly supplied files as bytes; preserve every newline."""
    sources: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    for supplied in paths:
        path = supplied.resolve()
        file = str(path)
        scan = scan_from_filename(path)
        source: dict[str, Any] = {'file': file, 'scan': scan}
        if path.suffix.lower() != '.tex':
            source['status'] = 'source_error'
            error = {'code': 'unsupported_source_extension', 'file': file, 'scan': scan,
                     'message': 'Input fragments must have the .tex extension.'}
            source['error'] = error
            errors.append(error)
            sources.append(source)
            continue
        try:
            source_bytes = path.read_bytes()
            text = source_bytes.decode('utf-8')
        except (OSError, UnicodeDecodeError) as exc:
            source['status'] = 'source_error'
            error = {'code': 'source_read_error', 'file': file, 'scan': scan,
                     'message': f'{type(exc).__name__}: {exc}'}
            source['error'] = error
            errors.append(error)
            sources.append(source)
            continue
        extracted = extract_text(text, file=file, scan=scan)
        source.update({
            'status': 'complete' if not extracted['errors'] else 'contains_malformed_arguments',
            'sha256': hashlib.sha256(source_bytes).hexdigest(),
            'utf8_bytes': len(source_bytes),
            'unicode_code_points': len(text),
            'occurrences': len(extracted['records']),
            'malformed_arguments': len(extracted['errors']),
        })
        sources.append(source)
        records.extend(extracted['records'])
        errors.extend(extracted['errors'])

    if not paths:
        errors.append({'code': 'no_input_files', 'message': 'No input page fragments were selected.'})
    return {
        'schema': SCHEMA,
        'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope': 'Raw lexical extraction only; no readings, confidence, or alternatives assigned.',
        'location_conventions': {
            'lines': '1-based; LF, CRLF, and bare CR each start one new line; every raw newline character remains unchanged.',
            'columns': '1-based Unicode code-point counts from the start of each line.',
            'character_offsets': '0-based Unicode code-point offsets; all span ends are exclusive.',
            'utf8_byte_offsets': '0-based offsets into the original UTF-8 bytes; all span ends are exclusive.',
            'raw_argument': 'Exact source slice between structural braces; an unclosed argument retains its available slice through EOF.',
            'scan': 'Integer derived solely from a scanNNN.tex filename suffix; null when the filename has no such suffix.',
        },
        'sources': sources,
        'records': records,
        'errors': errors,
        'summary': {
            'input_files': len(paths),
            'occurrences': len(records),
            'complete_occurrences': sum(record['status'] == 'complete' for record in records),
            'malformed_occurrences': sum(record['status'] != 'complete' for record in records),
            'errors': len(errors),
        },
    }


def validate_output(path: Path, inputs: list[Path]) -> None:
    resolved = path.resolve()
    if resolved.suffix.lower() != '.json':
        raise ValueError('The output must be a separate .json file; Markdown and other live deliverable formats are refused.')
    if resolved in {source.resolve() for source in inputs}:
        raise ValueError('The output path is also an input source path.')
    if re.fullmatch(r'scan\d+_inventory\.json', resolved.name):
        raise ValueError('A per-scan inventory record cannot be used as extractor output.')
    if resolved.exists():
        try:
            previous = json.loads(resolved.read_bytes().decode('utf-8'))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError('An existing output file could not be identified as an earlier extraction.') from exc
        if not isinstance(previous, dict) or previous.get('schema') != SCHEMA:
            raise ValueError('The existing output belongs to another artifact; it will not be overwritten.')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='*', type=Path, help='Explicit page .tex files; omitted selects the page directory.')
    parser.add_argument('--pages-dir', type=Path, default=DEFAULT_PAGES)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    paths = args.files or sorted(args.pages_dir.glob('*.tex'))
    try:
        validate_output(args.output, paths)
    except ValueError as exc:
        parser.error(str(exc))
    result = extract_files(paths)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    summary = result['summary']
    print(f"Wrote {summary['occurrences']} raw occurrences to {args.output}.")
    for error in result['errors']:
        location = error.get('location')
        where = error.get('file', '<input selection>')
        if location:
            where += f":{location['line']}:{location['column']}"
        print(f"ERROR {where}: {error['message']}", file=sys.stderr)
    if result['errors']:
        print('Extraction contains errors; all available records were written for review.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
