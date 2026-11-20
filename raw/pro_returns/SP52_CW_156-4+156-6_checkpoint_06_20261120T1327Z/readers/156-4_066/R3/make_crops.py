from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R3')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg'
items=[
('01_lemma_insert',[1170,110,1645,340],'Raised parenthesis, fini ending, and Il case'),
('02_lemma_b_end',[970,275,1645,500],'nb abbreviation, fini sont and terminal empty-set mark'),
('03_arrow_cancel',[270,540,950,750],'Cancellation immediately after pi zero of G; punctuation'),
('04_first_exponent',[495,650,805,865],'Cancelled exponent and surviving exclamation mark'),
('05_attention_second_exponent',[890,660,1575,950],'Attention and second superscript, including dot/loop distinction'),
('06_quotation',[290,850,1465,1065],'Article du/des, Sup and quote closure'),
('07_tuple_relation',[400,1020,825,1210],'Retraced third relation and its pointer'),
('08_left_c_contree',[205,1030,520,1295],'Left C alphabet and Contrée/Contrie note with pointer'),
('09_below_relation_note',[540,1090,855,1305],'Three-line note, crossed word and following accented mark'),
('10_c4_cancelled_exists',[990,1375,1635,1545],'Cancelled quantifier expression after product'),
('11_c4_overwrite_relation',[990,1490,1660,1675],'Overwritten F_i and terminal membership or turnstile'),
('12_heading',[310,1715,1650,1880],'Contrée résiduelle spelling and separate heading underlines'),
('13_bottom_first_delete',[270,1880,900,2090],'Cancelled indexed family and inserted H_i placement'),
('14_cosupp_deletion',[295,1980,1030,2215],'Deleted Cosupp. Phi and neighbouring live text'),
('15_disjointe',[925,1975,1650,2220],'Ending of disjointe and abbreviation f et s.'),
('16_footer',[300,2190,1530,2350],'Cause of C3 phrase, crossed final word and live Posons')]
im=Image.open(source)
meta=[]
for stem,bbox,reason in items:
    crop=ImageOps.autocontrast(im.crop(tuple(bbox)).convert('RGB'))
    scale=2500/crop.width
    crop=crop.resize((2500,round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=ImageEnhance.Sharpness(crop).enhance(1.25)
    p=out/'crops'/f'{stem}.jpg'
    crop.save(p,quality=94)
    meta.append(dict(path=str(p),source=source,bbox=bbox,scale=scale,rotation=0,reason=reason,transformations='RGB; autocontrast; LANCZOS resize to 2500 pixels across; sharpness 1.25; JPEG quality 94'))
(out/'crop_manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
log=['# Inspection log — reader R3, scan 156-4/066','', 'Started UTC: 2026-11-20 09:24:15', '', '## Ordered views', '1. Whole page: '+source+' — viewed once, native image; layout only.', '2. Upper half: '+source.replace('.jpg','_a.jpg')+' — viewed once, native image; all lines compared with C and H.', '3. Lower half: '+source.replace('.jpg','_b.jpg')+' — viewed once, native image; all lines compared with C and H.', '', '## Open-place crops prepared', 'One crop per named open-place cluster; no OCR or text recognition. All bboxes are pixels in the original whole-page JPEG.', '']
for m in meta:
    log.append(f"- {Path(m['path']).name}: source {m['source']}; bbox {m['bbox']}; scale {m['scale']:.9f}; rotation 0 degrees; {m['transformations']}; reason: {m['reason']}. Pending one inspection.")
(out/'inspection_log.md').write_text('\n'.join(log)+'\n')
print('Created',len(meta),'own crops and manifest; no crop has yet been displayed.')
