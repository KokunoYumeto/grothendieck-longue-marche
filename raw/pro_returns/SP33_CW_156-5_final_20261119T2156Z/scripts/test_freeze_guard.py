#!/usr/bin/env python3
"""Exercise work.py's freeze guard exclusively on synthetic temporary files."""
from pathlib import Path
import ast
import csv
import hashlib
import json
import os
import re
import tempfile


def main():
    source = (Path(__file__).parent / 'work.py').read_text()
    module = ast.parse(source)
    names = {'_guard_frozen_transcription', 'regenerate'}
    functions = [node for node in module.body if isinstance(node, ast.FunctionDef) and node.name in names]
    assert len(functions) == 2
    with tempfile.TemporaryDirectory(prefix='synthetic-freeze-guard-') as temp:
        out = Path(temp)
        (out/'pages').mkdir()
        (out/'records').mkdir()
        page = out/'pages/synthetic_scan002.tex'
        combined = out/'SP33_CW_156-5_transcription.tex'
        page.write_text('Synthetic test data.\n')
        (out/'records/scan002.json').write_text(json.dumps({'scan': 2}))
        for name in ('notation', 'abbreviations'):
            (out/f'records/{name}.json').write_text('[]')
        namespace = {
            'OUT': out, 'Path': Path, 'json': json, 'csv': csv,
            're': re, 'hashlib': hashlib,
            'md': lambda value: str(value),
            'mapping': lambda scan: {'folder':'synthetic', 'codex_file':'pages/synthetic_scan002.tex'},
        }
        exec(compile(ast.Module(body=functions, type_ignores=[]), 'synthetic_work_functions', 'exec'), namespace)
        guard = namespace['_guard_frozen_transcription']
        regenerate = namespace['regenerate']
        assert guard() is False
        regenerate()
        assert combined.read_bytes() == page.read_bytes()
        manifest = out/'records/frozen_hashes.json'
        hashes = {str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (page,combined)}
        manifest.write_text(json.dumps(hashes))
        assert guard() is True
        os.utime(combined, ns=(1_000_000_000, 1_000_000_000))
        before = (combined.read_bytes(), combined.stat().st_mtime_ns)
        regenerate()
        assert (combined.read_bytes(), combined.stat().st_mtime_ns) == before
        page.write_text('Changed synthetic data.\n')
        try:
            regenerate()
        except RuntimeError as exc:
            assert 'hash mismatch' in str(exc)
        else:
            raise AssertionError('Changed frozen page was accepted')
        assert (combined.read_bytes(), combined.stat().st_mtime_ns) == before
        page.write_text('Synthetic test data.\n')
        manifest.write_text(json.dumps({str(page.relative_to(out)):hashes[str(page.relative_to(out))]}))
        try:
            guard()
        except RuntimeError as exc:
            assert 'cover exactly' in str(exc)
        else:
            raise AssertionError('Incomplete frozen manifest was accepted')
        manifest.write_text(json.dumps(hashes))
        (out/'pages/unexpected.tex').write_text('Synthetic extra page.\n')
        try:
            guard()
        except RuntimeError as exc:
            assert 'cover exactly' in str(exc)
        else:
            raise AssertionError('Unfrozen added page was accepted')
    print('Synthetic freeze guard passed: normal pre-freeze generation; identical frozen TeX not rewritten; changed pages and incomplete coverage rejected.')


if __name__ == '__main__':
    main()
