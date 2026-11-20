from pathlib import Path
import json, csv

ROOT = Path('/workspace/scratch/ddf8babdc42e')
manifest = json.loads((ROOT/'out/review/scan008_crop_manifest.json').read_text())
crops = {x['name']:x for x in manifest['crops']}
C_text = (ROOT/'packets/scan008/C.tex').read_text()
H_text = (ROOT/'packets/scan008/H.tex').read_text()
P_text = (ROOT/'out/review/scan008_proposed.tex').read_text()

def spans(s, macro):
    result=[]; start=0; token='\\'+macro+'{'
    while (i:=s.find(token,start)) >= 0:
        a=j=i+len(token); depth=1
        while depth:
            if s[j]=='{': depth+=1
            elif s[j]=='}': depth-=1
            j+=1
        result.append(s[a:j-1]); start=i+1
    return result

changes=[]
def change(id, place, C, H, final, scan_shows, kind, crop, against_C=False,
           against_H=True, confidence='high', marked_in_H=False, consequential=False):
    m=crops[crop]
    changes.append(dict(id=id, place=place, C=C, H=H, final=final,
        scan_shows=scan_shows, confidence=confidence, kind=kind,
        crop=m['file'], box=m['box'], against_C=against_C, against_H=against_H,
        marked_in_H=marked_in_H, consequential=consequential))

change('008-01','Opening, after disjonction-compatibilité','(nothing)',r'\add{\uncertain{moins élégants}}','(nothing)',
 'The baseline continues with avant. The only raised words here belong to the next line and read avoir l’air de; no separate moins élégants is present.',
 'text not on the page','opening_insertion',marked_in_H=True)
change('008-02','Opening, between ne pas and les en faire',r'\inserted{avoir l\'air de}','(nothing)',r'\inserted{avoir l\'air de}',
 'Four raised words read avoir l’air de. Their horizontal attachment stroke turns down at its left end immediately before les.',
 'omission','opening_insertion',consequential=True)
change('008-03','Opening, quotation marks around facultatifs',"``facultatifs''",'« facultatifs »',"``facultatifs''",
 'Two high separate pen ticks occur on each side; neither side has angular guillemets.',
 'other','facultatifs_quotes')
change('008-04','Opening, after pas mal',r"\unsure{des'|des|d'}",r"d'",r"\unsure{des'|des|d'}",
 'A d-shaped loop is followed by an extended baseline and terminal hook, then a detached upright tick. The middle/terminal letter sequence remains compressed; C’s doubt is retained rather than silently reducing it to d’.',
 'misread word','des_ending',confidence='low')
change('008-05','Quoted definition, both quotation marks',r"``$F$ et $G$ \uline{disjoints}''",r'« $F$ et $G$ \emph{disjointes} »',r"``$F$ et $G$ \uline{disjoints}''",
 'Both the opening and closing marks are paired high ticks. The lower stroke under disjoints is an underline.',
 'other','disjoints')
change('008-06','Quoted definition, adjective','disjoints','disjointes','disjoints',
 'The terminal sequence passes from the t-shaped loop to the final s-hook without a separately written e.',
 'misread word','disjoints')
change('008-07','Raised label above the first equivalence',r'\unsure{\mathrm{defn}|\mathrm{défn}}',r'\mathrm{déf}',r'\unsure{\mathrm{dfn}|\mathrm{defn}}',
 'The complete crop shows a looped d, tall f-stroke and short terminal n-like run. A separate e cannot be securely isolated; no detached accent is visible. dfn is the provisional first candidate, defn remains possible. This is an unresolved revision, not a resolved abbreviation.',
 'misread word','definition_formula',against_C=True,confidence='low')
change('008-08','Empty-set subscript in first display',r'\unsure{\mathscr F|\mathcal F|F}',r'\mathfrak{F}',r'\unsure{\mathscr F|\mathcal F|F}',
 'The subscript has a tall stem and two cross strokes with a curved foot. The glyph is legible as F, but the mathematical alphabet cannot be fixed from this small inscription. C’s alphabet doubt is retained; Gothic is not adopted as certain.',
 'misread symbol or index','definition_formula',confidence='low',consequential=True)
change('008-09','After On a',"d'ailleurs","d'autre part","d'ailleurs",
 'There is one word after the apostrophe, with the pair of tall l-strokes and a continuous eurs ending; no second word part appears.',
 'misread word','ailleurs')
# Raw row 364 is the thin-space comma after H's forall command. Both witnesses
# already have the actual comma after G-tilde, which the crop confirms.
change('008-11','Start of interpretation sentence','donc',"d'où",'donc',
 'The word begins with a looped d and continues as one low baseline run. No apostrophe or detached accent follows d; the final c-like rise is visible.',
 'misread word','interpretation')
change('008-12','Interpretation sentence, ambient M',r'\unsure{M|\mathcal M}',r'\mathcal{M}',r'\unsure{M|\mathcal M}',
 'A curved two-shoulder M is visible. Its mathematical alphabet remains ambiguous; the first occurrence retains the explicit C doubt.',
 'misread symbol or index','interpretation',confidence='low',consequential=True)
change('008-13','Three-line definition in M, two relation subscripts and ambient M',r'M\text{ in all three positions}',r'\mathcal M\text{ in all three positions}',r'M\text{ in all three positions}',
 'The two small letters sit beneath the parallel and compatibility signs, and the third follows dans. Their small curved forms follow the same unresolved M convention marked at the preceding first occurrence.',
 'misread symbol or index','M_formula',confidence='low',consequential=True)
change('008-14','Three-line definition in M, word pas',r"n'est \uline{pas}",r"n'est pas",r"n'est \uline{pas}",
 'A short dark horizontal underline lies directly under pas and does not extend under n’est.',
 'omission','M_formula')
change('008-15','End of minoré dans M,≤ line',r'M,\leq',r'\mathcal M,\leq\text{,}',r'M,\leq',
 'There is a comma between M and ≤; no following comma is present at the right edge. The next i.e. starts on a lower baseline.',
 'text not on the page','M_formula')
change('008-16','Opening NB label',r'\uline{NB}','NB',r'\uline{NB}',
 'A short underline lies immediately below the two letters NB.',
 'omission','NB')
change('008-17','NB, overwritten verb after Il',r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}','résultera',r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}',
 'The ending contains heavy overwritten loops and cross strokes. The lower reading and surviving ending cannot both be separated letter by letter, so both C doubts and its overwritten-state encoding are retained.',
 'deletion state (struck given live or live given struck)','NB',confidence='low',consequential=True)
change('008-18','NB, subject before implique','ça',r'\ill{}','ça',
 'The small initial ç/ça-shaped inscription is present before the following verb; its loop and lower return are visible.',
 r'readable ink left as \ill{}','NB',marked_in_H=True)
change('008-19','NB, verb before que','implique',r'\uncertain{indique}','implique',
 'The word has the long joined m/p/l run before the dotted i and descending q; it does not show a simple n-d sequence. The tall loop and the following i/q are visible despite the later strike beneath.',
 'misread word','NB',confidence='medium',marked_in_H=True,consequential=True)
change('008-20','NB, cancelled explanatory phrase',r"\deleted{\unsure{i.e.} c'est un $\unsure{\exists}$}",r'\struck{i.e.\ \ill{}}',r"\deleted{\unsure{i.e.} c'est un $\unsure{\exists}$}",
 'A horizontal strike crosses the whole short line. c’est un remains readable between the initial abbreviation and a reversed-E-shaped final symbol; the initial abbreviation and final symbol remain doubtful under the strike.',
 r'readable ink left as \ill{}','NB',confidence='medium',marked_in_H=True,consequential=True)
change('008-21','NB, article between et and réciproque',r'\deleted{\unsure{la}}','la',r'\deleted{\unsure{la}}',
 'A dense local overwrite crosses the small article, independently of the long strike on the line above. Not every letter is separable, so the C doubt remains.',
 'deletion state (struck given live or live given struck)','NB',confidence='medium',consequential=True)
change('008-22','Slanted margin, adjective','spacieux','spécieux','spacieux',
 'The upright crop shows a low a-shaped body after sp, with no accent above it. The word is underlined.',
 'misread word','slanted_margin')
change('008-23','Slanted margin, after condition.','(nothing)',r'\ill{}','(nothing)',
 'The period after condition is followed directly by Contre-ex.; the intervening area contains no additional word.',
 'text not on the page','slanted_margin',marked_in_H=True)
change('008-24','Slanted margin, initial of Contre-ex.','Contre-ex.',r'\uncertain{contre-ex.}','Contre-ex.',
 'A large open capital C begins the abbreviated expression. Its hyphen and abbreviation point are present, followed by a colon.',
 'other','slanted_margin',marked_in_H=True)
change('008-25','Slanted margin, noun after les','ateliers','lieux','ateliers',
 'The next slanted line begins ateliers, with initial a/t and the tall l-stroke; the word is longer than lieux.',
 'misread word','slanted_margin')
change('008-26','Slanted margin, final adjective','simpliciaux',r'\ill{}\ \ill{}','simpliciaux',
 'The continuous last word reads simpliciaux, with the simpli part to the left of the intrusive At/DC writing and ciaux to its right, followed by three dots.',
 r'readable ink left as \ill{}','slanted_margin',confidence='medium',marked_in_H=True)
change('008-27','Slanted note position','margin immediately before At DC 1','marginal text after Cor; editorial note says en face de At DC 1','margin immediately before At DC 1',
 'The four slanted lines occupy the left side beside and above At DC 1, not the bottom of the Cor display. The first long block-cancellation stroke crosses part of the note; no separate note strike is identified.',
 'insertion or placement','slanted_margin',marked_in_H=True)
change('008-28','At DC 1 opening block, global state',r'\deleted{At DC 1 ... Supposons que ...}','live text; global cancellation mentioned only in an editorial note',r'\deleted{At DC 1 ... Supposons que ...}',
 'Three long oblique strokes traverse the At/Cor area. The heading, hypothesis sentence and its lower addition belong to this cancelled block; earlier local corrections are separately preserved.',
 'deletion state (struck given live or live given struck)','At_heading',marked_in_H=True,consequential=True)
change('008-29','At DC label underline',r'\uline{At DC} 1',r'\emph{At DC 1}',r'\uline{At DC} 1',
 'The underline ends below DC; the separate numeral 1 at its right is not underlined.',
 'other','At_heading')
change('008-30','Axiom parenthesis, adjective','spacieux','spécieux','spacieux',
 'The body after sp is a plain low a, followed by cieux; no accent is written above the a.',
 'misread word','At_heading')
change('008-31','Before the At K-definition, raised/repositioned word',r'\inserted{\unsure{soit}}','(nothing)',r'\inserted{\unsure{soit}}',
 'A small word at the left of the K line reads provisionally soit and is separately positioned below the main heading. Its short middle strokes remain uncertain; it is not omitted.',
 'omission','At_K',confidence='medium',consequential=True)
change('008-32','Immediately before K in At',r'\deleted{\unsure{et}}','(nothing)',r'\deleted{\unsure{et}}',
 'A short dark crossed/overwritten word remains immediately before K. The provisional et reading is retained with its doubt.',
 'omission','At_K',confidence='low',consequential=True)
change('008-33','At K-definition, state of K','K',r'\add{$K$}','K',
 'K is large and aligned with the equals sign and X∩Y on the main line; there is no insertion caret or raised position for K itself.',
 'insertion or placement','At_K')
change('008-34','At heading, X,Y∈M','M',r'\mathcal M','M',
 'The final glyph is the same two-shoulder M used in the preceding text. The alphabet follows the unresolved first-occurrence convention.',
 'misread symbol or index','At_heading',confidence='low',consequential=True)
change('008-35','After the At Sup formula and before Supposons',r'\deleted{\unsure{Il}}','(nothing)',r'\deleted{\unsure{Il}}',
 'After the formula’s period is a small dense overwritten upright-and-loop inscription. It is distinct from the period and from the S of Supposons; Il remains provisional.',
 'omission','At_K',confidence='low',consequential=True)
change('008-36','At, lower addition after Supposons que',r'\inserted{pour $X\',Y\'\in M$}',r'pour \add{tous} $X\',Y\'\in\mathcal M$',r'\inserted{pour $X\',Y\'\in M$}',
 'The entire phrase pour X′,Y′∈M sits on a smaller lower baseline under Supposons que. It is the addition as a whole, not a single inserted tous.',
 'insertion or placement','At_supposons',consequential=True)
change('008-37','Between pour and X′ in lower addition','(nothing)',r'\add{tous}','(nothing)',
 'After the end of pour the next written object is X′; no word tous occurs in the gap.',
 'text not on the page','At_supposons',consequential=True)
change('008-38','Lower addition, ambient M','M',r'\mathcal M','M',
 'The large curved M after ∈ follows the same unresolved alphabet convention as the first prose occurrence.',
 'misread symbol or index','At_supposons',confidence='low',consequential=True)
change('008-39','At displayed implication, global state',r'\deleted{X\'\ll X,\ldots\Longrightarrow X\'\parallel Y\'.}','live display',r'\deleted{X\'\ll X,\ldots\Longrightarrow X\'\parallel Y\'.}',
 'The three long cancellation strokes cross the displayed row. The final apparent diagonal through the parallel sign belongs to the long cancellation stroke, not a different relation.',
 'deletion state (struck given live or live given struck)','At_display',marked_in_H=True,consequential=True)
change('008-40','At display, cancelled sign before X′',r'\deleted{\unsure{\forall}}','omitted from body; editorial note mentions a crossed sign',r'\deleted{\unsure{\forall}}',
 'A densely crossed quantifier-like form stands before X′. Its upright and crossing strokes support ∀ as a candidate, but not every stroke is recoverable; C’s doubt remains.',
 'omission','At_display',confidence='low',marked_in_H=True,consequential=True)
change('008-41','At conclusion, global state',r'\deleted{Alors [NB ...] X\ldots Y.}','live text',r'\deleted{Alors [NB ...] X\ldots Y.}',
 'The conclusion lies within the same obliquely cancelled At/Cor block, and two of the long strokes cross its text region.',
 'deletion state (struck given live or live given struck)','At_conclusion',marked_in_H=True,consequential=True)
change('008-42','Bracketed NB in At conclusion','et alors seulement',r'il \ill{} dans tous les cas','et alors seulement',
 'The crop shows et, then the looped a/l and rounded o/r/s of alors, followed by seulement with its tall l and low ending. The alleged dans tous les cas sequence is absent.',
 'misread word','At_conclusion',marked_in_H=True,consequential=True)
change('008-43','At conclusion, cf Cor placement',r'\inserted{cf Cor}','inline cf. Cor; editorial note says written underneath',r'\inserted{cf Cor}',
 'cf Cor is on a lower baseline beneath the middle of the bracketed phrase and belongs to that bracketed note.',
 'insertion or placement','At_conclusion',marked_in_H=True)
change('008-44','At conclusion, punctuation after cf','cf Cor','cf. Cor','cf Cor',
 'The c/f strokes lead into the space before Cor without a separate period.',
 'abbreviation expanded or spelling modernised','At_conclusion')
change('008-45','Cor heading and K-definition, global state',r'\deleted{Cor Soient ... K=...}','live text',r'\deleted{Cor Soient ... K=...}',
 'Two long oblique cancellation strokes run through the Cor heading/formula region as part of the common cancelled lower block.',
 'deletion state (struck given live or live given struck)','Cor_formula',marked_in_H=True,consequential=True)
change('008-46','Cor heading, ambient F',r'\mathscr F',r'\mathfrak F',r'\mathscr F',
 'The letter following ∈ has a tall looped upper stem and long cross stroke, unlike the ordinary F immediately before G. Script F remains the first candidate under the alphabet doubt already marked in the first display.',
 'misread symbol or index','Cor_formula',confidence='medium',consequential=True)
change('008-47','Cor Sup index, overwritten first operand',r'\deleted{\unsure{\widetilde X|X}}\unsure{\widetilde F|F}',r'\widetilde F',r'\deleted{\unsure{\widetilde X|X}}\unsure{\widetilde F|F}',
 'Extra crossing strokes remain underneath the final F-shaped form. The prior X and its possible tilde are not fully separable; the final F’s top overlaps the Sup descender, leaving its tilde doubtful too.',
 'deletion state (struck given live or live given struck)','Cor_formula',confidence='low',consequential=True)
change('008-48','Cor Sup index, overwritten second operand',r'\deleted{\unsure{\widetilde Y|Y}}\widetilde G',r'\widetilde G',r'\deleted{\unsure{\widetilde Y|Y}}\widetilde G',
 'The final looped G and its wave are accompanied by older crossing/descending strokes. The former Y/tilde remains uncertain, so its C doubt is preserved.',
 'deletion state (struck given live or live given struck)','Cor_formula',confidence='low',consequential=True)
change('008-49','Cor Alors/quantifier row, global state',r'\deleted{Alors F...G ... \forall X,...\in M}','live text',r'\deleted{Alors F...G ... \forall X,...\in M}',
 'The row belongs to the obliquely cancelled Cor block; the descending central cancellation stroke passes through the quantifier/X area.',
 'deletion state (struck given live or live given struck)','Cor_final',marked_in_H=True,consequential=True)
change('008-50','Circled three-letter inscription','ses','(ssi)','ses',
 'There is a looped middle e between two s-shaped strokes; the final stroke has no separate i-dot. Literal ses is retained without expanding its apparent function.',
 'misread word','Cor_final',marked_in_H=True,consequential=True)
change('008-51','Outline around ses','closed ellipse in TikZ','parentheses in text; editorial note says circled','open ellipse with a small upper-right gap in TikZ',
 'The curved enclosure runs below and around the letters and is open between the upper and upper-right stroke ends. It is not a pair of parentheses and is not completely closed.',
 'drawing or diagram','Cor_final',against_C=True,confidence='medium',marked_in_H=True)
change('008-52','Cor quantifier row, overwritten letter after X,',r'\deleted{\unsure{\varphi|y}}\unsure{Y|y}','Y',r'\deleted{\unsure{\varphi|y}}\unsure{Y|y}',
 'The compact letter has multiple overlaid loops and a heavy descending stem. Both the old φ/y and the surviving Y/y remain uncertain; there is ink to preserve before the surviving reading.',
 'deletion state (struck given live or live given struck)','Cor_final',confidence='low',consequential=True)
change('008-53','Cor quantifier row, ambient M','M',r'\mathcal M','M',
 'The final two-shoulder M follows the same unresolved alphabet convention. It is not a separate new symbol.',
 'misread symbol or index','Cor_final',confidence='low',consequential=True)
change('008-54','After M at the end of Cor quantifier row','(no comma)',',','(no comma)',
 'The line ends after M. No dark curved comma is present in the following blank space.',
 'text not on the page','Cor_final')
change('008-55','Final Cor implication, global state',r'\deleted{X\ll F,\ldots\Longrightarrow X\parallel Y}','live display',r'\deleted{X\ll F,\ldots\Longrightarrow X\parallel Y}',
 'This is the final continuation row of the same cancelled Cor statement. No fresh live-text boundary is marked between it and the cancelled preceding row.',
 'deletion state (struck given live or live given struck)','Cor_final',marked_in_H=True,consequential=True)
change('008-56','End of final Cor display','(no period)','.','(no period)',
 'After the final Y the paper is blank; the dark terminal period visible in the earlier At display has no counterpart here.',
 'text not on the page','Cor_final')

# Every C doubt is retained or explicitly revised as unresolved.  No cancelled
# doubtful word is promoted to certainty merely because its context is familiar.
doubts=[]
def doubt(n, place, reading, alternatives, confidence, reason, crop, status='retained'):
    m=crops[crop]
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,
        confidence=confidence,reason=reason,C_marker_number=n,status=status,
        crop=m['file'],box=m['box']))
doubt(1,'pas mal ... implications',"des'",['des',"d'"],'low','The extended baseline and terminal hook do not securely separate de/des; a detached tick is visible. No grammatical correction is made.','des_ending')
doubt(2,'First equivalence label','dfn',['defn'],'low','The d and f strokes and terminal short run are visible, but an e cannot be isolated. There is no detached accent. Revision remains unresolved.','definition_formula','revised, unresolved')
doubt(3,'Empty-set subscript',r'\mathscr F',[r'\mathcal F','F'],'low','Tall stem, two bars and curved foot identify F but do not uniquely determine an alphabet.','definition_formula')
doubt(4,'en termes/terme','termes',['terme'],'medium','The low final run is not cleanly segmented into an independently identifiable final s.','interpretation')
doubt(5,'First ambient M','M',[r'\mathcal M'],'low','Two curved shoulders are legible, but this hand does not provide a secure plain/calligraphic alphabet boundary here. Applies to the subsequent Ms on this page.','interpretation')
doubt(6,'NB overwritten underlying verb','résultera',[],'low','The ending is heavily overwritten; every underlying letter cannot be seen.','NB')
doubt(7,'NB surviving verb','résulte',['résultera'],'low','The final overwritten loops favor a short ending but do not securely separate it from the underlying longer form.','NB')
doubt(8,'NB struck abbreviation','i.e.',[],'medium','Letters and stops are crossed by a dark horizontal strike; retain the C doubt.','NB')
doubt(9,'NB struck final mathematical symbol',r'\exists',[],'low','The reversed-E-like outline survives only partly under the cancellation stroke.','NB')
doubt(10,'NB struck article','la',[],'low','The looped initial and dense ending are overinked; every letter is not plain.','NB')
doubt(11,'NB d’axiome(s)',"d'axiome",["d'axiomes"],'low','The word reaches the sheet edge, and the terminal run does not securely identify or exclude s.','NB')
doubt(12,'At heading Soient','Soient',[],'medium','The ending is overinked and the global cancellation crosses the word region; not every letter is plain enough to resolve a C doubt in cancelled text.','At_heading')
doubt(13,'At lower-left insertion','soit',[],'medium','The short middle letters remain compressed in the small addition.','At_K')
doubt(14,'At local deletion before K','et',[],'low','The short word is largely reduced to a thick horizontal/crossed shape.','At_K')
doubt(15,'At local deletion before Supposons','Il',[],'low','The two-letter-like upright/loop cluster is densely overinked.','At_K')
doubt(16,'At display deleted initial quantifier',r'\forall',[],'low','Several heavy strokes obscure the original sign; ∀ is a candidate, not a resolved sign.','At_display')
doubt(17,'Cor first prior Sup operand',r'\widetilde X',['X'],'low','The prior crossing strokes are mixed with the final F and the descending Sup; a prior tilde cannot be separated.','Cor_formula')
doubt(18,'Cor surviving first Sup operand',r'\widetilde F',['F'],'low','The final F is recognizable, but a separate tilde competes with the nearby Sup descender/overwriting.','Cor_formula')
doubt(19,'Cor second prior Sup operand',r'\widetilde Y',['Y'],'low','Old strokes remain inside the final G and its wave; whether the prior Y carried a tilde is not plain.','Cor_formula')
doubt(20,'Cor prior letter after ∀X,',r'\varphi',['y'],'low','The lower loop and upper crossings are overlaid, leaving the prior glyph ambiguous.','Cor_final')
doubt(21,'Cor surviving letter after ∀X,','Y',['y'],'low','The surviving letter is compressed and overlaid; its case is not independently secure.','Cor_final')
doubts.append(dict(place='Slanted margin, cancellation scope',reading='margin kept live as in C',alternatives=['part of the common lower-block cancellation'],confidence='medium',reason='One long diagonal crosses part of the slanted note on its way through At/Cor; no independent strike identifies the margin note alone. Root should adjudicate the scope.',crop=crops['slanted_margin']['file'],box=crops['slanted_margin']['box']))

inventory=[
 dict(element='Author page number 7',kind='text',position='top, x≈650 y≈75',first_words_or_objects='7'),
 dict(element='Opening paragraph',kind='text',position='upper text block, y≈150–650',first_words_or_objects='Je voudrais maintenant faire passer les axiomes'),
 dict(element='Opening raised addition',kind='insertion',position='above line 3, after ne pas',first_words_or_objects="avoir l’air de"),
 dict(element='Quoted definition introduction',kind='text',position='y≈700–810',first_words_or_objects='Une notion essentielle ici est celle de'),
 dict(element='Definition of disjoint F,G',kind='display',position='y≈790–895',first_words_or_objects=r'F\parallel G; labelled double equivalence; compatibility; F∩G=empty set'),
 dict(element='Dependence sentence',kind='text',position='y≈945–980',first_words_or_objects='notion qui ne dépend que de ≤. On a d’ailleurs'),
 dict(element='Quantified equivalence',kind='display',position='y≈1010–1075',first_words_or_objects=r'F\parallel G\Longleftrightarrow\forall X∈F-tilde,Y∈G-tilde, X\parallel Y'),
 dict(element='Interpretation sentence',kind='text',position='y≈1110–1220',first_words_or_objects='donc interprétation en termes de'),
 dict(element='Three-line definition in M',kind='display',position='y≈1230–1390',first_words_or_objects='X parallel-under-M Y; compatibility-under-M; no common minorant'),
 dict(element='Parenthetical NB',kind='text',position='right of sheet, y≈1400–1620',first_words_or_objects='(NB Il ... des axiomes ...'),
 dict(element='NB verb overwrite',kind='deletion',position='after Il, y≈1435',first_words_or_objects='résultera / résulte'),
 dict(element='Raised NB adjective',kind='insertion',position='above axiomes / que, y≈1390',first_words_or_objects='précédents'),
 dict(element='NB cancelled explanation',kind='deletion',position='y≈1515–1545',first_words_or_objects='i.e. c’est un [symbol]'),
 dict(element='NB cancelled article',kind='deletion',position='after et, y≈1550',first_words_or_objects='la'),
 dict(element='Four-line diagonal note',kind='margin note',position='left margin, y≈1480–1960, slope upwards to right',first_words_or_objects='Un atelier sera dit spacieux'),
 dict(element='At DC 1 heading and hypothesis sentence',kind='deletion',position='y≈1640–1830, part of three-stroke cancellation',first_words_or_objects='At DC 1 (Axiome des ateliers spacieux) Soient X,Y∈M'),
 dict(element='At local lower-left addition',kind='insertion',position='left of K definition, y≈1775',first_words_or_objects='soit'),
 dict(element='At local discarded connective',kind='deletion',position='immediately before K, y≈1750',first_words_or_objects='et'),
 dict(element='At discarded start before Supposons',kind='deletion',position='x≈1030 y≈1750',first_words_or_objects='Il'),
 dict(element='At hypothesis addition',kind='insertion',position='under Supposons que, y≈1790',first_words_or_objects='pour X′,Y′∈M'),
 dict(element='At displayed implication',kind='display',position='y≈1850–1920, globally cancelled',first_words_or_objects='[deleted quantifier] X′≪X, X′∥K, Y′≪Y, Y′∥K ⇒ X′∥Y′.'),
 dict(element='At locally cancelled quantifier',kind='deletion',position='before first X′ in display',first_words_or_objects='∀, uncertain'),
 dict(element='At conclusion',kind='deletion',position='y≈1950–2020',first_words_or_objects='Alors [NB et alors seulement ...] X compatibility Y.'),
 dict(element='At bracket reference addition',kind='insertion',position='below the bracketed phrase, y≈2020',first_words_or_objects='cf Cor'),
 dict(element='Cor heading and Sup formula',kind='deletion',position='y≈2070–2160',first_words_or_objects='Cor Soient F,G∈script F, K=F∩G=Sup Z.'),
 dict(element='Cor prior first index operand',kind='deletion',position='first operand after Z∈ in Sup limit',first_words_or_objects='old X, possibly with tilde; overwritten by F, possibly with tilde'),
 dict(element='Cor prior second index operand',kind='deletion',position='second operand of Sup-limit intersection',first_words_or_objects='old Y, possibly with tilde; overwritten by G-tilde'),
 dict(element='Cor two-row assertion',kind='display',position='y≈2165–2300, globally cancelled',first_words_or_objects='Alors F compatibility G, circled ses, ∀X,...∈M; final implication'),
 dict(element='Open oval around ses',kind='drawing',position='middle of Cor first assertion row',first_words_or_objects='ses inside an oval with upper-right gap'),
 dict(element='Cor quantifier overwritten letter',kind='deletion',position='after ∀X, in first assertion row',first_words_or_objects='prior φ/y; surviving Y/y'),
]

notation=[
 dict(form=r'\parallel',reading='disjointness relation as written',place='five displays and inline occurrences',observation='Two upright strokes; the small M under the third display’s first relation is an underset, not a neighboring variable.'),
 dict(form='interlaced opposing chevrons',reading='handwritten compatibility sign, reproduced directly in TikZ',place='first and third displays, At conclusion, Cor first row',observation='Upper and lower crossings enclose a small central diamond. The same basic shape recurs; H’s between command is treated as an alternate rendering of this sign, not an extra source word.'),
 dict(form=r'\varnothing',reading='empty-set-like glyph',place='first display, F∩G=',observation='Open/rounded loop crossed by a long rising diagonal. The proposal retains the visible diagonal empty-set form; no semantic replacement by a different symbol is made.'),
 dict(form=r'\unsure{\mathscr F|\mathcal F|F}',reading='ambient F alphabet unresolved',place='empty-set subscript; repeated in Cor membership',observation='The Cor occurrence is more looped than the ordinary F beside it. First candidate remains script F, but the small first occurrence does not settle the alphabet.'),
 dict(form=r'\unsure{M|\mathcal M}',reading='ambient M alphabet unresolved',place='first prose occurrence and all later M occurrences',observation='Two rounded shoulders occur at full size and beneath relation signs. The alphabet doubt is marked once, at first occurrence.'),
 dict(form=r'\widetilde F,\widetilde G,\widetilde X,\widetilde Y',reading='wavy marks over the named letters',place='quantified display and two Sup limits',observation='Waves in the quantified display and At limit are clear; the first Cor-limit wave is entangled with the Sup descender and is retained as a doubt.'),
 dict(form=r'\ll',reading='double less-than / refinement sign as drawn',place='NB and cancelled At/Cor formulas',observation='Each sign has two distinct left-pointing chevrons. No conversion to ≤ was made.'),
 dict(form='ses inside an open oval',reading='literal ses',place='Cor first assertion row',observation='Middle letter is looped e; no final i-dot. Its apparent logical purpose is not expanded into ssi.'),
 dict(form='cf Cor',reading='abbreviated reference without period',place='below At bracketed NB',observation='No separate dot after cf; Cor is capitalized.'),
 dict(form='At DC 1',reading='axiom label with numeral 1',place='cancelled lower heading',observation='Underline under At DC only; numeral 1 separate. The only other source numeral is page 7.'),
]

hand_log=[
 dict(habit='High paired ticks for double quotation marks',place='facultatifs and F et G disjoints',observation='Both pairs consist of high pen ticks, consistently unlike guillemets. H changes their form.'),
 dict(habit='Very compressed low lowercase runs between tall letters',place='d’ailleurs, termes, des’, implique',observation='The tall l strokes settle d’ailleurs; the compressed ending of termes and the short des’ inscription remain ambiguous. No page-wide rule is inferred for an s that cannot be separated.'),
 dict(habit='G can be drawn with a very short lower return',place='all F/G formulas on this page',observation='Some Gs are nearly open C outlines with a downturned terminal, while the compatibility display and Cor membership show a clearer inward return. Each was visually checked; no uniform replacement by C was made.'),
 dict(habit='Curved M resembles a small μ-like two-shoulder mark when reduced',place='M in prose, relation undersets, At/Cor membership',observation='All occurrences retain M as the letter; plain/calligraphic style is unresolved rather than silently imposed.'),
 dict(habit='Local overinking remains inside a later large cancellation',place='NB verb; At et/Il/quantifier; Cor operands and Y/y',observation='The local correction strokes are denser and shorter than the three thin long diagonal strokes. Both layers are recorded.'),
 dict(habit='Underlining is narrower than the enclosing phrase',place='pas; At DC; Axiome des ateliers spacieux; Cor',observation='The actual stroke ends were checked. At’s separate numeral 1 is outside its underline.'),
 dict(habit='Interlaced-chevron compatibility sign',place='four formula groups',observation='The repeated upper/lower crossings and central diamond distinguish this sign from a single X or simple pair of parallel strokes.'),
 dict(habit='Final s and looped e in short words',place='circled ses and disjoints',observation='The middle loop of ses is visible; disjoints has no extra e before final s. These two places were read independently, without expanding ses to an expected abbreviation.'),
]

notes=[
 dict(id='008-N1',claim='All 21 C doubt marks have an explicit disposition; 20 retained and 1 revised but still unresolved.',source='C.tex doubt extraction and the named crops',reasoning_if_any='No C doubt in cancelled text was promoted to certainty. The changed definition-label candidate remains marked.'),
 dict(id='008-N2',claim='No mathematical proof check was performed.',source='first-reader workflow',reasoning_if_any='The checks were visual readings, source-state audits, collation coverage and file/schema validation. Formulas were not repaired from mathematical expectations.'),
 dict(id='008-N3',claim='The exact deletion scope of the slanted note is an open issue for root.',source='whole image and slanted_margin crop',reasoning_if_any='The first long block strike passes through part of the note but also continues through the lower block. C and H keep the note live; the proposal retains that state with this explicit qualification.'),
 dict(id='008-N4',claim='H’s three editorial notes are not manuscript text.',source='H.tex note wrappers; source image',reasoning_if_any='Their observations about global strikes, the omitted local sign, the lower cf Cor and the circle were checked against ink and encoded as source state where appropriate, not copied as prose.'),
 dict(id='008-N5',claim='The literal circled ses is preserved.',source='Cor_final crop',reasoning_if_any='A looped e is visible. The logical role is not used to substitute ssi.'),
 dict(id='008-N6',claim='Only page 7 and axiom numeral 1 are handwritten numbers on this sheet.',source='whole image and both half readings',reasoning_if_any='Both have neutral second-reading boxes. TeX coordinate numbers and scan metadata are not source numerals.'),
 dict(id='008-N7',claim='Three crop windows were extended before their pending decisions because upper strokes touched the original edge.',source='crop manifest and reproducible script',reasoning_if_any='The definition label, M-formula upper brace and raised précédents now have complete final windows; no new named crop was introduced.'),
 dict(id='008-N8',claim='The first-reader proposed TeX is complete but provisional.',source='scan008_proposed.tex',reasoning_if_any='Root independently adjudicates contested readings and cancellation scope. No finalized page or global log was written.'),
]

audit=[]
C_deletions=spans(C_text,'deleted'); C_insertions=spans(C_text,'inserted')
del_info=[
 ('NB overwritten verb','Keep overwritten-state wrapper and both reading doubts.','NB','Dense correction lies at the word ending; neither underlying nor surviving complete ending is wholly separable.'),
 ('NB cancelled explanatory line','Keep full local deletion.','NB','Horizontal stroke crosses i.e., c’est un and the final symbol; doubts stay under the strike.'),
 ('NB cancelled article','Keep local deletion.','NB','The small article after et is thickly overinked independently of the line above.'),
 ('At opening through lower hypothesis addition','Keep outer deletion; retain all nested earlier states.','At_heading','Three long diagonal strokes cancel the lower At/Cor block. Heading and sentence are inside it.'),
 ('At word before K','Keep nested local deletion and doubt.','At_K','Short overwritten connective remains immediately to the left of K.'),
 ('At word before Supposons','Keep nested local deletion and doubt.','At_K','Small dense upright/loop cluster remains after the formula period.'),
 ('At displayed implication','Keep outer deletion.','At_display','The row is crossed by the common long cancellation strokes.'),
 ('At displayed initial quantifier','Keep nested deletion and doubt.','At_display','The local dense strike differs from the thin long oblique cancellation.'),
 ('At Alors conclusion','Keep outer deletion, including bracket note and its lower addition.','At_conclusion','The conclusion is within the continuous cancelled lower block.'),
 ('Cor heading and Sup formula','Keep outer deletion and inner corrections.','Cor_formula','The heading and formula are within the lower diagonal cancellation.'),
 ('Cor first prior limit operand','Keep nested deleted X/tilde-X alternatives.','Cor_formula','Old crossing strokes remain beneath the F-shaped final operand; tilde not isolable.'),
 ('Cor second prior limit operand','Keep nested deleted Y/tilde-Y alternatives.','Cor_formula','Prior crossing/descending strokes remain within the final G region.'),
 ('Cor first assertion row','Keep outer deletion and its local overwrite.','Cor_final','The central long strike traverses the quantifier region; the row belongs to cancelled Cor.'),
 ('Cor prior overwritten letter after X,','Keep nested deletion and both old/new doubts.','Cor_final','Dense overlapping loops and stem prevent full recovery.'),
 ('Cor final implication row','Keep outer deletion as continuation of cancelled Cor.','Cor_final','No new live-text boundary or separate reopening is marked.'),
]
for n,(span,info) in enumerate(zip(C_deletions,del_info),1):
    place,decision,crop,ev=info; m=crops[crop]
    audit.append(dict(C_span=r'\deleted{'+span+'}',decision=decision,place=place,
        evidence=dict(crop=m['file'],box=m['box'],observation=ev),macro='deleted',C_occurrence=n))
ins_info=[
 ('Opening avoir l’air de','Keep insertion between ne pas and les.','opening_insertion','Raised phrase and bent attachment stroke terminate before les.'),
 ('NB précédents','Keep insertion after axiomes.','NB','Raised word and lower curved attachment lead to the space before que.'),
 ('At soit','Keep small lower-left insertion before the K clause, still doubtful and globally cancelled.','At_K','Small separate word sits left/below the main line; the former connective is locally cancelled.'),
 ('At pour X′,Y′∈M','Keep the whole phrase as an insertion, within global deletion.','At_supposons','It occupies the smaller lower baseline under Supposons que; no tous is present.'),
 ('At cf Cor','Keep lower insertion inside the bracketed note, within global deletion.','At_conclusion','It is centered below the bracketed phrase rather than on its main baseline.'),
]
for n,(span,info) in enumerate(zip(C_insertions,ins_info),1):
    place,decision,crop,ev=info; m=crops[crop]
    audit.append(dict(C_span=r'\inserted{'+span+'}',decision=decision,place=place,
        evidence=dict(crop=m['file'],box=m['box'],observation=ev),macro='inserted',C_occurrence=n))

# Each raw collation row is accounted for.  Math spacing commas and the H
# editorial notes are distinguished from punctuation and manuscript state.
row_map={
353:('metadata only: scan marker versus witness page marker',[]),
354:('substantive: H phrase absent from ink',['008-01']),
355:('substantive: real raised insertion omitted by H',['008-02']),
356:('substantive punctuation: source paired quote ticks',['008-03']),
357:('unresolved word difference; C doubt retained',['008-04']),
358:('substantive punctuation: opening double-quote ticks',['008-05']),
359:('substantive word ending and closing quote ticks',['008-05','008-06']),
360:('substantive unresolved abbreviation reading',['008-07']),
361:('mixed: relation-rendering syntax; complete formula and alphabet checked',['008-07','008-08']),
362:('unresolved mathematical alphabet, not mere macro syntax',['008-08']),
363:('substantive different word',['008-09']),
364:('macro-only thin-space comma after H forall; both witnesses already have the actual comma after G-tilde',[]),
365:('substantive different word',['008-11']),
366:('certainty/alternative only; termes|terme retained in doubts',[]),
367:('unresolved ambient alphabet',['008-12']),
368:('display layout/macro syntax only; source three-line arrangement retained',[]),
369:('mixed: relation-rendering syntax, M alphabet and omitted underline',['008-13','008-14']),
370:('substantive punctuation: H comma absent',['008-15']),
371:('macro-only math spacing comma in H nexists thin space',[]),
372:('aligned environment syntax only',[]),
373:('substantive overwritten state and unresolved surviving reading',['008-17']),
374:('substantive omitted/read-wrong words',['008-18','008-19']),
375:('macro-only math spacing comma in H nexists thin space',[]),
376:('substantive readable cancelled words omitted behind H illegibility',['008-20']),
377:('certainty/alternative only; d’axiome|d’axiomes retained in doubts',[]),
378:('same three-dot ellipsis, different TeX encoding',[]),
379:('H margin moved in text order; lexical and placement differences separately recorded',['008-22','008-23','008-24','008-25','008-26','008-27']),
380:('substantive different adjective',['008-30']),
381:('substantive omitted insertion and deleted connective',['008-31','008-32']),
382:('Sup and limit macro order only; whole formula checked',[]),
383:('Sup placement and thin-space comma macro only',[]),
384:('substantive omitted cancelled start',['008-35']),
385:('substantive phantom tous and insertion-scope difference',['008-36','008-37','008-38']),
386:('substantive different bracketed wording',['008-42']),
387:('substantive abbreviation punctuation',['008-44']),
388:('mixed: relation-rendering syntax and H editorial prose; source deletion/placement retained',['008-41','008-43']),
389:('H editorial note, not source prose; its reported features checked',['008-40','008-43']),
390:('Sup/limit order macro syntax; global state checked separately',['008-45']),
391:('substantive prior operand omitted; final operand doubt retained',['008-47']),
392:('substantive prior operand omitted',['008-48']),
393:('Sup order and thin-space comma macro only',[]),
394:('aligned syntax only; cancelled source state checked',['008-49']),
395:('substantive circled word and source enclosure',['008-50','008-51']),
396:('TikZ sizing parameters only',[]),
397:('mixed: TikZ syntax, overwritten letter and M alphabet',['008-49','008-50','008-51','008-52','008-53']),
398:('substantive H terminal comma absent',['008-54']),
399:('mixed aligned syntax and H terminal period absent',['008-56']),
400:('H editorial notes excluded; margin wording and global cancellations verified',['008-22','008-23','008-24','008-25','008-26','008-27','008-28','008-39','008-41','008-45','008-49','008-55']),
}
difference_review=[dict(source_row=n,classification=v[0],change_ids=v[1]) for n,v in sorted(row_map.items())]

P_deletions=spans(P_text,'deleted'); P_insertions=spans(P_text,'inserted')
P_displays=[]
pos=0
while (i:=P_text.find('\\[',pos))>=0:
    j=P_text.index('\\]',i)+2
    P_displays.append(P_text[i:j]); pos=j
margin=spans(P_text,'margin')[0]
NB=P_text[P_text.index('(\\uline{NB}'):P_text.index('% slanted')].strip()
definition_intro=P_text[P_text.index('Une notion essentielle'):P_text.index('\\[')].strip()
second_boxes=[]
def sb(n,kind,box,reading,coverage):
    x0,y0,x1,y1=box
    second_boxes.append(dict(box=f'scan008_b{n:02}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading,coverage=coverage))
sb(1,'number',(620,35,700,115),r'\mspage{7}','handwritten page number')
sb(2,'insertion',(1040,190,1640,350),r"\inserted{avoir l'air de}",'all words of opening addition; H false alternative; attachment')
sb(3,'punctuation',(1090,330,1530,438),r"``facultatifs''",'both real quotation marks')
sb(4,'word',(1400,425,1555,495),r"\unsure{des'|des|d'}",'C doubt and C/H differing word')
sb(5,'word',(255,745,790,825),r"``$F$ et $G$ \uline{disjoints}''",'different adjective, quote ticks and underline')
sb(6,'formula',(510,770,1450,905),P_displays[0],'whole formula with unresolved label and subscript alphabet; low-confidence departure from C')
sb(7,'word',(1430,900,1650,990),"d'ailleurs",'C/H different word')
sb(8,'formula',(515,985,1440,1085),P_displays[1],'whole formula; visible source comma agrees with both witnesses')
sb(9,'word',(255,1085,1610,1170),r'donc interprétation en \unsure{termes|terme} de $X\parallel Y$ dans $\unsure{M|\mathcal M}$,','donc difference and two C doubts')
sb(10,'formula',(535,1200,1660,1407),P_displays[2],'whole three-line formula, alphabets, relation undersets and source punctuation')
sb(11,'text',(860,1365,1670,1630),NB,'complete NB and all its source-state layers')
sb(12,'deletion',(1020,1395,1210,1470),r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}','overwritten verb, both C doubts')
sb(13,'insertion',(1400,1365,1620,1450),r'\inserted{précédents}','raised word and attachment')
sb(14,'deletion',(895,1490,1275,1560),r"\deleted{\unsure{i.e.} c'est un $\unsure{\exists}$}",'every word/symbol of the local cancellation')
sb(15,'deletion',(965,1530,1045,1590),r'\deleted{\unsure{la}}','local article deletion')
sb(16,'word',(1490,1490,1670,1590),r"\unsure{d'axiome|d'axiomes}",'C uncertain ending at sheet edge')
sb(17,'margin note',(20,1460,630,1980),r'\margin{'+margin+'}','all four slanted lines and cancellation-scope issue')
sb(18,'number',(230,1630,445,1750),r'\deleted{\uline{At DC} 1}','axiom numeral 1, label underline and global deletion')
sb(19,'word',(460,1620,1585,1742),r'\deleted{(\uline{Axiome des ateliers spacieux}) \unsure{Soient} $X,Y\in M$,}','spacieux difference, Soient doubt, alphabet')
sb(20,'deletion',(230,1625,1585,1845),r'\deleted{'+P_deletions[3]+'}','complete first globally cancelled block, including nested corrections')
sb(21,'insertion',(280,1735,390,1820),r'\deleted{\inserted{\unsure{soit}}}','lower-left doubtful insertion inside cancellation')
sb(22,'deletion',(400,1715,480,1795),r'\deleted{\deleted{\unsure{et}}}','earlier local connective deletion')
sb(23,'formula',(470,1705,1005,1840),r'\deleted{$K=X\cap Y=\underset{Z\in\widetilde X\cap\widetilde Y}{\mathrm{Sup}}\,Z$.}','complete K formula and limit')
sb(24,'deletion',(1008,1705,1065,1790),r'\deleted{\deleted{\unsure{Il}}}','earlier local start before Supposons')
sb(25,'insertion',(1190,1740,1560,1840),r'\deleted{\inserted{pour $X\',Y\'\in M$}}','complete lower insertion; absent tous; both primes and alphabet')
sb(26,'formula',(285,1815,1540,1945),P_displays[3],'whole formula containing doubtful cancelled quantifier')
sb(27,'deletion',(285,1840,355,1940),r'\deleted{\deleted{\unsure{\forall}}}','local quantifier deletion inside global deletion')
sb(28,'deletion',(300,1925,1390,2045),r'\deleted{'+P_deletions[8]+'}','complete At conclusion and bracketed phrase')
sb(29,'insertion',(730,1980,910,2060),r'\deleted{\inserted{cf Cor}}','complete lower reference addition and absence of point')
sb(30,'word',(605,1935,1110,2015),r'\deleted{et alors seulement\ldots}','all actual differing words in bracket')
sb(31,'formula',(470,2025,1555,2175),r'\deleted{'+P_deletions[9]+'}','complete Cor introduction/formula with all doubtful prior/current operands')
sb(32,'deletion',(1340,2095,1405,2170),r'\deleted{\deleted{\unsure{\widetilde X|X}}\unsure{\widetilde F|F}}','prior first operand and surviving doubtful wave')
sb(33,'deletion',(1400,2095,1465,2170),r'\deleted{\deleted{\unsure{\widetilde Y|Y}}\widetilde G}','prior second operand and surviving G-tilde')
sb(34,'formula',(565,2150,1305,2245),r'\[\deleted{'+P_deletions[12]+r'}\]','whole Cor first assertion row with uncertain overwritten letter')
sb(35,'drawing',(945,2145,1070,2245),r'\deleted{\tikz[baseline=(s.base)]{\node[inner sep=1pt] (s) {ses};\draw (s.center) ++(30:1.05em and .72em) arc[start angle=30,end angle=-295,x radius=1.05em,y radius=.72em];}}','literal word and full enclosure; lower-confidence graphic departure from C')
sb(36,'deletion',(1150,2150,1215,2240),r'\deleted{\deleted{\unsure{\varphi|y}}\unsure{Y|y}}','prior and surviving overwritten letter')
sb(37,'punctuation',(1200,2155,1300,2240),r'\deleted{\in M}','ambient alphabet and no following comma')
sb(38,'formula',(660,2220,1515,2310),r'\[\deleted{'+P_deletions[14]+r'}\]','complete final implication, global state and no terminal period')
sb(39,'word',(895,1445,1170,1520),'ça implique','both NB words that differ from H')
sb(40,'deletion',(225,1550,1600,2315),r'\deleted{'+P_deletions[3]+'}\n'+P_displays[3]+'\n'+r'\deleted{'+P_deletions[8]+'}\n'+r'\deleted{'+P_deletions[9]+'}\n'+P_displays[4],'common three-oblique-stroke cancellation, all six lower source blocks')

line_details=[
 ('main_01',174,'Je voudrais maintenant faire passer les'),
 ('main_02',246,'axiomes de disjonction-compatibilité avant'),
 ('main_03',315,'ceux sur les lieux, pour ne pas les en faire'),
 ('main_04',392,'dépendre. Les axiomes sont facultatifs pour'),
 ('main_05',473,'un atelier, et il y aura pas mal des’'),
 ('main_06',550,'implications mutuelles avec les axiomes sur'),
 ('main_07',635,'les lieux.'),
 ('main_08',711,'Une notion essentielle ici est celle de'),
 ('main_09',790,'F et G disjoints'),
 ('main_10',864,'F parallel G, labelled definition'),
 ('main_11',960,'notion qui ne dépend que de ≤. On a d’ailleurs'),
 ('main_12',1045,'quantified equivalence display'),
 ('main_13',1122,'donc interprétation en termes de X parallel Y dans M,'),
 ('main_14',1210,'qui y signifie'),
 ('main_15',1265,'X parallel-under-M Y iff ... et {X,Y} n’est pas'),
 ('main_16',1315,'minoré dans M,≤'),
 ('main_17',1368,'i.e. no Z avec Z≤X,Z≤Y'),
 ('main_18',1440,'(NB Il ... des axiomes ... que'),
 ('main_19',1490,'ça implique que no Z avec Z≪X,Z≪Y,'),
 ('main_20',1535,'cancelled i.e. c’est un [symbol]'),
 ('main_21',1568,'et [cancelled la] réciproque résultera d’axiome(s)'),
 ('main_22',1608,'ci-dessous...)'),
 ('main_23',1686,'At DC 1 (Axiome ...) Soient X,Y∈M,'),
 ('main_24',1760,'[et] K=X∩Y=Sup Z. [Il] Supposons que'),
 ('main_25',1902,'At implication display'),
 ('main_26',1995,'Alors [NB et alors seulement...] X compatibility Y.'),
 ('main_27',2109,'Cor Soient F,G∈script F, K=F∩G=Sup Z.'),
 ('main_28',2203,'Alors F compatibility G, circled ses, quantified X,Y∈M'),
 ('main_29',2266,'Cor implication display'),
]

review=dict(scan='008',status='first-reader proposal; root adjudication pending',
 lines_read=dict(count=39,convention='One count per main text/display physical baseline, including cancelled baselines; each of four slanted-note baselines and five separately written insertion baselines counts once; page numeral counts once. Formula labels, undersets, tildes, primes and Sup limits are counted with their parent formula, not as additional lines. Main baselines can slope slightly.',
  main_text_and_display_baselines=29,slanted_margin_baselines=4,separate_insertion_baselines=5,page_number_baselines=1,
  main_baselines=[dict(id=i,approx_y=y,first_words=w) for i,y,w in line_details],
  insertion_baselines=['avoir l’air de','précédents','soit','pour X′,Y′∈M','cf Cor'],
  slanted_baselines=['Un atelier sera dit','spacieux s’il satisfait','cette condition. Contre-ex. : les','ateliers simpliciaux...']),
 changes=changes,doubts=doubts,inventory=inventory,notation=notation,hand_log=hand_log,notes=notes,
 check_events=[],
 visual_inspections=[
  dict(id='008-V1',action='Viewed the original whole sheet once for layout',result='Located all text blocks, five additions, the four-line slanted note, local corrections and three long diagonal cancellation strokes.'),
  dict(id='008-V2',action='Viewed supplied upper half once, reading each baseline',result='Read opening paragraph, quotations, first two displays and interpretation sentence word/sign by word/sign.'),
  dict(id='008-V3',action='Viewed supplied lower half once, reading each baseline',result='Read M display, NB, all cancelled lower text and the slanted note; checked every formula sign, prime and index.'),
  dict(id='008-V4',action='Viewed all eighteen named cropped places',result='Read every actual C/H word difference, every C doubtful place, the small indices/labels and all local insertions/strikes. Three initially clipped upper edges were extended before decisions, as recorded in the manifest.'),
  dict(id='008-V5',action='Explicit C macro audit',result='Matched all fifteen deleted wrappers and five inserted wrappers to actual ink, including nested earlier corrections inside the globally cancelled block.'),
  dict(id='008-V6',action='Raw difference review',result='All forty-eight raw rows 353–400 classified; source-state differences absent from raw word matching added separately.'),
 ],
 deletion_insertion_audit=audit,difference_review=difference_review,second_boxes=second_boxes,
 doubt_summary=dict(C_marks=21,resolved=0,retained_unchanged=20,revised_but_unresolved=1,new_scope_issue=1),
 crop_manifest=str(ROOT/'out/review/scan008_crop_manifest.json'),
 crop_script=str(ROOT/'out/scripts/scan008_crops.py'))

def display_blocks(s):
    blocks=[]; pos=0
    while (i:=s.find('\\[',pos))>=0:
        j=s.index('\\]',i)+2
        blocks.append(s[i:j]); pos=j
    return blocks

C_displays=display_blocks(C_text)
H_displays=display_blocks(H_text)
by_id={x['id']:x for x in changes}
by_id['008-13'].update(C=C_displays[2],H=H_displays[2],final=P_displays[2])
by_id['008-27'].update(C=r'\margin{'+spans(C_text,'margin')[0]+'}',
    H=r'\marginal{'+spans(H_text,'marginal')[0]+'}',final=r'\margin{'+margin+'}')
for id,k in [('008-28',3),('008-39',6),('008-41',8),('008-45',9),('008-49',12),('008-55',14)]:
    by_id[id].update(C=r'\deleted{'+C_deletions[k]+'}',final=r'\deleted{'+P_deletions[k]+'}')
at_start=H_text.index(r'\emph{At DC 1}')
by_id['008-28']['H']=H_text[at_start:H_text.index('\\[',at_start)].strip()
by_id['008-39']['H']=H_displays[3]
at_conc=H_text.index('Alors [NB')
by_id['008-41']['H']=H_text[at_conc:H_text.index('\\note',at_conc)].strip()
cor_start=H_text.index(r'\emph{Cor}')
cor_alors=H_text.index('Alors $F',cor_start)
by_id['008-45']['H']=H_text[cor_start:cor_alors].strip()
by_id['008-49']['H']=H_text[cor_alors:H_text.index('\\[',cor_alors)].strip()
by_id['008-55']['H']=H_displays[4]
by_id['008-51'].update(
    C=r'\tikz[baseline=(s.base)]{\node[inner sep=1pt] (s) {ses};\draw (s.center) ellipse [x radius=1.05em,y radius=.72em];}',
    H='(ssi)',
    final=r'\tikz[baseline=(s.base)]{\node[inner sep=1pt] (s) {ses};\draw (s.center) ++(30:1.05em and .72em) arc[start angle=30,end angle=-295,x radius=1.05em,y radius=.72em];}')

def exact_primes(value):
    # Python raw single-quoted literals retain their quote-escape backslash.
    # Source primes and French apostrophes are literal apostrophes, not TeX accents.
    if isinstance(value,str): return value.replace("\\'", "'")
    if isinstance(value,list): return [exact_primes(x) for x in value]
    if isinstance(value,dict): return {k:exact_primes(v) for k,v in value.items()}
    return value
review=exact_primes(review)

out=ROOT/'out/review/scan008_review.json'
out.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print(out)
print(f'{len(changes)} changes; {len(doubts)} doubts/scope issues; {len(audit)} state audits; {len(second_boxes)} second boxes; {len(difference_review)} raw rows')
