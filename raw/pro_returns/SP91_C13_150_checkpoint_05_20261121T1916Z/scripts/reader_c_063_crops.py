from pathlib import Path
from PIL import Image, ImageOps
import json, os

root=Path(__file__).resolve().parents[1]
im=Image.open(root.parent/'input/SP91_C13_150_scans/150_scan063.jpg')
items=[
('p01_number',[23,35,99,104],'Author number 27',0),
('p02_cancelled_opening',[371,49,1512,157],'Cancelled opening: c), tuple, est l’ens/l’une des éléments de',0),
('p03_cancelled_formula',[274,168,1653,291],'Entire formula line of cancelled opening, including trailing les',0),
('p04_cancelled_tail',[282,302,550,363],'Short last line within opening cancellation',0),
('p05_a_opening',[419,373,1367,461],'a) Pour tt, l’ens punctuation and Sigma lower segment',0),
('p06_a_est_tot',[1389,332,1663,458],'Cancelled (fini) est and interlinear est tot raised t',0),
('p07_a_cancelled_map',[260,483,603,576],'Cancelled equivalence/preimage expression, complete delimiters',0),
('p08_b_opening',[435,557,1663,647],'b) Si Sigma(1) est le graphe de la relation; superscript',0),
('p09_b_maps',[268,648,1663,763],'x<y and complete pair of maps with source superscript and shafts',0),
('p10_b_crossed_gap',[270,758,1147,852],'source et but, crossing before l’application',0),
('p11_b_propre',[266,862,846,965],'immer-sion, cancelled bordante, underlined propre',0),
('p12_b_preimage',[906,838,1662,945],'Whole parenthetical preimage expression and its delimiters',0),
('p13_c_opening',[432,1016,1665,1145],'c) tuple and Sigma lower-segment/preimage expression',0),
('p14_c_first_insertions',[267,1126,1185,1259],'First c) revisions: la famille, live des/les, overwritten germes, en x',0),
('p15_c_bordants',[1198,1093,1515,1212],'Cancelled bordants, inserted de Sigma and attachment',0),
('p16_c_germes',[261,1224,1147,1357],'images par b des, inserted germes and whole germ tuple',0),
('p17_c_family',[1174,1187,1658,1332],'Live est; inserted une famille and transversale; cancelled transversaux',0),
('p18_d_first_map',[449,1356,1656,1477],'First d) map, overwritten map label and M0603 target superscript',0),
('p19_d_second_map',[832,1416,1399,1485],'Second d) map, bordante and M0604 target superscript',0),
('p20_cancelled_diag',[408,1441,634,1535],'Cancelled words beneath d), possible la diag',0),
('p21_upper_margin',[23,1433,424,1851],'Entire slanted upper margin note, M0605',-30),
('p22_case1_map',[994,1435,1663,1610],'Case 1 map and fibrant with inserted (propre)',0),
('p23_case2_border',[1018,1696,1667,1794],'Case 2 terminal b(Sigma(1)) expression',0),
('p24_case3_heading',[350,1818,1621,1923],'Case 3 heading and whole first map',0),
('p25_case3_propre',[529,1898,1608,2041],'Case 3 fibrant, insertion propre and following fibres phrase',0),
('p26_case3_bords',[529,2022,1618,2127],'fibré des bords and Sigma(2) superscript',0),
('p27_case3_morphism',[529,2082,1616,2212],'Whole morphism, arrow/label and cancelled avec with inserted donné',0),
('p28_final_tuple',[527,2198,1275,2321],'Final element mapping: all comparison signs, arrow ends and terminal point',0),
('p29_lower_margin',[33,1954,431,2352],'Entire lower slanted margin note and its case numbers',-25),
('p30_foliation',[32,2306,88,2350],'Other-hand foliation 62',0),
('p31_case2_opening',[345,1620,1668,1716],'Case 2 opening, ordinal and extra stroke within initial Sigma',0),
('p32_immer_end',[1462,754,1674,829],'Written immer- ending at the upper-right end of b) line 8',0),
]
out=[]
for name,box,purpose,angle in items:
    q=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if angle:
        q=q.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    q=q.resize((2400,round(q.height*2400/q.width)),Image.Resampling.LANCZOS)
    filename='crops/150_scan063_'+name+'.png'
    q.save(root/filename)
    out.append({'file':filename,'box':box,'purpose':purpose,'rotation_degrees':angle})
dest=root/'scripts/reader_c_063_crop_manifest.json'
tmp=dest.with_name(dest.name+'.tmp')
with tmp.open('w') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write('\n')
    f.flush()
    os.fsync(f.fileno())
os.replace(tmp,dest)
print('Original size:', im.size)
print('Saved',len(out),'crops.')
