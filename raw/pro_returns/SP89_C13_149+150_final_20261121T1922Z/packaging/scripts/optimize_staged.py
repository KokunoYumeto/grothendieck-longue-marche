"""Resumable optimization of verified copies only. Does not write under work/."""
from pathlib import Path
import argparse, concurrent.futures, hashlib, io, json, os, time
from PIL import Image
from png_codec import encode_fixed, recompress_idat, optimize
from stage_crops import STAGE, RECEIPTS, read_records, utc


def optimize_one(job):
    base, previous, strategies, strong, iterations, phase = job
    path=base['path'];dest=STAGE/path
    started=time.monotonic();data=dest.read_bytes()
    assert hashlib.sha256(data).hexdigest()==previous['staged_sha256'],path
    with Image.open(io.BytesIO(data)) as image:
        assert image.size==(base['width'],base['height'])
        assert hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest()==base['decoded_pixel_sha256']
    candidates={'existing':data}
    if strong:
        candidates['zopflipng_default_'+str(iterations)]=optimize(data,strong=True,iterations=iterations)
    else:
        candidates['existing_filters_libdeflate12']=recompress_idat(data)
        for strategy in strategies:
            candidates['fixed_'+str(strategy)+'_libdeflate12']=encode_fixed(data,strategy=strategy)
    name,result=min(candidates.items(),key=lambda kv:len(kv[1]))
    with Image.open(io.BytesIO(result)) as image:
        assert image.size==(base['width'],base['height'])
        actual_hash=hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest()
        assert actual_hash==base['decoded_pixel_sha256'],path
        mode=image.mode
    temp=dest.with_suffix('.png.optimized.partial')
    temp.write_bytes(result)
    assert hashlib.sha256(temp.read_bytes()).hexdigest()==hashlib.sha256(result).hexdigest()
    temp.replace(dest)
    return {'path':path,'phase':phase,'completed_phases':previous.get('completed_phases',[])+[phase],
            'source_sha256':base['source_sha256'],'source_bytes':base['source_bytes'],
            'before_staged_bytes':len(data),'before_staged_sha256':hashlib.sha256(data).hexdigest(),
            'staged_bytes':len(result),'staged_sha256':hashlib.sha256(result).hexdigest(),
            'selected_encoder':name,'candidate_bytes':{k:len(v) for k,v in candidates.items()},
            'width':base['width'],'height':base['height'],'staged_mode':mode,
            'canonical_pixel_mode':'RGBA','decoded_pixel_sha256':actual_hash,'exact_decoded_pixels':True,
            'utc':utc(),'seconds':round(time.monotonic()-started,4)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--workers',type=int,default=3)
    parser.add_argument('--strategies',default='2')
    parser.add_argument('--phase',required=True)
    parser.add_argument('--strong',action='store_true')
    parser.add_argument('--iterations',type=int,default=5)
    parser.add_argument('--target-bytes',type=int,default=0)
    args=parser.parse_args()
    base=read_records(RECEIPTS/'base.jsonl');history=read_records(RECEIPTS/'optimized.jsonl')
    current={p:history.get(p,row) for p,row in base.items()}
    strategies=[int(x) for x in args.strategies.split(',') if x]
    keys=[p for p,row in current.items() if args.phase not in row.get('completed_phases',[])]
    keys.sort(key=lambda p:current[p]['staged_bytes'],reverse=True)
    total=sum(row['staged_bytes'] for row in current.values())
    completed=0
    with (RECEIPTS/'optimized.jsonl').open('a') as receipt, concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        iterator=iter(keys);pending={}
        def submit_one():
            if args.target_bytes and total<=args.target_bytes:return False
            try:p=next(iterator)
            except StopIteration:return False
            future=pool.submit(optimize_one,(base[p],current[p],strategies,args.strong,args.iterations,args.phase));pending[future]=p
            return True
        for _ in range(args.workers):submit_one()
        while pending:
            done,_=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                p=pending.pop(future);row=future.result()
                total+=row['staged_bytes']-current[p]['staged_bytes'];current[p]=row;completed+=1
                receipt.write(json.dumps(row,ensure_ascii=False)+'\n');receipt.flush();os.fsync(receipt.fileno())
                if completed%50==0:
                    status={'phase':args.phase,'completed':completed,'eligible_jobs':len(keys),'files':len(base),'staged_bytes':total,'utc':utc()}
                    (RECEIPTS/'status.json').write_text(json.dumps(status,indent=2));print(json.dumps(status),flush=True)
                submit_one()
    status={'phase':args.phase,'completed':completed,'eligible_jobs':len(keys),'files':len(base),
            'source_bytes':sum(x['source_bytes'] for x in base.values()),'staged_bytes':total,
            'saved_bytes':sum(x['source_bytes'] for x in base.values())-total,'utc':utc(),
            'source_originals_written':False,'all_staged_pixels_verified':True,'target_bytes':args.target_bytes}
    (RECEIPTS/(args.phase+'_summary.json')).write_text(json.dumps(status,indent=2))
    (RECEIPTS/'status.json').write_text(json.dumps(status,indent=2));print(json.dumps(status),flush=True)


if __name__=='__main__': main()
