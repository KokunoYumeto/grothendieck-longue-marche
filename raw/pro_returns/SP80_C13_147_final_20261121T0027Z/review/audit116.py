from edition.scripts.root_audit import Audit

a=Audit(116)
stroke=r'\figure{\begin{tikzpicture}[x=.5cm,y=.5cm,line width=.35pt]\draw (0,9.2)..controls (.1,7.6) and (-.1,4)..(.03,2.7)..controls (.04,2.5) and (.12,2.35)..(.35,2.25);\draw (.03,2.7)..controls (.12,1.8) and (.45,.2)..(.85,0);\end{tikzpicture}}'
a.change('B03',stroke+r'\quad\unsure{(}','The long marginal stroke is nearly straight through its upper portion, forks into a short rightward hook low down, and continues to a lower right-curving extension. A normal left brace would invent a central left cusp. The detached open-right arc at the top is retained separately as a doubtful opening parenthesis.')
a.replace(r'$\left\{\rule{0pt}{14em}\right.$',stroke)
a.add_row('B03','long marginal grouping stroke',r'\left\{\rule{0pt}{14em}\right.','',stroke,'high','drawing or diagram','Drawings and diagrams',True,True)
a.report['inventory'][1]['first_words_or_objects']='(174) and long grouping stroke with short low hook and extended lower tail'
f=a.comparison['B04']['first'].replace(r"\deleted{\unsure{d'}}",r"\deleted{\unsure{p\leq d|d'}}")
a.change('B04',f,'The cancelled group has a left descending stem with a loop, a compact angled middle group, and a right tall d-like loop: p less-than-or-equal d is a better tentative reading than one d-prime. The crossing masks the middle strokes, so it is not resolved. In the live condition below, one high stroke belongs to the cancelled descender; only one separate prime follows d. Both sigma forms, def without accent, the equality, and the full formula were checked.')
a.replace(r"\deleted{\unsure{d'}}",r"\deleted{\unsure{p\leq d|d'}}")
a.update_row(2,'B04',final=r"\deleted{\unsure{p\leq d|d'}}",against_C=True)
a.doubt('cancelled coproduct index',r"\deleted{\unsure{p\leq d|d'}}",'The initial loop and descender, middle angle, and final upright favor the longer group; cancellation prevents resolving the candidate.','low',replace_place='cancelled coproduct index')
a.report['inventory'][4]['first_words_or_objects']=r"\unsure{p\leq d|d'}"
a.keep('B05','The stroke crosses but does not obliterate the entire phrase: the second word retains a long p descender, and the final d and prime are visible. The first word has the p opening, central tall d and high accent compatible with pondéré. It remains tentative rather than replaced by one illegible word.')
a.keep('B06','The figure has one filled left point, two solid outgoing arrows with full right heads, and a dotted upper-to-lower arrow with a clear head. Both encodings preserve these three directed edges; the slight gap at the lower shaft start is a pen placement, not a second labelled object.')
a.keep('B07','The added word has the tall medial d and final accented ending of pondéré, not produit. Its cue enters after source donnée); the other cue enters after the first P expression. et has no intervening s. The crossed E-like letter and small crossed superscript remain cancelled and doubtful; the lower superscript is a separate open circle. The live words faisceau, simpliciaux, and cardinal can be traced, including the final tall l of cardinal.')
a.keep('B08','The cancelled first tall loop is compatible with l and is followed by low e/s-like traces; a clean initial d bowl for de cannot be isolated. les remains tentative. The live au moins is separate and unstruck.')
a.keep('B09','The shaft has one small downward terminal turn but no separately visible two-arm head. The dash/arrow uncertainty remains; the source d,d-prime and target d-prime are clear.')
a.keep('B10','Both first-d positions have dense raised overtracing. Neither two clean prime strokes, a four-arm star, nor an intact xi can be isolated. The existing d/d-circle uncertainty therefore remains rather than being resolved to the blind candidates. The other primes, product base D_d-prime, and the single capped connector have been checked across the whole formula.')
a.change('B11',r'(la \unsure{flèche|flèches}','The short article contains one low return after the tall l, favoring la. After the h and low e of flèche, the extended terminal return could include a compressed s; the fresh crop does not justify the first pass’s certainty about the ending.')
a.replace('(la flèche composition)',r'(la \unsure{flèche|flèches} composition)')
a.update_row(16,'B11',final=r'(la \unsure{flèche|flèches} composition)',confidence='medium')
a.doubt('composition-map explanatory noun',r'\unsure{flèche|flèches}','The extended final return may contain a compressed s; singular remains first without using the number of maps to decide.','medium')
a.report['inventory'][19]['first_words_or_objects']=r"(la \unsure{flèche|flèches} composition), car il n'est pas clair"
a.keep('B12','The article and noun have the short endings favoring le morphisme, but their final low turns are compressed. The existing alternatives are retained; agreement with following sont does not decide their number.')
a.keep('B13','Both source and final target have the double-prime group. The long connector ends in the same small one-sided down-turn as the preceding maps, so the dash/arrow doubt is preserved.')
a.keep('B14','The opening word has an initial s, low o/n joins, and tall final t: sont. After the opening quotation strokes are two tall crossed t stems, not les. The later déterminées has its accented initial and compressed but continuous terminal sequence; the question mark and comma after mono are distinct.')
a.keep('B15','The word after Mais starts with f and a small i stroke and has a tall medial l before the low e/m/e/n/t ending. This favors finalement over forcément. sa source and son but, the closing quotation pair, and the punctuation at c). are visible.')
a.keep('B16','The lighter marginal number has two 1 forms followed by the open upper bend and lower bowl of 5. Its margin wrapper is already present in the page.')
a.note('Blind audit replaced the normalized long brace with its visible forked grouping stroke, broadened the cancelled coproduct-index reading to tentative p less-than-or-equal d, and marked the singular/plural ending of flèche as unresolved. The three reduced map connectors and two overwritten raised index clusters remain doubtful. The independent mathematical counterexample recorded for the closing claim is unchanged and was not used to normalize these signs.')
a.finish()
