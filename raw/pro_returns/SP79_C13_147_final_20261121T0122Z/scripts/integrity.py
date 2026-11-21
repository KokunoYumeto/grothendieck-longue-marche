"""Exact input-set and byte-integrity checks; no reading decisions."""
from pathlib import Path
import csv, difflib, hashlib, io, json, os, re
from build_reports import ROOT, ORDER, PREFIX

def digest(data):
    return hashlib.sha256(data).hexdigest()

def rows_from_bytes(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t'))

def atomic_write(path, data, exclusive=False):
    path=Path(path)
    if exclusive and path.exists():
        raise ValueError(f'Refusing to replace committed file: {path}')
    temporary=path.with_name(path.name+'.tmp')
    with temporary.open('wb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary,path)

def first_paths():
    return {f'second/147_scan{n:03d}_{s}' for n in ORDER for s in ('boxes.tsv','first.tsv')}

def transcription_paths():
    return {f'pages/147_scan{n:03d}.tex' for n in ORDER}|{f'{PREFIX}_transcription.tex'}

def verify_manifest(path, expected, root=ROOT):
    rows=rows_from_bytes(Path(path).read_bytes())
    names=[r['path'] for r in rows]
    if len(names)!=len(set(names)) or set(names)!=set(expected):
        raise ValueError(f'Incomplete, duplicate or unexpected manifest paths: {path}')
    for row in rows:
        if digest((root/row['path']).read_bytes())!=row['sha256']:
            raise ValueError(f'Committed bytes changed: {row["path"]}')
    return rows

def verify_first():
    return verify_manifest(ROOT/'second/FIRST_READING_SHA256.tsv',first_paths())

def verify_freeze():
    return verify_manifest(ROOT/'TRANSCRIPTION_SHA256.tsv',transcription_paths())

def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ0-9]+|[^\s]',s)

def compare_bytes(n, first_bytes, second_bytes):
    first=rows_from_bytes(first_bytes);second=rows_from_bytes(second_bytes)
    fm={r['box']:r['reading'] for r in first};sm={r['box']:r['reading'] for r in second}
    if len(fm)!=len(first) or len(sm)!=len(second) or set(fm)!=set(sm):
        raise ValueError('Duplicate or mismatched box identifiers')
    items=[]
    for box,a in fm.items():
        b=sm[box];at=tokens(a);bt=tokens(b)
        if at==bt:continue
        ops=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(a=at,b=bt,autojunk=False).get_opcodes():
            if tag!='equal':ops.append({'operation':tag,'first_tokens':at[i:j],'second_tokens':bt[k:l]})
        items.append({'box':box,'first':a,'second':b,'token_differences':ops})
    return {'scan':n,'boxes':len(first),'differences':len(items),'items':items}

def verify_second(n):
    stem=f'147_scan{n:03d}'
    path=f'second/{stem}_second.tsv'
    return verify_manifest(ROOT/'second'/f'{stem}_second_SHA256.tsv',{path})

def resolve_view_image(image, root=None):
    """Resolve historical paths after a checkpoint moves, without editing logs."""
    root=ROOT if root is None else Path(root)
    path=Path(image)
    if not path.is_absolute():
        return root/path
    parts=path.parts
    for i in range(len(parts)-1):
        if parts[i:i+2]==('work',PREFIX):
            return root.joinpath(*parts[i+2:])
        if parts[i:i+2]==('source',PREFIX+'_scans'):
            return root.parents[1].joinpath(*parts[i:])
    return path

def verify_views(n, reader=None):
    stem=f'147_scan{n:03d}'
    expected={r['box'] for r in rows_from_bytes((ROOT/'second'/f'{stem}_boxes.tsv').read_bytes())}
    rows=rows_from_bytes((ROOT/'second'/f'{stem}_view_log.tsv').read_bytes())
    original_id=f'{n:03d}-ORIGINAL'
    observed={r['box'] for r in rows}
    if observed-{original_id}!=expected:
        raise ValueError(f'Blind image-view log does not cover every prescribed box: {stem}')
    readers={r['reader'] for r in rows}
    if len(readers)!=1 or (reader is not None and readers!={reader}):
        raise ValueError(f'Inconsistent blind reader in image-view log: {stem}')
    for row in rows:
        path=resolve_view_image(row['image'])
        if not path.is_file():raise ValueError(f'Missing viewed blind crop: {row["image"]}')
        if row['box']==original_id:
            original=ROOT.parents[1]/'source/SP79_C13_147_scans'/f'{stem}.jpg'
            if path.resolve()!=original.resolve():
                raise ValueError(f'Original-image view has an unexpected path: {row["image"]}')
    return rows

def verify_comparison(n):
    verify_second(n)
    stem=f'147_scan{n:03d}'
    actual=compare_bytes(n,(ROOT/'second'/f'{stem}_first.tsv').read_bytes(),
        (ROOT/'second'/f'{stem}_second.tsv').read_bytes())
    recorded=json.loads((ROOT/'second'/f'{stem}_comparison.json').read_text())
    if actual!=recorded:
        raise ValueError(f'Stale or altered token comparison: {stem}')
    return actual
