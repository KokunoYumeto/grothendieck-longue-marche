"""Make a complete, deduplicated hourly checkpoint; never overwrite one.

Omitted supplied files are identified by SHA256. Downloaded source documents,
rendered QA images, caches and reproducible runtime binaries are not deliverables.
The manifest lists every omission and its source or regeneration route.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
W=Path(__file__).resolve().parents[1]; R=W.parent
a=argparse.ArgumentParser();a.add_argument('number',type=int);args=a.parse_args()
name=f'ANABELIAN_A1_SUCCESSOR_checkpoint_{args.number:02d}.zip'
out=R/name
if out.exists(): raise SystemExit('Refusing to overwrite a checkpoint')
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        while b:=f.read(1024*1024): h.update(b)
    return h.hexdigest()
provided={}
for p in (R/'background').rglob('*'):
    if p.is_file(): provided.setdefault(digest(p),str(p.relative_to(R)))
previous={}
for p in sorted((W/'notes').glob('checkpoint_*_file_manifest.json')):
    j=json.loads(p.read_text())
    for v in j['included']: previous[v['path']]=(v['sha256'],j['checkpoint'])
included=[];omitted=[];seen={}
always={'ANABELIAN_A1_SUCCESSOR_paper.tex','ANABELIAN_A1_SUCCESSOR_paper.pdf','ANABELIAN_A1_SUCCESSOR_results.csv','ANABELIAN_A1_SUCCESSOR_references.bib','ANABELIAN_A1_SUCCESSOR_report.md','CHECK_EVENTS.tsv','PROGRESS_LEDGER.md'}
for p in sorted(W.rglob('*')):
    if not p.is_file():continue
    rel=str(p.relative_to(W));parts=set(p.relative_to(W).parts)
    if rel.startswith('notes/checkpoint_') and rel.endswith('_file_manifest.json'):continue
    why=None
    if '__pycache__' in parts or 'tex_cache' in parts or 'runtime_deps' in parts or 'qa_pages' in parts: why='Reproducible runtime/cache or rendered QA page; excluded by deliverable rule'
    if 'sources' in parts: why='Opened external primary source, recorded by URL and exact passages in the source table'
    if rel.startswith('build/') and p.suffix not in {'.log','.json','.out','.blg'}:why='Reproducible build product; final PDF and source are included at root'
    if rel.startswith('configuration/') and p.suffix in {'.pdf','.txt'} and p.name not in {'BLIND_PROTOCOL.txt'}:why='Opened external source or extraction, not a deliverable; source_records.tsv gives location'
    if p.name in {'HM2011.txt'} or 'stix_numbering_build' in parts:why='External source or generated source-reading copy; exact source recorded in references'
    if p.suffix in {'.so','.o'} or (p.suffix=='' and p.stat().st_mode&0o111):why='Reproducible executable; source and outputs retained'
    if why:
        omitted.append({'path':rel,'reason':why});continue
    sha=digest(p)
    if sha in provided and rel not in always:
        omitted.append({'path':rel,'sha256':sha,'provided_input':provided[sha]});continue
    if rel in previous and previous[rel][0]==sha and rel not in always:
        omitted.append({'path':rel,'sha256':sha,'checkpoint':previous[rel][1]});continue
    if sha in seen and rel not in always:
        omitted.append({'path':rel,'sha256':sha,'identical_in_this_checkpoint':seen[sha]});continue
    included.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha});seen[sha]=rel
manifest={'checkpoint':name,'schema':1,'included':included,'omitted':omitted,'restore':'Extract latest checkpoint; restore paths named from earlier checkpoints; supplied input paths are in the original background ZIP. Duplicate paths can be copied from identical_in_this_checkpoint. Run code/build_paper.py for the PDF; original-source-dependent assembly additionally requires the supplied background inputs.'}
mp=W/'notes'/f'checkpoint_{args.number:02d}_file_manifest.json';mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
    for v in included:z.write(W/v['path'],v['path'])
    z.write(mp,'FILE_MANIFEST.json')
if out.stat().st_size>=500_000_000:raise SystemExit('Archive exceeds the requested 500 MB limit')
with zipfile.ZipFile(out) as z:
    bad=z.testzip()
    if bad:raise SystemExit('CRC failure: '+bad)
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'sha256':digest(out),'files':len(included)+1,'omitted':len(omitted)}))
