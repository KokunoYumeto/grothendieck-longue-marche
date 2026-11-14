# F.11: rank-six centralizer and certified common kernel

## Result and precise scope

The new fragment is work/part_a/f_c5_kernel.tex, with metadata in f_c5_kernel_results.json.

It proves an exact replacement for the attempted C5 restriction detector:

\[
C_{P\Gamma_{0,12}}(C_5)=C_{P\Gamma_{0,12}}(D_{10})\cong F_6,
\qquad
C_{\widehat{P\Gamma}_{0,12}}(C_5)
=C_{\widehat{P\Gamma}_{0,12}}(D_{10})\cong\widehat F_6.
\]

On this actual subgroup, two of the twelve seven-point maps are constant. The other ten have one common kernel, with explicitly specified D10 conjugation maps on the targets. All twenty-four six-point maps factor through their corresponding seven-point maps. Hence the joint kernel of all thirty-six maps is exactly the kernel of one displayed configuration map:

\[
t\longmapsto (1,\zeta^2,\zeta^4,t,t\zeta,t\zeta^4,\infty).
\]

For the exact meridians recorded in the proof and certificate,

\[
w=[m_{\zeta^2},m_\zeta m_{\zeta^3}m_0]
\]

is a nontrivial element of that kernel. Its closure is the full \(\widehat{\mathbb Z}\). F.10 proves that this particular procyclic subgroup intersects the actual residual A5 centralizer trivially. F.7 therefore remains Open.

## Actual centralizer maps

The source is \(X_5=\mathbf P^1-\{0,\infty,\mu_5\}\), of rank six. The quotient cover is literally \(z\mapsto z^5\), with four downstairs punctures. Its group extension is \(F_{11}\triangleleft F_3\), of index five.

The proof supplies descent for every pure centralizing mapping class by normalizing the embedded conjugation group \(F_3\leq\operatorname{Aut}(F_{11})\). The deck quotient is fixed. Fifth powers at the two ramified cusps and the unramified cusp lifts retain the actual peripheral classes; unique roots in the discrete free group give the four downstairs peripheral classes. A.12's discrete Dehn–Nielsen–Baer map then gives the downstairs class. The pure kernel of descent is trivial because a nontrivial deck transformation permutes the free five-cycles.

Every pure downstairs class lifts. Choosing the lift that fixes the first labelled orbit makes the second orbit pure exactly for zero winding modulo five. This is precisely the connected degree-five covering \(t\mapsto t^5\) from \(X_5\), with the explicit family of all twelve points.

The same family has global labelled D10 transformations \(z\mapsto\zeta z\) and \(z\mapsto t/z\). This proves equality of the two discrete pure centralizers directly. The two unmarked order-two branch orbits of the D10 quotient can be exchanged by this centralizer; counting that quotient as a fully labelled three-branch-point configuration would miss this action.

The full induced topology is proved independently. Retain the two poles, all five first-orbit points, and one moving second-orbit point. This gives a point-pushing fibre. A.12 identifies its action after filling the moving point with inner conjugation on \(\widehat F_6\). Triviality of its centre proves that the completed source embeds. The already justified prime-order centralizer comparison in F.7 then identifies its image with the entire ambient completed C5 centralizer.

## Exact geometric labels and transports

The certificate c5_centralizer_labels_f11.py uses the same based coset enumeration as modular_a5_gt0_f7.py. The actual configuration is

- poles: label0 at0 and label10 at infinity;
- first orbit, in zeta order: labels 1,3,5,6,2;
- second orbit, in zeta order: labels 4,7,9,11,8.

With \(\theta=2\sin(2\pi/5)\), \(k=1-\theta^2\), \(t_0=k\zeta^2\), the exact Möbius maps

\[
a(z)=\frac{1-z}{1-z/k},\qquad b(z)=a(\zeta z)
\]

realize the specified abstract generators on these actual points. The code verifies all 720 point images and all 120 products by the two generators in the sixty-element group. It verifies the named normalizer involution and all ten \(d^k\tau^\epsilon\) transports, and lists the literal 24 six-set containments.

The straight source path from \(t_0\) to the braid base \(2+2i\) lies in the half-plane \(\operatorname{Re}t\geq2\). This fixes the actual basepoint and target transport, rather than selecting an unrelated abstract marking.

## Exact braid certificate

c5_seven_kernel_exact.py uses only Python fractions in the real quartic field

\[
\mathbb Q[\theta]/(\theta^4-5\theta^2+5),
\qquad \theta\in(19/10,2).
\]

The root is isolated by 128 rational bisections; every sign is proved by interval evaluation of its exact field representative. No floating-point operation occurs in the certificate.

The source base is \(2+2i\), the square radius is \(31/1000\), and the projection multiplier is \(1+371i/1000\). The four specified based square loops have six straight segments each.

Executed results:

- 24 source segments;
- 360 coordinate-pair checks;
- 58 simple, strictly ordered crossings;
- 2,530 exact field sign evaluations, including the final independently evaluated base order;
- individual meridian braid lengths 14,8,20,16;
- second commutator factor freely reduced length20;
- commutator braid freely reduced length48;
- exactly the six original generators after the faithful Artin substitution.

The initial producer count of 2,504 omitted the last 26 base-order sign calls from its summary; the current producer moves that query before recording the count. This bookkeeping adjustment changes no crossing, braid, identity, or mathematical conclusion.

Both producers were executed successfully. Their complete JSON outputs and captured stdout are adjacent to their code. C independently audited and reran both producers; the complete mathematical fragment is now ready for the further independent proof audit.

## Nontriviality and source comparison

Filling all source punctures except \(\zeta^2,\zeta,\infty\) kills the last two meridians in the second factor. The surviving pair has winding vectors \((1,0)\), \((0,1)\). Its commutator has integral Heisenberg central coordinate1, independently of its two meridian conjugators. Reduction modulo every prime power then detects the p-coordinate of every profinite power of \(w\). This proves the exact full procyclic assertion.

The actual full source embedding proves that this is also a nontrivial discrete pure mapping class upstairs. Applying F.10 is therefore legitimate. The proof does not identify a kernel of forgetting with the A5 centralizer.

## Primary source

The existing bibliography key A-Artin1947 suffices; no new bibliographic entry is required. I reopened the original scan:

https://webhomes.maths.ed.ac.uk/~v1ranick/papers/artinbraids.pdf

The projection-pattern isotopy lemma and Theorem3 on p.103 justify extracting the actual braid from the certified crossings. Theorem14 on p.112 and formulas14–15 on p.113 justify the faithful free-group substitution. The relevant primary pages were reread as web references turn810view0 and turn817view0.

The full topology and discrete filling arguments are the actual internal maps already proved in A.12 and F.7. No partial marked-cover injection theorem or generic closure/intersection rule is used.
