#!/usr/bin/env python3
"""Verify frozen sources, bibliography annotations and the delivered PDF copy."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
frozen = json.loads((root / 'notes/checkpoint10_frozen_source_hashes.json').read_text())
changed = [p for p, digest in frozen.items()
           if hashlib.sha256((root / p).read_bytes()).hexdigest() != digest]
bib = (root / 'LM8_PUSH_references.bib').read_text()
blocks = [b for b in re.split(r'(?m)(?=^@)', bib) if b.strip()]
missing = [re.match(r'@\w+\{([^,]+)', b).group(1) for b in blocks
           if not re.search(r'\b(?:unverified|verified)\b', b, re.I)]
pdf_hash = hashlib.sha256((root / 'LM8_PUSH_paper.pdf').read_bytes()).hexdigest()
build_hash = hashlib.sha256((root / 'build/LM8_PUSH_paper.pdf').read_bytes()).hexdigest()
out = {
    'frozen_source_files': len(frozen),
    'changed_frozen_sources': changed,
    'bibliography_entries': len(blocks),
    'bibliography_without_verification_annotation': missing,
    'root_and_build_pdf_identical': pdf_hash == build_hash,
    'pdf_sha256': pdf_hash,
    'annotation_case': 'Case-insensitive; four existing annotations use Verified with initial capital.',
}
print(json.dumps(out, indent=2))
assert not changed and not missing and pdf_hash == build_hash
