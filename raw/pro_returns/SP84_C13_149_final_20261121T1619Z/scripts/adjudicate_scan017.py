"""Single-use scan017 main-reader adjudication from personally inspected crops."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan017_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b01','The dark upper figure consists of two joined loops and reads 8. The first reading preserves the author-page wrapper; the second supplies only the same numeral.')
c('b02','The short cancelled run has a low loop, a possible faint detached i dot and a terminal hump. The cancellation covers the lower joins, so ain, un and une cannot be separated securely. De, the apostrophe, and the continuous underline below action extérieure agree.',r"de \deleted{\unsure{ain|un|une}} l'\uline{action extérieure}")
c('b03','All four upper horizontal arrowheads and the upward head from Gamma are separately visible; the upward label is phi. The two-leg kernel signs are smaller than the adjacent capital A and match the inline pi forms, supporting lowercase pi rather than capital Pi. Diagram numbering and endpoints agree. Operator-name spacing and TeX layout are rendering differences.')
c('b04','The insertion leader clearly attaches un before the formula. The first group glyph has a short roof, two legs and a curved inner return, without the enclosed bowl required for R; it matches the second pi. The K forms are full-height angular capitals, whereas the k following the tensor sign is reduced. Bars, slash, index 1 and equality agree.')
c('b05','The raised word has an e loop, a continuous s-like bend and final t on the same inserted baseline. The middle stroke is not two crossing diagonals of x. Its leader attaches before the q of qu’on. Retain the literal signifie inserted est qu’on, including its grammatical irregularity.')
c('b06','Heavy cancellation leaves initial c/o curves, a low joined run, a long p-like descender and a later tall stem. These are compatible with both proposed compatible and correspond, but do not securely expose the middle letters or a word boundary. Preserve both tentative readings; do not complete the deleted prose from context.',r'\deleted{\unsure{compatible|correspond}}')
c('b07','The cancelled first glyph has the upper curl and lower-left hook of S, followed directly by barred K; no p/e/c bodies occur between them. The live barred eta has a short left stem, right arch and long descender, unlike that S. The barred letter inside Spec retains the angular arms of K, matching the nearby cancelled and indexed K forms. The full lower half confirms the descender and the ending de K with its point.')
c('b08','After the dotted i the next stroke forms a low v-shaped trough and rising exit into a separate o; there is no independently upright r shoulder there. This reverses the first reading’s r interpretation. The crop supports décrivons, agreeing with H at this word.',r'décrivons')
c('b09','The short word has low initial m shoulders, a reduced e and one tall terminal t. There is no enclosed p bowl or descending p stem, nor enough separate letter bodies for porte. Cœur and the closing parenthesis agree. Retain the literal met à cœur).')
c('b11','The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1.',r'$\pi=\pi_{\bar K/K}$ \inserted{et $\Gamma=\Gamma_{\bar K/K}^{\unsure{can|\illegible{}}}$} sont des')
ch['b11']['crop']='crops/149_scan017_audit_b11_full.png'
c('b12','The phi, colon, Gamma and Aut ext(pi) agree. The short shaft ends in a dark downward turn without two separable arrowhead arms. Both readers retain the same dash/arrow alternatives, in opposite order; arrow length and operator spacing are TeX choices, not additional ink.')
c('b13','The thin pale lower-left number is 16. Its placement and hand differ from the large dark author-page 8 at the top, so retain the margin wrapper rather than treating it as a second author page number.')
(R/'documentation/149_scan017_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan017.tex';s=p.read_text()
for k in ['b02','b06','b08','b11']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
p.write_text(s)
p=R/'reviews/149_scan017.json';r=json.loads(p.read_text())
mapping={'c01':'b02','c04':'b06','c06':'b08','c09':'b11'}
for x in r['changes']:
 if x['id'] in mapping:
  k=mapping[x['id']];x.update(final=ch[k]['final'],evidence=ch[k]['evidence'],against_C=True,confidence='high' if k=='b08' else 'low')
  if k=='b08':x['against_H']=False
  if k=='b11':x.update(crop=ch[k]['crop'],box=[1325,1850,1640,2000])
for x in r['doubts']:
 if 'Opening line' in x['place']:x.update(reading=r'\deleted{\unsure{ain|un|une}}',alternatives=['ain','un','une'],reason=ch['b02']['evidence'])
 if 'line 6' in x['place']:x.update(reading=ch['b06']['final'],alternatives=['compatible','correspond','partly unreadable cancelled run'],reason=ch['b06']['evidence'])
r['doubts'].append({'place':'Main paragraph line13, raised cluster above the indexed Gamma in the addition','reading':r'\Gamma_{\bar K/K}^{\unsure{can|\illegible{}}}','alternatives':['can','unreadable raised cluster'],'confidence':'low','reason':ch['b11']['evidence']})
for x in r['inventory']:
 if x['element']=='e03':x['first_words_or_objects']=r'de \deleted{\unsure{ain|un|une}}'
 if x['element']=='e08':x['first_words_or_objects']=r'\unsure{compatible|correspond}'
 if x['element']=='e11':x['first_words_or_objects']=r'et \Gamma=\Gamma_{\bar K/K}^{\unsure{can|\illegible{}}}'
for x in r['notation']:
 if x['written']==r'\Gamma=\Gamma_{\bar K/K}':
  x.update(written=r'\Gamma=\Gamma_{\bar K/K}^{\unsure{can|\illegible{}}}',rendering=r'\inserted{et $\Gamma=\Gamma_{\bar K/K}^{\unsure{can|\illegible{}}}$}',evidence=ch['b11']['evidence'])
for x in r['hand']:
 if 'second r of décrirons' in x['habit']:
  x.update(habit='The v in décrivons has a low trough and rising exit; the m/e run of met is compressed before a tall t.',consistency='Independent audit reverses the earlier r interpretation after comparing the full word crop.',misread='The first transcription and C had décrirons; H’s décrivons is supported here. Met remains unchanged.')
for x in r['diff_coverage']:
 if x.get('change_id') in mapping:
  k=mapping[x['change_id']];x['reason']=ch[k]['evidence'];x['final']=ch[k]['final']
r['notes']=[x.replace('The verb is décrirons, and the following word is cœur, not H’s décrivons and examiner.','The independent audit reads décrivons, agreeing with H at that verb; the following word remains cœur, not examiner.') for x in r['notes']]
r['notes'].append('Independent audit: all12 differing boxes and34 token spans personally inspected. Four boxes changed: the two cancelled words gain alternatives, décrivons replaces décrirons, and a previously omitted raised cluster is recorded tentatively as can or unreadable. The frozen b11 rectangle clipped its top; one supplementary full-formula scope crop is documented, preserving the original rectangle. No mathematical check was added.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
