from pathlib import Path
import json
from datetime import datetime, timezone

HERE = Path(__file__).parent
WORK = HERE.parent.parent
PACKET = Path('/workspace/scratch/ea90d891106a/runtime/packets/147_scan075')
boxes = json.loads((HERE / 'crop_boxes.json').read_text())
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

fig1 = r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.20,.03)--(.70,.07)--(1.30,.14);
\draw (1.50,.14)--(2.63,.23);
\draw (2.82,.23)--(3.72,.30);
\draw (3.99,.30)--(4.65,.31)--(5.24,.36);
\draw (5.86,.38)--(5.98,.38) (6.18,.40)--(6.40,.44)--(6.54,.43);
\draw (7.42,.47)--(8.54,.60);
\fill (0,0) ellipse (.09 and .045);
\fill (1.30,.14) circle (1.4pt);
\fill (2.63,.23) circle (1.4pt);
\fill (3.72,.30) circle (1.4pt);
\fill (5.24,.36) circle (1.4pt);
\draw[line width=.55pt] (8.95,.56)
 .. controls (8.79,.50) and (8.66,.59) .. (8.72,.69)
 .. controls (8.77,.76) and (8.93,.74) .. (8.93,.66);
\fill (8.82,.70) ellipse (.075 and .045);
\node[above] at (0,.24) {$(c_1,c_2)$};
\node[below] at (0,-.16) {$\unsure{C|c}$};
\node[above] at (1.30,.42) {$c_3$};
\node[above] at (2.63,.62) {$c_{i-1}$};
\node[above] at (3.72,.66) {$(c_i,c_{i+1})$};
\node[above] at (5.24,.73) {$c_{i+2}$};
\node[above] at (8.81,.94) {$c_\nu$};
\end{tikzpicture}}'''

fig2 = r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (-1.01,-.09)--(-.98,-.10) (-.86,-.09)--(-.81,-.08)
 (-.68,-.10)--(-.47,-.05);
\draw (.19,.02)--(.69,.06)--(.88,.05);
\draw (1.17,.06)--(1.80,.07)--(2.10,.11);
\draw (2.31,.09)--(2.59,.16)--(3.22,.20);
\fill (0,0) circle (1.4pt);
\fill (.98,.07) circle (1.4pt);
\fill (2.10,.11) circle (1.4pt);
\fill (3.22,.20) circle (1.4pt);
\fill (.06,-.20) circle (.7pt);
\fill (3.60,.21) circle (.65pt);
\draw (3.72,.20)--(3.79,.22) (3.90,.22)--(4.00,.23)
 (4.09,.25)--(4.18,.25);
\node[above] at (.05,.29) {$c_{i-1}$};
\node[above] at (.98,.34) {$c_i$};
\node[above] at (2.10,.40) {$c_{i-1}$};
\node[above] at (3.22,.49) {$\unsure{c_{i-2}|c_{i+2}}$};
\end{tikzpicture}}'''

fig3 = r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (-.94,-.05)--(-.89,-.07) (-.80,-.06)--(-.65,-.06)
 (-.55,-.06)--(-.38,-.04);
\draw (.20,-.04)--(.69,0)--(.98,.01);
\draw (1.36,.03)--(1.80,.02)--(2.34,.05);
\draw (2.70,.08)--(3.25,.09)--(3.35,.07)--(3.51,.12);
\fill (0,0) circle (1.4pt);
\fill (1.11,.04) circle (1.3pt);
\fill (2.46,.09) circle (1.3pt);
\fill (3.61,.09) ellipse (.025 and .045);
\fill (4.13,.22) circle (.65pt);
\draw (4.27,.23)--(4.39,.25) (4.47,.26)--(4.55,.26);
\node[above] at (.12,.26) {$c_{i-1}$};
\node[above] at (1.17,.32) {$c_{i+1}$};
\node[above] at (2.27,.48) {$c_i$};
\node[above] at (3.69,.40) {$c_{i+2}$};
\end{tikzpicture}}'''

opening = r'''diagramme qui est déterminé, à isom. unique près, en se donnant un ordre total sur $I$, \inserted{(défini} mod \deleted{\unsure{interversion}} \inserted{transposition} des deux premiers él, et des deux derniers). Pour montrer que deux ordres totaux sur $I$ définissent \deleted{\unsure{une}} des pts de $M^\infty_{0,\nu}$ qui appartiennent à une $=$ composante connexe, il \inserted{suffit de} montrer que deux ordres totaux déduits l'un de l'autre par \inserted{transposition des deux} \unsure{$\varepsilon$|$\in$} $c_i,c_{i+1}$ élts consécutifs sont dans la $=$ composante connexe. Or on le voit en notant qu'on a deux morphismes de générisation \deleted{\unsure{de}} \inserted{dans}'''
closing = r'''en contractant la \deleted{\unsure{seg}} \inserted{arête} qui joint $c_i$ et $\unsure{c_{i-1}|c_{i+1}}$, OK.'''
proposed = '\\scanpage{75}\n' + opening + '\n' + fig1 + '\nprovient de\n' + fig2 + '\net de\n' + fig3 + '\n' + closing + '\n\\margin{74}\n'
(HERE / 'proposed.tex').write_text(proposed)

def figures(s):
    answer=[]
    start=0
    while (start:=s.find(r'\figure{',start)) >= 0:
        pos=start+len(r'\figure')
        depth=0
        for end in range(pos,len(s)):
            if s[end]=='{' and (end==0 or s[end-1]!='\\'): depth+=1
            if s[end]=='}' and (end==0 or s[end-1]!='\\'):
                depth-=1
                if depth==0:
                    answer.append(s[start:end+1]);start=end+1;break
        else: raise ValueError('Unclosed figure')
    return answer

Cfig=figures(C)
Hfig=[r'\['+v.split(r'\]')[0]+r'\]' for v in H.split(r'\[')[1:]]
changes=[]
def change(place,c,h,final,evidence,crop,confidence='high',against_C=False,against_H=True,kind='misread word',marked=False,error='words',consequential=False):
    changes.append(dict(id=f'075-{len(changes)+1:02d}',place=place,C=c,H=h,final=final,evidence=evidence,crop=f'147_scan075_place{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked,error_sheet_kind=error,consequential=consequential))

change('Opening word','diagramme','diagrammes','diagramme','The terminal e turns out into the following space; no independent terminal s follows it. The dark retracing at the initial d is part of the letter, not a separate deletion.','01')
change('Opening predicate','qui est déterminé',r"qui ont \uncertain{ceci} de \uncertain{commun}",'qui est déterminé','After the q-descender and dotted i are the short e-s-t group, then the long t, successive reduced loops and final accented e of déterminé. There is a comma after that word.','01',marked=True)
change('End of first baseline','à isom. unique',r"\uncertain{à savoir} qu'ils \uncertain{sont}",'à isom. unique','The abbreviated isom. has a separate terminal dot. The next word has the q-descender and final ue of unique; the long phrase supplied by H does not fit the written groups.','01',marked=True)
change('Second baseline','près, en se donnant',r'\uncertain{donnés} par','près, en se donnant','The first word has a p-descender and terminal s before a comma; two short groups en se precede donnant, whose terminal t is angular. There is no par at this place.','02',marked=True)
change('Insertion before mod',r'\inserted{(défini}',r'\uncertain{(défini}',r'\inserted{(défini}','The opening parenthesis and défini stand above the baseline. Their bent insertion connector descends to the space before mod; this is an insertion, not baseline text.','03',kind='insertion or placement',marked=True,error='insertions put in wrong place')
change('Word before canceled interversion','mod',r'\uncertain{à}','mod','The baseline has an initial low m group, a reduced o, and a tall final d. It is mod, not a single accented a.','03',marked=True)
change('Canceled word after mod',r'\deleted{\unsure{interversion}}',r'\struck{\ill{}}',r'\deleted{\unsure{interversion}}','The initial i/t strokes and the later loops and tail are compatible with interversion, but the horizontal strike covers its central letters. The canceled original lies below the replacement transposition; H puts its struck placeholder after its inline transposition. This is an unresolved tentative reading, not a claim that all of H’s illegible span is securely deciphered.','03',confidence='low',kind=r'readable ink left as \ill{}',marked=True,error='readable ink left as illegible')
change('Replacement above canceled word',r'\inserted{transposition}',r'\uncertain{transposition}',r'\inserted{transposition}','The replacement is on the interline above the struck baseline word; its tall initial t and p-descender are independent of the cancellation. H gives the word in the ordinary line.','03',kind='insertion or placement',marked=True,error='insertions put in wrong place')
change('After replacement transposition','',r'\uncertain{près}','','After the replacement, the live baseline continues directly with des deux premiers. There is no separate p-descender or letter group for près at this position.','03',kind='text not on the page',marked=True,error='text not on page')
change('After premiers','él,','','él,','A short accented two-letter group stands between premiers and its comma, before the separate et at the right. H omits this abbreviated word and comma.','03',kind='omission',error='omissions')
change('Cancellation after définissent',r'\deleted{une}',r'\struck{\ill{}}',r'\deleted{\unsure{une}}','Small upper humps survive above the thick cancellation and support une tentatively. The strike prevents a letter-by-letter resolution; the extra doubt relative to C changes certainty only.','04',confidence='low',kind=r'readable ink left as \ill{}',marked=True,error='readable ink left as illegible')
change('First composante connexe phrase',r'$=$',r'\uncertain{même}',r'$=$','Two separate horizontal bars occupy the word position before composante. The sign is transcribed literally; the expansion même belongs in the abbreviation list.','05',kind='abbreviation expanded or spelling modernised',marked=True,error='abbreviations expanded spelling modernised')
change('Insertion after il',r'\inserted{suffit de}','suffit de',r'\inserted{suffit de}','The two tall f strokes are fully visible in crop 15. The words are above the baseline, and the curved connector ends immediately before montrer. Crop 05 clipped the tops of these ascenders.','15',kind='insertion or placement',error='insertions put in wrong place')
change('After montrer que','',r'\uncertain{cela} \uncertain{est vrai} pour','','The next written baseline begins deux ordres totaux; there is no intervening group for cela est vrai pour. Both the end of montrer que and that next baseline are present in crop 05.','05',kind='text not on the page',marked=True,error='text not on page')
change('Insertion after par',r'\inserted{transposition des deux}',r'\uncertain{transposition} des deux',r'\inserted{transposition des deux}','The full three-word group is written on the interline above par and the following mathematical labels. Its descenders and low connecting strokes lie above the ordinary baseline.','06',kind='insertion or placement',marked=True,error='insertions put in wrong place')
change('Overworked sign before the paired labels',r'\unsure{$\varepsilon$|$\in$}','',r'\unsure{$\varepsilon$|$\in$}','There is a compact overworked sign with two small interior spaces immediately before c_i,c_{i+1}. It has no clean pair of ordinary membership bars. The ε/∈ choice remains open; H has no corresponding symbol.','06',confidence='low',kind='omission',error='omissions',consequential=True)
change('Position and abbreviation of élts',r'$c_i,c_{i+1}$ élts',r'éléments $c_i, c_{i+1}$',r'$c_i,c_{i+1}$ élts','The labels precede the following baseline’s abbreviated élts. The short letter group has the high l/t structure and terminal s; the full word éléments before the labels is not the written order. The compact +1 has a short upright/hook and is retained independently of the lower chains.','06',kind='abbreviation expanded or spelling modernised',error='abbreviations expanded spelling modernised')
change('After consécutifs','sont','','sont','A separate group begins with s, has the low o/n run and terminal t, before dans. H omits it.','06',kind='omission',error='omissions')
change('After sont dans','la',r'\uncertain{les} \uncertain{deux}','la','The source has a tall looped l followed by the low a ending; only one short word occurs before the literal equals sign. There is no second group for deux.','06',marked=True)
change('Beginning of the explanation',"Or on le voit en notant qu'on",r'Or les \uncertain{deux} \uncertain{sont} \uncertain{toujours} \uncertain{la} \uncertain{spécialisation}',"Or on le voit en notant qu'on",'The O loop is followed by on le, then voit with its final t; en notant and the q-descender/apostrophe of qu’on are distinct. H’s specialization phrase does not match these written word groups.','07',marked=True,consequential=True)
change('Following baseline','a deux morphismes de générisation','','a deux morphismes de générisation','The reduced initial a is followed by deux. Morphismes has its p-like descending stroke and final mes; générisation has the initial g loop/descender, repeated reduced syllables and final ion. These words are absent from H’s rewritten explanation.','08',kind='omission',error='omissions',consequential=True)
change('Revision before first chain',r'\deleted{de} \inserted{dans}','de',r'\deleted{\unsure{de}} \inserted{dans}','Dans is a live higher word with a visible d loop and final s. A separate lower two-letter group is struck through; de is plausible, but its e is covered. H gives live de in its text and discusses dans in an editorial note after the first drawing. That note is evidence about H, not source text, and does not preserve the separate canceled original and live replacement.','08',confidence='medium',kind='deletion state',error='struck text')
change('First drawing: strokes, gaps and endpoint',Cfig[0],Hfig[0],fig1,'Five ordinary filled vertices precede a curved, partly open right endpoint with a black upper portion. Short gaps occur after the earlier vertices, there is no ellipsis after c_3, and only two short discontinuity strokes occur farther right before the final segment. The TikZ preserves these visible distinctions. Its separately reported C/c label remains open.','09',against_C=True,kind='drawing or diagram',error='drawings and diagrams',consequential=True)
change('Letter below first left vertex',r'$C$',r'$c$',r'$\unsure{C|c}$','The isolated curved letter is larger than some subscripts but does not decisively distinguish capital C from lower-case c. C is retained first, with H’s lower-case reading explicitly possible; this comparison row does not declare H wrong.','09',confidence='low',kind='misread symbol or index',error='symbols and indices')
change('Between first and second drawings','provient de','provenant de','provient de','After prov- there is a dotted i, a low e/n run and terminal t. There is no a followed by an additional n before that t.','10')
change('Second drawing, third label',r'$c_{i+1}$',r'$c_{i+1}$',r'$c_{i-1}$','The operator is a separate horizontal stroke with no independent vertical arm. It repeats the minus in the first label; it differs from the crossed plus in the second label of the next drawing. The literal repeated index is preserved.','11',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
change('Second drawing, fourth label',r'$c_{i+2}$',r'$c_{i+2}$',r'$\unsure{c_{i-2}|c_{i+2}}$','The small operator is thickened into a horizontal wedge. Minus is preferred because no separate upright can be isolated, but the overwork prevents excluding a compact plus. Neither witness’s plus is treated as definitively disproved.','11',confidence='low',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
change('Second drawing: gaps and detached dot',Cfig[1],Hfig[1],fig2,'The left discontinuity contains three marks; the right contains four. The first and second vertices are separated from the adjacent segment ends, and a small independent dark dot lies below the first vertex. The later segments also start after visible gaps. These marks and separations are reproduced; label readings are detailed in the two preceding rows.','11',against_C=True,kind='drawing or diagram',error='drawings and diagrams')
change('Third drawing: gaps and discontinuities',Cfig[2],Hfig[2],fig3,'There are four separate labeled principal points, three marks on the left and three on the right. The joining strokes stop or start short of the points, and the final point is a short upright mark. The second and fourth labels each have a visibly crossed plus, retained independently.','12',against_C=True,kind='drawing or diagram',error='drawings and diagrams')
change('Canceled word before arête',r'\deleted{\unsure{seg}}',r'\struck{\ill{}}',r'\deleted{\unsure{seg}}','The long descending loop of the final g survives, but the s/e region is covered by cancellation. Seg remains a tentative reading, not a full decipherment of the strike; no separate abbreviation period can be securely isolated.','13',confidence='low',kind=r'readable ink left as \ill{}',marked=True,error='readable ink left as illegible')
change('Final prose, second c label',r'$c_{i+1}$',r'$c_{i+1}$',r'$\unsure{c_{i-1}|c_{i+1}}$','The tiny operator after i is an overworked horizontal wedge without a securely separate upright. Minus is preferred, while plus remains possible. The complete c_i et c-label phrase is retained in the blind box; expected adjacency does not supply the sign.','13',confidence='low',against_C=True,kind='misread symbol or index',error='symbols and indices',consequential=True)
change('Pencil foliation',r'\margin{74}','',r'\margin{74}','The pale lower-left pencil group has the top and crossing stroke of 7, then the long upright and angular lower construction of 4. It is separate foliation, not an authorial heading.','14',kind='omission',error='omissions')

inventory=[]
def item(kind,position,words,hand='his hand'):
    inventory.append(dict(scan=75,sheet_kind='text',hand=hand,element=f'{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
item('text','Main upper body, first twelve prose baselines','diagramme qui est déterminé ... deux morphismes de générisation')
item('insertion','Above I, mod; connector before mod','(défini')
item('deletion','After baseline mod','interversion, tentative under strike')
item('insertion','Above canceled interversion','transposition')
item('deletion','At end of définissent baseline','une, tentative under strike')
item('insertion','Above il montrer; connector before montrer','suffit de')
item('insertion','Above par and paired c labels','transposition des deux')
item('deletion','Lower baseline immediately before first drawing','de, tentative under strike')
item('insertion','Above canceled de before first drawing','dans')
item('drawing','First long chain across middle of page','(c_1,c_2), c_3, c_{i-1}, (c_i,c_{i+1}), c_{i+2}, c_nu; C/c below left vertex')
item('text','Left of second chain','provient de')
item('drawing','Second chain','c_{i-1}, c_i, repeated c_{i-1}, doubtful c_{i-2}|c_{i+2}; detached dot below first point')
item('text','Left of third chain','et de')
item('drawing','Third chain','c_{i-1}, c_{i+1}, c_i, c_{i+2}')
item('text','Final prose baseline','en contractant la ... qui joint c_i et doubtful c-label, OK.')
item('deletion','After la in final baseline','seg, tentative under strike')
item('insertion','Above canceled seg','arête')
item('margin note','Pencil at lower left','74',hand='pencil foliation; hand not established')

doubts=[
 dict(place='Canceled word after mod',reading=r'\deleted{\unsure{interversion}}',alternatives='interversion remains tentative; portions are obscured',confidence='low',reason='The horizontal cancellation covers central letters. Retained C doubt, not indexed in MARKS.tsv.'),
 dict(place='Canceled word after définissent',reading=r'\deleted{\unsure{une}}',alternatives='une or partially illegible canceled word',confidence='low',reason='Only small upper humps remain distinct above the thick strike. This is an added certainty-only doubt relative to C.'),
 dict(place='M1067 before paired c labels',reading=r'\unsure{$\varepsilon$|$\in$}',alternatives=r'$\varepsilon$ or $\in$',confidence='low',reason='The compact overworked mark has two interior spaces, without clean standard membership bars. Its presumed meaning does not settle its shape.'),
 dict(place='Cancellation before first chain',reading=r'\deleted{\unsure{de}}',alternatives='de or a partly obscured two-letter group',confidence='medium',reason='The d loop and short ending support de, but the cancellation covers the e. Added certainty-only doubt relative to C.'),
 dict(place='Below first drawing’s left vertex',reading=r'$\unsure{C|c}$',alternatives=r'$C$ or $c$',confidence='low',reason='An isolated open curved letter does not provide a secure case distinction. C is first only as the preferred unresolved reading.'),
 dict(place='Second drawing, fourth label',reading=r'$\unsure{c_{i-2}|c_{i+2}}$',alternatives=r'$c_{i-2}$ or $c_{i+2}$',confidence='low',reason='The horizontal wedge is too thick to exclude a small plus upright. Minus is preferred from the visible contour.'),
 dict(place='Canceled word in final prose',reading=r'\deleted{\unsure{seg}}',alternatives='seg remains tentative; first two letters obscured',confidence='low',reason='The g descender is visible, while the first letters are under the strike. Retained C doubt, unindexed in MARKS.tsv.'),
 dict(place='Final prose, second c label',reading=r'$\unsure{c_{i-1}|c_{i+1}}$',alternatives=r'$c_{i-1}$ or $c_{i+1}$',confidence='low',reason='The tiny wedge favors minus but has local overwork. The expected adjacent index does not settle the ink.'),
]

notes=[
 'The manuscript claims that the diagram is determined up to unique isomorphism by a total order on I, modulo transposition of the first two and the last two elements. This assertion is reported as source text; no independent proof was attempted.',
 'The manuscript proposes reducing the connected-component assertion for points of M^infinity_{0,nu} to orders differing by an adjacent transposition. It then says there are two generization morphisms, draws three chains, and ends by contracting the edge joining the two written c labels. This is the manuscript’s argument, not a verified specialization claim supplied by the reader.',
 'The second chain literally repeats c_{i-1} in its third position. Its fourth operator and the second index in the final prose favor minus but remain minus/plus alternatives. The two earlier paired +1 indices and the third chain’s two plus signs were inspected separately and retained from their local short upright or crossed strokes. No global normalization to the intended adjacency was made.',
 'The case of the isolated C/c under the first chain and the ε/∈ choice at M1067 remain unresolved. The cancellations interversion, une, de and seg remain tentative where the strike covers letters. All six inserted spans, all four canceled spans, and their attachment positions are represented. H’s explanatory note before the chain is editorial and is not transcribed as manuscript prose.',
 'Count: 25 physical writing units were read: 16 ordinary prose baselines, five interlinear baselines, three complete labeled drawing units, and one pencil foliation. The two early insertions “(défini” and “transposition” share an interlinear level and count once in this line total; inventory records them separately. Each drawing unit includes all its labels and marks, including the lower C/c label. Full scan and both native halves were viewed once; 15 distinct crop places were saved and read. Subsequent use of saved crops served the same first-pass decisions. No OCR, research, TeX compilation, or second reading was performed.',
 'The drawing transcriptions retain visible pen gaps, the two short discontinuity strokes in the first chain, its partly open right endpoint, and the tiny separate dark dot below the first point in the second chain. Relative positions and contours are approximated in TikZ; no extra topological conclusion is inferred from a pen gap or detached mark. H’s extra ellipsis after c_3 has no ink counterpart.',
 'Both equals signs in the prose are literal two-bar abbreviations for même; isom., él, pts and élts remain abbreviated. La before the inserted arête and the final OK. are retained as written. There is no authorial page number at the top; the separate lower-left pencil 74 is recorded with margin{}.',
 'The blind-reading boxes contain complete formulas or drawings when a symbol is in question. B05 is expanded above crop 05 to include the whole M^infinity_{0,nu} formula and the entire tall suffit de insertion, including all of crop 15; it also includes the following ordinary baseline. Diagram boxes contain exact TikZ from proposed.tex, not label-only descriptions. Every substantive comparison has an existing saved crop, including unresolved comparisons retaining C against H.'
]

second=[]
def blind(kind,box,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
blind('word disagreement',boxes['01'],'diagramme qui est déterminé, à isom. unique')
blind('word disagreement',boxes['02'],'près, en se donnant un ordre total sur')
blind('struck passage',boxes['03'],r'$I$, \inserted{(défini} mod \deleted{\unsure{interversion}} \inserted{transposition} des deux premiers él, et')
blind('struck passage',boxes['04'],r'définissent \deleted{\unsure{une}}')
blind('handwritten number',[294,525,1660,889],r"des pts de $M^\infty_{0,\nu}$ qui appartiennent à une $=$ composante connexe, il \inserted{suffit de} montrer que deux ordres totaux déduits l'un de")
blind('doubtful formula',boxes['06'],r"l'autre par \inserted{transposition des deux} \unsure{$\varepsilon$|$\in$} $c_i,c_{i+1}$ élts consécutifs sont dans la $=$ composante")
blind('word disagreement',boxes['07'],"connexe. Or on le voit en notant qu'on")
blind('word disagreement',[296,1182,1570,1305],'a deux morphismes de générisation')
blind('struck passage',[296,1305,450,1408],r'\deleted{\unsure{de}} \inserted{dans}')
blind('doubtful formula',boxes['09'],fig1)
blind('word disagreement',boxes['10'],'provient de')
blind('doubtful formula',boxes['11'],fig2)
blind('handwritten number',boxes['12'],fig3)
blind('doubtful formula',boxes['13'],closing)
blind('margin note',boxes['14'],r'\margin{74}')

date=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report=dict(
 scan=75,reader='reader_a',physical_lines_read=25,changes=changes,
 decisions=[dict(id='M1067',cote=147,scan=75,decision='undecided',reading=r'\unsure{$\varepsilon$|$\in$}',ink='The locally overworked symbol has two interior spaces. Its contour admits ε, while the strokes do not establish ordinary membership bars; ∈ remains possible. The surrounding paired c labels and their +1 index were read in full, without supplying a sign from mathematical expectation.',crop='147_scan075_place06.png and (300,878,1670,1110)',confidence='low')],
 inventory=inventory,doubts=doubts,notes=notes,
 check_events=[
  dict(statement_id='147-075-N1',date=date,who='reader_a; GPT-6 Astra Pro; inherited reasoning effort not separately exposed',type='carried as background without fault found',outcome='Read and recorded the manuscript’s unique-isomorphism/order assertion. No independent proof, computation, or structural verification was undertaken.'),
  dict(statement_id='147-075-N2',date=date,who='reader_a; GPT-6 Astra Pro; inherited reasoning effort not separately exposed',type='carried as background without fault found',outcome='Carried the connectedness/generization argument as a source assertion only. No proof that the drawn chains establish it was performed; the literal repeated index and unresolved operators are recorded in N3. Visual reading of strokes is not classified as a mathematical recheck.')
 ],
 notation=[
  dict(sign=r'$=$',reading='literal abbreviation for même',evidence='Both occurrences before composante have two separate horizontal bars.',scope='Two prose occurrences on scan 075; expansion is not put in the transcription.'),
  dict(sign=r'$c_{i-1}$',reading='literal repeated index at the third point of the second chain',evidence='Separate horizontal minus with no upright, distinct from the crossed plus signs in the next chain.',scope='This local source reading does not normalize other indices.'),
  dict(sign=r'\unsure{$\varepsilon$|$\in$}',reading='unresolved locally overworked glyph',evidence='Two small interior spaces; no clean ordinary membership bars.',scope='M1067 only; no semantic identification established.')
 ],
 hand_log=[
  dict(habit='Very reduced cursive runs still retain diagnostic descenders and terminal t strokes.',pages=[75],all_occurrences='Checked in the opening two baselines, on le voit en notant qu’on, morphismes de générisation and provient de.',witness_misreadings='H replaces several reduced groups by longer paraphrases; the visible spacing and descenders support the shorter literal readings.'),
  dict(habit='A compact plus can have only a short thick upright/hook; flat minus strokes must be distinguished locally.',pages=[75],all_occurrences='Checked both early paired +1 labels, all operators in all three drawings, and the final prose label. Two locally overworked operators remain unresolved.',witness_misreadings='C and H both give +1 at the second chain’s third point, where the source has a flat minus; their fourth-label and final-prose plus readings remain possible alternatives.'),
  dict(habit='Literal equals sign used as a prose abbreviation.',pages=[75],all_occurrences='Both positions before composante were checked and each has two bars.',witness_misreadings='H expands the first occurrence to même and preserves the second equals sign.')
 ],
 abbreviations=[dict(written='isom.',expansion='isomorphisme'),dict(written='él',expansion='éléments'),dict(written='pts',expansion='points'),dict(written='élts',expansion='éléments'),dict(written='mod',expansion='modulo'),dict(written='=',expansion='même')],
 second_boxes=second,
 unresolved=[r'M1067: \varepsilon/\in.',r'Canceled interversion, une, de and seg are not fully legible through the strikes.',r'First-chain lower label: C/c.',r'Second-chain fourth label: c_{i-2}/c_{i+2}, minus preferred.',r'Final-prose second label: c_{i-1}/c_{i+1}, minus preferred.'],
 witness_comparison='C is substantially more faithful to the prose, abbreviations and revision sequence on this page. H supplies several unsupported phrases, expands or reorders words, and replaces the generization wording with a specialization paraphrase. Both witnesses idealize the drawings and agree on a plus where the second chain literally repeats c_{i-1}; two other operators remain unresolved against both. C’s preferred lower C is retained with H’s c as an open alternative. All comparisons are grounded in the saved crops, and tentative canceled readings are not presented as resolved.'
)
(HERE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'against_C':sum(x['against_C'] for x in changes),'against_H':sum(x['against_H'] for x in changes),'inventory':len(inventory),'doubts':len(doubts),'second_boxes':len(second),'crops':len(boxes),'physical_lines_read':report['physical_lines_read']},indent=2))
