from pathlib import Path
import json
from datetime import datetime, timezone
base=Path('/workspace/scratch/b9993b8b5640')
inp=base/'work/inputs/A57-02_57_scan074'
out=base/'out/readers/A57-02_57_scan074/R1'
page=json.loads((inp/'page.json').read_text())
whole=page['whole']; ha=page['half_a']; hb=page['half_b']
C=(inp/'C.tex').read_text()
repls=[
(r"\unsure{\mathbb{X}|X}'",r"\mathbb{X}'"),
(r"\unsure{f^{\bullet}|f^{\circ}}",r"f^{\bullet}"),
(r"\unsure{:|;}",r"\unsure{;|:}"),
(r"\inserted{\handwritten{\unsure{finite}}}",r"\inserted{\handwritten{finite}}"),
(r"\unsure{divect|divert|direct}",r"\unsure{divect|divest|divert|direct}"),
(r"namely $f'$is",r"namely $f^{\bullet}$is"),
(r"\deleted{\unsure{of|on} problem A and B}",r"\deleted{\unsure{for|of|on} problems A and B}"),
(r"\unsure{bacause|because}","bacause"),
("provide a counterexample to the effectivity", "provide a counterrexample to the effectivity")]
for old,new in repls:
 assert old in C,old
 C=C.replace(old,new,1)
(out/'reading.tex').write_text(C)
crop_files=sorted((out/'crops').glob('*.json'))
crops=[json.loads(f.read_text()) for f in crop_files]
cp={f.stem:str(f.with_suffix('.png')) for f in crop_files}
def ev(file,bbox):return {'source':file,'bbox':bbox}
def crop_ev(key):
 r=next(r for r in crops if Path(r['file']).stem==key)
 return ev(r['source'],r['bbox'])
changes=[]
def add(id,place,c,h,reading,dc,dh,kind,hm,confidence,shows,evidence,crop=None,consequence=None):
 changes.append(dict(id=id,place=place,c=c,h=h,reading=reading,differs_c=dc,differs_h=dh,kind=kind,h_marked=hm,confidence=confidence,scan_shows=shows,evidence=evidence,crop=crop,mathematical_consequence=consequence))
add('R1-01','Typed pagination above body',r'\mspage{2}','',r'\mspage{2}',False,True,'omission','no','high','The centred typed line reads - 2 -.',ev(ha,[826,104,933,143]))
add('R1-02','L1: first X prime after and',r"\unsure{\mathbb{X}|X}'",r"X'",r"\mathbb{X}'",True,True,'misread symbol or index','no','medium','The second X has displaced, overlapping diagonal and serif impressions, especially the doubled lower strokes; the immediately preceding plain X provides a local comparison.',crop_ev('01-heavy-X'),cp['01-heavy-X'],'Preserves the visibly doubled impression in the specified mathematical alphabet encoding.')
add('R1-03','L3: Picard homomorphism first raised mark',r'\unsure{f^{\bullet}|f^{\circ}}',r'f^{\cdot}',r'f^{\bullet}',True,False,'misread symbol or index','no','high','The raised mark is a filled round dot, with no open centre.',crop_ev('02-first-f'),cp['02-first-f'])
add('R1-04','L6: between f(O) and h(O)',r'= ',r'\rightrightarrows',r'=',False,True,'misread symbol or index','no','high','Two short horizontal bars are visible; neither has an arrowhead.',ev(ha,[1496,484,1586,535]),None,'The page calls the resulting expression exact; the equality sign is retained as inked.')
add('R1-05','L6: spacing after descent',r'descent,i.e.','descent, i.e.\\ ',r'descent,i.e.',False,True,'insertion or placement','no','high','The i starts immediately after the comma without an intervening typewriter space.',ev(ha,[1077,483,1308,529]))
add('R1-06','L8: homomorphism raised f mark',r"\unsure{f'|f^{\circ}}",r'f^{\cdot}',r"\unsure{f'|f^{\circ}}",False,True,'misread symbol or index','no','medium','The superscript is a short curved hook with white space to its upper left; a prime and an incompletely impressed ring remain supported.',crop_ev('03-homomorphism-f'),cp['03-homomorphism-f'])
add('R1-07','L8: punctuation after specifically',r'\unsure{:|;}','',r'\unsure{;|:}',True,True,'omission','no','low','A tall, partly clipped dark punctuation mark remains at the paper edge. The lower portion extends downward, favouring semicolon, while the cutoff prevents certainty.',crop_ev('04-specific-punctuation'),cp['04-specific-punctuation'])
add('R1-08','L9: raised f in factorisation',r'f^{\circ}',r'f^{\cdot}',r'f^{\circ}',False,True,'misread symbol or index','no','high','The small raised mark is an open ring with a visible pale centre.',ev(ha,[697,634,758,675]))
add('R1-09','L10: raised f in equation',r'f^{\circ}',r'f^{\cdot}',r'f^{\circ}',False,True,'misread symbol or index','no','high','The raised mark after the initial f is a small open ring.',ev(ha,[285,685,333,725]))
add('R1-10','L11: handwritten word before damaged typed word',r'\inserted{\handwritten{\unsure{finite}}}',r'\add{finite}',r'\inserted{\handwritten{finite}}',True,False,'misread word','no','high','The hand writes a tall looped f, dotted i, n, second dotted i, crossed t, and terminal e in the gap after by.',crop_ev('05-finite-direct'),cp['05-finite-direct'])
add('R1-11','L11: damaged typed word after finite',r'\unsure{divect|divert|direct}',r'direct',r'\unsure{divect|divest|divert|direct}',True,True,'misread word','yes','low','The third typed character has a v-shaped body. The fifth character is thick and has competing c/s/r contours. The crop does not establish a separate readable handwritten correction; the H direct reading remains an alternative.',crop_ev('05-finite-direct'),cp['05-finite-direct'])
add('R1-12','L13: family subscript on X',r'X_{i}',r'X_1',r'X_i',False,True,'misread symbol or index','no','high','The subscript has a detached round dot above a short stem and basal serif.',crop_ev('06-family-index'),cp['06-family-index'],'Preserves a letter index i.')
add('R1-13','L13: cancelled final s of conclusions',r'conclusion\deleted{s}','conclusion',r'conclusion\deleted{s}',False,True,'omission','no','high','A final typed s remains under a short dark cancellation stroke after conclusion.',ev(ha,[1372,835,1572,884]))
add('R1-14','L14: crossed word before holds',r'\deleted{\unsure{are}}','',r'\deleted{\unsure{are}}',False,True,'omission','no','medium','The handwritten zigzag crosses the small typed word. The first loop and partial following bodies support are, but the strokes obscure parts of its letters.',crop_ev('07-are-corollary-f'),cp['07-are-corollary-f'])
add('R1-15','L14: raised f mark in Corollary',r"f'",r'f^{\cdot}',r'f^{\bullet}',True,False,'misread symbol or index','no','high','The small raised mark is a solid compact spot rather than a visible open ring; its filled form matches the first homomorphism dot.',crop_ev('07-are-corollary-f'),cp['07-are-corollary-f'])
add('R1-16','L20: first word of cancelled phrase',r'\unsure{of|on}',r'for',r'\unsure{for|of|on}',True,True,'misread word','no','low','A high initial protrusion and several lower serif remnants favour for, but repeated horizontal cancellation strokes obstruct the first token.',crop_ev('08-cancelled-phrase'),cp['08-cancelled-phrase'])
add('R1-17','L20: plural in cancelled phrase',r'problem',r'problems',r'problems',True,False,'omission','no','high','The lower bodies spell problem and a separate final s remains before the space preceding A.',crop_ev('08-cancelled-phrase'),cp['08-cancelled-phrase'])
add('R1-18','L25–L29: left marginal stroke',r'\margin{\handwritten{\figure{\begin{tikzpicture}\draw (0,0) -- (0.08,2.6) -- (0.03,3.0);\end{tikzpicture}}}}','',r'\margin{\handwritten{\figure{\begin{tikzpicture}\draw (0,0) -- (0.08,2.6) -- (0.03,3.0);\end{tikzpicture}}}}',False,True,'drawing or diagram','yes','high','A continuous hand-drawn vertical emphasis stroke runs from below the N.B. heading to beside the line ending finite, with a small bend near the top.',ev(hb,[244,438,281,717]))
add('R1-19','L26: bacause',r'\unsure{bacause|because}',r'bacause',r'bacause',True,False,'misread word','no','high','The first vowel has the closed lower bowl and right stem of a; both a letters in bacause have matching shapes.',crop_ev('09-bacause'),cp['09-bacause'])
add('R1-20','L27: punctuation spacing in couterexample,say',r'couterexample,say',r'couterexample, say',r'couterexample,say',False,True,'insertion or placement','no','high','The s of say follows the comma without a full typewriter space.',ev(hb,[874,551,1195,593]))
add('R1-21','L30: second counterexample spelling',r'counterexample',r'counterrexample',r'counterrexample',True,False,'misread word','no','high','The word after provide a contains two consecutive r bodies between counte and example.',ev(hb,[1364,696,1634,744]))
add('R1-22','L32: continuation dots after descent',r'....','…',r'....',False,True,'other','no','high','Four separate full stops follow descent.',ev(hb,[463,806,559,846]))
add('R1-23','L36: X base-change product',r'X\mathbin{x}_{S}S\prime',r'X \times_S S\prime',r'X\mathbin{x}_{S}S\prime',False,True,'misread symbol or index','no','high','The product character is the typed lowercase x body, with lower S, after the capital X.',ev(hb,[1028,1007,1132,1057]),None,'Retains the source product glyph; no change to its use on the page is inferred.')
add('R1-24','L36: F base-change product',r'F\mathbin{x}_{S}S\prime',r'F \times_S S\prime',r'F\mathbin{x}_{S}S\prime',False,True,'misread symbol or index','no','high','The product character after F repeats the typed lowercase x form with lower S.',ev(hb,[1255,1007,1360,1057]))
add('R1-25','Bottom right continuation',r'.../...','',r'.../...',False,True,'omission','no','high','Three dots, a forward slash, and three dots are typed at the lower right.',ev(hb,[1519,1044,1650,1091]))
# Exact witness fragments use apostrophes rather than equivalent prime commands.
for row in changes:
 if row['id']=='R1-04':row['c']='='
 if row['id']=='R1-23':
  row.update(c=r"X\mathbin{x}_{S}S'",h=r"X \times_S S'",reading=r"X\mathbin{x}_{S}S'")
 if row['id']=='R1-24':
  row.update(c=r"F\mathbin{x}_{S}S'",h=r"F \times_S S'",reading=r"F\mathbin{x}_{S}S'")
doubts=[]
def doubt(place,c,reading,status,key,confidence):
 doubts.append(dict(place=place,c=c,reading=reading,status=status,evidence=crop_ev(key),crop=cp[key],confidence=confidence))
doubt('L1 first X prime',r'\unsure{\mathbb{X}|X}',r'\mathbb{X}','resolved','01-heavy-X','medium')
doubt('L3 first raised f',r'\unsure{f^{\bullet}|f^{\circ}}',r'f^{\bullet}','resolved','02-first-f','high')
doubt('L8 homomorphism f',r"\unsure{f'|f^{\circ}}",r"\unsure{f'|f^{\circ}}",'retained','03-homomorphism-f','medium')
doubt('L8 punctuation',r'\unsure{:|;}',r'\unsure{;|:}','revised','04-specific-punctuation','low')
doubt('L11 finite',r'\unsure{finite}',r'finite','resolved','05-finite-direct','high')
doubt('L11 damaged typed word',r'\unsure{divect|divert|direct}',r'\unsure{divect|divest|divert|direct}','revised','05-finite-direct','low')
doubt('L14 crossed are',r'\unsure{are}',r'\unsure{are}','retained','07-are-corollary-f','medium')
doubt('L20 cancelled first word',r'\unsure{of|on}',r'\unsure{for|of|on}','revised','08-cancelled-phrase','low')
doubt('L26 bacause',r'\unsure{bacause|because}',r'bacause','resolved','09-bacause','high')
remaining=[]
for place,reading,alts,conf,why,key in [
('L8 homomorphism f',r"f'",[r'f^{\circ}'],'medium','The hooked mark has no complete round outline, but an incomplete ring impression remains plausible.','03-homomorphism-f'),
('L8 punctuation',';',[':'],'low','The right paper edge clips the punctuation.','04-specific-punctuation'),
('L11 damaged typed word','divect',['divest','divert','direct'],'low','The third and especially fifth characters are thick or damaged; no recoverable correction layer can be separated with confidence.','05-finite-direct'),
('L14 crossed word','are',[],'medium','The tentative three-letter reading is partly covered by the cancellation zigzag.','07-are-corollary-f'),
('L20 cancelled first word','for',['of','on'],'low','Multiple cancellation strokes obscure much of the original word.','08-cancelled-phrase')]:
 remaining.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=why,crop=cp[key]))
inv=[]
def inventory(n,kind,position,first,hand='typewriter'):
 inv.append(dict(sheet_kind='typescript',hand=hand,element=f'074-R1-{n:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inventory(1,'text','top centre','- 2 -')
inventory(2,'text','L1–L11','Theorem (single underline); Let S be an integral noetherian scheme')
inventory(3,'insertion','L3 between double-underlined Pic names','right arrow','another unnamed hand')
inventory(4,'insertion','L5 generic-fibre map','right arrow','another unnamed hand')
inventory(5,'insertion','L6 descent sequence first relation','right arrow','another unnamed hand')
inventory(6,'insertion','L11 after representable by','finite','another unnamed hand')
inventory(7,'text','L12–L14','Corollary (single underline); Without assuming b)')
inventory(8,'deletion','L13 end of conclusions','s','another unnamed hand')
inventory(9,'deletion','L14 before holds','are (tentative)','another unnamed hand')
inventory(10,'text','L15–L17','This follows from the theorem')
inventory(11,'text','L18–L23','Corollary 2 (single underline); Assume X/S proper')
inventory(12,'deletion','L20 after allways solution','for/of/on problems A and B','another unnamed hand')
inventory(13,'text','L24–L32','N.B. (single underline); The proof does not give any evidence')
inventory(14,'drawing','left margin alongside L25–L29','bent vertical emphasis stroke','another unnamed hand')
inventory(15,'insertion','L28 around t after k','square brackets and following comma','another unnamed hand')
inventory(16,'insertion','L28 between X prime and X','right arrow','another unnamed hand')
inventory(17,'insertion','L29 after an','d','another unnamed hand')
inventory(18,'insertion','L29 map f:X prime to X','right arrow','another unnamed hand')
inventory(19,'text','L33–L36','"Problem A" is the following')
inventory(20,'text','lower right','.../...')
inventory(21,'text','lower left','archive sheet number 73','another unnamed hand')
notation=[
 dict(sign='heavy first X prime',latex=r"\mathbb{X}'",place='L1',visible_shape='Displaced overlapping X impressions, plus a raised prime.',alternatives=['X']),
 dict(sign='filled raised f mark',latex=r'f^{\bullet}',place='L3 and L14',visible_shape='Small solid raised round/compact spot.',alternatives=[]),
 dict(sign='hooked raised f mark',latex=r"\unsure{f'|f^{\circ}}",place='L8',visible_shape='Short hook, open on its upper-left side.',alternatives=[r"f'",r'f^{\circ}']),
 dict(sign='open raised f mark',latex=r'f^{\circ}',place='L9 and L10',visible_shape='Small ring with pale centre.',alternatives=[]),
 dict(sign='double-underlined Pic',latex=r'\text{\uuline{Pic}}_{X/S},\ \text{\uuline{Pic}}_{X\prime/S}',place='L3',visible_shape='Capital P and lower ic; two horizontal underline rows; source X/S and target X prime/S.',alternatives=[]),
 dict(sign='equality sign in descent expression',latex='=',place='L6',visible_shape='Two short horizontal bars, with no arrowheads.',alternatives=[]),
 dict(sign='structure sheaf terms',latex=r'\underline{O}_{X_s},\ \underline{O}_{X\prime_s},\ \underline{O}_{X\prime\prime_s}',place='L6',visible_shape='Capital singly underlined O, lower X with zero/one/two primes and nested lower s.',alternatives=[]),
 dict(sign='family index',latex=r'X_i',place='L13',visible_shape='Lower i has detached dot, upright stem and basal serif.',alternatives=[]),
 dict(sign='open subset index',latex=r'S_1',place='L19, L20 and L22',visible_shape='Lower digit 1 with upper flag and lower base, without detached dot.',alternatives=[]),
 dict(sign='singly underlined Pic',latex=r'\underline{\mathrm{Pic}}_{X/S}',place='L22',visible_shape='One continuous horizontal underline under Pic; X/S below.',alternatives=[]),
 dict(sign='polynomial ring brackets',latex=r'k\handwritten{[}t\handwritten{]}',place='L28',visible_shape='Left hand bracket has curved vertical join and short horizontal ends; right hand bracket has upright stem and leftward foot.',alternatives=[]),
 dict(sign='base-change product letter',latex=r'\mathbin{x}_S',place='L36, twice',visible_shape='Typed lowercase x with lower capital S.',alternatives=[]),
 dict(sign='typed quotation marks',latex="``...''",place='L25 and L33',visible_shape='Two upright typed marks at each end.',alternatives=[])
]
report=dict(page=page['page'],cote='57',our_scan='74',reader='R1',start_utc='2026-11-20T10:56:37Z',end_utc=datetime.now(timezone.utc).isoformat(),model='ChatGPT GPT-6 Astra Pro; /root/p57_074_r1',effort='not exposed',images_viewed=[whole,ha,hb],crops=crops,coverage=dict(all_lines_read=True,all_elements_included=True,blocks=['Typed pagination','Theorem L1–L11 with inline formulae and additions','Corollary L12–L14 and cancellations','Transition L15–L17','Corollary 2 L18–L23 and cancellation','N.B. L24–L32 with marginal stroke and handwritten completions','Problem A L33–L36','Continuation and archive number']),changes=changes,c_doubts=doubts,remaining_doubts=remaining,inventory=inv,notes=dict(summary='The page labels a theorem about a Picard-functor homomorphism, two corollaries, and a N.B. on the desired affine strengthening and counterexamples. It ends by defining the functor called Problem A. These are descriptions of the page, without a proof-verification claim.',reading_decisions=[],author_checks=['The proof does not give any evidence towards the fact that in the theorem, one could replace ``quasi-affine\'\' by ``affine\'\'.','It would be interesting to have a couterexample,say'],titles_dates_pagination=dict(headings=['Theorem','Corollary','Corollary 2','N.B.'],typed_pagination='- 2 -',archive_sheet_number='73',date=None)),notation=notation,abbreviations=[dict(abbreviation='i.e.',proposed_expansion='id est',place='L6'),dict(abbreviation='N.B.',proposed_expansion='nota bene',place='L24')],check_events=[],prior_flags=[dict(place='L3',flag='homomorphisme',finding='Terminal e confirmed.'),dict(place='L4',flag='problems A and B ... has',finding='Singular has confirmed.'),dict(place='L6',flag='descent,i.e.',finding='No space confirmed.'),dict(place='L20',flag='allways',finding='Double l confirmed.'),dict(place='L27',flag='couterexample,say',finding='Missing n and missing space confirmed.'),dict(place='L35',flag='occording',finding='Initial o confirmed.')])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (out/'observations.md').open('a') as f:
 f.write('''## Ordered coverage record

Body lines are numbered here from the first Theorem line, independently of the scan's title and footer. Every word and mathematical glyph in each line was read against the ink, including C/H agreements.

| Line | Read coverage and observations |
|---|---|
| Pagination | Centred - 2 -; no date or signature. |
| L1 | Theorem underline; Let S ... X and heavy X prime ... over S. Heavy X cropped. |
| L2 | and f: X prime, blank, X; missing arrow preserved; surjective S-morphism; split homomorphisme joined. |
| L3 | homomorphisme terminal e; first filled f dot; double Pic underlines, X/S and X prime/S; hand arrow; Assume: a) the. |
| L4 | existence problems A and B defined below for X/S has always a solution. |
| L5 | Parenthesis about projectivity; b) f_s: X prime_s hand-arrow X_s. |
| L6 | generic fiber; descent,i.e.; three singly underlined O terms; lower s throughout; primes 0/1/2; hand first arrow; typed equality before h. |
| L7 | is exact. Then, provided we replace S ... non empty open set, the. |
| L8 | homomorphism; hooked f mark retained uncertain; quasi-affine; clipped punctuation retained uncertain. |
| L9 | factorisation; open-ring f; via; functor representing suitable descent data, |
| L10 | open-ring f=vu; u affine; v monomorphism; parenthesis as you well know; v in fact. |
| L11 | representable by; finite hand addition resolved; damaged typed word retained uncertain; sums of immersions. |
| L12 | Corollary underline; Without assuming b), but instead in a) allowing X/S to be. |
| L13 | replaced ... other schemes X_i; dotted i resolved; finite over X; final s of conclusions struck. |
| L14 | crossed are retained tentative; holds, namely; f filled dot; quasi-affine morphisms. |
| L15 | This follows from the theorem, using a suitable factorisation. |
| L16 | of f. For instance, using Chow's lemma and the Main existence theorem in my. |
| L17 | first talk on Picard schemes, one gets: |
| L18 | Corollary 2 underline; Assume X/S proper satisfies the condition a') for every X prime. |
| L19 | finite over X, there exists a non empty open subset S_1 of S such that. |
| L20 | problem A for X prime, blank, S_1; allways solution; cancelled first word uncertain, problems plural clear; A and B; (this condition. |
| L21 | is satisfied if X/S is projective). Then provided we replace S by a suitable. |
| L22 | S_1 non empty and open; singly underlined Pic_X/S; exists, is separated, its connected components. |
| L23 | are of finite type over S. |
| L24 | N.B. underline; The proof does not give any evidence towards the fact that in. |
| L25 | the theorem, one could replace quoted quasi-affine by quoted affine. This is true. |
| L26 | however over a field, bacause; a quasi-affine algebraic group is affine ! First a resolved. |
| L27 | It would be interesting ... couterexample,say, over a ring of dimension. |
| L28 | 1 such as k[t]; hand square brackets and comma verified; X and X prime projective and simple over S; X prime hand-arrow X birational, |
| L29 | or alternatively; X an plus hand d; X prime projective and normal over S; f:X prime hand-arrow X finite. |
| Margin | Continuous bent hand stroke alongside L25–L29, drawn in TikZ. |
| L30 | A counterexample in the latter case would of course provide a counterrexample; the second word has rr. |
| L31 | to the effectivity problem for a finite morphism raised in my first talk. |
| L32 | on descent; four full stops. |
| L33 | Quoted Problem A; is the following: given X/S and Module F on X, to re-; word joined across line end. |
| L34 | present the functor on the category of S-preschemes taking any S prime/S into a. |
| L35 | one-element or into the empty set, occording as to whether F prime on X prime/S prime is. |
| L36 | flat with respect to S prime or not; where X prime=X x_S S prime, F prime=F x_S S prime. Typed x read in both products. |
| Footer | .../... lower right; pencil archive number 73 lower left. |

## Crops and decisions

Ten tight crops were generated and each was viewed once. Each has a JSON sidecar recording the exact original-image box, 2600-pixel output width, zero rotation, autocontrast, LANCZOS enlargement and sharpening. The source typing is horizontal, so rotation was unnecessary. No whole image or half was reopened. The bracket crop confirmed the existing bracket reading; it produced no witness-change row.

The five remaining doubtful places are the hooked raised f, clipped punctuation, damaged word after finite, crossed are, and the first word of the longer cancellation. All nine actual C uncertainty macros have a c_doubts decision. The plural problems, bacause, finite, first dot, and Corollary dot are established from their crops. The heavy X is represented with mathbb at medium confidence from its displaced doubled impressions.

## Mathematical attention

I read the indices, primes, arrows, equal sign, functor source/target and base-change products while following the page's argument. The equality sign in the sentence calling the expression exact was specifically compared with H's paired-arrow rendering. Ink determined the reading. No theorem or implication was independently proved or computationally checked; check_events is therefore empty.

End UTC: '''+report['end_utc']+'\n')
# Validate the required structure and the precise count of C's original in-text doubts.
assert C.count('\\unsure{')==5
assert len(doubts)==9
required=['page','cote','our_scan','reader','start_utc','end_utc','model','effort','images_viewed','crops','coverage','changes','c_doubts','remaining_doubts','inventory','notes','notation','abbreviations','check_events']
assert all(k in report for k in required)
assert len(crops)==10
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'observations':str(out/'observations.md'),'changes':len(changes),'c_doubts':len(doubts),'remaining_doubts':len(remaining),'crops':len(crops)},indent=2))
