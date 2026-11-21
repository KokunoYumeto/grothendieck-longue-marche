#!/usr/bin/env python3
"""Root-reviewed, source-only formatting plan. Prepared without execution.

Requires --apply and 25 completed audits. Does not compile TeX, regenerate
reports, or modify fixed readings, decisions, plans or historical receipts.
No snapshot whole-file hash is required: exact unique snippets and parsed
matrix selectors are checked against the sources present when this runs.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import re
import tempfile

BEGIN = r"\begin{tikzcd}"
END = r"\end{tikzcd}"
CONTROL = re.compile(r"\\(?:[A-Za-z@]+|.)", re.S)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def command_end(text, pos):
    match = CONTROL.match(text, pos)
    return match.end() if match else pos + 1


def mask_comments(text):
    out = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i = command_end(text, i)
        elif text[i] == "%":
            j = text.find("\n", i)
            if j < 0:
                j = len(text)
            out[i:j] = " " * (j - i)
            i = j
        else:
            i += 1
    return "".join(out)


def option_end(text, pos):
    """Return one past an option's closing ], respecting TeX brace groups."""
    assert text[pos] == "["
    braces = 0
    i = pos + 1
    while i < len(text):
        if text[i] == "\\":
            i = command_end(text, i)
            continue
        if text[i] == "{":
            braces += 1
        elif text[i] == "}":
            braces -= 1
        elif text[i] == "]" and braces == 0:
            return i + 1
        if braces < 0:
            raise ValueError("Malformed option group")
        i += 1
    raise ValueError("Unclosed option")


def split_option_parts(content):
    parts = []
    start = 0
    braces = 0
    i = 0
    while i < len(content):
        if content[i] == "\\":
            i = command_end(content, i)
            continue
        if content[i] == "{":
            braces += 1
        elif content[i] == "}":
            braces -= 1
        elif content[i] == "," and braces == 0:
            parts.append(content[start:i])
            start = i + 1
        i += 1
    if braces:
        raise ValueError("Unbalanced matrix option groups")
    parts.append(content[start:])
    return parts


def matrix_header(text, start):
    begin_end = start + len(BEGIN)
    pos = begin_end
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos < len(text) and text[pos] == "[":
        end = option_end(text, pos)
        content = text[pos + 1:end - 1]
        parts = split_option_parts(content)
        amp_parts = [p for p in parts if re.match(r"\s*ampersand replacement\s*=", p)]
        if len(amp_parts) > 1:
            raise ValueError("Repeated ampersand replacement option")
        amp = None
        if amp_parts:
            amp = amp_parts[0].split("=", 1)[1].strip()
            if amp != r"\&":
                raise ValueError("Nonstandard ampersand replacement needs review")
        remaining = [p for p in parts if p not in amp_parts]
        canonical = BEGIN
        if remaining and any(p.strip() for p in remaining):
            canonical += text[begin_end:pos] + "[" + ",".join(remaining) + "]"
        return end, text[start:end], canonical, amp
    return begin_end, BEGIN, BEGIN, None


def matrices(text):
    masked = mask_comments(text)
    matches = list(re.finditer(re.escape(BEGIN) + "|" + re.escape(END), masked))
    opened = None
    result = []
    for match in matches:
        if match.group() == BEGIN:
            if opened is not None:
                raise ValueError("Nested tikzcd requires review")
            opened = match.start()
        else:
            if opened is None:
                raise ValueError("Unmatched tikzcd end")
            body_start, head, canonical, amp = matrix_header(text, opened)
            result.append({
                "start": opened, "end": match.end(),
                "body_start": body_start, "body_end": match.start(),
                "header": head, "canonical_header": canonical, "amp": amp,
                "canonical_block": canonical + text[body_start:match.end()],
            })
            opened = None
    if opened is not None:
        raise ValueError("Unclosed tikzcd")
    return result


def repair_cell_tokens(body):
    """Replace only top-level matrix cell separators; preserve all other bytes."""
    masked = mask_comments(body)
    out = []
    braces = 0
    count = 0
    i = 0
    while i < len(body):
        if body[i] == "\\":
            end = command_end(body, i)
            token = body[i:end]
            # An & inside an arrow option is not assumed to be a cell separator.
            after = end
            while after < len(body) and body[after].isspace():
                after += 1
            if token == r"\arrow" and after < len(body) and body[after] == "[":
                opt_end = option_end(masked, after)
                option = masked[after:opt_end]
                if re.search(r"(?<!\\)&", option):
                    raise ValueError("Raw ampersand in arrow options needs review")
                end = opt_end
            out.append(body[i:end])
            i = end
            continue
        if masked[i] != body[i]:  # comment bytes
            out.append(body[i])
            i += 1
            continue
        if body.startswith("|[", i):
            end = option_end(masked, i + 1)
            if re.search(r"(?<!\\)&", masked[i:end]):
                raise ValueError("Raw ampersand in a cell option needs review")
            out.append(body[i:end])
            i = end
            continue
        if body[i] == "{":
            braces += 1
        elif body[i] == "}":
            braces -= 1
        if braces < 0:
            raise ValueError("Unexpected closing group in matrix body")
        if body[i] == "&":
            if braces != 0:
                raise ValueError("Raw ampersand inside a cell group needs review")
            out.append(r"\&")
            count += 1
        else:
            out.append(body[i])
        i += 1
    if braces:
        raise ValueError("Unbalanced matrix cell groups")
    return "".join(out), count


def literal_replace(text, item, log):
    old_count = text.count(item["old"])
    new_count = text.count(item["new"])
    if old_count == 1 and new_count == 0:
        log.append({"id": item["id"], "old": item["old"], "new": item["new"]})
        return text.replace(item["old"], item["new"], 1)
    if old_count == 0 and new_count == 1:
        return text  # already applied, without weakening uniqueness checks
    raise ValueError("Expected one exact old or already-applied new snippet: " + item["id"])



def main():
    parser = argparse.ArgumentParser(description='Apply root-approved source-only TeX formatting, without aggregation or compilation.')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if not args.apply:
        parser.error('No changes made; --apply is required.')
    here = Path(__file__).resolve().parent
    root = here.parent
    plan_path = here / 'reader_a_tex_static_patch_plan_final.json'
    plan = json.loads(plan_path.read_text())
    order = (root / 'work/scripts/page_order.txt').read_text().splitlines()
    if len(order) != 25 or len(set(order)) != 25:
        raise SystemExit('Unexpected page list')
    for page in order:
        report = json.loads((root / 'work/reports' / page / 'report.json').read_text())
        if not report.get('audited_utc') or not report.get('second_reader') or report['second_reader'] == report['reader']:
            raise SystemExit('Audit gate failed: ' + page)
    if 'transcription frozen' in (root / 'work/progress.log').read_text().lower():
        raise SystemExit('Source already frozen; no changes made.')
    prepared = []
    for page in order:
        rel = 'work/pages/' + page + '.tex'
        path = root / rel
        if path.is_symlink():
            raise SystemExit('Symlink source refused: ' + rel)
        before = path.read_bytes()
        text = before.decode('utf-8')
        envs = matrices(text)
        specs = [x for x in plan['matrix_selectors'] if x['file'] == rel]
        if len(envs) != len(specs):
            raise ValueError('Matrix set changed: ' + page)
        replacements = []
        logs = []
        matched = set()
        for spec in specs:
            found = [e for e in envs if e['canonical_block'].startswith(spec['unique_marker'])]
            if len(found) != 1 or found[0]['start'] in matched:
                raise ValueError('Nonunique matrix selector: ' + spec['id'])
            e = found[0]
            matched.add(e['start'])
            new_body, count = repair_cell_tokens(text[e['body_start']:e['body_end']])
            new_header = e['header']
            if count and e['amp'] is None:
                if new_header == BEGIN:
                    new_header += r'[ampersand replacement=\&]'
                else:
                    at = new_header.index('[')
                    new_header = new_header[:at+1] + r'ampersand replacement=\&,' + new_header[at+1:]
            old = text[e['start']:e['end']]
            new = new_header + new_body + END
            if old != new:
                replacements.append((e['start'], e['end'], new))
                logs.append({'id': spec['id'], 'old': old, 'new': new, 'cell_separators_retokenized': count})
        for start, end, new in reversed(replacements):
            text = text[:start] + new + text[end:]
        for item in plan['literal_operations'] + plan['wrapper_operations']:
            if item['file'] == rel:
                text = literal_replace(text, item, logs)
        for e in matrices(text):
            _, remaining = repair_cell_tokens(text[e['body_start']:e['body_end']])
            if remaining:
                raise ValueError('Unrepaired raw matrix separators: ' + page)
        if r'\diagram{\begin{tikzpicture}' in text or r'\diagram{\[\begin{array}' in text or r'\diagram{$\begin{array}' in text:
            raise ValueError('A reviewed diagram wrapper conversion is missing: ' + page)
        after = text.encode('utf-8')
        if after != before:
            prepared.append((path, before, after, logs))
    receipt_path = root / 'work/reports/tex_integration_receipt.json'
    if receipt_path.exists():
        raise SystemExit('Receipt exists; refusing to overwrite it.')
    timestamp = datetime.now(timezone.utc).isoformat()
    receipt = {
        'started_utc': timestamp,
        'authorization': 'Root approved the two doubt groupings, raw matrix ampersand repair and five exact content-preserving wrapper conversions after all25 audits.',
        'scope': plan['approved_scope'],
        'plan': str(plan_path.relative_to(root)),
        'plan_sha256': sha(plan_path.read_bytes()),
        'combined_status': 'Deferred by root instruction. No aggregate or combined-source write performed; root will regenerate the combined fragment later.',
        'compilation': 'Not performed; source-level checks only.',
        'status': 'validated; applying',
        'files': [{'path': str(path.relative_to(root)), 'before_sha256': sha(before), 'after_sha256': sha(after), 'operations': logs, 'applied': False}
                  for path,before,after,logs in prepared]
    }
    with receipt_path.open('x', encoding='utf-8') as stream:
        json.dump(receipt, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    staged = []
    try:
        for path,before,after,logs in prepared:
            fd,tmp_name = tempfile.mkstemp(prefix='tex_final_',suffix='.tex',dir=here)
            tmp = Path(tmp_name)
            with os.fdopen(fd,'wb') as stream:
                stream.write(after)
            os.chmod(tmp,path.stat().st_mode & 0o777)
            staged.append((path,before,after,tmp))
        for index,(path,before,after,tmp) in enumerate(staged):
            if path.read_bytes() != before:
                raise RuntimeError('Concurrent change before write: ' + str(path))
            os.replace(tmp,path)
            if path.read_bytes() != after:
                raise RuntimeError('Written bytes differ: ' + str(path))
            receipt['files'][index]['applied'] = True
            receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        receipt['status'] = 'applied'
        receipt['completed_utc'] = datetime.now(timezone.utc).isoformat()
    except Exception as exc:
        receipt['status'] = 'interrupted; inspect per-file applied flags'
        receipt['error'] = repr(exc)
        raise
    finally:
        for path,before,after,tmp in staged:
            if tmp.exists(): tmp.unlink()
        receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print('Applied source-only formatting to',len(prepared),'page files.')
    print('Receipt:',receipt_path)
    print('Combined/aggregates/fixed readings left unchanged.')


if __name__ == '__main__':
    main()
