from workflow import save_page
save_page(268,r'''
\scanpage{268}
\uline{Corollaire} 2.3 Supposons $\dim X_0\leq1$. Alors $X$ est projectif sur $Y$.
\margin{\figure{\begin{tikzpicture}\draw (0,1.1)--(.03,0);\end{tikzpicture}}}

\uline{Corollaire} 2.4. Soit $A$ comme dessus \inserted{et \uline{réduit}}, soit $Y=\operatorname{Spec}A$, $\widetilde Y=\operatorname{Spec}(\widehat A)$, $y$ ($\widetilde y$) le pt fermé de $A$. \inserted{Supposons $y$ singularité \uline{isolée}} Alors l'hom $\operatorname{Pic}(Y-y)\to\operatorname{Pic}(\widetilde Y-\widetilde y)$ est un \uline{\deleted{\unsure{mono}}\inserted{iso}morphisme}.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,2.1)--(.03,0);\draw (6.8,2.4)..controls(6.5,1.6)and(6.8,1.4)..(7.8,1.4)--(8.4,1.45)--(8.3,1.05);\draw (6.8,2.4)--(11.2,2.4)..controls(11.5,1.8)and(11.3,1.5)..(11,1.45)--(8.4,1.45);\end{tikzpicture}}

\deleted{Cet hom est injectif}

On peut supposer que les composantes irred. de $Y$ soient de dim $\geq2$. Alors, pour tt Module loc. libre $E'$ sur $Y'=Y-\{y\}$, $i_*(E')$ est coh (i.e. $i:Y'\unsure{-|\to}Y$ l'imm. can)

\margin{\unsure{dégager un énoncé plus général} valable si $A$ est \unsure{localisé d'un} \unsure{schéma}, \deleted{\unsure{excellent|noethérien}}}

En particulier, $i_*(\mathcal O_{Y'})$ est cohérent, donc correspond à une algèbre $A'$ finie sur $A$. \deleted{Rien ne change \unsure{à|si}} Cette dernière correspond à un $\unsure{Y_1|X_1}$ fini sur $\unsure{Y|X}$, réduit, tq que
\[
Y'_1=Y_1|Y'\to Y'\text{ soit un isom},
\]
[donc $\widetilde Y'_1=\deleted{\unsure{Y_1}}\inserted{\widetilde Y_1|\widetilde Y'}\to\widetilde Y'$ est \deleted{\unsure{tel que}} un isom], \deleted{et $\unsure{Y_1}\;\Gamma($} et
\[
\Gamma(Y_1)\to\Gamma(Y'_1)\text{ est un isom}.
\]
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (1.5,3.8)--(1.7,3.05)--(.45,3.1)..controls(.05,2.7)and(-.2,2.1)..(0,1.2)..controls(.3,.2)and(.5,-.4)..(.9,-.6);
\draw (1.5,3.8)..controls(1,3.6)and(.7,3.3)..(.45,3.1)--(.95,2.1);\draw (.45,3.1)--(-.1,1.9)--(.8,1.85);\draw (-.1,1.9)--(.12,2.3);
\end{tikzpicture}}}
Car nous revenons au cas où $\Gamma(Y_{\unsure{1}})\to\Gamma(Y')$ est un isom, i.e. à $\operatorname{prof}A\geq2$. Un raisonnement facile

\mspage{267}
''',[
('text','top','Corollaire 2.3'),('drawing','left of corollary 2.3','short vertical rule'),('text','upper middle','Corollaire 2.4'),('insertion','above comme dessus','et réduit'),('insertion','right callout before Alors','Supposons y singularité isolée'),('drawing','around upper callout and left margin','rounded contour with tail; vertical rule'),('display','middle','Pic(Y-y) → Pic(tilde Y-tilde y)'),('deletion','prefix of morphisme','mono'),('insertion','above prefix','iso'),('deletion','middle','Cet hom est injectif'),('text','middle','On peut supposer'),('display','within proof','Y′=Y-{y}, i_*(E′)'),('display','middle right','i:Y′-Y'),('margin note','left, diagonally','dégager un énoncé plus général'),('deletion','end of diagonal note','excellent / noethérien'),('text','lower middle','En particulier'),('display','within lower paragraph','i_*(O_Y′), A′'),('deletion','lower','Rien ne change à'),('text','lower','Cette dernière correspond'),('display','lower','Y′_1 = Y_1|Y′ → Y′'),('text','lower bracket','donc'),('display','lower bracket','tilde Y′_1 = tilde Y_1|tilde Y′ → tilde Y′'),('deletion','inside tilde equality','Y_1'),('insertion','above tilde equality','tilde Y_1|tilde Y′'),('deletion','lower bracket','tel que'),('deletion','after bracket','et Y_1 Gamma('),('display','lower','Gamma(Y_1) → Gamma(Y′_1)'),('drawing','left lower margin','long curved line with two angular flags'),('text','bottom','Car nous revenons'),('display','bottom','Gamma(Y_1) → Gamma(Y′); prof A ≥2'),('text','bottom left','267')
],doubts=[('Cor.2.4 revised prefix','mono → iso','old prefix overwritten heavily','medium'),('diagonal marginal note','dégager un énoncé plus général / valable si A est / localisé d’un / schéma','first and final lines compressed; canceled excellent/noethérien','low'),('immersion','plain dash','arrowhead not distinct','medium'),('canceled Rien ne change','à','si','medium'),('finite scheme labels','Y_1 and Y','X_1 and X underneath overwriting','medium'),('bracket tilde equality','canceled Y_1 replaced tilde Y_1|tilde Y′','old short term overwritten','low'),('canceled phrase before un isom','tel que','first word could be tq','low'),('canceled fragment after bracket','et Y_1 Gamma(','overwritten subscript','low'),('last Gamma domain','Y_1','1 overwritten / other subscript','medium')],observations='Cor2.3 dimension of special fibre ≤1 gives projectivity. Cor2.4 changes mono- to iso-morphism of punctured Pic under completion, with added reduced and isolated singularity assumptions. Proof cancels Cet hom est injectif, uses coherence of i_* of locally free modules and finite hull A′ to reduce to depth≥2. Margin asks a general formulation; its exact hypotheses are uncertain, do not assert them as a theorem. Continues after Un raisonnement facile.')
