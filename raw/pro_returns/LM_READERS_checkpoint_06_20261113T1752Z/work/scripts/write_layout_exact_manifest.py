"""Emit exact scan-local net patches against the mechanically repaired source.

The main edition uses the same mechanical-repair -> local-layout order. This
manifest supplies independently replayable text patches, SHA-256 digests,
expected literal-match counts, and both raw-source and input-stage offsets.
"""
from pathlib import Path
from hashlib import sha256
import json,re
import mechanical_repairs
from layout_repairs import repair,COVERAGE,_scan_ranges

ROOT=Path(__file__).resolve().parents[2]

def digest(text):return sha256(text.encode('utf-8')).hexdigest()

def apply_exact(text,patches):
    for patch in reversed(patches):
        a,b=patch['input_offset_start'],patch['input_offset_end']
        assert text[a:b]==patch['old'],patch['id']
        assert text.count(patch['old'])==patch['expected_match_count'],patch['id']
        text=text[:a]+patch['new']+text[b:]
    return text

def main():
    entries=[];count=0
    for language,folder,suffix in [('fr','fr/texts',''),('en','en/packages','_en')]:
        for package in COVERAGE:
            source=Path('sources')/folder/(package+suffix+'.tex')
            source_bytes=(ROOT/source).read_bytes()
            raw=source_bytes.decode('utf-8')
            input_text=(ROOT/source).read_text()
            initial,_=mechanical_repairs.repair(input_text,package,language)
            final,records=repair(initial,package,language)
            if initial==final:continue
            original_scans={n:(a,b,raw[a:b]) for n,a,b in _scan_ranges(raw)}
            final_scans={n:final[a:b] for n,a,b in _scan_ranges(final)}
            patches=[]
            for scan,a,b in _scan_ranges(initial):
                old,new=initial[a:b],final_scans[scan]
                if old==new:continue
                oa,ob,source_old=original_scans[scan]
                local=[r for r in records if r['scan']==scan]
                patches.append(dict(id=f"{COVERAGE[package]['cote']}-{scan}-layout",
                    cote=COVERAGE[package]['cote'],scan=scan,source_line=raw[:oa].count('\n')+1,
                    source_offset_start=oa,source_offset_end=ob,
                    source_byte_start=len(raw[:oa].encode('utf-8')),source_byte_end=len(raw[:ob].encode('utf-8')),
                    input_offset_start=a,input_offset_end=b,expected_match_count=1,
                    repair_ids=[r['id'] for r in local],source_old=source_old,old=old,new=new))
            assert apply_exact(initial,patches)==final,(package,language)
            entries.append(dict(package=package,language=language,source_path=source.relative_to('sources').as_posix(),
                source_sha256=sha256(source_bytes).hexdigest(),input_sha256=digest(initial),output_sha256=digest(final),
                patches=patches,records=records))
            count+=len(patches)
    manifest=dict(schema='local-layout-exact-patches-v1',offset_convention='zero-based, end-exclusive Unicode characters; source_byte_* use UTF-8',
        input_stage='mechanical_repairs.repair output, before editorial annotation',packages=entries)
    path=ROOT/'work/data/layout_exact_patches.json'
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(entries)} language/package entries; {count} exact scan-local net patches; every patch replayed exactly')

if __name__=='__main__':main()
