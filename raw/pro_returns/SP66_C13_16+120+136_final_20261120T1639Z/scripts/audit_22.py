from audit import *
k='120_scan024'
replace_text(k,[('Si on a M1 : M7 et M11',r'Si on a M1 : M\unsure{4|7} et M11')])
add_changes(k,[R('endpoint of axiom range in proposition','M7','M7',r'M\unsure{4|7}','The crowded digit has a long rising diagonal returning to a horizontal crossbar, supporting 4; a heavy upper cap and curved descending stem also support an overwritten 7. The stroke order cannot be securely recovered.','misread symbol or index','yes','yes',conf='low',crop='120_scan024 (1132,1732,1264,1827)',con='The axiom range endpoint is now qualified as M4/M7; neither witness’s unqualified M7 is secure on the overlapping strokes.')])
add_doubts(k,[('endpoint of axiom range',r'M\unsure{4|7}','overlapping 4-like and 7-like strokes; order of rewriting uncertain','low')])
p=ROOT/(PREFIX+'_notes.md');s=p.read_text();s=s.replace('The text writes M1 : M7, and the double-stem short form tt before partie is retained without grammatical expansion.','The endpoint of the axiom range is overwritten: the second audit favours M4 from its oblique left arm and crossbar, with M7 retained as an alternative. The product-separation step, once the families are given, does not use the extension axiom M7; this prompted reinspection but does not settle the composite ink. The double-stem short form tt before partie is retained without grammatical expansion.');p.write_text(s)
fs=['statement_id','date','who','type','outcome']
# Match the existing check-event schema rather than assuming its field labels.
events=readtsv('CHECK_EVENTS.tsv')
row=dict(events[-1]);row['statement_id']='120-024-product-separation'
for field in row:
 if field=='date':row[field]=now()
 if field=='type':row[field]='used and rechecked in this run'
 if field=='outcome':row[field]='Given the finite families f_alpha and g_beta, the product-separation step itself uses the field operations and the nonzero common scalar, not M7. This motivated inspection of the overwritten axiom endpoint without deciding its ink.'
append('CHECK_EVENTS.tsv',list(events[0]),[row])
finish(k,'Reread all struck and live lines, the displayed brace and the final proposition. A new crop of the crowded axiom endpoint reveals overlapping 4-like and 7-like strokes; the formerly unqualified M7 is now M4/M7 with low confidence. The lambda annotation stays beneath g_beta(x), and the stated separation of all points of X remains as written despite the mathematical qualification in the notes. Confirmed the final opening parenthesis and the short form tt.')
