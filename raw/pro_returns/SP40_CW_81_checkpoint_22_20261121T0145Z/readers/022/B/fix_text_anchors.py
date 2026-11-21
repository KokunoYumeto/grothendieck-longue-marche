from pathlib import Path
p=Path('out/readers/022/B/build_reading.py')
s=p.read_text()
replacements={
'T03':[
"text(258,233,'pour','deleted',ident='T03')",
"text(432,233,'prouver','deleted',ident='T03b')",
"text(713,224,'que','deleted',ident='T03c')"],
'T04':[
r"text(884,222,r'(si',size=r'\normalsize',ident='T04')",
r"text(1015,218,r'$V=X\setminus$',size=r'\normalsize',ident='T04b')"],
'T18':[
"text(263,852,'Comme',state='deleted',ident='T18')",
r"text(618,850,r'$V\subset$',state='deleted',size=r'\large',ident='T18b')"],
'T22':[
"text(275,983,'prouvons',state='deleted',ident='T22')",
'''text(576,960,"l'inclusion",state='deleted',ident='T22b')''',
"text(936,953,'inverse',state='deleted',ident='T22c')"],
'T24':[
"text(286,1211,'Soit',state='deleted',ident='T24')",
r"text(485,1205,r'$x\in$',state='deleted',size=r'\large',ident='T24b')"],
'T26':[
"text(869,1198,'prouvons',state='deleted',ident='T26')",
r"text(1164,1193,r'$x\in\overline V\cap E_\alpha$',state='deleted',size=r'\large',ident='T26b')",
"text(1462,1192,'i.e.',state='deleted',ident='T26c')"],
'T27':[
r"text(260,1304,r'$x\in\overline V$,',state='deleted',size=r'\large',ident='T27')",
"text(493,1303,'soit',state='deleted',ident='T27b')",
r"text(657,1292,r'$W$',state='deleted',size=r'\large',ident='T27c')",
"text(713,1292,'un',state='deleted',ident='T27d')",
"text(820,1293,'voisinage',state='deleted',ident='T27e')",
"text(1066,1285,'de',state='deleted',ident='T27f')",
r"text(1156,1285,r'$x$,',state='deleted',size=r'\large',ident='T27g')",
'''text(1250,1277,"montrons qu'il",state='deleted',ident='T27h')'''],
'T31':[
"text(950,1370,'peut',state='deleted',ident='T31')",
"text(1090,1371,'considérer',state='deleted',ident='T31b')",
"text(1460,1385,'cette',state='deleted',ident='T31c')"],
'T34':[
"text(566,1486,'comme',state='deleted',ident='T34')",
r"text(891,1484,r'\unsure{égalité|egalité}',state='deleted',ident='T34b')",
"text(1146,1477,'dans',state='deleted',ident='T34c')"],
'T39':[
"text(306,1734,'dans',state='deleted',ident='T39')",
"text(463,1722,'lequel',state='deleted',ident='T39b')",
"text(747,1712,'on a',state='deleted',ident='T39c')",
"text(947,1705,'deux',state='deleted',ident='T39d')",
"text(1095,1708,'parties',state='deleted',ident='T39e')",
"text(1295,1706,'fermées',state='deleted',ident='T39f')"],
'T41':[
"text(717,1792,'Or',ident='T41')",
"text(824,1782,'dans',ident='T41b')",
r"text(1002,1785,r'$X$',size=r'\large',ident='T41c')",
"text(1058,1785,'on a',ident='T41d')",
"text(1287,1784,'les',ident='T41e')",
"text(1403,1782,'deux',ident='T41f')"]}
rows=[];changed=[]
for line in s.splitlines():
 found=None
 for ident in replacements:
  if line.startswith('text(') and line.endswith("ident='"+ident+"')"):
   found=ident;break
 if found:rows+=replacements[found];changed.append(found)
 else:rows.append(line)
assert sorted(changed)==sorted(replacements),(changed,replacements.keys())
p.write_text('\n'.join(rows)+'\n')
print('Separated observed text anchors for '+', '.join(changed))
