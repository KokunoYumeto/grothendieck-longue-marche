import json,re
from pathlib import Path
w=Path(__file__).resolve().parents[1]
r=json.loads((w/'readers/scan008/record.json').read_text());r['scan']=8
for c in r['changes']:
 n=int(c['id'].split('-')[-1]);c['crop']=str(c.get('crop','')).replace(str(w)+'/','')
 c['marked_in_H']=bool(re.search(r'\\(?:uncertain|ill|illegible)\b',c.get('h','')))
 c['kind']='other'
 if n in {1,8,12,17,25,27,29,32,34,40,42}:c['kind']='misread word'
 if n in {5,9,11,19,28,31,33,43}:c['kind']='misread symbol or index'
 if n in {4,6,7,18,21,41}:c['kind']='omission'
 if n in {13,36}:c['kind']=r'readable ink left as \ill{}'
 if n in {14,15,37,39}:c['kind']='insertion or placement'
 if n in {20,22,26,30,35,38}:c['kind']='abbreviation expanded or spelling modernised'
 if n==23:c['kind']='misread word'
 if n in {1,11,17,27,28,29,42,43}:c['against_c']=True
 if n==33:
  c['final']=r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})\big\}$}'
  c['against_c']=False
  c['evidence']+=' Main reader: the two-lobed closing brace is clear, but a separate parenthesis is not independently distinguished; the reading without that extra parenthesis is preferred. The added alternative is a certainty qualification, not a C textual change.'
for d in r['doubts']:
 if d['place']=='condition reference ending':
  d['reading']=r'$1^{\circ}$ ou $2^{\circ}\big\}$';d['alternatives']=[r'$1^{\circ}$ ou $2^{\circ})\big\}$']
r['doubts']=[d for d in r['doubts'] if d['place']!='arc de S']
old=r'\unsure{$1^{\circ}$ ou $2^{\circ})\big\}$|$1^{\circ}$ ou $2^{\circ}\big\}$}'
new=r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})\big\}$}'
for b in r['second_boxes']:b['reading']=b['reading'].replace(old,new)
for i in r['inventory']:
 i['sheet_kind']='text';i['hand']='another unnamed hand' if 'archive' in (i.get('element','')+' '+i.get('position','')+' '+i.get('first_words_or_objects','')).lower() else 'his hand';i['transcribed']='yes'
r['reader_process_notes']=r['notes']
r['notes']=[
 'The page headed “Orientation d’un contour” describes an orientation by choosing an origin for each edge, with exactly one originating edge at each vertex. It states there are two orientations of a connected contour, constructs the associated vertex and edge advances u_omega and their inverses, and relates these to cyclic groups, torsors, and circular order. The final sentence continues onto the next leaf. No date, author page number, or page count is written; penciled archive numeral 7 is retained as a comment.',
 'Reading decisions: repeated omega has two rounded lobes and is resolved consistently with scans006–007. The cropped singular arc, lowercase or, avec, donc, singular élément, tte, and raised multiplication cross are retained. The short map shaft lacks a complete decisive arrowhead. The struck words and crowded interlinear annotation retain explicit alternatives. The visible closing brace after 2° has no corresponding opening set brace before g; none is supplied.',
 'Source slip at the edge definition: the ink says “l’unique arc de S”. The definition starts with a∈A and constructs u_omega(a), while sigma has domain A; the expected phrase is “arc de A”. S remains in the transcription.',
 'For a connected degree-two loopless graph, choosing one edge orientation forces the outgoing choice successively at each vertex. This gives the two directions on either a finite cycle or the bi-infinite path. The associated advance reverses when the orientation reverses; on a finite n-cycle its order is n. At n=2 the two orientations give the same advance on both the vertex and edge sets, explaining the exceptional equality without identifying the two orientation choices themselves.',
 'The asserted equivalence and characterization by conditions 1° and 2° again have the four-cycle counterexample recorded on scan006: one type of reflection moves every vertex to a neighbor but fixes two edges, while the other fixes vertices but moves every edge to an adjacent edge. Thus the two conditions individually are insufficient here; the two quarter-turns satisfy both. This conclusion uses the existing explicit certificate and does not alter the ink. The finite cyclic-order formulation is read with its stated n; the permitted n=1 torsor needs separate treatment if it is to correspond to the preceding loopless contour definition.'
]
r['check_events']=[
 {'statement_id':'scan008-two-orientations-and-advance','type':'targeted proof check','outcome':'A chosen direction propagates uniquely through each degree-two vertex on a connected cycle or bi-infinite path, giving precisely two choices. Reversing all directions inverts the vertex and edge advance; a finite n-cycle advance has order n, and n=2 identifies the two advances but not the two choices.'},
 {'statement_id':'scan008-adjacency-characterization','type':"refuted, with the refined statement's id",'outcome':'Rechecked the two square reflections recorded in scan006_square_certificate.json against the two conditions repeated here. They respectively satisfy only the vertex and only the edge condition. Refined statement id scan006-square-both-conditions: imposing both on the square leaves its two quarter-turns.'}
]
r['root_review']='Main reader inspected the whole scan and all 50 evidence crops, including all three drawings and added punctuation crops. First-reader resolutions are accepted; the closing-brace alternative is ordered without an unconfirmed separate parenthesis. Struck ambiguities remain. Pure added doubt does not count as a C text change.'
r['review_date']='2026-11-20';r['crop_count']=50
(w/'records/scan008.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(w/'pages/J75-01_75_scan008.tex').write_text((w/'readers/scan008/proposal.tex').read_text().replace(old,new))
with (w/'notation.md').open('a') as f:f.write('\n- Scan 008: the origin map is sigma:A→S; the two rounded omega bowls remain consistent. The operator is lowercase or. Literal exists1, autom, sss, tte and singular élément are retained. The raised cross before circulaire is multiplication-shaped, not a quotation mark. The source writes arc de S where its definitions require A.\n')
