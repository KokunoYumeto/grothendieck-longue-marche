# Main reader: limited algebra checks

## 078-A: inverse cocycle identity

From the displayed relation g_l(uv) = {}^u g_l(v) g_l(u), inversion reverses the two factors. As the superscript u is an automorphism, ({}^u g_l(v))^{-1} = {}^u(g_l(v)^{-1}). This gives g_l^{-1}(uv) = g_l^{-1}(u) {}^u g_l^{-1}(v), in the order shown by the ink. This is a targeted algebra check of (29), not a proof of the geometric construction or descent.

## 079-A: change-of-path identities

With int(a^{-1})(z)=a^{-1}za and f_a(u)=a^{-1}{}^u a, the displayed product int(a^{-1})f_l(u) f_a(u) reduces to a^{-1}f_l(u){}^u a. Similarly g_b(u) int(b)g_l(u) = ({}^u b b^{-1})(b g_l(u)b^{-1}) = {}^u b g_l(u)b^{-1}. Inverting gives b g_l^{-1}(u){}^u b^{-1}. These are targeted checks of (31) and its following parenthesis. They do not reconstruct the cancelled expression beneath g_l(u).

## 079-B: final target letter

The final diagram writes a clear Y in its right-hand group, although the surrounding source/target points and path concern X. A same-space change-of-basepoint map would have X there. Preserve the written Y; the mathematical expectation is a note, not a transcription correction.

## Scan 084 — conditional functoriality check (root)

Let F be the groupoid functor denoted by the manuscript’s hatted f. Assuming the equivariance written in (39), F({}^u l)={}^uF(l), and functorial preservation of products and inverses, the definitions from the earlier pages give F(f_l(u))=F(l^{-1}{}^u l)=F(l)^{-1}{}^uF(l)=f_{F(l)}(u). Similarly, F(g_l(u))=F({}^u l l^{-1})={}^uF(l)F(l)^{-1}=g_{F(l)}(u). This checks the two identities in (40) conditional on the stated equivariance, not the geometric claim that a particular functor is equivariant. The ink independently shows l in both subscripts. No mathematical correction was inserted. Record as one targeted proof check when scan084 is committed.

## Scan 086 — actual targeted proof check

For a fixed u, the definitions already read in this run give f_lambda(u)=lambda^{-1}({}^u lambda) and g_lambda(u)=({}^u lambda)lambda^{-1}. Hence {}^u lambda=lambda f_lambda(u)=g_lambda(u)lambda. Values of either displayed family (43) recover the action on the named generators. If those generators topologically generate the profinite group and the action is continuous, equality on the abstract subgroup they generate extends to the profinite group by density and the Hausdorff property. This verifies only that refined determination step, under explicit topological-generation and continuity assumptions. It does not supply a missing hat, replace x_i by I in the preceding path expression, or repair the repeated number (41). Main reader: GPT-6 Astra Pro; effort not exposed; 2026-11-20. Type: targeted proof check.


## Scan091

Targeted proof check 142-091-R1 (root): in a connected groupoid D with a functor F, let N_x=ker(Aut_D(x)→Aut_E(Fx)). For a path p:x→y, N_y=pN_xp^{-1}. If an automorphism γ fixes the relevant objects and preserves N_x, then γ(N_y)=γ(p)N_xγ(p)^{-1}=qN_yq^{-1}=N_y, where q=γ(p)p^{-1}∈Aut_D(y), using normality of N_y. Thus preservation at one basepoint implies preservation at every basepoint under these stated hypotheses, matching the page’s “alors ce sera vrai également pour tous les autres”. This algebraic check does not establish the geometric hypotheses or alter any written sign.
