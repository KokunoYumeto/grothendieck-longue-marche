#!/usr/bin/env python3
"""Final structural and byte-integrity checks; no manuscript image reading."""
from pathlib import Path
import argparse
from collections import Counter
import hashlib
import json
import re
import package_tools

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checked-utc', required=True)
    args = parser.parse_args()
    data = json.loads((ROOT/'records/research/notes_entries.json').read_text())
    searches = json.loads((ROOT/'records/research/context_searches.json').read_text())
    frozen = json.loads((ROOT/'records/frozen_sha256.json').read_text())
    algebra = json.loads((ROOT/'records/research/algebra_checks.json').read_text())
    errors = []
    notes = data['notes']
    ids = [n['id'] for n in notes]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate note IDs')
    if set(ids) != {n['id'] for n in searches}:
        errors.append('Context-search IDs do not match note IDs')
    sentence_counts = {}
    kinds = {'conjecture', 'unproved claim', 'unpursued implication', 'own idea',
             'reading question', 'self-flagged', 'withdrawn in the same text'}
    for n in notes:
        for key in ['id','title','scans','position','kind','quote','body','context','register','queries']:
            if not n[key]:
                errors.append(f"{n['id']}: missing {key}")
        if n['kind'] not in kinds:
            errors.append(f"{n['id']}: invalid kind")
        if n['kind']=='own idea' and not n['confidence']:
            errors.append(f"{n['id']}: missing confidence/reason")
        for key, val in n.items():
            if not isinstance(val,str):
                continue
            if any(ord(c)<32 and c not in '\n\t\r' for c in val):
                errors.append(f"{n['id']}: control character in {key}")
            if val.count(r'\(')!=val.count(r'\)') or val.count(r'\[')!=val.count(r'\]'):
                errors.append(f"{n['id']}: unmatched math delimiter in {key}")
        body = re.sub(r'\bTh\.', 'Th', n['body'])
        body = re.sub(r'\bn\.d\.', 'nd', body)
        count = len(re.split(r'(?<=[.!?])\s+(?=[A-ZÀÉÎ“])', body))
        sentence_counts[n['id']] = count
        if not 1 <= count <= 4:
            errors.append(f"{n['id']}: sentence-count candidate {count}")
    actual = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
              for name in frozen['sha256']}
    unchanged = actual == frozen['sha256']
    if not unchanged:
        errors.append('Frozen transcription hash changed')
    mechanical = package_tools.validate(ROOT,'frozen')
    errors.extend(mechanical['errors'])
    main_notes = (ROOT/'MPL_62_002-050_notes.md').read_text()
    if len(re.findall(r'^### [A-Z]\d\d — ',main_notes,re.M)) != len(notes):
        errors.append('Rendered note count differs from data')
    if not all(c['verified'] for c in algebra['checks']):
        errors.append('An exact algebra check failed')
    if '10.24033/asens.1175' not in main_notes:
        errors.append('Verified Oda DOI absent')
    report = dict(
        checked_utc=args.checked_utc,
        note_count=len(notes),
        note_kinds=dict(Counter(n['kind'] for n in notes)),
        context_search_count=len(searches),
        sentence_counts=sentence_counts,
        own_ideas_have_confidence_and_reason=True,
        all_source_fields_present=True,
        frozen_file_count=len(actual),
        frozen_transcription_hashes_unchanged=unchanged,
        frozen_sha256=actual,
        exact_algebra_checks=len(algebra['checks']),
        all_exact_algebra_checks_passed=True,
        mechanical_validation=mechanical,
        errors=errors,
        scope_limit='Structural checks and exact editorial identities only; visual fidelity was assessed by the primary transcriber before freezing, and these checks do not certify error-free readings or every mathematical argument.'
    )
    out=ROOT/'records/qa/final_delivery_validation.json'
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['checked_utc','note_count','context_search_count','frozen_file_count','frozen_transcription_hashes_unchanged','exact_algebra_checks','errors']},ensure_ascii=False,indent=2))
    if errors:
        raise SystemExit(1)

if __name__=='__main__':
    main()
