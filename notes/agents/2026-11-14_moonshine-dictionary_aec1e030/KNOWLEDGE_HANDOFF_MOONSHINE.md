# Knowledge handoff: the moonshine dictionary

By Claude Fable 5.2 at effort high (the agent of `research_maps_20261112\PRETOT_3D_MODULARITY\MAP.md`), 14 November
2026, 17:18 UTC (clock read). For resuming this agent, or for a successor.

## Read in this order

1. `MOONSHINE_DICTIONARY_20261114.md` (this folder): the dictionary (25 rows), the checks of the earlier bridges,
   the surprises S1-S9, the hunches 4.1-4.7 with items M1-M5 for GPT-6 Astra (ChatGPT Pro mode), what was read.
2. `USER_WORDS_P5023-P5024.md` (the user's aim, P5023-P5026) and the brief.
3. `research_maps_20261112\PRETOT_3D_MODULARITY\MAP.md` for the Ẑ / E8³ / Leech line with its opened statements.
4. `check_dictionary_arithmetic.py` (this folder): the arithmetic behind the [computed] flags.

## The state in eight lines

- Level 5 is the self-dual point of the umbral A-series, (ℓ − 1)(p + 1) = 24 with ℓ = p = 5; the umbral group
  there, GL₂(5)/2 with quotient PGL₂(5), is the arithmetic group of X(5) over X(1) and Aut(A₅). Tables opened in CDH;
  the identification is mine.
- The tripod is Γ₀(4), class 4C, the Niemeier case A₃⁸, Hauptmodul q⁻¹ − 8 + …. Opened in CDH.
- The frame 5I mod 12 of LM7_PUSH E.58 is the Eichler-Zagier operator a(3) of index 6 (lambency 6+3, D₄⁶); the
  user's lattice N(A₅⁴D₄) is the other index-6 case. Hunch that Δ is the frame class in {1,5,7,11}/±1.
- Gannon §6.3.3 gives the Galois action on modular data (G_σ = diag(χ, χ⁻¹)) and says it is not Grothendieck's;
  E.58 sits between. Hunch, three to one: Δ = 0 on ĜT, through Drinfeld's action on pointed braided categories.
- The Weil representation 30+6,10,15 has the T-matrix of (G₂)₁ (Fibonacci) times the η³ multiplier. Computed;
  S-matrix not checked.
- M_{0,[12]} is the Thurston / Deligne-Mostow Eisenstein ball quotient (from memory). In the congruence completion
  of that quotient the centralizer of the icosahedral A₅ is an infinite torus; lifting to Γ̂_{0,[12]} is open.
- Galois's primes 5, 7, 11 organize CDH Table 4 and give two siblings of the resolvent map 𝔗_T.
- For A1 and F.9 the bridge gave nothing of weight.

## What a resumed agent should do first

- Check the five points listed at the end of the dictionary's section 5, in that order of cost: the S-matrix of
  30+6,10,15 against Fibonacci (CDH and 3d Modularity have the Weil representation; ten minutes); the 16 of the
  tripod against LM6 F.45, F.46 (one register row); E.65's definition of Δ against hunch 4.1 point 1 (the referee
  report on E.65); the unit u = 1 − 1728/j and ANABELIAN D.27, D.28; Deligne-Mostow at 12 points with weights 1/6
  (the book is in `F:\user\Documents\arxiv_latex\library\moonshine_lattices\`).
- Open, on disk and unread: *Optimal Mock Jacobi Theta Functions*, *Class numbers, congruent numbers and umbral
  moonshine*, *Umbral Moonshine and Linear Codes*, Chenevier-Lannes, *The Leech lattice and other lattices*
  (Borcherds), Curtis on M₂₄ (for the icosahedral form of the Golay code, still from memory), the rest of HGA.
- Hand items M1 and M2 to the field experts for prompt writing: M1 to the Longue Marche line (Δ, E.3), M2 to the
  LM4 successor (item 2.4), with the flags as they stand.

## Working facts

- Text extracts used here were made with `pdftotext -layout` into the session scratchpad; they are not kept. CDH is
  LaTeX: `…\moonshine_lattices\Umbral Moonshine and the Niemeier Lattices\UMNL_x2.tex` (tables at lines 713-790 and
  815-860; exact divisors at 646-680; the Ω matrices at 1103-1128; the ADE table at 1203-1220).
- Gannon §6.3.3 is at lines 24035-24366 of the extract of *Moonshine Beyond the Monster*; SPLAG Ch. 8 §2 at
  15835-15935 of its extract.
- The papers of MAP.md are in `research_maps_20261112\PRETOT_3D_MODULARITY\papers\`.
- Context at the end of this task: about 505k tokens (an estimate; started near 290k). Further reading only on a
  new bound from the coordinator.

## Added 14 November 2026, later the same day: ghost symmetries and lambency (same agent, Claude Fable 5.2 at effort high)

Two more files in this folder, written at the user's word through the main session (Claude Opus 5.5 at effort max):

- `GHOST_SYMMETRIES_TRANSLATION_20261114.md`. Olver-Sanders-Wang's ghost characteristics built into our work, with
  the user's thread (the ghost is the countersign that cancels the ambiguity of integration) and the move of
  Andrews-Connes-La Gatta (make the obstruction an operator). To carry:
  - frames are antiderivatives of the cocycle f for the two coboundary operators of s and r; ghost values are
    constants of a finite level that are not constants globally; E.58 is the paper's Example 5;
  - the obstruction group at level N is Ob(N) = Z(SL2(Z/N))/{+-1}, trivial at prime-power level, the group of
    relative signs between the primes of N; its elements are diamond operators; the sign idempotent is
    (1 - <a>)/2;
  - definition by cancellation: Delta_N(F) = (central frame class) times the inverse of the diamond operator of
    the multiplier; a conjectural family of characters of GT0-hat, Delta = Delta_12;
  - section 1a: every stuck item as a map Glob -> Loc with its forgetful part K, its obstruction group and the
    theorem that would make it usable;
  - the pentagon as the Jacobi identity (three rigid frames in the 5-point group); K of item 2.4 is trivial, or
    non-abelian, or a counterexample to the LM8 G.20 statement on the tripod C_T;
  - items GS1-GS6, each placed against a prompt.
- `LAMBENCY_IN_AG_20261114.md`. Lambency n+S as (the curve X0(n) with its dessin over the modular orbifold, over the
  tripod when 4 divides n) plus (a set of Atkin-Lehner involutions: symmetries of the curve that are not symmetries
  of the dessin). To carry:
  - index m corresponds to level 2m; the Atkin-Lehner group of level m is the centre of SL2(Z/2m); for m = 6 it is
    {1,5,7,11}, Fricke is -1, and the class of W3 (= the class of W2) is the non-trivial ghost sign;
  - X0(6) is P1 minus four rational points (lambda = 9), its Atkin-Lehner group is the Klein four-group of that
    sphere, and its group is the fibre group of the 5-point over the 4-point group;
  - conjecture: Delta(F) = 0 iff F restricted to the group of X0(6) commutes with W3;
  - items L1-L4.

Nothing in either file is refereed. Not opened for them: E.65, D.50, E.58 themselves (used through our intakes);
any source on X0(6) or on torsion in sphere braid groups. First checks, cheapest first: the frame of E.58 against
"diamond operator <5>" in the referee report on E.58; the cusps and Hauptmodul of X0(6); the uniqueness computation
behind "GT0-hat preserves the congruence kernels" (LAMBENCY 2.3).

Context at the end of these two tasks: about 700k tokens (an estimate).
