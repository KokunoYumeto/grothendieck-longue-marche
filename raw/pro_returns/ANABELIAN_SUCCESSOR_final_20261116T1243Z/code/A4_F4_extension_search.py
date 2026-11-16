"""Continue precisely the unsuccessful F4 pointed tests over F16 and F64.

All prime-cyclic pointed constant-deck covers over each tested extension
are retained.  A witness here is not asserted to have the least prime.
"""
import json,csv,time,collections,concurrent.futures
from pathlib import Path
from itertools import product
from finite_jacobian import *
from even_jacobian import *
from A4_genus2_census import mod2gcd

HERE=Path(__file__).parent
def compute(task):
    rec,modulus,targets=task;F=BinaryField(modulus);a=F.embed_f4()
    embed=lambda x:(x&1)^ (a if x&2 else 0)
    model=rec['model'];h=tuple(map(embed,model['h']));f=tuple(map(embed,model['f']))
    J=(EvenJacobian if model['even'] else Jacobian)(F,h,f)
    pts=J.points();elts=J.enumerate();target_map={}
    for name in targets:
        mapped=name if isinstance(name,str) else tuple(map(embed,name))
        target_map[str(mapped)]=name
    selected=[(name,D) for name,D in pts if str(name) in target_map]
    assert len(selected)==len(targets),(rec['index'],targets,selected)
    tests=[];quotients=[]
    for ell in prime_factors(len(elts)):
        if ell==2:continue
        coords,basis,H=J.quotient(ell);r=len(basis)
        quotients.append({'ell':ell,'basis':basis,'ell_rank':r,'ellJ_order':len(H)})
        for v in product(range(ell),repeat=r):
            if not any(v) or next(x for x in v if x)!=1:continue
            chi=lambda D:sum(x*y for x,y in zip(v,coords[D]))%ell
            values=[chi(D) for _,D in pts]
            canonical=chi(getattr(J,'canonical_base_class',J.zero))
            for P,D in selected:
                pval=chi(D);counts=collections.Counter((x-pval)%ell for x in values)
                theta=1
                for x,n in counts.items():
                    if n%2:theta^=1<<x
                gd=mod2gcd(theta,(1<<ell)-1).bit_length()-1
                tests.append({'original_point':target_map[str(P)],'point':P,'ell':ell,'character':v,
                    'L_polynomial':[1,sorted(counts.items()),[(canonical-2*pval)%ell,F.q]],
                    'relative_class_number_mod2':int(gd==0),'mod2_gcd_degree':gd})
    good={str(t['original_point']) for t in tests if t['relative_class_number_mod2']}
    remaining=[x for x in targets if str(x) not in good]
    return {'model_id':rec['index'],'q':F.q,'field_modulus':modulus,'alpha':a,'h':h,'f':f,
            'J_order':len(elts),'N':len(pts),'quotients':quotients,'tests':tests,
            'targets':targets,'remaining':remaining}

def main():
    records=[json.loads(x) for x in (HERE/'A4_genus2_F4.jsonl').read_text().splitlines()]
    tasks=[]
    for rec in records:
        if not rec['rational_points']:continue
        F=BinaryField(7);m=rec['model'];J=(EvenJacobian if m['even'] else Jacobian)(F,m['h'],m['f'])
        pts=[name for name,_ in J.points()]
        good={str(t['point']) for t in rec['tests'] if t['relative_class_number_mod2']}
        # JSON point lists and in-memory tuples are normalized explicitly.
        key=lambda p:json.dumps(p)
        good={key(t['point']) for t in rec['tests'] if t['relative_class_number_mod2']}
        targets=[p for p in pts if key(p) not in good]
        if targets:tasks.append((rec,19,targets))
    totals=[]
    with (HERE/'A4_F4_extensions.jsonl').open('w') as out,(HERE/'A4_F4_extensions.csv').open('w',newline='') as cs:
        writer=csv.writer(cs);writer.writerow(['F4_model_id','original_point','L_q','ell','character','L_polynomial','relative_class_number_mod2','least_prime_status'])
        for modulus in [19,67]:
            start=time.time();next_tasks=[];count=0;tests=0;remaining_count=0
            with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
                for task,res in zip(tasks,pool.map(compute,tasks)):
                    out.write(json.dumps(res,separators=(',',':'))+'\n');out.flush()
                    for t in res['tests']:
                        writer.writerow([res['model_id'],json.dumps(t['original_point']),res['q'],t['ell'],json.dumps(t['character']),json.dumps(t['L_polynomial'],separators=(',',':')),t['relative_class_number_mod2'],'not asserted; all listed-field prime characters tested'])
                    cs.flush();count+=1;tests+=len(res['tests']);remaining_count+=len(res['remaining'])
                    if res['remaining']:next_tasks.append((task[0],67,res['remaining']))
                    print(json.dumps({'q':res['q'],'done':count,'models':len(tasks),'model_id':res['model_id'],'remaining_points':remaining_count,'elapsed':round(time.time()-start,2)}),flush=True)
            totals.append({'q':1<<(modulus.bit_length()-1),'models_tested':count,'tests':tests,'remaining_points':remaining_count,'elapsed':time.time()-start})
            tasks=next_tasks
    (HERE/'A4_F4_extensions.summary.json').write_text(json.dumps({'rounds':totals,'remaining':[{'model_id':r['index'],'points':pts} for r,mod,pts in tasks]},indent=2)+'\n')

if __name__=='__main__':main()
