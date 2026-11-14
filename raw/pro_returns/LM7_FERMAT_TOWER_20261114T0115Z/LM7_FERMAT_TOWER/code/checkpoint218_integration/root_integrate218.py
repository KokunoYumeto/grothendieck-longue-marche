#!/usr/bin/env python3
"""Integrate four completed proofs and their exact reviews, retaining all open tasks."""
from pathlib import Path
import hashlib
import json
import re
import shutil

R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
digest=lambda b:hashlib.sha256(b).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};reasons={};mapping=[];amendments=[]
assert not (B/'ledger/checkpoint218_integration.json').exists()
def put(rel,data,reason):
    p=B/rel;pending[p]=data.encode() if isinstance(data,str) else data;reasons[p]=reason
def get(rel):
    p=B/rel;return pending[p] if p in pending else p.read_bytes()
def cp(src,rel):
    p=B/rel
    if p.exists():assert p.read_bytes()==src.read_bytes(),str(rel)
    else:put(rel,src.read_bytes(),'Exact owned source, actual output or retained review evidence.')
    mapping.append({'source':str(src.relative_to(R)),'archive':str(rel),'sha256':sha(src)})
def verify(folder,name,expected):
    p=folder/'ledger'/name;assert sha(p)==expected,str(p)
    m=read(p);rows=m['files']
    if isinstance(rows,dict):rows=[dict(path=k,**v) for k,v in rows.items()]
    for row in rows+m.get('immutable_inputs',[]):
        q=folder/row.get('path',row.get('file'));assert sha(q)==row['sha256'],str(q)
        if 'bytes' in row:assert q.stat().st_size==row['bytes']
    return m
spec=[
 ('e115','research_e115','e_quartic_mixed_five_manifest.json','bcdacee1fb1b149fe250d98f5fdf472c6e9b4dd5538587cc31d6d493eeb43d44','E_quartic_mixed_five.tex','E.115','e_quartic_mixed_five'),
 ('e116','research_e116','e_inert_lower_manifest.json','f3621089be7dda072f6cfa26198340316544c08fb3e3067e1189a60766e2e53f','E_inert_lower_factors.tex','E.116','e_inert_lower'),
 ('e118','research_e118','e_quartic_five_numerical_manifest.json','a7956913d867120bf456310a9ea3de37d2aeac34ef9b8e96e446d63132ce11e6','E_quartic_five_numerical.tex','E.118','e_quartic_five_numerical'),
 ('d61','D61_EXPERIMENTS','d_remaining_projective_rows_manifest.json','2685a1c4f9ca12f7c285bcee1f5dcfe875e64e26e084faff7532cd35d8677bde','D_remaining_projective_rows.tex','D.61','d_remaining_projective_rows')]
for tag,folder,mname,expected,*rest in spec:verify(R/folder,mname,expected)
audits={
 'root_e115_audit':'0f2f5ccfeeb1fc46ab04442f04f4c1b520174b284a56c7e563cbf3560a71f0b0',
 'bc_e115_audit':'bfff5d21503e15615d2902642fa79bac44cd1eb198b26de11e3ccf5635aec514',
 'root_e116_audit':'0422df698643be4954deaf0af189e9c6034d69367eb41ab9c181b5bc15f0fe21',
 'root_d61_audit':'6b26e4604906d5d06ebe684f4087ae21591e436bbbf4adc2c92b1c76c303d13f',
 'bc_e118_audit':'c5446f85955b5e46e44dec25583aaefd62ff395ed39dddc0013d3ad8f3850a3f'}
for name,expected in audits.items():
    p=R/name/'audit.json';assert sha(p)==expected and read(p)['status']=='PASS',name

# Retain the actual last assembled/build/package inputs and their outputs.
for name in ['assemble.py','assemble.out','build_pdf.py','build_pdf.out','latex_pass1.out','latex_pass2.out','latex_pass3.out','bibtex.out','build_certificate.json','pdf_qa.out','package.py','package.out']:
    p=B/'code'/name
    if p.exists():cp(p,Path('code/checkpoint214_before218')/name)
cp(B/'LM7_FERMAT_TOWER_paper.tex',Path('code/checkpoint214_before218/paper_master.tex.md'))
for p in sorted((B/'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_','detail214_','visual214_')) or p.name in ['pdf_qa.json','visual_review.md']):
        cp(p,Path('qa/history/checkpoint214_before218')/p.name)

excluded={'sources','source_images','primary_sources','vendor','__pycache__'}
allowed={'.py','.gp','.cpp','.json','.csv','.out','.err','.md','.npz','.npy','.bin','.tex','.bib','.jpg','.txt','.patch','.diff'}
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
    if out.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():out=out.with_name(out.name+'.md')
    return out
for tag,folder,*rest in spec:
    folder=R/folder
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            dest=mapped_owned(p,folder,tag)
            if dest is not None:cp(p,dest)
for name in audits:
    folder=R/name
    for p in sorted(folder.rglob('*')):
        if not p.is_file() or any(x in excluded for x in p.relative_to(folder).parts) or p.suffix not in allowed:continue
        rel=Path('code')/name/p.relative_to(folder)
        if p.suffix in {'.tex','.bib','.txt','.patch','.diff'}:rel=rel.with_name(rel.name+'.md')
        if p.suffix in {'.py','.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem+'_gp.out').exists():rel=rel.with_name(rel.name+'.md')
        cp(p,rel)
    for f in ['audit.json','audit.md','verification.json']:
        p=folder/f
        if p.exists():cp(p,Path('ledger')/(name+'_'+f))
for ext in ['.py','.out']:
    cp(R/('root_record_e116_d61_audits'+ext),Path('code/checkpoint218_integration')/('root_record_e116_d61_audits'+ext))

details={
 'E.115':'E.115 completes the actual five-primary and rational-five quartic class-two image and every fibre. The based smooth-source descent has an explicit pullback inverse; every finite-S input lifts, with coordinates Z5^13 x Z5^81. For arbitrary arithmetic inputs the full test consists of all55 peripheral cups and the actual restricted mixed correction. The scalar valuation test retains the exact elliptic Kummer orders and finite-support/decay maps; Chebotarev proves these orders unbounded.',
 'E.116':'E.116 evaluates every global H fibre on nonzero first Kummer lines of inert primes ell congruent2 or5 modulo9, through the actual complete pure norm factors and positional comparison. At53 it evaluates the first pure S-unit norm map and all fibres, ordinary class group C3^2, zero pure S-class group and complex S-class group C3 with exact conjugation action. The higher lower53 positional norm factors and intrinsic preimages remain active.',
 'E.118':'E.118 gives the actual order800 Kummer cocycle and numerical prime3121. The complete integral compact slice over the specified toric class is5Z5^3, of index125, with every E115 central fibre. The exact tensor-extension isomorphism and the separately specified rational correcting cochain give the full Q5^3 slice.',
 'D.61':'D.61 constructs the integral projective homology replacement on the two size-twelve character orbits and retains the complete D57 and W_h projections. Seven old self and twelve new cross blocks have injective norm and compactification, so their actual orientation boundary vanishes. The lift retains22016 additional central coordinates and50 coinvariants; its residual has dimension331776 and562 coinvariants. All four actual involution-cover divided norms leave the stated26 self-wedge classes undetected; their remaining arithmetic boundary and full profinite realization remain active.'}
for tag,folder,mname,expected,section,ident,stem in spec:
    rel=Path('ledger')/(stem+'_results.json');rows=json.loads(get(rel));assert rows[0]['id']==ident
    rows[0]['notes']+=' '+details[ident]
    rows[0]['where_proved']=rows[0]['where_proved'].replace('code/',f'code/{tag}_bundle/code/').replace('audit/d61_author_rebuild/', 'code/d61_bundle/audit/d61_author_rebuild/')
    if ident=='E.115':rows[0]['manuscript_passages']='Section51.16; folios733v--736v; scans172--178; equations371--379; PartE(c),(d), follow-up4'
    if ident=='D.61':rows[0]['notes']=rows[0]['notes'].replace('Root and peer review pending.','Complete root proof/source audit and fresh four-stage replay PASS; no additional independent peer review is claimed.')
    put(rel,enc(rows),'Synchronize proof locations, completed review scope and original-task state.')
    rel=Path('ledger')/(stem+'_report.md')
    put(rel,get(rel).decode()+'\n## Integrated review and original-task scope\n\n'+details[ident]+'\n\nExact complete-proof, fresh-execution and primary-source reading scopes are retained in the attached root and peer audits. These original tasks remain explicit in the opening coverage table.\n','Record completed audit scope and remaining original tasks.')

rel=Path('LM7_FERMAT_TOWER_paper.tex');t=get(rel).decode()
for marker,addition in [
 (r'\input{sections/D_stabilizer_projective_lift.tex}',r'\input{sections/D_remaining_projective_rows.tex}'),
 (r'\input{sections/E_inert_prime_tail.tex}','\n'.join(r'\input{sections/'+x[4]+'}' for x in spec[:3]))]:
    assert t.count(marker)==1 and addition not in t;t=t.replace(marker,marker+'\n'+addition)
put(rel,t,'Register the four completely reviewed statements.')

rel=Path('sections/E.tex');t=get(rel).decode();a=t.index(r'\begin{statement}{E.23}');z=t.index(r'\end{statement}',a)
old='The full mixed obstruction in the remaining rank-127\nmodule, other coefficient primes and the higher targets remain active.'
assert old in t[a:z]
t=t.replace(old,'E.115 below evaluates the full mixed obstruction in that rank-127\nmodule. Other coefficient primes and the higher targets remain active.',1)
z=t.index(r'\end{statement}',a)
new=r'''
E.115 completes the actual five-primary quartic class-two image
and all its fibres, including the literal based descent and
finite-$S$ coordinates $\mathbb Z_5^{13}\times\mathbb Z_5^{81}$.
Its unrestricted image is given by the peripheral tests and the
actual restricted mixed correction, with the exact local Kummer
orders and scalar divisibility/decay inverse.
E.118 supplies an explicit global cocycle of finite image order
$800$, with exact local order five at $3121$; over the specified
toric input its entire compact slice is $5\mathbb Z_5^3$,
of index $125$. The tensor-extension map and the actual rational
cochain inverse are specified separately.
E.116 computes every $H$ fibre on the nonzero first Kummer lines
of inert primes congruent to $2$ or $5$ modulo $9$, and the
complete first pure norm step at $53$. Higher lower-$53$
positional norms, intrinsic metabelian and marked preimages,
the remaining coefficient primes and the higher full-source
sections continue to be the active original targets.
'''
put(rel,t[:z]+new+t[z:],'Update E23 through actual completed maps, retaining its Open status.')
rel=Path('sections/D.tex');t=get(rel).decode()
new=r'''
D.61 makes the exact integral homology replacement on the two
size-twelve character orbits. It retains D.57 and $\mathcal W_h$,
and its injective norm and compactification kill the actual
orientation boundary on seven previous self blocks and twelve
new cross blocks. The resulting lift retains $22\,016$ further
central coordinates and fifty coinvariants. Its specified
remaining module has dimension $331\,776$ and $562$ coinvariants.
The four actual involution-cover divided norms still leave
twenty-six named self-wedge classes; their arithmetic boundary
and the full profinite source realization remain active.
'''
for ident in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+ident+'}');z=t.index(r'\end{statement}',a);t=t[:z]+new+t[z:]
put(rel,t,'Update both original D questions without changing their Open status.')
for name in ['d_results.json','d_coverage.json']:
    rel=Path('ledger')/name;rows=json.loads(get(rel))
    for row in rows:
        if name=='d_results.json' and row['id'] in ['D.13','D.19']:
            row['depends_on'].append('D.61');row['notes']+=' '+details['D.61']
        if name=='d_coverage.json' and row['task'] in ['D.e','D.afterLM2.1']:
            row['statement_ids'].append('D.61');row['outcome']+=' '+details['D.61']
            row['remaining_step']='Evaluate the actual residual J61 boundary, including its331776-dimensional small-character module with562 coinvariants and the26 self-wedge classes surviving the proved norms, then the remaining full profinite source lift.'
    put(rel,enc(rows),'Synchronize original D results and coverage rows.')

rel=Path('code/assemble.py');t=get(rel).decode();needle='\ne_rows = []\n';assert t.count(needle)==1
eids=[x[5] for x in spec[:3]];edetail=' '.join(details[x] for x in eids)
t=t.replace(needle,"\ne_deps['E.23'].extend("+repr(eids)+")\ne_notes['E.23'] += "+repr(' '+edetail)+'\n'+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
       "        row['statement_ids'].extend(x for x in "+repr(tuple(eids))+" if x not in row['statement_ids'])\n"
       "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += "+repr('; '+edetail)+"\n"
       "        row['remaining_step'] = "+repr('Evaluate the remaining lower positional norm factors, intrinsic metabelian/marked preimages and higher layers, remaining quartic coefficient primes and full-source mixed finite realizations.')+'\n')
t=t.replace(needle,block+needle)
old=r"""for entry in re.split(r'(?=^@\w+\s*\{)',bib,flags=re.M):
    if re.match(r'@\w+\s*\{',entry):
        assert re.search(r'\b(?:verified|unverified)\b',entry,re.I), 'Bibliography status missing: '+entry.splitlines()[0]
"""
# Raw strings keep the exact regular-expression escapes of the checked assembler.
assert old in t
new=r'''for match in re.finditer(r'@\w+\s*\{\s*([^,]+),',bib):
    opening=bib.index('{',match.start());depth=0;end=None
    for pos in range(opening,len(bib)):
        escaped=pos>0 and bib[pos-1]=='\\'
        if not escaped and bib[pos]=='{':depth+=1
        elif not escaped and bib[pos]=='}':depth-=1
        if depth==0:end=pos+1;break
    assert end is not None, 'Unclosed bibliography entry: '+match.group(1)
    entry=bib[match.start():end]
    assert re.search(r'\b(?:verified|unverified)\b',entry,re.I), 'Bibliography status missing in this entry: '+match.group(1)
'''
t=t.replace(old,new)
put(rel,t,'Synchronize generated E rows and require each bibliography entry itself to carry its verification status.')

# Amend the one entry whose verified source record existed but its printed note was absent.
rel=Path('ledger/e_elliptic_refs.bib');before=get(rel).decode()
assert read(B/'ledger/e_elliptic_source_evidence.json')[0]['opened'] is True
old='  url = {https://www.ms.u-tokyo.ac.jp/journal/pdf/jms020107.pdf}\n'
new='  url = {https://www.ms.u-tokyo.ac.jp/journal/pdf/jms020107.pdf},\n  note = {Verified: original opened; Sections 2.4.1--2.4.2 and 4.3--4.12, Section 6.3, Theorem 6.6, Corollary 6.7 and Proposition 6.8 with their stated proofs read. Exact page and source-hash evidence is retained in the reading ledger.}\n'
assert before.count(old)==1;after=before.replace(old,new)
cp(B/rel,Path('code/checkpoint214_before218')/rel.with_name(rel.name+'.md'))
put(rel,after,'Print the already verified original-source status; no new reading or upgrade is asserted.')
amendments.append({'file':str(rel),'kind':'Add missing printed verification note from existing exact evidence','before_sha256':digest(before.encode()),'after_sha256':digest(after.encode())})

# Literal prose spacing only, preserving every frozen proof in its author bundle.
literal={'scans172':'scans 172','folios733':'folios 733','equations(371)':'equations (371)','Hilbert90':'Hilbert 90'}
pattern=re.compile(r'\b(Appendix|Corollary|Corollaries|Lemma|Lemmas|Proposition|Propositions|Section|Sections|Theorem|Theorems)(?=[A-Z]?\d)')
targets=[Path('sections')/n for n in ['E_nonunit_seventeen.tex','E_quartic_five_cohomology.tex','E_inert_prime_tail.tex','E_quartic_mixed_five.tex','E_inert_lower_factors.tex']]
targets+=sorted(p.relative_to(B) for p in (B/'ledger').glob('*_refs.bib'))
targets+=sorted(p.relative_to(B) for p in pending if p.parent==B/'ledger' and p.name.endswith('_refs.bib') and p.relative_to(B) not in targets)
for rel in targets:
    before=get(rel).decode();after=before;changes=[]
    for old,new in literal.items():
        n=after.count(old)
        if n:after=after.replace(old,new);changes.append({'old':old,'new':new,'count':n})
    counts={}
    def spacing(m):
        old=m.group(1);counts[old]=counts.get(old,0)+1;return old+' '
    after=pattern.sub(spacing,after)
    changes.extend({'old':k+'<number>','new':k+' <number>','count':v} for k,v in sorted(counts.items()))
    if changes:
        if (B/rel).exists() and rel.parts[0]=='ledger':
            history=Path('code/checkpoint214_before218')/rel.with_name(rel.name+'.md')
            if B/history not in pending:cp(B/rel,history)
        if rel.parts[0]=='sections':
            snapshot=Path('code/checkpoint218_integration/presentation_originals')/rel.name
            put(snapshot.with_name(snapshot.name+'.md'),before,'Exact pre-presentation source.')
        put(rel,after,'Literal visible prose-spacing correction; mathematical symbols and citation keys retained.')
        amendments.append({'file':str(rel),'kind':'Prose spacing only','changes':changes,'before_sha256':digest(before.encode()),'after_sha256':digest(after.encode())})
put(Path('ledger/checkpoint218_presentation_amendments.json'),enc({'status':'PASS','amendments':amendments}),'Record every presentation edit.')

rel=Path('ledger/d_original_source_recheck.md');t=get(rel).decode()
t+='\n## Checkpoint218 public-source pass\n\nThe exact-title, original-volume and institutional searches in retrieval families turn1007, turn1012, turn1013 and turn1014 returned publisher metadata, author bibliographies, the RIMS1997 catalogue and NDL records, together with separate later papers and other chapters. The RIMS catalogue confirms entry1177 without exposing a PartI download. The further Kyoto institutional-repository pass in turn1016 returned separate later papers and the same catalogue. No requested original Ihara1986, Coleman1989 or Ihara1999 PartI proof became readable. No original-proof label changed. The distinct official PARI documentation reading used by E118 is recorded in its own source ledger.\n'
put(rel,t,'Retain the actual public retrieval outcomes without upgrading unread originals.')

# Preserve genuinely empty failed stdout with exact nonempty error evidence.
failure_specs=[
 (Path('code/e115_bundle/code/history/initial_poly_generator/a_quartic_mixed_five.py'),'failure.txt.md','The initial SymPy polynomial-generator selection failed before writing stdout; the actual author traceback is retained.'),
 (Path('code/root_e116_audit/history/initial_warning_guard/verify.py'),'verify.err','The first root replay guard rejected two ordinary PARI stack-size warnings after successful arithmetic comparisons. The exact observed traceback was transcribed after stdout-only redirection, as recorded in provenance.json.')]
for script,error,reason in failure_specs:
    assert get(script.with_suffix('.out'))==b''
    err=script.parent/error;data=get(err);assert data
    put(script.with_name(script.stem+'_status.json'),enc({'status':'failed before result','exit_code':1,'reason':reason,'stderr_path':error,'stderr_sha256':digest(data)}),'Explain the actual failed empty stdout using retained exact error evidence.')
rel=Path('code/package.py');t=get(rel).decode()
t=t.replace("'.csv', '.out', '.md', '.npz'","'.csv', '.out', '.err', '.md', '.npz'")
old="""    interrupted_empty_outputs = []
    for script in (p for p in files if CODE in p.parents and p.suffix in {'.py', '.gp'}):
        assert script.with_suffix('.out').is_file(), 'Missing executed output: ' + script.name
        if not script.with_suffix('.out').stat().st_size:
            status_path = script.with_name(script.stem + '_status.json')
            assert status_path in files, 'Unexplained empty execution output: ' + script.name
            status = json.loads(status_path.read_text())
            assert status.get('status') == 'interrupted before result'
            assert status.get('exit_code') == 130 and status.get('reason')
            interrupted_empty_outputs.append(str(script.relative_to(BASE)))
"""
new="""    interrupted_empty_outputs = []
    failed_empty_outputs = []
    for script in (p for p in files if CODE in p.parents and p.suffix in {'.py', '.gp'}):
        assert script.with_suffix('.out').is_file(), 'Missing executed output: ' + script.name
        if not script.with_suffix('.out').stat().st_size:
            status_path = script.with_name(script.stem + '_status.json')
            assert status_path in files, 'Unexplained empty execution output: ' + script.name
            status = json.loads(status_path.read_text())
            assert status.get('reason')
            if status.get('status') == 'interrupted before result':
                assert status.get('exit_code') == 130
                interrupted_empty_outputs.append(str(script.relative_to(BASE)))
            else:
                assert status.get('status') == 'failed before result'
                assert isinstance(status.get('exit_code'), int) and status['exit_code'] != 0
                error = status_path.parent / status['stderr_path']
                assert error in files and error.stat().st_size
                assert sha(error.read_bytes()) == status['stderr_sha256']
                failed_empty_outputs.append(str(script.relative_to(BASE)))
"""
assert old in t;t=t.replace(old,new)
needle="        f'Interrupted runs with genuinely empty stdout and retained exit/status records: {len(interrupted_empty_outputs)}',\n"
assert needle in t;t=t.replace(needle,needle+"        f'Failed runs with genuinely empty stdout and exact retained error evidence: {len(failed_empty_outputs)}',\n")
put(rel,t,'Archive actual stderr and require exact nonempty error evidence for retained failed empty-output runs.')

for p in list(pending):
    if p.suffix=='.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
        alt=p.with_name(p.stem+'_gp.out');assert alt in pending or alt.exists(),str(p)
        put(p.with_suffix('.out').relative_to(B),get(alt.relative_to(B)),'Byte-identical alias of actual GP stdout.')
for p in pending:
    if p.suffix in {'.py','.gp'}:assert p.with_suffix('.out') in pending or p.with_suffix('.out').exists(),str(p)
rel=Path('code/README.md');t=get(rel).decode()
t+='''

## E115, E116, E118 and D61

The isolated bundles code/e115_bundle, code/e116_bundle and code/e118_bundle retain their code/, inputs/ and exact execution records. E115 accepts --input-dir inputs. E116 and E118 accept --gp /absolute/path/to/gp for complete mathematical reconstructions. E118 requires no external input for its final arithmetic certificate; its separate original discovery program keeps its original working-directory paths and exact E112 binary input, documented in the dependency ledger.

D61 retains all four programs and frozen arithmetic inputs under code/d61_bundle. Its manifest specifies the exact four-stage order. Root rebuilt all stages from copied source/inputs; only named elapsed_seconds fields are excluded from complete JSON/stdout comparisons. E115 root replay has no excluded fields. E116 matches all15 complete text outputs and all six decoded PARI GEN objects; raw binary serialization differences are retained. E118's independent no-input reconstruction matches all source/output/JSON bytes, with no exclusions, and its separate order800 group program checks every cocycle identity.

The initial E115 SymPy failure, initial E116 root warning-guard failure, and initial E118 TeX delimiter failure have genuinely empty stdout. Their real nonzero exit status and exact nonempty error evidence are retained. The package gate checks that evidence and its hash; no artificial successful output is inserted. Existing interrupted runs keep their separate actual status records. All .err evidence is archived.

The precise proof, primary-source and fresh-replay scopes are in the root/peer audit directories. Frozen author proofs are retained before literal spacing corrections. Every bibliography entry now carries its own verification note; Nakamura1995's missing printed note was restored from its existing original-source record, without a new source-verification claim.
'''
put(rel,t,'Document exact reconstruction, independent review and retained failure evidence.')

changes=[]
for p,data in pending.items():
    old=sha(p) if p.exists() else None
    if p.exists() and p.read_bytes()!=data and p.parent==B/'sections':
        h=B/'sections/history/checkpoint214_before218'/p.name;h.parent.mkdir(parents=True,exist_ok=True);assert not h.exists();shutil.copy2(p,h)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    changes.append({'path':str(p.relative_to(B)),'before_sha256':old,'after_sha256':sha(p),'reason':reasons[p]})
record={'status':'PASS','added_statements':[x[5] for x in spec],'expected_statement_count':218,'original_task_rows':33,
        'original_open_statements':['D.13','D.19','E.23'],'frozen_to_archive_mapping':mapping,'changes':changes,
        'build_status':'Assembly, full LuaLaTeX build, all-page rendering and actual visual review follow.'}
(B/'ledger/checkpoint218_integration.json').write_text(enc(record))
print(enc({'status':'PASS','added_statements':record['added_statements'],'expected_statement_count':218,'changed_files':len(changes),'preserved_mappings':len(mapping),'presentation_amendments':len(amendments)}))
