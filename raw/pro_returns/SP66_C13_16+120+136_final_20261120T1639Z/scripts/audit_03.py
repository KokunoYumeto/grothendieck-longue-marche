from audit import *
k='120_scan003'
add_certainty(k,[
 ('cancelled title continuation',r'\unsure{et espaces}','et espaces','The rotated title shows et and the longer espaces under the strike.','120_scan003 (20,20,350,330); rotated −38°','medium'),
 ('cancelled line: barred m',r'\unsure{$\overline{\mathrm m}$}',r'$\overline{\mathrm m}$','The short overbar and low m match its two uncancelled occurrences on the same leaf.','120_scan003 (450,1590,1345,1745)','medium'),
 ('cancelled line: stand.',r'\unsure{stand.|dans}','stand.','An ascending t and short d survive the strike; the first alternative is retained.','120_scan003 (450,1590,1345,1745)','medium')
])
ds=readtsv('DOUBTS.tsv')
for r in ds:
 if r['page']==k and r['place']=='cancelled case-c phrase':r['reading']=r"\unsure{(``op. dégénérescence'')}"
rewrite_tsv('DOUBTS.tsv',ds)
finish(k,'Reread the whole leaf, all four axioms, slanted margin additions, the overwritten M2 letters, the enclosed marginal map and both pagination marks. A new audit crop at (1370,1024,1508,1119) checked the cancelled tout: its surviving low interior strokes support the full word, so it is not shortened to tt. The M_I membership sign, S_n notation and final injectif remain as written. No additional textual change; added outside-MARKS certainty records and corrected escaped quotation characters in a doubts-table cell.')
