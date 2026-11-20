from PIL import Image
from pathlib import Path
import json
rows=[]
def a(i,b,s=24,rot=0,half='a'): rows.append(dict(id=i,source=f'SP02_CW_10+12_scans/B12-02_12_scan123_{half}.jpg',box=b,scale=s,rotation=rot))
a('titleword',[389,92,590,153],30);a('titlerest',[584,94,963,166],26);a('titleplace',[376,88,1013,228],15);a('titlerot',[389,92,963,166],24,1)
a('Un',[408,165,470,204],36);a('morphism',[1060,157,1257,207],30);a('schemaunderline',[1261,157,1467,218],25)
a('cancelclause1',[690,301,1289,351],24);a('cancelclause2',[1272,303,1573,352],26)
a('En',[1181,265,1592,310],27);a('Enrot',[1181,265,1592,310],27,2);a('Enplace',[1177,263,1636,353],20);a('La',[1573,297,1639,347],34)
a('ell1',[1120,367,1186,417],34);a('coeff1',[1438,372,1640,420],30);a('Cparen',[1003,440,1065,495],34);a('degparen',[1310,440,1348,488],36)
a('Uncas',[1374,442,1615,484],30);a('particulier',[241,521,768,563],28);a('Estart',[1354,405,1398,457],36)
a('Ce',[1390,413,1642,457],29);a('prouve',[247,471,602,514],28);a('modulo',[590,471,817,514],28);a('theoreme',[797,471,983,514],29);a('Lefschetz',[976,469,1148,520],32);a('pourla',[1153,470,1301,517],29);a('fibres',[1290,469,1645,521],27)
a('addsentence',[242,408,1648,560],14);a('prouverot',[247,471,1148,520],25,1);a('fibresrot',[1153,470,1645,521],25,1)
a('Sa',[241,505,294,547],36);a('kahler',[241,640,504,686],27);a('ait',[248,765,382,830],32);a('aitplace',[237,714,485,839],24)
a('entop',[306,143,434,184],32,half='b');a('comma',[766,359,802,402],36,half='b');a('Parexemple',[811,358,1118,400],30,half='b');a('etcancel',[1107,356,1202,402],34,half='b');a('Ce2',[1203,350,1262,398],34,half='b');a('redacteur',[1215,430,1419,469],30,half='b');a('rapporteur',[1211,398,1420,441],30,half='b');a('rapporteurrot',[1211,398,1420,441],30,1,half='b');a('rapporteurplace',[1160,393,1470,476],24,half='b');a('arith',[571,425,800,471],30,half='b');a('conjecturecancel',[539,495,805,539],30,half='b');a('somme',[1187,497,1303,536],34,half='b');a('Reimann',[380,642,629,687],30,half='b');a('frob',[992,710,1157,753],31,half='b');a('ell2',[241,776,285,829],36,half='b');a('restent',[440,780,942,827],27,half='b');a('coeff2',[548,849,790,900],29,half='b');a('tordus',[793,848,923,896],32,half='b');a('nombreux',[1345,894,1537,938],30,half='b');a('nombreuxrot',[1345,894,1537,938],30,1,half='b');a('nombreuxplace',[1270,890,1642,970],25,half='b');a('necessaires',[458,989,696,1030],30,half='b');a('indispensables',[476,966,713,1005],30,half='b');a('indispensablesrot',[476,966,713,1005],30,1,half='b');a('indispensablesplace',[445,959,781,1037],24,half='b');a('motifs',[1060,983,1494,1040],26,half='b');a('sera',[1566,984,1658,1037],36,half='b');a('archive',[32,1064,121,1123],30,half='b')
Path('work/view12_123').mkdir(exist_ok=True)
for x in rows:
 im=Image.open(Path('source')/x['source']).crop(x['box']); im=im.resize((im.width*x['scale'],im.height*x['scale']))
 if x['rotation']:im=im.rotate(x['rotation'],expand=True,fillcolor='white')
 im.save(f"work/crops/12-123-{x['id']}.png");im.thumbnail((1850,1500));im.save(f"work/view12_123/12-123-{x['id']}.png")
Path('work/crops12_123.json').write_text(json.dumps(rows,indent=2));print(len(rows))
