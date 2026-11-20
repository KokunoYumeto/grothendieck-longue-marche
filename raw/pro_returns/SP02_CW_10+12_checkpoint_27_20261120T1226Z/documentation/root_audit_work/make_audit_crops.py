"""Render root-authored audit recipes.

Order: crop -> flip -> grayscale -> autocontrast -> contrast -> rotation ->
scale -> thumbnail.  The existing autocontrast-before-rotation order is retained.
Optional grayscale=True converts to L; optional contrast is a Pillow contrast
factor (1 is neutral).  Missing flags preserve the previous rendering behavior.
"""
from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json,argparse
p=argparse.ArgumentParser();p.add_argument('key');p.add_argument('label');p.add_argument('--extras');a=p.parse_args()
r=json.loads(Path('SP02_CW_10+12/documentation/page_records',a.key+'.json').read_text())
out=Path('work/audit_view'+a.label);out.mkdir(exist_ok=True)
recipes=[]
for old in r['crops']:
 if old['id'].startswith('audit-'):continue
 x=dict(old);x['id']='audit-'+old['id'];x['scale']=max(8,x.get('scale',1));recipes.append(x)
if a.extras:recipes+=json.loads(Path(a.extras).read_text())
for x in recipes:
 src=Path(x['source'])
 if src.parts[0]!='source':src=Path('source')/src
 im=Image.open(src).crop(x['box'])
 if x.get('flip')=='vertical':im=ImageOps.flip(im)
 elif x.get('flip')=='horizontal':im=ImageOps.mirror(im)
 if x.get('grayscale',False):im=im.convert('L')
 if x.get('autocontrast') is not None:im=ImageOps.autocontrast(im,cutoff=x['autocontrast'])
 if x.get('contrast') is not None:im=ImageEnhance.Contrast(im).enhance(x['contrast'])
 if x.get('rotation'):im=im.rotate(x['rotation'],expand=True)
 im=im.resize((round(im.width*x['scale']),round(im.height*x['scale'])),Image.Resampling.LANCZOS);im.thumbnail((2000,1500));im.save(out/(x['id']+'.png'))
Path('work/audit'+a.label+'_crops.json').write_text(json.dumps(recipes,ensure_ascii=False,indent=2))
print(json.dumps({'count':len(recipes),'directory':str(out),'ids':[x['id'] for x in recipes]}))
