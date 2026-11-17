# Conditional checks for the extension worksheets

These computations use the frozen transcription only as a source of questions.
They do not select a doubtful reading or assert a global categorical theorem.

| Source / note | Exact result | Interpretation |
|---|---|---|
| 126 / B04 | `-U*(chi*gamma - 2)` | Residual in the displayed translation square; zero if gamma*chi=2. |
| 128 / B05 | `[-2, 0, 2*U, -2]` | Row-major entries of -T_-U minus inverse(T_U); the extra scalar minus is different from inversion. |
| 128 / B08 | `[(1, 3), (3, 1)]` | Pairs (gamma,v) modulo 4 for chi=2 and b=1; both shift b to -b, but the translations differ. |
| 130 / B09 | `(chi - 1)*(b1*u2 + b2*u1 + chi*u1*u2)` | Same-coordinate residual if the final increment is read as U instead of chi*U. |
| 132 / B11 | plus convention: `0`; minus convention: `2*chi*(u1*v2 + u2*v1)` | The two sign conventions cannot be mixed in the displayed cocycle calculation. |
| 140 / B19 | `chi*lambda1*lambda2` | The three terms on L1 tensor L2 simplify without imposing chi=1. |
| 144 / B24 | Q(relation)=0; Q((f tensor id)(relation))=`[1, 0]` | An endomorphism preserving L need not preserve the pushout relation. |

The scalar polynomial cocycle check is a bookkeeping check of the new draft signs;
the later context already claims the positive local groupoid composition identity (R11).
