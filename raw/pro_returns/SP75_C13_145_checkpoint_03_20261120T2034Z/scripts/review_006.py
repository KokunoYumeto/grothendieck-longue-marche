from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan006.json').read_text())
r['main_reader_reviewed']=True;r['crop_count']=18
r['root_review']={'whole_image':True,'crops_viewed':'All eighteen distinct first-reading crops were directly inspected. The third-calculation crop was consulted again to adjudicate the proposed removal of a struck-text doubt.','decisions':'Accepted du moins, écrira, barred m, quotation strokes, insertion positions, absence of terminal sentence dot, and legible cancelled sigmas. Preserved doubtful glyphs and restored the uncertainty on the struck l1 because its small index remains entangled with the cancellation.'}
r['unlisted_decisions']=[d for d in r['decisions'] if d['id'].startswith('U')]
r['decisions']=[d for d in r['decisions'] if d['id'].startswith('M')]
for d in r['unlisted_decisions']:
 if d['id']=='U006-03':d.update(decision='undecided',reading=r'\deleted{\unsure{l_1}}',confidence='low',ink='The tall l loop survives, but diagonal cancellation and retracing entangle the small lower index. Main reader retains the original struck-text doubt because every component is not plain.')
s=(E/'reader_reports/145_scan006.tex').read_text().replace(r'\deleted{l_1}',r'\deleted{\unsure{l_1}}')
for b in r['second_boxes']:b['reading']=b['reading'].replace(r'\deleted{l_1}',r'\deleted{\unsure{l_1}}')
r['doubts'].append({'place':'cancelled terminal factor in the third calculation','reading':r'\deleted{\unsure{l_1}}','alternatives':['l_1','overwritten lower index'],'confidence':'low','reason':'The cancellation tangles the lower index; the root reader does not resolve C’s struck uncertainty.'})
r['notes'][4]=r['notes'][4].replace('or mathematical proof check was used.','was used by the first reader. The main reader subsequently performed the local word computation described below.')
r['notes'][5]=r['notes'][5].replace('C’s uncertainty on struck l_1 is resolved from its complete calculation crop.','C’s uncertainty on struck l_1 remains after main-reader adjudication: its small index is entangled with the strike.')
r['notes'].append('The main reader checked the three live inner-conjugation identities by free-word reduction. With a=l₀, b=l₁ and l∞=(ab)⁻¹, the generator images written on scans 005–006 give σ₀σ₁=int(b⁻¹)ρ, σ₁σ∞=int(l∞⁻¹)ρ, and σ∞σ₀=int(a⁻¹)ρ on both free generators. The calculation and exact reduced words are saved in scripts/check_006_words.py and reader_reports/145_scan006_word_check.json. This verifies those local identities only; it is not a proof of the claim about realizing the exterior action or a warrant to normalize the uncertain fixed-point expression.')
r['check_events']=[{'statement_id':'145-006-three-inner-conjugation-identities','type':'computation or formal certificate','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'Executed free-word substitution and adjacent inverse cancellation on l₀,l₁ for all three displayed cyclic identities. Left and right images agree in each case. Script and reduced-word output are included.'}]
(E/'reader_reports/145_scan006_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan006.tex').write_text(s)
