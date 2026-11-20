#!/usr/bin/env python3
"""Mechanical reconciliation for DM01_1_001-160. No OCR or reading inference.

Run from the task workspace (or pass --workspace). Source ZIP extraction is
expected at source/DM01_1_001-160_texts. Per-page human/model readings go in
work/scanNNN.json; this script checks and applies them, never inventing readings.
"""
from __future__ import annotations
import argparse
import csv
import dataclasses
import datetime as dt
import io
import fcntl
import json
from pathlib import Path
import re
import sys
from typing import Any
from other_error_aliases import ErrorAliases

FIELDS = ['id', 'scan', 'decision', 'reading', 'what the ink shows', 'crop', 'confidence']
EVENT_FIELDS = ['statement id', 'date', 'who (model, effort, run)', 'type', 'outcome']
METRIC_FIELDS = ['scan', 'marks', 'committed_utc', 'reader_started_utc', 'reader_finished_utc', 'page_views', 'crop_views']
MARK_RE = re.compile(r'\\(unsure|illegible)\{')
ANOMALOUS_IDS = {'M1340', 'M2152', 'M2285', 'M2534'}


def fail(message: str):
    raise ValueError(message)


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def escaped(text: str, at: int) -> bool:
    before = at - 1
    while before >= 0 and text[before] == '\\':
        before -= 1
    return (at - before - 1) % 2 == 1


@dataclasses.dataclass
class Mark:
    id: str
    scan: int
    kind: str
    start: int
    end: int
    body_start: int
    text: str
    parent: int | None = None
    children: list[int] = dataclasses.field(default_factory=list)

    @property
    def body(self):
        return self.text[self.body_start - self.start:-1]


def parse_marks(text: str, scan: int) -> list[Mark]:
    result: list[Mark] = []
    for match in MARK_RE.finditer(text):
        if escaped(text, match.start()):
            continue
        depth = 1
        end = match.end()
        while end < len(text) and depth:
            if not escaped(text, end):
                depth += (text[end] == '{') - (text[end] == '}')
            end += 1
        if depth:
            fail(f'scan {scan:03}: unbalanced mark at character {match.start()}')
        result.append(Mark('', scan, match.group(1), match.start(), end,
                           match.end(), text[match.start():end]))
    stack: list[int] = []
    for index, mark in enumerate(result):
        while stack and result[stack[-1]].end <= mark.start:
            stack.pop()
        if stack:
            parent = stack[-1]
            if mark.end > result[parent].end:
                fail(f'scan {scan:03}: overlapping non-nested macros')
            mark.parent = parent
            result[parent].children.append(index)
        stack.append(index)
    return result


def choices(mark: Mark) -> list[tuple[str, int, int]]:
    """Top-level, unescaped pipes delimit alternatives. Return source offsets."""
    body = mark.body
    depth = 0
    starts = [0]
    ends = []
    for i, char in enumerate(body):
        if escaped(body, i):
            continue
        depth += (char == '{') - (char == '}')
        if char == '|' and depth == 0:
            ends.append(i)
            starts.append(i + 1)
    ends.append(len(body))
    return [(body[a:b], mark.body_start+a, mark.body_start+b)
            for a, b in zip(starts, ends)]


def normalized(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def tsv_read(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def tsv_bytes(fields, rows) -> bytes:
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='raise')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def atomic(path: Path, content: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_bytes(content)
    tmp.replace(path)


class Project:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        self.source = self.workspace / 'source/DM01_1_001-160_texts'
        self.scans = self.workspace / 'source/DM01_1_001-160_scans'
        self.out = self.workspace / 'deliverable'
        self.marks_rows = tsv_read(self.source / 'MARKS.tsv')
        if not self.marks_rows:
            fail(f'No MARKS.tsv rows at {self.source}')
        self.scans_order = list(dict.fromkeys(int(r['scan']) for r in self.marks_rows))
        if self.scans_order != sorted(self.scans_order):
            fail('MARKS.tsv pages are not in increasing scan order')
        self.by_scan = {scan: [r for r in self.marks_rows if int(r['scan']) == scan]
                        for scan in self.scans_order}
        self.texts: dict[int, str] = {}
        self.marks: dict[int, list[Mark]] = {}
        self.source_anomalies: list[dict[str, str]] = []
        for scan in self.scans_order:
            text = (self.source / f'pages/1_scan{scan:03}.tex').read_bytes().decode('utf-8')
            marks = parse_marks(text, scan)
            source_rows = self.by_scan[scan]
            if len(marks) != len(source_rows):
                fail(f'scan {scan:03}: {len(marks)} parsed macros vs {len(source_rows)} MARKS rows')
            for mark, row in zip(marks, source_rows):
                mark.id = row['id']
                if mark.kind != row['mark']:
                    fail(f'{mark.id}: source kind differs from MARKS.tsv')
                if mark.text != row['the mark as written']:
                    if mark.id not in ANOMALOUS_IDS:
                        fail(f'{mark.id}: unexpected source / MARKS discrepancy')
                    self.source_anomalies.append({'id': mark.id, 'scan': str(scan),
                                                 'listed': row['the mark as written'], 'actual': mark.text})
            self.texts[scan] = text
            self.marks[scan] = marks
        ids = [r['id'] for r in self.marks_rows]
        if len(ids) != len(set(ids)):
            fail('Duplicate IDs in MARKS.tsv')

    def receipts(self):
        receipts = []
        for path in sorted((self.out / 'audit/receipts').glob('scan*.json')):
            receipt = json.loads(path.read_text(encoding='utf-8'))
            if int(receipt['scan']) not in self.by_scan:
                fail(f'Unknown scan in receipt {path.name}')
            receipts.append(receipt)
        scans = [int(r['scan']) for r in receipts]
        if scans != self.scans_order[:len(scans)]:
            fail(f'Committed scans are not a prefix of MARKS order: {scans}')
        return receipts

    def view_counts(self, scan: int, meta: dict):
        from PIL import Image
        with Image.open(self.scans / f'1_scan{scan:03}.jpg') as image:
            width,height=image.size
        def is_page(view):
            box=view.get('box')
            return box=='page' or (isinstance(box,(list,tuple)) and list(box)==[0,0,width,height])
        views=meta.get('views',[])
        pages=sum(is_page(v) for v in views)
        crops=len(views)-pages
        return meta.get('page_views',pages),meta.get('crop_views',crops)

    def _crop(self, crop: Any, scan: int) -> str:
        if isinstance(crop,(list,tuple)) and crop and all(isinstance(box,(list,tuple)) for box in crop):
            return '; '.join(self._crop(box,scan) for box in crop)
        if isinstance(crop,str) and ';' in crop:
            return '; '.join(self._crop(box.strip(),scan) for box in crop.split(';'))
        if isinstance(crop, (list, tuple)):
            crop = ','.join(str(x) for x in crop)
        if not isinstance(crop, str):
            fail('crop must be "page" or four source-pixel coordinates')
        if crop == 'page':
            return crop
        found = re.fullmatch(r'\s*[\[(]?\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)\s*[\])]?\s*', crop)
        if not found:
            fail(f'scan {scan:03}: invalid crop {crop!r}; use x0,y0,x1,y1 or page')
        x0, y0, x1, y1 = map(int, found.groups())
        from PIL import Image
        with Image.open(self.scans / f'1_scan{scan:03}.jpg') as image:
            width, height = image.size
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
            fail(f'scan {scan:03}: crop {crop} outside actual image {width}x{height}')
        return f'{x0},{y0},{x1},{y1}'

    def validate_rows(self, scan: int, data: Any) -> tuple[list[dict[str, str]], dict]:
        if scan not in self.by_scan:
            fail(f'scan {scan:03} not listed in MARKS.tsv')
        meta = data if isinstance(data, dict) else {}
        supplied = meta.get('rows') if meta else data
        if not isinstance(supplied, list):
            fail('Submission must be a row list or an object containing rows')
        expected_ids = [m.id for m in self.marks[scan]]
        supplied_ids = [r.get('id') for r in supplied]
        if supplied_ids != expected_ids:
            fail(f'scan {scan:03}: rows must be exactly these IDs in order: {expected_ids}; got {supplied_ids}')
        rows = []
        for raw in supplied:
            absent = [k for k in FIELDS if k not in raw]
            if absent:
                fail(f'{raw.get("id")}: missing columns {absent}')
            row = {key: str(raw[key]) for key in FIELDS}
            if int(row['scan']) != scan:
                fail(f'{row["id"]}: wrong scan')
            row['scan'] = str(scan)
            row['crop'] = self._crop(raw['crop'], scan)
            if row['decision'] not in {'first','alternative','other','undecided'}:
                fail(f'{row["id"]}: invalid decision')
            if row['confidence'] not in {'high','medium','low'}:
                fail(f'{row["id"]}: invalid confidence')
            if not row['what the ink shows'].strip():
                fail(f'{row["id"]}: empty ink evidence')
            if '\t' in row['reading'] or '\r' in row['reading'] or '\n' in row['reading']:
                fail(f'{row["id"]}: reading must occupy a single TSV line; use LaTeX spaces')
            if any(ord(char)<32 or ord(char)==127 for char in row['reading']):
                fail(f'{row["id"]}: ASCII control character in LaTeX reading; check string escaping')
            brace_depth=0
            for position,char in enumerate(row['reading']):
                if escaped(row['reading'],position):
                    continue
                brace_depth += (char=='{')-(char=='}')
                if brace_depth<0:
                    fail(f'{row["id"]}: unmatched closing brace in replacement reading')
            if brace_depth:
                fail(f'{row["id"]}: unmatched opening brace in replacement reading')
            if row['decision'] == 'undecided' and not MARK_RE.search(row['reading']):
                fail(f'{row["id"]}: undecided reading must retain an uncertainty macro')
            if row['decision'] != 'undecided' and MARK_RE.search(row['reading']) and not self.marks[scan][len(rows)].children:
                fail(f'{row["id"]}: settled reading still contains an uncertainty macro')
            rows.append(row)
        # Resolve inner records before checking an outer candidate. Outer rows win
        # the actual replacement; all nested rows still require their own evidence.
        marks = self.marks[scan]
        for i in range(len(marks)-1, -1, -1):
            mark, row = marks[i], rows[i]
            candidates = choices(mark)
            resolved = []
            for text, begin, end in candidates:
                for child in reversed(mark.children):
                    cm = marks[child]
                    if begin <= cm.start and cm.end <= end:
                        text = text[:cm.start-begin] + rows[child]['reading'] + text[cm.end-begin:]
                resolved.append(text)
            decision = row['decision']
            if (mark.kind == 'illegible' or re.fullmatch(r'\\illegible\{\d+\}',mark.body.strip())) and decision in {'first','alternative'}:
                fail(f'{mark.id}: illegible placeholder is not a reading; use other or undecided')
            explicit = supplied[i].get('candidates')
            if explicit is not None:
                if not isinstance(explicit,list) or not explicit or not all(isinstance(c,str) for c in explicit):
                    fail(f'{mark.id}: candidates override must be a nonempty string list')
                resolved = explicit
            # Literal unescaped |...| is also used in source maths. An exact
            # full-body reading is therefore admissible as first; an explicit
            # candidates list is needed if literal bars and alternatives mix.
            first_forms = [resolved[0]]
            if explicit is None and '|' in mark.body:
                full_body = mark.body
                for child in reversed(mark.children):
                    cm = marks[child]
                    full_body = full_body[:cm.start-mark.body_start] + rows[child]['reading'] + full_body[cm.end-mark.body_start:]
                first_forms.append(full_body)
            if decision == 'first' and not any(normalized(row['reading']) == normalized(c) for c in first_forms):
                fail(f'{mark.id}: first reading must match first candidate after child reconciliation: {resolved[0]!r}')
            if decision == 'alternative' and not any(normalized(row['reading']) == normalized(c) for c in resolved[1:]):
                fail(f'{mark.id}: alternative reading must match a candidate after first: {resolved[1:]!r}')
            # If the outer output preserves the literal nested macro, replace it
            # with the nested decision, but reject repeated/ambiguous matches.
            for child in mark.children:
                cm = marks[child]
                inner = rows[child]['reading']
                if cm.text in row['reading'] and cm.text != inner:
                    if row['reading'].count(cm.text) != 1:
                        fail(f'{mark.id}: nested {cm.id} retained ambiguously')
                    row['reading'] = row['reading'].replace(cm.text, inner, 1)
        return rows, meta

    def apply(self, scan: int, rows: list[dict[str, str]]) -> bytes:
        text = self.texts[scan]
        for mark, row in reversed(list(zip(self.marks[scan], rows))):
            if mark.parent is None:
                text = text[:mark.start] + row['reading'] + text[mark.end:]
        return text.encode('utf-8')

    def commit(self, scan: int, path: Path | None, who: str | None, check_type: str):
        path = path or self.workspace / f'work/scan{scan:03}.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        rows, meta = self.validate_rows(scan, data)
        error_fields = ['scan','place','the reading','what the ink shows']
        existing_errors = tsv_read(self.out / 'other_errors.tsv')
        incoming_errors = []
        for error in meta.get('other_errors',[]):
            row = {key:str(error.get(key,'')) for key in error_fields}
            if row['scan'] and int(row['scan']) != scan:
                fail(f'scan {scan:03}: unmarked error assigned to another scan')
            row['scan'] = str(scan)
            incoming_errors.append(row)
        aliases = ErrorAliases.load(self.out / 'audit/OTHER_ERROR_ALIASES.json')
        other_errors = aliases.append(existing_errors, incoming_errors)
        who = who or meta.get('who') or meta.get('reader')
        if not who or not isinstance(who, str):
            fail('Supply --who "model; effort; run" or submission metadata who/reader; no provenance is inferred')
        log_path = self.out / 'progress.log'
        if not log_path.exists() or not log_path.read_text().splitlines():
            fail('Root must initialize progress.log with the actual UTC start before any commit')
        receipts = self.receipts()
        prior = next((r for r in receipts if int(r['scan']) == scan), None)
        if prior:
            if prior['rows'] != rows:
                fail(f'scan {scan:03} already committed with different decisions; amend explicitly and retain audit history')
            receipt = prior
        else:
            expected_scan = self.scans_order[len(receipts)] if len(receipts) < len(self.scans_order) else None
            if scan != expected_scan:
                fail(f'Next page must be {expected_scan}, not {scan}; pages complete in order')
            receipt = {'scan': scan, 'committed_utc': utcnow(), 'who': who, 'check_type': check_type,
                       'rows': rows, 'submission_rows': supplied_rows(data), 'metadata': {k:v for k,v in meta.items() if k != 'rows'},
                       'submission_path': str(path.relative_to(self.workspace)) if path.is_relative_to(self.workspace) else str(path)}
            receipt_path = self.out / f'audit/receipts/scan{scan:03}.json'
            atomic(receipt_path, (json.dumps(receipt, ensure_ascii=False, indent=2)+'\n').encode('utf-8'))
            receipts.append(receipt)
        # Preserve the reader's complete submitted record, including all views,
        # patterns, unmarked observations, and declared timing; no source scans.
        atomic(self.out / f'audit/scan{scan:03}.json',
               (json.dumps(data, ensure_ascii=False, indent=2)+'\n').encode('utf-8'))
        for part in meta.get('source_submission_paths',[]):
            part_path = Path(part)
            if not part_path.is_absolute():
                part_path = self.workspace / part_path
            if not part_path.is_file():
                fail(f'Missing declared source submission: {part_path}')
            atomic(self.out / 'audit/parts' / part_path.name,part_path.read_bytes())
        atomic(self.out / 'other_errors.tsv',tsv_bytes(error_fields,other_errors))
        patterns_path = self.out / 'PATTERNS.md'
        patterns_text = patterns_path.read_text(encoding='utf-8') if patterns_path.exists() else '# Recurring doubts and errors\n'
        marker = f'<!-- scan-{scan:03}-patterns -->'
        if meta.get('patterns') and marker not in patterns_text:
            addition = f'\n{marker}\n## Scan {scan:03}\n\n'
            for pattern in meta['patterns']:
                ids = pattern.get('marks',[])
                if not isinstance(ids,str):
                    ids = ', '.join(str(v) for v in ids)
                addition += f'### {pattern.get("name","Unnamed pattern")}\n\nMarks: {ids}.\n\n{pattern.get("description","")}\n\n'
            atomic(patterns_path,(patterns_text+addition).encode('utf-8'))
        # Receipts permit safe reconstruction after a partially completed write.
        all_rows = [r for receipt_item in receipts for r in receipt_item['rows']]
        atomic(self.out / 'decisions.tsv', tsv_bytes(FIELDS, all_rows))
        for item in receipts:
            atomic(self.out / f'pages/1_scan{int(item["scan"]):03}.tex', self.apply(int(item['scan']), item['rows']))
        events = tsv_read(self.out / 'CHECK_EVENTS.tsv')
        if events and set(events[0]) != set(EVENT_FIELDS):
            fail('Existing CHECK_EVENTS.tsv has unexpected header; expected '+str(EVENT_FIELDS))
        for item in receipts:
            # Initial checks retain their original statements after an audited
            # amendment. Never backdate a refined reading to its primary check.
            for row in item.get('initial_rows', item['rows']):
                event = {'statement id': row['id'], 'date': item['committed_utc'], 'who (model, effort, run)': item['metadata'].get('row_readers',{}).get(row['id'],item['who']),
                         'type': item['check_type'],
                         'outcome': f'{row["decision"]}; reading={row["reading"]}; confidence={row["confidence"]}; crop={row["crop"]}; {row["what the ink shows"]}'}
                if event not in events:
                    events.append(event)
        atomic(self.out / 'CHECK_EVENTS.tsv', tsv_bytes(EVENT_FIELDS, events))
        metrics = []
        for item in receipts:
            m = item['metadata']
            page_views,crop_views=self.view_counts(int(item['scan']),m)
            metrics.append({'scan': str(item['scan']), 'marks': str(len(item['rows'])),
                            'committed_utc': item['committed_utc'],
                            'reader_started_utc': str(m.get('reader_started_utc',m.get('started_utc',''))),
                            'reader_finished_utc': str(m.get('reader_finished_utc',m.get('finished_utc',''))),
                            'page_views': str(page_views), 'crop_views': str(crop_views)})
        atomic(self.out / 'audit/METRICS.tsv', tsv_bytes(METRIC_FIELDS, metrics))
        lines = log_path.read_text(encoding='utf-8').splitlines()
        existing_scans = [int(m.group(1)) for line in lines[1:] if (m := re.fullmatch(r'scan (\d+) done .+', line))]
        if existing_scans != [int(r['scan']) for r in receipts[:len(existing_scans)]]:
            fail('progress.log completed scans are out of receipt order')
        for item in receipts[len(existing_scans):]:
            lines.append(f'scan {int(item["scan"]):03} done {item["committed_utc"]}')
        atomic(log_path, ('\n'.join(lines)+'\n').encode('utf-8'))
        print(json.dumps({'committed_scan':scan, 'marks':len(rows), 'total_committed_marks':len(all_rows),
                          'total_committed_pages':len(receipts), 'committed_utc':receipt['committed_utc']}, ensure_ascii=False))

    def import_check(self, path: Path):
        data = json.loads(path.read_text(encoding='utf-8'))
        who = data.get('reader') or data.get('who')
        when = data.get('checked_at') or data.get('finished_utc') or data.get('date')
        check_type = data.get('type','independent re-proof')
        if not who or not when:
            fail('Independent check must declare reader/who and checked_at/finished_utc/date')
        known = {r['id']:r for r in tsv_read(self.out / 'decisions.tsv')}
        rows = data.get('rows',[])
        if not rows:
            fail('Independent check has no rows')
        events = tsv_read(self.out / 'CHECK_EVENTS.tsv')
        added = 0
        for row in rows:
            mark_id = row['id']
            if mark_id not in known:
                fail(f'{mark_id}: independent check precedes initial page commit')
            observation = row.get('observed strokes') or row.get('what the ink shows')
            if not observation:
                fail(f'{mark_id}: no ink observation in independent check')
            crop = self._crop(row['crop'],int(known[mark_id]['scan']))
            reading = row['reading']
            relation = 'agrees with committed reading' if reading == known[mark_id]['reading'] else 'differs from committed reading; see the primary page audit for reconciliation'
            versions_path = self.out / 'audit/STATEMENT_VERSIONS.json'
            versions = json.loads(versions_path.read_text()) if versions_path.exists() else {}
            statement_id = versions.get(mark_id, {}).get('statement_id', mark_id)
            event = {'statement id':statement_id, 'date':when, 'who (model, effort, run)':who,
                     'type':check_type, 'outcome':f'{relation}; reading={reading}; confidence={row.get("confidence","unspecified")}; crop={crop}; {observation}'}
            if event not in events:
                events.append(event)
                added += 1
        fields=['scan','place','the reading','what the ink shows']
        existing_errors=tsv_read(self.out/'other_errors.tsv')
        incoming_errors=[{key:str(row[key]) for key in fields}
                         for row in data.get('other_errors',[])]
        aliases=ErrorAliases.load(self.out/'audit/OTHER_ERROR_ALIASES.json')
        errors=aliases.append(existing_errors,incoming_errors)
        target = self.out / 'audit' / path.name
        content = (json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
        if target.exists() and target.read_bytes() != content:
            fail(f'Independent-check audit file already exists with different content: {target.name}')
        atomic(target,content)
        atomic(self.out / 'CHECK_EVENTS.tsv',tsv_bytes(EVENT_FIELDS,events))
        atomic(self.out/'other_errors.tsv',tsv_bytes(fields,errors))
        print(json.dumps({'imported_check':path.name,'new_check_events':added,'rows':len(rows)},ensure_ascii=False))

    def verify(self, final: bool):
        aliases = ErrorAliases.load(self.out / 'audit/OTHER_ERROR_ALIASES.json')
        aliases.assert_canonical(tsv_read(self.out / 'other_errors.tsv'))
        receipts = self.receipts()
        all_rows = []
        for receipt in receipts:
            scan = int(receipt['scan'])
            validation_data = receipt.get('submission_rows',receipt['rows'])
            rows, _ = self.validate_rows(scan, validation_data)
            if rows != receipt['rows']:
                fail(f'scan {scan:03}: receipt rows differ from validated submission')
            expected = self.apply(scan, rows)
            output_path = self.out / f'pages/1_scan{scan:03}.tex'
            if not output_path.exists() or output_path.read_bytes() != expected:
                fail(f'scan {scan:03}: output differs from exact mark-only substitutions')
            all_rows.extend(rows)
        if tsv_read(self.out / 'decisions.tsv') != all_rows:
            fail('decisions.tsv differs from committed receipts in content or order')
        events = tsv_read(self.out / 'CHECK_EVENTS.tsv')
        checked_ids = {r['statement id'] for r in events if r.get('who (model, effort, run)') and r.get('date') and r.get('type') and r.get('outcome')}
        if any(row['id'] not in checked_ids for row in all_rows):
            fail('Some decisions have no complete check event')
        if (self.out / 'audit/amendments').exists():
            from amendments import verify_amendments
            verify_amendments(self, receipts, events)
        lines = (self.out / 'progress.log').read_text(encoding='utf-8').splitlines()
        done = [int(m.group(1)) for line in lines[1:] if (m := re.fullmatch(r'scan (\d+) done .+', line))]
        if done != [int(r['scan']) for r in receipts]:
            fail('progress.log page order or count differs from receipts')
        committed = {int(r['scan']) for r in receipts}
        for path in (self.out / 'pages').glob('1_scan*.tex'):
            scan = int(re.fullmatch(r'1_scan(\d+)\.tex',path.name).group(1))
            if scan not in self.texts:
                fail(f'Unexpected page {path.name}')
            if scan not in committed and path.read_bytes() != self.texts[scan].encode('utf-8'):
                fail(f'Uncommitted page {path.name} differs from source')
        if final and (len(all_rows) != len(self.marks_rows) or len(receipts) != len(self.scans_order)):
            fail(f'Incomplete: {len(all_rows)}/{len(self.marks_rows)} marks, {len(receipts)}/{len(self.scans_order)} pages')
        print(json.dumps({'verified': True, 'final':final, 'marks':len(all_rows), 'pages':len(receipts),
                          'source_marks':len(self.marks_rows), 'source_pages':len(self.scans_order),
                          'source_anomalies':len(self.source_anomalies), 'check_events':len(events)}, ensure_ascii=False))

    def status(self):
        receipts = self.receipts()
        rows = [r for receipt in receipts for r in receipt['rows']]
        from collections import Counter
        print(json.dumps({'pages_done':len(receipts), 'marks_done':len(rows),
                          'total_pages':len(self.scans_order), 'total_marks':len(self.marks_rows),
                          'next_scan':self.scans_order[len(receipts)] if len(receipts)<len(self.scans_order) else None,
                          'decisions':dict(Counter(r['decision'] for r in rows)),
                          'source_anomalies':self.source_anomalies}, ensure_ascii=False, indent=2))


def supplied_rows(data):
    return data.get('rows',[]) if isinstance(data,dict) else data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,default=Path.cwd())
    commands = parser.add_subparsers(dest='command',required=True)
    commit = commands.add_parser('commit')
    commit.add_argument('scan',type=int)
    commit.add_argument('--file',type=Path)
    commit.add_argument('--who')
    commit.add_argument('--type',default='targeted proof check')
    verify = commands.add_parser('verify')
    verify.add_argument('--final',action='store_true')
    commands.add_parser('status')
    independent = commands.add_parser('import-check')
    independent.add_argument('file',type=Path)
    amendment = commands.add_parser('amend', help='Validate an explicit amendment plan; --apply preserves history and applies it')
    amendment.add_argument('plan', type=Path)
    amendment.add_argument('--apply', action='store_true')
    validate = commands.add_parser('validate')
    validate.add_argument('scan',type=int)
    validate.add_argument('--file',type=Path)
    args=parser.parse_args()
    project=Project(args.workspace)
    if args.command=='commit':
        lock_path=project.workspace/'work/reconcile.lock'
        lock_path.parent.mkdir(parents=True,exist_ok=True)
        with lock_path.open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            project.commit(args.scan,args.file,args.who,args.type)
    elif args.command=='verify':
        project.verify(args.final)
    elif args.command=='status':
        project.status()
    elif args.command in {'import-check', 'amend'}:
        lock_path=project.workspace/'work/reconcile.lock'
        lock_path.parent.mkdir(parents=True,exist_ok=True)
        with lock_path.open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            if args.command == 'import-check':
                project.import_check(args.file)
            else:
                from amendments import amend
                amend(project, args.plan, args.apply)
    else:
        path=args.file or project.workspace/f'work/scan{args.scan:03}.json'
        rows,_=project.validate_rows(args.scan,json.loads(path.read_text(encoding='utf-8')))
        print(json.dumps({'valid':True,'scan':args.scan,'marks':len(rows)},ensure_ascii=False))

if __name__=='__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr)
        sys.exit(1)
