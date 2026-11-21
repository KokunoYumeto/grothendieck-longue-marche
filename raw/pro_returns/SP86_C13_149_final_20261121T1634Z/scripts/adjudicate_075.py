"""Root crop adjudication of the fixed blind scan 075 reading."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan075';rp=B/'reviews'/f'{page}.json'
r=json.loads(rp.read_text());assert not r.get('audit');p=B/'pages'/f'{page}.tex';t=p.read_text()
label=r"\deleted{\unsure{c)|b'')}}"
pron=r"\unsure{qu'ils|qu'il}"
genus=r'\deleted{genre $g$ \unsure{est} $\geq 1$}'
end=r'finale-\newline \unsure{ment|vient}'
repls=[(r"I_{x\unsure{'}}",r"I_{x'}"),(r'\deleted{\unsure{c)}}',label),("qu'ils",pron),('aussitôt,',r'aussitôt\unsure{,}'),(r'\unsure{\mid|/}',r'\mid'),(r'\deleted{genre $g\geq 1$}',genus),('conclusion est',r'conclusion \unsure{est}'),(r'finale-\newline ment',end)]
for a,b in repls:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
evprime='The detached short dark tick stands immediately above/right of the lower x and is separated from both crossing x strokes and the following relation. Its lower end curves slightly left. This placement supports a prime attached to x. The relation still has a thick humped upper stroke over a straighter lower bar, leaving simeq/equal open. The infinity loop, barred K, parentheses and comma are preserved.'
evlabel='Several oblique cancellation strokes cover the left body and the raised short strokes beside it. The surviving lower bowl and left tall segment admit the blind b alternative as well as the first c reading; two small raised remnants may be primes. The complete canceled label remains c)/b\'\') rather than resolved from its expected item sequence.'
evpron='After the looped q and flattened u are a detached apostrophe, a dotted short i and one tall l. The l returns into a long nearly flat ending with only a small dark terminal bend. A separate s body is not secure, so qu\'ils/qu\'il remains open. The visible i and single l do not supply the additional e/l sequence of H\'s elles.'
evcomma='The a/u/s/s run is compressed, followed by the dotted i, tall first t, small round o with its detached circumflex and tall second t. The low curve after the final t is connected with its foot and descends. It may include the comma read on the first pass or the terminal pen return alone; retain the word and make only the comma tentative.'
evbar='Between the two K terms the separator has an essentially upright body with a small waviness, extending from their upper height to their feet. Its endpoints have nearly the same horizontal position, whereas the slash in B06 moves visibly rightward toward its top. Retain a vertical bar here. There are no enclosing parentheses; bar/overline represents the same separate stroke over the first K.'
evgenus='The raised le/en has a loop and low return whose long continuation bends downward as the insertion leader into the gap before genre. No independent stroke traverses the raised loop. The baseline strike crosses de, genre, g and the bound. Between g and the comparison survive a low e-like cup, a flattened middle run and a short terminal upright, supporting tentative est beneath the strike. The comma below the final 1 remains uncertain in cancellation state. The isolated spot below the raised lisse lies before that word\'s right edge and away from the old comma; its location does not securely supply a further punctuation token.'
evest='The compact group following conclusion has a long low entry and return leading to a tall final loop/crossing. The initial bodies are too compressed to settle every letter, so est remains tentative. A complete longer signifie sequence is not individually traceable in that extent.'
evment='The continuation starts with a low cup and a small rise running into a long flattened stretch; a faint separate mark above it leaves m/vi unresolved. The following low e/n run and tall terminal t are visible. Keep ment/vient at this physical line start, preserving the preceding visible finale and line-end hyphen and the following au.'
c={x['id']:x for x in r['changes']}
c['P01'].update(final=r"I_{x'}\unsure{\simeq|=}T_\infty(\overline K)",evidence=evprime)
c['P10'].update(final=label,evidence=evlabel)
c['P11'].update(final=pron,evidence=evpron,confidence='medium')
c['P14'].update(final='aussitôt',evidence=evcomma,confidence='medium')
c['P16'].update(final=r'E_K=\operatorname{Gal}\overline K\mid K',evidence=evbar)
c['P20'].update(final=c['P20']['final'].replace(r'\deleted{genre $g\geq 1$}',genus),evidence=evgenus)
c['P20']['components'].append('Tentative short word est recovered between canceled g and the comparison; no extra count for the existing revision place.')
c['P23'].update(final=r'\unsure{est}',evidence=evest,confidence='low')
c['R30'].update(final=end,evidence=c['R30']['evidence']+' Blind B21 leaves m/vi at the continuation unresolved; the retained source hyphen is unchanged.',confidence='medium')
old=[x for x in r['nonmaterial_observations'] if x['id']=='P16_separator'][0]
new={**old,'id':'P16b','final':r'\mid','evidence':evbar,'against_C':True,'against_H':True,'kind':'misread symbol or index','error_category':'Symbols and indices','marked_in_H':False,'consequential':True,'confidence':'medium'}
new.pop('status',None);r['changes'].insert(r['changes'].index(c['P16'])+1,new)
r['nonmaterial_observations'].remove(old)
r['doubts']=[x for x in r['doubts'] if x['place'] not in ['P01, short raised stroke beside lower x','P16, separator in the whole Gal expression']]
for x in r['doubts']:
 if x['place']=='P10, canceled item label':x.update(reading=label,alternatives="c) | b'')",reason=evlabel)
for place,reading,alts,ev in [('P11, terminal s after qu’il',pron,"qu'ils | qu'il",evpron),('P14, terminal comma',r'aussitôt\unsure{,}','comma | connected pen return',evcomma),('P20, canceled word between g and the bound',r'\deleted{\unsure{est}}','tentative est under the strike',evgenus),('P23, word following conclusion',r'\unsure{est}','tentative est',evest),('P25/R30, physical line continuation',r'\unsure{ment|vient}','ment | vient',evment)]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=ev))
for x in r['inventory']:
 if x['element']=='E04':x['first_words_or_objects']=label
 if x['element']=='E08':x['first_words_or_objects']=r'de … genre g \unsure{est} \geq1; final comma state uncertain'
 if x['element']=='E11':x['first_words_or_objects']=r'Alors f se prolonge en une section f … finale-\newline \unsure{ment|vient} au'
for x in r['notation']:
 for a,b in repls:x['form']=x['form'].replace(a,b)
 if x['places']=='Main line 1, P01':x['meaning']='Opening inertia expression; the raised x prime is retained, while the relation remains locally uncertain.'
for x in r['hand']:
 if x['form']=='Near-vertical field separator':x['observation']=evbar;x['witness_errors']='Both witnesses give a slash; the upright bar is now a resolved local departure. H also adds enclosing parentheses.'
r['deletion_insertion_review'][0]=evlabel
r['deletion_insertion_review'][3]=evgenus
r['notes'][3]='N075_04 — Source language. The dotted i and single l of qu’ils/qu’il are retained with a tentative final s. Unaccented impliques and clair remain from the ink. The source wording is not adjusted through an identification of the two overwritten base letters.'
r['notes'].append('The independent audit confirms the raised prime by x and the upright field separator, broadens the canceled item label, marks the terminal s, comma and two compressed live words, and recovers tentative est beneath the genus cancellation. The original fixed readings and fourteen crop decisions remain in second/. No mathematical check was added.')
r['open_issues']=['Twelve local doubts remain as enumerated in doubts. The opening relation, second connector, canceled label and fragment, small raised word, old comma state, S/T chronology and newly qualified letters remain explicit. All fourteen differing blind crops were directly viewed.']
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
D['B02']=dict(final=r"I_{x'}\unsure{\simeq|=}T_\infty(\overline K),",changed=True,decision='Retain the prime and keep the relation open',evidence=evprime)
keep('B04','Retain the visible live f_K','The f has a high loop, long descending stem and returning lower hook. Its middle oval/crossing continues into the rightward crossbar. The dark retracing follows that junction; an independent canceled glyph and its strike cannot be traced separately. The low K has its own upright and right branches. No extra revision sequence is supplied.')
D['B06']=dict(final=r'$U_K$ rat/$K$,',changed=False,decision='Retain the abbreviation, slash and existing comma',evidence='The r, low a and tall crossed t end without an independent abbreviation stop. The separator tilts rightward toward its top and the following K has an upright and two branches. The comma is visible and was already present in the complete page; its inclusion here extends the first excerpt without changing the transcription. Math wrappers map to the same U_K and K.')
keep('B08','Keep the second connector doubtful','The first shaft has a full right-pointing wedge and a psi above it. The second ends in a tiny dark knot with short upper and lower projections; its separate returning arms remain merged. The arrow/dash choice therefore stays, with all three E terms and their nested U/K indices unchanged.')
D['B09']=dict(final=label,changed=True,decision='Broaden the canceled label alternatives',evidence=evlabel)
D['B10']=dict(final=pron+' soient',changed=True,decision='Leave the terminal s open',evidence=evpron)
D['B13']=dict(final=r'aussitôt\unsure{,}',changed=True,decision='Retain the word and qualify the terminal comma',evidence=evcomma)
keep('B14','Retain uncertainty under the long cancellation','The d has a low bowl and tall loop, and the apostrophe is separately raised. The low u/n bodies are crossed through their upper joins by the long horizontal strike, which conceals the transitions. Keep d\'un tentative despite the second reader\'s certain rendering.')
D['B15']=dict(final=r'E_K=\operatorname{Gal}\overline K\mid K',changed=True,decision='Resolve the separator as an upright bar',evidence=evbar)
keep('B16','Retain the complete insertion and its attachment','The raised et E_S=(1) has the same letters, index, two-bar equality and parenthesized numeral in both readings. Its long curved leader descends before the baseline closing parenthesis. The baseline comma after inertie, following point and On remain visible; the blind excerpt selects only the raised insertion. No added comma follows the raised group.')
D['B17']=dict(final=r'\deleted{de} \inserted{\unsure{le|en}} '+genus+r'\unsure{\deleted{,}|,} \inserted{$U=X\setminus T$, $X$ lisse}',changed=True,decision='Recover tentative est beneath the cancellation',evidence=evgenus)
D['B20']=dict(final=r'conclusion \unsure{est}',changed=True,decision='Qualify the compressed word after conclusion',evidence=evest)
D['B21']=dict(final=r'\unsure{ment|vient} au',changed=True,decision='Keep the line-start m/vi reading open',evidence=evment)
keep('B25','Retain the same relative-dimension numeral','The numeral has one upright and a broad lower right foot between relative and connexe. Both readings record 1; the math wrapper around it does not add a sign or alter its source position.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_c')
