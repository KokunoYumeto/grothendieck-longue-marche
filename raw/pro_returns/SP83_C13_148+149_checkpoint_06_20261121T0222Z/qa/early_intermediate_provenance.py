"""Verify recovered A15 geometry without writing any evidence image.

Only the two sibling provenance reports are written. Source scans, retained
crops, accepted records, aggregate deliverables, frozen readings, and the
19-audit method snapshot are read-only inputs.
"""
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO
import hashlib
import json

import numpy as np
from PIL import Image, ImageFilter, ImageOps, __version__ as pillow_version

BASE = Path(__file__).resolve().parents[2]
QA = BASE / 'result/qa'
RECIPES = [
    ('148_scan051_r_arrow.png', '148_scan051', [631,1612,1023,1745], 0, (2300,780),115),
    ('148_scan053_cela.png', '148_scan053', [356,1627,1032,1714], 0, (3000,386),105),
    ('148_scan053_margin3.png', '148_scan053', [20,720,746,1409], 52, (3000,3021),105),
    ('148_scan053_margin4.png', '148_scan053', [20,1166,657,1812], 54, (3000,2990),105),
]
SNAPSHOT = {
    'reader_a_method_findings.md': '088ac04f5de485399acee4d91676db7adc602a753a7a94f86cb4055a49f4f58b',
    'reader_a_method_findings.json': '1ccc92c5e569577cb4971c2ce4bee009d9a331ff1aefc872055ca7bbe914fe59',
    'reader_a_method_audit.py': 'ce9a4c3d7315760a1b757d6d3336938d2cc3daefb40448daf06cdb6c64265d3f',
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def reference_paths(value, filename, path=''):
    if isinstance(value,dict):
        return [p for k,v in value.items() for p in reference_paths(v,filename,path+'/'+str(k))]
    if isinstance(value,list):
        return [p for i,v in enumerate(value) for p in reference_paths(v,filename,path+'/'+str(i))]
    if isinstance(value,str) and value.endswith('/'+filename):
        return [path]
    return []

def main():
    for filename, expected in SNAPSHOT.items():
        assert sha((QA/filename).read_bytes()) == expected, filename+' snapshot changed'
    rows=[]
    for name,page,box,angle,size,percent in RECIPES:
        source_path=BASE/'source/SP83_C13_148+149_scans'/(page+'.jpg')
        target_path=BASE/'result/crops'/name
        target_bytes=target_path.read_bytes()
        source=Image.open(source_path).convert('RGB')
        original=Image.open(target_path).convert('RGB')
        crop=source.crop(box)
        local_contrast_identity=np.array_equal(np.asarray(crop),np.asarray(ImageOps.autocontrast(crop)))
        global_contrast_identity=np.array_equal(np.asarray(crop),np.asarray(ImageOps.autocontrast(source).crop(box)))
        intermediate=crop.rotate(-angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white') if angle else crop
        candidate=intermediate.resize(size,Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,percent,3))
        a,b=np.asarray(original),np.asarray(candidate)
        assert a.shape==b.shape
        pixel_mismatches=int(np.count_nonzero(np.any(a!=b,axis=2)))
        channel_mismatches=int(np.count_nonzero(a!=b))
        maximum_error=int(np.max(np.abs(a.astype(np.int16)-b.astype(np.int16))))
        assert pixel_mismatches==channel_mismatches==maximum_error==0, name+' reconstruction differs'
        buf=BytesIO(); candidate.save(buf,format='PNG')
        png_bytes_equal=(buf.getvalue()==target_bytes)
        after=sha(target_path.read_bytes())
        assert after==sha(target_bytes), name+' evidence file changed'
        record_path=BASE/'result/records'/(page+'.json')
        record_bytes=record_path.read_bytes()
        paths=reference_paths(json.loads(record_bytes),name)
        assert paths and all(p.startswith('/main_reader_crops/') for p in paths), paths
        rows.append({
            'crop':'result/crops/'+name,
            'source':'source/SP83_C13_148+149_scans/'+page+'.jpg',
            'source_sha256':sha(source_path.read_bytes()),
            'source_box':box,
            'native_crop_size':list(crop.size),
            'clockwise_rotation_degrees':angle,
            'rotation_resampling':'BICUBIC' if angle else None,
            'rotation_expand':bool(angle),
            'rotation_fill':'white (255,255,255)' if angle else None,
            'rotated_intermediate_size':list(intermediate.size),
            'resize':{'size':list(size),'resampling':'LANCZOS'},
            'unsharp_mask':{'radius':1.2,'percent':percent,'threshold':3},
            'autocontrast':{'local_identity':local_contrast_identity,'global_identity':global_contrast_identity,
                'note':'Identity operations cannot be distinguished from their omission; this is a validated reconstruction, not a recovered historical command log.'},
            'crop_sha256_before':sha(target_bytes),
            'crop_sha256_after':after,
            'verification':{'all_rgb_channels_compared':int(a.size),'pixel_mismatches':pixel_mismatches,
                'channel_mismatches':channel_mismatches,'maximum_absolute_channel_error':maximum_error,
                'raw_rgb_sha256':sha(a.tobytes()),'in_memory_png_byte_identical':png_bytes_equal},
            'accepted_reference_locations':{'record':'result/records/'+page+'.json','record_sha256_at_check':sha(record_bytes),'json_pointers':paths},
            'final_mandatory_evidence':False,
            'recovery_status':'Exact original rectangle and output pixels recovered by geometry matching; original generator not found.',
        })
    generated=datetime.now(timezone.utc).isoformat()
    report={
        'finding':'A15',
        'status':'resolved by exact pixel-geometry recovery in this standalone addendum',
        'generated_utc':generated,
        'pillow_version':pillow_version,
        'coordinate_convention':'Original source pixels [left, top, right, bottom]; left/top inclusive and right/bottom exclusive (Pillow).',
        'method':'Existing metadata/script search followed by grayscale normalized cross-correlation, scale/rotation registration, integer rectangle refinement, and in-memory full RGB/PNG comparison. No OCR or text recognition.',
        'historical_limit':'The original first-pass generators for these four intermediates were not located. Identity transforms and the exact historical command order cannot be reconstructed uniquely. The reported recipe is an empirically exact reconstruction.',
        'final_mandatory_evidence_note':'None of the four intermediates is final mandatory evidence. Their accepted-record references are only retained main_reader_crops registry entries, not change, decision, implicit-decision, or audit evidence references.',
        'source_or_crop_files_written':False,
        'accepted_records_or_aggregates_edited':False,
        'method_report_snapshot_preserved':{'finalized_audits':19,'hashes':SNAPSHOT},
        'files':rows,
        'supporting_files':['result/qa/early_small_crop_recovery.py','result/qa/early_small_crop_recovery.json','result/qa/early_margin_crop_recovery.py','result/qa/early_margin_crop_registration.json'],
    }
    (QA/'early_intermediate_provenance.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    table=[]
    for row in rows:
        name=Path(row['crop']).name
        box=', '.join(map(str,row['source_box']))
        out=' × '.join(map(str,row['resize']['size']))
        table.append(f"| `{name}` | `[{box}]` | {row['clockwise_rotation_degrees']}° | {out} | {row['unsharp_mask']['percent']} |")
    hashes='\n'.join(f"| `{Path(row['crop']).name}` | `{row['crop_sha256_before']}` |" for row in rows)
    all_bytes=all(r['verification']['in_memory_png_byte_identical'] for r in rows)
    md=f'''# A15: provenance of four retained early intermediate crops

**All four original rectangles are now recovered exactly.** This standalone addendum resolves the missing-coordinate finding in `reader_a_method_findings.md`; that earlier report remains unchanged as its original **19-finalized-audit snapshot**. The later adjudications remain the main reader's work.

## Recovered geometry

Coordinates use the original JPEG pixels and Pillow's `[left, top, right, bottom]` convention: left/top inclusive, right/bottom exclusive. The source is `source/SP83_C13_148+149_scans/148_scan051.jpg` for the first row and `148_scan053.jpg` for the other three.

| Retained crop | Exact original box | Clockwise rotation | Final size | Unsharp percent |
| --- | --- | ---: | ---: | ---: |
{chr(10).join(table)}

After cropping, rotated images use Pillow BICUBIC rotation with `expand=True` and white fill. Every image then uses a LANCZOS resize to the stated final size, followed by `UnsharpMask(radius=1.2, percent=<table>, threshold=3)`. The rotated intermediate sizes are 990 × 997 for `margin3` and 899 × 896 for `margin4`.

## Evidence and limits of the recovery

The original first-pass generator files for these four intermediates were not located in the retained proposal/scripts work. The later 053 `crop_transforms` entries document different, superseding clause strips and do not supply these two early rotated rectangles. The missing geometry was therefore recovered by pixel matching: normalized grayscale cross-correlation located the unrotated crops; boundary geometry and scale/rotation registration located the rotated ones; integer rectangles were refined against the source image. No OCR, textual recognition, or mathematical reading was used.

The final verification reconstructs the candidates **in memory only** and compares every RGB channel against the existing crop files. All four have **zero differing pixels, zero differing channels, and zero maximum channel error**. Default PNG encoding of each in-memory candidate is also byte-identical to its retained PNG: **{str(all_bytes).lower()}**. This supports exact source rectangles and output transformations, not merely approximate locations.

This is an empirically exact reconstruction, **not a claim that the original command log survived**. Local-crop and full-source autocontrast are identity operations on these four pixel regions, so their historical inclusion cannot be distinguished from omission. No additional coordinates remain missing among the four A15 files.

## Evidence role and preservation

**None of these four retained intermediates is final mandatory evidence.** At this check, each appears in its accepted record only in the `main_reader_crops` registry; no accepted change, supplied-mark decision, implicit decision, or final audit evidence field cites it. The JSON companion records those reference locations and the accepted-record hashes at the time of this check. The report does not alter those records.

No crop, source scan, half image, accepted page/record, aggregate, or frozen reading was written, replaced, regenerated on disk, or deleted. Candidate arrays and temporary PNG encodings existed only in memory. Before/after SHA256 values for every retained crop match:

| Retained crop | Unchanged SHA256 |
| --- | --- |
{hashes}

The original method Markdown/JSON reports and their generator retain their recorded hashes. They were not rerun or updated to a later adjudication count.

## Reproducible documentation

- `result/qa/early_intermediate_provenance.json` contains complete boxes, transformations, source/crop hashes, RGB comparison counts, PNG-byte comparisons, and evidence-role checks.
- `result/qa/early_intermediate_provenance.py` verifies all four recipes without writing image files; it writes only this addendum and its JSON companion.
- `result/qa/early_small_crop_recovery.py` and its JSON/search outputs retain the two small-crop recovery process.
- `result/qa/early_margin_crop_recovery.py` and `early_margin_crop_registration.json` retain the two rotated-crop registration process.

Verification UTC: `{generated}`. Pillow version: `{pillow_version}`.
'''
    (QA/'early_intermediate_provenance.md').write_text(md)
    for filename,expected in SNAPSHOT.items():
        assert sha((QA/filename).read_bytes())==expected, filename+' snapshot changed'
    print(json.dumps({'status':'exactly recovered all four','pixel_mismatches':0,'all_png_bytes_equal':all_bytes,'crop_files_unchanged':True,'method_snapshot_preserved':True,'report':'result/qa/early_intermediate_provenance.md'},indent=2))

if __name__=='__main__':
    main()
