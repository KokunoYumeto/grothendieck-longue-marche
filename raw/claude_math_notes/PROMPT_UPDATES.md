# Prompt updates (main session, Claude Opus 5.5 at effort max)

The user, 16 Nov 2026: note the prompt updates I think are required; implement them myself when I am sure, or wait for a
Fable check; either way is fine. Every implemented change: backup of the PROMPT.md first, the push-rule lint after, and
a line here.

## Implemented

- **16 Nov ~00:4x UTC, LM 05_DELTA_ON_GT, item 2(b).**
  - Added: by Euler's pentagonal theorem eta = theta_{6,1}(tau, 0) - theta_{6,5}(tau, 0) =
    sum over n >= 1 of chi_12(n) q^{n^2/24}. So eta spans the chi_12-eigenline of the frame operators {1, 5, 7, 11}, and
    chi_12 is the character of {1, 5, 7, 11}/±1.
  - Prove or refute: on the multiplier-one subgroup, Delta = (1 - chi_12(a))/2, i.e. Delta = 1 exactly when the frame
    acts on eta by -1. Relate this to eta's multiplier system (Rademacher's Dedekind sums; Atiyah, Math. Ann. 278, 1987),
    and say whether the multiplier gives Delta a formula on all of GT-hat_0.
  - Why I am sure: the identity is classical. The Delta statement is put as prove-or-refute and only restates Lead 3(a)
    in a computable form.
  - Backup: longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/DELTA_ON_GT/
    PROMPT_before_eta_line_20261116.md.
  - `--lint-math` passes.

- **16 Nov ~01:2x UTC, LM 05_DELTA_ON_GT, item 2(b): consult lead C4.**
  - Replaced "say whether that multiplier gives Delta a formula on all of GT-hat_0" with prove-or-refute of aec1e030's
    lead: no function of the frame's class in the abelianization of the metaplectic group equals Delta (the E.58 frame
    lies in F'F^3, trivial in B^ab = Z/6, and has Delta = 1); Delta is the permutation part of the action of the
    central frame on eta in the Weil representation of index 6, and the phase part is the eta multiplier (chi_-4 on
    the centre separates 5 from 7).
  - Backup: .../DELTA_ON_GT/PROMPT_before_consult_lead_C4_20261116.md. `--lint-math` passes.

## Candidates (waiting for a Fable check or for reading)

- **aec1e030's C1-C3, for LM8_PUSH's successor (Part A) when it is written.**
  - C1: Goldstein's cusp etas of Gamma_0(4); kappa = Dedekind-sum differences; the order-4 character; A.6 as the
    Aut(E, O)-orbit of a tangential section. C1 could also go into the background of 02_SECTIONS_OVER_Q.
  - C2: Banerjee-Merel check of A.4's cusp divisor groups.
  - C3: the general A.3, i.e. Astra A1.
  - Text in research_maps_20261114/DEDEKIND_LM8_CONSULT/CONSULT_AEC1E030_20261116.md, section "Items for GPT-6
    Astra".

- **LM 02_SECTIONS_OVER_Q, background.**
  - lambda = theta_2^4/theta_3^4 = 16 eta(tau/2)^8 eta(2tau)^16/eta(tau)^24, and 1 - lambda likewise; Jacobi's identity
    is the unit equation.
  - A_s and B_s are Kummer classes of modular units on Y(2), with their archimedean side in the Kronecker limit formula
    at the three cusps.
  - Attach Banerjee-Merel for the cusp-divisor question.
  - Waits for F2.
- **LM 06_ANABELIAN_SUCCESSOR or a new item.** The general A.3 (Astra A1), with Banerjee-Merel and Zarhin as background.
  Waits for F1, and 06's scope still has to be checked.
- **LM 05_DELTA_ON_GT, item 2(c).** The elliptic Kashiwara-Vergne paper (dessins proceedings, p. 233) as a source for
  the genus-zero to genus-one step. I have to read it first.

## 16 Nov ~01:0x UTC
- LM 02_SECTIONS_OVER_Q was sent tonight without aec1e030's C1 (the candidate above): C1 moves to its successor.
- LM 05_DELTA_ON_GT was not sent tonight: R4 (CONSULT_AEC1E030_RAMANUJAN_20261116.md) and the chi_12 reading of NOTES
  §24 can go into item 2 before it is sent. Not implemented yet.
