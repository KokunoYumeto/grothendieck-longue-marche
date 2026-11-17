from record_page import record

record(188, r'''\scanpage{188}
\mspage{70}

that there exists $n_0(K)$ such that at $n\unsure{\mathrm m|\geq}n_0(K)$
\[
H^i(V,K[nE])=0\qquad i=1,2,\ldots
\]

From the exact sequence
\diagram{\[
\begin{tikzcd}[column sep=large]
H^i(V,O_V(-E_{\varphi})[nE]) \arrow[r] & H^i(V,O_V[nE]) \arrow[r] & H^i(V,K[nE])
\end{tikzcd}
\]}
at $n\geq n_0(K)$, $i=1,2,\ldots$ we obtain:
\[
\dim H^i(V,O_V[nE])\leq\dim H^i(V,O_V(-E_{\varphi})[nE]).
\]

Since
\[
O_V(-E_{\varphi})\cong O_V[-E],
\]
then
\[
O_V(-E_{\varphi})[nE]\cong O_V[-E][nE]\cong O_V[(n-1)E].
\]

Therefore, at $n\geq n_0(K)$, $i=1,2,\ldots$
\[
\dim H^i(V,O_V[nE])\leq\dim H^i(V,O_V[[n-1]E]).
\]

Evidently, there exists such $n'$ that, at $n\geq n'$

\margin{187}
''', [
('margin note','top right','70'),
('text','top','that there exists n_0(K)'),
('display','upper','H^i(V,K[nE])=0; i=1,2,...'),
('text','upper','From the exact sequence'),
('diagram','upper-middle','H^i(V,O_V(-E_phi)[nE]) → H^i(V,O_V[nE]) → H^i(V,K[nE])'),
('text','middle','at n≥n_0(K), i=1,2,... we obtain:'),
('display','middle','dim H^i(V,O_V[nE]) ≤ dim H^i(V,O_V(-E_phi)[nE])'),
('text','middle','Since'),
('display','middle-lower','O_V(-E_phi) ≅ O_V[-E]'),
('text','middle-lower','then'),
('display','lower','O_V(-E_phi)[nE] ≅ O_V[-E][nE] ≅ O_V[(n-1)E]'),
('text','lower','Therefore, at n≥n_0(K), i=1,2,...'),
('display','lower','dim H^i(V,O_V[nE]) ≤ dim H^i(V,O_V[[n-1]E])'),
('text','bottom of text','Evidently, there exists such n\''),
('margin note','bottom left','187')
], sheet_kind='reused_typed', observations='Whole and both halves read; top-line sign and the two lower formulas additionally enlarged. The top-line sign resembles a small upright m, not the clearly typed ≥ used later: m is retained as the first doubtful reading. The last formula has inner square brackets [n-1], whereas the preceding isomorphism has parentheses (n-1); neither is normalized. The E in E_phi is plain here, unlike some later-numbered pages of this typescript. The typed page number is 70 and the pencil number at the bottom is 187.')
