#!/usr/bin/env python3
"""Record the scope of this audit's source verification in every bib note."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "notes/local_agent_references.bib"
text = path.read_text()
unverified = {
    "AgentPorowskiFamilies": "Unverified for the cited full-text corollary; only metadata and abstract were retrieved. ",
}

def mark(match):
    entry = match.group(0)
    key = re.match(r"@\w+\{([^,]+),", entry).group(1)
    prefix = unverified.get(key, "Verified at the exact source passages described below. ")
    note = re.search(r"note\s*=\s*\{", entry)
    if note is None:
        raise RuntimeError(f"Missing note in {key}")
    old = entry[note.end():]
    if not old.lower().startswith(("verified", "unverified")):
        entry = entry[:note.end()] + prefix + old
    print(f"{key}: {'unverified' if key in unverified else 'verified'}")
    return entry

result, count = re.subn(r"@\w+\{[^\n]+[\s\S]*?\n\}", mark, text)
assert count >= 16, count
path.write_text(result)
print(f"Annotated {count} bibliography entries.")
