from pathlib import Path
from PIL import Image,ImageOps
import json
r=Path('/workspace/scratch/98070f078628/SP116_CW_75_work')
im=Image.open('/workspace/scratch/98070f078628/source/SP116_CW_75_scans/J75-02_75_scan010.jpg')
items=[
('affine',[530,70,640,147],0),
('associe',[639,79,800,128],0),
('a_title',[799,78,832,127],0),
('title_z',[1076,76,1147,137],0),
('s_top',[739,105,819,166],0),
('gr_op',[470,202,573,250],0),
('op_punct',[513,208,577,250],0),
('diagram',[134,113,1173,343],0),
('gamma_punct',[310,333,569,392],0),
('q_punct',[314,399,593,458],0),
('tau_super',[576,449,645,491],0),
('tau_formula',[313,448,675,551],0),
('restriction',[224,559,680,665],0),
('vertical_equiv',[1263,291,1602,529],0),
('aff_sub_deleted',[635,725,765,813],0),
('zd_deleted',[788,671,893,739],0),
('aff_product_formula',[594,668,1640,816],0),
('produit',[1241,674,1415,745],0),
('half',[1425,674,1487,741],0),
('naturel',[1425,809,1609,889],0),
('aut_deleted',[432,916,774,1036],0),
('equal_deleted',[955,959,1007,997],0),
('savoir',[1052,945,1192,999],0),
('hom_head',[378,1104,691,1175],0),
('ens_punct',[504,1114,641,1174],0),
('groupes',[892,1110,1043,1178],0),
('variables',[1044,1106,1220,1170],0),
('eg_morphism',[516,1180,936,1292],0),
('nb_deleted',[345,1251,419,1313],0),
('eprime',[522,1287,575,1351],0),
('gprime',[961,1294,1039,1345],0),
('empty_insert',[1044,1225,1321,1297],0),
('pour_deleted',[432,1404,506,1446],0),
('si_kept',[506,1402,547,1448],0),
('en',[1473,1388,1545,1442],0),
('termes',[312,1465,470,1532],0),
('de',[496,1474,567,1523],0),
('rho',[603,1472,650,1548],0),
('group_insert',[518,1530,782,1595],-3),
('grpe_insert',[521,1540,607,1594],-3),
('ssjacent_insert',[601,1530,777,1590],-3),
('un_absent',[554,1575,620,1651],0),
('v_punct',[719,1563,859,1654],0),
('un_corps',[812,1585,991,1651],0),
('pex',[1228,1581,1321,1647],0),
('member_z',[321,1920,363,1988],0),
('member_gamma',[380,1919,481,2017],0),
('product_tuple',[301,1859,1013,2026],0),
('non_deg',[1323,2036,1544,2118],0),
('q_insert',[1495,2011,1553,2053],0),
('on',[1530,2060,1622,2120],0),
('a_le',[314,2100,428,2169],0),
('transf',[1063,2100,1207,2172],0),
('invarient',[310,2165,496,2228],0),
('depl',[636,2218,755,2289],0),
('depl_sub',[742,2240,836,2303],0),
('depl_formula',[632,2216,1386,2310],0),
('archive9',[45,2256,91,2326],0),
('connector',[40,43,410,1560],0)
]
manifest={}
for name,box,angle in items:
 p=r/'crops'/('scan010_'+name+'.jpg')
 assert not p.exists(),p
 crop=ImageOps.autocontrast(im.crop(box))
 if angle: crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 f=2600/max(crop.size)
 crop=crop.resize((round(crop.width*f),round(crop.height*f)),Image.Resampling.LANCZOS)
 crop.save(p,quality=94)
 manifest[name]={'box':box,'rotate_degrees':angle,'crop':'crops/'+p.name}
(r/'readers/scan010/crop_boxes.json').write_text(json.dumps(manifest,indent=2))
print(len(manifest),'crops created')
