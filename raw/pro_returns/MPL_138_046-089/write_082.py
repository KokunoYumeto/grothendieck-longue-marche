from workflow import save_page
save_page(82,r'''\scanpage{82}
% archive foliation: 81
des $\Phi_i\in\operatorname{Homext}(T,\pi)$ canoniques,
$i\in I$. Le système
\deleted{$\unsure{\Sigma(X/I/k)}$}\inserted{$\Sigma(X/I/x/k)$}$=(T,I,\pi,(\Phi_i))$
satisfait aux conditions \unsure{envisag.} \deleted{Pour}
\inserted{Au lieu de} \deleted{\unsure{Changeons}} \deleted{\unsure{le}} prendre $x$, il suffit
de prendre un $\unsure{\xi|\zeta}$, foncteur fibre sur
la catégorie des rev. étales de $X\setminus I$
($\pi$ étant le groupe des autom. de $\xi\ldots$)
Alors $\Sigma$ dépend fonctoriellement de
$(X/I/\xi/k)$. Prenant $X,I,k$ fixes,
$\xi$ variable, on voit que $\Sigma$ est déterminé
``mod autom. intérieurs'' i.e. \deleted{\unsure{on est}}
définit un torseur \deleted{sous}\inserted{à droite} \unsure{non pas}
sous $\widetilde A_\nu$ mais sous son quotient
$\widetilde A_\nu/\pi_\nu=)\ \widetilde\Gamma_\nu$,
\inserted{soit $P(X/I/k)$}, \deleted{le dernier torseur}
dont le commutant est le groupe
des ``autom. ext.'' de \deleted{$\unsure{T,I,}$}
$\Sigma(X/I/\unsure{x|m}/k)\ldots$

Supposons que $X/I/\unsure{x}$ provienne
par extension de la base \deleted{$\unsure{\operatorname{Spec}k\longrightarrow S_0}$}\inserted{$k_0\subset k$}
\deleted{d'une situation}
''',[
('text','upper','des Φ_i∈Homext(T,π) canoniques'),
('deletion','upper tuple name','Σ(X/I/k)'),
('insertion','above tuple name','Σ(X/I/x/k)'),
('deletion','upper-right','Pour'),
('insertion','upper-middle','Au lieu de'),
('deletion','upper-middle','Changeons; le'),
('text','middle','prendre x, il suffit de prendre un ξ'),
('text','middle','Alors Σ dépend fonctoriellement'),
('deletion','below fold right','on est'),
('deletion','lower-middle','sous'),
('insertion','above sous','à droite'),
('text','lower-middle','définit un torseur non pas sous Atilde_ν'),
('insertion','lower-middle','soit P(X/I/k)'),
('deletion','lower-middle','le dernier torseur'),
('deletion','lower','T,I,'),
('text','lower','dont le commutant est le groupe'),
('text','bottom','Supposons que X/I/x provienne'),
('deletion','bottom-right','Spec k → S₀'),
('insertion','bottom-right above deletion','k₀⊂k'),
('deletion','bottom','d’une situation')])
