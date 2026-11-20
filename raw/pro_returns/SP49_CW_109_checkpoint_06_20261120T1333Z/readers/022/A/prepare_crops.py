from pathlib import Path
import json,subprocess
root=Path("work/readers/022/A")
source="source/SP49_CW_109_scans/H109-02_109_scan022.jpg"
for row in json.loads((root/"open_loci.json").read_text()):
 subprocess.run(["python","work/scripts/crop.py",source,str(root/"crops"/(row["id"]+".jpg")),*map(str,row["bbox"]),"--rotate",str(row["rotate"]),"--reason",row["reason"]],check=True)
