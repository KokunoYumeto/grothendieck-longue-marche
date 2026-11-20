from pathlib import Path
import csv, re, json, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'SP42_CW_29'
W=ROOT/'source/SP42_CW_29_witnesses'
scan=int(sys.argv[1])
rows=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
row=next(r for r in rows if int(r['our_scan'])==scan)
p=ROOT/'staging'/f'scan{scan:03d}';p.mkdir(parents=True,exist_ok=True)
(p/'C.tex').write_text((W/row['codex_file']).read_text())
(p/'PREAMBLE.tex').write_text((W/'codex'/row['folder']/'PREAMBLE.tex').read_text())
h=(W/row['hua_file']).read_text(); matches=list(re.finditer(r'\\page\{(\d+)\}',h))
hit=next(i for i,m in enumerate(matches) if int(m.group(1))==int(row['their_page']))
chunk=h[matches[hit].end():matches[hit+1].start() if hit+1<len(matches) else len(h)]
# Only a trailing editorial heading that introduces the next page is removed.
# A heading followed by actual page content must remain in this witness excerpt.
chunk=chunk.replace('\\end{document}','')
removed_headings=[]
for m in reversed(list(re.finditer(r'\\(?:sub)?section\*\{',chunk))):
 depth=1;j=m.end()
 while j<len(chunk) and depth:
  if chunk[j]=='{' and (j==0 or chunk[j-1]!='\\'):depth+=1
  elif chunk[j]=='}' and (j==0 or chunk[j-1]!='\\'):depth-=1
  j+=1
 if depth==0 and chunk[:m.start()].strip() and not re.sub(r'%[^\n]*','',chunk[j:]).strip():
  removed_headings.append(chunk[m.start():j]);chunk=chunk[:m.start()]
chunk=chunk.strip()
(p/'H.tex').write_text(chunk+'\n')
extract=[]
for suffix in ['doubts.md','notes.md']:
 f=W/'codex'/row['folder']/f"{row['folder']}_{suffix}"
 extract.append('# '+f.name)
 heading=''
 for line in f.read_text().splitlines():
  if line.startswith('#'):heading=line
  if re.match(r'\|\s*0*'+str(scan)+r'\s*\|',line):
   extract.append(heading+'\n'+line)
(p/'C_prior_questions.md').write_text('\n\n'.join(extract)+'\n')
s=[]
for f in (ROOT/'source/SP42_CW_29_sweep3/readings').glob('*_CORRECTIONS.tsv'):
 for r in csv.DictReader(f.open(),delimiter='\t'):
  where=r['where']
  if scan==31 and 'cote 29 scan 31' in where or scan in [21,22] and 'cote 29 scans 21-22' in where:
   s.append(dict(source=f.name,**r))
(p/'S.json').write_text(json.dumps(s,ensure_ascii=False,indent=2))
row['image_base']=str(ROOT/'source/SP42_CW_29_scans'/f"{row['folder']}_29_scan{scan:03d}")
row['packet']=str(p)
row['trailing_H_editorial_headings_removed']=removed_headings
(p/'page.json').write_text(json.dumps(row,indent=2))
(p/'notation.md').write_text((OUT/'notation.md').read_text())
ns=OUT/'reader_input_notation';ns.mkdir(exist_ok=True)
(ns/f'scan{scan:03d}.md').write_text((p/'notation.md').read_text())
print(json.dumps(row,indent=2))
