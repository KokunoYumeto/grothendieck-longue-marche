from PIL import Image, ImageOps, ImageFilter
import json
from pathlib import Path
root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
src = Image.open(root/'packets/145_scan027/page.jpg')
plan = [
 ('01_header_extension_margin',[270,26,1644,286],'Header 12; complete opening extension formula, both ornate S signs, Z/2Z and the note engendré par tau'),
 ('02_fundamental_group',[268,244,1645,415],'Complete fundamental-group display, three pi/Pi letters, base point, U underbrace'),
 ('03_conjugaison_strike',[274,397,1648,516],'Main opening prose line and struck au dessus des'),
 ('04_eventuelles_fixed_points',[270,505,1644,801],'Inserted parenthesis, fixed-point list and X indices, connexes des ens. d’invariants'),
 ('05_cancelled_rho',[268,811,780,924],'Whole invariant list beginning with struck rho before tau'),
 ('06_sont_savoir',[810,780,1632,969],'Inserted sont and savoir phi(S3), their placement and the undotted rho'),
 ('07_stabilizer_relevement',[272,890,1644,1184],'P and Pbar punctuation; complete six-element stabilizer list; inserted à P and following phi(S3)'),
 ('08_entre_eux',[273,1137,1562,1304],'Whole pi-conjugués phrase and inserted entre eux'),
 ('09_conj_elemt',[275,1294,1630,1408],'Pbar punctuation; struck conj.; first élémt abbreviation'),
 ('10_qui_soit_elemt',[278,1390,1648,1627],'Struck qui, live qui soit, au dessus, second élémt and following complete element list'),
 ('11_prendre_cancelled_formula',[275,1623,1648,1853],'End of cet élément; On peut donc prendre and struck sigma0,tau'),
 ('12_produits_cancelled_tau',[267,1846,1645,2075],'Complete sigma/epsilon/tau lists, overwritten les, struck tau and final rho/rho2 continuation dots'),
 ('13_singular_corrections',[264,2050,1649,2262],'Le/Les, inserted seul, pt/pts corrections and complete last-paragraph numeric formulas'),
 ('14_footer_last_line',[28,2240,1654,2344],'Last line par sigma0 et tau and handwritten footer 26')
]
manifest=[]
for stem, box, places in plan:
    crop=ImageOps.autocontrast(src.crop(box))
    w=2500
    crop=crop.resize((w,round(crop.height*w/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.0,percent=115,threshold=3))
    rel='crops/145_scan027_'+stem+'.png'
    crop.save(root/'edition'/rel)
    manifest.append({'crop':rel,'box':box,'places':places})
(root/'edition/crops/145_scan027_crop_meta.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(root/'edition/crops/145_scan027_crop_boxes.json').write_text(json.dumps({x['crop']:x['box'] for x in manifest},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
