from pathlib import Path
import datetime

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_147-181+34_002-017'
out = ['# Research notes: cote 33, scans 147–181; cote 34, scans 003–017\n',
       '**Working research draft; transcription already frozen.** This copy records the research completed so far, for the hourly checkpoint. Final integration, sentence limits, the separate self-flag/title inventories, and the complete results-register disposition remain in progress.\n',
       'Source line numbers refer to the frozen per-page LaTeX files. Context A = `same_cote_33/MPL_33_002-049_notes.md`; context B = `same_cote_33/MPL_33_098-146_notes.md`. Both are first-pass leads, not established results. The supplied `notes/RESULTS_STATE.md` and `README.md` were read only after the freeze at 2026-11-16 00:02:21 UTC.\n']
for name, start, stop in [
    ('research_duality.md','## Candidates',None),
    ('research_monodromy.md','## Candidates','## Verified primary comparisons'),
    ('research_reused_sheets.md','## Twenty-four note candidates','## Exact title and numbering catalogue'),
    ('research_integration.md','## I01.',None),
]:
    p=ROOT/'records'/name
    if not p.exists():
        out.append(f'\n## Pending contribution\n\n`{name}` not yet included in this draft.\n')
        continue
    text=p.read_text()
    pos=text.find(start)
    if pos>=0:text=text[pos:]
    if stop and stop in text:text=text.split(stop)[0]
    out.append('\n'+text+'\n')
(ROOT/f'{PREFIX}_notes.md').write_text('\n'.join(out))
with (ROOT/'progress.log').open('a') as f:
    f.write('research draft assembled '+datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print('Research draft assembled; frozen TeX untouched.')
