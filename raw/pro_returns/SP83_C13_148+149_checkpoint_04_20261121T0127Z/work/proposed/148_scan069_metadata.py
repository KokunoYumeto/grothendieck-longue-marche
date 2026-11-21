"""First-reading record for scan 069; retained as work documentation."""
from pathlib import Path
import json, re

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan069'
out=ROOT/'proposed'
C=(ROOT/'packets'/PAGE/'C.tex').read_text()
H=(ROOT/'packets'/PAGE/'H.tex').read_text()
T=(out/f'{PAGE}.tex').read_text()
parts=json.loads((out/f'{PAGE}_parts.json').read_text())
geometry=json.loads((out/f'{PAGE}_vector_geometry.json').read_text())
crops=json.loads((out/f'{PAGE}_crop_boxes.json').read_text())
for crop in crops:
    crop['viewed']=True
    crop['main_reader_viewed']=True
(out/f'{PAGE}_crop_boxes.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n')
cropby={c['name']:c for c in crops}
hdraw=H[H.index(r'\drawing{'):].strip()
figure=T[T.index(r'\figure{'):T.index('% crop-candidate:')].strip()
c_lines=C.splitlines(); t_lines=T.splitlines()
red=(out/f'{PAGE}_red_geometry.tex').read_text().strip()
black=(out/f'{PAGE}_black_geometry.tex').read_text().strip()
def select(lines, predicate): return '\n'.join(line for line in lines if predicate(line))
newedge=next(line for line in t_lines if '(g)--(h)' in line)
c_graph=select(c_lines,lambda s:s.startswith(r'\coordinate') or s.startswith(r'\draw[') and 'red' not in s and '->' not in s)
t_graph=select(t_lines,lambda s:s.startswith(r'\coordinate') or s.startswith(r'\draw[') and s!=newedge)
c_red=select(c_lines,lambda s:s.startswith(r'\draw[') and 'red' in s)
c_black=select(c_lines,lambda s:s.startswith(r'\draw[->,black]'))
c_labels=select(c_lines,lambda s:s.startswith(r'\node['))
t_labels=select(t_lines,lambda s:s.startswith(r'\node['))

changes=[]
def change(place,c,h,final,diff_c,diff_h,kind,error,evidence,crop,confidence='high',consequential=False,extra=None):
    box=cropby[crop]
    row=dict(id=f'{PAGE}-{len(changes)+1:02d}',place=place,c=c,h=h,final=final,
        diff_c=diff_c,diff_h=diff_h,kind=kind,error_kind=error,evidence=evidence,
        crop=box['crop'],box=box['box'],confidence=confidence,marked_in_h=False,consequential=consequential)
    if extra: row.update(extra)
    changes.append(row)

change('Finite edge from the small central infinity-labelled vertex to the upper-right zero-labelled vertex',
    'absent','absent',newedge,True,True,'drawing or diagram','Drawings and diagrams',
    'A broad grey diagonal runs continuously from the vertex at (1019,553) to the vertex at (1148,486), apart from the actual red overdraw. It joins the small central infinity-labelled vertex to the upper-right zero-labelled vertex. C has no g--h command. H gives only a prose description and no individual edge. The complete connection is visible in whole_graph and overlaps the two local crops; it was read before the incidence check.',
    'whole_graph',consequential=True,
    extra={'supporting_crops':[cropby['inner_labels']['crop'],cropby['upper_right']['crop']]})
change('Graph strokes, curved perimeter edges and ten exterior rays',
    c_graph,hdraw,t_graph,True,True,'drawing or diagram','Drawings and diagrams',
    'The finite graph has broad grey strokes and finer dark retracings. In particular f--a, b--h, h--j, i--l, d--k, l--p and m--p are dark; f--b, f--g, b--e, e--g, g--i, c--h, i--m, j--m, k--l, l--m, m--n and o--p are grey. C reverses these distinctions. The f--l and outer a--d, b--c, c--j, n--o strokes curve as reproduced. The ten rays have plain ends; the bottom ray from p is thin and dark, whereas C makes every ray grey and equally thick. The coordinate names are editorial handles and are not printed.',
    'whole_graph')
change('Red contours, their local projections and the sixteen small vertex loops',
    c_red,hdraw,red,True,True,'drawing or diagram','Drawings and diagrams',
    'The red ink has irregular loop shapes, repeated local thickenings and real pen breaks. Examples include the break below-left of the central zero at approximately (899,588), the separate endpoints near (812,425) in the upper-left fan, and breaks in the right-hand return strokes near (1215,578). C replaces these with ten smooth closed cycles, sixteen regular ellipses and twelve separately placed generic arrows. Direct outlines of the visible red ink retain the actual local shapes and gaps, including the projections seen in left_fan, without asserting a global orientation or a count of mathematically closed curves. H supplies only a prose drawing description.',
    'whole_graph',extra={'supporting_crops':[cropby['left_fan']['crop'],cropby['inner_labels']['crop'],cropby['upper_right']['crop'],cropby['lower_graph']['crop']],
    'geometry_method':'Filled TikZ polygon outlines from colour separation, after visual reading; no OCR, no smoothing or gap filling. Closed polygon boundaries enclose strokes and do not assert that the red centreline curves close.'})
change('Black overdraw beside the upper-right perimeter',
    c_black,'absent',black,True,True,'drawing or diagram','Drawings and diagrams',
    'The narrow black strip has six separate right-projecting chevron-like turns or lobes, at approximately y=456,469,483,499,511,526. Their shafts and joins are irregular. C gives three conventional arrows. The actual shape is outlined without converting the six projections into six idealized arrow symbols. H omits this local feature.',
    'black_chevrons')
change('Placement and orientation of the sixteen vertex labels',
    c_labels,hdraw,t_labels,True,True,'insertion or placement','Drawings and diagrams',
    'The labels do not all lie below and to the right of their vertices as in C. The two upper doubtful infinity forms lie inside the small loops and are rotated; the left doubtful infinity is low and oblique within its loop, and the doubtful 1 lies on the lower-left side of the small upper-central loop. The central 0, the 1 at i, the infinity at j and the lower infinity at l lie to the left of their junctions. The lower-right 1 and infinity sit within their loops. All sixteen label values were read separately; the four obscured values remain doubtful. H mentions the three kinds of label but provides no individual mapping or placements.',
    'whole_graph',extra={'supporting_crops':[cropby[name]['crop'] for name in ['upper_labels','left_label','inner_labels','upper_right','lower_graph']]})
change('Lower-left folio annotation',r'\mspage{68}','absent',r'\mspage{68}',False,True,
    'omission','Omissions',
    'The pale lower-left annotation has a curved upper stroke turning into the lower loop of 6, followed by the two joined loops of 8. Both digits are visible. H omits the folio.',
    'folio')

decisions=[
 dict(id='M0944',decision='undecided',reading=r'\unsure{\infty}',
      evidence='Inside the upper-left small red loop, two vertically arranged loop-like traces support an infinity form. The graph stroke crosses their middle and the contour touches nearby, so the complete closed form cannot be separated confidently. The vertical placement is clear; its value is not resolved.',
      crop=cropby['upper_labels']['crop'],box=cropby['upper_labels']['box'],confidence='low'),
 dict(id='M0945',decision='undecided',reading=r'\unsure{\infty}',
      evidence='Inside the other upper small red loop there are oblique upper and lower loop-like strokes. Grey rays and a dark graph edge overlap the group; the infinity reading is plausible, but the complete pair of loops is not independently clear. It is retained without using the neighbouring labels.',
      crop=cropby['upper_labels']['crop'],box=cropby['upper_labels']['box'],confidence='low'),
 dict(id='M0946',decision='undecided',reading=r'\unsure{\infty}',
      evidence='The left boundary vertex has low oblique loop-like writing, with a central narrowing compatible with infinity. Red and grey strokes merge with the right part. The ink does not make both loops fully separable, so the leading infinity reading remains doubtful.',
      crop=cropby['left_label']['crop'],box=cropby['left_label']['box'],confidence='low'),
 dict(id='M0947',decision='undecided',reading=r'\unsure{1}',
      evidence='A short slanting stroke with a small cap or foot lies to the lower-left of the upper-central vertex. It favours 1, but the adjoining f--e and b--e graph strokes prevent a secure isolation of the whole numeral. The reading is not settled by an assumed 0/1/infinity colouring.',
      crop=cropby['inner_labels']['crop'],box=cropby['inner_labels']['box'],confidence='low')]
doubts=[]
for decision,place in zip(decisions,[
    'Upper-left vertex label a at (859,349)',
    'Upper vertex label b at (989,335)',
    'Left boundary vertex label d at (714,490)',
    'Upper-central vertex label e at (980,501)']):
    doubts.append(dict(place=place,reading=decision['reading'],alternatives='No secure second reading from the visible ink.',confidence='low',reason=decision['evidence']))

inventory=[
 dict(element='E01',sheet_kind='text',hand='his hand',kind='drawing',position='Central-left drawing, including the ten exterior rays',first_words_or_objects='Sixteen finite vertices, thirty-five finite graph edges, ten rays',transcribed='yes'),
 dict(element='E02',sheet_kind='text',hand='his hand',kind='drawing',position='Red overlay throughout the central-left drawing',first_words_or_objects='Red contours, local projections, pen breaks and sixteen small vertex loops',transcribed='yes'),
 dict(element='E03',sheet_kind='text',hand='his hand',kind='display',position='Sixteen short labels at the graph vertices',first_words_or_objects=r'\unsure{\infty}, \unsure{\infty}, 1, \unsure{\infty}, \unsure{1}, 0, \infty, 0, 1, \infty, 1, \infty, 0, 1, \infty, 1',transcribed='yes'),
 dict(element='E04',sheet_kind='text',hand='his hand',kind='drawing',position='Narrow black strip beside the upper-right perimeter edge',first_words_or_objects='Six projecting chevron-like turns with irregular joins',transcribed='yes'),
 dict(element='E05',sheet_kind='text',hand='unnamed hand (folio annotation; attribution uncertain)',kind='text',position='Extreme lower-left corner',first_words_or_objects='68',transcribed='yes')]

notes=[
 dict(id=f'{PAGE}-N01',text='This leaf contains a drawing and the folio 68, with no prose theorem, legend or title. Sixteen finite vertices and ten exterior rays are visible. The vertex letters a through p used in the TikZ are editorial coordinate handles only and are not printed.'),
 dict(id=f'{PAGE}-N02',text='A computation on the manually transcribed finite graph found 35 edges, an outer boundary of length 10 and 20 triangular bounded face cycles. Thus V-E+F=16-35+21=2 and E=3V-b-3=35. The directly visible g--h edge, omitted by C, divides e--g--i--h into two triangles. The check supports the observed incidence; it did not supply an unseen edge.'),
 dict(id=f'{PAGE}-N03',text='No proper 0/1/infinity colouring is assumed. In particular the leading doubtful readings at a and b would both be infinity in the triangle a--b--f. The four obscured labels remain uncertain. The leaf itself gives no rule from which their values could be deduced.'),
 dict(id=f'{PAGE}-N04',text='H describes a spherical map and a pants decomposition. These are editorial descriptions, not words written on the leaf. The transcription reproduces the drawing without adding those phrases or asserting a global interpretation of the red curves.'),
 dict(id=f'{PAGE}-N05',text='The dense red layer is represented by direct filled vector outlines of the visible colour-separated ink after visual inspection. Only tiny isolated components below five pixels were excluded. No dilation, gap closing, smoothing or hole filling was used; closed outline polygons enclose pen strokes rather than asserting closed contour centrelines. The black overdraw was traced locally with the same principle. Graph incidence and label readings were transcribed manually. The retained geometry preview was produced independently of TeX; no TeX compilation was run.')]
check_events=[dict(statement_id=f'{PAGE}-N02',type='computation or formal certificate',
    outcome='Actually ran proposed/148_scan069_incidence_check.py on the saved 16-vertex, 35-edge model. Its rotation-system face walk used every directed edge once and returned twenty 3-cycles plus the 10-edge outer face; it checked Euler value 2 and 35=3*16-10-3. It identified the two triangles adjacent to g--h. The result is saved in proposed/148_scan069_incidence_check.json. The scope is the finite graph incidence, not the uncertain labels or red-curve topology.')]
notation=[
 dict(sign=r'0, 1, \infty',meaning_or_form='Literal vertex annotations; no explanatory legend on this leaf. The infinity forms are compact paired loops, sometimes oblique or nearly vertical. Several labels sit within their small red loops rather than uniformly below the vertices.',places='All sixteen vertex labels; four obscured forms at a,b,d,e',universality='Twelve labels are clear on their crops; the four supplied C doubts remain. No colouring rule is inferred.',witness_errors='C retains the same four value doubts but uniformly displaces all labels below-right; H supplies only generic label names, without the individual mapping.'),
 dict(sign='Grey graph strokes, dark retracings, red curves and black projecting turns',meaning_or_form='Distinct visible layers of the drawing; the small red loops and local pen gaps are reproduced as shapes.',places='The complete drawing, especially the upper-left fan and upper-right black strip',universality='The distinction is applied throughout this leaf; no meaning for the colours or stroke weights is stated.',witness_errors='C reverses several grey/dark strokes, omits g--h, smooths red gaps and replaces the six-turn black shape by three generic arrows. H describes the figure verbally.')]

data=dict(page=PAGE,reader='reader_a',lines_read=17,
    line_count_basis='Sixteen separate handwritten vertex-label units and the folio; no prose lines.',
    places_cropped=7,crop_files_saved=9,crop_files_viewed=9,
    changes=changes,decisions=decisions,implicit_decisions=[],doubts=doubts,inventory=inventory,
    notes=notes,check_events=check_events,notation=notation,abbreviations=[],
    second_boxes=[
        dict(box='B01',kind='doubtful formula',x0=380,y0=75,x1=1560,y1=1250,reading=figure,
            covers=['Entire drawing','All sixteen handwritten labels','All four doubtful label groups','Every graph edge and exterior ray','All red contours, loops, gaps and projections','Black six-turn overdraw']),
        dict(box='B02',kind='handwritten number',x0=22,y0=1612,x1=68,y1=1666,reading=r'\mspage{68}')],
    crops=crops,
    workflow=dict(original_viewed_once=True,half1_viewed_once=True,half2_viewed_once=True,
        all_agreed_ink_read=True,source_crops_viewed=9,discarded_image_outputs_counted=False,
        generated_preview_viewed=True,tex_compiled=False,ocr_used=False,web_used=False),
    geometry_production=dict(method=geometry['method'],red_outline_loops=len(geometry['red_paths']),
        red_outline_vertices=sum(map(len,geometry['red_paths'])),black_outline_loops=len(geometry['black_paths']),
        black_outline_vertices=sum(map(len,geometry['black_paths'])),red_stats=geometry['red_stats'],
        black_stats=geometry['black_stats'],working_files=[f'proposed/{PAGE}_{suffix}' for suffix in [
            'crops.py','detail_crops.py','crop_boxes.json','vector_trace.py','vector_geometry.json',
            'red_geometry.tex','black_geometry.tex','proposal.py','parts.json','geometry_preview.png',
            'incidence_check.py','incidence_check.json','metadata.py']]))
(out/f'{PAGE}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(changes),decisions=len(decisions),doubts=len(doubts),
    audit_boxes=len(data['second_boxes']),crop_files=len(crops),places_cropped=7,
    metadata_bytes=(out/f'{PAGE}.json').stat().st_size)))
