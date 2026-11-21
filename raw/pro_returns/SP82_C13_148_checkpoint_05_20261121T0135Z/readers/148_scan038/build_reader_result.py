from pathlib import Path
import json,csv,re
P=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan038')
O=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan038')
C=(P/'C.tex').read_text();H=(P/'H.tex').read_text()
B=json.loads((O/'crop_boxes.json').read_text())
S=C[:C.index(r'\unsure{\texttt{00 00}}')].rstrip()+'\n'
oldtitle=r'''\uline{Autom d'ordre deux d'une sphère holomorphe \inserted{$\Sigma$} à
\inserted{un $K$ de} $5$ pts marqués}'''
title=r'''\uline{Autom d'ordre deux d'une sphère holomorphe} \inserted{$\Sigma$}
\uline{\unsure{à|:}} \inserted{un $K$ de} $5$ \uline{pts marqués}'''
assert oldtitle in S
S=S.replace(oldtitle,title)
old=r'''Introduisant $T_2=T^{\wedge2}\simeq L_2^*$, où
$L_2=L_1^{\otimes2}$, cel'''
new=r'''Introduisant $T_2=T^{\wedge2}$\inserted{$\simeq L_2^*$, où
$L_2=L_1^{\otimes2}$,}, cel'''
assert old in S
S=S.replace(old,new)
S=S.replace(r'\mathrm{iso.}',r'\mathrm{iso}')
S=S.replace(r'\mu_4(\mathbb C^*)',r'\mu_4(\mathbb C_*)')
S=S.replace(r'\unsure{T_2|L_2}',r'\unsure{t_2|T_2}')
S=S.replace(r'\unsure{bibase}','bibase')
S=S.replace(r'(\xi+\eta)^2-4\xi\eta\ne0',r'(\xi\unsure{\wedge|+}\eta)^2-4\xi\wedge\eta\ne0')
S=S.replace(r'\unsure{\xi^2+\eta^2-2\xi\eta\ne}',r'\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}')
S=S.replace(r'\deleted{$(\xi+\eta)^2$}',r'\deleted{$\unsure{(\xi+\eta)^2}$}')
S=S.replace(r'\mspage{37}',r'\margin{37}')
(O/'candidate.tex').write_text(S)
print('candidate.tex saved')

def ref(k): return f'crops/148_scan038_{k}.png'
def hs(a,z): return H[H.index(a):H.index(z,H.index(a))]
changes=[]
def ch(place,c,h,final,ink,k,kind,ac=False,ah=False,math=False,confidence='high',**kw):
    assert c is None or c in C,('C',place,c)
    assert h is None or h in H,('H',place,h)
    d=dict(place=place,c=c,h=h,final=final,ink=ink,crop=ref(k),box=B[k],confidence=confidence,kind=kind,against_c=ac,against_h=ah,math=math)
    d.update(kw);changes.append(d)
ch('title, underline scope',oldtitle,None,title,'The long title underline ends to the left of the 5. A separate line lies below pts marqués. The raised un K de has its own returning insertion leader; it is not covered by the title underline. C’s one underline covers all these different positions.','heading','insertion or placement',ac=True)
ch('title, added sphere and five-point phrase',r'\inserted{$\Sigma$} à\n\inserted{un $K$ de} $5$'.replace(r'\n','\n'),r'\add{$\Sigma$ \uncertain{avec} $K$ \ill{}}',r'\inserted{$\Sigma$} \unsure{à|:} \inserted{un $K$ de} $5$','The upper zigzag has both horizontal arms of Sigma. Beside it, the short connected un precedes a clear open K and the looped d/e ending. The following live numeral has a bent upper entry and rounded returning lower part of 5. There is no avec sequence. The separate preposition/punctuation remains uncertain.','heading','misread word',ah=True,math=True)
ch('opening, abbreviation autom','autom',r'automor.','autom','The live abbreviation ends after the low connected m humps, before the separately raised automorphism label. No following or or point is visible.','autom_condition','abbreviation expanded or spelling modernised',ah=True)
ch('opening, inserted automorphism label',r'\inserted{$\sigma$}',None,r'\inserted{$\sigma$}','A small looped sign with a rightward exit sits above the gap between autom and d’ordre. It is an interlinear label omitted by H’s first sentence.','autom_condition','omission',ah=True,math=True)
ch('opening, inserted fixed-point exclusion',r'\inserted{$I$ ne contenant pas de pt fixe de $\sigma$.}',hs('$I$ ne contenant pas de pt fixe de', ' Donner'),r'\inserted{$I$ ne contenant pas de pt fixe de $\sigma$.}','The complete I ne contenant pas de pt fixe de sigma sentence occupies a smaller intermediate line between the automorphism sentence and Donc. Its final low loop and exit belong to the same automorphism label; H flattens the placement and proposes u.','autom_condition','insertion or placement',ah=True,math=True,confidence='medium')
ch('transition, Donc cel.','Donc cel.','Donner cela','Donc cel.','The first word ends in a short low c after the D/o/n sequence. The next word has a looped l and a separate point immediately after cel; no final a follows it.','autom_condition','misread word',ah=True)
ch('item a, automorphism wording',r'un autom \inserted{$\sigma$}',r'avec automorph.\ \add{$u$}',r'un autom \inserted{$\sigma$}','The short word after Sigma has the low strokes of un. The following contraction ends in m, without orph. The raised label has a curved body and extended exit like the earlier sigma; it is not a separate full-height u on the baseline.','item_a','misread word',ah=True,math=True,confidence='medium')
ch('item a, naming the marked fixed point','appelant celui-ci',r'\uncertain{appelons}-le','appelant celui-ci','Two descending p strokes begin the verb, followed by low e/l/a/n and a short terminal t. The next word begins with c/e and has the separated -ci ending; the source does not end the verb in -ons or follow it by -le.','item_a','misread word',ah=True)
ch('item a, punctuation after zero',r'pt fixe $0$,',r'pt fixe $0$ ;',r'pt fixe $0$,','The zero is a separate small loop. The following punctuation has one descending comma stroke, with no independent upper dot of a semicolon.','item_a','misread symbol or index',ah=True,math=True)
ch('item a, baseline complexe','complexe',"\\note{« complexe »\nen interligne ; sous la ligne, « (dimension 1) »}",'complexe','Complexe continues the baseline of vectorielle and L1. It has no insertion leader. The small parenthesized text below is a different addition linked to orbites in item b, not a dimension annotation belonging to this line.','distinctes_insertion','insertion or placement',ah=True)
ch('item b, distinctes insertion',r'\inserted{(distinctes)}','(dimension 1)',r'\inserted{(distinctes)}','Inside two visible parentheses, d is followed by the dotted i, crossed tall t, and compressed -inctes ending. A curved leader descends to the place after orbites. There is no m sequence or separate numeral 1.','distinctes_insertion','misread word',ah=True)
ch('item b, interlinear square-torsor identification',old[:-4],hs('$T_2 =', ' cela revient'),new[:-4],'The isomorphism sign, L2-star, où, and L2=L1-tensor-square lie above the Introduisant/cel baseline. One long returning stroke below them reaches the end of T-wedge-square. A separate small comma lies on the main line, while another follows the upper tensor-square expression; both visible comma strokes are retained.','torseur_square','insertion or placement',ac=True,ah=True,math=True,confidence='medium')
ch('item b, abbreviated cel','cel revient',r'cela revient','cel revient','The short word before revient has a small c/e entry and one tall looped l; it ends there before the next word, without a separate final a.','torseur_square','abbreviation expanded or spelling modernised',ah=True)
ch('item b, inserted pair coordinates',r'\inserted{$\{\xi,\eta\}$}',r'$\lbrace \xi, \eta \rbrace$',r'\inserted{$\{\xi,\eta\}$}','The small brace pair and xi/eta symbols are raised above the gap after pts, before the full-sized parenthesized distincts. H places them on the baseline.','pair_points','insertion or placement',ah=True,math=True)
ch('isomorphism display, short label',r'\mathrm{iso.}','isom',r'\mathrm{iso}','The label has the initial i, a compact s and a closed final o. No m follows. The only tiny point beyond o is gray and unlike the dark label strokes; it is not accepted as abbreviation punctuation.','iso','misread word',ac=True,ah=True,confidence='medium')
ch('isomorphism display, terminal punctuation',r'\mathbf1_{\mathbb C^*}',r'\mathbf{1}_{\mathbf{C}^{*}}$,',r'\mathbf1_{\mathbb C^*}','The dark unit/C-star group has no adjoining comma at its baseline. Pale reversed machine marks below the formula do not supply sentence punctuation.','iso','text not on the page',ah=True,math=True)
ch('first structural reduction, colon',r'de $\mathbb C^*$ :',r'de\n$\mathbf{C}^{*}$ à'.replace(r'\n','\n'),r'de $\mathbb C^*$ :','Two discrete dark dots stand vertically after C-star. There is no joined a body with an accent; the manuscript uses a colon here.','structural','misread symbol or index',ah=True)
ch('fourth-root group, lowered star',r'\mu_4(\mathbb C^*)',r'\mu_4(\mathbf{C}^{*})',r'\mu_4(\mathbb C_*)','The asterisk inside the parentheses is at the lower right of C, beneath its lower curve. This differs visibly from the raised star on the preceding C-star in the same line. Both witnesses raise this lower star.','structural','misread symbol or index',ac=True,ah=True,math=True)
ch('sum membership target',r'\unsure{T_2|L_2}',r'\xi + \eta \in T_2',r'\unsure{t_2|T_2}','The heavy glyph has a horizontal crossbar extending to both sides of a stem, with the stem protruding upward and turning into a lower rightward foot. This excludes an ordinary L; the overtraced form remains uncertain between lower-case t and capital T. No mathematical replacement by L is made.','sum_condition','misread symbol or index',ac=True,ah=True,math=True,confidence='medium',mark_ids=['M0499'])
ch('live condition, middle and product signs',r'(\xi+\eta)^2-4\xi\eta\ne0',r'(\xi + \eta)^{2} - 4\xi\eta \neq 0',r'(\xi\unsure{\wedge|+}\eta)^2-4\xi\wedge\eta\ne0','Between xi and eta after the4, two distinct inclined strokes meet at a peak, matching the explicit wedge in e=xi-wedge-eta above. Inside the first parentheses the smaller sign is also peaked, but a reduced crossing cannot be excluded; it is retained as wedge/plus uncertain. The clear plus in the preceding xi+eta line supplies the local comparison. Both witnesses omit the later wedge.','sum_condition','misread symbol or index',ac=True,ah=True,math=True,confidence='medium')
ch('short cancellation after discriminant',r'\deleted{\unsure{un}}',r'\struck{\ill{}}',r'\deleted{\unsure{un}}','The short crossed cluster retains two low humps and a final descending return, compatible with un, but the strike conceals enough of the letters to keep C’s doubt. The following point is separate and live.','sum_condition',r'readable ink left as \ill{}',ah=True,confidence='low')
ch('cancelled expansion after Notons',r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\eta\ne}$}',r'\struck{$(\xi + \eta)^{2} - 2\xi\eta \neq$}',r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}$}','The struck line has a distinct raised 2 after eta, a minus followed by2, and a peaked wedge between the long xi tail and eta descender before the final unequal sign. Both witnesses omit that wedge. There are no readable enclosing parentheses of H’s squared sum. The small raised shape after the first xi and the crossings through the other signs prevent certifying the full expanded expression.','cancelled_expansion','misread symbol or index',ac=True,ah=True,math=True,confidence='low')
ch('second structural reduction, colon',r'\mathbb C^*$ :',r'\mathbf{C}^{*}$ à',r'\mathbb C^*$ :','After C-star, two separated dark marks form a colon before the brace containing plus/minus 1. There is no continuous a-shaped letter.','lower_reduction','misread symbol or index',ah=True)
ch('bibase',r'\unsure{bibase}','le biais de','la bibase','The word has two separate tall b stems with a dotted short i between them, followed by the low joined a/s/e strokes. The radical follows directly after it: no separate de is written. The preceding article has the low a ending of la.','lower_reduction','misread word',ac=True,ah=True,certainty_resolution=True,mark_ids=['M0500'])
ch('abbreviated element',r'\unsure{élt}','élément',r'\unsure{élt}','The small word consists of a compact initial loop and the joined tall/final strokes of a short elt-form. It is far shorter than élément and has no following -ément sequence. The initial accent/letter detail remains uncertain.','ending','abbreviation expanded or spelling modernised',ah=True,confidence='medium')
ch('sign qualification','à un signe',r'aux signes','à un signe','The source has a separate small à-like mark followed by un; the following signe ends after its e, without a final s. No x closes the article.','ending','misread word',ah=True)
ch('final relative word','dont','donc','dont','The final word ends with a tall dark t stem and cross stroke. The ending is not the low open c of donc.','ending','misread word',ah=True)
ch('bottom-left foliation',r'\mspage{37}',None,r'\margin{37}','The light numeral has two open rounded lobes of 3 followed by a long descending 7 with a transverse bar. It is retained as unassigned foliation, not attributed to the main writer. H’s editorial note omits this written number.','foliation','omission',ah=True)
start=C.index(r'\unsure{\texttt{00 00}}');split=C.index(r'\unsure{\texttt{16.18 TOTL}}')
ch('pale reversed listing, labels block',C[start:split].strip(),None,'','The pale blue machine labels and number groups have laterally reversed asymmetric characters and run behind the dark front handwriting. Their source is reverse-side show-through, so C’s attempted text and illegibility tokens are excluded.','bleed_lower','text not on the page',ac=True,mark_ids=[f'M{i:04d}' for i in range(502,519)])
ch('pale reversed listing, numerical block',C[split:].strip(),None,'','The pale timestamp-like rows have the same reversed orientation and mechanical type as the lower labels. They do not belong to the front manuscript and are omitted, including C’s guessed digits and associated illegibility token.','bleed_upper','text not on the page',ac=True,mark_ids=[f'M{i:04d}' for i in range(519,526)])

decisions=[]
def de(i,d,reading,ink,k,confidence='high'):
    decisions.append(dict(id=i,decision=d,reading=reading,ink=ink,crop=ref(k),box=B[k],confidence=confidence))
de('M0499','other',r'\unsure{t_2|T_2}','The crossbar passes to both sides of a protruding stem, excluding an ordinary L. The thick lower foot and retouching leave the case t/T unresolved.','sum_condition','medium')
de('M0500','first','bibase','Two tall b stems, a short dotted i and the low a/s/e ending are visible; no separate de stands before the radical.','lower_reduction')
de('M0501','undecided',r'\unsure{élt}','The short form is not the full word élément, but the initial accent and compressed first letter do not yet support removal of the doubt.','ending','medium')
for i in range(502,526):
    de(f'M{i:04d}','other','','Pale blue machine type is laterally reversed and lies behind the dark front manuscript. This mark belongs to reverse-side show-through and is excluded.','bleed_lower' if i<519 else 'bleed_upper')

inventory=[]
def iv(e,k,pos,words,hand='main manuscript hand'):
    inventory.append(dict(element=e,kind=k,position=pos,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
iv('title','text','two upper baselines',title)
iv('title_sigma','insertion','above the end of holomorphe',r'\inserted{$\Sigma$}')
iv('title_five_point_phrase','insertion','above the 5, with curved leader',r'\inserted{un $K$ de}')
iv('fixed_point_description','text','below the title through the first automorphism sentence',r'Un pt fixe exactement dans \(K\)')
iv('first_sigma','insertion','above gap between autom and d’ordre',r'\inserted{$\sigma$}')
iv('fixed_point_exclusion','insertion','small line between the automorphism sentence and Donc',r'\inserted{$I$ ne contenant pas de pt fixe de $\sigma$.}')
iv('transition','text','above item a','Donc cel. revient à la donnée')
iv('item_a','text','six baselines from a) to L1-star',r"a) D'une sphère hol. \(\Sigma\)")
iv('item_a_sigma','insertion','above autom in item a',r'\inserted{$\sigma$}')
iv('item_b','text','from b) to Considérons alors le pt',r"b) D'une paire d'orbites")
iv('distinctes','insertion','between items a and b, linked to orbites',r'\inserted{(distinctes)}')
iv('square_torsor','insertion','above Introduisant/cel baseline',r'\inserted{$\simeq L_2^*$, où $L_2=L_1^{\otimes2}$,}')
iv('pair_coordinates','insertion','above the gap after pts',r'\inserted{$\{\xi,\eta\}$}')
iv('product_display','display','middle-lower page, with the L4 definition on a second baseline',r'e=\xi\wedge\eta=\eta\wedge\xi\in T_4=T^{\wedge4}\simeq L_4^*\quad(\text{où }L_4=L_1^{\otimes4})')
iv('isomorphism_intro','text','above the isomorphism display','on a donc un')
iv('isomorphism','display','below product display',r'\mathrm{iso}\quad T^{\wedge4}\simeq\mathbf1_{\mathbb C^*}')
iv('first_reduction','text','two baselines after the isomorphism',r"d'où une réduction du groupe structural")
iv('de_T','insertion','above end of structural',r'\inserted{de $T$}')
iv('pair_reconstruction','text','from On peut dire through the discriminant condition',r'On peut dire que la donnée de \(\{\xi,\eta\}\)')
iv('e_membership','insertion','above et following e=xi-wedge-eta',r'\inserted{\(\in T_4\)}')
iv('cancelled_un','deletion','after the nonzero discriminant, before the live point',r'\deleted{\unsure{un}}')
iv('Notons','text','right end of the discriminant baseline','Notons')
iv('cancelled_expansion','deletion','beginning of the following line, before que',r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}$}')
iv('second_reduction','text','last four manuscript baselines',r'que \(T_2\) admet une réduction du groupe structural')
iv('cancelled_final_square','deletion','bottom right, after dont',r'\deleted{$\unsure{(\xi+\eta)^2}$}')
iv('foliation','margin note','bottom left',r'\margin{37}','unassigned lighter foliation hand')

unresolved=[
dict(place='title, sign after holomorphe',reading=r'\unsure{à|:}',issue='An upper angled mark and lower heavy loop/dot do not securely distinguish an accented a from a colon.',alternatives=['à',':'],confidence='medium'),
dict(place='sum membership target',reading=r'\unsure{t_2|T_2}',issue='A strong crossbar excludes an ordinary L, but the protruding stem and heavy foot leave lowercase t versus capital T uncertain.',alternatives=[r't_2',r'T_2'],confidence='medium'),
dict(place='live condition, sign in first parentheses',reading=r'(\xi\unsure{\wedge|+}\eta)^2-4\xi\wedge\eta\ne0',issue='The small middle sign is peaked, unlike the clear plus in the preceding sum, but its reduced shape could include a crossing. The later product wedge is clear and is retained.',alternatives=[r'\wedge','+'],confidence='medium'),
dict(place='short cancellation after discriminant',reading=r'\deleted{\unsure{un}}',issue='The strike obscures most of the low letters; un remains only a tentative recovery.',alternatives=['un'],confidence='low'),
dict(place='cancelled expansion after Notons',reading=r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}$}',issue='The raised shape after the first xi and several crossings are not independently plain. The eta-square, expanded layout and peaked wedge between the last factors support the retained tentative expression.',alternatives=[r'\xi^2+\eta^2-2\xi\wedge\eta\ne'],confidence='low'),
dict(place='abbreviated element',reading=r'\unsure{élt}',issue='The word is visibly abbreviated, but the initial accent/letter is not secure enough to remove the existing doubt.',alternatives=['élt','elt'],confidence='medium'),
dict(place='final cancelled square',reading=r'\deleted{$\unsure{(\xi+\eta)^2}$}',issue='The outer parentheses and raised 2 survive; the central xi-plus-eta strokes are partly hidden by the heavy cancellation. The formula gains doubt without a certainty-only changes row.',alternatives=[r'(\xi+\eta)^2'],confidence='medium'),
]
notes=[
dict(id='148038_N01',text='This portrait manuscript is written over the reverse of a machine listing. The pale blue reversed type is excluded as show-through. The lighter bottom-left 37 is retained as foliation with its hand unassigned. No printed dates or source-page sequence are inferred from H’s editorial comments.'),
dict(id='148038_N02',text='The parenthesized distinctes is a raised addition linked to orbites in item b. It is not dimension1; complexe lies on the preceding baseline. The square-torsor identification is also interlinear, with two visible comma strokes retained around the addition.'),
dict(id='148038_C01',text='The page studies a nonidentity holomorphic involution of a sphere preserving five marked points. A Möbius involution has two fixed points. Decomposing a five-element invariant set into fixed points and two-element orbits leaves exactly one fixed point and two free orbits. Marking the fixed point called infinity and calling the other zero gives the multiplicative-torsor description used in item a.'),
dict(id='148038_C02',text='After those two fixed points are placed at infinity and zero, the involution is multiplication by −1. Squaring identifies its two-element orbits on the nonzero line with points of the square torsor. Thus item b’s unordered pair of distinct orbits corresponds to an unordered pair of distinct nonzero square-torsor points.'),
dict(id='148038_C03',text='The page uses wedge notation for a symmetric torsor product, as its explicit xi-wedge-eta=eta-wedge-xi indicates. In a compatible coordinate, e is the nonzero product xi eta in the fourth tensor power. A choice of e gives the fourth-root reduction to mu4; the two square roots in the square line give the plus/minus basis called a bibase. Relative to either member of that pair, the coordinate of xi+eta is determined up to sign. These are the interpretations checked; an alternating exterior-product convention is not imposed.'),
dict(id='148038_C04',text='If the uncertain sign inside the first parentheses is plus, the computed identity (xi+eta)^2−4xi eta=(xi−eta)^2 gives the distinctness criterion over C. The manuscript visibly writes a wedge in the later product and a peaked, unresolved wedge/plus sign inside the parentheses. Its cancelled expanded expression is compatible with the identity if the uncertain first exponent is2. These algebraic checks do not resolve the manuscript signs or the cancelled strokes.'),
dict(id='148038_C05',text='The sum target is written with a t/T-like crossbar, not a clear L. If it denotes the previously defined T2=L2-star, the membership assertion has a counterexample: xi=1 and eta=−1 are distinct nonzero points, their product is−1 and their sum is0. The plus interpretation of the following condition gives4, and the product interpretation gives5 in these coordinates; either is nonzero. The appropriate ambient vector line would be L2. The literal ambiguous t/T form remains in the transcription.'),
dict(id='148038_N03',text='In the fourth-root group notation the star is visibly below C, unlike the raised star just before it. The low placement is preserved as C_*. No further meaning or correction of this local star placement is imposed.'),
]
who='GPT-6 Astra Pro; effort not exposed; run SP82_C13_148; reader B'
checks=[
dict(statement_id='148038_C01',date='2026-11-20',who=who,type='targeted proof check',outcome='Represent the nonidentity Möbius involution by a nonscalar invertible 2×2 matrix A. Its square is scalar. Over C its two distinct eigenvalues differ by sign, giving exactly two fixed projective directions; after placing them at0 and infinity the map is z↦−z. This checks the geometric fixed-point premise used on the page.'),
dict(statement_id='148038_C01',date='2026-11-20',who=who,type='computation or formal certificate',outcome='Enumerating integer solutions of 5=f+2n with 0≤f≤2 and n≥0 returned only (f,n)=(1,2). This checks the fixed-point/orbit count conditional on the preceding geometric premise.'),
dict(statement_id='148038_C02',date='2026-11-20',who=who,type='targeted proof check',outcome='For nonzero complex x and y, x²=y² iff y=x or y=−x. The squaring map therefore identifies exactly the ±1 orbits; distinct orbits give distinct nonzero points of the square line.'),
dict(statement_id='148038_C03',date='2026-11-20',who=who,type='targeted proof check',outcome='For e≠0, the roots of w⁴=e are nonzero and distinct because 4w³ does not vanish there; multiplication by the fourth roots of1 acts freely and transitively. In the square line, the two roots of v²=e differ by sign and are nonzero. Dividing the same vector sum by the two opposite bases changes its scalar coordinate by sign.'),
dict(statement_id='148038_C04',date='2026-11-20',who=who,type='computation or formal certificate',outcome='SymPy expanded (x+y)²−4xy to x²−2xy+y², factored it as (x−y)², and returned0 for the difference between x²+y²−2xy and (x−y)². This checks the plus interpretation and tentative expanded algebra only; it does not settle the manuscript’s wedge/plus sign or cancelled handwriting.'),
dict(statement_id='148038_C05',date='2026-11-20',who=who,type='computation or formal certificate',outcome='Substituting x=1,y=−1 gives product−1, sum0 and (x+y)²−4xy=4. Direct substitution also gives (xy)²−4xy=1+4=5. The sum therefore need not lie in the nonzero torsor under either reading of the separate uncertain sign.'),
]
hand_log=[
dict(habit='A compressed short form may end with a tall looped l and no final a.',pages=[38],scope='holds_at_every_observed_occurrence',holds_at_every_observed_occurrence=True,observed_scope='The two cel forms after Donc and in item b.',witness_effect='H expands both to cela; the first source form also has a visible abbreviation point.'),
dict(habit='Colon punctuation consists of two detached stacked dark dots, distinct from a full joined a-shaped body.',pages=[38],scope='holds_at_every_observed_occurrence',holds_at_every_observed_occurrence=True,observed_scope='The two structural-group reductions; the uncertain title sign is excluded from this observation.',witness_effect='H reads à at both reduction signs; the manuscript dots support colons.'),
]
notation=[
dict(form=r'T^{\wedge2},\ T^{\wedge4}',observation='The page writes wedge powers for the square and fourth-power torsors, alongside tensor powers of L1.',place='item b and product display'),
dict(form=r'\xi\wedge\eta=\eta\wedge\xi',observation='The explicit equality records a symmetric torsor product; no alternating exterior-product convention is imposed.',place='product display'),
dict(form=r'\mu_4(\mathbb C_*)',observation='The star in the parentheses is placed below C; a raised star appears on the preceding C in the same line.',place='first structural reduction'),
dict(form='bibase',observation='The page names the opposite pair of square roots ±sqrt(e) by this word.',place='bottom reduction paragraph'),
]
abbreviations=[dict(form='Autom',expansion='Automorphisme'),dict(form='autom',expansion='automorphisme'),dict(form='pt',expansion='point'),dict(form='pts',expansion='points'),dict(form='hol.',expansion='holomorphe'),dict(form='cel.',expansion='cela'),dict(form='cel',expansion='cela'),dict(form='i.e.',expansion='id est'),dict(form='iso',expansion='isomorphisme'),dict(form=r'\unsure{élt}',expansion='élément (tentative short-form reading)')]

second=[]
def sb(key,kind,xy,reading):
    second.append(dict(box='148038_'+key,kind=kind,x0=xy[0],y0=xy[1],x1=xy[2],y1=xy[3],reading=reading))
sb('title_line','insertion',[150,37,1430,164],title[:title.index(r'\uline{pts marqués}')].strip())
sb('title_pts','underline scope',[244,168,570,267],r'\uline{pts marqués}')
sb('opening_autom','insertion',[579,328,1056,411],r"autom \inserted{$\sigma$} d'ordre $2$,")
sb('fixed_point_exclusion','insertion',[245,398,1078,458],r'\inserted{$I$ ne contenant pas de pt fixe de $\sigma$.}')
sb('Donc_cel','C/H different word',[241,446,938,498],'Donc cel. revient à la donnée')
sb('item_a_first','insertion',[245,493,1505,580],r"a) D'une sphère hol. $\Sigma$, un autom \inserted{$\sigma$} d'ordre $2$")
sb('appelant','C/H different word',[255,586,1476,682],'et un pt fixe marqué --- appelant celui-ci')
sb('fixed_points','handwritten number',[245,645,1310,726],r"$\infty$, et l'autre pt fixe $0$, cela revient à la")
sb('torseur_definition','handwritten number',[936,720,1337,793],r'$T_1\ (=\Sigma\setminus\{0,\infty\})$')
sb('vector_line','handwritten number',[244,787,1492,871],r"$\mathbb C^*$, i.e. d'une droite vectorielle complexe $L_1$ $(T_1=L_1^*)$")
sb('distinctes','insertion',[826,817,1076,923],r'\inserted{(distinctes)}')
sb('involution_group','handwritten number',[1026,875,1463,943],r'$\{\pm1\}\subset\mathbb C^*$ opérant')
sb('T1_line','handwritten number',[350,963,535,1030],r'$T_1=L_1^*$.')
sb('square_identification','insertion',B['torseur_square'],r'Introduisant $T_2=T^{\wedge2}$\inserted{$\simeq L_2^*$, où $L_2=L_1^{\otimes2}$,}, cel revient à la donnée')
sb('pair_coordinates','insertion',[806,1088,886,1149],r'\inserted{$\{\xi,\eta\}$}')
sb('pair_target','handwritten number',[1244,1120,1351,1178],r'$T_2$.')
sb('product_display','handwritten number',[590,1241,1437,1419],r'\(e=\xi\wedge\eta=\eta\wedge\xi\in T_4=T^{\wedge4}\simeq L_4^*\quad(\text{où }L_4=L_1^{\otimes4})\)')
sb('isomorphism','C departure below high confidence',B['iso'],r'\(\mathrm{iso}\quad T^{\wedge4}\simeq\mathbf1_{\mathbb C^*}\)')
sb('deT','insertion',[1311,1457,1468,1554],r'\inserted{de $T$}')
sb('fourth_root_group','handwritten number',[239,1585,1069,1669],r'de $\mathbb C^*$ : $\mu_4(\mathbb C_*)\simeq\mathbb Z/4\mathbb Z$.')
sb('product_membership','insertion',[395,1733,638,1844],r'$e=\xi\wedge\eta\inserted{\in T_4}$')
sb('sum_membership','doubtful formula',[801,1744,1027,1845],r'$\xi+\eta\in\unsure{t_2|T_2}$,')
sb('condition','doubtful formula',[669,1846,1071,1932],r'$(\xi\unsure{\wedge|+}\eta)^2-4\xi\wedge\eta\ne0$')
sb('cancelled_un','deletion',[1096,1841,1428,1913],r'\deleted{\unsure{un}}. Notons')
sb('cancelled_expansion','deletion',B['cancelled_expansion'],r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}$}')
sb('T2_reduction','handwritten number',[780,1926,858,1990],r'$T_2$')
sb('sign_group','handwritten number',[881,1992,1211,2074],r'$\mathbb C^*$ : $\{\pm1\}$,')
sb('bibase','C/H different word',[243,2063,879,2145],r'la bibase $\pm\sqrt e$, donc')
sb('elt','C/H different word',[324,2129,438,2188],r'\unsure{élt}')
sb('sign_qualification','C/H different word',[677,2127,1107,2205],'à un signe près,')
sb('dont','C/H different word',[1145,2128,1248,2188],'dont')
sb('cancelled_final_square','deletion',[1268,2115,1469,2199],r'\deleted{$\unsure{(\xi+\eta)^2}$}')
sb('foliation','handwritten number',B['foliation'],r'\margin{37}')

diffrows=list(csv.DictReader((P/'differences.tsv').open(),delimiter='\t'))
rev={}
def dr(ns,status,reading,ks,note):
    for n in ns: rev[n]=dict(source_row=n,status=status,reading=reading,crops=[ref(k) for k in ks],note=note)
dr([741],'editorial_only','',['foliation'],'H’s statement about the sheet and other face is editorial. The actual unassigned foliation37 is retained; no other page was opened.')
dr([742],'undecided',r'\unsure{à|:}',['heading'],'Upper angled stroke and lower heavy loop/dot do not settle accented a versus colon.')
dr([743],'other_reading',r'\unsure{à|:} \inserted{un $K$ de}',['heading'],'Un K de is an upper addition; avec is not written.')
dr([744],'editorial_only','',['heading'],'H’s interlinear description is editorial; the actual raised words and their attachment are recorded separately.')
dr([745],'C_confirmed','5',['heading'],'The live5 is visible and outside the title underline; H’s pointer wording does not transcribe it.')
dr([746],'C_confirmed',r'autom \inserted{$\sigma$}',['autom_condition'],'The contraction ends in m; the raised sigma is present.')
dr([747],'C_confirmed',r'\sigma',['autom_condition'],'The terminal low loop/exit is compared with the raised automorphism labels; the whole exclusion sentence is interlinear.')
dr([748],'C_confirmed','Donc cel.',['autom_condition'],'No Donner ending or final a after cel; the point is visible.')
dr([749],'C_confirmed',r'un autom \inserted{$\sigma$}',['item_a'],'Un and the short autom form are written, with a raised label.')
dr([750,751],'C_confirmed','appelant celui-ci',['item_a'],'Two p descenders and terminal t; the following word has a -ci ending.')
dr([752],'C_confirmed',r'$0$,',['item_a'],'The small loop is zero and the only following punctuation stroke is a comma.')
dr([753],'other_reading',r'complexe \inserted{(distinctes)}',['distinctes_insertion'],'Complexe is baseline. The small parenthesized word reads distinctes and is linked to orbites; there is no dimension1 annotation.')
dr([754],'C_confirmed',r'\inserted{(distinctes)}',['distinctes_insertion'],'The insertion is retained at its actual item-b attachment.')
dr([755],'C_confirmed','cel',['torseur_square'],'The tall looped l ends the abbreviation; no a follows.')
dr([756],'other_reading',r'\mathrm{iso}',['iso'],'The label has no m and no secure dark terminal dot.')
dr([757],'C_confirmed','',['iso'],'No baseline terminal comma appears after the unit/C-star group.')
dr([758],'C_confirmed',':',['structural'],'Two separate dark dots, not à.')
dr([759],'other_reading',r'\unsure{t_2|T_2}',['sum_condition'],'The crossbar excludes an ordinary L; case remains uncertain and mathematics does not replace the glyph.')
dr([760],'C_retained_uncertainty',r'\deleted{\unsure{un}}',['sum_condition'],'The short crossed word is retained tentatively; the following point is live.')
dr([761,762,763],'other_reading',r'\deleted{$\unsure{\xi^2+\eta^2-2\xi\wedge\eta\ne}$}',['cancelled_expansion'],'The expanded layout and eta-square differ from H’s parenthesized sum. A peaked wedge occurs in the last product; the whole crossed expression remains doubtful.')
dr([764],'C_confirmed',':',['lower_reduction'],'Two vertically detached dark punctuation marks precede the sign group.')
dr([765],'C_resolved_first','la bibase',['lower_reduction'],'Two b stems and the short i are visible; no separate de precedes the radical.')
dr([766],'C_retained_uncertainty',r'\unsure{élt}',['ending'],'The abbreviated form is retained; its initial accent/letter detail remains unresolved. H expands it.')
dr([767],'C_confirmed','à un signe',['ending'],'Separate un, with neither x nor a plural s after signe.')
dr([768],'C_confirmed','dont',['ending'],'A tall crossed terminal t is visible.')
dr([769],'other_reading',r'\margin{37}',['foliation','bleed_upper','bleed_lower'],'Retain the written foliation; exclude the pale reversed listing and H’s editorial continuation note.')
reviews=[]
for row in diffrows:
    n=int(row['source_row']);d=rev[n];d['c']=row['witness C'];d['h']=row['witness H'];reviews.append(d)
result=dict(scan=38,reader='B',model='GPT-6 Astra Pro',reasoning_effort='not exposed',run='SP82_C13_148',lines_read=38,
lines_read_breakdown=dict(main_prose_baselines=25,display_baselines=3,interlinear_baselines=9,margin_baselines=0,foliation=1,method='Primary manuscript baselines, counting the separately raised labels and additions. Pale reversed machine rows were visually inspected and excluded as show-through.'),
changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second,differences_review=reviews,
reading_procedure=dict(whole_page_views=1,native_half_views=[1,1],evidence_crop_count=15,crops=[dict(label=k,crop=ref(k),box=v,rotation=0) for k,v in B.items()],all_C_deletions_and_insertions_audited=True,all_supplied_marks_decided=True,all_supplied_difference_rows_reviewed=True,no_ocr=True,no_web=True,no_tex_compilation=True,crop_provenance='Each of15 evidence crops was made once and actually viewed. Existing sum_condition and cancelled_expansion evidence was reopened to compare signs; neither was recropped. Same-pixel JPEG encodings served only for image transport; original enhanced PNGs are preserved.'))
(O/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),marks=len(decisions),inventory=len(inventory),unresolved=len(unresolved),second_boxes=len(second),differences=len(reviews),checks=len(checks))))
