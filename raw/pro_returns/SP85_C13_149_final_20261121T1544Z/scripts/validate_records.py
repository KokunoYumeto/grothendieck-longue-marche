"""Validate deliverable coverage and links without compiling TeX or reading ink."""
from pathlib import Path
import json,csv,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'
expected=[p.stem for p in sorted((SOURCE/'SP85_C13_149_texts/pages').glob('*.tex'))]
issues=[]
def check(ok,msg):
    if not ok:issues.append(msg)

def illegible_math_offsets(tex):
    """Find forbidden illegibility macros in literal TeX math contexts.

    This is a lexical check, not TeX expansion. It covers dollar math,
    parenthesis/bracket math, standard math environments, tikz-cd cells,
    and ensuremath groups, while skipping comments and escaped delimiters.
    """
    math_environments={
        'math','displaymath','equation','equation*','align','align*',
        'alignat','alignat*','flalign','flalign*','gather','gather*',
        'multline','multline*','eqnarray','eqnarray*','split','aligned',
        'alignedat','gathered','array','matrix','pmatrix','bmatrix',
        'Bmatrix','vmatrix','Vmatrix','smallmatrix','cases','tikzcd',
    }
    token_re=re.compile(
        r'%[^\n]*|\\(?:begin|end)\s*\{[^{}]+\}|'
        r'\\ensuremath\s*\{|\\[A-Za-z]+|\\.|\$\$?|[{}]'
    )
    delimiters=[];environments=[];math_groups=[];depth=0;found=[]
    for match in token_re.finditer(tex):
        token=match.group()
        if token.startswith('%'):continue
        env=re.fullmatch(r'\\(begin|end)\s*\{([^{}]+)\}',token)
        if env:
            action,name=env.groups()
            if name in math_environments:
                if action=='begin':environments.append(name)
                elif name in environments:
                    environments.pop(len(environments)-1-environments[::-1].index(name))
            continue
        if re.fullmatch(r'\\ensuremath\s*\{',token):
            depth+=1;math_groups.append(depth);continue
        if token=='{':depth+=1;continue
        if token=='}':
            if math_groups and math_groups[-1]==depth:math_groups.pop()
            depth-=1;continue
        if token in ('$','$$'):
            if delimiters and delimiters[-1]==token:delimiters.pop()
            else:delimiters.append(token)
            continue
        if token in ('\\(','\\['):delimiters.append(token);continue
        if token in ('\\)','\\]'):
            opener='\\(' if token=='\\)' else '\\['
            if opener in delimiters:
                delimiters.pop(len(delimiters)-1-delimiters[::-1].index(opener))
            continue
        if token in ('\\illegible','\\ill') and (delimiters or environments or math_groups):
            found.append(match.start())
    return found

def frozen_input_issues(assignment,actual):
    """Require intact first-reading and box hashes at final validation."""
    hashes=assignment.get('precomparison_hashes')
    if not isinstance(hashes,dict):return ['Missing precomparison_hashes mapping']
    errors=[]
    for suffix in ('first','boxes'):
        digest=hashes.get(suffix)
        if not isinstance(digest,str) or re.fullmatch(r'[0-9a-f]{64}',digest) is None:
            errors.append(f'Missing or invalid frozen {suffix} hash')
        elif actual.get(suffix)!=digest:
            errors.append(f'Frozen {suffix} input changed or is missing')
    return errors

pages=sorted(p.stem for p in (ROOT/'pages').glob('*.tex'))
check(pages==expected,f'Page coverage: {pages}, expected {expected}')
records={p.stem:json.loads(p.read_text()) for p in (ROOT/'records').glob('149_scan*.json')}
check(sorted(records)==expected,'Approved record coverage differs from page coverage')
marks=list(csv.DictReader((SOURCE/'SP85_C13_149_texts/MARKS.tsv').open(),delimiter='\t'))
decisions=list(csv.DictReader((ROOT/'decisions.tsv').open(),delimiter='\t'))
check([r['id'] for r in marks]==[r['id'] for r in decisions],'MARKS decision IDs/order incomplete or duplicated')
for d in decisions:
    if d['decision']!='undecided':
        path=d['crop'].split(';')[0]
        check(path!='page' and (ROOT/path).is_file(),f"Resolved mark lacks crop: {d['id']}")
for page,p in records.items():
    check(p.get('main_reviewed') is True,f'No main-review flag: {page}')
    check(p.get('audited') is True,f'No completed blind-audit flag: {page}')
    for e in p.get('check_events',[]):
        check(bool(e.get('statement_id')),f'Mathematical event lacks statement ID: {page}')
        check(e.get('type') in ['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'],f'Invalid mathematical-event type {page}: {e.get("type")}')
        if e.get('type')=='refuted':check(bool(e.get('refined_statement_id')),f'Refutation has no refined statement ID: {page}')
    for i,r in enumerate(p.get('rows',[]),1):
        check(r.get('against_C') or r.get('against_H'),f'Neither-witness row {page}:{i}')
        check(r.get('confidence') in ['high','medium','low'],f'Confidence {page}:{i}')
        check(bool(r.get('crop')),f'Material-change row lacks crop: {page}:{i}')
        if r.get('crop'):check((ROOT/r['crop']).is_file(),f'Missing row crop {page}:{i}: {r["crop"]}')
    check(bool(p.get('inventory')),f'Empty inventory {page}')
    check(all(x.get('transcribed')=='yes' for x in p.get('inventory',[])),f'Inventory omission {page}')
    tex=(ROOT/'pages'/f'{page}.tex').read_text()
    depth=0
    for m in re.finditer(r'(?<!\\)[{}]',tex):
        depth+=1 if m.group()=='{' else -1
        check(depth>=0,f'Closing brace without opener {page} at {m.start()}')
    check(depth==0,f'Unbalanced TeX braces {page}: {depth}')
    dollars=len(re.findall(r'(?<!\\)\$',tex))
    check(dollars%2==0,f'Odd inline math delimiter count {page}: {dollars}')
    for offset in illegible_math_offsets(tex):
        check(False,f'Forbidden illegibility macro in math {page} at {offset}')
    check(f'\\scanpage{{{p["scan"]}}}' in tex,f'Scan macro missing {page}')
    for suffix in ['assignment.json','boxes.tsv','first.tsv','second.tsv','comparison.json','adjudication.tsv']:
        check((ROOT/'second'/f'{page}_{suffix}').is_file(),f'Second-reading file missing {page}_{suffix}')
    assignment_path=ROOT/'second'/f'{page}_assignment.json'
    if assignment_path.is_file():
        assignment=json.loads(assignment_path.read_text())
        actual={}
        for suffix in ('first','boxes'):
            path=ROOT/'second'/f'{page}_{suffix}.tsv'
            if path.is_file():actual[suffix]=hashlib.sha256(path.read_bytes()).hexdigest()
        for problem in frozen_input_issues(assignment,actual):
            check(False,f'{page}: {problem}')
    sp=ROOT/'second'/f'{page}_second.tsv'
    if sp.exists():
        boxes=list(csv.DictReader((ROOT/'second'/f'{page}_boxes.tsv').open(),delimiter='\t'))
        second=list(csv.DictReader(sp.open(),delimiter='\t'))
        check([x['box'] for x in boxes]==[x['box'] for x in second],f'Blind box coverage {page}')
        for b in boxes:check((ROOT/'crops'/f'{page}_second_{b["box"]}.jpg').exists(),f'Blind crop missing {page}:{b["box"]}')
        cp=ROOT/'second'/f'{page}_comparison.json';ap=ROOT/'second'/f'{page}_adjudication.tsv'
        if cp.exists() and ap.exists():
            differences={x['box'] for x in json.loads(cp.read_text()) if x['different']}
            adjudicated={x['box'] for x in csv.DictReader(ap.open(),delimiter='\t')}
            check(differences<=adjudicated,f'Unadjudicated token differences {page}: {sorted(differences-adjudicated)}')
combined=(ROOT/'SP85_C13_149_transcription.tex').read_text()
want='\\cotefile{149}\n'+''.join((ROOT/'pages'/f'{page}.tex').read_text().rstrip()+'\n\n' for page in expected if (ROOT/'pages'/f'{page}.tex').exists())
check(combined==want,'Combined fragment differs from ordered page files')
report={'expected_pages':len(expected),'page_files':len(pages),'marks':len(marks),'decision_rows':len(decisions),'issues':issues,'passed':not issues,'tex_compilation_performed':False,'ocr_used':False}
(ROOT/'records/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(bool(issues))
