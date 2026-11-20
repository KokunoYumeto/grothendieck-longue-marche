from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan003.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=12
r['root_review']={'whole_image':True,'crops_viewed':'All twelve saved first-reading crops; the saved last-display, closing-prose, and oblique-note crops were consulted again to adjudicate the reader return, without making further crops.','decisions':'Accepted recoverable letters and retained every opaque struck layer. The word before (2)_2 is marked uncertain against punctuation; the beta/gamma comparison remains doubtful despite the expected abelianized equality.'}
s=(E/'reader_reports/145_scan003.tex').read_text().replace(r'correspondante à $(2)_2$',r'correspondante \unsure{à|:} $(2)_2$')
for c in r['changes']:
 if c['id']=='s003-19':
  c['final']=r'correspondante \unsure{à|:} $(2)_2$';c['confidence']='low';c['ink']='A short oblique upper mark and a compact lower dark body stand before the parenthesized reference. The body may be a compressed a under an accent, but the pair can also be punctuation. The main reader therefore preserves à versus colon as an explicit uncertainty rather than supplying a certain new word.'
for b in r['second_boxes']:b['reading']=b['reading'].replace(r'correspondante à $(2)_2$',r'correspondante \unsure{à|:} $(2)_2$')
r['doubts'].append({'place':'closing prose before (2)_2','reading':r'\unsure{à|:}','alternatives':['à',':'],'confidence':'low','reason':'The lower body is compact rather than a fully separable a-loop; upper and lower marks also permit punctuation.'})
r['notes'][2]=r['notes'][2].replace('No targeted proof check, independent re-proof, or formal computation was completed.','The main reader performed the two local algebraic checks described below; the difficult final representative-change formula was not thereby resolved.')
r['notes'][3]=r['notes'][3].replace('Root must adjudicate this along with the small exponent before β, the opening overwritten word, and the touching parentheses in the last display.','The main reader retained uncertainty in this superscript and the overwritten terms; the touching parentheses are retained at medium confidence. Before (2)_2, à versus colon remains expressly doubtful.')
r['notes'] += [
'Local algebra check of the rewrite: put A = h₁ l₁^(−γ) ρ⁻¹(h₁). Equation (2) has ρ(h₁) l∞^(−γ) A = l₀^β; multiplying on the left by l∞^γ ρ(h₁)⁻¹ gives A = l∞^γ ρ(h₁)⁻¹ l₀^β, in that order. In int(A)(l₀^p), the terminal l₀^β commutes with l₀^p and therefore disappears from the conjugation. This verifies the displayed passage to (1′) locally. It does not identify the overwritten exponent or prove any surrounding characterization of automorphisms.',
'Local abelianization check of the margin: write e₀+e₁+e∞=0, with ρ cycling these three classes. The operator 1+ρ+ρ² is zero on this rank-two module. Abelianizing (2) gives −γ(e∞+e₁)=βe₀, hence γe₀=βe₀ and β=γ. Thus the expected statement is equality. The oblique comparison strokes themselves are still recorded as = versus ≠; the calculation is not used to erase that paleographical doubt.'
]
r['check_events']=[
{'statement_id':'145-003-rewrite-2-to-1prime','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'Verified the noncommutative rearrangement of (2) and cancellation of conjugation by the terminal l₀^β on l₀^p. No claim about the final heavily corrected display.'},
{'statement_id':'145-003-margin-abelianization','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'In the free rank-two completed abelianization with e₀+e₁+e∞=0 and cyclic ρ, the norm 1+ρ+ρ² vanishes; (2) implies β=γ. The uncertain written comparison sign remains unchanged.'}]
(E/'reader_reports/145_scan003_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan003.tex').write_text(s)
