#!/usr/bin/env python3
"""Repair the concrete first-build overflow and restore the checked citation."""
from pathlib import Path
import re, shutil, zipfile

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
BACK=ROOT/'notes/ninth_hour_preintegration'
p=WORK/'main_fivepoint_signed_source_module.tex'
shutil.copy2(p,BACK/'source_module_before_display_split.tex')
t=p.read_text()
old=r''' [F:J]=288,\qquad J/J_0\simeq C_3^{97},\qquad
 |B/J_0|=1728\cdot3^{97},\qquad
 1\longrightarrow C_3^2\longrightarrow B/J_0
     \longrightarrow E_3\longrightarrow1.'''
new=r''' \begin{gathered}
 [F:J]=288,\qquad J/J_0\simeq C_3^{97},\qquad
 |B/J_0|=1728\cdot3^{97},\\
 1\longrightarrow C_3^2\longrightarrow B/J_0
     \longrightarrow E_3\longrightarrow1.
 \end{gathered}'''
assert old in t
p.write_text(t.replace(old,new))

p=WORK/'ghost_references.bib'
shutil.copy2(p,BACK/'ghost_references_before_spacing.bib')
t=p.read_text()
replacements={
 "author's2006":"author's 2006", 'April2021':'April 2021',
 'January2004':'January 2004', 'opened17November2026':'opened 17 November 2026',
 'Theorem11.24':'Theorem 11.24', 'Theorem11.46':'Theorem 11.46',
 'Theorem11.51':'Theorem 11.51', 'printed150':'printed page 150',
 'printed161':'printed page 161', 'printed164':'printed page 164',
 'ExposeXIII':'Expose XIII', 'Corollary2.9':'Corollary 2.9',
 'Section2.10':'Section 2.10', 'Lemma2.11':'Lemma 2.11',
 'Corollary2.12':'Corollary 2.12', 'pages288':'pages 288',
 'formula(1.5.1)':'formula (1.5.1)', 'printed275':'printed page 275',
 'Theorem(1.6)':'Theorem (1.6)', 'printed276':'printed page 276',
 'dimension2g':'dimension 2g',
}
for a,b in replacements.items():t=t.replace(a,b)
p.write_text(t)

# The previously checked Fresse entry had been added directly to the merged
# bibliography. Preserve it in the authoritative root bibliography as well.
p=ROOT/'notes/root_references.bib'
shutil.copy2(p,BACK/'root_references_before_fresse_restore.bib')
with zipfile.ZipFile(ROOT.parent/'GT_TOWER_CHECK_checkpoint_08.zip') as z:
    old=z.read('GT_TOWER_CHECK/GT_TOWER_CHECK_references.bib').decode()
entries={re.match(r'@\w+\{([^,]+),',e).group(1):e.strip()
         for e in re.split(r'(?=^@)',old,flags=re.M) if e.strip()}
assert 'Fresse2017' not in p.read_text()
p.write_text(p.read_text().rstrip()+'\n\n'+entries['Fresse2017']+'\n')

(ROOT/'notes/build/ninth_initial_layout_defects.md').write_text('''# First ninth-hour build: exact defects and repairs

The three-pass LuaLaTeX build completed. Its retained log reported one
overfull display,5.168pt, at SVM.2 in the common-source proof. The display
has been split into two rows in the authoritative source.

The same build reported the undefined key Fresse2017. The bibliography
merge had omitted that previously checked entry because it existed only
in the merged file. Its exact checkpoint08 bytes were restored to the
authoritative root bibliography, and the opened primary location remains
unchanged. The checked statement itself was not changed.

The run-together bibliographical metadata observed in checkpoint08 was
repaired by adding the missing spaces. Every preedit source is preserved.
A fresh complete build and full-page inspection are still required.
''')
print('Repaired the one5.168pt display, restored the exact verified Fresse citation, and spaced bibliography metadata.')
