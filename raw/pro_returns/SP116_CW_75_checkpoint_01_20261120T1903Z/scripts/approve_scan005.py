import json, shutil, datetime
from pathlib import Path
w=Path('/workspace/scratch/98070f078628/SP116_CW_75_work')
r=json.loads((w/'readers/scan005/record.json').read_text());r['scan']=5
word={1,2,9,24,26,27,29,30,32,36,37,46,49,51}
insert={11,16,17,20,33,34,35,38,39,40,42,44,45}
symbol={13,14,18,19,21,25}
abbr={7,22,47,48}
omission={8,10,23,50}
for c in r['changes']:
 n=int(c['id'].split('-')[-1]);c['kind']='misread word' if n in word else 'insertion or placement' if n in insert else 'misread symbol or index' if n in symbol else 'abbreviation expanded or spelling modernised' if n in abbr else 'omission' if n in omission else 'drawing or diagram' if n==12 else 'readable ink left as \\ill{}' if n==31 else 'other'
 if c.get('crop'):c['crop']=str(c['crop']).replace(str(w)+'/','')
 if n==36:c['math_note']='The heading reads Dualité, rather than H’s Dénombrement: it introduces exchanging vertices and edges in a contour.'
 if n==26:c['math_note']='The extra source f after qui is legible and retained, although the extension sentence is syntactically unfinished.'
for i in r['inventory']:
 i['sheet_kind']='text';old=i['hand'];i['hand']='another unnamed hand (archive numeral)' if i['element']=='archive' else 'another unnamed hand (pencil attribution uncertain)' if 'attribution non' in old else 'his hand'
r['notes']=[
'This page continues rectilinear realization, states that a finite graph admits one exactly when it is strict and that R³ suffices, gives general-position conditions on the vertices, and asserts unique rectilinear realization extending them. It then defines connected graphs, disjoint sums, multipolygonal graphs/contours, duality, and classification of nonempty connected contours by 2≤c≤ℵ₀. There is no date or author page number; the lower-left 4 is archival.',
'The marginal drawing has an open lower endpoint, a filled middle point, a gap, and a finer extension to a small dark endpoint; these were counted twice. The pencil three-point gloss has distincts inserted after points by a curved leader. The later nonempty insertion attaches after connexe. Each replacement of graphes polygonaux by contours retains its own cancellation and insertion state.',
'The visible comma in the first overlined x,y is retained. The manuscript writes ∃1, not an exclamation mark. The lower map shaft has a hook but no complete right arrowhead. The operator is retained as réll/réel/réal, ranked by the two high loop-like strokes. The isolated f after qui stays although the clause is unfinished; an upper trace beside prolonge may be a question mark, so that authorial-check possibility remains doubtful. The pencil abbreviation v.a./v.ex., cancelled donq/donc, inserted conn./connexes and final ssi/sss remain unresolved. No mathematical expectation supplies the missing arrowhead or changes these words.',
'Targeted check of the finite-graph realization claim: two distinct edges with identical endpoints would have the same straight segment, contradicting an embedding. Conversely, choose finitely many distinct points (t,t²,t³). Vandermonde determinants give no three collinear and no four coplanar; hence segments with disjoint endpoints do not intersect and segments sharing one endpoint meet only there. This proves the claimed existence in R³ for the strict graph. The unique-extension phrase presupposes the affine realization of each coordinate segment; a condition on the image alone would not uniquely specify its parametrization.',
'Targeted check of the contour classification: following the two incident edges at each vertex of a connected loopless degree-two graph either closes into a finite cycle (including two vertices joined by two edges) or continues as a doubly infinite path. Connectedness leaves no other vertices. Thus its cardinal is an integer at least 2 or ℵ₀, vertices and edges have equal cardinal, and strictness excludes exactly the two-vertex case. Exchanging the two incidence sets preserves degree two, which explains the ink’s heading Dualité.'
]
r['check_events']=[
{'statement_id':'scan005-rectilinear-finite','type':'targeted proof check','outcome':'Verified both directions under the stated meaning of rectilinear embedding. Parallel edges obstruct it; moment-curve vertices in R³ have no three collinear or four coplanar by Vandermonde, so their edge segments only meet at shared endpoints. Uniqueness of the extension requires the affine parametrization implicit in coordinate-segment realization; the source wording is retained.'},
{'statement_id':'scan005-contour-classification','type':'targeted proof check','outcome':'Following degree-two incidence in a connected loopless graph gives a finite cycle (two-vertex double edge allowed) or a doubly infinite path, exhausting the graph by connectedness. Therefore 2≤card S=card A≤ℵ₀ and strictness is equivalent to card S≠2.'},
{'statement_id':'scan005-contour-duality','type':'used and rechecked in this run','outcome':'Both vertices and edges have incidence degree two for a contour; exchanging them again gives a contour. This is consistent with the crop-supported heading Dualité, without using the mathematics to invent its letters.'}
]
r['root_review']='Main reader inspected the whole scan and all 67 retained evidence crops, including every returned unresolved place and every reading differing from a witness. All proposed readings accepted with their explicit alternatives. Drawing endpoints, gap and stroke weights were counted twice. The attempted redundant crop subdivisions were stopped and discarded without changing a reading. The first-pass crop files and original boxes are preserved.'
r['review_date']='2026-11-20';r['crop_count']=67
(w/'records/scan005.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
shutil.copyfile(w/'readers/scan005/proposal.tex',w/'pages/J75-01_75_scan005.tex')
with (w/'notation.md').open('a') as f:
 f.write('\n- Scan 005: `\\exists 1` is again literal; endpoint segments are `\\overline{x,y}` with commas where visible. A lower hooked shaft lacks a complete arrowhead and is left as `\\lhook\\joinrel-`.\n- Scan 005: the empty-set marks here are slashed ovals (`\\varnothing`), distinct in shape from the stemmed phi on scan003. No silent glyph substitution is made.\n- Scan 005: `conn.`, `géom`, `réalis`, `il f et s`, `isom.` remain abbreviations; the g descender in segment is not an underline.\n')
print('approved scan005',len(r['changes']))
