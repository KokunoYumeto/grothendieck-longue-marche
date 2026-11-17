from save_page import save_page
save_page(56,r'''\scanpage{56}
\mspage{14}
% archive foliation: 55
\uline{Invariants de Galois et \unsure{thms} de commutation}

$X$ propre liss sur $K$ de type fini

$H^{2i}(\overline{X},\mathbf{Q}_\ell(i))$ est de poids $0$, donc peut avoir des invariants non nuls sous Galois.
La conjecture de Tate s'énonce en disant que
\[
H^{2i}(\overline{X},\mathbf{Q}_\ell(i))^\pi\simeq A^i(X/K)\otimes_{\mathbf{Q}}\mathbf{Q}_\ell
\]
On peut la préciser ainsi :

L'anneau des correspondances alg /$K$ \deleted{\unsure{en}} \inserted{opérant en dim $i$}, \deleted{$\unsure{C^i}$} $\unsure{\mathcal{U}^i|\mathcal{W}^i}(X/K)$ est un anneau semi-simple, et [via Hodge] et on veut que
\[
\unsure{\mathcal{U}^i|\mathcal{W}^i}(X/K)\otimes_{\mathbf{Q}}\mathbf{Q}_\ell
\]
soit le commutant de $\pi=\mathrm{Gal}(\overline{K}/K)$ dans $\mathrm{End}_{\mathbf{Q}_\ell}(H^i(X,\mathbf{Q}_\ell(0)))$, \uline{et} l'alg. enveloppe de $\pi$ ds $\mathrm{End}_{\mathbf{Q}_\ell}(H^i)$ doit être le commutant de $\unsure{\mathcal{U}^i|\mathcal{W}^i}(X/K)$ [donc \uline{l'action de $\pi$ est \unsure{ssimple}}]

Le deuxième énoncé $+$ injectivité de
\diagram{\begin{tikzcd}
\unsure{\mathcal{U}^i|\mathcal{W}^i}(X/K)\otimes_{\mathbf{Q}}\mathbf{Q}_\ell \arrow[r] & \mathrm{End}_{\mathbf{Q}_\ell}(H^i(X,\mathbf{Q}_\ell(0)))
\end{tikzcd}}
entraîne tout.
''',[
('top','text','14) Invariants de Galois et thms de commutation'),
('upper','text','X propre liss sur K de type fini'),
('upper-middle','text','H^{2i}(Xbar,Q_l(i)) est de poids 0; conjecture de Tate'),
('middle','display','H^{2i}(Xbar,Q_l(i))^pi ~= A^i(X/K) tensor Q_l'),
('middle','text','On peut la préciser ainsi'),
('lower-middle','text',"L'anneau des correspondances alg /K; semi-simple"),
('lower-middle','display','U^i(X/K) tensor Q_l'),
('lower','text',"soit le commutant; et l'alg. enveloppe"),
('bottom','text','Le deuxième énoncé + injectivité; entraîne tout'),
('bottom','diagram','U^i(X/K) tensor Q_l -> End_{Q_l}(H^i(X,Q_l(0)))')],remarks='Whole page and both supplied halves inspected and compared. Ring letter is a calligraphic U/W form, kept doubtful pending cross-page comparison.')
