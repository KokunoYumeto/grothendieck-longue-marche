from audit import *
k='120_scan009'
replace_text(k,[(r'e\!\!\prime\prime|e',r"e''|e"),(r'{R^0},R)\ne\varnothing$} dans des',r'{R^0},R)\ne\varnothing$)} dans des')])
for name,ff in [('CHANGE_LEDGER.tsv',['final']),('DOUBTS.tsv',['reading'])]:
 rows=readtsv(name)
 for r in rows:
  if r['page']==k:
   for f in ff:r[f]=r[f].replace(r'e\!\!\prime\prime',r"e''")
 rewrite_tsv(name,rows)
add_changes(k,[R('closing parenthesis after cancelled Hom nonemptiness','no closing parenthesis','no matching closing parenthesis at this position',')','A tall standalone closing curve follows the crossed nonemptiness formula; it is crossed by the same deletion line.','omission','yes','yes',crop='120_scan009 (252,165,1410,446)')])
add_certainty(k,[
 ('deleted alors',r'\unsure{alors}','alors','The a/l start and low ors remain under the horizontal stroke.','120_scan009 (1040,43,1629,170)','medium'),
 ('deleted category letter in top line',r'\unsure{$\mathcal E$}',r'$\mathcal E$','The two curved lobes match the live category E on the same line.','120_scan009 (1040,43,1629,170)','medium'),
 ('deleted dans at top',r'\unsure{dans}','dans','A tall d and low ans remain visible through the strike.','120_scan009 (1040,43,1629,170)','medium'),
 ('deleted existe un',r'\unsure{existe un}','existe un','Initial e/x, the tall t and separate low un remain visible.','120_scan009 (252,165,1410,446)','medium'),
 ('deleted de l’objet',r"\unsure{de l'objet}","de l'objet",'The d, apostrophe, tall l/b and descending j remain legible.','120_scan009 (252,165,1410,446)','medium'),
 ('vertical identification under R^0',r"\unsure{\shortparallel|''}",r'\shortparallel','Two short parallel strokes stand vertically between R^0 and {e}.','120_scan009 (252,165,1410,446)','high')
])
finish(k,'Reread the whole page and re-inspected the existing crop of the crossed Hom formulas. Restored the standalone closing parenthesis following the nonemptiness formula. Kept the uncertain double-prime reading but used ordinary superscript-prime TeX syntax for it; this is an encoding repair, not an additional reading change. Checked the insertion type de, the singular fini after diagrammes, the word vide, and the inserted certain and une. Added certainty-only records for readable cancelled words.')
