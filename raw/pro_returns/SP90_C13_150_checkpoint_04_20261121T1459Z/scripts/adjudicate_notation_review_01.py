"""Record root's direct crop comparison of recurring notation before the audit.

All image decisions were made visually. This script only applies and records
those decisions; it performs no recognition or mathematical normalization.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]

EMPTY = {
    31: [('corollary, first nonemptiness sign', 'corollary_start'),
         ('corollary, last nonemptiness sign', 'corollary_end')],
    32: [('display (14), first case', 'cases14'),
         ('display (15), final sign', 'display15'),
         ('parenthesis after (15), emptiness sign', 'paren15')],
    36: [('line 3, empty-index case', 'notation_empty_case'),
         ('line 5, nonempty-index case', 'notation_nonempty_case')],
    37: [('filtration, initial sign', 'filtration_formula')],
}


def row(scan, place, crop_suffix, c, h, final, evidence, confidence='high'):
    stem=f'150_scan{scan:03}_{crop_suffix}'
    meta=json.loads((ROOT/'crops'/f'{stem}.json').read_text())
    return {'place':place,'C':c,'H':h,'final':final,
            'evidence':evidence,'crop':f'{stem}.jpg','box':meta['box'],
            'confidence':confidence,'kind':'misread symbol or index',
            'error_kind':'symbols and indices','marked_in_H':False,
            'change_C':True,'change_H':True,'consequential':''}


for scan, places in EMPTY.items():
    path=ROOT/'editor'/f'150_scan{scan:03}.json'
    d=json.loads(path.read_text())
    if d.get('notation_review_01'):raise RuntimeError('Already applied')
    page=ROOT/'pages'/f'150_scan{scan:03}.tex'
    tex=page.read_text().replace(r'\varnothing',r'\phi')
    for item in d['changes']:
        item['final']=item['final'].replace(r'\varnothing',r'\phi')
    for key in ['marks','doubts','second_boxes']:
        for item in d[key]:
            item['reading']=item['reading'].replace(r'\varnothing',r'\phi')
    for place,suffix in places:
        d['changes'].append(row(scan,place,suffix,r'\varnothing',r'\emptyset',r'\phi',
            'Root compared this occurrence directly with the later empty-set notation. '
            'The glyph is a small closed loop traversed by a slanted stem extending well '
            'below the loop, the same phi-shaped handwritten form. The literal phi is '
            'retained; the witnesses had substituted a conventional empty-set glyph.'))
    if scan==31:
        before=r'$\ldots)'
        after=r'$\(\mathinner{\cdotp-\, -}\))'
        assert before in tex
        tex=tex.replace(before,after)
        for b in d['second_boxes']:
            b['reading']=b['reading'].replace(before,after)
        d['changes'].append(row(scan,'corollary, final continuation marks','corollary_end',
            r'\ldots',r'\ldots',r'\mathinner{\cdotp-\, -}',
            'Root reread the same existing end-of-line crop. Three detached marks follow '
            'the phi glyph: a point, then two wider short horizontal/slanting strokes. '
            'The closing parenthesis is independent. Their count and mixed shapes are '
            'preserved instead of an equal-dot ellipsis.', 'medium'))
    if scan==37:
        tex=tex.replace(r'I_1\cdots\subset',r'I_1-\, -\subset')
        for b in d['second_boxes']:
            b['reading']=b['reading'].replace(r'I_1\cdots\subset',r'I_1-\, -\subset')
        d['changes'].append(row(scan,'filtration, continuation after I_1','filtration_formula',
            r'I_1\cdots\subset I_{\unsure{n-1}}',r'I_1\subset\ldots\subset I_{n-1}',
            r'I_1-\, -\subset I_{n-1}',
            'Between I_1 and the next inclusion there are two short headless horizontal '
            'strokes, the first slightly longer. No three-point group occurs there. '
            'The absence of H’s extra inclusion had already been recorded; this row '
            'records the separate literal continuation-shape correction.'))
    if scan==36:
        d['crop_place_count']=21
        d['second_boxes'].append({'box':'b18','kind':'notation discrepancy; complete formula',
            'coords':[700,235,1060,355],'reading':r'Si $I=\phi$,',
            'reason':'Complete first empty-index formula; the second case is already in b05.'})
    d['notation'].append({'form':r'\phi','meaning_or_shape':
        'ϕ : l’ensemble vide. Small loop with a long descending crossing stem; '
        'directly compared with the same later handwritten form.','places':
        '; '.join(p[0] for p in places)})
    d['notes'].append('During the cross-page notation review, root directly checked every '
        'empty-set occurrence on this leaf. Each is the phi-shaped loop with long stem, '
        'consistent with scans 040, 041, 045 and 047; the literal form replaces the '
        'earlier normalized empty-set glyph. This is a graphical reading correction, '
        'not a new mathematical proof check.')
    d['hand_log'].append({'habit':'Empty-set notation has a small loop and a long descending crossing stem.',
        'places':'; '.join(p[0] for p in places),'consistent':'Every occurrence on this leaf visually compared with later phi forms.',
        'witness_errors':'Both witnesses normalized the written phi-shaped form to an empty-set glyph.'})
    d['notation_review_01']='Root viewed each cited existing crop; only the two uncropped 036 formulas required new tight crops.'
    page.write_text(tex)
    path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

path=ROOT/'editor/150_scan045.json'
d=json.loads(path.read_text())
page=ROOT/'pages/150_scan045.tex'
assert r'\supsetneqq' in page.read_text()
page.write_text(page.read_text().replace(r'\supsetneqq',r'\supsetneq'))
for c in d['changes']:
    if 'inclusion and cofinal parenthesis' in c['place']:
        c['final']=c['final'].replace(r'\supsetneqq',r'\supsetneq')
        c['evidence']+=' Root’s cross-page comparison of the same crop identifies the curved '
        c['evidence']+='bottom of the superset and one separate crossed lower bar; it does not '
        c['evidence']+='supply two extra lower bars. The strict sign is therefore supersetneq, '
        c['evidence']+='as in the separately inspected strict inclusions of scans 046–047.'
        c['change_C']=True
for b in d['second_boxes']:
    b['reading']=b['reading'].replace(r'\supsetneqq',r'\supsetneq')
d['notes'].append('Root’s cross-page comparison changes the lower-note strict superset '
    'from supersetneqq to supersetneq: the curved lower limb is part of the superset, '
    'with one additional crossed bar, matching the directly inspected strict signs '
    'of scans 046–047. No set-theoretic inference substitutes for that stroke count.')
d['notation_review_01']='Existing margin_d crop directly re-examined for the strict-inclusion bar count.'
path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'notation review {stamp}: root directly compared 8 earlier empty-set glyphs '
            'and adopted literal phi on scans 031, 032, 036, 037; preserved observed '
            'continuation strokes on 031 and 037; corrected strict-superset bar count '
            'on 045; two new formula crops on 036, all other evidence reused.\n')
print('Recorded visual notation decisions on scans 031, 032, 036, 037, 045.')
