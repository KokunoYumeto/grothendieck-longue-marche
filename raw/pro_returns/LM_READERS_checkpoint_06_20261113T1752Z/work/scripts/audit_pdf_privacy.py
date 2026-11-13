#!/usr/bin/env python3
"""Audit the exact PDFs proposed by package_release.final_maps(), without edits.

The report contains archive-relative names and hashes, never private filesystem
paths or the literal content of a privacy finding. A successful audit covers
document metadata, extracted page text, non-stream PDF object dictionaries and
their decoded strings, and absence of embedded files. Font/image stream bytes
are outside this scope.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

import pymupdf as fitz

from package_release import final_maps
from verify_pdf import ROOT, sha256


PATTERNS = (
    ('local_path', re.compile(r'/(?:workspace|home|root|usr|opt|tmp|var|mnt|Users)/[^\s"\'<>]+', re.I)),
    ('windows_path', re.compile(r'(?<![\w\\])[A-Za-z]:[\\/](?:Users|Windows|Program Files(?: \(x86\))?|texlive|workspace|home|Temp|tmp)(?:[\\/][^\s\n]*)?', re.I)),
    ('email_address', re.compile(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')),
)


def pdf_strings(source):
    """Yield decoded literal/hex string values from MuPDF's object serialization.

    MuPDF supplies the dictionary syntax. This small lexer handles balanced
    parentheses, PDF backslash/octal escapes, line continuations and hex strings
    so that an escaped Windows path is not missed by testing serialized text.
    """
    i = 0
    while i < len(source):
        data = None
        if source[i] == '(':
            i += 1
            depth = 1
            data = bytearray()
            while i < len(source) and depth:
                char = source[i]
                i += 1
                if char == '\\' and i < len(source):
                    escaped = source[i]
                    i += 1
                    if escaped in '\r\n':
                        if escaped == '\r' and i < len(source) and source[i] == '\n':
                            i += 1
                        continue
                    if escaped in '01234567':
                        digits = escaped
                        while i < len(source) and len(digits) < 3 and source[i] in '01234567':
                            digits += source[i]
                            i += 1
                        data.append(int(digits, 8) & 255)
                    else:
                        value = {'n': '\n', 'r': '\r', 't': '\t', 'b': '\b', 'f': '\f'}.get(escaped, escaped)
                        data.extend(value.encode('latin-1', errors='replace'))
                elif char == '(':
                    depth += 1
                    data.append(ord(char))
                elif char == ')':
                    depth -= 1
                    if depth:
                        data.append(ord(char))
                else:
                    data.extend(char.encode('latin-1', errors='replace'))
        elif source[i:i + 2] == '<<':
            i += 2
        elif source[i] == '<':
            end = source.find('>', i + 1)
            if end < 0:
                break
            value = re.sub(r'\s+', '', source[i + 1:end])
            i = end + 1
            if re.fullmatch(r'[0-9A-Fa-f]*', value):
                if len(value) % 2:
                    value += '0'
                data = bytearray.fromhex(value)
        else:
            i += 1
        if data is not None:
            raw = bytes(data)
            if raw.startswith((b'\xfe\xff', b'\xff\xfe')):
                yield raw.decode('utf-16', errors='replace')
            else:
                yield raw.decode('utf-8', errors='replace')


def scan_text(value, location):
    seen = set()
    # URI percent encoding can otherwise conceal a local path or mail address.
    variants = [value, unquote(value), unquote(unquote(value))]
    for text in variants:
        for kind, pattern in PATTERNS:
            for match in pattern.finditer(text):
                fingerprint = hashlib.sha256(match.group(0).encode()).hexdigest()
                key = (kind, fingerprint)
                if key not in seen:
                    seen.add(key)
                    yield {'kind': kind, 'location': location, 'match_sha256': fingerprint,
                           'content_redacted': True}


def inspect_pdf(path):
    result = {'pages': 0, 'object_count': 0, 'embedded_file_count': 0, 'findings': []}
    try:
        with fitz.open(path) as doc:
            if doc.needs_pass:
                result['findings'].append({'kind': 'encrypted_pdf_requires_review'})
                return result
            result['pages'] = len(doc)
            result['object_count'] = max(doc.xref_length() - 1, 0)
            result['embedded_file_count'] = doc.embfile_count()
            if result['embedded_file_count']:
                result['findings'].append({'kind': 'embedded_file_requires_review',
                                           'count': result['embedded_file_count']})
            result['findings'].extend(scan_text(json.dumps(doc.metadata, ensure_ascii=False), 'metadata'))
            result['findings'].extend(scan_text(doc.get_xml_metadata(), 'xml_metadata'))
            for number, page in enumerate(doc, 1):
                result['findings'].extend(scan_text(page.get_text(), 'page_text:' + str(number)))
            for xref in range(1, doc.xref_length()):
                value = doc.xref_object(xref, compressed=False)
                location = 'object:' + str(xref)
                result['findings'].extend(scan_text(value, location))
                for decoded in pdf_strings(value):
                    result['findings'].extend(scan_text(decoded, location + ':decoded_string'))
    except Exception as exc:
        # Exception messages may include an absolute source path: expose the
        # error class only, while retaining the safe archive/path context.
        result['findings'].append({'kind': 'pdf_read_error', 'error_type': type(exc).__name__})
    unique = {json.dumps(f, sort_keys=True): f for f in result['findings']}
    result['findings'] = list(unique.values())
    return result


def audit():
    rows = []
    for archive, items in sorted(final_maps().items()):
        for name, (source, role) in sorted(items.items()):
            if Path(name).suffix.lower() == '.pdf':
                if isinstance(source, bytes):
                    raise TypeError('Mapped PDF input must have a source file for stability checks')
                rows.append((archive, name, Path(source)))

    before = {}
    for _, _, source in rows:
        try:
            before[source] = sha256(source)
        except OSError:
            before[source] = None

    files = []
    cache = {}
    for archive, name, source in rows:
        if source not in cache:
            cache[source] = inspect_pdf(source)
        files.append({'archive': archive, 'path': name, 'sha256': before[source],
                      **cache[source]})

    # Recheck all initial hashes after all PDF reads, not only immediately after
    # each file: any detected concurrent rebuild invalidates this snapshot.
    after = {}
    for _, _, source in rows:
        try:
            after[source] = sha256(source)
        except OSError:
            after[source] = None
    all_findings = []
    for row, (_, _, source) in zip(files, rows):
        row['sha256_after'] = after[source]
        row['stable_during_audit'] = before[source] is not None and before[source] == after[source]
        # Copy the findings list before appending; cached source entries may be
        # represented by more than one archive-relative path.
        row['findings'] = list(row['findings'])
        if not row['stable_during_audit']:
            row['findings'].append({'kind': 'input_missing_or_changed_during_audit'})
        all_findings.extend({'archive': row['archive'], 'path': row['path'], **f}
                            for f in row['findings'])

    inventory = [{k: row[k] for k in ('archive', 'path', 'sha256')} for row in files]
    return {'status': 'PASS' if files and not all_findings else 'FAIL',
            'scope': 'All PDF entries from package_release.final_maps(): standard and XML metadata, extracted page text, every non-stream PDF object dictionary and decoded literal/hex string (including annotations/actions), URI percent decoding, and embedded-file absence. Binary font/image streams are not interpreted. Local-root patterns include workspace, home, root, usr, opt, tmp, var, mnt, Users, and common Windows roots in either slash form. Every source hash is frozen before all reads and checked again afterward.',
            'generated_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'backend': {'pymupdf': fitz.VersionBind, 'mupdf': fitz.VersionFitz},
            'mapped_pdf_inventory_sha256': hashlib.sha256(json.dumps(inventory, sort_keys=True).encode()).hexdigest(),
            'file_count': len(files), 'page_count': sum(f['pages'] for f in files),
            'object_count': sum(f['object_count'] for f in files),
            'embedded_file_count': sum(f['embedded_file_count'] for f in files),
            'files': files, 'findings': all_findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='work/data/pdf_privacy_audit.json',
                        help='JSON report path, relative to the project root unless absolute')
    args = parser.parse_args()
    result = audit()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'file_count', 'page_count', 'object_count', 'embedded_file_count')}
                     | {'finding_count': len(result['findings'])}))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
