#!/usr/bin/env python3
"""Mod3 image of the M3 evaluation map at17, retaining unknown degree4 data.

Matrices are the certified exact M3 lattice matrices of a_degree3_lattice.py.
The coefficient action over K0 is abelian. Its augmentation ideal has fourth
power zero modulo3. Therefore evaluation modulo3 sees the arithmetic word
only through degree4. A31 gives its entire degree3 term; the three degree4
coefficients are left arbitrary and the actual image is compared for all.
"""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
data = json.loads((HERE/'a_degree3_matrices.json').read_text())
U, V, C = [np.array(a, dtype=np.int64) % 3 for a in data['M3_Galois_matrices']]
I = np.eye(330, dtype=np.int64)


def mm(a, b):
    return a @ b % 3


def columns(matrix):
    original = matrix % 3
    mat = original.copy()
    rank, pivots = 0, []
    for col in range(mat.shape[1]):
        choices = np.flatnonzero(mat[rank:, col])
        if not len(choices):
            continue
        rr = rank + int(choices[0])
        mat[[rank, rr], :] = mat[[rr, rank], :]
        mat[rank, :] = mat[rank, :] * int(mat[rank, col]) % 3
        factors = mat[:, col].copy()
        factors[rank] = 0
        mat = (mat - factors[:, None]*mat[rank, :][None, :]) % 3
        pivots.append(col)
        rank += 1
        if rank == mat.shape[0]:
            break
    return original[:, pivots], pivots


def rank(matrix):
    return len(columns(matrix)[1])


def main():
    assert np.array_equal(mm(mm(U, U), U), I)
    assert np.array_equal(mm(mm(V, V), V), I)
    assert np.array_equal(mm(U, V), mm(V, U))
    M, N = mm(U, V), mm(V, mm(U, U))
    A, B = (M-I) % 3, (N-I) % 3
    assert np.array_equal(mm(C, M), mm(M, C))
    assert np.array_equal(mm(mm(C, N), C), mm(N, N))
    A2, B2 = mm(A, A), mm(B, B)
    A3, B3 = mm(A2, A), mm(B2, B)
    assert not np.any(A3) and not np.any(B3)
    assert not np.any(mm(A2, B2))
    plus, _ = columns((I+C) % 3)
    minus, _ = columns((I-mm(N, C)) % 3)
    assert plus.shape[1] == 164 and minus.shape[1] == 166
    assert not np.any(mm((mm(N, C)+I) % 3, minus))
    Pplus = (2*(I+C)) % 3
    # phi=m^6*[n,[n,m]] moduloD4. Cocycle values are v_m,v_n.
    E0 = np.hstack((mm((2*A2+B2) % 3, plus), -mm(mm(A, B), minus))) % 3
    # K1=[m,[m,[m,n]]], K2=[n,[m,[m,n]]], K3=[n,[n,[m,n]]].
    K1 = np.hstack((-mm(mm(A2, B), plus), mm(A3, minus))) % 3
    K2 = np.hstack((-mm(mm(A, B2), plus), mm(mm(A2, B), minus))) % 3
    K3 = np.hstack((-mm(B3, plus), mm(mm(A, B2), minus))) % 3
    E0, K1, K2, K3 = [mm(Pplus, e) for e in (E0, K1, K2, K3)]
    print('Module rank330; local mod3 target is the c-fixed space of dimension164.')
    print('Normalized source parameters: v_m dimension164, v_n dimension166.')
    print('Verified augmentation ideal fourth power zero modulo3.')
    print('Ranks of projected degree4 changes K1,K2,K3:', [rank(k) for k in (K1,K2,K3)])
    base_image, _ = columns(E0)
    print('Rank of degree3 evaluation:', base_image.shape[1])
    for coefficient in range(3):
        evaluated = (E0+coefficient*K2) % 3
        image, pivots = columns(evaluated)
        union_rank = rank(np.hstack((base_image, image)))
        print('Unknown invariant degree4 coefficient', coefficient,
              'evaluation rank', image.shape[1], 'union with coefficient0 rank', union_rank,
              'local cokernel mod3 dimension', 164-image.shape[1])
    print('Rank of all projected evaluations together:', rank(np.hstack((E0,K1,K2,K3))))
    chosen = next(j for j in range(plus.shape[1])
                  if np.any(E0[:,j]) and not np.any(K2[:,j]))
    plus_original, plus_indices = columns((I+C) % 3)
    source_index = plus_indices[chosen]
    # Frob_(17²)=Frob_17², so on the c-fixed local quotient its cocycle
    # value is twice the Frob17 value.  Divide by2, which equals2 mod3.
    local_value = (2*E0[:,chosen]) % 3
    assert np.array_equal(mm(C, local_value[:,None])[:,0], local_value)
    print('Explicit global cocycle: value at m is (1+c)*e_j, value at n is0.')
    print('Zero-based index j:', source_index, 'degree3 basis datum:', data['basis'][source_index])
    sparse_value = [[int(i), int(local_value[i])] for i in np.flatnonzero(local_value)]
    print('Nonzero coordinates of its local Frob17 class modulo3:', sparse_value)

    def addpoly(target, source, factor=1):
        for word, value in source.items():
            target[word] = (target.get(word,0)+factor*value) % 3
        return {word:value for word,value in target.items() if value}

    def productpoly(left,right):
        out = {}
        for a,x in left.items():
            for b,y in right.items():
                out[a+b] = (out.get(a+b,0)+x*y) % 3
        return {word:value for word,value in out.items() if value}

    def bracket(left,right):
        return addpoly(productpoly(left,right),productpoly(right,left),-1)

    polynomial = {}
    for index, value in sparse_value:
        mu, ii = data['basis'][index]
        jj = mu[0]
        remainder = list(mu)
        remainder.remove(ii)
        remainder.remove(jj)
        kk = remainder[0]
        hall = bracket(bracket({(ii,):1},{(jj,):1}),{(kk,):1})
        polynomial = addpoly(polynomial,hall,value)
    eO = {(j,):2 for j in range(8)}
    obstruction = bracket(polynomial,eO)
    assert obstruction
    # Verify the minus sign under actual complex conjugation on V.
    vc = np.array(json.loads((HERE/'a_k_lattice.out').read_text())['V_generator_matrices'][2],dtype=np.int64)%3
    images = [{(i,):int(vc[i,j]) for i in np.flatnonzero(vc[:,j])} for j in range(10)]
    conjugate = {}
    for word, value in obstruction.items():
        expanded = {():value}
        for letter in word:
            expanded = productpoly(expanded,images[letter])
        conjugate = addpoly(conjugate,expanded)
    assert conjugate == {word:(-value)%3 for word,value in obstruction.items()}
    print('Degree4 obstruction [local_value,e_O]: nonzero tensor words',len(obstruction))
    print('First nonzero word certificate:',sorted(obstruction.items())[0])
    print('Verified c(obstruction)=-obstruction; Frob17-17 is c+1 modulo3 and kills the other eigenspace.')
    artifact = {'source_index':source_index,'source_basis':data['basis'][source_index],
                'local_frobenius_mod3':sparse_value,
                'degree4_obstruction_mod3':[[list(word),int(value)] for word,value in sorted(obstruction.items())],
                'evaluation_image_mod3_basis':base_image.tolist()}
    (HERE/'a_frobenius17_eval_m3.json').write_text(json.dumps(artifact,indent=2)+'\n')
    print('PASS')


if __name__ == '__main__':
    main()
