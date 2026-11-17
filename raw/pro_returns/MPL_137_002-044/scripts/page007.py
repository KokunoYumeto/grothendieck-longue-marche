from record_page import record
tex=r'''\scanpage{7}
% archive foliation: 6
\uline{Lemme} Supposons les $L_n$ et $\pi_n(L_\bullet)$
projectifs de \unsure{r.f.|t.f.} sur $k$, et supposons $k$
commutatif à \uline{spec connexe} (donc
$\forall M$ projectif sur $k$, $\operatorname{rg}_k M\in\mathbf N$ est défini).
\margin{\unsure{on peut aussi} \illegible{1} \unsure{au sens} \illegible{1} \unsure{projectifs}}

Conditions équivalentes

a) $L'_\bullet$ à degrés bornés

b) \deleted{\unsure{$L_\bullet$}} Des $M_i$, $N_j$ \unsure{n.} nuls sauf
un nb fini t.q. $L_\bullet\simeq$ somme \uline{finie}
de modules $k$-simpliciaux $\Lambda^i\Phi_\bullet\otimes M_i$ $(i\geq1)$,
$\Lambda^j\Psi_\bullet\otimes N_j$ $(j\geq1)$ ($M_i$ et $N_j$ proj. de \unsure{r.f.|t.f.})

b') (Si $k$ principal, plus génér. si tout
module proj de \unsure{r.f.|t.f.} sur $k$ est libre).
$L_\bullet\simeq$ somme \uline{finie} de modules $k$-
simpliciaux $\Lambda^i\Phi_\bullet$ \inserted{$(i\geq1)$}, $\Lambda^j\Psi_\bullet$ $(j\geq0)$

c) $\operatorname{rang}_k L_n$ est une fonction
polynomiale en $n$ pour $n$ grand

d) $\exists N$ \inserted{et $c>0$} tel que pour $n$ assez
grand, on ait
\[
\operatorname{rang}_k L_n\leq c n^N
\]

[\deleted{\unsure{Cor.}} De plus, \deleted{\unsure{p}} pour $N$ fixé, la condition
que l'on ait $\operatorname{rang}_k L_n=O(n^N)$
signifie que $M_i$, $N_j$ sont nuls pour $i,j>N$;
\deleted{\unsure{et si $N$ est le plus petit possible} (\unsure{donc} $M_N+N_N\neq0$)}
\unsure{cf. b) ci-dessus} \deleted{\illegible{6}}
(\unsure{voir 1 et 2})]
\margin{\unsure{et si} \illegible{2}
$\displaystyle\unsure{\lim_{n\to\infty}\frac{\operatorname{rg}_k L_n}{n^N}
=\mu_N+\nu_N}$}

\uline{Dém.} \deleted{Équivalence des \unsure{conditions}}
\unsure{ci-dessus}), $\mathrm b)\Longleftrightarrow\mathrm b')$ trivial,
\deleted{\unsure{a)\ensuremath{\Rightarrow}}}
$\mathrm c)\Rightarrow\mathrm d)$ triv., $\mathrm a)\Rightarrow\mathrm c)$ et $\mathrm d)\Rightarrow\mathrm a)$
immédiat par les formules explicites
'''
record(7,tex,[('text','top lemma','Lemme Supposons les L_n'),('margin note','left upper slant','on peut aussi'),('text','upper','Conditions équivalentes'),('text','condition a','L′ à degrés bornés'),('text','condition b','Des M_i, N_j'),('deletion','condition b beginning','L'),('display','condition b inline pair','Λ^i Φ ⊗ M_i; Λ^j Ψ ⊗ N_j'),('text','condition b′','Si k principal'),('insertion','after Λ^i Φ','i≥1'),('text','condition c','rang_k L_n est une fonction'),('text','condition d','∃N tel que'),('insertion','above tel que','et c>0'),('display','middle-lower','rang_k L_n≤cn^N'),('text','bracketed paragraph','De plus, pour N fixé'),('deletion','above De plus','Cor.'),('deletion','after De plus','p'),('display','inline growth bound','rang_k L_n=O(n^N)'),('deletion','lower paragraph crossed line','et si N est le plus petit possible'),('deletion','lower right crossed words','six unreadable words'),('margin note','lower left oval','lim rg_k L_n/n^N=μ_N+ν_N'),('text','bottom proof','Dém. ci-dessus; b ⇔ b′'),('deletion','after Dém.','Équivalence des conditions'),('deletion','before c ⇒ d','a)⇒'),('text','last line','immédiat par les formules explicites')],doubts=[('opening / repetitions','r.f.','t.f.; first letter small and ambiguous','medium'),('left margin','on peut aussi; au sens; projectifs','intervening words unclear','low'),('b)','Des; n.; i≥1; j≥1','n. may be an abbreviation for non; inequalities require review','medium'),('b′)','Λ^j Ψ (j≥0)','last inequality appears ≥0, retained despite b)','medium'),('bracketed deletion','et si N est le plus petit possible','overstruck words and right-hand continuation','low'),('lower margin','lim rg_k L_n/n^N=μ_N+ν_N','rank subscript, Greek letters, possibly a coefficient obscured','low'),('proof transition','ci-dessus); voir 1 et 2; deleted a)⇒','scope of interlinear continuation unclear','low')],notation=[('rank abbreviations',r'$\operatorname{rg}_k$, $\operatorname{rang}_k$','scan 7 uses both spellings; do not unify lexical forms'),('finite rank/type abbreviation',r'\unsure{r.f.|t.f.}','scan 7: retain ambiguity instead of expanding'),('isomorphism mark above curved arrow',r'$\simeq$','scan 7; compare each later occurrence')])
