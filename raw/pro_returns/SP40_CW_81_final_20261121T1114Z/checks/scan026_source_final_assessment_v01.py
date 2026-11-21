#!/usr/bin/env python3
"""Isolated final-assessment proposal; reads text only and writes its own prefix.

The existing assessments, records, briefs, journals and global reports are inputs.
No global file, reading, classification, approval, or check-event list is changed.
"""
from pathlib import Path
from collections import Counter
import csv
import difflib
import hashlib
import io
import json
import re

BASE = Path(__file__).resolve().parents[2]
CHECKS = BASE / 'out/checks'
PREFIX = 'scan026_source_final_assessment_'
inputs = {}
claim_specs = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def raw(p):
    assert Path(p).suffix.lower() not in {'.jpg', '.jpeg', '.png', '.pdf', '.tif'}
    if p not in inputs:
        inputs[p] = (BASE / p).read_bytes()
    return inputs[p]


def text(p):
    return raw(p).decode('utf-8')


def load(p):
    return json.loads(raw(p))


def packed(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':')).encode()


def at(obj, ptr):
    if not ptr:
        return obj
    for x in ptr[1:].split('/'):
        x = x.replace('~1', '/').replace('~0', '~')
        obj = obj[int(x)] if isinstance(obj, list) else obj[x]
    return obj


def jref(p, ptr):
    value = at(load(p), ptr)
    return {'path': p, 'file_sha256': sha(raw(p)), 'json_pointer': ptr,
            'ordered_value_sha256': sha(packed(value)), 'type': type(value).__name__}


def tref(p, a, z):
    t = text(p); literal = t[a:z]
    return {'path': p, 'file_sha256': sha(raw(p)), 'char_start': a, 'char_end': z,
            'utf8_byte_start': len(t[:a].encode()), 'utf8_byte_end': len(t[:z].encode()),
            'literal_sha256': sha(literal.encode())}


def literalref(p, literal):
    t = text(p); assert t.count(literal) == 1, (p, literal)
    a = t.index(literal)
    return tref(p, a, a + len(literal))


def journal(n, section):
    p = f'out/checks/scan{n:03}_root_' + ('decisions.md' if n == 24 else 'journal.md')
    t = text(p)
    m = re.search(r'^## ' + f'{section:02}' + r' — .+$', t, re.M)
    assert m, (p, section)
    next_heading = re.search(r'^## ', t[m.end():], re.M)
    z = m.end() + next_heading.start() if next_heading else len(t)
    return {**tref(p, m.start(), z), 'section_heading': m.group()}


records = {n: load(f'out/records/scan{n:03}.json') for n in (24, 25, 26)}
audits = {n: load(f'out/checks/scan{n:03}_root_crop_audit.json') for n in (24, 25, 26)}
approvals = {n: load(f'out/checks/scan{n:03}_root_approval.json') for n in (24, 25, 26)}


def rec(n, ptr):
    return jref(f'out/records/scan{n:03}.json', ptr)


def dec(n, identity, field='final'):
    rows = records[n]['decisions']
    i = next(i for i, d in enumerate(rows) if d['id'] == identity or d['source_locus_id'] == identity)
    return rec(n, '/decisions/' + str(i) + '/' + field)


def audit(n, ptr):
    return jref(f'out/checks/scan{n:03}_root_crop_audit.json', ptr)


def count_claim(n):
    return [rec(n, '/counts'), jref(f'out/checks/scan{n:03}_root_approval.json', '/counts')]


def sentence(identity, value, references, derivation=None):
    claim_specs.append({'claim_id': identity, 'text': value, 'authority_refs': references,
                        'derivation': derivation or 'Attributed editorial statement bound to the exact listed root fields/sections; complete original candidate states are retained at those references.'})
    return value


def para(identity, sentences, footnote):
    return ' '.join(sentences) + footnote + '\n\n'


for n, r in records.items():
    assert r['main_approved'] is True and r['main_adjudicated'] is True
    assert r['counts'] == approvals[n]['counts']
    assert len(r['decisions']) == r['counts']['decision_loci']
    assert len(r['doubts']) == r['counts']['remaining_doubt_loci']
    assert len(r['inventory']) == r['counts']['inventory_elements']
    assert r['check_events'] == []
    page = 'out/' + approvals[n]['page']
    assert sha(raw(page)) == approvals[n]['sha256']
    assert len(audits[n]['viewed_once']) == audits[n]['total_distinct']
    assert all(x['successful_display_count'] == 1 for x in audits[n]['viewed_once'])
    assert audits[n]['whole_or_half_views'] == 0
assert Counter(x['selected_outcome'] for x in records[24]['C_source_rows']) == {'retained': 15, 'resolved': 2, 'mixed': 1}
assert Counter(x['selected_outcome'] for x in records[25]['C_source_rows']) == {'retained': 7, 'resolved': 1}
assert Counter(x['selected_outcome'] for x in records[26]['C_source_rows']) == {'retained': 13, 'resolved': 2}
for identity in ('SRC024-L03', 'SRC024-L04', 'SRC024-L19', 'SRC024-L32', 'SRC024-L47', 'SRC024-L50'):
    assert next(x for x in records[24]['decisions'] if x['id'] == identity)['confidence'] == 'low'
assert sum(x['created_by_root'] for x in audits[24]['viewed_once']) == 4
assert sum(x['created_by_root'] for x in audits[25]['viewed_once']) == 0
assert sum(x['created_by_root'] for x in audits[26]['viewed_once']) == 4
assert len(audits[25]['failed_unseen_deliveries']) == 1
assert len(audits[25]['failed_unseen_deliveries'][0]['paths']) == 2
assert len(audits[26]['failed_unseen_deliveries']) == 2
assert len(records[26]['S_source_rows']) == 7
assert len(records[26]['complete_selected_source_contexts']['contexts']) == 15
assert len(records[26]['original_reader_inventory_bindings']['reader_inventory_bindings']) == 262
assert sum(d['source_locus_id'].startswith('S') for d in records[26]['decisions']) == 39
assert len([d for d in records[25]['decisions'] if d['id'].startswith('SRC025-S')]) == 7
assert all(not d['diff_C'] and not d['diff_H'] for d in records[25]['decisions'] if d['id'].startswith('SRC025-S'))

progress_path = 'out/progress.log'
commit_lines = {}
for n in (24, 25, 26):
    candidates = [x for x in text(progress_path).splitlines() if x.startswith(f'scan {n:03} done ')]
    assert len(candidates) == 1
    commit_lines[n] = candidates[0]
assert commit_lines[24] == 'scan 024 done 2026-11-21 05:38:55 UTC'
assert commit_lines[25] == 'scan 025 done 2026-11-21 07:34:43 UTC'
assert commit_lines[26] == 'scan 026 done 2026-11-21 10:13:31 UTC'
all_commits = [x for x in text(progress_path).splitlines() if re.fullmatch(r'scan \d{3} done .* UTC', x)]
commit_scan_ids = [int(x.split()[1]) for x in all_commits]
assert sorted(commit_scan_ids) == list(range(2, 9)) + list(range(10, 27))

# Exact brief morphisms: one first-line replacement; all body bytes unchanged.
brief_paths = [f'out/briefs/brief_v{v}_scan{n:03}.md' for v, n in ((22, 24), (23, 25), (24, 26))]
brief_morphisms = []
for old, new in zip(brief_paths, brief_paths[1:]):
    a, b = raw(old), raw(new)
    ah, abody = a.split(b'\n', 1); bh, bbody = b.split(b'\n', 1)
    assert abody == bbody
    assert bh + b'\n' + abody == b
    assert ah + b'\n' + bbody == a
    diff = ''.join(difflib.unified_diff(a.decode().splitlines(True), b.decode().splitlines(True), fromfile=old, tofile=new))
    suffix = 'brief_' + re.search(r'scan(\d+)', old).group(1) + '_' + re.search(r'scan(\d+)', new).group(1) + '.diff'
    (CHECKS / (PREFIX + suffix)).write_text(diff)
    brief_morphisms.append({'before_path': old, 'before_sha256': sha(a), 'after_path': new,
                            'after_sha256': sha(b), 'old_first_line': ah.decode(), 'new_first_line': bh.decode(),
                            'common_body_bytes': len(abody), 'common_body_sha256': sha(abody),
                            'forward_byte_equal': True, 'inverse_byte_equal': True,
                            'full_unified_diff': 'out/checks/' + PREFIX + suffix})
last_named_heading = [x for x in text(brief_paths[-1]).splitlines() if x.startswith('## Revision ')][-1]
assert last_named_heading == '## Revision v22 after scan023'

# Current public totals: retain the raw table lines and bind their extraction.
changes_path = 'out/SP40_CW_81_changes.md'
count_lines = [x for x in text(changes_path).splitlines() if re.match(r'^\| (?:\d{3}|Total) \|', x)]
page_count_lines = [x for x in count_lines if not x.startswith('| Total |')]
raw_cells = [x.split('|')[1:-1] for x in page_count_lines]
table_rows = [[c.strip() for c in row] for row in raw_cells]
assert len(table_rows) == 24
totals = {'C': sum(int(x[1]) for x in table_rows), 'H': sum(int(x[5]) for x in table_rows),
          'remaining_doubts': sum(int(x[9]) for x in table_rows)}
assert totals == {'C': 618, 'H': 702, 'remaining_doubts': 574}
total_line = next(x for x in count_lines if x.startswith('| Total |'))
assert [int(x.strip()) for x in total_line.split('|')[2:-1]] == [618,153,311,154,702,310,245,147,574]
csv.field_size_limit(100000000)
inventory_path = 'out/SP40_CW_81_inventory.csv'
inventory_rows = list(csv.DictReader(io.StringIO(text(inventory_path))))
assert len(inventory_rows) == 1134

leg24 = para('leg24', [
    sentence('L24-1', "Scan024: Root assigns low confidence to the two opening index groups, the complete revised tuple, the reduced fait qu'on a phrase, and the first signed U/Sigma containment groups.",
             [dec(24, x, f) for x in ('SRC024-L03','SRC024-L04','SRC024-L19','SRC024-L32','SRC024-L47','SRC024-L50') for f in ('final','confidence')]),
    sentence('L24-2', 'Opening ens without a point and the definition label def without an accent are resolved.',
             [dec(24,'SRC024-L06'), dec(24,'SRC024-L15'), journal(24,27), journal(24,8)]),
    sentence('L24-3', 'Of eighteen original C rows, two are resolved, fifteen retained and one mixed: the arêtes accent scope remains qualified while the `.).` endpoint is resolved.',
             [rec(24,'/C_source_rows'), dec(24,'SRC024-L25'), dec(24,'SRC024-L26')],
             'Exact selected_outcome histogram of the eighteen root-approved C_source_rows; the two component scopes of R09 are referenced separately.'),
    sentence('L24-4', 'The complete raised replacement, returned lemma rule, interrupted pale traces and local component hand scopes remain in the selected record.',
             [journal(24,7), journal(24,10), journal(24,14), rec(24,'/notes')]),
    sentence('L24-5', 'The final U bar is separated from the preceding p descender in the recorded root observation.',
             [journal(24,24), rec(24,'/notes')])
], '[^leg24]')
leg25 = para('leg25', [
    sentence('L25-1', 'Scan025: Root retains the complete predecessor, relation, E/index, reduced-word and cancellation/live alternatives in their local groups.',
             [journal(25,x) for x in (2,3,5,7,9)]),
    sentence('L25-2', "The participle remains `determinés|determines`, with the short oblique trace qualified between a final accent and the preceding q's terminal trace.",
             [dec(25,'SRC025-P18'), journal(25,13)]),
    sentence('L25-3', 'The raised t and separate point in mut resolve; seven of the eight original C rows remain retained.',
             [dec(25,'SRC025-P15'), rec(25,'/C_source_rows'), journal(25,10)],
             'Exact root-selected abbreviation reading and selected_outcome histogram: seven retained, one resolved.'),
    sentence('L25-4', "The final Sigma's alpha and joined head are firm in the root record, and the written set endpoint remains without a closing brace.",
             [dec(25,'SRC025-P23'), dec(25,'SRC025-P26'), journal(25,16)]),
    sentence('L25-5', 'The faint lower curve and two lower-right points retain their full components and undetermined hand, role, attachment and surface-origin fields.',
             [dec(25,'SRC025-P24'), dec(25,'SRC025-P25'), journal(25,17), journal(25,18)])
], '[^leg25]')
leg26 = para('leg26', [
    sentence('L26-1', 'Scan026: Root retains qualifications for the underlined opening noun, overwritten indices, diagram components, the explanatory-parenthesis decoration and the lower underlined adjective.',
             [rec(26,'/notes'), journal(26,7), journal(26,13), journal(26,18), journal(26,21)]),
    sentence('L26-2', 'The 39 Sigma occurrences remain separately bound to their complete selected source spans and local state fields.',
             [jref('out/checks/scan026_source_selected_contract_v01.json','/sigma_loci'), jref('out/checks/scan026_source_selected_contract_v01.json','/loci')],
             'Thirty-nine locus_id values begin with S; every one has its original complete selected-state descriptor and exact source span bindings.'),
    sentence('L26-3', 'The first displayed relation retains its three complete relation/point states, and the first lower inclusion remains qualified.',
             [dec(26,'L038','root_selected_state_model'), dec(26,'L044','root_selected_state_model'), rec(26,'/notes')]),
    sentence('L26-4', 'Root resolves the cancelled ne-varnothing pair; thirteen of fifteen original C rows remain retained.',
             [dec(26,'L045','root_final_exact'), rec(26,'/C_source_rows'), journal(26,25)],
             'Root final L045 and exact selected_outcome histogram: thirteen retained and two resolved.'),
    sentence('L26-5', 'The 66 remaining doubtful loci include the locally scoped detached marks and the separately recorded faint fleck L052; their exact candidate and component hand/attachment fields remain in the record.',
             [rec(26,'/counts/remaining_doubt_loci'), dec(26,'L052','remaining_doubt'), dec(26,'L052','root_selected_state_model'), rec(26,'/doubts')])
], '[^leg26]')

leg_append = '\n' + leg24 + leg25 + leg26 + (
    '[^leg24]: [Approved scan024 record](records/scan024.json); [root local decisions](checks/scan024_root_decisions.md), especially §§03, 08–10, 12, 14, 22, 24 and 27.\n'
    '[^leg25]: [Approved scan025 record](records/scan025.json); [root local journal](checks/scan025_root_journal.md), especially §§02–03, 05, 07, 09–10 and 13–18.\n'
    '[^leg26]: [Approved scan026 record](records/scan026.json); [root notes authority](checks/scan026_root_notes_abbreviation_authority_v01.json); [complete selected-source contract](checks/scan026_source_selected_contract_v01.json).\n')

wf24 = para('wf24', [
    sentence('W24-1', 'Scan024 committed at 2026-11-21 05:38:55 UTC after thirty distinct once-viewed root crops: twenty-six reused reader crops and four new local crops.',
             [literalref(progress_path,commit_lines[24]), audit(24,'/viewed_once'), audit(24,'/total_distinct')],
             'Commit line copied exactly; total_distinct=30; created_by_root histogram is false:26, true:4; every successful_display_count is one.'),
    sentence('W24-2', 'Root saw no whole scan or supplied half.', [audit(24,'/whole_or_half_views'), audit(24,'/whole_or_halves_seen_by_root')]),
    sentence('W24-3', 'The approved record has 72 decision entries, C33/H49, 39 remaining doubtful loci, 56 inventory entries and zero page check events.', count_claim(24)),
    sentence('W24-4', 'Its eighteen original C rows retain two resolved outcomes, fifteen retained outcomes and one mixed outcome.', [rec(24,'/C_source_rows')], 'Exact selected_outcome histogram, retaining the original eighteen row identities.'),
    sentence('W24-5', 'The approval adapter added the expected `files` container around the same 42 ordered path/hash pairs, with the exact map `F ↦ {files: F}` and inverse selection of `files`; the manifest and required hash checks were preserved.',
             [jref('out/checks/scan024_approval_manifest_adapter.json','')])
], '[^wf24]')
wf25 = para('wf25', [
    sentence('W25-1', 'Scan025 committed at 2026-11-21 07:34:43 UTC after eighteen distinct existing reader crops, each successfully viewed once.',
             [literalref(progress_path,commit_lines[25]), audit(25,'/viewed_once')],
             'Commit line copied exactly; eighteen distinct paths, all created_by_root=false and successful_display_count=1.'),
    sentence('W25-2', 'The initial combined delivery of two crop files failed unseen; the same files were subsequently inspected once.', [audit(25,'/failed_unseen_deliveries'), rec(25,'/workflow_note')]),
    sentence('W25-3', 'Its 34 decision entries include seven source-only S rows with C0/H0; the approved totals are C25/H27, 19 remaining doubtful loci, 36 inventory entries and zero page check events.',
             count_claim(25) + [rec(25,'/decisions/' + str(i)) for i,d in enumerate(records[25]['decisions']) if d['id'].startswith('SRC025-S')],
             'Exact approved count fields; seven SRC025-S rows each have diff_C=false and diff_H=false.'),
    sentence('W25-4', 'Root journal §20 rescinded five added outer qualifier wrappers before release, retaining the exact original later-primary groups and every independently observed local state in the public record.', [journal(25,20)]),
    sentence('W25-5', 'That printing correction added no image view or reading decision, and the original eight C-row outcomes remained seven retained and one resolved.', [journal(25,20), rec(25,'/C_source_rows')])
], '[^wf25]')
wf26a = para('wf26a', [
    sentence('W26-1', 'Scan026 committed at 2026-11-21 10:13:31 UTC after 27 distinct once-viewed root crops: four new and twenty-three reused, comprising A10/B9/C4.',
             [literalref(progress_path,commit_lines[26]), audit(26,'/viewed_once'), rec(26,'/workflow_note')],
             'Exact commit line; created_by_root counts 4/23; reused path reader segments give A10/B9/C4; each successful_display_count is one.'),
    sentence('W26-2', 'Two failed unseen deliveries were recovered using the same existing files, and root saw no whole scan or supplied half.', [audit(26,'/failed_unseen_deliveries'), audit(26,'/whole_or_half_views'), rec(26,'/workflow_note')]),
    sentence('W26-3', 'The approved record has 91 decision loci, C70/H82, 66 remaining doubtful loci, 106 inventory entries and zero page check events.', count_claim(26)),
    sentence('W26-4', 'The fifteen original C rows preserve R02 as four original parts and R15 as one original part with eight separately bound recurrences.',
             [rec(26,'/C_source_rows/1'), rec(26,'/C_source_rows/14')]),
    sentence('W26-5', "The 91 selected-locus inventory entries and fifteen complete context containers cover the agreed paragraphs, displays and deleted l'intersection while retaining all 262 original reader inventory references.",
             [rec(26,'/inventory'), rec(26,'/complete_selected_source_contexts'), rec(26,'/original_reader_inventory_bindings')],
             'Ninety-one locus entries plus fifteen context entries equal 106; complete context supplement has an exact eight-segment selected-source partition; the original inventory reference array has 262 entries.')
], '[^wf26]')
wf26b = para('wf26b', [
    sentence('W26-6', 'The final bounded record closure attached all seven complete S source rows, exposed the full scoped hand assignments in public inventory fields, and preserved an explicit inverse for the inventory reordering and pointer rebasing.',
             [jref('out/checks/scan026_root_record_v03_review.json',''), rec(26,'/S_source_rows'), rec(26,'/inventory_order_provenance')]),
    sentence('W26-7', 'Root verified that all other decision, doubt, selected-state, source-span, note, count and check-event fields were unchanged by that closure.',
             [jref('out/checks/scan026_root_record_v03_review.json','/all_other_v02_decisions_doubts_selected_models_source_spans_notes_counts_check_events_exact')]),
    sentence('W26-8', 'Approval first stopped because the expected aggregate fingerprint filename was absent; the completed aggregate copied 107 existing preimage path/hash pairs exactly, and the approval script remained unchanged.',
             [jref('out/checks/scan026_root_fingerprint_aggregation.json','')])
], '[^wf26]')
brief_para = para('brief-history', [
    sentence('WB-1', 'The scan024→025→026 reader-brief transitions changed only the first heading line: v22/scan024 became v23/scan025 and then v24/scan026.',
             [tref(p,0,text(p).index('\n')+1) for p in brief_paths],
             'The two complete unified diffs contain one first-line replacement each; exact forward and inverse byte reconstruction is included in brief_morphisms.'),
    sentence('WB-2', 'Every byte after that first newline is identical across all three files, so the last named body revision remains `Revision v22 after scan023` under the later v23 and v24 headings.',
             [tref(p,text(p).index('\n')+1,len(text(p))) for p in brief_paths],
             'The three body byte strings are equal; the final ## Revision heading is extracted exactly from each body.'),
    sentence('WB-3', 'The scan025→026 handoff separately appended sixteen exact notation rows; it introduced no additional reader-brief body revision.', [jref('out/checks/scan026_brief_transition.json','')])
], '[^brief-history]')
closure = para('closure', [
    sentence('WF-1', 'All 24 requested scans are committed, with the final scan026 commit recorded at 2026-11-21 10:13:31 UTC.',
             [literalref(progress_path,x) for x in all_commits],
             'Twenty-four distinct commit lines cover scans002–008 and010–026; the final line is copied exactly.'),
    sentence('WF-2', 'The completed public count table reports C618/H702 and 574 remaining doubtful loci; the public inventory contains 1,134 entries.',
             [literalref(changes_path,total_line), {'path':inventory_path,'file_sha256':sha(raw(inventory_path)), 'CSV_data_record_count':len(inventory_rows)}],
             'The 24 exact table rows sum to C618/H702/574; csv.DictReader yields 1,134 data records with the header excluded. Raw source files and raw count-table cell text remain hash-bound.'),
    sentence('WF-3', 'Earlier in-progress passages above retain their historical phase wording; the later completion sections and this dated closure record the completed page sequence.',
             [literalref(progress_path,commit_lines[26])],
             'Editorial temporal framing; the historical paragraphs are byte-identical to the baseline, except for the single current open-status sentence explicitly replaced.'),
    sentence('WF-4', 'The final validation scope remains structural source and record review; no successful TeX compilation or rendered-page validation is claimed.',
             [literalref('out/workflow_assessment.md','No successful compilation or rendered-page validation is claimed.'),
              *[jref(f'out/checks/scan{n:03}_root_approval.json','/validation_scope') for n in (24,25,26)]])
], '[^final-closure]')

workflow_append = ('\n\n## Scan024 completion\n\n' + wf24 + '\n## Scan025 completion\n\n' + wf25 +
                   '\n## Scan026 completion\n\n' + wf26a + wf26b +
                   '\n## Exact brief history after scan023\n\n' + brief_para +
                   '\n## Final closure — 2026-11-21\n\n' + closure +
                   '[^wf24]: [Approved scan024 record](records/scan024.json); [closed crop audit](checks/scan024_root_crop_audit.json); [approval adapter](checks/scan024_approval_manifest_adapter.json); [progress log](progress.log).\n'
                   '[^wf25]: [Approved scan025 record](records/scan025.json); [closed crop audit](checks/scan025_root_crop_audit.json); [root journal §20](checks/scan025_root_journal.md); [progress log](progress.log).\n'
                   '[^wf26]: [Approved scan026 record](records/scan026.json); [closed crop audit](checks/scan026_root_crop_audit.json); [root v03 review](checks/scan026_root_record_v03_review.json); [fingerprint aggregation](checks/scan026_root_fingerprint_aggregation.json); [progress log](progress.log).\n'
                   '[^brief-history]: [v22 scan024 brief](briefs/brief_v22_scan024.md); [v23 scan025 brief](briefs/brief_v23_scan025.md); [v24 scan026 brief](briefs/brief_v24_scan026.md); [recorded 025→026 transition](checks/scan026_brief_transition.json).\n'
                   '[^final-closure]: [Progress log](progress.log); [public count table](SP40_CW_81_changes.md); [public inventory](SP40_CW_81_inventory.csv); root approval records for [024](checks/scan024_root_approval.json), [025](checks/scan025_root_approval.json) and [026](checks/scan026_root_approval.json).\n')

status_old = {
    'legibility': 'This assessment will be completed after all requested scans are decided.',
    'workflow': 'This assessment remains open while the requested page sequence is in progress.'}
status_new = {
    'legibility': 'The requested 24-scan sequence is complete; the final scan026 commit is recorded at 2026-11-21 10:13:31 UTC (see the completion paragraphs below).',
    'workflow': 'The requested 24-scan sequence is complete; scan026 committed at 2026-11-21 10:13:31 UTC, as recorded in the dated final closure below.'}
for name in status_new:
    sentence('STATUS-' + name, status_new[name], [literalref(progress_path,commit_lines[26]), *[literalref(progress_path,x) for x in all_commits]],
             'Twenty-four exact distinct commit rows and the final commit timestamp; replaces only the current open-status sentence.')

documents = []
full_diff = []
for name, source, addition in [('legibility','out/legibility_note.md',leg_append), ('workflow','out/workflow_assessment.md',workflow_append)]:
    before = text(source); old = status_old[name]; new = status_new[name]
    assert before.count(old) == 1
    start = before.index(old)
    selected = before[:start] + new + before[start+len(old):]
    proposed = selected + addition
    old_offset = start; new_offset = start
    operations = [
        {'operation': 'replace_current_open_status', 'old_char_start': old_offset,
         'old_char_end': old_offset+len(old), 'new_char_start': new_offset,
         'new_char_end': new_offset+len(new), 'before': old, 'after': new},
        {'operation': 'append_approved_completion_assessment', 'old_char_start': len(before),
         'old_char_end': len(before), 'new_char_start': len(selected),
         'new_char_end': len(proposed), 'before': '', 'after': addition}]
    forward = before
    for op in reversed(operations):
        assert forward[op['old_char_start']:op['old_char_end']] == op['before']
        forward = forward[:op['old_char_start']] + op['after'] + forward[op['old_char_end']:]
    assert forward == proposed
    inverse = proposed
    for op in reversed(operations):
        assert inverse[op['new_char_start']:op['new_char_end']] == op['after']
        inverse = inverse[:op['new_char_start']] + op['before'] + inverse[op['new_char_end']:]
    assert inverse.encode() == raw(source)
    old_file = CHECKS / (PREFIX + name + '.before.md')
    new_file = CHECKS / (PREFIX + name + '.proposed.md')
    old_file.write_bytes(raw(source)); new_file.write_bytes(proposed.encode())
    diff = ''.join(difflib.unified_diff(before.splitlines(True),proposed.splitlines(True),fromfile=source,tofile=str(new_file.relative_to(BASE))))
    full_diff.append(diff)
    documents.append({'target_path':source, 'baseline_path':str(old_file.relative_to(BASE)),
                      'baseline_sha256':sha(raw(source)), 'proposed_path':str(new_file.relative_to(BASE)),
                      'proposed_sha256':sha(proposed.encode()), 'operations':operations,
                      'forward_exact':True,'inverse_exact':True,
                      'historical_text_preserved_outside_current_status_sentence':True})
    for claim in claim_specs:
        if claim['text'] in proposed:
            assert proposed.count(claim['text']) == 1, claim['claim_id']
            a=proposed.index(claim['text']); z=a+len(claim['text'])
            claim.setdefault('proposed_occurrences',[]).append({'path':str(new_file.relative_to(BASE)),
                'char_start':a,'char_end':z,'utf8_byte_start':len(proposed[:a].encode()),
                'utf8_byte_end':len(proposed[:z].encode()),'literal_sha256':sha(claim['text'].encode())})

assert all(c.get('proposed_occurrences') for c in claim_specs)
# Every recorded source span and pointer is independently resolvable now.
for claim in claim_specs:
    for r in claim['authority_refs']:
        assert sha(raw(r['path'])) == r['file_sha256']
        if 'json_pointer' in r:
            assert sha(packed(at(load(r['path']),r['json_pointer']))) == r['ordered_value_sha256']
        if 'char_start' in r:
            assert sha(text(r['path'])[r['char_start']:r['char_end']].encode()) == r['literal_sha256']
for p, b in inputs.items():
    assert (BASE/p).read_bytes() == b, 'Input changed: '+p

delta = {'schema':'scan026-source-final-assessment-proposal-v01','source_only':True,'main_approved':False,
         'global_files_changed':False,'images_opened':0,'ink_decisions':0,'new_classifications':0,
         'documents':documents,'brief_morphisms':brief_morphisms,
         'claim_map':'out/checks/'+PREFIX+'claims_v01.json',
         'scope':'Only the two current open-status sentences and the appended completion sections differ. All historical wording elsewhere remains byte-exact. Root review is required before applying the proposal.'}
proof = {'schema':'scan026-source-final-assessment-proof-v01','all_forward_and_inverse_checks_passed':True,
         'all_authority_refs_resolve_and_match':True,'all_inputs_unchanged':True,
         'document_count':len(documents),'exact_text_operations':sum(len(x['operations']) for x in documents),
         'attributed_claim_count':len(claim_specs),'commit_lines':commit_lines,
         'complete_requested_commit_scan_ids':sorted(commit_scan_ids),'public_totals':totals,
         'inventory_data_records':len(inventory_rows),'raw_count_table_lines':count_lines,
         'raw_count_table_cells':raw_cells,'body_revision_heading':last_named_heading,
         'brief_morphisms':brief_morphisms,
         'input_files':[{'path':p,'sha256':sha(b),'bytes':len(b)} for p,b in inputs.items()]}
for suffix,obj in [('delta_v01.json',delta),('claims_v01.json',claim_specs),('proof_v01.json',proof)]:
    (CHECKS/(PREFIX+suffix)).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(CHECKS/(PREFIX+'full.diff')).write_text('\n'.join(full_diff))
review = ('# Final assessment proposal — exact new wording\n\n'
          'This is a source-only proposal for root review. The original assessment files are unchanged. The four operations are two current-status sentence replacements and two appended blocks; the inverse recovers both original files byte for byte.\n\n'
          '## Current status replacements\n\n'
          '**legibility_note.md — before**\n\n'+status_old['legibility']+'\n\n**After**\n\n'+status_new['legibility']+
          '\n\n**workflow_assessment.md — before**\n\n'+status_old['workflow']+'\n\n**After**\n\n'+status_new['workflow']+
          '\n\n## Complete legibility addition\n'+leg_append+'\n## Complete workflow addition\n'+workflow_append+
          '\n## Source review map\n\nEvery new sentence is bound in `scan026_source_final_assessment_claims_v01.json` to its exact root-record pointer, journal section, commit line or public count source. The complete header-only brief diffs and both forward/inverse byte proofs are included separately. No historical pending passage is rewritten.\n')
(CHECKS/(PREFIX+'review_v01.md')).write_text(review)
print(json.dumps({'delta':'out/checks/'+PREFIX+'delta_v01.json','delta_sha256':sha((CHECKS/(PREFIX+'delta_v01.json')).read_bytes()),
                  'review':'out/checks/'+PREFIX+'review_v01.md','proof':'out/checks/'+PREFIX+'proof_v01.json',
                  'claims':len(claim_specs),'operations':4,'global_writes':0},ensure_ascii=False))
