#!/usr/bin/env python3
"""Retain actual interruption and GP parser failure before the corrected run."""
from pathlib import Path
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent
rows = []
for stem, sub, exit_code, reason in [
    ('quartic_five_division_field', 'whole_field_certification_interrupted', 130,
     'All literal field and torsion identities passed. bnfinit returned class number1; '
     'the long default bnfcertify was interrupted with Ctrl-C in actual session10724. '
     'No certified class number is asserted from this output. Exact character-subfield '
     'norm/extension maps give the subsequently pursued five-primary certification.'),
    ('quartic_five_character_fields', 'reserved_I_parser_failure', 0,
     'GP rejected assignment to its reserved I constant and skipped the calculation '
     'body. It then printed a misleading completion marker with zero fields and '
     'exited0. The output was immediately inspected and rejected; no mathematical '
     'certificate is claimed for this run.')
]:
    dest = root / 'history' / sub
    dest.mkdir(parents=True, exist_ok=False)
    files = []
    for ext in ['gp', 'out', 'bin']:
        src = root / (stem + '.' + ext)
        if src.exists():
            out = dest / src.name
            shutil.copy2(src, out)
            files.append({'file': out.name, 'bytes': out.stat().st_size,
                          'sha256': hashlib.sha256(out.read_bytes()).hexdigest()})
            if ext == 'bin':
                src.unlink()
    row = {'attempt': sub, 'actual_exit_code': exit_code,
           'status': 'INTERRUPTED' if exit_code == 130 else 'FAILED_VALIDATION',
           'reason': reason, 'files': files}
    (dest / 'provenance.json').write_text(json.dumps(row, indent=2) + '\n')
    rows.append(row)
print(json.dumps({'status': 'PASS', 'retained_actual_attempts': rows}, indent=2))
