#!/usr/bin/env python3
"""Fresh-copy root replay of the genuine finite source and CM discrepancy family."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,time

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
DEST=ROOT/'notes/reproduced/eighth_hour_final'
LOCAL=DEST/'work'
files={
 'centralizer_code':['check_cap216_genuine_source.py','check_cap216_genuine_core.g'],
 'ghost_code':['check_main_mixed_capping.npz','check_cm_discrepancy_family.py',
               'check_main_normalizer_joint.npz','check_main_normalizer_joint.json'],
 'tower_code':['translation_quaternion_homology.npz','translation_quaternion_image.npz']}
for directory,names in files.items():
    (LOCAL/directory).mkdir(parents=True,exist_ok=True)
    for name in names:shutil.copy2(WORK/directory/name,LOCAL/directory/name)
runtime=ROOT.parent/'.gapruntime/root'
env=os.environ.copy()
env['LD_LIBRARY_PATH']=str(runtime/'usr/lib/x86_64-linux-gnu')+(':'+env['LD_LIBRARY_PATH'] if env.get('LD_LIBRARY_PATH') else '')
gap=[str(runtime/'usr/lib/x86_64-linux-gnu/gap/gap'),'-q','-b','-l',str(runtime/'usr/share/gap')]
jobs=[([sys.executable,str(LOCAL/'centralizer_code/check_cap216_genuine_source.py')],
       LOCAL/'centralizer_code/check_cap216_genuine_source.out'),
      (gap+[str(LOCAL/'centralizer_code/check_cap216_genuine_core.g')],
       LOCAL/'centralizer_code/check_cap216_genuine_core.out'),
      ([sys.executable,str(LOCAL/'ghost_code/check_cm_discrepancy_family.py')],
       LOCAL/'ghost_code/check_cm_discrepancy_family.out')]
records=[]
for command,output in jobs:
    start=time.monotonic()
    with output.open('w') as stream:
        result=subprocess.run(command,cwd=DEST,env=env,stdout=stream,stderr=subprocess.STDOUT)
    transcript=output.read_text()
    errors=[s for s in transcript.splitlines() if s.startswith(('Error,','Syntax error:'))]
    record={'program':Path(command[-1]).name,'exit':result.returncode,'gap_errors':len(errors),
            'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(Path(command[-1]).read_bytes()).hexdigest()}
    records.append(record)
    print(json.dumps(record),flush=True)
    print(transcript[-6000:],flush=True)
    assert result.returncode==0 and not errors
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS genuine finite joint source, exact signed frames, six CM lifts and all81 discrepancy classes.')
