from save_page import save
tex=r'''
\scanpage{45}
D'après le théor. d'Artin--Schreier--Witt, on a
\[
H^1(A,\mathbb Z/p)\simeq H^1(A,\underline O_A)^{\unsure{(\varphi)|(p)}}_{\deleted{\unsure{\varphi}}}
\]
éléments de $H^1(A,\underline O_A)$ tels que
\[Fx=x\]
\[
H^1(A,\mathbb Z/p^n)\simeq H^1(\unsure{A},\underline O_A(W_n))^{\unsure{(\varphi)|(p)}}
\]
--- $H^1(A,\underline O_A(W_n))$ tels que
\[Fx=x\]
\[
\boxed{\operatorname{Hom}(\pi_1^p(A),\mathbb Z_p)\simeq H^1(A,\deleted{\unsure{\mathbb Q_p}}\mathbb Z_p)
\simeq H^1(A,\unsure{\mathbb W|W})^{(\varphi)}_{\deleted{\unsure{\varphi}}}}
\]
\inserted{d'où} \deleted{\unsure{on a}} on déduit un \deleted{accouplement} isomorphisme
\[
\boxed{\deleted{\pi_1^p(A)\times H^1(A,\mathbb W)_s\longrightarrow\mathbb Z_p}}
\]
\[
\boxed{\deleted{\operatorname{Hom}_{\mathrm{cont}}(\pi_1^p(A),\Lambda)\simeq H^1(A,\mathbb W)_s}}
\]
qui est une dualité \deleted{\unsure{de}} de $\mathbb Z_p$-modules libres de type fini

D'autre part, utilisant encore le fait que tout revêtement de $A$ est une variété abélienne, on trouve aussi
\[\boxed{\pi_1^p(A)\simeq T_p(A)}\]
d'où en les composant
\[\boxed{T_p(A)\times H^1(A,\mathbb W)^{(\varphi)}\longrightarrow\mathbb Z_p}\]
qui est une dualité de $\mathbb Z_p$-modules libres de type fini.

\deleted{qu'on peut aussi écrire} d'où on déduit
\[
\boxed{\operatorname{Hom}_{\mathrm{cont}}(T_p(A),\deleted{\unsure{\Lambda}}W_\infty(k))\simeq H^1(A,\mathbb W)_s}
\]
\margin{44}
'''
e=[('text','top','D’après le théor. d’Artin–Schreier–Witt'),('display','first formula','H¹(A,Z/p) ≃ H¹(A,O_A)^(φ)'),('deletion','first formula subscript','φ'),('text','right of first formula','éléments de H¹(A,O_A) tels que'),('display','right upper','Fx=x'),('display','second formula','H¹(A,Z/pⁿ) ≃ H¹(A,O_A(W_n))'),('text','right of second formula','— H¹(A,O_A(W_n)) tels que'),('display','right below','Fx=x'),('display','first long box','Hom(π₁ᵖ(A),Z_p) ≃ H¹(A,Z_p) ≃ H¹(A,W)^(φ)'),('deletion','inside first long box','Q_p; φ subscript'),('text','between first and second boxes','d’où on déduit un isomorphisme'),('insertion','above deleted opening','d’où'),('deletion','between boxes','on a; accouplement'),('display','second box','π₁ᵖ(A)×H¹(A,W)_s→Z_p'),('deletion','whole second box','π₁ᵖ(A)×H¹(A,W)_s→Z_p'),('display','third box','Hom_cont(π₁ᵖ(A),Λ)≃H¹(A,W)_s'),('deletion','whole third box','Hom_cont(π₁ᵖ(A),Λ)≃H¹(A,W)_s'),('text','right of cancelled boxes','qui est une dualité de Z_p-modules'),('deletion','after dualité','de'),('text','middle paragraph','D’autre part, utilisant encore le fait'),('display','middle lower small box','π₁ᵖ(A) ≃ T_p(A)'),('text','right of small box','d’où en les composant'),('display','penultimate box','T_p(A)×H¹(A,W)^(φ)→Z_p'),('text','right of pairing','qui est une dualité de Z_p-modules'),('deletion','above last box','qu’on peut aussi écrire'),('text','above last box continuation','d’où on déduit'),('display','last box','Hom_cont(T_p(A),W_∞(k))≃H¹(A,W)_s'),('deletion','inside last box before W','Λ'),('margin note','bottom left','44')]
d=[{'line':'first two Frobenius-fixed cohomology expressions','reading':'(φ)','alternatives':'(p); use of the looped sign only becomes clearer in later displays','confidence':'medium'},{'line':'second formula, first argument','reading':'A','alternatives':'overwritten letter','confidence':'medium'},{'line':'first large box cancelled coefficient','reading':'Q_p','alternatives':'heavy crosshatching makes the first letter uncertain','confidence':'low'},{'line':'Witt coefficient alphabet','reading':'blackboard W in H¹(A,W), plain W_n / W_∞(k)','alternatives':'doubling may be cursive retracing','confidence':'medium'},{'line':'opening of sentence under first box','reading':'d’où inserted over deleted on a','alternatives':'short overwritten opening uncertain','confidence':'low'},{'line':'last box crossed coefficient','reading':'Λ','alternatives':'dense crossed character','confidence':'low'}]
save(45,tex,e,d,'Artin–Schreier–Witt comparison is explicitly invoked. The first pairing involving H¹(A,W)_s and the Hom_cont(π₁ᵖ(A),Λ) formula are struck out, while the later pairing uses Frobenius-fixed H¹(A,W)^(φ) and the final Hom uses W_∞(k). The statement that every covering of A is an abelian variety is used without qualifications on coverings or base points here; π₁ᵖ(A)≃T_p(A) and perfectness/freeness are asserted, not proved on the sheet. Research should distinguish the stable subscript s from fixed elements, not silently replace either.')
