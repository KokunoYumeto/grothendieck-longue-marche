"""One-use root-approved metadata and scan017 convention synchronization.

The final pages and completed adjudications are authoritative.  This performs
no image interpretation and preserves draft wording in an exact correction log.
Only the scan017 current page changes, as explicitly approved by root; all
frozen independent inputs and adjudications remain byte-identical.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

R = Path(__file__).resolve().parents[1]
NS = (11, 15, 17, 18, 19, 21, 22)
LOG = R / 'documentation/abbreviation_convention_corrections_reader_b.json'
assert not LOG.exists(), 'One-use correction already recorded.'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walkdiff(a, b, path=()):
    if isinstance(a, dict) and isinstance(b, dict):
        result = []
        for key in sorted(a.keys() | b.keys()):
            if key not in a or key not in b:
                result.append(dict(path=list(path + (key,)), before=a.get(key), after=b.get(key)))
            else:
                result.extend(walkdiff(a[key], b[key], path + (key,)))
        return result
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return sum((walkdiff(x, y, path + (i,)) for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [dict(path=list(path), before=a, after=b)]


reports = {n: json.loads((R / f'reviews/149_scan{n:03d}.json').read_text()) for n in NS}
before = copy.deepcopy(reports)
page17_path = R / 'pages/149_scan017.tex'
page17 = before_page17 = page17_path.read_text()
protected = {}
for n in NS:
    for p in (R / 'second').glob(f'149_scan{n:03d}_*'):
        if p.is_file():
            protected[str(p.relative_to(R))] = sha(p)
    if n != 17:
        p = R / f'pages/149_scan{n:03d}.tex'
        protected[str(p.relative_to(R))] = sha(p)

# Six page-level findings: explanatory expansions follow current source forms.
a = reports[11]['abbreviations']
assert a[0]['form'] == 'pt' and 'Notons' in a[0]['place']
a[0]['place'] = 'Le choix paragraph; pt is also a tentative alternative in the cancelled group after Ceci dit, le'
a.insert(1, dict(form='p$^t$', expansion='point', place='Notons insertion; the t is raised'))
assert 'p$^t$' in (R / 'pages/149_scan011.tex').read_text()

a = reports[15]['abbreviations']
assert a[3]['form'] == 'tors. (alternative only)'
a[3] = dict(form='tors (uncertain alternative)', expansion='torsion',
            place='Cancelled word at the start of L16; torsion/tors is uncertain, and the following colon/point is a separate punctuation doubt')
assert r'\unsure{torsion|tors}\unsure{:|.}' in (R / 'pages/149_scan015.tex').read_text()

a = reports[18]['abbreviations']
assert a[0]['form'] == r'\unsure{ens}'
a[0] = dict(form=r'\unsure{ens|en}', expansion='ensemble if ens is the written form; en remains an unresolved alternative',
            place="line8, after l' at the end of line7; expansion explanatory and conditional only")
assert a[0]['form'] in (R / 'pages/149_scan018.tex').read_text()

a = reports[19]['abbreviations']
assert not any('gr.-oïde' in x['form'] for x in a)
a.append(dict(form=r'\unsure{gr.-oïde|gr.-oïdes}', expansion='groupoïde(s)',
              place='left margin, rotated row1; singular/plural ending remains uncertain'))
assert a[-1]['form'] in (R / 'pages/149_scan019.tex').read_text()

a = reports[21]['abbreviations']
assert a[2]['form'] == r'\unsure{th.|Th.}'
a[2] = dict(form=r'\unsure{th.|Th.|H.}',
            expansion='théorème if th./Th. is written; H. remains unresolved',
            place='line5; the letter sequence and case remain uncertain')
assert a[2]['form'] in (R / 'pages/149_scan021.tex').read_text()

a = reports[22]['abbreviations']
assert a[2]['form'] == 'car' and a[3]['form'] == 'démon.'
a[2:4] = [
    dict(form='dém.', expansion='démonstration', place='upper marginal note, la dém. montre bien'),
    dict(form='pr', expansion='pour (proposed)', place='upper marginal parenthesis, bien que pr la'),
    dict(form=r'\unsure{démon.|démonstr.}', expansion='démonstration',
         place='upper marginal parenthesis; the abbreviated ending remains uncertain'),
]
p22 = (R / 'pages/149_scan022.tex').read_text()
assert 'la dém. montre bien' in p22 and 'bien que pr la' in p22
assert r'\unsure{démon.|démonstr.}' in p22

# Root explicitly approved the exact empty-argument replacement and this
# text-mode wrapper after reviewing them.  No ink reading or count changes.
old = r'\unsure{can|\illegible{}}'
new = r'\unsure{can}'
assert page17.count(old) == 1
diagram_start = page17.index('\\[\n(15)\\qquad\n\\diagram{')
diagram_end = page17.index('\n\\]', diagram_start) + len('\n\\]')
old_diagram = page17[diagram_start:diagram_end]
assert old_diagram.endswith('\\end{tikzcd}}\n\\]')
new_diagram = old_diagram.replace('\\[\n(15)\\qquad\n', '\\noindent (15)\\quad', 1)
new_diagram = new_diagram[:-len('\n\\]')]
page17 = page17.replace(old, new, 1).replace(old_diagram, new_diagram, 1)
assert '\\noindent (15)\\quad\\diagram{' in page17
r = reports[17]
paths = [('changes', 8, 'final'), ('inventory', 10, 'first_words_or_objects'),
         ('notation', 5, 'written'), ('notation', 5, 'rendering'), ('doubts', 3, 'reading')]
for field, index, key in paths:
    assert old in r[field][index][key], (field, index, key)
    r[field][index][key] = r[field][index][key].replace(old, new)
convention = (' Current formula serialization uses \\unsure{can}: the unresolved raised traces '
              'remain a low-confidence cluster, not a securely recovered word. The former '
              'empty \\illegible{} alternative is removed only because that macro is not '
              'permitted for a symbol inside a formula; this is not an ink resolution.')
for field, index, key in [('changes', 8, 'evidence'), ('notation', 5, 'evidence'), ('doubts', 3, 'reason')]:
    r[field][index][key] += convention
r['notes'][4] = r['notes'][4].replace('a doubtful raised can/unreadable cluster', 'a doubtful raised can cluster with unresolved traces')
r['notes'][10] = r['notes'][10].replace('recorded tentatively as can or unreadable', 'recorded tentatively as can with unresolved raised traces')
r['notes'].append('Convention-only repair after the completed audit: the tentative Gamma superscript now uses \\unsure{can}, with its unresolved traces still described in the doubts record. The formula no longer uses an empty illegible macro. Diagram(15) is placed in text mode with \\noindent (15)\\quad\\diagram{...}, matching scans010–011, because the supplied diagram macro contains paragraph/center commands. The number, objects, arrows, labels and all source readings are unchanged. Frozen first/second readings, adjudications and audit counts retain their historical values.')

# Ensure only the authorized report fields changed and counts/old audit data stay.
edits = []
for n in NS:
    diff = walkdiff(before[n], reports[n])
    allowed = {'abbreviations'} if n != 17 else {'changes', 'inventory', 'notation', 'doubts', 'notes'}
    assert all(x['path'][0] in allowed for x in diff), n
    if n == 17:
        for x in diff:
            if x['path'][0] == 'changes':
                assert x['path'] in [['changes', 8, 'final'], ['changes', 8, 'evidence']]
    for x in diff:
        x.update(scan=n, report=f'reviews/149_scan{n:03d}.json')
    edits.extend(diff)
    for key in before[n]:
        if key.startswith('audit_') or key in ('audited', 'second_reader'):
            assert before[n][key] == reports[n][key]

for n in NS:
    (R / f'reviews/149_scan{n:03d}.json').write_text(json.dumps(reports[n], ensure_ascii=False, indent=2) + '\n')
page17_path.write_text(page17)
assert all(sha(R / p) == value for p, value in protected.items())
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root approved six page-level abbreviation metadata findings and the exact two017 convention replacements; applied after CP05 release.',
           authority='Current final pages and existing adjudications; no new image reading.',
           metadata_edits=edits,
           page017_replacements=[dict(before=old, after=new), dict(before=old_diagram, after=new_diagram)],
           page017_sha256=dict(before=hashlib.sha256(before_page17.encode()).hexdigest(), after=sha(page17_path)),
           protected_file_hashes=protected, protected_files_unchanged=True,
           counts_and_audit_counts_unchanged=True, aggregate_rebuild_deferred_to_root=True)
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
md = ['# Approved abbreviation and convention corrections — reader B\n',
      log['completed_utc'] + '\n',
      'The six abbreviation findings are metadata-only. Scan017 changes are conventions only: no ink resolution, source number, formula value, substantive witness count or audit changed count is altered. Exact draft wording is preserved below. All frozen comparison inputs and adjudications remain byte-identical.\n']
for n in NS:
    md.append(f'## Scan {n:03d}\n')
    for x in edits:
        if x['scan'] == n:
            md.append('Path: `' + '.'.join(map(str, x['path'])) + '`\n')
            md.append('```json\n' + json.dumps({'before': x['before'], 'after': x['after']}, ensure_ascii=False, indent=2) + '\n```\n')
md.append('## Exact scan017 page replacements\n')
for x in log['page017_replacements']:
    md.append('Before:\n```tex\n' + x['before'] + '\n```\nAfter:\n```tex\n' + x['after'] + '\n```\n')
LOG.with_suffix('.md').write_text('\n'.join(md))
print(json.dumps({'reports': list(NS), 'metadata_edits': len(edits),
                  'page017_replacements': 2, 'protected_files': len(protected),
                  'protected_files_unchanged': True, 'counts_unchanged': True}))
