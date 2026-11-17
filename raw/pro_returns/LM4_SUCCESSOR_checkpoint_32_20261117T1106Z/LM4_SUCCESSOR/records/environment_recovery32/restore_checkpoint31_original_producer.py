from pathlib import Path
import os, zipfile, subprocess, json, time
base=Path('/workspace/scratch/a50d05093ca1')
archive=base/'recovered_inputs32/LM4_SUCCESSOR_checkpoint_31.zip'
project=base/'LM4_SUCCESSOR'
assert not project.exists(), 'Refuse to overwrite an existing project'
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert all(n.startswith('LM4_SUCCESSOR/') and '..' not in Path(n).parts for n in names)
    z.extractall(base)
print('Restored direct ZIP members',len(names),flush=True)
for name in ['verification_images.tar','historical_documents.tar','historical_data.tar']:
    path=project/name
    result=subprocess.run(['tar','-xf',str(path),'-C',str(base)],capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(name+': '+result.stderr)
    print('Restored standard TAR',name,flush=True)
target=base/'LM4_SUCCESSOR_checkpoint_31.zip'
assert not target.exists()
os.link(archive,target)
record={'archive_bytes':526709584,'archive_sha256':'98f1a6b74ae43dc4d09a1177a79c5e149fdf7530df52bc593964778172611d41','direct_members':len(names),'restored_project':str(project),'three_system_tar_extractions_exit_zero':True,'new_zip_created':False,'checkpoint32_not_created':True}
(project/'records/environment_recovery32').mkdir(parents=True,exist_ok=True)
(project/'records/environment_recovery32/checkpoint31_restore_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
