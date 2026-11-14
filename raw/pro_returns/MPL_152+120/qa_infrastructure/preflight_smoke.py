#!/usr/bin/env python3
"""Exercise structural guards on an isolated synthetic 38-page fixture only."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main() -> None:
    script = Path(__file__).resolve().with_name("preflight.py")
    spec = importlib.util.spec_from_file_location("preflight_synthetic_test", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix="preflight-fixture-") as temporary:
        root = Path(temporary)
        (root / "pages").mkdir()
        originals = {}
        rows = []
        for cote, scan, name in module.PAGES:
            content = (f"\\cotefile{{{cote}}}\n" if scan == 1 else "")
            content += f"\\scanpage{{{scan}}}\n"
            content += "% ignored marker: \\scanpage{999} and unmatched {\n"
            content += r"Escaped \{ \} \% and \verb|{ % }|." + "\n"
            content += r"\unsure{test} \illegible{1}" + "\n"
            content += r"\diagram{\begin{tikzcd} A \arrow[r] & B \end{tikzcd}}" + "\n"
            path = root / "pages" / name
            path.write_text(content, encoding="utf-8")
            originals[path] = content.encode("utf-8")
            rows.append([str(cote), str(scan), "text", "1", "text", "top", "Synthetic", "yes"])

        def write_inventory(data):
            with (root / module.INVENTORY).open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(module.COLUMNS)
                writer.writerows(data)

        def invoke(command, succeeds=True):
            result = subprocess.run([sys.executable, str(script), command, "--root", str(root)],
                                    text=True, capture_output=True)
            report = json.loads(result.stdout)
            assert (result.returncode == 0) == succeeds, (command, report)
            return report

        write_inventory(rows)
        checked = invoke("check")
        assert checked["macro_totals"]["unsure"] == 38
        assert checked["macro_totals"]["illegible"] == 38
        invoke("build")
        invoke("manifest")
        invoke("verify")
        assert all(path.read_bytes() == data for path, data in originals.items())
        print("PASS: 38 expected pages, comment/escape handling, counts, inventory, build, 39 hashes, input immutability")

        path = next(iter(originals))
        path.write_bytes(originals[path] + b"% synthetic edit\n")
        changed = invoke("verify", succeeds=False)
        assert any("SHA-256 mismatch" in issue for issue in changed["errors"])
        path.write_bytes(originals[path])
        print("PASS: manifest detects a source-byte change")

        path.write_bytes(originals[path] + b"\\begin{equation}\nx}\n")
        broken = invoke("check", succeeds=False)
        assert any("Closing brace" in issue for issue in broken["errors"])
        assert any("Unclosed environment" in issue for issue in broken["errors"])
        path.write_bytes(originals[path])
        print("PASS: unmatched braces and environments are detected")

        wrong_rows = [list(row) for row in rows[:-1]] + [list(rows[0])]
        wrong_rows[0][-1] = "no"
        write_inventory(wrong_rows)
        broken = invoke("check", succeeds=False)
        assert any("duplicate" in issue for issue in broken["errors"])
        assert any("no rows" in issue for issue in broken["errors"])
        assert any("not yes" in issue for issue in broken["errors"])
        write_inventory(rows)
        print("PASS: duplicate inventory IDs, missing page coverage, and non-yes rows are detected")

        moved = path.with_name("unexpected.tex")
        path.rename(moved)
        broken = invoke("check", succeeds=False)
        assert any("Missing page file" in issue for issue in broken["errors"])
        assert any("Unexpected page file" in issue for issue in broken["errors"])
        moved.rename(path)
        invoke("verify")
        print("PASS: exact filename set is enforced; restored fixture verifies")
    print("All tests used synthetic data in a temporary directory; the active manuscript was not opened.")


if __name__ == "__main__":
    main()
