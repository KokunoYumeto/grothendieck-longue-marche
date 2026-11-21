"""Root-authorized pre-blind correction of scan129 continuation shapes.

Uses only the already reviewed scan129 record and existing crop references.
Does not alter the source witnesses, first-reader report/proposal/builder,
fixed box coordinates, crop manifest, or completion log.  The committed page,
reviewed record, first readings and shared notation entry are updated together;
assemble.py is invoked exactly once on the first successful application.

Re-running after the manifest exists verifies the applied state and exits
without another assembly.  The manifest records exact before/after hashes.
"""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
PAGE = ROOT / 'pages/147_scan129.tex'
REVIEW = ROOT / 'review/147_scan129_reviewed.json'
FIRST = ROOT / 'second/147_scan129_first.tsv'
NOTATION = ROOT / 'notation.md'
MANIFEST = ROOT / 'review/147_scan129_preblind_continuations.json'
MARKER = 'Scan129 continuation-shape review (pre-blind)'
PAIR = r'\mathord{-\, -}'
OLD_INDEX = r'_{d_0,\ldots,d_r}'
SINGLE_INDEX = r'_{d_0,-,d_r}'
OLD_NAMED = r'\widetilde\Pi_{d_0-d_r}'
NEW_NAMED = r'\widetilde\Pi_{d_0\unsure{-}d_r}'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rel(path):
    return str(path.relative_to(BASE))

if MANIFEST.exists():
    prior = json.loads(MANIFEST.read_text())
    assert NEW_NAMED in PAGE.read_text()
    assert MARKER in NOTATION.read_text()
    assert any(x['statement_id'].startswith('R129-continuation-shapes')
               for x in json.loads(REVIEW.read_text())['check_events'])
    print(json.dumps({'status':'already applied; no writes or assembly',
                      'manifest':rel(MANIFEST), 'prior_counts':prior['after_counts']}))
    raise SystemExit(0)

protected = [
    ROOT/'reports/147_scan129_report.json',
    ROOT/'reports/147_scan129_proposed.tex',
    ROOT/'reports/147_scan129_build.py',
    ROOT/'reports/147_scan129_crops.jsonl',
    ROOT/'second/147_scan129_boxes.tsv',
    ROOT/'progress.log',
    BASE/'packets/147_scan129/C.tex', BASE/'packets/147_scan129/H.tex'
]
protected_hashes = {rel(p):sha(p) for p in protected}
targets = [PAGE, REVIEW, FIRST, NOTATION]
before_hashes = {rel(p):sha(p) for p in targets}
page = PAGE.read_text()
report = json.loads(REVIEW.read_text())
old_report = json.loads(REVIEW.read_text())

def counts(d):
    return dict(rows=len(d['rows']), against_C=sum(bool(x['against_C']) for x in d['rows']),
                against_H=sum(bool(x['against_H']) for x in d['rows']),
                math_consequential=sum(bool(x['math_consequential']) for x in d['rows']),
                doubts=len(d['doubts']), notes=len(d['notes']),
                check_events=len(d['check_events']), second_boxes=len(d['second_boxes']))

before_counts = counts(report)
assert before_counts['rows'] == 23
assert not any(x['place'].endswith('tuple continuation') for x in report['rows'])

def replace_exact(s, old, new, n=1):
    assert s.count(old) == n, (old, s.count(old), n)
    return s.replace(old, new)

def display(n):
    match = re.search(r'\\\[\n\\tag\{' + str(n) + r'\}.*?\\\]', page, re.S)
    assert match
    return match.group()

old206, old207, old208 = [display(n) for n in [206,207,208]]
old209 = page[page.index(r'\diagram{\(\bigl(\unsure{209}'):
                  page.index(r'\margin{128}')].rstrip()
new206 = replace_exact(old206, r'D^*_{d_0,d_1,\ldots,d_r}', r'D^*_{d_0,d_1,-,d_r}')
new207 = old207
for a,b in [
    (r'P_{d_0,d_1,\ldots,d_r}', r'P_{d_0,d_1,-,d_r}'),
    (r'D_{d_0,\ldots,d_r}', r'D_{d_0,'+PAIR+r',d_r}'),
    (r'P^*_{d_0,d_1,\ldots,d_r}', r'P^*_{d_0,d_1,'+PAIR+r',d_r}'),
    (r'P_{d_0,\ldots,d_r}', r'P_{d_0,-,d_r}'),
    (r'D^*_{d_0,\ldots,d_r}', r'D^*_{d_0,-,d_r}')
]:
    new207 = replace_exact(new207,a,b)
new208 = replace_exact(old208, OLD_INDEX, SINGLE_INDEX, 5)
new209 = replace_exact(old209,OLD_NAMED,NEW_NAMED)
new209 = replace_exact(new209,r'P^*_{d_0,\ldots,d_r}',r'P^*_{d_0,'+PAIR+r',d_r}')
new209 = replace_exact(new209,r'D_{d_0,\ldots,d_r}',r'D_{d_0,-,d_r}')
new209 = replace_exact(new209,r'D^*_{d_0,\ldots,d_r}',r'D^*_{d_0,-,d_r}')
blocks = [(old206,new206),(old207,new207),(old208,new208),(old209,new209)]

def replace_blocks(value):
    for a,b in blocks:
        value = value.replace(a,b)
    return value

new_page = replace_blocks(page)
assert new_page.count(PAIR) == 3
assert new_page.count(r'\ldots') == 1  # true three-mark D tuple in206
assert new_page.count(r'\cdots') == 1  # true three-mark coproduct bound

for b in report['second_boxes']:
    b['reading'] = replace_blocks(b['reading'])
for item in report['inventory']:
    item['first_words_or_objects'] = replace_blocks(item['first_words_or_objects'])
    if item['element'] == 'E02':
        item['first_words_or_objects'] = item['first_words_or_objects'].replace(
            r'D^*_{d_0,d_1,\ldots,d_r}',r'D^*_{d_0,d_1,-,d_r}')
for row in report['rows']:
    row['final'] = replace_blocks(row['final'])
    if row['place'] == '(209), upper-left named index':
        row['final'] = NEW_NAMED
        row['confidence'] = 'medium'
        row['scan_shows'] = (
            'The low 0 is followed by a short rough dash and then d_r, without flanking commas. '
            'A narrow faint interruption crosses its middle; a single dash remains the leading '
            'reading, with local uncertainty about its physical continuity. It is not the clearly '
            'separated pair visible in the adjacent P tuple. This is a notation-shape reading, '
            'with no mathematical subtraction inferred.')
    elif row['place'] == '(209), lower-left retraced D':
        row['final'] = row['final'].replace(OLD_INDEX,SINGLE_INDEX)

# Preserve C/H witness fields and original C spans in deletion/insertion checks.
for decision in report['decisions']:
    if decision['id'] == 'M1289':
        decision['reading'] = decision['reading'].replace(OLD_INDEX,SINGLE_INDEX)
for doubt in report['doubts']:
    if doubt['place'] == '(209), lower-left D':
        doubt['reading'] = doubt['reading'].replace(OLD_INDEX,SINGLE_INDEX)
report['doubts'].append(dict(
    place='(209), rough continuation in the upper-left named index',
    reading=NEW_NAMED,
    alternatives='one short dash with an ink interruption; two very closely separated stroke fragments remain possible, unlike the clearly spaced adjacent P pair',
    confidence='medium'))
report['unresolved'].append(
    'The upper-left named Pi continuation in209 remains dash-primary with a local doubt about its narrow middle interruption.')
for entry in report['notation']:
    if OLD_NAMED in entry['notation']:
        entry['notation'] = entry['notation'].replace(OLD_NAMED,NEW_NAMED)
        entry['meaning_or_form'] += ' The upper dash has a narrow faint interruption and is locally doubtful; the lower dash is continuous.'
    if r'\unsure{D_{d_0,\ldots,d_r}' in entry['notation']:
        entry['notation'] = entry['notation'].replace(OLD_INDEX,SINGLE_INDEX)
report['notation'].append(dict(
    notation=r'd_0,d_1,-,d_r;\quad d_0,-,d_r;\quad d_0,\mathord{-\, -},d_r',
    meaning_or_form=(
        'Continuation shapes are copied literally: one dash is -, and two separate short strokes '
        'are represented by an ordinary math atom containing two spaced strokes. These are serial '
        'continuation marks, not an assertion of mathematical subtraction. The two genuine three-mark '
        'groups in206 retain cdots/ldots; their actual dot/short-stroke mixtures are described in N129-13.'),
    places='129,(206)–(209), seventeen continuation sites'))
for item in report['hand_log']:
    if item['habit'] == 'Continuation dashes and commas vary within nearby multi-indices.':
        item.update(
            habit='A serial index continuation may be one continuous dash, two separate short strokes, or a three-mark dot/stroke group; adjacent occurrences need not match.',
            places='129: all seventeen continuation sites in206–209, including D/P/G tuple indices and the two named Pi indices',
            scope='Eleven clear single dashes, one rough dash with a local middle interruption, and five separated groups: two three-mark groups in206 and three two-stroke groups in207/209. This is a page-local inventory.',
            misreadings='C/H normalize many one-stroke and two-stroke continuations as ldots/dots. The first-reader return initially repeated that normalization outside the named Pi indices; the pre-blind patch corrects thirteen additional locations.')
for check in report['deletion_insertion_checks']:
    if check['span'] == r'\unsure{D_{d_0,\ldots,d_r}}':
        check['finding'] += ' The index continuation itself is one live continuous dash between commas.'

crop_boxes = {x['crop']:x['box'] for x in map(json.loads,
    (ROOT/'reports/147_scan129_crops.jsonl').read_text().splitlines())}
plans = [
    ('(206), first starred D tuple continuation', '206first', True, 'single',
     'After the written d_1 and its comma, one uninterrupted short horizontal stroke precedes another comma and d_r.'),
    ('(207), first unstarred P tuple continuation', '207', True, 'single',
     'After d_0,d_1 and the next comma, there is one continuous dash, then a comma and d_r.'),
    ('(207), source D in the par line, tuple continuation', '207', False, 'pair',
     'Between the two commas after d_0, two separate short horizontal strokes have a clear white gap; no third mark is visible.'),
    ('(207), starred P left of the final equality, tuple continuation', '207', True, 'pair',
     'After the explicit d_1 and comma there are two separated short strokes, followed by a comma and d_r.'),
    ('(207), right-hand P after the final equality, tuple continuation', '207', False, 'single',
     'Between the comma after d_0 and the comma before d_r lies one continuous horizontal dash.'),
    ('(207), right-hand starred D after the restriction bar, tuple continuation', '207', False, 'single',
     'The continuation between the two index commas is a single continuous dash.'),
    ('(208), first G left of the first equality, tuple continuation', '208', False, 'single',
     'The low continuation between the commas after d_0 and before d_r is one continuous short dash.'),
    ('(208), source D in the par line, tuple continuation', '208', False, 'single',
     'The source D index contains one short continuous dash between its two commas.'),
    ('(208), starred G left of the final equality, tuple continuation', '208', False, 'single',
     'After d_0 and its comma there is one slightly slanted continuous dash, followed by a comma and d_r.'),
    ('(208), G right of the final equality, tuple continuation', '208', False, 'single',
     'The longer low dash has an uneven lower edge, but no full white gap separates it into independent marks; commas flank it.'),
    ('(208), starred D after the restriction bar, tuple continuation', '208', False, 'single',
     'A single continuous horizontal dash lies between the two commas in the D index.'),
    ('(209), upper-left P tuple continuation', '209top', False, 'pair',
     'After d_0 and a comma are two distinct marks with a clear gap: a very short first stroke and a longer second horizontal stroke; a comma follows.'),
    ('(209), retraced lower-left D tuple continuation', '209bottom', False, 'single',
     'The index below the retraced D contains one continuous dash between the comma after d_0 and the comma before d_r; this is independent of the uncertainty about a star on D.')
]
new_rows=[]
for place,crop,has_d1,shape,evidence in plans:
    prefix = r'_{d_0,d_1,' if has_d1 else r'_{d_0,'
    mark = '-' if shape == 'single' else PAIR
    crop_path = f'crops/147_scan129_{crop}.jpg'
    new_rows.append(dict(
        place=place,C=prefix+r'\ldots,d_r}',H=prefix+r'\dots,d_r}',
        final=prefix+mark+r',d_r}',scan_shows=evidence+
        ' The change records continuation shape only and does not assert subtraction or alter the indexing range.',
        crop=crop_path,box=crop_boxes[crop_path],confidence='high',
        kind='misread symbol or index',against_C=True,against_H=True,
        marked_in_H=False,math_consequential=False,error_category='Symbols and indices'))

# Retain the original reviewed ordering and append precise, independently located rows.
report['rows'].extend(new_rows)
report['notes'].append(
    'Pre-blind continuation-shape consistency review: the six existing129 crops206first,206maps,207,208,209top and209bottom were reopened; no new first crop was made. '
    'Across seventeen index continuation sites, eleven are clear single dashes, the upper named Pi dash has a narrow doubtful middle interruption, and five are genuinely separated groups. '
    'The coproduct bound in206 has a dot followed by two short strokes; the D tuple in its defini-par line has three separate marks, approximately dot–short stroke–dot. '
    'Those two retain cdots/ldots. The source D and lower starred P of207, and upper-left P of209, have two separate short strokes, rendered as mathord{- thinspace -}. '
    'The first D tuple of206, three other tuples of207, all five tuples of208 and the lower-left D of209 now use literal single dashes; the already literal lower named Pi dash is unchanged. '
    'These marks indicate serial continuation; the encoding does not imply mathematical subtraction or a change in the indexed family. '
    'The earlier first-reader normalization outside the named Pi indices was inconsistent and is corrected in thirteen additional C/H rows before the blind freeze; source and first-reader proposal/report remain preserved.')
assert len(report['notes']) == 13
report['check_events'].append(dict(
    statement_id='R129-continuation-shapes; N129-13',
    type='used and rechecked in this run',
    who='reader_c; root confirmed the distinctions on existing crops before authorizing this patch',
    date=datetime.now(timezone.utc).strftime('%Y-%m-%d'),
    outcome='Re-inspected only existing129 crops and classified all17 continuation sites by visible stroke separation. Corrected13 additional notation-shape locations against C/H, retained the two actual three-mark ellipses, and added local uncertainty to the upper named Pi rough dash. This is a visual notation check, not a mathematical correction or proof.'))
report['preblind_continuation_patch'] = dict(
    script='scripts/patch_scan129_continuations.py',
    manifest='review/147_scan129_preblind_continuations.json',
    added_rows=13,changed_second_boxes=['B01','B04','B07','B08'],
    new_first_crops=0,completion_log_lines_added=0)

notation_line = (
    '\n- '+MARKER+': D/P/G tuple continuations are literal, not uniformly ldots: '
    'eleven clear single dashes and one rough locally doubtful dash coexist with five separated groups. '
    'The bound and source-D tuple of(206) have three separate dot/short-stroke marks; '
    'the source D and lower P* of(207), and upper-left P* of(209), have two separated strokes, '
    r'encoded as `\mathord{-\, -}`. Single strokes use `-`. '
    'These encode serial continuation without an implication of subtraction; see N129-13.\n')
assert MARKER not in NOTATION.read_text()

# Verify the new records before any write or assembly.
after_counts = counts(report)
assert after_counts['rows'] == before_counts['rows']+13
assert after_counts['against_C'] == before_counts['against_C']+13
assert after_counts['against_H'] == before_counts['against_H']+13
assert after_counts['math_consequential'] == before_counts['math_consequential']
assert [(b['box'],b['kind'],b['coords']) for b in report['second_boxes']] == [
    (b['box'],b['kind'],b['coords']) for b in old_report['second_boxes']]
for old,new in zip(old_report['rows'],report['rows']):
    assert old['C'] == new['C'] and old['H'] == new['H']
assert report['decisions'][4]['decision'] == 'undecided'  # root's D_0/d_0 decision
for b in report['second_boxes']:
    if b['box'] in {'B01','B04','B07','B08'}:
        assert b['reading'] in new_page
stack=[]
for i,c in enumerate(new_page):
    if c not in '{}': continue
    j=i-1;slashes=0
    while j>=0 and new_page[j]=='\\': slashes+=1;j-=1
    if slashes%2: continue
    if c=='{': stack.append(i)
    else:
        assert stack, i
        stack.pop()
assert not stack

PAGE.write_text(new_page)
REVIEW.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with FIRST.open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    writer.writerow(['box','reading'])
    writer.writerows((b['box'],b['reading']) for b in report['second_boxes'])
with NOTATION.open('a') as f:
    f.write(notation_line)

first_rows = list(csv.DictReader(FIRST.open(newline=''),delimiter='\t'))
assert first_rows == [dict(box=b['box'],reading=b['reading']) for b in report['second_boxes']]
for p in protected:
    assert sha(p) == protected_hashes[rel(p)], str(p)

# Exactly one assembly; commit_page.py is deliberately not called.
assembled = subprocess.run([sys.executable,str(ROOT/'scripts/assemble.py')],
                           check=True,text=True,capture_output=True)
assembly_summary=json.loads(assembled.stdout.strip())
for p in protected:
    assert sha(p) == protected_hashes[rel(p)], str(p)

manifest=dict(
    scan=129,phase='root-authorized pre-blind consistency correction',
    applied_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    script=rel(Path(__file__)),before_counts=before_counts,after_counts=after_counts,
    continuation_sites=17,clear_single_dashes=11,rough_dash_with_local_doubt=1,
    separated_groups=5,three_mark_groups_preserved=2,two_stroke_groups_encoded=3,
    added_rows=new_rows,changed_second_boxes=['B01','B04','B07','B08'],
    fixed_box_coordinates_changed=False,new_first_crops=0,assemble_invocations=1,
    completion_log_lines_added=0,before_sha256=before_hashes,
    after_sha256={rel(p):sha(p) for p in targets},protected_sha256=protected_hashes,
    assembly_summary=assembly_summary)
MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='applied',manifest=rel(MANIFEST),
                     before=before_counts,after=after_counts,
                     new_rows=13,changed_first_readings=4,assemble_invocations=1,
                     protected_files_unchanged=len(protected)),ensure_ascii=False))
