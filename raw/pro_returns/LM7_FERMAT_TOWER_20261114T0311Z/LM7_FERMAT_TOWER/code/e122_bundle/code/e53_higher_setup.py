from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
src=root.parent/'research_e119_continuation/inputs/e119_e53_genus_transition.bin'
dst=root/'inputs/e119_e53_genus_transition.bin'
shutil.copyfile(src,dst)
d={'status':'PASS','source':str(src),'target':'inputs/'+dst.name,
   'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
   'bytes':dst.stat().st_size,'scope':'Immutable exact certified lower E119 data, unchanged in amended E121.'}
(root/'inputs/manifest.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
