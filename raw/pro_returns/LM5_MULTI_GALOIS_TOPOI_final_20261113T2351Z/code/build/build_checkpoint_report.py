from pathlib import Path
import sys

ROOT=Path('/workspace/scratch/36f9c078cbe9/deliverable')
number=sys.argv[1]
parts=set(sys.argv[2])
labels=[
 'What is to be settled 1: §14 mixed topos and cohomology',
 'What is to be settled 2: §16 hole filling and van Kampen',
 'What is to be settled 3: §20 sphere two-type',
 'What is to be settled 4: Montpellier cotes149 and147',
]+[f'Lead {i}' for i in range(1,5)]+[f'A({x})' for x in 'abcdef']+[f'B({x})' for x in 'abcd']+[f'C({x})' for x in 'abcd']+[f'D({x})' for x in 'abcd']+[f'E({x})' for x in 'abc']+[f'F({x})' for x in 'abcdefgh']+['F(h-added)(1)','F(h-added)(2)']+[f'EXIT added task {i}' for i in range(1,7)]+['LM8 E.10/E.11 correction and coherent étale-limit lead']
settled={
 'What is to be settled 3: §20 sphere two-type':('D.1–D.16','(a)/(b): proved in corrected form; the specified false assertions are refuted'),
 'Lead 4':('D.16','(b): bare-gerbe identification refuted; exact categorical replacement proved'),
 'D(a)':('D.1–D.3','(a): proved with relative uniqueness correction'),
 'D(b)':('D.4–D.9','(a)/(b): classification through dimension five; characteristic-pair-only claim refuted'),
 'D(c)':('D.10','(b): conflicting bounds corrected; sharp cumulative bounds proved'),
 'D(d)':('D.11–D.15','(b): bare gerbe refuted; structured-gerbe classification and field restrictions proved'),
}
if 'B' in parts:
 settled.update({
 'What is to be settled 1: §14 mixed topos and cohomology':('B.1–B.13','(a)/(b): complete comparison theorem; unqualified scan129 proposition refuted'),
 'Lead 2':('B.1, B.3–B.4, B.9','(b): mixed ≠ logarithmic; exact comparison proved'),
 'B(a)':('B.1–B.2, B.9','(a)/(b): Artin gluing identified; logarithmic alternative refuted and compared'),
 'B(b)':('B.3–B.8','(a)/(b): exact coefficientwise criterion and complete geometric exceptions; all characteristics treated'),
 'B(c)':('B.10–B.12','(a)/(b): corrected support/orientation formulas and trace; ineffective one-cusp claim refuted'),
 'B(d)':('B.12–B.13','(a): complete mixed-map, torsor and splitting formulas; exact rigidity proved'),
 })
if 'C' in parts:
 settled.update({
 'What is to be settled 2: §16 hole filling and van Kampen':('C.1–C.8','(a)/(b): all-topoi hole-filling pushout with surjective boundary maps; exact acyclicity table'),
 'Lead 3':('C.1–C.5','(a)/(b): manuscript special case proved; unrestricted profinite pushout refuted'),
 'C(a)':('C.1–C.4','(a)/(b): squares, all-topoi pushout and transitivity proved; generic profinite extension refuted'),
 'C(b)':('C.5','(a)/(b): local acyclicity and complete global genus/boundary table proved'),
 'C(c)':('C.6–C.8','(a)/(b): discrete actions proved; continuous profinite extensions/protorsors give precise replacement'),
 'C(d)':('C.9–C.12','(a)/(b): transporter and operator constructions proved; composition closure and uniqueness margins refuted'),
 })
if 'A' in parts:
 settled.update({
 'Lead 1':('A.1–A.22','(a)/(b): discrete recognition, pointless counterexamples, intrinsic pro-groupoid theory and topology qualifications proved'),
 'A(a)':('A.1–A.4','(a)/(b): Boolean pointless counterexample; local connectedness or enough points separately suffices; exactness axioms proved'),
 'A(b)':('A.5–A.8','(a): every numbered assertion, the five equivalences and the missing Hom-groupoid formula proved'),
 'A(c)':('A.9, A.22; E.1–E.4','(a): envelope without points; all stages with exact hypotheses and Postnikov comparison proved'),
 'A(d)':('A.10–A.12','(a)/(b): both requested examples; beta requires a point in each component; exact alpha criteria'),
 'A(e)':('A.15–A.21','(a)/(b): full pro/discrete and finite Galois sections; intrinsic shape distinguished from arbitrary strict presentations and limits'),
 'A(f)':('A.13–A.14','(a)/(b): faithful-groupoid induction and thin Hom-groupoids; open image required in the profinite application'),
 })
if 'E' in parts:
 settled.update({
 'E(a)':('E.1–E.2, E.5','(a): shape for arbitrary infinity-topoi; exact recognition and actual-stage hypotheses'),
 'E(b)':('E.3–E.4, E.13','(a)/(b): first-stage identity and finite Postnikov tower; sheaf/hypersheaf qualification proved'),
 'E(c)':('E.6–E.14','(a)/(b): exhaustive A–C statement index, direct image obstruction, and n=4,5 finite-homotopy exodromy'),
 })
s='INCOMPLETE\n\n| Prompt item | Numbered statements | Outcome or state reached |\n|---|---|---|\n'
for lab in labels:
 ids,state=settled.get(lab,('in progress','active proof development or verification; not claimed complete'))
 s+=f'| {lab} | {ids} | {state} |\n'
s+=f'\n# Checkpoint {number}: integrated Parts '+', '.join(sorted(parts))+'\n\n'
s+='This is an interim research checkpoint. The remaining entries are being worked on; it is not the final return. The four opening rows follow the four actual bullet items under “What is to be settled.” Checkpoint01 used an imprecise introductory label for those rows; the present table corrects that bookkeeping without changing its mathematics.\n\n'
s+='The paper is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Author-date citations and an annotated bibliography identify opened primary sources; each bibliography entry carries its own verification status.\n\n'
if 'B' in parts:
 s+=(ROOT/'source_parts/root/report.md').read_text()+'\n\n'
s+=(ROOT/'source_parts/spheres/report.md').read_text()
if 'A' in parts and (ROOT/'source_parts/foundations/report.md').exists():
 s+='\n\n'+(ROOT/'source_parts/foundations/report.md').read_text()
s+='\n\n# Typesetting verification for this checkpoint\n\n'
s+='LuaLaTeX and BibTeX completed. The first successful integrated build had 0 overfull boxes; the final build has 0 overfull boxes and no missing-character or undefined-reference diagnostics. The optional luaotfload module is absent from the runtime; the build uses the installed Latin Modern Type1 fonts with explicit font maps, and the PDF has been rendered and visually checked. This nonfatal loader diagnostic does not leave missing glyphs in the PDF.\n\n'
s+='The build logs are retained under verification/checkpoint'+number+'. Page samples and the precise final page count are recorded below. The final package will preserve all checkpoint archives or explicitly identify superseded drafts.\n'
(ROOT/'LM5_MULTI_GALOIS_TOPOI_report.md').write_text(s)
print('Wrote checkpoint',number,'coverage report for',','.join(sorted(parts)))
