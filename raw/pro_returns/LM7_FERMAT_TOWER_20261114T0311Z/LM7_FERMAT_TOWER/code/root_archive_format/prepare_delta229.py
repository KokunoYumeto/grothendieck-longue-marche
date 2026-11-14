"""Preserve the previous format, then install exactly reversible binary deltas."""
from pathlib import Path
import hashlib,json,os,shutil

ROOT=Path(__file__).resolve().parent.parent
TREE=ROOT/'LM7_FERMAT_TOWER'
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    history=TREE/'code/packaging229_history/before_binary_deltas'
    assert not history.exists()
    history.mkdir(parents=True)
    pairs=[(TREE/'code/package.py','package.py'),
           (ROOT/'root_package229.out','package.out'),
           (ROOT/'root_package229.err','package.err'),
           (TREE/'code/package.out','internal_package.out'),
           (TREE/'code/materialize_archive_files.py','materialize_archive_files.py'),
           (TREE/'code/materialize_archive_files.out','materialize_archive_files.out'),
           (TREE/'code/ARCHIVE_README.md','ARCHIVE_README.md'),
           (TREE/'LM7_FERMAT_TOWER_manifest.json','manifest.json')]
    saved=[]
    for source,name in pairs:
        data=source.read_bytes();target=history/name;target.write_bytes(data)
        assert target.read_bytes()==data
        saved.append({'original_path':str(source.relative_to(ROOT)),
                      'history_path':str(target.relative_to(TREE)),
                      'bytes':len(data),'sha256':sha(data)})
    for suffix in ['.err','_status.json']:
        source=TREE/'code'/('materialize_archive_files'+suffix)
        if source.exists():
            data=source.read_bytes();target=history/source.name;target.write_bytes(data)
            saved.append({'original_path':str(source.relative_to(ROOT)),
                          'history_path':str(target.relative_to(TREE)),
                          'bytes':len(data),'sha256':sha(data)})
    benchmark=json.loads((HERE/'delta229_benchmark.json').read_bytes())
    archive=ROOT/'LM7_FERMAT_TOWER.zip'
    assert sha(archive.read_bytes())==benchmark['source_archive_sha256']
    assert benchmark['status']=='PASS' and benchmark['all_whole_byte_roundtrips_passed']
    rows=[];dest=TREE/'archive_data/binary_deltas';dest.mkdir(parents=True,exist_ok=True)
    for r in benchmark['records']:
        assert r['whole_target_roundtrip_equal'] and r['delta_codec_roundtrip_equal']
        target=(TREE/r['path']).read_bytes();base=(TREE/r['base_path']).read_bytes()
        delta=(HERE/r['delta_path']).read_bytes()
        assert len(target)==r['bytes'] and sha(target)==r['sha256']
        assert len(base)==r['base_bytes'] and sha(base)==r['base_sha256']
        assert len(delta)==r['delta_bytes']==len(target) and sha(delta)==r['delta_sha256']
        assert base
        repeated=(base*((len(delta)+len(base)-1)//len(base)))[:len(delta)]
        recovered=(int.from_bytes(delta,'little')^int.from_bytes(repeated,'little')).to_bytes(len(delta),'little')
        assert recovered==target
        dp=dest/(r['delta_sha256']+'.xor')
        assert not dp.exists()
        os.link(HERE/r['delta_path'],dp)
        assert dp.read_bytes()==delta
        rows.append({k:r[k] for k in ['path','base_path','bytes','sha256','base_bytes','base_sha256','delta_bytes','delta_sha256']}|
                    {'delta_path':str(dp.relative_to(TREE)),
                     'encoding':'xor-repeated-base-v1'})
    names={r['path'] for r in rows};assert len(names)==len(rows)
    assert all(r['base_path'] not in names for r in rows)
    plan={'format_version':1,'encoding':'xor-repeated-base-v1',
          'definition':'For target length n and nonempty complete base b, d[i] = target[i] XOR b[i modulo len(b)], for 0 <= i < n. Recovery applies the same XOR. No numeric or object serialization is performed.',
          'source_archive_sha256':benchmark['source_archive_sha256'],
          'benchmark_sha256':sha((HERE/'delta229_benchmark.json').read_bytes()),
          'deltas':sorted(rows,key=lambda r:r['path'])}
    planpath=TREE/'ledger/archive_binary_deltas.json'
    assert not planpath.exists();planpath.write_text(json.dumps(plan,indent=2)+'\n')
    record={'status':'PASS','source_archive_bytes':archive.stat().st_size,
            'source_archive_sha256':benchmark['source_archive_sha256'],
            'source_archive_original_size_exceeds_transfer_limit':True,
            'preserved_format_files':saved,'delta_count':len(rows),
            'every_delta_target_whole_byte_equal':True,
            'no_delta_chains':True,'no_original_files_changed':True,
            'plan_sha256':sha(planpath.read_bytes())}
    (history/'preservation.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
