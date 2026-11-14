#!/usr/bin/env python3
"""Run the exact image-alias round trip on the complete saved224 ZIP."""
from pathlib import Path
import hashlib,importlib.util,json,shutil,subprocess,sys,zipfile

A=Path(__file__).resolve().parent;W=A.parent
source=W/'LM7_FERMAT_TOWER.zip'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='710655b94beb024bcb3c281c60633446be8652d2a6d9467b6bb30719a2d0a645'
spec=importlib.util.spec_from_file_location('image_aliases',A/'materialize_archive_images.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
fresh=A/'fresh224_images';assert not fresh.exists();fresh.mkdir()
with zipfile.ZipFile(source) as z:
    prefix='LM7_FERMAT_TOWER/'
    images={n[len(prefix):]:z.read(n) for n in z.namelist()
            if Path(n).suffix.lower() in {'.jpg','.jpeg','.png'} and '/qa/' in n}
    plan=mod.plan_image_aliases(images,224)
    aliases={r['path']:r['storage_path'] for r in plan['aliases']}
    stored={n:b for n,b in images.items() if n not in aliases}
    saved_compressed=sum(z.getinfo(prefix+n).compress_size for n in aliases)
for name,data in stored.items():
    p=fresh/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
(fresh/'ledger').mkdir(exist_ok=True)
text=json.dumps(plan,indent=2)+'\n'
(fresh/'ledger/archive_image_aliases.json').write_text(text)
(A/'image_alias_plan224.json').write_text(text)
with (A/'materialize_archive_images.out').open('wb') as out,(A/'materialize_archive_images.err').open('wb') as err:
    run=subprocess.run([sys.executable,str(A/'materialize_archive_images.py'),'--root',str(fresh)],stdout=out,stderr=err)
assert run.returncode==0 and not (A/'materialize_archive_images.err').read_bytes()
created=json.loads((A/'materialize_archive_images.out').read_text())
assert created['exact_images_created']==len(aliases)
checks=[]
for name,data in sorted(images.items()):
    assert (fresh/name).read_bytes()==data,name
    checks.append({'path':name,'bytes':len(data),'sha256':mod.sha(data),'storage_path':aliases.get(name,name)})
again=mod.materialize(fresh,verify_only=True)
assert again['exact_images_created']==0
result={'status':'PASS','source_archive_sha256':mod.sha(source.read_bytes()),
        'logical_image_count':len(images),'stored_image_count':len(stored),'alias_count':len(aliases),
        'exact_prior_compressed_bytes_saved':saved_compressed,
        'all_logical_image_bytes_reconstructed_identically':True,
        'materializer_exit_code':run.returncode,'repeat_verify':again,
        'image_checks':checks}
(A/'image_roundtrip224.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='image_checks'},indent=2))
