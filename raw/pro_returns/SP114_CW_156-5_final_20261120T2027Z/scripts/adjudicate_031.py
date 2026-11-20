from pathlib import Path
import argparse
import json

p = argparse.ArgumentParser()
p.add_argument('--utc', required=True)
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
x = json.loads((root / 'review/scan031_findings.json').read_text())
x['scan'] = 31
manifest = json.loads((root / 'review/scan031_crop_manifest.json').read_text())
t = (root / 'review/scan031_draft.tex').read_text()
(root / 'pages/J156-5-04_156-5_scan031.tex').write_text(t)
kind_map = {'symbol': 'misread symbol or index', 'state': 'deletion state (struck given live or live given struck)', 'punctuation': 'other', 'abbreviation': 'abbreviation expanded or spelling modernised', 'word': 'misread word', 'certainty': 'other'}
for c in x['changes']:
    c['crop'] = c.get('crop', '').removeprefix('deliverable/')
    c['kind'] = kind_map.get(c['kind'], c['kind'])
    c['main_decision'] = 'Accepted after main-reader inspection of the saved crop; unrecovered letters remain explicitly doubtful.'
    i = int(c['id'].split('-')[1])
    if i == 15:
        c['against_H'] = False
        c['main_decision'] = 'The tall looped l, low u shoulder and final dotted upright favor lui, as H reads. Keep le as a local alternative; do not supply grammatical linking words.'
    if i in (19, 27):
        c['against_C'] = False
        c['main_decision'] += ' Adding an alternative without changing the preferred C reading is not counted as a textual departure from C.'
    if i == 21:
        c['against_H'] = False
        c['certainty_only'] = True
    if i in (8, 14, 22, 30, 35):
        c['kind'] = 'readable ink left as `\\ill{}`'
    if i in (17, 20):
        c['kind'] = 'text not on the page'
    if i == 25:
        c['kind'] = 'insertion or placement'
    if i == 28:
        c['kind'] = 'insertion or placement'
    if i == 4:
        c['main_decision'] = 'No terminal stop is present. The upper equality stroke hooks down, but the same separate two-stroke form recurs in the b heading; retain = after local comparison, not by assuming the desired conclusion.'
    if i == 10:
        c['main_decision'] = 'A small pale aperture is enclosed by the thick raised diamond-like loop; no independent radial spokes distinguish an asterisk. Prefer circle but keep bullet and star alternatives.'
for z in x['inventory']:
    z['kind'] = {'number': 'text', 'text block': 'text', 'page_number': 'text', 'text_block': 'text', 'heading': 'text', 'margin': 'margin note'}.get(z['kind'], z['kind'])
    z['hand'] = 'his hand'
x['notes'] = [
    'The handwritten sheet number is 30. Part a) argues that the proposed F′ is a figure. It first computes its support and then separates the least-containing-element argument into x in |G|=|G′| and x outside |G|. Both cases end with the author’s “OK”; the second has an exclamation mark. Part b) replaces raffine with inserted subdivise and, after a cancelled attempt, restates a least-containing-element condition and an intersection-as-union-of-strata condition. No title or date appears.',
    'The support calculation was checked conditionally (031-check-01): if F′=G′∪(F\\setminus G), |G′|=|G| and |G|⊆|F|, then every point of |F| outside |G| belongs to some member of F that is not a member of G. Thus |F\\setminus G| contains |F|\\setminus|G|, and the displayed union has support |F|. These premises are carried from the stated construction; the calculation does not prove that F′ is a figure or verify every refinement axiom.',
    'The first case announces “prouvons A⊂B” but its terminal A carries a small thick raised mark, preferred as a circle with bullet/star alternatives. That mark is retained: the mathematical target does not license erasing it. No complete proof check of the least-element or stratum arguments is claimed. The two cancelled signs in b) are inverted A forms, ∀, rather than the word Soit.',
    'In the second case the ink favors “c’est lui plus petit él. de F”; le remains a glyph alternative, and no qui est is supplied to repair the syntax. The parenthesis physically follows él. de F and reads “et à fortiori de F\\setminus G”, followed by qui contient x. H’s cf. définition and its reordered qui est are not supported. Four compressed élément forms and seult remain doubtful rather than being expanded. The two de-like groups in the cancelled lower line are retained.',
    'The isolated support equality has a hooked upper stroke, initially suggestive of a superset with a bar. Its matching form in the b heading supports the reading =. The cancelled slanted addition a un plus petit belongs inside the cancelled block; its letter bodies and precise replacement extent are not fully recoverable. The final script R adjective is crossed and replaced above by fermé dans F′. All 19 C deletion scopes and 3 insertion scopes were checked; no independent margin note or diagram occurs.'
]
x['check_events'] = [{
    'statement_id': '031-check-01', 'type': 'targeted proof check',
    'outcome': 'Conditional support computation from the stated construction: assuming F′=G′∪(F\\setminus G), |G′|=|G|⊆|F|, a point in |F|\\setminus|G| lies in some A∈F and in no member of G, so A∉G and x∈|F\\setminus G|. Conversely |F\\setminus G|⊆|F|. Hence |F′|=|F|. Figurehood and refinement axioms were not established.'
}]
x['adjudicator'] = 'GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc'] = a.utc
(root / 'review/scan031_adjudicated.json').write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
with (root / 'review/main_image_reviews.tsv').open('a') as f:
    f.write('031\twhole source scan\tmain reader\tinspected once for layout before first adjudication\n')
    for c in manifest:
        f.write('031\t' + c['crop'].removeprefix('deliverable/') + '\tmain reader\tinspected before first adjudication\n')
rows = sum(bool(c.get('certainty_only') or c.get('against_C') or c.get('against_H')) for c in x['changes'])
with (root / 'progress.log').open('a') as f:
    f.write(f"scan 031 done {a.utc}: {x['line_count']} lines read, {len(manifest)} places cropped, {rows} rows\n")
print('Saved scan031, rows', rows)
