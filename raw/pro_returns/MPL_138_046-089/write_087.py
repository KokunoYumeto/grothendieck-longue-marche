from workflow import save_page
save_page(87,r'''\scanpage{87}
% archive foliation: 86
En fait on a ici, exceptionnellement
\[
\widetilde{\mathcal T}_2\simeq\unsure{\mathfrak S}_3\cdot\mathcal T_2
\]
(produit $\tfrac12$ direct pour action de $\mathfrak S_3$ sur $\mathcal T_2$)
\[
\Gamma\longrightarrow\deleted{\mathcal T_2}\ \widetilde{\mathcal T}_2
\overset{\varepsilon}{-}\mathfrak S_3\qquad\text{trivial}
\]
i.e. $\Gamma\longrightarrow\deleted{\unsure{\mathfrak S_3}}\ \unsure{\mathcal T_2|\widetilde{\mathcal T}_2}$, d'où
\[
\boxed{\Gamma\longrightarrow\mathcal T_2^{\mathfrak S_3}}
\]
On aurait envie de définir un
iso can. $\mathcal T_2^!\simeq\mathcal T_2^{\mathfrak S_3}$
\margin{?}
et des iso can
\[
\mathcal T_2^!\simeq\mathcal T_\nu^!
\]
Pour ceci, on va généraliser d'
''',[
('text','top','En fait on a ici, exceptionnellement'),
('display','upper','Ttilde₂≃S₃·T₂'),
('text','upper-middle','produit 1/2 direct pour action'),
('display','middle','Γ→Ttilde₂−εS₃ trivial'),
('deletion','middle before Ttilde₂','T₂'),
('text','middle','i.e. Γ→T₂, d’où'),
('deletion','middle after arrow','S₃'),
('display','middle boxed','Γ→T₂^{S₃}'),
('text','lower-middle','On aurait envie de définir un iso can.'),
('display','lower-middle inline','T₂!≃T₂^{S₃}'),
('margin note','left beside two conjectural isomorphisms','?'),
('text','lower-middle','et des iso can'),
('display','lower','T₂!≃T_ν!'),
('text','last written line','Pour ceci, on va généraliser d’')])
