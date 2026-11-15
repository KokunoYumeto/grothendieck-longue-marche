#!/usr/bin/env python3
"""Render a checkpoint PDF and make a spread of pages for visual inspection."""
from pathlib import Path
import argparse, json
import fitz
from PIL import Image, ImageOps, ImageDraw

parser=argparse.ArgumentParser()
parser.add_argument('number')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
out=root/'qa'/('checkpoint_'+args.number)
out.mkdir(parents=True,exist_ok=True)
pdf=fitz.open(root/'EXIT_TOWER_paper.pdf')
needles={
    'C1_bridge_lattice':'C.1.',
    'C7_filling_kernel':'C.7.',
    'D10_threefold':'D.10.',
    'B33_wide_display':'(B.33)',
    'E23_wrapping_table':'E.23.',
    'E24_frame_display':'E.24.',
    'D22_new_complex':'D.22.',
    'B22_new_model':'B.22.',
    'B23_cover_functor':'B.23.',
    'T6_genus_one':'E.T6.',
    'T7_elliptic_topos':'E.T7.',
    'X1_residue':'E.X1.'
}
locations={key:[] for key in needles}
for i,page in enumerate(pdf):
    text=page.get_text()
    for key,needle in needles.items():
        if needle in text:locations[key].append(i+1)
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page_{i+1:03d}.png')
selected=sorted(set([1,2,len(pdf)]+[1+round(k*(len(pdf)-1)/9) for k in range(10)]
                    +[page for pages in locations.values() for page in pages]))
for block in range(0,len(selected),12):
    pages=selected[block:block+12]
    sheet=Image.new('RGB',(1200,4*580),'#d8d8d8')
    draw=ImageDraw.Draw(sheet)
    for j,num in enumerate(pages):
        im=Image.open(out/f'page_{num:03d}.png')
        im.thumbnail((390,548))
        x=(j%3)*400+(400-im.width)//2
        y=(j//3)*580+24
        sheet.paste(im,(x,y))
        draw.text(((j%3)*400+12,(j//3)*580+5),f'Page {num}',fill='black')
    sheet.save(out/f'contact_{block//12+1:02d}.png')
record={'pages':len(pdf),'rendered_pages':len(pdf),
        'keyword_locations':locations,'spread_pages':selected,
        'note':'Rendering is complete; the separate visual-inspection record states which images were actually viewed.'}
(out/'render_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
