#!/usr/bin/env python3
"""Read-only bounded extractor: source reads and JSON on stdout; no file writes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCANS = (2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20)
MACROS = 'source/SP40_CW_81_witnesses/hua/transcripts/preamble/grothendieck.sty'
INPUTS = {}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def read(relative):
    raw = (ROOT / relative).read_bytes()
    INPUTS[relative] = {'path':relative, 'sha256':sha(raw)}
    return raw.decode('utf-8')

RECORDS = {n:json.loads(read(f'out/records/scan{n:03d}.json')) for n in SCANS}

def decision(scan, identifier):
    for index, row in enumerate(RECORDS[scan]['decisions']):
        if row['id'] == identifier:
            return index, row
    raise KeyError((scan, identifier))

def display_boolean(value):
    if value is True or value == 'yes': return True
    if value is False or value == 'no': return False
    raise ValueError(value)

def reference(scan, identifier, expected):
    index, row = decision(scan, identifier)
    current = row['marked_in_H']
    assert type(current) is type(expected) and current == expected
    path = f'out/records/scan{scan:03d}.json'
    return {
        'scan':f'scan{scan:03d}', 'decision_id':identifier,
        'record_path':path, 'record_sha256':INPUTS[path]['sha256'],
        'record_pointer':f'/decisions/{index}',
        'field_pointer':f'/decisions/{index}/marked_in_H',
        'location_exact':row['location'], 'H_declaration_exact':row.get('H'),
        'marked_in_H_fields_exact':{k:v for k,v in row.items() if k.startswith('marked_in_H')},
        'current_serialized_value':current, 'current_boolean_display':display_boolean(current),
        'proposed_serialized_value':current, 'proposed_boolean_display':display_boolean(current),
    }

def excerpt(path, first, last=None):
    last = first if last is None else last
    text = read(path)
    lines = text.splitlines(keepends=True)
    assert 1 <= first <= last <= len(lines)
    start = sum(map(len, lines[:first-1]))
    end = sum(map(len, lines[:last]))
    literal = text[start:end]
    return {'path':path, 'source_sha256':INPUTS[path]['sha256'],
            'line_start':first, 'line_end':last, 'char_start':start, 'char_end':end,
            'excerpt_exact':literal, 'literal_sha256_utf8':sha(literal.encode('utf-8'))}

def h(scan, first, last=None):
    return excerpt(f'packets/{scan:03d}/H.tex', first, last)

def retained(label, scan, ids, expected, spans, reason):
    return {'audit_id':label, 'status':'retain_current_field',
            'decisions':[reference(scan, identifier, expected) for identifier in ids],
            'H_sources':[h(scan,*span) for span in spans], 'reason':reason}

proposal = reference(17, '017-D04b', True)
_, row = decision(17, '017-D04b')
old_scope = 'Covered source-placeholder locus; the marginal parent makes no exact positional-identity claim.'
new_scope = ('The attached local H span writes E_j without a doubt marker. H\'s '
             '\\ill{} follows the set\'s closing brace; the local marked_in_H flag is '
             'false. The existing 017-H-MARGIN-ILL count-parent grouping is retained.')
assert row['marked_in_H_scope'] == old_scope
assert row['H_count_parent'] == '017-H-MARGIN-ILL'
proposal.update({
    'audit_id':'MH-P01', 'status':'source_reviewed_proposal_no_record_mutation',
    'proposed_serialized_value':False, 'proposed_boolean_display':False,
    'prior_fields_exact':{'marked_in_H':True,'marked_in_H_scope':old_scope},
    'proposed_fields':{'marked_in_H':False,'marked_in_H_scope':new_scope},
    'history_preservation':{'prior_fields_preserved':True,'committed_record_modified':False,'application_owner':'root'},
    'H_sources':[h(17,30,31)],
    'existing_H_provenance_exact':row['witness_provenance']['H'],
    'existing_count_parent_exact':row['H_count_parent'],
    'existing_evidence_exact':row['evidence'],
    'reason':('The exact H attachment for this decision ends at the set\'s closing brace. '
              'Its local E_j has no uncertainty macro. The source places \\ill{} after '
              'that brace. The current scope text records count-parent coverage while '
              'expressly withholding an exact positional-identity claim. For the local '
              'doubt field, false is proposed. The count-parent assignment and prior '
              'wording remain preserved.'),
    'root_review_in_session':('Root directly read 017-D04b and packets/017/H.tex:31, '
                              'agreed with false for this local flag, and requested '
                              'preservation of both prior fields while leaving counts '
                              'and H_count_parent unchanged.'),
    'fields_outside_proposal':['H_count_parent','diff_C','diff_H','counts','C_doubt_status','final','evidence','witness_provenance'],
})

retained_cases = []
CASES = [
 ('MH-R01',3,['003-11','003-15','003-16'],'yes',[(10,12)],
  'The local scopes carry uncertain avec or the struck ill placeholder used by the committed cancellation-group mapping. That mapping is retained without ink reassessment.'),
 ('MH-R02',3,['003-33'],'yes',[(35,35)],
  'The local cancelled source group is \\struck{\\ill{}}; its nested ill marker supports yes.'),
 ('MH-R03',3,['003-40','003-47'],'no',[(41,41),(43,43)],
  'The local H struck arguments carry no uncertainty or ill marker; no is retained.'),
 ('MH-R04',4,['004-80','004-84'],'no',[(11,11)],
  'The local frame declaration reads Encadré, pour; it supplies no local doubt mark for these frame loci.'),
 ('MH-R05',6,['006-04','006-05'],'yes',[(33,33)],
  'The committed witness_context points both local predecessor/open-fragment decisions to H line 33, whose corresponding tail is an explicit ill placeholder. That scope is retained without mathematical evaluation.'),
 ('MH-R06',11,['011-D09','011-D12','011-D13','011-D14'],'no',[(11,12)],
  'The note reports an overwritten letter and a struck Hom expression. Its exact local text supplies no doubt wording or uncertainty macro for these decisions.'),
 ('MH-R07',11,['011-D62','011-D63','011-D64','011-D65','011-D66'],'no',[(3,5),(22,28)],
  'These exact note/drawing blocks describe the respective sketches. The explicit doubtful-letter note at line 17 is recorded separately below with its existing unchanged-audit pointer.'),
 ('MH-R08',12,['012-D01'],'yes',[(9,9)],
  'H explicitly gives the local label alternatives « OK » (ou « ok »). The actual note text supports yes at this label locus.'),
 ('MH-R09',12,['012-D04','012-D26','012-D29'],'no',[(2,9)],
  'H supplies direct local descriptions for these drawing/boundary loci. The OK/ok alternative in the same note attaches to the marked disks at 012-D01; its scope is retained there.'),
 ('MH-R10',15,['015-D01a','015-H-TITLE','015-D15','015-D19','015-D19-glyph','015-G12','015-G14','015-G-VOIS-CANCEL','015-G-IL-CANCEL','015-G-REMNANT-ANGULAR'],'no',[(2,2),(32,33),(42,43),(46,46)],
  'These exact local H arguments use plain struck commands. The quoted arguments and cancellation declarations carry no local uncertainty macro; no is retained.'),
 ('MH-R11',15,['015-H-DRAW'],'no',[(25,29)],
  'The drawing block directly describes the disk, chords, labels and braces; no local doubt is attached to this parent declaration.'),
 ('MH-R12',15,['015-D16','015-H17','015-G10a','015-G10b','015-S-NOTE-SECOND','015-G10-GROUP'],'yes',[(48,48)],
  'The H marginal-note tail has an explicit ill placeholder. The committed tail coverage for these textual/graphic components is retained; no graphic position or count-parent assignment was reassessed.'),
 ('MH-R13',16,['016-D05'],'yes',[(4,4)],
  'The local cancelled group is struck ill; its actual ill marker supports yes.'),
 ('MH-R14',16,['016-G08','016-BR-PAIR'],'no',[(16,18),(44,44)],
  'The brace-pair note gives labels directly and the lower cancellation uses a plain struck argument. These exact local descriptions carry no doubt mark.'),
 ('MH-R15',17,['017-D01a','017-D05','017-D06a','017-D06b'],False,[(4,4),(18,19)],
  'The local spans use plain struck wording and an add command for intersection. Their false flags are retained.'),
 ('MH-R16',17,['017-D04a'],False,[(30,31)],
  'The local partition-letter declaration is supplied directly. The trailing ill placeholder remains at the end of the marginal note.'),
 ('MH-R17',17,['017-G12','017-H-MARGIN-ILL'],True,[(30,31)],
  'These declarations expressly refer to the trailing ill placeholder after the closing brace; true is retained for that source-placeholder scope.'),
 ('MH-R18',18,['L018-13','L018-18','L018-25','L018-26','L018-29','L018-38'],False,[(14,15),(17,18),(21,21)],
  'The local H cancellations use plain struck arguments for la, un, choisie, est and et. Their false flags are retained.'),
 ('MH-R19',19,['L019-19','L019-23','L019-24','L019-25'],True,[(23,23),(28,29)],
  'The local scopes carry uncertain On a, Au and dernier, or a struck ill placeholder. Those actual marks support true.'),
 ('MH-R20',19,['L019-26'],False,[(30,30)],
  'The exact text is se borner : \\ill{} sur les. The colon precedes the placeholder and is supplied directly; the local colon flag remains false.'),
 ('MH-R21',19,['L019-27'],True,[(30,30)],
  'The adjoining word locus is represented by the actual ill placeholder after the colon. Its existing true flag is retained at that scope.'),
 ('MH-R22',20,['L020-09','L020-10','L020-23','L020-35'],True,[(8,8),(11,11),(24,24)],
  'The respective cancelled H groups are explicit struck ill placeholders. Existing component coverage inside those local groups is retained.'),
 ('MH-R23',20,['L020-33'],True,[(23,23)],
  'H supplies \\add{\\uncertain{non vide}} at this inserted phrase, supporting true.'),
 ('MH-R24',20,['L020-31','L020-32'],False,[(21,22)],
  'The exact note directly describes the upper label. It supplies no local question or uncertainty marker for this brace/label apparatus.'),
]
retained_cases = [retained(*case) for case in CASES]

unchanged = RECORDS[11]['unchanged_audit'][0]
assert unchanged['id'] == '011-U01' and 'marked_in_H' not in unchanged
out_of_field = {
    'audit_id':'MH-N01', 'scan':'scan011', 'existing_record_id':'011-U01',
    'record_path':'out/records/scan011.json',
    'record_sha256':INPUTS['out/records/scan011.json']['sha256'],
    'record_pointer':'/unchanged_audit/0', 'marked_in_H_present':False,
    'H_declaration_exact':unchanged['H'], 'existing_note_exact':unchanged['note'],
    'H_sources':[h(11,14,17)],
    'action':'Preserve the exact source note; no field creation or record mutation proposed.',
    'reason':('H expressly says la première lettre de cette ligne, lue $\\mathcal{E}$, est douteuse. '
              'The matching unchanged-audit entry already mentions H editorial doubt and '
              'has no marked_in_H field. This audit creates no new decision or field.'),
}

assert all(item.get('H') is None for item in RECORDS[10]['decisions'])
unmapped_drawing_note = {
    'audit_id':'MH-N02', 'scan':'scan010',
    'record_path':'out/records/scan010.json',
    'record_sha256':INPUTS['out/records/scan010.json']['sha256'],
    'record_pointer':'/decisions',
    'decision_ids':[item['id'] for item in RECORDS[10]['decisions']],
    'H_declarations_all_null':True,
    'H_sources':[h(10,2,len(read('packets/010/H.tex').splitlines()))],
    'action':'Exact apparatus wording preserved for scope; no metadata proposal.',
    'reason':('The drawing description includes apparemment and a quoted « ? ». '
              'All committed scan010 per-decision H declarations are null. '
              'This bounded local-declaration audit establishes no new locus mapping '
              'from that description to those field values.'),
}

metadata_sources = {}
for scan in (3,4,6,10,11,12,15,16,17,18,19,20):
    relative = f'packets/{scan:03d}/metadata.json'
    metadata = json.loads(read(relative))
    metadata_sources[f'scan{scan:03d}'] = {
        'path':relative, 'sha256':INPUTS[relative]['sha256'], 'exact_metadata':metadata,
        'source_used':f'packets/{scan:03d}/H.tex', 'full_hua_file_opened':False,
    }
macro_sources = [excerpt(MACROS,150,155), excerpt(MACROS,175,180), excerpt(MACROS,201,203)]

report = {
    'title':'Bounded source audit of prior marked_in_H metadata',
    'status':'proposal_only_committed_sources_untouched',
    'scope':{
        'committed_record_paths_examined_for_field_declarations':[f'out/records/scan{n:03d}.json' for n in SCANS],
        'last_permitted_scan':'scan020',
        'task':'Local H doubt-mark semantics at declared deletion/apparatus loci.',
        'excluded':['scan021 and later packet contents','images, crops, OCR, compilation and rendering',
                    'internet, research, installs and delegation','new manuscript readings or ink adjudication',
                    'mathematical or coordinate computations and proof checks',
                    'C/H count changes, selected TeX, page-file and reader changes'],
        'method':'Declaration searches were discovery only; reviewed cases were checked against exact local H text and supplied macro definitions.',
        'untouched_scope':('All other decisions retain their existing values outside this proposal. '
                           'Missing fields, not-applicable fields, unrelated lexical, mathematical, '
                           'ordering and graphic decisions were not converted or re-adjudicated.'),
    },
    'field_display_mapping':{
        'exact_serializations_preserved':True,
        'definition':[{'source':'yes','display':True},{'source':'no','display':False},
                      {'source':True,'display':True},{'source':False,'display':False}],
        'purpose':'Display only; source serialization families are preserved.',
    },
    'pointer_convention':{
        'record_pointers':'JSON pointers; array indices zero-based.',
        'lines':'One-based inclusive source line ranges.',
        'characters':'Zero-based Unicode code-point offsets in exact UTF-8-decoded source; end exclusive.',
        'hashes':'SHA-256 of original file bytes; excerpt hashes use exact UTF-8 excerpt bytes.',
    },
    'H_apparatus_definition_sources':macro_sources,
    'proposals':[proposal], 'reviewed_retained_cases':retained_cases,
    'explicit_local_doubt_without_existing_field':out_of_field,
    'apparatus_without_local_H_declarations':unmapped_drawing_note,
    'packet_provenance':metadata_sources,
    'preservation':{
        'record_files_written':[], 'page_or_selected_tex_files_written':[],
        'reader_files_written':[], 'count_fields_changed':[], 'original_history_preserved':True,
        'review_artifacts_only':['out/checks/marked_H_prior_source_audit.json',
                                'out/checks/marked_H_prior_source_audit.md',
                                'out/checks/extract_marked_H_prior_source_audit.py'],
    },
    'input_fingerprints':list(INPUTS.values()),
    'extractor':{'path':str(Path(__file__).resolve().relative_to(ROOT)),
                 'sha256':sha(Path(__file__).read_bytes()), 'side_effects':'Source reads and stdout only.'},
}
for relative, fingerprint in INPUTS.items():
    assert sha((ROOT/relative).read_bytes()) == fingerprint['sha256'], relative
print(json.dumps(report,ensure_ascii=False,indent=2))
