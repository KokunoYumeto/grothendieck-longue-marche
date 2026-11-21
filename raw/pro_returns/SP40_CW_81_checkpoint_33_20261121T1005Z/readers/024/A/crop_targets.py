from pathlib import Path
from PIL import Image, ImageOps
import json
out=Path('out/readers/024/A')
source=Path('source/SP40_CW_81_scans/J81-03_81_scan024.jpg')
targets=[
('01_opening_word',(278,78,598,195),2600,'opening Considérons accent and complete word'),
('02_pi',(1021,86,1169,207),2600,'Pi upper loop, I subscript, full head'),
('03_union_indices',(1320,88,1648,227),2600,'opening union and E indices with both upper marks and comma'),
('04_second_considerons',(942,299,1442,406),2600,'second Considérons accent and complete word with adjoining la'),
('05_struck_on',(703,317,943,410),2600,'complete cancelled On a/On cluster and full endpoints'),
('06_replacement',(299,393,1151,566),2600,'entire Relation R entre S et I replacement and old underlined Lemme forall clause with crossing strokes'),
('07_predecessor',(610,538,950,648),2600,'overdrawn predecessor with complete (s,i) in R continuation'),
('08_tuple',(1327,637,1630,800),2600,'complete tuple and overlapping R/closer state'),
('09_relation_point',(814,650,1213,804),2600,'relation ending and possible point with full adjoining fait descender'),
('10_rule_head',(248,753,340,930),1200,'marginal rule upper hook and separate pale left trace'),
('11_ens_des',(310,887,979,1008),2600,'complete ens des/de sommets wording and comma'),
('12_aretes',(308,999,685,1110),2600,'arêtes accent, endpoint period and closing curve'),
('13_ce_graphe',(676,950,1518,1095),2600,'complete deleted Cette relation and Le/Ce graphe with upper detached return'),
('14_le_quon',(426,1191,1098,1360),2600,'le/Le and complete qu’on a phrase including q descender and reduced a'),
('15_existe',(1122,1302,1490,1427),2600,'Il plus complete deleted existe/ex and live y a'),
('16_soient',(381,1745,592,1858),2600,'complete Soient/Soit initial word'),
('17_sigma_pair',(596,1734,825,1855),2600,'both signed Sigmas, complete heads and indices'),
('18_connexes',(940,1723,1557,1836),2600,'deux comp. connexes/conn. de complete phrase'),
('19_exactement',(305,1950,857,2078),2600,'a exactement/exactemt and underlined un, full word endpoints'),
('20_signed_containment',(924,1935,1586,2067),2600,'complete U signed subscript, contenu dans, Sigma signed superscript'),
('21_barred_u',(630,2071,977,2195),2600,'complete barred U signed subscript and intersection expression'),
('22_parenthetical',(1008,2044,1648,2297),2600,'full et de equals pour Sigma, qui/de, lower tel que formula and terminal closer/comma; all descenders retained'),
('23_definit',(337,2168,610,2304),2600,'complete définit with accents and long descender'),
('24_final_sigma',(734,2148,1010,2301),2600,'last U signed subscript subset Sigma with head, index and minus'),
('25_precise',(934,1815,1293,1952),2600,'complete précise en colon, including p descender and accent'),
('26_notees',(1148,201,1350,300),2600,'complete notées accent and letters')]
im=Image.open(source).convert('RGB')
records=[]
for name,bbox,width,purpose in targets:
 crop=im.crop(bbox)
 crop=ImageOps.autocontrast(crop)
 height=round(crop.height*width/crop.width)
 crop=crop.resize((width,height),Image.Resampling.LANCZOS)
 path=out/(name+'.png');crop.save(path)
 records.append({'path':path.name,'source':str(source),'bbox':list(bbox),'coordinate_system':'full scan, top-left origin, pixels','rotation':0,'width':width,'purpose':purpose})
(out/'crop_plan.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created 26 planned local crops; none displayed by this script.')
