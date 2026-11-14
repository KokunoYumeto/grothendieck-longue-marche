# D65: actual source extension and the divided integral orientation map

This is the current proof note, not a frozen theorem. The source and all
comparison maps are those of D58--D64. The new finite computations use the
actual marked graph over `(Z/4)[omega]/(omega^2+omega+1)`.

## 1. The two integral maps

Fix one of the two orbit-12 blocks. Write `M` for its integral compact
rank-16 coefficient lattice and `phi:M -> P_*` for the actual compact
small-cover map. Its reduction is the fixed D64 matrix. The actual
unordered stabilizer is `H`, of order 48. In Hermitian coordinates the
integral exterior action is

    B |-> M_g B bar(M_g)^t                 (g preserves the character),
    B |-> - M_g bar(B) bar(M_g)^t          (g exchanges the character).

The minus sign is necessary integrally. It follows directly on the
underlying coefficient basis `(1,omega)`: coefficient conjugation has
determinant -1. The executable real-wedge comparison is being retained
separately.

The actual graph calculation gives `N_H=0 mod 2` on the whole Hermitian
lattice. Consequently

    n(B mod 2) = (N_H(B)/2) mod 2

is independent of the integral lift. It annihilates every actual
stabilizer augmentation relation. On the D64 kernel `K` its descended
map has rank 6; its kernel on the ten-dimensional coinvariant space is
exactly the known four-dimensional source-s correction image.

For an ordinary coefficient-linear map `A:M -> ker(phi)` define

    d_A = Tr_H(A) = sum_{h in H} h A h^{-1}.

The actual full endomorphism trace is zero modulo 2. Thus

    k(A mod 2) = (d_A/2) mod 2

is well-defined, including the actual semilinear conjugations. On maps
to `ker(phi)` it has rank 16. For each of the four possible finite beta
framings, with actual rigid compact reduction `X`, the map

    A |-> k(A) Omega bar(X)^t + X Omega bar(k(A))^t

has rank 6 and precisely the image of `n`. Here
`Omega=bar(H_compact^{-1})` is the D64 actual reduced orientation
bivector. Complete columns and right inverses on all ten coinvariant
representatives are retained in `d_compact_divided_correction.json`.

## 2. Why this is an actual peripheral source correction

Let `G` be the actual arithmetic group, and `U` the integral homology of
its free source kernel. Let `E=Z_2[G]` be the Bass--Serre edge lattice.
There is the actual exact marked sequence

    0 -> U -> E -> Z_2[G/<s>] + Z_2[G/<r>] -> Z_2 -> 0.

Its path cocycle satisfies `p(s)=0` and `p(r)=e_1-e_r`.

The full global version of `d_A` factors as

    U -> M_global -> P -> L,

where `P` is a finite free `Z_2[G]`-lattice and
`L=ker(U^- -> U_*^-)`. The first map kills every cusp class and every
other compact summand. One explicit factorization takes the usual
coinduction map into `Z_2[G] tensor M_global`, and the induced map back
from an arbitrary integral lift of the one-character-pair map `A` into
`L`. Dividing that induced map by the odd unit `3^97` removes the
normal odd character-group multiplicity. Compactification of the
composite on the selected fibre is exactly `Tr_H(A)`. The lift into
`L` exists by the actual compact-kernel surjection D64.11.

The first map `j:U -> P` extends to `ell:E -> P`. Indeed the quotient
`E/U` is a free `Z_2`-lattice; `P` is a direct summand of a coinduced
lattice, so it is injective for this `Z_2`-split sequence. Equivalently
one extends the coefficient functionals across the split lattice and
uses the literal coinduction isomorphism. Put `w=ell(e_1)`.

Since `j` kills the full cusp homology, and the actual cusp has order 36
in `G`,

    N_t ell(p(t)) = ell(p(t^36)) = j([t^36]) = 0.

Restriction of `P` to `<t>` is free. Cyclic norm exactness therefore
supplies `b in P` with `ell(p(t))=(t-1)b`. The actual cocycle

    eta_P(g)=ell(p(g))+(1-g)b

then has `eta_P(t)=0`,

    eta_P(s)=(1-s)b,
    eta_P(r)=(1-r)(w+b),
    eta_P(n)=j([n]) for every n in the free kernel.

After `P -> L` this is the required cusp-fixed peripheral cocycle.
Lift its two conjugator coefficients through the proved surjection
`S57 -> L`. The resulting literal conjugators retain the maps to
`W_h` and the small class-two quotient. Their induced compact
homology change is exactly `d_A`, and the full homology change need
not be twice another integral map: its cusp component can be odd.

The reduction of the compact change is zero, while it kills all cusp
classes. The full homology map is therefore still invertible: in the
cusp/compact filtration it has the same diagonal reductions as the
old automorphism. All finite homology levels and their inverse limit
retain these actual two conjugators.

## 3. The literal integral orientation identity

Choose actual full-source lifts of the current conjugators. Their cusp
defect has zero integral abelianization, so it has a class `z_int` in
the integral class-two commutator lattice. The usual marked surface
boundary word, applied before reduction, gives

    N_G(z_int)_compact = T Omega_int bar(T)^t - Omega_int.

This is the integral version of the D55 proof: each conjugated cusp
contributes the sum over its 36 powers; the sum over cusp cosets is
the full group norm. Terms involving the conjugator and a cusp
homology class vanish after compactification. The commutator product
on the other side is the actual integral orientation bivector.

On the selected induced block the left side is `3^97 N_H` after the
literal coinvariant identification. The factor is an odd integral
unit. Divide by 2 and reduce modulo 2. Replacing `T` by `T+d_A`
changes the result by

    k(A) Omega bar(X)^t + X Omega bar(k(A))^t.

No value of the unknown integral `T` is substituted: only its already
proved rigid reduction `X` and the actual reduced orientation are
needed. The quadratic term has a factor 4 and disappears at this
specific reduction.

The retained rank-six right inverse can therefore be applied to the
actual class `n(z)` to choose an actual source correction. After that
choice, the residual coinvariant class lies in the exact rank-four
source-s image and is removed by the D64 source-s words. The ensuing
ordinary augmentation correction removes the whole compact block.

## 4. Remaining checks before freezing

The numerical statements above are proved by the current exact
certificates. The draft theorem must still spell out the comparisons
with `X64` and `Y`, including reapplying the earlier central moving
correction after the new source-s words. All earlier compact summands
are unchanged by the first projective-factor correction. The
intermediate full `Y` homology action changes by the displayed actual
cocycle; it is not claimed to remain pointwise unchanged.

The expected new central quotient retains the full two blocks `C2`
and `C3`, replacing only their earlier four-dimensional retractions.
Its extra dimension over D64 is `5760-8=5752`; its extra coinvariant
dimension is `12`. These counts are not a claim of full profinite
realization.
