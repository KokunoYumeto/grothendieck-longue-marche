# Independent FGH audit of D.79

Status: independent full proof and executed-certificate PASS. This is a notes-only audit during checkpoint12's canonical-source freeze, not registration authority.

I read the complete `notes/de_sha_matrix_family_draft.tex`, all of its certificate source, the complete D78 proof and the relevant D77/D75 invariant calculations and canonical D35/D39 action formulas. The new argument uses actual integral arithmetic operators; no uncomputed high-weight beta coefficient is assigned a value.

## Actual images and the finite-localization kernel

For any invertible integral matrix M, its inertia columns at two and three generate the whole translation lattice. Thus the actual global operator image remains Z5² semidirect I0. Local completed Kummer cohomology has the same primitive κ(6) generator; multiplying its coefficient vector by M preserves primitiveness. D78's kernel-primitivity argument and actual local surjection therefore give the exact local line semidirect I0 after one integral monomial gauge. Coinduction identifies restriction with the inclusion of the constant Cartier module λ into the line module. D78's finite affine Chebotarev descent still applies to every finite everywhere-locally-trivial class. The upper bound is therefore for the actual inverse finite localization kernel, not merely for divisible local coefficients.

The geometric S3 maps genuinely permute peripheral directions. Their abelian Kummer formulas are (a,b)↦(b,a) and (a,b)↦(−a,b−a), with κ(−1)=0 at five. Transport of the unit tangential reference section has zero abelian class; the integral gauge compares the actual Alexander extensions and their finite coefficient systems. Hence reducing the positive-depth case to v5(α)=d and β a unit is legitimate. At most one of α,β,α−β is nonunit because (α,β) is primitive.

For d=0, D78's generator and its single finite ten-dimensional primitive module continue to work for arbitrary matrix coefficients. At two and three the constant primitive remains valid on the entire decomposition group because inertia fixes it and residual Frobenius is respectively2 or3. At five the three-jet primitive has unit cubic coefficient β(−α)(β−α)/48. The common finite coefficient level is preserved by integral substitutions and gauges. For d=∞, both λ and the exact axis line module have trivial cyclotomic-kernel action; the nontrivial order-four scalar kills H1(Γ,λ), giving the asserted injection by inflation–restriction.

## Finite positive depth: exact module structure

Set N=5^d and Q=z²((1+z)^N−1). It is a monic distinguished polynomial of degree N+2; modulo5 it is z^(N+2). Exact three-boundary factorization makes every cyclotomic-kernel multiplier minus one divisible by Q. A primitive local Soulé element makes that multiplier exactly Q times an integral unit. Thus the invariant annihilator is the whole ideal Q, including its integral lattice, rather than its rational saturation.

The primal sequence is

0 → QR/zQR → zR/zQR → R/QR → Z5 → 0.

Dualizing gives exactly D79.14. The map J→V need not be surjective; the retained final term is essential and is included. On Q the leading coefficient calculation gives χ² from the multiplier and χ³ from substitution, hence χ^5. Its Cartier dual has character χ^(−4). Since H0(Γ,λ)=H1(Γ,λ)=0, the entire restriction kernel embeds into (Q5/Z5(−4))^Γ=F5. This is a rigorous integral upper bound.

## Independent derivation of the interpolation coefficients

I independently expanded Sγ(t^r) through z²:

Sγ(t^r)=γ+γ(γ−1)r z/2+γ(γ−1)(r²(2γ−1)−3r)z²/12.

The beta two-jet contributes −αβ(γ²−1)z²/24. Subtracting γSγ(t^β), dividing the known integral factor t^N−1, and comparing constant and linear terms gives exactly

Aγ=−a0 γ²(γ−1)/2,

Bγ=a0 γ²(γ−1)(α(2γ−1)/12+N/4−β(7γ−5)/24).

The division by N in this coefficient calculation is only a rational calculation of an already integral quotient; the displayed results have exclusively five-adic unit denominators. Unknown higher beta coefficients enter the quotient only in z² or higher and vanish modulo Q. In particular both displayed coefficients vanish modulo5 when γ≡1 mod5. This confirms the claimed exact reduction without assuming any higher arithmetic coefficient.

## The all-depth exclusion and divisible-kernel step

For the actual element g=k^(4·5^(d−1)), χ(g)=2^(4·5^(d−1))≡1+3N modulo5N. In characteristic five and through degree N+2, substitution is z↦z+3z^N+3z^(N+1). The first nonconstant coefficient of Sγ(t^β) is 3β^(N−1)=3 in degree N−1. Terms of degree2N and above cannot contribute because N≥5. Applying the actual operator to z³ therefore produces the top defect (9+3)z^(N+2)=2z^(N+2). This calculation works for every d, independently of finite tests.

An order-five invariant Cartier functional must annihilate (χ(g)^−1ρ(g)−1)z³, so it vanishes on Q modulo5. Hence it maps trivially to the last term of D79.14. D77 gives J^Γ=(Q5/Z5)^d, a divisible abelian group. If V^Γ/J^Γ were the allowed nonzero F5, injectivity of divisible groups would split that short exact sequence and supply an actual order-five lift with nonzero last image. The actual-power calculation excludes precisely that lift. There is no invalid assumption that every torsion quotient has an order-five lift without the divisible-kernel argument.

The conclusion is the vanishing of the whole restriction kernel and therefore of S at positive finite depth. At all depths the rows of M and their difference are primitive, so global boundary divisibilities are zero. The D77 compact decomposition gives exactly the stated piecewise K and T=0. Completed matrix combinations are still unramified outside2,3,5. D74 applies only to nonempty section fibres; no new section-existence or separated-extension splitting claim occurs.

## Sources and scope

D79's new steps are proved algebraically on the page. Its arithmetic inputs are the already audited D31/D35/D39/D75–D78. During my D78 audit I freshly opened Milne, *Class Field Theory*, V Theorem3.23, printed164 (PDF172), https://www.jmilne.org/math/CourseNotes/CFT.pdf; that exact finite-image Chebotarev statement is the one used here. No stronger source theorem or conjectural arithmetic independence is introduced.

## Exact independent execution

I copied the complete certificate to `notes/fgh_D79_certificate.py`, executed it independently without modifying the author files, and retained `.json` and `.out`. Exit status0/PASS. The entire JSON equals the author output, including symbolic Aγ/Bγ identities, the actual-power/Lucas checks for depths1–6, independent residual quotient matrices for depths1–3, and all480 invertible matrices over F5. The all-depth conclusion is supplied by the proof above, not by extrapolation from those ranks.

Independent JSON SHA-256: `d67a16fd531bfa91c4e95ff274624f7946e471c04e9823302a0d4a433285fc65`.
