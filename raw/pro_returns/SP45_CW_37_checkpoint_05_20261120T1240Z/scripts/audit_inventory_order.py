#!/usr/bin/env python3
"""Record-only ordering repair from already recorded scan 018 positions.

No source image is opened, and no transcription file is modified.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[1]
p=R/'decisions/scan018.json';d=json.loads(p.read_text())
if d.get('inventory_order_audit'):
    print('Scan 018 inventory ordering audit already applied.')
else:
    inv=d['inventory'];assert len(inv)==71
    order=list(range(44))+[44,65,45,46,47,48,49,66,67,50,51,68,52,53,69,54,70,55,56,57,58,59,60,61,62,63,64]
    assert sorted(order)==list(range(71))
    fixed=[inv[i] for i in order]
    note='Record-only inventory audit after scan 025: six late-added cells (NB B, passage overprint, second sûr, and three raised ordinal-o forms) were moved into their already-recorded paragraph positions. Existing element IDs and transcription text are unchanged; no image was reopened.'
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    for f in [p,R/'decisions/approved_scan018_config.json']:
        x=json.loads(f.read_text());x['inventory']=fixed;x['inventory_order_audit']={'date':now,'basis':note,'original_index_order':order};x['workflow_observation']+=' '+note;f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
    with (R/'progress.log').open('a') as f:f.write('inventory order audit scan 018 '+now+'; records only, transcription unchanged\n')
    print(note)
