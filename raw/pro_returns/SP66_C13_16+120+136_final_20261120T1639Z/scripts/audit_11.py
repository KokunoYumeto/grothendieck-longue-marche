from audit import *
k='120_scan011'
replace_text(k,[(r'(f_{\alpha i}\,{}_{i\in I}',r'(f_{\alpha i})_{i\in I}')])
add_changes(k,[
 R('NB family indexing parenthesis','no closing parenthesis before the index','(f_alpha i) indexed by i in I','(f_alpha i) indexed by i in I','A tall closing stroke separates the family term from the lower i∈I index.','omission','yes','no',conf='medium',crop='120_scan011 (510,1955,1468,2118)'),
 R('NB end of systems display',')',',',')','A tall curved closing parenthesis, not a comma, follows R and the lower modérée annotation.','other',crop='120_scan011 (510,1955,1468,2118)'),
 R('pair of functions: left enclosure','two unbraced rows','cases brace','two unbraced rows','No brace or left enclosure is drawn beside the two function rows.','text not on the page')
])
finish(k,'Reread the whole page, including all subscripts, both versions of the function pair and the cancelled phrases. A new crop of the NB systems display restores the closing parenthesis before the family index; the separate terminal closing parenthesis is retained, even though that leaves the written grouping unconventional. Confirmed the tiny headed connector to R in this display, and the distinct headless connectors in the upper pair. Logged H’s added cases brace. No normalization of the I/A exponents or the cancelled remnants.')
