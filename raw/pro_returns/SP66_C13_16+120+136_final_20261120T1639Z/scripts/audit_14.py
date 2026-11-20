from audit import *
k='120_scan014'
replace_text(k,[(r'{Z_i}\hookrightarrow R^{A_i}',r'{Z_i}\mathrel{\lhook\joinrel\relbar}R^{A_i}')])
add_changes(k,[R('quotient embedding before on a',r'X_i/Z_i\hookrightarrow R^{A_i}',r'X_i/Z_i\hookrightarrow R^{A_i}',r'X_i/Z_i\mathrel{\lhook\joinrel\relbar}R^{A_i}','The small curved hook at the left joins a bare horizontal shaft before R; its right end has no arrowhead.','misread symbol or index','yes','yes')])
finish(k,'Reread all prose and counted the objects, edges and decorations of the three diagrams again. The equality =ui(Z) is attached directly beneath the quotient denominator, as encoded. Corrected the quotient embedding itself to a hooked headless shaft. Confirmed the old R under the final Z, the duplicated A2 in the cancelled draft, and the direction and headlessness of the live diagram edges. No normalization of the unmatched curved stroke after Soit.')
