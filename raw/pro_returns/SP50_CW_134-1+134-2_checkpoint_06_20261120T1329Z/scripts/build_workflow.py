from pathlib import Path
import json
O=Path(__file__).resolve().parents[1];P='SP50_CW_134-1+134-2'
state=json.loads((O/'state.json').read_text())
history=json.loads((O/'workflow_history.json').read_text()) if (O/'workflow_history.json').exists() else []
s=f'# {P} — Reading workflow\n\nEach page was assigned in source order to three new independent sub-agents with fork_turns="none". No agent was given another reader’s return. Each received only this page’s witness extracts, images and earlier C questions, the controlling conventions, the current brief, and a frozen notation snapshot. The main reader retained their returns and inspected tight evidence crops for adjudication. The full individual reading, image-view log, evidence and reasoning are retained in readers/ and evidence/. Model names and exposed effort information are recorded in each report; effort is not invented where the runtime did not expose it.\n\nNo OCR, text recognition, PDF text layer, external archive, internet research or other reproduction was used. The supplied original images and witnesses are omitted from this return; cropped evidence is newly generated documentation, with source-pixel boxes and processing recorded alongside it. PREAMBLE.tex is included to specify the required macros.\n\n'
s+='## First reader brief\n\n'+(O/'briefs/v01.md').read_text()+'\n\n## Last reader brief\n\n'+(O/'briefs'/(state['active_brief']+'.md')).read_text()+'\n'
s+='\n## Changes to the brief\n\n'
if history:
    for x in history:s+=f"- after {x['page']}, {x['version']} (first used {x.get('first_used', 'as logged in page decisions')}): {x['reason']}\n"
else:s+='No change has yet been needed.\n'
s+='\n## Crops and completion by page\n\nCounts are actual tight-crop files made in this run, not source halves. A main-reader inspection of an existing reader crop does not add a new crop.\n\n| Cote / scan | Reader 1 | Reader 2 | Reader 3 | Main | Total | Status |\n| --- | --- | --- | --- | --- | --- | --- |\n'
for p in json.loads((O/'page_order.json').read_text()):
    key=f"{p['cote']}_scan{int(p['our_scan']):03d}";b=O/'evidence'/key
    if not b.exists():continue
    counts=[]
    for r in ['r1','r2','r3','main']:
        log=b/r/'crops.jsonl'
        counts.append(len(log.read_text().splitlines()) if log.exists() else 0)
    status='decided' if key in state['completed'] else 'in progress'
    s+='| '+p['cote']+' / '+p['our_scan']+' | '+' | '.join(map(str,counts+[sum(counts)]))+' | '+status+' |\n'
s+='\n## What worked and what did not\n\n'
notes=O/'workflow_observations.md'
s+=notes.read_text() if notes.exists() else 'Observations are being accumulated as the pages are decided.\n'
s+='\n## Record organization and checkpoint policy\n\nEach decided page is written to pages/ before the next page is assigned. decisions/ records the main reader’s choice at every logged place, including all three readings when they differed; build_records.py renders the cumulative tables. CHECK_EVENTS.tsv distinguishes actual targeted mathematical checking from background carried without a detected fault. Reading alone is never labelled a proof check. Checkpoints are new cumulative ZIPs created at 45-minute intervals only. Earlier checkpoint ZIPs and original source attachments are not nested in any archive. Final SHA-256 hashes are recorded only when all page readings and the combined fragment are frozen, then verified unchanged at the end.\n'
(O/(P+'_workflow.md')).write_text(s)
print('workflow updated')
