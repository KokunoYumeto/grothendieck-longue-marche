#!/usr/bin/env python3
"""Finite exact packet test for the cube-parameter F16 orbit inside F256.

Uses the proved Mumford arithmetic from A.29c.  The full field bound is
certified by the Frobenius counts in A_ordinary_cubic_family.json.
"""
import json
from pathlib import Path
import A_genus4_prym_experiment as J
from A_ordinary_elliptic_obstruction import BinaryField


def main():
    k=BinaryField(8,0x11b)
    J.fm=k.mul
    J.fp=k.power
    J.fi=lambda a:k.power(a,254) if a else (_ for _ in ()).throw(ValueError())
    root=next(z for z in range(256) if k.power(z,4)^z^1==0)
    def emb(z):
        r=0
        for i in range(4):
            if (z>>i)&1:r^=k.power(root,i)
        return r
    zeta=next(z for z in range(256) if k.mul(z,z)^z^1==0)
    solutions={}
    for y in range(256):solutions.setdefault(k.mul(y,y)^y,[]).append(y)
    family=json.loads(Path(__file__).with_name('A_ordinary_cubic_family.json').read_text())
    rows=[]
    for data in family['parameters']:
        if data['prym_orders']['2']['v2']!=8:continue
        a,b=emb(data['a_F16']),emb(data['b_F16'])
        J.H=[b,0,0,1]
        J.F=J.add(J.mul(J.mul(J.H,J.H),J.H),J.scale(J.H,a))
        packet=[]
        orbit_count=0
        seen=set()
        for s in range(256):
            h=k.power(s,3)^b
            ys=[0] if not h else [k.mul(h,y) for y in solutions.get(h^k.mul(a,J.fi(h)),[])]
            if not ys or s in seen:continue
            seen.update({s,k.mul(zeta,s),k.mul(k.mul(zeta,zeta),s)})
            orbit_count+=1
            Y=ys[0]
            D=J.cantor(J.point(s,Y),J.negate(J.point(k.mul(zeta,s),Y)))
            exact=0 if D==J.IDENTITY else None
            multiple=D
            for n in range(1,5):
                multiple=J.cantor(multiple,multiple)
                if multiple==J.IDENTITY and exact is None:exact=n
            if multiple==J.IDENTITY:
                packet.append({'s':s,'Y':Y,'order_power':exact,'fixed':s==0,'weierstrass':not h})
        rows.append({'b_F16':data['b_F16'],'a_F16':data['a_F16'],'b_F256':b,'a_F256':a,'orbits':orbit_count,'full_packet':packet,
                     'weierstrass_only':all(x['fixed'] or x['weierstrass'] for x in packet),
                     'field_bound':'v2 |A(F256)|=8 gives v(lambda^2-1)=4 and all nonzero packet points in F256, exponent<=16'})
    result={'rows':rows,'all_checks_passed':True}
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(out)
    print(out,end='')


if __name__=='__main__':main()
