from record import save
save(11,r'''
\scanpage{11}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&H^{i-1}(R,F\arrow[dl]\arrow[dr]\arrow[dd]&\\
H^{n-i}(P,F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee\simeq H_!^i(\mathring P,F)\arrow[dr]&&H_!^i(\mathring Q,F)\simeq H^{n-i}(Q,F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee\arrow[dl,very thick]\\
&H^i(W,F)\arrow[dl,very thick]\arrow[dr,very thick]&\\
H^i(P,F)\arrow[dr]&&H^i(Q,F)\arrow[dl]\\
&H^i(R,F)&
\end{tikzcd}}
\margin{\diagram{\boxed{\begin{tikzcd}[row sep=large,column sep=large]
{}\arrow[dr,leftrightarrow,"\begin{gathered}\text{suite exacte}\\\text{de coh. à supports}\\\deleted{\unsure{ordinaires}}\ \text{pour }P\subset W\end{gathered}","\begin{gathered}\text{suite exacte}\\\text{de cohomologie ! pour}\\Q\subset W\end{gathered}"']&\\
&{}
\end{tikzcd}}}}
\diagram{\boxed{\begin{tikzcd}[column sep=large,row sep=small]
S_!(W,R)&\text{duale de}&S(W,R)\arrow[d]\\
S(W,\unsure{P})\arrow[u]\arrow[d,phantom,"\simeq"{rotate=90}]&\text{duale de}&S(W,Q)\arrow[d,phantom,"\simeq"{rotate=90}]\\
S_!(W,Q)&\text{duale de}&S_!(W,P)\arrow[d]\\
S(W,R)\arrow[u]\arrow[d,phantom,"\simeq"{rotate=90}]&\text{duale de}&S_!(W,R)\arrow[d,phantom,"="{rotate=90}]\\
MV(W;P,Q)&&MV_!(W,R)
\end{tikzcd}}}
\margin{\deleted{1° Suite exacte de Mayer Vietoris $P,Q,P\cap Q=\unsure{S\times T|R=T},W$}

\deleted{2° Suite exacte de coh. relative}
\diagram{\begin{tikzcd}[row sep=small]
\deleted{H_Q^i(W)}\arrow[r,"{\deleted{\longrightarrow}}" description,draw=none]\arrow[d,phantom,"{\deleted{\simeq\ ?}}"{rotate=90}]&\deleted{H^i(W)}\arrow[r,"{\deleted{\longrightarrow}}" description,draw=none]&\deleted{H^i(W-Q)}\arrow[d,phantom,"{\deleted{\simeq}}"{rotate=90}]\\
\deleted{H_!^i(W-P)}\arrow[d,phantom,"{\deleted{=}}"{rotate=90}]&&\deleted{H^i(P)}\\
\deleted{H_!^i(Q-\partial Q)}\arrow[d,phantom,"{\deleted{\simeq}}"{rotate=90}]\\
\deleted{(H^{\unsure{n-i}}(Q,\partial Q))^\vee}\arrow[d,phantom,"{\deleted{=}}"{rotate=90}]\\
\deleted{H^{n-i}(Q)^\vee}
\end{tikzcd}}
\[\deleted{H_Q^i(W)\times H^{\unsure{n-i}}(Q\unsure{+|,}}\]}

\uline{Récapitulation}
\diagram{\boxed{\begin{tikzcd}[column sep=small]
&\Psi\arrow[dl]\arrow[dr]&\\
\Phi\arrow[dr]&&\Phi'\arrow[dl]\\
&\Psi'&
\end{tikzcd}}}
\diagram{\boxed{\begin{array}{rll}
\Psi:&H(P),H(Q),H(T),H(W)\\
\Psi':&\unsure{H}\mathbin{-}\text{duals}\mathbin{-}\\
\Phi:&H(P)^\vee,H(Q),H(W)&\deleted{(\text{pas de }H(T))}\\
\Phi':&H(P),H(Q)^\vee,H(W)&(\text{pas de }H(T))
\end{array}}}
\[
\left.\begin{aligned}
\Phi&\simeq S(W,P)\simeq S_!(W,Q)\\
\Phi'&\simeq S(W,Q)\simeq S_!(W,P)
\end{aligned}\right\}\ (\Phi,\Phi'\text{ duals})
\]
\[
\left.\begin{aligned}
\Psi&\simeq S(W,T)\simeq MV(W;P,Q)\\
\Psi'&\simeq S_!(W,T)\simeq MV_!(W,P,Q)
\end{aligned}\right\}\ (\Psi,\Psi'\text{ duals})
\]
\mspage{10}
''',[
('diagram','upper left','cohomology diamond from H^(i-1)(R,F) to H^i(R,F)'),('margin note','centre beside diamond','two exact-sequence captions with double arrow'),('diagram','centre','cohomology with supports P and cohomologie ! Q'),('deletion','centre caption','ordinaires'),('diagram','lower left boxed','S_!(W,R),S(W,P),S(W,R) and dual sequences'),('margin note','right rotated block','cancelled Mayer Vietoris and relative sequence'),('deletion','right rotated top','1° Suite exacte de Mayer Vietoris'),('deletion','right rotated','2° Suite exacte de coh. relative'),('diagram','right rotated','H_Q^i(W) and questionable H_!^i(W-P) identification'),('display','right rotated foot','cancelled H_Q^i(W) times H^(n-i)(Q'),('text','right middle','Récapitulation'),('diagram','right middle left','Psi Phi Phi prime Psi prime'),('diagram','right middle right table','cohomology terms for Psi Psi prime Phi Phi prime'),('deletion','right table Phi row','pas de H(T)'),('display','right lower','Phi and Phi prime sequence identifications duals'),('display','right bottom','Psi and Psi prime sequence identifications duals'),('text','bottom','10')],
[('top diamond first expression','H^(i-1)(R,F','Closing parenthesis not visibly written; left incomplete.','medium'),('central circled caption cancelled word','ordinaires','Dense overwriting before pour P subset W.','low'),('left boxed second row','P','Last letter overwritten; P preferred.','medium'),('right rotated 1°','S times T','R=T; cancellation line intersects the letters.','low'),('right rotated last line','H_Q^i(W) times H^(n-i)(Q plus/comma','Unfinished formula; trailing stroke crosses boundary of cancellation.','low'),('recapitulation Psi prime row','H - duals -','Initial repeated/ditto-like sign overwritten.','low'),('recapitulation Phi parenthesis','deleted pas de H(T)','A long crossing stroke traverses it; whether inherited from the older rotated cancellation is uncertain.','low'),('orientation sign','calligraphic T / tau','Consistent provisional reading with scans007 and009.','medium')],
['Cancelled rotated block explicitly questions H_Q^i(W) isomorphic H_!^i(W-P), with a ? beside the isomorphism.','Récapitulation identifies Phi/Phi prime and Psi/Psi prime as dual pairs; proof/sign compatibility implicit in diagrams.','One lower-left MV_! expression reads MV_!(W,R) while recap writes MV_!(W,P,Q); retain as written.'])
