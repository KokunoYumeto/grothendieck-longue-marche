from record_page import record
tex=r'''\scanpage{37}
% archive foliation: 36
\[
S^\circ\longrightarrow\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,\mathrm{Ab})
\]
Nous ferons cette étude dans le
cas où $S=\widehat\Delta=\mathrm{Ss}$, et \unsure{nous}
\uline{\unsure{choisirons pour $C$ les suivants}}.

$1^\circ)$ $C$ est formée des groupes ab. $\frac12$ simpli-
ciaux \deleted{\unsure{libres de rangs finis}}\inserted{str. $\partial$-parfaits}, $A$ est la
sous-catégorie formée des
$\Phi(i,n)$ ($n\in\mathbf N^*$, \deleted{\unsure{j\geqslant0}} $i\geqslant1$) et $\Lambda^j\Psi_*$ ($j\geqslant0$).
\margin{$C$ abélienne}

On voit que \inserted{pour $X\in\operatorname{Ob}\widehat\Delta$ fixé} la connaissance des
$\operatorname{Hom}_{\widehat\Delta}(X_*,M_*)$ comme foncteur
covariant en $M_*$ se réduit à
celle de $\operatorname{Hom}_{\widehat\Delta}(X_*,\deleted{\unsure{L}}\varphi)$ pour
$\varphi$ dans $A$. On peut encore
réduire \deleted{\unsure{à}}\inserted{à prendre} $\varphi$ dans $A_0$ défini
ci-dessous, et même pour $\varphi$ prenant
les $\Phi^i$.

$2^\circ)$ $C_0$ \inserted{$\subset C$} est formée des groupes ab.
$\frac12$ simpliciaux \deleted{\unsure{str.}} spéciaux
(\deleted{donc}\inserted{i.e.} $\in C$ et les $\pi_i(L_*)$ sont
sans torsion), $A_0\subset C_0$ sous-cat.
de ceux qui sont de la forme
\[
\Phi^i=\Lambda^i\Phi_*\deleted{\unsure{\Psi}}\quad(i\geqslant1)
\quad\text{ou}\quad\Psi^j=\Lambda^j\Psi_*\quad(j\geqslant0).
\]
\margin{$C_0$ est additive mais non abélienne.}
'''
record(37,tex,[('display','top','S°→Hom_Z-add(A,Ab)'),('text','upper','Nous ferons cette étude; S=widehat Δ=Ss; choix C'),('text','1°','C groupes ab ½ simpliciaux; A sous-catégorie'),('deletion','1° after simpliciaux','libres de rangs finis'),('insertion','1° above deleted qualification','str ∂-parfaits'),('text','1° generators','Φ(i,n), n∈N*, i≥1; Λ^jΨ*, j≥0'),('deletion','1° condition','j≥0'),('margin note','left of 1°','C abélienne'),('text','middle','On voit que connaissance Hom(X*,M*) se réduit'),('insertion','above la connaissance','pour X∈Ob widehat Δ fixé'),('deletion','argument before φ','L'),('text','middle-lower','On peut encore réduire; A0; même Φ^i'),('deletion','after réduire','à'),('insertion','above after réduire','à prendre'),('text','2°','C0 groupes ab ½ simpliciaux spéciaux'),('insertion','after C0','⊂C'),('deletion','before spéciaux','str'),('deletion','inside parenthesis','donc'),('insertion','above donc','i.e.'),('text','lower','π_i(L*) sans torsion; A0⊂C0 sous-cat'),('display','bottom','Φ^i=Λ^iΦ* (i≥1) ou Ψ^j=Λ^jΨ* (j≥0)'),('deletion','bottom after Φ*','Ψ'),('margin note','left of 2°','C0 est additive mais non abélienne')],doubts=[('top coefficient','Z-add','k-add; same unresolved repeated glyph','low'),('opening last phrase','nous choisirons pour C les suivants','underlined words faint; choisirons dans C possible','low'),('1° cancelled qualification','libres de rangs finis','long cancellation; no confident exact recovery','low'),('1° cancelled index condition','j≥0','j≥1; heavily struck','low'),('Hom argument cancelled letter','L','E; visible compact cancellation','low'),('reduction sentence insertion','à prendre','pour; insertion faint','medium'),('2° cancelled before spéciaux','str.','très; short cancellation','low'),('bottom cancelled symbol','Ψ','φ; heavy crossing','low')],notation=[('simplicial-set category',r'$\widehat\Delta=\mathrm{Ss}$','scan 37 opening'),('generator shorthand',r'$\Phi^i=\Lambda^i\Phi_*,\ \Psi^j=\Lambda^j\Psi_*$','scan 37 bottom; superscripts read separately from subscripts')])
