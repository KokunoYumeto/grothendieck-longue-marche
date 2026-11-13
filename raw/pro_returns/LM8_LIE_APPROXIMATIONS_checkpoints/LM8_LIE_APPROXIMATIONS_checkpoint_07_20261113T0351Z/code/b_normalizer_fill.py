"""Exact filling ranks on the point-pushing normalizer, and an extra-kernel witness."""
from b_lie_core import *

def nbasis(n):
    ds=special(3,n); pp=pointpush(n+1); pg=pointpush(1)
    C=column_matrix(pp,3,n+1)
    piv=C.T.rref()[1]; inv=C[list(piv),:].inv()
    blocks=[]
    for p in pg:
        A=column_matrix([dbracket(D,p) for D in ds],3,n+1)
        A=A-C*inv*A[list(piv),:]
        blocks.append(A)
    R=blocks[0].col_join(blocks[1])
    return [tuple(lincomb(v,[D[i] for D in ds]) for i in range(3))
            for v in R.nullspace()]

def main():
    out={'normalizer_filling':[]}
    for n in range(1,7):
        ds=nbasis(n)
        r=0 if n==1 else column_matrix([fill(D) for D in ds],2,n).rank()
        row={'degree':n,'normalizer':len(ds),'fill_rank':r,
             'kernel':len(ds)-r,'pointpush':len(pointpush(n))}
        assert row['kernel']==row['pointpush']
        out['normalizer_filling'].append(row);print(row,flush=True)
    x,y,z=map(gen,range(3));c=bracket(x,y)
    E=(bracket(bracket(y,c),x),add({},bracket(bracket(x,c),y),-1),{})
    assert not derivative(E,add(add(x,y),z))
    assert not any(fill(E))
    def erase_z(p):
        return {w:c for w,c in p.items() if 2 not in w}
    target=tuple(erase_z(p) for p in E[:2])
    assert any(target)
    rank=column_matrix(list(pointpush(3))+[E],3,3).rank()
    assert rank==len(pointpush(3))+1
    out['extra_kernel_witness']={'sum_defect_zero':True,'fill_x_zero':True,
        'fill_z_nonzero':True,'pointpush_rank':len(pointpush(3)),
        'rank_with_witness':rank}
    print(out['extra_kernel_witness'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))

if __name__=='__main__':main()
