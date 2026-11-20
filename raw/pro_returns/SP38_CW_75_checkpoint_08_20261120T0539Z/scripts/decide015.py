from pathlib import Path
from datetime import datetime,timezone
import copy,json

o=Path(__file__).resolve().parents[1]
rep={r:json.loads((o/'readings/scan015'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((o/'decisions/scan015_main_observations.json').read_text())
def get(r,k):return next(f for f in rep[r]['findings'] if f['id']==k)
def val(r,k):return get(r,k)['final'] if k else '[Not represented in this reader’s final reading.]'
mapping={f'C{i:02d}':(f'C{i:02d}',f'C{i:02d}') for i in range(1,19)}
mapping.update({'N01':('N02','F02'),'N02':('N03','F03'),'N03':('N06','C04'),'N04':('N10','F08'),'N05':('','N02'),'H01':('N01','F01'),'H02':('N08','F04'),'H03':('N09','F07'),'H04':('N20','F18'),'H05':('N21','F19'),'H06':('N04','F05'),'H07':('N05','C04'),'H08':('N12','F09'),'H09':('N14','F10'),'H10':('N14','F11'),'H11':('N16','F13'),'H12':('N17','F14'),'H13':('N18','F15'),'H14':('N18','F16'),'H15':('N19','F17'),'D01':('N07','F06'),'D02':('N15','F12'),'D03':('N19','F17')})
oi={'C01':1,'C02':2,'C03':4,'C04':5,'C05':6,'C06':7,'C07':7,'C08':7,'C09':8,'C10':11,'C11':12,'C12':13,'C13':14,'C14':15,'C15':16,'C16':17,'C17':18,'C18':20,'N01':2,'N02':3,'N03':5,'N04':10,'N05':21,'H01':0,'H02':4,'H03':22,'H04':30,'H05':31,'H06':23,'H07':5,'H08':12,'H09':25,'H10':26,'H11':27,'H12':18,'H13':28,'H14':29,'H15':19,'D01':9,'D02':17,'D03':19}
fs=copy.deepcopy(rep['R1']['findings'])
for f in fs:
    k=f['id'];a,b=mapping[k];ob=obs['observations'][oi[k]]
    f['readers']={'R1':f['final'],'R2':val('R2',a),'R3':val('R3',b)}
    f['evidence']=ob['decision'];f['crop']='; '.join(ob['crops'])
    f['decision']='All three final complete returns compared before main image review. '+ob['decision']
by={f['id']:f for f in fs}
def upd(k,**kw):by[k].update(kw)
upd('C01',final=r'\deleted{V}E',doubt_action='resolve',diff_c=True,diff_h=True,confidence='high',kind='omission')
upd('C02',final=r'\mathbb{R}',doubt_action='resolve',diff_c=True,diff_h=False,confidence='high')
upd('C03',final='cotes',doubt_action='resolve',diff_c=True,diff_h=True,confidence='high')
upd('C04',final=r'\deleted{et}',doubt_action='resolve',diff_c=True,diff_h=True,confidence='high')
upd('C05',final=r'\mathbb{C}',doubt_action='resolve',diff_c=True,diff_h=False,confidence='high')
upd('C08',final=r'\deleted{\unsure{A|B}}S',doubt_action='retain',diff_c=True,diff_h=True,confidence='low')
upd('C09',final=r'\unsure{rèal.|réal.}',doubt_action='retain',diff_c=True,diff_h=True,confidence='medium')
upd('C10',final=r'\deleted{\unsure{iso|isom}}',doubt_action='retain',diff_c=True,diff_h=True,confidence='low')
upd('C11',crop=by['C11']['crop']+'; crops/scan015/02_resp.png',evidence=by['C11']['evidence']+' '+obs['observations'][24]['decision'])
upd('C12',final='et',doubt_action='resolve',diff_c=True,diff_h=True,confidence='high')
upd('C13',final=r'\deleted{si $V\unsure{;|,}P,S$}, with hooked left cancellation return drawn in TikZ',doubt_action='retain',diff_c=True,diff_h=True,confidence='medium')
upd('C14',final=r'\deleted{P}',doubt_action='resolve',diff_c=True,diff_h=True,confidence='high')
upd('C18',final=r'\deleted{\unsure{Si|Soit}}',doubt_action='retain',diff_c=True,diff_h=True,confidence='low')
upd('N01',final='(avec metrique déf pos.',diff_c=True,diff_h=True,confidence='high')
upd('N02',final=r"sur \unsure{l'espace|l'esp|l'esp.} $V$ des translations",diff_c=True,diff_h=True,confidence='medium')
upd('H07',final=r'\uline{régulière}',diff_c=True,diff_h=True,place='Live repeated régulière and its short underline')
upd('D01',final='Two-line inserted angle condition within open boundary strokes, with separate comma in the left mouth',diff_c=True,diff_h=True)
upd('D03',final=r"\inserted{de l'ens des sommets} above gravité), with curved lead, short fork and long oblique stroke; d'un remains beneath the lead on the lower baseline",diff_c=True,diff_h=True)

def add(k,r,fid,readers,ob,**kw):
    f=copy.deepcopy(get(r,fid));f.update(id=k,readers=readers,crop='; '.join(obs['observations'][ob]['crops']),evidence=obs['observations'][ob]['decision'],decision=obs['observations'][ob]['decision']);f.update(kw);fs.append(f);by[k]=f
add('Y01','R2','N11',{'R1':r'\uline{rég.} in reading.tex','R2':val('R2','N11'),'R3':r'\uline{rég.} in reading.tex'},8)
add('Y02','R2','N13',{'R1':r"P' without doubt",'R2':val('R2','N13'),'R3':r"P' without doubt"},13,diff_h=False)
add('Y03','R3','N01',{'R1':'Live S without doubt','R2':'Live S without doubt','R3':val('R3','N01')},15,diff_h=False)

text=(o/'readings/scan015/R2/reading.tex').read_text()
def change(a,b):
    global text
    assert text.count(a)==1,(a,text.count(a))
    text=text.replace(a,b,1)
change('avec métrique déf pos.', 'avec metrique déf pos.')
change(r"sur l'\unsure{espace|esp.}",r"sur \unsure{l'espace|l'esp|l'esp.}")
change(r'\unsure{cotes|cotés}','cotes')
change(r'\deleted{\unsure{et}}',r'\deleted{et}')
change(r'\uline{normalisée}',r'\uline{\unsure{normalisee|normalisée}}')
change('(resp normalisée)',r'(resp \unsure{normalisee|normalisée})')
change(r'\unsure{\mathbb{C}|C}',r'\mathbb{C}')
change(r'\deleted{\unsure{iso}}',r'\deleted{\unsure{iso|isom}}')
r3=(o/'readings/scan015/R3/reading.tex').read_text()
hook=r3.split(r'\tikz[baseline=(cancel.base)')[1].split(' plus précisément,')[0]
change(r'\deleted{\unsure{si} $V,P,S$}',r'\tikz[baseline=(cancel.base)'+hook)
change(r'$(\deleted{P}S,A,R)$',r'$(\deleted{P}\unsure{S},A,R)$')
# Draw the gravity insertion as one local arrangement. Its baseline continuation
# lies beneath the curved lead; the surrounding ordinary prose wraps are joined.
head,tail=text.split('% The small addition stands above gravité',1)
tail=tail.split("d'un polygône combinatoire.",1)[1]
gravity=r'''% The addition is above gravité), with its independent closing parenthesis.
% The curved lead meets short forked strokes and a longer oblique stroke.
\begin{tikzpicture}[baseline=(gravite.base),x=1em,y=1em]
  \node[anchor=base west,inner sep=0pt] (gravite) at (0,0) {gravité)};
  \node[anchor=base west,inner sep=0pt,font=\small] at (-1.1,1.55)
    {\inserted{de l'ens des sommets}};
  \node[anchor=base west,inner sep=0pt] at (5.8,0) {d'un polygône combinatoire.};
  \draw[line width=.45pt] (3.7,-.5)
    .. controls (3.95,.9) and (4.5,1.18) .. (5.2,1.12)
    .. controls (6.3,1.1) and (7.6,1.02) .. (8.45,1.18);
  \draw[line width=.45pt] (8.45,1.18) -- (9.1,1.70);
  \draw[line width=.45pt] (9.35,3.0) -- (8.30,.96) -- (8.45,1.68);
\end{tikzpicture}'''
text=head+gravity+tail
points=r3.split('% Two detached dark points')[1].split('% archive sheet number:')[0]
change('% archive sheet number: 14','% Two detached dark points'+points+'% archive sheet number: 14')
(o/'decisions/scan015_final.tex').write_text(text)

inventory=copy.deepcopy(rep['R2']['inventory'])
hook_item=next(x for x in rep['R3']['inventory'] if x['element']=='Hooked left return of cancellation')
inventory.insert(15,copy.deepcopy(hook_item))
point_item=next(x for x in rep['R3']['inventory'] if x['element']=='Detached dark pair')
inventory.insert(len(inventory)-1,copy.deepcopy(point_item))
for x in inventory:
    e=x['element']
    if e=='Euclidean affine-plane setup':x['first_words_or_objects']='Soit E plan affine euclidien sur doubled R (avec metrique déf pos. …)'
    if e=='Canceled word before normalisée':x['first_words_or_objects']='et, resolved and canceled'
    if e=='Canceled metric fragment':x['first_words_or_objects']='iso / isom'
    if e=='Canceled clause before plus précisément':x['first_words_or_objects']='si V;P,S / si V,P,S; letter sequence resolved'
    if e=='Old P beneath combinatorial S':x['first_words_or_objects']='P resolved beneath an independently uncertain live S correction'

u=[
('Translation-space word',"l'espace","l'esp; l'esp.",'medium'),
('First normalization word','normalisee','normalisée','medium'),
('First chain, old punctuation after V','canceled comma','spur may belong to retraced superset','low'),
('First chain, old punctuation after P','canceled comma','spur may belong to retraced superset','low'),
('First chain, old letter','A','B','low'),
('Realization contraction','rèal.','réal.','medium'),
('Second normalization word','normalisee','normalisée','medium'),
('Canceled similarity precursor','iso','isom','low'),
('Parenthetic metric contraction','isom','compressed word; no securely recoverable alternative','medium'),
('Mark on transformed P','prime','exclamation-shaped two-component mark','medium'),
('Canceled clause separator after V','semicolon','comma','medium'),
('Live corrected first object of triple','S','upper contour merged with old P','medium'),
('Sign after exists','bare upright','unserifed numeral 1','medium'),
('Old letter beneath final V','E','overwritten fragments do not recover a complete contour','low'),
('Canceled old heading','Ex','Cor','low'),
('Canceled final introductory word','Si','Soit','low'),
('Detached lower-right pair','two drawn points','writing versus surface traces; no punctuation value assigned','low')]
notes=r'''An underlined Exercice heading introduces Réalisation régulière d'un polygône. The page defines regular and normalized rectilinear realizations, gives existence and comparison exercises a) and b), and closes with an underlined Cor about an affine or vector envelope and an orientation correspondence. No date or authorial pagination is present; archive 14 is a comment in an unnamed hand. No explicit authorial doubt words or question marks occur.

All three complete final returns were compared before the main reader inspected 32 crops: 23 existing reader crops and nine new crops for missing loci. All 18 original C doubts are explicitly disposed of: seven resolve and eleven remain, some narrowed or with revised alternatives. Six new local doubts remain, making seventeen in the final reading. The opening old V, doubled fields R and C, unaccented cotes, canceled et, the word et between P and P′, and the old P resolve. Metrique has no restored acute. The realization contraction favors a grave accent; the two normalization endings remain individually uncertain. The new uncertainty on the live correcting S is separate from the resolved old P. A prime-shaped mark on another P has two components and retains an exclamation-shaped alternative.

The written P et P′, later use of ambient V after the initial affine E, the bare upright after ∃, and grâce : centre de gravité are preserved. The repeated régulière has a short underline. The angle addition has two lines, open visible boundaries and a comma in its left mouth. The two lower interlinear additions retain their curved connectors, and the cancellation before plus précisément retains a hooked left return. Two detached lower points are drawn without assigning a punctuation function. The S packet is empty; H supplies no separate drawing supplement. Declared H alphabet macros and same-primary confidence differences are excluded from H counts.

Actual mathematical work is recorded in fourteen CHECK_EVENTS rows and decisions/scan015_math_work.md. For n≥3, the roots of unity supply an embedded regular n-gon; scaling makes its side length one. Under the usual interior-angle interpretation, equal angles give turn 2π/n and the equal-length edge recurrence gives vertices c+uζ^j. The two possible cycle orientations yield explicit direct or conjugate-linear similarities extending each prescribed combinatorial isomorphism. Three noncollinear vertices give uniqueness; without specifying the isomorphism there are 2n choices. Centroid preservation supplies the vector origin, and a two-dimensional sine/cosine subspace of real functions on the vertex set gives an intrinsic envelope and the two orientation choices. Polygon triangulability is recorded only as background used in the angle-sum check.

Two qualifications are kept separate from literal transcription. If part a is read without the n≥3 restriction written in b, a two-edge cycle cannot have the earlier required embedded straight-segment realization. If equal angles is instead interpreted only as equal smaller unoriented angles, a simple twelve-edge plus-shaped polygon has unit sides and right smaller angles but four reflex interior angles; it is not a regular twelve-gon. An exact integer certificate checks its twelve distinct vertices, side lengths and turns and all 54 nonadjacent segment pairs. This refutes only the weaker interpretation, not the usual interior-angle reading. No reader claimed an independent proof check, and no mathematical expectation was used to supply an unclear glyph.'''
events=copy.deepcopy(json.loads((o/'pending_events/scan015.json').read_text()))
assert all(not r.get('checks') for r in rep.values())
dec=dict(base='R2',text_file='decisions/scan015_final.tex',findings=fs,inventory=inventory,notes=notes,events=events,unresolved=[dict(place=a,reading=b,alternatives=c,confidence=d) for a,b,c,d in u],abbreviations=copy.deepcopy(rep['R1']['abbreviations']),main_crop_count=9,main_crop_views=obs['views'])
(o/'decisions/scan015.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
coverage=json.loads((o/'decisions/scan015_C_doubt_coverage.json').read_text())
for i,d in enumerate(coverage['doubts'],1):
    f=by[f'C{i:02d}'];d.update(c_doubt_id=f'C{i:02d}',disposition=f['doubt_action'],findings=[f'S015-{fs.index(f)+1:03d}'],final=f['final'],crop=f['crop'])
(o/'decisions/scan015_C_doubt_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
p=o/'decisions/scan015_witness_comparison_pending.json';d=json.loads(p.read_text());d.update(status='Complete; initial questions retained for audit',main_status='All three final complete returns compared before main crop review; all reader/witness disagreements and all original C doubts inspected. No pending locus.');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=o/'decisions/scan015_review_state.json';d=json.loads(p.read_text());d.update(stage='Adjudication complete, ready for commit',C_resolved=7,C_retained=11,new_uncertainties=6,final_uncertainties=17,completed_utc=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert text.count('\\unsure{')==len(u),(text.count('\\unsure{'),len(u))
assert all(x in obs['views'] for f in fs for x in f['crop'].split('; '))
assert sum(f.get('doubt_action')=='resolve' for f in fs)==7
print(dict(findings=len(fs),inventory=len(inventory),events=len(events),doubts=len(u),views=len(obs['views']),C_changes=sum(f.get('diff_c',False) for f in fs),H_changes=sum(f.get('diff_h',False) for f in fs)))
