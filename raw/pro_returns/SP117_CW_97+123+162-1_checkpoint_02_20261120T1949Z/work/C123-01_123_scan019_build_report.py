import json
from pathlib import Path
base=Path('/workspace/scratch/d27bd2a88bca')
p='C123-01_123_scan019'
cb=json.loads((base/'out/work'/f'{p}_crop_boxes.json').read_text())
report={'page':p,'line_count':24,'changes':[],'doubts':[],'inventory':[],'notes':[],'check_events':[],'notation':[],'hand_log':[],'boxes':[]}
def change(id,line,c,h,final,shows,crop,conf,kind,cc,ch,mh=False,conseq=False,certainty=False):
    report['changes'].append({'id':id,'line':line,'c':c,'h':h,'final':final,'scan_shows':shows,'crop':str(base/'out/crops'/f'{p}_{crop}.png'),'box':cb[crop],'confidence':conf,'kind':kind,'changed_C':cc,'changed_H':ch,'marked_in_H':mh,'consequential':conseq,'certainty_only':certainty})
change('01','L01',r'des',r'des',r'd\deleted{\unsure{a}}es','The e has an additional lower counter and a right-side trace consistent with an older a; the underletter remains doubtful.','01','low','omission',True,True)
change('02','L01',r'f\unsure{\mathrel{\mapstochar\relbar}|\mapsto}f\circ i_o',r'f\mapsto f\circ i_0',r'f\mathrel{\mapstochar\relbar}f\circ i_o','The first application sign has a left upright and horizontal shaft with a flat terminal stub; no pointed right arrowhead is separable. The index is handled separately.','01','high','misread symbol or index',True,True,False,True)
change('03','L01',r'i_{\unsure{o|0}}',r'i_0',r'i_o','The lowered round type is the small lower-case o of this typewriter, with the same body size as the adjacent u_o index.','01','high','misread symbol or index',True,True,False,True)
change('04','L01',r'f\mathrel{\mapstochar\relbar}f(u_o)',r'f\mapsto f(u_0)',r'f\mapsto f(u_o)','Unlike the first sign, this sign has a pointed right terminal, with a short return branch below the shaft. Each endpoint was compared separately. The index is handled separately.','01','high','misread symbol or index',True,False,False,True)
change('05','L01',r'u_o',r'u_0',r'u_o','A lower-case-sized typed round o is lowered after u; it is not the full-height zero form.','01','high','misread symbol or index',False,True,False,True)
change('06','L02',r'\operatorname{Un}_c\to\unsure{\underline{\phi}|\underline{\varnothing}}_c',r'\mathrm{Un}_c\to\underline{\varnothing}_c',r'\operatorname{Un}_c\to\unsure{\underline{\varnothing}|\underline{\phi}}_c','The handwritten sign is an oval crossed by an ascending diagonal, with a separate underline. The slashed-ring reading is placed first, while phi remains possible for this recurring glyph.','02','medium','misread symbol or index',True,False,False,True)
change('07','D1 lower left',r'\underline{\phi}_c\simeq\operatorname{Par}_{c\prime}',r'\underline{\varnothing}_c\simeq\mathrm{Par}_{c\prime}',r'\underline{\varnothing}_c\simeq\operatorname{Par}_{c\prime}','The full square repeats the same underlined slashed oval. The recurring doubt is marked at its first page occurrence only. All four arrows have single shafts and ordinary heads.','04','medium','misread symbol or index',True,False,False,True)
change('08','D1 after lower right',r'.',r'(omitted)',r'.','A separate dark full stop stands to the right of Un_c, outside the mathematical object.','04','high','omission',False,True)
change('09','D2 upper right',r'Z_o',r'Z_0',r'\unsure{Z|\deleted{I}Z}_o','The small round handwritten index is o. The overworked capital and its possible I underlayer remain explicitly uncertain; that new uncertainty is detailed in doubts rather than treated as a resolved letter.','05','medium','misread symbol or index',False,True,False,True)
change('10','D2 lower right',r'\unsure{z(e)|Z(e)|\mathfrak{z}(e)}',r'\mathfrak{z}(e)',r'\unsure{\mathfrak{z}(e)|Z(e)|z(e)}','The leading glyph has two large curves like a 3 and a long returning lower loop. Fraktur z is the best shape match, but the alternatives are retained. Group-centralizer context does not override the ink.','05','medium','misread symbol or index',True,False,False,True)
change('11','L04',r'\deleted{$\operatorname{Dyn}_c$, ou ce qui revient au même}',r'(omitted)',r'\deleted{$\operatorname{Dyn}_c$, ou ce qui revient au même}','The entire phrase survives under typed x cancellation, including Dyn_c and même.','06','high','omission',False,True,False,True)
change('12','L05',r'\underline{\phi}_c\simeq\operatorname{Par}_{c\prime}',r'\underline{\varnothing}_c\simeq\mathrm{Par}_{c\prime}',r'\underline{\varnothing}_c\simeq\operatorname{Par}_{c\prime}','The handwritten slashed oval and underline recur before the equivalence; the full formula and prime were read together. The initial page occurrence carries the recurring glyph doubt.','07','medium','misread symbol or index',True,False,False,True)
change('13','L05–06 interline insertion',r'Z_o=e',r'Z_0=e',r'Z_o=e','The handwritten loop after the Z is a small lowered o; the equals sign and terminal e are clear.','08','high','misread symbol or index',False,True,False,True)
change('14','L06 interline insertion',r'que $G$ est quasi-déployé',r'que $G$ soit quasi-déployé',r'que $G$ est quasi-déployé','The replacement has the three joined letters e-s-t after G. The old baseline phrase below has soit, which is cancelled; the two layers must not be conflated.','09','high','misread word',False,True,False,True)
change('15','L06 cancelled phrase ending',r'\deleted{i.e. que $G$ soit quasi-déployé}',r'\struck{i.e. que $G$ soit quasi-déployé;}',r'\deleted{i.e. que $G$ soit quasi-déployé\unsure{;}}','At the end of the cancelled baseline phrase, a thick upright overlaps a possible semicolon. H records the semicolon; the crop permits it but does not settle the underlayer. The new handwritten colon is clearly above.','09','low','omission',True,False)
change('16','L05–06 replacement placement',r'\deleted{old clause}\inserted{new parenthesis}:',r'\add{new parenthesis}: \struck{old clause}',r'\deleted{i.e. que $G$ soit quasi-déployé\unsure{;}}\inserted{\handwritten{(i.e., si $Z_o=e$, que $G$ est quasi-déployé)}}\handwritten{:}','The old clause is on the baseline under a continuous strike; its replacement is directly above it and wraps to the next line. The two layers are encoded as deletion followed by insertion. Crops 08 and 09 together cover the wrap.','08','high','insertion or placement',False,True,False,True)
change('17','L06 after choisi',r'\deleted{\unsure{ceci}}',r'(omitted)',r'\deleted{\unsure{les}}','An ascender above the x-height precedes an e-shaped counter and a terminal s curve. These support les, not ceci, but multiple x strikes obscure the word enough to retain doubt. No further old word can be separated from the cancellation x marks.','10','low','misread word',True,True)
change('18','L07',r'\deleted{point rationnel}',r'(omitted)',r'\deleted{point rationnel}','Both words are still readable beneath the line of typed x strikes between un and sous-groupe.','11','high','omission',False,True,False,True)
change('19','L07 after L',r'\deleted{i.e.}',r'(omitted)',r'\deleted{i.e.}','The old abbreviation i.e. is cancelled immediately after L, before the replacement phrase above the line.','12','high','omission',False,True)
change('20','L07 interline insertion',r'ou ce qui revient au même',r'ou ce qui revient au même',r'ou ce qui revient au \unsure{$=$|$\overline{\mathrm{m}}$}','After au the ink consists of a short upper rule and a lower wavy/m-like stroke. There is no written-out même. Equals shorthand is the first reading; an overlined m remains possible. The whole insertion and its connector were inspected.','12','medium','abbreviation expanded or spelling modernised',True,True)
change('21','L08',r'\deleted{aux}',r'(omitted)',r'\deleted{aux}','The old a-u-x remains visible beneath typed x strikes between qui and s\'adaptent.','13','high','omission',False,True)
change('22','L09',r'\unsure{\mathfrak{g}|\mathscr{G}}(2)',r'\mathfrak{g}(2)',r'\mathfrak{g}(2)','The handwritten letter has a small upper loop, tall right stem and long returning descender, matching the established minuscule g form; the complete (2) is clear.','14','high','misread symbol or index',True,False,False,True,True)
change('23','L09',r'\deleted{est donc non vide}',r'(omitted)',r'\deleted{est donc non vide}','All four words survive the typed x overstrike after qui; the live a donc follows outside the cancellation.','14','high','omission',False,True,False,True)
change('24','L11 interline insertion',r'\inserted{Dynkin-}',r'\supplied{Dynkin-}',r'\inserted{Dynkin-}','Dynkin- is physically typewritten above Kostant, with a handwritten insertion connector. It is a real source addition, not an editorial supplied prefix. The heavy closing parenthesis remains doubtful.','15','high','insertion or placement',False,True,False,True)
change('25','L16',r'\unsure{invariantè|invariante}',r'invariante',r'invariant\unsure{\deleted{d}e|è|e}','The final e has a high hooked stroke attached at its right. A typed d under an overtyped e is a plausible layer reading; a grave-like mark or a plain e with an extraneous stroke remain alternatives. No spelling is silently normalized.','17','low','deletion state (struck given live or live given struck)',True,True)
change('26','L17 before marche',r'\deleted{\unsure{p}}marche',r'marche',r'\deleted{p}marche','A left descender with its foot and a right bowl survive beneath the live m, identifying the old p.','19','high','omission',True,True)
change('27','M1 opening',r'\unsure{Il|Ce}',r'Il',r'Il','After rotating the same crop 22 degrees clockwise, the initial narrow upright followed by a separate looped l is clear. No open C curve precedes an e.','20','high','misread word',True,False,False,False,True)
change('28','M2',r'pas le cas, p.ex.',r'\uncertain{pas} \ill{} \uncertain{injectif}',r'pas le cas, p.ex.','The note has the short words pas le cas, followed by p.ex. with dots. There is no long injectif word. The whole four-line margin note is preserved and its referent remains unresolved editorially.','20','high','misread word',False,True,True,True)
change('29','M3–M4',r'(cela l\'est pour $A_3$)',r'(\uncertain{cela vaut} pour $A_3$)',r'(cela l\'est pour $A_3$)','The third line ends with (cela, and the next begins with l\'est: a tall l, apostrophe and compressed e-s-t. No v-a-u-t sequence is present. The A_2, A_4 and A_3 digits were individually inspected.','20','high','misread word',False,True,True,True)
change('30','L19',r'pour des questions',r'pour les questions',r'pour \unsure{\deleted{l}d|\deleted{d}l}es questions','Both l and d are present in the first letter: the l stem/head and d bowl are independently visible. The darker rounded form favors d as live, but chronological order is not secure, so both orders are retained.','21','medium','deletion state (struck given live or live given struck)',True,True)
change('31','L20',r'parab\handwritten{\unsure{-}}oliques',r'paraboliques',r'parab\handwritten{\unsure{-}}oliques','A dark sloping pen stroke joins the space between b and o. It is retained as a doubtful dash; it may instead be a correction/joining stroke.','22','medium','omission',False,True)
change('32','L21',r'si:',r'si',r'si:','Two distinct dark dots after si form a colon, despite the unusual syntax.','23','high','omission',False,True)
change('33','L21',r'\operatorname{Autext}(G_o)',r'\operatorname{Autext}(G_0)',r'\operatorname{Autext}(G_o)','The full Autext(G_o) has a lowered lower-case-sized o. All capitals and parentheses in the complete formula are single typed glyphs.','24','high','misread symbol or index',False,True,False,True)
change('34','L23',r'\deleted{fib}',r'(omitted)',r'\deleted{fib}','The f top, dotted i and b stem/bowl remain readable under the typed x cancellation before oubli.','25','high','omission',False,True)

def doubt(line,reading,alts,conf,reason):
    report['doubts'].append({'line':line,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason})
doubt('L01',r'd\deleted{\unsure{a}}es',['des without a distinct old letter'],'low','The possible a/e overprint is crowded; the lower counter favors a but does not conclusively prove a separate underletter.')
doubt('L02; repeated D1 and L05',r'\underline{\varnothing}_c',[r'\underline{\phi}_c'],'medium','Oval with diagonal slash and underline; same shape recurs three times. Only the first occurrence is marked, per recurring-glyph convention.')
doubt('D2 upper right',r'\unsure{Z|\deleted{I}Z}_o',[r'Z_o retraced',r'older I overwritten by Z_o'],'low','Heavy blackening leaves a central vertical and lower projection; whether a distinct older I exists is not secure. No illegible macro is used inside the diagram.')
doubt('D2 lower right',r'\mathfrak{z}(e)',[r'Z(e)',r'z(e)'],'medium','The visible 3-shaped body and long lower return favor fraktur z. The apparent stabilizer context would suggest a group Z(e), but does not decide the visible alphabet.')
doubt('L06 old clause ending',r'\deleted{\unsure{;}}',['cancellation upright without separable old punctuation'],'low','A thick vertical overlaps the position of H’s semicolon. The new parenthesis and colon above are clear.')
doubt('L06 after choisi',r'\deleted{\unsure{les}}',['no secure alternative complete word'],'low','The l ascender and e/s bodies favor les, but multiple x strikes still mask parts of all letters. C’s ceci is less compatible with the ascender.')
doubt('L07 insertion after au',r'\unsure{$=$|$\overline{\mathrm{m}}$}',[r'$\overline{\mathrm{m}}$'],'medium','Two short strokes are present; the lower is m-shaped enough to retain an overlined-m alternative. Both witnesses expand the abbreviation as même.')
doubt('L11 after Kostant',r'\unsure{)}',['no secure alternative punctuation'],'medium','A right-curving closing parenthesis is heavily overworked. The source uncertainty is preserved.')
doubt('L16',r'invariant\unsure{\deleted{d}e|è|e}',[r'invariantè',r'invariante'],'low','Connected high hook at the final e may belong to an old d, a grave-like accent or an accidental overstrike; the layer order is not secure.')
doubt('L19',r'\unsure{\deleted{l}d|\deleted{d}l}es',[r'\deleted{d}les'],'medium','Both letters are visible, but density alone does not prove which was typed last. D as live is the first reading.')
doubt('L20',r'parab\handwritten{\unsure{-}}oliques',['paraboliques with a nonlexical joining/correction stroke'],'low','The dark stroke between b and o is physically present; its lexical status is uncertain.')

def inv(element,kind,pos,start,hand='typewriting with main correcting hand'):
    report['inventory'].append({'scan':'19','sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':pos,'first_words_or_objects':start,'transcribed':'yes'})
inv('E01','text','L01–L03, upper body','de Kostant. On a donc … diagramme')
inv('E02','deletion','L01, within des','possible old a below e','typewritten overprint')
inv('E03','insertion','L01, both morphisms','barred shaft; composition circle; second mapsto','main correcting hand')
inv('E04','insertion','L02, after Un_c','right arrow and underlined slashed-ring glyph','main correcting hand')
inv('E05','insertion','L03, right end','d’esp. homogènes','main correcting hand')
inv('E06','diagram','D1, upper-middle, two rows','ST_c ≃ (CL)_{c′} ← Dyn_c; lower ring_c ≃ Par_{c′} ← Un_c; both downward arrows')
inv('E07','diagram','D2, right margin beside D1','L ← Z_o; P ← z-shaped(e); both downward arrows','main correcting hand')
inv('E08','deletion','D2 upper-right object','possible older I under Z, explicitly uncertain','main correcting hand')
inv('E09','text','L04–L18, main paragraph','Pour qu’il existe un point rationnel … jusqu’à nouvel ordre).')
inv('E10','deletion','L04 right','Dyn_c, ou ce qui revient au même','typewritten x cancellation')
inv('E11','insertion','L05 left, formula','underlined slashed-ring glyph and equivalence','main correcting hand')
inv('E12','insertion','above L05 right and L06 left','(i.e., si Z_o=e, que G est quasi-déployé):','main correcting hand')
inv('E13','deletion','L05 right to L06 left','i.e. que G soit quasi-déployé;','typed text, main-hand horizontal strike')
inv('E14','deletion','L06 after choisi','les, uncertain','typewritten x cancellation')
inv('E15','insertion','above L07, after L','ou ce qui revient au = / overlined m','main correcting hand')
inv('E16','deletion','L07 left','point rationnel','typewritten x cancellation')
inv('E17','deletion','L07 after L','i.e.','typed text, main-hand strike')
inv('E18','insertion','L07, i:G_m→G','right arrow','main correcting hand')
inv('E19','deletion','L08 after qui','aux','typewritten x cancellation')
inv('E20','insertion','L09 after de','fraktur g(2)','main correcting hand')
inv('E21','deletion','L09 after qui','est donc non vide','typewritten x cancellation')
inv('E22','insertion','above L11 Kostant','Dynkin-','typed addition, main-hand connector')
inv('E23','text','L11 after Kostant','overworked closing parenthesis','typewriting/overwork, layer uncertain')
inv('E24','text','L15 beginning','underlined invariant par followed by Γ','typed words, main-hand underline and Γ')
inv('E25','insertion','above L15 after propriété','de c','typed addition, main-hand connector')
inv('E26','deletion','L16 end of invariante','possible old d below e, alternatively accent/overstrike','typewritten overprint, doubtful')
inv('E27','insertion','L16 after par and between c,c′','Γ; mapsto','main correcting hand')
inv('E28','margin note','M1–M4, slanting left margin beside L16–L19','Il n’est en effet pas le cas, p.ex. pour A_2,A_4 (cela l’est pour A_3)','main correcting hand')
inv('E29','insertion','L17 before On notera; L18 after period','opening and closing parentheses','main correcting hand')
inv('E30','deletion','L17 within marche','p below the live m','typewritten overprint')
inv('E31','text','L19–L22, lower-middle paragraph','Ceci montre l’intérêt … et pas str. plus grand.')
inv('E32','deletion','L19 after pour','l/d overprinting, order uncertain','typewritten overprint')
inv('E33','insertion','above L20 before sous-groupes','classes de','typed classes; handwritten de and connector')
inv('E34','insertion','L20 within paraboliques','sloping dash/joining stroke','main correcting hand')
inv('E35','text','L23–L24, bottom paragraph','On notera cependant … de ce der-')
inv('E36','deletion','L23 before oubli','fib','typewritten x cancellation')
inv('E37','text','lower-left corner, y2047–2129','18; archive number recorded only in comment','archive numbering hand, pencil')

report['notes']=[
'Line labels L01–L24 count the 24 full-width typed prose lines, excluding the two diagram rows, interlinear additions and four slanting margin-note lines. D1 is the large square; D2 is the small handwritten square; M1–M4 label the marginal note. The sheet has no separate authorial page number; archive 18 is a comment only.',
'The page continues the Kostant/Dynkin discussion, compares Dyn_c, ST_c, Un_c and the underlined slashed-ring object through homogeneous-space diagrams, and discusses rational parabolics, rational Dynkin data, arithmetic questions and filtrations from unipotents. These are source assertions, not conclusions proved by this transcription.',
'The upper-right square’s apparent stabilizer interpretation makes a group Z(e) mathematically plausible, while the lower-right ink is 3-shaped with a returning loop. This contextual tension prompted a full-square relook and remains a doubt, not a reason to replace the written glyph.',
'The non-inner-form caveat is explicit: one must first verify that the class c′ of P comes from a Dynkin c invariant under Γ. The text does not claim that this verification has been completed.',
'The source expressly says that invariance of c does not clearly follow from invariance of c′, faute de savoir si c↦c′ est injectif sur les classes de Dynkin. The insertion de c is preserved at propriété. No injectivity theorem is supplied editorially.',
'The marginal note reads Il n’est en effet pas le cas, p.ex. pour A_2,A_4 (cela l’est pour A_3). Its grammatical reference is not resolved, and the A-type examples have not been independently proved here.',
'The semi-local-ring extension is qualified exactly as written by de car. nulle jusqu’à nouvel ordre. It remains a provisional restriction, not an unconditional statement over arbitrary characteristic.',
'The stabilizer comparison is presented as a question to investigate: de voir si: leur stabilisateur dans Autext(G_o) est le même … et pas str. plus grand. The unexpected colon and str. abbreviation are retained.',
'The agreement de cette classe rationnel is retained. The overworked final letter in invariante and the pen stroke within parab-oliques are retained with in-place doubts; neither grammar nor mathematical expectation repairs them.',
'The final printed der- ends the leaf. Under the inherited line-end joining convention the draft retains der% without a lexical hyphen; crop26 records the visible hyphen. No next leaf was consulted.',
'H’s explanatory note about the small square is editorial and is not ink. Macro-only differences, including handwritten wrappers, operatorname versus mathrm, colon spacing, ampersand syntax and archive/page markers, have no change rows.',
'The two first application signs were checked independently: the first terminates in a flat stub, the second in a pointed right tip. Later c↦c′ has a clear pointed head. No arrow was inferred merely by repetition.',
'All cancellation spans in C were inspected; H omits several of them. The newly identified old layers in the two short words and at invariante remain doubtful where stroke order or original letters cannot be established.'
]
report['reading_notes']=[
'34 change rows compare the candidate with either witness; pure new doubt marks are kept in doubts instead of counted as lexical corrections.',
'29 saved evidence crops were displayed. Crop20 was rotated in place 22 degrees clockwise for readable baselines, keeping its original source box unchanged.',
'Unresolved ink: possible old a in first des; slashed-ring alphabet; overworked Z/possible I and z-shaped(e); cancelled semicolon and les; = versus overlined m; Kostant closing parenthesis; final d/e/accent layer; lower l/d order; paraboliques joining stroke.'
]
report['check_events']=[
{'statement_id':'123-019-open-conditional','type':'targeted proof check','outcome':'Conditional local check only: over an infinite field k, a nonempty k-defined Zariski-open subset of affine n-space has a k-point. It contains D(f) for a nonzero polynomial f, and induction on n gives a k-point where f is nonzero. This supports the source’s open-dense-vector-space step under those hypotheses; it does not establish the rational Levi, the open set’s definition or the semi-local extension.'},
{'statement_id':'123-019-invariance-conditional','type':'targeted proof check','outcome':'Conditional elementary check: if the map of Γ-sets c↦c′ is equivariant and injective, Γ-invariance of c′ forces Γ-invariance of c, since c and γc have the same image. The page explicitly leaves injectivity and the required invariant lift unverified; neither premise is proved here.'},
{'statement_id':'123-019-homogeneous-maps','type':'carried as background without fault found','outcome':'The Kostant/Deligne maps and the homogeneous-space interpretation are carried as assertions of the source. Only the diagrams’ written objects and arrows were visually audited; no independent proof of these identifications was attempted.'}
]
report['visual_audit_events']=[
{'event':'layout','outcome':'Whole page viewed once for layout; supplied upper and lower halves each read once line-by-line against both C and H.'},
{'event':'differences','outcome':'Every substantive row of differences.tsv and every prior_questions.md lead was compared with the ink. Editorial H notes and macro-only mismatches were excluded.'},
{'event':'crops','outcome':'Saved and displayed crops01–29; selected existing crops were revisited for unresolved strokes and box placement. No second crop of a settled place was created.'},
{'event':'crop20_transform','outcome':'Original box [18,1338,252,1614], autocontrast and LANCZOS enlargement, mild unsharp mask, clockwise rotation 22 degrees, final width 2500 px. An initial 37-degree rotation was superseded in the same file; no duplicate evidence crop remains.'},
{'event':'restrictions','outcome':'No OCR, recognition library, external reference, other page image, out/second material or TeX compilation was used.'}
]
report['notation']=[
'123/019: i_o, u_o, the two Z_o and Autext(G_o) use lower-case o indices, confirmed from their own crops. They are not normalized to digit zero.',
'123/019: first handwritten application sign is a barred shaft without a clear arrowhead; the second and later c↦c′ have pointed right tips. Their forms are transcribed separately.',
'123/019: the underlined slashed oval is written as unsure{underline{varnothing}|underline{phi}} at the first occurrence, then underline{varnothing} at its two repeats.',
'123/019: handwritten g(2) has the loop/stem/returning-descender form of mathfrak g, matching the established packet notation.',
'123/019: the small square’s lower-right glyph is unsure{mathfrak z(e)|Z(e)|z(e)}; the top-right overworked glyph is unsure{Z|deleted I Z}_o. Neither alphabet nor old layer is imposed from expected group theory.',
'123/019: the short form after au is unsure{=|overlined m}; never expand it to même in the text. resp., i.e., d’esp., NB, p.ex., car. and str. retain their source forms.',
'123/019: underline G_m is a single typed G with a separate underline and lowered m; Γ has a footed stem and handwritten extended top stroke, not a Latin I replacement.'
]
report['hand_log']=[
'123/019: the correcting hand compresses n/u and some s strokes in d’esp. homogènes, ou ce qui revient and the marginal note; each whole word was checked, rather than regularized by French syntax.',
'123/019: the handwriting’s long descending f in effet and looped l in Il are visible after orienting the margin note. They decide Il and the actual note text against H’s injectif/vaut.',
'123/019: the lower-right z-like centralizer glyph can look like a large 3; its long returning lower loop supports the fraktur candidate, with alphabet uncertainty retained.',
'123/019: overtyping is distinct from double striking. Possible a/e, d/e and certain l/d layered shapes are recorded as cancelled/live alternatives, never as bold letters.',
'123/019: an insertion connector may resemble an opening parenthesis before Kostant, résulte or sous-groupes. The connector is represented by placement, while the actual added parentheses around On notera are transcribed.'
]

def box(id,kind,coords,reading):
    x0,y0,x1,y1=coords
    report['boxes'].append({'box':id,'kind':kind,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading})
box('B01','text',[680,149,753,213],r'd\deleted{\unsure{a}}es')
box('B02','formula',[963,149,1122,213],r'$f\handwritten{\mathrel{\mapstochar\relbar}}f\handwritten{\circ}i_o$')
box('B03','formula',[1217,149,1420,213],r'$f\handwritten{\mapsto}f(u_o)$')
box('B04','formula',cb['02'],r'$\operatorname{Un}_c\handwritten{\to\unsure{\underline{\varnothing}|\underline{\phi}}}_c$')
box('B05','insertion',[1388,278,1628,337],r'\handwritten{d\'esp. homogènes}')
box('B06','diagram',cb['04'],r'\diagram{\begin{tikzcd}[ampersand replacement=\&] \operatorname{ST}_c\handwritten{\simeq}(\operatorname{CL})_{c\prime}\handwritten{\arrow[d]} \& \operatorname{Dyn}_c\handwritten{\arrow[l]}\handwritten{\arrow[d]} \\ \handwritten{\underline{\varnothing}}_c\handwritten{\simeq}\operatorname{Par}_{c\prime} \& \operatorname{Un}_c\handwritten{\arrow[l]} \end{tikzcd}} .')
box('B07','diagram',cb['05'],r'\handwritten{\diagram{\begin{tikzcd}[ampersand replacement=\&] L\arrow[d] \& \unsure{Z|\deleted{I}Z}_o\arrow[l]\arrow[d] \\ P \& \unsure{\mathfrak{z}(e)|Z(e)|z(e)}\arrow[l] \end{tikzcd}}}')
box('B08','deletion',cb['06'],r'\deleted{$\operatorname{Dyn}_c$, ou ce qui revient au même}')
box('B09','formula',cb['07'],r'$\handwritten{\underline{\varnothing}}_c\handwritten{\simeq}\operatorname{Par}_{c\prime}$,')
box('B10','insertion and deletion',cb['08'],r'$\operatorname{Dyn}_c$ \deleted{i.e. que $G$}; above: \inserted{\handwritten{(i.e., si $Z_o=e$,}}')
box('B11','insertion and deletion',cb['09'],r'\deleted{soit quasi-déployé\unsure{;}}; above: \inserted{\handwritten{que $G$ est quasi-déployé)}}\handwritten{:}')
box('B12','deletion',[1144,687,1265,736],r'\deleted{\unsure{les}}')
box('B13','deletion',[337,752,641,807],r'\deleted{point rationnel}')
box('B14','insertion and deletion',cb['12'],r'$L$,\deleted{i.e.}\inserted{\handwritten{ou ce qui revient au \unsure{$=$|$\overline{\mathrm{m}}$}}} un $i:\underline{G}_m\handwritten{\to}G$')
box('B15','deletion',[1048,821,1114,876],r'\deleted{aux}')
box('B16','formula and deletion',cb['14'],r'$\handwritten{\mathfrak{g}(2)}$, qui \deleted{est donc non vide} a')
box('B17','insertion and text',cb['15'],r'de \inserted{Dynkin-}Kostant\unsure{)}')
box('B18','insertion',cb['16'],r'propriété\inserted{de $c$} résulte du')
box('B19','text',[274,1275,590,1339],r'\uline{invariant par} $\handwritten{\Gamma}$,')
box('B20','text and formula',cb['17'],r'invariant\unsure{\deleted{d}e|è|e} par $\handwritten{\Gamma}$,')
box('B21','formula',cb['18'],r'si $c\handwritten{\mapsto}c\prime$ est')
box('B22','text',[1390,1416,1590,1477],r'\deleted{p}marche')
box('B23','margin note',cb['20'],r'\handwritten{Il n\'est en effet pas le cas, p.ex. pour $A_2,A_4$ (cela l\'est pour $A_3$)}')
box('B24','insertion',cb['28'],r'Dynkin). \handwritten{(}On notera aussi')
box('B25','insertion',cb['29'],r'ordre).\handwritten{)}')
box('B26','text',[787,1540,861,1600],r'\unsure{\deleted{l}d|\deleted{d}l}es')
box('B27','insertion and text',cb['22'],r'les\inserted{classes \handwritten{de}} sous-groupes parab\handwritten{\unsure{-}}oliques')
box('B28','text',cb['23'],r'voir si: leur')
box('B29','formula',cb['24'],r'$\operatorname{Autext}(G_o)$')
box('B30','deletion',[1383,1811,1448,1876],r'\deleted{fib}')
box('B31','text',cb['26'],r'ce der-')
box('B32','pen number',cb['27'],r'% archive sheet number: 18')

(base/'out/work'/f'{p}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print({'changes':len(report['changes']),'doubts':len(report['doubts']),'inventory':len(report['inventory']),'boxes':len(report['boxes'])})
