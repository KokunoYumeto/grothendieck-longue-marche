#!/usr/bin/env python3
"""Write the separate D.12--D.16 ledgers; never changes root ledgers/builds."""
from pathlib import Path
import csv, hashlib, json

ROOT=Path(__file__).resolve().parent.parent
SEC=ROOT/'sections'
SOURCE=ROOT/'source_checks'/'140-4'

passages={
 'D.12':['C4 §50.1, folio 650bis verso, scan 6: characteristic-zero uniqueness and faithfully flat descent',
         'C4 §50.2, folios 652 verso–653 verso, scans 10–12: global positive-power assertion and extension lemma'],
 'D.13':['C4 §50.1, folio 650bis, scan 5: fibrewise definition and finite-order criterion in positive characteristic',
         'C4 §50.2, folio 653, scan 11: positive-characteristic generic test'],
 'D.14':['C4 §50.2, folios 652 verso–653, scans 10–11; exact physical PDF pages 10–11, printed footers 9–10: quasi-compact base, separated locally finitely presented G, conclusion φ(1)=g^n'],
 'D.15':['C4 §50.1, folio 651, scan 7: integral characteristic-zero extension discussion',
         'C4 §50.2, folios 653 verso–654, scans 12–13: Noetherian integral extension lemma and regular one-dimensional matrix test'],
 'D.16':['C4 §50.2, folios 653 verso–654, scans 12–13: extension after integer dilation on a Noetherian integral base; regular one-dimensional test'],
}

results=[
 {'id':'D.12','status':'Proved',
  'statement':'Two Ga homomorphisms into a separated locally finitely presented group over a quasi-compact base with the same value at 1 agree after one integer dilation; over a Q-scheme or Z-flat base they agree without dilation. A local positive-power parameter descends along a single faithfully flat quasi-compact covering morphism after one dilation. Consequently Zariski-local existence glues on quasi-compact quasi-separated bases.',
  'where_proved':'sections/D_nonlinear.tex, D.12; code/d_nonlinear.py verifies supplementary Vandermonde identities through degree 10',
  'depends_on':['Stacks Lemma 29.22.12, Tag 0818: finitely presented diagonal','Elementary Vandermonde adjugate identity','Stacks Lemma 35.35.11 and Remark 35.35.12, Tag 040L: descent of morphisms'],
  'notes':'The covering morphism and its overlap are genuinely quasi-compact. This is not a gluing claim for arbitrary non-quasi-compact overlaps; D.14 shows why that qualifier matters.'},
 {'id':'D.13','status':'Proved',
  'statement':'If a quasi-compact base is annihilated by one nonzero integer N, every fibrewise quasi-unipotent section of every separated locally finitely presented group scheme is torsion. The group need not be affine, flat or quasi-compact; the base need not be quasi-separated.',
  'where_proved':'sections/D_nonlinear.tex, D.13',
  'depends_on':['D.8 square-zero reduction kernels','D.12 finitely presented equalizer argument','Stacks Lemma 5.23.2, Tag 0901: compact constructible topology on affine schemes'],
  'notes':'Constructible compactness supplies one exponent a; the finitely generated equalizer ideal is nilpotent of some exponent r. Then g^(a N^(r−1))=1. No bound for the entire nilradical is assumed.'},
 {'id':'D.14','status':'Refuted',
  'statement':'The manuscript assertion that quasi-compactness alone forces some positive power of every fibrewise quasi-unipotent section onto a global Ga is false. A one-dimensional quasi-compact non-quasi-separated base supports a smooth separated finitely presented group and a fibrewise unipotent section with no such power. Both a relatively affine example H and a genuinely nonaffine example H×E are explicit.',
  'where_proved':'sections/D_nonlinear.tex, D.14; code/d_nonlinear.py/.json/.out supply supplementary exact polynomial checks',
  'depends_on':['Explicit gluing on U=disjoint union Spec F_p[ε,z]/ε² for all primes p≥5','Additive automorphisms α_p(t)=t+ε(t^p−t)','Bounded polynomial degree on each affine chart and an arbitrarily large prime not dividing m','Elliptic curve y²w=x³−xw² over Z[1/2] for the nonaffine product'],
  'notes':'The doubled base is not affine or quasi-separated and is non-Noetherian; this does not refute every ring-base or Noetherian-base version. Exact original images independently confirm that the manuscript only says quasi-compact S, with séparé modifying G. The infinite proof uses unbounded primes; the computations are finite supplementary checks.'},
 {'id':'D.15','status':'Proved',
  'statement':'Over every integral Noetherian regular one-dimensional Q-scheme, a generically unipotent section of a separated finitely presented group scheme lies on a unique global Ga; generically quasi-unipotent sections do so after a positive power. This covers Q[t] without flatness or affineness of G. The positive-power theorem also holds on standard finite free nilpotent thickenings S[ε]/ε^r and on the nonflat rings Q[t,ε]/(ε^r,tε).',
  'where_proved':'sections/D_nonlinear.tex, D.15: compactification/translation local lemma, globalization, restriction of scalars and closed patching',
  'depends_on':['D.12 uniqueness over Q and descent','Stacks Theorem 38.33.8, Tag 0F41: Nagata compactification','Stacks Lemma 32.10.1(2)–(3), Tag 01ZM: finite-presentation limit descent','D.11 restriction of scalars and square-zero unipotent kernels, iterated','Milne 2022 Corollary 14.7 and Proposition 14.32','Elementary fibre-product patching R×_Q Q[ε]/ε^r'],
  'notes':'Residue characteristic zero is used essentially in this local lemma to obtain infinitely many distinct integer translates in the special affine line. D.16 supplies a different integer-localization argument for mixed characteristic. The nonflat ring assertion uses closed patching, not an invalid finite-flat restriction of scalars.'},
 {'id':'D.16','status':'Proved',
  'statement':'Let S be integral Noetherian and G/S separated finitely presented. If the generic characteristic is positive, or S_Q is regular of dimension at most one, every generically quasi-unipotent section has a positive power on a global Ga. This includes every DVR, all Dedekind bases, Z[t] and Z[t]_(2,t), with no affine, flat or smooth hypothesis on G. The same positive-power conclusion holds on standard finite free nilpotent thickenings of such S.',
  'where_proved':'sections/D_nonlinear.tex, D.16: local integer-localization lemma, finite-presentation descent from S_Q, finite-cover globalization and restriction of scalars',
  'depends_on':['D.15 characteristic-zero regular-curve theorem','D.11 and D.15 finite-free nilpotent restriction of scalars','Stacks Lemma 32.10.1(2)–(3), Tag 01ZM','Elementary affine-chart coordinate argument: f(0)=1, n-dilation clears n-denominators, D(F) covers V(n)','Separatedness and generic density on integral bases'],
  'notes':'The local lemma starts from a parameter over R[1/n], not merely over the fraction field of a higher-dimensional ring. The entire zero section avoids the affine-chart complement, which supplies f with f(0)=1. After substitution F≡1 mod n, so D(F)∪A1_R[1/n]=A1_R. Rational generic fibre dimension ≤1 is used only to obtain a parameter there via D.15. The later D.17–D.21 arguments settle all Noetherian bases and then every quasi-compact quasi-separated base for separated finitely presented groups.'}
]
for result in results:
    result['manuscript_passages']=passages[result['id']]
    result['depends_on_doubtful_reading']=False
(SEC/'D_nonlinear_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')

coverage=[
 {'task':'Check the precise manuscript base/group quantifiers','status':'Complete','results':['D.14'],'evidence':'Original 140-4 physical pages 10–12 inspected; separated modifies G, S is merely quasi-compact; later lemma restricts to Noetherian integral S.'},
 {'task':'Determine whether local parameters glue after a common dilation','status':'Complete with exact hypothesis','results':['D.12','D.14'],'evidence':'Yes for one faithfully flat quasi-compact cover and hence qcqs Zariski bases; no for general non-quasi-compact overlaps.'},
 {'task':'Find a separated finitely presented nonaffine counterexample','status':'Complete','results':['D.14'],'evidence':'H×E over the explicit dimension-one non-quasi-separated doubled base; no positive power works.'},
 {'task':'Extend the finite-characteristic Artinian test','status':'Complete','results':['D.13'],'evidence':'All quasi-compact bases killed by one nonzero integer, regardless of dimension and nilpotents.'},
 {'task':'Settle the smallest regular characteristic-zero ring test Q[t]','status':'Complete','results':['D.15'],'evidence':'All characteristic-zero Dedekind bases, no flatness or affineness of G.'},
 {'task':'Test nonflat positive-dimensional infinitesimal bases','status':'Complete for specified family','results':['D.15'],'evidence':'Q[t,ε]/(ε^r,tε) by closed fibre-product patching; standard finite free thickenings treated separately by restriction of scalars.'},
 {'task':'Settle all traits and arithmetic bases with rational fibre a regular curve','status':'Complete','results':['D.16'],'evidence':'All DVRs, all integral Noetherian regular one-dimensional bases, Z[t], Z[t]_(2,t), and standard finite free nilpotent thickenings. Integer localization descends the characteristic-zero parameter.'},
 {'task':'Settle the remaining rational-surface and general base cases','status':'Complete in the following supplement','results':['D.17','D.18','D.19','D.20','D.21'],'evidence':'Spec Q[s,t]_(s,t) and Spec Z[s,t]_(2,s,t) are settled, followed by all Noetherian and all quasi-compact quasi-separated bases. No affine, flat or smooth hypothesis on the finitely presented group is required.'},
 {'task':'Resolve the actual smooth-model question and distinguish supplementary axioms','status':'Complete in the following supplement','results':['D.9','D.22','D.23'],'evidence':'D.22 constructs a smooth affine Z-model containing the compact adelic image and extending χ, as requested by preceding (45)–(49). D.23 corrects the literal Z-point recap and bare uniqueness. Conditions (55)–(64) are assumptions/definitions, not a manufactured universal model-existence claim.'},
 {'task':'Preserve source and finite computational steps','status':'Complete','results':['D.12','D.14','D.15'],'evidence':'code/d_nonlinear.py/.json/.out; code/d_source50_extract.py/.out; exact selected original pages, image concordance and SHA256 manifest.'}
]
(SEC/'D_nonlinear_coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')

rows=[
 ['140-4','5','650bis','§50.1 (1)–(2)','Unipotent means fibrewise value at 1 of Ga; quasi-unipotent means some fibrewise power.','Checked supplied transcription; fibre definition used exactly.','D.13–D.14','no'],
 ['140-4','6','650bis verso','§50.1','Characteristic-zero uniqueness and faithfully flat descent.','Checked supplied transcription; D.12 proves a stronger explicit common-dilation statement.','D.12','no'],
 ['140-4','9','652','§50.1 (8)–(12)','Matrix divided-power discussion.','Original physical page 9 directly viewed; handwritten folio 652 and archive footer 8 confirm the scan offset.','source concordance','no'],
 ['140-4','10','652 verso','§50.2 theorem beginning','G is a group scheme (separated), locally of finite presentation over a quasi-compact S.','Exact original physical page 10 viewed; separated is inserted over the phrase schéma en groupes, not attached to S. No quasi-separatedness of S appears.','D.14','no'],
 ['140-4','11','653','§50.2 (13)','There exist n>0 and φ:Ga→G with φ(1)=g^n; the subsequent argument supposes S Noetherian integral.','Exact original physical page 11 viewed; handwritten folio 653, archive footer 10.','D.14–D.15','no'],
 ['140-4','12','653 verso','§50.2 extension lemma','The lemma assumes Noetherian integral S; the author expressly does not prove it for general group schemes.','Exact original physical page 12 and magnified formula viewed. The written dilation notation resembles φ_U(λ^n); all present theorems explicitly use the additive map t↦dt and do not rely on resolving this notation.','D.15','notation only; no result depends on it'],
 ['140-4','211–219','753–757','§52.3 (43)–(64)','Model question at scan 213 concerns preceding (45)–(49); later conditions are supplementary hypotheses.','Original images 211,212,213,215,219 checked. D.22 answers the coherent adelic model question; D.23 treats the un-hatted integral-point recap separately.','D.9,D.22,D.23','scan213 Z versus explicit Z-hat in (45)/(47); both readings treated'],
 ['primary','0818','Stacks Lemma 29.22.12','diagonal','A quasi-separated locally finite-type morphism has finitely presented diagonal.','Official statement and proof opened directly.','D.12–D.13','no'],
 ['primary','040L','Stacks Lemma 35.35.11 / Remark 35.35.12','descent','Morphisms between existing schemes satisfy fpqc descent.','Official statement opened; single actual qc covering morphism used.','D.12','no'],
 ['primary','0901','Stacks Lemma 5.23.2','constructible topology','Constructible topology of a spectral space is quasi-compact.','Official statement opened; applied chartwise to affine schemes.','D.13','no'],
 ['primary','01KH','Stacks Lemma 26.21.6','quasi-separatedness','A scheme is quasi-separated iff intersections of affine opens are quasi-compact.','Official section opened; explicit non-quasi-compact overlap.','D.14','no'],
 ['primary','0F41','Stacks Theorem 38.33.8','Nagata','A separated finite-type scheme over a qcqs base has a compactification.','Official theorem and proof opened; base in the local proof is a DVR.','D.15','no'],
 ['primary','01ZM','Stacks Lemma 32.10.1(2)–(3)','limits','Morphisms and equalities of finitely presented schemes descend through affine inverse limits.','Official statement and proof opened; used to spread local maps and their group identities.','D.15','no'],
 ['computed','d_nonlinear.json','exact integer and finite-field arithmetic','finite certificates','Six selected primes, Vandermonde degrees≤10, 25 witness samples, pinched rings r=2,…,6.','All exact checks PASS; no exhaustive classification or infinite conclusion is inferred from samples.','D.12,D.14,D.15','no'],
 ['proved','D.16','integral Noetherian base','integer localization','A parameter over R[1/n] extends after n-power dilation; parameters over S_Q descend to S[1/n] by finite presentation.','Each denominator/domain step checked directly; local f(0)=1 follows because the entire zero section misses the complement. Dimension ≤1 is required of the regular rational fibre, not the total arithmetic base.','D.16','no'],
]
with (SEC/'D_nonlinear_readings.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful']);w.writerows(rows)

manifest=json.loads((SOURCE/'extraction_manifest.json').read_text())
manifest['pagination']='LM4 scan k = physical one-based PDF page k; zero-based page index and printed archive footer k−1. Checked from folio 652 on physical page 9 and folio 653 on physical page 11.'
for item in manifest['pages']:
    item.pop('lm4_scan_number_pending_visual_check',None)
    p=item['original_pdf_page_one_based'];item['lm4_scan_number']=p
    item['manuscript_folio']={1:'modern cover',2:'preliminary note',9:'652',10:'652 verso',11:'653',12:'653 verso',13:'654'}.get(p)
    item['directly_viewed']=p in [9,10,11,12]
    assert hashlib.sha256((ROOT/item['local_file']).read_bytes()).hexdigest()==item['sha256']
(SOURCE/'extraction_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')

(SOURCE/'reading_concordance.md').write_text('''# Original C4 image concordance

Source: https://grothendieck.umontpellier.fr/140-4.pdf (101,627,143 bytes; 280 physical PDF pages).
Selected pages were extracted by cached HTTP byte ranges without retyping or OCR replacement. SHA256 hashes are in extraction_manifest.json.

| Physical PDF page / LM scan | Printed archive footer | Manuscript folio | Direct image finding |
|---|---:|---|---|
| 9 | 8 | 652 | Matrix divided-power discussion; establishes exact folio/scan offset. |
| 10 | 9 | 652 verso | Theorem begins: G is a group scheme, with “séparé” inserted over that phrase; S is quasi-compact. No quasi-separatedness of S is written. |
| 11 | 10 | 653 | Conclusion φ(1)=g^n; the argument then explicitly supposes S Noetherian and integral. |
| 12 | 11 | 653 verso | Extension lemma over Noetherian integral S; the author expressly declines a proof for general group schemes and tests linear groups. |

The original display on scan 12 resembles φ_U(λ^n); the adjacent scan 11 also writes the usual additive rescaling via nλ. The proof here defines its own additive dilation t↦dt and does not depend on resolving that local notation. The theorem quantifier and conclusion are unambiguous.

Physical page k is the manuscript scan k, including the modern cover at page/scan 1. Subtract one for a PDF zero-based index or the archive printed footer.
''')
print(f'Wrote {len(results)} result entries, {len(coverage)} coverage entries, {len(rows)} reading rows; source hashes verified.')

if __name__=='__main__':
    pass
