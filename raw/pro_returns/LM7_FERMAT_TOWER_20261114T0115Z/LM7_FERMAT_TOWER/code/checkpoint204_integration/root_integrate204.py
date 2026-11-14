"""Integrate the fully audited E105, E107 and D57 frozen packets."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};reasons={};mapping=[]

def prep(relative,data,reason):
    target=BASE/relative
    value=data.encode() if isinstance(data,str) else data
    if target in pending:assert pending[target]==value,relative
    pending[target]=value;reasons[target]=reason

def copy(source,relative,reason='Preserved exact owned source, actual output or audit metadata.'):
    target=BASE/relative
    if target.exists():
        assert target.read_bytes()==source.read_bytes(),relative
    else:prep(relative,source.read_bytes(),reason)
    mapping.append({'source':str(source.relative_to(ROOT)),'archive':str(relative),'sha256':sha(source)})

def verify_manifest(folder,name,digest):
    path=folder/name
    assert sha(path)==digest
    m=read(path);files=m['files']
    rows=([dict(path=k,**v) for k,v in files.items()] if isinstance(files,dict) else files)
    rows+=m.get('immutable_inputs',[])
    for row in rows:assert sha(folder/row['path'])==row['sha256'],row['path']
    return m

assert not (BASE/'ledger/checkpoint204_integration.json').exists()
E105=ROOT/'research_e105';E107=ROOT/'research_e107';D57=ROOT/'D57_EXPERIMENTS'
verify_manifest(E105,Path('ledger/e_quartic_class2_manifest.json'),'662e1c77f11110d9280d1bca4a733a0165cf32adf3ee8f3c3ab8296117710608')
verify_manifest(E107,Path('ledger/e_stable_ordinary_manifest.json'),'c0591a02aa9f6e17086c31586cb18e7d156e2859457244bdda06b567856a5c8e')
md=verify_manifest(D57,Path('ledger/d_arithmetic_class2_repair_manifest.json'),'f213a0d93c952965e97a6064a04e4960ce669368e01a24e596f5138ebf093aff')
for directory,identifier in [('root_e105_audit','E.105'),('root_e107_audit','E.107'),('root_d57_audit','D.57')]:
    a=read(ROOT/directory/'audit.json');assert a['status']=='PASS' and a['statement']==identifier
assert read(ROOT/'bc_e105_audit/audit.json')['audit_status']=='PASS'
assert read(ROOT/'a_e107_audit/audit.json')['status']=='PASS'

# E105 has no external mathematical inputs. Its independent author replay and
# standalone layout images are preserved with their own provenance.
for p in sorted(E105.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(E105)
    if rel.parts[0]=='qa':
        if p.suffix=='.jpg':copy(p,Path('qa/e105_author')/p.name)
        elif p.name.startswith('pass_') and p.suffix=='.out':copy(p,Path('code/e105_author_layout')/p.name)
        elif p.suffix=='.tex':copy(p,Path('code/e105_author_layout')/(p.name+'.md'))
        continue
    if rel.parts[0]=='author_rebuild':rel=Path('code/e105_author_rebuild')/Path(*rel.parts[1:])
    copy(p,rel)

# E107 hashes every sibling input. It is therefore an isolated, portable
# bundle: adding these inputs to E106's directory would change both outputs.
for p in sorted(E107.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(E107)
    if rel.parts[0] in ('code','inputs'):rel=Path('code/e107_bundle')/rel
    elif rel==Path('ledger/e_stable_ordinary_coverage.json'):rel=Path('ledger/e107_staging')/p.name
    elif rel.parts[:2]==('ledger','e107_original_author_freeze'):rel=Path('code/e107_original_author_freeze')/p.name
    copy(p,rel)

# D57's frozen manifest deliberately excludes unused source copies. Its
# complete fresh author replay is included separately because it did run.
dpaths={row['path'] for row in md['files']+md['immutable_inputs']}
dpaths.add('ledger/d_arithmetic_class2_repair_manifest.json')
for reltext in sorted(dpaths):
    p=D57/reltext;rel=Path(reltext)
    if rel.parts[0]=='audit':
        if p.suffix=='.tex':rel=Path('sections/history/d57_pre_rref_exhaustion')/p.name
        else:rel=Path('code')/Path(*rel.parts[1:])
    if p.name=='verify.source.txt':rel=rel.with_name('verify.py')
    elif p.name=='d_arithmetic_local_transgression.source.txt':rel=rel.with_name('d_arithmetic_local_transgression.py')
    elif p.name=='nested_helper_actual_stdout.txt':rel=rel.with_name('d_arithmetic_local_transgression.out')
    elif p.suffix=='.patch':rel=rel.with_name(p.name+'.md')
    copy(p,rel)
for p in sorted((D57/'author_fresh_rebuild').rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        copy(p,Path('code/d57_author_fresh_rebuild')/p.relative_to(D57/'author_fresh_rebuild'))

# Audit drivers preserve their historical staging paths. Copied proof/source
# snapshots without their own execution are explicitly archived as text.
audit_dirs=[('root_e105_audit','e105_root_rebuild'),('bc_e105_audit','e105_peer_rebuild'),
            ('root_e107_audit','e107_root_rebuild'),('a_e107_audit','e107_peer_audit'),
            ('root_d57_audit','d57_root_rebuild')]
for source_dir,target_dir in audit_dirs:
    directory=ROOT/source_dir
    for p in sorted(directory.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts:continue
        rel=Path('code')/target_dir/p.relative_to(directory)
        if p.suffix=='.tex' or (p.suffix=='.py' and not p.with_suffix('.out').exists()):
            rel=rel.with_name(p.name+'.md')
        copy(p,rel)
    for name in ('audit.json','README.md','audit.md'):
        p=directory/name
        if p.exists():copy(p,Path('ledger')/(source_dir+('.json' if p.suffix=='.json' else '.md')))

# Preserve the exact frozen proof, and make the sole received citation fix.
p=BASE/'sections/E_stable_ordinary_phase.tex'
frozen=pending[p].decode();needle='in E101.20--24, and include it in'
assert frozen.count(needle)==1
copy(E107/'sections/E_stable_ordinary_phase.tex',Path('sections/history/E107_frozen_before_citation.tex'))
amended=frozen.replace(needle,'in E101.19 and its following residue paragraph, and include it in')
pending[p]=amended.encode();reasons[p]='Citation-only correction requested by the independent E107 proof auditor; frozen text preserved.'
prep(Path('ledger/e107_citation_amendment.json'),enc({'status':'PASS','kind':'citation only',
     'old':'E101.20--24','new':'E101.19 and its following residue paragraph',
     'frozen_sha256':hashlib.sha256(frozen.encode()).hexdigest(),
     'amended_sha256':hashlib.sha256(amended.encode()).hexdigest(),
     'requested_by':'a_structure independent full proof audit; accepted by author and root',
     'mathematical_text_changed':False}), 'Exact citation amendment and both hashes.')

detail_e105=('E.105 lifts the actual E103 four-coset abelian origin to every odd integral and every rational quartic class-two target. '
 'It evaluates the full two-coordinate toric image by the continuous restricted-correction criterion, retaining all framed cusp signs, '
 'the exact cup primitive and phantom classes. Every fibre over a fixed liftable abelian class is the actual central H1; '
 'the compact-handle action and the remaining general abelian inputs stay active.')
detail_e107=('E.107 proves all later ordinary class norm maps are isomorphisms in the actual named-prime bases: '
 'Cl(B_d){3}=C9^2+C3 for d>=3 and Cl(L_d){3}=C9+C3 for d>=2. '
 'The fifth ordinary-unit character and actual cyclic-nine norm square give rank5 at every later B step. '
 'The coherent three-unit exponent is h=1. The complete complex divisor phase has an explicit linear normalization, '
 'and every scaled toric fibre for pure positional component1 is the evaluated coherent kernel. '
 'The separate pure-field factor and the remaining intrinsic and mixed-source classifications remain active.')
detail_d57=('D.57 evaluates the actual order3888 arithmetic boundary for both possible integral rank9 branches. '
 'Every one of the sixteen framing cases has a literal zero of the complete ten-coordinate polynomial. '
 'Its exact genus3-to-E3 map, exhaustive integral conjugator search, rank64 local image in74 coinvariants, '
 'separate plus-central alignment and augmentation correction give an actual automorphism of '
 'Bhat/(R_h intersect M_* intersect L_{*,2}), retaining the full D49 W_h action and prescribed parameter. '
 'The full G3 invariant equation and the full profinite source still require lifting across the explicit kernels.')

for stem,identifier,detail,audit_dirs_for_row in [
 ('e_quartic_class2','E.105',detail_e105,['root_e105_audit','bc_e105_audit']),
 ('e_stable_ordinary','E.107',detail_e107,['root_e107_audit','a_e107_audit']),
 ('d_arithmetic_class2_repair','D.57',detail_d57,['root_d57_audit'])]:
    p=BASE/'ledger'/f'{stem}_results.json';rows=json.loads(pending[p]);assert len(rows)==1 and rows[0]['id']==identifier
    rows[0]['where_proved']+='; '+', '.join('ledger/'+x+'.json' for x in audit_dirs_for_row)
    rows[0]['notes']=rows[0]['notes'].replace('Root and peer audits pending.','Root full proof/source audit and fresh six-stage replay PASS; no independent peer audit is claimed for D57.')
    rows[0]['notes']+=' '+detail+' Completed audit scope is recorded in the attached root and received peer reports.'
    if identifier=='E.107':rows[0]['where_proved']=rows[0]['where_proved'].replace('code/e_stable_ordinary_phase','code/e107_bundle/code/e_stable_ordinary_phase')
    pending[p]=enc(rows).encode()
    p=BASE/'ledger'/f'{stem}_report.md'
    pending[p]+=('\n## Completed integration audit\n\n'+detail+'\n\n'+
                 'The full root proof/source audit and fresh execution have passed. '+
                 ('The independent full peer proof audit has also passed. ' if identifier!='D.57' else '')+
                 'All exact outputs and source amendments are preserved; whole-paper rendering is a separate checkpoint.\n').encode()

p=BASE/'LM7_FERMAT_TOWER_paper.tex';t=p.read_text()
for marker,new in [(r'\input{sections/E_two_prime_full_family.tex}',r'\input{sections/E_quartic_class_two.tex}'),
                   (r'\input{sections/E_next_ordinary_classes.tex}',r'\input{sections/E_stable_ordinary_phase.tex}'),
                   (r'\input{sections/D_arithmetic_detecting_quotient.tex}',r'\input{sections/D_arithmetic_class2_repair.tex}')]:
    assert t.count(marker)==1 and new not in t;t=t.replace(marker,marker+'\n'+new)
prep(p.relative_to(BASE),t,'Register the three fully audited sections.')

p=BASE/'sections/E.tex';t=p.read_text();a=t.index(r'\begin{statement}{E.23}');b=t.index(r'\end{statement}',a)
addition=r'''

E.105 lifts the actual quartic four-coset origin through class two
for every odd integral and every rational coefficient ring.
The entire two-coordinate toric image is evaluated by the exact
continuous correction criterion, including its nonclosed denominator.
The compact-handle arithmetic action and general abelian inputs
continue in the subsequent calculation.

E.107 now determines the previously retained all-level ordinary
class maps and coherent exponent: $h=1$.
The actual cyclic-nine Artin square preserves the fifth ordinary-unit
character, and the named-prime class norm maps stabilize as
isomorphisms. The full complex divisor phase and every scaled toric
fibre with pure positional component one are evaluated explicitly.
These conclusions supersede the later-layer and phase questions
recorded in the earlier milestones. The separate pure-field norm
factor, general coupled arithmetic sources and higher intrinsic
lifting questions remain active.
'''
prep(p.relative_to(BASE),t[:b]+addition+t[b:],'Update the completed cases and exact remaining scope at E23.')

p=BASE/'sections/D.tex';t=p.read_text()
addition=r'''

D.57 now solves the complete ten-coordinate boundary equation
on the actual order-$3888$ arithmetic quotient, for both integral
rank-nine branches and all sixteen framed cases. The literal
genus-three cover and degree-eight elliptic map, exhaustive integral
conjugator search, separate plus-central alignment and augmentation
correction give the asserted automorphism of
$\widehat B/(R_h\cap M_*\cap L_{*,2})$.
Its entire $W_h$ action and prescribed normalized parameter are
retained. The exact remaining quotient kernels carry the full
$G_3$ invariant and full profinite realization questions onward.
'''
for identifier in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+identifier+'}');b=t.index(r'\end{statement}',a)
    t=t[:b]+addition+t[b:]
prep(p.relative_to(BASE),t,'Update both original unresolved source questions with the actual D57 lift.')

p=BASE/'ledger/d_results.json';rows=read(p)
for row in rows:
    if row['id'] in ('D.13','D.19'):
        row['depends_on'].append('D.57');row['notes']+=' '+detail_d57
prep(p.relative_to(BASE),enc(rows),'Keep the original D result rows synchronized.')
p=BASE/'ledger/d_coverage.json';rows=read(p)
for row in rows:
    if row['task'] in ('D.e','D.afterLM2.1'):
        row['statement_ids'].append('D.57');row['outcome']+=' '+detail_d57
        row['remaining_step']='Lift the solved arithmetic class-two action through the full G3 invariant kernel and the remaining full profinite source; decide the original GT0 and all-loop image comparison.'
prep(p.relative_to(BASE),enc(rows),'Update the relevant original D task coverage.')

p=BASE/'code/assemble.py';t=p.read_text();needle='\ne_rows = []\n';assert t.count(needle)==1
block="\ne_deps['E.23'].extend(['E.105','E.107'])\ne_notes['E.23'] += "+repr(' '+detail_e105+' '+detail_e107)+'\n'
t=t.replace(needle,block+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n"
       "    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
       "        row['statement_ids'].extend(x for x in ('E.105','E.107') if x not in row['statement_ids'])\n"
       "    if row['task'] in ('E.d','E.follow-up-4'):\n"
       "        row['outcome'] += "+repr('; '+detail_e105+' '+detail_e107)+"\n"
       "        row['remaining_step'] = "+repr('evaluate unrestricted coupled global ramification and joint origins outside the completed two-prime families; evaluate the separate pure-field norm factor and combine it with the completed complex factor; continue higher wild cubic stages and general quartic compact-handle/mixed odd-primary and rational nonabelian inputs; evaluate other-primary and mixed sources')+'\n')
t=t.replace(needle,block+needle)
prep(p.relative_to(BASE),t,'Synchronize the generated E result and coverage rows; mark h and phase settled.')

# Exact original-source retrieval outcomes, without promoting metadata to a
# proof reading. Downloaded PDFs and raw provider responses stay outside.
for stem in ['root_public_source_routes','root_ceresa_sources','root_bloch_reading']:
    for suffix in ['.py','.out','.json']:
        p=ROOT/(stem+suffix)
        if p.exists():copy(p,Path('code/source_routes204')/p.name)
p=BASE/'ledger/d_original_source_recheck.md';t=p.read_text()
t+='\nThe subsequent owned HTTP metadata retrieval in code/source_routes204/root_public_source_routes.py returned HTTP200 for both exact OpenAlex records and both Crossref records. Ihara1986 had no public PDF location in that response. Coleman1989 supplied the exact Project Euclid chapter PDF URL; the web reader reached an access-challenge page (turn889view0), and no PDF proof was read. The successful metadata retrieval updates the earlier reader-API failure record, without changing any original-proof verification status. The same route obtained GDZ metadata for Bloch1984 and then the public original PDF used for a separate compact-handle calculation; that does not verify an Ihara or Coleman original.\n'
prep(p.relative_to(BASE),t,'Record actual subsequent public-source access outcomes precisely.')

p=BASE/'code/README.md';t=p.read_text()
t+='''

## E105, E107 and D57 completed calculations

E105: run `python code/a_quartic_frames_explore.py`, `python code/a_quartic_class2.py` and `python code/a_quartic_toric_cups.py`. The exact author and two independent copied executions are retained. Python3 and SymPy are required.

E107: run `python code/e107_bundle/code/e_stable_ordinary_phase.py`. Its three immutable inputs are in the sibling `inputs` directory within that bundle. This isolation preserves the exact input-hash metadata of both E106 and E107. The independent peer verifier is `code/e107_peer_audit/a_e107_rank_phase.py`. The raw/scaled-exponent test amendment and the citation-only proof amendment have separate records.

D57: run the six `code/d_arithmetic_*.py` programs in the order given by `ledger/d_arithmetic_class2_repair_manifest.json`: rank9 seed, geometry, conjugators, invariant module, local transgression, affine boundary. Python3, NumPy and SymPy are required. Both D56 JSON inputs are included. Complete final author and root copied replays are preserved, with comparisons excluding only elapsed_seconds. Every historical attempted program retains its actual output; nested local helpers retain their actual captured stdout. Files ending `.py.md` are source snapshots without a separate claimed execution; files ending `.patch.md` preserve exact patch bytes.

Archived audit and integration drivers retain their original staging paths and record the historical execution. The final mathematical programs above are the portable rerun entry points. Source-retrieval programs record access outcomes; raw third-party documents are excluded from the archive.
'''
prep(p.relative_to(BASE),t,'Document exact portable entry points and historical audit provenance.')

existing_allowed={BASE/x for x in ['LM7_FERMAT_TOWER_paper.tex','sections/E.tex','sections/D.tex',
 'ledger/d_results.json','ledger/d_coverage.json','code/assemble.py','code/README.md','ledger/d_original_source_recheck.md']}
for p in pending:assert not p.exists() or p in existing_allowed,p
changes=[]
for p,data in pending.items():
    before=sha(p) if p.exists() else None
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    changes.append({'path':str(p.relative_to(BASE)),'before_sha256':before,'after_sha256':sha(p),'reason':reasons[p]})

record={'status':'PASS','added_statements':['E.105','E.107','D.57'],
 'existing_integrated_statement':'E.106','expected_statement_count':204,
 'frozen_to_archive_mapping':mapping,'changes':changes,
 'root_audits':{name:sha(ROOT/name/'audit.json') for name,_ in audit_dirs if name.startswith('root_')},
 'received_peer_audits':{'E.105':sha(ROOT/'bc_e105_audit/audit.json'),'E.107':sha(ROOT/'a_e107_audit/audit.json')},
 'mathematical_proof_amendments':[],
 'citation_only_amendment':'E107 eta anchor changed from E101.20--24 to E101.19 and following residue paragraph; frozen proof preserved.',
 'build_status':'Working manuscript integrated; full build, whole-paper render and archive verification follow.',
 'unresolved_original_statements':['D.13','D.19','E.23']}
(BASE/'ledger/checkpoint204_integration.json').write_text(enc(record))
print(enc({'status':'PASS','added_statements':record['added_statements'],
           'changed_files':len(changes),'preserved_source_mappings':len(mapping),
           'expected_statement_count':204}))
