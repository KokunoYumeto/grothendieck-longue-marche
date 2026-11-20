from pathlib import Path
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/017/A')
tex=(out/'reading.tex').read_text()
needle="-- c'est aussi la partition definie"
addition=r'''% G11: two detached marks at far right between display and lower prose.
% Full-scan origin (1567,1735), fixed local rectangle 18 by 20.
% Shapes only: character, role, hand and surface origin remain unestablished.
\margin{\unsure{\begin{tikzpicture}[x=0.02cm,y=-0.02cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (18,20);
\fill (9,5) .. controls (11,4) and (13,6) .. (11,9) .. controls (8,10) and (8,7) .. cycle;
\fill (4,12) .. controls (7,11) and (8,14) .. (5,15) .. controls (3,16) and (2,13) .. cycle;
\end{tikzpicture}}}

'''
tex=tex.replace(needle,addition+needle,1)
(out/'reading.tex').write_text(tex)
r=json.loads((out/'report.json').read_text())
r['differences'].append({'id':'A017-D39','location':'Far right between partition display and final paragraph','C':'omitted','H':'omitted','reading':'G11: two separate dark point shapes under local unsure qualification','evidence':'The final tight crop shows two compact dark patches on a rising diagonal, separated by white paper. Both shapes are retained graphically without assigning a character, hand, role or surface origin.','confidence':'medium','kind':'drawing or diagram','diff_C':True,'diff_H':True,'C_doubt_status':None,'readers_crop':'20_right_detached_marks.png','bbox':[1570,1739,1581,1751],'physical_cluster':'G11','components':[{'component':'upper patch','shape_confidence':'high','interpretation_confidence':'low'},{'component':'lower patch','shape_confidence':'high','interpretation_confidence':'low'}]})
r['doubts'].append({'location':'far right between display and final prose','reading':'two separate dark point shapes','alternatives':[],'confidence':'medium','reason':'visible shapes clear; character, role, hand and surface origin unestablished','crop':'20_right_detached_marks.png','difference':'A017-D39'})
r['inventory'].insert(25,{'sheet_kind':'text','hand':'undetermined hand','element':'017.A.37','kind':'drawing','position':'far right between partition display and final paragraph','first_words_or_objects':'G11 two detached point shapes, one upper-right and one lower-left, locally qualified','transcribed':'yes','components':['G11 fill path1 upper patch','G11 fill path2 lower patch'],'role':'unestablished','surface_origin':'unestablished'})
r['crops']=json.loads((out/'crop_manifest.json').read_text())
r['notes']['workflow']='Brief read first; current UTC start was then recorded before packet/image reading. Whole scan opened once for layout, half a once, half b once. Sixteen initial distinct tight crops, three later previously uncropped accent loci, and one final previously uncropped detached-mark locus were each displayed once. The final mark crop followed the initial source-only structural check. No successfully viewed image or decided target was reopened. No crop retry occurred.'
r['notes']['graphics']='G01 and G08 each contain two literal draw paths. G02,G03,G04,G07,G09,G10 each contain one. G11 contains two separate fill paths. G05 is represented once by a qualified prime/dot candidate, and G06 once by a qualified baseline point. Every insertion-guide path appearing in reading.tex has its own difference and inventory item. Local drawing origins, rectangles, coordinate units, baselines and zero-separation base-west text anchors are declared in TeX; font extents are not asserted to coincide with source boxes.'
r['notes']['actual_computations'][2]['inputs']='twenty exact boxes in crop_manifest.json'
r['notes']['actual_computations'][2]['result']='twenty PNGs with recorded input/output dimensions in crop_manifest.json'
r['notes']['actual_computations'][3]['result']='hand-estimated full-scan path anchors declared for G01-G11 in reading.tex/report'
r['notes']['actual_computations'].append({'operation':'initial source-only structural check','inputs':['reading.tex before G11 addition','report.json before G11 addition','crop_manifest.json before crop20'],'result':{'reported_error':'empty line inside display','source_rows':12,'source_parts':19,'difference_rows':38,'draw_path_commands':10,'crop_files':19},'scope':'The empty-line report was caused by stripping a comment-only line into a blank line in the checker. The source had no empty physical line there. The checker is repaired to inspect physical display lines; no compiler or renderer was invoked.'})
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(out/'source_check_initial.json').write_text((out/'source_check.json').read_text())
p=out/'verify_sources.py'; s=p.read_text(); s=s.replace("for disp in re.findall(r'\\\\\\[(.*?)\\\\\\]',body,re.S):", "for disp in re.findall(r'\\\\\\[(.*?)\\\\\\]',tex,re.S):")
# The direct string above is deliberately verified below instead of relying on an unobserved replacement.
if ",tex,re.S):" not in s:
 s=s.replace(",body,re.S):\n if '\\n\\n' in disp", ",tex,re.S):\n if '\\n\\n' in disp")
p.write_text(s)
print('Added G11 and recorded its two components; synchronized report and crop manifest. Preserved initial checker result.')
