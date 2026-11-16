"""All F256 prime-character tests for the 26 points remaining after F64."""
import json,csv,time,concurrent.futures
from pathlib import Path
from A4_F4_extension_search import compute
P=Path(__file__).parent
def main():
    records=[json.loads(x) for x in (P/'A4_genus2_F4.jsonl').read_text().splitlines()]
    rem=json.loads((P/'A4_F4_extensions.summary.json').read_text())['remaining']
    tasks=[(records[x['model_id']],283,x['points']) for x in rem]
    start=time.time();remaining=[];tests=0
    with (P/'A4_F4_F256.jsonl').open('w') as out,(P/'A4_F4_F256.csv').open('w',newline='') as cs:
        wr=csv.writer(cs);wr.writerow(['F4_model_id','original_point','L_q','ell','character','L_polynomial','relative_class_number_mod2','least_prime_status'])
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
            for i,res in enumerate(pool.map(compute,tasks),1):
                out.write(json.dumps(res,separators=(',',':'))+'\n');out.flush()
                for t in res['tests']:
                    wr.writerow([res['model_id'],json.dumps(t['original_point']),256,t['ell'],json.dumps(t['character']),json.dumps(t['L_polynomial'],separators=(',',':')),t['relative_class_number_mod2'],'not asserted; all F256 prime characters tested'])
                cs.flush();tests+=len(res['tests'])
                if res['remaining']:remaining.append({'model_id':res['model_id'],'points':res['remaining']})
                print(json.dumps({'done':i,'total':len(tasks),'id':res['model_id'],'J':res['J_order'],'tests':len(res['tests']),'remaining':res['remaining'],'elapsed':time.time()-start}),flush=True)
    (P/'A4_F4_F256.summary.json').write_text(json.dumps({'tests':tests,'remaining':remaining,'elapsed':time.time()-start},indent=2)+'\n')
if __name__=='__main__':main()
