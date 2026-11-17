from record_page import record
tex=r'''\scanpage{21}
% archive foliation: 20
On a
\[
\operatorname{Hom}_k(\Phi(i,n),L_\bullet)
\simeq d^{-1}_{\unsure{L^!_\bullet,i}}(nL^!_{i-1})\subset L^!_i.
\]
\diagram{\begin{tikzcd}
&1\arrow[d,phantom,"\in"]&n\cdot1&\\
0\arrow[r]&k\arrow[r,"n"]\arrow[d,"u"]&k\arrow[r,dash]\arrow[d,"u_{i-1}"]&0\\
0\arrow[r]&\underset{\xi_i}{L^!_i}\arrow[r,"d_i"]&
\underset{n\xi_{i-1}}{L^!_{i-1}}\arrow[r]&0
\end{tikzcd}}
donc
\deleted{$\operatorname{Hom}(\Phi(i,n),\Phi_j(m))=0$
\unsure{si $j\neq i,i+1$}}
\[
\operatorname{Hom}(\Phi(i,n)_*,\Phi(j,m)_*)\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq i,i+1\\
\simeq\{\xi\in k\mid m\xi\in nk\}=n'k\simeq k&
\text{si }j=i\\
k&\text{si }j=i+1
\end{array}\right.
\]
\inserted{(où $n'=\dfrac{n}{(n,m)}$)}
[engendré par la composée
\diagram{\begin{tikzcd}
\Phi(i,n)\arrow[r,"\mathrm{can}"]&\Lambda^i\Psi_k\arrow[r,"\mathrm{can}"]&\Phi(i+1,m)_*
\end{tikzcd}}]

[p.ex. on trouve
\[
\operatorname{Hom}_k(\Phi(i,n)_*,\Phi(i,n)_*)
\simeq\deleted{\unsure{\mathbf Z}}k\operatorname{id}_{\Phi(i,n)}\simeq k
\]
(\unsure{isom.} \inserted{d'anneaux} \deleted{\unsure{d'anneaux}}
$k$-algèbres si $k$ comm.)
$\forall i\geq0,\ n\in k-\{0\}$
\deleted{$\operatorname{Hom}(\Lambda^i\Phi,\Lambda^{i+1}\Phi)$\unsure{$\simeq$}}
[en particulier
\[
\operatorname{Hom}_k(\Lambda^i\Phi_*,\Lambda^i\Phi_*)
\simeq k\operatorname{id}_{\Phi(i,1)}\simeq k
\]
\[
\operatorname{Hom}_k(\Lambda^i\Phi_*,\Lambda^{i+1}\Phi_*)
\simeq k\cdot\lambda\simeq k,\quad\text{où}
\]
\diagram{\begin{tikzcd}
\lambda=\unsure{T_\wedge}:\quad\Lambda^i\Phi_*\arrow[r]&\Lambda^{i+1}\Phi_*
\end{tikzcd}}]
\[
\operatorname{Hom}_k(\Phi(i,n),\Lambda^j\Psi_*)\simeq
\left\{\begin{array}{ll}0&\text{si }j\neq i\\k&\text{si }j=i\end{array}\right.
\]
[en particulier
\[
\operatorname{Hom}_k(\Lambda^i\Phi_*,\Lambda^j\Psi_*)\simeq
\left\{\begin{array}{ll}0&\text{si }j\neq i\\k&\text{si }j=i\end{array}\right.
\]
et le générateur dans le cas $j=i$ est
l'hom can
\diagram{\begin{tikzcd}\Lambda^i\Phi_*\arrow[r,"\mathrm{épi}"]&\Lambda^i\Psi_*\end{tikzcd}}]
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,L_\bullet)
\simeq Z_i(L_*)\simeq k^{\mu_{i+1}+\beta_{i+1}+\nu_i}
\]
en particulier
'''
record(21,tex,[('text','top','On a'),('display','top Hom','Hom_k(Φ(i,n),L)≃d−1(nL!_i−1)⊂L!_i'),('diagram','upper left','two chain rows k→k over L!_i→L!_i−1; u,d_i,ξ_i'),('text','upper right','donc'),('deletion','upper right formula','Hom(Φ(i,n),Φ_j(m))=0 si j≠i,i+1'),('display','middle three cases','Hom(Φ(i,n),Φ(j,m))=0; n′k; k'),('insertion','inside middle case','n′=n/(n,m)'),('text','bracket below cases','engendré par la composée'),('diagram','below cases','Φ(i,n)→Λ^iΨ→Φ(i+1,m); can labels'),('text','p.ex bracket','p.ex. on trouve'),('display','endomorphism ring','Hom_k(Φ(i,n),Φ(i,n))≃k id≃k'),('deletion','endomorphism display','Z'),('insertion','below endomorphism display','d’anneaux'),('deletion','below endomorphism display','d’anneaux'),('text','endomorphism qualifications','k-algèbres si k comm.; ∀i≥0,n∈k−{0}'),('deletion','middle-lower Hom display','Hom(Λ^iΦ,Λ^(i+1)Φ)≃'),('text','first en particulier bracket','en particulier'),('display','lower endomorphism','Hom(Λ^iΦ,Λ^iΦ)≃k id≃k'),('display','lower adjacent degrees','Hom(Λ^iΦ,Λ^(i+1)Φ)≃kλ≃k'),('diagram','definition λ','λ=T_wedge: Λ^iΦ→Λ^(i+1)Φ'),('display','lower mixed Hom','Hom(Φ(i,n),Λ^jΨ) cases'),('text','second en particulier','en particulier'),('display','lower mixed special Hom','Hom(Λ^iΦ,Λ^jΨ) cases'),('text','generator description','le générateur ... hom can'),('diagram','canonical epimorphism','Λ^iΦ→Λ^iΨ; épi'),('display','bottom cycles Hom','Hom(Λ^iΨ,L)≃Z_i(L*)≃k^(μ_i+1+β_i+1+ν_i)'),('text','last words','en particulier')],doubts=[('top d index','L!_•,i','small subscript partly overlaps inverse exponent','medium'),('upper chain labels','u; u_i−1; nξ_i−1','first u may carry i; element annotations difficult','medium'),('middle cancelled formula','Φ_j(m); j≠i,i+1','heavy strike over zero and condition','low'),('endomorphism note','isom.; d’anneaux; k-algèbres','interlinear changes and deletion scope uncertain','low'),('endomorphism index condition','i≥0','ink resembles 0 despite earlier lower bound 1; retained','medium'),('identity subscript in special case','Φ(i,1)','final glyph looks 1 but could retain earlier n','medium'),('λ notation','T_wedge','T with wedge/subscript mark, not fully clear','low'),('bottom cycles formula','Z_i(L_*)','no clear ! after L in this occurrence; literal star retained','medium')],notation=[('scalar n prime',r"$n'=n/(n,m)$",'scan 21; genuine prime, not exclamation'),('connecting morphism',r'$\lambda=\unsure{T_\wedge}$','scan 21; exact operator subscript uncertain'),('Hom qualifications',r'$\operatorname{Hom}_k$','scan 21; k subscript sometimes omitted in handwritten display, retained occurrence by occurrence')])
