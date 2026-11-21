"""Root decisions from thirteen differing blind crops of scan 062."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan062';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text()
replacements=[(r'$=\ \bar U,\bar V$',r'$\unsure{=}\ \bar U,\bar V$'),(r'\unsure{E|É}tant donné','Étant donné'),(r'Poincaré\unsure{.}','Poincaré.'),('complétée',r'compl\unsure{é|e}tée')]
for a,b in replacements:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t);c={x['id']:x for x in r['changes']}
eq='Before the clear barred U, comma and barred V, the lower horizontal trace is visible but broken, and the possible upper companion is extremely faint. The two-level equals reading remains plausible; the pale upper trace does not support a high-confidence resolution. M1168 is reopened as a localized unsure equals without a supplied interpretation.'
accent='A detached dark oblique/near-vertical stroke stands above the initial E, separate from both its upper stroke and the following t upright. Its gap and position support an accent on É. The a, n and terminal t of tant, then donné, remain visible.'
point='The isolated point after the final accented letter of Poincaré sits at the prose baseline, with darkness and size comparable to the neighboring written endpoints. It is separate from both the word and the inward U loop. Retain the full stop. The two close wavy upper strokes on U still leave the tilde/tilde-plus-bar alternatives open.'
comp='The c/o/m run leads to the long descending p and looped l. A very thin short trace above the flattened vowel before t leaves the first accent uncertain. After the tall t there are two distinct low returns, with a detached accent over the ending; the written ending remains tée. Keep uncertainty only on the first é/e, with no supplied ion ending.'
c['P06a'].update(final=r'\unsure{=}',evidence=eq,confidence='medium',against_C=False)
c['P10b'].update(final='.',evidence=point,confidence='high')
c['P12a'].update(final=r'compl\unsure{é|e}tée',evidence=comp,confidence='medium')
c['P12c']['final']=c['P12c']['final'].replace('complétée',r'compl\unsure{é|e}tée')
for d in r['decisions']:
 if d['id']=='M1168':d.update(decision='undecided',reading=r'\unsure{=}',evidence=eq,crop=f'crops/{page}_B04_second.png (565,1185,840,1295)',confidence='medium')
r['doubts']=[d for d in r['doubts'] if d['place'] not in ['line 15 opening, P09','line 15, dark point after Poincaré, P10']]
r['doubts'].extend([dict(place='line 11 before barred U,V, M1168 / B04',reading=r'\unsure{=}',alternatives='equals sign; faint companion stroke unresolved',confidence='medium',reason=eq),dict(place='line 17, first accent in completion word, B09',reading=r'compl\unsure{é|e}tée',alternatives='complétée; completée',confidence='medium',reason=comp)])
for x in r['inventory']:
 if x['element']=='E03':x['first_words_or_objects']=x['first_words_or_objects'].replace(r'\unsure{E|É}tant','Étant')
for h in r['hand']:
 if h['form']=='E / É at the opening of Etant':h.update(form='É at the opening of Étant',observation=accent,scope='This initial accent is resolved after blind crop comparison.',witness_errors='Both witnesses give the accented word; the added first-pass uncertainty is now removed.')
r['notation'].append(dict(form=r'\unsure{=}\ \bar U,\bar V',meaning='The faint two-level trace before the barred pair remains unresolved; no expansion or mathematical identification is supplied.',places='line 11, B04'))
r['notes'].append('Blind audit keeps the written words nos, car, définiss(e/a)nt, the quantifier before autom, pas néc. induisant, and induise un autom. de. It resolves the detached accent on Étant and the full stop after Poincaré, while reopening the faint equals sign and qualifying the first accent in the completion word. The different U entries and the local upper decorations remain as separately observed.')
for x in r.get('nonmaterial_observations',[]):
 if x.get('final')==r'\unsure{E|É}tant':x.update(final='Étant',evidence=accent)
r.setdefault('nonmaterial_observations',[]).append(dict(id='A062_E',place='line 15 opening, B06',C='Étant',H=r'\uncertain{Étant}',final='Étant',evidence=accent,crop=f'crops/{page}_B06_second.png',box=[310,1674,710,1770]))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,evidence):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=evidence)
def change(b,final,title,evidence):D[b]=dict(final=final,changed=True,decision=title,evidence=evidence)
keep('B01','Retain tous nos beaux','The first word has its tall t, closed o and low u/s. In the next group the raised middle arch joins a closed low oval before the terminal s, supporting n/o/s. The connected initial group has no separate open c followed by a distinct e. Beaux has the tall b, low e/a/u and crossed x.')
keep('B02','Retain the phrase and the recorded Q rendering','The e/x/t and its stop, de, type, fini and second de are visible in sequence. Q has its oval, a dark inner diagonal at the lower-left and a separate descending terminal at the right. The blackboard-Q encoding retains that inner stroke; both returns refer to this same single letter at the same coordinate.')
keep('B03','Retain car and the comma after zero','The word opens with an unclosed c curve and a low flattened a/r run ending in a small hooked return. No detached stop follows it. The numeral is a closed oval; a separate long curved comma follows. The written short word and punctuation remain car 0,.')
change('B04',r'$\unsure{=}\ \bar U,\bar V$','Reopen the faint sign in the full barred pair',eq)
keep('B05','Retain the e/a uncertainty','The tall d and f, the two i dots, the compressed middle run and terminal t are visible. The vowel before nt remains flattened into a very thin run and does not isolate a complete bowl. The blind e reading favors the existing first alternative but does not remove a.')
change('B06','Étant donné','Resolve the detached initial accent',accent)
change('B07',r'Poincaré. $\unsure{\widetilde{\mathcal U}|\widetilde{\overline{\mathcal U}}}$','Resolve the point and retain the decoration uncertainty',point)
change('B09',r'compl\unsure{é|e}tée','Qualify only the first accent',comp)
keep('B11','Retain the same inserted hatted U','The complete angular hat stands above an open left entry, deep cup and raised right limb of U. The wider B10 box already carries the insertion wrapper and comma in both readings. This narrow box changes only whether the same placement wrapper is repeated around the symbol.')
keep('B12','Retain forall and the unexpanded autom','The large sign has a left descending limb, low vertex, rising diagonal, right returning limb and a transverse interior stroke. These form the single forall glyph; there are no two separate t bodies. The following short word has a/u, tall t and low o/m. Its dark downturned terminal is continuous with the last return, leaving no separate abbreviation stop.')
keep('B13','Retain the tilde on the parenthesized calligraphic U','The U has a conspicuous inward head curl. Its upper sign has a central dip and raised right turn, with a gap beneath it; it is wavy rather than a straight bar. The following comma, barred K and both parentheses remain clear. The retracing stays within the one wavy sign.')
keep('B14','Retain the two short words and induisant','After the opening curve there is a p with a long descending loop and low a/s. A word gap precedes the low n/e/c, detached accent and stop. The next word has i, n, tall d, u, dotted i, low s/a/n and a final taller t. Those separate groups support pas néc. induisant, followed by l\'identité.')
keep('B15','Retain induise un autom. de','The first group has dotted i, n, looped d, u, dotted i and low s/e ending; its final short turn stays below the height of a t. The separate article has u/n. The following abbreviation has a low open a/u entry, a tall looped t and low o/m, then a detached stop. The last de is separate. The ink supports the retained words without the additional n/t ending or endom opening.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_c')
