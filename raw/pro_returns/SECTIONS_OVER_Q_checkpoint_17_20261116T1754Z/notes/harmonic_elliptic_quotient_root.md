# Exact elliptic quotient of the product-root curve

Work in progress toward A10; no rank or Tate–Shafarevich assertion has been made.

On the proper model of W^4=T(T−1)(T−1/2)/a put u=2T−1. Then W^4=(u^3−u)/(8a). The actual rational automorphism r:(u,W)→(−1/u,W/u) has order four and square (u,W)→(u,−W). It exchanges the boundary pairs T=0,1 and T=1/2,infinity. Its nonidentity square fixes exactly those four points; r and r^3 have no fixed points, so its quotient has genus one by Riemann–Hurwitz.

The invariant functions x=u−1/u and z=W²(u²+1)/u² satisfy z²=x(x²+4)/(8a). The inverse field reconstruction is u²−xu−1=0 and W²=z u²/(u²+1), giving degree at most four; the faithful order-four action gives equality. This is therefore the actual quotient morphism after proper normalization. Taking x_E=(a/2)x and y_E=a²z gives y_E²=x_E³+a²x_E.

For the exact A134 constants, a=573q² with q=325596479663/72962. The change x_E=q²X, y_E=q³Y gives E_573: Y²=X³+573²X. Its degree-two isogeny target is Y²=X³−1146²X. Rank and Sha need a proved computation or verified primary theorem and remain unchecked here.

The symbolic invariant equations were executed with SymPy and passed. Direct exhaustive integer enumeration of 573=4x²+y²+bz² gave the following counts: {8: 64, 32: 32}. No theorem has yet been applied to these counts.

Primary-source check,16November2026: J.B.Tunnell, A Classical Diophantine Problem and Modular Forms of Weight3/2, Inventiones Mathematicae72(1983),323–334, opened at https://sites.math.rutgers.edu/~zeilberg/EM22/JT1983.pdf . The introduction defines the q-product and the remark following Theorem1 records it; Theorem1 itself gives the signed theta expansion. Theorem3 on printed328–329 gives L(E^(2d),1)=b(d)² beta/(2 sqrt(2d)) for odd squarefree d. Here d=573=3·191 is squarefree. The independent q-product calculation gives b(573)=0 exactly, so this specific central L-value is zero. No converse or conditional rank theorem is used. The certificate is code/harmonic_elliptic_quotient_certificate.py with its actual output retained. This observation rules out applying the nonzero central-value criterion to this elliptic quotient.
