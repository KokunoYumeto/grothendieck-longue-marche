#!/usr/bin/env python3
"""Independently compare every literal finite replay input with original data."""
from pathlib import Path
import re,json,hashlib
r=Path(__file__).resolve().parent
p=r/'pbc_top_two_cover_source_fast.g'
t=p.read_text()
sp=r/'pbc_iterated_shortcut_v2_original_source.json'
s=json.loads(sp.read_text())
sec=json.loads((r/'pbc_top_two_section.json').read_text())
m=re.search(r'D:=rec\(orders:=(\[.*?\]),powers:=(\[.*?\]),conjugates:=(\[.*?\]),section:=(\[.*?\])\);;',t,re.S)
assert m
D=[json.loads(v) for v in m.groups()]
assert D[:3]==[s['relative_orders'],s['powers'],s['conjugates']]
section=[]
for g in range(1,105):
    a=int(sec['quotient_generator_corrections_hex'][str(g)],16)
    section.append([g,1]+[x for k in range(72) if (a>>k)&1 for x in (k+105,1)])
assert D[3]==section
pairs=json.loads(re.search(r'PBC_pairs:=(\[.*?\]);;',t,re.S).group(1))
ss,rr=s['s'],s['r'];aa,bb=s['s_image'],s['r_image']
bs,br=s['left_s_frame'],s['left_r_frame']
expected=[['target_s',bs+ss,aa+bs],['target_r',br+rr,bb+br],['target_product',aa+bb,ss+rr]]
expected += [[f's_frame_{i}',w+ss,ss+w] for i,w in enumerate(s['s_centralizers'],1)]
expected += [[f'r_frame_{i}',w+rr,rr+w] for i,w in enumerate(s['r_centralizers'],1)]
assert pairs==expected and len(pairs)==83
out={'status':'PASS','script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'original_source_sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),
     'all_finite_presentation_data_exact':True,'all104_section_words_exact':True,
     'all83_pairs_match_original_source':True}
(r.parent/'notes/fgh_top_two_source_fast_input_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
