#!/usr/bin/env python3
"""Commit an explicitly approved main-reader configuration for one scan.

No inference or OCR occurs here: the JSON configuration supplies all choices.
Usage: commit_page.py /path/to/approved_scan_config.json
"""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,sys
root=Path(__file__).resolve().parents[1]
cfg=json.loads(Path(sys.argv[1]).read_text());assert cfg['approved_by_main_reader'] is True
n=int(cfg['scan']);rs={r:json.loads((root/f'readers/scan{n:03d}/{r}/report.json').read_text()) for r in ['r1','r2','r3']}
base=cfg['base_reader'];d=copy.deepcopy(rs[base]);now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
state=json.loads((root/'run_state.json').read_text())
assert n==state['scan_order'][len(state['completed_scans'])],('Page order',n,state['completed_scans'])
meta=json.loads((root.parent/f'packets/scan{n:03d}/metadata.json').read_text())
d.update(scan=n,folder=meta['folder'],their_page=int(meta['their_page']),hua_has=meta['hua_has'],filename=Path(meta['codex_file']).name,decided_utc=now,brief_version=cfg['brief_version'],reader_crop_counts=[len(rs[r].get('crops',[])) for r in ['r1','r2','r3']],main_crop_count=cfg.get('main_crop_count',0))
for key in ['changes','c_doubts','unresolved','inventory','notes','notation','abbreviations','check_events','adjudications','workflow_observation','adjudication_note','main_viewed_crops']:
    if key in cfg:d[key]=cfg[key]
# From brief v007, explicit C-mark identifiers make the already-required
# outcome coverage mechanically reviewable. Earlier decisions remain intact.
mark_list=root.parent/f'packets/scan{n:03d}/C_marked_loci.md'
if mark_list.exists():
    expected_marks=set(re.findall(r'^## (C\d{3})\b',mark_list.read_text(),re.M))
    d['c_mark_count']=len(expected_marks)
    d['c_mark_coverage']=sorted({i for q in d.get('c_doubts',[]) for i in q.get('c_mark_ids',[])})
    if int(cfg['brief_version'].lstrip('v'))>=7:
        assert set(d['c_mark_coverage'])==expected_marks,('C-mark outcome coverage',n,expected_marks-set(d['c_mark_coverage']))
for c in d.get('changes',[]):
    if 'readable ink left' in c.get('kind',''):c['kind']=r'readable ink left as \ill{}'
    assert 'readers' in c,('Main must record all three readings',c['locus'])
tex=(root/f'readers/scan{n:03d}/{base}/reading.tex').read_text()
for before,after in cfg.get('replacements',[]):
    assert before in tex,('Replacement absent',before)
    tex=tex.replace(before,after)
if cfg.get('complete_tex') is not None:tex=cfg['complete_tex']
(root/'pages'/d['filename']).write_text(tex)
assert d.get('changes') is not None
# Explicitly supplied evidence types on notes are documentary, background,
# or an actual mathematical check. The record never promotes mere reading.
if 'check_events' not in cfg:
    d['check_events']=[]
    for note in d.get('notes',[]):
        et=note.get('event_type','used and rechecked in this run')
        outcome=note.get('event_outcome','Documentary/source-content observation compared across all three independent page readings and any stated main-reader crops; no mathematical proof is asserted by this event.')
        d['check_events'].append({'statement_id':note['id'],'date':now,'who':f'GPT-6 Astra Pro; effort inherited, not independently exposed; main scan{n:03d} adjudication','type':et,'outcome':outcome})
(root/f'decisions/scan{n:03d}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write(f'scan {n:03d} done {now}\n')
print(f'Scan {n:03d} committed; rebuild records before starting next scan.')
