from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
root=Path('/workspace/scratch/4770596940a0'); rows=[]
def d(id,place,C,H,reading,ink,confidence,kind,crop,against_C=False,against_H=True,marked_in_H=False,review_only=False):
 rows.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop='crops/R2/scan030_'+crop+'.png',against_C=against_C,against_H=against_H,marked_in_H=marked_in_H,review_only=review_only))
d('D01','heading',r'\uline{Proposition}',r'\textbf{Proposition}',r'\uline{Proposition}','Single long rule below the heading.','high','other','top')
d('D02','first primed F',r"{\unsure{F|\mathcal F}}'","F'","F'",'Plain upright and two short arms; one separate elevated prime.','high','other','top',True,False)
d('D03','upper-right a note, initial word','trivial','Trivial','trivial','Lowercase t has a stem extending above its mid-height crossbar; the rest reads trivial.','high','other','top_notes')
d('D04','upper-right a note, abbreviation',r'\unsure{déf.}','déf.',r'\unsure{déf.|def.}','d/e loops and tall f with terminal point are visible. A separate acute over the compressed e is not secure; retain abbreviation and record accent uncertainty.','medium','other','top_notes',True,True)
d('D05','upper-right b note, first verb',r'\unsure{résulte}','résulte',r'\unsure{résulte}','The beginning is heavily retraced, with an s-like angle and the u/l/t/e ending legible.','medium','other','top_notes')
d('D06','upper-right b note, remaining words','en regardant supports',r'\ill{} \ill{}','en regardant supports','Low en, r/e then descending g loop, tall d and ending of regardant; supports has two p descenders and final t/s run.','high','readable ink left as \\ill{}','top_notes',False,True,True)
d('D07','starred left gloss',r'\uline{\unsure{explicitation|expliciter|explicitons}}',r'\emph{explicitation}',r'\margin{* \uline{\unsure{explicitation|expliciter|explicitons}}}','The underlined word starts explic-; its small final humps and upright do not settle the ending. It is written beside the formula in the left margin.','low','other','star')
d('D08','starred equation and top relation symbols','F prime.G set formula; ll, preceq, leq','same mathematical reading','same mathematical reading','The top rows have respectively double wedges, round-backed barred wedges, and straight barred wedges. The set has a vertical separator, subset sign and two support bars.','high','other','top',False,False,False,True)
d('D09','small cancelled word before live Or',r'\deleted{\unsure{or}}',r'\struck{Or}',r'\deleted{\unsure{or}}','Small loop and short rising stroke under a horizontal scribble; case and complete letters are less secure than the following live Or.','low','other','proof')
d('D10','live Or after the small cancellation','Or','omitted','Or','A separate large O and r follow the earlier cancelled cluster; they have no cancellation stroke.','high','omission','proof')
d('D11','second parenthesis, right edge: B in …',r'B\in\unsure{G|L}',r'B\in G',r'B\in\unsure{L|G}','The visible shape is a sloping upright turning into a rightward foot, favouring L. The upper/right part reaches the cut edge, so a clipped G remains possible; mathematics was not used to select G.','low','misread symbol or index','edge_letter',True,True)
d('D12','proof: le sens de A circle',r'le \unsure{sens} de',r'les \ill{} \ill{}',r'le \unsure{sens} de','The article ends without a separate s. The next low run has s-like ends but its middle remains compressed; a distinct looped de follows.','medium','readable ink left as \\ill{}','sense',False,True,True)
d('D13','parenthetical abbreviation before F',r'\unsure{p.r.} à',r'\uncertain{pris} \ill{}','p.r. à','A long p descender, point, short r-like stroke, another point, then separate accented à. No full word pris is present.','high','abbreviation expanded or spelling modernised','sense',True,True,True)
d('D14','parenthetical between F and F prime',r'\unsure{dans|ds}',r'\ill{}',r'\unsure{ds|dans}','A tall d and separate flat final trace are visible. I prefer the short ds reading; additional a/n strokes cannot be distinguished, so dans is retained.','medium','readable ink left as \\ill{}','sense',True,True,True)
d('D15','proof: est le =','est le $=$','sont les mêmes','est le $=$','Short est, looped le, and exactly two horizontal strokes; no written word mêmes.','high','abbreviation expanded or spelling modernised','sense')
d('D16','cancelled setup after Si, opening delimiter',r'\deleted{$(A\cap B …$}',r'\struck{$A\cap B$} …',r'\deleted{$(A\cap B …$}','A clear left parenthesis begins the discarded setup. It is not completed by a right parenthesis before the other discarded symbols.','high','omission','centre_deleted')
d('D17','cancelled setup, rightmost F',r"A,A'\in F'",r"A,A'\in F",r"A,A'\in F",'With the preceding line included, the nearby vertical is continuous with the q of que above. It is not a prime beside F. The cancelled F itself has only its upright and two arms.','high','misread symbol or index','deleted_context',True,False)
for id,where,letter,base in [('D18','first A','A',"F'"),('D19','first B','B','G'),('D20','second A prime',"A'",'F'),('D21','second B prime',"B'",'G')]:
 d(id,'central membership annotation under '+where,'rotated membership sign above '+base,'base label '+base+' only','rotated membership sign above '+base,'An arch open downward with a short central descending stroke stands between '+letter+' and '+base+'; this is a rotated membership sign, not just positioning.','high','omission','centre')
d('D22','i.e. annotation of second F.G','interlinear insertion attached to F.G','ordinary adjacent formula','interlinear insertion attached to F.G','A curved leader begins beside F.G and descends to the smaller i.e. A-prime-circle cap B-prime-circle nonempty formula. Both primes and both circles are separate.','high','insertion or placement','centre')
d('D23','cancelled abbreviation after A prime cap B prime subset A cap B',r'\deleted{\unsure{\text{i.e.}}}',r'\struck{\ill{}}',r'\deleted{\unsure{\text{i.e.}}}','The dense crossed cluster contains a dot and small e-like ending. i.e. remains plausible but not secure.','low','readable ink left as \\ill{}','centre',False,True,True)
d('D24','conclusion, Or on sait que (…) que','Or on sait que (…) que','Or on sait (…) que','Or on sait que (…) que','A q descender and low ue follow sait before the parenthesis. A second que is written after the closing parenthesis. Preserve the repetition.','high','omission','conclusion')
d('D25','slanted left heading',r'\uline{Expliciter}','Explicitement',r'\uline{Expliciter}','After rotation the tall t and short er ending follow explici-. No -ement sequence. The underline is separate from the diagram.','high','misread word','left_rot')
d('D26','slanted left order arrangement','TikZ corner G <= F, F prime below F','inline G <= F succcurlyeq F prime','TikZ corner G <= F, F prime below F','The three letters form a corner: horizontal straight barred wedge between G and F, rotated curved barred relation between F and F prime.','high','drawing or diagram','left_rot')
d('D27','right note opening',r'\unsure{Un peu vif}',r'\ill{}','Un peu vif','Large U, low n, descending p and eu wave, followed by dotted i and long f after v. The words can be separated from the line above.','high','readable ink left as \\ill{}','right',True,True,True)
d('D28','right note: construction wording',r"on trouve par F'.G=G' un G'",r"F'.G=G' pour un G'",r"on trouve par F'.G=G' un G'",'on trouve begins at the end of the opening line; par starts the next line. un G-prime follows the equation.','medium','misread word','conclusion')
d('D29','right note: four-object order square','TikZ square','linear relations plus (en carré)','TikZ square','F-prime,F above G-prime,G; horizontal curved precedence signs and two downward-facing rotated straight inequality signs. All four primes/letters retained.','high','drawing or diagram','right')
d('D30','right note: remaining verification',r"mais il faut vérifier encore l'\uline{unicité}",r'mais il faut vérifier un nouvel \ill{}',r"mais il faut vérifier encore l'\uline{unicité}",'encore is a separate low wave, followed by l and the underlined u/n/i/c/i/t/é sequence.','high','readable ink left as \\ill{}','right',False,True,True)
d('D31','right note: introduction to a and b','Cela amène à dégager','cela revient à exiger','Cela amène à dégager','Initial capital C and Cela; then a/m/è/n/e and separate à; the final word has d loop and g descenders.','high','misread word','right')
d('D32','right note b: connector',r'\unsure{et}','et','et','Separate e loop and crossed upright t between R and P.','high','other','right_deleted',True,False)
d('D33','right note b: cancelled comparison',r'\deleted{\Rightarrow P\unsure{\leq|<}}',r'\struck{\Rightarrow P\leq}',r'\deleted{\Rightarrow P\unsure{\leq|<}}','The cancelled arrow and P are readable. The wedge is clear, but the possible lower bar merges into the cancellation stroke; retain both readings.','low','other','right_deleted')
d('D34','corollary heading',r'\uline{Cor}.',r'\textbf{Cor.}',r'\uline{Cor}.','The abbreviation has a full stop and an underline.','high','other','bottom')
d('D35','corollary predicate',r'\unsure{valable|valide}','valable','valable','The visible sequence includes first l and the second pair of tall b/l stems; no i/d pattern supporting valide.','high','other','valable',True,False)
d('D36','C7 introduction','Vérifions quand même','Vérifions pour de même','Vérifions quand même','Long q descender followed by the short u/a/n/d run; one word quand, then même with a high circumflex.','high','misread word','bottom')
d('D37','C7 label and placement','C7.','C7 in body; C7_0 in marginal note',r'C$7_0$ in the body introduction','A closed low oval follows the crossed 7. It is larger and hollow, unlike the solid points on this page. There is one label, aligned after Vérifions quand même, left of the marginal boundary; no extra terminal point.','high','misread symbol or index','c7',True,True)
d('D38','C7 order arrangement','TikZ corner with G prime under G','linear formula plus editorial layout note','TikZ corner with G prime under G','G and F are on the same row with straight <=; G-prime is below G with the rotated curved relation. The existence sentence continues to the right.','high','drawing or diagram','bottom')
d('D39','construction: cancelled parenthesis',r'\deleted{\unsure{(F.G)}}',r'\struck{\ill{}}',r'\deleted{\unsure{(F.G)}}','Dense diagonal hatching leaves an opening curve, possible F strokes, a G-like loop and closing parenthesis. The operator in the middle cannot be certified.','low','readable ink left as \\ill{}','union_deleted',False,True,True)
d('D40','construction parenthesis','(réunion disjointe)',r"(c'est une \uncertain{union} disjointe)",'(réunion disjointe)','The first word begins r/é and runs directly into union; there is no c’est une. The next word is disjointe.','high','text not on the page','bottom',False,True,True)
d('D41','verification b: relative word',r'\unsure{qui|que}',"qu'il",r'\unsure{qui|que}','q descender and u-like low curve followed by a short tail; no apostrophe or tall l. The ending allows qui or que.','medium','misread word','subdivise')
d('D42','verification b: cancelled verb',r'\deleted{\unsure{raffine}}',r'\struck{raffine}',r'\deleted{\unsure{raffine}}','Two tall f-like stems and a small final wave survive, but the horizontal cancellation covers the other letters.','low','other','subdivise')
d('D43','verification b: inserted verb',r'\inserted{\unsure{subdivise}}',r'\add{subdivise}',r'\inserted{subdivise}','Interlinear s/u/b then looped d and the i/v/i/s/e run are visible. A curved stroke ties the replacement to the cancelled verb.','medium','other','subdivise',True,False)
d('D44','verification b/c connector','F et c)','F c)','F et c)','An e/t-shaped word is written immediately after F at the right edge; c) begins below it.','high','omission','subdivise')
d('D45','right margin boundary strokes','not drawn','editorial description of framed block','TikZ left rule and open stepped boundary','A long left rule bounds the first note. The second boundary curves right, drops, steps farther right around body writing, and drops again. It is not a closed rectangle. These strokes and their relation to the notes are drawn in the proposed text.','high','drawing or diagram','right',True,True)
d('D46','relation command variants',r'\preceq',r'\preccurlyeq',r'\preceq','Both witness commands represent the same round-backed barred relation on this sheet. Retained consistently; distinct from straight leq and double-wedge ll.','high','other','top',False,False,False,True)

d('D47','reference star after c)',r'F.G\quad *',r'F.G followed by raised star',r'F.G\quad{}^{*}','The star is distinctly above the formula baseline at the upper-right of F.G; it is a raised reference mark matching the starred left gloss.','high','insertion or placement','top',True,False)

cddata=[('first F','D02','resolved'),('déf.','D04','revised'),('résulte','D05','retained'),('explicitation / expliciter / explicitons','D07','retained'),('cancelled or','D09','retained'),('G / L at right edge','D11','revised'),('sens','D12','retained'),('p.r.','D13','resolved'),('dans / ds','D14','revised'),('cancelled i.e.','D23','retained'),('Un peu vif','D27','resolved'),('et in marginal b','D32','resolved'),('cancelled leq / <','D33','retained'),('valable / valide','D35','resolved'),('cancelled (F.G)','D39','retained'),('qui / que','D41','retained'),('raffine','D42','retained'),('subdivise','D43','resolved')]
cd=[dict(id=f'C{i:02}',locus=l,difference_id=d,status=s) for i,(l,d,s) in enumerate(cddata,1)]
inv=[]
def invadd(element,kind,position,first,details=''):
 inv.append(dict(scan=30,sheet_kind='text',hand='his hand',element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes',details=details))
for args in [
 ('page number','text','top centre','29'),
 ('heading','text','top','Proposition Soient F prime,F,G','Heading underlined.'),
 ('three implications','display','upper body','a), b), c)','All six relation signs, three arrows and primes; c has raised star.'),
 ('note beside a','margin note','upper right','(trivial par déf. de ll comme Inf)'),
 ('note beside b','margin note','upper right','(résulte de a), en regardant supports)'),
 ('star gloss','margin note','upper left','* explicitation','Underlined, uncertain ending.'),
 ('star formula','display','below three implications','F prime.G = {A in F.G | A subset |F prime|}'),
 ('opening proof','text','upper middle','Prouvons c. Il faut prouver'),
 ('cancelled product','deletion','after prouver que','F prime.G'),
 ('small false start','deletion','before live Or','or'),
 ('intersection argument','text','middle upper','Or F prime.G est formé','Both pairs A cap B, nonempty circle intersections and parenthetical comparison.'),
 ('closedness introduction','text','centre','Prouvons que c’est fermé i.e. Si'),
 ('discarded setup','deletion','centre left','(A cap B … A,A prime in F,','No prime on final F; nearby vertical belongs to q above.'),
 ('first membership','display','centre right','A cap B in F prime.G','Rotated membership annotations to F prime and G; small i.e. nonempty circles at right.'),
 ('second membership','display','centre left next line','A prime cap B prime in F.G','Rotated membership annotations to F and G.'),
 ('nonempty gloss','insertion','under second F.G','i.e. A prime circle cap B prime circle nonempty','Curved connecting stroke.'),
 ('contained intersection premise','display','centre next line','et A prime cap B prime subset A cap B'),
 ('cancelled gloss','deletion','after containment premise','i.e.'),
 ('conclusion paragraph','text','middle lower','alors A prime cap B prime in F prime.G','Repeated que retained; component inclusions, closedness in F.'),
 ('slanted explanation','margin note','left lower, oblique','Expliciter : soit','Read after -45 degree rotation; all following formulas and map retained.'),
 ('slanted corner','diagram','within left margin','G <= F; F prime below F','TikZ-cd, both relation signs preserved.'),
 ('uniqueness note','margin note','right lower','Un peu vif, on trouve','Full note including request to verify uniqueness.'),
 ('order square','diagram','within right note','F prime,F / G prime,G','TikZ with all four relations.'),
 ('second right note','margin note','below uniqueness note','Cela amène à dégager','Two lettered implication statements.'),
 ('cancelled implication','deletion','right note b','=> P leq|<'),
 ('marginal boundary strokes','drawing','right note left edges','vertical rule and stepped open boundary','Reproduced in TikZ with note text; no closed rectangle invented.'),
 ('corollary','text','lower body','Cor. L’axiome C6 est valable'),
 ('verification introduction','text','lower body','Vérifions quand même C7_0','Low zero, no additional period.'),
 ('C7 order corner','diagram','lower body left','G <= F; G prime below G','TikZ-cd.'),
 ('existence sentence','text','to right of C7 corner','exists subdivision F prime de F qui induise G prime'),
 ('construction','text','bottom','On prend F prime = G prime cup (F setminus G)','Parenthesis réunion disjointe.'),
 ('discarded construction term','deletion','inside union construction','(F.G)'),
 ('verification list','text','bottom two lines','Il faut vérifier a) … b) … et c)'),
 ('replaced verb','deletion','verification b','raffine'),
 ('replacement verb','insertion','above deleted verb','subdivise')]: invadd(*args)

tex=(root/'out/readers/R2/scan030.tex').read_text(); body=re.sub(r'%[^\n]*','',tex);dep=0
for i,ch in enumerate(body):
 if ch=='{' and (i==0 or body[i-1]!='\\'):dep+=1
 if ch=='}' and (i==0 or body[i-1]!='\\'):dep-=1
 assert dep>=0
assert dep==0
assert body.count('\\[')==body.count('\\]')
assert len(re.findall(r'(?<!\\)\$',body))%2==0
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',body):
 if m[1]=='begin':stack.append(m[2])
 else: assert stack.pop()==m[2]
assert not stack
recipes=json.loads((root/'out/readers/R2/crops030.json').read_text()); math=json.loads((root/'out/readers/R2/math030.json').read_text())
report=dict(scan=30,manuscript_page=29,reader='R2',model='inherited; no separate model identifier used',effort='inherited',start_utc=(root/'out/readers/R2/start030.txt').read_text(),end_utc=datetime.now(timezone.utc).isoformat(),
 independence='Read supplied C/H and C doubts/notes, the original scans and my own crops only. No other readers’ files or root decisions inspected. No scan after030 viewed.',
 procedure='Whole page, upper half, lower half; full word/symbol comparison; 18 explicitly viewed enlarged crops, including the left margin rotated -45 degrees. A focused final recheck of the cancelled F used a newly made wider crop after a parent request to inspect that locus; no proposed reading was supplied with that request.',
 images_viewed=[dict(path=f'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan030{s}.jpg',role=t) for s,t in [('', 'whole'),('_a','upper half'),('_b','lower half')]]+[dict(path=r['path'],role='enlarged crop') for r in recipes],crops=recipes,
 comparison_policy='Flags include uncertainty/candidate changes and diplomatic state; equivalent macro syntax and preceq/preccurlyeq variants are not counted by themselves.',differences=rows,C_doubt_resolutions=cd,
 S_row_decisions=[dict(row_id=None,decision='not applicable',reason='No row in 156-5_CORRECTIONS.tsv covers scan030.')],inventory=inv,
 remaining_doubts=[x for x in cd if x['status']!='resolved'],
 notation=[
 dict(locus='three upper implications',latex=r'\ll,\preceq,\leq',ink='Two wedges; curved barred wedge; straight barred wedge, respectively.'),
 dict(locus='all four central lower annotations',latex=r'\rotatebox{-90}{$\in$}',ink='Open-down arch with separate short central stroke between element above and family below.'),
 dict(locus='all intersection formulas',latex=r"A^\circ\cap B^\circ,\ A'^\circ\cap B'^\circ",ink='Separate raised open circles; primes are short high ticks, not part of the circles.'),
 dict(locus='proof parenthetical conclusion',latex='le $=$',ink='Two short horizontal strokes instead of a written même.'),
 dict(locus='left margin map',latex=r"\varphi^{-1}(G),\quad\varphi:F'\to F\ldots",ink='Loop and descending stem of varphi, superscript minus/1, arrow right, three trailing points.'),
 dict(locus='C7 introduction',latex=r'C$7_0$',ink='Crossed digit seven and distinct lower hollow zero.'),
 dict(locus='construction',latex=r"G'\cup(F\setminus G)",ink='Open-up union and short diagonal backslash; unprimed G in difference.')],
 notes_while_reading=[
 'The proposition states monotonicity of figure intersection in three distinct relations, ll, preceq and leq. The first two are supplied with short marginal explanations; the body proves c).',
 'The starred formula identifies F-prime.G as the members of F.G contained in the support of F-prime. The body describes intersections with nonempty circle parts, then argues closedness.',
 'The proof literally says le sens de A-circle … est le =. H’s plural paraphrase does not match those strokes. The ambiguous right-edge letter is not silently changed to G for mathematical expectation.',
 'The containment inference A-prime cap B-prime subset A cap B => componentwise containment is explicitly attributed to la théorie de F.G. A small set computation below confirms that this inference is not valid for arbitrary sets; it does not refute the claim for figures.',
 'The conclusion repeats que around the parenthesis. The cancelled setup’s final F is unprimed: the possible prime is actually the q descender from the preceding line.',
 'Corollary: L’axiome C6 est valable. The next introduction reads Vérifions quand même C7_0 and proposes F-prime=G-prime union (F setminus G), called a réunion disjointe.',
 'The page expressly leaves verification tasks: Prouvons c. Il faut prouver que; Un peu vif; mais il faut vérifier encore l’unicité; Il faut vérifier a) c’est une figure b) qui/que subdivise F et c) qui induit G-prime sur G.',
 'The right note formulates two further order implications and retains a cancelled partial implication in b. The left note gives an explicit inverse-image description. No proof of those claims or of C6/C7 was undertaken.'
 ],
 mathematical_checks_actually_performed=[dict(statement_id='156-5-030-R2-general-set-inference',type='computation or formal certificate',claim='For arbitrary sets, intersection inclusion implies both factor inclusions.',example=math,outcome='False for arbitrary sets: both intersections equal {1}, but neither factor inclusion holds. The manuscript invokes additional figure theory, whose hypotheses were not tested by this example.')],
 check_events=[dict(statement_id='156-5-030-R2-general-set-inference',date=datetime.now(timezone.utc).date().isoformat(),who='R2; model and effort inherited',type='computation or formal certificate',outcome='Arbitrary-set implication fails on saved finite example; no refutation of the manuscript figure-theoretic statement is claimed.'),dict(statement_id='156-5-030-main-claims',date=datetime.now(timezone.utc).date().isoformat(),who='R2; model and effort inherited',type='carried as background without fault found',outcome='Read the three monotonicity claims, support formula, C6 corollary, C7 construction, and margin claims without independently proving them.')],
 absences=['No title or date','No printed text or separate archive number'],
 syntax_validation=dict(braces_balanced=True,math_dollars_even=True,environments_balanced=True,display_pairs=body.count('\\['),compiled=False),proposed_tex='out/readers/R2/scan030.tex',proposed_tex_sha256=hashlib.sha256(tex.encode()).hexdigest(),
 summary=dict(difference_or_review_rows=len(rows),C_doubts_reviewed=len(cd),C_doubts_resolved=sum(x['status']=='resolved' for x in cd),remaining_doubts=sum(x['status']!='resolved' for x in cd),inventory_elements=len(inv),crops_viewed=len(recipes),against_C=sum(x['against_C'] for x in rows),against_H=sum(x['against_H'] for x in rows)))
(root/'out/readers/R2/scan030.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary']))
print('Saved scan030.json; syntax-only checks passed')
