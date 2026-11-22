from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan085';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
rel=r'\unsure{=|\stackrel{?}{=}}'
oldbr=r'\underbrace{T_{\bar J\setminus J}}_{\displaystyle\bigcup_{i\in\bar J\setminus J}T_i}'
br=r'''\underset{\displaystyle\bigcup_{i\in\bar J-J}T_i}{\begin{tikzpicture}[baseline=(term.base)]
\node[inner sep=1pt] (term) {$T_{\bar J\setminus J}$};
\draw ([yshift=.5pt]term.south west)--([yshift=-1.5pt]term.south west)--([yshift=-1.5pt]term.south east)--([yshift=.5pt]term.south east);
\end{tikzpicture}}'''
# Explicit short return curls at the two right endpoints, in the diagram matrix.
oldarr=r'\Sigma_{ij}\arrow[ur]\arrow[dr]'
arr=r'''\Sigma_{ij}\arrow[ur,no head,to path={(\tikztostart.east)--([xshift=-3pt]\tikztotarget.west).. controls ([xshift=-1pt,yshift=1pt]\tikztotarget.west) and ([xshift=-1pt,yshift=-1pt]\tikztotarget.west)..([xshift=-3pt,yshift=-1pt]\tikztotarget.west)\tikztonodes}]\arrow[dr,no head,to path={(\tikztostart.east)--([xshift=-3pt]\tikztotarget.west).. controls ([xshift=-1pt,yshift=-1pt]\tikztotarget.west) and ([xshift=-1pt,yshift=1pt]\tikztotarget.west)..([xshift=-3pt,yshift=1pt]\tikztotarget.west)\tikztonodes}]'''
reps=[(r'\Sigma_{i_0\ldots i_n}',r'\Sigma_{i_0-i_n}'),(r'\Sigma_d$. On prend des',r'\Sigma_d$ etc. On prend des'),
 (r'X_J^*\setminus X_J^*\cap',r'X_J^*\unsure{\setminus|>}X_J^*\cap'),
 (r'X_j^*=X_{\bar J}^*',r'X_j^*'+rel+r'X_J^*'),('On a même, sauf erreur','On trouve, sauf erreur'),
 (r'(s_{ij},b_{ij}:',r'(s_j,b_{ij}:'),(oldarr,arr),
 (r"\unsure{l'on déduit} des",r"\unsure{l'on déduit} \unsure{aux|des}"),
 (r')$ avec $j,h\in I$',r')$ \unsure{avec|où} $\unsure{\forall|j,}h\in I$'),
 (r"(\text{équivalence d'homotopie})",r"\substack{\text{(équivalence d'homo-}\\\text{topie)}}"),
 (oldbr,br),(r'\unsure{ayant|avec}',r'\unsure{avec|ayant}')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for old,new in reps:assert s.count(old)==1,(old,s.count(old));s=s.replace(old,new)
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']}
def upd(ident,box,**kw):ch[ident].update(crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],**kw)
upd('C06','B02',final=ch['C06']['final'].replace(r'i_0\ldots i_n','i_0-i_n'),against_C=True,evidence=ch['C06']['evidence']+' The continuation between i0 and in is one unbroken horizontal stroke, not dots.')
upd('C12','B02',final='etc. On prend des',against_C=True,evidence='After Sigma_d the small e/t/c sequence and its stop are visible before On on the next slanted line. The latter continues with a p descender, low r/e/n/d and des. The independent reading recovered the omitted etc.; its longer Dans ce point de vue would require letters absent from this line.')
upd('C18','B03',final=ch['C18']['final'].replace(r'X_J^*\setminus X_J^*',r'X_J^*\unsure{\setminus|>}X_J^*'))
# The earlier complete resolution of the crowded relation is withdrawn; certainty-only is in doubts.
r['changes']=[x for x in r['changes'] if x['id']!='C28']
upd('C29','B05',final=r'X_J^*)$')
upd('C32','B07',final='On trouve, sauf erreur',evidence='After On there is one connected word: a tall crossed initial t, low r/o/u/v joins and a terminal e. There is no separate a followed by two m groups. The alleged accent belongs to the crossing diagonal marginal text. The following comma, sauf erreur and blank after erreur are clear.',confidence='high',same_as_C_first_reading=False)
upd('C36','B09',final=r"est muni d'une stratification de type $J$, que \unsure{l'on déduit} \unsure{aux|des}",evidence='The long stratification has the f descender and t stems, and type J with its comma is plain. Que is readable before the crossed group; the latter still cannot be separated securely into letters. Before the tuple there is a low oval, low joins and an angular final return, favouring aux; no clear d ascender can be certified. Keep a local aux/des doubt instead of the earlier certain des.')
upd('C40','B09',final=r'\unsure{avec|où}',confidence='low',evidence='The short group after the tuple has a small low opening and joined strokes with a separate upper mark. It does not securely distinguish avec from the blind où; the earlier certainty is withdrawn.')
upd('C41','B09',final=r'\unsure{\forall|j,}h\in I',confidence='medium',evidence='The second letter is an h with tall stem and one shoulder; the final I has two transverse bars. The opening sign has a long right stem, a lower angled left arm and a short transverse return, favouring forall, but the clipped left edge prevents excluding j with punctuation. There is no secure isolated j-dot or comma. Retain the two readings locally.')
upd('C42','B09',final=r'\unsure{\forall|j,}h\in I$')
upd('C48','B12',final=r'\unsure{avec|ayant}',evidence='The low a/v/e/c-like run now favours avec; the blind reading also chose it. The central retrace remains too dense to certify every join or exclude ayant. Reverse the preferred order only, and retain the doubt.',confidence='low')
newrows=[
 ('C50','Left marginal X note, final X subscript',r'X_{\bar J}^*',r'X_{\overline J}^*',r'X_J^*','B05','The final J has its ordinary upper arm but no separate overbar. In the same line the union-index bar over J is distinctly separate above its upper arm. Keep the final unbarred J, even though the preceding union has bar J.','misread symbol or index','1 symbols/indices',True),
 ('C51','(72), first map subscript',r's_{ij}',r's_{ij}',r's_j','B08','The first s is followed by one dot and one descending j body. There is no separate short i body or second dot, unlike the two-dot ij beside the following b and in the diagram source.','misread symbol or index','1 symbols/indices',True),
 ('C52','(72), two right arrow endpoints',r'\Sigma_{ij}\to\Sigma_i,\ \Sigma_{ij}\to\Sigma_j',r'\Sigma_{ij}\to\Sigma_i,\ \Sigma_{ij}\to\Sigma_j',arr,'B08','Both short shafts end in compact return curls, the lower one closing a tiny loop. They do not have two clean divergent chevron branches like the limit arrow in this same formula. The matrix objects and directions are preserved, with explicit return paths replacing generic arrowheads.','drawing or diagram','4 drawings/diagrams',False),
 ('C53','(73), written division of homotopie',"équivalence d'homotopie","équivalence d'homotopie",r"\substack{\text{(équivalence d'homo-}\\\text{topie)}}",'B11','The upper line ends in homo followed by a short independent horizontal hyphen at the right edge. Topie and the closing parenthesis are on the lower line. Preserve that written hyphen.','omission','3 omissions',False),
 ('C54','(74), lower bracket on T',r'\underbrace{T_{\bar J\setminus J}}',r'T_{\overline J\smallsetminus J}',br,'B12','The annotation line is flat across the base with short upward ends; it has no central cusp. Encode this square-ended lower bracket explicitly and keep the union beneath it.','drawing or diagram','4 drawings/diagrams',False),
 ('C55','(74), union index below the bracket',r'i\in\bar J\setminus J',r'i\in\overline J\smallsetminus J',r'i\in\bar J-J','B12','In the union index the separator is a horizontal short dash, unlike the descending slash in the T subscript immediately above.','misread symbol or index','1 symbols/indices',False)]
for ident,place,C,H,final,box,why,kind,ek,conseq in newrows:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high' if ident!='C52' else 'medium',kind=kind,error_kind=ek,against_C=True,against_H=True,consequential=conseq,marked_in_H=False,phase='blind audit'))
for d in r['decisions']:
 if d['id']=='M0690':d.update(decision='undecided',reading=rel,ink='Two horizontal equals bars are clear, but the adjacent tall curled overtrace may be a question/correction mark. Its relation to the equals cannot be certified; no third horizontal bar is visible.',crop=f'crops/{pg}_blind_B05.png',box=b['B05']['coordinates'],confidence='medium')
 if d['id']=='M0691':d.update(decision='other',reading='trouve',ink=ch['C32']['evidence'],crop=f'crops/{pg}_blind_B07.png',box=b['B07']['coordinates'])
 if d['id']=='M0692':d['ink']='Que is readable before the group; crossing main-line letters obscure the proposed l’on déduit. The following short word is itself now marked aux/des. The middle group remains unresolved.'
 if d['id']=='M0693':d.update(reading=r'\unsure{avec|ayant}',ink=ch['C48']['evidence'])
for d in r['doubts']:
 if 'M0692' in d['place']:d['reason']='Crossing main-line ink obscures the group after que; the short word before the tuple is also not secure.'
 if 'M0693' in d['place']:d.update(reading=r'\unsure{avec|ayant}',alternatives=['avec','ayant'],reason=ch['C48']['evidence'])
for place,reading,alts,box,why in [
 ('(70), first difference-shaped sign',r'\unsure{\setminus|>}',['set difference stroke','greater-than wedge'],'B03','Two oblique arms meet in a wedge-like outline. The expected set difference does not settle whether both arms are intentional; retain the local alternative.'),
 ('Left X note, relation M0690',rel,['equals','equals with question/correction mark'],'B05','Two equals bars are separate from a tall curled overtrace. The overtrace is not a third equals bar, but may qualify the relation; the former complete resolution is withdrawn.'),
 ('Left NB at (72), word before tuple',r'\unsure{aux|des}',['aux','des'],'B09',ch['C36']['evidence']),
 ('Left NB at (72), word after tuple',r'\unsure{avec|où}',['avec','où'],'B09',ch['C40']['evidence']),
 ('Left NB at (72), opening final condition sign',r'\unsure{\forall|j,}',['forall','j with comma'],'B09',ch['C41']['evidence'])]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium' if box=='B05' else 'low',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
for x in r['inventory']:
 if x['element']=='E05':x['first_words_or_objects']=x['first_words_or_objects'].replace(r'X_J^*\setminus',r'X_J^*\unsure{\setminus|>}')
 if x['element']=='E15':x['first_words_or_objects']='On trouve, sauf erreur'
 if x['element']=='E18':x['first_words_or_objects']='Sigma_ij to Sigma_i and Sigma_j, short shafts with terminal curls'
 if x['element']=='E21':x['first_words_or_objects']="(équivalence d'homo- / topie)"
 if x['element']=='E24':x['first_words_or_objects']=r'\bigcup_{i\in\bar J-J}T_i'
r['notes']+='\n### Blind reading corrections\n\nThe opening diagonal note has a single dash in the long Sigma index and includes etc. after the limit expression. The introduction to (72) reads On trouve, sauf erreur; the earlier On a même was not sustained by the connected strokes. The first map index in (72) is the literal s_j, beside b_ij. The final X in the marginal X_J identity has an unbarred J, unlike the barred J in the preceding union; that literal asymmetry is retained. Its crowded relation is now uncertain, and no mathematical repair is made. The two small diagram shafts have terminal return curls. Formula (73) writes homo- at the end of its upper line and topie below. Formula (74) has a square-ended lower bracket and a horizontal minus in the union bound beneath it; its main T bound uses a slash. The two tips under its last limit remain distinct. Several small words and a quantifier-like marginal sign remain explicitly uncertain. These are observations of ink, not new proofs of the claimed identities.\n'
r['hand_log'].append(dict(habit='Crossing slanted marginal ink can imitate an accent or extra word in a horizontal line.',places='Introduction to72 and adjacent NB',scope='Separated the different baseline directions on the blind crop.',witness_errors='C’s a même is corrected to trouve; the apparent high accent belongs to the diagonal note.'))
def put(box,evidence,changed=False):
 f=b[box]['first']
 for old,new in reps:f=f.replace(old,new)
 notes[box]=dict(viewed=True,evidence=evidence)
 if changed:notes[box].update(changed=True,final=f)
put('B01','The underlined16 stands on the title line immediately before the Sigma terms. It is a section heading, not an independent authorial page number. The et and final stop remain; the mspage wrapper of the blind reading does not change the glyphs.')
put('B02','All rotated panels were viewed. The long index has one continuous dash; etc. is visible after Sigma_d. On prend des has a descending p and low following joins, rather than the longer Dans ce point de vue. Éclatés and orientés are two distinct words with closing quotation ticks. The limit has a plain underline. Non is live; the following small Sigma is certainly crossed, with its residual identity still doubtful. Idem pour remains uncertain. The final Sigma has a separate dot, and three separate terminal dots remain visible.',True)
put('B03','The complete70 crop shows the separate live and crossed upright pairs. Keep the additional live Vert beside NB and do not turn the crossed upright relation horizontal. The first difference-shaped operator has a wedge-like second arm, so it is now locally unsure between setminus and greater-than. The lower difference stroke is a single oblique. Both old superscript identities remain doubtful; all remaining union bounds and live/crossed states agree.',True)
put('B04','The bar over J, idéal engendré par J, existential condition, inequality and closing brace agree. The right NB has no underline. Dollar/math delimiter and thin-space differences are representation only.')
put('B05','On a posé and the parenthesis are clear. The union index has a distinct overbar, whereas the final J does not. Two equals bars are visible, but their adjacent dense vertical curl may qualify the relation; restore a local doubt instead of treating the whole crowded relation as settled. No third equals bar or separate final stop is visible.',True)
put('B06','Both phi signs, the three initial identities, the braced second row and71 agree. The alternative array and aligned forms do not alter visible ink.')
put('B07',ch['C32']['evidence'],True)
put('B08','The first map has only the j dot/body; the following b has the two separate ij dots and bodies. Both arrow shafts terminate in short return curls, the lower with a tiny loop, so explicit matrix paths replace generic chevrons. The canceled b-like character stays doubtful. Both limit operators retain their different endpoints, and there is only one visible closing parenthesis. The lower canceled Par suite fragment is overlap with B10.',True)
put('B09','The entire exact region and three rotated display panels were read. Stratification is traceable with f/t stems and is not left wholly doubtful. Que is clear, but the next group remains crossed; the low word before the tuple now has aux/des alternatives. All three second indices have h shoulders, not k arms. The group after the tuple does not securely decide avec versus où. The final opening sign has a quantifier-like angled arm and transverse return, but its left edge is clipped; retain forall/j-comma alternatives before the clear h and I. No final stop is visible.',True)
put('B10','Par suite is traceable beneath the strike. The following tall form has a left loop consistent with d, and the final low wave can be un, but the apostrophe and joins remain obscured. Keep uncertain d’un; a clean isolated perpendicular/L plus wholly unreadable word is not better supported.')
put('B11','The left shaft curls upward into an unmistakable hook; the right end is pointed. Tilde lies above the shaft, with h higher. The word at right is physically divided homo- / topie with a separate hyphen, now restored.',True)
put('B12','The complete74 crop shows a flat lower bracket with upturned ends, not a cusp brace. The bound under it has a horizontal dash, whereas the T subscript has a slash. The image target is capital J; both union conditions agree. Two separate tips are visible on the final lower limit arrow, so keep the double head. The crowded word after d favours avec but does not resolve all joins; retain avec/ayant. On pose at the upper edge overlaps the preceding prose.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('085: all12 differing boxes observed; eight changed boxes.')
