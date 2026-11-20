import argparse,csv,json,datetime,difflib,collections
from pathlib import Path
W=Path(__file__).resolve().parents[1]
FIELDS=['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def read_tsv(p):
 with p.open(newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
def key(r): return r['id'],str(r['cote']),str(int(r['scan']))
def reconstruct(original,rows):
 ops=[]
 for r in rows:
  assert r['decision'] in ['a','b','c','d'] and r['confidence'] in ['high','medium','low']
  assert not r.get('unresolved',False),r['id']
  if r['decision']!='a':
   assert not r['find'] and not r['replace'];continue
  old,new=r['find'],r['replace'];assert old and old!=new
  assert original.count(old)==1,(r['id'],original.count(old))
  offset=original.index(old)
  for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
   if tag!='equal':
    op=(offset+i1,offset+i2,new[j1:j2])
    if op not in ops: ops.append(op)
 ops.sort()
 for a,b in zip(ops,ops[1:]): assert a[1]<=b[0] and not(a[0]==a[1]==b[0]==b[1]),('conflict',a,b)
 result=original
 for start,end,rep in reversed(ops): result=result[:start]+rep+result[end:]
 return result,ops
def regenerate():
 source=read_tsv(W/'source/IM03_9-12_corrections.tsv');accepted={};reports=[]
 for p in sorted((W/'reviews').glob('*/accepted.json')):
  doc=json.loads(p.read_text());reports.append(doc)
  for r in doc['rows']:
   k=key(r);assert k not in accepted;accepted[k]=r
 ordered=[accepted[key(r)] for r in source if key(r) in accepted]
 with (W/'placements.tsv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t',lineterminator='\n');wr.writeheader();wr.writerows([{k:r[k] for k in FIELDS} for r in ordered])
 source_by_key={key(r):r for r in source}
 parts=['# Notes on the diplomatic corrections','The supplied rows are judged against the original TeX and facsimiles. Mathematical amendments are recorded here, not substituted for his written text. Crop references are relative to this archive. No OCR was used.']
 for title,selected in [('His slips and mathematical refinements (b)',[r for r in ordered if r['decision']=='b']),('Not on the assigned page (d)',[r for r in ordered if r['decision']=='d']),('Mixed reading corrections and editorial qualifications',[r for r in ordered if r['decision']=='a' and r.get('editorial_note')]),('Readings left in doubt',[r for r in ordered if r.get('doubt_note') or r['confidence']=='low'])]:
  parts+=['## '+title]
  if not selected: parts+=['None among completed pages.']
  for r in selected:
   detail = (r.get('doubt_note') or r.get('notes','')) if title=='Readings left in doubt' else (r.get('editorial_note','') if title=='Mixed reading corrections and editorial qualifications' else r.get('notes',''))
   parts += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}",detail,r['what_the_ink_shows']]
   if r['decision']=='b' and source_by_key[key(r)]['should_read']: parts += ['Proposed sense supplied by the correction table (editorial, not adopted in the transcription): '+source_by_key[key(r)]['should_read']]
 parts+=['## Recording conventions','Repeated statement IDs on different pages remain separate rows, in the supplied table order. Cote and scan disambiguate them. Duplicate corrections at one place can support the same edit, applied once. Original CRLF line endings are preserved. Every (a) find span occurs exactly once in the original. Intervening text within multi-place spans stays unchanged.','CHECK_EVENTS.tsv records visual/transcription comparisons as “used and rechecked in this run”, not mathematical proofs. Effort is recorded as not separately exposed rather than invented. Reader proposals and main-reader acceptances are under reviews/.']
 (W/'notes.md').write_text('\n\n'.join(parts)+'\n')
 return len(reports),len(ordered)
def main():
 p=argparse.ArgumentParser();p.add_argument('page');p.add_argument('--main-note',required=True);a=p.parse_args();rd=W/'reviews'/a.page
 assert not (rd/'accepted.json').exists()
 doc=json.loads((rd/'proposal.json').read_text());rows=doc['rows']
 assert [key(r) for r in rows]==[key(r) for r in read_tsv(rd/'rows.tsv')]
 original=(W/'source/IM03_9-12_pages'/f'{a.page}.tex').read_bytes().decode('utf-8');result,ops=reconstruct(original,rows)
 assert (rd/'proposed.tex').read_bytes()==result.encode('utf-8'),'Proposed bytes differ from listed edits'
 for r in rows:
  r['what_the_ink_shows'] += ' (Crops: ' + '; '.join(r['crops']) + '.)'
  assert r['what_the_ink_shows'].strip() and r.get('crops')
  for crop in r['crops']: assert (W/crop).is_file()
  if r['decision'] in ['b','d']: assert r.get('notes','').strip()
 now=utc();doc.update(main_reviewed_at_utc=now,main_review_note=a.main_note)
 (W/'edited_pages'/f'{a.page}.tex').write_bytes(result.encode('utf-8'));(rd/'accepted.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
 pages,nrows=regenerate()
 with (W/'CHECK_EVENTS.tsv').open('a',newline='') as f:
  wr=csv.writer(f,delimiter='\t',lineterminator='\n')
  for r in rows:
   loc=f"cote {r['cote']}, scan {int(r['scan']):03d}; decision {r['decision']}; "
   wr.writerow([r['id'],doc.get('inspected_at_utc') or now,f"GPT-6 Astra Pro; effort not separately exposed; run {doc.get('reader','reader').split(';')[0]}/{a.page}",'used and rechecked in this run',loc+r['what_the_ink_shows']])
   wr.writerow([r['id'],now,f'GPT-6 Astra Pro; effort not separately exposed; run main/{a.page}','used and rechecked in this run',loc+'main reader checked crop evidence and unique original-span placement. '+a.main_note])
 cote,scan=a.page.split('_scan')
 with (W/'progress.log').open('a') as f: f.write(f'scan {scan} done {now} cote {cote}\n')
 print(json.dumps(dict(page=a.page,pages_done=pages,rows_done=nrows,decisions=dict(collections.Counter(r['decision'] for r in rows)),minimal_edits=len(ops))))
if __name__=='__main__': main()
