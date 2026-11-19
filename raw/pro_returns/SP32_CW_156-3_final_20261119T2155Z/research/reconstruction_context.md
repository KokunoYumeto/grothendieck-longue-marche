# Reconstruction and context research draft

Research only, after the root's 2026-11-19 21:31:14 UTC freeze. No scan was inspected by this research worker and no transcription, apparatus, or hash was changed. Sources read: the complete supplied `notes/RESULTS_STATE.md`; frozen scans 040–041; `Esquisse_cote119_copy1_API_transcription.tex`, especially its markers 119/29–44; `MPL_156-3/README.md`; `sweep3/readings/156-3.md`; relevant portions of `sweep3/STUDY.md`. Source paths below are relative to `source/SP32_CW_156-3_context/` unless explicitly labelled sweep. This is a draft for root integration, not a replacement final notes file.

## Concise note items

### REC-01 — Scan 041, lines 1–9 — unproved claim / reading question

**Anchor:** “Caractérisation d'un ... intervalle ... en ... que réseau”; “S ... Drap₂(L)”. The displayed data specify the unordered comparable pairs and a partition of the points simultaneously comparable with a given pair; in the total-order model $S=\mathcal P_2(L)$, so the cut partitions carry the information which the pair relation alone lacks. The mathematical discussion below uses the usual set-builder interpretation $x\in L\setminus\{a,b\}$, without resolving the frozen in-place `+|\in` or `a;x|a',x|a,x` doubts. **Context/relation:** sweep `readings/156-3.md` §§1.1–1.3 reports the same data at scans 002–004 and 015–016; scan 041 restates that programme, but this run did not inspect those earlier scans. **Register:** Hua, findings register, `156-3-betweenness-from-cuts` (supports the formulation, with the stated scope limit).

### REC-02 — Scan 041, lines 10–18 — self-flagged / unproved claim

**Anchor:** “J'ai commencé à faire l'exercice”; “ça n'en vaut pas la peine de l'expliciter jusqu'au bout”; “Hilbert ?”. This is an explicit abandonment of a complete written characterization, not a completed axiomatization or a verified historical attribution. Recovering an order from data already known to come from a tronçon and recognizing which abstract data $(S,R_\varepsilon)$ come from a tronçon are different questions, and the latter still needs exact necessary and sufficient axioms. **Context/relation:** sweep `readings/156-3.md` §§1.3 and 1.7 links this ending to the uncompleted scan 017 question; the supplied *Esquisse*, 119/34 and 119/36, likewise distinguishes plausible axioms and heuristic reconstruction from completed proofs. **Register:** Hua, findings register, both `156-3-order-from-betweenness` and `156-3-betweenness-from-cuts`; neither entry supplies a recognition theorem in the supplied register excerpt.

### REC-03 — Scan 041, cut data — own idea / targeted proof check

**Anchor:** “la décomposition ... en ‘composantes connexes’”. For a known dense tronçon with the model cut classes, let $K_{ab}(c)$ denote the class of the cut by $\{a,b\}$ containing $c$; for three distinct pairwise comparable points, $b$ is the middle point exactly when $K_{ab}(c)\cap K_{bc}(a)=\varnothing$. If $a<b<c$, that intersection is $L_{>b}\cap L_{<b}=\varnothing$, whereas the analogous intersections for the two outer candidates contain respectively $(b,c)$ and $(a,b)$, nonempty by divisibility. **Context/relation:** independently checks the mathematical criterion summarized by sweep `readings/156-3.md` §1.3 (its scans 015–016), without authenticating that earlier manuscript proof. **Register:** Hua, findings register, `156-3-betweenness-from-cuts`; **confidence:** high for this conditional reconstruction, because the three cases are explicit; no claim of novelty or of an abstract recognition theorem.

### REC-04 — Scan 041, “et divisible” — own idea / hypothesis check

**Anchor:** inserted “(et divisible)”. Density is essential for the preceding pair-cut criterion: on a three-point chain every cut by a two-point subset leaves one singleton, so all three possible choices of middle point give exactly the same pair relation and all the same cut partitions. Thus these data cannot reconstruct an arbitrary discrete linear order, even up to reversal. **Context/relation:** sharpens the scope of sweep `readings/156-3.md` §1.3, which says divisibility is used but gives no counterexample there; it also explains why the insertion on 041 matters mathematically. **Register:** Hua, findings register, `156-3-betweenness-from-cuts`; **confidence:** high, by direct inspection of all three two-point cuts.

### REC-05 — Scan 041, betweenness — own idea / independent re-proof

**Anchor:** “s est entre a et b”. A dense partially ordered set directed upwards and downwards and containing a comparable pair is determined up to reversal by its strict betweenness relation: orient one pair $a<b$, recover $L_{\le a}$ and $L_{\ge b}$ from betweenness, and bound any two points between an element of the first cone and an element of the second. Appendix A gives an explicit relation formula and proves it; the strict-cone filtering axioms of a tronçon are not needed for this uniqueness step. **Context/relation:** independently checks the claim of sweep `readings/156-3.md` §1.3 (earlier scans 012–014) and explains how scan 041 can invoke betweenness for non-total models without reducing them to lines. **Register:** Hua, findings register, `156-3-order-from-betweenness`; **confidence:** high for the stated theorem, because the reconstruction is explicit; the register's Courcelle attribution and precise literature scope were not checked.

### REC-06 — Scan 041, unordered data — unpursued implication

**Anchor:** “Drap₂(L)”; “décomposition”. Reversing the order preserves the set of comparable pairs and merely exchanges the lower and upper cut classes, so unlabelled partitions can recover at most the order up to reversal. Here “unlabelled” must still mean a partition into actual subsets of the given set $L$: retaining only the numbers of components loses all betweenness information on an endpoint-free dense total order, since every pair has three nonempty classes. **Context/relation:** clarifies the meaning of the “partition (unlabelled)” in `notes/RESULTS_STATE.md`, Hua entry `156-3-betweenness-from-cuts`, and the “biorder” terminology reported in sweep §1.3. **Register:** both Hua findings; proof is the direct reversal symmetry and the constant three-class count, not a literature attribution.

### REC-07 — Scan 041, scope of the Hua findings — reading question / research-status audit

**Anchor:** “J'ai commencé ... l'exercice”. The two Hua findings concern scans 012–016, outside this package's images, while scan 041 supplies a clear later reprise and an explicit limit on how far the characterization was written out. Their mathematical uniqueness claims pass the conditional checks REC-03 and REC-05, but neither the original ink nor the historical reference claims were independently checked in this research stage, and the full characterization is not thereby settled. **Context/relation:** corrects any reading of sweep `readings/156-3.md` §§1.3, 1.7 as proof that the final abstract network axioms are complete. **Register:** Hua, findings register, `156-3-order-from-betweenness` and `156-3-betweenness-from-cuts`; no unrelated open register item changes status.

### REC-08 — Scans 040–041 — own idea / test of S14

**Anchor:** “décomposition ... subdivision”; “en ... que réseau”. Finite cut sets of a total order are directed under inclusion, since the union of two finite cut sets is another one, but this fails for the natural finite-chain cuts of a non-total tronçon: two incomparable singleton cuts admit no common chain containing both. An admissible example is the doubled rational line, whose points $(q,i)$ and $(q,j)$ at the same rational level are incomparable, with all points at smaller levels below all points at larger levels. **Context/relation:** tests, and blocks an automatic extension of, the S14 pro-object guess in `MPL_156-3/README.md`; sweep `STUDY.md` §3 likewise says the pro-object description was not on its earlier pages, while `readings/156-3.md` §1.2 supplies the doubled-line lead. **Register:** `WG2 B15 (§1.2)` and `WG2 §3.1 #2` (a limitation on a proposed bridge, not a refutation of their stated finite-poset results); **confidence:** high for this particular indexing obstruction, with no claim that every possible category of cuttings fails to be cofiltered.

### REC-09 — Scan 040, finite subdivision — own idea / explicit counterexample to a naive limit identification

**Anchor:** “connue quand on connait S”. Even on $L=\mathbb R$, the ordinary inverse limit of the underlying finite cell-partition sets contains a compatible “$0^+$” thread choosing the cell immediately to the right of $0$, and this thread is not represented by any real point. Appendix B proves compatibility and nonrepresentation; choosing a finite incidence-poset structure does not by itself remove this extra point from the underlying set limit. **Context/relation:** qualifies S14 in `MPL_156-3/README.md` and connects with the Stone-space warning reported at sweep `STUDY.md`, 156-5 section, scans 016–017; this is not an identification with that later author's construction. **Register:** `STRATA A.4`, `STRATA A.12`, `BISITE G.10` (their finite realization claims do not assert this inverse-limit identification), and `WG2 B15 (§1.2)`; **confidence:** high for the explicit extra thread, not a disproof of a pro-object description with additional marked-point data.

### REC-10 — Scans 040–041 — unpursued implication / bounded planning verdict

**Anchor:** “subdivision”; “Caractérisation”. These pages give a concrete one-dimensional reconstruction project from compatible finite cuts, but do not define a pro-object of finite posets, give its morphisms, or prove an equivalence of categories. Thus S14 is supported only as motivation; its asserted categorical identification is unestablished here, and the specific naive constructions in REC-08–09 need extra choices or conditions. **Context/relation:** `MPL_156-3/README.md` labels S14 a title-derived guess, and the present pages justify retaining precisely that tentative status. **Register:** `WG2 B15 (§1.2)` and `WG2 §3.1 #2`; the finite-poset claims `STRATA A.4/A.12` remain background, not proofs of S14.

### REC-11 — Scans 030–041, flags and cut points — unpursued implication / terminology comparison

**Anchor:** scan 030 “Drap”; scan 041 “Drap₂(L)”. The common word “drapeaux” occurs at three different levels: scan 030 uses flags of pieces in $\operatorname{Tr}(L)$, scan 041 uses two-point flags in $L$, and the supplied *Esquisse* 119/36 indexes spaces by flags in a poset $I$ of strata. The latter construction also retains spaces and maps of embeddings or proper fibrations, not just the incidence poset, and 119/37 replaces the index poset by a category for moduli multiplicities. **Context/relation:** adds a precise distinction to the suggested finite-category bridge; *Esquisse* 119/36–37 is an unchecked API transcription, used as supplied context. **Register:** `MPL_121_049-073+153+155 R121-08`, `MPL_150_044-084 N18`, `EXIT_ONE_TYPE P4e`, `STRATA B.1` (related warnings or claims, carried as register background only).

### REC-12 — Scans 040–041 versus the tame comparison programme — unpursued implication

**Anchor:** scan 040 “Alg. de Boole”; scan 041 “intervalle”. The supplied *Esquisse* 119/33–34 asks for comparison of isotopy categories and even the homotopy types of isomorphism spaces across tame theories, while 119/40–41 insists that choices should vary in contractible spaces. A finite subdivision or reconstruction of an underlying biorder proves none of those mapping-space or choice-independence assertions, and no result about simple homotopy follows on these sixteen pages alone. **Context/relation:** distinguishes the concrete interval model from the B10/compact tame–PL bridge proposed in `MPL_156-3/README.md`. **Register:** `MPL_150_001-043 Q4b`, `MPL_151_032-075 Q4-02`, `MPL_151_032-075 Q4-03`, `MPL_121_001-048 Q4.3`, `MPL_150_044-084 T05` are supplied research leads, not newly checked theorems; no outside literature was consulted.

### REC-13 — Scan 041 versus recognition of richer stratified objects — own idea / scope limitation

**Anchor:** “intervalle ... en ... que réseau”. Order reconstruction is particularly strong because the object being recovered is already assumed to be an ordered interval or tronçon; it does not justify recovering general stratified homotopy types from partitions alone. The supplied *Esquisse* 119/36 retains local retractions and attaching maps, and the register's `EXIT_ONE_TYPE P4e` explicitly warns that a coarse maquette can forget links. **Context/relation:** this is a reason to test S14 against attachment-sensitive examples before extrapolating the interval calculation; it adds a methodological limitation rather than proving another obstruction theorem. **Register:** `EXIT_ONE_TYPE P4e`, `PATHS E.10`, `MPL_121_049-073+153+155 R121-08`; **confidence:** high about the difference in supplied data, moderate as a research proposal because the full higher-dimensional “form” definition is not supplied in these sixteen pages.

### REC-14 — Scans 026–041, requested form/network/cutting/workshop dictionary — reading question / documentary scope

**Anchor:** scan 041 “réseau”; scan 040 “subdivision”. These sixteen pages explicitly develop ordered pieces, compatible moderate subsets, relative algebra, components and the reconstruction of a network interval; they do not introduce an “atelier” definition or compare four versions of *Analysis situs*. The sweep's chronology locates contrées in 156-4 and ateliers in 156-6/7, and its reports may guide a later study but cannot be promoted to a first-hand finding about absent manuscripts. **Context/relation:** answers the carry-question in `MPL_156-3/README.md` by separating what this packet can establish from what `sweep3/STUDY.md` reports. **Register:** `WG2 §3.1 #2` is related programme context; no supplied theorem ID settles the missing definitions or historical evolution on the basis of this packet.

## Appendix A. Explicit order recovery from strict betweenness

This checks the mathematical content of Hua's `156-3-order-from-betweenness` claim; it does not authenticate scans 012–014 or a historical attribution.

Let $P$ be a poset directed both upwards and downwards, with at least two elements, and dense in the strict sense: whenever $x<y$, there exists $z$ with $x<z<y$. Define

\[
B(x,y,z)\iff (x<y<z)\text{ or }(z<y<x).
\]

The comparability relation is recovered because, for distinct $x,z$,

\[
x\text{ and }z\text{ comparable}\iff\exists y\ B(x,y,z).
\]

There is at least one comparable pair: for distinct $x,y$, an upper bound of both is either equal to one of them or strictly greater than $x$. Choose one such unordered pair $\{a,b\}$ and choose the orientation $a<b$. Set, using only $B$,

\[
D_a=\{a\}\cup\{u:B(u,a,b)\},\qquad
U_b=\{b\}\cup\{v:B(a,b,v)\},
\]

and, for distinct $u,v$,

\[
I_B(u,v)=\{u,v\}\cup\{z:B(u,z,v)\}.
\]

With the chosen orientation, these are exactly $P_{\le a}$, $P_{\ge b}$, and the order interval between $u$ and $v$. In particular every $u\in D_a,v\in U_b$ satisfies $u<v$.

For $x\ne y$, define $x\prec y$ if there exist $u\in D_a,v\in U_b$ such that $x,y\in I_B(u,v)$ and

\[
x=u\quad\text{or}\quad y=v\quad\text{or}\quad B(u,x,y).
\]

**Forward implication.** If $x<y$, choose a common lower bound $u$ of $a,x$ and a common upper bound $v$ of $b,y$. Then $u\le x<y\le v$; if $x=u$ or $y=v$ the displayed test holds, and otherwise $B(u,x,y)$ holds.

**Reverse implication.** Since $u<v$ and both points lie in $[u,v]$, $x=u\ne y$ forces $x<y$, and $y=v\ne x$ forces $x<y$. In the remaining case, $B(u,x,y)$, with $y\ge u$, can only mean $u<x<y$, since its other orientation would give $y<x<u\le y$, impossible. Thus $\prec$ is precisely the strict original order, and its reflexive closure is the original partial order.

Any other order with the same $B$ can be globally reversed to orient $a<b$, after which this same formula recovers it. Therefore there are exactly the two opposite orientations when they are distinct, and at most that ambiguity always. Density is used only to recover comparability and find a usable anchor from $B$; if comparability is supplied separately, the formula works for any bidirected poset with a comparable pair. The strong strict-cone filtering hypotheses of the tronçon definition are not used here.

**Degenerate cases.** For an empty or singleton set there is only the trivial order and no meaningful orientation choice. A two-point total order is determined up to reversal by the supplied comparability relation, but cannot satisfy the strict density hypothesis; no uniqueness theorem for arbitrary two-point partial orders follows from the empty betweenness relation alone.

## Appendix B. Cut reconstruction, its assumptions, and a naive inverse limit

### B1. What the partition formula assumes

For a comparable pair $a<b$, define

\[
C(\{a,b\})=\{x\notin\{a,b\}: x\text{ comparable with both }a,b\}.
\]

As a set this is the disjoint union $P_{<a}\amalg(a,b)\amalg P_{>b}$, with empty parts omitted. Assume the model cut equivalence relation has precisely these nonempty parts as classes. This is the intended model reported in sweep §1.2 and reprised at scan 041; it is not a conclusion about arbitrary abstract relations $R_\varepsilon$.

For three pairwise comparable distinct points with $a<b<c$, the relevant classes are

\[
K_{ab}(c)=P_{>b},\quad K_{bc}(a)=P_{<b},\quad K_{ac}(b)=(a,c).
\]

The test at $b$ intersects the first two and is empty. At $a$, it intersects the first and third and gives $(b,c)$. At $c$, it intersects the second and third and gives $(a,b)$. Both outer intersections are nonempty in a dense order. Thus the model pair cuts recover strict betweenness using no orientation labels for the classes, even if the poset is not total. Together with Appendix A this yields reconstruction up to reversal under the stated hypotheses.

On the three-point set $\{a,b,c\}$, every total order has all pairs comparable and every pair cut has one remaining singleton. Hence all three betweenness structures (one for each possible middle point) have identical pair-cut data; this disproves the unrestricted discrete analogue.

The actual partitions as subsets of $P$, not their unordered sizes or isomorphism types, are required. For example all pair cuts in every endpoint-free dense linear order have three nonempty parts; counts alone contain no information about which of three given points is in the middle.

### B2. Non-total cut indexing need not be directed

Let $P=\mathbb Q\times\{0,1\}$ with $(q,i)<(r,j)$ exactly when $q<r$. It is directed in both directions, dense, and its nonempty strict cones are directed in the required opposite direction: if two points have levels greater than $q$, choose a rational level strictly between $q$ and the smaller of their levels; the dual construction handles lower cones. Therefore this is an admissible non-total model under the definition reported in the sweep.

The singleton cuts $\{(0,0)\}$ and $\{(0,1)\}$ are finite chains, but no finite chain contains their union. Thus the inclusion order of all finite-chain cuts has no common upper bound for those two indices. A pro-object construction might choose different indexing objects or maps, but the simplest “all finite cuts ordered by inclusion” candidate is not a cofiltered inverse-system index in this non-total model.

### B3. The extra $0^+$ thread on the real line

For each finite $S\subset\mathbb R$, let $E_S$ be the finite set of cells: singleton cut points, open intervals between consecutive cut points, and the two exterior open rays, with $E_\varnothing=\{\mathbb R\}$. If $S\subset T$, each $T$-cell lies in a unique $S$-cell, defining a coarsening map $E_T\to E_S$.

Choose $c_S\in E_S$ as follows: if $0\in S$, take the open cell immediately to the right of $0$; if $0\notin S$, take the unique open cell containing $0$. These cells are nonempty and contain all sufficiently small positive real numbers, so for $S\subset T$, $c_T\subset c_S$; therefore they give an element of $\varprojlim E_S$.

No point $x\in\mathbb R$ induces this thread. At the stage $S=\{0\}$, the chosen cell is $(0,\infty)$, forcing $x>0$; but then at the stage $S=\{x/2\}$, the chosen cell is $( -\infty,x/2)$, which does not contain $x$. Thus the naive set limit strictly contains the image of the real line. Adding finite-poset incidence relations while retaining these same coarsening maps does not change this calculation of the underlying set limit. One could instead mark the point threads, recognize threads that hit a singleton cell, or impose an appropriate realization or spatial condition, but none is supplied on scans 040–041.

## Context limits and nonclaims

- All *Esquisse* quotations and marker references come from the supplied, explicitly unchecked API transcription; this worker did not inspect its scans.
- The original scans 002–025 and the other cotes are not in this image packet and were not inspected; sweep reports of them are attributed reports.
- The terms Pasch, Hilbert, Huntington–Kline, Altwegg, Courcelle and Shiota occur in supplied context as leads; this run did not verify their publications, dates, theorem numbers or applicability by external research, and makes no new bibliographic claim.
- S14 and B10 are planning labels in `MPL_156-3/README.md`, not proved entries of `RESULTS_STATE.md`. The finite realization entries and prior research notes are carried with their stated provenance, not promoted to reviewed results.
- No reconstruction argument here proves a recognition theorem for arbitrary cut relations, a tame–PL comparison, an equivalence of isotopy categories, a result about simple homotopy, or a general stratified reconstruction theorem.
