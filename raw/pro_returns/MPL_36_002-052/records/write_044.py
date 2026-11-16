from save_page import save
tex=r'''
\scanpage{44}
\uline{Foncteurs adjoints}

\uline{Définition 1} soient $X,Y\in(\mathrm{Cat})$, $f:X\longrightarrow Y$ et $g:Y\longrightarrow X$, on dit que $(f,g)$ est un couple de foncteurs adjoints, ou que $g$ est adjoint de $f$, ou que $f$ est coadjoint de $g$, s'il existe un

\deleted{$\unsure{\forall}$}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (.3,2.5) {$\mathcal H^1(X,\underline{\operatorname{Hom}}(\gamma,G))\simeq$};
\node[anchor=west] at (.3,1.7) {$\mathcal H^1(X,\underline{\operatorname{Ext}}^1(\gamma,G))$};
\node[anchor=west] at (1,.45) {$\operatorname{Ext}^1(\gamma,$};
\draw (0,0)--(3.5,.12)--(6,4.1)--(10,4.05);
\draw (0,.27)--(3.5,.12);
\end{tikzpicture}}
\diagram{\begin{tikzcd}[row sep=large]
X\arrow[r]&\underline{\operatorname{Hom}}_{S-gr}(\gamma,G)\\
X\times\gamma\arrow[r]&G\\
\deleted{\unsure{\gamma}}\ \gamma\arrow[r]\arrow[dr,no head]&\underline{\operatorname{Hom}}_S(X,G)\\
S&\overset{\unsure{\Pi_2}}{C}
\end{tikzcd}}
\[\operatorname{Hom}(\gamma,\]
\[\Pi^0_{X/S}\gamma_X\]
\[\text{''}\]
\[\underline{\operatorname{Hom}}_S(X,\gamma)\unsure{=|-}\gamma\]
\diagram{\begin{tikzcd}[column sep=small]
\unsure{e|0}\arrow[r]&\gamma\arrow[r]&\underline{\operatorname{Hom}}_S(X,\gamma)\arrow[r]&\operatorname{Hom}(X,a;\gamma)\arrow[r]&0
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw (0,0)--(.35,.12);\end{tikzpicture}}
\margin{43}
'''
e=[('text','heading','Foncteurs adjoints'),('text','top definition','Définition 1 soient X,Y∈(Cat)'),('deletion','below definition','∀-like sign'),('display','middle left, first line','H¹(X, Hom(γ,G)) ≃'),('display','middle left, second line','H¹(X, Ext¹(γ,G))'),('display','middle left, unfinished','Ext¹(γ,'),('drawing','middle, around three formulas','slanting divider joining doubled lower stroke and upper horizontal'),('diagram','middle right','X→Hom; X×γ→G; γ→Hom; S; C'),('deletion','before γ in middle-right diagram','γ'),('display','under middle-right diagram','Hom(γ,'),('display','lower left','Π⁰_{X/S} γ_X'),('display','between lower-left formulas','ditto strokes'),('display','lower left below ditto','Hom_S(X,γ) = γ'),('diagram','bottom','e→γ→Hom_S(X,γ)→Hom(X,a;γ)→0'),('drawing','below bottom sequence','short isolated oblique stroke'),('margin note','bottom left','43')]
d=[{'line':'under definition','reading':'∀ (deleted)','alternatives':'crossed abandoned symbol has two vertical strokes','confidence':'low'},{'line':'above C in middle-right diagram','reading':'Π_2','alternatives':'hooked symbol with small subscript 2, not a securely read arrow','confidence':'low'},{'line':'lower-left Hom formula','reading':'=','alternatives':'thick horizontal dash with detached dot','confidence':'low'},{'line':'bottom sequence first term','reading':'e','alternatives':'0','confidence':'medium'}]
save(44,tex,e,d,'Heading “Foncteurs adjoints”; the definition stops at “s’il existe un” and is not completed. The sheet revisits the Hom/Ext exchange of scan041 through adjunction sketches and a bottom sequence with a pointed term Hom(X,a;γ). Both Ext¹(γ, and Hom(γ, are abandoned fragments. Π⁰_{X/S} and the comparison Hom_S(X,γ)=γ are candidate relative connectedness/constant-group leads, but no hypotheses are supplied here.')
