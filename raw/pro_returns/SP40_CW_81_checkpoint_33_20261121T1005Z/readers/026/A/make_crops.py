from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json, hashlib, datetime
base=Path('out/readers/026/A')
source=Path('source/SP40_CW_81_scans/J81-03_81_scan026.jpg')
# Targets fixed after one whole layout view and one view of each supplied half.
plans=[
('01_title',(865,100,1415,215),0,'opening underlined noun: C décomposition / H disposition'),
('02_family',(560,265,805,360),0,'opening family complete Sigma, two alpha placements and terminal index sign, C026-R01'),
('03_hemispheres',(270,815,670,950),0,'initial h/cancellation state in hémisphères; H gives struck word'),
('04_inserted',(650,865,1140,1005),0,'complete raised equation, lower/upper overwritten indices, round raised sign, guide and struck group after connexes; C026-R02 parts a-c, R03, R15'),
('05_si_condition',(755,980,1475,1090),0,'following-si Sigma lower cancelled index and E relation, C026-R02 part d and R12'),
('06_connexe_correction',(540,1025,1140,1210),0,'X connexe et replacement, entire cancelled les Sigma connexes and long insertion/cancellation guide'),
('07_aussitot',(1405,1025,1665,1150),0,'entire crossed word after on conclut, C026-R04'),
('08_margin',(35,940,265,1390),-52,'entire oblique diagram including word, endpoints, cancelled upper label and E tail, C026-R05/R06'),
('09_closure_first',(450,1210,855,1340),0,'first closure Sigma alpha round sign and visible head/roof separation'),
('10_closure_equation',(1090,1140,1660,1285),0,'complete parenthetical equality, two closure roofs and unbarred right Sigma; endpoint comma'),
('11_et_sigma',(395,1330,565,1440),0,'complete Sigma after et with alpha round pair, local head shape'),
('12_car_sigma',(410,1435,615,1550),0,'car superscript including full first raised stroke and baseline comma, C026-R07'),
('13_lower_noun',(755,1510,1660,1640),0,'lower décompositions/dispositions noun and its accent'),
('14_pairs_correction',(90,1610,735,1780),0,'both binary pairs, second opener, entire struck distinctes and added de X with bent guide, C026-R08/R13'),
('15_non_adjective',(1130,1600,1650,1735),0,'complete underlined non adjective with final accent/ending, C026-R09'),
('16_distinctes_insertion',(265,1700,965,1875),0,'complete inserted elles sont distinctes et si, long guide, original si and on peut trouver attachment'),
('17_disjoint',(625,1885,1650,2045),0,'complete disjointness display and parenthesis, individual Sigma heads and raised signs'),
('18_alors',(285,2045,610,2150),0,'on a alors / on a donc'),
('19_first_inclusion',(630,2050,1090,2170),0,'complete first inclusion correction, cancelled nonempty pair and i.e., C026-R10/R14'),
('20_second_equality',(630,2150,1510,2255),0,'complete second row: explanatory label punctuation and individual Sigma heads, C026-R11'),
('21_bottom',(510,2230,1500,2350),0,'complete final definition, def accent and all indices, signs and endpoint')]
im=Image.open(source)
rows=[]
for name,bbox,rotation,purpose in plans:
 crop=ImageOps.autocontrast(im.crop(bbox).convert('RGB'))
 if rotation: crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 pre=crop.size; width=2800; height=round(pre[1]*width/pre[0]); crop=crop.resize((width,height),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=100,threshold=3))
 fn='crop_'+name+'.png'; crop.save(base/fn)
 rows.append({'id':name,'path':fn,'source':str(source),'bbox':list(bbox),'coordinate_space':'full scan; x right, y down; half-open PIL box','rotation_degrees_PIL_counterclockwise':rotation,'autocontrast':True,'rotation_resampling':'BICUBIC' if rotation else None,'after_rotation_size':list(pre),'output_size':[width,height],'resize':'LANCZOS','sharpen':{'filter':'UnsharpMask','radius':1.1,'percent':100,'threshold':3},'purpose':purpose,'sha256':hashlib.sha256((base/fn).read_bytes()).hexdigest()})
(base/'crop_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(base/'view_audit.json').write_text(json.dumps({'start_utc':'2026-11-21 07:37:04 UTC','source_dimensions':{'full':[1694,2370],'a':[1694,1265],'b':[1694,1265]},'half_coordinate_maps':{'a':{'full_x':'x','full_y':'y'},'b':{'full_x':'x','full_y':'y+1105','derivation':'2370-1265=1105; native lower-half extent'}},'image_events':[{'path':'source/SP40_CW_81_scans/J81-03_81_scan026.jpg','role':'whole layout','successful_displays':1,'failed_unseen_attempts':0},{'path':'source/SP40_CW_81_scans/J81-03_81_scan026_a.jpg','role':'upper-half complete line reading','successful_displays':1,'failed_unseen_attempts':0},{'path':'source/SP40_CW_81_scans/J81-03_81_scan026_b.jpg','role':'lower-half complete line reading','successful_displays':1,'failed_unseen_attempts':0}],'cropping_plan_fixed_before_deep_views':True,'crop_events':[]},ensure_ascii=False,indent=2)+'\n')
print('Created',len(rows),'planned tight crops; none viewed yet.')
