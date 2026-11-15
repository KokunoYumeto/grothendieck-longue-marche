# A local rank-one χ-trivialisation model

**Status:** an editorial calculation made after the transcription freeze. It neither changes doubtful readings nor supplies the missing global hypotheses. Sources motivating it are cote 84, scans 146, 164, 168, and 170; it bears on Hua, findings register, 84-chi-trivialised-extension-product, as quoted in the supplied RESULTS_STATE register.

Let R be any commutative ring, χ∈R, and fix the endpoints L=M=R. A split extension E=Rℓ⊕Rx with α(1)=ℓ and ψ(x)=1 has a χ-trivialisation of the displayed complementary form

\[
\pi=(\chi,\tau),\qquad \varpi=\binom{-\tau}{\chi}.
\]

Thus απ+ϖψ=χ id, πα=χ, ψϖ=χ and πϖ=0. In a new splitting x′=x+aℓ, the coordinate changes by τ′=τ+χa; the script checks conjugation of both endomorphisms απ and ϖψ. This convention is a choice for the calculation, not a silent resolution of every manuscript sign.

Define a groupoid Gχ(R) whose objects are τ∈R and whose arrows a:τ→τ+χa compose by addition. As an actual map between the two represented extensions, this arrow has matrix F=[[1,−a],[0,1]]: it satisfies π_target F=π_source and Fϖ_source=ϖ_target; the change-of-basis matrix instead has +a. Arrows remain distinct when χa=0, so this is a groupoid with automorphisms Ann_R(χ), not merely the set R/χR. Put

\[
\tau\star\sigma=\tau\sigma,
\qquad
(\tau,a)\star(\sigma,b)
=(\tau\sigma,\,a\sigma+\tau b+\chi ab).
\]

The target equation is

\[
(\tau+\chi a)(\sigma+\chi b)
=\tau\sigma+\chi(a\sigma+\tau b+\chi ab).
\]

The script checks compatibility with composition, strict associativity, symmetry, identity arrows and the unit object 1 as polynomial identities over Z[χ,τ,σ,…]. For example, both triple products have arrow coordinate

\[
a\sigma\rho+\tau b\rho+\tau\sigma c
+\chi(ab\rho+a\sigma c+\tau bc)+\chi^2abc.
\]

An object τ is invertible up to isomorphism precisely when there exist σ,a with τσ+χa=1: this is exactly the ideal condition (τ,χ)=R, or the statement that τ mod χ is a unit in R/χR. Necessity follows because an isomorphism of τσ with 1 is such an arrow, and sufficiency gives the inverse object σ and the required arrow directly; commutativity supplies the inverse on the other side. Multiplication by τ on Ann_R(χ) is then invertible as well: if τσ+χa=1, multiplication by σ is its inverse on that annihilator.

This calculation gives a concrete local mechanism behind the context's coefficient-product and invertibility clauses. To pass to varying line bundles and a scheme one must construct the relevant stack/descent data, identify exactly the category of allowed morphisms, and verify that the manuscript's global pushout product induces this local law. It says nothing by itself about whether the separately drawn pullback product agrees through a map inducing the identity on both endpoints; the χ=0 sign test in the early-page analysis concerns that distinct question.
