"""Record main-reader ink decisions for all 13 differing blind boxes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
B=Path(__file__).resolve().parents[2]
stem=B/'second/148_scan025'
with Path(str(stem)+'_comparison.tsv').open() as f:comp={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
with Path(str(stem)+'_boxes.tsv').open() as f:boxes={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
rp=B/'reviews/148_scan025.json';p=json.loads(rp.read_text());assert not p.get('second_audit')
page=B/'pages/148_scan025.tex';t=page.read_text()
new_symbol=r'\unsure{\bar Q|\bar R}'
raised=r'(1,\text{\raisebox{0.6ex}{\(2\)}})'
assert r'\unsure{\bar Q}' in t and '$(1,2)$' in t
t=t.replace(r'\unsure{\bar Q}',new_symbol).replace('$(1,2)$','$'+raised+'$')
ink={
'B025-01':'The word has the separate initial t/é, another tall t, r, a, accented è, d, r and final e: tétraèdre. The following word has o/r/i/e/n/t/é, not unité. The serifed capital has a broader head than foot and a separately headed arrow above. I/T are visually close; the already-seen corresponding Sigma_T and the written descriptor support T, as recorded in the local notation decision. No change.',
'B025-02':'The lower Q has an oval and a diagonal tail. Above it the right-headed arrow is crossed by an additional angular, looping stroke. Preserve the cancellation of the arrow alone; the Q is not struck through. The second reading offers this same state as its first alternative.',
'B025-04':'A closed lower/right oval and diagonal tail favor Q, while the left upright and upper bowl also admit R. The overtracing does not establish which outline preceded the other. Add R as an explicit alternative, retaining the preferred Q, without inventing a definite deleted letter or chronology. The top stroke ends in a downward tick, with no securely separate arrowhead.',
'B025-05':'Under the long strike, an initial tall h with a lower loop, an e/x-shaped middle, the long descending g loop and the joined terminal o/n/e occupy one continuous word. The g descender is not a p followed by a separate word. Retain the canceled hexagone; the strike covers the complete word.',
'B025-06':'The upper horizontal has a thick endpoint where it meets the tall right H stroke, but no separate angled head. The clear vector head in B025-01 supplies a contrasting local form. Retain bar H; do not turn the thick junction into an arrow.',
'B025-07':'Both versions read (0,3). The zero is a closed oval and the three has two rightward lobes. Parentheses and the low comma agree; the only difference is math wrappers.',
'B025-08':'Both versions read (0,4). The last digit has an open angular upper part and descending right stem. The only difference is math wrappers.',
'B025-09':'Both versions read (1,1), each one with an upright and basal foot. The only difference is math wrappers.',
'B025-10':'Both versions read (0,5). The five has a detached short top and a descending bend with a lower leftward foot. The only difference is math wrappers.',
'B025-11':'The second digit is a clear 2 with a curved head and rightward foot. Its body sits visibly above the baseline of the first 1 and above the comma. Adopt the raised placement while retaining it as the second entry of (1,2), not an exponent.',
'B025-12':'Both versions read d=0: a looped d, two separate equality bars and an oval zero. The only difference is math wrappers.',
'B025-13':'Both versions read d=1: a looped d, two separate short equality bars and a footed upright one. The only difference is math wrappers.',
'B025-14':'Both versions read d=2: a looped d, two equality strokes and a long-footed two. The only difference is math wrappers.'}
finals={'B025-04':new_symbol,'B025-11':raised}
entries=[]
for key,c in comp.items():
 if c['different']!='yes':continue
 d=dict(box=key,choice='revised' if key in finals else 'first',viewed_by_main=True,ink=ink[key],
        confidence='low' if key=='B025-04' else 'medium' if key=='B025-01' else 'high')
 if key in finals:d['final']=finals[key]
 entries.append(d)
for r in p['changes']:
 if r['place']=='Fourth-row overwritten first-column symbol':
  r.update(final=new_symbol,ink=ink['B025-04'],crop='crops/second/148_scan025/B025-04.jxl',
           box=[int(boxes['B025-04'][k]) for k in ['x0','y0','x1','y1']])
 if r['place']=='Table column alignment':r['final']=r['final'].replace(r'\unsure{\bar Q}',new_symbol).replace('$(1,2)$','$'+raised+'$')
# The raised second entry is a visible placement difference, not a changed value.
p['changes'].append(dict(place='Last ordered pair, raised second digit',c='(1,2)',h='(1,2)',
 final=raised,ink=ink['B025-11'],crop='crops/second/148_scan025/B025-11.jxl',
 box=[int(boxes['B025-11'][k]) for k in ['x0','y0','x1','y1']],confidence='high',
 kind='insertion or placement',against_c=True,against_h=True,math=False))
for d in p['decisions']:
 if d['id']=='M0267':d.update(reading=new_symbol,ink=ink['B025-04'],crop='crops/second/148_scan025/B025-04.jxl',box=[int(boxes['B025-04'][k]) for k in ['x0','y0','x1','y1']])
for u in p['unresolved']:
 if u['id']=='U025-01':u.update(reading=new_symbol,alternatives=[r'\bar R','unrecoverable sequence of overwritten outlines'],issue=ink['B025-04'],crop='crops/second/148_scan025/B025-04.jxl')
for n in p['notation']:
 if n['id']=='NT025-01':n['form']=n['form'].replace(r'\unsure{\bar Q}',new_symbol)
for n in p['notes']:
 if n['id']=='N025-02':n['text']=ink['B025-04']
p['notes'].append(dict(id='N025-BLIND',text='The main reader inspected all13 differing boxes. The number values and dimensions agree. The R-like outline is added to the uncertain overwritten symbol; no order of replacement is claimed. The final pair retains the visibly raised second entry as placement, not an exponent. The serifed T decision still rests on the letterform together with the local Sigma_T notation.'))
page.write_text(t);rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
Path(str(stem)+'_adjudications.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
 for e in entries:f.write(f'{now}\t025\tcrops/second/148_scan025/{e["box"]}.png\tMain reader viewed differing blind box; {e["ink"]}\n')
print('025:13 crop decisions and two local revisions recorded; first readings unchanged.')
