"""Single-use main-reader decisions after personally inspecting every differing crop."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]; ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan021_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b01','The final e has a long low return and downward terminal hook, without a separate s body. The independent underline crosses the q descender. Retain singular Remarque and its underline.')
c('b02','An accent and initial e are clear. The crowded middle contains doubled c/v/r/i/d/b/s-like curves and tall crossings; the low run ends in several joined humps and a crossed tall stroke. Neither complete lexical reading is secure. The independent évidemment remains possible; its shorter évident alternative omits part of the visible middle run. Retain the three complete alternatives without assigning an old/live chronology.',r'\unsure{écrivant|établissant|évidemment}')
c('b03','There are two tall joined strokes sharing one horizontal cross-stroke. No independently separable low e and s sequence follows a single l. The final down-hook is a return, not a separate s. Retain the literal short form tt.')
c('b04','Two small s curves precede a short hyphen; g and p have distinct descenders. The final e ends in a long low return without another s body. Retain ss-groupe, singular, without expansion.')
c('b05','The small subscript has a curved upper lobe, inward waist and lower return. These strokes allow epsilon as well as calligraphic or cursive ordinary E; this sheet has no decisive contrasting alphabet form. The complete formula has pi-prime, two equals bars, braces,1 and the final point. Preserve the entire formula and broaden only the letter alternative.',r"$\operatorname{Centr}_{\unsure{\mathcal E|E|\varepsilon}}(\pi')=\{1\}$.")
c('b06','The word Si is clear. The following symbol has a small curved upper hook, curved diagonal and long looped lower foot. Repetition of that construction does not distinguish ordinary from calligraphic Z, so retain the local alternative.')
c('b07','The centralizer symbol repeats the curved upper hook and looped lower foot of b06, without a decisive alphabet contrast. The following pi is shorter than that symbol and has two short legs under an overhanging roof, with a curved right foot. Retain lowercase pi, intersection, equals and the complete (1).')
c('b08','The de has a looped d and low e return. The symbol again has the curved diagonal and long lower foot; there is no evidence resolving its alphabet, so retain Z/calligraphic Z.')
c('b09','Under the cancellation the c/o/n/t/enu run is visible, but the possible final e merges into the cancelling stroke. Retain contenue/contenu uncertainty and the following dans. In the live replacement, two dotted i strokes are followed by a separate open e loop; this supports finie rather than fini. The cancellation continues into le noy on the next baseline.',r'\deleted{\unsure{contenue|contenu} dans}\inserted{finie}')
c('b10','The long l loop and following e are clear. An oval o and long y descender survive, but the short n joins lie beneath the strike. Retain the short noy with its doubt, without expanding it or declaring every letter certain.')
c('b11','The raised d/e and dotted j descender are mostly visible, but the final a and accent area meet the leader, so déjà remains tentative as a whole. The baseline word has an initial small oval, tall rise and compressed low run with terminal hook; it does not securely distinguish alors, dans and donc. The comma is independent, followed by que, the same unresolved Z alphabet and est. The leader attaches the raised word before this baseline word.',r'\inserted{\unsure{déjà}} \unsure{alors|dans|donc}, que $\unsure{Z|\mathcal Z}$ est')
c('b12','The initial two joined low curves under the strike can be un or ou. The next cluster has a curved tall stroke, upright, low dark oval and small right down-stroke; the far-right heavily crossed cluster resembles a Z/3 form. Two cancellation lines merge with these traces. They do not distinguish the abbreviated él. reading from (1), followed by a Z-like symbol, nor establish an extra symbol as certain. Retain the full alternative extents under cancellation.',r'\deleted{\unsure{un|ou} \unsure{él.|$(1)$, $Z$|$(1)$, $\mathcal Z$}}')
c('b13','One closing parenthesis and one horizontal prose dash are visible. The difference between one typed hyphen and the edition’s three-hyphen dash is rendering alone; no extra point or repeated ink dash is supplied.')
c('b14','The larger symbol repeats the small centralizer subscript: curved upper lobe, angular inward waist and long lower return. Epsilon remains possible alongside both E alphabets; the local repeated form does not resolve them. The following par has its own p descender and compressed ar.',r'$\unsure{\mathcal E|E|\varepsilon}$ par')
c('b15','Both symbols share the curved construction already seen; a detached elevated upright is the prime of the first only. The intervening de is clear. Retain both alphabet alternatives and the first prime.')
c('b16','The thin lower-left2 has a curved top, descending oblique and foot, followed by a closed0. This is the small marginal20, distinct in location and pen weight from the large10 at the head; retain the margin wrapper.')
c('b17','Both Gammas have a stem and roof. In the left index both K letters have angular branches and only the first is barred; the subset is open right. Both right index Q letters have independent internal strokes, with only the first barred. Bracing around the alphabet macro changes no reading.')
c('b18','The tall pair has a left descending stem and looping return, with an oblique connection to a second tall stem and long lower foot. The top of that second stem meets the crop boundary, also in first crop c19. The outline permits joined th/Th or a single H-like form; the independent H cannot be securely excluded. Retain all three, with a separate point and numeral1.',r'\unsure{th.|Th.|H.}1')
c('b19','The large head number has a slanted entry and upright1, followed by a closed oval0. Both readings agree on10; retain the established manuscript-page wrapper.')
c('b20','The two-legged sign has short curved feet and an overhanging roof, matching the small inserted pair and the intersection pi rather than the taller capital forms on other leaves. Retain lowercase pi. Two horizontal bars crossed by an upright give not-equal; parentheses and1 are complete. The neq/ne difference is macro syntax alone.')
c('b22','Both readings give the same inserted words. The K has two separate angular limbs, Q has a separate internal stroke and tail, and the comma descends independently. The i.e. points are distinct. Bracing the Q macro changes no ink; retain the first encoding.')
c('b24','Both signs have two short legs with curved lower returns under overhanging roofs, matching b20 in construction. The first has a detached prime; the subset opens right. Retain the lowercase pi pair as the insertion before ouvert.')
c('b27','The numerals are an upright1 with entry and foot, then a curved-top2 with diagonal and foot. Between them is the short ou run; a separate comma follows. Math wrappers alone differ.')
c('b28','An upright1 with slanted entry and broad low foot is followed by a separate descending comma. There is no reading difference beyond math wrappers.')
c('b29','The inserted du has a looped d and low u. The following two short curved legs and roof match the local lowercase pi forms; the small separate1 sits below its baseline. The long curve below belongs to the insertion leader, not the formula. Retain du pi_1 and its attachment.')
(R/'documentation/149_scan021_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan021.tex';s=p.read_text()
for k in ['b02','b05','b11','b12','b14','b18']:
 assert first[k] in s,k;s=s.replace(first[k],ch[k]['final'])
s=s.replace(r'\deleted{contenue dans le',r'\deleted{\unsure{contenue|contenu} dans le')
p.write_text(s)
p=R/'reviews/149_scan021.json';r=json.loads(p.read_text())
mapping={'c02':'b02','c05':'b05','c07':'b11','c08':'b12','c10':'b14','c12':'b18'}
for x in r['changes']:
 if x['id'] in mapping:
  k=mapping[x['id']];x.update(final=ch[k]['final'],evidence=ch[k]['evidence'],crop=f'crops/149_scan021_second_{k}.png',confidence='low' if k in ['b02','b11','b12','b18'] else 'medium')
  b=next(z for z in r['audit_boxes'] if z['box']==k);x['box']=[b[t] for t in ['x0','y0','x1','y1']]
for x in r['decisions']:
 if x['id'] in ['M1018','M1023']:
  k='b05' if x['id']=='M1018' else 'b14';x.update(reading=r'\unsure{\mathcal E|E|\varepsilon}',evidence=ch[k]['evidence'],confidence='medium')
for x in r['doubts']:
 q=x['place']
 if q=='Line 2, overwritten verb':x.update(reading=ch['b02']['final'],alternatives=['écrivant','établissant','évidemment'],reason=ch['b02']['evidence'])
 if q in ['Line 3, E-like subscript','Line 11, group symbol after remplacer']:x.update(reading=r'\unsure{\mathcal E|E|\varepsilon}',alternatives=[r'\mathcal E','E',r'\varepsilon'],reason=ch['b05' if q.startswith('Line 3') else 'b14']['evidence'])
 if q=='Line 5, theorem abbreviation':x.update(reading=r'\unsure{th.|Th.|H.}',alternatives=['th.','Th.','H.'],confidence='low',reason=ch['b18']['evidence'])
 if q=='Line 7, word after déjà':x.update(reading=r'\unsure{alors|dans|donc}',alternatives=['alors','dans','donc'],confidence='low',reason=ch['b11']['evidence'])
 if q=='Line 9, cancelled abbreviation':x.update(place='Line 9, whole cancelled group',reading=ch['b12']['final'],alternatives=[r'un él.',r'ou (1), Z',r'ou (1), \mathcal Z'],reason=ch['b12']['evidence'])
r['doubts'].extend([{'place':'Line 6, end of cancelled word','reading':r'\unsure{contenue|contenu}','alternatives':['contenue','contenu'],'confidence':'low','reason':ch['b09']['evidence']},{'place':'Line 7, inserted word','reading':r'\unsure{déjà}','alternatives':['déjà'],'confidence':'low','reason':ch['b11']['evidence']}])
for x in r['inventory']:
 if x['element']=='w1':x['first_words_or_objects']=ch['b02']['final']
 if x['element']=='d2':x['first_words_or_objects']=r'\unsure{contenue|contenu} dans le \unsure{noy}'
 if x['element']=='i6':x['first_words_or_objects']=r'\unsure{déjà}'
 if x['element']=='d3':x['first_words_or_objects']=ch['b12']['final']
for x in r['diff_coverage']:
 if x.get('change_id') in mapping:x['reason']=ch[mapping[x['change_id']]]['evidence']
r['notes'][3]='The crowded line-2 verb retains écrivant / établissant / évidemment. Doubled strokes do not establish an old/live order. The shorter independent évident reading does not account for the full low run.'
r['notes'][6]='Live finie replaces the cancelled phrase whose opening ending remains contenue/contenu, followed by dans le and tentative noy. The raised tentative déjà attaches before the baseline alors/dans/donc; the comma follows the baseline word.'
r['notes'][7]='Cancelled et is replaced by prouvons que. The later cancellation before engendrée retains un/ou and alternatives for the following él. versus (1), Z-like group; no certain extra symbol is supplied. Added du pi_1 attaches between au cas and d’une courbe algébrique. The insertion attachments and separately cancelled passages were inspected.'
r['notes'].append('Independent audit: all25 differing boxes were personally inspected. Seven boxes changed by broadening local alternatives or qualifying a reading. Clear live finie, all short pi forms, the singular heading and ss-groupe, numeral readings and insertion attachments were retained. The E-like forms now allow epsilon as well as both E alphabets. No mathematical proof check was added.')
for x in r['hand']:
 if x['habit'].startswith('The E-like'):x['misread']='The repeated curved shape permits calligraphic E, cursive ordinary E and epsilon; this sheet alone does not settle the alphabet.'
 if x['habit'].startswith('Tall joined'):x['misread']='th., Th. and the independent H. reading remain localized alternatives; the tall joined outline does not resolve them.'
 if x['habit'].startswith('Cancellation and'):x['consistency']='le and the y descender survive one cancellation; in the later group even un/ou and the extent of the following letters remain uncertain.'
for x in r['notation']:
 for key in ['written','rendering']:
  x[key]=x[key].replace(r'\unsure{\mathcal E|E}',r'\unsure{\mathcal E|E|\varepsilon}')
 if x['written'].startswith(r'\operatorname{Centr}'):x['evidence']=ch['b05']['evidence']
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
