#!/usr/bin/env python3
"""Prepare journal-to-source coverage; no image, source edit, or ink/count choice."""
from pathlib import Path
import hashlib
import json
import re

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'


def sha(value):
    return hashlib.sha256(value if isinstance(value,bytes) else value.encode('utf-8')).hexdigest()


def ref(path,text,a,b):
    return {'path':path,'sha256_utf8':sha(text),'char_start':a,'char_end_exclusive':b,'utf8_byte_start':len(text[:a].encode('utf-8')),'utf8_byte_end_exclusive':len(text[:b].encode('utf-8')),'line_start':text.count('\n',0,a)+1,'line_end':text.count('\n',0,max(a,b-1))+1,'literal_sha256_utf8':sha(text[a:b])}


def main():
    journal_path='out/checks/scan025_root_journal.md'
    journal=(BASE/journal_path).read_text()
    audit_path='out/checks/scan025_root_crop_audit.json'
    audit_raw=(BASE/audit_path).read_bytes()
    audit=json.loads(audit_raw)
    union_raw=(OUT/'scan025_source_union_v01.json').read_bytes()
    union=json.loads(union_raw)
    starts=list(re.finditer(r'(?m)^## (\d{2}) — (.+)$',journal))
    sections={}
    for i,m in enumerate(starts):
        end=starts[i+1].start() if i+1<len(starts) else len(journal)
        sections[m.group(1)]={'section':m.group(1),'title':m.group(2),'source_ref':ref(journal_path,journal,m.start(),end)}
    assert list(sections)==[f'{i:02}' for i in range(1,20)]
    crop_refs={}
    for i,row in enumerate(audit['viewed_once']):
        for s in row['decision_sections']:
            crop_refs[s]={'audit_path':audit_path,'audit_sha256_utf8':sha(audit_raw),'json_pointer':f'/viewed_once/{i}','crop_path':row['path'],'recorded_crop_sha256':row['sha256'],'successful_display_count':row['successful_display_count']}
    assert set(crop_refs)==set(f'{i:02}' for i in range(1,19))
    crop_refs['19']=dict(crop_refs['10'],reuse_of_section='10',new_display=False)
    for s in sections:
        sections[s]['crop_audit_reference']=crop_refs[s]

    # Counts, confidence and kinds below are copied from the named journal
    # sections. Their addition is the only arithmetic performed here.
    specifications=[
        ('01','01','C025-G01','exact group',1,1,'high'),
        ('02','03','C025-S01','exact group',1,1,'medium'),
        ('03','04','C025-G02','exact group',1,1,'medium'),
        ('03','04','C025-E01','exact group',1,1,'medium'),
        ('04','05','C025-G03','exact group',1,1,'high'),
        ('05','06','C025-G04','exact group',1,1,'low'),
        ('06','07','C025-G05','exact group; one external limit',1,1,'medium'),
        ('06','08','A025-S02','exact complete parent including A025-M01 once',1,1,'medium'),
        ('07','09','C025-G06','exact group',1,1,'low'),
        ('08','10','C025-S03','exact group',1,1,'high'),
        ('08','11','C025-E02','one new outer unsure wrapper only',1,1,'medium'),
        ('08','12','C025-G07','exact group; no separate comma; shared endpoint count',1,1,'low'),
        ('09','13','C025-G08','exact group; five complete own C states',1,1,'low'),
        ('09','14','C025-S04','one new outer unsure wrapper only',1,1,'medium'),
        ('10','15','mut_raised_t_stop','exact firm mut\\textsuperscript{t}.',1,1,'high'),
        ('11','16','A025-G09','exact complete parent including A025-M02 once',1,1,'medium'),
        ('12','17','C025-S05','one new outer unsure wrapper only',1,1,'medium'),
        ('13','18','participle','only remove middle candidate déterminés from original C word',1,1,'medium'),
        ('14','19','C025-S06','one new outer unsure wrapper only',1,1,'medium'),
        ('14','21','C025-S07','one new outer unsure wrapper only',1,1,'medium'),
        ('15','22','B025-G09','exact complete que/descender/point group',1,1,'medium'),
        ('16','23','B025-G08','exact brace group',1,1,'high'),
        ('16','24','A025-S08','exact group including additional alpha-internal path',1,1,'high'),
        ('16','24','final_set_endpoint','no closing brace; separate endpoint',0,1,'high'),
        ('17','25','B025-M01','exact child and full native shared outer lower frame',1,1,'low'),
        ('18','26','B025-M02','exact child and full native shared outer lower frame',1,1,'low'),
        ('19','15','disjoints_endpoint','no final point; separate endpoint and physical-edge limit',0,1,'medium'),
    ]
    expected=[]
    for i,(s,locus,key,transform,c,h,confidence) in enumerate(specifications,1):
        kind='drawing or diagram'
        if key=='mut_raised_t_stop':kind='abbreviation expanded or spelling modernised'
        if key=='participle':kind='misread word'
        if key in ['final_set_endpoint','disjoints_endpoint']:kind='text not on the page'
        expected.append({'qa_selection_key':key,'qa_cluster_ordinal':i,'source_locus':'L025-'+locus,'root_section':s,'root_section_ref':sections[s]['source_ref'],'crop_audit_reference':crop_refs[s],'authorized_transform':transform,'authorized_count_C':c,'authorized_count_H':h,'authorized_confidence':confidence,'authorized_kind':kind,'authorized_marked_in_H':False})
    ctotal=sum(x['authorized_count_C'] for x in expected)
    htotal=sum(x['authorized_count_H'] for x in expected)
    assert (ctotal,htotal)==(25,27)
    assert 'C25, H27' in journal
    assert sum(x['authorized_count_C']==1 and x['authorized_count_H']==1 for x in expected)==25
    by_locus={row['id']:[] for row in union['source_locus_union']}
    for row in expected:by_locus[row['source_locus']].append(row)
    ordinary_sections={'L025-02':['01','19'],'L025-20':['14','19'],'L025-27':['19'],'L025-28':['19']}
    source_coverage=[]
    for raw in union['raw_row_correspondence']:
        selections=by_locus[raw['locus']]
        sids=sorted(set(x['root_section'] for x in selections)|set(ordinary_sections.get(raw['locus'],[])))
        assert sids
        source_coverage.append({'original_row_id':raw['id'],'reader':raw['reader'],'section':raw['section'],'original_index':raw['original_index'],'original_identity':raw['original_identity'],'original_source_ref':raw['raw'],'source_locus':raw['locus'],'root_sections':sids,'root_section_refs':[sections[s]['source_ref'] for s in sids],'selection_scope_keys':[x['qa_selection_key'] for x in selections],'original_semantic_role':'own-reader row and its raw witness fields; preserved in full','coverage_note':'Complete locus scope mapping; a multi-part source group remains complete in its own-reader role. Root physical count parents remain separate from original report-row identities.'})
    assert len(source_coverage)==216
    counts={s:sum(x['section']==s for x in source_coverage) for s in ['differences','doubts','inventory']}
    assert counts=={'differences':77,'doubts':47,'inventory':92}
    canonical=[]
    row_sections=['02','03','03','06','08','09','10','13']
    for i,row in enumerate(union['canonical_original_C_rows']):
        canonical.append({'source_id':row['source_id'],'source_parts':row['source_parts'],'canonical_catalog_ref':row['canonical_catalog_ref'],'reader_reported_scopes':row['reader_reported_scopes'],'root_section':row_sections[i],'root_section_ref':sections[row_sections[i]]['source_ref'],'authorized_status':'resolved' if i==6 else 'retained','authorized_scope_note':'Two surviving complete whole-word candidates; first-accent scope settled and final-accent allocation retained.' if i==7 else 'Original row scope retained separately from any new local qualification or literal group count.'})
    wrappers=['C025-E02','C025-S04','C025-S05','C025-S06','C025-S07']
    selected_group_ids=[x['qa_selection_key'] for x in expected if x['qa_selection_key'] in union['complete_own_groups']]+['A025-M01','A025-M02']
    result={
        'scan':25,'stage':'post-root authority mapping before frozen assembled handoff','source_only':True,
        'authority':{'journal_path':journal_path,'journal_sha256_utf8':sha(journal),'crop_audit_path':audit_path,'crop_audit_sha256_utf8':sha(audit_raw),'union_path':'out/checks/scan025_source_union_v01.json','union_sha256_utf8':sha(union_raw)},
        'root_sections':sections,'expected_authorized_clusters':expected,'source_row_coverage':source_coverage,
        'source_row_counts':counts,'canonical_original_C_rows':canonical,
        'expected_selected_group_ids':selected_group_ids,
        'wrapper_only_groups':wrappers,
        'nested_groups_zero_duplicate_count':{'A025-M01':'A025-S02','A025-M02':'A025-G09'},
        'participle_exact_change':{'old':'\\unsure{determinés|déterminés|determines}','new':'\\unsure{determinés|determines}','root_section':'13','original_reader_states_unchanged':True},
        'root_authorized_count_arithmetic':{'both_witness_clusters':25,'H_only_endpoints':['final_set_endpoint','disjoints_endpoint'],'C':ctotal,'H':htotal,'R_resolved':1,'R_retained':7,'all_selected_H_flags':False,'choice_source':'Root journal §§01–19; arithmetic and source correspondence only.'},
        'source_agreement_closure':{'root_section':'19','archive_literal':'% archive sheet number: 24','archive_hand':'undetermined hand','S_source_rows':7,'S_counts_C_H':[0,0],'S_root_ink_choice_applied':False,'source_only_authority_ref':sections['19']['source_ref']},
        'post_assembly_replay':'pending frozen source025 handoff; stage1 replay is not repeated',
        'main_adjudicated':False,'main_approved':False,
    }
    output=OUT/'scan025_qa_assembly_authority_map.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'path':str(output.relative_to(BASE)),'sha256_utf8':sha(output.read_bytes()),'authority':result['authority'],'source_row_counts':counts,'selected_group_ids':selected_group_ids,'root_arithmetic':result['root_authorized_count_arithmetic']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
