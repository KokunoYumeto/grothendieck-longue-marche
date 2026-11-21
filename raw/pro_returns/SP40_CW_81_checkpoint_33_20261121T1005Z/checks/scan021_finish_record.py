#!/usr/bin/env python3
"""Bind scan021's root-selected record to the frozen selected source and map.

Source indexing, exact offsets, hashes and record bookkeeping only.
Original reader files and all image material remain untouched.
"""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
from scan021_prepare_sources import span

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda name: json.loads((OUT / name).read_text())
r = load('scan021_record_draft.json')
u = load('scan021_source_union.json')
m = load('scan021_final_source_map.json')
draft_path = OUT / 'scan021_final_draft.tex'
draft = draft_path.read_text()
draft_sha = sha(draft_path)
map_sha = sha(OUT / 'scan021_final_source_map.json')
prior_record_sha = sha(OUT / 'scan021_record_draft.json')
JP = 'out/checks/scan021_main_decisions.md'
J = (BASE / JP).read_text()
assert draft_sha == m['draft_sha256_utf8'] == m['final_sha256'] == m['final_sha256_utf8']
assert sha(BASE / JP) == r['root_journal']['sha256'] == m['root_journal'].get('sha256', m['root_journal'].get('sha256_utf8'))
assert set(m['attachments_by_decision']) == {d['id'] for d in r['decisions']}
assert len(r['decisions']) == 71 and len(r['doubts']) == 39


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def attachment(a):
    value = copy.deepcopy(a)
    assert a['path'] == 'checks/scan021_final_draft.tex'
    assert a['workspace_path'] == 'out/checks/scan021_final_draft.tex'
    assert (BASE / a['workspace_path']).resolve() == (BASE / 'out' / a['path']).resolve()
    assert draft[a['char_start']:a['char_end']] == a['excerpt']
    assert hashlib.sha256(a['excerpt'].encode()).hexdigest() == a['literal_sha256_utf8']
    assert a['draft_sha256_utf8'] == draft_sha
    value['source_map_original_path'] = a['workspace_path']
    value['source_map_manifest'] = a.get('workspace_manifest_path')
    value['source_map_sha256'] = map_sha
    return value


def attachments(values):
    return [attachment(a) for a in values]


def section(number):
    match = re.search(r'^## ' + f'{number:02d}' + r'\b[^\n]*', J, re.M)
    assert match, number
    nxt = re.search(r'^## ', J[match.end():], re.M)
    end = match.end() + nxt.start() if nxt else len(J)
    return span(JP, J, match.start(), end, section=number, source_sha256_utf8=sha(BASE / JP))


def exact_final(literal, label, occurrence=0):
    found = list(re.finditer(re.escape(literal), draft))
    assert len(found) > occurrence, (label, literal)
    match = found[occurrence]
    a = span('checks/scan021_final_draft.tex', draft, match.start(), match.end())
    a.update(workspace_path='out/checks/scan021_final_draft.tex', manifest='checks/scan021_final_source_map.json',
             workspace_manifest_path='out/checks/scan021_final_source_map.json', draft_sha256_utf8=draft_sha,
             final_file_sha256=draft_sha, body_sha256=draft_sha,
             byte_start=len(draft[:match.start()].encode()), byte_end=len(draft[:match.end()].encode()),
             attachment_id=label)
    return attachment(a)


def unique_attachments(values):
    seen = set()
    out = []
    for value in values:
        key = (value['path'], value['char_start'], value['char_end'])
        if key not in seen:
            seen.add(key)
            out.append(copy.deepcopy(value))
    return out


by = {d['id']: d for d in r['decisions']}
groups = {g['id']: g for g in m['selected_groups']}
for d in r['decisions']:
    d['source_locus_id'] = 'SRC021-' + d['id']
    d['final_source_attachment'] = attachments(m['attachments_by_decision'][d['id']])
    d['actual_final_group_ids'] = [g['id'] for g in m['selected_groups'] if d['id'] in g['decision_ids']]
    d['root_source_attachment_status'] = 'Exact selected-source offsets bound; final root approval remains pending.'
    d['count_status'] = 'Root-journal physical count copied exactly; original reader counts remain separate provenance.'
    d['main_approved'] = False
for q in r['doubts']:
    q['source_locus_id'] = by[q['decision_id']]['source_locus_id']
    q['final_source_attachment'] = copy.deepcopy(by[q['decision_id']]['final_source_attachment'])
    q['main_approved'] = False


def decision_attachments(numbers):
    return unique_attachments([a for n in numbers for a in by[f'L021-{n:02d}']['final_source_attachment']])


def decision_ids(numbers):
    return [f'L021-{n:02d}' for n in numbers]


# Original report doubts preserve their actual identity/pointer and independent outcome.
role_numbers = dict(zip(
    ['A021G01','A021G02','A021G03','A021G04','A021G05','A021G07','A021G08','A021G09','A021G10',
     'A021G12','A021G13','A021G14','A021G15','A021G16','A021G17','A021D01','A021D02','A021D03','A021D04'],
    [4,5,6,7,16,23,26,27,42,43,48,49,55,64,66,33,34,35,36]))
canonical_decisions = {d['source_C_doubt_rows'][0]: d['id'] for d in r['decisions'] if d['source_C_doubt_rows']}
b_extra_doubts = {1:10,10:56,11:57,12:24,13:37,14:53}
doubt_coverage = {reader: [] for reader in 'ABC'}
for reader in 'ABC':
    for ordinal, raw in enumerate(u['reader_sources'][reader]['raw_rows']['doubts']):
        value = raw['value']
        if reader == 'A' and value['id'].endswith('-role'):
            dids = decision_ids([role_numbers[value['location']]])
        elif reader == 'B':
            dids = [canonical_decisions[value['C_source_row']]] if value.get('C_source_row') else decision_ids([b_extra_doubts[ordinal]])
        else:
            identity = value.get('difference_id', value.get('id'))
            dids = r['original_reader_difference_coverage'][reader][identity]['root_decision_ids']
        assert dids, (reader, ordinal)
        doubt_coverage[reader].append(dict(original_identity=value.get('id', value.get('difference_id', raw['source']['pointer'])),
            original_source=copy.deepcopy(raw['source']), original_value=copy.deepcopy(value), root_decision_ids=dids,
            selected_remaining_doubt_ids=[did for did in dids if by[did]['remaining_doubt']],
            final_source_attachment=unique_attachments([a for did in dids for a in by[did]['final_source_attachment']]),
            scope='The original independent doubt and its exact source are retained; the selected outcome follows the attached root decision.'))
r['original_reader_doubt_coverage'] = doubt_coverage

# Twenty-one canonical inventory scopes use the completed selected state.
base_specs = [
    ('opening', "Soit alpha0 in K1; je dis que l'on a | on a; no endpoint colon", [1,2,71]),
    ('upper pair of equalities', 'Two empty intersections joined by literal i.e; first roofed Sigma has no raised plus; four local upper-run roles qualified', [3,4,5,6,7,8,71]),
    ('before first union', '(ce qui achèvera with grave/acute/no-accent alternatives; dèmonstration with grave/acute/no-accent alternatives, car on aura', [9,10,11]),
    ('upper union and right conditions', 'U = X setminus union of roofed Sigma-alpha-plus; K = qualified K1 union {i}; complete pointed brace and cancelled lower group', [12,13,14,15,16,17]),
    ('under the upper K condition', 'Qualified cancelled Sigma-alpha, surviving glyph/index strokes and all selected zigzag crossings', [14,15]),
    ('under upper union', 'comme dans le lemme.', [71]),
    ('Or proof lead-in', 'Or qualified complete comme / deleted-co-plus-mme / deleted-co-plus-comme / deleted-car-plus-comme group, on a; no endpoint colon', [18,19,20]),
    ('central first inclusion', 'E_i subset U_{J,i} = X setminus the literal cup and high transverse run, with roofed Sigma-alpha-plus and qualified detached point/continuation', [21,22,23,24]),
    ('before second inclusion', 'cela implique que', [67]),
    ('central second inclusion', 'E_i subset X setminus roofed Sigma-alpha0-plus = Sigma with qualified alpha0/alpha index and raised minus', [25,26,27]),
    ('separate lead-in immediately left of marginal diagram', 'Complete qualified j:e. / j.e. / i:e. / i.e. lead-in with its two middle points', [28,29]),
    ('middle-right diagram, five upright rows and two sideways labels', 'Complete two-brace diagram: top Sigma_i+ ou Sigma_i-, E_i, qualified third Sigma/index group, E_alpha, Sigma_alpha0+; two sideways signed Sigma labels and resolved upright shaft-and-point sign', list(range(30,41))),
    ('below central inclusion', "d'autre part alpha0 in K1 signifie | signifi", [41]),
    ('lower-middle exclusion', 'Complete Sigma-alpha0-plus, literal crossed-inclusion relation, Sigma-i-plus; both local upper-run roles qualified', [42,43,44]),
    ('conclusion of proof', 'ce qui, qualified cancelled impli/impl., live signifie aussi que, empty intersection and cqfd.', [45,46,47,48,49,50]),
    ('after ce qui', 'Qualified cancelled impli / impl., complete letter-body and both transverse cancellation runs', [45,46]),
    ('corollary heading and first body line', 'Underlined Corollaire du lemme; Pour une classe; V de complete Pi_I with qualified circle/zero exponent, son expression', [51,52,53,71]),
    ('corollary expression', 'V = X setminus union over alpha in K of roofed Sigma-alpha-plus; separate pale left union return and qualified Sigma upper-run role', [54,55]),
    ('corollary prose above final brace', 'du lemme pr(ê|é|e)c(é|è|e)dent est underlined unique, separate dash, on a', [56,57,58]),
    ('bottom two conditions and brace geometry', 'K set condition with bar V and dot V; complete three-brace geometry; Sigma-alpha-plus est l’unique comp. de X setminus Sigma-alpha contenue dans X setminus V', list(range(59,67))),
    ('bottom-right corrected E-alpha', 'Resolved earlier V overlapped by the live E-alpha; complete original strokes with no additional strike', [59]),
]
inventory = []
inventory_by_key = {}
raw_c = [item for item in u['candidate_inventory'] if item['reader'] == 'witness C']
assert len(raw_c) == len(base_specs) == 21
for ordinal, (position, label, numbers) in enumerate(base_specs, 1):
    key = f'021.{ordinal:02d}'
    raw = raw_c[ordinal-1]
    assert raw['value']['element'] == key
    item = dict(scan=21, sheet_kind='text', hand='his hand', element=key, kind=raw['value']['kind'],
        position=position, first_words_or_objects=label, transcribed='yes', selected=True, main_approved=False,
        source_inventory_group=key, original_C_inventory_identities=[key], source_rows=[],
        related_decision_ids=decision_ids(numbers), final_source_attachment=attachments(m['original_inventory_source_attachments'][key]),
        root_decision_sources=[copy.deepcopy(by[did]['root_evidence_source']) for did in decision_ids(numbers)],
        root_inventory_authorization=section(25),
        scope='Selected manuscript scope; nested graphical entries reference these same final occurrences. Separate small traces retain their own undetermined-hand entries.',
        selection_status='Completed selected source; final root approval pending.')
    inventory.append(item)
    inventory_by_key[key] = item

# Complete selected graphical groups retain their selected scope, syntax and literal pieces.
graphic_specs = {
 'C021-G01': ('display','first pair of intersections','Complete first display; four literal Sigma groups, selected i.e and formula companions'),
 'C021-G01a': ('drawing','first roofed Sigma','Complete roofed Sigma-alpha0, no raised plus; first printed short-head-role qualifier'),
 'C021-G02': ('display','upper U display and K condition','Complete upper display, selected Sigma, qualified K state, pointed brace, cancelled group and separate pale traces'),
 'C021-G02a': ('drawing','second K in K condition','Complete K with qualified head/retrace or deleted-I predecessor state'),
 'C021-M01': ('drawing','between upper prose and union','Qualified two interrupted pale runs; role, hand and surface origin undetermined'),
 'A021G05': ('drawing','upper U expression','Complete roofed Sigma-alpha-plus; local head/retrace or independent upper-rule role retained'),
 'B021-G02-cancelled-Sigma': ('deletion','under upper K condition','Complete qualified cancelled Sigma-alpha with its actual glyph and zigzag crossing paths'),
 'B021-G03': ('drawing','word cluster following Or','Complete qualified comme/cancelled-prefix state group; adjoining Or and on a remain outside this group'),
 'C021-M02': ('drawing','left margin beside central inclusion','Qualified detached oblique trace; role, hand and surface origin undetermined'),
 'C021-G03': ('display','central first inclusion','Complete inclusion, literal cup with high transverse run, roofed Sigma and detached point with pale continuation'),
 'C021-M03': ('drawing','below-left of central roof','Qualified point and pale lower continuation, represented once; role, hand and attachment undetermined'),
 'C021-G04': ('display','central second inclusion','Complete inclusion with roofed Sigma-alpha0-plus and signed Sigma with literal qualified alpha0/alpha index'),
 'B021-G05-index': ('drawing','right index of central second inclusion','Complete qualified alpha0/alpha index curl, shared terminal stroke once'),
 'A021G20': ('drawing','separate marginal lead-in','Complete qualified j:e./j.e./i:e./i.e. lead-in; diagram outside'),
 'A021DG': ('diagram','middle-right margin','Completed five-row diagram with six Sigma labels, both braces, resolved shaft-and-point sign and qualified detached pale trace; lead-in outside'),
 'A021D01': ('drawing','top-left upright marginal Sigma','Complete Sigma-i-plus with locally retained upper-run-role doubt'),
 'A021D02': ('drawing','top-right upright marginal Sigma','Complete Sigma-i-minus with locally retained upper-run-role doubt'),
 'B021-G06-middle-row': ('drawing','third upright marginal row','Complete qualified Sigma_i-alpha / Sigma_i-comma-alpha / Sigma_dotted-alpha group; shared hook and detached point once'),
 'A021D04': ('drawing','bottom upright marginal row','Complete Sigma-alpha0-plus with locally retained upper-run-role doubt'),
 'A021D05': ('drawing','between sideways marginal labels','Resolved literal upright shaft-and-point shape; no mathematical function assigned'),
 'A021M04': ('drawing','below outer marginal brace','Qualified detached pale run; connection, role, hand and surface origin undetermined'),
 'A021G10': ('drawing','left Sigma in exclusion','Complete Sigma-alpha0-plus with locally retained upper-run-role doubt'),
 'A021G11': ('drawing','crossed-inclusion relation','Complete curved inclusion and long crossing stroke; adjoining Sigmas outside'),
 'A021G12': ('drawing','right Sigma in exclusion','Complete Sigma-i-plus with separate dark and pale upper pieces; local upper-run-role doubt retained'),
 'B021-G08': ('deletion','cancelled word after ce qui','Complete qualified impli/impl. letter-body and both transverse cancellation runs; live signifie outside'),
 'C021-G08': ('display','concluding empty intersection','Complete Sigma-i-plus and Sigma-alpha-plus with integrated lower index strokes and locally retained upper-run-role doubts'),
 'C021-G09': ('drawing','corollary body after its heading','Completed corollary body with distinct selected Pi, pale traces, rule, expression, prose, brace components and corrected V/E state'),
 'C021-M05': ('drawing','above first corollary V','Qualified detached pale upright; V remains outside the point-only group'),
 'C021-M06': ('drawing','left of corollary rule','Qualified detached point; role, hand and surface origin undetermined'),
 'A021G22': ('drawing','Pi in corollary first body line','Complete Pi, pale broken head, interrupted right stem, lower I and qualified raised circle/zero'),
 'C021-G09a': ('drawing','corollary union','Complete cup and separate pale left return; existing union reading retained'),
 'A021G15': ('drawing','Sigma in corollary V expression','Complete roofed Sigma-alpha-plus with locally retained upper-run-role doubt'),
 'C021-G09b': ('deletion','bottom-right E-alpha','Resolved V predecessor under live E-alpha with complete overlap and no added strike'),
 'B021-G10-set-open': ('drawing','opening brace of bottom set','Complete literal opening set brace, component of the one bottom-geometry parent'),
 'B021-G10-set-close': ('drawing','closing brace of bottom set','Complete literal right closing set brace, component of the one bottom-geometry parent'),
 'A021G25-selected-path': ('drawing','left side of corollary','Complete bowed side-rule path, lower endpoint before physical paper boundary; adjacent words outside'),
}
assert set(graphic_specs) == set(groups)
undetermined = {'C021-M01','C021-M02','C021-M03','A021M04','C021-M05','C021-M06'}
for ordinal, group in enumerate(m['selected_groups'], 1):
    key = group['id']
    kind, position, label = graphic_specs[key]
    item = dict(scan=21, sheet_kind='text', hand='undetermined hand' if key in undetermined else 'his hand',
        element=f'021.G{ordinal:02d}', kind=kind, position=position, first_words_or_objects=label,
        transcribed='yes', selected=True, main_approved=False, source_inventory_group=key, source_rows=[],
        selected_source_group=key, selected_group_source=copy.deepcopy(group['source']),
        selected_group_source_pieces=copy.deepcopy(group['exact_source_pieces']),
        literal_graphical_components=copy.deepcopy(group['literal_components']),
        related_decision_ids=copy.deepcopy(group['decision_ids']),
        final_source_attachment=attachments(m['selected_graphic_inventory_source_attachments'][key]),
        root_decision_sources=[copy.deepcopy(by[did]['root_evidence_source']) for did in group['decision_ids']],
        root_inventory_authorization=section(25),
        scope='This entry references one actual selected group. Lexical parents and children share the same final occurrence; each literal component receives one owner in selected_literal_component_ownership.',
        hand_scope='Independent small-trace hand/role qualifications remain in their own nested entries.' if key not in undetermined else 'Undetermined, following the local root journal; no hand or character supplied.',
        selection_status='Completed selected source; final root approval pending.')
    inventory.append(item)
    inventory_by_key[key] = item
archive = dict(scan=21, sheet_kind='text', hand='undetermined hand', element='021.ARCHIVE', kind='text',
    position='bottom-left archive number', first_words_or_objects='20, retained only as an archive-sheet source comment',
    transcribed='yes', selected=True, main_approved=False, source_inventory_group='ARCHIVE', source_rows=[],
    related_decision_ids=['L021-71'], root_inventory_authorization=section(25),
    final_source_attachment=attachments(m['archive_inventory_source_attachment']),
    representation='comment only: % archive sheet number: 20', selection_status='Completed selected comment; final root approval pending.')
inventory.append(archive)
inventory_by_key['ARCHIVE'] = archive

# Every independent original inventory row is linked by its actual identity.
a_graphics = {
 'A021G01':(['C021-G01a'],[4,8]), 'A021G02':(['C021-G01'],[5]), 'A021G03':(['C021-G01'],[6]),
 'A021G04':(['C021-G01'],[7]), 'A021G05':(['A021G05'],[16]), 'A021G06':(['C021-G03'],[22]),
 'A021G07':(['C021-G03','C021-M03'],[23,24]), 'A021G08':(['C021-G04'],[26]),
 'A021G09':(['C021-G04','B021-G05-index'],[25,27]), 'A021G10':(['A021G10'],[42]),
 'A021G11':(['A021G11'],[44]), 'A021G12':(['A021G12'],[43]), 'A021G13':(['C021-G08'],[48]),
 'A021G14':(['C021-G08'],[49]), 'A021G15':(['A021G15'],[55]), 'A021G16':(['C021-G09'],[64]),
 'A021G17':(['C021-G09'],[65,66]), 'A021G19':(['B021-G02-cancelled-Sigma'],[14,15]),
 'A021G18':(['C021-G02'],[12,13,14,15]), 'A021M01':(['C021-M01'],[17]), 'A021M02':(['C021-M02'],[21]),
 'A021G20':(['A021G20'],[28,29]), 'A021G21':(['B021-G08'],[45,46]), 'A021G22':(['A021G22'],[51,52]),
 'A021M03':(['C021-M05'],[53]), 'A021G23':(['C021-G09b'],[59]), 'A021G24':(['C021-G09'],[60,61]),
 'A021G25':(['A021G25-selected-path'],[68]), 'A021D03':(['B021-G06-middle-row'],[31,35]),
 'A021D01':(['A021D01'],[33]), 'A021D02':(['A021D02'],[34]), 'A021D04':(['A021D04'],[36]),
 'A021D05':(['A021D05'],[32]), 'A021M04':(['A021M04'],[37]), 'A021DG':(['A021DG'],list(range(30,41))),
}
b_extra_inventory = {
 17:(['021.15','C021-G08'],[48,49,50]), 18:(['021.17'],[71]), 19:(['021.17','A021G22'],[51,52,53]),
 20:(['021.18'],[54,55]), 21:(['021.19'],[56,57,58]), 22:(['021.20'],list(range(59,67))),
 23:(['021.21'],[59]), 24:(['C021-G02'],[12]), 25:(['C021-G03'],[22]), 26:(['C021-M03'],[24]),
 27:(['A021M04'],[37]), 28:(['C021-M05'],[53]), 29:(['A021G25-selected-path'],[68]),
 30:(['021.17','021.19'],[58,71]), 31:(['C021-G09','B021-G10-set-open','B021-G10-set-close'],[60,61,62,63]),
 32:(['ARCHIVE'],[71]),
}
c_extra_inventory = {
 '021.C.23':(['C021-G02'],[12]), '021.C.24':(['A021G25-selected-path'],[68]),
 '021.C.25':(['C021-G09'],[60,61]), '021.C.26':(['C021-G09a'],[54]), '021.C.27':(['C021-G02a'],[13]),
 '021.C.28':(['C021-G01a'],[4]), '021.C.29':(['C021-G01'],[5]), '021.C.30':(['C021-G01'],[6]),
 '021.C.31':(['C021-G01'],[7]), '021.C.32':(['C021-G03'],[23]), '021.C.33':(['C021-G04'],[26]),
 '021.C.34':(['C021-G04','B021-G05-index'],[25,27]), '021.C.35':(['A021G10'],[42]),
 '021.C.36':(['A021G12'],[43]), '021.C.37':(['C021-G08'],[48]), '021.C.38':(['C021-G08'],[49]),
 '021.C.39':(['A021D01'],[33]), '021.C.40':(['A021D02'],[34]), '021.C.41':(['B021-G06-middle-row'],[31,35]),
 '021.C.42':(['A021D04'],[36]), '021.C.43':(['C021-G09'],[64]), '021.C.44':(['C021-G09'],[65,66]),
 '021.C.M01':(['C021-M01'],[17]), '021.C.M02':(['C021-M02'],[21]), '021.C.M03':(['C021-M03'],[24]),
 '021.C.M04':(['A021M04'],[37]), '021.C.M05':(['C021-M05'],[53]), '021.C.M06':(['C021-M06'],[69]),
 '021.C.archive':(['ARCHIVE'],[71]),
}
inventory_coverage = []
for raw in u['candidate_inventory']:
    reader, value = raw['reader'], raw['value']
    element = value['element']
    if reader == 'witness C' or (reader == 'A' and value.get('provenance_original_element')):
        key = element if reader == 'witness C' else value['provenance_original_element']
        keys, numbers = [key], base_specs[int(key.split('.')[-1])-1][2]
        final = copy.deepcopy(inventory_by_key[key]['final_source_attachment'])
    elif reader == 'A':
        keys, numbers = (['ARCHIVE'],[71]) if element == 'A021-archive' else a_graphics[element]
        final = copy.deepcopy(archive['final_source_attachment']) if keys == ['ARCHIVE'] else decision_attachments(numbers)
    elif reader == 'B':
        ordinal = int(element.split('.')[-1])
        keys, numbers = ([f'021.{ordinal:02d}'], base_specs[ordinal-1][2]) if ordinal <= 16 else b_extra_inventory[ordinal]
        final = copy.deepcopy(inventory_by_key[keys[0]]['final_source_attachment']) if ordinal <= 16 or ordinal in [18,20,21,22,23,32] else decision_attachments(numbers)
    elif reader == 'C':
        if value.get('source_C_element'):
            key = value['source_C_element']
            keys, numbers = [key], base_specs[int(key.split('.')[-1])-1][2]
            final = copy.deepcopy(inventory_by_key[key]['final_source_attachment'])
        else:
            keys, numbers = c_extra_inventory[element]
            final = copy.deepcopy(archive['final_source_attachment']) if keys == ['ARCHIVE'] else decision_attachments(numbers)
    else:
        raise AssertionError(reader)
    entry = dict(reader=reader, original_element=element, original_source=copy.deepcopy(raw['source']),
        original_value=copy.deepcopy(value), selected_inventory_elements=[inventory_by_key[key]['element'] for key in keys],
        root_decision_ids=decision_ids(numbers), final_source_attachment=final,
        scope='Original inventory wording and scope preserved; selected entries and exact attachments identify the completed represented locus.')
    inventory_coverage.append(entry)
    for key in keys:
        inventory_by_key[key]['source_rows'].append(dict(reader=reader, value=copy.deepcopy(value), source=copy.deepcopy(raw['source'])))
assert len(inventory_coverage) == 161
assert len({(x['reader'],x['original_source']['path'],x['original_source']['pointer']) for x in inventory_coverage}) == 161

# Literal commands nested in parent groups retain one owner at their deepest selected scope.
component_candidates = {}
for group in m['selected_groups']:
    for component in group['literal_components']:
        a = component['final_source_attachment']
        key = (a['char_start'], a['char_end'])
        component_candidates.setdefault(key, []).append((group, component))
ownership = []
for ordinal, (key, candidates) in enumerate(sorted(component_candidates.items()), 1):
    group, component = min(candidates, key=lambda pair: pair[0]['final_source_attachment']['char_end'] - pair[0]['final_source_attachment']['char_start'])
    identity = f'LIT021-{ordinal:03d}'
    owner = inventory_by_key[group['id']]
    owner.setdefault('owned_literal_component_ids', []).append(identity)
    a = component['final_source_attachment']
    ownership.append(dict(id=identity, group_id=group['id'], inventory_element=owner['element'],
        final_source_attachment=attachment(a), exact_source_pieces=copy.deepcopy(component['exact_source_pieces']),
        referencing_group_ids=[item[0]['id'] for item in candidates],
        literal_command_kind=re.match(r'\s*\\([A-Za-z]+)', a['excerpt']).group(1),
        scope='One exact selected command occurrence; parent/context references use this same final span.'))
r['selected_literal_component_ownership'] = ownership
r['selected_literal_path_ownership'] = [copy.deepcopy(item) for item in ownership if item['literal_command_kind'] in ['draw','fill','filldraw']]
r['inventory'] = inventory
r['original_inventory_coverage'] = dict(raw_rows=161, actual_C_rows=21, reader_rows=140, selected_inventory_entries=len(inventory),
    all_original_identities_preserved=True, rows=inventory_coverage,
    scope='Twenty-one original C scopes, thirty-six completed selected graphical scopes and one archive comment. Shared source occurrences have one literal-command owner.')

# Original C row/part identities stay canonical; raw pending status is preserved separately.
for row in r['C_source_rows']:
    row['final_source_attachment'] = attachments(m['original_C_doubt_attachments'][row['source_id']])
    for part in row['source_parts']:
        part['final_source_attachment'] = attachments(m['original_C_doubt_part_attachments'][part['part_id']])
        part['main_approved'] = False
        assert part['decision_status'] == part['original_source_decision_status'] == 'pending ink adjudication'
        assert part['part_id'] == row['source_id'] + '-1'
assert Counter(row['root_original_row_status'] for row in r['C_source_rows']) == {'retained':9,'resolved':6}

# Current selected source coverage; raw reports and local complete TeX remain attached.
r['source_locus_coverage'] = [dict(source_locus_id=d['source_locus_id'], root_decision_ids=[d['id']],
    original_reader_difference_ids={reader:[row['value']['id'] for row in d['reader_provenance'][reader]['original_difference_rows']] for reader in 'ABC'},
    readers=copy.deepcopy(d['readers']), reader_provenance=copy.deepcopy(d['reader_provenance']),
    selected=True, main_approved=False, root_authorization=copy.deepcopy(d['root_authorization_sources']),
    final_source_attachment=copy.deepcopy(d['final_source_attachment'])) for d in r['decisions']]
for reader, rows in r['original_reader_difference_coverage'].items():
    for rid, entry in rows.items():
        entry['source_locus_ids'] = [by[did]['source_locus_id'] for did in entry['root_decision_ids']]
        entry['final_source_attachment'] = unique_attachments([a for did in entry['root_decision_ids'] for a in by[did]['final_source_attachment']])


def overlapping_decisions(reader, source):
    result = []
    for d in r['decisions']:
        if d['root_source_audit_choice_applied']:
            continue
        for local in d['reader_provenance'][reader]['actual_complete_tex_sources']:
            if local['path'] == source['path'] and max(local['char_start'], source['char_start']) < min(local['char_end'], source['char_end']):
                result.append(d['id'])
                break
    return result


r['original_graphical_group_coverage'] = []
for raw in u['candidate_graphical_groups']:
    dids = overlapping_decisions(raw['reader'], raw['tex_source'])
    assert dids, (raw['reader'],raw['group_id'])
    r['original_graphical_group_coverage'].append(dict(reader=raw['reader'], original_group_id=raw['group_id'],
        exact_original_tex_source=copy.deepcopy(raw['tex_source']), original_metadata_source=copy.deepcopy(raw['source']),
        overlapping_source_scope_decision_ids=dids,
        source_locus_ids=[by[did]['source_locus_id'] for did in dids],
        scope='Exact original group remains an independent candidate. Overlapping inspected TeX spans link to local source comparisons; the selected map records the actual final donor pieces.'))
r['original_report_silent_source_coverage'] = {reader:[] for reader in 'ABC'}
for reader in 'ABC':
    for ordinal, raw in enumerate(u['reader_sources'][reader]['reported_silent_choices_with_complete_TeX']):
        dids = overlapping_decisions(reader,raw['tex_source'])
        r['original_report_silent_source_coverage'][reader].append(dict(original_ordinal=ordinal,
            original_record=copy.deepcopy(raw), overlapping_local_source_decision_ids=dids,
            agreed_remainder_decision_id='L021-71',
            scope='The exact complete original source span supplies the actual reading. Its independent literal source is preserved even where no difference was reported.'))

r['selected_graphical_groups'] = copy.deepcopy(m['selected_groups'])
for group in r['selected_graphical_groups']:
    group['final_source_attachment'] = attachment(group['final_source_attachment'])
    group['main_approved'] = False
r['complete_selected_source_blocks'] = [dict(id=b['id'], final_source_attachment=attachment(b['final_source_attachment'])) for b in m['final_blocks']]

# Probable expansions are separate from the literal selected transcription.
abbreviation_anchors = {
 'i.e': [exact_final(r'\node at (1090,225) {i.e};','ABBR021-ie')],
 'i.e.': [exact_final(r'\node at (521,2281) {$K=\phantom{\{}\alpha\in I\mid\overline V\cap E_\alpha\ne\varnothing\quad\text{i.e.}\quad$};','ABBR021-ie-period')],
 'cqfd.': [exact_final('$, cqfd.','ABBR021-cqfd')],
 'comp.': [exact_final(r"\node at (663,2341) {est l'unique comp. de};",'ABBR021-comp')],
}
for entry in r['abbreviations']:
    entry.update(final_source_attachment=abbreviation_anchors[entry['form']], selected=True, main_approved=False,
        scope='Probable conventional expansion only in this table; the manuscript abbreviation remains literal in the selected source.')
r['unresolved_leadin_abbreviation_exclusion'] = dict(decision_id='L021-28', literal_primary='j:e.',
    complete_alternatives=['j.e.','i:e.','i.e.'], probable_expansion_supplied=False,
    root_authorization=section(25), final_source_attachment=copy.deepcopy(by['L021-28']['final_source_attachment']))

content = copy.deepcopy(m['attributed_content_note'])
content['selected_source_spans'] = attachments(content['selected_source_spans'])
content['source_support'] = [attachments(values) for values in content['source_support']]
content['main_approved'] = False
content['selected'] = True
content['statement_scope'] = 'Attributed manuscript assertions and written i.e passages; no mathematical proof or inference was checked.'
content['display_and_adjacent_prose_coverage'] = True
r['attributed_content_note'] = content
r['root_selected_content_note'] = dict(note=r['notes'], root_authorization=section(25),
    final_source_attachment=copy.deepcopy(content['selected_source_spans']) + unique_attachments([a for group in content['source_support'] for a in group]),
    selected=True, main_approved=False, mathematical_checks_performed=False)

root_audit = load('scan021_root_crop_audit.json')
r['root_ink_pass'] = dict(successful_crop_views=root_audit['total_distinct'], whole_scan_views=0, supplied_half_views=0,
    failed_unseen_delivery_events=copy.deepcopy(root_audit['failed_image_deliveries']),
    source='out/checks/scan021_root_crop_audit.json', audit_sha256=sha(OUT/'scan021_root_crop_audit.json'), clerk_image_views=0)
r['processing_provenance'].update(root_crop_audit=copy.deepcopy(root_audit),
    source_assembly_provenance=copy.deepcopy(m['processing_provenance']),
    assembly_audit=copy.deepcopy(m['assembly_audit']),
    bounded_assembly_source_repairs=copy.deepcopy(m.get('bounded_source_repairs',[])),
    original_record_draft_sha256_before_final_binding=prior_record_sha,
    final_binding_script=dict(path='out/checks/scan021_finish_record.py',sha256=sha(OUT/'scan021_finish_record.py')),
    optional_mathematical_or_coordinate_computations=0, no_coordinate_or_mathematical_event_rerun=True)
processing_path = OUT/'scan021_root_processing.md'
if processing_path.exists():
    r['processing_provenance']['root_processing_source'] = dict(path='out/checks/scan021_root_processing.md',sha256=sha(processing_path))
r['selected_draft'] = dict(path='checks/scan021_final_draft.tex',workspace_path='out/checks/scan021_final_draft.tex',sha256=draft_sha)
r['selected_source_map'] = dict(path='checks/scan021_final_source_map.json',workspace_path='out/checks/scan021_final_source_map.json',sha256=map_sha)
r['source_attachment_path_correspondence'] = dict(record_path='checks/scan021_final_draft.tex',record_base=str(BASE/'out'),
    original_map_path='out/checks/scan021_final_draft.tex',original_map_base=str(BASE),exact_absolute_target=str(draft_path),
    relation='Both declared base/path concatenations resolve to the identical selected file; exact offsets and bytes are preserved.')
r['S_public_audit'] = [dict(decision_id=d['id'],S_id=d['S_id'],S_status=d['S_status'],
    root_ink_choice_applied=d['root_ink_choice_applied'],root_source_audit_choice_applied=d['root_source_audit_choice_applied'])
    for d in r['decisions'] if d.get('S_id')]
r['counts'].update(status='Complete root-selected readings and exact attachments; final source audit and root approval pending.',
    inventory_elements=len(inventory), decision_rows=len(r['decisions']), root_ink_entries=69, source_audit_entries=2, check_events=0)
r.update(root_ink_decision_entries=69,root_source_audit_entries=2,root_approved_decision_entries=0,
    root_approval_status='All selected choices, inventory, doubts and exact attachments recorded; final root approval pending.',
    source_attachment_status='Bound to frozen selected draft/map; independent source audit and final root approval pending.',
    main_adjudicated=False,main_approved=False)
r['mechanical_verification'] = dict(scope='Source-offset/hash and record bookkeeping only; no image, rendering, compilation, metric, coordinate or proof check.',
    all_ink_choices_supplied_by_root=True,all_public_reader_maps_complete=True,root_confidence_metadata_complete=True,
    selected_draft_and_map_sha256_bound=True,all_original_inventory_rows_mapped=True,all_original_reader_difference_rows_mapped=True,
    all_original_reader_doubt_rows_mapped=True,original_C_rows=15,source_primary_parts=15,
    final_targeted_source_QA='pending one independent frozen-bundle source pass')

# Bookkeeping completeness is checked without reinterpreting any source selection.
assert len(inventory) == 58
assert all(i['transcribed'] == 'yes' and i['final_source_attachment'] for i in inventory)
assert all(set(d['readers']) == set('ABC') and d['final_source_attachment'] for d in r['decisions'])
assert all(q['final_source_attachment'] for q in r['doubts'])
assert sum(d['diff_C'] for d in r['decisions']) == 45
assert sum(d['diff_H'] for d in r['decisions']) == 24
assert {w:dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_'+w])) for w in 'CH'} == {
    'C':{'high':4,'medium':8,'low':33},'H':{'high':5,'medium':8,'low':11}}
assert all(not d['main_approved'] for d in r['decisions'] + r['doubts'] + inventory)

write('scan021_attributed_content_note.json',content)
write('scan021_C_doubt_outcomes.json',dict(scan=21,original_catalog=u['canonical_C_catalog'],root_journal=r['root_journal'],
    counts=r['C_doubt_resolution_counts'],rows=r['C_source_rows'],main_adjudicated=False))
write('scan021_record_draft.json',r)
fingerprints = load('scan021_source_fingerprints.json')
prior_fingerprint_sha = sha(OUT/'scan021_source_fingerprints.json')
fingerprints.update(record_stage='Complete selected record frozen for independent source audit and final root review.',
    previous_preselection_manifest_sha256=prior_fingerprint_sha,
    selected_draft=dict(path='out/checks/scan021_final_draft.tex',sha256=draft_sha),
    selected_map=dict(path='out/checks/scan021_final_source_map.json',sha256=map_sha),
    prepared_files={name:dict(sha256=sha(OUT/name)) for name in ['scan021_record_draft.json','scan021_record_specs.json',
        'scan021_C_doubt_outcomes.json','scan021_attributed_content_note.json','scan021_finish_record.py']},
    root_journal=r['root_journal'],root_crop_audit_sha256=sha(OUT/'scan021_root_crop_audit.json'),root_approval_flags=False)
write('scan021_source_fingerprints.json',fingerprints)
print(json.dumps(dict(record_sha256=sha(OUT/'scan021_record_draft.json'),draft_sha256=draft_sha,map_sha256=map_sha,
    source_fingerprints_sha256=sha(OUT/'scan021_source_fingerprints.json'),counts=r['counts'],
    C_doubt_outcomes=r['C_doubt_resolution_counts'],original_reader_doubts={k:len(v) for k,v in doubt_coverage.items()},
    original_inventory_rows=len(inventory_coverage),selected_literal_components=len(ownership),
    selected_literal_path_commands=len(r['selected_literal_path_ownership']),current_selected_approval_flags=False),ensure_ascii=False))
