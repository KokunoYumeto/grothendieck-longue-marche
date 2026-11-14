#!/usr/bin/env python3
"""Exact geometric source/relative-track certificate for the F19 probe.

All geometry is over Q(theta), theta^4-5 theta^2+5=0, 19/10<theta<2.
Projected roots are counted by Bernstein/Descartes subdivision using exact
number-field signs.  No floating-point discovery output is read.
The original source labels and all based transport paths are retained in F.20.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from functools import cmp_to_key
import sys,json

sys.path.insert(0,str(Path(__file__).parent))
import c5_seven_kernel_exact as nf
R,C=nf.R,nf.C
ZERO=R(0);CZERO=C(0)
BASE=C(2,2);REFERENCE=C(8,3);RADIUS=Q(31,1000)
PROJECTION=C(1,Q(371,1000));ZETA=nf.ZETA;ROOTS=nf.ROOTS
CENTERS=[C(0)]+[sign*z for sign in (1,-1) for z in ROOTS]


def cinv(z):
    d=z.re*z.re+z.im*z.im
    assert d.sign()>0
    return C(z.re/d,-z.im/d)


def trim(p):
    while len(p)>1 and p[-1]==p[-1]*0:p.pop()
    return p


def padd(p,q):
    z=p[0]*0;out=[z for _ in range(max(len(p),len(q)))]
    for i,x in enumerate(p):out[i]=out[i]+x
    for i,x in enumerate(q):out[i]=out[i]+x
    return trim(out)


def pscale(p,c):return trim([x*c for x in p])
def psub(p,q):return padd(p,pscale(q,-1))


def pmul(p,q):
    out=[p[0]*0 for _ in range(len(p)+len(q)-1)]
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]=out[i+j]+x*y
    return trim(out)


def peval(p,t):
    v=p[-1]
    for x in p[-2::-1]:v=v*t+x
    return v


def bernstein(p,a=Q(0),b=Q(1)):
    n=len(p)-1;power=[]
    for j in range(n+1):
        v=R(0)
        for i in range(j,n+1):v=v+p[i]*(comb(i,j)*a**(i-j))
        power.append(v*(b-a)**j)
    return [sum((power[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),R(0)) for k in range(n+1)]


def signs(b):return [x.sign() for x in b]


def variation(b):
    ss=[s for s in signs(b) if s]
    return sum(a!=c for a,c in zip(ss,ss[1:]))


def split(b,r=Q(1,2)):
    left=[b[0]];right=[b[-1]];row=b[:]
    while len(row)>1:
        row=[(1-r)*x+r*y for x,y in zip(row,row[1:])]
        left.append(row[0]);right.append(row[-1])
    return left,right[::-1]


def split_nonroot(b,a,z):
    # At most degree-many distinct interior choices can be polynomial roots.
    for denominator in range(2,len(b)+3):
        r=Q(1,denominator);l,h=split(b,r)
        if l[-1]!=ZERO:return l,h,a+(z-a)*r
    raise AssertionError('too many exact interior roots')


def isolate(p):
    b=bernstein(p)
    assert b[0].sign() and b[-1].sign()
    todo=[(Q(0),Q(1),b)];roots=[];discarded=0;nodes=0
    while todo:
        a,z,b=todo.pop();v=variation(b);nodes+=1
        assert nodes<10000
        if v==0:discarded+=1;continue
        if v==1:roots.append({'lo':a,'hi':z,'bernstein':b});continue
        l,h,m=split_nonroot(b,a,z)
        todo.extend([(a,m,l),(m,z,h)])
    return roots,{'subdivision_nodes':nodes,'root_free_leaves':discarded}


def refine(root):
    l,h,m=split_nonroot(root['bernstein'],root['lo'],root['hi'])
    vl,vh=variation(l),variation(h)
    assert vl+vh==1
    if vl:root['hi']=m;root['bernstein']=l
    else:root['lo']=m;root['bernstein']=h


def one_sign(coeffs):
    ss=set(signs(coeffs));ss.discard(0)
    return ss.pop() if len(ss)==1 else None


def configurations(start,end,old):
    s=[start,end-start]
    an=psub([ZETA],s);ad=padd([ZETA],s)
    b=(pmul(an,an),pmul(ad,ad))
    if old:
        pn=psub([C(1)],s);pd=padd([C(1)],s)
        point=(pmul(pn,pn),pmul(pd,pd))
    else:point=(an,ad)
    return [([C(0)],[C(1)]),([C(1)],[C(1)]),b,point]


def point_at_base(old):
    a=(ZETA-BASE)*cinv(ZETA+BASE)
    if old:
        v=(C(1)-BASE)*cinv(C(1)+BASE);return v*v
    return a


def transport_configuration(old):
    a=(ZETA-BASE)*cinv(ZETA+BASE);b=a*a;p=point_at_base(old)
    return [([C(0)],[C(1)]),([C(1)],[C(1)]),([b],[C(1)]),([REFERENCE,p-REFERENCE],[C(1)])]


def projected_difference(r,i,j):
    ni,di=r[i];nj,dj=r[j]
    n=pscale(psub(pmul(ni,dj),pmul(nj,di)),PROJECTION)
    d=pmul(di,dj)
    p=pmul(n,[x.conjugate() for x in d])
    return trim([x.re for x in p]),trim([x.im for x in p])


def segment(r,label):
    pairs=[];events=[];endpoint_signs={}
    for i,j in combinations(range(4),2):
        real,height=projected_difference(r,i,j)
        s0,s1=peval(real,Q(0)).sign(),peval(real,Q(1)).sign()
        assert s0 and s1
        endpoint_signs[i,j]=(s0,s1)
        roots,tree=isolate(real)
        record={'pair':[i,j],'projected_numerator':[x.encoded() for x in real],
                'height_numerator':[x.encoded() for x in height],
                'endpoint_signs':[s0,s1],**tree,'roots':[]}
        for root in roots:
            while root['hi']-root['lo']>Q(1,2**36):refine(root)
            for extra in range(100):
                hb=bernstein(height,root['lo'],root['hi'])
                derivative=[(b-a)*(len(root['bernstein'])-1)/(root['hi']-root['lo'])
                            for a,b in zip(root['bernstein'],root['bernstein'][1:])]
                hs,ds=one_sign(hb),one_sign(derivative)
                if hs is not None and ds is not None:break
                refine(root)
            else:raise AssertionError('root height or simplicity not separated')
            root.update({'pair':(i,j),'height_sign':hs,'derivative_sign':ds,'record':record})
            events.append(root)
        pairs.append(record)
    # Refine complete isolating intervals until every time order is exact.
    for repeat in range(100):
        events.sort(key=lambda e:e['lo'])
        bad=[i for i in range(len(events)-1) if events[i]['hi']>=events[i+1]['lo']]
        if not bad:break
        for i in sorted(set(bad+[i+1 for i in bad])):refine(events[i])
    else:raise AssertionError('crossing parameters do not separate')
    def compare(i,j,endpoint):
        if i<j:return endpoint_signs[i,j][endpoint]
        return -endpoint_signs[j,i][endpoint]
    initial=sorted(range(4),key=cmp_to_key(lambda i,j:compare(i,j,0)))
    final=sorted(range(4),key=cmp_to_key(lambda i,j:compare(i,j,1)))
    order=initial[:];word=[]
    for event in events:
        i,j=event['pair'];ii,jj=order.index(i),order.index(j)
        assert abs(ii-jj)==1
        letter=(min(ii,jj)+1)*(event['height_sign'] if ii<jj else -event['height_sign'])
        word.append(letter);order[ii],order[jj]=order[jj],order[ii]
        event['record']['roots'].append({'interval':[str(event['lo']),str(event['hi'])],
                'bernstein_signs':signs(event['bernstein']),
                'height_sign':event['height_sign'],'derivative_sign':event['derivative_sign'],
                'braid_letter':letter})
    assert order==final
    return {'label':label,'initial_order':initial,'final_order':final,
            'crossing_count':len(events),'braid':nf.red(word),'pair_checks':pairs}


def certify_source_basis():
    rows=[];directions=[];r=RADIUS
    for i,c in enumerate(CENTERS):
        assert (BASE.re-c.re-r).sign()>0 and (BASE.im-c.im-r).sign()>0
        end=c+C(r,r);direction=end-BASE;directions.append(direction)
        norm=(direction*direction.conjugate()).re
        clear=[]
        for j,z in enumerate(CENTERS):
            if i==j:continue
            product=(z-BASE)*direction.conjugate();proj=product.re/norm
            if proj.sign()<0:distance=((z-BASE)*(z-BASE).conjugate()).re;where='start'
            elif (proj-1).sign()>0:distance=((z-end)*(z-end).conjugate()).re;where='end'
            else:distance=product.im*product.im/norm;where='interior'
            clearance=distance-2*r*r;assert clearance.sign()>0
            clear.append({'other_center':j,'nearest_location':where,'squared_clearance':clearance.encoded()})
        rows.append({'center':c.encoded(),'tail_end':end.encoded(),'other_square_clearance':clear})
    disjoint=[]
    for i,j in combinations(range(len(CENTERS)),2):
        z=CENTERS[i]-CENTERS[j];distance=(z*z.conjugate()).re
        assert (distance-8*r*r).sign()>0
        cross=(directions[i]*directions[j].conjugate()).im;assert cross.sign()
        disjoint.append({'pair':[i,j],'square_distance_clearance':(distance-8*r*r).encoded(),
                         'tail_cross_product':cross.encoded(),'tail_cross_sign':cross.sign()})
    return {'lassos':rows,'pairwise_disjointness':disjoint,
            'conclusion':'disjoint square meridians with an embedded common-base star; the eleven lassos are a geometric free basis'}


def certify_transport(old):
    a=(ZETA-BASE)*cinv(ZETA+BASE);punctures=[C(0),C(1),a*a]
    end=point_at_base(old);direction=end-REFERENCE;norm=(direction*direction.conjugate()).re
    checks=[]
    for z in punctures:
        product=(z-REFERENCE)*direction.conjugate();cross=product.im.sign()
        if not cross:
            t=product.re/norm;assert t.sign()<0 or (t-1).sign()>0
        checks.append({'puncture':z.encoded(),'cross':product.im.encoded(),'cross_sign':cross})
    return checks


def based_word(word):
    images=nf.artin(word,n=4);v=images[3][:];conjugator=[]
    while len(v)>1 and v[0]==-v[-1]:conjugator.append(v[0]);v=v[1:-1]
    assert v==[4]
    erase=lambda w:nf.red([x for x in w if abs(x)!=4])
    return {'braid':word,'artin_images':images,'conjugator':erase(conjugator),
            'base_automorphism':[erase(w) for w in images[:3]]}


def main():
    start_signs=nf.SIGN_COUNT
    source=certify_source_basis();segments=[];tracks={};transport_checks={}
    for name,old in [('old',True),('new',False)]:
        transport_checks[name]=certify_transport(old)
        tr=segment(transport_configuration(old),name+'_reference_transport');segments.append(tr)
        # Reference point is the fourth meridian in the fixed projection chart.
        assert tr['initial_order'][-1]==3
        tracks[name]=[]
        for i,c in enumerate(CENTERS):
            r=RADIUS;corner=c+C(r,r)
            route=[BASE,corner,c+C(-r,r),c+C(-r,-r),c+C(r,-r),corner]
            pieces=[]
            for j,(a,b) in enumerate(zip(route,route[1:])):
                item=segment(configurations(a,b,old),f'{name}_meridian_{i}_segment_{j}')
                pieces.append(item);segments.append(item)
            loop=pieces[0]['braid'][:]
            for item in pieces[1:]:loop.extend(item['braid'])
            loop.extend(nf.wi(pieces[0]['braid']))
            word=nf.red(tr['braid']+loop+nf.wi(tr['braid']))
            tracks[name].append(based_word(word))
            print(json.dumps({'completed_track':name,'source_generator':i,
                              'braid_length':len(word),'crossings_in_five_forward_segments':sum(x['crossing_count'] for x in pieces)}),flush=True)
    pairs=[]
    for i in range(len(CENTERS)):
        assert tracks['old'][i]['base_automorphism']==tracks['new'][i]['base_automorphism']
        pairs.append({'source_index':i,'old':tracks['old'][i],'new':tracks['new'][i]})
    out={'scope':'exact algebraic source-basis and crossing certificate; staged for independent mathematical audit',
         'number_field':'theta^4-5theta^2+5=0, 19/10<theta<2',
         'source_base':BASE.encoded(),'reference':REFERENCE.encoded(),'projection':PROJECTION.encoded(),
         'radius':str(RADIUS),'source_basis':source,'transport_avoidance':transport_checks,
         'source_generator_count':len(CENTERS),'old_root':C(1).encoded(),'new_sign':1,
         'certified_forward_segments':len(segments),'projected_pair_checks':6*len(segments),
         'certified_crossings':sum(s['crossing_count'] for s in segments),
         'number_field_sign_calls':nf.SIGN_COUNT-start_signs,
         'segments':segments,'pairs':pairs}
    output=Path(__file__).with_name('cross_divisor_monodromy_f20_output.json')
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('segments','pairs','source_basis','transport_avoidance')},indent=2),flush=True)


if __name__=='__main__':main()
