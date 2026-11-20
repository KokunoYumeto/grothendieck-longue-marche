"""Main-reader adjudication of scan 002, after personal inspection of cited crops."""
from pathlib import Path
import json,copy
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
for letter in 'ABC':
    if not (R/'readers/scan002'/letter/'report.json').exists():raise SystemExit('All three completed reports required before committing')
reports={l:json.loads((R/'readers/scan002'/l/'report.json').read_text()) for l in 'ABC'}
base=reports['C'];cs=[]
cropmap={c['id']:str(Path(c['path']).relative_to(R)) for c in base['crops']}
for ix,c in enumerate(base['changes']):
    if ix==10:continue # checked mixed origin, no reading/doubt difference
    x=copy.deepcopy(c);x['final']=x.pop('reading');x['crops']=[cropmap[k] for k in x.pop('crop_ids')]
    x['marked_in_H']='yes' if x['marked_in_H'] else 'no'
    # All three complete readings have been compared; explicit exceptions below.
    x['readers']={'A':x['final'],'B':x['final'],'C':x['final']}
    if ix in [0,1,13,19,24,35,39]:x['against_c']=True
    if ix in [8,13,14,15,16,17,21,22]:
        x['against_h']=True;x['change_type']='uncertainty marking'
    if ix==0:x['change_type']='uncertainty resolved'
    if ix==1:x['change_type']='uncertainty resolved'
    if ix==2:
        x['readers']['A']=r'\deleted{x}X'
        x['scan_shows']+=' Main adjudication retains x|Y: the smaller crossed impression and fork cannot securely exclude Y; A’s unqualified x overstates what survives.'
    if ix==4:x['crops']=['crops/scan002/21_product_CxC.png'];x['scan_shows']='A serifed lowercase x rests on the same baseline as the two C capitals. This confirms the baseline typewriter x, not a centred multiplication glyph.'
    if ix==7:
        x['readers']['A']=r'\unsure{\handwritten{s}|\deleted{s}}'
        x['scan_shows']+=' Main adjudication follows B and C: the thick strokes form the two lobes of s; no independent strike through the letter is distinguishable. The status is supported, at medium confidence.'
    if ix==12:x['crops']=['crops/scan002/22_homotopie_quotes.png'];x['scan_shows']='Two separate high vertical quotation strokes appear at both ends of à homotopie près; there are no angle-shaped guillemets.'
    if ix==19:
        x['readers']['B']=r'\unsure{=|\phantom{=}}'
        x['scan_shows']+=' Main adjudication follows A and C: put the absence of a visible sign first; retain = only as a possible lost mark, never as established ink.'
    if ix in range(24,29):
        x['readers']={'A':r'\unsure{G|\mathbb{G}|E|K}' if ix==24 else 'G','B':r'\unsure{\mathbb{G}|G|K|E}' if ix==24 else r'\mathbb{G}','C':r'\unsure{G|E|K}' if ix==24 else 'G'}
        x['final']=r'\unsure{\mathbb{G}|G|E|K}' if ix==24 else r'\mathbb{G}'
        x['against_c']=ix==24
        x['scan_shows']='The repeated typewriter composite has a heavy open-right G-like curve, horizontal upper/lower bars and an extra diagonal/internal stroke. All five impressions were inspected separately. The final retains C’s double-struck G as first candidate under the supplied alphabet convention, while explicitly preserving plain G, E and K as alternatives. The ink does not decide identity or whether the extra impression is deliberate doubling or correction; A/C’s plain G is not demonstrably preferable. Only the first occurrence carries the recurring doubt.'
    if ix in [29,30]:
        x['final']='qui' if ix==29 else 'lui'
        x['readers']={'A':x['final'],'B':x['final'],'C':c['reading']}
        x['against_c']=True;x['confidence']='medium';x['change_type']='uncertainty resolved'
        x['scan_shows']=('The q loop and long descender are followed by a joined u and a separate i stroke/dot; the letters survive above and below the cancellation. Main adjudication follows A and B: qui.' if ix==29 else 'The tall loop of l is followed by a low u and short i with a detached dot, still visible through the crossing line. Main adjudication follows A and B: lui.')
    if ix==34:
        x['crops']=['crops/scan002/23_cancelled_Exemple2.png'];x['scan_shows']='The typed word Exemple is readable under several diagonal cancelling strokes; its original underline remains visible. H’s editorial note gives the same word/state, so it is not counted as a textual omission.'
    if ix==35:x['change_type']='uncertainty resolved'
    if ix==36:
        x['crops']=['crops/scan002/24_cancelled_Exemple3.png'];x['scan_shows']='The entire typed and underlined Exemple is cancelled before the live 3. H’s editorial note gives the same word/state, so it is not counted as a textual omission.'
    if ix==37:x['consequential']='Restore H’s omitted handwritten subscript is on Hom(A,A), restricting the morphisms in this groupoid example to isomorphisms.'
    if ix==39:
        x['c']=r"l\deleted{o}'opération";x['final']=r"l\deleted{o}\handwritten{'}opération"
        x['readers']={'A':x['c'],'B':x['c'],'C':x['final']}
        x['scan_shows']+=' Main adjudication follows C on the apostrophe’s handwritten status: its broad irregular pen stroke differs from the adjacent typewriter outlines.'
    cs.append(x)
cs.append({'place':'Left margin: attachment arrow','c':r'\(\nearrow\)','h':'Arrow described in an editorial note, not drawn','final':r'\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->,line width=.6pt] (0,0)--(.4,.3);\end{tikzpicture}}','scan_shows':'A short oblique pen shaft rises rightward from above the note to an angular filled arrowhead. A and B reproduce it in TikZ; C uses the nearrow glyph. Main uses TikZ to preserve it as a drawing. The direction agrees with witness C, so that rendering conversion is not counted as a reading change against C.','confidence':'high','kind':'drawing or diagram','marked_in_H':'no','against_c':False,'against_h':True,'crops':[cropmap['09_margin_note']],'readers':{'A':'TikZ arrow up-right','B':'TikZ arrow up-right','C':r'\nearrow'}})
text=(R/'readers/scan002/C/reading.tex').read_text()
text=r'\cotefile{103}'+'\n'+text
text=text.replace(r'\(\nearrow\)',r'\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->,line width=.6pt] (0,0)--(.4,.3);\end{tikzpicture}}')
text=text.replace(r'\unsure{G|E|K}',r'\unsure{\mathbb{G}|G|E|K}')
text=text.replace('points de $G$','points de $\\mathbb{G}$').replace('composition de $G$','composition de $\\mathbb{G}$').replace('Lorsque $G$','Lorsque $\\mathbb{G}$')
text=text.replace(r"\unsure{qui|qu'} \unsure{lui|les}",'qui lui')
unresolved=copy.deepcopy(base['unresolved'])
unresolved=[u for u in unresolved if not ('cancelled' in u['place'].lower() and u['reading'] in ['qui','lui'])]
for u in unresolved:
    if isinstance(u.get('alternatives'),list):u['alternatives']='; '.join(u['alternatives'])
    if any(w in u['place'].lower() for w in ['hopf','variante','recurring capital']):
        u['reading']=r'\mathbb{G}';u['alternatives']=r'G; E; K';u['evidence']='Composite overstruck capital; all five impressions agree in shape but do not decide alphabet/underletter. See changes and notation.'
inv=copy.deepcopy(reports['A']['inventory'])
if not any(i['kind']=='drawing' for i in inv):inv.append({'sheet_kind':'typescript','hand':'his hand (attribution tentative)','element':'002.pointer','kind':'drawing','position':'left margin above note, pointing up-right','first_words_or_objects':'attachment arrow','transcribed':'yes'})
for i in inv:i['sheet_kind']='typescript'
notes=[
'[S002.N1] The page is the opening typescript sheet, numbered 1, of “Esquisse d’une théorie des Gr-Catégories”, with byline “par Mme Hoang Xuan Sinh”. Another hand records “9/74” and “Envoyé par Grothendieck” at upper right. The lower-left 1 is an archive number and remains a TeX comment.',
'[S002.N2] It defines the (Gr)-categories under discussion by an associative and unital binary operation, with a handwritten insertion requiring a groupoid and invertible objects. It gives loop/Hopf-space, torsor/invertible-module, and equivalence-functor examples; the last example continues on the next sheet. These are reports of the page’s assertions, not independent proofs of the examples. No explicit “à vérifier” or equivalent pending-check wording occurs on this sheet.',
'[S002.N3] The visible handwritten is beneath Hom(A,A) matters to the groupoid condition. A limited check confirms its role: in the category of abelian groups, the identity functor is an equivalence but its zero natural endomorphism is not an isomorphism. Thus allowing all natural transformations would not give a groupoid in general. This check supports revisiting the subscript; the crop, not the argument, decides its transcription. No general structure theorem is proved here.',
'[S002.N4] The enlarged margin shows Ω with a definite raised 1. The equality before Ω is outside/at the clipped edge: the final first candidate is no visible sign, with equality retained only as an uncertain alternative. The repeated overstruck Hopf-space capital is not settled: double-struck G, plain G, E and K remain recorded. Neither the mathematical expectation nor the witnesses resolves that alphabet.',
'[S002.N5] C’s title-underletter, crowded intéressons, cancelled comme, and the first two cancelled words qui lui were resolved on the crops. The continuation after même remains physically unreadable. The marginal note’s clipped beginnings are retained with doubt; no missing initial is supplied unmarked.'
]
notation=copy.deepcopy(base['notation'])
for x in notation:
    if 'Hopf' in x.get('sign','') or 'Variante' in x.get('place',''):
        x['latex']=r'\unsure{\mathbb{G}|G|E|K} at first occurrence; \mathbb{G} thereafter';x['ink']='Heavy overstruck composite, open-right G-like body plus extra internal strokes; alphabet and underletter unresolved.'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d={'scan':2,'folder':'H103-01','filename':'H103-01_103_scan002.tex','brief':'brief_v01.md','changes':cs,'unresolved':unresolved,'inventory':inv,'notation':notation,'abbreviations':base['abbreviations'],'notes':notes,'check_events':[
 {'statement_id':'S002.N2.groupoid_requirement','date':now,'who':'GPT-6 Astra Pro; effort not exposed; root scan002 adjudication','type':'carried as background without fault found','outcome':'The handwritten groupoid requirement is used as the premise of S002.N3; no independent proof of all examples is claimed.'},
 {'statement_id':'S002.N3.role_of_is','date':now,'who':'GPT-6 Astra Pro; effort not exposed; root scan002 adjudication','type':'targeted proof check','outcome':'For A=Ab, the zero natural endomorphism of the identity equivalence is not invertible. Hence all natural transformations between equivalence functors need not form a groupoid; restricting morphisms to isomorphisms is necessary in this example. The visible is was independently read in the crop.'}
], 'additional_main_crops':[cropmap['07_pointed_insertion'],cropmap['16_units_sheaf']]}
for row in d['changes']:
    if row['place'] in ['Example 1 heading: live added s','Example 2 heading: cancelled Exemple','Example 3 heading: cancelled Exemple']:
        row['marked_in_H']='no'
(R/'decisions/scan002.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'pages'/d['filename']).write_text(text)
print('Scan 002 adjudication written; rebuild deliverables and append completion before proceeding.')
