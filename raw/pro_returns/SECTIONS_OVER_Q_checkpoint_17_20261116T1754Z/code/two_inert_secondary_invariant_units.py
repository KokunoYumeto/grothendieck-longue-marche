#!/usr/bin/env python3
"""Complete finite necessary unit space for the A208 Hilbert--90 correction.

The coordinates are the actual A199 27-unit basis, recovered through its
27 fixed cubic-residue detectors.  This computes a necessary subspace;
it does not replace the actual unit-norm or descent conditions by that
subspace.
"""
from pathlib import Path
import runpy, json
import sympy as S
B=Path(__file__).resolve().parent
C=runpy.run_path(str(B/'two_inert_ninth_root_unit_norm_maps.py'))
values=C['values']; fixed=C['fixed']; columns=C['columns']; rank=C['rank']
solve=C['solve_injective']; matmul=C['matmul']
R=[[row[j-1] for j in columns] for row in C['R']]
n=27
I=[[int(i==j) for j in range(n)] for i in range(n)]

def difference(A,B):
    return [[(x-y)%3 for x,y in zip(a,b)] for a,b in zip(A,B)]

def kernel(A):
    a=[[x%3 for x in row] for row in A]
    piv=[]; k=0
    for j in range(n):
        z=next((i for i in range(k,len(a)) if a[i][j]),None)
        if z is None: continue
        a[k],a[z]=a[z],a[k]
        iv=pow(a[k][j],-1,3);a[k]=[iv*x%3 for x in a[k]]
        for i in range(len(a)):
            if i==k: continue
            v=a[i][j];a[i]=[(x-v*y)%3 for x,y in zip(a[i],a[k])]
        piv.append(j);k+=1
    free=[j for j in range(n) if j not in piv]
    basis=[]
    for j in free:
        v=[0]*n;v[j]=1
        for i,p in enumerate(piv):v[p]=-a[i][j]%3
        basis.append(v)
    assert all(not any(sum(x*y for x,y in zip(row,v))%3 for row in A) for v in basis)
    return basis

def action(t_exp,z_exp):
    rows=[]
    for p,t,z in fixed:
        vals=values(p,t*pow(z,t_exp,p)%p,pow(z,z_exp,p))
        logs={1:0,pow(z,3,p):1,pow(z,6,p):2}
        rows.append([logs[pow(vals[j-1],(p-1)//3,p)] for j in columns])
    return solve(R,rows)

g=action(1,1); sig=action(3,1); h=action(0,4); tau=action(0,8)
assert matmul(matmul(sig,sig),sig)==I
assert matmul(matmul(h,h),h)==I
assert matmul(tau,tau)==I
assert matmul(sig,h)==matmul(h,sig)
assert matmul(tau,h)==matmul(h,tau)
assert matmul(matmul(tau,sig),tau)==matmul(sig,sig)
assert matmul(matmul(g,g),g)==sig
assert matmul(matmul(h,g),matmul(h,h))==matmul(matmul(g,g),matmul(g,g))

norm_data=json.loads((B/'two_inert_ninth_root_next_norm_characters_data.json').read_text())
Lambda=[[row['row'][j-1] for j in columns] for row in norm_data['rows']]
constraints=difference(sig,I)+difference(h,I)+difference(tau,[[-x%3 for x in row] for row in I])
invariants=kernel(constraints)
necessary=kernel(constraints+Lambda)
lambda_on_invariants=matmul(Lambda,list(map(list,zip(*invariants))))
assert len(invariants)-rank(lambda_on_invariants)==len(necessary)

# The lower-field anti radicals have actual unit representatives in M:
# div_M(u_q)=3*j(Delta_q), and these order-three ideal classes
# capitulate by A206.  The finite detector therefore gives their actual
# unit cube-class coordinates, independent of a chosen principalizer.
lower_rows=[]
for p,t,z in fixed:
    alpha=pow(t,3,p)*pow(C['d']**2,-1,p)%p
    om=pow(z,3,p)
    aq=alpha*om%p; aqq=alpha*om*om%p
    u11=(2+aq)*pow(2+aqq,-1,p)%p
    u59=(2+2*aq-aq*aq)*pow(2+2*aqq-aqq*aqq,-1,p)%p
    eps=values(p,t,z)[13]
    logs={1:0,om:1,om*om%p:2}
    lower_rows.append([logs[pow(x,(p-1)//3,p)] for x in (eps,u11,u59)])
lower_coordinates=solve(R,lower_rows)
lower_basis=list(map(list,zip(*lower_coordinates)))
assert rank(lower_basis)==3
assert all(not any(sum(x*y for x,y in zip(row,v))%3 for row in constraints+Lambda) for v in lower_basis)
assert len(necessary)==3
lower_expressions=solve(list(map(list,zip(*lower_basis))),list(map(list,zip(*necessary))))
assert matmul(list(map(list,zip(*lower_basis))),lower_expressions)==list(map(list,zip(*necessary)))

def rank_witness(A):
    a=[[x%3 for x in row] for row in A];ids=list(range(len(a)))
    cols=[];k=0
    for j in range(len(a[0])):
        r=next((i for i in range(k,len(a)) if a[i][j]),None)
        if r is None:continue
        a[k],a[r]=a[r],a[k];ids[k],ids[r]=ids[r],ids[k]
        iv=pow(a[k][j],-1,3);a[k]=[iv*x%3 for x in a[k]]
        for i in range(k+1,len(a)):
            v=a[i][j];a[i]=[(x-v*y)%3 for x,y in zip(a[i],a[k])]
        cols.append(j);k+=1
    rows=ids[:k]
    minor=[[A[i][j]%3 for j in cols] for i in rows]
    det=int(S.Matrix(minor).det())
    assert det%3
    return {'rank':k,'rows_1based':[i+1 for i in rows],
            'columns_1based':[j+1 for j in cols],
            'minor':minor,'determinant':det,'det_mod3':det%3}
rank_witnesses={'invariant_constraints':rank_witness(constraints),
                'constraints_plus_tame':rank_witness(constraints+Lambda),
                'lower_basis':rank_witness(lower_coordinates)}
assert [rank_witnesses[x]['rank'] for x in rank_witnesses]==[23,24,3]

# Exact cyclic-nine group-ring identity for the additional h alignment.
def pmul(a,b):
    out=[0]*9
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[(i+j)%9]+=x*y
    return out
Ns=[int(j in (0,3,6)) for j in range(9)]
Rj=[[0,0,0,0,0,-1,0,-1,-1],
    [0,-1,-1,0,0,-1,0,0,0],
    [0,0,-1,0,-1,0,0,0,-1]]
for j in range(3):
    old=pow(4,(j-1)%3,9);new=pow(4,j,9)
    Lj=[-Ns[i]-int(i==0) for i in range(9)]
    for k in range(4):Lj[k*old%9]+=1
    factor=[-int(i==0)+int(i==new) for i in range(9)]
    assert pmul(factor,Rj[j])==Lj
rsum=[sum(row[i] for row in Rj) for i in range(9)]
assert rsum==pmul([0,-1,-2,0,0,0,0,0,0],Ns)

def expanded(v):
    out=[0]*51
    for j,a in zip(columns,v):out[j-1]=a
    return out

# The full old source and the two added root triples are retained literally.
labels=['e'+str(i) for i in range(1,10)]
for j in range(3):
    labels += [f'g^{j}(u{i})' for i in range(1,5)]
    labels += [f'g^{j}(epsilon)']
    labels += [f'g^{j}(r{i})' for i in range(2,5)]
labels += [f'g^{j}(r)' for j in range(9)]
labels += [f'g^{j}(s)' for j in range(9)]
assert len(labels)==51
def expression(v):return '*'.join(labels[j]+('^2' if x==2 else '') for j,x in enumerate(expanded(v)) if x) or '1'

print('Complete A199 action matrices: PASS')
print('sigma,h fixed and tau anti dimension:',len(invariants))
print('Next tame matrix rank on that space:',rank(lambda_on_invariants))
print('Necessary invariant norm-kernel dimension:',len(necessary))
for v in necessary:print('BASIS',expression(v))
print('Exact lower-radical basis: epsilon, u11, u59')
print('The three displayed kernel vectors in that basis:',list(map(list,zip(*lower_expressions))))
print('All three integral group-ring h-alignment identities: PASS')
for name,record in rank_witnesses.items():print('MINOR',name,record['rows_1based'],record['columns_1based'],record['determinant'])
data={'basis_columns_1based':columns,'sigma':sig,'h':h,'tau':tau,'g':g,
      'invariant_dimension':len(invariants),'invariant_basis':invariants,
      'lambda_on_invariants':lambda_on_invariants,
      'necessary_dimension':len(necessary),'necessary_basis':necessary,
      'necessary_expressions':[expression(v) for v in necessary],
      'lower_radical_basis':['epsilon','u11','u59'],
      'lower_radical_coordinates':lower_coordinates,
      'kernel_vectors_in_lower_radical_basis':list(map(list,zip(*lower_expressions))),
      'h_alignment_group_ring_vectors':Rj,
      'rank_witnesses':rank_witnesses,
      'scope':'Necessary unit cube-class subspace for c=x^3/f in A208. No converse descent, actual unit norm, eta=psi, or value of psi2 is inferred.'}
stem=Path(__file__).with_suffix('')
stem.with_name(stem.name+'_data.json').write_text(json.dumps(data,indent=2)+'\n')
stem.with_name(stem.name+'_output.txt').write_text('\n'.join([
    'Complete unit action/necessary subspace: PASS',
    f'Invariant dimension {len(invariants)}',
    f'Next tame rank {rank(lambda_on_invariants)}',
    f'Necessary dimension {len(necessary)}',
    *data['necessary_expressions'],
    'Exact lower-radical basis: epsilon,u11,u59',
    'Three integral group-ring h-alignment identities: PASS',data['scope']])+'\n')
