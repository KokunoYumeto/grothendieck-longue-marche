from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('out/readers/021/C')
src=Path('source/SP40_CW_81_scans/J81-03_81_scan021.jpg')
items=[
('crop01_opening',(885,45,1570,175),'C021-R01: complete opening lead-in after je dis que'),
('crop02_first_ie',(1040,65,1250,270),'C021-R02: first i.e and full attachment of que descender above'),
('crop03_ce_statement',(270,265,1635,480),'C021-R03 and full prose accents/ending through aura'),
('crop04_upper_brace',(1065,385,1510,650),'C021-R04; full brace, K line and cancelled Sigma group'),
('crop05_or_comme',(375,725,1050,840),'C021-R05; Or comme on a including endpoint'),
('crop06_central_union',(505,810,1265,1000),'C021-R14; complete central formula, cup cross-stroke and Sigma roof'),
('crop07_second_inclusion',(455,1005,1300,1210),'C021-R15; complete lower alpha index and roof plus neighbouring descenders'),
('crop08_margin',(1300,935,1678,1310),'C021-R06/R07/R08; complete marginal label/diagram group and braces'),
('crop09_signifi',(280,1195,1290,1310),'C021-R09; d\u2019autre part line and verb endpoint'),
('crop10_cancelled_impli',(540,1380,1030,1550),'C021-R10/R11; complete cancelled word and live signifie'),
('crop11_exclusion',(590,1305,1000,1415),'Full exclusion symbols including Sigma heads and right raised plus'),
('crop12_pi',(280,1815,685,1945),'C021-R12; V de Pi ring group'),
('crop13_bottom_brace',(420,2135,1680,2362),'C021-R13; full bottom brace/formulas and cancelled predecessor including physical lower page edge'),
('crop14_upper_traces',(795,390,955,475),'Two pale runs above first main union, discrete shape or surface trace unresolved'),
('crop15_left_trace',(65,825,690,975),'Detached short slash at left with neighbouring E_i line context'),
('crop16_lower_trace',(160,2035,440,2165),'Small left-side point beside corollary continuation with rule and du context'),
('crop17_corollary_words',(285,2040,1595,2240),'Corollary prose accent/endpoints and on a; separate from bottom correction target')
]
im=Image.open(src)
manifest=[]
for stem,bbox,purpose in items:
    cut=im.crop(bbox)
    target_width=2600
    target_height=round(cut.height*target_width/cut.width)
    cut=ImageOps.autocontrast(cut.resize((target_width,target_height),Image.Resampling.LANCZOS))
    cut=cut.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    target=base/(stem+'.png'); cut.save(target)
    manifest.append({'path':target.name,'source':str(src),'bbox':list(bbox),'coordinate_origin':'full scan top-left; x right, y down','rotation':0,'output_size':[target_width,target_height],'purpose':purpose,'viewed':False})
(base/'crop_manifest.json').write_text(json.dumps({'scan':'021','reader':'C','original_size':[1685,2362],'half_sizes':{'a':[1685,1261],'b':[1685,1261]},'lower_half_origin':[0,1101],'mapping_note':'Lower-half vertical origin derived only as original height 2362 minus half height 1261; no alignment or pixel-difference computation. Crops use original full-scan coordinates. Enlargement uses proportional height only.','crops':manifest},ensure_ascii=False,indent=2)+'\n')
print('Prepared',len(manifest),'distinct target crops; none viewed yet.')
