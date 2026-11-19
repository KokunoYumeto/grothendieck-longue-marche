import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
 (r'\unsure{\mathbb{B}\mathrm r|\mathrm{Br}}',r'\mathrm{Br}'),
 (r'\deleted{\unsure{sont}}',r'\deleted{\unsure{sont|est}}'),
 (r'\deleted{\unsure{et}}',r'\deleted{et}'),
 (r'H^{3}(k(y),G_{\mathrm m})=0$; de plus',r'H^{3}(k(y),\mathbb{G}_{\mathrm m})=0$, de plus'),
 (r'\deleted{\unsure{con}}',r'\deleted{\unsure{con|Con}}'),
 (r'(.69,.08)--(.69,1.43);}}^{\deleted{\unsure{\prime|*}}}',r'(.69,.08)--(.69,1.43);\draw[line width=.02em] (.44,.73)--(.69,.73);}}^{\deleted{\unsure{\prime|*}}}'),
 (r'\uline{Cas particulier} \deleted{\unsure{:|1}}\inserted{(4.6):}',r'''\uline{Cas particulier} \tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.7) rectangle (.15,4.3);
  \node[overlay,anchor=base west,inner sep=0pt] at (.05,2.7) {\inserted{(4.6):}};
  \draw[overlay] (0,-.7) -- (0,1.9) .. controls (0,2.3) and (.2,2.3) .. (.5,2.3)
    -- (4.6,2.3) .. controls (4.9,2.3) and (5.1,2.5) .. (5.1,2.9);
}\deleted{1}'''),
 (r'\deleted{\unsure{et (4.16)}}',r'''\tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.8) rectangle (.1,4.6);
  \node[overlay,anchor=base west,inner sep=0pt] at (.15,2.8) {\deleted{\handwritten{\unsure{et (4.16)}}}};
  \draw[overlay] (.15,-.7) .. controls (-.4,1.8) and (0,2.0) .. (1,2.0)
    -- (6.5,2.0) .. controls (6.8,2.0) and (6.9,2.2) .. (6.8,2.7);
}'''),
 (r'\inserted{\handwritten{la}} relation',r'''\tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.5) rectangle (.1,4.0);
  \node[overlay,anchor=base west,inner sep=0pt] at (.1,2.4) {\inserted{\handwritten{la}}};
  \draw[overlay] (0,-.5) .. controls (.4,.8) and (.6,1.6) .. (1.1,1.7)
    .. controls (1.5,1.8) and (1.9,2.0) .. (2.0,2.4);
} relation'''),
 (r'\inserted{\handwritten{[24] $H^{1}(k,G)=0$}}',r'''\tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.6) rectangle (.15,4.5);
  \node[overlay,anchor=base west,inner sep=0pt] at (-5.0,2.7) {\inserted{\handwritten{[24] $H^{1}(k,G)=0$}}};
  \draw[overlay] (-5.5,2.6) .. controls (-6.0,1.6) and (-5.7,1.5) .. (-4.7,1.5)
    -- (-.55,1.2) .. controls (-.2,1.2) and (-.05,1.2) .. (0,.65)
    .. controls (.15,1.3) and (.4,1.4) .. (.7,1.4)
    -- (4.8,1.5) .. controls (5.1,1.5) and (5.2,1.5) .. (5.2,2.6);
  \draw[overlay] (0,.65) -- (0,-.6);
}''')
]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('(4.38), the two Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','eq38a5x: each typed Z has one diagonal and separate top/bottom serifs; its lower underline is a separate horizontal stroke. No doubled diagonal.','high',False,True,'misread symbol or index')
a('(4.38), exponent on second three-stem glyph',r'\deleted{\unsure{\prime|*}}',r"\mathrm{III}'",r'\deleted{\unsure{\prime|*}}','eq38b5x and oldprime18x: the raised mark is heavily crossed, with short horizontal and oblique cancellation strokes; its underlying prime/star shape remains obscured. H makes it live.','low',False,True,'deletion state (struck given live or live given struck)',cons='The exponent after the second three-stem group in (4.38) is cancelled, not a live prime.')
a('(4.38), second three-stem glyph drawing','three stems, upper/lower bars only','three separate roman I letters','three stems and bars, with thin transverse remnant between right-hand stems','eq38b5x: a thin horizontal stroke remains halfway between the two right uprights, under the heavier handwritten top and bottom rules. The drawing now retains this visible remnant without assigning it a separate live letter.','medium',True,True,'drawing or diagram')
a('cancelled reference above first Cas particulier',r'\deleted{(\unsure{4.6})}','absent',r'\deleted{(\unsure{4.6})}','oldnum12x: the two parentheses, initial angular 4 and final looped numeral survive typed x cancellation and additional oblique hand strokes; the middle is too obscured to remove the doubt.','medium',False,True,'omission')
a('cancelled token after first Cas particulier',r'\deleted{\unsure{:|1}}',r'\struck{1}',r'\deleted{1}','caseoldtoken24x: a continuous upright typed stem, upper left serif and broad flat bottom serif remain beneath the oblique black cancellation. These are the form of 1, not two separate colon dots.','medium',True,False)
a('raised reference (4.6): and leader','inline insertion after cancelled token','inline addition after cancelled 1','raised (4.6): with curved lower rule and downward leader before cancelled 1','case6x5: the printed reference lies above the old token; its rule turns downward at the boundary after particulier and upward at the far right. Both relative placement and stroke are reproduced.','high',True,True,'insertion or placement')
a('first case underline scope',r'Y \uline{est ... clos}.',r'\emph{Y est ... clos.}',r'Y \uline{est ... clos}.','whole/top half and case6x5: the long rule begins beneath est, to the right of Y; the next-line short rule stops before the period after clos.','high',False,True,'insertion or placement')
a('cancelled sentence after Alors la',r'\deleted{relation (4.13) est automatiqu\unsure{e.|e. La}}',r'\struck{relation (4.13) est automatique la}',r'\deleted{relation (4.13) est automatiqu\unsure{e.|e. La}}','cancelrel5x and cancelrelend12x: the typed relation, reference, est and automatiqu remain identifiable beneath typed x and a handwritten rule; the end contains overlapping loops, preventing a secure division into e, punctuation and possible La.','low',False,True,'misread word')
a('(4.39), Br alphabet',r'\unsure{\mathbb{B}\mathrm r|\mathrm{Br}}',r'\mathrm{Br}',r'\mathrm{Br}','br39x7 and brletter22x: B has one solid left vertical and two curved right bowls, with no separate parallel upright; r is a single typed letter.','medium',True,False)
a('(4.40), the two Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','eq40a5x: each Z has a single sloping diagonal; the separate lower rules underline the typed letters.','high',False,True,'misread symbol or index')
a('(4.40), overwritten argument of first H1',r'\underline{\deleted{\unsure{X|B}}\handwritten A}',r'\underline A',r'\underline{\deleted{\unsure{X|B}}\handwritten A}','oldA18x: faint typed upper serifs and a lower diagonal remain behind the dark handwritten A; the underlying letter cannot be securely separated as X or B. H omits the correction layer.','low',False,True,'omission')
a('second case underline scope',r'Y \uline{est ... fini} k.',r'\emph{Y est ... fini k.}',r'Y \uline{est ... fini} k.','underlinescase7x2: the first rule begins after Y under est; the short continuation spans fini only, stopping before k and the period.','high',False,True,'insertion or placement')
a('cancelled raised addition after (4.13)',r'\deleted{\unsure{et (4.16)}}',r'\add{\struck{\ill{}}}',r'\deleted{\handwritten{\unsure{et (4.16)}}}, raised with leader','old4_16x10 and old4_16_upright8x: e/t strokes, parentheses and portions of the angular and looped numerals remain through cancellation; exact interior reading stays marked. A curved lower line points to the gap after (4.13).','medium',True,True,'readable ink left as \ill{}','yes')
a('overwritten verb after (4.13)',r'\deleted{\unsure{sont}}\handwritten{est}',r'\struck{est}',r'\deleted{\unsure{sont|est}}\handwritten{est}','sont_est18x: the dark handwritten e loop, s turn and t stem/cross remain live. The lighter typed word is largely covered, and its middle letters do not securely distinguish sont from est.','low',True,True,'deletion state (struck given live or live given struck)',cons='The correction est remains live after (4.13); the obscured underlying verb is cancelled.')
a('cancelled conjunction before on aura',r'\deleted{\unsure{et}}',r'\struck{et}',r'\deleted{et}','annoa5x and annotation_upright2x: two short typed characters survive under diagonal hatching, with an open e body and final t ascender/cross.','medium',True,False)
a('handwritten note after (4.16)','(4.16) puisque','(4.16), puisque','(4.16) puisque','annoa5x and annotation_upright2x: blank gap after the closing parenthesis before the long initial p stem; no comma.','high',False,True,'text not on the page')
a('handwritten note, coefficient group',r'G_{\mathrm m}',r'\mathbb G_m',r'\mathbb{G}_{\mathrm m}','handgm14x: the G has both a curved left outer stroke and a separate straight inner upright joining its upper turn to the lower stroke; m is smaller and lower. The double construction is distinct from the plain G in the Lang note.','high',True,False,'misread symbol or index',cons='The coefficient group in the handwritten H3 equation is written with a doubled G.')
a('handwritten note after =0','; de plus','; de plus',', de plus','endcomma20x: one continuous hooked low stroke follows 0, without a separate upper dot; it is a comma.','high',True,True,'misread symbol or index')
a('cancelled end of delta equality',r'\deleted{\unsure{=\delta\prime\prime}}',r'\struck{\ill{}}',r'\deleted{\unsure{=\delta\prime\prime}}','cancelenddelta15x: two short horizontal remnants at left, a high bent stem and lower loop in the middle, and two short right-hand strokes remain through the hatching, but cannot all be cleanly separated. The formula is retained with doubt, never replaced by an illegible-word token.','medium',False,True,'misread symbol or index','yes')
a('(4.41), corrected first Z',r'\deleted{\unsure{2|Z}}\handwritten Z',r'\mathbb Z',r'\deleted{\unsure{2|Z}}\handwritten Z','delta41x13: a dark handwritten zigzag covers an older rounded upper trace; whether that older trace was 2 or Z remains obscured. It is not a second independent diagonal producing a blackboard letter.','low',False,True,'omission')
a('(4.41), overwritten denominator before second Z',r'\deleted{\unsure{1|\delta}}\handwritten\Delta',r'\Delta',r'\deleted{\unsure{1|\delta}}\handwritten\Delta','delta41x13: a thin older vertical protrudes above and through the triangular handwritten Delta, with faint lower residue. The covered lower shape does not distinguish 1 from delta.','low',False,True,'omission')
a('(4.41), final Z',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','delta41x13: the final typed Z has one diagonal and separate underline, unlike the overwritten first letter.','high',False,True,'misread symbol or index')
a('cancelled words before D’autre part',r'\deleted{\unsure{compte tenu de|compte tenu du}}',r'\struck{\ill{}}',r'\deleted{\unsure{compte tenu de|compte tenu du}}','oldcompte8x: c/o, p descender, t ascender, following tenu and final tall d remain beneath cancellation; the final low letter is covered enough to retain de/du.','low',False,True,'readable ink left as \ill{}','yes')
a('(4.42), the two Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','eq42x3: each typed letter has one diagonal; the handwritten double prime belongs to delta and is separate from the following Z.','high',False,True,'misread symbol or index')
a('la inserted before relation','inline insertion','inline addition','la raised, with curved leader into gap before relation','correctionla6x: la lies above the line, and its long curved stroke ends between the cancelled s of des and the initial r of relation.','high',True,True,'insertion or placement')
a('right edge after suivante and cancelled s',r'\unsure{:}','absent',r'\unsure{:}','colonedge18x: a separate upper point is visible above the cancelled final s; the lower/right part meets the black scan edge. A colon remains possible, but is not secure enough to remove the doubt.','medium',False,True,'omission')
a('left-margin cross beside théorème',r'\unsure{x|$\times$}','absent',r'\unsure{x|$\times$}','marginx16x: two light oblique strokes cross, one with a long curved lower-right end. Shape is visible but does not distinguish a literal x from a cross mark.','low',False,True,'omission')
a('Lang correction layer',r'\deleted{Lang}\handwritten{LANG}','LANG',r'\deleted{Lang}\handwritten{LANG}','lang6x: typed lowercase a/n/g remain beneath the darker angular capital A/N/G; the original L is overtraced. The earlier mixed-case name is retained as replaced text.','high',False,True,'omission')
a('Lang note enclosure and endpoint','inline [24] H1(k,G)=0','([24] H1(k,G)=0)','raised [24] H1(k,G)=0 with curved lower brace and leader after LANG','lang6x and lang_upright5x: square brackets surround 24; a separate long lower curve has upturned ends and a downward central leader between LANG and pour. H’s outer parentheses are not literal punctuation on this note.','high',True,True,'drawing or diagram')
a('overwritten beginning of connexe',r'\deleted{\unsure{con}}\handwritten{con}nexe',r'\struck{Con}connexe',r'\deleted{\unsure{con|Con}}\handwritten{con}nexe','connexe9x and connexinitial18x: the three typed positions c/o/n are overwritten in dark ink; the original initial is partially covered and its case is uncertain. The live handwritten lower-case con is followed by unchanged typed nexe.','low',True,True,'misread word')
a('last line, handwritten final e of laissée',r'laissé\handwritten e',r'laissé\struck e',r'laissé\handwritten e','laissee14x: a small dark loop and descending exit follow the typed accented é; no cancellation stroke crosses this added letter.','high',False,True,'deletion state (struck given live or live given struck)')
I=[]
def i(kind,pos,text,hand='typewriter'):I.append(dict(kind=kind,position=pos,text=text,hand=hand))
i('text','upper right','23','his hand')
i('display','top, (4.38)','0 → underlined Z/δ″Z → three-stem group prime (Y,A) → three-stem group with cancelled exponent (Y,B) → 0','typewriter and his hand')
i('deletion','above second group in (4.38)','cancelled prime/star','his hand')
i('text','below (4.38)','Explicitons deux cas particuliers importants:')
i('deletion','above first case heading','(4.6), uncertain, cancelled','typewriter and his hand')
i('text','first case heading and opening paragraph','Cas particulier; Y est une courbe algébrique sur un corps algébriquement clos ... (4.12 bis) :')
i('deletion','after first Cas particulier','old 1','typewriter and his hand')
i('insertion','above first case, after heading','(4.6):','typewriter')
i('drawing','beneath raised (4.6):','curved rule with downward left leader and upturned right end','his hand')
i('drawing','first case heading and hypothesis','underlines beneath Cas particulier and est ... clos','his hand')
i('deletion','first paragraph after Alors la','relation (4.13) est automatiqu...','typewriter and his hand')
i('display','(4.39)','Br(X) ≃→ H1(Y, underlined B);','typewriter and his hand')
i('text','between (4.39) and (4.40)','lorsque de plus les δy sont égaux à 1 ... par','typewriter and his hand')
i('insertion','after i.e.','si','his hand')
i('deletion','after s’explicite','comme étant égal à','typewriter')
i('display','(4.40)','0 → underlined Z/δZ → H1(Y, corrected underlined A) → H1(Y,B) → 0,','typewriter and his hand')
i('deletion','first H1 argument in (4.40)','old X/B overwritten by A','typewriter and his hand')
i('text','after (4.40)','compte tenu que ... l’on a ici nécessairement δ=δ′=δ″.','typewriter and his hand')
i('deletion','after compte tenu que','dans','typewriter')
i('text','second case heading and paragraph','Cas particulier (4.7): Y est une courbe algébrique propre sur un corps fini k ... (4.4):','typewriter and his hand')
i('drawing','second case heading and hypothesis','underlines beneath Cas particulier and est ... fini','his hand')
i('deletion','raised after (4.13)','et (4.16), uncertain','his hand')
i('drawing','beneath cancelled raised addition','curved leader into gap after (4.13)','his hand')
i('deletion','before automatiquement','underlying sont/est','typewriter and his hand')
i('insertion','over underlying verb','est','his hand')
i('insertion','interline after k étant parfait','ainsi que (4.16) puisque k(y) est de dimension ≤1, d’où H3(k(y), doubled Gm)=0, de plus','his hand')
i('deletion','before on aura','et','typewriter and his hand')
i('deletion','after δ=δ′','uncertain =δ″','his hand')
i('display','(4.41)','0 → Br(X) → three-stem group(Y,B) → underlined corrected Z/ΔZ → 0, où Δ|δ.','typewriter and his hand')
i('deletion','quotient in (4.41)','old 2/Z and old 1/δ below corrections','typewriter and his hand')
i('deletion','before D’autre part','compte tenu de/du','typewriter and his hand')
i('text','between (4.41) and (4.42)','D’autre part, si les δy ... suite exacte','typewriter and his hand')
i('display','(4.42)','0 → underlined Z/δ″Z → three-stem(Y,A) → three-stem(Y,B) → 0,','typewriter and his hand')
i('text','introduction to (4.43)','ce qui est un cas particulier de (4.37), compte tenu de ... relation suivante','typewriter and his hand')
i('deletion','introduction to (4.43)','s of des, relations and suivantes','typewriter and his hand')
i('insertion','above gap before relation','la','his hand')
i('drawing','leader below la','curved stroke into gap before relation','his hand')
i('display','(4.43)','barred δy = δy','typewriter and his hand')
i('text','after (4.43)','pour tout point fermé y de Y ... three-stem prime (Y,A)=three-stem (Y,A).','typewriter and his hand')
i('text','final paragraph','La démonstration ... est laissée au lecteur comme un exercice plaisant et délectable.','typewriter and his hand')
i('deletion','start of final paragraph','s of des and égalités','typewriter and his hand')
i('insertion','before égalité','l′','his hand')
i('margin note','left of théorème','uncertain x/cross','his hand')
i('insertion','above LANG','[24] H1(k,G)=0','his hand')
i('drawing','beneath Lang note','long curved brace with downstroke after LANG','his hand')
i('deletion','theorem name','typed Lang overwritten by LANG','typewriter and his hand')
i('insertion','theorem name','LANG','his hand')
i('deletion','beginning of connexe','con/Con overwritten','typewriter and his hand')
i('insertion','beginning of connexe','con','his hand')
i('insertion','after connexe','G=','his hand')
i('display','embedded at start of final line','underlined Pic with exponent 0 and index X_y/y','typewriter and his hand')
i('insertion','last line after laissé','e','his hand')
commit(97,8,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter and his hand',observations='Whole then both supplied halves personally viewed before C/H. All 38 base crops, all eight adaptive crops and all three upright rotated crops personally read; exact crop boxes, scales and rotation angles are in crop_manifest.tsv. Entire typed prose read line by line, including accents, punctuation, singular/plural endings, line-end word joins and parenthesis closure. Every displayed and inline formula checked for letters, alphabets, indices, primes, bars, relations, directions and underlines. All cancellations, handwritten corrections and insertion endpoints checked; newly retained leaders are drawn. The two Zs in each exact sequence are single-stroke typed letters; the H3 coefficient G has an independently drawn inner upright. No readable watermark established. Archive 7 is comment only; manuscript 23 is transcribed. This is transcription collation, not a second audit or a check of the mathematical claims.'))
with open('out/notation.tsv','a') as f:
 f.write('Typed underlined Z\t97/8, (4.38), (4.40)–(4.42)\tOne typed diagonal plus separate underline; handwritten overwriting only on first Z in (4.41)\t\\underline{\\mathrm Z}\told first Z in (4.41) uncertain\n')
 f.write('Handwritten doubled G versus plain G\t97/8 H3 note and Lang H1 note\tH3 G has curved outer left stroke and distinct straight inner upright; Lang G has single curved left contour\t\\mathbb{G}_{m} in H3; G in H1\tnone\n')
