#!/usr/bin/env python3
"""Integrate the proved split source map and its precise cubic-frame gate."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent/'work'
p=WORK/'centralizer_ternary_fivepoint_retraction.tex';t=p.read_text()
t=t.replace('record with the earlier cubic frame; the general\nnonidentity pair records are not determined here.',
 'record with the earlier cubic frame. Identity pair records\n'
 'with other harmonic frames, and general nonidentity pair\n'
 'records, are not determined here.')
p.write_text(t)
p=ROOT/'code/assemble_draft.py';t=p.read_text()
needle=' "tower_cubic_orbit_orbifold.tex":"part_a_cubic_orbit_orbifold.tex",'
assert needle in t;t=t.replace(needle,needle+'\n'+
 ' "centralizer_ternary_fivepoint_retraction.tex":"part_a_ternary_fivepoint_retraction.tex",');p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_paper.tex';t=p.read_text()
needle=r'\input{part_a_cubic_orbit_orbifold}'
assert needle in t;t=t.replace(needle,needle+'\n'+r'\input{part_a_ternary_fivepoint_retraction}');p.write_text(t)
p=ROOT/'code/update_results.py';t=p.read_text()
pos=t.index("pat=re.compile(r'\\\\begin")
addition="""
add('A.4.45','Actual six-relator five-point presentation; fifth insertion; original signed modular marking; A.4.6--A.4.7; full finite vertex-module centralizer census', 'Task A.4; Lead 1(2)',
    'A literal split five-point retraction retains the complete ternary modular centralizer detector and excludes the earlier identity pair with cubic frame5I',
    'The five generator words give pi iota=id, with exact signed relation q192=(-I)^epsilon theta12 pi. The pure signed image has order96 and excludes-I modulo4, so its kernel equals the original B-normal projective kernel. Every relative abelian exponent-m quotient retains this split map. In the ternary modular source all six pure r-centralizer residues are tested in the actual192-dimensional vertex module with96-dimensional kernel; correction rank62 leaves onlyI. Every failed residue has an explicit dual obstruction. Other harmonic frames on identity pair records and general nonidentity pair records remain to be examined.')

"""
t=t[:pos]+addition+t[pos:]
t=t.replace('A.4.1--A.4.44;', 'A.4.1--A.4.45;');p.write_text(t)
p=ROOT/'part_a_finite.tex';t=p.read_text()
t=t.replace('The task also executes the complete genuine-source',
 'A.4.45 proves a split five-point retraction retaining the\n'
 'full ternary modular centralizer detector and excludes the\n'
 'previous identity-pair cubic frame.  Other harmonic frames\n'
 'and nonidentity records remain in the complete genuine-source')
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_report.md';t=p.read_text()
t=t.replace('A.4.1--A.4.44','A.4.1--A.4.45')
t=t.replace('Eight further independently audited results','Nine further independently audited results')
t=t.replace('All eight newly integrated proofs','All nine newly integrated proofs')
t=t.replace('164 statements:149Proved','165 statements:150Proved')
t=t.replace('164 numbered statements:149Proved','165 numbered statements:150Proved')
needle='The separate all-multiplier normalization supplement is preserved'
addition='''A.4.45 proves the exact split map from the alternating-prime five-point target to the full ternary modular source. All six defining relators reduce freely under the displayed retraction, and the fifth pentagon insertion is its literal section. The signed relation q192=(-I)^epsilon theta12 pi retains both signs; the pure signed image excludes-I modulo4, so its kernel is the original B-normal modular kernel. All six pure cubic-centralizer residues were checked in the actual vertex-module quotient, with kernel dimension96 and correction rank62; only identity lifts. Every other residue, including5I, has an explicit dual linear obstruction. Root replayed both the free retraction and the modular source calculation. This excludes the earlier identity pair record with harmonic frame1 and cubic frame5I. Identity records with other harmonic frames, and general nonidentity records, remain under investigation.

'''
assert needle in t;t=t.replace(needle,addition+needle);p.write_text(t)
p=ROOT/'code/render_pdf_qa.py';t=p.read_text()
t=t.replace('range(38,45)','range(38,46)').replace("'COO.'","'COB.','MFP.','TMR.'")
p.write_text(t)
print('Integrated A.4.45 with exact remaining frame scope; ledger count165.')
