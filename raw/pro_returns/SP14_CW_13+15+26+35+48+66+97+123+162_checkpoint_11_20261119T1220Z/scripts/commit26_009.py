import sys
sys.path.insert(0,'out/scripts');from work import commit,W,row
s=(W/row(26,9)['codex_file']).read_text()
R=[(r'{\unsure{S|\mathbb S}}','S'),(r'\unsure{\mathrm{eff}|\mathrm{rel}}',r'\mathrm{eff}'),(r'\unsure{\mathrm{Isom}|\mathrm{Imm}}',r'\mathrm{Isom}'),(r'\prod_{Y/S}X/Y',r'\prod_{{\unsure{\deleted{X}Y|Y}}/S}X/Y'),(r'X\deleted{\unsure{/}}/Y\unsure{)}',r'X/Y)'),(r'X\deleted{\unsure{/}}/Y)',r'X/Y)'),(r'{\unsure{H1|H^1}}','H1'),(r'\mathrm{Pr\acute epic}\'(X\'/S\')\deleted{\unsure{=}}',r'\mathrm{Pr\acute epic}\'(X\'/S\')\unsure{\deleted{=}|\ne|\deleted{\ne}}')]
# The apostrophes above are literal primes, not control symbols.
R[-1]=(r"\mathrm{Pr\acute epic}'(X'/S')\deleted{\unsure{=}}",r"\mathrm{Pr\acute epic}'(X'/S')\unsure{\deleted{=}|\ne|\deleted{\ne}}")
R.append((r"\underline H^{1}_{X'/S'}(\underline O^{*}_{X'}))}}",r"\underline H^{1}_{\unsure{X'/S'|X/S}}(\underline O^{*}_{X'}))}}"))
for a,b in R:
 assert a in s,a
 s=s.replace(a,b)
# Curved leaders, with their arrowheads at the written labels.
s=s.replace(r'\nearrow\,\text{\uuline{pré}faisceau}',r'\begin{tikzpicture}[baseline=(p.base),x=1em,y=1em]\node[inner sep=0pt] (p) at (1.8,.7) {\scriptsize\uuline{pré}faisceau};\draw[->] (-.4,-.65) .. controls (-.3,.1) and (.25,.35) .. (.65,.45);\end{tikzpicture}')
s=s.replace(r'\searrow\,\text{faisceau}',r'\begin{tikzpicture}[baseline=(p.base),x=1em,y=1em]\node[inner sep=0pt] (p) at (1.8,-.65) {\scriptsize faisceau};\draw[->] (-.35,.45) .. controls (-.2,-.05) and (.25,-.3) .. (.7,-.45);\end{tikzpicture}')
s=s[:s.index(r'\diagram{\resizebox{\linewidth}{!}{\(\displaystyle'+'\n'+r'\unsure{?}')]+r'''
% Lower portion: relative positions, enclosing lines, circles and hatching follow the sheet.
\figure{\resizebox{\linewidth}{!}{\begin{tikzpicture}[x=.01cm,y=-.01cm,every node/.style={inner sep=0pt,anchor=west}]
\useasboundingbox (0,0) rectangle (1620,590);
\node at (205,22) {\scriptsize\begin{tabular}{c}contravariant\\en $F$ \deleted{\unsure{covar.|sur}}\end{tabular}};
\node at (920,26) {\scriptsize\begin{tabular}{c}contravariant\\en $F$\end{tabular}};
\draw (190,70) .. controls (205,48) and (238,68) .. (252,57) -- (263,53) .. controls (281,63) and (298,56) .. (313,66);
\draw (914,71) .. controls (931,60) and (948,68) .. (961,60) -- (972,56) .. controls (994,64) and (1015,60) .. (1032,69);
\node at (95,112) {\resizebox{6.35cm}{!}{$\displaystyle\mathrm{Hom}(\prod_{X/S}\underline F,\underline M)=H^0(\underline F\otimes_S\underline M),$}};
\node at (780,117) {\resizebox{6.55cm}{!}{$\displaystyle\underline{\mathrm{Hom}}(\prod_{X/S}\underline F,\underline M)=\underline H^0_{X/S}(\underline F\otimes_S\underline M)$}};
\draw (1560,5)--(1560,164);\node at (1580,117) {$X$};
\node at (16,166) {$2.$};
\draw (89,77) .. controls (92,112) and (100,134) .. (83,152) -- (79,157) .. controls (94,192) and (87,237) .. (104,265);
\node at (128,239) {\resizebox{5.05cm}{!}{$\displaystyle\underline V(\prod_{X/S}\underline F)=\prod_{X/S}V(\underline F)$}};
\node at (1065,239) {\resizebox{5.30cm}{!}{$\displaystyle V(\prod_{X/S}\underline F)=\underline{\underline{\mathrm{Hom}}}_{X/S}(F,\underline O_X)$}};
\draw (1077,226) ellipse (23 and 46);
\node at (1035,298) {$?$};
\draw (1050,291) .. controls (1074,283) and (1094,270) .. (1100,248);
\draw (1085,184) .. controls (1240,142) and (1435,185) .. (1548,162) .. controls (1591,149) and (1612,159) .. (1614,181) -- (1614,390) .. controls (1612,415) and (1490,408) .. (1430,408) .. controls (1373,408) and (1338,411) .. (1335,373) -- (1335,345) .. controls (1325,326) and (1260,334) .. (1232,333) -- (1109,335) .. controls (1087,304) and (1046,229) .. (1085,184);
\node at (1358,341) {\begin{tabular}{l}Notation\\opportune\,???\end{tabular}};
\node at (755,284) {\resizebox{2.55cm}{!}{$\deleted{\underline{\mathrm{Hom}}_{X/S}(F,G)(S')}$}};
\node at (150,378) {\resizebox{11.85cm}{!}{$\displaystyle\deleted{\underline{\underline{\mathrm{Hom}}}_{X/S}(F,G)(S')=\Gamma(S',\underline{\mathrm{Hom}}_{X'/S'}(F',G'))=\mathrm{Hom}_{\underline O_{X'}}(F',G')\unsure{4|=|\sim|?}}$}};
% Stepped enclosing stroke and the broad zigzag cancellations of the abandoned definition.
\draw (151,344) .. controls (415,335) and (612,318) .. (733,313) -- (733,288) -- (1027,250) -- (1016,321) .. controls (1120,333) and (1240,328) .. (1335,338);
\draw (151,344)--(148,404)--(1275,388);
\draw (159,393)--(178,348)--(168,390)--(232,345)--(222,394)--(286,339)--(280,396)--(349,334)--(335,393)--(408,334)--(394,393)--(478,332)--(459,392)--(547,324)--(527,391)--(616,323)--(590,390)--(686,322)--(651,389)--(750,315)--(718,388)--(816,314)--(776,388)--(880,313)--(843,386)--(942,319)--(908,383);
\draw (777,291)--(791,267)--(816,286)--(841,260)--(866,278)--(893,258)--(920,272)--(948,254)--(974,267)--(1005,252);
\draw (372,347) .. controls (461,421) and (472,314) .. (561,348) .. controls (651,420) and (688,296) .. (756,345) .. controls (832,395) and (904,312) .. (961,348);
\draw (125,384) .. controls (111,398) and (133,437) .. (118,452) -- (113,457) .. controls (131,479) and (120,552) .. (135,570);
\node at (155,472) {\resizebox{8.50cm}{!}{$\displaystyle\mathrm{Hom}(\underline{\underline{\mathrm{Hom}}}_{X/S}(F,G),\underline M)=\mathrm{Hom}_{\underline O_X\deleted{\unsure{/S}}}(F,G\otimes_{\underline O_S}M)$}};
\node at (1080,467) {\resizebox{5.30cm}{!}{$\displaystyle\underline{\mathrm{Hom}}_{\underline O_S}(\underline{\underline{\mathrm{Hom}}}_{X/S}(F,G),\underline M)=\underline{\mathrm{Hom}}_{\unsure{X/S|\deleted{X/S}|Y/S}}(F,G\otimes_S\unsure{M|\underline M}$}};
\node at (168,550) {\resizebox{8.50cm}{!}{$\displaystyle\mathrm{Hom.}_{\unsure{\underline O_{S'}}}(\underline{\underline{\mathrm{Hom.}}}(F,G)\otimes_S S',\underline O_{S'})=\mathrm{Hom}_{\underline O_{X'}}(F',G')$}};
\draw (1580,584)--(1580,510)--(1620,500);\node at (1593,541) {$G$};
\end{tikzpicture}}}
% Paper watermark, sideways through the table and obscured by the writing.
\margin{\unsure{P.J.A|P.J.} \unsure{VELIN EXTRA}}
% archive sheet number: 8
'''
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no'):
 L.append(dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh))
a('Quot, first lower index',r'\unsure{x|X}','X',r'\unsure{x|X}','quot: two crossed strokes are visible, but their reduced size in this subscript does not securely distinguish lower from upper case.','low',False,True,'misread symbol or index')
a('Quot, S alphabet',r'\unsure{S|\mathbb S}','S','S','quot: the broad dark S follows one curved handwritten body with retracing; no independent doubled vertical stem occurs.','medium',True,False,'misread symbol or index')
a('Hilb, isolated dash','dash','omitted','dash','hilb: an isolated short horizontal black stroke occurs between the two separated equality groups.',k='omission')
a('Hilb and all structural-ring letters','underlined plain O','calligraphic O, sometimes without underline','underlined plain O','hilb, prepic_liveH, prepic_old1/2, boxV, bottomleft/right: closed oval bodies with distinct short horizontal underlines; no separate script alphabet is justified by the pen finishing stroke.','high',False,True,'misread symbol or index')
a('above first Div',r'\unsure{\prime}','apostrophe in note',r'\unsure{\prime}','div/divsuffixes: a short detached upright stroke sits above the first name; its attachment and purpose remain uncertain.','medium',False,False,'other')
a('three Div suffixes',r'first eff|rel; subsequent eff','letters described as illegible','three deleted eff suffixes','divold/divsuffixes: the first suffix preserves a small looped e followed by two tall f strokes; the same lower loops and ascenders recur in the two other suffixes under diagonal cancellation.','medium',True,True,'readable ink left as \\ill{}',mh='yes')
a('Isom, middle label',r'\unsure{Isom|Imm}','Isom','Isom','isom_tight: after I the curved s joins a closed oval o before the final two-stroke m; it is distinct from the m-m sequence in the Imm row.','high',True,False,'misread word')
a('Isom, Gamma argument closing parenthesis','one closing parenthesis after Y prime','two closing parentheses','one closing parenthesis','isom: only the closing curve of (X′,Y′) precedes the equals sign; the further Γ closing parenthesis supplied by H is not written.',k='text not on the page')
a('Aut, old marks inside and after argument',r'deleted unsure =; deleted unsure S prime|=','an overwritten (S prime), described in note',r'deleted unsure =; deleted unsure S prime|=','aut: two short bars lie under the live S′ and a dense separate hatch follows its closing curve. No full old pair of parentheses can be recovered.','low',False,True,'misread symbol or index')
a('first product sign','plain product','double-underlined product','plain product','prod: the Π has two legs and a reinforced top bar; there are no horizontal underlines below its legs.',k='misread symbol or index')
a('first product lower Y','Y','Y overwritten on X',r'\unsure{\deleted{X}Y|Y}','prodoldindex: the live fork and long descending Y stroke are clear; a thick old patch and two detached remnants occupy its upper-left part. An overwritten X is possible but not securely separable.','low',True,True,'misread symbol or index')
a('word before underlined Gamma',r'\unsure{Hom|Gamma|product}','illegible word in note',r'\deleted{\unsure{Hom|\Gamma|\prod}}','productoldword_tight: upright left and right remnants and low loops survive heavy oblique hatching, but not a secure full letter sequence. The alternative symbol readings remain explicit.','low',False,True,'omission',mh='yes')
a('alternative Gamma/H0, fraction strokes','deleted slash plus live slash twice','two reinforced slashes','one reinforced slash in each argument','gamma1/gamma2: each dark mark occupies one oblique stroke position with a narrow grey interior; there is no separable cancelled character beside it.','high',True,False,'deletion state (struck given live or live given struck)')
a('alternative Gamma, closing parenthesis',r'\unsure{)}',')',')','gamma1: a continuous tall closing stroke curves left at its lower end after Y and before the two equality bars.','medium',True,False,'misread symbol or index')
a('alternative Gamma/H0, cancelled final sign',r'\unsure{4|Delta}','biffed sign in note',r'\deleted{\unsure{4|\Delta}}','gammaend: a triangular left body and long right upright with a crossbar survive, but the thick cancellation obscures the distinction between 4 and a modified Δ.','low',False,True,'omission')
a('Prépic, overwritten old subscript',r'\unsure{X/S}','blot with replacement X prime/S prime below',r'\deleted{\unsure{X/S}}','prepicoldsub: a large dark hatch covers the old index; the live replacement X′/S′ is below it. The internal old X/S reading remains tentative.','low',False,True,'omission')
a('Prépic, added upper equality',r'\unsure{H1|H^1}','H^1','H1','prepic_liveH: the narrow 1 begins at the same height as H and runs down to its baseline immediately before the opening parenthesis, rather than occupying a raised exponent position.','medium',True,True,'misread symbol or index')
a('Prépic, old H exponent',r'\unsure{H^1}','H^1 in partial note',r'\unsure{H^1}','prepic_old1: H is visible and a short raised stroke follows it, but the hatching leaves the exponent itself uncertain.','medium',False,True,'misread symbol or index')
a('Prépic, cancelled long tail','full cancelled H1 and Gamma/H1 tail','tail partly described as illegible','full cancelled tail retained, with obscured H1 subscript newly doubtful','prepic_old1/2: Γ, S′, comma, H with raised 1, O oval/star and parentheses remain recoverable between hatches. The X/S subscript has heavy overwritten strokes; its primes cannot be guaranteed.','low',True,True,'readable ink left as \\ill{}',mh='yes')
a('Prépic, cancelled right-column X',r'\unsure{X}','omitted',r'\deleted{\unsure{X}}','prepic_old2: two diagonal remnants lie against the column rule, crossed by repeated dark strokes; X remains tentative.','medium',False,True,'omission')
a('Prépic prime, old letter inside name',r'\unsure{p}','raturée letter in note',r'\deleted{\unsure{p}}','prepicprime: a long descender and upper loop are visible through the compact blot between é and the live pic. The p identification is retained as doubtful.','medium',False,True,'omission')
a('Prépic prime, old relation sign',r'\deleted{\unsure{=}}',r'deleted not-equal',r'\unsure{\deleted{=}|\ne|\deleted{\ne}}','prepicprime_oldsign: two bars are crossed by a rising slant with a looped return at the bottom. The ink does not decide whether that slant is a cancellation of =, part of ≠, or a further cancellation.','low',True,True,'deletion state (struck given live or live given struck)')
a('Prépic and Prépic prime annotation arrows','straight directional glyphs','described curved arrows','curved TikZ leaders to préfaisceau and faisceau','prepic/prepicprime: the first curves upward-right from the underlined name, the second downward-right, each ending at its explanatory word. pré alone is double-underlined.','high',True,True,'drawing or diagram')
a('Pic, overwritten argument',r'\unsure{X prime/S prime|X prime}','blot in note',r'\deleted{\unsure{X prime/S prime|X prime}}','pic: intersecting upright and oblique remains are covered by hatching before the live S′; no exact old argument is secure.','low',False,True,'omission')
a('lower first brace label',r'\unsure{?}','2.','2.','left_number: the long descending stroke turns right into a baseline foot, followed by a detached dot; this is a handwritten 2 and stop.','medium',True,False,'misread symbol or index')
a('lower Hom pair, product underlining','plain products','first double-underlined, second single-underlined','plain products','homprod/homprod_oldX: the first short horizontal remnant crosses the top of the overwritten-looking X index and does not extend beneath Π; the second Π has no underline at all.','medium',False,True,'misread symbol or index')
a('first contravariant annotation, old word',r'\unsure{covar.|sur}','biffed word in note',r'\deleted{\unsure{covar.|sur}}','contraL: several low curved bodies and a descender remain under dense strokes after F; their exact sequence is unresolved.','low',False,True,'omission')
a('boxed V formula, alphabets and underlines','plain V and plain product','underlined V and double-underlined product','plain V and plain product','boxV: V has two sloping stems with no underline; the surrounding oval and the question-mark leader are separate pen strokes. Π likewise has no underlines.',k='misread symbol or index')
a('boxed V and adjacent notation note','rectangular box and straight question arrow; note outside','surround described, no circle reproduced','curved enclosure, oval on V, headless curved question leader, Notation opportune ??? inside lower right extension','boxV and whole lower half: the frame curves above the formula and steps around the writing below; V is separately encircled. No distinct arrowhead ends the curve from ?.','high',True,True,'drawing or diagram')
a('abandoned Hom definition, upper restart','single-underlined Hom','double-underlined Hom','single-underlined Hom','oldhom_start2: one thin horizontal underline is visible below the name; the other crossing stroke is diagonal cancellation, not a second underline.',k='misread symbol or index')
a('abandoned Hom definition, final mark',r'\unsure{=|sim|?}','omitted',r'\unsure{4|=|\sim|?}','oldhom_endwide: after the argument closing curve, an upright and an angular triangular lower shape remain. It does not show a clear pair of horizontal equality bars; 4 is the primary shape reading, with the prior alternatives retained.','low',True,True,'misread symbol or index')
a('abandoned Hom definition, frame and hatching','deleted formulas without the stepped frame','frame and hatching described in note','stepped outline and oblique/looped hatching drawn','oldhom/oldhom_start2 and lower half: the main narrow strip is crossed by successive diagonal strokes and loops; its upper edge steps around the shorter restart.','high',True,True,'drawing or diagram')
a('lower-left first formula, old index suffix',r'\unsure{/S}','blot after O_X in note',r'\deleted{\unsure{/S}}','bottomleft: a slash-like remnant and curved body remain beneath a dense hatch after X. The reading stays doubtful.','low',False,True,'omission')
a('last row, first Hom subscript',r'\unsure{underlined O_S prime}','O_S prime',r'\unsure{\underline O_{S\prime}}','lower_index: the O is visible but the underline and lower S′ run into the black clipped bottom edge; they cannot be securely confirmed.','medium',False,True,'misread symbol or index')
a('last row, first and inner Hom stops','Hom, Hom','Hom, Hom','Hom., Hom.','lower_index/bottom_innerhom: a detached dark dot follows each m, separate from the following parenthesis and the underlines.','high',True,True,'omission')
a('last row, inner Hom lower index','no X/S','X/S','no X/S','bottomleft/bottom_innerhom: the double underline ends before an empty gap leading to (F,G); no X/S characters are present below the name.',k='text not on the page')
a('last row, tensor lower index','S','O_S','S','bottomleft: a single curved S is written immediately beneath the tensor sign; no preceding O oval or underline is visible.',k='misread symbol or index')
a('lower-right Hom, final lower index',r'\unsure{X|Y}/S','X/S described as struck',r'\unsure{X/S|\deleted{X/S}|Y/S}','bottom_right_sub: overlapping diagonal and upright bodies obscure the first letter and any independent cancellation; S is clearer. The live/cancelled alternatives are made explicit.','low',True,True,'deletion state (struck given live or live given struck)')
a('lower-right tensor index',r'\unsure{S}','no index','S','lower_right_end: a long curved S descends directly below the tensor circle; the index is plainly present.','high',True,True,'omission')
a('lower-right final M',r'\unsure{M|underlined M}','M',r'\unsure{M|\underline M}','lower_right_end: the rightmost letter is clipped and a slanting stroke lies below it, continuous with nearby writing. Whether it independently underlines M is unresolved.','low',False,True,'misread symbol or index')
a('lower-right closing parenthesis','none','closing parenthesis','none visible','lower_right_end: the page ends immediately after the clipped M; no closing parenthesis is visible before the black border.',k='text not on the page')
a('paper watermark',r'\unsure{P.J.A|P.J.} VELIN EXTRA','omitted',r'\unsure{P.J.A|P.J.} \unsure{VELIN EXTRA}','watermark_upright, wm_initials/word1/word2 r90 and mirrored trials: large pale outlined capitals are visible behind the formula table, but overlying ink and paper texture prevent a secure complete reading on this leaf. The initials and both words remain uncertain rather than being inferred from other pages.','low',True,True,'omission')
I=[]
def i(k,p,t,h='his hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','upper right','Notations')
i('drawing','upper right','left and lower title rules; long right column rule')
for p,t in [('row1','Quot, three occurrences; right-column F'),('row2','Hilb and quotient equality, detached dash; right-column X'),('row3','Div, three occurrences with cancelled eff; right-column X'),('row4','Hom_S, four terms; right-column X'),('row5','Isom_S, incomplete Gamma parenthesis; right-column X'),('row6','Aut_S and overwritten argument; right-column X'),('row7','Imm_S; right-column X'),('row8','product and Gamma formula, bracketed intermediate term; right-column Y'),('below row8','double-underlined Gamma and H^0 alternatives, reinforced slashes'),('row9','Prépic formula and cancelled long tail'),('row10','Prépic prime formula and H^1'),('row11','Pic formula and sheafified Prépic; right-column X'),('lower pair row1','two Hom/product formulas; right-column X'),('lower pair row2 left','underlined V(product F) = product V(F)'),('lower pair row2 right','plain V(product F) = double-underlined Hom(F,O_X)'),('abandoned row','cancelled double-underlined Hom chain'),('abandoned restart above row','single-underlined Hom_X/S(F,G)(S prime)'),('bottom left row1','Hom of double-underlined Hom and M'),('bottom left row2','Hom. with base-change tensor and second Hom.'),('bottom right','underlined Hom formula, clipped end; right-column G')]:i('display',p,t)
i('drawing','between Hilb and Div','detached prime-like stroke')
i('deletion','Div row','three eff suffixes, diagonal hatching')
i('deletion','Aut row','old argument marks inside and after current S prime')
i('deletion','product row','possible old X under Y and old word before Gamma')
i('drawing','below first product','underbrace and ou')
i('deletion','end of alternative Gamma/H0','4/Delta-like sign')
i('deletion','Prépic row','old lower index, long cohomology tail, right-column X')
i('insertion','above Prépic old tail','H1 equality at full baseline height')
i('marginnote','above first underlined Prépic','pré double-underlined in préfaisceau')
i('drawing','above first underlined Prépic','curved leader to préfaisceau')
i('deletion','Prépic prime row','old p and relation-sign uncertainty')
i('marginnote','below underlined Prépic prime','faisceau')
i('drawing','below underlined Prépic prime','curved leader to faisceau')
i('marginnote','under H^1 expression','faisceau')
i('drawing','under H^1 expression','small underbrace')
i('deletion','Pic argument','old X prime/S prime or X prime')
i('marginnote','above Hom/product pair','two contravariant en F annotations')
i('drawing','above Hom/product pair','two annotation braces')
i('deletion','first contravariant note','covar./sur-like word')
i('text','left of lower pair','2.')
i('drawing','left of lower pair','two-row brace')
i('drawing','lower right','curved enclosure around V formula and notation note; V oval and headless question leader')
i('text','inside lower right frame','?; Notation opportune ???')
i('drawing','abandoned Hom row','stepped frame, successive diagonal hatching and loops')
i('deletion','abandoned Hom row and restart','entire definitions cancelled')
i('drawing','bottom left','brace around lower two formulas')
i('deletion','bottom left first formula','old /S after O_X')
i('drawing','bottom right','short G column rule with top stroke')
i('marginnote','through page, sideways','uncertain paper watermark','paper watermark')
commit(26,9,dict(text=s,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole and both supplied halves viewed personally before C and H. Every agreed formula read from enlarged row crops; every C doubt, deletion, overwritten argument, index and margin separately enlarged. All generated decision crops were viewed; initial productoldword and left_mark boxes missed the targets and were replaced by productoldword_tight and left_number. Lower frames and all labels reconstructed in TikZ without compiling. The first Hom-product X is retraced; its short crossing bar is not taken as product underlining. Handwritten retracing is not treated as a typewriter blackboard alphabet. No next-page title from H is attributed to this leaf. Archive8 stays a comment. Context unopened.'))
