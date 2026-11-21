"""Single-use application of the main reader's visual audit decisions."""
from pathlib import Path
import csv, json
R=Path(__file__).resolve().parents[1]; ch={}
def c(k,e,s='first',final=None):
    ch[k]={'personally_inspected':True,'selection':s,'evidence':e,'changed':'no' if s=='first' else 'yes'}
    if final is not None:ch[k]['final']=final
c('b01','The upper diagonal runs into an open angular crossbar and a long right upright. It is an open 4, without the closed upper bowl of 9. Keep the author-page wrapper and 4.')
c('b03','The first connector has only a tiny upright cap, whereas the Pi connector has two clear oblique head strokes. Both full Q indices and Pi capitals are visible. Dollars, quad/qquad and braces around mathbb Q are representation differences only.')
c('b04','The low u is followed by the n arch and its long descending terminal return. There is no separately formed e between that return and the next formula. Adopt un, independently also read by the second reader; the i.e. stops, barred K/K and comma remain.','second')
c('b07','The first sign has upper, middle and lower E arms with a closely retraced left stem. Its form and indexed use match the adjoining E occurrences. No local contrast establishes a second alphabet. The Gamma, barred rational index and distinct right arrowhead are present. Retain ordinary E; display dollars and bar/overline spelling are syntax.')
c('b08','The E is more rounded here, but retains the same three arms and stem as the displayed indexed E in b07. The changed curve does not establish a new mathematical alphabet. Retain the ordinary indexed E with both other objects and ou.')
c('b09','The article begins with the tall narrow l loop without a left bowl of d, followed by the low es. Retain les. The dash is a single horizontal source stroke; two or three TeX hyphens do not change its reading. The cancelled f and live morphismes are present.')
c('b10','The looped f is crossed by oblique replacement strokes. The live m is visible in the wider b09 context. The second answer scopes the deleted letter alone; retain that deletion and the live following m.')
c('b12','A detached short accent is visible above the compressed vowel after m and before the following t. The paired quotation ticks, separate underline and comma are also present. Keep arithmétiques; underline/uline is syntax only.')
c('b13','After the dotted i and n run there are several low separate returns before the final tall t, supporting eront rather than the shorter ant. The article has the looped l with a short a return. A separate full stop follows situation and the tall detached exclamation mark is visible at the far right, although the second reader excluded it from scope. Retain domineront la situation. ! without supplying qui.')
c('b14','The kernel sign has two upright legs and a straight roof, but is lower and smaller than the full capitals. Its matching denominator in b17 starts distinctly below the E roof; by contrast both Pi capitals in b03 are full-height. The local paired occurrences support lowercase pi despite its angular drawing. Retain pi and the complete barred-K/K index.')
c('b15','The paired high opening ticks and following n arch are clear; the final letter lacks a tall crossed t. The initial small open curve admits o or e. Keep the opening quotation and mark on/en, rather than resolving the subject by grammar. The following l\u2019appelle is unchanged.','custom',r"-- ``\unsure{on|en} l'appelle")
c('b16','The two low connected components before quotient form a/u without a word break, independent accent, or separate n arch. Keep au. The two quotation pairs, Galois, ordinary E and complete index agree.')
c('b17','The denominator is the same small angular pi as b14, distinctly lower than E, unlike the full-height Pi in b03. Both full indices, equality, left hook and right head, rational bar and comma are visible. The raised Gamma mark has a light rounded body and dark crossing stroke, not a clean prime; whether that crossing cancels the a-like mark is not secure. Make deletion status explicitly doubtful rather than treating the second live-a reading as settled.','custom',r'E_{\bar K/K}/\pi_{\bar K/K}=\Gamma^{\unsure{\deleted{a}|a}}_{\bar K/K}\hookrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q},')
c('b18','The rotated note begins with a tall oval O above the low n, supporting On. The second Gamma bears a wider dense superscript: a round opening, small adjacent curved strokes and an oblique dark crossing; a cancelled a, cancelled can, or live can cannot be separated securely. Both formula indices and equality are complete. A slanted accent is present over arithmétique; the closing quotation has two high ticks, the second paler, visible also in the existing first crop c15. Keep those ticks. The separate thin 8 is already covered by b19 and is retained as foliation, not part of the note.','custom',r'\margin{On va noter $\Gamma=\Gamma^{\unsure{\deleted{a}|\deleted{can}|can}}_{\bar K/K}$ cette ``partie arithmétique\'\'}\margin{8}')
# Use ordinary apostrophes, not control symbols, in the diplomatic quotation.
ch['b18']['final']=ch['b18']['final'].replace("\\'", "'")
(R/'documentation/149_scan009_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan009.tex';s=p.read_text()
s=s.replace(r'\unsure{un|une}', 'un').replace("``on l'appelle",r"``\unsure{on|en} l'appelle")
s=s.replace(r'\Gamma^{\deleted{\unsure{a}}}_{\bar K/K}\hookrightarrow',r'\Gamma^{\unsure{\deleted{a}|a}}_{\bar K/K}\hookrightarrow')
s=s.replace(r'\margin{on va noter $\Gamma=\Gamma^{\deleted{\unsure{a}}}_{\bar K/K}',r'\margin{On va noter $\Gamma=\Gamma^{\unsure{\deleted{a}|\deleted{can}|can}}_{\bar K/K}')
p.write_text(s)
p=R/'reviews/149_scan009.json';r=json.loads(p.read_text()); changes={x['id']:x for x in r['changes']}
def upd(i,b,final,**kw):
    x=changes[i]; x.update(final=final,evidence=ch[b]['evidence'],crop=f'crops/149_scan009_second_{b}.png',**kw)
    q=next(q for q in r['audit_boxes'] if q['box']==b);x['box']=[q[k] for k in ('x0','y0','x1','y1')]
upd('c03','b04','un',confidence='medium')
upd('c12a','b15',r'\unsure{on|en}',confidence='medium')
upd('c14b','b17',r'\Gamma^{\unsure{\deleted{a}|a}}_{\bar K/K}',confidence='low')
upd('c15a','b18','On va noter',against_C=True,confidence='medium')
upd('c15b','b18',r'\Gamma=\Gamma^{\unsure{\deleted{a}|\deleted{can}|can}}_{\bar K/K}',confidence='low')
r['doubts']=[d for d in r['doubts'] if d['place']!='L5, article after i.e.']
for d in r['doubts']:
    if d['place'].startswith('L18, superscript'):
        d.update(reading=changes['c14b']['final'],alternatives=['cancelled a','live a','another overwritten small mark'],reason=ch['b17']['evidence'])
    elif d['place'].startswith('Lower-left note, superscript'):
        d.update(reading=changes['c15b']['final'],alternatives=['cancelled a','cancelled can','live can'],reason=ch['b18']['evidence'])
r['doubts'].append({'place':'L16, subject before l’appelle','reading':r'\unsure{on|en}','alternatives':['on','en'],'confidence':'medium','reason':ch['b15']['evidence']})
r['notes'][2]='The opening abbreviation reads hom, not homs or homom. The independent audit resolves the article before barred K/K to un: the n has a long return but no further e body. The connector reads d’où. These are visual decisions, not grammatical completions.'
r['notes'][4]='The f beneath morphismes is a readable cancelled f. The two Gamma superscripts remain doubtful in letter content and cancellation state; these C doubts are not enumerated by MARKS.tsv.'
r['notes'][5]='Two opening quotation ticks occur before the subject of l’appelle. The subject is now unsure on|en: the first small open curve is not secure, though n is. The additional quotation pair remains unmatched; no closing partner is supplied.'
r['notes'][7]='The slanted note reads On va noter, with a tall initial O; its Gamma superscript remains unsure cancelled a|cancelled can|live can. The accent and both pairs of quotation ticks around partie arithmétique are retained. The separate thin 8 is foliation.'
r['notes'][8]='The main Gamma superscript is unsure cancelled a|live a. A clean prime is not supported by its rounded and crossing strokes. No proof or background mathematical check was performed.'
r['notes'].append('Independent audit: all14 differing boxes were inspected. Four box readings changed: article certainty, subject uncertainty, explicit superscript cancellation uncertainty, and the marginal note’s initial capital plus superscript uncertainty. The small pi forms were compared directly with the full-height Pi of (6); ordinary E was compared across three same-page occurrences.')
for h in r['hand']:
    if h['habit'].startswith('The low final run'):
        h.update(consistency='The independent audit isolates the n arch and terminal return in un, without a further e body.',misread='C gives une; H and the independent audit give un.')
    if h['habit'].startswith('Small superscripts'):
        h.update(consistency='Both marks have rounded and crossing strokes, but cancellation is now explicitly doubtful in the transcription; the marginal mark is wider and may contain can.',misread='H gives a prime in the main line and omits the marginal superscript; C treats both as cancelled unsure a.')
for d in r['diff_coverage']:
    if d.get('change_id') in ('c03','c12a','c14b','c15a','c15b'):d['reason']='Updated by independent image-only audit; see the referenced final change and the complete second-reading adjudication.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
