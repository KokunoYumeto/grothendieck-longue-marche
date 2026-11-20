# Scan007 — one exact arithmetic instance

The assignment is q=2, p=2, a=3, b=4, c=5, b′=2, a′=1, α=2, α′=1, b″=1. The evaluation morphism Z[A,B,C,U,V] → Z fixes integers and sends the five generators to 3,4,5,2,1 respectively; it extends by addition and multiplication. Thus each finite polynomial expression is evaluated using those generator images. Prime and divisibility assertions in this instance are checked by integer arithmetic below.

The equalities a²+b²=c²=25, c=a+b′=b+a′=5, b²=2ab′+b′²=16 and b²=b′(2a+b′)=16 hold numerically. The bracket in the last line is 2a+b′=8, and p^(qα−α′)=2³=8. Its quotient is1 and its remainder0. The exact valuations are evidenced by divisibility at2² and2¹ respectively and the nonzero next-power remainders. This finite instance rechecks the exponent/substitution pattern only. It does not prove the page's general implications or settle any glyph or hand attribution.

Executed: 2026-11-20 11:09:38 UTC

```json
{
  "values": {
    "a": 3,
    "b": 4,
    "c": 5,
    "q": 2,
    "p": 2,
    "b'": 2,
    "a'": 1,
    "alpha": 2,
    "alpha'": 1,
    "b''": 1
  },
  "coprimality": [
    1,
    1,
    1
  ],
  "power_identity": [
    25,
    25
  ],
  "positive_differences": [
    2,
    1
  ],
  "full_binomial_sum": 25,
  "equation_1": [
    16,
    16
  ],
  "factored_equation_1": [
    16,
    16
  ],
  "valuation_residues": {
    "b_mod_p_alpha": 0,
    "b_mod_next": 4,
    "bp_mod_p_alphap": 0,
    "bp_mod_next": 2
  },
  "valuation_inequality": [
    1,
    4
  ],
  "bpp_factorization": [
    2,
    2
  ],
  "bpp_coprimality": 1,
  "final_divisor": 8,
  "final_bracket": 8,
  "final_division": [
    1,
    0
  ]
}
```
