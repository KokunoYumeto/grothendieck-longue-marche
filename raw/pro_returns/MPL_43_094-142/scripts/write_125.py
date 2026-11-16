from page_work import save_page
text=r'''\scanpage{125}
\[
\operatorname{Ext}^i_Y(X,F,G)=\varinjlim_n\operatorname{Ext}^i(F/\mathcal J^nF,G)
\]
\margin{\unsure{dual}}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\simeq\varprojlim_n\operatorname{Ext}^{r-i}_a(X;G,F/\mathcal J^nF)&
H^p_a(X,\underline{\operatorname{Ext}}^q_{\underline O_X}(G,F_{\unsure{n}}))\arrow[l,Rightarrow]\\
\varprojlim_n\operatorname{Ext}^{r-i}_a(\widehat X,\widehat G,\widehat F_n)\arrow[u,"\sim"]&
H^p_a(\widehat X,\underline{\operatorname{Ext}}^q_{\underline O_X}(\widehat G,\widehat F_{\unsure{n}}))\arrow[l,Rightarrow]\\
\operatorname{Ext}^{r-i}_a(\widehat X,\unsure{\widehat G|\widehat C},\widehat F_{\unsure{n}})\arrow[u]&
\end{tikzcd}}
\margin{$\lim$}
\[
\operatorname{Ext}^i_{Y-Z}(X,F,G)=\varinjlim_n\operatorname{Ext}^i(X-Z,F/\mathcal J^nF,G)
\]
\noindent \unsure{dual}
\[
\simeq\varprojlim\qquad\varprojlim\operatorname{Ext}^{r-i}(\widehat X,\unsure{\widehat G|\widehat C},\widehat F)
\]
\[
H^i(X-Z,F
\]
\margin{$Z\subset Y$}
\noindent $\mathfrak X$ \unsure{schéma} formel
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
T\subset Z\subset\mathfrak X\arrow[r,bend right=20]&\text{partie \unsure{fermée}}\\
\mathfrak X_{/Z}\arrow[u]&\text{complété formel le long de }Z
\end{tikzcd}}
\[
H^i_T(\mathfrak X,\mathfrak F)\longrightarrow H^i_T(\mathfrak X,\mathfrak F_{/Z})\overset{?}{\mathrel{-}}H^i(\mathfrak X
\]
\mspage{124}
'''
save_page(125,text,[('display','top direct-limit formula','ExtiY(X,F,G)=lim→n Exti(F/JnF,G)'),('margin note','upper left beside second row','dual'),('diagram','upper middle vertical chain and spectral terms','lim←Extr-i a(X;G,F/JnF) ← Hp a(X,Extq OX(G,Fn)); lim←Extr-i a(hatX,hatG,hatFn); upward maps'),('margin note','upper middle left of lowest Ext','lim'),('display','middle direct-limit formula','ExtiY-Z(X,F,G)=lim→n Exti(X-Z,F/JnF,G)'),('text','middle left below formula','dual'),('display','middle unfinished inverse limits','≃lim← lim←Extr-i(hatX,hatG,hatF)'),('display','lower unfinished cohomology','Hi(X-Z,F'),('margin note','lower left','Z subset Y'),('text','lower formal scheme label','frakturX schéma formel'),('diagram','lower inclusions and formal completion','T subset Z subset frakturX; partie fermée; frakturX/Z→frakturX; complété formel le long de Z'),('display','bottom cohomology map','HiT(frakturX,frakturF)→HiT(frakturX,frakturF/Z)-?Hi(frakturX'),('text','bottom left page number','124')],observations='Whole and both halves read; spectral terms and formal-scheme words enlarged. Blue typescript is mirrored reverse show-through. Direct and inverse limit arrows distinguished. Both cohomology displays at the bottom genuinely stop without closing parentheses; no completion supplied. O_X is singly underlined beneath sheaf Ext in both spectral expressions and shows no hat. F subscripts and one G/C-shaped letter marked. Source plain queried segment in final formula retained as a dash.')
