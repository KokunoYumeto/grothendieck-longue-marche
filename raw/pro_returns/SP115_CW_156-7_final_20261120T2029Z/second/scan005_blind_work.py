from pathlib import Path
import csv,json
ROOT=Path('/workspace/scratch/ddf8babdc42e')
STAR=r'\tikz[baseline=-.4ex,x=.75em,y=.75em]{\draw (.5,.5) circle (.48);\draw (.18,.48)--(.82,.48) (.4,.2)--(.65,.8) (.32,.76)--(.72,.23);}'
STAR2=r'\tikz[baseline=-.4ex,x=.75em,y=.75em]{\draw (.5,.5) ellipse (.43 and .55);\draw (.3,.15)--(.3,.8) (.2,.5)--(.8,.5) (.3,.66)--(.58,.9) (.3,.45)--(.62,.18);}'
REL=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
R={}
R['B001']=r'\mspage{\deleted{\unsure{3}}4}'
R['B002']=STAR
R['B003']=STAR+r" $M=$ ensemble des \uline{figures} $\in\unsure{\mathscr F|\mathcal F}$ \uline{élémentaires}'' ou \uline{multistrates}"
R['B004']=r"\margin{\uline{strates} d'une figure : les $X\in M$ tels que $X\leq F$ \uline{déployement} de $F$ : ens. de ses \uline{strates} $\widetilde F=\{X\in M\mid X\leq F\}$. On écrit $X\triangleleft F$ ($\unsure{X_i-|X\vdash}$ \uline{ci devant} : $F$) pour $X\in M$ et $X\leq F$ \tikz[x=1em,y=1em]{\draw (4.5,3.4) .. controls (4.4,2.7) and (4.2,2.7) .. (2.8,2.55)--(2.8,1.4)--(4.8,1.2)--(4.8,-.4);}}"
R['B005']=r'\margin{formé des objets de $(\unsure{\mathscr F|\mathcal F},\leq)$ strictement irréductibles. \unsure{Munis|Muni} des relations $\leq_M$, $\ll_M$ induites par $\deleted{\unsure{\mathscr F|\leq}}$ $\leq$ et $\ll$ dans $\mathscr F$}'
R['B006']=r'$\deleted{\unsure{\mathscr F|\leq}}$'
R['B007']=STAR2

R['B008']=STAR2+r" $L\subset M$, ens. des \deleted{\uline{\unsure{points}}} \inserted{``lieux''} \deleted{\illegible{1}}"
R['B009']=r'\deleted{\uline{\unsure{points}}}'
R['B010']=r"\inserted{``lieux''}"
R['B011']=r'\deleted{\illegible{1}}'
R['B012']=r'\margin{éléments minimaux de $\mathscr F\setminus\{\varphi_{\mathscr F}\}$ pour $\ll$} \tikz[x=1em,y=1em]{\draw (0,2.1)--(2,2) .. controls (3,1.7) and (4,.7) .. (5,.3)--(6.5,.3);\draw (2,2) .. controls (3.2,1.2) and (4.2,.5) .. (5,.3);}'
R['B013']=r"I) Axiomes ``rien que rien''. Les premiers trois \inserted{At 1 -- At 3} ne concernent que $(\mathscr F,\leq)$, les quatre suiv. \unsure{ss|sur} At 4 -- At 7 \deleted{\uline{\unsure{At 1}}} \deleted{\unsure{3}} \unsure{4} les relations entre $\leq$ et $\ll$"
R['B014']=r'I)'
R['B015']=r'\inserted{At 1 -- At 3}'
R['B016']=r'At 4 -- At 7'
R['B017']=r'\deleted{\uline{\unsure{At 1}}}'
R['B018']=r'\deleted{\unsure{3}} \unsure{4}'
R['B019']=r'\uline{At 1} $\mathscr F\neq\varphi$ et stable par $\operatorname{Sup}_{I}$ \unsure{un. ponis|un. finis} ($I$ quelconque)'
R['B020']=r'\margin{Axiomes des \uline{sommes propres de figures}}'
R['B021']=r'\uline{At 2} Toute figure \unsure{e|t}st le Sup de ses strates : $F=\operatorname{Sup}_{X\in\widetilde F}X$ où $\widetilde F=\{X\in M\mid X\leq F\}$'
R['B022']=r'\unsure{e|t}'
R['B023']=r"\margin{Axiome des strates équivaut à : Si $F,G\in\mathscr F$, alors $F\leq G\Longleftrightarrow\forall X\in\widetilde F,\ \exists Y\in\widetilde G$ avec $X\leq Y$ Critère d'\uline{inclusion des figures par strates}}"
R['B024']=r"\uline{Scholie} \uline{At} 1 et \uline{At} 2 signifient que $\mathscr F$ s'interprète, via $F\mapsto\widetilde F$, comme une partie \inserted{$\widetilde{\mathscr F}$} de $\mathscr P(M)$, $M$ ens. ordonné (par $\leq$), avec les conditions :"
R['B025']=r'\uline{At} 1 et \uline{At} 2'
R['B026']=r'\inserted{$\widetilde{\mathscr F}$}'
R['B027']=r'a) les $\varphi\in\widetilde{\mathscr F}$ sont fermés'
R['B028']=r'b) Si $\varphi\in\widetilde{\mathscr F}$, toute partie fermée de $\varphi$ est $\in\widetilde{\mathscr F}$'
R['B030']=r'\deleted{$\unsure{\widetilde{\mathscr F}}\neq\varphi\ (\Longleftrightarrow\varphi\in\widetilde{\mathscr F})$}'
R['B031']=r'(\deleted{\unsure{et}}'
R['B029']=r'c) '+R['B030']+' '+R['B031']+r' $\bigcup_{\varphi\in\widetilde{\mathscr F}}\varphi=M$, et $\widetilde{\mathscr F}\neq\varphi$'
R['B032']=r'\margin{$\widetilde{\mathscr F}\neq\varphi$ automatique si $M\neq\varphi$ et dans tous les cas, équivaut à $\varphi\in\widetilde{\mathscr F}$}'
R['B033']=r"ou, indépendamment d'une relation d'ordre sur $M$, un ens. de parties satisfaisant"
R['B035']=r'$\deleted{\unsure{A|F}}\varphi$'
R['B036']=r'$\deleted{\unsure{F}}$'
R['B034']=r"b') $\forall x\in M$, l'ens. $\widetilde{\mathscr F}^{x}=\{\deleted{\unsure{A|F}}\varphi\in\mathscr F\mid x\in\varphi\}$ a un plus petit élément $\deleted{\unsure{F}}$ (noté $\widehat{x}$)"
R['B038']=r"a')"
R['B039']=r'$\deleted{\unsure{\forall F|\forall}}$'
R['B040']=r'\unsure{toute|toutes}'
R['B037']=r"a') $\deleted{\unsure{\forall F|\forall}}$ Dans $(\widetilde{\mathscr F},\subset)$, \unsure{toute|toutes} famille majorée a un Sup, \uline{et} $\widetilde{\mathscr F}\neq\varphi$ $(\Longleftrightarrow\varphi\in\widetilde{\mathscr F})$"
R['B041']=r"\begin{tikzpicture}[x=1em,y=1em]\node at (1,2.6) {b')};\node at (1,0) {a')};\draw[->] (.35,.12) .. controls (-.65,.55) and (-.65,1.05) .. (-.6,1.8) .. controls (-.55,2.45) and (-.35,2.9) .. (.2,3.2);\end{tikzpicture}"
R['B019']=r'\uline{At 1} $\mathscr F\neq\varphi$ et stable par $\operatorname{Sup}_{I}$ majorés ($I$ quelconque)'
R['B024']=R['B024'].replace(r'\mathscr P(M)',r'\unsure{\mathscr P|\mathscr F}(M)')
R['B004']=R['B004'].replace(r'F\}$. On',r'F\}$ On')
R['B043']=r'\mathrm{\unsure{dfn|déf}}'
R['B044']=r'$\unsure{G|C}$'
R['B045']=r'$\unsure{G|C}$'
R['B042']=r'Relation $F'+REL+r'G\ \overset{\mathrm{\unsure{dfn|déf}}}{\Longleftrightarrow}\ F\vee\unsure{G|C}$ existe i.e. $\{F,\unsure{G|C}\}$ majoré dans $(\mathscr F,\leq)$ \uline{figures compatibles}'
R['B047']=r'\inserted{avec At 1, At 2, At 3}'
R['B048']=r'\deleted{\unsure{est}}'
R['B046']=r'cette relation induit $X'+REL+r'Y$ dans $M$. Dans le cas où les figures sont des \unsure{l.f.|t.f.}, alors $(\mathscr F,\leq)$ \deleted{\unsure{est}} \inserted{avec At 1, At 2, At 3} se reconstruit par \tikz[x=1em,y=1em]{\draw (8,1.2) .. controls (8,1) and (8,1) .. (7.7,1)--(.6,1) .. controls (.2,1) and (.2,.3) .. (0,.3);\draw (.45,.6)--(0,.3)--(.55,.28);\draw (.3,.7)--(0,.3)--(.45,.2);}'
R['B049']=r'$(M,\leq,'+REL+r')$, où $'+REL+r'$ satisfait $\left\{\begin{array}{l}\unsure{X}\ '+REL+r'\ \text{réflexive symétrique}\\ X'+REL+r'Y,\ X^{\prime}\leq X,\ Y^{\prime}\leq Y\Longrightarrow X^{\prime}'+REL+r'Y^{\prime}\end{array}\right.$'
