"""One-use root-approved evidence-coordinate correction, with no new reading.

The independently frozen neutral rectangle remains unchanged.  The root's
supplementary017 evidence image has a separately documented original rectangle;
only that rectangle in the adjudication metadata is corrected here.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import csv
import hashlib
import io
import json

from validate_audit_integrity import load_crop_rectangles, validate

R = Path(__file__).resolve().parents[1]
LOG = R / 'documentation/adjudication_crop_coordinate_correction.json'
assert not LOG.exists()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def records(data):
    return list(csv.DictReader(io.StringIO(data.decode()), delimiter='\t'))


protected = {}
for suffix in ('boxes.tsv', 'first.tsv', 'second.tsv', 'comparison_provenance.json',
               'token_differences.tsv', 'second_notes.md'):
    for p in (R / 'second').glob('*_' + suffix):
        protected[str(p.relative_to(R))] = digest(p)
for name in ('pages/149_scan017.tex', 'reviews/149_scan017.json',
             'documentation/149_scan017_audit_choices.json'):
    protected[name] = digest(R / name)
path = R / 'second/149_scan017_adjudications.tsv'
before_bytes = path.read_bytes()
before = records(before_bytes)
item = next(x for x in before if x['box'] == 'b11')
old, new = '(1070, 1892, 1633, 2056)', '(1325, 1850, 1640, 2000)'
assert item['pixel_box'] == old
assert item['crop'] == 'crops/149_scan017_audit_b11_full.png'
known = load_crop_rectangles(R)
assert known[item['crop']] == ast.literal_eval(new)
assert before_bytes.count(old.encode()) == 1
after_bytes = before_bytes.replace(old.encode(), new.encode(), 1)
after = records(after_bytes)
for left, right in zip(before, after):
    if left['box'] == 'b11':
        assert {k: v for k, v in left.items() if k != 'pixel_box'} == {k: v for k, v in right.items() if k != 'pixel_box'}
    else:
        assert left == right
path.write_bytes(after_bytes)
assert all(digest(R / p) == h for p, h in protected.items())

overrides = []
for p in sorted((R / 'second').glob('*_adjudications.tsv')):
    stem = p.name.removesuffix('_adjudications.tsv')
    for row in records(p.read_bytes()):
        default = f"crops/{stem}_second_{row['box']}.png"
        if row['crop'] != default:
            rectangle = tuple(ast.literal_eval(row['pixel_box']))
            assert row['crop'] in known, row['crop']
            assert rectangle == known[row['crop']], row['crop']
            overrides.append(dict(page=stem, box=row['box'], crop=row['crop'],
                                  recorded_rectangle=list(rectangle),
                                  manifest_rectangle=list(known[row['crop']]), status='matches'))
validation = validate(R)
assert validation['status'] == 'passed', validation
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root explicitly approved coordinate-only017b11 correction, helper pixel_box overrides, and manifest-based validation; no source reading changes.',
           file=str(path.relative_to(R)), box='b11', crop=item['crop'],
           field='pixel_box', before=old, after=new,
           evidence='documentation/audit_scope_crops.tsv records the supplementary source rectangle; reviews/149_scan017.json c09 agrees. The old value is the preserved neutral b11 rectangle, not the selected supplementary evidence image extent.',
           before_sha256=hashlib.sha256(before_bytes).hexdigest(), after_sha256=digest(path),
           previously_observed_negative_gate='The new read-only validator rejected017b11 with the exact old/new rectangle mismatch before this correction; all other completed audits and mapped crop overrides passed.',
           other_fields_byte_preserved=True, protected_hashes=protected,
           protected_files_unchanged=True, readings_flags_counts_unchanged=True,
           crop_overrides_checked=overrides, validation_after=validation,
           script_hashes={str(p.relative_to(R)):digest(p) for p in [R/'scripts/write_adjudications.py', R/'scripts/validate_audit_integrity.py']},
           no_assembly=True)
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
md = ('# Adjudication evidence-coordinate correction\n\n' + log['completed_utc'] + '\n\n'
      'The main reader approved this metadata-only correction after the read-only checklist identified a mismatch.\n\n'
      '- Record: `second/149_scan017_adjudications.tsv`, b11.\n'
      '- Evidence image: `crops/149_scan017_audit_b11_full.png`.\n'
      '- Historical incorrect evidence rectangle: `(1070,1892,1633,2056)` (the original neutral box).\n'
      '- Current correct evidence rectangle: `(1325,1850,1640,2000)`, from `documentation/audit_scope_crops.tsv` and the current c09 report.\n\n'
      'Only the coordinate string changed in the adjudication TSV. All reading fields, evidence prose, flags, page text, report counts, neutral box coordinates, first/second readings and comparison inputs remain unchanged. The log preserves both values and file hashes. No aggregate assembly was run.\n\n'
      'The helper now accepts an explicit `pixel_box` choice and checks it against known manifests. The read-only validator uses direct original-coordinate manifests, recorded supplements and explicit full-extent derivation links; it does not infer coordinates from file names. Rotation-only evidence retains the original source rectangle. All existing crop overrides were checked; their exact comparisons are in the JSON log.\n')
LOG.with_suffix('.md').write_text(md)
print(json.dumps({'correction': '017b11 pixel_box only', 'overrides_checked':len(overrides),
                  'evidence_rectangles_verified':validation['evidence_rectangles_verified'],
                  'unmapped_evidence_crops':validation['unmapped_evidence_crops'],
                  'frozen_inputs_unchanged':True}))
