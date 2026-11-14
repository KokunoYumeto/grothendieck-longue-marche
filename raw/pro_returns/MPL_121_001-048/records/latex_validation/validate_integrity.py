#!/usr/bin/env python3
"""Report page-file, scan-marker, brace, and custom-macro integrity."""
from pathlib import Path
import argparse
from datetime import datetime, timezone
import hashlib
import json
import re

EXPECTED = [n for n in range(1,49) if n not in {3,25,29,38,40}]
ALLOWED = {'cotefile','scanpage','mspage','deleted','inserted','margin',
           'uline','uuline','diagram','figure','unsure','illegible'}
FORBIDDEN = {'documentclass','usepackage','newcommand','renewcommand','def',
             'gdef','includegraphics','input','include'}


def scan_tokens(text):
    stack, commands, issues = [], [], []
    i = 0
    while i < len(text):
        character = text[i]
        if character == '%':
            end = text.find('\n',i)
            i = len(text) if end < 0 else end+1
            continue
        if character == '\\':
            match = re.match(r'\\([A-Za-z@]+|.)',text[i:],flags=re.S)
            if match:
                commands.append((match.group(1),i,i+len(match.group(0))))
                i += len(match.group(0))
                continue
        if character == '{':
            stack.append(i)
        elif character == '}':
            if stack:
                stack.pop()
            else:
                issues.append(f'Unmatched closing brace at character {i}')
        i += 1
    issues += [f'Unclosed brace at character {position}' for position in stack]
    return commands, issues


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-root',type=Path,default=here.parents[1])
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    package = args.package_root.resolve()
    files = sorted((package/'pages').glob('*.tex'))
    actual = [int(re.search(r'scan(\d+)\.tex$',p.name).group(1)) for p in files]
    issues = [] if actual == EXPECTED else ['Page-file set differs from retained scans']
    counts = {name:0 for name in sorted(ALLOWED)}
    rows = []
    for page in files:
        data = page.read_bytes()
        text = data.decode('utf-8')
        commands, balance_issues = scan_tokens(text)
        local = list(balance_issues)
        for command,start,end in commands:
            if command in ALLOWED:
                counts[command] += 1
                if not text[end:].lstrip().startswith('{'):
                    local.append(f'Custom macro {command} lacks a braced argument at character {start}')
            if command in FORBIDDEN:
                local.append(f'Forbidden fragment-level declaration/input macro {command}')
        scan = int(re.search(r'scan(\d+)\.tex$',page.name).group(1))
        if re.findall(r'\\scanpage\{(\d+)\}',text) != [str(scan)]:
            local.append('Scan marker differs from filename')
        rows.append({'file':str(page.relative_to(package)),'scan':scan,'bytes':len(data),
                     'sha256':hashlib.sha256(data).hexdigest(),
                     'balanced_braces':not balance_issues,'issues':local})
        issues += [page.name+': '+issue for issue in local]
    combined = package/'MPL_121_001-048_transcription.tex'
    data = combined.read_bytes()
    scan_order = [int(v) for v in re.findall(r'\\scanpage\{(\d+)\}',data.decode('utf-8'))]
    if scan_order != EXPECTED:
        issues.append('Combined scan-marker order differs from retained scans')
    result = {
        'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'expected_scans':EXPECTED,'page_file_count':len(files),
        'custom_macro_occurrences':counts,'issues':issues,'pages':rows,
        'combined':{'file':combined.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                    'scan_markers_in_expected_order':scan_order==EXPECTED},
    }
    encoded = json.dumps(result,indent=2)
    if args.output:
        args.output.write_text(encoded,encoding='utf-8')
    print(json.dumps({'pages':len(files),'issues':issues}))
    if issues:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
