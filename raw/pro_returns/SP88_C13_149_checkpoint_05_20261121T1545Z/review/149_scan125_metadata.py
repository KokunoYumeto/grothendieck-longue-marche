"""Frozen first-reader return for assigned page 149_scan125; no proof audit."""
from pathlib import Path
import csv
import importlib.util
import json

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan125'
spec = importlib.util.spec_from_file_location('crop125', ROOT / f'edition/review/{PAGE}_crop.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
CROPS = module.CROPS

def change(id, crop, place, C, H, final, evidence, confidence='high',
           vs_C=False, vs_H=True, kind='misread word', error_category='Words',
           H_marked=False, consequential=False):
    return dict(id=id, place=place, C=C, H=H, final=final, evidence=evidence,
                crop=f'crops/{PAGE}_{crop}.png', bbox=CROPS[crop]['bbox'],
                confidence=confidence, vs_C=vs_C, vs_H=vs_H, kind=kind,
                error_category=error_category, H_marked=H_marked,
                consequential=consequential)

changes = [
    change('p01', 'p01', 'Main line 1, initial fragment', 'rait', '-rait', 'rait',
           'The first ink is the small r entry stroke, followed by a, dotted i and crossed t. The blank immediately to its left has no hyphen. The fragment is retained without completing the word.',
           kind='text not on the page', error_category='Text that is not on the page'),
    change('p02', 'p02', 'Main line 2, first word', 'construire', 'la construction', 'construire',
           'The c/o opening, short n/s strokes, crossed tall t, low r/u strokes and separated dotted i lead to the terminal r/e trace. No preceding la or terminal -ction is written.'),
    change('p03', 'p03', 'Main line 3, after à l’aide des', 'pts', r'p\supplied{oin}ts', 'pts',
           'The short form has a descending p, tall t and small terminal s-like curve, with no letters oin between the p and t and no following stop.',
           kind='abbreviation expanded or spelling modernised',
           error_category='Abbreviations expanded, spelling modernised'),
    change('p04', 'p04', 'Main lines 4–5, quotation around variété de Riemann',
           "``variété de Riemann''", '« variété de Riemann »', "``variété de Riemann''",
           'Two small raised strokes stand before variété, and another pair follows Riemann. They are paired quotation strokes rather than lateral chevrons. The detached accent on variété is present. The neighbouring ornate X is a live symbol, not a cancelled word.',
           kind='other', error_category='Other'),
    change('p05', 'p05', 'Main line 6, initial word', 'Composant', 'Comparant', 'Composant',
           'After capital C and the low om trace comes a descending p, a small o-like dot/curve, an s-shaped short stroke, then a low a/n run and a raised triangular terminal t. The middle does not show the ar sequence of Comparant.',
           consequential=True),
    change('p06a', 'p06', 'Main line 7, complete first L expression and its raised sign',
           r'L_1^{\unsure{k|*}}', r'L_1', r'L_1^{\unsure{k|*}}',
           'The L and separate lower 1 are plain. A real small raised sign at the upper right has a slender upright and short branching strokes with a curved lower-right exit. Its k-shaped outline is preferred, but the joined strokes do not securely exclude an asterisk. The whole L expression and neighbouring de K de degre de tr. 1, avec were inspected; no meaning is inferred from the marginal note.',
           confidence='low', kind='omission', error_category='Omissions'),
    change('p06b', 'p06', 'Main line 7, word before de tr. 1', 'degré', 'degré', 'degre',
           'The initial d has its tall upright and the g has a descending loop. The r/e ending is a connected low trace, and the space above it contains no detached accent. The whole word and its upper space lie within the existing p06 crop. The following tr. has a separate dark stop and is retained with it.',
           vs_C=True, kind='abbreviation expanded or spelling modernised',
           error_category='Abbreviations expanded, spelling modernised'),
    change('p07', 'p07', 'Main line 8, abbreviation before the complete group map',
           "l'hom", "l'hom.", "l'hom",
           'After the low final m trace there is blank space before the first E, with no separate point. The visible apostrophe belongs to l’. Both arrow ends were examined: a plain entry to the single shaft at left and a two-arm arrowhead at right. Source L and target L_1 remain distinct.',
           kind='text not on the page', error_category='Text that is not on the page'),
    change('p08', 'p08', 'Main line 10 and its raised addition, after un moyen de',
           r'construire des \inserted{germes de} sections',
           r'construction des \add{germes de} sections',
           r'construire des \inserted{germes de} sections',
           'The word again ends with the dotted i and short r/e strokes rather than -ction. Germes de is a separate raised baseline. Its long curved leader begins between des and sections, sweeps above sections, and ends to the right; it supplies neither an opening parenthesis nor an underline. The y descender in moyen on the line above is separate from that leader.'),
    change('p09', 'p15', 'Main line 11, le fait intéressant sera',
           'le fait intéressant sera', 'le test intéressant serait', 'le fait intéressant sera',
           'The first differing word starts with a tall f-like stroke crossing the low a/i run and ends in a tall t, supporting fait. The final word has a short s/e/r/a trace and no additional i dot or tall crossed t after it. The original p09 crop was inspected; p15 is a declared contextual repair including the complete initial E_K, whose lower K had touched the first crop edge. No reading was changed by the repair.'),
    change('p11', 'p11', 'Main line 14, quoted places',
           "``places''", '« places »', "``places''",
           'Each end of places carries two small raised strokes. Neither pair forms guillemets. The neighbouring complete L_1 sur K. has its lower 1 and final stop.',
           kind='other', error_category='Other'),
    change('p12', 'p12', 'Lower-left slanted margin, all four baselines',
           r'on pense ici au cas où $K$ est de type fini sur $\mathbf Q$, bien sûr !',
           r'\uncertain{on pourrait ici} $K = \mathbb{Q}$, \uncertain{au cas fini} \uncertain{typique} !',
           r'on pense ici au cas où $K$ est de type fini sur $\mathbf Q$, bien sûr !',
           'The first row reads on pense ici: the p stem is followed by a compact ense trace, and ici has two dots. The second reads au cas où K est, with an accent above où and a low word trace est after K, rather than equality bars. The third is de type fini sur Q, with the final comma; the fourth is bien sûr !, with a detached circumflex and separate exclamation point. Q has reinforced left/interior strokes and a crossing lower tail, but this does not establish a distinct bold versus double-struck alphabet: the existing C macro is retained and the font-macro difference is not counted.',
           H_marked=True, consequential=True),
    change('p14', 'p14', 'Lower-left thin foliation', r'\margin{124}', '[absent]', r'\margin{124}',
           'Three thin digits show a high-slant 1, a curved 2 with lower foot, and an open angular 4. The lower marginal 124 is separate from the dark author number 62 at the head.',
           kind='omission', error_category='Omissions'),
]

top_reading = r"""rait un principe général pour construire des germes de sections de $\mathcal E_L$ sur $\mathcal E_K$ --- à l'aide des pts de dim 0 de la ``variété de Riemann'' $\mathfrak X$ de $L$ sur $K$. Composant, pour une sous-extension $L_1^{\unsure{k|*}}$ de $K$ de degre de tr. 1, avec l'hom $\mathcal E_L\longrightarrow\mathcal E_{L_1}$, on a"""
lower_reading = r"""donc aussi un moyen de construire des \inserted{germes de} sections de $\mathcal E_{L_1}$ sur $\mathcal E_K$, et le fait intéressant sera de voir si on \inserted{en} trouve pas plus que les sections déjà envisagées, associées aux ``places'' de $L_1$ sur $K$.
\margin{on pense ici au cas où $K$ est de type fini sur $\mathbf Q$, bien sûr !}

Mais il en est bien ainsi, comme on voit en considérant $V_1=V\cap L_1$, qui est un anneau de valuation de $L_1$,
\margin{124}"""

data = {
    'page': PAGE, 'scan': 125, 'reader': 'reader_b',
    'line_count': 25,
    'line_count_detail': {'main': 17, 'diagram': 0, 'margin': 4, 'insertion': 2, 'standalone_numbers': 2},
    'changes': changes,
    'decisions': [{
        'id': 'M0140', 'cote': '149', 'scan': '125', 'decision': 'undecided',
        'reading': r'\unsure{k|*}',
        'evidence': 'The raised sign is real and separate from the lower index 1. A slender stem and compact branches make k the preferred outline, but their joined central ink does not securely separate k from an asterisk. The complete expression L_1 and its raised sign, plus the adjacent field and degree context, were inspected in p06; the marginal note is not used to decide the glyph.',
        'crop': f'crops/{PAGE}_p06.png', 'bbox': CROPS['p06']['bbox'], 'confidence': 'low',
    }],
    'inventory': [
        {'sheet_kind': 'text', 'hand': 'his hand, dark ink', 'element': 'e01', 'kind': 'text', 'position': 'Head, separate number above the first main baseline', 'first_words_or_objects': '62', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e02', 'kind': 'text', 'position': 'Main lines 1–14', 'first_words_or_objects': 'rait un principe général pour', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e03', 'kind': 'insertion', 'position': 'Raised between main lines 9 and 10; leader joins before sections on line 10', 'first_words_or_objects': 'germes de', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e04', 'kind': 'insertion', 'position': 'Raised above main line 12; leader joins between on and trouve', 'first_words_or_objects': 'en', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand', 'element': 'e05', 'kind': 'margin note', 'position': 'Lower-left slanted margin beside the end of the first paragraph, four baselines', 'first_words_or_objects': 'on pense ici', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'his hand, darker ink', 'element': 'e06', 'kind': 'text', 'position': 'Main lines 15–17', 'first_words_or_objects': 'Mais il en est bien ainsi, comme', 'transcribed': 'yes'},
        {'sheet_kind': 'text', 'hand': 'thin foliation hand, distinct from the author number', 'element': 'e07', 'kind': 'margin note', 'position': 'Bottom-left corner', 'first_words_or_objects': '124', 'transcribed': 'yes'},
    ],
    'doubts': [{
        'place': 'Main line 7, raised sign on the first L_1',
        'reading': r'L_1^{\unsure{k|*}}', 'alternatives': 'k; *', 'confidence': 'low',
    }],
    'audit_boxes': [
        {'box': 'b01', 'kind': 'handwritten number', 'bbox': CROPS['p13']['bbox'], 'reading': r'\mspage{62}'},
        {'box': 'b02', 'kind': 'handwritten number; doubtful formula; C/H word difference', 'bbox': [295, 85, 1645, 1065], 'reading': top_reading},
        {'box': 'b03', 'kind': 'insertion; margin note; handwritten number; C/H word difference', 'bbox': [20, 1070, 1650, 2340], 'reading': lower_reading},
    ],
    'notes': [
        'The page continues a discussion of constructing germs of sections from dimension-0 points of the Riemann variety of L over K. It then considers composition for a subextension of transcendence degree 1 and starts the statement about V_1=V intersect L_1. This is a content description, not verification of the section argument.',
        'Initial rait is a literal continuation fragment with no preceding hyphen. No missing part of that word is supplied. Both occurrences of construire, Composant, le fait and sera are supported by the inspected strokes.',
        'The written word is degre without a detached accent above its r/e ending. Both witnesses give degré; the change is recorded at p06b using the already inspected p06 crop, without further enlargement. The separate stop after tr is present.',
        'Germes de is a raised insertion attached between des and sections by one continuous curved leader. The leader is not transcribed as a parenthesis or underline. The descender of moyen above is independently traceable.',
        'The raised en attaches between on and trouve. The literal sequence on en trouve pas is preserved; no ne is substituted to repair its grammar. The curved attachment stroke is not punctuation. Pas, uncertain in H, is supported by the descending p and low terminal stroke in p10; a certainty-only difference is not a separate collation correction.',
        'The superscript on the first L_1 remains k|*. Its presence and placement are clear; its letter/symbol identity and function are not settled. No matching call sign is confidently identified at the beginning of the margin note, and no footnote function is inferred.',
        'The four marginal baselines are on pense ici / au cas où K est / de type fini sur Q, / bien sûr !. The comma after Q, accent over où, circumflex over sûr, and exclamation point are visible. The margin has no independent deletion or insertion leader to the raised L_1 sign.',
        'Q has reinforced left/interior strokes and a lower crossing tail. These strokes do not decide a bold versus double-struck typographic alphabet. C’s existing mathbf Q macro is retained; its font difference from H’s mathbb Q is not counted. The lexical difference between finite type over Q and H’s K=Q wording is counted separately as part of the marginal passage.',
        'Both quoted phrases have ordinary paired raised quotation strokes. The ornate X in the first paragraph is live mathematical notation; its horizontal and looped strokes are not treated as cancellation. No struck passage was found after checking the full text, both raised insertions and the margin separately.',
        'The complete short group map has one plain shaft and a right arrowhead. Both source and target subscripts were read. All handwritten digits are covered by the audit regions: author62, dim0, each L_1, degree1, V_1, and folio124.',
        'The all-logical-line count is25:17 main baselines,4 slanted marginal baselines,2 raised insertion baselines, and2 spatially separate numbering elements. Ordinary superscripts and subscripts are counted with their containing main line.',
        'Audit b02 contains all eight upper main baselines, including the complete doubtful L expression and every word of its context. Audit b03 contains all remaining main baselines, both insertions, the entire intersecting marginal note and the thin foliation. Broad contiguous boxes avoid cutting the interleaved writing; their reading fields contain the complete manuscript text in those boxes.',
        'Fifteen crops were saved and visually inspected. P15 is the sole declared contextual repair: p09 clipped the lower edge of the neighbouring K in E_K, while p15 includes the complete two-line context. The original crop remains; the repair did not revise a settled reading.',
        'The first attempted combined whole-page return was truncated before an image was available. The whole image was then returned alone and visually inspected once. Each native half was inspected once; the saved crops were then inspected individually. No OCR, external sources, other page content, TeX compilation or independent audit was used.',
        'No mathematical proof check was performed by this reader. The parent reader will record any separately conducted limited check; the paleographical reading does not certify the asserted construction of sections.',
    ],
    'checks': [],
    'hand_observations': [
        {'habit': 'Compact low cursive letter sequences can conceal the endings -uire, -ant and -a.', 'places': 'Main lines2,6,10,11; p02,p05,p08,p09/p15', 'holds': 'Both construire occurrences agree locally; Composant and sera are read from their own endings.', 'witness_errors': 'H gives construction twice, Comparant and serait.'},
        {'habit': 'A very small raised branching sign can resemble either k or an asterisk.', 'places': 'First L_1, main line7; p06', 'holds': 'One local occurrence only; its identity remains unresolved.', 'witness_errors': 'H omits the raised sign; C marks k|*.'},
        {'habit': 'Long curved insertion leaders can resemble a parenthesis or underline when detached from their attachment.', 'places': 'germes de above main line10 and en above main line12; p08,p10', 'holds': 'Both continuous leaders are traced to the insertion sites; neither supplies punctuation.', 'witness_errors': 'No separate punctuation error counted here.'},
        {'habit': 'The slanted note has compact low est and reinforced Q strokes.', 'places': 'Marginal lines2–3; p12', 'holds': 'The low trace after K is a word, not equality bars; Q font category is not decided.', 'witness_errors': 'H reads K=Q and replaces much of the surrounding note.'},
        {'habit': 'Written accent presence must be checked separately from conventional French spelling.', 'places': 'degre in main line7; variété in line4; où and sûr in the margin', 'holds': 'No detached accent over degre; accents are visible in the three compared words.', 'witness_errors': 'Both C and H supply an accent in degré.'},
    ],
    'notation': [
        {'written': r'\mathcal E_L\longrightarrow\mathcal E_{L_1}', 'meaning_or_use': 'The map called l’hom in the composition passage; a single right-pointing shaft is written.', 'places': 'Main line8; p07'},
        {'written': r'L_1^{\unsure{k|*}}', 'meaning_or_use': 'First written name of the subextension; the raised sign’s identity and function are unresolved.', 'places': 'Main line7; p06'},
        {'written': r'\mathfrak X', 'meaning_or_use': 'The ornate symbol attached to the quoted variété de Riemann of L over K.', 'places': 'Main line5; p04'},
        {'written': r'\mathbf Q', 'meaning_or_use': 'Field named after sur in the finite-type marginal qualification. The macro follows C; reinforced handwritten strokes do not decide bold versus double-struck alphabet.', 'places': 'Marginal line3; p12'},
        {'written': r'V_1=V\cap L_1', 'meaning_or_use': 'Written definition beginning the final paragraph’s valuation-ring assertion.', 'places': 'Main line16; auditb03'},
        {'written': 'dim 0; tr. 1', 'meaning_or_use': 'Numerical dimension and transcendence-degree qualifications written with digits.', 'places': 'Main lines4,7; p04,p06'},
    ],
    'abbreviations': [
        {'written': 'pts', 'expansion': 'points'},
        {'written': 'dim', 'expansion': 'dimension'},
        {'written': 'tr.', 'expansion': 'transcendance'},
        {'written': 'hom', 'expansion': 'homomorphisme'},
    ],
    'inspection': {
        'whole': True, 'halves': ['top', 'bottom'],
        'crops': [f'crops/{PAGE}_{name}.png' for name in CROPS],
        'deletions_insertions_checked': True,
        'whole_image_visual_inspections': 1,
        'native_half_visual_inspections': {'top': 1, 'bottom': 1},
        'contextual_repairs': [{'crop': f'crops/{PAGE}_p15.png', 'repairs': f'crops/{PAGE}_p09.png', 'reason': 'Complete contextual E_K was clipped at the lower edge of p09.'}],
    },
}

def main():
    expected_ids = {r['id'] for r in csv.DictReader((ROOT / f'packets/{PAGE}/marks.tsv').open(), delimiter='\t')}
    assert {r['id'] for r in data['decisions']} == expected_ids
    assert sum(data['line_count_detail'].values()) == data['line_count']
    for name, spec in CROPS.items():
        assert (ROOT / f'edition/crops/{PAGE}_{name}.png').exists()
        x0, y0, x1, y1 = spec['bbox']
        assert 0 <= x0 < x1 <= 1680 and 0 <= y0 < y1 <= 2360
    out = ROOT / f'edition/review/{PAGE}.json'
    if out.exists():
        raise FileExistsError(f'Refusing to overwrite completed metadata: {out}')
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{PAGE}: {len(changes)} places; {sum(x["vs_C"] for x in changes)} against C; {len(CROPS)} inspected crops; {len(data["doubts"])} open doubt; {data["line_count"]} logical lines')

if __name__ == '__main__':
    main()
