from pathlib import Path
import json,copy
b=Path('/workspace/scratch/b9993b8b5640');o=b/'out';p='A57-02_57_scan076'
r=json.loads((o/'readers'/p/'R1/report.json').read_text())
paths=[o/'readers'/p/'R3/crops/01_cancelled_morphism.png',o/'adjudication'/p/'proofsbeing.png',o/'readers'/p/'R1/crops/cancelled_mumford.png',o/'readers'/p/'R1/crops/cancelled_mumford.png',o/'readers'/p/'R1/crops/overtyped_to.png',o/'readers'/p/'R1/crops/deleted_continuation.png',o/'readers'/p/'R3/crops/06_handwritten_m.png',o/'readers'/p/'R1/crops/deleted_continuation.png',o/'readers'/p/'R3/crops/04_raised_f.png',o/'adjudication'/p/'is_space.png']
final0=r"\deleted{\unsure{morphism (namely that|morphism(with $X$ prjt|morphism(with $Y$ prjt}}"
shows=[
 'The crossed text begins morphism and a parenthesis. Compressed bowls and stems and a descending stroke before the final that-like group favor morphism (namely that. The typed x cancellation obscures enough central strokes that the two C readings remain explicit alternatives. Root prefers R3/H lexical reading, with lower confidence than R3 and no certainty adopted from H.',
 'The s of proofs and b of being occupy adjacent typewriter positions, with no blank position between them.',
 'The crossed layer retains and, the capital M and successive um shoulders, tall f, ord, apostrophe and s. The nearby uncancelled Mumford\'s supplies a same-page letter comparison. Root agrees with R1/R3 that the words are recoverable.',
 'The closing parenthesis of (i) directly precedes the crossed and, without a blank typewriter position. This spacing row does not recount the separate resolution of the cancelled words.',
 'The first position before o contains the tall stem, shoulder and right leg of h together with a t crossbar. Their superposition is visible; the order and live-layer assignment remain unclear. Both assignments are retained, deleted layer first in each alternative.',
 'The comma follows X and is immediately followed by Y; no blank typewriter position separates comma and Y.',
 'The inserted surjective has a continuous heavy underline immediately below its letters; the curved attachment bracket places it before S-morphis. H preserves the insertion but omits this underline.',
 'The crossed line opening retains the two shoulders and baseline of m, followed by a legible comma; diagonal cancellation strokes cross that typed continuation. The corresponding handwritten m, appears at the preceding line end.',
 'The raised mark is a compact dark round spot with no recoverable pale centre or elongated prime shaft. Root follows the filled-point reading of R1/R3. H cdot and the final bullet both encode this same filled raised point, so no H row is counted.',
 'A full blank typewriter position separates s from the baseline full stop.'
]
changes=[]
for i in range(10):
 e={'source':['R1',i],'reader_sources':{x:i for x in ['R1','R2','R3']},'evidence':str(paths[i]),'crop':str(paths[i]),'scan_shows':shows[i],'mathematical_consequence':None}
 if i==0:e.update(final=final0,differs_c=True,confidence='low')
 if i==4:e['confidence']='low'
 if i==7:e['h_marked']='yes'
 if i==8:e.update(differs_h=False,confidence='medium')
 changes.append(e)
cd=copy.deepcopy(r['c_doubts'])
cd[0].update(reading=final0,status='revised',crop=str(paths[0]),evidence=shows[0],confidence='low')
cd[1].update(crop=str(paths[2]),evidence=shows[2])
cd[2].update(crop=str(paths[4]),evidence=shows[4],confidence='low')
cd[3].update(crop=str(paths[8]),evidence=shows[8],confidence='medium')
rd=[{'place':'Opening paragraph, cancelled phrase after simple','reading':'morphism (namely that','alternatives':['morphism(with $X$ prjt','morphism(with $Y$ prjt'],'confidence':'low','reason':shows[0],'crop':str(paths[0])},{'place':'Opening paragraph, first character before o reduce','reading':r'\deleted{h}t','alternatives':[r'\deleted{t}h'],'confidence':'low','reason':shows[4],'crop':str(paths[4])}]
notes=copy.deepcopy(r['notes'])
notes['reading_decisions']=[{'place':'Statement (i), raised f mark','readings':r"f^{\bullet}, f^{\circ}, f'",'reason':'The label on the displayed-in-prose Picard map required inspection of its small raised mark. The dark filled spot supports the first reading; the visibly written source Y/S and target X/S were preserved. No property of that map was used to choose the glyph.'}]
notation=copy.deepcopy(r['notation'])
notation[-1]={'sign':'cancelled opening phrase','latex':final0,'place':'Opening paragraph after simple','visible_shape':shows[0],'alternatives':['morphism(with $X$ prjt','morphism(with $Y$ prjt']}
cfg={'base_reader':'R1','replacements':[{'old':r['changes'][0]['reading'],'new':final0}],'changes':changes,'c_doubts':cd,'remaining_doubts':rd,'inventory_edits':[{'index':4,'first_words_or_objects':'morphism (namely that; alternatives morphism(with X/Y prjt retained beneath x cancellation'}],'notes':notes,'notation':notation,'adjudicated_crops':list(dict.fromkeys(map(str,paths))),'rejected_difference_rows':[{'reader':'R3','place':'raised mark on f','decision':'The proposed H cdot versus final bullet difference is excluded: both encode the same raised filled point seen in the crop.'}]}
(o/'adjudication'/p/'decision.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
with (o/'records/tool_delivery_notes.md').open('a') as f:f.write('\nScan 076, main reader: the first attempted delivery of deleted_continuation.png and 06_handwritten_m.png was wholly truncated at a context limit; neither image reached the reader. The two existing files were then resent individually and first inspected. The same discarded-result call had successfully created proofsbeing.png and is_space.png; those existing crops were each first viewed individually. No crop was regenerated.\n')
with (o/'notation.md').open('a') as f:
 f.write('\n## Evidence added at cote 57, scan 076\n\n| Sign | Reading | Place | Visible form / residual alternatives |\n|---|---|---|---|\n')
 for n in notation[:-1]:f.write('| '+n['sign']+' | `'+n['latex'].replace('|',r'\|')+'` | '+n['place']+' | '+n['visible_shape'].replace('|',r'\|')+' |\n')
brief=(o/'briefs/reader_brief_v05.md').read_text().replace('brief v05','brief v06',1).replace('First used: cote 57, scan 075.','First used: cote 57, scan 077.',1)
brief=brief.replace('Emit no more than three crop images in one tool result to avoid output truncation.','Emit one or at most two crop images in one tool result to avoid output truncation.')
brief+='\n\n## Clarifications introduced in v06\n\n- A three-image result still discarded a crop on scan 076. Prefer one image per tool result, with two only when small; the resend-without-recropping rule applies to any explicitly unseen output.\n- H `f^{\\cdot}` and C `f^{\\bullet}` map to the same visible filled raised point when the ink establishes that shape. Do not count the macro names as a reading difference. An actual open ring or prime remains a separately judged glyph.\n'
(o/'briefs/reader_brief_v06.md').write_text(brief)
pb=o/'records/brief_changes.json';z=json.loads(pb.read_text());z.append({'version':'v06','first_page':'A57-02_57_scan077','reasons':['A three-image result discarded R1\'s third scan-076 crop. The brief now recommends one image per output, at most two small images.','R3 counted H cdot versus bullet on scan 076 despite both encoding the same visible raised filled point. This correspondence is now explicit.']});pb.write_text(json.dumps(z,ensure_ascii=False,indent=2))
