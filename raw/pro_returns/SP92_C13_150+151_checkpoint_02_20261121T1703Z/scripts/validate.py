from pathlib import Path
import csv,json,hashlib,re,sys
R=Path(__file__).resolve().parents[1]
pages=(R/'page_order.txt').read_text().splitlines()
errors=[];counts={}
def check(test,msg):
    if not test:errors.append(msg)
for page in pages:
    jp=R/'records'/f'{page}.json';tp=R/'pages'/f'{page}.tex'
    check(jp.exists() and tp.exists(),f'Missing final page {page}')
    if not jp.exists() or not tp.exists():continue
    d=json.loads(jp.read_text());s=tp.read_text()
    check(d.get('root_reviewed'),f'No root review {page}')
    level=0
    for line in s.splitlines():
        line=re.split(r'(?<!\\)%',line)[0]
        for m in re.finditer(r'(?<!\\)[{}]',line):
            level+=1 if m.group()=='{' else -1
            if level<0:errors.append(f'Premature closing brace {page}');break
    check(level==0,f'Unbalanced braces {page}: {level}')
    for c in d.get('changes',[]):
        check(c['confidence'] in ['high','medium','low'],f'Confidence {page}/{c["id"]}')
        if c.get('crop'):check((R/c['crop']).exists(),f'Missing crop {c["crop"]}')
    for dec in d.get('decisions',[]):
        check(dec['decision']=='undecided' or bool(dec.get('crop')),f'Resolved mark without crop {dec["id"]}')
    sets=[]
    for suffix in ['boxes','first','second']:
        p=R/'second'/f'{page}_{suffix}.tsv';check(p.exists(),f'Missing {suffix} file {page}')
        if p.exists():
            rows=list(csv.DictReader(p.open(),delimiter='\t'))
            check(len({x['box'] for x in rows})==len(rows),f'Duplicate {suffix} box {page}')
            sets.append({x['box'] for x in rows})
    check(len(sets)==3 and sets[0]==sets[1]==sets[2],f'Box coverage mismatch {page}')
    check(d.get('audited'),f'Blind audit not adjudicated {page}')
    cp=R/'second'/f'{page}_comparison.json'
    ap=R/'second'/f'{page}_adjudications.json'
    check(cp.exists() and ap.exists(),f'Missing scripted comparison/adjudication {page}')
    if cp.exists() and ap.exists():
        comparison=json.loads(cp.read_text()); audit=json.loads(ap.read_text())
        diffs={x['box']:x for x in comparison['results'] if not x['identical_tokens']}
        adjud={x['box']:x for x in audit['adjudications']}
        check(set(diffs)==set(adjud),f'Unadjudicated or extra differing box {page}')
        check(audit.get('root_reviewed'),f'No root audit review {page}')
        check(audit.get('reader')!=d.get('reader'),f'Same reader on both passes {page}')
        for box,x in adjud.items():
            check(x.get('root_viewed') and bool(x.get('evidence')),f'No crop observation {page}/{box}')
            check((R/x['crop']).exists(),f'Missing audit crop {page}/{box}')
            if box in diffs:
                check(x['first']==diffs[box]['first'] and x['second']==diffs[box]['second'],f'Changed written audit readings {page}/{box}')
                check(x['token_difference_count']==len(diffs[box]['token_differences']),f'Token difference coverage {page}/{box}')
        check(d.get('audit_token_difference_runs')==sum(len(x['token_differences']) for x in comparison['results']),f'Audit difference count {page}')
        check(d.get('audit_changed_boxes')==sum(x.get('changed',False) for x in adjud.values()),f'Audit changed count {page}')
    packet_path=R.parent/'reading_packets'/page/'packet.json'
    if packet_path.exists():
        packet=json.loads(packet_path.read_text())
        check({x['diff_id'] for x in d.get('diff_coverage',[])}=={x['diff_id'] for x in packet['differences']},f'C/H difference coverage {page}')
        check({x['id'] for x in d.get('decisions',[])}=={x['id'] for x in packet['marks']},f'Mark coverage {page}')
        if packet.get('witness_H') is None:
            check(not any(x.get('against_H') for x in d['changes']),f'H rows for absent witness {page}')
    check(all(x.get('transcribed')=='yes' for x in d.get('inventory',[])),f'Untranscribed inventory entry {page}')
seal=R/'second/first_reading_hashes.tsv'
check(seal.exists(),'Missing first-reading seal')
if seal.exists():
    sealed=list(csv.DictReader(seal.open(),delimiter='\t'))
    check(len(sealed)==50,'First-reading seal must contain 25 box lists and 25 first readings')
    for x in sealed:
        p=R/x['path']
        check(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],f'Sealed first reading changed: {x["path"]}')
eligibility=R/'records/blind_eligibility.json'
if eligibility.exists():
    exclusions=json.loads(eligibility.read_text())
    # The exclusion is also checked explicitly because its reason is session-specific.
    rp=R/'records/150_scan087.json'
    if rp.exists():
        rr=json.loads(rp.read_text())
        check(rr.get('audit_reader') in ('reader_c','/root/reader_c'), '087 must be audited by reader_c; reader_a saw witness material')
marks=list(csv.DictReader((R.parent/'source/SP92_C13_150+151_texts/MARKS.tsv').open(),delimiter='\t'))
decisions=list(csv.DictReader((R/'decisions.tsv').open(),delimiter='\t'))
check([x['id'] for x in marks]==[x['id'] for x in decisions],'decisions.tsv must match all MARKS ids in order')
for fn,minimum in [('SP92_C13_150+151_inventory.csv',25),('SP92_C13_150+151_collation.tsv',1),('CHECK_EVENTS.tsv',0)]:
    rows=list(csv.DictReader((R/fn).open(),delimiter=',' if fn.endswith('.csv') else '\t'));counts[fn]=len(rows)
    check(len(rows)>=minimum,f'Too few rows {fn}')
counts.update(pages=len(list((R/'pages').glob('*.tex'))),decisions=len(decisions),crops=len(list((R/'crops').glob('*.png'))))
print(json.dumps({'errors':errors,'counts':counts},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
