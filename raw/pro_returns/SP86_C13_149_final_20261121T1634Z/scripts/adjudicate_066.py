"""Root decisions from all eighteen differing blind crops of scan 066."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan066';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text()
newphrase=r'\inserted{(\unsure{en|ou} \unsure{topos|types} \unsure{galoisiques|galoisiens})}'
newdeleted=r'\deleted{\unsure{de|des|du}}'
newinsert=r'\inserted{(plutôt sections) \unsure{du|dans}}'
newlast=r'à \unsure{isom|deux} can. près).'
for a,b in [(r'\inserted{(ou topos \unsure{galoisiens})}',newphrase),(r'\deleted{\unsure{de|des}}',newdeleted),(r'\inserted{(ou les sections) du}',newinsert),('à deux cas. près).',newlast)]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
c={x['id']:x for x in r['changes']}
gal='The first short word has a large open returning curve followed by a flattened low run, leaving en/ou. In the next word a tall t, a compressed low body, a long p-like descender and two small terminal bodies remain; the o/y and o/e bodies are not secure, so topos/types are retained. In the final word g-a-l, the crowded o/i/s region and a second dotted i can be followed. A small loop with a downward stem after that i supports q and the low u/e/s run, while retracing leaves the earlier iens reading possible. Keep galoisiques/galoisiens locally; do not complete from the subject.'
del_ev='The first loop and tall ascender support d beneath the strike. The following low body is obscured by dark horizontal cancellation, and the right terminal upright overlaps that cancellation. The visible remainder admits e, e-s and u; retain de/des/du in the locally deleted word.'
ins='The opening parenthesis is followed by a separate descending p, tall l, low u, tall crossed t, rounded o with an upper accent stroke and terminal t. These bodies read plutôt. Sections has the separate initial s, low e/c, tall t, dotted i and ons ending. After the closing parenthesis the d ascender and compressed low run admit du/dans. The thin leader reaches the gap before baseline topos; the baseline word remains live.'
last='After à, the first group begins with a short separate upright and a high curved/angled stroke, followed by a very compressed low run. That segmentation favors isom, but the formerly read angular d/e/u/x sequence cannot be excluded from the merged run. Reopen M1181 as isom/deux. The following abbreviation has open c, a small closed a and a long low n return, then a distinct dark stop: can. The separate près, closing parenthesis and stop are clear.'
c['P03'].update(final=r'\unsure{topos|types}',evidence=gal,confidence='medium')
c['P12a'].update(final=newdeleted,evidence=del_ev,against_H=False,confidence='low')
c['P12b'].update(final=newinsert,evidence=ins,confidence='medium')
c['P12c']['place']='main line 14, baseline topos following the inserted phrase'
c['P12c']['evidence']='The larger topos sits on the main baseline after the cancelled word. The thin leader above it carries the interlinear phrase and returns to the gap before this word. The insertion ends with the uncertain du/dans; baseline topos remains live.'
c['P17'].update(final=r'\unsure{isom|deux} can.',evidence=last,confidence='medium')
# Candidate broadening and alternate encodings of the same observed round mark are documented without correction counts.
for ident,field,note in [('P01','against_C','Both ce and le remain explicit alternatives; reordering or retaining them does not settle a departure from either witness.'),('P12a','against_H','The H reading des remains an explicit alternative under the same local strike; adding du does not settle a contrary word.'),('P11a','against_H','At this coordinate H superscript 0 and the selected circ encode the same small closed raised round trace. No numerical identity or distinct manuscript letter has been established; this representation choice is excluded from material totals.')]:
 c[ident][field]=False;c[ident]['accounting_note']=note
for ident in ['P01','P12a','P11a']:
 x=c[ident]
 if not x['against_C'] and not x['against_H']:
  r['changes'].remove(x);r.setdefault('nonmaterial_observations',[]).append(x)
for d in r['decisions']:
 if d['id']=='M1176':d.update(decision='undecided',reading=r'\unsure{galoisiques|galoisiens}',evidence=gal,crop=f'crops/{page}_B03_second.png',confidence='medium')
 if d['id']=='M1178':d.update(decision='other',reading='(plutôt sections)',evidence=ins,crop=f'crops/{page}_B12_second.png',confidence='high')
 if d['id']=='M1181':d.update(decision='undecided',reading=r'\unsure{isom|deux}',evidence=last,crop=f'crops/{page}_B17_second.png',confidence='medium')
for d in r['doubts']:
 if 'M1176' in d['place']:d.update(reading=newphrase,alternatives='en/ou; topos/types; galoisiques/galoisiens',reason=gal)
 if d['place']=='cancelled word after points':d.update(reading=newdeleted,alternatives='de/des/du',reason=del_ev)
r['doubts'].extend([dict(place='end of insertion before baseline topos, B12',reading=r'\unsure{du|dans}',alternatives='du/dans',confidence='medium',reason=ins),dict(place='line 17, M1181 / B17',reading=r'\unsure{isom|deux}',alternatives='isom/deux',confidence='medium',reason=last)])
for x in r['inventory']:
 s=x.get('first_words_or_objects','')
 s=s.replace('(ou les sections) du',r'(plutôt sections) \unsure{du|dans}').replace('deux cas.',r'\unsure{isom|deux} can.').replace(r'\unsure{de|des}',r'\unsure{de|des|du}')
 x['first_words_or_objects']=s
for h in r['hand']:
 if h['form']=='topos / galoisiens':h.update(form='en/ou; topos/types; galoisiques/galoisiens',observation=gal,witness_errors='C gives top.; both witnesses give a doubtful galoisiens. The complete bodies after p remain, and the word choices are qualified after the independent reading.')
 if h['form']=='short-word endings and cancellation':h['observation']=del_ev
 if h['form']=='quote strokes, stops and insertion leaders':h['observation']=h['observation'].replace('Cas.','Can.')
r['notes']=[x.replace('The stops in cas. and fini. remain.','The stops in can. and fini. remain; the preceding word is now unsure isom/deux.') for x in r['notes']]
r['notes'].append('Blind audit revises the added phrase before topos to (plutôt sections) with du/dans unresolved, broadens the crowded upper insertion and the crossed short word, and reopens M1181 while reading can. with its written stop. No mathematical assertion is used to supply the abbreviated first word. The same-source closed round superscript circ/0 correspondence is recorded without a material correction count.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
keep('B01','Retain both short-article readings','The initial letter has overlapping upper hooks and a small low e follows. The l/c body remains unresolved. Both first and second returns preserve precisely le and ce; their order changes no letter candidate. The two linked curves of the section sign map to either literal § or LaTeX S-command at this coordinate; the comma is visible.')
change('B03',newphrase,'Qualify the complete crowded insertion',gal)
keep('B04','Retain the full fundamental-datum formula','Both Gamma bodies have a tall stem and right head. Q follows the first below; two short equals bars separate it from the second. Both lower Q bodies have separate horizontal overbars; the second carries a low zero, and the slash is distinct. The second reading adds TeX grouping braces and alternative math delimiters around those same glyphs and attachments.')
keep('B05','Retain the hatted pi with 03','An angular hat, a flat pi head with two descending legs, closed small zero and open three are visible. No comma occurs between the small digits. The extra braces and math delimiters in the second return map to these same four components.')
keep('B06','Retain the extension equality','The left E has a tall spine and curved lobes; the right E is open and curved. Both lowered 03 groups are visible without commas, and the right subscript contains open U, slash and Q. Two equals bars are clear. The returns differ only in the math delimiters around those same source components.')
keep('B07','Retain the written projective-line formula','U bears a low zero, comma and three. After the two equals bars, P has doubled uprights, raised 1 and lowered Q. A straight minus precedes braces enclosing zero, comma, one, comma and a two-loop infinity; the closing brace and dark point follow. Added grouping braces in the blind TeX change no component or attachment.')
keep('B08','Retain de and the existing inserted-word alternatives','After conj. and its stop, the d has a small loop and the e ends in a flat rightward terminal, matching the earlier de within this insertion; no separate s body follows it. The last word has compressed initial and medial bodies under the leader, leaving scissions/sections. Its long lower stroke is the insertion leader; baseline sections is separate and live.')
keep('B09','Retain E03 sur Gamma_Q=Gamma','The looped E and closed zero/open three are distinct; sur has its short s, low u and right return. Each Gamma has its vertical stem and rightward top, the first carries Q and the two equals bars intervene. No added comma stands after the last Gamma. The two returns only distribute math delimiters differently around the same formula parts and the same word.')
keep('B10','Retain the observed circular superscript and closing punctuation order','The small raised mark is one closed round trace at Gamma upper-right; circ and raised 0 each map to this trace, with no numerical assertion inferred. At the right edge, the tall curved closing parenthesis follows admissibles, and the two smaller terminal quote strokes stand farther right/lower. A separate descending comma lies below the insertion end. The observed order remains parenthesis then paired quotes, followed by comma.')
change('B11',newdeleted,'Retain the three readings beneath the heavy strike',del_ev)
change('B12',newinsert,'Read plutôt and qualify the final short word',ins)
keep('B13','Retain natural in the full first B formula','The B and its lower hatted pi, explicit 0,3, separating comma and Gamma_Q are visible. The raised sign has a left oblique stem extending upward beyond the top connecting bar and a right oblique stem extending downward beyond the lower connecting bar. Both bars join the staggered ends; these observed components are retained as natural. The blind doubt does not obscure those endpoints.')
keep('B14','Retain natural in the full second B formula','The lower Gamma and Q are visible beside B. The raised sign again has two connecting bars, with only the left stem prolonged upward and only the right prolonged downward. Those staggered endpoints give the same recorded natural form, at this separate coordinate.')
keep('B16','Retain U03 of barred Q0 and the following comma','The open U carries zero and three without a comma. Inside the two parentheses, Q has a separate upper horizontal bar and a lower small zero. A separate comma follows the closing parenthesis. Extra braces in the blind TeX surround the same Q body and add no manuscript component.')
change('B17',newlast,'Reopen the first abbreviation and read can.',last)
keep('B18','Retain the inserted serifed I','The tall single upright has broad upper and lower serifs, above the main line. The neighboring curved leader descends to its attachment after fini. Math delimiters change no stroke or position.')
keep('B19','Retain the dark baseline stop after fini','The final i has a detached dot above its low terminal stroke. A second, separate dark round point stands at the baseline beyond that terminal, at the written abbreviation boundary and before the insertion. Its darkness matches the nearby writing. These are two distinct marks; the baseline one is retained.')
keep('B20','Retain the inserted Gamma and its own comma','The letter has a long upright and a rounded head returning rightward with an open lower gap; there is no closed P bowl joining the middle of the stem. Its local referent is the Gamma already written as operating on the set in the immediately preceding sentence. The separate curved comma descends before the longer insertion leader. Keep Gamma and place that comma within the insertion.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_b')
