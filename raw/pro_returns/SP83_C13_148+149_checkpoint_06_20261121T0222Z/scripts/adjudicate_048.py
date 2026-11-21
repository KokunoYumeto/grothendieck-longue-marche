"""Main-reader crop decisions; the independent TSV is never edited."""
from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan048'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E={
'B02':'The lowered star sits beneath the S/T group; the established S-star category convention is retained. The old acronym has visible M and D under diagonal hatching; the initial upright with a possible middle bar is F under uncertainty, without confidently expanding it to Gamma. The displayed-arrow and font wrappers do not alter these readings.',
'B03':'The added tuple is linked between objet and de and contains X, tilde-Sigma, R. The only difference is braces around the tilde argument.',
'B04':'The overwritten old origin glyph remains unrecoverable beyond a tentative g. The small added oval has a rightward upper extension, preserving o|sigma. Before gamma the separate crossed form is bracket-like; it is retained as an uncertain closing parenthesis rather than replacing it by an unqualified question mark. All six tuple entries and the inserted MD are kept.',
'B05':'The tall crossed curve after X still allows a closing parenthesis or comma. The arrow points left and carries a tilde-like equivalence mark. Both Sigma letters have upper tildes. The first explicit alternatives retain more surviving ink than the second question-mark placeholder.',
'B06':'The old paired glyph and the words beneath the membership insertion remain obscured; the first candidate readings are retained under uncertainty. A small X is visible below rive, so the subscript is kept. The added relation has wavy upper and straight lower strokes. The word soumis has the initial s, low oum and final is; the full condition remains as first read.',
'B07':'The word before omega shows a low initial a, a tall l, rounded o, short r and final s: alors. The uncertainty is resolved on this fresh crop. Following omega, the four-letter group has an initial low s, rounded o, dotted i and tall t, supporting soit rather than est. The remaining boundary formula and prose agree.',
'B08':"After the opening parenthesis the q-descender, connected uan and tall d read quand, followed by separate on a. The long last word has a g-descender and final r, d’échanger. The next line shows sinon, i.e. si and on pose. The second reading’s perdons/bien sûr alternatives do not fit these strokes.",
'B09':'The new label is a compact oval o rather than a partial derivative. The overdrawn upper cluster remains uncertain. At the lower left a distinct crossed formula has two R-like forms and an intervening relation; it must be retained before contient cette rive, though the exact relation stays doubtful. The second reading omitted this cancellation.',
'B10':'Gamma precedes S with a colon; a rightward map reaches double-stroked N, and a vertical equality aligns S over pi_0(X minus tilde-Sigma). The difference is diagram column allocation and tilde bracing only.',
'B11':'The short initial stroke is the reduced a followed by two descending/looped p forms, then lication: application. It is not a separate dash plus fonction. The last noun ends with a compact nts cluster, without a distinct intervening e; composants is retained as written. Xi has a small lowered i, and genre alone is underlined.',
'B12':'The upper short-shouldered r replaces a cancelled descending old glyph, still tentatively rho. Sigma has a visible high curved tilde; the box touches some upper tips but the accent survives. The map and element-map arrows, intersection, cardinality and terminal point agree. The insertion wrapper is retained for the replacement.',
'B14':'The article has a final small low e turn after un; une surjectif is retained despite its grammatical disagreement. Both pi indices and the subsequent c’est un remain unchanged.',
'B15':'The underline starts beneath the i of isomorphisme, to the right of the initial 0 and its hyphen; its scope is corrected to that word. The crossed curved mark after the word still permits parenthesis or question-like form, so that uncertainty is not resolved.',
'B16':'A separate tall L and low following vowel are visible to the left of the large P. The first proposed Prop. alone omitted this left group. The two long cancellation strokes obscure the following word: the revised candidates Le Prop.|La preuve retain the visible initial group without claiming the full cancelled wording is settled. The colon is separate and clear.',
'B17':'The heading has the final s turn of Remarques. Its underline ends in a thick terminal nub below the baseline; there is no separate point after the word, so the inferred period is removed. Somme has no extra final s, directe is raised and underlined, and the lower cancelled acronym has two horizontal bars on F rather than Gamma. The upper replacement reads Gra bipond. The clipped category top does not justify changing the independently established category notation.',
'B18':'The lower-left annotation is an angular open 4 and a barred 7. It is a folio number, kept under mspage; the independent margin wrapper changes no numeral.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={'B07':[(r'\unsure{alors|donc}','alors')],'B15':[(r'\uline{0-isomorphisme}',r'0-\uline{isomorphisme}')],'B16':[(r'\unsure{Prop.|La preuve}',r'\unsure{Le Prop.|La preuve}')],'B17':[(r'\uline{Remarques}.',r'\uline{Remarques}') ]}
pp=R/'pages'/f'{p}.tex';page=pp.read_text()
for b,rs in repls.items():
 s=C[b]['first']
 for a,z in rs:
  assert a in s and a in page,(b,a)
  s=s.replace(a,z);page=page.replace(a,z)
 D[b].update(choice='reading',reading=s)
pp.write_text(page)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text());by={x['id']:x for x in r['changes']}
by[p+'-17'].update(final=r'alors $\omega$',confidence='high',evidence=E['B07'],crop=f'crops/{p}_second_B07.png',box=[502,810,1575,960])
by[p+'-41'].update(final=r'\deleted{\unsure{Le Prop.|La preuve}} :',diff_c=True,evidence=E['B16'],crop=f'crops/{p}_second_B16.png',box=[331,1940,665,2044])
r['doubts']=[x for x in r['doubts'] if x['place']!='after C in pi_0(boundary X)']
for x in r['doubts']:
 if x['place']=='cancelled heading before Remarques':x.update(reading=r'\deleted{\unsure{Le Prop.|La preuve}}',alternatives='Le Prop.; La preuve; second word remains unrecovered',reason=E['B16'])
for i,place,c,h,final,b,box in [
 (46,'Heading Remarques, terminal punctuation',r'\uline{Remarques}.',r'\emph{Remarques.}',r'\uline{Remarques}','B17',[315,2015,1640,2300]),
 (47,'Functors paragraph, extent of underline',r'\uline{0-isomorphisme}',r'\uncertain{$0$}-isomorphisme',r'0-\uline{isomorphisme}','B15',[345,1782,1630,1920])]:
 r['changes'].append(dict(id=f'{p}-{i}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind='text not on the page' if i==46 else 'other',error_kind='Text that is not on the page' if i==46 else 'Other',evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=box,confidence='high',marked_in_h=i==47,consequential=False))
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace(r'\unsure{Prop.|La preuve}',r'\unsure{Le Prop.|La preuve}').replace(r'\uline{0-isomorphisme}',r'0-\uline{isomorphisme}')
r['notes'].append(dict(id=p+'-N-audit',text='The independent audit resolves alors, retains the literal une surjectif, restricts the underline to isomorphisme, and removes an unsupported period after Remarques. The crossed heading visibly has a separate L-vowel group before P; Le Prop.|La preuve remains explicitly uncertain. No mathematical claim was independently checked during these visual decisions.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
