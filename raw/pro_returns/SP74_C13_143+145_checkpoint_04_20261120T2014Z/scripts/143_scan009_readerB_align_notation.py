import json,re
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=root/'reviews'/'143_scan009_readerB.tex'
def align(s):
    s=re.sub(r'(?<![A-Za-z])X(?![A-Za-z])',lambda m:r'\mathfrak X',s)
    s=s.replace(r'\mathcal E',r'\unsure{\mathcal E|\Sigma}')
    return s
p.write_text(align(p.read_text()))
p=root/'reviews'/'143_scan009_readerB.json'
r=json.loads(p.read_text())
for c in r['changes']:
    c['final']=align(c['final'])
    if c['place'] in ['Parenthesis: this time E-prime','Parenthesis: inverse-image ambient group','Compatibility sentence: operations','Cancelled final line, group']:
        c['confidence']='low'
        c['ink']='The glyph has two rounded open lobes and is consistent with the extension-group glyph elsewhere on this page. C reads calligraphic E and H reads Sigma. Reader B initially preferred E, but the main reader retained E/Sigma as unresolved across readers; the candidate follows that common uncertainty without asserting a settled identification.'
r['changes'][0]['ink']="The tilde-X is followed by a detached short rising prime before (j). The first Hom argument has a separate prime above the long j subscript. The second is a rounded two-lobed extension-group glyph, left uncertain between calligraphic E and Sigma under the main reader's convention. Its crossed-out lower index retains the crossed looped X and a small prime. The obliterated superscript is over the initial Psi, not over Psi_j as the H note says; ext remains uncertain."
r['changes'][7]['ink']="Both ext superscripts, the family subscript j in J, tilde, X-prime and capital undotted J are visible. Two small points support the colon. Both extension-group letters retain the rounded two-lobed form and are kept uncertain between calligraphic E and Sigma under the main reader's convention. The purported j after G-prime is not independently separable from the comma and cancellation stroke. The stroke just after (J) coincides with an oblique cancellation and cannot securely be assigned as an outer right parenthesis. No additional final outer parenthesis is securely visible at the right edge. The candidate marks the local uncertainties."
for d in r['remaining_doubts']:
    d['reading']=align(d['reading'])
r['remaining_doubts'].append({'place':'Extension-group glyph throughout the page','reading':r'\unsure{\mathcal E|\Sigma}','alternatives':r'\mathcal E or \Sigma','confidence':'low','reason':'The glyph is rounded and two-lobed. Reader B prefers calligraphic E, but the main reader reports disagreement between readers and requires the same unresolved choice throughout until further evidence settles it.'})
for c in r['certainty_resolutions']:
    c['final']=align(c['final'])
r['notation'][0]={'form':r'\unsure{\mathcal E|\Sigma}','meaning':'extension/action-group glyph; its primed version is defined here as an inverse image','evidence':'Rounded two-lobed form throughout scan009. Reader B initially preferred E; under the updated notation table the E/Sigma identification is left uncertain consistently.'}
r['notation'][3]={'form':r"\mathfrak X' = \mathfrak X-D",'meaning':'complement of the divisor','evidence':'Explicitly written on the last line of I. The main reader established mathfrak X for the looped crossed capital in the updated notation table. Reader B has not inspected any other page.'}
r['abbreviations']=[a for a in r['abbreviations'] if a['form']!='ext']
r['hand_log'][0]={'habit':'The extension-group glyph is open, rounded and two-lobed; the distinction between cursive E and Sigma cannot be treated as settled.','places':'All extension-group occurrences in (25), the explanatory paragraph and the cancelled (26) block.','scope':'All occurrences on this assigned page inspected; the main reader requires the shared unresolved E/Sigma encoding.','misreadings':'C gives calligraphic E; H gives Sigma. Reader B prefers E but does not classify the H reading as a confirmed misreading.'}
r['notes'].append({'id':'143_scan009-N5','text':'After the main reader updated notation.md, the candidate was aligned to mathfrak X for the looped capital and unsure{mathcal E|Sigma} for every extension-group occurrence. Reader B inspected only scan009; these cross-page conventions were supplied by the main reader. The rounded ink had led Reader B to prefer E, but the candidate preserves the unresolved identification.'})
r['raw_difference_disposition']='Every packet difference was inspected against the original and both full-resolution halves, including agreements outside the difference list. Material loci are recorded above, including readings retained from C against H. H editorial marginal/note wrappers, C scan wrapper, line breaks, [1ex], typeface encodings of Q, and equivalent emphasis/strike macros were not counted as reading changes. The main reader subsequently established mathfrak X for the looped capital, and that convention has been applied throughout the candidate without treating the old C X wrapper alone as a different letter. The E versus Sigma identification remains uncertain consistently under the main reader\'s notation table; its distinct loci are retained in the comparison rows. Insertion attachment and the cancelled superscript/index are addressed in the formula and insertion evidence. All uncertain residue is marked in the candidate; no other page was inspected, and no OCR, web search or TeX compilation was used.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
required=['key','reader','stage','image_views','changes','decisions','inventory','remaining_doubts','certainty_resolutions','notation','abbreviations','hand_log','notes','check_events','unresolved_for_main','raw_difference_disposition']
assert all(k in r for k in required)
assert [d['id'] for d in r['decisions']]==['M0660','M0661']
assert len(r['changes'])==19
print('Aligned candidate/report to supplied notation; schema fields present; 19 comparison rows; 25 inventoried elements; 6 inspected crops. No TeX compilation.')
