from save_page import save
text=r'''
\scanpage{31}
% archive foliation: 30
$J_0$ de $J$
\[
Y'_{J_0}=\coprod_{j\in J_0}\!{}_Y\,\unsure{Y'_{J_0}|Y'_j},
\]
et $Y'_J=\varinjlim Y'_{J_0}$, on aura $Y\longrightarrow Y'\in\underline W$. Donc il y aura quand $=$ surjectivité! Mais soient maintenant
\diagram{\begin{tikzcd}[column sep=large]
f,g:X\arrow[r,shift left=.5ex,"\unsure{f_0|f}"]\arrow[r,shift right=.5ex,"g"']&\deleted{Y'}\inserted{Y}
\end{tikzcd}}
qui \deleted{\unsure{deviennent}} sont tels que $\gamma(f_j)=\gamma(g_j)$ $\forall j\in J$, a-t-on $\gamma(f)=\gamma(g)$? Mais oui, par le $=$ argument --- condensé dans un

\margin{\uuline{bof!}}

\uline{Lemme} Soit $Y\xrightarrow{\alpha_j}Y'_j$ \deleted{de} une \unsure{famille} d'équivs. faibles, alors il existe $Y\xrightarrow{\alpha}Y'$ une équiv. faible \deleted{telle que} \inserted{$Y\lhook\joinrel\longrightarrow Y'$} (imm. ouverte ou fermée si on y tient) \deleted{telle que} des $\beta_j:Y'_j\longrightarrow Y'$ tels que $\beta_j\alpha_j=\alpha$.

\margin{\diagram{\begin{tikzcd}[column sep=large,row sep=large]
Y\arrow[r,hook,"\bar\alpha_j"]\arrow[dr,"\alpha"']&\overline{Y'_j}\arrow[r,shift left=.5ex,"i_j"]\arrow[d]&Y'_j\arrow[l,dashed,shift left=.5ex,"r_j"]\arrow[dl,dashed,"\beta_j"]\\
&Y'&
\arrow[from=1-1,to=2-2,phantom,"\mathrm{comm}"{pos=.55}]
\arrow[from=1-3,to=2-2,phantom,"\mathrm{comm}"'{pos=.6}]
\end{tikzcd}}
$r_ji_j=\mathrm{id}_{\overline{Y'_j}}$}

(De plus, si les $\alpha_j$ sont des imm. ouvertes, resp. fermées, on peut prendre pour $Y'$ la somme amalgamée des $Y'_j$.)

On est ramené à prouver ceci: Soient $f,g:X=\coprod X_j\longrightarrow Y$, tels que $f_j\sim g_j$ $\forall j\in J$, alors $\gamma(f)=\gamma(g)$. (Mais attention on n'aura pas $f\sim g$!) \uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}, ou plutôt un $Y'$, où $(Y\longrightarrow Y')\in\underline W$.
'''
elements=[
('text','top left','J_0 de J'),
('display','top right','Y prime_J0 = coproduct_Y'),
('text','upper','et Y prime_J = direct limit'),
('display','upper','Y → Y prime in W'),
('text','upper middle','Donc il y aura quand = surjectivité!'),
('diagram','upper middle','f,g:X ⇒ Y prime changed to Y'),
('deletion','in target','Y prime'),
('insertion','above target','Y'),
('deletion','following parallel arrows','deviennent'),
('display','middle','gamma(f_j)=gamma(g_j), for all j; gamma(f)=gamma(g)?'),
('text','middle','Mais oui, par le = argument'),
('margin note','left slanting','bof!'),
('text','middle lower','Lemme Soit Y → alpha_j Y prime_j'),
('deletion','after Y prime_j','de'),
('display','lower middle','Y → alpha Y prime'),
('deletion','after équiv. faible','telle que'),
('insertion','above first telle que','Y hook Y prime'),
('text','lower middle','imm. ouverte ou fermée si on y tient'),
('deletion','following parenthesis','telle que'),
('display','lower','beta_j:Y prime_j → Y prime; beta_j alpha_j = alpha'),
('diagram','left lower margin','Y hook barY prime_j → Y prime_j; Y prime'),
('margin note','right of marginal diagram','r_j i_j = id_barY prime_j'),
('text','lower','De plus, si les alpha_j sont des imm. ouvertes'),
('text','foot','On est ramené à prouver ceci'),
('display','foot','f,g:X=coproduct X_j → Y'),
('display','foot','f_j ~ g_j for all j implies gamma(f)=gamma(g)'),
('text','foot','Mais attention on n’aura pas f ~ g!'),
('text','bottom underlined','Il faut une condition du type Kan sur Y'),
('display','bottom right','Y → Y prime in W'),
]
save(31,text,'text',elements,'The page itself asserts surjectivity and proposes a common-target lemma, while the final added warning calls for a Kan-type condition. The first amalgamated-sum summand index, overwritten target in the parallel pair, and cancellation layers are doubtful. Quotient-map glyph gamma is retained pending notation audit. These are transcription observations only, not verification.')
