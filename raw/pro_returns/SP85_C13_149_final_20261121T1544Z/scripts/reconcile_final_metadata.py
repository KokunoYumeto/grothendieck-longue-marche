"""Final metadata-only reconciliation following blind audits 051–053."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')}
p=R/'records/149_scan051.json';r=json.loads(p.read_text())
r['hand_log'][0]['places']='L1 after possibles is doubtful des/de; L2 reads de tels; L11 before courbes remains des.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=R/'records/notation_consistency_review.md';s=p.read_text()
s=s.replace('052 p08/p14 and053','052 p13 and053')
s=s.replace('Blind-audit reconciliation through scan 050','Blind-audit reconciliation through scan 053')
needle='All these decisions were made on the corresponding saved blind crops.'
addition='''- 051: K(Pi,1) keeps its straight-legged capital Pi. The written fondamen-/taux division hyphen is restored. A tiny mark after là is a doubtful left arrow/on; the sign before un K has q primary with cancelled-d/f and universal-sign alternatives. The article, verbal ending, au/du and cancelled égale/égalant remain locally uncertain. Live surtout is distinguished from the clear adjacent cancellation.
- 052: The two-bar pair and same-meaning shorthand remain literal =, and the later map pair keeps its visible heads. The extended whole-formula crop resolves the subscript l.t.f without a final point. Written schém. is unexpanded; a source comma after fractions is restored. The short added labels retain uncertainty, and Exprimant and trouverait become the primary verb readings with explicit alternatives.
- 053: All four kernel variables keep the same local Pi/pi doubt and U/K separator rendering. The two conjugaison strokes remain text-height hyphens rather than K overbars. The small geometry addition now favours géom. conn with explicit segmentation and ending alternatives. The cancelled clause favours que/qui je suppose de from paired p descenders; no secure pi_1/nul formula survives there. The diagram keeps the original upward direction and right-hand equality node. The final i.e and accented fixé retain their independently read punctuation and accent.

'''
assert needle in s;s=s.replace(needle,addition+needle)
s=s.replace('The independent second readings are reconciled below as their audits are completed.','All 23 independent second readings are complete; their adjudications are reconciled below and in the per-page audit records.')
p.write_text(s)
p=R/'records/sheet_observations.md';s=p.read_text()
s=s.replace('Scans 041, 042, 043, 045, 046, 048, and 050','Scans 041, 042, 043, 045, 046, 048, 049, 050, and 052')
s=s.replace('Both witnesses join manifeste-/ment on042 and reconsti-/tue on043 without the visible source hyphen.','Both witnesses join manifeste-/ment on042, reconsti-/tue on043, and fondamen-/taux on051 without the visible source hyphen.')
s+='\n- **A cross-out can create a false formula outline.** On053 the stroke across an ordinary cancelled clause resembles a cap, while the two underlying descenders favour prose with suppose. The final clause remains explicitly doubtful. The cancellation line must not supply a mathematical symbol on its own.\n- **A short noun can be expanded even when both witnesses agree.** Both read schéma on052, but the noun ends with m followed by a detached stop: schém. The complete small category subscript on the same page also shows why a clipped descender must not be used to settle terminal punctuation.\n'
p.write_text(s)
p=R/'records/legibility.txt';s=p.read_text().replace('the revised formula and labels on 052','the retraced sign on 051, the revised formula and tiny labels on 052').replace('the overwrites and diagonal additions on 053','the overwrites, small geometry addition and cancelled clause on 053')
p.write_text(s)
after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'pages').glob('*.tex')};assert before==after
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'records/final_metadata_review.md').write_text('''# Final metadata review

The current records were checked separately from the frozen first readings. Reader C found a stale 051 hand-log claim (des before tels); it now agrees with the current de tels. Readers B and C identified old open-question summaries on 047 and 049–052; finalize_bookkeeping.py rebuilds all open questions from current doubts. Historical audit_boxes, reading_events, reader returns and frozen TSVs remain unchanged.

The cross-page notation review and sheet observations now include the completed 051–053 audits. The extension-capital evidence reference for 052 is corrected to p13, the actual cited source of that row. The validator now requires a crop for every material-change row and a statement ID for every mathematical check event. These changes do not alter any page TeX bytes and do not assert a new image reading or mathematical check.

Recorded '''+now+'\n')
print('Final metadata reconciled; all 23 page hashes unchanged')
