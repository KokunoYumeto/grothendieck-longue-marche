from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
base=Path('out/readers/021/B')
src=Path('source/SP40_CW_81_scans/J81-03_81_scan021.jpg')
im=Image.open(src)
specs=[
 ('crop01_opening',(870,50,1575,203),['C021-R01'],'Opening wording and endpoint; full ascenders and the descending que retained'),
 ('crop02_ie',(1060,160,1540,275),['C021-R02'],'First i.e and both adjoining formula endpoints'),
 ('crop03_parenthesis',(270,270,820,445),['C021-R03'],'Initial hook, ce, qui and next word; full descending qui'),
 ('crop04_brace_cancel',(1080,380,1510,650),['C021-R04'],'Whole right brace, K condition and cancelled lower indexed glyph'),
 ('crop05_comme',(410,730,1030,835),['C021-R05'],'Or and complete comme on a; assess retracing and cancellation state'),
 ('crop06_margin',(1320,935,1685,1305),['C021-R06','C021-R07','C021-R08'],'Complete five-row margin diagram, both braces, sideways labels and lead-in'),
 ('crop07_signifi',(735,1185,1285,1320),['C021-R09'],'Membership context and complete signifi ending with descender'),
 ('crop08_conclusion',(275,1398,1320,1555),['C021-R10','C021-R11'],'Complete ce qui, cancelled predecessor, live signifie, aussi que and full descenders'),
 ('crop09_pi',(280,1825,1205,1935),['C021-R12'],'V de Pi ring and adjoining son expression'),
 ('crop10_old_v',(1270,2150,1680,2322),['C021-R13'],'Complete bottom i.e., overwritten E predecessor, dotted V, relation and closing brace'),
 ('crop11_cross_cup',(975,815,1260,1000),['C021-R14'],'Whole central cup and crossed upper stroke with complete lower index and Sigma'),
 ('crop12_low_alpha',(1060,1075,1300,1190),['C021-R15'],'Complete final Sigma, minus and low alpha group in middle equality'),
 ('crop13_bottom',(440,2160,1270,2362),[],'Whole bottom left brace, first condition and second line through X setminus Sigma alpha; inspect all surviving lower-edge strokes'),
 ('crop14_precedent',(710,2035,1025,2190),[],'Complete précédent with both raised accent positions and full p descender'),
 ('crop15_exclusion',(595,1290,985,1415),[],'Complete noninclusion formula including separate head run on right Sigma and indices')
]
manifest=[]
for name,box,rows,purpose in specs:
 cut=im.crop(box)
 width=3000
 height=round(cut.height*width/cut.width)
 cut=cut.resize((width,height),Image.Resampling.LANCZOS)
 cut=ImageOps.autocontrast(cut)
 cut=cut.filter(ImageFilter.UnsharpMask(radius=1.3,percent=120,threshold=3))
 rel=name+'.png'; cut.save(base/rel)
 manifest.append({'path':rel,'source':str(src),'bbox':list(box),'coordinates':'original full scan; x right, y down; top-left (0,0)','rotation':0,'processing':'PIL LANCZOS to width3000, autocontrast, UnsharpMask(radius1.3,percent120,threshold3)','output_size':[width,height],'purpose':purpose,'C_source_rows':rows,'viewed':False,'attempts':[]})
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
log=json.loads((base/'processing_log.json').read_text())
for row in log['images']: row['viewed']=True; row['successful_deliveries']=1
log['whole_and_halves_view_order']=['full','a','b']
log['half_coordinate_map']={'a':{'origin_full':[0,0]},'b':{'origin_full':[0,1101]},'basis':'Read dimensions full1685x2362 and halves1685x1261; b starts at full-height minus half-height =2362-1261=1101. This task-necessary coordinate subtraction is an administrative mapping, not a mathematical-manuscript check.'}
log['failed_unseen_image_deliveries']=[]
(base/'processing_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
print('Created15 distinct local crops; none yet viewed. All source full/a/b successfully viewed once.')
