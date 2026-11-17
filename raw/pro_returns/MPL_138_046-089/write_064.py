from workflow import save_page
save_page(64,r'''
\scanpage{64}
% archive foliation: 63
\diagram{\begin{tikzcd}[row sep=large,column sep=small]
&& E^+ \arrow[dddll,"p_{20}^+"'] \arrow[d,dashed,"p_{12}^+"'] \arrow[dddrr,"p_{01}^+"] \arrow[ddl,dashed,"\pi_2^+"'] \arrow[ddr,dashed,"\pi_1^+"] \arrow[ddd,"\pi_0^+",near end] && \\
&& D_{12} \arrow[dl,"\varphi_{21}"'] \arrow[dr,"\varphi_{12}"] && \\
& S_2 && S_1 & \\
D_{20} \arrow[ur,"\varphi_{20}"] \arrow[rr,"\varphi_{02}"'] && S_0 && D_{01} \arrow[ul,"\varphi_{10}"'] \arrow[ll,"\varphi_{01}"] \\
&& E^- \arrow[ull,"p_{20}^-"'] \arrow[uuu,dashed,"p_{12}^-",near start] \arrow[urr,"p_{01}^-"] \arrow[uul,dashed,"\pi_2^-"'] \arrow[uur,dashed,"\pi_1^-"] \arrow[u,"\pi_0^-"'] &&
\end{tikzcd}}
\margin{\deleted{$\unsure{\pi_1^+}$}}
% Pale, unlabelled construction strokes lie behind the inked diagram.
\[
\left\{\begin{aligned}
\rho_0^+&=(p_{01}^+)^{-1}p_{01}^-(p_{20}^-)^{-1}p_{20}^+\\
\rho_{\unsure{1|0}}^+&=(p_{12}^+)^{-1}p_{12}^-(p_{01}^-)^{-1}p_{01}^+\\
\rho_2^+&=(p_{20}^+)^{-1}p_{20}^-(p_{12}^-)^{-1}p_{12}^+
\end{aligned}\right.
\qquad \rho_2^+\rho_1^+\rho_0^+=\operatorname{id}_{E^+}
\]
\[
\begin{aligned}
S_0&\simeq E^+/\rho_0^+\simeq E^-/\rho_0^-\\
S_1&\simeq E^+/\rho_1^+\simeq E^-/\rho_{\unsure{1|0}}^-\\
S_2&\simeq E^+/\rho_2^+\simeq E^-/\rho_2^-
\end{aligned}
\]
\[
\left\{\begin{aligned}
\rho_0^-&=(p_{01}^-)^{-1}p_{01}^+(p_{20}^+)^{-1}p_{20}^-\\
\rho_1^-&=(p_{12}^-)^{-1}p_{12}^+(p_{01}^+)^{-1}p_{01}^-\\
\rho_2^-&=(p_{20}^-)^{-1}p_{20}^+(p_{12}^+)^{-1}p_{12}^-
\end{aligned}\right.
\]
''',[
('diagram','left upper half','E plus,E minus,D_20,D_12,D_01,S_0,S_1,S_2; eighteen labelled arrows'),
('deletion','right edge of diagram near D_01','pi_1 plus'),
('display','top right','three definitions rho_i plus'),
('display','top far right','rho_2 plus rho_1 plus rho_0 plus = id_E plus'),
('display','upper right','S_i isom E plus/rho_i plus isom E minus/rho_i minus'),
('display','right middle','three definitions rho_i minus')])
