from workflow import save_page

def disk(cx,cy,scale=1,cross=False,rot=0):
    # Manually drawn curves; parameters only place the separately inspected disks.
    s=rf'\begin{{scope}}[shift={{({cx},{cy})}},scale={scale},rotate={rot}]'+'\n'
    s+=r'''\draw[yellow!70!green,line width=2pt](0,0)circle(1.2);
\fill[orange!85!yellow](-1,.7)--(-.6,.1)--(-1.2,-.1)--cycle;
\fill[orange!85!yellow](-.4,1.13)--(-.02,.6)--(.05,1.2)--cycle;
\fill[orange!85!yellow](.4,0)--(1.05,-.6)--(1.2,-.1)--cycle;
\draw[orange!70!red,line width=1.5pt](-1.2,-.1)..controls(-.6,.6)and(.3,.25)..(1.2,.25);
\draw[orange!70!red,line width=1.5pt](-1,.7)..controls(-.7,-.35)and(.4,-.3)..(1.2,-.1);
\draw[orange!70!red,line width=1.5pt](-.4,1.13)--(1.05,-.6);
'''
    if cross:
        s+=r'''\fill[orange!85!yellow](-.1,.6)..controls(.55,.2)and(.1,-.6)..(.1,-.8)..controls(-.3,-.4)and(-.35,.2)..(-.1,.6);
\fill[orange!85!yellow](.1,-.8)--(-.25,-1.17)--(.4,-1.13)--cycle;
\draw[orange!70!red,line width=1.5pt](.05,1.2)..controls(-.3,.2)and(-.35,-.7)..(.4,-1.13);
\draw[orange!70!red,line width=1.5pt](.4,1.13)..controls(.5,.2)and(.4,-.8)..(-.25,-1.17);
'''
    else:
        s+=r'''\fill[orange!85!yellow](-.2,.6)--(-.45,.15)--(.1,.25)--cycle;
\draw[orange!70!red,line width=1.5pt](.05,1.2)..controls(-.6,.2)and(-.5,-.8)..(-.2,-1.18);
\draw[orange!70!red,line width=1.5pt](.4,1.13)..controls(.6,.2)and(.4,-.8)..(.15,-1.2);
'''
    return s+'\\end{scope}\n'

f1=r'\figure{\begin{tikzpicture}[x=.65cm,y=.65cm,line cap=round]'+'\n'
f1+=disk(0,1.2)+disk(0,-1.2,cross=True,rot=180)+disk(3,1.2,cross=True)
f1+=r'''\node at(1.55,1.25){$+$};\node at(4.45,1.25){$=$};
\node at(-.45,1.85){$D$};\node at(.65,1.95){$D'\unsure{1}$};\node at(-.5,.7){$D$};\node at(.65,.55){$D'$};
\node at(-.5,-1.85){$D'$};\node at(.5,-1.95){$D$};\node at(.45,-.55){$D$};
\node at(-.05,2.6){$u$};\node at(.45,2.6){$v$};\draw[->](-.05,2.85)--(.45,2.85);
\node at(2.95,2.6){$u$};\node at(3.45,2.6){$v$};\draw[->](2.95,2.85)--(3.45,2.85);
\node at(2.5,1.75){$D$};\node at(3.6,1.75){$D'$};\node at(2.65,-.1){$s$};\node at(3.45,-.1){$t$};
\node at(-.3,-.15){$t$};\node at(.2,-.15){$s$};\node at(-.6,.05){$\unsure{s}$};\node at(.45,.08){$t$};
\node at(-.45,-2.55){$v$};\node at(.4,-2.55){$u$};
\draw[->](-.65,.05)..controls(-.9,.2)and(-1,.3)..(-1.1,.45);
\draw[->](-1,-.55)..controls(-.95,-.25)and(-.75,-.15)..(-.6,-.05);
\draw[->](1,.4)..controls(.85,.25)and(.7,.2)..(.6,.1);
\draw[->](.65,-.1)..controls(.9,-.25)and(1,-.4)..(1,-.55);
\draw(1.3,.6)..controls(1.45,.4)and(1.25,.1)..(1.4,0)..controls(1.25,-.1)and(1.45,-.45)..(1.3,-.6);
\draw[->](4.9,1.4)..controls(6,1.2)and(6,-.5)..(4.3,-.5)--(3.2,-.5)..controls(2.5,-.45)and(2,-.1)..(1.4,0);
\draw[gray,line width=2pt](-.8,-.3)--(.3,-1.45);
\end{tikzpicture}} % crop-candidate: scan 39
'''
f2=r'\figure{\begin{tikzpicture}[x=.6cm,y=.6cm,line cap=round]'+'\n'
f2+=disk(0,2.4,cross=True)+disk(0,0)+disk(0,-2.4,cross=True)+disk(3,2.4)+disk(3,-2.4,cross=True)
f2+=r'''\draw[green!25!black,line width=4pt](-.25,1.22)--(.4,1.27);\draw[green!25!black,line width=4pt](-.2,-1.18)--(.15,-1.2);
\draw[blue!40!green,line width=2pt](-.25,1.18)--(.4,1.23);\draw[blue!40!green,line width=2pt](-.2,-1.23)--(.15,-1.25);
\node[above]at(-.1,3.65){$D'$};\node[above]at(.55,3.65){$D$};
\node at(-.5,.6){$D$};\node at(.6,.6){$D'$};\node[below]at(-.2,-3.65){$D'$};\node[below]at(.55,-3.65){$D$};
\draw[gray,->](3.2,3.6)..controls(3.8,4.6)and(1.7,4.8)..(1.7,2.2)..controls(1.7,1.4)and(1.4,1.3)..(.9,1.15);
\draw[gray,->](2.75,-3.6)..controls(2.7,-4.4)and(1.6,-4.1)..(1.5,-2)..controls(1.5,-1.4)and(1,-1.2)..(.75,-1.1);
\draw[gray,line width=2pt](-.1,3.58)..controls(-.4,2.5)and(-.4,1.8)..(.4,1.28);
\draw[black,line width=1.2pt](2.1,-1.7)--(2.2,-1.8)--(2.2,-1.9)--(2.35,-2)--(2.35,-2.1);
\end{tikzpicture}} % crop-candidate: scan 39
'''
# Four separate disks, drawn from their relative arrangement in the large sketch.
f3=r'''\figure{\begin{tikzpicture}[x=.7cm,y=.7cm,line cap=round,line join=round]
\begin{scope}[shift={(-1.8,2.25)},rotate=12]
\draw[yellow!70!green,line width=2pt](0,0)ellipse(1.8 and1.7);
\fill[orange!85!yellow](.1,1.7)..controls(-.4,.9)and(.8,.2)..(.3,-.25)..controls(-.1,.5)and(.6,1.1)..(.5,1.65);
\fill[orange!85!yellow](-.5,-1.6)--(.05,-1.68)--(-.25,-.95)--cycle;
\fill[orange!85!yellow](1.1,-.9)--(1.35,-1.1)--(.8,-.25)--cycle;
\draw[orange!65!red,line width=1.5pt](-.35,1.67)..controls(-.85,.5)and(-1,-.6)..(-.5,-1.6);
\draw[orange!65!red,line width=1.5pt](.1,1.7)..controls(.15,.4)and(-.15,-.7)..(.05,-1.68);
\draw[orange!65!red,line width=1.5pt](.5,1.65)..controls(.15,.7)and(.3,-.3)..(1.35,-1.1);
\draw[orange!65!red,line width=1.5pt](-1.15,1.3)..controls(-1,.5)and(.4,-.75)..(1.35,-1.1);
\draw[orange!65!red,line width=1.5pt](-.8,1.5)--(1.1,-.9);
\draw[orange!65!red,dashed,line width=1pt](-.35,1.67)..controls(-1.4,.2)and(-.65,-.8)..(.4,-1.65);
\end{scope}
\begin{scope}[shift={(-2.1,-1.1)},rotate=-13]
\draw[yellow!70!green,line width=2pt](0,0)ellipse(1.8 and1.6);
\fill[orange!85!yellow](-.1,1.6)--(.4,1.55)--(.15,.85)--cycle;
\fill[orange!85!yellow](-.5,-1.5)..controls(-1,-.3)and(-1,.2)..(-.65,.45)..controls(-.2,.1)and(-.15,-.7)..(-.5,-1.5);
\fill[orange!85!yellow](.7,.3)..controls(1.2,.5)and(1.7,.1)..(1.7,-.2)--(.9,-.5)--cycle;
\draw[orange!65!red,line width=1.5pt](-.1,1.6)--(-.5,-1.5);
\draw[orange!65!red,line width=1.5pt](.4,1.55)--(.1,-1.6);
\draw[orange!65!red,line width=1.5pt](-1.75,-.35)..controls(-.5,.7)and(.75,.5)..(1.7,-.2);
\draw[orange!65!red,line width=1.5pt](-1.5,-.9)--(1.7,-.2);
\draw[orange!65!red,dashed,line width=1pt](-.9,-1.35)..controls(-1.3,.3)and(.6,.65)..(.8,1.35);
\draw[orange!65!red,dashed,line width=1pt](.2,-1.6)..controls(.3,-.7)and(1,0)..(1.2,.9);
\end{scope}
\begin{scope}[shift={(1.6,.8)},rotate=-25]
\draw[yellow!70!green,line width=2pt](0,0)ellipse(1.75 and1.55);
\fill[orange!85!yellow](-.45,1.5)--(.05,1.55)--(-.5,.9)--cycle;
\fill[orange!85!yellow](-1.5,.8)--(-1.6,.4)--(-.75,.6)--cycle;
\fill[orange!85!yellow](.6,.9)--(.1,-.05)--(.75,.2)--cycle;
\draw[orange!65!red,line width=1.5pt](-.45,1.5)..controls(-.65,.3)and(-.25,-1)..(.3,-1.55);
\draw[orange!65!red,line width=1.5pt](.05,1.55)--(-.3,-1.5);
\draw[orange!65!red,line width=1.5pt](.6,1.45)..controls(.8,.4)and(.5,-1)..(.3,-1.55);
\draw[orange!65!red,line width=1.5pt](-1.5,.8)--(1.7,-.4);
\draw[orange!65!red,line width=1.5pt](-1.75,.05)--(1.5,-.85);
\draw[orange!65!red,dashed,line width=1pt](-1.1,-1.2)..controls(-.1,-.5)and(.9,-.8)..(.9,.6);
\end{scope}
\begin{scope}[shift={(.8,-2.25)},rotate=-30]
\draw[yellow!70!green,line width=2pt](0,0)ellipse(1.6 and1.35);
\fill[orange!85!yellow](-.5,1.25)--(0,1.35)--(-.2,.7)--cycle;
\fill[orange!85!yellow](-.45,-1.25)..controls(-1.1,-.2)and(-.8,.6)..(-.5,.5)..controls(.1,-.1)and(-.2,-.7)..(-.45,-1.25);
\fill[orange!85!yellow](.6,.3)..controls(1,.1)and(.55,-.7)..(.35,-1.3)--(.25,-.3)--cycle;
\draw[orange!65!red,line width=1.5pt](-.5,1.25)--(-.45,-1.25);
\draw[orange!65!red,line width=1.5pt](0,1.35)--(.35,-1.3);
\draw[orange!65!red,line width=1.5pt](-1.55,.1)..controls(-.5,.2)and(.8,.15)..(1.55,-.1);
\draw[orange!65!red,line width=1.5pt](-1.4,-.6)--(1.4,-.6);
\draw[orange!65!red,dashed,line width=1pt](-.75,-1.15)..controls(-1,.2)and(-.4,.55)..(-.2,1.3);
\draw[orange!65!red,dashed,line width=1pt](.9,-1.1)..controls(1,-.3)and(.5,.5)..(.4,1.25);
\end{scope}
\draw[black,line width=4pt](-2.6,.6)..controls(-1.2,.5)and(-.8,.8)..(-.35,1.2)..controls(-.55,.5)and(-.55,-.1)..(.35,-.6)..controls(-.25,-.5)and(-.7,-.7)..(-1.1,-1.35)..controls(-1.05,-.25)and(-1.5,.5)..(-2.6,.6);
\draw[gray,line width=.5pt](-2.2,.55)..controls(-1.3,.05)and(-1,-.65)..(-1.1,-1.35);
\draw[gray,line width=.5pt](-1.95,.55)..controls(-.95,.1)and(-.6,-.2)..(.35,-.6);
\draw[gray,line width=.5pt](-.35,1.2)--(2.9,-.05);\draw[gray,line width=.5pt](-.55,.9)--(2.8,-.25);
\draw[blue!40!green,line width=2pt](-2.55,.57)--(-2.15,.52);\draw[blue!40!green,line width=2pt](-.5,1.1)--(-.25,1.35);\draw[blue!40!green,line width=2pt](.15,-.65)--(.55,-.8);\draw[blue!40!green,line width=2pt](-1.25,-1.3)--(-1.1,-1.6);
\node at(-3.05,3.65){$D_1$};\node at(-2.7,3.9){$D_1$};\node at(-2.05,4.1){$D_0$};\node at(-1.5,4.1){$D'_0$};
\node at(-2.75,.9){$D'_0$};\node at(-2.2,.88){$D_0$};\node at(-1.8,.82){$\alpha$};\node at(-1.5,.85){$\beta$};\node at(-1,.95){$D'_1$};\node at(-.35,1.65){$\unsure{D'_1}$};
\node at(-2.85,.2){$D_0$};\node at(-2.15,.1){$D'_0$};\node at(-1.8,-.05){$\alpha$};\node at(-1.35,-.35){$\beta$};
\node at(-3.95,-1.2){$D'_1$};\node at(-3.65,-1.85){$D_1$};\node at(-2.5,-2.85){$D_0$};\node at(-1.9,-2.85){$D'_0$};
\node at(-1.45,-1.15){$D_1$};\node at(-1.5,-1.7){$D'_1$};
\node at(1.6,2.55){$D'_0$};\node at(2.2,2.35){$D_0$};\node at(3.5,-.05){$D_1$};\node at(3.4,-.55){$D'_1$};
\node at(.15,1.2){$D_1$};\node at(-.15,.45){$\unsure{D'_1}$};\node at(-.05,.1){$\beta$};\node at(.3,-.25){$\alpha$};\node at(.75,-.5){$D_0$};\node at(1.2,-.65){$D'_0$};
\node at(-.45,-1.1){$\alpha$};\node at(-.75,-1.45){$\beta$};\node at(-1.05,-1.7){$\unsure{D'_1}$};\node at(-.9,-2.1){$D_1$};\node at(.1,-1.2){$D'_0$};\node at(.55,-1.4){$D_0$};\node at(2.65,-2.65){$D'_1$};\node at(2.55,-3.05){$D_1$};
\end{tikzpicture}} % crop-candidate: scan 39
'''
tex=r'''\scanpage{39}
\margin{38}
qui applique \deleted{\unsure{sommet appartenant}} \inserted{t\textsuperscript{te} extrémité de l'un des} arcs, sur l'unique extrémité de l'autre qui appartient à la ``$=$'' \deleted{pseudo} \deleted{droite} corde, ou pseudo-droite, donc \deleted{\unsure{avant le}} \inserted{en} intervertissant les extrémités, donnerait la \deleted{figure} figure ci-contre.
'''+f1+r'''
En le faisant pour les deux arcs de générisation antipodiques, on trouve la figure ci-dessous. Mais réflexion faite, comme ce recollement-là correspond à un isom de transport entre $\underline\omega(\Delta_L)\simeq\underline\omega(L)$ et $\underline\omega(\Delta_{L'})\simeq\underline\omega(L')$ qui est l'isomorphisme ``évident'', il me semble que ce n'est pas le bon ---
'''+f2+r'''
qu'il faudrait plutôt \deleted{l'isom} \inserted{prendre l'isom d'identification} $a\overset{\unsure{\sim}}{\simeq}a'$ qui transforme $s$ en $s$, $t$ en $t$, donc qui fait se continuer $D$ par $D'$, $D'$ par $D$; en façon imagée, cela revient à faire la symétrie p.r. à ``l'axe'' $(s,t)=a$,
'''+f3+r'''
Par cette identification, toutes les ``faces'' sont d'ordre 4, ou les sommets de la \deleted{\unsure{Γ}} carte duale de celle déduite du graphe des positions relatives, avec la semi-circularisation définie par les polygones caractéristiques et les isom de transport pour l'orientation qui est l'opposé de l'isom tautologique. Les coins définis ici comme faces, qui sont duels des coins formés par les arcs d'inertie, ont des sommets, correspondants aux arêtes des ``coins caractéristiques'', qui sont de trois types, suivant les types des arcs de transition qui les bordent :
'''
e=[('margin note','bottom left','38'),('text','left upper','qui applique'),('deletion','left top','sommet appartenant'),('insertion','left top','tte extrémité de l’un des'),('deletion','left top','pseudo'),('deletion','left upper','droite'),('deletion','left upper','avant le'),('insertion','left upper','en'),('deletion','left upper','figure'),('drawing','left upper cluster','three disks with u,v,s,t,D,D′ and addition/result signs'),('text','left middle','En le faisant'),('display','left middle','ω(ΔL)≃ω(L), ω(ΔL′)≃ω(L′)'),('drawing','left lower cluster','three attached disks and two separate disks; curved arrows'),('text','left bottom','qu’il faudrait plutôt'),('deletion','left bottom','l’isom'),('insertion','left bottom','prendre l’isom d’identification'),('display','left bottom','a≃a′'),('drawing','right upper','four disks; D0,D′0,D1,D′1,α,β; central black quadrilateral'),('text','right upper beside drawing','Par cette identification'),('deletion','right upper beside drawing','Γ'),('text','right lower','définie par les polygones'),('text','right lower','Les coins définis ici')]
d=[('left top crossed wording','sommet appartenant; avant le','Deleted opening words partly buried under replacement.','low'),('left bottom isomorphism','a with doubled equivalence stroke to a′','Two stacked curving strokes; no arrowheads visible.','medium'),('small upper drawing labels','D′1; s near gluing','Overwritten small labels retained with explicit doubt.','low'),('right large drawing','D0,D′0,D1,D′1,α,β','Every visible label attempted; dense junction labels and individual colored regions least secure.','medium'),('right prose','ou les sommets','Short connective appears ou; not silently changed to sont or où.','medium')]
save_page(39,tex,e,d,'''The initial same-pseudoline gluing is reconsidered: “il me semble que ce n’est pas le bon”, and the proposed replacement fixes endpoint names while continuing D by D′ and vice versa, described as reflection in axis (s,t). This changes orientation transport to the opposite of the tautological isomorphism. He claims all resulting faces have degree 4. This is a significant self-flagged/revised construction linking back to scans31–34; preserve both versions as separate notes. Large four-disk figure gives the local quadrilateral with labeled D0/D1 pairs and α,β.''',sheet_kind='reused_typed')
