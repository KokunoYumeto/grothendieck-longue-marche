#!/usr/bin/env python3
"""Root-reviewed append-only notation closure and finite publication inverse."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out'
CHECKS = OUT / 'checks'
sha = lambda b: hashlib.sha256(b).hexdigest()
packed = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
full = lambda v: (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()

proof_path = CHECKS / 'notation026_root_final_review.json'
assert not proof_path.exists()
notation = OUT / 'notation.md'
before = notation.read_bytes()
assert sha(before) == 'b44f91d17fc787c80246d32a4f93473d053d85d7a27ac9d405525a49cc53922c'
focus_bytes = (CHECKS / 'notation026_new_assertions_v01.json').read_bytes()
assert sha(focus_bytes) == '16708619cece52654f3fec993aa066bfee267badc7b3f43489987e185211cc6b'
focus = json.loads(focus_bytes)
page_hashes = {str(p.relative_to(OUT)): sha(p.read_bytes()) for p in sorted((OUT / 'pages').glob('*.tex'))}
assert len(page_hashes) == 24
combined_before = sha((OUT / 'SP40_CW_81_transcription.tex').read_bytes())

# Root read the entire replay source and both constructors. Execute only the
# read-only prefix; its complete-byte comparisons cover the parent proof too.
replay_path = CHECKS / 'notation026_constructor_replay_v01.py'
source = replay_path.read_text()
assert source.count('\nproof = {') == 1
replay = {'__name__': '__root_notation_replay__'}
exec(source.split('\nproof = {', 1)[0], replay)
supplement = replay['supplement']
base = replay['namespace']['base']
assert len(supplement['rows']) == 91
assert len(supplement['sigma_complete_state_index']) == 39

# Every historical table row remains present in its prior order and bytes.
cursor = 0
for row in base['exact_notation_rows']:
    literal = row['source']['literal'].encode()
    at = before.find(literal, cursor)
    assert at >= cursor, row['id']
    cursor = at + len(literal)
assert len(base['exact_notation_rows']) == 180

def point(value, tokens):
    for token in tokens:
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value

def table_json(value):
    # JSON's exact Unicode escape supplies the table-safe spelling of U+007C.
    text = packed(value).replace('|', r'\u007c')
    assert packed(json.loads(text)) == packed(value)
    fence = '`' * (max([len(m.group()) for m in re.finditer(r'`+', text)] + [0]) + 1)
    return fence + ' ' + text + ' ' + fence

intro = '''

## Scan026 — complete notation bindings

The final page adds 91 local entries, including its 39 separately observed Sigma occurrences. Each entry below retains the exact selected reading-field order and links to the complete selected candidate object, its hand, role, attachment, qualification and parent/child scope. The first ordinary `ens.` has its own row; the later `ens` remains L002. These entries follow the recorded source-contract order. The page inventory separately records their physical order. [Source contract](checks/scan026_source_selected_contract_v01.json), [root observations](checks/scan026_root_journal.md), [complete supplemental values](checks/notation026_supplement_v01.json).

The reading column is an exact JSON array of the direct `reading`, `complete_reading` and `complete_base_reading` string fields, traversed in the original candidate and member order. The complete selected object is retained at the stated `/rows/N/selected_value_exact` pointer. The publication map replaces just those string fields with numbered slots and retains every other field and its order; filling the slots from the displayed array recovers each complete object byte for byte under the recorded JSON serialization. The table spelling `\\u007c` decodes to the original vertical bar. An empty array records the absence of a direct string under these three field names; the complete scoped parent remains at its stated pointer. [Exact publication map and inverse](checks/notation026_publication_inverse.json).

| Locus and root section | Exact ordered reading-field array | Complete selected value | Exact selected source groups |
| --- | --- | --- | --- |
'''
rows = []
inverse_rows = []
vectors = supplement['current_direct_reading_vectors']
for index, (row, vector) in enumerate(zip(supplement['rows'], vectors)):
    assert row['locus_id'] == vector['locus_id']
    original = row['selected_value_exact']
    carrier = copy.deepcopy(original)
    slots = []
    prefix = f'/rows/{index}/selected_value_exact'
    for slot, field in enumerate(vector['direct_reading_fields_in_original_order']):
        pointer = field['source_pointer']
        assert pointer.startswith(prefix)
        suffix = pointer[len(prefix):]
        tokens = [s.replace('~1', '/').replace('~0', '~') for s in suffix.split('/')[1:]]
        assert tokens
        assert point(original, tokens) == vector['literal_string_vector'][slot]
        parent = point(carrier, tokens[:-1])
        key = int(tokens[-1]) if isinstance(parent, list) else tokens[-1]
        parent[key] = {'notation_display_slot': slot}
        slots.append({'slot': slot, 'relative_json_pointer': suffix})
    restored = copy.deepcopy(carrier)
    for slot in slots:
        tokens = [s.replace('~1', '/').replace('~0', '~') for s in slot['relative_json_pointer'].split('/')[1:]]
        parent = point(restored, tokens[:-1])
        key = int(tokens[-1]) if isinstance(parent, list) else tokens[-1]
        assert parent[key] == {'notation_display_slot': slot['slot']}
        parent[key] = vector['literal_string_vector'][slot['slot']]
    assert full(restored) == full(original)
    sections = ', '.join('agreed archive number' if s is None else '§' + s for s in row['root_sections_exact'])
    cells = [row['id'] + '; ' + sections,
             table_json(vector['literal_string_vector']),
             f'`/rows/{index}/selected_value_exact` in [supplement](checks/notation026_supplement_v01.json)',
             table_json(row['selected_source_groups_exact'])]
    assert all(' | ' not in cell and '\n' not in cell for cell in cells)
    rows.append('| ' + ' | '.join(cells) + ' |\n')
    inverse_rows.append({'locus_id': row['locus_id'], 'supplement_pointer': prefix,
        'displayed_array_exact': vector['literal_string_vector'],
        'slots': slots, 'selected_value_with_numbered_slots': carrier,
        'complete_value_serialized_sha256': sha(full(original)),
        'complete_forward_and_inverse_byte_equal': True})
ordinary = supplement['ordinary_first_ens']
rows.append('| N026-TEXT-ENS-FIRST; §02 | ' + table_json([ordinary['literal']]) + ' | `/ordinary_first_ens` in [supplement](checks/notation026_supplement_v01.json) | Source characters 26–30; complete literal `ens.` |\n')

closure = '''

## Final comparison across all 24 pages

Root has completed the comparison of the 180 historical notation rows and the 91 scan026 local bindings against the recorded local crop decisions. The 14 recurring-form families retain their full original member lists and evidence. The exact retrieval pairs, all local candidate values, source spans and component scopes are preserved in the [final review bundle](checks/notation026_review_input_v01.json). Root accepts those existing local decisions throughout this final table; the page sources retain their complete recorded alternatives. [Root review and byte checks](checks/notation026_root_final_review.json).

For the recurring Sigma forms, every occurrence retains its own recorded head/body paths, indices, superscripts, cancellations and candidate-specific hand assignments. The final page's 39 Sigma entries refer to their complete arrays. The embedded diagram and paired-expression tables reconstruct all 96 and 16 complete component states, respectively, with their recorded inverse tuple maps. The source comment review verified 52 own candidate arrays: 21 contain the complete selected objects, and 31 recover those complete objects through the exact retained-field and omitted-field maps. [Source constructor proof](checks/notation026_constructor_replay_proof_v01.json), [embedded-table proof](checks/notation026_parent_literal_replay_proof_v01.json).

The explicit comparison of 91 ordered direct-reading vectors with the 11 historical one-line comment vectors records 1,001 first differing byte positions. Its domain and projection are stated in the review bundle. Root's reading decisions continue to be the ones recorded at the individual ink loci. The historical and final arrays, each complete object and all original member orders remain available through the exact maps.

The two public-report corrections NREV01 and NREV02 were applied at 2026-11-21 10:13:45.151195 UTC: two report fields for scan018 and 38 fields for scan021 now reproduce the already selected complete Pi0 and Sigma readings. Their before/after values and inverses are retained in the [exact report proposal](checks/notation_NREV01_NREV02_public_report_proposal_v01.json) and [root application](checks/final_readiness026_root_application.json). The earlier pending wording in the preparation snapshot records its earlier timestamp. All 24 page-file hashes remained unchanged through these report corrections and this notation closure.

The final review retains the local qualifications for unresolved ink and records no new mathematical proof claim. The dated source-verification events state the computations actually performed. The page statements in the reading notes remain attributed to their manuscript locations.
'''
appendix = (intro + ''.join(rows) + closure).encode()
after = before + appendix
assert after[:len(before)] == before and after[len(before):] == appendix
inverse_document = {'schema': 'notation026-publication-finite-inverse-v1',
    'serialization': 'UTF-8 json.dumps(value, ensure_ascii=False, indent=2) followed by one LF',
    'table_array_decoding': 'Remove only the counted Markdown code fence and its two padding spaces; json.loads decodes the array, including the exact U+007C spelling.',
    'slot_rule': 'For each explicit relative pointer, replace its exact numbered-slot object by the correspondingly indexed decoded table string. All remaining keys, values and ordering are retained in the carrier.',
    'rows': inverse_rows, 'ordinary_first_ens_exact': ordinary,
    'historical_prefix_bytes': len(before), 'historical_prefix_sha256': sha(before),
    'appendix_sha256': sha(appendix), 'complete_notation_sha256': sha(after),
    'all_91_complete_value_forward_inverse_checks_passed': True}
(CHECKS / 'notation026_publication_inverse.json').write_bytes(full(inverse_document))
(CHECKS / 'notation026_public_appendix.md').write_bytes(appendix)
(CHECKS / 'notation026_public_notation_before.md').write_bytes(before)
notation.write_bytes(after)
assert page_hashes == {str(p.relative_to(OUT)): sha(p.read_bytes()) for p in sorted((OUT / 'pages').glob('*.tex'))}
assert combined_before == sha((OUT / 'SP40_CW_81_transcription.tex').read_bytes())
when = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
proof = {'root_review_completed_utc': when,
    'scope': 'Root read all 11 focused projection chunks, manifest, inverse proof, complete constructor and parser sources, and parser/constructor replay certificates. Root had already read all 180 historical rows and 14 families, and all complete scan026 selected-state values. Root accepts the complete local states and cross-page source correspondences; the closed crop journals remain the ink authority.',
    'focused_review_sha256': sha(focus_bytes),
    'constructor_replay_source_sha256': sha(replay_path.read_bytes()),
    'root_in_memory_constructor_replay_bytes_equal': True,
    'root_in_memory_parent_proof_bytes_equal': True,
    'historical_rows': 180, 'historical_families': 14, 'new_local_rows': 91,
    'new_sigma_rows': 39, 'separate_ordinary_ens_row': 1,
    'complete_publication_inverse_models_verified': 91,
    'public_appendix_sha256': sha(appendix), 'notation_before_sha256': sha(before),
    'notation_after_sha256': sha(after),
    'historical_prefix_byte_exact': True, 'historical_row_order_exact': True,
    'all_page_hashes_unchanged': page_hashes, 'combined_sha256_unchanged': combined_before,
    'images_opened': 0, 'new_ink_decisions': 0, 'new_mathematical_proof_claims': 0,
    'source_files_changed': [], 'report_corrections_already_applied': ['NREV01', 'NREV02']}
proof_path.write_bytes(full(proof))
events_path = CHECKS / 'global_check_events.json'
events = json.loads(events_path.read_bytes())
new_events = [
 {'statement_id': 'SP40-FINAL-ASSESSMENT-SOURCE-CLOSURE', 'date': when,
  'who': '/root; GPT-6 Astra Pro; inherited effort setting not separately exposed; apply_final_assessments026.py',
  'type': 'computation or formal certificate',
  'outcome': 'The executed finite source check verified all 190 exact authority references for 42 assessment sentences, every proposed occurrence, both complete four-operation document forward/inverse maps, both heading-only brief maps, and unchanged bytes for all 24 page files and the combined transcription. The exact map and scope are checks/scan026_root_final_assessment_application.json. This records source attribution and byte checks; no manuscript proof was performed.'},
 {'statement_id': 'SP40-FINAL-NOTATION-SOURCE-CLOSURE', 'date': when,
  'who': '/root; GPT-6 Astra Pro; inherited effort setting not separately exposed; close_notation026.py',
  'type': 'computation or formal certificate',
  'outcome': 'Root executed the reviewed finite constructors in memory and reproduced the complete supplement, embedded-parent proof and review bundle byte for byte. The publication inverse recovered all 91 complete selected values. The 180 historical rows retained their original bytes and order; all 24 page hashes and the combined transcription hash remained unchanged. The exact scopes, maps, 39 Sigma arrays, 52 candidate-comment comparisons and 1001 vector comparisons are preserved in checks/notation026_root_final_review.json and its referenced files. The closed local crop decisions remain the ink authority; this event adds no manuscript theorem check.'}]
assert not ({e['statement_id'] for e in events} & {e['statement_id'] for e in new_events})
events_path.write_bytes(full(events + new_events))
with (OUT / 'progress.log').open('a') as stream:
    stream.write('final cross-page notation review complete ' + when + '\n')
print(json.dumps({'root_review': str(proof_path), 'notation_bytes': len(after),
    'notation_sha256': sha(after), 'historical_rows_unchanged': 180,
    'new_local_rows': 91, 'separate_ordinary_row': 1,
    'complete_inverses_verified': 91, 'new_source_check_events': 2,
    'all_page_and_combined_hashes_unchanged': True}, indent=2))
