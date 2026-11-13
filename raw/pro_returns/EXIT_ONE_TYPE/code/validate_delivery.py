#!/usr/bin/env python3
"""Audit the built deliverable; no assertion of formal mathematical verification."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import platform
import re
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def command(*args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--render-dir', type=Path)
    args = parser.parse_args()
    pdf = ROOT/'EXIT_ONE_TYPE_paper.pdf'
    assert pdf.read_bytes().startswith(b'%PDF-')
    info = command('pdfinfo', str(pdf))
    pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
    font_table = command('pdffonts', str(pdf))
    font_lines = font_table.splitlines()
    assert 'Type 3' not in font_table, 'Bitmap font found'
    embedding_column = font_lines[0].index('emb')
    font_rows = [line for line in font_lines[2:] if line.strip()]
    assert all(line[embedding_column:embedding_column+3]=='yes' for line in font_rows)
    extracted = command('pdftotext', '-layout', str(pdf), '-')
    assert '??' not in extracted, 'Unresolved placeholder in extracted PDF text'
    assert 'INCOMPLETE' in extracted
    log_path = ROOT/'validation/final_lualatex.log'
    log = log_path.read_text()
    fatal_patterns = {
        'tex_error': r'^!', 'missing_glyph': r'Missing character:',
        'overfull_box': r'Overfull \\[hv]box',
        'undefined_citations_or_references': r'There were undefined|(?:Citation|Reference) .+ undefined',
        'unstable_labels': r'Label\(s\) may have changed',
    }
    failures = {key: len(re.findall(pattern, log, re.M)) for key, pattern in fatal_patterns.items()}
    assert not any(failures.values()), failures
    with (ROOT/'EXIT_ONE_TYPE_results.csv').open(newline='') as f:
        results = list(csv.DictReader(f))
    with (ROOT/'EXIT_ONE_TYPE_readings.csv').open(newline='') as f:
        readings = list(csv.DictReader(f))
    assembly = json.loads((ROOT/'code/assembly_output.json').read_text())
    assert len(results)==assembly['numbered_statements']==assembly['result_rows']
    assert not assembly['unresolved_number_labels']
    assert [r['id'] for r in results if r['status']=='Open']==['P3c-general']
    py_expansion = json.loads((ROOT/'code/levels_syzygies_expanded_python.json').read_text())
    js_expansion = json.loads((ROOT/'code/levels_syzygies_expanded.json').read_text())
    assert py_expansion==js_expansion, 'Independent identity expansions differ'
    identities = json.loads((ROOT/'code/levels_syzygies_js_output.json').read_text())
    assert sum(row['checked_identities'] for row in identities)==44
    assert all(row['all_freely_reduce_to_identity'] for row in identities)
    render_count = None
    if args.render_dir:
        rendered = sorted(args.render_dir.glob('page-*.png'))
        render_count = len(rendered)
        assert render_count==pages, (render_count,pages)
    output = {
        'scope': 'Delivery, exact-output agreement, and typesetting checks; not a proof assistant',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(),
        'pdf_pages': pages, 'pdf_bytes': pdf.stat().st_size,
        'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'fonts_embedded': len(font_rows), 'bitmap_fonts': 0,
        'tex_failure_counts': failures,
        'underfull_box_messages': len(re.findall(r'Underfull \\[hv]box',log)),
        'numbered_results': len(results), 'result_status_counts': assembly['status_counts'],
        'reading_rows': len(readings), 'bibliography_entries': assembly['bibliography_entries'],
        'independent_expanded_identity_data_agree': True,
        'identities_freely_verified': 44,
        'rendered_pages': render_count,
        'open_result': 'P3c-general', 'overall_research_status': 'INCOMPLETE',
    }
    (ROOT/'code/validation_output.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
