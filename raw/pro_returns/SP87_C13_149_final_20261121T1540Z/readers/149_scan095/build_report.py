import json
from pathlib import Path
p=Path('SP87_C13_149_work/readers/149_scan095')
boxes=json.loads((p/'crop_boxes.json').read_text())
def crop(n): return 'crops/149_scan095_'+n+'.png'
changes=[]
def change(place,c,h,final,evidence,n,kind,against_c=False,against_h=True,confidence='high',marked_in_h=False,consequential=False):
 changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=crop(n),box=boxes[n],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential))
change('095-incite','incite','intéresse','incite','An initial dotted i is followed by the compressed n, open c, a second i, crossed t and final e. There is no longer interesse sequence.','incite_justement','misread word')
change('095-a-regarder','à',':',r'\unsure{à|:}','Two small vertically separated marks stand before regarder. The lower mark is a compressed angular bowl, unlike a plainly round colon dot, but its a outline is not fully separable; preserve the local alternative.','a_regarder','misread word',confidence='medium')
change('095-les','les','la',r'\unsure{les|la}','After the tall looped l a low connector runs into a small closed terminal loop. It can be compressed e-s, comparable with the small end loop of classes, but an a bowl cannot be excluded. Grammar is not used to decide.','les','misread word',confidence='medium')
change('095-classes','classes','classe','classes','The two internal s strokes are separate; after the open e and its low connector there is a small additional closed return, read as final s.','classes','misread word',confidence='medium')
change('095-scindages-comma',',','[nothing]',r'\unsure{,}','After g, the low e ends in a downward return that can encode final s; a detached angular stroke follows before de. That detached stroke can be a comma, but it may itself be the final s if the preceding return belongs only to e. Keep a doubtful comma, with absence as the alternative.','scindages_stop','other',confidence='medium')
change('095-E-XB',r'\mathcal E_{\unsure{X_B|X_{s_\alpha}}}',r'\mathcal E_{X_s}',r'\mathcal E_{X_B}','Read with the entire phrase E_XB sur E_k(s): beneath X is an upright with two right-hand lobes. It has the B-shaped outline, not a separate s and alpha. A tiny detached low dot is not securely attached as a mathematical sign and is not added to the formula.','E_XB','misread symbol or index',consequential=True)
change('095-dun',"d'un","d'une","d'un",'The apostrophe is detached after d; the low u-n run ends without an independent e before the gap to uniformi-.','dun','misread word')
change('095-uniformisant','uniformisant','uniformisante','uniformisant','The margin split is uniformi- / sant. In the second part the terminal t has a cross stroke and ends before a broad gap to de; no final e is present. The first part is independently visible in crops/149_scan095_uniformi.png.','sant','misread word')
change('095-vois','vois.','voisinage','vois.','The short form consists of v-o-i-s followed by a separate dark stop; the following word is de. No -inage is written.','vois','abbreviation expanded or spelling modernised')
change('095-deleted-plus-gen',r'\deleted{\unsure{(plus gén.)}}',r'\struck{(spécialisation)}',r'\deleted{\unsure{(plus gén.)}}','The crossed parenthesis contains a descending p and tall l, then the short us run; the next group has the g descender and an accent above the e-region. It is much shorter than spécialisation. The cancellation overlaps the final abbreviation stop, so C’s local doubt is retained.','deleted_plus_gen','misread word',confidence='medium')
change('095-parenthesis-insertion',r'\inserted{(qui intervient par le ...)}','(qui interviennent par le ...) [unmarked inline]',r'\inserted{(qui intervient par le \unsure{biais|bout} qu\textquoteright\unsure{elles définissent|elle définit} $\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}$)}','The new parenthesis is raised above the s_alpha / Quant baseline and continues into a smaller quotient on a second raised tier. It replaces the crossed short parenthesis and attaches after s_alpha, before Quant; it is not a new main-line sentence.','insertion_start','insertion or placement')
change('095-intervient','intervient','interviennent','intervient','The verb after qui ends in the t-like upstroke and cross return after the single compressed vient sequence. No second nen group intervenes before par.','insertion_start','misread word')
change('095-dans','dans','[nothing]','[nothing]','The raised sentence ends at définissent on the right. The quotient resumes below, under le biais; the area to its left, below intervient/par, is blank. The insertion_start, insertion_verb and quotient crops together contain no written dans. The word is removed rather than supplied from syntax.','insertion_start','text not on the page',against_c=True,against_h=False)
change('095-quotient',r'\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}',r'U_{s_\alpha}/\ldots',r'\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}','Both main letters have the repeated humps of m, each with lower s_alpha. A slanted division stroke separates them; the second term carries an elevated 2 and is followed by the closing parenthesis. The q descender from the line above crosses the second m but is not a deletion.','quotient','misread symbol or index',consequential=True)
change('095-salpha-comma',r's_\alpha.',r's_\alpha.',r's_\alpha,','A detached short diagonal stroke after alpha has a downward tail, unlike the plainly round stop after inversible. It is read as a comma.','salpha_quant','misread symbol or index',against_c=True)
change('095-Quant-a','Quant à','. Quand on a','Quant à','The initial word has the large Q loop and terminal t upstroke; a compact accented a follows. The next word is ces, without on or a second a. No separate full stop follows the raised parenthesis.','salpha_quant','misread word')
change('095-conormal-index',r'\underline N_{D_\alpha,S}^{\unsure{r|\vee}}',r'\mathcal N^{\vee}_{D_\alpha/S}',r'\underline N_{D_\alpha,S}^{\unsure{r|\vee}}','Between alpha and S the first N index contains a short hooked descending comma. It differs visibly from the long straight diagonal slash in the later N_Dalpha/S. The underline beneath N is retained; alphabet-wrapper choices are not counted as another change.','conormal','misread symbol or index',consequential=True)
change('095-conormal-exponent',r'\unsure{r|\vee}',r'\vee',r'\unsure{r|\vee}','The superscript has a stem descending below a short right shoulder, favouring literal r. The small faint outline does not exclude an unusually drawn vee, and no identical same-page superscript settles it. Expected duality is not used to replace the preferred ink reading.','conormal','misread symbol or index',confidence='medium',consequential=True)
change('095-ampersand',r'\unsure{\&|et}',r'\uncertain{et}',r'\&','After the comma following régulier is one tall curled, crossing glyph with retracing. It is not the separate low e and crossed t visible in the later et after régulière.','regular_amp','abbreviation expanded or spelling modernised',marked_in_h=True)
change('095-donc','donc','du',r'\unsure{donc|du}','After the looped d, the rest is strongly compressed into a low run with a small rise and turned end. It favours donc, but the internal o-n-c divisions are not fully distinct; du remains a local alternative. The following two tiny isolated ink specks are not securely textual punctuation.','donc','misread word',confidence='medium')
change('095-parenthesis-order',r'(si on suppose $D_\alpha$ régulier, \& donc $\underline N_{D_\alpha/S}$ inversible) reste régulière, et inversible.',r'(si on suppose $D_\alpha$ régulier) reste régulière, et du $\mathcal N_{D_\alpha/S}$ inversible.',r'(si on suppose $D_\alpha$ régulier, \& \unsure{donc|du} $\underline N_{D_\alpha/S}$ inversible) reste régulière, et inversible.','The right parenthesis is drawn immediately after the first inversible beside N_Dalpha/S. The next baseline segment reads reste régulière, et, and a further main-line inversible has a round stop. H closes the parenthesis too early and relocates the regularity words. The full clause is supplied in an anonymous second-reading box.','N_inverse','insertion or placement',consequential=True)
change('095-cequi-insertion',r'\deleted{comment} \inserted{ce qui}',r'\struck{comment} ce qui',r'\deleted{comment} \inserted{ce qui}','A straight cancellation crosses comment; ce qui is written on a higher baseline directly above it. The q descender crosses the strike without cancelling the inserted phrase.','cequi','insertion or placement')
change('095-deuxieme-placement',r'sections \inserted{de deuxième type} d\textquoteright extensions',r"sections d'extensions du deuxième type",r"sections \inserted{de deuxième type} d'extensions",'The raised first word is de, followed by deuxième type. A long curved leader returns to the gap before d’extensions, after sections. The leader is an attachment stroke, not an underline or a new parenthesis. The final s of d’extensions is visible.','deuxieme','insertion or placement',consequential=True)
change('095-groupes-placement',"d'extensions de groupes profinis, en faisant une étude","d'extensions du deuxième type, en faisant une étude de groupes profinis",r"d'extensions de groupes profinis, en faisant une étude",'The next main line begins de groupes profinis, directly after d’extensions on the preceding line. The comma follows profinis. The phrase is not after une étude; H has moved it across en faisant une étude.','groupes','insertion or placement',consequential=True)
change('095-moins-dun',r"\deleted{moins} \inserted{d'un}","d'un",r"\deleted{moins} \inserted{d'un}",'The lower moins is crossed by a horizontal cancellation. Above it, a clear d plus apostrophe and u-n run supplies d’un. H omits the cancelled state and does not mark the raised replacement.','moins_dun','deletion state')
change('095-question-comma','question.','question.','question,','The detached mark after question is a hooked comma, with an open curved interior and descending end; it is not the round closed full stop seen after inversible.','question_stop','misread symbol or index',against_c=True)
change('095-moins-brulant','moins brûlant',r'\uncertain{mineur}','moins brulant','There are two words. The first has m, dotted i in the o-i-n run and terminal s; the second has tall b and l, with the intervening r-u and final a-n-t. Above u no circumflex is drawn, although the crop includes the ascender height and blank space there. Both the words and the absent accent are preserved.','moins_brulant','misread word',against_c=True,marked_in_h=True)
change('095-ending',"--- car cela n'est",r'--- \ill{}',"--- car cela n'est",'After the dash the c-a-r, c-e-l-a and n-apostrophe-e-s-t strokes are readable. The terminal t has its exit stroke; no full stop or further word is present at the leaf end.','ending',r'readable ink left as \ill{}',marked_in_h=True)
change('095-folio94',r'\margin{94}','[nothing]',r'\margin{94}','The fine lower-left hand writes a round-headed 9 with long tail followed by an open angular 4. Its hand and position differ from the author’s top-centre 47.','folio94','omission')
marks=[]
def mark(i,decision,reading,evidence,n,confidence):
 marks.append(dict(id=i,decision=decision,reading=reading,evidence=evidence,crop=crop(n),box=boxes[n],confidence=confidence))
mark('M1275','first',r'X_B','The complete E_XB sur E_k(s) crop shows a nested B with an upright and two right-hand lobes, with no separate s-alpha pair. The reading is literal and does not claim to identify B mathematically.','E_XB','high')
mark('M1276','undecided',r'\unsure{biais|bout}','The b is tall and looped, followed by compressed short strokes and a dot. The low ending lacks a clearly separate terminal t, favouring biais, but not every internal i/a stroke is distinct enough to dismiss bout categorically.','insertion_start','medium')
mark('M1277','undecided',r'\unsure{elles définissent|elle définit}','The pronoun has two tall l-like returns and a hooked ending, while the long verb favours définissent. Descenders from pt gén. above cross the smaller verb, and the final plural divisions are crowded. Retain the first reading and alternative.','insertion_verb','medium')
mark('M1278','undecided',r'\unsure{r|\vee}','The superscript’s descending stem and short shoulder favour r; the faint small outline and lack of a same-page identical control prevent a categorical exclusion of vee. The full N formula is preserved in its second box.','conormal','medium')
mark('M1279','first',r'\&','A single tall curled glyph crosses itself after the comma. Contrast with the separate written et after régulière on the following line settles ampersand rather than expanded et.','regular_amp','high')
inventory=[]
def inv(element,kind,position,words,hand='his hand'):
 inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('author-page','margin note','top centre, about x810–900 y25–85','47')
inv('paragraph-1','text','upper and middle body, principal baselines 1–13','qui nous incite justement … inversible.')
inv('cancelled-parenthesis','deletion','raised above baseline 7, left of replacement parenthesis','(plus gén.) [doubt retained]')
inv('replacement-parenthesis','insertion','above baseline 7, x610–1620, with quotient on a lower raised tier','(qui intervient par le biais …)')
inv('paragraph-2','text','lower body, principal baselines 14–20',"On peut se proposer d’étudier … car cela n’est")
inv('cancelled-comment','deletion','end of baseline 14, below ce qui','comment')
inv('ce-qui','insertion','above end of baseline 14','ce qui')
inv('deuxieme-type','insertion','above baseline 16; leader attaches between sections and d’extensions','de deuxième type')
inv('cancelled-moins','deletion','right end of baseline 19','moins')
inv('replacement-dun','insertion','above cancelled moins at right end of baseline 19',"d'un")
inv('folio-number','margin note','bottom-left margin, x20–85 y2306–2348','94','another unnamed hand')
second=[]
def sb(kind,b,reading):
 second.append(dict(box=f'B095_{len(second)+1:02d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
def sc(n,kind,reading): sb(kind,boxes[n],reading)
sb('handwritten number',[800,20,915,90],'47')
sc('incite_justement','different word','incite justement')
sc('a_regarder','doubtful word',r'\unsure{à|:} regarder')
sc('les','different word',r'\unsure{les|la}')
sc('classes','different word','classes')
sc('scindages_stop','doubtful punctuation',r'de scindages\unsure{,} de')
sc('E_XB','formula',r'$\mathcal E_{X_B}$ sur $\mathcal E_{k(s)}$')
sc('dun','different word',"d'un")
sc('uniformi','different word','uniformi-')
sc('sant','different word','sant de')
sc('vois','different word','au vois. de son pt gén.')
sc('deleted_plus_gen','deletion',r'\deleted{\unsure{(plus gén.)}}')
sb('insertion',[610,645,1630,782],r"\inserted{(qui intervient par le \unsure{biais|bout} qu'\unsure{elles définissent|elle définit} $\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}$)}")
sc('quotient','formula',r'$\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}$)')
sc('salpha_quant','different word and punctuation',r'$s_\alpha$, Quant à ces')
sc('en_lesquels','retraced text','en lesquels')
sc('conormal','doubtful formula',r'$\underline N_{D_\alpha,S}^{\unsure{r|\vee}}$')
sc('regular_amp','different word',r'$D_\alpha$ régulier, \&')
sc('donc','different word',r'\unsure{donc|du}')
sc('N_inverse','formula',r'$\underline N_{D_\alpha/S}$ inversible)')
sb('phrase placement',[270,1110,1660,1545],r'(si on suppose $D_\alpha$ régulier, \& \unsure{donc|du} $\underline N_{D_\alpha/S}$ inversible) reste régulière, et inversible.')
sc('reste','phrase placement','reste régulière, et')
sc('inversible_stop','punctuation','inversible.')
sc('cequi','deletion and insertion',r'\deleted{comment} \inserted{ce qui}')
sc('deuxieme','insertion',r"\inserted{de deuxième type} d'extensions")
sc('groupes','phrase placement','de groupes profinis,')
sc('moins_dun','deletion and insertion',r"\deleted{moins} \inserted{d'un}")
sc('question_stop','punctuation','question,')
sc('moins_brulant','different word','moins brulant')
sc('ending','readable ending',"--- car cela n'est")
sc('folio94','handwritten number','94')
unresolved=[
 dict(place='095-a-regarder',reading='à',alternatives='colon (:)',confidence='medium'),
 dict(place='095-les',reading='les',alternatives='la',confidence='medium'),
 dict(place='095-scindages-comma',reading='comma after scindages',alternatives='no punctuation: detached angular glyph is the final s of scindages',confidence='medium'),
 dict(place='095-deleted-plus-gen',reading='(plus gén.)',alternatives='final abbreviation stop cannot be isolated from cancellation; exact struck ending remains uncertain',confidence='medium'),
 dict(place='M1276',reading='biais',alternatives='bout',confidence='medium'),
 dict(place='M1277',reading='elles définissent',alternatives='elle définit',confidence='medium'),
 dict(place='M1278',reading='r',alternatives=r'\vee',confidence='medium'),
 dict(place='095-donc',reading='donc',alternatives='du',confidence='medium')]
coverage={
'D0411':('editorial scan/page marker encoding, no source-text difference',None),
'D0412':('H editorial description of the author page number, not manuscript text',None),
'D0413':('substantive wording; source incite','095-incite'),
'D0414':('substantive word/punctuation disagreement retained locally doubtful','095-a-regarder'),
'D0415':('article unresolved; final s preferred in classes','095-les; 095-classes'),
'D0416':('punctuation unresolved, comma retained with local doubt','095-scindages-comma'),
'D0417':('whole E subscript read on crop; literal B preferred','095-E-XB'),
'D0418':('same whole E subscript decision as D0417; no separate alpha restored','095-E-XB'),
'D0419':('pure dash encoding',None),
'D0420':('masculine ending read independently in article and split word','095-dun; 095-uniformisant'),
'D0421':('source abbreviation preserved','095-vois'),
'D0422':('different cancelled words; C reading preferred but cancellation doubt retained','095-deleted-plus-gen'),
'D0423':('singular verb and raised insertion state','095-intervient; 095-parenthesis-insertion'),
'D0424':('biais/bout is a C alternative; no different preferred word from H, unresolved M1276 retained',None),
'D0425':('pronoun/verb alternatives remain M1277; C supplied dans removed and H U corrected from quotient','095-dans; 095-quotient'),
'D0426':('complete denominator and exponent visible in quotient','095-quotient'),
'D0427':('Quant à and absence of H added full stop before it','095-Quant-a'),
'D0428':('superscript ordering is macro syntax only; actual exponent tracked separately',None),
'D0429':('first N index has comma, unlike later slash','095-conormal-index'),
'D0430':('literal r preferred with vee alternative retained','095-conormal-exponent'),
'D0431':('H closes parenthesis too early and moves reste régulière','095-parenthesis-order'),
'D0432':('source ampersand, not H expanded et; M1279 resolved on crop','095-ampersand'),
'D0433':('donc/du wording disagreement remains local doubt','095-donc'),
'D0434':('original parenthesis and regularity/invertibility order restored','095-parenthesis-order'),
'D0435':('pure dash encoding',None),
'D0436':('inserted de deuxième type attaches before d’extensions','095-deuxieme-placement'),
'D0437':('d’extensions de groupes profinis belongs before en faisant','095-deuxieme-placement; 095-groupes-placement'),
'D0438':('same relocation of de groupes profinis as D0437, not an extra source phrase','095-groupes-placement'),
'D0439':('cancelled moins and raised d’un preserved','095-moins-dun'),
'D0440':('source moins brulant, without written circumflex','095-moins-brulant'),
'D0441':('readable final words and separate folio; dash encoding itself ignored','095-ending; 095-folio94')}
notes=("Content summary: The page continues a discussion of classes of splittings relative to L_i, especially those attached to a local uniformizer at the generic point s_alpha of D_alpha. A raised parenthesis refers to the associated class in m_salpha/m_salpha^2. The author says specialization is clear at points where the rational section of the stated conormal sheaf remains regular and invertible. He then proposes studying specialization of sections of the second type at the other points, by an analogous study of extensions of profinite groups, but calls this a less burning interest; the final sentence ends unfinished at car cela n’est. "
"Layout and reading: two prose paragraphs, twenty principal baselines, no display, diagram or drawing; four raised insertions, three cancellations, the author’s 47 above and a fine other-hand 94 below left. The whole source and both supplied halves were read once; thirty unique crops were saved and read. Existing crops were reused, without recropping, to compare the article, classes ending, scindages punctuation and the disputed absence of dans. "
"Diplomatic cautions: preserve XB literally, without identifying or normalizing B. The two conormal indices differ on the page: first D_alpha comma S, later D_alpha/S. The first superscript remains r|vee despite the familiar conormal context; no mathematical expectation settles that stroke. The plural reading of the crowded raised verb and biais remain locally uncertain. The cancelled plus gén. doubt remains because its stop is crossed. No dans is written between the verb and the quotient, so it is absent from the draft. Both s_alpha and question have comma-shaped tails, while the final inversible has a round stop. Brulant has no visible circumflex. Uniformisant is physically divided uniformi- / sant at a line end; the running transcription joins the word. The en before lesquels is retraced on its existing strokes, with no separable earlier word or cancellation. The q descender over the quotient and the curved leader under de deuxième type are not deletions; the leader attaches the addition before d’extensions. Tiny isolated dots near XB and before the second N have no secure role as punctuation or mathematical signs and are not promoted to text. "
"Scope of checks: this is visual transcription and comparison only. No claim about existence, uniqueness or specialization of profinite splittings has been proved or used as a mathematical certificate here. The wording’s conditions and formulas were read as written, with no theorem-based repair. H’s uncertainty around analogue was settled as a readable common word on the supplied lower half; it does not produce a lexical collation row.")
report=dict(scan=95,line_count=20,changes=changes,marks=marks,inventory=inventory,second_boxes=second,notes=notes,check_events=[],hand_observations=[
 dict(habit='Low connected runs can compress several letters, while a terminal return can resemble a separate s or comma.',pages=[95],evidence='The article before classes, the small final loop of classes, the g-e ending and detached glyph of scindages, and donc/du are treated separately rather than regularized by agreement.',witness_errors='C and H differ on article/number and punctuation; some local alternatives remain unresolved.'),
 dict(habit='A straight downward stem with a short shoulder may look r-like even where vee is expected.',pages=[95],evidence='First conormal superscript above N_Dalpha,S; complete formula crop.',witness_errors='H prints vee certainly; C’s r|vee doubt is retained.'),
 dict(habit='Raised additions can be written on more than one small tier, crossed by descenders from the ordinary line above.',pages=[95],evidence='The qui intervient parenthesis and its quotient; pt gén. descenders cross the small verb and q crosses the denominator.',witness_errors='H loses the denominator and the insertion state; C supplies dans where no word is written.'),
 dict(habit='The local comma has a hooked or diagonal tail; a full stop can be a small closed round blob.',pages=[95],evidence='s_alpha and question versus final inversible.',witness_errors='Both witnesses print full stops at s_alpha and question.'),
 dict(habit='Accents are not supplied from normal spelling.',pages=[95],evidence='The brulant crop includes blank space above u and the b/l ascender height, without a circumflex.',witness_errors='C normalizes brûlant; H substitutes mineur.'),
 dict(habit='An attachment leader is a long curve returning to a precise main-line gap.',pages=[95],evidence='de deuxième type has a curve returning before d’extensions.',witness_errors='H attaches the type phrase after d’extensions and relocates de groupes profinis.')],notation_additions=[],abbreviations=[
 dict(form='vois.',expansion='voisinage'),dict(form='pt',expansion='point'),dict(form='pts',expansion='points'),dict(form='gén.',expansion='générique in pt gén.; the cancelled plus gén. may abbreviate plus généralement'),dict(form='i.e.',expansion='id est')],unresolved=unresolved,diff_coverage=[dict(diff_id=k,disposition=v[0],change_place=v[1]) for k,v in coverage.items()])
# Use source macros, without editorial typographic placeholders in actual readings.
for ch in changes:
 ch['final']=ch['final'].replace(r'qu\textquoteright',"qu'").replace(r'd\textquoteright extensions',"d'extensions")
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
draft=r'''\scanpage{95}
\mspage{47}
qui nous incite justement \unsure{à|:} regarder \unsure{les|la} classes de scindages\unsure{,} de $\mathcal E_{X_B}$ sur $\mathcal E_{k(s)}$ relatifs à cet $L_i$ --- et notamment ceux relatifs au choix d'un uniformisant de $\mathcal O_{S,s_\alpha}$, i.e. d'une équation locale de $D_\alpha$ au vois. de son pt gén. $s_\alpha$, \deleted{\unsure{(plus gén.)}} \inserted{(qui intervient par le \unsure{biais|bout} qu'\unsure{elles définissent|elle définit} $\mathfrak m_{s_\alpha}/\mathfrak m_{s_\alpha}^{2}$)} Quant à ces sections-là, on voit comment elles se spécialisent, du moins c'est clair en les pts de $D_\alpha$ en lesquels la section rationnelle envisagée du faisceau conormal $\underline N_{D_\alpha,S}^{\unsure{r|\vee}}$ (si on suppose $D_\alpha$ régulier, \& \unsure{donc|du} $\underline N_{D_\alpha/S}$ inversible) reste régulière, et inversible.

On peut se proposer d'étudier \deleted{comment} \inserted{ce qui} se passe en les autres points --- i.e. la spécialisation des sections \inserted{de deuxième type} d'extensions de groupes profinis, en faisant une étude analogue à la précédente, pour cette question, Mais cela me semble \deleted{moins} \inserted{d'un} intérêt moins brulant --- car cela n'est
\margin{94}
'''
(p/'draft.tex').write_text(draft)
print(json.dumps({k:len(report[k]) for k in ['changes','marks','inventory','second_boxes','unresolved','diff_coverage']},ensure_ascii=False))
