#!/usr/bin/env python3
"""Inventory adjacent tikzcd option blocks and probe the explicit option merge.

No source package or shared repair module is modified. Only the unambiguous
ampersand-replacement plus column-separation pair is proposed for merging.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path

import fitz
import build_readers
import editorial
from layout_repairs import _option_end
from texenv import environment
from verify_pdf import parse_log

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'
PROOFS = ROOT / 'work/layout_probes'
PRESERVED_NODES = {
    ('LM_P017', 170, 'B_{D_1^*}'): 'Source inspection identifies the bracketed mathematical first node [B_D1*], followed by its outgoing dotted arrow; it is not a key-value option list.',
    ('LM_C4-153-171', 158, r'\Gamma_{\mathbb Q}\hookrightarrow'): 'Source inspection identifies the bracketed Gamma_Q embedding as part of the first mathematical node before Gamma_Q etale; it is not an option list.',
    ('LM_C4-248-266', 253, 'I'): 'Source inspection identifies [I] as the first mathematical node of the displayed arrow sequence; it is not an option list.',
}


def digest(value):
    return hashlib.sha256(value).hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def inventory():
    manifest = {r['package']: r for r in json.loads((ROOT / 'sources/en/MANIFEST.json').read_text())['packages']}
    rows = []
    files = []
    starts = collections.Counter()
    for language, directory, suffix in [('fr', 'sources/fr/texts', '.tex'), ('en', 'sources/en/packages', '_en.tex')]:
        for package in manifest:
            path = ROOT / directory / (package + suffix)
            raw = path.read_bytes()
            text = raw.decode('utf-8')
            scans = list(re.finditer(r'\\scanpage\{(\d+)[^}]*\}', text))
            sequence = collections.Counter()
            for match in re.finditer(r'\\begin\{tikzcd\}', text):
                starts[language] += 1
                first = match.end()
                while first < len(text) and text[first].isspace():
                    first += 1
                if text[first:first + 1] != '[':
                    continue
                first_end = _option_end(text, first)
                second = first_end
                while second < len(text) and text[second].isspace():
                    second += 1
                if text[second:second + 1] != '[':
                    continue
                second_end = _option_end(text, second)
                scan = next(int(s[1]) for s in reversed(scans) if s.start() <= match.start())
                sequence[scan] += 1
                option1, option2 = text[first + 1:first_end - 1], text[second + 1:second_end - 1]
                explicit = (re.sub(r'\s+', '', option1) == r'ampersandreplacement=\&' and
                            re.sub(r'\s+', '', option2) == 'columnsep=small')
                preserved = PRESERVED_NODES.get((package, scan, option2))
                end = text.index(r'\end{tikzcd}', second_end) + len(r'\end{tikzcd}')
                prefix = text[match.start():second_end]
                old_raw = text[match.start():end]
                new_prefix = text[match.start():first] + '[' + option1 + ',' + option2 + ']'
                new_raw = new_prefix + text[second_end:end]
                assert old_raw[len(prefix):] == new_raw[len(new_prefix):]
                rows.append({'id': f"{manifest[package]['cote']}-{scan}-O{sequence[scan]}",
                             'language': language, 'package': package, 'cote': manifest[package]['cote'], 'scan': scan,
                             'source_path': relative(path), 'source_sha256': digest(raw),
                             'source_line': text[:match.start()].count('\n') + 1,
                             'source_offset_start': match.start(), 'source_offset_end': end,
                             'source_byte_start': len(text[:match.start()].encode('utf-8')),
                             'source_byte_end': len(text[:end].encode('utf-8')),
                             'first_options': option1, 'second_options': option2,
                             'classification': ('UNAMBIGUOUS_DUPLICATED_OPTIONS' if explicit else
                                                'MATHEMATICAL_BRACKETED_NODE_PRESERVED' if preserved else 'MANUAL_SOURCE_REVIEW_REQUIRED'),
                             'source_context_review': preserved or 'The second block is the explicit TikZ key-value option column sep=small.' if explicit or preserved else 'Pending manual source review.',
                             'old_prefix': prefix, 'new_prefix': new_prefix if explicit else None,
                             'source_old': old_raw, 'source_new': new_raw if explicit else None,
                             'old': old_raw.replace('\r\n', '\n'),
                             'new': new_raw.replace('\r\n', '\n') if explicit else None,
                             'kind': 'TeX option syntax',
                             'reason': ('Merge the two consecutive tikzcd option blocks into one comma-separated option list. Preserve every diagram-body character, node, arrow, mathematical symbol, and uncertainty wrapper; remove only the accidentally rendered option syntax.' if explicit else
                                        'Preserve this mathematical bracketed node exactly; no option merge or mathematical modification is proposed.'),
                             'diagram_body_sha256': digest(text[second_end:end].encode('utf-8')),
                             'diagram_body_unchanged': True, 'expected_match_count': 1})
            files.append({'path': relative(path), 'sha256_before': digest(raw),
                          'sha256_after': digest(path.read_bytes()), 'unchanged': raw == path.read_bytes()})
    unit_witnesses = []
    for path in sorted((ROOT / 'sources/en/units').rglob('*.tex')):
        text = path.read_text()
        matches = list(re.finditer(re.escape(r'\begin{tikzcd}[ampersand replacement=\&][column sep=small]'), text))
        if matches:
            unit_witnesses.append({'path': relative(path), 'sha256': digest(path.read_bytes()),
                                   'lines': [text[:m.start()].count('\n') + 1 for m in matches],
                                   'occurrences': len(matches)})
    result = {'status': 'SOURCE_INVENTORY_COMPLETE_PROPOSALS_REQUIRE_PROBE_REVIEW',
              'scope': 'All 116 French checked-source packages and all116 assembled English checked-source packages; every literal tikzcd environment start is inspected with bracket-aware option boundaries. Corresponding English unit witnesses are also listed.',
              'tikzcd_environment_starts': dict(starts), 'consecutive_option_candidates': len(rows),
              'unambiguous_proposed_edits': sum(r['classification'] == 'UNAMBIGUOUS_DUPLICATED_OPTIONS' for r in rows),
              'mathematical_bracketed_nodes_preserved': sum(r['classification'] == 'MATHEMATICAL_BRACKETED_NODE_PRESERVED' for r in rows),
              'other_candidates_requiring_review': sum(r['classification'] == 'MANUAL_SOURCE_REVIEW_REQUIRED' for r in rows),
              'records': rows, 'source_files': files, 'english_unit_witnesses': unit_witnesses,
              'shared_repair_module_modified': False, 'source_files_modified': False,
              'observations_generated_by_script': False}
    (DATA / 'double_tikz_options_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    (PROOFS / 'scan252_options_candidate.json').write_text(json.dumps([r for r in rows if r['classification'] == 'UNAMBIGUOUS_DUPLICATED_OPTIONS'], ensure_ascii=False, indent=2) + '\n')
    return result


def probes(data):
    if data['other_candidates_requiring_review']:
        raise ValueError('An ambiguous second option block requires manual source qualification before probing.')
    rows = [r for r in data['records'] if r['classification'] == 'UNAMBIGUOUS_DUPLICATED_OPTIONS']
    if len(rows) != 4 or {(r['package'], r['scan']) for r in rows} != {('LM_P026', 252)}:
        raise ValueError('Unexpected source inventory; prepare appropriate source-specific probes explicitly.')
    jobs = []
    for language in ('fr', 'en'):
        selected = sorted([r for r in rows if r['language'] == language], key=lambda r: r['source_line'])
        parts = [build_readers.preamble(language, 0), r'\begin{document}\LMcote{140-2}']
        for form in (0, 1, 2):
            for phase in ('old', 'new'):
                source = (r'\scanpage{252}' + '\n(75) ' + r'\diagram{' + selected[0][phase] + '}\n\n' +
                          r'\diagram{' + selected[1][phase] + '}\n')
                body, _, _ = editorial.annotate(source, 'LM_P026', language)
                parts.append(r'\clearpage' + '\n' + f'\\LMform={form}\n' + body)
        parts.append(r'\end{document}')
        tex = PROOFS / f'scan252_options_{language}.tex'
        tex.write_text('\n'.join(parts))
        process = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                                    '-halt-on-error', tex.name], cwd=PROOFS, env=environment(),
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((language, tex, process))
    records = []
    for language, tex, process in jobs:
        console, _ = process.communicate()
        tex.with_suffix('.console.txt').write_text(console)
        log = parse_log(tex.with_suffix('.log'))
        if process.returncode:
            raise RuntimeError('Source-specific option probe failed for ' + language)
        with fitz.open(tex.with_suffix('.pdf')) as doc:
            if len(doc) != 6:
                raise ValueError('Expected six isolated before/after form pages for ' + language)
            for index, page in enumerate(doc):
                form = index // 2
                phase = 'before' if index % 2 == 0 else 'after'
                image = PROOFS / f'scan252_options_{language}_{form}_{phase}.png'
                page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(50, 65, 555, 255), alpha=False).save(image)
                plain = re.sub(r'\s+', '', unicodedata.normalize('NFKC', page.get_text()))
                records.append({'language': language, 'form': form, 'phase': phase, 'physical_page': index + 1,
                                'pdf': relative(tex.with_suffix('.pdf')), 'pdf_sha256': digest(tex.with_suffix('.pdf').read_bytes()),
                                'image': relative(image), 'image_sha256': digest(image.read_bytes()),
                                'literal_option_text_detected': 'columnsep=small' in plain,
                                'log': relative(tex.with_suffix('.log')), 'log_sha256': digest(tex.with_suffix('.log').read_bytes()),
                                'compile_exit_code': process.returncode, 'error_count': log['error_count'],
                                'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
                                'status': 'PENDING_ACTUAL_VISUAL_REVIEW'})
        print(language + ': six before/after form pages; errors=' + str(log['error_count']) +
              ', overfull=' + str(log['overfull_count']) + ', missing=' + str(log['missing_character_count']), flush=True)
    result = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': records,
              'source_inventory': 'work/data/double_tikz_options_audit.json',
              'source_inventory_sha256': digest((DATA / 'double_tikz_options_audit.json').read_bytes()),
              'observations_generated_by_script': False}
    (PROOFS / 'scan252_options_validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compile', action='store_true')
    args = parser.parse_args()
    result = inventory()
    print(json.dumps({k: result[k] for k in ('tikzcd_environment_starts', 'consecutive_option_candidates',
                                            'unambiguous_proposed_edits', 'other_candidates_requiring_review')}), flush=True)
    if args.compile:
        probes(result)


if __name__ == '__main__':
    main()
