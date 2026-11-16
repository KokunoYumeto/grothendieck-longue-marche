"""Exact free-group Nielsen and Fox input for C'=F5 and D4.

C=<t0,t1,t2 | ti^2=1>; the eight-vertex cube is the C' cover.
Every assertion below is a freely reduced WORD assertion unless explicitly
labelled abelian.  No finite matrix equality replaces a source relation.
"""
from pathlib import Path
from collections import defaultdict
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'records'
OUT.mkdir(exist_ok=True)

def creduce(w):
    r=[]
    for x in w:
        if r and r[-1]==x:r.pop()
        else:r.append(x)
    return tuple(r)
def freduce(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def finv(w):return tuple(-x for x in reversed(w))
def csub(w,images):return creduce(x for i in w for x in images[i])
def fsub(w,images):
    return freduce(x for i in w for x in(images[i-1]if i>0 else finv(images[-i-1])))
def ccompose(a,b):return tuple(csub(w,a)for w in b)
def fcompose(a,b):return tuple(fsub(w,a)for w in b)
cid=((0,),(1,),(2,));fid=tuple((i,)for i in range(1,6))

sections={v:tuple(i for i in range(3)if v&(1<<i))for v in range(8)}
tree=set()
for word in sections.values():
    v=0
    for i in word:
        w=v^(1<<i);tree.add((min(v,w),max(v,w)));v=w
edges=sorted({(min(v,v^(1<<i)),max(v,v^(1<<i)))for v in range(8)for i in range(3)})
chords=[e for e in edges if e not in tree];ci={e:j+1 for j,e in enumerate(chords)}
basis=[]
for v,w in chords:
    letter=(v^w).bit_length()-1
    basis.append(creduce(sections[v]+(letter,)+tuple(reversed(sections[w]))))
assert len(basis)==5

def schreier(word):
    v=0;out=[]
    for letter in word:
        w=v^(1<<letter);edge=(min(v,w),max(v,w))
        if edge in ci:out.append(ci[edge]if v<w else-ci[edge])
        v=w
    assert v==0,'word must belong to C prime'
    return freduce(out)
def expand(word):
    return creduce(x for i in word for x in(basis[i-1]if i>0 else tuple(reversed(basis[-i-1]))))
assert tuple(schreier(w)for w in basis)==fid

cimages={
 'a':((0,1,0),(0,),(2,)),
 'a_inv':((1,),(1,0,1),(2,)),
 'b':((2,),(1,),(2,0,2)),
 'b_inv':((0,2,0),(1,),(0,)),
 'c':((1,),(1,0,1),(1,0,2,0,1)),
 'c_inv':((0,1,0),(0,),(0,1,2,1,0)),
}
for n in ('a','b','c'):
    assert ccompose(cimages[n],cimages[n+'_inv'])==cid
    assert ccompose(cimages[n+'_inv'],cimages[n])==cid
fimages={n:tuple(schreier(csub(w,im))for w in basis)for n,im in cimages.items()}
for n,im in fimages.items():
    assert all(expand(v)==csub(w,cimages[n])for v,w in zip(im,basis))
for n in ('a','b','c'):
    assert fcompose(fimages[n],fimages[n+'_inv'])==fid
    assert fcompose(fimages[n+'_inv'],fimages[n])==fid

def product(names,images,identity,compose):
    out=identity
    for n in names:out=compose(out,images[n])
    return out
rels=[(('a','b','a'),('b','a','b')),
      (('b','c','b'),('c','b','c')),
      (('a','c'),('c','a')),
      (('a','b','c')*4,())]
for lhs,rhs in rels:
    assert product(lhs,cimages,cid,ccompose)==product(rhs,cimages,cid,ccompose)
    assert product(lhs,fimages,fid,fcompose)==product(rhs,fimages,fid,fcompose)

def ab(w):
    v=[0]*5
    for i in w:v[abs(i)-1]+=1 if i>0 else-1
    return tuple(v)
def mat(images):
    cols=[ab(w)for w in images]
    return [[cols[j][i]for j in range(5)]for i in range(5)]
def mm(a,b):return[[sum(a[i][k]*b[k][j]for k in range(5))for j in range(5)]for i in range(5)]
I=[[int(i==j)for j in range(5)]for i in range(5)]
for n in('a','b','c'):assert mm(mat(fimages[n]),mat(fimages[n+'_inv']))==I

def fox(w):
    """Noncommutative left Fox derivatives: row i is d(w)/d(q_i)."""
    d=[defaultdict(int)for _ in range(5)];prefix=()
    for letter in w:
        i=abs(letter)-1
        if letter>0:d[i][prefix]+=1;prefix=freduce(prefix+(letter,))
        else:
            prefix=freduce(prefix+(letter,));d[i][prefix]-=1
    return [{k:v for k,v in row.items()if v}for row in d]
def abfox(w):
    dd=[]
    for row in fox(w):
        r=defaultdict(int)
        for mon,c in row.items():r[ab(mon)]+=c
        dd.append({k:v for k,v in r.items()if v})
    return dd
def group_ring_mul_left_q(poly,i):
    out=defaultdict(int)
    for word,c in poly.items():out[freduce(word+(i,))]+=c
    return out
for im in fimages.values():
    for w in im:
        # Exact fundamental formula w-1=sum_i (dw/dqi)(qi-1).
        total=defaultdict(int)
        for i,row in enumerate(fox(w),1):
            for mon,c in row.items():
                total[freduce(mon+(i,))]+=c;total[mon]-=c
        total={k:v for k,v in total.items()if v}
        expected=defaultdict(int);expected[w]+=1;expected[()]-=1
        assert total=={k:v for k,v in expected.items()if v}

def terms(poly):return[{'coefficient':v,'monomial':list(k)}for k,v in sorted(poly.items())]
w0=(1,0,2);xi1=(1,0);xi2=(2,0)
assert creduce(w0+w0)==creduce(xi1+xi2+tuple(reversed(xi1))+tuple(reversed(xi2)))
cusp_reps=((),xi1,xi2,creduce(xi1+xi2))
cusp_words=[schreier(creduce(r+w0+w0+tuple(reversed(r))))for r in cusp_reps]
assert all(sum(ab(w)[i]for w in cusp_words)==0 for i in range(5))
output={
 'involution_letters':'0,1,2 denote t0,t1,t2; consecutive equal letters cancel',
 'free_letters':'1,...,5 denote q1,...,q5; negative integers denote inverses',
 'basis_in_involutions':[list(w)for w in basis],
 'cube_tree_edges':sorted(tree),'cube_chords':chords,
 'involution_images':{n:[list(w)for w in im]for n,im in cimages.items()},
 'free_group_images':{n:[list(w)for w in im]for n,im in fimages.items()},
 'abelianization_matrices':{n:mat(im)for n,im in fimages.items()},
 'positive_cusp_source_word':list(w0+w0),
 'positive_cusp_conjugating_representatives':[list(r)for r in cusp_reps],
 'positive_cusp_free_words':[list(w)for w in cusp_words],
 'positive_cusp_abelian_vectors':[list(ab(w))for w in cusp_words],
 'fox_noncommutative':{n:[[terms(fox(im[j])[i])for j in range(5)]for i in range(5)]for n,im in fimages.items()},
 'fox_abelianized':{n:[[terms(abfox(im[j])[i])for j in range(5)]for i in range(5)]for n,im in fimages.items()},
 'all_six_inverse_word_identities_checked':True,
 'all_four_L_relators_checked_in_Aut_C_and_Aut_F5':True,
 'all_thirty_exact_free_group_Fox_fundamental_identities_checked':True,
 'fox_orientation':'Rows are derivative variables; columns are generator images. Entries are LEFT group-ring coefficients on target oriented edges.',
 'character_transport':'For source row character chi mod4, target eta=chi*T_alpha_inverse mod4; block matrix is J_alpha evaluated at eta.',
 'boundary_identity':'d_eta*J_alpha(eta)=d_chi, where d_chi=(i^chi_j-1)_j.',
 'chain_rule':'For abelianized Fox matrices, J_(alpha beta)(eta)=J_alpha(eta)*J_beta(eta*T_alpha), with alpha beta=alpha composed with beta.',
 'inner_D4_formula':'For d in D4, J_Ad(d)(chi)=I-v_d(chi)*d_chi. It is identity on ker d_chi but retains v_d on the full chain block when chi is nontrivial.',
 'trivial_character_scope':'At chi=0 the chain boundary is zero and inner translations are invisible; retain the old affine rank5 factor separately.'
}
(OUT/'f5_nielsen_fox.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:output[k]for k in('basis_in_involutions','free_group_images','abelianization_matrices','all_six_inverse_word_identities_checked','all_four_L_relators_checked_in_Aut_C_and_Aut_F5','all_thirty_exact_free_group_Fox_fundamental_identities_checked','character_transport','boundary_identity','chain_rule','inner_D4_formula','trivial_character_scope')},indent=2))
