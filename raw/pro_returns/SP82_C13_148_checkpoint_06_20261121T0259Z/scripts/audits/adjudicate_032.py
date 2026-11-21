#!/usr/bin/env python3
"""Mechanically apply root's two completed scan032 crop decisions; run once.

Root viewed both differing fixed crops in full. No new image interpretation,
compilation, shared-log change, or audit recording is performed by this script.
"""
from pathlib import Path
import csv,json,re

B=Path(__file__).resolve().parents[2]
stem=B/'second/148_scan032'
with Path(str(stem)+'_comparison.tsv').open() as f:
    comp={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
with Path(str(stem)+'_boxes.tsv').open() as f:
    boxes={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
rp=B/'reviews/148_scan032.json';p=json.loads(rp.read_text())
page=B/'pages/148_scan032.tex';t=page.read_text();original=t
ap=Path(str(stem)+'_adjudications.json')
assert not p.get('second_audit') and not ap.exists(), 'Non-idempotent: already applied.'

def body(s):
    return re.search(r'\\begin\{tikzpicture\}(?:\[[^\n]*?\])?\s*(.*?)\\end\{tikzpicture\}',s,re.S).group(1).strip()

def commands(s):
    s=re.sub(r'(?m)^\s*%[^\n]*\n?','',s)
    return [c.strip()+';' for c in s.split(';') if c.strip()]

def omit(cs,*starts):
    for start in starts:
        assert sum(c.startswith(start) for c in cs)==1,start
    return [c for c in cs if not any(c.startswith(s) for s in starts)]

cs1=commands(body(comp['B032-01']['second']))
cs1=omit(cs1,r'\path[use as bounding box]',r'\clip',r'\fill (378,185)')
second2=body(comp['B032-02']['second'])
second2=second2[second2.index('% Upward curved tail'):second2.index('% Partial neighboring')]
cs2=commands(second2)
cs2=omit(cs2,r'\draw[line width=.18pt] (503,227)',
    r'\draw[line width=.49pt] (198,776)',r'\fill (503,480)',r'\fill (521,480)',
    r'\fill (526,478)',r'\fill (319,709)',r'\fill (357,688)')

scopes={};transforms={}
for key,cs,base in [('B032-01',cs1,.02),('B032-02',cs2,.012)]:
    x0,y0,x1,y1=[int(boxes[key][f]) for f in ('x0','y0','x1','y1')]
    ratio=.007/base
    def pt(m):return f'{float(m.group(1))*ratio:.6f}'.rstrip('0').rstrip('.')+'pt'
    cs=[re.sub(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt',pt,c) for c in cs]
    scopes[key]='\n'.join([rf'\begin{{scope}}[shift={{({x0},{y0})}},line width={ratio:.8f}\pgflinewidth]']+cs+[r'\end{scope}'])
    old=body(comp[key]['first']);assert t.count(old)==1,key
    t=t.replace(old,scopes[key],1)
    transforms[key]=dict(native_box=[x0,y0,x1,y1],basis='native crop pixels',coordinate_scale=1,
        source_base_x_cm=base,target_base_x_cm=.007,physical_size_ratio=ratio)

def figure(content):
    return '\n'.join([r'\figure{',
        r'\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round,line join=round]',
        content,r'\end{tikzpicture}','}'])

finals={key:figure(scope) for key,scope in scopes.items()}
symbol=r'\unsure{\sqrt{1}|\pi}'
ink={
'B032-01':'The outer pencil arc has open lower and right ends, with inner near-parallel arcs, a small upper retrace, a literal angular head and a small right arch open beneath. The isolated speck at native crop (378,185) has no supported textual or diagram role and is omitted. The mark inside has a hooked lower-left stroke, a sloping retraced bar and a right upright. These admit a radical with 1 as well as pi; the radical reading is favored, but no definition settles its identity. Preserve both alternatives instead of resolving the symbol from a supposed mathematical role.',
'B032-02':'Independent curved paths, partial retracings, gaps and irregular hollow rings replace the former straight standardized edges. The upward curved tail, open-ended fan branches, separate lower-left loop, short mark and disconnected hook are visible. Printing fragments and the neighboring oval and its label are already transcribed in their own elements and are not duplicated. Five isolated specks and the pale disconnected horizontal stroke are excluded as background. At the lower main junction the pencil overlaps printed zeros; no separate clean closed pencil ring can be isolated there. Omit that proposed ring while retaining the separate loop farther left and all visible approaching strokes. The exact lower meeting remains uncertain.'
}
entries=[dict(box=key,choice='revised',viewed_by_main=True,final=finals[key],
    ink=ink[key],confidence='low' if key=='B032-01' else 'medium') for key in ['B032-01','B032-02']]

def crop(key):
    return dict(crop=f'crops/second/148_scan032/{key}.png',
        box=[int(boxes[key][f]) for f in ('x0','y0','x1','y1')])

p['changes'][1].update(final=finals['B032-02'],ink=ink['B032-02'],**crop('B032-02'),confidence='medium')
p['changes'][2].update(final=finals['B032-01'],ink=ink['B032-01'],**crop('B032-01'),confidence='medium')
p['changes'][3].update(place='Uncertain radical or pi mark inside the right oval',
    final=symbol,ink=ink['B032-01'],**crop('B032-01'),confidence='low',against_c=True)
assert len(p['decisions'])==1 and p['decisions'][0]['id']=='M0347'
p['decisions'][0].update(decision='undecided',reading=symbol,ink=ink['B032-01'],
    **crop('B032-01'),confidence='low')
for u in p['unresolved']:
    if u['place'].startswith('M0347'):
        u.update(place='M0347: radical or pi mark inside the right open oval',reading=symbol,
            issue=ink['B032-01'],alternatives=[r'\pi'],**crop('B032-01'),confidence='low')
    elif u['place'].startswith('Bipyramid lower junction'):
        u.update(reading=finals['B032-02'],issue=ink['B032-02'],**crop('B032-02'),confidence='medium')
for n in p['notation']:
    if n['form']==r'\unsure{\pi}':
        n.update(form=symbol,observed_use='Small mark in the right open oval: a hooked left stroke, sloping retraced bar and right upright.',
            caution='Radical with 1 is favored, pi remains possible; no local definition determines its identity or mathematical role.')
for inv in p['inventory']:
    if inv['element']=='Possible pi label':
        inv.update(element='Uncertain radical or pi mark',first_words_or_objects=symbol,
            hand='pencil drawing hand; symbol identity uncertain')
    elif inv['element']=='Bipyramid and retraced lower edges':
        inv['first_words_or_objects']='curved connections, irregular hollow and dark marks, open-ended fan branches and separate lower-left loop; main lower meeting obscured by printing'
for note in p['notes']:
    if note['id']=='N032-02':
        note['text']='The small mark inside the right oval favors a radical with 1, while pi remains possible. The hooked lower-left stroke, sloping retraced bar and right upright support both forms; no definition or expected mathematical role resolves them.'
    elif note['id']=='N032-05':
        note['text']='Several lower pencil lines cross the dark printer text. These remain drawing overlaps; no printed word is treated as deleted or replaced. The independent tracing refines the approaching curves, gaps and irregular rings. At the crowded main lower junction no separate closed pencil ring is secure, so none is imposed. The distinct small loop farther down-left remains.'
p['notes'].append(dict(id='N032-BLIND',
    text='The main reader personally viewed both differing fixed crops in full. Both graphic readings were revised, with the neighboring printing and oval represented once in their own elements. Unsupported isolated specks and a pale disconnected horizontal were omitted. The sphere and all 32 complete printed rows remain unchanged. Native crop coordinates use translation only; absolute pt sizes and inherited width are scaled by .007/.02 for the right oval and .007/.012 for the central drawing. No mathematical check or TeX compilation was performed.'))
p['hand_log'].append(dict(habit='A small hooked left stroke with a sloping retraced bar and a separate right upright can resemble either a radical containing 1 or pi.',
    pages=[32],holds_at_every_observed_occurrence='One undefined local mark; no general letter-formation rule is inferred.',
    witness_effect='C left pi doubtful. The independent reading and main-reader crop inspection favor a radical with 1 while retaining pi as an alternative.'))
p['blind_graphic_transforms']=transforms

# Checks address exact retained/removed content; no TeX compilation.
marker='% The mechanical listing is upside down relative to the pencil sketches.'
assert t[t.index(marker):]==original[original.index(marker):]
assert t[:t.index(r'\begin{scope}')]==original[:original.index(r'\coordinate (a)')]
assert t.count('GUTS OUTPUT FOR PREDONT DELIVER AT 0000 - PREDONT.MODULEF5')==32
assert r'\fill (378,185)' not in t
for pair in ['503,480','521,480','526,478','319,709','357,688']:
    assert r'\fill ('+pair+')' not in t
assert r'(198,776)' not in t and r'(503,227)' not in t
for pair in ['160,799','129,663','313,427']:
    assert '('+pair+')' in t
assert t.count(symbol)==1
assert set(finals)=={k for k,c in comp.items() if c['different']=='yes'}
assert all((B/crop(key)['crop']).is_file() for key in finals)
level=0
for m in re.finditer(r'(?<!\\)[{}]',t):
    level+=1 if m.group()=='{' else -1
    assert level>=0,m.start()
assert level==0
page.write_text(t)
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
ap.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=32,adjudications=len(entries),revised_boxes=len(finals),
    changes_rows=len(p['changes']),inventory_rows=len(p['inventory']),
    against_c=sum(bool(r['against_c']) for r in p['changes']),
    against_h=sum(bool(r['against_h']) for r in p['changes']))))
