from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R3')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan070.jpg'
items=[
('01_opening_sign_verb',(620,130,1674,345),0,'rel punctuation, first relation, terminal subdivision comma, très and aura with adjoining line'),
('02_deleted_elements',(1020,325,1595,575),0,'cancelled noun after deux; include line above and lower continuation'),
('03_raised_formula_general',(240,470,1090,710),0,'raised F-primes, relation and dash, en-general and i.e. strokes'),
('04_corrected_adjective',(620,750,1025,1045),0,'one overwritten underlined adjective and adjacent lines'),
('05_subdivision_primes_cancelled_phrase',(955,735,1640,1035),0,'singular/plural ending, prime count, cancelled phrase, vu and quoted-word end'),
('06_upper_slanted_note',(17,1132,477,1650),-39,'complete upper marginal note and its extreme right continuation'),
('07_diamond',(340,1080,735,1410),0,'all four objects and four relations, overwritten upper-right relation; adjoining text line'),
('08_double_underlined_definition',(785,1100,1645,1390),0,'contrée accent and double underline, modérée and preceding text line'),
('09_definition_correction_cancelled_clause',(735,1295,1630,1570),0,'d-un-e overwritten letters, repeated-word sign, full cancelled Dans-clause'),
('10_cancelled_label_on_a',(245,1540,1505,1800),0,'cancelled on-a and punctuation, C5, and alleged extra deletion after donner'),
('11_properties',(245,1720,1630,1968),0,'tout deletion, seul, ses-relations lettering and avec placement, both order signs'),
('12_lower_slanted_note',(15,1950,365,2358),-39,'entire lower note including C6 C7 foot and disjonction underline plus double bars'),
('13_c5_formula_tte',(710,1965,1555,2225),0,'C5 relation, tte abbreviation and G/F/ssi forms with surrounding line'),
('14_nb_corrected_letters',(310,2180,1645,2358),0,'entire NB clause and corrected G/F, X/x, plain M, closing bracket')]
records=[]
for name,box,angle,reason in items:
 im=Image.open(src).crop(box)
 if angle:
  im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 factor=2500/im.width
 im=im.resize((2500,round(im.height*factor)),Image.Resampling.LANCZOS)
 im=ImageOps.autocontrast(im,cutoff=0.2).filter(ImageFilter.UnsharpMask(radius=1.2,percent=130,threshold=3))
 p=root/'crops'/(name+'.jpg');im.save(p,quality=94)
 records.append({'path':str(p),'source':src,'bbox':list(box),'scale':factor,'rotation':angle,'reason':reason,'transforms':['PIL crop','rotate BICUBIC expand white' if angle else 'no rotation','LANCZOS resize to 2500 px across','autocontrast cutoff 0.2','UnsharpMask radius 1.2 percent 130 threshold 3','JPEG quality 94']})
root.joinpath('crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created',len(records),'targeted crops. None yet viewed.')
