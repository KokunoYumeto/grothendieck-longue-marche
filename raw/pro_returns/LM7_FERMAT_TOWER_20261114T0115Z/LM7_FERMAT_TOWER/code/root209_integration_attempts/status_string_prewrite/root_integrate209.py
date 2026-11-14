#!/usr/bin/env python3
"""Integrate E108--110 and the arithmetically amended D59, with exact provenance."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
read=lambda p:json.loads(p.read_text())
pending={};why={};mapping=[]
assert not (BASE/'ledger/checkpoint209_integration.json').exists()

def put(rel,data,reason):
    p=BASE/rel;data=data.encode() if isinstance(data,str) else data
    if p in pending:assert pending[p]==data,rel
    pending[p]=data;why[p]=reason

def copy(src,rel,reason='Exact owned source, actual output or verification record.'):
    dst=BASE/rel
    if dst.exists():assert dst.read_bytes()==src.read_bytes(),str(rel)
    else:put(rel,src.read_bytes(),reason)
    mapping.append({'source':str(src.relative_to(ROOT)),'archive':str(rel),'sha256':sha(src)})

def verify(folder,name,digest):
    p=folder/'ledger'/name;assert sha(p)==digest
    m=read(p)
    for row in m['files']+m.get('immutable_inputs',[]):
        q=folder/row.get('file',row.get('path'))
        assert sha(q)==row['sha256'],str(q)
        if 'bytes' in row:assert q.stat().st_size==row['bytes']
    for row in m.get('exact_inputs',[]):assert sha(ROOT/row['workspace_path'])==row['sha256']
    return m

E108=ROOT/'research_e108';E109=ROOT/'research_e109';E110=ROOT/'research_e110';D59=ROOT/'D59_EXPERIMENTS'
verify(E108,'e_quartic_peripheral_manifest.json','ec73c43c3cf3aa3dd59d6153135d8c04a99364e283b33e7babd50526babe6e3e')
verify(E109,'e_quartic_compact_action_manifest.json','ebf73fde595e439c07c356aff14534c3ad60e44f09322f187b7c576dd4ec5de4')
verify(E110,'e_pure_tower_manifest.json','320003a889adc19fa0c8d59a5629304e271e7a222f51ab41e2c0d0dad383305a')
verify(D59,'d_free_character_invariant_lift_manifest.json','f93e9fb1889fa1048e45ca1caff5ef2672a00cd3290d30d1cd0d465c200186bc')
for name,file in [('root_e108_audit','verification.json'),('bc_e108_audit','audit.json'),
                  ('d_e109_audit','audit.json'),('root_e110_audit','verification.json'),
                  ('a_e110_audit','audit.json'),('root_d59_audit','verification.json')]:
    d=read(ROOT/name/file);assert d.get('status',d.get('audit_status'))=='PASS',(name,d)

amend=read(D59/'audit/d59_numerical_amendment/amendment.json')
old=D59/'audit/d59_numerical_amendment/precorrection/D_free_character_invariant_lift.tex'
if not old.exists():
    choices=list((D59/'audit/d59_numerical_amendment/precorrection').glob('*.tex'))
    assert len(choices)==1;old=choices[0]
new=D59/'sections/D_free_character_invariant_lift.tex'
needle=r'830\,900\,448\,697\,714\,719'
assert old.read_text().count(needle)==1
assert old.read_text().replace(needle,needle+r'\,719')==new.read_text()
num=2*3**49-11351380622391;bound=(num+575)//576
assert bound==amend['ceiling']==830900448697714719719
assert (bound-1)*576<num<=bound*576
put(Path('ledger/root_d59_numerical_amendment.json'),enc({
    'status':'PASS','old_proof_sha256':sha(old),'corrected_proof_sha256':sha(new),
    'exact_only_change':amend['only_proof_change'],'numerator':num,'denominator':576,'ceiling':bound,
    'integer_inequalities_verified':True,'corrected_proof_lines':len(new.read_text().splitlines()),
    'earlier_audit_limit':'The earlier full root audit missed this displayed numerical transcription. '
    'Its complete program replay had the correct integer. This record corrects the proof equality '
    'and the earlier prose line count; all source maps and the finite certificate remain unchanged.'
}), 'Exact arithmetic correction and explicit previous-audit limit.')

# Keep the current build/assembly source and actual logs before this mutation.
for name in ['assemble.py','assemble.out','build_pdf.py','build_pdf.out','latex_pass1.out',
             'latex_pass2.out','latex_pass3.out','bibtex.out']:
    src=BASE/'code'/name
    if src.exists():copy(src,Path('code/checkpoint205_before209')/name)
copy(BASE/'LM7_FERMAT_TOWER_paper.tex',Path('code/checkpoint205_before209/paper_master.tex.md'))

for folder,tag in [(E108,'e108'),(E109,'e109'),(E110,'e110'),(D59,'d59')]:
    for p in sorted(folder.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts:continue
        rel=p.relative_to(folder)
        if rel.parts[0] in ('sources','source_images'):continue
        if p.suffix in ('.pdf','.png','.aux','.log','.bbl','.blg'):continue
        if rel.parts[0]=='qa':
            if p.suffix=='.jpg':rel=Path('qa')/(tag+'_author')/p.name
            elif p.suffix in ('.out','.tex','.bib'):
                rel=Path('code')/(tag+'_author_layout')/(p.name+('.md' if p.suffix in ('.tex','.bib') else ''))
            else:continue
        elif tag=='e110' and rel.parts[0] in ('code','inputs'):
            rel=Path('code/e110_bundle')/rel
        elif rel.parts[0]=='ledger' and p.name in ('e_quartic_compact_action_coverage.json','e_pure_tower_coverage.json'):
            rel=Path('ledger')/(tag+'_staging')/p.name
        elif rel.parts[0] in ('replay','replay_verified','audit','author_fresh_rebuild'):
            rel=Path('code')/(tag+'_retained')/rel
        if p.suffix=='.tex' and rel.parts[0]=='code':rel=rel.with_name(p.name+'.md')
        if p.suffix in ('.diff','.patch'):rel=rel.with_name(p.name+'.md')
        if p.name.endswith('.source.txt'):
            rel=rel.with_name(p.name.replace('.source.txt','.py'))
        elif p.suffix=='.txt':rel=rel.with_name(p.name+'.md')
        copy(p,rel)

# Received audits retain full actual executions, including the two diagnostic
# failures and the exact PARI read-deserialization equality in the root E110 run.
for name in ['root_e108_audit','bc_e108_audit','d_e109_audit','root_e110_audit','a_e110_audit','root_d59_audit']:
    folder=ROOT/name
    for p in sorted(folder.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts or 'source_images' in p.parts:continue
        if p.suffix in ('.png','.jpg','.pdf'):continue
        rel=Path('code')/name/p.relative_to(folder)
        if p.suffix=='.tex' or (p.suffix in ('.py','.gp') and not p.with_suffix('.out').exists()
                               and not p.with_name(p.stem+'_gp.out').exists()):rel=rel.with_name(p.name+'.md')
        copy(p,rel)
    for stem in ['audit','verification','rebuild_comparison']:
        for ext in ['.json','.md']:
            p=folder/(stem+ext)
            if p.exists():copy(p,Path('ledger')/(name+'_'+stem+ext))

# Supply literal stdout aliases for GP programs whose recorded output used
# the historical _gp suffix; the byte equality is part of the archive mapping.
for p in list(pending):
    if p.suffix=='.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
        alt=p.with_name(p.stem+'_gp.out')
        assert alt in pending or alt.exists(),str(p)
        data=pending.get(alt,alt.read_bytes() if alt.exists() else b'')
        put(p.with_suffix('.out').relative_to(BASE),data,'Byte-exact alias of the actual GP stdout recorded with _gp suffix.')

details={
'E.108':'E.108 evaluates every zero-compact quartic abelian input through55 exact shifted cups and the full restricted residue correction, without closure. It proves the rank5 two-ramified family and an explicit norm49 integral three-primary nonlifting example over the zero toric minimum. Actual Fourier and CM projections evaluate the peripheral and determinant central factors; the three displayed CM cohomology types and mixed inputs remain active.',
'E.109':'E.109 evaluates the entire actual compact pro-five class-two outer action through its rank2 pure-CM module. The integral coefficient left inverse, actual affine filling correction, factor2 cycle comparison, order16 average, and literal Bloch isogeny transfer prove that its arithmetic class is nontorsion. The independent p19 point has detecting order5; the invariant test at11 proves rational nonvanishing. Mixed section obstructions remain active.',
'E.110':'E.110 proves all pure-tower three-class groups zero and evaluates every coherent pure divisor and its unit kernel through exact norm-character maps. Combining the pure and complex factors gives the complete actual H section space over kappa3(17) and every unit multiple, with second toric support at3,17 and primes satisfying v3(ord_p17)<=1, and every explicit inverse fibre. Other first classes and the intrinsic metabelian/marked source image remain active.',
'D.59':'D.59 realizes an integral homology correction on every active cusp-safe free character orbit of the actual arithmetic source. Its invariant central block has an injective full norm and compactification, so the unquotiented orientation identity kills its boundary. The exact remaining kernel has dimension48w-2560-5308416*kappa and contains a specified366080-dimensional submodule. The certified bound is kappa>=830900448697714719719. Its remaining boundary and the original full profinite source remain active.'
}
for stem,ident in [('e_quartic_peripheral','E.108'),('e_quartic_compact_action','E.109'),
                    ('e_pure_tower','E.110'),('d_free_character_invariant_lift','D.59')]:
    p=BASE/'ledger'/(stem+'_results.json');rows=json.loads(pending[p]);assert rows[0]['id']==ident
    rows[0]['notes']+=' '+details[ident]+' Completed full audit and exact replay scopes are in the attached root/peer records.'
    rows[0]['notes']=rows[0]['notes'].replace('Root and peer audits pending.','Full root proof and fresh execution audit PASS, with the exact printed-number amendment separately verified. No independent D59 full proof peer audit is claimed.')
    if ident=='E.110':rows[0]['where_proved']=rows[0]['where_proved'].replace('code/e_pure_tower','code/e110_bundle/code/e_pure_tower')
    pending[p]=enc(rows).encode()
    p=BASE/'ledger'/(stem+'_report.md')
    pending[p]+=('\n## Integrated audit and current scope\n\n'+details[ident]+'\n\nFull root review and recorded fresh executions passed. E108, E109 and E110 also have received independent proof reviews. D59 includes its exact numerical amendment. The full-paper layout is verified in the following build.\n').encode()

p=BASE/'LM7_FERMAT_TOWER_paper.tex';t=p.read_text()
for marker,add in [(r'\input{sections/D_full_homology_repaired_block.tex}',r'\input{sections/D_free_character_invariant_lift.tex}'),
                  (r'\input{sections/E_stable_ordinary_phase.tex}','\n'.join(r'\input{sections/'+n+'}' for n in
                   ['E_quartic_peripheral_slice.tex','E_quartic_compact_action.tex','E_pure_tower_complete.tex']))]:
    assert t.count(marker)==1 and add not in t;t=t.replace(marker,marker+'\n'+add)
put(p.relative_to(BASE),t,'Register all four audited statements.')

p=BASE/'sections/E.tex';t=p.read_text();a=t.index(r'\begin{statement}{E.23}');b=t.index(r'\end{statement}',a)
addition=r'''

E.108 now evaluates the entire zero-compact quartic input space
with all fifty-five shifted cups, the exact restricted correction
and its inverse. It includes an explicit integral nonlifting example
over the zero toric minimum and the full rank-five two-ramified family.
The peripheral and determinant central factors have explicit coordinates.
E.109 determines the entire compact pro-five outer arithmetic action
through its rank-two pure-CM projector. Its exact affine comparison,
cycle normalization and original Bloch correspondence prove that this
class is nontorsion. The remaining mixed quartic cup obstruction and
the three retained CM cohomology types continue in the next calculation.

E.110 completes the separate pure-field norm factor and combines it
with E.107. Every pure three-class group is zero; all coherent divisors,
ordinary-unit kernels and their actual maps are evaluated.
The complete actual $H$ section set over $\kappa_3(17)$ and every
unit multiple now has its exact toric image and every inverse fibre.
Its second-coordinate support consists of $3,17$ and the primes
with $v_3(\operatorname{ord}_p17)\leq1$.
This closes the pure-factor question retained in the earlier milestones.
The nonunit and other first classes, their intrinsic metabelian and
marked source images, higher layers and mixed-prime sources remain active.
'''
put(p.relative_to(BASE),t[:b]+addition+t[b:],'Retain the original unrestricted question and update its completed steps.')
p=BASE/'sections/D.tex';t=p.read_text()
addition=r'''

D.59 corrects the full homology on every active cusp-safe free
character orbit of the actual arithmetic source. Its invariant
central block has an injective full norm and compactification;
the exact unquotiented orientation identity therefore kills its
boundary. The residual kernel has dimension
$48w-2560-5\,308\,416\kappa$, where
$\kappa\geq830\,900\,448\,697\,714\,719\,719$.
It contains the specified $366\,080$-dimensional small-character
submodule. Its remaining boundary and full profinite realization
are the next actual-source steps.
'''
for ident in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+ident+'}');b=t.index(r'\end{statement}',a);t=t[:b]+addition+t[b:]
put(p.relative_to(BASE),t,'Update both original full-source questions with the exact D59 result.')
for name in ['d_results.json','d_coverage.json']:
    p=BASE/'ledger'/name;rows=read(p)
    for row in rows:
        if name=='d_results.json' and row['id'] in ['D.13','D.19']:
            row['depends_on'].append('D.59');row['notes']+=' '+details['D.59']
        if name=='d_coverage.json' and row['task'] in ['D.e','D.afterLM2.1']:
            row['statement_ids'].append('D.59');row['outcome']+=' '+details['D.59']
            row['remaining_step']='Evaluate the actual residual J_G boundary, starting with its366080-dimensional small-character submodule, and lift across the remaining full profinite source kernel.'
    put(p.relative_to(BASE),enc(rows),'Synchronize the original D result and task rows.')
p=BASE/'code/assemble.py';t=p.read_text();needle='\ne_rows = []\n';assert t.count(needle)==1
e_detail=' '.join(details[x] for x in ['E.108','E.109','E.110'])
t=t.replace(needle,"\ne_deps['E.23'].extend(['E.108','E.109','E.110'])\ne_notes['E.23'] += "+repr(' '+e_detail)+'\n'+needle)
needle="(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')";assert t.count(needle)==1
block=("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
       "        row['statement_ids'].extend(x for x in ('E.108','E.109','E.110') if x not in row['statement_ids'])\n"
       "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += "+repr('; '+e_detail)+"\n"
       "        row['remaining_step'] = "+repr('Evaluate nonunit and other global H first classes, their intrinsic metabelian/marked source images, higher cubic layers, the mixed quartic obstruction and retained CM cohomology types, and other-primary/mixed sources.')+'\n')
t=t.replace(needle,block+needle);put(p.relative_to(BASE),t,'Synchronize generated E result and task rows.')

# Repair the specific prose spacing seen during the previous actual page review.
spacing=[]
replacements={'exactly864':'exactly 864','all262,144':'all 262,144','order3888':'order 3888',
              'dimension40':'dimension 40','dimension2560':'dimension 2560',
              'folios733':'folios 733','scans172':'scans 172','Hilbert90':'Hilbert--90'}
for relative in ['sections/D.tex','sections/E_next_ordinary_classes.tex','sections/E_stable_ordinary_phase.tex']:
    p=BASE/relative;before=pending.get(p,p.read_bytes());t=before.decode();changes=[]
    for old,new in replacements.items():
        count=t.count(old)
        if count:t=t.replace(old,new);changes.append({'old':old,'new':new,'count':count})
    if changes:
        pending[p]=t.encode();why[p]='Exact visible prose-spacing corrections, plus any recorded mathematical progress paragraph.'
        spacing.append({'path':relative,'changes':changes})
put(Path('ledger/checkpoint209_spacing.json'),enc({'status':'PASS','kind':'prose spacing only','changes':spacing}), 'Retain every literal spacing replacement.')

p=BASE/'code/README.md';t=p.read_text()+'''

## E108--110 and D59

E108: run `python code/a_quartic_w_slice.py`; the exact E105 input is in
`inputs/a_quartic_class2.json`. Full author/root replays and an independent
coefficient/source audit are preserved.

E109: run `python code/e_quartic_ceresa_shadow.py`. The final full replay is
byte-identical in stdout and JSON. Its separate independent coefficient and
finite-point program is under `code/d_e109_audit/code/`.

E110: run `python code/e110_bundle/code/e_pure_tower.py --gp /absolute/path/to/gp`.
The isolated sibling inputs retain the author's exact input-hash map. Without
`--gp` the saved certified base output is checked. The two complete fresh
replays retain all text/JSON identities; the binary certificates were compared
by PARI `read`, with exact full GEN identity rather than raw-byte equality.
Both actual diagnostic failures in the root replay are retained with their
capture provenance. The `_gp.out` files have byte-exact `.out` aliases for their
corresponding GP source names.

D59: run `python code/d_arithmetic_free_characters.py`. Its two exact arithmetic
inputs are beside the source. The full fresh output comparisons exclude only
the explicitly named elapsed-seconds fields. The missing final719 group in the
printed bound was corrected by exact integer arithmetic; the earlier proof,
manifest, actual correction program and all audits remain preserved.

The recorded audit/integration helpers retain their original staging paths.
Source snapshots without a separate execution are marked `.py.md` or `.tex.md`.
Third-party source PDFs and source-page images are excluded from this package.
'''
put(p.relative_to(BASE),t,'Document portable reproduction and every comparison convention.')

changes=[]
for p,data in pending.items():
    before=sha(p) if p.exists() else None
    if p.exists() and p.read_bytes()!=data and p.parent==BASE/'sections':
        history=BASE/'sections/history/checkpoint205_before209'/p.name
        history.parent.mkdir(parents=True,exist_ok=True);assert not history.exists();shutil.copy2(p,history)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    changes.append({'path':str(p.relative_to(BASE)),'before_sha256':before,'after_sha256':sha(p),'reason':why[p]})
record={'status':'PASS','added_statements':['E.108','E.109','E.110','D.59'],
        'expected_statement_count':209,'frozen_to_archive_mapping':mapping,'changes':changes,
        'D59_exact_numerical_amendment':amend,'original_open_statements':['D.13','D.19','E.23'],
        'build_status':'Full assembly, LuaLaTeX build, rendering and actual visual review follow.'}
(BASE/'ledger/checkpoint209_integration.json').write_text(enc(record))
print(enc({'status':'PASS','added_statements':record['added_statements'],
           'expected_statement_count':209,'changed_files':len(changes),'preserved_mappings':len(mapping),
           'D59_exact_ceiling':bound,'prose_spacing_files':len(spacing)}))
