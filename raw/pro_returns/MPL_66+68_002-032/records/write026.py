from record_page import record
record(26,r'''\scanpage{26}
\uline{Proposition}\quad \unsure{Soient|Soit} $\Sigma$ une $j$-Stratégie, $x_0\in C$ \deleted{position} gagnante pour $\Sigma$, $X=(x_0,x_1,\ldots,x_n\ldots)$ une partie (d'origine $x_0$) jouée suivant $\Sigma$, alors toutes les positions $x_i$ sont gagnantes pour $\Sigma$.

Soit en effet $Y=(y_0=x_i,y_1,\ldots,y_m,\ldots)$ une partie \inserted{maximale} jouée suivant $\Sigma$, \deleted{\unsure{et}} alors $XY$ est jouée suivant $\Sigma$ et est d'origine $x_0$ gagnante pour $\Sigma$, donc \deleted{est gagnée par $j$ donc $Y$ est finie} donc $Y$ est gagnée par $j$.

\uline{Th} On a \deleted{\unsure{rappel}}
\[
\begin{aligned}
a)\quad&G(j)\cap C(j)=\{x_0\in C(j)\mid R(x_0)\cap G(j)\ne\varnothing\}\\
b)\quad&G(j)\cap\bar C(j)=\{x_0\in\bar C(j)\mid R(x_0)\subset G(j)\}
\end{aligned}
\]
[et pour mémoire
\[
G(j)\cap C_0=\unsure{C_0|G_0}(j)
\]
].

\uline{Dém}\quad a) On suppose $x_0\in C(j)$.

\deleted{a)} 1) $\subset$ Soit $x_0\in G(j)\deleted{\cap C(j)}$, \inserted{soit} $\Sigma$ une stratégie pour $j$ gagnante pour $x_0$, considérons $x_1\in\Sigma(x_0)$, alors $(x_0,x_1)$ est une $\Sigma$-partie, donc par la prop. précédente, $x_1$ est gagnant pour $\Sigma$, donc $j$-gagnant, donc $x_1\in R(x)\cap G(j)$, donc $R(x)\cap G(j)\ne\varnothing$.

2) $\supset$ Soit $x_1\in R(x)\cap G(j)$. Prouvons que $x_0\in G(j)$. \deleted{\unsure{On déf}} Soit $\Sigma_1$ une $j$-stratégie $x_1$-gagnante. Si $x_0$ est gagnant pour $\Sigma_1$, on a $x_0\in G(j)$, OK. Sinon, définissons une $j$-stratégie $\Sigma_0$ $x_0$-gagnante ainsi :
\[
\begin{aligned}
\Sigma_0(x_0)&=\{x_1\}\\
\Sigma_0(x)&=\Sigma_1(x)\quad\text{si }x\ne x_0
\end{aligned}
\]
% archive foliation: 25
''',[
('text','top','Proposition Soient Σ une j-Stratégie ...'),
('deletion','top right','position'),
('text','upper middle','Soit en effet Y=(y_0=x_i,...), une partie ...'),
('insertion','upper middle','maximale'),
('deletion','upper middle','et'),
('deletion','middle','est gagnée par j donc Y est finie'),
('text','middle','Th On a'),
('deletion','middle','rappel'),
('display','middle','a) G(j)∩C(j)=...; b) G(j)∩bar C(j)=...'),
('text','middle lower','[et pour mémoire'),
('display','middle lower','G(j)∩C_0=C_0(j)]'),
('text','lower','Dém a) On suppose x_0∈C(j); 1) ⊂ ...'),
('deletion','lower','a); ∩C(j)'),
('insertion','lower','soit'),
('text','bottom','2) ⊃ Soit x_1∈R(x)∩G(j) ...'),
('deletion','bottom','On déf'),
('display','bottom edge','Σ_0(x_0)={x_1}; Σ_0(x)=Σ_1(x) si x≠x_0')
],'''The propagation proposition repeats the earlier winning-strategy lemma. Its proof writes XY even though Y starts at x_i rather than the final point of the full X: any formal account needs the prefix through x_i, not a silent change to the transcription. The theorem gives existential/universal predecessor equations for G(j); the terminal identity’s first letter is visually closer to C_0 than G_0 and remains doubtful. The converse proof again anticipates a return-to-x_0 problem by separating the case where Σ_1 already wins from x_0; continuation on scan 27 is essential.''')
