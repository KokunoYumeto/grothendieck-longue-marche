"""Retain source provenance; consolidate working findings into the main notes."""
from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone

R=Path(__file__).resolve().parents[2]
utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
specs={
'research_q1.md':('Q1 source-inspection record','Q1.1–Q1.6',r'''
- Supplied context read: README, RESULTS_STATE, 147/140–145 and 149/132–136, with exact searches in both complete supplied transcriptions.
- Current frozen selection searched for whole-word ombre/ombres and the stem tubul-; zero matches within these 43 pages.
- Original149/133 checked visually, including mechanical enlarged/rotated crops of three clauses; page object656, image object657, footer132, manuscript66.
- Original image SHA-256: `814bf2b4ca3c336390ec9db622977513ea7625f424f0f78a69320f9effef2b4c`.
- `research_q1_query_log.json` preserves the query sequence, candidate locations, retrieval paths, ranges and checksums.
- Public machine-text batches were used only for search locations. The later136 verification is recorded separately in `research_q1_cote136_source_ledger.json`.
- Confidence and interpretation are given once in the integrated question notes. No chronological priority follows from this bounded search.
'''),
'research_q2.md':('Q2 source-inspection record','Q2.1–Q2.8',r'''
- Supplied147/138–190, context README, RESULTS_STATE and relevant supplied notes were read before the external source comparison.
- Official151 PDF:75 pages,27,695,508 bytes, SHA-256 `ad5a7f5061fb5f9a2ee13f8b938611dc261b717203408c3279b41431d4d0bbd2`.
- Original JPEG streams were extracted without OCR and their indices checked against the complete PDF page/image references.
- Researcher visual scope:151/002,003,005,007,025–054; the mathematical sequence027–054 was read continuously.
- Principal integrating editor independently inspected151/041–044 and052.
- Physical039–044 correspond to archive footers38–43 and manuscript7–9 verso; physical052 has archive footer51.
- Primary URLs and published reference locators appear in the main bibliography. The web reader failed to parse151.pdf; evidence came from the downloaded original images, not an invented web extraction.
- Exact dating and proof-scope qualifications are integrated into Q2.2–Q2.4. The displayed calculations in Q2.5–Q2.8 are present explanations with their maps specified.
'''),
'research_q3_q4.md':('Q3–Q4 source-inspection record','Q3.1–Q4.7',r'''
- Supplied context README and RESULTS_STATE were read in full; relevant147/181–186 and149/132–134 were compared with frozen121/004–024 and026–037.
- All24 original mathematical leaves of cote120 were visually inspected: physical PDF002–025; the complete PDF includes one wrapper.
- Principal integrating editor independently inspected120/003,017 and021.
- Original150/037–039 were visually inspected; their image-object IDs were confirmed against the complete99-page PDF (40,334,954 bytes).
- Physical scan numbers in these records include the wrapper and exceed the archive footer by one.
- Primary literature passages checked: van den Dries–Miller§3,§§4.2–4.3,4.7,AppendixD.10; Schürmann Theorem0.1; Pillay Remark1.10; Shiota10 Theorem2.1, Complement and Lemma3.3; Shiota14 publisher abstract; Shiota16 Theorem2 and introductory Corollary(i).
- The integrating editor independently opened the primary papers and inspected their cited passages. Source URLs and publication versions appear in the main bibliography.
- Scope corrections from the final read-only review are recorded in `research/review_findings.md`.
'''),
'research_q1_cote136_check.md':('Q1 original136 inspection record','Q1.4–Q1.6',r'''
- Original physical scans003,023–026 were checked visually, corresponding to archive footers2,22–25.
- Page/image objects:003→6/7;023→106/107;024→111/112;025→116/117;026→121/122.
- The declared source PDF has376 pages and161,283,368 bytes; selected HTTP byte ranges were retrieved, not a complete PDF.
- Page-tree mapping was checked independently of visible footers. Root1976→1974→1963 reaches leaf groups1900–1905, with six pages in each group.
- Principal integrating editor independently inspected023,025 and026.
- `research_q1_cote136_source_ledger.json` retains exact byte ranges, response metadata and all five image checksums.
- The compressed tensor-base glyph and questioned grading restriction remain reading qualifications. The final notes use the explicit degreewise expansion and preserve the bounded scope of the comparison with149/133.
''')
}
manifest=[]
for name,(title,items,body) in specs.items():
 p=R/'records'/name
 old=p.read_bytes()
 # Preserve access locations without repeating the integrated source exposition.
 urls=sorted(set(re.findall(r'https?://[^\s<>\[\]`"()]+',old.decode())))
 md=f'# {title}\n\nConsolidated {utc}. The mathematical findings and their qualifications are integrated into `MPL_121_001-048_notes.md`, items {items}. This record retains inspection and retrieval scope; no frozen transcription file was modified.\n\n## Inspection scope\n'+body.strip()+'\n\n## Access URLs used\n\n'
 md+='\n'.join(f'- <{u.rstrip(".,;")}>' for u in urls)+'\n'
 md+='\n## Earlier working memo\n\nThe integrated working version had SHA-256 `'+hashlib.sha256(old).hexdigest()+'`. Its source exposition is carried in the main notes; this record supersedes the duplicate working prose.\n'
 p.write_text(md)
 manifest.append(dict(file=name,working_sha256=hashlib.sha256(old).hexdigest(),working_bytes=len(old),consolidated_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),integrated_items=items))

# The query ledger keeps query and retrieval evidence; interpretations live in the notes.
p=R/'records/research_q1_query_log.json'
j=json.loads(p.read_text())
j['memo_sha256_at_initial_completion']=j.pop('memo_sha256',None)
j['integrated_notes']='MPL_121_001-048_notes.md, Q1.1–Q1.6'
j['later_original136_check']='research_q1_cote136_source_ledger.json; supersedes initial uninspected-lead status for003,023–026 only'
j['consolidated_utc']=utc
if '151_team_verification' in j:
 v=j['151_team_verification']
 keep={k:val for k,val in v.items() if any(t in k for t in ('agent','url','scan','footer','path','sha','utc','method'))}
 keep['finding_location']='MPL_121_001-048_notes.md Q1.3'
 j['151_team_verification']=keep
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
(R/'records/research/consolidation_manifest.json').write_text(json.dumps(dict(utc=utc,records=manifest),ensure_ascii=False,indent=2)+'\n')
print('Consolidated',len(manifest),'working memos; retained source provenance and integrated findings.')
