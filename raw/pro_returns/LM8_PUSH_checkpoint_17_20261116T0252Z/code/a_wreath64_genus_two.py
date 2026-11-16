"""Read-only run() aggregating the three exact actual-cover certificates."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile


def run():
    root = Path(__file__).resolve().parents[1]
    names = ("frontier", "map", "prym")
    rows = []
    with tempfile.TemporaryDirectory(prefix="fgh_A80_replay_", dir=root / "notes") as tmp:
        for name in names:
            source = root / f"code/a_wreath64_{name}.py"
            copy = Path(tmp) / source.name
            copy.write_bytes(source.read_bytes())
            process = subprocess.run([sys.executable, str(copy)], check=True,
                                     text=True, capture_output=True, cwd=root)
            assert not process.stderr
            actual = json.loads(copy.with_suffix(".json").read_text())
            original = json.loads(source.with_suffix(".json").read_text())
            assert actual == original
            assert json.loads(process.stdout) == original
            rows.append({"name": name,
                         "source": str(source.relative_to(root)),
                         "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                         "original_json_sha256": hashlib.sha256(source.with_suffix(".json").read_bytes()).hexdigest(),
                         "whole_json_equal": True,
                         "result": actual})
    return {"status": "PASS", "candidate": "A.80",
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "certificates": rows,
            "scope": "Actual finite group, curve/isogeny/Prym identities and complete ordinary point counts. Stable geometry and unbounded partial-distance kernel are proved in the draft, not inferred from finite computations."}


if __name__ == "__main__":
    result = run()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
