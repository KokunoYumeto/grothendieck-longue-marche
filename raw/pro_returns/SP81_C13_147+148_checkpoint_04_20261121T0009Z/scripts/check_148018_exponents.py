"""Evaluate the two graphically retained exponent candidates, without choosing ink."""
from pathlib import Path
from datetime import datetime, timezone
import json

result = {
    'checked_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'evaluations': [{'exponent': e, 'power': 2**e, 'power_minus_one': 2**e-1}
                    for e in (4, 9)],
    'written_right_side': 15,
    'scope': 'Integer evaluation only; source exponent remains 9|4 from its closed loop and right stem.'
}
assert result['evaluations'] == [
    {'exponent': 4, 'power': 16, 'power_minus_one': 15},
    {'exponent': 9, 'power': 512, 'power_minus_one': 511}]
(Path(__file__).resolve().parents[1]/'work/148018_exponents_check.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
