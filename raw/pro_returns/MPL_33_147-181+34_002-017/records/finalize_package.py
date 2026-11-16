"""Verify the final deliverables and package them without touching frozen source.

Invoke from any working directory with an explicit UTC timestamp from the session
clock. The final ZIP is written beside the work folder and is never overwritten.
"""
from pathlib import Path
import argparse
import collections
import csv
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_147-181+34_002-017'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(timestamp):
    expected = [(33, n) for n in range(147, 182) if n != 169] + [(34, n) for n in range(3, 18)]
    page_paths = [ROOT / 'pages' / f'{PREFIX}_{c}_scan{n:03}.tex' for c, n in expected]
    assert len(list((ROOT / 'pages').glob('*.tex'))) == 49
    for (c, n), path in zip(expected, page_paths):
        assert path.is_file(), path
        page_text = path.read_text()
        if page_text.startswith(f'\\cotefile{{{c}}}\n'):
            page_text = page_text.split('\n',1)[1]
        assert page_text.startswith(f'\\scanpage{{{n}}}'), path

    frozen = []
    for line in (ROOT / 'records/frozen_sha256.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        actual = sha(ROOT / name)
        assert actual == digest, f'FROZEN SOURCE CHANGED: {name}'
        frozen.append({'file': name, 'frozen_sha256': digest, 'actual_sha256': actual, 'unchanged': True})
    assert len(frozen) == 50
    assert {x['file'] for x in frozen} == {p.relative_to(ROOT).as_posix() for p in page_paths} | {f'{PREFIX}_transcription.tex'}

    tex = (ROOT / f'{PREFIX}_transcription.tex').read_text()
    assert tex.startswith('\\cotefile{33}\n\\scanpage{147}')
    assert '\\documentclass' not in tex and '\\begin{document}' not in tex
    cote = None
    order = []
    for kind, value in re.findall(r'\\(cotefile|scanpage)\{(\d+)\}', tex):
        if kind == 'cotefile':
            cote = int(value)
        else:
            order.append((cote, int(value)))
    assert order == expected

    with (ROOT / f'{PREFIX}_inventory.csv').open(newline='') as fh:
        reader = csv.DictReader(fh)
        assert reader.fieldnames == ['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
        inventory = list(reader)
    assert len(inventory) == 951
    assert {(int(row['cote']), int(row['scan'])) for row in inventory} == set(expected)
    assert all(row['transcribed'] == 'yes' for row in inventory)
    assert all(row['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for row in inventory)
    assert all(row['sheet_kind'] in {'text','reused_typed','cancelled_draft','cover'} for row in inventory)

    log = (ROOT / 'progress.log').read_text()
    done = [(int(c),int(n)) for c,n in re.findall(r'^(33|34) scan (\d+) done ', log,re.M)]
    audited = [(int(c),int(n)) for c,n in re.findall(r'^(33|34) scan (\d+) audited ',log,re.M)]
    if not audited:
        # Historical log format may put the cote after the scan number.
        nums = [int(n) for n in re.findall(r'^scan (\d+) audited ',log,re.M)]
        audited = [(33 if n >=147 else 34,n) for n in nums]
    assert done == expected, ('done sequence',done)
    assert audited == expected, ('audit sequence',audited)
    assert log.index('transcription frozen ') < log.index('context opened ')
    assert 'transcription frozen 2026-11-16 00:02:21 UTC' in log
    assert 'context opened 2026-11-16 00:02:28 UTC' in log

    doubts = (ROOT / f'{PREFIX}_doubts.md').read_text()
    table_counts = {}
    for key,start,end in [
        ('notation','# Notation table','## Doubt register'),
        ('doubts','## Doubt register','## Abbreviations encountered'),
        ('abbreviations','## Abbreviations encountered','## Legibility and confidence')
    ]:
        section = doubts.split(start,1)[1].split(end,1)[0]
        table_counts[key] = sum(line.startswith('|') for line in section.splitlines()) - 2
    assert table_counts == {'notation':34,'doubts':406,'abbreviations':80}
    assert sum(path.read_text().count('\\unsure{') for path in page_paths) == 405
    assert sum(path.read_text().count('\\illegible{') for path in page_paths) == 1

    notes = (ROOT / f'{PREFIX}_notes.md').read_text()
    ids = re.findall(r'^### ([DMRI]\d\d)\. ',notes,re.M)
    note_expected = [f'{a}{n:02}' for a,m in [('D',40),('M',28),('R',28),('I',4)] for n in range(1,m+1)]
    assert ids == note_expected
    note_bodies = re.findall(r'^### ([DMRI]\d\d)\. [^\n]+\n(.*?)(?=^#{2,3} |\Z)',notes,re.M|re.S)
    assert len(note_bodies) == 100
    for ident, body in note_bodies:
        assert '**Kind:' in body, ident
        assert any(x in body for x in ['**Earlier context','**Context:**','**MPL_','**N','**S19**']), ident
        if re.search(r'\*\*Kind:\*\*[^\n]*own',body,re.I):
            assert 'confidence' in body.lower(), ident
    for lineno,line in enumerate(notes.splitlines(),1):
        clean = re.sub(r'`[^`]*`','',line)
        assert len(re.findall(r'(?<!\\)\$',clean)) % 2 == 0, ('math delimiter',lineno)
        for math in re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',clean):
            without_escaped_braces = re.sub(r'\\[{}]','',math)
            assert without_escaped_braces.count('{') == without_escaped_braces.count('}'), ('math braces',lineno)
            assert not re.search(r'\\(?:unsure|illegible|deleted|inserted)',math), ('custom math macro',lineno)
    table=[]
    for line in notes.splitlines()+['']:
        if line.startswith('|'):
            table.append(len(re.findall(r'(?<!\\)\|',line)))
        elif table:
            assert len(set(table)) == 1, ('inconsistent Markdown table',table)
            table=[]
    register = notes.split('## 10. Disposition',1)[1].split('## 11.',1)[0]
    register_ids = re.findall(r'^\| \*\*([^*]+)\*\* \|',register,re.M)
    assert len(register_ids) == len(set(register_ids)) == 51
    assert sum(x.startswith('MPL_') for x in register_ids) == 44

    compile_log = (ROOT / 'records/compile_validation.log').read_text()
    assert 'Output written on' in compile_log
    assert not re.search(r'^! ', compile_log, re.M)
    result = {
        'verified_at_utc': timestamp,
        'verdict': 'PASS',
        'frozen_source_files_unchanged': 50,
        'source_page_count': 49,
        'cote_page_counts': {'33':34,'34':15},
        'inventory_rows': len(inventory),
        'inventory_all_transcribed': True,
        'page_completion_and_second_audit_order_verified': True,
        'combined_fragment_order_verified': True,
        'notation_doubt_abbreviation_rows': table_counts,
        'research_notes': len(ids),
        'register_rows': len(register_ids),
        'notes_math_and_table_syntax': 'PASS',
        'prior_compilation_validation': 'PASS; syntax wrapper, not reading edition',
        'frozen_hashes': frozen,
    }
    return result


def package(timestamp, result):
    target = ROOT.parent / f'{PREFIX}.zip'
    assert not target.exists(), f'Will not overwrite {target}'
    (ROOT / 'records/final_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    with (ROOT / 'progress.log').open('a') as log:
        log.write(f'research notes finalized: 100 numbered items; source/context/primary-source and scope QA complete {timestamp}\n')
        log.write(f'final frozen-hash check: all 49 page files and combined transcription unchanged (50/50 SHA-256 matches) {timestamp}\n')
        log.write(f'final validation passed: 49 pages in order; 951 inventory rows all yes; 406 doubts; 100 research notes; 51 register entries {timestamp}\n')
        log.write(f'final ZIP prepared from deliverables and work records; supplied inputs, images, context source files and diagnostic PDFs excluded {timestamp}\n')
    files = sorted(path for path in ROOT.rglob('*') if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc')
    assert all(path.suffix.lower() not in {'.jpg','.jpeg','.png','.pdf','.zip'} for path in files)
    assert all('context' not in path.relative_to(ROOT).parts and 'upload' not in path.relative_to(ROOT).parts for path in files)
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files:
            archive.write(path,path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        assert len([n for n in archive.namelist() if n.startswith('pages/') and n.endswith('.tex')]) == 49
        for item in result['frozen_hashes']:
            assert hashlib.sha256(archive.read(item['file'])).hexdigest() == item['frozen_sha256']
    return {'path':str(target),'bytes':target.stat().st_size,'members':len(files),'sha256':sha(target),'zip_integrity':'PASS','frozen_members_verified':50}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--utc',required=True)
    parser.add_argument('--package',action='store_true')
    args = parser.parse_args()
    assert re.fullmatch(r'\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC',args.utc)
    validation = verify(args.utc)
    if args.package:
        print(json.dumps(package(args.utc,validation),indent=2))
    else:
        print(json.dumps({key:value for key,value in validation.items() if key!='frozen_hashes'},indent=2))
