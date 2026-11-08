# LM_P04 — Diplomatic transcription and notes

## 1. Transcription

```latex
\scanpage{31}

La condition \unsure{c)|e)} permet déjà de définir le
\unsure{$\pi_1$|$\Pi_1$} relatif
\[
\unsure{\pi_1|\Pi_1}(\sigma)
 = \unsure{\pi_1|\Pi_1}(\Pi_{D^*}/\Pi_D),
\]
qui est un syst. local de gr. profinis sur $\Pi_D$
\inserted{\unsure{i.e.} un foncteur
\uline{$(\Pi_D)^{\mathrm{o}}\to\mathrm{Ens}$}}
et la dernière donnée :

$4^\circ)$ Un isom. \unsure{kummérien}
\[
\deleted{\illegible{1}}\,k:\quad
\unsure{\pi_1|\Pi_1}(\sigma)\simeq
\psi^*(\unsure{\tau|\mathcal T})
\]

Si on a deux systèmes de cette nature
\[
\Pi=(\Pi_U,\Pi_D,\Pi_{D^*},\varphi,\psi,\rho,\sigma,\alpha,k)
\]
et $\Pi'=(\Pi'_U,\Pi'_D,\ldots)$, un \uline{morphisme}
de $\Pi'$ dans $\Pi$ est un système de $3$ foncteurs
\[
\begin{gathered}
f_U:\Pi'_U\to\Pi_U\\
f_D:\Pi'_D\to\Pi_D\\
\deleted{\illegible{1}}f_{D^*}:\Pi'_{D^*}\to\Pi_{D^*}
\end{gathered}
\]
et de \inserted{quatre}\deleted{\illegible{1}}
isomorphismes de commutation
$\alpha_{D^*D},\alpha_{D^*U},\alpha_{Ue},\alpha_{De}$
pour les quatre faces du prisme
\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
 & \Pi'_{D^*}\arrow[rr,"\sigma'"]\arrow[dd,"\rho'"]
   \arrow[dl,"f_{D^*}"'] &&
   \Pi'_D\arrow[dd,"\psi'"]\arrow[dl,"f_D"']\\
 \Pi_{D^*}\arrow[rr,"\sigma",near start]\arrow[dd,"\rho"'] &&
 \Pi_D\arrow[dd,"\psi",near end]\\
 & \Pi'_U\arrow[rr,"\unsure{\varphi'}"]\arrow[dl,"f_U"'] &&
 \Pi_e\arrow[dl,"="']\\
 \Pi_U\arrow[rr,"\varphi"'] && \Pi_e
\end{tikzcd}
}
\deleted{\illegible{2}}

\scanpage{32}
\mspage{14}

satisfaisant une \inserted{équation} de compatibilité avec $\alpha,\alpha'$ que je n'écris pas
--- \inserted{$u,v$} signifie que les \uline{deux}
\deleted{\illegible{1}} isomorphismes de foncteurs
\diagram{[Deux flèches parallèles de $\Pi'_{D^*}$ vers $\Pi_e$.
La flèche supérieure porte $\varphi\circ\rho\circ f_{D^*}$ ;
la flèche inférieure porte $\unsure{\mathrm{id}}\circ\psi'\circ\sigma'$.
Entre les deux, deux flèches descendantes, notées $u$ et $v$.]}
obtenus implicitement, en utilisant successivement
$\alpha,\alpha_{D^*D},\alpha_{De}$, \deleted{\illegible{1}} ou en
utilisant successivement $\alpha_{D^*U},\alpha_{Ue},\alpha'$, sont égaux.
[Cette compatibilité pourrait s'exprimer en interprétant la donnée
de $\Pi$ \inserted{\unsure{$\Pi$}} comme celle d'une catégorie
fibrée sur la \deleted{\unsure{de diagramme en forme}}
\inserted{``catégorie} carré''
\[
Q:
\]
\diagram{[Losange de sommets $D^*$ en haut, $\unsure{U}$ à gauche,
$D$ à droite, $e$ en bas. Le côté $D^*\to U$ porte $\rho_0$ ;
les trois autres côtés portent $\sigma_0$ entre $D^*$ et $D$,
$\varphi_0$ entre $U$ et $e$, $\psi_0$ entre $D$ et $e$.
Les pointes de ces trois traits ne sont pas nettement discernables.]}
où $\varphi_0\rho_0=\psi_0\sigma_0$.

: restriction à $\{e\}$ imposée, et en prenant des foncteurs
\inserted{cartésiens} (entre catégories fibrées\ldots)].
De plus, on exige une autre compatibilité, savoir que

\scanpage{33}

\deleted{l'hom.} l'hom. de syst. locaux en groupes définis sur $\Pi'_D$
\[
(f_D)^*\bigl(\unsure{\pi_1|\Pi_1}(\sigma)\bigr)
\longleftarrow \unsure{\pi_1|\Pi_1}(\sigma')
\]
défini à l'aide de : $f_{D^*},f_D,\alpha_{D^*D}$
rende commutatif le diagramme suivant de
\deleted{\illegible{1}} homomorphismes \inserted{de}
\deleted{foncteurs} systèmes locaux sur $\Pi'_D$
\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
(f_{\unsure{D^*|D}})^*\bigl(\unsure{\pi_1|\Pi_1}(\sigma)\bigr)
 & \unsure{\pi_1|\Pi_1}(\sigma')\arrow[l]\\
(f_{\unsure{D^*|D}})^*\bigl(\psi^*(\unsure{\tau|\mathcal T})\bigr)
 \arrow[u,"(f_{\unsure{D^*|D}})^*(k)","\sim"']
 \arrow[d,"\mathrm{can}","\sim"']
 & \psi'^*(\unsure{\tau|\mathcal T})
 \arrow[u,"k'","\sim"']\arrow[dl,"\sim"']\\
(\psi f_D)^*(\unsure{\tau|\mathcal T}) &
\end{tikzcd}
}
déduit de $\alpha_{De}:\psi'\simeq\psi\circ f_D$
\deleted{\illegible{1}}

\margin{\uline{non}, \illegible{3} \unsure{commute} \illegible{3}
\unsure{cas de morphismes} \unsure{étales}, sinon il faut faire
intervenir la multiplication par des degrés des morphismes
\illegible{2} ($\unsure{i'\in\pi_0(\Pi'_{D^*})}$).}

Pour $\Pi,\unsure{\Pi^*|\Pi'}$ fixes, les systèmes
\[
(f,\alpha):=(f_U,f_D,f_{D^*},\alpha_{D^*D},\alpha_{D^*U},
\alpha_{U,e},\alpha_{D,e})
\]
précédents forment une catégorie de \unsure{faç.} naturelle
--- en fait un groupoïde --- en prenant comme morphismes
\inserted{\unsure{$h$|$H$}} de $(f',\alpha')$ dans $(f,\alpha)$
les triplets des \unsure{isomorphismes|morphismes}
(foncteurs profinis)
\[
f'_U\xrightarrow{h_U}\unsure{f_U},\qquad
f'_D\xrightarrow{h_D}f_D,\qquad
f'_{D^*}\xrightarrow{h_{D^*}}\unsure{f_D|f_{D^*}}
\]

\scanpage{34}
\mspage{15}

satisfaisant \deleted{des} quatre conditions de compatibilité avec
$\alpha_{D^*D}$ et $\alpha'_{D^*D}$, avec $\alpha_{D^*U}$ et
$\alpha'_{D^*U}$, avec $\alpha_{Ue}$ et $\alpha'_{U,e}$, avec
$\alpha_{D,e}$ et $\alpha'_{D,e}$ respectivement.
(i.e. on travaille sur une ss-catégorie pleine de la
\unsure{$2$} cat. des \uline{$\mathrm{Hom}$} entre catégories
fibrées sur $Q$, à fibre en $e$ fixée\ldots).
J'ai l'impression que ce groupoïde
\uline{$\mathrm{Hom}$}$((f',\alpha'),(f,\alpha))$ est
\unsure{trop|très} \uline{rigide}, i.e.
$\mathrm{Aut}(f,\alpha)$ est toujours réduit au groupe unité
--- j'ai la flemme de vérifier --- donc que si $(f',\alpha')$ et
$(f,\alpha)$ sont isomorphes, l'isom. en question est unique.
Quoi qu'il en soit, on pose

$\mathrm{Hom}((f',\alpha'),(f,\alpha))=\pi_0$
\uline{$\mathrm{Hom}$}$((f',\alpha'),(f,\alpha))$

D'où une \uline{catégorie} des
\deleted{\unsure{couples} \illegible{1}} systèmes
$(\Pi_U,\Pi_D,\Pi_{D^*},\varphi,\psi,\rho,\sigma,\alpha,
\deleted{\illegible{1}}k)$

\scanpage{35}

On a un foncteur des couples $(X,S)$
(\unsure{i.e.} $X$ schéma \inserted{loc.} de t.f. sur $K$,
$S$ \uline{\unsure{ss-schéma}} \deleted{\unsure{discret}}
\inserted{fermé} \deleted{\illegible{1}} de $X$
\inserted{étale sur $K$} (\unsure{tel} que $\forall s\in S$, $X$
soit lisse de dim relative $1$ en $s$)
vers cette catégorie bordélique $\mathcal B$.

\margin{\unsure{Les} morphismes $(X',S')\to(X,S)$ sont les
morphismes $f:X'\to X$ tels que $f^{-1}(S)_{\mathrm{red}}=S'$.}

\uline{Conjecture bordélique \unsure{7.1}.}
Quand on se borne aux $(X,S)$ tels que $X$ projectif lisse de dim
$\leq 1$, et qui de plus sont anabéliens, alors le foncteur
précédent est pleinement fidèle.

\margin{\uline{NB} La fidélité est facile!}

Description de la catégorie bordélique en termes de théorie des groupes :

Soit $I=\pi_0(\Pi_{D^*})\simeq\pi_0(\Pi_D)$.
Choisissons un objet \inserted{$D_i^*$} dans chaque composante de
$\Pi_{D^*}$, et soit $D_i=\sigma(D_i^*)$.
Pour tt $i$, choisissons un isomorphisme
\[
\boxed{\psi(D_i)\xrightarrow[\simeq]{\unsure{\partial_{D_i}|\partial_i}}
\mathrm{Spec}(\overline K)}.
\]
\deleted{\illegible{4}}
Quitte à remplacer l'objet par un \unsure{``bon''} objet isomorphe,

\scanpage{36}
\mspage{16}

OPS que $\Pi_{D^*}$ est la catégorie somme des catégories
$[\mathcal E_i]$ définies par les
$\mathcal E_i=\mathrm{Aut}(D_i^*)$, $\Pi_D$
\deleted{est} \deleted{\illegible{1}}\inserted{la catégorie}
somme de catégories $[\Gamma_i]$ définies par les
$\Gamma_i=\mathrm{Aut}(D_i)$, le foncteur $\sigma$ s'exprimant
par un système d'homs
\[
\sigma_i:\mathcal E_i\to\Gamma_i\qquad(i\in I)
\]
qui sont surjectifs de noyaux abéliens,
\inserted{le foncteur $\psi$ par un système d'\uline{inclusions}
$\psi_i:\Gamma_i\subset\Gamma$}
et la donnée de $k$ équivaut en fait à des isom.
\[
k_i:\mathrm{Ker}\,\sigma_i\simeq T(\overline K)
\]
compatibles avec les op. de $\Gamma_i$ et $\Gamma$ sur les deux
\unsure{mbs|mbres} respectivement et les inclusions $\psi_i$.

\margin{\unsure{NB} \illegible{10} différents!}

On peut dire que la donnée de $(\sigma,\psi,k)$ est équivalente
à la donnée de syst. $(\mathcal E_i)_{i\in I}$, d'un système
\unsure{de} \deleted{homs} suites exactes
\deleted{$p_i:\Gamma_i\to\Gamma$}
\deleted{\illegible{5} et des isom. \illegible{1}}
\[
\boxed{1\to T(\overline K)\xrightarrow{k_i}\mathcal E_i
\xrightarrow{p_i}\Gamma}
\]
telles que les $\unsure{\Gamma_i|\mathcal E_i}
=\mathrm{Im}\,p_i$ soient ouverts, et que $k_i$ soit compatible
avec les opérations de $\Gamma_i\simeq\mathrm{Coker}\,k_i$
(i.e. de $\mathcal E_i$ et $\Gamma$ sur les deux termes respectivement).

\margin{\uline{NB} Les extensions des $\Gamma_i$ par
$T(\overline K)$ \illegible{2} obtenues par des situations géométriques
\illegible{4} --- \unsure{à les décrire}, \illegible{18}.}

\scanpage{37}

Supposons d'autre part (pour simplifier)
\deleted{\unsure{$X$}}\inserted{$\Pi_U$} connexe,
\deleted{\unsure{i.e.} $U=X\setminus S$ connexe, et}
et choisissons un objet $\widetilde U$ de $\Pi_U$ et un isom
\deleted{entre $\varphi(\widetilde U)$ et $\mathrm{Spec}\,K$}
\[
\varphi(\widetilde U)\xrightarrow{\unsure{\partial_U|\delta_U}}
\mathrm{Spec}(\overline K)
\]
Alors (quitte à remplacer $\Pi_U$ par un groupoïde équivalent)
OPS $\Pi_U$ réduit à $\widetilde U$, et $\Pi_U$ est décrit par
un groupe $\mathcal E$, et $\varphi$ par un hom de groupes
\[
\boxed{\mathcal E
\xrightarrow{\deleted{\illegible{1}}\,\unsure{\varphi_{\widetilde U,\partial_U}}}
\Gamma}
\]
\inserted{(ou $p$)}
dont l'image $\Gamma_0\subset\Gamma$ est donc un ss-groupe ouvert
de $\Gamma$, et le noyau \unsure{sera noté} $\unsure{\pi|\Pi}$
\[
\boxed{1\to\unsure{\pi|\Pi}\xrightarrow{\unsure{\kappa|\iota}}\mathcal E
\xrightarrow{\unsure{\varphi|p}}\Gamma_0\to1}
\]
\diagram{[Sous $\Gamma_0$, un signe d'inclusion vertical vers $\Gamma$.]}

\margin{Dans les situations géom. \uline{NB} Cette extension vient
 de \uline{\illegible{4}} \unsure{splittés}, i.e. \illegible{8}
 \deleted{\illegible{4}} \illegible{5}.
 \diagram{[Petit diagramme remanié, partiellement recouvert :
 $\unsure{\Gamma_0|\Gamma_\infty}\to\mathcal E$ ;
 autres objets et flèches \illegible{4}.]}}

[Ayant remplacé le $\Pi_U$ initial par une ss-catégorie pleine
plus petite, on sera obligé de modifier $\rho$ à isom près,
\unsure{ce qui se fait} en choisissant pour chaque $i\in I$ un isom.
\[
\rho(D_i)\xrightarrow{\mu_i}\widetilde U].
\]

\scanpage{38}
\mspage{17}

moyennant quoi $\rho$ s'explicite simplement par des
\uline{homomorphismes} de groupes
\[
\boxed{\rho_i:\mathcal E_i\longrightarrow\mathcal E}
\]
Il reste à expliciter l'isom de commutation
\[
\alpha:\varphi\rho\to\psi\sigma
\]
qui est défini par un système d'éléments
\[
\boxed{\unsure{\gamma_i|\sigma_i}\in\Gamma\qquad(i\in I)}
\]
tels que
\[
\unsure{(\alpha)|(*)}\qquad
\varphi\circ\rho_i=\mathrm{int}(\unsure{\gamma_i|\sigma_i})\circ p_i.
\]
Ce qui implique d'ailleurs que $\rho_i$ \deleted{\illegible{1}}
applique $\mathrm{Ker}\,p_i$ dans $\mathrm{Ker}\,p$, i.e. induit
un hom de suites exactes
\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
1\arrow[r] & T(\overline K)\arrow[r]\arrow[d] &
\mathcal E_i\arrow[r]\arrow[d,"\rho_i"] &
\deleted{\unsure{\mathcal E_i}}\inserted{\Gamma_i}
\arrow[r]\arrow[d,hook] & 1\\
1\arrow[r] & \unsure{\pi|\Pi}\arrow[r] & \mathcal E\arrow[r] &
\deleted{\unsure{\mathcal E_0}}\inserted{\Gamma_0}
\arrow[r] & 1
\end{tikzcd}
[Sous $\Gamma_0$, un signe d'inclusion et $\Gamma$.]
}
avec un hom induit $\Gamma_i\to\Gamma_0$ injectif
--- et à ceci près, la relation de compatibilité
\unsure{$(\alpha)$|$(*)$} devient une relation sur des
monomorphismes de groupes
\diagram{
\begin{tikzcd}
\Gamma_i\arrow[rr,hook]\arrow[dr] & & \Gamma\\
 & \Gamma_0\arrow[r,hook] & \Gamma
\end{tikzcd}
}

\scanpage{39}

\deleted{\uline{NB} Quand $I$ est vide i.e. $\Pi_{D^*},\Pi_D$
vides, alors les systèmes ``bordéliques'' \unsure{découlant}
de situations géom. correspondent à : $\unsure{\pi|\Pi}=\{1\}$, et
$\mathcal E$ se réduit à un \unsure{ss-groupe}}

Ainsi, on a une description relativement simple des systèmes
bordéliques ``réduits'' (i.e. où dans les groupoïdes
$\Pi_U,\Pi_{D^*},\Pi_D$, chaque composante connexe a exactement
un objet, et où \inserted{de plus} on force en quelque sorte
$\unsure{\Pi_1(K)|\Pi_e(K)}$ à n'avoir que l'objet
$\mathrm{Spec}(\overline K)$.
Mais on est \unsure{retourné} \unsure{en tournant}
\unsure{pr|par} la détermination des \uline{morphismes} des systèmes
\[
\mathcal G=(\inserted{I,}G_i,p_i,k_i,\mathcal E,\varphi,\rho_i,
\unsure{\gamma_i|\sigma_i})
\quad\hbox{et}\quad
\mathcal G'=(I',G'_{i'},\ldots),
\]
\inserted{(ou $p$)}
\deleted{\illegible{2}} disons dans le sens
\[
f:\mathcal G'\to\mathcal G.
\]
Il faut donc \inserted{(pour $f_{D^*}$)} une application
\[
\boxed{\deleted{\illegible{1}}\,\unsure{\tau=\tau_f}:I'\to I},
\]
et $\forall\unsure{i'|i}$ un hom
\[
\boxed{G'_{i'}\xrightarrow{f_{i'}}G_{\tau i'}},
\]
\deleted{\unsure{induisant} \illegible{2}}
\inserted{(\unsure{compat. au $D$})}
induisant \inserted{\unsure{par passage au quotient}} des homs
\[
\Gamma'_{i'}\xrightarrow{g_{i'}}\Gamma_{\tau i'}
\]
\deleted{\illegible{2}}

\margin{Les ``systèmes bordéliques simplifiés'' sont donc les
systèmes d'homs de suites exactes
\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
1\arrow[r] & T(\overline K)\arrow[r,"k_i"]
\arrow[d,"\unsure{\rho_i^0}"] &
\mathcal E_i\arrow[r,"p_i"]\arrow[d,"\rho_i"] &
\Gamma\arrow[d,"\mathrm{int}(\unsure{\gamma_i|\sigma_i})"]\\
1\arrow[r] & \unsure{\pi|\Pi}\arrow[r,"\unsure{\kappa}"] &
\mathcal E\arrow[r,"p"] & \Gamma
\end{tikzcd}
}}

\scanpage{40}
\mspage{18}

les ss-groupes ouverts de $\Gamma$,
et la donnée \inserted{$f_{D^*},f_D,$}
\unsure{de} $\alpha_{D^*D},\alpha_{D,e}$ équivaut alors
à la donnée d'éléments $\unsure{\alpha_i|\alpha_{i'}}$
$(\unsure{i\in I|i'\in I'})$ de $\Gamma$,
\inserted{$\boxed{\unsure{\alpha_{i'}|\alpha_i}\in\Gamma}
\quad(i'\in I')$}
tels que
\deleted{\illegible{6}}
\[
g_{i'}(\sigma')=\mathrm{int}(\alpha_{i'})(\sigma')
\qquad\forall i'\in I',\quad\sigma'\in\Gamma'_{i'}.
\]
La donnée de $f_U$ équivaut à la donnée d'un hom de groupes
\[
\boxed{f_{\mathcal E}:\mathcal E'\to\mathcal E}
\]
celle de $\alpha_{D,e}$ équivaut à la donnée de
\[
\boxed{\alpha\in\Gamma}
\]
tel que
\[
\unsure{(\alpha)|(*)}\qquad
\varphi f_{\mathcal E}=\mathrm{int}(\alpha)\varphi
\]
de sorte que $f_{\mathcal E}$ induit un hom de suites exactes
\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
1\arrow[r] & \unsure{\pi|\Pi}'\arrow[r]\arrow[d] &
\mathcal E'\arrow[r]\arrow[d,"f_{\mathcal E}"] &
\Gamma'_0\arrow[r]\arrow[d,"f_{\Gamma_0}"] & 1\\
1\arrow[r] & \unsure{\pi|\Pi}\arrow[r] & \mathcal E\arrow[r] &
\Gamma_0\arrow[r] & 1
\end{tikzcd}
[Au-dessus de $\Gamma'_0$, $\Gamma$ avec un signe d'inclusion
vertical ; sous $\Gamma_0$, un signe d'inclusion et $\Gamma$.]
}
et moyennant cela, la condition notée \unsure{$(\alpha)$|$(*)$}
\deleted{est}\inserted{devient} une condition sur des
\inserted{inclusions de} ss-groupes de $\Gamma$ :
\[
f_{\Gamma_0}(\sigma')=\mathrm{int}(\alpha)\sigma'
\quad\hbox{si}\quad\sigma'\in\Gamma'_0.
\]
Il faut expliciter encore (en plus des
$f_{D^*},f_D,f_U,\alpha_{D^*D},\alpha_{De},\alpha_{Ue}$
déjà explicités) le
```

# LM_P04 — Editorial and research notes

The scan numbers are 31–40, following the supplied order. The archival footer numbers visible in the images are 30–39. The separate manuscript headings 14, 15, 16, 17, and 18 are recorded on scans 32, 34, 36, 38, and 40. Approximate line numbers below count handwritten baselines, including displayed mathematics; they are not LaTeX file line numbers.

## 2. Table of doubts

Confidence concerns the proposed reading, not its mathematical plausibility. Unreadable cancellations are retained in the transcription even when they cannot be assigned a lexical alternative. Repeated instances of the same doubtful symbol are grouped here.

| Scan | Approximate line or location | Proposed reading | Alternative or unresolved point | Confidence |
|---|---|---|---|---|
| 31 | 1 | `c)` | `e)`; the referenced condition is not securely distinguishable. | Low |
| 31, 33 | Relative-group formulas | `\pi_1` | `\Pi_1`; the handwritten letter forms do not securely establish case. | Medium |
| 31 | 3–4, insertion | `i.e. un foncteur (\Pi_D)^o → Ens` | The initial abbreviation and extent of the underline are less secure than the formula. | Medium |
| 31 | 5–6 | `kummérien`; label `k` | Accent/letter sequence uncertain; the overwritten former label is unreadable. | Medium |
| 31, 33 | Formulas involving `\psi^*` | `\tau` | Calligraphic `\mathcal T`. | Low |
| 31 | Lower prism | Right-hand `\varphi'`; bottom identity | The prime and the bottom mark are faint; the other principal labels are clearer. | Medium |
| 32 | 4, parallel arrows | `\mathrm{id}\circ\psi'\circ\sigma'` | Initial `id` partly overwritten. | Medium |
| 32 | 10–11 | Small additional `\Pi`; deleted `de diagramme en forme` | The status of the small symbol and the exact cancelled words are unresolved. | Low |
| 32 | Square `Q` | Left vertex `U` | Overwritten vertex; arrowheads on three sides are not clearly visible. | Medium |
| 33 | 8–12, pullback diagram | Subscript `D^*` in `(f_{D^*})^*` | `D`; the preceding separate formula visibly uses `f_D`. | Medium |
| 33 | Left margin beside diagram | `non`, `commute`, `cas de morphismes étales`, degree qualification | Several connecting words and the final indexed expression are unreadable. | Low |
| 33 | 13 | `\Pi^*` in “Pour … fixes” | `\Pi'`; superscript resembles a small star. | Low |
| 33 | 15–17 | `faç.`; inserted `h` or `H`; `isomorphismes` | `façon` may be written more fully; case of inserted letter and prefix of “morphismes” uncertain. | Low |
| 33 | Final arrows | Last target `f_D` | Possible `f_{D^*}`; no secure terminal star. The first target also has overwriting. | Low |
| 34 | 6 | `2 cat.` | Numeral before `cat.` is heavily inked. | Medium |
| 34 | 9 | `trop rigide` | `très rigide`. | Medium |
| 34 | 17–18 | Deleted `couples`; deleted symbol before `k` | Remaining cancelled material unreadable. | Low |
| 35 | 2–4 | `i.e.`, `ss-schéma`, deleted `discret`, `tel` | Revisions overlap; placement of “fermé” and “étale sur K” is clearer than the cancelled wording. | Low |
| 35 | Upper-left margin | Morphisms with `f^{-1}(S)_{red}=S'` | Opening “Les” and the accent, if any, in the small subscript are uncertain. | Medium |
| 35 | Conjecture heading | `7.1` | First character could be `9` or a letter-like form; identifier unresolved. | Low |
| 35 | 18, isomorphism label | `\partial_{D_i}` | `\partial_i`; overwritten label. | Low |
| 35 | Final line | `“bon” objet` | Quoted adjective not secure. | Low |
| 36 | 3–4 | Replacement `la catégorie` | Underlying cancelled words partly unreadable. | Medium |
| 36 | 12–13 | `mbs` | `mbres`; both would abbreviate “membres.” | Low |
| 36 | 16–19 | Revised phrase introducing exact sequences; deleted `p_i:\Gamma_i→\Gamma` | Several words and the old displayed line are heavily cancelled. | Low |
| 36 | 20 | `\Gamma_i=\mathrm{Im}\,p_i` | Overwritten initial letter could be read `\mathcal E_i`; no correction from context has been imposed. | Medium |
| 36 | Both left margins | Fragments concerning extensions and geometric situations | Much remains unreadable, including essential qualifications; no complete claim is recovered. | Low |
| 37 | 2–4 | Deleted `X`, deleted `i.e.`, label `\partial_U` | Old first symbol uncertain; label could be `\delta_U`. | Low |
| 37 | 10 | `\varphi_{\widetilde U,\partial_U}`; insertion `(ou p)` | Subscript and original overwritten arrow label are not fully secure. | Low |
| 37–40 | Global-kernel formulas | `\pi` | Capital `\Pi`; repeated manuscript form retained as uncertain. | Medium |
| 37, 39 | Kernel inclusion label | `\kappa` | `\iota`, or a handwritten `k`; case/form uncertain. | Low |
| 37 | 13–14 | `sera noté`; quotient-map label `\varphi` | Overwriting; `p` is an alternative map-label reading. | Medium |
| 37 | Margin around boxed sequence | `Dans les situations géom.`, `Cette extension vient`, `splittés` | Most intervening text and part of the small diagram remain unreadable. | Low |
| 37 | 17–19 | `ce qui se fait`; `\rho(D_i)` | Connecting phrase uncertain; no star is securely visible on `D_i`. | Medium |
| 38–39 | Conjugating elements | `\gamma_i` | `\sigma_i`; the same ambiguity recurs in the boxed element, formula, tuple, and margin. | Medium |
| 38, 40 | Equation labels | `(\alpha)` | `(*)`; small reference mark not securely resolved. | Low |
| 38 | Exact-sequence diagram | Corrected quotient symbols `\Gamma_i`, `\Gamma_0` | Underlying overwritten symbols appear to be `\mathcal E_i`, `\mathcal E_0`. | Medium |
| 39 | Opening cancelled note | `découlant`; `ss-groupe` | These words are less secure than the cancellation itself, which is clear. | Medium |
| 39 | 10 | `\Pi_1(K)` | `\Pi_e(K)`. | Low |
| 39 | 11–13 | `retourné`, `en tournant`, `pr` | The transition remains unresolved; `par` is an alternative to `pr`. No grammatical repair supplied. | Low |
| 39 | Tuple and final boxes | `G_i`, `\tau=\tau_f`, `\forall i'` | Index-map label overwritten; prime on the quantified index not secure. The visible `G_i` is not replaced by earlier `\mathcal E_i`. | Medium |
| 39 | 18–19 | `compat. au D`; `par passage au quotient` | Wording and insertion boundaries uncertain. | Low |
| 39 | Marginal diagram | First vertical label `\rho_i^0` | Superscript may be another small mark. | Low |
| 40 | 2–4 | Inserted `f_{D^*},f_D`; correction from `\alpha_i` to `\alpha_{i'}` | Placement and priming are crowded; original and inserted index ranges differ or appear to differ. | Low |
| 40 | 11 and 14 | `\alpha_{D,e}`; final unprimed `\varphi` in `\varphi f_{\mathcal E}=\mathrm{int}(\alpha)\varphi` | These are retained as visible. `\alpha_{U,e}` and `\varphi'` would be conjectural corrections, not adopted readings. | High |

## 3. Abbreviations met

Expansions below are editorial; they have not been substituted into the transcription. Some entries are mathematical operator abbreviations rather than prose abbreviations.

| As written or provisionally read | Proposed expansion |
|---|---|
| `syst.` | système; systèmes |
| `gr.` | groupe; groupes |
| `i.e.` | id est; c'est-à-dire |
| `isom.`, `isom` | isomorphisme; isomorphismes |
| `hom`, `homs`, `l'hom.` | homomorphisme; homomorphismes; l'homomorphisme |
| `cat.` | catégorie |
| `ss-catégorie`, `ss-groupe`, `ss-groupes`, uncertain `ss-schéma` | sous-catégorie; sous-groupe(s); sous-schéma |
| uncertain `faç.` | façon |
| `loc.` | localement |
| `t.f.` | type fini |
| `dim` | dimension |
| `tt` | tout, in “Pour tt i” |
| `OPS` | on peut supposer |
| `op.` | opérations |
| uncertain `mbs` / `mbres` | membres |
| `NB` | nota bene |
| `géom.` | géométrique; géométriques |
| `can` | canonique |
| uncertain `pr` | probably pour; `par` is a competing reading, not an expansion |
| uncertain `compat.` | compatibilité; compatible, depending on the unrecovered phrase |
| `Aut`, `Hom`, `Ker`, `Coker`, `Im` | automorphismes; morphismes; noyau; conoyau; image |
| `Ens`, `Spec`, `int`, `red` | ensembles; spectre; automorphisme intérieur; réduit |

## 4. Legibility note

The main prose and most large displayed formulas are appreciably more legible than the marginal additions. The least reliable passages are the margin on scan 33, both margins on scan 36, the note surrounding the boxed extension on scan 37, the transition and lower revisions on scan 39, and the overwritten opening of scan 40. The conjecture identifier is unresolved. Several recurring symbol forms remain doubtful, particularly the case of pi, the symbol pulled back by psi, and the letter used for the conjugating elements.

This is a provisional diplomatic reading with explicit gaps. Counts in `\illegible{n}` are estimates, not verified word counts. Marginal qualifications have not been converted into complete mathematical assertions. The cancelled opening note on scan 39 remains cancelled, and the unfinished final sentence on scan 40 remains unfinished.

## 5. Research notes — English

These notes distinguish manuscript assertions from proposed investigations. They use only the supplied pages; no published transcription or external literature has been used to resolve readings. Where a reading is uncertain, the corresponding research interpretation is conditional on it.

**R1 — Scans 31–34, definition of morphisms and their groupoid. Kind: unproved claim.** The descriptions “un système de 3 foncteurs” and “en fait un groupoïde” lead to a categorical construction whose composition is not checked here. A proof would need to specify composition of the four commutation isomorphisms, establish preservation of the two compatibility conditions, and check that the described transformations are invertible. The doubtful pullback subscripts on scan 33 should be settled before writing those checks as formulas.

**R2 — Scan 32, middle bracketed discussion. Kind: conjecture / expectation.** “Cette compatibilité pourrait s'exprimer” proposes a formulation using a category fibred over the square Q. The investigation is to compare the explicit prism condition with the data of a cartesian functor over Q whose fibre at e is fixed. One should verify the direction of the comparison and the fixed-fibre condition, rather than merely identify the two pictures informally.

**R3 — Scan 33, margin beside the compatibility diagram. Kind: unproved claim, reading provisional.** The recoverable words include “multiplication par des degrés des morphismes.” This appears to qualify the naive compatibility in the adjacent diagram, but the preceding hypothesis is not fully readable. Any proof or counterexample should first establish exactly which morphisms are being excluded or admitted, and only then determine where the degree factor acts.

**R4 — Scan 34, rigidity paragraph. Kind: conjecture / expectation.** “J'ai l'impression” introduces the assertion that the relevant automorphism group is reduced to the unit group, followed by “j'ai la flemme de vérifier.” This is explicitly an expectation, not a proved rigidity result on these pages. A proof would need to show that all compatible triples of automorphisms are identities under the actual hypotheses on the systems.

**R5 — Scan 34, same paragraph. Kind: own idea.** Test the rigidity assertion first on one-object groupoids: a natural automorphism of a group homomorphism f is represented by a target-group element centralizing the image of f. The four face conditions and the fixed base should then give additional equations on these centralizer elements. **Confidence: high for this diagnostic calculation, not for the conjectured triviality**, because the centralizer condition follows directly from the naturality equation; the extra equations may or may not force the identity.

**R6 — Scan 34, passage to pi-zero. Kind: unpursued implication.** The passage “Quoi qu'il en soit, on pose” separates taking connected components of the morphism groupoid from the preceding uniqueness expectation. It suggests checking well-defined composition on isomorphism classes independently of proving rigidity. Failure of uniqueness would not, by itself, show that this passage to an ordinary category fails.

**R7 — Scan 35, central conjecture. Kind: conjecture.** The claim is that “le foncteur précédent est pleinement fidèle” for the stated pairs with X projective and smooth of dimension at most one and with the additional condition “anabéliens.” Its identifier is not securely read, so it should not yet be cited by a definite conjecture number. A proof requires the precise meaning of that additional condition and all hypotheses on K from the surrounding manuscript, as well as the exact source-category morphisms indicated in the margin.

**R8 — Scan 35, marginal note. Kind: unproved claim.** “La fidélité est facile!” is asserted without an argument in this excerpt. The required proof would show that two permitted geometric morphisms inducing the same morphism class of systems are equal. This should be treated separately from fullness, which requires constructing a geometric morphism from an abstract morphism of systems.

**R9 — Scans 35–36, reduction to group data. Kind: unproved claim.** “On peut dire que la donnée … est équivalente” asserts a replacement of groupoid-level data by indexed groups, kernel identifications, and maps to Gamma. A proof should construct an inverse description and track changes of the chosen objects and their identifications with Spec of the algebraic closure. It should also check the stated openness and equivariance requirements, and record how the isomorphism k_i is used when its arrow is drawn in the opposite direction in the exact-sequence display.

**R10 — Scans 37–38, changes of the chosen isomorphisms mu_i. Kind: own idea.** Assuming the convention int(g)(x)=gxg^{-1}, and assuming that a change of mu_i replaces rho_i by int(h_i) composed with rho_i, the displayed commutation relation is preserved by replacing the conjugating element gamma_i with phi(h_i)gamma_i. This is a concrete test of the independence of the chosen one-object presentation. **Confidence: high as a conditional algebraic calculation**, because it follows by substituting into the displayed relation; the direction of the manuscript's choice-change must still be checked.

**R11 — Scan 38, paragraph following the conjugation identity. Kind: unproved claim.** “Ce qui implique d'ailleurs” introduces the assertion that rho_i maps Ker p_i into Ker p. Formally, the displayed identity gives this containment because conjugation fixes the identity element. What still needs checking in the complete construction is compatibility with the selected kernel identifications and the precise maps in the exact-sequence diagram.

**R12 — Scan 38, induced map on the quotient groups. Kind: unpursued implication.** The text calls the induced map Gamma_i to Gamma_0 “injectif.” Its asserted injectivity should be checked using the identification of Gamma_i with Im p_i and the restriction of the conjugation map in Gamma. That statement must not be silently strengthened to injectivity of rho_i or of the map from T of the algebraic closure to the global kernel.

**R13 — Scan 39, cancelled opening NB. Kind: own idea prompted by a struck-through claim.** The cancelled passage associates empty I with “pi={1}”; it is not an active conclusion of the text. As a test at the level of abstract group data, take a nontrivial finite group H, an open subgroup Gamma_0 of Gamma, and E=H times Gamma_0 with projection to Gamma: the boundary index set can be empty while the kernel is H. **Confidence: high for this elementary group-data example**, since the kernel is explicit; it does not assert geometric realizability or satisfaction of any additional axioms outside the supplied pages.

**R14 — Scans 39–40, description of morphisms. Kind: unproved claim / unfinished construction.** The final words are “Il faut expliciter encore … le,” so this excerpt does not finish the group-theoretic morphism description. A complete comparison would have to include the remaining commutation datum, its compatibility, equivalence between choices of conjugating elements, and composition. The apparently unexpected index alpha_{D,e} and the unprimed right-hand phi on scan 40 should first be collated, not silently repaired during that comparison.

## Primary-source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, supplied scans 31–40]. Université de Montpellier.

The author, title, date, and archival identification in this reference are those supplied with the task; they have not been independently verified.
