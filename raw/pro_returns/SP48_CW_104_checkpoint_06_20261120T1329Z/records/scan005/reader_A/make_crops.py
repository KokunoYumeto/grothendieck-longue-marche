from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan005/reader_A')
src=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan005.jpg')
im=Image.open(src)
items=[
('01_chain_left',[55,88,438,190],2500,0,'First two chain indices and F alphabets'),
('02_top_mark',[1148,99,1220,160],2200,0,'Detached mark after top chain'),
('03_Dn_point',[901,292,1025,389],2200,0,'Cancelled D_n and separate dot'),
('04_difference',[151,523,1221,753],3200,0,'Arguments, parentheses and mark under first term'),
('05_small_maps',[1403,476,1911,748],2800,0,'Isolated stroke, s and t, cancelled existential note and small maps'),
('06_right_top',[1708,65,2335,264],3000,0,'C_i first two lines and cancelled words'),
('07_right_boundaries',[1914,344,2354,561],3000,0,'Donner, boundary indices and inserted words'),
('08_right_conditions',[1923,561,2354,790],3000,0,'Conditions deletion, boundary equalities and resp'),
('09_right_close',[1855,780,2349,1068],3000,0,'Deleted de and que, NB and last comparison'),
('10_level0',[29,811,243,927],2200,0,'E/Xi and first circled label'),
('11_pi0_surj',[1231,803,1561,950],2500,0,'Cancelled and live pi_0 surj notes'),
('12_level1',[27,1033,250,1178],2200,0,'E/Xi_1 and b-prime label'),
('13_epsilon',[1377,1054,1681,1188],2500,0,'Label and wavy arrow above f(u) to u-prime'),
('14_deleted_witness',[950,1168,1117,1249],2500,0,'Deleted witness below b-prime'),
('15_c_opening',[265,1247,1088,1398],3200,0,'Cancelled F_0 and first source index in c'),
('16_c_target',[1674,1223,2054,1368],2500,0,'Deleted f before u dash v'),
('17_c_pi',[2122,1222,2358,1365],2500,0,'Index of pi in c'),
('18_cprime_deletion',[1484,1433,1778,1546],2500,0,'Crossed word after u to v in c-prime'),
('19_lower_sketch',[1097,1537,1210,1660],2200,0,'Lower sketch label, endpoint marks and downward arrow'),
('20_pale_type',[182,210,394,806],2600,90,'Pale underlying vertical type, rotated for inspection')
]
out=[]
for ident,box,width,angle,purpose in items:
 c=im.crop(box)
 if angle: c=c.rotate(angle,expand=True)
 c=ImageOps.autocontrast(c,cutoff=0)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 p=root/'crops'/f'{ident}.png'
 c.save(p)
 out.append({'id':ident,'path':str(p),'source':str(src),'bbox':box,'rotation_degrees_counterclockwise':angle,'processing':['crop','rotate '+str(angle)+' degrees' if angle else 'no rotation','autocontrast cutoff 0','LANCZOS enlargement'],'sharpening':'none','output_size':list(c.size),'purpose':purpose,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Created',len(out),'crops; none viewed yet.')
