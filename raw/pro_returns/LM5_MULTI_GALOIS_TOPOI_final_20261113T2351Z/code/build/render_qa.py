"""Render a spread of final paper pages and both corrected overflow loci."""
from pathlib import Path
import json, re, subprocess
from PIL import Image, ImageOps, ImageDraw

BASE = Path('/workspace/scratch/36f9c078cbe9')
ROOT = BASE / 'deliverable'
pdf = ROOT / 'LM5_MULTI_GALOIS_TOPOI_paper.pdf'
pages = subprocess.check_output(['pdftotext','-layout',str(pdf),'-'], text=True).split('\f')
if not pages[-1].strip():
    pages.pop()
flat = [re.sub(r'\s+', ' ', p) for p in pages]
anchors = ['F.13 (Proved)', 'F.19 (Proved)', 'F.23 (Proved)',
           'F.44 (Open)', 'F.47 (Proved)', 'F.48 (Proved)',
           'F.49 (Proved)', 'F.50 (Proved)', 'F.51 (Refuted)',
           'LM8_LIE_APPROXIMATIONS', '2726 finite']
locations = {}
for anchor in anchors:
    hits = [i+1 for i,p in enumerate(flat) if anchor in p]
    locations[anchor] = hits
chosen = {1,8,18,28,38,48,58,68,len(pages)}
for hits in locations.values():
    if hits:
        chosen.add(hits[0])
# Include continuation of the stack counterexample, which contains its display.
if locations['F.51 (Refuted)']:
    chosen.add(locations['F.51 (Refuted)'][0] + 2)
chosen = sorted(x for x in chosen if 1 <= x <= len(pages))
out = ROOT / 'verification/final_pages'
out.mkdir(parents=True, exist_ok=True)
for n in chosen:
    prefix = out / f'page_{n:03d}'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','105','-singlefile','-png',str(pdf),str(prefix)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
tiles = []
for n in chosen:
    pic = Image.open(out / f'page_{n:03d}.png').convert('RGB')
    pic.thumbnail((360,510))
    tile = Image.new('RGB',(380,545),'#e5e7eb')
    tile.paste(pic,((380-pic.width)//2,28))
    ImageDraw.Draw(tile).text((12,8),f'Page {n}',fill='black')
    tiles.append(tile)
for group in range((len(tiles)+7)//8):
    selected = tiles[group*8:(group+1)*8]
    grid = Image.new('RGB',(380*4,545*2),'white')
    for i,tile in enumerate(selected):
        grid.paste(tile,((i%4)*380,(i//4)*545))
    grid.save(out / f'spread_{group+1}.jpg',quality=90)
record = {'pdf_pages':len(pages),'rendered_pages':chosen,'anchor_pages':locations,
          'images_are_rendered_not_yet_claimed_inspected':True}
(ROOT / 'verification/render_qa_output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
