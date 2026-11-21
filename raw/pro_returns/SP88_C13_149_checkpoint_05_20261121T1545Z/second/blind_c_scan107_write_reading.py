from pathlib import Path
import csv,json
root=Path('/workspace/scratch/0cab6a548abb'); out=root/'edition/second'
readings=[
('b01',r'\margin{\unsure{53|52}}'),
('b02',r"l'hom"),
('b03',r'\((6)\qquad\mathcal E_X^{\tilde x}\longrightarrow\mathcal E_Y^{\tilde y}\)'),
('b04',r'le rôle de'),
('b05',r'\unsure{en|on} \unsure{leur|deux} \deleted{\unsure{fait|soit}}'),
('b06',r'plus que.'),
('b07',r'\(Z\) 1-connexe,'),
('b08',r"``foncteur fibre''"),
('b09',r'\(\unsure{B_{\Pi(X)}|B\Pi(X)}\)'),
('b10',r'rev étales de \(Y\ldots\))'),
('b11',r'\deleted{\unsure{qui|ainsi} \(\mathcal E_X^{\tilde x}\)}'),
('b12',r'\((7)\qquad(X,\tilde x)\longmapsto\mathcal E_X^{\tilde x}\)'),
('b13',r"schémas 0-connexes \(X\) \uline{munis} d'un"),
('b14',r'\(Z\) 1-connexe'),
('b15',r"s'envoyant dans \(X\)) vers"),
('b16',r'la \inserted{sous-}cat.'),
('b17',r"des \((X,\unsure{\xi|\zeta})\) munis d'un pt géom -"),
('b18',r'\mspage{106}'),
]
notes={
'b01':{'ambiguities':['The upper standalone number is read 53; the angular second digit also admits 2. Both readings retained.'],'clipped_material':[],'number_role':'Standalone top foliation, separate from the lower manuscript page number.'},
'b02':{'ambiguities':[], 'clipped_material':[]},
'b03':{'ambiguities':['The letter pair is transcribed as capital base X/Y and smaller superscript x/y; both superscripts carry visible tildes.'], 'clipped_material':['A descending stroke from the preceding line enters at the upper left and is not reconstructed.']},
'b04':{'ambiguities':[], 'clipped_material':[]},
'b05':{'ambiguities':['Opening short word admits en or on.','Middle word admits leur or deux.','Cancelled final word has distinguishable last i and tall t; fait and soit are retained as possible readings. Cancellation obscures the first letters.'], 'clipped_material':[]},
'b06':{'ambiguities':['The descender of q sweeps far left and has an arrow-like endpoint; it is recorded as part of the letter, not a separate mathematical arrow.'], 'clipped_material':[]},
'b07':{'ambiguities':[], 'clipped_material':[]},
'b08':{'ambiguities':[], 'clipped_material':['A small tip of the next line appears at the lower boundary; it is not completed.']},
'b09':{'ambiguities':['Pi has a long horizontal bar and two visible descenders; read capital Pi.','Pi(X) lies lower than B, so subscript is the primary interpretation; same-line B Pi(X) remains possible.','The argument is read X.'], 'clipped_material':[]},
'b10':{'ambiguities':['Initial abbreviation is read rev, without supplying a full word.','The trailing dot and short connected mark after Y are read as an ellipsis.'], 'clipped_material':['Top of Y and a neighbouring upper-line stroke meet the crop boundary; no missing surrounding words supplied.']},
'b11':{'ambiguities':['A heavy zigzag cancellation crosses the text before and through the mathematical group. The preceding word admits qui or ainsi.','The mathematical group is read calligraphic E, subscript X, superscript tilde x; cancellation overlaps its upper strokes.','The full cancelled span is represented together because distinct finer cancellation boundaries cannot be isolated confidently.'], 'clipped_material':['A neighbouring line tail enters the lower-left edge; not completed.'],'cancellation_layout':'Zigzag traverses the word and upper part of the formula; an additional horizontal stroke crosses the formula near its lower part.'},
'b12':{'ambiguities':['Arrow has a visible vertical source bar and rightward head, transcribed longmapsto.'], 'clipped_material':['An upper-line descender intrudes near the top right of the blank area.']},
'b13':{'ambiguities':[], 'clipped_material':['Small neighbouring-line tip appears at the bottom right.'],'emphasis':'Single underline beneath munis.'},
'b14':{'ambiguities':[], 'clipped_material':[]},
'b15':{'ambiguities':[], 'clipped_material':['Upper tips of neighbouring lower-line letters enter from the bottom; no completion attempted.']},
'b16':{'ambiguities':['The short lower-left word is read la.'], 'clipped_material':['A small unrelated stroke enters at the top right.'],'insertion_layout':'sous- is written above cat. with a curved insertion connector pointing into the gap before cat.'},
'b17':{'ambiguities':['The second coordinate of the pair is a long narrow Greek letter; xi is primary, zeta retained.','Abbreviations pt and géom are preserved.','A separate horizontal terminal stroke is preserved as a dash; no continuation supplied.'], 'clipped_material':['A long upper-line descender enters above the opening pair; not reconstructed.']},
'b18':{'ambiguities':[], 'clipped_material':['Black page edge visible along the bottom.'],'number_role':'Handwritten lower-left author page number, read 106.'},
}
records=json.loads((out/'blind_c_scan107_crop_records.json').read_text(encoding='utf8'))
for rec in records:
    rec.update(notes[rec['box']]);rec['visually_inspected']=True
    rec['successful_visual_inspections']=[rec['crop_file']]
    if rec['box'] in ('b13','b17'):
        rec['successful_visual_inspections'].append(str(root/f"edition/crops/149_scan107_second_{rec['box']}_inspect_panels.png"))
    if rec['box'] in ('b01','b05','b11'):
        rec['successful_visual_inspections'].append(rec['crop_file'])
with (out/'149_scan107_second.tsv').open('w',encoding='utf8',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n');writer.writerow(['box','reading']);writer.writerows(readings)
obs={
'page':'149_scan107','reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[str(root/'source/SP88_C13_149_scans/149_scan107.jpg'),str(out/'149_scan107_boxes.tsv'),str(out/'READING_PROTOCOL.md')],
'independence':'No first reading, transcription, TEX, witness, notes, notation table, other manuscript page, comparison output, OCR, text recognition, PDF text layer, external research, or TeX compilation consulted for this page. Previously sealed scan106 files were not reopened.',
'crop_script':str(out/'blind_c_scan107_make_crops.py'),'inspection_layout_script':str(out/'blind_c_scan107_inspection_panels.py'),
'crop_count':len(records),'successfully_visually_inspected_boxes':len(records),'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each original source bbox was cropped once in Pillow, autocontrasted and enlarged 3x with LANCZOS, without rotation. Two saved long crops were rearranged into stacked inspection panels; no source recropping. Each image-view tool call emitted one image.',
'inspections':records,'freeze_status':'Completed and sealed before comparison; no further modification authorized to this reading.'
}
(out/'149_scan107_second_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Completed',len(readings),'readings,',len(records),'observations,',obs['visual_inspection_count'],'successful visual inspections.')
