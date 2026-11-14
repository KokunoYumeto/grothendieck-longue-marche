"""Rebuild the Part A statement ledger from current labelled TeX statements."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[2]
p=root/'sections/A.tex'
b=p.read_bytes()
b=b.replace(b'{\rm prime}',br'\mathrm{prime}')
p.write_bytes(b)
s=b.decode()
meta={
 'typed-functor':(['Item 1','A(a)'],['LM scans 21–24, 28–31, 43–44; manuscript §§5,7']),
 'proper-affine':(['A(b):IV(b)'],['LM scan 66; manuscript folio 31']),
 'section-eight-cases':(['A(b):I','A(b):II','A(b):III','A(b):IV(a)','A(b):IV(c)','A(b):IV(d)'],['LM scans 55–68; manuscript folios 25–31']),
 'lead-one':(['Lead 1','Lead 2','Item 1'],['LM scans 21–24, 35, 61–79']),
 'two-morphisms':(['A(a)'],['LM scans 44,50–54; manuscript folios 24–25']),
 'abstract-rigidity':(['A(a)'],['LM scan 34; unrestricted preliminary category']),
 'geometric-centralizer':(['A(a)'],['LM scans 34,52–53']),
 'tripod-commutant':(['A(e):full/pro-ell commutant','A(e):ell=2','Lead 4'],['LM scan 485']),
 'abelian-commutant':(['A(e):minimal solvable length'],['LM scan 485; §51 first approximation']),
 'metabelian-commutant':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; §51 first approximation']),
 'finite-metabelian':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; independent finite certificate']),
 'solvable-open':(['A(e):minimal solvable length'],['LM scan 485']),
 'literal-normalizer':(['A(e)'],['LM scan 483']),
 'cyclotomic-normalizer':(['A(e)(1)','A(c):transporter'],['LM scans 69,483; manuscript folio 32']),
 'unique-loops':(['A(e)(3)'],['LM scans 84,483']),
 'cyclotomic-centralizer':(['A(e)(1 bis)','Lead 2'],['Cote 149 scans 55–56; Faltings letter 1983 PS']),
 'normalizer-implications':(['A(e)(1)','A(e)(1 bis)'],['LM scan 483; cote 149 scans 55–56']),
 'padic-cusp-reconstruction':(['A(e)(4)'],['LM scan 483; Mochizuki 2004 Lemma 1.3.9']),
 'cm-degree-five':(['A(e)(2)','F(f):LM8 audit'],['LM8 G.3–G.11']),
 'cm-prime-normalizer':(['A(e)(2)','F(f):LM8 audit'],['LM8 G.12–G.13']),
 'cm-detected-normalizer':(['A(e)(2)','F(f):LM8 audit'],['LM8 G.19']),
 'cm-common-kernel':(['A(e)(2)','F(f):LM8 audit'],['LM8 G.20–G.22']),
 'local-embedding':(['A(a):slimness','A(b):IV(a)','A(b):IV(b)'],['LM scans 54,65–66,109']),
 'slim':(['A(a):slimness char0','A(a):slimness charp'],['LM scans 54,109; manuscript folio 25 margin']),
 'positive-degree-open':(['A(b):IV(d)'],['LM scans 44,50,54,67']),
 'relative-hom':(['A(b):dominant relative Hom','A(e):full faithfulness','Lead 1','Item 1'],['LM scans 21–24,35,67,484']),
 'boundary-recovery':(['A(c):nonrational cusps'],['LM scans 69–72,109–112']),
 'kummer-ambiguity':(['A(c):Kummer ambiguity','A(c):proper Kummer datum','A(c):affine-to-proper compatibility'],['LM scans 47–48,84,112–113']),
 'all-multipliers':(['A(d):all multipliers','A(d):explicit minus one','A(d):same handles'],['LM scans 86–87']),
 'five-conditions':(['A(d):geometric axioms'],['LM scans 82–88']),
 'condition-countermodels':(['A(d):dependencies'],['LM scans 82–88']),
 'condition-lattice-open':(['A(d):dependencies'],['LM scans 82–88']),
 'two-section-stabilizer':(['B added task:two point sections','B added task:ker Delta','B added task:C phi'],['Prompt line 236; cote 143 scans 29–31; cote 140-3 scans 229,234,240']),
 'root-orbit-stabilizer':(['B added task:two point sections'],['Prompt line 236; alternative full root-orbit interpretation']),
 'isogeny-weight-test':(['A(e)(2)'],['LM8 G.19–G.22; new genus-one covering reduction']),
 'deeper-common-kernel':(['A(e)(2)'],['LM8 G.20–G.22; new strict residual-kernel reduction']),
 'absolute-geometric':(['A(b):absolute open Hom','F(f):LM3 D.11 audit'],['LM scan 484; LM3 D.11']),
 'absolute-hom':(['A(b):absolute open Hom','A(b):Uchida 1981 open homomorphism check'],['LM scan 484; Uchida 1981 pp. 595–597, Proposition 1; OpenAI 2026 Theorem 2.4']),
 'local-absolute-isom':(['A(b):absolute Isom over p-adic fields'],['LM scan 484; RNS Theorem D and Theorem 3.12; Jarden–Ritter 1979 p. 2']),
 'local-absolute-hom-open':(['A(b):absolute open Hom over p-adic fields'],['LM scan 484; RNS Theorem 3.11 and Theorem 3.12']),
 'constant-kernel':(['A(b):kernel over finitely generated fields'],['LM scan 484; Hoshi–Mochizuki 2011 Corollary 6.2(ii)']),
 'family-kernel-quotient':(['A(b):kernel over finitely generated fields'],['LM scan 484; Hoshi–Mochizuki 2011 Corollaries 6.4–6.5']),
 'proprime-kernels':(['A(b):single-prime kernel','A(b):ell=2 kernel'],['LM scan 485']),
 'regular-prime-kernel':(['A(b):single-prime kernel'],['LM scan 485; Sharifi 2002 Theorem 1.1; Brown 2012 Theorem 1.1']),
 'kernel-open':(['A(b):kernel over finitely generated fields','A(b):single-prime kernel','A(b):ell=2 kernel'],['LM scans 484–485']),
 'strong-metabelian-counterexample':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; Yamaguchi Conjecture 0.1(2), S_{2,0,U,U}, and Remark 0.2']),
 'solvable-centers':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new exact arithmetic-extension reduction']),
 'solvable-projection-limit':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; Mochizuki 1999 Theorem A-prime/18.1; Yamaguchi Theorem 0.4']),
 'metabelian-unit-family':(['A(e):minimal solvable length','A(e):ell=2','Lead 4'],['LM scan 485; new full-unit refinement of the arithmetic-centralizing construction']),
 'normalizer-character-descent':(['A(e)(2)'],['LM scan 483; new full profinite finite-cover character descent']),
 'conjugation-prime-character':(['A(e)(2)'],['Serre, Abelian l-adic Representations, II section 3.1 and III sections 1.2, 2.1--2.3']),
 'full-support-normalizer':(['A(e)(2)'],['LM scan 483; LM8 G.20--G.22; new positive-density restriction on the full profinite residual case']),
 'cm-normalizer-field':(['A(e)(2)'],['LM scan 483; new CM-subfield and local-embedding restrictions; Serre II sections 3.1 and 3.3']),
 'third-derived-obstruction':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new explicit derived-length-three obstruction from elliptic and Fermat covers']),
 'third-derived-second-digit':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new modulus25 restriction from elliptic and Fermat25 covers at5701']),
 'third-derived-IA':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new structural third-derived IA-image theorem by exact arithmetic normalization and fibre isolation']),
 'metabelian-multiplier':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new scalar-multiplier rigidity using the two tangential sections and twisted Fermat covers']),
 'third-derived-projection':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new exact third-to-second-derived peripheral commutant equality']),
 'last-layer-unrestricted':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new explicit unrestricted third-derived arithmetic kernel and exact peripheral obstruction']),
 'haar-block-obstruction':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; exact obstruction to a normal prime-to-ell averaging construction of peripheral last-layer automorphisms']),
 'split-normalizer':(['A(e)(2)','A(e)(1 bis)'],['LM scan 483; LM8 G.20--G.22; new classification of all procyclic normalizers admitting a virtual arithmetic section']),
 'normalizer-prime-complement':(['A(e)(2)'],['LM scan 483; LM8 G.20--G.22; exact central-Sylow shrinking and quotient splitting leave a pro-prime-to-ell embedding problem']),
 'prime-complement-counterexample':(['A(e)(2)'],['LM scan 483; exact number-field counterexample to an abstract virtual-splitting shortcut for the remaining extension']),
 'surface-proprime-free':(['A(e)(2)'],['LM scan 483; independent finite-cover cohomology proof supplying the proper-surface input']),
 'proper-normalizer-restrictions':(['A(e)(2)'],['LM scan 483; proper-hyperbolic extension of character, CM-support and normalizer-splitting restrictions']),
 'one-layer-class-preservation':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new deck-twisted fibre-isolation theorem retaining every element conjugacy class one derived level below']),
 'third-derived-class-rigidity':(['A(e):minimal solvable length','Lead 4'],['LM scan 485; new full profinite class-preserving rigidity for S2 and S3 and exact fourth-to-third-derived peripheral commutant projection']),
}
patterns=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|corollary|remark)\}\[([^\]]+)\]\s*\\label\{(A:[^}]+)\}',s))
rows=[]
for n,m in enumerate(patterns,1):
 label=m.group(3); key=label[2:]; title=m.group(2)
 status=next((a for a in ['Refuted','Known','Open','Proved'] if a in title),'Unclassified')
 end=patterns[n].start() if n<len(patterns) else len(s)
 body=s[m.start():end]
 task,anchors=meta.get(key,(['A:UNMAPPED'],[]))
 sources=sorted({a.strip() for x in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',body) for a in x.split(',')})
 lim=''
 if status=='Open': lim='INCOMPLETE: the statement records the proved cases and exact unresolved obstruction; it does not settle this task.'
 if key=='section-eight-cases': lim='Global proper point-section surjectivity remains undecided. The statement proves the exact case-by-case reduction.'
 if key in ('proper-affine','section-eight-cases'): lim+=' Local infinite-index trichotomy uses the supplied unrefereed October 2026 local section theorem.'
 if key=='deeper-common-kernel': lim='This is a strict reduction to R_nil(F\u2032), not a proof that this remaining group contains no arithmetic-normalized procyclic subgroup.'
 if key=='padic-cusp-reconstruction': lim='Proves functorial cusp reconstruction under arithmetic group isomorphisms; does not classify all local cyclotomic-normalized procyclic subgroups.'
 if key=='absolute-hom': lim='Uses the supplied unrefereed 2026 open-Hom theorem for number-field Galois groups. The exact Uchida open-map step was checked independently; this does not certify the entire unpublished source.'
 if key=='solvable-projection-limit': lim='Determines the projected finite-level commutants and the prosolvable limit, not the same-level commutant at any finite derived length at least three.'
 if key=='local-absolute-isom': lim='The explicit nonisomorphic local fields concern the dimension-zero Galois functor; the curve statement is the positive RNS absolute Isom theorem. No local curve Hom counterexample is inferred.'
 if key=='full-support-normalizer': lim='Classifies cofinite prime support (in particular Zhat) and all subgroups with totally real normalizer field; does not exclude a subgroup supported at primes outside the displayed Chebotarev set.'
 if key=='cm-normalizer-field': lim='Classifies normalizer fields with no CM subfield. In the remaining case the required CM field and degree-one ell-adic place are necessary conditions, not constructions of a subgroup.'
 if key=='third-derived-obstruction': lim='Excludes the actual coefficient-five involution from the projected commutant at derived length three over Q and K0=Q(mu15,E[5]). Does not compute the whole third-derived commutant or assert this exclusion over arbitrary larger number fields.'
 if key=='third-derived-second-digit': lim='Explicit modulus25 certificate; the subsequent structural A:third-derived-IA theorem excludes the entire nonidentity unit family. The whole same-level commutant remains undetermined.'
 if key=='third-derived-IA': lim='Eliminates the entire IA image from derived length three to two. Does not eliminate the kernel of Out(S3)→Out(S2). The subsequent multiplier theorem settles the scalar part in the peripheral case.'
 if key=='metabelian-multiplier': lim='Determines the abelian image of the peripheral metabelian arithmetic commutant, while its nontrivial IA subgroup remains at that level.'
 if key=='third-derived-projection': lim='Determines the exact image at derived length two of every peripheral arithmetic commutant at length at least three. The same-level kernel at length three remains unresolved.'
 if key=='last-layer-unrestricted': lim='Constructs actual unrestricted third-derived arithmetic-centralizing outer automorphisms, but proves every nonidentity member fails the x peripheral condition. It does not supply an element of the remaining peripheral kernel.'
 if key=='haar-block-obstruction': lim='Rules out the specified central normal-pro-prime-to-ell Haar-idempotent inversion strategy. It does not classify arbitrary last-layer endomorphisms or determine the remaining peripheral kernel.'
 if key=='split-normalizer': lim='Uses the supplied unrefereed local section theorem through F.31. Proves cuspidality exactly for normalizers admitting a section after finite arithmetic base extension; no assertion that arbitrary normalizers virtually split is made.'
 if key=='normalizer-prime-complement': lim='Proves a genuine quotient splitting and identifies the remaining section-lifting problem with a pro-prime-to-ell geometric kernel. Does not solve that embedding problem or exclude a noncuspidal normalizer. Only the concluding failure of all virtual lifts uses the supplied local theorem through A.61.'
 if key=='prime-complement-counterexample': lim='Refutes automatic virtual splitting for abstract profinite extensions of a number-field Galois group with pro-prime-to-ell kernel. No realization of this extension inside an arithmetic curve group, and hence no geometric normalizer counterexample, is asserted.'
 if key=='proper-normalizer-restrictions': lim='Extends the proved restrictions to proper hyperbolic targets, with no cusp alternative. Does not exclude all CM and restricted-prime-support cases. Only the no-virtual-section conclusion uses the supplied unrefereed local theorem.'
 if key=='one-layer-class-preservation': lim='After removing the unique geometric cusp permutation, proves preservation of every individual conjugacy class one derived layer below. The conjugator may depend on the element; no common inner conjugator for every derived length is inferred.'
 if key=='third-derived-class-rigidity': lim='Proves full profinite class-preserving rigidity at derived lengths two and three and the exact image of the fourth-level peripheral commutant at level three. Does not compute the same-level peripheral commutant at level three or eliminate the kernel at level four.'
 rows.append(dict(id=f'A.{n}',label=label,status=status,statement=title,proof_location=f'sections/A.tex#{label}',task_ids=task,passage_anchors=anchors,sources=sources,limitations=lim))
(root/'A_results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'numbered_statements':len(rows),'statuses':{x:sum(r['status']==x for r in rows) for x in ['Proved','Known','Refuted','Open']},'unmapped':[r['label'] for r in rows if r['task_ids']==['A:UNMAPPED']]},indent=2))
