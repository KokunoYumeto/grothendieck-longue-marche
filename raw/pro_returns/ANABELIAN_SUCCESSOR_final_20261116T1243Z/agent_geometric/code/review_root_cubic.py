"""Read-only independent review of AR.15--16 and their retained census data.

No root output is overwritten.  This checks the symbolic converse identities,
re-evaluates the geometric theta flag for every recorded arithmetic model,
and independently joins it with all successful base-field cubic characters.
"""
from pathlib import Path
import sys, json, csv, collections
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]/'code'
sys.path.insert(0,str(ROOT))
from A4_cubic_classification import theta3_flags

a,b,c=sp.symbols('a b c')
relation=sp.Poly((a+b+c)**3+a*b*c,a,b,c,modulus=2)
identities=[]
for numerator,quotient in [
    (a*(a+c)**3+b*(b+c)**3,a+b),
    (a*(a+b)**3+c*(b+c)**3,a+c),
]:
    q,r=sp.div(sp.Poly(numerator,a,b,c,modulus=2),relation)
    assert r.is_zero and q==sp.Poly(quotient,a,b,c,modulus=2)
    identities.append(str(q.as_expr()))

reported=collections.defaultdict(list)
with (ROOT/'A4_cubic_classification.csv').open() as stream:
    for row in csv.DictReader(stream):
        reported[(int(row['q']),int(row['model_id']))].append(row)
counts={}
positive_f4=set()
base_f4=set()
for q,modulus,ext in [(4,7,67),(8,11,529),(16,19,4105)]:
    total=positive=geometric_models=models=0
    for rec,flag in theta3_flags(q,modulus,ext):
        models+=1; geometric_models+=int(flag)
        n=rec['rational_points']; total+=n
        good={json.dumps(t['point']) for t in rec['tests']
              if t['ell']==3 and t['relative_class_number_mod2']}
        assert len(good)<=n
        positive+=n if flag else len(good)
        rows=reported[(q,rec['index'])]
        assert len(rows)==n
        for row in rows:
            point=row['point']
            base=point in good
            exists=flag or base
            assert int(row['geometric_theta3_nonzero'])==flag
            assert int(row['base_field_cubic_witness'])==base
            assert int(row['cubic_witness_over_some_extension'])==exists
            if q==4 and exists:positive_f4.add((rec['index'],point))
            if q==4 and base:base_f4.add((rec['index'],point))
    counts[q]={'arithmetic_models':models,'geometric_theta3_models':geometric_models,
               'pointed_pairs':total,'least_prime_three':positive,
               'permanent_cubic_exclusion':total-positive}
assert [counts[q]['least_prime_three'] for q in (4,8,16)]==[264,3240,40284]
assert [counts[q]['pointed_pairs'] for q in (4,8,16)]==[730,9846,143990]

extra={}
with (ROOT/'A4_F4_extra_cubic.jsonl').open() as stream:
    for line in stream:
        rec=json.loads(line)
        for test in rec['tests']:
            if test['ell']==3 and test['relative_class_number_mod2']:
                key=(rec['model_id'],json.dumps(test['original_point']))
                extra[key]=min(extra.get(key,rec['q']),rec['q'])
assert set(extra)==positive_f4-base_f4
extra_counts=dict(collections.Counter(extra.values()))
assert extra_counts=={16:49,256:10}
assert {model for (model,_),q in extra.items() if q==256}=={71,87}

print(json.dumps({'symbolic_converse_quotients':identities,'census_counts':counts,
                  'extra_F4_witness_fields':extra_counts,
                  'all_retained_rows_reconciled':True,
                  'assertions':'all passed'},indent=2))
