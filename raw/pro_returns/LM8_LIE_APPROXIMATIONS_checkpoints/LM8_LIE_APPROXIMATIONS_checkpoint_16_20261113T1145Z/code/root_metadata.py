#!/usr/bin/env python3
"""Rebuild root-owned statement/coverage ledgers from the actual paper source."""
from pathlib import Path
import re,json,csv
ROOT=Path(__file__).resolve().parents[1]
SEC=ROOT/'sections'
pattern=re.compile(r"\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}\s*(.*?)\\end\{statement\}",re.S)
def statements(files):
    result=[]
    for name in files:
        text=(SEC/name).read_text()
        matches=list(pattern.finditer(text))
        for i,m in enumerate(matches):
            ident,status,title,claim=m.groups()
            end=matches[i+1].start() if i+1<len(matches) else len(text)
            context=text[m.end():end]
            deps=sorted(set(re.findall(r"\b[A-G]\.\d+[a-z]?\b",context))-{ident})
            passages=re.findall(r"\\MS\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}",claim+context)
            if passages:passages=[f'Section {a}; folio {b}; scan {c} (cote 140-4)' for a,b,c in passages]
            elif ident.startswith('B.'):passages=['Section 52.3-4; folios 748-758; scans 201-221; mathematical follow-up tasks stated separately in the prompt']
            else:passages=['Section 51, equations (371)-(373); folios 734 and 736; scans 173 and 178; explicit Selmer tasks in prompt Part F']
            result.append(dict(id=ident,statement=title+' — '+re.sub(r'\s+',' ',claim).strip(),status=status,where_proved='sections/'+name+', '+ident,depends_on=deps,manuscript_passages=passages,depends_on_doubtful_reading=False,notes='Full claim, assumptions and proof or recorded residual attack are in the indicated source.'))
    return result
b=statements(['B.tex','e_exceptional_lifting.tex'])
f=[r for r in statements(['F.tex']) if r['id']!='F.15']
# F.15 has its separately audited F_limit_results.json ledger.
def order(x):
    a=re.match(r'([A-G])\.(\d+)([a-z]*)',x['id']);return (a[1],int(a[2]),a[3])
for prefix,rows in [('B',b),('F',f)]:
    rows.sort(key=order)
    (SEC/(prefix+'_results.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(prefix,len(rows),'statements')
coverage=[
('item3','Axioms, one-parameter statements, presentations, limiting topos','proved_or_refuted_with_corrected_scope',['B.1','B.2','D.1','D.2','D.3','D.4','D.5','D.7','D.8','D.9','D.10','D.11','D.12','D.13','D.14','D.15','D.16','D.17','D.18','D.19','D.20','D.21','D.22','D.23','E.11'],['D.21 proves the positive-power theorem over every quasi-compact quasi-separated base; D.14 refutes quasi-compactness alone. D.22 proves the actual smooth-model existence question with its adelic factorization; D.23 refutes the stronger integral-point recap and uniqueness from the preceding data alone']),
('item4','Successive Lie approximations, examples and splittings','partial',['B.3','B.4','B.5','F.1','F.2','F.9','F.12','F.16','F.17','F.18','F.19','F.20','F.21','F.22','F.23','F.24'],['No canonical numbered stages in the manuscript; chosen towers are explicit','The rational elliptic tables through8, real full pro2 metabelian set, unrestricted global pro5 class2 set, integral classes3–4 over S={2,3,5}, actual class5 obstruction, and relative Fermat class5 sets are computed. The unit cusps first separate atclass3. The arbitrary global class3 frame-difference function and higher unrestricted global integral sets remain']),
('Lead1','Identify manuscript Lie approximations with later completions','refuted_and_corrected',['B.1','B.2','B.3','B.20','B.22'],[]),
('B(a)','Galois-Teichmuller axioms and tower','proved',['B.1','B.2'],[]),
('B(b)','Integral envelopes, universal property and filling','proved_for_explicit_virtually_abelian_system',['B.5','B.20','B.21'],[]),
('B(c)','First two approximations in types 03,04,11','proved_for_declared_Malcev_models',['B.3','B.4','D.6'],['The word first is not canonical without a chosen filtration; this ambiguity is resolved explicitly']),
('B(d).03','Special, invariant, normalizer and arithmetic tables through weight14','proved_with_corrected_finite_symmetry',['B.10','B.12','B.15'],[]),
('B(d).04','All requested tables through weight6','proved',['B.16','B.17'],[]),
('B(d).11','Elliptic tables through weight12','proved_via_cited_monodromy_theorem_and_exact_ranks',['B.18','B.19'],[]),
('B(e)','Exactness of filling on normalizers versus full special algebras','literal_surjectivity_to_entire_lower_normalizer_refuted',['B.16','B.17'],[]),
('B(f)','Compare weighted, GT, elliptic GT','typed_comparisons_proved',['B.3','B.22'],[]),
('B(g)','Limiting topos','literal_inverse_topos_degenerates_corrected_germ_topos_constructed',['E.11','E.12','E.13'],[]),
('B.followup(1)','Fundamental localizers and relative Theorem A','proved_for_all_listed_group_functors',['B.6'],['Literal section52 needs arithmetic data and is not a bare-group endofunctor']),
('B.followup(2)','Finite covers: comparison kernels/images and intrinsic fibrations','proved',['B.7','B.9'],[]),
('B.followup(3).Fermat','All approximation comparisons on Fermat covers','proved',['B.8','B.9','B.20'],[]),
('B.followup(3).conjugators','Signed M_rho_sigma and N_rho_sigma action/kernel/image, starting q2','partial',['B.8','B.24','B.24a','B.24b','B.24c','B.24d','B.31','B.32','B.33','B.34'],['The unrestricted minimal integral action is refuted and its first corrected lift functor computed. B31 identifies the actual signed source, preserves all Fermat kernels, and constructs continuous local/profinite relative actions. B32 identifies both whole Fermat detection quotients. B33 computes the exact first modular image. B34 refutes a compatible whole-source rational-base action. Retained conjugator images on q2 and higher stages, complete kernel classification and higher realization of arbitrary polynomial lifts remain']),
('B.followup(4)','All exact-Fermat splitting sets and separation of cusps','partial',['F.4','F.10','F.11','F.12','F.15','F.19','F.20','F.21','F.22','F.23','F.24'],['The real pro2 metabelian, unrestricted global pro5 class2, and integral classes3–4 over S={2,3,5} are computed. F.23 evaluates the actual class5 obstruction and all relative Fermat class5 sets; F.24 proves the specified unit cusps first separate atclass3. The arbitrary global class3 frame-difference function, higher unrestricted global sets, and full global Alexander-module twists remain']),
('B.program.allgroups24','All groups<=24 and all epimorphisms F2 to them','complete',['B.23'],[]),
('B.afterLM2(1)','Three tripod rows through weight14','complete',['B.10'],[]),
('B.afterLM2(2)','Integral special lift, coprime invariants, centralizer, strict inclusion','proved_for_primes_at_least5',['B.11','B.12'],[]),
('B.afterLM2(3)','H1/H2 mod2,3 through9 and q7/2q7/3q7 infinite lifts','proved',['B.13','B.14','B.14a','B.14b','B.14c','B.14d'],['The finite modular groups, actual integral cohomology, integral class14 certificate, and all-degree equivariant lifting theorem are proved separately; the full profinite compatibility problem is a different obligation']),
]
(SEC/'B_coverage.json').write_text(json.dumps([dict(task=t,requested=q,status=s,results=r,remaining=x) for t,q,s,r,x in coverage],ensure_ascii=False,indent=2)+'\n')
fc=[
('F(a)','Tripod global and local dimensions through8 for abelian, nilpotent and metabelian rational Selmer towers','complete_with_specified_local_conditions',['F.1','F.2'],[]),
('F(b)','First strict levels and finiteness','proved',['F.3'],[]),
('F(c)','Rank0/rank1 elliptic dimensions, thresholds, finiteness','proved_through_requested_class8',['F.6','F.7','F.8','F.9','F.16','F.17','F.18'],['All full and metabelian global/local tables through8 and the first strict thresholds are unconditional for the stated refined local conditions']),
('F(d)','What normalizer replacement adds or loses','typed_restriction_inflation_and_limitation_proved',['F.5','F.13'],[]),
('F(e)','Lemmas for LM6 point-section comparison','proved_with_hypotheses',['F.14'],[]),
('F.followup','All Fermat splitting sets, abelian/metabelian/full','partial',['F.4','F.10','F.11','F.12','F.15','F.19','F.20','F.21','F.22','F.23','F.24'],['Power-completed abelian cohomology explicitly computed','F.19 computes the full real pro2 metabelian set. F.20–F.21 compute finite and unrestricted global pro5 class2 sets, including the actual derived-limit cup obstruction. F.22 computes integral classes3–4 over S={2,3,5}. F.23 gives the twelve actual class5 congruences, the nonliftable pair(kappa2,2kappa2), and all relative Fermat class5 sets. F.24 proves the specified unit cusps first separate atclass3. A closed arbitrary-global class3 frame-difference formula, higher unrestricted stages, and full twisted Alexander-module cohomology remain. F.15 supplies the inverse-limit comparison']),
('F.afterLM2','q7 action through8 at every prime and change at finiteness level','proved_for_every_prime',['F.5','B.12','B.14d'],['The automorphism and transported-action statement holds for every prime; the specific Selmer thresholds retain the p>=5 hypotheses of F.3'])]
(SEC/'F_coverage.json').write_text(json.dumps([dict(task=t,requested=q,status=s,results=r,remaining=x) for t,q,s,r,x in fc],ensure_ascii=False,indent=2)+'\n')
with (SEC/'B_readings.csv').open('w',newline='') as h:
    w=csv.writer(h);w.writerow(['package','scan',r'the \unsure or \illegible place','what the mathematics supports','how strongly'])
    w.writerows([
    ['C4','202-208','Strong versus weak condition 3; rational points in diagram (35)','Adelic target and diagonal rationality on G0 are separate requirements; visually checked scan208','Direct reading with proof of typed definition'],
    ['C4','31-32','Section50 formula (58), direction of limit of Hom','Hom out of inverse affine limit into finitely presented target is a direct limit','Mathematical correction, no diplomatic reading claimed'],
    ['C4','173;178','Successive approximations and nouvelle etude des scindages','No canonical class1/class2 filtration is specified; each chosen tower needs local conditions and obstruction tests','Logical distinction proved; not a claim the handwriting is uncertain']])
with (SEC/'F_readings.csv').open('w',newline='') as h:
    w=csv.writer(h);w.writerow(['package','scan',r'the \unsure or \illegible place','what the mathematics supports','how strongly'])
    w.writerow(['C4','173;178','Scindages in (371)-(373)','Unrestricted splittings are not automatically Selmer varieties; local conditions must be supplied','Exact mathematical qualification, no unresolved glyph used'])
