"""Integrate eleven completely read formal proofs, retaining all predecessor bytes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
SPECS=[
 ('A.120','work_DE/A120_odd_coherent_forgetting_proposed.tex','sections/a_odd_coherent_forgetting.tex','32f8348499688ffd4d3d5cca16e995df5f4967355f03d57deb2ebda11f6a3e52'),
 ('A.121','work_A/A121_elliptic_pentagon_cubic_proposed.tex','sections/a_elliptic_pentagon_cubic.tex','cfee9d27b7ec7c597e0bd03409dd8d326d546f4aa754163cbbed2f160e84673d'),
 ('A.122','work_A/A122_elliptic_original_cusp_bridge_proposed.tex','sections/a_elliptic_original_cusp_bridge.tex','5c888bf3de836e8a234f37bf3cc9196f56063122d67400a8d40b951a41eb7dc1'),
 ('A.123','work_A/A123_elliptic_boundary_automorphy_proposed.tex','sections/a_elliptic_boundary_automorphy.tex','4d5eee62ae44f489c80a7d99a44c64f0dbdc16690eb160c2e01b7b8b3ea0ba82'),
 ('A.124','work_root/A124_actual_elliptic_torsion_transport_proposed.tex','sections/a_actual_elliptic_torsion_transport.tex','fd436ed98a15e581b7afed1c2e239ac2d8e2745dabd059a6c18d5217d110f9c0'),
 ('A.125','work_A/A125_elliptic_derived_transporter_proposed.tex','sections/a_elliptic_derived_transporter.tex','1fecf9668257fef978ef6de0e088bed9e351184c990ff332268159ad696ba37b'),
 ('B.169','work_CE/B169_one_sided_contact_image_topology_proposed.tex','sections/b_one_sided_contact_image_topology.tex','cabeee2269d8d73ddd4e9a73883007f06d1b07b730bd9d53191db5c7c83bc165'),
 ('B.170','work_CE/B170_actual_contact_split_defect_proposed.tex','sections/b_actual_contact_split_defect.tex','c6c4d595c8ccb2f0d64aff0272e3d4b89b269101ce73ae6266be7fe8a1ab773a'),
 ('B.171','work_CE/B171_mirrored_source_restriction_proposed.tex','sections/b_mirrored_source_restriction.tex','8ee0a88685d5a2aaf998e2abb564e13658f1e1ffdc7c5c278f71a087ad351338'),
 ('B.172','work_CE/B172_defect_derived_image_proposed.tex','sections/b_defect_derived_image.tex','a7ddca79723d9e4528502579c2da451fb95bba2e4d0e1b7b0f5130844ed2629c'),
 ('B.173','work_CE/B173_complementary_retained_contact_target_proposed.tex','sections/b_complementary_retained_contact_target.tex','e21b8e6f0a1a1b863776a6f3d822fc3d397f235da4215153efd310584f9d164a'),
]
REVIEW_PAIRS=[
 ('work_CE/review_A120_A123_full_sources36','txt'),
 ('work_DE/review_A124_full_source36','md'),
 ('work_A/review_A124_actual_elliptic_torsion36','md'),
 ('work_DE/review_A125_full_source36','md'),
 ('work_DE/review_B169_B172_full_sources36','md'),
 ('work_DE/review_B173_full_source36','md'),
]
REPORT=r'''## Thirty-sixth-hour research: elliptic torsion and complementary contact quotients

### Exact decision status

Main A, Main B, the original coherent involution class and the actual CM parity remain **Open**. This cycle adds eleven proved statements at their explicit scopes. Conditional conclusions retain their hypotheses. No finite quotient classification is promoted to an existence assertion in the full profinite group.

### Forgetting odd centralizer coordinates

A120 computes the actual inclusion-induced map from coherent centralizer cohomology to the full residual derived product. Every odd local coordinate is killed, including at three, by an integral determinant-corrected cocycle argument. The remaining ambient pointed space is the dyadic one. This does not evaluate the specified original coherent class: forgetting the centralizer permits changes of the positive factor frame.

### The exact elliptic cubic and the original boundary obstruction

A121 uses the full profinite section of Enriquez (2014, Proposition 2.20), applied only to established full-GT elements. Its separate ordered calculation proves a marked order-three identity from the original pentagon alone. The transported version retains every normalizing factor and every transformed pair. It supplies no elliptic action to an unproved GT pair or a merely GT-zero lift.

A122 embeds the original free pair as a literal free factor of an open index-two subgroup of the punctured-torus group. It identifies the original specified third-cusp conjugacy, the elliptic boundary-power equation, and the intertwining identity as equivalent conditions. Their exact normal obstruction is invariant under the original elliptic involution. These equivalent conditions remain unproved.

A123 proves that an endomorphism of the full free profinite rank-two group carrying the boundary commutator to a unit power is an automorphism. The proof uses actual finite punctured-torus covers and their integral boundary homology. For the candidate of A122, the still-unproved boundary equation would also imply automorphy of the original normalized map on the actual embedded free factor. No pro-p transfer or unverified discrete-retract assertion is used.

### Actual reduced elliptic torsion and unique derived transporters

A124 identifies the actual reduced three-strand elliptic braid group as the lift/orbifold group of the normalized torus configuration space. Its pure subgroup is free-three by free-two, with the full induced topology and all required goodness and cohomological-type hypotheses verified. An ordinary cellular cohomology argument gives a unique fixed vertex for each order-three subgroup of the lift group and excludes order two. The precise prime-order theorem and proof of Boggi and Zalesskii transfer the classification and centralizers to the full completion. There are four nontrivial finite-subgroup classes, all cyclic of order three, and eight nonidentity torsion-element classes distinguished by their nonzero abelian labels.

Each actual pentagon cubic therefore has a unique pure transporter from the fixed base cubic, continuously depending on the word. The actual elliptic involution gives a specified nonabelian C2 class and an actual commuting C6 extension. Constancy of that class does not prove it trivial or identify it with the original coherent CM frame.

A125 computes the actual pure integral abelianization as Z^4 using the relative homology of the three deleted subtori. The cyclic action has determinant nine after subtracting the identity and hence no full profinite invariant vector. This forces the unique transporter, and then the specified involution cocycle, into the closed pure derived subgroup. The entire C3 cohomology of that derived subgroup is trivial. The refined C2 class remains unevaluated; injectivity into the larger C2 cohomology space is not asserted.

### Whole one-sided and complementary contact images

B169 proves the full induced topology of the entire one-sided five-generator contact image by refining every finite target through actual whole-source maps. Its kernel is an exact continuous free profinite family, and the actual contact kernel maps onto it. B170 gives a literal continuous section and identifies the entire normal defect as the closed normal closure of the specified noncommuting contact. The section's exact action correction prevents an equivariance claim.

B171 proves that the two mirrored deletions have identical restrictions on the actual filled fixed source and its compact closure, including every finite refinement. They do not reduce the defect jointly. B172 uses a different actual retained map to show that the defect has an image containing the entire derived subgroup of a free profinite group of rank two; consequently every finite two-generated perfect group is a quotient.

B173 determines the full topology, exact normal kernel and continuous section of a complementary retained two-color contact target. Its proof separately extends every finite restriction through the original whole source, without asserting an unavailable signed action on the target quotient. It detects the first target's discarded defect and kills the mixed defect detected by that first target. The complete profinite family of normal translates identifies its retained image of the first defect. No original presentation of the full source or Main B fixed-generation equality follows.

### Sources, preservation and next work

All eleven entire formal proofs and their complete independent reviews were read before integration. The new Enriquez bibliography entry records the actual section/presentation/action proof scope, not an entire-paper read. The Boggi–Zalesskii application uses its complete needed prime-order proof; no fresh reading of the higher prime-power induction is claimed. The two citation-spacing corrections from checkpoint35 are limited to one space each, with all original owned and integrated bytes preserved.

Checkpoint35 was closed, verified by all three independent archive checks, and saved successfully. The sole next archive is checkpoint36 at 14:49:30 UTC, followed by checkpoint37 at 15:49:30 UTC. Its final PDF, prospective size and readiness checks are separate operations and are not certified by this source-integration report. Retention must compose all 163,040 inherited rows with all 10,746 parent35 logical files, for 173,786 rows. The original project remains incomplete; work continues on the based elliptic forgetting maps, the actual involution class, complementary source kernels and the controlled homeomorphism-filling boundary.
'''

def main():
    copies=[dict(statement=s,source=p,target=t,sha256=h) for s,p,t,h in SPECS]
    paths=[base+'.'+ext for base,kind in REVIEW_PAIRS for ext in (kind,'json')]
    reviews={p:sha(ROOT/p) for p in paths}
    all_reviews='\n'.join((ROOT/p).read_text() for p in paths)
    for row in copies:
        assert sha(ROOT/row['source'])==row['sha256']
        assert row['sha256'] in all_reviews
        assert not (ROOT/row['target']).exists()
    now=datetime.now(timezone.utc).isoformat()
    independent=dict(status='PASS_FINAL_SOURCES',recorded_at=now,
      root_read_all_complete_reviews=True,source_hashes={r['source']:r['sha256'] for r in copies},
      reviews=reviews,scope='All eleven complete formal proofs and all listed complete independent text/JSON reviews actually read. Not PDF visual approval.')
    paper=(ROOT/'LM4_SUCCESSOR_paper.tex').read_text()
    anchor=r'\input{sections/a_entire_residual_involution_cohomology.tex}'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+r['target']+'}' for r in copies[:6]))
    anchor='original coherent class or supply a full intertwining conjugator.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,anchor+'\n'+
      'The original pentagon now gives an exact reduced elliptic cubic.\n'
      'The actual torsion classification supplies a unique continuous\n'
      'transporter in the closed pure derived subgroup. The remaining\n'
      'boundary equation is exactly the specified original third-cusp\n'
      'conjugacy; it would imply automorphy of the original normalized\n'
      'map. A refined involution class is constant but remains unevaluated.\n'
      'Forgetting the odd coherent centralizers kills all their local\n'
      'cohomology coordinates without evaluating the original frame.')
    anchor='The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
    assert paper.count(anchor)==1
    paper=paper.replace(anchor,
      'Two entire complementary contact quotients now have proved full\n'
      'induced topology, exact normal restriction kernels and literal\n'
      'continuous sections. Each detects a specified defect erased by\n'
      'the other. The first defect also has a retained image containing\n'
      'the full derived subgroup of a free profinite rank-two group.\n'+anchor)
    part_b=(ROOT/'sections/part_B.tex').read_text()
    part_b+=''.join(r'\input{'+r['target']+'}\n' for r in copies[6:])
    register=(ROOT/'code/assemble_register.py').read_text()
    register=register.replace('{105,109,110,111,112,113,117,119}', '{105,109,110,111,112,113,117,119,120,124,125}')
    register=register.replace('{106,107,108,114,115,116,118}', '{106,107,108,114,115,116,118,121,122,123}')
    register=register.replace('banswers={167:', "banswers={"+','.join(str(n)+":'B.4;B.4.a;B.4.b;B.4.c;B.4.h'" for n in range(169,174))+',167:')
    marker="parts=['sections/b_sources.bib',"
    assert register.count(marker)==1
    register=register.replace(marker,"parts=['sections/a_elliptic_sources.bib','sections/b_sources.bib',")
    with (ROOT/'task_coverage.csv').open(newline='') as stream:
        reader=csv.DictReader(stream);fields=reader.fieldnames;tasks=list(reader)
    assert len(tasks)==49
    outcomes=[(r['task'],r['outcome']) for r in tasks]
    for row in tasks:
        selected=[]
        if row['task'] in {'A.4','A.5','A.7','A.8'}:
            selected+=['A.121','A.122','A.123']
            row['state']+=' Cycle36: the original pentagon gives an exact marked elliptic cubic. The original third-cusp condition is equivalent to the elliptic boundary-power and intertwining equations; if it holds, the actual normalized original free-factor map is an automorphism.'
            row['approaches']+=' Full profinite elliptic section at its established domain; literal ordered pentagon cancellation; actual index-two Schreier free factor; finite punctured-torus cover homology and Hopficity.'
            row['obstruction']='The original elliptic boundary/third-cusp equation remains unproved. The pentagon-only cubic does not supply that equation, the original full hexagon or a CM value.'
            row['next_step']='Use the actual torsion transporter and based strand-forgetting maps to constrain the specified boundary defect and original coherent frame.'
        if row['task'] in {'A.6','A.7','A.8'}:
            selected+=['A.120','A.124','A.125']
            row['state']+=' A120 computes the actual odd-coordinate forgetting map. A124 classifies all completed reduced elliptic torsion and gives a unique continuous pure transporter. A125 forces it and the specified involution cocycle into the closed pure derived subgroup and proves its whole C3 cohomology trivial.'
            row['obstruction']+=' The refined C2 class is constant but remains unevaluated. Neither its triviality nor identification with the original coherent/CM frame is asserted.'
        if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
            selected+=['B.'+str(n) for n in range(169,174)]
            row['state']+=' Cycle36: the entire one-sided contact image has full induced topology and a literal continuous section. Its exact normal defect survives in a complementary retained target, also fully determined. Mirrored deletions have equal restrictions. The defect has a retained image containing the entire derived free-two subgroup.'
            row['approaches']+=' Exact two-cyclic-edge presentations; compact cyclic intersection; induced finite permutation refinements; whole signed-source characteristic kernels with explicit m-order factor; continuous free families and universal inverse maps.'
            row['obstruction']='The complementary targets determine exact quotient kernels and non-equivariant sections, not a presentation of the original full source or equality with the entire fixed/cohomology fiber.'
            row['next_step']='Compare the joint retained kernels and all mixed contacts against the actual entire fixed/cohomology fiber.'
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
    spacing=[('work_DE/A119_entire_residual_involution_cohomology_proposed.tex','work_DE/spacing_proposals36/1_A119_entire_residual_involution_cohomology_proposed.tex'),
      ('sections/a_entire_residual_involution_cohomology.tex','work_DE/spacing_proposals36/2_a_entire_residual_involution_cohomology.tex'),
      ('sections/editorial.tex','work_DE/spacing_proposals36/3_editorial.tex')]
    for old,new in spacing:
        before=(ROOT/old).read_text();after=(ROOT/new).read_text()
        needle='own factor.\\citep' if '119' in old or 'involution_cohomology' in old else 'page~159.\\cite'
        assert before.count(needle)==1 and after==before.replace(needle,needle.replace('.\\','. \\'))
    bibsrc=ROOT/'work_A/A_elliptic_sources36.bib'
    assert sha(bibsrc)=='a3ccb33e1c3c6114ab853312aeb1dc81c0b21b172da44753407a3ae4b03b5600'
    backup=ROOT/'records/pdf_qa/checkpoint36_before_integration';assert not backup.exists()
    oldpaths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
    oldpaths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','code/assemble_register.py']
    oldpaths+=[old for old,new in spacing]
    oldpaths+=[str(p.relative_to(ROOT)) for p in (ROOT/'records').glob('build_*.log')]
    for rel in oldpaths:
        src=ROOT/rel
        if src.is_file():
            suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
            dest=backup/(rel+suffix);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
    for row in copies:(ROOT/row['target']).write_bytes((ROOT/row['source']).read_bytes())
    for old,new in spacing:(ROOT/old).write_bytes((ROOT/new).read_bytes())
    (ROOT/'sections/a_elliptic_sources.bib').write_bytes(bibsrc.read_bytes())
    for rel,value in [('LM4_SUCCESSOR_paper.tex',paper),('sections/part_B.tex',part_b),('LM4_SUCCESSOR_report.md',report),('code/assemble_register.py',register),('records/thirty_sixth_hour_research_report.md',REPORT)]:
        (ROOT/rel).write_text(value)
    with (ROOT/'task_coverage.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
    subprocess.run([sys.executable,str(ROOT/'code/assemble_register.py')],check=True)
    rows=list(csv.DictReader((ROOT/'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows)==383 and dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':339,'Refuted':19,'Open':19}
    bib=ROOT/'LM4_SUCCESSOR_references.bib';assert len(re.findall(r'^@',bib.read_text(),re.M))==117
    for name,data in [('independent_review_manifest',independent),('root_formal_reviews',dict(status='PASS_COMPLETE_SOURCE_REVIEW',recorded_at=now,reviewer='/root',copies=copies,independent_reviews=reviews,bibliography=dict(path=str(bib.relative_to(ROOT)),sha256=sha(bib),entries=117,scope='Enriquez actual presentation, action and all five parts of Proposition2.20; Boggi–Zalesskii complete needed prime-order proof. No entire-paper or higher-prime-power fresh-read claim.'),remaining_open=['Main A','Main B','Actual CM parity','Original coherent class','Local contact-image equality'])),('formal_source_copies',dict(integrated_at=now,copies=copies,comparison='All eleven integrated proofs byte-identical to completely reviewed candidates.',spacing_corrections=[dict(target=old,source=new,sha256=sha(ROOT/old)) for old,new in spacing]))]:
        with (ROOT/('records/checkpoint36_'+name+'.json')).open('x') as stream:json.dump(data,stream,indent=2);stream.write('\n')
    print('Integrated11 reviewed proofs:383 statements339Proved19Refuted19Open6Known;117references49tasks. MainA/MainB/actualCM remainOpen.',flush=True)

if __name__=='__main__':main()
