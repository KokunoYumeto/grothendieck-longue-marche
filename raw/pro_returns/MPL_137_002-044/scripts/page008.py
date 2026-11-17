from record_page import record
tex=r'''\scanpage{8}
% archive foliation: 7
\uline{Prop} Soit $L_\bullet$ un $k$-module $\frac12$ simplicial.
Les conditions suivantes sont équivalentes

a) les $L_n$ et $\pi_n(L_\bullet)$ sont des $k$-modules
projectifs.

a') Les composantes \deleted{\unsure{de}} $(L^!_\bullet)_n$ de $L^!_\bullet$ (le
complexe de chaînes de Dold-Puppe associé à
$L_\bullet$) et les $H_n(L^!_\bullet)$ sont des $k$-modules
projectifs

b) $L_*$ est isomorphe à un \deleted{\unsure{somme}} \inserted{produit}
direct \deleted{de modules} de la forme
\[
\left(\prod_{i\geq1}\Lambda^i\Phi_{*k}\otimes_k M_i\right)
\times\prod_{j\geq0}(\Lambda^j\Psi_{*k})\otimes_k N_j
\]
\unsure{et} b') $L^!$ est isomorphe à un produit
direct (de complexes de cochaînes) de
la forme
\diagram{\displaystyle
\prod_{i\geq1}\left(
\begin{tikzcd}[column sep=small]
0\arrow[r]&\underset{\text{en degré }i}{M_i}\arrow[r]&\underset{\text{et }i-1}{M_i}\arrow[r]&0\arrow[r]&\cdots
\end{tikzcd}\right)
\times\prod_{j\geq0}\left(
\begin{tikzcd}[column sep=small]
0\arrow[r]&\underset{\text{en degré }j}{N_j}\arrow[r]&0\arrow[r]&\cdots
\end{tikzcd}\right)}

De plus, les $M_i$ et $N_j$ de b) (resp. b'))
sont déterminés à isom près par \deleted{\unsure{$K$}} $L_\bullet$,
et ce sont les mêmes (à isom près) dans
b) et b').

\uline{Dém} $\mathrm{a'})\Longleftrightarrow\mathrm{b'})$ est trivial et bien connu,
ainsi que l'unicité à isom \inserted{can.} près des
$M_i$, $N_j$ dans b') (\uline{NB} on a $N_j\simeq H_j(L_\bullet)$
et $M_i\simeq L_i^!/Z_i\ (\simeq B_{i-1})$\unsure{*}.
Or $\mathrm a)\Longleftrightarrow\mathrm{a'})$
\inserted{et $\mathrm b)\Longleftrightarrow\mathrm{b'})$}
par la théorie de Dold-Puppe. D'où
l'équivalence des 4 conditions, et la dernière
assertion est \unsure{contenue|connue}.
'''
record(8,tex,[('text','top proposition','Prop Soit L un k-module ½ simplicial'),('text','condition a','les L_n et π_n(L)'),('text','condition a′','Les composantes'),('deletion','condition a′','de'),('text','condition b','L_* est isomorphe'),('deletion','condition b','somme'),('insertion','above deleted somme','produit'),('deletion','condition b next line','de modules'),('display','middle','product Λ^i Φ_*k ⊗ M_i; product Λ^j Ψ_*k ⊗ N_j'),('text','condition b′','L! est isomorphe'),('diagram','middle-lower products','0 → M_i → M_i → 0; 0 → N_j → 0'),('text','lower paragraph','De plus, les M_i et N_j'),('deletion','after par','K'),('text','lower proof','Dém a′ ⇔ b′'),('insertion','above près','can.'),('display','proof inline','N_j≃H_j(L); M_i≃L_i!/Z_i (≃B_{i-1})'),('insertion','left above par la théorie','et b)⇔b′)'),('text','last paragraph','par la théorie de Dold-Puppe')],doubts=[('b first word deletion','somme','letters heavily crossed','medium'),('b′ introduction','cochaînes','appears cochaînes, although preceding paragraph says chaînes','medium'),('products degrees','i and i−1; j','superscript on first M_i overlaps degree annotation','medium'),('before b′','et','stray handwritten character','low'),('De plus paragraph deletion','K','crossed symbol before L','low'),('end of NB','*','small crossed mark after closing parenthesis','low'),('last word','contenue','connue','low')],notation=[('exclamation exponent on associated complex',r'$L^!_\bullet$, $L_i^!$','scan 8 clearly includes lower dot of !; earlier prime readings require ink audit'),('asterisk subscript in displayed elementary modules',r'$\Phi_{*k}$, $\Psi_{*k}$','scan 8: star visible; do not silently replace by bullet'),('half-simplicial wording',r'$\frac12$ simplicial','scan 8 written ½; preserve without expansion')])
