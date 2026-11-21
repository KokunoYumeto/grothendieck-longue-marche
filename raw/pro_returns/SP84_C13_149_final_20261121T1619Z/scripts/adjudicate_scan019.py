"""Single-use scan019 main-reader adjudication, including full marginal text."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan019_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b02','The crowded initial word has a lower left loop, rising stem and reduced joined humps; these permit une, d’une or des, but no complete alternative is secure. The transverse overtrace still merges with the connections, so its cancellation state also remains uncertain. Extension ends in a low n return with a terminal hook but no separate s body. The raised angular K is after extension and before de.',r"\unsure{\deleted{\unsure{une|d'une|des}}|\unsure{une|d'une|des}} extension \inserted{$K$} de")
c('b04','The B has two lobes. Q contains an independent inner stroke in addition to its oval and tail, supporting the existing double-struck rendering. No final point is present.')
c('b06','The small group before topos has two reduced low curves; the second lacks a clearly isolated e loop or n shoulder. Ce/en cannot be securely separated. Topos and the detached low comma are clear. The short opening-parenthesis stroke and looped le at the right are retained as first-reading context; their omission from the second scope does not remove them.',r'\unsure{ce|en} topos, (le')
c('b07','The two Pi legs and roof agree. The Q has a separate inner stroke and tail, supporting mathbb Q. There is no separate point to its right.')
c('b08','The upper 2 and closing parenthesis are crossed independently. In the lower entry, the heavy live digit has two right-facing lobes of 3; lighter ink shows an older upper sweep, diagonal and foot, consistent with the already qualified earlier 2. Retain both layers and one shared closing parenthesis.')
c('b09','The two rounded E lobes match the ordinary indexed E in this hand; curvature alone does not establish a distinct calligraphic alphabet. Each Q has an extra internal stroke. The single shaft has a left angular head, with no parallel second bar or upper wave. Gamma, both parentheses and the literal pro-gr abbreviation agree.')
c('b10','The numeral has an oblique left stroke meeting a crossbar and a descending right stroke, supporting 4. The lower curved return does not turn the complete shape into two open lobes of 3. The closing parenthesis is distinct.')
c('b11','The article has a tall narrow l loop and a long reduced e return. Its initial low flourish does not independently establish a d bowl, and the second letter is not a separate two-leg u. Couple ends in one e return, without an additional s. Retain le couple.')
c('b12','All Q forms have their inner double stroke, with the indicated bars only; Ob has a narrow loop and upright/lower bowl, and Pi is capital. The detached curved mark after its index is large enough to permit a closing parenthesis as well as the first comma reading, so retain both. The lower map source remains mathcal-E/E uncertain. Its shaft ends in a downward dark wedge without a separately visible upper branch, leaving arrow/plain-shaft uncertain. The Gamma index and terminal point agree.',r'$\overline{\mathbb Q}\in\operatorname{Ob}\Pi_{\mathbb Q}$\unsure{,|)} $\unsure{\mathcal E|E}\unsure{\longrightarrow|-}\Gamma_{\overline{\mathbb Q}/\mathbb Q}$.')
c('b13','The cancellation is one independent line across un, the two short s strokes, groupe ouvert, Gamma and de. Between the second s and the g descender a separate short horizontal segment is visible beneath the long strike, supporting the literal ss-groupe hyphen. Do not expand it to sous.')
c('b14','The f loop, detached i dot and x-like crossing agree. The terminal e-run meets the leader; a possible second e and acute cannot be isolated securely, so retain fixée/fixe. Alg. is baseline context in the first scope, with its point visible at lower left. The raised word’s leader attaches before barred double-stroked Q.')
c('b16','The lower cancelled phrase has the p descender, ar, looped l/e, g descender and remaining roupe run. The raised replacement starts with an e loop and tall t, not a d plus e. A detached dot and tiny lower marks before Gamma still favour si but overlap the cancelled l, so that word remains qualified. Both Gamma letters, equality and barred/ordinary Q indices agree. The low comma follows the expression on the main baseline. The later par has an independent short stroke across it; no en intervenes before considérant.')
c('b17','The article after de has a tall l loop and open e return, not a closed a oval: retain the literal le. Above the o of the following word no independent circumflex can be separated securely from the nearby tall strokes, so record clôture/cloture uncertainty. The interlinear mark has one stem with angular branches, supporting k rather than two letters de or tr. Its leader attaches after alg.; the next baseline word has a looped d and low e, not sur. After the double-stroked Q, the longer low run is dans, followed by capital K.',r'de le \unsure{clôture|cloture} alg.\inserted{$k$} de $\mathbb Q$ dans $K$')
c('b18','An initial open c, following rounded trace, several obscured low humps and a terminal return remain under the strike. The middle cannot be segmented securely into mm or nn/ex, and the last hook may or may not be s. Preserve comme, connexe and connexes as tentative alternatives.',r'\deleted{\unsure{comme|connexe|connexes}}')
c('b19','The two kernel signs have comparable small size relative to capital K; retain lowercase pi. The relation has two low horizontal strokes and extra curved ink attached below the lower one. No diagonal cleanly crosses the upper bar, and its slight wave permits the independently proposed simeq interpretation. Preserve neq/equality/simeq instead of choosing from mathematical expectation. Both K forms, index1, parentheses and comma agree.',r'$\pi_K\unsure{\neq|=|\simeq}\pi_1(K)$,')
c('b20','The complete five-line margin was inspected upright using the same rectangle rotated clockwise90. The first noun is visibly shortened: g/r, a detached point, a short connecting dash, then oïde with a reduced terminal hook; no oup sequence supports expanded groupoïde. Retain gr.-oïde/gr.-oïdes uncertainty. Number6, En termes d’un, the colon, both formulas, bars, tensor signs, Q inner strokes, and (pas néc. connexe) sur lequel agree. After ou bien, the word has p descender, l/t uprights and a terminal t-like stroke, with no separate looped f for parfois: plutôt/plutot remains accent-uncertain. The next line begins le topos quotient: a q descender, low u/o, t uprights and dotted i support quotient, not galoisien. The mark after the B index is comma/parenthesis ambiguous. The following low four-letter run has an opening s curve, o/u bodies and terminal s, supporting sous rather than avec. The final Gamma index, opérant dessus and three separate dots agree. Margin placement is recorded explicitly.',r"\margin{6) En termes d'un $\overline{\mathbb Q}/\mathbb Q$ : par le \unsure{gr.-oïde|gr.-oïdes} $\Pi_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$ (pas néc. connexe) sur lequel $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opère --- ou bien \unsure{plutôt|plutot}, par le topos quotient $B_{K\otimes_{\mathbb Q}\overline{\mathbb Q}}$\unsure{,|)} sous $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opérant dessus\ldots}")
ch['b20']['crop']='crops/149_scan019_second_b20_rotated.png'
c('b21','The thin lower-left figures are a narrow1 and two-loop8. They are separate from the larger dark author9 at the top, so retain the margin wrapper.')
c('b22','The E_K is a rounded two-lobed capital comparable with the ordinary indexed E_Q in b09; no secure separate alphabet is established. The crop extends beyond the first scope to a comma, two very short low strokes and a compressed d-initial word. The full upper half confirms that the following line starts du groupe extérieur. The low strokes may be reduced au or a dash, and the word may be dessus or disons; the alternatives au-dessus / dash disons / dash dessus remain unresolved. Replace the existing au-dessus by this local uncertainty, without duplicating the continuation.',r'Par le groupe extérieur $E_K$, \unsure{au-dessus|--- disons|--- dessus}')
(R/'documentation/149_scan019_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan019.tex';s=p.read_text()
for k in ['b02','b06','b17','b18','b19','b20']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
old=r'$\overline{\mathbb Q}\in\operatorname{Ob}\Pi_{\mathbb Q}$, et un hom de groupes profinis $\unsure{\mathcal E|E}\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}$.'
new=r'$\overline{\mathbb Q}\in\operatorname{Ob}\Pi_{\mathbb Q}$\unsure{,|)} et un hom de groupes profinis $\unsure{\mathcal E|E}\unsure{\longrightarrow|-}\Gamma_{\overline{\mathbb Q}/\mathbb Q}$.'
assert old in s;s=s.replace(old,new)
old=r'Par le groupe extérieur $E_K$, au-dessus';assert old in s;s=s.replace(old,ch['b22']['final'])
p.write_text(s)
p=R/'reviews/149_scan019.json';r=json.loads(p.read_text())
mapping={'c01':'b02','c04':'b06','c19':'b18','c20':'b19','c22':'b20','c23':'b20'}
finals={'c01':r"\unsure{\deleted{\unsure{une|d'une|des}}|\unsure{une|d'une|des}}",'c04':ch['b06']['final'],'c19':ch['b18']['final'],'c20':ch['b19']['final'],'c22':r'ou bien \unsure{plutôt|plutot}, par','c23':'sous'}
for x in r['changes']:
 if x['id'] in mapping:x.update(final=finals[x['id']],evidence=ch[mapping[x['id']]]['evidence'],against_C=True,against_H=True,confidence='high' if x['id']=='c23' else 'low')
def add(cid,k,place,C,H,final,category='Words',math=False,confidence='low'):
 b=next(z for z in r['audit_boxes'] if z['box']==k)
 r['changes'].append({'id':cid,'place':place,'C':C,'H':H,'final':final,'evidence':ch[k]['evidence'],'crop':ch[k].get('crop',f'crops/149_scan019_second_{k}.png'),'box':[b[t] for t in ['x0','y0','x1','y1']],'confidence':confidence,'against_C':True,'against_H':True,'kind':'independent audit','error_category':category,'marked_in_H':False,'mathematical':math})
add('audit_b12_punct','b12','L14, punctuation after the object formula',',',',',r'\unsure{,|)}','Other')
add('audit_b12_map','b12','L15, map terminal',r'\longrightarrow',r'\to',r'\unsure{\longrightarrow|-}','Symbols and indices',True)
add('audit_b17_accent','b17','L20, accent in cloture','clôture','clôture',r'\unsure{clôture|cloture}')
add('audit_b20_abbrev','b20','Margin row1, abbreviated groupoid noun','groupoïde','groupoïde',r'\unsure{gr.-oïde|gr.-oïdes}','Abbreviations expanded, spelling modernised')
add('audit_b20_quotient','b20','Margin row4, adjective after topos','galoisien','galoisien','quotient',confidence='high')
add('audit_b20_punct','b20','Margin row4, punctuation after B expression',',',',',r'\unsure{,|)}','Other')
add('audit_b22_phrase','b22','Item3, words after E_K','au-dessus','au-dessus',r'\unsure{au-dessus|--- disons|--- dessus}')
for x in r['doubts']:
 if 'word before extension' in x['place']:x.update(reading=finals['c01'],alternatives=['une',"d'une",'des','cancellation state uncertain'],reason=ch['b02']['evidence'],confidence='low')
 if 'cancelled word before par' in x['place']:x.update(reading=ch['b18']['final'],alternatives=['comme','connexe','connexes'],reason=ch['b18']['evidence'],confidence='low')
 if 'relation in the whole pi' in x['place']:x.update(reading=ch['b19']['final'],alternatives=[r'\neq','=',r'\simeq'],reason=ch['b19']['evidence'],confidence='low')
for k,place,reading,alts in [
 ('b06','L7, word before topos',r'\unsure{ce|en}',['ce','en']),
 ('b12','L14, punctuation after object formula',r'\unsure{,|)}',[',',')']),
 ('b12','L15, map terminal',r'\unsure{\longrightarrow|-}',[r'\longrightarrow','-']),
 ('b17','L20, accent in cloture',r'\unsure{clôture|cloture}',['clôture','cloture']),
 ('b20','Margin row1, abbreviated noun',r'\unsure{gr.-oïde|gr.-oïdes}',['gr.-oïde','gr.-oïdes']),
 ('b20','Margin row3, word after bien',r'\unsure{plutôt|plutot}',['plutôt','plutot']),
 ('b20','Margin row4, punctuation after B expression',r'\unsure{,|)}',[',',')']),
 ('b22','Item3, phrase after E_K',r'\unsure{au-dessus|--- disons|--- dessus}',['au-dessus','dash disons','dash dessus'])]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':ch[k]['evidence']})
for x in r['diff_coverage']:
 if x.get('change_id') in mapping:
  cid=x['change_id'];x.update(final=finals[cid],reason=ch[mapping[cid]]['evidence'])
for x in r['inventory']:
 if x['kind']=='deletion' and 'comme' in x['first_words_or_objects']:x['first_words_or_objects']=r'\unsure{comme|connexe|connexes}'
r['notes'].append('Independent audit: all18 differing boxes and89 token spans personally inspected, including the complete five-line marginal note in a rotated view of the same rectangle. Eight boxes changed. The margin now preserves the abbreviated gr.-oïde(s), tentative plutôt/plutot, definite quotient and sous, plus punctuation uncertainty. The compressed phrase after E_K remains au-dessus / dash disons / dash dessus uncertain; no extra continuation is duplicated. Word, accent, cancellation and map-sign doubts are documented individually. No mathematical check was added.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
