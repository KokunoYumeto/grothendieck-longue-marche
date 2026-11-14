from pathlib import Path
import hashlib,json
import numpy as np

root=Path(__file__).resolve().parent.parent
a=json.loads((root/'code/a_cm_distribution_orbifold_witnesses.json').read_text())
b=json.loads((root/'research/E68_self_replay/code/a_cm_distribution_orbifold_witnesses.json').read_text())
def differences(a,b,path=()):
    if isinstance(a,dict) and isinstance(b,dict):
        assert a.keys()==b.keys()
        return [x for k in a if k not in {'seconds','total_seconds'} for x in differences(a[k],b[k],path+(k,))]
    if isinstance(a,list) and isinstance(b,list):
        assert len(a)==len(b)
        return [x for i,(u,v) in enumerate(zip(a,b)) for x in differences(u,v,path+(i,))]
    return [] if a==b else [{'path':list(path),'old':a,'new':b}]
diff=differences(a,b)
assert len(diff)==1
assert diff[0]['path']==['input_sha256','a_cm_distribution_orbifold.json']
maina=json.loads((root/'code/a_cm_distribution_orbifold.json').read_text())
mainb=json.loads((root/'research/E68_self_replay/code/a_cm_distribution_orbifold.json').read_text())
assert not differences(maina,mainb)
for stem in ['a_cm_distribution_orbifold','a_cm_distribution_orbifold_witnesses']:
    aa=np.load(root/'code'/(stem+'.npz'))
    bb=np.load(root/'research/E68_self_replay/code'/(stem+'.npz'))
    assert aa.files==bb.files and all(np.array_equal(aa[k],bb[k]) for k in aa.files)
out={'status':'EXACT_REPLAY_DIAGNOSIS','only_nonruntime_difference':diff,
     'reason':'Dependent certificate records the byte hash of the preceding JSON, whose runtime differs.',
     'all_preceding_mathematical_JSON_fields_equal':True,'both_NPZ_arrays_equal':True}
(root/'research/E68_replay_diagnosis.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
