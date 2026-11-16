"""Merge the proved statement records and regenerate the live research report."""
from pathlib import Path
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent / 'work'
fields = ['id','statement','status','where_proved','depends_on','answers (lead or task)','notes']
rows = {}
for name in ('a_main_rows.json','a_main_census_rows.json','a_main_local_rows.json','a_main_quintic_rows.json','a_main_badprime_rows.json','a_main_quotient_rows.json','a_main_rankone_rows.json','a_main_finiteprime_rows.json','a_main_abelian_fibres_rows.json','a_main_unit_rows.json','a_main_infinite_valuation_rows.json','a_main_congruence_rows.json','a_main_finite_congruence_rows.json','a_main_finite_support_rows.json','a_main_uniform_three_rows.json','a_main_uniform_finite_support_rows.json','c_b_detector_rows.json','b_rows.json','c_rows.json','c_B29_B30_rows.json','c_B42_rows.json'):
    p = WORK / name
    if p.exists():
        for source in json.loads(p.read_text()):
            row = {k: source.get(k,'') for k in fields}
            row['answers (lead or task)'] = source.get('answers (lead or task)',source.get('answers',''))
            rows[row['id']] = row

rootmap = {
17:'R8; D.2; B.1; manuscript Section 51.16 equations (373)--(379)',
20:'A.2; A.3; R7',21:'A.2; A.3',22:'A.2; R19',23:'A.5; A.6; Lead 2',
24:'A.4; A.5; A.6; Lead 2',25:'A.4; A.6',26:'A.6',27:'A.5',
28:'A.9; A.10; Lead 4',29:'A.10; Lead 4',30:'A.11; Lead 4',
31:'A.9; A.10; Lead 4',32:'A.8; R20',33:'A.5; A.6; A.7',
34:'A.6; A.7',35:'A.4; A.5; A.6; A.7',36:'A.4; A.5; A.6; A.7; Lead 2',
44:'A.12; Lead 5',45:'A.12; Lead 5'}

def group(text, pos):
    assert text[pos]=='{'
    start=pos+1; depth=1; pos+=1
    while depth:
        if text[pos]=='{': depth+=1
        elif text[pos]=='}': depth-=1
        pos+=1
    return text[start:pos-1],pos

present=[]
for path in sorted((ROOT/'sections').glob('*.tex')):
    text=path.read_text()
    marker=r'\begin{statement}'
    starts=[m.start() for m in re.finditer(re.escape(marker),text)]
    for index,start in enumerate(starts):
        pos=start+len(marker); vals=[]
        for _ in range(3):
            while text[pos].isspace(): pos+=1
            value,pos=group(text,pos); vals.append(value)
        sid,title,status=vals
        body=text[pos:starts[index+1] if index+1<len(starts) else len(text)]
        present.append(sid)
        if sid not in rows:
            answer=rootmap.get(int(sid.split('.')[1]),'') if sid.startswith('A.') else ('C.2; Lead 8; cross-ratio route in supplied note' if sid in ('C.23','C.24') else ('D.1' if sid=='D.1' else 'D.2; A and B manuscript concordance'))
            cites=sorted(set(re.findall(r'\\cite[pt]?[^\{]*\{([^}]+)\}',body)))
            rows[sid]=dict(zip(fields,[sid,title,status.split(',')[0].split(';')[0].split(' ')[0],f'sections/{path.name}, {sid}','; '.join(cites),answer,status]))
        else:
            rows[sid]['status']=status.split(',')[0].split(';')[0].split(' ')[0]
            rows[sid]['where_proved']=f'sections/{path.name}, {sid}'
assert len(present)==len(set(present)), 'Duplicate statement IDs in source files'
present=sorted(present,key=lambda s:(s[0],int(s.split('.')[1])))
with (ROOT/'FERMAT_SUCCESSOR_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fields); writer.writeheader()
    writer.writerows(rows[s] for s in present)
assert len(present)==len(set(present))

bibs=[WORK/n for n in ('a_main_references.bib','root_references.bib','b_references.bib','c_references.bib','c_b_references.bib')]
bibtext='\n\n'.join(p.read_text() for p in bibs if p.exists())
for match in reversed(list(re.finditer(r'\bnote\s*=\s*\{',bibtext))):
    start=match.end()-1
    value,end=group(bibtext,start)
    value=re.sub(r'(?<!\\)_',r'\\_',value)
    bibtext=bibtext[:start]+'{'+value+'}'+bibtext[end:]
(ROOT/'FERMAT_SUCCESSOR_references.bib').write_text(bibtext)

tasks=[
('A.1','A.1–A.11','Proved after correcting the cusp Tate constant; all-place Selmer hypotheses retained.'),
('A.2','A.20–A.22','Proper-to-affine deduction proved conditional on the stipulated local theorem; density inference corrected, global replacement still qualified.'),
('A.3','A.16, A.20–A.21','Proved for Selmer sections of every classical exponent; all sections conditional on the local theorem.'),
('A.4','A.12–A.15, A.24–A.25, A.33–A.36','Proved for the stated rank-zero quotient criterion; all three CM orders are Z[i].'),
('A.5','A.23–A.24, A.27, A.33–A.36','Finiteness false when a cusp packet occurs; geometric classification and exact packets proved.'),
('A.6','A.23–A.26, A.33–A.36','Rank-zero criteria and complete finite ordinary-point lists plus full cusp packets proved.'),
('A.7','A.33–A.42','Complete: all 3185 coefficient ranks certified and all 6,987,169 parameter pairs tabulated; 6,905,782 pairs meet a stated criterion, with complete point and cusp dictionaries.'),
('A.8','A.32','Rank-zero consequences proved; arbitrary positive-rank and noncuspidal finite-ramification problem not solved.'),
('A.9','A.28, A.31, A.48, A.55','INCOMPLETE independently for full global sections at bad primes: simultaneous recognition proved at good primes; all primes follow with the stipulated local theorem. A genuine local septic point at seven refutes the unrestricted local extension, without supplying a global counterexample.'),
('A.10','A.28–A.29, A.31','One completed parameter proved at good primes and, using the stipulated local theorem, all primes; the ordinary-integer interpretation is false.'),
('A.11','A.30, A.46–A.49, A.56–A.58','Exact exceptional set and quotient-level independence proved at every exceptional prime, with explicit global residual witnesses. A sufficient level-at-most-16 plus cofinal finite-abelian-descent hypothesis is proved. INCOMPLETE: weakest independent hypothesis for actual full hyperbolic sections and its necessity remain unresolved.'),
('A.12', 'A.43–A.45, A.59–A.71', 'Every exponent lifts abstractly to the exact full cuspidally central quotient. With Selmer conditions, A65 gives the exact abelian and intrinsic metabelian exponent sets among scalars that are units at almost all coefficient primes; A66 additionally settles the stated infinite nonunit valuation profiles. All abelian Selmer fibres above rational compact points are computed. A67 constructs the actual joint compact/j-line congruence quotients. A68–A71 then completely classify their level-three Selmer exponents among every finite alteration of every integer, uniformly on every cubic twist with a rational infinity origin and a nontorsion rational point: only the unchanged integer lifts. This includes finite support around zero and the exceptional coefficient primes two and three; the first listed finite congruence refinement therefore supplies the requested uniform one-extra-prime obstruction. INCOMPLETE: arbitrary infinite alterations, full metabelian fibres, and complete congruence lifting sets remain unresolved.'),
('B.1','B.1–B.3','Proved for the Legendre-relative derived residual and cubic/classical quartic prosolvable groups.'),
('B.2','B.4, A.50–A.53','Both septic and quintic maximal-prosolvable Selmer section sets are cuspidal. Quintic uses the explicitly identified Known Hilbert modular rank-zero theorem and a rigorous degree-four L-value certificate.'),
('B.3','B.5–B.6, B.12, B.18, B.26–B.27','Proved: least positive derived length is k=1 for cubic and quintic. At every 3-power and 5-power Fermat level, all whole pro-primary cocycles unramified outside the coefficient prime are Selmer exactly in the three global cusp packets. The full profinite zero-abelian metabelian families have the separate classification of B.6.'),
('B.4','B.13, B.19–B.22, B.35–B.40','Resolved with correction of the proposed finite test. The actual arithmetic Ross edge is nonzero and spans its one-dimensional rational space; the action coefficient is -1 relative to that edge, or -1/6 relative to its tame multiple. The complete geometric extension selects the unique integral refinement: local Smith vector b+6h9, with intrinsic detector values57 modulo81 and19 modulo27. The Ross symbol has the separately normalized Hodge coordinate -3/2. The prescribed inherited order-3^30 test is refuted as incapable because it kills the relevant commutator module; B39 supplies an actual intrinsic finite quotient and B40 evaluates its required invariant.'),
('B.5','B.7, B.10–B.13, B.17, B.28, B.31–B.32, B.35–B.36, B.41, B.43','Every nonempty class-three fibre is evaluated integrally. The entire zero-abelian slice has an exact order-and-decay law with unbounded local orders. Every unscaled kappa_3(p)w at p other than three is obstructed. The exact local order at two is 27, so the entire two-supported zero-abelian input lifts exactly when its valuation coefficient is divisible by 27. B41 proves that the Ross extension does not determine arbitrary-input lifting: a primitive cubic arithmetic-action deformation preserves that extension but changes local liftability and the class-two cusp origins. B43 specifies two actual compatible Heisenberg projections of cusp origins, including exact finite Frobenius data and the two independent homogeneous comparison rows. The full quadratic comparison to a specified reference origin remains necessary. INCOMPLETE: the actual missing action components, other exact local orders and the image for arbitrary ramified inputs remain unevaluated.'),
('B.6','B.13','INCOMPLETE: intrinsic/marked-to-inherited full image and fibres unresolved.'),
('B.7','B.23–B.25','Complete explicit class-two image law: 44 cubic corrections from a 2-by-2 inverse with integral gluing, and 55 quartic tame-symbol tests plus exact local Kummer orders. Necessity, sufficiency, nonadditivity and unbounded orders proved.'),
('B.8','B.8','Factor-two Ceresa comparison and rank-two CM carrier proved; no new nonvanishing assertion.'),
('B.9','B.14','INCOMPLETE: full profinite metabelian classification across all coefficient primes unresolved.'),
('B.10','B.14, B.29–B.30, B.33–B.34, B.42','Rational cusp forcing in (b), and its metabelian/marked versions in (c), is false: actual full pro-3 families ramified at seven are constructed, including a noncuspidal family whose local colour is a rational cusp. All cocycles unramified outside three and seven have an exact local parametrization. B42 proves common colours for full sections at all ramified inert primes with v3(q+1)<=3, and more generally <=3+v3(b), where b is the free compact coordinate. It also proves that the compact threshold is sharp without claiming a ramified two-prime example. INCOMPLETE: unrestricted equality at distinct rational primes in (a) and the corresponding part of (c) remains unresolved.'),
('B.11','B.7, B.14','Class-three form refuted by an explicit infinite-ramification lift; full pro-3 equivalence unresolved.'),
('B.12','B.15–B.17','Explicit 44-coordinate phantom and degree-three comparison proved; fibre discrepancy reconciled as 23+1.'),
('B.13','B.9–B.11','Actual full pro-3 lifting over the cyclotomic tower proved, with compact-lattice H2 vanishing there; descent back to Q is the literal coinvariant quotient, retaining its nonclosed-image lim1 part.'),
('C.1','C.1–C.5','Whole relative lifting and compatible conjugators proved, including fixed-fibre CM comparison.'),
('C.2','C.6–C.7, C.18–C.20, C.23–C.24','INCOMPLETE: both CM parities and their quotient computed; a single Galois element matches the whole adelic CM pair. Full G6 equality and icosahedral membership remain open; four-point common-kernel route has explicit counterexamples.'),
('C.3','C.8–C.9','INCOMPLETE: residual exact-sequence law proved; membership modulo specified lower changes unresolved.'),
('C.4','C.10–C.12, C.25','All deep finite certificates replayed. D32 has a retained nonnilpotent source; D45 obstructs a fixed cusp frame but admits an explicit next-layer lift with cusp conjugation. INCOMPLETE: exclusion on the whole relative completion remains open.'),
('C.5','C.13–C.14','Weight-nine exclusion proved conditional on precisely the R16 inputs exempted by the prompt; R18 scope corrected.'),
('C.6','C.15, C.26–C.28','INCOMPLETE: Delta on full GT remains unresolved. The folded test is identically blind; affine sieves are computed; a distinct Burau test has perfect common derived image and cannot eliminate any solvable CM shadow.'),
('C.7','C.16–C.18','Literal whole-product assertion false; corrected mod-2 projective product surjectivity and sole parity obstruction proved.'),
('C.8','C.21–C.22','Primary-source search recorded; no priority asserted; literature gaps distinguished from proved results.'),
('D.1','D.1','Completed against the original official cote145 scans. The raw gamma is the gauge orbit of g; inversion and the explicit abelian normalization give f_GT=y^a1 g^(-1)x^a0. The manuscript rho is a three-cycle, beta=(chi-1)/2, and the isotropy splittings at the equianharmonic and harmonic points are directly verified.'),
('D.2','D.2–D.4; individual concordance table','Every A/B statement has a section/folio/scan link and an individual answer beside a quoted question key. The original official scans167--178 have now been independently inspected, confirming the folios, questions, old twist sign and original scan178 inconsistency. Global joint and exact local-inertia Kummer images are proved, including all 2-primary exceptions.'),
('Lead 1','B.1–B.2','Proved in the stated relative quotient; expectation about each finite derived layer not established in general.'),
('Lead 2','A.23–A.27, A.35–A.36','Geometric classification proved; claim of finitely many sections refuted by cusp packets.'),
('Lead 3','B.19–B.22, B.36–B.40','Resolved: the arithmetic Ross edge is a nonzero generator, the action coefficient relative to it is -1, and its tame-normalized coefficient is -1/6. The symbol itself has real-regulator coordinate -3/2. The actual geometric extension selects the integral refinement with detector57 modulo81, or19 modulo27 on the primitive commutator module. The requested inherited test is refuted; the intrinsic replacement is specified and evaluated. No numerical three-adic regulator is claimed.'),
('Lead 4','A.28–A.31, A.46–A.49, A.55–A.58','Good-prime completed compatibility proved; exact exceptional quotient information and explicit sufficient residual/descent hypotheses established. INCOMPLETE: independent full-section sufficiency at bad/coefficient primes remains open.'),
('Lead 5', 'A.43–A.45, A.59–A.71', 'Full cuspidally central abstract survival is proved. Abelian Selmer exclusion covers all nonintegral exponents that are units at almost all coefficient primes, all finite alterations on CM curves, and the infinite nonunit valuation profiles in A66. A67–A71 prove that the actual joint level-three quotient excludes every nontrivial finite alteration of every integer, uniformly across all rational-origin cubic twists carrying a nontorsion rational point. The uniform coefficient-three proof includes dyadically ramified twists; the finite-support proof also includes coefficient two. INCOMPLETE: remaining infinite exponent classes and complete congruence-cover lifting sets remain unresolved.'),
('Lead 6','C.6–C.7, C.18','INCOMPLETE: exact CM pair matches a Galois element; equality of full retained actions unproved.'),
('Lead 7','C.16–C.18','Refuted literally; corrected mod-2 product and index-two arithmetic image proved.'),
('Lead 8','C.19–C.24','The multiplier-one group is torsion-free, hence finite K would be trivial. Four-point tests have explicit common-kernel witnesses in both symmetry families. Actual membership of the two specified lifts remains unresolved.'),
('Lead 9','B.9–B.11','Proved for the actual natural pro-3 action over Q(mu_3-infinity): every quotient section lifts to the full group. Compact-lattice H2 also vanishes there; the phantom obstruction returns in descent to Q.')]
report=['INCOMPLETE','','| Task or lead | Statements | State reached |','|---|---|---|']
report += ['| '+' | '.join(t)+' |' for t in tasks]
report += ['','## Scope and provenance','','AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. This is a live research checkpoint, not a claim that the requested programme is complete. Status Proved always retains explicitly stated theorem hypotheses, including conditional use of the supplied unrefereed local theorem.','',
'## Sources opened and computations executed','',
'Primary theorem texts, exact local proofs and bibliography verification are recorded in the paper and the work audit notes. In particular Stoll (including the erratum), Harari–Stix, Mazur, Serre, Kisin, Rubin, Hain–Matsumoto, and the CM and profinite-centralizer sources were opened. Download attempts and failures are retained. The initial Rubin LOG0034 candidate was an unrelated O’Farrell paper; it was rejected and replaced by the correct LOG0029. No claim relies on the rejected candidate.','',
'Executed code and its output are under code/. The CM census uses PARI exact arithmetic for models, conductors, signs and Fourier coefficients, with Arb interval bounds for analytic nonvanishing and derivatives. It does not call ellanalyticrank as a certificate. The full coefficient tables and compressed pair CSVs are included. The finite symbolic maps and counterexamples are checked by exact arithmetic.','',
'## Principal corrections','',
'The Fermat cusp Tate parameter has constant 1/256, so the claimed residual divisibility at 2 is false. The corrected modularity argument has Serre level 2. Stoll’s finite-support step still requires all-place descent; density one concerns only the supporting finite subscheme. The Gaussian quartic quotients have CM by Z[i], not Z[sqrt(-2)]. Rank-zero twist fibres with cusps have infinite cusp packets. The real place has component classes rather than a distinct global-style packet for every cusp side. The density-one/positive-density intersection inference belongs to Porowski’s global argument and is not a refutation of the supplied proper local theorem. R18 concerns Galois-commuting lifts and cannot be read as excluding every peripheral lift. The literal whole projective CM product omits the necessary mod-2 condition. The LM7 D32 source is relative to its retained nonnilpotent finite quotient.','',
'## Undecided lines and next steps','']
for t in tasks:
    if 'INCOMPLETE' in t[2]: report.append(f'- **{t[0]} ({t[1]}):** {t[2]} See the corresponding numbered Open statement and audit note for the exact obstruction, attempts and next comparison required.')
supplement=ROOT/'records'/'report_detailed_audit.md'
if supplement.exists(): report += ['',supplement.read_text().strip()]
qa=ROOT/'records'/'pdf_qa.json'
if qa.exists():
    q=json.loads(qa.read_text())
    qa_text=(f"The inspected PDF has {q['pages']} pages. In the last pre-repair build, {q['overfull_over_2pt_before']} overfull boxes exceeded 2 pt; the inspected build has {q['overfull_over_2pt_after']}. "
             f"Rendered page images inspected: {', '.join(map(str,q['viewed_pages']))}. Every previously overflowing passage was inspected again. "
             "The exact PDF digest, build-log checks, earlier defects and page-review notes are in records/pdf_qa.json. A subsequent edited PDF is not certified by that older digest.")
else: qa_text='Layout verification is in progress. No working PDF is certified for publication until the final overflow check and page-image inspection are recorded.'
report += ['','## Typesetting and verification','','The LuaLaTeX environment needed a local format and four missing runtime packages; exact fetch digests and build logs are retained. '+qa_text,'',
'## Preservation and exclusions','','Hourly checkpoint archives preserve the current deliverables and research notes. Superseded versions are retained in checkpoint history; the final package will preserve that history or list every exclusion. Attached input material and raw third-party source PDFs are excluded. Installed PARI/TeX runtime trees and caches are reproducible dependencies, not deliverables; fetch/build scripts, version/digest records and mathematical output are retained. Reproducible page-render PNGs and working PDF copies are excluded: the exact certified deliverable PDF, render script, inspected-page list, digest and visual-review record are preserved. This exclusion does not remove a distinct mathematical draft or research note.']
(ROOT/'FERMAT_SUCCESSOR_report.md').write_text('\n'.join(report)+'\n')
print(json.dumps({'statements':len(present),'task_and_lead_rows':len(tasks),'statuses':{s:sum(rows[k]['status']==s for k in present) for s in ['Proved','Known','Refuted','Open']}}))
