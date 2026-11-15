#!/usr/bin/env python3
"""Build the exact second descent envelope from the corrected C.27 frames.

The GAP file tests actual word membership before any lifting claim.  Its
target frame gauges range over the finite cusp and order-three ambiguity.
"""
from pathlib import Path
import json
import runpy

HERE = Path(__file__).parent
seed = json.loads((HERE / 'pbc_hopf_joint_seed.json').read_text())
n = len(seed['s'])
identity = list(range(1, n + 1))

def mul(a, b):
    return [b[i - 1] for i in a]

def inv(a):
    out = [0] * len(a)
    for i, j in enumerate(a, 1):
        out[j - 1] = i
    return out

s, r = seed['s'], seed['r']
tau = mul(s, r)
z = inv(r)
assert mul(s, mul(tau, z)) == identity
triple = (s, tau, z)
pairs = [(a, b) for a in range(3) for b in range(3) if a != b]
def blocks(seq):
    return [k * n + j for k, p in enumerate(seq) for j in p]
XX = blocks([triple[a] for a, b in pairs])
YY = blocks([triple[b] for a, b in pairs])

# The index-six induction uses the exact return words in the old marking.
d = runpy.run_path(str(HERE / 'pbc_modular_envelope.py'))
def ev(w):
    value = identity
    letters = {1: s, 2: tau, -1: inv(s), -2: inv(tau)}
    for letter in w:
        value = mul(value, letters[letter])
    return value

induced = []
for modg, t in ((d['S2'], 1), (d['R2'], 2)):
    p = [0] * (6 * n)
    for k, (a, w) in enumerate(d['cos']):
        j = d['ci'][d['mm'](a, modg, 2)]
        ret = d['gm'](d['gm'](w, (t,)), d['gi'](d['cos'][j][1]))
        value = ev(d['words'][ret])
        for h in range(n):
            p[k*n+h] = j*n + value[h]
    induced.append(p)

prefix = []
for key, val in seed.items():
    prefix.append(f'PBC_one_{key}:=PermList({val});;')
prefix += [f'PBC_n:={n};;', f'XX:=PermList({XX});;', f'YY:=PermList({YY});;',
           f'PBC_ind_s:=PermList({induced[0]});;',
           f'PBC_ind_r:=PermList({induced[1]});;']
body = r'''
PBC_one_G:=Group(PBC_one_s,PBC_one_r);;
PBC_one_D:=DerivedSubgroup(PBC_one_G);;
PBC_one_x:=(PBC_one_r*PBC_one_s)^2;;
PBC_one_y:=(PBC_one_s*PBC_one_r)^2;;
PBC_E2:=Group(XX,YY);;
Print("second_word_image_order ",Size(PBC_E2),"\n");
PBC_E2D:=DerivedSubgroup(PBC_E2);;
Print("second_derived_order ",Size(PBC_E2D),"\n");
PBC_block:=function(seq)
 local values,k,i;
 values:=[];
 for k in [1..Length(seq)] do
  for i in [1..PBC_n] do Add(values,(k-1)*PBC_n+i^seq[k]); od;
 od;
 return PermList(values);
end;;
PBC_survivors:=[];;
for PBC_a in [0..11] do
 for PBC_k in [0..2] do
  PBC_v:=PBC_one_y^PBC_a*PBC_one_beta;
  PBC_u:=PBC_one_r^PBC_k*PBC_one_A^-1*PBC_one_beta;
  if PBC_v in PBC_one_D and PBC_u in PBC_one_D then
   PBC_t:=PBC_block([PBC_v,PBC_u,PBC_v^-1,PBC_u*PBC_v^-1,PBC_u^-1,PBC_v*PBC_u^-1]);
   Print("target_gauge ",PBC_a," ",PBC_k," word_member ",PBC_t in PBC_E2," derived_member ",PBC_t in PBC_E2D,"\n");
   if PBC_t in PBC_E2D then Add(PBC_survivors,[PBC_a,PBC_k,PBC_t]); fi;
  fi;
 od;
od;
Print("surviving_gauges ",List(PBC_survivors,a->a{[1,2]}),"\n");
PBC_second_G:=Group(PBC_ind_s,PBC_ind_r);;
PBC_second_x:=(PBC_ind_r*PBC_ind_s)^2;;
PBC_second_y:=(PBC_ind_s*PBC_ind_r)^2;;
PBC_second_F:=Group(PBC_second_x,PBC_second_y);;
Print("second_modular_order ",Size(PBC_second_G)," second_pure_order ",Size(PBC_second_F),"\n");
if Length(PBC_survivors)>0 then
 PBC_comparison:=GroupHomomorphismByImages(PBC_E2,PBC_second_F,[XX,YY],[PBC_second_x,PBC_second_y]);;
 Print("comparison_isomorphism ",PBC_comparison<>fail and IsBijective(PBC_comparison),"\n");
 for PBC_row in PBC_survivors do
  PBC_f2:=Image(PBC_comparison,PBC_row[3]);;
  PBC_second_auto:=GroupHomomorphismByImages(PBC_second_G,PBC_second_G,[PBC_ind_s,PBC_ind_r],[PBC_ind_s*PBC_f2^-1,PBC_f2*PBC_ind_r]);;
  Print("candidate_automorphism ",PBC_row{[1,2]}," ",PBC_second_auto<>fail and IsBijective(PBC_second_auto),"\n");
 od;
fi;
QUIT;
'''
(HERE / 'pbc_iterated_descent.g').write_text('\n'.join(prefix) + '\n' + body)
# Reuse the audited actual-source centralization, with an abelian linear solve
# for the boundary corrections: this avoids enumerating a large multiplier.
hopf = (HERE / 'pbc_hopf_test.g').read_text().split('LoadPackage("polycyclic");', 1)[1]
hopf = hopf.replace('PBC_Tag:="mod4"', 'PBC_Tag:="iterated"')
start = hopf.index('PBC_values:=[One(PBC_Cover)]')
end = hopf.index('PBC_bs:=ebs*PBC_scor', start)
hopf = hopf[:start] + r'''
PBC_FreeChanges:=AbelianPcpGroup(Length(PBC_changes),ListWithIdenticalEntries(Length(PBC_changes),0));;
PBC_change_map:=GroupHomomorphismByImages(PBC_FreeChanges,J,GeneratorsOfGroup(PBC_FreeChanges),PBC_changes);;
PBC_pre:=PreImagesRepresentative(PBC_change_map,delta^-1);;
Assert(0,PBC_pre<>fail);
PBC_exps:=ExponentsByPcp(Pcp(PBC_FreeChanges),PBC_pre);;
PBC_word:=Filtered([1..Length(PBC_exps)],i->PBC_exps[i]<>0);;
PBC_word:=List(PBC_word,i->[i,PBC_exps[i]]);;
PBC_scor:=One(PBC_Cover);;PBC_rcor:=One(PBC_Cover);;
for PBC_j in [1..Length(PBC_exps)] do
 if PBC_j<=Length(PBC_cs) then
  PBC_scor:=PBC_scor*PBC_lifts[PBC_j]^PBC_exps[PBC_j];
 else
  PBC_rcor:=PBC_rcor*PBC_lifts[PBC_j]^PBC_exps[PBC_j];
 fi;
od;
''' + hopf[end:]
early = body[:body.index(' for PBC_row in PBC_survivors do')]
early += r'''
 PBC_f2:=Image(PBC_comparison,PBC_survivors[1][3]);;
else
 Error("No second-level commutator-word residue survives");
fi;
s:=PBC_ind_s;;r:=PBC_ind_r;;G:=PBC_second_G;;
x:=PBC_second_x;;y:=PBC_second_y;;f:=PBC_f2;;
LoadPackage("polycyclic");
'''
(HERE / 'pbc_hopf_iterated.g').write_text('\n'.join(prefix)+'\n'+early+hopf)
record = {'degree': 6*n, 'source': 'corrected C.27 source frames',
          'scope': 'Exact finite word-membership and automorphism test only; no full lift asserted'}
(HERE / 'pbc_iterated_descent.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
