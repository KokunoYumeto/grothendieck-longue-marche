"""Intermediate actual quotients between the 5- and 11-dimensional modules."""
import check_universal_relation_module as b
import numpy as np
import math,json

def quotient(rows,n):
    rr,piv=b.rref(rows,2);free=[j for j in range(n) if j not in piv]
    q=np.eye(n,dtype=np.int64)
    for row,j in zip(rr,piv):q=(q-q[:,j,None]*row[None,:])%2
    return q[:,free]
def group_order(perm):
    seen=set();ans=1
    for i in range(len(perm)):
        if i in seen:continue
        j=i;n=0
        while j not in seen:seen.add(j);n+=1;j=perm[j]-1
        ans=math.lcm(ans,n)
    return ans
def group_quot(key):
    return quotient(np.concatenate([b.matrices[k-1]-np.eye(25,dtype=np.int64)
                                   for k in b.data[key+'_indices']],axis=0)%2,25)
q0=group_quot('O3');q2=group_quot('T2')
assert q0.shape==(25,9) and q2.shape==(25,2)
def section(q):
    _,rows=b.rref(q.T,2);rr,piv=b.rref(np.concatenate((q[rows,:],np.eye(len(rows),dtype=np.int64)),axis=1),2)
    out=np.zeros((q.shape[1],q.shape[0]),dtype=np.int64);out[:,rows]=rr[:,len(rows):]
    assert np.array_equal(out@q%2,np.eye(q.shape[1],dtype=np.int64))
    return out
c=next(k for k in b.data['T3_indices'] if group_order(b.data['left_inverse_actions'][k-1])==4)
op=(section(q0)@b.matrices[c-1]@q0-np.eye(9,dtype=np.int64))%2
for power in (2,3):
    qq=quotient(np.linalg.matrix_power(op,power)%2,9)
    q=np.concatenate((q0@qq%2,q2),axis=1)%2;s=section(q)
    small=[s@m@q%2 for m in b.matrices]
    for m,sm in zip(b.matrices,small):assert not np.any((m@q-q@sm)%2)
    full_dual=[b.matrices[i-1].T%2 for i in b.data['inverse_indices']]
    small_dual=[small[i-1].T%2 for i in b.data['inverse_indices']]
    embed=q.T%2
    for fm,sm in zip(full_dual,small_dual):assert not np.any((sm@embed-embed@fm)%2)
    text=('RelationFullMats:='+json.dumps([a.tolist() for a in full_dual])+';;\n'
          +'RelationSmallMats:='+json.dumps([a.tolist() for a in small_dual])+';;\n'
          +'RelationEmbed:='+json.dumps(embed.tolist())+';;\n')
    (b.ROOT/f'relation_cohomology_modules_2_power{power}.g').write_text(text)
    print(f'Intermediate central operator power{power}, module dimension={q.shape[1]}, exact dual inclusion verified.',flush=True)
