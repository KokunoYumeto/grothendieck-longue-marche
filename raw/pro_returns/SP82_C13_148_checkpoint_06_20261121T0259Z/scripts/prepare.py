from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import csv, json, sys

ROOT = Path('/workspace/scratch/8132fe1cca43')
OUT = ROOT/'work/SP82_C13_148'
SOURCE = ROOT/'source'

def packet(scan):
    name=f'148_scan{scan:03d}'
    dest=ROOT/'work/packets'/name
    dest.mkdir(parents=True,exist_ok=True)
    image=SOURCE/'SP82_C13_148_scans'/f'{name}.jpg'
    im=Image.open(image)
    w,h=im.size
    halves=ROOT/'work/halves'
    boxes=([(0,0,w,round(h*.55)),(0,round(h*.45),w,h)] if h>=w else
           [(0,0,round(w*.55),h),(round(w*.45),0,w,h)])
    for i,b in enumerate(boxes,1):
        fn=halves/f'{name}_half{i}.png'
        if not fn.exists(): im.crop(b).save(fn)
    prompt=(ROOT/'upload/PROMPT(20261120-214606).md').read_text()
    errors=prompt.split('## The errors that recur in these papers: read this before the first page')[1].split('## Our conventions')[0]
    conventions=prompt.split('## Our conventions')[1].split('## Method')[0]
    (dest/'rules.md').write_text('# Recurrent errors\n'+errors+'\n# Conventions\n'+conventions)
    (dest/'PREAMBLE.tex').write_text((SOURCE/'SP82_C13_148_texts/PREAMBLE.tex').read_text())
    (dest/'C.tex').write_text((SOURCE/'SP82_C13_148_texts/pages'/f'{name}.tex').read_text())
    hf=SOURCE/'SP82_C13_148_texts/hua'/f'hua_{name}.tex'
    (dest/'H.tex').write_text(hf.read_text() if hf.exists() else '% No witness H for this page.\n')
    for source,target,col,value in [('SP82_C13_148_texts/MARKS.tsv','marks.tsv','scan',str(scan)),('SP82_C13_148_C_H_differences.tsv','differences.tsv','page',name)]:
        # These supplied TSVs use literal quote characters as manuscript tokens,
        # not CSV quoting. Treating quotes as delimiters joins unrelated lines.
        rows=list(csv.DictReader((SOURCE/source).open(),delimiter='\t',quoting=csv.QUOTE_NONE))
        with (dest/target).open('w') as f:
            wr=csv.DictWriter(f,fieldnames=['source_row']+list(rows[0]),delimiter='\t');wr.writeheader()
            wr.writerows(dict(source_row=i,**r) for i,r in enumerate(rows,1) if r[col]==value)
    (dest/'notation.md').write_text((OUT/'notation.md').read_text())
    (OUT/'readers'/name).mkdir(parents=True,exist_ok=True)
    meta={'scan':scan,'name':name,'image':str(image),'width':w,'height':h,'halves':[str(halves/f'{name}_half{i}.png') for i in [1,2]],'half_boxes':boxes,'output':str(OUT/'readers'/name),'crops':str(OUT/'crops')}
    (dest/'meta.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta))

def crop(scan,label,box,angle=0):
    name=f'148_scan{scan:03d}'
    dest=OUT/'crops'/f'{name}_{label}.png'
    if dest.exists(): raise ValueError(f'Crop already exists: {dest}; reuse it.')
    im=Image.open(SOURCE/'SP82_C13_148_scans'/f'{name}.jpg').crop(box)
    im=ImageOps.autocontrast(im)
    if angle: im=im.rotate(angle,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
    scale=max(1,2500/im.width)
    im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=125,threshold=3))
    im.save(dest)
    with (OUT/'crops'/f'{name}_manifest.tsv').open('a') as f:
        f.write('\t'.join(map(str,[dest.name,*box,angle]))+'\n')
    print(str(dest))

if __name__=='__main__':
    if sys.argv[1]=='packet': packet(int(sys.argv[2]))
    elif sys.argv[1]=='crop': crop(int(sys.argv[2]),sys.argv[3],tuple(map(int,sys.argv[4:8])),float(sys.argv[8]) if len(sys.argv)>8 else 0)
