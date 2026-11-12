# Late §49 normalized sections and restricted conjugators

| Task | Outcome | Statements | Exact scope |
|---|---|---|---|
| A.a | Partly settled | B.17–B.18 | Source-indexed dictionary for C3:583–595,635–650,651–690, including the additional open normal subgroup. |
| A.b | Partly settled | B.17–B.18 | Formal identities proved and finite alternatives executed; actual profinite subgroup identifications remain explicit. |
| B.c | Partly settled | B.17–B.18 | The ill-typed smaller quotient is refuted and repaired; conditional bisection exact sequences are proved. |
| B.g | Partly settled | B.17–B.18, B.16 | Retained signs, multiplier and allowed conjugators are separated; the unquotiented lifts and integral comparisons remain precisely stated. |

## B.17: a quotient defect in the actual modular input

The checked text at C3:658(18) deliberately replaces the intersection of the loop subgroup with the open normal subgroup by its inverse image under the numerical inner-automorphism map. Its margin explicitly allows this new loop subgroup to be larger. Nevertheless C3:659(28) places its entire antidiagonal in the smaller semidirect product, and C3:660(29) divides that product by it. These expressions are undefined when containment fails.

The defect occurs for the named universal modular input, not just for an arbitrary finite group. Set (C=\widehat{\mathrm{SL}_2(\mathbb Z)}), (A=\widehat\Pi_0), (e_0=\sigma\rho), and (l=e_0^2). The element (h=-e_0^2) is one of the specified generators of (A). It induces exactly the same inner automorphism as (l), so both restricted conjugators may be (h). This inner automorphism fixes the loop and acts trivially on (C/A), satisfying even the stronger discarded version of condition d). Reduction modulo four proves that (l\notin A). Thus (l\in L_A\setminus A) in the actual named construction.

The repair is to take the image (H_A) of (A\rtimes D) in the ambient quotient (G=(C\rtimes D)/\Delta L). Its presentation divides by (\Delta(L\cap A)), and its exact quotient is (D/j(L\cap A)). If (j) is injective, the kernel over (D/jL) is the image of (AL), which equals the image of (A) exactly when (L\subset A). The proof establishes normality, the actual intersection kernel, and the topological identification in the profinite case, assuming profinite (D), continuous action and (j), and closed stable subgroups.

The numerical automorphism-and-sign kernel also needs this intersection. For (P_A=\{(f,m)\in A\times T:(\mathrm{Int}(f),m,1,1)\in D\}), it is (P_A/\{(l,1):l\in L\cap A\}). The denominator in C3:664(52 bis) cannot remain all of (L_A) without an additional containment hypothesis.

The executed modular image has (C=\mathrm{SL}_2(\mathbb Z/4)), of order 48, and (A=V_4), of order 4. Its actual positive-sign loop preimage is (L=\{1,e_0^2\}); both (L\cap A) and (L\cap Z(C)) are trivial. For (D=jL), the corrected image (AL) has order 8 and automorphism kernel (\{I,-I\}). This verifies the defect and the repair without exploiting a failure of the earlier loop-injectivity condition.

## B.18: what the later formulas establish and what remains

The dictionary covers the normalized (a_0,a,b) maps and congruence-defined central extension in C3:583–595; the (M^0(-\bar j)), (M'''(-\bar j)) lattice and asserted index-24 normalizer quotient in C3:635–647; and the early smaller fibre product and bisection in C3:647–650. It then records the distinct §49.VI input (A=C^\natural), which begins at scan651 and continues through690. This input restricts the conjugators themselves. It is not the coefficient-only restriction in B.13/B.15.

The surviving C3:653(4)d requires identity on ((C/A)/\operatorname{Im}\Pi), not on all of (C/A). Allowed reversing conjugators use (\tau), not (\tau'=\sigma^{-1}\tau). Since (\tau(\rho)=\sigma\rho^{-1}\sigma^{-1}), replacing the condition by (A)-conjugacy to (\rho^{-1}) is unjustified when (\sigma\notin A). The first named proper modular datum is (A=\widehat\Pi), of index 6, followed by (A=\widehat\Pi_0), of index 12.

The following substantive cases are proved and executed:

- The twisted (a_0) multiplication law follows directly from (\delta(u)=t^{\nu(u)}\delta(a_0(u))). All 36 ordered pairs in (S_3) satisfy it; 12 fail ordinary multiplicativity.
- The corrected (\alpha'') formula includes (t^{\nu_3'}[a',t^{\nu_3}]t^{-\nu_3'}). Its group-word proof is accompanied by 5,184 finite checks and a counterexample to omitting the commutator.
- The source-order cocycle is (c((u',v'),(u,v))=u(u'+v')). All 512 associativity triples and 16 sign pairs are checked. The change ((s,u,v)\mapsto(s+uv,u,v)) identifies it with equation (D.15) in D.8, avoiding an unnoticed reversal of factor order.
- Given the exact typed normalizer inputs, the fibre-product proof gives the early bisection, its central kernel, the split quotient after dividing by that kernel, and the central intersection (\mu_\rho\times1\times\mu_G). The 192-element model has a 16-element smaller subgroup and an eight-element quotient. One quotient involution has both lifts of order four, proving that the omitted quotient in scan650 cannot be replaced by an automatic lift.
- For restricted factors, the image in the third factor is exactly the inverse image of the intersection of the first two images in the common quotient. This proves the precise reduction invoked but not checked in scan690.

B.16 now establishes normalized conjugators, maps (Z^!\to N_\rho^*/\langle\omega\rangle) and (Z^!\to N_\sigma^*), and quotient sections over (\gamma), inside its explicitly defined (G_Z). B.18 uses those results. It does not leave these normalized maps open. What remains includes the unquotiented (\sigma)-section, identification of the central pullback with the manuscript’s (N_\rho^?), and identification of the congruence-defined (S_0^\Pi\Gamma^!) with the computed central extension. The actual subgroup normality/index lattice in C3:635–642 and exact kernel (\ker(N_\rho^*\to\mathrm{GL}_2(\mathbb Z/4)/V_4)=M^0(-\bar j)) are also explicit residuals. Knowing that the finite target has order 24 does not prove that kernel.

For §49.VI, the remaining comparisons are the actual (L_A), the corrected image (H_A), and its map to (M^A) of C3:682(107), including the proposed identifications C3:686(115)–(116). The images of (N_\rho^{A,?}) and (Z_{\sigma0}^{A,!}) in (\Gamma_0^A) must then be determined to settle C3:689–690. These are stated for the explicit modular data (A=\widehat\Pi), then (\widehat\Pi_0); the latter already has the quotient defect of B.17. Representability over \(\mathbb Z\) and fppf comparison are separate residuals. Finite constant group schemes do not supply those general integral automorphism functors, and their constant (C_2) is not replaced by (\mu_2) in characteristic two.

## Sources, status and reproduction

The exact passages are recorded in `B_late_sections_readings.json`. The supplied photograph of scan652 was inspected; the exact formulas at583–595,635–650,658–664 and682–690 are available here as checked transcriptions, without their photographs. Consequently the corrections are mathematical consistency conclusions, not palaeographical determinations. The natural/sharp superscript remains a working reading. Cancelled diagrams and stronger deleted quotient-action conditions have not been reinstated.

There are two numbered statements: B.17 **Refuted**, with a fully proved repair; B.18 **Open**, with the proved formal cases, executed finite instances and exact remaining comparisons above. “Open” denotes what remains unresolved in this report, without a claim about the literature. No additional external theorem is used beyond the references already verified for B.16, D.8 and E.15–E.19.

Both programs use only Python’s standard library. From the project directory run:

```sh
python code/B_late_sections.py > code/B_late_sections.out
python code/B_late_sections_registers.py > code/B_late_sections_registers.out
```

The first writes `code/B_late_sections.json`; the second reads that output and regenerates the two-row results register, fifteen-row readings register and nine-row coverage register. Executed under Python 3.12.14. No new third-party dependency is required.
