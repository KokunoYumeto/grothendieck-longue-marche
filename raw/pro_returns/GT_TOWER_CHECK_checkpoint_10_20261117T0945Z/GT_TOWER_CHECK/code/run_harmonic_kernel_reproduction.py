#!/usr/bin/env python3
"""Root replay of the literal full finite frame and source A4 witness."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work/centralizer_code'
DEST=ROOT/'notes/reproduced/harmonic_kernel'
LOCAL=DEST/'work/centralizer_code'
LOCAL.mkdir(parents=True,exist_ok=True)
for name in ('check_central_certificate_replay.g','check_source_centralizer_affine.g',
             'check_source_affine_brunnian.py'):
    shutil.copy2(WORK/name,LOCAL/name)
runtime=ROOT.parent/'.gapruntime/root'
env=os.environ.copy()
env['LD_LIBRARY_PATH']=str(runtime/'usr/lib/x86_64-linux-gnu')+(':'+env['LD_LIBRARY_PATH'] if env.get('LD_LIBRARY_PATH') else '')
gap=[str(runtime/'usr/lib/x86_64-linux-gnu/gap/gap'),'-q','-b','-l',str(runtime/'usr/share/gap')]
jobs=[(gap+[str(LOCAL/'check_source_centralizer_affine.g')],LOCAL/'check_source_centralizer_affine.out'),
      ([sys.executable,str(LOCAL/'check_source_affine_brunnian.py')],LOCAL/'check_source_affine_brunnian.out')]
records=[]
for command,output in jobs:
    start=time.monotonic()
    with output.open('w') as f:
        result=subprocess.run(command,cwd=DEST,env=env,stdout=f,stderr=subprocess.STDOUT)
    transcript=output.read_text()
    errors=[s for s in transcript.splitlines() if s.startswith(('Error,','Syntax error:'))]
    record={'program':Path(command[-1]).name,'exit':result.returncode,'gap_errors':len(errors),
            'seconds':round(time.monotonic()-start,3),
            'source_sha256':hashlib.sha256(Path(command[-1]).read_bytes()).hexdigest()}
    records.append(record);print(json.dumps(record),flush=True);print(transcript[-5000:],flush=True)
    assert result.returncode==0 and not errors
(DEST/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS full finite frame, literal source A4 morphism and all normalized source cocycles.')
