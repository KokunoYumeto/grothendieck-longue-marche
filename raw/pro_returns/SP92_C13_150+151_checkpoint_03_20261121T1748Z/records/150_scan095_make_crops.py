from pathlib import Path
from PIL import Image
import json
base=Path('/workspace/scratch/d7279cb02214')
im=Image.open(base/'source/SP92_C13_150+151_scans/150_scan095.jpg')
specs=[
('author44',[42,25,116,84],2200),
('reciproque',[1285,54,1648,149],2800),
('ssi',[1095,163,1620,244],2800),
('memes_hypotheses',[304,249,1128,352],3000),
('top_math_insertion',[875,269,1639,447],3000),
('il_f_et_s',[299,462,795,577],2800),
('last_top_line',[300,562,1640,690],3000),
('loc',[838,570,966,646],2400),
('cancelled_sur',[441,716,708,787],2800),
('tt_provoisinage',[864,729,1655,827],3000),
('formula94',[267,872,1117,999],3000),
('margin94',[1205,798,1655,1046],3000),
('on_a',[1038,1006,1237,1072],2400),
('formula95',[285,1088,1552,1426],3000),
('number95_cancel',[280,1122,452,1257],2400),
('empty_first',[675,1108,769,1225],2400),
('caption_dense',[771,1321,984,1418],2600),
('caption_fid',[1269,1293,1444,1404],2600),
('cancelled_cela_ona',[295,1591,787,1689],3000),
('simple_equiv',[944,1537,1536,1659],3000),
('symmetrique_n_a',[299,1675,1640,1895],3000),
('cancelled_comme',[927,1773,1141,1833],2600),
('chance_equivalente',[300,1855,1110,1972],3000),
('formula96',[295,1915,1653,2185],3000),
('caption96',[731,1911,1238,1989],3000),
('number96',[299,2012,457,2097],2400),
('reverse_caption',[731,2092,989,2194],2800),
('formula97',[329,2180,1115,2327],3000),
('folio94',[20,2299,75,2344],2200)]
manifest=[]
for name,box,w in specs:
 crop=im.crop(box)
 crop=crop.resize((w,round(crop.height*w/crop.width)),Image.Resampling.LANCZOS)
 rel='crops/150_scan095_'+name+'.png'
 crop.save(base/'SP92_C13_150+151_work'/rel)
 manifest.append({'crop':rel,'box':box,'rotation':0})
(base/'SP92_C13_150+151_work/records/150_scan095_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(manifest),'original-coordinate crops.')
