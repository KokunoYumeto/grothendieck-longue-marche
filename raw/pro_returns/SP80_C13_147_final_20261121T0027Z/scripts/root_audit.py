"""Apply explicit main-reader decisions after visual comparison of fresh crops.

This helper makes no reading decisions. Each differing box must be supplied
with an individual selection and visual reason. Frozen readings are untouched.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

class Audit:
    def __init__(self, scan):
        self.scan = scan
        self.stem = f'147_scan{scan}'
        self.rp = ROOT/'review'/f'{self.stem}_reviewed.json'
        self.pp = ROOT/'pages'/f'{self.stem}.tex'
        self.report = json.loads(self.rp.read_text())
        self.page = self.pp.read_text()
        with (ROOT/'second'/f'{self.stem}_comparison.tsv').open() as f:
            self.comparison = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
        self.choices = []
        assert 'audit_completed_at' not in self.report

    def keep(self, box, evidence, **extra):
        self.choices.append(dict(box=box, selection='first', changed='no', evidence=evidence, **extra))

    def change(self, box, final, evidence, **extra):
        self.choices.append(dict(box=box, selection='literal', changed='yes', final=final, evidence=evidence, **extra))

    def replace(self, old, new, count=1):
        assert self.page.count(old) == count, (self.scan, old, self.page.count(old), count)
        self.page = self.page.replace(old, new)

    def evidence(self, box):
        return next(c['evidence'] for c in self.choices if c['box']==box)

    def crop_fields(self, box):
        b = next(b for b in self.report['second_boxes'] if b['box']==box)
        return dict(crop=f'crops/{self.stem}_second_{box}.jpg', box=b['coords'])

    def update_row(self, index, box, **fields):
        self.report['rows'][index].update(scan_shows=self.evidence(box), **self.crop_fields(box), **fields)

    def add_row(self, box, place, C, H, final, confidence, kind, error_category,
                against_C, against_H, math_consequential=False, marked_in_H=False):
        self.report['rows'].append(dict(place=place, C=C, H=H, final=final,
            scan_shows=self.evidence(box), **self.crop_fields(box), confidence=confidence,
            kind=kind, error_category=error_category, against_C=against_C, against_H=against_H,
            math_consequential=math_consequential, marked_in_H=marked_in_H))

    def doubt(self, place, reading, alternatives, confidence, replace_place=None):
        item=dict(place=place, reading=reading, alternatives=alternatives, confidence=confidence)
        if replace_place is None:
            self.report['doubts'].append(item)
        else:
            matches=[i for i,d in enumerate(self.report['doubts']) if d['place']==replace_place]
            assert len(matches)==1, (replace_place,matches)
            self.report['doubts'][matches[0]]=item

    def decision(self, identifier, box, **fields):
        d=next(d for d in self.report['decisions'] if d['id']==identifier)
        d.update(ink=self.evidence(box), **self.crop_fields(box), **fields)

    def note(self, text):
        self.report['notes'].append(text)
        n=len(self.report['notes'])
        self.report['check_events'].append(dict(statement_id=f'AUD{self.scan}; N{self.scan}-{n:02d}',
            date=datetime.now(timezone.utc).strftime('%Y-%m-%d'),
            type='used and rechecked in this run',
            outcome=f'Main reader visually adjudicated every differing second-reading crop on scan{self.scan}. Ink comparison only; no mathematical proof claimed.'))

    def finish(self):
        ids=[x['box'] for x in self.choices]
        assert len(ids)==len(set(ids))
        assert {b for b,r in self.comparison.items() if r['equal']=='no'}<=set(ids)
        assert all(c['evidence'].strip() for c in self.choices)
        for meta_path in (ROOT/'second/first_readings_frozen.json', ROOT/'second'/f'{self.stem}_comparison_meta.json'):
            meta=json.loads(meta_path.read_text())
            assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in meta['sha256'].items())
        cp=ROOT/'review'/f'{self.stem}_root_choices.json'
        assert not cp.exists()
        cp.write_text(json.dumps(self.choices, ensure_ascii=False, indent=2)+'\n')
        self.pp.write_text(self.page)
        self.rp.write_text(json.dumps(self.report, ensure_ascii=False, indent=2)+'\n')
        for script,args in [('expand_root_choices.py',[str(self.scan),str(cp)]),
                            ('write_adjudications.py',[str(self.scan),str(ROOT/'review'/f'{self.stem}_root_plan.json')]),
                            ('finish_audit.py',[str(self.scan)])]:
            subprocess.run([sys.executable,str(ROOT/'scripts'/script),*args],check=True)
