"""Root's explicit decisions after visual inspection of the differing audit crops."""
import json
from pathlib import Path
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign

B = Path(__file__).resolve().parents[1]
page = '149_scan057'
p = B / 'pages' / (page + '.tex')
rpath = B / 'reviews' / (page + '.json')
r = json.loads(rpath.read_text())
assert not r.get('audit')
t = p.read_text()
ins = r'\inserted{\unsure{classes de|\deleted{\unsure{classes} de}}}'
oldstrike = r'\deleted{\unsure{par}\ \unsure{des}}'
strike = r'\unsure{\deleted{\unsure{par}\ \unsure{des}}|par des}'
repls = [
 (r'\inserted{classes de} '+oldstrike, ins+' '+strike),
 (r'sections,\deleted{)} et en', r'sections,\deleted{\unsure{)|f|et}} et \unsure{en|un}'),
 ('ne sont', r'\unsure{ne|en} sont'),
 (r'finie \inserted', r'\unsure{finie|fini} \inserted'),
 (r'en $=$ temps', r'en $\unsure{=|\overline m}$ temps'),
 (r'U=X\setminus\bar I', r'U=X-\overline{\unsure{I|\underline I}}'),
 (r'(2g+\nu\geq3)', r'(2g\unsure{+}\nu\geqslant3)')
]
for a,b in repls:
 assert t.count(a)==1,(a,t.count(a))
 t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
state_evidence='The small interlinear classes de has a thin horizontal stroke extending through its upper bodies and across the gap toward de. The baseline par/des has overlapping horizontal joins through its bowls. The crop does not securely separate pen joins from cancellation at either level; the two revision states remain explicit alternatives. No leader fixes a different attachment.'
c['P02b'].update(final=ins,evidence=state_evidence,confidence='low',against_C=False,against_H=False)
c['P02c'].update(final=strike,evidence=state_evidence,confidence='low')
r.setdefault('observations',[]).append(c['P02b'])
r['changes']=[x for x in r['changes'] if x['id']!='P02b']
c['P05a'].update(final=r'sections,\deleted{\unsure{)|f|et}}',confidence='medium',evidence='The comma is dark and separate. The following cancelled sign has a broad right arc and intersecting loop/upright; the crossing obscures whether the underlying sign is a parenthesis or letter strokes. The cancelled reading remains tentative.')
c['P05b'].update(final=r'\unsure{en|un}',confidence='medium',evidence='The initial is an open low cup followed by a long n-like return. Its aperture supports en, while the joined stroke also allows un. There is no closed initial o bowl.')
c['P08'].update(final=r'\unsure{ne|en} sont',confidence='medium',evidence='The first short word is a cup and flattened connected return; ne/en cannot be separated securely. The following sont and blank space to the line edge are visible; the next line begins eux-mêmes. No pas is supplied.')
c['P12b'].update(final=r'\unsure{finie|fini} \inserted{$K\prime$} de $K$'.replace(r'K\prime',"K'"),confidence='medium',evidence='The last dotted i has a short rightward terminal return; that return may carry an e, but the ending is not independently clear. K and its prime stand above the gap, with the leader descending to the space before de K.')
c['P14'].update(final=r'$\unsure{=|\overline m}$',against_C=False,confidence='medium',evidence='A detached upper bar lies over a lower stroke with a left cup, central cusp, and long right return. The lower stroke admits the compressed barred-letter reading as well as the two-level equals shorthand. M1153 is reopened; the abbreviation is not expanded.')
c['P15'].update(final=r'$U=X-\overline{\unsure{I|\underline I}}$',against_C=True,confidence='medium',evidence='The separator after X is a short nearly horizontal stroke with a downturned end. I has a detached long upper bar and a separate short lower rule; the latter may be its foot or an underline. Three following marks of the ellipsis remain visible.')
for d in r['decisions']:
 if d['id']=='M1150':d.update(decision='undecided',reading=ins,evidence=state_evidence,confidence='low',crop='crops/149_scan057_B02_second.png (775,70,1190,185)')
 if d['id']=='M1153':d.update(decision='undecided',reading=r'\unsure{=|\overline m}',evidence=c['P14']['evidence'],confidence='medium',crop='crops/149_scan057_B14_second.png (605,1015,710,1090)')
r['doubts'][0].update(reading=strike,alternatives='cancelled tentative par des | live par des',reason=state_evidence)
new_doubts=[
 ('line 1, interlinear revision',ins,'live classes de | inserted and cancelled classes de', 'low',state_evidence),
 ('line 3, cancelled sign',r'\deleted{\unsure{)|f|et}}',')|f|et','medium',c['P05a']['evidence']),
 ('line 3, final word',r'\unsure{en|un}','en|un','medium',c['P05b']['evidence']),
 ('line 5, before sont',r'\unsure{ne|en}','ne|en','medium',c['P08']['evidence']),
 ('line 8, ending',r'\unsure{finie|fini}','finie|fini','medium',c['P12b']['evidence']),
 ('line 10, shorthand',r'$\unsure{=|\overline m}$',r'=|\overline m','medium',c['P14']['evidence']),
 ('line 11, lower stroke of barred I',r'$U=X-\overline{\unsure{I|\underline I}}$',r'I|\underline I','medium',c['P15']['evidence']),
 ('line 16, arithmetic sign',r'$(2g\unsure{+}\nu\geqslant3)$','+ remains tentative','medium','The short sign has a horizontal entry and curled return; a separate crossing upright is obscured. The lower inequality stroke rises obliquely beneath the greater-than sign.')]
for place,reading,alternatives,confidence,reason in new_doubts:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
for x in r['inventory']:
 if x['element']=='E03':x['first_words_or_objects']=ins
 if x['element']=='E04':x['first_words_or_objects']=strike;x['position']='line 1, baseline before paquets; cancellation state uncertain'
 if x['element']=='E05':x['first_words_or_objects']=r'\unsure{)|f|et}'
r['deletion_insertion_review'][:3]=[state_evidence,'The interlinear and baseline alternatives are both retained in place; their order is not asserted from the crowded joins.',r'Line 3: a live comma precedes the cancelled tentative sign \unsure{)|f|et}; et and the tentative en/un remain live.']
for n in r['notation']:
 if n['form']==r'U=X\setminus\bar I':n.update(form=r'U=X-\overline{\unsure{I|\underline I}}',meaning='The written separator is a short horizontal stroke; the lower rule beneath barred I remains uncertain as foot or underline.')
 if n['form']==r'(g,\nu),\ (2g+\nu\geq3)':n['form']=r'(g,\nu),\ (2g\unsure{+}\nu\geqslant3)'
r['audit_supplementary_crops']=[dict(crop='crops/149_scan057_B13_context_audit.png',box=[275,1000,605,1145],reason='Frozen B13 ends before the following comma; this audit context crop shows its separate dark curved stroke.',root_viewed=True)]
rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(box,decision,evidence):D[box]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
def change(box,final,decision,evidence):D[box]=dict(final=final,changed=True,decision=decision,evidence=evidence)
change('B02','donc '+ins+' '+strike,'Retain both uncertain revision states',state_evidence)
keep('B03','Retain ss-groupes','Two compact upright turns precede the separate hyphen; the following g has a long descending loop.')
keep('B04','Retain the circular superscript convention','A small rounded open oval is raised beside Gamma; par ses follows. The chosen circ records that circular glyph without expanding it to a word or assigning a new value.')
change('B05',r'sections,\deleted{\unsure{)|f|et}} et \unsure{en|un}','Mark the cancelled sign and final word uncertain',c['P05a']['evidence']+' '+c['P05b']['evidence'])
keep('B06','Retain mettant ensemble des','The first word has tall medial t strokes and a separate pointed terminal t; ensemble follows after a gap. The last word begins with the oval and ascender of d.')
keep('B07','Retain the same Z/C alternatives and circular superscript','The crowded initial contains an upper loop, diagonal, and broad base; entr is clear. The second reading relocates the same Z/C uncertainty within the word; the raised small circular glyph remains circ.')
change('B08',r'\unsure{ne|en} sont','Mark the short word uncertain',c['P08']['evidence'])
change('B12',r"tt ext. \unsure{finie|fini} \inserted{$K'$} de $K$)",'Retain the insertion and mark the ending uncertain',c['P12b']['evidence'])
keep('B13','Retain capital Pi and following comma','B13 shows the long top bar and two uprights of Pi, with L/K below. The frozen crop ends before the comma. The supplemental audit crop crops/149_scan057_B13_context_audit.png (275,1000,605,1145), viewed by root, shows the separate dark curved comma between K and en.')
change('B14',r'$\unsure{=|\overline m}$','Reopen M1153',c['P14']['evidence'])
change('B15',r'$U=X-\overline{\unsure{I|\underline I}}$\ldots','Read the horizontal separator and retain lower-rule uncertainty',c['P15']['evidence'])
keep('B16','Retain E and the uncertain connector','Each E has the same two rounded lobes and the subscripts L/K are clear. The mathcal wrapper maps occurrence-for-occurrence to these same E glyphs. The connector has a short shaft and downturned return without a secure separate head; the existing uncertainty remains.')
keep('B18','Retain nu and uncertain punctuation','The right member has a cupped body and rising right arm, also visible in the next formula. A separate dark mark follows the closing parenthesis; its short outline still permits period or comma.')
change('B19',r'$(2g\unsure{+}\nu\geqslant3)$','Mark the obscured sign and record the sloping lower inequality stroke',new_doubts[-1][-1])
keep('B20','Retain continu','The word has a tall medial t followed by a dotted i and the low n/u ending; the paired elevated quotation strokes are visible at both ends.')
keep('B21','Retain the ellipsis macro','Three separate dark points follow the final s. The literal three dots of the blind reading correspond to these same three marks.')
keep('B22','Retain modélique','After m/o/d, an e carries a detached accent; the following tall l precedes dotted i and the descending q, then u/e. The q descender and tall l support the first letter sequence.')
keep('B25','Retain manuscript page number 28','The first digit has an upper arch, descending diagonal and foot; the second has two closed bowls. The mspage wrapper records its location and changes neither digit.')
keep('B26','Retain margin number 56','A thin 5 with top bar and lower return precedes a 6 with closed lower bowl. The margin wrapper records the location of these same digits.')
keep('B27','Retain digits 0 and 1 with following comma','The first digit is a low oval and the second a long upright with foot; a dark separate comma follows. Math-mode delimiters change no written digit.')
main(dict(page=page,root_viewed=[f'crops/{page}_{x}_second.png' for x in D]+['crops/149_scan057_P02.png','crops/149_scan057_B13_context_audit.png'],decisions=D))
record(page)
assign('reader_a')
