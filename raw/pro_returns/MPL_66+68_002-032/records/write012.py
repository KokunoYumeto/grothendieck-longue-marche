from record_page import record
record(12,r'''
\scanpage{12}
% archive foliation: 11
une partie compatible avec $\Sigma$, commençant avec $x_0\in\overline G(j')$, et maximale i.e. $x_N\in C_0$, prouvons $x_N\in\overline G(j')$. On \deleted{le} prouve par réc. $x_i\in\overline G(j')\quad0\leq i\leq N$.
Supposons $x_i\in\overline G(j')$, \inserted{$0\leq i\leq N-1$} prouvons $x_{i+1}\in\overline G(j')$\ldots

A vrai dire, on a fait deux fois le même raisonnement. Considérons un jeu auxiliaire $\mathcal J'=\mathcal J(j')$ : deux joueurs $j'$ et $\overline{j'}=j$, avec même ens des \deleted{situations} positions $C'=C$, \inserted{$R'=R$} et
\[
C'(j')=C(j'),\quad C'(j)=C(J')\quad(J'=J-\{j'\}),
\]
\inserted{(on pose aussi $C(j)$)}
\deleted{\unsure{Pour}}
\[
G'_0(j')=G_0(j'),\quad G'_0(j)=C'_0\setminus G'_0(j')=C_0\setminus G_0(j')
\]
\inserted{(on le note aussi $\overline G_0(j')$)}
Alors $C_0=G'_0(j)\amalg\unsure{C'_0(j')|G'_0(j')}$.

Alors les stratégies du jeu $\mathcal J$ pour $J'=J\setminus\{j'\}$ sont les stratégies du jeu $\mathcal J'=\mathcal J(j')$ pour $j$, et une stratégie \inserted{$\Sigma'$} est acceptable \inserted{pour $x\in C$} contre $j'$ ssi elle est gagnante pour $x$ \inserted{(pour $j$)}.
\margin{S'il n'y a pas de parties infinies\ldots}
Donc les \inserted{positions} $x\in C$ \uline{acceptables} \deleted{pour}\inserted{contre} $j'$ sont celles qui sont gagnantes pour $j$.

Comme $G_0(j')\cap G_0(j)=\varnothing$, on sait déjà qu'un $x$ ne peut être simultanément gagnant pour $j$ et $j'$ : \inserted{gagnant pour $j$ $\Longrightarrow$ non gagnant pour $j'$} le raisonnement précédent montre \deleted{que le} l'implication en sens inverse.
''',[
('text','top','une partie compatible avec Sigma commençant avec x_0 ...'),('display','top inline','x_N in C_0; x_N in Gbar(j prime); x_i in Gbar(j prime) 0<=i<=N'),('deletion','top','le'),('text','upper','Supposons x_i in Gbar(j prime), prouvons ...'),('insertion','upper','0<=i<=N-1'),('text','middle','A vrai dire on a fait deux fois le même raisonnement'),('text','middle','Considérons un jeu auxiliaire J script prime=J script(j prime)'),('display','middle inline','j prime and bar(j prime)=j; C prime=C'),('deletion','middle','situations'),('insertion','middle','R prime=R'),('display','middle','C prime(j prime)=C(j prime), C prime(j)=C(J prime)'),('insertion','middle','on pose aussi C(j)'),('deletion','middle-left','Pour'),('display','middle-lower','G prime_0(j prime)=G_0(j prime); G prime_0(j)=complement'),('insertion','above terminal complement','on le note aussi Gbar_0(j prime)'),('display','middle-lower','C_0=G prime_0(j) disjoint union C prime_0(j prime)'),('text','lower','Alors les stratégies du jeu J ...'),('insertion','lower','Sigma prime; pour x in C; pour j'),('margin note','lower-left diagonal','S’il n’y a pas de parties infinies ...'),('text','lower','Donc les positions x in C acceptables ... gagnantes pour j'),('insertion','lower','positions; contre'),('deletion','lower','pour'),('text','bottom','Comme G_0(j prime) cap G_0(j)=empty ...'),('insertion','bottom','gagnant pour j implies non gagnant pour j prime'),('deletion','bottom','que le')
],'''He explicitly observes “on a fait deux fois le même raisonnement” and packages the complementary coalition as a single opponent in an auxiliary two-player game. Acceptable-versus-winning equivalence is accompanied by the marginal condition “S’il n’y a pas de parties infinies...” This condition cannot be dropped: acceptable play can be infinite whereas winning play must terminate. The complement notation and changed player labels should be distinguished from a claim about the original multiplayer game.''')
