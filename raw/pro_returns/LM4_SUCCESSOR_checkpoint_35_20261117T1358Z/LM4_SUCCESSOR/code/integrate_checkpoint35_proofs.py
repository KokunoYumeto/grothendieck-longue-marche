"""Integrate ten completely reviewed sources, preserving predecessor bytes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
SPECS=[
 ('A.112','work_DE/A112_actual_central_product_odd_cohomology_proposed.tex','sections/a_actual_central_product_odd_cohomology.tex','aac45807a4751e1299b7980225d0ef4bdcf4729acc842d19a202fa1636b9f310'),
 ('A.113','work_DE/A113_entire_cyclic_kernel_and_sign_twist_proposed.tex','sections/a_entire_cyclic_kernel_sign_twist.tex','9e527f4819dd688016cf26c6510b3b667b4114c8bb54dc60f2d010464a11bf9b'),
 ('A.114','work_A/A114_next_modular_central_refinement_proposed.tex','sections/a_next_modular_central_refinement.tex','28cf2329db608a2394dcdf84a588fd3d6d64fe716f2886b133e4a2246df48f22'),
 ('A.115','work_A/A115_full_modular_central_tower_proposed.tex','sections/a_full_modular_central_tower.tex','5ed6713a53cdf3f41b53862968e8a7e7bb013830f71bf69a50ebc7c8b44e7dde'),
 ('A.116','work_A/A116_relative_perfect_residual_proposed.tex','sections/a_relative_perfect_residual.tex','d80ef0d5d967bdadd6dad3c005ff56d0a84465d2171867661edcd8dc11a36ebc'),
 ('A.117','work_DE/A117_residual_cyclic_cohomology_coherent_norm_proposed.tex','sections/a_residual_cyclic_cohomology_coherent_norm.tex','207461c1ab3bc125ca8129a16238ccabd51243d38d319f85dcfcf9252cec0689'),
 ('A.118','work_A/A118_normalized_residual_reduction_proposed.tex','sections/a_normalized_residual_reduction.tex','f902b61022a4022b6dff8d833c6df6a7d9d4d489a81143cb5c54b0ea18bdf525'),
 ('A.119','work_DE/A119_entire_residual_involution_cohomology_proposed.tex','sections/a_entire_residual_involution_cohomology.tex','a1a009559be01ec8949dc04fa708c464fddadebad6c014607c0881ab557a7c6e'),
 ('B.167','work_CE/B167_compact_single_contact_family_proposed.tex','sections/b_compact_single_contact_family.tex','c1e8356b219d0cdc89ef5506975fb3a88e87f5ed01cddf5fd888bad9c503617d'),
 ('B.168','work_CE/B168_mixed_contact_compact_separation_proposed.tex','sections/b_mixed_contact_compact_separation.tex','6e83fd1b058d55d8598061554a2ada8f81c4ddabf8ddebecefed17a5da091507'),
]

def main():
    copies=[dict(statement=s,source=p,target=t,sha256=h) for s,p,t,h in SPECS]
    independent=json.loads((ROOT/'records/checkpoint35_independent_review_manifest.json').read_text())
    assert independent['status']=='PASS_FINAL_SOURCES' and independent['root_read_all_complete_reviews']
    assert independent['source_hashes']=={r['source']:r['sha256'] for r in copies}
    for rel,h in independent['reviews'].items(): assert sha(ROOT/rel)==h,rel
    for row in copies:
        data=(ROOT/row['source']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==row['sha256']
        assert not any(c<32 and c not in (9,10) for c in data)
        assert not (ROOT/row['target']).exists()
    paper=(ROOT/'LM4_SUCCESSOR_paper.tex').read_text()
    anchor=r'\input{sections/a_coherent_C2_CM.tex}'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+r['target']+'}' for r in copies[:8]))
    anchor='remaining actual value by these quotient results.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+
      'The actual modular central tower now has compatible full peripheral\n'
      'lifts, but is proved noncofinal: it retains a nontrivial relative\n'
      'perfect residual kernel. The full residual quotient is the product\n'
      'of the original free pro-two quotient and the actual odd factor.\n'
      'We compute its entire cyclic cohomology and retain the separate\n'
      'original cubic condition before a specified lift defines a cocycle.\n'
      'A full normalization puts the correction in the residual kernel\n'
      'and makes its dihedral unit one, with every normalizing factor\n'
      'retained in the transported pentagon. The entire residual\n'
      'involution cohomology is a product of the odd local unit groups.\n'
      'These pointed compact parameterizations do not determine the\n'
      'original coherent class or supply a full intertwining conjugator.')
    anchor='The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,
      'One whole compact contact orbit is a continuously parameterized\n'
      'free profinite family, with a distinct abstract completion of its\n'
      'discrete orbit kernel. A specified mixed contact lies outside this\n'
      'whole compact family; an actual finite ambient extension of a\n'
      'prescribed permutation map separates it.\n'+anchor)
    part_b=(ROOT/'sections/part_B.tex').read_text()
    for row in copies[8:]: part_b+=r'\input{'+row['target']+'}\n'
    with (ROOT/'task_coverage.csv').open(newline='') as stream:
        reader=csv.DictReader(stream); fields=reader.fieldnames; tasks=list(reader)
    assert len(tasks)==49
    outcomes=[(r['task'],r['outcome']) for r in tasks]
    for row in tasks:
        selected=[]
        if row['task'] in {'A.4','A.5','A.7','A.8'}:
            selected+=['A.114','A.115','A.116','A.118']
            row['state']+=' Cycle35: the actual modular central tower has full peripheral lifts; its nontrivial relative-perfect residual R is explicitly determined, and the tower is proved noncofinal. A full normalization has residual correction in R and dihedral unit one, with an exact five-pair transported pentagon retaining every normalizing factor.'
            row['approaches']+=' Primary-by-primary Schur cohomology; unique compact central splittings; actual-coordinate kernel comparison; nested compact full-lift sets; direct peripheral normalization and literal pair evaluations.'
            row['obstruction']='The nontrivial residual subgroup survives every central stage. The original full hexagon and canonical automorphism remain undecided. Normalization is proved at GT0 scope; full GT and an ordinary residual pentagon are not inferred.'
            row['next_step']='Use the complete transported pentagon to constrain the actual residual word and coherent frame, retaining the original cubic norm condition and all normalizing factors.'
        if row['task'] in {'A.6','A.7','A.8'}:
            selected+=['A.112','A.113','A.117','A.119']
            row['state']+=' A112/A113 compute actual central-product and whole cyclic cohomology coordinates, including the prime-three sign twist. A117 retains the original cubic and coherent-frame gates. A119 computes the entire residual involution H1 as the product of odd local unit groups via the specified pointed compact maps.'
            row['obstruction']+=' The original CM label and original coherent class remain unevaluated. The specified full factor lift is not yet a C3-cocycle before the original cubic word is one.'
        if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
            selected+=['B.167','B.168']
            row['state']+=' Cycle35: the entire compact single-contact m-orbit kernel is a continuous free profinite family. A prescribed mixed contact lies outside it, separated by an actual finite ambient characteristic-core extension of a verified S4 fiber map.'
            row['approaches']+=' Explicit inverse compact universal maps; discrete-versus-induced kernel topology; literal frozen source operators; free-basis normal forms; a prescribed permutation certificate and characteristic finite-index core.'
            row['obstruction']='The whole contact image is strictly larger than one compact orbit family, but its equality with the full fixed/cohomology fiber remains unproved. The mixed separator lies inside the contact image and is not a Main B counterexample.'
            row['next_step']='Analyze all mixed contact families and retained node relations against the exact full cohomology fiber.'
        for sid in selected:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids']+=';'+sid
    assert outcomes==[(r['task'],r['outcome']) for r in tasks]
    report=(ROOT/'LM4_SUCCESSOR_report.md').read_text()
    assert report.splitlines()[0]=='INCOMPLETE'
    lines=report.splitlines(True)
    start=next(i for i,s in enumerate(lines) if s.startswith('| Task or lead |'))
    end=start
    while end<len(lines) and lines[end].startswith('|'):end+=1
    cell=lambda s:s.replace('|',r'\|').replace('\n',' ')
    lines[start:end]=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']+[
       '| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks]
    report=''.join(lines)+'\n\n'+(ROOT/'records/thirty_fifth_hour_research_report.md').read_text()
    register=(ROOT/'code/assemble_register.py').read_text()
    old="('A.6;A.7;A.8' if int(m[2]) in {105,109,110,111} else ('A.4;A.5;A.7;A.8' if int(m[2]) in {106,107,108} else 'A.7;A.8'))"
    new="('A.6;A.7;A.8' if int(m[2]) in {105,109,110,111,112,113,117,119} else ('A.4;A.5;A.7;A.8' if int(m[2]) in {106,107,108,114,115,116,118} else 'A.7;A.8'))"
    assert register.count(old)==1;register=register.replace(old,new)
    marker='banswers={1:'
    assert register.count(marker)==1
    register=register.replace(marker,"banswers={167:'B.4;B.4.a;B.4.b;B.4.c;B.4.h',168:'B.4;B.4.a;B.4.b;B.4.c;B.4.h',1:")
    backup=ROOT/'records/pdf_qa/checkpoint35_before_integration'
    assert not backup.exists()
    paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
    paths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','code/assemble_register.py']
    paths+=[str(p.relative_to(ROOT)) for p in (ROOT/'records').glob('build_*.log')]
    for rel in paths:
        src=ROOT/rel
        if src.is_file():
            suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
            dest=backup/(rel+suffix);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
    for row in copies:(ROOT/row['target']).write_bytes((ROOT/row['source']).read_bytes())
    for rel,value in [('LM4_SUCCESSOR_paper.tex',paper),('sections/part_B.tex',part_b),('LM4_SUCCESSOR_report.md',report),('code/assemble_register.py',register)]:
        (ROOT/rel).write_text(value)
    with (ROOT/'task_coverage.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
    subprocess.run([sys.executable,str(ROOT/'code/assemble_register.py')],check=True)
    rows=list(csv.DictReader((ROOT/'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows)==372 and dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':328,'Refuted':19,'Open':19}
    bib=ROOT/'LM4_SUCCESSOR_references.bib'
    assert len(re.findall(r'^@',bib.read_text(),re.M))==116
    now=datetime.now(timezone.utc).isoformat()
    review=dict(status='PASS_COMPLETE_SOURCE_REVIEW',recorded_at=now,reviewer='/root',copies=copies,
      scope='All ten complete proofs read, including every preserved final precision/citation/cubic-gate difference. The full finite checker, actual output and certificate were read. This is not PDF visual approval.',
      independent_reviews=independent['reviews'],bibliography=dict(path='LM4_SUCCESSOR_references.bib',sha256=sha(bib),entries=116,
        scope='No new entry. Actual primary reading scope for HR1985 and the original LM4 D34 proof/referee is bound; Beyl retains its precise prior verified scope.'),
      remaining_open=['Main A','Main B','Actual CM parity','Original coherent class','Local contact-image equality'])
    with (ROOT/'records/checkpoint35_root_formal_reviews.json').open('x') as stream:json.dump(review,stream,indent=2);stream.write('\n')
    with (ROOT/'records/checkpoint35_formal_source_copies.json').open('x') as stream:
        json.dump(dict(integrated_at=now,copies=copies,comparison='Every integrated source is byte-identical to its final fully reviewed candidate.'),stream,indent=2);stream.write('\n')
    print('Integrated10 reviewed statements:372 claims,328Proved,19Refuted,19Open,6Known;116references,49tasks. Main A/B and actual CM parity remain Open.',flush=True)

if __name__=='__main__':main()
