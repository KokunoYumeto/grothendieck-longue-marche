"""Seal blind_b's image-only reading of scan117; no other reading is loaded."""
from pathlib import Path
import csv
import json
import hashlib

base=Path('/workspace/scratch/0cab6a548abb')
second=base/'edition/second'
diag=second/'diagnostics'

readings={
 'b01':r'''\mspage{58} $(23)\quad \mathcal{E}_{X}^{\deleted{}\inserted{\overline K}}=\mathcal{E}_{L}^{\unsure{g|\alpha}\overline L}\simeq\mathcal{E}_{\unsure{U|u}}^{\overline L}$ (\unsure{ss-groupe|ss-gr.} fermé inv. engendré par les $L_{x'_i}$ $(i\in\overline I)$)''',
 'b02':r'''variable $(24)\quad \mathcal{E}_{L}^{\overline L}\simeq\varprojlim_{\unsure{U|u}}\mathcal{E}_{\unsure{U|u}}^{\overline L}$''',
 'b03':r'''et de \unsure{même|$=$}, bien sûr $(25)\quad \Pi_{L/\unsure{K|M}}^{\overline L}\simeq\varprojlim_{\unsure{U|u}}\Pi_{\unsure{U|u}/K}^{\overline L}$. Comment récupérer les $\mathcal{E}_{\unsure{U|u}}^{\overline L}$, $\mathcal{E}_{L}^{\overline L}$ ? Pour \uline{\unsure{tt|$H$}} \unsure{demi-anneau|sous-anneau|d'un anneau} \inserted{\unsure{s-gr|s-ar} $V$} de \unsure{cr.|val.} de type fini sur $K$ (correspondant à un ``germe de modèle'' de $L/K$, un voisinage d'un pt de codim $1$ i.e. du pt gén. d'un diviseur), considé- rons le point fermé $x$ de $S_x=\operatorname{Spec}(V)$, \par \margin{Dans les considérations qui suivent, $K$ et $(X,U)$ ne jouent provisoirement aucun rôle. (Mais \unsure{un} \unsure{groupe} de \unsure{décomp.} \unsure{d'un} ``$U$'' étant \illegible{1} (\unsure{le} ``\unsure{géométrique}'' \unsure{pris}, $\mathcal{E}_L\unsure{\longrightarrow|\to}\mathcal{E}_U$) \inserted{\unsure{plus gén.} \illegible{2} \uline{\unsure{choix seulement}} \deleted{\unsure{relatif}} \uline{\unsure{à is.-conj.|opti-comp}}}} \par \margin{NB -- n'utiliser le terme ``modèle'' que pour des schémas \uline{\unsure{séparés}} (quasi-proj. ?) \uuline{réguliers}} \margin{116}'''
}

with (second/'149_scan117_boxes.tsv').open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in boxes]==list(readings)

tsv=second/'149_scan117_second.tsv'
with tsv.open('w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['box','reading'])
    for b in boxes:
        writer.writerow([b['box'],readings[b['box']]])

panel_manifest=json.loads((diag/'149_scan117_panel_manifest.json').read_text(encoding='utf-8'))
rotated_manifest=json.loads((diag/'149_scan117_rotated_panels_manifest.json').read_text(encoding='utf-8'))
strip_manifest=json.loads((diag/'149_scan117_strip_manifest.json').read_text(encoding='utf-8'))

successful=[]
def seen(path,box,count=1,rotation=0):
    successful.append({'box':box,'file':str(path),'successful_visual_displays':count,'rotation_degrees_pillow':rotation})
seen(base/'edition/crops/149_scan117_second_b01.png','b01')
for col in range(1,4):
    seen(diag/f'149_scan117_b01_r1_c{col}.png','b01',2 if col in [1,2] else 1)
seen(base/'edition/crops/149_scan117_second_b02.png','b02')
for col in range(1,4):
    seen(diag/f'149_scan117_b02_r1_c{col}.png','b02')
for row in range(1,5):
    for col in range(1,5):
        seen(diag/f'149_scan117_b03_r{row}_c{col}.png','b03')
seen(diag/'149_scan117_b03_overview.png','b03')
seen(diag/'149_scan117_b03_rot29_overview.png','b03',rotation=-29)
for row in range(1,3):
    for col in range(1,4):
        seen(diag/f'149_scan117_b03_rot29_r{row}_c{col}.png','b03',2 if (row,col)==(1,2) else 1,rotation=-29)
for label in ['main_question','main_middle','margin_upper','margin_lower']:
    seen(diag/f'149_scan117_{label}_strip.png','b03',rotation=-29 if label.startswith('margin') else 0)

obs={
 'reader':'blind_b',
 'task':'independent image-only diplomatic second reading',
 'page':'149_scan117',
 'permitted_inputs_only':[
    str(base/'source/SP88_C13_149_scans/149_scan117.jpg'),
    str(second/'149_scan117_boxes.tsv'),
    str(second/'READING_PROTOCOL.md')],
 'excluded_sources_accessed':False,
 'ocr_or_text_recognition_used':False,
 'external_research_used':False,
 'tex_compilation_used':False,
 'canonical_crop_count':len(boxes),
 'canonical_crops':[
    {'box':b['box'],'file':str(base/f"edition/crops/149_scan117_second_{b['box']}.png"),
     'original_pixel_bbox':[int(b[k]) for k in ['x0','y0','x1','y1']],
     'source_crop_operations':1,'enlargement':3,'resampling':'Pillow LANCZOS',
     'autocontrast_cutoff':0,'rotation_degrees_pillow':0,
     'visual_inspection_successful':True,
     'inspection_method':'canonical display and overlapping saved-crop panels' if b['box']!='b03' else 'complete coverage by 16 overlapping saved-crop panels; contextual overview; rotated note panels'}
    for b in boxes],
 'successful_visual_inspections':successful,
 'successful_display_count':sum(x['successful_visual_displays'] for x in successful),
 'unique_successfully_inspected_image_count':len(successful),
 'failed_display_attempts':[
    {'file':str(diag/'149_scan117_b01_r1_c3.png'),'reason':'Tool output was truncated at the context boundary; not counted. The same saved panel was subsequently displayed and inspected successfully.'},
    {'file':str(base/'edition/crops/149_scan117_second_b03.png'),'reason':'Full large-image output was discarded by the code-mode output limit. Not counted. All saved-crop tiles and an overview were inspected successfully.'}],
 'display_derivative_manifests':{
    'unrotated_panels':panel_manifest,
    'rotation':json.loads((diag/'149_scan117_rotation_manifest.json').read_text(encoding='utf-8')),
    'rotated_panels':rotated_manifest,
    'contextual_strips':strip_manifest},
 'crop_and_inspection_scripts':[
    str(second/'blind_b_scan117_crop.py'),str(second/'blind_b_scan117_inspect.py'),
    str(second/'blind_b_scan117_rotate.py'),str(second/'blind_b_scan117_rotated_panels.py'),
    str(second/'blind_b_scan117_strips.py')],
 'writer_script':str(second/'blind_b_scan117_write.py'),
 'ambiguities':[
    {'box':'b01','detail':'The first superscript has a dense cancellation below the replacement bar-K. No overwritten underletter is securely distinguishable. The empty deleted command records the cancellation without supplying an invented mathematical letter.'},
    {'box':'b01','detail':'A separate small loop/diagonal glyph precedes bar-L in the middle superscript. It is retained as g/alpha uncertainty. The U-shaped subscripts are not securely case-distinguishable.'},
    {'box':'b01','detail':'The parenthetical ss-groupe/ss-gr. is heavily compressed. The abbreviated inv., engendré, par les, x-prime-i and bar-I are read from the visible strokes; the first two are not expanded.'},
    {'box':'b02','detail':'The complete adjacent word variable appears above formula (24). The inverse-limit arrow points left. U/u case uncertainty is retained.'},
    {'box':'b03','detail':'At the top the word or ditto/equality-like mark after et de consists mainly of two short horizontal strokes; même and equals are retained as alternatives.'},
    {'box':'b03','detail':'In formula (25), the denominator letter of the first Pi subscript looks K/M, while the right denominator is a clear K. No mathematical correction is made.'},
    {'box':'b03','detail':'The main paragraph begins Comment récupérer les. The underlined item after Pour resembles either the abbreviation tt or H. The following compound or word-group, and the short abbreviation before de type, are not secure; alternatives are preserved.'},
    {'box':'b03','detail':'The above-line insertion contains an abbreviated s-gr/s-ar and V. A curved insertion/bracketing stroke runs beneath it toward the gap after the anneau-like word. It is recorded as an insertion, not as part of an equation.'},
    {'box':'b03','detail':'The long diagonal note begins Dans les considérations qui suivent, K et (X,U) ne jouent provisoirement aucun rôle. Its subsequent parenthesis and overlapping smaller addition are difficult. The group/decomp. wording and géométrique/pris are uncertain readings, not supplied from expected mathematics. A one-word obscured text span and two intersecting word-groups are represented by illegible counts; none of those markers replaces a mathematical symbol.'},
    {'box':'b03','detail':'The small diagonal addition contains a plus gén.-like start, an underlined choix seulement-like phrase, a cancelled relatif-like word and a separately underlined short expression read à is.-conj./opti-comp. The order and attachment of this addition to the parenthesis are uncertain; it is kept as a separate inserted layer.'},
    {'box':'b03','detail':'Only one closing parenthesis is visible at the right end of the upper diagonal passage, despite two possible opening marks. The transcription does not invent another closing parenthesis.'},
    {'box':'b03','detail':'The lower diagonal NB note reads n’utiliser le terme modèle que pour des schémas, followed by the underlined séparés-like word, quasi-proj. question, and double-underlined réguliers. The word séparés remains uncertain.'},
    {'box':'b03','detail':'The main paragraph has an actual end-of-line hyphen in considé- rons. The final formula reads S with subscript x, equals Spec(V), followed by a comma. The thin lower-left number is 116.'}],
 'clipped_material':[
    {'box':'b01','detail':'At the bottom of the central portion, the upper bar and stem fragment of material from the following line enter the crop. It is not completed into a symbol or word.'},
    {'box':'b02','detail':'No continuation beyond the crop is supplied. The word variable and displayed formula are complete inside this rectangle.'},
    {'box':'b03','detail':'At the upper edge a small isolated fragment from the preceding line is visible above the top main line; no preceding word or formula is supplied. The left and bottom limits include the physical page boundary, and the marginal writing is transcribed only insofar as visible.'}],
 'diagram_present':False,
 'freeze_status':'complete; frozen before any comparison',
}
assert obs['successful_display_count']==39
assert obs['unique_successfully_inspected_image_count']==36
obs_path=second/'149_scan117_second_observations.json'
obs_path.write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

with tsv.open(encoding='utf-8',newline='') as f:
    rows=list(csv.reader(f,delimiter='\t'))
assert rows[0]==['box','reading']
assert len(rows)==4 and all(len(r)==2 for r in rows)
assert [r[0] for r in rows[1:]]==[b['box'] for b in boxes]
for path in [tsv,obs_path]:
    print(path.name,hashlib.sha256(path.read_bytes()).hexdigest())
print('3 readings; 3 canonical crops; 39 successful visual displays; 36 unique successfully displayed images.')
