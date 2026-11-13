#!/usr/bin/env python3
"""Assemble ledgers, bibliography, coverage and audit report from saved sources."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib,zipfile,difflib
from package_files import exclusion_reason
ROOT=Path(__file__).resolve().parents[1]
SEC=ROOT/'sections'; AUDIT=ROOT/'audit';AUDIT.mkdir(exist_ok=True)
PREFIX='LM8_LIE_APPROXIMATIONS'
def key(ident):
    m=re.match(r'([A-G])\.(\d+)([a-z]*)',ident)
    return (m[1],int(m[2]),m[3]) if m else (ident,0,'')
def flat(x):
    if isinstance(x,(list,tuple)):return '; '.join(map(str,x))
    if isinstance(x,dict):return json.dumps(x,ensure_ascii=False)
    if x is False:return 'No'
    if x is True:return 'Yes; see source'
    return str(x)
def cell(x):return flat(x).replace('|',r'\|').replace('\n',' ')
results=[]
for p in sorted(SEC.glob('*_results.json')):results.extend(json.loads(p.read_text()))
ids=[r['id'] for r in results]
assert len(ids)==len(set(ids)),[x for x,n in Counter(ids).items() if n>1]
results.sort(key=lambda r:key(r['id']))
texids=[]
for p in SEC.glob('*.tex'):
    texids.extend(re.findall(r'\\begin\{statement\}\{([^}]+)\}',p.read_text()))
assert set(texids)==set(ids), {'unregistered':list(set(texids)-set(ids)),
                              'missing_from_paper':list(set(ids)-set(texids))}
reachable=set()
def visit_tex(p):
    p=p.resolve()
    if p in reachable:return
    reachable.add(p)
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}',p.read_text()):
        q=ROOT/name
        if not q.suffix:q=q.with_suffix('.tex')
        if q.exists():visit_tex(q)
visit_tex(ROOT/(PREFIX+'_paper.tex'))
assert all(p.resolve() in reachable for p in SEC.glob('*.tex')
           if re.search(r'\\begin\{statement\}',p.read_text())), 'A statement source is not included in the paper.'
headers=['id','statement','status','where_proved','depends_on',
         'manuscript_passages (section; folio; scan)',
         'depends_on_doubtful_reading (scan, alternatives)','notes']
with (ROOT/(PREFIX+'_results.csv')).open('w',newline='') as h:
    w=csv.writer(h);w.writerow(headers)
    for r in results:
        w.writerow([flat(r.get(k,'')) for k in
                    ['id','statement','status','where_proved','depends_on',
                     'manuscript_passages','depends_on_doubtful_reading','notes']])
rh=['package','scan',r'the \unsure or \illegible place',
    'what the mathematics supports','how strongly']
readings=[]
for p in sorted(SEC.glob('*_readings.csv')):
    for r in csv.DictReader(p.open()):
        if 'package' in r:
            readings.append([r.get(k,'') for k in rh])
        else:
            readings.append([r.get('cote',''),r.get('scan',''),
                             '; '.join(filter(None,[r.get('equation',''),r.get('reading','')])),
                             r.get('resolution',''),
                             'Doubtful-reading flag: '+r.get('doubtful','')+
                             '; used by '+r.get('used_by','')+
                             '; folio '+r.get('folio','')])
with (ROOT/(PREFIX+'_readings.csv')).open('w',newline='') as h:
    w=csv.writer(h);w.writerow(rh);w.writerows(readings)
def bibentries(text):
    pattern=re.compile(r'@\w+\s*\{([^,]+),')
    pos=0
    while (m:=pattern.search(text,pos)):
        start=m.start();j=text.index('{',start);depth=0
        for i in range(j,len(text)):
            if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'):
                depth-=1
                if depth==0:
                    yield m[1],text[start:i+1]
                    pos=i+1;break
        else:raise ValueError('Unclosed bibliography entry '+m[1])
entries={}; origins={}; duplicates=[]
for p in sorted(SEC.glob('*_refs.bib')):
    for k,v in bibentries(p.read_text()):
        if k in entries:
            duplicates.append({'key':k,'kept':origins[k],'also_present':str(p.relative_to(ROOT))})
            # Retain the more fully documented verified entry.
            if len(v)>len(entries[k]):entries[k]=v;origins[k]=str(p.relative_to(ROOT))
        else:entries[k]=v;origins[k]=str(p.relative_to(ROOT))
for k,v in list(entries.items()):
    if not re.search(r'keywords\s*=',v,re.I):
        verified=bool(re.search(r'\b(?:verified|opened|checked)\b',v,re.I)) and not bool(re.search(r'\bunverified\b|not (?:opened|checked)',v,re.I))
        entries[k]=v[:-1].rstrip().rstrip(',')+',\n  keywords={'+('verified' if verified else 'unverified')+'}\n}'
(ROOT/(PREFIX+'_references.bib')).write_text(
    '% Source verification is recorded in every entry and in the report.\n'+
    '\n\n'.join(entries[k] for k in sorted(entries))+'\n')
(AUDIT/'bibliography_deduplication.json').write_text(json.dumps(duplicates,indent=2)+'\n')
cites=set()
for p in SEC.glob('*.tex'):
    for v in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',p.read_text()):cites.update(v.split(','))
assert not cites-set(entries),sorted(cites-set(entries))
coverage=[]
for p in sorted(SEC.glob('*_coverage.json')):
    for r in json.loads(p.read_text()):
        r['_source']=str(p.relative_to(ROOT));coverage.append(r)
tasks=[r['task'] for r in coverage]
assert len(tasks)==len(set(tasks)), 'Duplicate exact task labels: '+str([t for t,n in Counter(tasks).items() if n>1])
for r in coverage:
    assert not set(r.get('results',[]))-set(ids), 'Unknown statement in task '+r['task']
(AUDIT/'task_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
counts=Counter(r['status'] for r in results)
status={'statements':len(results),'status_counts':dict(counts),'readings':len(readings),
        'bibliography_entries':len(entries),'task_rows':len(coverage)}
(AUDIT/'package_summary.json').write_text(json.dumps(status,indent=2)+'\n')
# Preserve a per-file and per-passage record of every earlier checkpoint change.
changes=[]; diffs=AUDIT/'checkpoint_diffs';diffs.mkdir(exist_ok=True)
for zpath in sorted((ROOT.parent/'checkpoints').glob(PREFIX+'_checkpoint_*.zip')):
    patch=[]
    with zipfile.ZipFile(zpath) as z:
        for name in z.namelist():
            if name.endswith('/'):continue
            rel=name.split('/',1)[-1]; current=ROOT/rel;old=z.read(name)
            if current.exists() and exclusion_reason(ROOT,current) is None:
                new=current.read_bytes()
                if old==new:state='retained_identical';reason='Retained.'
                else:
                    state='superseded'
                    if rel=='sections/G.tex' or rel.startswith('sections/G_'):
                        reason='Superseded by current Part G, including factor-12 erratum, all-prime proofs, and explicit degree-six line; see G_report.md.'
                    elif rel=='sections/E.tex' or rel.startswith('sections/E_'):
                        reason='Superseded by current Part E; original draft sign checked against scan, finite-quotient audit expanded; see E_report.md.'
                    elif rel=='sections/D.tex' or rel.startswith('sections/D_'):
                        reason='Superseded by current Part D; D.11-D.21 resolve the nonlinear positive-power assertion over every quasi-compact quasi-separated base and refute quasi-compactness alone. D.22-D.23 answer the original smooth-model question and separate its two point-factorization readings. See D_nonlinear_report.md and D_surface_report.md.'
                    else:reason='Superseded by current '+rel+'; proofs, bounds, metadata or typesetting extended/corrected. Full textual changes preserved in companion patch.'
                    if current.suffix in {'.tex','.md','.py','.g','.bib','.csv','.json','.out'}:
                        try:
                            patch.extend(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),
                                           fromfile=zpath.name+':'+rel,tofile='current:'+rel))
                        except UnicodeDecodeError:pass
            else:
                state='omitted'
                if current.exists() and exclusion_reason(ROOT,current):
                    reason=exclusion_reason(ROOT,current)
                elif rel.startswith('notes/') and current.suffix in {'.pdf','.txt'}:
                    reason='Externally retrieved primary reading material; not a generated deliverable. Bibliographic source and exact theorem use retained; full article redistribution omitted.'
                elif current.suffix in {'.aux','.toc','.log','.bbl','.blg'}:
                    reason='Superseded build intermediate; final build log and reproducible source retained.'
                else:reason='Not present in current package; must review before delivery.'
            changes.append({'checkpoint':zpath.name,'file':rel,'state':state,'reason':reason})
    (diffs/(zpath.stem+'.patch')).write_text(''.join(patch))
with (AUDIT/'checkpoint_changes.csv').open('w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=['checkpoint','file','state','reason']);w.writeheader();w.writerows(changes)
omitted={}
for r in changes:
    if r['state']=='omitted':omitted[r['file']]=r['reason']
# Reading material retained in workspace is excluded by packaging as well.
for folder in ['notes','source_checks']:
    for p in (ROOT/folder).rglob('*') if (ROOT/folder).exists() else []:
        if p.is_file() and p.suffix in {'.pdf','.txt','.png'}:
            reason=exclusion_reason(ROOT,p)
            if reason:omitted[str(p.relative_to(ROOT))]=reason
typ={}
if (AUDIT/'typesetting.json').exists():typ=json.loads((AUDIT/'typesetting.json').read_text())
qa={}
if (AUDIT/'visual_qa.json').exists():qa=json.loads((AUDIT/'visual_qa.json').read_text())
report=[
'INCOMPLETE','',
'# LM8_LIE_APPROXIMATIONS — research and verification report','',
'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. No priority is claimed. This package does not satisfy the prompt’s all-items completion criterion: the exact residual obligations are retained below and in the paper. An unresolved row describes the present work, not a declaration that the problem is open in the literature. No execution-environment disconnection is claimed.','',
'## Contents and proof register','',
f"The paper contains {len(results)} numbered statements: "+', '.join(f'{counts[k]} {k}' for k in ['Proved','Known','Refuted','Open'] if counts[k])+'.',
f"The results ledger contains exactly one row per statement; the readings ledger contains {len(readings)} entries; the bibliography contains {len(entries)} distinct keyed entries, each explicitly marked verified or unverified. The task matrix contains {len(coverage)} rows.",
'',
'The paper follows Parts A–G. Proved and Refuted entries give proofs or complete counterexamples. Known entries include exact theorem citations and the reduction to the stated problem. Open entries retain the strongest result, the concrete attacks and computations, and the remaining step. Citation verification is source-specific; earlier AI reviews were inputs to recheck, never authority.',
'',
'## Mathematical results and corrections','',
'### A. Surface and profinite realization',
'',
'The hyperbolic discrete realization statement is reduced to the centre-free extension classification and Nielsen realization, with ineffective actions and orientation reversal kept explicit. Germ data alone do not determine a defining commensurability class; that class must be part of the L-structure. The proposed modular uniqueness criterion is refuted by an explicit free-product example. The finite program treats its stated signature boxes, closed genus at most two, and groups of order at most twelve; it is not an enumeration of unbounded puncture counts.',
'',
'The profinite results include centre-freeness, peripheral structure and the full geometric closure for the once-punctured torus. Finite solvable subgroups in the oriented low-genus geometric closures are treated using the opened 2026 theorem. An explicit bare profinite involution is not misrepresented as peripheral: the finite word computation detects its failure to preserve the torus boundary. The unrestricted peripheral realization problem remains A.12/A.18.',
'A.19 gives canonical normalized genuine representatives of pure tripod outer actions and exact norm equations for finite order. Multiplier-one torsion is invisible in every maximal pro-prime quotient. A.20 proves that simultaneous powers preserve the full tripod peripheral structure only for the two diagonal signs: a mixed sign passes all nilpotent tests but fails in D24, the smallest witness by an exhaustive check of 293009 ordered pairs in all250 groups through order48. A.21 gives an exact compact finite lifting system for a possible pure involution and excludes every nonidentity conjugator in the universal S3 quotient of order972. These tests do not classify all peripheral profinite torsion.',
'A.22 constructs a genuine peripheral multiplier-one involution on the full free profinite metabelian quotient. A normalized Haar idempotent in the completed Alexander ring isolates a fifth-adic, nontrivial cubic-character component; the involution acts there by minus1 and elsewhere by1. Its image on the explicit order75 group F25 semidirect C3 is outer. It is invisible in every maximal pro-prime quotient and in the universal S3 test. This is a metabelian construction only: an order-preserving peripheral lift to the full free profinite group, or a finite nonmetabelian obstruction, remains to be found.',
'A.23 lifts this specified involution and its two norm-one conjugators through an infinite nonmetabelian quotient whose index-three kernel is the free class-two pro5 group of rank4. Exact BCH coordinates with denominators powers of3 verify all identities and identify the original metabelian residues. Its central second derived group is Z5, and the compatible finite quotients have orders3*5^(10n). Thus the first nonmetabelian test, of order29296875, supplies a lift; it supplies no full free profinite lift.',
'A.24 computes the entire next two lifting families: affine Z5-spaces of dimensions4 and20 at classes3 and4. The full class4 family projects to exactly one point of the class3 family; the initial zero-parameter class3 choice does not extend. Rational matrices, complete nullspaces, independent modular rank certificates and exact reductions prove the integral assertions. The calculation therefore retains all earlier choices instead of turning failure of one choice into an obstruction to every lift.',
'A.25 computes the complete class5 family in actual integral Hall group coordinates, retaining all20 preceding parameters. The1428-by428 system has rank338 overQ andF5, a full integral90-dimensional solution space, a2-dimensional affine image in class4, and88-dimensional fibres. The zero-parameter class4 point fails, while the full family extends. Actual group commutators certify the saturated second-derived lattice. The independent verifier checks the whole sparse system and every nullspace vector. Counts modulo5^n concern parameter-equation residues, not naive Hall-coordinate group quotients.',
'A.26 lifts the exact A.22 metabelian involution through the entire relative pro5 completion of the index-three kernel. Boundary twists realize its mod5 matrix, and Schur–Zassenhaus constructs the finite action in the pro5 automorphism group while retaining the prescribed C3 deck action. Primitive centralizers and exact norm corrections give derived peripheral conjugators. A relative Magnus embedding forces their precise A.22 residues. The actual fibre product F/(F-double-prime intersect R) therefore carries the whole metabelian action with an all-class nonmetabelian lift. This does not prescribe the earlier A.23 branch and does not construct a full free profinite lift. Increasing this one relative pro5 nilpotency class alone cannot obstruct A.22.',
'',
'### B. What the manuscript defines and what the computations establish',
'',
'The actual section 52.3 object is an adelic representation into a finite-type rational algebraic group, with diagonal rationality on the specified discrete geometric subgroup and a cyclotomic character. It is not defined as a nilpotent tower, and no first/second stage is canonical. The paper constructs the cofiltered category and its universal pro-object, the integral section 50 envelope on virtually abelian stages, and the required typed comparison maps to weighted, genus-zero and elliptic completions.',
'',
'For the auxiliary group functors, the fundamental-localizer argument is given through classifying-space mapping groupoids and relative Theorem A. Finite-cover comparisons, intrinsic-cover criteria, Fermat covers, and filling maps are proved with the required maps and hypotheses. The exhaustive group computation covers all 74 isomorphism types of order at most 24 and all 9,714 based epimorphisms from F2, including the nine vacuous non-two-generated types. Every actual Schreier word and abelian image lattice is recorded, with the free metabelian Alexander-module description and lower-central graded maps through class four.',
'',
'The three tripod rows are recomputed through weight fourteen; special outer derivations, raw cycle solutions and symmetry invariants remain distinct. Every integral invariant special outer leading term lifts to an actual symmetry-centralizing continuous pro-prime automorphism, at every prime. For primes at least five, averaging proves the result. At two and three, the integral involution and symmetric-group decompositions of the free Lie algebra prove uniform vanishing of H1 on the actual special outer lattice; successive cocycle corrections then converge. Thus q7, 2q7 and 3q7 all lift infinitely, with their nonzero pentagon defects. Modular H1 must not be substituted for this integral obstruction group. Independently, the complete 5030-by-2497 class-fourteen system retains all quadratic terms and every earlier free parameter; its exact rank is 2066 and nullity 431. Exact local congruences and a coprime-denominator Bezout combination produce an integral Hall word whose full group equations are independently verified. The finite certificate and the infinite lifting proof are distinct arguments; neither asserts a full profinite assembly.',
'',
'Four-puncture tables are exact through six. Filling is exact on the appropriate tower normalizer with point-pushing kernel, but is not surjective onto the entire lower tripod normalizer; a nonpentagonal witness detects the discrepancy. Elliptic tables through twelve separate the geometric epsilon algebra from the normalizer quotient: the latter begins in ordinary degrees six and ten. Treating the epsilon algebra as that quotient is false.',
'The characteristic-two signed comparison now has a complete first-stage obstruction and replacement. The integral Fermat projection has lattice matrix with Smith entries2,2 and reduces to a finite constant image of order48. A valid infinitesimal minimal conjugator moves rho outside that image, so the unrestricted compatible lift does not exist. B.24a-c compute the liftable locus t²=t, all marked lift fibres, and their ind-affine kernel Ga6 semidirect the additive-polynomial automorphisms fixing1. Exactly128 of256 fine dual-number parameters lift. The retained conjugator images and higher realization remain B.24d, while B.31-B.34 below settle its former source and action-existence obligations. B.29 proves finite-factor automorphism lifting by an exact compactness argument, then exhibits a PSL2(F13) quotient where the cusp order changes from13 to7, identifying why this does not solve the prescribed profinite peripheral word in B.28.',
'B.30 upgrades the rank-seven relative comparison from associated gradeds to full rational filtered automorphisms, and to actual integral relative pro-prime automorphisms for every prime at least5. It uses the actual quotient by deck commutators, strict centralizing representatives, unique peripheral roots, coprime cohomology, and convergent corrections. It assumes no simultaneous formality. Compatible and incompatible relative actions can still have the same absolute projection: the source is freely chosen, whereas a prescribed full profinite word induces a particular source action. That distinction retains the precise residual B.28.',
'B.31-B.34 identify the actual signed Section49 source, prove that it preserves every Fermat kernel, and construct its entire continuous local and profinite relative actions. Original pages530,534,549,550,559,560 were directly inspected. The complete abelian-kernel Fermat tower is C/F-double-prime; the complete relative pro-prime Fermat family detects exactly finite free-group quotients with nilpotent derived subgroup, still a proper quotient. The actual first modular image is Zhat semidirect Zhat-units, proved by an integral cocycle calculation and verified in finite reductions. An actual cyclotomic multiplier sqrt6 in Z5 gives an irrational first-layer trace and refutes a compatible action of the whole profinite source over Q. This does not deny the constructed local actions or rational fine-data lifts.',
'B.35 computes both actual signed normalizer images on C/F-prime. The rho image is C3 semidirect the cyclotomic units, with an explicit multiplicative section. The sigma image is C2 times the affine subgroup of pairs(t,mu) satisfying t mod2=(mu_2²-1)/8 mod2. The midpoint path identifies the surviving coordinate with the Kummer character of2; its image on the cyclotomic kernel is exactly2Zhat. An integral class-two calculation proves that no other multiplier-one translations occur. The sigma extension is nonsplit, already detected by translation modulo4 and units modulo8. The G_D and larger conjugator fibre products have the full inner-by-cyclotomic first-stage image, with explicit kernels. These conclusions use the actual signed source, not arbitrary quotient automorphisms.',
'',
'### C. Modular multiplicities',
'',
'The characteristic-zero classification includes ineffective gerbes, not just the two familiar effective bad orbifolds. Existence of a finite global-quotient presentation descends from Qbar to Q after a finite atlas and a symmetric-group frame construction; descending one prescribed connected presentation is a different problem. Over Z the proof uses the normal-crossing boundary extension argument, including residue characteristics two and three, and the Weierstrass atlas to compute the trivial etale fundamental group of M1,1. Nontrivial inertia therefore rules out a finite etale scheme atlas. Ordered M0,4 and M0,5 are treated separately from their symmetric quotient stacks.',
'',
'### D. Quasi-unipotence and nonlinear targets',
'',
'The exact divided-power criterion, positive-power result for finitely presented linear groups, primitive-lattice counterexample, and failure of an integer-section presentation of an integral sheaf are proved. The explicit class-one/class-two Dehn-twist models retain their integral denominators at two and three; free-word identities are checked independently through nilpotent class four.',
'',
'Both named nonlinear test bases are resolved: Z/4 by square-zero identity kernels, and characteristic-zero dual numbers by Weil restriction, its vector-group reduction kernel, the actual algebraic image, and exponential in a unipotent extension. No flatness assumption on the group scheme is inserted.',
'',
'Original images of section 50, scans 10-12, confirm that the base was only required to be quasi-compact. D.14 refutes that literal claim by gluing additive groups with unbounded Frobenius-degree transition maps over a one-dimensional quasi-compact, non-quasi-separated base; the product with an elliptic curve gives a separated smooth nonaffine example. D.12 proves descent after a common integer dilation on quasi-compact overlaps. D.17-D.21 then prove the positive-power theorem for every quasi-compact quasi-separated base and every separated group scheme of finite presentation, allowing nonaffine, nonsmooth and nonflat targets. Integer interpolation controls rational denominators; saturated primary filtrations handle nilpotents; finite integer-torsion ideals are killed by further dilation; constructible witness images descend arbitrary characteristic-zero bases to Noetherian models. These arguments close all former local-base residuals.',
'The original scan213 smooth-model question concerns conditions (45)-(49), preceding the additional hypotheses (55)-(64). D.22 derives the affirmative answer from a compact-adelic invariant lattice, schematic closure of the multiplier graph, and the exact Bosch-Lutkebohmert-Raynaud smoothening theorem, checking preservation of every Zp-valued point. The recap on scan213 visibly writes M(Z), whereas (45) and (47) use M(Ẑ). D.23 refutes the literal stronger integral-point reading by the open cyclotomic multiplier and gives two distinct smooth models showing that the preceding data alone do not force uniqueness. Both readings remain recorded; the handwriting is not silently regularized.',
'',
'### E. Special Teichmuller group, arithmetic action and germs',
'',
'The positive tangent/boundary group is B3. Its centre generator maps to minus the identity in SL2(Z), so the kernel over SL2(Z) is the square of the central generator. Orientation reversal inverts this kernel: the full GL2 extension is not central. The original cote 140-1 draft was opened and its sign checked on scans 35–36, correcting the earlier counterfactual class-five reading to the class-one universal-cover extension.',
'',
'The Tate tangential arithmetic action is derived with its Kummer correction and base-path conventions. The complete marked normal-kernel enumeration through braid quotient order 1000 has 1946 kernels (1000 cyclic, 946 noncyclic). The exact hexagon and surjectivity audit has 89721 noncyclic pairs, with every groupoid source kernel identified; 72251 are automorphisms of the target quotient itself. A proved forgetful refinement turns every retained pair into a full arity-four shadow on an explicitly declared target, giving 393913 projected pairs with the cyclic cases included. This convention does not assert that every refined target induces exactly the original kernel.',
'',
'For class-two pure free-group images, the global coefficient formula r=(chi^2-1)/24 gives the exact genuine GT, GT0 and Galois images, determining all 1000 cyclic and 354 noncyclic cases. An independent 54-point permutation certificate gives an order 486 quotient with m=0 and f=[X,Y] which passes every finite condition but violates the global coefficient congruence. Its full arity-four refinement is a charming fake GT-shadow, with pure arity-four quotient order 3^13 and induced braid quotient order 13122. Three published targets are independently checked with the actual pentagon; finite shadows, global genuine images and target-quotient automorphisms remain distinct.',
'',
'The literal inverse limit of all shrinking-annulus sheaf topoi is degenerate; the corrected covering-germ category retains the classifying topos. Infinite-sheet germ morphisms require their own cofinality condition. The surface Homeo/Diff comparison is proved with its hyperbolic and low-type qualifications.',
'',
'### F. Splittings and finiteness',
'',
'The unrestricted nonabelian section set is H1 of the actual Galois action. Selmer schemes impose additional local conditions. For the tripod, Hain–Matsumoto Proposition 9.6 supplies the constrained free Galois Lie algebra; the paper derives exact full and metabelian dimensions and their inverse towers. The first strict global/local dimension inequalities for zero, one and two denominator primes are at classes one, two and four, respectively. The cited Kim theorem is used with its indexing shift and Zariski-density argument to deduce integral finiteness.',
'',
'The unrestricted abelian power-completion cohomology is computed explicitly, including infinite ramification with coefficients tending to zero. Unit tangential sections at zero and one coincide after abelianization, so universal finite-level cusp separation is false. The degree-seven nonpentagonal element first changes a Lie generator in class eight; it is invisible at all three stated finiteness thresholds. Its cocycle transport changes the action as well and is not silently treated as an automorphism of a fixed-action Selmer set.',
'',
'The rank-zero and rank-one punctured elliptic examples have exact verified ranks, finite Tate–Shafarevich groups, and unconditional full and metabelian global/local tables through eight. F.16-F.18 evaluate every dual Selmer defect in that range. Exact polynomial Manin symbols for the first six CM powers, Hecke eigenspaces, quadratic twisting, ordinary measure distribution and twelve specializations modulo25 give nonzero values. Kato’s divisibility away from5 is applied at each specialization prime; finite specialized coinvariants and the bounded restriction kernel then force the rational dual Selmer groups to vanish. This uses no residual large-image hypothesis, no unproved main-conjecture equality, and no inference that a nonzero specialization makes the entire branch a unit. The first strict level for the rank-zero curve is 1 for s=0,1,2; for the rank-one curve the levels are 2,3,4. F.15 proves that H1 commutes with the compact pro-prime and finite-dimensional rational BCH towers; the earlier representative/stabilizer obstruction is removed in those cases. A fully explicit noncompact pro-discrete tower has H1 zero at every stage and Z2/Z in the limit. The genuinely unevaluated twisted integral metabelian and Fermat section sets remain F.12.',
'F.19 computes the complete real pro2 metabelian section set as three classes and all its induced Fermat2-power kernels as four classes, with the transition maps. The proof uses a clopen decomposition of the completed Alexander module, not just finite quotients. F.20 computes every global pro5 class2 section set with a fixed finite ramification set S containing5. The integral obstruction is an explicit family of tame-symbol congruences modulo5^v5(q-1), and each nonempty integral fibre is unique. For S={2,3,5} the set is Z5^6; adding11 gives one alternating congruence with90625 admissible pairs modulo5. The finite fibres, disappearing extra torsion and induced Fermat descent are also evaluated.',
'F.21 computes the unrestricted global integral class-two section set. The second continuous cohomology is the actual cokernel of the diagonal map multiplying the q-coordinate by5^v5(q-1) on the module of fifth-adic sequences tending to zero; replacing its image by its closure loses information. The integral cup obstruction is proved at the cochain level. It vanishes precisely when its divided tame-symbol coordinates are integral and tend to zero. A Chebotarev construction gives an explicit cup class which vanishes at every finite coefficient level but is nonzero integrally. Every finite quotient therefore admits a lift, while no compatible integral lift exists. The proof and the finite prime certificates were independently reviewed. Higher global stages and the full twisted integral metabelian fibres remain within F.12.',
'F.22 computes the fixed-ramification integral pro5 section sets over Z[1/30] through class4, with the actual arithmetic action. Class2 is Z5^6; every class3 fibre is a Z5^2 torsor, and every class4 fibre has125 elements. The latter classes merge after rationalization. Direct cyclotomic S-unit, class-number and Brauer calculations determine the integral cohomology groups; all twisted fixed groups vanish. Finite coefficient counts are5^(6r),5^(6r),5^(8r),5^(8r+3), and all induced Fermat kernels are evaluated. These are complete integral low-class results, not an assertion about the unevaluated full metabelian tower.',
'F.23 derives the actual class5 obstruction from the PB4 pentagon, retaining the Soulé coefficient and transporting it under an integral local change of coordinates. At both2 and3 it gives six explicit congruences over F5. The permissible valuation directions are a=0, b=0, or a=b; the pair(kappa(2),2kappa(2)) has no class5 lift regardless of earlier choices. Full and metabelian loci agree, with nonempty fibres Z5^6 and Z5^4. The two local class4 frames share one global shift; their actual difference is retained, not set to zero. Every induced relative Fermat class5 locus is completely evaluated. The entire abelian-zero fibre is Z5^8 plus C5^3, or Z5^6 plus C5^3 in the metabelian quotient, by an explicit integral diagonalization of gamma3.',
'F.24 proves that the three specified unit cusp sections first become pairwise distinct at integral class3. The exact global path coefficient is the raw Soulé character kappa3 divided by48. A cyclotomic Kummer product reduces to a fifth power times the cube of the fundamental unit of Q(sqrt5), proving primitiveness even on the cyclotomic kernel. A corresponding explicit Kummer product makes kappa5 a primitive generator as well. These sections have zero abelian coordinates and descend to every induced relative Fermat level. The arbitrary global class3 frame-difference matrix and higher unrestricted integral stages remain within F.12.',
'',
'### G. CM arithmetic',
'',
'The degree-four arithmetic lead is false in two of its three components: the order-four CM automorphism kills the extreme characters; the middle character is nonzero. The standard tangent has degree-two coefficient equal to the Kummer character of 1+i, and packet changes add the packet Kummer class. The published factor-twelve erratum to Nakamura’s 1995 formula is incorporated in the theta-character comparison.',
'',
'A free-Lie kernel argument for metabelian-detected special derivations proves the inertia fixed-subgroup assertion in every pro-prime quotient and every cusp packet, including inert primes and two. A finite-cover weight detector plus the degree-four obstruction gives the pro-prime arithmetic normalizer criterion; the split eigenline lifts through class four and stops in class five. In the full profinite group the criterion is also proved whenever one maximal pro-prime quotient detects the subgroup. The common kernel of all such quotients remains a genuine residual problem.',
'',
'Ambient special modules, CM characters and bracket ranks are computed through fourteen. The opened 2026 arithmetic-generation theorem is applied only after verifying its class-number and decomposition hypotheses, giving exact rational arithmetic dimensions 0,1,3,3,8,11,24 in even degrees two through fourteen. The first repeated-character arithmetic line, in degree six, is explicitly placed using the constant mixed-Tate quotient and the corrected theta comparison. Ordinary elliptic weight and relative Tate weight are distinguished. At degree eight, the exact Sigma3 lift and its Tate commutator were computed: imposing the proposed Tate condition on the CM character line excludes every value of its scalar, so that condition cannot determine the CM embedding. The remaining degree-eight scalar and higher integral indices stay in G.16.',
'The October2026 CM Coleman-Ihara formula was also evaluated at character(4,4): its local scalar is minus6048 in the source normalization. It remains a metabelian character formula and annihilates the missing B8 direction, so it gives no equation for the degree-eight scalar. Its use for integral image indices additionally requires the Coates-Wiles image lattice and comparison with the actual Johnson subgroup.',
'G.22 sharpens the full-profinite finite-cover attack. A residual proper-homology detector must lie in the Prym kernel of a cover of genus at least two. Transport to a once-punctured elliptic curve requires an entire fibre in the existing boundary, forcing the target-map degree to be at most the cover degree. The explicit degree-four cover E minus E[2], with Jacobian quotient multiplication by3, violates this condition. A conditional contradiction is proved only for a pointed target with the required normalizer-recognition theorem, including the original CM curve after finite extension; no transfer to arbitrary CM factors or isogenous curves is assumed.',
'G.23 proves that every degree8 candidate A8+lambda B8 exponentiates in the universal elliptic kernel to all orders and survives exact finite CM-lift transport; the universal equations cannot select its arithmetic parameter. G.24 computes the saturated ambient integral plane with basis C8=A8+(31/20)B8 and B8. Two specified length-nine Magnus coefficients give its integral coordinates alpha and nu in a characteristic finite quotient, without logarithms or division by5. Actual group-word examples modulo125 verify coordinate pairs(1,0) and(1,1). The arithmetic relation lambda=31/20+nu/alpha isolates the still unevaluated nonmetabelian coefficient; neither arithmetic realization of the examples nor arithmetic saturation is asserted.',
'',
'## Exact residual obligations','',
'These rows prevent a complete return. The paper gives the strongest established partial result and the unsuccessful or incomplete reductions for each. Finite computations are not extrapolated to infinite lifting, and a named cohomology group is not presented as an evaluated set.','',
'| ID | Unresolved statement | Location |','|---|---|---|']
for r in results:
    if r['status']=='Open':
        report.append('| '+cell(r['id'])+' | '+cell(r['statement'])+' | '+cell(r['where_proved'])+' |')
report+=['','## Complete task matrix','','Rows with a qualified finite box or local conditions retain that qualification. A row can have a proved replacement while a stronger literal request is refuted or remains incomplete.','','| Task | State reached | Statements | Remaining scope or qualification |','|---|---|---|---|']
for r in coverage:
    report.append('| '+cell(r.get('task',''))+' | '+cell(r.get('status',''))+' | '+cell(r.get('results',[]))+' | '+cell(r.get('remaining',r.get('evidence',[])))+' |')
report+=['','## What was read and how it was used','',
'The attached checked transcriptions, table of contents, relevant manuscript images, LM1/LM2/LM3/LM3b and CYCLOTOMIC returns and reviews, BISITE excerpts, and supplied primary papers were examined where used. Mathematical reductions were rewritten and computations rerun. The source-specific notes in the bibliography state the actual theorem or formula checked. Section reports and readings CSVs retain the manuscript folio/scan anchors and the distinction between a diplomatic reading and mathematical evidence.',
'',
'Primary sources opened include Harbater–Schneps on the centralizer, Brown on mixed Tate motives, Hain–Matsumoto on weighted completion and universal mixed elliptic motives, Enriquez on elliptic associators, Behrend–Noohi on stack uniformization, SGA1 for boundary extension, the specified Hoshi–Minamide–Mochizuki and Hoshi–Mochizuki theorems, Nakamura’s 1994, 1995 and 2013 texts, the elliptic polylogarithm comparison, Kim and Kim–Tamagawa, and the cited 2026 CM and realization preprints. Exact publication metadata and verification status are in the bibliography.',
'',
'The unrefereed 2026 Deligne–Drinfeld upper-bound manuscript is not used to assume the all-weight equality of the arithmetic Lie algebra with grt. No claim of novelty is made; source searches were organized by the supplied titles and exact theorem obligations, and the resulting source audit is recorded rather than converted into a priority claim.',
'',
'## Computations and reproducibility','',
'All mathematics programs and printed outputs are in code/. Exact integer, rational, finite-field, group-word and permutation arithmetic is used; numerical tolerance is not used to decide a rank or identity. The small-group catalogue is external verified input, while every based generating pair and cover calculation is performed explicitly. The analytic-rank certification for the two elliptic curves is a cited rigorous primary database input, separate from the exact descent and point arithmetic reproduced here.',
'',
'The direct weight-fourteen tripod matrix attempt was killed for memory use. Its log is retained. The final weight-fourteen dimensions use the exact character/Witt computation and agree with matrix calculations through thirteen; the report never describes the failed large matrix as completed. Every finite GT audit states whether it checks candidate equations, a marked quotient action, a full finite arity-four shadow, or a reduction of a global element.',
'',
'See code/README.md for commands, input/output pairs, dependency versions and resource scope. Metadata and document assembly scripts do not constitute independent mathematical verification.',
'',
'## Typesetting and visual verification','']
if typ:
    report.append(f"Latest recorded build: overfull boxes exceeding 2pt before fixes: {typ.get('over_2pt_before','unrecorded')}; after fixes: {typ.get('over_2pt_after','unrecorded')}. Undefined citations: {typ.get('undefined_citations','unrecorded')}; undefined references: {typ.get('undefined_references','unrecorded')}; missing glyphs: {typ.get('missing_characters','unrecorded')}.")
    history_path=AUDIT/'typesetting_integration_before_fixes.json'
    if history_path.exists():
        history=json.loads(history_path.read_text())
        widths=[r['points'] for r in history.get('overflow_after',[]) if r['points']>2]
        report.append('The integration build had '+str(len(widths))+' additional boxes exceeding 2pt, of widths '+', '.join(str(x)+'pt' for x in widths)+'. Their full source contexts are retained in audit/typesetting_integration_before_fixes.json. The final rendered review includes the current locations of every previously overflowing source passage, including passages superseded by stronger proofs.')
    milestone_path=AUDIT/'typesetting_milestone12_before_fixes.json'
    if milestone_path.exists():
        milestone=json.loads(milestone_path.read_text())
        widths=[r['points'] for r in milestone.get('overflow',[]) if r['points']>2]
        report.append('The later signed-model integration had '+str(len(widths))+' additional box exceeding 2pt, of width '+', '.join(str(x)+'pt' for x in widths)+'. The complete context is retained in audit/typesetting_milestone12_before_fixes.json; the affected sentence was shortened and its current page is included in the visual review. Alignment and subscript errors in intermediate halted builds were corrected in the source before the final build.')
else:report.append('The full build is in progress; no publication-ready PDF claim is made at this checkpoint.')
if qa:report.append('Visual QA record: '+json.dumps(qa,ensure_ascii=False)+'.')
else:report.append('Rendered-page visual inspection has not yet been recorded at this checkpoint.')
report+=['','Build commands and the final log are retained in audit/. The report is regenerated after the final layout and citation pass.','',
'## Checkpoints, corrections and omissions','',
'Earlier checkpoint ZIPs are immutable. The final source supersedes their drafts. audit/checkpoint_changes.csv lists every earlier checkpoint file, whether it is unchanged, superseded or omitted, and the reason. The companion audit/checkpoint_diffs/ patches preserve every changed textual passage against each earlier checkpoint. Original source files for duplicate bibliography keys remain in sections/; the assembled bibliography uses one documented entry per key.',
'',
'Specific mathematical corrections include the original-draft extension sign in Part E, the factor-twelve Kummer normalization in G.7/G.21, the nonlinear positive-power theorems replacing earlier residual base cases, the distinction between finite shadows and genuine global images in E.14-E.17, the removal of the compact/BCH inverse-limit obstruction by F.15, the narrowed full-profinite criterion in G.19, and the resolution of the exceptional-prime infinite lift by integral cohomology in B.14d. Layout-only changes include split displays, array alignment guards, explicit class-index notation, and line wrapping.',
'',
'Files intentionally omitted from distribution are listed below. Complete externally retrieved papers are reading material; source URLs and theorem use remain available in the bibliography. No generated research code or its final printed output is omitted.','',
'| File | Reason |','|---|---|']
for p,reason in sorted(omitted.items()):report.append('| '+cell(p)+' | '+cell(reason)+' |')
# Put the requested task-by-task matrix before the explanatory report.
mi=report.index('## Complete task matrix')
mj=report.index('## What was read and how it was used')
matrix=report[mi:mj]
del report[mi:mj]
insert_at=report.index('## Contents and proof register')
report[insert_at:insert_at]=matrix
(ROOT/(PREFIX+'_report.md')).write_text('\n'.join(report)+'\n')
print(json.dumps(status,indent=2))

