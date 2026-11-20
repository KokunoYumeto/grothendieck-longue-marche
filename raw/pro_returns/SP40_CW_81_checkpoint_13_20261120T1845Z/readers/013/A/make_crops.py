from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/013/A')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan013.jpg')
im=Image.open(source)
crops=[
('01_A_overwrite',(162,477,247,591),'C doubtful-readings row 1: pale A below dark A'),
('02_meditation',(102,789,377,857),'C doubtful-readings row 2: final word and ending'),
('03_cascades',(481,771,701,853),'C doubtful-readings row 3: overwritten opening C/Ca and live word'),
('04_cross_A',(165,875,248,953),'C doubtful-readings row 4: crossed subdivision A'),
('05_cross_B',(541,879,639,951),'C doubtful-readings row 5: crossed subdivision B'),
('06_cross_C',(928,879,1017,949),'C doubtful-readings row 6: crossed subdivision C'),
('07_cross_D',(1295,880,1386,943),'C doubtful-readings row 7: crossed subdivision D'),
('08_cross_E20',(1696,882,1789,949),'C doubtful-readings row 8: crossed subdivision E Notes 20'),
('09_cross_E23',(2107,885,2225,947),'C doubtful-readings row 9: crossed subdivision E Notes 23'),
('10_live_D',(1304,1026,1394,1107),'C doubtful-readings row 11: pale displaced (i) and dark subdivision'),
('11_plus',(428,1136,758,1251),'C doubtful-readings row 12: plus in subtitle'),
('12_live_A',(151,1042,221,1137),'C doubtful-readings row 13 sublocus A: pale lower (i)'),
('13_live_C',(928,1034,1005,1107),'C doubtful-readings row 13 sublocus C: offset parenthesis'),
('14_margin_arrows',(24,391,145,861),'Upper margin brace, bar, upward shaft, question mark and opposed arrows; exact geometry'),
('15_bent_arrows',(239,632,346,750),'Between A date and title: separate rules, bends and arrowheads'),
('16_top_cancellation',(67,229,343,319),'Cancelled A (1976/77): hatch geometry and surviving original glyphs'),
('17_reveil_initial',(486,679,563,761),'Initial R entry stroke: attachment of upper diagonal mark'),
('18_low_left_trace',(213,1389,255,1455),'Detached dark interrupted short stroke above first foot'),
('19_low_left_pale',(311,1578,360,1631),'Detached pale slanted stroke below first foot'),
('20_lower_right_marks',(1914,1280,2287,1384),'Detached dot below Fringale and short dash below last cell, with endpoint context'),
('21_edge_top',(2314,101,2365,441),'Right boundary top four partial stroke groups'),
('22_edge_middle',(2313,533,2365,666),'Right boundary stroke groups beside letters and dates'),
('23_edge_lower',(2310,949,2365,1222),'Right boundary stroke groups beside subdivisions and lower title'),
('24_edge_foot',(2303,1537,2365,1676),'Right boundary final stroke and archive numeral 12')]
manifest=[]
for name,bbox,purpose in crops:
 crop=im.crop(bbox)
 scale=min(8,2600/crop.width,3200/crop.height)
 crop=ImageOps.autocontrast(crop).resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 path=root/(name+'.png')
 crop.save(path)
 manifest.append({'path':path.name,'bbox':list(bbox),'coordinate_system':'original full scan, top-left origin, pixels; right/bottom exclusive','rotation':0,'purpose':purpose,'viewed':False})
(root/'crops.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'tight crops. No OCR or recognition used.')
