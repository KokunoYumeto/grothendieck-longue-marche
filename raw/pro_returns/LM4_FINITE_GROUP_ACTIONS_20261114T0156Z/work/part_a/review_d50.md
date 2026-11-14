# Independent audit of D.50

PASS. I read the whole TeX fragment and reran `torus_two_subgroups_d50.py` successfully.

The use of D.33 is precise: the named homology map to `GL2(Z2)` is injective on each finite 2-subgroup and bounds its order by eight. An order-eight matrix would have a primitive eighth-root eigenvalue, impossible in dimension two over `Q2`; the shifted cyclotomic polynomial is Eisenstein. Every order-four matrix has minimal polynomial `X²+1` and square `−I`.

An exponent-two subgroup is simultaneously diagonalizable and has order at most four. In order eight, an order-four subgroup is normal and its centralizer is exactly that subgroup because the matrix centralizer is the field `Q2(i)` and has at most four 2-power torsion elements. The remaining generator inverts it. The quaternion alternative reduces to `a²+b²=−1`. The minimum-valuation proof covers negative valuations and zero entries: both units give odd valuation one, while one unit forces minimum valuation zero and the contradiction modulo four. Thus only `D8` remains at order eight.

The actual maps `r(x)=y,r(y)=x⁻¹` and `s(x)=y,s(y)=x` satisfy all displayed word relations and preserve the specified commutator class with multipliers `+1` and `−1`. Eight distinct homology matrices establish the outer injection. The program verifies the maps and all48 unit-residue cases modulo eight.

The multiplier deductions use D.43 only on involutions. A positive involution has matrix `−I`, so it is unique within a finite 2-subgroup; this gives the V4 and D8 global signs. An arbitrary cyclic C4 generator retains only the stated square and dyadic restrictions. No conjugacy or further multiplier claim is inferred.
