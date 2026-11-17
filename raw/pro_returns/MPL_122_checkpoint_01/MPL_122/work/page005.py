from record import save
save(5,r'''
\scanpage{5}
\deleted{De plus, l'inclusion $(P,\widetilde{\partial P})\subset(P,\partial P)$ induit un hom de suites exactes}
\diagram{\begin{tikzcd}[column sep=small]
{}\arrow[r]&\deleted{H_!^i(P-\widetilde{\partial P})}\arrow[r]\arrow[d]&\deleted{H^i(P)}\arrow[r]\arrow[d,phantom,"{\deleted{=}}"{rotate=90}]&\deleted{H^i(\widetilde{\partial P})}\arrow[r]\arrow[d,"{\deleted{\simeq}}"]&\deleted{\cdots}\\
{}\arrow[r,dash]&\deleted{H_!^i(P-\partial P)}\arrow[r]&\deleted{H^i(P)}\arrow[r]&\deleted{H^i(\partial P)}\arrow[r]&\deleted{\cdots}
\end{tikzcd}}
\deleted{donc le lemme des cinq donne}
\[
\deleted{H_!^i(P-\widetilde{\partial P})\simeq H^i(P-\partial P)}
\]
\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&\partial P'\arrow[d,hook]\\
&\widetilde{\partial P}-\partial P\unsure{\simeq}\arrow[dl,hook]\arrow[dr,hook]\\
\widetilde{\partial P}&&\widetilde{\partial P}-\partial P-\partial P'\arrow[dl,hook]\\
&\widetilde{\partial P}-\partial P'\arrow[ul,hook]\arrow[d,phantom,"{\unsure{=P-P'}}"]\\
&\partial P\arrow[u,hook]
\end{tikzcd}}}
\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&P-P'=\widetilde{\partial P}-\partial P'\arrow[d,hook]\\
\partial P\arrow[ur,hook]\arrow[r,hook]&\widetilde{\partial P}&\partial P'\arrow[l,hook]\arrow[dl,hook]\\
&\widetilde{\partial P}-\partial P\arrow[u,hook]
\end{tikzcd}}
équivalences \unsure{d'}}
\diagram{\begin{tikzcd}[column sep=small]
{}\arrow[r]&H^i_{\unsure{P'}}(P,F)\arrow[r]\arrow[d]&H^i(P,F)\arrow[r,dash]\arrow[d,Rightarrow]&H^{\unsure{i}}(P-P',F)\arrow[r]\arrow[d,leftrightarrow,"\simeq"]&\cdots\\
{}\arrow[r]&H^i(P/\partial P;F)\arrow[r]&H^i(P,F)\arrow[r]&\begin{gathered}\deleted{H^i(\unsure{\partial P})}\\H^i(\partial P,F)\end{gathered}\arrow[r]&{}
\end{tikzcd}}
\margin{\diagram{\left\{\begin{tikzcd}[row sep=small]
(P,P-P')\\
(P,\partial P)\arrow[u]
\end{tikzcd}\right.}}
En somme
\[
H^i_{P'}(P,F)\simeq H^i(P\mathbin{\mathrm{mod}}\partial P,F)\simeq H_!^i(\mathring P,F)
\]
En somme on a
\[
H^i_{P'}(P,F)\xrightarrow{\simeq}H^i_{\unsure{?}}(\unsure{P'|\mathring P'},\deleted{\unsure{\mathrm{mod}}}\partial P',F)\simeq H_!^i(\mathring P',F)
\]
grâce à l'inclusion $(P',\partial P')\longrightarrow(P,P-P')$.
\mspage{4}
''',[
('deletion','top','De plus l’inclusion (P,collar) subset (P,boundary)'),('diagram','upper cancelled block','two exact sequences for collar and boundary'),('deletion','upper middle','donc le lemme des cinq donne'),('display','upper middle cancelled block','H_!^i(P-collar) isomorphic H^i(P-boundary)'),('margin note','left upper middle','collar comparison diagram'),('diagram','left upper middle','partial P prime; collar minus boundaries'),('margin note','right upper middle','collar inclusions and équivalences d’'),('diagram','right upper middle','boundary into P-P prime into collar'),('diagram','middle','supported cohomology and relative cohomology exact sequences'),('deletion','middle diagram lower right','H^i(partial P)'),('margin note','right middle','map of pairs'),('diagram','right middle','(P,partial P) to (P,P-P prime)'),('text','lower middle','En somme'),('display','lower middle','H^i_P prime(P,F) isomorphic H^i(P mod boundary,F)'),('text','lower middle','En somme on a'),('display','lower','H^i_P prime(P,F) to H^i_?(P prime, boundary P prime,F)'),('deletion','lower display','mod'),('text','lower','grâce à l’inclusion'),('text','bottom left','4')],
[('cancelled display','H^i(P-partial P)','Right-hand H has no clear support subscript; retained without one.','medium'),('left marginal diagram','isomorphism sign after collar minus boundary; =P-P prime','Small partly crowded signs and their attachment.','low'),('right marginal caption','équivalences d’','Caption stops after the small final strokes; no completion supplied.','low'),('main diagram','support P prime; exponent i','Support overwritten; upper-right exponent partly overwritten.','medium'),('last display','H^i_?; P prime or interior P prime; deleted mod','Several superposed strokes; lower index may be a question mark.','low')],
['Upper collar/cohomology argument explicitly cancelled; replacement diagram below.','Last map of pairs and overwritten relative-cohomology expression require mathematical scrutiny, not editorial correction.'])
