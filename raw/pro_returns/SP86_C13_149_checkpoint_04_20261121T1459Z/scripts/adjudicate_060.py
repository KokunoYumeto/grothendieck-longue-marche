"""Root decisions from the twelve differing blind crops, scan 060."""
import json
from pathlib import Path
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan060';p=B/'pages'/f'{page}.tex';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
t=p.read_text();sh=r'\unsure{=|\overline m}'
old=r'\deleted{\unsure{Z}}_{\unsure{\mathrm{en}|\pi}}'
frag=r'\unsure{\deleted{\unsure{Z}}\mathrm{er}|\deleted{\unsure{Z}}\mathrm{en}|\deleted{\unsure{Z}}_{\mathrm{en}}|\deleted{\unsure{Z}}_{\pi}}'
assert t.count('$=$')==4;t=t.replace('$=$','$'+sh+'$')
for a,b in [('pt fixes',r'p\textsuperscript{t} fixes'),(r'\deleted{\unsure{x}}',r'\deleted{\unsure{x|\mathrm{en}}}'),('faudrait écrire',r'faudrait $'+sh+'$ écrire'),(old,frag),('(i.e il',r'(i\unsure{.|:}e il')]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
shape='A detached upper bar stands over a cupped lower entrance, small central rise and long flat/downturned right return. This repeated prose shorthand admits equals and a compressed barred-m reading. Its written glyph remains uncertain and is not expanded.'
for cid in ['P04a','P05','P09','P11']:
 c[cid].update(final=('sur le ' if cid=='P04a' else '')+'$'+sh+'$',against_C=False,confidence='medium',evidence=shape)
xev='The crossed older cluster has looped low forms and overlapping diagonal strokes. These allow both a tentative x and an en-like group, without a secure letter-by-letter recovery. The separate dark live x and wavy tilde remain clear. The isolated mark to the upper right is above the baseline and does not establish a full stop after the symbol.'
c['P07b'].update(final=r'$\deleted{\unsure{x|\mathrm{en}}}$',evidence=xev,confidence='low')
zev='The large first form has an upper bar, descending diagonal and bottom return of Z, with a thinner independent oblique crossing it. The following small loop and terminal hump lie outside that crossing. They favor baseline er, while en and lowered en/pi alternatives remain open. There is no separate full-height left upright for K. The live pi, raised Gamma and its small round upper-right loop remain outside the cancelled fragment.'
c['P15'].update(final='$L_i='+frag+r'\pi^{\Gamma^\circ}$',evidence=zev,confidence='medium')
ptev='The t after the opening p is shorter and its foot sits above the p shoulder and the following fixes baseline. Its upright and short rightward cross stroke are separate and clear; it is retained as a raised t without expanding the abbreviation.'
margin_ev='At the start of the final slanted line, before écrire, a detached short bar and a lower cupped stroke are visible. The nearby descending q stroke crosses the right end but does not account for the two horizontal components. This restores a written shorthand omitted by both witnesses. The glyph remains uncertain between equals and barred m.'
colon_ev='Between the initial i and e are a dark lower point and a smaller higher mark, separate from the dot above i. The two-level form admits a colon, while the upper mark is too small to exclude a speck; the single-point reading remains first. No point follows e.'
newrows=[dict(id='P18',place='main line 2, raised t in pt',C='pt',H='pt',final=r'p\textsuperscript{t}',evidence=ptev,crop=f'crops/{page}_B03_second.png',box=next(x['coords'] for x in r['audit_boxes'] if x['box']=='B03'),confidence='high',against_C=True,against_H=True,kind='misread symbol or index',error_category='Symbols and indices',marked_in_H=False,consequential=False),dict(id='P19',place='margin, before écrire',C='(nothing)',H='(nothing)',final='$'+sh+'$',evidence=margin_ev,crop=f'crops/{page}_B10_second.png',box=next(x['coords'] for x in r['audit_boxes'] if x['box']=='B10'),confidence='medium',against_C=True,against_H=True,kind='omission',error_category='Omissions',marked_in_H=False,consequential=False)]
r['changes'].extend(newrows);c['P17'].update(final=r'(i\unsure{.|:}e',evidence=colon_ev,confidence='medium')
for d in r['decisions']:
 if d['id'] in ['M1161','M1162','M1164','M1165']:
  bn={'M1161':'B04','M1162':'B05','M1164':'B09','M1165':'B11'}[d['id']];box=next(x['coords'] for x in r['audit_boxes'] if x['box']==bn)
  d.update(decision='undecided',reading=sh,evidence=shape,crop=f'crops/{page}_{bn}_second.png ('+','.join(map(str,box))+')',confidence='medium')
for d in r['doubts']:
 if 'cancelled older' in d['place']:d.update(reading=r'$\deleted{\unsure{x|\mathrm{en}}}\ \widetilde x$',alternatives=r'x|\mathrm{en}',reason=xev)
 if 'Z-like' in d['place']:d.update(reading=frag,alternatives='cancelled Z with baseline er or en; lowered en or pi',reason=zev)
for place in ['main line 2 after le','main line 4 after en','main line 7 after en','main line 12 before action']:
 r['doubts'].append(dict(place=place,reading='$'+sh+'$',alternatives=r'=|\overline m',reason=shape,confidence='medium'))
r['doubts'].extend([dict(place='margin, before écrire',reading='$'+sh+'$',alternatives=r'=|\overline m',reason=margin_ev,confidence='medium'),dict(place='main line 1, inside abbreviation',reading=r'i\unsure{.|:}e',alternatives='.|:',reason=colon_ev,confidence='medium')])
for x in r['inventory']:
 if x['element']=='E03':x['first_words_or_objects']=r"C'est un cas particulier ... faudrait $"+sh+'$ écrire'
 if x['element']=='E04':x['first_words_or_objects']=r'\unsure{x|\mathrm{en}}'
r['deletion_insertion_review'][0]=xev;r['deletion_insertion_review'][2]=zev
for h in r['hand']:
 if h['form']=='=':h.update(form=sh,observation=shape,places='main lines 2, 4, 7, 12; final margin line',scope='All five occurrences remain glyph-qualified after blind comparison.',witness_errors='C doubts four main-text signs and omits the margin sign; H expands or rewrites the main-text signs and omits the margin sign.')
r['hand'].append(dict(form=r'p\textsuperscript{t}',observation=ptev,places='main line 2, B03',scope='This opening occurrence; no uniform raised-t rule is imposed.',witness_errors='Both witnesses set the t on the baseline.'))
for n in r['notation']:
 if n['form'].startswith('L_i='):n['form']='L_i='+frag+r'\pi^{\Gamma^\circ}'
r['notation'].append(dict(form=sh,meaning='Written two-level prose shorthand, left unexpanded and unresolved.',places='main lines 2, 4, 7, 12 and final margin line'))
r['notes']=[n.replace("sauf qu'il faudrait écrire",r"sauf qu'il faudrait $\unsure{=|\overline m}$ écrire") for n in r['notes']]
r['notes'].append('Blind audit restores the shorthand before écrire in the margin, records the raised t of the opening pt, and broadens the two cancelled-fragment readings. The initial abbreviation keeps uncertainty about point/colon between i and e. These are source-reading changes, with no mathematical proof check.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(n,decision,evidence):D[n]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
def change(n,final,decision,evidence):D[n]=dict(final=final,changed=True,decision=decision,evidence=evidence)
change('B03',r'p\textsuperscript{t} fixes','Preserve the raised abbreviation letter',ptev)
change('B04',r'sur le $'+sh+r'$ $x\in U(K)$,','Reopen the shorthand in the full phrase',shape+' The x, membership, U(K) with its one closing curve and separate comma are clear.')
for bn in ['B05','B09','B11']:change(bn,'$'+sh+'$','Reopen the recurring shorthand',shape)
change('B07',r'fixe $\deleted{\unsure{x|\mathrm{en}}}\ \widetilde x$','Broaden the cancelled older writing',xev)
change('B10',r"C'est un cas particulier d'une ``conséquence conjecturale'' des conjectures du $\S1$ --- sauf qu'il faudrait $"+sh+r'$ écrire $\pi^{\Gamma^\circ}=(1)$','Restore the omitted marginal shorthand',margin_ev+' Elsewhere the double-curved section sign and numeral 1 are visible after du. The final Gamma modifier is an open upper-right loop. The source has doubled quotation ticks; the line breaks and margin wrapper do not add words.')
keep('B12','Retain the dash and dessus','The separate horizontal dash precedes a d oval/ascender, low e, two s-like turns, and a low u/s ending. No separate i dot supplies disons; the visible final run and double-s support dessus. No au is added.')
keep('B13','Retain the bar over I','The dotted i and membership sign precede a tall I stroke with its own low foot. A separate long upper bar lies above the stem with a visible gap, retaining barred I.')
change('B15',c['P15']['final'],'Refine the lower letters and their placement alternatives',zev)
keep('B16','Retain the same marginal foliation','The pale numerals have the upper stroke and lower bend of 5 followed by the closed upper bowl and descending curve of 9. The second margin wrapper records the same location already assigned to 59 in the page.')
change('B17',r'(i\unsure{.|:}e il','Qualify the two-level punctuation',colon_ev+' The opening curve and following il remain visible.')
main(dict(page=page,root_viewed=[f'crops/{page}_{n}_second.png' for n in D],decisions=D));record(page);assign('reader_a')
