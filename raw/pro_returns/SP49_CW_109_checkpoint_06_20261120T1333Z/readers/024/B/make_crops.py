from pathlib import Path
import json
import subprocess
import sys

root = Path('/workspace/scratch/6d55c8c3e5a7')
dest = root / 'work/readers/024/B'
source = root / 'source/SP49_CW_109_scans'
items = [
 ('01','a',[25,40,180,115],'p191: read the faint page number, C doubt 191.'),
 ('02','a',[882,126,1246,187],'p191 continuation: determine whether the period C gives after again is present.'),
 ('03','a',[277,420,412,518],'p193 l5: read the crossed word and distinguish opening quote state from word cancellation.'),
 ('04','a',[18,493,215,573],'p194 left edge: read the cancelled marginal word, stating/starting, and its physical placement.'),
 ('05','a',[955,490,1110,567],'p194 reference to line -11: determine whether a point follows l.'),
 ('06','a',[25,610,169,705],'p196: independently read the pale final page-number digit, 196/191.'),
 ('07','a',[595,588,1095,719],'p196/p197 boundary: read apperent/apparent and determine the inserted p197 placement and following comma.'),
 ('08','a',[660,724,843,819],'p200: inspect opening and closing quote strokes surrounding the first explanatory it\'s.'),
 ('09','a',[1279,735,1440,815],'p200: inspect opening and closing quote strokes around it is.'),
 ('10','a',[1273,925,1525,1014],'p202 l17: distinguish single/double opening quotation before wouldn\'t.'),
 ('11','a',[925,1120,1201,1211],'p205: inspect the point and short stroke between is and a, plus nearby wether opener.'),
 ('12','a',[418,1179,641,1261],'p206 l20: inspect the crossed remnant after the numeral and its deletion state.'),
 ('13','b',[280,159,597,236],'p207 first quotation: count the low points between one and data.'),
 ('14','b',[899,157,1257,244],'p207 replacement quotation: independently count low points before datum.'),
 ('15','b',[532,340,668,415],'p209 second reference: decide whether a minus exists before 7 or belongs to the numeral.'),
 ('16','b',[664,402,838,486],'p210: determine identity of the raised cluster before I suggest.'),
 ('17','b',[1449,413,1530,479],'p210 right margin: inspect the two isolated marks not represented by C.'),
 ('18','b',[195,590,499,682],'p216 cancelled entry: inspect cancellation and opening-quote state near line -10 and that.'),
 ('19','b',[648,590,862,684],'p216 cancelled entry: independently inspect question mark, closing-quote count and cancellation extent.'),
 ('20','b',[1263,676,1453,752],'p216 live question: determine identity/count of the short strokes between the functor quotation and it.'),
 ('21','b',[302,843,447,926],'p219 l6: inspect the putative overwritten t in its and quotation strokes.'),
 ('22','b',[51,979,170,1043],'p224 reference: read the earlier numeral under the first 2 of 224.'),
 ('23','b',[544,965,879,1080],'p224 first functor: inspect j/J case, its A subscript, Cat, target hat and the low detached mark below the arrow.'),
 ('24','b',[902,977,1083,1090],'p224 second functor occurrence: independently inspect j/J and the overwritten argument B/X.'),
 ('25','b',[1283,977,1518,1088],'p224 Hom argument: inspect slash, comma, old argument under X, and delimiters at the vertical rule.'),
 ('26','b',[274,1022,685,1130],'p224 crowded note: read each insertion, cancelled word, j/J with B subscript, and numerator in x to B/x.'),
 ('27','b',[687,1117,1030,1194],'p224 final line: determine punctuation following l.20 and twice before l.21.'),
 ('28','b',[1603,402,1653,680],'Far-right edge: distinguish the faint vertical trace from an intentional ink rule.'),
]
records = []
for ident,half,box,question in items:
 records.append({'id':ident,'source':str(source/f'H109-02_109_scan024_{half}.jpg'),'bbox':box,'question_after_half':question,'crop':f'crops/{ident}.jpg','status':'not yet inspected'})
dest.mkdir(parents=True,exist_ok=True)
(dest/'unresolved_after_halves.json').write_text(json.dumps({'whole_viewed_once':True,'each_half_viewed_once':True,'loci':records},indent=2)+'\n')
for item in records:
 subprocess.run([sys.executable,str(root/'work/scripts/crop.py'),item['source'],str(dest/item['crop']),*[str(v) for v in item['bbox']],'--reason',item['question_after_half']],check=True)
