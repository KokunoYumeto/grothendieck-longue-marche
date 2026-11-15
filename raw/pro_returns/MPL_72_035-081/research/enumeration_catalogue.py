#!/usr/bin/env python3
"""Build the scan catalogue from fixed source anchors and exact run outputs.

Called by recompute_enumerations.py; can also be run directly after that script.
Writes only enumeration_catalogue.csv/json, enumeration_scan_coverage.csv and
enumeration_pairing_cases.csv in this research directory.
"""
import csv
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
COMMAND=f"python {HERE/'recompute_enumerations.py'} --max-n 12 --matrix-max-n 5"
CONT="Hua findings register: 72-automorphisms-deform-gm-to-ga"
BRIEF="context/README.md, Planning brief (unnumbered)"


def build_catalogue():
    rows=[]
    def add(i,scans,quote,what,parameters,total,files,kind="exact polynomial computation",qualification="",context=CONT):
        rows.append({"id":i,"scans":','.join(f'{v:03d}' for v in scans),"short_source_quote":quote,"what_is_enumerated":what,"parameters":parameters,"total_or_formula":total,"kind":kind,"outputs":files,"qualification":qualification,"context_id":context,"context_relation":"Supplies the explicit continuant/coordinate calculation for the parameter rho mentioned in that claim; its group-scheme verdict is not adopted." if context==CONT else "Fulfils the calculation/list catalogue requested by the unnumbered planning brief. No numbered context row matching these documentary lists was found.","rerun_command":COMMAND})
    add("E-C045-polar",[45,46,48],"f(a_i)=c_{i-1}","Quadratic coefficient table and polar pairings for a_-1,...,a_n and s_0,...,s_(n+1)","n>=1; beta0,...,beta(n-1); c_-1=1,c_i=product_(k<=i)beta_k","E dimension n+2; (n+2)^2 polar entries; 3n+3 formal nonzero entries; 2n+2 quadratic monomials","enumeration_matrix_entries.csv; enumeration_matrix_counts.csv; enumeration_vectors.csv")
    add("E-C046-Delta",[46,49,50,52],"F_n(c_0,...,c_{n-1})","Symmetric tridiagonal determinant Delta_n, its recurrence, and the polar restriction determinant","n=0..7 in determinant output; n variables C0,...,C(n-1)","n^2 matrix positions; 3n-2 nonzero positions for n>=1; sum_p binomial(n-p,p) determinant monomials","continuant_determinants.csv; matching_terms.csv","proved recurrence plus finite exact determinant checks","The ragged first full sketch on049 is retained as E-Q049-full-sketch; the entry formulas define the computed matrix.")
    add("E-C046-low",[46,49],"Delta_1=2c_0","Low-order Delta_1,Delta_2,Delta_3 and their primed/tilde quotients","n=1,2,3; source C variables","3 determinants; expanded monomial counts1,2,3, total6","continuant_determinants.csv")
    add("E-C046-cycles",[46],"permutation circulaire u,u^{-1}","The labelled circular permutation and its inverse","labels0..n-1; n=1..12 in output","two named permutations; explicit distinct-count column includes coincidences in orders1 and2","enumeration_circular_permutations.csv","literal diagram labels and exact finite maps","The arrows are recorded as i->i+1 modulo n and inverse i->i-1 modulo n.")
    add("E-C047-permutations",[47,49],"sigma(i) in {i-1,i,i+1}","Permutations supported on the tridiagonal and their disjoint adjacent transpositions","n=0..12; p=0..floor(n/2); edge labels1..n-1","binomial(n-p,p) for fixed p; totals1,1,2,3,5,8,13,21,34,55,89,144,233;609 across n=0..12","matching_counts.csv; matching_terms.csv","proved bijection plus explicit finite enumeration")
    add("E-C047-gaps",[47],"sum alpha_i=n-2p","Gap coordinates for p pairwise nonadjacent path edges","p+1 nonnegative gaps summing n-2p; or p nonnegative gaps with sum<=n-2p","binomial(n-p,p); n=3,p=1 gives2","matching_terms.csv; enumeration_reading_questions.csv","proved bijection","E-Q047-gap records the missing terminal slack in the literal equality with only p variables.")
    add("E-C048-pairing",[48,59],"mu_i=lambda_i-1","Four-case pairing table, with general mu and reflection specialization","N=n+2; n=1..5 in full tables; mu_i -> -2; beta_i -> alpha_i+2 in reflection coordinates","full table N^2; case counts0:N^2-(3N-3),1:N,mu:N-1,beta:N-2","enumeration_pairing_cases.csv; enumeration_matrix_entries.csv","exact table and explicit specialization")
    add("E-C048-zeta",[48,52,61,73],"zeta_n=1, zeta_{n-1}=2","Backward center-coordinate recurrence and its low-degree terms","indices i=-1..n; zeta_i=L_(n-i)(beta_(i+1),...,beta_(n-1)); n=1..5 in output","n+2 coordinates per n; source048 has5 completed endpoint expressions and1 unfinished zeta_(n-5) line","continuant_zeta.csv; continuant_polynomials.csv; enumeration_vectors.csv","proved recurrence and finite coefficient table","sigma on048 denotes the norm, related to the later tail sigma by2sigma_048=-rho*sigma_tail.")
    add("E-C049-primes",[49,51],"Delta'_n","Parity-normalized determinants and quotients by the last C or B variable","even n: denominator1; odd n: denominator2; n=1..7","2 parity rules; quotient formulas are polynomials","continuant_determinants.csv; continuant_parity.csv","integral polynomial computation","The tilde quotient subscript is a source question E-Q049-tilde-index.")
    add("E-C049-monomials",[49],"Il n'y a pas de cancellation de termes","Matching monomials in C variables and their images under cumulative B substitution","C_i -> product_(k=0..i)B_k; J subset1..n-1 has no adjacent labels","coefficient(-1)^p2^(n-2p); exponents C:0/1/2, B_k:n-k+1_(k in J)","matching_terms.csv; continuant_determinants.csv","proved polynomial substitution")
    add("E-C050-L-low",[50],"L_1=2","L_1,L_2,L_3,L_4, their alpha forms, and three specialized discriminants","L2 uses B1=alpha0+2; L3,L4 use Bi=alphai+2; Delta orders2,3,4 use leading cumulative variable1","4 L examples with1,2,3,5 monomials;3 specialized discriminants","continuant_polynomials.csv; continuant_determinants.csv; enumeration_checks.json","exact low-degree calculation","The literal B-expression for L4 has residualB1^2+B2^2+B3^2-B3B4; the final alpha expression verifies.")
    add("E-C050-shift",[50],"B_i=B'_i+4","Displayed shifted product and adjacent B'_i B'_(i+1) relations","n>=1; homomorphism B_i -> B'_i+4","product(2-B_i/2)=(-1)^n product(B'_i)/2^n; n=1,B'_1=0 comparison","enumeration_reading_questions.csv","computed comparison / verification task","The scalar-only right side is recorded in E-Q050-product.")
    add("E-C051-L-parity",[51,52],"mod 2","Parity tables for L_(2m) and L'_(2m+1)","n=0..12; maximal matchings; reduction ZZ -> F2","even:1 monomial; odd n=2m+1:m+1 monomials","continuant_parity.csv; matching_terms.csv","proved coefficient reduction")
    add("E-C051-delta-parity",[51],"delta_{2m}","Four determinant parity families, including leading-argument1 and square roots in even order","delta'_n(B0,...,B(n-1)) and delta'_n(1,B0,...,B(n-2)); n=1..12","24 output rows; each even row1 squared monomial; each odd row(n+1)/2 monomials","continuant_delta_parity.csv","exact polynomial reduction","Literal exponent/comma questions are E-Q051-final-square-exponent and E-Q051-shifted-pair-comma.")
    add("E-C052-recurrences",[52],"L_n=2L_{n-1}-B_1L_{n-2}","Unprimed and even/odd primed recurrence table","n>=2; L0=1,L1=2; source parity normalization","3 recurrence rows, with the applicable parity indices","continuant_polynomials.csv; enumeration_checks.json","proved recurrence","Second determinant subscript n-1|n-2 is retained as a reading question.")
    add("E-C057-sketches",[57],"a'_0 definit -2a_0^*+beta_0a_1^*","Cancelled triangular sketch, live cyclic sketch, and final tridiagonal determinant","Sketches retain blanks/ellipsis and literal indices; final restriction size n+1","3 displayed matrix sketches; the final band model has(n+1)^2 positions and3n+1 formal nonzero entries","enumeration_matrix_entries.csv; enumeration_reading_questions.csv","source catalogue plus precise verification task","The first two schematic arrays are not filled with inferred entries. The final determinant's sign is checked by Q^T=-A.")
    add("E-C059-bases",[59],"V~=O_S^{n+1}","Two ordered full bases and the V,V' restrictions; pairing incidence diagrams","E:a_-1..a_n; E':a'_0..a'_(n+1); V,V' have n+1 listed basis vectors","2(n+2) full basis symbols;2(n+1) restricted symbols","enumeration_pairing_cases.csv; enumeration_matrix_entries.csv","basis/index catalogue","The final b-row ending b_(n+2) is a literal label question, not an inferred extra basis vector.")
    add("E-C061-intervals",[61],"rho_ij=L_{j-i+2}","Interval continuants, their two boundary values, and rho,sigma,sigma',gamma","rho_ij for0<=i<=j<=n-1, plus rho_(i,i-1)=2 and rho_(i,i-2)=1","n(n+1)/2 nonempty intervals;4 named corner continuants;2 boundary values","continuant_zeta.csv; enumeration_dual_basis.csv; enumeration_norms.csv","proved interval recurrence","Reverse-subscript and basis-star questions are preserved in E-Q061-interval-arity and E-Q061-basis-star.")
    add("E-C061-dual-basis",[61],"a_i^*=a'_{i+1}+2a'_{i+2}+...","Two full dual-basis coefficient tables","N=n+2; P inverse and inverse transpose; n=1..5","2N^2 entries per n; N(N+1) nonzero entries in the two triangular tables;270 total entries over n=1..5","enumeration_dual_basis.csv","proved inverse matrix formula")
    add("E-C061-Psi",[61,63],"Psi(a_i)=-(beta_0...beta_{i-1})a'_i","Psi,Psi' and quadratic basis values in the two directions","q_i=product_(k<i)beta_k; q'_i=product_(k>=i)beta_k; n=1..5","two N-by-N maps; two N-entry quadratic basis lists","enumeration_matrix_entries.csv; enumeration_norms.csv","exact matrix computation")
    add("E-C063-transfer",[63,65,67],"sigma sigma'=beta+gamma rho","Four-continuant table and compositions of Psi,Psi',Theta","rho=L_(n+1)(all), sigma=L_n(tail), sigma_reverse=L_n(head), gamma=L_(n-1)(middle)","4 named polynomials; determinant identity from a2-by-2 transfer product; Theta Psi=Psi Theta=beta*sigma I","enumeration_norms.csv; enumeration_matrix_entries.csv; enumeration_checks.json","proved polynomial identities")
    add("E-C063-cancelled",[63],"s_0=a_{-1}","Cancelled draft s/s'/t coordinate list and two-case polar pairing","Draft retained inside deleted block; live replacement on065","source draft, including2 written cases for polar(t0,s_i)","enumeration_reading_questions.csv; frozen scan063 TeX","cancelled-source catalogue / verification task","The cancellation status is preserved. Live table065 defines the computed vectors.")
    add("E-C065-vertices",[65],"s_{i+1}=tau_i s_i","Primal and dual vertex sequences and their complete pairing table","s_i=sum_(r=0..i)e_r; s'_j=sum_(c=j..n+1)e'_c; n=1..5","2(n+2) vectors; (n+2)^2 pairings; above diagonal0,diagonal1, first lower diagonal0","enumeration_vectors.csv; enumeration_matrix_entries.csv","proved complete pairing table","The lower entries are explicitly sum_(k=j..i-2)(beta_k-1); source only prints the upper/diagonal cases.")
    add("E-C065-t",[65],"t_i=Theta(s'_i)","n+2 dual-image vertices, coefficients of t_(n+1), and polar/norm values","n=1..5; beta=product beta_i; t_i=t_final-sigma*sum_(j=i..n)q'_j a_j","n+2 vectors of n+2 coefficients each; final affine coefficient-beta and a0 coefficient0","enumeration_vectors.csv; enumeration_norms.csv","proved polynomial identities")
    add("E-C067-norms",[67],"u=s_0+s_1","Four recalled norm values for s0,t_final,u,v","u=s0+s1;v=t_n+t_(n+1); n=1..5","q(s0)=0;q(t_final)=beta*sigma*gamma/2;q(u)=-1;q(v)=beta*sigma*(2gamma-sigma)","enumeration_norms.csv; enumeration_checks.json","proved quadratic identities")
    add("E-C069-examples",[69],"n=1; n=2","Two explicit low-dimensional parameter, vector and norm examples","beta_i=alpha_i+2; n=1,2","2 dimension cases;19 scalar/vector-coordinate output rows","enumeration_n1_n2.csv; enumeration_reading_questions.csv","exact symbolic computation","The first alpha1^2 reading is evaluated, not removed; E-Q069-first-exponent gives its nonzero residual.")
    add("E-C071-centered",[71,73],"p_lambda(x)=x/lambda-Pi/rho","Centered s_i,u,t_i coefficient formulas and dual covector endpoint/interior table","R localized at rho; t formulas also at beta; source-specific further denominators retained","n+2 centered s vectors; n+2 t vectors;3 covector cases:initial,interior,terminal","enumeration_vectors.csv; enumeration_centered_tables.csv; enumeration_reading_questions.csv","exact coordinate maps and reading comparisons","E-Q071-* records the displayed increment/numerator differences; E-Q073-* records the arities.")
    add("E-C075-078-norms",[75,78],"f_V(s'_0)=rho' sigma'","Even/odd centered radius table, sum/difference norms, and homothety squared ratio","rho'=L'_(n+1);sigma'=L'_n(tail);s'_i=Pi-rho*s_i; n=1..5","2 parity rows;2 adjacent-vector signs; ratio4-rho^2/(rho' sigma')","enumeration_centered_tables.csv; enumeration_checks.json","proved polynomial identities and explicit localization","The primed sigma here equals parity-normalized tail sigma; the scan061 reverse sigma is related by sigma_tail*sigma_reverse=beta+gamma*rho.")
    add("E-D060",[60],"Composition du jury proposé","Thesis notice fields and jury","notice4001;26 Juin1978;event5 JUILLET1978,14h30;duration2ans","8 labelled fields;4 jury entries","documentary_items.csv; documentary_metadata.csv; documentary_totals.csv","literal documentary list count",context=BRIEF)
    add("E-D062",[62],"Composition du jury proposé","Thesis notice fields and jury","notice4151;1er Juillet1978;event12 JUILLET1978,15h;durationDeux ans","8 labelled fields;5 jury entries; doping range has two stated endpoints, not a sample count","documentary_items.csv; documentary_metadata.csv; documentary_totals.csv","literal documentary list count",context=BRIEF)
    add("E-D064",[64],"Composition du jury","Thesis notice fields, jury, and named ecological indices","notice4172;3 juillet1978;eventJeudi6 juillet,8h;duration3ans","8 labelled fields;4 jury entries;3 named indices","documentary_items.csv; documentary_metadata.csv; documentary_totals.csv","literal documentary list count",context=BRIEF)
    add("E-D066",[66],"Décisions prises au cours des séances","Council-session table, session118 subcategories, session119 personnel categories","Recueil16,MAI1978;sessions116..121","6 dated sessions;7 council-description units because118 has2;6 personnel categories in119","documentary_sessions.csv; documentary_items.csv; documentary_metadata.csv","literal documentary table count","Addressee label5, postcode34060, Recueil16 and session numbers retain separate documentary roles.",context=BRIEF)
    add("E-D068",[68],"Membres du jury","Diploma notice jury and event metadata","notice4060;28 Juin1978;event29 JUIN1978,10h","3 jury entries; four jury lists on060,062,064,068 contain16 name occurrences in total","documentary_items.csv; documentary_metadata.csv; documentary_totals.csv","literal documentary list count",context=BRIEF)
    add("E-D070-top",[70],"Etaient représentés","Upper meeting's representation, absence, and director lists","meeting identity not repeated on this scan","8 representation pairs;10 absent/excused name tokens;4 directors","documentary_items.csv; documentary_totals.csv","literal documentary list count","The upper lists are not assigned session120 from the lower heading.",context=BRIEF)
    add("E-D070-lower",[70],"120ème séance","Agenda, attendance, representation and absence lists","Vendredi3 Mars1978;printed page5|3;mspage69","3 agenda items;12 present tokens;4 representation pairs;9 literal comma-delimited absent atoms, or10 tokens after the explicitly recorded ROUZAUD/BERTRAND split","documentary_items.csv; documentary_lists.json; documentary_totals.csv","literal documentary list count","The candidate split changes one atom to two tokens and leaves the frozen text intact.",context=BRIEF)
    add("E-D-page-markers",[60,61,62,64,66,68,70],"mspage60; mspage60","Printed/source numbering and scan-to-manuscript markers","all47 scans035..081 are read as text","47 scan records; scan061 has two occurrences ofmspage60; documentary numbers are not page-count surrogates","enumeration_page_metadata.csv; documentary_metadata.csv","literal marker audit",context=BRIEF)
    fieldnames=list(rows[0])
    with (HERE/'enumeration_catalogue.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader();w.writerows(rows)
    (HERE/'enumeration_catalogue.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    root_cases={36,38,41,42,43,45,53,54,55,74,75,76,77,81}
    headings={37,44,56,72,79}
    coverage=[]
    for scan in range(35,82):
        relevant=[row['id'] for row in rows if f'{scan:03d}' in row['scans'].split(',')]
        remarks=[]
        if scan in root_cases:remarks.append('Root separately catalogues prose parameter/condition/case lists on this scan.')
        if scan in headings:remarks.append('Heading/caption page; no independent tabulated enumeration.')
        if scan==35:remarks.append('Prose conic uniqueness claim with source doubt; root research owns it.')
        if scan==39:remarks.append('Paired rank-one action formulas; group_quadric_checks.py owns their verification.')
        if scan==40:remarks.append('Orthogonality equation; group_quadric_checks.py owns its verification.')
        if scan==58:remarks.append('Cancelled invariant-subspace trial: casesa,b and subcases1,2; root invariant-subspace research owns it.')
        if scan in (80,81):remarks.append('Invariant-subspace enumeration is in invariant_subspaces.py and invariant_subspaces_cases.csv, owned separately; not recomputed here.')
        coverage.append({'scan':f'{scan:03d}','catalogue_ids':';'.join(relevant),'scope_note':' '.join(remarks)})
    with (HERE/'enumeration_scan_coverage.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(coverage[0]));w.writeheader();w.writerows(coverage)
    checks=json.loads((HERE/'enumeration_checks.json').read_text())
    cycles=[]
    for n in range(1,checks['parameters']['max_n']+1):
        forward=[(i+1)%n for i in range(n)]
        inverse=[(i-1)%n for i in range(n)]
        cycles.append({'scan':46,'n':n,'labels_0_based':list(range(n)),'u':forward,'u_inverse':inverse,'named_permutations':2,'distinct_permutations':len({tuple(forward),tuple(inverse)})})
    with (HERE/'enumeration_circular_permutations.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(cycles[0]));w.writeheader();w.writerows(cycles)
    pairs=[]
    for n in range(1,checks['parameters']['matrix_max_n']+1):
        N=n+2
        for space,counts in [('full_E_Eprime',{'zero':N*N-(3*N-3),'one':N,'mu':N-1,'beta':N-2}),('restricted_V_Vprime',{'zero':n*n-n,'one':n,'mu':n+1,'beta':n})]:
            for label,count in counts.items():pairs.append({'n':n,'space':space,'source_case':label,'count':count,'scans':'048,059'})
    with (HERE/'enumeration_pairing_cases.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(pairs[0]));w.writeheader();w.writerows(pairs)
    return {'catalogue_entries':len(rows),'scan_coverage_rows':len(coverage),'pairing_case_rows':len(pairs),'circular_permutation_rows':len(cycles)}


if __name__=='__main__':
    print(json.dumps(build_catalogue(),indent=2))
