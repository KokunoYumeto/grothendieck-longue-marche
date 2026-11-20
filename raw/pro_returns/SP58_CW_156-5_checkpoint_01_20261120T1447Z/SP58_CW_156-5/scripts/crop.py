"""Inspection crops only; never OCR; source images and crop pixels are excluded from delivery."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import csv

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1]

def crop(scan, key, box, angle=0, width=2800):
    folder = 'J156-5-05' if scan < 42 else 'J156-5-06'
    source = ROOT/'source/SP58_CW_156-5_scans'/f'{folder}_156-5_scan{scan:03d}.jpg'
    p = ROOT/'crops'/f'{scan:03d}_{key}.png'
    if p.exists():
        raise ValueError('A crop with this identifier already exists: do not recrop a decided place')
    im = Image.open(source).crop(box)
    im = ImageOps.autocontrast(im, cutoff=0.5)
    if angle:
        im = im.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    ratio = width/im.width
    im = im.resize((width, round(im.height*ratio)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=3))
    im.save(p)
    log = OUT/'CROP_LOG.tsv'
    fresh = not log.exists()
    with log.open('a', newline='') as f:
        w=csv.writer(f,delimiter='\t')
        if fresh: w.writerow(['scan','crop_id','x0','y0','x1','y1','rotation_degrees','rendered_width'])
        w.writerow([scan,key,*box,angle,width])
    return p
