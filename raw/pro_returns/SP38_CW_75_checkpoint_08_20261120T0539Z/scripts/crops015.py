from pathlib import Path
import json,subprocess
from datetime import datetime,timezone
o=Path(__file__).resolve().parents[1]
source=o.parent/'source/SP38_CW_75_scans/J75-02_75_scan015.jpg'
items=[
('01_equal_length',[1000,437,1210,530],'H has même where C and all readers report equals; no reader crop covers the sign.'),
('02_resp',[1390,812,1650,920],'Parenthetic resp is at the preceding line end; reader isom crops cover only its continuation.'),
('03_tt_isom',[1200,998,1635,1112],'H substitutes la donnée; this phrase was half-settled and has no reader crop.'),
('04_comb',[245,1106,520,1200],'H expands comb; no supplied reader crop covers this half-settled contraction.'),
('05_montrer',[1070,1190,1410,1310],'H leaves the canceled words illegible; no reader crop covers this right-hand locus.'),
('06_vectorielle',[1190,1298,1575,1389],'H convexe versus C/readers vectorielle; no reader crop covers this phrase.'),
('07_grace_centre',[266,1390,705,1500],'H rearranges grâce : centre de; this previously half-settled left span is outside the insertion crops.'),
('08_cor_polygone',[1110,1377,1660,1490],'H lacks the local accent in the Cor noun; no reader crop covers the complete noun.'),
('09_orientation_tail',[720,1485,1655,1620],'The beginning Orientation du is already visible in the final-cancellation crop; this missing continuation resolves H plural and checks the correspondence.'),
]
manifest=[]
for name,box,reason in items:
    dst=o/'crops/scan015'/f'{name}.png'
    if dst.exists():raise RuntimeError('No overwrite or recrop: '+str(dst))
    subprocess.run(['python3',str(o/'scripts/crop.py'),str(source),str(dst),*map(str,box),'--width','2800'],check=True,capture_output=True,text=True)
    manifest.append(dict(path=str(dst.relative_to(o)),bbox=box,reason=reason,rotation_degrees=0))
(o/'decisions/scan015_new_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print({'created':len(manifest),'utc':datetime.now(timezone.utc).isoformat()})
