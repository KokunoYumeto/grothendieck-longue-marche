from pathlib import Path
from datetime import datetime, timezone
import json, re

b=Path('/workspace/scratch/4770596940a0');p=b/'out/readers/R1'
tp=p/'scan033.tex';jp=p/'scan033.json'
tex=tp.read_text();r=json.loads(jp.read_text())
assert not any(x['id']=='D37' for x in r['differences'])
(p/'scan033_initial.tex').write_text(tex)
(p/'scan033_initial.json').write_text(jp.read_text())
old=r"prouvons que $A'=A$"
new=r"prouvons que $A'\deleted{\unsure{\in}}=A$"
assert tex.count(old)==1
tex=tex.replace(old,new)
tex=tex.replace(new,'% Supplemental close view: final equality overwrites a separable earlier membership-shaped sign.\n'+new)
tp.write_text(tex)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
crop=['crops/R1/scan033_supp_relation.png','crops/R1/scan033_supp_relation_context.png']
r['differences'].append(dict(
    id='D37',supplemental=True,place='2°), heavily traced relation in prouvons que A-prime ... A',
    C=r"A'=A",H=r"A'=A",reading=r"A'\deleted{\unsure{\in}}=A",
    ink='Two heavy near-horizontal bars give the final equality. Separately visible beneath/around them are a thin curved cap rising above the upper bar, a curved left side, and a short middle horizontal between the heavy bars. Those earlier strokes favour a membership sign; its exact old form remains marked uncertain.',
    confidence='medium',confidence_detail='High confidence in final = and in the presence of earlier curved/middle-bar strokes; medium confidence in identifying the earlier sign as in.',
    kind='Supplemental overwritten relation; earlier layer omitted by C, H and R1 initial TEX',
    crop=crop,against_C=True,against_H=True,marked_in_H=False,
    previous_R1_evidence='Original D36 and the initial TEX retained in the initial snapshot; D37 refines only the local overwritten layer.',
    mathematical_effect='No change to the live equality and no mathematical proof inferred from the overwriting.'))
r['inventory'].append(dict(element='I42',kind='overwritten relation',
    position='between A-prime and A after prouvons que in 2°)',
    first_words_or_objects='Earlier membership-shaped sign, uncertain, under final equality',
    sheet_kind='text',hand='his hand',transcribed='yes',supplemental=True))
r['remaining_doubts'].append(dict(difference_id='D37',place='2°), earlier relation under equality',
    reading=r'\deleted{\unsure{\in}}',confidence='medium'))
r['notation'].append(dict(place='2°), prouvons que A-prime ... A',
    reading=r"A'\deleted{\unsure{\in}}=A",decision='Final equality clear; earlier membership-shaped strokes retained as an uncertain overwritten layer.'))
r['notes'].append(dict(id='N033-6',type='supplemental reading note',
    text='A focused recheck of the heavily traced equality separated an earlier curved sign with a short middle bar, favouring in. The overwritten layer was added without changing the live equality. This was an ink reading, not a mathematical check.'))
r['images_viewed'].extend(crop)
r['crops']=json.loads((b/'crops/R1/scan033_recipes.json').read_text())
# The original top crop begins below the page number; add the already-viewed whole source as its exact evidence.
for x in r['differences']:
    if x['id']=='D35':
        x['crop'].append('source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033.jpg')
        x['evidence_note']='The page-number point is in the whole image; the existing top crop starts below it.'
r['initial_end_utc']=r['end_utc'];r['end_utc']=now
r['supplemental_reviews']=[dict(locus='D37',start_utc='2026-11-19 22:41:41 UTC',end_utc=now,
    model='GPT-6 Astra Pro',effort='inherited; not separately exposed',
    run='R1-scan033-supplement-relation-20261119T224141Z',
    activity='Focused enlarged ink reading; no new mathematical check event',images_viewed=crop,
    original_evidence=['out/readers/R1/scan033_initial.tex','out/readers/R1/scan033_initial.json'],
    evidence_preservation='Initial files saved; all original readings, C-doubt decisions and check events retained. D35 additionally links the already-viewed whole image for page-number evidence.',
    no_other_readers_consulted=True,no_later_scan_opened=True)]
depth=0;minimum=0
for c in tex:
    if c=='{':depth+=1
    if c=='}':depth-=1
    minimum=min(minimum,depth)
s=dict(brace_balance=depth,minimum_brace_depth=minimum,dollar_count=tex.count('$'),
       dollar_count_even=tex.count('$')%2==0,display_opens=tex.count('\\['),display_closes=tex.count('\\]'),
       environments_begin=re.findall(r'\\begin\{([^}]+)\}',tex),
       environments_end=re.findall(r'\\end\{([^}]+)\}',tex),compiled=False,
       scope='Mechanical delimiter/environment review after local supplemental insertion')
assert depth==0 and minimum==0 and s['dollar_count_even']
assert s['display_opens']==s['display_closes']
assert sorted(s['environments_begin'])==sorted(s['environments_end'])
r['syntax_check']=s
jp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(p/'scan033_crops.json').write_text(json.dumps(r['crops'],ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(r['differences']),C_doubts=len(r['C_doubt_resolutions']),
    inventory=len(r['inventory']),crops=len(r['crops']),end_utc=now,syntax_valid=True),ensure_ascii=False))
