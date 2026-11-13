"""Assemble the statement/readings/coverage ledgers and combined bibliography.

This script checks identities and coverage; it makes no mathematical claims
beyond the separately proved and computed statements in the source sections.
Run from any directory with Python 3. No network or nonstandard package needed.
"""
from pathlib import Path
from collections import Counter
import csv, json, re

BASE = Path(__file__).resolve().parents[1]
LEDGER = BASE / 'ledger'
PREFIX = 'LM7_FERMAT_TOWER'

def statements(path):
    text = path.read_text()
    marker = r'\begin{statement}'
    pos = 0
    out = []
    while True:
        start = text.find(marker, pos)
        if start < 0:
            return out
        p = start + len(marker)
        args = []
        for _ in range(3):
            while text[p].isspace(): p += 1
            assert text[p] == '{', (path, p)
            level, q = 1, p + 1
            while level:
                if text[q] == '{' and text[q-1] != '\\': level += 1
                if text[q] == '}' and text[q-1] != '\\': level -= 1
                q += 1
            args.append(text[p+1:q-1])
            p = q
        end = text.index(r'\end{statement}', p)
        out.append({'id': args[0], 'status': args[1], 'title': args[2],
                    'body': re.sub(r'\s+', ' ', text[p:end]).strip(),
                    'source': str(path.relative_to(BASE))})
        pos = end + len(r'\end{statement}')

e_deps = {
 'E.1': [], 'E.2': ['E.1'], 'E.3': ['E_HainMatsumoto', 'E_BrownDepth'],
 'E.4': ['E.2', 'E.3'], 'E.5': [], 'E.6': [], 'E.7': ['E.6'],
 'E.8': ['E.6'], 'E.9': ['E.7'], 'E.10': ['E.7', 'E.8', 'E.9'],
 'E.11': ['E.10'], 'E.12': ['E.6', 'E.7', 'E.8', 'E.9', 'E.10'],
 'E.13': ['B.5', 'E.6', 'E.7', 'E.8', 'E.9'],
 'E.14': ['E.7', 'E.9'], 'E.15': ['E.14'],
 'E.16': ['B.1', 'C.2'], 'E.17': ['E.16', 'E_Wickelgren'],
 'E.18': ['B.1', 'E.16'], 'E.19': ['C.4', 'E.17'],
 'E.20': ['E.16'], 'E.21': ['E.2'],
 'E.22': ['A.19', 'E.3', 'E.14', 'E.15'],
 'E.23': ['E.1', 'E.16', 'E.17', 'E.18', 'E.19', 'E.20', 'E.22']
}
e_notes = {
 'E.1': 'Exact noncommutative relation-module sequence; universal envelope specified.',
 'E.2': 'All comparison kernels explicit; no identity descent from the metabelian Lie quotient.',
 'E.3': 'Actual rationalized pro-l Galois image. Independent integer polynomial and tensor-word calculations agree.',
 'E.4': 'The same Ihara derivations are projected through the explicit quotient morphisms.',
 'E.5': 'Tests by functor groupoids prove the relative comma-category axiom on all small categories.',
 'E.6': 'Correct target is G/V(G); factorization to the original G is characterized exactly.',
 'E.7': 'Universal metabelian witness [a,tat^-1] has nonzero Alexander image.',
 'E.8': 'Image, closed-normal kernel generators, source/target ranks, and exact p-group criterion.',
 'E.9': 'Entire free-pronilpotent kernel described by Lie elimination; original finite target does not descend.',
 'E.10': 'Uniform base-change counterexamples and pro-p converse prove intrinsic-fibration classification.',
 'E.11': 'Finite S3 orbit counterexample verified in e_obstructions.py.',
 'E.12': '74 models, 65 two-generated groups, 9714 epimorphisms, 23634 nonisomorphism tests; saved integral witnesses.',
 'E.13': 'These are the actual covering comparison maps, including all mixed levels.',
 'E.14': 'Finite-quotient relative completion; splittings conjugate, not asserted to have a unique conjugator.',
 'E.15': 'Discrete genuine action is faithful; image is exactly the subgroup stabilizing the embedded free group.',
 'E.16': 'Every minimum-quotient section computed via roots, signs and restricted prime valuations.',
 'E.17': 'Rational cubic cusp sections coincide after the explicit minimum quotient map.',
 'E.18': 'Actual real extension is a completed free group of rank9, with index2 geometric subgroup of rank17; obstruction 1 mod2.',
 'E.19': 'Nonzero 3-torsion cusp differences have no rational 3-division; reduction at2 verifies this.',
 'E.20': 'Quaternion cup(2,3) detected at Q3 in a fully enumerated D8 quotient.',
 'E.21': 'Generator interchange gives an explicit non-descent; no LM8 return was attached.',
 'E.22': 'Actual cyclotomic Galois commutator is killed by M51 but survives the outer relative action.',
 'E.23': 'Incomplete section classification; every attempted transfer and concrete residual quotient is retained.'
}

e_rows = []
for st in statements(BASE/'sections/E.tex'):
    n = int(st['id'].split('.')[1])
    passage = ('§51.16; folios 733v–736v; scans 172–178; (369)–(379)'
               if n >= 16 else
               '§51.11 and §51.16; folios 695–697, 733v–736v; scans 95–99, 172–178; requested approximation/exactness follow-ups')
    e_rows.append({
      'id': st['id'], 'statement': st['body'], 'status': st['status'],
      'where_proved': f"{st['source']}, {st['id']} and its proof/obstruction discussion",
      'depends_on': e_deps.get(st['id'], []), 'manuscript_passages': passage,
      'depends_on_doubtful_reading': ('scan172 genus/threshold corrections; scan178 Tate sign notation retained as an editorial uncertainty'
                                     if n >= 16 else 'none; comparisons use the explicit group and ideal definitions'),
      'notes': e_notes.get(st['id'], '')
    })
(LEDGER/'e_results.json').write_text(json.dumps(e_rows, ensure_ascii=False, indent=2)+'\n')

e_readings = [
 {'package':'LM_C4-172-190','scan':'172',
  'place':'(369) crossed-out 2+ and (370) threshold3 corrected to4',
  'mathematical_support':'Euler characteristic gives g_n=(n-1)(n-2)/2; g3=1 and g4=3. This supports the inserted1 and4, and preserves the written genus-one case.',
  'strength':'Proved formula and finite computations; scan inspected as an image.'},
 {'package':'LM_C4-172-190','scan':'174–175',
  'place':'approximation minima and quotient in (373)',
  'mathematical_support':'The map is the covering pushforward N_n^ab→nZhat(1)^2; its kernel has geometric rank n²−1. After dividing the coordinate lattice by n it is the explicit torus-unit map. E.16 computes its section classes and E.17 its cusp collision.',
  'strength':'Exact morphism, including the arithmetic minus signs; supports the quotient reading without identifying full homology with rank2.'},
 {'package':'LM_C4-172-190','scan':'177–178',
  'place':'(379) Tate-module sign notation in transcription',
  'mathematical_support':'We define Zhat(1) as the inverse system of roots of unity. With that convention the root torsor has action χ and Kummer H1 is lim Q*/Q*^m. No visual settlement of an unattached scan is claimed.',
  'strength':'Mathematical convention and typed comparison only; original images not present in this attachment.'},
 {'package':'LM_C4-096-114 and LM_C4-172-190','scan':'97;172–175',
  'place':'Use of the plus-sign model when discussing section classes',
  'mathematical_support':'The plus quartic is empty over R. Its actual real arithmetic extension has a nonzero class in H²(C2,N^ab⊗Z2); the minimum torus quotient kills this class. The odd cubic admits three rational cusp tangents.',
  'strength':'Model-dependent proofs E.17–E.19 and exact finite obstruction checks; no replacement by the minus model over Q.'},
 {'package':'LM_C4-172-190','scan':'180',
  'place':'§52.1 inserted phrase de Pi ≃ Z beside the case (0,1)',
  'mathematical_support':'For genus0 with one deleted point the geometric group is trivial; Z is the twice-punctured geometric group. E.27 proves both by covering classification. The stated type and cyclic-group phrase cannot both describe the usual puncture count.',
  'strength':'Mathematical evidence only; the scan180 image is not attached, and no handwriting alternative is declared settled.'}
]
(LEDGER/'e_readings.json').write_text(json.dumps(e_readings, ensure_ascii=False, indent=2)+'\n')

e_coverage = [
 {'task':'E.a','statement_ids':['E.1','E.2','E.14'],
  'outcome':'(a) proved: third-derived module, marked-depth structure, and specified universal/relative envelopes',
  'remaining_step':'none for the stated structures; the marking is part of the depth object'},
 {'task':'E.b','statement_ids':['E.3','E.4'],
  'outcome':'(a) proved: actual rational pro-l depth2 ranks through14 and the weight12 period relation',
  'remaining_step':'none; no integral saturation claim is made'},
 {'task':'E.c','statement_ids':['E.4','E.20','E.21','E.22','E.26','E.28','E.29','E.31','E.32'],
  'outcome':'(a) actual class-two S3 obstruction and all local/rational replacements proved; inherited cubic Kummer lifting completely classified, including the continuous inverse-limit obstruction',
  'remaining_step':'none for these precise splitting and Kummer comparisons; the full intrinsic cubic classification remains in E.d'},
 {'task':'E.d','statement_ids':['E.16','E.18','E.19','E.20','E.23','E.24','E.25','E.28','E.29','E.31','E.32'],
  'outcome':'INCOMPLETE: quartic and every even plus-level empty in the specified integral quotients; cubic abelian sections and all inherited class-two pro3 sections computed; intrinsic obstructions proved',
  'remaining_step':'compute every fiber for the full rank-ten intrinsic cubic class-two quotient, then its metabelian and marked-depth refinements'},
 {'task':'E.follow-up-1','statement_ids':['E.5','E.21'],
  'outcome':'(a) all five specified group approximations satisfy the axioms; unmarked-depth assignment refuted by non-descent',
  'remaining_step':'no LM8 return was attached; no extra unmarked Lie functor is silently assumed'},
 {'task':'E.follow-up-2','statement_ids':['E.6','E.7','E.8','E.9','E.10','E.11','E.12'],
  'outcome':'(a) exact comparison and fibration classifications proved, with every requested small epimorphism checked',
  'remaining_step':'none'},
 {'task':'E.follow-up-3','statement_ids':['E.13','E.14','E.15','E.22','E.30','E.33'],
  'outcome':'(b) proposed M51 action descent refuted; exact covering and relative-completion morphisms proved; arithmetic proconstant completion kills geometry; continuous arithmetic kernel is an explicit inverse system of free groups',
  'remaining_step':'none for the stated comparison and non-descent results; abstract Q and continuous Q_l completion categories are stated independently, and the free-kernel calculation applies to the latter'},
 {'task':'E.follow-up-4','statement_ids':['E.16','E.17','E.18','E.19','E.20','E.23','E.24','E.25','E.28','E.29','E.31','E.32'],
  'outcome':'INCOMPLETE: minimum and cubic abelian sections fully computed, cusp-separation claim refuted through its explicit quotient, inherited cubic class-two sections fully classified; full intrinsic sections unresolved',
  'remaining_step':'evaluate the full intrinsic cubic class-two obstruction on every computed abelian class and all its fibers, then continue the nonabelian tower'}
]
if (BASE/'sections/E_intrinsic_positive.tex').exists():
    for row in e_coverage:
        if row['task'] in ('E.d','E.follow-up-4'):
            row['statement_ids'].append('E.34')
            row['outcome']+='; every intrinsic abelian class unramified outside3 lifts to the full pro3 extension'
if (BASE/'sections/E_intrinsic_finite.tex').exists():
    for row in e_coverage:
        if row['task'] in ('E.d','E.follow-up-4'):
            row['statement_ids'].append('E.35')
if (BASE/'sections/E_cuspidally_central.tex').exists():
    for row in e_coverage:
        if row['task'] in ('E.d','E.follow-up-4'):
            row['statement_ids'].append('E.36')
            row['outcome']+='; every cuspidally central fiber is computed over every rank-ten abelian class'
            row['remaining_step']='evaluate the obstruction and all fibers through the central rank44 kernel of E.36, then the metabelian and marked-depth refinements'
(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\n')

all_st = []
master_inputs=set(re.findall(r'\\input\{([^}]+)\}',(BASE/(PREFIX+'_paper.tex')).read_text()))
for path in sorted((BASE/'sections').glob('*.tex')):
    assert str(path.relative_to(BASE)) in master_inputs, 'Section omitted from master: '+str(path)
    all_st.extend(statements(path))
paper_ids = [s['id'] for s in all_st]
assert len(paper_ids) == len(set(paper_ids)), 'Duplicate paper statement ids'

rows = []
for path in sorted(LEDGER.glob('*_results.json')):
    rows.extend(json.loads(path.read_text()))
row_ids = [r['id'] for r in rows]
assert len(row_ids)==len(set(row_ids)), 'Duplicate ledger rows'
assert set(row_ids)==set(paper_ids), (set(paper_ids)-set(row_ids),set(row_ids)-set(paper_ids))
by_id = {s['id']:s for s in all_st}
for r in rows: assert r['status']==by_id[r['id']]['status'], r['id']
sort_id = lambda r: (r['id'].split('.')[0],int(r['id'].split('.')[1]))
rows.sort(key=sort_id)
fields=['id','statement','status','where_proved','depends_on','manuscript_passages (section; folio; scan)',
        'depends_on_doubtful_reading (scan, alternatives)','notes']
with (BASE/(PREFIX+'_results.csv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader()
    for r in rows:
        writer.writerow({
          'id':r['id'],'statement':r['statement'],'status':r['status'],
          'where_proved':r.get('where_proved',''),
          'depends_on':'; '.join(r.get('depends_on',[])) if isinstance(r.get('depends_on'),list) else r.get('depends_on',''),
          fields[5]:r.get('manuscript_passages',r.get(fields[5],'')),
          fields[6]:r.get('depends_on_doubtful_reading',r.get(fields[6],'')),
          'notes':r.get('notes','')})

reading_rows=[]
for path in sorted(LEDGER.glob('*_readings.json')): reading_rows.extend(json.loads(path.read_text()))
rf=['package','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']
with (BASE/(PREFIX+'_readings.csv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rf);w.writeheader()
    for r in reading_rows:
        w.writerow({rf[0]:r.get('package',''),rf[1]:r.get('scan',''),
          rf[2]:r.get('place',r.get(rf[2],'')),rf[3]:r.get('mathematical_support',r.get('mathematics_supports',r.get(rf[3],''))),
          rf[4]:r.get('strength',r.get(rf[4],''))})

aliases={'D.afterLM2.1':'D.after-LM2-1','D.afterLM2.2':'D.after-LM2-2'}
coverage={}
for path in sorted(LEDGER.glob('*_coverage.json')):
    for r in json.loads(path.read_text()):
        r['task']=aliases.get(r['task'],r['task'])
        assert r['task'] not in coverage, r['task']
        coverage[r['task']]=r
inventory=json.loads((LEDGER/'task_inventory.json').read_text())
assert set(coverage)=={r['task'] for r in inventory}, (set(coverage),inventory)
for r in coverage.values():
    assert set(r['statement_ids'])<=set(row_ids), r
(BASE/(PREFIX+'_coverage.json')).write_text(json.dumps([coverage[r['task']] for r in inventory],ensure_ascii=False,indent=2)+'\n')

bib='\n\n'.join(p.read_text().strip() for p in sorted(LEDGER.glob('*_refs.bib')))+'\n'
keys=re.findall(r'@\w+\s*\{\s*([^,]+),',bib)
assert len(keys)==len(set(keys)), 'Duplicate bibliography keys'
cited=set()
for stpath in (BASE/'sections').glob('*.tex'):
    for block in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]*)\}',stpath.read_text()):
        cited.update(k.strip() for k in block.split(','))
assert cited<=set(keys), 'Missing bibliography entries: '+repr(cited-set(keys))
(BASE/(PREFIX+'_references.bib')).write_text(bib)

counts=Counter(r['status'] for r in rows)
report=['INCOMPLETE','','| Task | Statements | Outcome or state reached | Remaining step |',
        '|---|---|---|---|']
for item in inventory:
    r=coverage[item['task']]
    clean=lambda t:str(t).replace('|','/').replace('\n',' ')
    report.append('| '+' | '.join(map(clean,[r['task'],', '.join(r['statement_ids']),r['outcome'],
       r.get('remaining_step',r.get('remaining_question',''))]))+' |')
report += ['', '# Research return and verification', '',
 f"The paper contains {len(rows)} numbered statements: "+', '.join(f'{n} {s}' for s,n in sorted(counts.items()))+'.', '',
 'The INCOMPLETE status records unfinished requested mathematics. It is not a claim that the full task was completed or that a session interruption occurred. Every currently proved, refuted, cited and unresolved statement remains in the paper and in the one-row-per-statement CSV.', '',
 'This work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The attached earlier returns and reviews were inputs to verify, not authorities.', '',
 '## Main completed comparisons', '',
 '- The integral level-12 calculation identifies K32 as V4 × Q8 and computes every requested genuine, outer and rank-two action, with their comparison maps.',
 '- The discrete and full profinite Alexander modules are free of rank one over the specified group rings. Every affine and compact Fermat homology module through level8 is computed integrally. The minimum extension splits and its translation conjugator is unique.',
 '- The full generalized-Jacobian Tate module maps onto the rank-two torus module with a computed kernel. Every distinct coordinate-cusp difference has exact order n for n≥3, giving exact extension exponent n and the specified isogeny.',
 '- The affine coordinate is the Kummer cocycle of −1/2. The image over Qcyc is 2 Zhat, and r distinct positive rational primes have joint image 2 Zhat^r. The two projective CM factors have exact joint index2, detected by Q(i,3^(1/4)).',
 '- All 9714 ordered epimorphisms into all groups of order≤24 were enumerated; exact Schreier, Smith, deck-character, metabelian-module and lower-central checks agree with the general proofs.',
 '- The requested action cannot descend from the final §51 scheme coordinates, even as an outer action: an actual cyclotomic Galois commutator is killed there but survives the weight8 relative-unipotent action.',
 '- The cubic abelian section set and every minimum-torus fiber are computed. All completed pro3 Kummer pairs are classified for the inherited cubic class-two quotient by explicit residue and convergence conditions, with exactly three classes in every nonempty fiber.',
 '- An actual completed Kummer pair has a nonzero continuous obstruction despite vanishing at every finite coefficient level and every local field. The proof computes the derived inverse limit and its nonclosed denominator explicitly.',
 '- Arithmetic completion over the proconstant cyclotomic base kills the geometric free group. Its continuous arithmetic kernels are free prounipotent groups of explicit ranks, with field traces on abelianizations and compatible free presentations of the entire inverse system.', '',
 '- Every intrinsic cubic abelian class unramified outside3 lifts to the full pro3 arithmetic extension. All classes, including ramified ones, lift to the cuspidally central quotient, whose fibers are computed as restricted Kummer sequences. The remaining central kernel has rank44.',
 '- Twelve finite GT0 shadows violate the exact arithmetic CM-field compatibility. They survive every abelian-kernel refinement of the rank97 congruence kernel. The cusp-correction maps have integral Smith cokernel C2 and become onto after adjoining the multiplier coordinate.', '',
 '## Root calculation and remaining steps', '',
 'Part E constructs the third-derived relation module and the marked-depth-two Lie quotient with explicit morphisms, computes the actual rational Galois depth-two image through weight14, and verifies the weight12 relation independently in two polynomial models. It proves the localizer axioms, exact covering criteria and universal base-change counterexamples, and retains all bounded finite witnesses.', '',
 'The minimum torus section set is computed as the completion of rational units for multiplication by all positive integers, including its sign and restricted prime-valuation coordinates. Rational cubic cusp sections collide under that quotient but separate in the cubic\'s own 3-adic abelianization. The plus-quartic real extension has nonzero class modulo2. The D8 quotient detects the nonzero cup(2,3) lifting obstruction.', '',
 'The full intrinsic cubic metabelian/marked-depth section calculation remains unfinished. E.24 computes the entire abelian starting set. E.31 gives an intrinsic quotient with its actual arithmetic origin term and shows two classes in the same toric fiber have different liftability. E.32 computes every section of the inherited class-two quotient, with the exact comparison from the intrinsic quotient in E.25. E.34 lifts the entire unramified abelian family to the full pro3 group. E.35 evaluates the intrinsic finite Heisenberg quotient, and E.36 computes all cuspidally central fibers. The full intrinsic class-two group maps onto the latter with a rank44 central kernel. The obstruction in that kernel, its integral lattice and its continuous convergence conditions remain to be evaluated on every class. Naming its nonabelian cohomology does not evaluate that remaining set.', '',
 'For the full profinite GT0 and all loop-preserving sources, rational special-derivation dimensions are upper bounds until a full profinite lift is proved. Pro-l lifting has been proved. The full-GT beta/gamma constraint gives the stricter actual full-GT comparison. D.25 constructs twelve nonarithmetical finite shadows and D.26 lifts them compatibly through every abelian-kernel refinement of the congruence kernel. D.26 also constructs an explicit finer nonabelian quotient outside this family. The all-finite-quotient realization criterion of D.22 still requires these further quotients; the homology-tower proof does not assert a full profinite lift.', '',
 '## Source and computation notes', '']
for path in sorted(LEDGER.glob('*_report.md')):
    if path.name=='e_report.md': continue
    report += [f'### {path.stem.replace("_report", "").upper()}', '', path.read_text().strip(), '']
report += ['## Files and reproduction', '',
 'The ZIP includes the LuaLaTeX master source and section sources, PDF, required CSV ledgers, combined bibliography, this report, exact mathematical programs, saved standard output, and machine-readable certificates. Published papers and raw third-party HTML are reading aids and are not redistributed. The small-group input retains source URLs and hashes.', '',
 'See code/README.md for commands, dependencies and the distinction between mathematical computations, ledger assembly and document compilation. code/assemble.py verifies statement/status correspondence, complete task coverage and citation-key coverage. The PDF build rejects undefined citations/references, missing characters and overfull boxes. Visual inspection is recorded separately after rendering.', '']
(BASE/(PREFIX+'_report.md')).write_text('\n'.join(report))
summary={'statements':len(rows),'statuses':dict(counts),'tasks':len(coverage),'readings':len(reading_rows),
         'references':len(keys),'cited_references':len(cited),'all_identity_and_coverage_checks':True}
(LEDGER/'assembly_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
