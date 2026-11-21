"""Root's previously unadjudicated scan004 loci; one crop per local group."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path(__file__).resolve().parents[1]
src=root.parent/'source/SP40_CW_81_scans/J81-01_81_scan004.jpg'
targets=[
 ('01_left_brace_relations',(75,475,495,905),'Outer left brace and punctuation at the left boxed equalities'),
 ('02_left_case_ends',(875,500,1150,705),'Ends of both left upper case labels; H terminal comma'),
 ('03_below_box_eta',(790,902,1360,1016),'Eta equalities, relative position and H punctuation'),
 ('04_below_box_condition',(475,948,825,1045),'Degree condition and terminal punctuation'),
 ('05_lower_annotation_extent',(520,1370,635,1475),'Complete lower extent of first expansion annotation, clipped in reader crops'),
 ('06_e2_e3_block',(25,1260,330,1475),'Separate two-line e2/e3 block and punctuation'),
 ('07_upper_right_brace',(1315,105,1770,630),'Tall outer right brace and first equality punctuation'),
 ('08_upper_right_case_labels',(1655,145,2105,310),'Two si labels and case-end punctuation'),
 ('09_right_linear_end',(1835,315,2145,435),'End of right f_i e_1 linear-combination line'),
 ('10_rule_identity_end',(1665,660,2325,825),'Underlining continuation and identity terminal punctuation'),
 ('11_lower_bound',(1510,785,1750,865),'Lower bound and terminal punctuation'),
 ('12_vertical_chain',(1340,974,1628,1430),'Descending equality signs and attachment beneath original member'),
 ('13_lower_case_labels',(2265,815,2455,1030),'Lower odd/even condition abbreviations'),
 ('14_circled_result',(1850,1260,2455,1455),'Donc, circled beta=0, alpha=plus/minus1 and punctuation'),
 ('15_foot_eta_delta',(1460,1590,2210,1795),'Last two equalities, line order and punctuation')
]
dest=root/'crops/004';dest.mkdir(parents=True,exist_ok=True)
manifest=[]
with Image.open(src) as full:
 for name,bbox,purpose in targets:
  path=dest/(name+'.png')
  if path.exists():raise RuntimeError('Refusing to recrop existing locus: '+name)
  im=ImageOps.autocontrast(full.crop(bbox))
  width=2600
  im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
  im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
  im.save(path)
  manifest.append({'path':str(path.relative_to(root)),'bbox':bbox,'purpose':purpose,'rotation':0,'viewed':False})
(dest/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'new root crops; no whole or half images emitted.')
