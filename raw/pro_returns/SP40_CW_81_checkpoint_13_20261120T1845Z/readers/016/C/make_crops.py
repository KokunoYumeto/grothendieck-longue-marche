from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/016/C'
source=root/'source/SP40_CW_81_scans/J81-02_81_scan016.jpg'
items=[
 ('c01_subscript.png',[680,65,963,167],'Opening union: predecessor under the live subscript 1.'),
 ('c02_old_verb.png',[954,75,1230,161],'Opening verb cluster: predecessor and live est or H serait.'),
 ('c03_right_insertions.png',[1032,91,1685,277],'Opening connexe, both raised insertions, complete visible guide runs and clipped right edge.'),
 ('c04_egale_cluster.png',[399,263,877,378],'After donc: struck predecessor, égal/égale endpoint, à/colon.'),
 ('c05_donc.png',[1076,276,1282,373],'Connective preceding the final opening inclusion.'),
 ('c06_cqfd.png',[228,365,418,531],'Opening conclusion abbreviation including full long descenders.'),
 ('c07_first_sigma.png',[506,586,802,690],'Overwritten first Sigma in first partition, with X and following join.'),
 ('c08_centre_sigma.png',[925,822,1218,1002],'Central overwritten Sigma12 and local overlapping brace endpoints.'),
 ('c09_dans.png',[255,1193,478,1321],'Overwritten initial of Dans with its endpoint.'),
 ('c10_ouverts.png',[1355,1212,1685,1318],'Right edge of sont ouverts, endpoint punctuation.'),
 ('c11_bottom_predecessors.png',[1018,2006,1463,2121],'Car paragraph: overwritten Sigma12 and E1, full overbar and comma.'),
 ('c12_lower_insertion.png',[286,2104,1065,2225],'Raised en/on conclurait/considérant and complete cancelled alors expression with strike geometry.'),
 ('c13_lower_joins.png',[486,2223,1090,2327],'Two overdrawn joins inside final long closure bar, with complete bar and adjacent terms.'),
 ('c14_right_bracket.png',[1403,2200,1685,2346],'Final right bracket, terminal closure index, and all visible returns at source boundary.'),
 ('c15_lower_annotation.png',[1090,2228,1405,2362],'Underbrace annotation below Sigma2 closure and endpoint along the bottom page edge.'),
 ('c16_footer.png',[281,2294,809,2362],'Full visible footer ce qui n\'est pas and endpoint punctuation.'),
 ('c17_detached_points.png',[1598,1702,1645,1764],'Two small detached points in right blank margin adjacent to third closure row.')
]
im=Image.open(source)
manifest=[]
for name,bbox,purpose in items:
    part=im.crop(tuple(bbox))
    part=ImageOps.autocontrast(part)
    width=2600
    part=part.resize((width,round(part.height*width/part.width)),Image.Resampling.LANCZOS)
    part=part.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
    part.save(out/name)
    manifest.append({'path':name,'bbox':bbox,'rotation':0,'purpose':purpose})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'created':len(manifest),'files':[m['path'] for m in manifest]}))
