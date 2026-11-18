#!/usr/bin/env python3
"""Assemble the research-note register and record per-note context searches.

Reads only written research candidates and textual context. Never modifies the
frozen page files, combined transcription, inventory, or doubts.
"""
from pathlib import Path
import csv, datetime, json, re, subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
REC = ROOT / 'records'
GROUPS = [
 ('inertia', 'Tame inertia, Kummer classes, monodromy and second homotopy'),
 ('torsors', 'Infinitesimal groups, pointed torsors and minimality'),
 ('local', 'Local algebra, representability, gluing and documentary strands'),
 ('root', 'Further comparisons and hypothesis checks'),
]
KINDS = {'conjecture','unproved claim','unpursued implication','own idea',
         'reading question','self-flagged','withdrawn in same text'}
EXPECTED = {95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,
            112,117,118,124,126,129,130,131,132,133,135,137,138,139,140}

notes=[]
for group, title in GROUPS:
    entries=json.loads((REC/f'notes_{group}_candidates.json').read_text())
    for entry in entries:
        entry['origin']=group
        entry['section']=title
        entry['id']=f'N{len(notes)+1:03}'
        if group=='inertia' and entry['key']=='K':
            entry['kind']='unproved claim'
        if group=='inertia' and entry['key']=='O':
            entry['kind']='reading question'
        if group=='torsors' and entry['key']=='T15':
            entry['body'] += ' The marginal reading “Sans rigueur” is uncertain and is not used as evidence that the author withdrew the proposition.'
            entry['source_words'] = entry['source_words'].rstrip('.') + '; uncertain marginal “Sans rigueur”'
        if group=='root' and entry['key']=='R7':
            entry['body']=entry['body'].replace('scans126 and138','scans 126 and 138').replace('sections0 and ε','sections 0 and ε')
        assert entry['kind'] in KINDS, entry['key']
        assert set(entry['scans']) <= EXPECTED, entry['key']
        assert entry['body'] and entry['context'] and entry['relation'] and entry['search_terms'],entry['key']
        if entry['kind']=='own idea':
            assert entry['confidence'] in {'high','medium','low'} and entry['reason'],entry['key']
        notes.append(entry)

index={(x['origin'],x['key']):x['id'] for x in notes}
(REC/'research_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
(REC/'note_id_mapping.json').write_text(json.dumps({f'{a}:{b}':c for (a,b),c in index.items()},ensure_ascii=False,indent=2)+'\n')

ledger=[]
for note in notes:
    searches=[]
    for term in dict.fromkeys(note['search_terms']):
        cmd=['rg','-n','-i','-F','--',term,str(CONTEXT)]
        result=subprocess.run(cmd,capture_output=True,text=True)
        if result.returncode not in (0,1):
            raise RuntimeError(result.stderr)
        refs=[]
        for line in result.stdout.splitlines():
            m=re.match(r'(.+?):(\d+):',line)
            if m:
                refs.append(str(Path(m[1]).relative_to(CONTEXT.parent))+':'+m[2])
        searches.append({'literal_term':term,'matches':len(refs),'first_locations':refs[:12],
                         'method':'rg -n -i -F; all four supplied context files searched'})
    ledger.append({'note_id':note['id'],'source_key':note['origin']+':'+note['key'],
                   'searches':searches,'selected_context':note['context'],'relation':note['relation']})
(REC/'context_searches.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
with (REC/'context_searches.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['note_id','literal_term','match_count','first_locations','selected_context'])
    for entry in ledger:
        for item in entry['searches']:
            w.writerow([entry['note_id'],item['literal_term'],item['matches'],
                        '; '.join(item['first_locations']),entry['selected_context']])

parts=[(REC/'notes_frontmatter.md').read_text().rstrip(), '\n## Research-note register\n']
last=None
for n in notes:
    if n['section'] != last:
        parts.append(f"\n### {n['section']}\n")
        last=n['section']
    parts.append(f"\n#### {n['id']} — {n['title']}\n")
    scans=', '.join(f'{i:03}' for i in n['scans'])
    parts.append(f"**Witness:** cote 29, scan(s) {scans}, {n['place']}. **Kind:** {n['kind']}.\n")
    parts.append(f"**Source words:** {n['source_words'].rstrip('.')}.\n")
    if n['kind']=='own idea':
        parts.append(f"**Confidence:** {n['confidence']} — {n['reason']}\n")
    parts.append(n['body'].strip()+'\n')
    parts.append('**Context and relation:** '+n['context'].rstrip()+' '+n['relation'].strip()+'\n')
    state='; '.join(n['results_ids']) if n['results_ids'] else 'No direct statement-level match in the supplied RESULTS_STATE register.'
    parts.append('**Register connection:** '+state+'\n')
    parts.append('**Context searches:** '+', '.join('`'+x.replace('`','')+'`' for x in n['search_terms'])+'.\n')
    if n['check_refs']:
        path=f"records/notes_{n['origin']}_support.md"
        parts.append('**Mathematical check record:** '+', '.join(n['check_refs'])+f' in [{Path(path).name}]({path}); see `CHECK_EVENTS.tsv` for the exact scope and event type.\n')
    else:
        parts.append('**Check status:** textual/contextual comparison or research lead; no independent proof of the mathematical assertion is claimed here.\n')

parts.append((REC/'notes_endmatter.md').read_text().strip()+'\n')
target=ROOT/'MPL_29_095-140_notes.md'
target.write_text('\n'.join(parts),encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'research notes assembled: {len(notes)} items; per-item context searches recorded {now}\n')
print(f'{len(notes)} notes; {sum(len(x["searches"]) for x in ledger)} context searches; {target.stat().st_size} bytes')
