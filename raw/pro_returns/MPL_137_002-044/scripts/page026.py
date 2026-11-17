from record_page import record
tex=r'''\scanpage{26}
% archive foliation: 25
\diagram{\begin{tikzcd}[column sep=large,row sep=huge]
\operatorname{Hom}(\Phi(i,n),\Psi^j)\arrow[r,phantom,"\subset"]\arrow[d]&
\operatorname{Hom}(\Phi(i,n),\Phi^{j+1})\\
\operatorname{Hom}(\Psi^{i-1},\Psi^j)=0\text{ si }j\neq i-1&
\end{tikzcd}}
\inserted{$\Phi(j+1,m)$}
\[
=0\quad\text{si }j+1\neq i,i+1\quad\text{i.e. si }j\neq i-1,i.
\]
Si donc $j=i$,\quad
\diagram{\begin{tikzcd}[column sep=large]
\operatorname{Hom}(\Phi(i,n),\Psi^{\deleted{j}i})&
\operatorname{Hom}(\Psi^i,\Psi^i)\arrow[l]\arrow[d,phantom,"\simeq" description]\\
&k
\end{tikzcd}}
(par l'hom can.)

\deleted{Si}
Si $j=i-1$,
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
0\arrow[r,dash]&\Psi^{i-1}\arrow[r]\arrow[d,"n\operatorname{id}"']&\Phi^i\arrow[r]\arrow[d]&\Psi^i\arrow[r]\arrow[d,equal]&0\\
0\arrow[r,dash]&\Psi^{i-1}\arrow[r,dash,"\iota"]&\Phi(i,n)\arrow[r]\arrow[d,"\alpha=?"]&\Psi^i\arrow[r,dash]&0\\
&&\Psi^{i-1}
\end{tikzcd}}
la composée de $\alpha\deleted{\unsure{\iota}}$ avec
\deleted{$n\operatorname{id}_{\Psi^i}$}
\inserted{$\Phi^i\longrightarrow\Phi(i,n)$}
est $\in\operatorname{Hom}(\Phi^i,\Psi^{i-1})=0$, donc
\deleted{sa composée $n\alpha\iota\in\operatorname{Hom}$}
$\alpha\iota\circ n\operatorname{id}_{\Psi^{i-1}}=n(\alpha\iota)$
$\in\operatorname{Hom}(\Psi^{i-1},\Psi^{i-1})$ est nul, et
comme $\operatorname{Hom}(\Psi^{i-1},\Psi^{i-1})\simeq k$,
on voit que $\alpha\iota=0$, donc
$\alpha$ \deleted{\unsure{puis}} se factorise par
$\Psi^i\longrightarrow\Psi^{i-1}$, donc est nul. Donc
\[
\operatorname{Hom}(\Phi(i,n),\Psi^j)=
\left\{\begin{array}{ll}
0&\text{si }j\neq i\\
\simeq k&\text{(par l'hom can. }\Phi(i,n)\longrightarrow\Psi^i\text{) si }j=i
\end{array}\right.
\]
'''
record(26,tex,[('diagram','top','Hom(Φ(i,n),Ψ^j)⊂Hom(Φ(i,n),Φ^(j+1)); restriction to Ψ^(i−1)'),('insertion','under upper right Φ','Φ(j+1,m)'),('display','upper side condition','=0 si j+1≠i,i+1; j≠i−1,i'),('text','upper-middle','Si donc j=i'),('diagram','upper-middle','Hom(Φ(i,n),Ψ^i)←Hom(Ψ^i,Ψ^i)≃k'),('deletion','superscript Ψ','j replaced by i'),('text','under isomorphism','par l’hom can.'),('deletion','left middle','Si'),('text','middle','Si j=i−1'),('diagram','middle','extension Φ^i over Φ(i,n), n id, ι, α=? to Ψ^(i−1)'),('text','lower-middle','la composée de α avec'),('deletion','after α','ι'),('deletion','old map','n id_Ψi'),('insertion','replacement map','Φ^i→Φ(i,n)'),('text','lower-middle','est ∈ Hom=0 donc'),('deletion','lower-middle old equation','sa composée nαι∈Hom'),('display','lower-middle','αι∘n id=n(αι)'),('text','lower argument','∈Hom est nul; comme Hom≃k; αι=0'),('deletion','after α','puis'),('text','lower argument','se factorise par Ψ^i→Ψ^(i−1), donc est nul'),('display','bottom','Hom(Φ(i,n),Ψ^j) cases 0 / ≃k')],doubts=[('insertion at upper right','Φ(j+1,m)','connected by short vertical guide; might replace Φ^(j+1) rather than add an alternative','medium'),('upper-middle Hom','Ψ^i with deleted j','overwritten index is small and crowded','medium'),('diagram n id','n id','subscripted source index faint','medium'),('deleted map beside composition','n id_Ψi','subscript may be Ψ^(i−1)','low'),('cancelled equation','sa composée nαι∈Hom','formula crossed through; best partial reconstruction marked by deletion','low'),('last deleted word','puis','puisse or another short verb; cancellation masks endpoint','low')])
