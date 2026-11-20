from pathlib import Path
import json,copy,re
O=Path(__file__).resolve().parents[1];K='156-4_070'
R=[json.loads((O/'readers'/K/f'R{i}/report.json').read_text()) for i in (1,2,3)]
P=f'readers/{K}/R1/crops/';Q=f'readers/{K}/R2/crops/';S=f'readers/{K}/R3/crops/'
t=(O/'readers'/K/'R2/reading.tex').read_text()
word=r'\unsure{toujours|en général|en position}'
middle=r'\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}'
adjective=r'\uline{comp'+middle+'bles}'
clause=r'\deleted{\unsure{quand et|on dit} que \unsure{seul|seult|sub|seulement}}'
prefix=r"\unsure{d'|\deleted{d'}}"
corrected=prefix+r'\unsure{une|un} $=$'
reporter=r'\unsure{Reporter|reporter}'
t=t.replace(r"Il n'y \unsure{aura}","Il n'y aura")
t=t.replace(r'\unsure{en général|en position}',word)
t=t.replace(r'\node[anchor=base west] at (2.95,0.03)',r'\node[anchor=base west] at (2.55,0.03)')
t=t.replace('% G1: local interlinear layout; the separate oblique arm has no supplied arrowhead.', '% G1: local interlinear layout. The long oblique stroke is drawn without an assigned function or an arrowhead; it may meet the initial letter of the following word.')
t=t.replace(r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}',adjective)
t=t.replace(r'\deleted{\unsure{quand et|on dit|c.à.d.} que \unsure{seulement|sub}}',clause)

sign=r'''\text{\unsure{\begin{tikzpicture}[baseline=-0.5ex,x=0.32cm,y=0.32cm]
\draw[line width=0.65pt] (0,0.34) .. controls (0.4,0.37) and (0.8,0.45) .. (1.05,0.86);
\draw[line width=0.3pt] (0.05,0.26) .. controls (0.5,0.29) and (1.05,0.58) .. (1.36,0.84);
\draw[line width=0.65pt] (0,0.34) .. controls (0.42,0.38) and (0.92,0.46) .. (1.18,0.12);
\draw[line width=0.65pt] (0.08,0.03) .. controls (0.48,0.16) and (0.95,0.13) .. (1.13,-0.14);
\end{tikzpicture}}}'''
oldsign=r'\begin{tikzpicture}[baseline=-0.5ex,x=0.5cm,y=0.5cm]\node at (0,0) {$\scriptstyle\unsure{\preceq}$};\draw[thin] (-0.18,0.02) -- (0.24,0.28);\end{tikzpicture}'
assert oldsign in t;t=t.replace(oldsign,sign)
t=t.replace('si deux subdivisions '+prefix,'si deux subdivision '+prefix)

old_start=t.index('% G3:')
old_end=t.index('% slanted\n\\margin{Reporter',old_start)
local=r'''% G3: on a, its two detached points, the cancelled C5 and the opening
% of the properties paragraph retain their relative positions.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base west,inner sep=0pt] at (0,0) {\deleted{on a}};
\fill (1.65,0.10) circle (0.012);
\fill (1.75,0.02) circle (0.012);
\node[anchor=base west,inner sep=0pt] at (2.30,0.10) {Je ne saurais donner};
\node[anchor=base west,inner sep=0pt] at (0,-0.48) {\deleted{\uline{C5}}};
\node[anchor=base west,inner sep=0pt] at (0,-1.00) {aucune propriété particulière de $\preceq$};
\node[anchor=base west,inner sep=0pt] at (0,-1.62) {\deleted{tout} seul. Les propriétés que j'ai en};
\node[anchor=base west,inner sep=0pt] at (0,-2.24) {vue concernent \unsure{ses|les} relations avec $\leq$.};
\end{tikzpicture}}

'''
t=t[:old_start]+local+t[old_end:]
t=t.replace(r'\margin{Reporter après C6, $C7_0$ \unsure{ces|mes} axiomes de \uline{disjonction}}',r'\margin{'+reporter+r' après C6, $C7_0$ ces axiomes \uline{de disjonction}}')
filename='J156-4-09_156-4_scan070.tex';(O/'pages'/filename).write_text(t)

d={k:copy.deepcopy(R[1][k]) for k in ['differences','c_doubts','inventory','abbreviations']}
d.update(key=K,cote='156-4',scan=70,folder='J156-4-09',their_page=69,filename=filename,brief_version='v06',check_events=[])
rows={i+1:x for i,x in enumerate(d['differences'])}
cropmap={1:P+'01_opening.jpg',2:P+'01_opening.jpg',3:P+'01_opening.jpg',4:P+'01_opening.jpg',5:P+'01_opening.jpg',6:Q+'c02_cancelled_noun.jpg',7:Q+'c03_raised_condition.jpg',8:Q+'c03_raised_condition.jpg',9:Q+'c03_raised_condition.jpg',10:Q+'c03_raised_condition.jpg',11:Q+'c04_ie_subdivisions.jpg',12:Q+'c04_ie_subdivisions.jpg',13:P+'02_first_correction.jpg',14:Q+'c04_ie_subdivisions.jpg',15:S+'05_subdivision_primes_cancelled_phrase.jpg',16:S+'05_subdivision_primes_cancelled_phrase.jpg',17:S+'04_corrected_adjective.jpg',18:S+'05_subdivision_primes_cancelled_phrase.jpg',19:P+'03_second_start.jpg',20:S+'05_subdivision_primes_cancelled_phrase.jpg',21:P+'04_diamond.jpg',22:P+'04_diamond.jpg',23:P+'05_middle_slant.jpg',24:P+'06_definition_head.jpg',25:P+'06_definition_head.jpg',26:Q+'c11_definition_corrections.jpg',27:Q+'c11_definition_corrections.jpg',28:Q+'c11_definition_corrections.jpg',29:Q+'c11_definition_corrections.jpg',30:S+'10_cancelled_label_on_a.jpg',31:S+'10_cancelled_label_on_a.jpg',32:S+'10_cancelled_label_on_a.jpg',34:P+'09_lower_para.jpg',35:Q+'c13_ses_relations.jpg',36:P+'09_lower_para.jpg',37:P+'12_lower_slant.jpg',38:P+'12_lower_slant.jpg',39:P+'12_lower_slant.jpg',40:P+'12_lower_slant.jpg',41:P+'12_lower_slant.jpg',42:P+'10_c5_abbreviation.jpg',43:P+'11_nb.jpg',44:P+'11_nb.jpg',45:P+'11_nb.jpg'}
for i,crop in cropmap.items():rows[i]['crop']=crop
rows[5].update(reading='aura',change_c=True,confidence='medium',scan_shows='After n’y the ink has an au-like low run and a distinct ra-like continuation. The two parts form aura; the latter strokes cannot be omitted as H’s lone a does. The locally separated writing does not require separate words.')
g1=t[t.index('\\figure{'):t.index('\\end{tikzpicture}}')+len('\\end{tikzpicture}}')]
nodes='\n'.join(line for line in g1.splitlines() if '\\inserted' in line)
arm=next(line for line in g1.splitlines() if line.startswith('\\draw'))
rows[8].update(reading='G1 raised-node excerpt: '+nodes,scan_shows='The pair F prime/F double prime is raised. The multiply traced relation and separate short dash occupy the same raised zone. Several close horizontal strokes leave cancellation versus retracing open; cancelled is retained as first state candidate. The excerpt quotes the two actual raised nodes, not a single continuous baseline.',consequence='The subdivision condition’s deletion state remains open. The final transcription does not turn the worked relation into a securely live or securely cancelled assertion.')
rows[9].update(reading='G1 stroke only: '+arm,scan_shows='A long oblique stroke rises rightward from beside the following word toward the raised condition. It may be an arm or an extended initial stroke. Its geometry is drawn at that position without assigning a function or adding an arrowhead. This row counts the stroke alone; lettering and relation state are separate loci.')
rows[10].update(reading=word,change_c=True,change_h=True,confidence='low',scan_shows='The descending loop and following low o/u/r/s-like run favour toujours. Its initial low run is crowded by a long rising stroke and can be segmented as en plus a second word, as R2 does. Toujours is first; C’s en général and en position remain alternatives. The choice is not made from the expected supremum assertion.',math_consequential=True,consequence='Toujours versus en général/en position changes the qualification of the claimed lack of a supremum. The preferred ink reading is retained with alternatives, not promoted to a proved or silently regularized statement.')
rows[16].update(c=r"$F',\unsure{F'''|F''}$",h=r"$F'$, $F''$",reading=r"$F',F'''$",consequence='The prose names F triple prime as its second subdivision, while the diagram’s lower node is F double prime. The mismatch is retained rather than repaired to the expected pair.')
rows[17].update(reading=adjective,change_c=True,scan_shows='The comp opening and bles ending surround one densely worked middle. Overlapping round forms, a tall crossed stem and a small high point suggest an older ati/atib and a later ara, but the layers are not independently secure. Joint alternatives also permit ata or ati without asserting a separate deleted layer. No extra whole older word is invented.',consequence='The visible revised term remains uncertain between comparables-like and compatibles/compatables-like lettering. The following explicit rejection of the word compatibles does not by itself settle the overwritten spelling.')
rows[18].update(reading=clause,scan_shows='The initial cancelled run has a loop, low humps and tall d-like end, followed by a crossed group; quand et is preferred, with on dit retained. Que has a clear descender. The final compact run begins with an s-like curve and ends in a tall stem. Seul is first, with seult, sub and a severely reduced seulement retained; the short run is not silently expanded.')
rows[20].update(c='vu que le',h='car le',reading='vu que le',scan_shows='The first group has the v/u humps, followed by a separate que with its descender and then le. H’s car replaces the entire vu que sequence; the full corresponding scope is counted here.')
diagram=t[t.index('\\diagram{'):t.index('\\end{tikzcd}}')+len('\\end{tikzcd}}')]
rows[21].update(reading=diagram,scan_shows='The one right-hand F is level with upper F prime. Lower F double prime is followed by an obliquely rising sign ending at an empty position below that F; no lower-right letter or connecting line is supplied. Left F triple prime is shared by the two arms. This row counts layout and node positions only; the worked upper-right glyph is a separate locus.',consequence='The sole right F is not moved to a central node, and the lower-right comparison is not completed by silently targeting that upper F. Literal placement and the blank endpoint are preserved.')
rows[22].update(c=r'{\scriptstyle\rlap{\ensuremath{\deleted{\unsure{\leq|\prec}}}}\preceq}',reading='D1 upper-right label: '+sign,scan_shows='One worked sign has two rising upper arms, a returning middle arm and a separate lower curve. The thin extra arm is visible, but no complete independently cancelled ≤ or prec is recoverable. The actual four strokes are drawn under a doubt mark. This row concerns the sign, not the node placement counted separately.',consequence='The overworking is preserved graphically without asserting a complete earlier relation or a secure deletion state.')
rows[26].update(location='Definition: subdivision ending and state',reading='subdivision',change_c=True,change_h=True,scan_shows='This second occurrence ends in an angular n-like return without a separate terminal s, as does the earlier noun. It lies on the ordinary baseline and is not raised as H’s add macro indicates. Singular subdivision is preserved despite deux.',confidence='high')
rows[27].update(reading=corrected,scan_shows='One heavily worked d/apostrophe position precedes a reduced une/un continuation. The initial d-like form may be live or cancelled; no second complete d’un or d’une-sized group is visible. A literal two-bar repetition mark follows. The alternatives concern the one prefix’s state, not two sequential whole words.')
rows[28].update(scan_shows='The unworked lower comparables has clear comp/ara/bles groups and a terminal stop. R2’s existing c11 crop includes the complete p descender; the clipped descender in R1 crop07 is not used as evidence of absence.')
rows[30].update(location='Cancelled on a: H first lower struck placeholder, before Je',h=r'\struck{\ill{}}',kind=r'readable ink left as \ill{}',marked_in_h='yes',scan_shows='The two short word groups under a horizontal strike stand left of the beginning Je line, before it in reading order. They read on a. This maps H’s first lower struck placeholder; it is not an additional omission from H.')
points='\n'.join(line for line in local.splitlines() if line.startswith('\\fill'))
rows[31].update(reading='G3 detached points only: '+points,scan_shows='Two separate small points fall diagonally down-right after the cancelled on a. Both are drawn at their observed offset without choosing colon or two-period punctuation. The words are counted in the preceding row.')
rows[32].update(location='Cancelled C5: H second lower struck placeholder, after donner',scan_shows='The large C and 5 retain an underline and diagonal cancellation strokes. The label lies below the Je ne saurais donner line and above/left of aucune, matching H’s second struck placeholder in reading order. Its decipherment is counted here; C’s displaced linear order is recorded separately.')
d['differences'].remove(rows[33])
rows[35]['confidence']='medium'
rows[37].update(reading=reporter,change_c=True,confidence='medium',scan_shows='The central descender returns like p and is followed by an orter-like reduced sequence, favouring Reporter/reporter over Rejeter. The initial tall swash does not securely decide capital versus lowercase. The complete rotated word is framed.')
rows[39].update(reading='ces axiomes',change_c=True,confidence='medium',scan_shows='The small raised group has an open initial curve and separate low e/s-like strokes, without the two initial humps needed for mes. Ces is accepted at medium confidence. Axiomes is fully readable on the next marginal line.')
rows[40].update(reading=r'\uline{de disjonction}',change_c=True,confidence='medium',scan_shows='The short word reads de, and disjonction ends without a separate s. The underline starts beneath the latter part of de and continues across disjonction; both words are retained in its scope. It intersects the separate long bars, which are drawn in G4. H’s des disjonctions and lack of an underline differ here.')
bars='\n'.join(line for line in t[t.index('% G4:'):].splitlines() if line.startswith('\\draw'))
rows[41].update(h='',reading='G4 bars only: '+bars,marked_in_h='no',scan_shows='Two long adjacent near-vertical strokes stand to the left of the lower axiom block. H describes them in an editorial note but does not draw them. This row counts only those strokes, not the independently collated words in their neighbouring node.')
rows[43].update(consequence='The surviving corrected letter is G. Older F-like straight strokes remain uncertain and are retained as an overwritten layer; the final letter is not forced to remain F by the earlier draft.')
rows[44]['math_consequential']=False
rows[38]['consequence']='The small closed oval is a lowered zero attached to C7; the marginal instruction refers to C7 subscript 0 rather than unindexed C7.'
placement=dict(location='Cancelled C5: position within the properties paragraph',c=r'\deleted{\uline{C5}} Je ne saurais donner aucune',h=r'Je ne saurais donner \struck{\ill{}} aucune',reading='G3 local layout excerpt: '+'\n'.join(line for line in local.splitlines() if any(s in line for s in ['Je ne saurais',r'\uline{C5}','aucune propriété'])),scan_shows='C5 is below the opening Je line and above/left of aucune. G3 retains that geometry. H’s linear placement after donner is consistent with this order, once its second placeholder is deciphered; no nonexistent extra cancelled word is alleged. This row counts C’s placement alone.',confidence='high',kind='insertion or placement',marked_in_h='yes',change_c=True,change_h=False,crop=S+'10_cancelled_label_on_a.jpg',math_consequential=False)
d['differences'].append(placement)
for i,x in enumerate(d['differences'],1):x['id']=f'A-070-D{i:03d}'

cd={i+1:x for i,x in enumerate(d['c_doubts'])}
cd[2].update(reading='D1: three ordinary '+r'\preceq'+' labels and the doubt-marked four-stroke upper-right label: '+sign,scan_shows='Three unworked bowed signs are secure. The upper-right sign is represented by its four visible strokes with a doubt mark; its earlier layer is not resolved.',crop=P+'04_diamond.jpg')
cd[4].update(scan_shows='The prime counts are 3/1/2/0. The only right F is at upper-F-prime height; the lower-right sign ends at an empty position below it. No connecting lines or additional endpoint letters are supplied.',crop=P+'04_diamond.jpg')
cd[8].update(reading='aura',status='resolved',scan_shows=rows[5]['scan_shows'],crop=rows[5]['crop'])
cd[10].update(reading=word,status='revised',scan_shows=rows[10]['scan_shows'],crop=rows[10]['crop'])
for i in (13,14):cd[i].update(reading=middle,status='revised',scan_shows=rows[17]['scan_shows'],crop=rows[17]['crop'])
cd[15].update(reading=r'\unsure{quand et|on dit}',status='revised',scan_shows=rows[18]['scan_shows'],crop=rows[18]['crop'])
cd[16].update(reading=r'\unsure{seul|seult|sub|seulement}',status='revised',scan_shows=rows[18]['scan_shows'],crop=rows[18]['crop'])
cd[19].update(reading=prefix,status='revised',scan_shows=rows[27]['scan_shows'],crop=rows[27]['crop'])
cd[20].update(reading=corrected,status='revised',scan_shows=rows[27]['scan_shows'],crop=rows[27]['crop'])
cd[21].update(reading=reporter,status='revised',scan_shows=rows[37]['scan_shows'],crop=rows[37]['crop'])
cd[22].update(reading='ces',status='resolved',scan_shows=rows[39]['scan_shows'],crop=rows[39]['crop'])
cd[26].update(c=r'\deleted{\unsure{\leq|\prec}}',reading='D1 upper-right label: '+sign,status='revised',scan_shows=rows[22]['scan_shows'],crop=rows[22]['crop'])
# Every C disposition uses an actually viewed root crop at the relevant occurrence.
for i,cp in {1:P+'01_opening.jpg',3:P+'10_c5_abbreviation.jpg; '+P+'11_nb.jpg',5:P+'02_first_correction.jpg',6:P+'10_c5_abbreviation.jpg; '+P+'11_nb.jpg',7:P+'01_opening.jpg',9:Q+'c02_cancelled_noun.jpg',11:Q+'c04_ie_subdivisions.jpg',12:S+'05_subdivision_primes_cancelled_phrase.jpg',17:P+'06_definition_head.jpg',18:P+'05_middle_slant.jpg',23:P+'10_c5_abbreviation.jpg',24:P+'11_nb.jpg',25:P+'11_nb.jpg',27:P+'11_nb.jpg',28:S+'05_subdivision_primes_cancelled_phrase.jpg',29:P+'03_second_start.jpg; '+Q+'c11_definition_corrections.jpg',30:P+'12_lower_slant.jpg',31:P+'08_deleted_labels.jpg; '+P+'09_lower_para.jpg'}.items():cd[i]['crop']=cp
cd[3]['scan_shows']='The readers each checked the full C5 relation in their lower-half reading. Root’s crops show its neighbouring abbreviation and following plain letters; the curved sign is also independently visible in the opening and properties crops. There was no C/H/reader difference at this C5 occurrence.'

remaining=[]
def doubt(loc,reading,alts,confidence,reason):remaining.append(dict(location=loc,reading=reading,alternatives=alts,confidence=confidence,reason=reason))
doubt('Opening très/trs','très',['trs'],'medium',rows[4]['scan_shows'])
doubt('Cancelled noun after de deux','éléments',['élémen'],'medium',rows[6]['scan_shows'])
doubt('Raised relation state',r'\deleted{\preceq}',[r'\preceq'],'low',rows[8]['scan_shows'])
doubt('Word after figures','toujours',['en général','en position'],'low',rows[10]['scan_shows'])
doubt('Worked middle of underlined adjective',r'\deleted{ati}ara',[r'\deleted{atib}ara','ata','ati'],'low',rows[17]['scan_shows'])
doubt('Cancelled clause first group','quand et',['on dit'],'low',rows[18]['scan_shows'])
doubt('Cancelled clause final group','seul',['seult','sub','seulement'],'low',rows[18]['scan_shows'])
doubt('Diagram upper-right worked relation','D1 four-stroke label: '+sign,['retraced upper arm','earlier overwritten relation not independently recoverable'],'low',rows[22]['scan_shows'])
doubt('Definition contrée/contrie','contrée',['contrie'],'medium',rows[24]['scan_shows'])
doubt('Definition single worked prefix',"d'",[r"\deleted{d'}"],'low',rows[27]['scan_shows'])
doubt('Definition continuation after worked prefix','une',['un'],'low',rows[27]['scan_shows'])
doubt('Before relations','ses',['les'],'medium',rows[35]['scan_shows'])
doubt('Lower note initial case','Reporter',['reporter'],'medium',rows[37]['scan_shows'])
doubt('NB older overwritten letter','F',[],'medium','Straight older-looking strokes lie within the later rounded G; their F identity remains uncertain.')
doubt('NB crossed letter after equals','X',['x'],'medium',rows[44]['scan_shows'])
d['remaining_doubts']=remaining

dis=[]
def dispute(loc,a,b,c,final,evidence,crop):dis.append(dict(location=loc,r1=a,r2=b,r3=c,final=final,evidence=evidence+' ['+crop+']'))
dispute('Aura certainty','aura',r'\unsure{aura}','aura','aura',rows[5]['scan_shows'],rows[5]['crop'])
dispute('Raised relation deletion-state preference',r'\unsure{\deleted{\preceq}|\preceq}',r'\unsure{\deleted{\preceq}|\preceq}',r'\unsure{\preceq|\deleted{\preceq}}',r'\unsure{\deleted{\preceq}|\preceq}',rows[8]['scan_shows'],rows[8]['crop'])
dispute('Long oblique stroke at raised condition','No separate drawing','Separate curved stroke in G1','No separate drawing',rows[9]['reading'],rows[9]['scan_shows'],rows[9]['crop'])
dispute('Following word',r'\unsure{toujours}',r'\unsure{en général|en position}','toujours',word,rows[10]['scan_shows'],rows[10]['crop'])
dispute('Dotted parenthetic group',r'\unsure{(i.e.|liée.}','(i.e.','(i.e.','(i.e.',rows[11]['scan_shows'],rows[11]['crop'])
dispute('Underlined adjective correction layers',adjective,R[1]['differences'][16]['reading'],R[2]['differences'][15]['reading'],adjective,rows[17]['scan_shows'],rows[17]['crop'])
dispute('Cancelled phrase',R[0]['differences'][16]['reading'],R[1]['differences'][17]['reading'],R[2]['differences'][16]['reading'],clause,rows[18]['scan_shows'],rows[18]['crop'])
dispute('Diagram lower-right target','uur to the upper-level F','ur to an empty middle-right position','uur to the upper-level F','D1 lower-right relation ends at an empty position below the sole right F',rows[21]['scan_shows'],rows[21]['crop'])
dispute('Diagram worked upper-right sign','Four-stroke TikZ drawing under doubt','Doubtful preceq plus a drawn extra arm','Alternatives include complete deleted ≤ or prec','D1 upper-right label: '+sign,rows[22]['scan_shows'],rows[22]['crop'])
dispute('Definition noun ending','subdivision','subdivisions','subdivisions','subdivision',rows[26]['scan_shows'],rows[26]['crop'])
dispute('Definition corrected prefix',r"\unsure{\deleted{d'}d'|d'}\unsure{une|un}",prefix+r'\unsure{une|un}',r"\unsure{\deleted{d'}d'une|d'une|d'un}",corrected,rows[27]['scan_shows'],rows[27]['crop'])
dispute('Two detached points',r'\unsure{..|:}','Two drawn points','Two drawn points',rows[31]['reading'],rows[31]['scan_shows'],rows[31]['crop'])
dispute('Alignment of H’s two lower struck placeholders','First on a; second C5','First C5; on a omitted; second placeholder allegedly without corresponding word','First on a; second C5','First on a; second C5',rows[30]['scan_shows']+' '+rows[32]['scan_shows'],S+'10_cancelled_label_on_a.jpg')
dispute('Cancelled C5 position','Between donner and aucune in linear text','Before Je','Margin macro before the paragraph','G3 below the Je line and above/left of aucune',placement['scan_shows'],placement['crop'])
dispute('Lower marginal instruction word/case',r'\unsure{Reporter|reporter|Rejeter|rejeter}','Reporter',r'\unsure{Reporter|reporter}',reporter,rows[37]['scan_shows'],rows[37]['crop'])
dispute('Lower marginal ces certainty','ces',r'\unsure{ces|mes}','ces','ces',rows[39]['scan_shows'],rows[39]['crop'])
dispute('Lower underline scope',r'de \uline{disjonction}',r'de \uline{disjonction}',r'de \uline{disjonction}',r'\uline{de disjonction}',rows[40]['scan_shows'],rows[40]['crop'])
dispute('NB older letter certainty',r'\deleted{F}',r'\deleted{\unsure{F}}',r'\deleted{\unsure{F}}',r'\deleted{\unsure{F}}','The straight internal strokes suggest an older F, but overlap the surviving G’s own upright and bar. The older identity remains uncertain; all three readers and the rounded outer contour support surviving G.',P+'11_nb.jpg')
d['disputes']=dis

names=['Manuscript page number','Opening paragraph','Cancelled elements noun','Raised F pair and condition','Possible cancellation of raised relation','Long oblique stroke by raised condition','Comparability paragraph','Worked adjective middle','Cancelled clause after adjective','Subdivision diagram','Upper oblique marginal note','Moderation definition','Worked d-apostrophe prefix','Cancelled Dans clause','Cancelled on a','Two detached points','Cancelled early C5','Properties paragraph','Cancelled tout','Lower oblique instruction','Pair of long C5 bars','C5 axiom and NB','Older overwritten NB letter']
for x,name in zip(d['inventory'],names):x['element']=name
d['inventory'][5]['first_words_or_objects']='G1 long oblique stroke, no assigned function or arrowhead'
d['inventory'][7]['first_words_or_objects']=middle+' within comp…bles; earlier layer uncertain'
d['inventory'][8]['first_words_or_objects']=clause
d['inventory'][9]['first_words_or_objects']='D1: F triple prime, F prime, F double prime, upper-level right F; blank lower-right endpoint; four relation positions'
d['inventory'][12]['first_words_or_objects']=prefix+'; one worked prefix, state uncertain'
d['inventory'][16]['position']='G3, below Je ne saurais donner and above/left of aucune'
d['inventory'][17]['position']='lower main paragraph reproduced in G3'
d['inventory'][19]['first_words_or_objects']=reporter+r' après C6, $C7_0$ ces axiomes \uline{de disjonction}'
d['abbreviations'].append({'form':'seult (uncertain candidate)','expansion':'seulement; only a candidate for the compact cancelled group'})
d['witness_reviews']=[
 dict(reference='H editorial note on subdivision-sign encoding',claim='H renders the curved subdivision relation with preccurlyeq.',decision='The consolidated convention retains preceq for the same observed bowed sign. Equivalent macro encoding alone is not counted as an H difference.',evidence='The opening and diagram show bent/curved arms, in contrast to the straight sign after avec. The upper-right worked occurrence is drawn separately rather than forced into an unambiguous old/new glyph sequence.',crop=P+'01_opening.jpg; '+P+'04_diamond.jpg; '+P+'09_lower_para.jpg'),
 dict(reference='H editorial notes on adjective, diagram and C5 bars',claim='H flags the overworked adjective, describes the incomplete second diagram chain and mentions two vertical bars.',decision='These editorial observations are retained as context, not manuscript words. The literal transcription still requires the worked adjective, the actual diagram arrangement and the two drawn bars.',evidence='The adjective is one worked word, the sole right F is upper-level with blank space after the lower sign, and the pair of long bars is visible beside C5. No H editorial note is inserted into the manuscript text.',crop=S+'04_corrected_adjective.jpg; '+P+'04_diamond.jpg; '+P+'12_lower_slant.jpg')
]
d['notes']={
 'summary':'The page turns to the subdivision order and contrasts it with the other order. It states the absence of extremal elements and discusses suprema and occasional infima, with an uncertain qualifier after figures. It gives a common-subdivision condition under a worked adjective, defines a moderate contrée by comparability of subdivisions, and says the author knows no particular properties of the subdivision order alone. C5 then states invariance of disjointness under subdivision, with an NB reducing the condition to point-like members using C3. These are manuscript statements, not mathematical results proved in this run.',
 'math_reading_decisions':[
  'The two different order relations prompted comparison of their actual strokes: the bowed subdivision sign is distinct from the straight sign after avec. Equivalent preceq/preccurlyeq macro choices were not counted as different readings.',
  'The prose’s second F has three primes while the diagram’s lower node has two. The mismatch is retained; it was not repaired to an expected two-subdivision pair.',
  'The only right-hand F is almost level with upper F prime; the lower-right sign ends in blank space beneath it. The diagram is not regularized into a centered diamond or completed by an inferred endpoint.',
  'The expected supremum wording did not settle toujours versus en général/en position. Toujours is first from the descending loop and following run, with the alternatives retained.',
  'The parenthetical rejection of the term compatibles did not settle the overwritten adjective. Shared comp/bles letters and joint middle-layer alternatives preserve the actual correction.',
  'The NB’s surviving G is read from its rounded outer return and spur. The older F-like layer and X/x case remain uncertain; plain M is retained.',
  'The lower instruction refers to C7 with a distinct lowered oval zero. No later axiom or external context was used to infer that suffix.'
 ],
 'author_checks':[
  'The upper oblique note says On sera amené à renforcer encore cette condition sur les contrées modérées ! This signals a planned strengthening, not a verification performed here.',
  'Je ne saurais donner aucune propriété particulière de the bowed relation, followed by struck tout and live seul, is preserved with the cancelled C5 at its physical position.',
  'The lower instruction begins Reporter/reporter and asks to move the disjunction axioms after C6 and C7 subscript 0. Its initial case remains uncertain.',
  'The NB says Il suffit de le poser ... à cause de C3. This is the author’s reduction; C3 was not independently proved or reapplied as a check.',
  'The cancelled on a and C5 account for H’s two lower struck placeholders. A preliminary phantom-word interpretation was rejected after crop-based placement comparison.'
 ],
 'title_dates_pagination':'Manuscript page 69; archive scan70. No separate title or date. The sheet carries two oblique marginal notes, the subdivision diagram, a raised condition, an overworked adjective and prefix, two detached points and the paired C5 bars.'
}
d.update(reader_crop_counts={'R1':12,'R2':16,'R3':14},adjudicator_crop_count=0,workflow_note='Three fresh independent readers used v06, each viewing whole and both halves once, then their own 12/16/14 crops. Root compared all three complete returns and viewed 20 existing crops: all12 R1; R2 c02,c03,c04,c11,c13; R3 04,05,10. No new crop was needed. An initial two-image root display was truncated and not counted; the same two files were successfully shown singly. R1 disclosed that crop07 clipped the extreme p descender of comparables; root used the already-existing complete R2 c11 crop. A text-only audit checked exact quotations, nine H ill placeholders and counting scopes. Root adopted the on a/C5 placeholder alignment supported by R1/R3 and the physical crop, dropping the preliminary phantom-placeholder claim. Graphic rows count only their named strokes/layout, not accompanying text already collated. All flags are booleans; equivalent sign macros are excluded from H totals. No OCR, external research, compilation or mathematical validation occurred.')
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['bbox_image','source']}
 if isinstance(x,list):return [clean(v) for v in x]
 if isinstance(x,str):return x.replace(str(O)+'/', '')
 return x
d=clean(d);(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':K,'differences':len(d['differences']),'C':sum(x['change_c'] for x in d['differences']),'H':sum(x['change_h'] for x in d['differences']),'disputes':len(dis),'remaining':len(remaining),'inventory':len(d['inventory'])}))
