#!/usr/bin/env python3
"""Build the Part B statement ledger from the actual saved LaTeX."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
tex = ROOT / 'sections' / 'B.tex'
data = tex.read_text()
spec = {
  1: (['B(b)', 'cote143.4-5'], ['B_StixCuspidal'], 'The semi-abelian embedding hypothesis is retained; G(k) itself is not asserted finitely generated.'),
  2: (['B(b)'], ['B_Koenigsmann'], 'The Hahn field is explicitly not finitely generated over Qp and is not a counterexample to B(d) in that field class.'),
  3: (['B(a)', 'F(g)(1)'], ['B_Deligne', 'B_StixCuspidal'], 'The tangent/uniformizer sign convention is fixed in the proof; the global intrinsic recognition problem belongs to F(g).'),
  4: (['B(a)'], ['B_Deligne'], 'Trace of logarithmic forms and determinant norm of differentials are typed separately and both formulas are proved.'),
  5: (['B(a)'], ['B_StixCuspidal'], 'Finitely generated characteristic-zero base field; positive genus, including the entire one-cusp collapse.'),
  6: (['B(a)'], ['B_StixCuspidal'], 'Finitely generated characteristic-zero base field; counts only rational point/cusp domain. In an anisotropic conic that domain is empty.'),
  7: (['B(d)', 'B(c)'], ['B_OpenAIPadic', 'B_StixLocal', 'B_StixCuspidal'], 'Uses the prompt-stipulated unrefereed local Theorem1.1. The complete affine reduction is supplied, but a complete independent referee verification of the input is not claimed.'),
  8: (['B(a)', 'B(d)'], ['B_Deligne'], 'Local finite extension of Qp; this does not establish a global intrinsic tangential criterion.'),
  9: (['B(d)'], ['B_HarariSzamuely'], 'Finite extension of Qp. The genus-one torsor class must lie in the maximal divisible subgroup; the classification is not a hyperbolic example.'),
 10: (['B(c)', 'B(d)'], ['B_StixCuspidal'], 'Full Galois group and its open subgroups; the cyclotomic-kernel precision is supplied in Part F.'),
 11: (['B(c)', 'F(a)'], ['B_StixCuspidal'], 'Centre-free geometric kernel; intrinsic admissibility is not defined merely by choosing an arbitrary lift.'),
 12: (['B(c).axiom6'], [], 'Refutes the prompt implication from L^H=1 alone. Scan421 itself already distinguishes normalizer-surjectivity existence from uniqueness; full geometric axiom6 is not refuted.'),
 13: (['B(c).axioms1-6', 'B(d)'], ['B_StixCuspidal', 'A:relative-hom'], 'Geometric subcategory proved. The actual forgetting kernel has no fixed element, including unordered markings, provided both curves remain hyperbolic. General intrinsic axioms5-6 and the full requested implication diagram remain incomplete.'),
 14: (['B(c)', 'B(e)', 'main.number_field_sections'], ['B_StixLocal', 'B_Stoll'], 'Requires Selmer localizations and density-one finite-place support in one finite subscheme; unrestricted global sections need not have support supplied by this argument.'),
 15: (['B(c)', 'main.modular_cuspidality'], ['B_OpenAIPadic', 'B_LM3', 'B_StixLocal', 'B_Stoll'], 'Uses prompt-stipulated local theorem and the verified proper modular conclusion; N has compact genus at least2.'),
 16: (['B(e)'], ['B_StixCuspidal'], 'Refutes unrestricted raw surjectivity. The exact geometric disjointness condition is proved, not a classification of all intrinsic admissible family sections.'),
 17: (['B(e)'], [], 'Genus≥2, at least one marking, and every finite étale base cover. The finite Chern obstruction applies to lifts of tautological complete classes; choose a prime coprime to the cover degree and 2g−2.'),
 18: (['B(e)'], ['B_LuoWatanabe'], 'Uses the exact supplied unrefereed complete-family classification for g≥3,n≥1. Does not quantify over arbitrary finite étale moduli covers.'),
 19: (['B(f)', 'B(d)'], ['B_OpenAIPadic', 'B_Steklov', 'B_StixCuspidal'], 'Local finite extension of Qp; complete groupoid retained. Number-field global surjectivity for these stacks remains unfinished.'),
 20: (['B(g)'], [], 'Elementary tripod proof. B.31 completes the general type using the precise archimedean intersection theorem.'),
 21: (['cote148.scan43', 'cote143.scan2'], [], 'The two doubtful fragments in the first-pass transcription remain unresolved as readings. Pointwise finite-field-definition germ assertion is proved; stronger universal Q-model reading is refuted.'),
 22: (['cote143.scans6-8', 'cote143.scan12'], ['B_Deligne'], 'At crossings, retain the actual local-to-global inertia map, which may have a kernel. No claim of a full intrinsic reconstruction of G_Q is made.'),
 23: (['B(e).n0'], ['B_LuoWatanabe'], 'Uses supplied n=1 classification for genus≥3; stated compatible symplectic level versions only.'),
 24: (['B(e).low_genus', 'B(e).multisections'], [], 'Explicit examples prove existence and refute a uniform no-multisection claim. They do not classify all low-genus or all open-subgroup cases.'),
 25: (['B(f)', 'B(c)'], [], 'Necessary criteria and the exact M0,4/tripod identification; sufficiency over number fields and arbitrary outer-action realization remain unfinished.'),
 26: (['B(e)'], [], 'The elementary open-image and geometrically trivial-image ranges. B.33 completes the image classification for constant families; general nonconstant families and the field-section term remain unfinished.'),
 27: (['B(c)', 'B(d).fg_Qp', 'B(e)', 'B(f)', 'main.number_field_sections'], [], 'Explicit incomplete ledger, updated after B.41 to retain the nonisotrivial p-adic case. B(g) is completed in B.31, stable-boundary exclusion in B.37, and the uniform tangential recognition in F.45; the narrower GT-automorphism-only formula remains in F.24.'),
 28: (['B(c).equation25', 'B(f).distinctness'], [], 'Refutes an unrestricted reading; geometric injectivity and the manuscript admissibility reservation are retained.'),
 29: (['B(c).axiom5', 'B(c).finite_descent', 'B(e)', 'main.number_field_sections'], ['B_OpenAIPadic', 'B_StixLocal', 'B_Stoll'], 'Computes all fibres over the geometric locus. Fibres over unknown nongeometric filled-curve sections are not classified.'),
 30: (['B(c).axiom6', 'B(e)', 'B(f).distinctness'], ['B_OpenAIPadic', 'B_MochizukiTamagawa'], 'Computes the fibre over an ordered tuple of distinct actual point classes. It does not force arbitrary coordinate section classes to be geometric.'),
 31: (['B(g)'], ['B_HoshiMochizukiIV'], 'Number field, actual rational base point, full profinite geometric group, with a specified complex embedding. The cited outer intersection theorem is converted to the actual based subgroup stabilizer.'),
 32: (['B(e)', 'B(d)', 'B(c).relative'], ['B_OpenAIPadic', 'B_CarlsonStix', 'A:relative-hom'], 'Finite extension of Qp, hyperbolic base curve and proper hyperbolic constant fibre. Uses the prompt-stipulated local theorem over every finite extension. General nonconstant families remain incomplete.'),
 33: (['B(e)', 'B(c).relative', 'B(d)'], ['B_OpenAIPadic', 'F-local-dichotomy', 'A:relative-hom', 'B_StixCuspidal'], 'The decomposition is complete, retaining the exact noncuspidal field-section term. Its surjectivity from number-field points remains unresolved. The unit identification is proved for number fields, and means the displayed power completion.'),
 34: (['B(e).dominant_functoriality'], ['A_MochizukiTsujimuraRNS', 'B_LeBorgne'], 'Refutes precisely the printed interior-point reflection under arbitrary dominant morphisms, with every local hypothesis checked. No claim is made against RNS Theorem A or its Isom uses.'),
 35: (['B(e).dominant_functoriality', 'B(c).deletion', 'main.number_field_sections'], ['B_OpenAIPadic', 'B_Stoll', 'B_StixLocal', 'B_StixCuspidal'], 'Computes the entire fibre over an actual point of the target, using the stipulated local theorem and finite-support descent. The finite-etale special case is independent of that theorem. Fibres over unknown nongeometric target classes remain uncomputed.'),
 36: (['B(f).boundary', 'B(f).outer_realization'], ['B_StixCuspidal', 'B_CarlsonCorwin', 'F-MochizukiCombinatorial', 'A:cyclotomic-normalizer'], 'A proved closed necessary obstruction over number fields, including all finite-extension germs. The compact orbits contain pro-simple tuples, not necessarily discrete simple curves. Absence of the obstruction is not asserted sufficient.'),
 37: (['B(f).boundary', 'B(f).stacks', 'B(f).outer_realization'], ['B_CarlsonCorwin', 'B_AOV', 'B_AOVCorrigendum', 'F-HoshiMochizukiNodes', 'F-MochizukiCombinatorial', 'F-Illusie', 'F-HoshiLog', 'B_StixCuspidal'], 'Covers the closure of every packet relative to the canonical stable boundary, including stack stabilizers and unordered markings, over number fields. Carlson–Corwin compactification independence is used in its scheme scope; no arbitrary-stack compactification theorem is imported. Does not establish surjectivity outside the closed boundary set and does not use the stipulated local p-adic theorem.'),
 38: (['B(d).fg_Qp', 'B(e).relative', 'B(c).relative'], ['B_OpenAIPadic', 'F-local-dichotomy', 'F-HolzschuhSchmidtStix'], 'Proves generic-section unramification and the exact bijection with relative fundamental-group sections over a smooth p-adic base curve. Every relative section is point-theoretic on all finite-extension fibres. Realization by a section of a nonconstant family remains unproved; the dominant Hom theorem is not applied outside its open range.'),
 39: (['B(d).fg_Qp', 'B(c).relative', 'B(e).relative'], ['B_OpenAIPadic', 'F-local-dichotomy', 'B_BorneVistoli', 'B_StacksLimits', 'B_LandesmanBaseChange'], 'Extends the open/trivial/cuspal geometric-image trichotomy to every sub-p-adic field by one coherent countable descent and a relation-preserving local-field embedding. The geometrically trivial case retains the exact field-section term; it is not asserted geometric.'),
 40: (['B(d).fg_Qp', 'B(e).relative'], ['B_OpenAIPadic', 'F-HolzschuhSchmidtStix', 'B_StacksPurity'], 'All dimensions of a smooth finite-type p-adic model. The residue-field map to the base fundamental group need not be injective; the actual fibre product is retained. Generic realization for nonconstant families remains open.'),
 41: (['B(d).fg_Qp', 'B(c).deletion', 'B(e).relative'], ['B_OpenAIPadic', 'F-local-dichotomy', 'F-Mochizuki', 'B_LandesmanBaseChange', 'B_StixCuspidal'], 'Complete point-or-cusp classification for isotrivial hyperbolic curves over finitely generated Qp fields in every transcendence degree. In the affine case the entire marked open curve must become constant. General nonisotrivial curves are not included.'),
 42: (['B(d).fg_Qp', 'B(e).relative'], ['B_TateUniformization', 'B_SaidiFunctionFields'], 'A completely split compatible Tate-curve tower gives a nonzero global quotient invisible on every closed-point decomposition group. This refutes the exact finite-cover local-point hypothesis needed by the inspected function-field transfer, but does not construct a nongeometric section of a proper hyperbolic family.'),
}
pattern = re.compile(r'\\begin\{statement\}\{(B\.(\d+))\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{statement\}', re.S)
rows = []
for match in pattern.finditer(data):
    sid, number, printed_status, title, statement = match.groups()
    n = int(number)
    tasks, sources, limitations = spec[n]
    status = 'Open' if printed_status.startswith('Open') else ('Refuted' if printed_status.startswith('Refuted') else 'Proved')
    rows.append({'id': sid, 'status': status, 'printed_status': printed_status,
                 'title': title, 'statement': re.sub(r'\s+', ' ', statement.strip()),
                 'proof_location': f'sections/B.tex, statement {sid} and its following proof',
                 'task_ids': tasks, 'sources': sources, 'limitations': limitations})
assert len(rows) == len(spec), (len(rows), len(spec))
assert {int(r['id'].split('.')[1]) for r in rows} == set(spec)
out = ROOT / 'B_results.json'
out.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'statements': len(rows), 'status_counts': {s: sum(r['status'] == s for r in rows) for s in ('Proved', 'Refuted', 'Open')}, 'output': str(out)}, indent=2))
