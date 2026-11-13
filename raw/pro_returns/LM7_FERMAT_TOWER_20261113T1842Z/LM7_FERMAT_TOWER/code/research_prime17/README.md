# Retained exploratory record

The standalone final entry points are ../e_frattini17.gp and ../e_frattini17.py. They rebuild and verify all field/action/residue claims in E.59 without these exploratory files.

The original staged GP files use paths relative to the parent code directory: frattini_field.gp creates research_prime17/frattini_field.bin; frattini_residues.gp creates the second temporary binary; frattini_actions.gp then creates the coefficient certificate. The two generated binaries are reproducible and are not retained. All ordinary implementation-failure outputs and earlier-stage outputs are retained here.

small_units.gp, cross_ratio.gp and short_basis.gp record the search for the small explicit character. The nine conjugate short units together with zeta9 span only dimension eight; adding root3 and1-zeta9 does not enlarge that space. The final complete Kummer basis therefore retains the unconditionally certified fundamental units and prime generator, with actual coefficient vectors. The cross ratio itself is explicit and does not depend on those coordinate choices.

first_layers.gp/.out is a checkpoint of the broader radical-field exploration at17. It certifies the first pure and complex fields and the second pure field. Its second complex bnf computation had not completed at this checkpoint; no result from that unfinished call is used. The complete first complex norm transition is separately proved in E.57.
