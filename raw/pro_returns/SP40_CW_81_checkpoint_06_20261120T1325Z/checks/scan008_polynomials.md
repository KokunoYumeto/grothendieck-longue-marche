# Scan008 — fixed polynomial certificates and marginal example

These calculations concern the supplied page formulas and do not establish their general implications. Each q below is one of the four explicit values2,3,5,7.

For these calculations, each manuscript coefficient symbol C_q^i is assigned the integer in the corresponding finite coefficient row below, computed by the integer function comb(q,i), with the assigned values printed below. This assignment extends the specified polynomial evaluation on those coefficient symbols.

For the binomial coefficients, the coefficient map Z[X,Y] → (Z/qZ)[X,Y] reduces each integer modulo that specified q and fixes X,Y. Addition and multiplication are carried to their coefficientwise residue operations, so these generator assignments define the stated morphism. Every internal coefficient in the four listed rows reduces to0.

For the lower bracket, use S_q(A,B)=sum(i=1,…,q−1) binom(q,i) A^i B^(q−i−1)+B^(q−1), with each listed q substituted before computation. The substitution map σ_q:Z[A,B] → Z[A,V] sends A to A and B to qV, and fixes integers; evaluation respects sums and products. The quotient map ρ_q:Z[A,V] → (Z/q²Z)[A,V] reduces integer coefficients modulo q² and fixes A,V. The composition is explicit. Direct coefficient calculation gives ρ_q(σ_q(S_q)−qA^(q−1))=2V for q=2, and0 for each of q=3,5,7. All unreduced bracket polynomials are below. These are four finite polynomial identities, with no conclusion asserted for other q.

The page's marginal values q=2,a0=b0=1,gamma=1,b=4,a=3,c=5 agree with the parameter values in the previous page's certificate. Direct evaluation gives b′=2, a′=1 and c=4+1=3+2=5. The two accompanying gcd values for the factorizations a=1·3 and b=1·4 are1. These computations check that written example and those concrete factorizations only. The previous event is007-arithmetic-instance.

Executed: 2026-11-20 11:25:04 UTC

```json
{
  "cases": [
    {
      "q": 2,
      "inner_binomial_coefficients": [
        2
      ],
      "remainders_mod_q": [
        0
      ],
      "substituted_bracket": "2*A + 2*V",
      "bracket_minus_qA_mod_q_squared": "2*V"
    },
    {
      "q": 3,
      "inner_binomial_coefficients": [
        3,
        3
      ],
      "remainders_mod_q": [
        0,
        0
      ],
      "substituted_bracket": "3*A**2 + 9*A*V + 9*V**2",
      "bracket_minus_qA_mod_q_squared": "0"
    },
    {
      "q": 5,
      "inner_binomial_coefficients": [
        5,
        10,
        10,
        5
      ],
      "remainders_mod_q": [
        0,
        0,
        0,
        0
      ],
      "substituted_bracket": "5*A**4 + 50*A**3*V + 250*A**2*V**2 + 625*A*V**3 + 625*V**4",
      "bracket_minus_qA_mod_q_squared": "0"
    },
    {
      "q": 7,
      "inner_binomial_coefficients": [
        7,
        21,
        35,
        35,
        21,
        7
      ],
      "remainders_mod_q": [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "substituted_bracket": "7*A**6 + 147*A**5*V + 1715*A**4*V**2 + 12005*A**3*V**3 + 50421*A**2*V**4 + 117649*A*V**5 + 117649*V**6",
      "bracket_minus_qA_mod_q_squared": "0"
    }
  ],
  "example": {
    "q": 2,
    "a0": 1,
    "b0": 1,
    "gamma": 1,
    "zeta": 0,
    "a": 3,
    "b": 4,
    "c": 5,
    "a_prime": 1,
    "b_prime": 2,
    "a_double_prime": 3,
    "b_double_prime": 4
  }
}
```
