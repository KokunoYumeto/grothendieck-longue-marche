from pathlib import Path
import json,re,subprocess,concurrent.futures,datetime
R=Path(__file__).resolve().parents[1]; C=R.parent/'context'
allnotes=[]
for fn in ['research_notes_seed.json','research_period_notes.json','research_structure_notes.json','research_bridge_notes.json','research_additional_notes.json','research_period_extra_notes.json','research_cote15_extra_notes.json']:
 p=R/'records'/fn
 if p.exists(): allnotes += json.loads(p.read_text())
ids=[n['id'] for n in allnotes]
if len(ids)!=len(set(ids)): raise ValueError('Duplicate note IDs')
# Queries execute separately for every observation, even when subjects overlap.
paths=[p for p in C.rglob('*') if p.is_file() and p.suffix in ('.tex','.md')]
line_maps={}
for p in paths:
 cote=scan=None; heading=''; m={}
 for i,l in enumerate(p.read_text().splitlines(),1):
  x=re.search(r'\\cotefile\{([^}]+)\}',l)
  if x:cote=x.group(1)
  x=re.search(r'\\scanpage\{([^}]+)\}',l)
  if x:scan=x.group(1)
  if l.startswith('#'):heading=l.lstrip('# ').strip()
  m[i]={'cote':cote,'scan':scan,'heading':heading}
 line_maps[str(p)]=m

def search(n):
 cmd=['rg','-n','-i','--no-heading','--with-filename','--fixed-strings']
 for t in n['terms']:cmd+=['-e',t]
 cmd += [str(p) for p in paths]
 q=subprocess.run(cmd,text=True,capture_output=True)
 if q.returncode not in(0,1):raise RuntimeError(q.stderr)
 matches=[]
 for l in q.stdout.splitlines():
  f,num,s=l.split(':',2);num=int(num)
  matches.append(dict(file=str(Path(f).relative_to(C)),line=num,**line_maps[f][num],excerpt=s[:260]))
 # All distinct hit scans retained; bounded representative excerpts, not source replication.
 locs=sorted(set((x['file'],x.get('cote') or '',x.get('scan') or '',x.get('heading') or '') for x in matches))
 reps=[];seen=set()
 for x in matches:
  k=(x['file'],x.get('cote'),x.get('scan'),x.get('heading'))
  if k not in seen:reps.append(x);seen.add(k)
 return dict(id=n['id'],terms=n['terms'],match_count=len(matches),hit_locations=locs,representative_matches=reps,selected_context=n['context'],ledger=n['ledger'])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: audit=list(pool.map(search,allnotes))
(R/'records/research_context_searches.json').write_text(json.dumps({'run_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'context_root':'supplied context archive, opened after freeze','searches':audit},ensure_ascii=False,indent=2)+'\n')
header=R/'records/notes_frontmatter.md'
footer=R/'records/notes_endmatter.md'
text=header.read_text() if header.exists() else '''# Research notes: MPL_15_195–228 + MPL_18_002–017\n\nPost-freeze research draft in progress. The frozen transcription is never changed by these comparisons. The observation register below is the report written so far; supplementary research reports and reference verification records are included under `records/`.\n\n## Conventions and status\n\nLocations such as `15/195:L9–19` mean cote 15, scan 195, lines 9–19 of the individual file `pages/MPL_15_195-228+18_002-017_15_scan195.tex`; they never mean line numbers of the combined transcription. **CT** denotes the supplied first-pass `context/MPL_16+47+54+44_transcription.tex`; **CN** denotes `context/MPL_16+47+54+44_notes.md`. A CT reference includes cote and scan; CN identifiers refer to its note headings. These supplied files are not independently verified manuscript readings.\n\nEvery ledger ID refers to the supplied `context/notes/RESULTS_STATE.md`, built 15 November 2026 at 12:08 UTC. “Proved”, “Known”, “Refuted” and “Open” are the named return’s claims unless explicitly qualified as refereed there; no status is upgraded by these notes. Broad WG references are project links, not evidence that a planning question is already settled. Each observation has a separately executed context search recorded in `records/research_context_searches.json`; the selected match and the relation are stated with the observation.\n'''
sects=[('A','## Cote 15: realizations, places and reconstruction'),('P','## Cote 18: local descriptions, periods and Hodge comparison'),('M','## Structural questions and modern motivic categories'),('B','## The four linear and non-linear comparisons'),('R','## Reused texts and source-critical observations'),('X','## Additional tests and qualifications')]
for prefix,title in sects:
 ns=sorted((n for n in allnotes if n['id'].startswith(prefix)),key=lambda n:int(n['id'][1:]))
 if not ns:continue
 text+='\n'+title+'\n'
 for n in ns:
  text+=f"\n### {n['id']} — {n['title']}\n\n"
  text+=f"**Kind:** {n['kind']}  \n**Witness:** `{n['location']}`  \n**Brief quotation:** {n['quote']}  \n**Context search:** `"+' | '.join(n['terms'])+f"` → {n['context']}  \n**Results ledger:** {n['ledger']}\n\n{n['body']}\n"
if footer.exists():text+='\n'+footer.read_text()
(R/'MPL_15_195-228+18_002-017_notes.md').write_text(text)
(R/'records/research_notes_all.json').write_text(json.dumps(allnotes,ensure_ascii=False,indent=2)+'\n')
print(f'Rendered {len(allnotes)} observations; {len(audit)} context searches; no transcription writes')
