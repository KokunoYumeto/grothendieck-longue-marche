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
    'X1_residue':'E.X1.',
    'B25_complete_model':'B.25.',
    'B27_finite_colimit':'B.27.',
    'D27_genus_two':'D.27.',
    'D12_genus_two_display':'(D.12)',
    'E26_normalizers':'E.26.',
    'E27_operad':'E.27.',
    'T10_higher_topos':'E.T10.',
    'T11_surface_topos':'E.T11.',
    'T12_unstable_topos':'E.T12.',
    'B28_sewing':'B.28.',
    'D28_elliptic_three':'D.28.',
    'E28_involution':'E.28.',
    'E29_arrow_topology':'E.29.',
    'B29_sphere_covers':'B.29.',
    'B30_sphere_colimit':'B.30.',
    'B31_path_comparison':'B.31.',
    'D29_elliptic_dictionary':'D.29.',
    'D30_peiffer_comparison':'D.30.',
    'E30_cross_parameter':'E.30.',
    'E31_mixed_pants':'E.31.',
    'E32_adjacent_topology':'E.32.',
    'E33_tail_normalizers':'E.33.',
    'E34_full_sewing':'E.34.',
    'E35_intrinsic_sewing':'E.35.',
    'E36_capping':'E.36.',
    'E37_cover_comparison':'E.37.',
    'E38_adjacent_presentation':'E.38.',
    'E39_exit_extension':'E.39.'
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
