from pathlib import Path
import json,re,subprocess
ROOT=Path('/workspace/scratch/b8e2c31cadf4/work')
BASE='MPL_36_053-085+39'
DATA=ROOT/'research_items.json'
CONTEXT={
'S19':('S19 / package-218 plan','unchecked planning request','README.md','36/053–085; 39/002–020, with blank scans omitted'),
'H1':('Hua, findings register, 36-h1-invariant-cycle-defect','unverified AI-produced conjecture; intake: “new to us”, not a proof review','notes/RESULTS_STATE.md, Findings of another project','36/061–071'),
'ORTH':('Hua, findings register, 36-orthogonality-regular-adic-base','unverified AI-produced conjecture, unsearched; intake: “new to us”','notes/RESULTS_STATE.md, Findings of another project','36/074–077'),
'HENS':('Hua, findings register, 39-inverse-function-axioms-henselian','unverified AI-produced conjecture; intake: “new to us”, not a proof review','notes/RESULTS_STATE.md, Findings of another project','39/010–013, 015'),
'N91':('MPL_91_099-143 §68','observation in a returned package, first-pass lead','MPL_91_099-143_notes.md, excerpt in notes/RESULTS_STATE.md','91/124, 126, 128 in the supplied excerpt'),
'H9':('WG H9','unchecked war-game hunch, “Believe”','WARGAME_MATH_HUNCHES_20261112.md, excerpt in notes/RESULTS_STATE.md','cote 44, Th. 4–5; scan numbers not supplied'),
'WG2':('WG2 §2.1 #2','unchecked round-2 plan item','PROGRAM_WARGAME_ROUND2_20261112.md, excerpt in notes/RESULTS_STATE.md','graded-ring unit, scans 003–018; association of individual cotes is not resolved by the excerpt'),
'M33':('MPL_33_002-049 §2','observation in a returned package, first-pass lead','MPL_33_002-049_notes.md, excerpt in notes/RESULTS_STATE.md','excerpt begins “Scans 002…” and is truncated; no complete scan range supplied'),
'M14':('MPL_14_002-044 §107','observation in a returned package, first-pass lead','MPL_14_002-044_notes.md, excerpt in notes/RESULTS_STATE.md','no individual scan supplied in this excerpt')
}
def load():return json.loads(DATA.read_text()) if DATA.exists() else []
def add(id,section,cote,scans,title,kind,note,refs,relation,query,confidence=None,reason=None,bib=None):
 items=load();assert id not in [x['id'] for x in items]
 items.append(dict(id=id,section=section,cote=cote,scans=scans,title=title,kind=kind,note=note,refs=refs,relation=relation,query=query,confidence=confidence,reason=reason,bib=bib or []))
 DATA.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
def search_all():
 rows=[]
 for x in load():
  r=subprocess.run(['rg','-ni','--',x['query'],'context/README.md','context/notes/RESULTS_STATE.md'],cwd=ROOT.parent,text=True,capture_output=True)
  assert r.returncode in (0,1),(x['id'],r.stderr)
  hits=[]
  for line in r.stdout.splitlines():
   p,n,s=line.split(':',2);m=re.search(r'^- \*\*(.+?)\*\*',s)
   hits.append({'file':p.removeprefix('context/'),'line':int(n),'entry':m.group(1) if m else ('S19 / plan' if 'S19' in s else 'context prose')})
  rows.append({'id':x['id'],'query':x['query'],'hits':hits})
 (ROOT/'qa'/'context_searches.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 lines=['# Per-item context searches','', 'Each query was actually run against both supplied context files after the freeze. The results below record source locations and entry IDs, not copies of the context files. An absent literal match does not prove that an unseen original has no relevant discussion.','', '| Note | Search expression | Context hits |','|---|---|---|']
 for r in rows:
  hit='; '.join(f"{h['file']}:{h['line']} — {h['entry']}" for h in r['hits']) or 'No literal match'
  lines.append('| '+r['id']+' | `'+r['query'].replace('|','&#124;')+'` | '+hit.replace('|','&#124;')+' |')
 (ROOT/'qa'/'context_searches.md').write_text('\n'.join(lines)+'\n')
 return rows
def render():
 items=load();head=(ROOT/'notes_preface.md').read_text() if (ROOT/'notes_preface.md').exists() else '# Research notes\n\nWork in progress after transcription freeze.\n'
 out=[head,'\n## Context citation key\n']
 for key,(name,status,source,scans) in CONTEXT.items():out.append(f'- **CTX-{key} — {name}**: {status}; source `{source}`; source locations: {scans}.')
 last=None
 for x in items:
  if x['section']!=last:out.append('\n## '+x['section']+'\n');last=x['section']
  out.extend([f"\n### {x['id']} — {x['title']}\n",f"**Source:** cote {x['cote']}, scan(s) {x['scans']}. **Kind:** {x['kind']}.\n",x['note']+'\n'])
  if x['confidence']:out.append(f"**Own-idea confidence:** {x['confidence']}; reason: {x['reason']}.\n")
  refs='; '.join('**'+CONTEXT[k][0]+'** ['+CONTEXT[k][1]+']' for k in x['refs'])
  out.append(f"**Context:** {refs}. **Relation:** {x['relation']}. **Search record:** {x['id']} in `qa/context_searches.md`.\n")
  if x['bib']:out.append('**Primary-source comparison:** '+', '.join(x['bib'])+'.\n')
 for name in ('notes_self_flags.md','notes_titles.md','notes_context_matrix.md','notes_bibliography.md','notes_verification.md'):
  p=ROOT/name
  if p.exists():out.append('\n'+p.read_text())
 (ROOT/(BASE+'_notes.md')).write_text('\n'.join(out))
if __name__=='__main__':
 rows=search_all();render()
 print(json.dumps({'notes':len(rows),'queries_with_hits':sum(bool(r['hits']) for r in rows),'queries_without_literal_hit':sum(not r['hits'] for r in rows)},ensure_ascii=False))
