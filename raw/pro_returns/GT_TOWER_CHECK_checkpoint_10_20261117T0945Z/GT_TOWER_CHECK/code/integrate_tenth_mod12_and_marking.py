#!/usr/bin/env python3
"""Integrate the audited full mod12 survivor and ordinary marking comparison."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
BACK=ROOT/'notes/tenth_mod12_preintegration'
BACK.mkdir(exist_ok=True)
for rel in ['code/assemble_draft.py','code/update_results.py','GT_TOWER_CHECK_paper.tex',
            'GT_TOWER_CHECK_report.md','part_a_finite.tex']:
    dest=BACK/rel
    assert not dest.exists(), 'One-shot integration: '+rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/rel,dest)
wide=WORK/'centralizer_common_mod6_canonical_survivor.tex'
shutil.copy2(wide,BACK/wide.name)
s=wide.read_text()
old=''' B_0=\\langle s,r\\mid s^2=r^3=1\\rangle,\\qquad
 F_0=\\langle x,y\\rangle,\\quad x=(sr)^{-2},\\quad y=sxs,
 \\qquad K=\\ker(B_0\\longrightarrow Q_B),\\quad |Q_B|=576.'''
new=''' \\begin{gathered}
 B_0=\\langle s,r\\mid s^2=r^3=1\\rangle,\\qquad
 F_0=\\langle x,y\\rangle,\\quad x=(sr)^{-2},\\quad y=sxs,\\\\
 K=\\ker(B_0\\longrightarrow Q_B),\\qquad |Q_B|=576.
 \\end{gathered}'''
assert old in s
wide.write_text(s.replace(old,new))
p=ROOT/'code/assemble_draft.py';s=p.read_text()
needle=' "ghost_common_quartic_kernel.tex":"part_a_common_quartic_kernel.tex",'
assert needle in s
s=s.replace(needle,needle+'\n'+
 ' "centralizer_involution_marking.tex":"part_a_involution_marking.tex",\n'+
 ' "centralizer_common_mod12_survivor.tex":"part_a_common_mod12_survivor.tex",')
p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_paper.tex';s=p.read_text()
needle=r'\input{part_a_finite_branch_output}'
assert needle in s
s=s.replace(needle,r'\input{part_a_involution_marking}'+'\n'+needle)
needle=r'\input{part_a_common_quartic_kernel}'
assert needle in s
s=s.replace(needle,needle+'\n'+r'\input{part_a_common_mod12_survivor}')
p.write_text(s)
p=ROOT/'code/update_results.py';s=p.read_text();pos=s.index("pat=re.compile(r'\\\\begin")
entry='''
add('A.4.59','A.4.55 genuine corrected mod6 source; A.4.58 exact mixed-mod4/12 maps; full integral quaternary canonical cover; actual finite automorphism and primary edge maps; B.2.7 and B.2.9 full lift', 'Task A.4; Lead 1(2)',
    'The complete mixed-mod12 five-point test has an actual normalized genuine gentle parity-one survivor reducing to the corrected mod6 record',
    'The actual606-equation291-variable mod4 system has97 binary lift directions; the selected support9,10,15,52,59 satisfies every mixed-target pentagon/cycle and frame equation. Its pure finite automorphism has identity288-state base and invertible97-dimensional reduction. The full canonical multiplier has Smith factors C2^8 and C4^8; an exact112-coordinate integral HNF witness kills the selected full cusp defect. Natural odd-kernel and2-power-kernel maps join the zero primary defects at E12. The full finite-certificate lift and72-divisible normalization preserve all eight insertion records and signed CM frames. Root and ghost replayed the full selected gate and actual automorphism; every saved array matches. The failed transpose attempt remains archived.')

'''
s=s[:pos]+entry+s[pos:]
s=s.replace('A.4.1--A.4.56; A.4.58; executed','A.4.1--A.4.56; A.4.58--A.4.59; executed')
p.write_text(s)
p=ROOT/'part_a_finite.tex';s=p.read_text()
needle='targets with their exact common source kernels.'
assert needle in s
s=s.replace(needle,needle+' A.4.59 then proves\n'
 'a genuine parity-one survivor in the entire mixed-modulus-twelve\n'
 'test, including the full canonical-cover obstruction and finite\n'
 'automorphism checks.\n')
p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_report.md';s=p.read_text()
s=s.replace('177statements:162Proved,2Known,13Open','178statements:163Proved,2Known,13Open')
s=s.replace('177 numbered statements:162Proved,2Known and13Open','178 numbered statements:163Proved,2Known and13Open')
s=s.replace('Four further audited results are now integrated','Five further audited results are now integrated')
lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A.4 |'):
        lines[i]='| A.4 | A.4, A.4.1--A.4.56; A.4.58--A.4.59 | Open; explicit translation and involution recognition/fusion and ambient branch output are proved; the full mod6 and mod12 tests have genuine parity1 survivors with full canonical lifts; exact mixed-mod4/12 source maps are proved, and final finite compiler audit and executed separating-level census continue |'
s='\n'.join(lines)+'\n'
needle='## Tenth-hour advances on the main finite task\n\n'
assert needle in s
s=s.replace(needle,needle+
 'A.4.59 now proves an actual normalized gentle parity-one survivor of the full mixed-modulus-twelve pentagon test. Its entire canonical obstruction is killed in the integral lattice, its finite automorphism is verified, and the full lift retains the record. The ordinary marking comparison IFM.1--6 has also been inserted, covering the full four-pair permutation action used by A.4.53. The CMC.1 display overflow exposed in the first tenth-hour build has been split in its authoritative source; the failed source and build log remain retained.\n\n')
p.write_text(s)
print('Integrated A.4.59 and IFM.1--6; repaired CMC.1 with previous bytes retained.')
