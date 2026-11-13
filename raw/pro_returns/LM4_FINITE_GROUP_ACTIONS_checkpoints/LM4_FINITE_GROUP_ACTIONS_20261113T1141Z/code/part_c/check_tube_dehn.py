"""Additional exact surface-group checks for the tube word formulas."""
from verify_tube_action import *
from itertools import product

def reducer(R):
    cyclics=[]
    for rr in (R,inv(R)):
        for i in range(len(R)):
            cyclics.append(rr[i:]+rr[:i])
    # symmetrized relators have no common initial segment of length 2.
    assert len({w[:2] for w in cyclics})==len(cyclics)
    rules={w[:n]:inv(w[n:]) for w in cyclics for n in range(len(R)//2+1,len(R)+1)}
    def reduce(w):
        w=red(w)
        while True:
            changed=False
            for n in range(len(R),len(R)//2,-1):
                for i in range(len(w)-n+1):
                    key=w[i:i+n]
                    if key in rules:
                        w=red(w[:i]+rules[key]+w[i+n:])
                        changed=True
                        break
                if changed:
                    break
            if not changed:
                return w
    return reduce

def comp(f,h):
    return tuple(subst(w,f) for w in h)

def inn(c,n):
    return tuple(mul(c,(j+1,),inv(c)) for j in range(n))

out=[]
for g in range(2,9):
    a=model(g); d=reducer(a['R']); n=2*g
    identity=tuple((j+1,) for j in range(n))
    def eq(f,h):
        return all(not d(mul(w,inv(v))) for w,v in zip(f,h))
    r,s,t=(a[k] for k in ('r','s','t'))
    rr=identity
    for j in range(2*g):
        rr=comp(r,rr)
    assert eq(rr,identity)
    assert eq(comp(s,s),inn(a['x'][0],n))
    assert eq(comp(t,t),inn(mul(*a['x'][:g]),n))
    rinv=identity
    for j in range(2*g-1):
        rinv=comp(r,rinv)
    assert eq(comp(s,comp(r,comp(s,r))),identity)
    assert eq(comp(t,comp(r,comp(t,rinv))),inn(mul(*a['x'][:g+1]),n))
    cts=mul(inv(a['u'][g-1]),a['u'][g],inv(a['u'][0]))
    assert eq(comp(t,comp(s,comp(t,s))),inn(cts,n))
    for j,tw in enumerate(a['twists']):
        assert eq(comp(r,comp(tw,rinv)),a['twists'][(j+1)%g])
        assert eq(comp(s,comp(tw,s)),comp(inn(a['x'][0],n),a['twists'][(-j)%g]))
        twinv=tuple(a['x'][:g])+tuple(mul(inv(a['x'][l]),a['p'][l]) if l==j else a['p'][l] for l in range(g))
        assert eq(comp(t,comp(tw,t)),comp(inn(mul(*a['x'][:g]),n),twinv))
    # The conjugating paths below come directly from a=N->S in the two-vertex cell model.
    checks={'r_order_2g':True,'s_squared_inner_x0':True,'tau_squared_inner_x0_to_xgminus1':True,'srsr_exact_identity':True,'tau_r_commutation_outer_with_explicit_inner_word':True,'tau_s_commutation_outer_with_explicit_inner_word':True,'all_three_generator_actions_on_every_tube_twist_exact_mod_explicit_inners':True}
    out.append({'g':g,'symmetrized_relator_max_piece':1,'checks':checks})
Path(__file__).with_name('check_tube_dehn_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
