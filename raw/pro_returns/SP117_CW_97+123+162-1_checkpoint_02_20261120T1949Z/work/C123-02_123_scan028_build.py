from pathlib import Path
import json
root=Path('/workspace/scratch/d27bd2a88bca')
page='C123-02_123_scan028'
packet=root/'packets'/page
work=root/'out/work'
cropdir=root/'out/crops'
c=(packet/'C.tex').read_text()
draft=r'\cotefile{123}'+'\n'+c
draft=draft.replace(r'\mspage{\handwritten{22}}',r'\mspage{\handwritten{\unsure{22|72}}}')
draft=draft.replace(r'\unsure{exact}',r'\unsure{exact|ex.ct}')
draft=draft.replace(r"\mathbb{E}'",r"\unsure{\mathbb{E}'|\underline{\mathrm{E}}'}")
draft=draft.replace(r'\unsure{vérifier que}','vérifier que')
draft=draft.replace(r'\deleted{d}\handwritten{c}e',r'\deleted{\unsure{d}}\handwritten{c}e')
draft=draft.replace(r'\margin{\handwritten{', '% Left margin beside the body reference on L07.\n'+r'\margin{\handwritten{',1)
(work/(page+'_draft.tex')).write_text(draft)
def macro(source,needle):
    start=source.index(needle)
    left=source.index('{',start)
    depth=0
    for p in range(left,len(source)):
        if source[p]=='{': depth+=1
        elif source[p]=='}':
            depth-=1
            if depth==0: return source[left+1:p],source[start:p+1]
    raise ValueError(needle)
def getblocks(source):
    first=macro(source,r'\deleted{un morphisme')[0]
    body=macro(source,r'\deleted{\deleted{\unsure')[0]
    foot=macro(source,r'\deleted{($')[0]
    cuts=[0]
    for needle in ['inductives '+r'\deleted',r'$(\mathrm{u}_','données de flèches',"d'une structure d'espèce",'peu engageante',"groupe, d'anneau"]:
        cuts.append(body.index(needle))
    cuts.append(len(body))
    result={'40':first,'48':foot}
    for n in range(7):
        result[str(41+n)]=body[cuts[n]:cuts[n+1]].strip()
    return result
blocks=getblocks(draft)
cblocks=getblocks(c)
coords=json.loads((work/(page+'_crop_boxes.json')).read_text())
coords.update(json.loads((work/(page+'_context_boxes.json')).read_text()))
margin=macro(draft,r'\margin{\handwritten{')[1]
figure=macro(draft,r'\handwritten{\figure{')[1]
starcall=r"\handwritten{($"+"{}"+r"^{*}$)}"
changes=[]
def change(line, cv, hv, final, why, key, kind='omission', changed_C=False,
           changed_H=True, confidence='high', consequential=False, certainty_only=False):
    changes.append(dict(id=f'028-{len(changes)+1:02d}',line=line,c=cv,h=hv,final=final,
        scan_shows=why,crop=str(cropdir/(page+'_'+key+'.png')),box=coords[key],
        confidence=confidence,kind=kind,changed_C=changed_C,changed_H=changed_H,
        marked_in_H=False,consequential=consequential,certainty_only=certainty_only))
change('head','22','72',r'\unsure{22|72}',
       'The first digit has a curved head and a small returning foot, favoring 2; it is less decisive than the second 2. H gives 72 without doubt. Both candidates remain in place.',
       '01','misread symbol or index',confidence='medium')
labels={'40':'L01–L03','41':'L04–L06','42':'L07–L09','43':'L10–L12','44':'L13–L15','45':'L16–L18','46':'L19–L21','47':'L22–L24','48':'F01–F04'}
hparts={'40':'','41':'','42':r'\marginal{est exact à gauche i.e.} ; \marginal{On peut donc dire que}','43':'','44':r'\marginal{et pour}','45':'','46':r"\marginal{l'expliciter et de}",'47':'','48':''}
for key in ['40','41','42','43','44','45','46','47']:
    change(labels[key],r'\deleted{'+cblocks[key]+'}',hparts[key],r'\deleted{'+blocks[key]+'}',
        'The full visible typescript in this consecutive source block is transcribed, including its page-wide cancellation and local revisions. H supplies an editorial synopsis rather than a full transcription; any direct addition quoted by H is listed in h. H’s prose is not treated as source wording. The saved strip gives every omitted word with its line context; separate targeted crops record the crowded alterations.',
        key,consequential=True)
change('L07–L08',r'\inserted{\handwritten{est \unsure{exact} à gauche i.e.}} commute aux limites projectives finies',
       'H editorial note: the addition replaces commute aux limites projectives finies.',
       r'\inserted{\handwritten{est \unsure{exact|ex.ct} à gauche i.e.}} commute aux limites projectives finies',
       'The curved insertion leader attaches before commute. No local cancellation crosses commute aux or the continuation limites projectives finies. The page-wide vertical cancellation is separate. Thus the original phrase remains locally live after the insertion.',
       '12','deletion state (struck given live or live given struck)',consequential=True)
change('left margin beside L07',margin,'',margin,
       'A separate handwritten reference is crossed twice in the left margin; its terminal dot survives. It is not the clear interlinear (I 2.11) after adjoints. H does not transcribe this marginal deletion.',
       '11',confidence='low')
change('between L24 and F01',figure,'',figure,
       'A long, gently irregular pen rule separates the body and footnote. H does not reproduce the rule. The source curve is retained in TikZ.',
       '28','drawing or diagram')
change('F01–F04',r'\deleted{'+cblocks['48']+'}','',r'\deleted{'+blocks['48']+'}',
       'H describes only selected footnote corrections in prose. The four visible source lines, including the old On peut, the case change d to D, the replacement citation, the second letter correction, both underlined U signs, and the cancelled final sentence, are transcribed in full. No closing parenthesis is supplied after droite at the cut edge.',
       '48',consequential=True)
change('F03',r'\inserted{$\underline{\mathrm{U}}$-}',r'$\mathcal{U}$-',r'\inserted{$\underline{\mathrm{U}}$-}',
       'The inserted U is a typewriter capital with a distinct short underline, not a calligraphic letter. The second U on the same line has the same single-underlined construction and was checked separately on crop36.',
       '35','misread symbol or index',consequential=True)
change('F01',r'\deleted{\unsure{vérifier que}}','H editorial note mentions the cancelled vérifier.',r'\deleted{vérifier que}',
       'The typed v, accented é, r, i, f, i, e, r and the q descender, u and e survive the oblique pen cancellation. Each letter is recoverable; the C doubt is resolved. The replacement (1.5 et 1.8) above is separately clear.',
       '30','other',changed_C=True,changed_H=False,certainty_only=True)
doubts=[
 dict(line='head',reading='22',alternatives=['72'],confidence='medium',reason='The first digit has a small return compatible with 2 but remains less certain than the second digit. Both readers retain 22|72.'),
 dict(line='L03, final reference',reading=r'(\deleted{\unsure{2|3}}3.2.1)',alternatives=['old first digit 3 rather than 2'],confidence='low',reason='Current handwritten 3 and the rest of 3.2.1 are clear; overlapping older strokes do not establish 2 versus 3.'),
 dict(line='L04, section number',reading=r'\deleted{\unsure{2|3}}\handwritten{3}.1.2.',alternatives=['old first digit 3 rather than 2'],confidence='low',reason='An older 2 is plausible beneath the handwritten 3, but the overwritten contour is insufficient for certainty. This occurrence was checked independently of L03.'),
 dict(line='L07, cancelled reference',reading='(2.11)',alternatives=['(2.1)','(I 2.11)'],confidence='low',reason='Dense oblique cancellation obscures the interior digits; the replacement footnote star is clear.'),
 dict(line='left margin beside L07',reading='(I 2.11)',alternatives=['(I 4.11)','(I 4.1)'],confidence='low',reason='The first I is visible; two diagonal cancellations interfere with the remaining figures. The dot after the crossed reference is live locally.'),
 dict(line='L07, interlinear insertion',reading='exact',alternatives=['ex.ct'],confidence='medium',reason='Between x and c the small mark is dot-like; it may be a very compressed a or a literal abbreviation dot. The remaining est, à gauche i.e. is clear.'),
 dict(line='L17, topos symbol',reading=r"\mathbb{E}'",alternatives=[r"\underline{\mathrm{E}}'"],confidence='low',reason='The lower body is strongly overprinted/darkened while the upper left stem looks single. Double striking and a thick separate underline cannot be distinguished securely; the whole E-prime symbol remains doubtful.'),
 dict(line='F02, overwritten initial letter',reading=r'\deleted{d}\handwritten{c}e',alternatives=[],confidence='medium',reason='The dense overprint favors old d under the current c, but does not expose the old bowl and ascender fully. The old d is marked unsure in place; no unsupported alternative letter is supplied.'),
 dict(line='F04, cancelled opening',reading="D'ailleurs",alternatives=[],confidence='low',reason='A probable D, following apostrophe and later letter fragments survive, but repeated oblique strokes prevent recovery of every letter.'),
 dict(line='F04, final cancelled citation',reading='1.2.(ii)',alternatives=['1.2.(iii)','1.2.(i)'],confidence='low',reason='1.2. is clear. The parenthetical subdivision is densely crossed at the right image edge; its strokes do not decide the number of i characters.')
]
targets=[
('text',[906,20,987,89],r'\mspage{\handwritten{\unsure{22|72}}}'),
('text',[1550,16,1652,94],'% archive sheet number: 27 (inverted)'),
('formula',[693,146,898,207],r"$\mathrm{u}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$"),
('formula',[1103,216,1367,284],r'$\mathrm{u}^{\handwritten{*}}$ resp. $\mathrm{u}_{\handwritten{*}}$'),
('text',[1533,289,1678,351],r'\handwritten{(\deleted{\unsure{2|3}}3.2.1)}'),
('text',[262,362,419,419],r'\deleted{\unsure{2|3}}\handwritten{3}.1.2.'),
('formula',[480,358,680,425],r"$\mathrm{u}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$"),
('insertion',[674,395,867,488],r'\inserted{\handwritten{(I 2.11)}}'),
('formula',[1301,436,1512,499],r"$\mathrm{u}_{\handwritten{*}}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$"),
('formula',[1046,502,1297,560],r"$\mathrm{u}^{\handwritten{*}}:\mathrm{E}'\handwritten{\longrightarrow}\mathrm{E}$"),
('deletion',[476,555,725,633],r'\deleted{\unsure{(2.11)|(2.1)|(I 2.11)}}'+starcall+'.Comme'),
('margin note',[98,565,244,642],margin),
('insertion',[1267,538,1635,620],r'\inserted{\handwritten{est \unsure{exact|ex.ct} à gauche i.e.}} commute aux'),
('text',[1420,637,1683,704],r'$\mathrm{u}^{\handwritten{*}}$ \uline{est} \deleted{exac}'),
('text',[267,689,877,787],r"\uline{exact}. \inserted{On peut donc dire que} \uline{\deleted{C}\handwritten{c}'est \deleted{donc} le foncteur}"),
('deletion',[1121,704,1297,777],r'$\mathrm{u}^{\handwritten{*}}$ \deleted{qui},'),
('formula',[271,781,448,842],r'$(\mathrm{u}_{\handwritten{*}},\mathrm{u}^{\handwritten{*}})$,'),
('deletion',[270,852,735,907],r'\deleted{assurant} Ces propriétés'),
('insertion',[463,896,672,990],r'\inserted{\handwritten{$\Sigma$}}\deleted{qui peut}'),
('insertion',[1102,1103,1500,1210],r"\inserted{\handwritten{et pour}} tout \handwritten{"+chr(96)*2+r"}objet de $\underline{\mathrm{E}}'$"),
('formula',[742,1200,847,1264],r'$\handwritten{\Sigma}$'+"''"),
('deletion',[520,1280,769,1336],r'\deleted{de} internes'),
('formula',[925,1279,1203,1342],r"$\unsure{\mathbb{E}'|\underline{\mathrm{E}}'}$ (II 4.1)),"),
('deletion',[1404,1278,1570,1341],r'\deleted{inverse}'),
('formula',[270,1339,333,1406],r'$\mathrm{u}^{\handwritten{*}}$'),
('insertion',[1184,1458,1600,1544],r"de \inserted{l'expliciter et de} se convaincre de"),
('deletion',[1344,1626,1658,1697],r'\deleted{ou de bimodule}'),
('text',[1456,1772,1683,1835],'se définis'),
('drawing',[74,1820,1661,1866],figure),
('deletion',[269,1855,741,1928],r"($\handwritten{*}$) \deleted{On peut} \deleted{d}\handwritten{D}'ailleurs"),
('insertion',[724,1839,1010,1933],r'\deleted{vérifier que}\inserted{\handwritten{(1.5 et 1.8)}},'),
('formula',[1319,1854,1551,1928],r"$\mathrm{u}_{\handwritten{*}}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$"),
('formula',[267,1927,615,1997],r"$\mathrm{u}^{\handwritten{*}}:\mathrm{E}'\handwritten{\longrightarrow}\mathrm{E}$ donné,"),
('text',[613,1927,685,1983],r'\deleted{\unsure{d}}\handwritten{c}e'),
('text',[1368,1927,1683,1996],'(resp. à droite'),
('insertion',[858,1971,1330,2050],r'aux \inserted{$\underline{\mathrm{U}}$-}limites projectives'),
('formula',[1541,1995,1599,2053],r'$\underline{\mathrm{U}}$-'),
('deletion',[575,2041,808,2124],r"\deleted{\unsure{D'ailleurs},}"),
('deletion',[803,2038,1476,2122],r"\deleted{c'est une conséquence immédiate de}"),
('deletion',[1460,2040,1683,2123],r'\deleted{1.2.\unsure{(ii)|(iii)|(i)}}')
]
boxes=[]
for n,(kind,b,reading) in enumerate(targets,1):
    boxes.append(dict(box=f'028-B{n:03d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
for key in ['40','41','42','43','44','45','46','47','48']:
    b=coords[key]
    boxes.append(dict(box=f'028-B{len(boxes)+1:03d}',kind='deletion',x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=r'\deleted{'+blocks[key]+'}'))
positions=[
'upper center','upper right, inverted','L01','L02','L03 right end','L04 section number','L04 morphism',
'above L05 after adjoints','L05 direct image','L06 inverse image','L07 reference and footnote call',
'left margin beside L07','above L07, before commute aux','L08 right','above and within L09 left',
'L09 middle','L10 beginning','L11 beginning','above and within L12','above and within L15',
'L16','L17 after exactitude','L17 before II 4.1','L17 after image','L18 beginning',
'above and within L20','L22 right','L24 right edge','between body and footnote','F01 beginning',
'above and within F01','F01 right','F02 beginning','F02 after donné','F02 right edge',
'above and within F03','F03 right','F04 beginning of cancelled sentence','F04 middle','F04 right edge'
]
inventory=[]
def inv(y,x,element,kind,position,words,hand):
    inventory.append((y,x,dict(scan=page,sheet_kind='cancelled_draft',hand=hand,element=element,
        kind=kind,position=position,first_words_or_objects=words,transcribed='yes')))
for n,((kind,b,reading),position) in enumerate(zip(targets,positions),1):
    ikind='text' if kind=='formula' else kind
    hand='typewritten and/or pen; authorship unassigned'
    if n==1: hand='handwritten page number'
    elif n==2: hand='archive hand'
    elif kind=='drawing': hand='pen rule'
    elif r'\handwritten{' not in reading: hand='typewritten with visible state/placement marks'
    inv(b[1],b[0],f'Localized source element {n:02d}',ikind,position,reading,hand)
    if r'\deleted{' in reading and ikind not in ['deletion']:
        inv(b[1]+0.1,b[0],f'Local cancellation within element {n:02d}','deletion',position,reading,hand)
    if r'\inserted{' in reading and ikind!='insertion':
        inv(b[1]+0.2,b[0],f'Insertion within element {n:02d}','insertion',position,reading,hand)
for key in ['40','41','42','43','44','45','46','47','48']:
    inv(coords[key][1],coords[key][0],f'Typescript source block {labels[key]}','text',labels[key],blocks[key][:220],'typewritten with pen corrections')
inv(207,815,'Single long vertical cancellation','deletion','from opening paragraph through footnote','Entire visible typescript, represented by enclosing deletion macros','pen stroke')
inventory=[row[2] for row in sorted(inventory,key=lambda x:(x[0],x[1]))]
reading_notes=[
 'Cancelled typescript on topos, with own page number 22|72 and revised section number 3.1.2. The inverted archive number is 27. No title sheet, date, or total page count is present.',
 'The opening continuation says that the topos morphism is unique up to unique isomorphism from the data u* or u_*, with a later explanation cited as 3.2.1; the older first digit is obscured.',
 'Section 3.1.2 invokes adjointness for preservation of projective limits by u_* and inductive limits by u*. It then invokes the additional finite-projective-limit condition, with the inserted wording exact|ex.ct à gauche i.e., and calls u* exact.',
 'The source claims transfer of algebraic structures Σ whose data use finite projective and arbitrary inductive limits. It declines to formalize the general assertion and asks the reader to explicate examples: groups, rings, modules, comodules, bigèbres and torsors. The former ou de bimodule is cancelled.',
 'The footnote states an adjoint-existence equivalence with preservation of the corresponding underlined-U limits, adds references 1.5 and 1.8, and cancels a consequence attributed to 1.2 with an overworked subdivision.',
 'Visible slips and edge limits remain: .Comme has no space; est muni and telles que celle de keep their source agreements; the body stops at se définis, and the footnote has no visible closing parenthesis after droite. No unseen continuation or punctuation is supplied. The phrase des ensembles déduits is correctly formed.'
]
check_events=[
 dict(statement_id='123/028.§3.1.2.adjoint-preservation',type='targeted proof check',
      outcome='Checked the local adjunction consequence formally, independently of the reference numbers: with L=u* left adjoint to R=u_*, Hom(A,R lim D) ≅ Hom(LA,lim D) ≅ lim Hom(LA,Dj) ≅ lim Hom(A,RDj), so R preserves existing limits; the dual Hom calculation gives preservation of existing colimits by L. This confirmed the directional pairing only and did not resolve any ink ambiguity.'),
 dict(statement_id='123/028.§3.1.2.structure-transfer',type='carried as background without fault found',
      outcome='The informal Σ-structure transfer assertion and examples are carried as source content. The author explicitly declines a formal specification and proof here; no independent proof of the full schema was attempted and no word was chosen from an expected theorem.'),
 dict(statement_id='123/028.footnote.adjoint-converse',type='carried as background without fault found',
      outcome='The converse adjoint-existence assertion is retained in its topos setting, with the newly added references. Those external numbered results were not available in this packet and were not checked. No unconditional adjoint-functor theorem is asserted by this audit.')
]
visual_audit_events=[
 'Read the whole image once for layout, then both full-resolution halves once line by line against C and H. All39 target crops and the nine consecutive source-context crops were displayed and inspected; root independently reviewed all48.',
 'Source-line labels L01–L24 denote the 24 typed body baselines; F01–F04 denote the four footnote baselines. Interlinear additions, margin material, numbers and the separator are separately inventoried and not counted as extra body lines. No mathematical display or diagram occurs.',
 'H contains an editorial synopsis and four direct additions, not a transcription of the cancelled typescript. H omissions are recorded as consecutive source blocks, with exact source text and saved evidence; its editorial prose is never copied as ink. Macro-only differences, its editorial page marker and stylistic guillemets create no change rows. Change flags refer to the issue of the row, not other separately logged issues in its context.',
 'All local deletions and insertions were checked separately from the page-wide vertical cancellation. The insertion before commute aux does not locally delete the following words. Curved insertion leaders under typed additions are placement marks rather than extra lexical underlines.',
 'The clear deleted vérifier que is resolved only after crop30 exposed every letter and the accent. Old reference digits, the cancelled references, the compressed exact|ex.ct, the overworked E-prime, the old d under c, the cancelled D’ailleurs and final subdivision retain doubts.',
 'Both source quotations were checked: the opening paragraph has paired typed double quotes, and the objet de E-prime quotation has a handwritten opening pair and a typed closing pair. C already uses the required paired backtick/apostrophe encoding; H’s editorial quote styling is not a source difference.',
 'Crop02 alone was rotated180 degrees to read the inverted archive number. Every crop retains its original-coordinate box; all crops use width2500, LANCZOS, autocontrast and mild unsharp masking. No OCR, recognition library, web lookup or TeX compilation was used.',
 'Target boxes give complete local readings and full affected formulas. The final nine source-strip boxes additionally carry the enclosing page-wide deletion, covering all source words omitted by H; targeted boxes separately cover each insertion, margin item, local cancellation, handwritten word/digit and unresolved symbol. Root may extract coordinates alone for blind second reading.'
]
notation=[
 '123/028: The many u stars are handwritten; their superscript/subscript placement is read separately at each occurrence. All six completed inline functor arrows have a single shaft and an ordinary right arrowhead, with no bar or hook.',
 '123/028: Both Σ symbols are handwritten angular capital sigmas. The prime marks on E belong to the typed symbols; no extra prime is supplied.',
 '123/028: E-prime in the object phrase has a single typed E and a separate underline. The E-prime before (II 4.1) is heavily overworked and remains unsure{mathbb E-prime|underline E-prime}; it is not normalized from the other occurrence.',
 '123/028: Both U qualifiers are single typed capitals with short separate underlines, not mathcal U. The first U- is a typed interlinear insertion with a pen leader.',
 '123/028: Source resp. and i.e. are retained. The compressed exact|ex.ct insertion remains ambiguous; a possible abbreviation is not silently expanded. The source word bigèbre is retained.'
]
hand_log=[
 'Scope: scan123/028 only. Handwritten stars have several short radiating strokes; every u-star and both footnote stars were checked independently, including the lowered stars of u_*.',
 'Scope: scan123/028 only. Revised handwritten3 has open upper/lower lobes; older2|3 remains ambiguous at both the citation and section number. The head number favors22, but its first glyph can still be read7. No digit rule is extrapolated from this uncertain occurrence.',
 'Scope: scan123/028 only. The a-like mark in exact is compressed to a dot-like trace, allowing ex.ct. The rest of the insertion and et pour have clear connected pen forms. H’s unsupported replacement claim is rejected on the live following line, not linguistic expectation.',
 'Scope: scan123/028 only. Sigma is written with an upper bar and angled return at both occurrences. Morphism arrows were checked at both ends on all six occurrences. Pen leaders for interlinear insertions are long low curves, distinct from local cancellation strokes.',
 'The correction hand is described only as the visible pen hand on this typescript. The page alone does not establish the author of either the typing or the corrections.'
]
report=dict(page=page,line_count=28,changes=changes,doubts=doubts,inventory=inventory,
 notes=[],reading_notes=reading_notes,check_events=check_events,
 visual_audit_events=visual_audit_events,notation=notation,hand_log=hand_log,boxes=boxes)
(work/(page+'_report.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'draft':str(work/(page+'_draft.tex')),'report':str(work/(page+'_report.json')),
 'changes':len(changes),'doubts':len(doubts),'inventory':len(inventory),'boxes':len(boxes)},ensure_ascii=False))
