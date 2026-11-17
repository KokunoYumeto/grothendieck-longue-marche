from workflow import save_page
save_page(60,r'''
\scanpage{60}
% archive foliation: 59
\deleted{
$C=(C_0,C_1)$ groupoïde connexe

$G=\operatorname{Aut}(C)$ gr. des automorphismes

$G^0$ ss gr. des $g\in G$ induisant l'identité sur $C_0$
\diagram{\begin{tikzcd}
1 \arrow[r] & G^0 \arrow[r] & G \arrow[r,"{\uuline{\text{Surj}}}"'] & \unsure{\mathfrak S|\mathcal S}_{C_0} \arrow[r] & 1
\end{tikzcd}}
[Pour qu'une autoéquivalence \inserted{$u$} soit un iso, il f et s. qu'elle soit \uline{bijective} sur les objets de $C$, et induise un iso. \deleted{sur les} $\operatorname{Aut}(x)\longrightarrow\operatorname{Aut}(ux)$ pour $\forall x\in C_0$ ; d'autre part, pour toute application $C_0\xrightarrow{u_0}C'_0$
}
\diagram{\begin{array}{ccccccccc}
1&-&\operatorname{Aut}^0(C)&-&\operatorname{Aut}C&-&\unsure{\mathfrak S|\mathcal S}_C&-&1
\end{array}}
\deleted{$\operatorname{Aut}^0(C)\simeq$}

On a
\diagram{\begin{tikzcd}[column sep=small]
1 \arrow[r,dash] & \operatorname{Aut}^0(C,a) \arrow[r,dash] & \operatorname{Aut}^0(C) \arrow[r] & \operatorname{Aut}(\underset{\substack{\Vert\\\operatorname{Aut}_C(a)}}{\pi_a}) \arrow[r] & 1
\end{tikzcd}}
\deleted{\unsure{À}} Pour déterminer \deleted{$\operatorname{Aut}^0(C,a)=$}
\[
\operatorname{Aut}^0(C,a)=\left\{f\in\operatorname{Aut}(C)\ \middle|\ \operatorname{Ob}f=\operatorname{id}\ .\ (f_a:\operatorname{Aut}(a)-\operatorname{Aut}(\underset{\substack{\Vert\\f(a)}}{a}))=\operatorname{id}\right\}
\]
On considère, pour $\forall x\in C_0$,
\[
T_x=\operatorname{Isom}(a,x),\qquad \pi_a\text{-torseur à droite}
\]
et son commutant \deleted{\unsure{G_x}} $\operatorname{Aut}(x)$
''',[
('deletion','upper half, long diagonal strokes','C=(C_0,C_1) through toute application C_0 to C_0 prime'),
('text','top','C=(C_0,C_1) groupoïde connexe; G; G^0'),
('diagram','upper middle','1 to G^0 to G to permutation group to 1; Surj'),
('text','middle, cancelled block','[Pour qu’une autoéquivalence soit un iso'),
('insertion','above autoéquivalence','u'),
('deletion','middle paragraph','sur les'),
('diagram','below cancelled block','1 - Aut^0(C) - Aut C - permutation group - 1'),
('deletion','below first live diagram','Aut^0(C) ≃'),
('text','lower middle','On a'),
('diagram','lower middle','1 - Aut^0(C,a) - Aut^0(C) to Aut(pi_a) to 1'),
('text','lower third','Pour déterminer'),
('deletion','before Pour','À'),
('deletion','right of Pour déterminer','Aut^0(C,a)='),
('display','lower third','Aut^0(C,a)={f in Aut(C) ...}'),
('text','bottom','On considère, pour tout x'),
('display','bottom','T_x=Isom(a,x), pi_a-torseur à droite'),
('text','last line','et son commutant Aut(x)'),
('deletion','last line before Aut(x)','G_x')],sheet_kind='cancelled_draft')
