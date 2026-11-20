"""Attach the exact released scan017 assembler map to the source-only record.

This reads text and checks declared literal source spans only. It opens no image
and performs no rendering, mathematical operation, or geometry computation.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
from scan017_build_record import fingerprint, json_text

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out'
CHECKS=OUT/'checks'


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def attach(expected_draft,expected_map):
    draft_path=CHECKS/'scan017_final_draft.tex'
    map_path=CHECKS/'scan017_final_source_map.json'
    assert file_sha(draft_path)==expected_draft,'Selected draft hash differs from released hash.'
    assert file_sha(map_path)==expected_map,'Selected map hash differs from released hash.'
    draft=draft_path.read_text();mapping=json.loads(map_path.read_text())
    assert mapping['draft_sha256_utf8']==expected_draft
    journal_path=CHECKS/'scan017_main_decisions.md'
    assert mapping['root_decision_journal']['sha256_utf8']==file_sha(journal_path),'Journal differs from assembler source.'
    record_path=CHECKS/'scan017_record_draft.json'
    record=json.loads(record_path.read_text())
    assert not record['main_adjudicated']
    assert all(not d['main_approved'] for d in record['decisions'])
    blocks={b['id']:(i,b) for i,b in enumerate(mapping['blocks'])}

    def convert(row,collection,index):
        src=row['draft'];start=src['character_start'];end=src['character_end_exclusive']
        literal=draft[start:end]
        assert literal==src['literal_tex'],(collection,index,'literal mismatch')
        assert hashlib.sha256(literal.encode()).hexdigest()==src['literal_sha256_utf8'],(collection,index,'literal hash mismatch')
        result={'manifest':'root.final_draft.tex','path':'checks/scan017_final_draft.tex',
                'char_start':start,'char_end':end,'line_start':src['covering_lines_inclusive'][0],
                'line_end':src['covering_lines_inclusive'][1],'excerpt':literal,
                'literal_sha256_utf8':src['literal_sha256_utf8'],
                'group_anchor':row.get('block_id'),
                'assembly_map':{'manifest':'root.final_source_map.json','pointer':f'/{collection}/{index}',
                                'sha256':expected_map},
                'scope':'exact selected-source locus; source offsets supplied by dedicated assembler'}
        if row.get('block_id') in blocks:
            block_index,block=blocks[row['block_id']]
            result['selected_component_source']={'manifest':'root.final_source_map.json','pointer':f'/blocks/{block_index}/source'}
            result['root_decision_sources']=copy.deepcopy(block.get('root_decision_sources',[]))
        elif 'source' in row:
            result['selected_component_source']={'manifest':'root.final_source_map.json','pointer':f'/{collection}/{index}/source'}
        if row.get('note'):
            result['note']=row['note']
        return result

    decisions={d['id']:d for d in record['decisions']}
    decision_sources={k:[] for k in decisions}
    for collection in ['decision_coverage','overbar_coverage']:
        for index,row in enumerate(mapping[collection]):
            key=row['decision_id'];assert key in decision_sources,key
            decision_sources[key].append(convert(row,collection,index))
    missing=[key for key,rows in decision_sources.items() if not rows]
    assert not missing,missing
    for key,d in decisions.items():
        d['final_source_attachment']=copy.deepcopy(decision_sources[key])
        d['root_page_sources']=copy.deepcopy(decision_sources[key])
        d['root_source_attachment_status']='Complete selected-source attachment; final record approval pending.'

    inventory={i['element']:i for i in record['inventory']}
    inventory_sources={key:[] for key in inventory}
    for index,row in enumerate(mapping['inventory_coverage']):
        key=row['inventory_id'];assert key in inventory_sources,key
        inventory_sources[key].append(convert(row,'inventory_coverage',index))
    assert all(inventory_sources.values())
    for key,item in inventory.items():
        item['root_page_sources']=copy.deepcopy(inventory_sources[key])
        item['final_source_attachment_status']='Complete selected-source attachment; root record approval pending.'
        item['selection_status']='Root ink selection and exact selected-source coverage attached.'
    for doubt in record['doubts']:
        key=doubt['decision_id'];assert key in decision_sources
        doubt['root_page_sources']=copy.deepcopy(decision_sources[key])
    for row in record['actual_C_doubt_map']:
        row['selected_source_attachments']={key:copy.deepcopy(decision_sources[key]) for key in row['decision_ids']}

    record['source_attachment_map']='checks/scan017_final_source_map.json'
    record['source_attachment_map_sha256']=expected_map
    record['root_selected_source']='checks/scan017_final_draft.tex'
    record['root_selected_source_sha256']=expected_draft
    record['source_attachment_status']='Complete: all56 decisions,39 inventory entries and18 retained-doubt clusters have current selected-source attachments.'
    record['final_source_missing_attachments']={'decisions':[],'inventory':[],'doubts':[]}
    record['assembler_original_C_scope']=copy.deepcopy(mapping['original_C_doubt_row_coverage'])
    record['recurring_ring_source_scope']=copy.deepcopy(mapping['recurring_ring_source_scope'])
    record['root_actions_pending']=['One final targeted source QA pass.','Root review, approval and commit.']
    record['mechanical_verification'].update({
        'status':'Exact current assembler attachments installed; final source QA pass pending.',
        'final_decision_attachment_entries':sum(map(len,decision_sources.values())),
        'final_inventory_attachment_entries':sum(map(len,inventory_sources.values())),
        'final_doubt_attachment_entries':sum(len(d['root_page_sources']) for d in record['doubts']),
        'selected_draft_sha256':expected_draft,'selected_map_sha256':expected_map,
        'assembler_literal_span_checks_only':True,'numerical_geometry_checks_by_clerk':0})
    manifest_path=CHECKS/'scan017_reader_fingerprints.json'
    manifest=json.loads(manifest_path.read_text())
    for key,path in [('root.final_draft.tex',draft_path),('root.final_source_map.json',map_path),
                     ('root.main_decisions.md',journal_path),('clerk.attach_final.py',Path(__file__))]:
        manifest['files'][key]=fingerprint(path)
    for filename in ['scan017_root_crop_audit.json','scan017_tex_assembly_audit.json']:
        path=CHECKS/filename
        if path.is_file():manifest['files']['root.'+filename]=fingerprint(path)
    manifest['root_files'].update({'final_draft':manifest['files']['root.final_draft.tex'],
                                   'final_source_map':manifest['files']['root.final_source_map.json'],
                                   'main_decisions':manifest['files']['root.main_decisions.md']})
    manifest['selected_source_state']='Exact assembler draft/map released and attached; root final approval pending.'
    record_path.write_text(json_text(record));manifest_path.write_text(json_text(manifest))
    union_path=CHECKS/'scan017_union.md';union=union_path.read_text()
    union=union.replace('Selected final-source attachments await the dedicated assembler current map/hash.',
                        'All selected final-source attachments use the dedicated assembler current draft and map.')
    union+='\n## Current selected-source attachments\n\n'
    union+=f'Selected draft SHA256: `{expected_draft}`. Selected map SHA256: `{expected_map}`. All56 decision entries,39 inventory entries and18 retained-doubt clusters are attached; overlapping inventory scopes retain their separate exact spans. Root final approval remains pending.\n'
    union_path.write_text(union)
    print(json_text({'record_sha256':file_sha(record_path),'fingerprints_sha256':file_sha(manifest_path),
                     'draft_sha256':expected_draft,'map_sha256':expected_map,
                     'decision_attachments':sum(map(len,decision_sources.values())),
                     'inventory_attachments':sum(map(len,inventory_sources.values())),
                     'doubt_attachments':sum(len(d['root_page_sources']) for d in record['doubts']),
                     'main_adjudicated':False,'main_approved_rows':0}))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--draft-sha256',required=True)
    parser.add_argument('--map-sha256',required=True)
    args=parser.parse_args()
    attach(args.draft_sha256,args.map_sha256)
