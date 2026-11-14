from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
a=root/'A.tex';e=root/'E.tex'
s=a.read_text()
s=s.replace('These assertions include the empty groupoid and the degenerate topos.', 'These assertions include the empty groupoid and the degenerate topos. These, and only these, are the multi-Galois topoi of Definition~1.2.')
s=s.replace('In the third condition it suffices to preserve coproducts and coequalizers,', 'Definition~1.6 calls an object with these equivalent properties a universal cover. In the third condition it suffices to preserve coproducts and coequalizers,')
s=s.replace('Thus a pointed universal cover is unique up to unique isomorphism;', 'These are the pointed universal covers of Definition~1.9. Thus a pointed universal cover is unique up to unique isomorphism;')
s=s.replace('(Refuted and corrected;', '(Refuted; corrected statement:')
a.write_text(s)
s=e.read_text()
s=s.replace('(Proved and delimited;', '(Proved; delimited statement:')
s=s.replace('(Refuted in general, with exact higher replacement;', '(Refuted; exact higher replacement:')
s=s.replace('(Refuted and corrected;', '(Refuted; corrected statement:')
s=s.replace('\\begin{center}\n\\small\n\\begin{tabular}{p{0.16\\textwidth}p{0.74\\textwidth}}', '\\begingroup\n\\small\n\\begin{longtable}{p{0.16\\textwidth}p{0.74\\textwidth}}')
s=s.replace('\\end{tabular}\n\\end{center}', '\\end{longtable}\n\\endgroup')
s=s.replace('The preceding congruence argument makes these data factor through a common finite quotient.', 'The continuous data in those degrees first give finite clopen partitions of compact spaces of composable arrow tuples. Because there are finitely many objects, these spaces are finite unions of products of compact zero-dimensional Hom spaces. Every finite clopen partition of such a product has a finite coordinatewise clopen refinement: cover each clopen cell by basic clopen rectangles and use compactness, then take the finite Boolean refinements in each coordinate. The preceding context-congruence argument now makes all these data factor through a common finite categorical quotient.')
e.write_text(s)
Ameta={
1:r'LM \S1, folio 1, scan 6 (1.1 and Definition 1.2)',
2:r'LM \S1, folio 1, scan 6 (1.1(a) and the marginal doubt)',
3:r'LM \S1, folio 1, scan 6 (1.1 and the proposed extra hypotheses)',
4:r'LM \S1, folio 1, scan 6 (1.1(c))',
5:r'LM \S1, folio 1, scans 6--7 (1.3--1.4)',
6:r'LM \S1, folios 1--2, scans 7--9 (1.5 and Definition 1.6)',
7:r'LM \S1, folios 2--3, scans 9--10 (1.7--1.10, including Definition 1.9)',
8:r'LM \S1, folio 3, scan 11 (1.11--1.12)',
9:r'LM \S2, folio 4, scans 12--13 (2.1--2.2)',
10:r'LM \S2, folio 5, scan 14 (2.3)',
11:r'LM \S2, folio 5, scans 14--15 (2.3)',
12:r'LM \S2, folio 5, scans 14--15 (2.3)',
13:r'LM \S4, folios 6--7, scans 16--18',
14:r'LM \S4, folio 7, scan 18 (application to fields)',
15:r'LM \S3, folio 6, scan 16',
16:r'LM \S3, folio 6, scan 16; \S2, folio 4, scan 12',
17:r'LM \S3, folio 6, scan 16; \S1, folios 1--3, scans 7--10',
18:r'LM \S3, folio 6, scan 16; \S7, folios 12--13, scans 28--30',
19:r'LM \S3, folio 6, scan 16; \S7, folios 12--13, scans 28--30',
20:r'LM \S1, folio 3, scan 11; \S3, folio 6, scan 16; PATHS E.13 test',
21:r'LM \S3, folio 6, scan 16; pro/ind qualifications in the task',
22:r'LM \S2, folio 4, scan 13 (Definition 2.2 and its tower)'}
Emeta={
1:r'LM \S2, folio 4, scans 12--13; \S3, folio 6, scan 16',
2:r'LM \S2, folio 4, scan 13 (the announced stages)',
3:r'LM \S2, folio 4, scans 12--13 (2.1--2.2)',
4:r'LM \S2, folio 4, scan 13 (local contractibility)',
5:r'LM \S1, folio 1, scan 6; \S2, folio 4, scan 12',
6:r'LM \S1, folios 1--3, scans 6--11; \S4, folios 6--7, scans 16--18',
7:r'LM \S16, folios 81--84, scans 163--170',
8:r'LM \S14, folio 63, scan 129; \S16, folio 83, scan 167',
9:r'LM \S14, folios 60--63, scans 123--129; cote 147, scans 179--180 (Remords)',
10:r'LM \S2, folio 4, scans 12--13; GALOIS B.3 comparison requested in Part E',
11:r'LM \S14, folios 64--67, scans 132--137; \S16, folios 85--88, scans 172--178; \S12, folios 50--53, scans 103--109',
12:r'Part E(c), the LM3b H.8--H.9 tests; cote 147, scan 179',
13:r'Part E(c), the STRATA A.1--A.3 qualification; LM \S2, folio 4, scan 13',
14:r'LM \S\S1--4, 12, 14, 16; exact passage references in the indexed statements'}
for file,prefix,meta in [(a,'A',Ameta),(e,'E',Emeta)]:
 s=file.read_text()
 for n,loc in meta.items():
  pattern=rf'(\\paragraph\{{{prefix}\.{n} \([^\n]*\}}\n)'
  replace=lambda m:m.group(1)+'\\textit{Manuscript: '+loc+'.}\n'
  if '\\textit{Manuscript: '+loc+'.}' not in s:
   s,count=re.subn(pattern,replace,s)
   assert count==1,(prefix,n,count)
 file.write_text(s)
print('Normalized statuses; inserted manuscript section/folio/scan references; E.14 uses longtable; expanded finite-coherence factorization.')
