from audit import *
k='120_scan005'
replace_text(k,[(r'alors pour $\forall$ ens fini $I$',r'alors pour tt ens fini $I$')])
revise_change(k,'finite-set quantifier and abbreviation',final='tt ens fini I',scan_shows='Two separate upright t stems with lower return strokes and a cross-stroke precede ens; they do not meet in the pointed lower vertex of the nearby universal quantifiers. ens has no point.',diff_C='yes',crop='120_scan005 (559,1565,715,1669)')
add_changes(k,[
 R('emphasis on un','underlined un','un','underlined un','A separate horizontal line lies immediately beneath un; the following n is separate.','other',crop='120_scan005 (251,482,571,582)'),
 R('item 4 label','circled 4','(4)','circled 4','A closed oval surrounds the numeral.','other'),
 R('reference after satisfait à','circled 3','(3)','circled 3','A drawn curved enclosure surrounds 3.','other'),
 R('item 5 label','circled 5','(5)','circled 5','A closed oval surrounds the numeral.','other')
])
add_certainty(k,[
 ('cancelled opening words',r'\unsure{On a}','On a','On and a remain on the baseline below the crossing stroke.','120_scan005 (270,300,1020,390)','medium'),
 ('cancelled NB',r'\unsure{NB}','NB','The two capital forms remain above the long cancellation.','120_scan005 (270,300,1020,390)','medium'),
 ('cancelled opening continuation',r'\unsure{Si on pose}','Si on pose','Initial S/i, low on and long descending p survive the strike.','120_scan005 (270,300,1020,390)','medium'),
 ('cancelled M before M1',r'\unsure{M}','M','The two high stems and connecting middle remain visible.','page','high'),
 ('cancelled M before the family equality',r'\unsure{M}','M','The high double-stemmed form is crossed but recognizable.','page','high'),
 ('cancelled existence sign',r'\unsure{\exists}',r'\exists','Three leftward bars join a right vertical stroke.','120_scan005 (410,780,1115,1018)','high')
])
finish(k,'Reread all text, formulas, cancellations, insertions and the crowded right margin. Corrected the first-pass reading of the sign before ens fini I from a quantifier to the written abbreviation tt; the new crop distinguishes its two separate stems from the pointed quantifiers elsewhere on this leaf. A separate new crop confirmed the underlined un and the following n. Logged H’s omitted underline and its parenthetical rendering of three circled numerals. The a/x mismatch, {x}∈R^n, inserted I≠∅ and vertical inclusion sign remain as written.',habits='Scan 005: before ens fini I the two upright stems belong to tt, not ∀. The latter is separately drawn with joined lower legs in the formulas and after aussi pour. The distinction holds here; it must be checked at each later occurrence rather than applied to every short mark before a noun.',notation=[('tt / ∀ on scan 005','tt before ens fini I has two separate stems; the formula quantifiers have joined, pointed lower legs.')],abbreviations=[('tt','tout')])
