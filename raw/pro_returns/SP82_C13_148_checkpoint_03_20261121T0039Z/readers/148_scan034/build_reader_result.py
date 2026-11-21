from pathlib import Path
import json,re,csv
P=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan034')
O=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan034')
C=(P/'C.tex').read_text()
H=(P/'H.tex').read_text()
B={
'header':[190,85,2185,294],
'definition':[242,281,2075,520],
'maximal_order':[245,623,2175,921],
'quotient_display':[247,922,1834,1110],
'operation_margin':[12,816,254,1168],
'case5_text':[246,1115,2199,1337],
'case5_isom':[256,1332,1592,1426],
'pentagon_margin':[19,1206,281,1610],
'figure5':[1711,1298,1858,1443],
'case4_correction':[795,1382,1303,1518],
'case4_text':[278,1517,2195,1745],
'square_margin':[18,1618,273,1883],
'figure4':[1769,1762,1976,1951],
'case3_formula':[811,1841,1745,2054],
'case3_rewrite':[323,2063,2143,2425],
'association':[345,2423,2185,2655],
'ending':[341,2632,2118,2859],
'third_margin':[9,1870,298,2490],
'figure3':[1659,2734,1877,2927],
'foliation':[55,2832,150,2921],
'case3_est':[1520,1900,2205,2080],
'case3_opening':[272,1930,850,2070],
}
angles={'operation_margin':-42,'pentagon_margin':-44,'square_margin':-45,'third_margin':-45}
def ref(label):return f'crops/148_scan034_{label}.png'
def macro(text,name,start=0):
    a=text.index('\\'+name+'{',start); j=a+len(name)+2; lev=1
    while lev:
        if text[j]=='{':lev+=1
        elif text[j]=='}':lev-=1
        j+=1
    return text[a:j]
def macros(text,name):
    out=[];n=0
    while True:
        try:s=macro(text,name,n)
        except ValueError:break
        a=text.index(s,n);out.append(s);n=a+len(s)
    return out
cm=macros(C,'margin')
hm=macros(H,'marginal')
cf=macros(C,'figure')
hd=macros(H,'drawing')
fig5=r"""\figure{\begin{tikzpicture}[scale=.75,line cap=round,line join=round]
\draw (-.73,-.03) .. controls (-.75,.43) and (-.34,.84) .. (.08,.87)
 .. controls (.65,.93) and (.75,.45) .. (.75,-.05)
 .. controls (.77,-.58) and (.42,-.87) .. (-.05,-.88)
 .. controls (-.53,-.88) and (-.76,-.56) .. (-.73,-.03);
\draw (-.73,-.08) .. controls (-.43,-.29) and (.23,-.31) .. (.69,-.18);
\draw (-.60,.09) .. controls (-.36,.18) and (-.25,.14) .. (-.08,.18)
 .. controls (.01,.19) and (.09,.17) .. (.17,.16);
\draw (.41,.14)--(.44,.12);
\draw (.59,.07)--(.61,.02);
\foreach \x/\y in {-.57/.09,.02/.19,.59/.05,-.43/-.23,.30/-.27}
 {\fill (\x,\y) circle(1.7pt);}
\draw (-.61,-.53) .. controls (-.47,-.58) and (-.25,-.60) .. (-.08,-.60);
\draw (-.03,.86)--(-.01,.80);
\end{tikzpicture}}"""
fig4=r"""\figure{\begin{tikzpicture}[scale=.75,line cap=round,line join=round]
\draw (-.02,.89) .. controls (-.43,.87) and (-.78,.48) .. (-.80,-.01)
 .. controls (-.82,-.49) and (-.62,-.74) .. (-.47,-.80);
\draw (-.42,-.82) .. controls (-.05,-.97) and (.43,-.88) .. (.67,-.59)
 .. controls (.84,-.31) and (.81,.29) .. (.65,.58)
 .. controls (.45,.83) and (.20,.91) .. (.04,.91);
\draw (-.80,-.12) .. controls (-.44,-.33) and (.35,-.33) .. (.79,-.17);
\draw[dash pattern=on 2.6pt off 2.5pt] (-.65,.13)
 .. controls (-.25,.25) and (.30,.25) .. (.69,.08);
\foreach \x/\y in {.05/.80,-.49/-.23,.27/-.29,-.31/.20,.57/.13}
 {\fill (\x,\y) circle(1.7pt);}
\draw (-.31,.20)--(-.36,.14);
\end{tikzpicture}}"""
fig3=r"""\figure{\begin{tikzpicture}[scale=.75,line cap=round,line join=round]
\draw (-.80,-.08) .. controls (-.77,.35) and (-.38,.87) .. (-.04,.88)
 .. controls (.04,.83) and (.13,.88) .. (.22,.87)
 .. controls (.63,.84) and (.81,.39) .. (.81,-.09)
 .. controls (.82,-.53) and (.52,-.88) .. (.11,-.90)
 .. controls (-.39,-.91) and (-.78,-.61) .. (-.80,-.08);
\draw (-.79,-.23) .. controls (-.44,-.34) and (.32,-.28) .. (.80,-.08);
\draw (-.68,.05) .. controls (-.56,.06) and (-.47,.11) .. (-.39,.13);
\draw[dash pattern=on 2.1pt off 2.6pt] (-.28,.15)
 .. controls (.06,.18) and (.33,.25) .. (.47,.22);
\draw (.48,.22) .. controls (.61,.23) and (.70,.17) .. (.73,.10);
\foreach \x/\y in {-.01/.78,.11/-.80,-.02/-.28,-.57/.07,.62/.21}
 {\fill (\x,\y) circle(1.7pt);}
\draw (-.65,-.63) .. controls (-.54,-.73) and (-.40,-.74) .. (-.26,-.72);
\end{tikzpicture}}"""
circleD5=r"\tikz[baseline=(d.base)]{\node[draw,circle,inner sep=1pt] (d) {\(\mathbb D_5\)};}"
S=C
def rep(a,b):
    global S
    assert a in S,a
    S=S.replace(a,b,1)
rep(r"\deleted{\(g\) d’ordre \(5\)}",r"\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}")
rep(cm[0],r"\margin{l’opération est celle de \(\mu_\nu\) sur \(\widehat{\mathbb G}_m\)}")
rep(r"\(\mathbb D_5\)",circleD5)
rep(cf[0],fig5)
rep(r"\deleted{\(\unsure{K^g}=\operatorname{card}I^g=1\)}",r"\deleted{\(K=\operatorname{card}I^g=1\)}")
rep(cf[1],fig4)
rep(r"\deleted{\(\unsure{K}\)}",r"\deleted{\(\unsure{\Sigma|K}\)}")
rep(r"\inserted{\(=J\)} une orbite,",r"\inserted{\(=J\)} est une orbite,")
rep(r"\deleted{Le groupe total des}",r"\deleted{Le groupe total est}")
rep(r"qu’on peut \unsure{supposer|prendre} \(\mu_3\).",r"\inserted{qu’on peut supposer \(\mu_3\).}")
rep("est équivalente à celle des triangles", "est équivalente : celle des triangles")
rep(r"À \(J\) on associe",r"A \(J\) on associe")
rep(r"\unsure{pour une|en}","pour")
rep(r"\omega(J)",r"\omega(I)")
rep(r"\unsure{symétries}","symétries")
rep(cf[2],fig3)
rep(r"\mspage{33}",r"\margin{33}")
(O/'candidate.tex').write_text(S)

changes=[]
def change(place,c,h,final,ink,label,kind,ac=False,ah=False,math=False,confidence='high',**extra):
    if c is not None:assert c in C,('C snippet missing',place,c)
    if h is not None:assert h in H,('H snippet missing',place,h)
    obj=dict(place=place,c=c,h=h,final=final,ink=ink,crop=ref(label),box=B[label],confidence=confidence,kind=kind,against_c=ac,against_h=ah,math=math)
    obj.update(extra);changes.append(obj)
change('title, abbreviation gén. with raised t',r"gén.\textsuperscript{t}",r"génér\supplied{alemen}t",r"gén.\textsuperscript{t}",
       'A period follows the low gén.; the final t is raised. No following baseline r or letters of an expanded ending are present.','header','abbreviation expanded or spelling modernised',ah=True)
change('title, alg clos',r"alg clos",r"alg.\ clos",r"alg clos",
       'The g finishes with its descender and is followed by the space before clos; no abbreviation point is visible after alg.','header','abbreviation expanded or spelling modernised',ah=True)
change('definition, autom.',"autom.","automorph.","autom.",
       'After auto the low m closes the short form and is followed by a dark point; there are no rph strokes.','definition','abbreviation expanded or spelling modernised',ah=True)
change('definition, inserted G and baseline des',r"\inserted{\(G\)} des",r"$G$\add{\ des}",r"\inserted{\(G\)} des",
       'G is above groupe with a V-shaped insertion cue. The des belongs to the main baseline, not to the interline G; the full half supplies the right-hand baseline context.','definition','insertion or placement',ah=True)
change('finite-order paragraph, autom.',"autom.","automorphisme","autom.",
       'The word after tout ends at the low m and abbreviation point; the long expanded ending in H has no corresponding strokes.','maximal_order','abbreviation expanded or spelling modernised',ah=True)
change('finite-order paragraph, cancelled group before a exactement',r"\deleted{\(g\) d’ordre \(5\)}",r"\struck{$\nu$ d'ordre 5}",r"\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}",
       'A separate short down-and-up, nu-like stroke precedes a loop with a descender read as g. The horizontal cancellation crosses both and d’ordre 5; the initial stroke is not secure enough to remove doubt. This group is at the beginning of the next baseline after the live tout autom. clause.','maximal_order','omission',ac=True,ah=True,math=True,confidence='medium')
change('finite-order paragraph, cancellation and interlinear condition',r"et que \deleted{\unsure{il est}} \inserted{si l’ordre est \(\nu\)}",r"qu'il \struck{\ill{}} \add{\uncertain{l'opère}} \add{comme}",r"et que \deleted{\unsure{il est}} \inserted{si l’ordre est \(\nu\)}",
       'Above the strike one reads a short si, the tall l of l’ordre, the following order letters, est, and the terminal nu. Below it the strike obscures the middle of the cancelled il est candidate, so that doubt is retained. H’s l’opère/comme does not match the visible sequence.','maximal_order','misread word',ah=True,math=True)
change('first oblique margin',cm[0],hm[0],r"\margin{l’opération est celle de \(\mu_\nu\) sur \(\widehat{\mathbb G}_m\)}",
       'The rotated crop has the loops and descender of opération, est celle de, then mu with a lowered nu, sur, and G with lowered m. Two straight oblique strokes form a roof above G; no radical hook or horizontal radical bar occurs. No secure final point follows m.','operation_margin','misread symbol or index',ac=True,ah=True,math=True)
change('case 1, orbit notation',r"\(\mu_5(k)\)",r"$\mu_5 \cdot 1$ \uncertain{ch.}",r"\(\mu_5(k)\)",
       'The lowered 5 is followed by an opening parenthesis, a small k with an upright and right branch, and a closing curve; no separate 1 or ch. follows.','case5_text','misread symbol or index',ah=True,math=True)
change('case 1, autom.',"autom.","automorph.","autom.",
       'After the compressed autom letters a point occurs before est; no rph suffix is written.','case5_text','abbreviation expanded or spelling modernised',ah=True)
change('case 1, circle around D5',r"\(\mathbb D_5\)",r"$\mathbb{D}_5$",circleD5,
       'A continuous irregular oval encloses the doubled-stem D and lowered 5. H explicitly reports the circle in its note; C’s uncircled math omits it.','case5_text','omission',ac=True,math=True)
change('case 1, isomorphism sentence',r"À isom. près, il y a un seul tel cas.",r"(à isom.\ près, il y a un seul tel cas.)",r"À isom. près, il y a un seul tel cas.",
       'The A is large with an accent stroke above it. The sentence ends in cas and a point, without a closing parenthesis. The curved fragment at the left edge is marginal ink, not a parenthesis enclosing this sentence.','case5_isom','text not on the page',ah=True)
change('case 1, pentagon margin',cm[1],hm[1],cm[1],
       'Structure begins with a capital S; pentagonale has no surrounding quotes. The next short line reads sur followed by a serif I. The final line has parentheses around a separately quoted pentagone.','pentagon_margin','misread word',ah=True,math=True)
change('case 1, sphere drawing',cf[0],hd[0],fig5,
       'There are three marked points on the rear course and two on the solid front course. The rear course is solid from its left point to the middle point and broken farther right. The lower interior stroke starts at the left boundary and curves down then right; it is not a floating straight line. A tiny inward stub is attached to the upper contour.','figure5','drawing or diagram',ac=True,ah=True,math=True)
a=H.index(r"\struck{$K =$}"); z=H.index(r"\note{en interligne",a)
change('case 2, cancelled equation',r"\deleted{\(\unsure{K^g}=\operatorname{card}I^g=1\)}",H[a:z],r"\deleted{\(K=\operatorname{card}I^g=1\)}",
       'The first cancelled letter has K’s two arms and no superscript g before the equals sign. The cancellation continues through card, the serif I with raised g, the second equals sign, and 1. Above it, the separate replacement K^g={P} is live.','case4_correction','deletion state',ac=True,ah=True,math=True,certainty_resolution=True)
change('case 2, lequel',"lequel","laquelle","lequel",
       'The short relative word has le-, a descending q, and the final -el; it has neither the medial a nor the extra final -le sequence of laquelle.','case4_text','misread word',ah=True)
change('case 2, punctuation before the overtraced pole symbol',r"pôle : \(\unsure{\infty}\)",r"pôle, \uncertain{$\infty$}",r"pôle : \(\unsure{\infty}\)",
       'Two vertically separated ink marks follow pôle, giving a colon. The following compact looped symbol remains overtraced and doubtful; this row resolves only punctuation.','case4_text','misread symbol or index',ah=True,math=True)
change('case 2, autom.',"autom.","automorph.","autom.",
       'The low ending stops after m and a point, with no rph strokes.','case4_text','abbreviation expanded or spelling modernised',ah=True)
a=H.index(r"\mathbf{Z}/4\mathbf{Z}");z=H.index(". La catégorie",a)
change('case 2, group evaluation at k',r"\(\mathbb Z/4\mathbb Z\simeq\mu_4(k)\)",H[a:z],r"\(\mathbb Z/4\mathbb Z\simeq\mu_4(k)\)",
       'The quotient has the handwritten 4 between the two Zs, followed by the isomorphism sign. After mu with lowered 4, parentheses enclose a small k; the parenthesis contents are not illegible.','case4_text',r'readable ink left as \ill{}',ah=True,math=True)
change('case 2, square-pyramid margin',cm[2],hm[2],cm[2],
       'The first quoted word ends with the looped d and e of pyramide, without an added -al-. The second line is carrée with its accent and closing double quote.','square_margin','misread word',ah=True)
change('case 2, sphere drawing',cf[1],hd[1],fig4,
       'One filled point sits inside the upper contour and four points lie on the equator, two front and two rear. The outer contour has a small top gap and a lower-left gap. Rear strokes are separate dashes. At the left rear point only a short descending oblique stroke is secure; C’s fully specified arrowhead is replaced by that visible stroke.','figure4','drawing or diagram',ac=True,ah=True,math=True,confidence='medium')
change('case 3, Alors capitalization',"Alors","alors","Alors",
       'The initial has a tall triangular body comparable in height to the adjacent looped l; it differs from the low initial a in case 1 alors. Capitalization is the less secure part of an otherwise plain word.','case3_opening','abbreviation expanded or spelling modernised',ah=True,confidence='medium')
change('case 3, cancelled initial symbol',r"\deleted{\(\unsure{K}\)}",r"\struck{$\Sigma$}",r"\deleted{\(\unsure{\Sigma|K}\)}",
       'The surviving upper and lower horizontal limbs and central oblique make a Sigma-like outline. Overtracing across that outline prevents an unqualified identification; K is retained as the alternative.','case3_formula','misread symbol or index',ac=True,ah=True,math=True,confidence='medium')
change('case 3, insertion connector versus parenthesis',r"\inserted{donc \(K^g=\Sigma^g\)}",r"(\add{donc $K^{g} = \Sigma^{g}$,}",r"\inserted{donc \(K^g=\Sigma^g\)}",
       'The long curve rises from the space after card K^g=2 and runs under the interlinear donc K^g=Sigma^g. It is a placement connector, not an opening semantic parenthesis around the subsequent clause.','case3_formula','insertion or placement',ah=True,math=True)
change('case 3, I in the orbit complement',r"I\setminus K^g",r"K \setminus K^{g}",r"\(I\setminus K^g\)",
       'The first letter has a straight vertical stem with transverse head and foot; it lacks K’s right-hand upper and lower arms, which are plainly present in the following K^g.','case3_formula','misread symbol or index',ah=True,math=True)
a=H.index(r"$K \setminus K^{g} = J$");z=H.index(r"\struck{Le groupe",a)
change('case 3, live est',r"\inserted{\(=J\)} une orbite,",H[a:z],r"\inserted{\(=J\)} est une orbite,",
       'Below the interlinear =J is a separate compressed est: low connected e/s strokes and a terminal upward t stroke. It is followed on the same baseline by une orbite and a comma. The word is live, not part of the addition or the cancellation on the next line.','case3_est','omission',ac=True,math=True)
change('case 3, final word under the strike',r"\deleted{Le groupe total des}",r"\struck{Le groupe total est}",r"\deleted{Le groupe total est}",
       'After total the cancelled word begins with low e/s strokes and ends in a raised t with its crossing stroke. It has no initial ascender d; the horizontal cancellation passes through the complete phrase.','case3_rewrite','misread word',ac=True)
change('case 3, supposer',r"\unsure{supposer|prendre}",r"\uncertain{prendre}","supposer",
       'The word has two adjacent long descending p strokes after the low initial su-, then the rounded o/s and terminal er; prendre would not account for this paired descent.','case3_rewrite','misread word',ac=True,ah=True,certainty_resolution=True,mark_ids=['M0450'])
a=H.index(r"\uncertain{qu'on}");z=H.index(" La catégorie",a)
change('case 3, replacement phrase below the cancellation',r"qu’on peut \unsure{supposer|prendre} \(\mu_3\).",H[a:z],r"\inserted{qu’on peut supposer \(\mu_3\).}",
       'The live qu’on peut supposer mu_3 is written on a lower interlinear baseline beneath the crossed-out Le groupe total est, before the main-baseline La catégorie. Its relative placement identifies it as the replacement addition.','case3_rewrite','insertion or placement',ac=True,ah=True,math=True)
change('case 3, colon after équivalente',"équivalente à celle","équivalente : celle","équivalente : celle",
       'After équivalente there are two separated, vertically arranged short marks and no closed a body or connecting baseline; the visible punctuation is a colon.','case3_rewrite','misread symbol or index',ac=True)
change('case 3, ens without a point',r"des ens \(J\)",r"des ens.\ $J$",r"des ens \(J\)",
       'The low ens strokes are followed by clear blank space and the separate J; there is no abbreviation point in that gap.','case3_rewrite','abbreviation expanded or spelling modernised',ah=True)
change('association paragraph, unaccented A',r"À \(J\) on associe",r"A $J$ on associe",r"A \(J\) on associe",
       'The initial A has its two sloping sides but there is no accent stroke above it; the clear space above distinguishes it from the accented A in the earlier isomorphism sentence.','association','abbreviation expanded or spelling modernised',ac=True)
change('association paragraph, cancelled symbol after Sigma_J',r"\(\Sigma_J\deleted{\unsure{\Sigma}}\)",r"$\Sigma_J$ \struck{\ill{}}",r"\(\Sigma_J\deleted{\unsure{\Sigma}}\)",
       'A small angular Sigma-like form survives within several crossing loops after the live Sigma_J. It is not wholly readable: the tentative Sigma and its deletion state remain explicitly doubtful.','association','misread symbol or index',ah=True,math=True,confidence='low')
change('association paragraph, ens des deux pôles',"ens des deux pôles",r"\ill{} un des deux pôles","ens des deux pôles",
       'The low initial sequence has the linked e/n and final s of ens; des follows separately before the clearly written deux pôles. No separate un follows a lost word.','association','misread word',ah=True)
change('association paragraph, pour corr.',r"\unsure{pour une|en}",r"pour \uncertain{une}","pour",
       'The p descender is followed by the low o/u/r sequence; a blank separates its terminal r from the initial c of corr. There is no intervening une.','association','text not on the page',ac=True,ah=True,certainty_resolution=True,mark_ids=['M0452'])
change('ending, omega argument and absence of underline',r"l’ens \(\omega(J)\)",r"l'ens.\ $\underline{\omega}(J)$",r"l’ens \(\omega(I)\)",
       'Inside the parentheses the letter has a straight upright and distinct head and foot serifs, giving I rather than the bent-hook J written later on the same line. Omega has its own joined lower strokes, with no independent underline. No point is visible after ens.','ending','misread symbol or index',ac=True,ah=True,math=True)
change('ending, autom.',"autom.","automorph.","autom.",
       'The final group sentence has the same compressed autom and terminal point, without an rph extension.','ending','abbreviation expanded or spelling modernised',ah=True)
a=hm[3].index('«');z=hm[3].index(r"\uncertain{symétries}")
hfirst=hm[3][a:z]
cfirst=r"\unsure{Partition} \(2\) et \(3\) (par ordre de \unsure{cardinaux|valeurs} ou"
change('third oblique margin, recoverable structure with two retained word doubts',cfirst,hfirst,cfirst,
       'The separate numerals have the angled lower foot of 2 and the double-bend form of 3. Parentheses, par ordre de, and ou are visible. The first word begins with a p/P-like downstroke, but its linked middle strokes remain uncertain. The later disputed word has a raised mark and a looped ascender; neither cardinaux nor valeurs can be certified.','third_margin','misread word',ah=True,math=True,confidence='low')
change('third oblique margin, symétries',r"\unsure{symétries}",r"\uncertain{symétries}","symétries",
       'The long y descender, the paired m humps, the accent over e, the crossed t and dotted i, and the final es are all distinguishable on the rotated crop.','third_margin','misread word',ac=True,ah=True,certainty_resolution=True,mark_ids=['M0456'])
change('case 3, sphere drawing',cf[2],hd[2],fig3,
       'Two poles lie inside the contour, with one filled point on the tilted solid front equator and two on the broken rear course. The rear course stops short of both outer boundaries. A short lower-left inner retrace follows the contour and is omitted by both witnesses.','figure3','drawing or diagram',ac=True,ah=True,math=True)
change('bottom-left foliation',r"\mspage{33}",None,r"\margin{33}",
       'Two open right-facing double curves give 33. This lower-left number is separate from the authorial 1 at the head; its hand is not assigned. The C-to-final macro change alone is not counted as a textual change.','foliation','omission',ah=True)

decisions=[]
def decision(i,d,reading,ink,label,confidence):
    decisions.append(dict(id=i,decision=d,reading=reading,ink=ink,crop=ref(label),box=B[label],confidence=confidence))
decision('M0448','undecided',r"\unsure{de car. \(0\)}",'The de region is overtraced; the later car. and small rounded 0 are more visible, but they do not resolve the entire marked phrase.','header','low')
decision('M0449','undecided',r"\(\unsure{\infty}\)",'The small symbol after the colon has intersecting loops inside heavier retracing. An infinity-like reading is plausible but the overtraced left component is not secure.','case4_text','medium')
decision('M0450','first','supposer','Two successive descending p strokes decide supposer over prendre, followed by the low rounded ending.','case3_rewrite','high')
decision('M0451','undecided',r"\(P_J\subset\Sigma_J^{\unsure{g}}\)",'The small right-hand cluster contains a loop and long descending stroke, but the relative position of g and the lower J cannot be isolated securely. The whole inclusion was inspected.','association','low')
decision('M0452','other','pour','The p descender and low our strokes lead directly, after a blank, to corr.; no une or separate en is present.','association','high')
decision('M0453','undecided',r"\(\unsure{k|K}=\mathbb C\)",'The first stem is overtraced, and its joined right branches do not distinguish upper from lower case securely. The equals sign, C, and parenthesis are clear.','ending','medium')
decision('M0454','undecided',r"\unsure{Partition}",'The initial downstroke is p/P-like, while the linked low strokes and two tall peaked/crossed forms in the rest of the word do not isolate every letter.','third_margin','low')
decision('M0455','undecided',r"\unsure{cardinaux|valeurs}",'A low opening is followed by a raised mark and a looped ascender; the compressed remaining sequence cannot certify either proposed word.','third_margin','low')
decision('M0456','first','symétries','The y descender, m humps, accented e, crossed t, dotted i, and final es remain individually visible.','third_margin','high')

inventory=[]
def inv(element,kind,position,reading,hand='main manuscript hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=reading,sheet_kind='text',hand=hand,transcribed='yes'))
inv('authorial_page_number','margin note','top centre',r'\mspage{1}')
inv('title','text','two lines at head','Systèmes spéciaux de cinq points sur une sphère complexe')
inv('title_cancelled_courbe','deletion','second title line',r'\deleted{\unsure{courbe}}')
inv('definition','text','below title, four baselines','Ce sont les systèmes')
inv('definition_G','insertion','above groupe',r'\inserted{\(G\)}')
inv('maximal_order','text','upper middle, five baselines',r'Soit \(g\in G\) d’ordre maximal')
inv('cancelled_order_clause','deletion','after Notons que',r'\deleted{l’ordre de \(g\ne1\) est}')
inv('cancelled_order5','deletion','start of following baseline',r'\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}')
inv('cancelled_il_est','deletion','after et que',r'\deleted{\unsure{il est}}')
inv('inserted_order_condition','insertion','above cancelled il est',r'\inserted{si l’ordre est \(\nu\)}')
inv('orbit_display','display','below free-action sentence',r'\(K=K^g\amalg\text{orbites d’ordre }\nu,\quad\text{donc }2\leq\nu\leq5\)')
inv('operation_margin','margin note','upper left, oblique',r'l’opération est celle de \(\mu_\nu\) sur \(\widehat{\mathbb G}_m\)')
inv('case1','text','middle, three baselines',r'\textcircled{1} \(\nu=5\), alors \(K\) est une orbite')
inv('case1_circled_D5','display','end of case-1 second baseline',circleD5)
inv('pentagon_margin','margin note','left of case 1, oblique',cm[1])
inv('sphere5','drawing','right of case-1 last baseline','oval contour; three rear and two front points; lower-left interior stroke')
inv('case2','text','middle-lower, five baselines',r'\textcircled{2} \(\nu=4\) alors')
inv('case2_cancelled_equation','deletion','case-2 first baseline',r'\deleted{\(K=\operatorname{card}I^g=1\)}')
inv('case2_inserted_equation','insertion','above cancelled equation',r'\inserted{\(K^g=\{P\}\)}')
inv('square_margin','margin note','left of case 2, oblique',cm[2])
inv('sphere4','drawing','right of square-category sentence','upper pole inside oval; four equator points; rear dashes and short stub')
inv('case3','text','lower portion, eight main baselines',r'\textcircled{3} \(\nu=3\), Alors')
inv('case3_cancelled_symbol','deletion','after Alors',r'\deleted{\(\unsure{\Sigma|K}\)}')
inv('case3_donc','insertion','above card K^g=2 and et',r'\inserted{donc \(K^g=\Sigma^g\)}')
inv('case3_J','insertion','above the live est',r'\inserted{\(=J\)}')
inv('case3_live_est','text','baseline after I minus K^g',r'est une orbite,')
inv('case3_cancelled_group','deletion','start of next baseline',r'\deleted{Le groupe total est}')
inv('case3_replacement','insertion','below cancelled group phrase',r'\inserted{qu’on peut supposer \(\mu_3\).}')
inv('association','text','last four baselines',r'A \(J\) on associe \(\Sigma_J\)')
inv('association_cancelled_symbol','deletion','after Sigma_J',r'\deleted{\(\unsure{\Sigma}\)}')
inv('partition_margin','margin note','left of case 3, oblique',r'\unsure{Partition} \(2\) et \(3\) (par ordre de \unsure{cardinaux|valeurs} ou symétries)')
inv('bitetrahedron_margin','margin note','below the preceding oblique note',cm[4])
inv('sphere3','drawing','bottom right','two poles inside oval; two rear and one front equator points; lower-left retrace')
inv('foliation','margin note','bottom left',r'\margin{33}','unassigned foliation hand')

unresolved=[
dict(place='title, cancelled courbe',reading=r'\deleted{\unsure{courbe}}',issue='The strike obscures the middle letters; beginning c, ascender b, and final e support but do not fully certify courbe.',alternatives=['courbe'],confidence='low'),
dict(place='title, characteristic phrase',reading=r'\unsure{de car. \(0\)}',issue='The opening de is overtraced; the more legible remainder does not certify the whole phrase.',alternatives=[r'de car. \(0\)'],confidence='low'),
dict(place='cancelled order-5 group, initial stroke',reading=r'\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}',issue='An extra nu-like stroke precedes g under the cancellation; its identity is not secure.',alternatives=[r'\nu','unidentified stroke'],confidence='medium'),
dict(place='cancelled il est',reading=r'\deleted{\unsure{il est}}',issue='The cancellation runs through the middle and terminal letters. The original doubt remains.',alternatives=['il est'],confidence='low'),
dict(place='case 2, pole symbol',reading=r'\(\unsure{\infty}\)',issue='Compact intersecting loops are overtraced, especially at the left.',alternatives=[r'\infty'],confidence='medium'),
dict(place='case 3, cancelled initial symbol',reading=r'\deleted{\(\unsure{\Sigma|K}\)}',issue='A Sigma-like angular outline survives, but the crossed strokes prevent an unqualified identification.',alternatives=[r'\Sigma','K'],confidence='medium'),
dict(place='association, cancelled symbol after Sigma_J',reading=r'\(\Sigma_J\deleted{\unsure{\Sigma}}\)',issue='Several crossing loops obscure the small angular symbol after the live Sigma_J.',alternatives=[r'\Sigma'],confidence='low'),
dict(place='association, inclusion formula exponent',reading=r'\(P_J\subset\Sigma_J^{\unsure{g}}\)',issue='The small loop and descending stroke on the right are not securely separable into exponent g and subscript J.',alternatives=[r'\Sigma_J^g',r'\Sigma_J'],confidence='low'),
dict(place='ending, field letter',reading=r'\(\unsure{k|K}=\mathbb C\)',issue='An overtraced stem with joined right branches does not securely distinguish case.',alternatives=['k','K'],confidence='medium'),
dict(place='third margin, initial word',reading=r'\unsure{Partition}',issue='The initial is p/P-like but the linked middle strokes do not certify the proposed word.',alternatives=['Partition'],confidence='low'),
dict(place='third margin, word before ou symétries',reading=r'\unsure{cardinaux|valeurs}',issue='The raised mark, looped ascender, and low ending do not securely distinguish the two witness candidates.',alternatives=['cardinaux','valeurs'],confidence='low'),
]
notes=[
dict(id='148034_N01',text='A portrait handwritten leaf on listing paper. The authorial number 1 is at the top centre; a separate lower-left 33 is preserved as unassigned foliation. No date is written on this leaf. H’s opening editorial account is not manuscript text.'),
dict(id='148034_C01',text='The page defines special five-point systems (Sigma,K) by the existence of a nontrivial automorphism and announces a classification by the automorphism group. This definition is transcribed, not independently established.'),
dict(id='148034_C02',text='The live finite-order sentence says that every finite-order automorphism of Sigma has exactly two fixed points. Taken literally this includes the identity, so it requires a nontriviality qualification; the earlier g≠1 lies in cancelled text. The identity counterexample was checked, and no qualification was inserted into the transcription.'),
dict(id='148034_C03',text='The displayed decomposition into fixed points and free nu-orbits gives 5=a+b nu with 0≤a≤2 and b≥1. This yields 2≤nu≤5 for the nontrivial automorphism under discussion and the fixed-point counts 0,1,2 for nu=5,4,3 respectively. The bound and integer possibilities were checked.'),
dict(id='148034_C04',text='For nu=5 the manuscript gives the orbit mu_5(k), the circled group D_5, and uniqueness up to isomorphism, with a pentagonal structure. The group identification and categorical assertion were transcribed but not independently proved.'),
dict(id='148034_C05',text='For nu=4 the revised equation is K^g={P}; the complement is one orbit, the pole is designated by an overtraced infinity-like symbol, and the full group is written Z/4Z ≃ mu_4(k). The category is compared with oriented squares. The orbit count was checked under C03; the full group and categorical assertions were not separately proved.'),
dict(id='148034_C06',text='For nu=3 the page gives card K^g=2, inserts K^g=Sigma^g and =J, and identifies the remaining orbit with mu_3. It compares the category with combinatorial triangles/Ens(3), associates Sigma_J and poles to J, and writes D_3. The orbit count was checked under C03; the categorical construction and automorphism group were not independently proved.'),
dict(id='148034_N02',text='Clear serif I is retained in permutation de I, the complements I minus {P} and I minus K^g, the pentagon margin, and omega(I). K and J are used elsewhere in the same discussion. These may reflect notational shifts or slips; they were not silently regularised.'),
dict(id='148034_N03',text='The first margin has a roof accent over G_m. Its role is not inferred from the mathematical setting. The additional nu-like stroke in the cancelled order-5 group, the cancelled symbols, the pole symbol, the exponent cluster, the field-letter case, and two margin words retain explicit uncertainty.'),
dict(id='148034_N04',text='The replacement qu’on peut supposer mu_3 is written below the crossed-out Le groupe total est. The curved leader from card K^g=2 to the inserted donc clause is not set as a parenthesis. The live est une orbite is included.'),
]
checks=[
dict(statement_id='148034_C02',date='2026-11-20',who='GPT-6 Astra Pro, reader B',type='formal certificate',outcome='Counterexample to the unrestricted live wording: the identity has finite order 1 and fixes every point of Sigma, rather than exactly two. The statement holds only after excluding the identity in this respect; the text was left unchanged.',reader='B',run='SP82_C13_148',reasoning_effort='not exposed'),
dict(statement_id='148034_C03',date='2026-11-20',who='GPT-6 Astra Pro, reader B',type='formal certificate',outcome='Given the stated free-orbit decomposition and at most two fixed points, write 5=a+b nu with a≤2. Then b≥1, hence nu≤5; nontriviality gives nu≥2. This establishes the displayed bound without changing the ink.',reader='B',run='SP82_C13_148',reasoning_effort='not exposed'),
dict(statement_id='148034_C03',date='2026-11-20',who='GPT-6 Astra Pro, reader B',type='computation',outcome='Python enumeration of nu=2,...,5, a=0,1,2 and positive b satisfying a+b nu=5 returned (nu,a,b)=(2,1,2),(3,2,1),(4,1,1),(5,0,1). Thus the fixed-point counts in the three listed cases agree with the displayed decomposition.',reader='B',run='SP82_C13_148',reasoning_effort='not exposed'),
]
hand_log=[
dict(habit='Clear capital I has a straight stem with head and foot serifs; J has a bent or hooked lower end.',pages=[34],holds_at_every_observed_occurrence=True,scope='Unobscured I and J occurrences on this leaf; the overtraced index cluster is excluded.',witness_effect='C and H both read omega(J), but the crop shows omega(I); H also reads K in the case-3 complement where the serif I is clear.'),
dict(habit='A compressed est may be almost horizontal, ending in a short upward stroke.',pages=[34],holds_at_every_observed_occurrence=False,scope='The live est below =J in case 3 is especially compressed; other est forms vary.',witness_effect='C omitted the live est after I minus K^g; the separate =J is interlinear.'),
dict(habit='The two p letters of supposer form adjacent long descenders.',pages=[34],holds_at_every_observed_occurrence=True,scope='One observed supposer on this leaf, with both descenders visible.',witness_effect='This resolves C’s supposer|prendre in favour of supposer and rejects H’s prendre candidate.'),
]
notation=[
dict(form=r'\(\Sigma,K\)',observation='Sigma is the sphere/projective line and K is explicitly a five-element subset on this page.',place='definition'),
dict(form=r'\(G\)',observation='G is inserted as the name of the automorphism group of the pair.',place='definition'),
dict(form=r'\(I\)',observation='A clear serif I occurs in places where the discussion elsewhere uses K or J; the actual letter is retained.',place='maximal-order sentence, complements, margin, omega argument'),
dict(form=r'\(\widehat{\mathbb G}_m\)',observation='The marginal multiplicative-group symbol carries a separately drawn roof; no meaning for that roof is supplied.',place='first oblique margin'),
dict(form=r'\(\mathbb D_5\)',observation='D with lowered 5 is encircled; the later D_3 is not encircled.',place='case 1 group and case 3 ending'),
]
abbreviations=[
dict(form=r'gén.\textsuperscript{t}',expansion='généralement'),
dict(form='alg',expansion='algébriquement'),
dict(form='car.',expansion='caractéristique'),
dict(form='autom.',expansion='automorphisme / automorphismes'),
dict(form='i.e.',expansion='id est'),
dict(form='pts',expansion='points'),
dict(form='OPS',expansion='on peut supposer'),
dict(form='isom.',expansion='isomorphisme'),
dict(form='ens',expansion='ensemble / ensembles'),
dict(form='card',expansion='cardinal'),
dict(form='corr.',expansion='correspondance'),
dict(form='or.',expansion='orientations'),
]

second=[]
def sb(key,kind,box,reading,rotation=None):
    d=dict(box='148034_'+key,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading)
    if rotation is not None:d['rotation']=rotation
    second.append(d)
sb('top_number','handwritten number',[1060,85,1128,137],r'\mspage{1}')
sb('title_abbrev','C/H different word',[1860,123,2168,191],r'gén.\textsuperscript{t}')
sb('title_cancel','deletion',[505,194,748,275],r'\deleted{\unsure{courbe}}')
sb('title_alg','C/H different word',[1561,204,1704,272],'alg clos')
sb('title_characteristic','doubtful formula',[1864,190,2167,285],r'\unsure{de car. \(0\)}')
sb('definition_count','handwritten number',[1571,294,1785,366],r'\(\operatorname{card}K=5\)')
sb('definition_autom','C/H different word',[594,383,824,431],'autom.')
sb('definition_G','insertion',[1868,347,1979,421],r'\inserted{\(G\)}')
sb('definition_identity','handwritten number',[1583,464,1759,526],r'à \(1\)')
sb('cancelled_order','deletion',[568,758,1059,829],r'\deleted{l’ordre de \(g\ne1\) est}')
sb('max_autom','C/H different word',[1257,774,1528,828],'autom.')
sb('cancelled_order5','deletion',[248,815,598,904],r'\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}')
sb('cancelled_ilest','deletion',[1587,858,1869,906],r'\deleted{\unsure{il est}}')
sb('order_condition','insertion',[1550,829,2082,907],r'\inserted{si l’ordre est \(\nu\)}')
sb('quotient_display','handwritten number',[327,1010,1504,1100],r'\(K=K^g\amalg\text{orbites d’ordre }\nu,\quad\text{donc }2\leq\nu\leq5\)')
sb('operation_note','margin note',[12,816,254,1168],r'l’opération est celle de \(\mu_\nu\) sur \(\widehat{\mathbb G}_m\)',-42)
sb('case1_number_order','handwritten number',[246,1120,495,1240],r'\textcircled{1} \(\nu=5\)')
sb('case1_orbit','handwritten number',[2057,1120,2199,1223],r'\(\mu_5(k)\)')
sb('case1_action','handwritten number',[360,1233,959,1325],r'de \(\mu_5\) opérant sur \(\mathbb P^1_k\)')
sb('case1_autom_D5','handwritten number',[1742,1204,2197,1337],r'autom. est '+circleD5)
sb('case1_isom','C/H different word',[285,1335,1579,1417],r'À isom. près, il y a un seul tel cas.')
sb('pentagon_note','margin note',[19,1206,281,1610],cm[1],-44)
sb('sphere5','drawing',[1711,1298,1858,1443],fig5)
sb('case2_number_order','handwritten number',[251,1434,522,1547],r'\textcircled{2} \(\nu=4\)')
sb('case2_deleted','deletion',[819,1431,1294,1515],r'\deleted{\(K=\operatorname{card}I^g=1\)}')
sb('case2_replacement','insertion',[862,1382,1065,1447],r'\inserted{\(K^g=\{P\}\)}')
sb('case2_mu4','handwritten number',[828,1539,926,1604],r'\(\mu_4\)')
sb('case2_relative_action','C/H different word',[1106,1518,1475,1612],r'lequel \(\mu_4\)')
sb('case2_pole','doubtful formula',[283,1642,629,1728],r'pôle : \(\unsure{\infty}\)')
sb('case2_group','handwritten number',[1721,1621,2195,1736],r'autom. est \(\mathbb Z/4\mathbb Z\simeq\mu_4(k)\)')
sb('square_note','margin note',[18,1618,273,1883],cm[2],-45)
sb('sphere4','drawing',[1769,1762,1976,1951],fig4)
sb('case3_number_order_Alors','handwritten number',[282,1973,736,2056],r'\textcircled{3} \(\nu=3\), Alors')
sb('case3_deleted_symbol','deletion',[830,1954,917,2032],r'\deleted{\(\unsure{\Sigma|K}\)}')
sb('case3_fixed_count','handwritten number',[921,1945,1209,2035],r'\(\operatorname{card}K^g=2\)')
sb('case3_donc','insertion',[1146,1850,1449,1921],r'\inserted{donc \(K^g=\Sigma^g\)}')
sb('case3_I','C/H different word',[1400,1935,1547,2007],r'\(I\setminus K^g\)')
sb('case3_J','insertion',[1565,1907,1664,1954],r'\inserted{\(=J\)}')
sb('case3_est','omission',[1572,1953,2125,2005],'est une orbite,')
sb('case3_struck_group','deletion',[330,2068,981,2157],r'\deleted{Le groupe total est}')
sb('case3_replacement','insertion',[347,2122,1129,2247],r'\inserted{qu’on peut supposer \(\mu_3\).}')
sb('case3_colon','C/H different word',[829,2227,1438,2343],'équivalente : celle')
sb('case3_Ens_count','handwritten number',[1220,2358,2141,2420],r'\(\mathrm{Ens}(3)\) des ens \(J\) de card \(3\)')
sb('association_A','C/H different word',[349,2458,961,2541],r'A \(J\) on associe')
sb('association_deleted_symbol','deletion',[1060,2451,1215,2520],r'\deleted{\(\unsure{\Sigma}\)}')
sb('association_inclusion','doubtful formula',[1888,2433,2184,2515],r'\(P_J\subset\Sigma_J^{\unsure{g}}\)')
sb('association_ens','C/H different word',[349,2618,630,2655],'ens des')
sb('association_pour','C/H different word',[1426,2569,1703,2629],'pour corr.')
sb('association_1to1','handwritten number',[1731,2562,1873,2622],r'\(1\)-\(1\)')
sb('ending_omega','doubtful formula',[384,2682,822,2764],r'l’ens \(\omega(I)\)')
sb('ending_field','doubtful formula',[1431,2648,1597,2713],r'\(\unsure{k|K}=\mathbb C\)')
sb('ending_group','handwritten number',[350,2763,1009,2857],r'autom. est \(\mathbb D_3\)')
sb('partition_note','margin note',[9,1870,298,2307],r'\unsure{Partition} \(2\) et \(3\) (par ordre de \unsure{cardinaux|valeurs} ou symétries)',-45)
sb('bitetrahedron_note','margin note',[9,2261,180,2490],cm[4],-45)
sb('sphere3','drawing',[1659,2734,1877,2927],fig3)
sb('folio','handwritten number',[65,2842,143,2912],r'\margin{33}')

# Every supplied difference row is explicitly reviewed. Tokenizer-only TeX
# wrappers and H editorial matter receive no artificial textual-change row.
diffs=list(csv.DictReader((P/'differences.tsv').open(),delimiter='\t'))
review={}
def dr(rows,status,reading,labels,note):
    for n in rows:
        review[n]=dict(source_row=n,status=status,reading=reading,crops=[ref(x) for x in labels],note=note)
dr([375,376],'editorial_only','',['header','foliation'],'H’s introductory editorial account is excluded; actual top1 and lower-left33 are separately inventoried.')
dr([377,378],'C_confirmed',r'gén.\textsuperscript{t}; alg clos',['header'],'Raised t and no point after alg; H expands or punctuates beyond the ink.')
dr([391],'C_confirmed','autom.',['definition'],'Abbreviation ends after m and point.')
dr([396],'C_confirmed',r'\inserted{\(G\)} des',['definition'],'G is interlinear; des is on the baseline.')
dr([406],'editorial_only',r'\(I\)',['maximal_order'],'The serif I is retained. H’s sic note is editorial, not source ink.')
dr([410,413],'other_reading',r'\deleted{\(\unsure{\nu}\,g\) d’ordre \(5\)}',['maximal_order'],'Preserve extra uncertain nu-like stroke and the placement after the live finite-order clause.')
dr([411],'C_confirmed','autom. d’ordre',['maximal_order'],'H expands the abbreviated autom.')
dr([414,415],'C_confirmed',r'et que \deleted{\unsure{il est}} \inserted{si l’ordre est \(\nu\)}',['maximal_order'],'The inserted condition is readable; cancelled il est remains doubtful.')
dr([420,421],'macro_only',r'2\leq\nu\leq5',['quotient_display'],'Both inequalities are present; H uses a different less-or-equal macro omitted by the token comparison.')
dr(list(range(422,427)),'other_reading',r'l’opération est celle de \(\mu_\nu\) sur \(\widehat{\mathbb G}_m\)',['operation_margin'],'Readable marginal prose and roof accent, no radical and no secure final period.')
dr([427],'macro_only',r'\textcircled{1}',['case5_text'],'Circled case number; parentheses in H’s case label are not a different word.')
dr([432],'C_confirmed',r'\(\mu_5(k)\)',['case5_text'],'Parentheses contain k; no dot1 or ch. follows.')
dr([437],'C_confirmed','autom.',['case5_text'],'Abbreviation is not expanded.')
dr([439,440],'H_confirmed',circleD5,['case5_text'],'The D5 circle described in H’s note is reproduced; C omitted it.')
dr([441],'C_confirmed','À isom. près, il y a un seul tel cas.',['case5_isom'],'No parentheses enclose this sentence.')
dr([442,443,444,445],'C_confirmed',cm[1],['pentagon_margin','figure5'],'The margin continues sur I (quoted pentagone). The sphere has three rear and two front points; H’s counts are reversed. TikZ is retained with stroke corrections.')
dr([446],'C_confirmed',r'\(\nu=4\) alors',['case4_correction'],'C’s lack of an added comma after nu=4 is retained from the native half.')
dr([448,450,451],'other_reading',r'\deleted{\(K=\operatorname{card}I^g=1\)} \inserted{\(K^g=\{P\}\)}',['case4_correction'],'Initial K has no raised g; the strike spans the entire equation; the replacement is interlinear.')
dr([456],'C_confirmed','lequel',['case4_text'],'No extra -le ending or a of laquelle.')
dr([460],'C_confirmed',r'pôle : \(\unsure{\infty}\)',['case4_text'],'Colon is secure; the overtraced infinity-like symbol remains doubtful.')
dr([462],'C_confirmed','autom.',['case4_text'],'H expands the abbreviation.')
dr([464],'C_confirmed',r'\(\mathbb Z/4\mathbb Z\simeq\mu_4(k)\)',['case4_text'],'The parenthesised k is visible.')
dr([465,466,467,468],'other_reading',cm[2]+'\n'+fig4,['square_margin','figure4'],'Pyramide carrée is quoted. Five points and contour gaps are reproduced; the short rear-point stroke is not enlarged into an inferred arrowhead.')
dr([470],'undecided',r'\deleted{\(\unsure{\Sigma|K}\)}',['case3_formula'],'Sigma-like outline but overtraced; no forced resolution.')
dr([472,473,474],'C_confirmed',r'\(\operatorname{card}K^g=2\), \inserted{donc \(K^g=\Sigma^g\)}',['case3_formula'],'The long curve is an insertion connector, not an opening parenthesis.')
dr([475],'C_confirmed',r'\(I\setminus K^g\)',['case3_formula'],'First letter has I’s head and foot serifs.')
dr([476,477,478],'other_reading',r'\(I\setminus K^g\) \inserted{\(=J\)} est une orbite,',['case3_formula','case3_est'],'=J is interlinear; est is live on the baseline and was omitted by C; no closing parenthesis is written.')
dr([479],'H_confirmed',r'\deleted{Le groupe total est}',['case3_rewrite'],'The final word has low e/s plus a tall t, not initial d.')
dr([480,481,482],'C_first_reading_resolved',r'\inserted{qu’on peut supposer \(\mu_3\).}',['case3_rewrite'],'Paired p descenders decide supposer; the whole phrase is below the cancellation.')
dr([483],'H_confirmed','équivalente : celle',['case3_rewrite'],'Two separated marks form a colon.')
dr([486],'C_confirmed',r'des ens \(J\)',['case3_rewrite'],'No point follows ens.')
dr([490],'H_confirmed',r'A \(J\) on associe',['association'],'No accent is drawn above the A.')
dr([493],'undecided',r'\(\Sigma_J\deleted{\unsure{\Sigma}}\)',['association'],'A tentative angular Sigma survives under crossed loops; retain doubt.')
dr([496],'C_confirmed','ens des deux pôles',['association'],'The low word is ens, not un after an illegible word; exponent uncertainty remains separately recorded.')
dr([499,500],'other_reading','pour corr.',['association'],'The visible pour is directly followed by corr.; there is no une.')
dr([502],'macro_only',r'\(1\)-\(1\)',['association'],'One horizontal dash connects the two handwritten 1s; TeX hyphen-length coding is not a different reading.')
dr([504,505],'other_reading',r'l’ens \(\omega(I)\)',['ending'],'Serif I inside parentheses; no separate omega underline and no point after ens.')
dr([508,509],'undecided',r'\(\unsure{k|K}=\mathbb C\)',['ending'],'The letter is overtraced; neither case is forced.')
dr([510],'C_confirmed','autom.',['ending'],'The short form is retained.')
dr([512,513],'partly_resolved',r'\unsure{Partition} \(2\) et \(3\) (par ordre de \unsure{cardinaux|valeurs} ou symétries)',['third_margin','figure3'],'Numerals and symétries are readable; the initial and medial words retain doubt. The separate quoted bitétraèdre and complete drawing are retained.')
for row in diffs:
    n=int(row['source_row'])
    if n not in review:
        review[n]=dict(source_row=n,status='macro_only',reading='',crops=[],note='Reviewed against the complete page: math delimiters, TeX spacing, apostrophe encoding, or line wrapping only; no independent ink difference.')
    review[n]['c']=row['witness C']
    review[n]['h']=row['witness H']
differences_review=[review[int(x['source_row'])] for x in diffs]
result=dict(
scan=34,reader='B',model='GPT-6 Astra Pro',reasoning_effort='not exposed',run='SP82_C13_148',
lines_read=50,
lines_read_breakdown=dict(main_prose_baselines=27,display_baselines=1,oblique_margin_baselines=14,interlinear_addition_baselines=6,pagination=2,method='Physical line accounting; cancelled matter sharing a baseline is included with that baseline. Three drawings were independently read and their points recounted, not counted as prose lines.'),
changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second,differences_review=differences_review,
reading_procedure=dict(whole_page_views=1,native_half_views=[1,1],evidence_crop_count=22,crops=[dict(label=k,crop=ref(k),box=v,rotation=angles.get(k,0)) for k,v in B.items()],crop_provenance='Reader B made21 crops once each; root made the first complete est-passage crop. Reader B viewed all22 saved crops. Native-size JPEG encodings were used for display transport only; the evidence PNGs and original rectangles are preserved.',no_ocr=True,no_web=True,no_tex_compilation=True,all_C_deletions_and_insertions_audited=True,all_supplied_marks_decided=True,all_supplied_difference_rows_reviewed=True)
)

# Final shared review: retain the crossed initial letter as a doubt, and make
# the drawn lower stroke meet the sphere contour exactly.
old_cancel=r"\deleted{\(K=\operatorname{card}I^g=1\)}"
new_cancel=r"\deleted{\(\unsure{K|\Sigma}=\operatorname{card}I^g=1\)}"
new_fig5=fig5.replace(
r".. controls (-.53,-.88) and (-.76,-.56) .. (-.73,-.03);",
r".. controls (-.39,-.89) and (-.60,-.73) .. (-.68,-.53)"+"\n"+
r" .. controls (-.74,-.34) and (-.76,-.16) .. (-.73,-.03);"
).replace(r"\draw (-.61,-.53)",r"\draw (-.68,-.53)")
S=S.replace(old_cancel,new_cancel).replace(fig5,new_fig5)
def apply_final_strings(x):
    if isinstance(x,str):return x.replace(old_cancel,new_cancel).replace(fig5,new_fig5)
    if isinstance(x,list):return [apply_final_strings(v) for v in x]
    if isinstance(x,dict):return {k:apply_final_strings(v) for k,v in x.items()}
    return x
result=apply_final_strings(result)
for row in result['changes']:
    if row['place']=='case 2, cancelled equation':
        row['confidence']='medium'
        row.pop('certainty_resolution',None)
        row['ink']='The initial crossed form has no separate superscript g before the equals sign. Its diagonal and horizontal strokes are entangled, so K remains a tentative first reading and Sigma an alternative. The cancellation itself continues through the complete card I^g=1 equation. The distinct K^g={P} above is live.'
result['unresolved'].insert(4,dict(
place='case 2, cancelled initial letter',
reading=new_cancel,
issue='The crossed and entangled initial cannot securely be separated into both K arms; a Sigma-like outline remains possible. No separate superscript g is visible before the equals sign.',
alternatives=['K',r'\Sigma'],confidence='medium'))
for row in result['differences_review']:
    if row['source_row'] in [448,450,451]:
        row['status']='partly_resolved'
        row['note']='No separate superscript g follows the initial crossed letter; K|Sigma remains doubtful. The strike spans the whole equation, and K^g={P} is the interlinear replacement.'
for e in result['checks']:
    if e['type']=='formal certificate':e['type']='targeted proof check'
    elif e['type']=='computation':e['type']='computation or formal certificate'
    e['who']='GPT-6 Astra Pro; effort not exposed; run SP82_C13_148; reader B'
root_event=json.loads(Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/reviews/root_check_034.json').read_text())
result['checks'].append(root_event)
for n in result['notes']:
    if n['id']=='148034_C03':
        n['text']='Conditional on the page’s stated two-fixed-point bound and free nonfixed-orbit premise for the nontrivial g, write 5=a+b nu with 0≤a≤2 and b≥1. This yields 2≤nu≤5 and fixed-point counts 0,1,2 for nu=5,4,3 respectively. Reader B checked the bound and enumerated the integer possibilities; this is not an independent proof of the fixed-point premise.'
result['notes'].append(dict(id=root_event['statement_id'],text='Root independently checked the same orbit arithmetic, conditional on the page’s stated two-fixed-point and free-orbit premises. This confirms the counts for nu=5,4,3 without emending any I/K letters.'))

# Coordinate audit uses the already viewed evidence pixels, not additional crops.
coord={
'title_abbrev':[2000,153,2166,249],
'title_cancel':[525,212,711,264],
'title_alg':[1678,224,1860,294],
'title_characteristic':[1935,221,2153,294],
'definition_count':[1479,282,1738,364],
'definition_autom':[565,378,783,437],
'definition_identity':[1620,473,1763,530],
'max_autom':[1281,774,1518,831],
'cancelled_order5':[245,812,603,912],
'cancelled_ilest':[1360,850,1870,914],
'quotient_display':[350,1010,1469,1100],
'case1_action':[280,1233,959,1337],
'case1_autom_D5':[1705,1204,2197,1337],
'case2_mu4':[846,1550,939,1634],
'case2_pole':[278,1645,626,1745],
'case2_group':[1410,1621,2195,1740],
'case3_fixed_count':[921,1945,1220,2035],
'case3_donc':[1140,1842,1452,1926],
'case3_J':[1584,1895,1664,1942],
'case3_struck_group':[330,2068,981,2168],
'case3_replacement':[377,2120,1110,2252],
'case3_colon':[818,2215,1448,2344],
'case3_Ens_count':[1215,2302,2143,2415],
'association_deleted_symbol':[1055,2444,1252,2550],
'association_inclusion':[1888,2424,2184,2515],
'association_1to1':[1788,2553,1886,2620],
'ending_field':[1428,2638,1605,2706],
'bitetrahedron_note':[20,2225,260,2490],
}
for box in result['second_boxes']:
    key=box['box'].replace('148034_','',1)
    if key in coord:
        box['x0'],box['y0'],box['x1'],box['y1']=coord[key]
    if key=='cancelled_ilest':
        box['reading']=r'et que \deleted{\unsure{il est}}'
    if key=='association_deleted_symbol':
        box['kind']='doubtful formula'
        box['reading']=r'\(\Sigma_J\deleted{\unsure{\Sigma}}\)'
(O/'candidate.tex').write_text(S)

(O/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(candidate=str(O/'candidate.tex'),result=str(O/'result.json'),changes=len(changes),decisions=len(decisions),inventory=len(inventory),unresolved=len(unresolved),second_boxes=len(second),differences_review=len(differences_review)),ensure_ascii=False))
