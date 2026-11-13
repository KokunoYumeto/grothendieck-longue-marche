#!/usr/bin/env python3
"""Assemble ledgers, bibliography, coverage and audit report from saved sources."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib,zipfile,difflib
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
        verified=bool(re.search(r'verified|opened|checked',v,re.I))
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
            if current.exists():
                new=current.read_bytes()
                if old==new:state='retained_identical';reason='Retained.'
                else:
                    state='superseded'
                    if rel=='sections/G.tex' or rel.startswith('sections/G_'):
                        reason='Superseded by current Part G, including factor-12 erratum, all-prime proofs, and explicit degree-six line; see G_report.md.'
                    elif rel=='sections/E.tex' or rel.startswith('sections/E_'):
                        reason='Superseded by current Part E; original draft sign checked against scan, finite-quotient audit expanded; see E_report.md.'
                    elif rel=='sections/D.tex' or rel.startswith('sections/D_'):
                        reason='Superseded by current Part D; nonlinear dual-number theorem D.11 resolves the former named test.'
                    else:reason='Superseded by current '+rel+'; proofs, bounds, metadata or typesetting extended/corrected. Full textual changes preserved in companion patch.'
                    if current.suffix in {'.tex','.md','.py','.g','.bib','.csv','.json','.out'}:
                        try:
                            patch.extend(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),
                                           fromfile=zpath.name+':'+rel,tofile='current:'+rel))
                        except UnicodeDecodeError:pass
            else:
                state='omitted'
                if rel.startswith('notes/') and current.suffix in {'.pdf','.txt'}:
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
for p in (ROOT/'notes').glob('*') if (ROOT/'notes').exists() else []:
    if p.suffix in {'.pdf','.txt'}:
        omitted[str(p.relative_to(ROOT))]='Primary reading material; exact source and theorem uses are retained in the bibliography and section reports, rather than redistributing the complete article.'
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
'',
'### B. What the manuscript defines and what the computations establish',
'',
'The actual section 52.3 object is an adelic representation into a finite-type rational algebraic group, with diagonal rationality on the specified discrete geometric subgroup and a cyclotomic character. It is not defined as a nilpotent tower, and no first/second stage is canonical. The paper constructs the cofiltered category and its universal pro-object, the integral section 50 envelope on virtually abelian stages, and the required typed comparison maps to weighted, genus-zero and elliptic completions.',
'',
'For the auxiliary group functors, the fundamental-localizer argument is given through classifying-space mapping groupoids and relative Theorem A. Finite-cover comparisons, intrinsic-cover criteria, Fermat covers, and filling maps are proved with the required maps and hypotheses. The exhaustive group computation covers all 74 isomorphism types of order at most 24 and all 9,714 based epimorphisms from F2, including the nine vacuous non-two-generated types. Every actual Schreier word and abelian image lattice is recorded, with the free metabelian Alexander-module presentation and lower-central graded maps through class four.',
'',
'The three tripod rows are recomputed through weight fourteen; special outer derivations, raw cycle solutions and symmetry invariants remain distinct. The all-prime special-leading-term lifting theorem is proved. For primes at least five, coprime symmetry lifting and the exact centralizer interpretation give a nonpentagonal pro-prime element. At primes two and three there are actual integral group jets with leading q7 through class twelve, without multiplying q7; simultaneous Hall-coordinate equations preserve all earlier free parameters. This does not prove an infinite lift.',
'',
'Four-puncture tables are exact through six. Filling is exact on the appropriate tower normalizer with point-pushing kernel, but is not surjective onto the entire lower tripod normalizer; a nonpentagonal witness detects the discrepancy. Elliptic tables through twelve separate the geometric epsilon algebra from the normalizer quotient: the latter begins in ordinary degrees six and ten. Treating the epsilon algebra as that quotient is false.',
'',
'### C. Modular multiplicities',
'',
'The characteristic-zero classification includes ineffective gerbes, not just the two familiar effective bad orbifolds. Existence of a finite global-quotient presentation descends from Qbar to Q after a finite atlas and a symmetric-group frame construction; descending one prescribed connected presentation is a different problem. Over Z the proof uses the normal-crossing boundary extension argument, including residue characteristics two and three, and the Weierstrass atlas to compute the trivial etale fundamental group of M1,1. Nontrivial inertia therefore rules out a finite etale scheme atlas. Ordered M0,4 and M0,5 are treated separately from their symmetric quotient stacks.',
'',
'### D. Quasi-unipotence and nonlinear targets',
'',
'The exact divided-power criterion, positive-power result for finitely presented linear groups, primitive-lattice counterexample, and failure of an integer-section presentation of an integral sheaf are proved. The explicit class-one/class-two Dehn-twist models retain their integral denominators at two and three; free-word identities are checked independently through nilpotent class four.',
'',
'Both named nonlinear test bases are resolved: Z/4 by square-zero identity kernels, and characteristic-zero dual numbers by Weil restriction, its vector-group reduction kernel, the actual algebraic image, and exponential in a unipotent extension. No flatness assumption is silently inserted. General integral-model conditions and the remaining general nonlinear-base assertion are separately retained in D.9.',
'',
'### E. Special Teichmuller group, arithmetic action and germs',
'',
'The positive tangent/boundary group is B3. Its centre generator maps to minus the identity in SL2(Z), so the kernel over SL2(Z) is the square of the central generator. Orientation reversal inverts this kernel: the full GL2 extension is not central. The original cote 140-1 draft was opened and its sign checked on scans 35–36, correcting the earlier counterfactual class-five reading to the class-one universal-cover extension.',
'',
'The Tate tangential arithmetic action is derived with its Kummer correction and base-path conventions. Genuine arity-four GT shadows are distinguished from two-hexagon candidates and from arbitrary braid-group automorphisms; the exact bounds of each completed enumeration are in the Part E report. The literal inverse limit of all shrinking-annulus sheaf topoi is degenerate; the corrected covering-germ category retains the classifying topos. Infinite-sheet germ morphisms require their own cofinality condition. The surface Homeo/Diff comparison is proved with its hyperbolic and low-type qualifications.',
'',
'### F. Splittings and finiteness',
'',
'The unrestricted nonabelian section set is H1 of the actual Galois action. Selmer schemes impose additional local conditions. For the tripod, Hain–Matsumoto Proposition 9.6 supplies the constrained free Galois Lie algebra; the paper derives exact full and metabelian dimensions and their inverse towers. The first strict global/local dimension inequalities for zero, one and two denominator primes are at classes one, two and four, respectively. The cited Kim theorem is used with its indexing shift and Zariski-density argument to deduce integral finiteness.',
'',
'The unrestricted abelian power-completion cohomology is computed explicitly, including infinite ramification with coefficients tending to zero. Unit tangential sections at zero and one coincide after abelianization, so universal finite-level cusp separation is false. The degree-seven nonpentagonal element first changes a Lie generator in class eight; it is invisible at all three stated finiteness thresholds. Its cocycle transport changes the action as well and is not silently treated as an automorphism of a fixed-action Selmer set.',
'',
'The rank-zero and rank-one punctured elliptic examples have exact verified ranks, finite Tate–Shafarevich groups, local tables through eight, and exact first two global levels. Higher global dimensions are expressed in explicit dual Selmer defects; the zero-defect tables and corresponding higher thresholds are conditional, not unconditional computations. The full unrestricted integral metabelian and Fermat section sets remain F.12.',
'',
'### G. CM arithmetic',
'',
'The degree-four arithmetic lead is false in two of its three components: the order-four CM automorphism kills the extreme characters; the middle character is nonzero. The standard tangent has degree-two coefficient equal to the Kummer character of 1+i, and packet changes add the packet Kummer class. The published factor-twelve erratum to Nakamura’s 1995 formula is incorporated in the theta-character comparison.',
'',
'A free-Lie kernel argument for metabelian-detected special derivations proves the inertia fixed-subgroup assertion in every pro-prime quotient and every cusp packet, including inert primes and two. A finite-cover weight detector plus the degree-four obstruction gives the pro-prime arithmetic normalizer criterion; the split eigenline lifts through class four and stops in class five. In the full profinite group the criterion is also proved whenever one maximal pro-prime quotient detects the subgroup. The common kernel of all such quotients remains a genuine residual problem.',
'',
'Ambient special modules, CM characters and bracket ranks are computed through fourteen. The opened 2026 arithmetic-generation theorem is applied only after verifying its class-number and decomposition hypotheses, giving exact rational arithmetic dimensions 0,1,3,3,8,11,24 in even degrees two through fourteen. The first repeated-character arithmetic line, in degree six, is explicitly placed using the constant mixed-Tate quotient and the corrected theta comparison. Ordinary elliptic weight and relative Tate weight are distinguished. Higher embedded vectors and integral indices remain separate from those exact dimensions.',
'',
'## Exact residual obligations','',
'These rows prevent a complete return. The paper gives the strongest established partial result and the unsuccessful or incomplete reductions for each. Finite computations are not extrapolated to infinite lifting, and a named cohomology group is not presented as an evaluated set.','',
'| ID | Unresolved statement | Location |','|---|---|---|']
for r in results:
    if r['status']=='Open':
        report.append('| '+cell(r['id'])+' | '+cell(r['statement'])+' | '+cell(r['where_proved'])+' |')
report+=['','## Complete task matrix','','Rows with a qualified finite box or local conditions retain that qualification. A row can have a proved replacement while a stronger literal request is refuted or remains incomplete.','','| Task | State reached | Statements | Remaining scope or qualification |','|---|---|---|---|']
for r in coverage:
    report.append('| '+cell(r.get('task',''))+' | '+cell(r.get('status',''))+' | '+cell(r.get('results',[]))+' | '+cell(r.get('remaining',[]))+' |')
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
'The direct weight-fourteen tripod matrix attempt was killed for memory use. Its log is retained. The final weight-fourteen dimensions use the exact character/Witt computation and agree with matrix calculations through thirteen; the report never describes the failed large matrix as completed. Every finite GT audit states whether it checks candidate equations, a marked quotient action, or genuine arity-four shadows.',
'',
'See code/README.md for commands, input/output pairs, dependency versions and resource scope. Metadata and document assembly scripts do not constitute independent mathematical verification.',
'',
'## Typesetting and visual verification','']
if typ:
    report.append(f"Latest recorded build: overfull boxes exceeding 2pt before fixes: {typ.get('over_2pt_before','unrecorded')}; after fixes: {typ.get('over_2pt_after','unrecorded')}. Undefined citations: {typ.get('undefined_citations','unrecorded')}; undefined references: {typ.get('undefined_references','unrecorded')}; missing glyphs: {typ.get('missing_characters','unrecorded')}.")
else:report.append('The full build is in progress; no publication-ready PDF claim is made at this checkpoint.')
if qa:report.append('Visual QA record: '+json.dumps(qa,ensure_ascii=False)+'.')
else:report.append('Rendered-page visual inspection has not yet been recorded at this checkpoint.')
report+=['','Build commands and the final log are retained in audit/. The report is regenerated after the final layout and citation pass.','',
'## Checkpoints, corrections and omissions','',
'Earlier checkpoint ZIPs are immutable. The final source supersedes their drafts. audit/checkpoint_changes.csv lists every earlier checkpoint file, whether it is unchanged, superseded or omitted, and the reason. The companion audit/checkpoint_diffs/ patches preserve every changed textual passage against each earlier checkpoint. Original source files for duplicate bibliography keys remain in sections/; the assembled bibliography uses one documented entry per key.',
'',
'Specific mathematical corrections include the original-draft extension sign in Part E, the factor-twelve Kummer normalization in G.7/G.21, the new nonlinear D.11 replacing the former dual-number residual, the narrowed full-profinite criterion in G.19, and the finite/infinite distinction in the exceptional-prime lift. Layout-only changes include split displays, array alignment guards, explicit class-index notation, and line wrapping.',
'',
'Files intentionally omitted from distribution are listed below. Complete externally retrieved papers are reading material; source URLs and theorem use remain available in the bibliography. No generated research code or its final printed output is omitted.','',
'| File | Reason |','|---|---|']
for p,reason in sorted(omitted.items()):report.append('| '+cell(p)+' | '+cell(reason)+' |')
(ROOT/(PREFIX+'_report.md')).write_text('\n'.join(report)+'\n')
print(json.dumps(status,indent=2))

