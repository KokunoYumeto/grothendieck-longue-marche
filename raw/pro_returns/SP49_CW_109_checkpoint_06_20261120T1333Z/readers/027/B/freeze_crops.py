import json
from pathlib import Path
base=Path('work/readers/027/B')
a='source/SP49_CW_109_scans/H109-02_109_scan027_a.jpg'
b='source/SP49_CW_109_scans/H109-02_109_scan027_b.jpg'
items=[
('01',a,[125,66,470,145],'Faint opening page and line numerals; clipped/faded quotation end.'),
('02',a,[352,130,560,206],'Cancelled word before which, with/who.'),
('03',a,[1395,114,1586,224],'Final capital in image of A by A; possible prime versus quotation strokes.'),
('04',a,[919,250,1436,355],'Cancelled reference and quoted play no/not s, with quote-edge state.'),
('05',a,[360,322,605,395],'Closing quotation count after interpret.'),
('06',a,[470,379,676,450],'Cancelled cluster before also, l/it.'),
('07',a,[1075,394,1320,472],'Number and extent of category underline.'),
('08',a,[570,497,868,578],'Cancelled l-6 and lets/let\'s; buried apostrophe and reference.'),
('09',a,[350,571,661,640],'Opening quotation count at should not contraction on 313.'),
('10',a,[297,635,799,727],'Cancelled filtering and raised ending plus replacement line reference.'),
('11',a,[292,757,503,831],'Overwritten medial letters in Sentence.'),
('12',a,[925,831,1100,903],'Cancelled false start before in order to.'),
('13',a,[1205,962,1545,1035],'Number of low dots between situations and theory.'),
('14',a,[995,1007,1630,1107],'Cancelled first parenthesis line; certainly and as far as our placement, presumably.'),
('15',a,[261,1080,1146,1165],'Cancelled second parenthesis line and No/Now with terminal continuation strokes.'),
('16',b,[388,98,555,170],'Closing quotation count after its at l.17.'),
('17',b,[1306,105,1480,183],'Closing quotation count after compute.'),
('18',b,[754,227,1043,306],'Two cancelled clusters in and after quoted i(a) is a fragment.'),
('19',b,[332,288,450,361],'Opening quotation count before its at317.'),
('20',b,[366,538,451,620],'Cancelled ampersand before live ampersand at326.'),
('21',b,[524,525,694,644],'Raised & l-3 and descending insertion connector, exact placement.'),
('22',b,[980,618,1104,679],'Terminal mark after should it be.'),
('23',b,[1235,671,1414,747],'Deleted closing-quote group after is not contraction before there!.'),
('24',b,[433,802,624,876],'Cancelled would not contraction, apostrophe position and deletion extent.'),
('25',b,[1167,989,1520,1083],'Semisimplicial ending and punctuation, insertion connector.'),
('26',b,[1413,931,1685,1148],'Clipped raised l-5 word and right-hand slanted question; developing/enveloping, quote and certa/p doubts, note shape.'),
('27',b,[344,1109,584,1194],'Opening and closing quotation marks around b membership expression.'),
]
obj={'scan':27,'reader':'B','frozen_after':['whole viewed once','half a viewed once','half b viewed once'],'unresolved':[]}
for n,s,box,reason in items:
    obj['unresolved'].append({'id':n,'source':s,'bbox':box,'reason':reason,'crop':str(base/'crops'/f'{n}.jpg')})
(base/'unresolved_frozen.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(base/'views.json').write_text(json.dumps({'whole':'source/SP49_CW_109_scans/H109-02_109_scan027.jpg','half_a':a,'half_b':b,'whole_views':1,'half_a_views':1,'half_b_views':1,'procedure':'Whole view then each half once; unresolved list frozen before enhancement. No OCR or compilation.'},indent=2)+'\n')
