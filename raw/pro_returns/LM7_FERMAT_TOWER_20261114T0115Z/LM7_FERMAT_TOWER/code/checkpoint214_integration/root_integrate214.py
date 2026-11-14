#!/usr/bin/env python3
"""Integrate five fully reviewed statements while retaining all original open tasks."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};reasons={};mapping=[];amendments=[]
assert not (B/'ledger/checkpoint214_integration.json').exists()
def put(rel,data,reason):
 p=B/rel;data=data.encode() if isinstance(data,str) else data
 pending[p]=data;reasons[p]=reason
def cp(src,rel):
 p=B/rel
 if p.exists():assert p.read_bytes()==src.read_bytes(),str(rel)
 else:put(rel,src.read_bytes(),'Exact owned source, actual output or retained review evidence.')
 mapping.append(dict(source=str(src.relative_to(R)),archive=str(rel),sha256=sha(src)))
def verify(folder,name,digest):
 p=folder/'ledger'/name;assert sha(p)==digest,str(p)
 m=read(p)
 for row in m['files']+m.get('immutable_inputs',[]):
  q=folder/row.get('path',row.get('file'))
  assert sha(q)==row['sha256'],str(q)
  if 'bytes' in row:assert q.stat().st_size==row['bytes']
 return m
spec=[
 ('e111','research_e111','e_nonunit_seventeen_manifest.json','c0797403ce861e6372e1c5e8d5d8fc913d577a379188a7899950a7b89b5e6286','E_nonunit_seventeen.tex','E.111','e_nonunit_seventeen'),
 ('e112','research_e112','e_quartic_five_cohomology_manifest.json','ce7a58496ba4de2512e3f18a6ce794f4a2a3c2c1fdfb3357cfc2736912c02189','E_quartic_five_cohomology.tex','E.112','e_quartic_five_cohomology'),
 ('e113','research_e113','e_quartic_compact_cups_manifest.json','e23d7679e88c774e8e84597376d6386841c2b2c9a3deaf70f365f7b752cb9837','E_quartic_compact_cups.tex','E.113','e_quartic_compact_cups'),
 ('e114','research_e114','e_inert_tail_manifest.json','48305f50a4b98dab82db936e7b3836c2694a9e60038cd41d79aa38d647817b07','E_inert_prime_tail.tex','E.114','e_inert_tail'),
 ('d60','D60_EXPERIMENTS','d_stabilizer_projective_lift_manifest.json','15d9474161603b831afcb5f8770efb5c5f6e148965f96aac9eb3f53abd1de55c','D_stabilizer_projective_lift.tex','D.60','d_stabilizer_projective_lift')]
for tag,folder,mname,digest,section,ident,stem in spec:verify(R/folder,mname,digest)
auditfolders=['root_e111_audit','a_e111_audit','a_e112_audit','root_e112_postfreeze','root_e113_audit','bc_e113_audit','root_e114_audit','root_d60_audit']
for name in auditfolders:
 p=R/name/('record_visual.json' if name=='root_e112_postfreeze' else 'audit.json')
 d=read(p);assert d.get('status',d.get('result'))=='PASS',name

# Preserve the actual previous assembly/build inputs and output logs.
for name in ['assemble.py','assemble.out','build_pdf.py','build_pdf.out','latex_pass1.out','latex_pass2.out','latex_pass3.out','bibtex.out','build_certificate.json','pdf_qa.out','package.out']:
 p=B/'code'/name
 if p.exists():cp(p,Path('code/checkpoint209_before214')/name)
cp(B/'LM7_FERMAT_TOWER_paper.tex',Path('code/checkpoint209_before214/paper_master.tex.md'))

excluded={'sources','source_images','primary_sources','vendor','__pycache__'}
allowed={'.py','.gp','.cpp','.json','.csv','.out','.md','.npz','.npy','.bin','.tex','.bib','.jpg','.txt','.patch','.diff'}
def mapped_owned(p,folder,tag):
 rel=p.relative_to(folder)
 if any(x in excluded for x in rel.parts) or p.suffix not in allowed:return None
 if rel.parts[0]=='sections':return rel
 if rel.parts[0]=='ledger':
  if p.name.endswith('_coverage.json') and isinstance(read(p),dict):return Path('ledger')/(tag+'_staging')/p.name
  return rel
 if rel.parts[0]=='qa' and p.suffix in {'.jpg','.json','.md'}:return Path('qa')/(tag+'_author')/Path(*rel.parts[1:])
 out=Path('code')/(tag+'_bundle')/rel
 if p.suffix in {'.tex','.bib','.patch','.diff'}:out=out.with_name(out.name+'.md')
 elif p.name.endswith('.source.txt'):out=out.with_name(out.name[:-11]+'.py')
 elif p.suffix=='.txt':out=out.with_name(out.name+'.md')
 if out.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():
  # An unexecuted source snapshot stays explicitly a document.
  out=out.with_name(out.name+'.md')
 return out
for tag,folder,*rest in spec:
 folder=R/folder
 for p in sorted(folder.rglob('*')):
  if p.is_file():
   dest=mapped_owned(p,folder,tag)
   if dest is not None:cp(p,dest)
for name in auditfolders:
 folder=R/name
 for p in sorted(folder.rglob('*')):
  if not p.is_file() or any(x in excluded for x in p.relative_to(folder).parts) or p.suffix not in allowed:continue
  rel=Path('code')/name/p.relative_to(folder)
  if p.suffix in {'.tex','.bib','.txt','.patch','.diff'}:rel=rel.with_name(rel.name+'.md')
  if p.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():rel=rel.with_name(rel.name+'.md')
  cp(p,rel)
 for f in ['audit.json','audit.md','verification.json','replay_result.json','record_visual.json']:
  p=folder/f
  if p.exists():cp(p,Path('ledger')/(name+'_'+f))
for ext in ['.py','.out']:cp(R/('root_record214_audits'+ext),Path('code/checkpoint214_integration')/('root_record214_audits'+ext))

# Preserve the author proof before the specifically requested exponent typo correction.
p=R/'research_e111/sections/E_nonunit_seventeen.tex'
cp(p,Path('code/e111_bundle/author_proof/E_nonunit_seventeen.tex.md'))
q=B/'sections/E_nonunit_seventeen.tex';before=pending[q].decode();after=before.replace('^{,','^{')
assert before.count('^{,')>0
pending[q]=after.encode()
amendments.append(dict(file=str(q.relative_to(B)),kind='Author-requested removal of literal leading exponent commas',count=before.count('^{,'),old='^{,',new='^{',before_sha256=sha(p),after_sha256=hashlib.sha256(after.encode()).hexdigest()))
reasons[q]='Exact author-requested exponent punctuation correction; frozen original retained.'

details={
'E.111':'E.111 completes every nonzero first multiple of kappa3(17) in the actual quotient H. All new S-class groups vanish, the four-character S-unit quotient and compact unit coordinates are evaluated, and both toric image and fibre inverse use the actual pure-factor compensations. Its intrinsic metabelian and marked preimages remain active.',
'E.112':'E.112 evaluates all five retained CM finite-S cohomology types at5 through twelve unconditionally certified degree-eight character fields, actual ideal extension/norm maps and integral Fourier projectors. Every central quartic fibre has explicit coordinates Z5^66 plus six all-prime, three split-prime and three inert-prime restricted factors. The mixed obstruction and other coefficient primes remain active.',
'E.113':'E.113 proves integral Weil-cup vanishing at every prime and removes the compact quadratic term through an explicit central cochain shift. It evaluates all nine Tate obstruction projections of the actual quartic action, with their coefficient sections and primitive maps; the exact remaining module has rank127.',
'E.114':'E.114 computes all S-class groups and every cyclic S-unit norm quotient in the positional tails j>=v3(ell+1) for every inert first prime ell. Its actual circulant character inverse, higher residue matrices and coherent divisor/compact coordinates give a split family of global H sections, while retaining the exact unevaluated lower-factor norm coupling.',
'D.60':'D.60 realizes an integral and peripheral homology replacement on two actual arithmetic character orbits, retains the complete D57 and W_h projections, and kills twelve new central blocks of total rank12288 with28 invariant coordinates. Its actual residual small-character kernel has dimension353792 and612 coinvariants; the full remaining boundary and profinite realization remain active.'
}
for tag,folder,mname,digest,section,ident,stem in spec:
 p=B/'ledger'/(stem+'_results.json');rows=json.loads(pending[p]);assert rows[0]['id']==ident
 rows[0]['notes']+=' '+details[ident]+' Exact root and independent review scopes are retained in the attached audit records.'
 # Main programs remain portable in their isolated sibling input trees.
 if 'where_proved' in rows[0]:
  rows[0]['where_proved']=rows[0]['where_proved'].replace('code/',f'code/{tag}_bundle/code/')
 pending[p]=enc(rows).encode()
 p=B/'ledger'/(stem+'_report.md')
 pending[p]+=('\n## Integrated review and current original-task scope\n\n'+details[ident]+'\n\nThe complete proof and mathematical source programs were read by root. Actual independent replay and primary-source scopes are in the attached audit records. The full integrated build and rendered-page review follow.\n').encode()

# Register each actual statement in the original master.
p=B/'LM7_FERMAT_TOWER_paper.tex';t=p.read_text()
for marker,add in [
 (r'\input{sections/D_free_character_invariant_lift.tex}',r'\input{sections/D_stabilizer_projective_lift.tex}'),
 (r'\input{sections/E_pure_tower_complete.tex}','\n'.join(r'\input{sections/'+x[4]+'}' for x in spec[:4]))]:
 assert t.count(marker)==1 and add not in t;t=t.replace(marker,marker+'\n'+add)
put(p.relative_to(B),t,'Register the five completely reviewed statements.')

p=B/'sections/E.tex';t=p.read_text();a=t.index(r'\begin{statement}{E.23}');z=t.index(r'\end{statement}',a)
new=r'''
E.111 completes every nonzero first multiple of $\kappa_3(17)$
in the actual quotient $H$, with all higher positional S-class,
S-unit and toric-fibre maps. E.114 gives the uniform evaluated
tail for every inert first prime and retains the exact lower
norm coupling. Their intrinsic metabelian and marked preimages
remain on the original list.
E.112 computes all central quartic fibres at five through the
actual character-field and coefficient maps:
$\mathbb Z_5^{66}$ and the three specified restricted-prime
families. E.113 evaluates all nine Tate obstruction projections
and removes the compact quadratic term with its literal cochain
inverse. The full mixed obstruction in the remaining rank-127
module, other coefficient primes and the higher targets remain active.
'''
put(p.relative_to(B),t[:z]+new+t[z:],'Update the original full section question without changing its Open status.')
p=B/'sections/D.tex';t=p.read_text();new=r'''
D.60 now repairs twelve further central blocks on the same
arithmetic source. Its integral projective-cover construction
retains the complete D.57 action and the prescribed $\mathcal W_h$
projection, while changing the D.59 homology action on two
explicit character orbits. The full norm and compactification
are injective on the new $12\,288$-dimensional central block,
so its twenty-eight boundary coordinates vanish by the
unquotiented orientation identity. The explicit residual
small-character module has dimension $353\,792$ and
$612$ coinvariants; its actual remaining boundary and the
full profinite realization remain to be evaluated.
'''
for ident in ['D.13','D.19']:
 a=t.index(r'\begin{statement}{'+ident+'}');z=t.index(r'\end{statement}',a);t=t[:z]+new+t[z:]
put(p.relative_to(B),t,'Update both original D questions through their actual source maps.')
for name in ['d_results.json','d_coverage.json']:
 p=B/'ledger'/name;rows=read(p)
 for row in rows:
  if name=='d_results.json' and row['id'] in ['D.13','D.19']:
   row['depends_on'].append('D.60');row['notes']+=' '+details['D.60']
  if name=='d_coverage.json' and row['task'] in ['D.e','D.afterLM2.1']:
   row['statement_ids'].append('D.60');row['outcome']+=' '+details['D.60']
   row['remaining_step']='Determine the actual residual J60 boundary, including the353792-dimensional small-character module with612 coinvariants, then the remaining full profinite source lift.'
 put(p.relative_to(B),enc(rows),'Synchronize original result and coverage rows.')

p=B/'code/assemble.py';t=p.read_text();needle='\ne_rows = []\n';assert t.count(needle)==1
eids=[x[5] for x in spec[:4]];edetail=' '.join(details[x] for x in eids)
t=t.replace(needle,"\ne_deps['E.23'].extend("+repr(eids)+")\ne_notes['E.23'] += "+repr(' '+edetail)+'\n'+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
 "        row['statement_ids'].extend(x for x in "+repr(tuple(eids))+" if x not in row['statement_ids'])\n"
 "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += "+repr('; '+edetail)+"\n"
 "        row['remaining_step'] = "+repr('Evaluate the lower norm factors for general first classes, intrinsic metabelian/marked preimages and higher layers, the mixed quartic obstruction and other coefficient primes, and mixed finite sources.')+'\n')
t=t.replace(needle,block+needle);put(p.relative_to(B),t,'Synchronize generated E rows while retaining all33 original tasks.')

# Literal prose spacing corrections observed in the209 visual review.
fixes={'scans172':'scans 172','folios733':'folios 733','equations(371)':'equations (371)',
 'Theorem1.1':'Theorem 1.1','Theorem3.5':'Theorem 3.5','Theorem7.2':'Theorem 7.2',
 'PropositionA2.1':'Proposition A2.1','Appendix2':'Appendix 2','Proposition1.6':'Proposition 1.6',
 'Theorem2.2':'Theorem 2.2','Section2':'Section 2','Sections2':'Sections 2',
 'Section3.2':'Section 3.2','Sections4':'Sections 4','Sections5':'Sections 5',
 'Theorem3.1':'Theorem 3.1','Theorem4.4':'Theorem 4.4','Proposition1':'Proposition 1',
 'Theorem1':'Theorem 1','formula(1)':'formula (1)','formulas(1)':'formulas (1)',
 'formulas(29)':'formulas (29)','Hilbert90':'Hilbert--90'}
for rel in ['sections/E_quartic_peripheral_slice.tex','sections/E_quartic_compact_action.tex','sections/E_pure_tower_complete.tex']:
 p=B/rel;before=p.read_text();after=before;changes=[]
 for old,new in fixes.items():
  n=after.count(old)
  if n:after=after.replace(old,new);changes.append(dict(old=old,new=new,count=n))
 if changes:
  put(Path(rel),after,'Exact visible prose-spacing corrections.')
  amendments.append(dict(file=rel,kind='Prose spacing only',changes=changes,before_sha256=sha(p),after_sha256=hashlib.sha256(after.encode()).hexdigest()))
put(Path('ledger/checkpoint214_presentation_amendments.json'),enc(dict(status='PASS',amendments=amendments)),'Record every presentation edit.')
p=B/'ledger/d_original_source_recheck.md';t=p.read_text()
t+='\n## Checkpoint214 public-source pass\n\nThe additional exact-title and RIMS1177 pass (retrieval family turn1001) again returned publisher metadata, the author bibliography, catalogue records and separate later works. No readable original Ihara1986, Coleman1989 or Ihara1999 PartI proof was obtained. Existing original-proof labels remain unchanged.\n'
put(p.relative_to(B),t,'Record the actual public retrieval outcome.')

# Every GP stdout alias is byte-exact; every executable source keeps actual output.
for p in list(pending):
 if p.suffix=='.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
  alt=p.with_name(p.stem+'_gp.out')
  assert alt in pending or alt.exists(),str(p)
  put(p.with_suffix('.out').relative_to(B),pending[alt] if alt in pending else alt.read_bytes(),'Byte-identical alias of actual GP stdout.')
for p in pending:
 if p.suffix in {'.py','.gp'}:
  out=p.with_suffix('.out')
  assert out in pending or out.exists(),str(p)
p=B/'code/README.md';t=p.read_text()+'\n\n## E111–E114 and D60\n\n'
t+='Each new arithmetic bundle is under code/e111_bundle through code/e114_bundle, and the actual arithmetic group programs are under code/d60_bundle. Run each mathematical Python file from its retained code/ subdirectory; sibling inputs/ are preserved. E111, E112 and E114 accept --gp /absolute/path/to/gp for complete arithmetic rebuilds. E113 accepts that flag for its corroborating local-reduction stage. D60 has the four-stage order and exact frozen raw inputs specified in its manifest.\n\n'
t+='The root/peer audit directories retain complete copied-source executions. E113 and E114 match every text and JSON byte. E114 raw BIN bytes differ, while PARI read gives exact equality of the entire four-component GEN and all five embedded base components. D60 comparisons omit only elapsed_seconds and rebuild every stage independently. E111 has a complete independent peer rebuild and additional independent maps. E112 has the same full peer replay and an actual root review of all six standalone pages.\n\n'
t+='The frozen author E111 proof remains in code/e111_bundle/author_proof/; only its specified exponent-comma typoes were corrected for presentation. Historical failed and interrupted programs retain their actual outputs/statuses. Unexecuted snapshots are explicitly .py.md or .tex.md documents. Original third-party PDFs, OCR and compiled executables remain excluded.\n'
put(p.relative_to(B),t,'Document exact reproduction and review scopes.')

changes=[]
for p,data in pending.items():
 old=sha(p) if p.exists() else None
 if p.exists() and p.read_bytes()!=data and p.parent==B/'sections':
  h=B/'sections/history/checkpoint209_before214'/p.name;h.parent.mkdir(parents=True,exist_ok=True);assert not h.exists();shutil.copy2(p,h)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 changes.append(dict(path=str(p.relative_to(B)),before_sha256=old,after_sha256=sha(p),reason=reasons[p]))
record=dict(status='PASS',added_statements=[x[5] for x in spec],expected_statement_count=214,original_task_rows=33,
 original_open_statements=['D.13','D.19','E.23'],frozen_to_archive_mapping=mapping,changes=changes,
 build_status='Assembly, full LuaLaTeX build, rendering and actual visual review follow.')
(B/'ledger/checkpoint214_integration.json').write_text(enc(record))
print(enc(dict(status='PASS',added_statements=record['added_statements'],expected_statement_count=214,changed_files=len(changes),preserved_mappings=len(mapping),presentation_amendments=len(amendments))))

