#!/usr/bin/env python3
"""Record each source occurrence governed by the verified heading guards.

This is an implementation/provenance inventory, not a visual-review claim.
It runs only after the candidate definitions are integrated into the generator.
The source readings and the variant apparatus remain unchanged.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work'
DATA = WORK / 'data'
SCRIPTS = WORK / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from build_readers import BOOKS, INDEX, apparatus


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def implementation_line(path, token):
    matches = [i for i, line in enumerate(Path(path).read_text().splitlines(), 1)
               if token in line]
    if len(matches) != 1:
        raise ValueError(f'Expected one implementation line for {token!r}: {matches}')
    return matches[0]


def main():
    app = read(WORK / 'layout_probes/apparatus_heading_candidate.json')
    retained = read(WORK / 'layout_probes/retained_heading_candidate.json')
    ranges = read(WORK / 'layout_probes/range_heading_candidate.json')
    preamble = SCRIPTS / 'book_preamble.tex'
    generator = SCRIPTS / 'build_readers.py'
    preamble_text = preamble.read_text()
    assert app['new_definition'] in preamble_text, 'Apparatus guard not integrated'
    margin_old = r'\begingroup\LMmarginstyle\parindent=0pt'
    margin_new = margin_old + r'\@beginparpenalty=10000\relax'
    assert margin_new in preamble_text, 'Marginal-note guard not integrated'
    margin_proof = read(DATA / 'note_heading_probe.json')
    assert margin_proof['status'] == 'PASS'
    lines = {
        'apparatus': implementation_line(preamble, r'\newenvironment{LMapparatus}'),
        'retained': implementation_line(generator, r"out += [r'\ifnum\LMform=2',r'\par\smallskip"),
        'range': implementation_line(generator, "pieces += ['% BEGIN PACKAGE '"),
        'margin': implementation_line(preamble, margin_new),
    }
    prov = {lang: read(WORK / 'build' / (lang + '_provenance.json'))
            for lang in ('fr', 'en')}
    grouped = {}
    for lang, value in prov.items():
        groups = collections.defaultdict(list)
        for entry in value['entries']:
            groups[(entry['package'], entry['cote'], int(entry['scan']))].append(entry)
        grouped[lang] = groups
    with (WORK / 'records/MARGINAL_NOTE_CONTEXTS.tsv').open() as stream:
        notes = list(csv.DictReader(stream, delimiter='\t'))
    rows = []
    counts = collections.Counter()

    def add(book, lang, package, cote, scan, source_path, source_line, record_id,
            category, old, new, reason, generator_path, generator_line,
            source_entry_ids='', note_id='', applicability='active generated heading'):
        rows.append(dict(
            reader=book, language=lang, package=package, cote=cote, scan=scan,
            source_path=source_path, source_line=source_line, id=record_id,
            record_basis='generated heading pagination',
            what_was_wrong=category, what_was_done=reason, old=old, new=new,
            generator_path=generator_path, generator_line=generator_line,
            source_entry_ids=source_entry_ids, note_id=note_id,
            applicability=applicability,
        ))
        counts[category] += 1

    for book, (lang, form, _title) in BOOKS.items():
        text = (WORK / 'build' / (book + '.tex')).read_text()
        for (package, cote, scan), entries in grouped[lang].items():
            carry = [e for e in entries if e['kind'] == 'deletion'
                     and (e.get('doubts') or e.get('inherited_doubt'))]
            rendered = apparatus(entries, lang)
            if carry:
                assert retained['new_generated_prefix'] in rendered, 'Retained guard not integrated'
            selected = entries if form == 1 else carry if form == 2 else []
            if not selected:
                continue
            first = selected[0]
            if form == 1:
                kind, spec, before, after, gp = (
                    'apparatus', app, app['old_definition'], app['new_definition'],
                    'work/scripts/book_preamble.tex')
            else:
                kind, spec, before, after, gp = (
                    'retained', retained, retained['old_generated_prefix'],
                    retained['new_generated_prefix'], 'work/scripts/build_readers.py')
            add(book, lang, package, cote, scan, first['source_path'], first['source_line'],
                f'GEN-{kind.upper()}-{cote}-s{scan:03d}', kind + ' heading guard',
                before, after, spec['reason'], gp, lines[kind],
                source_entry_ids=';'.join(e['id'] for e in selected))
        if form < 2:
            for item in INDEX:
                package, cote = item['package'], item['cote']
                span = item['scans'].replace('-', '--')
                old = ranges['old_template'].replace('#1', span)
                new = ranges['new_template'].replace('#1', span)
                assert '% BEGIN PACKAGE ' + package + '\n' + new in text, (
                    'Range guard missing from built source', book, package)
                source_path = ('fr/texts/' + package + '.tex' if lang == 'fr'
                               else 'en/packages/' + package + '_en.tex')
                source = (ROOT / 'sources' / source_path).read_text()
                marker = source.index(r'\scanpage{')
                scan = int(source[marker:].split('{', 1)[1].split('}', 1)[0])
                add(book, lang, package, cote, scan, source_path,
                    source.count('\n', 0, marker) + 1, 'GEN-RANGE-' + package,
                    'scan-range heading guard', old, new, ranges['reason'],
                    'work/scripts/build_readers.py', lines['range'])
        # These rows enumerate conditional applicability, not a claim that each
        # source note prints as a block in every form. The three-line measurement
        # branch and authorial deletion rules continue to decide placement.
        for note in notes:
            if note['language'] != lang or 'Institutional archive footer excluded' in note['action']:
                continue
            add(book, lang, note['package'], note['cote'], int(note['scan']),
                note['source_path'], int(note['source_line']),
                'GEN-MARGIN-' + note['id'].removeprefix('NOTE-'),
                'conditional marginal-note heading guard', margin_old, margin_new,
                'When this original note is emitted as a text-block note, retain its rule and '
                'label with the first body paragraph or display by a locally scoped beginning-'
                'paragraph penalty. Short-margin placement, source wording, anchored deferred '
                'notes and subsequent page breaks inside long notes remain governed by the '
                'existing renderer. This row records applicability, not a claim of block placement.',
                'work/scripts/book_preamble.tex', lines['margin'], note_id=note['id'],
                applicability='conditional: note emitted in the breakable text-block branch')
    keys = [(r['reader'], r['id']) for r in rows]
    assert len(keys) == len(set(keys)), 'Duplicate reader/repair occurrence'
    result = dict(
        status='INTEGRATED_SOURCE_INVENTORY', source_readings_changed=False,
        visual_review_claim=False, rows=rows, counts=dict(counts),
        dependencies=[{'path': str(p.relative_to(ROOT)), 'sha256': digest(p)}
                      for p in (preamble, generator, WORK / 'build/fr_provenance.json',
                                WORK / 'build/en_provenance.json',
                                WORK / 'records/MARGINAL_NOTE_CONTEXTS.tsv')],
        note='Generated rules and headings are edition formatting; these rows are excluded '
             'from manuscript variant logs and apparatus-entry counts. Marginal-note rows '
             'explicitly inventory conditional source applicability.',
    )
    (DATA / 'generated_heading_repairs.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'rows': len(rows), 'counts': dict(counts)}, indent=2))


if __name__ == '__main__':
    main()
