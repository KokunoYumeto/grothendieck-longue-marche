"""Root-selected crop coverage; source checks only, no image display."""
from pathlib import Path
from datetime import datetime, timezone
from collections import OrderedDict
import json, hashlib

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out'
CHECKS=OUT/'checks'
sha=lambda b:hashlib.sha256(b).hexdigest()
packed=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
pretty=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
registry=json.loads((CHECKS/'scan026_source_union_sources_v01.json').read_bytes())
original={}
for key,item in registry.items():
    data=(BASE/item['path']).read_bytes()
    assert len(data)==item['bytes'] and sha(data)==item['sha256']
    original[key]=json.loads(data) if item['path'].endswith('.json') else data.decode()
def resolve(ref):
    value=original[ref['source']]
    for token in ref['json_pointer'].split('/')[1:]:
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value
pool=json.loads((CHECKS/'scan026_source_union_state_pool_v01.json').read_bytes())
for row in pool:
    if 'ordered_fields' in row:
        value=OrderedDict((f['key'],f['value'] if 'value' in f else resolve(f['exact_value_ref'])) for f in row['ordered_fields'])
    else:
        value=row['value']
    assert packed(value)==packed(resolve(row['raw_ref']))
replay=json.loads((CHECKS/'scan026_source_union_replay_v01.json').read_bytes())
rows=[]
for item in replay['review_files']:
    data=(BASE/item['path']).read_bytes()
    assert len(data)==item['bytes'] and sha(data)==item['sha256']
    rows.extend(json.loads(line) for line in data.splitlines())
union=json.loads((CHECKS/'scan026_source_union_v01.json').read_bytes())
assert packed(rows)==packed(union)
for row in union:
    spans=list(row['witness_source_spans'])
    for scopes in row['reader_sources'].values():
        spans.extend(scopes['local_source_spans'])
    for span in spans:
        literal=original[span['source']][span['start_char']:span['end_char_exclusive']]
        assert sha(literal.encode())==span['sha256']
        if 'literal' in span:
            assert literal==span['literal']

metadata={w:original[w+'.crops'] for w in 'ABC'}
plan=[]
def existing(w,filename,loci,note=''):
    matches=[r for r in metadata[w] if Path(r['path']).name==filename]
    assert len(matches)==1
    item=matches[0]
    path=f'readers/026/{w}/'+item['path']
    data=(OUT/path).read_bytes()
    expected=item.get('sha256',item.get('crop_sha256'))
    if expected: assert sha(data)==expected
    plan.append({'section':f'{len(plan)+1:02d}','path':path,'reader':w,'created_by_root':False,
        'bbox':item['bbox'],'rotation':item.get('rotation',item.get('rotation_degrees_PIL_counterclockwise',0)),
        'sha256':sha(data),'source_loci':loci,'target_scope_note':note})
def new(name,box,loci,note):
    plan.append({'section':f'{len(plan)+1:02d}','path':'crops/scan026_'+name+'.png',
        'reader':None,'created_by_root':True,'bbox':box,'rotation':0,'width':3000,
        'source_loci':loci,'target_scope_note':note})
existing('A','crop_01_title.png',['L001'])
new('second_ens',[430,215,790,285],['L002'],'No reader made a dedicated crop of the second ens and its following gap; all three report exact native positions.')
existing('A','crop_02_family.png',['S01','L003'])
new('first_quotes',[850,260,1470,365],['L004'],'The opening naming parenthesis is in B inventory box [580,278,1445,350]; family token and alphabet lie left of this new word-and-context box. No reader crop covers the complete quoted naming phrase.')
existing('B','02_interest.png',['L005'])
existing('C','17_hemispheres.png',['L006'])
existing('C','04_inserted_formula.png',['S02','L008','S03','S04','S05','S06'],'This complete crop includes the body Sigma above the three inserted terms. Its right edge precedes the et où target, reserved for section09.')
existing('C','18_de_plus.png',['L007'])
existing('B','04_interlinear.png',['L009'],'Only et où and its own baseline attachment are newly adjudicated here. The already decided inserted terms appear as context and are not reopened.')
existing('B','05_si_condition.png',['S07','L010'])
existing('A','crop_06_connexe_correction.png',['L011','S08'])
existing('A','crop_07_aussitot.png',['L012'])
existing('A','crop_08_margin.png',['L015','L016','L017','L018','L019','S15','S16'])
existing('A','crop_09_closure_first.png',['S09','L014'],'The pale arc at the left context boundary is reserved for the existing complete B17 crop in section15; no arc decision is made from this clipped context.')
existing('B','17_pale_arc.png',['L013'],'Complete arc target only; adjoining formula context is not reopened.')
existing('A','crop_10_closure_equation.png',['S10','L020','S11','S12'])
existing('B','09_parenthesis_end.png',['L021','S13','L022','L023','L024','L025','S14','L026','L027'],'Existing complete B crop includes the lower word strokes and both separately located fleck groups; C09 clips some descenders and is not selected.')
existing('C','11_lower_heading.png',['L028'])
existing('A','crop_14_pairs_correction.png',['L029','S17','S18','L030','S19','S20','L031','L032'])
new('quelles_descender',[750,1635,930,1785],['L033'],'B GQDESC full native box [775,1666,904,1764] extends above its declared crop12 top1690. This fresh whole-word crop is the sole root decision view of the q and its complete descender.')
existing('A','crop_15_non_adjective.png',['L034','L035'])
existing('B','12_distinctes_insertion.png',['L036','L037'],'The following Sigma at the right boundary is reserved for section23. The previously decided q descender can appear as context and is not reopened.')
new('two_prose_sigmas',[900,1700,1550,1835],['S21','S22'],'No reader crop contains all of S22. B12 right1005 falls inside reported S21 boxes ending1016/1022. This complete pair-of-terms context is their sole root decision view.')
existing('B','13_first_display.png',['S23','L038','S24','L039','L040','L041'])
existing('B','14_first_bottom_row.png',['L042','L043','S25','L044','S26','L045','L046','S27','S28','S29'])
existing('B','15_second_bottom_row.png',['S30','S31','L047','S32','S33','S34'])
existing('A','crop_21_bottom.png',['S35','L048','S36','L049','S37','S38','S39','L050'])
covered=[loc for item in plan for loc in item['source_loci']]
assert len(covered)==len(set(covered))==89
assert set(covered)|{'L051'}=={row['locus_id'] for row in union}
assert len(plan)==27 and len({item['path'] for item in plan})==27
now=datetime.now(timezone.utc).isoformat()
document={'scan':26,'created_by':'/root','at_utc':now,'source_image':'source/SP40_CW_81_scans/J81-03_81_scan026.jpg',
    'source_image_sha256':'6a0ff5c611f2f484417f4e879a7707953ad85340003248dd265c3059fbf9773c',
    'whole_or_halves_seen_by_root':False,'plan':plan,
    'agreed_locus_without_new_root_crop':{'locus_id':'L051','reading':'archive25, comment only; undetermined hand',
        'evidence':'A /inventory/77; B /inventory/93; C /inventory/86 all explicitly agree after their prescribed visual readings. No reader or witness difference or conflicting hand attribution is recorded for this numeral.'},
    'planned_distinct_crops':27,'new_crops':4,'existing_crops':23,
    'all90_loci_accounted_for':True,'all1106_pool_records_exact_raw_replay_verified_by_root':True,
    'all16_union_chunks_and_all90_rows_fully_read_by_root':True,
    'truncated_union_delivery_recovered':'S15 and S16 fully reread separately; no image delivery was involved.',
    'S15S16_source_observation_correction':'scan026_source_union_S15S16_delta_v02.json',
    'no_image_opened_by_this_script':True}
assert not (CHECKS/'scan026_root_crop_plan.json').exists()
(CHECKS/'scan026_root_crop_plan.json').write_bytes(pretty(document))
print(json.dumps({'planned':27,'new':4,'reused':23,'loci':90,'utc':now},indent=2))
