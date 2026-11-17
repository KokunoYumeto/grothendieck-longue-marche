#!/usr/bin/env python3
"""Assemble audited contributions and retain their source snapshots."""
from pathlib import Path
import re,shutil

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/"work"
SNAP=ROOT/"notes"/"source_fragments"
SNAP.mkdir(parents=True,exist_ok=True)
if WORK.exists():
    for p in WORK.iterdir():
        if p.is_file() and p.suffix in {".tex",".md",".bib"}:
            shutil.copy2(p,SNAP/p.name)
    for d in ("centralizer_code","tower_code","ghost_code"):
        if (WORK/d).exists():
            for p in (WORK/d).iterdir():
                if p.is_file():shutil.copy2(p,ROOT/"code"/p.name)

# New coefficient-four programs retain their own directory and all failures.
for dirname in ("ghost_mod4","centralizer_mod4"):
    if (WORK/dirname).exists():
        shutil.copytree(WORK/dirname,ROOT/"code"/dirname,dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__"))

mapping={
 "prop:ghost-finite-support":"C.1.1",
 "prop:ghost-infinite-ramification":"C.1.2",
 "lem:ghost-higher-z1":"C.1.3",
 "lem:ghost-hall-model":"C.1.4",
 "lem:ghost-primitive-family":"C.1.5",
 "prop:ghost-compact-fibres":"C.1.6",
 "thm:ghost-fixed-pair-compatible":"C.1.7",
 "prop:ghost-h2-691":"C.1.8",
 "cor:ghost-integral-extension":"C.1.9",
 "prop:ghost-uncountable-kernel":"C.1.10",
 "prop:ghost-ordinary-cup":"C.1.11",
 "cor:ghost-class2-lift":"C.1.12",
 "thm:ghost-strict-localization":"C.1.13",
 "prop:ghost-tame-cochain":"C.1.14",
 "prop:ghost-class3-residue":"C.1.15",
 "prop:ghost-1129-unramified":"C.2.4",
 "lem:ghost-magnus-conjugacy":"C.1.16",
 "prop:ghost-local-boundary":"C.1.17",
 "prop:ghost-h1-weight2":"C.1.18",
 "cor:ghost-class2-fibre24":"C.1.19",
 "lem:ghost-prefix-five":"C.1.20",
 "lem:ghost-finite-prefix-determines":"C.1.21",
 "thm:ghost-first-integral-class3":"C.2.5",
 "thm:ghost-original-first-integral-class3":"C.2.6",
 "thm:ghost-passing-first-class3":"C.2.7",
 "thm:ghost-dense-class3":"C.2.8",
 "cor:ghost-open-dense-class3":"C.2.9",
 "lem:ghost-variable-exponent-image":"C.2.10",
 "thm:ghost-general-exponent-arithmetic":"C.2.11",
 "thm:ghost-fixed-depth-survival":"C.2.12",
 "thm:ghost-unbounded-finite-failures":"C.2.13",
 "lem:ghost-weighted-augmentation":"C.2.14",
 "prop:ghost-finite-local-bound":"C.2.15",
 "cor:ghost-selected-failure-bound":"C.2.16",
 "thm:ghost-finite-quotient-survival":"C.2.17",
 "thm:ghost-a72-first-class3":"C.2.18",
 "lem:two-orthogonal-radicals":"A.4.16",
 "lem:orthogonal-centralizer-determinant":"A.4.17",
 "lem:orthogonal-centralizer-spinor":"A.4.20",
 "prop:orthogonal-first-order-joint-normalizer":"A.4.21",
 "prop:ghost-elliptic-target":"C.3.1",
 "prop:ghost-elliptic-selmer":"C.3.2",
 "prop:ghost-elliptic-h1":"C.3.3",
 "prop:ghost-elliptic-support-test":"C.3.4",
 "prop:ghost-elliptic-passing":"C.3.5",
 "lem:ghost-elliptic-two-fibre":"C.3.6",
 "prop:ghost-genjac-image":"C.3.7",
 "prop:ghost-boundary-hasse-norm":"C.3.8",
 "prop:ghost-original-genjac-survival":"C.3.9",
 "prop:ghost-all-passing-genjac":"C.3.10",
 "cor:ghost-metabelian-cover-exclusion":"C.3.11",
 "prop:ghost-a65-limit":"C.2.1",
 "thm:ghost-factorial-selmer32":"C.2.2",
 "prop:ghost-a196-scope":"C.2.3",
 "prop:birman-cyclic-fibre-detector":"A.4.33",
}
def convert_numbered(text):
    pattern=r"\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[([^\]]*)\])?\s*\\label\{([^}]+)\}"
    def sub(m):
        env,title,label=m.groups()
        if label not in mapping:raise ValueError("Unmapped statement "+label)
        return rf"\begin{{result}}{{{mapping[label]}}}{{Proved}}{{{title or env.title()}}}"+"\n"+rf"\label{{{label}}}"
    text=re.sub(pattern,sub,text)
    text=re.sub(r"\\end\{(?:theorem|lemma|proposition|corollary)\}",r"\\end{result}",text)
    return text
for src,dst in {
 "centralizer_a1.tex":"part_a_centralizers.tex",
 "centralizer_harmonic.tex":"part_a_harmonic.tex",
 "centralizer_distribution.tex":"part_a_distribution.tex",
 "centralizer_b1.tex":"part_b_descent_proofs.tex",
 "centralizer_cyclic_descent.tex":"part_b_cyclic_descent.tex",
 "centralizer_dihedral_quotients.tex":"part_b_dihedral_quotients.tex",
 "centralizer_genus_two_quotient.tex":"part_b_genus_two_quotient.tex",
 "root_origami_covariance.tex":"part_b_origami_covariance.tex",
 "root_descent_characters.tex":"part_b_descent_characters.tex",
 "centralizer_relative_obstruction.tex":"part_b_relative_obstruction.tex",
 "centralizer_kernel_source_refinement.tex":"part_b_kernel_source_refinement.tex",
 "centralizer_second_character.tex":"part_b_second_character.tex",
 "centralizer_descent_image.tex":"part_b_descent_image.tex",
 "centralizer_universal_source.tex":"part_b_universal_source.tex",
 "centralizer_universal_source_144.tex":"part_b_universal_source_144.tex",
 "centralizer_universal_word_lift.tex":"part_b_universal_word_lift.tex",
 "centralizer_universal_positive_lift.tex":"part_b_universal_positive_lift.tex",
 "centralizer_infinite_central_image.tex":"part_b_infinite_central_image.tex",
 "centralizer_universal_central_kernel.tex":"part_b_universal_central_kernel.tex",
 "centralizer_open_descent_image.tex":"part_b_open_descent_image.tex",
 "centralizer_finite_central_detector.tex":"part_b_finite_central_detector.tex",
 "centralizer_cusp_centralizer.tex":"part_b_cusp_centralizer.tex",
 "centralizer_finite_descent_obstruction.tex":"part_b_finite_descent_obstruction.tex",
 "centralizer_finite_base_reduction.tex":"part_b_finite_base_reduction.tex",
 "centralizer_relation_module_bounds.tex":"part_b_relation_module_bounds.tex",
 "centralizer_small_central_detectors.tex":"part_b_small_central_detectors.tex",
 "centralizer_ternary_obstruction_vanishes.tex":"part_b_ternary_obstruction_vanishes.tex",
 "centralizer_binary_obstruction_vanishes.tex":"part_b_binary_obstruction_vanishes.tex",
 "centralizer_infinite_characters.tex":"part_b_infinite_characters.tex",
 "centralizer_fixed_lifting.tex":"part_b_fixed_lifting.tex",
 "centralizer_fixed_frame_test.tex":"part_b_fixed_frame_test.tex",
 "centralizer_harmonic_character.tex":"part_b_harmonic_character.tex",
 "centralizer_harmonic_kernel.tex":"part_b_harmonic_kernel.tex",
 "centralizer_two_character_shifts.tex":"part_b_two_character_shifts.tex",
 "centralizer_perfect_source_factor.tex":"part_b_perfect_source_factor.tex",
 "centralizer_prime_characters.tex":"part_b_prime_characters.tex",
 "centralizer_full_harmonic_formula.tex":"part_b_full_harmonic_formula.tex",
 "centralizer_e49_repair.tex":"part_a_label_repair.tex",
 "tower_bridge.tex":"part_a_tower.tex",
 "tower_completion.tex":"part_a_completion.tex",
 "tower_finite_cubic.tex":"part_a_finite_cubic.tex",
 "tower_finite_embedding.tex":"part_a_finite_embedding.tex",
 "tower_marking_core.tex":"part_a_marking_core.tex",
 "tower_modular_centralizer_finite.tex":"part_a_modular_centralizer.tex",
 "tower_finite_graph_lemma.tex":"part_a_finite_graph.tex",
 "tower_translation_centralizer_finite.tex":"part_a_translation_centralizer.tex",
 "tower_translation_peripheral_lift.tex":"part_a_translation_peripheral_lift.tex",
 "tower_modular_surface_realization.tex":"part_a_modular_surface_realization.tex",
 "tower_finite_deck_reconstruction.tex":"part_a_finite_deck_reconstruction.tex",
 "tower_quaternion_surface_detector.tex":"part_a_quaternion_surface_detector.tex",
 "tower_quaternion_deck_reconstruction.tex":"part_a_quaternion_deck_reconstruction.tex",
 "tower_quaternion_homology_detector.tex":"part_a_quaternion_homology_detector.tex",
 "tower_quaternion_geometric_image.tex":"part_a_quaternion_geometric_image.tex",
 "tower_quaternion_faithful_detector.tex":"part_a_quaternion_faithful_detector.tex",
 "main_orthogonal_ghost_audit.tex":"part_a_orthogonal_lemmas.tex",
 "tower_faithful_extension_split.tex":"part_a_faithful_extension_split.tex",
 "main_normalizer_ghost_audit.tex":"part_a_normalizer_lemmas.tex",
 "tower_compact_ordinary_normalizer.tex":"part_a_compact_ordinary_normalizer.tex",
 "main_pure_orthogonal_corrections.tex":"part_a_pure_orthogonal_corrections.tex",
 "tower_joint_peripheral_input.tex":"part_a_joint_peripheral_input.tex",
 "main_finite_transport_fusion.tex":"part_a_finite_transport_fusion.tex",
 "tower_finite_braid_bridge.tex":"part_a_finite_braid_bridge.tex",
 "tower_local_mixed_image.tex":"part_a_local_mixed_image.tex",
 "main_mixed_central_recovery.tex":"part_a_mixed_central_recovery.tex",
 "main_sphere10_binary_fusion.tex":"part_a_sphere10_binary_fusion.tex",
 "tower_sphere10_class3.tex":"part_a_sphere10_class3.tex",
 "main_sphere10_quaternary_fusion.tex":"part_a_sphere10_quaternary_fusion.tex",
 "main_sphere10_joint_quotient.tex":"part_a_sphere10_joint_quotient.tex",
 "tower_birman_cyclic_detector.tex":"part_a_birman_cyclic_detector.tex",
 "tower_finite_klein_centralizer.tex":"part_a_finite_klein_centralizer.tex",
 "tower_finite_klein_fusion.tex":"part_a_finite_klein_fusion.tex",
 "main_sphere10_geometric_klein.tex":"part_a_sphere10_geometric_klein.tex",
 "tower_finite_pentagon_action.tex":"part_a_finite_pentagon_action.tex",
 "main_sphere10_ordinary_centralizer_image.tex":"part_a_ordinary_centralizer_image.tex",
 "tower_finite_e44_comparison.tex":"part_a_finite_e44_comparison.tex",
 "tower_finite_genus_one_action.tex":"part_a_finite_genus_one_action.tex",
 "centralizer_odd_target_survivors.tex":"part_a_odd_target_survivors.tex",
 "main_finite_cm_forgetting_discrepancy.tex":"part_a_cm_forgetting_discrepancy.tex",
 "centralizer_reversed_binary_obstruction.tex":"part_a_reversed_binary_obstruction.tex",
 "tower_cubic_orbit_orbifold.tex":"part_a_cubic_orbit_orbifold.tex",
 "centralizer_ternary_fivepoint_retraction.tex":"part_a_ternary_fivepoint_retraction.tex",
 "tower_configuration_fixed_locus.tex":"part_a_configuration_fixed_locus.tex",
 "tower_effective_configuration_recognition.tex":"part_a_effective_configuration_recognition.tex",
 "main_fivepoint_signed_source_module.tex":"part_a_fivepoint_signed_source_module.tex",
 "centralizer_ternary_harmonic_survivor.tex":"part_a_ternary_harmonic_survivor.tex",
 "centralizer_odd_refinement_harmonic.tex":"part_a_odd_refinement_harmonic.tex",
 "centralizer_mixed_mod6_identity.tex":"part_a_mixed_mod6_identity.tex",
 "tower_finite_configuration_fusion.tex":"part_a_finite_configuration_fusion.tex",
 "main_fivepoint_common_kernel.tex":"part_a_fivepoint_common_kernel.tex",
 "root_involution_configuration_recognition.tex":"part_a_involution_configuration_recognition.tex",
 "tower_finite_branch_output.tex":"part_a_finite_branch_output.tex",
 "ghost_diagonal_disk_parameter.tex":"part_a_diagonal_disk_parameter.tex",
 "centralizer_common_mod6_canonical_survivor.tex":"part_a_common_mod6_canonical_survivor.tex",
 "root_involution_configuration_fusion.tex":"part_a_involution_configuration_fusion.tex",
 "ghost_common_quartic_kernel.tex":"part_a_common_quartic_kernel.tex",
 "centralizer_involution_marking.tex":"part_a_involution_marking.tex",
 "centralizer_common_mod12_survivor.tex":"part_a_common_mod12_survivor.tex",
 "B25_audit.tex":"part_b_arrows.tex",
 "ghost_results.tex":"part_c_results.tex",
 "ghost_compatibility.tex":"part_c_compatibility.tex",
 "ghost_h2_counterexample.tex":"part_c_h2.tex",
 "ghost_cup.tex":"part_c_cup.tex",
 "ghost_localization.tex":"part_c_localization.tex",
 "ghost_class3.tex":"part_c_class3.tex",
 "ghost_local_rigidity.tex":"part_c_local_rigidity.tex",
 "ghost_h1.tex":"part_c_h1.tex",
 "ghost_class3_example.tex":"part_c_class3_example.tex",
 "ghost_class3_original.tex":"part_c_class3_original.tex",
 "ghost_elliptic_target.tex":"part_c_elliptic_target.tex",
 "ghost_elliptic_arithmetic.tex":"part_c_elliptic_arithmetic.tex",
 "ghost_elliptic_survival.tex":"part_c_elliptic_survival.tex",
 "ghost_generalized_jacobian.tex":"part_c_generalized_jacobian.tex",
 "ghost_boundary_norms.tex":"part_c_boundary_norms.tex",
 "ghost_boundary_local_norm.tex":"part_c_boundary_local_norm.tex",
 "ghost_prefix_class3.tex":"part_c_prefix_class3.tex",
 "ghost_dense_class3.tex":"part_c_dense_class3.tex",
 "ghost_prefix_topology.tex":"part_c_prefix_topology.tex",
 "ghost_general_exponent.tex":"part_c_general_exponent.tex",
 "ghost_fixed_depth.tex":"part_c_fixed_depth.tex",
 "ghost_unbounded_finite_failures.tex":"part_c_unbounded_finite_failures.tex",
 "ghost_finite_failure_bound.tex":"part_c_finite_failure_bound.tex",
 "ghost_finite_quotient_survival.tex":"part_c_finite_quotient_survival.tex",
 "ghost_a72_class3.tex":"part_c_a72_class3.tex",
}.items():
    p=SNAP/src
    if not p.exists():continue
    t=p.read_text()
    if src=="tower_finite_braid_bridge.tex":
        extra=(SNAP/"main_mixed_braid_finite_target.tex").read_text()
        head,tail=t.rsplit(r"\end{proof}",1)
        t=head+"\n"+extra+"\n"+r"\end{proof}"+tail
    if src in {"centralizer_a1.tex","centralizer_harmonic.tex",
               "tower_sphere10_class3.tex","tower_birman_cyclic_detector.tex",
               "tower_finite_klein_centralizer.tex","tower_finite_klein_fusion.tex"}:
        t=t.replace("A.C","A.T")
    if src in {"tower_bridge.tex","tower_completion.tex","B25_audit.tex"}:
        t=t.replace(r"\section{",r"\subsection{")
    t=t.replace(r"\begin{statement}",r"\begin{result}").replace(r"\end{statement}",r"\end{result}")
    if src.startswith("ghost_") or src in {"main_orthogonal_ghost_audit.tex", "main_normalizer_ghost_audit.tex", "tower_birman_cyclic_detector.tex"}:t=convert_numbered(t)
    (ROOT/dst).write_text(t)

status=(SNAP/"ghost_task_status.tex").read_text()
status=status.split(r"\paragraph{Lead 3")[0]
chunks=re.split(r"\\subsection\*\{C\.([123])\. ([^\n]+)\}\s*",status)
out=chunks[0]
for i in range(1,len(chunks),3):
    num,title,body=chunks[i:i+3]
    title=title.split("---")[0].strip()
    out+=rf"\begin{{result}}{{C.{num}}}{{Open}}{{{title}}}"+"\n"+body+"\n"+r"\end{result}"+"\n"
(ROOT/"part_c_status.tex").write_text(out)

# A list of all statement IDs with exact titles is a reproducible audit
# of numbering.  Semantic dependencies are added in the separate ledger.
rows=[]
for p in sorted(ROOT.glob("part_*.tex")):
    for m in re.finditer(r"\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{",p.read_text()):
        t=p.read_text();start=m.end();depth=1;j=start
        while depth and j<len(t):
            if t[j]=="{" and t[j-1]!="\\":depth+=1
            elif t[j]=="}" and t[j-1]!="\\":depth-=1
            j+=1
        rows.append((m.group(1),m.group(2),t[start:j-1],p.name))
ids=[r[0] for r in rows]
assert len(ids)==len(set(ids)),[x for x in ids if ids.count(x)>1]
(ROOT/"notes"/"statement_inventory.tsv").write_text(
    "id\tstatus\ttitle\tfile\n"+"\n".join("\t".join(r) for r in rows)+"\n")
for p in ROOT.glob("part_*.tex"):
    t=p.read_text()
    def move_tag(m):
        body=m.group(1)
        tags=re.findall(r"\\tag\{[^}]+\}",body)
        if not tags:return m.group()
        assert len(tags)==1
        return r"\begin{split}"+body.replace(tags[0],"")+r"\end{split}"+tags[0]
    t=re.sub(r"\\begin\{split\}([\s\S]*?)\\end\{split\}",move_tag,t)
    t=re.sub(r"(?<![A-Za-z\\])(qquad|quad)\b",lambda m:"\\"+m.group(),t)
    p.write_text(t)
print("Assembled contributions; numbered statements:",len(rows))
