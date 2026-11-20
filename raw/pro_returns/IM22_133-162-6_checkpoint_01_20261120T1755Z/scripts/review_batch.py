"""Prepare concise source/decision comparisons and visual review sheets."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import sys,json
from review_and_commit import load,W
stems=sys.argv[1:]
tiles=[]
for stem in stems:
    packet,result,original,revised=load(stem)
    print('\nPAGE',stem)
    for src,r in zip(packet['rows'],result['rows']):
        print(json.dumps({'id':r['id'],'kind':src['kind'],'source_reading':src['as_the_page_reads'],'requested':src['should_read'],'evidence':src['evidence'],'decision':r['decision'],'find':r['find'],'replace':r['replace'],'ink':r['what_the_ink_shows'],'confidence':r['confidence'],'note':r.get('note','')},ensure_ascii=False))
        crop=r.get('crop')
        if crop and crop not in [x[0] for x in tiles]:
            im=Image.open(W/crop).convert('RGB')
            im.thumbnail((1500,1300))
            tile=Image.new('RGB',(1500,im.height+40),'white')
            ImageDraw.Draw(tile).text((10,8),stem+' '+r['id']+' '+r['decision'],fill='black',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20))
            tile.paste(im,(0,40));tiles.append((crop,tile))
out=W/'review_sheets';out.mkdir(exist_ok=True)
group=[];height=0;num=0
def save(group,num):
    canvas=Image.new('RGB',(1500,sum(t.height for t in group)),'white');y=0
    for t in group:canvas.paste(t,(0,y));y+=t.height
    p=out/('_'.join(stems[:2])+f'_{num}.jpg');canvas.save(p,quality=92);print('REVIEW_IMAGE',p)
for _,tile in tiles:
    if group and height+tile.height>2200:
        save(group,num);num+=1;group=[];height=0
    group.append(tile);height+=tile.height
if group:save(group,num)
