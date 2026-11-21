"""Apply root's recorded visual comparison of remaining continuation groups.

No recognition is performed. All decisions below were made by viewing the cited
saved crop, including groups whose existing three-point reading was retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT=Path(__file__).resolve().parents[1]

def row(n,place,suffix,c,h,final,evidence,confidence='high'):
    stem=f'150_scan{n:03}_{suffix}'
    crop=json.loads((ROOT/'crops'/f'{stem}.json').read_text())
    return dict(place=place,C=c,H=h,final=final,evidence=evidence,
                crop=stem+'.jpg',box=crop['box'],confidence=confidence,
                kind='misread symbol or index',error_kind='symbols and indices',
                marked_in_H=False,change_C=True,change_H=True,consequential='')

def apply(n,replacements):
    p=ROOT/'editor'/f'150_scan{n:03}.json'
    d=json.loads(p.read_text())
    if d.get('notation_review_02'): raise RuntimeError('Already applied')
    t=(ROOT/'pages'/f'150_scan{n:03}.tex').read_text()
    for old,new in replacements:
        assert old in t,(n,old)
        t=t.replace(old,new)
        for c in d['changes']:c['final']=c['final'].replace(old,new)
        for key in ['marks','doubts','second_boxes']:
            for item in d[key]:item['reading']=item['reading'].replace(old,new)
    return p,d,t

def save(n,p,d,t,note):
    d['notation_review_02']=note
    d['notes'].append(note)
    d['hand_log'].append(dict(habit='Continuation marks vary in count and relative length.',
        places=f'{n:03}: places recorded in notation review 02',
        consistent='Each listed group was viewed separately; no uniform ellipsis was imposed.',
        witness_errors='The witnesses often substitute three conventional points for one or two written strokes.'))
    (ROOT/'pages'/f'150_scan{n:03}.tex').write_text(t)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# 027: preserve the existing uncertainty but encode the mixed shape literally.
p,d,t=apply(27,[(r'\unsure{\ldots}',r'\unsure{\(\mathinner{\cdotp-\cdotp}\)}')])
c=d['changes'][35]
assert c['place']=='lower margin / small marks after par'
c['evidence']='Root re-examined the existing bottom_note crop: the three dark groups are a compact point, an elongated horizontal stroke, and a compact final blob/point. Their function remains uncertain, so the existing doubt is retained around a literal point–stroke–point sequence; no word is supplied.'
for x in d['doubts']:
    if 'ldots' in str(x) or 'small marks' in x.get('place',''):
        x['alternatives']='Three uncertain marks, graphically point–horizontal stroke–point; not completed to words.'
save(27,p,d,t,'Root notation review: the diagonal_note and cylindrical sentence each retain three compact points. The existing bottom_note doubt now preserves its observed point–stroke–point shapes. No crop was regenerated.')

# 028: existing rows already cover these physical places.
p,d,t=apply(28,[(r'$Y_J$\ldots.',r'$Y_J$\(\mathinner{\cdotp\cdotp-}\).'),
               (r'$X_k$\ldots cf.',r'$X_k$\(\mathinner{\cdotp-\, -}\) cf.')])
d['changes'][4]['evidence']='Root re-examined partie_bord: two compact dark points and one longer short horizontal stroke form the close group after Y_J; a fourth separate lower point stands farther right. All four marks are retained with their different shapes.'
d['changes'][4]['confidence']='medium'
c=d['changes'][47]
c['final']=r'\(\mathinner{\cdotp-\, -}\) cf. (0) ci-dessous.'
c['change_C']=True
c['evidence']='The existing rotated margin_final crop shows one compact point followed by two short horizontal strokes before cf. The parenthesized zero and ci-dessous follow as previously read. Three equal points do not preserve the drawn lengths.'
c['confidence']='medium'
save(28,p,d,t,'Root notation review: after Y_J the sequence is two points and a short stroke, then a separate final point; after X_k it is one point and two short strokes. The existing evidence crops were reused.')

# 039: position-specific replacements preserve genuinely different groups.
p,d,t=apply(39,[(r'(i_0,\ldots i_n)',r'(i_0,-i_n)'),
               (r'\Sigma_{i_0,\ldots i_p}',r'\Sigma_{i_0,-i_p}')])
old=r'\Sigma_{i_0\ldots i_n}'
assert t.count(old)==4
new_forms=[r'\Sigma_{i_0\mathinner{\cdotp-}i_n}',
           r'\Sigma_{i_0-\, -i_n}',r'\Sigma_{i_0-\, -i_n}',
           r'\Sigma_{i_0\mathinner{\cdotp-}i_n}']
for new in new_forms:t=t.replace(old,new,1)
t=t.replace(r'\Sigma_{i_0\ldots i_{n-1}}',r'\Sigma_{i_0-\, -i_{n-1}}')
t=t.replace(r'\Sigma_{i_0\ldots\widehat{i_p}\ldots i_n}',
            r'\Sigma_{i_0\mathinner{\cdotp-}\widehat{i_p}\mathinner{\cdotp-}i_n}')
# Apply matching local replacements to the first readings and collation finals.
for collection in [d['second_boxes'],d['changes']]:
    for x in collection:
        key='reading' if 'reading' in x else 'final'
        s=x[key]
        # Complete box / local formula identifies the occurrence independently.
        if r'\longmapsto' in s:
            s=s.replace(old,new_forms[0])
        elif r'i_{n-1}' in s:
            s=s.replace(old,new_forms[2]).replace(r'\Sigma_{i_0\ldots i_{n-1}}',r'\Sigma_{i_0-\, -i_{n-1}}')
        elif r'\widehat{i_p}' in s:
            s=s.replace(old,new_forms[3]).replace(r'\Sigma_{i_0\ldots\widehat{i_p}\ldots i_n}',r'\Sigma_{i_0\mathinner{\cdotp-}\widehat{i_p}\mathinner{\cdotp-}i_n}')
        elif r'i_p}' in s:
            s=s.replace(old,new_forms[1])
        x[key]=s
d['changes'][10]['evidence']='The tuple has a comma after i_0, one very short headless continuation stroke, then i_n. There is no comma before the final index and no three-point sequence.'
d['changes'][14]['evidence']='The target index has a comma after i_0, one headless horizontal continuation stroke, then i_p. There is no comma before i_p and no three-point sequence.'
d['changes'].extend([
 row(39,'functor display / output continuation','functor',old,old,new_forms[0],
     'The output index has two marks between i_0 and i_n: a compact point-like mark followed by a short horizontal stroke. The tuple input has its own separately recorded single-stroke continuation.','medium'),
 row(39,'condition 1 / source continuation','one_map',old,old,new_forms[1],
     'Two separated short horizontal strokes stand between i_0 and i_n. The target has only one stroke after its comma; each side is read independently.'),
 row(39,'sufficiency parenthesis / both index continuations','suffit_map',
     r'\Sigma_{i_0\ldots i_n}\longrightarrow\Sigma_{i_0\ldots i_{n-1}}',
     r'\Sigma_{i_0\ldots i_n}\to\Sigma_{i_0\ldots i_{n-1}}',
     r'\Sigma_{i_0-\, -i_n}\longrightarrow\Sigma_{i_0-\, -i_{n-1}}',
     'Each index contains two detached horizontal strokes. Neither side contains a conventional three-point group.'),
 row(39,'condition 2 / all three continuation groups','two_map',
     r'\Sigma_{i_0\ldots i_n}\longrightarrow\Sigma_{i_0\ldots\widehat{i_p}\ldots i_n}',
     r'\Sigma_{i_0\ldots i_n}\longrightarrow\Sigma_{i_0\ldots\widehat{i_p}\ldots i_n}',
     r'\Sigma_{i_0\mathinner{\cdotp-}i_n}\longrightarrow\Sigma_{i_0\mathinner{\cdotp-}\widehat{i_p}\mathinner{\cdotp-}i_n}',
     'All three groups contain two marks: a compact point-like first mark and a longer horizontal second stroke. The hat above i_p remains distinct. The three groups are not expanded to equal-dot ellipses.','medium')])
d['crop_place_count']=33
d['second_boxes'].append(dict(box='b33',kind='notation comparison',coords=[230,430,1240,545],
    reading=r'espaces topologiques \(\cdots\)).',reason='The whole continuation group and separate closing parenthesis/point, checked visually and retained as three compact points.'))
save(39,p,d,t,'Root notation review: the prose after espaces topologiques retains three compact points. The functor tuple has one stroke, its output has two marks; condition 1 has two source strokes and one target stroke; the sufficiency map has two strokes on both sides; condition 2 has three two-mark groups. Existing formula crops were reused; the previously uncropped prose group received one crop. Every group was directly inspected.')

# 040: one long source stroke and two short continuation strokes in the product.
p,d,t=apply(40,[(r'\Sigma_{i_0\ldots i_n}',r'\Sigma_{i_0-i_n}'),
               (r'\Sigma_{i_1i_n}\cdots',r'\Sigma_{i_1i_n}-\, -')])
c=d['changes'][35]
c['change_C']=True
c['evidence']+=' Root directly re-examined the same crop for continuation shapes: the left index has one long headless stroke between i_0 and i_n; after the second intersection factor are two short horizontal strokes. Those literal counts replace the normalized ellipses.'
save(40,p,d,t,'Root notation review: in the diagonal condition b), the first index has one long stroke and the intersection continuation has two short strokes. The same left_formulas crop was directly inspected; the final factor index remains doubtful.')

stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'notation review {stamp}: root directly checked remaining conventional ellipses on scans 027, 028, 036, 037, 039, 040, 043. Retained actual three-point groups on 027, 036, 037, 039 prose and 043; recorded literal mixed or one/two-stroke groups on 027, 028, 039 formulas and 040. One new crop on 039; all other evidence reused.\n')
print('Recorded second continuation-notation review.')
