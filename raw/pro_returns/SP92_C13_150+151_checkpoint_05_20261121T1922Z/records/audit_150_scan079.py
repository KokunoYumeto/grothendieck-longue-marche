from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan079'
p=W/'pages'/f'{pg}.tex';s=p.read_text();rpath=W/'records'/f'{pg}.json';r=json.loads(rpath.read_text())
comp=json.loads((W/'second'/f'{pg}_comparison.json').read_text());boxes={x['box']:x for x in comp['results']}
index=r'\unsure{i|\deleted{x}\inserted{i}}'
s=s.replace(r'i.e. $i\in J$',r'i.e. $'+index+r'\in J$',1)
s=s.replace(r'V_{j_0\ldots j_n}',r'V_{j_0\mathord{-}\mathord{-}j_n}')
s=s.replace(r'j_0\ldots j_n\in J',r'j_0\unsure{\ast|\ne}\mathord{-}j_n\in J')
s=s.replace(r'j_0<j_1<\ldots<j_n',r'j_0<j_1<\mathord{-}\mathord{-}<j_n')
s=s.replace(r'V_{i_0\ldots i_n}',r'V_{i_0\mathord{-}\mathord{-}i_n}')
s=s.replace(r'\unsure{\varinjlim|\uline{\lim}}',r'\unsure{\uline{\lim}|\varinjlim}')
s=s.replace(r'(i_0<\ldots<i_n)',r'(i_0\unsure{<|\leq}\mathord{\cdot}\mathord{-}\unsure{<|\leq}i_n)')
p.write_text(s);(W/'records'/f'{pg}.tex').write_text(s)

for c in r['changes']:
    if c['id']=='C12':
        c.update(final=r'j_0\unsure{\ast|\ne}\mathord{-}j_n\in J',against_C=True,confidence='low',
          kind='misread symbol or index',error_kind='1 symbols/indices',crop=f'crops/{pg}_blind_B09.png',box=boxes['B09']['coordinates'],
          evidence='Blind rereading shows a small crossed, star-like mark after j0, followed by one horizontal stroke. Its crossed body admits an asterisk-like or not-equal-like reading, not a plain series of dots; no comma is visible on either side. The comma after J is separate. The ambiguous sign is kept locally, without repairing its mathematical meaning.')

new=[
 ('C18','(60), middle V subscript',r'V_{j_0\ldots j_n}',r'\mathcal V_{j_0\ldots j_n}',r'V_{j_0\mathord{-}\mathord{-}j_n}','B08','high','Two separate short horizontal rules, with a white gap between, occur between j0 and jn. They differ from the single continuous rule in the first and final V terms.'),
 ('C19','Line after (60), continuation within the increasing chain',r'j_0<j_1<\ldots<j_n',r'j_0<j_1<\cdots<j_n',r'j_0<j_1<\mathord{-}\mathord{-}<j_n','B09','high','Two elongated horizontal marks lie between the clear less-than signs; they are not three points.'),
 ('C20','Line after (60), subscript of the final live V',r'V_{i_0\ldots i_n}',r'\mathcal V_{i_0\ldots i_n}',r'V_{i_0\mathord{-}\mathord{-}i_n}','B09','high','The V subscript has two short horizontal rules separated by white space, matching the middle term of (60).'),
 ('C21','(61), index chain beneath the lower limit',r'(i_0<\ldots<i_n)',r'(i_0<\cdots<i_n)',r'(i_0\unsure{<|\leq}\mathord{\cdot}\mathord{-}\unsure{<|\leq}i_n)','B11','medium','Between the two compact relation signs there is a detached point followed by a longer horizontal rule. Each relation has a thickened lower return that does not settle an extra lower bar; the strict-sign reading is retained first with a narrow less-or-equal alternative.'),
 ('C22','(61), lower V subscript',r'V_{i_0\ldots i_n}^J',r'\mathcal V^{J}_{i_0\ldots i_n}',r'V_{i_0\mathord{-}\mathord{-}i_n}^J','B11','high','The lower V has two separate short horizontal continuation strokes, not a three-point ellipsis.')
]
for ident,place,c,h,final,b,conf,evidence in new:
    r['changes'].append(dict(id=ident,place=place,C=c,H=h,final=final,evidence=evidence,
      crop=f'crops/{pg}_blind_{b}.png',box=boxes[b]['coordinates'],confidence=conf,
      kind='misread symbol or index',error_kind='1 symbols/indices',against_C=True,against_H=True,
      consequential=False,marked_in_H=False,phase='blind audit'))
for d in r['decisions']:
    if d['id']=='M0661':d.update(reading=r'\unsure{\uline{\lim}|\varinjlim}',crop=f'crops/{pg}_blind_B11.png',box=boxes['B11']['coordinates'],ink='Both limit rules have thickened, slightly upturned ends without an isolated second arrowhead arm. Blind full-formula review favors a plain underline as the first alternative but does not resolve the arrow ambiguity.')
for d in r['doubts']:
    if 'upper limit' in d['place']:d.update(reading=r'\unsure{\uline{\lim}|\varinjlim}',alternatives=[r'\uline{\lim}',r'\varinjlim'],reason='Blind full-formula review favors the plain rule; a small endpoint return still permits an arrow, so M0661 stays undecided.')
r['doubts'] += [
 dict(place='Opening ideal condition, overwritten first index',reading=index,alternatives=['i',r'\deleted{x}\inserted{i}'],confidence='low',reason='A detached high dot supports i, but crossing oblique strokes below it could preserve an old x. The sequence of strokes cannot be certified; the alternative concerns revision state rather than a different final index.'),
 dict(place='Line after (60), crossed separator after j0',reading=r'\unsure{\ast|\ne}',alternatives=[r'\ast',r'\ne'],confidence='low',reason='The small crossed body has more than the simple points supplied by both drafts. An asterisk-like or not-equal-like construction remains possible.'),
 dict(place='(61), both relations in lower index chain',reading=r'\unsure{<|\leq}',alternatives=['<',r'\leq'],confidence='low',reason='Compact wedges have thickened lower returns; an independent lower bar cannot be securely excluded. No expected flag inequality is imposed.')
]
r['notes']+='\n### Blind-reading corrections\n\nThe independent reading led to a second inspection of every differing region. The continuation notation in (60), its following line and (61) is now distinguished as one rule, two rules, or point-plus-rule according to the ink. The first line also carries a local doubt about a possible overwritten x beneath the final i. The crossed separator after j0 and the compact inequalities below the lower limit remain uncertain. Both limits retain the rule/arrow doubt; the rule is now the first alternative for both. The letters of Drap and the crossed words dans la remain readable, and the cropped upper fragments in B06 do not replace the full-line reading alors on a. No new mathematical proof claim is made by these decisions.\n'
r['hand_log'].append(dict(habit='Continuation marks vary within one formula family',places='(60), following chain and V; (61)',scope='All six continuation regions in the two blind formula crops and following-line crop were compared: first/final (60) one rule, middle two; other local strings as recorded.',witness_errors='Both drafts regularize several two-rule or point/rule strings as an ellipsis.'))
rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

notes={}
def put(b,evidence,final=None):
    x=dict(viewed=True,evidence=evidence)
    if final is not None:x.update(changed=True,final=final)
    notes[b]=x
put('B02','The final index has a high dot and upright-compatible body, but two crossing diagonals beneath it permit an old x. Add a local uncertainty about the revision state, with i first; do not certify a separate struck x. The implication has a doubled shaft and a right head; Rightarrow versus Longrightarrow, math delimiters and spacing are equivalent encoding choices.',boxes['B02']['first'].replace(r'$i\in J$',r'$'+index+r'\in J$'))
put('B06','The upper strip cuts through the preceding baseline; the surviving l and reduced ors/on/a belong to the full-page alors on a, not an independently written donc plus dots. The formula shows both stars and J prime. The initial two short strokes of the canceled continuation remain equals; oblique hatching does not establish an independent wave. The tilde/J doubt remains in its original order because the upper zone is crossed. Prime spelling, star braces, spacing and inline/display wrappers do not change the reading.')
put('B07','All letters, the comma, the apostrophe and the raised crossed t agree. The three added line-break commands merely reproduce the four physical lines; retain the same words in the original paragraph encoding.')
put('B08','The first and last V indices each contain one long rule; the middle contains two separated short horizontal strokes. Replace only the middle ellipsis with two rules. All letters, indices and superscripts otherwise agree; mathord wrappers, braces and quad/qquad spacing have no independent reading effect.',boxes['B08']['first'].replace(r'V_{j_0\ldots j_n}',r'V_{j_0\mathord{-}\mathord{-}j_n}'))
f=boxes['B09']['first'].replace(r'j_0\ldots j_n\in J',r'j_0\unsure{\ast|\ne}\mathord{-}j_n\in J').replace(r'j_0<j_1<\ldots<j_n',r'j_0<j_1<\mathord{-}\mathord{-}<j_n').replace(r'V_{i_0\ldots i_n}',r'V_{i_0\mathord{-}\mathord{-}i_n}')
put('B09','The first separator has a crossed star-like body followed by one rule, so a narrow star/not-equal doubt replaces the supplied ellipsis. The later flag continuation and V subscript each have two horizontal strokes. The canceled first word shows looped d plus a/n/s; the next has tall l and one low a, with no independent final s: retain dans la. The comma after the flag and the live ce sont alors les are visible; moving the comma inside math delimiters is encoding only.',f)
put('B10','The terminal on is compressed against the edge but its rounded body and long final n return remain on the sheet. The complete word stratification is retained. The second reader adds uncertainty only; no missing letters are supplied beyond the visible terminal return.')
f=boxes['B11']['first'].replace(r'\unsure{\varinjlim|\uline{\lim}}',r'\unsure{\uline{\lim}|\varinjlim}').replace(r'(i_0<\ldots<i_n)',r'(i_0\unsure{<|\leq}\mathord{\cdot}\mathord{-}\unsure{<|\leq}i_n)').replace(r'V_{i_0\ldots i_n}',r'V_{i_0\mathord{-}\mathord{-}i_n}')
put('B11','The two lim rules end in compact returns without distinct second head arms; keep both alternatives and put the plain rule first. The lower index has a point and then a rule between compact relation signs; retain < first but add a less-or-equal alternative to both. The lower V has two horizontal strokes. Drap has the tall D, reduced r/a and descending p; the small a is not certified as a period, so no Dr.p alternative is added. The remaining differences are braces, font wrapper and horizontal spacing.',f)
(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('079 page/records updated; seven actually observed differing crops adjudicated.')
