#!/usr/bin/env python3
"""Mechanical scan035 adjudication after root's 26 sealed crop decisions.

This module maps the 26 differing comparison boxes to the current page, C/H
review rows, packet MARKS, unresolved readings, and related local records.
The original read-only map is preserved below. The completed root working file
now supplies every reading and geometric choice; no new ink judgment is made.

Run normally for a dry run; --apply atomically writes only the page, local review,
and adjudication JSON. --map --json prints the original map before application.
After application use --verify-applied; do not rerun the non-idempotent main pass.
No images, OCR, research, TeX compilation, audit recording or shared rebuild.

Implemented ownership and preservation rules:
  1. Re-read the completed working file and require the exact DIFF box set.
  2. Resolve the canceled-block decisions into ONE canonical owner string.
     Its ten detail boxes are projections, not ten additional page replacements.
     The ne2 fragment in canceled_change aliases the parameter insertion.
  3. Reconcile any extra second-reader context explicitly with root's decisions;
     the second readings contain live text outside several first-target spans.
  4. Replace the 16 disjoint page units once; retain the existing shared graphic
     wrapper and lower-sphere scope unless root explicitly changes them.
  5. Derive detail adjudication finals and existing review-row finals from that
     same canonical result. Update MARKS/doubts/notes only as root directs.
  6. Preserve the five locked TSVs. No shared output or audit write belongs here.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import os
import re

B = Path(__file__).resolve().parents[2]
PACKET = B.parent / 'packets/148_scan035'
OWNER = '035_large_canceled_scope'
DETAILS = (
    '035_canceled_mu', '035_canceled_orbit', '035_canceled_J',
    '035_canceled_change', '035_canceled_parameter', '035_canceled_triple',
    '035_canceled_eliminer', '035_canceled_discriminant',
    '035_canceled_comme', '035_canceled_g',
)
FIGURES = ('035_figure_upper', '035_figure_lower')

# Pinned before any root adjudication was applied. The scaffold writes none of
# these files. A later implementation must deliberately refresh a changed page
# baseline rather than silently applying old substring targets to new content.
EXPECTED_HASHES = {
    'second/148_scan035_first.tsv': 'e27a02636bcf0ebdc15e452aee2028ab2840fa8d624c2d8a0cdd1ac582478566',
    'second/148_scan035_second.tsv': '9d67f0116e714f6484070a9a59cb44ad4514081d909d0f3f4d1ff924e729e57a',
    'second/148_scan035_boxes.tsv': 'bfd2b6037052966071b890bee8320c1bb1c68f05e2ba716d892c3af70cfcc193',
    'second/148_scan035_comparison.tsv': 'bd1bbfb1ccf7698e5d130bd3b244deba6a5332ccb6c7a14df353e19644a3c857',
    'second/148_scan035_token_differences.tsv': 'b6563b29109887b239cd84b551cf7ff8f92f6c2ce09e5201c873db6c2c8187b8',
    'pages/148_scan035.tex': '8aed36eefee3ad3b50e6eddc7e3516d56cc52e11533801b944c0439f206b0d1b',
    'reviews/148_scan035.json': '62df17cb660b69beeceae6d9b95170b8036c46187366fbee14520767e323b33a',
}

CHANGE_PLACES = {
    '035_heading_case': ['circled_case_4', 'canceled_opening_clause', 'initial_interlinear_insertion'],
    '035_first_kg': ['live_est_reunion'],
    '035_autom_universel': ['short_autom_abbreviation', 'canceled_de_after_autom', 'universel_quotation_marks'],
    '035_di_fixed': ['D_I_alphabet', 'insertion_after_P_est', 'canceled_baseline_word_after_P_est', 'singular_fixed_point', 'canceled_De_before_Cette'],
    '035_modules_orbit': ['modules_quotation_marks'],
    '035_canceled_mu': ['canceled_OPS_que', 'canceled_elle_est_celle_de'],
    '035_canceled_orbit': ['local_cancellation_donnee_par', 'un_before_t_pair', 'multiplicative_k_superscript'],
    '035_canceled_J': ['local_deleted_lambda_equals', 'canceled_radicals_after_J', 'domain_Sigma_k'],
    '035_canceled_change': ['orbit_change_prose'],
    '035_canceled_parameter': ['rho_parameter_definition', 'rho_in_quadratic', 'deleted_quadratic_root_formula'],
    '035_canceled_triple': ['rho_in_final_tuple'],
    '035_canceled_eliminer': ['Comme_in_canceled_prose', 'deux_in_canceled_prose'],
    '035_canceled_discriminant': ['discriminant_different_in_canceled_prose', 'canceled_two_infinity_pair'],
    '035_canceled_comme': ['lower_canceled_comme_les_lambda_et'],
    '035_canceled_g': ['final_canceled_g_formula_and_points'],
    '035_pointdevue': ['du_notre_point_de_vue'],
    '035_des_sommets': ['live_d_un_after_des_sommets', 'canceled_word_before_carre'],
    '035_equilateral_edge': ['possible_comma_after_equilateral', 'singular_midpoint_phrase_M0459'],
    '035_question_tetra': ['ordinal_in_inserted_question'],
    '035_figure_upper': ['upper_sphere_drawing'],
    '035_figure_lower': ['lower_sphere_drawing'],
    '035_antiauto_heading': ['heading_sigma_and_underline_scope', 'heading_stables_plural_and_scope', 'capital_Cas_insertion', 'pronoun_after_Comme_M0460'],
    '035_antiauto_body': ['local_canceled_a', 'raised_t_in_bottom_live_fixed_point', 'local_canceled_et_and_preceding_comma'],
    '035_page_two': [],
    '035_folio': ['bottom_foliation_34'],
    '035_square_case_number': [],
}

MARK_IDS = {
    '035_di_fixed': ['M0457'],
    '035_equilateral_edge': ['M0458', 'M0459'],
    '035_antiauto_heading': ['M0460'],
}

DOUBT_PLACES = {
    '035_heading_case': ['canceled_opening_clause', 'initial_interlinear_insertion'],
    '035_autom_universel': ['canceled_de_after_autom'],
    '035_di_fixed': ['D_I_alphabet', 'insertion_after_P_est', 'canceled_baseline_word_after_P_est', 'canceled_De_before_Cette'],
    '035_canceled_mu': ['canceled_OPS_que'],
    '035_canceled_orbit': ['local_cancellation_donnee_par'],
    '035_canceled_J': ['canceled_radicals_after_J'],
    '035_canceled_change': ['orbit_change_initial_word', 'locally_deleted_changeant'],
    '035_canceled_eliminer': ['Comme_in_canceled_prose', 'deux_in_canceled_prose'],
    '035_canceled_discriminant': ['discriminant_different_in_canceled_prose'],
    '035_canceled_comme': ['lower_canceled_comme', 'locally_deleted_les'],
    '035_pointdevue': ['du_notre_point_de_vue'],
    '035_des_sommets': ['canceled_word_before_carre'],
    '035_equilateral_edge': ['M0458', 'possible_comma_after_equilateral'],
    '035_antiauto_heading': ['opening_parenthesis_of_case_insertion', 'M0460'],
    '035_antiauto_body': ['local_canceled_a', 'local_canceled_et'],
}

INVENTORY_ELEMENTS = {
    '035_page_two': ['top_page_number'],
    '035_heading_case': ['opening_case_paragraph', 'opening_canceled_clause', 'Dans_ce_cas_insertion'],
    '035_first_kg': ['I_insertion'],
    '035_autom_universel': ['de_after_autom'],
    '035_di_fixed': ['un_de_insertion', 'baseline_un_cancellation', 'De_before_Cette'],
    '035_modules_orbit': ['opening_case_paragraph'],
    OWNER: ['large_canceled_calculation'],
    '035_canceled_mu': ['first_mu_set_insertion', 'second_mu_set_insertion'],
    '035_canceled_orbit': ['donnee_par_local_cancellation'],
    '035_canceled_J': ['lambda_equals_local_cancellation', 'J_formula', 'radical_pair_local_cancellation'],
    '035_canceled_change': ['changeant_local_cancellation', 'not_two_insertion'],
    '035_canceled_parameter': ['changed_orbit_tuple', 'rho_parameter_and_equation', 'not_two_insertion', 'quadratic_root_local_cancellation'],
    '035_canceled_triple': ['final_tuple'],
    '035_canceled_comme': ['les_local_cancellation'],
    '035_canceled_g': ['g_formula'],
    '035_pointdevue': ['live_configuration_paragraph'],
    '035_square_case_number': ['live_configuration_paragraph'],
    '035_des_sommets': ['des_sommets_insertion', 'canceled_carre_or_cas'],
    '035_equilateral_edge': ['live_configuration_paragraph'],
    '035_question_tetra': ['case_question_insertion', 'six_insertion'],
    '035_figure_upper': ['upper_sphere'],
    '035_figure_lower': ['lower_sphere'],
    '035_antiauto_heading': ['antiautomorphism_heading', 'heading_sigma_insertion', 'complex_case_insertion', 'antiautomorphism_paragraph'],
    '035_antiauto_body': ['antiautomorphism_paragraph', 'a_local_cancellation', 'et_local_cancellation'],
    '035_folio': ['bottom_foliation'],
}

NOTE_IDS = {
    '035_heading_case': ['S035-01', 'N035-03'],
    '035_first_kg': ['S035-01'],
    '035_autom_universel': ['S035-01'],
    '035_di_fixed': ['S035-01', 'N035-03'],
    '035_modules_orbit': ['S035-01'],
    OWNER: ['S035-02', 'N035-01', 'N035-02', 'S035-C01', 'S035-C02', 'S035-C03'],
    '035_canceled_mu': ['N035-01'],
    '035_canceled_orbit': ['N035-01', 'S035-C01'],
    '035_canceled_J': ['N035-01'],
    '035_canceled_change': ['N035-01', 'S035-C01'],
    '035_canceled_parameter': ['S035-02', 'N035-01', 'S035-C01', 'S035-C02'],
    '035_canceled_triple': ['S035-02', 'S035-C02'],
    '035_canceled_eliminer': ['N035-02'],
    '035_canceled_discriminant': ['N035-02'],
    '035_canceled_comme': ['N035-01', 'N035-02'],
    '035_canceled_g': ['S035-C03'],
    '035_pointdevue': ['S035-03', 'N035-02'],
    '035_square_case_number': ['S035-03'],
    '035_des_sommets': ['S035-03'],
    '035_equilateral_edge': ['S035-03', 'N035-04'],
    '035_question_tetra': ['S035-03'],
    '035_figure_upper': ['N035-05'],
    '035_figure_lower': ['N035-05'],
    '035_antiauto_heading': ['S035-04', 'N035-04'],
    '035_antiauto_body': ['S035-04'],
    '035_page_two': ['N035-06'],
    '035_folio': ['N035-06'],
}

# These are textual-collation observations, not ink judgments. A whole second
# reading cannot safely be pasted into the narrower first-target substring.
SECOND_CONTEXT_WARNINGS = {
    '035_autom_universel': {
        'context': 'Second adds the existing prefix Ainsi, g est un and suffix de.',
        'action': 'Project the agreed surrounding page context; do not duplicate it.'},
    '035_di_fixed': {
        'context': 'Second includes a following comma after Cette fois that is outside the first target.',
        'action': 'Any punctuation extension needs the completed root instruction.'},
    '035_canceled_mu': {
        'context': 'Second begins with live des deux orbites, before the large deletion.',
        'action': 'The live prefix exists before OWNER and must neither be duplicated nor absorbed into its cancellation.'},
    '035_canceled_change': {
        'context': 'First extraction has a second outer-deleted fragment containing inserted ne2.',
        'action': 'That fragment aliases the one parameter insertion; never insert it into the page twice.'},
    '035_canceled_eliminer': {
        'context': 'Second includes lambda/et material also covered by canceled_comme.',
        'peers': ['035_canceled_comme'],
        'action': 'Reconcile as projections of OWNER after root decides the sequence.'},
    '035_pointdevue': {
        'context': 'Second repeats the canceled g formula before the live paragraph.',
        'peers': ['035_canceled_g', OWNER],
        'action': 'Canceled formula stays in OWNER; only the live point-of-view span belongs to this page unit.'},
    '035_des_sommets': {
        'context': 'Second includes the preceding live cas; its first target starts at inserted des sommets.',
        'action': 'Do not duplicate the preceding cas.'},
    '035_equilateral_edge': {
        'context': 'Second includes preceding sphériques and the following inserted question and Quand clause.',
        'peers': ['035_question_tetra'],
        'action': 'First target excludes preceding sphérique. A root-directed change to that word needs an explicitly extended target; the question is applied once.'},
    '035_question_tetra': {
        'context': 'Question is repeated in the second equilateral reading; second also reaches the next de l\u2019 fragment.',
        'peers': ['035_equilateral_edge'],
        'action': 'Keep one question insertion and obtain any extended suffix from the canonical live paragraph.'},
    '035_antiauto_heading': {
        'context': 'Second extends beyond d’ordre pair into on voit qu’il and later dans K, donc dans Sigma.',
        'peers': ['035_antiauto_body'],
        'action': 'The bridge on voit qu’il already follows the first heading target; the later fixed-point text is owned by the body.'},
    '035_square_case_number': {
        'context': 'Second repeats earlier point-of-view/modules context and later des sommets/d’un/canceled word/carré.',
        'peers': ['035_pointdevue', '035_des_sommets'],
        'action': 'Apply the square-case core once; reconcile neighboring excerpts without duplicating their text.'},
    OWNER: {
        'context': 'Second starts with live des deux orbites, and ends with live Cas moins intéressant que les.',
        'peers': ['035_canceled_mu', '035_pointdevue'],
        'action': 'Preserve both live boundary contexts outside the single outer deletion. Detail finals must derive from the canonical canceled result.'},
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tsv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def verify_pins():
    for relative, wanted in EXPECTED_HASHES.items():
        assert digest(B/relative) == wanted, f'Pinned input changed: {relative}'


def escaped(s, index):
    n = 0
    j = index-1
    while j >= 0 and s[j] == '\\':
        n += 1
        j -= 1
    return bool(n % 2)


def closing_brace(s, opening):
    assert s[opening] == '{' and not escaped(s, opening)
    depth = 0
    for i in range(opening, len(s)):
        if s[i] in '{}' and not escaped(s, i):
            depth += 1 if s[i] == '{' else -1
            if depth == 0:
                return i
    raise AssertionError('Unclosed LaTeX argument in source extraction')


def deleted_sequence(s):
    """Return arguments of top-level deleted wrappers, preserving inner bytes."""
    out = []
    i = 0
    prefix = r'\deleted{'
    while i < len(s):
        while i < len(s) and s[i].isspace():
            i += 1
        if i == len(s):
            break
        assert s.startswith(prefix, i), (i, s[i:i+80])
        start = i + len(prefix)
        end = closing_brace(s, start-1)
        out.append(s[start:end])
        i = end+1
    assert out
    return out


def unique_span(haystack, needle):
    assert needle and haystack.count(needle) == 1, (needle[:100], haystack.count(needle))
    start = haystack.index(needle)
    return [start, start+len(needle)]


def tikz_body(s):
    match = re.fullmatch(r'\\begin\{tikzpicture\}(?:\[[\s\S]*?\])?\s*([\s\S]*?)\\end\{tikzpicture\}', s)
    assert match
    return match.group(1).strip()


def load_snapshot():
    verify_pins()
    comparison = load_tsv(B/'second/148_scan035_comparison.tsv')
    rectangles = load_tsv(B/'second/148_scan035_boxes.tsv')
    review = json.loads((B/'reviews/148_scan035.json').read_text(encoding='utf-8'))
    page = (B/'pages/148_scan035.tex').read_text(encoding='utf-8')
    marks = load_tsv(PACKET/'marks.tsv')
    assert len(comparison) == len(rectangles) == 27
    assert sum(r['different'] == 'yes' for r in comparison) == 26
    assert [r['box'] for r in comparison] == [r['box'] for r in rectangles]
    assert len(review['changes']) == 48 and len(review['decisions']) == 4
    assert len(review['unresolved']) == 25 and len(review['inventory']) == 38
    return dict(page=page, comparison=comparison,
                comp={r['box']: r for r in comparison},
                rectangles={r['box']: r for r in rectangles},
                review=review, packet_marks=marks)


def canceled_segments(snapshot):
    """Locate ten main fragments and the single ne2 alias inside one owner."""
    comp = snapshot['comp']
    owner_first = comp[OWNER]['first']
    inners = deleted_sequence(owner_first)
    assert len(inners) == 1
    owner_inner = inners[0]
    owner_page_span = unique_span(snapshot['page'], owner_first)
    inner_page_start = owner_page_span[0] + len(r'\deleted{')
    projections = {}
    for key in DETAILS:
        fragments = deleted_sequence(comp[key]['first'])
        assert len(fragments) == (2 if key == '035_canceled_change' else 1)
        parts = []
        for i, fragment in enumerate(fragments):
            span = unique_span(owner_inner, fragment)
            parts.append(dict(
                inner_span=span,
                page_span=[inner_page_start+span[0], inner_page_start+span[1]],
                inner_text=fragment,
                role='alias of parameter insertion' if i == 1 else 'main detail fragment',
                page_write=False))
        projections[key] = parts
        restored = '\n'.join(r'\deleted{' + item['inner_text'] + '}' for item in parts)
        assert restored == comp[key]['first'], key
    alias = projections['035_canceled_change'][1]
    parameter = projections['035_canceled_parameter'][0]
    assert parameter['inner_span'][0] <= alias['inner_span'][0] < alias['inner_span'][1] <= parameter['inner_span'][1]
    assert alias['inner_text'] == r'\inserted{\(\ne2\)}'
    mains = sorted((parts[0]['inner_span'][0], parts[0]['inner_span'][1], key)
                   for key, parts in projections.items())
    assert [key for _,_,key in mains] == list(DETAILS)
    assert all(a[1] <= b[0] for a,b in zip(mains,mains[1:]))
    chunks = []
    cursor = 0
    for start, end, key in mains:
        if start > cursor:
            chunks.append(dict(kind='unchanged separator', text=owner_inner[cursor:start]))
        chunks.append(dict(kind='detail', box=key, text=owner_inner[start:end]))
        cursor = end
    if cursor < len(owner_inner):
        chunks.append(dict(kind='unchanged separator', text=owner_inner[cursor:]))
    assert ''.join(c['text'] for c in chunks) == owner_inner
    return dict(owner_first=owner_first, owner_inner=owner_inner,
                owner_page_span=owner_page_span, inner_page_start=inner_page_start,
                projections=projections, chunks=chunks,
                alias_parameter_relative_span=[
                    alias['inner_span'][0]-parameter['inner_span'][0],
                    alias['inner_span'][1]-parameter['inner_span'][0]])


def compose_approved_canceled_fragments(snapshot, approved_inner_fragments):
    """Pure helper for later use; caller must supply all ten root-approved inners.

    No first/second choice is made here. The caller must separately reconcile the
    completed large-scope root decision and any requested ordering changes.
    """
    assert set(approved_inner_fragments) == set(DETAILS)
    pieces = canceled_segments(snapshot)['chunks']
    inner = ''.join(approved_inner_fragments[p['box']] if p['kind'] == 'detail'
                    else p['text'] for p in pieces)
    return r'\deleted{' + inner + '}'


def project_approved_details(approved_inner_fragments, parameter_alias):
    """Pure helper: derive consistent detail finals; alias never changes the page.

    parameter_alias must be explicitly supplied after root adjudication. Use None
    only if root excludes that context from the change-box extraction. A supplied
    alias must occur exactly once in the approved parameter fragment.
    """
    assert set(approved_inner_fragments) == set(DETAILS)
    out = {key: r'\deleted{' + approved_inner_fragments[key] + '}' for key in DETAILS}
    if parameter_alias is not None:
        assert parameter_alias and approved_inner_fragments['035_canceled_parameter'].count(parameter_alias) == 1
        out['035_canceled_change'] += '\n' + r'\deleted{' + parameter_alias + '}'
    return out


def require_completed_root_decisions(snapshot, entries):
    """Gate only; this scaffold does not read a potentially unfinished working file."""
    expected = {r['box'] for r in snapshot['comparison'] if r['different'] == 'yes'}
    assert len(entries) == 26 and len({r['box'] for r in entries}) == 26
    assert {r['box'] for r in entries} == expected
    assert all(r.get('viewed_by_main') is True for r in entries)
    assert all(r.get('choice') in ('first', 'second', 'revised') for r in entries)
    assert all(r.get('ink') and r.get('confidence') for r in entries)
    return True


def build_map(snapshot):
    review = snapshot['review']
    page = snapshot['page']
    comp = snapshot['comp']
    canceled = canceled_segments(snapshot)
    change_index = {r['place']: i for i,r in enumerate(review['changes'])}
    doubt_index = {r['place']: i for i,r in enumerate(review['unresolved'])}
    decision_index = {r['id']: i for i,r in enumerate(review['decisions'])}
    mark_source = {r['id']: r for r in snapshot['packet_marks']}
    inventory_index = {r['element']: i for i,r in enumerate(review['inventory'])}
    note_index = {r['id']: i for i,r in enumerate(review['notes'])}
    assert set(change_index) == {name for values in CHANGE_PLACES.values() for name in values}
    assert set(doubt_index) == {name for values in DOUBT_PLACES.values() for name in values}
    assert set(decision_index) == set(mark_source) == {name for values in MARK_IDS.values() for name in values}
    assert set(inventory_index) == {name for values in INVENTORY_ELEMENTS.values() for name in values}

    result = []
    scheduled = []
    for c in snapshot['comparison']:
        key = c['box']
        b = snapshot['rectangles'][key]
        own_change_names = CHANGE_PLACES.get(key, [])
        own_doubt_names = DOUBT_PLACES.get(key, [])
        own_inventory = INVENTORY_ELEMENTS.get(key, [])
        if key == OWNER:
            own_change_names = [name for child in DETAILS for name in CHANGE_PLACES.get(child, [])]
            own_doubt_names = [name for child in DETAILS for name in DOUBT_PLACES.get(child, [])]
            own_inventory = sorted(set(own_inventory + [name for child in DETAILS for name in INVENTORY_ELEMENTS.get(child, [])]))
        row = dict(box=key, different=c['different'],
                   original_rectangle=[int(b[x]) for x in ('x0','y0','x1','y1')],
                   existing_changes=[dict(index=change_index[name], place=name,
                       c=review['changes'][change_index[name]]['c'],
                       h=review['changes'][change_index[name]]['h'],
                       current_final=review['changes'][change_index[name]]['final'],
                       against_c=review['changes'][change_index[name]]['against_c'],
                       against_h=review['changes'][change_index[name]]['against_h'])
                       for name in own_change_names],
                   marks=[dict(id=name, review_index=decision_index[name],
                       packet_source_row=mark_source[name]['source_row'],
                       packet_mark=mark_source[name]['the mark as written'],
                       current_decision=review['decisions'][decision_index[name]]['decision'],
                       current_reading=review['decisions'][decision_index[name]]['reading'])
                       for name in MARK_IDS.get(key, [])],
                   doubts=[dict(index=doubt_index[name], place=name,
                       current_reading=review['unresolved'][doubt_index[name]]['reading'])
                       for name in own_doubt_names],
                   inventory=[dict(index=inventory_index[name], element=name) for name in own_inventory],
                   notes=[dict(index=note_index[name], id=name) for name in NOTE_IDS.get(key, [])],
                   second_context_warning=SECOND_CONTEXT_WARNINGS.get(key))
        if key in DETAILS:
            row.update(page_write_owner=OWNER, page_write=False,
                       extraction_parts=canceled['projections'][key])
        else:
            target = tikz_body(c['first']) if key in FIGURES else c['first']
            span = unique_span(page, target)
            row.update(page_write_owner=key, page_write=c['different']=='yes',
                       target_mode='body inside shared figure' if key in FIGURES else 'exact first span',
                       page_span=span, target_text=target)
            if c['different'] == 'yes':
                scheduled.append(dict(box=key, span=span))
        if key in FIGURES:
            row['graphic_integration'] = dict(
                shared_outer_coordinates='x=.0088cm,y=-.0088cm',
                first_extraction_wrapper='synthetic tikzpicture without unit options; do not paste as a second picture',
                existing_inner_scope='shift={(25,305)}' if key == '035_figure_lower' else None,
                instruction='Retain first graphic placement until root supplies final geometry and any physical-size scaling.')
        if key == '035_square_case_number':
            row['accounting_note'] = 'No existing C/H change row for this first-target case-number clause. Await root; do not create a row for agreement or additional doubt alone.'
        if key == OWNER:
            row['accounting_note'] = 'Aggregate links to the nineteen existing canceled-detail C/H rows; these are not nineteen additional rows.'
        result.append(row)
    scheduled.sort(key=lambda r:r['span'][0])
    assert len(scheduled) == 16
    assert all(a['span'][1] <= b['span'][0] for a,b in zip(scheduled,scheduled[1:]))
    assert len(result) == 27
    initial_fragments = {key: canceled['projections'][key][0]['inner_text'] for key in DETAILS}
    assert compose_approved_canceled_fragments(snapshot, initial_fragments) == comp[OWNER]['first']
    projected = project_approved_details(initial_fragments, canceled['projections']['035_canceled_change'][1]['inner_text'])
    assert all(projected[key] == comp[key]['first'] for key in DETAILS)
    assert page[:canceled['owner_page_span'][0]].endswith('des deux orbites,\n\n')
    assert page[canceled['owner_page_span'][1]:].startswith('\n\nCas moins intéressant')
    verify_pins()
    return dict(
        status='read-only scaffold; no root choices applied', scan=35,
        total_boxes=27, differing_boxes=26, agreed_box='035_page_two',
        existing_review_counts=dict(changes=48, marks=4, doubts=25, inventory=38),
        owner=OWNER, detail_box_count=10, detail_projection_fragment_count=11,
        page_write_unit_count=16, disjoint_future_write_schedule=scheduled,
        canceled_alias=dict(box='035_canceled_change', fragment=1,
            owner_detail='035_canceled_parameter',
            parameter_relative_span=canceled['alias_parameter_relative_span'],
            current_text=r'\inserted{\(\ne2\)}', page_occurrences=page.count(r'\inserted{\(\ne2\)}')),
        live_boundaries=dict(before='des deux orbites,', after='Cas moins intéressant',
            instruction='Both remain outside the single large cancellation.'),
        boxes=result, pinned_hashes=EXPECTED_HASHES,
        root_working_file_read=False, images_read=False,
        page_or_review_written=False, shared_outputs_touched=False,
    )


# The read-only map above was completed before root released the sealed choices.
# Everything below mechanically implements the now-complete root working file.
# It reads no images and makes no new letter, symbol, or geometry judgment.
WORKING = B/'second/148_scan035_root_working.json'
ADJUDICATIONS = B/'second/148_scan035_adjudications.json'
LOWER_OLD = r'\draw[line width=.55pt] (92,167)..controls(82,178)and(73,186)..(71,195);'
LOWER_NEW = '\n'.join([
    r'\draw[line width=.55pt] (88.1778,166.4)--(71.1111,189.1556)--(74.6667,191.6444);',
    r'\draw[line width=.55pt] (71.4667,194.8444)--(80,179.5556)--(95.2889,173.1556);',
])
NE2 = r'\inserted{\(\ne2\)}'


def once(text, old, new):
    assert text.count(old) == 1, (old[:160], text.count(old))
    return text.replace(old, new, 1)


def protected_tsvs_unchanged():
    for relative, wanted in EXPECTED_HASHES.items():
        if relative.endswith('.tsv'):
            assert digest(B/relative) == wanted, relative


def atomic(path, content):
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w', encoding='utf-8', newline='') as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def validate_final(page, review, entries, comp):
    """Mechanical consistency checks only, with no TeX execution."""
    root = {e['box']: e for e in json.loads(WORKING.read_text(encoding='utf-8'))}
    final = {e['box']: e['final'] for e in entries}
    assert len(entries) == len(root) == 26
    assert set(final) == set(root)
    assert all(e['viewed_by_main'] is True for e in entries)
    assert all((B/e['crop']).is_file() for e in entries)
    assert sum(e['choice'] == 'revised' for e in entries) == 17
    assert {key for key in final if final[key] != comp[key]['first']} == {
        key for key in root if root[key]['choice'] == 'revised'}
    for key, text in final.items():
        if key in DETAILS:
            continue
        body = tikz_body(text) if key in FIGURES else text
        assert page.count(body) == 1, key
    owner_inner, = deleted_sequence(final[OWNER])
    fragments = {}
    for key in DETAILS:
        pieces = deleted_sequence(final[key])
        assert len(pieces) == (2 if key == '035_canceled_change' else 1)
        fragments[key] = pieces[0]
        assert owner_inner.count(pieces[0]) == 1, key
        if key == '035_canceled_change':
            assert pieces[1] == NE2
    assert project_approved_details(fragments, NE2) == {
        key: final[key] for key in DETAILS}
    assert [key for _, key in sorted((owner_inner.index(fragments[key]), key)
                                     for key in DETAILS)] == list(DETAILS)
    # The same saved separators reassemble the owner; no detail is inserted twice.
    old_inner, = deleted_sequence(comp[OWNER]['first'])
    for key in DETAILS:
        old_fragment = deleted_sequence(comp[key]['first'])[0]
        old_inner = once(old_inner, old_fragment, fragments[key])
    assert owner_inner == old_inner
    start = page.index(final[OWNER])
    assert page[:start].endswith('des deux orbites,\n\n')
    assert page[start+len(final[OWNER]):].startswith('\n\nCas moins intéressant')
    assert page.count(NE2) == 1
    assert r'\deleted{elle est celle' not in page
    assert page.count(r'\begin{tikzpicture}') == page.count(r'\end{tikzpicture}') == 1
    assert page.count(r'\figure{') == 1
    assert r'[x=.0088cm,y=-.0088cm,line cap=round,line join=round]' in page
    lower = tikz_body(final['035_figure_lower'])
    assert lower == once(tikz_body(comp['035_figure_lower']['first']), LOWER_OLD, LOWER_NEW)
    assert lower.count(r'\begin{scope}[shift={(25,305)}]') == 1
    assert lower.count(LOWER_NEW) == 1 and LOWER_OLD not in lower
    assert r'(143,143)..controls(124,166)and(94,167)..(72,195)' in lower
    assert final['035_figure_upper'] == comp['035_figure_upper']['first']
    assert page.count('on voit qu’il') == 1
    assert page.count('on sait qu’il') == 1
    assert r'étant d’ordre fini, on sait qu’il' in page
    assert r'qui est \(1,3\), ou \(\unsure{6|5}\).' in page
    assert r'\unsure{équilatéral}' not in page
    assert r'\unsure{6|5}' in page
    assert r'\deleted{\unsure{et|a}} \unsure{a|.} un p\textsuperscript{t}' in page
    assert r'\lambda^2-\rho\lambda+1=0\);' in page
    assert r'\rho^2\unsure{-4}' in page
    assert r'\unsure{discriminant} \(\lambda\longrightarrow1\), ou ---' in page
    assert r'\deleted{\(\unsure{f^\circ|\rho}\)}' in page
    level = 0
    for i, char in enumerate(page):
        if char in '{}' and not escaped(page, i):
            level += 1 if char == '{' else -1
            assert level >= 0, i
    assert level == 0
    for environment in ('tikzpicture', 'scope'):
        assert page.count(r'\begin{'+environment+'}') == page.count(r'\end{'+environment+'}')
    assert len(review['changes']) == 51
    assert len(review['decisions']) == 4
    assert len(review['unresolved']) == 32
    assert len(review['inventory']) == 38
    assert len(review['checks']) == 3
    assert all(r['type'] == 'computation or formal certificate' for r in review['checks'])
    places = [r['place'] for r in review['changes']]
    assert len(places) == len(set(places))
    doubts = {r['place']: r for r in review['unresolved']}
    assert 'M0458' not in doubts and 'possible_comma_after_equilateral' not in doubts
    assert doubts['final_fixed_cardinality']['reading'] == r'\unsure{6|5}'
    changes = {r['place']: r for r in review['changes']}
    assert changes['lower_sphere_drawing']['final'] == lower
    assert changes['upper_sphere_drawing']['final'].strip() == tikz_body(final['035_figure_upper'])
    assert changes['canceled_two_infinity_pair']['final'] == r'\(\lambda\longrightarrow1\), ou ---'
    assert changes['lower_canceled_comme_les_lambda_et']['final'] == fragments['035_canceled_comme']
    assert changes['final_fixed_cardinality']['final'] == r'\unsure{6|5}'
    assert review['pending_cross_page_checks'][0]['status'] in (
        'pending', 'comparison completed; doubt retained')
    assert review['pending_cross_page_checks'][0]['compare_scan'] == 36
    protected_tsvs_unchanged()


def implement(write=False):
    snapshot = load_snapshot()
    mapping = build_map(snapshot)
    assert not ADJUDICATIONS.exists(), 'Non-idempotent main pass: adjudications already exist.'
    assert not snapshot['review'].get('second_audit'), 'Root audit already recorded.'
    working_hash = digest(WORKING)
    working = json.loads(WORKING.read_text(encoding='utf-8'))
    require_completed_root_decisions(snapshot, working)
    root = {e['box']: e for e in working}
    assert sum(e['choice'] == 'revised' for e in working) == 17
    assert r'\unsure{6|5}' in root['035_antiauto_body']['instructions']
    comp = snapshot['comp']
    review = snapshot['review']
    finals = {key: value['first'] for key, value in comp.items()}

    def meta(key):
        rectangle = snapshot['rectangles'][key]
        return dict(crop=f'crops/second/148_scan035/{key}.png',
                    box=[int(rectangle[x]) for x in ('x0','y0','x1','y1')])

    confidence_order = {'low': 0, 'medium': 1, 'high': 2}

    def evidence(key, old_confidence=None):
        confidence = root[key]['confidence']
        # A broad crop's high confidence does not silently certify a locally
        # obscured word that root explicitly retains under an uncertainty macro.
        if old_confidence in confidence_order:
            confidence = min((confidence, old_confidence), key=confidence_order.get)
        return dict(ink=root[key]['ink'], confidence=confidence, **meta(key))

    def revise_final(key, old, new):
        finals[key] = once(finals[key], old, new)

    revise_final('035_heading_case', r'\inserted{\unsure{Dans ce cas}}',
                 r'\inserted{\unsure{Dans ce cas|Dans les}}')
    revise_final('035_di_fixed', r'\inserted{\unsure{un de|un}} \deleted{\unsure{un}}',
                 r'\inserted{\unsure{un de|un|un aut.}} \unsure{\deleted{un}|un}')
    revise_final('035_di_fixed', r'\deleted{\unsure{De}}', r'\deleted{\unsure{De|Ce}}')
    revise_final('035_modules_orbit', 'la situation a des', r'la situation \unsure{a} des')

    pieces = canceled_segments(snapshot)
    fragments = {key: pieces['projections'][key][0]['inner_text'] for key in DETAILS}

    def revise_fragment(key, old, new):
        fragments[key] = once(fragments[key], old, new)

    revise_fragment('035_canceled_mu', r'\unsure{OPS} que', r'\unsure{OPS} \unsure{que|pour}')
    revise_fragment('035_canceled_mu', r'de \(g\) sur', r'de \(\unsure{g|\langle g\rangle}\) sur')
    revise_fragment('035_canceled_mu', r'sur \(\mu_2\) \inserted{\(=\{\pm1\}\)}',
                    r'sur \(\mu_2\) \inserted{\(=\unsure{\{\pm1\}|(\pm1)}\)}')
    revise_fragment('035_canceled_orbit', r'}} un \(\{t,-t\}\)',
                    r'}} \unsure{un|une} \(\{t,-t\}\)')
    revise_fragment('035_canceled_J', r'\pm\sqrt\lambda)\)',
                    r'\pm\unsure{\sqrt\lambda|t})\)')
    revise_fragment('035_canceled_J',
        r'\deleted{\(\unsure{\sqrt\lambda,\sqrt\lambda}\)}',
        r'\deleted{\(\unsure{\sqrt\lambda,\sqrt\lambda)|\sqrt\lambda,-\sqrt\lambda)}\)}')
    fragments['035_canceled_change'] = (
        r'\unsure{Si on|en} \deleted{\unsure{change}} change le choix de l’orbite, on trouve')
    revise_fragment('035_canceled_parameter', r'\lambda^2-\rho\lambda+1=0\),',
                    r'\lambda^2-\rho\lambda+1=0\);')
    revise_fragment('035_canceled_triple', r'\rho^2-4', r'\rho^2\unsure{-4}')
    fragments['035_canceled_eliminer'] = r'\unsure{Eliminer|Comme} \(0,\infty\), et \unsure{deux|les}'
    fragments['035_canceled_discriminant'] = r'\unsure{discriminant} \(\lambda\longrightarrow1\), ou ---'
    fragments['035_canceled_comme'] = r'\unsure{comme} \deleted{\(\unsure{f^\circ|\rho}\)} \(\lambda\), et'
    finals.update(project_approved_details(fragments, NE2))
    finals[OWNER] = compose_approved_canceled_fragments(snapshot, fragments)

    revise_final('035_des_sommets', r'\deleted{\unsure{carré|cas}}',
                 r'\deleted{\unsure{carré|cas|cube}}')
    revise_final('035_equilateral_edge', r'\unsure{équilatéral}\unsure{,}', 'équilatéral,')
    revise_final('035_figure_lower', LOWER_OLD, LOWER_NEW)
    revise_final('035_antiauto_body', r'\deleted{\unsure{a}} a un',
                 r'\deleted{\unsure{et|a}} \unsure{a|.} un')
    revise_final('035_antiauto_body', 'étant d’ordre fini, on voit', 'étant d’ordre fini, on sait')
    revise_final('035_antiauto_body', r'ou \(5\).', r'ou \(\unsure{6|5}\).')

    # Only the sixteen disjoint page units are ever replaced. All ten canceled
    # detail outputs, including the separate ne2 alias, remain projections.
    page = snapshot['page']
    targets = {row['box']: row for row in mapping['boxes']}
    for unit in reversed(mapping['disjoint_future_write_schedule']):
        key = unit['box']
        start, end = unit['span']
        assert page[start:end] == targets[key]['target_text']
        replacement = tikz_body(finals[key]) if key in FIGURES else finals[key]
        page = page[:start] + replacement + page[end:]

    changes = {row['place']: row for row in review['changes']}
    place_to_box = {place: key for key, places in CHANGE_PLACES.items() for place in places}
    for place, row in changes.items():
        row.update(evidence(place_to_box[place], row['confidence']))

    def change(place, key, final, **updates):
        assert place_to_box[place] == key
        changes[place].update(final=final, **evidence(key, changes[place]['confidence']), **updates)

    change('initial_interlinear_insertion', '035_heading_case',
           r'\inserted{\unsure{Dans ce cas|Dans les}}')
    change('insertion_after_P_est', '035_di_fixed', r'\inserted{\unsure{un de|un|un aut.}}')
    change('canceled_baseline_word_after_P_est', '035_di_fixed', r'\unsure{\deleted{un}|un}')
    change('canceled_De_before_Cette', '035_di_fixed', r'\deleted{\unsure{De|Ce}} Cette fois')
    change('canceled_OPS_que', '035_canceled_mu', r'\unsure{OPS} \unsure{que|pour}')
    change('local_cancellation_donnee_par', '035_canceled_orbit',
           r'est \deleted{\unsure{donnée par}} \unsure{un|une}')
    change('un_before_t_pair', '035_canceled_orbit', r'\unsure{un|une} \(\{t,-t\}\)')
    change('canceled_radicals_after_J', '035_canceled_J',
           r'\deleted{\(\unsure{\sqrt\lambda,\sqrt\lambda)|\sqrt\lambda,-\sqrt\lambda)}\)}',
           against_c=True)
    change('orbit_change_prose', '035_canceled_change',
           r'\unsure{Si on|en} \deleted{\unsure{change}} change le choix de l’orbite',
           against_c=True, against_h=True)
    change('rho_in_final_tuple', '035_canceled_triple',
           r'(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2\unsure{-4}})})')
    change('Comme_in_canceled_prose', '035_canceled_eliminer', r'\unsure{Eliminer|Comme}',
           against_c=False, against_h=True)
    change('deux_in_canceled_prose', '035_canceled_eliminer', r'\unsure{deux|les}')
    change('discriminant_different_in_canceled_prose', '035_canceled_discriminant',
           r'\unsure{discriminant}', against_c=True, against_h=True, kind='misread word')
    change('canceled_two_infinity_pair', '035_canceled_discriminant',
           r'\(\lambda\longrightarrow1\), ou ---', against_c=True, against_h=True)
    change('lower_canceled_comme_les_lambda_et', '035_canceled_comme',
           fragments['035_canceled_comme'], against_c=True, against_h=True,
           kind='misread symbol or index', math=True)
    change('canceled_word_before_carre', '035_des_sommets', r'\deleted{\unsure{carré|cas|cube}}')
    change('possible_comma_after_equilateral', '035_equilateral_edge', 'équilatéral, et')
    changes['possible_comma_after_equilateral']['confidence'] = 'high'
    change('lower_sphere_drawing', '035_figure_lower', tikz_body(finals['035_figure_lower']))
    change('local_canceled_a', '035_antiauto_body', r'\deleted{\unsure{et|a}} \unsure{a|.}',
           against_c=True, against_h=True)

    # These three places require new substantive C/H rows. Added alternatives,
    # resolved certainty, coordinate refinements and overlapping extracts do not.
    witnesses = {name: (PACKET/(name+'.tex')).read_text(encoding='utf-8') for name in ('C','H')}

    def new_change(place, key, c, h, final, kind, mathematical=False):
        assert place not in changes
        assert c in witnesses['C'], (place, 'C', c)
        assert h in witnesses['H'], (place, 'H', h)
        row = dict(place=place, c=c, h=h, final=final, kind=kind,
                   against_c=True, against_h=True, math=mathematical, **evidence(key))
        review['changes'].append(row)
        changes[place] = row

    new_change('semicolon_after_quadratic', '035_canceled_parameter',
        r'\(\lambda^2-\beta\lambda+1=0\),', '$\\lambda^{2} - \\rho\\lambda + 1\n= 0$,',
        r'\(\lambda^2-\rho\lambda+1=0\);', 'misread symbol or index')
    new_change('verb_after_finite_order', '035_antiauto_body',
        'étant d’ordre fini, on voit', "étant d'ordre fini, on voit",
        'étant d’ordre fini, on sait', 'misread word')
    new_change('final_fixed_cardinality', '035_antiauto_body',
        r'ou \(5\).', 'ou 5.', r'\unsure{6|5}', 'misread symbol or index', True)

    marks = {row['id']: row for row in review['decisions']}
    for key, names in MARK_IDS.items():
        for name in names:
            marks[name].update(evidence(key, marks[name]['confidence']))
    marks['M0458'].update(decision='first', reading='équilatéral', confidence='high')

    # Refresh evidence without claiming that a broad crop resolved its local
    # crossed words. Then apply only root's stated changed/added uncertainties.
    doubt_box = {place: key for key, places in DOUBT_PLACES.items() for place in places}
    for row in review['unresolved']:
        key = doubt_box[row['place']]
        ev = evidence(key, row['confidence'])
        row.update(issue=ev.pop('ink'), **ev)
    review['unresolved'] = [row for row in review['unresolved']
        if row['place'] not in ('M0458', 'possible_comma_after_equilateral')]
    doubts = {row['place']: row for row in review['unresolved']}

    def doubt(place, key, reading, alternatives):
        old = doubts.get(place)
        ev = evidence(key, old['confidence'] if old else None)
        row = dict(place=place, reading=reading, alternatives=alternatives,
                   issue=ev.pop('ink'), **ev)
        if old:
            old.update(row)
        else:
            review['unresolved'].append(row)
            doubts[place] = row

    doubt('initial_interlinear_insertion', '035_heading_case',
          r'\unsure{Dans ce cas|Dans les}', ['Dans ce cas','Dans les'])
    doubt('insertion_after_P_est', '035_di_fixed', r'\unsure{un de|un|un aut.}',
          ['un de','un','un aut.'])
    doubt('canceled_baseline_word_after_P_est', '035_di_fixed',
          r'\unsure{\deleted{un}|un}', [r'\deleted{un}','un without a local deletion'])
    doubt('canceled_De_before_Cette', '035_di_fixed', r'\unsure{De|Ce}', ['De','Ce'])
    doubt('situation_a', '035_modules_orbit', r'\unsure{a}', [])
    doubt('canceled_word_after_OPS', '035_canceled_mu', r'\unsure{que|pour}', ['que','pour'])
    doubt('canceled_g_group_brackets', '035_canceled_mu',
          r'\unsure{g|\langle g\rangle}', ['g',r'\langle g\rangle'])
    doubt('second_mu_insertion_delimiters', '035_canceled_mu',
          r'\unsure{\{\pm1\}|(\pm1)}', [r'\{\pm1\}',r'(\pm1)'])
    doubt('un_before_t_pair', '035_canceled_orbit', r'\unsure{un|une}', ['un','une'])
    doubt('last_term_of_J', '035_canceled_J', r'\unsure{\sqrt\lambda|t}', [r'\sqrt\lambda','t'])
    doubt('canceled_radicals_after_J', '035_canceled_J',
          r'\unsure{\sqrt\lambda,\sqrt\lambda)|\sqrt\lambda,-\sqrt\lambda)}',
          [r'\sqrt\lambda,\sqrt\lambda)',r'\sqrt\lambda,-\sqrt\lambda)'])
    doubt('orbit_change_initial_word', '035_canceled_change', r'\unsure{Si on|en}', ['Si on','en'])
    doubt('locally_deleted_changeant', '035_canceled_change', r'\unsure{change}', [])
    doubt('inner_discriminant_terminal', '035_canceled_triple', r'\unsure{-4}', [])
    doubt('Comme_in_canceled_prose', '035_canceled_eliminer', r'\unsure{Eliminer|Comme}',
          ['Eliminer','Comme'])
    doubt('deux_in_canceled_prose', '035_canceled_eliminer', r'\unsure{deux|les}', ['deux','les'])
    doubt('discriminant_different_in_canceled_prose', '035_canceled_discriminant',
          r'\unsure{discriminant}', [])
    doubt('locally_deleted_les', '035_canceled_comme', r'\unsure{f^\circ|\rho}',
          [r'f^\circ',r'\rho'])
    doubt('canceled_word_before_carre', '035_des_sommets', r'\unsure{carré|cas|cube}',
          ['carré','cas','cube'])
    doubt('local_canceled_a', '035_antiauto_body', r'\unsure{et|a}', ['et','a'])
    doubt('compressed_live_a', '035_antiauto_body', r'\unsure{a|.}', ['a','.'])
    doubt('final_fixed_cardinality', '035_antiauto_body', r'\unsure{6|5}', ['6','5'])

    inventory = {row['element']: row for row in review['inventory']}
    inventory_readings = {
        'Dans_ce_cas_insertion': r'\unsure{Dans ce cas|Dans les}',
        'un_de_insertion': r'\unsure{un de|un|un aut.}',
        'baseline_un_cancellation': r'\unsure{\deleted{un}|un}',
        'De_before_Cette': r'\unsure{De|Ce}',
        'large_canceled_calculation': r'\unsure{OPS} \unsure{que|pour} l’opération; one outer cancellation through pts fixes',
        'second_mu_set_insertion': r'=\unsure{\{\pm1\}|(\pm1)}',
        'J_formula': r'J=(0,\pm1,\pm\unsure{\sqrt\lambda|t})',
        'radical_pair_local_cancellation': r'\unsure{\sqrt\lambda,\sqrt\lambda)|\sqrt\lambda,-\sqrt\lambda)}',
        'changeant_local_cancellation': r'\unsure{change}',
        'rho_parameter_and_equation': r'\rho=\lambda+1/\lambda; one inserted \ne2; equation followed by a semicolon',
        'final_tuple': r'(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2\unsure{-4}})})',
        'les_local_cancellation': r'\unsure{f^\circ|\rho}',
        'canceled_carre_or_cas': r'\unsure{carré|cas|cube}',
        'lower_sphere': 'Tetrahedral strokes; seven marked points including P; two short returning strokes at the lower-left edge',
        'a_local_cancellation': r'\unsure{et|a}',
    }
    for name, reading in inventory_readings.items():
        inventory[name]['first_words_or_objects'] = reading
    inventory['baseline_un_cancellation']['kind'] = 'word with uncertain deletion state'
    inventory['baseline_un_cancellation']['position'] = 'Below the preceding insertion; leader versus local strike unresolved'
    inventory['changeant_local_cancellation']['position'] = 'Between tentative Si on|en and the replacement change'
    inventory['antiautomorphism_paragraph']['position'] = r'From Comme through the final ou \unsure{6|5}'
    inventory['a_local_cancellation']['position'] = r'Before the uncertain \unsure{a|.} un p^t fixe'

    notes = {row['id']: row for row in review['notes']}
    notes['S035-02']['text'] = (
        'The canceled calculation uses rho=lambda+1/lambda, then the written quadratic and radical expressions. '
        'The equation is followed by a semicolon. Its canceled state, local revisions and doubtful inner -4 '
        'are retained. Earlier computations S035-C01–C03 do not identify crossed or retraced ink.')
    notes['S035-04']['text'] = (
        'The last paragraph asserts that the finite-order antiautomorphism has order 2 and corresponds to a '
        'real structure. It then distinguishes fixed-set cardinalities 1, 3 and an uncertain 6|5. Root favors '
        '6 from the closed lower loop and rising upper curve, while retaining 5 despite the expected odd count. '
        'That expectation does not settle the stroke, and no mathematical repair is imposed. A numeral-form '
        'comparison with scan 036 remains queued before final freeze; this implementation did not inspect 036.')
    notes['N035-01']['text'] = (
        'The large canceled calculation is one outer deleted block, beginning at doubtful OPS and ending '
        'at pts fixes. The preceding des deux orbites and following Cas moins intéressant remain outside it. '
        'Local deletions are retained for donnée par, lambda=, the radical tail with its closing parenthesis, '
        'the first doubtful change, the quadratic solution and f-circle|rho. The line over elle est celle '
        'belongs to the stepped large cancellation boundary; no additional local deletion is asserted there. '
        'The two mu additions and the single ne2 insertion belong to this canceled draft.')
    notes['N035-02']['text'] = (
        'Du|de notre point de vue stays unresolved. In the canceled prose root favors Si on|en, doubtful '
        'deleted change followed by change, and Eliminer|Comme with deux|les. The next physical row reads '
        'doubtful discriminant, lambda→1, ou and a dash at the left, then doubtful comme, locally deleted '
        'f-circle|rho, lambda and et at the right. These readings follow the supplied ink decisions and '
        'are not completed into a coherent mathematical argument. The numerator of g(z) remains lambda.')
    notes['N035-03']['text'] = (
        'The initial insertion is Dans ce cas|Dans les. After P est the clipped small insertion remains '
        'un de|un|un aut.; no ses is supplied. The baseline un may be crossed or merely touched by the '
        'insertion guide, so its deletion state is itself uncertain. The canceled word before Cette is De|Ce. '
        'Both live fixed-point abbreviations retain the raised singular t.')
    notes['N035-04']['text'] = (
        'The sealed root crop review resolves équilatéral and its separate comma, preserving singular '
        'du milieu de l’une. Il|sigma and the opening-parenthesis versus insertion-guide ambiguity remain '
        'unresolved. Root also retains doubt on the compressed a after situation and a|point before un p^t '
        'fixe. In the latter paragraph the locally canceled word favors et|a; only the later on voit, after '
        'étant d’ordre fini, changes to on sait. The earlier on voit is unchanged.')
    notes['N035-05']['text'] = (
        'The two spheres remain in one figure with the first coordinate system and placement. The upper '
        'five points, P, irregular rear traces, substantial lower-right gap, short right-side gap and detached '
        'left stroke are retained. The lower sphere keeps seven points, P, doubled left contour, open '
        'lower-right contour and manually placed unequal rear traces and oblique dots. Exactly one short '
        'lower-left edge path is replaced by the two returning strokes supplied by root, already converted '
        'by division by 2.8125. The separate long center-to-left curve remains once; no arrowhead is added.')
    notes['N035-08']['text'] += (
        ' The subsequent sealed blind stage contains 27 boxes, of which 26 differ. Root personally viewed '
        'all 26 differing fixed crops and supplied 17 revised choices. This mechanical pass updates those '
        'decisions without any image judgment, OCR, research, TeX compilation, shared rebuild or audit recording.')
    notes['S035-C02']['text'] += (
        ' This is a formal computation only. It does not resolve the canceled final tuple’s doubtful -4.')
    review['notes'].extend([
        dict(id='N035-BLIND', kind='main-reader adjudication', text=(
            'The 26 sealed root decisions are applied mechanically. The large canceled owner is assembled '
            'once from ten canonical detail fragments. Eleven detail projections include the repeated ne2 '
            'context, which remains one page insertion. Sixteen disjoint page targets preserve live contexts '
            'around the cancellation, question insertion, square-case sentence and combined figure. The five '
            'locked first/second/boxes/comparison/token TSVs remain byte-identical. There is no duplicate '
            'catchall C/H row, and no new row for changed certainty, coordinate-only work or macro-only changes.')),
        dict(id='N035-NUMERAL-CHECK', kind='pending comparison', text=(
            'Before final freeze, compare the final antiautomorphism numeral on scan035 with the author’s '
            '5/6 forms on scan 036. The current reading is 6|5, with 6 favored by root’s crop decision. The '
            'comparison is pending and does not establish the mathematically expected 5.')),
    ])
    for record in review['checks']:
        record['type'] = 'computation or formal certificate'

    leader = next(row for row in review['hand_log'] if row.get('form') == 'insertion leaders')
    leader.update(
        observation='Curved or bracketed leaders pass close to baseline letters and can resemble cancellation or punctuation.',
        witness_effect='Est réunion and d’un stay live. The opening parenthesis of Cas and the deletion state of baseline un after P est remain ambiguous.')
    leader['habit'] = leader['form']+': '+leader['observation']
    for form, observation, effect in [
        ('compressed a', 'The situation a and the later a before un p^t fixe are compressed dark bodies; root retains local doubt rather than classifying every dark trace as punctuation.', 'The first remains a under doubt; the second is a|point. No new C/H row is counted for those alternatives alone.'),
        ('change', 'In the canceled orbit-change phrase, the separately struck verb and its replacement terminate after the g/e bodies; root sees no additional ant ending.', 'The existing orbit-change row now reads doubtful deleted change followed by change, after Si on|en.'),
        ('5/6', 'The final antiautomorphism numeral has a closed lower loop and rising upper curve favoring 6; cursive 5 and 6 may converge locally.', 'The final reading is 6|5. Scan 036 comparison is pending, and expected odd cardinality does not certify 5.'),
        (r'f^\circ|\rho', 'The locally crossed lower-prose cluster has a long descending stem and a small raised loop, admitting f-circle or rho.', 'The former tentative les is replaced by a doubtful formula symbol within its separate local deletion.'),
    ]:
        review['hand_log'].append(dict(form=form, observation=observation, pages=[35],
            holds_at_every_observed_occurrence=False, witness_effect=effect,
            habit=form+': '+observation))
    review['notation'].extend([
        dict(form=r'\unsure{f^\circ|\rho}', use='Locally deleted symbol in the lower canceled prose.',
             pages=[35], caution='The crossing prevents resolution; no word les is supplied.'),
        dict(form=r'\unsure{6|5}', use='Final fixed-set cardinality in the antiautomorphism paragraph.',
             pages=[35], caution='Root favors 6 from the stroke; scan 036 form comparison remains pending.'),
    ])
    revised_place_keys = {place: key for place, key in place_to_box.items()
                         if root[key]['choice'] == 'revised'}
    for row in review['differences_review']:
        places = row['place'].split('; ')
        keys = list(dict.fromkeys(revised_place_keys[place] for place in places if place in revised_place_keys))
        if keys:
            row['note'] = 'Sealed root decision: '+' '.join(root[key]['ink'] for key in keys)
    review['main_reader_review']['pre_blind_adjudication'] = review['main_reader_review']['adjudication']
    review['main_reader_review']['adjudication'] = (
        'Subsequent sealed blind adjudication: all 26 DIFF fixed crops were viewed by root; 17 choices are '
        'revised. Equilatéral and its comma are resolved. The canceled owner, local uncertainty layers, '
        'two returning lower-sphere strokes and final 6|5 are retained as recorded in the adjudication JSON. '
        'The scan 036 numeral-form comparison remains pending.')
    review['main_reader_review']['post_blind_decision_file'] = 'second/148_scan035_adjudications.json'
    review['blind_graphic_transforms'] = {
        '035_figure_lower': dict(
            authority='Exact paths supplied by root; no new geometric or ink judgment.',
            target_coordinate_cm='.0088', existing_scope_shift=[25,305],
            supplied_conversion_divisor='2.8125', replaced_paths=1, replacement_paths=2,
            replacement_line_width_pt='.55', long_center_to_left_curve_unchanged=True,
            upper_sphere_unchanged=True, shared_figure_retained=True,
            commands=LOWER_NEW.splitlines())}
    review['pending_cross_page_checks'] = [dict(
        id='Q035-036-FINAL-NUMERAL', status='pending', source_scan=35, compare_scan=36,
        source_box='035_antiauto_body', current_reading=r'\unsure{6|5}',
        task='Compare the author’s 5/6 numeral forms before final freeze; retain uncertainty unless ink resolves it.',
        limitation='The expected odd fixed count does not decide the stroke. No scan 036 input was opened in this mechanical pass.')]

    entries = []
    for item in working:
        entry = {key: value for key, value in item.items() if key != 'instructions'}
        entry.update(final=finals[item['box']], crop=meta(item['box'])['crop'],
                     crop_box=meta(item['box'])['box'])
        entries.append(entry)
    validate_final(page, review, entries, comp)
    verify_pins()
    assert digest(WORKING) == working_hash, 'Root working file changed during implementation.'
    if write:
        atomic(B/'pages/148_scan035.tex', page)
        atomic(B/'reviews/148_scan035.json', json.dumps(review, ensure_ascii=False, indent=2)+'\n')
        atomic(ADJUDICATIONS, json.dumps(entries, ensure_ascii=False, indent=2)+'\n')
        protected_tsvs_unchanged()
    return dict(scan=35, applied=write, adjudications=len(entries), revised_boxes=17,
        page_write_units=16, canceled_detail_boxes=10, detail_projection_fragments=11,
        page_ne2_insertions=page.count(NE2), changes_rows=len(review['changes']),
        against_c=sum(bool(row['against_c']) for row in review['changes']),
        against_h=sum(bool(row['against_h']) for row in review['changes']),
        mark_decisions=len(review['decisions']), unresolved=len(review['unresolved']),
        inventory_rows=len(review['inventory']), computation_checks=len(review['checks']),
        pending_scan036_numeral_comparison=True, protected_tsv_hashes_unchanged=True,
        root_working_sha256=working_hash, images_read=False,
        record_audit_run=False, shared_outputs_rebuilt=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--map', action='store_true', help='Print the original read-only mapping.')
    mode.add_argument('--apply', action='store_true', help='Atomically write page, review and adjudications.')
    mode.add_argument('--verify-applied', action='store_true', help='Check applied local files without mutation.')
    parser.add_argument('--json', action='store_true', help='Print the complete map with --map.')
    args = parser.parse_args()
    if args.map:
        report = build_map(load_snapshot())
        if not args.json:
            report = {key: report[key] for key in (
                'status','scan','total_boxes','differing_boxes','agreed_box',
                'existing_review_counts','detail_box_count','detail_projection_fragment_count',
                'page_write_unit_count','canceled_alias','root_working_file_read',
                'images_read','page_or_review_written','shared_outputs_touched')}
    elif args.verify_applied:
        comp = {row['box']: row for row in load_tsv(B/'second/148_scan035_comparison.tsv')}
        current_review = json.loads((B/'reviews/148_scan035.json').read_text(encoding='utf-8'))
        validate_final((B/'pages/148_scan035.tex').read_text(encoding='utf-8'),
                       current_review,
                       json.loads(ADJUDICATIONS.read_text(encoding='utf-8')), comp)
        report = dict(scan=35, applied_files_valid=True, protected_tsv_hashes_unchanged=True,
                      pending_scan036_numeral_comparison=any(
                          row['status'] == 'pending' for row in current_review['pending_cross_page_checks']),
                      files_written=False)
    else:
        report = implement(write=args.apply)
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.json else None))


if __name__ == '__main__':
    main()


def apply_root_numeral_comparison_followup_20261121():
    """Metadata-only, idempotent follow-up after root compared the 035/036 ink.

    Execute this FunctionDef alone using AST extraction; never rerun the main
    application pass. No image or scan036 source is read here. Root supplied the
    comparison observations. The page, audited finals, decisions and audit stay
    byte-identical; only notes, hand observations and pending-status markers change.
    """
    from pathlib import Path
    import copy
    import hashlib
    import json
    import os

    base = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
    review_file = base/'reviews/148_scan035.json'
    review = json.loads(review_file.read_text(encoding='utf-8'))
    before = copy.deepcopy(review)
    protected = [base/'pages/148_scan035.tex', base/'second/148_scan035_adjudications.json']
    protected += [base/('second/148_scan035'+suffix) for suffix in (
        '_first.tsv','_second.tsv','_boxes.tsv','_comparison.tsv','_token_differences.tsv')]
    sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    hashes = {str(path): sha(path) for path in protected}
    assert hashes[str(base/'pages/148_scan035.tex')] == 'aa6631665b83787111ef9bab651beeb153a49b79b60bc99ecdcf8b214fe8db52'
    assert hashes[str(base/'second/148_scan035_adjudications.json')] == 'e083134decd68f8d284e3a8c02c24a8985d131b07bff3bebd39abc482fcc0935'
    assert review['second_audit']['differences'] == 26
    assert review['second_audit']['changed'] == 17
    checkpoint = next(row for row in review['pending_cross_page_checks']
                      if row['id'] == 'Q035-036-FINAL-NUMERAL')
    already_applied = checkpoint['status'] == 'comparison completed; doubt retained'
    assert checkpoint['status'] in ('pending','comparison completed; doubt retained')
    comparison = (
        'Root compared the final scan035 numeral with scan036’s clear 6 in 10×2×6=120, '
        'the two occurrences of 15, and the final foliation 35. The clear 6 shares the '
        'closed lower loop and rising stem; the sampled 5s have a separate upper bar '
        'and open angular middle. This supports favored 6 without settling every cursive '
        'variant, so the final reading remains 6|5.')
    notes = {row['id']: row for row in review['notes']}
    old_pending = ('A numeral-form comparison with scan 036 remains queued before final freeze; '
                   'this implementation did not inspect 036.')
    if old_pending in notes['S035-04']['text']:
        notes['S035-04']['text'] = notes['S035-04']['text'].replace(
            old_pending, 'The numeral-form comparison is completed with doubt retained. '+comparison, 1)
    else:
        assert comparison in notes['S035-04']['text']
    notes['N035-NUMERAL-CHECK'].update(kind='completed comparison', text=(
        'Comparison completed; doubt retained. '+comparison+' The expected odd fixed count '
        'does not override the ink, and neither transcription nor audited adjudication changes.'))
    hand = next(row for row in review['hand_log'] if row.get('form') == '5/6')
    hand.update(pages=[35,36], observation=comparison,
                holds_at_every_observed_occurrence=False,
                witness_effect='The root comparison supports favored 6; the reading 6|5 and all audited finals remain unchanged.',
                habit='5/6: '+comparison)
    checkpoint.update(status='comparison completed; doubt retained', completed_by='root',
        compared_samples=['scan036: 6 in 10×2×6=120','scan036: both occurrences of 15','scan036: final foliation35'],
        outcome=comparison,
        limitation='The sampled forms do not settle every cursive variant. The expected odd count does not decide the stroke.')
    # Refresh the two textual mirrors of the pending marker; their readings and
    # the actual second_audit record remain unchanged.
    notation = next(row for row in review['notation'] if row.get('form') == r'\unsure{6|5}')
    notation['caution'] = 'Root favors 6; the scan036 comparison is completed, with 6|5 retained under doubt.'
    old_marker = 'The scan 036 numeral-form comparison remains pending.'
    new_marker = 'The scan 036 numeral-form comparison is completed; 6|5 remains under doubt.'
    main = review['main_reader_review']
    if old_marker in main['adjudication']:
        main['adjudication'] = main['adjudication'].replace(old_marker, new_marker, 1)
    else:
        assert new_marker in main['adjudication']
    assert before['second_audit'] == review['second_audit']
    for key in set(review)-{'notes','hand_log','pending_cross_page_checks','notation','main_reader_review'}:
        assert review[key] == before[key], key
    for old, new in zip(before['notation'], review['notation']):
        assert {k:v for k,v in old.items() if k != 'caution'} == {k:v for k,v in new.items() if k != 'caution'}
    assert {k:v for k,v in before['main_reader_review'].items() if k != 'adjudication'} == {
        k:v for k,v in review['main_reader_review'].items() if k != 'adjudication'}
    changed = review != before
    if changed:
        temporary = review_file.with_name(review_file.name+'.tmp')
        with temporary.open('w', encoding='utf-8', newline='') as stream:
            stream.write(json.dumps(review, ensure_ascii=False, indent=2)+'\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, review_file)
    assert all(sha(path) == hashes[str(path)] for path in protected)
    return dict(scan=35, comparison='completed; doubt retained', reading=r'\unsure{6|5}',
        already_applied=already_applied, review_metadata_written=changed,
        protected_page_adjudications_and_tsvs_unchanged=True, recorded_audit_unchanged=True,
        images_read=False, shared_outputs_touched=False)
