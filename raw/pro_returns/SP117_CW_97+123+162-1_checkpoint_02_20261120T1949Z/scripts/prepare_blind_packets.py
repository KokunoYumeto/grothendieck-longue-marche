"""Build image-only packets, and refuse to run before all first passes exist."""
from pathlib import Path
import json
import shutil

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
order = json.loads((OUT / "work/page_order.json").read_text())
pages = [Path(row["codex_file"]).stem for row in order]
missing = [page for page in pages if not (OUT / "work" / f"{page}_decided.json").exists()]
if missing:
    raise SystemExit("First pass incomplete: " + ", ".join(missing))
for page in pages:
    packet = ROOT / "blind" / page
    packet.mkdir(parents=True, exist_ok=True)
    source = ROOT / "packets" / page / "whole.jpg"
    if not source.exists():
        alternatives = list((ROOT / "packets" / page).glob(page + ".jpg"))
        if len(alternatives) != 1:
            raise FileNotFoundError(source)
        source = alternatives[0]
    link = packet / "image.jpg"
    if not link.exists():
        link.symlink_to(source.resolve())
    shutil.copyfile(OUT / "second" / f"{page}_boxes.tsv", packet / "boxes.tsv")
    shutil.copyfile(ROOT / "packets/CONVENTIONS.md", packet / "CONVENTIONS.md")
print(f"Prepared {len(pages)} image-only packets; no witness or first reading copied.")
