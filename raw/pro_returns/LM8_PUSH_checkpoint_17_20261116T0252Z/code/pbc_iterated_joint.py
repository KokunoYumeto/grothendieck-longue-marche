#!/usr/bin/env python3
"""Retain both descent levels, prescribing zero first descended parity.

This strengthens the second-level finite test by requiring every first signed
evaluation of f to be the identity.  Actual full existence is a separate
centralization calculation, emitted as pbc_hopf_iterated_joint.g.
"""
from pathlib import Path
import json,runpy

HERE=Path(__file__).parent
d=runpy.run_path(str(HERE/'pbc_iterated_ghost.py'))
base=d['d']
DX,DY=d['DX'],d['DY']
induced=base['induced']
old=base['d']
mm,mi,gm,gi=old['mm'],old['mi'],old['gm'],old['gi']
I=old['I']

extra=[[],[]]
for mod in (3,4):
    mats=[(a,b,c,e) for a in range(mod) for b in range(mod) for c in range(mod) for e in range(mod) if (a*e-b*c)%mod==1]
    idx={a:i for i,a in enumerate(mats)}
    S=(0,1,mod-1,0);tau=(1,mod-1,0,1)
    letters={1:S,2:tau,-1:mi(S,mod),-2:mi(tau,mod)}
    def ev(w):
        value=I
        for letter in w:value=mm(value,letters[letter],mod)
        return value
    for bidx,(modg,t) in enumerate(((old['S2'],1),(old['R2'],2))):
        p=[0]*(6*len(mats))
        for k,(a,w) in enumerate(old['cos']):
            j=old['ci'][mm(a,modg,2)]
            ret=gm(gm(w,(t,)),gi(old['cos'][j][1]))
            value=ev(old['words'][ret])
            for h,v in enumerate(mats):p[k*len(mats)+h]=j*len(mats)+idx[mm(v,value,mod)]+1
        offset=len(induced[bidx])+len(extra[bidx])
        extra[bidx].extend(offset+i for i in p)
full_induced=[a+b for a,b in zip(induced,extra)]
assert len(DX)==len(full_induced[0])

prefix=[]
for key,val in base['seed'].items():prefix.append(f'PBC_one_{key}:=PermList({val});;')
prefix += [f'PBC_n:={base["n"]};;',f'XX:=PermList({DX});;',f'YY:=PermList({DY});;',
           f'PBC_ind_s:=PermList({full_induced[0]});;',f'PBC_ind_r:=PermList({full_induced[1]});;']
body=base['body']
body=body.replace('return PermList(values);',f'Append(values,[Length(values)+1..{len(DX)}]);\n return PermList(values);')
body=body.replace('second_word_image_order','joint_second_word_image_order')
body=body.replace('second_modular_order','joint_second_modular_order')
(HERE/'pbc_iterated_joint.g').write_text('\n'.join(prefix)+'\n'+body)

hopf=(HERE/'pbc_hopf_iterated.g').read_text().split('LoadPackage("polycyclic");',1)[1]
hopf=hopf.replace('PBC_Tag:="iterated"','PBC_Tag:="iterated_joint"')
early=body[:body.index(' for PBC_row in PBC_survivors do')]
early += r'''
 PBC_f2:=Image(PBC_comparison,PBC_survivors[1][3]);;
else
 Error("No joint second-level commutator-word residue survives");
fi;
s:=PBC_ind_s;;r:=PBC_ind_r;;G:=PBC_second_G;;
x:=PBC_second_x;;y:=PBC_second_y;;f:=PBC_f2;;
LoadPackage("polycyclic");
'''
(HERE/'pbc_hopf_iterated_joint.g').write_text('\n'.join(prefix)+'\n'+early+hopf)
cache = r'''
PBC_CacheGens:=Igs(P);;
PBC_CacheVector:=g->ExponentsByIgs(PBC_CacheGens,g);;
PBC_CacheWord:=function(g)
 local e,i,w;
 e:=PBC_CacheVector(g);w:=[];
 for i in [1..Length(e)] do if e[i]<>0 then Append(w,[i,e[i]]);fi;od;
 return w;
end;;
PBC_CacheOrders:=List(PBC_CacheGens,RelativeOrderPcp);;
PBC_CachePowers:=List([1..Length(PBC_CacheGens)],i->PBC_CacheWord(PBC_CacheGens[i]^PBC_CacheOrders[i]));;
PBC_CacheConj:=[];;
for PBC_i in [1..Length(PBC_CacheGens)] do
 for PBC_j in [1..PBC_i-1] do
  Add(PBC_CacheConj,[PBC_i,PBC_j,PBC_CacheWord(PBC_CacheGens[PBC_i]^PBC_CacheGens[PBC_j])]);
 od;
od;
PrintTo("LM8_PUSH/code/pbc_iterated_joint_pc.json","{\n\"order\":",Size(P),",\n\"relative_orders\":",PBC_CacheOrders,",\n\"powers\":",PBC_CachePowers,",\n\"conjugates\":",PBC_CacheConj,",\n\"s\":",PBC_CacheWord(ps),",\n\"r\":",PBC_CacheWord(pr),",\n\"f\":",PBC_CacheWord(Image(iso,f)),",\n\"bs\":",PBC_CacheWord(Image(iso,bs)),",\n\"br\":",PBC_CacheWord(Image(iso,br)),"\n}\n");
Print("base_pc_presentation_saved\n");
Read("LM8_PUSH/code/pbc_sparse_schur.g");;
epi:=PBC_SparseSchur(P);;
'''
sparse=('\n'.join(prefix)+'\n'+early+hopf).replace('epi:=SchurExtensionEpimorphism(P);;',cache)
sparse=sparse.replace('PBC_Tag:="iterated_joint"','PBC_Tag:="iterated_joint_sparse"')
(HERE/'pbc_hopf_iterated_joint_sparse.g').write_text(sparse)
record={'degree':len(DX),'first_signed_detector_value':'identity',
        'second_target':'C.27 corrected frames',
        'scope':'Exact finite test; central lift needed for full existence'}
(HERE/'pbc_iterated_joint.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
