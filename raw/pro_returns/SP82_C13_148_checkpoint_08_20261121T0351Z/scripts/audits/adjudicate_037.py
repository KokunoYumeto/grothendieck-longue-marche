#!/usr/bin/env python3
"""Read-only scan037 mechanical scaffold, pending completed root decisions.

Maps all 31 comparison boxes (26 DIFF) to the page, existing C/H rows, MARKS,
doubts, inventory, notes and difference records. It does not inspect images,
read root's unfinished working file, choose readings, modify a review/page,
write adjudications, run TeX/OCR/research, record an audit, or rebuild outputs.

Run normally for a compact validation report, or --json for the complete map.
There is deliberately no apply mode. After root finishes, two ownership groups
must be reconciled before applying the 24 disjoint differing page units:
  * pair_inserted and pair_coordinates share one baseline/interlinear owner;
  * mu_membership is a projection of mu_parameter, including its comma.
Five display extracts use synthetic inline delimiters; preserve the actual
display wrappers. The 28 excluded background MARKS and two exclusion C/H rows
have no comparison boxes and must not be reintroduced as source text.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

B = Path(__file__).resolve().parents[2]
PACKET = B.parent/'packets/148_scan037'
PAIR_OWNER = '037_pair_group'
MU_OWNER = '148037_mu_parameter'
EXPECTED_HASHES = {
    'second/148_scan037_first.tsv': '95282378a6a4c308030ab1eea91b822e017df07aaa3c8fe5cbcef45d6f2be31f',
    'second/148_scan037_second.tsv': '9204a4805d6e4432aaff7f6e132ba2d86ea3c87c571be7baa8c042ff7561fb30',
    'second/148_scan037_boxes.tsv': '8ddb3d752fd92f415a89f84ec573732b6d97dae41ce0eedf6863ea88c58da71b',
    'second/148_scan037_comparison.tsv': 'c96b9de9805027944abbb660d4700c274c26db8df0056e3cbe794cb63575c4f1',
    'second/148_scan037_token_differences.tsv': 'df44bb79825cbc3e36f71f65927a9861744deb3e9547cc361d39d28e3f35e770',
    'pages/148_scan037.tex': 'ef95626ab9feb62afcc1beb90074856ac0d9110bd699eb04d3448952ab9ccc34',
    'reviews/148_scan037.json': '9782050ca569c5a13f4cecaf7f6a92ab1791bf82194404ccbf67198f37097442',
}

# Repeated links identify existing shared review rows, not extra correction rows.
CHANGE_LINKS = {
    '148037_folio': [0],
    '148037_opening': [1],
    '148037_lambda_whole': [2],
    '148037_iso': [3],
    '148037_underlined_word': [4],
    '148037_unique': [5],
    '148037_condition': [6],
    '148037_lambda_minus4': [],
    '148037_lambda_prime_whole': [7,8,9,10],
    '148037_basis_line': [11,12],
    '148037_basis_fourth_power': [13],
    '148037_donnant': [14],
    '148037_basis_square': [14],
    '148037_pair_inserted': [15],
    '148037_pair_coordinates': [15],
    '148037_product_transition': [16],
    '148037_mu_parameter': [16,17,18],
    '148037_mu_membership': [17,18],
    '148037_mu_nondegeneracy': [19],
    '148037_quadratic': [],
    '148037_distinctness_formula': [20],
    '148037_sexprime': [21],
    '148037_inserted2': [],
    '148037_nonzero': [22],
    '148037_product1': [22],
    '148037_cancelled_Les': [],
    '148037_On_recupere': [23],
    '148037_lens_des': [24],
    '148037_quartic': [],
    '148037_radicals': [25,26],
    '148037_muprime_margin': [27],
}
CHANGE_NAMES = [
    'top-left foliation','opening words','first display, cancelled fraction',
    'isomorphism phrase','short underlined word after iso.','unique près',
    'condition wording','definition display, prime','definition display, annotation above equals',
    'definition display, retouched 2','definition display, final punctuation',
    'basis paragraph, En termes','basis paragraph, tentative cancelled de',
    'basis formula, fourth power','basis sentence, donnant','pair insertion and baseline par',
    'parameter transition','parameter, raised membership insertion','parameter, comma before satisfaisant',
    'recovery of xi0 and eta0','distinctness formula, bent underline','distinctness sentence',
    'nonzero-root parenthesis','On récupère','baseline l’ens des',
    'first radical, closing parenthesis at page edge','radical display, final point',
    'mu-prime margin, curved enclosing stroke','pale reversed listing, first witness block',
    'pale reversed listing, remaining witness block',
]
MARK_LINKS = {
    '148037_lambda_prime_whole': ['M0467','M0468','M0469'],
    '148037_distinctness_formula': ['M0470'],
}
DOUBT_LINKS = {
    '148037_lambda_whole': [0],
    '148037_underlined_word': [1],
    '148037_lambda_prime_whole': [2],
    '148037_basis_line': [3],
    '148037_distinctness_formula': [4],
    '148037_cancelled_Les': [5],
    '148037_radicals': [6],
}
INVENTORY_LINKS = {
    '148037_folio': ['foliation'],
    '148037_opening': ['opening'],
    '148037_lambda_whole': ['lambda_display','cancelled_fraction'],
    '148037_iso': ['recover_situation'],
    '148037_underlined_word': ['short_underlined_word'],
    '148037_unique': ['unique_underline'],
    '148037_condition': ['recover_situation'],
    '148037_lambda_minus4': ['recover_situation'],
    '148037_lambda_prime_whole': ['lambda_prime_display'],
    '148037_basis_line': ['basis','cancelled_de'],
    '148037_basis_fourth_power': ['basis'],
    '148037_donnant': ['basis'],
    '148037_basis_square': ['basis'],
    '148037_pair_inserted': ['pair'],
    '148037_pair_coordinates': ['pair','parameter'],
    '148037_product_transition': ['parameter'],
    '148037_mu_parameter': ['parameter','parameter_membership'],
    '148037_mu_membership': ['parameter_membership'],
    '148037_mu_nondegeneracy': ['parameter'],
    '148037_quadratic': ['quadratic'],
    '148037_distinctness_formula': ['distinctness_sentence','distinctness_underline'],
    '148037_sexprime': ['distinctness_sentence'],
    '148037_inserted2': ['inserted_two'],
    '148037_nonzero': ['nonzero_parenthesis'],
    '148037_product1': ['nonzero_parenthesis'],
    '148037_cancelled_Les': ['cancelled_Les'],
    '148037_On_recupere': ['recover_I'],
    '148037_lens_des': ['recover_I'],
    '148037_quartic': ['quartic'],
    '148037_radicals': ['radicals'],
    '148037_muprime_margin': ['muprime_note','muprime_enclosure'],
}
NOTE_LINKS = {
    '148037_folio': ['148037_N01'],
    '148037_opening': ['148037_C01'],
    '148037_lambda_whole': ['148037_C01','148037_N02'],
    '148037_iso': ['148037_C01'],
    '148037_underlined_word': ['148037_C01','148037_N02'],
    '148037_unique': ['148037_C01'],
    '148037_condition': ['148037_C01'],
    '148037_lambda_minus4': ['148037_C01'],
    '148037_lambda_prime_whole': ['148037_C01'],
    '148037_basis_line': ['148037_C02','148037_N02'],
    '148037_basis_fourth_power': ['148037_C02'],
    '148037_donnant': ['148037_C02'],
    '148037_basis_square': ['148037_C02'],
    '148037_pair_inserted': ['148037_C02'],
    '148037_pair_coordinates': ['148037_C02'],
    '148037_product_transition': ['148037_C02'],
    '148037_mu_parameter': ['148037_C02','148037_C03'],
    '148037_mu_membership': ['148037_C02'],
    '148037_mu_nondegeneracy': ['148037_C03'],
    '148037_quadratic': ['148037_C03'],
    '148037_distinctness_formula': ['148037_C03','148037_N02'],
    '148037_sexprime': ['148037_C03'],
    '148037_inserted2': ['148037_C03'],
    '148037_nonzero': ['148037_C03'],
    '148037_product1': ['148037_C03'],
    '148037_cancelled_Les': ['148037_N02'],
    '148037_On_recupere': ['148037_C04'],
    '148037_lens_des': ['148037_C04'],
    '148037_quartic': ['148037_C04'],
    '148037_radicals': ['148037_C05'],
    '148037_muprime_margin': ['148037_C05','148037_N01'],
}
DIFFERENCE_LINKS = {
    '148037_folio': [709,710,711],
    '148037_opening': [712],
    '148037_lambda_whole': [713,714],
    '148037_iso': [715],
    '148037_underlined_word': [716],
    '148037_unique': [716],
    '148037_condition': [717],
    '148037_lambda_prime_whole': [718,719,720,721],
    '148037_basis_line': [722,723],
    '148037_basis_fourth_power': [724],
    '148037_donnant': [725],
    '148037_basis_square': [725],
    '148037_pair_inserted': [726,727],
    '148037_pair_coordinates': [726,727,728,729],
    '148037_product_transition': [730],
    '148037_mu_parameter': [730,731],
    '148037_mu_membership': [731],
    '148037_distinctness_formula': [732],
    '148037_sexprime': [733],
    '148037_nonzero': [734],
    '148037_product1': [734],
    '148037_lens_des': [735,736],
    '148037_radicals': [737,738,739],
    '148037_muprime_margin': [737,739,740],
}
DISPLAY_INDEX = {
    '148037_lambda_whole': 0,
    '148037_lambda_prime_whole': 1,
    '148037_quadratic': 2,
    '148037_quartic': 3,
    '148037_radicals': 4,
}
EXACT_TARGETS = {
    '148037_condition': 'La condition à mettre sur\n$\\lambda$',
    '148037_lambda_minus4': r'$\lambda-4\ne0$ i.e.',
    '148037_basis_line': r"En termes d'une base \deleted{\unsure{de}} $e_1$ de $L_1$,",
    '148037_basis_fourth_power': r'$e_1^4=e=\xi\wedge\eta$',
    '148037_basis_square': r'base $e_1^2$ de $L_2$',
    '148037_product_transition': r'$\xi_0\eta_0=1$, ou encore',
    '148037_mu_nondegeneracy': '$\\mu^2-4\\ne0$,\n$\\xi_0$ et $\\eta_0$ se récupérant comme',
    '148037_product1': 'car leur\nproduit est $1$).',
}
PAIR_BASELINE = 'par'
PAIR_COORDINATES = r'$\xi_0,\eta_0\in\mathbb C$ $(\xi=\xi_0e_1^2,\ \eta=\eta_0e_1^2)$,'
MU_TARGET = 'par\n$\\mu=\\xi_0+\\eta_0\\inserted{\\in\\mathbb C}$, satisfaisant'

CONTEXT_NOTES = {
    '148037_lambda_whole': 'The first extraction uses synthetic inline math; the current page has a multiline display. Replace only the approved display body, retaining its one wrapper.',
    '148037_lambda_prime_whole': 'The second adds def and a raised +|4 after the first2; root must decide all letters, layering and placement. Its inline delimiters must not be pasted into the existing display.',
    '148037_basis_fourth_power': 'The second includes the following comma, which lies outside this first target. Do not duplicate or remove that comma from an extraction-only difference.',
    '148037_basis_square': 'The second includes the following comma; the first target excludes it. The existing donnant C/H row spans the agreed donnant box and this box’s initial base.',
    '148037_pair_inserted': 'This insertion is inside one canonical pair owner. The first retains la; root must decide the article and abbreviation. Do not insert another baseline par.',
    '148037_pair_coordinates': 'The initial par is before the interlinear insertion in the page. This extraction is noncontiguous: par plus the coordinate line, omitting the insertion between them.',
    '148037_product_transition': 'The first ends at ou encore; the following par belongs to the mu_parameter target. The existing transition C/H row spans both targets.',
    '148037_mu_parameter': 'The raised membership and following comma are also extracted in mu_membership. There is only one insertion and one comma in the canonical parameter owner.',
    '148037_mu_membership': 'Synthetic outer math delimiters differ from the inline insertion. Project the insertion and baseline comma from mu_parameter; do not write another membership formula.',
    '148037_quadratic': 'The page comma is inside the display while the first synthetic inline extraction puts it after the math delimiter; keep one comma.',
    '148037_distinctness_formula': 'The current inline TikZ owns the complete comparison, bent underline and separate right stroke. Any revised geometry must remain one owner and use root instructions; do not infer geometry from text.',
    '148037_inserted2': 'The second contains additional drawn marks around the inserted2. The current page target is only the insertion; await root ownership/geometry instructions before extending it.',
    '148037_nonzero': 'The first target includes an opening parenthesis absent from the second extraction. The existing nonzero C/H row also includes car, owned by the next product1 box.',
    '148037_product1': 'The current page wraps between leur and produit. Keep the existing closing parenthesis and point once, and synchronize the shared nonzero C/H row.',
    '148037_cancelled_Les': 'No existing C/H row covers the certainty-only difference. Add no row solely for resolving or broadening a doubt.',
    '148037_radicals': 'Two forms share one displayed equality. Preserve root-directed edge punctuation and delimiter visibility; the current invisible delimiter deliberately avoids supplying an unread closing parenthesis.',
    '148037_muprime_margin': 'The first owns a single margin wrapper, text nodes and enclosing curve. The second uses a nested figure wrapper. Root must choose geometry; differences row740 also references already excluded background text.',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_pins():
    for relative, expected in EXPECTED_HASHES.items():
        assert digest(B/relative) == expected, relative


def tsv(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def unique_span(text, target):
    assert target and text.count(target) == 1, (target[:100],text.count(target))
    start = text.index(target)
    return [start,start+len(target)]


def normalized_extraction(text):
    """Check only wrapper/whitespace equivalence; never used to select ink."""
    for delimiter in (r'\(',r'\)',r'\[',r'\]','$'):
        text = text.replace(delimiter,'')
    return re.sub(r'\s+','',text)


def require_completed_root_decisions(comparison, entries):
    """Future gate only; this scaffold never opens the root working file."""
    wanted = {row['box'] for row in comparison if row['different'] == 'yes'}
    assert len(entries) == 26 and len({row['box'] for row in entries}) == 26
    assert {row['box'] for row in entries} == wanted
    assert all(row.get('viewed_by_main') is True for row in entries)
    assert all(row.get('choice') in ('first','second','revised') for row in entries)
    assert all(row.get('ink') and row.get('confidence') for row in entries)
    return True


def build_map():
    verify_pins()
    page = (B/'pages/148_scan037.tex').read_text(encoding='utf-8')
    review = json.loads((B/'reviews/148_scan037.json').read_text(encoding='utf-8'))
    comparison = tsv(B/'second/148_scan037_comparison.tsv')
    rectangle_rows = tsv(B/'second/148_scan037_boxes.tsv')
    packet_marks = {row['id']: row for row in tsv(PACKET/'marks.tsv')}
    comp = {row['box']: row for row in comparison}
    rectangles = {row['box']: row for row in rectangle_rows}
    assert len(comparison) == len(rectangles) == 31
    assert sum(row['different']=='yes' for row in comparison) == 26
    assert list(comp) == list(rectangles)
    assert set(comp) == set(CHANGE_LINKS) == set(INVENTORY_LINKS) == set(NOTE_LINKS)
    assert [row['place'] for row in review['changes']] == CHANGE_NAMES
    assert {i for values in CHANGE_LINKS.values() for i in values} == set(range(28))
    assert len(review['changes']) == 30 and len(review['decisions']) == 32
    assert len(review['unresolved']) == 7 and len(review['inventory']) == 24
    assert {i for values in DOUBT_LINKS.values() for i in values} == set(range(7))
    inventory = {row['element']: i for i,row in enumerate(review['inventory'])}
    assert set(inventory) == {name for values in INVENTORY_LINKS.values() for name in values}
    notes = {row['id']: i for i,row in enumerate(review['notes'])}
    assert set(notes) == {name for values in NOTE_LINKS.values() for name in values}
    differences = {row['source_row']: i for i,row in enumerate(review['differences_review'])}
    assert set(differences) == {number for values in DIFFERENCE_LINKS.values() for number in values}
    decisions = {row['id']: i for i,row in enumerate(review['decisions'])}
    assert set(decisions) == set(packet_marks) == {f'M{i:04}' for i in range(467,499)}

    # Extract the actual display bodies and offsets without normalizing the page.
    displays = list(re.finditer(r'\\\[\n([\s\S]*?)\n\\\]',page))
    assert len(displays) == 5
    units = {}
    source_projections = {}
    box_owner = {}
    projection_parts = {}
    pair_text = PAIR_BASELINE+' '+comp['148037_pair_inserted']['first']+'\n'+PAIR_COORDINATES
    pair_span = unique_span(page,pair_text)
    units[PAIR_OWNER] = dict(owner=PAIR_OWNER, boxes=['148037_pair_inserted','148037_pair_coordinates'],
        page_span=pair_span, target_text=pair_text, mode='one baseline/interlinear owner',
        page_write=True, future_instruction='Build one approved group and derive both excerpts; baseline par appears once.')
    mu_span = unique_span(page,MU_TARGET)
    units[MU_OWNER] = dict(owner=MU_OWNER, boxes=[MU_OWNER,'148037_mu_membership'],
        page_span=mu_span,target_text=MU_TARGET,mode='parameter owner with aliased membership',
        page_write=True,future_instruction='Build one parameter result and derive the membership plus comma projection.')
    for key in ('148037_pair_inserted','148037_pair_coordinates'):
        box_owner[key] = PAIR_OWNER
    box_owner[MU_OWNER] = box_owner['148037_mu_membership'] = MU_OWNER
    pair_insertion = comp['148037_pair_inserted']['first']
    source_projections['148037_pair_inserted'] = pair_insertion
    source_projections['148037_pair_coordinates'] = 'par '+PAIR_COORDINATES
    projection_parts['148037_pair_inserted'] = [unique_span(page,pair_insertion)]
    projection_parts['148037_pair_coordinates'] = [
        [pair_span[0],pair_span[0]+len(PAIR_BASELINE)],unique_span(page,PAIR_COORDINATES)]
    source_projections[MU_OWNER] = MU_TARGET
    membership = r'\inserted{\in\mathbb C}'
    source_projections['148037_mu_membership'] = membership+','
    membership_span = unique_span(page,membership)
    comma_position = membership_span[1]+1
    assert page[membership_span[1]:comma_position+1] == '$,'
    projection_parts[MU_OWNER] = [mu_span]
    projection_parts['148037_mu_membership'] = [membership_span,[comma_position,comma_position+1]]
    for row in comparison:
        key = row['box']
        if key in box_owner:
            continue
        if key in DISPLAY_INDEX:
            match = displays[DISPLAY_INDEX[key]]
            raw = match.group(1)
            left_trim = len(raw)-len(raw.lstrip())
            body = raw.strip()
            span = [match.start(1)+left_trim,match.start(1)+left_trim+len(body)]
            mode = 'body inside existing display wrapper'
            instruction = 'Replace only the root-approved body and retain the existing single display wrapper.'
        else:
            body = EXACT_TARGETS.get(key,row['first'])
            span = unique_span(page,body)
            mode = 'exact source span'
            instruction = 'Keep surrounding context outside this span unless root explicitly extends it.'
        assert page[span[0]:span[1]] == body
        units[key] = dict(owner=key,boxes=[key],page_span=span,target_text=body,
            mode=mode,page_write=row['different']=='yes',future_instruction=instruction)
        box_owner[key] = key
        source_projections[key] = body
        projection_parts[key] = [span]
    assert len(units) == 29
    for key in comp:
        assert normalized_extraction(source_projections[key]) == normalized_extraction(comp[key]['first']), key
    sorted_units = sorted(units.values(),key=lambda row: row['page_span'][0])
    assert all(a['page_span'][1] <= b['page_span'][0] for a,b in zip(sorted_units,sorted_units[1:]))
    schedule = [row for row in sorted_units if row['page_write']]
    assert len(schedule) == 24
    assert page.count(membership) == 1
    assert pair_text.count('par ') == 1 and pair_text.count(pair_insertion) == 1

    rows = []
    for item in comparison:
        key = item['box']
        rectangle = rectangles[key]
        row = dict(box=key,different=item['different'],
            original_rectangle=[int(rectangle[x]) for x in ('x0','y0','x1','y1')],
            owner=box_owner[key],page_write=False if key in ('148037_pair_inserted','148037_pair_coordinates','148037_mu_membership') else item['different']=='yes',
            page_write_note='The owner schedule controls mutations; a projection must never be independently pasted.',
            source_projection=source_projections[key],projection_parts=projection_parts[key],
            first_extract=item['first'],context_note=CONTEXT_NOTES.get(key),
            existing_changes=[dict(index=i,**review['changes'][i]) for i in CHANGE_LINKS[key]],
            marks=[dict(id=name,review_index=decisions[name],
                current_decision=review['decisions'][decisions[name]]['decision'],
                current_reading=review['decisions'][decisions[name]]['reading'],
                source_row=packet_marks[name]['source_row'],
                source_mark=packet_marks[name]['the mark as written']) for name in MARK_LINKS.get(key,[])],
            doubts=[dict(index=i,**review['unresolved'][i]) for i in DOUBT_LINKS.get(key,[])],
            inventory=[dict(index=inventory[name],element=name) for name in INVENTORY_LINKS[key]],
            notes=[dict(index=notes[name],id=name) for name in NOTE_LINKS[key]],
            difference_records=[dict(index=differences[number],source_row=number)
                                for number in DIFFERENCE_LINKS.get(key,[])])
        rows.append(row)
    excluded_marks = [name for name in decisions if name not in {m for v in MARK_LINKS.values() for m in v}]
    assert len(excluded_marks) == 28
    assert all(review['decisions'][decisions[name]]['reading'] == '' for name in excluded_marks)
    assert all(review['changes'][i]['final'] == '' for i in (28,29))
    verify_pins()
    return dict(status='read-only scaffold; root decisions not read or applied',scan=37,
        total_boxes=31,differing_boxes=26,agreed_boxes=[row['box'] for row in comparison if row['different']=='no'],
        existing_review_counts=dict(changes=30,marks=32,doubts=7,inventory=24,notes=7,checks=6),
        front_change_rows_mapped=28,excluded_background_change_rows=2,
        front_marks_mapped=4,excluded_background_marks=28,
        page_units=29,differing_page_write_units=24,
        ownership_groups=[units[PAIR_OWNER],units[MU_OWNER]],
        disjoint_future_write_schedule=schedule,boxes=rows,
        preserved_unboxed_records=dict(
            instruction='Existing exclusions only, not new ink judgments. No matching fixed comparison box; preserve unless root explicitly directs otherwise.',
            changes=[dict(index=i,**review['changes'][i]) for i in (28,29)],
            marks=[dict(index=decisions[name],**review['decisions'][decisions[name]]) for name in excluded_marks]),
        shared_review_rows={str(i):[key for key,values in CHANGE_LINKS.items() if i in values]
                            for i in range(28) if sum(i in values for values in CHANGE_LINKS.values())>1},
        pinned_hashes=EXPECTED_HASHES,root_working_file_read=False,images_read=False,
        page_or_review_written=False,shared_outputs_touched=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true',help='Print the complete read-only map.')
    args = parser.parse_args()
    report = build_map()
    if not args.json:
        report = {key:report[key] for key in (
            'status','scan','total_boxes','differing_boxes','agreed_boxes','existing_review_counts',
            'front_change_rows_mapped','excluded_background_change_rows','front_marks_mapped',
            'excluded_background_marks','page_units','differing_page_write_units',
            'shared_review_rows','root_working_file_read','images_read',
            'page_or_review_written','shared_outputs_touched')}
    print(json.dumps(report,ensure_ascii=False,indent=2 if args.json else None))


if __name__ == '__main__':
    main()
