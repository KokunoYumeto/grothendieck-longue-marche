from pathlib import Path
import re,json
out=Path(__file__).parent
packet=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan031')
C=(packet/'C.tex').read_text()
figs={}
def fig(n,s):
 figs[n]=r'\begin{tikzpicture}[x=.85cm,y=.85cm,line cap=round,line join=round]'+'\n'+s.strip()+'\n'+r'\end{tikzpicture}'
def points(coords,color='red!55!black',radius='1.8pt'):
 return '\n'.join(r'\fill['+color+'] ('+p+') circle('+radius+');' for p in coords)
fig(180,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (-1,0)..controls(-.8,-.3)and(.7,-.3)..(1,0);
\draw[dash pattern=on 1.7pt off 1.5pt] (-1,0)..controls(-.6,.3)and(.6,.3)..(1,0);
'''+points(['-.7,-.17','0,-.24','.7,-.17','-.4,.22','.4,.22']))
fig(181,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (-1,0)..controls(-.7,-.31)and(.7,-.31)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.6,.3)and(.6,.3)..(1,0);
\draw[red!55!black,very thick] (0,1.05)..controls(-.55,1)and(-.7,.2)..(-.65,-.19)..controls(-.55,-.9)..(-.1,-1.05)..controls(.5,-.95)and(.7,-.4)..(.65,-.19)..controls(.63,.5)and(.4,1)..(0,1.05);
\draw[red!55!black,densely dashed] (0,1.05)..controls(.03,.7)and(.03,.5)..(0,.24)..controls(-.02,-.3)and(-.08,-.8)..(-.1,-1.05);
'''+points(['0,1.05','-.65,-.19','.65,-.19','0,.24','-.1,-1.05']))
fig(182,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (-1,0)..controls(-.65,-.32)and(.6,-.3)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.6,.3)and(.65,.3)..(1,0);
\draw[red!55!black,very thick] (0,1.05)..controls(-.5,.95)and(-.68,.4)..(-.7,-.10);
\draw[red!55!black,very thick] (0,1.05)..controls(.36,.9)and(.42,.35)..(.45,-.16);
\draw[red!55!black,densely dashed] (0,1.05)..controls(-.15,.9)and(-.29,.5)..(-.3,.22);
\draw[red!55!black,thick] (0,1.05)..controls(.4,1.02)and(.73,.75)..(.76,.48);
\draw[red!55!black,densely dashed] (.76,.48)--(.75,.15);
\draw[->,thick] (1.14,-.05)..controls(1.52,.2)and(1.47,.52)..(1.17,.63);
'''+points(['0,1.05','-.7,-.17','.45,-.24','-.3,.22','.75,.15']))
fig(183,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (-1,0)..controls(-.7,-.3)and(.7,-.3)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.6,.3)and(.6,.3)..(1,0);
\draw[red!55!black,thick] (.2,1.05)..controls(.35,.9)and(.35,-.8)..(-.1,-1.05);
\draw[red!55!black,densely dashed] (.2,1.05)..controls(-.28,.7)and(-.3,-.8)..(-.1,-1.05);
\fill[red!55!black] (-.45,.22) circle(1.8pt) node[above,black] {$\alpha$};
\fill[red!55!black] (.45,.2) circle(1.8pt) node[above,black] {$\alpha'$};
\fill[red!55!black] (-.82,-.12) circle(1.8pt) node[below,black] {$P$};
\fill[red!55!black] (-.02,-.24) circle(1.8pt) node[below,black] {$\beta$};
\fill[red!55!black] (.72,-.15) circle(1.8pt) node[below,black] {$\beta'$};
\fill (-.16,.23) circle(1.2pt);\fill (.22,-.24) circle(1.2pt);
''')
fig(184,r'''
% The drawing is canceled by its seven oblique strokes. No alphabetic labels are secure beneath them.
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (0,1.05)..controls(.75,1.05)and(1,-.65)..(0,-1.05);
\draw[very thick] (-1,0)..controls(-.7,-.3)and(.65,-.28)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.65,.3)and(.7,.25)..(1,0);
\draw[red!55!black,thick] (0,1.05)..controls(.43,.8)and(.42,-.8)..(0,-1.05);
\draw[red!55!black,densely dashed] (0,1.05)..controls(-.36,.8)and(-.3,-.8)..(0,-1.05);
'''+points(['-.95,-.03','-.48,.21','-.15,-.2','.75,.6','.65,-.75'])+r'''
\draw[thick] (-1.12,-.9)--(-.3,1.12);
\draw[thick] (-.84,-1.02)--(.02,1.05);
\draw[thick] (-.51,-1.04)--(.34,1.02);
\draw[thick] (-.22,-1.02)--(.67,1.02);
\draw[thick] (.08,-.95)--(.93,.92);
\draw[thick] (.37,-.84)--(1.2,.86);
\draw[thick] (.67,-.75)--(1.38,.73);
''')
fig(185,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[very thick] (0,1.05)..controls(.46,1.04)and(.64,.84)..(.7,.72);
\draw[very thick] (.76,.59)..controls(1,.16)and(.93,-.4)..(.68,-.72);
\draw[very thick] (.59,-.86)..controls(.4,-1)..(0,-1.05);
\draw[red!55!black,thick] (0,1.05)..controls(.45,.8)and(.4,-.8)..(0,-1.05);
\draw[red!55!black,densely dashed] (0,1.05)..controls(-.35,.8)and(-.3,-.8)..(0,-1.05);
\draw[very thick] (-1,0)..controls(-.8,-.22)and(-.3,-.27)..(.3,-.24);
\draw[densely dashed] (-1,0)..controls(-.8,.27)and(-.4,.3)..(-.17,.23);
\draw[gray,densely dashed] (-.17,.23)..controls(.48,.28)and(.86,.2)..(1,0)..controls(.8,-.2)and(.6,-.25)..(.3,-.24);
\fill[red!55!black] (-.55,.22) circle(1.8pt) node[above,black] {$\alpha$};
\fill[red!55!black] (.74,.65) circle(1.8pt) node[above right,black] {$\beta'$};
\fill[red!55!black] (-.95,-.06) circle(1.8pt) node[below left,black] {$P$};
\fill[red!55!black] (-.15,-.25) circle(1.8pt) node[below,black] {$\beta$};
\fill[red!55!black] (.65,-.8) circle(1.8pt) node[below right,black] {$\alpha'$};
\fill (0,1.05) circle(1.2pt);\fill (0,-1.05) circle(1.2pt);\fill (-.17,.23) circle(1.2pt);\fill (.3,-.24) circle(1.2pt);
\draw[->,thick] (.94,.86)..controls(.87,1.03)..(.65,1.11);
\draw[->,thick] (.86,-.89)..controls(.69,-1.08)..(.45,-1.15);
''')
fig(186,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[red!55!black,thick] (-1,0)..controls(-.7,-.3)and(.7,-.3)..(1,0);
\draw[red!55!black,densely dashed] (-1,0)..controls(-.65,.32)and(.65,.32)..(1,0);
\draw[very thick] (-.55,.8)..controls(-1,.4)and(-.95,-.5)..(-.45,-.9);
\draw[very thick] (-.55,.8)..controls(-.1,1.13)and(.25,1.14)..(.6,.85);
\draw[very thick,densely dashed] (.6,.85)..controls(.92,.5)..(.75,.15);
\draw[densely dashed] (.75,.15)..controls(.99,-.42)..(.35,-.93);
\draw[very thick] (.6,-.2)..controls(.78,-.56)..(.35,-.93);
\draw[very thick] (-.45,-.9)..controls(-.15,-1.1)and(.15,-1.12)..(.35,-.93);
\draw[densely dashed] (-.45,-.9)..controls(-.12,-.65)and(.12,-.65)..(.35,-.93);
\draw[densely dashed] (0,.27)--(0,-.75);
\fill[red!55!black] (-.55,.8) circle(1.8pt) node[above,black] {$1$};
\fill[red!55!black] (.6,.85) circle(1.8pt) node[above,black] {$\infty$};
\fill[red!55!black] (-.45,-.9) circle(1.8pt) node[below,black] {$0$};
\fill[red!55!black] (.35,-.93) circle(1.8pt) node[below right,black] {$\unsure{\bar P}$};
\fill[red!55!black] (0,-.75) circle(1.8pt) node[above right,black] {$\unsure{P}$};
\fill (-.75,-.1) circle(1.2pt) node[below left] {$u_0$};
\fill (0,-.23) circle(1.2pt) node[below left] {$u_1$};
\fill (.6,-.2) circle(1.2pt) node[below right] {$u_2$};
\fill (.75,.15) circle(1.2pt) node[above right] {$u_3$};
\fill (0,.27) circle(1.2pt) node[above] {$u_4$};
\fill (-.68,.27) circle(1.2pt) node[above left] {$u_5$};
''')
fig(187,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[thick] (-1,0)..controls(-.7,-.3)and(.7,-.3)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.65,.3)and(.65,.3)..(1,0);
\draw[red!55!black,thick] (-.15,1)..controls(-.34,.65)and(-.36,-.65)..(-.12,-1);
\draw[red!55!black,densely dashed] (-.15,1)..controls(.02,.7)and(.02,-.7)..(-.12,-1);
\draw[red!55!black,densely dashed] (.4,1)..controls(.1,.7)and(.12,-.7)..(.35,-1);
\draw[red!55!black,thick] (.4,1)..controls(.64,.7)and(.65,-.7)..(.35,-1);
'''+points(['-.8,-.14','0,-.24','.85,-.1','-.45,.22','.3,.22'])+points(['-.3,-.24','.5,-.2','-.05,.24','.2,.24'],'black','1.15pt')+r'\node[below] at (0,-.25) {$P$};')
fig(188,r'''
\draw[gray] (0,0) circle(1);
\draw[very thick] (-.86,.4)..controls(-1,.2)and(-1,-.1)..(-.96,-.22);
\draw[very thick] (-.95,-.35)..controls(-.9,-.8)and(-.6,-1)..(-.22,-1.02);
\draw[very thick] (-.08,-1.02)..controls(.35,-1.05)and(.6,-.96)..(.71,-.83);
\draw[very thick] (.81,-.72)..controls(.94,-.49)and(1,-.12)..(.95,0);
\draw[red!55!black,thick] (-.86,.4)..controls(-.4,.1)and(.65,-.28)..(.95,0);
\draw[red!55!black,densely dashed] (-.86,.4)..controls(-.35,.54)and(.6,.22)..(.95,0);
\draw[red!55!black,thick] (-.75,-.65)..controls(-.25,-.88)and(.6,-.63)..(.92,-.3);
\draw[red!55!black,densely dashed] (-.75,-.65)..controls(-.1,-.35)and(.6,-.25)..(.92,-.3);
\draw[very thick] (-.1,.17)..controls(-.05,.43)and(.02,.64)..(.05,.65);
\draw[very thick] (.12,.76)..controls(.24,1.02)and(.31,1.07)..(.4,.98);
\draw[densely dashed] (.4,.98)--(.38,.32);
\fill[red!55!black] (-.97,-.28) circle(1.8pt) node[right,black] {$0$};
\fill[red!55!black] (-.15,-1.02) circle(1.8pt) node[below,black] {$1$};
\fill[red!55!black] (.76,-.78) circle(1.8pt) node[below right,black] {$\infty$};
\fill[red!55!black] (.08,.7) circle(1.8pt) node[left,black] {$P$};
\fill[red!55!black] (.39,.79) circle(1.8pt) node[right,black] {$\bar P$};
'''+points(['-.86,.4','-.1,.17','.38,.32','.95,0','-.75,-.65','.92,-.3'],'black','1.2pt'))
fig(189,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[red!55!black,thick] (-.25,.97)..controls(-.65,.65)and(-.63,-.7)..(-.4,-.98);
\draw[red!55!black,densely dashed] (-.25,.97)..controls(-.06,.65)and(-.08,-.7)..(-.4,-.98);
\draw[red!55!black,densely dashed] (.4,1)..controls(.05,.65)and(.04,-.7)..(.18,-1.03);
\draw[red!55!black,thick] (.4,1)..controls(.7,.7)and(.65,-.75)..(.18,-1.03);
\draw[very thick] (-.25,.97)..controls(-.4,.93)..(-.57,.78);
\draw[very thick] (-.69,.66)..controls(-1,.2)and(-1,-.36)..(-.85,-.68);
\draw[very thick] (-.76,-.82)..controls(-.62,-.91)..(-.4,-.98);
\draw[gray,densely dashed] (-1,0)..controls(-.83,-.14)..(-.55,-.17);
\draw[very thick] (-.55,-.17)--(-.14,-.23);
\draw[very thick] (0,-.23)..controls(.4,-.27)and(.7,-.24)..(.76,-.14);
\draw[very thick] (.88,-.07)..controls(1,-.04)and(1,.05)..(.96,.09);
\draw[densely dashed] (.96,.09)..controls(.76,.21)..(.55,.23);
\draw[very thick] (-.15,.23)--(.15,.23);
\draw[gray] (-1,0)..controls(-.68,.28)..(-.15,.23);
\fill[red!55!black] (-.63,.73) circle(1.8pt) node[above left,black] {$P$};
\fill[red!55!black] (-.81,-.75) circle(1.8pt) node[below left,black] {$\bar P$};
\fill[red!55!black] (-.07,-.23) circle(1.8pt) node[below,black] {$0$};
\fill[red!55!black] (.82,-.12) circle(1.8pt) node[below,black] {$1$};
\fill[red!55!black] (.55,.23) circle(1.8pt) node[above right,black] {$\infty$};
'''+points(['-.25,.97','-.4,-.98','-.55,-.17','-.15,.23','.15,.23','.5,-.22'],'black','1.2pt'))
fig(190,r'''
\draw[gray] (0,0) circle(1);
\draw[gray] (-.8,.66)..controls(-.38,1.2)and(.3,1.16)..(.7,.7);
\draw[very thick] (-.8,.57)..controls(-1,.32)..(-.99,.08);
\draw[very thick] (-.99,-.07)..controls(-1,-.37)..(-.87,-.56);
\draw[very thick] (.98,.01)--(.98,-.28);
\draw[red!55!black,thick] (-.8,.57)..controls(-.4,.2)and(.62,-.13)..(.98,.01);
\draw[red!55!black,densely dashed] (-.8,.57)..controls(-.15,.65)and(.65,.22)..(.98,.01);
\draw[red!55!black,thick] (-.87,-.56)..controls(-.45,-.83)and(.62,-.67)..(.98,-.28);
\draw[red!55!black,densely dashed] (-.87,-.56)..controls(-.1,-.29)and(.58,-.22)..(.98,-.28);
\draw[very thick] (-.08,.2)..controls(.02,.36)..(.08,.52);
\draw[very thick] (.16,.64)..controls(.5,1.17)and(.55,.98)..(.52,.75);
\draw[densely dashed] (.51,.61)--(.38,.34);
\draw[very thick] (-.07,-.69)--(-.03,-.91);
\draw[very thick] (.05,-1.04)..controls(.2,-1.16)and(.36,-1.18)..(.46,-1.01);
\draw[densely dashed] (.46,-1.01)--(.38,-.37);
\fill[red!55!black] (-.99,0) circle(1.8pt) node[left,black] {$P$};
\fill[red!55!black] (.12,.58) circle(1.8pt) node[above left,black] {$\alpha$};
\fill[red!55!black] (.52,.68) circle(1.8pt) node[right,black] {$\unsure{\alpha'}$};
\fill[red!55!black] (0,-.98) circle(1.8pt) node[below left,black] {$\unsure{\beta}$};
\fill[red!55!black] (.42,-.75) circle(1.8pt) node[right,black] {$\unsure{\beta'}$};
'''+points(['-.8,.57','-.08,.2','.38,.34','.98,.01','-.87,-.56','-.07,-.69','.38,-.37','.98,-.28'],'black','1.2pt'))
fig(191,r'''
\draw[gray] (0,0) ellipse (1 and 1.05);
\draw[red!55!black,thick] (-.3,1)..controls(-.56,.65)and(-.57,-.7)..(-.4,-1);
\draw[red!55!black,densely dashed] (-.3,1)..controls(-.1,.65)and(-.1,-.7)..(-.4,-1);
\draw[red!55!black,thick] (.3,1.04)..controls(.01,.65)and(-.04,-.75)..(.08,-1.05);
\draw[red!55!black,densely dashed] (.3,1.04)..controls(.5,.7)and(.4,-.7)..(.08,-1.05);
\draw[very thick] (-.3,1)..controls(-.12,1.08)..(-.02,1.07);
\draw[very thick] (.12,1.07)--(.3,1.04);
\draw[very thick] (-.4,-1)..controls(-.21,-1.1)..(.08,-1.05);
\draw[very thick] (-1,0)..controls(-1,-.17)and(-.73,-.21)..(-.55,-.21);
\draw[densely dashed] (-.55,-.21)--(-.24,-.24);
\draw[very thick] (-.03,-.24)..controls(.5,-.3)and(1,-.12)..(1,0);
\draw[densely dashed] (-1,0)..controls(-.7,.16)..(-.46,.2);
\draw[very thick] (-.46,.2)--(-.22,.22);
\draw[very thick] (.38,.21)--(.62,.17);
\draw[densely dashed] (.62,.17)..controls(.88,.1)..(1,0);
\fill[red!55!black] (.05,1.07) circle(1.8pt) node[above,black] {$P$};
\fill[red!55!black] (-.76,-.18) circle(1.8pt) node[below,black] {$\alpha$};
\fill[red!55!black] (.16,-.24) circle(1.8pt) node[below,black] {$\alpha'$};
\fill[red!55!black] (-.45,.21) circle(1.8pt) node[above,black] {$\beta'$};
\fill[red!55!black] (.62,.18) circle(1.8pt) node[above,black] {$\beta$};
\draw[->,thick] (1.13,-.12)..controls(1.54,-.02)and(1.45,.22)..(1.2,.26);
'''+points(['-.3,1','.3,1.04','-.4,-1','.08,-1.05','-.55,-.21','-.22,.22','-.03,-.24','.38,.21'],'black','1.2pt'))
margin=r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round,line join=round]
\fill (0,6.2) circle(2pt);
\draw (0,6.2)..controls(-.25,6.4)..(-.5,7.05);
\draw (0,6.2)..controls(-.15,6.55)..(-.22,7.18);
\draw (0,6.2)--(.04,7.21);
\draw (0,6.2)..controls(.2,6.65)..(.26,7.25);
\draw (0,6.2)..controls(.38,6.65)..(.47,7.28);
\draw (0,3.4)--(.85,3.4);\fill (0,3.4) circle(2pt);\fill (.85,3.4) circle(2pt);
\draw (0,3.4)--(-.17,4.1);\draw (0,3.4)--(.1,4.15);\draw (0,3.4)--(.32,4.14);
\draw (.85,3.4)--(.72,4.18);\draw (.85,3.4)--(1.03,4.26);
\draw (0,.6)--(.55,.63)--(1,.66);
\foreach \x/\y in {0/.6,.55/.63,1/.66}{\fill (\x,\y) circle(2pt);}
\draw (0,.6)--(-.06,1.5);\draw (0,.6)--(.1,1.5);\draw (.55,.63)--(.5,1.45);\draw (1,.66)--(.86,1.49);\draw (1,.66)--(1.15,1.47);
% Literal courses of the two retraced marginal arrows.
\draw[thick] (.52,5.35)--(1.04,5.38)..controls(1.4,5.42)..(1.68,5.42);
\draw[thick] (1.68,5.42)..controls(1.34,5.29)..(1.04,5.38);
\draw[thick] (.52,2.32)..controls(1.15,2.37)..(1.65,2.4);
\draw[thick] (.52,2.32)..controls(1.15,2.3)..(1.65,2.28);
\draw[thick] (.52,2.32)..controls(1.15,2.2)..(1.7,2.17);
\draw[gray] (.52,7.3)..controls(.44,4.7)and(.55,1.5)..(.57,-.32);
\draw[gray] (.6,-.47)..controls(1.12,-.45)and(1.52,-.52)..(1.72,-.51)--(1.73,-.55);
\end{tikzpicture}}}
'''
# Keep C's source layout, replace the drawing scaffolding and readings.
s=C
s=re.sub(r'\\margin\{\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}\}',lambda m:margin,s,count=1,flags=re.S)
s=re.sub(r'^\\sbox\{\d+\}.*\n','',s,flags=re.M)
for n,t in figs.items():
 old=r'\figure{\usebox{'+str(n)+'}}'
 if n==184:
  s=s.replace(r'\deleted{'+old+'}',r'\vcenter{\hbox{'+t+'}}')
 else:s=s.replace(old,r'\vcenter{\hbox{'+t+'}}')
repl={
r'\unsure{\mathbb P}_2(\unsure{\mathrm{Circ}}(K))':r'P_2(\mathrm{Circ}(K)',
r'\unsure{\mathfrak S}':r'\unsure{\mathfrak S|G}',
r'I\ \text{structure carré \uline{orienté}}':r'I\ \text{structure carrée \uline{orientée}}',
r'\unsure{\delta|J}':r'\delta',
r'f_{\vec Q,\unsure{\omega},a}':r'f_{\vec Q,\omega,a}',
r'\unsure{\Lambda}(Q)':r'\Lambda(Q)',
r'\unsure{J|B}':r'B',
r'\omega\xrightarrow{\sim}\omega':r'\omega\simeq\omega',
r'\text{mêmes paramètres que }':r'\text{même paramétrage que }',
r'\unsure{entièrement|anticanoniques}':r'entièrement',
r'\underline\omega(J))':r'\underline\omega(J)',
r'G=\mathbb Z/2\mathbb Z,\widetilde G\simeq':r'G=\mathbb Z/2\mathbb Z,\widetilde G=',
r'\mathrm{tw}_{\unsure{1/4|1/3}}\quad\unsure{1|2}':r'\mathrm{tw}_{1/4}\quad1',
r'\unsure{\mathfrak X}(I)':r'\unsure{\mathfrak X|\mathbb J}\unsure{(}I)',
r'\unsure{\gamma_r^{21}|\gamma_r^{2\'}}':r'\unsure{\gamma_r^{2\'}|\gamma_r^{21}}',
r'\arrow[ul,bend left=40,"{2\quad\gamma_r^2\quad2}"\']':r'\arrow[ull,bend left=65,"{2\quad\gamma_r^2\quad2}"\']',
r'\uline{\text{niveau }1}':r'\uline{\text{niveau }}1',
r'\uline{\text{niveau }0}':r'\uline{\text{niveau }}0',
r'\mathrm{III}_2,\mathrm{III}_1,\mathrm{III}\'_2&':r'\mathrm{III}_2,\mathrm{III}_{\unsure{1|4}},\mathrm{III}\'_2&',
r'\underline{542}':r'\overline{542}',
r'\unsure{\mathrm{Pent}|\mathrm{Pand}}':r'\mathrm{Pent}',
}
# Prime-bearing strings are set explicitly to avoid Python quote escapes becoming source characters.
repl.pop(r'\unsure{\gamma_r^{21}|\gamma_r^{2\'}}')
repl.pop(r'\arrow[ul,bend left=40,"{2\quad\gamma_r^2\quad2}"\']')
repl.pop(r'\mathrm{III}_2,\mathrm{III}_1,\mathrm{III}\'_2&')
repl[r"\unsure{\gamma_r^{21}|\gamma_r^{2'}}"]=r"\unsure{\gamma_r^{2'}|\gamma_r^{21}}"
repl[r'''\arrow[ul,bend left=40,"{2\quad\gamma_r^2\quad2}"']''']=r'''\arrow[ull,bend left=65,"{2\quad\gamma_r^2\quad2}"']'''
repl[r"\mathrm{III}_2,\mathrm{III}_1,\mathrm{III}'_2&"]=r"\mathrm{III}_2,\mathrm{III}_{\unsure{1|4}},\mathrm{III}'_2&"
for a,b in repl.items():
 if a not in s:raise ValueError('Missing replacement '+a)
 s=s.replace(a,b)
# Accent differs in certainty between the upper arrow and the lower key.
s=s.replace(r'\mathrm{Bit\acute et}(K)',r'\unsure{\mathrm{Bit\acute et}|\mathrm{Bitet}}(K)',1)
s=s.replace(r'B\in\mathrm{Bit\acute et}(K)',r'B\in\mathrm{Bitet}(K)')
# Punctuation after Aut+ has no secure modern normalization.
s=s.replace(r'G=\operatorname{Aut}^{+}\) ;',r'G=\operatorname{Aut}^{+}\)\unsure{;|,}')
# Circle and exclamation belong to the diagonal gamma label, not to an exponent.
s=s.replace(r'''\arrow[ur,"{3\quad\gamma^{1'}_r\quad3}","{(r\in\mathrm{Rep}(K))}"']''',r'''\arrow[ur,"{3\qquad3}","{(r\in\mathrm{Rep}(K))}"',"{\begin{tikzpicture}[baseline=-.6ex]\node[draw,ellipse,inner sep=3pt] {$\gamma_r^{1'}\!\begin{smallmatrix}\\!\end{smallmatrix}$};\end{tikzpicture}}"{description}]''')
# Trace the lower hook on gamma_{pi,rho} without claiming a second complete arrowhead.
s=s.replace(r'''\arrow[u,"{2\quad\gamma_{\pi,\rho}\quad2}"''',r'''\arrow[u,start anchor=north west,"{2\quad\gamma_{\pi,\rho}\quad2}","{\begin{tikzpicture}[baseline]\draw (0,.15)..controls(-.12,.23)and(-.16,.3)..(-.14,.37);\end{tikzpicture}}"{pos=.02,description}''')
# Do not turn retracing into a definite deleted reading.
s=s.replace(r'\begin{gathered}\mathrm{III}\'_2\ (\text{triple triangle gauche})',r'\begin{gathered}\mathrm{III}\'_{\unsure{2}}\ (\text{triple triangle gauche})')
s=s.replace(r"\begin{gathered}\mathrm{III}'_2\ (\text{triple triangle gauche})",r"\begin{gathered}\mathrm{III}'_{\unsure{2}}\ (\text{triple triangle gauche})")
s=s.replace(r'\text{60 structures de carré orienté à}',r'\text{\unsure{60} structures de carré orienté à}')
s=s.replace(r'\text{codiagonales, }K=',r'\text{codiagonales, }\unsure{K}=')
s=s.replace(r'\text{2+2 sommets-repère}',r'2+\unsure{2}\ \text{sommets-repère}')
s=s.replace(r'\uline{\text{niveau }2}',r'\uline{\text{niveau }\unsure{2}}')
s=s.replace(r'\{(\pi,\rho)\}\simeq\mathrm{Rep}(K)',r'\{(\pi,\rho)\}\unsure{\simeq}\mathrm{Rep}(K)')
s=re.sub(r'\\unsure\{\\texttt\{GUTS OUTPUT FOR PREDONT DELIVER AT 0000 - PREDONT\.MODULEF5\}\}\s*','',s)
s=s.replace(r'\end{tikzcd}}',r'\end{tikzcd}}'+'\n% crop-candidate: scan 31',1)
s=s.replace(r'\scanpage{31}',r'''\scanpage{31}
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (.12,.32)--(.1,.08)..controls(.09,.01)and(.02,.01)..(0,.05);\end{tikzpicture}}}''',1)
# Keep the exact output fragment; no compilation is performed.
(out/'candidate.tex').write_text(s)
(out/'figure_readings.json').write_text(json.dumps({str(k):v for k,v in figs.items()},ensure_ascii=False,indent=2)+'\n')
(out/'margin_reading.txt').write_text(margin)
print('candidate bytes',len(s.encode()),'figures',len(figs))
