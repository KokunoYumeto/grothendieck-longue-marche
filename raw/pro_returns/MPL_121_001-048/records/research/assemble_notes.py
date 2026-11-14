"""Assemble research notes and document searches; frozen files are read-only."""
from pathlib import Path
import json,re,hashlib
from datetime import datetime,timezone

R=Path(__file__).resolve().parents[2]
W=R.parent
D=R/'records/research'
q=(D/'question_notes.md').read_text()
if q.startswith('# Consolidated question-note record'):
 previous=(R/'MPL_121_001-048_notes.md').read_text()
 start=previous.index('## Answers to the four requested questions')
 end=previous.index('## Page-by-page research register',start)
 q=previous[start:end].strip()+'\n'
terms={
'Q1.1':['ombre','tubul','X_J'],
'Q1.2':['voisinage tubulaire','germe',r'D\prime'],
'Q1.3':['tubulaire','voisinage','germe'],
'Q1.4':['ombre','module','localisé'],
'Q1.5':['localisation','germe','faisceau'],
'Q1.6':['ombre','module'],
'Q2.1':['Remords','reconstituer','S^2'],
'Q2.2':['Remords','gerbe','cohomologie'],
'Q2.3':['drapeau','Delta','reconstituer'],
'Q2.4':['Remords','1981','décembre'],
'Q2.5':['flèche','topos','S^2'],
'Q2.6':['gerbe','extension','cohomologie'],
'Q2.7':['amalgam','groupoïde','S^2'],
'Q2.8':['groupoïde','homotopie','Remords'],
'Q3.1':['modéré','stratification','parties'],
'Q3.2':['compact','produit','morphisme'],
'Q3.3':['connexe','rare','adhérence'],
'Q3.4':['quotient','cellulaire','connexe'],
'Q3.5':['constante','structure','modéré'],
'Q3.6':['analytique','local','faisceau'],
'Q3.7':['local','faisceau','modéré'],
'Q3.8':['localement','fini','connexe'],
'Q3.9':['local','connexe','stratification'],
'Q4.1':['modéré','drapeau','isomorphisme'],
'Q4.2':['partition','homéomorph','modéré'],
'Q4.3':['isotopie','homéomorph','modéré'],
'Q4.4':['isotopie','homotopie','morphisme'],
'Q4.5':['homéomorph','compact','modéré'],
'Q4.6':['isotopie','morphisme','homéomorph'],
'Q4.7':['drapeau','maquette','homotopie'],
}
ids=re.findall(r'^#### (Q\d+\.\d+) —',q,re.M)
assert len(ids)==30 and set(ids)==set(terms)
parts=[]
for f in sorted((W/'context').glob('*transcription.tex')):
 sp=re.split(r'\\scanpage\{(\d+)\}',f.read_text())
 for i in range(1,len(sp),2):parts.append((f.name,int(sp[i]),sp[i+1]))
audit=[]
for id in ids:
 hits=[]
 for fn,scan,body in parts:
  found=[t for t in terms[id] if re.search(re.escape(t),body,re.I)]
  if found:hits.append(dict(file=fn,scan=scan,terms=found))
 audit.append(dict(note=id,terms=terms[id],hits=hits))
(D/'question_context_search_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')

out='\n\n'.join([(D/'notes_frontmatter.md').read_text().strip(),q.strip(),(D/'root_notes.md').read_text().strip(),(D/'standing_sections.md').read_text().strip(),(D/'bibliography.md').read_text().strip()])+'\n'
assert 'undergoing a targeted' not in out
assert out.count('### N')==85
assert len(re.findall(r'^#### Q\d+\.\d+ —',out,re.M))==30
dest=R/'MPL_121_001-048_notes.md'
dest.write_text(out)
print(json.dumps(dict(file=str(dest),bytes=dest.stat().st_size,words=len(out.split()),current_page_items=85,question_items=30,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()),indent=2))

utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'progress.log').open('a') as f:
 f.write(f'research notes assembled {utc}; 85 current-page items; 30 question items; primary-source and scope reviews integrated; transcription unchanged\n')
