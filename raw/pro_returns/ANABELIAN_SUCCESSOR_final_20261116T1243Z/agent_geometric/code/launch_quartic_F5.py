"""Run disjoint exact F5 census shards, then reconcile and concatenate outputs."""
from pathlib import Path
import csv,json,subprocess,time,hashlib,collections

P=Path(__file__).resolve().parent
census=P/'plane_quartic_F5_trial2_census.csv'
with census.open() as f:rows=list(csv.DictReader(f))
assert len(rows)==94283
jobs=[];started=time.time();shards=4
for j in range(shards):
    lo=len(rows)*j//shards;hi=len(rows)*(j+1)//shards
    prefix=P/f'plane_quartic_F5_part{j}'
    stdout=(P/f'plane_quartic_F5_part{j}.stdout').open('w')
    stderr=(P/f'plane_quartic_F5_part{j}.log').open('w')
    command=[str(P/'plane_quartic_F5'),str(prefix),str(hi-lo),rows[lo]['normalized_code']]
    process=subprocess.Popen(command,stdout=stdout,stderr=stderr)
    jobs.append({'shard':j,'first_row':lo,'last_row_exclusive':hi,
                 'first_code':int(rows[lo]['normalized_code']),'count':hi-lo,
                 'prefix':str(prefix),'command':command,'process':process,
                 'stdout':stdout,'stderr':stderr})
plan=[{k:v for k,v in job.items() if k not in ('process','stdout','stderr')} for job in jobs]
(P/'plane_quartic_F5_launch_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print('Launched four disjoint shards covering all94283 pointed classes.',flush=True)
for job in jobs:
    result=job['process'].wait();job['stdout'].close();job['stderr'].close()
    assert result==0,(job['shard'],result)
    print('Completed shard',job['shard'],flush=True)

seen=[];good=least=tests=0;distribution=collections.Counter();manifest=[]
with (P/'plane_quartic_F5_tests.jsonl').open('w') as out:
    for job in jobs:
        file=Path(job['prefix']+'_tests.jsonl');count=0
        with file.open() as inp:
            for line in inp:
                record=json.loads(line);seen.append(record['normalized_code']);count+=1
                prime=record['least_successful_base_field_prime'];tests+=len(record['tests'])
                if prime:good+=1;distribution[prime]+=1
                least+=prime==3;out.write(line)
        assert count==job['count']
        manifest.append({'shard':job['shard'],'records':count,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
assert seen==[int(r['normalized_code']) for r in rows]
with (P/'plane_quartic_F5_tests.csv').open('w',newline='') as out:
    writer=None
    for job in jobs:
        with Path(job['prefix']+'_tests.csv').open() as inp:
            reader=csv.reader(inp);header=next(reader)
            if writer is None:writer=csv.writer(out);writer.writerow(header)
            for row in reader:writer.writerow(row)
(P/'plane_quartic_F5_census.csv').write_bytes(census.read_bytes())
summary={'field':5,'normalized_forms':5**12,'slice_forms':5**8+5**7+5**6,
         'smooth_normalized_forms':sum(int(r['orbit_size']) for r in rows),
         'smooth_pointed_isomorphism_classes':len(rows),'tested_pointed_classes':len(seen),
         'base_field_witnesses':good,'no_base_field_witness':len(seen)-good,
         'proved_global_least_prime_3':least,'total_prime_quotient_tests':tests,
         'least_successful_base_field_prime_distribution':dict(sorted(distribution.items())),
         'complete_disjoint_shards_verified':manifest,
         'scope':'every odd prime cyclic quotient over F5; no extension tests',
         'elapsed_seconds':time.time()-started}
(P/'plane_quartic_F5_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
