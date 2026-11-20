from pathlib import Path
from datetime import datetime, timezone
import json,re
root=Path('/workspace/scratch/4770596940a0')
base=root/'out/readers/R2'
D=[]
def add(id,place,C,H,reading,ink,confidence,kind,crop,against_C,against_H,marked_in_H=False):
 D.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop=crop,against_C=against_C,against_H=against_H,marked_in_H=marked_in_H))
add('D01','a), initial F',r"\unsure{F|\mathcal F}'","F'","F'",'Upright with two separated arms; no separate script flourish. Matches ordinary F on this sheet.',0.93,'C_doubt_resolved',['top'],True,False)
add('D02','opening display, cancelled operator after |F\\G|',r'\deleted{\unsure{=|\supset}}','omitted',r'\deleted{\unsure{=|\supset}}','Two horizontal traces and a rounded right closure are obscured by a heavy oval/diagonal cancellation; cannot separate original closure from cancellation.',0.54,'C_doubt_retained;H_omission',['top_deleted','relation_comparators'],False,True)
add('D03','proof demand, plus petit ... de F′',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Accented opening, tall l, compressed medial sweep and terminal t; the intervening letter count remains unsettled.',0.69,'C_doubt_retained;abbreviation',['argument','word_element_top'],False,True)
add('D04','case 1, small worked-over mark after G′',r"G'\deleted{\unsure{\circ}}","G'",r"G'\deleted{\unsure{\circ}}",'Small black angular blot immediately after prime. No clean live circle is recoverable; retained as the doubtful cancelled circle recorded by C. Deletion state is itself less secure than the existence of the blot.',0.52,'C_doubt_retained;H_omission;deletion_state',['first_symbols'],False,True)
add('D05','case 1, closing high curve of A circle(G′)',r"A^{\circ(G')\deleted{\unsure{)|?}}}",r"A^{\circ(G')}",r"A^{\circ(G')\deleted{\unsure{)|?}}}",'Closing curve has extra dark retracing and a small lower hook; retain the doubtful extra cancelled parenthesis/hook rather than silently regularize it.',0.49,'C_doubt_retained;H_omission',['first_symbols'],False,True)
add('D06','case 1, full cancelled fragment before x∈B',r'\deleted{\unsure{B}}',r'\struck{\ill{}}',r'\deleted{$B\ni$}','Two bowls survive under the crossed capital. At its right is a separate reversed-membership curve with a middle horizontal bar; cancellation extends as a fragment B∋, not just the letter.',0.94,'C_doubt_resolved;fragment_extent;H_illegible_resolved',['first_deleted','first_cancel_context'],True,True,True)
add('D07','case 1, final raised mark on A',r'A^{\unsure{\bullet|\circ}}',r'A^{*}; note astérisque ou rond appuyé',r'A^{\unsure{\circ|\bullet}}','Irregular thick annular mark, with a small pale centre. No distinct radial asterisk strokes. Prefer a retraced circle, retain filled-mark alternative.',0.70,'C_doubt_revised_preference;math_symbol',['first_final_mark'],True,True,True)
add('D08','case 2, old letter below F within support bars',r'|\deleted{\unsure{G}}F|','|F|',r'|\deleted{\unsure{G}}F|','Live F has a rounded lower/left residue under its stem. A prior G fits, but overwriting prevents a secure original-letter reading.',0.59,'C_doubt_retained;H_omission',['second_overwrites'],False,True)
add('D09','case 2, old letter below A after alors les',r'\deleted{\unsure{B}}A','A',r'\deleted{B}A','Underlying stem and two rounded bowls are visible behind the stronger diagonal A.',0.89,'C_doubt_resolved;H_omission',['second_overwrites'],True,True)
add('D10','case 2, l’unique ... A de F',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Compressed e/l and ending t are visible; long medial sweep does not securely spell out ment.',0.66,'C_doubt_retained;abbreviation',['second','word_element_second'],False,True)
add('D11','case 2, deletion immediately before c’est',r'\deleted{\unsure{si $x\in A$}}',r'\struck{\ill{} $A$}',r'\deleted{\unsure{si $x\in A$}}','Initial s and dotted i, final A, and lower traces compatible with x∈ survive multiple parallel bars. Retain uncertainty in the intervening fragment.',0.70,'C_doubt_retained;H_partial_reading',['second_phrase'],False,True,True)
add('D12','b), cancelled verb under subdivise',r'\deleted{\unsure{raffine}}',r'\struck{raffine}',r'\deleted{raffine}','Two tall f strokes, initial r and terminal ne remain under the deletion and raised replacement; confirmed against live raffine just below.',0.91,'C_doubt_resolved',['b_start','seult_tout'],True,False)
add('D13','b), il faut voir ... que',r'\unsure{seult}','seulement','seult','s-e-u-like low movement, tall l and short terminal t. No separate ment sequence is visible.',0.86,'C_doubt_resolved;abbreviation',['b_start','seult_tout'],True,True)
add('D14','b), cancelled word after Donc que',r'\deleted{que \unsure{tout}}',r'\struck{que \ill{} que $A\subset B$}',r'\deleted{que \unsure{tout}}','A tall initial t and low linked strokes survive, ending in a worked-over stroke consistent with t. Retain tout as uncertain.',0.61,'C_doubt_retained;deletion_extent',['b_start','seult_tout'],False,True,True)
add('D15','cancelled draft, short word after comma on base line',r'\unsure{et} before l’ens',r'\ill{} before contienne',r'\unsure{est|et}, on the base line before contenu','Only one short e-(s?)-t group occurs after the comma; the upper l’ens belongs to the separate interlinear addition. Prefer est, keep et.',0.63,'C_doubt_revised;line_assignment',['draft_rot','draft_word_after_comma'],True,True,True)
add('D16','cancelled draft, base-line predicate',r'\unsure{est contenu dans}',r'\ill{} contienne',r'\unsure{est|et} \unsure{contenu dans}','The word after the short group begins open c, has a tall t-like stem and ends in a flattened u; a following d-loop and short joined strokes support dans. The single est/et is D15, not an additional word after the upper A⊂B.',0.67,'C_doubt_revised_segmentation;H_wording',['draft_middle','draft_rot'],True,True,True)
add('D17','cancelled draft, left slanted insertion',r'\inserted{\unsure{a un plus petit}}','un plus petit, without explicit insertion state',r'\inserted{a un plus petit}','Small initial a, un, long p/l of plus and legible petit; curved leader leads toward the abbreviated élément on next line.',0.91,'C_doubt_resolved;insertion_state',['draft_insertion_rot','draft_element'],True,True)
add('D18','cancelled draft, ... de F before C’est évident',r'\unsure{élémt|élément|élt}','él.',r'\unsure{élémt|élément|élt}','Opening e/l, accent-like stroke and long abbreviated ending survive, but strike line and insertion leader obscure the middle. No secure basis for H’s shorter él. alone.',0.59,'C_doubt_retained;abbreviation',['draft_element','draft_low_rot'],False,True)
add('D19','lowest abandoned line, first abbreviation',r'\unsure{str.}',r'\ill{}',r'\unsure{str.}','Tall sinuous initial and short joined strokes followed by a point remain under the long cancellation. Expansion is not supplied.',0.55,'C_doubt_retained;H_illegible_partial_reading',['draft_low_rot'],False,True,True)
add('D20','restated condition 1, overwritten letter in set-builder',r'\deleted{\unsure{B}}A','A',r'\deleted{B}A','An older vertical and rounded bowl project to the left of live A, consistent with B; thick newer A lies on top.',0.87,'C_doubt_resolved;H_omission',['set_overwrite'],True,True)
add('D21','restated condition 1, plus petit ...',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Tall l, accent/initial loop, elongated medial sweep and final short upturn; precise contraction remains ambiguous.',0.65,'C_doubt_retained;abbreviation',['restated','word_element_last_full'],False,True)
add('D22','condition 2, deleted saturation phrase',r'\unsure{$\mathcal R_{F\prime}$-satu.|$\mathscr R_{F\prime}$-satu.}',r'$R_{F\prime}$-\ill{}',r'\unsure{$\mathcal R_{F\prime}$-satu.|$\mathscr R_{F\prime}$-satu.}','Large looped R with low F′, then satu. remnants under heavy strike. Script-family choice not settled; plain H R loses the looped form.',0.68,'C_doubt_retained;H_partial_reading;alphabet',['footer','last_correction'],False,True,True)
add('D23','standalone support display below donc, comme','=','= plus terminal period',r'\unsure{\supseteq|=}','Small upper stroke curves down and back left over detached lower bar. This resembles superset-with-bar; a hooked upper equality stroke remains possible. Same shape recurs in b (D29).',0.66,'new_graphic_doubt;math_relation',['support_relation','relation_comparators','support_compare_b'],True,True)
add('D24','standalone display, punctuation after right support','none','period','none','Blank paper after final support bar; no separate punctuation dot.',0.94,'H_added_punctuation',['support_relation','top'],False,True)
add('D25','case 2, single word after c’est','le','lui','lui','Tall looped l followed by low u and final short i with an independent dot above. The final dot rules out a simple e ending.',0.97,'C_word_correction',['second_phrase','word_after_cest'],True,False)
add('D26','case 2, text immediately after lui','plus petit él. de F','(cf. définition de F\\G) qui [uncertain est] plus petit él. de F','plus petit él. de F','Next line starts plus petit él. de F; there is no cf., définition, or fronted qui est at this point.',0.96,'H_added_words;word_order',['second'],False,True,True)
add('D27','case 2, parenthesis after de F','(et à fortiori de F\\G)','omitted at this position; different parenthesis placed earlier','(et à fortiori de F\\G)','Opening parenthesis, et, accented à, tall f of fortiori, de, F\\G and closing parenthesis visible in order.',0.96,'H_omission;parenthesis;accent',['second'],False,True)
add('D28','case 2, final relative clause','qui contient x','contenant x','qui contient x','qui begins to the right of the closing parenthesis; next line carries contient then x and OK!. Ending is -ient, not -enant.',0.94,'H_wording',['second'],False,True)
add('D29','b), support relation after Comme','=','= ',r'\unsure{\supseteq|=}','Same small hooked upper component plus separate lower bar as D23; use same unresolved reading at both occurrences.',0.66,'new_graphic_doubt;math_relation',['support_compare_b','b_start'],True,True)
add('D30','b), before seult','no deletion',r'\struck{\ill{}}','no additional deleted word','The line before seult contains only the continuation from il faut voir; no independent cancelled word in the available gap.',0.89,'H_spurious_deletion',['b_start','seult_tout'],False,True,True)
add('D31','b), live que after cancelled que tout','live que','que grouped into deletion with A⊂B','live que; A⊂B belongs to the cancelled upper interline below','Deletion bar ends over the worked-over tout. Following que sits clear above the separately struck draft line; upper A⊂B is lower and belongs to l’ens sentence.',0.92,'H_deletion_extent;line_assignment',['b_start','seult_tout','draft_rot'],False,True,True)
add('D32','cancelled draft, symbol immediately before A∈F′',r'\deleted{Soit}','unreadable group in cancelled draft',r'\deleted{$\forall$}','Large open V-form with middle cross-stroke, overlaid by cancellation; no o-i-t sequence. Same form occurs in restated condition (D34).',0.95,'C_symbol_correction;H_illegible_resolved',['soit_first','draft_rot'],True,True,True)
add('D33','cancelled draft, upper interline l’ens ... A⊂B','l’ens F^A des B∈F tels que A⊂B as unmarked text in cancelled paragraph','l’ens. F^A ... A⊂B, A∈F′ ...','interlinear insertion l’ens F^A des B∈F tels que A⊂B, under the overall cancellation','This complete clause is on a separate higher sloping line. No full stop after ens and no extra A∈F′ after its final B; A∈F′ is on base line at left.',0.93,'insertion_state;H_punctuation;spatial_order',['draft_rot','draft_middle'],True,True)
add('D34','restated condition 1, struck opening symbol',r'\deleted{Soit}',r'\struck{$\forall$}',r'\deleted{$\forall$}','Same large V-shaped universal sign and horizontal crossbar as the draft occurrence. Not four cursive letters.',0.97,'C_symbol_correction',['soit_second'],True,False)
add('D35','restated condition 1, abbreviation l’ens','l’ens','l’ens.','l’ens','Final s sweep ends without a separate dot before F^A.',0.89,'H_added_punctuation',['restated','word_element_last_full'],False,True)
add('D36','cancelled lower line, repetition after str.','de de F′ raffine F. Si','F′ raffine F. Si (preceded by ill.)','de de F′ raffine F. Si','Two distinct short de-like groups precede F′ under the long strike; repetition retained. Both F′ and following F are legible.',0.83,'H_omission;authorial_repetition',['draft_low_rot'],False,True,True)
add('D37','cancelled draft, label and base-line order','1°) before Soit A∈F′','1) appears in a later struck chunk before un plus petit','1°) before cancelled ∀ and A∈F′; base-line predicate and next line follow','1 with high small circle and closing parenthesis lies at left of base line, not beside the later slanted insertion.',0.94,'H_label_position;spatial_order',['draft_rot','draft_insertion_rot'],False,True,True)

Crows=[]
statuses={1:'resolved',2:'retained',3:'retained',4:'retained',5:'retained',6:'resolved and extended',7:'retained, preferred candidate changed',8:'retained',9:'resolved',10:'retained',11:'retained',12:'resolved',13:'resolved',14:'retained',15:'revised and retained',16:'resegmented and retained',17:'resolved',18:'retained',19:'retained',20:'resolved',21:'retained',22:'retained'}
for i in range(1,23):
 row=D[i-1]
 Crows.append({'occurrence':i,'source_locus':row['place'],'source_C':row['C'],'status':statuses[i],'difference_id':row['id'],'reading':row['reading'],'confidence':row['confidence']})
I=[]
def inv(id,place,content,state,crops):I.append(dict(id=id,place=place,content=content,state=state,crops=crops))
inv('I01','top right','manuscript number 30','page marker',['whole'])
inv('I02','top line','a) F′ est une figure. Notons que','live body',['top'])
inv('I03','top line','i.e.','deleted',['top'])
inv('I04','end of top line','|F′|=','deleted setup',['top'])
inv('I05','opening display','|F′|=|G′|∪|F\\G|, then cancelled operator and ⊃|F|','display',['top','top_deleted','relation_comparators'])
inv('I06','beneath opening display','underbrace |G′| labelled |G|','underbrace annotation',['top'])
inv('I07','beneath opening display','underbrace |F\\G| labelled ⊃ |F|\\|G|','underbrace annotation',['top'])
inv('I08','connector','donc, comme |F′|⊂|F|, on a','live body',['top'])
inv('I09','standalone display','|F′| [supseteq|=] |F|','display, unresolved relation',['support_relation'])
inv('I10','upper paragraph','Il faut prouver que ∀x∈|F′|=|F|, ∃ plus petit [élémt|élément|élt] de F′ qui le contienne. Distinguons deux cas','live body',['argument'])
inv('I11','case 1 first line','1°) x∈|G|=|G′|, soit A∈G′ ... tel que x∈A circle(G′)','live body with tiny cancelled blot and overworked closing high curve',['first','first_symbols'])
inv('I12','case 1 next clause','Si B∈F′ et [B∋ deleted] x∈B, prouvons A⊂B','body and cancelled fragment',['first_cancel_context','first'])
inv('I13','case 1 branch clauses','Si B∈G′, c’est évident. Si B∈F\\G, alors','live body',['first'])
inv('I14','case 1 replacement','B contient','deleted',['first'])
inv('I15','case 1 conclusion','A circle(G′) ∩B≠∅ donc A[raised circle/bullet]⊂B OK','live formula and ending',['first','first_final_mark'])
inv('I16','case 2 start','2°) x∈|F|\\|G|, old G under F; alors les A∈F′, old B under A','body with overwrites',['second','second_overwrites'])
inv('I17','case 2 first assertion','qui contiennent x ne sont pas dans G′, ils sont donc dans F\\G','live body',['second'])
inv('I18','case 2 unique element','D’autre part, l’unique [élémt|élément|élt] A de F tel que x∈A circle(F) n’est pas dans G puisque x∉|G|, il est donc dans F\\G','live body',['second','word_element_second'])
inv('I19','case 2 near c’est','et [si x∈A deleted, uncertain], c’est lui','body plus cancelled fragment',['second_phrase','word_after_cest'])
inv('I20','case 2 end','plus petit él. de F (et à fortiori de F\\G) qui contient x, OK!','live body; grammatical omission not repaired',['second'])
inv('I21','b heading','F′ [raffine deleted] [subdivise inserted] F','revision',['b_start'])
inv('I22','b opening claim','Comme |F′| [supseteq|=] |F|, il faut voir seult que F′ raffine F','live body, unresolved relation',['b_start','support_compare_b','seult_tout'])
inv('I23','b transition','Donc [que tout deleted] que','revision',['seult_tout'])
inv('I24','cancelled draft base line','1°) [∀ deleted] A∈F′, [est|et] [contenu dans] un plus petit','overall cancellation with local deletion',['draft_rot','soit_first','draft_word_after_comma'])
inv('I25','cancelled draft upper line','l’ens F^A des B∈F tels que A⊂B','interlinear insertion, then overall cancellation',['draft_rot','draft_middle'])
inv('I26','cancelled draft left slanted addition','a un plus petit, curved leader toward following élément abbreviation','insertion inside overall cancellation',['draft_insertion_rot'])
inv('I27','cancelled draft next line','[élémt|élément|élt] de F. C’est évident si A∈F c’est évident. Si','overall cancellation; repeated clause preserved',['draft_rot','draft_element','draft_low_rot'])
inv('I28','cancelled draft lowest line','[str.] de de F′ raffine F. Si','overall cancellation, repeated de retained',['draft_low_rot'])
inv('I29','cancelled draft marks','long horizontal crossing lines, large right enclosure and curved insertion leader','cancellation/placement marks, not an independent mathematical drawing',['cancelled','draft_rot','draft_low_rot'])
inv('I30','restated condition 1','1°) [∀ deleted] A∈F′, l’ens F^A={B∈F | [B overwritten]A⊂B} a un plus petit [élémt|élément|élt]','live condition with corrections',['restated','soit_second','set_overwrite','word_element_last_full'])
inv('I31','restated condition 1 middle','C’est évident si A∈F [(B=A) deleted] (on prend B=A)','live body and deletion',['restated'])
inv('I32','restated condition 1 ending','et si A∈G′, c’est vrai puisque G′≪F','live body',['restated'])
inv('I33','condition 2 opening','2°) Si A∈F′, B∈F, alors A∩B est','live body',['footer'])
inv('I34','condition 2 correction','[script R_F′-satu. deleted] [fermé dans F′ inserted]','deletion and raised insertion',['footer','last_correction'])
inv('I35','condition 2 conclusion','i.e. réunion de strates de F′. Si A∈G′, comme G′≪F, A∩B est réunion de strates de G′, qui sont aussi des strates de F′.','live body to bottom edge',['footer'])

recipes=json.loads((base/'crops031.json').read_text())
for c in recipes:
 c['source']=str((root/c['source']).resolve())
 c['path']=str((root/c['path']).resolve())
 c['rotation_degrees']=c.get('rotation_degrees',c.get('rotation',0))
 c['id']=Path(c['path']).stem.replace('scan031_','')
 c['viewed']=True
images=[{'source':str(root/f'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan031{s}.jpg'),'role':r,'order':i} for i,(s,r) in enumerate([('','whole'),('_a','upper half'),('_b','lower half')],1)]
tex=(base/'scan031.tex').read_text()
# This checks TeX delimiters, not rendering and not mathematical validity.
clean='\n'.join(x.split('%',1)[0] for x in tex.splitlines())
balance=0;minbal=0
for i,ch in enumerate(clean):
 if ch in '{}':
  # braces escaped by an odd backslash run are literal delimiters.
  n=0;j=i-1
  while j>=0 and clean[j]=='\\':n+=1;j-=1
  if n%2:continue
  balance+=1 if ch=='{' else -1;minbal=min(minbal,balance)
assert balance==0 and minbal==0,(balance,minbal)
assert clean.count('\\[')==clean.count('\\]')==2
assert clean.count('$')%2==0
assert len(Crows)==22
assert len({x['id'] for x in D})==len(D)
for c in recipes: assert Path(c['path']).exists()
report={
 'scan':'031','manuscript_page':'30','reader':'R2','effort':'inherited',
 'start_utc':(base/'start031.txt').read_text().strip(),'end_utc':datetime.now(timezone.utc).isoformat(),
 'sources':{'C':str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan031.tex'),'H':str(root/'working/H/scan031.tex'),'C_doubts':str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_doubts.md'),'C_notes':str(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_notes.md')},
 'independence':{'other_reader_files_read':False,'root_decisions_read':False,'later_scans_read':False,'OCR_used':False,'external_research_used':False},
 'images_viewed':images,'crops':recipes,
 'viewing_note':'Whole, then upper and lower halves, then enlarged crops. A tool response that truncated a three-image batch was not counted as viewing; the affected targeted crops were subsequently emitted and examined separately. All recipes listed were ultimately viewed.',
 'differences':D,'C_doubt_resolutions':Crows,
 'S_row_decisions':{'relevant_rows':[],'decision':'No sweep3 correction row for scan031; source table checked for this scan.'},
 'inventory':I,
 'remaining_doubts':[dict(difference_id=x['id'],place=x['place'],reading=x['reading']) for x in D if ('retained' in x['kind'] or 'new_graphic_doubt' in x['kind'] or x['id'] in ['D07','D15','D16'])],
 'notation':[
  'Plain F, G, A, B and x retained; initial F resolved against script alternative.',
  'Support bars retained, and F\\G kept distinct from |F|\\|G|. The opening display has two separate underbraces and right-facing inclusion beneath the second.',
  'A circle(G′) and A circle(F) are elevated open circles followed by same-level parenthesized figure labels; primes reviewed in their own locations.',
  'The nearly filled final raised mark on A is retained as circle/bullet uncertainty, without the asterisk selected by H.',
  'The relation below donc and its matching occurrence after Comme in b are both recorded as supseteq|=, because their identical hooked upper strokes and detached lower bars remain graphically ambiguous.',
  'F^A has upper-case superscript A; the set-builder inequality is A⊂B, with overwritten B before A preserved.',
  'Both G′≪F relations have two distinct wedge components and a prime on G.',
  'Two crossed opening glyphs are ∀, not the word Soit.',
  'No independent diagram or mathematical drawing on this page. Underbraces preserved as TeX; cancellation rules and leader are accounted for as revision marks.'
 ],
 'reading_notes':[
  'Every body line was read visually against the page, including agreements, not merely a text diff.',
  'Three focused requests were independently examined: B∋ extent, lui after c’est, standalone support relation. Crop recipes are included.',
  'The page reads c’est lui plus petit ...; no missing article or copula is supplied to repair the grammar.',
  'The cancelled draft is spatially layered. Its upper l’ens clause and left a un plus petit addition are recorded as insertions inside the overall cancellation. The single est/et after the base-line comma is not duplicated as both C’s et and a later est.',
  'C’s visible à fortiori accent and repeated de de are retained. The two C wording notes for this page were reviewed.',
  'No claim is made to settle the semantic role of the worked-over circle after G′. Its ink existence is secure, but the exact original mark/deletion interpretation remains low confidence.'
 ],
 'checks_performed':[
  {'type':'visual_reading','scope':'Whole page then both halves; every line and physical revision.','result':'Completed; no OCR.'},
  {'type':'comparative_palaeographic_review','scope':'34 enlarged/rotated crops, including all 22 C doubts and all differing H loci.','result':'Completed; exact recipes retained.'},
  {'type':'local_mathematical_inference','scope':'The pair of inclusions stated immediately around the opening display.','result':'If both |F′|⊇|F| and |F′|⊆|F| hold, equality follows by mutual containment. This logical observation does not decide the handwritten glyph, so the graphic uncertainty remains.'},
  {'type':'scope_limitation','scope':'Full proof check of the two-case argument and subdivision argument.','result':'Not performed. The manuscript invokes figure/refinement facts whose proof was not re-established in this reading.'},
  {'type':'syntax_validation','scope':'Own complete page LaTeX.','result':{'balanced_group_braces':True,'two_paired_display_delimiters':True,'even_dollar_delimiter_count':True,'C_doubt_occurrences_accounted_for':22,'all_crop_paths_exist':True,'compiled':False}}
 ],
 'flag_semantics':'against_C/against_H compare submitted text, uncertainty candidate order/set, and physical deletion/insertion state. Equivalent macro names, spacing, itemize formatting and setminus/smallsetminus do not count. marked_in_H is local explicit uncertainty/illegibility or the explicit asterisk/circle note, not merely struck text.',
 'summary':{'differences_and_review_rows':len(D),'C_doubt_occurrences':22,'resolved_C_doubts':7,'remaining_C_doubts':15,'inventory_entries':len(I),'crop_recipes':len(recipes),'full_tex':str(base/'scan031.tex')}
}
(base/'scan031.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False))
