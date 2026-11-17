from record_page import record
tex=r'''\cotefile{137}
\scanpage{2}
% archive foliation: 1
\margin{\unsure{le même} \illegible{3}; \unsure{$k_\bullet$} \illegible{5}}

\uline{Lemme 1} Soit $L_\bullet$ un $k$-module \unsure{simplicial}.
Pour que $L_\bullet$ soit un \unsure{$k_\bullet$-module} projectif, il suffit
qu'il soit flasque (i.e. $\unsure{\pi_i}(L_\bullet)=0$ $\forall i\geq 0$), et que
les $L_n$ soient des $k$-modules projectifs.
\margin{\unsure{NB} \illegible{2} \unsure{$L_\bullet$} \illegible{3} \unsure{projectif}}

La \unsure{cond°} \illegible{1} \unsure{signifie aussi} que le complexe de
chaînes (de $k$-modules) associé par Dold-Puppe
est acyclique et à \unsure{composantes projectives}. On voit
alors qu'il est \inserted{\unsure{donc}} isomorphe à une somme directe
\unsure{de complexes de chaînes de la forme}
\[
\unsure{0\longrightarrow L\xrightarrow{\mathrm{id}}L\longrightarrow 0}.
\]
\unsure{On} \illegible{3} \unsure{tel}
\illegible{2} \unsure{correspond} \illegible{4}
\unsure{complexe} \illegible{2} \unsure{projectif} \illegible{3}
\unsure{au} \illegible{3} (\illegible{3})
\illegible{5} \unsure{donc on} \illegible{3}.

\uline{NB} Il suffit \unsure{en fait} \illegible{2} \unsure{que}
$L_\bullet$ \unsure{vérifie} i.e. $\pi_i(L_\bullet)=0$ $\forall i>0$, \unsure{au lieu de}
$\pi_i(L_\bullet)=0$ pour $i\geq0$, et $\pi_0(L_\bullet)$ $k$-projectif.
(\unsure{On trouve les mêmes conclusions} \illegible{2}
\unsure{c. et s.}) En effet, dans l'argument précédent,
il faut de plus tenir compte du \unsure{som-}
\unsure{mande} qui est un module projectif
$L_0$ placé au degré $0$. Or il est \unsure{immédiat}
que c'est aussi un complexe de \unsure{$k_\bullet$-}
chaînes projectif.

\uline{Cor.} Les $\unsure{\Gamma^i\Phi_{\bullet k}}\otimes_k\unsure{\Lambda^j\Psi_{\bullet k}}$
\inserted{et $\unsure{\Lambda^i\Phi_{\bullet k}}\otimes\unsure{\Lambda^j\Psi_{\bullet k}}$},
(pour $i>0$) sont des
modules \unsure{simpliciaux} projectifs.
'''
record(2,tex,[
('margin note','top edge','le même; k'),
('text','upper, heading and lemma','Lemme 1 Soit L'),
('display','upper, inline condition','π_i(L)=0 ∀i≥0'),
('margin note','left upper vertical','NB'),
('text','upper-middle proof','La cond°'),
('insertion','above isomorphe','donc'),
('display','middle','0 → L → L → 0'),
('text','middle, faded proof continuation','On; tel; complexe'),
('text','below fold','NB Il suffit'),
('display','below fold, inline','π_i(L)=0 ∀i>0; π_0(L)'),
('text','lower-middle','On trouve; En effet'),
('text','lower','il faut de plus tenir compte'),
('text','bottom corollary','Cor. Les Γ'),
('insertion','bottom, above corollary','et Λ^i Φ ⊗ Λ^j Ψ')
],doubts=[
('top edge','le même; k_•','severely faded / partly clipped words','low'),
('lemma, lines 1–4','simplicial; k_•-module; π_i','subscripts and alphabet faint','low'),
('lemma condition','∀i≥0','∀i>0 (lower stroke faint; ≥ retained)','medium'),
('left margin','NB; L_•; projectif','most adjoining words unreadable','low'),
('proof, lines 5–14','cond°; signifie aussi; composantes projectives; chain complex','severe fading; individual in-place markers','low'),
('middle display','0 → L → L → 0','objects and arrow label faint; entire best reading marked','low'),
('NB, lines 15–19','en fait; vérifie; au lieu de; c. et s.','word endings physically faint','low'),
('bottom paragraph','som-mande; immédiat; k_•-chaînes','possible different first/last letters','low'),
('corollary','Γ^i Φ_{•k} ⊗_k Λ^j Ψ_{•k}; Λ^i Φ_{•k} ⊗ Λ^j Ψ_{•k}','capital letter shape, subscripts and exponents uncertain','low')
],notation=[
('simplicial lower dot',r'$L_\bullet$','scan 2; faint dot, do not replace by an index'),
('homotopy letter',r'$\pi_i$','scan 2; retained with doubt where faint'),
('powers of Γ and Λ',r'$\Gamma^i$, $\Lambda^j$','scan 2; provisional, compare later recurrence'),
('underlining',r'\uline{…}; \uuline{…}','single and double rules distinguished visually'),
('quotation marks',r"``…''",'only when paired double quotation marks are drawn; guillemets only if visible')
])
