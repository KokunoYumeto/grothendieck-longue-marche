# E76 scope clarification for the frozen proof

The intended certified based-automorphism assertion in E76 is for
`g in {2,3,4}`. The actual finite surface-cover assertions use only
`(g,L)=(2,S3),(3,S3),(2,S4)`.

After the frozen package replay, the first sentence of the statement
should therefore begin:

> For g in {2,3,4}, let V_g=F(u_1,...,u_{2g}), and put ...

The literal inverse, presentation, boundary and capping certificates
cover precisely those three genera. Every map, relation and finite
fibre assertion printed later in E76 lies within that range. This
clarification makes no assertion for additional genera and changes
none of the retained programs or certificate arrays.

The frozen package remains unchanged while the root replay runs.
