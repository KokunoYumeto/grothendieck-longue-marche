#!/usr/bin/env python3
"""Bounded positive theta search on the twelve p-rank-one F4 moduli classes.

This is exploratory until its fixed positive witnesses are independently
verified and the geometric interpretation is reviewed.  It does not alter
the complete ordinary-class certificate.
"""
from pathlib import Path
from math import gcd
import json,time,random
import sympy as sp
from A_rank_one_arithmetic import Field,Div,lib,eta,times,add,ZERO,HASH
from A_F4_large_theta_canonical import IndependentField
from A_theta_F4_remaining_Jacobian import Jacobian

ROOT=Path(__file__).parent
MODS={2:7,4:19,6:67,8:283,10:1033,12:4179,16:65581,18:262273}

def coefficients(F,a,b):
    vals=[0,1,F.alpha,F.mul(F.alpha,F.alpha)]
    return vals[a],vals[b]

def configure(F,a,b):
    A,B=coefficients(F,a,b)
    assert lib.a_set_rank_one(A,B)==0
    return A,B

def count(F):
    return 2+sum(2 for x in range(1,F.q) if F.point(x)[0]==1)

def polynomial_counts():
    counts={}
    for e in (2,4):
        F=Field(e,MODS[e])
        for a in (1,2,3):
            for b in range(4):
                configure(F,a,b);counts.setdefault((a,b),[]).append(count(F))
    out={}
    for (a,b),(n1,n2) in counts.items():
        s1=5-n1;s2=17-n2;c1=-s1;c2=(s1*s1-s2)//2
        out[(a,b)]={'F4_coefficients':[a,b],'counts':[n1,n2],
                    'P4_ascending':[16,4*c1,c2,c1,1]}
    return out

def orders(record,r):
    P=record['P4_ascending'];c1=P[3];c2=P[2]
    s=[4,-c1,c1*c1-2*c2]
    s.append(-c1*s[2]-c2*s[1]-3*4*c1)
    s.append(-c1*s[3]-c2*s[2]-4*c1*s[1]-4*16)
    while len(s)<=2*r:
        k=len(s);s.append(-c1*s[k-1]-c2*s[k-2]-4*c1*s[k-3]-16*s[k-4])
    q=4**r;N=q*q+1-(q+1)*s[r]+(s[r]*s[r]-s[2*r])//2
    return N,q+1-s[r]

def unit_info(n):
    phi=int(sp.totient(n));o=phi
    for p in sp.factorint(phi):
        while o%p==0 and pow(2,o//p,n)==1:o//=p
    minus=(o%2==0 and pow(2,o//2,n)==n-1)
    index=phi//(o*(1 if minus else 2))
    return {'phi':phi,'doubling_period':o,'sign_in_doubling_group':minus,
            'index_of_doubling_and_sign':index}

def canonical_crosscheck():
    rng=random.Random(14925);tests=0
    for e in (4,6):
        F=Field(e,MODS[e]);K=IndependentField(e,MODS[e],F.generator)
        for a,b in [(1,2),(2,0),(2,1),(2,2)]:
            A,B=configure(F,a,b);J=Jacobian(K,[1,1,1]);J.h=[0,1];J.f=[0,1,0,B,0,A];J.T=(J.h,[])
            points=[]
            for x in range(1,F.q):
                ok,y=F.point(x)
                if ok!=1:continue
                d=eta(x,y);Y=K.mul(x,y)
                c=J.add(J.check(([x,1],[Y] if Y else [])),J.T)
                assert d.lists()==c;points.append((d,c));tests+=1
            for _ in range(30):
                d,c=rng.choice(points);e0,c0=rng.choice(points);n=rng.randrange(10000)
                assert add(d,e0).lists()==J.add(c,c0);tests+=1
                assert times(d,n).lists()==J.times(c,n);tests+=1
    return tests

def main():
    start=time.time();tests=canonical_crosscheck();records=polynomial_counts()
    for key,rec in records.items():
        a,b=key
        if b==({1:1,2:3,3:2}[a]):rec['already_proved']='A.C2.3'
        if key==(1,0):rec['already_proved']='A.C2.4'
    targets=[(1,2),(2,0),(2,1),(2,2)]
    print('COUNTS',json.dumps(list(records.values())),flush=True)
    for e,mod in MODS.items():
        if all('witness' in records[k] for k in targets):break
        F=Field(e,mod)
        for key in targets:
            rec=records[key]
            if 'witness' in rec:continue
            A,B=configure(F,*key);N,Nc=orders(rec,e//2);nodd=N
            while nodd%2==0:nodd//=2
            factors={int(p):int(a) for p,a in sp.factorint(nodd).items()}
            count_actual=2;tested=0;seen_orders={}
            for x in range(1,F.q):
                ok,y=F.point(x)
                if ok!=1:continue
                count_actual+=2;d=eta(x,y)
                assert times(d,N).key()==ZERO.key()
                if times(d,nodd).key()!=ZERO.key():continue
                n=nodd
                for p in factors:
                    while n%p==0 and times(d,n//p).key()==ZERO.key():n//=p
                assert n>1
                info=unit_info(n);seen_orders[n]=info;tested+=1
                if info['index_of_doubling_and_sign']!=1:continue
                rec['witness']={'field_degree_over_F2':e,'field_modulus':mod,
                    'field_generator':F.generator,'alpha':F.alpha,
                    'A':A,'B':B,'point':[x,y],'mumford_theta':d.lists(),
                    'exact_order':n,'order_factorization':{int(p):int(a) for p,a in sp.factorint(n).items()},
                    'Jacobian_order':N,'curve_count_expected':Nc,**info}
                print('POSITIVE',key,rec['witness'],flush=True);break
            if 'witness' not in rec:assert count_actual==Nc
            rec.setdefault('searches',[]).append({'field_degree':e,'Jacobian_order':N,
                'odd_part':nodd,'odd_theta_points_tested_up_to_sign':tested,
                'orders_seen':seen_orders,'found':'witness' in rec})
            print('FIELD',e,'curve',key,'orders',seen_orders,flush=True)
            out={'status':'EXPLORATORY bounded positive search','C_source_sha256':HASH,
                 'canonical_crosschecks':tests,'curves':list(records.values()),
                 'targets':targets,'runtime_seconds':time.time()-start}
            Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE', {str(k):records[k].get('witness',{}).get('exact_order') for k in targets},flush=True)

if __name__=='__main__':main()
