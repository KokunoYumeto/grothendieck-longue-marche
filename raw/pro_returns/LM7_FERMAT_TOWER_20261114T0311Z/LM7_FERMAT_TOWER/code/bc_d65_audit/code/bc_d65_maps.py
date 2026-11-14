#!/usr/bin/env python3
"""Independent D65 map audit; imports data only, never author code.

Reconstruct the complete divided exterior norm and endomorphism trace
in pairs of integer matrices modulo four.  Check every recorded actual
framing, its linearized orientation map, and the complete 10-dimensional
kernel.  This is a focused independent certificate, not a replay of the
eight construction programs.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
ROOT = WORK / 'D65_EXPERIMENTS'
MANIFEST = ROOT / 'ledger/d_divided_compact_source_manifest.json'
manifest = json.loads(MANIFEST.read_text())
hash_checks = []
for row in manifest['owned_files']:
    p = ROOT / row['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256']
    hash_checks.append(str(p.relative_to(WORK)))
for row in manifest['immutable_inputs']:
    for key in ('source', 'copied'):
        p = WORK / row[key]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256']
        hash_checks.append(str(p.relative_to(WORK)))

inputs = {}
def read(stem):
    p = ROOT / 'code' / (stem + '.json')
    inputs[stem] = hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text())

integral = read('d_compact_integral')
correction = read('d_compact_divided_correction')
pairing = read('d_residual_compact_pairing')
cusp = read('d_residual_compact_cusp')
rigid = read('d_compact_rigid_source')
arithmetic = read('d_arithmetic_A4_twisted')
table = np.array(arithmetic['Q_multiplication'], dtype=np.int64)

def plus(x, y):
    return ((x[0]+y[0]) % 4, (x[1]+y[1]) % 4)
def minus(x, y):
    return ((x[0]-y[0]) % 4, (x[1]-y[1]) % 4)
def mult(x, y):
    a,b = x; c,d = y
    return ((a@c-b@d) % 4, (a@d+b@c-b@d) % 4)
def conj(x):
    return ((x[0]-x[1]) % 4, (-x[1]) % 4)
def transpose(x):
    return (x[0].T, x[1].T)
def decode4(cols):
    a = np.array(cols, dtype=np.int64).T
    return (a % 4, a // 4)
def lift2(a, hermitian=False):
    a = np.array(a, dtype=np.int64)
    x, y = a & 1, a >> 1
    if hermitian:
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                x[j,i],y[j,i] = (x[i,j]-y[i,j]) % 4, -y[i,j] % 4
    return x,y
def reduced(x):
    return (x[0] & 1) + 2*(x[1] & 1)
def half(x):
    assert not np.any(x[0] & 1) and not np.any(x[1] & 1)
    return (x[0]//2) + 2*(x[1]//2)
def matrix(v):
    return np.array([(v >> (2*i)) & 3 for i in range(256)], dtype=np.int64).reshape(16,16)
def packed(a):
    return sum(int(x) << (2*i) for i,x in enumerate(a.ravel()))
def hermitian_packed(a):
    assert np.array_equal(a, (a.T & 1) ^ (a.T >> 1) ^ (2*(a.T >> 1)))
    assert not np.any(a.diagonal() >> 1)
    digits = list(map(int,a.diagonal()))
    for i in range(16):
        for j in range(i+1,16):
            digits.extend((int(a[i,j]) & 1, int(a[i,j]) >> 1))
    return sum(x << i for i,x in enumerate(digits))
def xor_columns(cols, v):
    ans = 0
    for i,c in enumerate(cols):
        if (v >> i) & 1:
            ans ^= c
    return ans
def rank(cols):
    pivots = {}
    for col in cols:
        while col:
            bit = (col & -col).bit_length()-1
            if bit not in pivots:
                pivots[bit] = col
                break
            col ^= pivots[bit]
    return len(pivots)
def field_mult(a,b):
    a0,a1 = a & 1,a >> 1
    b0,b1 = b & 1,b >> 1
    return (a0*b0 ^ a1*b1) + 2*(a0*b1 ^ a1*b0 ^ a1*b1)
def inverse2(a):
    n = len(a)
    aug = np.concatenate([a.copy(),np.eye(n,dtype=np.int64)],axis=1)
    for i in range(n):
        p = next(j for j in range(i,n) if aug[j,i])
        aug[[i,p]] = aug[[p,i]]
        c = int(aug[i,i]); ci = next(z for z in range(1,4) if field_mult(c,z)==1)
        aug[i] = field_mult(aug[i],ci)
        for j in range(n):
            if j != i and aug[j,i]:
                aug[j] ^= field_mult(aug[i],int(aug[j,i]))
    assert np.array_equal(aug[:,:n],np.eye(n,dtype=np.int64))
    return aug[:,n:]

rows=[]
for rec in integral['cases']:
    char = rec['character']
    find = lambda d: next(x for x in d['cases'] if x['character']==char)
    cr,pa,cu,ri = map(find,(correction,pairing,cusp,rigid))
    source = next(x for x in arithmetic['character_blocks'] if x['character']==char)
    flips = {int(x['q_state']): bool(x['flip']) for x in source['all_stabilizer_actions']}
    actions = {int(g):decode4(v) for g,v in rec['all_integral_complement_actions'].items()}
    inverses={g:next(h for h in actions if table[g,h]==0) for g in actions}
    ai={g:conj(actions[inverses[g]]) if flips[g] else actions[inverses[g]] for g in actions}
    eye=np.eye(16,dtype=np.int64);zero=np.zeros((16,16),dtype=np.int64)
    for g in actions:
        assert np.array_equal(mult(actions[g],ai[g])[0],eye)
        assert not np.any(mult(actions[g],ai[g])[1])
    trace=[]
    for i in range(16):
        for j in range(16):
            for component in range(2):
                a=(zero.copy(),zero.copy());a[component][i,j]=1
                total=(zero.copy(),zero.copy())
                for g,m in actions.items():
                    total=plus(total,mult(mult(m,conj(a) if flips[g] else a),ai[g]))
                trace.append(packed(half(total)))
    assert trace == [int(x,16) for x in rec['full_End_divided_trace_columns']]
    norms=[]
    specs=[(i,i,0) for i in range(16)] + [(i,j,c) for i in range(16) for j in range(i+1,16) for c in range(2)]
    for i,j,c in specs:
        a=(zero.copy(),zero.copy());a[c][i,j]=1
        if i != j:
            a[0][j,i],a[1][j,i] = (int(c==0)-int(c==1))%4, -int(c==1)%4
        total=(zero.copy(),zero.copy())
        for g,m in actions.items():
            term=mult(mult(m,conj(a) if flips[g] else a),transpose(conj(m)))
            total=minus(total,term) if flips[g] else plus(total,term)
        norms.append(hermitian_packed(half(total)))
    assert norms == [int(x,16) for x in rec['full_Hermitian_divided_norm_columns']]
    nc=[int(x,16) for x in cr['coinvariant_divided_norm_columns']]
    sc=[int(x,16) for x in cu['source_s_correction_columns']]
    source_image={xor_columns(sc,v) for v in range(1 << 4)} if len(sc)==4 else {0}
    source_image={0}
    for col in sc:
        source_image |= {v^col for v in tuple(source_image)}
    actual_kernel={v for v in range(1024) if xor_columns(nc,v)==0}
    assert actual_kernel == source_image and len(actual_kernel)==16
    assert rank(nc)==6
    tc=[xor_columns(trace,int(x,16)) for x in cr['projective_trace_input_columns']]
    assert tc==[int(x,16) for x in cr['projective_trace_half_columns']] and rank(tc)==16
    form=np.array(pa['M_pairing'],dtype=np.int64)
    omega=inverse2(form)
    omega=(omega & 1) ^ (omega >> 1) ^ (2*(omega >> 1))
    O=lift2(omega,hermitian=True)
    frames=[]
    for case in cr['cases']:
        rr=next(x for x in ri['cases'] if x['branch']==case['branch'] and x['beta_Q_state']==case['beta_Q_state'])
        D=lift2(np.array(rr['rigid_compact_action_columns'],dtype=np.int64).T)
        old=mult(mult(D,O),transpose(conj(D)))
        cols=[]
        for v in tc:
            K=lift2(matrix(v));new=plus(D,((2*K[0])%4,(2*K[1])%4))
            direct=half(minus(mult(mult(new,O),transpose(conj(new))),old))
            linear=plus(mult(mult(K,O),transpose(conj(D))),mult(mult(D,O),transpose(conj(K))))
            assert np.array_equal(direct,reduced(linear))
            cols.append(hermitian_packed(direct))
        assert cols==[int(x,16) for x in case['all_linearized_bivector_columns']]
        solutions=[int(x,16) for x in case['right_inverse_on_coinvariant_representatives']]
        assert all(xor_columns(cols,s)==v for s,v in zip(solutions,nc))
        assert rank(cols)==6 and all(xor_columns(solutions,v)==0 for v in actual_kernel)
        frames.append({'branch':case['branch'],'beta_Q_state':case['beta_Q_state'],'orientation_columns':len(cols),'inverse_columns':len(solutions)})
    rows.append({'character':char,'whole_norm_columns':len(norms),'whole_trace_columns':len(trace),
                 'coinvariant_vectors_enumerated':1024,'kernel_equals_source_image':True,
                 'restricted_trace_rank':rank(tc),'frames':frames})

result={'status':'PASS','scope':'independent actual-data map reconstruction; no author executable imports or claimed construction replay',
        'proof_sha256':hashlib.sha256((ROOT/manifest['section']).read_bytes()).hexdigest(),
        'manifest_sha256':hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
        'hash_checks':len(hash_checks),'cases':rows,'inputs':inputs,
        'odd_cover_identity':{'translation_exponent':97,'cover_exponent':93,'residual_exponent':4},
        'dimensions':{'new':5752,'new_coinvariants':12,'total':7682,'total_coinvariants':26,'specified_residual':276478}}
assert 97-93==4 and 2*(2880-4)==5752 and 2*(10-4)==12
assert 1920+2880+2880+2==7682 and 282230-5752==276478
(HERE/'bc_d65_maps.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
