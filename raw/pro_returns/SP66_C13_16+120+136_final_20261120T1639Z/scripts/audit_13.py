from audit import *
k='120_scan013'
replace_text(k,[(r'et $Z_2\hookrightarrow X_2$}',r'et $Z_2\mathrel{\lhook\joinrel\relbar}X_2$}')])
revise_change(k,'last cancelled sentence',final='Appliquons ceci: Z1 hook-arrow X1 et Z2 hook-shaft X2',scan_shows='Tall initial A and p descenders in Appliquons; the first map has an upper hook over a dark rightward arrow. The second map has a hooked tail and a plain shaft; its headlessness is separately recorded in the second audit.')
add_changes(k,[
 R('second map in cancelled last sentence',r'Z_2\hookrightarrow X_2',r'Z_2\subset X_2',r'Z_2\mathrel{\lhook\joinrel\relbar}X_2','The upper tail curves back into a long lower shaft. The shaft ends with a single rounded stroke before X2, with no arrowhead.','drawing or diagram','yes','yes',crop='120_scan013 (1190,848,1550,959)'),
 R('M7 left enclosure','no brace','cases brace','no brace','There is blank space to the left of the M7 formulas; no grouping brace is drawn.','text not on the page')
])
finish(k,'Reread the entire page and all three marginal annotations. The existing rotated middle-note crop still does not settle the first word; supplém. remains tentative. A new crop of the second map in the cancelled final sentence confirms a hooked headless shaft, distinct from the headed first map. Logged the absent M7 brace that H supplies. The old letter under Z, cancelled initial function and terminal object of prolonge remain doubtful.')
