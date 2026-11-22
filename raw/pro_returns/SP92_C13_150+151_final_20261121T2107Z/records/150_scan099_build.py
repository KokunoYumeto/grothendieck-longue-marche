from pathlib import Path
import json

ROOT = Path('/workspace/scratch/d7279cb02214')
WORK = ROOT / 'SP92_C13_150+151_work'
PAGE = '150_scan099'
packet = json.loads((ROOT / 'reading_packets' / PAGE / 'packet.json').read_text())
cm = json.loads((WORK / 'records' / (PAGE + '_cropmap.json')).read_text())
C, H = packet['witness_C'], packet['witness_H']

dotrule = r'\mathord{\cdot}\mathord{-}'
tworules = r'\mathord{-}\mathord{-}'
twodotsrule = r'\mathord{\cdot}\mathord{\cdot}\mathord{-}'
old_main = r'\deleted{X_J^*\unsure{\cap}}'
old_margin = old_main
annotation = r'''\begin{tikzpicture}[baseline=(top.base),x=1cm,y=1cm]
  \node (top) at (0,0) {$\mathcal V_d^Z$};
  \draw (-.48,-.25)--(-.48,-.36)--(.48,-.36)--(.48,-.25);
  \draw[->] (0,-.49)--(0,-1.17);
  \node[rotate=90] at (.21,-.79) {$\sim$};
  \node at (.61,-.79) {$(h)$};
  \node at (0,-1.42) {$\mathcal V_d$};
\end{tikzpicture}'''
opening = r'On aura de $=$, pour $J$ et $L$ quelconques'
f109 = r'''(109)\qquad
\mathcal V_{J,L}^Z=
\underset{\substack{d\in\mathrm{Drap}(J\cup L)\\d\cap J\ne\phi,\,d\cap L\ne\phi}}{\lim_{\longrightarrow}}
''' + annotation
margin = (r'si $J\prec L$, $J$ et $L$ des bandes et si $Z$ contient $'
          + old_margin + r'X_L^*$, donc contient $X_{i_n}^*$ si $d=(i_0,'
          + dotrule + r',i_n)$')
main = (r'\deleted{clairement} \inserted{donc si} '
        r'\inserted{$J,L$ des bandes et $J\prec L$, et si} $Z$ contient $'
        + old_main + r'X_L^*$, on aura')
f110 = r'(110)\qquad\mathcal V_{J,L}^Z\overset{(\overset h\sim)}{\hookrightarrow}\mathcal V_{\unsure{J|\square},L}'
f111 = r'(111)\qquad\mathcal V_{J\unsure{,|0}}^L\left(\overset{\mathrm{déf}}=\mathcal V_{J,L}^{X_L^*}\right)\overset{(\overset h\sim)}{\hookrightarrow}\mathcal V_{J,L}'
f112 = r'(112)\qquad J_0\prec J_1\prec '+dotrule+r'\prec J_n'
f113row1 = (r'\mathcal V_{J_0,'+dotrule+r',J_n}'
            r'&=\mathcal V_{J_0}\cap '+tworules+r'\cap\mathcal V_{J_n}')
f113row2 = (r'&=\bigcup_{\substack{j_0\in J_0\\'+twodotsrule+r'\\j_n\in J_n}}'
            r'\mathcal V_{j_0j_1'+dotrule+r'j_n}')
f113row3 = (r'&=\underset{\substack{d\in\mathrm{Drap}(J_0\cup J_1\cup '+dotrule+r'\cup J_n)\\'
            r'd\cap J_0\ne\phi,'+twodotsrule+r',d\cap J_n\ne\phi}}{\lim_{\longrightarrow}}\mathcal V_d')
f113 = '(113)\\qquad\\begin{aligned}\n'+f113row1+'\\\\\n'+f113row2+'\\\\\n'+f113row3+'\n\\end{aligned}'
cancel1 = r'\deleted{X}&\deleted{=\unsure{\overline{\mathcal V}_{J}^{L}}}'
cancel2 = r'&\deleted{\unsure{Z\cap\mathcal V_J}}'
cancel3 = r'&\deleted{=\unsure{{}_{*}X\cup\mathcal V_{J\cup L}\cap{}_{*}\mathcal V_L}}'
cancel = '\\begin{aligned}\n'+cancel1+'\\\\\n'+cancel2+'\\\\\n'+cancel3+'\n\\end{aligned}'
candidate = (r'\scanpage{99}'+'\n'+r'\mspage{46}'+'\n\n'+opening+'\n\\[\n'+f109+'\n\\]\n'
             r'\margin{'+margin+'}\n\n'+main+'\n\\[\n'+f110+'\n\\]\n'
             'en particulier\n\\[\n'+f111+'\n\\]\n\nSoient\n\\[\n'+f112+'\n\\]\n'
             'des bandes, on posera\n\\[\n'+f113+'\n\\]\n\n'
             '% The following three-line block is entirely canceled. The lower stars are placed below the baseline; their attachment remains uncertain.\n'
             '\\[\n'+cancel+'\n\\]\n'+r'\margin{98}'+'\n')

changes=[]
def add(place,c,h,final,evidence,crop,confidence,kind,error_kind,against_C,against_H,consequential=False,marked_in_H=False,change_type=None):
    assert c in C, (place,'C',c)
    assert h in H, (place,'H',h)
    d={'id':f'C{len(changes)+1:02d}','place':place,'C':c,'H':h,'final':final,
       'evidence':evidence,'crop':cm[crop]['crop'],'box':cm[crop]['box'],
       'confidence':confidence,'kind':kind,'error_kind':error_kind,
       'against_C':against_C,'against_H':against_H,'consequential':consequential,
       'marked_in_H':marked_in_H}
    if change_type: d['change_type']=change_type
    changes.append(d)
    return d['id']

ids={}
ids['same']=add('opening, after de',r'\unsure{$=$}','même',r'$=$',
 'Two separate short horizontal strokes are visible, with a detached following comma. No letters of même are written. The enlargement resolves M0733 to its first reading.',
 'opening','high','abbreviation expanded or spelling modernised','8 abbreviation/spelling',True,True,change_type='doubt resolution')
ids['phi109']=add('(109), both nonempty conditions',r'd\cap J\ne\varnothing,\,d\cap L\ne\varnothing',r'd\cap J\ne\emptyset,\ d\cap L\ne\emptyset',
 r'd\cap J\ne\phi,\,d\cap L\ne\phi',
 'Each small loop is crossed by a long upright/slanting stem continuing below it. These are phi-shaped written signs; neither is a loop with only an oblique empty-set slash.',
 'formula109','high','misread symbol or index','1 symbols/indices',True,True)
ids['annotation']=add('annotation directly under the sole RHS object of (109)',
 r'\margin{\diagram{\begin{tikzcd}[row sep=small]\mathcal V_d^Z\arrow[d,hook,"(h)"]\\\mathcal V_d\end{tikzcd}}',
 r'sous $\mathcal V^Z_d$, une flèche verticale marquée $\simeq$ (h) vers $\mathcal V_d$',annotation,
 'There is one written upper V_d^Z, the RHS of (109). A square underbracket has short upward ends; below its center a separate straight vertical shaft points down to V_d. The shaft has no hook at its top. A vertically oriented tilde-like curve stands to its right, with (h) farther right. C repeats the upper object and adds a hook; H describes a different similarity glyph and gives no drawn bracket.',
 'annotation_connector','high','drawing or diagram','4 drawing/diagram',True,True,True)
ids['marginold']=add('marginal condition, canceled group before live X_L^*',
 r'\deleted{\unsure{X_J^*\cap}}',r'(un mot biffé devant $X^{*}_L$)',old_margin,
 'The canceled group is mathematical: two diagonals make X, a small upper star has distinct rays and a lower J has a right stem and leftward foot. These three characters are readable and are released from C’s doubt. Only the following arch/relation remains crossed beyond certainty, so cap retains a narrow doubt. H gives only an editorial description of an unspecified word.',
 'marginal_cancellation','medium','omission','3 omissions',True,True,marked_in_H=True,change_type='doubt resolution')
ids['flagdots']=add('last line of marginal note, d tuple',r'd=(i_0,\ldots,i_n)',r'd=(i_0,\ldots,i_n)',
 r'd=(i_0,'+dotrule+r',i_n)',
 'Between the two written commas there is one round dot followed by one short horizontal rule. Three dots are not present. The initial i has a separate dot and its 0 is closed; the final index is n.',
 'marginal_flag','high','misread symbol or index','1 symbols/indices',True,True)
ids['clairement']=add('head of main line leading to (110), canceled word',r'\deleted{clairement}',r'devant « donc si », un mot biffé',r'\deleted{clairement}',
 'The struck word starts with open c and a tall looped l, then a low a/i sequence with a detached i dot; the remaining joined turns end in the high t. A separate horizontal cancellation traverses the entire word. The compressed middle supports clairement; H describes the deletion without transcribing it.',
 'clairement_doncsi','medium','omission','3 omissions',False,True,marked_in_H=True)
ids['doncsi']=add('replacement immediately above canceled clairement',r'\inserted{donc si}',r'donc si \add{',r'\inserted{donc si}',
 'The words donc si occupy their own short interlinear line directly above the canceled clairement. They are replacement ink, not an unmarked continuation of the original baseline.',
 'clairement_doncsi','high','insertion or placement','6 insertion placement',False,True)
ids['mainold']=add('main condition, canceled group before live X_L^*',r'\deleted{\unsure{X_J^*\cap}}',r'\struck{\ill{}}',old_main,
 'X has crossed diagonals, the upper star has separate rays and the lower J has a capped right stem and leftward foot. These characters are individually readable and are released from C’s doubt. The final curved relation is crossed by looping cancellation strokes, so only cap retains a narrow doubt. H leaves the entire group illegible.',
 'main_cancel_clause','medium','readable ink left as \\ill{}','5 readable left illegible',True,True,marked_in_H=True,change_type='doubt resolution')
ids['aura']=add('end of main line immediately before (110)','on aura',r'\ill{},','on aura',
 'The first word has the rounded o and connected n. The next has a low initial a, two u turns, a short r, and final a. No detached comma follows the final a; the existing comma precedes on.',
 'on_aura','high','readable ink left as \\ill{}','5 readable left illegible',False,True,marked_in_H=True)
ids['label110']=add('(110), label over hooked arrow',r'\overset{(\overset h\sim)}{\hookrightarrow}',r'\overset{(h)}{\hookrightarrow}',r'\overset{(\overset h\sim)}{\hookrightarrow}',
 'The small h sits above a wavy tilde; parentheses flank the tilde level. The long horizontal arrow has a curled left hook and a small right head. H drops the visible tilde and relocates h into its parentheses.',
 'formula110','high','misread symbol or index','1 symbols/indices',False,True,False)
ids['mark111']=add('(111), small mark immediately after the first subscript J',r'\mathcal V_J^L',r'\mathcal V^L_J',r'\mathcal V_{J\unsure{,|0}}^L',
 'A detached dark curled mark follows J at the lower right, before the large opening parenthesis. Its upper lobe and descending hooked return are separate from the J foot. It may be a comma or a heavily filled 0; the ink is present but its identity is not secure. Neither witness represents it.',
 'definition111_detail','low','omission','3 omissions',True,True,True)
ids['label111']=add('(111), label over hooked arrow',r'\overset{(\overset h\sim)}{\hookrightarrow}',r'\overset{(h)}{\hookrightarrow}',r'\overset{(\overset h\sim)}{\hookrightarrow}',
 'As in (110), a short upright h is above a curved tilde, with parentheses around the tilde level. The two levels remain separate in the enlarged whole formula; H omits the lower sign.',
 'formula111','high','misread symbol or index','1 symbols/indices',False,True,False)
ids['posera']=add('prose immediately before (113)','posera','pose','posera',
 'After the descending p and low o-s-e sequence there is a short r turn followed by a final a. The longer ending is visibly written, not merely a terminal stroke of e.',
 'posera','high','misread word','2 words',False,True)
ids['chain112']=add('(112), continuation between J_1 and J_n',r'J_0\prec J_1\prec\cdots\prec J_n',r'J_0\prec J_1\prec\cdots\prec J_n',
 r'J_0\prec J_1\prec '+dotrule+r'\prec J_n',
 'The continuation consists of one round dot followed by one longer horizontal rule; it has two components, not three dot marks. Both prec signs around it are separate angular curves.',
 'formula112','high','misread symbol or index','1 symbols/indices',True,True)
ids['lhs113']=add('(113), LHS tuple continuation',r'\mathcal V_{J_0,\ldots,J_n}',r'\mathcal V_{J_0,\ldots,J_n}',
 r'\mathcal V_{J_0,'+dotrule+r',J_n}',
 'There is a written low comma after J_0, then a detached dot and one horizontal rule at the index baseline, then a second low comma before J_n. The first dot is not the upper half of a semicolon.',
 'formula113_first','high','misread symbol or index','1 symbols/indices',True,True)
ids['inter113']=add('(113), first-row intersection continuation',r'\mathcal V_{J_0}\cap\cdots\cap\mathcal V_{J_n}',r'\mathcal V_{J_0}\cap\cdots\cap\mathcal V_{J_n}',
 r'\mathcal V_{J_0}\cap '+tworules+r'\cap\mathcal V_{J_n}',
 'The two components between the intersection arches are short horizontal rules, the second longer than the first. There is no third dot or stroke.',
 'formula113_first','high','misread symbol or index','1 symbols/indices',True,True)
ids['union113']=add('(113), middle line beneath big union',r'j_0\in J_0\\\cdots\\j_n\in J_n',r'j_0\in J_0\\ \cdots\\ j_n\in J_n',
 r'j_0\in J_0\\'+twodotsrule+r'\\j_n\in J_n',
 'The middle condition line contains two distinct rounded dots followed by a short nearly horizontal rule. All three marks are present but the last is drawn as a rule.',
 'formula113_union','high','misread symbol or index','1 symbols/indices',True,True)
ids['jtuple113']=add('(113), indices of V in the union expression',r'\mathcal V_{j_0j_1\ldots j_n}',r'\mathcal V_{j_0 j_1\ldots j_n}',
 r'\mathcal V_{j_0j_1'+dotrule+r'j_n}',
 'The j_0 and j_1 are followed by one dot and one short rule before the final j_n. No commas are written in this index string. The lower j loops and the numeric 0/1 are distinct.',
 'formula113_union','high','misread symbol or index','1 symbols/indices',True,True)
ids['drap113']=add('(113), Drap union argument',r'J_0\cup J_1\cup\cdots\cup J_n',r'J_0\cup J_1\cup\cdots\cup J_n',
 r'J_0\cup J_1\cup '+dotrule+r'\cup J_n',
 'Between the third union sign and the final union sign lie only one round dot and one short horizontal rule. The preceding index is 1 and the final index is n.',
 'formula113_limit','high','misread symbol or index','1 symbols/indices',True,True)
ids['condition113']=add('(113), continuation between the two nonempty conditions',r',\ldots,',r',\ldots,',
 r','+twodotsrule+r',',
 'After the first comma there are two separate dots and one short rule, followed by a second comma. This row records the continuation marks only; the phi shapes are recorded separately.',
 'formula113_limit','high','misread symbol or index','1 symbols/indices',True,True)
ids['phi113']=add('(113), both nonempty-condition glyphs',r'\varnothing',r'\emptyset',
 r'\phi',
 'Each final sign has a small oval and a long stem extending above/below it. They repeat the phi-shaped signs in (109). This row records only those two signs; the continuation between them has its own row.',
 'formula113_limit','high','misread symbol or index','1 symbols/indices',True,True)
ids['cancelX']=add('canceled block, initial X',r'\unsure{X}',r'\struck{\ill{}}',r'\deleted{X}',
 'The initial character has two clear crossing diagonals below/left of the first equals sign. The long additional sweeps belong to the cancellation. It reads X despite the cancellation, so the C doubt is resolved for this character only.',
 'cancelled_top','high','readable ink left as \\ill{}','5 readable left illegible',True,True,marked_in_H=True,change_type='doubt resolution')
ids['cancelRHS']=add('canceled block, first-row RHS',r'\unsure{\overline{\mathcal V}_{J}^{L}}',r'\struck{\ill{}}',r'\deleted{\unsure{\overline{\mathcal V}_{J}^{L}}}',
 'A large V-like looping character, a lower J-like hooked form, an upper L-like upright, and a detached short bar survive within the crossings. The bar is offset to the right and its scope is not certain; the complete RHS remains a tentative C reading. The two bars of the preceding equals sign are separately visible.',
 'cancelled_top','low','readable ink left as \\ill{}','5 readable left illegible',False,True,marked_in_H=True)
ids['cancelmiddle']=add('canceled block, second row',r'\unsure{Z\cap\mathcal V_J}',r'\struck{\ill{}}',r'\deleted{\unsure{Z\cap\mathcal V_J}}',
 'A small initial angular Z-like stroke and a following arch are visible, with a larger V-like loop crossed by several diagonal strokes. The right-hand/subscript extent cannot be separated reliably, so the complete row remains doubtful. No equals sign is supplied to this row.',
 'cancelled_middle','low','readable ink left as \\ill{}','5 readable left illegible',False,True,marked_in_H=True)
ids['cancelbottom']=add('canceled block, last row and lower star placement',r'\unsure{X^*\cup\mathcal V_{J\cup L}\cap\mathcal V_L^*}',r'\struck{\ill{}}',
 r'\deleted{=\unsure{{}_{*}X\cup\mathcal V_{J\cup L}\cap{}_{*}\mathcal V_L}}',
 'The equals sign at the far left and two small stars at the lower edge survive. The first star lies below and left of the X-like crossing; the second is low and left of the final V-like character, not above it. The intervening letters, relation signs, and exact star attachments are still obscured by multiple cancellation sweeps. Their tentative grouping is retained with uncertainty, but C’s high superscript positions are not asserted.',
 'cancelled_bottom','low','misread symbol or index','1 symbols/indices',True,True,True,True)
ids['folio']=add('bottom-left foliation in the lighter other hand',r'\margin{98}','',r'\margin{98}',
 'The lighter, thinner pair has a rounded upper bowl and descending stem for 9, then two joined loops for 8. It is separate from the darker authorial 46 and is encoded as a margin item. H omits it.',
 'folio98','high','omission','3 omissions',False,True)

# Map every supplied difference; the token aligner sometimes splits a single formula.
diff_coverage=[]
mapping={
 'D0817':('editorial-only',[],'C’s scanpage marker and H’s editorial location phrase are framing, not competing manuscript wording. The written 46 is retained.'),
 'D0818':('editorial-only',[],'H’s attribution and statement that this is the last page are editorial; there is no corresponding sentence on the manuscript.'),
 'D0819':('reading',[ids['same']],'The written equality-shaped abbreviation is recovered and M0733 settled.'),
 'D0820':('macro-only',[],'Z is the same superscript; source order relative to subscript differs.'),
 'D0821':('macro-only',[],'Same superscript Z in the same position; no reading difference.'),
 'D0822':('macro-only',[],'underset/lim and varinjlim source syntax place the same written conditions under the limit.'),
 'D0823':('alignment-only',[],'Both witnesses contain d at the beginning of the lower condition; a line-break macro disrupts token alignment.'),
 'D0824':('alignment-only',[],'Both witnesses contain the comma between nonempty conditions; spacing commands affect token alignment.'),
 'D0825':('alignment-only',[ids['annotation']],'The sole upper RHS V_d^Z is common; the annotation treatment is accounted for in the diagram row.'),
 'D0826':('reading',[ids['annotation']],'C/H representations of the underbracket, vertical arrow, and label differ; a drawn version now follows the ink.'),
 'D0827':('reading',[ids['annotation']],'C duplicates the upper RHS object in a detached diagram; there is only one upper V_d^Z on the page.'),
 'D0828':('reading',[ids['annotation']],'The hook in C and H’s textual similarity description do not match the straight vertical tail and vertical tilde-like mark.'),
 'D0829':('reading',[ids['marginold']],'The marginal canceled mathematical group is not an unspecified word; a narrow unresolved formula is retained.'),
 'D0830':('reading',[ids['marginold']],'Continuation of the same canceled mathematical group; its final relation remains doubtful.'),
 'D0831':('alignment-only',[ids['marginold']],'The live X_L^* is common to both; the earlier canceled group causes displaced token matching.'),
 'D0832':('macro-only',[],'Star/index source order differs for the same X_{i_n}^*.'),
 'D0833':('macro-only',[],'Same star and i_n index; no ink difference.'),
 'D0834':('reading',[ids['clairement'],ids['doncsi']],'H’s trailing marginal editorial note aligns against C’s next canceled word. The actual canceled clairement and its replacement are logged.'),
 'D0835':('reading',[ids['mainold']],'H leaves the main canceled mathematical group illegible; X/J/star are recovered after full-clause review, with only cap still doubtful.'),
 'D0836':('reading',[ids['mainold']],'Same main canceled group, including its still uncertain final relation.'),
 'D0837':('alignment-only',[ids['mainold']],'The live X_L^* is shared; the difference is displaced by the canceled group.'),
 'D0838':('reading',[ids['aura']],'on aura is readable and no comma follows it.'),
 'D0839':('macro-only',[],'Superscript Z placement is unchanged; only source ordering differs.'),
 'D0840':('macro-only',[],'Same Z on the first object of (110).'),
 'D0841':('editorial-only',[],'H describes cancellation and retracing. The manuscript states neither sentence. Retracing of the RHS subscript is recorded in doubts.'),
 'D0842':('macro-only',[],'Superscript L is common; source ordering differs.'),
 'D0843':('macro-only',[],'Same superscript L. The separate small mark after J is an independent agreed-witness omission, logged separately.'),
 'D0844':('macro-only',[],'The entire X_L^* is the superscript of V in both witnesses; source order differs.'),
 'D0845':('macro-only',[],'Same nested star/index placement in the definition.'),
 'D0846':('reading',[ids['posera']],'Final ra is visibly written after pose.'),
 'D0847':('macro-only',[],'aligned is a layout environment, not manuscript text.'),
 'D0848':('alignment-only',[],'Both witnesses have j_n in the lower union condition; line-break syntax disrupts alignment.'),
 'D0849':('macro-only',[],'Whitespace between math subscript tokens does not introduce a manuscript comma or alter the j_0 j_1 string.'),
 'D0850':('macro-only',[],'underset versus varinjlim syntax places the same condition beneath the written limit.'),
 'D0851':('alignment-only',[],'Both witnesses include d at the start of the second line of conditions.'),
 'D0852':('macro-only',[],'Both forms represent a right-pointing limit arrow. The enlarged tip confirms the direction.'),
 'D0853':('macro-only',[],'Closing aligned is layout syntax.'),
 'D0854':('reading',[ids['cancelX'],ids['cancelRHS'],ids['cancelmiddle'],ids['cancelbottom'],ids['folio']],'The canceled block and other-hand 98 are ink. H’s statements about the dossier ending are editorial and are excluded.')
}
for row in packet['differences']:
    classification,change_ids,reason=mapping[row['diff_id']]
    diff_coverage.append({'diff_id':row['diff_id'],'classification':classification,'change_ids':change_ids,'reason':reason})

inventory=[]
def inv(element,kind,position,words,hand='author',sheet_kind='text'):
    inventory.append({'sheet_kind':sheet_kind,'hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('authorial page number','margin note','top left','46')
inv('opening sentence','text','upper main column','On aura de =, pour J et L quelconques')
inv('formula (109)','display','upper main column','V_{J,L}^Z = lim V_d^Z')
inv('annotation attached to RHS of (109)','diagram','below the RHS of (109)','square underbracket; downward arrow; vertical tilde-like sign; (h); V_d')
inv('five-line marginal condition','margin note','upper right','si J prec L, J et L des bandes')
inv('canceled mathematical group in margin','deletion','third marginal line','X_J^* cap (doubtful last sign)')
inv('canceled clairement','deletion','left of main edited sentence','clairement')
inv('replacement donc si','insertion','above canceled clairement','donc si')
inv('inserted bands/order condition','insertion','above Z contient with a curved insertion leader','J,L des bandes et J prec L, et si')
inv('edited main condition','text','between (109) and (110)','Z contient ... X_L^*, on aura')
inv('canceled mathematical group in main condition','deletion','before live X_L^*','X_J^* cap (doubtful last sign)')
inv('formula (110)','display','upper middle','V_{J,L}^Z hooked arrow V_{J,L}; h above tilde')
inv('transition','text','below (110)','en particulier')
inv('formula (111)','display','middle','V_J^L (def = V_{J,L}^{X_L^*}) hooked arrow V_{J,L}')
inv('introductory word','text','below (111)','Soient')
inv('formula (112)','display','middle lower','J_0 prec J_1 prec dot-rule prec J_n')
inv('definition introduction','text','above (113)','des bandes, on posera')
inv('formula (113), first row','display','lower half','V_{J_0,dot-rule,J_n} = intersection')
inv('formula (113), second row','display','lower half','big union over j_0 in J_0 through j_n in J_n')
inv('formula (113), third row','display','lower half','limit over flags d with two nonempty conditions')
inv('canceled draft block','deletion','bottom main area','X = ...; Z cap ...; = ... lower stars',sheet_kind='cancelled_draft')
inv('other-hand foliation','margin note','bottom left','98',hand='other hand: thin, light foliation')

second_boxes=[]
def blind(kind,box,reading):
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,'x0':box[0],'y0':box[1],'x1':box[2],'y1':box[3],'reading':reading})
blind('authorial page number',cm['page46']['box'],r'\mspage{46}')
blind('different word and resolved M0733',cm['opening']['box'],opening)
blind('whole numbered formula and attached diagram',[240,158,1255,470],f109)
blind('whole marginal note, canceled group, tuple digits',cm['margin_note']['box'],r'\margin{'+margin+'}')
blind('canceled word and replacement',cm['clairement_doncsi']['box'],r'\deleted{clairement} \inserted{donc si}')
blind('whole interlinear insertion, attachment and main canceled clause',[500,470,1190,625],r'\inserted{$J,L$ des bandes et $J\prec L$, et si} $Z$ contient $'+old_main+r'X_L^*$')
blind('different words',cm['on_aura']['box'],'on aura')
blind('whole numbered formula, h/tilde, retraced subscript',cm['formula110']['box'],f110)
blind('whole numbered formula, small added subscript mark, def label, h/tilde',cm['formula111']['box'],f111)
blind('whole numbered order chain and digits',cm['formula112']['box'],f112)
blind('different verb',cm['posera']['box'],'des bandes, on posera')
blind('whole numbered three-row formula, all numerical indices and continuation marks',cm['formula113']['box'],f113)
blind('whole canceled formula block',cm['cancelled_block']['box'],cancel)
blind('other-hand foliation',cm['folio98']['box'],r'\margin{98}')

record={
 'page':PAGE,'cote':'150','scan':99,'reader':'reader_a / GPT-6 Astra Pro / effort not exposed / run SP92',
 'line_count':25,
 'line_count_note':'25 principal written baselines: 15 main prose/display/canceled rows, two interlinear insertion/replacement baselines, five marginal prose/tuple lines, the lower node of the attached arrow, and both handwritten page/folio baselines (46 and 98). Subscript/superscript condition stacks belong to their display baselines.',
 'half_review':'Whole original viewed once for layout; native half1 [0,0,1682,1298] and half2 [0,1062,1682,2360] each viewed once. Every main line, all five numbered formulas, the attached vertical annotation, the five-line marginal note, all corrections, the canceled bottom block, and both foliation numbers were read against both witnesses. All 28 final saved crops were personally viewed; three were reframed to restore full upper formula extents and then viewed again. No OCR, research, or TeX compilation was used.',
 'deletion_insertion_review':[
  {'place':'marginal X_J^* cap','state':'deleted','bounds':'Only the compact mathematical group preceding the separate live X_L^* is crossed; the live X_L^* and following comma/donc remain unstruck.','attachment':'Inside the condition Z contient, before the surviving X_L^*.','reading':old_margin,'confidence':'low','crop':cm['marginal_cancellation']['crop'],'box':cm['marginal_cancellation']['box']},
  {'place':'clairement','state':'deleted','bounds':'One horizontal cancellation traverses the word from its opening c/l to final t; it does not cancel the words above.','attachment':'Former head of the main sentence leading to (110).','reading':r'\deleted{clairement}','confidence':'medium','crop':cm['clairement_doncsi']['crop'],'box':cm['clairement_doncsi']['box']},
  {'place':'donc si','state':'inserted replacement','bounds':'The two words on the short line above clairement.','attachment':'Replaces the canceled head word; followed by the longer inserted condition.','reading':r'\inserted{donc si}','confidence':'high','crop':cm['clairement_doncsi']['crop'],'box':cm['clairement_doncsi']['box']},
  {'place':'J,L des bandes et J prec L, et si','state':'inserted','bounds':'Entire raised phrase, ending at si. The long curved stroke beneath it is an insertion leader, not an enclosing parenthesis.','attachment':'Placed between donc si and Z contient, with the leader turning down before Z.','reading':r'\inserted{$J,L$ des bandes et $J\prec L$, et si}','confidence':'high','crop':cm['insertion']['crop'],'box':cm['insertion']['box']},
  {'place':'main X_J^* cap','state':'deleted','bounds':'Compact mathematical group after contient; the following separate X_L^* is live. Crossings obscure the final relation.','attachment':'Before the surviving X_L^* in the main condition.','reading':old_main,'confidence':'low','crop':cm['main_cancel_clause']['crop'],'box':cm['main_cancel_clause']['box']},
  {'place':'RHS subscript in (110)','state':'overwritten/retraced; prior character not securely recoverable','bounds':'The first subscript is very dark on top, right, and bottom, with a lighter extra left vertical.','attachment':'First subscript of the target V, before comma and L.','reading':r'\unsure{J|\square}','confidence':'low','crop':cm['rhs110_J']['crop'],'box':cm['rhs110_J']['box']},
  {'place':'bottom three-line block','state':'deleted in its entirety','bounds':'Long looping and diagonal cancellation strokes cross all three formula rows. The two low stars are within the canceled block.','attachment':'Separate abandoned draft below (113), not a continuation of its live equality.','reading':cancel,'confidence':'low','crop':cm['cancelled_block']['crop'],'box':cm['cancelled_block']['box']}
 ],
 'changes':changes,'diff_coverage':diff_coverage,
 'decisions':[{'id':'M0733','cote':'150','scan':'99','decision':'first','reading':r'$=$','ink':'Two distinct horizontal bars followed by a comma; no written letters of même.','crop':cm['opening']['crop'],'box':cm['opening']['box'],'confidence':'high'}],
 'inventory':inventory,
 'notes':'''# 150_scan099 — reader A

The authorial number is 46. The lighter 98 at the lower left is a separate foliation hand and is retained with the margin convention. There is no written title or date. H’s statements that this is the dossier’s final page and that the dossier ends here are editorial framing, not manuscript sentences.

The page writes (109), a flag-indexed limit expression for V_{J,L}^Z for arbitrary J and L, with two nonempty conditions. The only RHS V_d^Z also serves as the upper object of a downward annotated arrow to V_d. Its square underbracket, straight tail, vertical tilde-like mark, and (h) are preserved as diagram geometry. The accompanying marginal condition concerns ordered bands, containment of X_L^*, and the top member i_n of a flag. The main line repeats the condition after replacing clairement with donc si and adding the raised bands/order phrase. Displays (110) and (111) have hooked arrows with h above a parenthesized tilde. The page then introduces ordered bands in (112) and defines V for their tuple by an intersection, a union, and a flag-indexed limit in (113). This is a report of what the page writes, not a proof verification.

## Ink-triggered rereadings

M0733 is the written equality-shaped abbreviation for même. Four nonempty signs, two in (109) and two in (113), have phi stems and are transcribed literally as phi. Both limit arrows have compact right heads; the (109) tip was separately enlarged. All continuation sequences were counted as actual ink: dot followed by rule in the marginal tuple and (112); in (113), dot-rule in the LHS tuple, two rules in the intersection chain, two dots and a rule in the union condition stack and between nonempty conditions, and dot-rule in the j-index string and Drap argument. No conventional three-dot ellipsis is silently supplied.

The target subscript of (110) is heavily retraced; a rectangular final contour overlaps a J-shaped right stem and left foot, so it is left narrowly doubtful. A small separate curled mark follows the initial J in (111); both witnesses omit it, and its identity as comma or filled 0 remains uncertain. The detached stroke above e in déf is present. The main verb is posera, with final r and a; on aura is readable and has no following comma.

## Revisions and bounds

The canceled head word reads clairement at medium confidence. donc si is written above it. The longer phrase J,L des bandes et J prec L, et si is attached before Z contient by a continuous curved leader; the curved line is not punctuation. In each of the main and marginal containment clauses, the old X_J^* plus following relation is crossed and the separate X_L^* remains live. X has two diagonals, the star has distinct rays, and J has a capped right stem and leftward foot: these characters are released from the C doubts after crop inspection. Only the following relation remains narrowly doubtful as cap. The entire bottom three-row formula block is canceled. Its initial X and two equal signs are visible, but the first RHS bar scope, middle row, and most of the final row remain doubtful. Two final-row stars lie low and left of the X-like crossing and final V-like character; they are not silently promoted to superscripts. Their precise attachment is still uncertain.

There is no securely written authorial question mark or explicit verbal doubt on the page. The transcription’s uncertainty marks identify reading limits. No mathematical slip is repaired from context, and no proof or computational check was performed. A tiny contact dot by the lower left of the big union is not in the position of a disjoint-union marker and is treated as incidental pen contact, not an extra mathematical operator.
''',
 'check_events':[],
 'notation':[
  {'sign':r'= in de =','reading':'literal abbreviation for même','evidence':'Two short horizontal strokes; M0733 resolved on opening crop.'},
  {'sign':r'\phi','reading':'literal phi-shaped empty-condition glyph','evidence':'All four loops have long stems, two in (109), two in (113).'},
  {'sign':'continuation marks','reading':'explicit dot/rule counts, not normalized ellipses','evidence':'Dot-rule in marginal tuple, (112), and three locations of (113); two rules in its intersection; two dots plus rule in two other locations.'},
  {'sign':'annotation of V_d^Z','reading':'square underbracket, plain downward arrow, vertical tilde-like mark, (h), V_d','evidence':'The single upper object is shared with (109), and the tail has no curl.'},
  {'sign':r'(\overset h\sim)','reading':'h above parenthesized tilde','evidence':'Both (110) and (111) show two vertically distinct label levels.'},
  {'sign':'small mark following first J in (111)','reading':'comma or filled 0, unresolved','evidence':'A detached two-turn curled mark is visible to the lower right of J.'},
  {'sign':'low stars in canceled final row','reading':'placement low; attachment unresolved','evidence':'Two multi-ray stars lie along the lower edge of the canceled block, not at ordinary superscript height.'}
 ],
 'hand_log':[
  {'habit':'Uses = as a word abbreviation for même','places':['opening sentence'],'scope':'this page','witness_errors':'H expands the abbreviation; C marks it doubtful although the two bars are distinct.'},
  {'habit':'Draws phi-shaped signs in nonempty tests','places':['(109), two signs','(113), two signs'],'scope':'this page','witness_errors':'C/H normalize to varnothing/emptyset.'},
  {'habit':'Continuation writing mixes rounded dots and short rules with variable counts','places':['marginal flag tuple','(112)','six locations in (113)'],'scope':'this page','witness_errors':'Both witnesses regularize to ldots/cdots.'},
  {'habit':'Small h written above a parenthesized tilde','places':['(110)','(111)'],'scope':'this page','witness_errors':'H retains only (h).'},
  {'habit':'Heavy retracing can close a J-shaped character into a rectangle','places':['target first subscript in (110)'],'scope':'this page; not a global resolution rule','witness_errors':'Both witnesses print plain J; H at least notes the overwriting.'},
  {'habit':'Very compressed low joins in words, with final ra still written','places':['on aura','on posera','clairement'],'scope':'this page','witness_errors':'H leaves on aura illegible, shortens posera to pose, and does not transcribe the canceled head word.'},
  {'habit':'Large looping cancellation sweeps obscure old symbols and must not be read as bars or punctuation automatically','places':['two X_J^* groups','bottom canceled block'],'scope':'this page','witness_errors':'C’s tentative formulas remain uncertain; H omits most of the underlying ink.'}
 ],
 'abbreviations':[{'form':'=','expansion':'même'},{'form':'déf','expansion':'définition'},{'form':'Drap','expansion':'drapeaux (notation; no expansion in transcription)'}],
 'doubts':[
  {'place':'marginal canceled group, final relation only','reading':r'X_J^*\unsure{\cap}','alternatives':'Final relation uncertain; X/J/star resolved.','confidence':'low','reason':'Diagonal and horizontal deletion strokes coincide with the relation’s upper/lower curves; uncertainty is confined to this sign.'},
  {'place':'main canceled group, final relation only','reading':r'X_J^*\unsure{\cap}','alternatives':'Final relation uncertain; X/J/star resolved.','confidence':'low','reason':'The heavy curling cancellation obstructs the sign after J; no semantic completion used.'},
  {'place':'(110), target first subscript','reading':r'\unsure{J|\square}','alternatives':'J or literal closed rectangular mark; older underlying letter is not recoverable.','confidence':'low','reason':'Dark top/right/bottom resembles J, but a lighter left vertical closes the contour.'},
  {'place':'(111), detached mark after initial J','reading':r'J\unsure{,|0}','alternatives':'Comma, filled 0, or retraced terminal mark.','confidence':'low','reason':'The isolated curled mark has an upper dark lobe and long downward return; its presence is clear but identity/attachment uncertain.'},
  {'place':'canceled block, first RHS','reading':r'\unsure{\overline{\mathcal V}_J^L}','alternatives':'Bar scope and right-hand upper character uncertain.','confidence':'low','reason':'A short detached bar is visible to the right of the main V-like loop; overlapping diagonal cancellations prevent a secure grouping.'},
  {'place':'canceled block, second row','reading':r'\unsure{Z\cap\mathcal V_J}','alternatives':'Z, arch, V-like loop and subscript grouping remain tentative.','confidence':'low','reason':'Multiple long cancellation sweeps conceal character boundaries; no equals sign supplied.'},
  {'place':'canceled block, last row','reading':r'\unsure{{}_{*}X\cup\mathcal V_{J\cup L}\cap{}_{*}\mathcal V_L}','alternatives':'Relations, index grouping, and low-star attachments uncertain.','confidence':'low','reason':'Two low stars and an equals sign survive, but most letter/index boundaries coincide with canceling loops.'}
 ],
 'second_boxes':second_boxes,
 'crops':[{'place':name,**v,'viewed':True,'method':'Pillow crop from assigned original; LANCZOS enlargement, autocontrast, sharpness 1.15; no rotation'} for name,v in cm.items()]
}

assert len(diff_coverage)==38
assert set(mapping)=={x['diff_id'] for x in packet['differences']}
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert all((WORK/x['crop']).exists() for x in changes)
assert [x['id'] for x in record['decisions']]==[x['id'] for x in packet['marks']]
(WORK/'records'/(PAGE+'.tex')).write_text(candidate)
(WORK/'records'/(PAGE+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {PAGE}: {len(changes)} changes, {len(diff_coverage)} diffs, {len(record["decisions"])} mark, {len(inventory)} inventory entries, {len(second_boxes)} blind boxes, {len(cm)} crops.')
