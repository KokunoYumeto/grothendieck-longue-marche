from pathlib import Path
from datetime import datetime, timezone
import json, re

b=Path('/workspace/scratch/4770596940a0');p=b/'out/readers/R1'
tp=p/'scan033.tex';jp=p/'scan033.json'
tex=tp.read_text();r=json.loads(jp.read_text())
assert not any(x['id']=='D38' for x in r['differences'])
(p/'scan033_before_faint_margin.tex').write_text(tex)
(p/'scan033_before_faint_margin.json').write_text(jp.read_text())
insert=r'''% @ faint marks between the left rule and Je dis, around source x214–270,y660–725
% Three pale stroke groups; no secure lexical/symbol reading, function or hand.
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
\draw[gray,line width=.35pt] (1.03,1.35) -- (1.40,1.63);
\draw[gray,line width=.25pt] (1.00,1.15) .. controls (1.03,1.12) and (1.08,1.09) .. (1.08,1.04);
\draw[gray,line width=.2pt] (1.08,1.00) -- (1.10,.95);
\draw[gray,line width=.2pt] (0,.025) -- (.20,.15);
\draw[gray,line width=.18pt] (.27,.19) -- (.32,.21);
\draw[gray,line width=.28pt] (.40,.26) .. controls (.57,.33) and (.67,.42) .. (.79,.44);
\end{tikzpicture}}}

'''
needle='% @ middle, Je dis'
assert tex.count(needle)==1
tex=tex.replace(needle,insert+needle)
tp.write_text(tex)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
crop=['crops/R1/scan033_supp_left_faint.png','crops/R1/scan033_supp_left_context.png']
r['differences'].append(dict(
    id='D38',supplemental=True,place='Between long left rule and Je dis, source rectangle x180–285,y620–765',
    C='omitted',H='omitted',
    reading='Three pale stroke groups, preserved graphically without a lexical or mathematical interpretation.',
    ink='Upper group: a short continuous diagonal rising to the right, approximately x254–269,y660–672. Middle group: a small bent/broken trace approximately x253–257,y679–687. Lower group: a longer interrupted diagonal rising rightward, approximately x214–245,y709–724. All are much paler than the black text and lie independently between the long rule and the J of Je dis.',
    confidence='medium',confidence_detail='High confidence that all three groups survive; low confidence about whether they are erased writing, annotation or incidental pen traces. No secure letter, word, arrow or relation is identified.',
    kind='Supplemental pale graphical traces omitted by both witnesses and initial R1 record',
    crop=crop,against_C=True,against_H=True,marked_in_H=False,
    state='Pale and partly interrupted; deletion/erasure status and hand uncertain.',
    mathematical_effect='None assigned. No mathematical check performed.'))
r['inventory'].append(dict(element='I43',kind='pale unassigned graphical traces',
    position='right of long left rule, beside Je dis',
    first_words_or_objects='Short upper rising diagonal; small bent middle trace; longer interrupted lower diagonal',
    sheet_kind='text',hand='uncertain',transcribed='yes, graphical reproduction',
    state='Pale, partly interrupted; function and possible erasure state unresolved',supplemental=True))
r['remaining_doubts'].append(dict(difference_id='D38',place='pale traces beside Je dis',
    reading='unassigned shapes; no confident lexical or symbol reading',confidence='low'))
r['notes'].append(dict(id='N033-7',type='supplemental reading note',
    text='The requested x180–285,y620–765 recheck shows three separate pale stroke groups. Their shapes and relative positions were reproduced in TikZ without inventing a word or mathematical sign. This is an image-reading event, not a mathematical check.'))
r['images_viewed'].extend(crop)
r['crops']=json.loads((b/'crops/R1/scan033_recipes.json').read_text())
previous_end=r['end_utc'];r['end_utc']=now
r['supplemental_reviews'].append(dict(locus='D38',start_utc='2026-11-19 22:47:22 UTC',end_utc=now,
    model='GPT-6 Astra Pro',effort='inherited; not separately exposed',
    run='R1-scan033-supplement-faint-margin-20261119T224722Z',
    activity='Focused enlarged visual reading; no new mathematical check event',images_viewed=crop,
    prior_end_utc=previous_end,
    original_evidence=['out/readers/R1/scan033_before_faint_margin.tex','out/readers/R1/scan033_before_faint_margin.json'],
    evidence_preservation='All existing report rows, C-doubt decisions, prior supplements and mathematical check events retained; three-group drawing and D38/I43 appended.',
    no_other_readers_consulted=True,no_later_scan_opened=True))
depth=0;minimum=0
for c in tex:
    if c=='{':depth+=1
    if c=='}':depth-=1
    minimum=min(minimum,depth)
s=dict(brace_balance=depth,minimum_brace_depth=minimum,dollar_count=tex.count('$'),
       dollar_count_even=tex.count('$')%2==0,display_opens=tex.count('\\['),display_closes=tex.count('\\]'),
       environments_begin=re.findall(r'\\begin\{([^}]+)\}',tex),
       environments_end=re.findall(r'\\end\{([^}]+)\}',tex),compiled=False,
       scope='Mechanical delimiter/environment check after supplemental graphical traces')
assert depth==0 and minimum==0 and s['dollar_count_even']
assert s['display_opens']==s['display_closes']
assert sorted(s['environments_begin'])==sorted(s['environments_end'])
r['syntax_check']=s
jp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(p/'scan033_crops.json').write_text(json.dumps(r['crops'],ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(r['differences']),inventory=len(r['inventory']),
    crops=len(r['crops']),end_utc=now,prior_evidence_preserved=True,syntax_valid=True),ensure_ascii=False))
