"""Apply root's visually adjudicated accounting and audit-record refinements."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
stem = '150_scan044'
d = json.loads((ROOT/'reader_returns'/f'{stem}.json').read_text())
page = (ROOT/'reader_returns'/f'{stem}.tex').read_text()
page = page.removeprefix('\\cotefile{150}\n')
rows = {r['place']: r for r in d['changes']}

r = rows['first display / item number']
r['H'] = r'\note{dans la marge, devant le numéro, « (2°) ».}'
r['change_H'] = False
r['evidence'] += ' Root accounting: H explicitly records the same item in its note, so this is not an omission or a substantive H correction.'

r = rows['cancelled line below decompositions']
r['H'] = r'\note{sous la seconde égalité, une ligne biffée : \struck{$\Sigma_{ii}=\Sigma_i$}.}'
r['kind'] = 'misread symbol or index'
r['error_kind'] = 'symbols and indices'
r['evidence'] = ('The line is crossed. The tentative avec cannot be separated letter by letter; both Sigmas and their ii/i indices survive. The relation has an upper wavy stroke and a lower bar, supporting simeq rather than equality; a terminal closing curve survives. H explicitly records a canceled equality in its editorial note, so that whole line is not called absent. The actual differences are its equality reading and omission of the tentative preceding word and surviving closing curve. The editorial prose itself is not manuscript text.')

r = rows['left margin / Condition circled a']
r['H'] = r'\marginal{condition (a)}\note{« a » cerclé ; le passage qui suit est marqué d\'un trait vertical.}'
# Use a regular apostrophe, not a Python-source escaping backslash, in the quotation.
r['H'] = r['H'].replace("d\\'un", "d'un")
r['evidence'] += ' H itself identifies the circle in its note; the counted H word difference here is the lowercase initial of condition, not failure to recognize the circle.'

r = rows['left margin / first vertical marking stroke']
r['H'] = r'\note{« a » cerclé ; le passage qui suit est marqué d\'un trait vertical.}'.replace("d\\'un", "d'un")
r['change_H'] = False
r['evidence'] += ' Root accounting: H accurately describes the stroke, so only C is counted as missing it.'

r = rows['left margin / second vertical marking stroke']
r['H'] = r'\note{le passage est marqué d\'un trait vertical.}'.replace("d\\'un", "d'un")
r['change_H'] = False
r['evidence'] += ' Root accounting: H accurately describes the stroke, so only C is counted as missing it.'

last_note = r'\note{devant « $\mathrm{Drap}_n(I)$ », un $\Sigma$ biffé ; « OK » est écrit à gauche de la réunion disjointe.}'
r = rows['second display 27 / cancelled symbol before Drap']
r['H'] = last_note
r['change_H'] = False
r['evidence'] += ' Root accounting: H explicitly records the canceled Sigma, and Sigma remains admitted in the final alternative; no H correction is established.'

r = rows['lower left / OK placement']
r['H'] = last_note
r['change_H'] = False
r['evidence'] += ' Root accounting: the accurate left-position statement in H is retained as evidence of its reading; the differing TeX placement alone is not counted as a substantive correction.'

rows['lower left margin / note about condition']['change_C'] = False
for m in d['marks']:
    if m['mark'] == r"\unsure{permet ainsi l'énoncé de la condition (\unsure{b})}":
        m['decision'] = 'undecided'
        m['evidence'] += ' The wording is unchanged from C; narrowing the uncertainty is not a substantive C correction.'

pos = next(i for i, v in enumerate(d['inventory']) if v['element'] == 'D02') + 1
d['inventory'][pos:pos] = [
    {'element':'X09','kind':'deletion','position':'inside the second top decomposition','first_words_or_objects':r'\sum','sheet_kind':'text','hand':'his hand','transcribed':'yes'},
    {'element':'I03','kind':'insertion','position':'over the deleted sum in the second top decomposition','first_words_or_objects':r'\unsure{\coprod}','sheet_kind':'text','hand':'his hand','transcribed':'yes'},
]

boxes = {b['box']:b for b in d['second_boxes']}
a = page.index("(d'où")
b = page.index(' a la propriété') + len(' a')
boxes['b03']['reading'] = page[a:b]
a = page.index(r'\margin{\begin{tabular}', page.index('Cela implique aussi'))
b = page.index(r'\deleted{$\Sigma_i$}', a) + len(r'\deleted{$\Sigma_i$}')
boxes['b06']['reading'] = page[a:b]
for key in ['b03','b06']:
    boxes[key]['reason'] += ' Root replaced English graphic placeholders with the literal page TeX, including all graphic-only paths.'

d['notes'][3] = ('The crossed top relation is simeq, not equality. H records the canceled equality explicitly in an editorial note; that reading is quoted as H evidence, without treating its surrounding editorial prose as authorial text. Its relation and missing preceding/closing ink are actual differences.')
d['notes'][12] = ('H editorial prose is not manuscript text. Explicit source readings and geometry recorded inside H notes nevertheless count as evidence of what H read: the item (2 degrees), circled a, two vertical strokes, canceled Sigma and left-position OK are not called absent. Root excluded those already described features from H correction counts; the lowercase condition and the canceled equality reading remain real differences. New uncertainty or reordered alternatives alone is not a substantive correction. The lower note narrows C uncertainty without changing C wording, so it is not counted as a C change. H’s insertion wrapper around the separately canceled Sigma_i remains a macro difference only.')
d['notes'].append('Root read the complete returned page and every metadata field, directly viewed all 33 crops, refined H-note accounting, added separate inventory entries for the old sum and replacement coproduct, and replaced English placeholders in audit readings with the literal page TeX. No transcription wording was changed during these final accounting refinements.')
for h in d['hand_log']:
    if h['habit'].startswith('Dark correction strokes'):
        h['witness_errors'] = 'No certain strict/nonstrict or I/Sigma correction is claimed; H explicitly records a canceled Sigma in its note.'
d['crop_place_count'] = 33
d['editor_review'] = ('Root directly viewed all 33 crop images and read the complete TeX and all metadata. See editor/150_scan044_visual_review.md. The text preserves literal strokes, uncertain clipped endings and canceled interiors. H-note descriptions were considered as witness evidence without importing editorial prose into the transcription. Audit readings now contain literal LaTeX rather than descriptive placeholders; all 15 C marks are accounted for.')
(ROOT/'editor'/f'{stem}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(ROOT/'pages'/f'{stem}.tex').write_text(page)
print(json.dumps({'rows':sum(bool(r.get('change_C') or r.get('change_H')) for r in d['changes']), 'C':sum(bool(r.get('change_C')) for r in d['changes']), 'H':sum(bool(r.get('change_H')) for r in d['changes']), 'inventory':len(d['inventory'])}))
