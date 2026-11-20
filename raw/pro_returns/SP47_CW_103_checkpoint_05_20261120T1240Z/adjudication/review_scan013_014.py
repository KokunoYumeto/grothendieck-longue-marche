"""Apply the main reader's explicit cross-page glyph decision, before freeze.

This is an adjudication overlay, not an automated recognition or consistency rule.
The earlier builder/reader returns remain historical records. Run this overlay
after rebuilding scan013 if reproducing the final consolidation.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, copy, re
R=Path(__file__).resolve().parents[1]
page=R/'pages/H103-02_103_scan013.tex'
dp=R/'decisions/scan013.json';cfgp=R/'adjudication/scan013.json'
d=json.loads(dp.read_text());cfg=json.loads(cfgp.read_text());old=page.read_text()
record=R/'records/notation_review_013_014.json'
if not record.exists():
    before={'page':old,'decision':copy.deepcopy(d),'config':copy.deepcopy(cfg)}
    (R/'records/scan013_before_notation_review.json').write_text(json.dumps(before,ensure_ascii=False,indent=2)+'\n')
    review=dict(date=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),type='visual cross-page notation adjudication; not a mathematical check',
      inspected_existing_crops=['readers/scan013/B/c01.png','readers/scan013/B/c07.png','readers/scan013/B/c08.png','readers/scan013/A/crops/c14.png','crops/scan014/main01_example_morphism.png','crops/scan014/main04_brace.png'],
      decision='Use q/g at the first occurrence on both scans013 and014, q thereafter under the reservation. Scan013’s terminal nubs or short hooks do not distinguish a separate g family from scan014. Its first and display forms have the same small bowl and long straight descending stem. This changes candidate order, not certainty. Keep source-specific resolution e on013 and C on014, since the former has a distinct interior return and the latter an open curve without that bar.',
      new_crops=0,whole_or_half_views=0)
    record.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
review=json.loads(record.read_text())
explanation='Cross-page review of retained scan013 B/c01, B/c07, B/c08 and A/c14 against scan014 main01: the same small upper bowl and long nearly straight descender recur. Some scan013 endings have a short left nub or hook, but the first and display forms have no developed left return; these do not establish a distinct g family. Prefer q consistently, retaining g as the alternative at first occurrence. This is a revised candidate order from visible strokes, not a resolution from mathematical context.'
d['changes'][1].update(final=r'\unsure{q|g}',scan_shows=explanation,consequential='The common morphism family across scans013–014 is q/g at first occurrence, with q first; the alphabetic uncertainty remains.',crops=['readers/scan013/B/c01.png','readers/scan013/B/c07.png','readers/scan013/B/c08.png','readers/scan013/A/crops/c14.png'])
for i in [10,13,14,27,30]:
    row=d['changes'][i]
    row['final']=row['final'].replace('g','q')
    row.update(against_c=True,against_h=False,scan_shows='Main cross-page review, using '+', '.join(row['crops'])+': a small bowl and long descender end in at most a short left nub or hook. This is the same q/g family as scan014. Use q under the first-occurrence reservation; star position is unchanged.')
d['changes'][12]['final']=r'F\mathord{-}q_*'
d['changes'][12]['scan_shows']=d['changes'][12]['scan_shows'].split(' Cross-page notation review:')[0]+' Cross-page notation review: the following letter is q under the common q/g reservation; the dash decision is unchanged.'
for u in d['unresolved']:
    if u['place']=='Recurring morphism, first occurrence':u.update(reading=r'\unsure{q|g}',alternatives='q; g',evidence=explanation)
def rename_symbol(s):
    return s.replace('g/q','q/g').replace('g|q','q|g').replace('g_*','q_*').replace('g^*','q^*').replace('g_{*}','q_{*}').replace('g^{*}','q^{*}')
for row in d['notation']:
    row['latex']=rename_symbol(row['latex'])
d['notation'][0].update(sign='q/g',ink=explanation,latex=r'\unsure{q|g};\quad q')
for row in d['inventory']:
    row['first_words_or_objects']=rename_symbol(row['first_words_or_objects'])
    row['first_words_or_objects']=re.sub(r'\bg(?=\s*[:→])','q',row['first_words_or_objects'])
for i,note in enumerate(d['notes']):
    note=note.replace('Case a) calls g “','Case a) calls the q/g morphism “').replace('The recurring morphism is g/q','The recurring morphism is q/g')
    if '[S013.N3]' in note and 'abstract name g' not in note:note+=' The calculation uses the abstract name g; the final source transcription has q/g after the cross-page ink review.'
    d['notes'][i]=note
append='[S013.N8] The later cross-page notation review reused B/c01, B/c07, B/c08 and A/c14, without a new crop or whole/half view. Compared with scan014’s same letter family, the straight descending stems favour q, while the short terminal hooks keep g possible. Candidate order is now q/g on both pages; earlier independent readings and the pre-review decision are preserved. The e in this page’s resolution remains distinct from scan014’s C because the interior return is visible here. This review is a visual adjudication, not a new mathematical check.'
if not any('[S013.N8]' in s for s in d['notes']):d['notes'].append(append)
for i in [1,10,12,13,14,27,30]:
    for key in ['final','scan_shows','against_c','against_h','consequential','crops']:
        if key in d['changes'][i]:cfg['change_overrides'][str(i)][key]=d['changes'][i][key]
cfg['unresolved']=copy.deepcopy(d['unresolved']);cfg['notation']=copy.deepcopy(d['notation']);cfg['notes']=copy.deepcopy(d['notes'])
# Config inventory has unnumbered element labels; preserve those labels.
for dst,src in zip(cfg['inventory'],d['inventory']):dst['first_words_or_objects']=src['first_words_or_objects']
for s in cfg['substitutions']:
    if s['old']==r'$g:X\to Y$':s['new']=r'$\unsure{q|g}:X\to Y$'
    if s['old']==r'F\unsure{\mathord{-}|\to}g_{*}':s['new']=r'F\mathord{-}q_{*}'
additional=[dict(old=r'g_{*}',new=r'q_{*}',count=1),dict(old=r'g^{*}',new=r'q^{*}',count=2),dict(old='$g$',new='$q$',count=1)]
for s in additional:
    if not any(x['old']==s['old'] for x in cfg['substitutions']):cfg['substitutions'].append(s)
new=rename_symbol(old).replace('$g$','$q$')
page.write_text(new);dp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');cfgp.write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print('Applied scan013/014 notation review; no new crops or scan views')
