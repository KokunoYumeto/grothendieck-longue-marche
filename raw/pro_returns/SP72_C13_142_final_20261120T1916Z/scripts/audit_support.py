"""Small helpers for explicit main-reader audit adjudications.

These functions do no reading and choose no manuscript text. The main reader
supplies every accepted reading and every apparatus edit after inspecting ink.
"""
from pathlib import Path
import json
import subprocess
import sys

OUT = Path(__file__).resolve().parents[1]


def load(scan):
    folder = OUT/'documentation/reviews'/f'scan{scan:03}'
    report = json.loads((folder/'report.json').read_text())
    audit = json.loads((OUT/'audit'/f'scan{scan:03}'/'report.json').read_text())
    assert audit['complete_page_read'] and audit['inventory_checked']
    assert not report.get('audit_complete'), 'Already audited.'
    return report, audit, (folder/'page.tex').read_text()


def replace_exact(text, before, after, count=1):
    assert text.count(before) == count, (before, text.count(before), count)
    return text.replace(before, after, count)


def commit(scan, report, audit, text, summary, adjudications):
    assert summary and adjudications
    required = {c['id'] for c in audit.get('changes', [])}
    covered = {a.get('id') for a in adjudications}
    assert required <= covered, ('Unadjudicated audit proposal', required-covered)
    report['audit_complete'] = True
    report['audit_review_complete'] = True
    report['audit_reader'] = audit['auditor']
    report['audit_note'] = summary
    report['audit_adjudication'] = adjudications
    report['audit_report'] = f'audit/scan{scan:03}/report.json'
    folder = OUT/'documentation/reviews'/f'scan{scan:03}'
    (folder/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    (folder/'page.tex').write_text(text)
    subprocess.run([sys.executable, str(OUT/'scripts/normalize_report_metadata.py')], check=True)
    subprocess.run([sys.executable, str(OUT/'scripts/finish_audit.py'), str(scan)], check=True)
