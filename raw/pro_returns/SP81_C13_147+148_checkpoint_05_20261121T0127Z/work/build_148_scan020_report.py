from pathlib import Path
import json, re

B=Path('/workspace/scratch/15c7af26487b/edition')
P='148_scan020'
packet=(B/'packets'/f'{P}.md').read_text()
t=(B/'work'/f'{P}.tex').read_text()
root_lower=(B/'work/148_scan020_root_lower_section.tex').read_text().strip()
fence=chr(96)*3
def witness(name,next_name):
    block=packet.split('## Witness '+name,1)[1].split(next_name,1)[0]
    return block.split(fence+'tex',1)[1].split(fence,1)[0].strip()
C=witness('C','## Witness H')
H=witness('H','## C doubt marks')
marks=json.loads(packet.split('## C doubt marks',1)[1].split('## C/H difference rows',1)[0].strip())
diffs=json.loads(packet.split('## C/H difference rows',1)[1].split('## Preamble',1)[0].strip())
def span(s,start,end):
    return s.split(start,1)[1].split(end,1)[0].strip()
def brace_arg(s,start):
    i=s.index('{',start); level=0
    for j in range(i,len(s)):
        if s[j]=='{' and (j==0 or s[j-1]!='\\'): level+=1
        if s[j]=='}' and (j==0 or s[j-1]!='\\'):
            level-=1
            if level==0:return s[i+1:j]
    raise ValueError('unclosed argument')
def macro(s,token):
    start=s.index(token)
    arg=brace_arg(s,start+len(token))
    return token+'{'+arg+'}'
def node_contents(coord):
    return brace_arg(t,t.index('at '+coord)+len('at '+coord))
top=t[t.index(r'\figure{'):t.index('% FORMULAS')].strip()
head=top.splitlines()[0]
def wrap(code,h=head):
    return h+'\n'+code.strip()+'\n'+r'\end{tikzpicture}}'
isol=wrap(span(top,'% Isolated drawing.','% Upper branch.'))
network_code=top.split('% Upper branch.',1)[1].rsplit(r'\end{tikzpicture}}',1)[0]
network=wrap(network_code)
figs={
 'isolated':isol,
 'upper':wrap(span(top,'% Upper branch.','% Left branch.')),
 'left':wrap(span(top,'% Left branch.','% Central sphere.')),
 'centre':wrap(span(top,'% Central sphere.','% Right branch.')),
 'right':wrap(span(top,'% Right branch.','% Lower branch.')),
 'lower':wrap(top.split('% Lower branch.',1)[1].rsplit(r'\end{tikzpicture}}',1)[0])
}
sections={}
labels=['FORMULAS','PARTITIONS','EQUIVALENCE','EXACT_SEQUENCE','PENCIL_SHAPE','RELATIONS','LOWER_DIAGRAM']
for i,name in enumerate(labels):
    sections[name]=span(t,'% '+name,'% '+labels[i+1]) if i+1<len(labels) else t.split('% '+name,1)[1].split(r'\margin{19}',1)[0].strip()
eq=sections['EQUIVALENCE']
eqhead=eq.splitlines()[0]
upper_pencil=wrap(span(eq,'% Weak upper pencil annotation.','% Live expression and raised word.'),eqhead)
live_code=span(eq,'% Live expression and raised word.','% First faint line below')
brace_code=eq.split('% Brace below the central span and its two formula baselines.',1)[1].rsplit(r'\end{tikzpicture}}',1)[0]
live_equivalence=wrap(live_code+'\n'+brace_code,eqhead)
upper_mid=node_contents('(1080,982)')
under_first=node_contents('(631,1063)')
under_second=node_contents('(682,1117)')
lower_head=r'\diagram{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round,line join=round]'
overlay_code=span(root_lower,'% Pale overwritten span beside the lower Pi; drawn before the dark label and shaft.',r'\node[inner sep=0pt] (u0)')
overlay=lower_head+'\n'+overlay_code+'\n'+r'\end{tikzpicture}}'
hatch_code=span(root_lower,'% The upper middle arrow begins in the crossed raised cluster.',r'\draw[->,line width=.65pt] (4.42,.04)')
hatch=lower_head+'\n'+hatch_code+'\n'+r'\end{tikzpicture}}'
cfigs=re.findall(r'\\figure\{\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}\}',C)
assert len(cfigs)==5
hdraw=macro(H,r'\drawing')
cpartition=C[C.index(r'\boxed{\begin{gathered}'):C.index(r'\margin{\unsure{tétraèdre')].strip()
hpartition=H[H.index(r'\begin{array}{l}'):H.index(r'\[\n(\text{tétraèdre') if r'\[\n(\text{tétraèdre' in H else H.index(r'(\text{tétraèdre')].strip()
cupper=macro(C,r'\margin')
ceq=C[C.index(r'\underbrace{'):C.index(r'\margin{$\unsure{\omega')].strip()
heq=H[H.index(r'(\text{tétraèdre'):H.index(r'0 \to V(J)')].strip()
clower=C[C.index(r'\diagram{\begin{tikzcd}[column sep=small'):C.index(r'\margin{19}')].strip()
hlower=H[H.index(r'\begin{tikzcd}'):].strip()
crops={
'isolated_sphere':[121,72,381,349],'drawing_upper':[756,100,1298,352],
'drawing_left':[285,356,817,585],'drawing_centre':[817,349,987,537],
'drawing_right':[1005,351,1500,522],'drawing_lower':[817,535,1285,864],
'large_bleed':[1012,624,1507,1052],'formula_I':[55,591,334,689],
'formula_A':[133,681,333,779],'formula_C':[134,778,482,869],
'omegas':[129,864,655,981],'partitions':[78,976,476,1204],
'equivalence':[547,973,1435,1253],'printer_bleed':[244,1086,1511,1310],
'exact_sequence':[110,1237,617,1319],'pencil_shape':[184,1340,468,1471],
'relations':[698,1270,1183,1578],'lower_diagram':[79,1567,1029,2012],
'margin_number':[103,2134,190,2204],'upper_pencil_completion':[831,946,1380,1027]}
def cropref(name):return f'{P}_{name}.png'
def cref(name):return cropref(name)+' '+str(crops[name]).replace(' ','')

r={
'page':P,'reader':'reader_c','line_count':25,
'layout':"The upright sheet has an isolated upper-left sphere and a connected network of ten sphere outlines and two tetrahedral outlines across the upper and middle area. Formula blocks occupy the left middle. A pairing table has only a top/right frame. A live middle equivalence carries a raised word, a short central underbrace and faint pencil drafts above and below its left part. A short sequence, an open pencil sketch, framed relations and a lower three-row diagram with adjacent annotations follow. There is no written head page number; lighter 19 is at lower left. L01–L25 count local text/formula baselines, not a continuous prose paragraph; drawing labels and the isolated margin number are inventoried separately.",
'legibility':"Dark letters and most numeral forms are exposed, but dark retracing and pale pencil overlap at several mathematical loci. The first S/I form and its first relation remain uncertain; the pencil terminal = perpendicular is readable. The first pairing's final small letter has a retraced loop admitting e/c. The upper pencil words remain candidates, and two faint lower annotations are preserved graphically because neither their full contents nor every cancellation state is secure. D(Q) remains doubtful. The lower first 1 is clear; the last lowered digit remains 5|3 and the pale material beside it extends beyond a lone exponent. The source distinguishes fine pencil contours, thick dark/red paths, broken arcs and exposed dots. C is useful for many labels and formulas, but transcribes mirrored printer show-through, closes open frames/sketches and smooths source graphic details. H supplies a top-drawing description here, omits the terminal pencil = perpendicular and faint drafts, and uses lower-case pi, single shafts and expanded relations at several lower-diagram loci. No separate H drawing file was supplied. Marginal 19 is clear.",
'changes':[],'decisions':[],'unnumbered_decisions':[],
'inventory':[],'doubts':[],'notation':[],'abbreviations':[],'hand':[],
'notes':'','check_events':[],'second_boxes':[],'diff_coverage':[],
'deletion_insertion_check':''
}
def change(n,place,c,h,final,evidence,crop,confidence,kind,sheet,dc,dh,marked=False):
    r['changes'].append({'id':f'{P}-{n:02}','place':place,'C':c,'H':h,'final':final,'evidence':evidence,'crop':cropref(crop),'box':crops[crop],'confidence':confidence,'kind':kind,'error_sheet_kind':sheet,'differs_C':dc,'differs_H':dh,'marked_in_H':marked,'consequential':False})
change(1,'Isolated upper-left drawing',cfigs[0],hdraw,isol,
 "Five filled loci, the central cross, four drawn radial directions, the broken upper shaft beside the cross and repeated outer contours are visible. The final direct paths retain these details and the uneven head contours. C substitutes smooth ellipses and uninterrupted regular shafts. H supplies a verbal description; no error is asserted against an unseen separate H drawing.",
 'isolated_sphere','high','drawing or diagram','Drawings and diagrams',True,False)
change(2,'Connected drawing network across upper/middle page',cfigs[1],hdraw,network,
 "Ten sphere outlines and two tetrahedral outlines were inspected in all five branch/centre crops. The touching pair has continuous pale equators and asymmetric red point positions. The left meridian sphere has two explicit left equatorial points and a gapped heavy equator. The central rear equatorial arc is heavy and broken around c/d, not a uniform dotted arc. The upper/lower paired spheres have short connectors and distinct solid/dotted coloured paths. The far-right pencil sphere has layered transverse contours and irregular short marks. Selected tetrahedral edges are heavy; the lower rising internal edge is broken and pale. C omits/smooths several of these strokes. No comparison to an unavailable H drawing file is claimed. Additional inspected crops: drawing_upper, drawing_left, drawing_centre, drawing_lower.",
 'drawing_right','high','drawing or diagram','Drawings and diagrams',True,False)
change(3,'Pale repeated block at middle right',cfigs[2],'[not transcribed as front-side writing in H]','',
 "The uniformly spaced pale blue glyphs are mirrored, and the unmirrored pencil/dark drawings cross them. They form reverse-side printer show-through. C constructs front-side character runs from this pattern; the source rule excludes show-through. No individual letter/count claim is needed to classify it.",
 'large_bleed','high','text not on the page','Text that is not on the page',True,False)
change(4,'L03, terminal pencil continuation of wedge formula',
 r'C_Q=\bigwedge_{d\in D_Q}d=\unsure{\perp}',r'C_Q=\bigwedge_{d\in D_Q}d',
 r'C_Q=\bigwedge_{d\in D_Q}d=\perp',
 "Two pale parallel equality strokes precede a pale upright meeting a long baseline. The complete expression was inspected. C's first terminal-symbol reading is resolved; H omits the exposed pencil continuation.",
 'formula_C','high','omission','Omissions',False,True)
change(5,'L06–L09, pairing block and frame',cpartition,hpartition,sections['PARTITIONS'],
 "The enclosing line runs along the top and down the right only. The source has no closed lower/left sides. C supplies a closed box; H's editorial note places the vertical side at the left. A real comma stands between b and d on the second row; H's thin-space command supplies no comma. The other pair interiors lack separately exposed commas. The first row's last small letter is changed from C/H's c to preferred e with retained c alternative: an upper closed triangular loop and a continuous low return give the e appearance, while retracing leaves c possible. This letter is read from its strokes rather than the pairing pattern. Confidence for the whole locus is medium because it includes that lexical change.",
 'partitions','medium','drawing or diagram','Drawings and diagrams',True,True)
change(6,'L10, faint upper pencil annotation',cupper,'[omitted]',upper_pencil,
 "The completion crop contains the first tall stroke and the full upper pencil span. The proposed words tetraedre + b and (carre + remain weak, with their accents retained as candidates. Intervening short curves/obliques and horizontal traces are rendered graphically. C's text candidates remain undecided; the replacement of its illegible placeholder by a trace is not a claimed decipherment. H supplies no transcription of this annotation.",
 'upper_pencil_completion','low','omission','Omissions',False,True)
change(7,'L11 and L14–L15, live middle expression, raised word and brace',ceq,heq,live_equivalence,
 "oriente is raised above tetraedre and has a drawn underline/short attachment stroke. The brace spans the central portion beneath the comparison arrow and adjacent ends, not the complete width of both text terms. The two lower formulas belong to that short brace. C omits the underline and extends the brace across the whole expression. H's emphasis can represent the underline, and its note locates the brace under the arrow; no error is counted merely for that macro choice.",
 'equivalence','high','insertion or placement','Insertions put in the wrong place',True,False)
change(8,'L12–L13, faint annotations below the left middle term',
 r'\margin{$\unsure{\omega_I\times J|\deleted{\omega_I\times J}}$}',
 r'\note{sous le tetraedre, un $\omega_I\times J$ biffe}',
 under_first+'\n'+under_second,
 "The first faint line has intersecting leading strokes before the omega-like form, lowered I, cross and angular terminal form. Its cancellation scope is unresolved. A further faint formula line below it has a loop with an internal diagonal, an upright, paired short strokes, another small curved/upright trace, a long oblique and a terminal curl. Those visible marks are retained without a completed algebraic reading. C/H omit the leading trace and the further line; H's definite biffe state is not imposed on the whole preserved span.",
 'equivalence','medium','omission','Omissions',True,True,True)
change(9,'Pale repeated small rows across middle page',cfigs[3],'[not transcribed as front-side writing in H]','',
 "Uniform pale blue printer rows are mirrored beneath the unmirrored manuscript formulas. C supplies six speculative repeated printer strings. They are reverse-side show-through and are excluded, with this inspection recorded.",
 'printer_bleed','high','text not on the page','Text that is not on the page',True,False)
change(10,'L17, pencil label and open sketch',cfigs[4],'[no transcription of this label/sketch in supplied H]',sections['PENCIL_SHAPE'],
 "The left oblique rises to a short hooked tip, then a clear gap spans the top. A long slightly bowed lower stroke joins a short rising right oblique with an upper-left flick. C closes these into a parallelogram. D(Q) remains a candidate: the first upright/loop and the inner Q-like loop/descender are faint. H supplies no text for this label here; no claim is made about any unseen separate drawing file.",
 'pencil_shape','high','drawing or diagram','Drawings and diagrams',True,True)
change(11,'L18–L19, framed relations',
 r'\boxed{\left\{\begin{aligned}\rho^3&=\sigma^2=1\\\rho\sigma&=\ell\end{aligned}\right.}',
 r'\boxed{\begin{cases}\rho^{3}=\sigma^{2}=1\\\rho\sigma=\ell\end{cases}}',
 sections['RELATIONS'],
 "The formula's rho, sigma, exponents 3/2, 1 and looped terminal ell are exposed. The pencil frame has separated corners: a long top stroke, a left stroke beginning lower, a right stroke stopping above the bottom, and a bottom stroke ending before the right side. C/H close the frame through these gaps. No relation was proved by reading it.",
 'relations','high','drawing or diagram','Drawings and diagrams',True,True)
change(12,'L20–L25, lower three-row diagram and attached annotations',clower,hlower,root_lower,
 "Both Pi forms have two upright stems and a continuous top bar, supporting capital Pi rather than H's lower-case pi. The two Pi-to-T connectors have two shafts. The middle terminal connector has a low upturned blunt end. Three comparison marks have a curled left stroke and a straight right bar; they are rendered as vertical comparisons without a supplied connecting shaft. cart is inside the upper square. The upper T's outgoing line begins in the raised hatched cluster; its old character is unresolved. The lower dark index remains 5|3; the pale span beside it is kept in full as a graphical doubt, including bent enclosure, 2-like oblique, detached lower stroke, Z-like return and faint terminal curve. Two ditto ticks precede the middle Sl annotation. The last quotient ends with slash-minus, with no added plus; H itself notes the minus reading while its annotation supplies plus-minus. Group-letter alphabet identification stays locally doubtful. The root's exact drawing section is reused, after reader and root inspected the same complete crop.",
 'lower_diagram','medium','drawing or diagram','Drawings and diagrams',True,True,True)
change(13,'Lower-left marginal number',r'\margin{19}','[omitted]',r'\margin{19}',
 "The first numeral has a long oblique entry and upright. The second has a closed upper loop and descending curved return. Both 1 and 9 are exposed.",
 'margin_number','high','omission','Omissions',False,True)

for m in marks:
    n=int(m['id'][1:])
    if 139<=n<=164 or 171<=n<=176:
        crop='large_bleed' if n<=164 else 'printer_bleed'
        r['decisions'].append({'id':m['id'],'decision':'other','reading':'','evidence':"Excluded reverse-side printer show-through: uniformly spaced pale blue mirrored glyphs lie beneath unmirrored front-side drawing/writing. This original C mark belongs to that constructed printed pattern; no front-side text is retained.",'crop':cref(crop),'confidence':'high'})
    else:
        choices={
        165:('undecided',r'\unsure{S_Q|I_Q}',"The broad curved upper/lower parts favor an S-like form, but a straight interior upright and heavy retracing leave the S/I identification and any earlier state uncertain. The complete formula and subscript were inspected.",'formula_I','low'),
        166:('first',r'\perp',"A pale upright meets the pale long baseline after two equal-sign strokes; the full formula was inspected.",'formula_C','high'),
        167:('undecided',r'\unsure{tétraèdre $+$ b}',"The first tall stroke and following pale letter components admit the supplied candidate, but several low letters and the last loop/stem remain weak. The full upper span is present in the completion crop.",'upper_pencil_completion','low'),
        168:('undecided',upper_mid,"Intervening pale short curves, obliques and paired horizontal traces are exposed but do not establish two legible words or a secure formula. The actual graphical trace replaces the placeholder without claiming decipherment.",'upper_pencil_completion','low'),
        169:('undecided',r'\unsure{(carré $+$}',"A curved opening stroke, low letter strokes, raised accent region and cross are exposed; pale overlap prevents clearing the whole candidate.",'upper_pencil_completion','low'),
        170:('undecided',under_first,"The candidate omega-I cross angular-J sequence and preceding intersecting strokes are retained graphically. No independent strike securely establishes cancellation of every following sign.",'equivalence','low'),
        177:('undecided',r'\unsure{D(Q)}',"First upright/loop and enclosing curves survive; the inner Q-like loop and descender are worked over. The whole nearby open sketch was inspected.",'pencil_shape','medium'),
        178:('first','1',"A single leaning upright precedes the first horizontal connector; there is no enclosing oval. It matches the exposed first-column numeral state on this crop.",'lower_diagram','high'),
        179:('undecided',r'\unsure{5|3}',"The dark final lowered digit has a deep downstroke and returning lower curve, favoring 5 over the middle row's clear 3 form. Pale overlapping material prevents a definitive choice.",'lower_diagram','medium'),
        180:('undecided',overlay,"The complete pale span has a bent left enclosure, a 2-like oblique/return, detached low stroke, Z-like diagonal/right return and faint terminal curve. It is not fixed to a lone exponent or a completed parenthetic formula; the exact graphical span and its local question marker are retained.",'lower_diagram','low')}
        decision,reading,evidence,crop,confidence=choices[n]
        r['decisions'].append({'id':m['id'],'decision':decision,'reading':reading,'evidence':evidence,'crop':cref(crop),'confidence':confidence})
r['unnumbered_decisions']=[{'place':'L20, nested C exclamation doubt in raised hatched superscript','decision':'undecided','reading':hatch,'evidence':"Several oblique hatch strokes cover short upright/curved strokes. No complete underlying exclamation character is independently exposed. Its candidate status remains in the evidence; the actual crossed cluster is drawn with a local doubt marker, and the outgoing line begins within it.",'crop':cref('lower_diagram'),'confidence':'low'}]

# Complete the witness quotation at the faint-line locus from H itself.
hnote_start=H.index(r'\note{sous la double flèche')
r['changes'][7]['H']=r'\note{'+brace_arg(H,hnote_start+len(r'\note'))+'}'
r['changes'][7]['marked_in_H']=False

def inv(n,kind,position,objects,hand='his hand'):
    r['inventory'].append({'sheet_kind':'text','hand':hand,'element':f'E{n:02}',
        'kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes'})
inv(1,'drawing','Upper left, separate from the network','Isolated sphere: retraced ring, five filled loci, central cross and four radial directions')
inv(2,'drawing','Upper and middle page, connected network','Ten sphere outlines, two tetrahedral outlines, connectors, labels and coloured paths')
inv(3,'display','L01, first left formula',r'I\unsure{=|\simeq}\unsure{S_Q|I_Q}=\coprod_{d\in D_Q}d')
inv(4,'display','L02, second left formula',r'A_Q=\prod_{d\in D_Q}d')
inv(5,'display','L03, third left formula, including pale terminal signs',r'C_Q=\bigwedge_{d\in D_Q}d=\perp')
inv(6,'display','L04, first omega baseline',r'\omega_Q=C_Q\wedge D_Q')
inv(7,'display','L05, second omega baseline',r'\omega_I\simeq\omega_J\simeq C_Q\simeq J\setminus\{Q\}')
inv(8,'display','L06–L09, middle-left pairing block',r'a\ b\ c\ d; (ad)(b\unsure{e|c})=Q_0; (b,d)(ac)=Q_1; (cd)(ab)=Q_\infty; top/right frame')
inv(9,'text','L10, faint upper pencil annotation','Doubtful tétraèdre + b, intervening graphical traces, doubtful (carré +')
inv(10,'display','L11, main middle expression',r'(tétraèdre + diagonale)\longleftrightarrow(carré + codiagonale)')
inv(11,'insertion','Above the first noun of L11; underline and short attachment stroke',r'\inserted{orienté}')
inv(12,'display','L12, faint line below the left term of L11','Intersecting leading strokes and candidate omega-I cross angular terminal form; cancellation scope unresolved')
inv(13,'display','L13, further faint line below L12','Loop with internal diagonal, upright, paired short strokes, small curve/upright, long oblique and terminal curl')
inv(14,'display','L14–L15, beneath the short central brace',r'\omega_I\times J; \simeq J\times\omega_I')
inv(15,'diagram','L16, short sequence below middle expressions',r'0\to V(J)\to\unsure{\mathfrak S}_I\to\unsure{\mathfrak S}_J\to1')
inv(16,'drawing','L17, small lower-left pencil sketch and its label',r'\unsure{D(Q)}; open separated pencil strokes')
inv(17,'display','L18–L19, lower-right relations within a gapped pencil frame',r'\rho^3=\sigma^2=1; \rho\sigma=\ell')
inv(18,'diagram','L20, L22 and L24, lower three-row array','Three rows beginning with 1; T and Pi labels; doubtful group letters; horizontal/vertical connectors and comparison marks')
inv(19,'deletion','Raised cluster at the middle label of L20','Hatched short upright/curved strokes; no secure complete underlying character')
inv(20,'display','Pale overlapping span beside the lower Pi on L24','Whole bent enclosure, oblique/return, detached lower stroke, diagonal/right return and terminal curve')
inv(21,'text','Interior of the upper square in the lower diagram','cart')
inv(22,'display','L21, adjacent to the upper row of the lower diagram',r'\simeq\operatorname{Aff}(2,\mathbb Z/2\mathbb Z)')
inv(23,'display','L23, adjacent to the middle row of the lower diagram',r'two ditto ticks; \operatorname{Sl}(2,\mathbb Z/2\mathbb Z)')
inv(24,'display','L24, adjacent to the lower row of the lower diagram',r'\simeq\operatorname{Sl}(2,\mathbb Z/4\mathbb Z)/-')
inv(25,'display','L25, below the lower middle T label',r'\operatorname{Sl}(2,\mathbb Z); preceding rotated comparison sign')
inv(26,'margin note','Lower-left footer',r'\margin{19}','lighter hand, attribution unestablished')

def doubt(place,reading,alternatives,confidence,reason):
    r['doubts'].append({'place':place,'reading':reading,'alternatives':alternatives,
        'confidence':confidence,'reason':reason})
doubt('L01, first relation',r'\unsure{=|\simeq}',r'=; \simeq','medium',
      'The horizontal components are retraced and the upper component has curvature. The crop does not establish whether that curvature belongs to a comparison form or to retracing of equality. '+cref('formula_I'))
doubt('L01, broad letter and earlier stroke state',r'\unsure{S_Q|I_Q}',r'S_Q; I_Q; unresolved earlier letter state','low',
      'The broad curved top and bottom admit S, while an interior upright and dark overlap also admit I. No complete independent earlier glyph is exposed. '+cref('formula_I'))
doubt('L07, last small letter in the first pairing',r'(ad)(b\unsure{e|c})=Q_0',r'e preferred; c retained','medium',
      'An upper closed triangular loop and continuous low return support the preferred e. Retracing can also account for the closure, so c remains possible. No letter was supplied to complete a prescribed set. '+cref('partitions'))
doubt('L10, complete faint upper annotation',upper_pencil,
      'tétraèdre + b and (carré + are candidates; intervening traces have no secure verbal or algebraic reading','low',
      'The completion crop includes the uppermost and initial tall strokes. Several low letter strokes, the last loop/stem of the first group and intervening curves/obliques remain weak. The whole retained span is represented, including the unresolved middle trace. '+cref('upper_pencil_completion'))
doubt('L12, first faint lower annotation and cancellation extent',under_first,
      r'candidate \omega_I\times J with preceding intersecting strokes; extent of deletion unresolved','low',
      'The leading strokes cross one another before the omega-like form. The following lowered I, cross and angular terminal form remain visible. The crop does not expose a separate strike establishing that every following sign was deleted. '+cref('equivalence'))
doubt('L13, further faint lower formula',under_second,
      'Graphical reading only; complete algebraic contents unresolved','low',
      'A loop with internal diagonal, upright, paired short strokes, a small curve/upright, long oblique and terminal curl are visible. Their complete character sequence is not securely legible. '+cref('equivalence'))
doubt('L17, label above the open pencil sketch',r'\unsure{D(Q)}',r'D(Q) remains a candidate','medium',
      'The first upright/loop, enclosing curves and inner Q-like loop/descender are faint and retraced. The open sketch is secure independently of the label reading. '+cref('pencil_shape'))
doubt('L16, L20, L22 and L24, five group-letter labels',r'\unsure{\mathfrak S}',
      'Preferred fraktur S; precise alphabet identification retained as doubtful','medium',
      'The curved body and inward return fit the supplied notation-table candidate, but the exact alphabet style is not independently resolved here. All five occurrences remain locally marked. '+cref('exact_sequence')+'; '+cref('lower_diagram'))
doubt('L20, raised hatched cluster at the middle T label',hatch,
      'Crossed short upright/curved strokes; an underlying exclamation character is only a witness candidate','low',
      'The hatch covers the component strokes and the outgoing line begins in the cluster. A complete underlying character cannot be separated. The actual cluster and a local question marker are retained. '+cref('lower_diagram'))
doubt('L24, final lowered digit beside the lower Pi',r'\unsure{5|3}',r'5 preferred; 3 retained','medium',
      'The dark deep downstroke and lower return favor 5. The pale overlapping span prevents a secure separation of all strokes. The clear middle-row 3 was compared only as a local hand form. '+cref('lower_diagram'))
doubt('L24, whole pale span beside the lower Pi',overlay,
      'Full graphical overlay; a lone superscript and a completed parenthetic formula remain unestablished','low',
      'The bent left enclosure, oblique/return, detached low stroke, diagonal/right return and terminal curve occupy a wider span than a lone raised digit. The full trace is kept without choosing its contents from an expected formula. '+cref('lower_diagram'))
doubt('Upper drawing, far-right pencil sphere',figs['right'],
      'Direct contours retained; classification of individual short marks unresolved','medium',
      'Three layered transverse contours and several uneven short marks are exposed. Their head-like forms do not all establish a single regular arrow convention, so the saved direct paths retain their shapes. '+cref('drawing_right'))

r['notation']=[
 {'form':r'I\unsure{=|\simeq}\unsure{S_Q|I_Q}=\coprod_{d\in D_Q}d',
  'meaning':'The page writes this first formula; the first relation and letter remain unresolved. No further definition is supplied here.',
  'evidence':'L01; broad retraced letter, lowered Q and complete coproduct expression. '+cref('formula_I'),
  'scope':'This complete formula only.'},
 {'form':r'A_Q=\prod_{d\in D_Q}d; C_Q=\bigwedge_{d\in D_Q}d=\perp',
  'meaning':'Written product and wedge expressions. The wedge expression has a pale terminal equality and perpendicular form.',
  'evidence':'L02–L03; both complete formulas inspected, including pale terminal strokes. '+cref('formula_A')+'; '+cref('formula_C'),
  'scope':'These two formula baselines; no algebraic verification performed.'},
 {'form':r'\omega_Q=C_Q\wedge D_Q; \omega_I\simeq\omega_J\simeq C_Q\simeq J\setminus\{Q\}',
  'meaning':'The two source formula baselines are transcribed as written claims.',
  'evidence':'L04–L05; omega loops, subscripts, wedge and retraced comparison signs checked in full. '+cref('omegas'),
  'scope':'These two baselines only; their asserted relations have not been proved in this reading.'},
 {'form':r'(ad)(b\unsure{e|c})=Q_0; (b,d)(ac)=Q_1; (cd)(ab)=Q_\infty',
  'meaning':'Three written pairings beneath the a b c d header; the first row keeps its actual letter doubt and the second its comma.',
  'evidence':'L06–L09; retraced first-row final letter, second-row separated comma and indices checked. '+cref('partitions'),
  'scope':'All three displayed pairing rows, without repair from the header.'},
 {'form':r'\unsure{\mathfrak S}',
  'meaning':'Local group-letter candidate retained from the supplied notation table; exact alphabet identity remains uncertain.',
  'evidence':'Curved body and inward return in two short-sequence labels and three lower-diagram labels. '+cref('exact_sequence')+'; '+cref('lower_diagram'),
  'scope':'Five occurrences on this page; no universal handwriting rule inferred.'},
 {'form':r'\rotatebox{90}{$\simeq$}',
  'meaning':'Rendering of a vertically disposed curled stroke beside a straight bar.',
  'evidence':'Two first-column comparison marks and the mark below the lower middle label have this disposition. '+cref('lower_diagram'),
  'scope':'Three visible occurrences on this page.'},
 {'form':r'\operatorname{Sl}',
  'meaning':'Literal mixed-capitalization operator in the attached annotations.',
  'evidence':'L23–L25; initial capital followed by a lower tall letter retained from the source. '+cref('lower_diagram'),
  'scope':'Three written operator occurrences; no expansion or case normalization.'},
 {'form':r'/-',
  'meaning':'Literal terminal slash and minus of the last right-hand annotation.',
  'evidence':'L24; exposed oblique slash followed by a single horizontal stroke. '+cref('lower_diagram'),
  'scope':'This endpoint only; no plus sign or further denominator element supplied.'}
]
r['abbreviations']=[
 {'form':'cart','expansion':'Possibly cartésien; the source remains cart, without a supplied full stop or expansion.'},
 {'form':'Aff','expansion':'No expansion is written on this page; retained as the literal operator.'},
 {'form':'Sl','expansion':'No expansion is written on this page; mixed capitalization retained.'}
]
r['hand']=[
 {'habit':'Heavy retracing can close a small loop or leave an interior upright visible.',
  'places':'L01 broad letter and L07 final small letter of the first pairing.',
  'scope':'These two inspected loci only; S/I and e/c remain local doubts.',
  'witness_errors':'C/H give a definite c in the pairing; the preferred e has retained c alternative. H gives a definite S in L01.'},
 {'habit':'Pale pencil traces coexist with darker writing and sometimes overlap it.',
  'places':'L03 terminal signs; L10–L13 draft spans; L24 pale span beside the lower Pi.',
  'scope':'The inspected spans; relative colour alone has not been used to assign a deletion or chronological state.',
  'witness_errors':'H omits the pale wedge endpoint and upper/further drafts; C/H narrow the lower overlay to proposed symbols.'},
 {'habit':'The two Pi labels have two uprights joined by a top bar.',
  'places':'Middle and lower rows of the lower diagram.',
  'scope':'Both exposed Pi forms on this page.',
  'witness_errors':'H substitutes lower-case pi at these two labels.'},
 {'habit':'A curled stroke beside a straight bar is written vertically.',
  'places':'Two first-column comparisons and the comparison below the lower middle label.',
  'scope':'All three occurrences in the lower crop.',
  'witness_errors':'C places horizontal comparison labels at the first two; H uses shaft/label constructions there. The transcription keeps the vertical form.'},
 {'habit':'Drawing contours distinguish continuous, dotted, retraced and interrupted strokes, in dark and reddish inks and pale pencil.',
  'places':'Isolated sphere and all five cropped parts of the connected network.',
  'scope':'The six saved drawing crops only.',
  'witness_errors':'C smooths repeated contours and several gapped arcs, omits two left equatorial points and simplifies layered right-hand contours.'},
 {'habit':'Two small detached ticks repeat an adjacent annotation; an endpoint elsewhere is a single horizontal stroke after a slash.',
  'places':'Middle and lower right-hand annotations in the lower diagram.',
  'scope':'These two written shorthand forms only.',
  'witness_errors':'H expands the ticks to a comparison sign and supplies plus-minus in the final annotation while noting the visible minus.'}
]
r['notes']=(
 '148_scan020, L01–L05: the page writes a coproduct expression with two local doubts, a product expression, a wedge expression ending in a pale equality/perpendicular form, an omega equality and a chain of comparison signs ending at J minus the displayed singleton Q. These are recorded source statements. Their reading has not established their mathematical assertions.\n\n'
 'L06–L09: the a b c d header is followed by three pairing rows and a frame along the top and right. The first row keeps e|c under retracing; the second keeps the exposed comma between b and d. No pairing was altered to satisfy a set or a mathematical pattern. L10 is a weak upper pencil draft with candidate words and a graphical intervening span. L11 gives the tetrahedron/diagonal and square/codiagonal expression, with orienté raised, underlined and attached above the first noun. The brace covers a short central span. L12–L13 preserve two faint lower draft lines graphically. L14–L15 give the two product expressions beneath that brace.\n\n'
 'L16 is the short sequence beginning with 0 and ending with 1; the two group-letter forms retain local alphabet doubts. L17 has the doubtful D(Q) label and an open pencil sketch with separated strokes. L18–L19 give the two written rho/sigma relations, a left brace and a pencil frame with corner gaps. No proof or calculation was performed on these relations by this reader.\n\n'
 'L20–L25 contain the lower three-row diagram, the cart annotation and the adjacent Aff/Sl expressions. The source indices, the first separate exclamation, the crossed raised cluster, the lower 5|3 doubt, the entire pale overlay, the two double shafts, the blunt middle endpoint, the three vertical comparison forms, the two ditto ticks and terminal /- are retained. The locally doubtful group-letter family is kept in all five occurrences across the short sequence and this diagram. The root supplied the final lower section from the same inspected source crop; its exact TeX is merged into the page and reused in change 12 and the complete lower blind-reading box.\n\n'
 'The drawings retain the isolated sphere and the connected network of ten sphere outlines and two tetrahedral outlines. Their direct paths preserve marked points, labels, repeated and interrupted contours, selected heavy edges, coloured solid/dotted paths and irregular short marks. No unavailable H drawing file was used for comparison. H’s supplied drawing description and editorial notes are witness apparatus rather than extra source prose.\n\n'
 'Two pale blue printer-pattern regions were inspected and excluded as mirrored reverse-side show-through: the large repeated block at middle right and the small repeated rows across the middle. Their original C marks remain accounted for in decisions and their neutral material-inspection boxes have empty source readings. Crossing manuscript ink is retained in the adjoining scoped boxes. There is no written head manuscript number; the lower-left lighter 19 is retained as a margin number with its hand attribution unestablished.\n\n'
 'The whole scan and both supplied full-resolution halves were inspected once each before tight crops. Nineteen initial crops and one upper-pencil completion crop were saved and inspected; the completion was needed for the first tall stroke and weak upper span near the original crop edge. All twenty crops were also personally viewed by the root for adjudication. No further crop was made of a decided locus. No OCR, external research, TeX compilation, blind-reading crop or other page was accessed in this assignment.\n\n'
 'No mathematical proof, group enumeration or formal certificate was performed, read or incorporated by this reader for this page. check_events is therefore empty. The root’s separate mathematical check is reserved for the root to merge with its own attribution and scope; it has not been used to choose any glyph.'
)

omega_reading=r'\[\begin{aligned}\omega_Q&=C_Q\wedge D_Q\\\omega_I&\simeq\omega_J\simeq C_Q\simeq J\setminus\{Q\}\end{aligned}\]'
box_specs=[
 ('B01','Upper-left isolated drawing',crops['isolated_sphere'],figs['isolated']),
 ('B02','Upper drawing branch and connector',crops['drawing_upper'],figs['upper']),
 ('B03','Left drawing branch and connector',crops['drawing_left'],figs['left']),
 ('B04','Central drawing',crops['drawing_centre'],figs['centre']),
 ('B05','Right drawing branch and connector',crops['drawing_right'],figs['right']),
 ('B06','Lower drawing branch and connector',crops['drawing_lower'],figs['lower']),
 ('B07','Middle-right pale repeated pattern; darker drawing and handwriting excluded',crops['large_bleed'],''),
 ('B08','First standalone formula at left',crops['formula_I'],r'$I\unsure{=|\simeq}\unsure{S_Q|I_Q}=\coprod_{d\in D_Q}d$'),
 ('B09','Second standalone formula at left; adjoining upper line excluded',crops['formula_A'],r'$A_Q=\prod_{d\in D_Q}d$'),
 ('B10','Third standalone formula at left',crops['formula_C'],r'$C_Q=\bigwedge_{d\in D_Q}d=\perp$'),
 ('B11','Two succeeding formula baselines at left',crops['omegas'],omega_reading),
 ('B12','Framed middle-left block; pale printing excluded',crops['partitions'],sections['PARTITIONS']),
 ('B13','Faint upper annotation above main middle expression; darker overlapping writing excluded',crops['upper_pencil_completion'],upper_pencil),
 ('B14','Main middle expression with raised annotation and lower brace formulas; faint pencil drafts and pale printing excluded',crops['equivalence'],live_equivalence),
 ('B15','First faint annotation below left portion of middle expression; darker main expression and pale printing excluded',[623,1057,827,1119],under_first),
 ('B16','Second faint annotation below left portion; pale printing excluded',[675,1113,888,1166],under_second),
 ('B17','Pale repeated rows across the middle; front-side handwriting and drawings excluded',crops['printer_bleed'],''),
 ('B18','Short middle-lower sequence; pale printing excluded',crops['exact_sequence'],sections['EXACT_SEQUENCE']),
 ('B19','Small lower-left pencil sketch and label',crops['pencil_shape'],sections['PENCIL_SHAPE']),
 ('B20','Framed lower-right formula block; pale printing excluded',crops['relations'],sections['RELATIONS']),
 ('B21','Lower diagram and adjacent annotations',crops['lower_diagram'],root_lower),
 ('B22','Lower-left marginal handwriting',crops['margin_number'],r'\margin{19}')
]
for ident,kind,box,reading in box_specs:
    r['second_boxes'].append(dict(box=ident,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))

coverage={
 612:'Changes 148_scan020-01 and -02 account for the upper drawings. H’s introductory note and drawing description are editorial witness apparatus; the scan label is metadata.',
 613:'Changes 148_scan020-01, -02 and -03 cover this long C drawing-code span: actual drawing contours retained, mirrored printer pattern excluded. No unseen H drawing file was compared.',
 614:'M0165 remains undecided as S_Q|I_Q; complete formula inspected in formula_I. The first relation also retains a local =|simeq doubt. H’s single S is not used to force a choice.',
 615:'Change 148_scan020-04: the complete wedge formula exposes the pale terminal equality and perpendicular form; M0166 resolves to the first reading.',
 616:'Same-reading layout syntax: aligned environment versus separate displays. The complete omega baselines were checked in omegas.',
 617:'H’s note about surcharge and retraced comparison signs is editorial. The initial relation/letter doubts and unresolved earlier state are explicit; the complete omega signs were inspected, with no added prose from this note.',
 618:'Same-reading array/gathered layout syntax. Frame and lexical details are separately covered by change 148_scan020-05.',
 619:'H’s backslash-comma is TeX thin spacing inside ad; it is not a source comma. The first pair has no separately exposed comma. Checked in partitions.',
 620:'H’s backslash-comma is spacing inside its bc reading. The actual last small letter remains preferred e with c alternative under retracing; change 148_scan020-05 records that lexical change.',
 621:'H’s backslash-comma is spacing inside ac. The source pair has no separately exposed comma; checked in partitions.',
 622:'H’s backslash-comma is spacing inside cd. The source pair has no separately exposed comma; checked in partitions.',
 623:'H’s backslash-comma is spacing inside ab. The source pair has no separately exposed comma; checked in partitions.',
 624:'Same-reading gathered/array closing syntax. The actual top/right frame is retained in change 148_scan020-05.',
 625:'Change 148_scan020-06 preserves the weak upper pencil annotation, including M0167–M0169; completion crop contains its full upper extent. Change -05 corrects H’s editorial left/top frame placement to the visible top/right strokes.',
 626:'Change 148_scan020-07 retains the short central brace and its attached formulas. The macro boundary itself has no source content.',
 627:'H’s note describes the brace and the faint line below the left term. Changes 148_scan020-07 and -08 give their actual positions and full retained ink; witness explanatory prose is excluded.',
 628:'M0170 remains a whole graphical doubt with unresolved cancellation extent. Change 148_scan020-08 retains the intersecting leading strokes and further faint line; H’s definite biffé state is not imposed across the whole span.',
 629:'Change 148_scan020-09: the mirror-transform/font wrapper belongs to C’s representation of reverse-side printer show-through, which is excluded from source text.',
 630:'Change 148_scan020-09 excludes the six speculative printer strings. The adjacent short sequence is retained in full and inspected in exact_sequence; original printer marks M0171–M0176 are accounted for.',
 631:'Same-reading connector syntax: tikzcd arrow[r] versus inline to. The full short sequence and all endpoints were inspected in exact_sequence; group-letter alphabet doubt remains local.',
 632:'Same-reading connector syntax in the short sequence; the actual complete formula was inspected in exact_sequence.',
 633:'Same-reading connector syntax in the short sequence; the final numeral and complete sequence were inspected in exact_sequence.',
 634:'Change 148_scan020-10 retains the open pencil sketch and its doubtful label. Change -11 retains the actual gapped relations frame. The long code span also contains drawing/display wrappers.',
 635:'Aligned/left-brace versus cases is same-reading formula syntax. Change 148_scan020-11 concerns the physical frame gaps; the displayed relations are preserved.',
 636:'Row-separation setting is layout syntax. The complete source arrangement is reproduced in the lower direct drawing, change 148_scan020-12.',
 637:'Order of the first T superscript and subscript in TeX is same-reading syntax. The separate first exclamation and 0,4 are retained in change 148_scan020-12.',
 638:'Companion TeX-order fragment to row 637; the source first exclamation remains separately legible. The later hatched cluster is treated independently.',
 639:'Change 148_scan020-12 retains the vertically disposed curled-stroke/bar comparison. H’s no-head shaft construction supplies a shaft not separately exposed for this comparison.',
 640:'Change 148_scan020-12 renders the actual vertical comparison form, rather than a horizontal label. The complete lower crop supplies its disposition.',
 641:'Companion comparison-macro fragment to rows 639–640; no extra stroke is inferred from draw=none, quote placement or label-side syntax.',
 642:'Change 148_scan020-12 and the unnumbered decision retain the complete raised hatched cluster, without a secure underlying exclamation. H’s thin spacing within 04 is syntax; the visible lowered digits are retained.',
 643:'Change 148_scan020-12: the middle Pi-to-T connector has two shafts, and the first-column comparison is vertically disposed. Both were inspected in the full lower crop.',
 644:'Prime ordering in TeX is syntax; the actual middle T prime is retained in change 148_scan020-12.',
 645:'Companion prime/index-spacing fragment to row 644. The source prime and adjacent lowered digits are kept; no additional prime or written comma is supplied from thin spacing.',
 646:'Change 148_scan020-12: the middle terminal connector has a blunt upturned end. Its direct path preserves that endpoint without a triangular head.',
 647:'Change 148_scan020-12 retains M0179 as 5|3 and M0180 as the complete pale graphical overlay. Neither witness’s narrowed completed lower label is imposed.',
 648:'Change 148_scan020-12 records the source’s vertical comparison form and the lower double-shaft connector. The macro boundary does not supply an extra joining stroke.',
 649:'Change 148_scan020-12: the lower Pi-to-T connector has two shafts, and the adjacent vertical comparison has its own curled-stroke/bar form.',
 650:'Change 148_scan020-12 places cart inside the upper square and retains the attached annotations. H’s note about the diagram’s medium is editorial.',
 651:'The semicolon belongs to H’s editorial annotation list. No corresponding source punctuation is supplied.',
 652:'Change 148_scan020-12 preserves the two exposed ditto ticks before the middle Sl annotation; H expands them to a comparison sign.',
 653:'The semicolon belongs to H’s editorial annotation list. No corresponding source punctuation is supplied.',
 654:'Change 148_scan020-12 retains literal /-. H’s annotation expands it to plus-minus while its accompanying note records the visible minus.',
 655:'Continuation of H’s editorial explanation of /-. The visible terminal stroke is preserved without a supplied plus or added punctuation.',
 656:'Change 148_scan020-13 retains margin 19, omitted by H. H’s remaining lower-diagram commentary is editorial: M0178 resolves 1, M0179 stays 5|3, M0180 and the raised hatched cluster remain graphical doubts in change -12.'
}
assert set(coverage)=={d['row'] for d in diffs}
r['diff_coverage']=[{'row':d['row'],'disposition':coverage[d['row']]} for d in diffs]
r['deletion_insertion_check']=(
 'L01: the broad letter has retraced curves and an interior upright. The possible earlier state mentioned by H cannot be separated as a complete character, so no definite deleted letter is supplied. '+cref('formula_I')+'\n'
 'L10: the faint upper pencil span is retained in full, including the intervening graphical trace. Its medium and position do not by themselves establish a cancellation chronology. '+cref('upper_pencil_completion')+'\n'
 'L11: orienté is a raised insertion above tétraèdre, with an underline and short attachment stroke. The direct path preserves those marks and the source attachment. '+cref('equivalence')+'\n'
 'L12–L13: intersecting strokes precede the candidate omega-product line, but a strike across every following sign is not separately established. C’s alternate whole-deletion state and H’s definite biffé description remain unresolved in extent. The further faint formula line is retained graphically rather than omitted. '+cref('equivalence')+'\n'
 'L20: the second T’s raised cluster is visibly hatched. Its actual upright/curved components and the hatch are drawn, with a local question marker; C’s nested exclamation candidate is not promoted to an exposed underlying character. '+cref('lower_diagram')+'\n'
 'L24: dark lowered digits overlap a pale wider span. The 5|3 doubt remains local, and the full pale span is drawn. No single exponent or completed parenthetic group is substituted for the overlap. '+cref('lower_diagram')+'\n'
 'Group-letter retracing has not been converted into asserted deleted labels. The mirrored printer patterns are excluded reverse-side show-through, not cancelled front-side text. All C insertion/deletion alternatives and H correction comments on this page were checked at their full formula or annotation loci.'
)

# REMAINING_REPORT_FIELDS
(B/'work'/f'{P}_report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report_complete':True,'changes':len(r['changes']),'marks':len(r['decisions']),
 'inventory':len(r['inventory']),'doubts':len(r['doubts']),'second_boxes':len(r['second_boxes']),
 'diff_rows':len(r['diff_coverage'])}))
