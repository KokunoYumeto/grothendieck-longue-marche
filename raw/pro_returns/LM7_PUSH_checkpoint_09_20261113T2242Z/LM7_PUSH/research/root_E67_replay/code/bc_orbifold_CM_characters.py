#!/usr/bin/env python3
"""Two actual finite triangle-Tate quotients and the Mordell sign.

This is a new exploratory certificate after frozen E64.  The theorem it
checks is the positive sign of the original multiplier-one Mordell action.
The optional saved-word values are finite probes, not full-GT realizations.
"""
from pathlib import Path
from collections import deque
import hashlib
import itertools
import json

from bc_hyperelliptic_sewing import eye, mm, mp, inv


HERE = Path(__file__).resolve().parent
P = 3
I = eye(2)
R = ((0, 1), (2, 1))
S = ((0, 1), (2, 0))


def modmat(a):
    return tuple(tuple(x % P for x in row) for row in a)


def mv(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(2)) % P for i in range(2))


def add(a, b):
    return tuple((x+y) % P for x, y in zip(a, b))


def neg(v):
    return tuple(-x % P for x in v)


def det(a):
    return (a[0][0]*a[1][1] - a[0][1]*a[1][0]) % P


class Affine:
    def __init__(self, matrix, order, X, Y, Z):
        self.matrix, self.order = matrix, order
        self.powers = [modmat(mp(matrix, i)) for i in range(order)]
        assert modmat(mp(matrix, order)) == I
        self.one = ((0, 0), 0)
        self.X, self.Y, self.Z = X, Y, Z
        self.all = tuple((v, i) for v in itertools.product(range(P), repeat=2)
                         for i in range(order))
        assert self.mul(self.mul(X, Y), Z) == self.one

    def mul(self, a, b):
        return add(a[0], mv(self.powers[a[1]], b[0])), (a[1]+b[1]) % self.order

    def inv(self, a):
        return neg(mv(self.powers[-a[1] % self.order], a[0])), -a[1] % self.order

    def power(self, a, n):
        if n < 0:
            a, n = self.inv(a), -n
        out = self.one
        for _ in range(n):
            out = self.mul(out, a)
        return out

    def conj(self, a, b):
        return self.mul(self.mul(a, b), self.inv(a))

    def comm(self, a, b):
        return self.mul(self.conj(a, b), self.inv(b))

    def word(self, word, X=None, Y=None):
        X = self.X if X is None else X
        Y = self.Y if Y is None else Y
        g = {1:X, 2:Y, -1:self.inv(X), -2:self.inv(Y)}
        out = self.one
        for letter in word:
            out = self.mul(out, g[letter])
        return out

    def closure(self, generators):
        generators = list(generators)
        seen = {self.one}
        todo = deque([self.one])
        while todo:
            a = todo.popleft()
            for b in generators:
                c = self.mul(a, b)
                if c not in seen:
                    seen.add(c); todo.append(c)
        return seen

    def check_pair_map(self, Ximage, Yimage):
        mapping = {self.one:self.one}
        todo = deque([self.one])
        pairs = [(self.X, Ximage), (self.Y, Yimage)]
        while todo:
            g = todo.popleft()
            for a, b in pairs:
                ga = self.mul(g, a); vb = self.mul(mapping[g], b)
                if ga in mapping and mapping[ga] != vb:
                    return False, None
                if ga not in mapping:
                    mapping[ga] = vb; todo.append(ga)
        assert len(mapping) == len(self.all)
        return len(set(mapping.values())) == len(self.all), mapping


def centralizer(matrix):
    result = []
    for entries in itertools.product(range(P), repeat=4):
        A = (entries[:2], entries[2:])
        if det(A) == 1 and modmat(mm(A, matrix)) == modmat(mm(matrix, A)):
            result.append(A)
    return result


def main():
    M = Affine(R, 6, ((0,0),1), ((1,0),3), ((1,0),2))
    G = Affine(S, 4, ((1,0),1), ((0,2),2), ((0,0),1))
    assert len(M.closure([M.X,M.Y])) == 54
    assert len(G.closure([G.X,G.Y])) == 36
    assert M.power(M.Y,2)==M.power(M.Z,3)==M.one
    assert G.power(G.Y,2)==G.power(G.Z,4)==G.one
    assert M.mul(M.Z,M.power(M.X,-2)) == ((1,0),0)
    assert M.mul(M.power(M.X,4),M.Z) == ((0,1),0)
    assert G.mul(G.power(G.X,2),G.Y) == ((1,0),0)
    assert G.mul(G.power(G.Z,2),G.Y) == ((0,1),0)

    vectors = list(itertools.product(range(P),repeat=2))
    R2 = M.powers[2]
    rimage = {add(v, neg(mv(R2,v))) for v in vectors}
    assert rimage == {(0,0),(1,2),(2,1)}
    mordell = []
    for B in centralizer(R):
        ze = mv(B,(1,0))
        candidates = [v for v in vectors if M.conj((v,0),M.Z)==(ze,2)]
        sign = 0 if mv(B,(1,2))==(1,2) else 1
        assert bool(candidates) == (sign == 0)
        mordell.append({'B':B,'sign':sign,'z_translation_conjugators':candidates,
                        'admitted_by_exact_z_frame':bool(candidates)})
    assert sum(r['admitted_by_exact_z_frame'] for r in mordell)==3

    gaussian = []
    for B in centralizer(S):
        a = add((1,0),neg(mv(B,(1,0))))
        zimage = (a,1)
        yimage = G.inv(G.mul(zimage,G.X))
        ok, mapping = G.check_pair_map(G.X,yimage)
        assert ok and mapping[G.Z]==zimage
        Bactual = tuple(zip(mapping[((1,0),0)][0],mapping[((0,1),0)][0]))
        assert Bactual == B
        yframes=[v for v in vectors if G.conj((v,0),G.Y)==yimage]
        zframes=[v for v in vectors if G.conj((v,0),G.Z)==zimage]
        assert len(yframes)==len(zframes)==1
        vxy = neg(yframes[0])
        assert mv(B,(1,0))==add((1,0),neg(vxy))
        bit=int(B[1][0]!=0)
        assert bit==(vxy[1]*vxy[1])%P
        gaussian.append({'B':B,'bit':bit,'actual_y_image':yimage,
                         'actual_z_image':zimage,'y_frame':yframes[0],
                         'z_frame':zframes[0],'f_xy_translation':vxy,
                         'automorphism_permutation':[G.all.index(mapping[g]) for g in G.all]})
    assert len(gaussian)==4 and sum(r['bit'] for r in gaussian)==2

    # Exact old-source kernel images, retaining literal commutator preimages.
    input_path=HERE/'bc_cm_literal_words.json'
    data=json.loads(input_path.read_text())
    nwords=[tuple(w) for w in data['N_B_basis_in_F']]
    nM=[M.word(w) for w in nwords]; nG=[G.word(w) for w in nwords]
    imageM=M.closure(nM); imageG=G.closure(nG)
    comm_records=[]
    joint={(M.one,G.one):()}
    todo=deque([(M.one,G.one)])
    gens=[]
    for i in range(len(nwords)):
        for j in range(i+1,len(nwords)):
            value=(M.comm(nM[i],nM[j]),G.comm(nG[i],nG[j]))
            if value==(M.one,G.one):continue
            gens.append((value,(i,j)))
    while todo:
        v=todo.popleft()
        for w,ij in gens:
            z=(M.mul(v[0],w[0]),G.mul(v[1],w[1]))
            if z not in joint:
                joint[z]=joint[v]+(ij,);todo.append(z)
    derivedM=M.closure(M.comm(a,b) for a in imageM for b in imageM)
    derivedG=G.closure(G.comm(a,b) for a in imageG for b in imageG)
    assert len(derivedM)==3 and len(derivedG)==9
    assert len(joint)==len(derivedM)*len(derivedG)==27
    qG_only=sorted(g for m,g in joint if m==M.one)
    for value in qG_only:
        ij_pairs=joint[(M.one,value)]
        word=()
        for i,j in ij_pairs:
            word+=nwords[i]+nwords[j]+inv(nwords[i])+inv(nwords[j])
        assert M.word(word)==M.one and G.word(word)==value
        assert all(sum(1 if k==i else -1 if k==-i else 0 for k in word)==0
                   for i in (1,2))
        comm_records.append({'Gaussian_image':value,'commutator_pairs':ij_pairs,
                             'literal_F_word':word})

    probes=[]
    for index,record in enumerate(data['CM_words_in_F']):
        word=record['word']; outcomes={}
        for label,model in [('Mordell',M),('Gaussian',G)]:
            fxy=model.word(word)
            fyx=model.word(word,model.Y,model.X)
            fzx=model.word(word,model.Z,model.X)
            fxz=model.word(word,model.X,model.Z)
            Yimage=model.mul(model.mul(fyx,model.Y),fxy)
            Zimage=model.mul(model.mul(fzx,model.Z),fxz)
            ok,mapping=model.check_pair_map(model.X,Yimage)
            exact=ok and mapping[model.Z]==Zimage
            outcomes[label]={'f_xy':fxy,'two_cycle':fyx==model.inv(fxy),
                             'pair_induces_automorphism':ok,
                             'full_three_generator_comparison':exact}
            if exact:
                B=tuple(zip(mapping[((1,0),0)][0],mapping[((0,1),0)][0]))
                outcomes[label]['B']=B
                outcomes[label]['determinant_mod3']=det(B)
                outcomes[label]['also_preserves_primitive_cusp_commutator']=det(B)==1
        probes.append({'index':index,'extra_CM_coset':record['extra_CM_coset'],
                       'literal_word_scope':'fixed E1 word, not an asserted full GT pair',
                       'outcomes':outcomes})

    output=dict(status='PASS_EXACT_ORBIFOLD_CM_QUOTIENTS_AND_POSITIVE_MORDELL_SIGN',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                input_sha256=hashlib.sha256(input_path.read_bytes()).hexdigest(),
                group_orders={'Mordell':54,'Gaussian':36},
                literal_generators={'Mordell':{'x':M.X,'y':M.Y,'z':M.Z,'rotation':R},
                                    'Gaussian':{'x':G.X,'y':G.Y,'z':G.Z,'rotation':S}},
                Mordell_image_of_one_minus_R_squared=sorted(rimage),
                Mordell_exact_frame_table=mordell,
                Gaussian_exact_frame_table=gaussian,
                old_source_N_image_orders={'Mordell':len(imageM),'Gaussian':len(imageG)},
                old_source_N_derived_projection_orders={'Mordell':len(derivedM),'Gaussian':len(derivedG)},
                old_source_N_prime_joint_order=len(joint),
                Gaussian_image_of_N_prime_intersect_Mordell_kernel_order=len(qG_only),
                exact_commutator_preimages=comm_records,
                old_E1_literal_word_probes=probes,
                scope='The universal positive Mordell orbifold sign and explicit '
                      'finite source maps are proved. Gaussian finite automorphisms '
                      'and fixed-word probes are not promoted to whole GT realizations.')
    (HERE/'bc_orbifold_CM_characters.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in
         ['status','group_orders','old_source_N_image_orders','old_source_N_prime_joint_order',
          'Gaussian_image_of_N_prime_intersect_Mordell_kernel_order','source_sha256']},indent=2))


if __name__=='__main__':main()
