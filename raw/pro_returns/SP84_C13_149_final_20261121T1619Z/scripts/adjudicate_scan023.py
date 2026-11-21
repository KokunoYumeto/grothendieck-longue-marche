"""Single-use root adjudication; every differing box personally inspected."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan023_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b02','The initial tall t has a looped cross-stroke, followed by a flattened a/n run, a second tall t, a low o with a detached circumflex-like stroke, and final tall t. There is no separate i dot or independent two-word et soit sequence. Retain tantôt.')
c('b03','The curved low terminal is aligned with the detached dot of the index i. No additional mark follows that dotted index. The limit arrow has a right point; K, equality and A_i are intact. Retain the opening expression without an extra comma.')
c('b04','The cancelled first glyph retains the stem and angular limbs of K. The following oval has internal crossing strokes besides the horizontal cancellation, supporting tensor rather than a plain0. The live eta, Spec(K), equality, inverse-limit left head and U_i remain intact. The second reading includes the following comma within its formula scope; the page already carries that separator outside the formula. This scope difference does not change the page.')
low=r'{}_{\deleted{\unsure{\bar\eta|\bar K|\bar Q}}}'
f5=first['b05'].replace(r'\deleted{\unsure{\bar\eta|\bar K}}',low)
c('b05','The group letter has the same short two-legged roofed construction as the local pi_1 forms, with curved feet; retain the established lowercase pi notation. In the first argument the crossed barred glyph lies distinctly low, below the U_i baseline. Its surviving upper bar and closed/angled inner traces permit barred eta, K or Q; the cancellation prevents a secure alphabet assignment. Preserve its low placement with a separate subscript-position wrapper, without assigning it to the existing i index. The live following barred glyph remains eta/K: its angled upper join is not settled by the clearer later eta-primes. The full limit formula, index i, comma, tensor, base k/K and doubled Q stroke were rechecked.',f5)
f6=first['b06'].replace(' :',r' \unsure{:|.}')
c('b06','The labels f_i and g_i are above shallow continuous arcs, which lack a separate central brace cusp; retain overlines. The main-line f/g, restriction strokes, A_i indices and equality are clear. The far-right small points do not securely distinguish a full colon from a single stop once the index dot is separated, so retain colon/point uncertainty; no comma descent is visible.',f6)
c('b07','The two tiny raised forms have short crossing arms, matching the clearer star after g in b17; they are retained as asterisks, not a letters. All pi forms match the short local group notation. The map endpoint has only a small cap, so the head/shaft doubt remains. The target U has blank space above it, unlike the clear barred U in b17; retain unbarred U_i. The crossed following glyph retains K-like arms but its overlapping upper strokes still allow barred eta. The whole formula was checked.')
c('b10','K and A have separate primes and the lower index j has a long hooked descent. Beneath lim the shaft ends in a short down-return without two separate head branches. Both readings encode this same unresolved arrow-versus-shaft alternative; retain the first complete-formula encoding.')
c('b11','Both group letters have the same short local pi construction. The source K has a separate prime; V_j and eta-prime have separate bars and their distinct lower strokes. The later Spec argument is plain A_j, with no raised prime, and the tensor index has the curled k form. Q has an inner stroke and a separate bar, followed by a real point. The comma occurs between the display expression and avec; math-delimiter placement changes no reading.')
c('b12','The long horizontal strike crosses the old word. Its opening low humps and final x-like crossing fit normaux, but the middle r/m/a/u joins also meet the descending g and attachment of the replacement. Not every old letter is plain, so retain its doubt. The raised réguliers and final parenthesis remain live.')
c('b15','The initial mark is one long horizontal stroke with no closed bowl or second n stroke. It is a dash, not a or on. Donc has a looped d and compressed o/n/c run. Exactly two dark points descend obliquely to the right; retain the colon/two-point alternative.')
c('b16','The source has the same short two-legged pi construction as the neighboring pi_1, with a distinct K-prime index. The arrow has two clear head branches. Both V_j and eta-prime have separate bars; the comma and parentheses are present. Retain the first reading.')
f17=r'$f^*$ et $g^*:\pi_{K\prime}\substack{\unsure{-|\longrightarrow}\\\longrightarrow}\pi_{\deleted{\unsure{K|k}}}(\bar U_i)$'
f17=f17.replace(r'K\prime',"K'")
c('b17','The raised signs after f and g have crossing arms and repeat the local asterisks, with no complete a bowl. The source pi has a K-prime index. The upper shaft has only a small end-return, while the lower arrow has a two-branch head: localize the uncertainty to the upper head. In this target the roof and two pi legs are followed immediately by the heavily crossed low K/k. Unlike the three separate uprights of the clear pi_1 targets in b16 and b20, no independent live1 can be separated here. Omit the supplied1 and retain the cancelled K/k in its low index position. The following U_i has a separate bar. First crop c14 was also inspected to confirm the target stroke count.',f17)
c('b20','Each pi has two legs plus a separate lowered1; the two arguments have distinct bars and j/i indices. The shaft has a clear two-arm right head. A separate point follows the closing parenthesis. Moving that point inside math delimiters changes no ink reading.')
f21=first['b21'][:-1]+r'\unsure{,|;}'
c('b21','The last two source baselines contain consé followed by a separate hyphen, then quence on the next line. The space after the typed hyphen in the second reading is line-wrap representation. Résultat has an initial r, accent, low s/u run and tall l/t strokes; it is readable. The final dark mark has a curved lower body and a tiny upper component whose separation is not secure, so retain comma/semicolon uncertainty. The two equalities and indices i are unchanged.',f21)
(R/'documentation/149_scan023_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan023.tex';s=p.read_text()
s=s.replace(r'\bar U_i\deleted{\unsure{\bar\eta|\bar K}}',r'\bar U_i'+low)
for k in ['b06','b17','b21']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
p.write_text(s)
p=R/'reviews/149_scan023.json';r=json.loads(p.read_text());boxes={x['box']:x for x in r['audit_boxes']}
def upd(cid,k,final,**kw):
 x=next(z for z in r['changes'] if z['id']==cid);b=boxes[k]
 x.update(final=final,evidence=ch[k]['evidence'],crop=f'crops/149_scan023_second_{k}.png',box=[b[t] for t in ['x0','y0','x1','y1']],**kw)
upd('c04','b05',low,confidence='low',against_C=True)
upd('c06','b06',r'\unsure{:|.}',confidence='medium')
upd('c15','b17',r'\pi_{\deleted{\unsure{K|k}}}(\bar U_i)',confidence='medium',against_C=True,mathematical=True)
upd('c18','b21',r'consé-quence du résultat plus général\unsure{,|;}',confidence='medium')
for x in r['doubts']:
 if x['place']=='L5, crossed low glyph after U_i':x.update(reading=low,alternatives=[r'\bar\eta',r'\bar K',r'\bar Q'],reason=ch['b05']['evidence'])
 if x['place']=='L18, crossed glyph in the complete paired-arrow formula':x.update(reading=r'\pi_{\deleted{\unsure{K|k}}}(\bar U_i)',reason=ch['b17']['evidence'])
r['doubts'].extend([dict(place='L6, point after restriction equality',reading=r'\unsure{:|.}',alternatives=[':','.'],confidence='medium',reason=ch['b06']['evidence']),dict(place='L18, upper parallel-shaft head',reading=r'\unsure{-|\longrightarrow}',alternatives=['-',r'\longrightarrow'],confidence='medium',reason=ch['b17']['evidence']),dict(place='Last line, final punctuation',reading=r'\unsure{,|;}',alternatives=[',',';'],confidence='medium',reason=ch['b21']['evidence'])])
for x in r['inventory']:
 for key in ['first_words_or_objects','position']:
  if key in x:
   x[key]=x[key].replace(r'\deleted{\unsure{\bar\eta|\bar K}}',low).replace(r'\pi_1\deleted{\unsure{K|k}}',r'\pi_{\deleted{\unsure{K|k}}}')
byid={x['id']:x for x in r['changes']}
for x in r['diff_coverage']:
 if x.get('change_id') in ['c04','c06','c15','c18']:x['reason']=byid[x['change_id']]['evidence']
r['notes'][5]='The restriction labels f_i and g_i are above shallow overlines. The far-right punctuation now retains colon/point uncertainty. The first direct-limit arrow and inverse-limit heads are clear; the later direct-limit shaft and second-display map remain qualified. In the lower paired map the upper head is doubtful and the lower head is clear. No separate live1 is visible after the target pi before its cancelled low K/k, so that supplied numeral has been removed; nearby clear pi_1 formulas retain their separate numerals.'
r['notes'][8]='The cancelled opening fragment is K tensor. The live M1038 barred eta/K remains open. Its neighboring crossed low barred glyph now also allows barred Q and is represented below the baseline. The crossed glyph after the second display, normaux and the lower K/k remain qualified; a cancellation is not resolved unless all of its letters are plain.'
r['notes'][10]='The last source word is divided consé-/quence, with its hyphen preserved in the continuous text. The final punctuation retains comma/semicolon uncertainty. There is no margin prose, diagram or drawing beyond the separate foliation.'
r['notes'].append('Independent audit: all14 differing boxes were personally inspected; four boxes changed. The changes preserve the low crossed glyph, qualify punctuation and the upper paired-arrow head, and remove an unsupported live1 before the cancelled lower target index. Frozen first/second readings remain intact. These are ink judgments; no mathematical assertion was proof-checked.')
for x in r['hand']:
 if x['habit'].startswith('Barred eta'):x['consistency']='The live eta/K head remains ambiguous; the crossed low head also permits Q. Later eta-primes are clearer and do not remove local doubt.'
 if x['habit'].startswith('A small cap'):x['consistency']='The second-display map, later direct-limit shaft and upper shaft of the lower parallel pair have small ambiguous endpoints. The lower parallel arrow and later single arrow have clear heads.'
r['hand'].append({'habit':'A cancelled low index must not be replaced by an expected live1.','pages':[23],'consistency':'Local to the lower paired-arrow target; nearby clear pi_1 forms have a third separate upright after the two pi legs.','misread':'Both C and H supplied a live1 at that target; the independent reader omitted it and the crop comparison supports the omission.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
