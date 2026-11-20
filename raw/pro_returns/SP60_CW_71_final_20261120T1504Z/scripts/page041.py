from record import *
t=(ROOT.parent/'source/SP60_CW_71_witnesses/codex/J71-05/pages/J71-05_71_scan041.tex').read_text(encoding='utf-8').replace(r'\unsure{de|d}','de')
(ROOT/'pages/J71-05_71_scan041.tex').write_text(t,encoding='utf-8')
doubt(41,'unfinished last word','de','d','high','resolved','After the d, a distinct short rounded e-turn is visible in the 180-degree-rotated supplied bottom half. The sentence is unfinished but the word de is present; no crop needed.')
notation('Reversed sheet orientation','Two lines are upside down relative to archive number 40; rotate 180° to read.','41','Inclusion is genuinely ⊃ with Λ² left and Λ¹ right.')
inv(41,[('text','bottom in supplied orientation; top when rotated','Demonstration : pour voir que intΛ²⊃intΛ¹ il suffit de prouver que tout point de')])
note(41,"""**Content and physical state.** A short abandoned beginning of a proof occupies two lines, upside down relative to archive number 40. The rest is blank apart from faint reversed show-through. There is no manuscript number, title, date, or cancellation. Both supplied halves were viewed after rotation through 180° without resizing.

**041-N1 — relation checked for transcription.** It reads `int Λ²⊃int Λ¹`, opposite to the inclusion on scan 40. The curved right side and open left side decide ⊃; the exponents are 2 then 1. This unfinished version is preserved, with no attempt to complete its argument or join it to scan 42. The last word is legible as “de”; C’s de/d uncertainty is resolved. No authorial question mark or reservation is written.""")
event('041-N1','used and rechecked in this run','Only direction and endpoint order were compared to scan 40: the fragment has the opposite inclusion. No proof of this unfinished assertion was attempted.')
done(41)
