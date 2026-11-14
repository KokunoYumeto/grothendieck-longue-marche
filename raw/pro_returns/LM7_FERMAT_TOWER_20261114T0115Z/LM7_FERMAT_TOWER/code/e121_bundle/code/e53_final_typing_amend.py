#!/usr/bin/env python3
"""Preserve the E121 freeze and clarify two literal morphisms in its proof."""
from pathlib import Path
import shutil,hashlib,json,difflib
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
frozen=ROOT/'ledger/e_fiftythree_normalizer_manifest.json'
oldmanifest=json.loads(frozen.read_text())
for rel,entry in oldmanifest['files'].items():assert sha(ROOT/rel)==entry['sha256'],rel
saved=ROOT/'audit/pre_final_typing/full_tree'
stage=ROOT.parent/'e121_pre_final_typing_snapshot'
assert not saved.exists() and not stage.exists()
shutil.copytree(ROOT,stage)
saved.parent.mkdir(parents=True,exist_ok=True)
shutil.move(str(stage),str(saved))
proof=ROOT/'sections/E_fiftythree_normalizer.tex'
old=proof.read_text()
before=r'''E.119's onto quotient norm. The trace identity then forces
$j_L=3N_L^{-1}$ in the displayed bases, yielding (E121.4).
Its kernel is zero.'''
after=r'''E.119's onto quotient norm. Its kernel is $3A_{L_2}$:
the target has exponent three, while both $\ker N_L$ and
$3A_{L_2}$ have order nine.
The actual trace identity gives the precise rule
$j_L(b)=3a$ for any lift $a$ with $N_L(a)=b$.
Changing that lift by $3A_{L_2}$ changes $3a$ by zero,
since $9A_{L_2}=0$. This rule yields (E121.4), and its
kernel is zero.'''
assert old.count(before)==1
new=old.replace(before,after)
before=r'''literal $\mu_3$ torsion and the rank difference in (E121.9).
Finite-rank unit groups complete exactly'''
after=r'''literal $\mu_3$ torsion and the rank difference in (E121.9).
For each of these actual kernels $K$, choose a $\mathbb Z_3$-basis
of the free quotient $K/\mu_3$ and lifts $k_1,\ldots,k_r\in K$.
The displayed direct-sum isomorphism is the continuous map
$(z,(a_i))\mapsto z\prod_i k_i^{a_i}$.
Its inverse reads the quotient-basis coordinates $(a_i)$ and
then divides the input by $\prod_i k_i^{a_i}$ to obtain
$z\in\mu_3$. These two constructions compose to the identity.
A different quotient basis is an actual $\mathrm{GL}_r(\mathbb Z_3)$
coordinate change; a different lift multiplies $k_i$ by
a specified element of $\mu_3$ and changes the torsion coordinate
by the inverse product of those elements to the powers $a_i$.
Thus the choice ambiguity is explicit without assigning an
uncomputed numerical upper unit basis.
Finite-rank unit groups complete exactly'''
assert new.count(before)==1
new=new.replace(before,after)
proof.write_text(new)
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
 fromfile='original_128_file_freeze',tofile='actual_lift_rule_and_completed_kernel_map'))
(ROOT/'audit/e121_final_typing.diff').write_text(diff)
math_paths=['code/e53_normalizer_module.py','code/e53_normalizer_module.out','code/e53_normalizer_module.json']
math_paths += [r for r in oldmanifest['files'] if r.startswith('code/') and '/history/' not in r and r.endswith(('.gp','.bin'))]
unchanged={r:sha(ROOT/r) for r in math_paths}
assert all(unchanged[r]==oldmanifest['files'][r]['sha256'] for r in unchanged)
result={'status':'PASS','scope':'Two proof-only morphism clarifications; mathematical code, outputs and all complete PARI objects unchanged.',
 'original_manifest_sha256':sha(saved/'ledger/e_fiftythree_normalizer_manifest.json'),
 'before_proof_sha256':sha(saved/'sections/E_fiftythree_normalizer.tex'),
 'after_proof_sha256':sha(proof),'exact_diff_sha256':sha(ROOT/'audit/e121_final_typing.diff'),
 'complete_original_freeze':'audit/pre_final_typing/full_tree','original_manifest_entries_checked':len(oldmanifest['files']),
 'unchanged_mathematical_files':unchanged,
 'claims':['j_L(b)=3a for an actual norm lift; independence follows from kerN=3A and9A=0.',
           'The completed-kernel product map, its quotient-and-division inverse, and basis/lift ambiguity are explicit.'],
 'arithmetic_replay_needed':False}
(ROOT/'audit/e121_final_typing.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
