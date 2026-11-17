"""Independent raw-word/free-pair strengthening of the same D_s test.

Keep only (B,000) and (bar d,001) after the complete retained-residue map.
The all-orbit omission is proved by one integral sum character, not search.
"""
from pathlib import Path
import json,hashlib

ROOT=Path(__file__).resolve().parents[2]
FP=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
SP=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
F=json.loads(FP.read_text());S=json.loads(SP.read_text())
RET={5:1,10:2,11:4}

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,im):return mul(*(im[abs(x)] if x>0 else inv(im[abs(x)]) for x in w))
def chi(w):return sum(1 if x in (5,10) else -1 if x in (-5,-10) else 0 for x in w)
def free_pair(w):
    t=0;out=[]
    for x in w:
        if abs(x) in RET:t^=RET[abs(x)]
        elif (abs(x),t)==(2,0):out.append(1 if x>0 else -1)
        elif (abs(x),t)==(8,4):out.append(2 if x>0 else -2)
    assert t==0
    return red(out)

heads={};preserved=[]
for name,op in F['all_four_signed_source_operators'].items():
    shifts={chi(r['conjugator_F11']) for r in op['family_images'].values()}
    assert len(shifts)==1
    heads[name]=shifts.pop()
    actual={int(k):v for k,v in S['source_ordinary_actions'][name].items()}
    for i in (5,10,11):
        assert chi(actual[i])==chi([i])
        preserved.append([name,i])
assert heads=={'m':0,'m_inverse':0,'v':-1,'v_inverse':1}

relevant=[];omissions=[]
for row in F['all40_node_factor_pairs']:
    a,b=row['first_factor'],row['second_factor']
    ca,cb=abs(a['signed_core']),abs(b['signed_core'])
    if {ca,cb}=={2,8}:
        if ca!=2:a,b=b,a
        diff=chi(a['conjugator_F11'])-chi(b['conjugator_F11'])
        assert diff in (-1,1)
        relevant.append({'side':row['side'],'name':row['name'],'sheet':row['sheet'],'sum_difference':diff})
        reason='B/bar-d core pair has invariant odd sum difference'
    else:reason='at least one of the two peripheral colors is omitted'
    omissions.append({'side':row['side'],'name':row['name'],'sheet':row['sheet'],'reason':reason})
assert len(omissions)==40 and relevant

raw=[x['fiber11'] for x in S['actual_six_source_normal_forms'][:4]]
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
U=mul(raw[0],inv(raw[3]),inv(raw[0]))
results=[]
for label,w in [('D_s',Ds),('U_known',U)]:
    for name in ('m','m_inverse'):
        im={int(k):v for k,v in S['source_ordinary_actions'][name].items()}
        defect=mul(sub(w,im),inv(w))
        image=free_pair(defect)
        if label=='D_s':assert image==[2,-1,-2,1]
        else:assert image==[]
        results.append({'word':label,'operator':name,'raw_length':len(defect),'literal_free_pair_image':image})
        print(label,name,'literal free-pair image',image)

assert free_pair([2])==[1]
assert free_pair([11,8,-11])==[2]
def hmul(p,q):
    a,b,c=p;u,v,w=q
    return ((a+u)%2,(b+v)%2,(c+w+a*v)%2)
def hinv(p):a,b,c=p;return (a,b,(c+a*b)%2)
im={1:(1,0,0),2:(0,1,0)};z=(0,0,0)
for x in [2,-1,-2,1]:z=hmul(z,im[x] if x>0 else hinv(im[-x]))
assert z==(0,0,1)

out={'status':'PASS_ACTUAL_DISCRETE_AND_COMPACT_FREE_PAIR',
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (FP,SP)},
     'selected_vertices':{'X':{'color_F11':2,'bits':0},'Y':{'color_F11':8,'bits':4}},
     'uniform_signed_sum_head_shifts':heads,'retained_sum_checks':preserved,
     'all40_omission_reasons':omissions,'all_B_bar_d_seed_differences':relevant,
     'complete_raw_word_images':results,'actual_section_words':{'X':[2],'Y':[11,8,-11]},
     'finite_UT3_F2_image':list(z),
     'scope':'The uniform color/sum rule kills every source/deck translate even with nonlinear connectors. The continuous finite-residue map restricts to actual closed L/N, yielding a free-profinite two-generator retract. It need not be equivariant for the selected cone.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all40 omission rules, all32 uniform sum heads and12 retained sum checks.')
print('Exact source defects map to [Y,X^-1], detected by UT3(F2); both actual section words checked.')
