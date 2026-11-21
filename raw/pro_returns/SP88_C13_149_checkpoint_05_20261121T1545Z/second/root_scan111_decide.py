import json
from root_decision_support import write_decisions, ROOT
scan=111
comp=json.loads((ROOT/'second/149_scan111_comparison.json').read_text());first={x['box']:x['first'] for x in comp}
evidence={
'b01':"The rotated margin begins with a long S and the open ou run of Sous, without the D loop of Dans or the closed a of Sans. The separate oblique runs read suite exacte, d'homo-, topie, mais avec fibres and pas néc.; their irregular spatial order explains the interrupted second reading. The compressed connexes/conn. ending stays doubtful. On and X to Y are overlapping main text, already transcribed there.",
'b02':"The long word has f-a-c-t-o-r-i-s-a-t-i-o-n, including its internal dotted i and tall t; it is appreciably longer than fibration. The short terminal can has a separate point. Retain the first wording and initial on.",
'b04':"The word after est has the low ma, dotted i, tall t and final t of maintenant; it has no initial d ascender required by évidemment. The two open E lobes, prime on the source E and prime on target Y are visible.",
'b05':"The cancelled opening supports donc, but the crossing still obscures its middle letters, so its doubt remains. The live abbreviation has low u-n-i-v and a detached point; it lacks the two tall l strokes needed for usuelle. Retain univ.",
'b06':"The explicit accent over sûr, stop after it, On aura, looped d of des, short iso and ca-n run are visible. The final two words are not ce cas and no abbreviation stops are added.",
'b07':"Both group letters have two right-open lobes rather than the closed outer curve of G. The right superscript is T; the pale angular trace above the right end of its bar is much lighter than the foreground formula and does not establish an additional A/a exponent. Both X/Y indices and the target prime remain, as does the single arrow with a wave above it.",
'b09':"Both E forms have open upper and lower lobes. The left index is the complete product over Y-prime and the right index is X/Y; the relation has a wave over one bar. Retain the first formula.",
'b10':"The isolated group letter clearly repeats the two-open-lobe E of the displays, with T above and X_T below. The surrounding words and comma agree; the new E/G doubt is unnecessary here.",
'b12':"The word after non has a tall looped l between p and the low u-s ending, hence plus rather than pas. The inserted Y-prime arrow and its curved leader are distinct. The product after mais has the literal unprimed Y, which remains despite the earlier definition.",
'b13':"There is no accent stroke over sur, unlike the explicit circumflex in b06. After près, the upper-baseline oval and low n read on; the crossing below belongs to the tall letter in the following line. The last word ends in the short returned t form, not a separate x. Retain on peut and both abbreviation stops.",
'b14':"The cancelled word begins with a clear e loop, but the heavy crossing and tall terminal remnant admit en or et; add et without resolving the cancellation. An initial d for de is not supported. The E has open lobes; its X_T index is heavily retraced, but no independent cancellation stroke can be separated from the T crossbar and overtracing. Keep the live T rather than inventing a deleted underlying Y-prime.",
'b15':"The words after pour have a low ce, q descender, dotted i, short est and looped d-u: ce qui est du. No un point sequence is written. The tilde Y has the same capital construction as the other cover symbols; the last word is the shorter par, with a joined a rather than an ou run.",
'b16':"After l and the apostrophe the extended low an-c-r-a run precedes the descending g and final e: ancrage. It is longer than image and has no dotted initial i. The following word has a looped d plus low ans, so dans, not de. The smaller Y under X is the recurring capital cover symbol, with its wave and terminal comma.",
'b17':"The dark authorial number is 55: both digits have a top bar and returned lower curve. The second reading adds only its page-number wrapper; the page already uses mspage.",
'b18':"The thin lower-left number has two rising-entry 1 strokes and a closed 0. The second reading's margin wrapper only describes placement already encoded in the page."
}
new=first['b14'].replace(r'\unsure{en}',r'\unsure{en|et}')
write_decisions(scan,evidence,medium=('b01','b05','b07','b13','b14'),final_readings={'b14':new})
plan={'scan':scan,'page_replacements':[{'old':r'\unsure{en}','new':r'\unsure{en|et}','expected_count':1}],
'changes_updates':[{'id':'p14','patch':{'final':new,'evidence':evidence['b14']}}],
'doubts_updates':[{'place':'cancelled word at the start of main line 16','patch':{'alternatives':'et; cancelled terminal strokes not securely separable'}}],
'inventory_updates':[{'element':'e13','patch':{'first_words_or_objects':'uncertain en/et'}}],
'notes_append':['Independent audit: fifteen token-different boxes were adjudicated. The cancelled en/et remains uncertain; the additional alternative changes certainty, not the preferred witness-error reading. Formula (15) has no secure added A/a exponent above T. The retraced X_T in the last paragraph has no separately legible erased underletter.']}
(ROOT/'second/149_scan111_update_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
