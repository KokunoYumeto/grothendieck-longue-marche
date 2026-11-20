"""Exact, reviewed aliases for other_errors.tsv; no reading inference.

All four serialized TSV fields form an identity. No whitespace, place, scan,
or reading similarity is used. Raw submitted reports are never modified.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

FIELDS = ('scan', 'place', 'the reading', 'what the ink shows')


def exact_row(raw):
    if not isinstance(raw, dict) or set(raw) != set(FIELDS):
        raise ValueError('Other-error row must have exactly the four TSV fields')
    if any(not isinstance(raw[field], str) for field in FIELDS):
        raise ValueError('Other-error identity requires serialized string fields')
    return {field: raw[field] for field in FIELDS}


def row_key(raw):
    row = exact_row(raw)
    return tuple(row[field] for field in FIELDS)


def row_sha256(raw):
    encoded = json.dumps(row_key(raw), ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


class ErrorAliases:
    def __init__(self, registry):
        if registry.get('schema_version') != 1 or registry.get('fields') != list(FIELDS):
            raise ValueError('Unsupported other-error alias registry schema')
        self.by_hash = {}
        canonical_hashes, ids = set(), set()
        for entry in registry['aliases']:
            if not isinstance(entry.get('id'), str) or not entry['id'] or entry['id'] in ids:
                raise ValueError('Each alias must have a unique nonempty ID')
            ids.add(entry['id'])
            alias, canonical = exact_row(entry['alias']), exact_row(entry['canonical'])
            ah, ch = row_sha256(alias), row_sha256(canonical)
            if ah != entry['alias_sha256'] or ch != entry['canonical_sha256']:
                raise ValueError(f"Alias {entry['id']}: full-row SHA-256 mismatch")
            if ah == ch or alias['scan'] != canonical['scan']:
                raise ValueError(f"Alias {entry['id']}: self-alias or cross-scan alias")
            if ah in self.by_hash:
                raise ValueError('An exact alias row is registered more than once')
            self.by_hash[ah] = (alias, canonical)
            canonical_hashes.add(ch)
        if canonical_hashes & self.by_hash.keys():
            raise ValueError('Alias chains and cycles are forbidden; target a final canonical row')

    @classmethod
    def load(cls, path: Path):
        # Required after installation: silently losing the registry would allow
        # old peer reports to reintroduce aliases on a later import.
        return cls(json.loads(path.read_text(encoding='utf-8')))

    def canonical(self, raw):
        row = exact_row(raw)
        pair = self.by_hash.get(row_sha256(row))
        if pair is None:
            return row
        alias, canonical = pair
        if row != alias:
            raise ValueError('SHA-256 collision: full row does not match its registered alias')
        return dict(canonical)

    def normalize(self, rows):
        result, seen = [], set()
        for raw in rows:
            row = self.canonical(raw)
            key = row_key(row)
            if key not in seen:
                result.append(row)
                seen.add(key)
        return result

    def assert_canonical(self, rows):
        if self.normalize(rows) != rows:
            raise ValueError('other_errors.tsv contains aliases or exact duplicates; apply an audited normalization first')

    def append(self, existing, incoming):
        # Existing-table changes require their own explicit audit transaction.
        # New submissions may be canonicalized without rewriting their reports.
        self.assert_canonical(existing)
        return self.normalize([*existing, *incoming])
