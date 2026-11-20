from pathlib import Path
from datetime import datetime,timezone
import json,re
root=Path(__file__).resolve().parents[1]
def clean(x):
 if isinstance(x,str): return re.sub(r'\\\\(?=[A-Za-z])',lambda m:'\\',x)
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
 return x
R=clean({rn:json.loads((root/'readers'/rn/'scan004.json').read_text()) for rn in ['R1','R2','R3']})
T={rn:(root/'readers'/rn/'scan004.tex').read_text() for rn in R}
final=T['R2'].replace('précédente GF ',r'précédente \unsure{GF|CF} ')
final=final.replace(r'pre\deleted{\unsure{li|pré}}mières',r'pre\deleted{\unsure{l|li|pré}}mières')
final=final.replace(r'\mathrm{Inf}^{\leq}(F,\unsure{c|G})',r'\mathrm{Inf}^{\leq}(F,c)')
final=final.replace('pour familles infinie',r'pour \unsure{familles|famille} infinie')
final=final.replace(r'\deleted{\unsure{G|CG}}',r'\deleted{\unsure{CG|G}}')
(root/'pages/H156-01_156-7_scan004.tex').write_text(final)
# The report mappings are completed only after all three independent reports exist.
maps=json.loads((root/'records/scan004_reader_maps.json').read_text())
rows=[]
for n,src in enumerate(R['R3']['differences'],1):
 d=src.copy();d['id']=f'004-{n:02d}';d['final']=d.pop('reading');d['readers']={'R3':d['final']}
 for rn in ['R1','R2']:
  ix=maps[rn].get(str(n))
  d['readers'][rn]=R[rn]['differences'][ix-1]['reading'] if ix else maps.get('literal',{}).get(rn,{}).get(str(n),'same wording and state as C in full page transcription')
 rows.append(d)
rows[7].update(final='ensembliste), on',diff_C=False,diff_H=True,confidence='high',crop='crops/main/004_parenthesis_punctuation.png',evidence='A detached comma is visible immediately below and to the right of the closing parenthesis. R3 omitted it; the targeted crop confirms C/R1/R2.')
rows[9]['final']='premières (live letters, with internal cancelled fragment)'
rows[10].update(final=r'pre\deleted{\unsure{l|li|pré}}mières',diff_C=True,diff_H=True,kind='insertion or placement',crop='readers/R2/crops/scan004_heading.png',evidence='The live pre lies to the left of the crossing and the live mières to its right. The overwritten tall stroke lies at their junction, not as a separate prefix before the whole word. Its visible l-like stroke is preferred; li and C’s pré remain uncertain alternatives. R2 located the correction within the word; R3 retained a separately printed fragment; M preserves its medial position. The live word premières is clear.',confidence='low')
rows[12].update(final='rellation',diff_C=True,diff_H=True,confidence='medium',crop='readers/R2/crops/scan004_rellation_de.png',evidence='Two distinct rising strokes follow re before the compressed a/t sequence. M follows the doubled-l reading, while recording R3’s retained relation alternative. The literal doubled spelling is not modernised.')
rows[13].update(final='de',diff_C=True,diff_H=True,confidence='medium',crop='readers/R2/crops/scan004_rellation_de.png',evidence='The short d/e group ends in a low terminal extension without a separate s. M selects de; R3’s possible des remains documented in the reader column.')
rows[15].update(final=r'\unsure{déf|def}',diff_C=False,diff_H=True,confidence='medium',crop='readers/R1/crops/scan004_def_first.jpg; readers/R2/crops/scan004_defs.png',evidence='A short rising stroke to the left of the tall f can be read as an acute over the reduced e (R1) or as part of the compressed letter strokes (R3). R2 retains the doubt. M retains C’s déf|def, with the possible accent first; the second label is plainly unaccented.')
rows[25].update(final='c',confidence='high',crop='readers/R2/crops/scan004_b_inf.png',evidence='The second argument is a small open c, approximately half the height of F and without an internal G spur. R1/R3 resolve c; R2 retains c|G. M follows the literal small c, preserving the mismatch with the surrounding G.')
rows[27].update(final=r'\unsure{familles|famille} infinie (non vide)',diff_C=True,diff_H=True,confidence='medium',crop='readers/R1/crops/scan004_b_prose.jpg',evidence='The noun ends in a low curl after the tall l strokes, which may be es or simply e. R2 resolves familles; R1/R3 retain the singular alternative. M keeps that doubt. The following qualifiers are visibly singular, infinie and non vide, and are not changed to H’s plurals.')
rows[30]['crop']='readers/R2/crops/scan004_c_inf.png'
rows[32]['crop']='readers/R2/crops/scan004_mechise.png'
rows[33].update(final=r'\deleted{\unsure{CG|G}}',diff_C=True,confidence='low',crop='readers/R1/crops/scan004_deleted_c.jpg',evidence='A left curve and a separate right curved/horizontal group remain beneath the strike. R1 favours CG, while R2/R3 favour a retraced G. M follows CG as the first candidate, retaining G; cancellation prevents a secure unique reading.')
rows[34]['readers']={'R1':'circled a, b, c; unsure d','R2':'circled a, b; unsure c and d','R3':'circled a, b; unsure c and d'}
rows[34]['evidence']+=' R1 resolves c, but M retains the doubt because the angular interior touches and merges with the surrounding circle.'
rows[36].update(H='pour ≤ et pour ≪, followed by a point',final='(pour ≤ et pour ≪), with no terminal point',evidence='A parenthesis opens before pour and closes after the final ≪. No separate terminal point is visible; H omits the parentheses and supplies a point.')
rows[22]['marked_in_H']=True
rows[23]['marked_in_H']=True;rows[23]['kind']='omission'
# Additional punctuation and underlining loci in the exact H page.
def add(place,C,H,reading,evidence,kind='other',conf='high',crop=None,rs=None):
 n=len(rows)+1
 rows.append(dict(id=f'004-{n:02d}',place=place,C=C,H=H,final=reading,readers=rs or {rn:reading for rn in R},diff_C=False,diff_H=True,kind=kind,marked_in_H=False,confidence=conf,evidence=evidence,crop=crop))
add('two lower marginal NB headings',r'\uline{NB}', 'NB without underline',r'\uline{NB}','The tilde-intersection note and the lower existence note each have a separate rule under NB. The first crossed Question/NB replacement is recorded separately.')
for q in ['engendrée','réunion','somme','intersection fine']:
 add('quotation pair around '+q,"``…''",'« … »',"``…''",'Raised paired strokes enclose the term; no angled guillemets are drawn. The underlines are separately recorded.')
add('opening, after set letter L',r'L \deleted{…}',r'\mathcal L, \struck{ce}',r'L \deleted{…}','Between the foot of L and the crossed token there is no comma. The letter-alphabet and deleted-token decisions are separate.',crop='readers/R2/crops/scan004_L_deleted.png')
add('data definitions, end of each relation description','figures / raffinement followed by a new formula line','figures, / raffinement,','figures / raffinement followed by a new formula line','Each verbal relation description is followed by its definition on a separate line, with no comma written at the line ending. H adds commas in converting the brace into inline list prose.')
for ix in [21,28,36,43,46,48]:
 d=R['R1']['differences'][ix-1]
 add(d['place'],d['C'],d['H'],d['reading'],d['evidence'],d['kind'],d['confidence'],d.get('crop'))
add('set letter in both marginal Fig operators',r'\mathrm{Fig}(L)',r'\mathrm{Fig}(\mathcal L)',r'\mathrm{Fig}(L)','The first-occurrence L|calligraphic L doubt governs these repeated occurrences. The transcription uses its first candidate consistently; the script distinction is not newly resolved here.',conf='medium')
# All twenty C doubts, including resolved ones, are kept in an explicit audit.
values=[r'\unsure{GF|CF}',r'\unsure{L|\mathcal L}',r'\deleted{\unsure{ou|de}}',r'pre\deleted{\unsure{l|li|pré}}mières','premières',r'\unsure{\mathscr F|\mathcal F}','rellation','de',r'\unsure{déf|def}',r'\unsure{\}|)}',r'\deleted{Question}','c','(',r'\unsure{familles|famille}','temps',r'\unsure{C|G}',r'\unsure{mechisé|méchisé}',r'\unsure{c}',r'\deleted{\unsure{CG|G}}',r'\unsure{d}']
kept={0,1,2,3,5,8,9,13,15,16,17,18,19};changed={3,9,13,16,18}
audit=[];unresolved=[]
for i,a in enumerate(R['R2']['C_doubt_audit']):
 status='changed reading/placement; retained' if i in changed else ('retained' if i in kept else 'resolved')
 audit.append(dict(place=a['place'],C=a['C_reading'],status=status,final=values[i],evidence=a['crop']+'; see the corresponding main decision above.'))
 if i in kept:
  unresolved.append(dict(place=a['place']+': '+a['C_reading'],reading=values[i],alternatives='Explicit alternatives are retained in the reading; no further letters securely recoverable.',confidence='low' if i in {2,3,9,16,17,18,19} else 'medium',reason='Overwriting, crossed strokes or the letter’s shape prevents a unique reading.' if i not in {1,5} else 'Handwritten alphabet does not uniquely distinguish the typographic font.'))
inv=[('text','top centre','3'),('text','upper paragraph','(et je suis resté muet sur ce support'),('deletion','upper paragraph after L',r'\unsure{ou|de}'),('text','underlined heading','Données premières'),('deletion','inside premières, after pre',r'\unsure{l|li|pré}'),('display','left-braced data block','script F; ≤; ≪; two definitions'),('text','above At 0 display','avec'),('display','middle, labelled At 0','F≤G ⇒ F≪G'),('margin note','left, oblique beside At 0','NB. Ce sera aussi contenu'),('text','below At 0','— axiome si évident'),('display','row a of the table','circled a; F∨G ou F∪G; figure engendrée'),('margin note','left beside row a','Si (F,G) ont un sup pour ≪'),('deletion','start of preceding note','Question'),('insertion','above preceding cancellation','NB.'),('margin note','left between rows a/b','NB tilde(F∩G)=tilde F∩tilde G'),('display','row b of the table','circled b; F∧G ou F∩G; Inf≤(F,c)'),('insertion','above intersection in row b, with connector','ou Inf pour ≤'),('margin note','left beside row c','NB Existe dans le cas ensembliste'),('display','row c of the table','circled unsure c; F.G; Inf≪(F,c)'),('deletion','below row-c formula',r'\unsure{G|CG}'),('display','row d of the table','circled unsure d; empty figure')]
now=datetime.now(timezone.utc)
rec=dict(scan=4,decided_utc=now.strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=rows,C_doubt_audit=audit,unresolved=unresolved,inventory=[dict(kind=k,position=p,first_words_or_objects=v) for k,p,v in inv],notation=[
 dict(sign='Set of lieux',latex=r'\unsure{L|\mathcal L}; L',evidence='004, opening and Fig(L) margins: long rising stem with a looped foot. Plain L is the first candidate; alphabet doubt marked at first occurrence.',status='recurring alphabet doubt'),
 dict(sign='Set of figures',latex=r'\unsure{\mathscr F|\mathcal F}; \mathscr F',evidence='004, brace and empty-figure row: looping top, long curved descender and short middle cross-stroke. Not the angular Gothic F of H.',status='recurring alphabet doubt'),
 dict(sign='Inclusion and refinement',latex=r'\leq; \ll',evidence='004: a single angle with a lower bar versus two separate left-pointing angles; both also occur as Inf superscripts.',status='settled'),
 dict(sign='Small multiombre and support',latex=r'\mathrm{mulomb}(F);\mathrm{omb}(F)',evidence='004 opening: both initial letters lowercase; mulomb has no t. Distinct from scan 003’s uppercase operators.',status='settled'),
 dict(sign='Infimum second argument',latex='c',evidence='004 rows b/c: small open c-shaped sign, without internal G spur; literal mismatch with surrounding G preserved.',status='literal manuscript discrepancy'),
 dict(sign='Barred m and equality-sign abbreviation',latex=r'\overline{\mathrm m}; en $=$ temps',evidence='004 row b: short rule directly above m; two equal horizontal strokes before temps.',status='settled')],
 abbreviations=[dict(form='ens.',meaning='ensemble',location='004, opening'),dict(form='def',meaning='définition',location='004, both equivalence labels, unaccented'),dict(form='At',meaning='atelier axiom label',location='004, At 0 and At 4 reference'),dict(form='tjrs',meaning='toujours',location='004, left supremum note'),dict(form='néc.',meaning='nécessairement',location='004, same note'),dict(form='barred m',meaning='même',location='004, row b'),dict(form='en = temps',meaning='en même temps',location='004, row b'),dict(form='Inf',meaning='infimum',location='004, rows b/c')],
 notes=[
 '**Statement 004-N1.** The page distinguishes the lowercase interpretations mulomb(F) and omb(F), then gives the set of figures and the two relations, inclusion ≤ and refinement ≪. At 0 states F≤G ⇒ F≪G. Its oblique note reads “Ce sera aussi contenu dans At 4 plus bas”. These are read as data and assertions, not independently proved (Grothendieck, 1986, scan 4).',
 '**Statement 004-N2.** Rows a–d describe the union/sum as a ≤ supremum (when it exists), ordinary intersection as a ≤ infimum, fine intersection as a ≪ infimum (when it exists), and the empty figure as least for both relations. The marginal note says a ≪ supremum need not be a ≤ supremum. The compatibility and existence assertions have not been independently established from this page’s preliminary data.',
 '**Reading decisions prompted by mathematics.** The connector of “ou Inf pour ≤” lands after intersection in row b; H attached it to row a. Both displayed Inf formulas have a small c as second argument, despite the surrounding G notation. Their literal c is retained; the open capital in F∨C remains C|G. The different Inf superscripts, ≤ and ≪, are clearly distinct. The final marginal case-name is retained as mechisé|méchisé, without substituting H’s rectiligne or inferring a term from its mathematical use.',
 '**Literal irregularities.** Rellation has a doubled l. The noun remains familles|famille; the following qualifiers are visibly singular, “infinie (non vide)”. The closure after “quand il existe” is brace-like and remains }|). The medial correction in premières is not expanded into a reconstructed preliminary heading. None of these is repaired in the transcription.',
 '**Qualifications and dating.** “quand il existe”, “quand elle existe”, and “ce n’est pas néc.” qualify the assertions. The note promises that At 0 will be contained in At 4; it is not a proof on this page. No new date or title is present; manuscript page 3 is visible.'
 ],check_events=[dict(statement_id='004-N1',date=now.date().isoformat(),who='M; GPT-6 Astra Pro; effort not exposed; SP35 run',type='carried as background without fault found',outcome='Definitions and At 0 transcribed; no independent implication proof claimed.'),dict(statement_id='004-N2',date=now.date().isoformat(),who='M; GPT-6 Astra Pro; effort not exposed; SP35 run',type='carried as background without fault found',outcome='Order-theoretic descriptions, existence and compatibility claims read as the author’s assertions; no theorem check claimed.')],main_images_viewed=['whole','half a','half b']+[x['file'] for x in json.loads((root/'readers/R2/scan004_crops.json').read_text())]+['readers/R1/crops/scan004_heading.jpg','crops/main/004_parenthesis_punctuation.png'])
rec['main_images_viewed'] += ['readers/R1/crops/scan004_def_first.jpg','readers/R1/crops/scan004_label_c.jpg','readers/R1/crops/scan004_deleted_c.jpg','readers/R1/crops/scan004_rellation.jpg','readers/R1/crops/scan004_b_prose.jpg']
(root/'records/scan004.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
