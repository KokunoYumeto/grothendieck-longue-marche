#!/usr/bin/env python3
"""Render exact PDF regions for reading the manuscript ink."""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'work/root_sources/cote148_selected_31_33.pdf'
doc=fitz.open(src)
regions=[(0,(215,300,325,366),'cote148_quarter_turn'),
         (2,(58,59,205,243),'cote148_arrow_counts')]
for page,rect,name in regions:
    target=src.parent/(name+'.png')
    doc[page].get_pixmap(matrix=fitz.Matrix(5,5),clip=fitz.Rect(rect)).save(target)
    print('PDF selected-page index',page,'rectangle',rect,'rendered as',target.name)
