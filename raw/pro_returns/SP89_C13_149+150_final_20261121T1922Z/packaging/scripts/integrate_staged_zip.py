"""Integration helper for root review. Creates a new ZIP; never modifies work/crops.

Run only after the root reader authorizes incorporation, for example:
  python scratch/packaging_probe_reader_b/integrate_staged_zip.py \
    --output deliverables/SP89_C13_149+150.zip

The crop plan and independent verification must match the complete current crop set.
Existing output/partial files are never overwritten. No TeX compilation is performed.
"""
from pathlib import Path
import argparse, collections, hashlib, json, os, struct, zipfile
from stage_crops import ROOT, RECEIPTS, read_records, utc
from prepare_archive_crops import ARCHIVE_STAGE
HERE=Path(__file__).resolve().parent
WORK=ROOT/'work'
LIMIT=536870912


def sha(data):return hashlib.sha256(data).hexdigest()


def current_work_files():
    return sorted(p for p in WORK.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                  and p.suffix!='.zip' and p.relative_to(WORK).as_posix()!='MANIFEST.tsv')


def read_stable(path):
    before=path.stat();data=path.read_bytes();after=path.stat()
    assert (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns),('file changed during read',str(path))
    return data


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    output=Path(args.output).resolve();partial=output.with_suffix(output.suffix+'.partial')
    if not __debug__:raise RuntimeError('Run without Python optimization so validation assertions remain enabled')
    assert output.name=='SP89_C13_149+150.zip','Final archive filename must be SP89_C13_149+150.zip'
    assert not output.is_relative_to(WORK),'Refusing to write inside work'
    assert not output.is_relative_to(ARCHIVE_STAGE),'Refusing to write inside crop staging'
    report_path=output.with_suffix('.packaging-verification.json')
    if output.exists() or partial.exists() or report_path.exists():raise RuntimeError('Refusing to overwrite output, partial file or verification report')
    output.parent.mkdir(parents=True,exist_ok=True)
    started=utc();plan=read_records(RECEIPTS/'archive_crops.jsonl')
    verified=read_records(RECEIPTS/'archive_verification.jsonl')
    base=read_records(RECEIPTS/'base.jsonl')
    crop_files=[p for p in (WORK/'crops').rglob('*') if p.is_file()]
    assert all(p.parent==WORK/'crops' and p.suffix=='.png' for p in crop_files), 'Unexpected crop file type or nested path'
    originals={p.relative_to(WORK).as_posix() for p in crop_files}
    staged={p.relative_to(ARCHIVE_STAGE).as_posix() for p in (ARCHIVE_STAGE/'crops').glob('*.png')}
    assert originals==staged==set(plan)==set(verified)==set(base), 'Crop inventory changed: refresh staging and independent verification'
    assert not list((ARCHIVE_STAGE/'crops').glob('*.partial')), 'Incomplete crop writes'
    original_hashes={}
    for p in sorted(plan):
        row=plan[p];v=verified[p];b=base[p]
        assert v['original_unchanged'] and v['exact_dimensions'] and v['exact_decoded_pixels']
        assert v['source_sha256']==row['original_source_sha256']==b['source_sha256']
        assert v['archive_png_sha256']==row['archive_png_sha256']
        assert v['archive_png_bytes']==row['archive_png_bytes']
        assert v['zip_method']==row['zip_method'] and v['zip_compressed_bytes']==row['zip_compressed_bytes']
        assert row['zip_level']=={8:6,12:9}[row['zip_method']]
        assert v['decoded_RGBA_sha256']==row['decoded_pixel_sha256']==b['decoded_pixel_sha256']
        assert (v['width'],v['height'])==(row['width'],row['height'])==(b['width'],b['height'])
        original=read_stable(WORK/p);assert sha(original)==row['original_source_sha256'],('original crop changed',p)
        assert len(original)==row['original_source_bytes']
        original_hashes[p]=sha(original)
    files=current_work_files();work_names={p.relative_to(WORK).as_posix() for p in files}
    summary=json.loads((RECEIPTS/'archive_verification_summary.json').read_text())
    assert summary['files']==len(plan)
    assert summary['all_source_hashes_unchanged'] and summary['all_dimensions_identical'] and summary['all_decoded_RGBA_pixels_identical']
    assert summary['all_staged_hashes_match_receipts'] and summary['all_current_crop_paths_preserved']
    assert summary['source_bytes']==sum(row['original_source_bytes'] for row in plan.values())
    assert summary['archive_png_bytes']==sum(row['archive_png_bytes'] for row in plan.values())
    assert summary['compressed_crop_bytes']==sum(row['zip_compressed_bytes'] for row in plan.values())
    assert summary['zip_methods']=={str(method):sum(row['zip_method']==method for row in plan.values()) for method in sorted({row['zip_method'] for row in plan.values()})}
    technical={
        'packaging/README.md':(HERE/'README_final_snippet.md').read_bytes(),
        'packaging/encoding_receipts.jsonl':(''.join(json.dumps(plan[p])+'\n' for p in sorted(plan))).encode(),
        'packaging/pixel_verification.jsonl':(RECEIPTS/'archive_verification.jsonl').read_bytes(),
        'packaging/pixel_verification_summary.json':(RECEIPTS/'archive_verification_summary.json').read_bytes(),
    }
    for name in ['png_codec.py','stage_crops.py','optimize_staged.py','prepare_archive_crops.py','verify_archive_staging.py','integrate_staged_zip.py']:
        technical['packaging/scripts/'+name]=(HERE/name).read_bytes()
    assert work_names.isdisjoint(technical), 'Technical entry collides with work entry'
    method_path='packaging/ZIP_METHODS.tsv'
    all_names=work_names|set(technical)|{method_path,'MANIFEST.tsv'}
    assert len(all_names)==len(work_names)+len(technical)+2
    method_rows=[]
    for name in sorted(all_names):
        method=plan[name]['zip_method'] if name in plan else 8
        level=plan[name]['zip_level'] if name in plan else 6
        assert method in (8,12)
        method_rows.append((name,method,'BZIP2' if method==12 else 'DEFLATE',level))
    technical[method_path]=('path\tzip_method_id\tzip_method_name\tcompression_level\n'+
                            ''.join(f'{p}\t{m}\t{n}\t{level}\n' for p,m,n,level in method_rows)).encode()
    expected={};manifest=[];methods=collections.Counter();source_doc_hashes={};crop_compressed=0
    with zipfile.ZipFile(partial,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for index,path in enumerate(files,1):
            name=path.relative_to(WORK).as_posix()
            if name in plan:
                row=plan[name];data=read_stable(ARCHIVE_STAGE/name);digest=sha(data)
                assert digest==row['archive_png_sha256'] and len(data)==row['archive_png_bytes'],('staged PNG changed',name)
                assert data.startswith(b'\x89PNG\r\n\x1a\n')
                method=row['zip_method'];level=row['zip_level']
            else:
                data=read_stable(path);digest=sha(data);method=8;level=6;source_doc_hashes[name]=digest
            z.writestr(name,data,compress_type=method,compresslevel=level)
            info=z.getinfo(name)
            if name in plan:
                assert info.compress_size==plan[name]['zip_compressed_bytes'],('compressed size changed',name)
                crop_compressed+=info.compress_size
            expected[name]=digest;manifest.append((name,len(data),digest));methods[method]+=1
            if index%250==0:print(json.dumps({'entries_written':index,'work_entries':len(files),'utc':utc()}),flush=True)
        for name,data in sorted(technical.items()):
            digest=sha(data);z.writestr(name,data)
            expected[name]=digest;manifest.append((name,len(data),digest));methods[8]+=1
        manifest_data=('path\tbytes\tsha256\n'+''.join(f'{p}\t{n}\t{h}\n' for p,n,h in sorted(manifest))).encode()
        z.writestr('MANIFEST.tsv',manifest_data);expected['MANIFEST.tsv']=sha(manifest_data);methods[8]+=1
    assert partial.stat().st_size<LIMIT,('Archive is not below upload limit',partial.stat().st_size,LIMIT)
    assert {p.relative_to(WORK).as_posix() for p in current_work_files()}==work_names,'Work file inventory changed during packaging'
    for name,digest in source_doc_hashes.items():
        assert sha(read_stable(WORK/name))==digest,('Work document changed during packaging',name)
    for name,digest in original_hashes.items():
        assert sha(read_stable(WORK/name))==digest,('Original crop changed during packaging',name)
    with zipfile.ZipFile(partial) as z:
        assert len(z.namelist())==len(expected) and set(z.namelist())==set(expected)
        for name,digest in expected.items():
            assert sha(z.read(name))==digest,('Extracted entry hash mismatch',name)
        for name,method,_,level in method_rows:assert z.getinfo(name).compress_type==method
        with partial.open('rb') as raw:
            for name,row in sorted(plan.items()):
                info=z.getinfo(name);raw.seek(info.header_offset);header=raw.read(30)
                assert header[:4]==b'PK\x03\x04',('Local ZIP header',name)
                name_len,extra_len=struct.unpack_from('<HH',header,26)
                raw.seek(info.header_offset+30+name_len+extra_len)
                digest=hashlib.sha256();remaining=info.compress_size
                while remaining:
                    chunk=raw.read(min(1048576,remaining));assert chunk,('Truncated ZIP entry',name)
                    digest.update(chunk);remaining-=len(chunk)
                assert digest.hexdigest()==row['zip_compressed_payload_sha256'],('Compressed payload hash',name)
        assert z.testzip() is None,'ZIP CRC verification failed'
    assert not output.exists(),'Output appeared during build'
    partial.replace(output)
    report={'started_utc':started,'finished_utc':utc(),'path':str(output),'zip_bytes':output.stat().st_size,
            'upload_limit_bytes':LIMIT,'headroom_bytes':LIMIT-output.stat().st_size,'entries':len(expected),
            'crops':len(plan),'compressed_crop_bytes':crop_compressed,'extracted_crop_bytes':summary['archive_png_bytes'],
            'method_counts':dict(methods),'all_original_crop_hashes_verified_before_and_after':True,
            'all_work_document_hashes_verified_unchanged_after_packaging':True,
            'all_staged_crop_hashes_match_independent_pixel_verification':True,
            'all_extracted_entry_hashes_verified':True,'all_ZIP_CRCs_verified':True,
            'all_crop_compressed_payload_hashes_verified':True,
            'all_crop_paths_preserved':True,'work_written':False,'sha256':sha(output.read_bytes())}
    assert not report_path.exists(),'Verification report appeared during build'
    report_path.write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)

if __name__=='__main__':main()
