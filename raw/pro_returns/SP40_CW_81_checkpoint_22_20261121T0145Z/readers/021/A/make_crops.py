from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('out/readers/021/A')
im=Image.open('source/SP40_CW_81_scans/J81-03_81_scan021.jpg')
plan=[
 ('c01_opening',(880,45,1550,211),0,2700,['C021-R01'],'opening l\'on a and endpoint'),
 ('c02_first_display',(548,145,1530,278),0,3400,['C021-R02'],'complete paired intersections and i.e endpoint'),
 ('c03_parenthesis_prose',(280,278,1640,480),0,3600,['C021-R03'],'initial hook, accents and complete sentence including wrapped aura'),
 ('c04_first_brace_cancel',(1090,395,1485,645),0,2600,['C021-R04'],'whole first brace, K condition and cancelled Sigma group'),
 ('c05_or_comme',(410,738,1030,832),0,2700,['C021-R05'],'Or comme on a, including retraced first letters'),
 ('c06_crossed_cup',(900,826,1240,989),0,2400,['C021-R14'],'cup complete crossing stroke, lower limit and following hatted Sigma'),
 ('c07_final_alpha',(1120,1082,1290,1195),0,1900,['C021-R15'],'right-hand Sigma minus with complete low alpha group'),
 ('c08_margin_leadin',(1325,1100,1438,1210),0,1700,['C021-R06'],'small j.e./i.e. lead-in complete'),
 ('c09_margin_diagram',(1435,948,1667,1285),-90,2700,['C021-R07','C021-R08'],'all five rows, both braces and transverse labels, rotated clockwise'),
 ('c10_signifi',(1005,1197,1275,1310),0,2200,['C021-R09'],'complete signifi/signifie word with descender and endpoint'),
 ('c11_exclusion',(600,1309,965,1427),0,2600,[],'both signed Sigmas and crossed inclusion'),
 ('c12_cancel_live_verb',(395,1388,1000,1555),0,3000,['C021-R10','C021-R11'],'qui, cancelled verb and complete live verb including g descender'),
 ('c13_pi_ring',(285,1830,700,1940),0,2600,['C021-R12'],'V de Pi_I with ring and following comma'),
 ('c14_bottom_conditions',(440,2150,1667,2354),0,3600,['C021-R13'],'entire two condition rows, V predecessor, dot, closing brace, lower physical edge'),
 ('c15_precedent_line',(285,2048,1575,2255),0,3500,[],'complete preceding prose including both accents, underline, dash and wrapped on a')
]
manifest=[]
for name,box,rotation,width,rows,purpose in plan:
 c=im.crop(box)
 if rotation: c=c.rotate(rotation,expand=True)
 c=ImageOps.autocontrast(c)
 height=round(c.height*width/c.width)
 c=c.resize((width,height), Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
 filename=name+'.png'; c.save(root/filename)
 manifest.append({'path':filename,'source':'source/SP40_CW_81_scans/J81-03_81_scan021.jpg','bbox':list(box),'coordinate_system':'full scan top-left pixel origin','rotation_degrees_PIL':rotation,'output_size':[width,height],'purpose':purpose,'C_source_rows':rows,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(root/'image_audit.json').write_text(json.dumps({'start_utc':'2026-11-20 22:05:25 UTC','source_dimensions':{'whole':[1685,2362],'a':[1685,1261],'b':[1685,1261]},'source_views':[{'image':'whole','sequence':1,'purpose':'layout','delivered':True,'views':1},{'image':'a','sequence':2,'purpose':'complete line-by-line upper reading','delivered':True,'views':1},{'image':'b','sequence':3,'purpose':'complete line-by-line lower reading','delivered':True,'views':1}],'half_coordinate_map':{'a':'full x=x_a, y=y_a','b':'full x=x_b, y=y_b+1101','derivation':'lower half offset from actual full height 2362 minus half height 1261; task-necessary image-coordinate arithmetic only'},'crops':[],'failed_unseen_deliveries':[],'retries':[],'processing_events':['Read actual dimensions with PIL. Crop bounds selected visually from supplied halves. PIL crop, autocontrast, clockwise rotation for c09, aspect-preserving LANCZOS resize and unsharp mask. These are image preparation, with no pixel-difference comparison, mathematical check, OCR, compilation or rendering.'],'text_delivery_history':[{'attempt':'initial batched notation output','status':'tool aggregate text truncation; first portion of notation not fully delivered','recovery':'notation re-read as lines 1–70 and71–140 before any source image'}]},ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'one-pass planned crops; no crops viewed yet.')
