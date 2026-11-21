import copy
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
C = BASE / 'out/checks'
files = {}
ref_count = 0

def getfile(path):
    p = Path(path)
    if not p.is_absolute():
        p = BASE / p
        if not p.exists():
            p = BASE / 'out' / path
    if p not in files:
        raw = p.read_bytes()
        files[p] = (raw, raw.decode('utf-8'), hashlib.sha256(raw).hexdigest())
    return files[p]

def pointer(obj, path):
    for key in path.split('/')[1:]:
        key = key.replace('~1', '/').replace('~0', '~')
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj

def ref(r):
    global ref_count
    raw, text, sha = getfile(r['path'])
    assert sha == r['sha256'], r['path']
    a, b = r['char_start'], r['char_end']
    body = text[a:b]
    assert hashlib.sha256(body.encode()).hexdigest() == r['body_sha256']
    if 'literal' in r:
        assert body == r['literal']
    if 'utf8_byte_start' in r:
        assert len(text[:a].encode()) == r['utf8_byte_start']
        assert len(text[:b].encode()) == r['utf8_byte_end']
    if 'json_pointer' in r:
        assert json.loads(body) == pointer(json.loads(text), r['json_pointer'])
    ref_count += 1
    return body

def walk(x):
    if isinstance(x, dict):
        if {'path','sha256','char_start','char_end','body_sha256'} <= x.keys():
            ref(x)
        for value in x.values():
            walk(value)
    elif isinstance(x, list):
        for value in x:
            walk(value)

def ordered_values(value, order):
    if isinstance(value, dict):
        assert value.keys() == order.keys()
        return {k: ordered_values(value[k], order[k]) for k in order}
    if isinstance(value, list):
        assert len(value) == len(order)
        return [ordered_values(a,b) for a,b in zip(value,order)]
    return value

def mutation(obj, path, exists, value):
    parts = path.split('/')
    parent = pointer(obj, '/'.join(parts[:-1]))
    key = parts[-1].replace('~1','/').replace('~0','~')
    if isinstance(parent, list):
        assert exists
        parent[int(key)] = copy.deepcopy(value)
    elif exists:
        parent[key] = copy.deepcopy(value)
    else:
        del parent[key]

def closure(oldref, newref, changes):
    oldbytes, oldtext, oldsha = getfile(oldref['path'])
    newbytes, newtext, newsha = getfile(newref['path'])
    assert oldsha == oldref['sha256'] and newsha == newref['sha256']
    old, new = json.loads(oldtext), json.loads(newtext)
    forward, inverse = copy.deepcopy(old), copy.deepcopy(new)
    for c in changes:
        hasold = c.get('old_present', 'old_exact_value' in c or 'old_value' in c)
        hasnew = c.get('new_present', 'new_exact_value' in c or 'new_value' in c)
        values = {}
        for side, exists in [('old',hasold),('new',hasnew)]:
            if not exists:
                continue
            key = side + '_exact_value'
            values[side] = json.loads(ref(c[key])) if key in c else c[side+'_value']
            if side+'_value' in c:
                assert values[side] == c[side+'_value']
            assert pointer(old if side=='old' else new, c['path']) == values[side]
        mutation(forward,c['path'],hasnew,values.get('new'))
        mutation(inverse,c['path'],hasold,values.get('old'))
    assert forward == new and inverse == old
    assert (json.dumps(ordered_values(forward,new),ensure_ascii=False,indent=2)+'\n').encode() == newbytes
    assert (json.dumps(ordered_values(inverse,old),ensure_ascii=False,indent=2)+'\n').encode() == oldbytes
    return {'changes':len(changes),'forward_exact_UTF8':True,'inverse_exact_UTF8':True}

v1 = json.loads((C/'scan024_source_bounded_closure_v01.json').read_text())
v2 = json.loads((C/'scan024_source_bounded_closure_v02.json').read_text())
results = {
    'record_v01':closure(v1['initial_record'],v1['current_record'],v1['record_changes']),
    'map_v01':closure(v1['initial_map'],v1['current_map'],v1['map_changes']),
    'record_v02':closure(v2['initial_record'],v2['current_record'],v2['changes']),
}
record = json.loads((C/'scan024_record_draft.json').read_text())
assert (C/'scan024_record_draft.json').read_bytes() == (C/'scan024_source_record_repaired_v02.json').read_bytes()
projection = json.loads((C/'scan024_source_public_projection_v02.json').read_text())
pool = projection['values']

def expand(x):
    if isinstance(x, dict):
        if set(x)=={'concat'}:
            return ''.join(pool[k] for k in x['concat'])
        return {k:expand(v) for k,v in x.items()}
    if isinstance(x, list):
        return [expand(v) for v in x]
    return x

leaf_count = 0
def subset(actual, selected):
    global leaf_count
    if isinstance(selected, dict):
        for k,v in selected.items():
            subset(actual[k],v)
    elif isinstance(selected, list):
        assert len(actual)==len(selected)
        for a,b in zip(actual,selected):
            subset(a,b)
    else:
        assert actual==selected
        leaf_count += 1

subset(record,expand(projection['public_fields']))
before = ref_count
walk(record)
record_refs = ref_count-before
before = ref_count
walk(json.loads((C/'scan024_final_source_map.json').read_text()))
map_refs = ref_count-before
release = json.loads((C/'scan024_source_record_release_v02.json').read_text())
for path, sha in release['files'].items():
    assert getfile(path)[2] == sha
authority = json.loads((C/'scan024_root_doubt_alternatives_authorization.json').read_text())
for d in record['doubts']:
    assert d['alternatives']==authority['alternatives_by_doubt_id'][d['id']]
    related = [x for x in record['decisions'] if x['id']==d['decision_id']]
    assert len(related)==1 and related[0]['alternatives']==d['alternatives']
results.update({
    'scan':24,'record_sha256':getfile('out/checks/scan024_record_draft.json')[2],
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'reviewer':'root','source_only':True,'public_projection_exact_selected_leaves':leaf_count,
    'closure_and_current_reference_replays':ref_count,
    'current_record_references':record_refs,'current_map_references':map_refs,
    'release_hashes_verified':len(release['files']),
    'doubt_alternative_arrays_authority_exact':len(record['doubts']),
    'C_outcomes':dict(Counter(x['selected_outcome'] for x in record['C_source_rows'])),
    'limits':'Exact source and record binding review only; no image views or rendered/geometric/mathematical assertion.',
})
(C/'scan024_root_final_binding_review.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
