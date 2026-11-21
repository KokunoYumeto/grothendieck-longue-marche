from pathlib import Path
import json,re

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'; OUT=ROOT/'proposed'
C=(ROOT/'packets'/PAGE/'C.tex').read_text()
H=(ROOT/'packets'/PAGE/'H.tex').read_text()
T=(OUT/f'{PAGE}.tex').read_text()
parts=json.loads((OUT/f'{PAGE}_parts.json').read_text())
geometry=json.loads((OUT/f'{PAGE}_vector_geometry.json').read_text())
crops=json.loads((OUT/f'{PAGE}_crop_boxes.json').read_text())
for crop in crops: crop['viewed']=True; crop['main_reader_viewed']=True
(OUT/f'{PAGE}_crop_boxes.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n')
bycrop={c['name']:c for c in crops}
first=C.index(r'\figure{'); first_end=C.index(r'\end{tikzpicture}}',first)+len(r'\end{tikzpicture}}')
second=C.index(r'\figure{',first_end); second_end=C.index(r'\end{tikzpicture}}',second)+len(r'\end{tikzpicture}}')
c_left=C[first:first_end]; c_right=C[second:second_end]
h_note=H[H.index(r'\note{à gauche'):H.index(r'\end{document}')].strip()
figure=T[T.index(r'\figure{'):T.index('% crop-candidate:')].strip()
def lines_matching(text,predicate): return '\n'.join(line for line in text.splitlines() if predicate(line))
c_red=lines_matching(c_left,lambda s:'red!55!black' in s)
c_graph=lines_matching(c_left,lambda s:s.startswith(r'\coordinate') or (s.startswith(r'\draw[') or s.startswith(r'\fill[')) and 'red' not in s)
red=parts['red_supplement_tex']+'\n'+(OUT/f'{PAGE}_red_geometry.tex').read_text().strip()
tip=(OUT/f'{PAGE}_ray_tip_geometry.tex').read_text().strip()
upper_nodes=lines_matching(parts['right_complete_tex'],lambda s:s.startswith(r'\node[') and any(f'at ({x},{y})' in s for x,y in [(1730,693),(1730,765),(1781,760)]))
c_upper=next(line for line in c_right.splitlines() if 'at (1730,693)' in line)
changes=[]
def add(place,c,h,final,diff_c,diff_h,kind,error,evidence,crop,confidence='high',consequential=False,extra=None):
    cp=bycrop[crop]
    row=dict(id=f'{PAGE}-{len(changes)+1:02d}',place=place,c=c,h=h,final=final,
        diff_c=diff_c,diff_h=diff_h,kind=kind,error_kind=error,evidence=evidence,
        crop=cp['crop'],box=cp['box'],confidence=confidence,marked_in_h=False,consequential=consequential)
    if extra: row.update(extra)
    changes.append(row)

add('Caption, first line, adjective after découpage','pantalonique','pantalonnesque',
    r'\unsure{pantalonnesque|pantalonesque}',True,False,'misread word','Words',
    'After the tall looped l and the low o, the final run has an s-like rising finish, a long descending q and the following u/e: -esque is visible, so C -ique is not supported. The low arches between lo and esque are compressed, and their count cannot securely distinguish n from nn. The H spelling is retained first, with the single-n alternative explicit. Both caption lines, accents and parentheses were also read directly.',
    'title',confidence='low')
add('Left drawing, complete red layer',c_red,h_note,red,True,True,'drawing or diagram','Drawings and diagrams',
    'There are eight extended red routes, eleven small vertex enclosures, and an additional small lobe attached beside g. C supplies a ninth extended smooth cycle starting at (900,467); its long segment follows the grey doubled c--f pencil trace, where left_inner shows no independent long red curve. H count eight agrees with the ink, but its prose does not reproduce the drawing. The actual red loops, local thickened projections, dots and small openings replace C regular ellipses and generic arrows. Colour-separated vector outlines are supplemented only along four source-visible continuous brown stretches that the initial mask missed: the outer-left crossing at y850--891 and three inner flanks at approximately y500--860.',
    'left_graph',consequential=True,extra={'supporting_crops':[bycrop['left_inner']['crop']],
    'geometry_method':'Visible red-ink vector outlines plus four manually traced continuous stretches; no automatic global component closing.'})
add('Left pencil graph, retracing, marked vertices and seven rays',c_graph,h_note,parts['left_graph_tex'],True,True,
    'drawing or diagram','Drawings and diagrams',
    'Eleven junctions, twenty-three distinct finite endpoint joins and seven exterior rays are visible. The c--f connection has two closely spaced grey pencil traces; both are drawn, without treating their multiplicity as an additional endpoint incidence. Broad grey joins such as a--b, b--h, c--h, g--j and h--k contrast with thin darker a--d, e--i and f--j, while a--e is particularly faint. C reverses several of these stroke distinctions and uses uniformly oversized filled vertex disks; the source marks are smaller irregular dark patches. The curved traces and rays are reproduced at their observed positions.',
    'left_graph',extra={'supporting_crops':[bycrop['left_inner']['crop']]})
add('Tip of the upper-left ray in the left drawing',
    r'\draw[black] (a) .. controls (443,452) and (324,310) .. (214,216);','absent',tip,
    True,True,'drawing or diagram','Drawings and diagrams',
    'The end has a short nearly horizontal return above the diagonal shaft and a small upright projection farther down the shaft. The shape suggests an arrowhead, but its semantics are uncertain. The actual dark outline is retained rather than replacing it by a conventional arrow or C bare terminal line. H does not describe the terminal decoration.',
    'upper_left_ray')
add('Complete right graph, local weight positions and drawn enclosures',c_right,h_note,parts['right_complete_tex'],
    True,True,'drawing or diagram','Drawings and diagrams',
    'The graph has a six-sided cycle, two lower stems, a lower-left fork, six exterior rays and one loop attached to the lower-right vertex. Eight dark vertices and twenty-three numerical annotations were read individually. The three enclosures surround 1, 2 and 3 at their actual positions; the last enclosure has a small upper-right opening. The rightward ray has an irregular thickening and pointed end, preserved as a local outline. C regularizes these enclosure/ray shapes. H gives only a compressed verbal description and number list, without the complete incidence-to-weight mapping. The source values otherwise agree with C, including 15, 17 and the repeated 3, 4 and 5 labels.',
    'right_graph')
add('Right graph, the upper vertex and its three nearby weights',c_upper,'$9$, $19$',upper_nodes,
    False,True,'misread symbol or index','Symbols and indices',
    'A small looped 9 lies beside the upward branch. Below the vertex, a large flagged 1 with a horizontal foot lies by the lower-left branch, and a separate large looped 9 lies by the lower-right branch. Their placements on the two sides of the vertex are distinct; H combines the lower pair into 19. The flagged first digit of the separate 15 at the leftmost vertex was compared with this large 1 and supports C/H 15.',
    'right_graph',consequential=True)
add('Isolated small mark inside the left drawing',r'\unsure{1}','absent',r'\unsure{1}',False,True,
    'omission','Omissions',
    'A small dark upright-to-curved stroke with a faded lower-left continuation lies between the central pencil connection and the right-hand red flank, at approximately (925,601). Its form can resemble a numeral 1 or a comma-like mark, but neither identity is secure. C doubt is retained. H omits this visible ink group.',
    'left_mark',confidence='low')
add('Lower-left folio',r'\mspage{71}','absent',r'\mspage{71}',False,True,'omission','Omissions',
    'The first digit has an upper bar, descending stem and middle crossbar, giving 7. The following digit has a diagonal entry flag and a single long upright, giving 1. The pale annotation is 71; H omits it.',
    'folio')

decisions=[dict(id='M0950',decision='undecided',reading=r'\unsure{1}',
    evidence='The isolated group has a short dark upright and curved lower-left continuation, with no secure detached cap or complete numeral foot. It could be a small 1, but is also comma-like. The close crop does not resolve its identity; no mathematical role is inferred.',
    crop=bycrop['left_mark']['crop'],box=bycrop['left_mark']['box'],confidence='low')]
doubts=[
 dict(place='Caption adjective after découpage',reading=r'\unsure{pantalonnesque|pantalonesque}',
      alternatives='pantalonnesque; pantalonesque',confidence='low',
      reason='The ending -esque is visible. The compressed low arches after lo do not securely distinguish nn from n.'),
 dict(place='Small isolated mark at approximately (925,601) in the left drawing',reading=r'\unsure{1}',
      alternatives='1; comma-like stroke without a securely identified textual function',confidence='low',reason=decisions[0]['evidence'])]
inventory=[
 dict(element='E01',sheet_kind='text',hand='his hand',kind='text',position='Two-line caption at upper right',first_words_or_objects=r'découpage \unsure{pantalonnesque|pantalonesque}',transcribed='yes'),
 dict(element='E02',sheet_kind='text',hand='his hand',kind='drawing',position='Large left pencil graph and its seven exterior rays',first_words_or_objects='Eleven marked junctions; twenty-three distinct finite joins; doubled c--f trace; decorated upper-left ray tip',transcribed='yes'),
 dict(element='E03',sheet_kind='text',hand='his hand',kind='drawing',position='Red layer of the large left drawing',first_words_or_objects='Eight extended red contours, eleven vertex enclosures and an attached extra lobe beside g',transcribed='yes'),
 dict(element='E04',sheet_kind='text',hand='his hand',kind='display',position='Inside the left drawing, near (925,601)',first_words_or_objects=r'\unsure{1}',transcribed='yes'),
 dict(element='E05',sheet_kind='text',hand='his hand',kind='drawing',position='Right-hand weighted graph',first_words_or_objects='Eight vertices; six-sided cycle; two lower stems; fork; loop; six rays',transcribed='yes'),
 dict(element='E06',sheet_kind='text',hand='his hand',kind='display',position='Twenty-three local numerical annotations on the right graph',first_words_or_objects='3, 6, 15; 9, 1, 9; 3, 3, 7; 2, 1, 5; 4, circled 2, circled 3; circled 1, 5, 4; 4, 2; 17, 3, 3',transcribed='yes'),
 dict(element='E07',sheet_kind='text',hand='unnamed hand (folio annotation; attribution uncertain)',kind='text',position='Extreme lower-left corner',first_words_or_objects='71',transcribed='yes')]
notes=[
 dict(id=f'{PAGE}-N01',text='The caption identifies the drawing as a pants-style decomposition of a triangulated map. Its coined adjective ends in -esque; the single/double n remains uncertain. The two drawings and caption are reproduced in one common coordinate frame to retain their positions on the leaf. Editorial coordinate letters are not printed.'),
 dict(id=f'{PAGE}-N02',text='The left drawing has eleven junctions and twenty-three distinct finite endpoint joins, with seven exterior rays. Both visible c--f pencil traces are retained. A face walk on the simple endpoint-incidence model returned thirteen triangular bounded faces and a seven-edge outer boundary, with 11-23+14=2. This is a conditional consistency check of that incidence model, not a claim that two physical traces must represent two different edges or a reason to identify the doubtful small mark.'),
 dict(id=f'{PAGE}-N03',text='The right drawing has eight vertices, nine finite edges including its loop, and six exterior rays. Counting the loop twice at its vertex gives degree three at every vertex. Its connected finite core has first Betti number 9-8+1=2. Twenty-three numeric annotations are visible; no number is supplied for the third local branch at the lower-left fork. The calculation does not impose a compatibility rule on the written numbers.'),
 dict(id=f'{PAGE}-N04',text='The separate 1 and 9 below the upper right-graph vertex are local branch annotations, not one number 19. The two ends of other edges can carry different nearby numbers, so the transcription preserves every local placement. The leaf contains no written theorem or numerical rule that would justify changing them.'),
 dict(id=f'{PAGE}-N05',text='The red geometry uses colour-separated vector outlines after visual reading, with manually traced thin paths along four specific source-visible continuous stretches that the initial threshold omitted. The actual small enclosure openings remain. The local upper-left tip and rightward-ray thickening are also vector shapes. A clipped fragment of the nearby numeral 5 was excluded from the ray mask because the complete 5 is separately typeset. Filtered mask-to-polygon export was checked for pixel equality; this production check is not a mathematical proof. The drawing remains an explicit TikZ approximation, with evidence crops and generators retained. No TeX engine was invoked.')]
check_events=[
 dict(statement_id=f'{PAGE}-N02',type='computation or formal certificate',outcome='Actually ran proposed/148_scan072_incidence_check.py. The left rotation-system face walk traversed all 46 directed incidences of the 23 distinct endpoint joins, obtaining thirteen triangles and a seven-edge outer face, with Euler value 2. The doubled physical trace is stored separately. The result is in proposed/148_scan072_incidence_check.json.'),
 dict(statement_id=f'{PAGE}-N03',type='computation or formal certificate',outcome='The same retained script counted eight right-graph vertices, nine finite edges including the loop and six rays, verified connectedness of the finite core and degree three at all vertices after counting the loop twice, and computed first Betti number 2. It did not check or infer any arithmetic relation among the twenty-three written annotations.')]
notation=[
 dict(sign='Flagged 1; crossed 7',meaning_or_form='The large 1 below the upper vertex has a diagonal entry flag and horizontal foot; the first digit of 15 has the same structure. The 7 is crossed in the graph and folio.',places='Right graph: large 1, 15, 7 and 17; lower folio 71',universality='These clear occurrences were compared locally. The separate small doubtful mark in the left drawing is not resolved from them.',witness_errors='H combines the upper vertex lower pair 1 and 9 into 19. Both witnesses preserve 15; the ink confirms it.'),
 dict(sign=r'\unsure{pantalonnesque|pantalonesque}',meaning_or_form='The final -esque has a long q descender and following u/e; the preceding low n/nn sequence is compressed.',places='First line of the caption',universality='One occurrence only.',witness_errors='C gives pantalonique; H gives pantalonnesque without retaining uncertainty over the n count.'),
 dict(sign='Grey doubled trace beside red contours',meaning_or_form='The c--f connection has two close pencil traces; the red inner contour remains a separate route.',places='Central area of the left drawing',universality='One visible retraced connection on this leaf; no general graph convention is inferred.',witness_errors='C adds a ninth extended red cycle along this pencil trace. H counts eight extended red curves, which the ink supports.'),
 dict(sign='Numerical labels at individual branches',meaning_or_form='Separate local annotations are positioned around each right-graph vertex. Three annotations have drawn enclosures, around 1, 2 and 3.',places='All twenty-three right-graph labels',universality='Every visible numeral was checked; no unprinted value is supplied for the unlabelled branch.',witness_errors='H compresses the mapping into a prose list and combines one separate 1/9 pair. C retains the numerical values but regularizes the enclosure shapes.')]

data=dict(page=PAGE,reader='reader_a',lines_read=27,
    line_count_basis='Two caption lines, twenty-three separate numerical label units on the right graph, one isolated doubtful mark on the left, and the folio.',
    places_cropped=7,crop_files_saved=7,crop_files_viewed=7,
    changes=changes,decisions=decisions,implicit_decisions=[],doubts=doubts,
    inventory=inventory,notes=notes,check_events=check_events,notation=notation,abbreviations=[],
    second_boxes=[dict(box='B01',kind='doubtful formula',x0=195,y0=75,x1=2300,y1=1360,reading=figure,
        covers=['Both complete drawings','Entire two-line caption including the differing word','The isolated C doubt','All twenty-three right-graph numerical annotations','All stroke decorations and three numerical enclosures']),
        dict(box='B02',kind='handwritten number',x0=24,y0=1616,x1=86,y1=1665,reading=r'\mspage{71}')],
    crops=crops,workflow=dict(original_viewed_once=True,half1_viewed_once=True,half2_viewed_once=True,
        all_agreed_ink_read=True,source_crops_viewed=7,generated_preview_viewed=True,
        tex_compiled=False,ocr_used=False,web_used=False),
    geometry_production=dict(method=geometry['method'],manual_red_supplements=parts['red_supplements'],
        layers=[dict(name=l['name'],box=l['box'],paths=len(l['paths']),vertices=sum(map(len,l['paths'])),
            threshold=l['threshold'],stats=l['stats'],filtered_mask_export_identical=l['vector_export_identical_pixels']) for l in geometry['layers']],
        working_files=[f'proposed/{PAGE}_{s}' for s in ['crops.py','crop_boxes.json','vector_trace.py',
            'vector_geometry.json','red_geometry.tex','ray_tip_geometry.tex','right_ray_geometry.tex',
            'proposal.py','parts.json','geometry_preview.png','incidence_check.py','incidence_check.json','metadata.py']]))
(OUT/f'{PAGE}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(changes),decisions=len(decisions),doubts=len(doubts),
    crop_files=7,audit_boxes=2,metadata_bytes=(OUT/f'{PAGE}.json').stat().st_size)))
