#!/usr/bin/env python3
"""Assemble the audited result register, bibliography, and progress report.

This script checks correspondence with actual numbered LaTeX claims. It does
not prove those claims: their proofs and independent reviews are in the paper.
Run from any directory. Output is reproducible from the component ledgers.
"""
from pathlib import Path
from collections import Counter
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]

ROOT_CLAIMS = [
 ('D.1','Known','Universal birational liftability over all finitely generated characteristic-zero fields is equivalent to the section conjecture; the t-birational theorem has its transcendental-extension hypothesis.','Bresciani Theorems A and B'),
 ('D.2','Proved','D2 and D4 imply D1 and Conjecture A for the three-punctured projective line over Q.','D.1; R15 with its cyclotomic centralizer hypothesis'),
 ('D.3','Proved','The completion of Q* consists of a sign and restricted profinite valuation vectors; local rationality and cofinite unit integrality characterize its diagonal rational elements.','Elementary Kummer theory and valuation coordinates'),
 ('D.4','Refuted','Ordinary evaluation at a zero or pole cannot replace tangential Kummer evaluation; the example at t=0 with tangent class 2 gives values 2,-1,1 for t,t-1,t+1.','Local Kummer decomposition'),
 ('D.5','Known','Uniform almost-everywhere integral adelic support implies rational or cuspidal origin under the exact hypotheses of the opened Stix and finite-descent theorems.','Stix 2015 Corollaries 5 and 6; Stoll 2007 Theorem 8.2 and errata; Harari-Stix preprint Theorem 2.1 and Remark 2.2(1)'),
 ('D.6','Proved','If the unrefereed proper p-adic local assertion R24 holds, it implies the stated affine point-or-cusp assertion by characteristic neighborhoods and compactness.','R24 as an explicitly conditional hypothesis; proper covers of genus at least two'),
 ('D.7','Proved','An abstract finite-involution twist gives a discontinuous semilinear action normalizing the usual deck group and with exactly one cyclotomic-kernel-fixed completed pro-point.','Ribet cyclotomic torsion finiteness; local abelian-variety Kummer injectivity'),
 ('D.8','Proved','An automorphism changing the constants cannot alone be used as a semilinear cocycle for the specified G_Q action.','Definition of semilinearity'),
 ('D.9','Proved','A finite embedding problem can have split abelianized kernel and no splitting: the nonsquare semilinear extension of PSL2(F9) by C2 has no involution outside its perfect kernel.','Elementary matrix and determinant calculation; code/D_embedding_obstruction.py'),
 ('D.U1','Unresolved','Every noncuspidal section over Q of P1 minus three points is the section of a rational point.','D.2; D.5; D.6'),
 ('D.U2','Unresolved','Every continuous section of G_Q(t) to G_Q lies in the decomposition group of a rational place.','D.3; D.4; D.5'),
 ('D.U3','Unresolved','Every section of every hyperbolic curve over a field finitely generated over Q admits a compatible birational lift.','D.1; D.9'),
 ('D.U4','Unresolved','Every section for P1_Q minus three points admits a birational lift.','D.1; D.2; D.9'),
 ('E.1','Proved','The Artin-Schreier torsor z^p-z=tx does not descend from the extended algebraically closed field; the exact full-path marking category cannot be invariant under base extension.','Artin-Schreier principal parts; ordered M_0,4 and its finite étale unordered cover'),
 ('E.2','Refuted','There is no type-preserving specialization functor from the entire characteristic-zero covering category into the prime-to-p-Galois-closure category preserving covering arrows.','A connected étale cyclic degree-p cover of a proper genus-two curve and Riemann-Hurwitz'),
 ('E.3','Known','For a fixed smooth marked curve, the prime-to-p finite-cover categories have the stated base-extension and specialization comparisons, preserving degrees and types.','SGA1 XIII 2.12, 4.3, Examples 4.4, 4.5.3; Bertin-Romagny 6.9, 6.14, 6.20'),
 ('E.4','Known','The opened Hoshi-Mochizuki-Tsujimura criterion identifies conjugates of G_Q as maximal closed arithmetically ample subgroups of GT, with its extra axioms retained.','Hoshi-Mochizuki-Tsujimura 2025 Definition 5.12 and Theorem 5.17(ii)'),
 ('E.5','Proved','The generated fixed-diagram isotopy relation defines a category of covers and puncture fillings, with mapping class automorphism groups, faithful pure covering subcategory, and finitely many source orbits in each Hom set.','Euler-characteristic degree/defect identity; finite-index subgroup classification; isotopy extension for finite configurations'),
 ('E.6','Proved','That diagram-isotopy category has a universal Hausdorff profinite envelope, with Hom spaces finite unions of closed-stabilizer coset spaces and jointly continuous composition.','E.5; finite-index lifting groups; extension of finite quotient actions'),
 ('E.7','Proved','The family (z^3-3z+t)^2 gives equal classes for the generated diagram-isotopy relation while its two-sided source/target orbit changes.','E.5; explicit ramification and puncture calculation'),
 ('E.U2','Unresolved','Characterize the image of G_Q in the compatible outer automorphisms of the completed all-types curve category using the requested intrinsic data.','E.4; compatibility with all covering and puncture-filling operations'),
 ('G.1','Proved','A continuous profinite homomorphism is injective exactly when every transitive finite source-group set is an orbit, equivalently a quotient of an orbit, in a finite target-group set; this proves the precisely typed local covering-germ criterion.','SGA1 V Corollary 6.8; XIII Propositions 5.1 and 5.2; strict henselian normal crossings chart'),
 ('G.2','Proved','The germ criterion gives injection at a coordinate torus, failure at infinity of A1, and the map (a,b) to a-b with diagonal kernel for P2 minus two lines at their crossing.','G.1; Riemann-Hurwitz; Kummer valuation calculation')
]

def root_rows():
    rows=[]
    for ident,status,statement,deps in ROOT_CLAIMS:
        letter=ident[0]
        section={'D':'D','E':'E','G':'local_lead'}[letter]
        if letter=='D':
            passage='149; manuscript pp.22-31, 62v-63; scans45,48,56,59-63,126-127'
            doubtful='Scan126: I_V versus N_V remains doubtful; the crossed ce is excluded. No proof depends on resolving that ink.' if ident in {'D.1','D.2','D.U2','D.U3','D.U4'} else 'None; no doubtful reading is used as a premise.'
        elif letter=='E':
            passage='142; manuscript pp.7-10; scans15-21'
            doubtful='No doubtful word is used as a mathematical premise; the isotopy proposal is explicitly tentative.'
        else:
            passage='Additional lead of 13 November 2026; comparison with 149, manuscript pp.36v-38v,44v; scans74-78,90'
            doubtful='The lead is mathematically typed using a geometric local point and strict henselization.'
        rows.append(dict(id=ident,statement=statement,status=status,
            where_proved=f'sections/{section}.tex, statement {ident} and its proof or explicit remaining obligation',
            depends_on=deps,manuscript_passages=passage,doubtful_reading=doubtful,
            notes='Unresolved does not mean known to be open in the literature; it records an obligation not proved or refuted in this return.' if status=='Unresolved' else 'Scope and comparison maps are part of the statement and proof; no priority is claimed.'))
    return rows

def cell(value):
    if isinstance(value,list): return '; '.join(map(str,value))
    if value is False or value is None: return 'None'
    return str(value)

def canonical(value):
    if value.startswith('Refuted'): return 'Refuted'
    if value.startswith('Proved'): return 'Proved'
    if value.startswith('Known'): return 'Known'
    return 'Unresolved'

def main():
    (ROOT/'audit/root_results.json').write_text(json.dumps(root_rows(),indent=2,ensure_ascii=False)+'\n')
    rows=[]
    for name in ['A_results.json','A_char2_results.json','BC_results.json','root_results.json','D_extension_results.json','D_ultralimit_results.json','E_extension_results.json','E_tame_results.json','F_results.json']:
        path=ROOT/'audit'/name
        if path.exists(): rows.extend(json.loads(path.read_text()))
    assert len({r['id'] for r in rows})==len(rows),'Duplicate result ID'
    identifiers={r['id'] for r in rows}
    texids=[]
    for path in sorted((ROOT/'sections').glob('*.tex')):
        texids.extend(re.findall(r'\\begin\{claim\}\{([^}]+)\}',path.read_text()))
    assert len(set(texids))==len(texids),'Duplicate LaTeX claim ID'
    assert set(texids)==identifiers, {'ledger_only':sorted(identifiers-set(texids)), 'paper_only':sorted(set(texids)-identifiers)}
    fields=['id','statement','status','where_proved','depends_on','manuscript_passages (cote; page; scan)','depends_on_doubtful_reading (scan, alternatives)','notes']
    with (ROOT/'ANABELIAN_149_PUSH_results.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=fields);writer.writeheader()
        for row in rows:
            writer.writerow(dict(zip(fields,[row['id'],row['statement'],canonical(row['status']),row['where_proved'],cell(row.get('depends_on',[])),cell(row.get('manuscript_passages','')),cell(row.get('depends_on_doubtful_reading',row.get('doubtful_reading','None'))),cell(row.get('notes',''))])))
    def tex_escape(s):
        return ''.join({'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in s)
    loci=[r'\section*{Numbered statements and manuscript loci}',r'\addcontentsline{toc}{section}{Numbered statements and manuscript loci}',
          'This register assigns the manuscript locus to every numbered statement. The CSV supplies the dependencies and the exact qualifications about doubtful readings. Repeated loci identify the question being answered; they do not attribute our proofs to the manuscript.',
          r'{\small',r'\begin{longtable}{p{1.9cm}p{1.7cm}p{10.3cm}}',r'\toprule Statement & Status & Cote; manuscript page; scan \\ \midrule\endhead']
    for row in rows:
        passage=cell(row.get('manuscript_passages',''))
        if row['id'] in {'D.10','D.11'}: passage='149; manuscript pp.29-31; scans59-63'
        if row['id'] in {'E.8','E.9'}: passage='142; manuscript pp.8v-10; scans18-21'
        loci.append(tex_escape(row['id'])+' & '+canonical(row['status'])+' & '+tex_escape(passage)+r' \\')
    loci.extend([r'\bottomrule\end{longtable}',r'}'])
    (ROOT/'audit/statement_loci.tex').write_text('\n'.join(loci)+'\n')
    bibs=sorted((ROOT/'sources').glob('*_refs.bib'))
    bibtext='\n\n'.join(p.read_text().strip() for p in bibs)+'\n'
    bibkeys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',bibtext)
    assert len(set(bibkeys))==len(bibkeys),'Duplicate bibliography key'
    cited=set()
    for path in (ROOT/'sections').glob('*.tex'):
        for block in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',path.read_text()):
            cited.update(k.strip() for k in block.split(','))
    assert not cited-set(bibkeys),f'Missing bibliography keys: {cited-set(bibkeys)}'
    for block in re.split(r'(?=@\w+\s*\{)',bibtext):
        if block.lstrip().startswith('@'): assert re.search(r'opened',block,re.I),block[:100]
    (ROOT/'ANABELIAN_149_PUSH_references.bib').write_text(bibtext)
    coverage=[
      dict(item='A1',status='Unresolved',statement_ids=sorted(x for x in identifiers if x.startswith('A.')),remaining_obligation='Universal proper-curve point separation in every genus and characteristic; proved special cases do not finish A1.'),
      dict(item='A2',status='Unresolved',statement_ids=['A.1','A.2','A.3','A.4'],remaining_obligation='The covering conditions are proved equivalent to section-class equality; their universal implication P=Q remains the A1 problem.')]
    coverage.extend(json.loads((ROOT/'audit/BC_coverage.json').read_text()))
    for i in range(1,5):
        coverage.append(dict(item=f'D{i}',status='Unresolved',statement_ids=({'1':['D.2','D.5','D.6','D.U1'],'2':['D.3','D.4','D.5','D.U2'],'3':['D.1','D.9','D.U3'],'4':['D.2','D.9','D.U4']})[str(i)],remaining_obligation='The requested universal continuous section assertion is neither proved nor refuted.'))
    coverage.append(dict(item='D5',status='Refuted; second demand proved',statement_ids=['D.7','D.10','D.11','D.12','D.13','D.14'],remaining_obligation='An explicit abstract cocycle has empty cyclotomic-kernel fixed set and is provably discontinuous. A separate cocycle normalizes no finite-quotient deck group and has exactly one fixed cusp. Both demands are settled; D1-D4 concern continuous sections and are unaffected.'))
    coverage.extend([
      dict(item='E1',status='Refuted as requested; corrected construction proved',statement_ids=['E.1','E.2','E.3','E.10','E.11','E.12'],remaining_obligation='The literal full-path base invariance and unrestricted specialization are false. The boundary-tame all-types category, faithful actual covers, base invariance, and restricted specialization with all automorphism and Hom maps are proved.'),
      dict(item='E2',status='Unresolved',statement_ids=['E.4','E.U2'],remaining_obligation='The intrinsic all-types arithmetic-image characterization remains; the exact genus-zero arithmetically-ample criterion is supplied.'),
      dict(item='E3',status='Proved',statement_ids=['E.5','E.6','E.7','E.8','E.9'],remaining_obligation='The algebraic comparison is with the explicitly Hausdorff presentation by etale diagram paths and a closed congruence; no assertion about the naive unseparated quotient is needed.'),
      dict(item='F1',status='Proved after definition repair; literal R27 refuted',statement_ids=['F.1','F.3','F.4','F.5','F.6','F.7'],remaining_obligation='The intended closed-point-preserving F.50 is proved. No exact prior publication of F.47/F.50 was located; no novelty is inferred.'),
      dict(item='F2',status='Qsolv all-scheme reconstruction proved; intrinsic field classification unresolved',statement_ids=['F.1','F.2','F.8','F.9']+[f'F.{i}' for i in range(16,32)],remaining_obligation='The literal relative-only assertion is refuted by F.17. With closed-point preservation restored, F.23 settles the unique c*t^m endomorphism theorem, and F.26-F.31 prove reconstruction for all finite-type schemes over every finite extension of Qsolv. The proof controls the Picard Tate component through finite-point detection and arithmetic semiabelian Tate-Hom, then applies the exact CHW criterion. The intrinsic arithmetic classification of all reconstruction fields remains unresolved.'),
      dict(item='F3',status='Proved',statement_ids=['F.10','F.11','F.12','F.13','F.14','F.15'],remaining_obligation='The eight-row comparison retains geometric hypotheses and refutes the stated arbitrary-section extensions.'),
      dict(item='Additional local-germ lead',status='Proved',statement_ids=['G.1','G.2'],remaining_obligation='The exact geometric local interpretation is stated; injectivity is a criterion, not a universal assertion.')])
    def order(item):
        m=re.fullmatch(r'([A-FL])(\d+)',item)
        return ('ABCDEFGHIKL'.index(m.group(1)),int(m.group(2))) if m else (99,0)
    coverage.sort(key=lambda r:order(r['item']))
    assert len(coverage)==43, len(coverage)
    expected={f'{p}{i}' for p,start,end in [('A',1,2),('B',0,14),('C',1,4),('D',1,5),('E',1,3),('F',1,3),('L',1,10)] for i in range(start,end+1)}|{'Additional local-germ lead'}
    assert {r['item'] for r in coverage}==expected
    (ROOT/'audit/coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')
    lines=['INCOMPLETE','','| Item | Outcome | Paper statements | Exact remaining obligation or qualification |','|---|---|---|---|']
    for r in coverage:
        state=r['status']
        if state.startswith('Partially'): state='Unresolved; specified cases proved'
        lines.append('| '+' | '.join([r['item'],state,', '.join(r['statement_ids']),r['remaining_obligation'] or 'None within the stated scope.']).replace('|','\\|')+' |')
    # Undo only the separator escaping introduced by the content join.
    lines=[s.replace(' \\| ',' | ') if s.startswith('| ') else s for s in lines]
    lines += ['','AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.','',
      'A proved special case does not complete an unresolved requested item. Unresolved here means not settled by this return; it is not a literature-wide assertion of openness.',
      '', '## Register and reproducibility', '',
      f'The current register contains {len(rows)} numbered statements: '+', '.join(f'{v} {k}' for k,v in sorted(Counter(canonical(r["status"]) for r in rows).items()))+'.',
      'The CSV and bibliography are regenerated by code/assemble_return.py, which checks the exact correspondence of ledger IDs with the numbered LaTeX claims, all 43 requested-item rows, citation keys, and opened/not-opened labels.',
      '', 'The component reports below preserve the routes, failures, source checks, and scope qualifications. They record the state when authored; the numbered paper and combined outcome table govern later strengthened conclusions.', '']
    for name in ['corrections_R1_R27.md','A_report.md','A_char2_report.md','BC_report.md','root_report.md','D_ultralimit_report.md','E_extension_report.md','E_tame_report.md','F_report.md','F_D5_construction.md','research_progress.md','typesetting_report.md','checkpoint_history.md']:
        path=ROOT/'audit'/name
        if path.exists(): lines.extend(['',path.read_text().strip(),''])
    (ROOT/'ANABELIAN_149_PUSH_report.md').write_text('\n'.join(lines)+'\n')
    result={'numbered_statements':len(rows),'statuses':dict(Counter(canonical(r['status']) for r in rows)),'coverage_rows':len(coverage),'bibliography_entries':len(bibkeys),'cited_keys':len(cited),'ledger_matches_paper':True,'all_citations_resolved':True}
    (ROOT/'code/assemble_return_output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
