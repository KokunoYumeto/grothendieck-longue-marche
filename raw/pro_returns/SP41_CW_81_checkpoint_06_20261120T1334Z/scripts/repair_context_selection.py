"""Restore page-specific C context rows with comma-qualified scan fields.

This deterministic input extraction performs no transcription or ink reading.
Earlier packets and all final page files remain unchanged.
"""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[2]
changes=[]
for n in range(42,56):
 p=root/f'runtime_inputs/scan{n:03d}/packet.json'
 d=json.loads(p.read_text());folder=d['folder']
 source=root/f'source/SP41_CW_81_witnesses/codex/{folder}/{folder}_doubts.md'
 rows=[s for s in source.read_text().splitlines() if re.match(r'\|\s*0*'+str(n)+r'(?:\s*\||\s*,)',s)]
 target=Path(d['C_context']);old=target.read_text()
 marker='Folder-wide C notes are held by the main reader;'
 tail=old[old.index(marker):]
 text='# Witness C page-specific doubt and notation rows\n\n'+'\n'.join(rows)+'\n\n'+tail
 target.write_text(text)
 changes.append({'scan':n,'selected_rows':len(rows),'old_selected_rows':sum(s.startswith('|') for s in old.splitlines()),'method':'Exact first-column scan identifier, accepting a following comma or column boundary.'})
(root/'work/validation/context_selection_repair.json').write_text(json.dumps({'reason':'J81-06 identifies rows as 42, locus within the first column; the earlier extractor required a column boundary immediately after the scan. Repaired at the start of scan042 and supplied to its three running readers.','affected_packets':changes,'page_text_files_changed':False},indent=2))
print(json.dumps(changes))
