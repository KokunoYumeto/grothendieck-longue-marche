from record_page import record
tex=r'''\scanpage{38}
% archive foliation: 37
Il y a lieu de \unsure{généraliser|linéariser}
$1^\circ)$ au cas où on a un anneau
de base $k$ de Dedekind,
et $2^\circ)$ un $k$ quelconque \inserted{(\unsure{commutatif})}
(donc $C\subset\widehat\Delta_{k\text{-}mod}$). La \unsure{seule}
conclusion à retenir, c'est
qu'on connaît les $\operatorname{Hom}$ de
$X_*$ dans les $k$-modules str.
$\partial$-\deleted{\unsure{parf.}}\inserted{\unsure{parfaits}} \inserted{$M$ (comme foncteur en $M$)} dès qu'on connaît
le complexe \inserted{de cochaînes ``non dég''} $C^{*\unsure{!}}(X_*,k)$ à coeff. dans
$k$. Notre propos principal
est de voir comment reconstituer
les structures multiplicatives
et ``puissances divisées'' sur ce
foncteur
\[
M\longmapsto F_{X_*}(M_*)=F(M_*)=\operatorname{Hom}_{\unsure{\widehat\Delta|S}}(X_*,M_*)
\]
i.e. les lois
\[
\left\{\begin{aligned}
F(M_*)\otimes_k F(N_*)&\longrightarrow F(M_*\otimes N_*)\\
\Gamma^iF(\deleted{\unsure{\Gamma^i}}M_*)&\longrightarrow F(\Gamma^i(M_*))
\end{aligned}\right.
\]
en termes de \deleted{\unsure{la}} structures
sur le complexe \inserted{de cochaînes} $C^*=C^{*\unsure{!}}(X_*,k)$.
Il faudrait examiner si pour
$k$ de car $0$ \inserted{\unsure{$C^*$}} cette structure suppl.
'''
record(38,tex,[('text','top','Il y a lieu de généraliser 1° base k Dedekind; 2° k quelconque'),('insertion','right after quelconque','commutatif'),('text','upper','donc C⊂widehatΔ_k-mod; conclusion à retenir'),('text','upper-middle','Hom de X* dans k-modules str ∂-parfaits'),('deletion','after ∂','parf'),('insertion','above cancelled qualification','parfaits'),('insertion','above dès','M (comme foncteur en M)'),('text','middle','dès qu’on connaît le complexe C*(X*,k) à coeff dans k'),('insertion','above complexe','de cochaînes non dég'),('text','middle','Notre propos principal; structures multiplicatives et puissances divisées'),('display','lower-middle','M↦F_X*(M*)=F(M*)=Hom(X*,M*)'),('text','lower-middle','i.e. les lois'),('display','lower','tensor law; Γ^i F(M*)→F(Γ^i(M*))'),('deletion','within Γ^iF argument','Γ^i'),('text','lower','en termes de structures sur le complexe C*=C*!(X*,k)'),('deletion','before structures','la'),('insertion','above complexe','de cochaînes'),('text','bottom','Il faudrait examiner si pour k de car 0 cette structure suppl'),('insertion','above cette','C*')],doubts=[('first line final verb','généraliser','linéariser; staff lines obscure letter bodies','low'),('insertion after quelconque','commutatif','short abbreviation beginning comm; ending unclear','low'),('La ... conclusion','seule','deleted-looking staff intersection; word faint','medium'),('∂ qualification correction','parf. replaced by parfaits','may be initial incomplete form; retained visibly distinct layers','low'),('cochain superscript twice','C^{*!}','C^*; second stroke may be ! or prime, dot faint','low'),('Hom subscript','widehat Δ','S; ornate small glyph intersects staff','low'),('cancelled inside Γ^iF argument','Γ^i','small overwritten symbol; best tentative reading','low'),('before structures','deleted la','deleted les; staff and scribble overlap','low'),('final insertion above cette','C*','C* ... ; attachment uncertain','low')],notation=[('explicit multiplicative laws',r'$F(M_*)\otimes_kF(N_*)\to F(M_*\otimes N_*),\ \Gamma^iF(M_*)\to F(\Gamma^i(M_*))$','scan 38; no identity sign added'),('cochain complex',r'$C^*,C^{*\unsure{!}}(X_*,k)$','scan 38; exclamation/prime distinction not secure at the staff intersection')])
