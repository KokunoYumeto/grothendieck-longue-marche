#!/usr/bin/env python3
"""Read-only pending metadata-followup gate; never applies a correction."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

FOLLOWUPS = 'evidence/audit_metadata_followups.json'


def check_followups(output):
    root = Path(output).resolve()
    path = root
    for part in Path(FOLLOWUPS).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('Metadata followup paths cannot contain symlinks.')
    if not path.exists():
        return {'path': FOLLOWUPS, 'exists': False, 'sha256': None, 'entries': 0}
    if not path.is_file():
        raise ValueError('Metadata followups must be a regular file.')
    raw = path.read_bytes()
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate metadata-followup JSON field.')
            result[key] = value
        return result
    def nonfinite(value):
        raise ValueError('Non-finite metadata-followup JSON value.')
    value = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
    if isinstance(value, list):
        entries = value
    elif (isinstance(value, dict) and type(value.get('schema_version')) is int
          and value['schema_version'] == 1 and isinstance(value.get('entries'), list)):
        entries = value['entries']
    else:
        raise ValueError('Malformed metadata-followup schema.')
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get('id'), str) or not entry['id'].strip():
            raise ValueError('Metadata followup requires a nonempty id.')
        if entry['id'] in seen:
            raise ValueError('Duplicate metadata-followup id.')
        seen.add(entry['id'])
        if entry.get('status') == 'pending':
            raise ValueError('Pending metadata followup must be reconciled through explicit root audit history: ' + entry['id'])
        if entry.get('status') not in {'resolved', 'applied'} or entry.get('applied') is not True:
            raise ValueError('Metadata followup has an unresolved or invalid disposition: ' + entry['id'])
    return {'path': FOLLOWUPS, 'exists': True,
            'sha256': hashlib.sha256(raw).hexdigest(), 'entries': len(entries)}
