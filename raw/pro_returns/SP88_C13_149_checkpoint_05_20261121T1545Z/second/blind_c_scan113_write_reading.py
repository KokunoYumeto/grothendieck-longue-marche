from pathlib import Path
import csv,json,hashlib
root=Path('/workspace/scratch/0cab6a548abb');out=root/'edition/second'
readings=[
('b01',r'\margin{56}'),
('b02',r'le lien avec le'),
('b03',r'\deleted{définition}\inserted{plus \unsure{ample|simple}} (11)'),
('b04',r"est évident que, si \(\xi_X\) provient d'un"),
('b05',r'pt géom \(\xi_T\) de \(T\), alors on aura'),
('b06',r'dans \unsure{ce|le} cas'),
('b07',r'\((20)\qquad\begin{array}{ccc}\mathcal E_{X/Y}^{\xi_T}&\simeq&\mathcal E_{X/Y}^{T}\\\rotatebox{90}{$\simeq$}&&\\\unsure{\pi|\Pi}_1(X_{\xi_Y},\xi_T)&&\end{array}\)'),
('b08',r'\deleted{\unsure{les|donc}} -- les \(\unsure{\pi|\Pi}_1(X_{\xi_Y},\xi_T)\) des fibres géom, relatifs aux divers pts géom de \(\mathcal E_{X/Y}^{T}\), sont canoniquement iso entre eux. \margin{\unsure{20|16}}'),
('b09',r"( Il faut donc faire attention que \(\mathcal E_{X/Y}\) \inserted{(\(Z\) non précisé)} est une classe d'iso."),
('b10',r"de groupes profinis sans plus, \uline{pas} un groupe extrinsèque. L'arbitraire"),
('b11',r"\unsure{dans|de} le choix d'un iso entre"),
('b12',r'\(\mathcal E_{X/Y}^{T}\) et \(\mathcal E_{X/Y}^{T\prime}\) provient du choix'),
('b13',r'\mspage{112}'),
]
notes={
'b01':{'ambiguities':[], 'clipped_material':[], 'number_role':'Standalone upper foliation read 56.'},
'b02':{'ambiguities':[], 'clipped_material':[]},
'b03':{'ambiguities':['The cancelled word is read définition; its ascenders and f descender remain distinguishable beneath the long strike.','The raised replacement reads plus ample or plus simple; the second word\'s first short strokes are compressed.'], 'clipped_material':['Upper tip of the raised word\'s l reaches the upper crop boundary.'],'layers':'Long horizontal cancellation through définition, with replacement phrase written above; (11) remains literal at right.'},
'b04':{'ambiguities':['Dense strokes under the beginning of évident were read as letter joins, not as a separate complete underline or deletion.'], 'clipped_material':[]},
'b05':{'ambiguities':['The field-point symbol is read xi with subscript T.','No full stop supplied after the abbreviated géom because no separate stop is clearly present here.'], 'clipped_material':[]},
'b06':{'ambiguities':['Short middle word admits ce or le; ce is primary.'], 'clipped_material':[]},
'b07':{'ambiguities':['The two-legged pi glyph with subscript 1 admits lower-case pi or capital Pi in this hand; both retained.'], 'clipped_material':[], 'diagram_layout':'Literal label (20) at left. Top-left E^(xi_T)_(X/Y) is horizontally isomorphic to top-right E^T_(X/Y). A vertically oriented isomorphism sign connects the top-left term to the lower pi_1(X_(xi_Y),xi_T). No arrowheads are drawn; the TSV uses an array and a 90-degree rotated isomorphism sign to preserve the relation and layout.','index_notes':'xi_T is the superscript of the upper-left group; xi_Y is the subscript of X in the lower formula; xi_T is the second argument.'},
'b08':{'ambiguities':['First cancelled short word admits les or donc.','Pi glyph in the displayed fundamental-group expression admits pi or Pi.','A very faint pencil-like mark in the blank area near the last line looks like 20 or 16; retained with uncertainty. It may be offset/show-through rather than a deliberate annotation.'], 'clipped_material':[], 'line_readings':['Cancelled word, dash, les pi_1(X_(xi_Y),xi_T) des fibres','géom, relatifs aux divers pts géom','de E^T_(X/Y), sont canoniquement iso','entre eux.'], 'abbreviations':'géom, pts, and iso preserved without expansion.'},
'b09':{'ambiguities':['The inserted initial symbol is read Z; the short following word is non.'], 'clipped_material':['Lower end of q in que meets the lower boundary but the word is readable.'],'insertion_layout':'(Z non précisé) is written between the two main lines, with a long curved connector leading to the gap after E_(X/Y), before est. The initial opening parenthesis is preserved without inventing a closing partner.'},
'b10':{'ambiguities':['The adjective after un groupe is read extrinsèque.','Last word read L\'arbitraire.'], 'clipped_material':['A preceding-line descender intrudes at the upper-left boundary.'],'emphasis':'Single underline under pas.'},
'b11':{'ambiguities':['Opening long low word admits dans or de; its compressed strokes do not decisively distinguish them.'], 'clipped_material':[]},
'b12':{'ambiguities':[], 'clipped_material':[], 'formula_notes':'First superscript is T; second is T with a clearly separate prime. Both subscripts read X/Y.'},
'b13':{'ambiguities':[], 'clipped_material':['Black page edge along the bottom.'],'number_role':'Lower-left manuscript author page number read 112.'},
}
records=json.loads((out/'blind_c_scan113_crop_records.json').read_text(encoding='utf8'))
for rec in records:
    rec.update(notes[rec['box']]);rec['visually_inspected']=True
    rec['successful_visual_inspections']=[{'file':rec['crop_file'],'rotation_degrees':0}]
    if rec['box'] in ('b09','b10','b11'):
        rec['successful_visual_inspections'].append({'file':str(root/f"edition/crops/149_scan113_second_{rec['box']}_inspect_panels.png"),'rotation_degrees':0,'layout':'left and right halves stacked, 40-pixel white gap'})
    if rec['box']=='b08':
        for i,bounds in enumerate(((0,430),(390,830),(800,1250),(1230,1614)),1):
            rec['successful_visual_inspections'].append({'file':str(root/f'edition/crops/149_scan113_second_b08_inspect_line{i}.png'),'rotation_degrees':0,'derived_y_bounds':list(bounds),'layout':'row band from saved crop, left and right halves stacked'})
    if rec['box']=='b03':
        rec['successful_visual_inspections'].append({'file':rec['crop_file'],'rotation_degrees':0,'purpose':'Second visual inspection of correction layers'})
tsv=out/'149_scan113_second.tsv';obs_path=out/'149_scan113_second_observations.json'
with tsv.open('w',encoding='utf8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['box','reading']);w.writerows(readings)
obs={
'page':'149_scan113','reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[str(root/'source/SP88_C13_149_scans/149_scan113.jpg'),str(out/'149_scan113_boxes.tsv'),str(out/'READING_PROTOCOL.md')],
'independence':'No witnesses, first readings, candidate text, page TEX, notation, notes, comparison/adjudication output, other manuscript page, OCR, text recognition, PDF text layer, external research, or TeX compilation consulted for this page. Earlier sealed pages were not reopened.',
'crop_script':str(out/'blind_c_scan113_make_crops.py'),'inspection_script':str(out/'blind_c_scan113_inspection_panels.py'),
'crop_count':len(records),'successfully_visually_inspected_boxes':len(records),'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each original source bbox cropped once with Pillow, autocontrasted, enlarged 3x with LANCZOS, and saved without rotation. Inspection variants were derived only from saved crops. One image emitted per image-view call. No compilation was performed.',
'inspections':records,'freeze_status':'Completed and sealed before any comparison; files will remain unchanged after notification.'
}
obs_path.write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Completed',len(readings),'readings,',len(records),'observations,',obs['visual_inspection_count'],'successful visual inspections.')
for path in (tsv,obs_path):print(hashlib.sha256(path.read_bytes()).hexdigest(),path.name)
