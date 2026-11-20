"""Main-reader decisions from three complete returns and fourteen delivered local crops."""
import copy,json,re
from adjudication_io import PageDecision,OUT

p=PageDecision('134-2_scan152','v07',base='r1')
r1,r2,r3=(p.readers[r] for r in ('r1','r2','r3'))
cm={1:'main/combine.jpg',2:'r1/01_lf_exponent.png',3:'main/six_quotes.jpg',
4:'r2/02_split_noun.jpg',5:'r1/03_deleted_initial.png',6:'r3/04_schemas_punctuation.png',
7:'main/les_coefficients.jpg',8:'r2/04_coefficient_insertions.jpg',9:'r2/04_coefficient_insertions.jpg',
10:'r2/04_coefficient_insertions.jpg',11:'r2/04_coefficient_insertions.jpg',12:'r1/04_deleted_article.png',
13:'r1/04_deleted_article.png',14:'r2/04_coefficient_insertions.jpg',15:'r1/06_analytic_end_guide.png',
16:'r1/06_analytic_end_guide.png',17:'r1/06_analytic_end_guide.png',18:'r2/04_coefficient_insertions.jpg',
19:'r2/05_singularites.jpg',20:'r3/07_etre_dot.png',21:'r1/08_separe.png',22:'r1/08_separe.png',
23:'r2/08_bottom_edge.jpg',24:'r2/08_bottom_edge.jpg',25:'r2/08_bottom_edge.jpg'}
for n,crop in cm.items():
    p.change(n,crop=p.crop(crop),decision='Main reader inspected this existing or newly made local crop and adopts the described ink reading/state.')
p.change(2,final=r'Lf^{\alpha}',against_c=True,confidence='high',
    readers={'r1':r'Lf^{\unsure{\alpha|*}}','r2':r'Lf^{\alpha}','r3':r'Lf^\alpha'},
    evidence='The raised mark has a closed left loop crossed by the rising right stem and an oblique exit. The nearby lowered star is an open intersection of strokes, without that loop.',
    decision='Resolve the superscript as alpha, agreeing with r2/r3. The usual pullback notation does not replace the actual looped glyph.',
    consequence='Lf bears alpha rather than H’s star; C’s alpha/star doubt is resolved from the contrasting local shapes.')
p.change(4,readers={'r1':r'\unsure{fonctions}','r2':'fonctions','r3':r'\unsure{fonctions}'},
    evidence='The crop includes both physical segments. A long f and a later tall t-like stroke with a high point precede the next-line ons; the middle low strokes remain contracted. There is no visible formalismes ending.',
    decision='Retain C’s fonctions doubt, agreeing with r1/r3 on uncertainty; r2’s unqualified reading is too strong for the compressed middle.',
    consequence='The proposed identity is stated between the uncertain fonctions, not H’s unqualified formalismes.')
p.change(9,decision='Use the literal paired quotation strokes. The looped lowercase l is the same letter represented by r2/H with ell; that encoding-only choice is excluded from error counts.',
    readers={'r1':"``$l$-adiques''",'r2':"``$\\ell$-adiques''",'r3':"``$l$-adiques''"})
p.change(10,final='TikZ long upper arm, short left descent beside premiers, and small right upturn',
    source_bbox=[543,1023,1170,1093],
    readers={'r1':'Long guide extended to y=1140 with a low foot beside the analytic insertion.',
             'r2':'Short left descent ending beside premiers at about y=1093.',
             'r3':'Long guide extended to y=1140 with a low foot.'},
    evidence='The upper rule bends down beside premiers and ends there. A nearby lower vertical stroke is displaced slightly to the left and crosses the baseline of faisc.; it is the f of that word, not a further length of the guide.',
    decision='Adopt r2’s short left descent. Do not duplicate the neighbouring f stem as part of the independent guide. The guide has no arrowhead.')
p.change(11,consequence='The prime-to-residue-characteristic condition remains live and underlined; H incorrectly treats the entire condition as replaced/cancelled.')
p.change(12,readers={'r1':r'a\unsure{\.{u}|u}x','r2':'aux','r3':'aux'},
    decision='Retain the visible compact upper point with uncertain intent. It is positioned above u rather than converted to baseline punctuation.')
p.change(13,readers={'r1':r'\deleted{\unsure{la|le}}','r2':r'\deleted{\unsure{le|la}}','r3':r'\deleted{\unsure{la|le}}'},
    decision='Retain la first from the rounded terminal body, with le as an unresolved alternative. H’s note acknowledges cancellation but supplies neither letters nor a doubt mark on the omitted article.')
surname=r'\unsure{Rüget|Ruget|Rüguet|Ruguet}'
p.change(15,final=surname,confidence='low',
    readers={'r1':r'\unsure{Ruget|Rüget}','r2':'Ruget','r3':r'\unsure{Ruguet|Ruget}'},
    evidence='The capital R is followed by a u-like body with two separate dark raised strokes over it, then a descending g and the ending before crossed t. Low minims after g do not securely distinguish a compressed e from ue.',
    decision='Keep both independent uncertainties: possible diaeresis and possible extra u after g. Rüget is first because the two upper strokes are actually present. No external name or bibliography settles the spelling.')
p.change(17,readers={'r1':'Clear semicolon drawn as two strokes inside the guide.',
                    'r2':r'\unsure{;} inside the guide.',
                    'r3':r'\inserted{;} inside the guide; against-H flag false.'},
    decision='The upper oblique dot and curved lower stroke securely form a semicolon. Reproduce the two strokes at their actual position inside the guide. Logical attachment before/after the analytic line remains unassigned; both witnesses flatten it to a different position, so both difference flags are true.')
p.change(20,readers={'r1':r'\unsure{.} below initial u, with zero-width positioning.',
                    'r2':r'\unsure{.} in a local figure after un.',
                    'r3':'Visible low mark recorded in a comment as probable stray/copy mark.'},
    decision='Retain the actual short vertical dark mark with uncertain intent below the initial u. Its position does not support a definite comma after the word.')
p.change(21,consequence='The inserted separatedness qualification is now resolved instead of remaining uncertain in C.')
p.change(24,readers={'r1':r'\unsure{car}','r2':r'\unsure{car.|car}','r3':r'\unsure{car.|car}'},
    decision='Keep the uncertain surviving abbreviation without a hypothetical point. The crop’s black edge removes the lower contours and any possible punctuation; absence of recoverable punctuation is not an assertion about the uncut manuscript.',
    consequence='The final characteristic abbreviation stays uncertain because of clipping; no outside-page wording or punctuation is restored.')

# Additional distinct loci from the other complete returns.
for n in [11,21,25,26,27,28]:
    x=copy.deepcopy(r2['changes'][n-1])
    if n==11:
        x['final']="\\inserted{(de torsion ou ``$l$-adiques'')}, before the live underlined condition"
        x['decision']='The long guide turns down into the gap after discrets and before premiers. Preserve C’s insertion point; H places the addition after a falsely cancelled condition.'
    elif n==21:
        x['readers']={'r1':'No separate point transcribed.','r2':x['final'],'r3':'No separate point transcribed.'}
        x['decision']='A compact round dark point is visibly detached below the early part of stratifiés. Preserve it uncertainly at the left of the local guide drawing; do not assign baseline punctuation.'
    elif n==25:
        x['final']=r'\unsure{.} below the initial portion of avec'
        x['readers']={'r1':'No separate point transcribed.','r2':r'\unsure{.} in a local drawing below avec','r3':'No separate point transcribed.'}
        x['decision']='Retain the actual compact dark point with uncertain intent, using zero-width positioning below the beginning of avec.'
    else:
        word={26:'coeff.',27:'torsion',28:'premier'}[n]
        x['readers']={'r1':word,'r2':x['final'],'r3':word}
        x['decision']='Adopt r2’s uncertainty. The cropped edge and fading prevent certainty about '+('the abbreviation point, although the letters coeff are readable.' if n==26 else 'the complete surviving word, although the listed reading best fits its upper traces.')
    p.add(x)
accent=copy.deepcopy(r3['changes'][19])
accent.update(readers={'r1':'peut-être','r2':'peut-être','r3':r'peut-\unsure{\={e}tre|être}'},
    decision='Retain r3’s literal flat-accent alternative first: the detached stroke is shallow and almost horizontal, with no clear peak. A flattened handwritten circumflex remains possible.',
    crop=p.crop('r3/07_etre_dot.png'))
p.add(accent)

# Consolidate the complete r1 text. Figure code is selected by visible geometry,
# not by arbitrary differences in TikZ scale or control-point formatting.
t2=(OUT/'readers/134-2_scan152/r2/reading.tex').read_text()
figpat=r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}'
f1=re.findall(figpat,p.text,flags=re.S)
f2=re.findall(figpat,t2,flags=re.S)
assert len(f1)==4 and len(f2)==6,(len(f1),len(f2))
p.text=p.text.replace(f1[0],f2[0]).replace(f1[2],f2[2])
p.text=p.text.replace('% Source guide below the parenthetic addition: long upper arm, left downward bend, and short left foot; no arrowhead. The downward leg passes beside premiers and through the interlinear-note zone.',
    '% Source guide below the parenthetic addition: long upper arm, short left descent beside premiers, and right upturn; no arrowhead. The separate lower crossed stem belongs to f in faisc.')
p.text=p.text.replace('% Guide immediately below singularités: the left end bends down just before the baseline à la; the long arm continues rightward beneath the added word.',
    '% Guide immediately below singularités, with an uncertain detached point to its left below early stratifiés. The g descender above is separate from the guide.')
p.text=p.text.replace(r'Lf^{\unsure{\alpha|*}}',r'Lf^{\alpha}')
p.text=p.text.replace(r'\unsure{Ruget|Rüget}',surname)
p.text=p.text.replace('partout, peut-être,',r'partout, peut-\unsure{\={e}tre|être},')
p.text=p.text.replace('disons, avec un anneau de coeff. $\\Lambda$ de torsion premier à',
    'disons,\n% Detached point beneath the initial portion of avec; intent uncertain.\n'+
    r'\makebox[0pt][l]{\hspace{0.1em}\raisebox{-1.4ex}[0pt][0pt]{\unsure{.}}}avec un anneau de \unsure{coeff.|coeff} $\Lambda$ de \unsure{torsion} \unsure{premier} à')
assert r'\unsure{premier}' in p.text

# One unresolved row per actual locus, without duplicating nested doubts from
# the separate underline-state and placement rows.
doubt_indices=[4,5,12,13,15,20,23,24,27,28,29,30,31,32]
p.data['doubts']=[]
for n in doubt_indices:
    x=p.data['changes'][n-1]
    p.data['doubts'].append({'location':x['location'],'reading':x['final'],'alternatives':[],
        'confidence':x['confidence'],'reason':x['evidence']+' '+x.get('decision',''),'crop':x['crop']})
p.data['doubts'].append({'location':'Logical attachment of semicolon in right insertion guide',
    'reading':'Clear semicolon at its physical position inside the guide',
    'alternatives':['attachment before analytic addition','attachment after analytic addition'],
    'confidence':'low','reason':'Glyph and placement are clear, but the ink does not prescribe a unique flattened reading order. The actual strokes are reproduced without choosing one.',
    'crop':p.crop('r1/06_analytic_end_guide.png')})

inv=p.data['inventory']
for x in inv:
    if x['element']=='Left guide beneath the added parenthesis':
        x.update(first_words_or_objects='Long upper arm, short left descent beside premiers, right upturn',source_bbox=[543,1023,1170,1093])
for name,bbox,pos in [('Detached point below stratifiés',[1157,1363,1168,1376],'Below early letters of stratifiés, to the left of the insertion guide'),
                     ('Detached point below avec',[788,2270,801,2285],'Below initial portion of avec, above clipped final line')]:
    inv.append({'sheet_kind':'letter','hand':'author manuscript hand; intentional status uncertain',
        'element':name,'kind':'text','position':pos,'first_words_or_objects':'Uncertain isolated point retained spatially',
        'transcribed':'yes','source_bbox':bbox})
def first_y(x):
    b=x.get('source_bbox',[0,9999,0,9999]);return min(z[1] for z in b) if isinstance(b[0],list) else b[1]
p.data['inventory']=sorted(inv,key=first_y)
p.data['slips']=[]
p.data['notes']="""Letter continuation, author page 7, archive pencil folio 152. No new date, salutation or signature occurs. Section A begins with the author’s claim that the six-operation formalism contains the definition of homology and an essential identity between the uncertain “fonctions” homologiques and cohomologiques. The opening Lf superscript is alpha: the closed loop and crossing stem differ from the adjacent open-stroke star. Mathematical expectation prompted this inspection but did not override the visible glyph. The exceptional exclamation marks, derived L/R lettering, double-struck C, 0, k and Lambda were individually read by all three readers; this is visual collation, not a proof check.

The page lists contexts involving quasi-coherent sheaves on schemes, topological spaces with arbitrary coefficients, étale cohomology, and an inserted analytic coherent-sheaf case. The references to the Hartshorne seminar, Verdier/Bourbaki and SGA 5 are the author’s references; no external bibliography was consulted. The analytic adjective reads analytiques rather than H’s an. complexes. The surname after Verdier has unresolved raised marks over u and a possible extra minim after g, recorded as Rüget/Ruget/Rüguet/Ruguet rather than normalised from a known name.

The prime-to-residue-characteristic qualification is live and underlined. Only the small intervening article is cancelled, with la/le unresolved. The torsion or l-adic parenthesis is inserted before that qualification; H’s interpretation of the entire condition as replaced is contradicted by the baseline and guide. The looped lowercase l is represented consistently by l; ell is an equivalent typographic encoding here and not a separate symbol error. The short upper guide ends beside premiers; the separate lower crossed vertical is the f of faisc., not an extension of the guide. Four independent guides are reproduced in TikZ. A clear semicolon stays inside the right guide, with its logical attachment to the analytic sentence left unassigned.

The author says the formalism remains to be developed in the crystalline setting and, in characteristic 0, for stratified modules with the inserted qualification “à singularités”. Deligne, Hodge structures over C and motives are mentioned. “je suis persuadé” and “partout, peut-être” preserve his own conviction and qualification. The accent above être is unusually flat and remains a graphic doubt. These are the author’s programmatic statements, not the results of proofs performed in this transcription.

The final sentence starts an étale-cohomology setup on a scheme de t.f. over k. The inserted séparé is resolved from its letters and two accents. The bottom edge physically clips the last baseline: coeff’s point, torsion, premier, la and car remain uncertain. No point or comma is restored beyond the recoverable image. This does not assert that the original uncut manuscript lacked punctuation. Small detached marks above aux, below stratifiés, below initial un and below initial avec are preserved at their positions with uncertain intent; they may include stray pen or reproduction marks. No mathematical or grammatical emendation is made."""
p.data['checks']=[
 {'statement_id':'134-2.152.author.six_operations','type':'carried as background without fault found',
  'outcome':'The author’s homology/cohomology claim is described as his assertion. No construction, identity proof or six-operation theorem was checked; glyph and word inspections are visual decisions only.'},
 {'statement_id':'134-2.152.author.contexts','type':'carried as background without fault found',
  'outcome':'The listed sheaf settings, references and proposed further developments were carried as authorial context. Availability of those formalisms and historical attributions was not independently established.'},
 {'statement_id':'134-2.152.document.continuation','type':'carried as background without fault found',
  'outcome':'Section A, author page 7, folio 152, insertions and clipped ending were used as documentary context. No proof claim is attached to their visual transcription.'}]
review=json.loads((OUT/'reviews/134-2_scan152_main_review.json').read_text())
p.save(main_viewed=review['main_viewed'])
p.notation([
 '| 134-2 / 152 | Opening Lf exponent | <code>Lf^{\\alpha}</code> | Closed loop and crossing stem resolve alpha; adjacent Rf star has open intersecting strokes. Expected operation notation does not decide the glyph. |',
 '| 134-2 / 152 | Exceptional operations and derived symbols | <code>Rf_!, f^!, Rf_*, \\overset{\\mathbb L}{\\otimes}, \\mathbb R\\mathrm{Hom}</code> | All three readers inspected every exclamation, subscript, alphabet and operator. |',
 '| 134-2 / 152 | Adic coefficient letter and quotes | <code>l</code>; paired raised double strokes | The looped lowercase letter is the same l represented typographically by ell in H/r2; only the literal quotation shape differs. |',
 '| 134-2 / 152 | Coefficient condition | Live underline; cancelled la/le only | The upper insertion guide is separate from the underline and from the f stem below; parenthesis precedes the live condition. |',
 '| 134-2 / 152 | Insertion guides and detached marks | Four TikZ guides; spatially retained uncertain points | The semicolon remains inside the right guide. Small marks are not forced into baseline punctuation. |'])
p.observation("""All three complete readings, their indexed loci, and their notes/inventories were compared. The main reader inspected eleven existing reader crops and three newly made tight crops, fourteen successful image views in total. An attempted two-image delivery was truncated at a context boundary and neither image was considered viewed; the same existing files were then successfully delivered one at a time, without recropping. The retry is recorded in the main-review journal.

Disagreements concerned uncertainty, accents, the surname, four detached marks, bottom-edge losses and the left insertion guide’s endpoint. R1/r3 extended that guide along the nearby f stem; r2 correctly separated the independent line and letter. The l/ell choice is encoding-only and excluded from counts. R2’s uncertain semicolon glyph was resolved, while its logical attachment remains open. A narrower surname crop preserved genuine graphic questions that the broader r2 crop did not settle. No mathematical proof check was performed on this programmatic page. The next brief adds general guidance on separating letter strokes from guides, l/ell equivalence, and not inventing punctuation beyond a clipped edge.""")
review['status']='adjudication saved; awaiting page commitment'
(OUT/'reviews/134-2_scan152_main_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print('C/H',sum(x['against_c'] for x in p.data['changes']),sum(x['against_h'] for x in p.data['changes']),'doubts',len(p.data['doubts']),'inventory',len(p.data['inventory']))
