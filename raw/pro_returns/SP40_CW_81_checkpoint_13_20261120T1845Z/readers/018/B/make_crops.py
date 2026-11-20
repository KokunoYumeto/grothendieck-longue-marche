"""One planned enlargement for each unresolved scan018 locality. No OCR."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

ROOT = Path('/workspace/scratch/94548b74fbe0')
SOURCE = ROOT / 'source/SP40_CW_81_scans/J81-02_81_scan018.jpg'
DEST = ROOT / 'out/readers/018/B'
PLAN = [
    ('crop01_opening.png', [224,58,793,165], 2600, 'dernière, its accent, and adjoining cette/si'),
    ('crop02_recurrence.png', [440,165,1060,285], 2600, 'parenthetical par récurrence and endpoints'),
    ('crop03_ens.png', [373,280,810,373], 2400, 'l’ens and absence/presence of abbreviation point'),
    ('crop04_unique.png', [805,397,1490,613], 2800, 'l’une, raised (unique), full guide, de/des ces n'),
    ('crop05_upper_quote.png', [796,728,1380,861], 2600, 'upper (ou “composante”) including terminal letters/quotes'),
    ('crop06_considerons.png', [789,867,1460,1018], 2800, 'et considérons les, accent and ending'),
    ('crop07_lemma_pi.png', [1034,1140,1645,1275], 2800, 'lemma Pi ring, J and cancelled following index; comma and distincte'),
    ('crop08_dire.png', [1328,1368,1599,1475], 2400, 'colon and worked-over Dire'),
    ('crop09_insertions.png', [216,1437,1150,1606], 3200, 'qu’une/la and U-alpha de Pi additions, all adjoining words and guide endpoints'),
    ('crop10_corrected_Ei.png', [1155,1465,1614,1599], 2800, 'pas, overwritten E_i, separate upper stroke, i.e. est'),
    ('crop11_formula_choisi.png', [940,1689,1622,1846], 3000, 'signed Sigma-j, pi-zero expression, overwritten E_j and crossed choisi'),
    ('crop12_lower_quote.png', [221,1867,733,1995], 2800, 'quoted composant/e and complete final ticks'),
    ('crop13_live_est.png', [648,1843,1493,1990], 3000, 'de cette classe, crossed est and live following verb'),
    ('crop14_element_du.png', [243,1970,756,2101], 2800, 'l’élément du/de pi-zero with full word endings'),
    ('crop15_soit_guide.png', [251,2128,712,2286], 2800, 'raised (soit Sigma-i-minus), full guide, éléments de'),
    ('crop16_bottom_corrections.png', [244,2230,1125,2363], 3200, 'cas, deux/card I=2 correction, cancelled word and accent before fortiori; page edge included'),
    ('crop17_final.png', [1147,2242,1604,2363], 2800, 'final U subscript, inclusion, Sigma-i-minus, comma and OK punctuation'),
]

im = Image.open(SOURCE)
records=[]
for name, bbox, width, purpose in PLAN:
    crop = ImageOps.autocontrast(im.crop(tuple(bbox)))
    # The only dimension arithmetic is the same aspect-preserving display
    # enlargement as the supplied helper. No pixel comparison is performed.
    crop = crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    crop.save(DEST/name)
    records.append({'path':name,'bbox':bbox,'coordinate_space':'original full scan; top-left origin; right/bottom exclusive','rotation':0,'purpose':purpose,'output_size':list(crop.size),'viewed':False})
(DEST/'crop_manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(records, ensure_ascii=False, indent=2))
