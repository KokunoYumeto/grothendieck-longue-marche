from record_page import record
tex=r'''\scanpage{24}
% archive foliation: 23
est nul; or
\[
q^*(e_{i,m})=\unsure{m|qm}e_i,\qquad
p_*(e_{i,\unsure{m|n}})=\unsure{n|pn}e_i
\]
où $e_i$ définit l'extension $\Phi^i$.
Donc la condition est que
\[
(qm-pn)e_i=0
\]
On fait l'hypothèse
\[
\text{(c)}\qquad
\boxed{e_i\text{ est une base de }\operatorname{Ext}^1_{C_0}(\Psi^i,\Psi^{i-1})}
\]
de sorte que la condition devient
\[
qm=pn
\]
i.e.\quad
\[
\frac q p=\frac{\unsure{m|n}}{\unsure{n|m}}
=\frac{\unsure{m'|n'}}{\unsure{n'|m'}}
\]
si $m'=\dfrac{m}{(m,n)}$, $n'=\dfrac{n}{(m,n)}$, donc
on aura
\[
p=\deleted{\unsure{pq}}\,t m',\quad q=t n'\qquad(t\in k).
\]
Or pour $p,q$ correspondant ainsi
à un $t$ (évidemment uniquement
déterminé par $(p,q)$) l'hom
$\alpha$ qui leur correspond est déterminé
mod un $\operatorname{Hom}(\Psi^i,\Psi^{i-1})=0$,
donc est unique. On trouve donc
\[
\operatorname{Hom}(\Phi(i,n),\Phi(i,m))\simeq k.
\]
'''
record(24,tex,[('text','top','est nul; or'),('display','top','q*(e_i,m), p*(e_i,n)'),('text','upper','e_i définit extension; condition'),('display','upper','(qm−pn)e_i=0'),('text','upper-middle','On fait l’hypothèse'),('display','boxed c','e_i base Ext^1_C0(Ψ^i,Ψ^(i−1))'),('text','middle','de sorte que la condition devient'),('display','middle','qm=pn'),('text','middle','i.e.'),('display','middle','q/p=m/n=m′/n′'),('text','lower-middle','si m′=m/(m,n), n′=n/(m,n), donc on aura'),('display','lower-middle','p=tm′, q=tn′ (t∈k)'),('deletion','after p=','pq'),('text','bottom argument','Or pour p,q correspondant ainsi; unicité α'),('display','bottom','Hom(Φ(i,n),Φ(i,m))≃k')],doubts=[('top pullback formula','q*(e_i,m)=m e_i','coefficient may include q; faint fused strokes','low'),('top pushout formula','p*(e_i,m)=n e_i','subscript n; coefficient pn; faint overtraced strokes','low'),('ratio after i.e.','m/n=m′/n′','n/m=n′/m′; m and n difficult to distinguish; no algebraic emendation made','low'),('after p=','deleted pq','heavily obliterated short expression','low'),('hypothesis c','Ext^1_C0','category subscript reads C_0; superscript 1 close to t','medium')])
