#!/usr/bin/env python3
"""Structural checks only; no OCR, reading correction, or mathematical checking.

This script reads page fragments and, if present, the combined transcription and
inventory only when explicitly run. It never opens scans or context archives and
never modifies source files. A report path is optional. A successful result is
not a claim of transcription completeness, visual fidelity, or TeX compilation.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


MACROS = {
    'cotefile', 'scanpage', 'mspage', 'deleted', 'inserted', 'margin',
    'uline', 'uuline', 'diagram', 'figure', 'unsure', 'illegible',
}
KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
SHEET_KINDS = {'text', 'reused_typed', 'cancelled_draft', 'cover'}
INVENTORY_COLUMNS = [
    'cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
    'first_words_or_objects', 'transcribed',
]
MATH_ENVS = {
    'math', 'displaymath', 'equation', 'equation*', 'align', 'align*',
    'alignat', 'alignat*', 'gather', 'gather*', 'multline', 'multline*',
    'flalign', 'flalign*', 'eqnarray', 'eqnarray*',
}
COMMAND = re.compile(r'\\([A-Za-z@]+|.)', re.S)


def escaped(text: str, offset: int) -> bool:
    n = 0
    offset -= 1
    while offset >= 0 and text[offset] == '\\':
        n += 1
        offset -= 1
    return n % 2 == 1


def mask_comments(text: str) -> str:
    """Keep offsets and newlines stable while hiding unescaped TeX comments."""
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == '%' and not escaped(text, i):
            j = text.find('\n', i)
            if j < 0:
                j = len(text)
            chars[i:j] = ' ' * (j - i)
            i = j
        else:
            i += 1
    return ''.join(chars)


def skip_space(text: str, offset: int) -> int:
    while offset < len(text) and text[offset].isspace():
        offset += 1
    return offset


def argument(text: str, offset: int):
    """Read one balanced braced argument; return content, end, start or None."""
    start = skip_space(text, offset)
    if start >= len(text) or text[start] != '{':
        return None
    depth = 1
    i = start + 1
    while i < len(text):
        if not escaped(text, i):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    return text[start + 1:i], i + 1, start
        i += 1
    return None


def commands(text: str):
    for match in COMMAND.finditer(text):
        if not escaped(text, match.start()):
            yield match


def check_fragment(path: Path, scan: int, first: int, cote: str, margin_arity: str):
    original = path.read_text(encoding='utf-8')
    text = mask_comments(original)
    issues = []
    counts = Counter()
    spans = []
    math_spans = []
    math_stack = []
    env_stack = []
    begin_commands = {}

    def issue(level, offset, message):
        line = original.count('\n', 0, max(0, offset)) + 1
        issues.append((level, f'{path.name}:{line}: {message}'))

    braces = []
    for i, c in enumerate(text):
        if escaped(text, i):
            continue
        if c == '{':
            braces.append(i)
        elif c == '}':
            if braces:
                braces.pop()
            else:
                issue('ERROR', i, 'unmatched closing brace')
    for i in braces:
        issue('ERROR', i, 'unclosed opening brace')

    values = {name: [] for name in MACROS}
    for match in commands(text):
        name = match.group(1)
        pos = match.start()
        if name in {'documentclass', 'input', 'include', 'includegraphics'}:
            issue('ERROR', pos, f'\\{name} is not permitted in this complete fragment')
        if name in MACROS:
            counts[name] += 1
            arg = argument(text, match.end())
            if arg is None:
                issue('ERROR', pos, f'\\{name} needs one balanced braced argument')
            else:
                content, end, start = arg
                values[name].append((content, pos, end))
                if name in {'diagram', 'figure'}:
                    spans.append((name, start, end))
                if name == 'illegible' and not re.fullmatch(r'\s*\d+\s*', content):
                    issue('ERROR', pos, '\\illegible argument must be an estimated integer count')
                if name == 'margin':
                    second = argument(text, end)
                    if margin_arity == 'one' and second is not None:
                        issue('ERROR', pos, 'suspected two-argument \\margin{...}{...}; one argument required')
                    elif margin_arity == 'two' and second is None:
                        issue('ERROR', pos, 'two-argument margin audit mode selected, but second argument absent')
        if name in {'begin', 'end'}:
            arg = argument(text, match.end())
            if arg is None:
                issue('ERROR', pos, f'\\{name} lacks a balanced environment name')
                continue
            env = arg[0].strip()
            begin_commands[pos] = (name, env, arg[1])
            if env == 'document':
                issue('ERROR', pos, 'document environment belongs in wrapper, not fragment')
            if name == 'begin':
                env_stack.append((env, pos))
            elif not env_stack:
                issue('ERROR', pos, f'\\end{{{env}}} has no matching begin')
            elif env_stack[-1][0] != env:
                issue('ERROR', pos, f'\\end{{{env}}} mismatches open {env_stack[-1][0]}')
            else:
                start_env, start_pos = env_stack.pop()
                if start_env in MATH_ENVS:
                    math_spans.append((start_pos, arg[1]))
    for env, pos in env_stack:
        issue('ERROR', pos, f'unclosed environment {env}')

    # Explicit math delimiters; environment matching was handled above.
    i = 0
    while i < len(text):
        token = None
        length = 1
        if text[i] == '\\' and not escaped(text, i) and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt in '[]()':
                token = '\\' + nxt
                length = 2
        elif text[i] == '$' and not escaped(text, i):
            token = '$$' if text[i:i + 2] == '$$' else '$'
            length = len(token)
        if token in {'\\[', '\\('}:
            math_stack.append((token, i))
        elif token in {'\\]', '\\)'}:
            needed = '\\[' if token == '\\]' else '\\('
            if math_stack and math_stack[-1][0] == needed:
                _, start = math_stack.pop()
                math_spans.append((start, i + length))
            else:
                issue('ERROR', i, f'unmatched math delimiter {token}')
        elif token in {'$', '$$'}:
            if math_stack and math_stack[-1][0] == token:
                _, start = math_stack.pop()
                math_spans.append((start, i + length))
            else:
                math_stack.append((token, i))
        i += length
    for token, pos in math_stack:
        issue('ERROR', pos, f'unclosed math delimiter {token}')

    for _, pos, _ in values['illegible']:
        if any(a <= pos < b for a, b in math_spans):
            issue('ERROR', pos, '\\illegible occurs inside a formula; user requires a best-reading \\unsure')
        if any(kind == 'diagram' and a <= pos < b for kind, a, b in spans):
            issue('ERROR', pos, '\\illegible occurs inside a diagram; user requires \\unsure')

    page_markers = values['scanpage']
    if len(page_markers) != 1 or page_markers[0][0].strip() != str(scan):
        issue('ERROR', 0, f'expected exactly one \\scanpage{{{scan}}}')
    cotes = values['cotefile']
    if scan == first:
        if len(cotes) != 1 or cotes[0][0].strip() != cote:
            issue('ERROR', 0, f'first page must contain exactly one \\cotefile{{{cote}}}')
        expected_start = rf'\cotefile{{{cote}}}\scanpage{{{scan}}}'
    else:
        if cotes:
            issue('ERROR', cotes[0][1], 'unexpected repeated cotefile marker')
        expected_start = rf'\scanpage{{{scan}}}'
    compact = re.sub(r'\s+', '', text)
    if not compact.startswith(expected_start):
        issue('ERROR', 0, f'fragment must start with {expected_start}, allowing comments/whitespace')
    return original, issues, counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-dir', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--first', type=int, default=78)
    parser.add_argument('--last', type=int, default=115)
    parser.add_argument('--cote', default='64')
    parser.add_argument('--stem', default='MPL_64_078-115')
    parser.add_argument('--margin-arity', choices=['one', 'two', 'either'], default='one')
    parser.add_argument('--no-inventory', action='store_true', help='skip inventory while root is auditing')
    parser.add_argument('--require-combined', action='store_true')
    parser.add_argument('--strict-combined', action='store_true', help='require exact concatenated page bytes as UTF-8 text')
    parser.add_argument('--report', type=Path, help='optional plain-text report; source files are never changed')
    args = parser.parse_args(argv)
    root = args.package_dir.resolve()
    expected_scans = set(range(args.first, args.last + 1))
    expected_paths = [root/'pages'/f'{args.stem}_{args.cote}_scan{n:03d}.tex' for n in sorted(expected_scans)]
    issues = []
    total = Counter()
    page_texts = []
    loaded_scans = set()
    for n, path in zip(sorted(expected_scans), expected_paths):
        if not path.is_file():
            issues.append(('ERROR', f'missing page file: {path.name}'))
            continue
        try:
            text, local_issues, counts = check_fragment(path, n, args.first, args.cote, args.margin_arity)
        except (OSError, UnicodeError) as exc:
            issues.append(('ERROR', f'{path.name}: {exc}'))
            continue
        loaded_scans.add(n)
        page_texts.append(text)
        total.update(counts)
        issues.extend(local_issues)
    expected_set = set(expected_paths)
    for path in sorted((root/'pages').glob(f'{args.stem}_{args.cote}_scan*.tex')):
        if path not in expected_set:
            issues.append(('ERROR', f'unexpected page file: {path.name}'))

    combined = root/f'{args.stem}_transcription.tex'
    combined_status = 'not present'
    if combined.is_file() and loaded_scans == expected_scans:
        combined_text = combined.read_text(encoding='utf-8')
        concatenated = ''.join(page_texts)
        if args.strict_combined:
            same = combined_text == concatenated
            combined_status = 'exact concatenation matches' if same else 'exact concatenation differs'
        else:
            normalize = lambda s: re.sub(r'\s+', '', mask_comments(s))
            same = normalize(combined_text) == normalize(concatenated)
            combined_status = 'page sequence matches after comments/whitespace removed' if same else 'page sequence differs'
        if not same:
            issues.append(('ERROR', f'{combined.name}: {combined_status}'))
    elif args.require_combined and not combined.is_file():
        issues.append(('ERROR', f'missing combined fragment: {combined.name}'))

    inventory_count = 0
    if not args.no_inventory:
        inventory = root/f'{args.stem}_inventory.csv'
        if not inventory.is_file():
            issues.append(('ERROR', f'missing inventory: {inventory.name}'))
        else:
            seen_scans = set()
            ids = set()
            with inventory.open(newline='', encoding='utf-8-sig') as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != INVENTORY_COLUMNS:
                    issues.append(('ERROR', 'inventory column names or order differ from requested schema'))
                for row_number, row in enumerate(reader, 2):
                    inventory_count += 1
                    prefix = f'{inventory.name}:{row_number}'
                    try:
                        scan = int(row.get('scan', ''))
                    except (ValueError, TypeError):
                        issues.append(('ERROR', f'{prefix}: invalid scan number'))
                        continue
                    seen_scans.add(scan)
                    if scan not in expected_scans:
                        issues.append(('ERROR', f'{prefix}: scan outside requested range'))
                    if row.get('cote') != args.cote:
                        issues.append(('ERROR', f'{prefix}: incorrect cote'))
                    if row.get('kind') not in KINDS:
                        issues.append(('ERROR', f'{prefix}: unknown element kind'))
                    if row.get('sheet_kind') not in SHEET_KINDS:
                        issues.append(('ERROR', f'{prefix}: unknown sheet kind'))
                    if row.get('transcribed') != 'yes':
                        issues.append(('ERROR', f'{prefix}: transcribed is not yes'))
                    identity = (scan, row.get('element'))
                    if not row.get('element') or identity in ids:
                        issues.append(('ERROR', f'{prefix}: blank or repeated element identifier within scan'))
                    ids.add(identity)
            for scan in sorted(expected_scans - seen_scans):
                issues.append(('ERROR', f'inventory has no rows for scan {scan}'))

    errors = sum(level == 'ERROR' for level, _ in issues)
    lines = [
        'STRUCTURAL QA — no visual, linguistic, or mathematical verification',
        f'Pages loaded: {len(loaded_scans)}/{len(expected_scans)}',
        f'Margin arity mode: {args.margin_arity}',
        f'Combined fragment: {combined_status}',
        f'Inventory rows checked: {inventory_count}' if not args.no_inventory else 'Inventory: skipped by request',
        'Editorial macro counts: ' + ', '.join(f'{name}={total[name]}' for name in sorted(MACROS)),
        f'Errors: {errors}',
    ]
    lines.extend(f'{level}: {message}' for level, message in issues)
    if not issues:
        lines.append('PASS: no checked structural faults found. This is not a completeness or accuracy certificate.')
    report = '\n'.join(lines) + '\n'
    print(report, end='')
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding='utf-8')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
