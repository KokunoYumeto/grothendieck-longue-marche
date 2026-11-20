"""Record an audit only after the primary reader has reread the scan image.

This helper never opens an image or derives a reading. All decisions are
explicit caller input. It updates existing records, not the original witness.
"""
from editorial import *

def audit(scan, note, *, replacements=(), changes=(), certainty=(),
          inventory=(), doubts=None, notation=(), hand=(), checks=(),
          notes_append='', crops=()):
    record_path=ROOT/'records'/f'scan{scan:03}.json'
    r=json.loads(record_path.read_text())
    if r.get('audited'):
        raise ValueError(f'scan {scan} already audited')
    prior=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
    expected=next((x['scan'] for x in prior if not x.get('audited')),None)
    if len(prior)!=26 or scan!=expected:
        raise ValueError(f'all first readings must precede ordered audit; expected {expected}')
    p=ROOT/'pages'/Path(r['map']['codex_file']).name
    text=p.read_text()
    for before,after in replacements:
        if before not in text:
            raise ValueError(f'scan {scan}: replacement absent: {before}')
        text=text.replace(before,after)
    p.write_text(text)
    for c in changes:
        c['stage']='second image reading'
        r['changes'].append(c)
    for name,values in [('certainty',certainty),('inventory',inventory),
                        ('notation',notation),('hand',hand),('checks',checks),('crops',crops)]:
        r[name].extend(values)
    if doubts is not None:
        r['doubts']=list(doubts)
    if notes_append:
        r['notes']+='\n\n'+notes_append
    r['audit_note']=note
    r['audited']=utc()
    record_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    build()
    log(f'scan {scan:03} audited {r["audited"]}')
    audited=[x['scan'] for x in prior if x.get('audited')]+[scan]
    remaining=[s for s in ORDER if s not in audited]
    (ROOT/'READING_STATUS.md').write_text(
        '# Current reading state\n\nAll 26 first readings are complete. '
        f'Second image readings completed in order: {", ".join(map(str,audited))}. '
        f'Next audit: {remaining[0] if remaining else "none; all 26 complete"}. '
        'Each audit is recorded at its actual UTC completion time in progress.log. '
        'No OCR, external research or TeX compilation has been used. '
        'Checkpoint history is in CHECKPOINTS.md.\n')
    print(f'scan {scan:03} audited; {len(changes)} new comparison rows')
