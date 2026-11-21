from edition.scripts.root_audit import Audit

a=Audit(115)
a.keep('B01','The abbreviation has two upright t stems with separate lower returns crossed by a shared bar, not the two converging arms of a single universal quantifier.')
f=a.comparison['B02']['first'].replace(r'\unsure{ens}',r'\unsure{ens|en}')
a.change('B02',f,'The low initial loop is compatible with e rather than u; the cancellation obscures whether the terminal hook supplies s. Retain ens first, add en as an unresolved alternative. The separate raised t and low s after p remain visible.')
a.replace(r'\deleted{\unsure{ens}}',r'\deleted{\unsure{ens|en}}')
a.update_row(1,'B02',final=r'\deleted{\unsure{ens|en}}')
a.doubt('opening canceled group',r'\deleted{\unsure{ens|en}}','The terminal hook may be s or part of n under the strike; the initial loop favors e over u. Neither reading is resolved.','low',replace_place='opening canceled group')
a.report['inventory'][1]['first_words_or_objects']=r'\deleted{\unsure{ens|en}}'
a.keep('B03','The detached terminal low arch is the return of r; there is no further independent s after valeur. The preceding S is plain, unlike the ornate D on the next baseline.')
a.keep('B05','The ending of formé carries an accent and no following s. Both indices are compact crossed stars of this page; etc has no separate abbreviation point before its closing parenthesis.')
a.keep('B06','The last low return belongs to n in codimension; there is no additional letter before the paired elevated closing quotation strokes.')
a.keep('B07','The rotated derivative shows elle sort, des autres structures, and cf plus bas with three final points. The small descending terminal hook after structures supports the comma; there is no dark independent point after cf. The border crossing the line is not cancellation.',crop='crops/147_scan115_second_B07_view_rot_minus45.jpg')
a.keep('B08','The display has the single star below D, c above a fully headed rightward shaft, and the doubled upright N. The two readings differ only in their math wrappers.')
a.keep('B09','The first digit has a curved top and oblique foot: 271 remains the literal number. The coproduct index is d in the doubled-upright N, with D_d on the right; wrappers alone differ.')
a.keep('B10','Both compact crossed subscript forms agree with the stars in the neighboring formulas, rather than alpha. The lower pair d,d prime has no enclosing parentheses; N times N is written literally.')
a.keep('B11','The display number is 173. The small neighboring word at the upper edge is où, with its high accent; it is already transcribed on the preceding prose baseline, and is not an omitted i.e.')
a.keep('B12','The abbreviated im has a separate point and lacks the extra letters of image. The arrow label begins with a round sigma-like loop and ends with a tall b and bowl. The crossed star forms and the low source comma are retained; a final point follows the target product.')
a.keep('B13','The long stem projects well above and below the oval, supporting the written phi form. The inequality is the strict d prime greater than d; the formula has been read as a whole.')
a.keep('B14','Both occurrences of codim lack an abbreviation point; the inequality has the short lower bar of less-than-or-equal. The right-edge curved closure belongs to the parenthesis, with no semicolon. The difference is line arrangement and wrappers.')
a.keep('B15','The ending after the tall t is accented é followed by the elevated closing pair; there is no separate s. The source and target carry the same compact star forms as above. The terminal cancelled word remains only a tentative induit because the strike masks its interior.')
a.keep('B16','The right coproduct index has a looped d, the small membership sign, and the doubled/zigzag N. The heavy trailing overtrace does not isolate another readable letter; its uncertainty is already recorded. The full factorisation agrees.')
a.keep('B17','The first word has the looped d and e/s ending of des. The following iso has a separate i dot but no abbreviation point. The relation has one wave over one bar, with D_d and D_{d,d}.')
a.keep('B18','After de are two horizontal strokes of an equals sign. The lower line begins with one long shaft and a right-end head, not the letter sequence est. A descending comma follows codim without a separate point.')
a.keep('B19','In the rotated derivative, the parenthetical first group has a tall t/h-like pair and low m-like join; the following word begins with a long p descender. These favor the tentative thm prouvé? over être précis/prévu, but the compressed internal letters remain unresolved. ce sera conséquence de c) ci-dessous is visible.',crop='crops/147_scan115_second_B19_view_rot_minus45.jpg')
f=a.comparison['B20']['first'].replace("``source''",r"\inserted{``source''}")
a.change('B20',f,'The quoted source stands above the cancelled formula, beyond the baseline end of morphisme, and is a live interlinear insertion. The zigzag cancellation crosses the two D terms; b with a distinct low star remains above the shaft. The lower two-upright operator and possible prime remain doubtful, not resolved as Pi_d.')
a.replace("le morphisme ``source''",r"le morphisme \inserted{``source''}")
a.update_row(22,'B20',final=r"\inserted{``source''}",against_C=True,kind='insertion or placement',error_category='Insertions put in the wrong place')
a.report['inventory'][15].update(kind='insertion',first_words_or_objects=r"\inserted{``source''}")
old="""(174)\u005ctext{\u005cbegin{tikzpicture}[x=1mm,y=1mm,line width=.35pt,baseline=-.5mm]
\u005cdraw (0,.6)..controls (.4,.9) and (.8,-.1)..(1.5,.1);
\u005cend{tikzpicture}}"""
new=r'(174)\text{-.}'
f=a.comparison['B21']['first'].replace(old,new)
assert f!=a.comparison['B21']['first']
a.change('B21',f,'Immediately after the closing parenthesis are a dark short horizontal dash and a separate dark dot. They are not one continuous wave. The lower oblique figure remains a separately drawn pointer with two converging strokes and a short return, rather than a substituted mathematical relation.')
a.replace(old,new)
a.update_row(24,'B21',final=f)
a.report['inventory'][12]['first_words_or_objects']='short dash and separate dot after (174); small down-right pointer below'
a.keep('B22','The lighter marginal digits are two upright 1 forms followed by a clearly angled 4. The page already encloses 114 in the margin macro; this is a wrapper difference.')
a.note('Blind audit retained literal 271, the phi-shaped empty-set sign, the single explanatory arrow, and the unresolved lower marginal parenthesis. It added en as an alternative under the opening cancellation, marked the raised live source as an insertion, and separated the dash and dot after (174). Both diagonal notes were also inspected using rotations of the same fresh crops; no additional source recrop was made.')
a.finish()
