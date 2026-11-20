"""Structural final checks only; never OCR or compile the transcription."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "SP73_C13_142+143"
PAGES = [f"142_scan{n:03}" for n in
         [101,102,103,104,106,108,109,110,111,112,113,114,115,116,117,118,120,121]]
PAGES += [f"143_scan{n:03}" for n in range(2,8)]
ERRORS = []
SCHEMAS = {
    'decisions.tsv': ['id', 'cote', 'scan', 'decision', 'reading',
                      'what the ink shows', 'crop', 'confidence'],
    f'{PREFIX}_inventory.csv': ['scan', 'sheet_kind', 'hand', 'element', 'kind',
                               'position', 'first_words_or_objects', 'transcribed'],
    f'{PREFIX}_collation.tsv': ['folder', 'their_page', 'our_scan', 'line',
                               'their_reading', 'codex_reading', 'final_reading',
                               'scan_shows', 'kind', 'marked_in_H', 'confidence'],
    'CHECK_EVENTS.tsv': ['statement_id', 'date', 'who', 'type', 'outcome',
                         'place', 'statement'],
}

def require(condition, message):
    if not condition:
        ERRORS.append(message)

def rows(name, delimiter="\t"):
    with (ROOT / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def balanced_braces(text):
    depth = 0
    for line in text.splitlines():
        for m in re.finditer(r"\\.|%|[{}]", line):
            s = m.group()
            if s == "%":
                break
            if s == "{":
                depth += 1
            elif s == "}":
                depth -= 1
                if depth < 0:
                    return False
    return depth == 0

def balanced_environments(text):
    stack = []
    for line in text.splitlines():
        line = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
        for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", line):
            action, environment = match.groups()
            if action == 'begin':
                stack.append(environment)
            elif not stack or stack.pop() != environment:
                return False
    return not stack

required = list(SCHEMAS) + ['progress.log', f'{PREFIX}_transcription.tex']
required += [f'{PREFIX}_{suffix}.md' for suffix in
             ['changes', 'doubts', 'notes', 'sheet_feedback', 'hand_log']]
required += ['state/notes_consolidated.json', 'state/notation_consolidated.md',
             'state/notation_reconciliation.md', 'state/legibility.md',
             'state/additional_feedback.md']
for name in required:
    require((ROOT / name).is_file(), 'Missing required final file ' + name)
for name, fields in SCHEMAS.items():
    if (ROOT / name).exists():
        with (ROOT / name).open(encoding='utf-8', newline='') as stream:
            reader = csv.DictReader(stream, delimiter=',' if name.endswith('.csv') else '\t')
            require(reader.fieldnames == fields, 'Incorrect column schema in ' + name)
            for number, row in enumerate(reader, 2):
                require(None not in row and all(value is not None for value in row.values()),
                        f'Malformed row {number} in {name}')
if ERRORS:
    print(json.dumps({'errors': ERRORS}, ensure_ascii=False, indent=2))
    sys.exit(1)

accepted = {}
for page in PAGES:
    p = ROOT / "pages" / f"{page}.tex"
    require(p.exists(), f"Missing page {page}")
    if not p.exists():
        continue
    text = p.read_text()
    require(balanced_braces(text), f"Unbalanced braces in {page}")
    require(balanced_environments(text), f"Unbalanced environments in {page}")
    scan = str(int(page.split("scan")[1]))
    require(re.findall(r"\\scanpage\{(\d+)\}", text) == [scan],
            f"Wrong scan marker in {page}")
    rp = ROOT / "state" / f"{page}_accepted.json"
    require(rp.exists(), f"Missing accepted record {page}")
    if not rp.exists():
        continue
    d = json.loads(rp.read_text())
    accepted[page] = d
    require(str(d.get('reader', '')).split('/')[-1] in {'reader_a', 'reader_b', 'reader_c'}
            and str(d.get('auditor', '')).split('/')[-1] in {'reader_a', 'reader_b', 'reader_c'},
            f'Missing or unexpected reader identity {page}')
    require(d.get("main_review", {}).get("approved"), f"Unapproved main review {page}")
    require(d.get("audited_at") and d.get("audit_main_review", {}).get("approved"),
            f"Unapproved second reading {page}")
    audit_path = ROOT / 'audits' / (page + '.json')
    require(audit_path.is_file(), f'Missing full second-reading record {page}')
    if audit_path.exists():
        audit = json.loads(audit_path.read_text())
        view_names = [Path(view).name for view in audit.get('views', [])]
        initial_views = [page + '.jpg', page + '_top.png', page + '_bottom.png']
        require(view_names[:3] == initial_views and
                all(view_names.count(view) == 1 for view in initial_views),
                f'Original/native-half audit view record differs for {page}')
    require(str(d.get("reader", "")).split('/')[-1] !=
            str(d.get("auditor", "")).split('/')[-1],
            f"Same first and second reader {page}")
    viewed_crops = set(d.get("main_review", {}).get("crops_viewed", []))
    viewed_crops.update(d.get("audit_main_review", {}).get("crops_viewed", []))
    for c in d.get("changes", []):
        if not (c.get("differs_c") or c.get("differs_h")):
            continue
        cp = c.get("crop")
        # The entire wrong H leaf at scan104 is assessed against the original.
        whole_wrong_leaf = page == "142_scan104" and c["id"].endswith("D40")
        require(bool(cp) or whole_wrong_leaf, f"Missing crop reference {c['id']}")
        if cp:
            require((ROOT / cp).exists(), f"Missing crop file {cp}")
            require(isinstance(c.get("box"), list) and len(c["box"]) == 4,
                    f"Missing original pixel box {c['id']}")
            require(cp in viewed_crops, f"No main-reader view recorded for {c['id']}")
        for extra in c.get('additional_crops', []) + c.get('evidence_crops', []):
            ep = extra.get('crop')
            require(bool(ep) and (ROOT / ep).exists(),
                    f"Missing additional crop file in {c['id']}")
            require(isinstance(extra.get('box'), list) and len(extra['box']) == 4,
                    f"Missing additional crop box in {c['id']}")
            require(ep in viewed_crops,
                    f"No main-reader additional-crop view recorded for {c['id']}")
        require(c.get("confidence") in {"high", "medium", "low"},
                f"Invalid confidence {c['id']}")

require(sorted(p.stem for p in (ROOT / "pages").glob("*.tex")) == sorted(PAGES),
        "Page directory does not contain exactly the requested24 files")
combined = (ROOT / f"{PREFIX}_transcription.tex").read_text()
require(balanced_braces(combined), "Unbalanced combined transcription")
require(balanced_environments(combined), "Unbalanced combined environments")
for page in PAGES:
    require((ROOT / 'pages' / (page + '.tex')).read_text().strip() in combined,
            f"Combined transcription does not contain the complete page {page}")
require(re.findall(r"\\scanpage\{(\d+)\}", combined) ==
        [str(int(p.split("scan")[1])) for p in PAGES], "Wrong combined page order")
require(re.findall(r"\\cotefile\{(\d+)\}", combined) == ["142", "143"],
        "Wrong cote boundaries")
expected_tokens = []
last_cote = None
for page in PAGES:
    cote, scan = page.split('_scan')
    if cote != last_cote:
        expected_tokens.append(('cotefile', cote))
        last_cote = cote
    expected_tokens.append(('scanpage', str(int(scan))))
require(re.findall(r'\\(cotefile|scanpage)\{(\d+)\}', combined) == expected_tokens,
        'Cote markers are not interleaved with the correct page boundaries')
require(not re.search(r'\\(?:documentclass|usepackage)\b|\\begin\{document\}', combined),
        'Combined transcription contains a preamble or document wrapper')

decisions = rows("decisions.tsv")
source_marks = ROOT.parent / "source" / "SP73_C13_142+143_texts" / "MARKS.tsv"
with source_marks.open(encoding="utf-8-sig", newline="") as f:
    original = list(csv.DictReader(f, delimiter="\t"))
require([d["id"] for d in decisions] == [d["id"] for d in original],
        "Source-mark coverage/order differs")
require(len(decisions) == 175, "Expected175 source-mark decisions")
for d in decisions:
    require(d["decision"] in {"first", "alternative", "other", "undecided"},
            f"Invalid mark decision {d['id']}")
    require(d['confidence'] in {'high', 'medium', 'low'} and
            bool(d['what the ink shows']) and bool(d['crop']),
            f'Incomplete mark evidence/confidence {d["id"]}')

inventory = rows(f"{PREFIX}_inventory.csv", ",")
require(all(d["transcribed"] == "yes" for d in inventory), "Incomplete inventory")
require(set(d["scan"] for d in inventory) == set(PAGES), "Inventory page coverage differs")
sheet_kinds = {'text', 'reused_typed', 'typescript', 'letter', 'list', 'cancelled_draft', 'cover'}
element_kinds = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
require(all(d['sheet_kind'] in sheet_kinds and d['kind'] in element_kinds
            and d['hand'] and d['element'] for d in inventory),
        'Invalid or incomplete inventory metadata')
for page in PAGES:
    ids = [d['element'] for d in inventory if d['scan'] == page]
    require(len(ids) == len(set(ids)), f'Duplicate inventory element in {page}')
collation = rows(f"{PREFIX}_collation.tsv")
require(not any(d["folder"] == "142" and int(d["our_scan"]) == 109 for d in collation),
        "H collation incorrectly contains scan109")
allowed_kinds = {"misread word", "misread symbol or index", "omission",
                 "text not on the page", "deletion state (struck given live or live given struck)", "insertion or placement",
                 "abbreviation expanded or spelling modernised", "readable ink left as \\ill{}",
                 "drawing or diagram", "other"}
require(all(d["kind"] in allowed_kinds for d in collation), "Invalid H collation kind")
for d in collation:
    require(int(d['their_page']) == int(d['our_scan']) - 1,
            'Incorrect H page mapping: ' + d['folder'] + '/' + d['our_scan'])
    require(d['marked_in_H'] in {'yes', 'no'} and d['confidence'] in {'high', 'medium', 'low'},
            'Invalid H doubt/confidence metadata')
    require(d['scan_shows'] and d['line'], 'Missing H comparison evidence/place')

events = rows('CHECK_EVENTS.tsv')
expected_events = [event for record in accepted.values() for event in record.get('check_events', [])]
require(len(events) == len(expected_events), 'Check-event export count differs from accepted records')
event_ids = {event['statement_id'] for event in events}
event_types = {'targeted proof check', 'independent re-proof',
               'computation or formal certificate', 'used and rechecked in this run',
               'carried as background without fault found'}
for number, event in enumerate(events, 1):
    require(all(event[field].strip() for field in SCHEMAS['CHECK_EVENTS.tsv']),
            f'Incomplete check event {number}')
    require(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}:\d{2} UTC)?', event['date'])),
            f'Invalid check-event date {number}')
    event_type = event['type']
    if event_type.startswith('refuted, with '):
        refined = event_type[len('refuted, with '):]
        if refined.startswith('refined statement '):
            refined = refined[len('refined statement '):]
        require(refined in event_ids,
                f'Refutation has no recorded refined statement ID: event {number}')
    else:
        require(event_type in event_types, f'Unsupported check-event type {number}')
    # Several actual events may legitimately share the same statement ID.
notes = json.loads((ROOT / 'state/notes_consolidated.json').read_text())
require(set(notes) == set(PAGES) and all(notes.values()), 'Incomplete consolidated reading notes')
require(re.findall(r'^### (\d+_scan\d+)$', (ROOT / f'{PREFIX}_notes.md').read_text(), re.M) == PAGES,
        'Notes page coverage/order differs')

assignments = rows("state/assignments.tsv")
require([d["page"] for d in assignments] == PAGES, "Assignment order differs")
for d in assignments:
    first = d['first_reader'].split('/')[-1]
    second = d['second_reader'].split('/')[-1]
    require(bool(first) and bool(second) and first != second,
            f"Missing or non-independent second reader {d['page']}")
    record = accepted.get(d['page'], {})
    require(first == str(record.get('reader', '')).split('/')[-1] and
            second == str(record.get('auditor', '')).split('/')[-1],
            f'Assignment and accepted-reader identities differ for {d["page"]}')
progress = (ROOT / "progress.log").read_text()
require(len(re.findall(r"^scan \d+ audited ", progress, re.M)) == 24,
        "Expected24 completed audit log entries")
for status in ('done', 'audited'):
    logged = re.findall(r'^scan (\d+) ' + status + r' .*? cote (\d+)$', progress, re.M)
    logged_pages = [cote + '_scan' + scan.zfill(3) for scan, cote in logged]
    require(len(logged_pages) == 24 and set(logged_pages) == set(PAGES),
            f'Expected exactly one completed {status} log entry per page')
done_positions = [match.start() for match in re.finditer(r'^scan \d+ done ', progress, re.M)]
audit_positions = [match.start() for match in re.finditer(r'^scan \d+ audited ', progress, re.M)]
require(bool(done_positions) and bool(audit_positions) and max(done_positions) < min(audit_positions),
        'A second reading was accepted before all first readings were completed')

result = {"pages": len(accepted), "marks": len(decisions), "inventory": len(inventory),
          "H_collation_rows": len(collation), "check_events": len(events), "errors": ERRORS}
print(json.dumps(result, ensure_ascii=False, indent=2))
if ERRORS:
    sys.exit(1)
