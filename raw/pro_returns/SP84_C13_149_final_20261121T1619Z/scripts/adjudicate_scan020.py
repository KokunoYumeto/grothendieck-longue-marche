"""Single-use main-reader adjudication of the frozen scan020 comparison."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan020_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b02','The two-legged sign is distinctly shorter than the adjacent K and Gamma, with the same short legs and overhanging roof as the live kernel signs in b06. Retain lowercase pi, its small subscript1, the literal equality, capital K forms and comma. No expected mathematical replacement is supplied.')
c('b03','The whole interlinear phrase and its attachment before the ambient Gamma agree. After non there is a detached-looking low horizontal run, but its left end is not cleanly separated from the n return; retain hyphen/space uncertainty. Both Q forms have an extra internal stroke, supporting mathbb Q; the first alone is barred. The leader is separate from the Gamma stem and roof, and the final adverb has its own underline and point.',r"sur lesquels \inserted{un sous-groupe ouvert $\Gamma$ (\unsure{non-précisé|non précisé} d'avance) de} $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opère \uline{extérieurement}.")
c('b05','The complete marginal rectangle was read upright in its saved rotated views. The opening two reduced curves leave on/en uncertain. The next word has an opening s curve, low u, two long p descenders and a low ose run: suppose. On the next line, the initial p descender and low our support pour; the following low s, dotted i, m run, long p/l/f strokes and final ier support simplifier rather than définition. After que c’est, a longer r/e/l/a/t/i/f run is visible: the tall strokes overlap the preceding line, but the t cross, detached i dot and final long f return exclude the short le reading. The next line begins a very reduced a/u-like unit crossed by the descender of que; retain tentative au, not a certain Greek letter generated from that crossing. Two separate equals bars, lowercase k, subset, barred double-stroked Q and three terminal points are clear. The note remains marginal.',r"\margin{\unsure{on|en} suppose pour simplifier que c'est relatif \unsure{au} $=$ $k\subset\overline{\mathbb Q}$\ldots}")
ch['b05']['crop']='crops/149_scan020_second_b05_rot-35_fullview.png'
c('b06','The cancelled letters have a stem and three bars, with a detached prime after the first. The old shaft survives below the oblique hatching, ending in a dark point with short upper and lower returns; retain its right arrow. The separate live arrow has two plainly separated branches. Its short two-legged signs match b02 in relative size and curved right foot, so retain lowercase pi, the first prime and comma.')
c('b07','Both readers give the same visible opening parenthesis, narrow1, closing parenthesis and comma. Math-mode wrappers change no ink; retain the established typesetting.')
c('b09','The lower Gamma_K sits at the height of baseline de and sur. Gamma= is raised to its upper left; subset Gamma_K-prime rises to its upper right, with a curved attachment line ending after the baseline group. Thus only these two surrounding pieces are inserted, not the entire expression. The two equality bars, open-right subset and final K prime agree.',r"de \inserted{$\Gamma=$}$\Gamma_K$\inserted{$\subset\Gamma_{K'}$} sur")
c('b10','The first sign has short legs and a curved right foot, matching lowercase pi in b06. In the target, a retraced diagonal joins the right leg to the roof, but a separate left descent and curved right foot remain; this is the same pi construction, not a secure Z with one diagonal between two bars. Its size matches the source. The connector ends in one downward return and lacks a separate upper branch or pointed two-sided head, unlike b06 and b16. Retain the bare shaft and prime.')
c('b12','Both letters have a continuous upper curve, inward waist and long lower return, contrasting locally with the stem and separate bars of both cancelled E letters in b06. All four lower forms repeat this construction, including b16. This same-sheet comparison supports calligraphic E here; curvature alone is not used as a rule for every E elsewhere. The comma and detached second prime are clear.')
c('b13','There are two separate quotation ticks on each side, plus independent parentheses. After the final r a small open e loop precedes the terminal s-like downward return; this supports extérieures, including the feminine e. The long curve below is the insertion leader attaching before de, not another parenthesis. Keep the prescribed paired backtick/apostrophe notation.')
c('b14','Both connectors end in a single short downward return, with no separate upper head branch; retain bare shafts, unlike the clear head in b16. The subscripts are angular K and K-prime, and both Q forms have an independent internal stroke. The upper équivalence rigide is visible context omitted from the second scope, not absent text. At the physical right edge, upper and lower portions of one large closing curve survive; retain the closing parenthesis without completing its clipped middle as additional text.')
c('b16','Both curved letters repeat the upper lobe, inward waist and lower return of b12, and contrast with the stemmed three-bar E in b06: retain the local calligraphic alphabet. The target has a separate prime; the arrow has two clear branches. The following de, capital Gamma and point agree.')
c('b17','The small thin lower-left number is1 followed by a looped9 with a descending curve. It is marginal foliation, so retain the margin wrapper; there is no numerical disagreement.')
(R/'documentation/149_scan020_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan020.tex';s=p.read_text()
for k in ['b03','b05','b09']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
p.write_text(s)
p=R/'reviews/149_scan020.json';r=json.loads(p.read_text())
for x in r['changes']:
 if x['id'] in ['c05','c07']:
  k={'c05':'b05','c07':'b09'}[x['id']]
  x.update(final=ch[k]['final'],evidence=ch[k]['evidence'],against_C=True,against_H=True,confidence='medium' if k=='b05' else 'high',crop=ch[k].get('crop',f'crops/149_scan020_second_{k}.png'))
b=next(z for z in r['audit_boxes'] if z['box']=='b03')
r['changes'].append({'id':'audit_b03','place':'Opening insertion, parenthetical non précisé','C':'non précisé','H':'non précisé','final':r'\unsure{non-précisé|non précisé}','evidence':ch['b03']['evidence'],'crop':'crops/149_scan020_second_b03.png','box':[b[t] for t in ['x0','y0','x1','y1']],'confidence':'low','against_C':True,'against_H':True,'kind':'other','error_category':'Other','marked_in_H':False,'mathematical':False})
for k,place,reading,alts in [('b03','Opening insertion, possible hyphen',r'\unsure{non-précisé|non précisé}',['non-précisé','non précisé']),('b05','Slanted marginal note, opening word',r'\unsure{on|en}',['on','en']),('b05','Slanted marginal note, reduced word before equals',r'\unsure{au}',['au'])]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':ch[k]['evidence']})
for x in r['inventory']:
 if 'Gamma=' in x.get('first_words_or_objects','') or r'\Gamma=\Gamma_K' in x.get('first_words_or_objects',''):
  x['first_words_or_objects']=r'\inserted{$\Gamma=$}$\Gamma_K$\inserted{$\subset\Gamma_{K\prime}$}'
for x in r['diff_coverage']:
 if x.get('change_id') in ['c05','c07']:
  k={'c05':'b05','c07':'b09'}[x['change_id']];x['reason']=ch[k]['evidence']
r['notes'][3]='The marginal note now reads tentative on/en suppose pour simplifier que c’est relatif, followed by tentative au, literal equals, k subset barred Q and three points. The long descender of que crosses the reduced au-like unit; it is not securely a separate Greek symbol. The written equals remains the short form discussed in the abbreviations list. The independent audit reverses the initial short le reading after c’est.'
r['notes'][5]='The baseline Gamma_K has two additions around it: Gamma= at upper left and subset Gamma_K-prime at upper right. The first inserted extérieures has literal parentheses and paired quote ticks. The second extérieures has a leader without textual parentheses. These attachment questions are separate from the words and signs themselves.'
r['notes'].append('Independent audit: all12 differing boxes were personally inspected, including both saved upright views of the same marginal rectangle. Three boxes changed: the possible non-précisé hyphen, the marginal wording and its local uncertainties, and the split insertion around baseline Gamma_K. The lowercase kernel signs, four local calligraphic-E forms, short headless shafts, extérieures ending and clipped closing parenthesis were retained after explicit comparison. No mathematical proof check was added.')
for x in r['hand']:
 if x['habit'].startswith('An entire formula'):
  x.update(habit='Interlinear additions can surround a formula that remains on the main baseline.',consistency='On scan020 Gamma_K is baseline; Gamma= and subset Gamma_K-prime are raised additions on either side.',misread='C and the first pass included baseline Gamma_K in one whole insertion; H instead marked sur as inserted. The independent audit separates the additions.')
for x in r['notation']:
 if x['written']==r'\Gamma=\Gamma_K\subset\Gamma_{K\prime}':
  x.update(rendering=ch['b09']['final'],evidence=ch['b09']['evidence'])
 if x['written']==r'\Gamma=\Gamma_K\subset\Gamma_{K\'}':
  x.update(rendering=ch['b09']['final'],evidence=ch['b09']['evidence'])
 if x['written'].startswith(r'\Gamma=\Gamma_K'):
  x.update(rendering=ch['b09']['final'],evidence=ch['b09']['evidence'])
for x in r['abbreviations']:
 if x['form']=='=':x['place']='Slanted marginal note, after relatif and tentative au'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
