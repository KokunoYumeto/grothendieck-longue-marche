"""Consolidate research fragments without touching the frozen transcription."""
from pathlib import Path
from datetime import datetime,timezone
import re,json,csv,subprocess
R=Path(__file__).resolve().parents[1]
header=r'''# MPL_67_053–101 — Research notes

## Scope, attribution, and evidence

These notes concern cote67, scans53–101, with the supplied blank scans83 and90 omitted. The diplomatic transcription was completed, audited against every supplied whole image and both halves, compared for recurring notation, and frozen at **2026-11-18 01:15:15UTC**; the supplied context was first opened at **01:15:25UTC**. Nothing learned from that context was used to change a frozen page.

The manuscript, the supplied modernised reading, earlier research notes, and checks in this run have separate evidential roles. **Hua** means **Michel Hua’s project, modernised reading of cote67**, supplied as `hua_project/67.modern.tex`; it is an attributed interpretation, not another manuscript witness. A source labelled “Proved,” “Known,” or “Refuted” in `notes/RESULTS_STATE.md` remains that run’s claim unless the specific argument was actually rechecked here; the claimed Lean verification of the module–triple equivalence was not rerun because its source/certificate was not supplied.

Citations to context files are relative to the original context ZIP; some specialist notes retain the local prefix `context/`, which denotes that same supplied source set. Hua’s printed page *p* corresponds to this task’s **scan p+1**, not to the archive pencil foliation or Grothendieck’s handwritten numbering. Approximate locations refer to the frozen transcription; question-mark alternatives and cancellations are not silently resolved by the research notes.

There are **100 research notes** (S01–S34, B01–B19, O01–O16, E01–E30, P01), plus the separate **33-item self-flag census** and **12-item title/page-count census** below. Every numbered item has an actual context search recorded in `research/*/search_ledger.json`, `research/census_search_ledger.json`, or `research/plan_search_ledger.json`; a search hit establishes a lead, not a proof. `CHECK_EVENTS.tsv` distinguishes proof checks, exact computations, source comparisons, background use, and qualified refutations, retaining the run responsible for each event.

The root assistant alone transcribed and audited the images. Parallel work began only after the freeze and was confined to research: the octahedral, real-elliptic, and contextual-bridge sections; subsequent cross-reviews checked selected mathematical arguments without changing any transcription. These are in-run checks, not external referee verdicts or claims of novelty.

## Navigation and supporting arguments

| Material | Notes | Detailed checks |
|---|---|---|
| Boundary regularity, cutting/welding, capping, shadows, and stable-curve surgery | S01–S34 | `research/surgery/proofs.md`; limited primary-source checks W1–W4 in `research/surgery/web_sources.md` |
| Longue Marche §§37/53, normal frames, groupoids, and limits of open-register comparisons | B01–B19 | Local covariance and radial-fibre checks in the notes and event ledger |
| Octahedron, Klein-four torsors, exceptional characteristics, and four-point moduli | O01–O16 | `research/octahedron/proof_checks.md`; two exact-computation scripts and JSON certificates |
| Real elliptic curves, module involutions, quadratic ratios, and torsors | E01–E30 | `research/elliptic/proofs.md`; exact arithmetic script and JSON record |
| Explicit hedges, assumed steps, and same-text withdrawals | F01–F33 | Dedicated census, with links back to the detailed notes |
| Written headings, dates, manuscript numbers, and printed identifiers | T01–T12 | Dedicated census; author numbering remains distinct from scan count |
| Supplied planning question | P01 | Scope comparison with `README.md` and the context map |
| Hua’s complete modernised reading | 36-row coverage map | Every section and subsection read; §§I–V lie outside this packet |

The independently reviewed arguments are documented in `research/elliptic/surgery_review.md` and `research/octahedron/elliptic_review.md`; those reviews retain the same scope limits as the original notes. Longer proofs are kept in these supporting files so each numbered research note remains a short, separately assessable item.

## Relation to the supplied package plan

### P01 — The packet confirms the subject placement, but contains no Bers letter

**67/054, 070, 084, 091–101; kind: unpursued implication; words: “Chirurgie conforme,” “Retour sur le principe,” and “Courbes elliptiques réelles.”** The supplied pages **confirm** `README.md`’s BookIII.6 placement through conformal surgery and uniformization (53–82), add a finite four-point/octahedral block (84–89), and explicitly develop real elliptic curves and torsors (91–101). They contain no Bers letter, so this packet neither verifies nor refutes the planning claim that the1984 letter is in print; Hua §III locates that letter on their pp.15–21 (= scans16–22), outside the supplied range. The proposed Longue Marche bridges are concrete at §37 scans537–555 and §53 scans225–227,259–260 (B02,B06,B15,O01,O13), while the absent rank4 returns and the unprovided Q1-07 comparison remain source gaps rather than inferred results.

'''
surgery=(R/'research/surgery/notes.md').read_text()
bridges=(R/'research/bridges/notes.md').read_text()
bridge_notes=bridges.split('## Bridge notes\n',1)[1].split('## Complete coverage of Hua',1)[0]
coverage='## Complete coverage of Hua'+bridges.split('## Complete coverage of Hua',1)[1]
octa=(R/'research/octahedron/notes.md').read_text()
octa=octa.split('\n',1)[1].strip()
octa=re.sub(r'^## (O\d{2})',r'### \1',octa,flags=re.M)
elliptic=(R/'research/elliptic/notes.md').read_text()
elliptic=elliptic.split('\n',1)[1].strip()
censuses=(R/'research/censuses.md').read_text()
censuses=re.sub(r'^# ', '## ',censuses,flags=re.M)
web=(R/'research/surgery/web_sources.md').read_text()
text=header+surgery+'\n\n## B. Bridges to the supplied archive context and research register\n\n'+bridge_notes+'\n## C. Octahedron and four-point moduli\n\n'+octa+'\n\n## D. Real elliptic curves, involution modules, and torsors\n\n'+elliptic+'\n\n'+censuses+'\n\n'+coverage+'\n\n## Primary literature consulted\n\n'+web.split('\n',1)[1].strip()+'\n'
(R/'MPL_67_053-101_notes.md').write_text(text)
# The planning item has its own real search, just as each other note does.
q='Chirurgie conforme|Courbes elliptiques|Bers|rank.?4|Q1-07|37|53'
p=subprocess.run(['rg','--json','-i',q,str(R.parent/'context')],capture_output=True,text=True)
assert p.returncode==0
hits=[];counts={}
for line in p.stdout.splitlines():
 d=json.loads(line)
 if d.get('type')!='match':continue
 d=d['data'];fn=str(Path(d['path']['text']).relative_to(R.parent/'context'));counts[fn]=counts.get(fn,0)+1
 if counts[fn]<=2:hits.append({'file':fn,'line':d['line_number'],'text':d['lines']['text'].strip()[:300]})
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'research/plan_search_ledger.json').write_text(json.dumps({'note':'P01','timestamp_utc':now,'query':q,'counts':counts,'sample_hits':hits,'selected':'README.md, planning question; Hua §§III,VII,XI,XII; B02/B06/B15/O01/O13 locators'},ensure_ascii=False,indent=2)+'\n')
with (R/'research/plan_checks.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerow(['P01',now,'GPT-6 Astra Pro; effort not exposed; run MPL_67_053-101/root consolidation','carried as background without fault found','Compared packet subjects and headings with context README. No current Bers-letter evidence or rank4 return; no claim of proof or publication verification.'])
# Preserve the original specialist rows; expand multi-entry register aliases only in the consolidated ledger.
paths=sorted(set((R/'research').rglob('checks.tsv'))|set((R/'research').rglob('*_checks.tsv')))
field=['statement_id','date','who','type','outcome']
expand={
 'EXIT_TOWER E.23/E.35/E.36':['EXIT_TOWER E.23','EXIT_TOWER E.35','EXIT_TOWER E.36'],
 'MPL_147_003-047 N075; WG2 §1.1 #6; WG2 §Summary #1':['MPL_147_003-047 N075','WG2 §1.1 #6','WG2 §Summary #1'],
 'LM2 C.r2/C.r3/C.d3/C.d5':['LM2 C.r2','LM2 C.r3','LM2 C.d3','LM2 C.d5']}
rows=[]
for path in paths:
 with path.open(newline='') as f:
  rd=csv.DictReader(f,delimiter='\t');assert rd.fieldnames==field,(str(path),rd.fieldnames)
  for row in rd:
   assert all(row.get(k) for k in field),row
   for s in expand.get(row['statement_id'],[row['statement_id']]):
    copy=row.copy();copy['statement_id']=s;rows.append(copy)
with (R/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=field,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(R/'records/research_assembly.json').write_text(json.dumps({'assembled_utc':now,'main_research_note_count':100,'self_flagged_count':33,'title_count_items':12,'check_event_rows':len(rows),'event_sources':[str(x.relative_to(R)) for x in paths],'note_families':['S01–S34','B01–B19','O01–O16','E01–E30','P01'],'approximate_words':len(text.split())},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'notes_words':len(text.split()),'event_rows':len(rows),'event_source_files':len(paths)}))
