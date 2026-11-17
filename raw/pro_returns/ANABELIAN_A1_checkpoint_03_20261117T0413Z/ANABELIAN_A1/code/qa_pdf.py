"""Render specified manuscript pages and record the exact LuaLaTeX overflow log."""
from pathlib import Path
import argparse, json, re
import fitz
from PIL import Image, ImageDraw

p=argparse.ArgumentParser()
p.add_argument('--log',required=True)
p.add_argument('--out',required=True)
p.add_argument('--pages',required=True)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
log=(root/a.log).read_text()
widths=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in widths), widths
assert 'Fatal error' not in log and 'Missing character' not in log
assert not re.search(r'(Citation .* undefined|There were undefined|undefined references)',log)
doc=fitz.open(root/'ANABELIAN_A1_paper.pdf')
out=root/a.out;out.mkdir(parents=True,exist_ok=True)
pages=sorted(set(int(x) for x in a.pages.split(',') if int(x)<=len(doc)))
tiles=[]
for n in pages:
    pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
    path=out/f'page_{n:03d}.png';pix.save(path)
    im=Image.open(path).convert('RGB');im.thumbnail((360,510))
    tile=Image.new('RGB',(380,550),'#eeeeee');tile.paste(im,((380-im.width)//2,28))
    ImageDraw.Draw(tile).text((10,8),f'Page {n}',fill='black')
    tiles.append(tile)
sheet=Image.new('RGB',(380*3,550*((len(tiles)+2)//3)),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%3)*380,(i//3)*550))
sheet.save(out/'contact.png')
data={'pages':len(doc),'sample_pages':pages,'overfull_all_pt':widths,
      'overfull_greater_than_2pt':sum(x>2 for x in widths),
      'undefined_citations_or_references':False,'missing_glyphs':False,
      'visual_inspection':'Rendered; manual review recorded separately.'}
(out/'inspection.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
