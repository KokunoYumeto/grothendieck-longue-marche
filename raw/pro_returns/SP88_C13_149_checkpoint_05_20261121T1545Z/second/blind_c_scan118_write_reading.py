from pathlib import Path
import csv,json,hashlib
root=Path('/workspace/scratch/0cab6a548abb')
out=root/'edition/second'
readings=[
('b01',r"groupe d'inertie $\unsure{I|L}_{x'}$, avec"),
('b02',r"\margin{$I_{x'}$ \unsure{provient} d'un ``groupe \unsure{lent}''}"),
('b03',r"(26) $\mathcal N_{x'}/I_{x'}\simeq\unsure{k|\kappa}(x')$"),
('b04',r"(ext. de type fini de $K$, de degré de tr. $n-1$, si $n=\operatorname{deg\,tr}L/K$), et"),
('b05',r"(27) $I_{x'}\simeq T_{\unsure{\infty|0}}(\bar L)\simeq T_\infty(\bar K)$ --"),
('b06',r"\margin{si car. $k(x)$ est nulle -- sinon faire des \unsure{subtilités}...} de"),
('b07',r"(par Kummer) \deleted{Notons \unsure{enfin|bien} que}\inserted{Les considérations}"),
('b08',r"\unsure{ne|en} dépendent du choix d'aucun \deleted{\unsure{des|de}} \unsure{modèle|modele} $(U,\ldots X\ldots)$. Notons que"),
('b09',r"(28) $I_{\unsure{x'|x_1}}\subset\pi_{L/K}^{\bar L}$."),
('b10',r"En fait, on peut dire, posant"),
('b11',r"(29) $\left\{\begin{aligned}\widetilde S_{\unsure{x|n}}&=\operatorname{Spec}\widetilde V,\\\widetilde U_{\unsure{x|n}}&=\widetilde S_{\unsure{x|n}}\setminus\{\unsure{x|n}\}\simeq\operatorname{Spec}\widetilde{\deleted{\unsure{K}}\inserted{L}}_{\unsure{x|n}}\end{aligned}\right.$ $\widetilde V$ hensélisé (\unsure{pas|non} strict) de $V$ (où $\widetilde{\deleted{\unsure{K}}\inserted{L}}_{\unsure{x|n}}$ est le corps des fractions de $\widetilde V$) \inserted{ext}"),
('b12',r"de $V$) que l'on a un hom \inserted{ext} $\mathcal E_{\widetilde U_{\unsure{x|n}}}\longrightarrow\mathcal E_L$, \deleted{\unsure{(30)}} dont le choix ``effectif'' dépend de"),
('b13',r"\mspage{117}"),
]
ambiguities={
'b01':['The tall initial of the inertia symbol has an L-shaped lower stroke and an uncertain top: I versus L is preserved.','The prime is attached to x.'],
'b02':['The marginal verb is provisionally read provient, apparently divided across two short diagonal lines. The apparent dot near the end of the upper group may belong to i, not be a full stop. No hyphen has been supplied.','The quoted adjective is provisionally lent; its compressed middle strokes are not secure.'],
'b03':['The right-hand symbol resembles a tall k; k versus kappa is explicitly unresolved.','A diagonal slash is visible between the N term and the I term; it is transcribed as a quotient slash.'],
'b04':['The opening abbreviation is read ext. and is not expanded.','No inner opening parenthesis is visible immediately before L/K; none is supplied.'],
'b05':['The first T subscript resembles a small loop with a trailing stroke: infinity versus zero remains unresolved. The second T subscript shows two loops and is read infinity.','Bars over L and K are separately visible.','The final short horizontal mark is retained as a dash, without turning it into an arrow.'],
'b06':['The final marginal word is tentatively subtilités; the compressed middle strokes remain uncertain.','The formula in the first marginal line is read k(x), without adding a prime.'],
'b07':['The middle word in the cancelled phrase is obscured by the horizontal cancellation and the inserted line; enfin and bien are tentative alternatives.','The inserted line is read Les considérations.'],
'b08':['Initial short word may be ne or en.','The isolated cancelled word between the two main lines may be des or de.','The accent in modèle is not securely separable; accented and unaccented spellings are preserved as alternatives.','The short marks before and after X are read as ellipses; no extra separator or arrow has been supplied.'],
'b09':['The small mark following the subscript x is dense and could be a prime or a low 1.','The opening parenthesis of the label is retraced; the number itself reads 28.','The inclusion sign has no separately visible equality bar.'],
'b10':[],
'b11':['Several small index letters have an arch-shaped x/n form; the alternatives are retained explicitly.','The first S is heavily retraced or overwritten. Its final S shape is visible, but no earlier letter can be independently recovered.','Two field symbols show a heavy L over lighter diagonal strokes consistent with K. The lower-layer K is explicitly tentative, and the final L is preserved as the inserted layer.','The first word inside the henselization parenthesis is overwritten; pas versus non remains unresolved. No separate earlier word is reconstructed.'],
'b12':['The small U subscript has the same unresolved x/n form within this box.','The cancelled parenthesized item at the beginning of the lower line is tentatively (30); the intersecting descender and cancellation obscure the digits.','The quoted word is read effectif; the long f strokes are letters, not extra arrows.'],
'b13':[]
}
clipping={
'b01':['A tiny previous-line stroke at the upper edge is clipped and not completed.'],
'b02':['Along the right edge are incomplete main-text label parentheses/digits and a partial upper letter; none is completed from neighboring boxes.'],
'b03':['A short clipped upper-left marginal stroke is not expanded into a word.'],
'b04':['Small lower-edge strokes from the following formula are clipped and not completed.'],
'b05':['Tiny previous-line and left-edge fragments are not completed.'],
'b06':['The formula-label fragment at the upper right is clipped. Other main-text starts at the right are incomplete; the complete short word de at the lower right is retained.'],
'b07':['Fragments of the diagonal marginal note enter at the left edge and are clipped; no extra marginal words are completed.'],
'b08':['Very faint small outlines between lines are not securely identifiable as primary writing. No numeral is invented from them.'],
'b09':['The opening label-parenthesis stroke reaches the left crop boundary; the visible label is retained without reconstructing an earlier layer.'],
'b10':['Only upper parts of the next formula enter the lower edge; that formula is not completed here.'],
'b11':['Top-edge fragments from the preceding prose line and tiny bottom-edge following-line marks are clipped and excluded.','The insertion text ext is complete, but its insertion cue toward the following line is not complete within this box.'],
'b12':['The top adjacent context de V) is complete, but the upper accent above V is clipped; no complete tilde is supplied in this box.'],
'b13':['The black lower/left page border is not writing.']
}
layout={
'b02':'A diagonal marginal note, including its quotation marks; inspected at two rotations. The right-edge main-text fragments are separate from the note.',
'b04':'Two lines of prose, with one parenthesis beginning before ext. and closing after L/K.',
'b06':'Diagonal marginal prose; the separate complete main-text word de at the right is recorded outside margin.',
'b07':'A horizontal stroke cancels the baseline phrase. Les considérations is written above it as the replacement line. The Kummer parenthesis remains on the baseline to the left.',
'b08':'An isolated cancelled des/de lies below the initial short word and above the following line. It is recorded separately rather than made into surviving prose.',
'b11':'A left brace groups two formula lines. The henselization explanation is to the right of the first line. The field-of-fractions parenthesis follows the second line and continues below it. The separately written ext at the bottom is an adjacent insertion, not part of the preceding phrase de V.',
'b12':'The word ext is written above hom; a bent insertion cue points between hom and the displayed E-map. It is transcribed as an insertion into hom ext, not as part of the preceding de V) context. The map arrow points right. A crossed parenthesized item precedes dont on the lower line.',
'b13':'Isolated handwritten page number at the lower left.'
}
records=json.loads((out/'blind_c_scan118_crop_records.json').read_text())
derivatives=json.loads((out/'blind_c_scan118_inspection_records.json').read_text())
with (out/'149_scan118_boxes.tsv').open(encoding='utf8',newline='') as f:
    expected=[r['box'] for r in csv.DictReader(f,delimiter='\t')]
assert [b for b,_ in readings]==expected
for r in records:
    box=r['box']
    r['visually_inspected']=True
    r['successful_visual_inspections']=[{'file':r['crop_file'],'rotation_degrees':0,'layout':'complete saved source crop'}]
    r['successful_visual_inspections'] += [d for d in derivatives if Path(d['file']).name.startswith(f'149_scan118_second_{box}_')]
    r['ambiguities']=ambiguities[box]
    r['clipped_material']=clipping[box]
    if box in layout:r['layout_and_layers']=layout[box]
obs={
'page':'149_scan118',
'reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[str(root/'source/SP88_C13_149_scans/149_scan118.jpg'),str(out/'149_scan118_boxes.tsv'),str(out/'READING_PROTOCOL.md')],
'independence':'Only the assigned image, assigned box list, unchanged neutral reading protocol, and this reader’s own crops and inspection metadata were consulted. No witnesses, first readings, candidate text, notes, notation table, other-page texts, comparisons, adjudication outputs, OCR, PDF text layers, research, or TeX compilation were used.',
'crop_script':str(out/'blind_c_scan118_make_crops.py'),
'inspection_scripts':[str(out/'blind_c_scan118_inspection_panels.py'),str(out/'blind_c_scan118_inspection_details.py')],
'writer_script':str(out/'blind_c_scan118_write_reading.py'),
'crop_count':len(records),
'successfully_visually_inspected_boxes':len(records),
'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each listed source bbox was cropped exactly once with Pillow, autocontrasted and enlarged 3x with LANCZOS. Each complete crop was displayed and visually inspected in its own tool call. Wide boxes were additionally inspected in saved stacked half-panels. Each diagonal margin note was inspected at two rotations. Three details of the dense lower formula box were derived from its already saved crop and visually inspected. No recognition software was used.',
'inspections':records,
'freeze_status':'Completed independently and sealed before comparison; do not modify after reporting completion.'
}
with (out/'149_scan118_second.tsv').open('w',encoding='utf8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['box','reading'])
    w.writerows(readings)
(out/'149_scan118_second_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Readings:',len(readings),'Crops:',len(records),'Successful visual inspections:',obs['visual_inspection_count'])
for name in ['149_scan118_second.tsv','149_scan118_second_observations.json']:
    p=out/name
    print(name,hashlib.sha256(p.read_bytes()).hexdigest())
