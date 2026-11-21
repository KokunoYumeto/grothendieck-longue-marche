from pathlib import Path
import json
import csv

BASE = Path('/workspace/scratch/9d0bd22e5d3a/work/SP86_C13_149')
PACKET = Path('/workspace/scratch/9d0bd22e5d3a/packets/149_scan077')
PAGE = '149_scan077'
manifest_path = BASE/'readings'/f'{PAGE}_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
crops = {p['id']:p for p in manifest}
crops['P17']['subject'] = 'g_i0 relation f before on voit; the low f return also read in native view and P18, audit extends below this crop'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

tex = r'''\scanpage{77}
\mspage{38}
dans ce cas le critère homologique s'avère insuffisant\ldots) Il faudrait donc calculer cet \deleted{élément de}\inserted{homomorphisme}
\[
(11)\qquad T_\ell\bigl(\simeq H_1(\eta,\mathbb Z_\ell)\bigr)\longrightarrow\unsure{T|\mathbb T}_\ell^I/T_\ell
\]
pour constater qu'il n'est pas nul dans le cas \unsure{envisagé|envisage}, $\nu\geqslant2$ (et traiter séparé-
ment le cas $\nu=1$).

\deleted{[On va faire des calculs intrinsèques, en}
\[
\deleted{\unsure{\operatorname{Ker}}(\mathcal J^\bullet_{U/S}\longrightarrow\mathcal J^\bullet_{X/S})\simeq G_m^I/G_m}
\]
\[
\deleted{H_1(\mathcal U,\mathbb Z_\ell)\simeq H_1(\mathcal J^1_{U/S},\mathbb Z_\ell)\underset{\substack{\text{isom}\\\text{de Kummer}}}{\simeq}\lim_{\longleftarrow}\deleted{\unsure{\ell^n}}{}_{\ell^n}(\mathcal J^0_{U/S})}
\]
\deleted{On considère donc l'image inverse par $\eta\longrightarrow\mathcal J^1_{U/S}$ composé de $\eta\longrightarrow U\longrightarrow\mathcal J^1_{U/S}$) des isogénies}

Je vais deviner le résultat :

Soit \deleted{\unsure{q}} $x=g_{i_0}(s)$, $A=\underline O_{X,x}$, $V$ l'anneau de $S$, $\mathcal J_{i_0}$ l'idéal de l'hom $A\xrightarrow{g_{i_0}^*}V$ associé à $g_{i_0}$, c'est donc un idéal inversible de $A$ -- soit de $\overline m$ $\mathcal J_f$ l'idéal associé à $f^*:A\longrightarrow V$, et considérons $g_{i_0}^*(\mathcal J_f)$, c'est un idéal de $V$ engendré par un générateur, et comme $g_{i_0}\neq f$, on voit que cet idéal n'est pas nul. Soit $\mu=\operatorname{long}V/g_{i_0}^*(\mathcal J_f)\ \deleted{\unsure{=}}$. , cet entier
\margin{76}
'''
(BASE/'readings'/f'{PAGE}.tex').write_text(tex)

changes=[]
def change(identifier,cp,place,C,H,final,evidence,confidence='high',against_C=False,against_H=True,kind='misread word',category='Words',marked_in_H=False,consequential=False):
    c=crops[cp]
    changes.append(dict(id=identifier,place=place,C=C,H=H,final=final,evidence=evidence,crop=c['path'],box=c['box'],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=category,marked_in_H=marked_in_H,consequential=consequential))

change('P01a','P01','main line 1, final verb',"s'avère",'serait',"s'avère",'The initial short s is followed by a separate apostrophe. The following a/v bodies lead to an e with a detached accent, then the final r/e return at the right edge. The apostrophe and accented middle support s\x27avère.')
change('P03a','P03','display (11), argument of H_1',r'\eta',r'\mathcal Y',r'\eta','The small argument has a short left stem, joined upper arch and longer curved right descender. It is read with the two matching eta forms in the later canceled expression, rather than as a tall capital Y.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P04a','P04','main line 5, placement of nu comparison',r'$\nu\geq2$',r'\add{$\nu\geqslant2$}',r'$\nu\geqslant2$','The comparison follows the same rising writing line as the preceding comma and the following (et traiter. It has no separate attachment leader or independent raised insertion position. The lower comparison stroke is slanted upward to the right; geqslant records its angle, which is not counted separately as a material difference.',kind='insertion or placement',category='Insertions put in the wrong place')
change('P04b','P04','main lines 5–6, divided word', 'séparément','séparément','séparé-\nment','A visible horizontal hyphen follows séparé at the right edge of line5. The next line starts with ment, fully visible in P05. Both parts and the original line-end division are preserved.',against_C=True,kind='omission',category='Omissions')
change('P07a','P07','canceled main line 7, final word','en',r'\uncertain{avec}','en','After the comma only two low connected bodies are present: an e-like entry followed by a flat n return. The horizontal cancellation passes through their level. There is no longer four-letter body between the comma and line end.',kind='misread word',category='Words',marked_in_H=True)
change('P08a','P08','first canceled display, first J superscript',r'\unsure{\bullet|0}','1',r'\bullet','The raised mark is a compact solid dark point. There is no enclosed counter as in the later hollow zero of P09, and no stem/foot structure as in the clear1 of that same later formula. The whole Ker expression was read with this mark.',against_C=True,kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P08b','P08','first canceled display, second J superscript',r'\unsure{\bullet|0}','1',r'\bullet','The second raised mark is likewise a small solid point beside the upper J contour. Its darkness is continuous across the tiny body; no hollow zero or extended numeral1 body is visible. The following X/S, parenthesis, similarity sign and G quotient were also read.',against_C=True,kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P09a','P09','second canceled display, first relation',r'\simeq',r'\xrightarrow{\sim}',r'\simeq','A separate wavy upper stroke lies above a long lower horizontal bar. The bar ends without a paired arrowhead. The source therefore retains the two-part similarity sign of C.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P09b','P09','second canceled display, annotation below the second relation',r'\underset{\text{isom de Kummer}}{\simeq}',r'(\uncertain{isom. de Kummer}).',r'\underset{\substack{\text{isom}\\\text{de Kummer}}}{\simeq}','The annotation consists of two short lines, isom above de Kummer, directly below the second relation. The i dot, low s/o/m returns, de, and the K stem/branches followed by ummer are visible. No independent opening/closing parentheses or terminal full stop surround it. The long diagonal crossing the annotation belongs to the block cancellation.',kind='insertion or placement',category='Insertions put in the wrong place',marked_in_H=True)
change('P09c','P09','second canceled display, internal cancellation after lim',r'\deleted{\unsure{\ell^n}}','(nothing)',r'\deleted{\unsure{\ell^n}}','A separately overwritten/canceled cluster follows lim and precedes the smaller legible left torsion index. At least a tall loop and higher short bodies survive; the crossed strokes do not expose all of the proposed ell^n. The tentative C reading is retained within an inner deletion, in addition to the larger canceled passage.',confidence='low',kind='omission',category='Omissions')
change('P11a','P11','canceled main line 9, first expression after par',r'\eta\longrightarrow\mathcal J^1_{U/S}',r'\mathcal Y\to J^1_{\mathcal U/S}',r'\eta\longrightarrow\mathcal J^1_{U/S}','The first small symbol has a short left upright/arch and a long curved right descender. Its body is much smaller than the following J. The single right arrow, raised1 and U/S index are separately visible.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P11b','P11','canceled main line 9, expression after composé de',r'\eta\longrightarrow U\longrightarrow\mathcal J^1_{U/S}',r'\mathcal Y\to\mathcal U\to J^1_{\mathcal U/S}',r'\eta\longrightarrow U\longrightarrow\mathcal J^1_{U/S}','The second small symbol repeats the short upper arch and curved descending right side of the first eta. The following U has an open hooked entry. Both right arrows have one small head; the last J bears a visible1.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P11c','P11','canceled main line 9, before composé','(composé','(composé','composé','Only one separate initial c contour precedes omposé. The larger curve farther left continues into the long horizontal cancellation stroke and down toward des isogénies. It is not an independent opening parenthesis. The final closing parenthesis after the last J expression is clearly present and is retained.',against_C=True,kind='text not on the page',category='Text that is not on the page')
change('P13a','P13','main line 12, canceled fragment after Soit',r'\deleted{\unsure{q}}',r'\struck{\ill{}}',r'\deleted{\unsure{q}}','An upper bowl and descending return survive beneath additional crossing/overwriting strokes. They support a tentative q-shaped reading; the complete letter is not securely exposed. The adjacent live g has a clearer closed lower loop. The uncertainty remains within the deletion.',confidence='low',kind=r'readable ink left as \ill{}',category='Readable ink left as illegible')
change('P14a','P14','main line 12, O in A equality',r'A=\underline O_{X,x}',r'A=\mathcal O_{X,x}',r'A=\underline O_{X,x}','A short detached underline lies beneath the open oval O and ends before the large crossed X index. Both X diagonals, the separator comma and the small x are visible. Additional pale/vertical retracing near X does not yield a separate older letter securely.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P15a','P15','main line 13, hom abbreviation',"l'hom","l'hom.","l'hom",'The looped l and apostrophe precede tall h, a tiny dark oval o and a very compressed m with an upper cusp and long flat return. No independent point follows the m. The black o inside the word is not a terminal full stop.',kind='text not on the page',category='Text that is not on the page')
change('P16a','P16','main line 15, prose shorthand; M1214',r'\unsure{\overline m|\overset{m}{=}}','même',r'\overline m','The sign has two levels: a short upper bar, and a lower open cup/cusp followed by a long flat return. The lower shaped stroke supports compressed m, compared with the low m of hom in P15. There is no separately recoverable third level for an m above an equals sign. The written barred abbreviation is retained without expansion.',confidence='medium',against_C=True,kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised')
change('P18a','P18','main line 19, initial symbol of length equality',r'\mu','n',r'\mu','The initial symbol has a long left descending stem, a central rising return and a shorter right stroke/foot. The extended left descender and two-part body support mu. The following equality has two separate bars.',kind='misread symbol or index',category='Symbols and indices',consequential=True)
change('P18b','P18','main line 19, punctuation after canceled sign',r'\deleted{\unsure{=}},',r'\struck{=},',r'\deleted{\unsure{=}}. ,','A small dark oval point is detached to the right of the canceled equals-like cluster at punctuation height. No cancellation stroke reaches it. A further separate comma follows after a gap. The point is preserved outside the deletion, before the comma; confidence in its punctuation role is medium. The unexpected sequence is not regularized.',confidence='medium',against_C=True,kind='omission',category='Omissions')
change('P19a','P19','main line 19, final words','cet entier','est entier','cet entier','The first word starts with an open c curve, then a low e body and a tall t with its return. The next word has a low e/n stretch, tall t, dotted i, low e and final r return. No terminal punctuation follows entier.')
change('P20a','P20','bottom-left thin foliation',r'\margin{76}','(nothing)',r'\margin{76}','The thin7 has a top bar, descending stem and crossing stroke. The6 has a long curved upper entry and closed lower loop. This small narrow-pen foliation is separate from the autograph38 at the head.',kind='omission',category='Omissions')

decisions=[dict(id='M1214',cote='149',scan='77',decision='first',reading=r'\overline m',evidence='A short upper bar sits over one low cup/cusp with a flat terminal return. The lower shape matches the compressed m observation in hom. Only these two levels are recoverable; no separate third level supports m over an equals sign. The result remains medium confidence.',crop='crops/149_scan077_P16.png (285,1925,710,2055)',confidence='medium')]

inventory=[
 dict(element='E01',kind='margin note',position='head near centre; [785,30,840,75]',first_words_or_objects='38',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E02',kind='text',position='main lines1–3 above display(11)',first_words_or_objects="dans ce cas le critère homologique s'avère",sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E03',kind='deletion',position='main line3; [755,205,1585,337]',first_words_or_objects=r'\deleted{élément de}',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E04',kind='insertion',position='above the canceled élément de; same P02 box',first_words_or_objects=r'\inserted{homomorphisme}',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E05',kind='display',position='display(11); [300,333,1450,475]',first_words_or_objects=r'(11) T_\ell(\simeq H_1(\eta,\mathbb Z_\ell))\longrightarrow\unsure{T|\mathbb T}_\ell^I/T_\ell',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E06',kind='text',position='main lines4–6, y475–810',first_words_or_objects="pour constater qu'il n'est pas nul",sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E07',kind='deletion',position='large canceled passage from right end of main line6 through des isogénies; approximately [275,649,1655,1675]',first_words_or_objects='[On va faire des calculs intrinsèques, en',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E08',kind='display',position='first display within the large cancellation; [275,868,1550,1048]',first_words_or_objects=r'\unsure{\operatorname{Ker}}(\mathcal J^\bullet_{U/S}\longrightarrow\mathcal J^\bullet_{X/S})\simeq G_m^I/G_m',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E09',kind='display',position='second display within large cancellation; [275,1030,1555,1283]',first_words_or_objects=r'H_1(\mathcal U,\mathbb Z_\ell)\simeq H_1(\mathcal J^1_{U/S},\mathbb Z_\ell)',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E10',kind='insertion',position='two-line annotation below second similarity sign, inside canceled block; approximately [910,1170,1150,1270]',first_words_or_objects='isom / de Kummer',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E11',kind='deletion',position='inner overwritten/canceled group after lim in second canceled display',first_words_or_objects=r'\deleted{\unsure{\ell^n}}',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E12',kind='text',position='live paragraph beginning at right of the final canceled lines, main line11, y1490–1620',first_words_or_objects='Je vais deviner le résultat :',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E13',kind='text',position='main lines12–19, y1610–2365',first_words_or_objects='Soit',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E14',kind='deletion',position='small canceled fragment immediately after Soit in line12; P13',first_words_or_objects=r'\deleted{\unsure{q}}',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E15',kind='deletion',position='final line after the closed length-expression parenthesis; P18',first_words_or_objects=r'\deleted{\unsure{=}}',sheet_kind='text',hand='his hand',transcribed='yes'),
 dict(element='E16',kind='margin note',position='bottom left; [18,2290,85,2350]',first_words_or_objects='76',sheet_kind='text',hand='another hand',transcribed='yes'),
]

doubts=[
 dict(place='display(11), numerator T',reading=r'\unsure{T|\mathbb T}_\ell^I/T_\ell',alternatives=r'T | \mathbb T',confidence='low',reason='A conspicuous oblique crosses the top/stem of this T, unlike the two other T forms in the same display. A separate parallel second stem is not securely isolated; no complete earlier letter or revision chronology is recovered. The doubt concerns this local letter form only.'),
 dict(place='main line5, final-e accent of envisagé',reading=r'\unsure{envisagé|envisage}',alternatives='envisagé | envisage',confidence='low',reason='The low final e return is legible, and the earlier i dot is clear, but no securely detached accent can be separated above the final e. This is a new certainty-only doubt.'),
 dict(place='first canceled display, operator',reading=r'\unsure{\operatorname{Ker}}',alternatives='Ker remains tentative beneath local overwriting',confidence='low',reason='Dense crossing and retracing cover the left operator bodies. Its latter low returns support the tentative reading, but not every letter is recoverable. The whole expression remains within the larger canceled block.'),
 dict(place='second canceled display, internal canceled fragment after lim',reading=r'\deleted{\unsure{\ell^n}}',alternatives=r'\ell^n remains tentative',confidence='low',reason='A tall loop and higher compact bodies survive several local crossing strokes. A complete second copy cannot be established. The separate smaller left torsion index that follows is legible.'),
 dict(place='main line12, canceled fragment after Soit',reading=r'\deleted{\unsure{q}}',alternatives='q remains tentative; g-like descending return also noted',confidence='low',reason='The upper bowl and descending return are partly overlaid. The adjacent live g has a more complete lower loop, so the canceled fragment is not resolved from that comparison.'),
 dict(place='main line19, canceled sign after length expression',reading=r'\deleted{\unsure{=}}',alternatives='equals sign remains tentative beneath cancellation',confidence='low',reason='Two short horizontal levels are partly visible but crossed by dense oblique strokes. The later detached point and comma lie outside those strokes.'),
]

notes=[
 '[S077.1; source opening] The page continues with the author\x27s wording about a critère homologique and the wish to calculer cet homomorphisme. Formula(11) follows. The text itself says pour constater qu\x27il n\x27est pas nul and gives the two written nu cases; this transcription reports those source claims without proving them.',
 '[S077.2; canceled source] The large canceled passage begins [On va faire des calculs intrinsèques, en, contains two displays and the annotation isom / de Kummer, then continues On considère donc l\x27image inverse par and ends des isogénies. Its mathematical and verbal content is transcribed as canceled source text, without treating it as an asserted result.',
 '[S077.3; source transition] The live sentence Je vais deviner le résultat : stands to the right of the last canceled lines. The author\x27s own wording is preserved; no guessed result is supplied by the transcription.',
 r'[S077.4; source lower paragraph] The author writes x=g_{i_0}(s), A=\underline O_{X,x}, names V and the ideal expressions, and writes the final length expression beginning with mu. The closing words are cet entier. This reports the written definitions and claims on the page; no continuation or mathematical check is supplied.',
 'Nineteen main-text lines are counted, with three separate display rows and the two short annotation lines described separately. Within the reading order, the last canceled line des isogénies is completed before the live Je vais deviner line, although the live line begins physically higher at its right.',
 'The original scan was viewed before C/H, as instructed. Both native halves were then read once line by line against both witnesses, including every agreed token, accent, stop, index, endpoint, correction and source number. The twenty saved first crops cover all mandatory or open places. No OCR, external research or TeX compilation was used.',
 'The first deletion crosses élément de; homomorphisme is written above it as its replacement. The larger cancellation has long oblique strokes plus horizontal strokes across its prose lines and a long bent stroke across the composé / des isogénies ending. The small local cancellations inside and after that block are retained independently.',
 'The line-end division séparé- / ment is literal source ink and is preserved. The nu comparison follows the same rising baseline as the surrounding prose; it has no separate insertion leader. Its lower stroke is slanted, represented by geqslant without a material count for angle alone.',
 'Only the initial c contour precedes omposé. The farther-left bend belongs to a cancellation stroke. The source retains its final closing parenthesis without an added opening parenthesis; the opening square bracket at the start of the canceled block likewise has no supplied closing mate.',
 'The first large U in the second canceled display has a closed oval upper-left entry and is rendered mathcal U locally. The smaller U indices and the later standalone U have open entries. Individual contours are recorded in the hand log; uniform H font-wrapper differences are not broadly counted on this page. J, G, O and T contours are also recorded without assigning new meanings from typography.',
 'The final point is a small dark detached oval outside the canceled equals-like cluster. A separate comma follows it. Both are preserved in their source order; the point\x27s punctuation role is medium confidence. The cancellation does not visibly reach it.',
 'The thin76 at lower left belongs to another hand and is encoded as margin76. The autograph head number38 uses mspage. The display label11 and all small numerical indices are covered by audit boxes.',
 'P17 reaches the low f return at its border; that return was also read in the native half and the neighboring P18 view. Its audit box extends below the saved P17 border. No crop was replaced or repeated.',
]

hand=[
 dict(form='eta',observation='A short left upright joins a small upper arch, with a longer curved right descender. The shape recurs in the small H_1 argument and twice in the canceled map line.',places='P03; P11 twice',scope='all three eta occurrences on this sheet',witness_errors='H uses capital mathcal Y at these positions.'),
 dict(form='solid raised point / hollow0 / numeral1',observation='Both raised marks in the first canceled display are solid points. The last J of the second canceled display has a hollow0. Its preceding J has1 with an angled cap and lower foot, as do both J superscripts in the later canceled map line.',places='P08; P09; P11',scope='all raised J marks on the page',witness_errors='C keeps bullet|0 doubts at the first two points; H gives1 at both. They resolve to bullet from their solid bodies.'),
 dict(form='numerator T with extra oblique',observation='The numerator T in display11 has a diagonal crossing its stem/top bar. The other two T forms have a top bar and a single simpler stem. A separate parallel second stem and a complete older letter cannot be isolated.',places='P03',scope='local numerator only',witness_errors='C plain T and H mathbb T remain local alternatives; no revision chronology is invented.'),
 dict(form='closed-entry and open-entry U',observation='The first large U in H_1 has a closed oval upper-left entry. The smaller U subscripts in the two canceled displays have open cups, and the later standalone U has an open hook. These local shapes are retained rather than uniformly applying a witness wrapper.',places='P08/P09/P11',scope='each visible U occurrence locally compared',witness_errors='Local mathcal U rendering is recorded at the first H_1 argument; wrapper-only counts are deferred to root reconciliation.'),
 dict(form='script J, G and O',observation='J has a long top/body stroke and broad lower turn; the two G forms have a curved outside body with short internal strokes; the O in A has an open upper oval contour and a separate underline. The X below it has two dark diagonals plus pale/vertical retracing.',places='P08/P09/P11/P13/P14 and lower paragraph',scope='observed forms on this sheet',witness_errors='H omits the actual O underline; alphabet wrappers alone are not broadly counted. No older X letter is reconstructed.'),
 dict(form='compressed m and barred m',observation='The m in hom has a shallow cusp followed by a long flat return. The lower component of the shorthand likewise has a cup/cusp and flat continuation, with a separate short upper bar. Only two levels are visible.',places='P15/P16',scope='local comparison supporting M1214 at medium confidence',witness_errors='C marks overline m versus m over equals; H expands the shorthand to même.'),
 dict(form='similarity and arrow endpoints',observation='The first relation in the second canceled display is an upper wave over an unheaded lower bar. The earlier display11 map and later map-line connectors have a single right head. The limit arrow points left beneath lim. The lower comparison bar of nu geqslant2 rises to the right.',places='P03/P04/P08/P09/P11',scope='each connector and decoration inspected',witness_errors='H turns the first canceled similarity relation into an arrow with tilde.'),
 dict(form='mu',observation='The final length variable has a long left descender, central rising return and shorter right stroke; the source body is mu-shaped.',places='P18',scope='this final variable only',witness_errors='H reads n.'),
 dict(form='near-vertical inequality slash',observation='The relation between g_i0 and f has two separate horizontal levels crossed by an upright/slightly oblique stroke.',places='P17',scope='single agreed occurrence',witness_errors='Both witnesses agree on neq; direct ink inspection supports it.'),
 dict(form='punctuation and abbreviation stops',observation='The small dark oval inside hom is its o; no stop follows the m. The annotation isom has no supplied stop or surrounding parentheses. The final detached point lies outside the local cancellation and precedes a separate comma.',places='P09/P15/P18',scope='each named place independently inspected',witness_errors='H adds hom. and parentheses/periods around the annotation; both witnesses omit the final detached point.'),
 dict(form='accents and cancellation overlap',observation='The apostrophe and accent in s\x27avère are detached. In envisagé the final accent cannot be isolated securely, although the i dot is clear. The short accent in canceled isogénies is crossed by a long diagonal, whose path is distinguishable from the word.',places='P01/P04/P12',scope='local occurrences only',witness_errors='The envisagé accent doubt is certainty-only; the visible source line-end hyphen in séparé- is restored.'),
]

notation=[
 dict(form=r'T_\ell(\simeq H_1(\eta,\mathbb Z_\ell))\longrightarrow\unsure{T|\mathbb T}_\ell^I/T_\ell',meaning='The homomorphism written as source formula(11); the numerator letter form remains a local reading doubt.',places='display(11), P03'),
 dict(form=r'\nu\geqslant2;\ \nu=1',meaning='The two explicit numerical comparisons appearing in the source sentence following formula11.',places='main lines5–6, P04/P05'),
 dict(form=r'\mathcal J^\bullet_{U/S};\ \mathcal J^\bullet_{X/S}',meaning='The two J expressions in the canceled Ker display. The raised marks are solid dots as written; no mathematical interpretation is assigned to them.',places='first canceled display, P08'),
 dict(form=r'\overline m',meaning='Written prose shorthand after soit de, retained without expansion in the transcription.',places='main line15, P16 / M1214'),
 dict(form=r'x=g_{i_0}(s),\quad A=\underline O_{X,x}',meaning='Equalities explicitly written after Soit in the live lower paragraph.',places='main line12, P13/P14'),
 dict(form=r'\mu=\operatorname{long}V/g_{i_0}^*(\mathcal J_f)',meaning='The final written length expression, followed by a locally canceled tentative equals sign and the separate point/comma sequence.',places='main line19, P18'),
]

abbreviations=[
 dict(written='hom',expansion='homomorphisme',places='main line13; written without a stop'),
 dict(written='isom',expansion='isomorphisme',places='two-line annotation under the second canceled relation; no stop written'),
 dict(written=r'\overline m',expansion='même',places='main line15, M1214; expansion is kept out of source text'),
 dict(written='long',expansion='longueur',places='final length expression'),
 dict(written=r'\operatorname{Ker}',expansion='kernel; the written operator remains tentative',places='first canceled display'),
]

audit_boxes=[]
def audit(kind,coords,reading):
    audit_boxes.append(dict(box=f'B{len(audit_boxes)+1:02d}',kind=kind,coords=coords,reading=reading))
audit('handwritten number',[785,30,840,75],r'\mspage{38}')
audit('C/H word disagreement',crops['P01']['box'],"s'avère")
audit('insertion',crops['P02']['box'],r'\deleted{élément de}\inserted{homomorphisme}')
audit('formula with doubt',crops['P03']['box'],r'(11)\qquad T_\ell(\simeq H_1(\eta,\mathbb Z_\ell))\longrightarrow\unsure{T|\mathbb T}_\ell^I/T_\ell')
audit('C/H word disagreement',crops['P04']['box'],r'cas \unsure{envisagé|envisage}, $\nu\geqslant2$ (et traiter séparé-')
audit('handwritten number',crops['P05']['box'],r'ment le cas $\nu=1$).')
audit('struck passage',crops['P06']['box'],r'\deleted{[On va faire des}')
audit('struck passage',crops['P07']['box'],r'\deleted{calculs intrinsèques, en}')
audit('formula with doubt',crops['P08']['box'],r'\deleted{\unsure{\operatorname{Ker}}(\mathcal J^\bullet_{U/S}\longrightarrow\mathcal J^\bullet_{X/S})\simeq G_m^I/G_m}')
audit('formula with doubt',crops['P09']['box'],r'\deleted{H_1(\mathcal U,\mathbb Z_\ell)\simeq H_1(\mathcal J^1_{U/S},\mathbb Z_\ell)\underset{\substack{\text{isom}\\\text{de Kummer}}}{\simeq}\lim_{\longleftarrow}\deleted{\unsure{\ell^n}}{}_{\ell^n}(\mathcal J^0_{U/S})}')
audit('struck passage',crops['P10']['box'],r"\deleted{On considère donc l'image inverse par}")
audit('struck passage',crops['P11']['box'],r'\deleted{$\eta\longrightarrow\mathcal J^1_{U/S}$ composé de $\eta\longrightarrow U\longrightarrow\mathcal J^1_{U/S}$)}')
audit('struck passage',crops['P12']['box'],r'\deleted{des isogénies}')
audit('struck passage',crops['P13']['box'],r'Soit \deleted{\unsure{q}} $x=g_{i_0}(s)$,')
audit('C/H word disagreement',crops['P14']['box'],r'A=\underline O_{X,x},')
audit('C/H word disagreement',crops['P15']['box'],"l'hom")
audit('lower confidence departure',crops['P16']['box'],r'de $\overline m$ $\mathcal J_f$')
audit('handwritten number',[275,2200,485,2335],r'g_{i_0}\neq f,')
audit('formula with doubt',crops['P18']['box'],r'Soit $\mu=\operatorname{long}V/g_{i_0}^*(\mathcal J_f)\ \deleted{\unsure{=}}$. ,')
audit('C/H word disagreement',crops['P19']['box'],'cet entier')
audit('handwritten number',crops['P20']['box'],r'\margin{76}')
audit('handwritten number',[280,1725,405,1870],r'\mathcal J_{i_0}')
audit('handwritten number',[905,1710,1105,1840],r'A\xrightarrow{g_{i_0}^*}V')
audit('handwritten number',[1375,1685,1560,1815],r'g_{i_0}')
audit('handwritten number',[800,2015,1110,2160],r'g_{i_0}^*(\mathcal J_f)')

coverage={
 1:('editorial page marker','The scan77 marker and H editorial page notation are outside source prose; autograph38 is preserved.'),
 2:('editorial page marker','H de l\x27auteur is editorial. The visible header is38.'),
 3:('material; P01a','The apostrophe and accented verb support s\x27avère.'),
 4:('equivalent typography','Both witnesses represent the same three source dots before the closing parenthesis; C uses ldots and H the ellipsis character.'),
 5:('macro syntax only','H \\, is a spacing command after T_ell, not a source comma.'),
 6:('material; P03a','The H_1 argument has the local eta shape. The extra numerator T stroke is a separate certainty-only doubt.'),
 7:('material; P04a','The nu comparison is on the rising prose baseline. geq/geqslant angle alone is nonmaterial; the source angle is preserved with geqslant.'),
 8:('macro syntax only','H prose about the canceled passage is editorial. Actual cancellation scope is inventoried and transcribed in full.'),
 9:('material; P07a','Only the two low bodies of en are written after the comma.'),
 10:('material; P08a','The first raised J mark is a solid point; the C bullet|0 doubt is resolved locally without inventing a MARKS ID.'),
 11:('material; P08b','The second raised J mark is likewise a solid point, with the same full-formula evidence.'),
 12:('material; P09a','The first relation in the second canceled display has a wave over an unheaded bar; H supplies an arrowhead.'),
 13:('material; P09b','The isom / de Kummer annotation belongs physically below the second relation.'),
 14:('material; P09c','The left arrow belongs below lim; a separately canceled tentative ell^n cluster follows it. H omits that internal correction.'),
 15:('material; P09b','Independent parentheses and periods around the annotation are not present. The same annotation place is counted once.'),
 16:('material; P11a','The first canceled map-line symbol is eta, with small arch and curved right descender.'),
 17:('material; P11b/P11c','The second map-line symbol is eta. There is no independent opening parenthesis before composé; the visible closing parenthesis remains.'),
 18:('material; P13a','Surviving bowl and descending return support a tentative q within the deletion, rather than wholly unreadable ink.'),
 19:('material; P15a','No independent stop follows the m of hom.'),
 20:('equivalent typography','The one source prose dash is represented by C -- or H ---; the differing dash macro lengths are not counted separately.'),
 21:('material; P16a','M1214 resolves first to the written barred m; H expands it to même.'),
 22:('material; P18a','The final variable has a long mu descender and right return.'),
 23:('material; P19a','The opening c, low e and tall t give cet. The adjacent omitted point is separately recorded at P18b.'),
 24:('material; P20a','The small thin foliation76 is present at the lower left and retained as another hand.'),
}
diff_coverage=[dict(row=i,status=s,reason=e) for i,(s,e) in coverage.items()]

review=[
 r'The line through élément de crosses both words and stops after de; the replacement homomorphisme is raised above that phrase. Both scopes are retained as \deleted{élément de}\inserted{homomorphisme}.',
 'The large cancellation begins with the source opening bracket before On va faire des and includes calculs intrinsèques, both displays, the below-relation annotation, On considère donc l\x27image inverse par, the complete map/composé line and des isogénies. The later Je vais deviner and Soit paragraphs remain live.',
 'The dense local overwriting at Ker leaves its reading uncertain. Its strokes are described without assigning an unsupported older-letter chronology.',
 r'The internal canceled cluster after lim is preserved as \deleted{\unsure{\ell^n}} within the larger canceled display. The separate smaller left torsion index following it remains live relative to that local correction, while the whole display is globally canceled.',
 'The below-relation words isom / de Kummer are within the global cancellation. Their two-line physical placement is retained; they are not moved into a later parenthetical sentence.',
 'The long bent cancellation stroke before composé continues across that line and down toward des isogénies. It is not copied as an opening parenthesis. The source\x27s closing parenthesis remains.',
 r'The small canceled fragment after Soit remains \deleted{\unsure{q}}. No letter under the crossing is asserted as fully certain.',
 r'The last locally canceled sign remains \deleted{\unsure{=}}. Its crossing strokes stop before a detached dark point, followed farther right by a comma; both punctuation marks remain outside the deletion.',
]

report=dict(page=PAGE,scan=77,reader='reader_a',line_count=19,changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,notes=notes,check_events=[],hand=hand,notation=notation,abbreviations=abbreviations,audit_boxes=audit_boxes,diff_coverage=diff_coverage,deletion_insertion_review=review,open_issues=[
 'Six local uncertainties remain in place: numerator T form, final accent of envisagé, overwritten Ker, inner canceled ell^n, canceled q after Soit, and final canceled equals-like sign. Root reviewed and agreed to retain each.',
 'Root has viewed all20 saved crops and supplied the final local decisions. No unreviewed crop or remaining root decision is requested.'
],viewed=['page before C/H','top half','bottom half']+[p['path'] for p in manifest])

def restore(obj):
    if isinstance(obj,str): return obj.replace('\\x27',"'")
    if isinstance(obj,list): return [restore(x) for x in obj]
    if isinstance(obj,dict): return {k:restore(v) for k,v in obj.items()}
    return obj
report=restore(report)
(BASE/'readings'/f'{PAGE}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

expected=[r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t')]
assert [d['id'] for d in decisions]==expected==['M1214']
assert tex.count('{')==tex.count('}')
assert tex.count(r'\unsure')==len(doubts)==6
assert len(diff_coverage)==24
assert all((BASE/c['crop']).exists() for c in changes)
assert len({c['id'] for c in changes})==len(changes)
assert all(0<=b['coords'][0]<b['coords'][2]<=1680 and 0<=b['coords'][1]<b['coords'][3]<=2365 for b in audit_boxes)
print(json.dumps(dict(page=PAGE,changes=len(changes),against_C=sum(c['against_C'] for c in changes),against_H=sum(c['against_H'] for c in changes),decisions=len(decisions),doubts=len(doubts),crops=len(manifest),audit_boxes=len(audit_boxes)),indent=2))
