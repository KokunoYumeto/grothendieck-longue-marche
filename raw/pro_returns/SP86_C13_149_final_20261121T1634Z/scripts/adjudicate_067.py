"""Root crop decisions for the fixed blind return on scan 067."""
from pathlib import Path
import json,csv
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan067';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit')
p=B/'pages'/f'{page}.tex';t=p.read_text()
pword=r'\unsure{peut|pourra|pour}';short=r'\unsure{ou|en} devra';on=r'\unsure{on|en}'
sphere=r'\deleted{``sph\unsure{è|ê}re \unsure{ar.|ari}}';var=r'\deleted{\unsure{X|x}_{\unsure{1|4}}}';last=r'\unsure{remonte|prendre|prendra}'
for a,b in [(r'\unsure{peut|pourra}',pword),('ou devra',short),('— on trouve','— '+on+' trouve'),(r'\deleted{``sphère \unsure{ar.}}',sphere),(r'\deleted{\unsure{X_1|x_1}}',var),('et on remonte comme','et on '+last+' comme')]:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t);c={x['id']:x for x in r['changes']}
pev='A deep p descender leads into a long nearly horizontal middle and a compact raised terminal with an angled return. The ending does not separate a crossed t, r or ra securely. Retain peut/pourra and the blind pour candidate; no second word or extra d ascender appears in this interval.'
sev='The opening short group consists of a dark compact first body followed by a detached flat run. Its o/e closure and u/n return remain inseparable, so ou/en stays open. The next word has a closed lower d oval and looped ascender, shallow e, angular v/r movements and a terminal a loop. These strokes retain devra; the independent decrire/deux would need a different articulation of that visible final group.'
onev='The first compact body has a curved open right edge and a dark low return; the following n-like stroke is almost horizontal. This supports on/en as local alternatives. The crop supplies visible letters for the beginning of the phrase that H leaves as one illegibility mark.'
spev='The cancellation crosses two opening quote ticks and the whole sph-word plus the short following group. The s, deep p, tall h and terminal re remain readable. The tiny detached accent above e has a dark angular apex, admitting grave or circumflex. In the following group a lower curved a-like body and low r-like run survive; the raised terminal mark can be the point in ar. or an i dot with a compressed stem. Preserve ar./ari and both accent shapes under the cancellation, without completing the word or supplying a closing quote.'
varev='The whole display contains (6), K_1, two horizontal equality strokes, Q, both parentheses and live T_1. The canceled variable has intersecting diagonal strokes that leave X/x open. Its low right numeral has a dark upright joined at the foot to a leftward horizontal stroke; the overlapping strike prevents separating a plain 1 from a small 4. Both letter and lowered numeral remain doubtful, inside the canceled group. Q and mathbb-Q map here to the same oval, internal retrace and descending tail.'
lastev='The opening has a short descending fork; several low connected humps follow before a separate small rounded body and the tall looped final ascender with a low exit. The humps favor remonte, but the initial fork and merged middle also admit the independent prendr- reading; the final exit does not securely separate e/a. Retain remonte/prendre/prendra. No grammatical continuation is used to settle it.'
for i,f,ev in [('P05',pword,pev),('P06',short,sev),('P09',on,onev),('P11',sphere,spev),('P16',r'\tag{6}K_1=Q('+var+r'\,T_1)',varev),('P21',last,lastev)]:c[i].update(final=f,evidence=ev,confidence='medium')
c['P06']['against_C']=False;c['P06']['accounting_note']='The formerly resolved C phrase is reopened at ou/en; unresolved candidate broadening is excluded from changes against C. The visible devra remains a material departure from H trois.'
boxes={x['box']:x for x in csv.DictReader((B/'second'/f'{page}_boxes.tsv').open(),delimiter='\t')}
for d in r['decisions']:
 if d['id'] in ['M1182','M1183']:
  bn='B05' if d['id']=='M1182' else 'B06';q=boxes[bn]
  d.update(decision='undecided',reading=pword if bn=='B05' else short,evidence=pev if bn=='B05' else sev,confidence='medium',crop=f'crops/{page}_{bn}_second.png ('+','.join(q[k] for k in ['x0','y0','x1','y1'])+')')
for d in r['doubts']:
 if d['place'].startswith('P05'):d.update(reading=pword,alternatives='peut; pourra; pour',reason=pev)
 if d['place'].startswith('P11'):d.update(reading=sphere,alternatives='è/ê; ar./ari within the canceled phrase',reason=spev)
 if d['place'].startswith('P16'):d.update(reading=var,alternatives='X/x; lowered 1/4, all canceled',reason=varev)
r['doubts'].extend([dict(place='P06 / M1183, line 6',reading=short,alternatives='ou/en before devra',confidence='medium',reason=sev),dict(place='P09, line 7',reading=on,alternatives='on/en',confidence='medium',reason=onev),dict(place='P21, line 19',reading=last,alternatives='remonte/prendre/prendra',confidence='medium',reason=lastev)])
r['notes'][2]=r['notes'][2].replace('peut|pourra','peut|pourra|pour')+' The following ou/en remains open after the blind audit; devra is retained from its final a and preceding v/r movements.'
r['notes'][5]=r['notes'][5].replace('et on remonte comme','et on [remonte/prendre/prendra] comme')
r['notes'].append('Blind audit reopens the canceled accent and ar./ari ending, the low 1/4 in the canceled variable of (6), the short on/en, and the final remonte/prendre/prendra. The literal vertical stroke and barred-m form remain accepted. The comma after the prose reference (6) was already present in the page text; its omission from the frozen first box excerpt is documented as a box-extent difference, with no page correction.')
for h in r['hand']:
 if h['form']=='long low e/u/n strokes':h['observation']+=' In B06 and B09 the collapsed forms leave ou/en and on/en open; the other cited longer words have additional identifying strokes.';h['scope']='These local occurrences; the p-word, two short groups and final remonte/prendre/prendra retain explicit alternatives.'
 if h['form']=='dense diagonal hatching':h['witness_errors']='H omits the low numeral in display (6), now read tentatively 1/4, and leaves the last canceled character as illegible.'
for v in r['inventory']:
 v['first_words_or_objects']=v['first_words_or_objects'].replace(r'``sphère \unsure{ar.}',r'``sph\unsure{è|ê}re \unsure{ar.|ari}').replace(r'\deleted{\unsure{X_1|x_1}}',var).replace(r'\unsure{X_1|x_1}',r'\unsure{X|x}_{\unsure{1|4}}')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
keep('B01','Retain de and both double quote marks','The looped d joins one long flat e exit ending in a single downward bend. Compare the locally visible de in B03: its flat exit has the same bend. The wider detached final s body of trous is separately articulated. Retain de, two ticks at either end, and the bold head 33. The long lower stroke belongs continuously to the g descender.')
keep('B02','Retain capital Pi and complete indexed expression','One top bar spans two straight full-height legs. The low 0, comma and 3 are followed by a parenthesized serifed I and separate comma. Both returns assign exactly these same components and attachments; only math delimiters differ.')
keep('B03','Retain the complete insertion','The raised d has a low oval and tall stroke; its e flattens into one return. Type contains tall t, descending y/p and low terminal return. The formula has 0, comma, 3, plus, card and serifed I, then closing parenthesis and comma. The long leader reaches the gap before sur. Operator braces and math delimiters map to the same formula and insertion extent in both returns.')
change('B05',pword,'Retain three p-word alternatives',pev)
change('B06',short,'Reopen the short word before devra',sev)
keep('B07','Retain aussi boucher','The first word has a small a body, flat u, two short s movements and a separate final i dot. The next begins with a tall b and small o, then low u/c, a tall h with a following shoulder, e and a long r exit. The h shoulder and final r return support boucher; all visible word bodies are preserved.')
keep('B08','Retain certains des','An open c begins the word, followed by low e/r, one tall t, a clear small a loop and separate i dot, then n/s return. Des follows with its own d loop. The c opening and internal dotted i provide the local support for certains.')
change('B09',on,'Retain on/en at the line end',onev)
keep('B10','Retain trouve donc','The opening tall t passes through a low loop/crossing and connects to a separate rising r movement. A small o, flat u, upward v and terminal e follow. Donc has its own d oval and upright, a small o and low n/c. The first ascender and following r movement support trouve.')
change('B11',sphere,'Qualify the canceled accent and ending',spev)
keep('B12','Retain projective-line expression and comma','The doubled P stem has its right bowl, an elevated 1 and a lower Q with internal stroke and tail. A separate comma follows. Braces and math delimiters in the blind return enclose the same P, elevated 1 and lowered Q with identical attachment.')
keep('B14','Retain infini','Before the large looped f there is a short upright i and a separate flat n; the initial upright ends near the baseline and carries no deep p descender. After f the dotted i, low n and final dotted i are visible. Retain the written infini without supplying an opening pro.')
keep('B15','Retain the literal vertical stroke','The complete E_K1 shows two curved E lobes, lowered K and a still lower 1. After its comma and the accented short word où is one tall straight stroke without head, foot or serifs. Encode that observed stroke as vert and assign no mathematical role. The alternatives I/1 refer to this same stroke; the literal representation retains its geometry without deciding a letter or numeral.')
change('B16',r'\tag{6}K_1=Q('+var+r'\,T_1)','Qualify the canceled lowered numeral in the full display',varev)
keep('B17','Retain typ. and its attachment','The raised group shows crossed t, a deep y and a tall p whose shoulder runs into a long flat terminal return, followed by a detached dark point. No separately articulated extra e loop is visible in that return. The curved leader runs to the gap between the visible baseline pure and de; retain their placement and the abbreviation typ.')
keep('B18','Retain barred m','The lower trace has a deep first cusp, a raised middle join and a second curved return; a separate horizontal bar spans it. Both readings attach their bar to the same low m form. Bar and overline here render the identical detached upper stroke; the two-level sign is retained unexpanded.')
keep('B19','Retain both local canceled groups and the live U expression','The first canceled character retains a tall stem/right bowl amid hatching, leaving X/P open. The live U has an open hooked entry and small right-foot loop, followed by low 0, comma, 3. Farther right a large parenthesis-like left curve is crossed by a long horizontal; the small lower loop near its middle-right and adjacent upper rounded return still support tentative qu. The blind le does not isolate a separate tall l body within that small fragment. Retain the overall graphical/canceled-parenthesis alternatives with their visible fragment.')
change('B20',last,'Qualify the compressed final verb',lastev)
keep('B22','Retain the three puncture labels','The zero is closed, the 1 is a separate upright, and infinity has two joined lobes with retracing at the middle. Two commas separate them. The math delimiters in the two returns map to this same ordered list.')
keep('B23','Retain the degree 1','The numeral has a slanted head, one main upright and a long horizontal foot. Both returns read this same 1; only the enclosing math delimiters differ.')
D['B24']=dict(final='(6),',changed=False,decision='Record the comma already present in the page',evidence='The 6 has a tall curved entry and closed lower loop, inside two parentheses. At the crop lower-right edge is the separate descending comma. The consolidated page already reads Partant de (6),. The frozen first excerpt stops at the closing parenthesis; extend only the adjudicated box reading to record the observed comma, with no change to the page file.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_b')
