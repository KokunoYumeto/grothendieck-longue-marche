#!/usr/bin/env python3
"""Exact, post-freeze enumeration and table calculations for cote 72/035--081.

Run from any directory:
  python /workspace/scratch/cf8f74b97916/MPL_72_035-081_work/research/recompute_enumerations.py --max-n 12 --matrix-max-n 5

Requires Python 3 and SymPy. Reads frozen TeX as text only, writes files whose
names begin enumeration_, matching_, continuant_, or documentary_ beside this
script. It never edits a page, transcription, inventory, record, audit, or log.
All calculations are over ZZ or QQ and are exact. No OCR or image access.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import sys

import sympy as s


HERE = Path(__file__).resolve().parent
WORK = HERE.parent
PAGES = WORK / "pages"
COMMAND = f"python {HERE / 'recompute_enumerations.py'} --max-n 12 --matrix-max-n 5"
CONTEXT_CONTINUANT = "Hua findings register: 72-automorphisms-deform-gm-to-ga"
CONTEXT_BRIEF = "context/README.md, Planning brief (unnumbered)"


def expr(value):
    return str(s.expand(value))


def dump_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def dump_csv(name, rows):
    if not rows:
        return
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with (HERE / name).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})


def continuant(n, b):
    """L_0=1, L_1=2, L_n=2L_(n-1)(tail)-b[0]L_(n-2)(tail2)."""
    b = tuple(b)
    assert n >= 0 and len(b) == max(n - 1, 0), (n, b)
    if n == 0:
        return s.Integer(1)
    if n == 1:
        return s.Integer(2)
    previous, current = s.Integer(1), s.Integer(2)
    for z in b:
        previous, current = current, s.expand(2 * current - z * previous)
    return current


def matching_sets(n, p=None):
    """Edges are 1,...,n-1; a matching has no consecutive edge labels."""
    choices = range(n // 2 + 1) if p is None else (p,)
    for k in choices:
        for edges in itertools.combinations(range(1, n), k):
            if all(v - u >= 2 for u, v in zip(edges, edges[1:])):
                yield edges


def gaps(n, edges):
    if not edges:
        return [n]
    return [edges[0] - 1] + [v - u - 2 for u, v in zip(edges, edges[1:])] + [n - 1 - edges[-1]]


def matching_sum(n, b):
    return s.expand(sum((-1) ** len(j) * 2 ** (n - 2 * len(j)) * s.prod(b[k - 1] for k in j) for j in matching_sets(n)))


def normalized(n, value):
    return s.expand(value / (2 if n % 2 else 1))


def continuant_matrix(n, b):
    a = 2 * s.eye(n)
    for i, z in enumerate(b):
        a[i, i + 1], a[i + 1, i] = -z, -1
    return a


def delta_matrix(c):
    a = s.diag(*(2 * x for x in c))
    for i in range(len(c) - 1):
        a[i, i + 1] = a[i + 1, i] = -c[i + 1]
    return a


def delta_matching(c):
    n = len(c)
    terms = []
    for j in matching_sets(n):
        covered = {i for edge in j for i in (edge - 1, edge)}
        terms.append((-1) ** len(j) * 2 ** (n - 2 * len(j)) * s.prod(c[i] for i in range(n) if i not in covered) * s.prod(c[edge] ** 2 for edge in j))
    return s.expand(sum(terms))


CHECKS = []
QUESTIONS = []


def check(label, residual, scans, parameters=None):
    if isinstance(residual, s.MatrixBase):
        entries = [s.cancel(v) for v in residual]
        zero = all(v == 0 for v in entries)
        shown = [[expr(v) for v in row] for row in residual.tolist()]
    else:
        residual = s.cancel(residual)
        zero = residual == 0
        shown = expr(residual)
    CHECKS.append({"check": label, "scans": scans, "parameters": parameters or {}, "passed": bool(zero), "residual": shown})
    assert zero, (label, parameters, residual)


def question(qid, scan, quote, observation, residual=None, substitution=None, task=None):
    QUESTIONS.append({"id": qid, "scan": scan, "kind": "literal reading / mathematical comparison question", "short_quote": quote, "observation": observation, "computed_residual": None if residual is None else expr(residual), "explicit_substitution": substitution or {}, "verification_task": task or "Revisit the marked source expression against the frozen alternatives; retain the original transcription.", "context_id": CONTEXT_CONTINUANT, "relation": "Computes the continuant or its associated table; does not promote the context group-scheme claim."})


def enumerate_continuants(max_n):
    counts, terms, polynomials, parity, delta_rows, delta_parity = [], [], [], [], [], []
    for n in range(max_n + 1):
        b = s.symbols(f"B1:{n}") if n > 1 else ()
        value = continuant(n, b)
        explicit = matching_sum(n, b)
        check("continuant equals complete matching sum", value - explicit, [47, 49, 52], {"n": n})
        check("path reversal", value - continuant(n, tuple(reversed(b))), [50, 61], {"n": n})
        if n >= 2:
            check("left-end recurrence", value - (2 * continuant(n - 1, b[1:]) - b[0] * continuant(n - 2, b[2:])), [49, 52], {"n": n})
        if n <= 7:
            check("determinant of nonsymmetric tridiagonal A_n", continuant_matrix(n, b).det(method="domain-ge") - value, [49, 52, 57], {"n": n})
        total = 0
        for p in range(n // 2 + 1):
            js = list(matching_sets(n, p))
            expected = math.comb(n - p, p)
            assert len(js) == expected
            total += len(js)
            counts.append({"n": n, "p": p, "edge_labels": f"1..{n-1}", "enumerated": len(js), "binomial_n_minus_p_choose_p": expected, "coefficient_per_monomial": (-1) ** p * 2 ** (n - 2 * p), "gap_variables_equality": p + 1, "gap_total": n - 2 * p, "total_matchings_at_n": sum(math.comb(n - k, k) for k in range(n // 2 + 1)), "scans": "047,049,051"})
            for j in js:
                gap = gaps(n, j)
                assert all(v >= 0 for v in gap) and sum(gap) == n - 2 * p
                reconstructed = tuple(2 * r - 1 + sum(gap[:r]) for r in range(1, p + 1))
                assert reconstructed == j
                covered = {i for edge in j for i in (edge - 1, edge)}
                monomial = s.prod(b[k - 1] for k in j)
                permutation=list(range(1,n+1))
                for edge in j:
                    permutation[edge-1],permutation[edge]=permutation[edge],permutation[edge-1]
                terms.append({"n": n, "p": p, "edges_1_based": list(j), "permutation_1_based":permutation,"unmatched_vertices_0_based": [i for i in range(n) if i not in covered], "gap_tuple": gap, "C_exponents_0_based":[2 if i in j else 0 if i+1 in j else 1 for i in range(n)],"cumulative_B_exponents_0_based":[n-i+int(i in j) for i in range(n)],"coefficient": (-1) ** p * 2 ** (n - 2 * p), "B_monomial": expr(monomial), "term": expr((-1) ** p * 2 ** (n - 2 * p) * monomial)})
        prime = normalized(n, value)
        poly = s.Poly(prime, *b) if b else None
        mod2 = s.Poly(prime, *b, modulus=2).as_expr() if b else s.Integer(int(prime) % 2)
        maximal = sum(s.prod(b[k - 1] for k in j) for j in matching_sets(n, n // 2))
        check("parity-normalized maximal-matching reduction", s.Poly(mod2 - maximal, *b, modulus=2).as_expr() if b else s.Integer(int(mod2 - maximal) % 2), [51], {"n": n})
        parity.append({"n": n, "source_prime_denominator": 2 if n % 2 else 1, "L_prime": expr(prime), "mod_2_polynomial": expr(mod2), "maximal_matching_size": n // 2, "surviving_monomials_mod_2": 1 if n % 2 == 0 else (n + 1) // 2, "all_coefficients_integral": all(c.q == 1 for c in (poly.coeffs() if poly else [prime]))})
        if n>=1:
            for shifted in (False,True):
                variables=s.symbols(f"B0:{n-1 if shifted else n}")
                monomial=s.prod(variables[i]**(len(variables)-i) for i in range(len(variables)))
                lvars=variables if shifted else variables[1:]
                value_delta=s.expand(monomial*normalized(n,continuant(n,lvars)))
                reduction=s.Poly(value_delta,*variables,modulus=2).as_expr() if variables else s.Integer(int(value_delta)%2)
                square_root=""
                if n%2==0:
                    k=n//2
                    root=variables[0]**k*s.prod((variables[2*r-1]*variables[2*r])**(k-r) for r in range(1,k)) if shifted else s.prod((variables[2*r]*variables[2*r+1])**(k-r) for r in range(k))
                    check("even delta reduction square",s.Poly(reduction-root**2,*variables,modulus=2).as_expr(),[51],{"n":n,"leading_argument_one":shifted})
                    square_root=expr(root)
                delta_parity.append({"n":n,"leading_argument_one":shifted,"source_family":"delta_n_prime(1,B0,...,B(n-2))" if shifted else "delta_n_prime(B0,...,B(n-1))","mod_2_polynomial":expr(reduction),"square_root_for_even_n":square_root,"surviving_terms":1 if n%2==0 else (n+1)//2})
        alphas = s.symbols(f"alpha1:{n}") if n > 1 else ()
        polynomials.append({"n": n, "arity": max(n - 1, 0), "L_n": expr(value), "L_n_Bi_equals_alphai_plus_2": expr(value.subs(dict(zip(b, (x + 2 for x in alphas))))), "total_distinct_monomials": total, "degree": n // 2, "L_prime": expr(prime)})
        if n <= 7:
            c = s.symbols(f"C0:{n}")
            delta = delta_matching(c)
            check("symmetric tridiagonal determinant matching sum", delta_matrix(c).det(method="domain-ge") - delta, [46, 47, 49], {"n": n})
            if n >= 2:
                check("Delta left-end recurrence", delta - (2 * c[0] * delta_matching(c[1:]) - c[1] ** 2 * delta_matching(c[2:])), [46, 49, 52], {"n": n})
            bb = s.symbols(f"B0:{n}")
            cc = [s.prod(bb[:i + 1]) for i in range(n)]
            substituted = s.expand(delta.subs(dict(zip(c, cc))))
            factor = s.prod(bb[i] ** (n - i) for i in range(n))
            check("Delta substitution factors as M_n L_n", substituted - factor * continuant(n, bb[1:]), [49, 50, 51, 52], {"n": n})
            check("entrywise Delta substitution D A_n", delta_matrix(cc) - s.diag(*cc) * continuant_matrix(n, bb[1:]), [49, 52], {"n": n})
            delta_prime=normalized(n,delta)
            substituted_prime=normalized(n,substituted)
            quotient_c=s.cancel(delta_prime/c[-1]) if n else s.Integer(1)
            quotient_b=s.cancel(substituted_prime/bb[-1]) if n else s.Integer(1)
            if n:
                check("Delta prime divisible by last C",delta_prime-c[-1]*quotient_c,[49],{"n":n})
                assert s.denom(quotient_c)==1 and s.denom(quotient_b)==1
            delta_rows.append({"n": n, "Delta_n_C": expr(delta), "Delta_prime":expr(delta_prime),"Delta_prime_quotient_C_last":expr(quotient_c),"map_C_i": "C_i -> product(B_0,...,B_i)", "M_n": expr(factor), "delta_n_B": expr(substituted),"delta_prime_B":expr(substituted_prime),"delta_prime_quotient_B_last":expr(quotient_b), "quotient_L_n": expr(continuant(n, bb[1:]))})
    dump_csv("matching_counts.csv", counts)
    dump_csv("matching_terms.csv", terms)
    dump_csv("continuant_polynomials.csv", polynomials)
    dump_csv("continuant_parity.csv", parity)
    dump_csv("continuant_determinants.csv", delta_rows)
    dump_csv("continuant_delta_parity.csv",delta_parity)
    return {"n_range": [0, max_n], "matching_count_rows": len(counts), "individual_matchings": len(terms), "determinant_symbolic_n_range": [0, min(max_n, 7)]}


def model(n):
    b = s.symbols(f"beta0:{n}")
    d = n + 2
    eye = s.eye(d)
    p = s.eye(d)
    for r in range(1, d):
        p[r, r - 1] = -2
    for r in range(2, d):
        p[r, r - 2] = b[r - 2]
    pi = p.inv().applyfunc(s.expand)
    q = [s.prod(b[:i]) for i in range(n + 1)]
    qp = [s.prod(b[i:]) for i in range(n + 1)]
    g = s.diag(0, *(2 * v for v in q))
    gp = s.diag(*(2 * v for v in qp), 0)
    for r in range(d - 1):
        g[r, r + 1] = g[r + 1, r] = -q[r]
        gp[r, r + 1] = gp[r + 1, r] = -qp[r]
    psi = (pi * g).applyfunc(s.expand)
    psip = (pi.T * gp).applyfunc(s.expand)
    rho = continuant(n + 1, b)
    sigma = continuant(n, b[1:])
    sigma_reverse = continuant(n, b[:-1])
    gamma = continuant(n - 1, b[1:-1])
    beta = s.prod(b)
    center = pi.T[:, -1]
    center_dual = pi[:, 0]
    theta = (sigma * psip + gamma * center * eye[-1, :]).applyfunc(s.expand)
    vertices = s.Matrix(d, d, lambda r, c: 1 if r <= c else 0)
    vertices_dual = s.Matrix(d, d, lambda r, c: 1 if r >= c else 0)
    t = (theta * vertices_dual).applyfunc(s.expand)
    scaled_centered = (center * s.ones(1, d) - rho * vertices).applyfunc(s.expand)
    return locals()


def enumerate_matrices(max_n):
    entries, basis, vectors, small, counts, norms, centereds, zetas = [], [], [], [], [], [], [], []
    for n in range(1, max_n + 1):
        z = model(n)
        b,d,p,pi,g,gp,psi,psip,rho,sigma,sigma_reverse,gamma,beta,center,center_dual,theta,vertices,vertices_dual,t,scaled_centered = (z[k] for k in ("b","d","p","pi","g","gp","psi","psip","rho","sigma","sigma_reverse","gamma","beta","center","center_dual","theta","vertices","vertices_dual","t","scaled_centered"))
        eye = s.eye(d)
        check("pairing determinant", p.det() - 1, [59], {"n": n})
        check("full pairing inverse", p * pi - eye, [59, 61], {"n": n})
        restriction = p[1:, :-1]
        mu=s.symbols(f"mu0:{n+1}")
        general_pairing=p.copy()
        for r in range(1,d):
            general_pairing[r,r-1]=mu[r-1]
        check("general pairing specialization mu_i -> -2",general_pairing.subs(dict(zip(mu,[-2]*(n+1))))-p,[48,59],{"n":n})
        check("general pairing determinant",general_pairing.det()-1,[59],{"n":n})
        check("Q transpose equals negative continuant matrix", restriction.T + continuant_matrix(n + 1, b), [57, 59], {"n": n})
        check("restricted pairing determinant sign", restriction.det(method="domain-ge") - (-1) ** (n + 1) * rho, [57, 59], {"n": n})
        product = s.eye(2)
        for value in b:
            product = product * s.Matrix([[2,-value],[1,0]])
        product = product * s.Matrix([[2,1],[1,0]])
        check("two by two transfer product", product - s.Matrix([[rho,sigma_reverse],[sigma,gamma]]), [61, 63], {"n": n})
        check("four continuants determinant identity", sigma * sigma_reverse - rho * gamma - beta, [63, 65, 67], {"n": n})
        check("Psi restricted basis columns", psi[:,1:] - s.Matrix(d,n+1,lambda r,c: -z['q'][c] if r==c else 0), [61], {"n":n})
        check("Psi prime restricted basis columns", psip[:,:-1] - s.Matrix(d,n+1,lambda r,c: -z['qp'][c] if r==c+1 else 0), [63], {"n":n})
        check("Psi center", psi * center + sigma * center_dual, [48, 61], {"n":n})
        check("Psi prime center dual", psip * center_dual + sigma_reverse * center, [63], {"n":n})
        check("composition rank one", psip * psi - beta * eye - gamma * center * eye[0,:], [63], {"n":n})
        check("Theta Psi denominator identity", theta * psi - beta * sigma * eye, [63], {"n":n})
        check("Psi Theta denominator identity", psi * theta - beta * sigma * eye, [63], {"n":n})
        check("Theta center dual", theta * center_dual + beta * center, [63], {"n":n})
        coefficient_table = s.zeros(d)
        for r in range(d):
            for c in range(r + 1):
                coefficient_table[r,c] = continuant(r-c, b[c:r-1] if r-c>=2 else ())
        check("dual basis interval continuants", pi - coefficient_table, [61], {"n":n})
        pairing_vertices = (vertices.T*p*vertices_dual).applyfunc(s.expand)
        polar_vertices=(vertices.T*g*vertices).applyfunc(s.expand)
        expected_polar=s.Matrix(d,d,lambda i,j: 0 if i==j else -z['q'][int(min(i,j))])
        check("source polar vertex table",polar_vertices-expected_polar,[45,46],{"n":n})
        completed = s.Matrix(d,d,lambda i,j: 0 if i<j else 1 if i==j else sum(b[k]-1 for k in range(j,i-1)))
        check("vertex pairing complete table", pairing_vertices-completed, [65], {"n":n})
        check("primal vertex center-dual pairing", vertices.T*p*center_dual-s.ones(d,1), [65], {"n":n})
        check("dual vertex center pairing", center.T*p*vertices_dual-s.ones(1,d), [65], {"n":n})
        final = t[:,-1]
        check("final t vector", final + sigma*pi.T[:,-2]-gamma*center, [65,69], {"n":n})
        check("t affine evaluation", t[0,:]+beta*s.ones(1,d), [65], {"n":n})
        check("t final polar pairing", g*final-beta*sigma*eye[:,-1], [65], {"n":n})
        qform = lambda v: s.expand((v.T*g*v)[0]/2)
        for i in range(d):
            check("isotropic primal vertices",qform(vertices[:,i]),[45,48],{"n":n,"i":i})
            check("equal t vertex norms",qform(t[:,i])-qform(final),[65,67],{"n":n,"i":i})
            check("equal centered vertex norms",qform(scaled_centered[:,i])-rho*sigma/2,[75,78],{"n":n,"i":i})
        check("norm of center", 2*qform(center)+rho*sigma, [48,53,61], {"n":n})
        check("norm of t final", 2*qform(final)-beta*sigma*gamma, [65,69], {"n":n})
        u = vertices[:,0]+vertices[:,1]
        v = t[:,-2]+t[:,-1]
        check("norm of primal midpoint sum", qform(u)+1, [67], {"n":n})
        check("norm of dual midpoint sum", qform(v)-beta*sigma*(2*gamma-sigma), [67], {"n":n})
        m = s.prod(b[i]**(n-i) for i in range(n))
        check("full polar determinant", g.det(method="domain-ge")+m*sigma, [46,49,53], {"n":n})
        check("restricted polar determinant", g[1:,1:].det(method="domain-ge")-m*rho, [53,75], {"n":n})
        rho_norm, sigma_norm = normalized(n+1,rho), normalized(n,sigma)
        check("parity normalized product", rho_norm*sigma_norm-rho*sigma/2, [53,75,78], {"n":n})
        check("centered scaled vertex norm", qform(scaled_centered[:,0])-rho_norm*sigma_norm, [75,78], {"n":n})
        check("centered successive vertices", scaled_centered[:,1:]-scaled_centered[:,:-1]+rho*eye[:,1:], [78], {"n":n})
        check("centered polar coefficients", (g*scaled_centered[:,0])[1:,0]-rho*eye[1:,1], [78], {"n":n})
        check("centered adjacent sum norm", qform(scaled_centered[:,0]+scaled_centered[:,1])-(4*rho_norm*sigma_norm-rho**2), [78], {"n":n})
        check("centered adjacent difference norm", qform(scaled_centered[:,0]-scaled_centered[:,1])-rho**2, [78], {"n":n})
        if n % 2 == 0:
            parity_midpoint=4*rho_norm*(sigma_norm-rho_norm)
        else:
            parity_midpoint=rho_norm*(4*sigma_norm-rho_norm)
        check("centered midpoint parity table", qform(scaled_centered[:,0]+scaled_centered[:,1])-parity_midpoint, [78], {"n":n})
        families={"pairing_E_Eprime_general":general_pairing,"pairing_E_Eprime":p,"pairing_V_Vprime":restriction,"inverse_pairing":pi,"polar_E":g,"polar_Eprime":gp,"pairing_s_sprime":pairing_vertices,"polar_s_s":(vertices.T*g*vertices).applyfunc(s.expand),"polar_s_a":(vertices.T*g).applyfunc(s.expand),"Psi":psi,"Psi_prime":psip,"Theta":theta}
        for family, matrix in families.items():
            count = sum(s.expand(value)!=0 for value in matrix)
            counts.append({"n":n,"family":family,"rows":matrix.rows,"columns":matrix.cols,"formal_nonzero_entries":count,"formal_zero_entries":matrix.rows*matrix.cols-count,"ring":"ZZ[mu0,...,mu(n),beta0,...,beta(n-1)]" if family=="pairing_E_Eprime_general" else "ZZ[beta0,...,beta(n-1)]"})
            for r in range(matrix.rows):
                for c in range(matrix.cols):
                    entries.append({"n":n,"family":family,"row_0_based":r,"column_0_based":c,"entry":expr(matrix[r,c])})
        for r in range(d):
            for c in range(d):
                basis.append({"n":n,"dual_basis":"a_i^* expressed in a'_j","i":c-1,"j":r,"coefficient":expr(pi[r,c]),"boundary_size":r-c})
                basis.append({"n":n,"dual_basis":"a'_j^* expressed in a_i","i":r-1,"j":c,"coefficient":expr(pi.T[r,c]),"boundary_size":c-r})
        for family,matrix in {"s":vertices,"sprime":vertices_dual,"t":t,"scaled_centered_s":scaled_centered,"Pi":center,"Pi_prime":center_dual}.items():
            for r in range(matrix.rows):
                for c in range(matrix.cols):
                    vectors.append({"n":n,"family":family,"vector_index":c,"basis_index":r if family in ("sprime","Pi_prime") else r-1,"coefficient":expr(matrix[r,c])})
        for r in range(d):
            zetas.append({"n":n,"source_zeta_index":r-1,"L_index":n+1-r,"L_arguments":[str(v) for v in b[r:]],"zeta_polynomial":expr(center[r]),"scans":"048,052,061,073"})
        norms.append({"n":n,"rho":expr(rho),"sigma_tail":expr(sigma),"sigma_reverse":expr(sigma_reverse),"gamma":expr(gamma),"beta_product":expr(beta),"rho_normalized":expr(rho_norm),"sigma_normalized":expr(sigma_norm),"q_center":expr(qform(center)),"q_t_final":expr(qform(final)),"q_s0_plus_s1":expr(qform(u)),"q_tn_plus_tnplus1":expr(qform(v))})
        centereds.append({"n":n,"rho":expr(rho),"sigma_tail":expr(sigma),"rho_prime_source_075_078":expr(rho_norm),"sigma_prime_source_075_078":expr(sigma_norm),"q_scaled_s0":expr(qform(scaled_centered[:,0])),"q_scaled_s0_plus_scaled_s1":expr(qform(scaled_centered[:,0]+scaled_centered[:,1])),"q_scaled_s0_minus_scaled_s1":expr(rho**2),"q_tilde_s0_rational":str(s.cancel(sigma/(2*rho))),"ratio_midpoint_norm_to_vertex_norm":str(s.cancel((4*rho_norm*sigma_norm-rho**2)/(rho_norm*sigma_norm)))})
        if n<=2:
            aa=s.symbols(f"alpha0:{n}")
            substitution=dict(zip(b,[a+2 for a in aa]))
            for name,value in [("rho",rho),("sigma_tail",sigma),("sigma_reverse",sigma_reverse),("gamma",gamma),("beta_product",beta),("q_t_final",qform(final))]+[(f"t_final_coefficient_a{i-1}",final[i]) for i in range(d)]:
                small.append({"n":n,"quantity":name,"beta_expression":expr(value),"map":"beta_i -> alpha_i+2","alpha_expression":expr(value.subs(substitution)),"scan":69})
    dump_csv("enumeration_matrix_entries.csv",entries)
    dump_csv("enumeration_matrix_counts.csv",counts)
    dump_csv("enumeration_dual_basis.csv",basis)
    dump_csv("enumeration_vectors.csv",vectors)
    dump_csv("enumeration_norms.csv",norms)
    dump_csv("enumeration_centered_tables.csv",centereds)
    dump_csv("enumeration_n1_n2.csv",small)
    dump_csv("continuant_zeta.csv",zetas)
    return {"n_range":[1,max_n],"matrix_entries":len(entries),"dual_basis_entries":len(basis),"vector_entries":len(vectors),"small_dimension_entries":len(small)}


def explicit_low_degree_checks():
    b0,b1,b2=s.symbols("beta0 beta1 beta2")
    a0,a1,a2,a3=s.symbols("alpha0 alpha1 alpha2 alpha3")
    check("source L2 local alpha map",continuant(2,[a0+2])-(2-a0),[50],{"map":"B1 -> alpha0+2"})
    check("source L3 local alpha map",continuant(3,[a1+2,a2+2])+2*(a1+a2),[50],{"map":"Bi -> alphai+2"})
    check("source L4 alpha expansion",continuant(4,[a1+2,a2+2,a3+2])-((a1-2)*(a3-2)-4*(a2+2)),[48,50],{"map":"Bi -> alphai+2"})
    check("source delta2 normalized first cumulative variable",delta_matching([1,b0])-b0*(4-b0),[50])
    check("source delta3 prime example",delta_matching([1,b0,b0*b1])/2+b0*b0*b1*((b0-2)+(b1-2)),[50])
    check("source delta4 example",delta_matching([1,b0,b0*b1,b0*b1*b2])-b0**3*b1**2*b2*((b0-4)*(b2-4)-4*b1),[50])
    z=model(2)
    mapping={z['b'][0]:a0+2,z['b'][1]:a1+2}
    literal=z['t'][:,-1].subs(mapping)
    literal[2]=2+a1*a1
    gram=z['g'].subs(mapping)
    literal_norm=s.expand((literal.T*gram*literal)[0]/2)
    printed_norm=(4-a1*a1)*(2+a0)
    check("n2 first exponent reading norm residual",literal_norm-printed_norm-(a0+2)*(a1*a1-a1)**2,[69])


def literal_questions():
    B=s.symbols("B0:5")
    a0,a1=s.symbols("alpha0 alpha1")
    rho,sigma,sigmar,gamma,beta=s.symbols("rho sigma sigma_reverse gamma beta")
    question("E-Q045-margin-a1",45,"varphi(s0,s1)=varphi(s0,a1)","The main table gives varphi(s0,s1)=-1 and varphi(s0,a1)=0; the inserted continuation gives varphi(s0,a0)=-1. The first equality has residual-1 in the same source model.",-1,{"n":1,"varphi_s0_s1":-1,"varphi_s0_a1":0},"Revisit the margin's a1 label while retaining its inserted continuation and the frozen text.")
    question("E-Q047-identity",47,"sum_{1<=p<=n/2}","The first p=0 term contributes the identity permutation. At n=2 the literal p>=1 polynomial is -B1 and the complete determinant is 4-B1.",-4,{"n":2},"Compare the lower bound1 on047 with049's lower bound0 and its note Attention p=0!.")
    question("E-Q047-gap",47,"sum alpha_i=n-2p","With p gap variables the equality misses the terminal slack: n=3,p=1 yields edge2 only, while edges1 and2 are both matchings.",-1,{"n":3,"p":1,"literal_gap_count":1,"matching_count":2},"Use p+1 gaps with equality, or p gaps with sum<=n-2p; retain which line is literally written.")
    question("E-Q049-recurrence",49,"Delta_{n-1|n-2}","The determinant expansion has second factor Delta_(n-2)(C2,...). The two frozen subscript readings have different matrix sizes.",task="Revisit the second recurrence subscript; the exact row/column expansion is supplied in computation_conventions.md.")
    question("E-Q049-arity",49,"L_n(B1,...,B_{n-1})","The following linear sum starts at0 and the cubic range reachesn, outside the n-1 variables supplied to L_n; the nearby margin says n-1 et non n.",task="Check each index bound separately; no extra variable is silently discarded in the computation.")
    question("E-Q049-full-sketch",49,"... -c2 & -c3 ...","The first full matrix sketch has an additional -c3 in the second superdiagonal of its fourth written row. The exact model is obtained from the entry formulas045/046 and the second tridiagonal matrix on049; the ragged first sketch remains a reading question.",task="Check the extra off-band entry and the schematic row alignment; do not treat all blank cells as a newly inferred matrix.")
    question("E-Q049-last-exponent",49,"B_{n-1}^{epsilon_n}","The matching term after C_i=product_(k<=i)B_k has exponent n-k+1_(k in J) on B_k. Its last exponent is1+epsilon_n in the source's shifted epsilon indexing.",task="Check the missing baseline1 at the final exponent and the surrounding epsilon index shift.")
    question("E-Q049-tilde-index",49,"Delta'_n=C_{n-1} tildeDelta'_{n-1}","The margin uses a tilde subscript n-1, while the three examples label the quotient by n. The quotient is exactly Delta'_n/C_(n-1) in the polynomial ring.",task="Compare quotient subscripts and supplied arguments; use the explicit quotient definition without silently relabelling the source.")
    question("E-Q050-product",50,"(2-B1/2)...(2-Bn/2)=(-1)^n/2^n","Under B_i=B'_i+4 the product equals (-1)^n*product(B'_i)/2^n. For n=1,B'_1=0 the displayed left side is0 and the displayed scalar right side is-1/2.",s.Rational(1,2),{"n":1,"Bprime1":0},"Check whether a product of the B'_i is omitted at the end of the line.")
    literal=16-4*sum(B[1:4])+sum(B[i]*B[j] for i in range(1,4) for j in range(i,4))-(B[1]*B[2]+B[2]*B[3]+B[3]*B[4])
    expected=continuant(4,B[1:4])
    question("E-Q050-L4",50,"sum_{1<=i<=j<=3} B_i B_j","The live B-polynomial and the correct alpha-polynomial on the same page have the following residual under the explicit substitution B_i=alpha_i+2; the deleted B4 in the linear sum is excluded here.",literal-expected,task="Check the weak inequality and final B3B4 subtraction in the B-polynomial; the final alpha expression verifies exactly.")
    question("E-Q050-index-map",50,"L2=4-B1=2-alpha0","The L2 line uses B1=alpha0+2; the L3 and L4 alpha lines use Bi=alphai+2. Both maps are reported explicitly.",task="Keep these two local index maps separate when comparing source examples.")
    question("E-Q050-extra-one",50,"B0 L2(1,B0)","L2 is defined with one argument and the later polynomial B0(4-B0) equals B0*L2(B0). The first displayed L2 term supplies an extra leading1.",task="Revisit the leading1 as a local arity question.")
    question("E-Q050-reversal-subscript",50,"L_{n-1}(B1,...,B_{n-1})","The n-1 listed variables fit L_n; the source reversal line labels both sides L_(n-1). The path reversal bijection proves the equal-arity polynomial identity.",task="Check the subscript while retaining reversal as a proved exact identity for the defined continuants.")
    question("E-Q051-final-square-exponent",51,"... (B_{2m-2}B_{2m-1})","The even-delta product's last factor is printed without exponent2; its underbrace is explicitly the square of a product. The computed exponent of each variable in that last pair is2.",task="Check the final exponent against the underbraced square and continuant_delta_parity.csv.")
    question("E-Q051-shifted-pair-comma",51,"(B_{2m-1},B_{2m})","The shifted even-delta square ends with a comma between its last pair of variables. The polynomial square root computed from the matching formula uses their product.",task="Verify whether the comma is a multiplication separator or another reading.")
    question("E-Q053-sigma-arity",53,"sigma=L_n(beta0,...,beta_{n-1})","This line supplies n variables to L_n, whose matching/determinant definition supplies n-1. Scans052 and061 give the tail beta1,...,beta(n-1).",task="Revisit the initial beta index without changing the frozen source.")
    question("E-Q053-Gram-sign",53,"delta_E=B sigma","The source045/046 polar matrix has determinant-M_n*sigma_tail; the written053 value is+M_n*sigma_tail. Their exact relation is multiplication by-1, and written053 minus the046 determinant is2*M_n*sigma_tail.",2*s.Symbol("M_n")*sigma,{"n":1,"beta0":1,"det_G_E":-2,"written_delta_E":2},"Verify the discriminant sign convention between046 and053; retain both source expressions.")
    question("E-Q057-sign",57,"det(-2,1,beta)=L_{n+1}=rho","For Q of size n+1 with diagonal-2, upper1, lowerbeta, Q^T=-A_(n+1), hence det Q=(-1)^(n+1)rho. At n=2,beta0=beta1=1, detQ=-4 and rho=4.",-8,{"n":2,"beta0":1,"beta1":1},"Check whether a determinant sign convention or a missing factor is intended.")
    question("E-Q061-interval-arity",61,"L_{j-i+1}(beta_j,...,beta_i)","The reverse list has j-i+1 variables and therefore fits L_(j-i+2), exactly as the preceding forward list. The frozen subscript is marked unsure.",task="Compare the two displayed arities while retaining the unsure marker.")
    question("E-Q061-basis-star",61,"a'_j{}^*=a_{j-1}^*+...","The computed dual-to-Eprime basis vector has coefficients in the primal E basis a_i. The displayed right-hand stars alternate with unstarred terminal terms.",task="Verify the basis labels against the pairing identification; coefficient values are in enumeration_dual_basis.csv.")
    question("E-Q069-first-exponent",69,"2+alpha1^2 | alpha1","The first frozen reading gives coefficient2+alpha1^2 on a1, while the underbrace beta1 and the computed coefficient give2+alpha1. The coefficient residual is alpha1^2-alpha1; the corresponding norm residual is (alpha0+2)*(alpha1^2-alpha1)^2.",a1*a1-a1,{"alpha0":0,"alpha1":2,"literal_coefficient":6,"computed_coefficient":4,"literal_norm":8,"computed_norm":0},"Verify the superscript-shaped mark and retain both frozen readings; this comparison does not select a transcription.")
    question("E-Q071-centered-vertices",71,"s_tilde_i=s_tilde_0-1/rho [a0+...+a_{i-1}]","The displayed definition s_tilde_i=s_i-Pi/rho and the source increment s_i-s_0=sum a_j give the increment +sum a_j. Multiplication by rho makes the residual -(rho+1)sum a_j.",-(rho+1),{"basis_increment_coefficient":1},"Compare this line with the explicit plus increment on078.")
    actual=-(2*gamma-sigma)*rho-2*beta
    printed_first=-(2*gamma*rho-sigma*rho-2*beta)
    question("E-Q071-a_nminus1-first",71,"-(2gamma rho-sigma rho-2beta)/(beta rho)","Subtracting the displayed preceding expression and clearing beta*rho gives4beta.",printed_first-actual,task="Check the sign of2beta in the first combined numerator.")
    printed_last=-sigma*(2*sigmar+rho)
    coherent=sigma*(rho-2*sigmar)
    question("E-Q071-a_nminus1-last",71,"-sigma[2sigma'+rho]/(beta rho)","Using sigma*sigma_reverse=beta+gamma*rho, the preceding coefficient is sigma*(rho-2sigma_reverse)/(beta*rho). The last printed expression has cleared residual-2sigma*rho.",printed_last-coherent,task="Check the sign ofrho in the last bracket separately from the earlier numerator.")
    question("E-Q071-t-increment",71,"+rho beta(a_n+beta_{n-1}a_{n-1}+...)","From t_i=t_(n+1)-sigma*tail and -rho*beta*s_tilde_t_i=rho*t_i+beta*Pi, the scaled increment is -rho*tail. The printed increment has residual rho*(beta+1)*tail.",rho*(beta+1),task="Check both sign and extra beta in the final increment line.")
    question("E-Q073-zeta-arity",73,"L_{n+i|n-i}","zeta_i has n-i-1 listed beta variables, so L_(n-i) has the displayed arity; the first frozen subscript alternative n+i has a different arity except i=0.",task="Keep the two marked subscript alternatives; use the explicit basis-coefficient table for comparison.")
    question("E-Q073-sigma-endpoint",73,"L_n(beta1,...,beta_n)=sigma","The reversed left list ends atbeta1 and has n-1 variables; the right list ends atbeta_n and supplies n variables.",task="Verify the right endpoint separately from reversal symmetry.")
    question("E-Q078-midpoint-sign",78,"f_V(s'_0 -|+ s'_1)","The first reading of the later sign gives normrho^2, whereas the displayed parity table is the norm of the sum,2rho*sigma-rho^2. Their difference is2rho(rho-sigma).",2*rho*(rho-sigma),{"n":2,"beta0":1,"beta1":1,"difference":8},"Compare the first and second frozen sign alternatives with the immediately preceding sum computation.")


def documentary_data():
    """Literal text lists, without external person resolution or identity merging."""
    lists = [
        ("D060-jury",60,"Composition du jury proposé",["Ph. JEANTEUR","B. LEBLEU","CJ LARSEN","J. DEMAILLE"]),
        ("D062-jury",62,"Composition du jury proposé",["PISTOULET, Président","ROBERT","RAYMOND","LEROUX HUGON","THUILLIER"]),
        ("D064-jury",64,"Composition du jury",["M. R. LEGENDRE, Président","M. M. GODRON","M. J. BONS","M. G. PASTEUR"]),
        ("D068-jury",68,"Membres du jury",["David W. LEE","B. SAUGIER","F. HALLE"]),
        ("D070-represented-top",70,"Etaient représentés (top)",[("GOUT","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]")]),
        ("D070-absent-top",70,"Etaient absents ou excusés (top)",["[name redacted]","[name redacted]","[name redacted]","[name redacted]","[name redacted]","[name redacted]","[name redacted]","[name redacted]","Mle [name redacted]","Mme [name redacted]"]),
        ("D070-directors",70,"Directeur d'U.E.R.",["[name redacted]","[name redacted]","[name redacted]","[name redacted]"]),
        ("D070-agenda-120",70,"CONSEIL RESTREINT AUX ENSEIGNANTS: agenda",["I. Approbation d'un procès-verbal","II. Commissions de spécialistes","III. Sécurité dans les laboratoires"]),
        ("D070-present-120",70,"Etaient présents (120ème séance)",["[name redacted]","[name redacted]","GOUT","[name redacted]","[name redacted]","Mme PARIS","[name redacted]","[name redacted]","Mme [name redacted]","[name redacted]","[name redacted]","[name redacted]"]),
        ("D070-represented-120",70,"Etaient représentés (120ème séance)",[("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]"),("[name redacted]","[name redacted]")]),
        ("D070-absent-120-literal-atoms",70,"Etaient absents ou excusés (120ème séance), comma-delimited atoms",["[name redacted]","[name redacted]","[name redacted]","Mme [name redacted]","M.M. [name redacted]\\\\\nBERTRAND","Mme [name redacted] [name redacted]","M.M. [name redacted]","[name redacted]","[name redacted]"]),
        ("D066-personnel-119",66,"personnels (119ème séance)",["enseignants","chercheurs","administratifs","techniques","ouvriers","de service"]),
        ("D064-indices",64,"Différents indices",["probabilité de présence","diversité spécifique","richesse spécifique"]),
    ]
    form_fields=["Nom et prénom du candidat","Titre de la thèse","Date, heure et lieu de soutenance prévus","Nom du Directeur de thèse","Désignation du laboratoire où la thèse est préparée","Analyse de l'ouvrage","Durée approximative des recherches ayant abouti à la thèse","Composition du jury proposé"]
    for scan in (60,62,64):
        labels=list(form_fields)
        if scan==62:
            labels[0]="Nom et prénom de la candidate"
        if scan==64:
            labels[-1]="Composition du jury"
        lists.append((f"D{scan:03d}-form-fields",scan,"Thesis notice labelled fields",labels))
    sessions=[
        (116,"15 Décembre 1977",["Conseil plénier"]),
        (117,"12 Janvier 1978",["Conseil restreint aux professeurs titulaires"]),
        (118,"26 Janvier 1978",["a) aux membres électeurs au Conseil Scientifique","b) aux membres enseignants du Conseil"]),
        (119,"17 Février 1978",["personnels enseignants, chercheurs, administratifs, techniques, ouvriers et de service"]),
        (120,"3 Mars 1978",["Conseil restreint aux enseignants"]),
        (121,"16 Mars 1978",["Conseil restreint aux professeurs titulaires"]),
    ]
    items, totals = [],[]
    for list_id,scan,label,values in lists:
        for index,value in enumerate(values,1):
            if isinstance(value,tuple):
                items.append({"id":list_id,"scan":scan,"label":label,"index":index,"literal_item":value[0],"representative":value[1]})
            else:
                items.append({"id":list_id,"scan":scan,"label":label,"index":index,"literal_item":value,"representative":""})
        totals.append({"id":list_id,"scan":scan,"label":label,"total":len(values),"unit":"representation pairs" if isinstance(values[0],tuple) else "listed items", "qualification":"The [name redacted] line break [name redacted] atom remains unsplit; a two-name reading gives10 persons." if "literal-atoms" in list_id else "Literal listed entries; no cross-list identity merge."})
    session_rows=[]
    for number,date,types in sessions:
        session_rows.append({"scan":66,"session_number":number,"literal_date":date,"council_descriptions":types,"description_count":len(types)})
    totals.append({"id":"D066-sessions","scan":66,"label":"Décisions prises au cours des séances","total":len(sessions),"unit":"dated sessions","qualification":"116..121 inclusive; session118 has two lettered subcategories, hence7 council-description units."})
    totals.append({"id":"D-juries-all","scan":"060,062,064,068","label":"All four jury lists","total":sum(len(v) for i,_,_,v in lists if i.endswith("jury")),"unit":"name occurrences","qualification":"4+5+4+3=16; shared names, titles and people are not resolved externally."})
    metadata=[
        {"scan":60,"mspage_occurrences":["59"],"notice_number":"4001","document_date":"26 Juin 1978","event_date":"5 JUILLET 1978","event_time":"14 heures 30mn","room_or_venue":"Salle de cours n6, U.S.T.L.","duration":"2 ans","distribution":"Liste A","initials":"MR/GJ","person":"BLAAS Dieter","director":"Ph. JEANTEUR","field":"BIOCHIMIE","other_numbers":"3ème cycle; salle6"},
        {"scan":62,"mspage_occurrences":["61"],"notice_number":"4151","document_date":"1er Juillet 1978","event_date":"12 JUILLET 1978","event_time":"15 Heures","room_or_venue":"Salle de Séminaire du C.E.E.S.-U.S.T.L.","duration":"Deux ans","distribution":"Liste A","initials":"MR/GJ","person":"MERLET née BERNARD Catherine","director":"ROBERT","field":"PHYSIQUE DU SOLIDE - APPLICATION A L'ELECTRONIQUE","other_numbers":"3ème cycle; dopage10^14 à10^16 cm^-3"},
        {"scan":64,"mspage_occurrences":["63"],"notice_number":"4172","document_date":"3 juillet 1978","event_date":"Jeudi6 juillet [year not repeated in event line]","event_time":"8 heures","room_or_venue":"amphithéâtre9","duration":"3 ans","distribution":"Liste A","initials":"MR/MD","person":"LIVET François","director":"J. BONS","field":"SCIENCES BIOLOGIQUES - Mention ECOLOGIE","other_numbers":"amphithéâtre9; no printed event-year inference entered"},
        {"scan":66,"mspage_occurrences":["65"],"notice_number":"Recueil n16","document_date":"MAI1978","event_date":"six sessions; see documentary_sessions.csv","event_time":"","room_or_venue":"Place Eugène Bataillon,34060 MONTPELLIER CEDEX","duration":"","distribution":"","initials":"","person":"MR LE PROFESSEUR GROTHENDIECK A.","director":"","field":"MATHEMATIQUES","other_numbers":"margin/addressee label5; Recueil16; postcode34060; session numbers116..121. These are kept in their printed roles."},
        {"scan":68,"mspage_occurrences":["67"],"notice_number":"4060","document_date":"28 Juin 1978","event_date":"29 JUIN1978","event_time":"10 Heures","room_or_venue":"Laboratoire de M. le Professeur HALLE; Institut de Botanique; U.S.T.L.","duration":"","distribution":"Liste A","initials":"MR/GJ","person":"Ibrahima DIAITE","director":"","field":"Diplôme d'Etudes Supérieures d'Université","other_numbers":"notice4060"},
        {"scan":70,"mspage_occurrences":["69"],"notice_number":"","document_date":"Vendredi3 Mars1978 (lower session)","event_date":"120ème séance","event_time":"","room_or_venue":"","duration":"","distribution":"","initials":"","person":"","director":"","field":"CONSEIL RESTREINT AUX ENSEIGNANTS","other_numbers":"printed/margin page5|3; mspage69; upper meeting's session number not supplied on this scan; lower agendaI,II,III"},
    ]
    dump_csv("documentary_items.csv",items)
    dump_csv("documentary_totals.csv",totals)
    dump_csv("documentary_sessions.csv",session_rows)
    dump_csv("documentary_metadata.csv",metadata)
    dump_json("documentary_lists.json",{"lists":[{"id":i,"scan":p,"label":l,"items":v} for i,p,l,v in lists],"sessions":session_rows,"totals":totals,"metadata":metadata,"reading_question":{"scan":70,"literal_atom":"M.M. [name redacted]\\\\\nBERTRAND","comma_delimited_atoms":9,"two_name_split_total":10,"operation_for_candidate":"Replace the one literal atom by the two tokens [name redacted] and [name redacted]; no source edit or person-identity claim."}})
    return {"source_lists":len(lists)+1,"literal_items_excluding_sessions":len(items),"sessions":6,"jury_occurrences":16,"last_absence_literal_atoms":9,"last_absence_candidate_names":10}


def source_metadata():
    rows, hashes = [],{}
    for n in range(35,82):
        path=PAGES/f"MPL_72_035-081_72_scan{n:03d}.tex"
        data=path.read_bytes()
        text=data.decode("utf-8")
        hashes[str(path.relative_to(WORK))]=hashlib.sha256(data).hexdigest()
        rows.append({"scan":n,"filename":path.name,"scanpage_occurrences":re.findall(r"\\scanpage\{([^}]*)\}",text),"mspage_occurrences":re.findall(r"\\mspage\{([^}]*)\}",text),"mspage_count":len(re.findall(r"\\mspage\{",text)),"other_numbering_note":"mspage60 occurs twice" if n==61 else "printed/margin5|3 and mspage69" if n==70 else "addressee5; Recueil16; sessions116..121; mspage65" if n==66 else ""})
    combined=WORK/"MPL_72_035-081_transcription.tex"
    hashes[combined.name]=hashlib.sha256(combined.read_bytes()).hexdigest()
    assert len(hashes)==48
    dump_csv("enumeration_page_metadata.csv",rows)
    dump_json("enumeration_source_hashes.json",hashes)
    return hashes


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n",type=int,default=12)
    parser.add_argument("--matrix-max-n",type=int,default=5)
    args=parser.parse_args()
    if not 2<=args.max_n<=18 or not 2<=args.matrix_max_n<=7:
        parser.error("Use 2<=max-n<=18 and 2<=matrix-max-n<=7 for the explicit output tables.")
    before=source_metadata()
    matching=enumerate_continuants(args.max_n)
    matrices=enumerate_matrices(args.matrix_max_n)
    explicit_low_degree_checks()
    literal_questions()
    documentary=documentary_data()
    after={name:hashlib.sha256((WORK/name).read_bytes()).hexdigest() for name in before}
    assert before==after,"A frozen source changed during this research run."
    dump_json("enumeration_reading_questions.json",QUESTIONS)
    dump_csv("enumeration_reading_questions.csv",QUESTIONS)
    dump_json("enumeration_checks.json",{"parameters":vars(args),"python":sys.version.split()[0],"sympy":s.__version__,"command":COMMAND,"ring":"ZZ[formal beta variables], with rational expressions explicitly displayed only after localization","matching":matching,"matrices":matrices,"documentary":documentary,"checked_frozen_source_hashes":48,"frozen_sources_unchanged_during_run":before==after,"checks":CHECKS,"all_exact_checks_passed":all(c['passed'] for c in CHECKS),"literal_questions":len(QUESTIONS),"other_research_outputs":"invariant_subspaces.py and group_quadric_checks.py have separate owners and are not overwritten by this script."})
    from enumeration_catalogue import build_catalogue
    catalogue=build_catalogue()
    print(json.dumps({"all_exact_checks_passed":all(c['passed'] for c in CHECKS),"exact_checks":len(CHECKS),"matching":matching,"matrices":matrices,"documentary":documentary,"catalogue":catalogue,"literal_questions":len(QUESTIONS),"frozen_sources_unchanged":before==after},indent=2))


if __name__=="__main__":
    main()
