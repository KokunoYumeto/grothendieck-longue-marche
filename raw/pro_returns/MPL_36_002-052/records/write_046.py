from save_page import save
tex=r'''
\scanpage{46}
$A$ variété abélienne en car $p$. On a, pour la partie de $\pi_1(A)$ première à $p$
\[
\pi_1^{\neq p}(A)\simeq\varprojlim_{\substack{n\\\text{\unsure{arith}}\\(n,p)=1}}\deleted{\unsure{n}}A^{(n)}
\]
où $\deleted{\unsure{n}}A^{(n)}$ est le noyau de $A\xrightarrow{n}A$, et où $A^{(mn)}\longrightarrow A^{(n)}$ est la multiplication par $m$.
\[
\boxed{\pi_1^\ell(A)\simeq\varprojlim_{\deleted{\unsure{\ell}}k} A^{(\ell^k)}\simeq T_\ell(A)=\operatorname{Hom}(\mathbb Q_\ell/\mathbb Z_\ell,A)}
\]
\margin{module de Tate}
$\ell$ étant un nb premier $\neq p$. Ce résultat provient du fait qu'un \uline{revêtement non ramifié d'une variété abélienne est une variété abélienne}

D'après Kummer, on a d'autre part
\[
\deleted{\text{Donc}}\operatorname{Hom}(\pi_1^\ell(A),U_\ell)\simeq
\text{sous-gpe de }\unsure{\mathfrak P|\mathfrak D}(A)=H^1(A,\underline O_A^{\unsure{*}})
\]
des élts d'ordre une puissance de $\ell$.

Si on admet que \uline{$A$ n'a pas de torsion}, on obtient donc
\[
\operatorname{Hom}(\pi_1^\ell(A),U_\ell)\simeq A^{*(\ell^\infty)},\qquad\text{i.e.}
\]
\[\boxed{T_\ell(A)\times T_\ell(A^*)\longrightarrow T_\ell(U_\ell)}\]
accouplement à valeurs dans le $\mathbb Z_\ell$-module libre de rang 1 $T_\ell U_\ell)$, et accouplement qui est une dualité.
\[
T_\ell(A)/\ell^kT_\ell(A)\times T_\ell(A^*)/\ell^kT_\ell(\unsure{A'|A^*})\longrightarrow
T_\ell(U_\ell)/\ell^kT_\ell(U_\ell)
\]
\[A^{(\ell^k)}\times A^{*(\ell^k)}\longrightarrow U^{(\ell^k)}\]
\margin{45}
'''
e=[('text','top','A variété abélienne en car p'),('display','first formula','π₁^(≠p)(A) ≃ lim A^(n)'),('deletion','first formula before A','n'),('text','right of first display','où A^(n) est le noyau'),('deletion','before A in explanation','n'),('display','upper boxed','π₁^ℓ(A) ≃ lim A^(ℓ^k) ≃ T_ℓ(A)'),('deletion','limit index in box','ℓ'),('margin note','right of box','module de Tate'),('text','under box','ℓ étant un nb premier ≠p'),('text','middle','D’après Kummer'),('display','Kummer formula','Hom(π₁^ℓ(A),U_ℓ) ≃ sous-gpe'),('deletion','start of Kummer formula','Donc'),('text','continuation of Kummer formula','des élts d’ordre une puissance de ℓ'),('text','conditional paragraph','Si on admet que A n’a pas de torsion'),('display','lower comparison','Hom(π₁^ℓ(A),U_ℓ) ≃ A*^(ℓ∞)'),('display','boxed pairing','T_ℓ(A)×T_ℓ(A*)→T_ℓ(U_ℓ)'),('text','right of pairing','accouplement à valeurs dans le Z_ℓ-module'),('display','penultimate row','T_ℓ(A)/ℓ^kT_ℓ(A) × T_ℓ(A*)/ℓ^kT_ℓ(A′)'),('display','last row','A^(ℓ^k)×A*^(ℓ^k)→U^(ℓ^k)'),('margin note','bottom left','45')]
d=[{'line':'first inverse-limit index','reading':'arith','alternatives':'abbreviation uncertain','confidence':'low'},{'line':'Kummer display Picard-like letter','reading':'fraktur P','alternatives':'fraktur D','confidence':'low'},{'line':'Kummer display sheaf exponent','reading':'*','alternatives':'short superscript stroke compressed','confidence':'medium'},{'line':'underlined no-torsion hypothesis','reading':'A','alternatives':'Λ conceivable from mathematical role, but the ink has the crossbar of A','confidence':'medium'},{'line':'penultimate row second denominator','reading':'A′','alternatives':'A*','confidence':'medium'}]
save(46,tex,e,d,'The manuscript explicitly says “Si on admet que A n’a pas de torsion” before the duality. A is what the ink resembles, despite the conflict with the surrounding abelian-variety notation; a potential Néron–Severi/Λ interpretation belongs to a reading question, not a silent correction. The covering argument is stated here with “non ramifié”, qualifying the shorter use in045. Perfectness and finite-level descent of the pairing are asserted; base field and continuity hypotheses are not supplied on this sheet. U_ℓ matches the U-shaped root-of-unity notation already seen in036; no conversion to μ has been made.')
