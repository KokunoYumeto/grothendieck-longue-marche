"""Probe exactly the three wholly cancelled source tags in both languages.

Source files and shared build dependencies are read only.  The replacement
changes AMS-generated parentheses, retaining each source argument once.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import sys

sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers
import editorial
import fitz
import instrument_marks
from texenv import environment

D = Path('work/layout_probes')
DEFINITION = r'\newcommand\LMcancelledtag[1]{\ifnum\LMform=0\tag{#1}\else\tag*{#1}\fi}'
SPECS = [('LM_C3-245-263', r'\tag{\deleted{\unsure{44|43}}}', '44or43'),
         ('LM_C3-245-263', r'\tag{\deleted{\unsure{15}}}', '15'),
         ('LM_C3-359-377', r'\tag{\deleted{55}}', '55')]

def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def readings(entries):
    return [(e['id'], e['kind'], e['manuscript'], e['corrected'],
             e['corrected_tex'], e['math_mode']) for e in entries]

records = []
jobs = []
for lang in ('fr', 'en'):
    fixtures = []
    for package, oldtag, label in SPECS:
        path = Path('sources') / lang / ('texts' if lang == 'fr' else 'packages') / (package + ('_en' if lang == 'en' else '') + '.tex')
        rawbytes = path.read_bytes()
        rawbytes_text = rawbytes.decode()
        raw = build_readers.raw_package(package, lang)
        assert raw.count(oldtag) == rawbytes_text.count(oldtag) == 1
        index = raw.index(oldtag)
        byte_index = len(rawbytes_text[:rawbytes_text.index(oldtag)].encode())
        scan = int(list(re.finditer(r'\\scanpage\{(\d+)\}', raw[:index]))[-1][1])
        newtag = oldtag.replace(r'\tag{', r'\LMcancelledtag{', 1)
        _, all_old, _ = editorial.annotate(raw, package, lang)
        _, all_new, _ = editorial.annotate(raw.replace(oldtag, newtag), package, lang)
        assert readings(all_old) == readings(all_new)
        relevant = [e for e in all_old if index <= e['start'] < index + len(oldtag)]
        assert len(relevant) == 1
        first = raw.rfind(r'\[', 0, index)
        last = raw.index(r'\]', index) + 2
        old = raw[first:last]
        new = old.replace(oldtag, newtag)
        annotations = []
        for snippet in (old, new):
            annotated, entries, _ = editorial.annotate(r'\scanpage{' + str(scan) + '}' + snippet, package, lang)
            annotations.append((annotated, entries))
        assert readings(annotations[0][1]) == readings(annotations[1][1])
        record = dict(language=lang, package=package, source=path.as_posix(),
                      source_sha256=sha(rawbytes), scan=scan, cote='140-3',
                      source_line=raw[:index].count('\n') + 1,
                      source_character_start=index, source_character_end=index + len(oldtag),
                      source_byte_start=byte_index, source_byte_end=byte_index + len(oldtag.encode()),
                      old=oldtag, new=newtag, old_sha256=sha(oldtag),
                      macro_definition=DEFINITION,
                      source_variant_ids=[e['id'] for e in relevant],
                      source_marks=[d['raw'] for e in relevant for d in e['doubts']],
                      original_readings_unchanged=True,
                      reader_mode_intent='Diplomatic form keeps the original parenthesized cancelled argument. Corrected forms select tag* with that same single argument, removing only synthetic AMS parentheses; uncertainty daggers, apparatus originals and linked residual readings remain.',
                      reason='Only the entire tag argument is cancelled. Preserve its exact deletion and uncertainty macros while suppressing generated parentheses around an omitted tag; no partial replacement or uncancelled tag is changed.')
        records.append(record)
        fixtures.append(dict(label=label, scan=scan, annotations=annotations))

    for variant_index, variant in enumerate(('before', 'after')):
        body = [r'\LMcote{140-3}']
        pages = []
        for fixture in fixtures:
            for form in (0, 1, 2):
                ident = f"{lang}-{fixture['scan']}-{fixture['label']}-{form}"
                annotated, entries = fixture['annotations'][variant_index]
                body += [rf'\clearpage\LMform={form}', rf'\noindent Fixture {ident}.\par',
                         annotated, r'\par\noindent Following source text.\par',
                         build_readers.apparatus(entries, lang)]
                pages.append(dict(id=ident, language=lang, scan=fixture['scan'],
                                  label=fixture['label'], form=form))
        source = '\n'.join(body)
        marked, marks = instrument_marks.instrument(source)
        assert instrument_marks.deinstrument(marked) == source
        target = D / f'cancelled_tags_{variant}_{lang}.tex'
        target.write_text(build_readers.preamble(lang, 1) + '\n' + DEFINITION + '\n' +
                          r'\begin{document}' + marked + '\n' + r'\end{document}')
        proc = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                                 '-halt-on-error', target.name], cwd=D, env=environment(),
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, pages, marks, proc))

(D / 'cancelled_tags_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
proof = []
for lang, variant, target, pages, marks, proc in jobs:
    output, _ = proc.communicate()
    target.with_suffix('.console.txt').write_text(output)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=proc.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, variant, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    assert len(doc) == len(pages) == 9
    links = list(csv.DictReader(target.with_suffix('.lm-links.tsv').open(), delimiter='\t'))
    assert all(int(r['linked_runs']) > 0 for r in links), links
    for page, fixture in zip(doc, pages):
        assert f"Fixture {fixture['id']}." in page.get_text()
        image = D / f"cancelled_tags_{variant}_{fixture['id']}.png"
        page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=fitz.Rect(65, 70, 535, 330)).save(image)
        actual_links = page.get_links()
        proof.append(dict(**fixture, variant=variant, compile=counts,
                          extracted_text=page.get_text(),
                          link_count=len(actual_links),
                          link_targets=sorted(link.get('uri', '') for link in actual_links),
                          image=image.as_posix(), image_sha256=sha(image.read_bytes()),
                          status='PENDING_VISUAL'))
for after in [r for r in proof if r['variant'] == 'after']:
    before = next(r for r in proof if r['id'] == after['id'] and r['variant'] == 'before')
    assert after['link_targets'] == before['link_targets'], (after['id'], before['link_targets'], after['link_targets'])
    after['archive_links_preserved'] = True
    # An omitted empty tag also removes its PDF text-extraction newline.
    normalized = lambda text: re.sub(r'\s+', '', text.replace('(', '').replace(')', ''))
    assert normalized(after['extracted_text']) == normalized(before['extracted_text'])
(D / 'cancelled_tags_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',
    semantic_projection='Exact equality of all package variant IDs/kinds/originals/corrected fields and math modes.',
    archive_links='All marked PDF runs linked; exact per-page archive URI multiplicities unchanged before/after.',
    source_sites=6, after_forms=18, forms=proof), ensure_ascii=False, indent=2) + '\n')
