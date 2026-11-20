# Conditional cohomology check while reading scan 005

Statement id: `134-1.005.check.exact_sequence`. Main reader: GPT-6 Astra Pro; effort not exposed. This is reasoning from the formulas on the supplied pages, not external research and not proof that the proposed triangle exists.

Scan 004 specifies E with cohomology Ext^i in degrees 0 through 2 and zero outside that range. Put A = underlined Hom(M,{}_2N)[-2]. Under the usual cohomological shift convention, A has just one cohomology object, H^2(A) = underlined Hom(M,{}_2N).

Conditionally interpret the author’s proposed distinguished triangle as E → E′ → A → E[1]. The relevant segment of its long exact cohomology sequence is

H^1(A) → H^2(E) → H^2(E′) → H^2(A) → H^3(E).

The two outer terms vanish under the displayed degree specifications. Therefore the short exact sequence written on scan 005 is the one the triangle would give: 0 → Ext^2(M,N) → H^2(E′) → Hom(M,{}_2N) → 0.

For i other than 2 and 3, both H^(i−1)(A) and H^i(A) vanish, giving H^i(E) ≅ H^i(E′). For i = 3, H^3(E)=0 and H^3(A)=0 force H^3(E′)=0 as well. Hence the cohomology agrees away from degree 2. This makes an inequality i≠2 a meaningful alternative to inspect in the opening sentence. It supplies no license to replace a plus sign if a plus is what the ink shows.

Event classification: targeted proof check of a conditional consequence. Outcome: the degree-exception statement and displayed short exact sequence are consistent consequences of the proposed triangle and the displayed cohomology range. The triangle itself remains the author’s heuristic assertion, not a verified construction. Visual adjudication of the ambiguous sign is still pending when this note is first written.
