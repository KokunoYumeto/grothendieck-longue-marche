"""Crop-adjudicated scan014 decisions. Never rerun after commitment."""
import copy,json,re
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan014.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan014/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
m1=[0,1,2,3,4,6,7,8,None,10,11,12,9,13,13,13,13,14,19,15,16,17,18,19,20,21,23,24,24,25,26,27,28,29,30]
m3=[0,1,2,3,4,5,6,7,None,8,9,10,11,12,14,14,14,15,21,16,17,18,19,20,22,23,24,25,25,26,27,28,29,30,31]
rows=[]
for i,x in enumerate(b):
    r=copy.deepcopy(x);r['final']=r.pop('reading');r['mathematical']=False
    for k in ['crop_box','crop_source']:r.pop(k,None)
    r['readers']={'R1':a[m1[i]]['reading'] if m1[i] is not None else "d'après",
                  'R2':x['reading'],'R3':c[m3[i]]['reading'] if m3[i] is not None else "d'après"}
    rows.append(r)
def rp(reader,name):return f'readers/scan014/{reader}/'+('crops/' if reader!='R3' else '')+name+'.jpg'
def main(name):return f'crops/scan014/{name}.jpg'
def put(i,**kw):rows[i].update(kw)
notes=(O/'working/scan014_main_crop_notes.md').read_text()
viewnotes={}
for rel,body in re.findall(r'^## \d+ — ([^\n]+)\n\n(.*?)(?=\n## |\Z)',notes,re.M|re.S):
    viewnotes[rel]=re.sub(r'^Recorded [^.]+\. ','',body.strip())
def evidence(i,crop,extra=''):
    put(i,crop=crop,evidence=viewnotes[crop]+(' '+extra if extra else ''))
evidence(0,main('01_opening_comme'))
evidence(1,rp('R3','01_optima'))
evidence(2,rp('R3','02_definir'))
evidence(3,rp('R3','03_family_f'))
evidence(4,main('02_capital_Soit'))
evidence(5,rp('R3','05_compatibility_display'))
glyph=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]{\draw (-.38,.62)--(.28,.20)--(-.45,-.20); \draw (.35,.52)--(-.30,.18)--(.34,-.18); \draw (-.38,.62)--(-.40,.50)--(.28,.20); \draw (-.30,.18)--(-.42,.08)--(.32,-.14)--(.34,-.23);}}'
put(5,final=glyph,against_C=True)
for i in [6,7,8]:evidence(i,rp('R3','04_right_note'))
put(8,evidence='The apostrophe is distinct, but no separate grave accent can securely be assigned to the reduced e. Retain d_apres/d_après, unaccented first, as R2, rather than silently normalizing C/R1/R3/H. The earlier main note used acute generically; the actual disputed accent is a grave.')
for i in [9,10]:evidence(i,rp('R2','06_definition_initial_sign'))
evidence(11,main('04_ou_encore'))
evidence(12,main('05_brace_scope'))
for i in [13,14,15,16]:evidence(i,rp('R3','07_slanted_note'))
put(16,place='Slanted note: relation-dependence clause',against_C=False,
    final=r'$\ll$ soit déterminé ainsi en termes de $\leq,\preccurlyeq$, mais plutôt que $\preccurlyeq$ est déterminé par $\ll,\leq$',
    evidence='The entire clause and each order sign are recoverable: ll, then leq/preccurlyeq, then preccurlyeq, finally ll/leq. The last verb is est, not H’s et. No terminal point follows the last leq. H’s partly illegible continuous span is kept together to avoid invented token correspondences. The comma after the first pair is a separate unresolved locus below.')
evidence(17,main('06_Cela_correspond'))
put(17,h='correspondant (inside H’s bare editorial brackets)',evidence='The large C and separate l loop give Cela; the following word has a p descender and terminal ascending d, giving correspond. H omits Cela and changes the verb ending. Bare H brackets are considered separately as possible editorial grouping, not included in this lexical error count.')
evidence(18,main('09_et_intuitif'))
evidence(19,main('07_centre'))
evidence(20,main('08_gravite'))
for i in [21,22]:evidence(i,rp('R3','08_conceptuel_geometrique'))
put(21,final=r'\deleted{\unsure{conceptuel}}',against_C=False,confidence='medium')
evidence(23,main('09_et_intuitif'))
evidence(24,main('10_sur_la'))
evidence(25,main('11_que_sur'))
evidence(26,main('12_cela'))
for i in [27,28]:evidence(i,main('13_mettre_des'))
evidence(29,main('14_surnombre'))
evidence(30,main('15_de_partir'))
evidence(31,main('16_qui'))
evidence(32,rp('R3','09_tantot'))
evidence(33,main('17_body_compatibility'))
evidence(34,main('18_terminal_comma'))
frame=copy.deepcopy(a[5]);frame['final']=frame.pop('reading')
for k in ['crop_box','crop_source']:frame.pop(k,None)
frame.update(final='Enclosure with three gaps: upper left, upper right and lower right; left and bottom joined.',
             crop=main('03_pair_enclosure'),evidence=viewnotes[main('03_pair_enclosure')],
             readers={'R1':a[5]['reading'],'R2':'Closed box in reading.tex','R3':'Closed box in reading.tex'},
             against_C=True,against_H=True,mathematical=False,confidence='high')
reflex=copy.deepcopy(a[22]);reflex['final']=reflex.pop('reading')
for k in ['crop_box','crop_source']:reflex.pop(k,None)
reflex.update(crop=rp('R1','09_transitivite_reflexivite'),evidence=viewnotes[rp('R1','09_transitivite_reflexivite')],
              readers={'R1':a[22]['reading'],'R2':'réflexivité','R3':'réflexivité'},mathematical=False)
comma=dict(place='Slanted note: comma after first leq/preccurlyeq pair',c=r'$\leq,\preccurlyeq$,',
           h='Punctuation not securely aligned in the partly illegible marginal span',
           final=r'\unsure{$\leq,\preccurlyeq$,|$\leq,\preccurlyeq$}',
           against_C=True,against_H=False,kind='other',marked_in_H='yes',confidence='medium',
           crop=rp('R3','07_slanted_note'),mathematical=False,
           evidence='A short oblique lies beside a descending stroke from the line above. Its assignment as an independent comma is not secure. Retain comma/no-comma, comma first; syntax does not settle the conflicting reader returns.',
           readers={'R1':r'$\leq,\preccurlyeq$,','R2':r'$\leq,\preccurlyeq$','R3':r'$\leq,\preccurlyeq$,'})
bracket=dict(place='H bare square brackets around first lower phrase',
             readers={'R1':'No brackets in reading.tex','R2':'No brackets; counted as non-ink text','R3':'No square brackets'},
             final='No brackets in diplomatic text; do not count H’s possible editorial grouping as an established ink-reading error.',
             crop=main('09_et_intuitif'),
             evidence='Local crops 06 and 09 show no independent opening/closing square-bracket pair. The apparent long final upright belongs to f in intuitif. H uses bare square brackets here; its explicit supplied/note conventions do not settle this bare-bracket intention. The lexical differences within the span are recorded separately. This is an editorial-markup adjudication, not a substantive H-error row.')
ordered=rows[:5]+[frame]+rows[5:17]+[comma,rows[17]]+rows[19:26]+[reflex]+rows[26:]
assert len(ordered)==37
for i,r in enumerate(ordered,1):r['id']=f'014-{i:02}'
tex=(O/'readers/scan014/R1/reading.tex').read_text()
old=r'\draw ([xshift=1pt]pair.north west)--(pair.north east)--(pair.south east)--(pair.south west)--([yshift=-2pt]pair.north west);'
new=r'\draw ([xshift=1pt]pair.north west)--([xshift=-1pt]pair.north east); \draw ([yshift=-1pt]pair.north east)--([yshift=1pt]pair.south east); \draw ([xshift=-1pt]pair.south east)--(pair.south west)--([yshift=-2pt]pair.north west);'
assert old in tex;tex=tex.replace(old,new)
tex=tex.replace("pas, d'après nouveau",r"pas, \unsure{d'apres|d'après} nouveau")
tex=tex.replace(r'en termes de $\leq,\preccurlyeq$, mais',r'en termes de \unsure{$\leq,\preccurlyeq$,|$\leq,\preccurlyeq$} mais')
(O/'decisions/scan014_final.tex').write_text(tex)
cd=copy.deepcopy(rs[2]['c_doubts'])
links=[1,2,3,6,7,13,14,15,21,32]
for j,i in enumerate(links):
    r=rows[i]
    reading=r['final']
    if j==5:reading='changerai'
    if j==6:reading='pt'
    if j==7:reading=r'\unsure{supposerai}'
    cd[j].update(reading=reading,evidence=r['evidence'],crop=r['crop'],disposition='resolved' if j in [1,4,5,6,9] else 'retained')
    for k in ['crop_box','crop_source']:cd[j].pop(k,None)
inv=copy.deepcopy(rs[0]['inventory'])
inv[2]['first_words_or_objects']='Soit par; leq,ll in a three-gap frame; leq,preccurlyeq; ll,retraced compatibility'
inv[3]['first_words_or_objects']="Non, sa/ça ne suffira pas, d'apres/d'après nouveau point de vue ..."
notes={
 'content':' '.join(rs[0]['notes']['content']),
 'math_reading_decisions':[
 'Only the opening family F has a returning foot and a printed-alphabet doubt. Each ordinary G/F and both high-right F primes in (1.29) are individually distinguished by the independent readers; no extra family-font alternatives are assigned to ordinary operands.',
 'The first pair’s enclosure has three gaps. The upper compatibility occurrence has reinforced branches; the lower occurrence is an unreinforced pair of opposed zigzags. Their geometry is reproduced locally in TikZ without changing relational meaning.',
 'The heavy double chevron in (1.29) is live retracing. Est is on the baseline, and the brace groups all three lines of the definition. These displays are aligned definitions/lists, not diagrams.',
 'The marginal note reads page 20, not a date, and separates its text from the nearby (1.29) label. Its compressed supposerai and the comma after the first relation pair remain uncertain.',
 'Literal reflexivity is preserved, with an initial-accent doubt, and surtout is inserted before de. S’s proposed replacement by antisymmetry is not established by this page and is not adopted.',
 'A targeted conditional proof was performed: assuming both leq and preccurlyeq are reflexive, choose the intermediate F prime equal to F in (1.29). Then F leq F and F preccurlyeq F imply F ll F. This proves only that conditional assertion, not the assumptions from atelier axioms or the author’s intended correction.',
 'The generated-preorder equivalence, transitivity of the composite, the alternative primitive-relation descriptions and the historical C8_0/antisymmetry claim were read but not mathematically verified.',
 'H’s bare square brackets around the first lower phrase are absent from the manuscript transcription, but their possible editorial intention is not counted as an established ink-reading error. H is credited for explicitly marking the struck adjective, its replacement and surtout.'
 ],
 'author_doubts':[
 r"Non, \unsure{sa|ça} ne suffira pas, \unsure{d'apres|d'après} nouveau point de vue ...",
 r"Je changerai le pt de vue page 20, et ne \unsure{supposerai} plus que ...",
 'il semblerait que ce soit de partir de ≤,≪ qui soit le plus simple',
 "c'est plutôt une curiosité qu'autre chose,"
 ],
 'titles_dates_counts':'Manuscript page 13; labels (1.28) and (1.29); forward reference page 20. No title, explicit calendar date, page count or archive pencil sheet number is identified. H’s June dating is editorial inference and does not enter the transcription.'
}
events=[]
for i,r in enumerate(rs,1):
    for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan014 R{i}'))
for sid in ['scan014-(1.28)','scan014-(1.29)-generated-preorder-equivalence','scan014-transitivity-and-axiom-burden','scan014-S-SA21-K6-02-historical-antisymmetry-correction']:
    events.append(dict(statement_id=sid,type='carried as background without fault found',outcome='Read as the author’s or supplied sweep’s assertion; no mathematical verification of this claim was performed.',who='GPT-6 Astra Pro; effort not exposed; main reader; scan014'))
events.append(dict(statement_id='scan014-(1.29)-conditional-reflexivity',type='targeted proof check',
 outcome='Assume both leq and preccurlyeq are reflexive. For any F choose F prime=F; F leq F and F preccurlyeq F establish F ll F by the displayed existential definition. The constituent-reflexivity assumptions were not derived from atelier axioms. No antisymmetry correction, historical C8_0 claim, generated-preorder equivalence or transitivity claim was proved. Working note: working/scan014_math_checks.md.',
 who='GPT-6 Astra Pro; effort not exposed; main reader; scan014'))
s=[dict(id='SA21-K6-02',disposition='partly confirmed',reading=r'de transitivité et \inserted{surtout} de \unsure{reflexivité|réflexivité} pour $\ll$; conditional reflexivity proved, antisymmetry replacement unverified.',
 evidence='Main local crop confirms the reflexivity lexeme and inserted surtout; the initial acute remains uncertain. The choice F prime=F proves reflexivity under explicit constituent-reflexivity assumptions. This does not establish S’s historical/axiomatic proposal to replace the word by antisymmetry.',
 crop=rp('R1','09_transitivite_reflexivite'))]
un=[dict(place=r['place'],reading=r['reading'],alternatives='As marked in the diplomatic transcription; single-candidate doubts have no securely recovered alternative.',confidence='medium',evidence=r['evidence']) for r in cd if r['disposition']=='retained']
for r in [rows[8],rows[22],reflex,comma]:
    un.append(dict(place=r['place'],reading=r['final'],alternatives='As explicitly marked in the transcription.',confidence='medium',evidence=r['evidence']))
assert len(un)==9
d=dict(scan=14,mspage='13',folder='J156-6-02',filename='J156-6-02_156-6_scan014.tex',brief='v007',committed=False,adjudicated_all=True,
 differences=ordered,adjudications=[bracket],c_doubts=cd,s_rows=s,inventory=inv,notes=notes,check_events=events,unresolved=un,abbreviations=rs[0]['abbreviations'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('scan014 draft:',len(ordered),'loci;',sum(r['against_C'] for r in ordered),'against C;',sum(r['against_H'] for r in ordered),'against H;',len(inv),'inventory;',len(un),'doubts')
