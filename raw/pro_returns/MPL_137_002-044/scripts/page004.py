from record_page import record
tex=r'''\scanpage{4}
% archive foliation: 3
\uline{Lemme 2} Soit $L_\bullet$ un $k$-module \unsure{simplicial},
\inserted{\unsure{projectif}} \deleted{flasque}, \unsure{$q>0$}, $M$ un $k$-module, \unsure{alors}
\[
\unsure{\operatorname{Hom}_{\widehat\Delta_k}}
\bigl(L_\bullet\otimes_k\unsure{\Lambda^q\Psi_{\bullet k}},
\unsure{\Lambda^{q'}\Psi_{\bullet k}}\otimes_k M\bigr)=0
\]
\inserted{(\unsure{ou Eilenberg} \illegible{1})}
(\unsure{pour} \illegible{2} \unsure{en degrés} $<q$).

\deleted{\unsure{Soit} \illegible{7}}
\inserted{le complexe de chaînes associé à}
\deleted{\illegible{4}}
$L_\bullet\otimes_k\unsure{\Lambda^q\Psi_{\bullet k}}$ \unsure{est}
\deleted{\illegible{3}}
\deleted{\unsure{un} \illegible{5}} \unsure{de la forme}
\[
\cdots\longrightarrow L'_{q+1}\longrightarrow L'_q\longrightarrow0\longrightarrow\cdots
\]
tandis que $\unsure{\Lambda^{q'}\Psi_{\bullet k}}\otimes_k M$ est $M$ placé au \unsure{degré}
$q'$ \inserted{\unsure{i.e. $M[q']$}}. \unsure{Si} $q'=q$, il \unsure{s'agit} de \illegible{1}
$\unsure{\operatorname{Hom}}(L'_\bullet,M\unsure{[q]})$
$=0$ \unsure{pour un morphisme de} \illegible{2} \unsure{de la forme}
\diagram{\begin{tikzcd}
\unsure{L'_{q+1}}\arrow[r,"\unsure{d}"]\arrow[d]&\unsure{L'_q}\arrow[r]\arrow[d]&0\\
0\arrow[r]&M\arrow[r]&0
\end{tikzcd}}
alors $\unsure{\pi_q}(L_\bullet)=0$ $\Rightarrow$ $L'_{q+1}\xrightarrow{d}L'_q$ est surjectif,
donc $L'_q\to M$ est nul, \unsure{donc le hom. de}
\unsure{complexes} \inserted{de chaînes} $\unsure{L'_\bullet\to M[q]}$, cqfd.

\uline{Théorème} Soit $n\geq0$. Il existe un \unsure{homomorphisme}
de complexes de \unsure{modules dans} $\unsure{\widehat\Delta_k}$
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&\unsure{\Gamma^n\Phi_\bullet}\arrow[r]\arrow[d,"u_0"]
&\unsure{\Gamma^{n-1}\Phi_\bullet\otimes\Psi_\bullet}\arrow[r]\arrow[d,"u_1"]
&\unsure{\Gamma^{n-2}\Phi_\bullet\otimes\Lambda^2\Psi_\bullet}\arrow[r]\arrow[d,"u_2"]
&\cdots\arrow[r]&\unsure{\Lambda^n\Psi_\bullet}\arrow[r]\arrow[d,"u_n"]&0\arrow[d]\\
0\arrow[r]&\unsure{\Phi_\bullet}\arrow[r,"\unsure{\wedge T}"']
&\unsure{\Lambda^2\Omega_\bullet}\arrow[r,"\unsure{\wedge T}"']
&\unsure{\Lambda^3\Omega_\bullet}\arrow[r]&\cdots\arrow[r,"\unsure{\wedge T}"']
&\unsure{\Lambda^{n+1}\Omega_\bullet}\arrow[r,"\unsure{\wedge T}"']&\unsure{\Lambda^{n+2}\Omega_\bullet}
\end{tikzcd}}
(\unsure{nb}: on écrit $\unsure{\Phi_\bullet}$ et $\unsure{\Psi_\bullet}$ pour
$\unsure{\Phi_{\bullet k}}$, $\unsure{\Psi_{\bullet k}}$, et $\unsure{\Omega}$
\unsure{l'algèbre} $\unsure{\Omega_k}$) tel que \unsure{$u_n$ soit l'isom. de}
$\unsure{\Lambda^n\Psi_\bullet}$ sur
$\unsure{\operatorname{Ker}(\Lambda^{n+1}\Omega_\bullet\to\Lambda^{n+2}\Omega_\bullet)
=d\,Z(\Lambda^n\Omega_\bullet)}$
'''
record(4,tex,[('text','top heading and statement','Lemme 2 Soit L'),('insertion','above flasque','projectif'),('deletion','top line 2','flasque'),('display','top Hom formula','Hom(L ⊗ Λ^q Ψ, Λ^{q′} Ψ ⊗ M)=0'),('insertion','brace under left object','ou Eilenberg'),('text','below formula condition','pour; en degrés <q'),('deletion','line under Hom','Soit'),('insertion','between ruled deletions','le complexe de chaînes associé à'),('deletion','next line left','unreadable four words'),('display','same line surviving object','L ⊗ Λ^q Ψ'),('deletion','same line right','unreadable three words'),('deletion','next line','un'),('text','above truncated complex','de la forme'),('display','upper-middle','… → L′_{q+1} → L′_q → 0 → …'),('text','middle','tandis que'),('insertion','above q′','i.e. M[q′]'),('diagram','centre fold','L′_{q+1}, L′_q, M, 0'),('text','below diagram','alors π_q(L)=0'),('insertion','above complexes','de chaînes'),('text','lower theorem heading','Théorème Soit n≥0'),('diagram','lower two rows','Γ^n Φ; Λ^n Ψ; Λ^{n+1} Ω'),('text','bottom parenthesis','nb: on écrit'),('display','bottom inline','Ker(Λ^{n+1} Ω → Λ^{n+2} Ω)')],doubts=[('lemma opening','projectif; q>0; simplicial','letters and inequality faded','low'),('Hom display','Hom_{Δ̂_k}; Λ^q Ψ; Λ^{q′} Ψ','subscript category and exponents uncertain','low'),('brace / following condition','ou Eilenberg; en degrés <q','other words unreadable; could be a different phrase','low'),('deleted passage','Soit; un; associated chain-complex wording','most struck words additionally faded','low'),('middle proof','q′=q; Hom(L′,M[q]); π_q(L)=0','indices and some connective words uncertain','low'),('theorem introduction','homomorphisme; modules dans Δ̂_k','word endings faded','low'),('two-row diagram','Φ, Ψ, Ω; Γ exponents; ∧T; u_i','faint alphabets, indices and arrow labels; all marked locally','low'),('bottom','l’algèbre; u_n soit l’isom.; Ker; d Z','partly clipped final line and severe fading','low')],notation=[('prime on chain-complex letters',r"$L'_q$",'scan 4: small raised stroke appears prime, not !; marked where uncertain'),('new recurring capitals',r'$\Phi$, $\Psi$, $\Omega$','scan 4: extremely faded; local uncertainty retained rather than forced identification')])
