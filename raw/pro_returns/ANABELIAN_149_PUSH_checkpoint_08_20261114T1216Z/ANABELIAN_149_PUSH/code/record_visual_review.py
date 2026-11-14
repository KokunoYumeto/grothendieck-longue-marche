#!/usr/bin/env python3
"""Record an actually completed manual review; never perform or infer it.

The reviewer must inspect every rendered contact sheet and the named full-size
pages before invoking this script. The automatic audit deliberately retains its
unreviewed status; this separate, hash-bound record states the human/model review.
"""
from pathlib import Path
import argparse
import hashlib
import json

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--all-rendered-inspected', action='store_true', required=True)
parser.add_argument('--full-resolution', required=True)
parser.add_argument('--notes', required=True)
args = parser.parse_args()
data = json.loads((root/'code/PDF_layout_audit_output.json').read_text())
digest = hashlib.sha256((root/'ANABELIAN_149_PUSH_paper.pdf').read_bytes()).hexdigest()
assert digest == data['pdf_sha256'], 'The rendered PDF has changed'
data['visually_reviewed_pages'] = data['rendered_pages']
data['full_resolution_reviewed_pages'] = [int(x) for x in args.full_resolution.split(',')]
assert set(data['full_resolution_reviewed_pages']) <= set(data['rendered_pages'])
data['review_status'] = args.notes
destination = root/f"audit/typesetting_review_{data['pages']}pages.json"
assert not destination.exists(), 'Preserve earlier review records'
destination.write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps({'review_record':str(destination),'pdf_sha256':digest,
                  'reviewed_pages':len(data['visually_reviewed_pages'])},indent=2))
