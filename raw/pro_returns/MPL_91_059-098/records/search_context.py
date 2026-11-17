from pathlib import Path
import subprocess,json,datetime,re
root=Path(__file__).resolve().parents[1]
context=root.parent/'context'
records=[]
for row in (root/'records/context_queries.tsv').read_text().splitlines():
 ident,query=row.split('\t',1)
 p=subprocess.run(['rg','-n','-i','--no-heading','-e',query,str(context)],capture_output=True,text=True)
 if p.returncode not in (0,1):raise RuntimeError(p.stderr)
 matches=[]
 for line in p.stdout.splitlines():
  m=re.match(r'(.+?):(\d+):(.*)',line)
  if not m:continue
  path,num,txt=m.groups(); relative=str(Path(path).relative_to(context))
  # Retain locators and short search snippets, not copies of the supplied sources.
  matches.append({'file':relative,'line':int(num),'snippet':txt[:190]})
 rec={'id':ident,'query':query,'searched_files':sorted(str(x.relative_to(context)) for x in context.rglob('*') if x.is_file()),'utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'match_count':len(matches),'matches':matches}
 records.append(rec)
 print(f'{ident}: {len(matches)} matches; '+', '.join(sorted(set(x['file'] for x in matches))))
(root/'records/context_searches.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records))
lines=['# Context search record','', 'Searches were run after the transcription freeze. All matches were located in the supplied six-file context; the research notes report relevance and limits, rather than treating keyword matches as evidence of equivalence. Snippets are abbreviated; exact file/line locators preserve traceability.','']
for r in records:
 lines.extend(['## '+r['id'],'','Query: `'+r['query']+'`','',f"Matches: {r['match_count']}; searched at {r['utc']}.",''])
 # Concise directory-level index; full short snippets are retained in the JSONL record.
 for f in sorted(set(x['file'] for x in r['matches'])):
  nums=[str(x['line']) for x in r['matches'] if x['file']==f]
  lines.append('- `'+f+'`: lines '+', '.join(nums)+'.')
 lines.append('')
(root/'records/context_searches.md').write_text('\n'.join(lines))
