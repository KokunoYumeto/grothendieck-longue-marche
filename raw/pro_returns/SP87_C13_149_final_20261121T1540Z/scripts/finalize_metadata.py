"""Reconcile static metadata findings only; never alter page or blind-reading bytes."""
from pathlib import Path
import json
from datetime import datetime,timezone
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
for s,did,old,new in [
 (79,'D0027','live_index',dict(disposition='certainty-only resolution',change_place=None,reason="The index is resolved to1 in M1218 and certainty_resolutions/live_index. H and C's preferred branch agree; no substantive collation row is counted.")),
 (89,'D0282','final_underlined_letter',dict(disposition='macro/editorial convention and retained mark',change_place=None,reason='The source underline and O/U uncertainty remain in M1247. The removed final_underlined_letter row represented the underline/mathcal-O convention rather than a substantive lexical difference; no collation row is counted.'))]:
 p=w/'review'/f'149_scan{s:03d}_reviewed.json';r=json.loads(p.read_text());d=next(d for d in r['diff_coverage'] if d['diff_id']==did)
 assert d['change_place']==old
 d.update(new);p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'review/149_scan090_reviewed.json';r=json.loads(p.read_text())
updates={
 '090.kappa':(r'\kappa_i\text{ preferred, at both occurrences}',r'\unsure{\kappa|k}_i'),
 '090.f_deleted_words':('désigne ... aussi',r'\deleted{\unsure{désigne|désignons} \unsure{aussi}}'),
 '090.f_deleted_formula':('lower exists i tel que; upper i in I(k), simeq, colon',r'\deleted{$\begin{array}[b]{@{}c@{\ }l@{}} &\inserted{\unsure{i\in I(k)}\,\unsure{\simeq|\sim}:}\\ \exists&i\ \text{\unsure{tel que}} \end{array}$}')}
for u in r['unresolved']:
 if u['place'] in updates:
  before,after=updates[u['place']];assert u['reading']==before,(u['place'],u['reading']);u['reading']=after
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'README.txt';text=p.read_text();assert 'SP87 / cote 13, file 149' in text
text=text.replace('SP87 / cote 13, file 149','SP87 / cote 149',1)
text+='\nFinal coverage: all23 supplied leaves079–098 and100–102. Scan099 was not\nsupplied. All23 blind audits are complete. Each second reader differed from\nthe first reader and saved the independent reading before comparison. The\n466 anonymous boxes yielded328 token-different boxes, all explicitly\nadjudicated;122 boxes changed a reading or its doubt state. These are box\ncounts, not token error rates or a comparative accuracy percentage.\n\nThe canonical reviewed reports feed all generated tables. Earlier drafts,\nproposals and static-audit snapshots remain as historical documentation;\nfinal reconciliation is recorded in review/final_completion_report.md.\nThe24 transcription hashes are in review/frozen_hashes.tsv and progress.log.\n'
p.write_text(text)
with (w/'progress.log').open('a') as f:f.write('documentation reconciled '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+': applied guarded079–095 explanatory cleanup; corrected D0027/D0282 metadata links, three090 literal doubt readings and README cote label; page and frozen blind-reading bytes unchanged.\n')
