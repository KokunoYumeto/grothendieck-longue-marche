"""Integrate the six complete reviewed37 proofs, retaining every predecessor.

The explicit inputs are written by root only after complete source and
independent-review reads. This helper creates no PDF or checkpoint ZIP.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
REPORT=r'''## Thirty-seventh-hour research: the actual Brunnian kernel and GT0 torus fixed group

### Exact decision status

Main A, Main B, the original coherent class and actual CM parity remain **Open**. Six new proved statements retain their actual groups, maps, markings and topology. They strengthen the full-group reductions; none identifies a finite or linear shadow with the original missing word equality.

### Actual based deletions and the entire obstruction

A126 proves every based deletion row of the reduced three-strand elliptic braid group, including the two-strand half-twist and its square. The original unique derived transporter has tuple (Ua,U theta(a),Ua). The entire joint image of the pure derived subgroup is the product of three full derived free groups. The common word remains tied to the original transporter, and arbitrary quotient tuples are not assigned pentagon realizations.

One literal row in the retained checkpoint36 research note was incorrect: for C=sigma tau and m=tau^-1 sigma^2 tau, the actual braid cycle is a -> b -> m -> a, so rho(b)=m, not b m b^-1. A126 prints the corrected full calculation. All three deletion tuples and the subsequent quotient identities are unchanged, because the two meridians have different coordinate supports. The former source and its former reviews remain preserved; the explicit correction is work_A/actual_based_forgetting_row_correction37.md. No earlier archive is altered.

A127 computes the entire continuous C3 cohomology of the actual Brunnian joint kernel as a pointed compact copy of E'. The actual corrected involution is Ad(b0^-1) beta2. The specified canonical cyclic defect has parameter ell=b0^-1 beta2(a_u^-1) a_u, and its corrected C2 class is [b0^-1]. The proof retains the original unique transporter, every half-braid action and all conjugation orders. Neither this representative nor its class is evaluated. Reduced cubic, tuple and norm constraints admit arbitrary common parameters through actual lifts; this is not a realization by the canonical pentagon word.

A128 identifies that entire actual Brunnian kernel as U intersect V = closed[U,V], where U,V are the kernels of the two literal retractions of the actual free rank-three forgetting fiber. It proves the ordinary intersection identity by a complete simultaneous Schreier basis, then proves full induced topology for the specific finitely generated fiber product by explicit finite-target refinement. Only then does it pass to the actual compact kernel. The kernel is nontrivial by an exact reduced word. No general infinite-index completion theorem or freeness assertion for the joint kernel is used.

### Boundary neutrality, norm uniqueness and the exact remaining word

A129 writes the actual boundary defect as a full-group coboundary for a noncusp reflection. Its entire derived H1 is trivial because the actual noncusp fixed group maps onto the full fixed homology line. The cusp actions instead have full pointed compact derived H1 equal to Zhat. The canonical norm equation has a unique solution in the entire group, and its allowed norm-preserving derived repair group is trivial. Thus derived cohomological neutrality supplies no alteration of the specified canonical word.

With the original C13 marking, the canonical norm word is exactly its specified cusp transporter. Using A130, the missing boundary equality is equivalent to a(k)=a_B, where a_B is the unique Y-normalized noncusp fixed generator and a(s) is the printed continuous all-exponent family. The two actual reflections send a(s) to a(-s-1) and a(-s-1)^-1. Their composite always inverts a(s), while the required specified equality a(k)=a(-k-1) remains open. The Brunnian corrected class lies in the other reflection branch and is not neutralized by the boundary cohomology calculation.

A130 constructs the two-strand torus involution directly from the original negative GT0 equations. The correctly ordered negative hexagon implies the multiplier-one hexagon by the original C30 substitution. The resulting endomorphism sends the actual commutator to its inverse, so the finite-cover boundary argument proves full automorphy. Its restriction to the embedded original pair is the original involution. The exact half-twist identity gives two commuting reflections. A fixed-point-free involution on the pro-odd fixed kernel has actual fixed-coset lifting by a literal half-root; its finite quotients are abelian and inverted. The primitive-power centralizer theorem then kills that entire kernel. The noncusp fixed group is therefore Zhat at this actual GT0-derived two-strand scope. A full three-strand GT0 action, a canonical-word pentagon, a full-unit assertion for its parameter and full generation are not inferred.

### The actual index-two three-color source quotient

B174 constructs the genuine index-two subgroup using the combined fiber parity and second-source exponent. The corrected source lift v*=f^-1 v preserves the relevant Schreier deletion kernel under all four signed operators. All forty original nodes and their decks leave exactly two seeds. The filled quotient retains their normal closure under the entire signed source group, rather than only one source orbit.

The two initial fiber seeds give a partial centralizer amalgam. The actual second source operator fails to preserve its proposed free base even after the canonical correction fixing D0; a displayed amalgam-reduced word proves the obstruction. The fully filled target also kills [A_s,D_s] and [[m,D_s],A_s], so it cannot decide the original mixed-word kernel membership. These are target statements, not relations asserted in the original source. Every finite target pulls back through the actual finite-index source, which gives the claimed compact quotient with its ambient topology.

The sole prescribed exact checker genuinely exited zero in the owner's tool chunk79935c and passed353 checks. Its complete source, stdout, empty stderr, all signed words, all node/deck images and the observed-exit receipt are retained. It is one exact symbolic certificate, not a finite-target census.

### Sources, retention and next work

All six complete formal proofs and their independent reviews were read before integration. The new arguments use the already checked original braid and cusp sources; the entire original C30 substitution and the full needed C5--C8/C11--C13 project proofs were reopened at their stated scopes. No fresh whole-paper primary reading or new bibliography entry is claimed. The117-reference bibliography retains its verified/unverified scope annotations. All49 task outcomes are unchanged.

Checkpoint36 was closed and all three actual archive verifiers exited zero. Its service receipt reports the save succeeded and the exact link was delivered. The save process's completion-poll output was lost to truncation; its exit code is explicitly not reconstructed from the receipt, and the save was not retried. The exact observed record retains that limitation.

Checkpoint37 is the sole scheduled archive for15:49:30UTC, with the next review at16:49:30UTC. Its closed-parent induction must retain all173786 inherited identities and all11156 parent logical files, for184942 rows and zero omissions. The final PDF, source hashes, render reviews and actual sequential512/256/64MiB size measurement are separate required evidence. No archive is created by this integration step.

The next mathematical work attacks the marked generator equality and its original pentagon transporter, and the original joint contact kernel beyond the target that kills the mixed test. Both mains and actual CM parity remain open.
'''

def main():
    inputs=json.loads((ROOT/'records/checkpoint37_integration_inputs.json').read_text())
    assert inputs['root_entire_sources_and_reviews_read'] is True
    copies=inputs['copies'];reviews=inputs['independent_reviews']
    assert [r['statement'] for r in copies]==['A.'+str(n) for n in range(126,131)]+['B.174']
    for rel,digest in reviews.items():assert sha(ROOT/rel)==digest,rel
    review_text='\n'.join((ROOT/p).read_text() for p in reviews)
    for row in copies:
        assert sha(ROOT/row['source'])==row['sha256']
        assert row['sha256'] in review_text
        assert not (ROOT/row['target']).exists()
    paper=(ROOT/'LM4_SUCCESSOR_paper.tex').read_text()
    anchor=r'\input{sections/a_elliptic_derived_transporter.tex}'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+r['target']+'}' for r in copies[:5]))
    anchor='cohomology coordinates without evaluating the original frame.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+r'''The actual based joint kernel now has the entire closed-commutator
description and a full cyclic cohomology parameterization. The actual
boundary reflection has trivial derived cohomology, while the canonical
norm permits no nontrivial correction. A direct two-strand construction
from negative GT-zero data proves that its noncusp fixed group is
procyclic. The boundary is equality with its uniquely marked generator;
that specified equality and full generation remain unresolved.''')
    anchor='The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,r'''An actual index-two three-color quotient retains the entire signed
source saturation of two node seeds. Its second source operator defeats
the proposed base-preserving centralizer correction, and the quotient
kills the specified mixed contact test.
'''+anchor)
    part_b=(ROOT/'sections/part_B.tex').read_text()+'\n'+r'\input{'+copies[-1]['target']+'}\n'
    register=(ROOT/'code/assemble_register.py').read_text()
    register=register.replace("banswers={169:","banswers={174:'B.4;B.4.a;B.4.b;B.4.c;B.4.h',169:")
    register=register.replace('{105,109,110,111,112,113,117,119,120,124,125}', '{105,109,110,111,112,113,117,119,120,124,125,126,127,128}')
    register=register.replace("answers=(banswers.get(","answers=('A.4;A.5;A.7;A.8;C.1;C.2' if m[1]=='A.130' else 'A.4;A.5;A.7;A.8;C.2' if m[1]=='A.129' else banswers.get(")
    with (ROOT/'task_coverage.csv').open(newline='') as f:
        reader=csv.DictReader(f);fields=reader.fieldnames;tasks=list(reader)
    assert len(tasks)==49
    outcomes=[(r['task'],r['outcome']) for r in tasks]
    for row in tasks:
        selected=[]
        if row['task'] in {'A.4','A.5','A.6','A.7','A.8'}:
            selected=['A.'+str(n) for n in range(126,131)]
            row['state']+=' Cycle37: the entire actual Brunnian kernel is a closed commutator, and its whole C3 cohomology and corrected involution parameter are determined. The boundary reflection has trivial derived H1 but its canonical norm has no nontrivial repair. The actual GT0-derived noncusp torus fixed group is procyclic; the specified marked generator equality and full generation remain open.'
            row['approaches']+=' Complete based deletion tables and exact row correction; full simultaneous Schreier intersection proof and finite-target fiber-product topology; exact cusp/noncusp cohomology; direct ordered GT0 two-strand construction and pro-odd half-root fixed lifting.'
            row['obstruction']='The specified canonical a(k)=a_B equality, the full original transporter parameter and the original coherent/CM value remain unevaluated. Quotient cohomology neutrality and fixed-group procyclicity do not imply marked generation.'
            row['next_step']='Constrain the specified a(k) by the original pentagon transporter and its full Brunnian action, retaining every original marking.'
        if row['task'] in {'C.1','C.2'}:
            selected=['A.130']+(['A.129'] if row['task']=='C.2' else [])
            row['state']+=' Cycle37: for the actual torus action constructed from a negative GT0 involution, the noncusp pro-odd fixed kernel is trivial and the full fixed group is Zhat. This restricted result does not classify every negative torus action or prove marked generation.'
        if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
            selected=['B.174']
            row['state']+=' Cycle37: the actual combined-parity index-two source has a three-color quotient retaining the complete signed source saturation of two nodes. Its canonical second-source correction does not preserve the partial free base, and the filled target kills the specified mixed contact word.'
            row['approaches']+=' Exact all-signed Schreier quotient, forty original nodes and decks, whole-source normal closure, partial amalgam normal form and actual finite-index ambient refinement;353 prescribed word checks.'
            row['obstruction']='The new target kills the mixed word and therefore cannot determine its membership in the original unknown joint kernel C0. The partial centralizer amalgam is not the fully source-saturated fiber.'
            row['next_step']='Analyze the original whole joint contact kernel with a target or structural comparison that retains the mixed contact word.'
        for sid in selected:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids']+=';'+sid
    assert outcomes==[(r['task'],r['outcome']) for r in tasks]
    report=(ROOT/'LM4_SUCCESSOR_report.md').read_text()
    assert report.splitlines()[0]=='INCOMPLETE'
    lines=report.splitlines(True);start=next(i for i,s in enumerate(lines) if s.startswith('| Task or lead |'));end=start
    while end<len(lines) and lines[end].startswith('|'):end+=1
    cell=lambda s:s.replace('|',r'\|').replace('\n',' ')
    lines[start:end]=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']+[
        '| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks]
    report=''.join(lines)+'\n\n'+REPORT
    backup=ROOT/'records/pdf_qa/checkpoint37_before_integration';backup.mkdir(parents=True,exist_ok=False)
    oldpaths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
    oldpaths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','code/assemble_register.py']
    oldpaths+=[str(p.relative_to(ROOT)) for p in (ROOT/'records').glob('build_*.log')]
    for rel in oldpaths:
        p=ROOT/rel
        if p.is_file():
            suffix='.retained.txt' if p.suffix in {'.aux','.bbl','.blg','.toc'} else ''
            dest=backup/(rel+suffix);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
    for row in copies:(ROOT/row['target']).write_bytes((ROOT/row['source']).read_bytes())
    for rel,value in [('LM4_SUCCESSOR_paper.tex',paper),('sections/part_B.tex',part_b),('code/assemble_register.py',register),('LM4_SUCCESSOR_report.md',report),('records/thirty_seventh_hour_research_report.md',REPORT)]:
        (ROOT/rel).write_text(value)
    with (ROOT/'task_coverage.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
    subprocess.run([sys.executable,str(ROOT/'code/assemble_register.py')],check=True)
    rows=list(csv.DictReader((ROOT/'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows)==389 and dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':345,'Refuted':19,'Open':19}
    bib=ROOT/'LM4_SUCCESSOR_references.bib';assert len(re.findall(r'^@',bib.read_text(),re.M))==117
    now=datetime.now(timezone.utc).isoformat()
    records={
      'root_formal_reviews':dict(status='PASS_COMPLETE_SOURCE_REVIEW',recorded_at=now,reviewer='/root',copies=copies,independent_reviews=reviews,bibliography=dict(path=str(bib.relative_to(ROOT)),sha256=sha(bib),entries=117,scope='No new entry. Exact prior primary scopes retained; fresh full C30 and needed C5--C8/C11--C13 project proof reads. No fresh whole-primary-paper assertion.'),remaining_open=['Main A','Main B','Actual CM parity','Original boundary','Original coherent class','Original mixed contact kernel']),
      'formal_source_copies':dict(integrated_at=now,copies=copies,comparison='All six integrated proofs byte-identical to completely reviewed final candidates.'),
      'independent_review_manifest':dict(status='PASS_FINAL_SOURCES',recorded_at=now,root_read_all_complete_reviews=True,source_hashes={row['source']:row['sha256'] for row in copies},reviews=reviews,scope='Complete final-source reviews; no PDF or producer completion is inferred.')}
    for name,record in records.items():
        with (ROOT/('records/checkpoint37_'+name+'.json')).open('x') as f:json.dump(record,f,indent=2);f.write('\n')
    print('Integrated6 reviewed proofs:389statements345Proved19Refuted19Open6Known;117references49tasks. Both mains and actualCM remainOpen.',flush=True)

if __name__=='__main__':main()
