from record_page import record
tex=r'''\scanpage{22}
% archive foliation: 21
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,\Lambda^j\Psi_*)\simeq
\left\{\begin{array}{ll}0&\text{si }j\neq i\\k&\text{si }j=i\end{array}\right.
\]
de façon précise
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,\Lambda^i\Psi_*)
\simeq k\operatorname{id}_{\Lambda^i\Psi_*}\simeq k,
\]
et
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,\Phi_{\deleted{j}}(j,n))\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq\deleted{i,}\ i+1\\
k&\text{si }j=i+1
\end{array}\right.
\]
en particulier
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,\Lambda^j\Phi_*)\simeq
\left\{\begin{array}{ll}0&\text{si }j\neq i+1\\k&\text{si }j=i+1\end{array}\right.
\]
et
\[
\operatorname{Hom}_k(\Lambda^i\Psi_*,\Lambda^{i+1}\Phi_*)
=k\cdot\iota\simeq k
\]
où $\iota:\Lambda^i\Psi_*\hookrightarrow\Lambda^{i+1}\Phi_*$ est l'inclusion
canonique.

\uline{NB} On a un \inserted{hom de} suites exactes can
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r,dash]&\Lambda^{i-1}\Psi_*\arrow[r,dash]\arrow[d,"n\operatorname{id}"']&
\Lambda^{i\deleted{\unsure{+1}}}\Phi_*\arrow[r]\arrow[d,equal]&
\Lambda^i\Psi_*\arrow[r,dash]\arrow[d,"\operatorname{id}"]&0\\
0\arrow[r,dash]&\Lambda^{i-1}\Psi_*\arrow[r]&
\deleted{\unsure{\Lambda^i}}\Phi_*(i,n)\arrow[r,dash]&\Lambda^i\Psi_*\arrow[r,dash]&0
\end{tikzcd}}
qui montre que $\Phi_*(i,n)$ est l'ext.
déduite de \inserted{l'ext} $\Lambda^i\Phi_*$ de $\Lambda^i\Psi_*$ par $\Lambda^{i-1}\Psi_*$
par l'hom $n\operatorname{id}:\Lambda^{i-1}\Psi_*\longrightarrow\Lambda^{i-1}\Psi_*$.
'''
record(22,tex,[('display','top','Hom(Λ^iΨ,Λ^jΨ) cases'),('text','upper lead','de façon précise'),('display','upper endomorphism','Hom(Λ^iΨ,Λ^iΨ)=k id≃k'),('text','before mixed case','et'),('display','middle','Hom(Λ^iΨ,Φ(j,n)) cases'),('deletion','inside Φ subscript','j'),('deletion','first case after ≠','i,'),('text','middle','en particulier'),('display','middle special case','Hom(Λ^iΨ,Λ^jΦ) cases'),('display','lower-middle generator','Hom(Λ^iΨ,Λ^(i+1)Φ)=kι≃k'),('text','generator explanation','ι inclusion canonique'),('text','NB','On a un suites exactes can'),('insertion','above un suites','hom de'),('diagram','lower exact sequences','Λ^(i−1)Ψ, Λ^iΦ, Λ^iΨ over Φ(i,n); n id, =, id'),('deletion','diagram top superscript','+1'),('deletion','diagram bottom before Φ(i,n)','Λ^i'),('text','bottom','Φ(i,n) ext déduite; n id'),('insertion','bottom before Λ^iΦ','l’ext')],doubts=[('first mixed Hom','Φ with deleted j subscript','small correction at lower edge of Φ','medium'),('diagram top exponent','deleted +1','arrow-shaped overwritten superscript may have another original digit','low'),('diagram central vertical mark','equal sign','two parallel vertical strokes visible; kept despite categorical expectation','medium'),('diagram bottom deleted prefix','Λ^i','heavily overwritten, could be just Λ','low'),('bottom wording','l’ext.; l’ext inserted','short abbreviation and insertion attachment faint','medium')],notation=[('canonical inclusion generator',r'$\iota$','scan 22; dot over short vertical-curved letter, distinguished from integer i'),('handwritten diagram dashes',r'\arrow[r,dash]','scan 22; arrowheads not supplied when ink shows only line')])
