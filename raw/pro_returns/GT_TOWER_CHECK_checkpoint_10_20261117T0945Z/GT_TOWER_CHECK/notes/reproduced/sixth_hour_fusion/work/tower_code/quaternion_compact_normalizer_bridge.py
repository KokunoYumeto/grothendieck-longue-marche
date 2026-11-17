#!/usr/bin/env python3
"""Literal18-to6 bridge for every ordinary modular/deck kernel word."""
import numpy as np,json
from pathlib import Path
import translation_quaternion_homology as T
D=Path(__file__).parent
C=np.load(D/'modular_quaternion_compact_setup.npz');F=np.load(D/'modular_quaternion_compact_faithful.npz');J=np.load(D/'quaternion_compact_normalizer_joint.npz')
R=json.loads((D/'quaternion_compact_normalizer_joint.json').read_text());P=json.loads((D/'translation_cover_basis.json').read_text())
# Actual four automorphisms on the original rank73 free cover.
gwords=[tuple(tuple(w) for w in g) for g in P['normalizer_automorphisms']]+T.H
G73=[np.stack([T.rewrite(T.sub(w,g),True) for w in T.basis],axis=1)%3 for g in gwords]
# Build precisely the compact12 primitive basis used in the joint producer.
W=F['T_image_basis'];_,wr=T.rref(W.T);Wi=T.minv(W[wr]);G14=C['actual_generator_matrices'];G12=[]
for g in G14:
 A=Wi@(g@W%3)[wr]%3;assert np.array_equal(W@A%3,g@W%3);G12.append(A)
def power(A,k):
 B=np.eye(len(A),dtype=np.int16)
 for _ in range(k):B=B@A%3
 return B
E=2*(np.eye(12,dtype=np.int16)+power(G12[2],9)+power(G12[3],9))%3
B,_=T.rref(E.T);B=B.T;_,br=T.rref(B.T);Bi=T.minv(B[br]);ModuleBasis=J['module6_basis'];MBi=T.minv(ModuleBasis)
Phi=MBi@Bi@(Wi@F['literal_T_homology_map'][wr]%3@T.CB%3)[br]%3
assert Phi.shape==(6,18) and len(T.rref(Phi)[0])==6
Form=np.load(D/'translation_quaternion_image.npz')['form'];I=np.eye(73,dtype=np.int16);matrices=[]
for k,w in enumerate(R['quaternion_automorphism_kernel_words']):
 A=I.copy()
 for j in w:A=A@(G73[j-1] if j>0 else T.minv(G73[-j-1]))%3
 M=T.restrict(A,T.CB,T.cbr,T.CBi)
 assert np.array_equal(M.T@Form%3@M%3,Form)
 assert np.array_equal(Phi@M%3,J['actual_generators'][k]@Phi%3)
 matrices.append(M)
print('PASS all96 actual18-to6 intertwining identities, with original Σ words and signed periods',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),ordinary_generator_matrices73=np.array(G73),source_kernel_matrices18=np.array(matrices),multiplicity_quotient_map=Phi)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Literal ordinary Σ generator action on T73, all96 source kernel words, and exact18-to6 quotient intertwining',
 'checked_source_words':len(matrices),'quotient_rank':6,'source_generator_words_K3':gwords,
 'period_basis_comparison':'q_down=J q_up J, J swaps the primitive upstairs handle basis(A=b³,B=a³) with(3a,3b)'} ,indent=2)+'\n')
