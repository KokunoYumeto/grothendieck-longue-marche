from workflow import save_page
save_page(53,r'''
\scanpage{53}
% archive foliation: 52
\[
\Pi_n=\mu_n^3/\mu_n
\]
\[
0'\unsure{\leftrightarrow|\leftarrow}0'',\quad
1'\unsure{\leftrightarrow|\leftarrow}1'',\quad
\infty'\unsure{\leftrightarrow|\leftarrow}\infty''
\]
\diagram{\begin{tikzcd}[column sep=small]
0'\arrow[r,bend right=25,"{\unsure{\leftrightarrow|=}}" description]&1'
&1'&\infty'\arrow[l,bend left=25,"{\unsure{\leftrightarrow|=}}" description]&?
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&&&\deleted{\unsure{\widetilde X(p,q,r;n)}}
\arrow[dll,"\Pi_n"']
\arrow[dddll,"{\mu_p\times\mu_q\times\mu_r\times\Pi_n}" description]
\arrow[dd,leftrightarrow,"{\mu_p\times\mu_q\times\mu_r}"]
\arrow[dddddll,bend left=80,leftrightarrow,"{\mu_{2p}\times\mu_{2q}\times\mu_{2r}\times\Pi_n}"]&\\
&\widetilde X_2(p,q,r)=X_2(2p,2q,2r)\arrow[dd,"{\mu_p\times\mu_q\times\mu_r}"]&&&\\
X_2(p,q,r)\arrow[dddr,"{\mu_p\times\mu_q\times\mu_r}"']&&&\widetilde X_2(n)\arrow[dll,"\Pi_n"']\arrow[d,"\unsure{\mu_2}"]&\\
&X_2(2,2,2)=\widetilde X_2\arrow[dr,"\mu_2"]\arrow[dd,"\mu_2^3"']&&X_{4n}\arrow[dl,"\Pi_n"]&\\
&&X_4\arrow[dl,"\Pi_2"]\arrow[ddl,bend left=15,"\Pi_4"]&&{}\\
&X_2\arrow[d,"\Pi_2"']&&&\\
&X_1\arrow[uu rrr,bend right=40,dash,"\Pi_{2n}"']&&&
\end{tikzcd}}
\[
\deleted{\unsure{\mu_n\cdot1}}\qquad
\deleted{\unsure{\Pi_n=\mu_n^3/\mu_n}}
\]
\margin{si $p=q=r=1$, $n=2$
on trouve
\[
\mu_2\times\mu_2\times\mu_2\times\underbrace{\Pi_2}_{\mu_2^3/\mu_2}
\]}
\unsure{TSVP}
''',[
('display','top left','Pi_n=mu_n^3/mu_n'),
('display','top right first row','0 prime and 0 double prime; 1 prime; infini prime'),
('diagram','top right second row','0 prime,1 prime;1 prime,infini prime; question mark'),
('diagram','main diagram, upper source','X tilde(p,q,r;n); Pi_n; three mu factors'),
('deletion','top node of main diagram','X tilde(p,q,r;n)'),
('diagram','main diagram, upper left node','X tilde_2(p,q,r)=X_2(2p,2q,2r)'),
('diagram','main diagram, far left node and arrow','X_2(p,q,r) -> X_2'),
('diagram','main diagram, centre and right square','X tilde_2(n), X tilde_2, X_4n, X_4'),
('diagram','main diagram, lower nodes and arrows','X_4, X_2, X_1; Pi_2, Pi_4'),
('diagram','main diagram, large outer curved arrows','mu_2p x mu_2q x mu_2r x Pi_n; Pi_2n'),
('deletion','lower centre, short crossed label','mu_n . 1'),
('deletion','lower centre, crossed formula on outer curve','Pi_n=mu_n^3/mu_n'),
('margin note','lower right','si p=q=r=1,n=2 on trouve; mu_2 x mu_2 x mu_2 x Pi_2'),
('text','bottom right','TSVP')])
