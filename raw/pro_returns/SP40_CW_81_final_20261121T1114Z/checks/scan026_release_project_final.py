"""Finite source-only release projections. Existing v01 artifacts stay unchanged."""
import copy
import hashlib
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
P='scan026_release_'
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def read(n):return json.loads((OUT/n).read_text())
def save(n,v):
    assert n.startswith(P)
    b=enc(v);(OUT/n).write_bytes(b)
    return {'path':'out/checks/'+n,'sha256':sha(b),'bytes':len(b)}
def ref(n,p):return {'path':'out/checks/'+n,'json_pointer':p}
def ptr(v,p):
    for k in p.split('/')[1:] if p else []:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
    return v
def span(path,a,b,scope):
    raw=(BASE/path).read_bytes();s=raw.decode();value=s[a:b]
    return {'path':path,'source_sha256':sha(raw),'char_start':a,'char_end':b,'utf8_byte_start':len(s[:a].encode()),'utf8_byte_end':len(s[:b].encode()),'line_start':s.count('\n',0,a)+1,'line_end':s.count('\n',0,b-1)+1,'literal':value,'literal_sha256':sha(value.encode()),'scope':scope}

old_scalar=read(P+'scalar_review_v01.json')
old_witness=read(P+'witness_bindings_v01.json')
authority=read('scan026_root_scalar_authority_v01.json')
assert sha((OUT/(P+'scalar_review_v01.json')).read_bytes())==authority['input_scalar_sha256']
contract=read('scan026_source_selected_contract_v01.json')
assert sha((OUT/'scan026_source_selected_contract_v01.json').read_bytes())=='31635052f19c29904453133ad8c18c7607dcb39b9ddbdb4ff45c54905fc0bc5b'
contract_indices={x['locus_id']:i for i,x in enumerate(contract['loci'])}
sid=next(i for i,x in enumerate(old_scalar['rows']) if x['source_locus_id']=='S06')
Cpath='packets/026/C.tex';Ctext=(BASE/Cpath).read_text();Cvalue=r'\deleted{\unsure{$\Sigma_{\alpha}$|les}}'
assert Ctext.count(Cvalue)==1
a=Ctext.index(Cvalue);Cspan=span(Cpath,a,a+len(Cvalue),'complete deleted qualifier governing S06')
Hcatalog=read('scan026_H_marker_catalog.json')
Hmarker=next(x for x in Hcatalog['uncertainty_macros'] if x['source_id']=='H026-U05')
Hspan=span('packets/026/H.tex',Hmarker['char_start'],Hmarker['char_end'],'exact local U05 illegibility marker following connexes')
assert Hspan['literal']==Hmarker['literal']==r'\ill{}'
new_witness=copy.deepcopy(old_witness);new_witness['rows'][sid]['witnesses']={'C':[Cspan],'H':[Hspan]}
final_scalar=copy.deepcopy(authority['rows'])
before_scalar=copy.deepcopy(final_scalar[sid])
final_scalar[sid]['C']=[Cspan['literal']];final_scalar[sid]['H']=[Hspan['literal']]
final_scalar[sid]['witness_scope']={'C':[Cspan['scope']],'H':[Hspan['scope']]}
scalar_changes=[{'pointer':f'/rows/{sid}/'+k,'before':before_scalar[k],'after':final_scalar[sid][k]} for k in ['C','H','witness_scope']]
new_scalar={'schema':'scan026-root-scalar-authority-projection-v02','source_only':True,'main_approved':False,'root_authority_ref':ref('scan026_root_scalar_authority_v01.json',''),'rows':final_scalar}
for i,row in enumerate(final_scalar):
    for key in authority['rows'][i]:
        if not(i==sid and key in ['C','H','witness_scope']):assert compact(row[key])==compact(authority['rows'][i][key])
assert sum(x['diff_C'] for x in final_scalar)==70 and sum(x['diff_H'] for x in final_scalar)==82
assert sum(x['remaining_doubt'] for x in final_scalar)==66
witness_manifest=save(P+'witness_bindings_v02.json',new_witness)
scalar_manifest=save(P+'scalar_authority_projection_v02.json',new_scalar)
old_audit=read(P+'audit_v01.json');new_audit=copy.deepcopy(old_audit)
audit_changes=[]
for i,row in enumerate(new_audit['rows']):
    lid=row['source_locus_id']
    for key,new_value in [
        ('scalar_review_ref',ref(P+'scalar_authority_projection_v02.json',f'/rows/{i}')),
        ('root_selected_source_contract',ref('scan026_source_selected_contract_v01.json',f'/loci/{contract_indices[lid]}')),
    ]:
        audit_changes.append({'pointer':f'/rows/{i}/'+key,'before':row[key],'after':new_value});row[key]=new_value
    if lid=='S06':
        audit_changes.append({'pointer':f'/rows/{i}/exact_witnesses','before':row['exact_witnesses'],'after':new_witness['rows'][i]['witnesses']})
        row['exact_witnesses']=new_witness['rows'][i]['witnesses']
new_audit['schema']='scan026-complete-source-audit-proposal-v02'
audit_changes.append({'pointer':'/schema','before':old_audit['schema'],'after':new_audit['schema']})
new_audit['pending_root_fields']=['selected_public_inventory_assignment','final_record_approval']
audit_changes.append({'pointer':'/pending_root_fields','before':old_audit['pending_root_fields'],'after':new_audit['pending_root_fields']})

def set_pointer(v,p,value):
    bits=p.split('/')[1:];parent=v
    for k in bits[:-1]:parent=parent[int(k)] if isinstance(parent,list) else parent[k]
    k=bits[-1];parent[int(k) if isinstance(parent,list) else k]=value
forward=copy.deepcopy(old_audit)
for op in audit_changes:
    assert compact(ptr(forward,op['pointer']))==compact(op['before']);set_pointer(forward,op['pointer'],copy.deepcopy(op['after']))
assert enc(forward)==enc(new_audit)
inverse=copy.deepcopy(new_audit)
for op in reversed(audit_changes):
    assert compact(ptr(inverse,op['pointer']))==compact(op['after']);set_pointer(inverse,op['pointer'],copy.deepcopy(op['before']))
assert enc(inverse)==(OUT/(P+'audit_v01.json')).read_bytes()
audit_manifest=save(P+'audit_v02.json',new_audit)
correction=save(P+'S06_scope_correction_v01.json',{
    'authority':'Root source-only witness correction after full scalar/witness reading; selected source and all flags remain as authorized.',
    'locus_id':'S06','old_scalar_exact_ref':ref(P+'scalar_review_v01.json',f'/rows/{sid}'),
    'old_witness_exact_ref':ref(P+'witness_bindings_v01.json',f'/rows/{sid}'),
    'root_authority_exact_ref':ref('scan026_root_scalar_authority_v01.json','/required_source_correction'),
    'old_witness_value':old_witness['rows'][sid]['witnesses'],'corrected_witness_value':new_witness['rows'][sid]['witnesses'],
    'scalar_changes':scalar_changes,'new_scalar':scalar_manifest,'new_witness':witness_manifest,
    'no_selected_source_change':True,'all_root_scalar_fields_preserved_except_authorized_witness_correction':True,
})
delta=save(P+'audit_v01_to_v02_delta.json',{'old_sha256':sha((OUT/(P+'audit_v01.json')).read_bytes()),'new_sha256':audit_manifest['sha256'],'operations':audit_changes,'forward_exact_bytes':True,'inverse_exact_original_bytes':True,'all_original_v01_files_preserved':True})
print(json.dumps({'correction':correction,'scalar':scalar_manifest,'audit':audit_manifest,'delta':delta},ensure_ascii=False))
