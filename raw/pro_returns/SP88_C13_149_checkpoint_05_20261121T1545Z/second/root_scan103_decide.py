from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];s=r/'second';comp=json.loads((s/'149_scan103_comparison.json').read_text());data=json.loads((r/'review/accepted/149_scan103.json').read_text());boxes={x['box']:x for x in data['audit_boxes']}
evidence={
'b01':'The first two relations have two shafts and explicit right-pointing curves. Between c) and d) the two shafts close in a small rounded return without a clearly projecting head; retain the equals/implication uncertainty. Long versus short TeX arrows elsewhere add no content.',
'b02':'Two parallel shafts end in a distinct right-pointing curve between d and a. Both readings denote this implication; only arrow length differs.',
'b03':'After the low n-n-u strokes of connu there is a separate comma, without an additional e loop. The final small vowel body lies below a detached accent and is read à in the continuation, not a semicolon. Retain ou du moins se prouver.',
'b05':'The long word has the descending p and subsequent accented e and h ascender of compréhension. It does not have the l-t sequence of compilation. After the parenthesis the tall looped f, u, t, hyphen and two l ascenders support fut-elle; no circumflex is visible.',
'b06':'The complete oblique margin was inspected in its rotated audit crop. The third line begins une version de ceci: initial v, dotted i and low on are visible, without the word groups needed for en premier le cas. The subscript is the repeated eta form. The bar spans X_eta-U_eta and belongs to that expression, rather than underlining mais; the expression continues multisection on its baseline. The final compressed à has an accent and vowel body, rather than two punctuation dots. Retain the first complete margin reading.',
'b07':'Before vient the low c-o-n run is present, giving convient. The raised word begins a barred capital I followed by the small n-d-i-v sequence and the later d-u-e-l-l-es, supporting Individuelles rather than naturelles.',
'b08':'The baseline begins e-x-t, with a crossed x and tall t, and continues érieures. It does not begin d-é-f. The long curve is the leader attaching the raised Individuelles after extérieures, not a strike or extra text.',
'b09':'The mathematical letter has a tall stem with a short angled branch rather than a full h arch, supporting k in the local field notation. The cancelled word has an e loop, crossed x, tall t and a terminal point: ext., not est.',
'b10':'The first groups read sur des. The short mathematical sign has the curved right foot of pi. The next detached accent sits above the small a body, and bouts has the tall open b, low ou run, crossed t and terminal s. It is one word, not two mathematical letters.',
'b11':'The raised parenthesized phrase reads sans doute; the small marks after doute do not securely separate an ellipsis from the terminal return, so the first uncertainty remains. Below it the two groups read ne soient, with a dotted i and final t, not un sens.',
'b12':'The cancelled d loop and a low e body remain visible. The dark final descending hook could be the surviving s or part of the cancellation; every letter is not plain. Retain des as preferred but add de as an explicit alternative inside the deletion.',
'b13':'The second type parameter has a low descending then rising curved stroke, without the arch and terminal fall of n; retain nu. The comma after g is separately visible.',
'b14':'The negative n and raised apostrophe precede a, then the short repeated r strokes, dotted i and v-e. The sequence supports n\'arrive, not m\'avise. The quotation marks and stop after mal agree.',
'b15':'The dark top number is 51. The second reading adds only the manuscript-page wrapper already used in the page text.',
'b16':'The thin bottom foliation is 102, with a closed oval and angular final 2. It remains a margin number; wrapper syntax changes no reading.',
'b18':'The word starts with the tall h structure partly overlapped by marginal writing, then the low eur run and stique with a long q descender. The longer initial character sequence needed for caractéristiques is absent. Retain heuristique.',
'b19':'The preceding full insertion is visible in b11; this wider crop confirms the baseline ne soient géométriques, with dotted i and terminal t in soient and a separate final s return in géométriques. No additional pas is present.'
}
rows=[]
for c in comp:
 if not c['different']:continue
 b=c['box'];final=c['first'];changed=b=='b12'
 if changed:final=final.replace(r'\deleted{des}',r'\deleted{\unsure{des|de}}')
 rows.append({'box':b,'root_visually_inspected':True,'final':final,'evidence':evidence[b],'crop':f'crops/149_scan103_second_{b}'+('_rotminus35' if b=='b06' else '')+'.png','bbox':boxes[b]['bbox'],'confidence':'medium' if b in ['b01','b03','b06','b11','b12','b19'] else 'high','changed':changed})
(s/'149_scan103_adjudications.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
plan={'scan':103,'page_replacements':[{'old':r'\deleted{des}','new':r'\deleted{\unsure{des|de}}'}],'doubts_append':[{'place':'main line 17, cancelled word between par and la','reading':r'\deleted{\unsure{des|de}}','alternatives':'des; de. The cancellation obscures whether the final hook is a letter s.','confidence':'low'}],'inventory_updates':[{'element':'e08','patch':{'first_words_or_objects':'doubtful des/de'}}],'notes_append':['Independent audit: seventeen boxes with token differences were visually adjudicated. The preferred text remains unchanged. Uncertainty was added to the cancelled des/de because its final hook is not separable from the crossing-out; this is not counted as an additional witness error.']}
(s/'149_scan103_update_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
