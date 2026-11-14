#!/usr/bin/env python3
"""Create the exact statement register and the task coverage table.

This is a packaging script, not a mathematical verification program.
Statuses are read from the manuscript. Task outcomes are explicit below.
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parent.parent
TASKS = [
 ('Lead 1','B.2; B.9','(a) Proved','The exclusion is false; an unramified full-section counterexample lies outside the three inherited cusp lines. The drafter\'s particular inherited toric argument is corrected.'),
 ('Lead 2','A.5; A.17; B.7','(b) Refuted','A mixed-inertia class-two lift at 2 is explicit. Full and metabelian sections obey the proved cusp-line restriction.'),
 ('Lead 3','A.6; A.18','(b) Refuted','An infinitely ramified noncuspidal class-two family is constructed with a complete convergence proof; its higher images are excluded.'),
 ('Lead 4','B.4; B.5','(a) Proved','The full geometric pro-3 cyclotomic centralizer is cusp inertia for cuspidal sections and trivial for every other section.'),
 ('Lead 5','A.1; A.2; A.13','(a) Proved','The first derived limit for the intrinsic rank-44 coefficient is explicitly nonzero.'),
 ('A.1','A.1; A.2; A.7; A.13','(a) Proved','The finite-S complex, its integral Smith factors, localization, and the complete Milnor sequence are computed.'),
 ('A.2','A.8; A.9; A.10','(a) Proved','All residue formulas retain the nine tangential origin cochains, the extra unramified generator, and the E36 central-coordinate sign.'),
 ('A.3','A.7; A.8','(a) Proved','Integral local corrections must form a restricted family; every nonempty fiber is the computed rank-23 module with its finite torsion.'),
 ('A.4','A.3; A.4','(a) Proved','An actual pair has a nonzero intrinsic obstruction with every local and finite-coefficient image zero.'),
 ('A.5','A.11; A.12','(b) Refuted as a total evaluator','Total decision is impossible both for finite-coefficient queries and for the explicit finite-program input family with a known convergence modulus. The exact finite/certified-tail evaluator and all four requested regressions are executed; its input interface is stated explicitly.'),
 ('A.6','A.14; A.15; A.16; A.17; A.18; A.19; A.20; A.21; A.22; A.23; A.24; A.25; A.26; A.27; A.28; A.29; A.30; A.31; A.32; A.33; A.34; A.35; A.36; A.37; A.38; A.39; A.40; A.41; A.42; A.43; A.44; B.12; B.13; B.14; B.15; B.16; B.17; B.18; B.19; B.20','(a) Proved by finite arithmetic tests','Every metabelian and marked image and fibre is determined by explicitly constructed finite arithmetic cocycle sets and their compatible kernel orbits, including infinite ramification support. Cofinal finite-rank towers, every coefficient layer and its derived limit, and both exact inherited comparison kernels are proved. An explicit integral target at 17 has the literal local cusp restriction and a class-three lift but no class-four or higher lift. The exact criterion has terminating finite stages and an infinite compatibility limit.'),
 ('B.1','B.1; B.2; B.3; B.9','(a) Proved','All three packets in the abelian, cuspidally central, and inherited class-two coordinates are given with their origins.'),
 ('B.2','A.5; A.6; A.17; A.18','(b) Refuted both leads','Both requested class-two assertions have complete counterexamples and proved higher-quotient restrictions.'),
 ('B.3','B.4; B.5','(a) Proved','The centralizer criterion and precisely the cuspidal members of the full unramified family are determined.'),
 ('B.4','B.6; B.7; B.8; B.10; B.11; B.15; B.16; B.17; B.18; B.19; B.20; A.16; A.22; A.24; A.25; A.26; A.27; A.28; A.29; A.30; A.31; A.33; A.34; A.35; A.36; A.37; A.38; A.39; A.40; A.43','(a) Proved by finite arithmetic tests','The exact image for every one-prime target is given by a terminating finite field and cocycle construction at each precision, with all earlier ramification constraints. The inverse limit of the specified kernel orbits gives every fibre and is equivalent to lifting through all nilpotent quotients. At 17 an explicit integral cocycle has the literal local cusp restriction and a class-three lift but no class-four lift; its nine-term obstruction certificate is independently verified.'),
 ('C.1','C.11; C.12; C.13; C.14; C.15; F.1; F.2; F.3','(a) Proved with the retained arithmetic term','The residue convergence criterion is combined with finite Galois cocycle matrices and explicit compact-support cup traces over every number field. These compute the arithmetic obstruction and the complete fiber inverse limit; the initial quadratic obstruction is also evaluated.'),
 ('C.2','C.1; C.2; C.3','(a) Proved','Restriction is injective and finite Galois descent identifies precisely the invariant classes.'),
 ('C.3','C.3; C.6; C.8; C.9; C.10; C.16; C.17; C.18','(a) Proved','Finite algebraic cover equations evaluate every point section in all 45 central coordinates. Their exact finite conjugacy criterion determines the point image, with the E36 origin and rank-44 fiber translation. The nine cusp packets, Galois action, and rational fixed subset are explicit.'),
 ('C.4','C.4; C.5; C.7','(b) Refuted','Neither the R2 phantom nor the constructed intrinsic phantom dies after any finite extension.'),
 ('D.1', 'D.1; D.4; D.6; D.20; D.21; D.22; D.23; D.24; D.25; D.26; D.27; D.28; D.29; D.30; D.31; D.32; D.33; D.34; D.35; D.36; D.37; D.38; D.39; D.40; D.41; D.42; D.43; D.45; D.47; D.49; D.50; D.51', '(a) Proved', 'The complete rational leading image has dimension three for every prime ell at least five. D.50 lifts each complete pronilpotent peripheral automorphism, retaining all three actual conjugators, through every finite source. D.51 gives three literal integral Lie witnesses, their actual pro-ell realizations, the full characteristic projection square, and the matching upper bound. Every earlier chief comparison and finite obstruction is retained with its specified source.'),
 ('D.2', 'D.2; D.4; D.6; D.7; D.8; D.20; D.22; D.23; D.24; D.25; D.26; D.27; D.28; D.29; D.30; D.31; D.32; D.33; D.34; D.35; D.36; D.38; D.44; D.46; D.48; D.50; D.52', '(a) Proved', 'The complete rational invariant metabelian leading image has dimension two for every prime ell at least five. D.52 constructs an actual full multiplier-one gentle pair with weight-nine pair coefficient X^2Y^2(X+Y)^3 and normalized derivation coefficient its negative. D.50 retains the entire normalized pro-ell pair and every actual modular-source conjugator. The Galois gamma line and this extra direction are independent. The same complete pentagon map excludes the constructed pair. All 42 printed integral witness coefficients pass exact replay.'),
 ('D.3','D.3; D.4; D.7; D.8; D.20','(a) Proved','Compatible finite braid quotients give gentle/pentagon dimensions 37/2 and leading metabelian dimensions 2/1. The integer certificate and actual Galois lower bound derive R9 in weight nine.'),
 ('E.1','E.1; E.4','(a) Proved','Independent exact programs confirm every count, cusp equation, generation certificate, and both Smith forms.'),
 ('E.2', 'E.2; E.5; E.7; E.8; E.9; E.10; E.11; E.12; E.13; E.14; E.15; E.16; E.20; E.22; E.23; E.24; E.25; E.26; E.27; E.28; E.29; E.31; E.33; E.36; E.37; E.38; E.41; E.42; E.43; E.44; E.45; E.46; E.47; E.49; E.50; E.51; E.48; E.52; E.53; E.55; E.56; E.54; E.57; E.58; E.65', '(a) Proved', 'E.58 constructs an actual full multiplier-one gentle pair in the extra CM coset, with positive bits (1,0). Its relative pronilpotent lifting theorem retains all three prescribed conjugators through every finite source. For H=F-prime F-cube, the exact two-primary centralizer lift gives the unique pure frames A=[5I], beta=V=1 modulo twelve, with f in R_nil(H). The whole proof and every finite source/sign calculation pass independent audit. E.9 excludes all twelve earlier particular representatives, so their asserted equivalence with full CM existence is false. The constructed automorphism has an actual new G6 shadow in the whole CM matrix fibre. All earlier finite refinements and whole-fibre results remain in the paper.'),
 ('E.3', 'E.3; D.5; E.6; E.17; E.18; E.19; E.21; E.22; E.23; E.24; E.25; E.26; E.27; E.28; E.29; E.30; E.31; E.32; E.33; E.34; E.35; E.36; E.37; E.38; E.39; E.40; E.41; E.42; E.43; E.44; E.45; E.46; E.47; E.49; E.50; E.51; E.48; E.52; E.53; E.55; E.56; E.54; E.57; E.59; E.61; E.62; E.60; E.64; E.65; E.66; E.67; E.68; E.69; E.63; E.70; E.71; E.72; E.73', 'OPEN: full GT image', "All 864 degree-six points pass the retained pentagons, braid and twist relations. The actual $\\mathrm{SL}_2(\\mathbf F_5)$ source maps onto the five-point Hurwitz source; the same word retains both through E.47's complete integral class-three families at multiplier one. Their full common four-strand target is $(T_{23}\\times_{S_L}T_L)\\times A_{96}$. The $A_6$ kernel/outer tests also retain all 864 points in their stated common sources. Compatibility through every finite quotient remains. The full five-strand $\\mathrm{Sp}_4(\\mathbf F_3)$ test also retains all 864 points. Its complete source factors through $G_6$, its first $B_4$ target is the actual E.18 group, and three explicit simultaneous conjugators prove full $B_5$ generation for every retained word. The prime-five five-strand test retains all 432 multiplier-one points and every prescribed full boundary fibre. Its actual source of order $9000000$ has common quotient $J=A_{10}\\times_{A_2}Q_{20}$ of order $72000$ with $G_L$, retaining all three signed modular bits. The exact residual correction in the old kernels reaches $(\\mathbf Z/5)^3$, and one word gives generating maps on the full common sources and joint braid targets. The prime-seven source also retains this entire family and the prime-five source. Its exact residual correction is $\\mathrm{SL}_2(\\mathbf F_7)\\times(\\mathbf Z/7)^3$, its maximum common quotient with the full old boundary source is $A_{14}$, and the complete joint four- and five-strand targets are generated by the same corrected word. E.48 now retains all 864 old points through the full $A_6$ Ferrari source, including its complete ternary and binary solvable layers, exact positive Kummer label, all centralizer choices and actual joint-source generation. E.52 identifies the full integral symplectic source at every modulus prime to 6 and its common inverse-limit lower-central residual; its simultaneous peripheral comparison with the remaining sources is the next step. E.53 determines the exact uniform common source $G_L\\times_{\\mathcal J_5}G_R$, including the central sign and abelian kernel. Its full residual correction retains the old small-prime and level-five/seven values through the specified congruence subgroups. E.55 now retains the complete 432-point multiplier-one family and every prescribed full boundary fibre through all these congruence levels with one profinite word and the same actual Galois value. Its maximum common source quotients and both full word fibres are explicit. E.56 proves the exact integral four- and five-strand targets and their entire products with the preceding targets, including every congruence kernel. E.54 proves the complete joint A6 and signed source, its exact common quotient of order 1166400000, perfect common residual and full retained boundary fibres. All 864 finite points and all 432 multiplier-one full boundary families survive. The joint four-strand target has the same specified solvable quotient of order 96. Its eight complete chain and twenty quotient audits pass. E.57 retains every whole E.55 word, for all 432 multiplier-one points and every full admitted boundary parameter, through the full A6 source and the entire congruence system. The actual common quotient remains the signed level-five quotient, and the exact residual correction, common source fibres and full target products are proved. All four new certificate steps, including 219684 complete target relations, pass isolated replay. E.59 exhausts the complete 512-element correction image above each of the 24 specified E.17 G6 points in the universal SL2(F3) Ferrari source. Each has four generating gentle values and two generating pentagon values. The actual correction group is Q8^3 through three specified evaluation maps. All 24 positive CM matrix pairs, including 12 extra pairs, survive; the nontrivial cusp gauges and whole common G6 source are retained. Every mathematical output and all 144 final generation certificates pass isolated root replay. E.61 proves the signed matrix formula q12(f)=[[1,-8rho],[-8rho,1+64rho^2]] for every normalized full gentle pair of multiplier one. The actual affine four-strand sewing word has translation (-B-8rho A,A-1); its modulus twelve value is the identity throughout this entire gentle domain. All four central braid carries and the exact frame rho are retained. E.62 retains all 18 literal GL2(F3) epikernels and their actual common source and target with E.59. The full K6 correction groups have orders 2^21 and 2^24; their central derived groups have orders 2^3 and 2^6. Every specified G6 fibre has 16 GL gentle values and 32 common gentle values, with four final pentagon/braid values in each test. The four common final values map two-to-one onto only two of the four GL-only final values and onto both E.59 final values. All 24 CM pairs survive. All source and target generation claims, the complete G6 fibre product and the actual N-prime words are proved; root replay passes all 1011 complete certificates, including 960 generation certificates. E.60 retains every old finite CM point and the entire E.57 boundary and congruence family through the literal 3.A6 Ferrari source. Its whole relative kernel has dimension 79 over F3; the preimage of the old perfect residual has abelianization F3^3 and derived kernel dimension 76. Exact stable commutators fill all three characters, and compactness retains every lower-central correction. The actual four-strand target has specified maximal solvable quotient S_L times ASL2(F3), of order 20736, with perfect kernel; all six target chains pass root replay. E.64 proves full hyperelliptic presentation descent, the selected completed genus-two sewing map, both exact CM subgroup inclusions and two integral norm characters. Its separate orbifold discrepancy characters remain unevaluated on full GT. E.65 constructs the actual continuous quadratic character Delta on the full gentle group, invariant under every multiplier and vanishing on Galois. E.58 has Delta equal to one. The explicit map F to F sigma-inverse to its cube proves that E.3 is precisely the image of Delta restricted to full GT. This restriction remains unassigned. E.66 proves the actual index-two common source of all five distribution maps and the E.62 correction group, with both explicit binary characters. All 96 final E.62 values have exactly three compatible coefficient tuples; all 288 same-word witnesses are independently replayed. Its cyclic-three source comparisons retain the complete based and induced maps and prove their direct products with the E.62 two-group through their odd abelianizations. E.67 proves the positive original Mordell orbifold sign, the exact four Gaussian frame values, and the entire twelve-evaluation N-prime correction image F3^9. Both the E.1 and E.17 origin lists are evaluated separately, each with four complete finite norm values and actual correction words. The specified order-1944 two-factor source map is generating. The full-GT discrepancy character remains unevaluated. E.68 computes the actual common N-prime image of E.66 and E.67 as their full direct product, of order 7011906707722862592. All 1152 combinations over the separately evaluated E.17 origins have literal common N-prime witnesses. Every retained E.62 final value, each of its three distribution tuples and all four orbifold norm values coexist. The whole word fibre is the displayed coset of the actual common kernel. E.69 retains the first Gaussian central layer with its actual six substitutions. Its complete correction image is the product of the Mordell rank-three space and three Heisenberg groups of order27, of total order3^12. The exact E.67 projection is its abelianization; E.68 therefore proves the common E.66 source is the full product of order189321481108517289984. Each of the 1152 retained combinations has three Gaussian framed lifts, and all3456 actual common N-prime words are replayed. The full word fibres retain the specified common kernel. E.63 proves the complete 2.A6 source and its exact signed common quotient of order 9331200000. The entire 125-dimensional relative binary kernel survives while preserving the signed, triple-cover, uniform congruence and nilpotent boundary system of E.60. Its perfect common residual has relative kernel dimension 122, and stable actual commutators fill all three remaining characters. Every specified finite point and full boundary family extends with the same Galois values. The double/triple joint target is the exact fibre product over the old signed-A6 target, with order 2^557*3^271*5^117*7^8*11^3*13^2 and a perfect kernel over the specified order-20736 solvable quotient. All four new complete source presentations and independent literal replays pass root isolated replay. E.73 computes this additional binary source overlap and its exact deep image. E.70 computes the entire Gaussian pro-three six-coordinate image as the specified fibre product of two free-group triples over their class-two quotient. Its abelianization has rank12, including all six weight-three characters. The complete same-source finite Frattini comparison proves its full product with E.66 and the unchanged finite Mordell image. All3456 E.69 finite combinations have compatible full Gaussian norm lifts. E.71 evaluates both matrix distribution equations on all34 literal GL2(F3)/SL2(F3) epikernels over the entire K6-intersect-F-prime domain. Its exact integral lattice adds95 sixth powers, and its enlargement over N-prime is the actual C4 quotient c2/6 modulo4. Every one of the1152 E.68 values admits all16 coefficient lifts modulo24, with unique finite values and18432 actual full-source words. E.72 supplies integral block-conjugation morphisms proving that the five genus-three homology evaluations have exactly the kernel of the three retained genus-two evaluations. Their same-Galois source families retain all displayed Wajnryb relations and full matrix generation. E.73 computes the actual double-cover/E.62 common quotient, of order 2^17 times 3^6, retaining the complete signed source. Its old-J/E.62 identity kernel is exactly the 122-dimensional kernel of the perfect bridge. On N-prime, descent by the actual C_J2-times-identity subgroup identifies the reduced source with V6 times the entire E.62 class-two two-group, through six explicit parity masks. On I=gamma5(Nhat) intersect R_nil(H), the exact image is V6 times the 2^15-element intersection of that two-group with the whole H-image nilpotent residual. Nested compact source fibres and the matching full-H upper bound prove both inclusions. Every fixed J2 value has precisely a coset of the 64-element E.62 kernel, with the entire common word-kernel fibre. Additional prescribed pentagon targets in these cosets remain to be evaluated. Arbitrary finite pentagon sources remain unresolved."),
 ('F.1','F.1; F.2; F.3; F.4','(a), with a corrected order test','The exact global correction and vanishing equivalences are proved over every number field, including 2 and real places. Orders must be taken after quotienting the maximal divisible subgroup.'),
 ('F.2','F.5; A.22','(a) Proved for the specified finite-rank coefficients','Vanishing is computed for the Tate, cusp, elliptic, intrinsic, exterior-square, and finite-rank higher graded coefficient modules.'),
 ('F.3','F.9; F.10; F.11; F.12','(a) Proved','The genuine integral action, tame equations including 2, obstruction group, Milnor summands, and section fibers are determined.'),
 ('F.4','F.20; F.21; F.22; F.23; F.24; F.25; F.26; F.27; F.28; F.29; F.30; F.31; F.32','(a) Proved','The three full profinite fixed groups are the identity, the actual full cusp inertia group, and the identity. The proof applies valuation uniqueness to the actual cyclotomic kernel, identifies its fixed primitive valuation, and recovers the exact geometric stabilizer. All fixed-lift images follow through the specified quotient maps.'),
]

def arg(text, start):
    assert text[start] == '{'
    depth = 1
    pos = start + 1
    begin = pos
    while depth:
        if text[pos] == '{' and text[pos-1] != '\\': depth += 1
        elif text[pos] == '}' and text[pos-1] != '\\': depth -= 1
        pos += 1
    return text[begin:pos-1], pos

active_sources, pending = set(), [ROOT/'LM7_PUSH_paper.tex']
while pending:
    source = pending.pop()
    if not source.suffix:
        source = source.with_suffix('.tex')
    if source in active_sources:
        continue
    assert source.exists(), source
    active_sources.add(source)
    names = re.findall(r'\\(?:InputIfFileExists|input)\{([^}]+)\}', source.read_text())
    pending.extend(ROOT/name for name in names)

rows = []
for file in sorted(p for p in active_sources if p.is_relative_to(ROOT/'sections')):
    text = file.read_text()
    positions = [m.start() for m in re.finditer(re.escape(r'\begin{statement}'), text)]
    for k, start in enumerate(positions):
        pos = start + len(r'\begin{statement}')
        ident, pos = arg(text, pos)
        status, pos = arg(text, pos)
        title, pos = arg(text, pos)
        end = text.index(r'\end{statement}', pos)
        following = positions[k+1] if k+1 < len(positions) else len(text)
        body = text[pos:end].strip()
        proof = text[end:following]
        rows.append({'id':ident, 'statement':title+'. '+body,
                     'status':status, 'where_proved':str(file.relative_to(ROOT)),
                     '_proof':proof, '_title':title})
ids = {r['id'] for r in rows}
assert len(ids) == len(rows), 'duplicate statement id'
for row in rows:
    refs = sorted(set(re.findall(r'\b[A-F]\.\d+\b', row['_proof']+row['statement'])) & ids)
    refs = [r for r in refs if r != row['id']]
    citations = re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', row['_proof'])
    row['depends_on'] = '; '.join(refs + citations)
    row['answers (lead or task)'] = '; '.join(t[0] for t in TASKS if row['id'] in t[1].split('; ')) or 'Supporting result in Part '+row['id'][0]
    row['notes'] = ('Unresolved statement; no completion certified.' if row['status']=='Open'
                    else 'Read the statement and proof for its exact scope; task-level completeness is recorded separately.')
    del row['_proof']; del row['_title']
rows.sort(key=lambda r:(r['id'].split('.')[0], int(r['id'].split('.')[1])))
with (ROOT/'LM7_PUSH_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','answers (lead or task)','notes'])
    writer.writeheader();writer.writerows(rows)

ledger=[{'task':a,'statements':b,'outcome':c,'state':d} for a,b,c,d in TASKS]
(ROOT/'research/task_ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
table='| Lead or task | Statements | Outcome or state reached |\n|---|---|---|\n'
for a,b,c,d in TASKS:
    table+=f'| {a} | {b} | **{c}.** {d} |\n'
tail=(ROOT/'research/report_body.md').read_text()
(ROOT/'LM7_PUSH_report.md').write_text('INCOMPLETE\n\n'+table+'\n'+tail)

def tex_escape(s):
    return (s.replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')
             .replace('^',r'\textasciicircum{}'))

def tex_text(s):
    # Task-state strings use paired dollar signs only for explicit mathematics.
    pieces = re.split(r'(\$[^$]*\$)', s)
    return ''.join(p if p.startswith('$') else tex_escape(p) for p in pieces)
coverage='The following table records task-level scope. A proved supporting statement does not certify an unresolved task.\n'
coverage+=r'\begin{longtable}{@{}p{1.1cm}p{3.0cm}p{10.3cm}@{}}'+'\n'
coverage+=r'\toprule Item & Statements & State \\ \midrule\endhead'+'\n'
def coverage_chunks(text, limit=900):
    # Retain every character and only split at whitespace outside inline math.
    chunks = []
    start = 0
    while len(text) - start > limit:
        math = False
        candidates = []
        for pos in range(start, min(len(text), start + limit)):
            if text[pos] == '$' and (pos == 0 or text[pos-1] != '\\'):
                math = not math
            if text[pos].isspace() and not math:
                candidates.append(pos + 1)
        assert candidates, text[start:start+limit]
        end = candidates[-1]
        chunks.append(text[start:end])
        start = end
    chunks.append(text[start:])
    assert ''.join(chunks) == text
    assert all(chunk.count('$') % 2 == 0 for chunk in chunks)
    return chunks

for a,b,c,d in TASKS:
    for index, chunk in enumerate(coverage_chunks(c+'. '+d)):
        item = a if index == 0 else a + ' cont.'
        statements = b if index == 0 else ''
        coverage+=tex_escape(item)+' & '+tex_escape(statements)+' & '+tex_text(chunk)+r' \\'+'\n'
coverage+=r'\bottomrule\end{longtable}'+'\n'
(ROOT/'sections/coverage.tex').write_text(coverage)

# Merge complete BibTeX entries by key; each fragment is an audited source.
files=[ROOT/'LM7_PUSH_references.bib',ROOT/'research/BC_references.bib',ROOT/'research/DE_references.bib']
entries={}
for file in files:
    text=file.read_text()
    for m in re.finditer(r'@\w+\{([^,]+),',text):
        _,end=arg(text,text.index('{',m.start()))
        entries[m.group(1)]=text[m.start():end]
assert all(re.search(r'\b(?:unverified|verified)\b',v) for v in entries.values())
(ROOT/'LM7_PUSH_references.bib').write_text('\n\n'.join(entries.values())+'\n')
print(json.dumps({'numbered_statements':len(rows),'coverage_rows':len(TASKS),
                  'active_tex_source_count':len(active_sources),
                  'statuses':{s:sum(r['status']==s for r in rows) for s in sorted({r['status'] for r in rows})},
                  'bibliography_entries':len(entries)},indent=2))
