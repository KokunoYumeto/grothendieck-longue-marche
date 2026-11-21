"""Root audit decisions from the freshly viewed second crops, scan 058."""
import json
from pathlib import Path
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan058'
p=B/'pages'/f'{page}.tex';rp=B/'reviews'/f'{page}.json'
r=json.loads(rp.read_text());assert not r.get('audit')
t=p.read_text()
oldstate=r'\unsure{\deleted{de}|\inserted{\deleted{de}}}'
state=r'\unsure{\deleted{de}|\inserted{\deleted{de}}|\inserted{de}}'
oldabbr=r"l'\deleted{ens}\unsure{.|\deleted{.}}"
abbr=r"l'e\deleted{\unsure{ns}}\unsure{.|\deleted{.}}"
for a,b in [(r'en $=$ temps',r'en $\unsure{=|\overline m}$ temps'),(r'\deleted{de} $\widetilde U$',r'\deleted{\unsure{de}} $\widetilde U$'),(oldstate,state),(oldabbr,abbr),("pts à l'infini",r"pts \unsure{à|:} l'infini")]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
c['P09'].update(final=r"en $\unsure{=|\overline m}$ temps qu'un",against_C=False,confidence='medium',evidence='A short detached upper bar is followed by a lower cupped/cusped stroke with a long right return. Its curvature leaves the equals shorthand and compressed barred-letter reading open. The apostrophe in qu\'un remains visible. M1155 is reopened; no expansion is introduced.')
c['P10'].update(final=r'\deleted{\unsure{de}} $\widetilde U$',against_C=False,confidence='medium',evidence='The underlying d has a pale oval and ascender; the following loop is crossed by the heavy U. The proposed de remains plausible, but the overwritten e is not plain throughout. Local doubt D058_01 is restored.')
c['P11'].update(final="le normalisé "+state+" $X'$ de $X$",evidence='The article has a looped l and low open e; normalisé ends in one short accented e. The raised de lies above X-prime and has a thick horizontal return through its lower part. The crop leaves both its cancellation status and the sequence of insertion/overwriting open; all supported source states are retained.',confidence='medium')
c['P15'].update(final=r'$1-1$ avec '+abbr+' fibre',evidence='The l, apostrophe and following e loop stand left of the independent cancellation stroke. That stroke begins over the next low minims and crosses the terminal return, retained as tentative ns. The separate dark dot has uncertain cancellation scope. The next word has f, dotted i, tall b, and a low r/e ending; no separate terminal s or intervening les is visible.',confidence='medium')
c['P20'].update(final="``pts \\unsure{à|:} l'infini''",evidence='The quotation marks are elevated tick pairs. Between pts and l\'infini there is a small lower curved mark and a detached upper stroke. They favor à, while the two-mark form also allows a colon; the uncertainty is retained.',confidence='medium')
for d in r['decisions']:
 if d['id']=='M1155':d.update(decision='undecided',reading=r'\unsure{=|\overline m}',evidence=c['P09']['evidence'],confidence='medium',crop='crops/149_scan058_B09_second.png (285,800,1180,960)')
for d in r['doubts']:
 if 'raised cancelled' in d['place']:d.update(reading=state,alternatives='cancelled de | inserted then cancelled de | live inserted de',reason=c['P11']['evidence'])
 if 'dot after' in d['place']:d.update(place='main line 15, cancelled ns and following dot',reading=abbr+' fibre',alternatives='ns tentative; following dot live or cancelled',reason=c['P15']['evidence'])
for place,reading,alts,reason in [
 ('main line 8, shorthand',r'$\unsure{=|\overline m}$',r'=|\overline m',c['P09']['evidence']),
 ('main line 9, overwritten word',r'\deleted{\unsure{de}}','de remains tentative',c['P10']['evidence']),
 ('main line 20, before l\'infini',r'\unsure{à|:}','à|:',c['P20']['evidence'])]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,reason=reason,confidence='medium'))
for x in r['inventory']:
 if x['element']=='E05':x['first_words_or_objects']=r'\deleted{\unsure{de}} $\widetilde U$'
 if x['element']=='E06':x.update(first_words_or_objects=state,position='raised de above X prime in main line 9; cancellation and insertion sequence uncertain; P11')
 if x['element']=='E08':x.update(first_words_or_objects=abbr,position='main line 15, ns cancelled after live l apostrophe e; following dot state uncertain; P15')
r['deletion_insertion_review'][1]=c['P10']['evidence']
r['deletion_insertion_review'][2]=c['P11']['evidence']
r['deletion_insertion_review'][4]=c['P15']['evidence']
for n in r['notation']:
 if n['form']=='=':n.update(form=r'\unsure{=|\overline m}',meaning='Two-level prose shorthand with a curved lower stroke; the glyph reading remains uncertain and the abbreviation remains unexpanded.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(n,decision,evidence):D[n]=dict(keep_first=True,changed=False,decision=decision,evidence=evidence)
def change(n,final,decision,evidence):D[n]=dict(final=final,changed=True,decision=decision,evidence=evidence)
keep('B02','Retain the headless connector','The shaft ends in a thick terminal dot/return. There are no two distinct oblique arms forming a head; both E forms and U/K subscripts are visible.')
keep('B03','Retain the unreadable cancelled start and live remonte','The dense crossed cluster is confined before the separate r/e opening of remonte. The latter continues to a tall t and final e outside that cluster; the cancelled underlying unit cannot be recovered letter by letter.')
keep('B04','Retain the headless connector','The almost horizontal shaft has a short downturned right end without separately drawn upper and lower head strokes. L and K remain clear.')
keep('B05','Retain both cancelled word alternatives','The long p descender survives and the horizontal strike covers the vowel/minim run. Both par and pour remain possible; their proposed order does not settle the covered letters.')
keep('B07','Retain the headless connector and comma','The shaft rises slightly and curls downward at its right end. This terminal return supplies no distinct pair of arrowhead arms. The comma after K is a separate dark curved stroke.')
change('B09',c['P09']['final'],'Reopen the shorthand reading',c['P09']['evidence'])
change('B10',c['P10']['final'],'Restore uncertainty in the overwritten word',c['P10']['evidence'])
change('B11',c['P11']['final'],'Retain normalisé and broaden the source-state uncertainty',c['P11']['evidence'])
keep('B12','Retain dans and the following formula','After the d oval and ascender the word has a low extra cusp, extended joined run and terminal s-like return. The following tilde U, parenthesis, accented où, equality, hat U and final point remain visible.')
keep('B14','Retain the uncertain small insertion','The small inserted word after the apostrophe has several low cups/minims and a terminal turn; ens/un remains unresolved. The curved leader descends into the gap after baseline les and before L_i. The bar, equality and minus signs of the full formula are visible.')
change('B15',c['P15']['final'],'Correct the deletion boundary after live e',c['P15']['evidence'])
keep('B16','Retain au dessus','The short first word has a small a-like body and long low u return. The following word has d/e, two s turns, and a low u/s ending, without a separate o bowl after the doubled s. The X-primes and i are visible.')
keep('B17','Retain the diagram and its established encoding','The same eight objects occupy three rows. Five horizontal strokes, two lower vertical strokes and three independent upright cup signs occupy the same corresponding positions in both encodings. Every connecting stroke is headless; bar and overline, dash and no-head, and ampersand escaping account for the token differences.')
keep('B18','Retain the baseline barred-I expression','X-prime and the tall separate vertical rule are followed by I whose foot lies at the neighboring formula baseline. Its upper bar is detached. The second rendering lowers I as a subscript; the observed relative height is retained by the first rendering.')
keep('B19','Retain qui apparaissent','The short word has q descender, joined u and a separate i dot. The next word begins with a low a and two long descending p strokes; its later low runs and pointed terminal t support apparaissent. The two p descenders are visible separately.')
change('B20',r"des ``pts \unsure{à|:} l'infini'' du",'Mark the small two-level mark uncertain',c['P20']['evidence'])
keep('B21','Retain the visible inter- ending','After s-apostrophe, the dotted i and flat n lead to a tall crossed t and low e/r return. The last return has no closed o bowl. The separate short line-ending hyphen is retained without completing the word.')
main(dict(page=page,root_viewed=[f'crops/{page}_{n}_second.png' for n in D],decisions=D))
record(page);assign('reader_b')
