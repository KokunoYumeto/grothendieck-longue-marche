#!/usr/bin/env python3
"""Structural TeX checks, not a replacement for a TeX-engine compile."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
names = ["ghost_results.tex", "ghost_compatibility.tex",
         "ghost_h2_counterexample.tex", "ghost_task_status.tex", "ghost_cup.tex",
         "ghost_localization.tex", "ghost_class3.tex", "ghost_local_rigidity.tex",
         "ghost_h1.tex", "ghost_class3_example.tex", "ghost_class3_original.tex",
         "ghost_elliptic_target.tex", "ghost_elliptic_arithmetic.tex",
         "ghost_elliptic_survival.tex", "ghost_generalized_jacobian.tex",
         "ghost_boundary_norms.tex", "ghost_boundary_local_norm.tex",
         "ghost_prefix_class3.tex", "ghost_dense_class3.tex",
         "ghost_prefix_topology.tex", "ghost_general_exponent.tex",
         "ghost_fixed_depth.tex", "ghost_unbounded_finite_failures.tex",
         "ghost_finite_failure_bound.tex", "ghost_a72_class3.tex",
         "ghost_finite_quotient_survival.tex", "main_orthogonal_ghost_audit.tex",
         "main_faithful_detector_audit.tex", "main_normalizer_ghost_audit.tex",
         "main_pure_orthogonal_corrections.tex", "main_finite_transport_fusion.tex",
         "main_mixed_braid_finite_target.tex", "main_mixed_central_recovery.tex",
         "main_sphere10_binary_fusion.tex", "main_sphere10_quaternary_fusion.tex",
         "main_sphere10_geometric_klein.tex",
         "main_sphere10_ordinary_centralizer_image.tex",
         "main_cm_discrepancy_family_supplement.tex",
         "main_cm_marking_fiber_product.tex",
         "main_fivepoint_signed_source_module.tex"]
labels, refs, cites = [], [], []
for name in names:
    text = "\n".join(re.split(r"(?<!\\)%", line)[0]
                     for line in (root/name).read_text().splitlines())
    stack = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        kind, env = match.groups()
        if kind == "begin":
            stack.append(env)
        else:
            assert stack and stack.pop() == env, (name, env, match.start())
    assert not stack, (name, stack)
    for left, right in [(r"\(", r"\)"), (r"\[", r"\]")]:
        assert text.count(left) == text.count(right), (name, left)
    depth = 0
    for match in re.finditer(r"(?<!\\)[{}]", text):
        depth += 1 if match.group() == "{" else -1
        assert depth >= 0, (name, match.start())
    assert depth == 0, (name, depth)
    labels += re.findall(r"\\label\{([^}]+)\}", text)
    refs += re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text)
    for group in re.findall(r"\\cite(?:\[[^]]*\])?\s*\{([^}]+)\}", text):
        cites += group.split(",")
    print(name, ": environments, math delimiters, and braces balanced")
assert len(labels) == len(set(labels)), "Duplicate label"
assert set(refs) <= set(labels), set(refs) - set(labels)
bib = (root/"ghost_references.bib").read_text()
parent_bib = root.parent/"GT_TOWER_CHECK"/"GT_TOWER_CHECK_references.bib"
if parent_bib.exists():
    bib += "\n" + parent_bib.read_text()
keys = set(re.findall(r"@\w+\{([^,]+),", bib))
assert set(cites) <= keys, set(cites) - keys
print("Unique labels:", len(labels), "; reference occurrences:", len(refs))
print("Citation keys present:", ", ".join(sorted(set(cites))))
print("PASS: structural checks only; the parent master supplies the TeX-engine compile.")
