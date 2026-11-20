from adjudication import *
n=28;rr=reports(n)
t=(O/'readers/R1/scan028.tex').read_text()
old=r'\deleted{\deleted{\uline{Proposition}} Soient $F,G$ deux figures ens. de $\mathcal L$. \deleted{\unsure{Cons}} Soit \deleted{$\unsure{H|K}$}}'
new=r'\deleted{\uline{Proposition}} Soient $F,G$ deux figures ens. de $\mathcal L$. \deleted{\unsure{Cons}} \unsure{Soit|\deleted{Soit}} \deleted{$\unsure{H|K}$}'
assert old in t;t=t.replace(old,new).replace(r'\deleted{\unsure{A_k}}',r'\deleted{A_k}').replace(r'\deleted{\unsure{A}}',r'\deleted{A}')
m2={1:2,2:3,3:5,4:6,5:7,6:10,7:11,8:14,9:15,10:17,11:19,12:20,13:23,14:25,15:28,16:29,17:30,18:32,19:33,20:34,21:1,22:4,23:8,24:12,25:13,26:16,27:18,28:21,29:22,30:26,31:27,32:31,33:35}
m3={1:3,2:4,3:6,4:7,5:8,6:11,7:12,8:15,9:16,10:19,11:21,12:22,13:24,14:26,15:29,16:30,17:31,18:33,19:34,20:35,21:1,22:5,23:10,24:13,25:14,26:18,27:20,28:27,29:25,30:28,31:0,32:32,33:36}
assert len(m3)==33,'R3 locus mapping must be supplied after reading its completed report'
rows=[]
for i,x in enumerate(differences(rr[0]),1):
    cr='top' if i in (1,2,3,4,5,6,7,22,23) else 'cancel' if i in (8,9,10,21,24,25,26) else 'diag1' if i in (11,12,27) else 'diag2' if i in (13,14,28,29) else 'set' if i in (15,16,17) else 'defs' if i in (18,19,20,33) else 'foot'
    reads=[reading(x),reading(differences(rr[1])[m2[i]-1]),reading(differences(rr[2])[m3[i]-1]) if m3[i] else r'I\times J (submitted page)']
    y=row(n,i,x,reads,f'crops/root/028_{cr}.png')
    if i==4:y['ink']+=' Main sees two strong upright stems and retains H first; diagonals still permit K.'
    if i in (10,19):
        y['final']='A_k' if i==10 else 'A';y['against_C']=True;y['confidence']='medium';y['ink']+=' Main resolves the triangular A and, in the first occurrence, the small low k beneath the strike.'
    if i==11:y['ink']+=' Main confirms the old T by the projecting horizontal top and vertical stem beneath the live S.'
    if i==2:y['ink']+=' R3 retains a doubt; main resolves the low ens run and explicit point, comparing the separate ens. in the diagram side note.'
    if i==13:y['ink']+=' R3 retains psi/Y; main resolves psi from the curved upper bowl and central stem extending above its join, unlike a simple Y.'
    if i==15:y['ink']+=' Main isolated the set at fourfold size: a long descending j and a separate prime are clear.';y['consequential']='The set pair is (i,j′), not H’s (i,i′); the index mismatch is retained.'
    if i==18:y['consequential']='The first bottom definition has A_i′, not H’s A_i. The visible prime is retained despite the adjacent boxed A_i.'
    if i==20:y['consequential']='The second bottom definition has a j subscript, with B/A overprinting, rather than H’s normalized A′_{i′}.'
    if i==21:
        y['place']='upper introductory sentence cancellation scope';y['final']='Proposition locally deleted; Soient F,G … de L live; construction below cancelled; Soit state separately uncertain'
        y['against_C']=True;y['against_H']=False;y['ink']='The first sentence lies above every broad cancellation stroke. Proposition is separately crossed. R1 regards the whole attempt as deleted; R2 and R3 retain the sentence live. Main retains it live because the diagonal strokes begin below it; the following construction remains cancelled. The word Soit is treated in a separate scope-doubt row.'
    if i==33:y['consequential']='The lower-set bound is I′_{≤j}, not H’s I′_{≤i′}; the visible long j descender decides.'
    rows.append(y)
x=differences(rr[1])[8]
rows.append(row(n,34,x,['cancelled block']*3,'crops/root/028_cancel.png',final='Cancelled construction from the defining set through C_k',against_C=False,against_H=True,confidence='high'))
x=differences(rr[1])[23]
rows.append(row(n,35,x,['downward S→I map','downward S→I map with upper retracing','downward S→I map'],'crops/R2/scan028_shaft.png',final='Downward S→I map',ink=x['ink']+' Main also viewed the fivefold crop and finds a closed retrace rather than an additional arrowhead.',against_C=False,against_H=False,review_type='diagram decoration reviewed'))
rows.append({'id':'028-36','place':'punctuation after k=(A,B) in cancelled prose','C':'k=(A,B), no following comma','H':'k=(A,B), followed by comma','readers':['no comma']*3,'final':'k=(A,B), no following comma','ink':'No separate comma follows the closing parenthesis; the broad diagonal below belongs to the cancellation.','crop':'crops/root/028_cancel.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
rows.append({'id':'028-37','place':'punctuation between the two final definitions','C':'two lines, no comma','H':'first definition followed by comma','readers':['two lines, no comma']*3,'final':'two lines, no comma','ink':'The first definition ends at its closing parenthesis; the second begins below. No comma is drawn.','crop':'crops/root/028_defs.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
rows.append(row(n,38,differences(rr[2])[1],[r'\deleted{\uline{Proposition}}']*3,'crops/root/028_top.png'))
for ix,num in [(22,39),(36,40)]:
    x=differences(rr[2])[ix]
    rows.append(row(n,num,x,['No editorial sentence']*3,'crops/root/028_diag1.png' if ix==22 else 'crops/root/028_foot.png',against_H=False,review_type='H editorial apparatus excluded; no transcription-error count'))
rows.append({'id':'028-41','place':'word Soit at upper cancellation boundary','C':r'\deleted{Soit}','H':'Soit live','readers':['Soit globally deleted','Soit deleted','Soit live'],'final':r'\unsure{Soit|\deleted{Soit}}','ink':'No stroke directly crosses Soit, but it introduces the cancelled definition immediately below. R1/R2 include it in the cancelled construction, while R3 leaves it live. The endpoint does not decide the scope securely; main leaves the state uncertain, with the directly unstruck word first.','crop':'crops/root/028_top.png','confidence':'low','kind':'deletion state (struck given live or live given struck)','against_C':True,'against_H':False,'marked_in_H':'no','review_type':'new in-place state uncertainty'})
inv=rr[1]['inventory']
notes='[TXT028-construction] Manuscript page 27 opens with a locally cancelled Proposition and a live setup sentence. The abandoned construction below uses nonempty intersections A°∩B° and calls the induced equivalence relation a “borne sup”. That cancelled argument is transcribed, not certified. The diagrams then form the image of S∩T under the two displayed maps and propose A_j=A_i∩A′_{i′}.\n\n[TXT028-indices] The diagram targets are I and I′, but the image formula writes I×J. A direct map-type check, recorded separately for each reader who performed it, flags this unexplained naming change. The set pair visibly reads (i,j′), the first bottom definition reads A_i′, and the second bound is I′_{≤j}. These differences from the surrounding expected pattern triggered enlarged readings; none was repaired. The second diagram has a headless psi line and an ordinary downward phi arrow with a retraced upper shaft.\n\nNo date, title sheet, page-count statement or explicit verification request appears. The capital and subscript overprints remain the least secure portions.'
notation=[{'sign':'prime on A_i′','form':'Detached short high tick; distinguished from low dotted i.','evidence':'028_defs, 4×.','ambiguity':'None for this prime.'},{'sign':'i / j / j′','form':'Short dotted i versus long left-hooked j; detached prime on the set pair.','evidence':'028_set and 028_defs.','ambiguity':'Overprinted second stratum remains uncertain.'},{'sign':'inclusion signs / arrows','form':'First diagram has rotated subset marks; second has hooked arrows and a headless psi stroke.','evidence':'028_diag1 and 028_diag2.','ambiguity':'Upper phi retrace does not add an arrowhead.'}]
save(n,t,rows,inv,notes,rr,notation,{'ens.':'ensemblistes / ensembles (context-dependent abbreviation)','rel.':'relation','équi.':'équivalence','sup':'supérieure','surj':'surjective','ord.':'ordonnés'},'Whole scan, both halves, and all inherited doubts, differences, cancellations, diagrams and bottom indices enlarged. The three independent readings are preserved; the main reader adjudicated the differing deletion scope and the overwritten letters.')
