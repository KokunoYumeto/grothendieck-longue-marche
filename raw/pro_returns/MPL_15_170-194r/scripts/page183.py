from record_page import record

record(183, r'''\scanpage{183}

Soit $\mathcal M$ une catégorie de motifs \unsure{géomologiques|géométriques}, \inserted{de type fini,} sur le préschéma $S$ de type fini sur $\mathbb Z$. Pour simplifier, supposons que les degrés de $\mathcal M$ soient pairs (sinon, il sera possible, pour \deleted{\unsure{la plupart des}} \inserted{certaines} questions de distribution de Frobenius, de remplacer $\mathcal M$ par $\mathcal M^{\unsure{\mathrm{pairs}|\mathrm{pair}}}$). Tout choix d'un pt fermé $s\in S$ permet \unsure{donc}, de définir des (\unsure{à iso bien déf.}) ``$\mathbb R$-points motiviques'' \deleted{\unsure{de $\mathcal M$}''}\inserted{de $\mathcal M$}.

Pour fixer les idées, choisissons un pt $\mathbb R$-motivique de $\mathcal M$, d'où un gpe algébrique $G_{\mathbb R}$ sur $\mathbb R$.

Il y a lieu de \deleted{\uline{\unsure{dédoubler}}} \inserted{démultiplier} les points \inserted{fermés $s$} de $S$, en prenant les couples $s':(s,i)$, où $s\in S^0$, et
\margin{\unsure{l'exposant} $^0$ désigne \unsure{les} pts \uline{fermés}}
$i:\unsure{G_{m\mathbb C}-G^{(s)}_{\mathbb C}|G_{m\mathbb C}\to G^{(s)}_{\mathbb C}}$ est de type \deleted{\unsure{donné}} préférentiel -- $G(s)$ désigne le gpe de Galois motivique associé à $\mathcal M_s$.

\deleted{Alors} Soit $S'$ l'ens de ces couples. À tout $s'\in S'$ est associé un $\mathbb R$-point motivique de $\mathcal M$, \deleted{d'où un} déterminé à isom près, d'où un
\[
\unsure{\xi|\zeta}(s')\in H^1(\mathbb R,\unsure{G^{00}_{\mathbb R}}),
\]
où $G^{\unsure{00}}$ est le noyau de
\diagram{\[
\begin{tikzcd}
G^0_{\mathbb R} \arrow[r,"\varepsilon"] & G_m .
\end{tikzcd}
\]}
De plus, si $G^{\unsure{\xi}(s')}_{\mathbb R}$ est ``le'' gpe déduit de $G_{\mathbb R}$ par torsion par $\unsure{\xi}(s')$, on obtient un hom
\diagram{\[
\begin{tikzcd}[column sep=large]
u(s'):\ G(s')_{\deleted{\unsure{\mathbb R}}\mathbb R}=G(s)_{\mathbb R} \arrow[r] & G^{\unsure{\xi}(s')}_{\mathbb R}
\end{tikzcd}
\]}
compatible aux $\varepsilon_{\mathbb R},\unsure{J_{\mathbb R}|j_{\mathbb R}}$, et déterminé en fait mod \deleted{automorphisme intérieur} \inserted{conjugaison} par un élément de $G^{\unsure{00}}_{\mathbb R}(\mathbb R)$.

\margin{182}
''', [
('text','opening paragraph','Soit M une catégorie de motifs'),
('insertion','above line 1','de type fini'),
('deletion','after pour line 4','la plupart des'),
('insertion','above deletion line 4','certaines'),
('text','after parenthesis','Tout choix d’un pt fermé'),
('deletion','after R-points motiviques','de M and old closing quotation marks'),
('insertion','above same deletion','de M'),
('text','second paragraph','Pour fixer les idées'),
('text','third paragraph','Il y a lieu de'),
('deletion','third paragraph after de','dédoubler'),
('insertion','above deletion','démultiplier'),
('insertion','after points','fermés s'),
('margin note','left opposite S0','l’exposant 0 désigne les pts fermés'),
('text','third paragraph continuation','i : GmC - G(s)C'),
('deletion','before préférentiel','donné'),
('deletion','start of fourth paragraph','Alors'),
('text','fourth paragraph','Soit S’ l’ens de ces couples'),
('deletion','after R-point motivique de M','d’où un'),
('display','cohomology class','ξ(s’) ∈ H1(R,G00R)'),
('text','before kernel map','où G00 est le noyau de'),
('diagram','kernel map','G0R → Gm with ε'),
('text','twisting paragraph','De plus, si Gξ(s’)R'),
('diagram','last display','u(s’): G(s’)R = G(s)R → Gξ(s’)R'),
('deletion','subscript in last display','R overwritten'),
('text','closing lines','compatible aux εR, JR'),
('deletion','closing line after mod','automorphisme intérieur'),
('insertion','above closing deletion','conjugaison'),
('margin note','bottom left pencil','182')
], sheet_kind='reused_typed', observations='''Whole image and both halves inspected, followed by enlarged crops across all handwritten text. Blue reversed print is show-through from a reused typed sheet; it is not treated as a second live text on this side. The word qualifying motifs at the opening is low-confidence and has not been normalized. Several indices and Greek letters are retraced; ξ/ζ, G00, and J/j are explicitly marked for the cross-page notation audit. The preferred-type map has no clearly visible arrowhead, so a dash is the first reading. The superscript in M^pairs is not silently changed to pur. The marginal note explains the superscript 0 used for closed points. The cancelled subscript at G(s’) is retained even though overwritten.''')
