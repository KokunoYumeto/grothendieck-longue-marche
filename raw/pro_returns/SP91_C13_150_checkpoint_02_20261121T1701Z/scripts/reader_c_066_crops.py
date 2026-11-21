from pathlib import Path
from PIL import Image, ImageOps
import json, os
root=Path(__file__).resolve().parents[1]
im=Image.open(root.parent/'input/SP91_C13_150_scans/150_scan066.jpg')
items=[
('p01_d_initial',[290,43,479,130],'Initial d) and cancelled short group before Les'),
('p02_d_hook',[652,50,1050,155],'Entire opening hooked map and written subscripts'),
('p03_d_donc',[648,160,1008,248],'Cancelled les and following donc/dans les'),
('p04_d_indices',[1350,132,1657,268],'Inserted indices/indexés and cancelled pour j<i'),
('p05_d_revision',[332,238,791,390],'Crossed tels que and Sigma, interlinear par l’ens/l’on'),
('p06_definition',[812,234,1648,354],'Entire I lower-segment definition, definition label, braces and comma'),
('p07_b_parenthesis',[1090,368,1559,476],'par b and closing-parenthesis count before sont'),
('p08_mutuellement',[1300,693,1635,791],'Written length and raised ending of mutuellement'),
('p09_e_first_map',[378,916,786,1026],'e) first whole labelled map and indices'),
('p10_trans_ending',[1461,866,1648,936],'Written trans- ending at right of e) first line'),
('p11_e_morphismes',[826,921,1575,1018],'versal de/des morphismes and bordants strike state'),
('p12_b_indices',[861,996,1306,1090],'Whole b-labelled map, ik/ki and M0609'),
('p13_coproduct1',[541,1189,991,1339],'Entire first coproduct display and absence/presence of punctuation'),
('p14_coproduct2',[538,1334,1095,1559],'Entire second coproduct display, raised sign, indexing and summand'),
('p15_induits_map',[337,1547,1574,1657],'et s,b source-to-target expression and induits par les'),
('p16_graph_map',[814,1739,1472,1870],'Whole (s,b) graph map, source exponent, shaft and product sign'),
('p17_image',[859,1853,1145,1985],'Cancelled graphe and interlinear image'),
('p18_stricte_avec',[742,1983,1152,2089],'stricte/strict and avec, above lower insertion'),
('p19_lower_b',[1232,1961,1650,2047],'Whole lower underlined-b map and source exponent'),
('p20_immersion_et',[171,2101,796,2209],'Inserted immersion, propre, cancelled/live et and que'),
('p21_application_phi',[824,2037,1524,2199],'Inserted continue évidente and whole phi expression M0610'),
('p22_strict',[343,2169,1044,2257],'Written strict raised-t form and croissante'),
('p23_tt',[1208,2156,1669,2264],'pour tt/tout or quantifier-shaped sign, x in Sigma and comma'),
('p24_induced',[853,2197,1669,2319],'Entire induced phi map, index relation and final est'),
('p25_injective_enfin',[340,2285,967,2355],'Bottom injective state and enfin before que'),
('p26_tott',[983,2274,1605,2355],'Final Sigma lower segment, est, tot raised-t and ordonné'),
('p27_foliation',[22,2296,86,2355],'Pale other-hand foliation 65'),
]
out=[]
for name,box,purpose in items:
    q=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    q=q.resize((2400,round(q.height*2400/q.width)),Image.Resampling.LANCZOS)
    rel='crops/150_scan066_'+name+'.png'
    dest=root/rel
    tmp=dest.with_name(dest.name+'.tmp')
    q.save(tmp,format='PNG')
    os.replace(tmp,dest)
    out.append({'file':rel,'box':box,'purpose':purpose,'rotation_degrees':0})
dest=root/'scripts/reader_c_066_crop_manifest.json'
tmp=dest.with_name(dest.name+'.tmp')
with tmp.open('w') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write('\n'); f.flush(); os.fsync(f.fileno())
os.replace(tmp,dest)
print({'original_size':im.size,'crops':len(out)})
