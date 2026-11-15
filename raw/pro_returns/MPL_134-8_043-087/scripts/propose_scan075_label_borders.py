#!/usr/bin/env python3
"""Prepare the two label borders requested by the principal reader.

Only existing TikZ label-node options are extended. Every original byte is
retained in its existing order, and removing the two added option groups must
recover the complete source file exactly. No live page is changed.
"""
from pathlib import Path
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / 'pages' / 'MPL_134-8_043-087_134-8_scan075.tex'
MIRROR = ROOT.parent / 'texqa-cache' / 'label-border-proposal'
LABELS = [
    {
        'name': 'upper label',
        'content': r'\begin{array}{l}\text{Si }M,N\text{ asph. i.e.}\\\kappa_{M!}(1_M)\simeq k\\\kappa_{N!}(1_N)\simeq k\end{array}',
        'options': '{draw,ellipse,inner sep=2pt}',
        'border': 'ellipse',
    },
    {
        'name': 'lower label',
        'content': r'\begin{array}{l}\text{Si }M,N\text{ asph}\\\text{et en plus pour }x\text{ projectif en }N\\x\longrightarrow\kappa_N^*\kappa_{N!}x\quad\text{\uline{épi}}\end{array}',
        'options': '{draw,rectangle,rounded corners=3pt,inner sep=2pt}',
        'border': 'rounded rectangle',
    },
]


def main():
    original_bytes = PAGE.read_bytes()
    original = original_bytes.decode('utf-8')
    updated = original
    manifest = []
    for item in LABELS:
        old = '"{' + item['content'] + '}"' + "'"
        new = old + item['options']
        if new in updated:
            continue
        if updated.count(old) != 1:
            raise ValueError('The ' + item['name'] + ' no longer matches the principal reader’s specified source label.')
        position = updated.index(old)
        updated = updated.replace(old, new, 1)
        manifest.append({'label': item['name'], 'border': item['border'],
                         'line': original.count('\n', 0, original.index(old)) + 1,
                         'unchanged_label_content': item['content'],
                         'label_content_sha256': hashlib.sha256(item['content'].encode('utf-8')).hexdigest(),
                         'added_options': item['options']})
    recovered = updated
    for item in reversed(LABELS):
        old = '"{' + item['content'] + '}"' + "'"
        new = old + item['options']
        if new not in original:
            recovered = recovered.replace(new, old, 1)
    if recovered != original:
        raise AssertionError('Removing the added border options did not recover the exact original file')
    MIRROR.mkdir(parents=True, exist_ok=True)
    (MIRROR / PAGE.name).write_text(updated)
    label = 'pages/' + PAGE.name
    patch = ''.join(difflib.unified_diff(original.splitlines(keepends=True),
                                       updated.splitlines(keepends=True),
                                       fromfile='a/' + label, tofile='b/' + label))
    (ROOT / 'records' / 'proposed_scan075_label_borders.patch').write_text(patch)
    record = {'file': label, 'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
              'proposed_sha256': hashlib.sha256(updated.encode('utf-8')).hexdigest(),
              'all_original_bytes_retained_in_order': True,
              'exact_inverse_by_removing_added_options': True,
              'changes': manifest}
    (ROOT / 'records' / 'proposed_scan075_label_borders.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('Prepared', len(manifest), 'label borders; all original words and arrow options retained.')
    print('Live scan 075 was not changed.')


if __name__ == '__main__':
    main()
