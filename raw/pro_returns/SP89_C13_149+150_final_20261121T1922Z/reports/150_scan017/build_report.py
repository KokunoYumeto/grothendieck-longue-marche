from pathlib import Path
import csv,json,re

ROOT=Path('/workspace/scratch/8759b8008681')
PAGE='150_scan017'
OUT=ROOT/'work/reports'/PAGE
C=(ROOT/'packets'/PAGE/'C.tex').read_text()
H=(ROOT/'packets'/PAGE/'H.tex').read_text()
D=(OUT/'draft.tex').read_text()
BOX=json.loads((OUT/'crop_boxes.json').read_text())

def between(s,a,b):
    i=s.index(a); j=s.index(b,i)+len(b)
    return s[i:j]
def macro(s,a):
    i=s.index(a); j=s.index('{',i); n=1; k=j+1
    while n:
        n+=(s[k]=='{')-(s[k]=='}'); k+=1
    return s[i:k]
def norm(s): return re.sub(r'\s+',' ',s).strip()

dia_c=between(C,r'\begin{tikzcd}',r'\end{tikzcd}')
dia_h=between(H,r'\begin{tikzcd}',r'\end{tikzcd}')
dia_d=between(D,r'\begin{tikzcd}',r'\end{tikzcd}')
short_c=macro(C,r'\margin{plutôt')
short_d=macro(D,r'\margin{plutot')
long_c=macro(C,r'\margin{Cela')
long_h=macro(H,r'\marginal{Il')
long_d=macro(D,r'\margin{Cela')
old_formula_d=between(D,r"X'\cap E\simeq B'",r'\{0,\varepsilon\}}')

R=dict(page=PAGE,reader='reader_b',line_count=len(D.splitlines()),changes=[],decisions=[],
       inventory=[],audit_boxes=[],doubts=[],notes=[],check_events=[],notation=[],
       abbreviations=[],hand=[],diff_coverage=[],deletion_insertion_review=[])

def change(id,p,place,c,h,final,evidence,confidence='high',kind='misread word',
           against_c=True,against_h=True,marked_in_h=False,consequential=False,error_category='2'):
    R['changes'].append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,
        crop=f'crops/{PAGE}_{p}.png',box=BOX[p],confidence=confidence,kind=kind,
        against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,
        consequential=consequential,error_category=error_category))

change('P01','P01','Whole commutative diagram and its vertical identification',dia_c,dia_h,dia_d,
       'Three objects were counted twice: dot T, E, and dot T×[0,1]. There are two directed shafts, two terminal heads and one hook. The horizontal arrow has a left hook and right head; the diagonal has a down-right terminal head. The dark mid-diagonal notch joins the closing parenthesis of (t,0), rather than forming a separately identifiable extra head. Between E and the product is a long straight upright on the left and a smaller curved upright on its right, without a lower head. C rotates this into a horizontal simeq label; H draws a directed down-arrow carrying wr. The draft preserves the vertical two-stroke identification as vert then wr, without an arrow shaft.',
       kind='drawing or diagram',consequential=True,error_category='4')
change('P02a','P02','First words below the diagram','et tel que','il faut que','et tel que',
       'The first group has the low e turn and tall t. The next has t, low e and a tall final l; it is only tel, not the longer faut. The following que has its own q descender and low u/e joins.',against_c=False)
change('P02b','P02','Decorated X in the whole intersection formula',r"X'{}^*\cap E",r"X'^{*}\cap E",r"X'_{\unsure{*|\varepsilon}}\cap E",
       'A separate prime is above/right of X. The smaller branched mark lies below that prime, at the low right of the X body. Its short left branches and upper diagonal favor a star; an epsilon-like compact form remains possible. Both witnesses raise the mark as an exponent, which its physical placement does not support. No separately recoverable earlier X* is duplicated from H’s editorial chronology.',
       confidence='medium',kind='misread symbol or index',marked_in_h=True,consequential=True,error_category='1')
change('P03','P03','partie bord stricte','partie bord stricte','partie bordante stricte','partie bord stricte',
       'The b has a tall stem and lower loop, o is small/filled, r is a low run, and the final d has a separate high return. A broad gap follows d before stricte; there are no a-n-t-e bodies. The source’s short adjectival wording is retained.',against_c=False)
change('P04','P04','Cancelled absolu de and raised replacement de',
       r'\deleted{\unsure{absolu de}}\inserted{de}',r'\struck{\ill{} de} \add{de}',
       r'\deleted{\unsure{absolu de}}\inserted{de}',
       'The old first word has a rounded initial body, a tall inner loop and low joins under a heavy horizontal strike; not every letter of absolu can be isolated. Its following de is also crossed. The replacement de stands above, with a clear d loop/ascender and low e return. Keep the proposed old phrase doubtful against H’s unreadable first word.',
       confidence='low',kind='other',against_c=False,marked_in_h=True,error_category='7')
change('P05','P05','X prime dans X, with the raised fermée',
       r"$X'$ \unsure{dans|de} $X$",r"$X'$ de $X$",r"$X'$ dans $X$",
       'The word has a closed d loop and tall stem, then a cramped but distinct a-n-s group with a final up/down turn. It is longer than de. This resolves C M0338 to its first candidate. Above it, fermée has a separate raised baseline and curved insertion leader after partie; the leader is not an opening parenthesis around X prime.',
       consequential=True)
change('P06a','P06','Overwritten letter in avec E',r'avec $E$',r'avec $E$',r'avec $\deleted{\unsure{B}}E$',
       'Inside the E are a narrow upper curved body and a lower rounded/angled return beneath its heavier horizontal arms, compatible with an earlier B. The neighbouring q descender from qu’une reaches the top area but does not explain both inner returns. The prior B remains doubtful here; the live E is clear. Both witnesses omit the visible prior layer.',
       confidence='medium',kind='omission',error_category='3')
change('P06b','P06','Abbreviation at the end of the explanatory line',"l'homéom.","l'homéomorphisme","l'homéom.",
       'After l apostrophe the h stem, o/m joins, accented e, o and final low m are visible, followed by a distinct dark stop. No r-p-h-i-s-m-e continuation is present. Preserve the written abbreviation.',
       kind='abbreviation expanded or spelling modernised',against_c=False,error_category='8')
change('P07a','P07','Overwritten B beneath the E of the product formula',r'E\simeq B\times[0,1]',r'E\simeq B\times[0,1]',r'\deleted{B}E\simeq B\times[0,1]',
       'The earlier letter has two distinct right-hand bowls: a small closed upper loop under the E roof and a larger lower bowl returning to the left stem. Three heavier horizontal E arms cross these thinner curves. Unlike the less secure prose occurrence P06, both B bowls are recoverable here. The live letter is ordinary E, not a separately bold alphabet.',
       kind='omission',error_category='3')
change('P07b','P07','Isolated dash after the product formula',r'\qquad -','(nothing)',r'\qquad -',
       'At the far right of the formula line is a separate short horizontal dash. It is not a dot or paper mark. C retains it; H omits it.',kind='omission',against_c=False,error_category='3')
change('P08','P08','Parenthetical necessity and B prime identity',
       r"(où néc$^t$. on a $B'=X'\cap B$).",r"($\ldots$ $B'=X'\cap B$).",
       r"(où néc$^t$. on a $B'=X'\cap B$).",
       'Before the formula are the compressed où with its raised accent, the n-é-c group, a clearly raised crossed t, a baseline stop, and the three short on a bodies. H’s ellipsis suppresses readable ink. B prime and X prime have separate prime strokes, the relation is an intersection, and the closing parenthesis and following period are distinct. Oblique lettering above belongs to the margin note and is excluded.',
       confidence='medium',kind=r'readable ink left as \ill{}',against_c=False,error_category='5')
change('P09','P09','Complete short slanted marginal recommendation',short_c,
       r'on lit aussi, plus haut, « \uncertain{transversal} ».',short_d,
       'The opening word reads plutot: p descender, looped l, low u, two tall t stems and a small o-like body, with no independent circumflex above that o. Two separate dots form the colon. Transversale ends with a tall l and an e return and has one separate underline. The final punctuation has a tapering upright plus detached lower dot, without the curved upper hook of a question mark; M0339 is resolved to the alternative !. The lower oblique fragments outside the note are main-text context.',
       kind='other',marked_in_h=True,error_category='10')
change('P10','P10','Complete long slanted marginal implication',long_c,long_h,long_d,
       'Cela starts with a broad C, low e and looped l/a ending. Implique has the dotted i, p and q descenders and intervening l loop; donc begins with a d loop and ends in a small c. The next line has que, B∩X prime, est and un. The following line has sous, a separate hyphen, espace with a p descender, then bord and de; the final X prime is on its own lower continuation. No separate terminal stop follows that X prime. H’s Il importe ... soit reconstruction is not supported; C’s final period is also omitted.',
       confidence='medium',kind=r'readable ink left as \ill{}',marked_in_h=True,consequential=True,error_category='5')
change('P11','P11','Opening quotation and replacement transversalité at the edge',
       r'``\deleted{compatibilité}\inserted{transversalité}',
       r'« \struck{compatibilité} \add{\uncertain{transversalité}}',
       r'``\deleted{\unsure{compatibilité}}\inserted{\unsure{transversalité}}',
       'The opening quote is two separate short ticks before the old line, not a guillemet. The lower compatibilité is crossed by a continuous strike; its middle is too covered to newly certify each letter. The replacement is raised, with recognizable transversali-t bodies, but its final group meets the clipped physical edge. Both proposed words remain locally doubtful; this added uncertainty alone is not counted against C.',
       confidence='medium',kind='other',against_c=False,marked_in_h=True,error_category='10')
change('P12','P12','Cancelled dans le cas, closing quotation, and n’est pas underline',
       r"\deleted{dans le cas} cylindrique'' \uline{n'est pas}",
       r"\struck{dans le cas} cylindrique » n'est pas",
       r"\deleted{dans le cas} cylindrique'' \uline{n'est pas}",
       'The old phrase has its own continuous strike, with d and l ascenders and the three word groups below it. Cylindrique is live, its y/q descenders extending below; two high closing ticks follow it. A separate long underline runs under n’est pas; the p descender crosses that underline but does not cancel the words.',
       kind='other',against_c=False,error_category='10')
change('P13a','P13','dans la before the short crossed word','celle dans la','celle dans le','celle dans la',
       'The article after dans has a tall looped l and a rounded a body/return at its foot, rather than a final open e. Preserve la even though the surrounding revision produces awkward syntax.',against_c=False)
change('P13b','P13','Accent on cônique','conique,','conique,','cônique,',
       'A short detached arch lies immediately above the o and below the larger insertion leader. It is independent of both the letter body and the leader; the source therefore has cônique. Both witnesses omit this visible accent.',
       kind='abbreviation expanded or spelling modernised',error_category='8')
change('P13c','P13','Live underlined mais est',r'\uline{mais est}',
       r'\struck{\ill{}} \add{\uncertain{mais en}}',r'\uline{mais est}',
       'The low m/a/i/s bodies are followed by e, the s turn and a tall final t, giving est rather than en. A separate horizontal underline lies below the phrase. No cancellation crosses either word and no separate old phrase is recoverable there; H’s deleted/inserted reconstruction is not supported.',
       kind='deletion state (struck given live or live given struck)',against_c=False,marked_in_h=True,error_category='7')
change('P14a','P14','plus exigeant(e) and the separately crossed que',
       r'\unsure{plus|bien} exigeante \deleted{\unsure{que}}',
       r'\struck{\ill{} exigeant que \ill{}} \add{\uncertain{bien exigeant}}',
       r'plus \unsure{exigeante|exigeant} \deleted{\unsure{que}}',
       'Plus has a deep p descender, tall looped l and the low u/s joins, resolving M0340 to its first candidate rather than bien. Exigeant(e) is live: e/x/i are separate, g has a full loop and a long descending return, and the ending t meets a crowded following group. A separate final e cannot be certified, so both exigeante and exigeant remain. The following que-like group is crossed on its own lower body; its full letters are not secure. H’s additional cancelled exigeant phrase duplicates live ink.',
       confidence='medium',kind='deletion state (struck given live or live given struck)',marked_in_h=True,consequential=True,error_category='7')
change('P14b','P14','Crossed introduction before the cancelled formula',r'dans ce cas',r'\struck{\uncertain{\ill{}}}',r'\unsure{dans ce cas}',
       'The lower line has a looped initial d and several low joined groups under the long strike. The proposed dans ce cas fits those surviving bodies, but the middle and ending are too obscured to isolate every letter. The uncertainty is retained against H’s unreadable old phrase; no grammatical completion is used.',
       confidence='low',kind='other',against_c=False,marked_in_h=True,error_category='7')
change('P15','P15','End of the inserted comparison clause',
       r'correspond au cas où on \unsure{lui demandait|\ldots\ devait}',
       r'\uncertain{correspond} au cas où on \uncertain{\ill{}} devait',
       r'correspond au cas où on \unsure{lui} devait',
       'Correspond has its descending p and final tall d; au cas où on is spaced in separate small groups, with an accent above où. The final verb has d loop/stem, e, one v, a, dotted i and crossed t, giving devait; there are no m/n bodies for demandait. Before it the proposed lui intersects the descending q from cônique above and contains a tiny low dot/short return, so that pronoun/remnant remains uncertain. M0341 is an other reading with a resolved verb but unresolved pronoun.',
       confidence='medium',marked_in_h=True,consequential=True)
change('P16','P16','Terminal group of the whole cancelled formula',
       r"X'\cap E\simeq B'\times[0,1]\cup"+'\n'+r'B\times\{0\}\unsure{\varepsilon}',
       r"X'\cap E\simeq B'\times[0,1]\cup B\times\lbrace0\rbrace",
       old_formula_d,
       'The whole X-prime intersection formula is under one long strike. Its E is recoverable but visibly retraced; no earlier glyph is identified. After B×, an initial {0}-like group is followed by an epsilon-like dark cluster and a further tall closing-brace return. The draft keeps alternatives {0} epsilon } and {0,epsilon}, without discarding the extra return or normalizing the expression to an expected set. Both interval brackets and the preceding union are retained.',
       confidence='low',kind='misread symbol or index',marked_in_h=True,consequential=True,error_category='1')
change('P17a','P17','Written abbreviation de =','de $=$','de même','de $=$',
       'After de are two independent near-horizontal strokes, the upper shorter and the lower longer. There are no letter bodies for même. This is the author’s written equals-sign abbreviation, retained without expansion.',
       kind='abbreviation expanded or spelling modernised',against_c=False,error_category='8')
change('P17b','P17','Cancelled de before parties',r'\deleted{\unsure{de}}',r'\struck{de}',r'\deleted{de}',
       'The old d has a small lower loop and a tall looped ascender, and the e has a distinct low return to its right. The independent crossing strokes do not hide both complete letter bodies. This resolves the C doubt inside the deletion, although that doubt is not one of the four packet mark IDs.',against_h=False)
change('P18','P18','Thin lower-left foliation',r'\margin{16}','(nothing)',r'\margin{16}',
       'The first thin digit is 1 with an oblique approach; the second has a descending curved upper stroke and a closed lower bowl, giving 6. The weight and small size differ from the main text. The digits are retained as 16, with hand attribution uncertain.',kind='omission',against_c=False,error_category='3')

def decision(id,p,which,reading,evidence,confidence):
    R['decisions'].append(dict(id=id,cote='150',scan='17',decision=which,reading=reading,
        evidence=evidence,crop=f'crops/{PAGE}_{p}.png',box=BOX[p],confidence=confidence))
decision('M0338','P05','first','dans','Tall d loop/stem is followed by cramped but distinct a-n-s bodies, longer than the alternative de.','high')
decision('M0339','P09','alternative','!','A short tapering upright is followed below by one detached dot; there is no upper question-mark hook.','high')
decision('M0340','P14','first','plus','The initial p descender and looped l are distinct before the low u/s joins; bien would require a different first two letters.','high')
decision('M0341','P15','other',r'\unsure{lui} devait','Devait is separable as d/e/v/a/i/t, without the m/n sequence of demandait. The pronoun overlaps the q descender from above and a small remnant remains, so the phrase is not wholly resolved.','medium')

def inv(kind,pos,content,hand='his hand'):
    R['inventory'].append(dict(scan=PAGE,sheet_kind='text',hand=hand,
       element=f'E{len(R["inventory"])+1:02d}',kind=kind,position=pos,
       first_words_or_objects=content,transcribed='yes'))
inv('display','Top, P00',r'(13) E\simeq\dot T\times[0,1]')
inv('text','Below formula (13), upper native half','rendant commutatif')
inv('diagram','Upper middle, P01',dia_d)
inv('text','First paragraph below diagram, P02 and upper native half',r"et tel que X'_{\unsure{*|\varepsilon}}\cap E ... partie fermée de dot T")
inv('text','Second paragraph opening, P03–P08','Soit B une partie bord stricte ... définition de compatible avec E')
inv('deletion','After cylindrique E, P04',r'\deleted{\unsure{absolu de}}')
inv('insertion','Above old de, P04',r'\inserted{de}')
inv('insertion','After partie, above X prime, P05',r'\inserted{fermée}')
inv('deletion','Overwritten prior letter in avec E, P06',r'\deleted{\unsure{B}}E')
inv('display','Unnumbered product formula, P07',r'\deleted{B}E\simeq B\times[0,1]\qquad -')
inv('deletion','Under the E of that formula, P07',r'\deleted{B}')
inv('text','Product-subset condition and necessity parenthesis, P08 and lower half',r"si X'\cap E s’identifie à B'×[0,1] (où néc^t. on a B'=X'\cap B).")
inv('margin note','Short slanted left note, P09',short_d)
inv('margin note','Long slanted left note, P10',long_d)
inv('text','Lower comparison paragraph, P11–P16','On fera attention que ... n’est pas ... cônique, mais est ...')
inv('deletion','Before cylindrique, at right edge, P11',r'\deleted{\unsure{compatibilité}}')
inv('insertion','Above that cancelled word, at right edge, P11',r'\inserted{\unsure{transversalité}}')
inv('deletion','Before live cylindrique, P12',r'\deleted{dans le cas}')
inv('deletion','After dans la, P13',r'\deleted{\unsure{cas|en}}')
inv('insertion','Above the short crossed word before cônique, P13',r'\inserted{compatibilité}')
inv('insertion','Crowded revision above old last line, P14–P15',r'plus \unsure{exigeante|exigeant} \deleted{\unsure{que}} : correspond au cas où on \unsure{lui} devait')
inv('deletion','Inside that revision, P14',r'\deleted{\unsure{que}}')
inv('insertion','Small formula below plus/exigeant(e), P14',r"T'\cap Y=0.\dot T'")
inv('deletion','Whole old last line, P14/P16',r'\unsure{dans ce cas} '+old_formula_d)
inv('text','Final paragraph, P17','On définit de = la compatibilité pour une famille ... parties ...')
inv('deletion','Between famille and parties, P17',r'\deleted{finie} \deleted{de}')
inv('margin note','Thin lower-left number, P18',r'\margin{16}','uncertain hand')

def audit(id,kind,xy,reading): R['audit_boxes'].append(dict(box=id,kind=kind,xyxy=xy,reading=reading))
audit('B00','handwritten number',BOX['P00'],r'(13)\qquad E\simeq\dot T\times[0,1]')
audit('B01','doubtful formula; handwritten number',BOX['P01'],dia_d)
audit('B02','doubtful formula; C/H different words; less than high confidence departure',BOX['P02'],r"et tel que $X'_{\unsure{*|\varepsilon}}\cap E$ s’identifie à une partie")
audit('B03','handwritten number',[272,603,1584,788],r"de $\dot T\times[0,1]$ de la forme $X'_0\times[0,1]$, où $X'_0$ est une partie fermée de $\dot T$.")
audit('B04','C/H different words',BOX['P03'],'bord stricte')
audit('B05','struck passage; insertion; C/H different words; less than high confidence departure',BOX['P04'],r'\deleted{\unsure{absolu de}}\inserted{de}')
audit('B06','insertion; C/H different words',[753,1085,1305,1222],r"partie \inserted{fermée} $X'$ dans $X$")
audit('B07','struck passage; doubtful formula; C/H different words; less than high confidence departure',BOX['P06'],r"$\deleted{\unsure{B}}E$ --- i.e. avec l'homéom.")
audit('B08','struck passage; handwritten number',BOX['P07'],r'\deleted{B}E\simeq B\times[0,1]\qquad -')
audit('B09','handwritten number',[270,1494,1590,1587],r"si $X'\cap E$ s’identifie à $B'\times[0,1]$")
audit('B10','C/H different words; less than high confidence departure',BOX['P08'],r"(où néc$^t$. on a $B'=X'\cap B$).")
audit('B11','margin note; C/H different words',BOX['P09'],short_d)
audit('B12','margin note; C/H different words; less than high confidence departure',BOX['P10'],long_d)
audit('B13','struck passage; insertion; C/H different words; less than high confidence departure',BOX['P11'],r'``\deleted{\unsure{compatibilité}}\inserted{\unsure{transversalité}}')
audit('B14','struck passage; C/H different words',BOX['P12'],r"\deleted{dans le cas} cylindrique'' \uline{n'est pas}")
audit('B15','struck passage; insertion; C/H different words; less than high confidence departure',BOX['P13'],r'particulier de celle dans la \deleted{\unsure{cas|en}}\inserted{compatibilité} cônique, \uline{mais est}')
audit('B16','insertion; struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',BOX['P14'],r"plus \unsure{exigeante|exigeant} \deleted{\unsure{que}} :\quad T'\cap Y=0.\dot T'\quad\deleted{\unsure{dans ce cas}}")
audit('B17','insertion; C/H different words; less than high confidence departure',BOX['P15'],r'correspond au cas où on \unsure{lui} devait')
audit('B18','struck passage; doubtful formula; handwritten number; less than high confidence departure',[774,2045,1681,2177],r'\deleted{'+old_formula_d+'}')
audit('B19','struck passage; doubtful formula; C/H different words',BOX['P17'],between(D,'On définit de',r'$(X_i)_{i\in I}$.'))
audit('B20','margin note; handwritten number',BOX['P18'],'16')

def doubt(place,reading,alts,reason,confidence='low'):
    R['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,reason=reason))
doubt('P02 low mark beside X prime',r"X'_{\unsure{*|\varepsilon}}",'star | epsilon-like mark','Prime is independently high; the branched mark lies low. Star is favored by the short branches, but its compact body does not exclude epsilon.','medium')
doubt('P04 old absolu de',r'\deleted{\unsure{absolu de}}','absolu de; no full alternative recovered','Heavy strike covers the low joins and part of the tall inner body; no full clean resolution is claimed.')
doubt('P06 prior B under E',r'\deleted{\unsure{B}}E','earlier B-like body; mere retracing not wholly excluded','Inner upper curve and lower return suggest B, but the nearby q descender and heavy E strokes make this less secure than P07.','medium')
doubt('P11 cancelled compatibilité',r'\deleted{\unsure{compatibilité}}','compatibilité','The middle bodies are under a heavy strike and the ending meets the physical edge; this newly added doubt does not alter C’s candidate.')
doubt('P11 replacement at the physical edge',r'\inserted{\unsure{transversalité}}','transversalité, clipped final group','Recognizable raised transversali-t sequence reaches the clipped edge; no unseen complete final letter is supplied.','medium')
doubt('P13 short crossed token',r'\deleted{\unsure{cas|en}}','cas | en','Only a small opening loop and low run survive under the short strike; neither whole candidate is independently secure.')
doubt('P14 adjective ending',r'\unsure{exigeante|exigeant}','exigeante | exigeant','Final t meets a crowded following group and a separate final e cannot be isolated; grammatical agreement does not settle it.','medium')
doubt('P14 cancelled que',r'\deleted{\unsure{que}}','que','The descending q-like component and low crossed body remain, but all three letters are not separate.')
doubt('P14 old introduction',r'\deleted{\unsure{dans ce cas}}','dans ce cas','Surviving lower loops support the candidate, while the continuous strike masks the central/last word bodies.')
doubt('P15 pronoun/remnant before devait',r'\unsure{lui} devait','lui; unresolved low trailing remnant','The region intersects the q descender from cônique above and includes a tiny low dot/short return. The final verb itself is readable as devait.','medium')
doubt('P16 retraced E',r'E','No prior glyph recovered','E is the recoverable letter. The inner small roof/stem-like strokes and dark point do not securely identify a preceding T, B or other character; no invented prior symbol is transcribed.','medium')
doubt('P16 terminal group',r'\unsure{\{0\}\varepsilon\}|\{0,\varepsilon\}}',r'\{0\}\varepsilon\} | \{0,\varepsilon\}','An initial {0}-like group is followed by an epsilon-like cluster and another tall brace-like return. Segmentation is undecided under the strike; the extra return is retained.')

R['notes']=[
 {'id':'N01','text':'Source report: the page begins with (13), E identified with dot T×[0,1], and a commutative diagram fixing the copy of dot T at parameter zero. It then gives the product condition for a closed X prime to be called compatible with a cylindrical neighbourhood E of B. A marginal correction proposes “plutot : transversale !”. The later cylindrical/conical comparison is heavily revised, and the final paragraph removes finie from the family formulation. This report of content is not itself a mathematical proof.'},
 {'id':'N02','text':'Targeted proof check supplied by the main reader and rechecked here: restrict the given product collar h:E→B×[0,1] to E∩X prime. The stated compatibility condition identifies this restriction with B prime×[0,1]. Since h sends the embedded B to B×{0}, taking the zero slice gives (B∩X prime)×{0}=B prime×{0}, hence B prime=B∩X prime. Moreover, E∩X prime is a neighbourhood of B∩X prime in the subspace X prime because E is a neighbourhood of B in X. The restricted product identification therefore gives the claimed bord structure on B∩X prime inside X prime. Closedness of X prime implies that its intersection with B is closed in B. This is an actual product/restriction check, separate from reading the marginal words.'},
 {'id':'N03','text':'The source emphasizes that cylindrical “transversalité” “n’est pas” a special case of the conical comparison but “mais est” followed by the revised plus exigeant(e) clause. Its added condition is T prime∩Y=0.dot T prime. The exact earlier conical definition is not supplied afresh on this assigned leaf. No independent proof of the full cylindrical/conical comparison is claimed, and mathematical expectation does not resolve exigeante/exigeant, the pronoun before devait, or the struck terminal set-like group.'},
 {'id':'N04','text':'The initial decorated X has a clear upper prime and a second, low branched mark. The transcription keeps that second mark as a subscript with star/epsilon alternatives; its use is not defined on this leaf. H’s editorial claim of an earlier X* does not establish a separately recoverable cancelled copy, so none is duplicated.'},
 {'id':'N05','text':'Two local overwriting layers are distinguished. In the product formula the thinner upper and lower B bowls remain under the heavy E arms, so deleted B followed by E is recorded. In the preceding prose E the B-like old body is less secure and remains doubtful. This is not a global change of font. In the later cancelled formula E is retraced but no preceding glyph is recoverable; no earlier T or other letter is supplied there.'},
 {'id':'N06','text':'The curved stroke under 0.dot T prime is continuous with the descending g of exigeant(e) above. It is not treated as an independent box or underline, despite H’s editorial “entouré”. Likewise, insertion leaders near fermée and compatibilité are separated from parentheses and cancellations. The live adjective and mais est are not duplicated into additional crossed passages.'},
 {'id':'N07','text':'Literal forms retained include bord rather than bordante, homéom. rather than its expansion, néc with raised t and a baseline stop, plutot without an independently visible circumflex, cônique with its visible arch over o, and de = as the written abbreviation for de même. The final grammar after deleting finie and de is left as written; no extra de is restored.'},
 {'id':'N08','text':'The diagram has three objects, two directed shafts, two terminal heads and one hook, plus two independent strokes of a vertical identification. These components were counted twice. The mid-diagonal notch is continuous with the closing parenthesis of (t,0); it is not reproduced as another arrowhead. No arrowhead is added to the vertical straight stroke.'},
 {'id':'N09','text':'Reading record: only this assigned page, its C/H packet, current notation, preamble and governing protocol were used. The original was viewed once, both prepared native halves once, and P00–P18 once each. P09 and P10 were rotated for their slanted notes; original boxes and rotations are saved. Root independently reviewed all 19 crops. No OCR, recognition library, outside research, compilation, other-page report or other-page image was used.'},
 {'id':'N10','text':'There is no author folio number visible at the head. The thin lower-left 16 is separately retained with uncertain hand attribution. The terminal stop after the long marginal note’s final X prime is not visible and is omitted; the final main-text family sentence does have its own distinct stop. Physical clipping at the right edge is not silently completed.'}
]
R['check_events']=[
 {'statement_id':PAGE+'.N01','type':'carried as background without fault found','outcome':'Contents read visually and collated; no proof is inferred merely from successful transcription.'},
 {'statement_id':PAGE+'.N02','type':'targeted proof check','outcome':'Main reader supplied the collar-restriction argument; reader B rechecked the zero-slice identity B prime=B∩X prime, the relative-neighbourhood property, and the restricted product identification.'},
 {'statement_id':PAGE+'.N03','type':'carried as background without fault found','outcome':'The broader cylindrical/conical comparison is reported as the source’s claim; no independent theorem verification is claimed from this leaf alone.'}
]
R['notation']=[
 {'form':r'E\simeq\dot T\times[0,1]','meaning':'Product identification numbered (13)','evidence':'P00 and the accompanying three-object diagram P01.'},
 {'form':r'\vert\!\wr','meaning':'Vertical identification, straight upright on the left and curved upright on the right','evidence':'P01: two separate strokes, no downward head; their left/right order is confirmed locally.'},
 {'form':r"X'_{\unsure{*|\varepsilon}}",'meaning':'Decorated X prime in the first product-subset condition; the low mark is not defined here','evidence':'P02: independent high prime and low right branched/star-or-epsilon group.'},
 {'form':r"X'_0",'meaning':'Closed subset of dot T whose product describes the first intersection','evidence':'Upper native half: both occurrences have a separate prime and lowered round zero.'},
 {'form':r"B'=X'\cap B",'meaning':'Boundary part induced on X prime by the product condition','evidence':'P08 gives the identity inside the necessity parenthesis.'},
 {'form':r"T'\cap Y=0.\dot T'",'meaning':'Added condition in the cylindrical/conical comparison','evidence':'P14: both T primes, Y, zero and dot are separate; the apparent lower enclosure is the g descender.'},
 {'form':'= in de =','meaning':'Written abbreviation for même','evidence':'P17: two separate near-horizontal strokes after de.'}
]
R['abbreviations']=[
 {'form':'vois.','expansion':'voisinage'}, {'form':'homéom.','expansion':'homéomorphisme'},
 {'form':'i.e.','expansion':'id est'}, {'form':r'néc$^t$.','expansion':'nécessairement'},
 {'form':'de =','expansion':'de même'}
]
R['hand']=[
 {'habit':'A letter’s descender or an insertion leader may resemble an enclosure or cancellation.','places':'150_scan017 P01 parenthesis/diagonal, P05 fermée leader, P13 compatibilité leader, P14 g descender.','consistency':'Each path was attached to its originating letter or insertion before assigning revision state; no general rule is imposed without local tracing.','witness_errors':'H calls the inserted formula entouré and reconstructs extra deleted/inserted words; the mid-diagonal notch could also be mistaken for an extra head.'},
 {'habit':'An earlier B can remain as thin loops beneath a heavier E.','places':'150_scan017 P06/P07.','consistency':'Both bowls are clear in P07; the prose occurrence remains doubtful, and the later retraced E has no identified prior letter.','witness_errors':'Both witnesses omit the recoverable P07 old B and the doubtful P06 prior layer.'},
 {'habit':'Low/right decorations must be distinguished from a separate high prime.','places':'150_scan017 P02.','consistency':'One local occurrence; low placement is clear while star/epsilon identity is unresolved.','witness_errors':'Both witnesses set the small mark as a raised star.'},
 {'habit':'Short written words and abbreviations may be expanded by a reader from familiar terminology.','places':'150_scan017 P03 bord, P06 homéom., P08 néc^t., P17 de =.','consistency':'Endings and independent stops were checked from the saved crops.','witness_errors':'H expands bord to bordante, homéom. to homéomorphisme, and = to même, while suppressing the parenthetical short words.'},
 {'habit':'Accents are locally variable and independent small strokes matter.','places':'150_scan017 P09 plutot and P13 cônique.','consistency':'No circumflex can be isolated above plutot; an independent arch is visible over the o of cônique.','witness_errors':'C regularizes plutot to plutôt; both witnesses omit the arch in cônique.'}
]
coverage={
1:'H continuation note is editorial, not source. No author folio is visible; scanpage17 is archive metadata.',
2:'Diagram/display wrappers are macro-only; P01 records the actual geometry.',
3:'P01: literal straight-left/curved-right vertical identification, not horizontal simeq.',
4:'P01: no directed down-arrow; retain the two independent vertical strokes without a head.',
5:'P02a: et tel que, not il faut que.',
6:'P02b: low mark under the separate prime; H editorial chronology does not justify a duplicated earlier X*.',
7:'P03: short bord, no ante ending.',
8:'P04: old absolu de remains a doubtful candidate against H unreadable word; raised replacement de clear.',
9:'P05: dans resolves M0338 first, against H de.',
10:'Different TeX dash lengths alone do not make a lexical change; one source dash precedes i.e.',
11:'P06b: homéom. retained with its stop, not expanded.',
12:'P07b: separate far-right dash retained.',
13:'P08: où néc with raised t, stop, on a are readable and retained.',
14:'P09/P10: both marginal notes restored completely; ! resolves M0339, plutot lacks a separate circumflex, long note ends without a stop.',
15:'P11: two opening quotation ticks, not guillemet; crossed/raised words retained with local edge doubts.',
16:'P12: live cylindrique followed by two closing quotation ticks.',
17:'P13a: literal dans la, not dans le.',
18:'Short crossed cas|en remains doubtful; H cas agrees with the first candidate, so added certainty differences alone remain in doubts. The raised compatibilité and its leader are inventoried.',
19:'P13c/P14a: live underlined mais est; plus resolves M0340; H extra revision reconstruction not supported.',
20:'P14a: exigeante|exigeant remains unresolved; que is separately crossed and doubtful.',
21:'P15: verb devait resolved, pronoun lui remains doubtful; M0341 other, not a clean first or second phrase.',
22:'P14b/P15: new formula attaches to the inserted comparison; old dans ce cas stays crossed/doubtful. Formula itself is readable without a separate box.',
23:'P16 preserves the unresolved terminal epsilon/brace group; H explanatory prose is excluded. P09/P10 give the actual two notes. No missing closing brace or phrase is normalized by context.',
24:'P17a: literal de =, not expanded de même.',
25:'P18: thin16 retained with uncertain hand attribution.'
}
R['diff_coverage']=[dict(row=i,disposition=coverage[i]) for i in range(1,26)]

def rev(text,scope,evidence): R['deletion_insertion_review'].append(dict(text=text,scope_attachment=scope,evidence=evidence))
rev(r'\deleted{\unsure{absolu de}}\inserted{de}','Whole old phrase after cylindrique E; raised de replaces its preposition before B.','P04: old line crosses both groups; replacement de is on a higher baseline.')
rev(r'\inserted{fermée}','After partie, before X prime.','P05: curved leader turns down toward the insertion site; it is not a parenthesis.')
rev(r'\deleted{\unsure{B}}E','Overwriting inside the prose letter after avec.','P06: narrow upper curve/lower return beneath E; nearby q descender separately traced.')
rev(r'\deleted{B}E','Earlier B overwritten by E in the product formula.','P07: two thinner bowls remain under three heavy E arms.')
rev(r'\deleted{\unsure{compatibilité}}\inserted{\unsure{transversalité}}','Old word at right edge inside the opening quotation; replacement raised above it.','P11: lower strike and higher word bodies distinct; physical clipping prevents completing the final group as certain.')
rev(r'\deleted{dans le cas}','Only the three old groups before live cylindrique.','P12: continuous strike ends before cylindrique; closing quote pair belongs to the live quoted phrase.')
rev(r'\deleted{\unsure{cas|en}}\inserted{compatibilité}','Short old word after dans la, with replacement above before cônique.','P13: leader curves from the raised word to its site, rather than striking cônique.')
rev(r'\uline{mais est}','Live emphasized phrase, not a deleted old phrase plus replacement.','P13: independent underline below the intact letter bodies.')
rev(r'plus \unsure{exigeante|exigeant} \deleted{\unsure{que}} : correspond au cas où on \unsure{lui} devait','Raised/revised comparison clause above the old cancelled line.','P14/P15: plus and the live adjective stay above the separate crossed que group; colon has two dots; final verb reads devait.')
rev(r"T'\cap Y=0.\dot T'",'Small inserted formula below the left part of the comparison, associated with the revised clause.','P14: all formula marks visible. The curved lower stroke continues from g above; no independent box/underline is asserted.')
rev(r'\unsure{dans ce cas} '+old_formula_d,'Entire old lower line cancelled, including its terminal uncertain group.','P14/P16: one long strike crosses the old introduction and formula; earlier glyph under retraced E is not recovered.')
rev(r'\deleted{finie} \deleted{de}','Two separate cancelled words between famille and parties.','P17: finie has a horizontal strike; de has crossing strokes through independently visible d/e bodies. No replacement de is supplied.')

marks=list(csv.DictReader((ROOT/'packets'/PAGE/'marks.tsv').open(),delimiter='\t'))
diffs=list(csv.DictReader((ROOT/'packets'/PAGE/'differences.tsv').open(),delimiter='\t'))
assert [x['id'] for x in marks]==[x['id'] for x in R['decisions']]
assert len(diffs)==len(R['diff_coverage'])==25
bad=[]
for x in R['changes']:
    for k,s in [('c',C),('h',H)]:
        if x[k]!='(nothing)' and norm(x[k]) not in norm(s): bad.append((x['id'],k,x[k]))
    assert (ROOT/'work'/x['crop']).exists()
for x in R['audit_boxes']:
    a,b,c,d=x['xyxy']; assert 0<=a<c<=1685 and 0<=b<d<=2362
if bad:
    print('SOURCE EXCERPTS NEED CORRECTION',bad)
    raise SystemExit(1)
(OUT/'report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,crops=len(BOX),changes=len(R['changes']),marks=len(R['decisions']),inventory=len(R['inventory']),audit_boxes=len(R['audit_boxes']),doubts=len(R['doubts']),diff_rows=len(R['diff_coverage'])),ensure_ascii=False))
