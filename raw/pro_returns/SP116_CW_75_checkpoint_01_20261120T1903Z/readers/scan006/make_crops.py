from pathlib import Path
from PIL import Image,ImageOps
import json
root=Path('/workspace/scratch/98070f078628/SP116_CW_75_work')
im=Image.open('/workspace/scratch/98070f078628/source/SP116_CW_75_scans/J75-01_75_scan006.jpg')
items=[
('h_insert',[1040,35,1136,123],0),
('dots',[703,183,805,220],0),
('heading_deleted',[1061,294,1171,352],0),
('prop',[401,374,525,447],0),
('soit_suffix',[582,375,708,437],0),
('strict_deleted',[1320,335,1455,423],0),
('empty',[1558,391,1661,448],0),
('soit_insert',[405,433,633,492],0),
('un_deleted',[483,472,579,523],0),
('est_deleted',[1135,477,1238,519],0),
('dit_deleted',[1243,466,1363,519],0),
('direct_deleted',[1375,470,1633,534],0),
('conditions_insert',[1148,425,1584,498],0),
('dorientation',[509,545,777,620],0),
('si_deleted',[874,552,941,607],0),
('brace_deleted',[529,640,594,722],0),
('b_deleted',[450,737,533,813],0),
('autom_deleted',[1241,719,1447,790],0),
('dprime',[1449,718,1548,790],0),
('omega',[651,824,807,893],0),
('ens',[875,829,985,889],0),
('aut_insert',[785,770,1027,859],0),
('autom_b_deleted',[1098,826,1403,887],0),
('orientations_b',[1341,826,1671,899],0),
('inverse_insert',[434,870,941,938],0),
('strict_insert',[934,858,1536,939],0),
('c_insert',[1257,869,1337,924],0),
('two_punct',[914,934,996,995],0),
('et_deleted',[1010,920,1079,975],0),
('si_b_deleted',[1068,920,1155,975],0),
('g_deleted',[1161,924,1239,982],0),
('omega_deleted',[1223,923,1448,985],0),
('phrase_deleted',[1008,920,1538,982],0),
('ssgrpe_deleted',[1235,1026,1451,1107],0),
('forme_deleted',[385,1103,510,1176],0),
('gin_deleted',[668,1100,747,1178],0),
('triv_deleted',[894,1160,1087,1232],0),
('ie_deleted',[1435,1168,1568,1241],0),
('c_deleted_scope',[350,1023,1652,1245],0),
('aut_arrow',[837,1232,1626,1313],-1),
('hom',[698,1312,839,1386],0),
('ssgrpe_c',[899,1408,1122,1479],0),
('tt',[814,1600,898,1675],0),
('produit',[1233,1663,1405,1729],0),
('half',[1397,1660,1449,1725],0),
('direct',[1444,1660,1574,1727],0),
('cor_punct',[1567,1674,1620,1730],0),
('h_est',[1440,1731,1601,1794],0),
('ssgrpe_cor',[431,1879,619,1951],-3),
('etant',[443,1960,562,2038],-3),
('fixee',[1028,1937,1178,2036],-3),
('drawing',[60,401,479,811],0),
('archive5',[37,2268,89,2322],0)
]
manifest={}
for name,box,angle in items:
 p=root/'crops'/('scan006_'+name+'.jpg')
 if p.exists(): raise RuntimeError('Preserve existing crop: '+str(p))
 crop=ImageOps.autocontrast(im.crop(box))
 if angle: crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 scale=2800/max(crop.size)
 crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop.save(p,quality=94)
 manifest[name]={'box':box,'rotate_degrees':angle,'crop':'crops/'+p.name}
(root/'readers/scan006/crop_boxes.json').write_text(json.dumps(manifest,indent=2))
print(len(items),'crops created')
