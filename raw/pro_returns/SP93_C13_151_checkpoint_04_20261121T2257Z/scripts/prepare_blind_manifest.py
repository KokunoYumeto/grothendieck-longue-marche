"""Remove reading clues from box-kind metadata, then freeze first TSV hashes.

Run once, only after every first-pass page is committed. It never changes a box,
the first transcription of a box, or the manuscript transcription. Blind readers
receive the original images and these neutral box lists, not this manifest.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

ROOT=Path('/workspace/scratch/d12e26a9cd50')
OUT=ROOT/'SP93_C13_151_work'

def neutral(kind):
    s=kind.lower()
    categories=[]
    for label,pattern in [
        ('diagram',r'diagram|square|grid|fork|cospan|adjunction'),
        ('table',r'table|count column'),
        ('formula',r'formula|equation|relation|calculation|display|bound'),
        ('drawing',r'drawing|sketch|figure|stroke|segment|tick|frame|enclosure'),
        ('deletion',r'cancel|struck|delet'),
        ('insertion',r'insert|replacement'),
        ('margin note',r'margin'),
        ('handwritten number',r'folio|author number|page number|numeral'),
        ('text',r'word|prose|text|letterhead|heading|typed|note'),
    ]:
        if re.search(pattern,s):categories.append(label)
    result='; '.join(categories) if categories else 'passage'
    refs=re.findall(r'\bB[0-9]{3}\b',kind)
    if refs:result+='; adjacent material covered by '+', '.join(dict.fromkeys(refs))
    return result

def main():
    source=sorted(p.stem for p in (ROOT/'source/SP93_C13_151_texts/pages').glob('*.tex'))
    actual=sorted(p.stem for p in (OUT/'pages').glob('*.tex'))
    if actual!=source:raise ValueError('All first-pass pages must be committed before blind dispatch.')
    target=OUT/'second/first_reading_manifest.json'
    if target.exists():raise FileExistsError('Blind preparation already completed.')
    edits=[];hashes={}
    for name in source:
        b=OUT/'second'/f'{name}_boxes.tsv'
        with b.open(newline='') as f:
            reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
        for row in rows:
            old=row['kind'];row['kind']=neutral(old)
            edits.append({'page':name,'box':row['box'],'old_kind':old,'blind_kind':row['kind']})
        with b.open('w',newline='') as f:
            w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
        for suffix in ['first','boxes']:
            p=OUT/'second'/f'{name}_{suffix}.tsv'
            hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    target.write_text(json.dumps({'prepared':stamp,'sha256':hashes},indent=2)+'\n')
    (OUT/'reviews/blind_metadata_cleanup.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
    with (OUT/'progress.log').open('a') as f:
        f.write(f'blind reading prepared {stamp}: {len(source)} pages; box-kind metadata neutralized without changing coordinates or first readings; first and box TSV hashes recorded.\n')
    print(json.dumps({'pages':len(source),'boxes':len(edits),'hashes':len(hashes)}))

if __name__=='__main__':main()
