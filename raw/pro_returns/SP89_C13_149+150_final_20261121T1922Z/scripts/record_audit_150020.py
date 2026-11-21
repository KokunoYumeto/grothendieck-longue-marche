from audit_record import AuditRecord
A=AuditRecord('150_scan020');S=A.c
ret={
'B01':'The top bar and lower bowl identify 5, and the separate closing parenthesis continues below it. The second reading differs only in the numbering wrapper.',
'B07':'The additional narrow old group before Y has its own hooked top and long lower curved return, partly crossed by the live Y. A doubtful old closing brace remains preferable to silently dropping the group. The following cancelled f is independently uncertain. The final connector has a dark end mass but no securely separated head arms, so the existing arrow/headless alternative remains appropriate.',
'B10':'The opening has a tall looped S body followed by the small i stroke and dot. Capital Si is sufficiently supported. The T has one roof, cônique has its detached accent, and strict is below that word within the raised clause. The long bracket beneath the clause crosses only the upper P stem and does not cancel Pour que T.',
'B12':'The tall f and detached stop are separate from the next compact upstroke. A low initial entry permits compressed et, but its e is not individually resolved. The existing et/t doubt is retained. The dot above X and the terminal bord, without ant, remain visible.',
'B13':'The independent dark oblique mark above X is separate from the star at upper right; dotted X-star remains preferred with the existing interpretation alternative. The short cancelled word has both a separate low underline and diagonal crossing strokes. Those strikes hide its middle letters, so strict remains doubtful.',
'B14':'There is one long horizontal roof above the retraced stem and its curved return. No second independent roof supplies an overbar. The second reading has treated the sole roof as an additional bar; the literal T is retained without asserting a recoverable prior letter.',
'B17':'The thin lower-left number has a straight 1 with entry slant and a looped 9 with descending return. Both readings give 19; the margin wrapper records placement only.'}
chg={}
o=r'\deleted{\unsure{\}}}';n=r'\deleted{\unsure{\}|f|\varphi}}'
e='The narrow old group after the family index has a looped upper part, dark descending body and curved lower return, crossed locally. Its segmentation does not uniquely distinguish a closing brace from an f-like or phi-like old token. The preferred doubtful brace is retained, with the second reader’s alternatives recorded explicitly; no second certain token is supplied.'
A.replace(r'(X_i)_{i\in I}'+o,r'(X_i)_{i\in I}'+n);chg['B02']=(o,n,e)
A.change('P01',final=A.get('changes','id','P01')['final'].replace(o,n),evidence=e)
A.inventory('E03',first_words_or_objects=n)
A.update('doubts','place','P01 old delimiter',reading=n,alternatives='closing brace | f | phi-like old token',reason='The upper loop, long dark body and lower return are partly crossed; the old glyph cannot be segmented uniquely.')
A.update('deletion_insertion_review','text',o+' in first tuple',text=n+' in first tuple',scope_attachment='Old crossed group immediately after family index and before comma/T; preferred brace with f/phi alternatives; no other tuple symbol cancelled',evidence=e)
o='cônique';n=r'\unsure{cô}nique'
e='One live word body continues through nique, with its descending q, and the separate upper arch supplies the accent. The initial c/o region is heavily overworked by an additional tall stroke. The preferred cô opening is retained but is now marked uncertain locally; no earlier whole word is reconstructed.'
A.replace('$T$ voisinage cônique de',r'$T$ voisinage \unsure{cô}nique de');chg['B03']=(o,n,e)
A.change('P02',final=n,evidence=e);A.inventory('E04',first_words_or_objects=n+'; opening retraced, earlier token unrecoverable')
A.update('doubts','place','P02 overwritten opening of cônique',reading=n,reason='The separate accent and final nique body survive clearly; the c/o opening merges with a tall older stroke. Preferred letters remain cô, without a recovered earlier word.')
A.update('deletion_insertion_review','text','cônique',text=n,evidence=e)
o=r'\unsure{Y|X_i}';n=r'\unsure{X_i|Y}'
e='The long diagonal runs from upper right to lower left, while the other dark diagonal continues into the lower-right mass. The visible four-limbed crossing favors X over a simple Y fork. Small low returns allow the old X_i candidate, although the index and overworking remain unresolved; X_i is now preferred, Y secondary. No two independent Y states are established.'
A.replace(o,n);chg['B04']=(o,n,e)
A.change('P03',final='$'+n+'$',evidence=e,kind='misread symbol or index',against_c=True,against_h=True,error_category='1')
A.update('decisions','id','M0352',reading=n,evidence=e)
A.inventory('E05',first_words_or_objects=n)
A.update('doubts','place','P03 base glyph',reading=n,alternatives='X_i | Y; index and chronology of lower-right overwork unresolved',reason=e)
A.update('deletion_insertion_review','text',o,text=n,evidence=e)
A.update('diff_coverage','row',4,disposition='P03/M0352: X_i now preferred on the four-limbed crossing, Y retained as an alternative; H’s two-Y state inference is not adopted.')
o=r'soit \uline{strictement} \deleted{compatible avec les}';n=r'soit \uline{\unsure{strictement|strict}} \deleted{compatible \unsure{avec les}}'
e='The underlined word begins str/ict and has a long joined rightward continuation, favoring strictement; the compressed continuation does not securely expose every letter, so strict is retained as an alternative. In the cancelled phrase the compatible ascenders and descender remain readable, but the following low avec les bodies merge with their strikes. Their preferred wording is retained under a local doubt. The raised transversal aux and the following live X_i are unchanged.'
A.replace(o,n);chg['B11']=(o,n,e)
A.change('P09b',final=A.get('changes','id','P09b')['final'].replace(r'\uline{strictement}',r'\uline{\unsure{strictement|strict}}'),evidence='The Si leader crosses only the upper P stem, above the live Pour que T bodies. T has one roof. The following underlined word remains live; strictement is preferred, with strict retained because its long compressed ending is not fully separated.',confidence='medium')
A.change('P10',final=A.get('changes','id','P10')['final'].replace(r'\deleted{compatible avec les}',r'\deleted{compatible \unsure{avec les}}'),evidence=e,confidence='medium')
A.inventory('E16',first_words_or_objects=r'Pour que T soit \uline{\unsure{strictement|strict}}')
A.inventory('E17',first_words_or_objects=r'\deleted{compatible \unsure{avec les}}')
A.doubt('P10 underlined live word',r'\uline{\unsure{strictement|strict}}','strictement | strict','Long compressed continuation after the initial strict-like strokes favors the longer form but does not expose every final letter.','medium')
A.doubt('P10 cancelled low words',r'\deleted{compatible \unsure{avec les}}','compatible avec les','The low bodies after compatible are partly hidden by their separate cancellation strokes.','medium')
A.update('deletion_insertion_review','text',r'soit \uline{strictement}',text=r'soit \uline{\unsure{strictement|strict}}',scope_attachment='Both words live; uncertain strictement/strict alone underlined',evidence=e)
A.update('deletion_insertion_review','text',r'\deleted{compatible avec les}\inserted{transversal aux}',text=r'\deleted{compatible \unsure{avec les}}\inserted{transversal aux}',evidence=e)
o='\\begin{tikzcd}\n\\dot X\\arrow[r]&Y,\\\\\n(\\dot X_i)\\arrow[u,phantom,"\\cup" description]&\n\\end{tikzcd}'
n='\\begin{tikzcd}[column sep=small]\n\\dot X&\\unsure{\\longrightarrow|\\mathrel{\\relbar\\joinrel\\relbar}}&Y,\\\\\n(\\dot X_i)\\arrow[u,phantom,"\\cup" description]&&\n\\end{tikzcd}'
e='Counted twice: dot X, Y followed by a comma, and parenthesized dot X_i below the first object; one horizontal connector and one separate upward-open cup, without a vertical shaft. The right endpoint of the connector is a small filled termination with a short downward return; independent arrowhead arms cannot be securely separated. Arrow remains preferred but the headless alternative is now explicit in the connector cell. The existing et/t doubt in the preceding abbreviation is retained.'
A.replace(o,n);chg['B15']=(o,n,e)
A.change('P14b',final=A.get('changes','id','P14b')['final'].replace(o,n),evidence=e,confidence='medium')
A.inventory('E22',first_words_or_objects=r'dot X to Y with doubtful arrowhead, comma after Y, parenthesized dot X_i beneath dot X with vertical cup')
A.doubt('P14 diagram connector',r'\unsure{\longrightarrow|\mathrel{\relbar\joinrel\relbar}}','right arrow | unheaded horizontal connector','The tiny filled right termination does not resolve two independent arrowhead arms.','medium')
A.update('diff_coverage','row',19,disposition='P14b: both witnesses give a right connector; the terminal arrowhead is now locally doubtful, with a headless alternative.')
for c in A.comp:
 b=c['box']
 if c['token_equal']:continue
 if b in chg:
  o,n,e=chg[b];assert o in S[b]['first'],(b,o);A.decide(b,e,S[b]['first'].replace(o,n))
 else:A.decide(b,ret[b])
A.append('notes',id='N99',text='Independent audit: root personally inspected all twelve nonidentical boxes. Five box readings were revised: the first old tuple token gained f/phi alternatives, the cô opening gained local uncertainty, X_i became the preferred overworked base candidate, the live/cancelled wording gained local doubts, and the diagram arrowhead gained a headless alternative. Only the base candidate order changes the preferred lexical/symbol reading; prior first/second files remain fixed. The three-object diagram and its vertical cup were counted twice. These are visual reading decisions, not additional mathematical proof checks.')
A.save()
