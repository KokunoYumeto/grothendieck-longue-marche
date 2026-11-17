# Structural comparison for the actual rho projection

This is a coordinate and source comparison, not a fifth monodromy census.

Put `r=rho(v,w)=w(v-1)/(1-w)`. On the actual surfaces the inverse formula is

\[
v=1-r+\frac r w,\qquad r\notin\{0,1\}.
\]

The actual source is literally `w=r`. For generic r the finite w-fiber
punctures are

\[
0,\quad1,\quad\frac r{r-1},\quad-r,\quad
\frac{u-r}{1-r},\quad\frac r{r+u-1},\quad u
\qquad(u\in\mu _5\setminus\{1\}).
\]

There are sixteen generic punctures. The groups of four entries are,
respectively, retained nonidentity product divisors, constant-family
deleted divisors, and moving-family deleted divisors. The diagonal has
equation `(w-1)(w+r)=0`; w=1 was already removed, so its additional point
is -r. The old product-one divisor becomes the omitted base value r=1.

The source `w=r` meets the additional fiber punctures at

* r=2 for v=0;
* r=u for the four moving-family holes;
* r=2-u for the four constant-family holes;
* r=1+-sqrt(1-u) for the eight nonidentity product holes.

Together with the old base holes0,1 these are exactly its original
nineteen holes. Thus its actual map to the r-base is F19 onto F2, with
seventeen extra source-hole meridians. Constant filling kills four;
both-family filling kills eight. The nine extra retained source holes
remain, so the original source is not a globally defined section over
the whole twice-punctured r-base.

Every r-fiber is a nonempty punctured plane; the map is locally trivial
away from finitely many coincidences of the displayed rational puncture
functions. No new list of all those coincidences or their braid actions
is claimed here. The usual based van Kampen construction may use a
generic sixteen-puncture fiber and the actual source crossing paths, but
it must still retain the old critical-fiber relations. Merely changing
the projection does not establish source-kernel surjectivity.

This model makes the previous sufficient-method obstruction transparent:
the product-one meridian is a base peripheral at r=1, while the omitted
source zero direction is the other independent base peripheral. A
single-direction induction requiring every source operator to fix that
peripheral modulo the deleted kernel cannot include the other base
direction. A structural argument could instead identify the entire
relative kernel in the generic-fiber image and then use its actual
monodromy invariance. That fiber-image equality is not supplied by the
coordinate change or by the all-positive controlled subgroup alone.
