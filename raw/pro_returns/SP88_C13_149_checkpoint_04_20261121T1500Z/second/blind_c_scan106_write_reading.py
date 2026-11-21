from pathlib import Path
import csv,json
root=Path('/workspace/scratch/0cab6a548abb')
out=root/'edition/second'
readings=[
('b01',r'de \(\unsure{\xi|\zeta}\)'),
('b02',r"l'un est \(X\)"),
('b03',r'close \(\deleted{\bar K}\inserted{\Omega}\) de \(k(x)\),'),
('b04',r'(pas néc. \deleted{une} clôture alg. de \(k(x)\)) et on'),
('b05',r'\unsure{notera|note alors} aussi \(\mathcal E_X^\Omega\) au lieu de'),
('b06',r"\(\mathcal E_X^{\unsure{\xi|\zeta}}\) (\(\Omega\) sous-entendu en tant qu'"),
('b07',r'extension de \(k(x)\), donc avec sa structure de \(k(x)\) algèbre). On \unsure{aura|a ici} \inserted{même dans ce cas}'),
('b08',r'\((5)\qquad \mathcal E_{\unsure{X|x}}^\Omega\simeq\mathcal E_X^{\overline{k(x)}}\),'),
('b09',r'la clôture alg. de'),
('b10',r'est très'),
('b11',r'\(Y\) connexe, \inserted{en \unsure{retour|notant}}'),
('b12',r'\((6)\qquad \mathcal E(f):\mathcal E_X\longrightarrow\mathcal E_Y\qquad\) où \(f:X\longrightarrow Y\)'),
('b13',r'\((\mathrm{Sch}\ \unsure{\mathrm{conn}|\mathrm{geom}})\longrightarrow\unsure{\mathrm{grpro}|\mathrm{grpr}}\ \mathrm{ext}\)'),
('b14',r'\mspage{105}'),
]
notes={
'b01':{'ambiguities':['Long narrow Greek letter read as xi, with zeta retained as an alternative; no mathematical illegibility placeholder used.'],'clipped_material':[]},
'b02':{'ambiguities':[], 'clipped_material':['Tiny tip of ink from the following line touches the bottom edge; no word supplied for it.']},
'b03':{'ambiguities':['An earlier barred K is distinguishable inside a larger Omega; read as overwritten replacement, with both layers preserved.','First word read close, including the small final e.'], 'clipped_material':[]},
'b04':{'ambiguities':['The crossed word is read une.','Final low strokes read on.'], 'clipped_material':['The descender of p in pas reaches the lower crop edge; its visible body suffices for the reading.']},
'b05':{'ambiguities':['The opening lettering has a wide internal gap: notera is the primary reading; note alors is retained as a visual alternative.'], 'clipped_material':['A descender from the preceding line enters from the top; no adjacent word reconstructed.']},
'b06':{'ambiguities':['Superscript Greek letter read xi, with zeta retained.'], 'clipped_material':['A few upper tips of the following line enter along the bottom; no completion attempted.']},
'b07':{'ambiguities':['The final main-line words are read On aura, with On a ici retained as an alternative.','The raised phrase connected by a curved insertion mark is read même dans ce cas.','The compressed main-line phrase is read donc avec sa structure.'], 'clipped_material':['Upper extremities of some tall strokes touch the upper boundary.','Small piece of the next formula enters at the bottom; not transcribed as a complete symbol.'],'insertion_layout':'Main text continues from structure to de k(x) algèbre). Raised phrase même dans ce cas has a long curved connector down toward the following On aura phrase.'},
'b08':{'ambiguities':['Left subscript has a looped hand; X is primary, x is retained.','Formula label read (5), not a manuscript page number.'], 'clipped_material':['Isolated preceding-line tails appear at the top; not reconstructed.']},
'b09':{'ambiguities':[], 'clipped_material':[]},
'b10':{'ambiguities':['A word at the right begins nature... and runs out of the rectangle; only the complete preceding words est très are transcribed.'], 'clipped_material':['An isolated horizontal tail enters from the left.','Right-hand word is clipped; no complete word supplied.']},
'b11':{'ambiguities':['Raised/connected phrase read en retour, with en notant retained as an alternative.'], 'clipped_material':['Upper end of Y meets the upper edge.','Small neighbouring curved stroke at the lower left is clipped.'],'insertion_layout':'The lower phrase is linked to the upper text by a long curved mark.'},
'b12':{'ambiguities':['Formula label read (6), left literal.'], 'clipped_material':[]},
'b13':{'ambiguities':['Dense first letter of the word after Sch admits conn or geom; conn is primary.','The target abbreviation is read grpro, with grpr retained; last word is read ext.','No definite separate deleted underletter can be isolated in the dense first letter.'], 'clipped_material':[]},
'b14':{'ambiguities':[], 'clipped_material':['Black page border is visible at the left and bottom.'],'number_role':'Handwritten author page number at lower-left, read 105.'},
}
records=json.loads((out/'blind_c_scan106_crop_records.json').read_text(encoding='utf8'))
for rec in records:
    rec.update(notes[rec['box']])
    rec['visually_inspected']=True
    rec['successful_visual_inspections']=[rec['crop_file']]
    if rec['box'] in ('b04','b05','b06','b07','b13'):
        rec['successful_visual_inspections'].append(str(root/f"edition/crops/149_scan106_second_{rec['box']}_inspect_panels.png"))
    if rec['box'] in ('b03','b11'):
        rec['successful_visual_inspections'].append(rec['crop_file'])
with (out/'149_scan106_second.tsv').open('w',encoding='utf8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['box','reading'])
    w.writerows(readings)
obs={
'page':'149_scan106',
'reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[str(root/'source/SP88_C13_149_scans/149_scan106.jpg'),str(out/'149_scan106_boxes.tsv'),str(out/'READING_PROTOCOL.md')],
'independence':'No first reading, transcription, TEX, witness, notes, notation table, other manuscript page, comparison output, OCR, text recognition, PDF text layer, external research, or TeX compilation consulted.',
'crop_script':str(out/'blind_c_scan106_make_crops.py'),
'inspection_layout_script':str(out/'blind_c_scan106_inspection_panels.py'),
'crop_count':len(records),
'successfully_visually_inspected_boxes':len(records),
'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each original source bbox was cropped once with Pillow, autocontrasted and enlarged 3x with LANCZOS, without rotation. Five already-saved long crops were rearranged into two stacked inspection panels, preserving all pixels and adding only a white gap. Each visual tool call emitted exactly one image.',
'inspections':records,
'freeze_status':'Completed and sealed before any comparison; no subsequent changes authorized to this reading.'
}
(out/'149_scan106_second_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Completed',len(readings),'TSV readings and',len(records),'observations;',obs['visual_inspection_count'],'successful visual image inspections.')
