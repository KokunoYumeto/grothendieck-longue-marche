"""Release two disposable restored trees, retaining all differing exact bytes."""
from pathlib import Path
import hashlib,json,shutil

HERE=Path(__file__).resolve().parent
TREE=HERE.parent/'LM7_FERMAT_TOWER'
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    archive=HERE/'released_extracts229';assert not archive.exists();archive.mkdir()
    records=[];total=0
    for name in ['fresh224_images','fresh229_binary']:
        root=HERE/name;assert root.is_dir()
        for p in sorted(root.rglob('*')):
            assert not p.is_symlink()
            if not p.is_file():continue
            relative=p.relative_to(root);b=p.read_bytes();ordinary=TREE/relative
            if ordinary.is_file() and ordinary.read_bytes()==b:
                retained=ordinary
            else:
                retained=archive/name/relative
                retained.parent.mkdir(parents=True,exist_ok=True);retained.write_bytes(b)
            assert retained.read_bytes()==b
            records.append({'original_path':str(p.relative_to(HERE)),
                            'retained_path':str(retained.relative_to(HERE.parent)),
                            'bytes':len(b),'sha256':sha(b)})
            total+=len(b)
        shutil.rmtree(root)
    result={'status':'PASS','released_bytes':total,'files_checked':len(records),
            'all_complete_bytes_retained':True,'records':records}
    (HERE/'released_extracts229.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

if __name__=='__main__':main()
