"""Root adjudication after direct viewing of every differing scan 073 crop."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1]; page='149_scan073'
rp=B/'reviews'/f'{page}.json'; r=json.loads(rp.read_text()); assert not r.get('audit')
p=B/'pages'/f'{page}.tex'; t=p.read_text()
les=r'\unsure{Les|\deleted{Les}|\uline{Les}}'
idx=r'E_{U_{\unsure{\eta|K|\kappa}}}'
prep=r'\unsure{sur|dans|\deleted{dan}\unsure{s|\deleted{s}}}'
prefix=r'\unsure{s.|s-}groupe'
ox=r'\unsure{O_x|\underline O_x|\underline U_x}'
pi=r'\unsure{\pi|\Pi}_1'
sep=r'U_S\unsure{/|\mid}S'
repls=[('(Les ', '('+les+' '),(r'E_{U_{\unsure{\eta|K}}}',idx),(r'\unsure{sur|dans}',prep),(r'\unsure{s.}groupe',prefix),(r'\unsure{O_x|\underline O_x}',ox),(r'\pi_1(\operatorname{Spec}',pi+r'(\operatorname{Spec}'),('U_S/S',sep)]
for old,new in repls:
 assert t.count(old)==1,(old,t.count(old)); t=t.replace(old,new)
p.write_text(t)
evles='One Les is traceable after the parenthesis. The heavy lower stroke continues from the tall L foot beneath the e/s, while a further dark crossing touches their lower bodies. Its attachment permits the L foot, an underline, or partial cancellation; no second independent Les is visible. The following relèvements retains its initial returning r, small e, tall l, accented e, low v and compressed ending. The raised canceled dernier(s) and its curved leader remain separately recorded.'
evidx='The small index below U has a short left upright, a joined rounded upper turn and a short descending right return. The crossing that would settle a K branch is merged with that turn. The eta, K and kappa readings remain open at this occurrence. The separately written E_K to the right has its own stem and joined angle.'
evprep='The single cluster has a tall d-like upright, a small adjacent oval and densely retraced low middle strokes. The final s-like cup is slightly separated at the right. A thick transverse stroke passes through the middle, leaving a canceled dan with a live or canceled s as an additional reading. Sur/dans and the revision state remain unresolved; no sequence of two complete words or revision chronology is asserted.'
evmargin='The marginal prefix is crossed by the q descender from quotient; a small point and short low dash-like stroke precede the clear g loop and groupe. Keep s./s- open. The cap above I remains slightly separated from its upright, preserving the serif/overbar doubt. In the last formula the pi-shaped sign has a long upper bar and two descending stems; their straight, compact shape leaves pi/Pi open. The final O/U contour has an open top and low returning stroke, so both its letter and underline remain uncertain. The first O underline, NB underline, Le quotient and final unpunctuated closing parenthesis remain visible.'
evsep='The separator after the lowered S is a tall, nearly upright stroke with a small rightward tilt toward its top. It supplies too little slant to settle slash versus vertical bar. Preserve both graphic readings. The blind excerpt includes the following est; that word was already present in the page text.'
c={x['id']:x for x in r['changes']}
c['P08a']['final']=les+r' \inserted{\deleted{\unsure{derniers|dernier}}} relèvements'
c['P08a']['evidence']=c['P08a']['evidence'].replace('live Les','single Les')
c['P08b'].update(final='('+les,evidence=evles,confidence='low')
c['P15a'].update(final=prep,evidence=evprep)
c['P21d'].update(final=prefix,evidence=evmargin)
for d in r['decisions']:
 if d['id']=='M1201':d.update(reading=prep,evidence=evprep)
 if d['id']=='M1203':d.update(reading=prefix,evidence=evmargin)
 if d['id']=='M1205':d.update(reading=ox,evidence=evmargin)
for d in r['doubts']:
 if 'nested index' in d['place']:d.update(reading=idx,alternatives=r'\eta | K | \kappa',reason=evidx)
 if 'M1201' in d['place']:d.update(reading=prep,alternatives='sur | dans | canceled dan with live/canceled final s',reason=evprep)
 if 'M1203' in d['place']:d.update(reading=prefix,alternatives='s. | s-',reason=evmargin)
 if 'M1205' in d['place']:d.update(reading=ox,alternatives=r'O_x | \underline O_x | \underline U_x',reason=evmargin)
for place,reading,alternatives,ev in [('main line 5, single Les',les,'live | canceled | underlined',evles),('oblique note, pi-shaped sign',pi,r'\pi | \Pi',evmargin),('main line 13, separator in U_S/S',sep,'slash | vertical bar',evsep)]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence='low',reason=ev))
for e in r['inventory']:
 if e['element']=='E08':e.update(first_words_or_objects=prep+' I_x')
r['inventory'].insert(6,dict(element='E11',kind='deletion',position='possible cancellation of the single baseline Les; [1110,1220,1595,1395]',first_words_or_objects=les,sheet_kind='text',hand='his hand',transcribed='yes'))
r['inventory'].insert(9,dict(element='E12',kind='deletion',position='possible canceled dan(s) within the one overwritten preposition; [1050,1945,1325,2060]',first_words_or_objects=prep,sheet_kind='text',hand='his hand',transcribed='yes'))
for h in r['hand']:
 if h['form']=='K / eta-like small index':h['observation']=evidx;h['witness_errors']='The C eta / H K readings remain unresolved together with the blind kappa alternative; no index departure is counted.'
 if h['form']=='overwritten preposition':h['observation']=evprep;h['witness_errors']='The single cluster retains candidate readings and revision states; no two-word sequence is reconstructed.'
 if h['form']=='q descender crossing marginal prefix':h['observation']=evmargin
 if h['form']=='ordinary U':h['witness_errors']='Each observed U form remains documented in the nonmaterial observations; the wrapper mapping contributes no material count.'
for k in ['notation','nonmaterial_observations']:
 for x in r[k]:
  for key in ['form','final']:
   if key in x:
    for old,new in repls:x[key]=x[key].replace(old,new)
  if x.get('id')=='P10u':x.update(evidence=evidx,confidence='low')
  if x.get('id')=='P25u':x.update(evidence=evsep,confidence='low')
r['notes']=[s.replace('The live Les is written once.','One Les is written; its live, canceled or underlined state remains open.').replace('The ordinary U observations are recorded per source occurrence in the change log.','The ordinary U observations are recorded per source occurrence in the nonmaterial observations.') for s in r['notes']]
r['notes'].append('The fixed blind audit broadens the single Les state, nested eta/K/kappa index, overwritten preposition, marginal prefix and final letter/decoration, pi/Pi form, and near-upright U_S/S separator. These unresolved alternatives add no material departure counts. See the explicit crop adjudications for the literal stroke mappings of every differing encoding. No mathematical verification was added.')
r['deletion_insertion_review'][1]=r['deletion_insertion_review'][1].replace('live Les','single Les')
r['deletion_insertion_review'][2]=evles
r['deletion_insertion_review'][4]=evprep
r['open_issues']=['Nine local doubts remain; each is listed with its current reading and stroke evidence in doubts. All twenty differing blind crops were directly viewed and adjudicated.']
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
keep('B02','Retain the mapped diagram (9)','The five upper objects and four lower objects are joined by four upper horizontal, three lower horizontal and four vertical unheaded strokes. Each no-head r/d encoding and blind dash encoding connects those same endpoints. Bar/overline marks the same top stroke over K; grouping braces preserve the same O-only underline and lower x. Both wrappers record the written (9), without adding a source object or connector.')
keep('B03','Retain diagram (10) and its label side','The six objects, four leftward horizontal arrows, three downward arrows and dashed lower-right to upper-middle arrow map one for one in both encodings. Phi_x is above/right, northeast of the dashed up-left shaft. The apostrophe in the retained tikzcd label option places that label on this observed side. Formula wrappers and O-only grouping braces change no object or endpoint.')
keep('B04','Retain capital L and no stop','The initial has a tall straight upright and broad rightward foot, followed by a detached apostrophe and tall h. The low o/m run has no detached final point. These strokes retain the written L\'hom.')
keep('B05','Retain the headless connector','The single horizontal shaft ends in a rounded dark cap with a tiny upper kink. There is no lower return paired into a head. Both terms retain the same E, K, U and O_x nesting; math delimiters add no source sign.')
keep('B07','Retain the hat and headless connector','Two peaked inner slopes touch the upper E lobe and remain independently traceable. The following shaft ends with a single upturned cap and no paired lower wing. The point after the right E_U_S remains separate. Grouped E in the blind encoding refers to the same hatted letter.')
D['B08']=dict(final='('+les+r' \inserted{\deleted{\unsure{derniers|dernier}}} relèvements',changed=True,decision='Qualify the state of the single Les',evidence=evles)
keep('B09','Retain the same abbreviation and raised t','The b, dotted i, low u/n, second i and v are followed by a point and a separate raised crossed t. Superscript math t and textsuperscript t map to that same raised letter. Aux is separately present.')
D['B10']=dict(final=idx+' sur E_K',changed=True,decision='Keep eta, K and kappa open',evidence=evidx)
keep('B11','Retain raised t and lowered s','After ou aux, the r/e run joins a tall looped l. The t lies above that baseline. The following small s starts lower and extends beneath the rel baseline; it is preserved as a lowered s rather than placed at the rel baseline.')
keep('B12','Retain the single unheaded connector','The shaft between E_K and E_S has a flat run and one short downward cap at its right end. No upper wing returns into a point. The split K stem and two diagonals and the lower S are independently visible.')
keep('B13','Retain the headless segment, three dots and closing parenthesis','The horizontal segment has rounded ends with no separate paired head. E, K, U and lower S are visible. The three detached dots and closing parenthesis map exactly to the retained ldots and closing parenthesis; the blind math wrapper adds no source mark.')
D['B14']=dict(final=prep+' I_x',changed=True,decision='Retain unresolved reading and cancellation alternatives',evidence=evprep)
keep('B15','Retain the O-only underline','The nested O_x after U has no separate underline. The final O after sur has a detached lower stroke ending before x. Grouped underline{O} and underline O both attach that stroke to O alone, and both math wrappers enclose the same letters.')
keep('B17','Retain corresp. with raised t and separate star','The c/o, two r returns and flattened e/s run lead into the clear p descender. A detached point follows p, followed by a long-entry raised t. No additional baseline o/n/d bodies occur after p. A separate multi-ray star lies farther right; its intersecting rays remain distinct from the raised letter.')
keep('B18','Retain impliquera','The q descender returns into the low u; the subsequent e return, separate r rise and final small a loop continue to the right. Those final bodies are present before the paper edge, preserving the full era ending without a final stop.')
margin=t.split('\\margin{\\uline{NB} ',1)[1].split('\n\\margin{72}',1)[0][:-1]
D['B19']=dict(final=r'\uline{NB} '+margin,changed=True,decision='Broaden the local marginal glyph doubts',evidence=evmargin)
keep('B21','Retain the leftward arrow','The left end of the shaft has two returns converging into one left-pointing tip. The right term has E and nested U_S; the left term has E_K. The blind math wrapper encloses exactly these source signs.')
keep('B22','Retain the rightward arrow','The horizontal shaft has a detached right-pointing head with two converging returns. E_K lies to the left; E with nested U and O_x lies to the right. Both encodings preserve these terms, indices and one head.')
D['B23']=dict(final=sep,changed=True,decision='Leave the near-upright separator open',evidence=evsep)
keep('B24','Retain the same phi_x formula','The phi has a long descending stem and looped upper body, followed by lower x and two distinct colon points. E_K is joined to E_U_Ox by one right-pointing head. The short upper shaft kink supplies no second paired head. The blind delimiters preserve this same formula.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_b')
