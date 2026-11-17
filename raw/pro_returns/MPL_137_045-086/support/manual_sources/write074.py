import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{74}
% archive foliation: 73
Il y a donc un complexe de De Rham-Sullivan \deleted{en} \inserted{\unsure{à la clef,}} Car. $0$.'''
e=[('text','top two lines','Il y a donc un complexe de De Rham-Sullivan'),('deletion','second line','en'),('insertion','above second line','à la clef')]
save(74,text,e)
