#!/usr/bin/env python3
"""Exact finite-field enumeration for the rank-one chain recorded on scans 059,080–081.

No images or transcription files are read or changed. Standard Python only.
Vector coordinates are (a_-1,a_0,...,a_n); matrices act on column vectors.
"""
from __future__ import annotations
import argparse,csv,json,itertools
from collections import Counter
from pathlib import Path


def rref(rows,p,d):
    a=[[x%p for x in row] for row in rows if any(x%p for x in row)]
    k=0
    for col in range(d):
        found=next((j for j in range(k,len(a)) if a[j][col]),None)
        if found is None: continue
        a[k],a[found]=a[found],a[k]
        inv=pow(a[k][col],-1,p);a[k]=[(x*inv)%p for x in a[k]]
        for j in range(len(a)):
            if j!=k and a[j][col]:
                factor=a[j][col];a[j]=[(x-factor*y)%p for x,y in zip(a[j],a[k])]
        k+=1
        if k==len(a):break
    return tuple(tuple(row) for row in a[:k])


def nullspace(rows,p,d):
    a=rref(rows,p,d);piv=[next(j for j,x in enumerate(row) if x) for row in a]
    free=[j for j in range(d) if j not in piv];basis=[]
    for col in free:
        v=[0]*d;v[col]=1
        for row,j in zip(a,piv):v[j]=-row[col]%p
        basis.append(v)
    return rref(basis,p,d)


def all_subspaces(p,d):
    """One canonical RREF basis per subspace, with no rank tests or repetitions."""
    for rank in range(d+1):
        for piv in itertools.combinations(range(d),rank):
            positions=[(i,c) for i,pivot in enumerate(piv) for c in range(pivot+1,d) if c not in piv]
            for coeff in itertools.product(range(p),repeat=len(positions)):
                rows=[[int(c==pivot) for c in range(d)] for pivot in piv]
                for (i,c),value in zip(positions,coeff):rows[i][c]=value
                yield tuple(tuple(row) for row in rows)


def contains(basis,v,p):
    w=list(v)
    for row in basis:
        pivot=next(j for j,x in enumerate(row) if x)
        t=w[pivot]%p
        if t:w=[(x-t*y)%p for x,y in zip(w,row)]
    return not any(x%p for x in w)


def matvec(matrix,v,p):
    return tuple(sum(x*y for x,y in zip(row,v))%p for row in matrix)


def matrix_model(p,n,mu,beta):
    d=n+2;basis=tuple(tuple(int(i==j) for j in range(d)) for i in range(d))
    phi=[];tau=[]
    for i in range(n+1):
        f=[0]*d;f[i]=1;f[i+1]=mu[i]
        if i<n:f[i+2]=beta[i]
        phi.append(tuple(f))
        t=[list(row) for row in basis]
        t[i+1]=[(x+y)%p for x,y in zip(t[i+1],f)]
        tau.append(tuple(tuple(row) for row in t))
    return basis,tuple(phi),tuple(tau)


def determinant_pairing(p,mu,beta):
    prevprev,prev=1,mu[0]%p
    for i in range(1,len(mu)):
        prevprev,prev=prev,(mu[i]*prev-beta[i-1]*prevprev)%p
    return prev


def stable(basis,tau,p):
    return all(contains(basis,matvec(t,v,p),p) for t in tau for v in basis)


def predicted(p,n,mu,beta):
    basis,phi,tau=matrix_model(p,n,mu,beta);d=n+2
    A={i:tuple(basis[i+1:]) for i in range(n+2)}
    K={-1:basis}
    K.update({i:nullspace(phi[:i+1],p,d) for i in range(n+1)})
    labels={'empty':(), 'X':basis,'c':K[n],'C':A[0]}
    for i,b in enumerate(beta):
        if b==0:labels[f'A_{i+1}']=A[i+1];labels[f'K_{i}']=K[i]
    delta=[i for i in range(n+1) if mu[i]==0 and (i==0 or beta[i-1]==0) and (i==n or beta[i]==0)]
    count=4+2*sum(b==0 for b in beta)-len(delta)
    return labels,A,K,delta,count,tau,phi


def gaussian_binomial(p,d,r):
    top=bottom=1
    for i in range(r):top*=p**(d-i)-1;bottom*=p**(r-i)-1
    return top//bottom


def case(p,n,mu,beta,universe,detail=False):
    labels,A,K,delta,count,tau,phi=predicted(p,n,mu,beta)
    actual={w for w in universe if stable(w,tau,p)}
    candidate=set(labels.values())
    assert actual==candidate,(p,n,mu,beta,'candidate mismatch',actual-candidate,candidate-actual)
    assert len(actual)==count,(p,n,mu,beta,'count mismatch')
    det=determinant_pairing(p,mu,beta)
    c=K[n][0]
    assert (c[0]!=0)==(det!=0)
    allflags=set(A.values())|set(K.values())
    assert len(allflags)==2*(n+2)-len(delta)
    assert (len(actual)==2*(n+2))==(all(b==0 for b in beta) and all(m!=0 for m in mu))
    for i in range(n):assert all(contains(K[i],v,p) for v in A[i+1])==(beta[i]==0)
    if det:
        assert all(not all(contains(A[j],v,p) for v in K[i]) for i in range(-1,n+1) for j in range(n+2))
        proper_C={w for w in actual if w and w!=A[0] and all(contains(A[0],v,p) for v in w)}
        assert proper_C=={A[i+1] for i,b in enumerate(beta) if b==0}
    # The strict-interior interpretation is the first reading on scan 081.
    literal_min=(all(beta[i]!=0 for i in range(1,n-1)) and (beta[0]!=0 or mu[0]==0) and (beta[-1]!=0 or mu[-1]==0))
    reflection=all(m==(-2)%p for m in mu)
    row={'p':p,'n':n,'mu':','.join(map(str,mu)),'beta':','.join(map(str,beta)),
         'all_subspaces':len(universe),'invariant_subspaces':len(actual),'zero_beta_count':sum(b==0 for b in beta),
         'coincidences':','.join(map(str,delta)),'coincidence_count':len(delta),'formula_count':count,
         'det_pairing_mod_p':det,'all_flag_subspaces':len(allflags),'reflection':reflection,
         'literal_081_four_space_criterion':literal_min,'actual_exactly_four':len(actual)==4,
         'literal_criterion_agrees':literal_min==(len(actual)==4)}
    if detail:
        byspace=[]
        for w in sorted(actual,key=lambda x:(len(x),x)):
            byspace.append({'vector_dimension':len(w),'projective_dimension':len(w)-1,'rref_basis':[list(v) for v in w],
                            'labels':[name for name,v in labels.items() if v==w]})
        return {'parameters':row,'coordinates':['a_-1']+[f'a_{i}' for i in range(n+1)],
                'functionals':[list(v) for v in phi], 'generator_matrices':[[list(v) for v in t] for t in tau],
                'invariant_subspaces':byspace,'all_A':{str(i):[list(v) for v in w] for i,w in A.items()},
                'all_K':{str(i):[list(v) for v in w] for i,w in K.items()}}
    return row


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--outdir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();args.outdir.mkdir(parents=True,exist_ok=True)
    grids=[(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]
    rows=[];summary=[];universes={}
    for p,n in grids:
        d=n+2;universe=tuple(all_subspaces(p,d));universes[p,n]=universe
        expected=sum(gaussian_binomial(p,d,r) for r in range(d+1))
        assert len(universe)==expected and len(set(universe))==expected
        start=len(rows)
        for mu in itertools.product(range(p-1),repeat=n+1):
            for beta in itertools.product(range(p),repeat=n):rows.append(case(p,n,mu,beta,universe))
        part=rows[start:];counts=Counter(r['invariant_subspaces'] for r in part)
        summary.append({'p':p,'n':n,'parameter_cases':len(part),'subspaces_per_case':len(universe),
                        'subspace_tests':len(part)*len(universe),'invariant_count_distribution':dict(sorted(counts.items())),
                        'candidate_or_count_failures':0,'literal_081_criterion_failures':sum(not r['literal_criterion_agrees'] for r in part),
                        'reflection_cases':sum(r['reflection'] for r in part),
                        'reflection_literal_criterion_failures':sum(r['reflection'] and not r['literal_criterion_agrees'] for r in part)})
    target=args.outdir/'invariant_subspaces_cases.csv'
    with target.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    details={
      'scan081_characteristic_two_counterexample':case(2,2,(0,0,0),(0,0),universes[2,2],True),
      'scan080_vertical_inclusion_counterexample':case(3,1,(1,1),(2,),universes[3,1],True),
      'maximum_eight_subspaces':case(3,2,(1,1,1),(0,0),universes[3,2],True),
      'single_endpoint_zero':case(2,2,(0,0,0),(0,1),universes[2,2],True),
    }
    full={'model':'E=(a_-1,a_0,...,a_n), tau_i=I+a_i tensor phi_i; phi_i=(1,mu_i,beta_i) at consecutive positions',
          'scope':'Complete subspace enumeration for all admissible parameters in the six explicitly listed prime-field grids; these finite checks complement the written algebraic proof.',
          'grids':summary,'totals':{'parameter_cases':len(rows),'subspace_tests':sum(x['subspace_tests'] for x in summary),
                                   'candidate_or_count_failures':0,'literal_081_criterion_failures':sum(x['literal_081_criterion_failures'] for x in summary)},
          'examples':details}
    (args.outdir/'invariant_subspaces_results.json').write_text(json.dumps(full,indent=2)+'\n')
    print(json.dumps({'grids':summary,'totals':full['totals'],'files':[str(target),str(args.outdir/'invariant_subspaces_results.json')]},indent=2))

if __name__=='__main__':main()
