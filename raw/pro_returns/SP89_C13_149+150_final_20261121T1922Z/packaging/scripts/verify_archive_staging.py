"""Independent source/staged exact pixel check for archive PNG copies."""
from pathlib import Path
import argparse, concurrent.futures, hashlib, io, json, os
from PIL import Image
from stage_crops import ROOT, RECEIPTS, read_records, utc
from prepare_archive_crops import ARCHIVE_STAGE

def verify_one(job):
    path,base,plan=job
    original=(ROOT/'work'/path).read_bytes();staged=(ARCHIVE_STAGE/path).read_bytes()
    source_hash=hashlib.sha256(original).hexdigest();staged_hash=hashlib.sha256(staged).hexdigest()
    assert source_hash==base['source_sha256']==plan['original_source_sha256'],('source changed',path)
    assert staged_hash==plan['archive_png_sha256'],('staged bytes changed',path)
    assert len(original)==base['source_bytes'] and len(staged)==plan['archive_png_bytes']
    with Image.open(io.BytesIO(original)) as a, Image.open(io.BytesIO(staged)) as b:
        assert a.size==b.size==(base['width'],base['height']),('dimensions',path)
        first=a.convert('RGBA').tobytes();second=b.convert('RGBA').tobytes()
        assert first==second,('pixels',path)
        pixel_hash=hashlib.sha256(second).hexdigest();assert pixel_hash==base['decoded_pixel_sha256']
        source_mode=a.mode;staged_mode=b.mode
    return {'path':path,'source_sha256':source_hash,'archive_png_sha256':staged_hash,
            'decoded_RGBA_sha256':pixel_hash,'width':base['width'],'height':base['height'],
            'source_mode':source_mode,'archive_png_mode':staged_mode,'archive_png_bytes':len(staged),
            'zip_method':plan['zip_method'],'zip_compressed_bytes':plan['zip_compressed_bytes'],
            'original_unchanged':True,'exact_dimensions':True,'exact_decoded_pixels':True,'utc':utc()}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=3);args=parser.parse_args()
    base=read_records(RECEIPTS/'base.jsonl');plan=read_records(RECEIPTS/'archive_crops.jsonl')
    originals={p.relative_to(ROOT/'work').as_posix() for p in (ROOT/'work/crops').glob('*.png')}
    staged={p.relative_to(ARCHIVE_STAGE).as_posix() for p in (ARCHIVE_STAGE/'crops').glob('*.png')}
    if originals!=set(base) or staged!=set(base) or set(plan)!=set(base):
        raise RuntimeError({'new_originals':sorted(originals-set(base)),'missing_originals':sorted(set(base)-originals),
                            'missing_staged':sorted(set(base)-staged),'extra_staged':sorted(staged-set(base)),
                            'missing_plan':sorted(set(base)-set(plan))})
    assert not list((ARCHIVE_STAGE/'crops').glob('*.partial'))
    records=[];target=RECEIPTS/'archive_verification.jsonl';temp=target.with_suffix('.jsonl.partial')
    with temp.open('w') as report,concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        for row in pool.map(verify_one,[(p,row,plan[p]) for p,row in sorted(base.items())]):
            records.append(row);report.write(json.dumps(row)+'\n')
        report.flush();os.fsync(report.fileno())
    temp.replace(target)
    summary={'utc':utc(),'files':len(records),'source_bytes':sum(x['source_bytes'] for x in base.values()),
             'archive_png_bytes':sum(x['archive_png_bytes'] for x in records),
             'compressed_crop_bytes':sum(x['zip_compressed_bytes'] for x in records),
             'upload_limit_bytes':536870912,
             'all_source_hashes_unchanged':True,'all_staged_hashes_match_receipts':True,'all_dimensions_identical':True,
             'all_decoded_RGBA_pixels_identical':True,'all_current_crop_paths_preserved':True,
             'zip_methods':{str(method):sum(x['zip_method']==method for x in records) for method in sorted({x['zip_method'] for x in records})}}
    (RECEIPTS/'archive_verification_summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary),flush=True)

if __name__=='__main__':main()
