#!/usr/bin/env python3
"""Reconstruct all long D31/D33 words from the retained textual certificates."""
from pathlib import Path
from itertools import product
import json
OUT=Path(__file__).resolve().parent
def inverse(w):return bytes(0 if a==0 else 3-a for a in reversed(w))
def comm(a,b):return a+b+inverse(a)+inverse(b)
def select(mask,words):
    out=bytearray()
    while mask:
        bit=mask&-mask;out.extend(words[bit.bit_length()-1]);mask^=bit
    return bytes(out)
def central(mask,words,pairs,power=1):
    out=bytearray()
    while mask:
        bit=mask&-mask;i,j=pairs[bit.bit_length()-1]
        out.extend((words[i]*2 if i==j else comm(words[i],words[j]))*power);mask^=bit
    return bytes(out)
def seed_words(R):
    J30=json.loads((OUT/'d_cm_rank4_joint.json').read_text())['witness']
    J31all=json.loads((OUT/'d_cm_rank4_degree7.json').read_text());J31=J31all['witness']
    old=[bytes(w) for w in R['Nwords']]
    pairs=[(i,j) for i in range(97) for j in range(i,97)]
    U=[bytes(w) for w in R['Wwords']]
    for i,j,k in J31all['degree7_basis_indices']:
        U.append(comm(bytes(R['relwords'][i]),comm(bytes(R['relwords'][j]),bytes(R['lieword'](R['L3'][k])))))
    out={}
    for name,rname in (('beta','wb'),('A','wa')):
        w=(central(int(J30['upper_'+name+'_correction'],16),old,pairs,2)
          +central(int(J30['previous_Z4_'+name+'_central_change'],16),old,pairs)+bytes(R[rname]))
        w=select(int(J30['gamma3N_'+name+'_correction'],16),U[:240])+w
        w=(central(int(J31['upper_'+name+'_correction'],16),old,pairs,2)
          +central(int(J31['lower_'+name+'_change'],16),old,pairs)+w)
        w=select(int(J31['gamma3N_'+name+'_correction'],16),U)+w
        out[name]=w
    assert J30['lambda_mod288']==J31['lambda_mod288']==1
    assert 2*(len(out['beta'])+len(out['A']))+4==J31['corrected_B_word_length']==4903248
    return out
def joint_words(R):
    seed=seed_words(R)
    J=json.loads((OUT/'d_cm_degree8_joint.json').read_text())['witness'];assert J is not None
    H=json.loads((OUT/'d_cm_degree8_high.json').read_text())
    old=[bytes(w) for w in R['Nwords']]
    new=[bytes(w) for w in H['actual_Nielsen_basis_B_words']]
    pairs=[(i,j) for i in range(97) for j in range(i,97)]
    L4=[]
    for power,d in ((1,4),(2,2),(4,1)):
        for w in product(range(4),repeat=d):
            if R['lyndon'](w):L4.append(bytes(R['lieword'](w))*power)
    base={'2':[bytes(w) for w in R['relwords']],
          '3':[bytes(R['lieword'](w)) for w in R['L3']],'4':L4}
    labels=json.loads((OUT/'d_cm_degree8_gamma3.json').read_text())['basis_labels']
    def triples(mask):
        out=bytearray()
        while mask:
            bit=mask&-mask;typ,i,j,k=labels[bit.bit_length()-1]
            out.extend(comm(base[typ[0]][i],comm(base[typ[1]][j],base[typ[2]][k])));mask^=bit
        return bytes(out)
    out={'lambda':J['lambda']}
    for name in ('beta','A'):
        cor=(triples(int(J['gamma3_'+name+'_change'],16))
            +central(int(J['upper_old_C1_'+name+'_change'],16),old,pairs,2)
            +central(int(J['high_C1_'+name+'_change'],16),new,H['high_C1_pairs']))
        out[name+'_correction']=cor;out[name]=cor+seed[name]
    return out
if __name__=='__main__':
    from contextlib import redirect_stdout
    import io,runpy,hashlib
    with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
    J=joint_words(R)
    result={'seed_B_cusp_word_length':4903248,
     'joint_B_cusp_word_length':2*(len(J['beta'])+len(J['A']))+2+2*J['lambda'],
     'beta_sha256':hashlib.sha256(J['beta']).hexdigest(),
     'A_sha256':hashlib.sha256(J['A']).hexdigest(),
     'all_words_reconstructed_from_textual_certificates':True}
    assert result['joint_B_cusp_word_length']==12921196
    print(json.dumps(result,indent=2))
