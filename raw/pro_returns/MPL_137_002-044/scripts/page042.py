from record_page import record
tex=r'''\scanpage{42}
% archive foliation: 41
On trouve donc un foncteur pl. fid
\[
C^\circ\lhook\joinrel\xrightarrow{\deleted{\unsure{\beta}}\alpha'}\mathrm{Ab}^\bullet_k\deleted{\unsure{*}},
\]
qui associe à tout \deleted{\unsure{M_*}} $L_*$ associe le complexe
de cochaînes $\operatorname{Hom}_C(L_*,C^\bullet_*)$
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&\operatorname{Hom}(L_*,C^0_*)\arrow[r]&\operatorname{Hom}(L_*,C^1_*)\arrow[r]&\cdots
\end{tikzcd}}
et dont la restriction à $A$ est donnée par
\[
\alpha'\deleted{\unsure{\beta}}(C^i_*)=\left(0\longrightarrow0\longrightarrow\cdots\ 0\longrightarrow
\underset{\text{degré }i}{k}\xrightarrow{\mathrm{id}}
\underset{\text{degré }i+1}{k}\longrightarrow0\longrightarrow\cdots\right)
=\deleted{\unsure{K}}\inserted{C'_i},
\]
et par la loi
\diagram{\begin{tikzcd}[row sep=small,column sep=large]
\alpha'(C^i_*)\arrow[d,equal]&\alpha(C^{i+1}_*)\arrow[l,"\alpha'(d^i)"']\arrow[d,equal]\\
\unsure{(C'_i)^\bullet|K'_i}\arrow[r]&\unsure{(C'_{i+1})^\bullet|K'_{i+1}}\\
\vdots\arrow[d]&0\arrow[d]\\
k\arrow[d]&0\arrow[l]\arrow[d]\\
k\arrow[d]&k\arrow[l,"\mathrm{id}"']\arrow[d]\\
0\arrow[d]&k\arrow[l]\arrow[d]\\
0&0\\
\vdots&\vdots
\end{tikzcd}}
\[
k\longrightarrow0
\]
\margin{L'image essentielle \inserted{d'$\alpha'$} de $C^\circ$
est la catégor. des $K^\bullet\in\operatorname{Ob}\mathrm{Ab}_k^\bullet$
qui sont libres de t.f.
en ttes dimensions, et
qui sont à \unsure{ch.} nulle
(on admettra que tt facteur
direct d'un libre de t.f.
est libre).}

\margin{\unsure{Commencer} par Ex 2}
\uline{Ex 2} Faisons $B=\mathrm{Ab}_k^\circ$,
qui est $k$-linéaire (on suppose
$k$ commutatif), et pour $\forall L_*\in\operatorname{Ob}C$, on consi-
dère le foncteur controv. qu'il représente, \unsure{interprété}
comme foncteur $k$-lin.
\[
C^\circ\longrightarrow\deleted{\unsure{\mathrm{Ab}^\circ_k}}\mathrm{Ab}_k^{\unsure{\circ|\bullet}}:
\quad M_*\longmapsto\operatorname{Hom}_C(M_*,L_*)
\]
on trouve ainsi un foncteur pl. fid (pour la
même raison)
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
C\arrow[r,hook]&\underline{\operatorname{Hom}}_{k\text{-}lin}(C^\circ,\mathrm{Ab}_k^{\unsure{\circ|\bullet}})\arrow[r,"\simeq"]\arrow[d,"\simeq"']&
\underline{\operatorname{Hom}}_{k\text{-}lin}(C,\mathrm{Ab}_k^\circ)^\circ\arrow[d,"\simeq"]\\
&\underline{\operatorname{Hom}}_{k\text{-}lin}(A^\circ,\mathrm{Ab}_k^{\unsure{\circ|\bullet}})\arrow[r,"\simeq"]\arrow[d]&
\underline{\operatorname{Hom}}_{k\text{-}lin}(A,\mathrm{Ab}_k^\circ)^\circ\arrow[d,"\simeq"]\\
&\unsure{\{(\mathrm{Ab}_k^\circ)_*\simeq\deleted{\mathrm{Ab}_{k*}}^{*}\}^{\circ}}&
(\mathrm{Ab}_k^{\circ\unsure{*|\bullet}})^\circ
\end{tikzcd}}
on trouve un foncteur pl. fid.
\[
C^{\unsure{\circ}}\lhook\joinrel\xrightarrow{\beta}\mathrm{Ab}_{k*}.
\]
'''
record(42,tex,[('text','top','On trouve donc foncteur pl fid'),('display','top','C°↪Ab_k• via α′'),('deletion','top functor label','β'),('deletion','top codomain after bullet','star'),('text','upper','qui associe à tout L* associe complexe cochaînes'),('deletion','before L*','M*'),('diagram','upper','0→Hom(L*,C0*)→Hom(L*,C1*)→…'),('text','upper-middle','restriction à A donnée par'),('display','upper-middle','α′(Ci*)=(0→…→k id→k→0…)=C′i; degree labels'),('deletion','before argument Ci*','β'),('deletion','final name old letter','K'),('insertion','final name','C′i'),('text','middle','et par la loi'),('diagram','middle-left','α′(Ci*)←α(Ci+1*); equalities; two vertical complexes with left arrows and id'),('display','middle-right','k→0'),('margin note','middle-right','image essentielle libres t.f. ch nulle; on admettra facteur direct libre'),('insertion','in right marginal note','d’α′'),('margin note','left of Ex 2','Commencer par Ex 2'),('text','Ex 2','Faisons B=Ab_k°; k commutatif; L*; foncteur controv'),('display','lower','C°→Ab_k; M*↦Hom_C(M*,L*)'),('deletion','lower old codomain','Ab_k°'),('text','lower','on trouve ainsi foncteur pl fid pour même raison'),('diagram','lower','C↪Hom(C°,Ab_k); opposite Hom equivalences; restriction A; chain categories'),('deletion','lowest left object in large diagram','Ab_k*'),('text','bottom','on trouve foncteur pl fid'),('display','bottom','C°↪Ab_k* via β')],doubts=[('top functor','α′','extra crossed label β; prime distinct from prior normalized-complex !','medium'),('name of elementary cochain object','C′i','K′i; overwritten C/K throughout diagram','low'),('map of elementary complexes top row','α(Ci+1*) without prime','no clear prime on this occurrence; not standardized to α′','medium'),('margin image condition','ch. nulle','coh. nulle; abbreviation faint','low'),('left margin','Commencer par Ex 2','Commençons par Ex 2','medium'),('Ex 2 codomain decorations','Ab_k^circ','Ab_k^bullet; blue dot/overwriting makes several superscripts uncertain','low'),('lowest left object in large diagram','{(Ab_k°)_*≃deleted Ab_k* ^*}°','successive overwritten stars and circles; tentative exact placement','low'),('bottom source','C°','C; isolated blue mark may be a cancellation rather than superscript','low')],notation=[('two evaluation functors',r'$\alpha\prime,\beta$','scan 42; prime on α visually distinguished, β final'),('ordinary versus opposite / complex module categories',r'$\mathrm{Ab}_k^\circ,\mathrm{Ab}_k^\bullet,\mathrm{Ab}_{k*}$','scan 42; overwritten instances locally uncertain rather than regularized')])
