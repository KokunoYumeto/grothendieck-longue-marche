from pathlib import Path
from datetime import datetime, timezone
import json, re

b = Path('/workspace/scratch/4770596940a0')
p = b/'out/readers/R1'
texpath = p/'scan032.tex'
jsonpath = p/'scan032.json'
tex = texpath.read_text()
report = json.loads(jsonpath.read_text())
assert not any(r['id'] == 'D43' for r in report['differences']), 'Supplement already applied'

# Preserve the submitted files before applying the supplemental locus.
(p/'scan032_initial.tex').write_text(tex)
(p/'scan032_initial.json').write_text(jsonpath.read_text())

before = r"A\in F\setminus G'\subset F'"
after = r"A\in F\underset{\scriptscriptstyle\unsure{\swarrow}}{\setminus}G'\subset F'"
assert tex.count(before) == 1
tex = tex.replace(before, after)
tex = tex.replace('% @ upper part, two cases; both high primes in the first case are visible',
                  '% @ upper part, two cases; both high primes in the first case are visible\n'
                  '% Supplemental recheck: separate hooked down-left mark immediately below the first-case set-difference slash. Its function is uncertain.')
texpath.write_text(tex)

end = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
newcrops = ['crops/R1/scan032_supp_slash_context.png', 'crops/R1/scan032_supp_slash_mark.png']
newrow = dict(
    id='D43', supplemental=True,
    place='First-case formula A in F minus G-prime subset F-prime, directly below the set-difference slash (whole-image x about 1420, y about 315)',
    C=r"A\in F\setminus G'\subset F' (small lower mark omitted)",
    H=r"A\in F\smallsetminus G\subset F' (small lower mark omitted)",
    reading=after,
    ink='A separate small hooked down-left arrow-shaped mark: a longer curved stroke descends from the upper right toward a lower-left point, with a shorter rising arm and a short bottom arm extending right. A visible gap separates it from the large slash above. It is not a prime on G and does not connect to the next line.',
    confidence='medium',
    confidence_detail='High confidence in the presence, separation and downward-left orientation; medium confidence in calling it an arrow; its intended function is unresolved.',
    kind='Supplemental omission in both witnesses and in R1 initial transcription; uncertain annotation',
    crop=newcrops, against_C=True, against_H=True, marked_in_H=False,
    previous_R1_evidence='Original D08 and initial TEX preserved; D08 remains unchanged as a record of the first submitted reading.',
    mathematical_effect='No change of the set-difference operation is inferred. The lower mark is represented spatially beneath the slash and is not assigned a mathematical relation.')
report['differences'].append(newrow)
report['inventory'].append(dict(
    element='I41', kind='small separate annotation', position='beneath first-case set-difference slash',
    first_words_or_objects='Hooked down-left arrow-shaped mark, uncertain function', sheet_kind='text',
    hand='his hand', transcribed='yes', representation=after, supplemental=True))
report['remaining_doubts'].append(dict(difference_id='D43', place=newrow['place'],
    reading=r'\unsure{\swarrow}, function unknown', confidence='medium'))
report['notation'].append(dict(place=newrow['place'], reading=r'\underset{\unsure{\swarrow}}{\setminus}',
    decision='Spatial transcription of the detached lower mark only; no reinterpretation of the main slash.'))
report['notes'].append(dict(id='N032-6', type='supplemental reading note',
    text='A requested close recheck found the small detached hooked down-left mark below the first-case slash. R1 initially omitted it; the original evidence is preserved and the supplemental locus records the correction. This image reading is not a mathematical check.'))
report['images_viewed'].extend(newcrops)
recipes = json.loads((b/'crops/R1/scan032_recipes.json').read_text())
report['crops'] = recipes
report['initial_end_utc'] = report['end_utc']
report['end_utc'] = end
report['supplemental_reviews'] = [dict(
    locus='D43', start_utc='2026-11-19 22:18:39 UTC', end_utc=end,
    model='GPT-6 Astra Pro', effort='inherited; not separately exposed',
    run='R1-scan032-supplement-slashmark-20261119T221839Z',
    activity='Independent enlarged ink reading, not a mathematical check event',
    images_viewed=newcrops,
    original_evidence=['out/readers/R1/scan032_initial.tex','out/readers/R1/scan032_initial.json'],
    evidence_preservation='All original difference rows, C-doubt decisions, notes and check events retained unchanged; only supplemental records appended and the specific TEX locus amended.',
    no_other_readers_consulted=True, no_later_scan_opened=True)]

depth = 0
min_depth = 0
for c in tex:
    if c == '{': depth += 1
    if c == '}': depth -= 1
    min_depth = min(min_depth, depth)
syntax = dict(brace_balance=depth, minimum_brace_depth=min_depth,
              dollar_count=tex.count('$'), dollar_count_even=tex.count('$') % 2 == 0,
              display_opens=tex.count('\\['), display_closes=tex.count('\\]'),
              environments_begin=re.findall(r'\\begin\{([^}]+)\}',tex),
              environments_end=re.findall(r'\\end\{([^}]+)\}',tex),
              compiled=False, scope='Mechanical delimiter/environment review after supplemental insertion only')
assert depth == 0 and min_depth == 0 and syntax['dollar_count_even']
assert syntax['display_opens'] == syntax['display_closes']
assert sorted(syntax['environments_begin']) == sorted(syntax['environments_end'])
report['syntax_check'] = syntax
jsonpath.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(p/'scan032_crops.json').write_text(json.dumps(recipes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(report['differences']), inventory=len(report['inventory']),
    crops=len(recipes), supplemental_locus='D43', end_utc=end, original_evidence_preserved=True,
    syntax_valid=True),ensure_ascii=False))
