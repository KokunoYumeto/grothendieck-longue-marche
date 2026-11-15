from record_page import save
save(18,6,'text',r'''
\diagram{\begin{tikzcd}[row sep=small,column sep=small]
&\pi\arrow[d,"u"']&&&\\
&G_{\unsure{\rho}}(\mathbf Q_p)&&&\\
&G(C)\arrow[d,dash,"\unsure{\alpha}"']&&&\\
1\arrow[r,dash]&G'(C)\arrow[r]\arrow[d,dash,"\unsure{\downarrow|\uparrow}"']&E\arrow[r]&\pi\arrow[r,dash]\arrow[l,bend right=35,"\sigma_1"']\arrow[l,bend left=35,"\sigma_2"]&1\\
&G'(\mathbf Q_p)&&&\\
&G_m(\mathbf Q_p)=\mathbf Q_p^*\arrow[u,hook,"j_2"']&&&\\
&\pi\arrow[u,"\chi"']&&&
\end{tikzcd}}

\deleted{\unsure{on}} $\alpha$ permet d'identifier une \unsure{certaine ext. de} $E$ de $\pi$ par $G'(C)$ avec une autre ext. de $\pi$ par $G(C)$

Le splitting $\sigma_2$ de la première est tel que $\sigma_2(\pi)$ commute à $G'(\mathbf Q_p)$ et a fortiori à $j_2\chi(\pi)$. On trouve donc
\[
\left\{\begin{array}{l}
\gamma\longmapsto\widetilde\sigma_2(\gamma)=\sigma_2(\gamma).j_2\chi(\gamma)\\
\pi\longrightarrow E
\end{array}\right.
\]
un autre splitting.
Le splitting $\sigma_1$ \deleted{de} la seconde commute à $G(\mathbf Q_p)$, et a fortiori à $u(\pi)$. On trouve donc
\[
\gamma\longmapsto\sigma_1(\gamma)u(\gamma)=\widetilde\sigma_1(\gamma)
\]

On écrit que $\widetilde\sigma_1(\gamma)=\widetilde\sigma_2(\gamma)$

i.e.
\[
\sigma_2(\gamma)j_2(\chi(\gamma))=\sigma_1(\gamma)u(\gamma)
\]
-- donc
\[
\underbrace{\sigma_1(\gamma)^{-1}\sigma_2(\gamma)}_{\varphi(\gamma)}
=\deleted{\unsure{j_2}}\underset{\substack{\rotatebox{90}{$\in$}\\G(\mathbf Q_p)}}{u(\gamma)}.
\underbrace{j_2(\chi(\gamma^{-1}))}_{\substack{\rotatebox{90}{$\in$}\\j_2(\mathbf Q_p^*)}}
\]
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.3,.02)--(.3,.18);\end{tikzpicture}}}

1\textsuperscript{o}) Sur $\operatorname{Ker}\chi$, on a $\varphi(\gamma)=u(\gamma)$. donc $u$ connu sur $\operatorname{Ker}\chi$

2\textsuperscript{o}) $\operatorname{Ker}u=\deleted{\chi(\gamma)}\{\gamma,\chi(\gamma)=1,\varphi(\gamma)=1\}$ connu. Soit $\Pi_1=\pi/\operatorname{Ker}u$. C'est un groupe analytique $p$-adique, et
\[
\Pi_1\xrightarrow{\chi_1}\mathbf Q_p^*\qquad\text{induit par }\unsure{\rho|p}
\]
\mspage{5}
''',[
('diagram','upper left','π, Gρ(Qp), G(C), 1—G′(C)→E→π—1; σ1,σ2,j2,χ'),
('text','upper right','α permet d’identifier'),
('text','right middle','Le splitting σ2 de la première'),
('display','right middle','γ maps to tilde σ2; π→E'),
('text','right lower','un autre splitting; Le splitting σ1'),
('display','right lower','γ maps to σ1(γ)u(γ)=tilde σ1(γ)'),
('text','left lower','On écrit que ... i.e.'),
('display','left lower','σ2(γ)j2(χ(γ))=σ1(γ)u(γ)'),
('text','left lower','– donc'),
('display','lower middle','underbraces φ(γ), G(Qp), j2(Qp*)'),
('drawing','left margin','small right-angled stroke'),
('text','bottom item 1°','Sur Kerχ ... u connu'),
('text','bottom item 2°','Ker u ... Π1=π/Ker u'),
('display','bottom right','Π1→Qp*, χ1'),
('text','bottom left','5')
], 'Landscape whole then left/right halves read; diagram and formulas enlarged. Gρ subscript and central vertical edge direction remain explicitly uncertain. Mirrored reverse-side print excluded.')
