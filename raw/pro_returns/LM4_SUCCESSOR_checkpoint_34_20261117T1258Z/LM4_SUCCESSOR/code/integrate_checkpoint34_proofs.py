"""Integrate eight fully reviewed proofs, preserving all preceding central bytes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    specs = [
      ('A.106','work_A/A106_central_congruence_hexagon_proposed.tex','sections/a_central_congruence_hexagon.tex','7da2b23a1c970fd1dfb38423d3d43b9c7391ec866828eaf0c20685115139d97b'),
      ('A.107','work_A/A107_relative_central_modular_conjugacy_proposed.tex','sections/a_relative_central_modular_conjugacy.tex','27289531e4c5bfff0e2fa950892d656a812ca8cc830a75ed8a86b0351d53a660'),
      ('A.108','work_A/A108_central_quotient_factor_transporter_proposed.tex','sections/a_central_quotient_factor_transporter.tex','eb01b6017808a8ea08b789300d62a0e360c40e1d91fe038bbde3b23cad0e263c'),
      ('A.109','work_DE/A109_derived_cyclic_cohomology_proposed.tex','sections/a_derived_cyclic_cohomology.tex','caf3f5d1711a8e249c4f5bbeef97faf58c7d0d9218335fe7e9e285280fe976b0'),
      ('A.110','work_DE/A110_quotient_frame_ambiguity_proposed.tex','sections/a_quotient_frame_ambiguity.tex','32a44b0a03f01f7cc55d2e5bd9dd2a1127fae6951845b3436d7ea10e7219d61b'),
      ('A.111','work_root/A111_coherent_C2_CM_proposed.tex','sections/a_coherent_C2_CM.tex','6eb5def140f375f616d9f2ba56d02d260fc58f5bb4d06cdedfcee29a545f0ebc'),
      ('B.165','work_CE/B165_entire_deleted_kernel_cohomology_proposed.tex','sections/b_entire_deleted_kernel_cohomology.tex','2b35c67cf3452f646aa1c51bbd5464331cc17b055e5b15b726861e5ecb6842bb'),
      ('B.166','work_CE/B166_entire_filling_cohomology_proposed.tex','sections/b_entire_filling_cohomology.tex','7dd113a2fb9db4f23b82705ace9141a9cbaa030f7c27cdb46d8f992601148d09'),
    ]
    copies = [dict(statement=s,source=p,target=t,sha256=h) for s,p,t,h in specs]
    for row in copies:
        data=(ROOT/row['source']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==row['sha256']
        assert not any(c<32 and c not in (9,10) for c in data)
        assert not (ROOT/row['target']).exists()
    independent=json.loads((ROOT/'records/checkpoint34_independent_review_manifest.json').read_text())
    assert independent['root_read_all_complete_reviews'] is True
    assert independent['status']=='PASS_FINAL_SOURCES'
    assert independent['source_hashes']=={r['source']:r['sha256'] for r in copies}
    for rel,h in independent['reviews'].items():
        assert digest(ROOT/rel)==h,rel
    review_path=ROOT/'records/checkpoint34_root_formal_reviews.json'
    assert not review_path.exists()

    paper=(ROOT/'LM4_SUCCESSOR_paper.tex').read_text()
    anchor=r'\input{sections/a_original_CM_parity.tex}'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+r['target']+'}' for r in copies[:6]))
    anchor='the other frame sign, and hence the actual parity, remains open.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'
      'The same marked hexagon is now killed in the first relative central\n'
      'quotient of the actual signed congruence kernel, with an exact\n'
      'coordinate description. The prescribed map is an automorphism\n'
      'through the entire relative central tower, and extends to a genuine\n'
      'modular automorphism on the first quotient. An actual factor\n'
      'transporter exists there. Its extra centralizers prevent the\n'
      'original character formula from using arbitrary quotient frames.\n'
      'The derived cyclic kernel has exactly two cohomology classes.\n'
      'A separate choice-independent involutory coherence class maps\n'
      'exactly to the original CM sign. Neither class is assigned its\n'
      'remaining actual value by these quotient results.')
    anchor='The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,
      'The entire deletion-kernel cohomology is the completed source coset\n'
      'space, and the entire filling-kernel cohomology is a left-coset\n'
      'space of the actual fixed subgroup. The actual contact source\n'
      'is an exact closed subspace; deciding whether it is the whole\n'
      'space remains the local contact gate.\n'+anchor)
    part_b=(ROOT/'sections/part_B.tex').read_text()
    for row in copies[6:]:
        part_b+=r'\input{'+row['target']+'}\n'

    with (ROOT/'task_coverage.csv').open(newline='') as stream:
        reader=csv.DictReader(stream); fields=reader.fieldnames; tasks=list(reader)
    assert len(tasks)==49
    old_outcomes=[(r['task'],r['outcome']) for r in tasks]
    for row in tasks:
        selected=[]
        if row['task'] in {'A.4','A.5','A.7','A.8'}:
            selected+=['A.106','A.107','A.108']
            row['state']+=' Cycle34: A106 proves the exact first central congruence model and kills the same marked hexagon there; A107 proves automorphy through the entire relative central F tower and genuine modular conjugacy on its first quotient; A108 constructs the actual quotient order-three factor transporter with its exact branch, abelian vector and signed matrix.'
            row['approaches']+=' Continuous Schur cohomology with the actual dyadic factor; natural five-term comparison; central-image Hopfian induction; exact signed cyclic covariance; all-prime determinant correction and coprime pro-two lifting.'
            row['obstruction']='The tower is not proved cofinal; full surjectivity is exactly surjectivity on N_infinity. No higher cubic relation, full hexagon or full negative involution lift follows. A positive lifting criterion must retain its exact multiplier and kernel hypotheses.'
            row['next_step']='Test closed-normal central lifting on the actual modular quotient with multiplier powers fully typed, then solve the remaining negative norm and coherent full-frame equations.'
        if row['task'] in {'A.6','A.7','A.8'}:
            selected+=['A.109','A.110','A.111']
            row['state']+=' A109 computes the entire two-point derived cyclic H1 and identifies the original CM point; A110 proves arbitrary quotient-frame ambiguity and a nonlifting class, so N1 is not pro-two; A111 constructs an intrinsic C2 coherent-frame class whose signed image is exactly the original CM parity.'
            row['obstruction']+=' The actual two-point label and the coherent C2 class remain undecided. Scalar-image vanishing is not claimed sufficient for full coherent-frame triviality.'
        if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
            selected+=['B.165','B.166']
            row['state']+=' Cycle34: B165 identifies the whole actual deletion-kernel H1 with the completed source coset space and gives a continuous pointed section from filling cohomology. B166 identifies the whole filling H1 with a left-coset space of the actual fixed subgroup and the contact source with its exact closed subspace.'
            row['approaches']+=' Finite-factor torsion with the unwanted branch excluded in the filled target; compact actual lift sets; exact nonabelian cohomology fibers and inverse-coset comparison.'
            row['obstruction']='The exact contact subspace is not yet proved to be the whole filling cohomology space; equivalently the basepoint fiber is not yet proved to equal the full closed contact image. Further global Main B transfer remains separate.'
            row['next_step']='Determine the actual basepoint fiber using all three whole contact orbits and the retained node and signed-translate presentation.'
        for sid in selected:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids']+=';'+sid
    assert [(r['task'],r['outcome']) for r in tasks]==old_outcomes
    assert all(next(r for r in tasks if r['task']==t)['outcome']=='Open' for t in ('A.8','B.4'))

    report=(ROOT/'LM4_SUCCESSOR_report.md').read_text()
    assert report.splitlines()[0]=='INCOMPLETE'
    lines=report.splitlines(True)
    start=next(i for i,line in enumerate(lines) if line.startswith('| Task or lead |'))
    end=start
    while end<len(lines) and lines[end].startswith('|'): end+=1
    cell=lambda s:s.replace('|',r'\|').replace('\n',' ')
    lines[start:end]=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']+[
      '| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks]
    report=''.join(lines)+'\n\n'+(ROOT/'records/thirty_fourth_hour_research_report.md').read_text()

    backup=ROOT/'records/pdf_qa/checkpoint34_before_integration'
    assert not backup.exists()
    paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
    paths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','code/assemble_register.py']
    paths+=[str(p.relative_to(ROOT)) for p in (ROOT/'records').glob('build_*.log')]
    for rel in paths:
        src=ROOT/rel
        if src.is_file():
            suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
            dest=backup/(rel+suffix); dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dest)
    for row in copies: (ROOT/row['target']).write_bytes((ROOT/row['source']).read_bytes())
    (ROOT/'LM4_SUCCESSOR_paper.tex').write_text(paper)
    (ROOT/'sections/part_B.tex').write_text(part_b)
    (ROOT/'LM4_SUCCESSOR_report.md').write_text(report)
    with (ROOT/'task_coverage.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader(); writer.writerows(tasks)
    register=(ROOT/'code/assemble_register.py').read_text()
    old="('A.6;A.7;A.8' if int(m[2])==105 else 'A.7;A.8')"
    new="('A.6;A.7;A.8' if int(m[2]) in {105,109,110,111} else ('A.4;A.5;A.7;A.8' if int(m[2]) in {106,107,108} else 'A.7;A.8'))"
    assert register.count(old)==1
    register=register.replace(old,new)
    old="parts=['sections/b_sources.bib',"
    assert register.count(old)==1
    register=register.replace(old,"parts=['sections/b_sources.bib','sections/a_central_sources.bib',")
    (ROOT/'code/assemble_register.py').write_text(register)
    subprocess.run([sys.executable,str(ROOT/'code/assemble_register.py')],check=True)
    rows=list(csv.DictReader((ROOT/'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows)==362 and dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':318,'Refuted':19,'Open':19}
    bib=ROOT/'LM4_SUCCESSOR_references.bib'
    assert len(re.findall(r'^@',bib.read_text(),re.M))==116
    review=dict(status='PASS_COMPLETE_SOURCE_REVIEW',recorded_at=datetime.now(timezone.utc).isoformat(),reviewer='/root',
        scope='All eight complete proposed proofs read. Final notation/provenance-only differences read in full. Independent final-source reviews and the two genuinely executed finite certificates are bound; this is not PDF visual approval.',
        copies=copies,independent_reviews=independent['reviews'],
        bibliography=dict(path='LM4_SUCCESSOR_references.bib',sha256=digest(bib),entries=116,
                          scope='One verified primary entry A_Beyl1986 added, with exact Prop5.7 reading scope and explicit earlier-proof retrieval limitation.'),
        remaining_open=['Main A','Main B','Actual CM parity','Coherent C2 class','Local contact-image equality'])
    review_path.write_text(json.dumps(review,indent=2)+'\n')
    (ROOT/'records/checkpoint34_formal_source_copies.json').write_text(json.dumps(dict(
        integrated_at=datetime.now(timezone.utc).isoformat(),copies=copies,
        comparison='Every integrated source is byte-identical to its final fully reviewed candidate.'),indent=2)+'\n')
    print('Integrated8 reviewed statements:362 claims,318Proved,19Refuted,19Open,6Known;116references,49tasks. Main A/B and actual CM parity remain Open.',flush=True)


if __name__=='__main__':
    main()
