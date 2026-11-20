from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(root/'packets/145_scan020/page.jpg')
dest=root/'edition/crops'
items=[
 ('01_equal_abbreviation',[548,62,722,132],0,'Opening = versus expanded même'),
 ('02_relation_four',[315,215,1377,388],0,'Complete relation4, three cancelled rhos, brace labels'),
 ('03_relation_six',[308,466,790,554],0,'Relation6 and possible final stop'),
 ('04_right_nb_margin',[1324,326,1664,636],-25,'Complete diagonal NB margin, three formulas and cancelled term'),
 ('05_main_nb_insertion',[282,550,1112,665],0,'Underlined NB and de plus insertion, full sigma list'),
 ('06_deleted_donc',[752,674,1160,765],0,'rho^3=1 and deleted donc'),
 ('07_prouve_un_mot_pr',[263,684,1654,873],0,'prouve que without aussi; n’est pas un mot; p.r./p.v.'),
 ('08_debuts_deleted_line_one',[260,975,1664,1070],0,'débuts/listes and first cancelled line'),
 ('09_deleted_line_two',[260,1070,1650,1168],0,'primes; qu’on interprète; both primed formulas'),
 ('10_deleted_ie_groupe',[270,1164,653,1282],0,'Cancelled i.e. sigma_i and de notre groupe sigma_i prime'),
 ('11_ici_sigma_relation',[268,1244,1006,1350],0,'Ici on a versus Ceci dit and complete doubtful sigma relation'),
 ('12_relation_seven',[261,1308,1664,1575],0,'Complete relation7 including index cancellation, insertion and deleted comment'),
 ('13_epsilon_centralisateur',[250,1680,1634,2100],0,'Entire epsilon-generator passage, idem doubt, both centralisateur occurrences and punctuation'),
 ('14_chgts_donnent',[247,2090,1450,2210],0,'chgts. de notation indiqués, donnent'),
 ('15_struck_eight',[376,2183,931,2360],0,'Complete cancelled relation8 with internal exponent cancellations and index doubts'),
 ('16_footer_nineteen',[35,2272,107,2347],0,'Lower-left handwritten number'),
 ('17_margin_intro',[18,295,342,970],-45,'Left margin introduction and first presentation'),
 ('18_margin_deleted_relation',[14,862,348,1288],-45,'Crossed marginal product formula'),
 ('19_margin_consequence',[14,1145,355,1584],-45,'Marginal consequence statement, parenthetical identities and cancelled short item'),
 ('20_margin_lzero',[14,1440,355,1845],-45,'Marginal l0 computation, deleted first expression and boxed result'),
 ('21_margin_lone_linfty',[14,1680,355,2015],-45,'Marginal l1 and linfinity formulas, cancelled rhos and disputed rho exponent'),
 ('22_margin_conjugations',[14,1870,355,2208],-45,'Three marginal inner-conjugation formulas'),
]
boxes={}
meta=[]
for name,box,angle,target in items:
    key='145_scan020_'+name
    im=ImageOps.autocontrast(source.crop(box))
    if angle:
        im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    im=im.resize((2800,round(im.height*2800/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    im.save(dest/(key+'.png'))
    boxes[key]=box
    meta.append({'file':'crops/'+key+'.png','box':box,'rotation_degrees':angle,'target':target})
(dest/'145_scan020_crop_boxes.json').write_text(json.dumps(boxes,ensure_ascii=False,indent=2)+'\n')
(dest/'145_scan020_crop_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'crops':len(items),'manifest':str(dest/'145_scan020_crop_boxes.json')},ensure_ascii=False))
