from pathlib import Path
import subprocess, json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/008/A'
for name,bbox,rotation,purpose in json.loads((out/'crop_plan.json').read_text()):
    subprocess.run(['python',str(root/'out/scripts/crop.py'),str(root/'source/SP40_CW_81_scans/J81-01_81_scan008.jpg'),str(out/name),*map(str,bbox),'--rotate',str(rotation),'--width','2800'],check=True)
