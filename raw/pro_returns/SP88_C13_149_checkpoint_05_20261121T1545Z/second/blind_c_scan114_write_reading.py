from pathlib import Path
import csv,json,hashlib
root=Path('/workspace/scratch/0cab6a548abb')
out=root/'edition/second'
readings=[
('b01',r"d'un ob. de $\mathcal E_X^T$\deleted{$\unsure{/Y}$}, opère"),
('b02',r"sur le sous-groupe $\mathcal E_{X/Y}^T$ par \unsure{autom.}"),
('b03',r"intérieur. Les notations \inserted{$\mathcal E_X,$} $\mathcal E_{X/Y}$ \unsure{conviennent|correspondent}"),
('b04',r"intuitives au pt de vue \unsure{qui|géom}"),
('b05',r"intuitives au pt de vue \unsure{qui|géom} \\ regarde $\mathcal E_X^T$\deleted{$\unsure{/Y}$} comme \uline{extension}"),
('b06',r"de $\mathcal E_Y^T$ (ou d'un ss groupe \\ convenable \unsure{réduit|induit}) par $\mathcal E_{X/Y}^T$,"),
('b07',r"qui sera souvent, pour les besoins de"),
('b08',r"la cause, noté $\pi$ -- il joue le"),
('b09',r"\margin{$\unsure{\dagger|+}$ J'hésite \unsure{encore} entre notations $\mathcal E_{X/Y}^T$ et $\pi_{X/Y}^T$ ; que \unsure{je} vais peut-être employer concur-\\remment.} la \\ \unsure{le|les} \\ \unsure{ou|au}"),
('b10',r"(géométrique), tandis que $\mathcal E_Y^T$ joue"),
('b11',r"\unsure{ou|au} d'un groupe profini mixte."),
('b12',r"\deleted{Aussi \unsure{souvent}}"),
('b13',r"\mspage{113}"),
('b14',r", $K$ un corps. \\ $\mathcal E_{\unsure{Y|y}}\simeq\mathcal E_{\unsure{Y|y}}^{Y}$"),
]
ambiguities={
'b01':[
'The superscript is read as T, with its broad top stroke; the small adjacent dot is not promoted to an additional index.',
'The cancelled tail after X is heavily overwritten. Slash plus Y is only a tentative surviving-layer reading; additional horizontal loops cannot be separated securely into further symbols. The cancellation span is longer than the tentative two-glyph reading.',
'The initial abbreviation is read ob.; no expansion is supplied.'
],
'b02':['The final abbreviated word is provisionally autom.; the letters are highly compressed.','The Y-shaped subscript is rendered Y without importing a notation convention.'],
'b03':['The final compressed word is unresolved; conviennent and correspondent are tentative readings from its strokes, not a grammatical correction.','The upper word is read intérieur.; no agreement ending has been added.'],
'b04':['Final word has a long descending initial and compressed following strokes: qui versus géom remains unresolved.','The abbreviation pt is retained.'],
'b05':['Final word of the first line has the same unresolved qui/géom shape within this independently inspected box.','The short cancelled tail immediately after X may be /Y; overstriking obscures its internal strokes.'],
'b06':['The word following convenable may be réduit or induit; the initial stroke/accent is not secure.','The short form ss is retained without expansion.'],
'b07':['The compressed sequence is read sera souvent; no semantic normalization was used.'],
'b08':['The mathematical sign is read pi, without an index or superscript.','Faint light outlines above pi cannot be securely distinguished as separate primary writing; they are not converted into a number or additional formula.'],
'b09':['Marginal reference sign appears cross-like after rotation; dagger versus plus is unresolved.','The start of encore is very near the source crop boundary; the whole word remains explicitly uncertain.','Small strokes after que are tentatively je; their relation to the nearby main-text ink is uncertain.','The complete short main-text words at the right are read la, le/les, and ou/au; the alternatives preserve uncertain endings and initial shape.'],
'b10':[],
'b11':['Initial short word is ou or au.','The word profini has a tall stroke reaching the upper crop edge; its other letters remain visible.'],
'b12':['The first deleted word is Aussi. The second is tentatively souvent; the long strike crosses its middle.'],
'b13':[],
'b14':['The subscripts are Y/y-shaped and capitalization is not secure; both alternatives are preserved.','The right superscript is read Y. The looping descender of corps above it is not treated as a separate tilde or bar.','The relation is read simeq, with the wavy upper stroke and short lower line.']
}
clipping={
'b01':[],
'b02':[],
'b03':[],
'b04':[],
'b05':[],
'b06':[],
'b07':['Small tops/descenders from the neighboring lower line and a partial marginal mark at the lower left are clipped; no neighboring words are completed.'],
'b08':['Top-left descender/oblique marginal strokes and small bottom-edge neighboring fragments are clipped and not completed.'],
'b09':['Main-text fragments along the right edge include an upper q-shaped word fragment and other incomplete word starts; these are not completed.','The diagonal marginal lines begin close to the left crop boundary; uncertain initial strokes are explicitly noted rather than supplied from other boxes.'],
'b10':['Clipped oblique marginal text at the upper left and partial previous-line descenders at the top are not completed.'],
'b11':['Upper edge meets a tall stroke within profini; no extra letter/accent is inferred above the box.'],
'b12':[],
'b13':['The lower black page border is not writing.'],
'b14':['The left-edge comma is complete and retained; a separate lower-left oblique fragment is clipped and not expanded into a neighboring formula.']
}
layout={
'b03':'E_X followed by a comma is written above the main line, with a curved insertion cue leading to the position before E_{X/Y}; the cue is not treated as a mathematical arrow.',
'b05':'Two full lines are retained. The word extension is singly underlined.',
'b06':'Two lines; the opening parenthesis is on the first and its closing parenthesis on the second.',
'b09':'Diagonal marginal prose is enclosed in margin. Main-text words completely visible at the right are recorded separately after it. The written line-ending split concur-/remment is preserved.',
'b12':'A long cancellation stroke crosses the entire two-word phrase.',
'b13':'Isolated handwritten page number at the lower left.',
'b14':'A prose line ending is above a separate formula; the descender from corps approaches the superscript region.'
}
records=json.loads((out/'blind_c_scan114_crop_records.json').read_text())
derivatives=json.loads((out/'blind_c_scan114_inspection_records.json').read_text())
with (out/'149_scan114_boxes.tsv').open(encoding='utf8',newline='') as f:
    expected=[r['box'] for r in csv.DictReader(f,delimiter='\t')]
assert [b for b,_ in readings]==expected
for r in records:
    box=r['box']
    r['visually_inspected']=True
    r['successful_visual_inspections']=[{'file':r['crop_file'],'rotation_degrees':0,'layout':'complete saved source crop'}]
    r['successful_visual_inspections'] += [d for d in derivatives if Path(d['file']).name.startswith(f'149_scan114_second_{box}_')]
    r['ambiguities']=ambiguities[box]
    r['clipped_material']=clipping[box]
    if box in layout:r['layout_and_layers']=layout[box]
obs={
'page':'149_scan114',
'reader_identity':'blind_c — independent image-only diplomatic second reader',
'inputs_consulted':[
str(root/'source/SP88_C13_149_scans/149_scan114.jpg'),
str(out/'149_scan114_boxes.tsv'),
str(out/'READING_PROTOCOL.md')
],
'independence':'Only the assigned image, assigned box list, neutral reading protocol, and the reader’s own saved crops/inspection metadata were consulted. No first readings, witnesses, candidate text, notes, notation table, comparison or adjudication output, OCR, external research, PDF text layer, or TeX compilation was used.',
'crop_script':str(out/'blind_c_scan114_make_crops.py'),
'inspection_scripts':[str(out/'blind_c_scan114_inspection_panels.py'),str(out/'blind_c_scan114_inspection_details.py')],
'writer_script':str(out/'blind_c_scan114_write_reading.py'),
'crop_count':len(records),
'successfully_visually_inspected_boxes':len(records),
'visual_inspection_count':sum(len(r['successful_visual_inspections']) for r in records),
'method':'Each source bbox was cropped once with Pillow at the supplied original coordinates, autocontrasted and enlarged 3x with LANCZOS. All complete saved crops were visually inspected. Wide crops were additionally inspected as saved stacked half-panels. The diagonal note was inspected at -45 degrees and in a detail derived from that rotated crop. Two upper-line details were derived from saved crops. No recognition software was used.',
'failed_visual_attempts':[{'box':'b01','reason':'The combined crop-generation/view call returned a context-truncation message, so that attempt was not counted as a successful visual inspection. The saved b01 crop was subsequently displayed successfully in its own call.'}],
'inspections':records,
'freeze_status':'Completed independently and sealed before comparison; do not modify after reporting completion.'
}
with (out/'149_scan114_second.tsv').open('w',encoding='utf8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['box','reading'])
    w.writerows(readings)
(out/'149_scan114_second_observations.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Readings:',len(readings),'Crops:',len(records),'Successful visual inspections:',obs['visual_inspection_count'])
for name in ['149_scan114_second.tsv','149_scan114_second_observations.json']:
    p=out/name
    print(name,hashlib.sha256(p.read_bytes()).hexdigest())
