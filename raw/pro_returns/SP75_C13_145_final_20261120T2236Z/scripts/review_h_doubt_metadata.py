"""Apply explicit scope-checked metadata decisions; do not change transcriptions."""
from pathlib import Path
import json
from datetime import datetime,timezone
E=Path(__file__).resolve().parents[1]
yes={
's007-12','s023-02','s023-11','s023-16','s023-17',
's026-03','s026-04','s026-11','s026-14','s026-15','s026-19','s026-26','s026-27'
}
no={
's003-14','s003-16','s008-08','s015-05','s015-06','s017-01','s017-03','s017-15',
's018-09','s018-41','s022-22','s022-24','s025-08','s025-17','s026-05',
's027-02','s027-04'
}
seen=set()
for p in sorted((E/'reader_reports').glob('*_reviewed.json')):
    r=json.loads(p.read_text());changed=False
    for c in r['changes']:
        if c['id'] in yes|no:
            c['marked_in_H']='yes' if c['id'] in yes else 'no'
            seen.add(c['id']);changed=True
    if changed:p.write_text(json.dumps(r,ensure_ascii=False,indent=2))
assert seen==yes|no,sorted((yes|no)-seen)
review={
 'rule':'The actual differing locus carries an explicit H doubt macro or an editorial expression of uncertainty/alternative reading. A description of cancellation, insertion or overtracing alone is not a doubt mark. A doubt on a different sign within a longer quoted formula is not transferred to the differing sign.',
 'explicit_macro_scope_yes':sorted(yes),
 'scope_or_editorial_correction_no':sorted(no),
 'retained_editorial_uncertainties':['s013-05: lecture comme exposant est douteuse','s018-01: uncertain macro in note on the overwritten product block','s022-01 and s022-02: systeme ... tres incertain, surcharge illisible','s023-28: inclusion ou egalite','s024-05: lecture ... incertaine'],
 'inspected_H_notes_scans':[3,8,13,15,17,18,22,23,24,25],
 'effect':'Metadata only; no source text, first reading, or C/H substantive flag changed.'
}
(E/'H_doubt_metadata_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2))
with (E/'progress.log').open('a') as f:f.write(datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+' H doubt metadata reviewed at locus scope, superseding the earlier blanket macro-presence rule; actual H notes checked, correction descriptions distinguished from uncertainty, and doubts on adjacent signs not transferred. Transcription unchanged.\n')
print('H doubt metadata reconciled at the actual locus scope.')
