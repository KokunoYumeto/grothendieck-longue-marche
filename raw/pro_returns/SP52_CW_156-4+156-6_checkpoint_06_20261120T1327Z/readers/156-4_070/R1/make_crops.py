from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R1')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan070.jpg'
im=Image.open(source)
targets=[
 ('01_opening',(600,140,1670,345),0,'Opening order sign and punctuation; très/trs and aura/a.'),
 ('02_first_correction',(235,400,1665,705),0,'Deleted noun, raised formula and its relation/dash, following adverb and i.e. group, repeated-word mark and possible parenthesis.'),
 ('03_second_start',(230,750,1635,1030),0,'Singular/plural subdivision, second F prime count, overwritten underlined adjective and following cancelled words.'),
 ('04_diamond',(335,1140,705,1370),0,'Four nodes and relation marks, including worked upper-right mark.'),
 ('05_middle_slant',(20,1140,480,1650),-38,'Entire oblique note, including all line endings and final exclamation.'),
 ('06_definition_head',(770,1185,1655,1385),0,'Contrée/contrie and both double underlines; spelling and state of definition.'),
 ('07_definition_tail',(245,1355,1655,1555),0,'Rewritten d’un(e), repeated-word mark, plain F, comparables; deleted clause and punctuation.'),
 ('08_deleted_labels',(245,1545,1630,1800),0,'Cancelled on a, its stop, cancelled C5 and absence/presence of a deletion after donner.'),
 ('09_lower_para',(250,1740,1625,1970),0,'tout deletion, seul/seule, ses/les and placement of avec; final order sign.'),
 ('10_c5_abbreviation',(1035,1970,1635,2210),0,'Before figure G: tte/toute and adjoining C5 text.'),
 ('11_nb',(305,2140,1645,2354),0,'NB wording and underline, corrected initial letter, equals, X/x, membership, M alphabet, bracket.'),
 ('12_lower_slant',(20,1955,355,2347),-31,'Entire lower slanted note, C6/C7 subscript, disjonction underline, double vertical strokes.'),
]
rows=[]
for name,bbox,rotation,reason in targets:
 crop=im.crop(bbox)
 crop=ImageOps.autocontrast(ImageOps.grayscale(crop))
 if rotation:
  crop=crop.rotate(rotation,Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 scale=2500/crop.width
 crop=crop.resize((2500,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 path=out/'crops'/(name+'.jpg')
 crop.save(path,quality=94)
 rows.append(dict(path=str(path),source=source,bbox=list(bbox),scale=scale,rotation=rotation,reason=reason,transform='grayscale; autocontrast; rotation (PIL degrees); LANCZOS resize to 2500 px width; UnsharpMask radius 1.1 percent 110 threshold 3; JPEG quality 94'))
(out/'crop_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print(json.dumps(rows,ensure_ascii=False,indent=2))
