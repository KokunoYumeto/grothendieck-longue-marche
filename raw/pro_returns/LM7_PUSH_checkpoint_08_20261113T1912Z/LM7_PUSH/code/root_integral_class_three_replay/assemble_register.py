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
 ('D.1', 'D.1; D.4; D.6; D.20; D.21; D.22; D.23; D.24; D.25; D.26; D.27; D.28; D.29; D.30; D.31; D.32; D.33; D.34; D.35; D.36; D.37', 'OPEN: dimension one or three', 'The actual geometric S3 action excludes dimension two. The complete chief-step lifting and obstruction comparisons are retained. Fully invariant finite five-group targets P_n of order 5^(17n+2) now carry all three compatible ordinary special outer parameters, with the exact S3 action and inner powers accounted for. Their kernels are proved fully invariant by Fox substitution. Realization or exclusion of the two-dimensional complement through every finer full finite source remains.'),
 ('D.2', 'D.2; D.4; D.6; D.7; D.8; D.20; D.22; D.23; D.24; D.25; D.26; D.27; D.28; D.29; D.30; D.31; D.32; D.33; D.34; D.35; D.36', 'OPEN: dimension one or two', 'The extra weight-nine vector, gamma line and complete finite pentagon comparison are verified. Elementary abelian and central obstructions, the complete A5 chief-step count, and the ordinary order-five A6^20 obstruction retain their actual source maps and every centralizer choice. The latter also retains an admitted component above the prescribed five-group shadow. A cofinal equivariant lift or exclusion of the extra gentle direction remains.'),
 ('D.3','D.3; D.4; D.7; D.8; D.20','(a) Proved','Compatible finite braid quotients give gentle/pentagon dimensions 37/2 and leading metabelian dimensions 2/1. The integer certificate and actual Galois lower bound derive R9 in weight nine.'),
 ('E.1','E.1; E.4','(a) Proved','Independent exact programs confirm every count, cusp equation, generation certificate, and both Smith forms.'),
 ('E.2', 'E.2; E.5; E.7; E.8; E.9; E.10; E.11; E.12; E.13; E.14; E.15; E.16; E.20; E.22; E.23; E.24; E.25; E.26; E.27; E.28; E.29; E.31; E.33; E.36; E.37; E.38; E.41; E.42; E.43; E.44; E.45; E.46', 'OPEN: complete CM fibers', 'All24 CM fibres survive every proved refinement through E46. The exponent-three class-three boundary test adds four congruences beyond the full three-adic class-two tower and excludes one specified full-tower point, while retaining all432 multiplier-one sources. The compatible boundary fibre is Z3^10 times F3^22. Both A6 kernel/outer tests and the five-point A96 Hurwitz test retain all864 finite points, with exact boundary gluing maps. Full profinite survival remains.'),
 ('E.3', 'E.3; D.5; E.6; E.17; E.18; E.19; E.21; E.22; E.23; E.24; E.25; E.26; E.27; E.28; E.29; E.30; E.31; E.32; E.33; E.34; E.35; E.36; E.37; E.38; E.39; E.40; E.41; E.42; E.43; E.44; E.45; E.46', 'OPEN: full GT image', 'All864 degree-six points pass the retained full pentagons, braid and twist relations. The A6 kernel/outer tests and five-point A96 Hurwitz test retain them through exact correction and common-quotient maps. The actual SL2(F5) source maps onto the Hurwitz source, so the same corrected word retains both with every E42/E44 boundary family. The full common four-strand target is (T23 times over S_L T_L) times A96. Compatibility through every finite quotient remains.'),
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
coverage='The following table records task-level scope. A proved supporting statement does not certify an unresolved task.\n'
coverage+=r'\begin{longtable}{@{}p{1.1cm}p{3.0cm}p{10.3cm}@{}}'+'\n'
coverage+=r'\toprule Item & Statements & State \\ \midrule\endhead'+'\n'
for a,b,c,d in TASKS:
    coverage+=tex_escape(a)+' & '+tex_escape(b)+' & '+tex_escape(c+'. '+d)+r' \\'+'\n'
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
