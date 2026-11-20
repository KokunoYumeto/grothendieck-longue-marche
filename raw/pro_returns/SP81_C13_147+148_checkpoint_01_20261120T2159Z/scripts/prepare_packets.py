from pathlib import Path
import csv,json
r=Path(__file__).resolve().parents[2];out=r/'edition';s=r/'source';texts=s/'SP81_C13_147+148_texts'
marks=list(csv.DictReader((texts/'MARKS.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
diffs=list(csv.DictReader((s/'SP81_C13_147+148_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
for n,d in enumerate(diffs,1):d['row']=n
manifest=json.loads((out/'work/manifest.json').read_text())
for p in manifest:
 name=p['page'];cote=p['cote'];scan=p['scan'];h=texts/'hua'/f'hua_{name}.tex'
 bits=[f'# Page {name}',f"Image: {s/'SP81_C13_147+148_scans'/f'{name}.jpg'}",f"Original dimensions: {p['width']} × {p['height']}",f"Halves: {p['halves']}",'## Witness C','```tex',(texts/'pages'/f'{name}.tex').read_text(),'```','## Witness H','```tex',h.read_text() if h.exists() else '[No witness H for this page]','```','## C doubt marks',json.dumps([x for x in marks if x['cote']==cote and int(x['scan'])==scan],ensure_ascii=False,indent=2),'## C/H difference rows',json.dumps([x for x in diffs if x['page']==name],ensure_ascii=False,indent=2),'## Preamble', '```tex',(texts/'PREAMBLE.tex').read_text(),'```']
 (out/'packets'/f'{name}.md').write_text('\n\n'.join(bits))
print('Prepared',len(manifest),'page packets:',len(marks),'marks;',len(diffs),'input difference rows. Literal TSV quotes preserved (QUOTE_NONE).')
