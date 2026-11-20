from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
R=Path(__file__).resolve().parents[1];src=R.parent/'source/SP40_CW_81_scans/J81-02_81_scan012.jpg'
plans=[
('01_top_first_oval',[130,30,460,392],'H first large oval: all chord, hatch and cap paths'),
('02_top_small_alternative',[468,12,552,112],'H first small oval alternative'),
('03_top_second_oval',[560,38,854,412],'H second large oval and lower detached gray point A21d/C-N04'),
('04_top_third_oval',[908,20,1210,393],'H third large oval, hatching and detached interior path pieces'),
('05_top_fourth_oval',[1220,24,1533,377],'H fourth large oval; C-D1 OK/Ok and nearby ou'),
('06_top_right_miniature',[1526,269,1644,416],'H second small alternative, inner bottom point A17'),
('07_left_lower_assembly',[15,546,418,931],'Two lower-left ovals, C-D3 crossing function, C-D2 ou, parenthetical miniatures and dash; complete assembly beyond reader crops'),
('08_central_lower_oval',[556,600,797,853],'H central oval with chord crossings and wedge hatching'),
('09_thick_tripod',[603,409,770,566],'H thick three-pronged graph, all ends'),
('10_upper_square',[968,410,1080,500],'H middle square outline, all corners'),
('11_stemmed_triangle',[1228,380,1356,500],'H small triangle with upper stem, all ends'),
('12_lower_diagonal_quadrilateral',[154,904,285,1010],'H lower quadrilateral with diagonal and projecting endpoints'),
('13_lower_spoked_triangle',[562,880,683,1026],'H lower triangle with three inner spokes and protruding ends'),
('14_upper_right_point',[1642,36,1677,79],'A21c / C-N03 isolated upper-right point'),
('15_mid_lower_point',[1060,1448,1097,1484],'A23b isolated lower field point, omitted by B/C'),
('16_lower_left_centre_point',[638,1616,679,1655],'A23a / C-N18 lower field point'),
('17_lower_left_point',[469,2034,506,2071],'A23f / C-N26 lower field point'),
('18_lowest_point',[666,2316,708,2356],'A23i / C-N30 low short slant')]
image=Image.open(src);manifest=[]
for name,box,purpose in plans:
 assert box[0]>=0 and box[1]>=0 and box[2]<=image.width and box[3]<=image.height,(name,image.size)
 im=ImageOps.autocontrast(image.crop(box));width=2800
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=75,threshold=3))
 dest=R/'crops/012'/f'{name}.png';im.save(dest)
 manifest.append({'path':str(dest.relative_to(R)),'bbox':box,'purpose':purpose,'source_image':str(src.relative_to(R.parent)),'processing':'PIL autocontrast, LANCZOS 2800px across, mild UnsharpMask','viewed':False})
(R/'crops/012/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print({'generated':len(manifest),'image_dimensions':image.size,'views':0})
