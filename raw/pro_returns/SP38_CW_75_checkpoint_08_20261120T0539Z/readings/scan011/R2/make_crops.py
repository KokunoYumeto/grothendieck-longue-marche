from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
root=Path('out/readings/scan011/R2')
source=Path('source/SP38_CW_75_scans/J75-02_75_scan011.jpg')
im=Image.open(source)
loci=[
 ('01_heading',[304,51,1190,133],0,'Resolve contracted grpe/grp and angular group alphabet; check compressed à against heading context.'),
 ('02_cancelled_aut',[292,140,906,255],0,'Read the crossed Aut expression and its two low subscript lines, including var/op and T/D.'),
 ('03_verb',[319,809,1371,889],0,'Distinguish avait/aurait/écrit/aura from the compressed verb after On.'),
 ('04_underbrace',[692,1073,1341,1220],0,'Distinguish possible composition circle from joined parenthesis and reproduce the slanted equal beneath the brace.'),
 ('05_cancelled_gamma',[521,1240,1272,1320],0,'Read the densely retraced first gamma in the canceled equation.'),
 ('06_live_subscript',[950,1361,1521,1443],0,'Distinguish t/b in the second q subscript of the live proof equation.'),
 ('07_nb',[1351,1621,1670,1750],0,'Resolve compressed si in the right-hand NB parenthesis.'),
 ('08_cancelled_gamma_relation',[470,1698,663,1765],0,'Read canceled Gamma and the following containment/membership trace.'),
 ('09_dihedral',[1157,1895,1621,2045],0,'Read diédral/diédhral and inspect the D alphabet in the margin note.'),
 ('10_bottom_correction',[1018,2088,1639,2183],0,'Read canceled d\'ordre n and its period beneath the raised inverse-generators replacement.'),
 ('11_detached_point',[316,1756,961,1891],0,'Decide whether the detached dark flick below and left of the upper Aff line is ink or a surface mark.')
]
manifest={'scan':'011','reader':'R2','whole_dimensions':[1685,2361],'halves':{'a':{'bbox':[0,0,1685,1260]},'b':{'bbox':[0,1100,1685,2361]}},'crops':[]}
for name,box,rot,reason in loci:
 c=im.crop(box)
 scale=max(2.5,2600/c.width)
 c=c.resize((round(c.width*scale),round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageOps.autocontrast(c,cutoff=0.35).filter(ImageFilter.UnsharpMask(radius=1.4,percent=140,threshold=3))
 if rot:c=c.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 p=root/(name+'.png');c.save(p)
 manifest['crops'].append({'id':name,'source':str(source),'bbox':box,'rotation_degrees':rot,'enhancement':'LANCZOS enlargement to 2600 px width or at least 2.5x; autocontrast cutoff .35%; unsharp mask radius 1.4, 140%, threshold 3','file':str(p.relative_to('out')),'reason':reason,'inspected':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(loci),'single-locus crops.')
