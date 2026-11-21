from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan059'
boxes=json.loads((root/f'proposed/{page}_crop_boxes.json').read_text())
changes=[]
def change(place,c,h,final,dc,dh,kind,error,evidence,crop,confidence='high',marked=False,consequential=False,additional=()):
    row=dict(id=f'{page}-{len(changes)+1:02}',place=place,c=c,h=h,final=final,diff_c=dc,diff_h=dh,kind=kind,error_kind=error,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence,marked_in_h=marked,consequential=consequential)
    if additional:
        row['supporting_evidence']=[dict(crop=f'crops/{page}_{n}.png',box=boxes[n]) for n in additional]
    changes.append(row)
change('Opening cancelled word',r'\deleted{traduire}',r'\struck{\ill{}}',r'\deleted{\unsure{traduire}}',False,True,r'readable ink left as \ill{}','Struck text','The tall crossed t, following r-like stroke, low a and looped d support traduire. The repeated dark cancellation obscures the middle and final joins, so the recovered word receives a doubt rather than being asserted as fully legible. The extra doubt alone is not counted as a change from C.','old_traduire','medium',True)
change('Cancelled designation sentence',r'\deleted{Si on désigne désormais par $S\mathcal TD_{\mathrm{top}}^\pm$ le groupoïde}',r'\struck{\ill{} \ill{} distinguer, \ill{} pour $S\mathcal{T}D^{\pm}_{\mathrm{top}}$ le groupoïde}',r'\deleted{Si on désigne désormais par $S\mathcal TD_{\mathrm{top}}^\pm$ le groupoïde}',False,True,'misread word','Struck text','The right-hand opening has Si, low on, and désigne with d ascender, accented e, dotted i and descending g. The left continuation has the longer désormais run. On the lower baseline par has only p/a/r, without the additional ou of pour. The source has no comma after désigne. The category formula and final le groupoïde remain under the same cancellation.','cancelled_groupoid','medium',True)
change('Quotation marks around gommer',r"``gommer''",r'« gommer »',r"``gommer''",False,True,'other','Other','Two short raised ticks stand before gommer and another pair after it. There are no angled guillemet strokes.','forgetting')
change('Forgetting clause',r'de les oublier',r"d'où la \ill{}",r'de les oublier',False,True,'misread word','Words','At the upper right de is followed by the tall l and low es; the next baseline begins oublier with initial ou, b/l ascenders, dotted i and final er. These letters do not give où la.','forgetting','high',True)
change('Inserted ces marquages and its attachment',r'\inserted{\unsure{ces|les} marquages} ---',r'--- \add{\uncertain{marquages}}',r'\inserted{ces marquages} ---',False,True,'insertion or placement','Insertions put in the wrong place','The raised prefix begins with a rounded open c, with no tall l ascender, followed by low e/s. Marquages has the q descender and terminal s. The curved attachment returns immediately after oublier and before the dash; H omits ces and places the insertion after the dash.','forgetting','high',True)
change('Section D heading singular',r'\uline{Opération de recollement}',r'\emph{Opérations de recollement.}',r'\uline{Opération de recollement}',False,True,'misread word','Words','After the t/i/o run of Opération the final n ends in a downturned exit. There is no separately written s before de. The underline ends before the visible following full stop.','heading')
change('Live adjective after plus',r'\unsure{cruciale|essentielle}',r'\struck{\ill{}} \add{essentielle}',r'cruciale',False,True,'misread word','Words','The word has an initial c, retraced r/u joins, a second c, dotted i, low a, one tall looped l and final e. There is no distinct cancellation stroke or separate raised replacement. The heavier initial cru is retracing within the live word.','crucial','high',True)
change('tautologique',r'tautologique',r'triviale',r'tautologique',False,True,'misread word','Words','The two t ascenders, flattened intervening au, looped l, descending g and later q distinguish the full tautologique run. The word is much longer than triviale and has both visible descenders.','tautologique')
change('Determiner before opérations',r'les',r'ces',r'\unsure{les|ces}',False,True,'misread word','Words','The initial letter is a tall open curve followed by a low e/s ending. It is compatible with the page’s open looped l, but its lack of a closed loop also admits c. Les is retained first, with the alternative explicitly marked rather than settled from grammar.','toutes','medium')
change('passons versus proposons',r'passons',r'\uncertain{proposons en vue}',r'passons',False,True,'misread word','Words','The low word has one descending initial p, then a/s/s/o/n/s-like joins. No second p descender appears as required by proposons. Parts of the low connecting strokes are pale but their positions are visible.','passons_revue','medium',True)
change('revue and sentence boundary',r'en revue.',r'en vue',r'en revue.',False,True,'misread word','Words','After en, the initial raised r and following e precede the visible v/u/e run; the word is revue, not vue. A separate full stop follows it, and the next word begins with a capital P.','passons_revue','high',True)
change('Pour la pratiquer and connection to preceding sentence',r'que nous passons en revue. Pour la pratiquer, il faut comme donnée préliminaire',r'. Pour ce que nous \uncertain{proposons en vue}, il faut comme donnée préliminaire',r'que nous passons en revue. Pour la pratiquer, il faut comme donnée préliminaire',False,True,'omission','Omissions','The preceding line ends with capital Pour and the looped la. The next line begins pratiquer: p, short r/a, t, dotted i, long q descender and final u/e/r. The comma follows pratiquer before il faut. No Pour ce begins the clause before que nous; that phrase continues directly from opérations.','pratiquer','high',True,False,('passons_revue','toutes'))
change('Cancelled word after Une partie',r'\deleted{\unsure{les}}',r'\struck{\ill{}}',r'\deleted{\unsure{les}}',False,True,r'readable ink left as \ill{}','Struck text','An ascending l-like stroke and a small low loop survive before the thick terminal cancellation. The ending is not independently plain, so les remains doubtful.','partie_old','low',True)
change('Pair after sigma-prime: glyphs and withdrawal state',r"\deleted{$\unsure{\{c,c'\}}$}",r'absent',r"\unsure{$\{c,c'\}$|\deleted{$\{c,c'\}$}}",True,True,'deletion state (struck given live or live given struck)','Struck text','Both c-shaped curves, their separating comma, the short raised prime after the second c and both braces are visible. No independent strike traverses those letters. An upper stroke extends from de across the opening-brace area, while a lower curved stroke rises toward A-prime. The visible live pair therefore comes first; withdrawal remains an alternative interpretation of the correction marks.','sigma_old','medium',False,True)
change('Raised A-prime',r"$A'$",r"$A'$",r"\inserted{$A'$}",True,True,'insertion or placement','Insertions put in the wrong place','The capital A and its separate raised prime occupy the space above and to the right of the pair. A curved stroke rises in their direction. The placement is a raised addition; whether it replaces the unstruck pair remains explicitly uncertain.','sigma_old','medium',False,True)
change('Punctuation after raised A-prime',r"$A'$.",r"$A'$ \struck{\ill{}} ;",r"\inserted{$A'$}",True,True,'text not on the page','Text that is not on the page','The visible prime is followed by blank space. Neither a separate full stop nor a semicolon is visible after A-prime. The nearby lower curved mark belongs to the attachment/correction stroke.','sigma_old','medium',True)
change('Separate cancelled et les sigma',r'\deleted{\unsure{et les}\ $\unsure{\sigma}$}',r'\struck{\ill{}}',r'\deleted{\unsure{et les}\ $\sigma$}',False,True,r'readable ink left as \ill{}','Struck text','The long horizontal cancellation crosses the short et/les-like run on the left and the symbol on the right. The words overlap adjacent baselines and remain doubtful. The symbol itself has a closed left loop and a long rightward arm, the page’s clear sigma form, with no raised prime.','cancel_etles','medium',True)
change('Cancelled item-b formula: low index',r"\deleted{$\{a,a'\}\in\unsure{A'_l|A'_2}$}",r"\struck{$\lbrace a,a'\rbrace\in A'_2$}",r"\deleted{$\{a,a'\}\in\unsure{A'_2|A'_l}$}",True,False,'misread symbol or index','Symbols and indices','The brace-enclosed a pair, comma, prime and membership-shaped sign remain visible along the strike. The A is heavily retraced. Its low index begins with an arch/rising stroke and ends in a short rightward return, favouring 2 over looped l, but overwriting prevents a certain choice. The whole cancelled formula is included in one audit unit.','b_old_formula','low',False,True)
change('tout orbite',r'\unsure{toute|tout} orbite',r'toute orbite',r'tout orbite',True,True,'misread word','Words','The final t has an upright and shared crossbar ending in a hook. The baseline after its lower foot is blank until orbite; no separate e follows. The grammatical surprise tout orbite is retained.','toute_orbite','high')
change('de after orbite: uncertain withdrawal',r'\deleted{de}',r'absent',r'\unsure{de|\deleted{de}}',True,True,'deletion state (struck given live or live given struck)','Struck text','The d has its loop and ascender, followed by a low e. The curved stroke passes above this baseline and rises toward the A-prime of item a; it does not independently strike through de. Live de is therefore first, with possible withdrawal retained as an alternative.','toute_orbite','medium')
change('un isom.',r'un isom.',r'une isom.',r'un isom.',False,True,'misread word','Words','The final n of un ends with a single downturned stroke; the gap before dotted i contains no e. A clear separate point follows isom in this occurrence.','un_isom')
change('inverses l’un',r"l'un de l'autre.",r"l'une de l'autre.",r"l'un de l'autre.",False,True,'misread word','Words','After the apostrophe, u/n form one low joined run ending in a descending exit. There is no following e before de. The full stop after autre is visible.','inverse_lun')
change('Final isom without point',r'à isom unique',r'à isom.\ unique',r'à isom unique',False,True,'other','Other','The m ends in a downturned hook, then a clear gap precedes unique. No separate point is visible, unlike the earlier un isom. occurrence.','final_isom')
change('Lower handwritten foliation',r'\mspage{58}',r'absent',r'\mspage{58}',False,True,'omission','Omissions','The first digit has a short upper bar and broad lower curve, giving 5. The second has two stacked closed loops joined at a narrow waist, giving 8.','lower_number')

def dec(i,act,reading,evidence,crop,confidence):
    return dict(id=i,decision=act,reading=reading,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence)
decisions=[
 dec('M0748','first','ces','The initial rounded open c has no tall l ascender; the following low e/s complete ces before marquages.','forgetting','high'),
 dec('M0749','first','cruciale','The sequence c-r-u-c-i-a-l-e is visible, including the dotted i and single tall l loop. Heavy initial retracing does not form a separate strike or an inserted second word.','crucial','high'),
 dec('M0750','alternative','tout','After the final t upright and its crossbar/foot there is no separate e on the baseline before orbite.','toute_orbite','high')]
implicit=[
 dec('I01','undecided',r'\deleted{\unsure{les}}','The initial ascending l-like stroke survives, but the low ending is merged with the cancellation and is not fully legible.','partie_old','low'),
 dec('I02','first',r"$\{c,c'\}$",'Both c curves, comma, second prime and braces are clear. This resolves the glyph doubt only; the final text separately preserves uncertainty about whether the pair was withdrawn.','sigma_old','high'),
 dec('I03','undecided',r'\deleted{\unsure{et les}}','The short word shapes are crossed and intersect nearby live baselines; every letter is not independently visible.','cancel_etles','low'),
 dec('I04','first',r'$\sigma$','A closed left loop joins a long rightward arm. There is no second loop or raised prime that would require another symbol.','cancel_etles','high'),
 dec('I05','undecided',r"\deleted{$\{a,a'\}\in\unsure{A'_2|A'_l}$}",'The low arch and rightward return favour 2, but the A and index region are overworked. The first reading is changed to 2 without claiming resolution.','b_old_formula','low')]
doubts=[
 dict(place='Opening cancelled word',reading=r'\deleted{\unsure{traduire}}',alternatives='traduire; middle and ending partly obscured',confidence='medium',reason='Repeated cancellation conceals several joins; the plausible word is not treated as fully recovered.'),
 dict(place='Determiner after toutes',reading=r'\unsure{les|ces}',alternatives='les / ces',confidence='medium',reason='The tall initial curve may be an open l loop, but it also resembles c; grammar does not decide.'),
 dict(place='Cancelled word after Une partie',reading=r'\deleted{\unsure{les}}',alternatives='les; ending unresolved',confidence='low',reason='The terminal letters are merged with the cancellation.'),
 dict(place='Visible pair after sigma-prime',reading=r"\unsure{$\{c,c'\}$|\deleted{$\{c,c'\}$}}",alternatives='visible live pair / pair withdrawn by correction marks',confidence='medium',reason='The glyphs are clear, but no independent strike crosses them. The surrounding curved strokes may instead mark attachment or replacement.'),
 dict(place='Cancelled et les',reading=r'\deleted{\unsure{et les}}',alternatives='et les; one or more letters obscured',confidence='low',reason='The cancellation and nearby live writing intersect the small word run.'),
 dict(place='Whole cancelled item-b formula',reading=r"\deleted{$\{a,a'\}\in\unsure{A'_2|A'_l}$}",alternatives="A'_2 / A'_l",confidence='low',reason='The low index has a 2-like arch and return, but overwriting prevents a secure distinction from a cursive l.'),
 dict(place='de after orbite',reading=r'\unsure{de|\deleted{de}}',alternatives='live de / withdrawn de',confidence='medium',reason='The curved mark passes above the letters and rises toward the A-prime above; its role is not settled by a crossing stroke.')]
inv=[]
def element(kind,pos,words,sheet='text'):
    inv.append(dict(element=f'E{len(inv)+1:02}',sheet_kind=sheet,hand='his hand',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
element('text','Top centre','15')
element('text','Opening continuation','pour ... traduire le groupoïde de Teichmüller topologique ...')
element('deletion','First baseline, after pour','traduire')
element('deletion','Right end of fourth baseline and two following continuations','Si on désigne désormais par S𝒯D_top^± le groupoïde','cancelled_draft')
element('insertion','Above cancelled Si on désigne','Néanmoins on')
element('text','Forgetting paragraph','veut avoir le droit de les ``gommer\'\' ...')
element('insertion','Above oublier / dash junction','ces marquages')
element('deletion','After dash, before s’ils','même')
element('text','Middle heading','D) Opération de recollement.')
element('text','Introduction below heading','C’est la plus cruciale, la moins tautologique ...')
element('text','Before item a','Pour la pratiquer, il faut comme donnée préliminaire')
element('text','Item a, first baseline',r"a) Une partie ... $A'$ de $A_l$ (arêtes libres),")
element('deletion','Item a, after Une partie','les')
element('text','Item a, involution and equivalence clause','et une involution ss pts fixes ... classes de cardinal 2 ...')
element('text','Item a, lowered pair with uncertain withdrawal state',r"$\sigma'$ de $\{c,c'\}$")
element('insertion','Item a, above-right of pair',r"$A'$")
element('deletion','Short left interlinear cancelled run','et les sigma')
element('text','Item b opening','b) Pour ... tout orbite ...')
element('deletion','Item b, after Pour',r"$\{a,a'\}\in\unsure{A'_2|A'_l}$")
element('text','Item b, word with uncertain withdrawal state','de after orbite')
element('text','Item b, main data',r"$\{a,a'\}$ de $A'$, un isom. renversant l’orientation ...")
element('text','Lower lines','de C_a sur C_a′ et de C_a′ sur C_a, inverses l’un de l’autre.')
element('text','Unfinished last sentence','Pour que l’opération soit bien déterminée à isom unique')
element('text','Bottom left','58')
notes=[
 dict(id=f'{page}-N01',text='The opening continuation says that the topological Teichmüller groupoid leads to structures whose cutting circles are effectively marked, while one still wants the right to forget those markings. Section D introduces recollement. It specifies a part A′ of the free-edge set A_l and a fixed-point-free involution, described parenthetically by equivalence classes of cardinality 2. For each pair it asks for orientation-reversing isomorphisms between C_a and C_a′ that are inverse to one another. The sentence about determination up to unique isomorphism stops at unique on this page. These are statements read from the page, not proof claims.'),
 dict(id=f'{page}-N02',text='The source reads tout orbite, un isom. and l’un; these endings have not been adjusted for agreement. The last isom has no point, although the preceding un isom. does. No continuation such as près is supplied after the page-ending unique.'),
 dict(id=f'{page}-N03',text='The visible {c,c′} pair is not crossed by an independent strike. The raised A′ and the curved attachment marks may indicate replacement, but that intention does not erase the visible pair. The first alternative therefore retains it live. The de after orbite receives the same treatment because its curved overhead line does not independently strike the letters. Both state questions are reserved for independent audit.'),
 dict(id=f'{page}-N04',text='The original and each prepared half were read once, including witness agreements. Nineteen first-pass crops were viewed. The extra groupoid_name crop checked the agreed first-line proper name and accents without changing the reading. No OCR, outside page packet, web lookup, TeX compilation or blind second reading was used. Page-specific generators and working files are retained.')]
checks=[dict(statement_id=f'{page}-N01',type='carried as background without fault found',outcome='The definitions and asserted data for recollement were read and summarized. No proof check or formal verification was performed; the transcription does not certify the mathematical assertions.')]
notation=[
 dict(sign=r'\sigma',meaning_or_form='A small closed left loop joins a long horizontal right arm; a prime is a separate raised short stroke.',places='Live sigma-prime in item a; isolated cancelled sigma in the left interlinear run.',universality='The two visible sigma forms on this page share the loop-and-arm form; only the live occurrence has a prime.',witness_errors='C doubts the cancelled sigma; H leaves it as illegible. The clear glyph is now recovered.'),
 dict(sign='un / l’un',meaning_or_form='The final n ends in a downturned exit with no following e loop.',places='un isom.; inverses l’un de l’autre.',universality='Both disputed occurrences on this page have the same final n shape.',witness_errors='H reads une and l’une at these two places; C preserves the visible endings.'),
 dict(sign='tout',meaning_or_form='The t crossbar ends in a hook above the baseline; the last lower foot has no separate following e.',places='tout orbite in item b.',universality='One disputed occurrence on this page only.',witness_errors='C leads with toute in its alternatives and H gives toute; the crop supports tout.'),
 dict(sign='Curved correction / attachment strokes',meaning_or_form='A curved line above a word or below a formula need not cross its letters; its role may be attachment or replacement rather than cancellation.',places='Pair {c,c′}, raised A′, and de after orbite.',universality='These connected local marks are recorded with explicit state doubts, not generalized to unrelated strikes.',witness_errors='C treats the pair and de as certainly deleted; H omits the pair and de. Both remain visible in the proposal.'),
 dict(sign="A'_2 / A'_l",meaning_or_form='The low index has an arched rising start and short right return; heavy overwriting prevents certainty.',places='Cancelled item-b formula.',universality='One cancelled occurrence only; the clear live A_l is not changed.',witness_errors='C puts l first and H gives 2. The proposal leads with 2 but retains l as a doubt.')]
abbreviations=[dict(form='ss',expansion='sans'),dict(form='pts',expansion='points'),dict(form='i.e.',expansion='id est'),dict(form='isom.',expansion='isomorphisme'),dict(form='isom',expansion='isomorphisme')]
second=[]
def audit(kind,box,reading):
    second.append(dict(box=f'B{len(second)+1:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
audit('handwritten number',(820,20,910,90),r'\mspage{15}')
audit('struck passage',(454,86,666,154),r'\deleted{\unsure{traduire}}')
audit('struck passage',(220,385,1666,647),r'\deleted{Si on désigne désormais par $S\mathcal TD_{\mathrm{top}}^\pm$ le groupoïde} \inserted{Néanmoins on}')
audit('insertion',(270,620,1666,834),r"veut avoir le droit de les ``gommer'', de les oublier \inserted{ces marquages} --- \deleted{même} s'ils y sont bel et bien!")
audit('different words',(330,895,1312,1044),r'D) \uline{Opération de recollement}.')
audit('different words',(274,1035,1572,1178),r'plus cruciale, la moins tautologique')
audit('different words',(605,1180,1565,1285),r'de toutes \unsure{les|ces} opérations')
audit('different words',(272,1290,1668,1620),r'que nous passons en revue. Pour la pratiquer, il faut comme donnée préliminaire')
audit('struck passage',(421,1620,1637,1712),r"a) Une partie \deleted{\unsure{les}} $A'$ de $A_l$ (arêtes libres),")
audit('doubtful formula',(277,1718,1640,1857),r"et une involution ss pts fixes (i.e. une relation d'équivalence à classes de cardinal 2) $\sigma'$ de \unsure{$\{c,c'\}$|\deleted{$\{c,c'\}$}} \inserted{$A'$} \deleted{\unsure{et les}\ $\sigma$}")
audit('doubtful formula',(438,1840,1516,1940),r"b) Pour \deleted{$\{a,a'\}\in\unsure{A'_2|A'_l}$} tout orbite \unsure{de|\deleted{de}}")
audit('different words',(274,1924,1635,2035),r"$\{a,a'\}$ de $A'$, un isom. renversant l'orientation")
audit('different words',(273,2160,891,2249),r"l'un de l'autre.")
audit('different words',(1081,2244,1632,2338),r'à isom unique')
audit('handwritten number',(37,2267,132,2340),r'\mspage{58}')
agreed=[dict(place='First-line groupoid and proper name',reading='le groupoïde de Teichmüller',crop=f'crops/{page}_groupoid_name.png',box=boxes['groupoid_name'],outcome='C/H agreement checked on a crop; no material change. The compact letter sequence and accent marks were preserved.')]
data=dict(page=page,reader='reader_c',lines_read=28,changes=changes,decisions=decisions,implicit_decisions=implicit,doubts=doubts,inventory=inv,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,second_boxes=second,agreed_reading_checks=agreed)
(root/f'proposed/{page}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {page}.tex and .json: {len(changes)} material rows; {len(decisions)} MARKS decisions; {len(implicit)} implicit decisions; {len(doubts)} doubts; {len(second)} non-duplicated audit units.')
