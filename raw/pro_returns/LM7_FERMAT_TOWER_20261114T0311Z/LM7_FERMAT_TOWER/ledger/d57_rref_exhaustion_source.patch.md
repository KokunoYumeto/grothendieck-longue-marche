--- pre_rref_exhaustion.py
+++ d_arithmetic_rank9_conjugators.py
@@ -80,6 +80,13 @@
          'quarter_turn_power':rec['quarter_turn_power'],
          'linear_constraint_rank':A.rank(),'consistent_over_Q':consistent}
    if consistent:
+    denominators=sorted({int(x.q) for x in rref})
+    two_parts=[d&-d for d in denominators]
+    assert max(two_parts)<=4
+    item.update({'rref_denominators':denominators,
+                 'maximum_two_primary_rref_denominator':max(two_parts),
+                 'exhaustive_free_residue_modulus':4,
+                 'integrality_constant_on_each_mod4_free_residue_class':True})
     piv=list(piv);free=[j for j in range(18) if j not in piv]
     found=None;attempts=0
     for vals in product(range(4),repeat=len(free)):
@@ -122,6 +129,8 @@
  'Z2_integral_conjugator_cases':sum(bool(r.get('integral_over_Z2')) for r in records),
  'all9_homology_columns_and_exact_cusp_checked_in_every_integral_case':True,
  'constraint_ranks':sorted({x['linear_constraint_rank'] for x in records}),
+ 'all_free_mod4_residue_tests_exhaustive':True,
+ 'maximum_two_primary_rref_denominator':max(x['maximum_two_primary_rref_denominator'] for x in records),
  'free_parameter_dimensions':sorted({x['free_parameter_count'] for x in records}),
  'fixed_cusp_lattice_rank':1,'actual_t12_class_is_primitive':True,
  'ordinary_H1_Qstar_UQ_vanishes':True,
