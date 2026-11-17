from record_page import record
tex=r'''\scanpage{11}
% archive foliation: 10
\[
\rho(n)\overset{\mathrm{df}}=\operatorname{rg}_kL_n
=\sum_{1\leq i\leq n+1}\mu_i\binom{n+1}{i}
+\sum_{0\leq j\leq n}\nu_j\binom{n}{j}
\]
\diagram{\begin{tikzcd}[column sep=huge]
\binom{n+1}{i}\arrow[d] & \binom{n}{j}\arrow[d]\\
\text{pol. de degré $i$ en $n$} & \text{pol. de degré $j$ en $n$}
\end{tikzcd}}
où $\mu_i=\operatorname{rg}_kM_i$, $\nu_j=\operatorname{rg}_kN_j$.

donc si \deleted{\unsure{$\mu_i\ (\nu_j)$}} un $\mu_i$ ou un $\nu_j$
est $\neq0$, cela montre que $\rho(n)$ pour
$n$ grand est minoré par un polynôme
de degré $i$ resp $j$.

[2°) Cas de $\Lambda^k$. Utilisant la formule
du $\Lambda^k$ d'une somme directe et
1°), on est ramené à prouver que
le $\Lambda^k$ d'un module $\frac12$ simplicial
$L_\bullet$ de la forme $\Lambda^i\Phi_\bullet\otimes M$, $\Lambda^j\Psi_\bullet\otimes N$.

Comme $M$, $N$ sont facteurs directs d'un
libre $P$, \inserted{$L_\bullet$ est facteur direct de
$L'_\bullet=\Lambda^i\Phi_\bullet\otimes P$ \unsure{ou} $\Lambda^j\Psi_\bullet\otimes P$,}
\deleted{\unsure{et}} \deleted{\unsure{cela montre}}
\inserted{\unsure{la propriété du cor. 1 et du cor 2}
\deleted{\unsure{prop}} est stable par fact. direct}
\deleted{\unsure{la propriété de déf.}}
et en utilisant la
formule du $\Lambda^k$ d'une somme directe,
\unsure{montre} que $\Lambda^k(L_\bullet)$ est facteur
direct de $\Lambda^kL'_\bullet$. On est ramené à
prouver $\Lambda^kL'_\bullet$ est \deleted{\unsure{str.}} spécial, donc
\unsure{supp.} $M$, $N$ libres --- donc $=$ (par la
formule de la somme) $M=k$, $N=k$.
Donc on est ramené à prouver
'''
record(11,tex,[('display','top','ρ(n)=rg_k L_n=Σ μ_i binomial+Σ ν_j binomial'),('diagram','below binomial factors','downward arrows; pol. de degré i en n; j en n'),('text','upper middle','où μ_i=rg_k M_i, ν_j=rg_k N_j'),('deletion','after donc si','μ_i (ν_j)'),('text','upper middle paragraph','un μ_i ou un ν_j est ≠0'),('text','middle bracket','2°) Cas de Λ^k'),('text','middle continuation','le Λ^k d’un module ½ simplicial'),('text','lower proof opening','Comme M,N sont facteurs directs'),('insertion','above lower lines','L est facteur direct de L′=Λ^iΦ⊗P ou Λ^jΨ⊗P'),('deletion','after libre P','et; cela montre'),('insertion','between lower lines, curved connector','la propriété du cor.1 et du cor2 est stable par fact. direct'),('deletion','inside insertion','prop'),('deletion','under inserted line','la propriété de déf.'),('text','lower continuation','et en utilisant la formule du Λ^k'),('text','lower continuation after curved arrow','On est ramené à prouver'),('deletion','before spécial','str.'),('text','bottom','M,N libres; M=k,N=k; Donc on est ramené à prouver')],doubts=[('first deleted phrase','μ_i (ν_j)','two coefficients crossed out; grouping faint','low'),('second section','M,N; Φ_•,Ψ_•','possible subscripts by M,N in the first formula','medium'),('dense insertion above lower block','L′=Λ^iΦ⊗P ou Λ^jΨ⊗P','connector and word between alternatives faint','low'),('dense insertion between lines','la propriété du cor. 1 et du cor 2','several overwritten words; possibility prop. 1','low'),('deleted words','et; cela montre; prop; la propriété de déf.','crossed strokes obstruct original lettering','low'),('lower prose','montre; supp.; donc =','compressed strokes; grammar not used to repair','low'),('bracket opening','[2°)','opening bracket visible; no closing bracket on this scan','high')],notation=[('rank polynomial coefficients',r'$\rho(n),\mu_i,\nu_j$','scan 11'),('prime on newly introduced retract',r"$L'_\bullet$",'scan 11; prime of a second object, to distinguish from associated-complex exclamation mark')])
