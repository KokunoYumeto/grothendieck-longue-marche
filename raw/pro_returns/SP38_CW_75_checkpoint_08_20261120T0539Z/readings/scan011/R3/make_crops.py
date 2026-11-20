from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
root = Path('out/readings/scan011/R3')
source = '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan011.jpg'
loci = [
('L01_heading', [820,55,1195,140], 7, 0, 'C01 contracted group word and C02 group alphabet remain open after half a.'),
('L02_cancelled_opening', [295,135,900,260], 4, 0, 'C03-C05: structure, lower words and object of canceled initial attempt obscured by crossing.'),
('L03_splitting', [635,425,1435,515], 4, 0, 'C06 and C/H difference splitting/section; inspect compressed word and its immediate agreement endings.'),
('L04_verb', [320,805,930,885], 4, 0, 'C07 verb before t-prime remains compressed; H proposes aura.'),
('L05_verification', [680,1080,1345,1225], 4, 0, 'C08 composition mark and exact bracket/underbrace span remain open.'),
('L06_cancelled_gamma', [525,1243,1265,1335], 4, 0, 'C09 first gamma in struck calculation is overwritten.'),
('L07_proof_subscript', [925,1350,1530,1445], 4, 0, 'C10 second q-subscript has a closed lower shape, unlike the preceding t.'),
('L08_itou', [95,1420,620,1635], 5, 0, 'Itou/Idem lettering unresolved; same locus has C/H enclosure versus asserted connection discrepancy.'),
('L09_nb', [1355,1620,1660,1755], 8, 0, 'C11 short word before n and marginal punctuation remain compressed.'),
('L10_cancelled_gamma_subset', [460,1650,690,1760], 10, 0, 'C12 crossed Gamma and following relation need inspection; H leaves illegible.'),
('L11_dihedral', [1145,1885,1640,2050], 5, 0, 'C13 spelling diédral/diédhral, H d-indice doubt, and D alphabet remain open.'),
('L12_final_insertion', [1210,2097,1655,2190], 6, 0, 'C14 crossed d-order clause and exact state of replacement must be inspected.'),
('L13_detached_point', [330,1780,630,1895], 8, 0, 'Detached dark mark left of Aff comparison: writing versus surface trace remains uncertain.'),
]
with Image.open(source) as im:
    im = im.convert('RGB')
    for name, box, scale, rotation, reason in loci:
        crop = im.crop(tuple(box))
        crop = ImageOps.autocontrast(crop)
        crop = crop.resize((crop.width*scale, crop.height*scale), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1.4, percent=140, threshold=3))
        if rotation:
            crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        crop.save(root / (name + '.png'))
manifest = {'scan':'011','reader':'R3','source_image':source,'source_dimensions':[1685,2361],
'whole_viewed_once':True,'halves_viewed_once_each':True,'half_b_y_offset':1100,
'crop_count':len(loci),'crops':[{'id':name,'bbox':box,'rotation_degrees':rotation,'scale':scale,
'operations':['autocontrast','LANCZOS enlargement','UnsharpMask radius=1.4 percent=140 threshold=3'],
'file':'readings/scan011/R3/'+name+'.png','reason':reason,'visually_inspected':False}
for name,box,scale,rotation,reason in loci]}
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Wrote 13 distinct unresolved-locus crops and crop_manifest.json')
