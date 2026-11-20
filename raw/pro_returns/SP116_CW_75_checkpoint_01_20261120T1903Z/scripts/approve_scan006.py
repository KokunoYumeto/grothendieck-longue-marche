import json, shutil, datetime
from pathlib import Path
w=Path(__file__).resolve().parents[1]
r=json.loads((w/'readers/scan006/record.json').read_text());r['scan']=6
for c in r['changes']:
    n=int(c['id'].split('-c')[1])
    c['kind']='other'
    if n in {1,6,8,13,23,26,27}:c['kind']='insertion or placement'
    if n in {7,17,21,28,32,33,36,39}:c['kind']='misread symbol or index'
    if n in {3,5,18,25,43,44,46,48,49}:c['kind']='misread word'
    if n in {10,11,12,15,19,24,30,31,35}:c['kind']='readable ink left as \\ill{}'
    if n in {14,20}:c['kind']='deletion state (struck given live or live given struck)'
    if n in {22,34,37,40,41,42,47}:c['kind']='abbreviation expanded or spelling modernised'
    if n==50:c['kind']='drawing or diagram'
    if n in {9,10,11,24,25,30,31,32,34,35,36,43}:c['against_c']=False
    c['marked_in_H']=n in {6,10,11,12,15,17,18,19,24,30,31,32,33,35,36,42}
    if n in {10,11}:c['h']=r'\struck{\ill{}} (part of the cancelled predication)'
    if n==39:
        c['final']=c['c'];c['against_c']=False
        c['evidence']='The connector is a short horizontal shaft with a small terminal nub; no two-wing arrowhead is separately clear. The dash remains the first candidate and an arrow the alternative. The whole formula was inspected together. Existing crop scan006_aut_arrow.jpg, original box [837, 1232, 1626, 1313].'
    if n==7:c['math_note']='The long descending stem through a small bowl is the phi-shaped empty-set glyph; this differs from the slashed oval of scan005.'
r['changes']=[c for c in r['changes'] if c['id'] not in {'scan006-c09','scan006-c51'}]
for d in r['doubts']:
    if d['place']=='c Aut action formula':
        d['reading']=d['reading'].replace(r'\unsure{\to|-}',r'\unsure{-|\to}')
        d['alternatives']=['-',r'\to']
for b in r['second_boxes']:
    b['reading']=b['reading'].replace(r'\unsure{\to|-}',r'\unsure{-|\to}')
for i in r['inventory']:
    i['sheet_kind']='text'
    i['hand']='another unnamed hand (archive numeral)' if 'archive' in i['element'] else 'his hand'
r['notes']=[
 'The page continues the classification by proper subgroups H of Z and is headed Orientation d’un contour. It proposes two equivalent conditions for an automorphism to be an orientation, the two orientations and their inverse relation, the orientation-preserving subgroup, and a semidirect-product description of the automorphism group. The small left figures have two vertices/two arcs and five corners/five sides respectively. There is no date or author page number; the lower-left 5 is archival.',
 'The marginal d’orientation is live and double-underlined, whereas C deleted it. Strict above the proposition is an insertion subsequently cancelled. The sentence Si g∈ω(X), on a g⁻¹∈ω(X) is a complete interlinear addition. The separate strictness parenthesis attaches to the cardinal-two assertion; its c-like mark and equality remain in the ink despite H’s omission. The first ω is resolved from its two rounded lobes. The empty-set mark has a long stem through a small bowl and is transcribed as phi. Abbreviations hom, ss-grpe and tt remain unexpanded; the half symbol in produit 1/2 direct is literal.',
 'The cancelled definition of Aut⁺ retains its incomplete [i.e. and its crossed word/formula doubts. The action connector remains dash/arrow because the terminal nub does not settle an arrowhead. In the corollary the compact mark after H admits est or an arrow; etant/étant/étans/dans and fixé/fixée remain unresolved. Mathematics and agreement would favour a verbal construction and feminine ending, but do not override these letter shapes.',
 'The asserted equivalence of conditions 1° and 2° fails for the square under adjacency of distinct vertices or edges. Number the vertices 0,1,2,3 cyclically. The reflection (0 1)(2 3) sends every vertex to a neighbour, satisfying 1°, but fixes the edges {0,1} and {2,3}, violating 2°. The reflection (1 3) fixes vertices 0 and 2, violating 1°, but sends each edge to a distinct incident edge, satisfying 2°. Exhaustive enumeration of the eight square automorphisms confirms four satisfying each separate condition and only the two quarter-turns satisfying both. For this square the refined statement is to require both conditions. The source’s Conditions équiv. and subsequent cardinal assertion remain unchanged. This is a mathematical counterexample, not grounds to revise the ink.',
 'The semidirect-product claim is recorded as the page’s claim, without being independently proved here. Its relationship to the stated definition requires care after the square counterexample; the computation certifies only the finite square and does not silently repair the proposition for every contour.'
]
r['check_events']=[
 {'statement_id':'scan006-orientation-conditions','type':'computation or formal certificate','outcome':'Enumerated all 24 permutations of four vertices, retaining the eight automorphisms of C4. Four satisfy condition 1, four satisfy condition 2, and only two satisfy both. Reproducible script scripts/check_scan006_square.py; full result records/scan006_square_certificate.json.'},
 {'statement_id':'scan006-orientation-conditions','type':'refuted, with the refined statement\'s id','outcome':'Refuted under distinct-adjacency convention by g=(0 1)(2 3) and the dual reflection (1 3). Refined statement scan006-square-both-conditions: for the square, requiring both conditions gives exactly the two inverse quarter-turns; certified by the enumeration.'}
]
r['root_review']='Main reader inspected the whole scan and all 55 evidence crops, including every unresolved return and every disagreement. The two drawings were counted again: two endpoints/two arcs, and five corners/five sides with retraced edge and corner hooks. The proposed action connector ranking was changed back to dash/arrow on the existing crop. New doubt alone does not count as a change against C; the archive numeral and the pure Un certainty change are documented outside the changes table.'
r['review_date']='2026-11-20';r['crop_count']=55
(w/'records/scan006.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
page=(w/'readers/scan006/proposal.tex').read_text().replace(r'\unsure{\to|-}',r'\unsure{-|\to}')
(w/'pages/J75-01_75_scan006.tex').write_text(page)
with (w/'notation.md').open('a') as f:
    f.write('\n- Scan 006: `\\omega(X)` has two rounded lobes, resolving the first omega/w doubt. `\\phi` for the empty set again has a long stem through a small bowl. `tt`, `hom`, and `ss-grpe` remain unexpanded. The corollary writes a literal `1/2` in “produit 1/2 direct”.\n')
assign=json.loads((w/'records/assignments.json').read_text());assign['10']='reader_c';(w/'records/assignments.json').write_text(json.dumps(assign,indent=2))
print('approved',r['scan'],len(r['changes']))
