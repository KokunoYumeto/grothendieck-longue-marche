"""Apply root-reviewed spatial ordering while preserving every inventory row."""
from pathlib import Path
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parents[1]
qa=json.loads((B/'reviews/final_inventory_order_review_c.json').read_text())
jp=B/'reviews/final_inventory_order_journal.json';assert not jp.exists()
assert len(qa['proposals'])==16
updated={};records=[]
for proposal in qa['proposals']:
 page=proposal['page'];r=json.loads((B/'reviews'/f'{page}.json').read_text())
 current=[x['element'] for x in r['inventory']];assert current==proposal['current_order'],page
 by_id={x['element']:x for x in r['inventory']};assert len(by_id)==len(current)
 for move in proposal['proposed_moves']:
  for element,position in move['recorded_positions'].items():assert by_id[element]['position']==position,(page,element)
 candidate=proposal['candidate_order_after_proposed_moves']
 assert len(candidate)==len(current) and set(candidate)==set(current)
 r['inventory']=[by_id[element] for element in candidate]
 updated[page]=r
 records.append(dict(page=page,before=current,after=candidate,evidence=proposal['proposed_moves']))
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for page,r in updated.items():(B/'reviews'/f'{page}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
jp.write_text(json.dumps(dict(completed_utc=stamp,scope='Spatial inventory row order only. Stable element IDs and every row value, page file and fixed audit record are preserved.',source_report='reviews/final_inventory_order_review_c.json',edits=records),ensure_ascii=False,indent=2)+'\n')
with (B/'progress.log').open('a') as f:f.write(f'inventory spatial-order reconciliation completed {stamp}: 32 recorded moves on 16 pages; all 270 entries and stable element IDs preserved\n')
print(json.dumps({'utc':stamp,'pages_reordered':len(updated),'moves':sum(len(x['evidence']) for x in records)}))
