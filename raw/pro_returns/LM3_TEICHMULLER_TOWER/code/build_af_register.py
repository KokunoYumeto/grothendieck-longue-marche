from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
deps={
'A.1':[], 'A.2':['A.1','AF_FarbMargalit2012'], 'A.3':['A.2','AF_FarbMargalit2012'],
'A.4':['A.2','A.3'], 'A.5':['A.1','AF_FarbMargalit2012','AF_BGH2020'],
'A.6':['A.3','A.5','C.2','C.3','D.14'], 'A.7':['A.2','A.6'],
'A.8':['A.1','A.2','A.7'], 'A.9':['A.6','A.7'], 'A.10':['A.8','A.9','D.17'],
'A.11':['A.1','A.2'], 'A.12':['A.1','A.6'], 'A.13':['A.3'],
'F.1':['A.1','AF_Jansen2023'], 'F.2':[], 'F.3':['F.2'],
'F.4':['F.2','AF_Hoyois2018'], 'F.5':['B.2','AF_Boggi2020'],
'F.6':['F.5','A.2'], 'F.7':['F.1','F.2','F.5','F.6'],
'F.8':['F.2','F.6','F.7','C.2'], 'F.9':['F.1','F.2','F.7','AF_BGH2020'],
'F.10':['F.9','D.16'], 'F.11':['F.5','F.7','F.8','F.10'],
'F.12':['F.2','F.5','F.7','AF_BoggiFunar2023','AF_Boggi2026'],
'F.13':['F.12','E.4','AF_HarbaterSchneps2000'],
'F.14':['F.10','F.12','F.13','E.8','AF_HarbaterSchneps2000'],
'F.15':['F.1','F.2','F.5','F.6','F.7','F.9','F.10','B.2'],
'F.16':['F.15','E.10','E.11','E.13','E.14'],
'F.17':['E.19','E.20','E.26','Drinfeld1990','BarNatan1998'],
'F.18':['F.2','F.7','F.9','AF_BGH2020']
}
passages={
'A.1':'19; 102r–v and 112–113; 204–205 and 224–226',
'A.2':'19; 111–113; 221–226',
'A.3':'19; 103–111; 206–221',
'A.4':'19 and 28; 102–111 and 177–180; 204–221 and 350–356',
'A.5':'21 and 26; 128–131 and 165–166; 255–261 and 326–329',
'A.6':'26; 165–166; 326–329',
'A.7':'26; 162–163; 320–323',
'A.8':'26 and 29; 162–163 and 188–189; 320–323 and 371–374',
'A.9':'26 and 29; 164–165 and 187–188; 324–326 and 370–371',
'A.10':'29; 189–190; 373–376',
'A.11':'19 and 21; 111–115 and 129–131; 222–230 and 257–261',
'A.12':'19 and 34; 114–115 and 245–248; 228–230 and 483–490 (scope)',
'A.13':'21; 126–132; 251–263',
'F.1':'19; 102r–v; 204–205 (mapping-class convention); new categorical bridge',
'F.13':'26 and 29; 164–168 and 187–190; 324–332 and 370–376 (comparison only)',
'F.14':'26,29,33; 164–168,187–190,242; 324–332,370–376,479 (comparison only)',
'F.15':'36; 255–256; 503–505 (elliptic comparison); new categorical construction',
'F.16':'36; 255–256; 503–505 (elliptic comparison)',
'F.17':'33; 242; 479 (rational analogue); no claim that this construction is in the manuscript'
}
doubt={
'A.1':r'204: \unsure{x_{g,i}|a_{g,i}}, positive versus zero indexing; reindexing harmless',
'A.2':r'222: \unsure{pointées|ponctuées}; based target supports pointées',
'A.5':r'258: \unsure{i|\nu} and \unsure{\nu-1|i-1}; 261: changing-genus chain, mathematical correction only',
'A.7':'320: injection explicitly assumed, not proved; no doubtful alternative used',
'A.8':r'321: \unsure{ou} \unsure{pré-discrétification}; closure denominator distinguishes the meanings',
'A.9':r'324: \unsure{\mathcal N|N}; symbol has no mathematical effect; 370–371 new image definition',
'A.10':'No doubtful alternative affects the orbit proof',
'A.11':r'226: \unsure{(-1,-1)|(-1,1)} supports (-1,1) for permutation/orientation; 227: \unsure{g|0} supports 0; 261: switched subscripts',
'A.13':r'252: \unsure{U|\widetilde U} supports U; \unsure{\times|\rtimes} supports direct product in specified pullback'
}
notes={
'A.11':'Includes the explicit correction rho_pi=rho_permutation*orientation in the cylinder case; literal identifications on scans225 and227 are false.',
'A.13':'For a genuine surface action use the topological lift group or the homotopy quotient; no arbitrary splitting of the Birman extension is introduced.',
'F.2':'Strict actual transition functors; quotient by natural isomorphism only.',
'F.3':'Finite counterexample [1] versus point; subterminal counts3 versus2; program output attached.',
'F.4':'GALOIS F.4 is not refuted. It correctly distinguishes split representations from the classifying topos; the stronger misreading is false.',
'F.7':'Cofinality in all finite functors is proved using the full induced topology on stabilizers; residual finiteness alone would not suffice.',
'F.9':'Finite-set exodromy with specified stalk/evaluation functors. Full infinity-categorical comparison is separately stated in F.18.',
'F.11':'The obstruction is H^1 with finite continuous coefficients, not failure of ordinary connectedness.',
'F.13':'Common cyclotomic exponent and coherent symmetric-group action are explicit. Galois surjectivity onto this group remains E.8.',
'F.15':'Graph symmetries and central elliptic involutions retained; no coarse-space substitution.',
'F.16':'Audit-unresolved comparison, not a claim that the existence of positive-genus GT actions is open.',
'F.17':'Known operadic/groupoid analogue. Motive surjectivity is conditional E.20; no unproved termwise boundary-Malcev comparison is asserted.',
'F.18':'Audit-unresolved stronger comparison; finite-set comparison F.9 is proved and suffices for the stated categorical automorphism result.'
}
rows=[]
for name in ['A.tex','A_continuation.tex','F.tex','F_continuation.tex']:
 p=root/'sections'/name;s=p.read_text()
 ms=list(re.finditer(r'^\\statement\{([^}]+)\}\{([^}]+)\}\{(.*)\}\s*$',s,re.M))
 for i,m in enumerate(ms):
  ident,status,title=m.groups()
  block=s[m.end():ms[i+1].start() if i+1<len(ms) else len(s)]
  claim=block.split(r'\begin{proof}',1)[0].strip()
  claim=re.sub(r'\\Man\{[^}]*\}\{[^}]*\}\{[^}]*\}\.?','',claim)
  claim=re.sub(r'\s+',' ',claim)
  rows.append(dict(id=ident,statement=title+'. '+claim,status=status,
   where_proved=f'sections/{name}, Statement {ident}',
   depends_on='; '.join(deps[ident]),
   manuscript_passages=passages.get(ident,'None: new categorical bridge requested in Part F'),
   depends_on_doubtful_reading=doubt.get(ident,'No'),
   notes=notes.get(ident,'Full hypotheses and proof/source scope in the cited statement. TeX math retained for precision.')))
(root/'audit'/'AF_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')

readings=[]
def add(package,scan,place,support,strength):
 readings.append({'package':package,'scan':str(scan),'place':place,'support':support,'strength':strength})
add('LM_P021',204,r'\unsure{x_{g,i}|a_{g,i}}; positive enumeration versus 0≤i≤ν−1','Names do not matter; the finite set must have ν distinct points. A reindexing reconciles the conventions.','Strong structural support; image inspected; no palaeographic settlement.')
add('LM_P021',206,r'A_g \unsure{=|\supset} A^!_{g,0}','Equality holds because fixing the empty marked set imposes no condition; containment is true but weaker.','Decisive mathematically; image not inspected.')
add('LM_P023',222,r'\unsure{pointées|ponctuées}','The based fundamental group functor needs a chosen ordinary base point, so pointées is the mathematically appropriate reading. Punctures remain part of type (g,ν).','Strong mathematical support; image not supplied.')
add('LM_P023',223,r'Aut(\unsure{X_{1,1}|U_{1,1}},a_{1,0})','If a_{1,0} is the deleted marked point, it is not a point of U_{1,1}; fixing it is interpreted on the compactification X.','Conditional on the local convention for the marked point; no image supplied.')
add('LM_P023',225,r'\unsure{\nu|2}; subscripts g,2 in the g=0 paragraph','Here ν=2 and g=0. The cylinder table in A.11 applies only with that substitution.','Strong contextual and mathematical support.')
add('LM_P023',225,r'Identification of (51) with (51 bis), adjoining doubtful/deleted words','If the first rho acts on π1 and the second permutes the ends, they differ by orientation: rho_pi=rho_perm*epsilon. Complex conjugation is a complete counterexample to literal equality.','Mathematically decisive correction; does not establish what was written.')
add('LM_P023',226,r'\unsure{\rho|\chi} in the pair; \unsure{(-1,-1)|(-1,1)} for z↦1/z','The pair is permutation and orientation, hence (rho,chi); inversion swaps the two punctures and is holomorphic, giving (-1,+1).','Decisive with the explicitly stated convention; image not supplied.')
add('LM_P023',227,r'\Gamma^+_{\unsure{g|0},3}','The isomorphism with S3 requires genus zero, so 0 is supported; it fails for arbitrary genus.','Decisive mathematically; image not supplied.')
add('LM_P023',227,r'Rank-one determinant-one image sentence following the doubtful genus subscript','The orientation-preserving cylinder transposition acts by -1 on Z; the literal determinant-one claim in rank one is false. The torus determinant-one statement is correct.','Counterexample supplied in A.11; not a palaeographic conclusion.')
add('LM_P023',228,r'\Gamma^!_{g,\unsure{1|2}} and \Gamma_{\unsure{0|g},1}','The stabilizer identified with the once-punctured-sphere mapping class group is the pure two-point sphere group; g=0 in this paragraph. Supports 2 and 0.','Strong mathematical support; no image supplied.')
add('LM_P026',252,r'\Pi_{g,\nu}=\pi_1(\unsure{U_{g,\nu}|\widetilde U_{g,\nu}},a_{g,\nu})','The deck group of the universal cover is π1(U); π1 of the universal cover is trivial. Supports U.','Decisive mathematically in the hyperbolic setting; no image supplied.')
add('LM_P026',252,r'A^\circ_{g,\nu}\unsure{\times|\rtimes}\Pi_{g,\nu}','For the explicitly defined pullback A×_ΓΓ_* the kernel over Γ is A^circ×Π with componentwise multiplication. A nontrivial semidirect action is not present.','Proved in A.13; no image supplied.')
add('LM_P026',253,r'\unsure{v^{-1}} in the right-translation action','Converting a left action to right translation introduces the inverse. The convention is essential; reversing all action conventions reverses this formula.','Strong convention-dependent support; no image supplied.')
add('LM_P026',258,r'\pi_{\unsure{i|\nu}}(\widetilde M) ≅ \pi_{\unsure{\nu-1|i-1}}(A^\circ)','For a free A^circ-action with contractible total space, the homotopy sequence gives π_i(base)≅π_{i−1}(A^circ). The variable is the homotopy degree i, not the puncture count ν.','Decisive under the freeness hypothesis; does not extend to nonfree exceptional cases.')
add('LM_P026',260,r'g\unsure{=|\neq|\geq}1 ou 0','The reductions are closed genus≥2, the once-punctured torus for g=1, and the three-point sphere for g=0. The intended alternatives here are equality to1 or0.','Strong mathematical support.')
add('LM_P027',261,r'\widetilde M_{3,0}→\widetilde M_{2,0}≃\widetilde M_{1,0}≃\widetilde M_{\unsure{00|0,0}}','The changing-genus chain is false by dimensions. The surrounding sphere argument supports M_{0,3}→M_{0,2}→M_{0,1}→M_{0,0}; all are points.','Decisive inconsistency and strong proposed mathematical correction; scan image absent.')
add('LM_P027',263,r'Final extension called \Gamma^{prime}_{g,\nu} after discussion of \Gamma^{prime}_{g,\nu+1}','The mixed group is the extension for one additional distinguished point, so the consistent subscript is ν+1.','Proved in A.13; no image supplied.')
add('LM_P027',266,r'\unsure{\Pi_{B_U}|\Pi_{B_{D^*}}} containing rho_!(D*)→U','Both rho_!(D*) and U lie in the target covering groupoid Π_{B_U}; the Hom must be taken there.','Decisive type check; editorial observation outside the main deductions.')
add('LM_P033',321,r'\inserted{\unsure{ou} \unsure{pré-discrétification}}; natural/sharp and S/G glyph alternatives','The stabilizer is explicitly the closure of the discrete automorphism group, so this is the prediscretization quotient, not the raw embedded lattice set. Glyph choices do not alter the quotient argument.','Strong mathematical support; scan visually inspected by root.')
add('LM_P033',328,r'Folio \unsure{166|168}','The surrounding folio sequence supports166; the mathematics depends only on the sequence labels, not this folio digit.','Weak chronological support; no mathematical settlement.')
(root/'audit'/'AF_readings.json').write_text(json.dumps(readings,indent=2,ensure_ascii=False)+'\n')
print(f'AF: {len(rows)} statement rows, {len(readings)} reading rows')

