"""Explicit main-reader scan032 decisions after every differing crop was viewed."""
from pathlib import Path
import hashlib,json,csv
r=Path(__file__).resolve().parents[1];p=r/'pages/J156-5-04_156-5_scan032.tex'
rec=json.loads((r/'review/scan032_adjudicated.json').read_text());comp=json.loads((r/'second/J156-5-04_156-5_scan032_comparison.json').read_text())
oldnote=p.read_text().split('% slanted; state of broad curved stroke uncertain, note retained live.\n')[1].split('\n\nb)')[0]
fig=oldnote[oldnote.index(r'\margin{')+8:-1]
plain=r"les conditions \deleted{\unsure{a)}} b) c) d) sont équivalentes, \unsure{et} \uline{impliquées} par a), lesquelles \unsure{caractérisent|caractérise} la subdivision construite \unsure{précédemment|précédemm$^{t}$}. Mais \unsure{ces trois|c) très} \unsure{cond.} (b,c,d) \unsure{sont} \unsure{loin} d'impliquer a)"
newnote='% slanted; live state preferred, whole-note cancellation explicitly retained as an alternative.\n'+r'\margin{\unsure{'+fig+'|'+r'\deleted{'+plain+'}}}'
edits=[
 {'old':r'\inserted{\unsure{$G$|$\in$}}','new':r'\inserted{\unsure{$G$|$\in$|e}}'},
 {'old':r'\deleted{\unsure{On}}','new':r'\deleted{\unsure{On|les|le}}'},
 {'old':r"Si $A\notin G'$, alors",'new':r"Si $A\notin G'$, \unsure{donc|alors}"},
 {'old':r'\inserted{chacune} des propriétés','new':r'\inserted{chacune} des \unsure{pr.|pro.} propriétés'},
 {'old':"dans l'ens des",'new':r"\unsure{dans|pour} l'ens des"},
 {'old':'% slanted; state of broad curved stroke uncertain, note retained live.\n'+oldnote,'new':newnote},
 {'old':"b) L'application can.",'new':"% Small additional a)-like label above the end of application, attachment uncertain.\nb) L'application \\inserted{\\unsure{a)}} can."},
 {'old':r"$A^\circ$ est une strate ouverte} de $F'$.",'new':r"$A^\circ$ est une \unsure{str.te|strate|str.} ouverte} de $F'$."}
]
def transform(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
O={
2:('19:34:15','The terminal capital has the open curved bowl and inward lower hook of this page’s G, not plain C. The blind Si is already in the complete page before the excerpt. Retain the formula.','high',False),
3:('19:34:15','R and some low remnants survive under the old strike; the live mark before voir has only a tiny body and upper dot/stroke. It can still be à or a colon. The blind omission of strate is an excerpt boundary.','low',False),
4:('19:34:15','A compact raised loop sits above the end of strate, with a short interior/terminal stroke. Separate G remains preferred and membership remains possible; the loop also admits the blind e alternative, which is now explicit. No extra de is supplied.','low',True),
5:('19:34:34','The cancellation crosses a tall curved/looped beginning and low continuation. On remains preferred, but les/le cannot be excluded letter by letter. Add those alternatives without silently replacing the cancelled group.','low',True),
6:('19:34:34','The entire cancelled union was reread. The lower-limit capital has an upright with two short rightward bars, rather than the two legs of A. Retain B≤F. Display-style wrappers account for the remaining token difference.','high',False),
7:('19:35:01','The first connective has a tall initial loop with a low oval and then a compressed low run, favouring donc. The later alors in the same crop has a different a/l sequence. Adopt donc with alors as an alternative. G-prime has its separate tick in both parts of the chain, and the later G is unprimed. A tighter source crop was inspected at19:40:19UTC.','medium',True),
9:('19:35:01','Ultra has its tall initial and connected low t/r/a. In the next word the f stem is followed by a rounded a/u group and crossing terminal x. There is no terminal tall t supporting fort. Retain Ultra faux.','high',False),
10:('19:35:01','Le has a low e return. The older raffinement remains under its strike; précédente has its accent, tall d and -ente tail, not the -ipale sequence of principale. Between des and the full propriétés is a separate p-descender, small r-like continuation and dot: restore doubtful pr./pro. A tight source crop inspected19:39:58UTC confirms that this is not a descender from the line above.','medium',True),
11:('19:35:01','The whole a) item lies under the large crossing diagonals. Both G forms have their inward hooked lower ends, and the order relation has a bent upper stroke plus curved lower bar, distinct from ordinary ≤. The shorter blind excerpt does not remove i.e. or F-prime est from the complete page.','high',False),
12:('19:37:57','Maximal has a thick cancellation through its bodies and a separate lower underline; these are not two surviving underlines. The replacement begins un plus grand. The final compact group has a low curved start, tall looped l-like stem and a compressed high ending, supporting the existing doubtful élémt/élément/élt. The blind parenthetical h.-s is not secured by distinct parentheses. The order sign is the bent preceq, with its separate star.','low',False),
13:('19:38:04','The line continues subdivisions de F qui induisent G-prime sur G. The first G has an interior horizontal arm and downturned endpoint; the last has the same lower inward return. The first words occur partly at the edge of this box and remain in the adjacent coverage.','high',False),
14:('19:38:04','The enlargement shows a detached short initial curve, a tall narrow loop, and an elevated ending crossed by the later diagonal. It does not establish literal parentheses and h.-s. Retain the existing three short-form alternatives rather than expanding to an unambiguous word.','low',False),
15:('19:38:12','The first word has a densely retraced initial loop and long descending stroke; the low remainder is compressed. Dans remains preferred, but pour is visually possible beneath the retracing. Add the alternative. The following l’ens is plain and has no final point.','low',True),
16:('19:38:12','Opening ou has a closed low o and u return; the next word has p-descender and ou/r continuation, supporting ou pour. The following cela revient is distinct. Both equals signs consist of two horizontal strokes; no inclusion curve is clear. Preserve the literal equals and the final d’une = F.','high',False),
17:('19:38:20','The rotated complete note shows an underlined impliquées-like ending followed by a separate p-descender/short ar run before a), so retain impliquées par, not impliquent alone. Lesquelles has the longer connected ending. The long lower continuation extends beyond the blind court reconstruction and remains transcribed with its original doubts. The broad curve crosses several word rows; live remains preferred but whole-note cancellation is now explicit as an alternative.','low',True),
18:('19:38:39','The formula has a single right arrow and the bent preceq relation; induit has its tall d/t and dotted i. A small separate a)-like group sits above the end of application. A wider crop inspected19:39:58UTC shows the original a) already at the start of the preceding cancelled item, so this is additional ink: restore it as a doubtful raised label with uncertain attachment.','low',True),
19:('19:38:39','Both difference slashes, primes, the tilde and the single right-pointing arrowhead are clear. Both readings encode the same formula; retain the existing display.','high',False),
20:('19:38:39','Only a point after B is dark enough for punctuation. The shortened toujours has a t stem, long j descender and a short r-like shoulder before the terminal s, so retain tjrs. The tiny ici ending is beyond the blind excerpt and remains in the edition.','medium',False),
21:('19:38:56','The separator is a long headless upright with a slight lower bend. Both TikZ strings approximate the same stroke; retain the integrated margin geometry.','high',False),
22:('19:38:56','Two long horizontal cancellations cross the old Les strates ouvertes ... line; its q-shaped descender, short ui and separate ne support the existing qui ne, with sont still doubtful. The new text is above that line, while de F-prime remains on the lower baseline. A tight source crop inspected19:39:58UTC shows a dark dot between str and a detached te-like ending: use doubtful str.te/strate/str. rather than certain expanded strate.','low',True),
23:('19:38:56','The old group has a long q-like descender followed by low ui and a separate short ne group; the horizontal strokes obscure the ending. Retain qui ne with sont doubtful. Distinct r/v bodies needed by prises/privées are not established.','low',False),
24:('19:39:15','Both capitals after the difference slashes have a downturned inner lower terminal, matching this page’s G. The formula’s universal quantifier, membership signs, prime and right-hand A are all clear. Retain G without C alternatives.','high',False),
25:('19:39:15','The heading has a large D bowl, small accented é and the final low m run, above its separate underline. Retain readable Dém without adding uncertainty.','high',False),
26:('19:39:15','Every implication has two shafts and a right head. The labels are d), b), c), a), d) in that order. Display and text wrappers introduce no ink difference.','high',False),
27:('19:39:20','The old heading has local crossing strokes and a separate lower underline. In the entire restriction formula F difference G sits at the main baseline after a tall bar, not as a reduced subscript. Both G forms have inward hooks. Retain the literal baseline notation and the explicit old-word uncertainty.','medium',False),
28:('19:39:20','New inclusion is heavily written over residues of an older identité-like word, including projecting tall strokes; keep the two layers. In (trivial), the tall final l is immediately followed by the closing parenthesis; a separate terminal e is not clear. The insertion’s arrow has a curved hook at its left and a right head.','medium',False),
29:('19:39:20','The old donc retains a looped d, low o bowl, short n ridge and open c end under the horizontal strike; the same sequence occurs again live. Retain both states and the full following phrase, whose prouver lies outside the shorter blind excerpt.','medium',False),
30:('19:39:20','The final equality has two parallel bars, the two primes are distinct and the final point is dark. Display wrappers alone differ.','high',False),
31:('19:39:28','The unrotated crop confirms a continuous headless curved stroke through multiple rows, ending in a turn rather than a secure arrowhead. Keep the drawn geometry. Its function cannot be fixed; explicitly retain a whole-note cancellation alternative beside the preferred live note. The differing blind text is adjudicated in the overlapping full-note box032-b17.','low',True)}
dec=[]
for x in comp:
 if not x['different']:continue
 k=int(x['box'][-2:]);tm,ev,conf,ch=O[k]
 v=transform(x['first'])
 if k in (17,31):v=newnote
 if k==7:v=v.replace('alors',r'\unsure{donc|alors}',1) if r'\unsure{donc|alors}' not in v else v
 if k==10:v=v.replace('des propriétés',r'des \unsure{pr.|pro.} propriétés')
 if k==18:v=v.replace("L'application can.",r"L'application \inserted{\unsure{a)}} can.")
 if k==22:v=v.replace('une strate ouverte',r'une \unsure{str.te|strate|str.} ouverte')
 dec.append({'box':x['box'],'changed':ch,'final':v,'evidence':ev,'confidence':conf,'crop':f'crops/second_scan032_{x["box"]}.png','viewed_utc':f'2026-11-20 {tm} UTC'})
updates=[]
for c in rec['changes']:
 v=transform(c['final'])
 if v!=c['final']:updates.append({'id':c['id'],'fields':{'final':v,'second_evidence':'See the corresponding independent-reading adjudication and main-reader crop observations.'}})
updates.append({'id':'032-62','fields':{'final':newnote,'confidence':'low','second_evidence':O[31][1]}})
def newrow(i,place,C,H,final,k,kind,box,crop=None,conf='low'):
 return {'id':f'032-BL{i:02}','place':place,'C':C,'H':H,'final':final,'evidence':O[k][1],'crop':crop or f'crops/second_scan032_032-b{k:02}.png','box':box,'rotation_degrees':0,'confidence':conf,'kind':kind,'against_C':True,'against_H':True,'H_marked':False,'certainty_only':False,'main_decision':'Changed following independent blind reading and main-reader source-crop inspection.'}
new=[
 newrow(1,'first case, connective after A not in G-prime','alors','alors',r'\unsure{donc|alors}',7,'misread word',[1010,240,1340,325],'crops/main_audit032_alors_donc.png','medium'),
 newrow(2,'corollary, short start between des and propriétés','(omitted)','(omitted)',r'\unsure{pr.|pro.}',10,'omission',[480,675,1250,875],'crops/main_audit032_corollary_pr.png','medium'),
 newrow(3,'above application, small additional label','(omitted)','(omitted)',r'\inserted{\unsure{a)}}',18,'omission',[250,880,1630,1450],'crops/main_audit032_label_a.png'),
 newrow(4,'condition c, shortened word before ouverte','strate','strate',r'\unsure{str.te|strate|str.}',22,'abbreviation expanded or spelling modernised',[1120,1585,1640,1710],'crops/main_audit032_word_strate.png')]
u=[]
for q in rec['unresolved']:
 q=dict(q);q['reading']=transform(q['reading'])
 if q['place']=='top inserted glyph':q['alternatives']=['G',r'\in','e']
 if q['place']=='top cancelled On':q['alternatives']=['On','les','le'];q['confidence']='low'
 if q['place']=='long oblique note, curved stroke state':q['reading']=newnote;q['reason']=O[31][1]
 u.append(q)
for place,read,alts,reason,crop in [
 ('first-case connective','donc',['alors'],O[7][1],'crops/main_audit032_alors_donc.png'),
 ('corollary short start','pr.',['pro.'],O[10][1],'crops/main_audit032_corollary_pr.png'),
 ('condition a, before l’ens','dans',['pour'],O[15][1],'crops/second_scan032_032-b15.png'),
 ('raised label above application','a)',[],O[18][1],'crops/main_audit032_label_a.png'),
 ('condition c shortened strate','str.te',['strate','str.'],O[22][1],'crops/main_audit032_word_strate.png')]:
 u.append({'place':place,'reading':read,'alternatives':alts,'confidence':'low','reason':reason,'crop':crop})
out={'scan':32,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edits':edits,'decisions':dec,'record_updates':updates,'new_changes':new,'unresolved_replace':u,'changed_loci':['032-top-insertion-alternative','032-cancelled-On-alternatives','032-BL01','032-BL02','032-dans-certainty','032-note-state','032-BL03','032-BL04'],'notes_append':['Independent crop audit restores the separate pr.-like short start before propriétés and the small raised a)-like label above application. The first connective is now preferred as donc, with alors retained as an alternative. The replacement in condition c appears abbreviated str.te rather than securely written out. The long slanted note now carries an explicit whole-note cancellation alternative; neither this doubtful state nor its disputed wording is used to repair the mathematics.'],'abbreviations_append':[{'form':'pr. (or pro.)','expansion':'Possible unfinished start of propriétés; retained before the following complete word.'},{'form':'str.te','expansion':'Possibly strate, but dot and detached ending retained in the diplomatic text; form remains doubtful.'}]}
(r/'second/scan032_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (r/'review/main_image_reviews.tsv').open('a') as f:
 for name,b,z in [('label_a',[250,880,1630,1450],1.5),('corollary_pr',[480,675,1250,875],2.3),('word_strate',[1120,1585,1640,1710],3),('alors_donc',[1010,240,1340,325],4)]:
  f.write(f'2026-11-20 19:39:58 UTC\tmain\tcrops/main_audit032_{name}.png\tIndependent audit follow-up; source box {b}; LANCZOS {z}x; no rotation\n')
print(len(dec),'decisions;',len(edits),'edits')
