#!/usr/bin/env python3
"""All nine points of every degree-six correction plane, including generation."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix,InducedSix
from de_ferrari_degree5_lift import chunk_trie
from de_ferrari_mod9_lift import Span,rref
import de_ferrari_class2_model as old

here=Path(__file__).resolve().parent

def schreier_logs(H,generators):
    low=[tuple(int(t) for t in H.project(g)) for g in generators]
    seen={old.one:0};queue=[old.one];lifts=[H.one];inverses=[H.one];columns=[]
    for i,q in enumerate(queue):
        for g,h in zip(generators,low):
            qn=old.mul(q,h);image=H.mul(lifts[i],g);j=seen.get(qn)
            if j is None:
                seen[qn]=len(queue);queue.append(qn);lifts.append(image);inverses.append(H.inv(image))
            else:columns.append(H.log_kernel(H.mul(image,inverses[j])))
    assert len(queue)==648
    return np.array(columns,dtype=np.int64).T

def main():
    start=time.time()
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=CombinedSix();W=InducedSix(H,d);N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
    target_data=np.load(here/'de_ferrari_degree6_generation_certificate.npz')
    M=target_data['target_kernel_Lie_basis'];ambient_derived=target_data['target_kernel_commutator_basis']
    target=Span(M.shape[0])
    for v in M.T:assert target.add(v,[])
    piv=sorted(target.rows);rank=M.shape[1];R,p=rref(np.column_stack((M[piv],np.eye(rank,dtype=np.int64))))
    assert p[:rank]==list(range(rank)) and np.array_equal(R[:,:rank],np.eye(rank,dtype=np.int64))
    left=R[:,rank:]
    def coordinates(A):
        C=left@A[piv]%3;assert np.array_equal(M@C%3,A%3);return C
    D=coordinates(ambient_derived)
    data=json.loads(here.joinpath('de_ferrari_degree6_lift.json').read_text())['records']
    origins=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
    CM=np.load(here/'de_ferrari_degree6_kernel_certificate.npz')['F_prime_top_kernel_basis']
    s,rr=W.letters[0],W.letters[1];t=W.mul(s,rr);x=W.word(d['xword']);u=W.word([-1,0]);v=W.word([0,-1])
    center3=H.power(H.mul(H.a,H.b),3);center4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    rows=[];certificates={'target_basis':M,'target_derived_basis':ambient_derived}
    for rec,origin in zip(data,origins):
        ix=rec['certificate_index'];witness=rec['chosen_witness'];K=np.array(witness['homogeneous_top_correction'],dtype=np.int64)
        assert K.shape==(6,2)
        beta=W.word(origin['base_beta_word_B'])
        S=W.mul(W.conj(beta,s),W.word(witness['literal_B_old_correction_word']+witness['literal_B_top_correction_word']))
        R=W.mul(W.inv(S),t);assert W.equal(W.mul(S,R),t)
        xg=W.power(x,origin['integral_cusp_gauge']);f0=W.mul(s,W.conj(xg,S));vals0=f0[1][W.root]
        images0=H.braid_images(vals0)
        assert all(np.array_equal(a,H.decode(b)) for a,b in zip(images0,witness['actual_braid_images']))
        def point(a,b):
            delta=W.element(CM@K@np.array([a,b],dtype=np.int64)%3)
            SS=W.mul(S,delta);RR=W.mul(W.inv(delta),R)
            assert W.equal(W.mul(SS,RR),t)
            assert W.equal(W.power(SS,2),W.one) and W.equal(W.power(RR,3),W.one)
            ff=W.mul(s,W.conj(xg,SS));fi=W.inv(ff)
            hex1=W.mul(W.mul(W.mul(W.mul(u,fi),v),ff),W.inv(W.mul(fi,rr)))
            hex2=W.mul(W.mul(W.mul(W.mul(fi,v),ff),u),W.inv(W.mul(W.mul(v,u),ff)))
            assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
            vals=ff[1][W.root];assert np.array_equal(H.pentagon(vals),H.one)
            images=H.braid_images(vals);H.check_braids(images)
            aa,bb,cc=images
            assert np.array_equal(H.power(H.mul(aa,bb),3),center3)
            assert np.array_equal(H.power(H.mul(H.mul(aa,bb),cc),4),center4)
            return images
        L0=schreier_logs(H,point(0,0));L1=schreier_logs(H,point(1,0));L2=schreier_logs(H,point(0,1))
        d1=(L1-L0)%3;d2=(L2-L0)%3
        assert np.array_equal(schreier_logs(H,point(1,1)),(L0+d1+d2)%3)
        for delta in (d1,d2):
            for vector in delta.T:
                # Differences lie in the central top layer of the E.18 kernel.
                H.kernel_vector(H.exp_kernel(vector))
        C0,C1,C2=coordinates(L0),coordinates(d1),coordinates(d2)
        S0=Span(rank)
        for c in C0.T:S0.add(c,[])
        derived=Span(rank)
        for a in S0.basis:
            ea=H.exp_kernel(M@a%3)
            for b in S0.basis:derived.add(coordinates(H.log_kernel(H.comm(ea,H.exp_kernel(M@b%3)))),[])
        assert len(derived.basis)==ambient_derived.shape[1]
        for c in D.T:derived.coordinates(c)
        points=[]
        for a in range(3):
            for b in range(3):
                point(a,b)
                matrix=np.column_stack(((C0+a*C1+b*C2)%3,derived.matrix()))
                newrank=len(rref(matrix)[1]);assert newrank==rank
                points.append({'homogeneous_parameters':[a,b],'four_strand_kernel_rank':newrank,
                    'full_hexagons_pentagon_braids_and_full_twists_verified':True,
                    'source_surjectivity_by_exact_Frattini_quotient':True})
        certificates[f'Schreier_constant_{ix}']=C0;certificates[f'Schreier_direction1_{ix}']=C1
        certificates[f'Schreier_direction2_{ix}']=C2;certificates[f'actual_Schreier_derived_basis_{ix}']=derived.matrix()
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],'all_nine_points':points}
        rows.append(row);print(json.dumps({'certificate_index':ix,'all_nine_generation_ranks':[r['four_strand_kernel_rank'] for r in points]}),flush=True)
    out={'records':rows,'complete_planes_tested':len(rows),'total_actual_points_tested':9*len(rows),
        'target_kernel_Lie_dimension':rank,'all_simultaneous_corrections_retained':True,
        'elapsed_seconds':round(time.time()-start,3),
        'scope':'Every point of every degree-six homogeneous correction plane: full relations and four-strand generation; source generation by the exact Frattini comparison.'}
    here.joinpath('de_ferrari_degree6_wholeplanes.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree6_wholeplanes_certificate.npz',**certificates)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
