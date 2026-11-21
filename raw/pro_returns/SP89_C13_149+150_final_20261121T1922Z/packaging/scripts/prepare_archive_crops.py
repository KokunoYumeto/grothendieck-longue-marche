"""Prepare valid pixel-identical PNG copies for per-entry standard ZIP compression.
Only scratch staging and receipts are written. No manuscript reading occurs.
"""
from pathlib import Path
import argparse, bz2, concurrent.futures, hashlib, io, json, os, time, zlib
from PIL import Image
from png_codec import chunks, replace_idat
from stage_crops import ROOT, STAGE, RECEIPTS, read_records, utc
ARCHIVE_STAGE=Path(__file__).resolve().parent/'staged_archive'

def prepare_one(job):
    path,base,current=job
    started=time.monotonic()
    data=(STAGE/path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==current['staged_sha256'],('input changed',path)
    cs=list(chunks(data))
    filtered=zlib.decompress(b''.join(payload for kind,payload,_ in cs if kind==b'IDAT'))
    stored=replace_idat(data,zlib.compress(filtered,level=0))
    compressed_bzip=bz2.compress(stored,compresslevel=9)
    assert bz2.decompress(compressed_bzip)==stored
    deflater=zlib.compressobj(6,zlib.DEFLATED,-15)
    compressed_normal=deflater.compress(data)+deflater.flush()
    assert zlib.decompress(compressed_normal,-15)==data
    if len(compressed_bzip)<len(compressed_normal):
        selected=stored;method=12;compressed=compressed_bzip;encoding='stored_IDAT_BZIP2_9';level=9
    else:
        selected=data;method=8;compressed=compressed_normal;encoding='optimized_PNG_DEFLATE_6';level=6
    with Image.open(io.BytesIO(selected)) as im:
        assert im.size==(base['width'],base['height'])
        pixels=im.convert('RGBA').tobytes()
        pixel_hash=hashlib.sha256(pixels).hexdigest()
        assert pixel_hash==base['decoded_pixel_sha256'],('pixel mismatch',path)
        mode=im.mode
    dest=ARCHIVE_STAGE/path;dest.parent.mkdir(parents=True,exist_ok=True)
    temp=dest.with_suffix('.png.archive.partial');temp.write_bytes(selected)
    output_hash=hashlib.sha256(selected).hexdigest()
    assert hashlib.sha256(temp.read_bytes()).hexdigest()==output_hash
    temp.replace(dest)
    return {'path':path,'original_source_sha256':base['source_sha256'],'original_source_bytes':base['source_bytes'],
            'input_optimized_sha256':current['staged_sha256'],'input_optimized_bytes':len(data),
            'archive_png_sha256':output_hash,'archive_png_bytes':len(selected),
            'zip_method':method,'zip_level':level,'zip_compressed_bytes':len(compressed),
            'zip_compressed_payload_sha256':hashlib.sha256(compressed).hexdigest(),
            'selected_encoding':encoding,'candidate_compressed_bytes':{'stored_IDAT_BZIP2_9':len(compressed_bzip),'optimized_PNG_DEFLATE_6':len(compressed_normal)},
            'width':base['width'],'height':base['height'],'archive_png_mode':mode,
            'canonical_pixel_mode':'RGBA','decoded_pixel_sha256':pixel_hash,
            'exact_decoded_pixels':True,'exact_compression_roundtrip':True,'utc':utc(),'seconds':round(time.monotonic()-started,4)}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=1);args=parser.parse_args()
    base=read_records(RECEIPTS/'base.jsonl');optimized=read_records(RECEIPTS/'optimized.jsonl')
    records=read_records(RECEIPTS/'archive_crops.jsonl')
    jobs=[(p,base[p],current) for p,current in optimized.items() if p in base and
          (p not in records or records[p]['input_optimized_sha256']!=current['staged_sha256'])]
    jobs.sort(key=lambda job:job[2]['staged_bytes'],reverse=True)
    completed=0
    with (RECEIPTS/'archive_crops.jsonl').open('a') as receipt, concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        for row in pool.map(prepare_one,jobs,chunksize=1):
            records[row['path']]=row;completed+=1
            receipt.write(json.dumps(row)+'\n');receipt.flush();os.fsync(receipt.fileno())
            if completed%50==0:
                status={'utc':utc(),'completed_this_run':completed,'jobs_this_run':len(jobs),'prepared_paths':len(records),
                        'compressed_crop_bytes':sum(x['zip_compressed_bytes'] for x in records.values()),
                        'archive_png_bytes':sum(x['archive_png_bytes'] for x in records.values())}
                (RECEIPTS/'archive_status.json').write_text(json.dumps(status,indent=2));print(json.dumps(status),flush=True)
    status={'utc':utc(),'completed_this_run':completed,'jobs_this_run':len(jobs),'prepared_paths':len(records),
            'known_base_paths':len(base),'unprepared_paths':sorted(set(base)-set(records)),
            'compressed_crop_bytes':sum(x['zip_compressed_bytes'] for x in records.values()),
            'archive_png_bytes':sum(x['archive_png_bytes'] for x in records.values()),
            'original_png_bytes':sum(base[p]['source_bytes'] for p in records if p in base),
            'all_prepared_pixels_verified':True,'source_originals_written':False}
    (RECEIPTS/'archive_status.json').write_text(json.dumps(status,indent=2));print(json.dumps(status),flush=True)

if __name__=='__main__':main()
