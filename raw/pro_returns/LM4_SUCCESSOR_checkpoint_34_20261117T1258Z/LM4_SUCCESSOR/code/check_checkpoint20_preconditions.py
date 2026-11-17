"""Check the final unchanged PDF and required capture inputs before checkpoint20 exists."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
metrics=json.loads((root/'records/checkpoint20_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==metrics['pdf_sha256']
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_20.zip').exists()
for name in ['checkpoint20_typesetting.txt','checkpoint20_writer_pause.md',
             'checkpoint20_computation_audit_state.md','checkpoint20_late_root_reviews.json']:
    assert (root/'records'/name).is_file()
assert (root/'LM4_SUCCESSOR_report.md').read_text().startswith('INCOMPLETE\n')
print('All immutable-capture preconditions present; final PDF hash unchanged; checkpoint20 does not yet exist.')
