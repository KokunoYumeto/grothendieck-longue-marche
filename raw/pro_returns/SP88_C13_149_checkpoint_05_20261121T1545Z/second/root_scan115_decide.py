import json
from root_decision_support import write_decisions, ROOT
comp=json.loads((ROOT/'second/149_scan115_comparison.json').read_text());first={x['box']:x['first'] for x in comp}
evidence={
'b01':'The dark top number has the open 5 and crossed descending 7 of 57. The second reading adds only the page-number wrapper already used in the page.',
'b02':'Both horizontal bars over K are visible. Bar/overline and the placement of math delimiters inside the deletion are encoding differences. The cancelled E_Y remains doubtful beneath its hatching; neither reading resolves an additional underletter.',
'b03':'Spec K has a curved horizontal bar above K, a wave-over-bar isomorphism sign, and a separate wave above the capital Y. The two readings agree on all source marks; bar/overline and tilde/widetilde account for the remaining tokens.',
'b04':'The lower abbreviation begins with the small detached a-like lead and low u stroke of au, not a connected e-n run. Retain au lieu de. The insertion leader carries ou Gamma_K and the further barred-K superscript notation to the position after Gamma; superscript/subscript ordering in TeX and comma delimiters do not alter that reading.',
'b08':'The raised two-stroke word lies above the end of Soit, before the large K; its curved cue descends into that gap. It does not attach after K at the cancelled tel. Retain its uncertain un before K and keep the cancelled tel doubtful.',
'b09':'The canonical crop touches the top of the tall l, so a wider upper context was inspected specifically for the open accent question. There is no separate accent stroke over the e of the quoted modele. The later modèle in b10 has an unmistakable detached accent after its d ascender, providing a same-page contrast. Change this first occurrence to unaccented modele; retain its paired high quotation strokes.',
'b10':'The cancelled p-like stem and upper loop remain crossed by extra ink and the underline, so their doubt is not removed. The two physical underline segments continue the same phrase over the line break. The later modèle has its visible accent; it remains accented. No final s is present on modèle or choisi.',
'b11':'The thin foliation reads 114; the two 1 strokes precede the angular 4 with a cross-stroke. The second reading supplies only the margin wrapper already encoded.'}
new=first['b09'].replace('modèle','modele')
write_decisions(115,evidence,medium=('b02','b04','b08','b10'),final_readings={'b09':new},extra={'b09':{'additional_evidence':[{'crop':'crops/149_scan115_audit_b09_accent.png','bbox':[1250,1480,1660,1750]}]}})
plan={'scan':115,'page_replacements':[{'old':"``modèle''",'new':"``modele''",'expected_count':1}],
'changes_updates':[{'id':'p09','patch':{'place':'Main line 12, quoted modele: missing accent and quotation shape','final':"``modele''",'evidence':evidence['b09'],'crop':'crops/149_scan115_audit_b09_accent.png','bbox':[1250,1480,1660,1750],'vs_C':True,'kind':'abbreviation expanded or spelling modernised','error_category':'Abbreviations expanded, spelling modernised'}}],
'notes_append':['Independent audit: the first quoted modele is unaccented; the wider context shows no omitted accent above it, while the later underlined modèle on the same page is accented. Both witnesses supplied the accent to the first occurrence. The short-form spelling is kept occurrence by occurrence.'],
'hand_observations_append':[{'habit':'Accent varies within the same leaf: quoted modele but later underlined modèle.','pages':[115],'holds':'Only the first occurrence lacks an accent; no blanket rule is imposed.','witness_errors':'Both C and H supplied an accent in the first quoted modele.'}]}
(ROOT/'second/149_scan115_update_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
