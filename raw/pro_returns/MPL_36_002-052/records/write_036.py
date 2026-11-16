from save_page import save
tex=r'''
\scanpage{36}
\margin{Cohomologie discrète\quad $*$\unsure{[}}
\figure{\begin{tikzpicture}\draw (0,5.2) .. controls (-.25,5.2) and (-.15,3.2) .. (-.2,2.6) .. controls (-.22,2.35) and (-.38,2.3) .. (-.45,2.3) .. controls (-.05,2.3) and (-.15,.5) .. (0,0);\end{tikzpicture}}

\diagram{\begin{array}{l|l|l}
\begin{gathered}
H^0(X,\zeta_\ell)=\unsure{U_\ell|\mu_\ell}\\[1em]
\begin{aligned}
H^2(X,\mathbf Z/\ell)&=H^2(X,\zeta_\ell)\otimes_{\mathbf Z/\ell}\operatorname{Hom}(U_\ell,\mathbf Z/\ell)\\
&=\unsure{\mathbf Z_\ell|\mathbf Z/\ell}\otimes_{\mathbf Z/\ell}\operatorname{Hom}(U_\ell,\mathbf Z/\ell)\\
&\simeq\deleted{\unsure{\mathbf Z/\ell}}\operatorname{Hom}(U_\ell,\mathbf Z/\ell)
\end{aligned}
\end{gathered}
&
\begin{gathered}
H^1(X,\zeta_\ell)=P^{(\ell)}\quad\text{\unsure{Points} de la jacobienne}\\
\text{$P$ de $X$, annulés par $\ell$}\\[1em]
\begin{aligned}
H^1(X,\mathbf Z/\ell)&=H^1(X,\zeta_\ell)\otimes_{\mathbf Z/\ell}\operatorname{Hom}(\unsure{U_\ell},\mathbf Z/\ell)\\
&\deleted{=P^{(\ell)}\mathbin{\underset{\text{''}}{\otimes}}\operatorname{Hom}(\zeta_\ell,\unsure{H})}\\
&=P^{(\ell)}\otimes_{\mathbf Z/\ell}\operatorname{Hom}(\unsure{U_\ell},\mathbf Z/\ell)
\end{aligned}\\[1em]
\text{Or}\quad P^{(\ell)}\times P^{(\ell)}\longrightarrow U_\ell\quad\text{\unsure{en vertu}}\\
\boxed{\begin{gathered}\text{de l'autodualité de }P\ \unsure{\ldots}\\\text{et la dualité de Kummer-Serre}\end{gathered}}
\end{gathered}
&
\begin{gathered}H^2(X,\zeta_\ell)\simeq\mathbf Z/\ell\\[2em]H^0(X,\mathbf Z/\ell)\simeq\mathbf Z/\ell\end{gathered}
\\\hline
\begin{gathered}H^0(X,\zeta_p)=0\\[1.5em]H^2(X,\mathbf Z/p)\simeq H^2(X,\mathbf Z/p)=0\end{gathered}
&
\begin{gathered}
H^1(X,\zeta_p)=P^{(p)}:\ \text{\unsure{élts} d'ordre $p$}\\
\text{de la jacobienne}\\[1em]
H^1(X,\mathbf Z/p)\simeq\text{\unsure{Points} de }H^1(X,\underline{\mathrm O}_X)\text{ fixes}\\
\text{par }F\\
\boxed{\text{dualité de Serre - Cartier}}
\end{gathered}
&\begin{gathered}H^2(X,\zeta_p)\simeq\mathbf Z/p\\[2em]H^0(X,\mathbf Z/p)\simeq\mathbf Z/p\end{gathered}
\\\hline
H^0(X,\unsure{i_p|\alpha_p})=0
& H^1(X,\unsure{i_p})\simeq{}_{F}H^1(X,\underline{\mathrm O}_X)\deleted{\unsure{F}}
& H^2(X,\unsure{i_p})=H^1(X,\underline{\mathrm O}_X)_F
\end{array}}
\margin{35}
'''
e=[('margin note','vertical left beside first two table rows','Cohomologie discrète; star and bracket'),('drawing','left table rows 1-2','large brace'),('diagram','entire page upper two thirds','3-column 3-row cohomology comparison table'),('display','row 1 column 1 top','H^0(X,zeta_l)=U_l'),('display','row 1 column 1 lower','H^2(X,Z/l)=H^2(X,zeta_l) tensor Hom(U_l,Z/l)'),('deletion','row 1 column 1 final equality','Z/l'),('display','row 1 column 2 top','H^1(X,zeta_l)=P^(l)'),('text','row 1 column 2 top explanation','Points de la jacobienne P de X annulés par l'),('display','row 1 column 2 middle','H^1(X,Z/l)=H^1(X,zeta_l) tensor Hom(U_l,Z/l)'),('deletion','row 1 column 2 cancelled middle equality','P^(l) tensor Hom(zeta_l,H)'),('display','row 1 column 2 lower','P^(l) x P^(l) -> U_l'),('text','row 1 column 2 around pairing','Or ... en vertu'),('text','row 1 column 2 boxed','de l’autodualité de P ... et la dualité de Kummer-Serre'),('display','row 1 column 3 top','H^2(X,zeta_l) ~= Z/l'),('display','row 1 column 3 lower','H^0(X,Z/l) ~= Z/l'),('display','row 2 column 1 top','H^0(X,zeta_p)=0'),('display','row 2 column 1 lower','H^2(X,Z/p) ~= H^2(X,Z/p)=0'),('display','row 2 column 2 top','H^1(X,zeta_p)=P^(p)'),('text','row 2 column 2 explanation','élts d’ordre p de la jacobienne'),('display','row 2 column 2 middle','H^1(X,Z/p) ~= Points de H^1(X,O_X) fixes par F'),('text','row 2 column 2 boxed','dualité de Serre - Cartier'),('display','row 2 column 3 top','H^2(X,zeta_p) ~= Z/p'),('display','row 2 column 3 lower','H^0(X,Z/p) ~= Z/p'),('display','row 3 column 1','H^0(X,i_p)=0'),('display','row 3 column 2','H^1(X,i_p) ~= left F H^1(X,O_X)'),('deletion','row 3 column 2 right of cohomology','obliterated F-like superscript'),('display','row 3 column 3','H^2(X,i_p)=H^1(X,O_X)_F'),('margin note','bottom left','35')]
d=[{'line':'left margin lower mark','reading':'star and opening bracket','alternatives':'bracket-like stroke may be separate mark','confidence':'low'},{'line':'row 1 U everywhere','reading':'U_l','alternatives':'mu_l; same handform repeated in Hom arguments','confidence':'medium'},{'line':'row 1 first column second equality','reading':'Z_l','alternatives':'Z/l; slash not distinct','confidence':'low'},{'line':'row 1 second column explanation','reading':'Points','alternatives':'short initial word resembling Points; possibly abbreviation','confidence':'medium'},{'line':'row 1 second column deleted Hom argument','reading':'H','alternatives':'under cancellation only initial capital visible','confidence':'low'},{'line':'row 1 second column after pairing','reading':'en vertu','alternatives':'se déduit; very compressed strokes','confidence':'low'},{'line':'row 2 second column','reading':'élts','alternatives':'éléments contracted; retain short form','confidence':'medium'},{'line':'row 3 coefficient in all columns','reading':'i_p','alternatives':'alpha_p; first/last show dotted i-like letter, middle overwritten','confidence':'low'},{'line':'row 3 second column cancellation','reading':'F','alternatives':'solid ink blob; best symbolic conjecture only','confidence':'low'}]
save(36,tex,e,d,'Landscape cohomology table after the Picard cover. Three columns and three rows, with the first two rows bracketed as “Cohomologie discrète”; coefficient ink is zeta_l, zeta_p, then a dotted i-like p coefficient (not silently identified with alpha_p). Abelian/Jacobian l torsion paired via autoduality and Kummer–Serre, p row via Serre–Cartier, bottom row shows Frobenius kernel/cokernel on coherent H^1. Repeated H^2(X,Z/p) in left middle cell preserved. No hypotheses about X supplied here. Important unproved comparison claims, no proof. Pencil 35.')
