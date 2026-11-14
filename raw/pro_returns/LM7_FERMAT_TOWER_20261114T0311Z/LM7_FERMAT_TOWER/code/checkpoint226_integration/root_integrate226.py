#!/usr/bin/env python3
"""Integrate frozen E122 and D65, complete audits and lossless image layout."""
from pathlib import Path
import csv,hashlib,json,shutil

R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
digest=lambda b:hashlib.sha256(b).hexdigest()
enc=lambda d:json.dumps(d,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};reasons={};mapping=[];amendments=[]
assert not (B/'ledger/checkpoint226_integration.json').exists()
with (B/'LM7_FERMAT_TOWER_results.csv').open() as f:assert len(list(csv.DictReader(f)))==224
def put(rel,data,reason):
    p=B/rel;pending[p]=data.encode() if isinstance(data,str) else data;reasons[p]=reason
def get(rel):
    p=B/rel;return pending[p] if p in pending else p.read_bytes()
def cp(src,rel):
    p=B/rel;data=src.read_bytes()
    if p.exists():assert p.read_bytes()==data,str(rel)
    elif p in pending:assert pending[p]==data,str(rel)
    else:put(rel,data,'Exact frozen source, actual output or review evidence.')
    mapping.append({'source':str(src.relative_to(R)),'archive':str(rel),'sha256':digest(data)})
spec=[
 ('e122','research_e122','e_fiftythree_higher_manifest.json',
  '9f63758a401fad7db429d657ab7008f98d0f4e864580b9ca517876597735cd9e',
  'E_fiftythree_higher_action.tex','E.122','e_fiftythree_higher'),
 ('d65','D65_EXPERIMENTS','d_divided_compact_source_manifest.json',
  'a0912a250ef5a225f30471f02de19b569333813c81ed66adfa0af0be2b25cde1',
  'D_divided_compact_source.tex','D.65','d_divided_compact_source')]
def verify(folder,name,expected):
    p=folder/'ledger'/name;assert sha(p)==expected,str(p);m=read(p)
    for row in m.get('files',m.get('owned_files',[])):
        q=folder/row['path'];assert sha(q)==row['sha256'],str(q)
        if 'bytes' in row:assert q.stat().st_size==row['bytes']
    for row in m.get('immutable_inputs',[]):
        assert sha(R/row['source'])==sha(R/row['copied'])==row['sha256']
    return m
manifests={tag:verify(R/folder,name,expected) for tag,folder,name,expected,*_ in spec}
audits={
 'root_e122_audit':('final_replay_audit.json','167c126245a5907a92a5f2bf62f12e2986567844fe50c3abaea27a434362025a'),
 'd_e122_audit':('audit.json','be7cb3def61db66250ebedc63984a5f073502b45f6c208bb1bdaa7f27dd2e436'),
 'root_d65_audit':('replay_audit.json','a064c6ea55c2bc71297413ad40b082e9d98d95a426776571129946ecde11c741'),
 'bc_d65_audit':('audit.json','bdbe10edc5149744f100baff791cab6f5d28454457ebdf1f4066f9031027ef4e')}
for folder,(name,expected) in audits.items():
    p=R/folder/name;assert sha(p)==expected and read(p)['status']=='PASS'
assert read(R/'root_archive_format/image_roundtrip224.json')['status']=='PASS'
assert read(R/'.lm7_archive224_lzma_readback.json')['status']=='PASS'
for name in ['assemble.py','assemble.out','build_pdf.py','build_pdf.out','latex_pass1.out',
             'latex_pass2.out','latex_pass3.out','bibtex.out','build_certificate.json',
             'pdf_qa.out','package.py','package.out','ARCHIVE_README.md']:
    p=B/'code'/name
    if p.exists():cp(p,Path('code/checkpoint224_before226')/name)
for name in ['LM7_FERMAT_TOWER_paper.tex','LM7_FERMAT_TOWER_manifest.json']:
    cp(B/name,Path('code/checkpoint224_before226')/(name+'.md' if name.endswith('.tex') else name))
for p in sorted((B/'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_','detail224_','visual224_')) or p.name in ['pdf_qa.json','visual_review.md']):
        cp(p,Path('qa/history/checkpoint224_before226')/p.name)
excluded={'sources','source_images','primary_sources','vendor','__pycache__','fresh224_images'}
allowed={'.py','.gp','.cpp','.json','.csv','.out','.err','.md','.npz','.npy','.bin',
         '.tex','.bib','.jpg','.png','.pdf','.aux','.log','.txt','.patch','.diff'}
def owned_path(p,folder,tag):
    rel=p.relative_to(folder)
    if any(x in excluded for x in rel.parts) or p.suffix not in allowed:return None
    if rel.parts[0]=='sections' and len(rel.parts)==2:return rel
    if rel.parts[0]=='ledger':
        if p.name.endswith('_coverage.json') and isinstance(read(p),dict):return Path('ledger')/(tag+'_staging')/p.name
        return rel
    out=(Path('qa')/(tag+'_author')/Path(*rel.parts[1:]) if rel.parts[0]=='qa'
         else Path('code')/(tag+'_bundle')/rel)
    if p.suffix in {'.tex','.bib','.patch','.diff'}:out=out.with_name(out.name+'.md')
    # Actual text inputs retain their native filenames, including the E122
    # GP literal-witness input. They are included by the revised packager.
    source_stdout=p.with_suffix('.out')
    if out.suffix in {'.py','.gp'} and not source_stdout.exists() and not p.with_name(p.stem+'_gp.out').exists():
        out=out.with_name(out.name+'.md')
    return out
for tag,folder_name,*_ in spec:
    folder=R/folder_name
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            out=owned_path(p,folder,tag)
            if out is not None:cp(p,out)
    for row in manifests[tag].get('files',manifests[tag].get('owned_files',[])):
        out=owned_path(folder/row['path'],folder,tag)
        assert out is not None and digest(get(out))==row['sha256'],row['path']
    for row in manifests[tag].get('immutable_inputs',[]):
        p=R/row['copied'];out=owned_path(p,folder,tag)
        assert out is not None and digest(get(out))==row['sha256']
    for p in (folder/'ledger').glob('*'):
        if p.is_file() and p.name.endswith(('_results.json','_report.md')):
            cp(p,Path('code')/(tag+'_bundle/author_freeze/ledger')/p.name)
for folder_name in list(audits)+['root_archive_format']:
    folder=R/folder_name
    for p in sorted(folder.rglob('*')):
        rel=p.relative_to(folder)
        if not p.is_file() or any(x in excluded for x in rel.parts) or p.suffix not in allowed:continue
        out=Path('code')/folder_name/rel
        if p.suffix in {'.tex','.bib','.patch','.diff'}:out=out.with_name(out.name+'.md')
        if p.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():
            out=out.with_name(out.name+'.md')
        cp(p,out)
    if folder_name in audits:
        fn=audits[folder_name][0];cp(folder/fn,Path('ledger')/(folder_name+'_'+fn))
for name in ['root_archive224_lzma_readback.py','root_archive224_lzma_readback.out','root_archive224_lzma_readback.err',
             'root_bind226_outputs.py','root_bind226_outputs.out','root_bind226_outputs.err','root_output_bindings226.json']:
    cp(R/name,Path('code/checkpoint226_integration')/name)
cp(R/'.lm7_archive224_lzma_readback.json',Path('ledger/archive224_lzma_readback.json'))
details={
 'E.122':'E.122 evaluates the entire B_d positional53 three-primary S-class tower. All actual norms from level2 onward are isomorphisms, giving C9+C3^3 and the same inverse limit through literal norm coordinates; extension is three times the actual norm inverse and the horizontal H action is retained. Twenty-two literal cube/norm witnesses supply the full rank-five local character hyperplane, killing K2; the proved actual recurrence K_d=j_dK_(d-1) gives every later kernel. The complete first embedded unit norm image is the six-row congruence lattice of index729 with actual preimages. Later unit norm quotients are C3^9 and completed kernels are mu3+Z3^(2*3^(d+1)), through explicit local-character/Hilbert90 maps. Coherent positional unit/divisor inverse systems, separate lower factors, and the intrinsic section maps remain active.',
 'D.65':'D.65 constructs an actual peripheral action on X/J65, extending the retained compact quotient by5752 dimensions and12 coinvariants. The actual signed integral exterior norm divided by two has rank6 in each ten-dimensional compact test; an actual coinduced source correction realizes its entire image, and eight source-involution words kill its rank4 kernels. Both D57 branches, literal small conjugators and complete W_h/metabelian/CM maps survive. The lower Y action is exactly Int(b_t,Y) beta_Y with the displayed derivation and all36 cusp terms. The specified residual J65 has dimension276478 and maps onto the old1918-dimensional compact norm kernel. Its two remaining tested coordinates retain their precise test scope; full residual and profinite realization remain active.'}
reviews={
 'E.122':'Root read all624 final proof lines and all470 mathematical source lines and performed the complete three-GP/two-Python copied-source replay. All seven whole text outputs match byte for byte and all three complete decoded GEN objects agree, with no exclusions; all171 frozen hashes were rechecked. The independent peer read the same complete proof and sources, then independently checked22 cube/norm identities, ten complete principal divisors, both243-element genus kernels,165 local norm columns, all22 upper characters, the243-element hyperplane and the complete729-element norm quotient. No correction was requested.',
 'D.65':'Root read all643 final proof lines and all1346 mathematical source lines, then replayed all eight complete programs from eight immutable inputs. All whole JSON/stdout files agree under the explicit clock-only projection; no algebraic field or input hash is excluded, and all actual fresh outputs remain retained. The independent peer read the full proof and all eight sources and independently reconstructed512 modulo-four norm columns,1024 trace columns,2048 coinvariant vectors,3072 orientation identities and80 correction columns. The actual integral source extension, odd-cover/Fourier comparison and post-word moving repair were checked. No correction was requested.'}
for tag,folder,name,expected,section,ident,stem in spec:
    rel=Path('ledger')/(stem+'_results.json');before=get(rel);rows=json.loads(before)
    assert len(rows)==1 and rows[0]['id']==ident
    if isinstance(rows[0]['notes'],list):rows[0]['notes']=' '.join(rows[0]['notes'])
    rows[0]['notes']+=' '+details[ident]+' '+reviews[ident]
    rows[0]['where_proved']=rows[0]['where_proved'].replace('code/',f'code/{tag}_bundle/code/')
    if isinstance(rows[0]['manuscript_passages'],list):rows[0]['manuscript_passages']='; '.join(rows[0]['manuscript_passages'])
    after=enc(rows);put(rel,after,'Append completed reviews and exact original-task scope.')
    amendments.append({'file':str(rel),'before_sha256':digest(before),'after_sha256':digest(after.encode()),
                       'author_freeze':str(Path('code')/(tag+'_bundle/author_freeze/ledger')/rel.name)})
    rel=Path('ledger')/(stem+'_report.md');before=get(rel)
    after=before.decode()+'\n\n## Completed integration reviews\n\n'+reviews[ident]+'\n\n## Original-task scope\n\n'+details[ident]+'\n'
    put(rel,after,'Append completed reviews; retain exact original report.')
    amendments.append({'file':str(rel),'before_sha256':digest(before),'after_sha256':digest(after.encode()),
                       'author_freeze':str(Path('code')/(tag+'_bundle/author_freeze/ledger')/rel.name)})
rel=Path('LM7_FERMAT_TOWER_paper.tex');t=get(rel).decode()
for old,new in [(r'\input{sections/D_compact_isometry_source.tex}',r'\input{sections/D_divided_compact_source.tex}'),
                (r'\input{sections/E_fiftythree_normalizer.tex}',r'\input{sections/E_fiftythree_higher_action.tex}')]:
    assert t.count(old)==1 and new not in t;t=t.replace(old,old+'\n'+new)
put(rel,t,'Register both completely audited proofs.')
rel=Path('sections/E.tex');t=get(rel).decode();a=t.index(r'\begin{statement}{E.23}');z=t.index(r'\end{statement}',a)
new=r'''
E.122 evaluates the entire $B_d$ positional-$53$ S-class tower.
The actual norms from level two onward identify every class group
and the inverse limit with $C_9\oplus C_3^3$; extension is three
times their specified inverse and the horizontal action remains H.
Twenty-two literal cube and norm witnesses give the full rank-five
local character hyperplane. They evaluate $K_2=0$, and the proved
actual recurrence $K_d=j_dK_{d-1}$ kills every later norm kernel.
The first embedded unit norm image has its six explicit congruences,
index $729$ and actual preimage map. Every later unit norm quotient
is $C_3^9$, with completed kernel
$\mu_3\oplus\mathbb Z_3^{2\cdot3^{d+1}}$ through the stated maps.
Compatible positional unit/divisor inverse systems, the separate
lower factors and the intrinsic section comparisons remain active.
'''
put(rel,t[:z]+new+t[z:],'Record evaluated all-level class factor and exact remaining maps.')
rel=Path('sections/D.tex');t=get(rel).decode()
new=r'''
D.65 retains the full second and third compact blocks by an actual
integral source correction. Its signed exterior norm divided by two
has rank six in each ten-dimensional test. Coinduction realizes the
full image, and the actual source-involution words kill both rank-four
kernels. The further quotient has dimension $5752$ and twelve
coinvariants, with total retained dimension $7682$ and twenty-six
coinvariants. Both D.57 branches, literal small conjugators and the
full $\mathcal W_h$ maps are retained. The lower action is exactly
$\operatorname{Int}(b_{t,Y})\beta_Y$ with its stated derivation and
all thirty-six cusp factors. The remaining specified kernel has
dimension $276\,478$ and maps onto the old compact norm kernel of
dimension $1918$. Its two remaining tested coordinates retain that
test scope. The residual source boundary and full profinite
realization continue to require their actual lifts.
'''
for ident in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+ident+'}');z=t.index(r'\end{statement}',a);t=t[:z]+new+t[z:]
put(rel,t,'Record actual D65 source comparison and specified residual.')
for name in ['d_results.json','d_coverage.json']:
    rel=Path('ledger')/name;rows=json.loads(get(rel))
    for row in rows:
        if name=='d_results.json' and row['id'] in ['D.13','D.19']:
            assert 'D.65' not in row['depends_on'];row['depends_on'].append('D.65');row['notes']+=' '+details['D.65']
        if name=='d_coverage.json' and row['task'] in ['D.e','D.afterLM2.1']:
            row['statement_ids'].append('D.65');row['outcome']+=' '+details['D.65']
            row['remaining_step']='Evaluate the actual boundary in J65 (specified dimension276478 and surjection to the old1918-dimensional compact norm kernel), then the full profinite realization. Its two uncovered old compact-test coordinates are not assigned to the whole J65 coinvariant group.'
    put(rel,enc(rows),'Synchronize original D result and task rows.')
rel=Path('code/assemble.py');t=get(rel).decode();needle='\ne_rows = []\n';assert t.count(needle)==1
t=t.replace(needle,"\ne_deps['E.23'].append('E.122')\ne_notes['E.23'] += "+repr(' '+details['E.122'])+'\n'+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
       "        row['statement_ids'].extend(x for x in ('E.122',) if x not in row['statement_ids'])\n"
       "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += "+repr('; '+details['E.122'])+'\n'
       "        row['remaining_step'] = "+repr('Evaluate intrinsic class-three and later section maps, further quartic quotients and coefficient primes; construct compatible positional unit/divisor inverse systems and the separate lower factors. E122 has evaluated the entire positional53 B_d class tower and every finite one-step unit defect.')+'\n')
t=t.replace(needle,block+needle);put(rel,t,'Synchronize generated E23 and all33 original-task rows.')
put(Path('code/package.py'),(R/'root_archive_format/package226.py').read_bytes(),'Use verified lossless image aliases and retain literal text inputs.')
for name in ['materialize_archive_images.py','materialize_archive_images.out','materialize_archive_images.err']:
    cp(R/'root_archive_format'/name,Path('code')/name)
put(Path('code/ARCHIVE_README.md'),(R/'root_archive_format/ARCHIVE_README226.md').read_bytes(),'Document exact extraction and logical image restoration.')
rel=Path('code/README.md')
put(rel,get(rel).decode()+'\n\n## E122 and D65\n\n'+reviews['E.122']+'\n\n'+reviews['D.65']+'\n\n'+details['E.122']+'\n\n'+details['D.65']+'''

All literal E122 text inputs retain their native filenames, including
inputs/e122_literal_unit_witnesses.txt. The complete arithmetic replay
uses those explicit relative input paths. Exact author ledgers are in
each bundle's author_freeze/ledger; active ledger amendments are recorded
separately. Root and peer execution scopes are not interchanged.

The archive stores exact duplicate QA image bytes once with an explicit
logical-path map. All mathematical sources, inputs and outputs remain
ordinary members. See ARCHIVE_README.md for exact restoration; all prior
logical image bytes and their hashes are retained.
''','Document new complete evidence and exact archive layout.')
for p in list(pending):
    if p.suffix=='.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
        alt=p.with_name(p.stem+'_gp.out');assert alt in pending or alt.exists(),str(p)
        put(p.with_suffix('.out').relative_to(B),get(alt.relative_to(B)),'Exact alias of actual GP stdout.')
for p in pending:
    if p.suffix in {'.py','.gp'}:assert p.with_suffix('.out') in pending or p.with_suffix('.out').exists(),str(p)
for item in mapping:
    if digest(get(Path(item['archive'])))!=item['sha256']:
        change=next(a for a in amendments if a['file']==item['archive'])
        assert change['before_sha256']==item['sha256'];item['active_editorial_path']=item['archive'];item['archive']=change['author_freeze']
    assert digest(get(Path(item['archive'])))==item['sha256'],item
put(Path('ledger/checkpoint226_amendments.json'),enc({'status':'PASS','amendments':amendments}),'Record exact editorial amendments and unchanged originals.')
for tag,folder,name,expected,*_ in spec:verify(R/folder,name,expected)
changes=[]
for p,data in pending.items():
    old=sha(p) if p.exists() else None
    if p.exists() and p.read_bytes()!=data:
        if p.parent==B/'sections':h=B/'sections/history/checkpoint224_before226'/p.name
        elif p.parent==B/'ledger':h=B/'code/checkpoint224_before226/ledger'/p.name
        else:h=None
        if h is not None:
            h.parent.mkdir(parents=True,exist_ok=True);assert not h.exists();shutil.copy2(p,h)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    changes.append({'path':str(p.relative_to(B)),'before_sha256':old,'after_sha256':sha(p),'reason':reasons[p]})
record={'status':'PASS','added_statements':['E.122','D.65'],'expected_statement_count':226,'original_task_rows':33,
        'original_open_statements':['D.13','D.19','E.23'],'frozen_to_archive_mapping':mapping,
        'changes':changes,'active_ledger_amendments':amendments,
        'build_status':'Assembly, LuaLaTeX build, integrated visual review and physical/logical archive verification follow.'}
(B/'ledger/checkpoint226_integration.json').write_text(enc(record))
print(enc({'status':'PASS','expected_statement_count':226,'mapped_frozen_files':len(mapping),
           'written_files':len(changes),'original_task_rows':33,'all_frozen_mappings_match_actual_archive_bytes':True}),end='')
