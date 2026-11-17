"""One authorized exact-word class-two test, with whole-orbit level typing.

The result is stronger than a zero class-two coordinate: after killing
the retained f,g directions, both signed actual m operators are literally
the identity on the entire remaining free group.  Thus no detector using
only color and chi_x level can see this particular commutator.
"""
from pathlib import Path
import json,hashlib
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[2]
F=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
S=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
J=json.loads(F.read_text()); Q=json.loads(S.read_text())
family={1,2,3,4,6,7,8,9}
first={1,2,3,4};second={6,7,8,9}

def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x:s.pop()
        else:s.append(x)
    return s
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,images):return mul(*(images[abs(x)] if x>0 else inv(images[abs(x)]) for x in w))
def level_F3(w):return sum(1 if x==3 else -1 if x==-3 else 0 for x in w)
def level_F11(w):return sum(1 if x==11 else -1 if x==-11 else 0 for x in w)
def delete_fg(w):return red(x for x in w if abs(x) not in (5,10))

# Entire finite seed family.  In class two, nonlinear conjugators disappear
# only from the commutator, not from an arbitrary word evaluation.
allowed=defaultdict(set); node_rows=[]
for row in J['all40_node_factor_pairs']:
    a,b=row['first_factor'],row['second_factor']
    assert a['signed_core'] and b['signed_core']
    if abs(a['signed_core']) in second:a,b=b,a
    i,j=abs(a['signed_core']),abs(b['signed_core'])
    assert i in first and j in second
    la,lb=level_F3(a['retained_head']),level_F3(b['retained_head'])
    allowed[i,j].add(la-lb)
    node_rows.append({'side':row['side'],'name':row['name'],'sheet':row['sheet'],
                      'first_color':i,'second_color':j,'first_level':la,'second_level':lb,
                      'level_difference':la-lb,'first_signed_core':a['signed_core'],'second_signed_core':b['signed_core']})
assert len(node_rows)==40

# Uniform all-word consequence: signed source maps retain the same positive
# core, zero head level, and preserve chi_x on the retained quotient.
head_checks=0;retained_checks=0
for name,op in J['all_four_signed_source_operators'].items():
    for i,r in op['family_images'].items():
        assert r['signed_core']==int(i)
        assert level_F3(r['retained_head'])==0
        head_checks+=1
    # Use literal source images to avoid relying on a cached induced map.
    images={int(k):v for k,v in Q['source_ordinary_actions'][name].items()}
    for i in (5,10,11):
        assert level_F11(images[i])==(1 if i==11 else 0)
        retained_checks+=1
assert (head_checks,retained_checks)==(32,12)

# The entire retained-f,g filling, not just the chosen source word.
identity_checks=[]
for name in ('m','m_inverse'):
    images={int(k):v for k,v in Q['source_ordinary_actions'][name].items()}
    for i in range(1,12):
        expected=[] if i in (5,10) else [i]
        actual=delete_fg(images[i])
        assert actual==expected,(name,i,actual,expected)
        identity_checks.append({'operator':name,'generator':i,'projected_image':actual})

raw=[x['fiber11'] for x in Q['actual_six_source_normal_forms'][:4]]
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
assert level_F11(Ds)==0
word_checks=[]
for name in ('m','m_inverse'):
    images={int(k):v for k,v in Q['source_ordinary_actions'][name].items()}
    defect=mul(sub(Ds,images),inv(Ds))
    projected=delete_fg(defect)
    assert projected==[]
    word_checks.append({'operator':name,'defect_F11':defect,'raw_length':len(defect),
                        'free_color_level_projection':projected})

out={'status':'PASS_ZERO_TEST','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (F,S)},
     'all40_level_pairs':node_rows,
     'allowed_color_level_differences':[{'first_color':i,'second_color':j,'differences':sorted(v)} for (i,j),v in sorted(allowed.items())],
     'uniform_signed_head_checks':head_checks,'uniform_retained_level_checks':retained_checks,
     'all22_signed_m_free_projection_identities':identity_checks,
     'actual_Ds_F11':Ds,'Ds_color_level_projection':delete_fg(Ds),
     'actual_two_signed_defects':word_checks,
     'preserved_first_attempt':'Initial checker incorrectly asserted positive node cores. Node factor signs are irrelevant to the imposed commutation; repaired to absolute colors while preserving both signs. The all32 operator cores are still checked literally positive. Initial source/stdout/stderr retained.',
     'scope':'The exact actual [m,Ds] has zero image already in the free color/chi_x-level group. Therefore the entire authorized level-based class-two quotient cannot decide this word. No actual commutation is proved or refuted.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete40 seed color/level rows,32 signed peripheral heads and12 retained level checks.')
print('PASS stronger degeneracy: all22 signed m images are identity after deleting retained f,g.')
print('Both exact Ds defects vanish already in the free color/chi_x-level group; no class-two obstruction survives.')
print('Full defect lengths:',[x['raw_length'] for x in word_checks])
