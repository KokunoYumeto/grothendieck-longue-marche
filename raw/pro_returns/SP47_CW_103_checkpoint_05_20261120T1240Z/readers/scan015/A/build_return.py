from pathlib import Path
import json

out = Path('/workspace/scratch/ae626167fbca/SP47_CW_103_work/readers/scan015/A')
reading = r'''\scanpage{15}

% Detached point at whole-source (199,104), below-left of the initial J;
% its textual status is uncertain, not its physical presence.
$\underset{\hspace{-0.6em}\unsure{\cdot|\phantom{\cdot}}}{\mathrm{J}}$e te signale que j'ai \unsure{réfléchi} aux Gr-champs sur $X$. Si $G$ est un Groupe sur $X$, $N$ un $G$-Module les Gr-champs sur $X$ ``épinglés par $G,N$'' forment a priori une $2$-\unsure{catégorie} et même une $2$-catégorie de Picard stricte, grâce à l'opération évident à la Baer. On trouve que le complexe \inserted{(de cochaines)} tronqué à l'échelon $2$ qui leur correspond est le tronqué
\[
\tau_{\leq 2}\bigl(\mathbb R\Gamma(B_{G}\mathbin{\mathrm{mod}}X,N)[1]\bigr)
\]
(\uline{NB} la cohomologie de $\mathbb R\Gamma(B_{G}\mathbin{\mathrm{mod}}X,N)$ commence en degré $1$) Plus \unsure{géométriquement}, un Gr-champ sur $X$ \unsure{épi-glé|épinglé} \inserted{par $(G,N)$} est essentiellement ``la même chose'' qu'une $2$-gerbe sur $B_{G}$, liée par $N$, et \deleted{\unsure{épi|pri}}\unsure{munie} d'une \unsure{trivialisation} au dessus de $X\approx B_{c}=(B_{G})_{/P}$ (où $P$ est le $\overset{\unsure{\deleted{\mathrm{s}}|\ast}}{\mathrm{o}}$bjet de $B_{G}$ ``torseur universel sous $G$''). Ces $2$-gerbes forment en fait une $3$-catégorie
% The uncertain crossed mark above the o of objet is at about (475,1362).
% Detached point at whole-source (175,1631), below de in the final line.
$\underset{\unsure{\cdot|\phantom{\cdot}}}{\text{de}}$ Picard a priori, mais il se
% archive sheet number: 14
'''
(out/'reading.tex').write_text(reading,encoding='utf-8')

logs=json.loads((out/'view_log.json').read_text())
crops=json.loads((out/'open_loci.json').read_text())
times={r['id']:r['opened_utc'] for r in logs['crops_viewed']}
readings={
'c01':r'\unsure{réfléchi}; the middle ascending strokes remain faint, so the original C doubt is retained.',
'c02':r'$2$-\unsure{catégorie}; the word reaches the right paper edge, with a high final point but no securely complete terminal e.',
'c03':'évident; a separate final t has an upright, cross-stroke and rightward foot; no subsequent e loop is visible.',
'c04':'(de cochaines); one small vertical i-dot, not a two-arm circumflex. The larger higher spot belongs to the Baer full stop on the preceding line. The line below is the insertion hook.',
'c05':r'\unsure{géométriquement}; géométri reaches the right edge, and quement was read at the left of the next line in half_b. The extreme right strokes remain clipped.',
'c06':r'\unsure{épi-glé|épinglé}; after the dotted i there is a detached flat stroke without a securely rising n-shoulder. The g reaches the paper edge; no separate final lé survives inside the page.',
'c07':r'\deleted{\unsure{épi|pri}}\unsure{munie}; a low initial loop precedes the clearest p-descender and final dot. Oblique cancellation strokes obscure the prefix. The live munie has flattened middle strokes and remains doubtful.',
'c08':r'\unsure{trivialisation}; the stem sequence is visible through the late i, but the terminal strokes meet the clipped edge and are not individually established.',
'c09':r'X\approx B_c=(B_G)_{/P}; the first low letter is an open c with no interior bar. The approximate sign has two wavy strokes, the equality two straight strokes; G is low, and /P lies below-right of the enclosing parenthesis.',
'c10':r'\overset{\unsure{\deleted{\mathrm{s}}|\ast}}{\mathrm{o}}bjet; the compact raised crossed unit is above-left of o, not on the baseline and not a pair of quotation strokes. A cancelled s and a small star remain alternatives; the star alternative does not assert a separate cancellation.',
'c11':r'A dark detached point below-left of J, preserved as \unsure{\cdot|\phantom{\cdot}} at that position. Its textual role is unknown.',
'c12':r'A small dark detached point below de, preserved as \unsure{\cdot|\phantom{\cdot}} at that position. Its textual role is unknown.'
}
for c in crops:
    c['processing']['opened_utc']=times[c['id']]
    c['reading']=readings[c['id']]
    c.pop('coordinate_system')

def ch(place,c,h,reading,shows,confidence,kind,marked=False,ac=False,ah=False,ids=()):
    return dict(place=place,c=c,h=h,reading=reading,scan_shows=shows,confidence=confidence,kind=kind,marked_in_H=marked,against_c=ac,against_h=ah,crop_ids=list(ids))

changes=[
ch('Opening Je: detached point below-left of J','omitted','omitted',r'\underset{\hspace{-0.6em}\unsure{\cdot|\phantom{\cdot}}}{\mathrm{J}}e','c11 shows a compact dark triangular point around whole-source (199,104), separate from the faint returning J foot. Its physical presence is definite; textual status is not.','medium','omission',ac=True,ah=True,ids=['c11']),
ch("Opening line, after j'ai",r'\unsure{réfléchi}','réfléchi',r'\unsure{réfléchi}','c01 preserves a low r/e beginning and final chi, but the tall middle f/l strokes and their small high marks are pale. I retain the C doubt rather than certify every middle stroke.','medium','other',ac=False,ah=True,ids=['c01']),
ch('First quotation: épinglés par G,N',r"``épinglés par $G,N$''",'« épinglés par $G$, $N$ »',r"``épinglés par $G,N$''",'Half_a settled the quotation shapes: paired short high pen strokes at each boundary, not angled guillemets. Approximate whole-source box [140,245,1115,362] covers the two-line quotation.','high','other',ac=False,ah=True),
ch('First 2-catégorie, right edge of line 5',r'$2$-\unsure{catégorie}','2-catégorie',r'$2$-\unsure{catégorie}','c02 shows catégorie extending to the paper boundary. The late dot/short strokes survive, but the complete terminal e does not. The full proposed word remains explicitly doubtful.','medium','other',ac=False,ah=True,ids=['c02']),
ch('After opération, line 7',r'\unsure{évident|évidente}','évidente','évident','c03 shows the last unit as t: a tall upright with a short rightward cross-stroke and a lower rightward foot. There is white space after it and no separate following e.','high','misread word',ac=True,ah=True,ids=['c03']),
ch('Interlinear insertion after complexe',r'\inserted{(de \unsure{cochaines|cochaînes})}',r'\add{(de cochaînes)}',r'\inserted{(de cochaines)}','c04 shows one short vertical dot over i. No two converging circumflex strokes are present. The large higher dot is the preceding line’s full stop after Baer, not a word accent.','high','abbreviation expanded or spelling modernised',ac=True,ah=True,ids=['c04']),
ch('Display: derived R',r'\mathbb R','R',r'\mathbb R','Half_a settled a separate inner upright within the outer R outline. This is a doubled R, not merely a thick ordinary stem. Approximate whole-source box [469,730,520,783].','high','misread symbol or index',ac=False,ah=True),
ch('NB parenthesis: derived R',r'\mathbb R','R',r'\mathbb R','Half_a and the overlapping top of half_b showed an outer R outline with an additional upright. Approximate whole-source box [718,814,772,870]. No separate crop was made.','high','misread symbol or index',ac=False,ah=True),
ch('Plus géométriquement across lines 13–14',r'\unsure{géométriquement}','géométriquement',r'\unsure{géométriquement}','c05 shows géométri running into the right edge. Half_b supplied the independently visible continuation quement at the start of the following line. The extreme-right letter parts remain clipped, so the whole-word doubt is retained.','medium','other',ac=False,ah=True,ids=['c05']),
ch('Second épinglé, right edge of line 14',r'\unsure{épinglé}','épinglé',r'\unsure{épi-glé|épinglé}','c06 shows a detached nearly flat horizontal at the n-position after the dotted i, without a secure n shoulder. A low g loop and returning descender touch the paper boundary. Final lé is outside the surviving visible word area. The dash reading is first; both alternatives retain the clipped-ending reservation.','low','misread word',ac=True,ah=True,ids=['c06']),
ch('Quotation la même chose',r"``la même chose''",'« la même chose »',r"``la même chose''",'Half_b settled both boundaries as paired high short pen strokes. Approximate whole-source box [656,1038,1081,1094].','high','other',ac=False,ah=True),
ch('Cancelled prefix before munie',r'\deleted{\unsure{pri|épi}}',r'\struck{\ill{}}',r'\deleted{\unsure{épi|pri}}','c07 shows a low loop before the clearest long p-descender and a high terminal dot. Four oblique cancelling strokes obscure the earlier letters. The surviving order favours épi over pri, but does not justify certainty.','low',r'readable ink left as \ill{}',marked=True,ac=True,ah=True,ids=['c07']),
ch('Live word after cancelled prefix',r'\unsure{munie}','munie',r'\unsure{munie}','c07 shows three low joined groups and a faint final e; the interior shoulders are flattened and the small i mark is weak. Retain the C doubt.','medium','other',ac=False,ah=True,ids=['c07']),
ch("After d'une, right end of line 17",r'\unsure{trivialisation}','trivialisation',r'\unsure{trivialisation}','c08 shows the ascending t/l/t and several i-dots, but the terminal on is not individually recoverable inside the clipped right edge. The proposed full word remains doubtful.','medium','other',ac=False,ah=True,ids=['c08']),
ch('First B subscript in X≈B…',r'B_{\unsure{e|c}}','B_e','B_c','c09 shows one low open c-curve with a long lower exit and an empty interior. There is no interior e bar. Resolve c from the strokes, without replacing it from the surrounding interpretation.','high','misread symbol or index',ac=True,ah=True,ids=['c09']),
ch('Raised crossed unit above-left of o in objet',r'le \deleted{\unsure{s|$\ast$}}objet','le « objet',r'le $\overset{\unsure{\deleted{\mathrm{s}}|\ast}}{\mathrm{o}}$bjet','c10 shows a compact raised loop with crossing/diagonal strokes at about (475,1362), above-left of the live o. It is not two guillemet strokes. A cancelled s is the first candidate, with a small star as an alternative whose deletion state is not independently established. Preserve the height instead of placing the unit as a baseline prefix.','low','misread symbol or index',ac=True,ah=True,ids=['c10']),
ch('End of torseur universel sous G quotation and prose parenthesis',r"$G$'').",'$G$" »).',r"$G$'').",'Half_b settled a pair of high closing quote strokes after G, followed by one round parenthesis and a point. There is no additional outer guillemet between the quotation and the parenthesis. Approximate whole-source box [505,1416,624,1477]. H’s inner straight double-quote notation itself is not counted as a reading difference.','high','text not on the page',ac=False,ah=True),
ch('Final line: detached point below de','omitted','omitted',r'\underset{\unsure{\cdot|\phantom{\cdot}}}{\text{de}}','c12 shows a small dark detached point around (175,1631), below the de group. Its textual role is unassigned; the no-textual-character alternative does not deny the physical mark.','medium','omission',ac=True,ah=True,ids=['c12'])
]

unresolved=[
{'place':"Opening réfléchi",'reading':r'\unsure{réfléchi}','alternatives':['réfléchi; middle strokes remain pale'],'confidence':'medium','evidence':'c01: thin internal ascenders and small high marks; no alternate full word is asserted.'},
{'place':'First catégorie at right edge','reading':r'\unsure{catégorie}','alternatives':['catégorie; complete ending remains clipped'],'confidence':'medium','evidence':'c02: last high point and short strokes survive, but no independently complete final e.'},
{'place':'géométriquement across line break','reading':r'\unsure{géométriquement}','alternatives':['géométriquement; the extreme-right junction remains clipped'],'confidence':'medium','evidence':'c05 plus quement already read in half_b; no visible division hyphen was supplied.'},
{'place':'Second épinglé','reading':r'\unsure{épi-glé|épinglé}','alternatives':['épi-glé','épinglé'],'confidence':'low','evidence':'c06: flat separated stroke after the dotted i; no secure n shoulder; the ending lé has no independent surviving strokes inside the clipped edge.'},
{'place':'Cancelled prefix','reading':r'\deleted{\unsure{épi|pri}}','alternatives':['épi','pri'],'confidence':'low','evidence':'c07: low first loop, later p-descender and high dot survive under oblique cancellation.'},
{'place':'munie','reading':r'\unsure{munie}','alternatives':['munie; flattened middle letters not independently secure'],'confidence':'medium','evidence':'c07: the low stroke groups favour the proposed word but remain compressed.'},
{'place':'trivialisation','reading':r'\unsure{trivialisation}','alternatives':['trivialisation; terminal strokes remain clipped'],'confidence':'medium','evidence':'c08: final on is not individually established inside the paper edge.'},
{'place':'Raised unit above objet','reading':r'\overset{\unsure{\deleted{\mathrm{s}}|\ast}}{\mathrm{o}}','alternatives':['cancelled s','small star, deletion not independently established'],'confidence':'low','evidence':'c10: compact upper loop and crossing lower diagonal; exact original letter and layer cannot be isolated.'},
{'place':'Point below-left of Je','reading':r'\unsure{\cdot|\phantom{\cdot}}','alternatives':['textual point','nontextual mark'],'confidence':'medium','evidence':'c11: definite detached dark point at about (199,104), with no secure textual function.'},
{'place':'Point below de in final line','reading':r'\unsure{\cdot|\phantom{\cdot}}','alternatives':['textual point','nontextual mark'],'confidence':'medium','evidence':'c12: definite small dark point at about (175,1631), with no secure textual function.'}
]

hand='another unnamed hand (dark pen; personal attribution not established from this packet)'
def inv(element,kind,position,first,transcribed='yes',whichhand=hand):
    return {'sheet_kind':'letter','hand':whichhand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':transcribed}
inventory=[
inv('Opening prose through est le tronqué','text','whole-source x145–1115, y40–728',"Je te signale que j'ai réfléchi"),
inv('Interlinear parenthesis and its insertion hook','insertion','x292–608, y565–654','(de cochaines), attached after complexe'),
inv('Displayed truncation formula','display','x347–1039, y730–807',r'\tau_{\leq2}(\mathbb R\Gamma(B_G mod X,N)[1])'),
inv('NB parenthesis with inline cohomology formula','text','x137–1076, y817–946','(NB la cohomologie de'),
inv('NB single underline','text','x169–224, y869–876','NB'),
inv('Geometrical description through final incomplete clause','text','x132–1116, y888–1627','Plus géométriquement, un Gr-champ'),
inv('Left-side phrase and its insertion hook','insertion','x18–215, y1028–1101','par (G,N), attached after the right-edge épinglé and before est'),
inv('Cancelled prefix before live munie','deletion','x335–413, y1205–1255','épi / pri'),
inv('Raised crossed unit above-left of objet','deletion','x467–484, y1351–1375','cancelled s / small star; state remains uncertain'),
inv('Detached initial point','text','approximately (199,104), below-left of initial J','point / nontextual mark'),
inv('Detached final-line point','text','approximately (175,1631), below de','point / nontextual mark'),
inv('Archive pencil sheet number','text','x41–97, y1646–1689','14',whichhand='another unnamed hand (lighter pencil; attribution and identity relative to the pen hand not established)')
]

notation=[
{'place':'All prose mathematical capitals and quoted pair','sign':'G, X, N; Gr; G,N','ink':'Ordinary pen capitals with single outlines; G has a curved bowl and internal return, X crossed diagonals, N joined uprights. Gr has the extra small r. The first quoted pair has a low comma without surrounding parentheses. No comma follows Module.','latex':r'G,\ X,\ N;\ G\text{-Module};\ G,N;\ Gr\text{-champs}'},
{'place':'All dimension prefixes, échelon and degree statement','sign':'2; 3; 1','ink':'The category/gerbe dimensions are baseline numerals followed by hyphens. The final category has two lobes of 3, distinct from the 2 figures. Échelon has 2 and the NB has degree 1.','latex':r'2\text{-catégorie};\ 2\text{-gerbe};\ 3\text{-catégorie};\ 2;\ 1'},
{'place':'Display, first operator','sign':'tau with low ≤2','ink':'Tau has a flat top and hooked lower body. Its low qualifier has an angular left-pointing upper portion and a separate lower bar, followed by low 2.','latex':r'\tau_{\leq2}'},
{'place':'Display and NB inline formula','sign':'derived R, Gamma and B subscript','ink':'Each R has an outer bowl/leg and additional inner upright. Gamma has a headbar and descending stem. B has two curves, G lies low-right. The plain mod letters are followed by X and a low comma before N.','latex':r'\mathbb R\Gamma(B_G\mathbin{\mathrm{mod}}X,N)'},
{'place':'Display ending','sign':'[1] and closing delimiters','ink':'Square opening and closing surround an upright 1; there is no minus. Round parentheses enclose the derived expression and the Gamma arguments.','latex':r'\tau_{\leq2}(\mathbb R\Gamma(B_G\mathbin{\mathrm{mod}}X,N)[1])'},
{'place':'Later inserted pair','sign':'(G,N)','ink':'Separate opening/closing round parentheses and a low comma; the phrase is joined by a curved insertion hook.','latex':r'\inserted{par $(G,N)$}'},
{'place':'Relation and slice, c09','sign':'approximately equal, c, equality, /P','ink':'Two wavy strokes after X; low c is open with no interior bar; two straight equality strokes; low G after the second B; slash and capital P below-right of its closing parenthesis.','latex':r'X\approx B_c=(B_G)_{/P}'},
{'place':'NB rubric','sign':'single underline','ink':'One short rule under NB only. No double line.','latex':r'\uline{NB}'},
{'place':'All three quotation spans','sign':'paired high quotation strokes','ink':'Paired high pen strokes enclose épinglés par G,N, la même chose and torseur universel sous G. There is no additional outer quotation around objet de B_G and the torseur phrase.','latex':r"``...''"},
{'place':'Interlinear cochaines, c04','sign':'plain i-dot','ink':'One short vertical dot over i; no circumflex pair. The higher broad point belongs to the preceding Baer full stop.','latex':'cochaines'},
{'place':'Second épinglé, c06','sign':'dash / flattened n','ink':'A separated flat stroke is visible at the n-position; no n shoulder is secure. The final letters are clipped.','latex':r'\unsure{épi-glé|épinglé}'},
{'place':'Above-left of o in objet, c10','sign':'cancelled s / star','ink':'Small raised loop with crossing diagonal; letter and deletion state are not fully separable. Position is preserved above o.','latex':r'\overset{\unsure{\deleted{\mathrm{s}}|\ast}}{\mathrm{o}}'},
{'place':'Below-left of J and below final de, c11/c12','sign':'detached points','ink':'Two isolated dark points, with no assigned semantic role. Physical presence is secure; textual status is uncertain.','latex':r'\unsure{\cdot|\phantom{\cdot}}'},
{'place':'Footer','sign':'14','ink':'Lighter pencil 1 followed by angular 4 at lower left. No separate author page number is visible.','latex':'% archive sheet number: 14'}
]

notes=[
'Coverage: I compared every text block, every word and ending, all punctuation and accents, and every inline/display formula against BOTH C and H while viewing the whole once for layout and each half once in order. This included agreed readings. No other page input, image, reader return, OCR, PDF text layer, outside research or delegation was used.',
'Whole-source dimensions are 1129×1733 pixels. Half_a is 1129×946 and corresponds to whole-source origin (0,0); half_b is 1129×947 and starts at whole-source y=786. Every crop box in this report uses whole-source pixels in (left, top, right, bottom) order.',
'The first recorded UTC clock observation, used as start_utc, was 2026-11-20 12:30:34 UTC; the brief had already been read when that clock was taken. Image-open times are the actual clock readings immediately before the corresponding view_image calls, not invented reading-completion times. Crop times are retained in each processing object and in view_log.json.',
'Open loci were listed and saved in open_loci.json before making the 12 crops. Each listed crop was generated once and inspected once. No whole/half image was reopened, no settled locus was recropped, and no LaTeX compilation, installation, format generation or rendering was attempted.',
'Half-settled witness differences with no reader crop: quotation épinglés par G,N, approximate whole-source box [140,245,1115,362]; display doubled R [469,730,520,783]; inline doubled R [718,814,772,870]; quotation la même chose [656,1038,1081,1094]; absence of an additional closing guillemet after G [505,1416,624,1477]. These boxes are observation metadata, not additional image views.',
'This is a continuation of a handwritten letter: no letterhead, date, salutation, signature, heading, independent diagram or non-diagram drawing is visible on this scan. The two curved connector strokes are insertion hooks, represented at their textual attachments. The lower pencil 14 is archive metadata. No personal identification of either writing layer is established here.',
'The page states that Gr-champs on X pinned by G,N form a 2-category, and even a strict Picard 2-category through an operation à la Baer. It gives a truncated derived relative-sections expression. It then describes such a Gr-champ as essentially the same thing as a 2-gerbe on B_G linked by N and equipped with a trivialisation over the displayed slice expression. The final claim begins a 3-category-of-Picard qualification and ends visibly at mais il se; no continuation was imported.',
'The initial reflected-word doubt and right-edge word doubts are retained because particular strokes remain faint or clipped. A full proposed word inside unsure is not a claim that the invisible terminal letters were recovered. At the later épinglé the flat internal stroke prompted the additional épi-glé alternative; no mathematical expectation was used to supply its missing ending.',
'The raised object mark is represented above the o, not moved to a baseline sequence. Its first reading is cancelled s; the alternative small star carries uncertainty about deletion state. The points below the initial J and final de are likewise preserved at their observed vertical positions with no-textual-character alternatives. Those alternatives do not deny the visible marks.',
'Mathematical checking was limited to the explicitly logged conditional degree-shift arithmetic. The visual recognition of the formula, equality, slice, dimensions, group letters and quotation structure is not counted as proof. The claimed classification, relative-cohomology vanishing and Picard-category assertions were not independently proved.'
]

report={
'scan':15,'reader':'A','start_utc':logs['start_utc'],'end_utc':'PENDING_FINAL_CLOCK',
'model':'GPT-6 Astra Pro','effort':'not exposed','viewed':logs['viewed'],'crops':crops,
'changes':changes,'unresolved':unresolved,'inventory':inventory,'notation':notation,
'abbreviations':[{'form':'NB','expansion':'nota bene'},{'form':'mod','expansion':'modulo'},{'form':'Gr','expansion':'groupe (within Gr-champs; not expanded in the transcription)'}],
'notes':notes,
'math_checks':[{'statement_id':'scan015-conditional-degree-shift','place':'Displayed complex and following NB','statement':'Conditional on the page’s assertion that the unshifted relative derived sections begin in degree 1, the cohomological shift [1] moves the first possible degree to 0, and truncation at ≤2 retains degrees 0, 1 and 2.','type':'computation or formal certificate','outcome':'Computed H^i(K[1])=H^{i+1}(K): the onset changes from 1 to 1−1=0; applying τ≤2 keeps the possible degrees 0,1,2. This checks only the shift/truncation arithmetic under the stated vanishing assumption, not that assumption or the classification by 2-gerbes.'}]
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote reading.tex and draft report.json:',len(changes),'change loci;',len(unresolved),'unresolved loci;',len(crops),'crops.')
