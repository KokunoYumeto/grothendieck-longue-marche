#!/usr/bin/env python3
"""Complete K6 correction image in all six CM orbifold substitutions.

All correction generators have literal N_B'-word preimages.  The result
concerns the stated finite six-evaluation equations, not full GT lifts.
"""
from pathlib import Path
from collections import deque
import hashlib
import itertools
import json
import time

from bc_hyperelliptic_sewing import red, inv, eye
from bc_orbifold_CM_characters import Affine, R, S, mv, add, neg, centralizer


HERE=Path(__file__).resolve().parent


class Span:
    def __init__(self,dimension):
        self.dimension=dimension
        self.rows={}
        self.words={}

    def reduce(self,v):
        v=list(v); coeff={}
        for p,row in sorted(self.rows.items()):
            c=v[p]
            if c:
                coeff[p]=c
                v=[(a-c*b)%3 for a,b in zip(v,row)]
        return v,coeff

    def add(self,v,word):
        v,coeff=self.reduce(v)
        if not any(v):return False
        word=tuple(word)
        for p,c in coeff.items():word=red(word+inv(self.words[p])*c)
        p=next(i for i,x in enumerate(v) if x)
        if v[p]==2:
            v=[2*x%3 for x in v];word=red(word*2)
        self.rows[p]=tuple(v);self.words[p]=word
        return True

    def solution(self,v):
        residue,coeff=self.reduce(v)
        if any(residue):return None
        word=()
        for p,c in coeff.items():word=red(word+self.words[p]*c)
        return word,coeff


def main():
    start=time.monotonic()
    M=Affine(R,6,((0,0),1),((1,0),3),((1,0),2))
    G=Affine(S,4,((1,0),1),((0,2),2),((0,0),1))
    pairs=lambda T: [(T.X,T.Y),(T.Y,T.X),(T.Z,T.X),
                     (T.X,T.Z),(T.Y,T.Z),(T.Z,T.Y)]
    maps=[(T,a,b) for T in (M,G) for a,b in pairs(T)]
    def evaluate(word):return tuple(T.word(word,a,b) for T,a,b in maps)
    def vector(values):
        assert all(e==0 for v,e in values)
        return tuple(c for v,e in values for c in v)
    def vecword(word):return vector(evaluate(word))

    inp=HERE/'bc_cm_literal_words.json';data=json.loads(inp.read_text())
    nwords=[tuple(w) for w in data['N_B_basis_in_F']]
    nvalues=[evaluate(w) for w in nwords]
    assert len(nwords)==97
    # In all twelve actual factors every N-generator has sixth power one.
    # Their images are contained in a 3-group (Mordell) or V: C2 (Gaussian),
    # so every N-word has this same property, not just these generators.
    assert all(e%2==0 for values in nvalues for v,e in values)
    for values in nvalues:
        assert all(T.power(g,6)==T.one for (T,a,b),g in zip(maps,values))
    span=Span(24)
    allcomm=[]
    for i in range(97):
        for j in range(i):
            vals=tuple(T.comm(g,h) for (T,a,b),g,h in zip(maps,nvalues[i],nvalues[j]))
            v=vector(vals); allcomm.append(v)
            span.add(v,nwords[i]+nwords[j]+inv(nwords[i])+inv(nwords[j]))
    initial_rank=len(span.rows)
    changed=True; conjugation_additions=0
    while changed:
        changed=False
        for p,w in list(span.words.items()):
            v=span.rows[p]
            for i,nv in enumerate(nvalues):
                conjugated=tuple(c for block,((T,a,b),g) in enumerate(zip(maps,nv))
                                  for c in mv(T.powers[g[1]],v[2*block:2*block+2]))
                if span.add(conjugated,nwords[i]+w+inv(nwords[i])):
                    changed=True;conjugation_additions+=1
    assert all(not any(span.reduce(v)[0]) for v in allcomm)
    for p,v in span.rows.items():
        assert vecword(span.words[p])==v
        for nv in nvalues:
            conjugated=tuple(c for block,((T,a,b),g) in enumerate(zip(maps,nv))
                              for c in mv(T.powers[g[1]],v[2*block:2*block+2]))
            assert not any(span.reduce(conjugated)[0])

    # These are ranks of the specified maps, on the actual common domain.
    def rank(rows):
        s=Span(len(rows[0]))
        for row in rows:s.add(row,())
        return len(s.rows)
    mordell_rank=rank([v[:12] for v in span.rows.values()])
    gaussian_rank=rank([v[12:] for v in span.rows.values()])
    assert (mordell_rank,gaussian_rank,len(span.rows))==(3,6,9)

    def negv(v):return tuple(-x%3 for x in v)
    def six_values(hy,hz):
        vxy=negv(hy);vyz=negv(add(vxy,hz))
        six=(vxy,hy,hz,negv(hz),vyz,negv(vyz))
        assert all(add(six[i],six[j])==(0,0) for i,j in [(0,1),(2,3),(4,5)])
        assert add(add(six[2],six[4]),six[0])==(0,0)
        return tuple(c for v in six for c in v)

    targets=[]
    vv=list(itertools.product(range(3),repeat=2))
    for B in centralizer(S):
        zimage=(add((1,0),neg(mv(B,(1,0)))),1)
        yimage=G.inv(G.mul(zimage,G.X))
        hy=next(v for v in vv if G.conj((v,0),G.Y)==yimage)
        hz=next(v for v in vv if G.conj((v,0),G.Z)==zimage)
        target=six_values(hy,hz)
        ok,autom=G.check_pair_map(G.X,yimage)
        assert ok and autom[G.Z]==zimage
        targets.append((B,target,autom))

    # Exhaust every determinant-one Mordell action and every actual z-frame.
    # The frame ambiguity is exactly ker(I-R^2), and is retained.
    mordell_targets=[]
    for B in centralizer(R):
        yimage=(mv(B,(1,0)),3);zimage=(mv(B,(1,0)),2)
        hy=next(v for v in vv if M.conj((v,0),M.Y)==yimage)
        for hz in vv:
            if M.conj((hz,0),M.Z)!=zimage:continue
            target=six_values(hy,hz)
            ok,autom=M.check_pair_map(M.X,yimage)
            assert ok and autom[M.Z]==zimage
            assert mv(B,(1,2))==(1,2)
            mordell_targets.append((B,target,autom))
    assert len(mordell_targets)==9 and len(targets)==4

    records=[]
    full_records=[]
    original_mordell_three_cycle_failures=[]
    for index,rec in enumerate(data['CM_words_in_F']):
        f=tuple(rec['word']);fvector=vecword(f)
        fm=[fvector[2*j:2*j+2] for j in range(6)]
        if add(add(fm[2],fm[4]),fm[0])!=(0,0):
            original_mordell_three_cycle_failures.append(index)
        for target_index,(B,target,autom) in enumerate(targets):
            wanted=(0,)*12+tuple((a-b)%3 for a,b in zip(target,fvector[12:]))
            solution=span.solution(wanted)
            entry={'CM_index':index,'extra_CM_coset':rec['extra_CM_coset'],
                   'Gaussian_B':B,'target_index':target_index,
                   'has_correction_retaining_all_six_Mordell_values':solution is not None}
            if solution is not None:
                correction,coeff=solution
                fixed=red(f+correction)
                fv=vecword(fixed)
                assert fv[:12]==fvector[:12] and fv[12:]==target
                assert all(sum((1 if k>0 else -1) for k in correction if abs(k)==i)==0
                           for i in (1,2))
                entry.update({'basis_coefficients':sorted(coeff.items()),
                              'correction_literal_F_word':correction,
                              'corrected_word_sha256':hashlib.sha256(json.dumps(fixed).encode()).hexdigest()})
            records.append(entry)
        for mordell_index,(MB,mt,mautom) in enumerate(mordell_targets):
            for gaussian_index,(GB,gt,gautom) in enumerate(targets):
                target=mt+gt
                wanted=tuple((a-b)%3 for a,b in zip(target,fvector))
                solution=span.solution(wanted)
                if solution is None:continue
                correction,coeff=solution
                fixed=red(f+correction)
                assert vecword(fixed)==target
                # The literal corrected source pair induces the two full
                # automorphisms, hence their automorphism of the actual
                # full product image certified below.
                full_records.append({'CM_index':index,
                    'extra_CM_coset':rec['extra_CM_coset'],
                    'Mordell_target_index':mordell_index,
                    'Gaussian_target_index':gaussian_index,
                    'Mordell_B':MB,'Gaussian_B':GB,
                    'basis_coefficients':sorted(coeff.items()),
                    'correction_literal_F_word':correction,
                    'corrected_word_sha256':hashlib.sha256(json.dumps(fixed).encode()).hexdigest()})

    # The exact two-factor F-image is also retained for the generation scope.
    one=(M.one,G.one);gens=[(M.X,G.X),(M.Y,G.Y)]
    joint={one};todo=deque([one])
    while todo:
        a=todo.popleft()
        for b in gens:
            c=(M.mul(a[0],b[0]),G.mul(a[1],b[1]))
            if c not in joint:joint.add(c);todo.append(c)
    assert len(joint)==54*36

    counts={str(i):sum(r['has_correction_retaining_all_six_Mordell_values']
                       for r in records if r['CM_index']==i) for i in range(24)}
    full_counts={str(i):sum(r['CM_index']==i for r in full_records) for i in range(24)}
    assert all(n==4 for n in counts.values())
    assert all(n==4 for n in full_counts.values())
    for i in range(24):
        rows=[r for r in full_records if r['CM_index']==i]
        assert len({r['Mordell_target_index'] for r in rows})==1
        assert len({r['Gaussian_target_index'] for r in rows})==4
    output={'status':'PASS_COMPLETE_TWELVE_EVALUATION_K6_IMAGE',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
            'pair_order':['xy','yx','zx','xz','yz','zy'],
            'factor_order':['Mordell']*6+['Gaussian']*6,
            'all_original_N_pair_commutators':len(allcomm),
            'initial_commutator_rank':initial_rank,
            'normal_conjugation_additions':conjugation_additions,
            'complete_N_derived_and_K6_translation_rank':len(span.rows),
            'Mordell_correction_projection_rank':mordell_rank,
            'Gaussian_correction_projection_rank':gaussian_rank,
            'correction_image_is_exact_product':len(span.rows)==mordell_rank+gaussian_rank,
            'exact_basis':[{'pivot':p,'vector':span.rows[p],'literal_F_word':span.words[p]}
                           for p in sorted(span.rows)],
            'all_N_images_have_exponent_dividing6':True,
            'all_basis_words_replayed_in_all_twelve_maps':True,
            'Gaussian_targets_per_CM_origin_retaining_all_Mordell_values':counts,
            'joint_single_pair_F_image_order':len(joint),
            'records':records,
            'Mordell_framed_norm_targets':[
                {'B':B,'six_values':v} for B,v,_ in mordell_targets],
            'Gaussian_framed_norm_targets':[
                {'B':B,'six_values':v} for B,v,_ in targets],
            'original_Mordell_three_cycle_failures':original_mordell_three_cycle_failures,
            'complete_both_orbifold_norm_fibre_counts':full_counts,
            'complete_both_orbifold_norm_records':full_records,
            'actual_corrected_two_factor_source_image_order':len(joint),
            'scope':'Complete correction-image fibres for the twelve specified '
                    'evaluations, including all two-cycle and three-cycle equations '
                    'and determinant-one automorphisms of both actual orbifold '
                    'quotients. The corrected two-factor source map is onto. '
                    'No automorphism of the whole old joint source, full-GT lift, '
                    'or omitted evaluation is inferred.',
            'seconds':round(time.monotonic()-start,6)}
    (HERE/'bc_orbifold_CM_six.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['status','initial_commutator_rank',
                'normal_conjugation_additions','complete_N_derived_and_K6_translation_rank',
                'Gaussian_targets_per_CM_origin_retaining_all_Mordell_values',
                'complete_both_orbifold_norm_fibre_counts',
                'original_Mordell_three_cycle_failures',
                'joint_single_pair_F_image_order','seconds']},indent=2))


if __name__=='__main__':main()
