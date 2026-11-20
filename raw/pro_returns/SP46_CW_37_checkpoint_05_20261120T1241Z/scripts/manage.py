#!/usr/bin/env python3
"""Record aggregation only. No OCR or image recognition. Run from any cwd."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re,sys,hashlib,zipfile,difflib
O=Path(__file__).resolve().parents[1];R=O.parent
ORDER=json.loads((O/'page_order.json').read_text())
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def load(p):return json.loads(p.read_text())
def md(v):return str(v if v is not None else '—').replace('|','\\|').replace('\n','<br>')
def reports(n):return {a:load(O/'readers'/f'scan{n:03}'/a/'report.json') for a in 'ABC'}
def compare(n):
 rs=reports(n)
 for a,r in rs.items():
  print('\nREADER',a,'CROPS',len(r['crops']))
  for i,d in enumerate(r['decisions']):print(i,json.dumps(d,ensure_ascii=False))
  print('NOTES',r.get('notes'));print('MATH',r.get('math_reading_decisions'))
 for a,b in [('A','B'),('A','C')]:
  pa=O/'readers'/f'scan{n:03}'/a/'reading.tex';pb=O/'readers'/f'scan{n:03}'/b/'reading.tex'
  print(''.join(difflib.unified_diff(pa.read_text().splitlines(True),pb.read_text().splitlines(True),fromfile=a,tofile=b)))
def rebuild():
 ds=[load(p) for p in sorted((O/'decisions').glob('scan*.json'))]
 inv=[];coll=[];events=load(O/'global_check_events.json') if (O/'global_check_events.json').exists() else [];notes=['# Notes while reading\n\nThese notes concern only the supplied scans. Statements attributed to a writer are reports of the page, not claims that the mathematics has been independently proved. Actual checks are identified explicitly and in CHECK_EVENTS.tsv.\n'];notation=[];abbr={};doubts=[];slips=[];change_sections=[];counts=[];consequential=[];math_uncertainties=[]
 for d in ds:
  n=d['scan'];meta=next(x for x in ORDER if int(x['our_scan'])==n);dc=d['decisions'];changed=[x for x in dc if x.get('diff_c') or x.get('diff_h')]
  counts.append((n,sum(bool(x.get('diff_c')) for x in dc),sum(bool(x.get('diff_h')) for x in dc),*[sum(x['confidence']==c for x in changed) for c in ['high','medium','low']]))
  lines=[f'\n## Scan {n:03} — {meta["folder"]}\n',f'Witness H: {meta["hua_has"]}; their page {meta["their_page"]}. Reader returns: `readers/scan{n:03}/A/`, `B/`, `C/`.\n','| Place | Witness C | Witness H | Consolidated reading | Three readers and main decision; scan evidence | Confidence |','| --- | --- | --- | --- | --- | --- |']
  for x in dc:
   evidence=x.get('scan_shows','');rr=x.get('readers',{})
   if rr:evidence='; '.join(f'{a}: {rr.get(a,"—")}' for a in 'ABC')+'. Main: '+evidence
   if x.get('crop'):evidence+=' Crop: `'+x['crop']+'`.'
   if x.get('c_doubt') and not x.get('diff_c'):evidence+=' C doubt retained (not counted as a change).'
   lines.append('| '+' | '.join(md(z) for z in [x['place'],x['c_reading'],x.get('h_reading'),x['reading'],evidence,x['confidence']])+' |')
   if x.get('diff_h'):
    assert meta['hua_has']=='text'
    coll.append(dict(folder=meta['folder'],their_page=meta['their_page'],our_scan=n,line=x['place'],their_reading=x.get('h_reading',''),codex_reading=x['c_reading'],final_reading=x['reading'],scan_shows=evidence,kind=x['kind'],marked_in_H=x.get('marked_in_H','no'),confidence=x['confidence']))
   if x.get('unresolved'):doubts.append((n,x['place'],x['reading'],x.get('alternatives',''),x['confidence']))
   if x.get('consequential'):consequential.append(f'- Scan {n}, {x["place"]}: {x["consequential"]}')
   if x.get('math_uncertainty'):math_uncertainties.append(f'- Scan {n}, {x["place"]}: {x["math_uncertainty"]}')
  unresolved=[x for x in dc if x.get('unresolved')]
  lines+=['\n### Still unresolved\n']+[f'- {x["place"]}: `{x["reading"]}` ({x["confidence"]}); {x.get("alternatives","")}.' for x in unresolved] if unresolved else lines+['\n### Still unresolved\n\nNone.']
  change_sections+=lines
  for i,x in enumerate(d['inventory'],1):inv.append(dict(scan=n,**{k:x.get(k,'') for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']}))
  notes.append(f'\n## Scan {n:03}\n\n'+d['notes']+'\n')
  if d.get('math_reading_decisions'):notes.append('\n### Mathematics and reading decisions\n\n'+'\n'.join('- '+s for s in d['math_reading_decisions'])+'\n')
  for x in d.get('notation',[]):notation.append(dict(scan=n,**x))
  for x in d.get('abbreviations',[]):abbr.setdefault(x['form'],{'expansion':x['expansion'],'scans':[]})['scans'].append(n)
  slips.extend((n,s) for s in d.get('slips',[]))
  for x in d.get('check_events',[]):events.append(x)
  events.append(dict(statement_id=f'S{n:03}-DOCUMENTARY',date=d['decided_utc'],who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Documentary claims in this page’s notes checked against the three independent visual readings and main adjudication crops. This is a source-reading check, not a proof of the mathematical assertions.'))
 header=['# Changes against the two witnesses\n','Counts are places, not words. Removing or revising a doubt mark counts against C; a retained doubt is recorded but not counted. Confidence columns count distinct changed places (a place differing from both witnesses counts once there). H-description pages have no H collation rows. Pure macro syntax is excluded.\n','| Scan | Changes vs C | Changes vs H | High | Medium | Low |','| --- | ---: | ---: | ---: | ---: | ---: |']
 header+=['| '+' | '.join(map(str,x))+' |' for x in counts]
 if counts:header.append('| **Total** | '+' | '.join('**'+str(sum(x[i] for x in counts))+'**' for i in range(1,6))+' |')
 header+=['\n## Consequential corrections\n']+(consequential or ['No change to mathematical meaning established so far.'])
 if math_uncertainties:header+=['\n### Uncertainties relevant to mathematical meaning\n','These are preserved ambiguities, not established corrections of the author’s mathematics.\n']+math_uncertainties
 (O/'SP46_CW_37_changes.md').write_text('\n'.join(header+change_sections)+'\n')
 for fname,rows,cols,delimiter in [('SP46_CW_37_inventory.csv',inv,['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],','),('SP46_CW_37_collation.tsv',coll,['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],'\t'),('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'],'\t')]:
  with (O/fname).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=cols,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
 (O/'SP46_CW_37_notes.md').write_text('\n'.join(notes))
 (O/'notation.json').write_text(json.dumps(notation,ensure_ascii=False,indent=2)+'\n')
 dl=['# Doubts and notation\n','## Notation table\n','Each entry records this page’s ink. Recurrence is a comparison aid; a different author or machine is not normalized into another hand.\n','| Scan | Place | Sign | LaTeX | Ink evidence |','| --- | --- | --- | --- | --- |']
 dl+=['| '+' | '.join(md(x.get(k,'')) for k in ['scan','place','sign','latex','evidence'])+' |' for x in notation]
 dl+=['\n## Remaining doubts\n','| Scan | Place | Reading | Alternatives | Confidence |','| --- | --- | --- | --- | --- |']+['| '+' | '.join(md(z) for z in row)+' |' for row in doubts]
 overrides=load(O/'abbreviation_overrides.json') if (O/'abbreviation_overrides.json').exists() else {}
 for k,v in overrides.items():
  if k in abbr:abbr[k]['expansion']=v['expansion']
 dl+=['\n## Abbreviations\n\nExpansions here are interpretations, not expansions in the transcription.\n','| Form | Possible expansion | Scans |','| --- | --- | --- |']+['| '+md(k)+' | '+md(v['expansion'])+' | '+', '.join(map(str,sorted(set(v['scans']))))+' |' for k,v in abbr.items()]
 dl+=['\n## Slips, corrections and unusual forms retained\n']+[f'- Scan {n}: {s}' for n,s in slips]
 leg=O/'legibility.txt'
 dl+=['\n## Legibility and witness comparison\n',leg.read_text() if leg.exists() else 'Assessment in progress. Faint handwriting, overwritten letters and deletion boundaries require more caution than clean typescript. Remaining uncertainty is recorded in place and above.']
 (O/'SP46_CW_37_doubts.md').write_text('\n'.join(dl)+'\n')
 pagefiles=[O/'pages'/Path(x['codex_file']).name for x in ORDER if (O/'pages'/Path(x['codex_file']).name).exists()]
 (O/'SP46_CW_37_transcription.tex').write_text('\n'.join(p.read_text().rstrip() for p in pagefiles)+'\n')
 workflow(ds)
def workflow(ds):
 hist=load(O/'briefs/history.json');s=['# Reading workflow\n','Pages were processed in increasing scan order. Each page was assigned to three fresh agents with no inherited conversation. Their scope was one page, its two witness extracts, C’s earlier doubts/notes for that page, the conventions, and the notation table established so far. They could not read one another’s files. The main reader compared the returns and inspected disputed crops before committing each page.\n','## Reader briefs\n']
 for h in hist:s +=[f'### Version {h["version"]} — first used scan {h["first_scan"]}\n',h['reason']+'\n',f'Full brief: `briefs/brief_v{h["version"]:02}.md`.\n']
 s+=['\n## First brief\n',(O/'briefs/brief_v01.md').read_text(),'\n## Last brief\n',(O/f'briefs/brief_v{hist[-1]["version"]:02}.md').read_text(),'\n## Crops and completion\n','Counts include retained reader crops and additional main-reader crops. Reuse of a reader crop for adjudication does not create another crop.\n','| Scan | A | B | C | Main additional | Total | Decided UTC |','| --- | ---: | ---: | ---: | ---: | ---: | --- |']
 for d in ds:
  n=d['scan'];rs=reports(n);nums=[len(rs[a]['crops']) for a in 'ABC'];m=len(d.get('main_crops',[]));s.append('| '+' | '.join(map(str,[n,*nums,m,sum(nums)+m,d['decided_utc']]))+' |')
 p=O/'workflow_assessment.txt';s+=['\n## What worked and what did not\n',p.read_text() if p.exists() else 'Assessment in progress. Independent returns, explicit crop coordinates, and retaining doubts provide an inspectable record. Differences in certainty are treated as disagreements, even when the proposed letters agree.']
 (O/'SP46_CW_37_workflow.md').write_text('\n'.join(s)+'\n')
def commit(n):
 p=O/'decisions'/f'scan{n:03}.json';d=load(p);d['decided_utc']=now();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 target=O/'pages'/Path(next(x['codex_file'] for x in ORDER if int(x['our_scan'])==n)).name
 assert target.exists(),'Main must write consolidated page before committing'
 rebuild()
 with (O/'progress.log').open('a') as f:f.write(f'scan {n:03} done {d["decided_utc"]}\n')
 print('Committed',n,now())
def checkpoint(num):
 path=R/f'SP46_CW_37_checkpoint_{num:02}.zip';assert not path.exists()
 with (O/'progress.log').open('a') as f:f.write(f'checkpoint {num:02} packaged {now()}\n')
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(O.rglob('*')):
   if p.is_file() and p.suffix!='.zip':z.write(p,p.relative_to(O))
 print(path,path.stat().st_size)
if __name__=='__main__':
 cmd=sys.argv[1]
 if cmd=='compare':compare(int(sys.argv[2]))
 elif cmd=='commit':commit(int(sys.argv[2]))
 elif cmd=='rebuild':rebuild()
 elif cmd=='checkpoint':checkpoint(int(sys.argv[2]))
