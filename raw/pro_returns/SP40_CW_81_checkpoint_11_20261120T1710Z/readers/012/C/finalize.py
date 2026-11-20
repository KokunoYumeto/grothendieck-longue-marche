from pathlib import Path
from datetime import datetime, timezone
import json

O = Path('/workspace/scratch/94548b74fbe0/out/readers/012/C')
checks = json.loads((O / 'structural_checks.json').read_text())
assert checks['overall_pass']
report = json.loads((O / 'report.json').read_text())
end = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
report['end_utc'] = end
report['structural_verification'] = {
    'path': 'structural_checks.json',
    'overall_pass': True,
    'source_paths': 68,
    'source_labels': 8,
    'new_mark_entries': 31,
    'crop_count': 17,
    'original_C_doubt_rows': 3,
    'qualification': 'Source-level structure and record synchronization checked; no compilation or rendering performed.'
}
(O / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
(O / 'end_utc.txt').write_text(end + '\n')
md = (O / 'reading.md').read_text()
md += '\n## Completion and structural verification\n\n'
md += f'End UTC: {end}\n\n'
md += ('All source checks pass. The 68 original contour blocks and eight labels occur exactly once; '
       'the 31 added visible-mark records agree across TeX anchors, differences, doubts, inventory, '
       'and crop references. All 17 crop paths exist and the report matches the crop manifest. '
       'The three original C doubt rows remain explicitly mapped, including the local geometric '
       'and state subloci of the compound third row. Delimiters, environments, macro vocabulary, '
       'inventory coverage, abbreviation fields, and page-boundary restrictions pass their checks. '
       'The complete check output is in `structural_checks.json`. No compilation, rendering, '
       'or mathematical computation was performed.\n')
(O / 'reading.md').write_text(md)
print(json.dumps({'end_utc': end, 'overall_pass': True, 'crop_count': 17,
                  'source_paths': 68, 'source_labels': 8, 'new_mark_entries': 31}, indent=2))
