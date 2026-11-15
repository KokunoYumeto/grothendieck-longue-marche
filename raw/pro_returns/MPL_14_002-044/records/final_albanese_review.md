# Final A/H and standing-register review

Reviewed the assembled `MPL_14_002-044_notes.md` without editing it or the frozen transcription. Locations below refer to the assembly read for this review; note IDs remain the stable locators during rebuild.

## Actual issues reported to root

| Location | Issue | Exact repair |
|---|---|---|
| A12, assembled line524, first two sentences | The decomposition using the two axis projections and boxes omits the term $-\deg(\nu)[(0,0)]$ for a general zero-cycle. The argument concerns degree-zero cycles. | Change “each zero-cycle” to “each degree-zero cycle” and “The axis summands” to “The degree-zero axis summands”. |
| A18, line584, first sentence | With $U_*$ denoting the usual correspondence action on Chow groups, $S_Y\circ U_*=[n]$ omits the source Albanese map. | Write $S_Y\circ U_*=[n]\circ S_{A_Y}$ on $\mathrm{CH}_0(A_Y)^0$. |
| A26, line664, first sentence | The displayed map uses the variety symbols $A,A^\vee$ where the manuscript construction presently supplies point-group maps. | “The new construction sends the map $u_Z:A(k)\to P^i(X)$ induced by $Z$ to $u_{{}^tZ}:P^j(X)\to P^{i+j-n}(A)=P^1(A)\simeq A^\vee(k)$.” |
| A30, line702, metadata quotation | Ordinary French prose has been included inside a math span. | Use “mod. torsion (i.e. à coefficients $\mathbf Q_\ell$!)”. |
| Compact Standing question I table, after the scan044:6–10 row | The explicit historical hard/weak Lefschetz proof-status pair is absent from the compact index, although preserved in the full register S73/S86. | Add a scan044:10 row quoting “n'est pas même démontré pour le moment !” and “N'est démontré que le théorème de Lefschetz … faible”, identified as the dated 1965 author's statement about what was then proved. |

The first four repairs were sent to root with exact replacement text. The fifth is an index omission, not a loss from the archived exhaustive register. Root acknowledged the A12 correction and will apply repairs to the source record before rebuilding.

## Passes

- All **A01–A38** and **H01–H04** are present; the assembled file has **97 numbered note headings**.
- All A/H body dollar-math spans have balanced braces; dollar delimiters are paired. The repaired A14 expression $zZ'=z_0(mZ')=0$ survives assembly.
- A21 now states Kahn's printed dimension-greater-than-two scope, smooth projectivity, algebraic closedness, and the bound $2\dim B\le b_3(X)$.
- A35 now states smooth proper $X/K$, the surjective regular homomorphism and miniversal cycle, the three listed codimensions, and the exclusions on $\ell$.
- A28 retains complex smooth projective $X$ and projective parameter spaces, and supplies the factorization map without asserting an all-codimension identification with an algebraic representative.
- A38 correctly distinguishes Oda's **Corollaries 5.11 and 5.12**, retains the full Picard-scheme $p$-kernel and its nonreduced structure, and leaves the general manuscript Theorem3.1 unfinished.
- The compact index preserves the scope of scan015's Q-to-R correction and the live scan013 assertion with its deleted attempted proof. All **86 status entries, 24 typescript entries, 155 deletions, and 40 manuscript marks** remain in the full standing register.
- The cover and internal-title inventory survives in the compact title table and H01–H04. H01 correctly gives scan003's heading as “Structure”. Page marks and internal typed pagination are not converted into an invented total count.

## Primary rechecks for the changed hypotheses

- Kahn, Theorem 0.1 and the bound argument, printed pp.844–846: [published PDF](https://www.numdam.org/item/10.5802/aif.3408.pdf), reopened in this audit.
- Achter–Casalaina-Martin–Vial, §8.2 and Proposition 8.2, printed pp.119–120: [published PDF](https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf), web refs `turn85view0` and `turn86view0`. The source explicitly supplies smooth proper $X/K$, the miniversal degree $r$, and the injection for $i=1,2,\dim X$ and the stated primes.
- Oda's printed p.131 had already been visually rechecked in the immediately preceding standing-register audit; no changed Oda claim arose in assembly.
