"""Complete prime-character test on two specified F4 models over listed fields."""
import json,sys,time
from pathlib import Path
from finite_jacobian import *

def run(modulus,key):
    start=time.time();F=BinaryField(modulus);R=PolynomialRing(F);a=F.embed_f4()
    if key=='302':a=F.mul(a,a)
    h=(a,1,1);G=(a^1,1,1,1);J=Jacobian(F,h,R.mul(h,G))
    rows=genus2_characters(J)
    for row in rows:row['class']=key
    out={'class':key,'field_q':F.q,'alpha':a,'h':h,'f':J.f,'N':len(J.points()),'J_order':len(J.enumerate()),'tests':rows,'elapsed':time.time()-start}
    Path(__file__).with_name(f'A4_{key}_F{F.q}_output.json').write_text(json.dumps(out,indent=2)+'\n')
    pts=J.points();basepoints=[name for name,D in pts if name=='infinity' or all(F.power(t,4)==t for t in name)]
    brief=[]
    for P in basepoints:
        rs=[r for r in rows if r['point']==P]
        brief.append({'P':P,'witnesses':[(r['ell'],r['character_vector'],r['relative_class_number']) for r in rs if r['L1_passes']],'tests':len(rs)})
    print(json.dumps({'class':key,'q':F.q,'alpha':a,'N':out['N'],'J':out['J_order'],'original_F4_points':brief,'elapsed':out['elapsed']},indent=2),flush=True)

if __name__=='__main__':
    for modulus in map(int,sys.argv[1:] or ['7','19','67']):
        for key in ('203','302'):run(modulus,key)
