"""Copy the completed exact-format programs and their actual records."""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
TREE=HERE.parent/'LM7_FERMAT_TOWER'
DEST=TREE/'code/root_archive_format'
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    rt=json.loads((HERE/'delta229_roundtrip.json').read_bytes())
    assert rt['status']=='PASS' and rt['all_whole_byte_equal']
    assert rt['negative_fixture_count']==16
    assert rt['source_sha256']==sha((TREE/'code/materialize_archive_files.py').read_bytes())
    names=['delta229_benchmark.json','delta229_roundtrip.json','released_extracts229.json',
           'delta229_restore.out','delta229_restore.err','delta229_verify.out','delta229_verify.err']
    for stem in ['benchmark_delta229','prepare_delta229','release_verified_extracts229','test_delta229']:
        for suffix in ['.py','.out','.err']:names.append(stem+suffix)
    files=[HERE/n for n in names]
    files+=sorted(p for p in (HERE/'released_extracts229').rglob('*') if p.is_file())
    records=[]
    for source in files:
        relative=source.relative_to(HERE);target=DEST/relative;data=source.read_bytes()
        assert not target.exists()
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        assert target.read_bytes()==data
        records.append({'source':str(source.relative_to(HERE.parent)),
                        'archive_path':str(target.relative_to(TREE)),
                        'bytes':len(data),'sha256':sha(data)})
    result={'status':'PASS','files':records,'count':len(records),
            'all_whole_bytes_equal':True,'restorer_sha256':rt['source_sha256']}
    (TREE/'ledger/archive_delta229_staging.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))

if __name__=='__main__':main()
