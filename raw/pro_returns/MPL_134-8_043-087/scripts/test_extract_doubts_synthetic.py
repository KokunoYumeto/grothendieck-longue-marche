#!/usr/bin/env python3
"""Validate extract_doubts.py using synthetic strings and temporary fixtures.

No live page, inventory, doubts Markdown, per-scan record, progress log, image,
or context file is read. The only .tex files read are the synthetic fixtures
created by this script in a temporary directory beneath records/.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / 'scripts' / 'extract_doubts.py'
REPORT = ROOT / 'records' / 'doubts_extractor_synthetic_validation.json'


def load_extractor():
    ast.parse(SCRIPT.read_bytes().decode('utf-8'), filename=str(SCRIPT))
    spec = importlib.util.spec_from_file_location('raw_doubts_extractor', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_raw_spans(text, records):
    encoded = text.encode('utf-8')
    for record in records:
        token = record['macro_token_span']
        a = token['start']['character_offset']
        b = token['end']['character_offset']
        assert text[a:b] == '\\' + record['macro']
        span = record['argument_content_span']
        if span is None:
            assert record['raw_argument'] is None
            continue
        start, end = span['start'], span['end']
        assert text[start['character_offset']:end['character_offset']] == record['raw_argument']
        assert encoded[start['utf8_byte_offset']:end['utf8_byte_offset']].decode('utf-8') == record['raw_argument']


def main():
    extractor = load_extractor()
    checks = []

    def checked(name, condition=True):
        assert condition, name
        checks.append({'test': name, 'result': 'pass'})

    def extract(text, scan=901):
        result = extractor.extract_text(text, file='synthetic_scan901.tex', scan=scan)
        validate_raw_spans(text, result['records'])
        return result

    text = 'préface\n\\unsure{a}\n\\illegible{2}'
    result = extract(text)
    assert [r['raw_argument'] for r in result['records']] == ['a', '2']
    first = result['records'][0]
    assert first['location'] == {'line': 2, 'column': 1, 'character_offset': 8, 'utf8_byte_offset': 9}
    assert first['argument_content_span']['start']['character_offset'] == 16
    checked('Basic raw arguments and independently specified Unicode/byte locations', not result['errors'])

    text = r'\unsure{outer {group} \illegible{2} \unsure{x|y}}'
    result = extract(text)
    assert [r['macro'] for r in result['records']] == ['unsure', 'illegible', 'unsure']
    assert [r['raw_argument'] for r in result['records']] == [
        r'outer {group} \illegible{2} \unsure{x|y}', '2', 'x|y']
    checked('Nested targets recorded individually in lexical order; alternative bar preserved', not result['errors'])

    text = r'\unsure{L \{ R \} \\{G} \% done}'
    result = extract(text)
    assert result['records'][0]['raw_argument'] == r'L \{ R \} \\{G} \% done'
    checked('Escaped braces, escaped percent, and structural braces after a doubled backslash', not result['errors'])

    text = (
        '% \\unsure{ignored}\n'
        '\\unsure % comment } \\illegible{ignored}\n'
        ' {A% unmatched } { \\unsure{ignored}\n'
        'B \\{C\\} \\illegible % comment {\n'
        ' {3}}\n'
    )
    result = extract(text)
    assert [r['macro'] for r in result['records']] == ['unsure', 'illegible']
    assert result['records'][0]['raw_argument'] == (
        'A% unmatched } { \\unsure{ignored}\n'
        'B \\{C\\} \\illegible % comment {\n'
        ' {3}'
    )
    assert result['records'][0]['between_name_and_argument'] == ' % comment } \\illegible{ignored}\n '
    assert result['records'][1]['raw_argument'] == '3'
    checked('Commented targets/braces ignored structurally while exact comment text is retained', not result['errors'])

    text = r'\\unsure{literal} \unsurex{longerword} \unsure{yes}'
    result = extract(text)
    assert [r['raw_argument'] for r in result['records']] == ['yes']
    checked('Escaped control sequence and longer control word excluded', not result['errors'])

    text = r'\unsure{a \% literal} \\% \unsure{hidden}' + '\n' + r'\illegible{7}'
    result = extract(text)
    assert [r['raw_argument'] for r in result['records']] == [r'a \% literal', '7']
    checked('Backslash parity before percent distinguishes an escaped percent from a comment', not result['errors'])

    text = r'\unsure{$\mathcal{M}_{\{x\}}\to \unsure{\alpha}$}'
    result = extract(text)
    assert [r['raw_argument'] for r in result['records']] == [
        r'$\mathcal{M}_{\{x\}}\to \unsure{\alpha}$', r'\alpha']
    checked('Nested math and macro groups retained without interpretation', not result['errors'])

    text = '\\unsure\t\r\n\n {spaced} \\illegible{\\unsure{n}}'
    result = extract(text)
    assert [r['raw_argument'] for r in result['records']] == ['spaced', r'\unsure{n}', 'n']
    assert result['records'][0]['between_name_and_argument'] == '\t\r\n\n '
    checked('Whitespace before arguments and a nonnumeric nested illegible argument remain raw', not result['errors'])

    text = r'\unsure x \illegible{4} \unsure'
    result = extract(text)
    assert [r['status'] for r in result['records']] == ['missing_braced_argument', 'complete', 'missing_braced_argument']
    assert result['records'][1]['raw_argument'] == '4'
    assert len(result['errors']) == 2
    checked('Missing braced arguments at an ordinary token and EOF preserve intervening records')

    text = r'\unsure{first} \unsure{open {nested} \illegible{5}'
    result = extract(text)
    assert [r['status'] for r in result['records']] == ['complete', 'unclosed_argument', 'complete']
    assert result['records'][0]['raw_argument'] == 'first'
    assert result['records'][1]['raw_argument'] == r'open {nested} \illegible{5}'
    assert result['records'][2]['raw_argument'] == '5'
    assert len(result['errors']) == 1
    checked('Unclosed outer argument preserves partial raw text, earlier record, and completed nested target')

    text = r'\unsure{open \illegible{2'
    result = extract(text)
    assert [r['status'] for r in result['records']] == ['unclosed_argument', 'unclosed_argument']
    assert [r['unclosed_group_depth'] for r in result['records']] == [2, 1]
    assert len(result['errors']) == 2
    checked('Every nested unclosed target is retained and reported')

    text = r'\unsure{abc% } \illegible{2}'
    result = extract(text)
    assert len(result['records']) == 1
    assert result['records'][0]['raw_argument'] == r'abc% } \illegible{2}'
    assert result['records'][0]['status'] == 'unclosed_argument'
    checked('Comment through EOF cannot close a target argument or introduce a nested target')

    text = '% \\unsure{ignored}\r\\unsure{A% } \\illegible{ignored}\rB}'
    result = extract(text)
    assert len(result['records']) == 1
    assert result['records'][0]['location']['line'] == 2
    assert result['records'][0]['location']['column'] == 1
    assert result['records'][0]['raw_argument'] == 'A% } \\illegible{ignored}\rB'
    checked('Bare-CR comments end correctly while raw carriage returns remain intact', not result['errors'])

    text = 'é\r\n\\unsure  %skip\r\n {α\r\nβ\\% γ}\r\n'
    with tempfile.TemporaryDirectory(prefix='synthetic_doubts_', dir=ROOT / 'records') as temporary:
        folder = Path(temporary)
        crlf = folder / 'synthetic_scan901.tex'
        crlf.write_bytes(text.encode('utf-8'))
        result = extractor.extract_files([crlf])
        record = result['records'][0]
        assert record['location'] == {'line': 2, 'column': 1, 'character_offset': 3, 'utf8_byte_offset': 4}
        assert record['raw_argument'] == 'α\r\nβ\\% γ'
        assert record['between_name_and_argument'] == '  %skip\r\n '
        assert result['sources'][0]['utf8_bytes'] == len(text.encode('utf-8'))
        assert result['sources'][0]['scan'] == 901
        validate_raw_spans(text, result['records'])
        checked('Byte-read UTF-8 fixture preserves CRLF, Unicode, comments, and exact byte spans', not result['errors'])

        malformed = folder / 'synthetic_scan902.tex'
        malformed.write_bytes(b'\\unsure{done} \\illegible{broken')
        output = folder / 'synthetic_extraction.json'
        run = subprocess.run([sys.executable, str(SCRIPT), str(crlf), str(malformed), '--output', str(output)],
                             text=True, capture_output=True, check=False)
        saved = json.loads(output.read_bytes().decode('utf-8'))
        assert run.returncode == 2
        assert saved['summary']['occurrences'] == 3
        assert saved['summary']['complete_occurrences'] == 2
        assert saved['summary']['malformed_occurrences'] == 1
        assert saved['records'][0]['raw_argument'] == 'α\r\nβ\\% γ'
        assert saved['records'][1]['raw_argument'] == 'done'
        assert saved['records'][2]['raw_argument'] == 'broken'
        assert 'ERROR' in run.stderr and 'unclosed' in run.stderr
        checked('CLI emits earlier and partial records to JSON and exits visibly with status 2 on malformed input')

        invalid_utf8 = folder / 'synthetic_scan903.tex'
        invalid_utf8.write_bytes(b'\xff')
        result = extractor.extract_files([crlf, invalid_utf8])
        assert len(result['records']) == 1 and result['records'][0]['raw_argument'] == 'α\r\nβ\\% γ'
        assert result['errors'][0]['code'] == 'source_read_error'
        checked('An unreadable synthetic UTF-8 source preserves records from the earlier synthetic file')

        foreign = folder / 'foreign.json'
        foreign.write_bytes(b'{"unrelated":true}\n')
        before = foreign.read_bytes()
        run = subprocess.run([sys.executable, str(SCRIPT), str(crlf), '--output', str(foreign)],
                             text=True, capture_output=True, check=False)
        assert run.returncode == 2 and foreign.read_bytes() == before
        checked('An unrelated existing JSON artifact is protected from overwrite')

        forbidden = folder / 'synthetic_doubts.md'
        run = subprocess.run([sys.executable, str(SCRIPT), str(crlf), '--output', str(forbidden)],
                             text=True, capture_output=True, check=False)
        assert run.returncode == 2 and not forbidden.exists()
        checked('Markdown output is refused before any write')

        record_path = folder / 'scan901_inventory.json'
        try:
            extractor.validate_output(record_path, [crlf])
        except ValueError:
            checked('Per-scan inventory JSON filenames are protected')
        else:
            raise AssertionError('Per-scan inventory record output was accepted')

    report = {
        'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope': 'Python syntax parse, synthetic in-memory fixtures, and temporary synthetic .tex files only.',
        'live_pages_read': False,
        'images_or_context_read': False,
        'live_doubts_or_metadata_modified': False,
        'tests': checks,
    }
    REPORT.write_bytes((json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    print(f'{len(checks)} synthetic checks passed. No live page extraction was run.')
    print('Validation record:', REPORT)


if __name__ == '__main__':
    main()
