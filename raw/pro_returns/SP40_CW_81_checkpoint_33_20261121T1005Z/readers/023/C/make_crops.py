from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/023/C')
src=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan023.jpg')
plans=[
('01_opening_a',(230,150,835,302),0,'Opening line-break a/mark and complete following formula'),
('02_prouvons',(1090,65,1650,205),0,'Complete prouvons que l\'on wording'),
('03_first_union_sigma',(675,365,930,548),0,'First union whole-state C R14; hatted Sigma predecessor C R01; all head, roof, plus and index strokes'),
('04_donc_si',(1038,398,1440,524),0,'Whole cancelled donc si and endpoint before je, C R02 and H ill placeholder'),
('05_on_a',(900,540,1440,680),0,'Compressed on a en fait and discrete ochre trace above it'),
('06_margin',(24,638,590,980),-24,'Complete slanted note with cancelled word, parenthetical I/J, all descenders; adjoining ce qui'),
('07_prouvera',(570,765,1160,920),0,'Complete prouvera and l\'assertion; C R05 and H prouve'),
('08_sigma02',(835,670,1032,792),0,'Second union and S02 with head, body, alpha and raised plus'),
('09_sigma03',(480,1028,642,1154),0,'S03, all head/body/index/raised-sign strokes and final point'),
('10_revient_au',(760,1015,1215,1147),0,'Complete Cela revient au and final endpoint, C R06 and H résulte du'),
('11_sigma04',(620,1268,790,1390),0,'Lemma S04 head/body/index/raised-sign strokes'),
('12_tels',(1070,1168,1495,1413),0,'Complete cancelled tel que les with its descender; complete live tels que, C R07'),
('13_first_relation',(300,1370,790,1514),0,'First alpha relation beta plus second relation for context; complete beta descenders; C R15'),
('14_sigma05_06',(992,1370,1435,1505),0,'Both disjointness Sigmas with their local heads, alpha/beta indices, pluses, empty-set and point'),
('15_sigma07',(1235,1460,1455,1590),0,'Lemma antecedent union and complete S07'),
('16_conclusion_correction',(300,1570,937,1723),0,'Entire deleted E_i est contenu candidate and raised existential tel que; C R08, H dans un/comma/insertion'),
('17_sigma08',(1195,1573,1355,1685),0,'Lemma conclusion S08 and point'),
('18_provient_du',(1030,1655,1645,1800),0,'Complete live verb and final short word, C R09/R10, plus right detached trace'),
('19_prec',(895,1800,1288,1920),0,'Complete hyp. préc. sur wording and accent/abbreviation endpoint'),
('20_family',(1312,1783,1613,1910),0,'Whole corollary family, S09 head/body, upper alpha, lower i, outer alpha-in-K/I and comma, C R12'),
('21_rule_words',(245,1915,667,2150),0,'Complete lower left rule including runs/endpoints and adjoining la partition / et de'),
('22_pi',(675,1930,829,2055),0,'Complete Pi K with raised circle/zero, C R13'),
('23_sigma10',(1318,1900,1648,2015),0,'Complete partition S10, plus/index and following parenthesis alpha-in-K'),
('24_final_union_sigma',(923,1925,1220,2143),0,'Complete formée f descender, final union cross/run, S11 head/roof/index/plus and fullstop, C R16'),
('25_final_accents',(425,2130,1320,2252),0,'Whole Immédiat par récurrence with accent/ending strokes'),
('26_left_trace',(65,398,370,552),0,'Left detached dark trace with E_beta line context')
]
im=Image.open(src)
records=[]
for name,bbox,angle,purpose in plans:
    path=name+'.png'
    if (out/path).exists():
        width,height=Image.open(out/path).size
    else:
        crop=im.crop(bbox)
        crop=ImageOps.autocontrast(crop)
        if angle:
            crop=crop.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
        width=3000 if crop.width>=450 else 2400
        height=round(crop.height*width/crop.width)
        crop=crop.resize((width,height),Image.Resampling.LANCZOS)
        crop=crop.filter(ImageFilter.UnsharpMask(radius=1.0,percent=115,threshold=3))
        crop.save(out/path)
    records.append({'path':path,'bbox':list(bbox),'coordinate_system':'original full scan; top-left origin; right/bottom exclusive','rotation':angle,'resampling':'LANCZOS','processing':'autocontrast; rotation BICUBIC when nonzero; unsharp radius 1 percent 115 threshold 3','output_dimensions':[width,height],'purpose':purpose})
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(records)} once-planned target crops.')
