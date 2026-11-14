# E3 completion update

| Request | Outcome | Statements | Scope |
|---|---|---|---|
| E3 | Proved for the stated diagram-isotopy relation and Hausdorff algebraic presentation | E.5–E.9 | The naive unseparated abstract quotient of profinite paths is not asserted to be Hausdorff. |

The gap previously recorded as E.U3 is resolved by defining the algebraic construction through its Hausdorff presentation and proving its universal property. A topological word becomes holomorphic by pulling a chosen target complex structure backwards. Diagram isotopies are represented by smooth configuration paths and finite-cover transports; these give continuous paths in the analytic diagram stack. This does not claim that an arbitrary nonsmooth isotopy is itself a holomorphic family in a real parameter. Equal actual composites receive the same source complex structure and are simultaneously algebraic, so the complete Betti presentation agrees with C_diag.

Noohi's comparison identifies the completions of the ordinary moduli and diagram path groupoids with their étale versions. In any Hausdorff target category with profinite automorphism groups, every ordinary-path realization extends uniquely, and every diagram naturality relation extends from dense ordinary paths by continuity. Therefore the E.6 envelope represents the purely algebraic Hausdorff presentation. The precise closure of the right stabilizer is proved by separation: all realizations kill its closure, and the E.6 envelope itself distinguishes every coset outside that closure. This is a proof of compatibility with all generated relations, not an assertion that arbitrary quotient operations commute with profinite completion.

E.9 checks the first nontrivial cover-and-filling family f_b(z)=z^2+b. The diagram component with labelled target is Y times B(mu_2); its braid group image and its profinite closure are compared exactly. Degree and defect force its factorization, avoiding additional unexamined relations in that component.

The root agent independently reviewed this argument and accepted E.8–E.9 as Proved. `sections/E_extension.tex` and `audit/E_extension_results.json` are ready for integration. Root should replace the old E.U3 unresolved statement by a scope remark about the naive unseparated presentation, remove that unresolved result-register row, and update E3's outcome to Proved. E1's repaired tame construction and E2's all-types arithmetic characterization remain separate.

Primary sources opened for this extension are recorded in `audit/F_E3_construction.md`: Bertin–Romagny 6.20 and 6.14 in the supplied source; Noohi 20.4 and its following corollary in the supplied source; Schneps (2003), section 2.1, in publisher PDF screenshots. The new bibliography key is `F_Schneps2003`.
