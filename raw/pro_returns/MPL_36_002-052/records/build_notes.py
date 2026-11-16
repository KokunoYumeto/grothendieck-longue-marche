from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,json,re,subprocess
from notes_data import NOTES,ROOT
CTX=ROOT.parent/'context'
context_files=sorted(CTX.rglob('*.md'))
def polish(text):
 # Preserve math, identifiers and code while spacing prose and scan locators.
 chunks = re.split(r'(\$[^$]*\$|`[^`]*`)', text)
 for i in range(0, len(chunks), 2):
  t = chunks[i]
  t = re.sub(r'(?<=[a-z])(?=\d)', ' ', t)
  t = re.sub(r'(?<=\d),(?=N?\d)', ', ', t)
  t = re.sub(r'(?<=N\d{2}),(?=N)', ', ', t)
  t = t.replace('degrees−', 'degrees −').replace('line−', 'line −')
  t = t.replace('section2', 'section 2').replace('n°316', 'n° 316')
  t = t.replace('SGA7', 'SGA 7').replace('cf.2.3', 'cf. 2.3')
  chunks[i] = t
 return ''.join(chunks)

records=[]
search_md=['# Actual context searches for the research notes\n','The full three supplied Markdown files were searched for each numbered item after the transcription freeze. These are query records and short location excerpts, not copies of the supplied sources; a keyword hit is not a proof of mathematical identity.\n']
for n in NOTES:
 for key in ('title','body','context','reason','location'):
  if n.get(key):
   n[key]=polish(n[key])
   n[key]=n[key].replace('dual1-motives','dual 1-motives').replace('degree0','degree 0').replace('degree1','degree 1').replace('proper0-dimensional','proper 0-dimensional').replace('degree-one0-cycle','degree-one 0-cycle').replace('SGA7','SGA 7')
 q=n['query']
 r=subprocess.run(['rg','-n','-i','-e',q]+[str(p) for p in context_files],capture_output=True,text=True)
 assert r.returncode in (0,1),(n['id'],r.stderr)
 hits=r.stdout.splitlines(); matches=[]
 for hit in hits:
  path,line,excerpt=hit.split(':',2)
  matches.append({'file':str(Path(path).relative_to(CTX)),'line':int(line),'excerpt':excerpt[:360]})
 row={'id':n['id'],'query':q,'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'searched_files':[str(p.relative_to(CTX)) for p in context_files],'exit_code':r.returncode,'hit_count':len(hits),'matches':matches}
 records.append(row)
 search_md.append(f"## {n['id']} — {n['title']}\n\nQuery: `{q}`; matches: **{len(hits)}**; searched: README.md, notes/RESULTS_STATE.md, same_cote_36/MPL_36_053-085+39_notes.md.\n\n")
 for m in matches[:20]:search_md.append(f"- `{m['file']}:{m['line']}` — {m['excerpt']}\n")
 if not matches:search_md.append('No literal match; the main note specifies the scope or semantic comparison rather than treating absence of a keyword as a literature result.\n')
 if len(matches)>20:search_md.append(f"\n{len(matches)-20} further matched lines are indexed in the JSON record.\n")
 search_md.append('\n')
(ROOT/'records/context_searches.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(ROOT/'records/context_searches.md').write_text(''.join(search_md))
(ROOT/'records/notes_data.json').write_text(json.dumps(NOTES,ensure_ascii=False,indent=2)+'\n')
header=r'''# Research notes — MPL_36_002-052

## Scope, source status and citation key

These notes concern **36.pdf, scans003–008 and028–052: 31 retained scans**, all personally transcribed and separately audited before context access. The transcription was frozen at **2026-11-16 22:35:26 UTC**, and the context was opened at **22:35:31 UTC**; the page texts have not been revised using the context or published literature. “Scan” always means the PDF scan number, not the lower pencil folio or a reused typescript’s own pagination. The prompt’s later “49 pages” conflicts with its opening count and the93 supplied images; no unprovided pages have been fabricated.

**CT** means `same_cote_36/MPL_36_053-085+39_notes.md`, the supplied first-pass, unchecked research notes for neighbouring cote36 scans053–085 and cote39. A citation such as “CT N06 (36/054)” identifies that file, its note and the scan it reports; those earlier scan images and their full transcriptions were not supplied here and were not independently inspected. **RS** means `notes/RESULTS_STATE.md`, with entries cited by their exact IDs; a status is the earlier return’s claim unless that exact entry is expressly certified, and the referee list in the introduction does not certify adjacent IDs. **README S19** means the supplied package217 planning request to compare SGA4/5/7 drafts with print and the Stacks Project; it is a plan, not a mathematical result. The README’s original “Only this README” sentence is superseded by its dated additions announcing the other two files.

Each item has one permitted kind, a brief source quotation or formula, a scan/block locator, a context comparison and an independently executed keyword search. The **15 own-idea items** are calculations, conditional proof routes or proposed tests, with confidence and reasons; none is claimed to be new. Some short formal arguments are completed, but this does not certify the broader manuscript statements. Uncertain readings remain visibly qualified, and a crossed argument is distinguished from a retracted theorem. The reused Lie-algebra and cohomology typescripts are treated as distinct source texts, without assigning authorship or an edition from their physical proximity to the handwritten notes.

The primary-source references **P1–P9** are listed at the end, with their actual verification limits. Author–date citations refer to those entries; exact tags and section numbers distinguish the living Stacks references. All source searches took place after the transcription freeze. The raw record for every note is in `records/context_searches.json`, with a readable index in `records/context_searches.md`.

| Strand | Current scans | Main context comparison |
|---|---|---|
| Editorial objections and requested proofs for SGA7 IX |003–008|CT N38–N49,N57–N59,N97;36/073–084|
| Lattices, two-term complexes and torsion biextension pairings |028–034|CT N06–N12;36/054–058; Deligne’s published two-term formulation|
| Picard, adjunction and higher obstruction programme |035–044|CT N24,N30,N37,N58;36/063–071,083|
| Witt/Frobenius and prime-to-p Tate comparisons |045–046|CT N25–N26,N47;36/063,079–080|
| Reconstruction from torsion and rigidity |047–052|Direct continuation in CT N06–N12;36/054–058|
| Reused Lie and Čech material |038,049,051|Separate source/provenance questions; S19 comparisons|

'''
header=re.sub(r'(?<=[a-z])(?=\d)',' ',header).replace('SGA4/5/7','SGA 4/5/7').replace('SGA7','SGA 7').replace('cote36','cote 36').replace('cote39','cote 39').replace('the93','the 93')
parts=[header]; current=None
for n in NOTES:
 if n['section']!=current:
  current=n['section'];parts.append(f"\n## {current}\n\n")
 scans=', '.join(f'{x:03}' for x in n['scans'])
 parts.append(f"### {n['id']} — {n['title']}\n\n**Source:** 36.pdf, scan(s) {scans}; {n['location']}. **Kind:** {n['kind']}.\n\n{n['body']}\n\n")
 if n['confidence']:parts.append(f"**Own-idea confidence:** {n['confidence']}; **reason:** {n['reason']}.\n\n")
 parts.append(f"**Context comparison:** {n['context']}\n\n**Context search:** `{n['query']}` — record {n['id']} in `records/context_searches.md`.\n\n")
 if n['refs']:parts.append(f"**Primary comparison:** {', '.join(n['refs'])}.\n\n")
for filename in ('notes_standing.md','notes_register.md','notes_bibliography.md','notes_final_verification.md'):
 p=ROOT/'records'/filename
 if p.exists():parts.append(p.read_text())
(ROOT/'MPL_36_002-052_notes.md').write_text(''.join(parts))
print('Built',len(NOTES),'notes;',sum(x['hit_count']==0 for x in records),'no-hit queries;',Counter(n['kind'] for n in NOTES))
