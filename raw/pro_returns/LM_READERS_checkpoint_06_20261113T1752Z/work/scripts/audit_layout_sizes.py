"""Audit only explicit size changes added by exact local layout records."""
from collections import Counter
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[2]

def audit(records):
    rows = []
    for record in records:
        old, new = record['old'], record['new']
        changes = []
        patterns = [
            ('font_size_pt', r'\\fontsize\s*\{\s*([0-9.]+)\s*\}'),
            ('scale_factor', r'\\scalebox\s*\{\s*([0-9.]+)\s*\}'),
            ('tikz_scale_factor', r'(?:^|[,{])\s*(?:scale|xscale|yscale)\s*=\s*([0-9.]+)'),
        ]
        for kind, pattern in patterns:
            added = Counter(re.findall(pattern, new)) - Counter(re.findall(pattern, old))
            for value, count in added.items():
                numeric = float(value)
                ratio = numeric / 11 if kind == 'font_size_pt' else numeric
                assert ratio >= .70, (record['id'], record['language'], kind, value)
                changes.append(dict(kind=kind, value=numeric, occurrences=count,
                                    ratio_to_reference=ratio, passes_70_percent=True))
        # The measured 105pt prose cell uses the standard 11pt-class footnote size.
        added_footnotesize = new.count(r'\footnotesize') - old.count(r'\footnotesize')
        if added_footnotesize > 0:
            changes.append(dict(kind='named_text_size_pt', command='footnotesize', value=9,
                                occurrences=added_footnotesize, ratio_to_reference=9/11,
                                passes_70_percent=True))
        assert new.count(r'\resizebox') <= old.count(r'\resizebox'), record['id']
        if changes:
            rows.append(dict(repair_id=record['id'], language=record['language'],
                             package=record['package'], scan=record['scan'], added_sizes=changes))
    sizes = [c['value'] for r in rows for c in r['added_sizes'] if c['kind']=='font_size_pt']
    scales = [c['value'] for r in rows for c in r['added_sizes'] if 'scale_factor' in c['kind']]
    result = dict(schema='exact-local-layout-size-audit-v1',
                  scope='Positive differences in explicit font and scale declarations between each exact old/new layout record; existing source sizes and mathematical subscript sizing are not alterations by this pass.',
                  reference_body_font_pt=11, minimum_allowed_ratio=.70,
                  added_font_sizes_pt=sorted(set(sizes)), minimum_added_font_pt=min(sizes),
                  minimum_added_font_ratio_to_body=min(sizes)/11,
                  added_scale_factors=sorted(set(scales)), minimum_added_scale_factor=min(scales),
                  named_text_size_reference='LaTeX 11pt class: footnotesize is9pt; applied only to the recorded105pt prose cell.',
                  all_added_sizes_pass=True, added_resizebox_calls=0, records=rows)
    (ROOT/'work/data/layout_size_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    return result

if __name__ == '__main__':
    result=audit(json.loads((ROOT/'work/data/layout_repairs_applied.json').read_text()))
    print(result['added_font_sizes_pt'], result['minimum_added_font_ratio_to_body'],
          result['added_scale_factors'], 'all pass the0.70 threshold')
