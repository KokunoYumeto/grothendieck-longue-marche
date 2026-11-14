#!/usr/bin/env python3
"""Preserve and correct mathematical typography in the checkpoint-06 ledger."""
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / 'code/assemble_register.py'
text = path.read_text()
tree = ast.parse(text)
node = next(n for n in tree.body if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'TASKS' for t in n.targets))
tasks = ast.literal_eval(node.value)
prior = {r[0]: r for r in tasks if r[0] in {'D.1', 'D.2', 'E.2', 'E.3'}}
dest = ROOT / 'research/checkpoint06_coverage_formatting_prior_passages.json'
assert not dest.exists(), 'Preserved passages may not be overwritten.'
old_function = """def tex_escape(s):
    return (s.replace('&',r'\\&').replace('_',r'\\_').replace('%',r'\\%')
             .replace('^',r'\\textasciicircum{}'))
"""
assert old_function in text
dest.write_text(json.dumps({'task_rows': prior, 'formatter': old_function}, indent=2)+'\n')
states = {
 'D.1': r'The actual geometric $\mathfrak S_3$ action excludes dimension two. Fully invariant finite five-group targets carry all three ordinary special outer parameters. Every first-precision parameter is class-preserving with an exact elementwise conjugator. All $A_6$ chief steps over an odd-order base have the proved equal positive generating-lift count, including coupled odd pullbacks. The ordinary even-base $A_6^{20}$ obstruction and all earlier lifting comparisons remain retained. Realization or exclusion of the two-dimensional complement through every finer full finite source remains. Every generating lift at the first universal coprime elementary-$p$ cover factors through an automorphism of that same cover; its complete fixed-conjugator fibre and ordinary centralizer union are parameterized and counted.',
 'D.2': r'The extra weight-nine vector, gamma line and complete finite pentagon comparison are verified. Elementary abelian and central obstructions, the complete $A_5$ chief-step count, and the ordinary order-five $A_6^{20}$ obstruction retain their actual source maps and every centralizer choice. The latter also retains an admitted component above the prescribed five-group shadow. A cofinal equivariant lift or exclusion of the extra gentle direction remains. The exact odd-base $A_6$ chief comparison now fixes every prescribed peripheral conjugator and counts every generating lift at that stage.',
 'E.2': r'All 24 CM fibres survive each proved refinement through E.49. The full three-adic class-three boundary correction-image fibre is $\mathbf Z_3^{70}$ over every one of the 432 multiplier-one sources. Four rational equations and two integral residue tests give its exact class-two projection. Its complete exponent-three image has $3^{25}$ points per source, with a specified finite nonlift surviving every change of higher class-two digits. The defined binary, prime-supported, $\mathrm{SL}_2(\mathbf F_5)$ and Hurwitz common families are retained. Full profinite survival remains. The full five-strand $\mathrm{Sp}_4(\mathbf F_3)$ test also retains all 864 points. Its complete source factors through $G_6$, its first $B_4$ target is the actual E.18 group, and three explicit simultaneous conjugators prove full $B_5$ generation for every retained word.',
 'E.3': r"All 864 degree-six points pass the retained pentagons, braid and twist relations. The actual $\mathrm{SL}_2(\mathbf F_5)$ source maps onto the five-point Hurwitz source; the same word retains both through E.47's complete integral class-three families at multiplier one. Their full common four-strand target is $(T_{23}\times_{S_L}T_L)\times A_{96}$. The $A_6$ kernel/outer tests also retain all 864 points in their stated common sources. Compatibility through every finite quotient remains. The full five-strand $\mathrm{Sp}_4(\mathbf F_3)$ test also retains all 864 points. Its complete source factors through $G_6$, its first $B_4$ target is the actual E.18 group, and three explicit simultaneous conjugators prove full $B_5$ generation for every retained word.",
}
for row in tasks:
    if row[0] in states:
        replacement = (*row[:3], states[row[0]])
        old = repr(row)
        assert old in text
        text = text.replace(old, repr(replacement), 1)
new_function = old_function + """
def tex_text(s):
    # Task-state strings use paired dollar signs only for explicit mathematics.
    pieces = re.split(r'(\\$[^$]*\\$)', s)
    return ''.join(p if p.startswith('$') else tex_escape(p) for p in pieces)
"""
text = text.replace(old_function, new_function, 1)
text = text.replace("tex_escape(c+'. '+d)", "tex_text(c+'. '+d)", 1)
path.write_text(text)
print(json.dumps({'status':'PASS','preserved':str(dest.relative_to(ROOT)),
                  'edited_task_rows':sorted(states),
                  'scope':'Spacing and mathematical typography; no proof or source map changed.'}, indent=2))
