from record import save_page
tex=r'''\scanpage{9}
% archive foliation: 8
\[
\left(\prod_{i\in I}A_i\right)^\wedge\qquad
A_1^\circ\times A_2^\circ\times\text{---}\times A_n^\circ\longrightarrow\mathrm{Ens}
\qquad A_1\times\cdots\times
\]
\[
\widehat A_1^\circ\times A_2^\vee\times A_3^\vee\times\widehat A_4^\circ\times A_5^\vee\times\cdots\times\widehat A_{n-1}^\circ\times A_n
\]
\deleted{
\[
\deleted{\unsure{A_n}}\quad\mathcal F(\unsure{\mathcal X}_1\times\text{---}\times\unsure{\mathcal X}_n)\deleted{\unsure{\simeq}}\quad
A_1^\circ\times\text{---}\times A_n^\circ\longrightarrow E
\]
\margin{$\unsure{A_n}$\quad\deleted{\unsure{\mathcal F}}}
\[
F\in\mathcal F(\mathcal X_1\times\text{---}\times\mathcal X_n)\qquad
F:A_1^\circ\times\text{---}\times A_n^\circ\longrightarrow\mathrm{Ens}
\]
\[
\widehat A_{\unsure{1}}^\circ\ \text{---}\times\widehat A_n^\circ\mathrel{\rule{.7cm}{.3pt}}\mathrm{Ens}
\]
\[
X_1\otimes X_2\simeq\mathrm{Hom}(X_1^\vee,X_2^\vee;\underline1)
\simeq\mathrm{Hom}(X_1^\vee,X_2)\simeq\mathrm{Hom}(X_2^\vee,X_1)
\]
\[
\begin{aligned}
\mathcal F(X_1,\unsure{\&|\times}X_2)
&\simeq\mathrm{Hom}^{!!}_{\deleted{\unsure{!}}}(\mathcal F(X_1)^\circ,\mathcal F(X_2)^\circ;\mathrm{Ens})
\simeq\mathrm{Hom}^{!}_{\unsure{!}}(\mathcal F(X_1)^\circ,\unsure{\mathcal F}(X_2))
\simeq\mathrm{Hom}^{!}_{\deleted{\unsure{!}}}(\mathcal F(X_2)^\circ,\mathcal F(X_1))\\
&\simeq\mathrm{Hom}_{!!}(\unsure{\mathcal F}(X_1)^\vee,\mathcal F(X_2)^\vee;\mathrm{Ens})
\simeq\mathrm{Hom}_!(\mathcal F(X_1)^\vee,\mathcal F(X_2))
\simeq\mathrm{Hom}_!(\mathcal F(X_2)^\vee,\mathcal F(X_1))\\
&\simeq\mathrm{Hom}(\mathcal F(X_1)^\circ,\mathcal F(X_2)^\vee;\mathrm{Ens})
\end{aligned}
\]
\[
X_I=\overset{\deleted{\unsure{\infty}}}{\prod_{i\in I}}X_j\qquad
X_I=X_{I^+}\times X_{I^-}\simeq\mathrm{Hom}
\]
\[
\mathcal F(\deleted{\unsure{\prod X_i}})\simeq\mathcal F(\prod
\]
\[
I=I^+\amalg I^-
\]
\[
\mathcal F_J\qquad\widehat X_J\qquad X_J^\vee{}_{\deleted{\unsure{J}}}
\]
\[
\mathcal F(X_J)\qquad\mathcal F(X_J^\vee)
\]
\[
I=\coprod_{j\in J}I_j\qquad J=J^+\amalg J^-
\]
\[
\begin{aligned}
\mathcal F(X_I)&\simeq\underline{\mathrm{Hom}}^{\textcircled{!}}_{\unsure{,}}\left(\prod_{j\in J}\mathcal F(X_{I_j})^\circ,\mathrm{Ens}\right)\\
&\simeq\underline{\mathrm{Hom}}_{\textcircled{!}}\left(\prod_{j\in J}\mathcal F(X_{I_j}^{\vee}),\mathrm{Ens}\right)
\end{aligned}
\]
\diagram{\begin{tikzcd}[row sep=large]
\simeq\underline{\mathrm{Hom}}^!_!\left(\prod_{j^-\in\unsure{J^-|J^+}}\mathcal F(X_{I_{j^-}})^\vee\times\prod_{j^+\in J^+}\mathcal F(X_{I_{\unsure{j^-|j^+}}})^\circ,\mathrm{Ens}\right)
\arrow[d,bend left=35,"\simeq"]\arrow[dd,bend left=60,"\simeq"]\\
\simeq\underline{\mathrm{Hom}}_!\left(\prod_{j^-\in\unsure{J^-|J^+}}\mathcal F(X_{I_{j^-}}),\prod_{j^+\in J^+}\mathcal F(X_{I_j})\right)\\
\simeq\mathrm{Hom}^!\left(\prod_{j^+\in\unsure{J^+}}\mathcal F(X_{I_j})^\circ,\prod_{j^-\in J^-}\mathcal F(X_{I_{j^-}}^\vee)\right)
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw(0,0)..controls(-.3,.2)and(-.3,.7)..(-.3,1.2)..controls(-.3,1.45)and(-.5,1.5)..(-.5,1.5)..controls(-.25,1.7)and(-.3,2)..(-.3,2.5)..controls(-.3,2.9)and(-.2,3)..(0,3);\draw(-.4,1.55)..controls(-.2,1.8)and(-.2,2.1)..(-.2,2.4);\draw(.6,2.25)--(.6,2.6);\end{tikzpicture}}
\diagram{\begin{tikzcd}[column sep=small]
X\arrow[r,shift left=1ex,no head,"f"]\arrow[r,shift right=1ex,"g"']&Y
\arrow[from=1-1,to=1-2,phantom,"\unsure{\Downarrow\mu}" description]
\end{tikzcd}}
\margin{$\deleted{\unsure A}$}
\deleted{\diagram{\begin{tikzcd}X\arrow[r]&Y\end{tikzcd}}}
\diagram{\begin{tikzcd}[column sep=small]
X^\vee\arrow[r,shift left=1ex,"f^\vee"]\arrow[r,shift right=1ex,"g^\vee"']&Y^\vee
\arrow[from=1-1,to=1-2,phantom,"\unsure{\Uparrow\mu^\vee}" description]
\end{tikzcd}}
\margin{$\deleted{\unsure A}$\quad$\deleted{\unsure A}$}
\figure{\begin{tikzpicture}\draw(-.5,-.2)--(-.3,.15);\draw[->](.7,-.35)--(.2,.35);\draw[->](.8,.45)--(.25,-.5);\end{tikzpicture}}
\[
\deleted{\unsure A}\quad\mathcal F(X^\vee)\ ?
\]
\diagram{\begin{tikzcd}
\mathrm{Top}(A)\arrow[r,"\varphi"]&X\arrow[r,"\psi"]&\mathrm{Top}(B)
\end{tikzcd}}
\diagram{\begin{tikzcd}A\arrow[r]&\unsure{\mathrm{Pt}}(X)\end{tikzcd}}
\[
\deleted{(A\times X)^\wedge\simeq\underline{\mathrm{Hom}}(}
\]
\[
\varphi_*^\vee(F),\quad F\in\mathcal F(\mathrm{Top}(A^\circ))=A^\vee
\]
\[
\psi^*(G),\quad G\in\mathrm{Ob}\,B^\vee
\]
}
'''
el=[('display','top left','(product A_i)^'),('display','top middle','A1° × A2° × — × An° → Ens'),('display','top right','A1 × ... ×'),('display','second row','Ahat1° × A2vee × A3vee × Ahat4° × A5vee × ...'),('deletion','upper through bottom','large diagonal cancellation over working draft'),('display','upper draft','F(X1 × — × Xn), A1° × — × An° → E'),('deletion','upper draft left and relation','A_n; equivalence sign'),('margin note','upper left','A_n; cancelled F'),('display','upper draft second','F ∈ F(X1 × — × Xn); F: A1° × — × An° → Ens'),('display','upper draft third','Ahat1° — × Ahatn° — Ens'),('display','middle','X1 ⊗ X2 ≃ Hom(X1vee,X2vee;1) ≃ Hom(X1vee,X2) ≃ Hom(X2vee,X1)'),('display','middle first Hom row','F(X1,& X2) ≃ Hom!! ≃ Hom! ≃ Hom!'),('deletion','middle first Hom row','lower exclamation marks'),('display','middle second Hom row','Hom_!! and Hom_! equivalences'),('display','middle third Hom row','Hom(F(X1)°,F(X2)vee;Ens)'),('display','middle left','X_I = product X_j; X_I = X_I+ × X_I− ≃ Hom'),('deletion','middle product','infinity-shaped sign'),('display','middle unfinished','F(product X_i) ≃ F(product'),('deletion','middle unfinished argument','product X_i'),('display','middle left below','I=I+ ∐ I−'),('display','lower left','F_J; Xhat_J; X_Jvee'),('deletion','lower left index','J'),('display','lower left next','F(X_J), F(X_Jvee)'),('display','lower upper','I=∐ I_j; J=J+ ∐ J−'),('display','lower first two Hom rows','F(X_I) ≃ Hom^(circled !) ≃ Hom_(circled !)'),('diagram','lower three mixed rows','Hom!_! → Hom_! and Hom^!'),('drawing','lower Hom rows left','brace and short vertical stroke'),('diagram','bottom left upper','X ⇒ Y; f,g,mu'),('deletion','bottom left','A; X→Y; A; A'),('diagram','bottom left lower','Xvee ⇒ Yvee; fvee,gvee,muvee'),('drawing','bottom left lowest','two crossing arrows and short slash'),('display','bottom left right','F(Xvee)?'),('diagram','bottom right','Top(A) → X → Top(B)'),('diagram','bottom right next','A → Pt(X)'),('deletion','bottom right unfinished','(A×X)^ ≃ Hom('),('display','bottom right penultimate','phivee_*(F), F ∈ F(Top(A°))=Avee'),('display','bottom right last','psi*(G), G∈Ob Bvee')]
save_page(115,9,tex,el,'cancelled_draft',doubts=[('upper script categories','mathcal X and mathcal F','ordinary X or a Gothic F','medium'),('first F(X1,X2) Hom row','ampersand-like sign before X2','cross product sign overwritten','low'),('first Hom row','upper and lower exclamation marks','cancelled lower signs not all legible','low'),('X_I product','index i∈I and factor X_j','j and i discrepancy retained','medium'),('lower mixed Hom products','J− / J+; I_j− / I_j+','several overwritten signs and inconsistent indices','low'),('bottom 2-cells','Downarrow mu, Uparrow muvee','tiny vertical marks','low'),('bottom Pt','Pt','Pf','medium'),('draft extent','large diagonal cancellations cover working body','top two rows precede strokes and retained live','medium')],notes='Cancelled working draft, with two uncancelled preliminary product lines. Generalises Hom equivalences to multi-index families, with overwritten plus/minus indices and several unfinished formulas. Bottom sketches concern dual 2-cells and Top(A)→X→Top(B), A→Pt(X). These are cancelled and must not be promoted to established claims. Script F and X distinguished from ordinary F and X where visible; weaker readings are marked.')
