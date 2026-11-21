from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/8759b8008681')
PAGE = '149_scan136'
OUT = ROOT / 'work/reports' / PAGE
PACKET = ROOT / 'packets' / PAGE
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
draft = C
replacements = [
    (r'\unsure{habile|arbitraire}', 'habile'),
    (r'\unsure{autom.}', 'autom'),
    (r"$D_J=D_i$} connexe", r"$D_J=D_i$} est connexe"),
    (r'\unsure{\kappa_i|k_i}', r'\kappa_i'),
    (r'\uline{et}', 'et'),
    (r'\unsure{\tilde U_x|U_x}', r'\tilde U_x'),
    (r'\unsure{\tilde U_x}', r'\tilde U_x'),
    (r'\unsure{géom.}', 'géom'),
    (r'\unsure{laissent}', 'laissent'),
    (r'\unsure{les hom}', 'les hom'),
    (r'\inserted{\unsure{extérieurs}}', r'\inserted{extérieurs}'),
    (r"\unsure{\bar D_{J'}}", r"\bar D_{J'}"),
    (r'\varnothing', r'\phi'),
]
for old, new in replacements:
    assert draft.count(old) == 1, (old, draft.count(old))
    draft = draft.replace(old, new)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'draft.tex').write_text(draft)

boxes = {
 'P00':[408,54,716,145], 'P01':[923,112,1282,226],
 'P02a':[1331,145,1564,224], 'P02b':[537,242,825,311],
 'P03':[395,478,538,599], 'P04':[677,574,1658,686],
 'P05':[255,677,1580,797], 'P06':[251,775,1594,909],
 'P07':[225,867,1646,1078], 'P08':[587,1024,1003,1175],
 'P09':[250,1189,1660,1496], 'P10':[239,1488,1130,1640],
 'P11':[271,1620,1658,1848], 'P12':[270,1798,1650,2122],
 'P13':[16,20,511,895], 'P14':[14,934,553,1955],
 'P15':[273,2042,1657,2349], 'P16':[16,2287,114,2348],
}
def crop(p): return f'crops/{PAGE}_{p}.png'
changes=[]
def ch(i, p, place, c, h, final, evidence, kind, cat, ac=False, ah=True,
       confidence='high', marked=False, consequential=False):
    assert c == '' or c in C, ('C quotation',i,c)
    assert h == '' or h in H, ('H quotation',i,h)
    assert final == '' or final in draft, ('final quotation',i,final)
    changes.append(dict(id=i,place=place,c=c,h=h,final=final,evidence=evidence,
      crop=crop(p),box=boxes[p],confidence=confidence,kind=kind,
      against_c=ac,against_h=ah,marked_in_h=marked,
      consequential=consequential,error_category=cat))

ch('P00','P00','Opening of the main text',
   'éléments dont',r'\struck{\ill{}} éléments dont','éléments dont',
   'The accented initial é, tall looped l and connected remainder of éléments lie on the live baseline. The separate slanting stroke at their lower left continues the oblique margin writing; it does not cross a preceding word. H supplies an independent struck illegible item where no such item is visible.',
   'text not on the page',9,marked=True)
ch('P02a','P02a','End of the second main line',
   '--- on','—','--- on',
   'After the separate horizontal dash are a closed o and a long, low n with a terminal downward return. This on is separate from the next line’s verb and is omitted in H.',
   'omission',3)
ch('P02b','P02b','Beginning of the following main line',
   'voit que',r'\uncertain{ont} que','voit que',
   'The compressed verb has an initial rounded down-and-up v form, a low connected middle cluster and a tall final t with a distinct cross stroke; que begins separately with its descending q. Read with the independently visible on at the preceding line end (P02a), the connected middle strokes support voit. The o/i are not widely separated, so confidence is medium.',
   'misread word',2,confidence='medium',marked=True)
ch('P03','P03','Overwritten superscript of the main extension group',
   r'$\mathcal E_{U/K}^{\unsure{\bar L|\bar K}}$',
   r'\struck{\ill{}} $\mathcal{E}_{U/K}$',
   r'$\mathcal E_{U/K}^{\unsure{\bar L|\bar K}}$',
   'The bar is separate and secure above a repeatedly retraced capital. An upright and broad lower foot favor L, while a diagonal branch remains entangled with the rewriting. The entire body cannot be separated as L or K. The overwritten ink is a superscript of E_{U/K}, not a separate struck word before it, and must not be omitted.',
   'misread symbol or index',1,confidence='low',marked=True,consequential=True)
ch('P04a','P04','Index following différents',
   r'différents $\alpha$',r'différents $x$',r'différents $\alpha$',
   'The detached small symbol has a closed left loop with a rightward crossing tail, the alpha form also used in D_{J,alpha}; it is not the two diagonal strokes of x.',
   'misread symbol or index',1,consequential=True)
ch('P04b','P04','Manner of making the choices',
   r'\unsure{habile|arbitraire}', 'cohérente,', 'habile',
   'The short word ends with a dotted i, a tall l and a low e; its compact preceding joined body fits hab-. It lacks the extra repeated r/t strokes and length required by arbitraire, and lacks the long cohérent- body of H. C’s first candidate is retained with the doubt resolved; the crowded opening keeps the reading at medium confidence.',
   'misread word',2,ac=True,confidence='medium')
ch('P05a','P05','Continuation after habile',
   'telle, que maintenant les',r'qui mainten\supplied{ant}',
   'telle, que maintenant les',
   'The initial word has a crossed t followed by two tall l loops and terminal e, then a visible comma. The next word begins with descending q, not an i-ending qui. Maintenant has the complete connected ending on the page, and the following les has a tall initial l; ant is not an editorial completion.',
   'misread word',2)
ch('P05b','P05','Abbreviation before extérieurs',
   r'\unsure{autom.}',"l'incertitude",'autom',
   'The short body has a rounded a/u opening, a tall crossed t, and low joined o/m strokes. There is no separate stop after m and no following letters of a long noun. The crop resolves C’s abbreviation while removing its unsupported period.',
   'abbreviation expanded or spelling modernised',8,ac=True)
ch('P05c','P05','Ending of the adjective after autom',
   'extérieurs','extérieure','extérieurs',
   'The word has the crossed x, tall t and accented interior vowel, followed by a final returning s stroke. There is no additional e loop after the r before that terminal return.',
   'misread word',2)
ch('P06','P06','Group and relative clause after autom extérieurs de',
   r"$\pi_{U/K}^{\bar L}$ qui expriment l'indétermination dans",
   r"\uncertain{celle}, qui exprime l'indétermination dans $\pi_{U/K}^{\overline{L}}$",
   r"$\pi_{U/K}^{\bar L}$ qui expriment l'indétermination dans",
   'The line starts with pi, U/K below it, and a barred angular L above; there is no word celle. Immediately after the group are a descending q in qui and an e-x-p opening in expriment, with the plural nt ending. The long indétermination follows its own l-apostrophe. H reverses the group’s place and changes the relative clause.',
   'misread word',2,marked=True,consequential=True)
ch('P07a','P07','Words following the inline reference',
   'soient ceux provenant',r'\uncertain{ici} \uncertain{seulement} aux produits',
   'soient ceux provenant',
   'The first word has the separate dot over i and the terminal t. Ceux ends in a small crossed x. Provenant begins with a long descending p, followed by low r/o/v strokes and a final tall t. There is no produits sequence or separate aux.',
   'misread word',2,marked=True)
ch('P07b','P07','Placement of handwritten (39)',
   'dans (39)',r'(39) \qquad','dans (39)',
   'The parenthesized digits stand at the left of the prose line before soient. The second digit has a small loop above a downward stem, giving 9; the first is 3. The succeeding displayed group map is lower on the page and has no repeated 39 at its left. H has moved this inline reference into the display.',
   'insertion or placement',6,consequential=True)
ch('P09a','P09','Singleton case and its description',
   r'$J=\{i\}$ est particulièrement \unsure{simple}',
   r'$J = \{i\}$ est particulier',
   r'$J=\{i\}$ est particulièrement \unsure{simple}',
   'After the dotted i inside the braces, the adjective continues through a long joined -ment ending beyond particulier. The next main-line word is the separate wrapped simple candidate, with a descending p and tall l, but crossing marginal strokes keep C’s doubt on that word. H omits the separate word and truncates particulièrement.',
   'misread word',2,confidence='medium')
ch('P09b','P09','Cancelled wording preceding the replacement clause',
   r'\deleted{chaque composante \unsure{conn.}}',
   r'\struck{\uncertain{lorsque}}',
   r'\deleted{chaque composante \unsure{conn.}}',
   'A horizontal cancellation traverses the entire lower sequence: chaque has the tall h and long descending q; composante has an initial rounded c/o group, descending p and later tall t. The final abbreviated body is crossed and remains conn. under doubt. The line is longer than H’s lorsque and includes composante before the replacement, not after its D_i.',
   'deletion state (struck given live or live given struck)',7,confidence='medium',marked=True)
ch('P09c','P09','Extent of the interlinear replacement',
   r"\inserted{dans ce cas d'ailleurs $D_J=D_i$}",
   r"\add{dans} ce cas d'ailleurs $D_J = D_i$ \struck{\uncertain{composante}}, \add{et}",
   r"\inserted{dans ce cas d'ailleurs $D_J=D_i$}",
   'The entire line above the cancellation is inserted: dans has a tall d, the separate ce and cas are visible, d’ailleurs has its apostrophe and paired tall l strokes, and D_J = D_i ends the same raised line. There is no separately added et here. The ordinary live et belongs after connexe on the next main line.',
   'insertion or placement',6,marked=True,consequential=True)
ch('P09d','P09','Live word before connexe',
   'connexe, et on trouve des hom',r'\uncertain{connexe}, et on trouve des hom',
   'est connexe, et on trouve des hom',
   'At the lower left of the main paragraph, before connexe, a low e/s sequence ends in a distinct raised t. It sits on the main baseline and is not part of the diagonal marginal text or the raised insertion. Both witnesses omit this live est.',
   'omission',3,ac=True,marked=True,consequential=True)
ch('P10','P10','Label of the map numbered (40)',
   r'T\xrightarrow{\unsure{\kappa_i|k_i}}\pi_{U/K}^{\bar L}',
   r'T \xrightarrow{\ \kappa_i\ } \pi_{U/K}^{\overline{L}}',
   r'T\xrightarrow{\kappa_i}\pi_{U/K}^{\bar L}',
   'The arrow has two converging head strokes and a single shaft. Its label has a short upright and two branches occupying the same letter height, unlike the taller ascender of k(x) in P01; a dotted i is written below at the right. The same short-stemmed label recurs in P11. This resolves C toward kappa_i; the hand remains k-like, so the certainty resolution is medium. The source 40, T, pi, U/K and barred L are all present.',
   'misread symbol or index',1,ac=True,ah=False,confidence='medium',consequential=True)
ch('P11a','P11','Abbreviations after a priori',
   'mod autom',r'mod.\ automorphismes','mod autom',
   'Mod ends in a compact upright d and autom ends in low m strokes; neither has a separate period. The space after m is blank before intérieurs, so the additional orphismes of H is not written.',
   'abbreviation expanded or spelling modernised',8)
ch('P11b','P11','Word at the following line start',
   'près',r'\uncertain{\ill{}}','près',
   'The word begins with a descending p, then short r, an accented low vowel and terminal s. These strokes form près before the separate dash and are not physically illegible.',
   'readable ink left as \\ill{}',5,marked=True)
ch('P11c','P11','Phrase after près',
   '--- donc en fait',r'— dans un \uncertain{fait}','--- donc en fait',
   'Donc has a tall looped d, rounded o/n body and open c; the next short group is en. Fait has its long descending f, low a/i and terminal crossed t. H’s dans un changes the two visible words.',
   'misread word',2,marked=True)
ch('P11d','P11','Underlined term split over the main lines',
   r'\uline{hom} \uline{extérieur}',r'hom \emph{extérieur}',
   r'\uline{hom} \uline{extérieur}',
   'A separate straight stroke lies below hom at the end of the line; the next line’s extérieur also has its own underline, visible in P12. H’s treatment of extérieur is an equivalent emphasis convention, but the underline under hom is absent in H.',
   'other',10)
ch('P12a','P12','First cancelled candidate after qui est',
   r'\deleted{\unsure{invariant}}',r'\struck{\ill{}}',
   r'\deleted{\unsure{invariant}}',
   'A compact cancelled word has the initial short upright and a dotted interior stroke, with a low joined body ending in a taller return. Invariant remains a candidate because the horizontal strike obscures several interior joins; it is not resolved. H gives no candidate at all for this visible word.',
   'readable ink left as \\ill{}',5,confidence='low',marked=True)
ch('P12b','P12','Second cancelled candidate',
   r"\deleted{stable par l'opération}",
   r'\struck{\ill{} par \uncertain{opération}}',
   r"\deleted{stable par l'opération}",
   'The long straight cancellation crosses stable, with its initial s/t and tall b/l bodies, then par with a long p descender, then l’opération with its tall l, apostrophe, descending p and crossed t. This complete struck phrase is below the live compatible wording and before its continuation ext. de; H relocates its surviving words after les opérations.',
   'insertion or placement',6,marked=True,consequential=True)
ch('P12c','P12','Stroke below live et',
   r'\uline{et}','et','et',
   'The short stroke below et sits directly over the D_{J\'} in the inserted parenthesis beneath this line. A matching short stroke below sur is over its second D_J. The paired bars belong to those two D symbols; treating the first again as an underline of et duplicates one stroke. C’s underline is removed.',
   'other',10,ac=True,ah=False)

def margin_block(text, beginning):
    m = re.search(r'\\margin\{' + re.escape(beginning) + r'.*?\\ldots\}', text, re.S)
    assert m
    return m.group()
C_upper=margin_block(C,'de façon plus précise')
D_upper=margin_block(draft,'de façon plus précise')
C_lower=margin_block(C,'Mais a priori')
D_lower=margin_block(draft,'Mais a priori')
H_margin=next(line for line in H.splitlines() if line.startswith(r'\marginal{'))
ch('P13','P13','Upper oblique marginal note and its group diagram',
   C_upper,H_margin,D_upper,
   'The note begins de façon plus précise with a long descending f and the c-cedilla in façon; choix has tall ch and final x. The source has the short rev. with a separate dot, followed by the complete universel. Above the first U_x is a distinct two-sided wavy tilde, resolving M0223. En implique has the descending p and following tall l; un de K is on the next line. Et on suppose and que c’est remain live prose. The small word after avec and the ending of rigidification(s) are not forced. Choisit has ch, a dotted i and final t; au dessus de is repeated before the later barred K. The lower lines visibly contain rev. universel de k(x), Ces choix étant faits, on a. In the terminal diagram the lower U_x has a separate wavy mark, resolving M0226; the tiny superposed upper covering mark remains doubtful. The connecting arrow has a visible right head and ends at E_K with barred K. Three separated dots follow. H replaces most of these readable spans by illegibility and fragmentary guesses. The image is rotated for inspection only; the coordinates are original coordinates.',
   'readable ink left as \\ill{}',5,ac=True,marked=True,confidence='medium',consequential=True)
ch('P14','P14','Lower oblique marginal note',
   C_lower,'',D_lower,
   'The capital M and dotted i identify Mais; a priori is followed by ils sont par voie. Géom has a descending g, accented e and rounded o/m body, but no secure isolated final period. Mod autom remain short forms. The first pi expression is underlined. A straight stroke crosses extérieures after opérations; its internal lettering remains doubtful. The later laissent has a tall looped l and a low joined -aissent body, while les hom has the raised l and h and two low final m humps; these two cramped words are resolved at medium confidence. The inserted extérieurs has crossed x, tall t and visible final r/s, and is connected to the position after hom by a bent leader, not a punctuation mark. The remaining lines read en tenant compte de l’action extérieure, the quoted cyclotomique with descending y and tall l/t, and E_K with barred K sur T^J followed by three dots. H supplies no separately identifiable transcription of this second note.',
   'omission',3,ac=True,confidence='medium',consequential=True)
ch('P15a','P15','Beginning of the wholly cancelled bottom paragraph',
   r"Si \unsure{on a} $J'\supset J$",r"Si $J' \supset J$",
   r"Si \unsure{on a} $J'\supset J$",
   'Between Si and the primed J are two small low groups under the large diagonal cancellation. They support the existing on a candidate but do not expose every letter. Their presence is retained under doubt; H omits the groups. The prime on J and the superset sign are separately visible.',
   'omission',3,confidence='low')
ch('P15b','P15','Inserted parenthesis within the cancelled bottom paragraph',
   r"\inserted{(\unsure{donc|d'où} $\bar D_{J'}\subset\bar D_J$),}",'',
   r"\inserted{(\unsure{donc|d'où} $\bar D_{J'}\subset\bar D_J$),}",
   'The smaller line above the original i.e. parenthesis is a separate insertion. Both D bodies have overbars, with J-prime below the first and J below the second; the connecting sign is an open inclusion curve. The word at its opening is crossed by a large diagonal and remains donc|d’où. Its parentheses and following comma belong to the insertion, which is itself included in the later whole-paragraph cancellation. H absorbs the subset relation into its sole i.e. parenthesis and omits this revision layer.',
   'insertion or placement',6,confidence='medium',consequential=True)
ch('P15c','P15','Old nonemptiness parenthesis with nested cancellation',
   r"$\unsure{\bar D_{J'}}\deleted{\unsure{\cap D_J}}\ne\varnothing$",
   r"$D_{J'} \subset D_J$",
   r"$\bar D_{J'}\deleted{\unsure{\cap D_J}}\ne\phi$",
   'The first surviving D has a separate overbar and its lowered J has a prime; this resolves C’s doubt on that complete group. Several short strokes cancel the following intersection candidate, which remains unsure. To its right, two short horizontal strokes crossed by an oblique make the inequality. The empty-set glyph has a closed loop with a descending upright passing through it: phi, not a bare slashed circle. H’s main transcription conflates this old nonemptiness condition with the inserted inclusion above; its editorial variant does not restore the bars or the nested cancellation.',
   'misread symbol or index',1,ac=True,confidence='medium',consequential=True)
ch('P15d','P15','Chosen component inside the bottom cancellation',
   r"$\unsure{\bar D_{J',\alpha'}}$ de $D_{J'}$",
   r"$D_{J',\alpha'}$ \ill{} de $D_{J'}$",
   r"$\unsure{\bar D_{J',\alpha'}}$ de $D_{J'}$",
   'The large component D has a clear short bar above it and lower J/alpha material. The primes are crowded by the large crossing stroke, so C’s full-group uncertainty is retained. At the far right de is the final word of the line; the next line starts D_{J\'}. There is no separate additional word between the component symbol and de for H’s illegibility slot.',
   'misread symbol or index',1,confidence='medium',marked=True,consequential=True)
ch('P15e','P15','End of the cancelled bottom paragraph',
   'dans une comp. conn.',r'dans une \uncertain{seule} comp.\ conn.',
   'dans une comp. conn.',
   'After the tall d of dans, the low three-stroke une is followed directly by the c/o/m body and long p descender of comp. and then conn. No s/l/e letter group lies between une and comp.; the intervening diagonal is part of the large cancellation, not the word seule.',
   'text not on the page',9,marked=True)
ch('P16','P16','Thin foliation at the lower left',
   r'\margin{135}','',r'\margin{135}',
   'The separate thin number has a single angled 1, a double-curved 3, and a final 5 with a short upper stroke and curved lower bowl. The brown spots are not digits or punctuation. Its thin, lighter hand is not assigned confidently to the main writer.',
   'omission',3)

marks=list(csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t'))
decision_specs=[
 ('P01','undecided',r'\unsure{\mathrel{\text{---}}|\longrightarrow}', 'A single horizontal connector ends in an upward thickening. There is no securely separable lower branch of a two-sided arrowhead; retain dash|arrow while keeping both complete flanking groups.', 'low'),
 ('P03','undecided',r'\unsure{\bar L|\bar K}', 'The overbar is distinct, but the body below is repeatedly retraced. Upright/foot strokes favor L while a diagonal branch can belong to K or the rewriting.', 'low'),
 ('P04','first','habile', 'The compact word ends dotted i, tall l, low e and has a short hab- body. It is too short and lacks the repeated r/t structure of arbitraire. The first candidate is resolved with medium confidence.', 'medium'),
 ('P05','other','autom', 'Rounded a/u, tall t and low o/m strokes form the complete abbreviation. No separate dot follows m; resolve the letters and omit the unsupported stop.', 'high'),
 ('P09','undecided',r'\unsure{simple}', 'A wrapped word has the descending p and tall l expected in simple, but compressed initial strokes intersect the oblique marginal writing. The inspected crop does not make every letter secure.', 'medium'),
 ('P10','first',r'\kappa_i', 'The label has a short upright and two branches at letter height, without the taller Latin k ascender seen in k(x); the dotted lower i is separate. The same form recurs in the prose. The whole labelled map has been checked.', 'medium'),
 ('P13','first',r'\tilde U_x', 'A separate two-sided wavy stroke stands over the complete U, with a small x at its lower right. It is not an accidental continuation from the preceding word.', 'high'),
 ('P13','undecided',r'\unsure{des}', 'After avec there is a tall d-like body, but the following compressed short strokes do not separate e and s securely from adjacent main-line ink.', 'medium'),
 ('P13','undecided',r'\unsure{rigidifications|rigidification}', 'The rigidification body is readable, with the long g and tall d/f/t strokes, but the tiny ending before the closing parenthesis does not securely distinguish a final s from a terminal pen return.', 'medium'),
 ('P13','first',r'\tilde U_x', 'In the left diagram object, the lower U has a distinct wavy mark over it and a lowered x. The arrow and the entire right object E_K with barred K have also been inspected.', 'high'),
 ('P13','undecided',r'\unsure{\tilde{\tilde U}_x}', 'The upper U_x is visible, with tiny stacked wavy strokes above it; their tight meeting with the line above prevents a secure count and separation of both tildes. Retain the double-tilde candidate under doubt.', 'medium'),
 ('P14','other','géom', 'The short form has a descending g, accented e and compact rounded o/m strokes. A separate terminal stop cannot be distinguished securely from the adjacent crossing/leader, so none is supplied.', 'medium'),
 ('P14','first','laissent', 'A tall looped l opens the word, followed by low joined a/i/ss/en material and a raised final t. The cramped joins make the resolved reading medium confidence.', 'medium'),
 ('P14','first','les hom', 'The first word has a raised l and connected e/s ending; the next begins with a tall h, rounded o and low m humps. The groups are visibly separated. Resolve at medium confidence.', 'medium'),
 ('P14','first','extérieurs', 'The inserted word has crossed x, tall t, accented interior vowel and a visible final r/s return. A bent leader carries it to after hom; that leader is not punctuation.', 'high'),
]
assert len(marks)==len(decision_specs)==15
decisions=[]
for m,(p,d,r,e,conf) in zip(marks,decision_specs):
    assert r in draft
    decisions.append(dict(id=m['id'],cote='149',scan='136',decision=d,reading=r,evidence=e,crop=crop(p),box=boxes[p],confidence=conf))

inventory=[]
def inv(i,kind,position,words,hand='his hand'):
    inventory.append(dict(scan=PAGE,sheet_kind='text',hand=hand,element=i,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('E01','text','Main column, top to y1050','éléments dont l’image ... (39) soient ceux provenant ...')
inv('E02','display','Main column, about y1050–1175',r'\mathcal E_{D_{J,\alpha}}^{\tilde D_{J,\alpha}}\longrightarrow\mathcal E_K^{\bar K}')
inv('E03','text','Main column, y1200–1496',r'J=\{i\} est particulièrement ... est connexe, et on trouve des hom')
inv('E04','deletion','Under the singleton replacement line, P09','chaque composante conn. (last abbreviation doubtful)')
inv('E05','insertion','Above E04, P09',r"dans ce cas d'ailleurs D_J=D_i")
inv('E06','display','Main column, y1488–1640',r'(40) T\xrightarrow{\kappa_i}\pi_{U/K}^{\bar L}')
inv('E07','text','Main column, y1620–2122','déterminés a priori mod autom intérieurs près ...')
inv('E08','deletion','Below extérieur, P12','invariant (doubt retained)')
inv('E09','deletion','Below compatible, P12',"stable par l'opération")
inv('E10','margin note','Upper oblique left note, [16,20,511,895]','de façon plus précise, le choix d’un rev. universel ...')
inv('E11','diagram','At the foot of E10, P13',r'\mathcal E_{\tilde U_x}^{\unsure{\tilde{\tilde U}_x}}\longrightarrow\mathcal E_K^{\bar K} ...')
inv('E12','margin note','Lower oblique left note, [14,934,553,1955]','Mais a priori ils sont par voie géom ...')
inv('E13','deletion','Within E12, after opérations','extérieures (doubt retained)')
inv('E14','insertion','Within E12, bent leader to after hom','extérieurs')
inv('E15','deletion','Entire bottom paragraph, y2090–2349',r"Si on a J'\supset J ... elle est contenue dans une comp. conn.")
inv('E16','insertion','Raised line inside E15, y2060–2130',r"(donc|d'où \bar D_{J'}\subset\bar D_J),")
inv('E17','deletion','Old parenthesis inside E15, P15',r'\cap D_J (doubt retained beneath local crossing)')
inv('E18','margin note','Bottom-left, [16,2287,114,2348]','135','thin, lighter foliation hand; not securely identified')

audit=[]
def ab(i,p,kind,reading,xy=None):
    audit.append(dict(box=i,kind=kind,xyxy=xy or boxes[p],reading=reading))
ab('B01','P00','C/H different words','éléments')
ab('B02','P01','doubtful formula',r'$\mathcal E_{k(x)}^{\overline{k(x)}}\unsure{\mathrel{\text{---}}|\longrightarrow}\mathcal E_K^{\bar K}$')
ab('B03','P02a','C/H different words','--- on')
ab('B04','P02b','C/H different words','voit que')
ab('B05','P03','doubtful formula; struck passage; C/H different words',r'$\mathcal E_{U/K}^{\unsure{\bar L|\bar K}}$')
ab('B06','P04','C/H different words; less than high confidence departure',r"$\alpha$ d'une façon habile",[963,574,1658,686])
ab('B07','P05','C/H different words','telle, que maintenant les autom extérieurs de')
ab('B08','P06','C/H different words',r"$\pi_{U/K}^{\bar L}$ qui expriment l'indétermination dans")
ab('B09','P07','C/H different words; handwritten number',"(39) soient ceux provenant des éléments de l'image de")
ab('B10','P08','C/H different words',r'$\mathcal E_{D_{J,\alpha}}^{\tilde D_{J,\alpha}}\longrightarrow\mathcal E_K^{\bar K}.$',[587,1024,1070,1175])
singleton=re.search(r'\$J=.*?des hom',draft,re.S).group()
ab('B11','P09','insertion; struck passage; C/H different words',singleton,[205,1189,1660,1505])
ab('B12','P10','doubtful formula; handwritten number; less than high confidence departure',r'\tag{40} T\xrightarrow{\kappa_i}\pi_{U/K}^{\bar L},')
ab('B13','P11','C/H different words',r'déterminés a priori mod autom intérieurs près --- donc en fait $\kappa_i$ est un \uline{hom}')
ab('B14','P12','struck passage; C/H different words',r"\uline{extérieur} bien déterminé, qui est \deleted{\unsure{invariant}} \deleted{stable par l'opération} compatible avec les opérations ext. de $\mathcal E_K^{\bar K}$ sur $T$, et sur $\pi_{U/K}^{\bar L}$.")
ab('B15','P13','margin note; doubtful formula; C/H different words; less than high confidence departure',D_upper)
ab('B16','P14','margin note; insertion; struck passage; C/H different words; less than high confidence departure',D_lower)
bottom=next(line for line in draft.splitlines() if line.startswith(r'\deleted{Si '))
ab('B17','P15','insertion; struck passage; doubtful formula; C/H different words; less than high confidence departure',bottom)
ab('B18','P16','margin note; handwritten number','135')

doubts=[
 dict(place='P01 main residue-field group connector',reading=r'\unsure{\mathrel{\text{---}}|\longrightarrow}',alternatives='dash | right arrow',confidence='low',reason='The right end turns upward, but a separate lower arrowhead branch is not secure.'),
 dict(place='P03 overwritten group superscript',reading=r'\unsure{\bar L|\bar K}',alternatives='barred L | barred K',confidence='low',reason='The overbar is clear; multiple retraced strokes obscure the capital’s original branch and foot.'),
 dict(place='P09 wrapped adjective',reading=r'\unsure{simple}',alternatives='simple; no secure different word',confidence='medium',reason='The p/l body is supported, but the compressed initial strokes meet the oblique note and are not all separated.'),
 dict(place='P09 last cancelled abbreviation',reading=r'\unsure{conn.}',alternatives='conn.; terminal letters/stop partly crossed',confidence='medium',reason='A cancellation covers the low final letter group; no certainty resolution is made.'),
 dict(place='P12 first cancelled predicate',reading=r'\unsure{invariant}',alternatives='invariant; interior letters obscured',confidence='low',reason='The strike traverses the connected middle letters, so not every letter can be read independently.'),
 dict(place='P13 after avec',reading=r'\unsure{des}',alternatives='des; final short strokes unresolved',confidence='medium',reason='The d-like opening is visible but the ending lies among cramped strokes from adjacent writing.'),
 dict(place='P13 noun before closing parenthesis',reading=r'\unsure{rigidifications|rigidification}',alternatives='plural | singular',confidence='medium',reason='The final s cannot be separated securely from the terminal pen return; grammar does not decide it.'),
 dict(place='P13 upper covering label of the diagram',reading=r'\unsure{\tilde{\tilde U}_x}',alternatives='double tilde U_x; precise stacked covering marks uncertain',confidence='medium',reason='The small superposed wavy marks crowd the preceding line; the entire two-node formula is retained and audited.'),
 dict(place='P14 cancelled adjective',reading=r'\unsure{extérieures}',alternatives='extérieures; struck interior letters remain uncertain',confidence='medium',reason='A straight cancellation crosses the interior of this word, distinct from the live later insertion extérieurs.'),
 dict(place='P15 words after Si',reading=r'\unsure{on a}',alternatives='on a; both low groups partly crossed',confidence='low',reason='The large diagonal traverses the short word bodies; their presence is visible but every letter is not.'),
 dict(place='P15 inserted connective',reading=r"\unsure{donc|d'où}",alternatives="donc | d'où",confidence='medium',reason='The opening d and subsequent low strokes are crossed by the large cancellation; the apostrophe/accent question remains unresolved.'),
 dict(place='P15 nested cancelled intersection',reading=r'\unsure{\cap D_J}',alternatives='intersection with D_J; inner strokes obscured',confidence='low',reason='Several short cancellation strokes and a large diagonal cover the operator and part of D_J.'),
 dict(place='P15 selected component symbol',reading=r"\unsure{\bar D_{J',\alpha'}}",alternatives='barred D with J-prime, alpha-prime; primes crowded',confidence='medium',reason='The bar and large D are clear, but the small primes remain entangled with the diagonal cancellation.'),
]
notes=[
 dict(id='N01',text='The continuing main argument says that the relevant elements are conjugate for x varying in a connected component D_{J,alpha}, and that choices can make the exterior-automorphism indeterminacy in (39) come from the displayed component extension group. This reports the manuscript’s assertion; no theorem has been independently established here.'),
 dict(id='N02',text='For J={i}, the author inserts “dans ce cas d’ailleurs D_J=D_i” over cancelled wording, followed by the live “est connexe”. Formula (40) gives the map labelled kappa_i from T to pi_{U/K}^{bar L}. The following claim is that its exterior homomorphism is well determined and compatible with the indicated exterior operations. The source’s “mod autom intérieurs près” is retained without stylistic repair.'),
 dict(id='N03',text='The upper margin explains choices of universal covers over the fixed barred K and ends in a two-object group diagram. The lower note qualifies the geometric definition modulo inner automorphisms and discusses invariance of the exterior homomorphisms with the exterior “cyclotomique” action on T^J. The tiny covering superscript and two small word endings remain paleographic doubts; their intended mathematical values have not been supplied.'),
 dict(id='N04',text='The entire last paragraph is cancelled by large crosses. Within it, a raised inclusion of barred D strata and a locally cancelled intersection remain separately visible revision layers. The original nonemptiness parenthesis uses the phi-shaped empty-set sign. The final sentence stops after “une comp. conn.” on this sheet; nothing is completed from an expected continuation.'),
 dict(id='N05',text='The handwritten (39) is an inline reference in the prose, while (40) labels the following displayed map. The short strokes beneath “et” and “sur” are the two overbars of the inserted D symbols below, so et receives no underline. Thin foliation 135 is recorded separately without confidently assigning it to the main hand. No additional authorial question or demonstrable mathematical slip has been asserted from this page alone.'),
 dict(id='N06',text='All 18 saved first-pass crops were visually inspected. P13 and P14 are rotated inspection images of the two oblique notes; all recorded boxes remain coordinates in the original 1679 by 2359 scan. The full image and both supplied halves were each read once before these crop decisions. No OCR, external research, proof computation or TeX compilation was used.'),
]
events=[dict(statement_id=f'{PAGE}.N{i:02d}',type='carried as background without fault found',outcome='The corresponding source assertion was transcribed and its notation compared visually on this page. No independent proof, general theorem verification, or computational certificate was attempted.') for i in range(1,5)]
notation=[
 dict(form=r'\kappa_i',meaning=r'Label of the map T to \pi_{U/K}^{\bar L} in the singleton case.',evidence='P10 has the short-stemmed branched letter and lowered dotted i above the arrow; P11 repeats the same form in prose.'),
 dict(form=r'\phi',meaning="l'ensemble vide",evidence='P15 has a closed loop crossed by a descending upright after the inequality, matching the phi convention supplied in the page packet.'),
 dict(form=r'\tilde U_x',meaning='Base object named in the upper note’s universal-cover choice; the note also uses it below the left extension-group symbol.',evidence='P13 shows separate wavy tilde strokes over both these U forms. The upper covering label of the terminal diagram is still doubtful.'),
 dict(form=r'J=\{i\},\quad D_J=D_i',meaning='The singleton-index specialization stated on this page.',evidence='P09 main line contains J={i}; its raised replacement ends D_J=D_i.'),
 dict(form=r"\bar D_{J'},\ \bar D_J",meaning='Barred D expressions in the cancelled incidence paragraph; no definition is supplied on this page.',evidence='P15 has paired overbars in the raised inclusion and a separate bar over the first D in the old parenthesis.'),
]
abbreviations=[
 dict(form='autom',expansion='automorphismes'),dict(form='mod',expansion='modulo'),
 dict(form='hom',expansion='homomorphisme(s)'),dict(form='rev.',expansion='revêtement'),
 dict(form='géom',expansion='géométrique'),dict(form='ext.',expansion='extérieures'),
 dict(form='conn.',expansion='connexe(s)'),dict(form='comp.',expansion='composante'),
 dict(form='i.e.',expansion='id est'),
]
hand=[
 dict(habit='Long low n/m joins can compress whole word endings into nearly horizontal strokes.',places='P02a/b on / voit; P05 maintenant / autom; P11 donc en; P14 laissent / les hom',consistency='Repeated on this page, with tall ascenders and descenders providing the more discriminating evidence.',witness_errors='H merges the two-line on voit, replaces the autom clause, and changes donc en to dans un.'),
 dict(habit='The small kappa has a short upright with two branch strokes and can look like a small Latin k.',places='P10 arrow label; P11 inline kappa_i; compared with k(x) in P01',consistency='The two map-label forms agree; the k(x) stem is taller.',witness_errors='C retains kappa_i|k_i; resolved to kappa_i at medium confidence.'),
 dict(habit='Short forms autom and mod do not receive automatic abbreviation periods.',places='P05 and P11 main text; P14 margin',consistency='No separate stops follow the clear main occurrences; the stop after géom is also not secure and is not supplied.',witness_errors='C proposes autom. and géom.; H expands automorphismes and supplies mod.'),
 dict(habit='A bar belonging to a cramped inserted formula can lie immediately beneath an unrelated word in the line above.',places='P12/P15 paired bars below et and sur',consistency='The two corresponding D bodies below make the paired assignment clear.',witness_errors='C gives et an underline by reusing the first D overbar.'),
 dict(habit='Large diagonal crosses cancel an entire paragraph without erasing its earlier insertion and local-deletion layers.',places='P15',consistency='The raised inclusion, old nonemptiness condition and local intersection cancellation remain distinguishable within the later whole-paragraph cancellation.',witness_errors='H collapses the two parenthetical formula states and proposes an additional seule.'),
 dict(habit='The empty-set glyph is a loop with a long crossing upright, represented as phi.',places='P15 old nonemptiness condition',consistency='Consistent with the notation convention supplied in this page packet.',witness_errors='C renders varnothing; H uses emptyset in an editorial variant.'),
 dict(habit='Oblique marginal writing crosses the vicinity of main-line words and should not be converted into separate struck text.',places='P00 opening; P09 left edge; P13/P14 note borders',consistency='Both long marginal notes are distinct prose blocks with their own baselines.',witness_errors='H invents a struck illegibility before éléments and fails to recover most of the marginal prose.'),
 dict(habit='The thin foliation is materially lighter and narrower than the body hand.',places='P16 lower-left 135',consistency='Only this foliation instance assessed on the assigned page.',witness_errors='H omits the number; the reading does not assign the foliation confidently to the main writer.'),
]
dispositions=[
 'Editorial scan marker only; retain scanpage{136}, not an ink discrepancy.',
 'M0217/P01: dash|arrow remains undecided; no certainty-only collation row.',
 'P02a and P02b: separate on at the line end and voit que on the next line.',
 'P03: retain the overwritten barred L|K superscript as part of the group.',
 'P04a: alpha, not x.',
 'P04b and P05a: habile followed by telle,; no cohérente.',
 'P05a–P05c: complete maintenant and les autom extérieurs; autom without a stop.',
 'P06: no celle; pi-group precedes qui expriment.',
 'P06/P07a/P07b: qui expriment ... dans (39) soient ceux provenant.',
 'P07b with P08: (39) is in the prose; the component group display is unnumbered here.',
 'P09a: particulièrement plus the wrapped, still-doubtful simple.',
 'P09b: cancelled chaque composante conn., with doubt retained on the abbreviated ending.',
 'P09b/P09c/P09d: no post-D_i cancelled composante or inserted et; insertion is the entire raised clause, then live est connexe, et.',
 'Macro-only delimiter representation of the visibly parenthesized display label (40), preserved with tag{40}.',
 'Macro-only delimiter representation of the visibly parenthesized display label (40), preserved with tag{40}.',
 'P10/M0222: resolve the map label to kappa_i with medium confidence.',
 'P11a: mod autom, neither expanded nor dotted.',
 'P11b: readable près.',
 'P11c: donc en fait.',
 'P12a/P12b: preserve both cancellation layers before compatible; invariant remains doubtful.',
 'P12b: the cancelled phrase stable par l’opération belongs before compatible, not after les opérations.',
 'P13/P14: transcribe the two distinct oblique marginal notes, including the group diagram and the later note’s deletion/insertion.',
 'P15a: retain the visible but crossed on a candidate under doubt.',
 'P15b: retain the separate raised inclusion insertion inside the later whole-paragraph cancellation.',
 'P15c: the old parenthesis retains its locally cancelled intersection candidate; it is not the inserted subset condition.',
 'P15c: visible inequality followed by phi-shaped empty set; bars preserved.',
 'P15e: no seule between une and comp.',
 'P16 restores foliation 135. P13/P14 handle the actual margin ink. H’s two editorial notes and end-document command are not manuscript text and produce no separate ink collation rows.',
]
diff_coverage=[dict(row=i+1,disposition=x) for i,x in enumerate(dispositions)]
review=[
 dict(text='Opening before éléments',scope_attachment='No independent deletion is transcribed.',evidence='P00: the diagonal belongs to adjacent oblique marginal writing and does not traverse a preceding word.'),
 dict(text=r'\mathcal E_{U/K}^{\unsure{\bar L|\bar K}}',scope_attachment='Rewriting is confined to the superscript body; no separate cancelled word is inferred.',evidence='P03: clear overbar and repeatedly retraced capital immediately above the group subscript.'),
 dict(text=r'\deleted{chaque composante \unsure{conn.}}',scope_attachment='The straight strike covers this entire original sequence.',evidence='P09: one long cancellation crosses the three successive word groups.'),
 dict(text=r"\inserted{dans ce cas d'ailleurs $D_J=D_i$}",scope_attachment='The entire raised line replaces the preceding cancelled sequence; the later est connexe remains live baseline text.',evidence='P09: raised baseline throughout the insertion; separate lower e/s/t before connexe; no added et before it.'),
 dict(text=r'\deleted{\unsure{invariant}}',scope_attachment='First cancelled candidate after qui est.',evidence='P12: separate short strike through a single compact word; internal letters remain uncertain.'),
 dict(text=r"\deleted{stable par l'opération}",scope_attachment='Second cancelled candidate before the live compatible avec les opérations continuation.',evidence='P12: a long strike crosses the complete stable/par/l’opération sequence below the live replacement.'),
 dict(text=r'\deleted{\unsure{extérieures}}',scope_attachment='Cancellation only of the adjective after les opérations in the lower note.',evidence='P14: strike through the word below the underlined first pi group, not through les opérations or the later exterior-hom insertion.'),
 dict(text=r'\inserted{extérieurs}',scope_attachment='Attaches after les hom in the lower marginal note.',evidence='P14: bent leader reaches that position; its shape is not transcribed as a brace or parenthesis.'),
 dict(text=bottom,scope_attachment='All of the bottom paragraph, including its earlier insertion and local deletion, is later cancelled by the large diagonal crosses.',evidence='P15: several large diagonals traverse every line of the paragraph and the raised parenthesis.'),
 dict(text=r"\inserted{(\unsure{donc|d'où} $\bar D_{J'}\subset\bar D_J$),}",scope_attachment='Raised parenthesis follows J-prime superset J and precedes the old i.e. parenthesis; it remains inside the whole-paragraph deletion.',evidence='P15: smaller raised lettering, paired D overbars, and its own parentheses/comma; opening word crossed and uncertain.'),
 dict(text=r'\deleted{\unsure{\cap D_J}}',scope_attachment='Local earlier deletion within the old nonemptiness parenthesis, distinct from the later large-cross cancellation.',evidence='P15: short dense cancellation strokes cover the operator and D_J between barred D_{J\'} and the visible inequality.'),
]

report=dict(page=PAGE,reader='reader_c',line_count=51,changes=changes,decisions=decisions,
 inventory=inventory,audit_boxes=audit,doubts=doubts,notes=notes,check_events=events,
 notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff_coverage,
 deletion_insertion_review=review)
assert [d['id'] for d in decisions]==[m['id'] for m in marks]
assert len(diff_coverage)==len(list(csv.DictReader((PACKET/'differences.tsv').open(),delimiter='\t')))==28
for p in boxes:
    assert (ROOT/'work'/crop(p)).exists(), p
for a in audit:
    x0,y0,x1,y1=a['xyxy']; assert 0<=x0<x1<=1679 and 0<=y0<y1<=2359
assert len({x['id'] for x in changes})==len(changes)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,crops=len(boxes),changes=len(changes),marks=len(decisions),audit_boxes=len(audit),diff_rows=len(diff_coverage),draft=str(OUT/'draft.tex'),report=str(OUT/'report.json'))))
