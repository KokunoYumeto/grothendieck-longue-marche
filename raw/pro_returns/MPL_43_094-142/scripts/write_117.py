from page_work import save_page
text=r'''\scanpage{117}
\[
A'_0=\mathcal A'\qquad\pi_0(A)\text{ et }\pi_0(B)\text{ duaux}
\]
\[
\boxed{\begin{array}{l}
(3)\quad\left\{\begin{aligned}
H^1(K,A)&\simeq\underline{\operatorname{Ext}}_{k\mathrm{gr}}(\mathcal B,\mathbb Q/\mathbb Z)
\simeq\underline{\operatorname{Ext}}^1_{k\mathrm{gr}}(\mathcal B'{}^0,\mathbb Q/\mathbb Z)
\times\underline{\operatorname{Ext}}_{k\mathrm{gr}}(V,\mathbb Q/\mathbb Z)\\
H^1(K,B)&\simeq\underline{\operatorname{Ext}}_{k\mathrm{gr}}(\mathcal A,\mathbb Q/\mathbb Z)
\simeq\underline{\operatorname{Ext}}^1_{k\mathrm{gr}}(\mathcal A'{}^0,\mathbb Q/\mathbb Z)
\times\underline{\operatorname{Ext}}_{k\mathrm{gr}}(U,\mathbb Q/\mathbb Z)
\end{aligned}\right.\\[1em]
(2)\quad\pi_0(A)\text{ et }\pi_0(B)\text{ duaux (à valeurs dans }\mathbb Q/\mathbb Z)\\[1em]
(1)\quad0\longrightarrow\pi_1(A'_0)\longrightarrow
\end{array}}
\]
\margin{\deleted{\unsure{Vue d'ensemble}}}
\figure{\begin{tikzpicture}[x=.6cm,y=.5cm]
\draw (0,0)--(.05,.6)..controls(3,1.8)and(6,1.3)..(6.2,-.4);
\draw (.1,.2)..controls(1.5,1.6)and(5.8,1.5)..(6.3,.6)--(6.5,-.1);
\draw (0,-.3)..controls(2.2,1.2)and(7,.6)..(8,-.3);
\end{tikzpicture}}
\figure{\begin{tikzpicture}\draw (0,0)--(11,.2);\end{tikzpicture}}
\diagram{\begin{tikzcd}
0\arrow[r]&U\arrow[r]\arrow[d,phantom,"\text{unip. connexe}"]&
\mathcal A\arrow[r,dash]&\mathcal A'\arrow[r,dash]\arrow[d,phantom,"\text{sans unip. connexe}"]&0\\
&\phantom{U}&&\phantom{A'}&
\end{tikzcd}}
\[
\mu(A)=2\underbrace{\alpha(A^0)}_{\substack{\text{\unsure{composante}}\\\deleted{\text{multiplicative}}\\\text{abélienne}}}
+\underbrace{\mu(A^0)}_{\substack{\text{comp.}\\\text{multiplicative}}}
\]
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,dash]&\operatorname{Ext}^1(\mathcal A'{}^0,\mathbb Q/\mathbb Z)\arrow[r]
\arrow[d,phantom,"(\mathbb Q/\mathbb Z)^{\unsure{\mu(A)}}"]&
\operatorname{Ext}^1(\mathcal A,\mathbb Q/\mathbb Z)\arrow[r]\arrow[d,equal]&
\underline{\operatorname{Ext}}(U,\mathbb Q/\mathbb Z)\arrow[r]
\arrow[d,phantom,"\substack{\text{groupe \unsure{pro-algébrique}}\\\text{\unsure{unip.} connexe}}"]&0\\
&\phantom{X}&H^1(K,B)&\phantom{X}&
\end{tikzcd}}
\mspage{116}
'''
save_page(117,text,[('display','top left','Aprime0=scriptAprime'),('text','top middle','pi0(A) et pi0(B) duaux'),('display','upper boxed item3 first','H1(K,A) and Ext of scriptB'),('display','upper boxed item3 second','H1(K,B) and Ext of scriptA'),('text','upper boxed item2','pi0(A) et pi0(B) duaux à valeurs dans Q/Z'),('display','upper boxed item1 unfinished','0→pi1(Aprime0)→'),('margin note','right vertical cancelled','Vue d’ensemble'),('deletion','right vertical note','Vue d’ensemble'),('drawing','faint pencil above and over item3','several arched connector lines'),('drawing','middle rule','long horizontal line'),('diagram','lower sequence and labels','0→U→scriptA-scriptAprime-0; unip.connexe; sans unip.connexe'),('display','bottom left','mu(A)=2alpha(A0)+mu(A0)'),('text','below alpha','composante abélienne'),('deletion','below alpha','multiplicative'),('text','below mu','comp. multiplicative'),('diagram','bottom Ext sequence','0-Ext1(scriptAprime0,Q/Z)→Ext1(scriptA,Q/Z)→underlinedExt(U,Q/Z)→0'),('display','below first Ext','(Q/Z)mu(A)'),('display','below second Ext vertical equal','H1(K,B)'),('text','below final Ext','groupe pro-algébrique unip. connexe'),('text','bottom left page number','116')],observations='Landscape whole and both left/right halves read. Enlarged rotated cancellation and both lower annotations inspected. Script A/B in Ext arguments and the quotient sequence have looped left strokes unlike the plain A/B in H1; these alphabets are distinguished. Single-underlined Ext is retained, and no Ext degree is added where absent. Reverse numbering 3,2,1 and the unfinished item1 arrow are retained. The first two connectors in the lower group sequence point right; its last two are plain lines.')
