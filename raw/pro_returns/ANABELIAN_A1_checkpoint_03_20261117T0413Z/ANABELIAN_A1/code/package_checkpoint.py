"""Package all current deliverables and work records, without nested archives."""
from pathlib import Path
import hashlib,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
name=f"ANABELIAN_A1_checkpoint_{number:02d}.zip"
dest=root.parent/name
if dest.exists():raise SystemExit("Refusing to overwrite an existing checkpoint")
included=[];omitted=[]
for path in sorted(root.rglob("*")):
    if not path.is_file():continue
    rel=path.relative_to(root)
    if ("__pycache__" in rel.parts or path.suffix==".zip"
        or (rel.parts[0]=="sources" and path.suffix in (".pdf",".txt"))
        or (path.suffix==".pdf" and path.name!="ANABELIAN_A1_paper.pdf")):
        omitted.append(str(rel));continue
    included.append(path)
manifest={"files":[{"path":str(p.relative_to(root)),
                    "bytes":p.stat().st_size,
                    "sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in included],
          "omitted_reproducible_material":omitted,
          "note":"Source URLs/hashes and retrieval programs are included; supplied attachments are not duplicated."}
with zipfile.ZipFile(dest,"x",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in included:z.write(path,"ANABELIAN_A1/"+str(path.relative_to(root)))
    z.writestr("ANABELIAN_A1/checkpoint_manifest.json",json.dumps(manifest,indent=2)+"\n")
print(dest)
print("files",len(included),"bytes",dest.stat().st_size)
print("sha256",hashlib.sha256(dest.read_bytes()).hexdigest())

