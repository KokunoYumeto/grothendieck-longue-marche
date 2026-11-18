#!/usr/bin/env python3
"""Integrate faithful post-checkpoint transcriptions; no mathematical search."""
from pathlib import Path
import shutil,re,json
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT.parents[1]/"recovery_addenda"
sources={
"P.16":("literature/part_P_pal_schlank_matching_reconstructed.tex","part_P_pal_schlank_matching_reconstructed.tex"),
"E.214":("cohomology/E214_fragment.tex","E214_fragment.tex"),
"E.215":("ghost/part_E_primitive_five_support_reconstructed.tex","part_E_primitive_five_support_reconstructed.tex"),
"E.216":("cohomology/E216_fragment.tex","E216_fragment.tex"),
"E.217":("cohomology/E217_fragment.tex","E217_fragment.tex"),
"E.218":("ghost/part_E_all_prime_local_detector_reconstructed.tex","part_E_all_prime_local_detector_reconstructed.tex"),
}
for rid,(src,dst) in sources.items():
    text=(REC/src).read_text()
    assert re.findall(r"\\begin\{result\}\{([^}]+)\}",text)==[rid],(rid,src)
    assert "\\documentclass" not in text and "\\begin{document}" not in text,src
    shutil.copy2(REC/src,ROOT/"sections"/dst)
add="primitive_five_catalog_and_matching_addendum_reconstructed.tex"
shutil.copy2(REC/"ghost"/add,ROOT/"sections"/add)
shutil.copytree(REC,ROOT/"recovery_provenance",dirs_exist_ok=True)
rows=json.loads((ROOT/"notes/recovery_final_result_rows.json").read_text())
for r in rows:
    r["where_proved"]="sections/"+sources[r["id"]][1]
    if r["id"]=="E.215":r["where_proved"]+="; sections/"+add
(ROOT/"notes/recovery_final_result_rows.json").write_text(json.dumps(rows,indent=2)+"\n")
main=ROOT/"SECTION_GHOSTS_paper.tex"
backup=ROOT/"notes/paper_checkpoint08.tex"
if not backup.exists():shutil.copy2(main,backup)
text=backup.read_text()
text=text.replace("Work in progress; incomplete","Final incomplete return; research stopped under the specified rule")
insert=r"""
We additionally prove that selected outputs of the original factorial family
first fail at pro-five class four. A different primitive-five support family
has a common twenty-five-element class-four matching catalog, and a selected
subfamily has an off-five matched class-four lift and a global class-five lift.
No matching at the next class or all-depth survival is inferred.
Relative coefficient interpolation is proved at fixed classes two, three
and four with its actual arithmetic compatibility hypotheses; it is not a
nilpotency-class transition.
An explicit finite characteristic pro-prime quotient separates interior
point sections from cusp sections over finite fields, with the full
arithmetic action retained. This is a local detector, not a global
finite-support theorem.
"""
text=text.replace("We also identify the odd-prime Heisenberg-cover genera",insert+"\nWe also identify the odd-prime Heisenberg-cover genera")
status=r"""
\subsection*{Final stopping status and textual recovery}
The two consecutive scheduled reviews at approximately 11:45 and 12:45 UTC
on 18 November 2026 recorded no qualifying movement on an original open
main question. We stopped research under the specified rule. The nine open
entries remain A.2, A.7, B.1, B.2, B.3, C.7, D.3, E.120 and E.1.
The subsequent work only restores and packages the results already reached.
The exact checkpoint08 source was restored and its archive hash verified.
The later parts P.16 and E.214--E.218 include clearly identified fresh
transcriptions of reviewed conversation proofs. They are not claimed to be
byte-identical to the lost working files. The accompanying report and
provenance records distinguish mathematical review, executed computations,
and final build and visual verification.
"""
text=text.replace("\\section{P. Literature and the scope of established results}",status+"\n\\section{P. Literature and the scope of established results}")
text=text.replace("\\input{sections/part_P_regular_embedding_scope}","\\input{sections/part_P_regular_embedding_scope}\n\\input{sections/part_P_pal_schlank_matching_reconstructed}")
block="\n".join("\\input{sections/"+sources[r][1].removesuffix(".tex")+"}" for r in ["E.214","E.215"])
block+="\n\\input{sections/"+add.removesuffix(".tex")+"}\n"
block+="\n".join("\\input{sections/"+sources[r][1].removesuffix(".tex")+"}" for r in ["E.216","E.217","E.218"])
text=text.replace("\\input{sections/part_E_register}",block+"\n\\input{sections/part_E_register}")
main.write_text(text)
bib=ROOT/"SECTION_GHOSTS_references.bib"
bibbackup=ROOT/"notes/references_checkpoint08.bib"
if not bibbackup.exists():shutil.copy2(bib,bibbackup)
base=bibbackup.read_text()
def entries(s):
    starts=list(re.finditer(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",s))
    return [(m.group(1),s[m.start():starts[i+1].start() if i+1<len(starts) else len(s)].strip()+"\n") for i,m in enumerate(starts)]
keys={k for k,_ in entries(base)}
new=[]
for key,entry in entries((REC/"literature/literature_recovery_references.bib").read_text()):
    if key not in keys:new.append(entry);keys.add(key)
bib.write_text(base.rstrip()+"\n\n"+"\n".join(new))
print("Integrated result fragments:",", ".join(sources))
print("Appended bibliography entries:",len(new))
print("Bibliography keys:",len(keys))
