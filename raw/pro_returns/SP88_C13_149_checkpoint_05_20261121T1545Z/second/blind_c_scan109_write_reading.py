from pathlib import Path
import csv,json
root=Path('/workspace/scratch/0cab6a548abb');out=root/'edition/second'
readings=[
('b01',r'\margin{54}'),
('b02',r'par un triple'),
('b03',r'\(\widetilde{\unsure{X|x}}\unsure{\longrightarrow|-}X\unsure{\longrightarrow|-}Y\)'),
('b04',r'plus générale,'),
('b05',r'si \(\deleted{Z}\inserted{T}\longrightarrow X\) avec \(\deleted{Z}\inserted{T}\) 1-connexe,'),
('b06',r'\unsure{ou|en|on} non'),
('b07',r'\((11)\) \margin{\unsure{!|1})} \(\deleted{\unsure{\mathcal E}}\inserted{\unsure{\Pi|\mathcal E|\mathcal G}}_{X/Y}^{\deleted{Z}\inserted{T}}=\operatorname{Ker}(\mathcal E_X^{\deleted{Z}\inserted{T}}\longrightarrow\mathcal E_Y^{\deleted{Z}\inserted{T}})\)'),
('b08',r"on a un foncteur en l'objet \((\deleted{Z}\inserted{T}\longrightarrow X_{\unsure{0|\bullet}}\longrightarrow Y)\)"),
('b09',r'\unsure{riable}. En particulier : \(\mathcal E_{X/Y}^{\unsure{\xi|\zeta}},\unsure{\xi|\zeta}\)'),
('b10',r'un pt géom. de \(X\),'),
('b11',r"\margin{\uline{NB} \(\mathcal E_{X/Y}^T\), pour \(T\) variable, \(X/Y\) fixé, est défini à isom canonique près, et la notation \(\mathcal E_{X/Y}\) \unsure{s'impose}} \par \unsure{ou|en|on} \par \((11)\) \margin{\unsure{!|1})} \par on a \par un \par \(\mathcal E_{X/A}^{\widetilde{\unsure{x|X}}}\)"),
('b12',r"``suite exacte d'"),
('b13',r"homotopie universelle'' \deleted{\unsure{de|des}} (en dim 1)"),
('b14',r'(pour \(X=Y\) donné) de \(T\longrightarrow X\),'),
('b15',r"(avec \(T\) 1-connexe) peut s'interpréter"),
('b17',r'\margin{Car \(\mathcal E_X^{\deleted{\unsure{Z}}\inserted{T}}\longrightarrow\mathcal E_Y^{\deleted{\unsure{Z}}\inserted{T}}\) est épi \quad \(-\) \unsure{?}}'),
('b18',r'\mspage{108}'),
('b19',r'\margin{\unsure{!|1})}'),
('b21',r'0-connexe,'),
('b22',r'\margin{\(-\) \unsure{?}}'),
]
notes={
'b01':{'ambiguities':[], 'clipped_material':[], 'number_role':'Standalone top foliation, 54.'},
'b02':{'ambiguities':['Opening word read par.'], 'clipped_material':[]},
'b03':{'ambiguities':['First crossed letter with tilde is retained as X or x.','Both horizontal relations have weak terminal hooks; rightward arrows are primary, plain strokes retained as alternatives.'], 'clipped_material':[]},
'b04':{'ambiguities':[], 'clipped_material':[]},
'b05':{'ambiguities':['Each Z has a visibly superimposed darker T; both underlying diagonal and baseline strokes remain distinguishable.'], 'clipped_material':[]},
'b06':{'ambiguities':['Very compressed first short word admits ou, en, or on; non is clear.'], 'clipped_material':['A tail from the line above enters at the top; no completion supplied.']},
'b07':{'ambiguities':['The first formula letter has a visible large upper E-like curve but a heavily blackened lower body. An earlier calligraphic E is tentative; possible resulting readings Pi, retouched E, or G are retained. No unreadable-symbol placeholder is used.','Superscript replacements Z to T are visible on all three group terms.','Marginal sign before the formula resembles !) but may be 1); both retained.'], 'clipped_material':['A marginal diagonal note is cut at the left/top and lower-left; incomplete words not borrowed from another crop.','The following-line word l\'objet intersects the bottom boundary and is incomplete in this box; not completed.'], 'layer_notes':'Heavily overwritten leading group symbol, three Z/T superscript layers, formula label (11), and a separate marginal reference sign are all preserved.'},
'b08':{'ambiguities':['A small dark mark below/right of X is retained as a subscript 0 or bullet; it may instead be punctuation or a stray corrected mark.','The initial object Z is visibly overwritten by T.'], 'clipped_material':['Part of the preceding formula along the upper edge is clipped.','Diagonal marginal words enter at the left and are incomplete.','Tips of the next line at the lower edge are not completed.'], 'layout_notes':'l\'objet is raised above the main baseline before the parenthesized rightward three-object chain.'},
'b09':{'ambiguities':['Only a clipped word-ending, tentatively riable, is visible before the period; its missing beginning is not supplied.','The tall narrow Greek letter appears both as superscript and as a standalone symbol after the comma; xi is primary, zeta retained.'], 'clipped_material':['The preceding line intrudes at the top.','Beginning of the first word is outside the left boundary.','An upper part of the next line enters at the bottom right.']},
'b10':{'ambiguities':[], 'clipped_material':[], 'letter_shape_note':'The long leftward return under géom. is the g descender, not a separately labelled arrow.'},
'b11':{'ambiguities':['Final marginal word is tentatively s\'impose.','The superscript of the complete bottom main-text formula has a tilde and crossed x/X form; case uncertain.','The short main-text word near the top admits ou/en/on.','The separate sign beside (11) admits !) or 1).'], 'clipped_material':['Several main-line words at the right boundary are incomplete and not completed.','The upper-right non word and the middle-right variable-like word extend outside the crop.','The main-text abbreviation pt at the right edge is incomplete; only complete un before it is retained.'], 'layout_notes':'Main marginal note runs diagonally upward to the right, starting underlined NB. It was read after a 40-degree clockwise inspection rotation. Canonique is one long word, crossing the main text; the nearby !) sign belongs to the main formula callout, not to the word. Separate complete main-text fragments are divided by par in the reading, without implying a continuous sentence.'},
'b12':{'ambiguities':[], 'clipped_material':['The quotation continues outside the box; no closing quote supplied.']},
'b13':{'ambiguities':['Crossed short word after closing quotation admits de or des.'], 'clipped_material':['A preceding-line descender enters at the upper left.'],'deletion_notes':'Two horizontal strokes cross the short word between closing quotation and (en dim 1).'},
'b14':{'ambiguities':['Equality is read X=Y; final T-to-X relation is rightward.'], 'clipped_material':['An upper-line descender intrudes at the top left.']},
'b15':{'ambiguities':[], 'clipped_material':['A preceding-line descender touches the upper-left edge.']},
'b17':{'ambiguities':['Superscripts contain dark T overwrites; underlying Z is tentative in each.','A small separate sign above the second group is not securely identifiable: visible dash and a question-like form are retained separately.','Final abbreviation read épi without supplying an expansion.'], 'clipped_material':['A curved piece of main-text parenthesis intrudes at the lower-right boundary.'], 'layout_notes':'Diagonal marginal statement read after a 40-degree clockwise rotation. Small separate dash/question-like sign lies above the second group, not after the word épi; its position is described here because the TSV is linear.'},
'b18':{'ambiguities':[], 'clipped_material':['Black page edge along bottom.'],'number_role':'Lower-left manuscript page number, 108.'},
'b19':{'ambiguities':['A short slanted stroke with a detached point and a closing parenthesis reads !) or 1).'], 'clipped_material':[]},
'b21':{'ambiguities':[], 'clipped_material':[]},
'b22':{'ambiguities':['An isolated short dash and part of a question-like curved sign are visible; no secure full interpretation.'], 'clipped_material':['Curved lower/right part of the sign exits the rectangle. No missing continuation supplied.']},
}
records=json.loads((out/'blind_c_scan109_crop_records.json').read_text(encoding='utf8'))
viewed_panels={'b05','b07','b08','b09','b13','b14','b15'}
for rec in records:
    rec.update(notes[rec['box']]);rec['visually_inspected']=True
    rec['successful_visual_inspections']=[{'file':rec['crop_file'],'rotation_degrees':0}]
    if rec['box'] in viewed_panels:
        rec['successful_visual_inspections'].append({'file':str(root/f"edition/crops/149_scan109_second_{rec['box']}_inspect_panels.png"),'rotation_degrees':0,'layout':'left and right halves stacked, 40-pixel white gap'})
    if rec['box']=='b11':
        for suffix in ('rotated','upper','lower'):
            item={'file':str(root/f'edition/crops/149_scan109_second_b11_inspect_{suffix}.png'),'rotation_degrees':-40}
            if suffix=='upper':item['derived_bbox']=[700,600,2400,1480]
            if suffix=='lower':item['derived_bbox']=[100,1150,2250,1980]
            rec['successful_visual_inspections'].append(item)
    if rec['box']=='b17':
        rec['successful_visual_inspections'].append({'file':str(root/'edition/crops/149_scan109_second_b17_inspect_rotated.png'),'rotation_degrees':-40})
with (out/'149_scan109_second.tsv').open('w',encoding='utf8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['box','reading']);w.writerows(readings)
obs={
'page':'149_scan109','reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[str(root/'source/SP88_C13_149_scans/149_scan109.jpg'),str(out/'149_scan109_boxes.tsv'),str(out/'READING_PROTOCOL.md')],
'independence':'No first reading, transcription, TEX, witness, notes, notation table, review metadata, comparison/adjudication output, other manuscript page, OCR, text recognition, PDF text layer, external research, or TeX compilation consulted for this page. Previously sealed page readings were not reopened.',
'crop_script':str(out/'blind_c_scan109_make_crops.py'),
'inspection_scripts':[str(out/'blind_c_scan109_inspection_layouts.py'),str(out/'blind_c_scan109_margin_panels.py'),str(out/'blind_c_scan109_rotate_b17.py')],
'crop_count':len(records),'successfully_visually_inspected_boxes':len(records),'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each original source bbox cropped once with Pillow, autocontrasted and enlarged 3x using LANCZOS. Inspection variants were derived only from saved crops: stacked halves or 40-degree clockwise BICUBIC rotation with white fill. B11 additionally inspected in two detailed rectangular panels of that rotated crop. One image emitted per image-view call.',
'inspections':records,'freeze_status':'Completed and sealed before comparison; these two outputs will not be modified after notification.'
}
(out/'149_scan109_second_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Completed',len(readings),'readings,',len(records),'crop observations,',obs['visual_inspection_count'],'successful image inspections.')
