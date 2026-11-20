from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan005_review.json').read_text()); t=(R/'review/scan005_proposed.tex').read_text()
# One alphabet throughout the cote; uncertainty is registered at its first occurrence.
t=t.replace(r'\unsure{M|\mathcal M}', 'M').replace(r'\unsure{L|\mathcal L}', 'L').replace(r'\unsure{\mathscr F|\mathcal F|\mathfrak F}',r'\mathscr F')
cs=[]
for c in d['changes']:
 c['crop']=c['crop'].removeprefix('out/')
 c['consequential']=c['id'] in ['S005-25','S005-29','S005-40','S005-43','S005-45','S005-51','S005-52','S005-57']
 if c['id'] in ['S005-04','S005-20','S005-25','S005-29','S005-31','S005-34','S005-38','S005-43','S005-44','S005-45','S005-57']:c['against_C']=False
 if c['id']=='S005-03':
  c['final']='M, consistently with the first-occurrence M/mathcal M uncertainty on scan003';c['scan_shows']+=' Repeated doubt markup is consolidated into the first occurrence in the cote; this is not a new semantic reading.'
 if c['id']=='S005-04':
  c['final']=r'\mathscr F, with the mathscr/mathcal uncertainty recorded at its definition on004';c['scan_shows']='The curved upper swash, stem and short transverse bar are the same script capital as in the data definition on004. The first-occurrence mathscr/mathcal uncertainty governs this page; the block F for one figure is distinct. No additional blackletter alternative is introduced merely because H chose that font.'
 if c['id']=='S005-06':c['final']=r'figures $\subset\mathscr F$ élémentaires'
 if c['id']=='S005-12':
  c['final']='L, consistently with the L/mathcal L uncertainty first registered on004';c['scan_shows']+=' The same first-occurrence uncertainty governs this repeated symbol.'
 if c['id']=='S005-50':
  c['against_H']=False;c['consequential']=False;c['kind']='other';c['scan_shows']+=' This is one global glyph mapping of the same intended relation, not seven semantic corrections against H; it is excluded from the H collation count.'
 cs.append(c)
# Split records referring to distinct source locations; no new reading or crop is involved.
by={c['id']:c for c in cs}
def split(id,parts):
 orig=by[id];cs.remove(orig)
 for i,patch in enumerate(parts,1):
  a=dict(orig);a.update(patch);a['id']=id+f'-{i}';cs.append(a)
split('S005-02',[
 dict(place='M entry, circled label',C=r'\textcircled{\scriptsize\unsure{e}}',H='(e)',final=r'\textcircled{\scriptsize\unsure{e}}',scan_shows='A complete enclosing oval surrounds the compressed inner strokes; the e remains uncertain.'),
 dict(place='L entry, circled label',C=r'\textcircled{\scriptsize\unsure{f}}',H='(f)',final=r'\textcircled{\scriptsize\unsure{f}}',crop='crops/scan005_L_heading.png',box=[323,270,1030,402],scan_shows='A complete enclosing oval surrounds the inner crossed stem; f is plausible but remains uncertain.')])
split('S005-05',[
 dict(place='quotation marks around figures élémentaires',C=r"\unsure{``}figures élémentaires''",H='« figures élémentaires »',final=r"\unsure{``}figures élémentaires''",confidence='low',scan_shows='The closing marks are raised paired pen strokes. The opening pair is crowded against the tall f and remains uncertain.'),
 dict(place='quotation marks around lieux',C="``lieux''",H='« lieux »',final="``lieux''",crop='crops/scan005_L_heading.png',box=[323,270,1030,402],scan_shows='Raised paired pen ticks enclose lieux; neither pair forms guillemet angles.'),
 dict(place='quotation marks around sine qua non',C="``sine qua non''",H='« sine qua non »',final="``sine qua non''",crop='crops/scan005_axiom_intro.png',box=[262,545,1665,739],scan_shows='Both pairs are short high ticks, not guillemet chevrons.')])
split('S005-15',[
 dict(place='upper left note, opening strates underline',C=r'\uline{strates}',H='strates',final=r'\uline{strates}',scan_shows='A short horizontal underline lies beneath the opening strates.'),
 dict(place='upper left note, strates after ens. de ses',C=r'\uline{strates}',H='strates',final=r'\uline{strates}',scan_shows='A separate underline lies beneath strates and meets the note connector.')])
split('S005-16',[
 dict(place='upper left note, after X≤F',C='no semicolon',H='semicolon',final='no semicolon',scan_shows='No semicolon follows the final F on this baseline.'),
 dict(place='upper left note, after the tilde F set formula',C='no period',H='period',final='no period',scan_shows='The formula ends with its set brace; the nearby vertical stroke belongs to the note connector, not punctuation.')])
split('S005-17',[
 dict(place='upper right definition of M, ending',C='no terminal semicolon',H='terminal semicolon',final='no terminal semicolon',crop='crops/scan005_right_note.png',box=[1215,60,1670,360],scan_shows='Blank paper follows the final ambient F in the upper block.'),
 dict(place='replacement definition of L, ending',C='no terminal period',H='terminal period',final='no terminal period',scan_shows='Blank paper follows the final refinement chevrons in the lower definition.')])
split('S005-27',[
 dict(place='At2 marginal criterion, initial Si',C='Si',H='si',final='Si',scan_shows='The initial S is tall and capital, followed by a separate dotted i.'),
 dict(place='condition b, initial Si',C='Si',H='si',final='Si',crop='crops/scan005_conditions_ab.png',box=[705,1255,1655,1383],scan_shows='The initial S is a tall capital form beside the lower-case i.')])
split('S005-54',[
 dict(place='compatibility definition, after existe',C='no comma',H='comma',final='no comma',scan_shows='The gap after existe and before i.e. contains no comma.'),
 dict(place='caption figures compatibles, ending',C='no period',H='period',final='no period',scan_shows='The caption ends with the underline and word, without a period.')])
d['changes']=sorted(cs,key=lambda c:c['id'])
d['doubts']=[q for q in d['doubts'] if q['place'] not in ['first bare set capital and its repetitions','first ambient F and its repeated forms','first L symbol']]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole image once, both halves once, all 22 reader crops','decisions':['Confirmed C in the At2 marginal quantifier, F∨C and {F,C}; context would require G but ink remains C.','Accepted straight overbar, a-prime, toutes famille, one-X final line, live parenthesis, raised family insertion and separate underline under cancelled éléments.','Consolidated repeated alphabet uncertainty at its first occurrence in the cote, without introducing H’s blackletter as an extra reading.','Retained seventeen local doubts; ten C doubt tokens resolved and three repeated font doubts referred to earlier definitions.','Recorded equivalent compatibility-glyph mapping once, excluded from semantic H differences.']}
lines=t.splitlines()
def line(prefix):return next(x for x in lines if x.startswith(prefix))
def span(a,b):return t[t.index(a):t.index(b)+len(b)].replace('\n',' ')
compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
reads={
1:r'\deleted{\unsure{3}}4',2:r'\textcircled{\scriptsize\unsure{e}}',3:lines[2],
4:line(r'\margin{\tikz'),5:line(r'\margin{formé'),6:r'\deleted{\unsure{$\mathscr F$}}',7:r'\textcircled{\scriptsize\unsure{f}}',
8:line(r'\textcircled{\scriptsize\unsure{f}}'),9:r'\deleted{\uline{\unsure{éléments}}}',10:r"\inserted{``lieux''}",11:r'\deleted{\unsure{minimaux}}',
12:line(r'\inserted{\tikz'),13:line('I) Axiomes'),14:'I)',15:r'\inserted{At~1 - At~3}',16:r'At~4 - At~7',17:r'\deleted{\unsure{At 1|At 4}}',18:r'\deleted{\unsure{et|4}}',
19:line(r'\uline{At 1}'),20:line(r'\margin{Axiomes'),21:span(r'\uline{At 2}',r'\widetilde F=\{X\in M\mid X\leq F\}'+'\n'+r'\]'),22:r'\deleted{\unsure{d}}est',23:line(r'\margin{Axiome des strates'),24:line(r'\uline{Scholie}'),25:r'\uline{At}~1 et \uline{At}~2',26:r'\inserted{$\widetilde{\mathscr F}$}',27:line('a) les'),28:line('b) Si'),29:line('c) '),
30:r'$\deleted{\widetilde{\mathscr F}\neq\varnothing\quad(\Longleftrightarrow\varnothing\in\widetilde{\mathscr F})}$',31:r'(\deleted{\unsure{et}}',32:line(r'\margin{$\widetilde{\mathscr F}'),33:line('ou, indépendamment'),
34:r"b') $\forall x\in M$, l'ens $\widetilde{\mathscr F}^{x}=\{\deleted{\unsure{F}}\Phi\in\overline{\mathscr F}\mid x\in\Phi\}$ a un plus petit élément $\deleted{F}$ (noté $\widetilde X$)",35:r'\deleted{\unsure{F}}\Phi',36:r'\deleted{F}',
37:r"a') $\deleted{\unsure{\forall|F}}$ Dans $(\widetilde{\mathscr F},\subset)$, toutes famille majorée a un Sup, \uline{et} $\widetilde{\mathscr F}\neq\varnothing$ ($\Longleftrightarrow\varnothing\in\widetilde{\mathscr F}$)",38:"a')",39:r'\deleted{\unsure{\forall|F}}',40:'toutes',
41:r"\diagram{\begin{tikzcd} \text{b$'$)} \\ \text{a$'$)}\arrow[u,bend left=35] \end{tikzcd}}",
42:span('Relation\n',r'\end{aligned}'+'\n'+r'\]'),43:r'\unsure{défn|defn}',44:'C',45:'C',46:line('Cette relation'),47:r'\inserted{avec At~1, At~2, At~3}',48:r'\deleted{\unsure{est}}',
49:t[t.index('\\[\n(M,'):].replace('\n',' ').strip()}
bs=[]
for i,b in enumerate(d['second_boxes'],1):
 b['source_box_id']=b['box']; b['box']=f'B{i:03d}';b['reading']=reads[i]
 if i in [4,5,20,23,32]:b['kind']='whole marginal note; include all formulae, cancellations and any connector'
 elif i in [1,14,15,16,17,18,19,21,25,47]:b['kind']='handwritten numerical inscription with its complete associated text or formula'
 elif i in [6,9,10,11,22,26,30,31,35,36,39,48]:b['kind']='central correction; transcribe visible cancelled and added ink, and punctuation'
 elif i in [3,8,12,13,24,27,28,29,33,34,37,42,46,49]:b['kind']='complete text block or formula; include all corrections, decorations and punctuation'
 elif i==41:b['kind']='complete curved connector and adjacent list labels; inspect both ends'
 elif i in [2,7,38,43]:b['kind']='central handwritten label'
 else:b['kind']='central complete word or mathematical letter'
 bs.append(b)
d['second_boxes']=bs
(R/'pages/H156-01_156-7_scan005.tex').write_text(t)
(R/'review/scan005_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=R/'second/H156-01_156-7_scan005'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan005_*.png')):f.write(f'5\tcrops/{p.name}\t{now}\troot direct crop inspection completed before adjudication\n')
 f.write(f'5\twhole + a + b\t{now}\troot layout and continuous reading completed before adjudication\n')
print(len(cs),'records;',len(bs),'blind boxes;',len(d['doubts']),'remaining local doubts')
