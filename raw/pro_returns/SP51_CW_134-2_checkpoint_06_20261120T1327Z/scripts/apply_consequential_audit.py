"""Apply root's accepted written-record audit; no transcription or image operations."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
updates={
 172:{5:'Against H: restores the specified sheaf coefficients, sets or modules, left unread in H, and attaches the parenthesis to faisceaux. The C-side differences here concern punctuation and doubt resolution.'},
 175:{19:r'Against H: restores the left comparison glyph as \underline{\approx}, two waves above a straight rule, rather than \simeq. This corrects the mathematical sign without assigning a different equivalence semantics.',23:r'Against H: restores the right comparison glyph before X_1 as \underline{\approx}, two waves above a straight rule, rather than \simeq; its exact semantic convention is not inferred.'},
 178:{5:'Against H: removes the two supplied terminal object bullets from the corner diagram. The ink has one source point and two outgoing arrows with unwritten targets; no mathematical absence of target objects is asserted.'}
}
for n,rows in updates.items():
 p=root/f'records/scan{n}/decision.json'
 d=json.loads(p.read_text())
 for i,value in rows.items():
  assert d['differences'][i]['differs_H']
  d['differences'][i]['consequential']=value
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Accepted consequential-correction annotations applied to scans 172, 175 and 178; transcription unchanged.')
