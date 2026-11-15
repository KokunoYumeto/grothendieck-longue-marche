#!/usr/bin/env python3
"""Propose table-environment repairs inside diagram macros, without page edits.

Each tabular within a diagram becomes a math-mode array. Original cell text,
spacing commands, column specifications, and row separators are retained.
Text-mode wrappers preserve the original text interpretation of every cell;
arraycolsep is set to the existing tabcolsep. A reverse transformation must
recover each original table exactly before a proposal can be written.

The live pages are read only. The review patch and manifest go to records;
proposed full-page copies go to the sibling scratch texqa-cache folder.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
MIRROR = ROOT.parent / 'texqa-cache' / 'banner-proposal'
PREFIX = r'\begingroup\setlength{\arraycolsep}{\tabcolsep}$'
SUFFIX = r'$\endgroup'


def group_end(text, start):
    if text[start] != '{':
        raise ValueError('Expected a braced group')
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('Unclosed braced group')


def skip_space(text, start):
    while start < len(text) and text[start].isspace():
        start += 1
    return start


def cell_segments(body):
    """Yield (cell, following separator), preserving all original characters."""
    depth, i, start = 0, 0, 0
    while i < len(body):
        c = body[i]
        if c == '\\':
            if i + 1 < len(body) and body[i + 1] == '\\' and depth == 0:
                end = i + 2
                # Preserve an optional row-height argument as part of the row
                # separator; none of the currently proposed tables has one.
                next_token = skip_space(body, end)
                if next_token < len(body) and body[next_token] == '[':
                    close = body.find(']', next_token + 1)
                    if close < 0:
                        raise ValueError('Unclosed row-height argument')
                    end = close + 1
                yield body[start:i], body[i:end]
                start = i = end
            else:
                i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == '&' and depth == 0:
            yield body[start:i], '&'
            start = i + 1
        i += 1
    yield body[start:], ''


def text_wrap(content, reverse=False):
    if reverse:
        if not content.startswith(r'\text{'):
            raise ValueError('Missing generated text wrapper')
        end = group_end(content, len(r'\text'))
        if end != len(content) - 1:
            raise ValueError('Unexpected content after generated text wrapper')
        return content[len(r'\text{'):-1]
    return r'\text{' + content + '}'


def transform_cell(cell, reverse=False):
    leading = len(cell) - len(cell.lstrip())
    trailing = len(cell) - len(cell.rstrip())
    if leading == len(cell):
        return cell
    end = len(cell) - trailing if trailing else len(cell)
    left, core, right = cell[:leading], cell[leading:end], cell[end:]
    if core.startswith(r'\multicolumn'):
        pos = len(r'\multicolumn')
        groups = []
        for _ in range(3):
            pos = skip_space(core, pos)
            close = group_end(core, pos)
            groups.append((pos, close))
            pos = close + 1
        if core[pos:].strip():
            raise ValueError('Unexpected tokens after a multicolumn cell')
        a, b = groups[2]
        core = core[:a+1] + text_wrap(core[a+1:b], reverse) + core[b:]
    else:
        core = text_wrap(core, reverse)
    return left + core + right


def transform_body(body, reverse=False):
    return ''.join(transform_cell(cell, reverse) + separator
                   for cell, separator in cell_segments(body))


def table_parts(table, environment):
    opening = r'\begin{' + environment + '}'
    closing = r'\end{' + environment + '}'
    if not table.startswith(opening) or not table.endswith(closing):
        raise ValueError('Unexpected table delimiters')
    pos = skip_space(table, len(opening))
    if table[pos] == '[':
        pos = skip_space(table, table.index(']', pos + 1) + 1)
    spec_end = group_end(table, pos)
    return table[len(opening):spec_end+1], table[spec_end+1:-len(closing)]


def to_array(table):
    spec, body = table_parts(table, 'tabular')
    return PREFIX + r'\begin{array}' + spec + transform_body(body) + r'\end{array}' + SUFFIX


def to_original(table):
    if not table.startswith(PREFIX) or not table.endswith(SUFFIX):
        raise ValueError('Unexpected generated wrapper')
    array = table[len(PREFIX):-len(SUFFIX)]
    spec, body = table_parts(array, 'array')
    return r'\begin{tabular}' + spec + transform_body(body, reverse=True) + r'\end{tabular}'


def diagram_ranges(text):
    return [(m.end(), group_end(text, m.end() - 1))
            for m in re.finditer(r'\\diagram\s*\{', text)]


def main():
    MIRROR.mkdir(parents=True, exist_ok=True)
    manifest, patch = [], []
    for path in sorted((ROOT / 'pages').glob('*.tex')):
        original_bytes = path.read_bytes()
        original = original_bytes.decode('utf-8')
        ranges = diagram_ranges(original)
        tables = []
        for match in re.finditer(r'\\begin\{tabular\}', original):
            if not any(a <= match.start() < b for a, b in ranges):
                continue
            closing = original.index(r'\end{tabular}', match.end()) + len(r'\end{tabular}')
            table = original[match.start():closing]
            if table.count(r'\begin{tabular}') != 1:
                raise ValueError('Nested tabular requires separate review')
            proposed = to_array(table)
            if to_original(proposed) != table:
                raise AssertionError('Original table did not round-trip exactly')
            tables.append((match.start(), closing, proposed,
                           {'line': original.count('\n', 0, match.start()) + 1,
                            'original_table_sha256': hashlib.sha256(table.encode('utf-8')).hexdigest(),
                            'proposed_table_sha256': hashlib.sha256(proposed.encode('utf-8')).hexdigest(),
                            'exact_inverse_verified': True}))
        updated = original
        for start, end, proposed, _ in reversed(tables):
            updated = updated[:start] + proposed + updated[end:]
        (MIRROR / path.name).write_text(updated)
        if tables:
            label = 'pages/' + path.name
            manifest.append({'file': label, 'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
                             'proposed_sha256': hashlib.sha256(updated.encode('utf-8')).hexdigest(),
                             'tables': [entry[3] for entry in tables]})
            patch.extend(difflib.unified_diff(original.splitlines(keepends=True),
                                            updated.splitlines(keepends=True),
                                            fromfile='a/' + label, tofile='b/' + label))
    (ROOT / 'records' / 'proposed_diagram_arrays.patch').write_text(''.join(patch))
    (ROOT / 'records' / 'proposed_diagram_arrays.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Prepared', sum(len(item['tables']) for item in manifest), 'table conversions in', len(manifest), 'pages.')
    print('Original tables all recovered exactly by the inverse transformation.')
    print('Live page files were not changed.')


if __name__ == '__main__':
    main()
