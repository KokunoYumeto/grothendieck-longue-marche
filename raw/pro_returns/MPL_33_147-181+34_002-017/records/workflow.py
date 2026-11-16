from pathlib import Path
import csv, datetime, re, json, hashlib, zipfile
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_33_147-181+34_002-017'
FIELDS=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save_page(cote,scan,tex,elements,sheet_kind='text',remarks=''):
    p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03d}.tex'
    if p.exists(): raise RuntimeError('Page already exists; use explicit revision')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    exists=inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if not exists:w.writerow(FIELDS)
        for i,(kind,pos,words) in enumerate(elements,1):w.writerow([cote,f'{scan:03d}',sheet_kind,f'{cote}-{scan:03d}-{i:02d}',kind,pos,words,'yes'])
    if remarks:
        with (ROOT/'records/reading_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## {cote} scan {scan:03d}\n\n{remarks}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'{cote} scan {scan:03d} done {utc()}\n')
    update_doubts()
    print(f'Saved {cote} scan {scan:03d}: {len(tex)} characters; {len(elements)} inventory elements; {utc()}')
def update_doubts():
    from latex_scan import macro_arguments,split_alternative
    table=ROOT/'records/notation_table.md'
    head=table.read_text(encoding='utf-8') if table.exists() else '# Notation table\n'
    out=[head,'\n## Doubt register\n\nLine numbers refer to the page LaTeX source; each entry is located in its immediate manuscript context. Confidence concerns the tentative reading, not a claim that the whole passage is certain.\n\n| File | Scan | Approximate line | Reading | Alternative | Confidence |\n|---|---:|---:|---|---|---|']
    for p in sorted((ROOT/'pages').glob('*.tex')):
        m=re.search(r'_(\d+)_scan(\d+)\.tex$',p.name);c,s=m.groups();t=p.read_text(encoding='utf-8')
        deletions=macro_arguments(t,'deleted')
        for name,start,end,v in sorted(macro_arguments(t,'unsure')+macro_arguments(t,'illegible'),key=lambda z:z[1]):
            reading,alt=split_alternative(v)
            if name=='illegible':reading=f'Physically unreadable: approximately {v} words';alt='No defensible reading';conf='low'
            else:
                conf='medium'
                if any(a<=start<end<=b for _,a,b,_ in deletions):conf='low'
                low_words={'33/148':['cohomos','déduisent'], '33/150':['à valeurs','bonnes dimensions'], '33/152':['inquiét','vérification','vibrations','sinon','des signes','des cônes'], '33/158':['commutant','donnant','permutation','multiplication'], '33/172':['quotient','produit','générateur'], '33/180':['poncti'], '34/003':['première partie','strictement','$S$'], '34/006':['empilements'], '34/013':['0<e']}
                if f'{c}/{s}'=='34/014' or any(x in v for x in low_words.get(f'{c}/{s}',[])):conf='low'
                if f'{c}/{s}' in ['34/011','34/015'] and ('\\deleted' in v or '\\inserted' in v):conf='low'
            clean=lambda z:z.replace('|','\\|').replace('\n',' ')
            out.append(f'| {c}.pdf | {s} | {t.count(chr(10),0,start)+1} | `{clean(reading)}` | `{clean(alt)}` | {conf} |')
    ab=ROOT/'records/abbreviations.md'
    if ab.exists():out.append('\n'+ab.read_text(encoding='utf-8'))
    leg=ROOT/'records/legibility.md'
    out.append('\n'+leg.read_text() if leg.exists() else '\n## Legibility and confidence\n\nProvisional while work is in progress. Every uncertainty marked in the transcription is registered above. No OCR is used.\n')
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(out),encoding='utf-8')
def checkpoint(number):
    target=ROOT.parent/f'{PREFIX}_checkpoint_{number:02d}.zip'
    if target.exists():raise RuntimeError('Checkpoint exists')
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in str(p):z.write(p,p.relative_to(ROOT))
    return str(target)
