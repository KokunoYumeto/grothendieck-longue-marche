"""One distribution policy shared by checkpoint and final-package builders."""
from pathlib import Path


def exclusion_reason(root: Path, path: Path):
    rel = path.relative_to(root)
    if '__pycache__' in rel.parts:
        return 'Regenerable Python bytecode cache.'
    if rel.parts[0] == 'notes' and path.suffix in {'.pdf', '.txt'}:
        return ('Externally retrieved primary reading material; source URL, exact '
                'theorem use and verification record are retained instead of the full article.')
    if rel.parts[0] == 'source_checks' and path.suffix in {'.pdf', '.png'}:
        return ('Externally retrieved original manuscript image; the page concordance, '
                'source URL, extraction code and SHA-256 manifest are retained.')
    if path.suffix in {'.aux', '.toc', '.bbl', '.blg'}:
        return 'Regenerable TeX build intermediate; source and final build log retained.'
    if len(rel.parts) == 1 and path.suffix in {'.log', '.out'}:
        return 'Regenerable TeX build intermediate; final build log retained in audit/.'
    return None


def distribution_files(root: Path):
    return [p for p in sorted(root.rglob('*'))
            if p.is_file() and exclusion_reason(root, p) is None]
