"""Create independently verified staging copies; never write under work/."""
from pathlib import Path
import argparse, concurrent.futures, datetime, hashlib, io, json, os, time
from PIL import Image
from png_codec import chunks

ROOT = Path('/workspace/scratch/8759b8008681')
PROBE = Path(__file__).resolve().parent
STAGE = PROBE / 'staged_final'
RECEIPTS = PROBE / 'receipts'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read_records(path):
    result = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                result[row['path']] = row
    return result


def copy_one(src):
    started = time.monotonic()
    before = src.stat()
    data = src.read_bytes()
    after = src.stat()
    if (before.st_size,before.st_mtime_ns) != (after.st_size,after.st_mtime_ns):
        raise RuntimeError('Source changed during copy: '+str(src))
    rel = src.relative_to(ROOT / 'work')
    dest = STAGE / rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    temp = dest.with_suffix('.png.copy.partial')
    temp.write_bytes(data)
    copied = temp.read_bytes()
    assert copied == data
    with Image.open(io.BytesIO(copied)) as image:
        width,height = image.size
        mode = image.mode
        decoded = image.convert('RGBA').tobytes()
        info_keys = list(image.info)
    chunk_names = [kind.decode('ascii') for kind,_,_ in chunks(copied)]
    temp.replace(dest)
    return {'path':rel.as_posix(),'source_bytes':len(data),'source_mtime_ns':after.st_mtime_ns,
            'source_sha256':hashlib.sha256(data).hexdigest(),'staged_bytes':len(copied),
            'staged_sha256':hashlib.sha256(copied).hexdigest(),'width':width,'height':height,
            'source_mode':mode,'canonical_pixel_mode':'RGBA','decoded_pixel_sha256':hashlib.sha256(decoded).hexdigest(),
            'exact_source_bytes':True,'exact_decoded_pixels':True,'info_keys':info_keys,'png_chunks':chunk_names,
            'utc':utc(),'seconds':round(time.monotonic()-started,4)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers',type=int,default=3)
    args = parser.parse_args()
    RECEIPTS.mkdir(parents=True,exist_ok=True)
    path = RECEIPTS/'base.jsonl'
    records = read_records(path)
    files = sorted((ROOT/'work/crops').glob('*.png'))
    jobs = []
    for src in files:
        rel=src.relative_to(ROOT/'work').as_posix()
        if rel in records:
            stat=src.stat();row=records[rel]
            if (stat.st_size,stat.st_mtime_ns)!=(row['source_bytes'],row['source_mtime_ns']):
                raise RuntimeError('Previously staged source changed: '+rel)
            if not (STAGE/rel).is_file(): raise RuntimeError('Missing staged copy: '+rel)
        else: jobs.append(src)
    with path.open('a') as receipt, concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(copy_one,p) for p in jobs]
        for n,future in enumerate(concurrent.futures.as_completed(futures),1):
            row=future.result();records[row['path']]=row
            receipt.write(json.dumps(row,ensure_ascii=False)+'\n');receipt.flush();os.fsync(receipt.fileno())
            if n%100==0: print(json.dumps({'copied':n,'new_jobs':len(jobs),'utc':utc()}),flush=True)
    summary={'utc':utc(),'files':len(records),'source_bytes':sum(x['source_bytes'] for x in records.values()),
             'staged_bytes':sum((STAGE/p).stat().st_size for p in records),'new_copies':len(jobs),
             'source_originals_written':False,'all_source_bytes_verified':True,'all_pixel_hashes_recorded':True}
    (RECEIPTS/'base_summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary),flush=True)


if __name__=='__main__': main()
