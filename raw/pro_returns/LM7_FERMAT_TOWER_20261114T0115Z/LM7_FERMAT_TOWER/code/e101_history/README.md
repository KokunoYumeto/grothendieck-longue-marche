# Actual exploratory work preceding E.101

Every source and actual output in this directory is retained, including
representation errors, bounded searches with no hit, and timed-out certification.
The final portable proof is in the two e_unit_norm_*.gp files one directory up.

`unit_kummer_bnf.bin` is discovery data. Its BNF initialization completed and
was saved, but the certification command timed out after sixty seconds (exit124).
No theorem uses its displayed class group or the completeness of its units.
The literal reversed norm extracted with those candidate generators is checked
independently by rational polynomial identities in the final certificate.

`ordinary_unit_preimage.out` records 160 weighted ideal reductions without a
generator hit. The target ideal is proved principal by the exact class map and
the full ambiguous-class order27. This unsuccessful bounded search gives no
nonprincipality or non-norm conclusion.

Both original radical-upper BNF jobs were explicitly interrupted after their
requested arithmetic outputs had been superseded by proved class-field maps.
Their actual outputs and the successful lower-field results are preserved in
`superseded_bnf/`; the status JSON records exit130, not a completed certification.

Historical sources retain their actual workspace input paths. The final
five-stage driver has its own complete portable input routing and does not read
either unfinished upper BNF, the discovery BNF, or a historical failed output.
