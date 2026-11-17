from workflow import save_page
tex=r'''\scanpage{32}
\margin{31}

Par ces identifications, on trouve une surface topologique \inserted{(\unsure{compacte sans bords})}, dans laquelle la réalisation topologique de $|\Gamma|$ de $\Gamma$ est canoniquement plongée. Les faces orientées de cette surface se réalisent comme les orbites sous l'opération $\rho_f$ sur l'ens \deleted{$\unsure{\vec A}$} $\operatorname{Rep}$ des couples $(\vec a,\omega)$, où $\vec a\in\vec A$, $\omega\in\underline\omega_s\overset{\mathrm{def}}=\underline\omega(\vec A_s)$, opération définie par
\[
\deleted{\rho_f(\vec a,\unsure{\omega})=}
\qquad\text{où }\boxed{\omega_t=\varphi_{\vec a}\omega_s\in\underline\omega(\unsure{A_s|A_t})}
\]
\[
\left\{\begin{aligned}
\rho_f(\vec a,\omega_s)&=(\vec b,\deleted{\unsure{\varphi_{\vec a}\omega_s}}\inserted{\omega_t})\\
\vec b&=\rho_{\omega_t}^{-1}(\deleted{\unsure{\sigma}}-\vec a)
\end{aligned}\right.
\qquad\begin{gathered}\text{et où }b\in\vec A_t\\(t=\operatorname{ex}(\vec a))\\\text{est donné par}\end{gathered}
\]
où $\rho_{\omega_t}$ est la permutation circulaire sur $\vec A_t$ définie par l'orientation $\omega_t$. C'est aussi l'opération de rotation autour des sommets de la carte duale $C^*$, définie par les faces en question.

Si on veut une description combinatoire complète de la carte $C$ définie par $(\Gamma,(\unsure{\pi_s})_{s\in S},(\varphi_{\vec a})_{\vec a\in\vec A})$, il faut expliciter les opérations $\sigma_0,\sigma_1,\sigma_2$ sur $\operatorname{Rep}C$, ens. des repères. On trouve
\margin{str. pol. sur $\vec A_s$}
\[
\left\{\begin{aligned}
\sigma_0(\vec a,\omega_s)&=(-\vec a,-\varphi_{\vec a}\omega_s)\\
\sigma_2(\vec a,\omega_s)&=(\vec a,-\omega_s)\\
\sigma_1(\vec a,\omega_s)&=(\deleted{\unsure{\vec a}}\rho_{\omega_s}(a),-\omega_s)
\end{aligned}\right.
\]
\figure{\begin{tikzpicture}[x=.8cm,y=.8cm,line cap=round]
\draw[gray] (0,0)--(-1.2,1)--(.1,2.2)--(1.25,1.3)--cycle;
\draw[gray] (-1.2,1)--(1.25,1.3) (-1.2,1)--(0,0);
\begin{scope}\clip(0,0)--(-1.2,1)--(.1,2.2)--(1.25,1.3)--cycle;\foreach\x in {-1.4,-1.15,...,1.2}{\draw[gray](\x,-.2)--({\x+.3},1.8);}\end{scope}
\draw[yellow!65!green,line width=2pt,->] (0,0)--(.1,2.25);\draw[yellow!65!green,line width=2pt,->] (0,-.05)--(-1.8,-.65);
\draw[green!40!black,line width=2pt,->] (-.55,-1.1)--(-1.2,.85);\draw[green!40!black,line width=1.3pt,->](1.25,1.3)--(-1.2,1);
\draw[green!40!black,thick,->](.25,-.05)arc(-65:100:.2);
\node[below]at(0,0){$s$};\node[above]at(.1,2.2){$t$};\node at(-.55,.72){$r$};\node at(-.35,1.6){$\sigma_0r$};\node at(.5,.9){$\sigma_2r$};\node at(-.7,.22){$\unsure{\sigma_1r}$};
\end{tikzpicture}}

Soit encore, en termes de repères $r$ des $\vec A_s$, en interprétant
\[
\operatorname{Rep}(C)\simeq\coprod_{s\in S}\underbrace{\operatorname{Rep}(\vec A_s)}_{\text{ens des drapeaux}}
\]
\margin{\deleted{\unsure{par le côté}} $\vec a$.}
\[
\left\{\begin{aligned}
\sigma_0(r)&=\deleted{\unsure{(\vec a,\omega)\text{ repère de l'arête}}}\ r',\quad\text{défini par }\left\{\begin{aligned}a_{r'}&=-\vec a\\\omega_{r'}&=-\varphi_{\vec a}\omega_r\end{aligned}\right.\\
\sigma_1(r)&=\widetilde\sigma_0(r)\\
\sigma_2(r)&=\widetilde\sigma_1(r)
\end{aligned}\right.
\]
où $\widetilde\sigma_0^s,\widetilde\sigma_1^s$ sont les opérations sur $\operatorname{Rep}(\vec A_s)$ habituelles, $\widetilde\sigma_i^s$ changeant le composant \inserted{du drapeau} de dimension $i$, pas l'autre.

En termes de ces opérations, on trouve
\[
\left\{\begin{aligned}
\rho_{\mathrm{som}}&=\sigma_2\sigma_{\unsure{1|4}}\deleted{\unsure{\xi}}=\widetilde\sigma_0^s\widetilde\sigma_1^s=\widetilde\rho^s\\
\rho_{\mathrm{face}}&=\sigma_1\sigma_0
\end{aligned}\right.
\]
\inserted{sur $\operatorname{Rep}_s=\operatorname{Rep}(\vec A_s)$}
\margin{opération de rotation \unsure{sur l'ens} des rep. d'un polygone comb.)}
Donc
\[
\rho_{\mathrm{som}}\rho_f=\sigma_2\sigma_0\overset{\mathrm{def}}=\sigma
\qquad\sigma(\vec a,\omega_s)=(-\vec a,\varphi_{\vec a}(\omega_s)).
\]
'''
e=[('text','left upper','Par ces identifications'),('insertion','left upper','compacte sans bords'),('display','left upper','|Gamma|'),('text','left middle','Les faces orientées; orbites'),('deletion','left middle','vector A before Rep'),('display','left middle','Rep; (vector a,omega); omega set'),('deletion','left middle lower','rho_f(vector a,omega)='),('display','left lower','omega_t=phi_a omega_s; rho_f; b=rho inverse(-a)'),('deletion','left lower formula','phi_a omega_s; sigma'),('insertion','left lower formula','omega_t'),('text','left lower','où b∈A_t; t=ex(a)'),('text','left bottom','permutation circulaire; carte duale C star'),('text','right upper','Si on veut une description combinatoire complète'),('display','right upper','Gamma,(pi_s),(phi_a)'),('margin note','right upper','str. pol. sur vector A_s'),('text','right upper middle','Il faut expliciter les opérations'),('display','right middle','sigma0, sigma2, sigma1 on (a,omega_s)'),('deletion','right middle formula','vector a before rho'),('drawing','centre gutter','four flags r, sigma0r, sigma1r, sigma2r; s,t'),('text','right middle','Soit encore, en termes de repères'),('display','right middle lower','Rep(C) ≃ coproduct Rep(A_s)'),('margin note','right middle lower','ens des drapeaux; par le côté vector a'),('display','right lower','sigma0(r)=r prime; sigma1=tilde sigma0; sigma2=tilde sigma1'),('deletion','right lower formula','abandoned expression for sigma0(r)'),('text','right lower','où tilde sigma0^s, tilde sigma1^s'),('insertion','right lower','du drapeau'),('text','right lower','En termes de ces opérations'),('display','right bottom','rho_som=sigma2 sigma1; rho_face=sigma1 sigma0'),('deletion','right bottom','xi after first product'),('insertion','right bottom','sur Rep_s=Rep(A_s)'),('margin note','right bottom','opération de rotation sur l’ens des rep.'),('display','right bottom','rho_som rho_f=sigma2 sigma0=def sigma; sigma(a,omega)')]
d=[('inserted first parenthesis','compacte sans bords','Very fast insertion above main line; several syllables compressed','low'),('left boxed formula','omega(A_s) / omega(A_t)','Last subscript appears s despite preceding t; left unrepaired','low'),('right defining tuple','pi_s','Rewritten initial glyph before subscript s','medium'),('first involution block','rho_omega_s(a)','Argument appears plain a rather than vector a; retained as seen','medium'),('cancelled sigma0(r) formula','(vector a,omega) repère de l’arête','Heavily inked-out entire expression; words and grouping tentative','low'),('bottom first product','sigma2 sigma1 / sigma2 sigma4','Final subscript has a cross stroke; do not decide from identity alone','low')]
obs='Faces described as orbits of explicit rho_f on oriented-edge/orientation pairs. Full flag-involution formulas sigma0/1/2 and identification Rep(C)=coproduct Rep(A_s); vertex/face rotations and transport involution sigma. Candidate exact combinatorial encoding to relate to later context after freeze. Several indices (A_s versus A_t; sigma1 versus sigma4-like glyph) require ink audit, not algebraic correction. Claims topological embedding and orbit description without detailed proof.'
save_page(32,tex,e,d,obs,sheet_kind='reused_typed')
