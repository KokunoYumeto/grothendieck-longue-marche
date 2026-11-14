from pathlib import Path
from datetime import datetime,timezone
import zipfile,sys
root=Path(__file__).resolve().parents[1]
name="MPL_156-1+156-2"
pages=sorted((root/"pages").glob("*.tex"))
(root/f"{name}_transcription.tex").write_text("\n".join(p.read_text(encoding="utf-8").rstrip()+"\n" for p in pages),encoding="utf-8")
tag=sys.argv[1] if len(sys.argv)>1 else "final"
out=root.parent/(f"{name}.zip" if tag=="final" else f"{name}_checkpoint_{tag}.zip")
with (root/"progress.log").open("a") as f:
    f.write(f"checkpoint assembled {tag} {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ({len(pages)} pages)\n")
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts:
            z.write(p,p.relative_to(root))
print(out.resolve())
print(f"{len(pages)} page files; {out.stat().st_size} bytes")

