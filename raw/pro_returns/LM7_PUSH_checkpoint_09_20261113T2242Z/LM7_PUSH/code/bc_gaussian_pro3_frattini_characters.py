#!/usr/bin/env python3
"""The actual twelve Frattini characters, including all weight-three terms."""
from pathlib import Path
import hashlib
import itertools
import json
import numpy as np

from bc_gaussian_pro3_frattini_model import X,Y,ONE,mul,inv,power,comm,collect,uinv,rank3
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent


def main():
    model=np.load(HERE/'bc_gaussian_pro3_frattini_model.npz')
    elements=[tuple(tuple(map(int,u)) for u in g) for g in model['P_elements']]
    coords=[tuple(map(int,u)) for u in model['P_Hall_coordinates']]
    at={g:i for i,g in enumerate(elements)};coord={g:q for g,q in zip(elements,coords)}
    c=comm(X,Y)
    pairs={'A':(mul(inv(X),c),mul(inv(Y),c)),
           'B':(mul(Y,c),mul(inv(X),c))}
    automorphisms={}
    for name,(xx,yy) in pairs.items():
        images=[collect(*q,xx=xx,yy=yy) for q in coords]
        assert len(set(images))==2187
        for i,g in enumerate(elements):
            for a,b in ((X,xx),(Y,yy)):
                assert images[at[mul(g,a)]]==mul(images[i],b)
        automorphisms[name]=images
    pts=list(itertools.product(range(3),repeat=3));pos={p:i for i,p in enumerate(pts)}
    def perm(g):
        out=[]
        for j,a in enumerate(g):
            r,s,t,u,v,w=uinv(a)
            out.extend(27*j+pos[((x+r*y+u*z+w)%3,(y+s*z+v)%3,(z+t)%3)] for x,y,z in pts)
        return np.array(out,dtype=np.uint16)
    lookup={perm(g).tobytes():g for g in elements}

    def decode(p):
        assert len(p)==2592
        gs=[]
        for i in range(6):
            q=p[432*i:432*(i+1)]-432*i
            g=lookup[q[:108].tobytes()]
            assert np.all(q[:108]<108)
            gs.append(g)
        return gs

    def characters(p):
        gs=decode(p);out=[]
        for i,j,name in [(0,5,'B'),(1,4,'B'),(2,3,'A')]:
            g,h=gs[i],gs[j]
            delta=mul(h,inv(automorphisms[name][at[g]]));q=coord[delta]
            assert q[:3]==(0,0,0),q
            out.extend([coord[g][0]%3,coord[g][1]%3,q[3],q[4]])
        return np.array(out,dtype=np.uint8)

    certificate=read_certificate(HERE/'bc_gaussian_pro3_common_Gaussian.bin')
    verify_words(certificate)
    vals=np.array([characters(g) for g in certificate['strong']],dtype=np.uint8)
    assert rank3(vals)==12
    original=np.array([characters(g) for g in certificate['original']],dtype=np.uint8)
    # Independently evaluate every saved word in the additive character
    # target, and compare it with the actual six-matrix decoding.
    dagvals=[]
    for op,a,b in certificate['nodes']:
        op,a,b=map(int,(op,a,b))
        if op==0:v=np.zeros(12,dtype=np.int64)
        elif op==1:v=original[a].astype(np.int64)
        elif op==2:v=(dagvals[a]+dagvals[b])%3
        elif op==3:v=-dagvals[a]%3
        elif op==4:v=np.zeros(12,dtype=np.int64)
        elif op==5:v=dagvals[b]
        else:raise AssertionError(op)
        dagvals.append(v)
    for node,v in zip(certificate['words'],vals):assert np.array_equal(dagvals[int(node)],v)
    out={'status':'PASS_ALL_TWELVE_ACTUAL_GAUSSIAN_FRATTINI_CHARACTERS',
         'rank':12,'coordinate_order_per_pair':['first.X_mod3','first.Y_mod3',
                'last_times_lift(first)_inverse.gamma3_X',
                'last_times_lift(first)_inverse.gamma3_Y'],
         'pairs':[[1,6,'B'],[2,5,'B'],[3,4,'A']],
         'A_lift_images':[coord[mul(inv(X),c)],coord[mul(inv(Y),c)]],
         'B_lift_images':[coord[mul(Y,c)],coord[mul(inv(X),c)]],
         'half_power_explanation':'-[1/2]=1 mod3 on the order-three commutator subgroup',
         'all2187_automorphism_images_and_generator_products_checked':True,
         'actual_strong_generator_character_values':vals.tolist(),
         'all_saved_character_word_DAG_values_checked':True,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
             ['bc_gaussian_pro3_frattini_model.py','bc_gaussian_pro3_frattini_model.npz',
              'bc_gaussian_pro3_common_Gaussian.bin']}}
    np.savez_compressed(HERE/'bc_gaussian_pro3_frattini_characters.npz',
                        strong_characters=vals,original_characters=original,
                        A_automorphism=np.array([at[g] for g in automorphisms['A']],dtype=np.uint16),
                        B_automorphism=np.array([at[g] for g in automorphisms['B']],dtype=np.uint16))
    (HERE/'bc_gaussian_pro3_frattini_characters.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
