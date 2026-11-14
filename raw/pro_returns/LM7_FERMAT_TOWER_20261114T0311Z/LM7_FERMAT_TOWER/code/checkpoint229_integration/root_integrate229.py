#!/usr/bin/env python3
"""Integrate three frozen proofs, four exact elliptic comparisons and audits."""
from pathlib import Path
import csv,hashlib,json,shutil

R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
digest=lambda b:hashlib.sha256(b).hexdigest()
enc=lambda d:json.dumps(d,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};reasons={};mapping=[];amendments=[]
assert not (B/'ledger/checkpoint229_integration.json').exists()
with (B/'LM7_FERMAT_TOWER_results.csv').open() as f:assert len(list(csv.DictReader(f)))==226
def put(rel,data,reason):
    p=B/rel;pending[p]=data.encode() if isinstance(data,str) else data;reasons[p]=reason
def get(rel):
    p=B/rel;return pending[p] if p in pending else p.read_bytes()
def cp(src,rel):
    p=B/rel;data=src.read_bytes()
    if p in pending:assert pending[p]==data,str(rel)
    elif p.exists():assert p.read_bytes()==data,str(rel)
    else:put(rel,data,'Exact frozen source, actual output or reviewed evidence.')
    mapping.append({'source':str(src.relative_to(R)),'archive':str(rel),'sha256':digest(data)})

spec=[
 ('e123','research_e123','e_fiftythree_positional_manifest.json',
  'f375db968bbce03f11ca1ea434a9c52f7998cc87a6426ea69e9183909336224a',
  'E_fiftythree_positional_stable.tex','E.123','e_fiftythree_positional'),
 ('d66','D66_EXPERIMENTS','d_quadratic_compact_source_manifest.json',
  '1d77562247b199c5c78f1a4a8b71d4474a3e7d9d3031f43c3dce7ff5ddb71ada',
  'D_quadratic_compact_source.tex','D.66','d_quadratic_compact_source'),
 ('e124','research_after_e123','e_fiftythree_ordinary_manifest.json',
  '2ee0a1016536f05016a20f99b92b2fb813ebf0959330b7414cd9847cdcee943c',
  'E_fiftythree_ordinary_valuation.tex','E.124','e_fiftythree_ordinary')]
espec=[
 ('a_elliptic_tor_symbol_manifest.json','14116ce60b91b8968fa659dc022e3f4cbe02d13c9b50ef583d427207452c9001'),
 ('a_theta_principal_distribution_manifest.json','c59f0dcd88e32fcc42422611050ecfe6dac5532ae6936b1d4615b769199f9e26'),
 ('a_elliptic_log_torsor_manifest.json','c288aafb2017b0fcc0da339ddc63e7c3404736e0b1a9bdd27d3241e7ab789d90'),
 ('a_principal_cubic_cover_manifest.json','e26f6e1ab7d3998b0d530a2f8e0be3c5aeb41c20a7255c74afab6b0ea5de18f3')]
def declared(m):return m.get('owned_files',m.get('owned',m.get('files',[])))
def verify(folder,name,expected):
    p=folder/'ledger'/name;assert sha(p)==expected,str(p);m=read(p)
    for row in declared(m):
        q=folder/row['path'];assert sha(q)==row['sha256'],str(q)
        if 'bytes' in row:assert q.stat().st_size==row['bytes']
    for row in m.get('immutable_inputs',[]):
        if 'path' in row:q=folder/row['path']
        else:
            q=R/row['copied'];assert sha(R/row['source'])==row['sha256']
        assert sha(q)==row['sha256'],str(q)
        if 'bytes' in row:assert q.stat().st_size==row['bytes']
    return m
manifests={tag:verify(R/folder,name,h) for tag,folder,name,h,*_ in spec}
em={name:verify(R/'research_e120',name,h) for name,h in espec}
audits={
 'root_e123_audit':('replay_audit.json','d68e18cc2dd21dbd459873fd6109523782ad70a8f3bab188c6beca8c6d86a5f0'),
 'root_d66_audit':('replay_audit.json','719316f60577048f7720d3c550bc26ac999dfcb7901faab2133bcf888fa7d12f'),
 'root_e124_audit':('replay_audit.json','d4155a8bd2b60f42a9d981dfc1204ac308288f4ba65e9321644e9b90743f4ba1')}
for folder,(name,h) in audits.items():
    p=R/folder/name;assert sha(p)==h and read(p)['status']=='PASS'
for name,h in [
 ('tor_replay_audit.json','9b6aab15b385a99e5b78454e5f7ccd0d05ae1b385969ee84d85ddf4df09df7da'),
 ('theta_distribution_replay_audit.json','cbdfcb84723983b16b952b353b6753dfeeb59ab14c87c086eea1ffa591ecdc65'),
 ('log_torsor_replay_audit.json','35ff6ffe6d4d9ed4b5f3b09407513fd985998115ffc32bb3c27f1fff31d4624f'),
 ('principal_cubic_replay_audit.json','b358c84aab0b2b54cd47ae4cff0d6fbf5605b760cde491afbc306f1a745a6c00')]:
    p=R/'root_e120_audit'/name;assert sha(p)==h and read(p)['status']=='PASS'
assert read(R/'root_archive_format/binary_roundtrip229.json')['status']=='PASS'
assert read(R/'root_archive_format/compression229_benchmark.json')['status']=='PASS'
assert read(R/'.lm7_archive226_readback.json')['status']=='PASS'
assert read(R/'root_output_bindings229.json')['status']=='PASS'

for name in ['assemble.py','assemble.out','build_pdf.py','build_pdf.out','latex_pass1.out',
             'latex_pass2.out','latex_pass3.out','bibtex.out','build_certificate.json',
             'pdf_qa.out','package.py','package.out','ARCHIVE_README.md','README.md',
             'materialize_archive_images.py','materialize_archive_images.out','materialize_archive_images.err']:
    p=B/'code'/name
    if p.exists():cp(p,Path('code/checkpoint226_before229')/name)
for name in ['LM7_FERMAT_TOWER_paper.tex','LM7_FERMAT_TOWER_manifest.json']:
    cp(B/name,Path('code/checkpoint226_before229')/(name+'.md' if name.endswith('.tex') else name))
for p in sorted((B/'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_','detail226_','visual226_')) or p.name in ['pdf_qa.json','visual_review.md']):
        cp(p,Path('qa/history/checkpoint226_before229')/p.name)

excluded={'sources','source_images','primary_sources','vendor','__pycache__',
          'fresh224_images','fresh229_binary','negative229_binary'}
allowed={'.py','.gp','.cpp','.json','.csv','.out','.err','.md','.npz','.npy','.bin',
         '.tex','.bib','.jpg','.png','.pdf','.aux','.log','.txt','.patch','.diff'}
def native_or_document(p,out):
    if p.suffix in {'.tex','.bib','.patch','.diff'}:out=out.with_name(out.name+'.md')
    if p.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():
        out=out.with_name(out.name+'.md')
    return out
def owned_path(p,folder,tag):
    rel=p.relative_to(folder)
    if any(x in excluded for x in rel.parts) or p.suffix not in allowed:return None
    if rel.parts[0]=='sections' and len(rel.parts)==2:return rel
    if rel.parts[0]=='ledger':
        if p.name.endswith('_coverage.json') and isinstance(read(p),dict):return Path('ledger')/(tag+'_staging')/p.name
        return rel
    out=(Path('qa')/(tag+'_author')/Path(*rel.parts[1:]) if rel.parts[0]=='qa'
         else Path('code')/(tag+'_bundle')/rel)
    return native_or_document(p,out)
for tag,folder_name,*_ in spec:
    folder=R/folder_name
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            out=owned_path(p,folder,tag)
            if out is not None:cp(p,out)
    for row in declared(manifests[tag])+manifests[tag].get('immutable_inputs',[]):
        p=folder/row['path'] if 'path' in row else R/row['copied']
        out=owned_path(p,folder,tag)
        assert out is not None and digest(get(out))==row['sha256'],row
    for p in (folder/'ledger').glob('*'):
        if p.is_file() and p.name.endswith(('_results.json','_report.md')):
            cp(p,Path('code')/(tag+'_bundle/author_freeze/ledger')/p.name)

# Only declared frozen E120 results, inputs and their declared history are
# copied from the still-active author directory.
efiles=set()
for name,m in em.items():
    efiles.add(R/'research_e120/ledger'/name)
    for x in declared(m)+m['immutable_inputs']:efiles.add(R/'research_e120'/x['path'])
    patterns=m.get('history',[])
    if isinstance(patterns,str):patterns=[patterns]
    for pattern in patterns:efiles.update((R/'research_e120').glob(pattern))
for p in sorted(efiles):
    assert p.is_file() and p.suffix in allowed
    rel=p.relative_to(R/'research_e120');out=Path('code/e120_frozen229')/rel
    # The two imported helpers retain their native executable filenames.
    if p.name not in {'a_e120_exact.py','a_local_smith.py'}:out=native_or_document(p,out)
    cp(p,out)
bindings=read(R/'root_output_bindings229.json')
for row in bindings['actual_helper_executions'][:2]:
    p=Path(row['source']);out=Path('code/e120_frozen229/code')/p.name
    assert digest(get(out))==row['source_sha256']
    cp(R/row['stdout'],out.with_suffix('.out'));cp(R/row['stderr'],out.with_suffix('.err'))
    status={'status':'silent module executed successfully' if not row['arguments'] else 'help entry point executed; arithmetic exercised by importing certificate',
            'exit_code':row['exit_code'],'source_sha256':row['source_sha256'],
            'reason':'Actual standalone helper execution retained. Its exact operations are exercised by the complete copied-source elliptic comparison replay.',
            'importing_certificate':'a_elliptic_tor_symbol.py' if not row['arguments'] else 'a_theta_principal_distribution.py',
            'execution':row}
    put(out.with_name(out.stem+'_status.json'),enc(status),'Record actual helper invocation and successful mathematical consumer.')

for folder_name in list(audits)+['root_e120_audit','root_archive_format','root_output_records229']:
    folder=R/folder_name
    for p in sorted(folder.rglob('*')):
        rel=p.relative_to(folder)
        if not p.is_file() or any(x in excluded for x in rel.parts) or p.suffix not in allowed:continue
        cp(p,native_or_document(p,Path('code')/folder_name/rel))
    if folder_name in audits:
        fn=audits[folder_name][0];cp(folder/fn,Path('ledger')/(folder_name+'_'+fn))
for name in ['root_archive226_readback.py','root_archive226_readback.out','root_archive226_readback.err',
             'root_prepare229_records.py','root_prepare229_records.out','root_prepare229_records.err','root_output_bindings229.json']:
    cp(R/name,Path('code/checkpoint229_integration')/name)
cp(R/'.lm7_archive226_readback.json',Path('ledger/archive226_readback.json'))
cp(R/'root_source_routes227.md',Path('ledger/root229_source_routes.md'))
cp(R/'root_source_refs229.bib',Path('ledger/root229_refs.bib'))

details={
 'E.123':'E.123 evaluates the entire L_d positional53 three-primary S-class tower: actual norms from level2 are isomorphisms on C9^2, with extension3 times the specified inverse and complete horizontal maps. The full coherent divisor image is the kernel of a surjective restricted-support map to C9^2. Literal primes31 and103 give its coordinates and inverse, and compact fibres give coherent lifts. The whole factor is its coherent unit kernel times that divisor module, with the literal total norm and an embedded family of actual H-section classes. Other positional factors and intrinsic section lifts remain active.',
 'E.124':'E.124 gives complete ordinary class groups D2=C9^2+C3 and D3=C27+C9+C3, including actual norm, extension, prime and S-class quotient maps. A literal rank9 residue matrix proves the full completed L2 ordinary-unit basis. Every later norm is onto with kernel in the fixed three-prime subgroup, and both trace compositions equal3. The exact Kato restriction proves a finite h>=2, with coherent three-valuation image3^h Z3 and explicit product coordinates/inverse for the full positional factor. The numerical value of h, a minimal valuation generator, other factors and intrinsic lifts remain active.',
 'D.66':'D.66 fills the complete fourth compact comparison block by actual quadratic source automorphisms. The integral projective cover, full quadratic source square and literal small conjugators realize both remaining compact directions. The ordered correction preserves the preceding three blocks, both D57 branches and all W_h maps. The total retained compact quotient has dimension9600 and28 coinvariants; J66 is the specified remaining kernel of dimension274560. Its cusp-radical correction and full profinite realization remain active.'}
reviews={
 'E.123':'Root read the complete640-line proof and all eight final mathematical sources plus their replay driver. All eight stages were replayed from the exact frozen sources and inputs; all text and both JSON outputs agree byte for byte, both whole decoded GEN objects agree, and the standalone nf-only verifier checks all nine ideal identities in certified maximal orders. All304 owned files and8 inputs were hashed before and after. No fields were excluded and no author source was changed. No separate final third-agent audit is claimed.',
 'E.124':'Root read the complete final proof, all nine mathematical sources and their replay driver, and rechecked the actual class-field, ambiguity and Kato reductions. All nine stages were replayed: all whole text, five JSON outputs and generated inputs agree exactly, as do both complete decoded GEN objects with7 and8 components. The residue rank9,729 upper classes,243 lower classes and all729 actual lifts were checked. All153 owned files and8 inputs remained unchanged. No field was excluded and no upper BNF was used. No separate final third-agent audit is claimed.',
 'D.66':'Root read the complete final proof and all nine sources, with the actual D58 source intersections, D60 odd transfer and unordered stabilizer, D64 joint surjectivity and D65 ordered repair. All nine programs were independently replayed from ten exact inputs. Entire JSON and stdout agree under the declared elapsed-time-only projection; every mathematical field and input hash remains checked. All144 owned files and10 inputs were hashed before and after, with all fresh raw outputs preserved. No separate final third-agent audit is claimed.'}
elliptic=('Four frozen E120 comparison subresults now have complete root proof/source review and copied-source replay: the integral Tor symbol and torsion class, the theta distribution and integral cokernel of order27, the logarithm torsor with its full basis/tangent transport and actual local class of order27, and the framed principal cubic cover. The latter has the literal norm-seven isogeny lift and full Schreier source map; its next augmentation extension detects both residual intrinsic directions by a determinant-one minor. Their arithmetic coefficients remain unassigned. The root Tor and theta checks additionally reconstruct the asserted finite maps independently. All notes, exact dependencies, failed attempts and actual outputs are retained.')
for tag,folder,name,h,section,ident,stem in spec:
    rel=Path('ledger')/(stem+'_results.json');before=get(rel);rows=json.loads(before)
    assert len(rows)==1 and rows[0]['id']==ident
    if isinstance(rows[0]['notes'],dict):rows[0]['notes']=json.dumps(rows[0]['notes'],ensure_ascii=False,sort_keys=True)
    if isinstance(rows[0]['notes'],list):rows[0]['notes']=' '.join(rows[0]['notes'])
    rows[0]['notes']+=' '+details[ident]+' '+reviews[ident]
    rows[0]['where_proved']=rows[0]['where_proved'].replace('code/',f'code/{tag}_bundle/code/')
    if isinstance(rows[0]['manuscript_passages'],list):rows[0]['manuscript_passages']='; '.join(rows[0]['manuscript_passages'])
    after=enc(rows);put(rel,after,'Append completed root review and exact remaining original-task scope.')
    amendments.append({'file':str(rel),'before_sha256':digest(before),'after_sha256':digest(after.encode()),
                       'author_freeze':str(Path('code')/(tag+'_bundle/author_freeze/ledger')/rel.name)})
    rel=Path('ledger')/(stem+'_report.md');before=get(rel)
    after=before.decode()+'\n\n## Completed root review\n\n'+reviews[ident]+'\n\n## Original-task scope\n\n'+details[ident]+'\n'
    put(rel,after,'Append completed review while retaining the exact original author report.')
    amendments.append({'file':str(rel),'before_sha256':digest(before),'after_sha256':digest(after.encode()),
                       'author_freeze':str(Path('code')/(tag+'_bundle/author_freeze/ledger')/rel.name)})

rel=Path('LM7_FERMAT_TOWER_paper.tex');t=get(rel).decode()
for old,news in [
 (r'\input{sections/D_divided_compact_source.tex}',[r'\input{sections/D_quadratic_compact_source.tex}']),
 (r'\input{sections/E_fiftythree_higher_action.tex}',[r'\input{sections/E_fiftythree_positional_stable.tex}',r'\input{sections/E_fiftythree_ordinary_valuation.tex}'])]:
    assert t.count(old)==1 and all(n not in t for n in news);t=t.replace(old,old+'\n'+'\n'.join(news))
put(rel,t,'Register all three completely reviewed and replayed proofs.')
rel=Path('sections/E.tex');t=get(rel).decode();a=t.index(r'\begin{statement}{E.23}');z=t.index(r'\end{statement}',a)
new=r'''
E.123 evaluates the separate $L_d$ positional-$53$ S-class tower:
all actual norms from level two identify the class groups with
$C_9\oplus C_9$, with complete horizontal maps. The entire coherent
divisor image is the kernel of its explicit restricted-support class
map, with prime basis $31,103$, coordinates and inverse. Compact fibres
give coherent lifts and a product decomposition with the coherent
unit kernel, retaining the total norm and an actual H-section family.
E.124 evaluates the ordinary groups
$D_2=C_9^2\oplus C_3$ and $D_3=C_{27}\oplus C_9\oplus C_3$,
including the norm, extension and S-class quotient maps. The actual
Kato restriction proves a finite $h\geq2$ and coherent three-valuation
image $3^h\mathbb Z_3$, with literal product coordinates and inverse.
Its numerical value and a minimal coherent generator remain under
calculation. Four frozen elliptic comparison notes additionally give
the integral Tor class, theta distribution, logarithm torsor and
framed principal cubic cover. The last has an actual based Schreier
map whose next augmentation extension detects both residual handle
directions with a determinant-one minor. Their arithmetic coefficients,
the intrinsic higher section lifts and the other positional factors
remain on the active list.
'''
put(rel,t[:z]+new+t[z:],'Record the evaluated full positional factor and actual remaining coefficient maps.')
rel=Path('sections/D.tex');t=get(rel).decode()
new=r'''
D.66 fills the complete fourth compact comparison block by actual
quadratic source automorphisms. Its integral projective cover and full
quadratic source square realize both remaining compact directions,
retaining the literal small conjugators, both D.57 branches, all
$\mathcal W_h$ maps and the preceding three compact blocks. The total
retained compact quotient has dimension $9600$ and $28$ coinvariants.
The specified remaining source kernel is $J_{66}$, of dimension
$274\,560$. Its cusp-radical correction and the full profinite
realization continue to require their actual source maps.
'''
for ident in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+ident+'}');z=t.index(r'\end{statement}',a);t=t[:z]+new+t[z:]
put(rel,t,'Record the complete compact correction and specified remaining source kernel.')
for name in ['d_results.json','d_coverage.json']:
    rel=Path('ledger')/name;rows=json.loads(get(rel))
    for row in rows:
        if name=='d_results.json' and row['id'] in ['D.13','D.19']:
            assert 'D.66' not in row['depends_on'];row['depends_on'].append('D.66');row['notes']+=' '+details['D.66']
        if name=='d_coverage.json' and row['task'] in ['D.e','D.afterLM2.1']:
            row['statement_ids'].append('D.66');row['outcome']+=' '+details['D.66']
            row['remaining_step']='Evaluate the actual cusp-radical boundary in the specified J66 of dimension274560, preserving the completed compact source maps, and then the full profinite realization.'
    put(rel,enc(rows),'Synchronize original D statement and task rows.')
rel=Path('code/assemble.py');t=get(rel).decode();needle='\ne_rows = []\n';assert t.count(needle)==1
t=t.replace(needle,"\ne_deps['E.23'].extend(['E.123','E.124'])\ne_notes['E.23'] += "+repr(' '+details['E.123']+' '+details['E.124']+' '+elliptic)+'\n'+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
       "        row['statement_ids'].extend(x for x in ('E.123','E.124') if x not in row['statement_ids'])\n"
       "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += "+repr('; '+details['E.123']+' '+details['E.124']+' '+elliptic)+'\n'
       "        row['remaining_step'] = "+repr('Evaluate the two residual intrinsic arithmetic handle coefficients through the actual cubic-cover augmentation comparison, then intrinsic class-three and later section maps, further quartic quotients and coefficient primes. Evaluate numerical h and its minimal coherent unit generator, and the other positional factors. The full positional53 L_d divisor factor, both stable S-class towers and all finite one-step unit defects are proved through their actual maps.')+'\n')
t=t.replace(needle,block+needle);put(rel,t,'Synchronize generated E23 and all33 original-task rows.')

put(Path('code/package.py'),(R/'root_archive_format/package229.py').read_bytes(),'Use verified lossless binary/image aliases, codec cache and exact historical execution guards.')
for source,target in [
 ('materialize_archive_images229.py','materialize_archive_images.py'),
 ('materialize_archive_images229.out','materialize_archive_images.out'),
 ('materialize_archive_images229.err','materialize_archive_images.err'),
 ('materialize_archive_files.py','materialize_archive_files.py'),
 ('materialize_archive_files.out','materialize_archive_files.out'),
 ('materialize_archive_files.err','materialize_archive_files.err')]:
    put(Path('code')/target,(R/'root_archive_format'/source).read_bytes(),'Exact reviewed materializer and actual execution output.')
put(Path('code/ARCHIVE_README.md'),(R/'root_archive_format/ARCHIVE_README229.md').read_bytes(),'Document exact extraction and all original binary/image paths.')
rel=Path('code/README.md')
put(rel,get(rel).decode()+'\n\n## E123, D66 and E124\n\n'+'\n\n'.join(reviews[x]+'\n\n'+details[x] for x in ['E.123','D.66','E.124'])+'\n\n## Four frozen elliptic comparisons\n\n'+elliptic+'''

The three exact author ledgers are retained in their author_freeze/ledger
directories; active editorial amendments have an explicit separate ledger.
The E120 author tree remains active: code/e120_frozen229 contains only the
four declared frozen notes, programs, exact dependencies and declared history.
Imported helpers retain their native names and actual execution records.

## Current lossless archive layout

The current extraction instructions are in ARCHIVE_README.md. Complete
byte-identical binary data and historical QA images have explicit logical
path aliases. Every original path and byte string is retained, with the
whole-byte materializer and independently executed restoration checks.
Source programs, text transcripts, JSON records and current main-PDF page
images are ordinary members. Different binary serializations retain their
different complete bytes. Earlier image-only layout descriptions above
record the preceding versions; the current binary alias policy is the one
specified here and in the two current alias manifests.
''','Document exact review scope and complete lossless archive representation.')

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
put(Path('ledger/checkpoint229_amendments.json'),enc({'status':'PASS','amendments':amendments}),'Record exact editorial amendments and unchanged originals.')
for tag,folder,name,h,*_ in spec:verify(R/folder,name,h)
for name,h in espec:verify(R/'research_e120',name,h)
changes=[]
for p,data in pending.items():
    old=sha(p) if p.exists() else None
    if p.exists() and p.read_bytes()!=data:
        if p.parent==B/'sections':h=B/'sections/history/checkpoint226_before229'/p.name
        elif p.parent==B/'ledger':h=B/'code/checkpoint226_before229/ledger'/p.name
        else:h=None
        if h is not None:
            h.parent.mkdir(parents=True,exist_ok=True);assert not h.exists();shutil.copy2(p,h)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    changes.append({'path':str(p.relative_to(B)),'before_sha256':old,'after_sha256':sha(p),'reason':reasons[p]})
record={'status':'PASS','added_statements':['E.123','D.66','E.124'],'expected_statement_count':229,'original_task_rows':33,
        'original_open_statements':['D.13','D.19','E.23'],'frozen_elliptic_subresults':list(em),
        'frozen_to_archive_mapping':mapping,'changes':changes,'active_ledger_amendments':amendments,
        'build_status':'Assembly, LuaLaTeX build, integrated visual review and physical/logical archive verification follow.'}
(B/'ledger/checkpoint229_integration.json').write_text(enc(record))
print(enc({'status':'PASS','expected_statement_count':229,'mapped_frozen_files':len(mapping),
           'written_files':len(changes),'original_task_rows':33,'all_frozen_mappings_match_actual_archive_bytes':True}),end='')
