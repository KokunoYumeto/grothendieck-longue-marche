#!/usr/bin/env python3
"""Exact checks on stated first readings; never writes the frozen transcription.

Requires SymPy.  Run from any directory; JSON output is written beside this file.
Field-degree and invariant-presentation arguments are in the companion memo;
this script certifies polynomial identities and integer linear algebra only.
"""
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent


def zeros(expr):
    return S.expand(expr) == 0


def zero_matrix(matrix):
    return all(zeros(x) for x in matrix)


def snf(matrix):
    return [abs(int(x)) for x in smith_normal_form(matrix, domain=S.ZZ).diagonal()]


def rank_mod(matrix, prime):
    rows = [[int(x) % prime for x in row] for row in matrix.tolist()]
    rank = 0
    for column in range(matrix.cols):
        pivot = next((i for i in range(rank, matrix.rows) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(x * inverse) % prime for x in rows[rank]]
        for i in range(matrix.rows):
            if i != rank:
                factor = rows[i][column]
                rows[i] = [(a - factor * b) % prime for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == matrix.rows:
            break
    return rank


def generic_matrix(prefix):
    return S.Matrix(2, 2, S.symbols(f"{prefix}11 {prefix}12 {prefix}21 {prefix}22"))


def invariants(x, y, z):
    b, bp, bpp = [m.trace() for m in (x, y, z)]
    c, cp, cpp = [m.det() for m in (x, y, z)]
    t, tp, tpp = (y*z).trace(), (z*x).trace(), (x*y).trace()
    sigma = b*t + bp*tp + bpp*tpp - b*bp*bpp
    printed = (t*tp*tpp + c*t*t + cp*tp*tp + cpp*tpp*tpp
               + b*b*cp*cpp + bp*bp*cpp*c + bpp*bpp*c*cp
               - bp*bpp*c*t - bpp*b*cp*tp - b*bp*cpp*tpp)
    tau, reverse = (x*y*z).trace(), (y*x*z).trace()
    return sigma, printed, c*cp*cpp, tau, reverse


def volume(x, y, z):
    basis_coordinates = lambda m: S.Matrix([m[0,0], m[1,1], m[1,0], m[0,1]])
    return S.Matrix.hstack(*(basis_coordinates(m) for m in (S.eye(2), x, y, z))).det()


def triple_checks():
    x, y, z = [generic_matrix(p) for p in "xyz"]
    sigma, printed, cprod, tau, reverse = invariants(x, y, z)
    assert zeros(sigma - tau - reverse)
    assert zeros(printed - tau*reverse - 4*cprod)
    delta = volume(x, y, z)
    assert zeros(delta - tau + reverse)
    phi = lambda u,v: u.trace()*v.trace() - (u*v).trace()
    basis = [S.eye(2), x, y, z]
    gram = S.Matrix([[phi(u,v) for v in basis] for u in basis])
    assert zeros(gram.det(method="domain-ge") - delta**2)
    b,bp,bpp,c,cp,cpp,t,tp,tpp = S.symbols("b bp bpp c cp cpp t tp tpp")
    formal_gram = S.Matrix([[2,b,bp,bpp],[b,2*c,b*bp-tpp,b*bpp-tp],
                           [bp,b*bp-tpp,2*cp,bp*bpp-t],[bpp,b*bpp-tp,bp*bpp-t,2*cpp]])
    formal_sigma = b*t+bp*tp+bpp*tpp-b*bp*bpp
    formal_printed = (t*tp*tpp+c*t*t+cp*tp*tp+cpp*tpp*tpp+b*b*cp*cpp
                      +bp*bp*cpp*c+bpp*bpp*c*cp-bp*bpp*c*t-bpp*b*cp*tp-b*bp*cpp*tpp)
    residual = S.expand(formal_sigma**2-formal_gram.det(method="domain-ge")-4*formal_printed)
    assert residual == -16*c*cp*cpp
    I=S.eye(2); F=S.Matrix([[0,0],[1,0]]); E=F.T; Z=F*E-E*F; A=S.diag(1,0)
    si,pi,ci,ti,ri=invariants(I,I,I)
    _,_,_,tf,rf=invariants(F,E,Z)
    units=[S.Matrix([[1,0],[0,0]]),S.Matrix([[0,0],[0,1]]),F,E]
    trace_gram=S.Matrix([[(u*v).trace() for v in units]for u in units])
    polar_gram=S.Matrix([[phi(u,v) for v in units]for u in units])
    assert trace_gram.det()==-1 and polar_gram.det()==1
    adj=lambda u:u.trace()*S.eye(2)-u
    assert zero_matrix(adj(x)*x-x.det()*S.eye(2))
    assert zeros(adj(x).det()-x.det())
    coords=lambda u:S.Matrix([u[0,0],u[1,1],u[1,0],u[0,1]])
    adj_linear=S.Matrix.hstack(*(coords(adj(u))for u in units))
    assert adj_linear.det()==-1 and adj(I)==I
    assert adj(E)*adj(F)==units[0] and adj(E*F)==units[1]
    return {
        "universal_sum_identity":True,"universal_corrected_product_identity":True,
        "printed_product_error":"Pi_printed - tau*tau_prime = 4*c*cp*cpp",
        "formal_gram_error_without_correction":str(residual),
        "identity_matrix_witness":{"Sigma":int(si),"Pi_printed":int(pi),"Pi_corrected":int(pi-4*ci),"tau":int(ti),"tau_prime":int(ri)},
        "orientation_basis":"E11,E22,E21,E12",
        "universal_volume_identity":"volume(1,x,y,z)=Tr([x,y]z)",
        "normalization_probe":{"tau":int(tf),"tau_prime":int(rf),"volume":int(volume(F,E,Z)),"Tr_commutator_z":int(((F*E-E*F)*Z).trace()),"scan186_left_tau_prime_minus_tau":int(rf-tf)},
        "unit_volume_probe":{"x":"E21","y":"E12","z":"E11","volume":int(volume(F,E,A)),"Tr_commutator_z":int(((F*E-E*F)*A).trace())},
        "trace_pairing_gram":trace_gram.tolist(),"trace_pairing_determinant":-1,
        "determinant_polar_gram":polar_gram.tolist(),"determinant_polar_determinant":1,
        "char2_identity_witness":{"c_product":1,"Pi_printed_mod2":int(pi%2),"tau_product_mod2":int((ti*ri)%2)},
        "char2_orientation_counterexample":{"adjugate_linear_determinant":-1,"mod2_orientation_multiplier":1,"adjugate_fixes_one_and_preserves_determinant":True,"adj_E12_times_adj_E21":(adj(E)*adj(F)).tolist(),"adj_E12E21":adj(E*F).tolist(),"scope":"ordinary top-exterior-volume orientation only"},
    }


def four_checks():
    xs=[generic_matrix("x"+str(i))for i in range(1,5)]
    bs=[x.trace()for x in xs]; cs=[x.det()for x in xs]
    ys=[x-b*S.eye(2)/2 for x,b in zip(xs,bs)]
    g=S.Matrix([[(u*v).trace()for v in ys]for u in ys])
    h=S.Matrix([[bs[i]**2-4*cs[i] if i==j else 2*(xs[i]*xs[j]).trace()-bs[i]*bs[j]for j in range(4)]for i in range(4)])
    assert zero_matrix(h-2*g)
    vectors=S.Matrix.hstack(*(S.Matrix([y[0,0],y[0,1],y[1,0]])for y in ys))
    J=S.Matrix([[2,0,0],[0,0,1],[0,1,0]])
    assert zero_matrix(g-vectors.T*J*vectors)
    assert zeros(h.det(method="domain-ge"))
    fb=S.symbols("b1:5");fc=S.symbols("c1:5")
    ft={pair:S.Symbol("t"+str(pair[0]+1)+str(pair[1]+1))for pair in itertools.combinations(range(4),2)}
    formal_h=S.Matrix([[fb[i]**2-4*fc[i] if i==j else 2*ft[tuple(sorted((i,j)))]-fb[i]*fb[j]for j in range(4)]for i in range(4)])
    formal_poly=S.Poly(formal_h.det(method="domain-ge"),*(list(fb)+list(fc)+list(ft.values())))
    content,primitive=formal_poly.primitive()
    primitive_mod2=S.Poly(primitive.as_expr(),*primitive.gens,modulus=2)
    substitution=dict(zip(fb,bs))|dict(zip(fc,cs))|{ft[(i,j)]:(xs[i]*xs[j]).trace()for i,j in ft}
    assert zeros(primitive.as_expr().subs(substitution, simultaneous=True))
    omega=lambda i,j,k:(ys[i]*ys[j]*ys[k]-ys[j]*ys[i]*ys[k]).trace()
    for i,j,k in itertools.combinations(range(4),3):
        transpose=(xs[i].T*xs[j].T*xs[k].T-xs[j].T*xs[i].T*xs[k].T).trace()
        assert zeros(transpose+omega(i,j,k))
    alphas=[b/2 for b in bs]
    trace4=2*S.prod(alphas)
    for i,j in itertools.combinations(range(4),2):
        trace4+=S.prod(alphas[k]for k in range(4)if k not in (i,j))*g[i,j]
    for omitted in range(4):
        triple=[i for i in range(4)if i!=omitted]
        trace4+=alphas[omitted]*omega(*triple)/2
    trace4+=(g[0,1]*g[2,3]-g[0,2]*g[1,3]+g[0,3]*g[1,2])/2
    assert zeros(trace4-(xs[0]*xs[1]*xs[2]*xs[3]).trace())
    I=S.eye(2); F=S.Matrix([[0,0],[1,0]]); E=F.T; Z=F*E-E*F
    word1234=(I*F*E*Z).trace();word2134=(F*I*E*Z).trace()
    word3412=(E*Z*I*F).trace();word4312=(Z*E*I*F).trace()
    return {"H_equals_twice_traceless_Gram":True,"Gram_relation_detH_zero":True,
            "formal_Gram_relation":{"integer_content":int(content),"term_count":len(formal_poly.terms()),"primitive_mod2_nonzero":not primitive_mod2.is_zero,"primitive_mod2_term_count":len(primitive_mod2.terms()),"primitive_mod2_polynomial":str(primitive_mod2.as_expr()),"primitive_integer_polynomial":str(primitive.as_expr())},
            "transpose_fixes_scalar_pair_data_and_negates_volumes":True,
            "four_word_trace_formula_verified":True,
            "generic_degree_hypothesis":"Algebraically closed field of characteristic !=2; generic four matrices; a three-vector Gram minor nonzero. See memo proof, not an invariant-base-change claim.",
            "parallel_edge_counterexample":{"matrices":["I","E21","E12","diag(-1,1)"],"T_1234":int(word1234),"T_2134":int(word2134),"T_3412":int(word3412),"T_4312":int(word4312),"Sigma_12_bar_34":int(word1234+word2134),"Sigma_34_bar_12":int(word3412+word4312),"cube_direction_partition":"12|34; complementary endpoint-label pairs12 and34"}}


def cube_checks():
    names="a b c ap bp cp ABp BCp CAp ACp CBp BAp".split()
    v=S.symbols(" ".join(names)); a,b,c,ap,bp,cp,ABp,BCp,CAp,ACp,CBp,BAp=v
    relations=[a+cp-ABp-BCp,a+bp-ACp-CBp,b+ap-BCp-CAp,b+cp-BAp-ACp,
               c+bp-CAp-ABp,c+ap-CBp-BAp,a+CAp-b-CBp,ap+ACp-bp-BCp,
               b+ABp-c-ACp,bp+BAp-cp-CAp,c+BCp-a-BAp,cp+CBp-ap-ABp]
    R=S.Matrix([[expr.coeff(x)for x in v]for expr in relations])
    supports=[("a","b","BCp","ACp"),("a","c","ABp","CBp"),("b","c","CAp","BAp"),
              ("ap","bp","CAp","CBp"),("ap","cp","BCp","BAp"),("bp","cp","ABp","ACp")]
    E=S.Matrix([[int(name in support)for support in supports]for name in names])
    assert R*E==S.zeros(12,6)
    assert E*S.ones(6,1)==2*S.ones(12,1)
    assert S.ones(1,6)*R[6:,:]==S.zeros(1,12)
    V=S.Matrix.hstack(*R.nullspace())
    assert all(x.q==1 for x in V)
    N=S.Matrix([[1,1,1,1,0,0],[-3,1,1,1,4,0],[1,-1,0,1,1,2],
                [-3,1,4,-1,1,2],[-2,0,1,2,1,2],[-2,4,1,-2,1,2]])
    M=S.Matrix([[-1,2,2],[2,-1,2],[2,2,-1]])
    P=M.row_join(S.eye(3)).col_join(S.eye(3).row_join(M))
    assert M*M==9*S.eye(3)
    inverse=M.row_join(-S.eye(3)).col_join((-S.eye(3)).row_join(M))/8
    assert P*inverse==S.eye(6)
    theta=S.symbols("theta"); alternative=P.copy();alternative[0,0]=theta
    T=S.Matrix([[0,1,1],[1,0,1],[1,1,0]])
    pair=S.Matrix([[1,1],[-1,1]])
    return {"scan203_variable_order":names,"scan203_relation_matrix":R.tolist(),
      "scan203_ranks":{"all":R.rank(),"first_six":R[:6,:].rank(),"last_six":R[6:,:].rank()},
      "scan203_smith":{"all":snf(R),"first_six":snf(R[:6,:]),"last_six":snf(R[6:,:])},
      "scan203_ranks_mod2":{"all":rank_mod(R,2),"first_six":rank_mod(R[:6,:],2),"last_six":rank_mod(R[6:,:],2)},
      "last_six_unique_rational_dependency":[1]*6,
      "face_edge_incidence":E.tolist(),"face_edge_smith":snf(E),"face_edge_rank_mod2":rank_mod(E,2),
      "six_selected_edges_determinant":int(E[:6,:].det()),"six_selected_edges_smith":snf(E[:6,:]),
      "relation_kernel_projection_determinant":int(V[:6,:].det()),"relation_kernel_projection_smith":snf(V[:6,:]),
      "constant_edge_counterexample":"all twelve edge values 1 satisfy every written linear relation, but cannot be integer face sums: each triangle sum is odd",
      "scan211":{"matrix":N.tolist(),"determinant":int(N.det()),"rank":N.rank(),"smith":snf(N),"rank_mod2":rank_mod(N,2),"signed_first_row_cofactors":[int((-1)**j*N.minor_submatrix(0,j).det())for j in range(4)]},
      "scan219":{"first_reading_caveat":"entry(1,1) read as -1; it is marked unsure in frozen TeX","matrix":P.tolist(),"M_determinant":int(M.det()),"M_squared":(M*M).tolist(),"determinant":int(P.det()),"rank":P.rank(),"smith":snf(P),"rank_mod2":rank_mod(P,2),"printed_scalar_block_value":728,"determinant_if_first_entry_theta":str(S.factor(alternative.det())),"determinant_if_first_entry_plus1":int(alternative.det().subs(theta,1))},
      "scan215_delta_system":{"matrix":T.tolist(),"determinant":int(T.det()),"smith":snf(T),"rank_mod2":rank_mod(T,2),"inverse":[[str(x)for x in row]for row in T.inv().tolist()]},
      "scan221_sum_difference_pair":{"matrix":pair.tolist(),"determinant":int(pair.det()),"smith":snf(pair),"rank_mod2":rank_mod(pair,2)}}


def lambda_checks():
    lam,beta,gamma,c,a,b,d,e=S.symbols("lambda beta gamma c a b d e")
    shear=S.Matrix([[1,c],[0,1]])
    assert S.Matrix([[lam,beta]])*shear==S.Matrix([[lam,beta+lam*c]])
    first=lam*a*d+gamma*a*e+beta*b*d; second=b*e
    assert zeros(lam*first+beta*gamma*second-(lam*a+beta*b)*(lam*d+gamma*e))
    assert shear.det()==1
    return {"shear_identity":"u_beta o phi_c = u_(beta+lambda*c); phi_c(a,b)=(a+c*b,b)",
            "split_product_identity":"E_beta *_lambda E_gamma = E_(beta*gamma), with product coordinates (lambda*a*d+gamma*a*e+beta*b*d,b*e)",
            "lambda1_beta0_witness":"phi_1:E_1 -> E_0 preserves injection, quotient, and u; determinant 1",
            "lambda2_beta3_witness":"phi_1:E_3 -> E_1 over Z preserves injection, quotient, and u; 3 is not a unit in Z",
            "conditional_unit_criterion":"For the usual extension morphisms and the stated product/unit, beta mod(lambda) is a unit; equivalently (beta,lambda)=k."}


def hashes():
    paths=sorted((PACKAGE/"pages").glob("*.tex"))+[PACKAGE/"MPL_83_178-222_transcription.tex"]
    return {str(p.relative_to(PACKAGE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}


if __name__=="__main__":
    before=hashes()
    output={"created_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),"sympy_version":S.__version__,
            "triple":triple_checks(),"four":four_checks(),"cube":cube_checks(),"lambda":lambda_checks()}
    after=hashes();assert before==after
    output["frozen_tex_unchanged_during_verification"]=True
    output["frozen_tex_sha256"]=before
    target=HERE/"algebra_verification.json"
    target.write_text(json.dumps(output,indent=2,default=str)+"\n",encoding="utf-8")
    print(json.dumps({"all_assertions_passed":True,"output":str(target),"frozen_tex_unchanged":True},indent=2))
